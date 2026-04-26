#!/usr/bin/env python3
"""
Gate 1 numerical controls:
1. Deterministic same-scale quadrature negative control.
2. Random positive packet comparison.
3. Singular/shallow packet dominance and cancellation controls.

Run:
    python gate1_controls.py

Optional:
    python gate1_controls.py --fast
    python gate1_controls.py --out gate1_controls_results.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable

# Pin BLAS / OpenMP to 1 thread per process (unified gate1 convention).
# Set before numpy import.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")

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


# ----------------------------
# Shared normalized packet model
# ----------------------------

def build_sine_quadrature(R: int, N: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    """
    Deterministic positive same-scale quadrature.

    theta_j = j*pi/(N+1), j=1..N
    w_j = 2/(N+1) sin(theta_j)

    Then sum_j w_j sin(k theta_j) = delta_{k1}, 1 <= k <= N.
    Need N >= R+3 to kill F^(r)(0), r=0..R, where F=Q''.
    """
    if N is None:
        N = R + 3
    if N < R + 3:
        raise ValueError(f"Need N >= R+3; got N={N}, R={R}")

    j = np.arange(1, N + 1, dtype=np.float64)
    theta = j * math.pi / (N + 1)
    weights = (2.0 / (N + 1)) * np.sin(theta)
    return theta, weights


def build_random_positive_cluster(
    N: int,
    seed: int,
    theta_min: float = 0.05 * math.pi,
    theta_max: float = 0.95 * math.pi,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Random positive packet cluster, normalized by sum_j w_j sin(theta_j)=1.
    """
    rng = np.random.default_rng(seed)
    theta = np.sort(rng.uniform(theta_min, theta_max, size=N))
    raw = rng.exponential(scale=1.0, size=N)
    weights = raw / np.sum(raw * np.sin(theta))
    return theta, weights


def moments(theta: np.ndarray, weights: np.ndarray, ks: Iterable[int]) -> np.ndarray:
    return np.array([np.sum(weights * np.sin(k * theta)) for k in ks], dtype=np.float64)


