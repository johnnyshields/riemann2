#!/usr/bin/env python3
"""
packet_frequency_stress.py
--------------------------

Packet-frequency determinant stress-test harness for the ordinary Wronskian
route. Tests Z_alpha(m) ~ 0 and Wtilde_R(m, alpha) ~ 0 on prime-only blocks

    B_pf = {p : c Q <= log p <= c Q + Q/R}

across stages:

    relaxed             plus branch only, independent random phases (negative control)
    main_orbit          plus branch only, one-parameter orbit u_p = exp(-i m log p)
    b2                  plus branch + canonical B_2 background (b2_canonical.B2_fast_3term)
    formal_dual         plus + reflected log-derivative minus branch, plateau smoothing
    actual_like_dual    plus + reflected log-derivative minus branch, configured smoothing/conductor
    e2                  row perturbation test on the actual_like_dual matrix

Conventions (from Agent 4/Agent 6 audit):
    A(s)   = -zeta'(s)/zeta(s)
    C_k(s) = (-1)^k d_s^k A(s)
    Reflected dual: sigma_k = (-1)^(k+1), no chi(s) multiplier.
    Operator node != folded conductor node.
    Defaults: k_Z=0, k_q=3 (script convention); k_q=2 for literal q''_can.

Output: one CSV row per (R, c, alpha, stage) candidate. Filename suffixed
with a 12-char params hash; resume by row-key dedupe is on by default.

Reuses scripts/zeta_bridge_agent2/b2_canonical.py and
scripts/zeta_bridge_shared/afe_logderiv_weights.py via sys.path injection.
"""

from __future__ import annotations

# Pin BLAS / OpenMP to 1 thread per process before numpy import — we
# parallelize at the (R, c, alpha) level via multiprocessing.
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import csv
import dataclasses
import hashlib
import json
import math
import multiprocessing as _mp
import sys
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

try:
    import scipy.optimize as _opt
except Exception:
    _opt = None

try:
    import sympy as sp
except Exception:
    sp = None


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))
_AGENT2_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "zeta_bridge_agent2"))
_SHARED_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "zeta_bridge_shared"))
for _d in (_AGENT2_DIR, _SHARED_DIR):
    if _d not in sys.path:
        sys.path.insert(0, _d)

from b2_canonical import B2_fast_3term  # noqa: E402  (agent2 source of truth)
from afe_logderiv_weights import (  # noqa: E402
    build_logderiv_weights,
    conductor_cover_block,
    conductor_sqrt_m,
)


SCHEMA_VERSION = 3  # v3: m_min guard for actual_like_dual / e2 (corner_artifact
                    # class); m parameter threaded into classify().
                    # v2: B_2 at m (not u_0); B_2 in dual stages; b2_toy label;
                    # filled op_node fields; sqrt_m guard.
EPS = 1e-300


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def _default_out(*parts: str) -> str:
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


# ============================================================
# Data structures
# ============================================================

@dataclass
class PrimeBlock:
    R: int
    Q: float
    c: float
    lam: float
    u_min: float
    u_max: float
    u0: float
    L: float
    primes: np.ndarray
    logs: np.ndarray

    @property
    def lambda_u0(self) -> float:
        return self.lam * self.u0

    @property
    def lambda_L(self) -> float:
        return self.lam * self.L


@dataclass
class TermSet:
    z_coeffs: np.ndarray
    c_coeffs: np.ndarray
    z_phases: np.ndarray
    c_phases: np.ndarray
    op_nodes_z: np.ndarray
    op_nodes_c: np.ndarray
    branch_labels_z: List[str]
    branch_labels_c: List[str]


@dataclass
class Basis:
    Phi_z: np.ndarray
    Phi_c: np.ndarray
    x_z: np.ndarray
    x_c: np.ndarray
    x_center: float
    x_halfwidth: float
    kappa_basis: float
    gram_error: float


@dataclass
class Diagnostics:
    eta_Z: float
    log_eta_Z: float
    eta_W: float
    log_eta_W: float
    eta_sv: float
    sigma_min: float
    sigma_max: float
    row_norm_min: float
    row_norm_max: float
    rho_rank_2: float
    rho_rank_inf: float
    kappa_basis: float
    gram_error: float
    objective_value: float
    op_node_min: float
    op_node_max: float
    diam_x: float


@dataclass
class CandidateRow:
    run_id: str
    timestamp: str
    config_name: str
    stage: str
    R: int
    Q: float
    lambda_: float
    c: float
    u_min: float
    u_max: float
    u0: float
    L: float
    num_primes: int
    alpha: float
    m: float
    lambda_u0: float
    lambda_L: float
    op_node_min: float
    op_node_max: float
    diam_x: float
    eta_Z: float
    log_eta_Z: float
    eta_W: float
    log_eta_W: float
    eta_sv: float
    rho_rank_2: float
    rho_rank_inf: float
    kappa_basis: float
    gram_error: float
    eta_E2_det: float
    row_norm_min: float
    row_norm_max: float
    sigma_min: float
    sigma_max: float
    objective_value: float
    collapse_class: str
    notes: str
    k_Z: int
    k_q: int
    source_mode: str
    smoothing: str
    conductor_policy: str
    dual_type: str = ""
    dual_node_convention: str = "operator_signed"
    num_dual_terms: int = 0
    E2_model: str = ""
    E2_trials: int = 0
    eta_W_median_perturbed: float = float("nan")
    eta_W_worst_perturbed: float = float("nan")
    eta_W_best_perturbed: float = float("nan")
    survives_E2: bool = False


