#!/usr/bin/env python3
"""
UV-026 L2N0R1/L1N0R2 homogeneous-grade order gate.

Under the homogeneous scalar source grade
    Gr_a r = r^(a+2)(m) (t-m)^(a+2)/(a+2)!
the same-point first-Frechet grade a starts in ordinary z order a, and a
second-Frechet output with grades {a,b} starts at order a+b.  The middle
factor is the baseline mixed block N0, which has a removable holomorphic
ordinary-z expansion starting at order 0.

This script enumerates the (1,1,5) placements for L2N0R1/L1N0R2 and records
the minimal z^7 coefficient theorem.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "l2n0r1_homogeneous_order_gate.json"


def same_point_order(grade: int) -> int:
    return grade


def first_frechet_order(grade: int) -> int:
    return same_point_order(grade)


def second_frechet_order(grades: tuple[int, int]) -> int:
    return same_point_order(grades[0]) + same_point_order(grades[1])


def baseline_n0_order() -> int:
    return 0


def family_terms(side: str):
    if side == "L2N0R1":
        return [
            {
                "family": side,
                "second_side": "left",
                "second_frechet_grades": [1, 1],
                "first_side": "right",
                "first_frechet_grade": 5,
            },
            {
                "family": side,
                "second_side": "left",
                "second_frechet_grades": [1, 5],
                "first_side": "right",
                "first_frechet_grade": 1,
            },
        ]
    if side == "L1N0R2":
        return [
            {
                "family": side,
                "second_side": "right",
                "second_frechet_grades": [1, 1],
                "first_side": "left",
                "first_frechet_grade": 5,
            },
            {
                "family": side,
                "second_side": "right",
                "second_frechet_grades": [1, 5],
                "first_side": "left",
                "first_frechet_grade": 1,
            },
        ]
    raise ValueError(side)


def annotate(term):
    second_order = second_frechet_order(tuple(term["second_frechet_grades"]))
    first_order = first_frechet_order(term["first_frechet_grade"])
    n0_order = baseline_n0_order()
    total_order = second_order + n0_order + first_order
    out = dict(term)
    out.update(
        {
            "second_frechet_lowest_order": second_order,
            "baseline_N0_lowest_order": n0_order,
            "first_frechet_lowest_order": first_order,
            "total_lowest_order": total_order,
            "can_reach_z7": total_order <= 7,
            "requires_exact_leading_coefficients_only": total_order == 7,
            "z7_extra_order_budget": 7 - total_order,
        }
    )
    return out


def leading_theorem():
    return {
        "L2N0R1": {
            "112": [
                "L_{-,11}^{[1,1]}[z^2] * N0[z^0] * Lambda_{2,+}^{[5]}[z^5]",
                "L_{-,11}^{[1,5]}[z^6] * N0[z^0] * Lambda_{2,+}^{[1]}[z^1]",
                "L_{-,12}^{[1,1]}[z^2] * N0[z^0] * Lambda_{1,+}^{[5]}[z^5]",
                "L_{-,12}^{[1,5]}[z^6] * N0[z^0] * Lambda_{1,+}^{[1]}[z^1]",
            ],
            "122": [
                "L_{-,22}^{[1,1]}[z^2] * N0[z^0] * Lambda_{1,+}^{[5]}[z^5]",
                "L_{-,22}^{[1,5]}[z^6] * N0[z^0] * Lambda_{1,+}^{[1]}[z^1]",
                "L_{-,12}^{[1,1]}[z^2] * N0[z^0] * Lambda_{2,+}^{[5]}[z^5]",
                "L_{-,12}^{[1,5]}[z^6] * N0[z^0] * Lambda_{2,+}^{[1]}[z^1]",
            ],
        },
        "L1N0R2": {
            "112": [
                "Lambda_{1,-}^{[5]}[z^5] * N0[z^0] * R_{+,12}^{[1,1]}[z^2]",
                "Lambda_{1,-}^{[1]}[z^1] * N0[z^0] * R_{+,12}^{[1,5]}[z^6]",
                "Lambda_{2,-}^{[5]}[z^5] * N0[z^0] * R_{+,11}^{[1,1]}[z^2]",
                "Lambda_{2,-}^{[1]}[z^1] * N0[z^0] * R_{+,11}^{[1,5]}[z^6]",
            ],
            "122": [
                "Lambda_{2,-}^{[5]}[z^5] * N0[z^0] * R_{+,12}^{[1,1]}[z^2]",
                "Lambda_{2,-}^{[1]}[z^1] * N0[z^0] * R_{+,12}^{[1,5]}[z^6]",
                "Lambda_{1,-}^{[5]}[z^5] * N0[z^0] * R_{+,22}^{[1,1]}[z^2]",
                "Lambda_{1,-}^{[1]}[z^1] * N0[z^0] * R_{+,22}^{[1,5]}[z^6]",
            ],
        },
    }


def main() -> None:
    terms = [annotate(t) for fam in ("L2N0R1", "L1N0R2") for t in family_terms(fam)]
    manifest = {
        "scope": "pre-Phi_K ordinary-z order gate for L_2N_0R_1 and L_1N_0R_2",
        "assumption": "homogeneous scalar grade Gr_a r=r^(a+2)(m)(t-m)^(a+2)/(a+2)!",
        "rules": {
            "first_frechet_grade_a_lowest_order": "a",
            "second_frechet_grades_a_b_lowest_order": "a+b",
            "baseline_N0_lowest_order": 0,
        },
        "terms": terms,
        "closure": {
            "order_count_removes_families": all(t["total_lowest_order"] > 7 for t in terms),
            "minimum_total_order": min(t["total_lowest_order"] for t in terms),
            "all_terms_can_reach_z7": all(t["total_lowest_order"] == 7 for t in terms),
            "only_leading_coefficients_contribute_to_z7": all(
                t["requires_exact_leading_coefficients_only"] for t in terms
            ),
            "reason": (
                "N0 has order 0, so {1,1} with first grade 5 and {1,5} "
                "with first grade 1 both land exactly at z^7"
            ),
        },
        "minimal_missing_theorem": leading_theorem(),
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(
        json.dumps(
            {
                "output": str(OUT),
                "sha1": digest,
                "closure": manifest["closure"],
                "terms": terms,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
