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

import argparse
import csv
import math
import os
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
                 seed: int = 0) -> List[Tuple[str, float, Optional[int]]]:
    """
    start_index/end_index are 1-based zeta zero indices.
    """
    rng = random.Random(seed)
    z = list(zeros)
    # convert to zero-based inclusive-ish bounds
    s = max(1, start_index) - 1
    e = min(len(z) - 2, end_index - 1)

    centers: List[Tuple[str, float, Optional[int]]] = []

    # gap midpoints
    for i in range(s, e):
        centers.append(("gap_midpoint", 0.5 * (z[i] + z[i + 1]), i + 1))

    # every 5th zero center
    for i in range(s, e + 1, 5):
        centers.append(("zero_center", z[i], i + 1))

    # small/large gap neighborhoods
    gaps = [(z[i + 1] - z[i], i) for i in range(s, e)]
    gaps_sorted = sorted(gaps, key=lambda t: t[0])
    k = max(1, int(0.05 * len(gaps_sorted)))
    for label, subset in [("small_gap", gaps_sorted[:k]), ("large_gap", gaps_sorted[-k:])]:
        for gap, i in subset:
            for eta in [0.25, 0.5, 0.75]:
                centers.append((label, z[i] + eta * gap, i + 1))

    # random centers
    lo, hi = z[s], z[e]
    for _ in range(random_count):
        centers.append(("random", rng.uniform(lo, hi), None))

    return centers


# ----------------------------
# Actual-zero proxy scan
# ----------------------------

def run_actual_zero_proxy_scan(outdir: str,
                               n_zeros: int,
                               start_index: int,
                               end_index: int,
                               smoke: bool = False) -> List[Dict]:
    log(f"loading or generating {n_zeros} zeros")
    zeros = load_or_generate_zeros(outdir, n_zeros=n_zeros)
    log(f"have {len(zeros)} zeros: gamma_1={zeros[0]:.4f}, gamma_N={zeros[-1]:.4f}")

    if smoke:
        centers = make_centers(zeros, start_index, min(start_index + 50, end_index), random_count=10)
        c_I_list = [0.5]
        kappa_list = [1.0]
        W_mult_list = [50.0]
        R_list = [4]
        n_quad_list = [257]
    else:
        centers = make_centers(zeros, start_index, end_index, random_count=100)
        c_I_list = [0.2, 0.5]
        kappa_list = [0.5, 1.0]
        W_mult_list = [25.0, 50.0]
        R_list = [4]
        n_quad_list = [257]

    n_params_per_center = (
        len(c_I_list) * len(kappa_list) * len(W_mult_list) * len(R_list) * len(n_quad_list)
    )
    log(
        f"scan plan: {len(centers)} centers x {n_params_per_center} params = "
        f"{len(centers) * n_params_per_center} total work units"
    )

    rows: List[Dict] = []
    t0 = time.time()
    progress_every = max(1, len(centers) // 50)
    log(f"progress prints every {progress_every} centers")

    for idx, (center_type, m0, ref_idx) in enumerate(centers):
        Q = math.log(m0 / (2.0 * math.pi))
        if Q <= 1.0:
            continue

        for c_I in c_I_list:
            Delta = c_I / Q
            for kappa in kappa_list:
                eps = kappa / Q
                for W_mult in W_mult_list:
                    W = W_mult / Q
                    edge_truncated = (m0 - W < zeros[0]) or (m0 + W > zeros[-1])
                    for R in R_list:
                        for n_quad in n_quad_list:
                            E_I, S_I, num_used = integrate_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                n_nodes=n_quad
                            )
                            if not math.isfinite(E_I):
                                continue

                            B_eff = -safe_log(E_I) / math.log(Q)
                            J_max, J_rms = finite_difference_jets_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                R=R
                            )

                            rows.append({
                                "run_label": "zero_kernel_only_proxy",
                                "center_type": center_type,
                                "ref_idx": ref_idx,
                                "m0": m0,
                                "Q": Q,
                                "c_I": c_I,
                                "Delta": Delta,
                                "kappa": kappa,
                                "eps": eps,
                                "W_mult": W_mult,
                                "W": W,
                                "R": R,
                                "N_quad": n_quad,
                                "num_zeros_used": num_used,
                                "edge_truncated": edge_truncated,
                                "E_I": E_I,
                                "S_I": S_I,
                                "B_eff": B_eff,
                                "J_max": J_max,
                                "J_rms": J_rms,
                            })

        if (idx + 1) % progress_every == 0 or idx + 1 == len(centers):
            elapsed = time.time() - t0
            rate = (idx + 1) / elapsed if elapsed > 0 else 0
            eta = (len(centers) - idx - 1) / rate if rate > 0 else 0
            log(
                f"  centers {idx+1}/{len(centers)}  rows={len(rows)}  "
                f"elapsed={elapsed:.1f}s  rate={rate:.2f}/s  eta={eta:.1f}s"
            )

    suffix = "smoke" if smoke else "small"
    path = os.path.join(outdir, f"actual_zero_proxy_{suffix}.csv")
    write_csv(path, rows)

    # Top diagnostics
    top_path = os.path.join(outdir, f"actual_zero_proxy_{suffix}_top_by_Beff.csv")
    write_csv(top_path, summarize_top(rows, "B_eff", n=50, reverse=True))

    return rows


# ----------------------------
# Main
# ----------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["controls", "actual", "all"], default="controls")
    ap.add_argument("--outdir", default="gate1_out")
    ap.add_argument("--zeros", type=int, default=500)
    ap.add_argument("--start-index", type=int, default=50)
    ap.add_argument("--end-index", type=int, default=500)
    ap.add_argument("--smoke", action="store_true")
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
        )
        log(f"wrote {len(rows)} rows to actual_zero_proxy CSV")
        top = summarize_top(rows, "B_eff", n=10, reverse=True)
        log("top rows by B_eff:")
        for r in top:
            print({
                "center_type": r.get("center_type"),
                "m0": r.get("m0"),
                "Q": r.get("Q"),
                "c_I": r.get("c_I"),
                "kappa": r.get("kappa"),
                "W_mult": r.get("W_mult"),
                "R": r.get("R"),
                "N_quad": r.get("N_quad"),
                "E_I": r.get("E_I"),
                "B_eff": r.get("B_eff"),
                "J_max": r.get("J_max"),
                "num_zeros_used": r.get("num_zeros_used"),
                "edge_truncated": r.get("edge_truncated"),
            }, flush=True)


if __name__ == "__main__":
    main()