CSV_FIELDS = list(CandidateRow.__dataclass_fields__.keys())

_ROW_KEY_FIELDS = ("config_name", "stage", "R", "c", "alpha", "k_Z", "k_q",
                   "smoothing", "conductor_policy")


def _row_key(row: CandidateRow) -> tuple:
    return tuple(getattr(row, f) for f in _ROW_KEY_FIELDS)


def _row_key_from_dict(d: dict) -> tuple:
    out = []
    for f in _ROW_KEY_FIELDS:
        v = d.get(f, "")
        if f in ("R",):
            v = int(float(v))
        elif f in ("c", "alpha", "k_Z", "k_q"):
            try:
                v = float(v)
            except Exception:
                pass
        out.append(v)
    return tuple(out)


# ============================================================
# Config / params hash / output path
# ============================================================

def load_config(path: Optional[str]) -> Dict[str, Any]:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def compute_params_hash(cfg: Dict[str, Any], config_name: str) -> str:
    record = {
        "schema_version": SCHEMA_VERSION,
        "config_name": config_name,
        # everything that can affect row math
        "Q_mode": cfg.get("Q_mode", "toy"),
        "R_values": [int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12])],
        "c_values": [float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])],
        "stages": list(cfg.get("stages", ["relaxed", "main_orbit"])),
        "k_Z": int(cfg.get("k_Z", 0)),
        "k_q": int(cfg.get("k_q", 3)),
        "smoothing": cfg.get("smoothing", "plateau"),
        "conductor_policy": cfg.get("conductor_policy", "plateau"),
        "m_grid": int(cfg.get("m_grid", 1000)),
        "m_min": float(cfg.get("m_min", 0.0)),
        "m_max_factor": float(cfg.get("m_max_factor", 100.0)),
        "relaxed_restarts": int(cfg.get("relaxed_restarts", 64)),
        "relaxed_m": float(cfg.get("relaxed_m", 0.0)),
        "max_primes": int(cfg.get("max_primes", 5000)),
        "min_primes_factor": int(cfg.get("min_primes_factor", 4)),
        "E2_trials": int(cfg.get("E2_trials", 200)),
        "E2_scale": float(cfg.get("E2_scale", 1e-8)),
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_W": float(cfg.get("C_W", 6.0)),
        "C_rank": float(cfg.get("C_rank", 4.0)),
        "C_kappa": float(cfg.get("C_kappa", 4.0)),
        "seed": int(cfg.get("seed", 12345)),
        "alpha_grid_mode": cfg.get("alpha_grid_mode", "default"),
        "include_B2_in_dual": bool(cfg.get("include_B2_in_dual", True)),
    }
    blob = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def derive_output_path(stem: str, params_hash: str, hash_len: int = 12) -> str:
    short = params_hash[:hash_len]
    head, ext = os.path.splitext(stem)
    return f"{head}.{short}{ext}" if ext else f"{head}.{short}"


def load_existing_keys(csv_path: str) -> set:
    keys: set = set()
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        return keys
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            try:
                keys.add(_row_key_from_dict(row))
            except Exception:
                continue
    return keys


# ============================================================
# Block construction
# ============================================================

def primes_in_interval(lo: int, hi: int, max_count: Optional[int] = None) -> List[int]:
    lo = max(2, int(lo))
    hi = int(hi)
    if lo > hi:
        return []
    if sp is not None:
        out: List[int] = []
        for p in sp.primerange(lo, hi + 1):
            out.append(int(p))
            if max_count and len(out) >= max_count:
                break
        return out

    # Trivial fallback (small intervals only).
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d += 2
        return True
    out = []
    for n in range(lo, hi + 1):
        if is_prime(n):
            out.append(n)
            if max_count and len(out) >= max_count:
                break
    return out


def choose_Q_for_R(R: int, mode: str) -> float:
    if mode == "toy":
        return float(20 + 2 * R)
    if mode == "larger_toy":
        return float(40 + 3 * R)
    if mode.startswith("fixed:"):
        return float(mode.split(":", 1)[1])
    raise ValueError(f"unknown Q mode: {mode}")


def build_prime_block(R: int, Q: float, c: float, max_primes: int) -> PrimeBlock:
    lam = 1.0 / Q
    u_min = c * Q
    u_max = c * Q + Q / R
    u0 = 0.5 * (u_min + u_max)
    L = u_max - u_min
    p_min = int(math.ceil(math.exp(u_min)))
    p_max = int(math.floor(math.exp(u_max)))
    ps = primes_in_interval(p_min, p_max, max_count=max_primes)
    arr = np.asarray(ps, dtype=np.float64)
    logs = np.log(arr) if len(arr) else np.asarray([], dtype=float)
    return PrimeBlock(R=R, Q=Q, c=c, lam=lam, u_min=u_min, u_max=u_max,
                      u0=u0, L=L, primes=arr, logs=logs)


# ============================================================
# Basis & matrix
# ============================================================

