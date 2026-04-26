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

Dependencies:
  pip install numpy pandas mpmath
"""

import argparse
import hashlib
import json
import math
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import mpmath as mp


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

    def zval(x: float) -> float:
        return float(mp.siegelz(x))

    lo = t_center - radius
    hi = t_center + radius
    xs = np.arange(lo, hi + step, step)

    zeros = []
    prev_x = float(xs[0])
    prev_v = zval(prev_x)

    for x in xs[1:]:
        x = float(x)
        v = zval(x)

        if prev_v == 0.0:
            zeros.append(prev_x)
        elif v == 0.0:
            zeros.append(x)
        elif prev_v * v < 0:
            # Bisection refinement inside the sign-change bracket.
            a, b = prev_x, x
            fa, fb = prev_v, v
            for _ in range(40):
                mid = 0.5 * (a + b)
                fm = zval(mid)
                if fa == 0:
                    b = a
                    break
                if fm == 0:
                    a = b = mid
                    break
                if fa * fm <= 0:
                    b, fb = mid, fm
                else:
                    a, fa = mid, fm
            zeros.append(0.5 * (a + b))

        prev_x, prev_v = x, v

    zeros = np.array(sorted(set(round(z, 12) for z in zeros)), dtype=float)

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
    W: float,
    kappa: float,
) -> Tuple[np.ndarray, int]:
    Q = math.log(max(center, 3.0))
    eps = kappa / Q
    use = zeros[np.abs(zeros - center) <= W]

    vals = np.zeros_like(xs, dtype=float)
    for g in use:
        vals += K2_proxy(xs, g, eps)

    return vals, len(use)


def interval_metrics(
    center: float,
    zeros: np.ndarray,
    cI: float = 0.5,
    kappa: float = 0.5,
    W: float = 40.0,
    grid: int = 401,
) -> Dict[str, float]:
    Q = math.log(max(center, 3.0))
    half = cI / Q
    xs = np.linspace(center - half, center + half, grid)

    vals, n_used = q2_zero_proxy(xs, zeros, center, W=W, kappa=kappa)
    E = float(np.trapz(vals ** 2, xs) / (2.0 * half))
    S = float(np.max(np.abs(vals)))
    Beff = -math.log(max(E, 1e-300)) / math.log(Q)

    return {
        "E": E,
        "S": S,
        "Beff": Beff,
        "zeros_used": n_used,
    }


def finite_jet_proxy(
    center: float,
    zeros: np.ndarray,
    R: int = 4,
    kappa: float = 0.5,
    W: float = 40.0,
    h_factor: float = 0.015,
    n_fit: int = 31,
) -> Dict[str, float]:
    """
    Estimate normalized finite jets J_r = Delta^r d^r q2/dm^r(center)
    by local polynomial fitting.

    This is diagnostic only; high-order jet estimates are noisy.
    """
    Q = math.log(max(center, 3.0))
    Delta = 1.0 / Q
    h = h_factor / Q

    xs = center + np.linspace(-h, h, n_fit)
    vals, _ = q2_zero_proxy(xs, zeros, center, W=W, kappa=kappa)

    deg = min(max(R + 2, 6), n_fit - 1)
    # Fit in local variable y = x - center for numerical conditioning.
    y = xs - center
    coeff = np.polyfit(y, vals, deg=deg)  # descending powers

    jets = []
    p = np.poly1d(coeff)
    for r in range(R + 1):
        deriv = np.polyder(p, m=r)
        raw = float(deriv(0.0))
        jets.append((Delta ** r) * raw)

    jets = np.array(jets, dtype=float)
    return {
        "J_max": float(np.max(np.abs(jets))),
        "J_0": float(jets[0]),
        "J_1": float(jets[1]) if len(jets) > 1 else np.nan,
        "J_2": float(jets[2]) if len(jets) > 2 else np.nan,
        "J_3": float(jets[3]) if len(jets) > 3 else np.nan,
        "J_4": float(jets[4]) if len(jets) > 4 else np.nan,
    }


# -----------------------------
# Center generation
# -----------------------------

def gram_theta(t: float) -> float:
    """
    Riemann-Siegel theta approximation via mpmath.
    """
    return float(mp.siegeltheta(t))


def gram_points_near(lo: float, hi: float, dps: int = 30) -> np.ndarray:
    """
    Approximate Gram points by solving theta(t) = n*pi.
    Uses coarse bracketing based on sampled theta.
    """
    mp.mp.dps = dps

    # Determine n range.
    n_lo = math.floor(gram_theta(lo) / math.pi) - 2
    n_hi = math.ceil(gram_theta(hi) / math.pi) + 2

    gps = []
    for n in range(n_lo, n_hi + 1):
        target = n * math.pi

        # Find rough bracket by local scan.
        xs = np.linspace(lo, hi, 300)
        vals = np.array([gram_theta(float(x)) - target for x in xs])
        idxs = np.where(vals[:-1] * vals[1:] <= 0)[0]
        if len(idxs) == 0:
            continue

        i = idxs[0]
        a, b = float(xs[i]), float(xs[i + 1])
        fa = gram_theta(a) - target

        for _ in range(40):
            mid = 0.5 * (a + b)
            fm = gram_theta(mid) - target
            if fa * fm <= 0:
                b = mid
            else:
                a, fa = mid, fm
        g = 0.5 * (a + b)
        if lo <= g <= hi:
            gps.append(g)

    return np.array(sorted(set(round(g, 12) for g in gps)), dtype=float)


def build_centers_for_zone(
    zeros: np.ndarray,
    zone_center: float,
    radius: float,
    random_count: int = 80,
    uniform_count: int = 120,
    seed: int = 0,
    include_gram: bool = True,
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
            gps = gram_points_near(lo, hi)
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

    if args.zones:
        zones.extend(args.zones)

    if args.candidate_csv:
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
    )

    centers = build_centers_for_zone(
        zeros=zeros,
        zone_center=zone,
        radius=args.scan_radius,
        random_count=args.random_count,
        uniform_count=args.uniform_count,
        seed=args.seed,
        include_gram=not args.no_gram,
    )

    rows = []
    for fam, center in centers:
        for cI in args.cI:
            base = {
                "zone": zone,
                "family": fam,
                "center": center,
                "cI": cI,
                "Q": math.log(max(center, 3.0)),
                "zero_count_zone": len(zeros),
                "zero_min": float(np.min(zeros)) if len(zeros) else np.nan,
                "zero_max": float(np.max(zeros)) if len(zeros) else np.nan,
            }

            metrics = interval_metrics(
                center,
                zeros,
                cI=cI,
                kappa=args.kappa,
                W=args.W,
                grid=args.grid,
            )
            jets = finite_jet_proxy(
                center,
                zeros,
                R=args.R,
                kappa=args.kappa,
                W=args.W,
                h_factor=args.jet_h_factor,
                n_fit=args.jet_fit_points,
            )

            # Stability checks for selected small subset only: all rows get W/kappa drift.
            E_base = metrics["E"]

            tail_E = []
            for W2 in args.stability_W:
                tail_E.append(interval_metrics(center, zeros, cI=cI, kappa=args.kappa, W=W2, grid=args.grid)["E"])
            tail_drift = max(abs(e - E_base) for e in tail_E) / max(abs(E_base), 1e-300)

            reg_E = []
            for k2 in args.stability_kappa:
                reg_E.append(interval_metrics(center, zeros, cI=cI, kappa=k2, W=args.W, grid=args.grid)["E"])
            reg_drift = max(abs(e - E_base) for e in reg_E) / max(abs(E_base), 1e-300)

            row = {
                **base,
                **metrics,
                **jets,
                "tail_drift": tail_drift,
                "reg_drift": reg_drift,
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

    idx = df.groupby(["zone", "family", "cI"])["E"].idxmin()
    summary = df.loc[idx].copy()
    summary = summary.sort_values(["zone", "E"], ascending=[True, True])
    return summary


def classify_row(row, warn_Beff=3.0, serious_Beff=6.0, max_tail_drift=0.1):
    if row["tail_drift"] > max_tail_drift:
        return "reject_tail_unstable"
    if row["Beff"] >= serious_Beff and row["J_max"] < 1e-2:
        return "serious_warning_proxy"
    if row["Beff"] >= warn_Beff:
        return "watch_proxy"
    return "healthy_proxy"


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument("--candidate-csv", default="gate1_surrogate_best_candidates.csv")
    p.add_argument("--zones", type=float, nargs="*", default=[])
    p.add_argument("--top", type=int, default=8)
    p.add_argument("--merge-distance", type=float, default=5.0)

    p.add_argument("--zero-radius", type=float, default=55.0)
    p.add_argument("--scan-radius", type=float, default=35.0)
    p.add_argument("--zero-step", type=float, default=0.1)
    p.add_argument("--mp-dps", type=int, default=30)
    p.add_argument("--cache-dir", default="zero_proxy_cache")
    p.add_argument("--force-zero-rescan", action="store_true")

    p.add_argument("--cI", type=float, nargs="+", default=[0.1, 0.2, 0.5, 1.0])
    p.add_argument("--kappa", type=float, default=0.5)
    p.add_argument("--W", type=float, default=40.0)
    p.add_argument("--grid", type=int, default=401)

    p.add_argument("--R", type=int, default=4)
    p.add_argument("--jet-h-factor", type=float, default=0.015)
    p.add_argument("--jet-fit-points", type=int, default=31)

    p.add_argument("--random-count", type=int, default=80)
    p.add_argument("--uniform-count", type=int, default=120)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--no-gram", action="store_true")

    p.add_argument("--stability-W", type=float, nargs="+", default=[10.0, 20.0, 40.0])
    p.add_argument("--stability-kappa", type=float, nargs="+", default=[0.25, 0.5, 1.0])

    p.add_argument("--out", default="gate1_actual_zero_proxy_zone_scan.csv")
    p.add_argument("--summary-out", default="gate1_actual_zero_proxy_zone_summary.csv")

    return p.parse_args()


def main():
    args = parse_args()
    zones = load_zones(args)

    if not zones:
        raise RuntimeError("No zones supplied. Use --candidate-csv or --zones.")

    print(f"Scanning {len(zones)} zones:")
    for z in zones:
        print(f"  {z:.6f}")

    all_rows = []
    metas = []

    for i, zone in enumerate(zones, start=1):
        print(f"\n[{i}/{len(zones)}] Zone {zone:.6f}")
        df_zone, meta = scan_zone(zone, args)
        metas.append(meta)
        all_rows.append(df_zone)

        if not df_zone.empty:
            best = df_zone.sort_values("E").head(5)
            print(best[["family", "center", "cI", "E", "S", "Beff", "J_max", "tail_drift", "reg_drift"]].to_string(index=False))

    df = pd.concat(all_rows, ignore_index=True) if all_rows else pd.DataFrame()
    if not df.empty:
        df["classification"] = df.apply(classify_row, axis=1)

    summary = summarize_results(df)
    if not summary.empty:
        summary["classification"] = summary.apply(classify_row, axis=1)

    df.to_csv(args.out, index=False)
    summary.to_csv(args.summary_out, index=False)

    print("\nWrote:")
    print(f"  {args.out}")
    print(f"  {args.summary_out}")

    print("\nBest overall rows:")
    if not df.empty:
        print(df.sort_values("E").head(20)[
            ["zone", "family", "center", "cI", "E", "S", "Beff", "J_max", "tail_drift", "reg_drift", "classification"]
        ].to_string(index=False))

    print("\nZone metadata:")
    print(pd.DataFrame(metas).to_string(index=False))


if __name__ == "__main__":
    main()
