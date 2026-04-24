"""Explore the UV-017 determinant gap for sums of strip-edge kernels.

The determinant expression is

    D[q] = 2 q q'' + 4 q**4 - 3 (q')**2

with derivatives in the boundary variable t.  A completed-zero kernel is

    K_{beta,gamma}(t)
      = (1-beta)/((1-beta)**2 + (2t-gamma)**2)
        + beta/(beta**2 + (2t-gamma)**2).

This script searches literal positive integer-multiplicity sums, conjugate
gamma-symmetric sums, and a deliberately non-source small-coefficient stress
case.  It also checks an exact symbolic special case when sympy is available.
"""

from __future__ import annotations

import hashlib
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


@dataclass(frozen=True)
class Kernel:
    beta: float
    gamma: float
    mult: int = 1
    weight: float = 1.0


def component(a: float, y: float) -> Tuple[float, float, float]:
    """Return p, dp/dt, d2p/dt2 for a/(a^2+y^2), y=2t-gamma."""

    den = a * a + y * y
    p = a / den
    dp = -4.0 * a * y / (den * den)
    d2p = 8.0 * a * (3.0 * y * y - a * a) / (den * den * den)
    return p, dp, d2p


def q_values(t: float, kernels: Sequence[Kernel]) -> Tuple[float, float, float]:
    q = 0.0
    qp = 0.0
    qpp = 0.0
    for ker in kernels:
        beta = ker.beta
        y = 2.0 * t - ker.gamma
        scale = ker.mult * ker.weight
        p1, dp1, d2p1 = component(1.0 - beta, y)
        p2, dp2, d2p2 = component(beta, y)
        q += scale * (p1 + p2)
        qp += scale * (dp1 + dp2)
        qpp += scale * (d2p1 + d2p2)
    return q, qp, qpp


def det_gap(t: float, kernels: Sequence[Kernel]) -> float:
    q, qp, qpp = q_values(t, kernels)
    return 2.0 * q * qpp + 4.0 * q**4 - 3.0 * qp**2


def det_ratio(t: float, kernels: Sequence[Kernel]) -> float:
    q, qp, qpp = q_values(t, kernels)
    return (2.0 * q * qpp + 4.0 * q**4 - 3.0 * qp**2) / q**4


def local_minimize(
    kernels: Sequence[Kernel],
    lo: float,
    hi: float,
    grid_points: int = 1201,
) -> Tuple[float, float, float]:
    """Grid then ternary-like refinement around the best grid point."""

    best_t = lo
    best_d = float("inf")
    for i in range(grid_points):
        t = lo + (hi - lo) * i / (grid_points - 1)
        d = det_gap(t, kernels)
        if d < best_d:
            best_t, best_d = t, d

    step = (hi - lo) / (grid_points - 1)
    a = max(lo, best_t - 2.0 * step)
    b = min(hi, best_t + 2.0 * step)
    for _ in range(80):
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        if det_gap(m1, kernels) < det_gap(m2, kernels):
            b = m2
        else:
            a = m1
    t = 0.5 * (a + b)
    return t, det_gap(t, kernels), det_ratio(t, kernels)


def format_kernels(kernels: Sequence[Kernel]) -> str:
    return "[" + ", ".join(
        f"(beta={k.beta:.12g}, gamma={k.gamma:.12g}, mult={k.mult}, weight={k.weight:.12g})"
        for k in kernels
    ) + "]"


def conjugate_symmetric(kernels: Iterable[Kernel]) -> List[Kernel]:
    out: List[Kernel] = []
    for k in kernels:
        out.append(k)
        if abs(k.gamma) > 1e-14:
            out.append(Kernel(k.beta, -k.gamma, k.mult, k.weight))
    return out


def functional_conjugate_symmetric(kernels: Iterable[Kernel]) -> List[Kernel]:
    """Full zero-orbit closure under rho -> conjugate and rho -> 1-rho."""

    out: List[Kernel] = []
    for k in kernels:
        candidates = [
            Kernel(k.beta, k.gamma, k.mult, k.weight),
            Kernel(k.beta, -k.gamma, k.mult, k.weight),
            Kernel(1.0 - k.beta, k.gamma, k.mult, k.weight),
            Kernel(1.0 - k.beta, -k.gamma, k.mult, k.weight),
        ]
        for cand in candidates:
            if abs(cand.gamma) <= 1e-14 and any(
                abs(prev.beta - cand.beta) < 1e-14 and abs(prev.gamma - cand.gamma) < 1e-14
                for prev in out
            ):
                continue
            out.append(cand)
    return out