def cheb_vander(x: np.ndarray, degree: int) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    A = np.zeros((len(x), degree + 1), dtype=float)
    if degree >= 0:
        A[:, 0] = 1.0
    if degree >= 1:
        A[:, 1] = x
    for j in range(2, degree + 1):
        A[:, j] = 2 * x * A[:, j - 1] - A[:, j - 2]
    return A


def normalize_nodes(op_nodes: np.ndarray) -> Tuple[np.ndarray, float, float]:
    mn = float(np.min(op_nodes))
    mx = float(np.max(op_nodes))
    center = 0.5 * (mn + mx)
    half = 0.5 * (mx - mn)
    if half <= 0:
        half = 1.0
    return (op_nodes - center) / half, center, half


def build_basis(op_nodes_z: np.ndarray, op_nodes_c: np.ndarray,
                weights_c: np.ndarray, degree: int) -> Basis:
    x_c, center, half = normalize_nodes(op_nodes_c)
    x_z = (op_nodes_z - center) / half
    A_c = cheb_vander(x_c, degree)
    Aw = np.sqrt(weights_c)[:, None] * A_c
    Qmat, Rmat = np.linalg.qr(Aw, mode="reduced")
    Phi_c = Qmat / np.sqrt(weights_c)[:, None]
    invR = np.linalg.inv(Rmat)
    Phi_z = cheb_vander(x_z, degree) @ invR
    Gram = Phi_c.conj().T @ (weights_c[:, None] * Phi_c)
    gram_error = float(np.linalg.norm(Gram - np.eye(degree + 1), ord=2))
    kappa = float(np.linalg.cond(Rmat))
    return Basis(Phi_z=Phi_z, Phi_c=Phi_c, x_z=x_z, x_c=x_c,
                 x_center=center, x_halfwidth=half,
                 kappa_basis=kappa, gram_error=gram_error)


def build_M(terms: TermSet, basis: Basis, R: int,
            b2_value: Optional[float] = None) -> np.ndarray:
    d = R + 2
    M = np.zeros((d, d), dtype=np.complex128)
    z_w = terms.z_coeffs * terms.z_phases
    c_w = terms.c_coeffs * terms.c_phases
    Phi_c = basis.Phi_c  # shape (n, R+2)
    # Z row: M[0, l] = sum_n z_n * Phi_l(x_z_n) * exp(-i m log n)
    M[0, :] = (basis.Phi_z * z_w[:, None]).sum(axis=0)
    # Source rows (j=0..R, l=0..R+1):
    #   M[j+1, l] = sum_n c_n * Phi_c[n, j] * Phi_c[n, l] * phase_n
    #            = (Phi_c[:, :R+1].T @ (Phi_c * c_w[:, None]))[j, l]
    weighted_Phi = Phi_c * c_w[:, None]
    M[1:, :] = Phi_c[:, : R + 1].T @ weighted_Phi  # (R+1, R+2)
    if b2_value is not None:
        for row in range(1, d):
            M[row, 0] += b2_value
    return M


# ============================================================
# Diagnostics
# ============================================================

def eta_Z_direct(terms: TermSet) -> Tuple[float, float]:
    Z = np.sum(terms.z_coeffs * terms.z_phases)
    denom = float(np.linalg.norm(terms.z_coeffs))
    eta = float(abs(Z) / max(denom, EPS))
    return eta, math.log(max(eta, EPS))


def det_diagnostics(M: np.ndarray) -> Dict[str, float]:
    s = np.linalg.svd(M, compute_uv=False)
    rows = np.linalg.norm(M, axis=1)
    log_eta_W = float(
        np.sum(np.log(np.maximum(s, EPS))) -
        np.sum(np.log(np.maximum(rows, EPS)))
    )
    return {
        "eta_W": float(math.exp(max(log_eta_W, math.log(EPS)))),
        "log_eta_W": log_eta_W,
        "eta_sv": float(s[-1] / max(s[0], EPS)),
        "sigma_min": float(s[-1]),
        "sigma_max": float(s[0]),
        "row_norm_min": float(np.min(rows)),
        "row_norm_max": float(np.max(rows)),
    }


def symbol_rank_residual(x: np.ndarray, r: np.ndarray, weights: np.ndarray, R: int) -> Tuple[float, float]:
    V = cheb_vander(x, R)
    Vw = np.sqrt(weights)[:, None] * V
    rw = np.sqrt(weights) * r
    coeff, *_ = np.linalg.lstsq(Vw, rw, rcond=None)
    fit = V @ coeff
    resid = r - fit
    return (float(np.sqrt(np.sum(weights * np.abs(resid) ** 2))),
            float(np.max(np.abs(resid))))


# ============================================================
# Term construction per stage
# ============================================================

def get_N(policy: str, n_values: np.ndarray, m: float) -> Optional[float]:
    if policy in ("plateau", "none"):
        return None
    if policy == "cover_block":
        return conductor_cover_block(n_values, y_at_max=0.5)
    if policy == "sqrt_m":
        # Clamp to m >= 1 so the orbit grid's m=0 starting point doesn't
        # crash sqrt_m configs. sqrt_m at the clamp value is just a small
        # conductor, which the bump cuts off harmlessly.
        return conductor_sqrt_m(max(float(m), 1.0))
    raise ValueError(f"unknown conductor policy: {policy}")


