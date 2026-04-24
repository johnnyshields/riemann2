"""UV-026 L1 Y R1 fixed-sector gauge checker.

The checker accepts a proposed fixed-sector vector for the L1 Y R1 cubic family
only if the vector is explicit in the I,S basis and is proportional to A5^f(m).
Determinants are used here only as an algebraic proportionality test on an
already supplied fixed-sector vector, not as determinant scalarization of an
undefined quotient object.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json


@dataclass(frozen=True)
class FixedVector:
    u: Fraction
    v: Fraction

    def pair(self) -> tuple[int | str, int | str]:
        return (_fmt(self.u), _fmt(self.v))


def _fmt(x: Fraction) -> int | str:
    return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def det(v: FixedVector, a5: FixedVector) -> Fraction:
    return v.u * a5.v - a5.u * v.v


def check_vector(label: str, v: FixedVector, a5: FixedVector) -> dict[str, object]:
    d = det(v, a5)
    return {
        "label": label,
        "fixed_sector_vector": v.pair(),
        "det_against_A5": _fmt(d),
        "is_A5_gauge": d == 0,
        "accepted_for_UV026": d == 0,
        "acceptance_reason": (
            "explicit fixed-sector proportionality"
            if d == 0
            else "nonzero quotient determinant, so not proportional to A5"
        ),
    }


def main() -> None:
    a5 = FixedVector(Fraction(2), Fraction(5))

    # No actual L1 Y R1 coefficient vector is supplied by the source-term report.
    proposed_l1yr1_vectors: list[tuple[str, FixedVector]] = []

    # Calibration examples only.  They are not claims about the actual package.
    calibration = [
        ("gauge_example_2A5", FixedVector(Fraction(4), Fraction(10))),
        ("prior_formal_witness", FixedVector(Fraction(3), Fraction(7))),
    ]

    result = {
        "A5": a5.pair(),
        "proof_standard": (
            "A proposed L1 Y R1 coefficient must be an explicit vector "
            "u I + v S after pi_f [z^7], and must satisfy det((u,v), A5)=0."
        ),
        "rejected_shortcuts": [
            "Phi_K scalar invisibility",
            "determinant scalarization without an explicit fixed-sector vector",
            "formal source support or UV-025 K-linear provenance alone",
            "swap symmetry without line-image theorem",
            "one-pair gauge law without identifying L1 Y R1 as that gauge shadow",
        ],
        "proposed_l1yr1_vectors_available": bool(proposed_l1yr1_vectors),
        "proposed_l1yr1_checks": [
            check_vector(label, vector, a5)
            for label, vector in proposed_l1yr1_vectors
        ],
        "calibration_checks_not_actual_claims": [
            check_vector(label, vector, a5) for label, vector in calibration
        ],
        "smallest_missing_coefficient_data": [
            "the fixed-sector coordinates (u,v) of pi_f [z^7] for the actual L1 Y R1 cubic family",
            "the source-tag component, tau1^2 tau2 or tau1 tau2^2, being checked",
            "the A5^f(m) coordinates in the same fixed-sector basis and same midpoint convention",
            "a derivation from the UV-025 tagged pre-whitening block through the matrix whitening expansion before Phi_K",
        ],
        "UV026_L1YR1_status": (
            "blocked_on_missing_coefficient_vector"
            if not proposed_l1yr1_vectors
            else "checked"
        ),
    }

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
