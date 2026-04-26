#!/usr/bin/env python3
"""
Gate 1 actual-zero proxy zone scan.

Purpose:
  Scan actual Hardy-Z sign-change zero proxies around surrogate-flat candidate
  zones, using the zero-kernel-only proxy:

      K2(m; gamma, eps)
        = 2 eps (3(m-gamma)^2 - eps^2) / ((m-gamma)^2 + eps^2)^3

  This is NOT the final canonical q''_can calculation. It is a pilot
  actual-zero-side proxy meant to test whether surrogate-flat zones correspond
  to actual-zero source-flat behavior.

Inputs:
  - gate1_surrogate_best_candidates.csv, or explicit --zones

Outputs:
  - gate1_actual_zero_proxy_zone_scan.csv
  - gate1_actual_zero_proxy_zone_summary.csv
  - cached zero proxy files under ./zero_proxy_cache/

Parallelism:
  --workers controls process-pool size for mpmath-heavy work
  (Hardy-Z grid eval, sign-change bisection, Gram-point bisection).
  When len(zones) >= 2, zones are dispatched in parallel and each
  zone runs its mpmath work serially. When len(zones) == 1, the
  single zone uses within-zone parallelism for its Hardy-Z scan,
  bisection brackets, and Gram-point search.

Dependencies:
  pip install numpy pandas mpmath
"""

import argparse
import hashlib
import io
import json
import math
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Dict, List, Tuple

# Pin BLAS / OpenMP to 1 thread per process. We parallelize at the center
# level via multiprocessing; with 30 workers each trying to spawn 32 OpenMP
# threads, the first batch was thrashing for ~12 minutes before the OS
# balanced affinity. Set these before numpy is imported.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import numpy as np
import pandas as pd
import mpmath as mp

from datetime import datetime