def random_kernel(
    rng: random.Random,
    beta_mode: str,
    gamma_span: float,
    mult_max: int,
    weight: float = 1.0,
) -> Kernel:
    if beta_mode == "grh":
        beta = 0.5
    elif beta_mode == "near-edge":
        beta = 10 ** rng.uniform(-3.0, -0.05)
        if rng.random() < 0.5:
            beta = 1.0 - beta
    else:
        beta = rng.uniform(0.02, 0.98)
    gamma = rng.uniform(-gamma_span, gamma_span)
    mult = rng.randint(1, mult_max)
    return Kernel(beta, gamma, mult, weight)


def search_family(
    name: str,
    rng: random.Random,
    trials: int,
    n_min: int,
    n_max: int,
    beta_mode: str,
    symmetric: bool,
    quartet: bool,
    gamma_span: float,
    window_pad: float,
    mult_max: int,
    weight: float = 1.0,
) -> Tuple[float, float, float, List[Kernel]]:
    best = (float("inf"), 0.0, 0.0, [])
    for _ in range(trials):
        n = rng.randint(n_min, n_max)
        base = [
            random_kernel(rng, beta_mode, gamma_span, mult_max, weight=weight)
            for _ in range(n)
        ]
        if quartet:
            kernels = functional_conjugate_symmetric(base)
        elif symmetric:
            kernels = conjugate_symmetric(base)
        else:
            kernels = base
        gammas = [k.gamma for k in kernels]
        lo = min(gammas) / 2.0 - window_pad
        hi = max(gammas) / 2.0 + window_pad
        t, d, r = local_minimize(kernels, lo, hi)
        if d < best[0]:
            best = (d, t, r, list(kernels))
    d, t, r, kernels = best
    print(f"{name}: best_D={d:.17g} at t={t:.17g}, D/q^4={r:.17g}")
    print(f"{name}: kernels={format_kernels(kernels)}")
    return best


def check_named_configurations() -> None:
    configs = {
        "single_grh_origin": [Kernel(0.5, 0.0)],
        "single_offcritical_beta_1_50_origin": [Kernel(0.02, 0.0)],
        "two_grh_centers_pm_10": [Kernel(0.5, -10.0), Kernel(0.5, 10.0)],
        "conj_pair_grh_gamma_20": conjugate_symmetric([Kernel(0.5, 20.0)]),
        "two_offline_same_center": [Kernel(0.1, 0.0), Kernel(0.9, 0.0)],
        "two_near_edge_separated": [Kernel(0.02, -5.0), Kernel(0.98, 5.0)],
        "full_quartet_near_edge_gamma_5": functional_conjugate_symmetric([Kernel(0.02, 5.0)]),
    }
    print("Named configurations:")
    for name, kernels in configs.items():
        gammas = [k.gamma for k in kernels]
        t, d, r = local_minimize(kernels, min(gammas) / 2.0 - 4.0, max(gammas) / 2.0 + 4.0)
        print(f"{name}: min_D={d:.17g} at t={t:.17g}, D/q^4={r:.17g}")
        print(f"{name}: kernels={format_kernels(kernels)}")
    print()


def symbolic_two_grh_symmetric() -> None:
    print("Symbolic two-GRH symmetric check:")
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - availability check
        print(f"sympy unavailable: {exc}")
        return

    x, a = sp.symbols("x a", real=True)
    # Use x = 2t and centers at +/- a in the y=2t-gamma coordinate.
    q = 1 / ((x - a) ** 2 + sp.Rational(1, 4)) + 1 / ((x + a) ** 2 + sp.Rational(1, 4))
    qt = 2 * sp.diff(q, x)
    qtt = 4 * sp.diff(q, x, 2)
    det = sp.factor(2 * q * qtt + 4 * q**4 - 3 * qt**2)
    num, den = sp.factor(sp.together(det).as_numer_denom()[0]), sp.factor(sp.together(det).as_numer_denom()[1])
    print(f"numerator factorization: {num}")
    print(f"denominator factorization: {den}")
    # Sample the numerator as a polynomial in u=x^2, v=a^2 by substitution.
    u, v = sp.symbols("u v", nonnegative=True)
    num_uv = sp.factor(num.subs({x**2: u, a**2: v}))
    print(f"numerator after x^2=u, a^2=v substitution attempt: {num_uv}")
    print()


