"""Verifier for UV-026 L_2YR_0 / L_0YR_2 homogeneous order absence.

The audit checks the order-count argument only.  It assumes the homogeneous
scalar-grade convention and the source-proved holomorphy of the baseline
inverse square root.  A holomorphic second Frechet coefficient has no negative
ordinary-z powers, so the second-Frechet output order is at least the sum of
the two input orders.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "l2yr0_order_verifier.json"


def sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def same_point_order(grade: int) -> int:
    # Under Gr_a r = r^(a+2)(m)*(t-m)^(a+2)/(a+2)!,
    # the g=r'' same-point channel starts at z^a.
    return grade


def mixed_order(grade: int) -> int:
    # The grades used here are odd derivative orders k=a+2.
    # Exact mixed parity delays odd k by one: r^(3) -> z^2, r^(7) -> z^6.
    if grade == 1:
        return 2
    if grade == 5:
        return 6
    raise ValueError(f"unexpected grade {grade}")


def second_frechet_order(grades: tuple[int, int]) -> int:
    return sum(same_point_order(g) for g in grades)


placements = [
    {
        "family": "L2YR0",
        "side_factor": "left second Frechet",
        "same_point_grades": [1, 1],
        "mixed_grade": 5,
        "right_baseline_order": 0,
    },
    {
        "family": "L2YR0",
        "side_factor": "left second Frechet",
        "same_point_grades": [1, 5],
        "mixed_grade": 1,
        "right_baseline_order": 0,
    },
    {
        "family": "L0YR2",
        "side_factor": "right second Frechet",
        "same_point_grades": [1, 1],
        "mixed_grade": 5,
        "left_baseline_order": 0,
    },
    {
        "family": "L0YR2",
        "side_factor": "right second Frechet",
        "same_point_grades": [1, 5],
        "mixed_grade": 1,
        "left_baseline_order": 0,
    },
]

rows = []
for item in placements:
    side_order = second_frechet_order(tuple(item["same_point_grades"]))
    y_order = mixed_order(item["mixed_grade"])
    baseline_order = item.get("left_baseline_order", item.get("right_baseline_order", 0))
    total = side_order + y_order + baseline_order
    rows.append({
        **item,
        "second_frechet_min_order": side_order,
        "mixed_min_order": y_order,
        "baseline_factor_min_order": baseline_order,
        "total_min_order": total,
        "can_reach_z7": total <= 7,
    })

manifest = {
    "scope": "pre-Phi_K ordinary-z order verification for homogeneous L2YR0/L0YR2",
    "homogeneous_grade_rule": "Gr_a r keeps r^(a+2)(m)*(t-m)^(a+2)/(a+2)!",
    "order_lemma": "holomorphic second Frechet inverse-square-root coefficients have no negative ordinary-z powers",
    "placements": rows,
    "minimum_total_order": min(row["total_min_order"] for row in rows),
    "all_terms_start_after_z7": all(not row["can_reach_z7"] for row in rows),
    "families_absent_at_B7": all(not row["can_reach_z7"] for row in rows),
    "quarantine": "alternative matrix-output M^[5] order-5 convention not tested here",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "output": str(OUT),
    "script_sha1": sha1(Path(__file__).resolve()),
    "output_sha1": sha1(OUT),
    "minimum_total_order": manifest["minimum_total_order"],
    "all_terms_start_after_z7": manifest["all_terms_start_after_z7"],
    "families_absent_at_B7": manifest["families_absent_at_B7"],
}, indent=2))
