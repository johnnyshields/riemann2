#!/usr/bin/env python3
"""
gate1_canonical_zeta_crosscheck.py
----------------------------------

Numerical AFE / canonical-zeta cross-check for the zero-side proxy.

For each (m_0, c_I) target on the canonical_eta_targets list, evaluate

    q''_can_eta(t) := d^3/dt^3 Im log xi(1/2 + eta + it)       (canonical sensor)
    q''_proxy(t)   := B_2(t) + sum_{|gamma-t|<=W_abs} K_2(t; gamma, eps)
                                                               (zero-side sensor)

on a shared tight grid in [m_0 - c_I/Q, m_0 + c_I/Q], where eta = kappa/Q.

Note the apparently-second-derivative q'' notation actually denotes the
THIRD t-derivative of Im log xi: K_2 is the kernel d^3/dt^3 arctan((t-g)/eta)
and B_2 = theta'''(t) -- both consistent with q''_can = d^3/dt^3 Im log xi.

The canonical sensor calls mpmath.zeta and mpmath.loggamma (both use AFE /
Riemann-Siegel internally at high t). The third derivative is taken by a
7-point central stencil (4th-order accurate). The proxy reuses the cached
Hardy-Z zero ordinates from the matching canonical-eta scan.

Outputs per (m_0, c_I):
  - E_I_zeta, B_eff_zeta            (canonical sensor)
  - E_I_proxy, B_eff_proxy          (zero-side sensor)
  - D_completed                     = ||q''_zeta - q''_proxy||^2 / ||q''_proxy||^2
  - ratio_E_zeta_proxy              = E_I_zeta / E_I_proxy

Decision: a candidate is canonical-consistent when D_completed < 0.1 and the
ratio is within a factor of two of unity.

This is a one-shot diagnostic, not part of the main scan. Multiprocessing is
used over (m_0, c_I) tasks; each task hits ~200 mpmath.zeta calls which is
the dominant cost.
"""

import argparse
import hashlib
import io
import json
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Tuple

# Pin BLAS / OpenMP to 1 thread per process.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import numpy as np
import pandas as pd
import mpmath as mp


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))
_SHARED_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "..", "zeta_bridge_shared"))
if _SHARED_DIR not in sys.path:
    sys.path.insert(0, _SHARED_DIR)


def _default_out(*parts: str) -> str:
    return os.path.join(_DEFAULT_OUT_DIR, *parts)


try:
    from numpy import trapezoid as _trapz
except ImportError:
    from numpy import trapz as _trapz


# Reuse canonical B_2 helpers and the proxy zero kernel.
from b2_canonical import B2_array_cached
from gate1_actual_zero_proxy_zone_scan import (
    K2_proxy,
    chi_smooth,
    hardy_z_zeros_near,
)


# -----------------------------
# Canonical-zeta sensor: q''_can = d^3/dt^3 Im log xi(1/2 + eta + it)
# -----------------------------

def _phi_xi_at(t: float, eta: float, dps: int) -> float:
    """Im log xi(1/2 + eta + it), built from log gamma + log zeta + linear term.

    log xi(s) = const + log s + log(s-1) - (s/2) log pi + log Gamma(s/2) + log zeta(s).
    The s(s-1) factor's imag part is small (O(1/t)) and contributes only
    O(1/t^k) to higher derivatives at our heights; it is included here for
    correctness.
    """
    mp.mp.dps = dps
    s = mp.mpc(mp.mpf("0.5") + mp.mpf(eta), mp.mpf(t))
    log_pi = mp.log(mp.pi)
    val = (
        mp.arg(s) + mp.arg(s - 1)
        - (mp.mpf(t) / 2) * log_pi
        + mp.im(mp.loggamma(s / 2))
        + mp.arg(mp.zeta(s))
    )
    return float(val)


def phi_xi_grid(t_grid: np.ndarray, eta: float, dps: int) -> np.ndarray:
    """Phi(t) = Im log xi(1/2 + eta + it), continuous in t for eta > 0."""
    raw = np.array([_phi_xi_at(float(t), eta, dps) for t in t_grid], dtype=float)
    # mp.arg returns a value in (-pi, pi]; for eta > 0 the underlying function
    # is continuous, so any 2*pi jumps are unwrappable artifacts of the
    # principal-value branch.
    return np.unwrap(raw)


