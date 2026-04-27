#!/usr/bin/env python3
"""
local_zalpha_amplitude_v2.py
----------------------------

V2 cell-sum hardening of the local Z_alpha amplitude / zero-crowding stress
test (Agent 5 / E follow-up).

Theorem under empirical attack:

    Z_alpha(m0) = 0
    =>
    sup_{|t| <= (log Q)^2} |Z_alpha(m0 + lambda*t)| >= Q^{-A}.

The v1 test produced 0 Yellow / 0 Red across 1152 rows. v2 hunts harder by:
  - selecting most-adversarial v1 rows (smallest A(logQ^2), smallest J_max,
    smallest combined threat score, largest minima crowding);
  - direct jet-minimizer search over m for points minimizing
        (Q^CZ |Z|)^2 + Q^(2 CJ) sum_k |F^(k)(0)/k!|^2;
  - coarse cell-mass diagnostic
        CellMassRatio_M = sum_r |B_r|^2 / sum_n |z_n|^2,
    for M in {R, 2R, 4R}, plus-only or plus+minus combined.

Verdicts (one row per target):
  red_local_amplitude_threat   Z0 small AND J_max small AND A(logQ^2) small
                                AND N_min(logQ^2) > C0_crowd*R
                                AND CellMassRatio_2R <= Q^-C_cell
  orange_cell_warning           Z0 small AND J_max small AND
                                CellMassRatio_2R <= Q^-C_cell
                                AND A(logQ^2) > Q^-C_A
  yellow_local_flatness         Z0 small AND J_max small AND A(R) <= Q^-C_A
                                AND A(logQ^2) > Q^-C_A
  z_small_but_amplitude_ok      Z0 small AND A(logQ^2) > Q^-C_A
  harmless                      otherwise

Conventions:
    A(s) = -zeta'(s)/zeta(s); reflected dual sigma_0 = -1.
    k_Z = 0 default. plus phase exp(-i m log p), minus phase exp(+i m log p).
    plus operator node = +log p, minus operator node = -log p (signed real
    frequency); folded conductor node is diagnostic only.

Reuses scripts/zeta_bridge_shared/afe_logderiv_weights.py (sigma_k).
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

from afe_logderiv_weights import sigma_k  # noqa: E402


SCHEMA_VERSION = 3  # v3: log-uniform prime sampling so max_primes-capped wide
                    # blocks actually cover the full [u_min, u_max] log range
                    # instead of only the left edge. Records actual_u_min /
                    # actual_u_max / actual_lambda_width from selected primes
                    # and demotes Orange/Red to "undercovered_*_diagnostic"
                    # when actual coverage or active cell count is too low.
                    # v2: multi-block support_blocks K (widened cell-sum support
                    # K*Q/R); active_cell_count_*; Orange/Red guarded to
                    # support_blocks > 1.
                    # v1: single-block support, no active cell count.
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
    source_a_kind: str = ""
    source_eta_Z: float = float("nan")
    source_eta_W: float = float("nan")
    source_A_sup: float = float("nan")
    source_J_max: float = float("nan")
    source_N_minima: float = float("nan")
    source_rho_rank: float = float("nan")
    source_kappa_basis: float = float("nan")


@dataclass
class PrimeBlock:
    R: int
    Q: float
    c: float
    lam: float
    u_min: float        # nominal: c*Q
    u_max: float        # nominal: c*Q + K*Q/R
    support_blocks: float  # K such that u_max = c*Q + K*Q/R
    primes: np.ndarray
    logs: np.ndarray
    sampling_mode: str = "all"  # "all" or "log_uniform"

    @property
    def lambda_width(self) -> float:
        # lam * (u_max - u_min) = K / R (nominal)
        return self.lam * (self.u_max - self.u_min)

    @property
    def actual_u_min(self) -> float:
        return float(self.logs.min()) if len(self.logs) else float("nan")

    @property
    def actual_u_max(self) -> float:
        return float(self.logs.max()) if len(self.logs) else float("nan")

    @property
    def actual_lambda_width(self) -> float:
        if len(self.logs) == 0:
            return float("nan")
        return self.lam * (self.actual_u_max - self.actual_u_min)


@dataclass
class ZModel:
    R: int
    Q: float
    c: float
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
        plus = np.exp(-1j * np.outer(ms, self.logs)) @ self.plus_coeffs
        if self.include_dual and self.minus_coeffs is not None:
            minus = np.exp(+1j * np.outer(ms, self.logs)) @ self.minus_coeffs
            return plus + minus
        return plus

    def derivative_t_at(self, m0: float, k: int) -> complex:
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
    target_generation_method: str
    source_csv: str
    source_row_index: int
    source_config: str
    source_stage: str
    source_a_kind: str
    source_eta_Z: float
    source_eta_W: float
    source_A_sup: float
    source_J_max: float
    source_N_minima: float
    source_rho_rank: float
    source_kappa_basis: float

    R: int
    Q: float
    lambda_: float
    c: float
    alpha: float
    m0: float
    num_primes: int
    include_dual: bool
    k_Z: int
    support_blocks: float
    u_min: float
    u_max: float
    lambda_width: float
    actual_u_min: float
    actual_u_max: float
    actual_lambda_width: float
    sampling_mode: str

    Z0_abs: float
    eta_Z0: float

    A_1: float
    A_R: float
    A_2R: float
    A_logQ2: float
    L2_1: float
    L2_R: float
    L2_2R: float
    L2_logQ2: float

    min_Z_1: float
    min_Z_R: float
    min_Z_2R: float
    min_Z_logQ2: float
    m_at_min_Z_logQ2: float

    N_min_1: int
    N_min_R: int
    N_min_2R: int
    N_min_logQ2: int
    N_min_ratio_logQ2: float

    J_max: float
    J_rms: float
    J_sum_sq: float
    J_argmax_k: int

    cell_count_R: int
    cell_mass_l2_R: float
    cell_mass_inf_R: float
    cell_mass_ratio_R: float
    active_cell_count_R: int

    cell_count_2R: int
    cell_mass_l2_2R: float
    cell_mass_inf_2R: float
    cell_mass_ratio_2R: float
    active_cell_count_2R: int

    cell_count_4R: int
    cell_mass_l2_4R: float
    cell_mass_inf_4R: float
    cell_mass_ratio_4R: float
    active_cell_count_4R: int

    threat_score: float
    jet_objective: float
    classification: str
    notes: str


CSV_FIELDS = list(ResultRow.__dataclass_fields__.keys())

_ROW_KEY_FIELDS = ("config_name", "target_id", "include_dual", "k_Z")


def _row_key(row: ResultRow) -> tuple:
    return tuple(getattr(row, f) for f in _ROW_KEY_FIELDS)


def _row_key_from_dict(d: dict) -> tuple:
    out = []
    for f in _ROW_KEY_FIELDS:
        v = d.get(f, "")
        if f == "include_dual":
            v = str(v).lower() in ("true", "1")
        elif f == "k_Z":
            try:
                v = int(float(v))
            except Exception:
                v = 0
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
                        input_paths: Sequence[str]) -> str:
    input_sig = []
    for p in sorted(input_paths):
        if os.path.exists(p):
            input_sig.append((os.path.basename(p), os.path.getsize(p)))
        else:
            input_sig.append((os.path.basename(p), -1))
    record = {
        "schema_version": SCHEMA_VERSION,
        "config_name": config_name,
        "input_signature": input_sig,
        "include_dual": bool(cfg.get("include_dual", False)),
        "k_Z": int(cfg.get("k_Z", 0)),
        "Q_mode": cfg.get("Q_mode", "larger_toy"),
        "R_values": [int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12, 16])],
        "c_values": [float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])],
        "support_blocks": float(cfg.get("support_blocks", 1.0)),
        "max_targets": int(cfg.get("max_targets", 800)),
        "random_controls": int(cfg.get("random_controls", 100)),
        "direct_jet_minimizers": int(cfg.get("direct_jet_minimizers", 3)),
        "jet_minimizer_grid": int(cfg.get("jet_minimizer_grid", 400)),
        "top_k": int(cfg.get("top_k", 5)),
        "etaZ_cut_abs": float(cfg.get("etaZ_cut_abs", 1e-3)),
        "etaZ_cut_power": float(cfg.get("etaZ_cut_power", 3.0)),
        "best_by_stage": bool(cfg.get("best_by_stage", True)),
        "m_min": float(cfg.get("m_min", 50.0)),
        "m_max_factor": float(cfg.get("m_max_factor", 100.0)),
        "max_primes": int(cfg.get("max_primes", 8000)),
        "max_grid": int(cfg.get("max_grid", 10001)),
        "min_grid_factor": int(cfg.get("min_grid_factor", 40)),
        "min_grid_floor": int(cfg.get("min_grid_floor", 401)),
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_A": float(cfg.get("C_A", 4.0)),
        "C_J": float(cfg.get("C_J", 4.0)),
        "C_cell": float(cfg.get("C_cell", 4.0)),
        "C0_crowd": float(cfg.get("C0_crowd", 4.0)),
        "c_max_eff_limit": float(cfg.get("c_max_eff_limit", 1.0)),
        "seed": int(cfg.get("seed", 12345)),
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

def choose_Q_for_R(R: int, mode: str) -> float:
    if mode == "toy":
        return float(20 + 2 * R)
    if mode == "larger_toy":
        return float(40 + 3 * R)
    if mode.startswith("fixed:"):
        return float(mode.split(":", 1)[1])
    raise ValueError(f"unknown Q mode: {mode}")


def primes_in_interval(lo: int, hi: int, max_count: Optional[int] = None) -> List[int]:
    """Left-edge enumerator: returns the first `max_count` primes in [lo, hi]
    via sympy.nextprime. Used for ALL-mode sampling and as the inner primitive
    for log-uniform sampling."""
    lo = max(2, int(lo))
    hi = int(hi)
    if lo > hi:
        return []
    if sp is not None:
        out: List[int] = []
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


def primes_in_log_interval_log_uniform(u_min: float, u_max: float,
                                       max_count: int) -> List[int]:
    """Log-uniform prime sampling across [u_min, u_max].

    Visits `max_count` evenly-spaced log-anchors and takes the next prime at
    or after each anchor. Returns sorted unique primes within
    [exp(u_min), exp(u_max)]. Designed for wide multi-block supports where the
    full prime count exceeds max_count and we want coverage across the entire
    log interval rather than only the left edge.
    """
    if sp is None:
        # Fallback: dense enumeration capped at max_count (left-edge biased).
        return primes_in_interval(int(math.ceil(math.exp(u_min))),
                                  int(math.floor(math.exp(u_max))),
                                  max_count=max_count)
    if max_count <= 0:
        return []
    hi_int = int(math.floor(math.exp(u_max)))
    us = np.linspace(float(u_min), float(u_max), int(max_count))
    seen: set = set()
    out: List[int] = []
    for u in us:
        n = int(math.ceil(math.exp(float(u))))
        try:
            p = int(sp.nextprime(n - 1))
        except Exception:
            continue
        if p > hi_int or p in seen:
            continue
        seen.add(p)
        out.append(p)
    out.sort()
    return out


def build_prime_block(R: int, Q: float, c: float, max_primes: int,
                      support_blocks: float = 1.0,
                      sampling_mode: str = "auto") -> PrimeBlock:
    """
    Wide-support prime block: u_max = c*Q + K*(Q/R), where K = support_blocks.
    K=1 reproduces the original determinant (Q/R)-block. K>=4 widens the
    support so cell-mass diagnostics don't degenerate to one cell.

    sampling_mode:
        "all":         use primes_in_interval; capped at max_primes from the
                       left edge (fine for narrow blocks where the cap is not
                       hit).
        "log_uniform": evenly-spaced log-anchors with nextprime(); covers the
                       full [u_min, u_max] log range when the prime count
                       exceeds max_primes.
        "auto":        log_uniform for wide blocks (K > 1); all for K <= 1.
    """
    K = float(support_blocks)
    lam = 1.0 / Q
    u_min = c * Q
    u_max = c * Q + K * Q / R

    if sampling_mode == "auto":
        sampling_mode = "log_uniform" if K > 1.0 else "all"

    if sampling_mode == "log_uniform":
        ps = primes_in_log_interval_log_uniform(u_min, u_max, max_primes)
    else:
        p_min = int(math.ceil(math.exp(u_min)))
        p_max = int(math.floor(math.exp(u_max)))
        ps = primes_in_interval(p_min, p_max, max_count=max_primes)

    primes = np.asarray(ps, dtype=np.float64)
    logs = np.log(primes) if len(primes) else np.asarray([], dtype=float)
    return PrimeBlock(R=R, Q=Q, c=c, lam=lam, u_min=u_min, u_max=u_max,
                      support_blocks=K, primes=primes, logs=logs,
                      sampling_mode=sampling_mode)


def build_z_model(block: PrimeBlock, alpha: float, k_Z: int,
                  include_dual: bool) -> ZModel:
    if len(block.primes) == 0:
        raise ValueError(f"empty prime block R={block.R} Q={block.Q} c={block.c}")
    p = block.primes
    L = block.logs
    Lam = L  # prime-only von Mangoldt

    plus = Lam * (L ** k_Z) * (p ** (-0.5 - alpha))
    plus_c = plus.astype(np.complex128)

    minus_c: Optional[np.ndarray] = None
    if include_dual:
        minus = sigma_k(k_Z) * Lam * (L ** k_Z) * (p ** (-0.5 + alpha))
        minus_c = minus.astype(np.complex128)
        coeff_norm = math.sqrt(np.linalg.norm(plus_c) ** 2 + np.linalg.norm(minus_c) ** 2)
    else:
        coeff_norm = float(np.linalg.norm(plus_c))

    return ZModel(
        R=block.R, Q=block.Q, c=block.c, lam=block.lam, alpha=alpha,
        primes=p, logs=L,
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


def make_target(kind: str, row: Dict[str, str], source_csv: str, idx: int
                ) -> Optional[Target]:
    R = safe_int(row.get("R"))
    Q = safe_float(row.get("Q"))
    alpha = safe_float(row.get("alpha"))
    m0 = safe_float(row.get("m0", row.get("m")))
    c = safe_float(row.get("c"))
    if not (R > 0 and Q > 0 and math.isfinite(m0) and m0 > 0 and math.isfinite(c)):
        return None
    tid = target_hash(kind, R, Q, alpha, m0, c)
    return Target(
        target_id=tid, kind=kind, R=R, Q=Q, alpha=alpha, m0=m0, c=c,
        source_csv=os.path.basename(source_csv), source_row_index=idx,
        source_config=row.get("config_name", ""),
        source_stage=row.get("stage", row.get("source_stage", "")),
        source_a_kind=row.get("a_kind", ""),
        source_eta_Z=safe_float(row.get("eta_Z", row.get("eta_Z0"))),
        source_eta_W=safe_float(row.get("eta_W")),
        source_A_sup=safe_float(row.get("A_sup")),
        source_J_max=safe_float(row.get("J_max")),
        source_N_minima=safe_float(row.get("N_minima_thresholded")),
        source_rho_rank=safe_float(row.get("rho_rank_2")),
        source_kappa_basis=safe_float(row.get("kappa_basis")),
    )


def collect_from_v1_amplitude(csv_paths: Sequence[str], top_k: int,
                              m_min: float) -> List[Target]:
    out: List[Target] = []
    for path in csv_paths:
        if not os.path.exists(path):
            continue
        rows = read_csv_rows(path)
        logq2 = [r for r in rows
                 if r.get("a_kind") == "logQ2" and safe_float(r.get("m0")) >= m_min]

        # A. smallest A(logQ^2)
        for idx, row in sorted(enumerate(logq2),
                               key=lambda ir: safe_float(ir[1].get("A_sup"),
                                                          float("inf")))[:top_k]:
            t = make_target("v1_smallest_A_logQ2", row, path, idx)
            if t:
                out.append(t)

        # B. smallest J_max
        for idx, row in sorted(enumerate(logq2),
                               key=lambda ir: safe_float(ir[1].get("J_max"),
                                                          float("inf")))[:top_k]:
            t = make_target("v1_smallest_Jmax", row, path, idx)
            if t:
                out.append(t)

        # C. combined threat score
        scored: List[Tuple[float, int, Dict[str, str]]] = []
        for idx, row in enumerate(logq2):
            R = safe_int(row.get("R"))
            Q = safe_float(row.get("Q"))
            Z0 = safe_float(row.get("Z0_abs"))
            A = safe_float(row.get("A_sup"))
            J = safe_float(row.get("J_max"))
            N = safe_float(row.get("N_minima_thresholded"), 0.0)
            if R > 0 and Q > 1:
                score = (Z0 + EPS) * (A + EPS) * (J + EPS) / (1.0 + max(N, 0.0))
                scored.append((score, idx, row))
        for _, idx, row in sorted(scored, key=lambda x: x[0])[:top_k]:
            t = make_target("v1_best_threat_score", row, path, idx)
            if t:
                out.append(t)

        # E. largest minima crowding (descending by N_minima_thresholded)
        for idx, row in sorted(enumerate(logq2),
                               key=lambda ir: safe_float(
                                   ir[1].get("N_minima_thresholded"), 0.0),
                               reverse=True)[:top_k]:
            t = make_target("v1_largest_minima_crowding", row, path, idx)
            if t:
                out.append(t)

    return out


def collect_from_determinant(csv_paths: Sequence[str], etaZ_cut_abs: float,
                             etaZ_cut_power: float, best_by_stage: bool,
                             top_k: int, m_min: float) -> List[Target]:
    out: List[Target] = []
    grouped: Dict[Tuple[str, str, int], List[Tuple[int, Dict[str, str], str]]] = {}

    for path in csv_paths:
        if not os.path.exists(path):
            continue
        rows = read_csv_rows(path)
        for idx, row in enumerate(rows):
            R = safe_int(row.get("R"))
            Q = safe_float(row.get("Q"))
            m = safe_float(row.get("m"))
            etaZ = safe_float(row.get("eta_Z"))
            if not (R > 0 and Q > 0 and math.isfinite(m) and m >= m_min):
                continue
            threshold = min(etaZ_cut_abs, Q ** (-etaZ_cut_power))
            if math.isfinite(etaZ) and etaZ <= threshold:
                t = make_target("det_small_etaZ", row, path, idx)
                if t:
                    out.append(t)
            grouped.setdefault((row.get("config_name", ""),
                                row.get("stage", ""), R), []
                              ).append((idx, row, path))

    if best_by_stage:
        for _key, items in grouped.items():
            items_sorted = sorted(items,
                                  key=lambda ir: safe_float(ir[1].get("eta_Z"),
                                                            float("inf")))
            for idx, row, path in items_sorted[:top_k]:
                t = make_target("det_best_etaZ_by_stage", row, path, idx)
                if t:
                    out.append(t)

    return out


def random_targets(count: int, R_values: Sequence[int], c_values: Sequence[float],
                   Q_mode: str, m_min: float, m_max_factor: float,
                   seed: int) -> List[Target]:
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
        out.append(Target(target_id=tid, kind=kind, R=R, Q=Q, alpha=alpha,
                          m0=m0, c=c))
    return out


def jet_objective_at(model: ZModel, m: float, cfg: Dict[str, Any]) -> float:
    Z0 = abs(model.Z(m))
    Q = model.Q
    CZ = float(cfg.get("C_Z", 6.0))
    CJ = float(cfg.get("C_J", 4.0))
    Jsum = 0.0
    for k in range(1, model.R + 2):
        d = model.derivative_t_at(m, k)
        v = abs(d) / float(math.factorial(k))
        Jsum += v * v
    return (Q ** CZ * Z0) ** 2 + (Q ** (2.0 * CJ)) * Jsum


def _direct_jet_minimizer_one_block(task: tuple) -> List[Target]:
    """One (R, c) block's direct jet minimizer search. Worker function."""
    (R, Q, c, m_lo, m_hi, scan_grid, count_per_block, k_Z, include_dual,
     max_primes, cfg, support_blocks) = task
    out: List[Target] = []
    try:
        block = build_prime_block(R, Q, c, max_primes,
                                  support_blocks=support_blocks)
        model = build_z_model(block, alpha=0.0, k_Z=k_Z,
                              include_dual=include_dual)
    except Exception:
        return out

    m_grid = np.linspace(m_lo, m_hi, scan_grid)
    vals = np.array([jet_objective_at(model, float(m), cfg) for m in m_grid])
    best_idx = np.argsort(vals)[:count_per_block]
    for idx in best_idx:
        m0 = float(m_grid[int(idx)])
        if _opt is not None:
            def obj(x):
                m = float(x[0])
                if m < m_lo or m > m_hi:
                    return 1e100
                return jet_objective_at(model, m, cfg)
            try:
                res = _opt.minimize(obj, np.array([m0]),
                                    method="Nelder-Mead",
                                    options={"maxiter": 120, "xatol": 1e-6})
                m0 = float(np.clip(res.x[0], m_lo, m_hi))
            except Exception:
                pass
        kind = "direct_jet_minimizer"
        tid = target_hash(kind, R, Q, 0.0, m0, c)
        out.append(Target(target_id=tid, kind=kind, R=R, Q=Q,
                          alpha=0.0, m0=m0, c=c))
    return out


