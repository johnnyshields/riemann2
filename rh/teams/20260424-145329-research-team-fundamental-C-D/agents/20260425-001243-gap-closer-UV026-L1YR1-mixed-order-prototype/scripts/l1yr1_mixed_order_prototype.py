#!/usr/bin/env python3
"""
UV-026 L_1YR_1 homogeneous mixed-order prototype.

This is an exact order/parity audit for the displayed pre-Phi_K source
formulas.  It tests the candidate:
  grade 1 = r^(3)(m) only,
  grade 5 = r^(7)(m) only.

The key point is the plus/minus symmetry in the mixed block.  A scalar Taylor
monomial of odd order k has d_+ + d_- = 0, so the apparent M_22 order k-2
channel cancels.  The first mixed contribution then occurs in the off-diagonal
d/s channel at order k-1.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "l1yr1_mixed_order_prototype.json"


def same_point_order(k: int) -> int:
    # delta G_22 contains g=r'', so same-point order is k-2.
    return k - 2


def mixed_order(k: int) -> int:
    # Mixed input M=D_Q delta N:
    # - if k is even, eta/s^3 and (d_-+d_+)/s^2 both occur in M_22 at k-2;
    # - if k is odd, eta=0 and d_-+d_+=0, so the first channel is off-diagonal d/s at k-1.
    return k - 2 if k % 2 == 0 else k - 1


def mixed_leading_channel(k: int) -> str:
    if k % 2 == 0:
        return "M22 via eta/s^3 and (d_-+d_+)/s^2"
    return "M12/M21 via d_+/s and d_-/s after M22 leading cancellation"


def main():
    rows = []
    for k in range(2, 10):
        rows.append({
            "scalar_derivative_order_k": k,
            "same_point_deltaG_first_order": same_point_order(k),
            "mixed_M_first_order": mixed_order(k),
            "mixed_leading_channel": mixed_leading_channel(k),
            "same_and_mixed_orders_match": same_point_order(k) == mixed_order(k),
        })

    candidate = {
        "grade1": {
            "source": "r^(3)(m) only",
            "same_point_deltaG_order": same_point_order(3),
            "mixed_M_order": mixed_order(3),
            "compatible": same_point_order(3) == mixed_order(3),
            "obstruction": "grade 1 same-point input exists at z^1, but mixed input first appears at z^2",
        },
        "grade5": {
            "source": "r^(7)(m) only",
            "same_point_deltaG_order": same_point_order(7),
            "mixed_M_order": mixed_order(7),
            "M_z5": "zero by odd plus/minus cancellation",
            "compatible": same_point_order(7) == mixed_order(7),
            "obstruction": "grade 5 same-point input exists at z^5, but mixed input first appears at z^6",
        },
    }

    manifest = {
        "scope": "pre-Phi_K exact order/parity audit for homogeneous mixed-order L_1YR_1 prototype",
        "source_formula_reason": {
            "same_point": "deltaG_22 has the linear g=r'' channel, so derivative order k appears at z^(k-2)",
            "mixed_even_k": "eta is nonzero and d_-+d_+ is nonzero, so M_22 appears at z^(k-2)",
            "mixed_odd_k": "eta=0 and d_-+d_+=0; M_22 leading channel cancels and off-diagonal d/s appears at z^(k-1)",
        },
        "rows": rows,
        "homogeneous_candidate": candidate,
        "L1YR1_consequence": {
            "needed_for_z7": "[z]Lambda^[1], [z^5]M^[5], [z]Lambda^[1]",
            "under_candidate_M5_z5": "zero",
            "C112_z7": "zero for the prototype because [z^5]M(r^(7))=0",
            "C122_z7": "zero for the prototype because [z^5]M(r^(7))=0",
            "interpretation": (
                "This is not a positive determinant-gate computation. It shows the homogeneous "
                "mixed-order convention fails to supply the intended M_i^[5] input."
            ),
        },
        "baseline_status": {
            "full_q0_specialization_is_hard_blocker": False,
            "hard_blocker": "exact mixed-block parity: odd k=a+2 pieces miss odd mixed grades",
            "baseline_coefficients_needed_after_fixing_grade": (
                "If a nonzero M^[5] source convention is supplied, Lambda leading terms still need "
                "the Frechet inverse-square-root operator at G0(0), hence q0(m), q0'(m), q0''(m)."
            ),
        },
        "minimal_compatibility_list": [
            "Decide whether M_i^[5] is allowed to be zero under this homogeneous source convention.",
            "If not, abandon grade a = derivative order k-2 for odd k in the mixed input.",
            "Supply a different scalar grade-five source piece or a non-homogeneous projection that has nonzero [z^5]M.",
            "Then compute Lambda leading coefficients using the baseline constant same-point block G0(0).",
        ],
    }

    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({
        "output": str(OUT),
        "sha1": digest,
        "homogeneous_candidate": candidate,
        "all_rows": rows,
        "hard_blocker": manifest["baseline_status"]["hard_blocker"],
    }, indent=2))


if __name__ == "__main__":
    main()
