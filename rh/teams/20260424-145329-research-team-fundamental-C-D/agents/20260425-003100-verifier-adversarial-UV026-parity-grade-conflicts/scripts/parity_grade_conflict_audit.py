"""Audit UV-026 parity-corrected M^[5] bookkeeping.

This script does not recompute the full mixed block.  It records the finite
order consequences of the source formulas and the already verified parity
theorem, then checks whether assigning the even derivatives that support
[z^5]M to a grade-five mixed input is compatible with scalar-grade bookkeeping.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "parity_grade_conflict_audit.json"


def sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def derivative_row(k: int) -> dict:
    natural_grade = k - 2
    same_point_lowest = k - 2
    if k % 2 == 0:
        mixed_lowest = k - 2
        mixed_lowest_channel = "diagonal M22"
        odd_mixed_powers_possible = True
    else:
        mixed_lowest = k - 1
        mixed_lowest_channel = "off-diagonal after M22 cancellation"
        odd_mixed_powers_possible = False
    return {
        "source_derivative": f"r^{k}",
        "natural_grade_if_grade_is_lowest_order": natural_grade,
        "same_point_deltaG_lowest_order": same_point_lowest,
        "mixed_M_lowest_order": mixed_lowest,
        "mixed_lowest_channel": mixed_lowest_channel,
        "can_contribute_to_z5_M_by_parity_theorem": k in (2, 4, 6),
        "odd_mixed_powers_possible_for_this_derivative": odd_mixed_powers_possible,
        "conflict_if_assigned_to_M_grade_5": (
            natural_grade != 5
            and k in (2, 4, 6)
        ),
    }


rows = [derivative_row(k) for k in range(2, 8)]

even_support = [row for row in rows if row["can_contribute_to_z5_M_by_parity_theorem"]]
conflicts = [row for row in rows if row["conflict_if_assigned_to_M_grade_5"]]

readings = {
    "source_grade_label": {
        "verdict": "conflict unless a new non-homogeneous grade theorem moves or duplicates lower natural grades",
        "reason": "r^2,r^4,r^6 naturally occupy grades 0,2,4 and their same-point deltaG pieces start in orders 0,2,4, not grade 5.",
    },
    "actual_ordinary_z_order_5_projection": {
        "verdict": "conditionally coherent as a matrix-output projection, not as a scalar source grade",
        "reason": "It may define the coefficient [z^5] of the full scaled mixed input, but then M^[5] is not Gr_5 r and cannot supply deltaG^[5] source data.",
    },
    "parity_corrected_nonhomogeneous_source_projection": {
        "verdict": "possible only with explicit compatibility conditions",
        "reason": "A projection using r^2,r^4,r^6 must state how it avoids double-counting grades 0,2,4 and how its same-point low-order shadows are excluded or reclassified.",
    },
}

manifest = {
    "scope": "pre-Phi_K ordinary-z grade conflict audit for UV-026 M_i^[5]",
    "input_facts": {
        "transpose_parity": "M(-z)=M(z)^T",
        "z5_M_support": ["r^2", "r^4", "r^6"],
        "homogeneous_r7_candidate": "[z^5]M=0; first mixed order is 6",
    },
    "derivative_rows": rows,
    "even_derivatives_supporting_z5M": [row["source_derivative"] for row in even_support],
    "conflicting_assignments_to_scalar_grade5": [
        {
            "source_derivative": row["source_derivative"],
            "natural_grade": row["natural_grade_if_grade_is_lowest_order"],
            "same_point_lowest_order": row["same_point_deltaG_lowest_order"],
            "mixed_lowest_order": row["mixed_M_lowest_order"],
        }
        for row in conflicts
    ],
    "readings": readings,
    "acceptance_checklist": [
        "State whether [5] is a source-grade label, an actual z^5 matrix projection, or a non-homogeneous parity-corrected projection.",
        "If [5] is scalar source grade, prove r^2,r^4,r^6 are removed from or consistently shared with grades 0,2,4.",
        "If [5] is z^5 matrix projection, rename or define it as a mixed-output coefficient, not Gr_5 r.",
        "If non-homogeneous, prove source tags remain linear and same-point low-order shadows do not enter Lambda^[1] or unlisted cubic families.",
        "Update or prove compatibility with the seven-family inventory before determinant/gauge tests.",
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "output": str(OUT),
    "script_sha1": sha1(Path(__file__).resolve()),
    "output_sha1": sha1(OUT),
    "conflicting_derivatives": manifest["conflicting_assignments_to_scalar_grade5"],
    "readings": readings,
}, indent=2))