def generate_jet_minimizer_targets(cfg: Dict[str, Any],
                                   workers: int = 1) -> List[Target]:
    count_per_block = int(cfg.get("direct_jet_minimizers", 0))
    if count_per_block <= 0:
        return []

    R_values = [int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12, 16])]
    c_values = [float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])]
    Q_mode = str(cfg.get("Q_mode", "larger_toy"))
    m_min = float(cfg.get("m_min", 50.0))
    m_max_factor = float(cfg.get("m_max_factor", 100.0))
    include_dual = bool(cfg.get("include_dual", False))
    k_Z = int(cfg.get("k_Z", 0))
    max_primes = int(cfg.get("max_primes", 8000))
    scan_grid = int(cfg.get("jet_minimizer_grid", 400))
    support_blocks = float(cfg.get("support_blocks", 1.0))

    cfg_constants = {
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_J": float(cfg.get("C_J", 4.0)),
    }

    tasks: List[tuple] = []
    for R in R_values:
        Q = choose_Q_for_R(R, Q_mode)
        for c in c_values:
            tasks.append((R, Q, c, m_min, m_max_factor * Q, scan_grid,
                          count_per_block, k_Z, include_dual, max_primes,
                          cfg_constants, support_blocks))

    out: List[Target] = []
    if workers <= 1 or len(tasks) <= 1:
        for t in tasks:
            out.extend(_direct_jet_minimizer_one_block(t))
        return out

    try:
        ctx = _mp.get_context("fork")
    except ValueError:
        ctx = _mp.get_context("spawn")
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
        for fut in as_completed([pool.submit(_direct_jet_minimizer_one_block, t)
                                 for t in tasks]):
            out.extend(fut.result())
    return out


