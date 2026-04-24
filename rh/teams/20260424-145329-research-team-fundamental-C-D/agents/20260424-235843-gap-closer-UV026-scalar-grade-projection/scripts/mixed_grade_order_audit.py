#!/usr/bin/env python3
"""
Order audit for UV-026 scalar grade projection.

The source mixed-block formula has entries divided by s, s^2, and s^3.
For a scalar affine-removed source monomial whose first nonzero midpoint
derivative is order k, this script records the lowest possible z-order in the
linearized scaled mixed input M = D_Q delta N.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "mixed_grade_order_audit.json"


def eta_order(k: int) -> int | None:
    # eta = integral from +a to -a of (u-m)^k du.  It vanishes for odd k and
    # has z^(k+1) order for even k.
    return k + 1 if k % 2 == 0 else None


def min_ignore_none(values):
    values = [value for value in values if value is not None]
    return min(values) if values else None


def orders_for_k(k: int):
    d_order = k
    e_order = k - 1
    g_order = k - 2
    eta = eta_order(k)

    # Linearized mixed-block orders from the displayed formula:
    # N11: eta / s.
    # N12,N21: eta / s^2 and d*s / s^2 = d/s.
    # N22: eta / s^3 and d*s / s^3 = d/s^2.
    # D_Q introduces Q factors but no z-order shift.
    m11 = None if eta is None else eta - 1
    m12 = min_ignore_none([None if eta is None else eta - 2, d_order - 1])
    m21 = m12
    m22 = min_ignore_none([None if eta is None else eta - 3, d_order - 2])

    return {
        "scalar_derivative_order_k": k,
        "source_point_orders": {"d": d_order, "e": e_order, "g": g_order, "eta": eta},
        "scaled_mixed_M_lowest_orders": {"11": m11, "12": m12, "21": m21, "22": m22},
        "lowest_M_order": min_ignore_none([m11, m12, m21, m22]),
    }


def main():
    rows = [orders_for_k(k) for k in range(2, 10)]
    by_lowest = {str(row["scalar_derivative_order_k"]): row["lowest_M_order"] for row in rows}
    manifest = {
        "scope": "linearized scaled mixed input M = D_Q delta N, z-order only",
        "source_formula_refs": [
            "proof_of_rh.tex:2724-2787 mixed block and linear Taylor expansion",
            "proof_of_rh.tex:12657-12659 grade-five mixed input M_i^[5]",
        ],
        "rule": "a scalar source derivative of order k can first enter M in z-order k-2 through the (2,2) entry",
        "k_to_lowest_M_order": by_lowest,
        "candidate_decision": {
            "q^(5)_scalar_derivative_k": 5,
            "q^(5)_lowest_M_order": by_lowest["5"],
            "q^(7)_scalar_derivative_k": 7,
            "q^(7)_lowest_M_order": by_lowest["7"],
            "grade_5_if_grade_means_lowest_M_z_order": "q^(7), not q^(5)",
        },
        "rows": rows,
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({
        "output": str(OUT),
        "sha1": digest,
        "k_to_lowest_M_order": by_lowest,
        "grade5_candidate": manifest["candidate_decision"],
    }, indent=2))


if __name__ == "__main__":
    main()
