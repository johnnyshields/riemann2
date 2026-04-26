#!/usr/bin/env python3
"""
afe_logderiv_weights.py

Shared log-derivative / phase-consistent AFE weight helpers. Used by the
packet-frequency determinant stress test (agent_b5) and any other agent
that needs the same convention.

Convention (canonical handoff, Agent 4 / Agent 6 audit):

    A(s) = - zeta'(s) / zeta(s)
    C_k(s) = (-1)^k d_s^k A(s)

Main branch coefficient:
    Lambda(n) (log n)^k n^(-1/2-alpha) V^+(n/N^+)
    phase exp(-i m log n)

Reflected dual branch coefficient:
    sigma_k Lambda(n) (log n)^k n^(-1/2+alpha) V^-(n/N^-)
    phase exp(+i m log n)
    sigma_k = (-1)^(k+1)

No multiplicative chi(s) appears in the reflected log-derivative dual
coefficients. The additive gamma/background term is handled separately
(see b2_canonical.py for the canonical real phase-curvature B_2).

Defaults for Agent 5's current script convention:
    k_Z = 0     # zero/incidence row z_n = Lambda(n) n^-1/2-alpha
    k_q = 3     # current Wronskian surrogate source row

Literal q''_can source-row tests should use:
    k_q = 2

Operator node convention:
    plus branch op-node:  +log n
    minus branch op-node: -log n  (signed real-frequency convention)

The folded conductor node log(m/(2*pi*n)) is diagnostic only and must NOT
be used as the Wronskian differential/operator node unless a folded
operator has explicitly been defined.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Iterable, Optional

import numpy as np


def sigma_k(k: int) -> int:
    """sigma_k = (-1)^(k+1)."""
    return -1 if (k % 2 == 0) else 1


def lambda_prime_only(n: int) -> float:
    """Von Mangoldt for prime-only runs; assumes n is prime."""
    return math.log(int(n))


def von_mangoldt_trial(n: int) -> float:
    """Von Mangoldt via trial division. Fine for toy runs."""
    n = int(n)
    if n < 2:
        return 0.0
    temp = n
    factors = []
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                temp //= d
                count += 1
            factors.append((d, count))
        d += 1 if d == 2 else 2
    if temp > 1:
        factors.append((temp, 1))
    if len(factors) == 1:
        return math.log(factors[0][0])
    return 0.0


def smooth_plateau(y: float) -> float:
    return 1.0


def smooth_bump(y: float) -> float:
    """C-infinity compact bump on [0,1), normalized to V(0)=1."""
    y = float(y)
    if y < 0.0 or y >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - y * y)) / math.exp(-1.0)


def get_smoothing(name: str) -> Callable[[float], float]:
    if name in ("plateau", "one", "none"):
        return smooth_plateau
    if name == "bump":
        return smooth_bump
    raise ValueError(f"unknown smoothing: {name!r}")


@dataclass
class BranchWeights:
    coeffs: np.ndarray
    phases: np.ndarray
    op_nodes: np.ndarray
    folded_nodes: np.ndarray
    weights_for_qr: np.ndarray
    logs: np.ndarray
    n_values: np.ndarray


def build_logderiv_weights(
    n_values: Iterable[int],
    m: float,
    alpha: float,
    branch: str,
    k: int,
    N: Optional[float] = None,
    smoothing: str | Callable[[float], float] = "plateau",
    lambda_func: Callable[[int], float] = lambda_prime_only,
    signed_operator_nodes: bool = True,
) -> BranchWeights:
    """
    Build corrected reflected log-derivative AFE branch weights.

    Args:
        branch: 'plus' or 'minus'.
        k: C_k index. Agent 5 current defaults: k_Z=0, k_q=3.
        N: smoothing conductor. If None, V=1 regardless of smoothing.
        smoothing: 'plateau', 'bump', or callable V(y).
        signed_operator_nodes: if True, minus op-node is -log n.
    """
    Vfun = smoothing if callable(smoothing) else get_smoothing(smoothing)

    n_arr = np.asarray(list(n_values), dtype=np.int64)
    L_arr = np.log(n_arr.astype(np.float64))
    Lam_arr = np.array([lambda_func(int(n)) for n in n_arr], dtype=np.float64)

    if N is None:
        V_arr = np.ones_like(L_arr)
    else:
        V_arr = np.array([Vfun(float(n) / float(N)) for n in n_arr], dtype=np.float64)

    if branch == "plus":
        coeff_arr = Lam_arr * (L_arr ** k) * (n_arr.astype(np.float64) ** (-0.5 - alpha)) * V_arr
        phase_arr = np.exp(-1j * m * L_arr)
        op_node_arr = +L_arr if signed_operator_nodes else L_arr.copy()
        folded_arr = L_arr.copy()
    elif branch == "minus":
        coeff_arr = sigma_k(k) * Lam_arr * (L_arr ** k) * (n_arr.astype(np.float64) ** (-0.5 + alpha)) * V_arr
        phase_arr = np.exp(+1j * m * L_arr)
        op_node_arr = -L_arr if signed_operator_nodes else L_arr.copy()
        if m > 0:
            folded_arr = np.log(m / (2.0 * math.pi * n_arr.astype(np.float64)))
        else:
            folded_arr = np.full_like(L_arr, np.nan)
    else:
        raise ValueError("branch must be 'plus' or 'minus'")

    coeffs_c = coeff_arr.astype(np.complex128)
    return BranchWeights(
        coeffs=coeffs_c,
        phases=phase_arr.astype(np.complex128),
        op_nodes=op_node_arr.astype(np.float64),
        folded_nodes=folded_arr.astype(np.float64),
        weights_for_qr=np.abs(coeffs_c) ** 2,
        logs=L_arr,
        n_values=n_arr,
    )


def conductor_sqrt_m(m: float) -> float:
    if m <= 0:
        raise ValueError("m must be positive for sqrt(m/(2*pi)) conductor")
    return math.sqrt(m / (2.0 * math.pi))


def conductor_cover_block(n_values: Iterable[int], y_at_max: float = 0.5) -> float:
    """Choose N so max(n)/N = y_at_max, keeping a block inside the bump plateau."""
    vals = [float(n) for n in n_values]
    if not vals:
        raise ValueError("empty n_values")
    return max(vals) / y_at_max