def dedupe_targets(targets: Sequence[Target]) -> List[Target]:
    seen: set = set()
    out: List[Target] = []
    for t in targets:
        key = (t.kind, t.R, round(t.Q, 10), round(t.alpha, 12),
               round(t.m0, 8), round(t.c, 8))
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


def evaluate_window(model: ZModel, m0: float, a: float,
                    cfg: Dict[str, Any]) -> Dict[str, Any]:
    N_grid = max(int(cfg.get("min_grid_floor", 401)),
                 int(int(cfg.get("min_grid_factor", 40)) * a * model.R))
    N_grid = min(N_grid, int(cfg.get("max_grid", 10001)))
    t_grid = np.linspace(-a, a, N_grid)
    m_grid = m0 + model.lam * t_grid
    vals = np.abs(model.Z_grid(m_grid))

    idx_max = int(np.argmax(vals))
    A_grid = float(vals[idx_max])
    t_at_A = float(t_grid[idx_max])
    A_sup = A_grid
    if _opt is not None:
        try:
            def obj_max(x):
                t = float(x[0])
                if t < -a or t > a:
                    return 1e100
                return -abs(model.Z(m0 + model.lam * t))
            res = _opt.minimize(obj_max, np.array([t_at_A]),
                                method="Nelder-Mead",
                                options={"maxiter": 80, "xatol": 1e-6})
            t_ref = float(np.clip(res.x[0], -a, a))
            A_ref = abs(model.Z(m0 + model.lam * t_ref))
            if A_ref > A_sup:
                A_sup = float(A_ref)
                t_at_A = t_ref
        except Exception:
            pass

    L2_amp = float(math.sqrt(np.trapezoid(vals * vals, t_grid)))

    minima_idx = find_local_minima_indices(vals)
    refined: List[Tuple[float, float]] = []
    for i in minima_idx:
        t0 = float(t_grid[i])
        v0 = float(vals[i])
        if _opt is not None:
            try:
                def obj_min(x):
                    t = float(x[0])
                    if t < -a or t > a:
                        return 1e100
                    return abs(model.Z(m0 + model.lam * t))
                res = _opt.minimize(obj_min, np.array([t0]),
                                    method="Nelder-Mead",
                                    options={"maxiter": 80, "xatol": 1e-6})
                t_ref = float(np.clip(res.x[0], -a, a))
                v_ref = abs(model.Z(m0 + model.lam * t_ref))
                refined.append((t_ref, float(v_ref)))
            except Exception:
                refined.append((t0, v0))
        else:
            refined.append((t0, v0))

    if refined:
        t_min, v_min = min(refined, key=lambda tv: tv[1])
    else:
        i_min = int(np.argmin(vals))
        t_min, v_min = float(t_grid[i_min]), float(vals[i_min])

    threshold = model.Q ** (-float(cfg.get("C_Z", 6.0)))
    N_thresh = sum(1 for _, v in refined if v <= threshold)

    return {
        "A_sup": A_sup,
        "t_at_A_sup": t_at_A,
        "L2_amp": L2_amp,
        "min_Z": float(v_min),
        "m_at_min_Z": m0 + model.lam * float(t_min),
        "N_minima": len(refined),
        "N_minima_thresholded": N_thresh,
        "N_grid": N_grid,
    }


