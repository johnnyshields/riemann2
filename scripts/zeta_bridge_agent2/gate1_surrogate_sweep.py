#!/usr/bin/env python3
"""
Gate 1 surrogate reoptimization sweep.

Purpose:
  For each cutoff/smoothing model, re-optimize the source-flat objective instead
  of evaluating only one fixed candidate. This tests whether source-flat
  candidates are robust across surrogate choices or model-specific artifacts.

Dependencies:
  pip install numpy scipy mpmath pandas

Outputs:
  - gate1_surrogate_sweep_results.csv
  - gate1_surrogate_best_candidates.csv
  - optional actual-zero proxy rows if --actual-zero-proxy is used
"""

import argparse
import math
import os
import warnings
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Dict, List, Tuple

# Pin BLAS / OpenMP to 1 thread per process (unified gate1 convention).
# Set before numpy import.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.signal import argrelextrema


def log(msg: str) -> None:
    """Timestamped, flushed line. Unified logging helper across the gate1 scripts."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))


def _default_out(*parts: str) -> str:
    """Resolve <script_dir>/out/<parts...>; unified outputs location."""
    return os.path.join(_DEFAULT_OUT_DIR, *parts)

try:
    import mpmath as mp
except Exception:
    mp = None


# -----------------------------
# Basic arithmetic helpers
# -----------------------------

def von_mangoldt_values(N: int) -> np.ndarray:
    """
    Lambda(n) for n <= N using a simple sieve-like prime-power pass.
    """
    lam = np.zeros(N + 1, dtype=float)
    is_prime = np.ones(N + 1, dtype=bool)
    is_prime[:2] = False

    for p in range(2, N + 1):
        if is_prime[p]:
            for k in range(p * p, N + 1, p):
                is_prime[k] = False
            pk = p
            while pk <= N:
                lam[pk] = math.log(p)
                pk *= p
    return lam


def smoothing_weights(n: np.ndarray, N: int, mode: str) -> np.ndarray:
    x = n / float(N)
    if mode == "exp":
        return np.exp(-x)
    if mode == "cos":
        w = np.zeros_like(x, dtype=float)
        mask = x <= 1
        w[mask] = 0.5 * (1 + np.cos(np.pi * x[mask]))
        return w
    if mode == "sharp":
        return (x <= 1).astype(float)
    raise ValueError(f"unknown smoothing mode: {mode}")


@dataclass
class SurrogateModel:
    N: int
    smoothing: str
    level: int
    n: np.ndarray
    logn: np.ndarray
    coeff_main: np.ndarray
    coeff_dual: np.ndarray
    norm: float

    def source_value(self, t: float) -> float:
        """
        Surrogate q''_can(t) approximation.
        Level 1: main only
        Level 2: main + dual-like
        Level 3: main + dual-like + smooth background
        """
        phase = np.exp(-1j * t * self.logn)
        main = np.real(np.sum(self.coeff_main * phase))

        val = main

        if self.level >= 2:
            # A crude chi-like dual surrogate. Not a real AFE; meant for robustness testing.
            # Deterministic slowly varying phase/amplitude.
            chi_phase = np.exp(1j * (0.5 * t * np.log(max(t, 2.0) / (2 * np.pi)) - 0.5 * t))
            dual = np.real(chi_phase * np.sum(self.coeff_dual * np.conj(phase)))
            val += 0.65 * dual

        if self.level >= 3:
            # Smooth background proxy. Small and slowly varying.
            val += 0.04 * math.sin(0.7 * math.log(max(t, 2.0))) + 0.02 * math.cos(0.17 * t)

        return val / self.norm

    def derivative_value(self, t: float, r: int) -> float:
        """
        r-th t derivative of surrogate source q''_can(t), normalized.
        """
        phase = np.exp(-1j * t * self.logn)
        main = np.real(np.sum(self.coeff_main * ((-1j * self.logn) ** r) * phase))
        val = main

        if self.level >= 2:
            chi_phase = np.exp(1j * (0.5 * t * np.log(max(t, 2.0) / (2 * np.pi)) - 0.5 * t))
            # Approximate derivative: differentiate phase terms, ignore chi derivatives for this pilot.
            dual = np.real(chi_phase * np.sum(self.coeff_dual * ((1j * self.logn) ** r) * np.conj(phase)))
            val += 0.65 * dual

        if self.level >= 3:
            # Derivatives of smooth background up to a few orders; beyond that negligible for pilot.
            if r == 0:
                bg = 0.04 * math.sin(0.7 * math.log(max(t, 2.0))) + 0.02 * math.cos(0.17 * t)
            elif r == 1:
                bg = 0.04 * 0.7 * math.cos(0.7 * math.log(max(t, 2.0))) / max(t, 2.0) - 0.02 * 0.17 * math.sin(0.17 * t)
            else:
                bg = 0.02 * (0.17 ** r) * math.cos(0.17 * t + r * math.pi / 2)
            val += bg

        return val / self.norm

    def source_jets(self, t: float, R: int) -> np.ndarray:
        Q = math.log(t / (2.0 * math.pi))
        Delta = 1.0 / Q
        return np.array([(Delta ** r) * self.derivative_value(t, r) for r in range(R + 1)])

    def source_objective(self, t: float, R: int) -> float:
        jets = self.source_jets(t, R)
        return float(np.sum(jets ** 2))

    def interval_energy(self, t0: float, cI: float = 0.5, grid: int = 401) -> Tuple[float, float, float]:
        Q = math.log(t0 / (2.0 * math.pi))
        half = cI / Q
        xs = np.linspace(t0 - half, t0 + half, grid)
        vals = np.array([self.source_value(float(x)) for x in xs])
        E = float(np.trapz(vals ** 2, xs) / (2 * half))
        S = float(np.max(np.abs(vals)))
        Beff = -math.log(max(E, 1e-300)) / math.log(Q)
        return E, S, Beff


def make_model(N: int, smoothing: str, level: int) -> SurrogateModel:
    lam = von_mangoldt_values(N)
    n = np.arange(2, N + 1, dtype=float)
    logn = np.log(n)
    lamn = lam[2:]

    W = smoothing_weights(n, N, smoothing)

    # Source-curvature-like weights: Lambda(n) * (log n)^2 * n^-1/2 * W.
    coeff_main = lamn * (logn ** 2) * (n ** -0.5) * W

    # Dual-like weights: reverse-ish smoothing with lower log power for diversity.
    W_dual = smoothing_weights(n, N, "cos" if smoothing != "cos" else "exp")
    coeff_dual = lamn * (logn ** 2) * (n ** -0.5) * W_dual

    # Normalize RMS over a modest sample grid so objectives compare across cutoffs.
    sample_ts = np.linspace(100.0, 800.0, 256)
    raw_vals = []
    for t in sample_ts:
        phase = np.exp(-1j * t * logn)
        raw_vals.append(np.real(np.sum(coeff_main * phase)))
    norm = float(np.sqrt(np.mean(np.array(raw_vals) ** 2)))
    norm = max(norm, 1e-12)

    return SurrogateModel(
        N=N,
        smoothing=smoothing,
        level=level,
        n=n,
        logn=logn,
        coeff_main=coeff_main,
        coeff_dual=coeff_dual,
        norm=norm,
    )


# -----------------------------
# Search
# -----------------------------

def find_local_minima_candidates(
    model: SurrogateModel,
    R: int,
    t_min: float,
    t_max: float,
    coarse_points: int,
    keep: int,
) -> List[Tuple[float, float]]:
    ts = np.linspace(t_min, t_max, coarse_points)
    vals = np.array([model.source_objective(float(t), R) for t in ts])

    # Get local minima indices, plus global best fallback.
    loc_idx = argrelextrema(vals, np.less, order=2)[0].tolist()
    loc_idx.append(int(np.argmin(vals)))
    loc_idx = sorted(set(loc_idx), key=lambda i: vals[i])[:keep]

    candidates = []
    step = (t_max - t_min) / (coarse_points - 1)

    for i in loc_idx:
        lo = max(t_min, ts[i] - 2 * step)
        hi = min(t_max, ts[i] + 2 * step)

        res = minimize_scalar(lambda x: model.source_objective(float(x), R), bounds=(lo, hi), method="bounded")
        candidates.append((float(res.x), float(res.fun)))

    candidates = sorted(candidates, key=lambda x: x[1])
    return candidates[:keep]


def run_surrogate_sweep(args) -> Tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    best_rows = []

    for N in args.cutoffs:
        for smoothing in args.smoothing:
            for level in args.levels:
                model = make_model(N=N, smoothing=smoothing, level=level)

                candidates = find_local_minima_candidates(
                    model=model,
                    R=args.R,
                    t_min=args.t_min,
                    t_max=args.t_max,
                    coarse_points=args.coarse_points,
                    keep=args.keep_candidates,
                )

                for rank, (t0, obj) in enumerate(candidates, start=1):
                    jets = model.source_jets(t0, args.R)
                    jmax = float(np.max(np.abs(jets)))

                    width_results = {}
                    for cI in args.widths:
                        E, S, Beff = model.interval_energy(t0, cI=cI, grid=args.interval_grid)
                        width_results[f"E_cI_{cI}"] = E
                        width_results[f"S_cI_{cI}"] = S
                        width_results[f"Beff_cI_{cI}"] = Beff

                    row = {
                        "N": N,
                        "smoothing": smoothing,
                        "level": level,
                        "R": args.R,
                        "rank": rank,
                        "t0": t0,
                        "source_objective": obj,
                        "J_max": jmax,
                        **width_results,
                    }
                    rows.append(row)

                if candidates:
                    t0, obj = candidates[0]
                    E, S, Beff = model.interval_energy(t0, cI=0.5, grid=args.interval_grid)
                    best_rows.append({
                        "N": N,
                        "smoothing": smoothing,
                        "level": level,
                        "R": args.R,
                        "best_t0": t0,
                        "best_objective": obj,
                        "E_cI_0.5": E,
                        "S_cI_0.5": S,
                        "Beff_cI_0.5": Beff,
                        "J_max": float(np.max(np.abs(model.source_jets(t0, args.R)))),
                    })

    return pd.DataFrame(rows), pd.DataFrame(best_rows)


# -----------------------------
# Optional actual-zero proxy cross-check
# -----------------------------

def hardy_z_zeros_near(t0: float, radius: float, step: float = 0.1, mp_dps: int = 30) -> np.ndarray:
    if mp is None:
        raise RuntimeError("mpmath not installed")
    mp.mp.dps = mp_dps

    def zval(x):
        return float(mp.siegelz(x))

    xs = np.arange(t0 - radius, t0 + radius + step, step)
    zs = []
    vals = []

    prev_x = xs[0]
    prev_v = zval(prev_x)

    for x in xs[1:]:
        v = zval(float(x))
        if prev_v == 0:
            zs.append(prev_x)
        elif v == 0 or prev_v * v < 0:
            # Linear interpolation is enough for proxy; not certified.
            root = prev_x + (float(x) - prev_x) * abs(prev_v) / (abs(prev_v) + abs(v))
            zs.append(root)
        prev_x, prev_v = float(x), v

    return np.array(zs, dtype=float)


def K2_proxy(m: np.ndarray, gamma: float, eps: float) -> np.ndarray:
    x = m - gamma
    den = x*x + eps*eps
    return 2 * eps * (3*x*x - eps*eps) / den**3


def zero_proxy_energy(t0: float, zeros: np.ndarray, cI: float = 0.5, kappa: float = 0.5, W: float = 40.0, grid: int = 401):
    Q = math.log(t0 / (2.0 * math.pi))
    eps = kappa / Q
    half = cI / Q
    xs = np.linspace(t0 - half, t0 + half, grid)

    use = zeros[np.abs(zeros - t0) <= W]
    vals = np.zeros_like(xs)
    for g in use:
        vals += K2_proxy(xs, g, eps)

    E = float(np.trapz(vals**2, xs) / (2 * half))
    S = float(np.max(np.abs(vals)))
    Beff = -math.log(max(E, 1e-300)) / math.log(Q)

    return {
        "zero_proxy_E": E,
        "zero_proxy_S": S,
        "zero_proxy_Beff": Beff,
        "zero_proxy_zeros_used": len(use),
    }


def run_actual_zero_proxy_for_best(best_df: pd.DataFrame, args) -> pd.DataFrame:
    rows = []
    for _, row in best_df.head(args.proxy_best_count).iterrows():
        t0 = float(row["best_t0"])
        try:
            zeros = hardy_z_zeros_near(t0, radius=args.proxy_radius, step=args.proxy_step, mp_dps=args.mp_dps)
            zp = zero_proxy_energy(t0, zeros, cI=0.5, kappa=0.5, W=min(40.0, args.proxy_radius), grid=401)
            rows.append({
                **row.to_dict(),
                "proxy_zero_count": len(zeros),
                "proxy_zero_min": float(np.min(zeros)) if len(zeros) else np.nan,
                "proxy_zero_max": float(np.max(zeros)) if len(zeros) else np.nan,
                **zp,
            })
        except Exception as e:
            rows.append({
                **row.to_dict(),
                "proxy_error": repr(e),
            })
    return pd.DataFrame(rows)


# -----------------------------
# Main
# -----------------------------

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--t-min", type=float, default=80.0)
    p.add_argument("--t-max", type=float, default=4000.0)
    p.add_argument("--coarse-points", type=int, default=4000)
    p.add_argument("--keep-candidates", type=int, default=3)
    p.add_argument("--R", type=int, default=8)
    p.add_argument("--cutoffs", type=int, nargs="+", default=[200, 350, 500, 800])
    p.add_argument("--smoothing", nargs="+", default=["exp", "cos", "sharp"])
    p.add_argument("--levels", type=int, nargs="+", default=[1, 2, 3])
    p.add_argument("--widths", type=float, nargs="+", default=[0.1, 0.2, 0.5, 1.0])
    p.add_argument("--interval-grid", type=int, default=401)

    p.add_argument("--actual-zero-proxy", action="store_true")
    p.add_argument("--proxy-best-count", type=int, default=6)
    p.add_argument("--proxy-radius", type=float, default=45.0)
    p.add_argument("--proxy-step", type=float, default=0.1)
    p.add_argument("--mp-dps", type=int, default=30)

    args = p.parse_args()

    # Q = log(t / (2π)) is used as the canonical scale; B_eff = -log(E)/log(Q)
    # would blow up or sign-flip when Q ≤ 1, i.e. t ≤ 2π·e ≈ 17.08. Reject up
    # front rather than emit NaNs deep in the sweep.
    _Q1_THRESHOLD = 2.0 * math.pi * math.e
    if args.t_min <= _Q1_THRESHOLD:
        p.error(
            f"--t-min must exceed 2π·e ≈ {_Q1_THRESHOLD:.4f} so that Q = log(t/(2π)) > 1; "
            f"got {args.t_min}"
        )

    return args


def main():
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    args = parse_args()

    log("Running surrogate sweep...")
    all_df, best_df = run_surrogate_sweep(args)

    os.makedirs(_DEFAULT_OUT_DIR, exist_ok=True)
    sweep_path = _default_out("gate1_surrogate_sweep_results.csv")
    best_path = _default_out("gate1_surrogate_best_candidates.csv")
    crosscheck_path = _default_out("gate1_surrogate_actual_zero_proxy_crosscheck.csv")

    all_df.to_csv(sweep_path, index=False)
    best_df.to_csv(best_path, index=False)

    log("Best candidates by model:")
    print(best_df.sort_values("best_objective").head(20).to_string(index=False), flush=True)

    if args.actual_zero_proxy:
        log("Running optional actual-zero proxy cross-checks for best candidates...")
        proxy_df = run_actual_zero_proxy_for_best(best_df.sort_values("best_objective"), args)
        proxy_df.to_csv(crosscheck_path, index=False)
        print(proxy_df.head(args.proxy_best_count).to_string(index=False), flush=True)

    log("Wrote:")
    log(f"  {sweep_path}")
    log(f"  {best_path}")
    if args.actual_zero_proxy:
        log(f"  {crosscheck_path}")


if __name__ == "__main__":
    main()