def build_terms(block: PrimeBlock, m: float, alpha: float, include_dual: bool,
                k_Z: int, k_q: int, smoothing: str, conductor_policy: str) -> TermSet:
    n_values = block.primes.astype(int)
    N_Z = get_N(conductor_policy, n_values, m)
    N_q = get_N(conductor_policy, n_values, m)

    zp = build_logderiv_weights(n_values, m=m, alpha=alpha, branch="plus",
                                k=k_Z, N=N_Z, smoothing=smoothing)
    cp = build_logderiv_weights(n_values, m=m, alpha=0.0, branch="plus",
                                k=k_q, N=N_q, smoothing=smoothing)

    z_coeffs = [zp.coeffs]
    z_phases = [zp.phases]
    z_nodes = [zp.op_nodes]
    z_labels = ["plus"] * len(zp.coeffs)
    c_coeffs = [cp.coeffs]
    c_phases = [cp.phases]
    c_nodes = [cp.op_nodes]
    c_labels = ["plus"] * len(cp.coeffs)

    if include_dual:
        zm = build_logderiv_weights(n_values, m=m, alpha=alpha, branch="minus",
                                    k=k_Z, N=N_Z, smoothing=smoothing)
        cm = build_logderiv_weights(n_values, m=m, alpha=0.0, branch="minus",
                                    k=k_q, N=N_q, smoothing=smoothing)
        z_coeffs.append(zm.coeffs); z_phases.append(zm.phases); z_nodes.append(zm.op_nodes)
        c_coeffs.append(cm.coeffs); c_phases.append(cm.phases); c_nodes.append(cm.op_nodes)
        z_labels += ["minus"] * len(zm.coeffs)
        c_labels += ["minus"] * len(cm.coeffs)

    return TermSet(
        z_coeffs=np.concatenate(z_coeffs),
        c_coeffs=np.concatenate(c_coeffs),
        z_phases=np.concatenate(z_phases),
        c_phases=np.concatenate(c_phases),
        op_nodes_z=np.concatenate(z_nodes),
        op_nodes_c=np.concatenate(c_nodes),
        branch_labels_z=z_labels,
        branch_labels_c=c_labels,
    )


def evaluate_terms(block: PrimeBlock, terms: TermSet, R: int,
                   include_b2: bool,
                   m: Optional[float] = None) -> Tuple[Diagnostics, np.ndarray, Basis]:
    """
    `m` is the height (the spectral parameter), not the block center.
    B_2 must be evaluated at m, not at u_0. When `m` is None (e.g. relaxed
    stage), include_b2 is silently disabled.
    """
    weights_c = np.maximum(np.abs(terms.c_coeffs) ** 2, EPS)
    basis = build_basis(terms.op_nodes_z, terms.op_nodes_c, weights_c, degree=R + 1)

    if include_b2 and m is not None and math.isfinite(m) and m > 0:
        b2 = B2_fast_3term(float(m))
    else:
        b2 = None
    M = build_M(terms, basis, R, b2_value=b2)
    eta_z, log_eta_z = eta_Z_direct(terms)
    dd = det_diagnostics(M)
    # Two-branch rank residual on source nodes; plus and minus included
    # whenever dual is active in `terms`.
    r = terms.z_coeffs / np.where(np.abs(terms.c_coeffs) > EPS,
                                  terms.c_coeffs, EPS)
    w = weights_c
    rho2, rhoinf = symbol_rank_residual(basis.x_c, r, w, R)

    op_min = float(np.min(terms.op_nodes_c))
    op_max = float(np.max(terms.op_nodes_c))
    diam_x = float(np.max(basis.x_c) - np.min(basis.x_c))

    diag = Diagnostics(
        eta_Z=eta_z, log_eta_Z=log_eta_z,
        eta_W=dd["eta_W"], log_eta_W=dd["log_eta_W"], eta_sv=dd["eta_sv"],
        sigma_min=dd["sigma_min"], sigma_max=dd["sigma_max"],
        row_norm_min=dd["row_norm_min"], row_norm_max=dd["row_norm_max"],
        rho_rank_2=rho2, rho_rank_inf=rhoinf,
        kappa_basis=basis.kappa_basis, gram_error=basis.gram_error,
        objective_value=eta_z ** 2 + dd["eta_W"] ** 2,
        op_node_min=op_min, op_node_max=op_max, diam_x=diam_x,
    )
    return diag, M, basis


# ============================================================
# Search routines
# ============================================================

def relaxed_search(block: PrimeBlock, alpha: float, cfg: Dict[str, Any],
                   restarts: int, seed: int) -> Tuple[float, Diagnostics, np.ndarray]:
    rng = np.random.default_rng(seed)
    m0 = float(cfg.get("relaxed_m", max(1.0, block.Q)))
    base_terms = build_terms(block, m=m0, alpha=alpha, include_dual=False,
                             k_Z=int(cfg.get("k_Z", 0)),
                             k_q=int(cfg.get("k_q", 3)),
                             smoothing=str(cfg.get("smoothing", "plateau")),
                             conductor_policy=str(cfg.get("conductor_policy", "plateau")))
    n_z = len(base_terms.z_coeffs)
    n_c = len(base_terms.c_coeffs)
    best: Optional[Tuple[Diagnostics, np.ndarray]] = None
    for _ in range(restarts):
        z_phase = np.exp(-1j * rng.uniform(0, 2 * np.pi, size=n_z))
        c_phase = np.exp(-1j * rng.uniform(0, 2 * np.pi, size=n_c))
        terms = dataclasses.replace(base_terms, z_phases=z_phase, c_phases=c_phase)
        # Relaxed phases destroy the m-dependence in coefficients we built,
        # so leaving include_b2=False is correct here regardless.
        diag, M, _basis = evaluate_terms(block, terms, block.R, include_b2=False, m=None)
        if best is None or diag.objective_value < best[0].objective_value:
            best = (diag, M)
    assert best is not None
    return float("nan"), best[0], best[1]