def compute_jets(model: ZModel, m0: float) -> Tuple[float, float, float, int]:
    vals: List[float] = []
    for k in range(1, model.R + 2):
        d = model.derivative_t_at(m0, k)
        vals.append(abs(d) / float(math.factorial(k)))
    arr = np.asarray(vals, dtype=float)
    if len(arr) == 0:
        return float("nan"), float("nan"), float("nan"), -1
    return (float(np.max(arr)),
            float(np.sqrt(np.sum(arr * arr))),
            float(np.sum(arr * arr)),
            int(np.argmax(arr) + 1))


def compute_cell_sums(model: ZModel, m0: float, M_cell: int) -> Dict[str, Any]:
    """
    Combined plus + minus cell sums. plus operator nodes are +lambda*log p,
    minus operator nodes are -lambda*log p; bins span [min(x_all), max(x_all)]
    so plus contributions land in positive cells and minus in negative cells.
    The returned B_r = B_r^+ + B_r^- automatically (each cell typically
    contains contributions from one branch only).
    """
    x_plus = model.lam * model.logs
    z_plus = model.plus_coeffs * np.exp(-1j * m0 * model.logs)

    if model.include_dual and model.minus_coeffs is not None:
        x_minus = -model.lam * model.logs
        z_minus = model.minus_coeffs * np.exp(+1j * m0 * model.logs)
        x_all = np.concatenate([x_plus, x_minus])
        z_all = np.concatenate([z_plus, z_minus])
    else:
        x_all = x_plus
        z_all = z_plus

    if len(x_all) == 0:
        return {"cell_count": M_cell, "cell_mass_l2": float("nan"),
                "cell_mass_inf": float("nan"),
                "cell_mass_ratio": float("nan"),
                "active_cell_count": 0}

    mn = float(np.min(x_all))
    mx = float(np.max(x_all))
    if mx <= mn:
        mx = mn + 1.0
    bins = np.linspace(mn, mx, M_cell + 1)
    inds = np.searchsorted(bins, x_all, side="right") - 1
    inds = np.clip(inds, 0, M_cell - 1)
    B = np.zeros(M_cell, dtype=np.complex128)
    np.add.at(B, inds, z_all)
    cell_l2 = float(np.sum(np.abs(B) ** 2))
    cell_inf = float(np.max(np.abs(B)))
    coeff_l2 = float(np.sum(np.abs(z_all) ** 2))
    active = int(np.sum(np.abs(B) > 0))
    return {
        "cell_count": M_cell,
        "cell_mass_l2": cell_l2,
        "cell_mass_inf": cell_inf,
        "cell_mass_ratio": cell_l2 / max(coeff_l2, EPS),
        "active_cell_count": active,
    }


