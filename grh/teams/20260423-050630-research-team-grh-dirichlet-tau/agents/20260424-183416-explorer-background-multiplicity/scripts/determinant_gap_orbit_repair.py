"""Check whether paired-completed zero orbits repair one-zero determinant failure.

Noether's one-zero computation rejects positivity for a single unscaled
K_{beta,gamma}.  In the completed paired Dirichlet object, a noncritical zero
orbit also carries the functional-equation reflected zero beta -> 1-beta,
which gives the same K and hence a local factor 2K at the same ordinate.

This script records the exact numerator for D[2K] and runs deterministic
random searches for sums of reflected and full conjugate-reflected orbits.
The searches are evidence only, not a proof.
"""

from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence, Tuple


@dataclass(frozen=True)
class Kernel:
    beta: float
    gamma: float
    weight: float


def component(a: float, y: float) -> Tuple[float, float, float]:
    den = a * a + y * y
    value = a / den
    first = -4.0 * a * y / (den * den)
    second = 8.0 * a * (3.0 * y * y - a * a) / (den * den * den)
    return value, first, second


def q_values(t: float, kernels: Sequence[Kernel]) -> Tuple[float, float, float]:
    q = 0.0
    qp = 0.0
    qpp = 0.0
    for k in kernels:
        y = 2.0 * t - k.gamma
        p1, d1, dd1 = component(1.0 - k.beta, y)
        p2, d2, dd2 = component(k.beta, y)
        q += k.weight * (p1 + p2)
        qp += k.weight * (d1 + d2)
        qpp += k.weight * (dd1 + dd2)
    return q, qp, qpp


def det_gap(t: float, kernels: Sequence[Kernel]) -> float:
    q, qp, qpp = q_values(t, kernels)
    return 2.0 * q * qpp + 4.0 * q**4 - 3.0 * qp**2


def local_minimize(kernels: Sequence[Kernel], lo: float, hi: float) -> Tuple[float, float]:
    best_t = lo
    best_d = float("inf")
    grid_points = 501
    for i in range(grid_points):
        t = lo + (hi - lo) * i / (grid_points - 1)
        d = det_gap(t, kernels)
        if d < best_d:
            best_t = t
            best_d = d
    step = (hi - lo) / (grid_points - 1)
    a = max(lo, best_t - 3.0 * step)
    b = min(hi, best_t + 3.0 * step)
    for _ in range(70):
        m1 = a + (b - a) / 3.0
        m2 = b - (b - a) / 3.0
        if det_gap(m1, kernels) < det_gap(m2, kernels):
            b = m2
        else:
            a = m1
    t = 0.5 * (a + b)
    return t, det_gap(t, kernels)


def exact_reflected_double_formula() -> None:
    print("Exact reflected-double formula:")
    print("For c=beta(1-beta), y=(2t-gamma)^2, h=(y+beta^2)(y+(1-beta)^2),")
    print("D[2K] = N2(c,y)/h^4 with")
    print("N2 = 192*c*y^4")
    print("   + 384*c*(1-2*c)*y^3")
    print("   + 192*c*(6*c^2-4*c+1)*y^2")
    print("   + 384*c^3*(1-2*c)*y")
    print("   + 192*c^5")
    print("For 0<c<=1/4 all displayed coefficients are positive.")
    print("Thus D[2K]>0 for every real t, beta in (0,1), and gamma.")
    print()


def orbit(beta: float, gamma: float, full: bool, multiplicity: int) -> List[Kernel]:
    # Off the critical line, beta -> 1-beta gives the same K, so the reflected
    # local weight is 2m.  On the critical line away from gamma=0, the
    # reflection is the same zero; a generic completed pair contributes the
    # conjugate ordinate with weight m, not a same-ordinate double.
    if abs(beta - 0.5) <= 1e-14 and abs(gamma) > 1e-14:
        kernels = [Kernel(beta, gamma, 1.0 * multiplicity)]
        if full:
            kernels.append(Kernel(beta, -gamma, 1.0 * multiplicity))
        return kernels
    kernels = [Kernel(beta, gamma, 2.0 * multiplicity)]
    if full and abs(gamma) > 1e-14:
        kernels.append(Kernel(beta, -gamma, 2.0 * multiplicity))
    return kernels


def fmt(kernels: Sequence[Kernel]) -> str:
    return "[" + ", ".join(
        f"(beta={k.beta:.12g}, gamma={k.gamma:.12g}, weight={k.weight:.12g})"
        for k in kernels
    ) + "]"


def random_beta(rng: random.Random, mode: str) -> float:
    if mode == "near-edge":
        eps = 10 ** rng.uniform(-3.0, -0.02)
        return eps if rng.random() < 0.5 else 1.0 - eps
    if mode == "critical":
        return 0.5
    return rng.uniform(0.001, 0.999)


def random_search(name: str, rng: random.Random, trials: int, full: bool, mode: str) -> None:
    best_t = 0.0
    best_d = float("inf")
    best_kernels: List[Kernel] = []
    for _ in range(trials):
        count = rng.randint(1, 5)
        kernels: List[Kernel] = []
        for _ in range(count):
            beta = random_beta(rng, mode)
            gamma = rng.uniform(-30.0, 30.0)
            mult = rng.randint(1, 3)
            kernels.extend(orbit(beta, gamma, full=full, multiplicity=mult))
        gammas = [k.gamma for k in kernels]
        lo = min(gammas) / 2.0 - 5.0
        hi = max(gammas) / 2.0 + 5.0
        t, d = local_minimize(kernels, lo, hi)
        if d < best_d:
            best_t = t
            best_d = d
            best_kernels = kernels
    print(f"{name}: best_D={best_d:.17g} at t={best_t:.17g}")
    print(f"{name}: kernels={fmt(best_kernels)}")


def named_checks() -> None:
    checks = {
        "unpaired_one_zero_beta_1_50": [Kernel(0.02, 0.0, 1.0)],
        "reflected_double_beta_1_50": [Kernel(0.02, 0.0, 2.0)],
        "critical_conjugate_pair_gamma_5": orbit(0.5, 5.0, full=True, multiplicity=1),
        "full_orbit_beta_1_50_gamma_5": orbit(0.02, 5.0, full=True, multiplicity=1),
        "two_full_orbits_nearby": orbit(0.02, 5.0, full=True, multiplicity=1)
        + orbit(0.03, 5.4, full=True, multiplicity=1),
    }
    print("Named checks:")
    for name, kernels in checks.items():
        gammas = [k.gamma for k in kernels]
        t, d = local_minimize(kernels, min(gammas) / 2.0 - 5.0, max(gammas) / 2.0 + 5.0)
        print(f"{name}: min_D={d:.17g} at t={t:.17g}")
        print(f"{name}: kernels={fmt(kernels)}")
    print()


def main() -> None:
    script_path = Path(__file__)
    print(f"script={script_path}")
    print(f"sha256={hashlib.sha256(script_path.read_bytes()).hexdigest()}")
    print()

    exact_reflected_double_formula()
    named_checks()

    rng = random.Random(2026042402)
    print("Random search evidence:")
    random_search("reflected_sums_general", rng, trials=2500, full=False, mode="general")
    random_search("full_orbit_sums_general", rng, trials=2500, full=True, mode="general")
    random_search("full_orbit_sums_near_edge", rng, trials=2500, full=True, mode="near-edge")
    random_search("generic_critical_conjugate_sums", rng, trials=2500, full=True, mode="critical")


if __name__ == "__main__":
    main()