def third_derivative_7point(y: np.ndarray, dt: float) -> np.ndarray:
    """7-point central 3rd derivative, O(dt^4) accurate.

    Interior (i in [3, n-4]):
      f'''(x_i) ~ ( f_{i-3} - 8 f_{i-2} + 13 f_{i-1}
                   -13 f_{i+1} + 8 f_{i+2} - f_{i+3}) / (8 dt^3)
    Edges fall back to the 5-point stencil (O(dt^2)):
      f'''(x_i) ~ (-f_{i-2} + 2 f_{i-1} - 2 f_{i+1} + f_{i+2}) / (2 dt^3)
    Far edges replicate the next-interior value to avoid boundary
    dominance in the squared integral.
    """
    n = len(y)
    d3 = np.empty(n)
    if n < 7:
        # 5-point fallback for short grids
        for i in range(2, n - 2):
            d3[i] = (-y[i - 2] + 2 * y[i - 1] - 2 * y[i + 1] + y[i + 2]) / (2.0 * dt ** 3)
        for i in (0, 1, n - 2, n - 1):
            d3[i] = d3[max(2, min(i, n - 3))]
        return d3
    for i in range(3, n - 3):
        d3[i] = (
            y[i - 3] - 8 * y[i - 2] + 13 * y[i - 1]
            - 13 * y[i + 1] + 8 * y[i + 2] - y[i + 3]
        ) / (8.0 * dt ** 3)
    for i in (2, n - 3):
        d3[i] = (-y[i - 2] + 2 * y[i - 1] - 2 * y[i + 1] + y[i + 2]) / (2.0 * dt ** 3)
    for i in (0, 1):
        d3[i] = d3[3]
    for i in (n - 2, n - 1):
        d3[i] = d3[n - 4]
    return d3


def q2_zeta(t_grid: np.ndarray, eta: float, dps: int = 40) -> np.ndarray:
    """Canonical sensor: d^3/dt^3 Im log xi(1/2 + eta + it)."""
    phi = phi_xi_grid(t_grid, eta=eta, dps=dps)
    dt = float(t_grid[1] - t_grid[0])
    return third_derivative_7point(phi, dt)


# -----------------------------
# Proxy sensor (matches the scanner's q2_zero_proxy)
# -----------------------------

def q2_proxy(
    xs: np.ndarray,
    zeros: np.ndarray,
    center: float,
    W_factor: float,
    kappa: float,
    include_B2: bool = True,
    cutoff_mode: str = "hard",
    mp_dps: int = 30,
) -> np.ndarray:
    Q = math.log(center / (2.0 * math.pi))
    eps = kappa / Q
    W_abs = W_factor / Q
    if cutoff_mode == "hard":
        use = zeros[np.abs(zeros - center) <= W_abs]
        weights = np.ones(len(use), dtype=float)
    elif cutoff_mode == "smooth":
        use = zeros[np.abs(zeros - center) <= 2.0 * W_abs]
        weights = chi_smooth((use - center) / W_abs)
    else:
        raise ValueError(f"unknown cutoff_mode: {cutoff_mode!r}")
    vals = np.zeros_like(xs, dtype=float)
    for g, w in zip(use, weights):
        if w == 0.0:
            continue
        vals += w * K2_proxy(xs, g, eps)
    if include_B2:
        vals += B2_array_cached(xs, dps=mp_dps)
    return vals


# -----------------------------
# Per-target evaluation
# -----------------------------