def classify_v2(metrics: Dict[str, Any], cfg: Dict[str, Any]) -> str:
    Q = float(metrics["Q"])
    R = int(metrics["R"])
    CZ = float(cfg.get("C_Z", 6.0))
    CA = float(cfg.get("C_A", 4.0))
    CJ = float(cfg.get("C_J", 4.0))
    Ccell = float(cfg.get("C_cell", 4.0))
    C0 = float(cfg.get("C0_crowd", 4.0))

    Z0 = float(metrics["Z0_abs"])
    Jm = float(metrics["J_max"])
    A_R = float(metrics["A_R"])
    A_lq = float(metrics["A_logQ2"])
    Nlq = int(metrics["N_min_logQ2"])
    cell2R = float(metrics["cell_mass_ratio_2R"])

    z_small = math.isfinite(Z0) and Z0 <= Q ** (-CZ)
    jet_small = math.isfinite(Jm) and Jm <= Q ** (-CJ)
    A_R_small = math.isfinite(A_R) and A_R <= Q ** (-CA)
    A_lq_small = math.isfinite(A_lq) and A_lq <= Q ** (-CA)
    crowded = Nlq > C0 * R
    cell_small = math.isfinite(cell2R) and cell2R <= Q ** (-Ccell)

    support_blocks = float(metrics.get("support_blocks", 1.0))

    if z_small and jet_small and A_lq_small and crowded and cell_small:
        verdict = "red_local_amplitude_threat"
    elif z_small and jet_small and cell_small and not A_lq_small:
        verdict = "orange_cell_warning"
    elif z_small and jet_small and A_R_small and not A_lq_small:
        verdict = "yellow_local_flatness"
    elif z_small and not A_lq_small:
        verdict = "z_small_but_amplitude_ok"
    else:
        verdict = "harmless"

    # Cell-mass diagnostic degenerates on a single (Q/R)-width block
    # (only ~1 active cell), so demote Orange/Red verdicts that depend on
    # cell_mass_ratio to a separate label until support_blocks > 1.
    if support_blocks <= 1.0 and verdict in {
        "orange_cell_warning", "red_local_amplitude_threat"
    }:
        return "single_block_cell_diagnostic"

    # Coverage guards: even with K > 1, the block can be undercovered if
    # max_primes truncated the sample or active cells are too sparse.
    actual_lambda_width = float(metrics.get("actual_lambda_width", float("nan")))
    nominal_lambda_width = support_blocks / max(R, 1)
    if (math.isfinite(actual_lambda_width)
            and actual_lambda_width < 0.5 * nominal_lambda_width
            and verdict in {"orange_cell_warning", "red_local_amplitude_threat"}):
        return "undercovered_support_diagnostic"

    active2R = int(metrics.get("active_cell_count_2R", 0))
    # ceil to avoid aggressive flooring for non-integer K, and bump the
    # floor so a meaningful multi-block cell test really has at least
    # ceil(K/2) active cells (per audit recommendation).
    min_active = max(4, int(math.ceil(support_blocks / 2.0)))
    if (active2R < min_active
            and verdict in {"orange_cell_warning", "red_local_amplitude_threat"}):
        return "undercovered_cell_diagnostic"

    # Out-of-band guard: if c + K/R exceeds c_max_eff_limit, the wide block
    # leaves the intended (c < c_max) region. Demote Orange/Red to a
    # diagnostic class rather than treat as evidence.
    c_val = float(metrics.get("c", 0.0))
    c_max_eff = c_val + support_blocks / max(R, 1)
    c_max_eff_limit = float(cfg.get("c_max_eff_limit", 1.0))
    if (c_max_eff > c_max_eff_limit
            and verdict in {"orange_cell_warning", "red_local_amplitude_threat"}):
        return "out_of_band_diagnostic"

    return verdict


