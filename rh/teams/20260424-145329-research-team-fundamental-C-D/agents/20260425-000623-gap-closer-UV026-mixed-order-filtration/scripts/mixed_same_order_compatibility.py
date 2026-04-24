#!/usr/bin/env python3
"""
UV-026 mixed-order scalar filtration compatibility audit.

For an affine-removed scalar source Taylor monomial with first nonzero
derivative order k, compare the lowest ordinary-z orders in:
  * same-point linear input delta G,
  * scaled mixed input M = D_Q delta N.

This is an order audit only; Q powers and baseline coefficients are not used to
claim determinant identities.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "mixed_same_order_compatibility.json"


def eta_order(k: int) -> int | None:
    return k + 1 if k % 2 == 0 else None


def min_present(values):
    values = [v for v in values if v is not None]
    return min(values) if values else None


def same_point_orders(k: int):
    # Linear same-point formula:
    # delta G_11 ~ d, delta G_12 ~ e, delta G_22 ~ g + baseline*d.
    return {
        "11_from_d": k,
        "12_from_e": k - 1,
        "21_from_e": k - 1,
        "22_from_g": k - 2,
        "22_from_baseline_times_d": k,
        "lowest_deltaG_order": k - 2,
        "leading_entry": "22_from_g",
    }


def mixed_orders(k: int):
    d = k
    eta = eta_order(k)
    return {
        "11_from_eta_over_s": None if eta is None else eta - 1,
        "12_from_d_over_s": d - 1,
        "12_from_eta_over_s2": None if eta is None else eta - 2,
        "21_from_d_over_s": d - 1,
        "21_from_eta_over_s2": None if eta is None else eta - 2,
        "22_from_d_over_s2": d - 2,
        "22_from_eta_over_s3": None if eta is None else eta - 3,
        "lowest_M_order": min_present([
            None if eta is None else eta - 1,
            d - 1,
            None if eta is None else eta - 2,
            d - 2,
            None if eta is None else eta - 3,
        ]),
        "leading_entry": "22_from_d_over_s2" if k % 2 else "22_from_d_over_s2 and 22_from_eta_over_s3",
    }


def candidate_grade(a: int):
    k = a + 2
    return {
        "grade": a,
        "scalar_derivative_order": k,
        "candidate_projection": f"Gr_{a} r keeps r^({k})(m)*(t-m)^{k}/{k}!",
        "same_point": same_point_orders(k),
        "mixed": mixed_orders(k),
        "same_and_mixed_lowest_orders_match": same_point_orders(k)["lowest_deltaG_order"] == mixed_orders(k)["lowest_M_order"] == a,
    }


def main():
    rows = []
    for k in range(2, 10):
        sg = same_point_orders(k)
        mm = mixed_orders(k)
        rows.append({
            "k": k,
            "same_point_lowest_deltaG_order": sg["lowest_deltaG_order"],
            "same_point_leading_entry": sg["leading_entry"],
            "mixed_lowest_M_order": mm["lowest_M_order"],
            "mixed_leading_entry": mm["leading_entry"],
            "eta_present": eta_order(k) is not None,
            "compatible_order": sg["lowest_deltaG_order"] == mm["lowest_M_order"],
        })

    manifest = {
        "scope": "ordinary-z order compatibility for pre-Phi_K source-linear inputs",
        "candidate_definition": "For a in {1,5}, Gr_a r is the homogeneous Taylor piece with scalar derivative order k=a+2.",
        "order_rule": "For every k>=2, both deltaG_lin and scaled M first see the scalar derivative in order k-2.",
        "rows": rows,
        "candidate_grades": {
            "1": candidate_grade(1),
            "5": candidate_grade(5),
        },
        "compatibility_verdict": {
            "formal_order_compatible_with_same_point_inputs": True,
            "formal_order_compatible_with_mixed_inputs": True,
            "witness_slice_mismatch": (
                "Grade 1 in this mixed-order filtration is r^(3), not the eta_2/r^(2) witness slice; "
                "therefore it needs a new source theorem and does not inherit the existing eta_2/X_1 witness."
            ),
            "missing_for_promotion": [
                "Declare whether Gr_a is exact homogeneous Taylor projection or cumulative filtration quotient.",
                "Prove that UV-026 finite grade 1/5 refers to this pre-whitening order, not witness eta_2/q^(5)/q^(7) labels.",
                "Prove k=2 grade-0 contributions are excluded from the (1,1,5) gates or already handled elsewhere.",
                "Supply baseline q0 jets and run Stage 1/Frechet/determinant tests.",
            ],
        },
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({
        "output": str(OUT),
        "sha1": digest,
        "candidate_grade_1": manifest["candidate_grades"]["1"],
        "candidate_grade_5": manifest["candidate_grades"]["5"],
        "all_rows_order_compatible": all(row["compatible_order"] for row in rows),
    }, indent=2))


if __name__ == "__main__":
    main()
