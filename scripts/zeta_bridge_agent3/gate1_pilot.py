#!/usr/bin/env python3
"""
Gate 1 pilot harness.

Modes:
  controls  - deterministic same-scale quadrature negative control + singular dominance control
  actual    - zero-kernel-only proxy scan using zeta zero ordinates from mpmath
  all       - controls + actual

Outputs CSV files in --outdir.

This is NOT the final canonical q''_can computation. The actual-zero scan uses:
  qpp_zero_eps(m) = sum_gamma K2(m; gamma, eps)
with
  K(m; gamma, eps) = eps / ((m-gamma)^2 + eps^2)
  K2 = d^2/dm^2 K
as a labeled zero-kernel-only proxy.
"""

from __future__ import annotations

import os

# Pin BLAS / OpenMP to 1 thread per process. We parallelize at the center
# level via multiprocessing; with 30 workers each trying to spawn 32 OpenMP
# threads, the first batch was thrashing for ~12 minutes before the OS
# balanced affinity. Set these before numpy is imported.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import argparse
import csv
import hashlib
import json
import math
import multiprocessing as mp_proc
import random
import sys
import time
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import warnings

import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

warnings.filterwarnings("ignore", category=np.exceptions.RankWarning)


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))


def _default_out(*parts: str) -> str:
    """Resolve <script_dir>/out/<parts...>; unified outputs location."""
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


# ----------------------------
# Utility
# ----------------------------

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def safe_log(x: float, floor: float = 1e-300) -> float:
    return math.log(max(float(x), floor))


def write_csv(path: str, rows: List[Dict]) -> None:
    if not rows:
        return
    keys = sorted({k for row in rows for k in row.keys()})
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def summarize_top(rows: List[Dict], key: str, n: int = 10, reverse: bool = True) -> List[Dict]:
    clean = [r for r in rows if key in r and isinstance(r[key], (int, float)) and math.isfinite(r[key])]
    return sorted(clean, key=lambda r: r[key], reverse=reverse)[:n]


# ----------------------------
# Negative control: same-scale quadrature
# ----------------------------