def log(msg: str) -> None:
    """Timestamped, flushed line. Unified logging helper across the gate1 scripts."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))


def _default_out(*parts: str) -> str:
    """Resolve <script_dir>/out/<parts...>; unified outputs location."""
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


try:
    from numpy import trapezoid as _trapz
except ImportError:
    from numpy import trapz as _trapz


# -----------------------------
# Canonical gamma curvature term B_2(t)
# -----------------------------
#
# Canonical zero-side curvature is q''_can(t) = B_2(t) + sum_rho K_2(t; rho).
# B_2(t) = theta'''(t) = -(1/8) Re psi^(2)(1/4 + i t/2). For t > 50 the
# asymptotic B_2(t) ~ -1/(2 t^2) agrees with the exact polygamma expression
# to better than 1 part in 10^4 (smaller still as t grows), so we use the
# closed form there and fall back to mpmath only for low heights.

_B2_ASYMPTOTIC_CUTOFF = 50.0


def B2_exact(t: float, dps: int = 30) -> float:
    mp.mp.dps = dps
    z = mp.mpc(mp.mpf("0.25"), mp.mpf(t) / 2)
    return float(-mp.re(mp.polygamma(2, z)) / 8.0)


def B2_fast(t: float, dps: int = 30) -> float:
    if t > _B2_ASYMPTOTIC_CUTOFF:
        return -0.5 / (t * t)
    return B2_exact(t, dps=dps)


def B2_array(xs: np.ndarray, dps: int = 30) -> np.ndarray:
    """Vectorized B_2 over a grid. Asymptotic where xs > cutoff, else exact."""
    out = np.empty_like(xs, dtype=float)
    mask_large = xs > _B2_ASYMPTOTIC_CUTOFF
    if mask_large.any():
        out[mask_large] = -0.5 / (xs[mask_large] ** 2)
    if not mask_large.all():
        small_idx = np.where(~mask_large)[0]
        for i in small_idx:
            out[i] = B2_exact(float(xs[i]), dps=dps)
    return out


# Process-local cache: same xs grid is reused across stability_W /
# stability_kappa / B2-toggle variants; only stability_nquad changes it.
# Cache hit on the second-and-later use saves ~13 redundant polygamma sweeps
# per (center, c_I) at low-t centers where the asymptotic cutoff doesn't fire.
# Keyed by (xs[0], xs[-1], len(xs), dps) — coarse enough that nearby grids
# don't collide and fine enough that identical grids from the same call site
# always hit. Grows monotonically; capped via FIFO eviction below.
_B2_CACHE: Dict[Tuple[float, float, int, int], np.ndarray] = {}
_B2_CACHE_MAX = 4096


def B2_array_cached(xs: np.ndarray, dps: int = 30) -> np.ndarray:
    if len(xs) == 0:
        return np.empty(0, dtype=float)
    key = (round(float(xs[0]), 9), round(float(xs[-1]), 9), int(len(xs)), int(dps))
    cached = _B2_CACHE.get(key)
    if cached is not None and cached.shape == xs.shape:
        return cached
    result = B2_array(xs, dps=dps)
    if len(_B2_CACHE) >= _B2_CACHE_MAX:
        # Cheap FIFO drop: pop the oldest insertion.
        _B2_CACHE.pop(next(iter(_B2_CACHE)))
    _B2_CACHE[key] = result
    return result


# -----------------------------
# Top-level workers (must be picklable for ProcessPoolExecutor)
# -----------------------------

def _siegelz_chunk_eval(args):
    xs, dps = args
    mp.mp.dps = dps
    return np.array([float(mp.siegelz(float(x))) for x in xs], dtype=float)


def _siegelz_bisect(args):
    a, b, fa, fb, dps, n_iter = args
    mp.mp.dps = dps
    for _ in range(n_iter):
        mid = 0.5 * (a + b)
        fm = float(mp.siegelz(mid))
        if fa == 0:
            return a
        if fm == 0:
            return mid
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return 0.5 * (a + b)


def _gram_single_n(args):
    n, lo, hi, dps, scan_pts, n_bisect = args
    mp.mp.dps = dps
    target = n * math.pi
    xs = np.linspace(lo, hi, scan_pts)
    vals = np.array([float(mp.siegeltheta(float(x))) - target for x in xs], dtype=float)
    idxs = np.where(vals[:-1] * vals[1:] <= 0)[0]
    if len(idxs) == 0:
        return None

    i = int(idxs[0])
    a, b = float(xs[i]), float(xs[i + 1])
    fa = float(mp.siegeltheta(a)) - target

    for _ in range(n_bisect):
        mid = 0.5 * (a + b)
        fm = float(mp.siegeltheta(mid)) - target
        if fa * fm <= 0:
            b = mid
        else:
            a, fa = mid, fm

    g = 0.5 * (a + b)
    if lo <= g <= hi:
        return g
    return None


def _scan_zone_worker(args):
    """Run a single zone scan serially inside one worker process."""
    zone, args_dict = args
    ns = argparse.Namespace(**args_dict)
    # Children must run serially -- nested ProcessPoolExecutors are not allowed
    # (or at least asking for trouble across platforms).
    ns.workers = 1
    return scan_zone(zone, ns)


# -----------------------------
# Hardy Z zero proxy
# -----------------------------

def cache_key(t_center: float, radius: float, step: float, dps: int) -> str:
    s = f"{t_center:.8f}_{radius:.8f}_{step:.8f}_{dps}"
    return hashlib.sha1(s.encode()).hexdigest()[:16]


def hardy_z_zeros_near(
    t_center: float,
    radius: float,
    step: float = 0.1,
    dps: int = 30,
    cache_dir: str = "zero_proxy_cache",
    force: bool = False,
    workers: int = 1,
) -> np.ndarray:
    """
    Find approximate critical-line zeros by sign changes of Hardy Z(t).

    This is proxy data, not verified Odlyzko-quality zero data.
    """
    os.makedirs(cache_dir, exist_ok=True)
    key = cache_key(t_center, radius, step, dps)
    path = os.path.join(cache_dir, f"zeros_{key}.json")

    if os.path.exists(path) and not force:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return np.array(data["zeros"], dtype=float)

    mp.mp.dps = dps
    lo = t_center - radius
    hi = t_center + radius
    xs = np.arange(lo, hi + step, step)

    # Evaluate siegelz on the full grid (parallel chunks if requested).
    if workers > 1 and len(xs) >= 2 * workers:
        chunks = np.array_split(xs, workers)
        chunk_args = [(np.asarray(c, dtype=float), dps) for c in chunks]
        with ProcessPoolExecutor(max_workers=workers) as ex:
            chunk_vals = list(ex.map(_siegelz_chunk_eval, chunk_args))
        vals = np.concatenate(chunk_vals)
    else:
        vals = _siegelz_chunk_eval((xs, dps))

    # Identify sign-change brackets.
    bracket_args = []
    exact_zeros: List[float] = []

    for i in range(len(xs) - 1):
        prev_x, prev_v = float(xs[i]), float(vals[i])
        x, v = float(xs[i + 1]), float(vals[i + 1])

        if prev_v == 0.0:
            exact_zeros.append(prev_x)
        elif v == 0.0 and i == len(xs) - 2:
            exact_zeros.append(x)
        elif prev_v * v < 0:
            bracket_args.append((prev_x, x, prev_v, v, dps, 40))

    # Bisect brackets in parallel.
    bisect_zeros: List[float] = []
    if bracket_args:
        if workers > 1 and len(bracket_args) >= 2:
            with ProcessPoolExecutor(max_workers=workers) as ex:
                bisect_zeros = list(ex.map(_siegelz_bisect, bracket_args))
        else:
            bisect_zeros = [_siegelz_bisect(a) for a in bracket_args]

    zeros = np.array(
        sorted(set(round(z, 12) for z in (exact_zeros + bisect_zeros))),
        dtype=float,
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "t_center": t_center,
                "radius": radius,
                "step": step,
                "dps": dps,
                "zeros": zeros.tolist(),
            },
            f,
            indent=2,
        )

    return zeros


# -----------------------------
# Zero-kernel proxy q''
# -----------------------------

def K2_proxy(m: np.ndarray, gamma: float, eps: float) -> np.ndarray:
    x = m - gamma
    den = x * x + eps * eps
    return 2.0 * eps * (3.0 * x * x - eps * eps) / (den ** 3)


def q2_zero_proxy(
    xs: np.ndarray,
    zeros: np.ndarray,
    center: float,
    W_factor: float,
    kappa: float,
    include_B2: bool = False,
    mp_dps: int = 30,
) -> Tuple[np.ndarray, int]:
    """Canonical-shape proxy q''_can,eta(t) = B_2(t) + sum_{|gamma-t|<=W_abs} K2(t; gamma, eps).

    `include_B2` toggles the canonical gamma curvature term. `W_abs = W_factor/Q`
    matches the factor semantics used by agent1/agent3 and by the `tail_edge`
    guard in scan_zone.
    """
    Q = math.log(center / (2.0 * math.pi))
    eps = kappa / Q
    W_abs = W_factor / Q
    use = zeros[np.abs(zeros - center) <= W_abs]

    vals = np.zeros_like(xs, dtype=float)
    for g in use:
        vals += K2_proxy(xs, g, eps)

    if include_B2:
        vals += B2_array_cached(xs, dps=mp_dps)

    return vals, len(use)


def interval_metrics(
    center: float,
    zeros: np.ndarray,
    c_I: float = 0.5,
    kappa: float = 0.5,
    W_factor: float = 40.0,
    nquad: int = 401,
    include_B2: bool = False,
    mp_dps: int = 30,
) -> Dict[str, float]:
    Q = math.log(center / (2.0 * math.pi))
    half = c_I / Q
    xs = np.linspace(center - half, center + half, nquad)

    vals, n_used = q2_zero_proxy(
        xs, zeros, center, W_factor=W_factor, kappa=kappa,
        include_B2=include_B2, mp_dps=mp_dps,
    )
    E = float(_trapz(vals ** 2, xs) / (2.0 * half))
    S = float(np.max(np.abs(vals)))
    B_eff = -math.log(max(E, 1e-300)) / math.log(Q)

    return {
        "E_I": E,
        "S_I": S,
        "B_eff": B_eff,
        "local_zero_count": n_used,
    }


def finite_jet_proxy(
    center: float,
    zeros: np.ndarray,
    R_jet: int = 4,
    kappa: float = 0.5,
    W_factor: float = 40.0,
    h_factor: float = 0.015,
    n_fit: int = 31,
    include_B2: bool = False,
    mp_dps: int = 30,
) -> Dict[str, float]:
    """
    Estimate normalized finite jets J_r = Delta^r d^r q2/dm^r(center)
    by local polynomial fitting.

    This is diagnostic only; high-order jet estimates are noisy.
    """
    Q = math.log(center / (2.0 * math.pi))
    Delta = 1.0 / Q
    h = h_factor / Q

    xs = center + np.linspace(-h, h, n_fit)
    vals, _ = q2_zero_proxy(
        xs, zeros, center, W_factor=W_factor, kappa=kappa,
        include_B2=include_B2, mp_dps=mp_dps,
    )

    deg = min(max(R_jet + 2, 6), n_fit - 1)
    # Fit in local variable y = x - center for numerical conditioning.
    y = xs - center
    coeff = np.polyfit(y, vals, deg=deg)  # descending powers

    jets = []
    p = np.poly1d(coeff)
    for r in range(R_jet + 1):
        deriv = np.polyder(p, m=r)
        raw = float(deriv(0.0))
        jets.append((Delta ** r) * raw)

    jets = np.array(jets, dtype=float)
    return {
        "J_max": float(np.max(np.abs(jets))),
        "J_rms": float(np.sqrt(np.mean(jets * jets))),
        "J_0": float(jets[0]),
        "J_1": float(jets[1]) if len(jets) > 1 else np.nan,
        "J_2": float(jets[2]) if len(jets) > 2 else np.nan,
        "J_3": float(jets[3]) if len(jets) > 3 else np.nan,
        "J_4": float(jets[4]) if len(jets) > 4 else np.nan,
    }


# -----------------------------
# Center generation
# -----------------------------

def gram_points_near(lo: float, hi: float, dps: int = 30, workers: int = 1) -> np.ndarray:
    """
    Approximate Gram points by solving theta(t) = n*pi.
    Uses coarse bracketing based on sampled theta.
    """
    mp.mp.dps = dps

    # Determine n range from theta endpoints.
    th_lo = float(mp.siegeltheta(lo))
    th_hi = float(mp.siegeltheta(hi))
    n_lo = math.floor(min(th_lo, th_hi) / math.pi) - 2
    n_hi = math.ceil(max(th_lo, th_hi) / math.pi) + 2

    args_list = [
        (n, lo, hi, dps, 300, 40)
        for n in range(n_lo, n_hi + 1)
    ]

    if workers > 1 and len(args_list) >= 2:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            results = list(ex.map(_gram_single_n, args_list))
    else:
        results = [_gram_single_n(a) for a in args_list]

    gps = [r for r in results if r is not None]
    return np.array(sorted(set(round(g, 12) for g in gps)), dtype=float)


def build_centers_for_zone(
    zeros: np.ndarray,
    zone_center: float,
    radius: float,
    random_count: int = 80,
    uniform_count: int = 120,
    seed: int = 0,
    include_gram: bool = True,
    workers: int = 1,
) -> List[Tuple[str, float]]:
    lo, hi = zone_center - radius, zone_center + radius
    centers = []

    z = zeros[(zeros >= lo) & (zeros <= hi)]
    for g in z:
        centers.append(("zero_ordinate", float(g)))

    if len(z) >= 2:
        mids = 0.5 * (z[:-1] + z[1:])
        gaps = z[1:] - z[:-1]

        for m in mids:
            centers.append(("gap_midpoint", float(m)))

        # Top quartile gap midpoints.
        thresh = np.quantile(gaps, 0.75)
        for m, gap in zip(mids, gaps):
            if gap >= thresh:
                centers.append(("large_gap_midpoint", float(m)))

        # Bottom quartile gap midpoints.
        sthresh = np.quantile(gaps, 0.25)
        for m, gap in zip(mids, gaps):
            if gap <= sthresh:
                centers.append(("small_gap_midpoint", float(m)))

    rng = np.random.default_rng(seed)
    for m in rng.uniform(lo, hi, size=random_count):
        centers.append(("random", float(m)))

    for m in np.linspace(lo, hi, uniform_count):
        centers.append(("uniform", float(m)))

    if include_gram:
        try:
            gps = gram_points_near(lo, hi, workers=workers)
            for g in gps:
                centers.append(("gram_point", float(g)))
        except Exception as e:
            print(f"WARNING: Gram point generation failed near {zone_center}: {e}")

    # Deduplicate by rounded center and family.
    seen = set()
    out = []
    for fam, c in centers:
        key = (fam, round(c, 9))
        if key not in seen and lo <= c <= hi:
            seen.add(key)
            out.append((fam, c))

    return out


# -----------------------------
# Candidate loading
# -----------------------------

def load_zones(args) -> List[float]:
    zones = []

    # Explicit --zones overrides --candidate-csv. The CSV is only consulted
    # when no zones were given on the command line.
    if args.zones:
        zones.extend(args.zones)
    elif args.candidate_csv:
        df = pd.read_csv(args.candidate_csv)

        # Try common columns.
        t_col = None
        for col in ["best_t0", "t0", "candidate_t0"]:
            if col in df.columns:
                t_col = col
                break
        if t_col is None:
            raise ValueError(f"No t0 column found in {args.candidate_csv}")

        sort_col = None
        for col in ["E_cI_0.5", "best_objective", "source_objective", "J_max"]:
            if col in df.columns:
                sort_col = col
                break

        if sort_col:
            df = df.sort_values(sort_col, ascending=True)

        zones.extend([float(x) for x in df[t_col].head(args.top).tolist()])

    # Deduplicate nearby zones.
    zones_sorted = []
    for z in sorted(zones):
        if not zones_sorted or abs(z - zones_sorted[-1]) > args.merge_distance:
            zones_sorted.append(z)

    return zones_sorted


# -----------------------------
# Main scan
# -----------------------------

def scan_zone(zone: float, args) -> Tuple[pd.DataFrame, Dict]:
    zeros = hardy_z_zeros_near(
        zone,
        radius=args.zero_radius,
        step=args.zero_step,
        dps=args.mp_dps,
        cache_dir=args.cache_dir,
        force=args.force_zero_rescan,
        workers=args.workers,
    )

    centers = build_centers_for_zone(
        zeros=zeros,
        zone_center=zone,
        radius=args.scan_radius,
        random_count=args.random_count,
        uniform_count=args.uniform_count,
        seed=args.seed,
        include_gram=not args.no_gram,
        workers=args.workers,
    )

    rows = []
    for fam, center in centers:
        Q_check = math.log(center / (2.0 * math.pi))
        if Q_check <= 1.0:
            continue
        for c_I in args.c_I_values:
            base = {
                "zone": zone,
                "center_type": fam,
                "m0": center,
                "c_I": c_I,
                "kappa": args.kappa,
                "W_factor": args.W_factor,
                "nquad": args.nquad,
                "R_jet": args.R_jet,
                "Q": Q_check,
            }

            metrics = interval_metrics(
                center, zeros,
                c_I=c_I, kappa=args.kappa, W_factor=args.W_factor, nquad=args.nquad,
                include_B2=args.include_B2, mp_dps=args.mp_dps,
            )
            jets = finite_jet_proxy(
                center, zeros,
                R_jet=args.R_jet, kappa=args.kappa, W_factor=args.W_factor,
                h_factor=args.jet_h_factor, n_fit=args.jet_fit_points,
                include_B2=args.include_B2, mp_dps=args.mp_dps,
            )

            # Tail drift: vary cutoff window. Quad drift: vary nquad.
            # Eta drift: vary kappa (smoothing scale eps = kappa/Q). B2 drift:
            # toggle the canonical gamma term to detect B_2-driven artifacts.
            E_base = metrics["E_I"]

            tail_E = []
            for W2 in args.stability_W:
                tail_E.append(interval_metrics(
                    center, zeros, c_I=c_I, kappa=args.kappa, W_factor=W2, nquad=args.nquad,
                    include_B2=args.include_B2, mp_dps=args.mp_dps,
                )["E_I"])
            tail_drift_rel = max(abs(e - E_base) for e in tail_E) / max(abs(E_base), 1e-300)

            quad_E = []
            for nq in args.stability_nquad:
                quad_E.append(interval_metrics(
                    center, zeros, c_I=c_I, kappa=args.kappa, W_factor=args.W_factor, nquad=int(nq),
                    include_B2=args.include_B2, mp_dps=args.mp_dps,
                )["E_I"])
            quad_drift_rel = max(abs(e - E_base) for e in quad_E) / max(abs(E_base), 1e-300)

            kappa_E = []
            for k2 in args.stability_kappa:
                kappa_E.append(interval_metrics(
                    center, zeros, c_I=c_I, kappa=float(k2), W_factor=args.W_factor, nquad=args.nquad,
                    include_B2=args.include_B2, mp_dps=args.mp_dps,
                )["E_I"])
            kappa_drift_rel = max(abs(e - E_base) for e in kappa_E) / max(abs(E_base), 1e-300)

            if args.include_B2:
                E_no_B2 = interval_metrics(
                    center, zeros, c_I=c_I, kappa=args.kappa, W_factor=args.W_factor, nquad=args.nquad,
                    include_B2=False, mp_dps=args.mp_dps,
                )["E_I"]
                B2_drift_rel = abs(E_base - E_no_B2) / max(abs(E_base), 1e-300)
            else:
                B2_drift_rel = float("nan")

            # Tail-edge guard: the largest stability window 2 * max(stability_W) / Q
            # might extend beyond the available zero range, in which case the
            # tail_drift_rel comparison can look stable for the wrong reason.
            W_max = max(list(args.stability_W) + [args.W_factor])
            W2_abs = 2.0 * W_max / Q_check
            tail_edge = bool(
                len(zeros) >= 2 and
                ((center - W2_abs < float(zeros[0])) or (center + W2_abs > float(zeros[-1])))
            )

            row = {
                **base,
                "include_B2": bool(args.include_B2),
                **metrics,
                **jets,
                "tail_drift_rel": tail_drift_rel,
                "tail_edge": tail_edge,
                "quad_drift_rel": quad_drift_rel,
                "kappa_drift_rel": kappa_drift_rel,
                "B2_drift_rel": B2_drift_rel,
            }
            rows.append(row)

    meta = {
        "zone": zone,
        "zero_count": len(zeros),
        "center_count": len(centers),
    }
    return pd.DataFrame(rows), meta


def summarize_results(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    idx = df.groupby(["zone", "center_type", "c_I"])["E_I"].idxmin()
    summary = df.loc[idx].copy()
    summary = summary.sort_values(["zone", "E_I"], ascending=[True, True])
    return summary


def classify_row(
    row,
    tail_tol: float = 2e-2,
    quad_tol: float = 1e-5,
    kappa_tol: float = 0.1,
    B2_tol: float = 0.5,
):
    """Unified status. Combines agent1/agent3 stability rejects with the
    canonical artifact diagnostics:

    - `artifact_eta`: large drift across kappa (smoothing scale eps=kappa/Q),
      i.e. the candidate is a critical-line smoothing artifact.
    - `artifact_B2`: large drift when toggling the B_2 gamma term, i.e. the
      candidate is dominated by the background curvature term and not by the
      zero structure.

    `candidate_proxy_flat` requires small J_max (simultaneous interval and
    finite-jet flatness). `tail_edge` shorts the chain so near-edge centers
    are not accepted as 'healthy' just because the truncated 2*W window
    happens to look stable for the wrong reason.
    """
    tail_drift = float(row.get("tail_drift_rel", float("nan")))
    quad_drift = float(row.get("quad_drift_rel", float("nan")))
    kappa_drift = float(row.get("kappa_drift_rel", float("nan")))
    B2_drift = float(row.get("B2_drift_rel", float("nan")))
    B_eff = float(row.get("B_eff", float("nan")))
    J_max = float(row.get("J_max", float("nan")))
    tail_edge = bool(row.get("tail_edge", False))

    if tail_edge:
        return "reject_tail_edge"
    if not math.isfinite(tail_drift) or tail_drift > tail_tol:
        return "reject_tail_unstable"
    if not math.isfinite(quad_drift) or quad_drift > quad_tol:
        return "reject_quad_unstable"
    if math.isfinite(kappa_drift) and kappa_drift > kappa_tol:
        return "artifact_eta"
    if math.isfinite(B2_drift) and B2_drift > B2_tol:
        return "artifact_B2"
    if math.isfinite(B_eff) and math.isfinite(J_max) and B_eff > 20 and J_max < 1e-8:
        return "serious_proxy_warning"
    if math.isfinite(B_eff) and math.isfinite(J_max) and B_eff > 10 and J_max < 1e-6:
        return "candidate_proxy_flat"
    if math.isfinite(B_eff) and B_eff > 5:
        return "watch"
    return "healthy"


# -----------------------------
# Param hashing + resume
# -----------------------------

# Args that affect the per-row contents. Orchestration knobs (workers, top,
# zones list, output paths, force-zero-rescan, resume) are deliberately
# excluded so they don't invalidate cached rows.
_PARAM_HASH_KEYS = (
    "scan_radius",
    "kappa",
    "W_factor",
    "nquad",
    "R_jet",
    "jet_h_factor",
    "jet_fit_points",
    "random_count",
    "uniform_count",
    "seed",
    "no_gram",
    "stability_W",
    "stability_nquad",
    "stability_kappa",
    "c_I_values",
    "mp_dps",
    "zero_radius",
    "zero_step",
    "include_B2",
)


def compute_param_hash(args) -> str:
    payload = {}
    for k in _PARAM_HASH_KEYS:
        v = getattr(args, k)
        if isinstance(v, (list, tuple)):
            v = sorted(float(x) for x in v)
        elif isinstance(v, bool):
            v = bool(v)
        payload[k] = v
    s = json.dumps(payload, sort_keys=True)
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def _backup(path: str) -> str:
    bak = path + ".bak"
    if os.path.exists(bak):
        os.remove(bak)
    os.rename(path, bak)
    return bak


def with_hash_suffix(path: str, h: str) -> str:
    """Insert .<hash> before the file extension (unified gate1 convention).
    'a/b.csv' -> 'a/b.<h>.csv'."""
    root, ext = os.path.splitext(path)
    return f"{root}.{h}{ext}"


def open_resume_state(csv_path: str, param_hash: str, resume_flag: bool):
    """
    Decide whether the existing per-hash output CSV should be resumed from.

    Returns (done_zones_set, header_needed_bool). On --no-resume or an
    unreadable/malformed file, the existing file is moved to <csv_path>.bak
    and a fresh write begins.
    """
    if not resume_flag and os.path.exists(csv_path):
        bak = _backup(csv_path)
        print(f"--no-resume: moved existing {csv_path} -> {bak}")
        return set(), True

    if not os.path.exists(csv_path):
        return set(), True

    try:
        existing = pd.read_csv(csv_path)
    except Exception as e:
        bak = _backup(csv_path)
        print(f"WARN: could not read {csv_path} ({e}); moved to {bak}")
        return set(), True

    if "zone" not in existing.columns:
        bak = _backup(csv_path)
        print(f"WARN: {csv_path} lacks 'zone' column; moved to {bak}")
        return set(), True

    # Defensive: filter out any rows whose stamped param_hash disagrees with
    # the filename (should not happen unless a previous run was interrupted
    # mid-write). Keep the file but ignore the bad rows for resume purposes.
    if "param_hash" in existing.columns:
        bad = existing[existing["param_hash"].astype(str) != param_hash]
        if len(bad):
            print(
                f"WARN: {csv_path} contains {len(bad)} row(s) with non-matching "
                f"param_hash; expected {param_hash}. Ignoring those for resume."
            )
            existing = existing[existing["param_hash"].astype(str) == param_hash]

    done_zones = set(round(float(z), 6) for z in existing["zone"].unique())
    print(
        f"Resume: {csv_path} has {len(existing)} row(s) covering {len(done_zones)} zone(s)."
    )
    return done_zones, False


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument("--candidate-csv", default=_default_out("gate1_surrogate_best_candidates.csv"),
                   help="Path to surrogate-best-candidates CSV. Default reads from <script>/out/.")
    p.add_argument("--zones", type=float, nargs="*", default=[])
    p.add_argument("--top", type=int, default=8)
    p.add_argument("--merge-distance", type=float, default=5.0)

    p.add_argument("--zero-radius", type=float, default=55.0)
    p.add_argument("--scan-radius", type=float, default=35.0)
    p.add_argument("--zero-step", type=float, default=0.1)
    p.add_argument("--mp-dps", type=int, default=30)
    p.add_argument("--cache-dir", default=_default_out("zero_proxy_cache"),
                   help="Hardy-Z zero cache directory. Default lands under <script>/out/.")
    p.add_argument("--force-zero-rescan", action="store_true")

    p.add_argument("--c-I-values", dest="c_I_values", type=float, nargs="+",
                   default=[0.1, 0.2, 0.5, 1.0])
    p.add_argument("--kappa", type=float, default=0.5)
    p.add_argument("--W-factor", dest="W_factor", type=float, default=40.0)
    p.add_argument("--nquad", type=int, default=401)

    p.add_argument("--R-jet", dest="R_jet", type=int, default=4)
    p.add_argument("--jet-h-factor", type=float, default=0.015)
    p.add_argument("--jet-fit-points", type=int, default=31)

    p.add_argument("--random-count", type=int, default=80)
    p.add_argument("--uniform-count", type=int, default=120)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--no-gram", action="store_true")

    p.add_argument("--stability-W", type=float, nargs="+", default=[10.0, 20.0, 40.0],
                   help="W_factor values used to compute tail_drift_rel.")
    p.add_argument("--stability-nquad", type=int, nargs="+", default=[201, 401, 801],
                   help="nquad values used to compute quad_drift_rel.")
    p.add_argument("--stability-kappa", type=float, nargs="+",
                   default=[0.0625, 0.125, 0.25, 0.5, 1.0, 2.0],
                   help="kappa values used to compute kappa_drift_rel "
                        "(eta-sweep for critical-line smoothing scale eps=kappa/Q).")

    p.add_argument(
        "--include-B2",
        dest="include_B2",
        action="store_true",
        default=True,
        help="Add the canonical gamma curvature term B_2(t) to q'' (default).",
    )
    p.add_argument(
        "--no-include-B2",
        dest="include_B2",
        action="store_false",
        help="Disable B_2; use the bare K_2 zero kernel only (proxy-only mode).",
    )

    p.add_argument(
        "--workers",
        type=int,
        default=max(1, min((os.cpu_count() or 2) - 2, 10)),
        help="Process-pool size for mpmath-heavy work "
             "(default: max(1, min(cpu_count - 2, 10))).",
    )

    p.add_argument(
        "--out",
        default=_default_out("gate1_actual_zero_proxy_zone_scan.csv"),
        help=(
            "Output CSV stem. The current param_hash is inserted before the "
            "extension, e.g. <stem>.<hash>.csv, so each param set has its own file. "
            "Default lands in <script>/out/."
        ),
    )
    p.add_argument(
        "--summary-out",
        default=_default_out("gate1_actual_zero_proxy_zone_summary.csv"),
        help="Summary CSV stem. Hash-suffixed the same way as --out. "
             "Default lands in <script>/out/.",
    )

    p.add_argument(
        "--resume",
        dest="resume",
        action="store_true",
        default=True,
        help="Resume from the per-hash output CSV if it exists (default).",
    )
    p.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
        help="Ignore existing per-hash --out file; back it up to .bak and start fresh.",
    )

    return p.parse_args()


def _print_zone_best(zone: float, df_zone: pd.DataFrame, idx: int, total: int):
    log(f"[{idx}/{total}] Zone {zone:.6f}")
    if not df_zone.empty:
        best = df_zone.sort_values("E_I").head(5)
        cols = ["center_type", "m0", "c_I", "E_I", "B_eff", "J_max",
                "tail_drift_rel", "quad_drift_rel",
                "kappa_drift_rel", "B2_drift_rel", "tail_edge"]
        cols = [c for c in cols if c in best.columns]
        print(best[cols].to_string(index=False), flush=True)


def _finalize_zone_df(df_zone: pd.DataFrame, param_hash: str) -> pd.DataFrame:
    if df_zone.empty:
        return df_zone
    df_z = df_zone.copy()
    df_z["status"] = df_z.apply(classify_row, axis=1)
    df_z["param_hash"] = param_hash
    return df_z


def main():
    args = parse_args()
    zones = load_zones(args)

    if not zones:
        raise RuntimeError("No zones supplied. Use --candidate-csv or --zones.")

    n_zones = len(zones)
    workers = max(1, int(args.workers))
    param_hash = compute_param_hash(args)
    out_path = with_hash_suffix(args.out, param_hash)
    for _p in (out_path, args.summary_out, args.cache_dir):
        _parent = _p if _p == args.cache_dir else os.path.dirname(os.path.abspath(_p))
        if _parent:
            os.makedirs(_parent, exist_ok=True)
    summary_path = with_hash_suffix(args.summary_out, param_hash)

    log(f"Scanning {n_zones} zones with --workers {workers}, param_hash={param_hash}:")
    for z in zones:
        log(f"  {z:.6f}")
    log(f"Output:  {out_path}")
    log(f"Summary: {summary_path}")

    done_zones, header_needed = open_resume_state(out_path, param_hash, args.resume)

    pending_zones = [z for z in zones if round(z, 6) not in done_zones]
    skipped = n_zones - len(pending_zones)
    if skipped:
        log(f"Skipping {skipped} zone(s) already complete in {out_path}.")

    metas: List[Dict] = []

    def write_zone(df_zone: pd.DataFrame):
        """Best-effort per-zone append.

        Serialize the whole zone to an in-memory buffer first, then issue a
        single write(). The win is against SIGINT/Ctrl-C: CPython delivers
        signals between bytecodes and the actual write is a single C call, so
        a Python-level interrupt won't leave a half-written zone in the file.

        This is *not* POSIX-atomic. Hard crashes, kernel panics, or power loss
        between the write and disk flush can still leave the file truncated
        mid-payload. If you need stronger guarantees, the right tool is a
        zone-complete manifest or write-to-temp-then-rename, not fsync.
        """
        nonlocal header_needed
        df_z = _finalize_zone_df(df_zone, param_hash)
        if df_z.empty:
            return
        buf = io.StringIO()
        df_z.to_csv(buf, header=header_needed, index=False)
        payload = buf.getvalue().encode("utf-8")
        with open(out_path, "ab") as f:
            f.write(payload)
        header_needed = False

    if pending_zones:
        n_pending = len(pending_zones)
        use_zone_pool = n_pending >= 2 and workers >= 2

        if use_zone_pool:
            zone_workers = min(workers, n_pending)
            log(
                f"Dispatching {n_pending} pending zone(s) in parallel "
                f"(pool={zone_workers}); each zone runs serially."
            )

            args_dict = vars(args)
            completed = 0
            with ProcessPoolExecutor(max_workers=zone_workers) as ex:
                futures = {
                    ex.submit(_scan_zone_worker, (zone, args_dict)): zone
                    for zone in pending_zones
                }
                for fut in as_completed(futures):
                    zone = futures[fut]
                    completed += 1
                    df_zone, meta = fut.result()
                    metas.append(meta)
                    write_zone(df_zone)
                    _print_zone_best(zone, df_zone, completed, n_pending)
        else:
            if n_pending == 1 and workers >= 2:
                log(f"Single pending zone: using within-zone parallelism (pool={workers}).")
            else:
                log("Running pending zones serially.")

            for i, zone in enumerate(pending_zones, start=1):
                df_zone, meta = scan_zone(zone, args)
                metas.append(meta)
                write_zone(df_zone)
                _print_zone_best(zone, df_zone, i, n_pending)
    else:
        log("All requested zones already complete; rebuilding summary only.")

    # Read back the per-hash CSV for summary + final report.
    if not os.path.exists(out_path):
        log(f"No data written to {out_path}; nothing to summarize.")
        return

    full_df = pd.read_csv(out_path)
    if "param_hash" in full_df.columns:
        full_df = full_df[full_df["param_hash"].astype(str) == param_hash].copy()
    if not full_df.empty:
        full_df = full_df.sort_values(["zone", "E_I"]).reset_index(drop=True)

    summary = summarize_results(full_df)
    if not summary.empty:
        summary["status"] = summary.apply(classify_row, axis=1)
    summary.to_csv(summary_path, index=False)

    log("Wrote:")
    log(f"  {out_path}")
    log(f"  {summary_path}")

    log("Best overall rows:")
    if not full_df.empty:
        cols = ["zone", "center_type", "m0", "c_I", "E_I", "B_eff", "J_max",
                "tail_drift_rel", "quad_drift_rel",
                "kappa_drift_rel", "B2_drift_rel", "tail_edge", "status"]
        cols = [c for c in cols if c in full_df.columns]
        print(full_df.sort_values("E_I").head(20)[cols].to_string(index=False), flush=True)

    if metas:
        log("Zone metadata (this run):")
        metas_df = pd.DataFrame(metas).sort_values("zone").reset_index(drop=True)
        print(metas_df.to_string(index=False), flush=True)


if __name__ == "__main__":
    main()