def scan_orbit_grid(block: PrimeBlock, alpha: float, cfg: Dict[str, Any],
                    include_dual: bool, include_b2: bool,
                    grid_size: int,
                    smoothing_override: Optional[str] = None,
                    conductor_override: Optional[str] = None,
                    ) -> Tuple[float, Diagnostics, np.ndarray]:
    """Sweep m on a grid; return (best_m, best_diag, best_M).

    If `smoothing_override` / `conductor_override` are given, they replace
    the cfg-level smoothing / conductor_policy for this stage only — used
    by `formal_dual` to force plateau geometry while leaving the configured
    smoothing for `actual_like_dual`.
    """
    m_min = float(cfg.get("m_min", 0.0))
    m_max = float(cfg.get("m_max_factor", 100.0)) * block.Q
    k_Z = int(cfg.get("k_Z", 0))
    k_q = int(cfg.get("k_q", 3))
    smoothing = smoothing_override or str(cfg.get("smoothing", "plateau"))
    conductor_policy = conductor_override or str(cfg.get("conductor_policy", "plateau"))

    best: Optional[Tuple[Diagnostics, np.ndarray]] = None
    best_m = m_min
    for m in np.linspace(m_min, m_max, grid_size):
        m_f = float(m)
        terms = build_terms(block, m=m_f, alpha=alpha, include_dual=include_dual,
                            k_Z=k_Z, k_q=k_q,
                            smoothing=smoothing, conductor_policy=conductor_policy)
        diag, M, _basis = evaluate_terms(block, terms, block.R,
                                         include_b2=include_b2, m=m_f)
        if best is None or diag.objective_value < best[0].objective_value:
            best = (diag, M)
            best_m = m_f
    assert best is not None
    return best_m, best[0], best[1]


def E2_perturbation(M: np.ndarray, trials: int, scale: float, seed: int) -> Dict[str, Any]:
    rng = np.random.default_rng(seed)
    row_norms = np.linalg.norm(M, axis=1)
    eta_rows = scale * np.maximum(row_norms, EPS)
    base_eta_W = det_diagnostics(M)["eta_W"]
    vals = []
    d = M.shape[0]
    for _ in range(trials):
        dM = np.zeros_like(M)
        for j, eta in enumerate(eta_rows):
            v = rng.normal(size=d) + 1j * rng.normal(size=d)
            v /= max(np.linalg.norm(v), EPS)
            dM[j, :] = eta * v
        vals.append(det_diagnostics(M + dM)["eta_W"])
    return {
        "E2_model": "row_perturbation",
        "E2_trials": trials,
        "eta_W_median_perturbed": float(np.median(vals)),
        "eta_W_worst_perturbed": float(np.max(vals)),
        "eta_W_best_perturbed": float(np.min(vals)),
        "survives_E2": bool(np.median(vals) <= 10.0 * base_eta_W),
    }


# ============================================================
# Classification
# ============================================================

def classify(stage: str, Q: float, diag: Diagnostics, survives_E2: bool,
             cfg: Dict[str, Any], m: float = float("nan")) -> str:
    """
    Stage labels:
      relaxed          -> phase-relaxed negative control
      main_orbit       -> plus-only one-parameter orbit
      b2_toy           -> main_orbit + crude scalar B_2 injection (toy_diagnostic only)
      formal_dual      -> plus + reflected minus, plateau geometry, B_2 included if cfg
      actual_like_dual -> plus + reflected minus, configured geometry, B_2 included if cfg
      e2               -> row perturbation on actual_like_dual

    Corner guard: m <= 0 is not an admissible RH-height stress point. For
    actual_like_dual and e2 stages, any candidate at m <= 0 is reported
    as "corner_artifact" regardless of eta_Z / eta_W magnitudes.
    """
    if stage in {"actual_like_dual", "e2"} and (math.isfinite(m) and m <= 0):
        return "corner_artifact"

    CZ = float(cfg.get("C_Z", 6.0))
    CW = float(cfg.get("C_W", 6.0))
    CR = float(cfg.get("C_rank", 4.0))
    CK = float(cfg.get("C_kappa", 4.0))
    healthy = (diag.rho_rank_2 >= Q ** (-CR)) and (diag.kappa_basis <= Q ** CK)
    collapsed = (diag.eta_Z <= Q ** (-CZ)) and (diag.eta_W <= Q ** (-CW))

    if stage == "b2_toy":
        # Crude scalar injection is not a canonical Wronskian B_2 action;
        # never produce Yellow/Red from this stage. See script docstring
        # and audit notes for the planned `b2_operator` upgrade.
        return "toy_diagnostic"

    if not healthy:
        return "degenerate"
    if stage == "relaxed" and collapsed:
        return "relaxed_only_possible"
    if stage == "main_orbit" and collapsed:
        return "yellow_orbit_collapse"
    if stage == "formal_dual" and collapsed:
        return "red_candidate_pre_E2"
    if stage == "actual_like_dual" and collapsed:
        return "red_candidate_pre_E2"
    if stage == "e2" and collapsed and survives_E2:
        return "red_collapse"
    return "no_collapse"


