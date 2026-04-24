"""Inventory cubic (1,1,5) sources in pre-PhiK whitening.

This is a formal bookkeeping harness, not an actual coefficient computation.
It enumerates the homogeneous cubic families in
W(G_-,N,G_+) = G_-^{-1/2} N G_+^{-1/2}, assuming N is affine in the block
perturbation and each inverse square-root factor has a Frechet series.

The goal is to test whether the currently cited source mechanisms
(one-pair K5 shadow and commutator projection) classify all possible cubic
non-(1,1) source-tag families. They do not: unless a term is identified by a
separate theorem as a K5/K3 shadow, a generic fixed-sector coefficient remains
live modulo C A5^f.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json


@dataclass(frozen=True)
class CubicFamily:
    left_degree: int
    middle_degree: int
    right_degree: int
    description: str
    source_classification: str

    def as_dict(self) -> dict[str, object]:
        return {
            "degrees_LNR": (self.left_degree, self.middle_degree, self.right_degree),
            "description": self.description,
            "source_classification": self.source_classification,
            "can_carry_115_grades": True,
            "can_carry_non11_tags": True,
        }


def det(vec: tuple[Fraction, Fraction], a5: tuple[Fraction, Fraction]) -> Fraction:
    return vec[0] * a5[1] - a5[0] * vec[1]


def fmt(x: Fraction) -> int | str:
    return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    families = [
        CubicFamily(3, 0, 0, "D^3(G_-^{-1/2})[X,X,X] N0 R0", "live unless proved K5/K3/pure"),
        CubicFamily(0, 0, 3, "L0 N0 D^3(G_+^{-1/2})[X,X,X]", "live unless proved K5/K3/pure"),
        CubicFamily(2, 1, 0, "D^2(G_-^{-1/2})[X,X] Y R0", "live unless proved K5/K3/pure"),
        CubicFamily(0, 1, 2, "L0 Y D^2(G_+^{-1/2})[X,X]", "live unless proved K5/K3/pure"),
        CubicFamily(2, 0, 1, "D^2(G_-^{-1/2})[X,X] N0 D(G_+^{-1/2})[X]", "live unless proved K5/K3/pure"),
        CubicFamily(1, 0, 2, "D(G_-^{-1/2})[X] N0 D^2(G_+^{-1/2})[X,X]", "live unless proved K5/K3/pure"),
        CubicFamily(1, 1, 1, "D(G_-^{-1/2})[X] Y D(G_+^{-1/2})[X]", "live unless proved K5/K3/pure"),
    ]

    a5 = (Fraction(2), Fraction(5))
    generic_witness = (Fraction(3), Fraction(7))
    quotient_det = det(generic_witness, a5)

    output = {
        "scope": "formal cubic family inventory for staged UV-025 pre-PhiK source block",
        "cubic_homogeneous_families": [family.as_dict() for family in families],
        "non11_tag_monomials_from_three_source_linear_factors": [
            "tau1^2 tau2",
            "tau1 tau2^2",
        ],
        "finite_grade_pattern": [1, 1, 5],
        "source_mechanisms_seen_in_paper": {
            "K5_shadow": "A_{7,K5}^f = c2 A5^f, only after term is identified as K5 shadow",
            "K3_shadow": "A_{7,K3}^f = 0, only after term is identified as K3 shadow",
            "pure_same_point": "vanishes in one-pair odd germ, not automatic for two-source cross terms",
            "general_cubic_whitening_term": "no cited theorem maps it to K5/K3/pure",
        },
        "generic_fixed_sector_test": {
            "A5": [fmt(a5[0]), fmt(a5[1])],
            "witness": [fmt(generic_witness[0]), fmt(generic_witness[1])],
            "det_against_A5": fmt(quotient_det),
            "is_A5_gauge": quotient_det == 0,
        },
        "conclusion": {
            "all_cubic_families_classified_by_current_source": False,
            "UV026_closed": False,
            "remaining_live_status": "formal-live until actual B7^f coefficients are computed or a source theorem identifies them as K5/K3/pure",
        },
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