# ============================================================
# Per-target / per-group worker
# ============================================================

def _evaluate_target_with_model(target: Target, model: ZModel,
                                cfg: Dict[str, Any], run_id: str,
                                config_name: str,
                                block: PrimeBlock) -> ResultRow:
    Z0 = abs(model.Z(target.m0))
    eta_Z0 = Z0 / max(model.coeff_norm, EPS)
    J_max, J_rms, J_sum_sq, J_argmax_k = compute_jets(model, target.m0)

    windows = {
        "1": 1.0,
        "R": float(target.R),
        "2R": float(2 * target.R),
        "logQ2": float(math.log(target.Q) ** 2),
    }
    ev: Dict[str, Dict[str, Any]] = {}
    for key, a in windows.items():
        ev[key] = evaluate_window(model, target.m0, a, cfg)

    cells_R = compute_cell_sums(model, target.m0, max(1, target.R))
    cells_2R = compute_cell_sums(model, target.m0, max(1, 2 * target.R))
    cells_4R = compute_cell_sums(model, target.m0, max(1, 4 * target.R))

    metrics = {
        "R": target.R, "Q": target.Q, "Z0_abs": Z0, "J_max": J_max,
        "A_R": ev["R"]["A_sup"], "A_logQ2": ev["logQ2"]["A_sup"],
        "N_min_logQ2": ev["logQ2"]["N_minima_thresholded"],
        "cell_mass_ratio_2R": cells_2R["cell_mass_ratio"],
        "support_blocks": block.support_blocks,
        "actual_lambda_width": block.actual_lambda_width,
        "active_cell_count_2R": cells_2R["active_cell_count"],
        "c": target.c,
    }
    cls = classify_v2(metrics, cfg)
    threat = (Z0 + EPS) * (J_max + EPS) * (ev["logQ2"]["A_sup"] + EPS) / (
        1.0 + max(ev["logQ2"]["N_minima_thresholded"], 0))
    Q = target.Q
    CZ = float(cfg.get("C_Z", 6.0))
    CJ = float(cfg.get("C_J", 4.0))
    jet_obj = (Q ** CZ * Z0) ** 2 + (Q ** (2.0 * CJ)) * J_sum_sq

    return ResultRow(
        run_id=run_id,
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        config_name=config_name,
        target_id=target.target_id,
        target_class=target.kind,
        target_generation_method=target.kind,
        source_csv=target.source_csv,
        source_row_index=target.source_row_index,
        source_config=target.source_config,
        source_stage=target.source_stage,
        source_a_kind=target.source_a_kind,
        source_eta_Z=target.source_eta_Z,
        source_eta_W=target.source_eta_W,
        source_A_sup=target.source_A_sup,
        source_J_max=target.source_J_max,
        source_N_minima=target.source_N_minima,
        source_rho_rank=target.source_rho_rank,
        source_kappa_basis=target.source_kappa_basis,
        R=target.R, Q=target.Q, lambda_=model.lam, c=target.c,
        alpha=target.alpha, m0=target.m0,
        num_primes=int(len(model.primes)),
        include_dual=model.include_dual, k_Z=model.k_Z,
        support_blocks=block.support_blocks,
        u_min=block.u_min, u_max=block.u_max,
        lambda_width=block.lambda_width,
        actual_u_min=block.actual_u_min,
        actual_u_max=block.actual_u_max,
        actual_lambda_width=block.actual_lambda_width,
        sampling_mode=block.sampling_mode,
        Z0_abs=Z0, eta_Z0=eta_Z0,
        A_1=ev["1"]["A_sup"], A_R=ev["R"]["A_sup"],
        A_2R=ev["2R"]["A_sup"], A_logQ2=ev["logQ2"]["A_sup"],
        L2_1=ev["1"]["L2_amp"], L2_R=ev["R"]["L2_amp"],
        L2_2R=ev["2R"]["L2_amp"], L2_logQ2=ev["logQ2"]["L2_amp"],
        min_Z_1=ev["1"]["min_Z"], min_Z_R=ev["R"]["min_Z"],
        min_Z_2R=ev["2R"]["min_Z"], min_Z_logQ2=ev["logQ2"]["min_Z"],
        m_at_min_Z_logQ2=ev["logQ2"]["m_at_min_Z"],
        N_min_1=ev["1"]["N_minima_thresholded"],
        N_min_R=ev["R"]["N_minima_thresholded"],
        N_min_2R=ev["2R"]["N_minima_thresholded"],
        N_min_logQ2=ev["logQ2"]["N_minima_thresholded"],
        N_min_ratio_logQ2=ev["logQ2"]["N_minima_thresholded"] / max(target.R, 1),
        J_max=J_max, J_rms=J_rms, J_sum_sq=J_sum_sq, J_argmax_k=J_argmax_k,
        cell_count_R=cells_R["cell_count"],
        cell_mass_l2_R=cells_R["cell_mass_l2"],
        cell_mass_inf_R=cells_R["cell_mass_inf"],
        cell_mass_ratio_R=cells_R["cell_mass_ratio"],
        active_cell_count_R=cells_R["active_cell_count"],
        cell_count_2R=cells_2R["cell_count"],
        cell_mass_l2_2R=cells_2R["cell_mass_l2"],
        cell_mass_inf_2R=cells_2R["cell_mass_inf"],
        cell_mass_ratio_2R=cells_2R["cell_mass_ratio"],
        active_cell_count_2R=cells_2R["active_cell_count"],
        cell_count_4R=cells_4R["cell_count"],
        cell_mass_l2_4R=cells_4R["cell_mass_l2"],
        cell_mass_inf_4R=cells_4R["cell_mass_inf"],
        cell_mass_ratio_4R=cells_4R["cell_mass_ratio"],
        active_cell_count_4R=cells_4R["active_cell_count"],
        threat_score=float(threat),
        jet_objective=float(jet_obj),
        classification=cls,
        notes="",
    )