def K(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    K_theta(x) = sin(theta) / ((x-cos(theta))^2 + sin(theta)^2)

    Vectorized:
      theta shape: (N,)
      x shape: (M,)
      returns shape: (M,N)
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    return s / ((xx - c) ** 2 + s ** 2)


def K_second(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Analytic second derivative of K_theta(x).

    K = s / ((x-c)^2 + s^2)
    K'' = s * (6(x-c)^2 - 2s^2) / ((x-c)^2+s^2)^3
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y * y + s * s
    return s * (6.0 * y * y - 2.0 * s * s) / (den ** 3)


def K_fourth(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Analytic fourth derivative of K_theta(x).

    Let y=x-c, a=s. For K=a/(y^2+a^2):
    K'''' = 24*a*(16*y^4 - 12*a^2*y^2 + a^4) / (y^2+a^2)^5
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y * y + s * s
    numerator = 24.0 * s * (16.0 * y**4 - 12.0 * s**2 * y**2 + s**4)
    return numerator / (den**5)


def eval_Q(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    return K(theta, x) @ weights


def eval_F(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    """F(x)=Q''(x)."""
    return K_second(theta, x) @ weights


def eval_Q4(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Q^{(4)}(x)."""
    return K_fourth(theta, x) @ weights


def compute_E_and_S(
    theta: np.ndarray,
    weights: np.ndarray,
    X0: float,
    nquad: int = 256,
    ngrid: int = 2001,
) -> tuple[float, float]:
    """
    E_X = |X|^{-1} int_X |F(x)|^2 dx, X=[-X0,X0]
    S_X = sup_X |F(x)| approximated on a dense grid.
    """
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts
    F_vals = eval_F(theta, weights, xs)
    E_X = float(np.sum(ws * F_vals * F_vals) / (2.0 * X0))

    grid = np.linspace(-X0, X0, ngrid)
    S_X = float(np.max(np.abs(eval_F(theta, weights, grid))))
    return E_X, S_X


@dataclass
class NegativeControlRow:
    R: int
    N: int
    X0: float
    mu1_error: float
    killed_moment_max: float
    normalized_jet_max: float
    E_X: float
    S_X: float
    random_E_median: float
    ratio_to_random: float


def run_negative_control_case(
    R: int,
    X0: float,
    nquad: int,
    ngrid: int,
    n_random: int,
) -> NegativeControlRow:
    theta, weights = build_sine_quadrature(R)
    N = len(theta)

    mu1_error = abs(float(np.sum(weights * np.sin(theta))) - 1.0)

    ks = range(3, R + 4)
    killed_moment_max = float(np.max(np.abs(moments(theta, weights, ks))))
    normalized_jet_max = killed_moment_max  # F^(r)(0)/(r+2)! = moment k=r+3

    E_X, S_X = compute_E_and_S(theta, weights, X0, nquad=nquad, ngrid=ngrid)

    random_Es = []
    for seed in range(n_random):
        th_r, w_r = build_random_positive_cluster(N, seed=10_000 + 997 * R + 31 * seed)
        E_r, _ = compute_E_and_S(th_r, w_r, X0, nquad=max(64, nquad // 2), ngrid=max(501, ngrid // 4))
        random_Es.append(E_r)

    random_E_median = float(np.median(random_Es))
    ratio_to_random = float(E_X / random_E_median) if random_E_median > 0 else float("nan")

    return NegativeControlRow(
        R=R,
        N=N,
        X0=X0,
        mu1_error=mu1_error,
        killed_moment_max=killed_moment_max,
        normalized_jet_max=normalized_jet_max,
        E_X=E_X,
        S_X=S_X,
        random_E_median=random_E_median,
        ratio_to_random=ratio_to_random,
    )


# ----------------------------
# Singular controls
# ----------------------------

@dataclass
class SingularRow:
    label: str
    c: float
    X0: float
    E_u_norm: float
    E_u_physical: float
    gate2_norm: float
    gate2_physical: float
    S_u_norm: float
    S_gammaG_norm: float
    S_gammaG2_norm: float


def compute_singular_diagnostics(
    theta: np.ndarray,
    weights: np.ndarray,
    c_scale: float,
    X0: float,
    label: str,
    nquad: int = 256,
    ngrid: int = 2001,
) -> SingularRow:
    """
    Normalized model:
      q(m)=c^{-1} Q(x)
      u=q''=c^{-3} Q''(x)
      q^(4)=c^{-5} Q^(4)(x)

    Physical dm = c dx. Physical interval length = c |X|.
    Mean physical E_u = |I|^{-1} int |u|^2 dm = c^{-6} * mean_X |Q''|^2.

    Gate2 physical mean:
      |I|^{-1} int |u|^2 (GammaG^2+GammaG2^2) dm
    computed directly from scaled quantities.
    """
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts

    Q = eval_Q(theta, weights, xs)
    Q2 = eval_F(theta, weights, xs)
    Q4 = eval_Q4(theta, weights, xs)

    q = c_scale ** -1 * Q
    u = c_scale ** -3 * Q2
    q4 = c_scale ** -5 * Q4

    gammaG = u - 6.0 * q + 2.0 * q**3
    gammaG2 = (1.0 - q**2) * u - (1.0 / 6.0) * q4

    E_u_physical = float(np.sum(ws * u * u) / (2.0 * X0))
    gate2_physical = float(np.sum(ws * (u * u) * (gammaG * gammaG + gammaG2 * gammaG2)) / (2.0 * X0))

    # Normalized diagnostics:
    # E_u_norm = mean_X |Q''|^2
    E_u_norm = float(np.sum(ws * Q2 * Q2) / (2.0 * X0))

    # Gate2 normalized by dominant singular c^{-16} factor:
    # integrand dominated by u^2 * gammaG2^2 ~ c^{-16}, so multiply by c^16.
    gate2_norm = gate2_physical * (c_scale ** 16)

    grid = np.linspace(-X0, X0, ngrid)
    Qg = eval_Q(theta, weights, grid)
    Q2g = eval_F(theta, weights, grid)
    Q4g = eval_Q4(theta, weights, grid)

    qg = c_scale ** -1 * Qg
    ug = c_scale ** -3 * Q2g
    q4g = c_scale ** -5 * Q4g
    gammaGg = ug - 6.0 * qg + 2.0 * qg**3
    gammaG2g = (1.0 - qg**2) * ug - (1.0 / 6.0) * q4g

    return SingularRow(
        label=label,
        c=c_scale,
        X0=X0,
        E_u_norm=E_u_norm,
        E_u_physical=E_u_physical,
        gate2_norm=gate2_norm,
        gate2_physical=gate2_physical,
        S_u_norm=float(np.max(np.abs(Q2g))),
        S_gammaG_norm=float(np.max(np.abs(gammaGg * c_scale**3))),   # rough c^3-normalization
        S_gammaG2_norm=float(np.max(np.abs(gammaG2g * c_scale**5))), # rough c^5-normalization
    )


def build_single_packet() -> tuple[np.ndarray, np.ndarray]:
    """
    Single centered packet Q(x)=1/(1+x^2), represented as theta=pi/2.
    """
    return np.array([math.pi / 2.0]), np.array([1.0])


def run_singular_controls(
    c_values: list[float],
    X0: float,
    R_cancel: int,
    nquad: int,
    ngrid: int,
) -> list[SingularRow]:
    rows = []

    th_single, w_single = build_single_packet()
    th_cancel, w_cancel = build_sine_quadrature(R_cancel)
    th_random, w_random = build_random_positive_cluster(R_cancel + 3, seed=424242)

    for c in c_values:
        rows.append(compute_singular_diagnostics(th_single, w_single, c, X0, "single", nquad, ngrid))
        rows.append(compute_singular_diagnostics(th_random, w_random, c, X0, "random_cluster", nquad, ngrid))
        rows.append(compute_singular_diagnostics(th_cancel, w_cancel, c, X0, "quadrature_cancelled", nquad, ngrid))

    return rows


# ----------------------------
# Reporting
# ----------------------------

def sci(x: float) -> str:
    return f"{x:.6e}"


def print_negative_rows(rows: list[NegativeControlRow]) -> None:
    print("\n=== Deterministic same-scale quadrature negative control ===")
    header = [
        "R", "N", "X0", "mu1_err", "killed_moment_max",
        "E_X", "S_X", "random_E_med", "ratio"
    ]
    print(",".join(header))
    for r in rows:
        print(",".join([
            str(r.R),
            str(r.N),
            f"{r.X0:.2f}",
            sci(r.mu1_error),
            sci(r.killed_moment_max),
            sci(r.E_X),
            sci(r.S_X),
            sci(r.random_E_median),
            sci(r.ratio_to_random),
        ]))


def print_singular_rows(rows: list[SingularRow]) -> None:
    print("\n=== Singular/shallow packet controls ===")
    header = [
        "label", "c", "X0", "E_u_norm", "E_u_physical",
        "gate2_norm", "gate2_physical", "S_u_norm",
        "S_gammaG_norm", "S_gammaG2_norm"
    ]
    print(",".join(header))
    for r in rows:
        print(",".join([
            r.label,
            sci(r.c),
            f"{r.X0:.2f}",
            sci(r.E_u_norm),
            sci(r.E_u_physical),
            sci(r.gate2_norm),
            sci(r.gate2_physical),
            sci(r.S_u_norm),
            sci(r.S_gammaG_norm),
            sci(r.S_gammaG2_norm),
        ]))


def write_csv(path: str, neg_rows: list[NegativeControlRow], sing_rows: list[SingularRow]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["section", "R", "N", "X0", "mu1_error", "killed_moment_max",
                         "normalized_jet_max", "E_X", "S_X", "random_E_median", "ratio_to_random"])
        for r in neg_rows:
            writer.writerow([
                "negative_control", r.R, r.N, r.X0, r.mu1_error, r.killed_moment_max,
                r.normalized_jet_max, r.E_X, r.S_X, r.random_E_median, r.ratio_to_random
            ])

        writer.writerow([])
        writer.writerow(["section", "label", "c", "X0", "E_u_norm", "E_u_physical",
                         "gate2_norm", "gate2_physical", "S_u_norm",
                         "S_gammaG_norm", "S_gammaG2_norm"])
        for r in sing_rows:
            writer.writerow([
                "singular_control", r.label, r.c, r.X0, r.E_u_norm, r.E_u_physical,
                r.gate2_norm, r.gate2_physical, r.S_u_norm,
                r.S_gammaG_norm, r.S_gammaG2_norm
            ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="Run a faster reduced test suite.")
    parser.add_argument("--out", type=str,
                        default=_default_out("gate1_controls_results.csv"),
                        help="CSV output path. Default lands in <script>/out/. "
                             "Pass an empty string to skip writing.")
    args = parser.parse_args()

    if args.fast:
        neg_cases = [(12, 0.5), (24, 0.5)]
        nquad = 128
        ngrid = 801
        n_random = 5
        singular_c_values = [1e-2, 1e-3]
    else:
        neg_cases = [
            (12, 0.25), (12, 0.5), (12, 0.75),
            (24, 0.25), (24, 0.5), (24, 0.75),
            (40, 0.25), (40, 0.5), (40, 0.75),
        ]
        nquad = 256
        ngrid = 2001
        n_random = 20
        singular_c_values = [1e-2, 1e-3, 1e-4]

    neg_rows = [
        run_negative_control_case(R, X0, nquad=nquad, ngrid=ngrid, n_random=n_random)
        for R, X0 in neg_cases
    ]

    sing_rows = run_singular_controls(
        c_values=singular_c_values,
        X0=0.5,
        R_cancel=24,
        nquad=nquad,
        ngrid=ngrid,
    )

    print_negative_rows(neg_rows)
    print_singular_rows(sing_rows)

    if args.out:
        out_parent = os.path.dirname(os.path.abspath(args.out))
        if out_parent:
            os.makedirs(out_parent, exist_ok=True)
        write_csv(args.out, neg_rows, sing_rows)
        log(f"Wrote CSV: {args.out}")


if __name__ == "__main__":
    main()