def _evaluate_target(args_tuple) -> Dict:
    (m0, c_I, kappa, W_factor, cutoff_mode, ngrid, mp_dps_zeta, mp_dps_b2,
     zeros_radius, zeros_step, zeros_dps, zeros_cache_dir) = args_tuple

    Q = math.log(m0 / (2.0 * math.pi))
    eta = kappa / Q
    half = c_I / Q

    t_grid = np.linspace(m0 - half, m0 + half, ngrid)

    # Canonical-zeta sensor
    q_z = q2_zeta(t_grid, eta=eta, dps=mp_dps_zeta)

    # Proxy sensor: load cached zeros (do NOT trigger a fresh scan here)
    zeros = hardy_z_zeros_near(
        m0, radius=zeros_radius, step=zeros_step, dps=zeros_dps,
        cache_dir=zeros_cache_dir, force=False, workers=1,
    )
    q_p = q2_proxy(
        t_grid, zeros, center=m0,
        W_factor=W_factor, kappa=kappa,
        include_B2=True, cutoff_mode=cutoff_mode, mp_dps=mp_dps_b2,
    )

    E_zeta = float(_trapz(q_z ** 2, t_grid) / (2.0 * half))
    E_proxy = float(_trapz(q_p ** 2, t_grid) / (2.0 * half))
    diff = q_z - q_p
    E_diff = float(_trapz(diff ** 2, t_grid) / (2.0 * half))

    B_zeta = -math.log(max(E_zeta, 1e-300)) / math.log(Q)
    B_proxy = -math.log(max(E_proxy, 1e-300)) / math.log(Q)

    D_completed = E_diff / max(E_proxy, 1e-300)
    ratio = E_zeta / max(E_proxy, 1e-300)

    return {
        "m0": m0,
        "c_I": c_I,
        "Q": Q,
        "eta_abs": eta,
        "kappa": kappa,
        "W_factor": W_factor,
        "cutoff_mode": cutoff_mode,
        "ngrid": ngrid,
        "n_local_zeros": int((np.abs(zeros - m0) <= W_factor / Q).sum()),
        "E_I_zeta": E_zeta,
        "B_eff_zeta": B_zeta,
        "E_I_proxy": E_proxy,
        "B_eff_proxy": B_proxy,
        "D_completed": D_completed,
        "ratio_E_zeta_proxy": ratio,
    }


# -----------------------------
# Main
# -----------------------------

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--targets-csv",
        default=_default_out("canonical_eta_targets.csv"),
        help="CSV of m_0 targets with a 'group' column.",
    )
    p.add_argument(
        "--c-I-values", dest="c_I_values", type=float, nargs="+",
        default=[0.1, 0.2, 0.5],
        help="c_I values to sweep per m_0.",
    )
    p.add_argument("--kappa", type=float, default=0.5)
    p.add_argument("--W-factor", dest="W_factor", type=float, default=40.0)
    p.add_argument(
        "--cutoff-mode", dest="cutoff_mode",
        choices=("hard", "smooth"), default="hard",
    )
    p.add_argument("--ngrid", type=int, default=201,
                   help="Grid points across the c_I/Q half-window.")
    p.add_argument("--mp-dps-zeta", dest="mp_dps_zeta", type=int, default=40,
                   help="Precision for mpmath.zeta evaluations.")
    p.add_argument("--mp-dps-b2", dest="mp_dps_b2", type=int, default=30,
                   help="Precision for B_2 polygamma evaluations.")
    p.add_argument("--zero-radius", type=float, default=90.0,
                   help="Hardy-Z cache radius (must match the canonical scan).")
    p.add_argument("--zero-step", type=float, default=0.075)
    p.add_argument("--zero-dps", type=int, default=40)
    p.add_argument(
        "--cache-dir",
        default=_default_out("zero_proxy_cache"),
    )
    p.add_argument(
        "--workers", type=int,
        default=max(1, (os.cpu_count() or 2) - 2),
    )
    p.add_argument(
        "--prioritize-non-watch",
        dest="prioritize_non_watch",
        action="store_true",
        default=True,
        help="Run B/C groups before A_watch (default).",
    )
    p.add_argument(
        "--out",
        default=_default_out("gate1_canonical_zeta_crosscheck.csv"),
    )
    return p.parse_args()


def _hash_args(args) -> str:
    payload = {
        "c_I_values": sorted(args.c_I_values),
        "kappa": args.kappa,
        "W_factor": args.W_factor,
        "cutoff_mode": args.cutoff_mode,
        "ngrid": args.ngrid,
        "mp_dps_zeta": args.mp_dps_zeta,
        "mp_dps_b2": args.mp_dps_b2,
        "zero_radius": args.zero_radius,
        "zero_step": args.zero_step,
        "zero_dps": args.zero_dps,
    }
    return hashlib.sha1(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:12]


def _with_hash_suffix(path: str, h: str) -> str:
    root, ext = os.path.splitext(path)
    return f"{root}.{h}{ext}"