# ============================================================
# Row construction
# ============================================================

def make_row(run_id: str, config_name: str, block: PrimeBlock, stage: str,
             alpha: float, m: float, diag: Diagnostics, M: Optional[np.ndarray],
             cfg: Dict[str, Any], notes: str,
             include_dual: bool,
             e2: Optional[Dict[str, Any]] = None,
             num_dual_terms: int = 0) -> CandidateRow:
    e2 = e2 or {}
    survives = bool(e2.get("survives_E2", False))
    op_min = float(diag.op_node_min)
    op_max = float(diag.op_node_max)
    diam_x = float(diag.diam_x)
    return CandidateRow(
        run_id=run_id,
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        config_name=config_name,
        stage=stage,
        R=block.R, Q=block.Q, lambda_=block.lam, c=block.c,
        u_min=block.u_min, u_max=block.u_max, u0=block.u0, L=block.L,
        num_primes=int(len(block.primes)),
        alpha=float(alpha), m=float(m),
        lambda_u0=block.lambda_u0, lambda_L=block.lambda_L,
        op_node_min=op_min, op_node_max=op_max, diam_x=diam_x,
        eta_Z=diag.eta_Z, log_eta_Z=diag.log_eta_Z,
        eta_W=diag.eta_W, log_eta_W=diag.log_eta_W, eta_sv=diag.eta_sv,
        rho_rank_2=diag.rho_rank_2, rho_rank_inf=diag.rho_rank_inf,
        kappa_basis=diag.kappa_basis, gram_error=diag.gram_error,
        eta_E2_det=float("nan"),
        row_norm_min=diag.row_norm_min, row_norm_max=diag.row_norm_max,
        sigma_min=diag.sigma_min, sigma_max=diag.sigma_max,
        objective_value=diag.objective_value,
        collapse_class=classify(stage, block.Q, diag, survives, cfg, m=float(m)),
        notes=notes,
        k_Z=int(cfg.get("k_Z", 0)),
        k_q=int(cfg.get("k_q", 3)),
        source_mode=str(cfg.get("source_mode", "script_kq3")),
        smoothing=str(cfg.get("smoothing", "plateau")),
        conductor_policy=str(cfg.get("conductor_policy", "plateau")),
        dual_type=("reflected_logderiv" if include_dual else ""),
        dual_node_convention="operator_signed",
        num_dual_terms=int(num_dual_terms),
        E2_model=str(e2.get("E2_model", "")),
        E2_trials=int(e2.get("E2_trials", 0)),
        eta_W_median_perturbed=float(e2.get("eta_W_median_perturbed", float("nan"))),
        eta_W_worst_perturbed=float(e2.get("eta_W_worst_perturbed", float("nan"))),
        eta_W_best_perturbed=float(e2.get("eta_W_best_perturbed", float("nan"))),
        survives_E2=survives,
    )


# ============================================================
# Per-task worker
# ============================================================

