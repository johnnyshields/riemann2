#!/usr/bin/env python3
"""
Gate 1 actual-zero pilot scan, zero-kernel-only proxy.

This script tests the Gate 1 source-curvature diagnostic on actual zero ordinates
using a deliberately simplified proxy kernel:

    K(m; gamma, eps) = eps / ((m-gamma)^2 + eps^2)

    K2(m; gamma, eps) = d^2/dm^2 K
        = 2 eps (3(m-gamma)^2 - eps^2) / ((m-gamma)^2 + eps^2)^3

Proxy object:

    qpp_zero_eps(m) = sum_{gamma in cutoff window} K2(m; gamma, eps)

This is NOT the final canonical q''_can. It omits B2, completed-phase constants,
tail regularization, and quartet/completed-zero normalization. Use it as a
geometry/pipeline pilot only.

Run:
    python gate1_zero_pilot.py --zeros zeros.txt --out zero_pilot_results.csv
    python gate1_zero_pilot.py --zeros zeros.csv --fast --out zero_pilot_fast.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import os

# Pin BLAS / OpenMP to 1 thread per process. We parallelize at the center
# level via multiprocessing; with 30 workers each trying to spawn 32 OpenMP
# threads, the first batch was thrashing for ~12 minutes before the OS
# balanced affinity. Set these before numpy is imported.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import hashlib
import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss


def log(msg: str) -> None:
    """Timestamped, flushed line. Unified logging helper across the gate1 scripts."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))


def _default_out(*parts: str) -> str:
    """Resolve <script_dir>/out/<parts...>; unified outputs location."""
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


# Worker-side global, set by _worker_init.
_WORKER_ZEROS: np.ndarray | None = None


def _worker_init(zeros: np.ndarray) -> None:
    global _WORKER_ZEROS
    _WORKER_ZEROS = zeros


# ----------------------------
# Input
# ----------------------------

