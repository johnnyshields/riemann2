#!/usr/bin/env python3
"""
local_zalpha_amplitude_stress.py
--------------------------------

Empirical stress test for the missing local Z_alpha amplitude / zero-crowding
theorem (Agent 5 / E follow-up to the determinant route):

    Z_alpha(m0) ~= 0
    =>
    sup_{|t| <= a} |Z_alpha(m0 + lambda t)| >= Q^{-A}.

For each target (m0, alpha, R, Q, c), we compute on the same packet-frequency
log-derivative AFE surrogate as agent_b5:

    Z0_abs              = |Z_alpha(m0)|
    eta_Z0              = Z0_abs / ||z||_2
    A_sup(a)            = sup_{|t|<=a} |Z_alpha(m0 + lambda t)|
    L2_amp(a)           = ( int_{-a}^{a} |Z_alpha(m0+lambda t)|^2 dt )^{1/2}
    J_k(m0)             = |F^{(k)}(0)| / k!,   F(t) = Z_alpha(m0 + lambda t)
    N_minima_thresholded= # local minima of |Z_alpha| in window <= Q^{-C_Z}

Windows: a in {1, R, 2R, (log Q)^2}.

Stop rules (from the brief):
    red_local_amplitude_threat:
        Z0 <= Q^-CZ AND A_sup(logQ^2) <= Q^-CA AND J_max <= Q^-CJ AND
        N_min((logQ^2),CZ) > C0*R
    yellow_local_flatness:
        Z0 <= Q^-CZ AND A_sup(R) <= Q^-CA AND J_max <= Q^-CJ AND
        A_sup(logQ^2) > Q^-CA  (one-packet flat, polylog rescue possible)
    z_small_but_amplitude_ok:  Z0 small, but A_sup not small
    harmless: anything else

Conventions:
    A(s) = -zeta'/zeta(s); reflected dual sigma_k = (-1)^(k+1).
    k_Z = 0 default (current zero/incidence row, Lambda(p)*p^{-1/2-alpha}).
    Operator nodes are signed (+log p plus, -log p minus); folded node is
    diagnostic only and not used here.

Reuses scripts/zeta_bridge_shared/afe_logderiv_weights.py via sys.path.

Output: param-hashed CSV in <SCRIPT_DIR>/out/. Resume by row key on rerun.
"""

from __future__ import annotations

# Pin BLAS / OpenMP threads before numpy import — we parallelize at the
# (R, Q, c) target-group level via multiprocessing.
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
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

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
_SHARED_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "zeta_bridge_shared"))
_AGENT_B5_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "zeta_bridge_agent_b5"))
for _d in (_SHARED_DIR,):
    if _d not in sys.path:
        sys.path.insert(0, _d)

from afe_logderiv_weights import sigma_k  # noqa: E402  (locked dual sign)


SCHEMA_VERSION = 2  # v2: cross-window target-level reclassification.
                    # Per-row classify emits `local_flatness_candidate`; final
                    # `yellow_local_flatness` / `red_local_amplitude_threat`
                    # promotion is done in a target-level post-pass after all
                    # four windows are collected.
                    # v1: per-row classification only.
EPS = 1e-300


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def _default_out(*parts: str) -> str:
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


# ============================================================
# Data structures
# ============================================================

@dataclass(frozen=True)
class Target:
    target_id: str
    kind: str
    R: int
    Q: float
    alpha: float
    m0: float
    c: float
    source_csv: str = ""
    source_row_index: int = -1
    source_config: str = ""
    source_stage: str = ""
    source_eta_Z: float = float("nan")
    source_eta_W: float = float("nan")
    source_rho_rank: float = float("nan")
    source_kappa_basis: float = float("nan")


@dataclass
class PrimeBlock:
    R: int
    Q: float
    c: float
    lam: float
    u_min: float
    u_max: float
    primes: np.ndarray
    logs: np.ndarray


@dataclass
class ZModel:
    R: int
    Q: float
    lam: float
    alpha: float
    primes: np.ndarray
    logs: np.ndarray
    plus_coeffs: np.ndarray
    minus_coeffs: Optional[np.ndarray]
    include_dual: bool
    coeff_norm: float
    k_Z: int

    def Z(self, m: float) -> complex:
        plus = np.sum(self.plus_coeffs * np.exp(-1j * m * self.logs))
        if self.include_dual and self.minus_coeffs is not None:
            minus = np.sum(self.minus_coeffs * np.exp(+1j * m * self.logs))
            return complex(plus + minus)
        return complex(plus)

    def Z_grid(self, ms: np.ndarray) -> np.ndarray:
        """Vectorized: ms shape (M,) -> values shape (M,) complex."""
        # exp(-1j * m * logs) is a (M, N) matrix; multiply by plus_coeffs (N,).
        plus = np.exp(-1j * np.outer(ms, self.logs)) @ self.plus_coeffs
        if self.include_dual and self.minus_coeffs is not None:
            minus = np.exp(+1j * np.outer(ms, self.logs)) @ self.minus_coeffs
            return plus + minus
        return plus

    def derivative_t_at(self, m0: float, k: int) -> complex:
        """F(t)=Z(m0+lambda*t); F^(k)(0) = sum_n a_n (-i lambda log n)^k e^{-i m0 log n}
        plus the matching minus-branch term."""
        x = self.lam * self.logs
        plus_phase = self.plus_coeffs * np.exp(-1j * m0 * self.logs)
        plus = np.sum(plus_phase * ((-1j * x) ** k))
        if self.include_dual and self.minus_coeffs is not None:
            minus_phase = self.minus_coeffs * np.exp(+1j * m0 * self.logs)
            minus = np.sum(minus_phase * ((+1j * x) ** k))
            return complex(plus + minus)
        return complex(plus)