def quadrature_nodes_weights(R: int, N: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Deterministic sine quadrature:
      theta_j = j*pi/(N+1)
      w_j = 2/(N+1) sin(theta_j)
    For 1 <= k <= N:
      sum_j w_j sin(k theta_j) = delta_{k1}
    """
    if N is None:
        N = R + 3
    j = np.arange(1, N + 1, dtype=float)
    theta = j * math.pi / (N + 1)
    w = 2.0 / (N + 1) * np.sin(theta)
    return theta, w


def Ktheta(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    K_theta(x) = sin(theta) / ((x - cos(theta))^2 + sin(theta)^2)
    Vectorized over x and theta.
    Returns shape (len(x), len(theta)).
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    den = (xx - c) ** 2 + s ** 2
    return s / den


def Ktheta_second(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    d^2/dx^2 K_theta(x)
    = 2s(3y^2 - s^2)/(y^2+s^2)^3, y=x-cos(theta).
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y ** 2 + s ** 2
    return 2.0 * s * (3.0 * y ** 2 - s ** 2) / (den ** 3)


def integrate_on_interval_values(func_values: Callable[[np.ndarray], np.ndarray],
                                 a: float,
                                 b: float,
                                 n_nodes: int = 1001) -> Tuple[float, float]:
    """
    Integrate |f|^2 over [a,b] and compute sampled sup norm.
    """
    xs, ws = leggauss(n_nodes)
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)
    pts = mid + half * xs
    vals = func_values(pts)
    integral = half * float(np.sum(ws * vals * vals))
    supnorm = float(np.max(np.abs(vals)))
    return integral, supnorm


def run_negative_control(outdir: str) -> List[Dict]:
    rows: List[Dict] = []
    for R in [12, 24, 40]:
        N = R + 3
        theta, w = quadrature_nodes_weights(R, N=N)

        # Moment checks through R+3
        residuals = []
        for k in range(1, R + 4):
            target = 1.0 if k == 1 else 0.0
            val = float(np.sum(w * np.sin(k * theta)))
            residuals.append(abs(val - target))
        moment_max = max(residuals)

        for X0 in [0.25, 0.5, 0.75]:
            def F_vals(x: np.ndarray) -> np.ndarray:
                return Ktheta_second(theta, x).dot(w)

            integral, S_X = integrate_on_interval_values(F_vals, -X0, X0, n_nodes=1001)
            E_X = integral / (2.0 * X0)

            # Approximate jets by fitting F near 0; exact moments already validate jets.
            h = min(1e-3, X0 / 200.0)
            stencil = np.arange(-80, 81, dtype=float) * h
            y = F_vals(stencil)
            deg = min(80, R + 12)
            coeffs = np.polynomial.polynomial.polyfit(stencil, y, deg)
            jets = []
            for r in range(R + 1):
                jets.append(math.factorial(r) * coeffs[r])
            jet_max = float(np.max(np.abs(jets)))

            rows.append({
                "control": "sine_quadrature_negative",
                "R": R,
                "N": N,
                "X0": X0,
                "moment_max": moment_max,
                "jet_max_fit_proxy": jet_max,
                "E_X": E_X,
                "S_X": S_X,
                "classification": "pass" if moment_max < 1e-12 and E_X < 1e-3 else "check",
            })

    path = os.path.join(outdir, "negative_control.csv")
    write_csv(path, rows)
    return rows


# ----------------------------
# Singular controls
# ----------------------------

def Q_single(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + x * x)


def Q_single_second(x: np.ndarray) -> np.ndarray:
    return 2.0 * (3.0 * x * x - 1.0) / ((1.0 + x * x) ** 3)


def Q_single_fourth(x: np.ndarray) -> np.ndarray:
    return 24.0 * (1.0 - 10.0 * x * x + 5.0 * x ** 4) / ((1.0 + x * x) ** 5)


def singular_gate2_mass_single(c: float, X0: float = 5.0, n_nodes: int = 2001) -> Tuple[float, float]:
    """
    Single packet q(gamma+c x)=c^-1 Q(x). dm = c dx.
    u=q''=c^-3 Q''
    q4=c^-5 Q^(4)
    Gamma_G = u - 6q + 2q^3
    Gamma_G2 = (1-q^2)u - q4/6
    Returns gate2 mass and scaled mass * c^15.
    """
    xs, ws = leggauss(n_nodes)
    x = X0 * xs
    q = (c ** -1) * Q_single(x)
    u = (c ** -3) * Q_single_second(x)
    q4 = (c ** -5) * Q_single_fourth(x)
    gamma_g = u - 6.0 * q + 2.0 * q ** 3
    gamma_g2 = (1.0 - q ** 2) * u - q4 / 6.0
    integrand = u ** 2 * (gamma_g ** 2 + gamma_g2 ** 2)
    # integral over m: dm = c dx = c * X0 * ds
    mass = c * X0 * float(np.sum(ws * integrand))
    return mass, mass * (c ** 15)


def run_singular_controls(outdir: str) -> List[Dict]:
    rows: List[Dict] = []
    for c in [1e-2, 1e-3, 1e-4]:
        mass, scaled = singular_gate2_mass_single(c)
        rows.append({
            "control": "singular_single_packet_dominance",
            "c": c,
            "gate2_mass": mass,
            "gate2_mass_times_c15": scaled,
            "expected_scaling": "mass ~ c^-15",
            "classification": "pass" if math.isfinite(mass) and scaled > 0 else "check",
        })
    path = os.path.join(outdir, "singular_control.csv")
    write_csv(path, rows)
    return rows


# ----------------------------
# Zeta zeros
# ----------------------------

def load_or_generate_zeros(outdir: str, n_zeros: int, dps: int = 50) -> List[float]:
    """
    Load zeros from CSV if present, otherwise generate via mpmath.zetazero.
    File path: outdir/zeros_N.csv
    """
    path = os.path.join(outdir, f"zeros_{n_zeros}.csv")
    if os.path.exists(path):
        vals = []
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                vals.append(float(row["gamma"]))
        return vals

    mp.mp.dps = dps
    rows = []
    vals = []
    log(f"generating {n_zeros} zeta zeros at dps={dps}")
    t0 = time.time()
    for n in range(1, n_zeros + 1):
        z = mp.zetazero(n)
        gamma = float(mp.im(z))
        vals.append(gamma)
        rows.append({"index": n, "gamma": gamma})
        if n % 25 == 0:
            elapsed = time.time() - t0
            rate = n / elapsed if elapsed > 0 else 0
            eta = (n_zeros - n) / rate if rate > 0 else 0
            log(f"  zero {n}/{n_zeros}: gamma={gamma:.4f}  elapsed={elapsed:.1f}s  rate={rate:.2f}/s  eta={eta:.1f}s")

    write_csv(path, rows)
    return vals


def K2_poisson_values(points: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    """
    Sum K2 over gammas at all points.
    K2 = 2 eps (3x^2 - eps^2)/(x^2 + eps^2)^3.
    """
    x = points[:, None] - gammas[None, :]
    den = x * x + eps * eps
    vals = 2.0 * eps * (3.0 * x * x - eps * eps) / (den ** 3)
    return np.sum(vals, axis=1)


def select_zeros(zeros: Sequence[float], m0: float, W: float) -> np.ndarray:
    return np.array([g for g in zeros if abs(g - m0) <= W], dtype=float)


def integrate_zero_proxy(zeros: Sequence[float],
                         m0: float,
                         Delta: float,
                         eps: float,
                         W: float,
                         n_nodes: int = 257) -> Tuple[float, float, int]:
    gammas = select_zeros(zeros, m0, W)
    if len(gammas) == 0:
        return float("nan"), float("nan"), 0

    xs, ws = leggauss(n_nodes)
    pts = m0 + Delta * xs
    vals = K2_poisson_values(pts, gammas, eps)
    integral = Delta * float(np.sum(ws * vals * vals))
    E_I = integral / (2.0 * Delta)
    S_I = float(np.max(np.abs(vals)))
    return E_I, S_I, int(len(gammas))


def finite_difference_jets_zero_proxy(zeros: Sequence[float],
                                      m0: float,
                                      Delta: float,
                                      eps: float,
                                      W: float,
                                      R: int,
                                      h_factor: float = 1e-3) -> Tuple[float, float]:
    gammas = select_zeros(zeros, m0, W)
    if len(gammas) == 0:
        return float("nan"), float("nan")

    h = h_factor * Delta
    radius = max(R + 8, 20)
    offsets = np.arange(-radius, radius + 1, dtype=float) * h
    pts = m0 + offsets
    vals = K2_poisson_values(pts, gammas, eps)

    deg = min(2 * radius, R + 12)
    coeffs = np.polynomial.polynomial.polyfit(offsets, vals, deg)
    jets = []
    for r in range(R + 1):
        deriv = math.factorial(r) * coeffs[r]
        jets.append((Delta ** r) * deriv)
    jets = np.array(jets, dtype=float)
    return float(np.max(np.abs(jets))), float(np.sqrt(np.mean(jets * jets)))


# ----------------------------
# Center generation
# ----------------------------

def make_centers(zeros: Sequence[float],
                 start_index: int,
                 end_index: int,
                 random_count: int = 100,
                 uniform_count: int = 0,
                 seed: int = 0) -> List[Tuple[str, float, Optional[int]]]:
    """
    Generate centers using the unified family vocabulary:
      zero_ordinate, gap_midpoint, large_gap_midpoint, small_gap_midpoint,
      random, uniform.

    start_index/end_index are 1-based zeta zero indices.
    """
    rng = random.Random(seed)
    z = list(zeros)
    s = max(1, start_index) - 1
    e = min(len(z) - 2, end_index - 1)

    centers: List[Tuple[str, float, Optional[int]]] = []

    for i in range(s, e):
        centers.append(("gap_midpoint", 0.5 * (z[i] + z[i + 1]), i + 1))

    for i in range(s, e + 1, 5):
        centers.append(("zero_ordinate", z[i], i + 1))

    gaps = [(z[i + 1] - z[i], i) for i in range(s, e)]
    gaps_sorted = sorted(gaps, key=lambda t: t[0])
    k = max(1, int(0.05 * len(gaps_sorted)))
    for label, subset in [("small_gap_midpoint", gaps_sorted[:k]),
                          ("large_gap_midpoint", gaps_sorted[-k:])]:
        for gap, i in subset:
            centers.append((label, z[i] + 0.5 * gap, i + 1))

    lo, hi = z[s], z[e]
    for _ in range(random_count):
        centers.append(("random", rng.uniform(lo, hi), None))

    if uniform_count > 0:
        for v in np.linspace(lo, hi, uniform_count):
            centers.append(("uniform", float(v), None))

    return centers


# ----------------------------
# Actual-zero proxy scan
# ----------------------------

def _zeros_content_hash(zeros: Sequence[float]) -> str:
    """Stable SHA-256 over the actual zero ordinates so different generations
    (or different n_zeros) produce different filenames."""
    payload = json.dumps([float(g) for g in zeros], separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def compute_params_hash(zeros: Sequence[float],
                        c_I_list: Sequence[float],
                        kappa_list: Sequence[float],
                        W_factor_list: Sequence[float],
                        R_jet_list: Sequence[int],
                        nquad_list: Sequence[int],
                        start_index: int,
                        end_index: int,
                        random_count: int,
                        uniform_count: int,
                        seed: int) -> str:
    """Full SHA-256 over every input that affects row math, matching the unified
    convention across the gate1 scripts. Includes a content hash of the actual
    zero ordinates."""
    record = {
        "zeros_sha256": _zeros_content_hash(zeros),
        "Q_mode": "log",
        "c_I_values": [float(x) for x in c_I_list],
        "kappa_values": [float(x) for x in kappa_list],
        "W_factor_values": [float(x) for x in W_factor_list],
        "R_jet_values": [int(x) for x in R_jet_list],
        "nquad_values": [int(x) for x in nquad_list],
        "start_index": int(start_index),
        "end_index": int(end_index),
        "random_count": int(random_count),
        "uniform_count": int(uniform_count),
        "seed": int(seed),
        "schema_version": 1,
    }
    blob = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def derive_output_path(stem: str, params_hash: str, hash_len: int = 12) -> str:
    """Insert a short params hash before the extension of stem (unified convention).

    foo.csv -> foo.<hash>.csv
    foo     -> foo.<hash>
    """
    short = params_hash[:hash_len]
    head, ext = os.path.splitext(stem)
    return f"{head}.{short}{ext}" if ext else f"{head}.{short}"


# Unified schema (matches agent1's ScanRow). Streaming writes / resume key both
# use these column names.
_PROXY_FIELDNAMES = [
    "center_type", "m0", "Q", "c_I", "kappa", "W_factor",
    "nquad", "R_jet", "local_zero_count",
    "E_I", "S_I", "B_eff", "J_max", "J_rms",
    "tail_drift_rel", "quad_drift_rel", "status",
]


def _rel_diff(a: float, b: float) -> float:
    denom = max(abs(a), abs(b), 1e-300)
    return abs(a - b) / denom


def _classify_row(B_eff: float, J_max: float,
                  tail_drift_rel: float, quad_drift_rel: float,
                  tail_tol: float = 2e-2, quad_tol: float = 1e-5) -> str:
    """Unified six-tier status. Matches agent1 thresholds."""
    if not math.isfinite(tail_drift_rel) or tail_drift_rel > tail_tol:
        return "reject_tail_unstable"
    if not math.isfinite(quad_drift_rel) or quad_drift_rel > quad_tol:
        return "reject_quad_unstable"
    if math.isfinite(B_eff) and math.isfinite(J_max) and B_eff > 20 and J_max < 1e-8:
        return "serious_proxy_warning"
    if math.isfinite(B_eff) and B_eff > 10:
        return "candidate_proxy_flat"
    if math.isfinite(B_eff) and B_eff > 5:
        return "watch"
    return "healthy"


def _row_key(row: Dict) -> tuple:
    """Unified resume key (matches agent1)."""
    return (
        row["center_type"],
        round(float(row["m0"]), 12),
        float(row["c_I"]),
        float(row["kappa"]),
        float(row["W_factor"]),
        int(row["nquad"]),
        int(row["R_jet"]),
    )


def _load_done_keys(path: str) -> set:
    """Build set of unified row keys already present in CSV."""
    if not os.path.exists(path):
        return set()
    done = set()
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    done.add(_row_key(row))
                except (KeyError, ValueError):
                    continue
    except Exception as e:
        log(f"warning: failed to read existing CSV for resume: {e}")
    return done


def _load_existing_rows(path: str) -> List[Dict]:
    """Re-read full CSV with type coercion so summaries can include resumed rows."""
    if not os.path.exists(path):
        return []
    out: List[Dict] = []
    int_fields = {"nquad", "R_jet", "local_zero_count"}
    float_fields = {"m0", "Q", "c_I", "kappa", "W_factor",
                    "E_I", "S_I", "B_eff", "J_max", "J_rms",
                    "tail_drift_rel", "quad_drift_rel"}
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            parsed: Dict = {}
            for k, v in row.items():
                if k in int_fields:
                    try:
                        parsed[k] = int(v) if v != "" else None
                    except ValueError:
                        parsed[k] = None
                elif k in float_fields:
                    try:
                        parsed[k] = float(v)
                    except ValueError:
                        parsed[k] = float("nan")
                else:
                    parsed[k] = v
            out.append(parsed)
    return out


# Worker globals (set by _init_worker in each subprocess to avoid re-pickling
# the zero list on every task).
_W_ZEROS: Optional[List[float]] = None


def _init_worker(zeros: List[float]) -> None:
    global _W_ZEROS
    _W_ZEROS = zeros


def _process_center(task: Tuple) -> List[Dict]:
    """Worker: process one center across the full param grid. Emits rows in
    the unified schema (matches agent1). Computes tail and quadrature drift
    by re-integrating at 2*W and at nquad/2, then classifies status."""
    (center_type, m0, ref_idx,
     c_I_list, kappa_list, W_factor_list, R_jet_list, nquad_list) = task

    zeros = _W_ZEROS
    if zeros is None:
        return []

    Q = math.log(m0 / (2.0 * math.pi))
    if Q <= 1.0:
        return []

    out: List[Dict] = []
    for c_I in c_I_list:
        Delta = c_I / Q
        for kappa in kappa_list:
            eps = kappa / Q
            for W_factor in W_factor_list:
                W = W_factor / Q
                W2 = 2.0 * W_factor / Q
                for R_jet in R_jet_list:
                    for nquad in nquad_list:
                        E_I, S_I, num_used = integrate_zero_proxy(
                            zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W, n_nodes=nquad
                        )
                        if not math.isfinite(E_I):
                            continue
                        E_half, _, _ = integrate_zero_proxy(
                            zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W,
                            n_nodes=max(32, nquad // 2),
                        )
                        quad_drift = _rel_diff(E_I, E_half) if math.isfinite(E_half) else float("nan")
                        E_2W, _, _ = integrate_zero_proxy(
                            zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W2, n_nodes=nquad
                        )
                        tail_drift = _rel_diff(E_I, E_2W) if math.isfinite(E_2W) else float("nan")

                        B_eff = -safe_log(E_I) / math.log(Q)
                        J_max, J_rms = finite_difference_jets_zero_proxy(
                            zeros=zeros, m0=m0, Delta=Delta, eps=eps, W=W, R=R_jet
                        )
                        status = _classify_row(B_eff, J_max, tail_drift, quad_drift)
                        out.append({
                            "center_type": center_type,
                            "m0": m0,
                            "Q": Q,
                            "c_I": c_I,
                            "kappa": kappa,
                            "W_factor": W_factor,
                            "nquad": nquad,
                            "R_jet": R_jet,
                            "local_zero_count": num_used,
                            "E_I": E_I,
                            "S_I": S_I,
                            "B_eff": B_eff,
                            "J_max": J_max,
                            "J_rms": J_rms,
                            "tail_drift_rel": tail_drift,
                            "quad_drift_rel": quad_drift,
                            "status": status,
                        })
    return out


def run_actual_zero_proxy_scan(outdir: str,
                               n_zeros: int,
                               start_index: int,
                               end_index: int,
                               smoke: bool = False,
                               workers: int = 1,
                               resume: bool = True,
                               random_count: int = 100,
                               uniform_count: int = 0,
                               seed: int = 0,
                               hash_len: int = 12) -> List[Dict]:
    log(f"loading or generating {n_zeros} zeros")
    zeros = load_or_generate_zeros(outdir, n_zeros=n_zeros)
    log(f"have {len(zeros)} zeros: gamma_1={zeros[0]:.4f}, gamma_N={zeros[-1]:.4f}")

    if smoke:
        centers = make_centers(zeros, start_index, min(start_index + 50, end_index),
                               random_count=10, uniform_count=uniform_count, seed=seed)
        c_I_list = [0.5]
        kappa_list = [1.0]
        W_factor_list = [50.0]
        R_jet_list = [4]
        nquad_list = [257]
        suffix = "smoke"
    else:
        centers = make_centers(zeros, start_index, end_index,
                               random_count=random_count, uniform_count=uniform_count, seed=seed)
        c_I_list = [0.2, 0.5]
        kappa_list = [0.5, 1.0]
        W_factor_list = [25.0, 50.0]
        R_jet_list = [4]
        nquad_list = [257]
        suffix = "small"

    n_params_per_center = (
        len(c_I_list) * len(kappa_list) * len(W_factor_list) * len(R_jet_list) * len(nquad_list)
    )
    log(
        f"scan plan: {len(centers)} centers x {n_params_per_center} params = "
        f"{len(centers) * n_params_per_center} total work units"
    )

    params_hash = compute_params_hash(
        zeros=zeros, c_I_list=c_I_list, kappa_list=kappa_list,
        W_factor_list=W_factor_list, R_jet_list=R_jet_list, nquad_list=nquad_list,
        start_index=start_index, end_index=end_index,
        random_count=random_count, uniform_count=uniform_count, seed=seed,
    )
    stem = os.path.join(outdir, f"actual_zero_proxy_{suffix}.csv")
    csv_path = derive_output_path(stem, params_hash, hash_len=hash_len)
    log(f"params hash: {params_hash[:hash_len]}  (full sha256: {params_hash})")
    log(f"output csv: {csv_path}")

    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    if not resume and file_exists:
        log(f"--no-resume: truncating existing file {csv_path}")
        os.remove(csv_path)
        file_exists = False

    done_keys = _load_done_keys(csv_path) if (resume and file_exists) else set()
    if done_keys:
        log(f"resume: {len(done_keys)} rows already present in {csv_path}")
    rows: List[Dict] = _load_existing_rows(csv_path) if done_keys else []

    tasks = []
    for (center_type, m0, ref_idx) in centers:
        Q_check = math.log(m0 / (2.0 * math.pi))
        if Q_check <= 1.0:
            continue
        all_done = all(
            (center_type, round(float(m0), 12), float(c_I), float(kappa),
             float(W_factor), int(nquad), int(R_jet)) in done_keys
            for c_I in c_I_list for kappa in kappa_list
            for W_factor in W_factor_list for R_jet in R_jet_list for nquad in nquad_list
        )
        if all_done:
            continue
        tasks.append((center_type, m0, ref_idx,
                      c_I_list, kappa_list, W_factor_list, R_jet_list, nquad_list))
    skipped = len(centers) - len(tasks)
    log(f"to compute: {len(tasks)} centers; skipped (resumed or Q<=1): {skipped}")

    t0 = time.time()
    progress_every = 5
    log(f"progress prints every {progress_every} centers, workers={workers}")

    if not tasks:
        log("nothing to compute; using existing CSV for summary")
    else:
        # Open CSV in append mode if it exists, else create with header.
        file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
        mode = "a" if file_exists else "w"
        fout = open(csv_path, mode, encoding="utf-8", newline="")
        writer = csv.DictWriter(fout, fieldnames=_PROXY_FIELDNAMES)
        if not file_exists:
            writer.writeheader()
            fout.flush()

        try:
            if workers <= 1:
                log("running serial (workers <= 1)")
                _init_worker(list(zeros))
                for idx, task in enumerate(tasks):
                    result = _process_center(task)
                    for row in result:
                        writer.writerow(row)
                    fout.flush()
                    rows.extend(result)
                    if (idx + 1) % progress_every == 0 or idx + 1 == len(tasks):
                        elapsed = time.time() - t0
                        rate = (idx + 1) / elapsed if elapsed > 0 else 0
                        eta = (len(tasks) - idx - 1) / rate if rate > 0 else 0
                        log(
                            f"  centers {idx+1}/{len(tasks)}  rows={len(rows)}  "
                            f"elapsed={elapsed:.1f}s  rate={rate:.2f}/s  eta={eta:.1f}s"
                        )
            else:
                log(f"running in process pool with {workers} workers")
                ctx = mp_proc.get_context("fork")
                with ctx.Pool(processes=workers, initializer=_init_worker,
                              initargs=(list(zeros),)) as pool:
                    for idx, result in enumerate(
                        pool.imap_unordered(_process_center, tasks, chunksize=4)
                    ):
                        for row in result:
                            writer.writerow(row)
                        fout.flush()
                        rows.extend(result)
                        if (idx + 1) % progress_every == 0 or idx + 1 == len(tasks):
                            elapsed = time.time() - t0
                            rate = (idx + 1) / elapsed if elapsed > 0 else 0
                            eta = (len(tasks) - idx - 1) / rate if rate > 0 else 0
                            log(
                                f"  centers {idx+1}/{len(tasks)}  rows={len(rows)}  "
                                f"elapsed={elapsed:.1f}s  rate={rate:.2f}/s  eta={eta:.1f}s"
                            )
        finally:
            fout.close()

    # Top diagnostics (over union of resumed + newly computed rows).
    top_stem = os.path.join(outdir, f"actual_zero_proxy_{suffix}_top_by_Beff.csv")
    top_path = derive_output_path(top_stem, params_hash, hash_len=hash_len)
    write_csv(top_path, summarize_top(rows, "B_eff", n=50, reverse=True))

    return rows


# ----------------------------
# Main
# ----------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["controls", "actual", "all"], default="controls")
    ap.add_argument("--outdir", default=_DEFAULT_OUT_DIR,
                    help="Output directory. Default: <script>/out/.")
    ap.add_argument("--zeros", type=int, default=500)
    ap.add_argument("--start-index", type=int, default=50)
    ap.add_argument("--end-index", type=int, default=500)
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2),
                    help="number of worker processes for the actual-zero scan; 1 = serial")
    ap.add_argument("--resume", dest="resume", action="store_true", default=True,
                    help="If the params-hash-derived CSV already exists, append to it and skip "
                         "rows whose key is already present. Resume is on by default.")
    ap.add_argument("--no-resume", dest="resume", action="store_false",
                    help="Truncate the output CSV if it already exists.")
    ap.add_argument("--hash-len", type=int, default=12,
                    help="Length of the params-hash slug embedded in the output filename.")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--random-count", type=int, default=100,
                    help="Number of random centers per scan.")
    ap.add_argument("--uniform-count", type=int, default=0,
                    help="Number of evenly-spaced uniform centers per scan (0 disables).")
    args = ap.parse_args()

    ensure_dir(args.outdir)

    log(f"starting gate1_pilot mode={args.mode} outdir={args.outdir}")

    if args.mode in ("controls", "all"):
        log("running deterministic same-scale quadrature negative control")
        neg_rows = run_negative_control(args.outdir)
        log(f"wrote {len(neg_rows)} rows to negative_control.csv")
        for r in neg_rows[:3]:
            print(r, flush=True)

        log("running singular dominance control")
        sing_rows = run_singular_controls(args.outdir)
        log(f"wrote {len(sing_rows)} rows to singular_control.csv")
        for r in sing_rows:
            print(r, flush=True)

    if args.mode in ("actual", "all"):
        log("running actual-zero zero-kernel-only proxy scan")
        rows = run_actual_zero_proxy_scan(
            outdir=args.outdir,
            n_zeros=args.zeros,
            start_index=args.start_index,
            end_index=args.end_index,
            smoke=args.smoke,
            workers=args.workers,
            resume=args.resume,
            random_count=args.random_count,
            uniform_count=args.uniform_count,
            seed=args.seed,
            hash_len=args.hash_len,
        )
        log(f"wrote {len(rows)} rows to actual_zero_proxy CSV")
        top = summarize_top(rows, "B_eff", n=10, reverse=True)
        log("top rows by B_eff:")
        for r in top:
            print({
                "status": r.get("status"),
                "center_type": r.get("center_type"),
                "m0": r.get("m0"),
                "Q": r.get("Q"),
                "c_I": r.get("c_I"),
                "kappa": r.get("kappa"),
                "W_factor": r.get("W_factor"),
                "R_jet": r.get("R_jet"),
                "nquad": r.get("nquad"),
                "E_I": r.get("E_I"),
                "B_eff": r.get("B_eff"),
                "J_max": r.get("J_max"),
                "tail_drift_rel": r.get("tail_drift_rel"),
                "quad_drift_rel": r.get("quad_drift_rel"),
                "local_zero_count": r.get("local_zero_count"),
            }, flush=True)


if __name__ == "__main__":
    main()