def main():
    args = parse_args()
    out_hash = _hash_args(args)
    out_path = _with_hash_suffix(args.out, out_hash)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)

    targets_df = pd.read_csv(args.targets_csv)
    if "group" not in targets_df.columns:
        targets_df["group"] = "unknown"
    if args.prioritize_non_watch:
        # Order: B then C then A_watch (so non-watch runs first).
        order = {"B_top50_Beff": 0, "C_random_healthy": 1, "A_watch": 2}
        targets_df["_order"] = targets_df["group"].map(order).fillna(99)
        targets_df = targets_df.sort_values("_order").reset_index(drop=True)
        targets_df = targets_df.drop(columns=["_order"])

    n_targets = len(targets_df)
    n_c_I = len(args.c_I_values)
    n_tasks = n_targets * n_c_I
    log(f"Cross-check {n_targets} m_0 x {n_c_I} c_I = {n_tasks} (m_0, c_I) tasks")
    log(f"Output: {out_path}")

    # Build task list. Group label is preserved for post-hoc analysis.
    tasks = []
    task_meta = []
    for _, row in targets_df.iterrows():
        m0 = float(row["m0"])
        group = str(row.get("group", "unknown"))
        for c_I in args.c_I_values:
            tasks.append((
                m0, c_I,
                args.kappa, args.W_factor, args.cutoff_mode,
                args.ngrid, args.mp_dps_zeta, args.mp_dps_b2,
                args.zero_radius, args.zero_step, args.zero_dps,
                args.cache_dir,
            ))
            task_meta.append({"m0": m0, "c_I": c_I, "group": group})

    rows = []
    workers = max(1, int(args.workers))
    if workers > 1 and n_tasks > 1:
        log(f"Running on {workers} workers")
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(_evaluate_target, t): i for i, t in enumerate(tasks)}
            done_count = 0
            for fut in as_completed(futures):
                i = futures[fut]
                result = fut.result()
                result["group"] = task_meta[i]["group"]
                rows.append(result)
                done_count += 1
                if done_count % max(1, n_tasks // 20) == 0 or done_count == n_tasks:
                    log(f"  {done_count}/{n_tasks} done")
    else:
        log("Running serially")
        for i, t in enumerate(tasks, start=1):
            result = _evaluate_target(t)
            result["group"] = task_meta[i - 1]["group"]
            rows.append(result)
            if i % max(1, n_tasks // 20) == 0 or i == n_tasks:
                log(f"  {i}/{n_tasks} done")

    df = pd.DataFrame(rows)
    df = df.sort_values(["group", "m0", "c_I"]).reset_index(drop=True)
    df.to_csv(out_path, index=False)
    log(f"Wrote {out_path} ({len(df)} rows)")

    print()
    print("=== Cross-check summary by group ===")
    for g, gdf in df.groupby("group"):
        print(f"\n  {g}: {len(gdf)} rows")
        print(f"    D_completed     median {gdf['D_completed'].median():.4f}  "
              f"max {gdf['D_completed'].max():.4f}  min {gdf['D_completed'].min():.4f}")
        print(f"    ratio E zeta/proxy  median {gdf['ratio_E_zeta_proxy'].median():.4f}  "
              f"min {gdf['ratio_E_zeta_proxy'].min():.4f}  max {gdf['ratio_E_zeta_proxy'].max():.4f}")
        print(f"    B_eff_zeta      median {gdf['B_eff_zeta'].median():.3f}  max {gdf['B_eff_zeta'].max():.3f}")
        print(f"    B_eff_proxy     median {gdf['B_eff_proxy'].median():.3f}  max {gdf['B_eff_proxy'].max():.3f}")

    # Strict canonical-consistency rule:
    # D_completed < 0.1 AND |ratio - 1| < 1.0 (factor of two in either direction).
    print()
    print("=== Canonical-consistent rows (D_completed < 0.1 AND 0.5 <= ratio <= 2.0) ===")
    consistent = df[
        (df["D_completed"] < 0.1)
        & (df["ratio_E_zeta_proxy"] >= 0.5)
        & (df["ratio_E_zeta_proxy"] <= 2.0)
    ]
    print(f"  {len(consistent)} / {len(df)} rows pass")
    if len(consistent):
        cols = ["group", "m0", "c_I", "E_I_zeta", "E_I_proxy",
                "ratio_E_zeta_proxy", "D_completed", "B_eff_zeta", "B_eff_proxy"]
        print(consistent[cols].head(20).to_string(index=False))


if __name__ == "__main__":
    main()