@dataclass
class ResultRow:
    run_id: str
    timestamp: str
    config_name: str
    target_id: str
    target_class: str
    source_csv: str
    source_row_index: int
    source_config: str
    source_stage: str
    source_eta_Z: float
    source_eta_W: float
    source_rho_rank: float
    source_kappa_basis: float
    R: int
    Q: float
    lambda_: float
    c: float
    alpha: float
    m0: float
    a: float
    a_kind: str
    window_m_radius: float
    num_primes: int
    Z0_abs: float
    eta_Z0: float
    A_sup: float
    A_sup_log: float
    t_at_A_sup: float
    L2_amp: float
    J_max: float
    J_rms: float
    J_argmax_k: int
    N_minima: int
    N_minima_thresholded: int
    min_Z_abs_in_window: float
    m_at_min_Z: float
    crowding_ratio: float
    classification: str
    N_grid: int
    refined_max: bool
    refined_min: bool
    optimizer_status: str
    afe_model: str
    include_dual: bool
    k_Z: int
    notes: str


CSV_FIELDS = list(ResultRow.__dataclass_fields__.keys())

_ROW_KEY_FIELDS = ("config_name", "target_id", "a_kind", "include_dual", "k_Z")


def _row_key(row: ResultRow) -> tuple:
    return tuple(getattr(row, f) for f in _ROW_KEY_FIELDS)


def _row_key_from_dict(d: dict) -> tuple:
    out = []
    for f in _ROW_KEY_FIELDS:
        v = d.get(f, "")
        if f == "include_dual":
            v = str(v).lower() in ("true", "1")
        out.append(v)
    return tuple(out)


# ============================================================
# Config / params hash
# ============================================================

def load_config(path: Optional[str]) -> Dict[str, Any]:
    if not path:
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def safe_float(x: Any, default: float = float("nan")) -> float:
    try:
        if x is None or x == "":
            return default
        v = float(x)
        return v if math.isfinite(v) else default
    except Exception:
        return default


def safe_int(x: Any, default: int = 0) -> int:
    try:
        if x is None or x == "":
            return default
        return int(float(x))
    except Exception:
        return default


def compute_params_hash(cfg: Dict[str, Any], config_name: str,
                        det_csv_paths: Sequence[str]) -> str:
    csv_sigs = []
    for p in sorted(det_csv_paths):
        if os.path.exists(p):
            csv_sigs.append((os.path.basename(p), os.path.getsize(p)))
        else:
            csv_sigs.append((os.path.basename(p), -1))
    record = {
        "schema_version": SCHEMA_VERSION,
        "config_name": config_name,
        "det_csv_signatures": csv_sigs,
        "etaZ_cut_abs": float(cfg.get("etaZ_cut_abs", 1e-3)),
        "etaZ_cut_power": float(cfg.get("etaZ_cut_power", 3.0)),
        "best_by_stage": bool(cfg.get("best_by_stage", True)),
        "max_targets_per_group": int(cfg.get("max_targets_per_group", 1)),
        "max_targets": int(cfg.get("max_targets", 400)),
        "random_controls": int(cfg.get("random_controls", 100)),
        "include_dual": bool(cfg.get("include_dual", False)),
        "k_Z": int(cfg.get("k_Z", 0)),
        "Q_mode": cfg.get("Q_mode", "larger_toy"),
        "R_values": [int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12, 16])],
        "c_values": [float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])],
        "m_min_random": float(cfg.get("m_min_random", 50.0)),
        "m_max_factor_random": float(cfg.get("m_max_factor_random", 100.0)),
        "max_primes": int(cfg.get("max_primes", 5000)),
        "max_grid": int(cfg.get("max_grid", 8001)),
        "min_grid_factor": int(cfg.get("min_grid_factor", 40)),
        "min_grid_floor": int(cfg.get("min_grid_floor", 401)),
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_A": float(cfg.get("C_A", 4.0)),
        "C_J": float(cfg.get("C_J", 4.0)),
        "C0_crowd": float(cfg.get("C0_crowd", 4.0)),
        "seed": int(cfg.get("seed", 12345)),
        "m_min_target": float(cfg.get("m_min_target", 50.0)),
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
# Prime block / Z model
# ============================================================

def primes_in_interval(lo: int, hi: int, max_count: Optional[int] = None) -> List[int]:
    lo = max(2, int(lo))
    hi = int(hi)
    if lo > hi:
        return []
    if sp is not None:
        out: List[int] = []
        # nextprime loop avoids materializing huge intervals; stop at max_count or hi.
        p = int(sp.nextprime(lo - 1))
        while p <= hi and (max_count is None or len(out) < max_count):
            out.append(int(p))
            p = int(sp.nextprime(p))
        return out

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


def build_prime_block(R: int, Q: float, c: float, max_primes: int) -> PrimeBlock:
    lam = 1.0 / Q
    u_min = c * Q
    u_max = c * Q + Q / R
    p_min = int(math.ceil(math.exp(u_min)))
    p_max = int(math.floor(math.exp(u_max)))
    ps = primes_in_interval(p_min, p_max, max_count=max_primes)
    primes = np.asarray(ps, dtype=np.float64)
    logs = np.log(primes) if len(primes) else np.asarray([], dtype=float)
    return PrimeBlock(R=R, Q=Q, c=c, lam=lam, u_min=u_min, u_max=u_max,
                      primes=primes, logs=logs)


