"""Adversarial UV-026 cubic witness harness.

This script keeps the formal fixed-sector witness from the UV-024 A5-gauge
pass and tests which proof routes actually force proportionality to A5^f.
It treats the UV-025 tagged pre-whitening B2 block as an allowed upstream
constraint, but not as a downstream B7^f or quotient-gauge theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json


@dataclass(frozen=True)
class FixedVector:
    u: Fraction
    v: Fraction

    def __add__(self, other: "FixedVector") -> "FixedVector":
        return FixedVector(self.u + other.u, self.v + other.v)

    def scale(self, c: int) -> "FixedVector":
        return FixedVector(c * self.u, c * self.v)

    def pair(self) -> tuple[int | str, int | str]:
        return (_fmt(self.u), _fmt(self.v))


def _fmt(x: Fraction) -> int | str:
    return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


A5 = FixedVector(Fraction(2), Fraction(5))
WITNESS = FixedVector(Fraction(3), Fraction(7))


def det_against_a5(v: FixedVector) -> Fraction:
    return v.u * A5.v - A5.u * v.v


def is_gauge(v: FixedVector) -> bool:
    return det_against_a5(v) == 0


def report_vector(v: FixedVector) -> dict[str, object]:
    return {
        "vector": v.pair(),
        "det_against_A5": _fmt(det_against_a5(v)),
        "is_A5_gauge": is_gauge(v),
    }


def route(name: str, forces_gauge: bool, accepted: bool, reason: str) -> dict[str, object]:
    return {
        "route": name,
        "forces_fixed_sector_A5_proportionality": forces_gauge,
        "accepted_for_UV026": accepted,
        "reason": reason,
    }


def main() -> None:
    symmetric_swap = WITNESS.scale(2)
    generic_swap = WITNESS + FixedVector(Fraction(4), Fraction(6))
    gauge_shifted = WITNESS + A5.scale(11)

    routes = [
        route(
            "Phi_K scalar hiding",
            False,
            False,
            "A scalar functional can vanish while det(B7f(T), A5) remains nonzero.",
        ),
        route(
            "determinant scalarization after quotient chart",
            False,
            False,
            "The determinant chart detects the same nonzero quotient; it is not a proof of gauge.",
        ),
        route(
            "swap symmetry",
            False,
            False,
            "Symmetric witness has det 2 and generic mirrored sum has det 9.",
        ),
        route(
            "one-pair projected gauge law",
            False,
            False,
            "Adding multiples of A5 preserves det; the witness det stays 1.",
        ),
        route(
            "UV-025 tagged pre-whitening B2 linearity",
            False,
            False,
            "It supplies source-linear input but no B7f fixed-sector proportionality theorem.",
        ),
        route(
            "actual fixed-sector cubic gauge theorem",
            True,
            True,
            "This is the missing UV-026 theorem: B7f(T) in C A5^f(m).",
        ),
    ]

    result = {
        "A5": A5.pair(),
        "cubic_115_witness": report_vector(WITNESS),
        "stress_tests": {
            "swap_symmetric": report_vector(symmetric_swap),
            "swap_generic_pair_sum": report_vector(generic_swap),
            "one_pair_gauge_shift": report_vector(gauge_shifted),
            "gauge_shift_det_invariant": det_against_a5(gauge_shifted)
            == det_against_a5(WITNESS),
        },
        "accepted_proof_standard": "fixed-sector proportionality to A5^f before scalar hiding or determinant bookkeeping",
        "route_verdicts": routes,
        "uv025_changes_status": "upstream source-linear B2 block only",
        "witness_status_after_uv025": {
            "formal_countermodel_to_shortcuts": True,
            "genuine_actual_package_obstruction": False,
            "why_not_actual": (
                "No inspected source or paper-update computes B7^f for the actual "
                "cubic (1,1,5) term or proves/prohibits its proportionality to A5^f."
            ),
        },
    }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
