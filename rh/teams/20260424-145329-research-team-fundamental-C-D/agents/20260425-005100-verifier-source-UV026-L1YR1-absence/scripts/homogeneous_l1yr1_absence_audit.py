"""Order audit for the homogeneous UV-026 L_1YR_1 absence theorem.

The script records the source-order implications of the inspected formulas:
under Gr_a r = r^(a+2)(m)(t-m)^(a+2)/(a+2)!, the Lambda^[1] same-point input
from r^(3) starts at z^1, while the mixed input induced by r^(7) starts at z^6
because the leading mixed diagonal channel cancels for odd source monomials.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "homogeneous_l1yr1_absence_audit.json"


def sha1(path: Path) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def source_orders(k: int) -> dict:
    """Return lowest ordinary-z orders for a pure derivative r^(k) monomial."""
    same_point_order = k - 2  # via g=r''
    if k % 2 == 1:
        mixed_order = k - 1  # M22 leading channel cancels; off-diagonal d/s remains
        mixed_reason = "odd monomial: eta=0 and d_-+d_+=0; first mixed channel is off-diagonal d/s"
    else:
        mixed_order = k - 2
        mixed_reason = "even monomial: diagonal M22 channel survives"
    return {
        "source_derivative": f"r^{k}",
        "same_point_deltaG_lowest_order": same_point_order,
        "mixed_M_lowest_order": mixed_order,
        "mixed_reason": mixed_reason,
    }


lambda_grade_1 = source_orders(3)
mixed_grade_5 = source_orders(7)

product_min_order = (
    lambda_grade_1["same_point_deltaG_lowest_order"]
    + mixed_grade_5["mixed_M_lowest_order"]
    + lambda_grade_1["same_point_deltaG_lowest_order"]
)

manifest = {
    "scope": "pre-Phi_K ordinary-z order audit for homogeneous L_1YR_1",
    "homogeneous_grade_rule": "Gr_a r keeps r^(a+2)(m)*(t-m)^(a+2)/(a+2)!",
    "Lambda_grade_1_source": lambda_grade_1,
    "M_grade_5_source": mixed_grade_5,
    "M5_has_z5_coefficient": mixed_grade_5["mixed_M_lowest_order"] <= 5,
    "L1YR1_min_order": product_min_order,
    "L1YR1_has_z7_contribution": product_min_order <= 7,
    "verdict": "absent at z^7 under homogeneous scalar grade" if product_min_order > 7 else "not absent",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "output": str(OUT),
    "script_sha1": sha1(Path(__file__).resolve()),
    "output_sha1": sha1(OUT),
    "M5_has_z5_coefficient": manifest["M5_has_z5_coefficient"],
    "L1YR1_min_order": product_min_order,
    "L1YR1_has_z7_contribution": manifest["L1YR1_has_z7_contribution"],
    "verdict": manifest["verdict"],
}, indent=2))