def build_z_model(block: PrimeBlock, alpha: float, k_Z: int,
                  include_dual: bool) -> ZModel:
    if len(block.primes) == 0:
        raise ValueError(f"empty prime block R={block.R} Q={block.Q} c={block.c}")
    primes = block.primes
    logs = block.logs
    Lam = logs  # prime-only von Mangoldt

    plus = Lam * (logs ** k_Z) * (primes ** (-0.5 - alpha))
    plus_c = plus.astype(np.complex128)

    minus_c: Optional[np.ndarray] = None
    if include_dual:
        minus = sigma_k(k_Z) * Lam * (logs ** k_Z) * (primes ** (-0.5 + alpha))
        minus_c = minus.astype(np.complex128)
        coeff_norm = math.sqrt(np.linalg.norm(plus_c) ** 2 + np.linalg.norm(minus_c) ** 2)
    else:
        coeff_norm = float(np.linalg.norm(plus_c))

    return ZModel(
        R=block.R, Q=block.Q, lam=block.lam, alpha=alpha,
        primes=primes, logs=logs,
        plus_coeffs=plus_c, minus_coeffs=minus_c,
        include_dual=include_dual,
        coeff_norm=max(coeff_norm, EPS),
        k_Z=k_Z,
    )


# ============================================================
# Target collection
# ============================================================

def target_hash(kind: str, R: int, Q: float, alpha: float, m0: float, c: float) -> str:
    s = f"{kind}|{R}|{Q:.12g}|{alpha:.12g}|{m0:.12g}|{c:.12g}"
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def read_csv_rows(path: str) -> List[Dict[str, str]]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def collect_targets_from_csvs(
    paths: Sequence[str],
    etaZ_cut_abs: float,
    etaZ_cut_power: float,
    best_by_stage: bool,
    max_targets_per_group: int,
    m_min_target: float,
) -> List[Target]:
    out: List[Target] = []
    grouped: Dict[Tuple[str, str, int], List[Tuple[int, Dict[str, str], str]]] = {}

    for path in paths:
        if not os.path.exists(path):
            log(f"  warning: missing det CSV: {path}")
            continue
        rows = read_csv_rows(path)
        for idx, row in enumerate(rows):
            R = safe_int(row.get("R"))
            Q = safe_float(row.get("Q"))
            alpha = safe_float(row.get("alpha"))
            m0 = safe_float(row.get("m"))
            c = safe_float(row.get("c"))
            etaZ = safe_float(row.get("eta_Z"))
            etaW = safe_float(row.get("eta_W"))
            rho = safe_float(row.get("rho_rank_2"))
            kappa = safe_float(row.get("kappa_basis"))
            config = row.get("config_name", os.path.basename(path))
            stage = row.get("stage", "")

            if not (R > 0 and Q > 0 and math.isfinite(m0) and m0 >= m_min_target):
                continue

            threshold = min(etaZ_cut_abs, Q ** (-etaZ_cut_power))
            if math.isfinite(etaZ) and etaZ <= threshold:
                kind = "determinant_small_etaZ"
                tid = target_hash(kind, R, Q, alpha, m0, c)
                out.append(Target(
                    target_id=tid, kind=kind, R=R, Q=Q, alpha=alpha, m0=m0, c=c,
                    source_csv=os.path.basename(path), source_row_index=idx,
                    source_config=config, source_stage=stage,
                    source_eta_Z=etaZ, source_eta_W=etaW,
                    source_rho_rank=rho, source_kappa_basis=kappa,
                ))

            grouped.setdefault((config, stage, R), []).append((idx, row, os.path.basename(path)))

    if best_by_stage:
        for (config, stage, R), items in grouped.items():
            items_sorted = sorted(
                items, key=lambda ir: safe_float(ir[1].get("eta_Z"), float("inf"))
            )
            for idx, row, fn in items_sorted[:max_targets_per_group]:
                Q = safe_float(row.get("Q"))
                alpha = safe_float(row.get("alpha"))
                m0 = safe_float(row.get("m"))
                c = safe_float(row.get("c"))
                if not (math.isfinite(Q) and math.isfinite(m0) and m0 >= m_min_target):
                    continue
                kind = "best_etaZ_by_stage"
                tid = target_hash(kind, R, Q, alpha, m0, c)
                out.append(Target(
                    target_id=tid, kind=kind, R=R, Q=Q, alpha=alpha, m0=m0, c=c,
                    source_csv=fn, source_row_index=idx,
                    source_config=config, source_stage=stage,
                    source_eta_Z=safe_float(row.get("eta_Z")),
                    source_eta_W=safe_float(row.get("eta_W")),
                    source_rho_rank=safe_float(row.get("rho_rank_2")),
                    source_kappa_basis=safe_float(row.get("kappa_basis")),
                ))

    return dedupe_targets(out)


def random_targets(
    count: int, R_values: Sequence[int], c_values: Sequence[float],
    Q_mode: str, m_min: float, m_max_factor: float, seed: int,
) -> List[Target]:
    rng = np.random.default_rng(seed)
    out: List[Target] = []
    for _ in range(count):
        R = int(rng.choice(list(R_values)))
        Q = choose_Q_for_R(R, Q_mode)
        c = float(rng.choice(list(c_values)))
        L = Q / R
        alpha = float(rng.choice(np.array([0.0, 1.0 / (R * L), -1.0 / (R * L),
                                            1.0 / L, -1.0 / L])))
        m0 = float(rng.uniform(m_min, m_max_factor * Q))
        kind = "random_control"
        tid = target_hash(kind, R, Q, alpha, m0, c)
        out.append(Target(target_id=tid, kind=kind, R=R, Q=Q, alpha=alpha, m0=m0, c=c))
    return out