def artificial_small_weight_stress() -> None:
    # This is not a literal multiplicity source. It tests whether the inequality
    # could hold for arbitrary positive coefficients.
    kernels = [Kernel(0.5, 0.0, weight=0.05), Kernel(0.5, 6.0, weight=0.05)]
    t, d, r = local_minimize(kernels, -2.0, 5.0)
    print("Artificial small-coefficient stress:")
    print(f"min_D={d:.17g} at t={t:.17g}, D/q^4={r:.17g}")
    print(f"kernels={format_kernels(kernels)}")
    print()


def exact_single_center_formula() -> None:
    from fractions import Fraction

    beta = Fraction(1, 50)
    one = Fraction(1, 1)
    a = beta
    b = one - beta
    q = one / (a * b)
    qp = Fraction(0, 1)
    qpp = -8 * (one / (a**3) + one / (b**3))
    det = 2 * q * qpp + 4 * q**4 - 3 * qp**2
    print("Exact single off-critical center check:")
    print("beta=1/50, gamma=0, t=0")
    print(f"q={q}")
    print(f"q'={qp}")
    print(f"q''={qpp}")
    print(f"D={det}")
    print(f"D_float={float(det):.17g}")
    print()


def main() -> None:
    script_path = Path(__file__)
    sha = hashlib.sha256(script_path.read_bytes()).hexdigest()
    print(f"script={script_path}")
    print(f"sha256={sha}")
    print()

    check_named_configurations()
    symbolic_two_grh_symmetric()
    exact_single_center_formula()
    artificial_small_weight_stress()

    rng = random.Random(20260424)
    print("Random searches:")
    search_family(
        name="integer_unconstrained_2_to_5",
        rng=rng,
        trials=3000,
        n_min=2,
        n_max=5,
        beta_mode="general",
        symmetric=False,
        quartet=False,
        gamma_span=20.0,
        window_pad=4.0,
        mult_max=3,
    )
    search_family(
        name="integer_conjugate_symmetric_1_to_4_base",
        rng=rng,
        trials=3000,
        n_min=1,
        n_max=4,
        beta_mode="general",
        symmetric=True,
        quartet=False,
        gamma_span=20.0,
        window_pad=4.0,
        mult_max=3,
    )
    search_family(
        name="integer_grh_conjugate_symmetric_1_to_5_base",
        rng=rng,
        trials=3000,
        n_min=1,
        n_max=5,
        beta_mode="grh",
        symmetric=True,
        quartet=False,
        gamma_span=30.0,
        window_pad=4.0,
        mult_max=3,
    )
    search_family(
        name="integer_near_edge_conjugate_symmetric_1_to_4_base",
        rng=rng,
        trials=3000,
        n_min=1,
        n_max=4,
        beta_mode="near-edge",
        symmetric=True,
        quartet=False,
        gamma_span=20.0,
        window_pad=4.0,
        mult_max=3,
    )
    search_family(
        name="integer_full_quartet_general_1_to_4_base",
        rng=rng,
        trials=3000,
        n_min=1,
        n_max=4,
        beta_mode="general",
        symmetric=False,
        quartet=True,
        gamma_span=20.0,
        window_pad=4.0,
        mult_max=3,
    )
    search_family(
        name="integer_full_quartet_near_edge_1_to_4_base",
        rng=rng,
        trials=3000,
        n_min=1,
        n_max=4,
        beta_mode="near-edge",
        symmetric=False,
        quartet=True,
        gamma_span=20.0,
        window_pad=4.0,
        mult_max=3,
    )


if __name__ == "__main__":
    main()
