#!/usr/bin/env python3
"""
UV-026 L2YR0/L0YR2 homogeneous-grade order gate.

Under the homogeneous scalar source grade
    Gr_a r = r^(a+2)(m) (t-m)^(a+2)/(a+2)!
the same-point source-linear input of grade a starts in ordinary z order a,
while the mixed input of odd grades a=1,5 starts in order a+1 by the exact
plus/minus parity cancellation.

This script enumerates the L2YR0/L0YR2 grade placements of type (1,1,5) and
tests whether any can reach B_7 before Phi_K.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "l2yr0_homogeneous_order_gate.json"


def same_point_order(grade: int) -> int:
    """Lowest z order of delta G^[grade] under the homogeneous scalar split."""
    return grade


def mixed_order(grade: int) -> int:
    """Lowest z order of M^[grade] for grade 1/5 odd scalar pieces."""
    if grade in (1, 5):
        return grade + 1
    raise ValueError(f"Only grade 1/5 needed here, got {grade}")


def second_frechet_order(grades: tuple[int, int]) -> int:
    """Holomorphic second Frechet term cannot lower the sum of input orders."""
    return same_point_order(grades[0]) + same_point_order(grades[1])


def family_terms(side: str):
    if side not in {"L2YR0", "L0YR2"}:
        raise ValueError(side)
    baseline_side = "R0" if side == "L2YR0" else "L0"
    return [
        {
            "family": side,
            "second_frechet_grades": [1, 1],
            "mixed_grade": 5,
            "baseline_factor": baseline_side,
        },
        {
            "family": side,
            "second_frechet_grades": [1, 5],
            "mixed_grade": 1,
            "baseline_factor": baseline_side,
        },
    ]


def annotate(term):
    second_order = second_frechet_order(tuple(term["second_frechet_grades"]))
    middle_order = mixed_order(term["mixed_grade"])
    baseline_order = 0
    total_order = second_order + middle_order + baseline_order
    out = dict(term)
    out.update(
        {
            "second_frechet_lowest_order": second_order,
            "mixed_lowest_order": middle_order,
            "baseline_lowest_order": baseline_order,
            "total_lowest_order": total_order,
            "can_reach_z7": total_order <= 7,
            "z7_requires_extra_order": 7 - total_order,
        }
    )
    return out


def main() -> None:
    terms = [annotate(t) for fam in ("L2YR0", "L0YR2") for t in family_terms(fam)]
    manifest = {
        "scope": "pre-Phi_K ordinary-z order gate for L_2YR_0 and L_0YR_2",
        "assumption": "homogeneous scalar grade Gr_a r=r^(a+2)(m)(t-m)^(a+2)/(a+2)!",
        "rules": {
            "same_point_grade_a_lowest_order": "a",
            "mixed_grade_1_lowest_order": mixed_order(1),
            "mixed_grade_5_lowest_order": mixed_order(5),
            "second_frechet_lowest_order": "sum of same-point input orders",
            "baseline_L0_R0_lowest_order": 0,
        },
        "terms": terms,
        "closure": {
            "all_terms_start_after_z7": all(t["total_lowest_order"] > 7 for t in terms),
            "minimum_total_order": min(t["total_lowest_order"] for t in terms),
            "families_absent_at_B7": all(t["total_lowest_order"] > 7 for t in terms),
            "reason": (
                "L2^{1,1}M^{5} and L2^{1,5}M^{1} both start at z^8; "
                "the second Frechet factors do not lower order"
            ),
        },
        "next_y_slot_gate": "none among L_1YR_1, L_2YR_0, L_0YR_2 under homogeneous grade; remaining families with N0 do not contain Y",
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