def choose_Q_for_R(R: int, mode: str) -> float:
    if mode == "toy":
        return float(20 + 2 * R)
    if mode == "larger_toy":
        return float(40 + 3 * R)
    if mode.startswith("fixed:"):
        return float(mode.split(":", 1)[1])
    raise ValueError(f"unknown Q mode: {mode}")


def dedupe_targets(targets: Sequence[Target]) -> List[Target]:
    seen: set = set()
    out: List[Target] = []
    for t in targets:
        key = (t.kind, t.R, round(t.Q, 10), round(t.alpha, 12),
               round(t.m0, 9), round(t.c, 8))
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
    return out


# ============================================================
# Window evaluation
# ============================================================

def find_local_minima_indices(values: np.ndarray) -> List[int]:
    out = []
    for i in range(1, len(values) - 1):
        if values[i] <= values[i - 1] and values[i] <= values[i + 1]:
            out.append(i)
    return out


def refine_max_abs_Z(model: ZModel, m0: float, a: float,
                     t_guess: float) -> Tuple[float, float, bool, str]:
    if _opt is None:
        v = abs(model.Z(m0 + model.lam * t_guess))
        return t_guess, v, False, "no_scipy"
    lo, hi = -a, a

    def obj(t_arr):
        t = float(t_arr[0])
        if t < lo or t > hi:
            return 1e100 + (abs(t) - a) ** 2
        return -abs(model.Z(m0 + model.lam * t))

    res = _opt.minimize(obj, np.array([t_guess]), method="Nelder-Mead",
                        options={"maxiter": 80, "xatol": 1e-6, "fatol": 1e-12})
    t = float(np.clip(res.x[0], lo, hi))
    v = abs(model.Z(m0 + model.lam * t))
    return t, v, bool(res.success), str(res.message)[:40]


def refine_min_abs_Z(model: ZModel, m0: float, a: float,
                     t_guess: float) -> Tuple[float, float, bool]:
    if _opt is None:
        v = abs(model.Z(m0 + model.lam * t_guess))
        return t_guess, v, False
    lo, hi = -a, a

    def obj(t_arr):
        t = float(t_arr[0])
        if t < lo or t > hi:
            return 1e100 + (abs(t) - a) ** 2
        return abs(model.Z(m0 + model.lam * t))

    res = _opt.minimize(obj, np.array([t_guess]), method="Nelder-Mead",
                        options={"maxiter": 80, "xatol": 1e-6, "fatol": 1e-16})
    t = float(np.clip(res.x[0], lo, hi))
    v = abs(model.Z(m0 + model.lam * t))
    return t, v, bool(res.success)


def compute_jets(model: ZModel, m0: float) -> Tuple[float, float, int, List[float]]:
    vals: List[float] = []
    for k in range(1, model.R + 2):
        d = model.derivative_t_at(m0, k)
        vals.append(abs(d) / float(math.factorial(k)))
    arr = np.asarray(vals, dtype=float)
    if len(arr) == 0:
        return float("nan"), float("nan"), -1, vals
    return (float(np.max(arr)),
            float(np.sqrt(np.sum(arr * arr))),
            int(np.argmax(arr) + 1),
            vals)


def classify_local(Z0_abs: float, A_sup: float, J_max: float, N_thresh: int,
                   R: int, Q: float, a_kind: str, cfg: Dict[str, Any]) -> str:
    """
    Per-row signal only. The full Yellow / Red verdicts require comparing the
    R window to the (log Q)^2 window for the same target, so they are emitted
    by the post-pass `reclassify_target_level()` below — the per-row
    classifier returns `local_flatness_candidate` (a candidate flag, not a
    verdict).
    """
    CZ = float(cfg.get("C_Z", 6.0))
    CA = float(cfg.get("C_A", 4.0))
    CJ = float(cfg.get("C_J", 4.0))
    z_small = Z0_abs <= Q ** (-CZ)
    amp_small = A_sup <= Q ** (-CA)
    jet_small = J_max <= Q ** (-CJ)
    if z_small and amp_small and jet_small:
        return "local_flatness_candidate"
    if z_small and not amp_small:
        return "z_small_but_amplitude_ok"
    return "harmless"