def _process_one_task(task: tuple) -> List[CandidateRow]:
    """One task = one (R, c, alpha) triple. Builds the block once and runs all
    requested stages inside the worker. Returns a list of CandidateRow."""
    (run_id, config_name, R, c_val, alpha, cfg) = task
    rows: List[CandidateRow] = []

    Q = choose_Q_for_R(R, str(cfg.get("Q_mode", "toy")))
    block = build_prime_block(R=R, Q=Q, c=c_val, max_primes=int(cfg.get("max_primes", 5000)))
    if len(block.primes) < int(cfg.get("min_primes_factor", 4)) * (R + 2):
        return rows

    stages = list(cfg.get("stages", ["relaxed", "main_orbit"]))
    # B_2 in dual stages: per the audit, the canonical Red/Green ladder is
    # +B_2 -> +dual -> +E_2, so dual stages should include B_2 by default.
    include_B2_in_dual = bool(cfg.get("include_B2_in_dual", True))
    grid_size = int(cfg.get("m_grid", 1000))
    seed = int(cfg.get("seed", 12345)) + int(R) * 1000 + int(round(c_val * 100)) * 17 + int(round(alpha * 13))

    # Stage: relaxed (negative control)
    if "relaxed" in stages:
        m_r, diag_r, M_r = relaxed_search(block, alpha, cfg,
                                          restarts=int(cfg.get("relaxed_restarts", 64)),
                                          seed=seed)
        rows.append(make_row(run_id, config_name, block, "relaxed", alpha, m_r,
                             diag_r, M_r, cfg, "phase-relaxed negative control",
                             include_dual=False))

    # Stage: main_orbit (plus-only orbit)
    if "main_orbit" in stages:
        m, diag, M = scan_orbit_grid(block, alpha, cfg,
                                     include_dual=False, include_b2=False,
                                     grid_size=grid_size)
        rows.append(make_row(run_id, config_name, block, "main_orbit", alpha, m,
                             diag, M, cfg, "main-only orbit", include_dual=False))

    # Stage: b2_toy (main_orbit + crude scalar B_2(m) injection — diagnostic only)
    if "b2_toy" in stages or "b2" in stages:
        m, diag, M = scan_orbit_grid(block, alpha, cfg,
                                     include_dual=False, include_b2=True,
                                     grid_size=grid_size)
        rows.append(make_row(run_id, config_name, block, "b2_toy", alpha, m,
                             diag, M, cfg, "B2 toy scalar injection (diagnostic only)",
                             include_dual=False))

    # Stage: formal_dual (plus + reflected minus, plateau geometry forced;
    # B_2(m) included by default).
    if "formal_dual" in stages:
        m, diag, M = scan_orbit_grid(block, alpha, cfg,
                                     include_dual=True,
                                     include_b2=include_B2_in_dual,
                                     grid_size=grid_size,
                                     smoothing_override="plateau",
                                     conductor_override="plateau")
        rows.append(make_row(run_id, config_name, block, "formal_dual", alpha, m,
                             diag, M, cfg,
                             "reflected dual (plateau forced) + B_2"
                             if include_B2_in_dual else
                             "reflected dual (plateau forced) without B_2",
                             include_dual=True, num_dual_terms=2 * len(block.primes)))

    # Stage: actual_like_dual (configured smoothing/conductor; B_2(m) included by default)
    M_actual: Optional[np.ndarray] = None
    diag_actual: Optional[Diagnostics] = None
    m_actual: float = float("nan")
    if "actual_like_dual" in stages:
        m_actual, diag_actual, M_actual = scan_orbit_grid(
            block, alpha, cfg,
            include_dual=True, include_b2=include_B2_in_dual,
            grid_size=grid_size)
        rows.append(make_row(run_id, config_name, block, "actual_like_dual",
                             alpha, m_actual, diag_actual, M_actual, cfg,
                             "reflected dual (configured) + B_2"
                             if include_B2_in_dual else
                             "reflected dual (configured) without B_2",
                             include_dual=True, num_dual_terms=2 * len(block.primes)))

    # Stage: e2 (row perturbation on actual_like_dual M; B_2 already baked in)
    if "e2" in stages and M_actual is not None and diag_actual is not None:
        e2 = E2_perturbation(M_actual,
                             trials=int(cfg.get("E2_trials", 200)),
                             scale=float(cfg.get("E2_scale", 1e-8)),
                             seed=seed + 7)
        rows.append(make_row(run_id, config_name, block, "e2", alpha, m_actual,
                             diag_actual, M_actual, cfg,
                             "E2 row perturbation on actual_like_dual",
                             include_dual=True, e2=e2,
                             num_dual_terms=2 * len(block.primes)))

    return rows


# ============================================================
# CSV streaming
# ============================================================

class CSVStream:
    def __init__(self, path: str) -> None:
        self.path = path
        out_parent = os.path.dirname(os.path.abspath(path))
        if out_parent:
            os.makedirs(out_parent, exist_ok=True)
        file_exists = os.path.exists(path) and os.path.getsize(path) > 0
        self._fp = open(path, "a", newline="")
        self._w = csv.DictWriter(self._fp, fieldnames=CSV_FIELDS)
        if not file_exists:
            self._w.writeheader()
            self._fp.flush()

    def emit(self, row: CandidateRow) -> None:
        self._w.writerow(asdict(row))
        self._fp.flush()

    def close(self) -> None:
        self._fp.close()


# ============================================================
# alpha grid
# ============================================================

def alpha_grid(R: int, L: float, mode: str = "default") -> List[float]:
    if mode == "default":
        vals = [0.0, R ** -2, -R ** -2, R ** -1, -R ** -1, 1.0, -1.0, 2.0, -2.0]
    elif mode == "compact":
        vals = [0.0, R ** -1, -R ** -1, 1.0, -1.0]
    else:
        raise ValueError(f"unknown alpha_grid_mode: {mode}")
    return [float(v / max(L, EPS)) for v in vals]


# ============================================================
# Main
# ============================================================

def print_summary(out_path: str, config_name: str) -> None:
    rows: List[dict] = []
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        with open(out_path, newline="") as f:
            for d in csv.DictReader(f):
                rows.append(d)
    if not rows:
        log("no rows to summarize.")
        return
    log(f"=== Summary: {config_name} ({len(rows)} rows) ===")
    cls_counts: Dict[str, int] = {}
    stage_counts: Dict[str, int] = {}
    for d in rows:
        cls_counts[d.get("collapse_class", "")] = cls_counts.get(d.get("collapse_class", ""), 0) + 1
        stage_counts[d.get("stage", "")] = stage_counts.get(d.get("stage", ""), 0) + 1
    log("collapse_class counts:")
    for k in sorted(cls_counts):
        log(f"  {k}: {cls_counts[k]}")
    log("stage counts:")
    for k in sorted(stage_counts):
        log(f"  {k}: {stage_counts[k]}")

    def f(x: str) -> float:
        try:
            return float(x)
        except Exception:
            return float("nan")

    # By stage, smallest objective_value (best collapse candidate)
    log("Best (smallest objective_value) per stage:")
    for stage in sorted(stage_counts):
        stage_rows = [d for d in rows if d.get("stage") == stage]
        stage_rows.sort(key=lambda d: f(d.get("objective_value", "inf")))
        if not stage_rows:
            continue
        d = stage_rows[0]
        log(f"  {stage}: R={d.get('R')} c={d.get('c')} alpha={f(d.get('alpha')):.4e} "
            f"m={f(d.get('m')):.3e} eta_Z={f(d.get('eta_Z')):.3e} "
            f"eta_W={f(d.get('eta_W')):.3e} rho_rank_2={f(d.get('rho_rank_2')):.3e} "
            f"kappa={f(d.get('kappa_basis')):.3e} class={d.get('collapse_class')}")

    flagged = [d for d in rows if d.get("collapse_class") in
               {"yellow_orbit_collapse", "red_candidate_pre_E2", "red_collapse"}]
    log(f"flagged rows (yellow/red): {len(flagged)}")
    for d in flagged[:20]:
        log(f"  FLAG {d.get('stage')}: R={d.get('R')} c={d.get('c')} "
            f"alpha={f(d.get('alpha')):.4e} eta_Z={f(d.get('eta_Z')):.3e} "
            f"eta_W={f(d.get('eta_W')):.3e} class={d.get('collapse_class')}")