def _failed_row(run_id: str, config_name: str, target: Target,
                include_dual: bool, k_Z: int, msg: str,
                support_blocks: float = 1.0) -> ResultRow:
    nan = float("nan")
    u_min = target.c * target.Q
    u_max = u_min + support_blocks * target.Q / max(target.R, 1)
    return ResultRow(
        run_id=run_id, timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
        config_name=config_name,
        target_id=target.target_id, target_class=target.kind,
        target_generation_method=target.kind,
        source_csv=target.source_csv, source_row_index=target.source_row_index,
        source_config=target.source_config, source_stage=target.source_stage,
        source_a_kind=target.source_a_kind,
        source_eta_Z=target.source_eta_Z, source_eta_W=target.source_eta_W,
        source_A_sup=target.source_A_sup, source_J_max=target.source_J_max,
        source_N_minima=target.source_N_minima,
        source_rho_rank=target.source_rho_rank,
        source_kappa_basis=target.source_kappa_basis,
        R=target.R, Q=target.Q, lambda_=1.0 / target.Q, c=target.c,
        alpha=target.alpha, m0=target.m0, num_primes=0,
        include_dual=include_dual, k_Z=k_Z,
        support_blocks=float(support_blocks),
        u_min=u_min, u_max=u_max,
        lambda_width=(u_max - u_min) / target.Q,
        actual_u_min=nan, actual_u_max=nan, actual_lambda_width=nan,
        sampling_mode="failed",
        Z0_abs=nan, eta_Z0=nan,
        A_1=nan, A_R=nan, A_2R=nan, A_logQ2=nan,
        L2_1=nan, L2_R=nan, L2_2R=nan, L2_logQ2=nan,
        min_Z_1=nan, min_Z_R=nan, min_Z_2R=nan, min_Z_logQ2=nan,
        m_at_min_Z_logQ2=nan,
        N_min_1=0, N_min_R=0, N_min_2R=0, N_min_logQ2=0,
        N_min_ratio_logQ2=nan,
        J_max=nan, J_rms=nan, J_sum_sq=nan, J_argmax_k=-1,
        cell_count_R=0, cell_mass_l2_R=nan, cell_mass_inf_R=nan,
        cell_mass_ratio_R=nan, active_cell_count_R=0,
        cell_count_2R=0, cell_mass_l2_2R=nan, cell_mass_inf_2R=nan,
        cell_mass_ratio_2R=nan, active_cell_count_2R=0,
        cell_count_4R=0, cell_mass_l2_4R=nan, cell_mass_inf_4R=nan,
        cell_mass_ratio_4R=nan, active_cell_count_4R=0,
        threat_score=nan, jet_objective=nan,
        classification="failed", notes=msg[:200],
    )