def reclassify_target_level(out_path: str, cfg: Dict[str, Any]) -> Dict[str, int]:
    """
    Second-pass classification across the four window rows of each target.

    Yellow (yellow_local_flatness):
        Z0_abs <= Q^-CZ AND A_sup(R) <= Q^-CA AND J_max <= Q^-CJ
        AND A_sup(logQ^2) > Q^-CA
    Red (red_local_amplitude_threat):
        Z0_abs <= Q^-CZ AND A_sup(logQ^2) <= Q^-CA AND J_max <= Q^-CJ
        AND N_minima_thresholded(logQ^2) > C0_crowd * R
    z_small_but_amplitude_ok:
        Z0_abs <= Q^-CZ AND A_sup(logQ^2) > Q^-CA AND not Yellow
    harmless: anything else.

    All four rows of a target receive the same target-level verdict so the
    summary doesn't have to re-aggregate.

    Returns the new classification counts.
    """
    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        return {}

    with open(out_path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return {}

    CZ = float(cfg.get("C_Z", 6.0))
    CA = float(cfg.get("C_A", 4.0))
    CJ = float(cfg.get("C_J", 4.0))
    C0 = float(cfg.get("C0_crowd", 4.0))

    # Group by (config_name, target_id, include_dual, k_Z); each group is one
    # target's four windows.
    groups: Dict[tuple, List[dict]] = {}
    for r in rows:
        key = (r.get("config_name", ""), r.get("target_id", ""),
               str(r.get("include_dual", "")).lower(),
               r.get("k_Z", "0"))
        groups.setdefault(key, []).append(r)

    counts: Dict[str, int] = {}
    for key, group_rows in groups.items():
        by_kind = {r.get("a_kind", ""): r for r in group_rows}
        # Find R-window and logQ2-window rows; if either is missing we fall
        # back to per-row signal (e.g. failed targets).
        r_R = by_kind.get("R")
        r_logQ2 = by_kind.get("logQ2")
        if r_R is None or r_logQ2 is None:
            # Keep existing classification; count as-is.
            for r in group_rows:
                cls = r.get("classification", "harmless")
                counts[cls] = counts.get(cls, 0) + 1
            continue

        Q = safe_float(r_R.get("Q"))
        R_int = safe_int(r_R.get("R"))
        Z0 = safe_float(r_R.get("Z0_abs"))
        Jm = safe_float(r_R.get("J_max"))
        A_R = safe_float(r_R.get("A_sup"))
        A_lq = safe_float(r_logQ2.get("A_sup"))
        N_thr_lq = safe_int(r_logQ2.get("N_minima_thresholded"))

        z_small = math.isfinite(Z0) and Z0 <= Q ** (-CZ)
        jet_small = math.isfinite(Jm) and Jm <= Q ** (-CJ)
        A_R_small = math.isfinite(A_R) and A_R <= Q ** (-CA)
        A_lq_small = math.isfinite(A_lq) and A_lq <= Q ** (-CA)
        crowded = N_thr_lq > C0 * R_int

        if z_small and A_lq_small and jet_small and crowded:
            verdict = "red_local_amplitude_threat"
        elif z_small and A_R_small and jet_small and not A_lq_small:
            verdict = "yellow_local_flatness"
        elif z_small and not A_lq_small:
            verdict = "z_small_but_amplitude_ok"
        else:
            verdict = "harmless"

        for r in group_rows:
            r["classification"] = verdict
            counts[verdict] = counts.get(verdict, 0) + 1

    # Rewrite CSV with updated classifications.
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        for r in rows:
            # Coerce keys to CSV_FIELDS exactly.
            w.writerow({k: r.get(k, "") for k in CSV_FIELDS})

    return counts


def evaluate_window(model: ZModel, target: Target, a: float, a_kind: str,
                    cfg: Dict[str, Any]) -> Dict[str, Any]:
    R = target.R
    Q = target.Q
    lam = model.lam
    Z0 = model.Z(target.m0)
    Z0_abs = abs(Z0)
    eta_Z0 = Z0_abs / max(model.coeff_norm, EPS)

    N_grid = max(int(cfg.get("min_grid_floor", 401)),
                 int(int(cfg.get("min_grid_factor", 40)) * a * R))
    N_grid = min(N_grid, int(cfg.get("max_grid", 8001)))
    t_grid = np.linspace(-a, a, N_grid)
    m_grid = target.m0 + lam * t_grid
    vals = np.abs(model.Z_grid(m_grid))

    idx_max = int(np.argmax(vals))
    A_grid = float(vals[idx_max])
    t_max0 = float(t_grid[idx_max])
    t_max, A_refined, max_ok, max_msg = refine_max_abs_Z(model, target.m0, a, t_max0)
    A_sup = max(A_grid, A_refined)

    L2_amp = float(math.sqrt(np.trapezoid(vals * vals, t_grid)))

    minima_idx = find_local_minima_indices(vals)
    refined_min: List[Tuple[float, float]] = []
    for i in minima_idx:
        t_min, v_min, _ok = refine_min_abs_Z(model, target.m0, a, float(t_grid[i]))
        refined_min.append((t_min, v_min))
    if refined_min:
        t_min_best, min_val = min(refined_min, key=lambda tv: tv[1])
    else:
        i_min = int(np.argmin(vals))
        t_min_best, min_val = float(t_grid[i_min]), float(vals[i_min])

    threshold = Q ** (-float(cfg.get("C_Z", 6.0)))
    N_thresh = sum(1 for _, v in refined_min if v <= threshold)

    return dict(
        Z0_abs=Z0_abs, eta_Z0=eta_Z0, A_sup=A_sup,
        A_sup_log=math.log(max(A_sup, EPS)),
        t_at_A_sup=float(t_max), L2_amp=L2_amp,
        N_grid=N_grid, refined_max=max_ok, refined_min=bool(refined_min),
        optimizer_status=max_msg,
        N_minima=len(refined_min), N_minima_thresholded=N_thresh,
        min_Z_abs_in_window=float(min_val),
        m_at_min_Z=target.m0 + lam * float(t_min_best),
        crowding_ratio=N_thresh / max(R, 1),
    )


# ============================================================
# Per-task worker
# ============================================================

WINDOW_KINDS = ("1", "R", "2R", "logQ2")


def _window_size(kind: str, R: int, Q: float) -> float:
    if kind == "1":
        return 1.0
    if kind == "R":
        return float(R)
    if kind == "2R":
        return float(2 * R)
    if kind == "logQ2":
        return float(math.log(Q) ** 2)
    raise ValueError(kind)


def _process_group(task: tuple) -> List[ResultRow]:
    """Task = (run_id, config_name, R, Q, c, [Target...], cfg_serialized).

    Builds the prime block and Z model once per (R, Q, c, alpha, include_dual)
    sub-key inside the worker, then evaluates all four windows for each target.
    """
    (run_id, config_name, R, Q, c_val, targets_blob, cfg, include_dual,
     k_Z, max_primes) = task
    rows: List[ResultRow] = []

    block: Optional[PrimeBlock] = None
    cached_models: Dict[Tuple[float, bool, int], ZModel] = {}

    for tgt in targets_blob:
        try:
            if block is None:
                block = build_prime_block(R=R, Q=Q, c=c_val, max_primes=max_primes)
            mkey = (round(tgt.alpha, 14), include_dual, k_Z)
            model = cached_models.get(mkey)
            if model is None:
                model = build_z_model(block, alpha=tgt.alpha, k_Z=k_Z,
                                      include_dual=include_dual)
                cached_models[mkey] = model
        except Exception as e:
            # Emit a single 'failed' row so resume keys still match a target.
            for kind in WINDOW_KINDS:
                a = _window_size(kind, R, Q)
                rows.append(_failed_row(run_id, config_name, tgt, a, kind, str(e),
                                         include_dual=include_dual, k_Z=k_Z))
            continue

        for kind in WINDOW_KINDS:
            a = _window_size(kind, R, Q)
            try:
                ev = evaluate_window(model, tgt, a, kind, cfg)
            except Exception as e:
                rows.append(_failed_row(run_id, config_name, tgt, a, kind, str(e),
                                         include_dual=include_dual, k_Z=k_Z))
                continue
            j_max, j_rms, j_arg, _jets = compute_jets(model, tgt.m0)
            cls = classify_local(ev["Z0_abs"], ev["A_sup"], j_max,
                                 ev["N_minima_thresholded"], R, Q, kind, cfg)
            rows.append(ResultRow(
                run_id=run_id, timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                config_name=config_name,
                target_id=tgt.target_id, target_class=tgt.kind,
                source_csv=tgt.source_csv, source_row_index=tgt.source_row_index,
                source_config=tgt.source_config, source_stage=tgt.source_stage,
                source_eta_Z=tgt.source_eta_Z, source_eta_W=tgt.source_eta_W,
                source_rho_rank=tgt.source_rho_rank,
                source_kappa_basis=tgt.source_kappa_basis,
                R=R, Q=Q, lambda_=block.lam, c=c_val, alpha=tgt.alpha,
                m0=tgt.m0,
                a=a, a_kind=kind, window_m_radius=block.lam * a,
                num_primes=int(len(block.primes)),
                Z0_abs=ev["Z0_abs"], eta_Z0=ev["eta_Z0"],
                A_sup=ev["A_sup"], A_sup_log=ev["A_sup_log"],
                t_at_A_sup=ev["t_at_A_sup"], L2_amp=ev["L2_amp"],
                J_max=j_max, J_rms=j_rms, J_argmax_k=j_arg,
                N_minima=ev["N_minima"],
                N_minima_thresholded=ev["N_minima_thresholded"],
                min_Z_abs_in_window=ev["min_Z_abs_in_window"],
                m_at_min_Z=ev["m_at_min_Z"],
                crowding_ratio=ev["crowding_ratio"],
                classification=cls, N_grid=ev["N_grid"],
                refined_max=ev["refined_max"], refined_min=ev["refined_min"],
                optimizer_status=ev["optimizer_status"],
                afe_model="logderiv_packet_frequency",
                include_dual=include_dual, k_Z=k_Z, notes="",
            ))

    return rows


def _failed_row(run_id: str, config_name: str, tgt: Target, a: float,
                a_kind: str, msg: str, include_dual: bool, k_Z: int) -> ResultRow:
    return ResultRow(
        run_id=run_id, timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        config_name=config_name, target_id=tgt.target_id,
        target_class=tgt.kind, source_csv=tgt.source_csv,
        source_row_index=tgt.source_row_index,
        source_config=tgt.source_config, source_stage=tgt.source_stage,
        source_eta_Z=tgt.source_eta_Z, source_eta_W=tgt.source_eta_W,
        source_rho_rank=tgt.source_rho_rank,
        source_kappa_basis=tgt.source_kappa_basis,
        R=tgt.R, Q=tgt.Q, lambda_=1.0 / tgt.Q, c=tgt.c, alpha=tgt.alpha,
        m0=tgt.m0, a=a, a_kind=a_kind, window_m_radius=a / tgt.Q,
        num_primes=0,
        Z0_abs=float("nan"), eta_Z0=float("nan"),
        A_sup=float("nan"), A_sup_log=float("nan"),
        t_at_A_sup=float("nan"), L2_amp=float("nan"),
        J_max=float("nan"), J_rms=float("nan"), J_argmax_k=-1,
        N_minima=0, N_minima_thresholded=0,
        min_Z_abs_in_window=float("nan"), m_at_min_Z=float("nan"),
        crowding_ratio=float("nan"),
        classification="failed", N_grid=0,
        refined_max=False, refined_min=False, optimizer_status="error",
        afe_model="logderiv_packet_frequency",
        include_dual=include_dual, k_Z=k_Z, notes=msg[:120],
    )


# ============================================================
# CSV streaming
# ============================================================

class CSVStream:
    def __init__(self, path: str) -> None:
        self.path = path
        parent = os.path.dirname(os.path.abspath(path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        file_exists = os.path.exists(path) and os.path.getsize(path) > 0
        self._fp = open(path, "a", newline="")
        self._w = csv.DictWriter(self._fp, fieldnames=CSV_FIELDS)
        if not file_exists:
            self._w.writeheader()
            self._fp.flush()

    def emit(self, row: ResultRow) -> None:
        self._w.writerow(asdict(row))
        self._fp.flush()

    def close(self) -> None:
        self._fp.close()


# ============================================================
# Summary
# ============================================================

def print_summary(out_path: str, config_name: str) -> None:
    if not os.path.exists(out_path):
        log("no rows to summarize.")
        return
    with open(out_path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        log("no rows to summarize.")
        return
    log(f"=== Summary: {config_name} ({len(rows)} rows) ===")

    cls_counts: Dict[str, int] = {}
    for r in rows:
        c = r.get("classification", "")
        cls_counts[c] = cls_counts.get(c, 0) + 1
    log("classification counts:")
    for k in sorted(cls_counts):
        log(f"  {k}: {cls_counts[k]}")

    a_kind_counts: Dict[str, int] = {}
    for r in rows:
        a_kind_counts[r.get("a_kind", "")] = a_kind_counts.get(r.get("a_kind", ""), 0) + 1
    log("a_kind counts:")
    for k in sorted(a_kind_counts):
        log(f"  {k}: {a_kind_counts[k]}")

    target_class_counts: Dict[str, int] = {}
    for r in rows:
        if r.get("a_kind") == "logQ2":
            target_class_counts[r.get("target_class", "")] = target_class_counts.get(
                r.get("target_class", ""), 0) + 1
    log("target_class counts (logQ2 row only):")
    for k in sorted(target_class_counts):
        log(f"  {k}: {target_class_counts[k]}")

    def f(x: str) -> float:
        return safe_float(x, float("inf"))

    flagged_classes = ("red_local_amplitude_threat", "yellow_local_flatness",
                       "z_small_but_amplitude_ok")
    flagged = [r for r in rows if r.get("classification") in flagged_classes]
    log(f"flagged rows: {len(flagged)}")
    for r in flagged[:20]:
        log(f"  FLAG {r.get('classification')}: a_kind={r.get('a_kind')} "
            f"R={r.get('R')} Q={r.get('Q')} c={r.get('c')} "
            f"alpha={f(r.get('alpha')):.3e} m0={f(r.get('m0')):.6e} "
            f"Z0={f(r.get('Z0_abs')):.3e} A_sup={f(r.get('A_sup')):.3e} "
            f"J_max={f(r.get('J_max')):.3e} N_thr={r.get('N_minima_thresholded')}")

    # Top-10 smallest A_sup at logQ2 across all rows
    logq2 = [r for r in rows if r.get("a_kind") == "logQ2"]
    logq2.sort(key=lambda r: f(r.get("A_sup")))
    log("Top-10 smallest A_sup (logQ2 window):")
    for r in logq2[:10]:
        log(f"  cls={r.get('classification')} R={r.get('R')} c={r.get('c')} "
            f"m0={f(r.get('m0')):.6e} Z0={f(r.get('Z0_abs')):.3e} "
            f"A_sup={f(r.get('A_sup')):.3e} J_max={f(r.get('J_max')):.3e} "
            f"src={r.get('source_config')}/{r.get('source_stage')}")


# ============================================================
# Main
# ============================================================

def resolve_det_csv_paths(cfg: Dict[str, Any]) -> List[str]:
    paths: List[str] = []
    raw = cfg.get("det_csv", [])
    for p in raw:
        if os.path.isabs(p):
            paths.append(p)
        elif os.path.exists(os.path.join(_SCRIPT_DIR, p)):
            paths.append(os.path.join(_SCRIPT_DIR, p))
        elif os.path.exists(os.path.join(_AGENT_B5_DIR, p)):
            paths.append(os.path.join(_AGENT_B5_DIR, p))
        elif os.path.exists(os.path.join(_AGENT_B5_DIR, "out", p)):
            paths.append(os.path.join(_AGENT_B5_DIR, "out", p))
        else:
            paths.append(p)  # let collect_targets_from_csvs warn
    return paths


def build_targets(cfg: Dict[str, Any], det_csv_paths: Sequence[str]) -> List[Target]:
    targets: List[Target] = []
    targets.extend(collect_targets_from_csvs(
        paths=det_csv_paths,
        etaZ_cut_abs=float(cfg.get("etaZ_cut_abs", 1e-3)),
        etaZ_cut_power=float(cfg.get("etaZ_cut_power", 3.0)),
        best_by_stage=bool(cfg.get("best_by_stage", True)),
        max_targets_per_group=int(cfg.get("max_targets_per_group", 1)),
        m_min_target=float(cfg.get("m_min_target", 50.0)),
    ))
    rc = int(cfg.get("random_controls", 100))
    if rc > 0:
        targets.extend(random_targets(
            count=rc,
            R_values=[int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12, 16])],
            c_values=[float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])],
            Q_mode=str(cfg.get("Q_mode", "larger_toy")),
            m_min=float(cfg.get("m_min_random", 50.0)),
            m_max_factor=float(cfg.get("m_max_factor_random", 100.0)),
            seed=int(cfg.get("seed", 12345)),
        ))
    targets = dedupe_targets(targets)
    targets.sort(key=lambda t: (
        0 if t.kind == "determinant_small_etaZ" else 1,
        safe_float(t.source_eta_Z, 1e99),
    ))
    cap = int(cfg.get("max_targets", 400))
    if cap and len(targets) > cap:
        targets = targets[:cap]
    return targets