def load_zeros(path: str) -> np.ndarray:
    """
    Load zero ordinates from:
      - plain text, one float per line
      - CSV with column gamma/zero/zeros/ordinate/t
      - CSV-like first column fallback

    Lines beginning with # are ignored.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    # Try CSV/header mode.
    with open(path, "r", newline="") as f:
        sample = f.read(4096)
        f.seek(0)

        # If header-ish, use csv.DictReader.
        first_nonempty = None
        for line in sample.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                first_nonempty = line
                break

        if first_nonempty and any(name in first_nonempty.lower().split(",") for name in ["gamma", "zero", "zeros", "ordinate", "t"]):
            reader = csv.DictReader(f)
            candidates = ["gamma", "zero", "zeros", "ordinate", "t"]
            col = None
            lower_map = {c.lower(): c for c in (reader.fieldnames or [])}
            for cand in candidates:
                if cand in lower_map:
                    col = lower_map[cand]
                    break
            if col is None:
                raise ValueError(f"Could not find zero ordinate column in {reader.fieldnames}")
            vals = []
            for row in reader:
                raw = (row.get(col) or "").strip()
                if raw:
                    vals.append(float(raw))
            arr = np.array(vals, dtype=np.float64)
            arr.sort()
            return arr

    # Plain/fallback mode.
    vals = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # accept comma-separated; take first parseable field
            parts = [p.strip() for p in line.replace("\t", ",").split(",")]
            for p in parts:
                if not p:
                    continue
                try:
                    vals.append(float(p))
                    break
                except ValueError:
                    continue

    arr = np.array(vals, dtype=np.float64)
    arr = arr[np.isfinite(arr)]
    arr.sort()
    if len(arr) == 0:
        raise ValueError("No zero ordinates loaded.")
    return arr


# ----------------------------
# Proxy kernel and derivatives
# ----------------------------

def K2_eps(m: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    """
    Return matrix K2(m_i; gamma_j, eps), shape (len(m), len(gammas)).

    K2 = 2 eps (3 x^2 - eps^2) / (x^2 + eps^2)^3
    """
    x = m[:, None] - gammas[None, :]
    den = x * x + eps * eps
    return 2.0 * eps * (3.0 * x * x - eps * eps) / (den ** 3)


def K2_deriv_at_center(gammas: np.ndarray, m0: float, eps: float, r: int) -> float:
    """
    Numerically stable-ish finite-difference-free derivatives for small r by
    polynomial recurrence would be ideal. For pilot, use complex-step-like
    polynomial fitting instead elsewhere. This placeholder is not used directly.
    """
    raise NotImplementedError


def qpp_proxy_values(ms: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    if len(gammas) == 0:
        return np.zeros_like(ms)
    return np.sum(K2_eps(ms, gammas, eps), axis=1)


# ----------------------------
# Interval computations
# ----------------------------

def Q_of_m(m0: float, mode: str = "log") -> float:
    """Q is the asymptotic mean Gram-point spacing scale: Q = log(m0 / (2*pi)).

    Valid only for positive m0 (zero ordinates of zeta on the critical line are
    positive). For m0 <= 0 returns -inf so callers can filter via --min-Q (or
    short-circuit) without hitting a math domain error. Returns log(m0/(2*pi))
    without clamping for valid inputs; values <= 0 are valid sentinels meaning
    "skip this center".
    """
    if mode == "log":
        if m0 <= 0:
            return float("-inf")
        return math.log(m0 / (2.0 * math.pi))
    raise ValueError(f"Unknown Q mode: {mode}")


def select_zeros_in_window(zeros: np.ndarray, center: float, W: float) -> np.ndarray:
    lo = np.searchsorted(zeros, center - W, side="left")
    hi = np.searchsorted(zeros, center + W, side="right")
    return zeros[lo:hi]


def compute_interval_energy(
    zeros: np.ndarray,
    m0: float,
    c_I: float,
    kappa: float,
    W_factor: float,
    Q_mode: str,
    nquad: int,
) -> tuple[float, float, float, int]:
    """
    Compute:
      Q = log-ish scale
      eps = kappa/Q
      I = [m0-c_I/Q, m0+c_I/Q]
      W = W_factor/Q
      qpp = sum_{|gamma-m0|<=W} K2
      E_I = mean |qpp|^2 over I
      S_I = max over quadrature nodes
    """
    Q = Q_of_m(m0, Q_mode)
    eps = kappa / Q
    half = c_I / Q
    W = W_factor / Q

    local_zeros = select_zeros_in_window(zeros, m0, W)

    nodes, weights = leggauss(nquad)
    ms = m0 + half * nodes
    ws = half * weights

    vals = qpp_proxy_values(ms, local_zeros, eps)
    integral = float(np.sum(ws * vals * vals))
    E_I = integral / (2.0 * half)
    S_I = float(np.max(np.abs(vals))) if len(vals) else 0.0
    return E_I, S_I, Q, len(local_zeros)


def chebyshev_jet_proxy(
    zeros: np.ndarray,
    m0: float,
    c_I: float,
    kappa: float,
    W_factor: float,
    Q_mode: str,
    R: int,
    nfit: int,
) -> tuple[float, float]:
    """
    Compute normalized finite jets J_r = Delta^r f^(r)(m0), r=0..R,
    via Chebyshev/polynomial fit over [-Delta, Delta].

    We fit f(m0 + Delta*x) as polynomial in x:
        f ~ sum a_r x^r
    Then Delta^r f^(r)(m0) = r! a_r.

    Returns:
      J_max, J_rms
    """
    Q = Q_of_m(m0, Q_mode)
    eps = kappa / Q
    Delta = c_I / Q
    W = W_factor / Q

    local_zeros = select_zeros_in_window(zeros, m0, W)

    # Chebyshev-ish nodes in x.
    j = np.arange(nfit)
    x = np.cos((2 * j + 1) * math.pi / (2 * nfit))
    ms = m0 + Delta * x
    vals = qpp_proxy_values(ms, local_zeros, eps)

    # Fit ordinary polynomial in x up to degree R.
    # Use overdetermined least squares.
    V = np.vander(x, N=R + 1, increasing=True)
    coeffs, *_ = np.linalg.lstsq(V, vals, rcond=None)

    jets = np.array([math.factorial(r) * coeffs[r] for r in range(R + 1)], dtype=np.float64)
    J_max = float(np.max(np.abs(jets)))
    J_rms = float(np.sqrt(np.sum(jets * jets)))
    return J_max, J_rms


# ----------------------------
# Center families
# ----------------------------

def gram_placeholder_centers(zeros: np.ndarray, max_count: int) -> np.ndarray:
    """Placeholder for Gram points: evenly spaced between min/max zero ordinate.
    Real Gram points require theta(t); this script does not compute them."""
    if len(zeros) < 2:
        return zeros.copy()
    lo, hi = float(zeros[0]), float(zeros[-1])
    return np.linspace(lo, hi, min(max_count, max(2, len(zeros) // 2)))


def generate_centers(
    zeros: np.ndarray,
    max_per_family: int,
    seed: int,
) -> list[tuple[str, float]]:
    """Build centers for a scan. Family names follow the unified vocabulary:
    zero_ordinate, gap_midpoint, large_gap_midpoint, small_gap_midpoint,
    gram_placeholder, random, uniform."""
    rng = np.random.default_rng(seed)
    centers: list[tuple[str, float]] = []

    for g in zeros[:max_per_family]:
        centers.append(("zero_ordinate", float(g)))

    gaps = np.diff(zeros)
    if len(gaps) > 0:
        idx_sorted_small = np.argsort(gaps)[:max_per_family]
        idx_sorted_large = np.argsort(gaps)[-max_per_family:]
        for i in idx_sorted_small:
            a, b = zeros[i], zeros[i + 1]
            centers.append(("small_gap_midpoint", float(0.5 * (a + b))))
        for i in idx_sorted_large:
            a, b = zeros[i], zeros[i + 1]
            centers.append(("large_gap_midpoint", float(0.5 * (a + b))))

    for i in range(min(max_per_family, max(0, len(zeros) - 1))):
        centers.append(("gap_midpoint", float(0.5 * (zeros[i] + zeros[i + 1]))))

    for g in gram_placeholder_centers(zeros, max_per_family):
        centers.append(("gram_placeholder", float(g)))

    if len(zeros) >= 2:
        lo, hi = float(zeros[0]), float(zeros[-1])
        for m in rng.uniform(lo, hi, size=max_per_family):
            centers.append(("random", float(m)))
        for m in np.linspace(lo, hi, max_per_family):
            centers.append(("uniform", float(m)))

    seen = set()
    deduped = []
    for typ, m in centers:
        key = (typ, round(m, 12))
        if key not in seen:
            seen.add(key)
            deduped.append((typ, m))
    return deduped


# ----------------------------
# Result row
# ----------------------------

@dataclass
class ScanRow:
    center_type: str
    m0: float
    Q: float
    c_I: float
    kappa: float
    W_factor: float
    nquad: int
    R_jet: int
    local_zero_count: int
    E_I: float
    S_I: float
    B_eff: float
    J_max: float
    J_rms: float
    tail_drift_rel: float
    quad_drift_rel: float
    status: str


def safe_B_eff(E_I: float, Q: float) -> float:
    if E_I <= 0 or Q <= 1:
        return float("nan")
    return -math.log(E_I) / math.log(Q)


def rel_diff(a: float, b: float) -> float:
    denom = max(abs(a), abs(b), 1e-300)
    return abs(a - b) / denom


def classify_row(row: ScanRow, tail_tol: float, quad_tol: float) -> str:
    if row.tail_drift_rel > tail_tol:
        return "reject_tail_unstable"
    if row.quad_drift_rel > quad_tol:
        return "reject_quad_unstable"
    # Proxy thresholds only.
    if row.B_eff > 20 and row.J_max < 1e-8:
        return "serious_proxy_warning"
    if row.B_eff > 10:
        return "candidate_proxy_flat"
    if row.B_eff > 5:
        return "watch"
    return "healthy"


def _scan_one(task: tuple) -> ScanRow:
    """Compute one ScanRow. Reads zeros from the worker-global set by _worker_init."""
    (center_type, m0, c_I, kappa, W_factor, Q_mode,
     nquad, R_jet, nfit, tail_tol, quad_tol) = task
    zeros = _WORKER_ZEROS
    if zeros is None:
        raise RuntimeError("Worker not initialized with zeros.")

    E, S, Q, count = compute_interval_energy(
        zeros, m0, c_I, kappa, W_factor, Q_mode, nquad
    )
    E_half, _, _, _ = compute_interval_energy(
        zeros, m0, c_I, kappa, W_factor, Q_mode, max(32, nquad // 2)
    )
    quad_drift = rel_diff(E, E_half)
    E_2W, _, _, _ = compute_interval_energy(
        zeros, m0, c_I, kappa, 2.0 * W_factor, Q_mode, nquad
    )
    tail_drift = rel_diff(E, E_2W)

    try:
        J_max, J_rms = chebyshev_jet_proxy(
            zeros, m0, c_I, kappa, W_factor, Q_mode, R_jet, nfit
        )
    except Exception:
        J_max, J_rms = float("nan"), float("nan")

    B_eff = safe_B_eff(E, Q)
    row = ScanRow(
        center_type=center_type,
        m0=m0,
        Q=Q,
        c_I=c_I,
        kappa=kappa,
        W_factor=W_factor,
        nquad=nquad,
        R_jet=R_jet,
        local_zero_count=count,
        E_I=E,
        S_I=S,
        B_eff=B_eff,
        J_max=J_max,
        J_rms=J_rms,
        tail_drift_rel=tail_drift,
        quad_drift_rel=quad_drift,
        status="",
    )
    row.status = classify_row(row, tail_tol, quad_tol)
    return row


_ROW_KEY_FIELDS = ("center_type", "m0", "c_I", "kappa", "W_factor", "nquad", "R_jet")


def _row_key(center_type: str, m0: float, c_I: float, kappa: float,
             W_factor: float, nquad: int, R_jet: int) -> tuple:
    return (center_type, round(float(m0), 12), float(c_I), float(kappa),
            float(W_factor), int(nquad), int(R_jet))


def _row_key_from_dict(d: dict) -> tuple:
    return _row_key(
        d["center_type"], float(d["m0"]), float(d["c_I"]), float(d["kappa"]),
        float(d["W_factor"]), int(d["nquad"]), int(d["R_jet"]),
    )


def run_scan(
    zeros: np.ndarray,
    centers: list[tuple[str, float]],
    c_I_values: list[float],
    kappa_values: list[float],
    W_factor_values: list[float],
    Q_mode: str,
    nquad: int,
    R_jet: int,
    nfit: int,
    tail_tol: float,
    quad_tol: float,
    workers: int = 1,
    progress_every: int = 0,
    out_path: str | None = None,
    resume_keys: set[tuple] | None = None,
) -> list[ScanRow]:
    """
    Build the task list, optionally skipping any task whose row-key is already
    in resume_keys, and execute. If out_path is given, each row is appended
    to the CSV (with header on first write) and flushed as soon as it is
    computed, so a kill leaves a valid partial CSV.
    """
    tasks: list[tuple] = []
    skipped = 0
    for center_type, m0 in centers:
        for c_I in c_I_values:
            for kappa in kappa_values:
                for W_factor in W_factor_values:
                    if resume_keys is not None:
                        key = _row_key(center_type, m0, c_I, kappa, W_factor, nquad, R_jet)
                        if key in resume_keys:
                            skipped += 1
                            continue
                    tasks.append((
                        center_type, m0, c_I, kappa, W_factor, Q_mode,
                        nquad, R_jet, nfit, tail_tol, quad_tol,
                    ))

    if resume_keys is not None:
        log(f"Resume: skipping {skipped} already-computed tasks; "
            f"{len(tasks)} new tasks to run.")

    total = len(tasks)
    rows: list[ScanRow] = []

    csv_writer = None
    csv_file = None
    if out_path is not None:
        out_parent = os.path.dirname(os.path.abspath(out_path))
        if out_parent:
            os.makedirs(out_parent, exist_ok=True)
        file_exists = os.path.exists(out_path) and os.path.getsize(out_path) > 0
        csv_file = open(out_path, "a", newline="")
        fieldnames = list(asdict(ScanRow(
            center_type="", m0=0.0, Q=0.0, c_I=0.0, kappa=0.0, W_factor=0.0,
            nquad=0, R_jet=0, local_zero_count=0, E_I=0.0, S_I=0.0, B_eff=0.0,
            J_max=0.0, J_rms=0.0, tail_drift_rel=0.0, quad_drift_rel=0.0,
            status="",
        )).keys())
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            csv_writer.writeheader()
            csv_file.flush()

    def _emit(row: ScanRow) -> None:
        rows.append(row)
        if csv_writer is not None:
            csv_writer.writerow(asdict(row))
            csv_file.flush()

    try:
        if workers <= 1:
            _worker_init(zeros)
            for i, t in enumerate(tasks, 1):
                _emit(_scan_one(t))
                if progress_every and i % progress_every == 0:
                    print(f"  scan: {i}/{total}", flush=True)
        else:
            with ProcessPoolExecutor(
                max_workers=workers,
                initializer=_worker_init,
                initargs=(zeros,),
            ) as pool:
                futures = [pool.submit(_scan_one, t) for t in tasks]
                done = 0
                for fut in as_completed(futures):
                    _emit(fut.result())
                    done += 1
                    if progress_every and done % progress_every == 0:
                        print(f"  scan: {done}/{total}", flush=True)
    finally:
        if csv_file is not None:
            csv_file.close()

    return rows


def _hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_params_hash(
    zeros_path: str,
    Q_mode: str,
    c_I_values: list[float],
    kappa_values: list[float],
    W_factor_values: list[float],
    nquad: int,
    R_jet: int,
    nfit: int,
    tail_tol: float,
    quad_tol: float,
    max_per_family: int,
    seed: int,
    min_m0: float | None,
    min_Q: float | None,
) -> str:
    """SHA-256 over every input that affects row math, including the zeros file content."""
    record = {
        "zeros_sha256": _hash_file(zeros_path),
        "Q_mode": Q_mode,
        "c_I_values": [float(x) for x in c_I_values],
        "kappa_values": [float(x) for x in kappa_values],
        "W_factor_values": [float(x) for x in W_factor_values],
        "nquad": int(nquad),
        "R_jet": int(R_jet),
        "nfit": int(nfit),
        "tail_tol": float(tail_tol),
        "quad_tol": float(quad_tol),
        "max_per_family": int(max_per_family),
        "seed": int(seed),
        "min_m0": None if min_m0 is None else float(min_m0),
        "min_Q": None if min_Q is None else float(min_Q),
        "schema_version": 1,
    }
    blob = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def derive_output_path(stem: str, params_hash: str, hash_len: int = 12) -> str:
    """Insert a short params hash before the extension of `stem`.

    foo.csv -> foo.<hash>.csv
    foo     -> foo.<hash>
    /a/b/foo.csv -> /a/b/foo.<hash>.csv
    """
    short = params_hash[:hash_len]
    head, ext = os.path.splitext(stem)
    return f"{head}.{short}{ext}" if ext else f"{head}.{short}"


def load_existing_keys(csv_path: str) -> set[tuple]:
    keys: set[tuple] = set()
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        return keys
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                keys.add(_row_key_from_dict(row))
            except (KeyError, ValueError):
                continue
    return keys


def _load_rows_for_summary(csv_path: str) -> list[ScanRow]:
    """Reload the full CSV (prior + freshly streamed rows) so the end-of-run
    summary covers everything when --resume was used."""
    rows: list[ScanRow] = []
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        return rows
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for d in reader:
            try:
                rows.append(ScanRow(
                    center_type=d["center_type"],
                    m0=float(d["m0"]),
                    Q=float(d["Q"]),
                    c_I=float(d["c_I"]),
                    kappa=float(d["kappa"]),
                    W_factor=float(d["W_factor"]),
                    nquad=int(d["nquad"]),
                    R_jet=int(d["R_jet"]),
                    local_zero_count=int(d["local_zero_count"]),
                    E_I=float(d["E_I"]),
                    S_I=float(d["S_I"]),
                    B_eff=float(d["B_eff"]),
                    J_max=float(d["J_max"]),
                    J_rms=float(d["J_rms"]),
                    tail_drift_rel=float(d["tail_drift_rel"]),
                    quad_drift_rel=float(d["quad_drift_rel"]),
                    status=d.get("status", ""),
                ))
            except (KeyError, ValueError):
                continue
    return rows


def write_rows(path: str, rows: list[ScanRow]) -> None:
    fields = list(asdict(rows[0]).keys()) if rows else []
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


_NUMERIC_SUMMARY_FIELDS = (
    "E_I", "S_I", "B_eff", "J_max", "J_rms",
    "tail_drift_rel", "quad_drift_rel", "local_zero_count",
)

_THRESHOLD_CHECKS = (
    ("B_eff > 5",            lambda r: math.isfinite(r.B_eff) and r.B_eff > 5),
    ("B_eff > 10",           lambda r: math.isfinite(r.B_eff) and r.B_eff > 10),
    ("B_eff > 20",           lambda r: math.isfinite(r.B_eff) and r.B_eff > 20),
    ("tail_drift_rel > 0.02", lambda r: math.isfinite(r.tail_drift_rel) and r.tail_drift_rel > 0.02),
    ("quad_drift_rel > 1e-5", lambda r: math.isfinite(r.quad_drift_rel) and r.quad_drift_rel > 1e-5),
)


def print_summary(rows: list[ScanRow], top_n: int) -> None:
    print("\n=== Gate 1 actual-zero pilot summary: zero-kernel-only proxy ===")
    print(f"rows: {len(rows)}")

    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r.status] = by_status.get(r.status, 0) + 1
    print("status counts:")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")

    print("\npercentiles:")
    for col in _NUMERIC_SUMMARY_FIELDS:
        xs = [getattr(r, col) for r in rows]
        xs = [float(x) for x in xs if x is not None and math.isfinite(float(x))]
        if not xs:
            continue
        xs.sort()
        def _pct(p: float) -> float:
            return xs[int(p * (len(xs) - 1))]
        print(
            f"  {col}: "
            f"min={xs[0]:.6e}, "
            f"p25={_pct(0.25):.6e}, "
            f"median={_pct(0.50):.6e}, "
            f"p75={_pct(0.75):.6e}, "
            f"max={xs[-1]:.6e}"
        )

    print("\nthreshold counts:")
    for label, predicate in _THRESHOLD_CHECKS:
        n_match = sum(1 for r in rows if predicate(r))
        print(f"  {label}: {n_match}")

    # Top-N by B_eff (desc), tie-broken by ascending tail/quad drift.
    rows_sorted = sorted(
        rows,
        key=lambda r: (
            -float(np.nan_to_num(r.B_eff, nan=-1e999)),
            r.tail_drift_rel,
            r.quad_drift_rel,
        ),
    )

    print(f"\nTop {top_n} by B_eff:")
    header = [
        "rank", "status", "center_type", "m0", "Q", "c_I", "kappa", "W_factor",
        "count", "E_I", "S_I", "B_eff", "J_max", "tail_drift", "quad_drift",
    ]
    print(",".join(header))
    for i, r in enumerate(rows_sorted[:top_n], start=1):
        print(",".join([
            str(i),
            r.status,
            r.center_type,
            f"{r.m0:.12g}",
            f"{r.Q:.6g}",
            f"{r.c_I:.3g}",
            f"{r.kappa:.3g}",
            f"{r.W_factor:.3g}",
            str(r.local_zero_count),
            f"{r.E_I:.6e}",
            f"{r.S_I:.6e}",
            f"{r.B_eff:.6g}",
            f"{r.J_max:.6e}",
            f"{r.tail_drift_rel:.3e}",
            f"{r.quad_drift_rel:.3e}",
        ]))


def _parse_floats(s: str) -> list[float]:
    return [float(p.strip()) for p in s.split(",") if p.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeros", required=True, help="Path to zero ordinates file.")
    parser.add_argument("--out", default=_default_out("zero_pilot_results.csv"),
                        help="Output CSV path. Default lands in <script>/out/.")
    parser.add_argument("--fast", action="store_true", help="Small fast pilot.")
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--min-m0", type=float, default=None,
                        help="Discard zero ordinates and centers below this height.")
    parser.add_argument("--min-Q", type=float, default=1.0,
                        help="Discard centers whose Q = log(m0/(2*pi)) is below this. "
                             "Default 1.0 (m0 > 2*pi*e ~= 17.08) so B_eff = -log(E)/log(Q) is well-defined.")
    parser.add_argument("--W-factors", type=str, default=None,
                        help="Comma-separated W_factor values (override default).")
    parser.add_argument("--c-I-values", type=str, default=None,
                        help="Comma-separated c_I values (override default).")
    parser.add_argument("--kappa-values", type=str, default=None,
                        help="Comma-separated kappa values (override default).")
    parser.add_argument("--nquad", type=int, default=None)
    parser.add_argument("--R-jet", type=int, default=None)
    parser.add_argument("--nfit", type=int, default=None)
    parser.add_argument("--tail-tol", type=float, default=None)
    parser.add_argument("--quad-tol", type=float, default=None)
    parser.add_argument("--max-per-family", type=int, default=None)
    parser.add_argument("--workers", type=int,
                        default=max(1, (os.cpu_count() or 2) - 2),
                        help="Process-pool workers (default: cpu_count - 2).")
    parser.add_argument("--progress-every", type=int, default=0,
                        help="Print progress every N completed tasks (0 = silent).")
    parser.add_argument("--resume", dest="resume", action="store_true", default=True,
                        help="If the params-hash-derived output file already exists, append to it "
                             "and skip rows whose key is already present. Resume is on by default.")
    parser.add_argument("--no-resume", dest="resume", action="store_false",
                        help="Truncate the output file if it already exists. Off by default.")
    parser.add_argument("--hash-len", type=int, default=12,
                        help="Length of the params-hash slug embedded in the output filename.")
    args = parser.parse_args()

    zeros = load_zeros(args.zeros)
    log(f"Loaded {len(zeros)} zeros: [{zeros[0]}, {zeros[-1]}]")

    if args.min_m0 is not None:
        before = len(zeros)
        zeros = zeros[zeros >= args.min_m0]
        log(f"Filtered to {len(zeros)} zeros with m0 >= {args.min_m0} (was {before})")
        if len(zeros) < 2:
            raise SystemExit("Too few zeros after --min-m0 filter.")

    if args.fast:
        max_per_family = 8
        c_I_values = [0.2, 0.5]
        kappa_values = [0.5, 1.0]
        W_factor_values = [10.0, 25.0]
        nquad = 96
        R_jet = 6
        nfit = 24
        tail_tol = 5e-2
        quad_tol = 1e-4
    else:
        max_per_family = 25
        c_I_values = [0.1, 0.2, 0.5, 1.0]
        kappa_values = [0.25, 0.5, 1.0]
        W_factor_values = [10.0, 25.0, 50.0, 100.0]
        nquad = 160
        R_jet = 8
        nfit = 36
        tail_tol = 2e-2
        quad_tol = 1e-5

    if args.max_per_family is not None:
        max_per_family = args.max_per_family
    if args.c_I_values is not None:
        c_I_values = _parse_floats(args.c_I_values)
    if args.kappa_values is not None:
        kappa_values = _parse_floats(args.kappa_values)
    if args.W_factors is not None:
        W_factor_values = _parse_floats(args.W_factors)
    if args.nquad is not None:
        nquad = args.nquad
    if args.R_jet is not None:
        R_jet = args.R_jet
    if args.nfit is not None:
        nfit = args.nfit
    if args.tail_tol is not None:
        tail_tol = args.tail_tol
    if args.quad_tol is not None:
        quad_tol = args.quad_tol

    centers = generate_centers(zeros, max_per_family=max_per_family, seed=args.seed)
    log(f"Generated {len(centers)} centers.")

    if args.min_m0 is not None:
        before = len(centers)
        centers = [(t, m) for (t, m) in centers if m >= args.min_m0]
        log(f"Centers after --min-m0: {len(centers)} (was {before})")

    if args.min_Q is not None:
        before = len(centers)
        centers = [(t, m) for (t, m) in centers if Q_of_m(m, "log") >= args.min_Q]
        log(f"Centers after --min-Q: {len(centers)} (was {before})")

    if not centers:
        raise SystemExit("No centers remain after filters.")

    workers = max(1, args.workers)
    log(f"Workers: {workers}")

    params_hash = compute_params_hash(
        zeros_path=args.zeros,
        Q_mode="log",
        c_I_values=c_I_values,
        kappa_values=kappa_values,
        W_factor_values=W_factor_values,
        nquad=nquad,
        R_jet=R_jet,
        nfit=nfit,
        tail_tol=tail_tol,
        quad_tol=quad_tol,
        max_per_family=max_per_family,
        seed=args.seed,
        min_m0=args.min_m0,
        min_Q=args.min_Q,
    )
    out_path = derive_output_path(args.out, params_hash, hash_len=args.hash_len)
    log(f"Params hash: {params_hash[:args.hash_len]}  (full sha256: {params_hash})")
    log(f"Output CSV : {out_path}")

    resume_keys: set[tuple] | None = None
    file_exists = os.path.exists(out_path) and os.path.getsize(out_path) > 0
    if args.resume:
        if file_exists:
            resume_keys = load_existing_keys(out_path)
            log(f"Resume: loaded {len(resume_keys)} existing keys from {out_path}.")
        else:
            log("Resume: no prior file at this hash; starting fresh.")
    else:
        if file_exists:
            log(f"--no-resume: truncating existing file {out_path}.")
            os.remove(out_path)

    rows = run_scan(
        zeros=zeros,
        centers=centers,
        c_I_values=c_I_values,
        kappa_values=kappa_values,
        W_factor_values=W_factor_values,
        Q_mode="log",
        nquad=nquad,
        R_jet=R_jet,
        nfit=nfit,
        tail_tol=tail_tol,
        quad_tol=quad_tol,
        workers=workers,
        progress_every=args.progress_every,
        out_path=out_path,
        resume_keys=resume_keys,
    )

    if args.resume and resume_keys:
        all_rows = _load_rows_for_summary(out_path)
        print_summary(all_rows, top_n=args.top)
    else:
        print_summary(rows, top_n=args.top)
    log(f"Wrote CSV: {out_path}")
    log("NOTE: This is a zero-kernel-only proxy. It omits B2 and final canonical regularization.")


if __name__ == "__main__":
    main()