def _process_group(task: tuple) -> List[ResultRow]:
    """One worker task = all targets sharing a (R, Q, c) prime block."""
    (run_id, config_name, R, Q, c_val, targets, cfg, include_dual,
     k_Z, max_primes, support_blocks) = task
    rows: List[ResultRow] = []

    block: Optional[PrimeBlock] = None
    cached: Dict[float, ZModel] = {}

    for tgt in targets:
        try:
            if block is None:
                block = build_prime_block(R, Q, c_val, max_primes,
                                          support_blocks=support_blocks)
            akey = round(tgt.alpha, 14)
            model = cached.get(akey)
            if model is None:
                model = build_z_model(block, alpha=tgt.alpha, k_Z=k_Z,
                                      include_dual=include_dual)
                cached[akey] = model
        except Exception as e:
            rows.append(_failed_row(run_id, config_name, tgt, include_dual,
                                    k_Z, str(e), support_blocks=support_blocks))
            continue

        try:
            rows.append(_evaluate_target_with_model(tgt, model, cfg,
                                                    run_id, config_name,
                                                    block))
        except Exception as e:
            rows.append(_failed_row(run_id, config_name, tgt, include_dual,
                                    k_Z, str(e), support_blocks=support_blocks))
    return rows


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
        return
    with open(out_path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return
    log(f"=== Summary: {config_name} ({len(rows)} rows) ===")
    counts: Dict[str, int] = {}
    for r in rows:
        counts[r.get("classification", "")] = counts.get(
            r.get("classification", ""), 0) + 1
    log("classification counts:")
    for k in sorted(counts):
        log(f"  {k}: {counts[k]}")

    by_kind: Dict[str, int] = {}
    for r in rows:
        by_kind[r.get("target_class", "")] = by_kind.get(
            r.get("target_class", ""), 0) + 1
    log("target_class counts:")
    for k in sorted(by_kind):
        log(f"  {k}: {by_kind[k]}")

    def f(x: str) -> float:
        return safe_float(x, float("inf"))

    flagged_classes = {"red_local_amplitude_threat", "orange_cell_warning",
                       "yellow_local_flatness", "z_small_but_amplitude_ok"}
    flagged = [r for r in rows if r.get("classification") in flagged_classes]
    log(f"flagged rows: {len(flagged)}")
    for r in flagged[:20]:
        log(f"  FLAG {r.get('classification')}: target_class={r.get('target_class')} "
            f"R={r.get('R')} c={r.get('c')} m0={f(r.get('m0')):.6e} "
            f"Z0={f(r.get('Z0_abs')):.3e} A_R={f(r.get('A_R')):.3e} "
            f"A_logQ2={f(r.get('A_logQ2')):.3e} J_max={f(r.get('J_max')):.3e} "
            f"cell2R={f(r.get('cell_mass_ratio_2R')):.3e} "
            f"Nlog={r.get('N_min_logQ2')}")

    # Top-10 smallest threat_score
    rows.sort(key=lambda r: f(r.get("threat_score")))
    log("Top-10 smallest threat_score:")
    for r in rows[:10]:
        log(f"  cls={r.get('classification')} target_class={r.get('target_class')} "
            f"R={r.get('R')} c={r.get('c')} m0={f(r.get('m0')):.6e} "
            f"Z0={f(r.get('Z0_abs')):.3e} A_logQ2={f(r.get('A_logQ2')):.3e} "
            f"J_max={f(r.get('J_max')):.3e} "
            f"cell2R={f(r.get('cell_mass_ratio_2R')):.3e} "
            f"threat={f(r.get('threat_score')):.3e}")


# ============================================================
# Path resolution + main
# ============================================================

def resolve_paths(paths: Sequence[str]) -> List[str]:
    out: List[str] = []
    cwd = os.getcwd()
    for p in paths:
        if os.path.isabs(p) and os.path.exists(p):
            out.append(p); continue
        candidates = [
            p,
            os.path.join(cwd, p),
            os.path.join(_SCRIPT_DIR, p),
            os.path.join(_SCRIPT_DIR, "out", p),
            os.path.join(_SCRIPT_DIR, "out", "v1", p),
            os.path.join(_AGENT_B5_DIR, "out", p),
        ]
        found: Optional[str] = None
        for q in candidates:
            if os.path.exists(q):
                found = os.path.abspath(q)
                break
        out.append(found or p)
    return out


def collect_targets(cfg: Dict[str, Any], v1_paths: Sequence[str],
                    det_paths: Sequence[str]) -> List[Target]:
    targets: List[Target] = []
    top_k = int(cfg.get("top_k", 5))
    m_min = float(cfg.get("m_min", 50.0))

    targets += collect_from_v1_amplitude(v1_paths, top_k=top_k, m_min=m_min)
    targets += collect_from_determinant(
        det_paths,
        etaZ_cut_abs=float(cfg.get("etaZ_cut_abs", 1e-3)),
        etaZ_cut_power=float(cfg.get("etaZ_cut_power", 3.0)),
        best_by_stage=bool(cfg.get("best_by_stage", True)),
        top_k=top_k, m_min=m_min,
    )
    rc = int(cfg.get("random_controls", 100))
    if rc > 0:
        targets += random_targets(
            rc,
            R_values=[int(x) for x in cfg.get("R_values", [4, 6, 8, 10, 12, 16])],
            c_values=[float(x) for x in cfg.get("c_values", [0.1, 0.2, 0.3, 0.4])],
            Q_mode=str(cfg.get("Q_mode", "larger_toy")),
            m_min=m_min,
            m_max_factor=float(cfg.get("m_max_factor", 100.0)),
            seed=int(cfg.get("seed", 12345)),
        )
    targets += generate_jet_minimizer_targets(cfg, workers=int(cfg.get("workers", 1)))

    targets = dedupe_targets(targets)

    def score(t: Target) -> Tuple[int, float]:
        if t.kind == "direct_jet_minimizer":
            return (0, 0.0)
        if math.isfinite(t.source_A_sup):
            return (1, t.source_A_sup)
        if math.isfinite(t.source_J_max):
            return (2, t.source_J_max)
        if math.isfinite(t.source_eta_Z):
            return (3, t.source_eta_Z)
        return (9, 1e99)

    targets.sort(key=score)
    cap = int(cfg.get("max_targets", 800))
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
    cfg["workers"] = workers  # share with target-generation parallelism

    v1_paths = resolve_paths(cfg.get("v1_amplitude_csv", []))
    det_paths = resolve_paths(cfg.get("det_csv", []))
    all_inputs = v1_paths + det_paths

    out_stem = str(cfg.get("output", _default_out(f"{config_name}.csv")))
    if not os.path.isabs(out_stem) and os.sep not in out_stem:
        out_stem = _default_out(out_stem)
    params_hash = compute_params_hash(cfg, config_name, all_inputs)
    out_path = derive_output_path(out_stem, params_hash)

    log(f"config: {config_name}")
    log(f"workers: {workers}")
    log(f"include_dual: {cfg.get('include_dual', False)}  k_Z: {cfg.get('k_Z', 0)}  "
        f"support_blocks: {cfg.get('support_blocks', 1.0)}")
    log(f"input files:")
    for p in all_inputs:
        log(f"  - {p} ({'ok' if os.path.exists(p) else 'MISSING'})")
    log(f"params hash: {params_hash[:12]} (full: {params_hash})")
    log(f"output: {out_path}")

    targets = collect_targets(cfg, v1_paths, det_paths)
    log(f"targets: {len(targets)}")
    by_kind: Dict[str, int] = {}
    for t in targets:
        by_kind[t.kind] = by_kind.get(t.kind, 0) + 1
    for k in sorted(by_kind):
        log(f"  target {k}: {by_kind[k]}")

    groups = group_targets_by_block(targets)
    log(f"prime-block groups: {len(groups)}")

    resume = bool(cfg.get("resume", True))
    existing_keys: set = load_existing_keys(out_path) if resume else set()
    if existing_keys:
        log(f"resume: {len(existing_keys)} existing rows; will dedupe by row key.")

    run_id = str(uuid.uuid4())[:8]
    include_dual = bool(cfg.get("include_dual", False))
    k_Z = int(cfg.get("k_Z", 0))
    max_primes = int(cfg.get("max_primes", 8000))
    support_blocks = float(cfg.get("support_blocks", 1.0))

    cfg_for_workers = {
        "C_Z": float(cfg.get("C_Z", 6.0)),
        "C_A": float(cfg.get("C_A", 4.0)),
        "C_J": float(cfg.get("C_J", 4.0)),
        "C_cell": float(cfg.get("C_cell", 4.0)),
        "C0_crowd": float(cfg.get("C0_crowd", 4.0)),
        "c_max_eff_limit": float(cfg.get("c_max_eff_limit", 1.0)),
        "min_grid_floor": int(cfg.get("min_grid_floor", 401)),
        "min_grid_factor": int(cfg.get("min_grid_factor", 40)),
        "max_grid": int(cfg.get("max_grid", 10001)),
    }

    tasks: List[tuple] = []
    for (R, Q, c_val), tgts in sorted(groups.items()):
        tasks.append((run_id, config_name, R, Q, c_val, tgts, cfg_for_workers,
                      include_dual, k_Z, max_primes, support_blocks))
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
    print_summary(out_path, config_name)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=None, help="JSON config file")
    p.add_argument("--output", default=None,
                   help="output CSV stem (params hash inserted)")
    p.add_argument("--workers", type=int, default=None,
                   help="process-pool size; default cpu_count - 2")
    p.add_argument("--no-resume", action="store_true",
                   help="ignore existing CSV at this hash and re-emit all rows")
    p.add_argument("--include-dual", action="store_true",
                   help="include reflected log-derivative dual branch")
    return p.parse_args()


if __name__ == "__main__":
    run(parse_args())