def group_targets_by_block(targets: Sequence[Target]
                           ) -> Dict[Tuple[int, float, float], List[Target]]:
    groups: Dict[Tuple[int, float, float], List[Target]] = {}
    for t in targets:
        key = (int(t.R), float(t.Q), float(t.c))
        groups.setdefault(key, []).append(t)
    return groups


def run(args: argparse.Namespace) -> None:
    cfg = load_config(args.config) if args.config else {}
    if args.output:
        cfg["output"] = args.output
    if args.workers is not None:
        cfg["workers"] = int(args.workers)
    if args.no_resume:
        cfg["resume"] = False
    if args.include_dual:
        cfg["include_dual"] = True

    config_name = (
        os.path.splitext(os.path.basename(args.config))[0]
        if args.config else "default"
    )
    workers = int(cfg.get("workers", max(1, (os.cpu_count() or 2) - 2)))
    det_csv_paths = resolve_det_csv_paths(cfg)

    out_stem = str(cfg.get("output", _default_out(f"{config_name}.csv")))
    if not os.path.isabs(out_stem) and os.sep not in out_stem:
        out_stem = _default_out(out_stem)
    params_hash = compute_params_hash(cfg, config_name, det_csv_paths)
    out_path = derive_output_path(out_stem, params_hash)

    log(f"config: {config_name}")
    log(f"workers: {workers}")
    log(f"include_dual: {cfg.get('include_dual', False)}  k_Z: {cfg.get('k_Z', 0)}")
    log(f"det_csv inputs: {len(det_csv_paths)}")
    for p in det_csv_paths:
        log(f"  - {p} ({'ok' if os.path.exists(p) else 'MISSING'})")
    log(f"params hash: {params_hash[:12]} (full: {params_hash})")
    log(f"output: {out_path}")

    targets = build_targets(cfg, det_csv_paths)
    log(f"targets: {len(targets)}  "
        f"(small_etaZ={sum(1 for t in targets if t.kind=='determinant_small_etaZ')}, "
        f"best_by_stage={sum(1 for t in targets if t.kind=='best_etaZ_by_stage')}, "
        f"random={sum(1 for t in targets if t.kind=='random_control')})")

    groups = group_targets_by_block(targets)
    log(f"prime-block groups: {len(groups)}")

    resume = bool(cfg.get("resume", True))
    existing_keys: set = load_existing_keys(out_path) if resume else set()
    if existing_keys:
        log(f"resume: {len(existing_keys)} existing rows; will dedupe by row key.")

    run_id = str(uuid.uuid4())[:8]
    include_dual = bool(cfg.get("include_dual", False))
    k_Z = int(cfg.get("k_Z", 0))
    max_primes = int(cfg.get("max_primes", 5000))

    # Cap cfg fields needed by workers to keep pickle small and stable.
    cfg_for_workers = {
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_A": float(cfg.get("C_A", 4.0)),
        "C_J": float(cfg.get("C_J", 4.0)),
        "C0_crowd": float(cfg.get("C0_crowd", 4.0)),
        "min_grid_floor": int(cfg.get("min_grid_floor", 401)),
        "min_grid_factor": int(cfg.get("min_grid_factor", 40)),
        "max_grid": int(cfg.get("max_grid", 8001)),
    }

    tasks: List[tuple] = []
    for (R, Q, c_val), tgts in sorted(groups.items()):
        tasks.append((run_id, config_name, R, Q, c_val, tgts, cfg_for_workers,
                      include_dual, k_Z, max_primes))
    log(f"tasks: {len(tasks)}")

    stream = CSVStream(out_path)
    completed = 0
    emitted = 0
    skipped_rows = 0
    t_start = time.time()

    try:
        if workers <= 1:
            for t in tasks:
                rows = _process_group(t)
                completed += 1
                for row in rows:
                    if _row_key(row) in existing_keys:
                        skipped_rows += 1
                        continue
                    stream.emit(row)
                    emitted += 1
                if completed % 5 == 0 or completed == len(tasks):
                    log(f"  progress: {completed}/{len(tasks)} groups, "
                        f"{emitted} rows emitted")
        else:
            try:
                ctx = _mp.get_context("fork")
            except ValueError:
                ctx = _mp.get_context("spawn")
            with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
                futures = [pool.submit(_process_group, t) for t in tasks]
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
                        log(f"  progress: {completed}/{len(tasks)} groups, "
                            f"{emitted} rows emitted")
    finally:
        stream.close()

    elapsed = time.time() - t_start
    log(f"done in {elapsed:.1f}s; emitted {emitted} new rows, "
        f"skipped {skipped_rows} resume hits.")

    # Cross-window target-level reclassification (per audit fix #2).
    target_counts = reclassify_target_level(out_path, cfg)
    if target_counts:
        log("target-level verdict counts (after cross-window reclassification):")
        for k in sorted(target_counts):
            log(f"  {k}: {target_counts[k]}")

    print_summary(out_path, config_name)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=None, help="JSON config file")
    p.add_argument("--output", default=None, help="output CSV stem (params hash inserted)")
    p.add_argument("--workers", type=int, default=None,
                   help="process-pool size; default cpu_count - 2")
    p.add_argument("--no-resume", action="store_true",
                   help="ignore existing CSV at this hash and re-emit all rows")
    p.add_argument("--include-dual", action="store_true",
                   help="include reflected log-derivative dual branch")
    return p.parse_args()


if __name__ == "__main__":
    run(parse_args())