def run(args: argparse.Namespace) -> None:
    cfg = load_config(args.config) if args.config else {}
    if args.output:
        cfg["output"] = args.output
    if args.workers is not None:
        cfg["workers"] = int(args.workers)
    if args.no_resume:
        cfg["resume"] = False
    if args.stages:
        cfg["stages"] = args.stages.split(",")

    config_name = (
        os.path.splitext(os.path.basename(args.config))[0]
        if args.config else "default"
    )
    workers = int(cfg.get("workers", max(1, (os.cpu_count() or 2) - 2)))
    R_values = [int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12])]
    c_values = [float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])]
    stages = list(cfg.get("stages", ["relaxed", "main_orbit"]))
    Q_mode = str(cfg.get("Q_mode", "toy"))

    out_stem = str(cfg.get("output", _default_out(f"{config_name}.csv")))
    if not os.path.isabs(out_stem):
        if os.sep not in out_stem:
            out_stem = _default_out(out_stem)
    params_hash = compute_params_hash(cfg, config_name)
    out_path = derive_output_path(out_stem, params_hash)

    log(f"config: {config_name}")
    log(f"workers: {workers}")
    log(f"Q_mode: {Q_mode}, R_values: {R_values}, c_values: {c_values}")
    log(f"stages: {stages}")
    log(f"params hash: {params_hash[:12]} (full: {params_hash})")
    log(f"output: {out_path}")

    resume = bool(cfg.get("resume", True))
    existing_keys: set = load_existing_keys(out_path) if resume else set()
    if existing_keys:
        log(f"resume: {len(existing_keys)} existing rows; will dedupe by row key.")

    run_id = str(uuid.uuid4())[:8]

    # Build task list. Each task = one (R, c, alpha) triple; the worker runs
    # all enabled stages inside that triple.
    tasks: List[tuple] = []
    skipped_blocks = 0
    for R in R_values:
        Q = choose_Q_for_R(R, Q_mode)
        for c_val in c_values:
            # Compute alphas at this (R, c)
            L = Q / R
            for alpha in alpha_grid(R, L, mode=str(cfg.get("alpha_grid_mode", "default"))):
                tasks.append((run_id, config_name, R, c_val, alpha, cfg))
    log(f"task count: {len(tasks)}")

    stream = CSVStream(out_path)
    completed = 0
    emitted = 0
    skipped_rows = 0
    t_start = time.time()

    try:
        if workers <= 1:
            for t in tasks:
                rows = _process_one_task(t)
                completed += 1
                for row in rows:
                    if _row_key(row) in existing_keys:
                        skipped_rows += 1
                        continue
                    stream.emit(row)
                    emitted += 1
                if completed % 5 == 0 or completed == len(tasks):
                    log(f"  progress: {completed}/{len(tasks)} tasks, {emitted} rows emitted")
        else:
            try:
                ctx = _mp.get_context("fork")
            except ValueError:
                ctx = _mp.get_context("spawn")
            with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
                futures = [pool.submit(_process_one_task, t) for t in tasks]
                for fut in as_completed(futures):
                    rows = fut.result()
                    completed += 1
                    for row in rows:
                        if _row_key(row) in existing_keys:
                            skipped_rows += 1
                            continue
                        stream.emit(row)
                        emitted += 1
                    if completed % 5 == 0 or completed == len(tasks):
                        log(f"  progress: {completed}/{len(tasks)} tasks, {emitted} rows emitted")
    finally:
        stream.close()

    elapsed = time.time() - t_start
    log(f"done in {elapsed:.1f}s; emitted {emitted} new rows, skipped {skipped_rows} resume hits.")
    print_summary(out_path, config_name)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=None, help="JSON config file")
    p.add_argument("--output", default=None, help="output CSV stem (params hash inserted)")
    p.add_argument("--workers", type=int, default=None,
                   help="process-pool size; default cpu_count - 2")
    p.add_argument("--no-resume", action="store_true",
                   help="ignore existing CSV at this hash and re-emit all rows")
    p.add_argument("--stages", default=None,
                   help="comma-separated stages override (e.g. relaxed,main_orbit)")
    return p.parse_args()


if __name__ == "__main__":
    run(parse_args())
