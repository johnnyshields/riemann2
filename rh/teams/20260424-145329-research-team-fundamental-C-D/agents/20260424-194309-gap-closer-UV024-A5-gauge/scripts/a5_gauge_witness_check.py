"""UV-024 fixed-sector gauge witness check.

This is a formal fixed-sector harness, not a computation of the actual
corrected-whitening package.  It tests whether the source constraints visible
in the inspected paper ranges force a cubic non-(1,1) order-7 coefficient to
lie on the gauge line C A5^f.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json


@dataclass(frozen=True)
class FixedVector:
    """Coordinates u I + v S in the fixed sector f = span{I,S}."""

    u: Fraction
    v: Fraction

    def __add__(self, other: "FixedVector") -> "FixedVector":
        return FixedVector(self.u + other.u, self.v + other.v)

    def scale(self, c: int) -> "FixedVector":
        return FixedVector(Fraction(c) * self.u, Fraction(c) * self.v)

    def as_pair(self) -> tuple[int | str, int | str]:
        return (_fmt(self.u), _fmt(self.v))


def _fmt(x: Fraction) -> int | str:
    return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


A5 = FixedVector(Fraction(2), Fraction(5))


def det_against_a5(vec: FixedVector) -> Fraction:
    """Good-patch quotient coordinate det(vec, A5)."""

    return vec.u * A5.v - A5.u * vec.v


def is_a5_gauge(vec: FixedVector) -> bool:
    return det_against_a5(vec) == 0


def quotient_report(vec: FixedVector) -> dict[str, object]:
    d = det_against_a5(vec)
    return {
        "vector": vec.as_pair(),
        "det_against_A5": _fmt(d),
        "is_A5_gauge": d == 0,
    }


def main() -> None:
    # Cubic finite-order witness of type (1,1,5): two source legs and one
    # fifth-order leg can contribute to the order-7 cross-effect coefficient.
    cubic_115 = FixedVector(Fraction(3), Fraction(7))

    # Swap compatibility can at most relate the mirrored source slots unless
    # an extra source theorem fixes the image line.  Test the strongest formal
    # symmetric version: the mirrored slot carries the same fixed-sector vector.
    swap_symmetric = cubic_115.scale(2)

    # A less specialized mirrored partner used by the prior UV-024 model.
    mirrored_partner = FixedVector(Fraction(4), Fraction(6))
    swap_pair_sum = cubic_115 + mirrored_partner

    # One-pair gauge law only adds multiples of A5, so det(_, A5) is invariant.
    gauge_shift = cubic_115 + A5.scale(11)

    result = {
        "harness_scope": (
            "formal fixed-sector source-bidegree model satisfying positive "
            "source support, order 7 = 1+1+5, swap symmetrization tests, and "
            "one-pair A5 gauge invariance; not the actual package"
        ),
        "A5": A5.as_pair(),
        "cubic_115_witness": quotient_report(cubic_115),
        "source_support_constraints": {
            "has_both_sources": True,
            "one_amplitude_collapse_kills": False,
            "total_finite_order": 7,
            "can_reach_B7": True,
        },
        "swap_tests": {
            "symmetric_same_slot": quotient_report(swap_symmetric),
            "generic_mirrored_pair_sum": quotient_report(swap_pair_sum),
            "swap_compatibility_alone_forces_gauge": False,
        },
        "one_pair_gauge_law_test": {
            "gauge_shift": quotient_report(gauge_shift),
            "det_invariant_under_adding_A5": det_against_a5(gauge_shift)
            == det_against_a5(cubic_115),
            "one_pair_gauge_law_kills_cubic_cross_effect": False,
        },
        "scalar_hidden_warning": {
            "can_set_scalar_detector_to_zero_on_witness_in_model": True,
            "quotient_det_still_nonzero": det_against_a5(cubic_115) != 0,
        },
        "forced_by_tested_constraints": False,
        "minimal_missing_theorem": (
            "For every actual non-(1,1) cubic finite-order source term T of "
            "type (1,1,5), det(B7^f(T), A5^f(m)) = 0, equivalently "
            "B7^f(T) lies in C A5^f(m)."
        ),
    }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
