#!/usr/bin/env python3
"""
UV-026 parity-corrected grade compatibility test.

This script tests candidate meanings of M_i^[5] against two finite facts:

1. Under the common scalar mixed-order filtration, a scalar Taylor derivative
   r^(k)(m) has same-point leading order k-2 via the g=r'' channel.
2. The exact mixed parity audit found [z^5]M support only from r2,r4,r6.

It does not prove determinant identities.  It checks whether a nonzero
parity-corrected [z^5]M_i^[5] can coexist with Lambda^[1] under one common
scalar grade split r=sum Gr_a r.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEAM = ROOT.parents[1]
PREV = (
    TEAM
    / "agents"
    / "20260425-002114-gap-closer-UV026-mixed-parity-theorem"
    / "notes"
    / "mixed_parity_audit.json"
)
OUT = ROOT / "notes" / "parity_corrected_grade_test.json"


def derivative_index(symbol: str) -> int:
    assert symbol.startswith("r"), symbol
    return int(symbol[1:])


def same_point_grade_for_source_derivative(k: int) -> int:
    # Source: same-point linear (2,2) channel has g=r'', so r^(k)
    # first appears in ordinary z order k-2.
    return k - 2


def main() -> None:
    mixed_audit = json.loads(PREV.read_text(encoding="utf-8"))
    by_source = mixed_audit["powers_by_source_derivative"]
    z5_sources = sorted(
        source
        for source, entries in by_source.items()
        if any(5 in powers for powers in entries.values())
    )
    z5_source_derivative_orders = [derivative_index(source) for source in z5_sources]

    homogeneous_grade_1 = ["r3"]
    homogeneous_grade_5 = ["r7"]
    homogeneous_m5_z5_sources = [
        source for source in homogeneous_grade_5 if source in z5_sources
    ]

    parity_corrected_conflicts = {
        source: {
            "source_derivative_order": derivative_index(source),
            "same_point_scalar_grade": same_point_grade_for_source_derivative(
                derivative_index(source)
            ),
            "requested_mixed_label": 5,
            "conflict": same_point_grade_for_source_derivative(
                derivative_index(source)
            )
            != 5,
        }
        for source in z5_sources
    }

    same_point_grade_5_sources = [
        f"r{k}" for k in range(2, 10) if same_point_grade_for_source_derivative(k) == 5
    ]
    lambda_grade_1_sources = [
        f"r{k}" for k in range(2, 10) if same_point_grade_for_source_derivative(k) == 1
    ]

    manifest = {
        "input_manifest": str(PREV),
        "scope": "ordinary-z, pre-Phi_K compatibility of M^[5] with Lambda^[1]",
        "source_facts": {
            "same_point_grade_rule": "r^(k)(m) first appears in delta G^lin at z^(k-2)",
            "lambda_grade_1_sources_under_common_scalar_grade": lambda_grade_1_sources,
            "same_point_grade_5_sources_under_common_scalar_grade": same_point_grade_5_sources,
            "mixed_z5_sources_from_exact_parity_audit": z5_sources,
            "mixed_z5_source_derivative_orders": z5_source_derivative_orders,
        },
        "candidate_conventions": {
            "homogeneous_common_scalar_grade": {
                "meaning": "Gr_a r = r^(a+2)(m)(t-m)^(a+2)/(a+2)!",
                "Gr_1_sources": homogeneous_grade_1,
                "Gr_5_sources": homogeneous_grade_5,
                "M5_has_z5_source": bool(homogeneous_m5_z5_sources),
                "M5_z5_sources": homogeneous_m5_z5_sources,
                "L1YR1_at_B7": "absent",
                "reason": "common scalar Gr_5 uses r7, but r7 has no z5 mixed support",
            },
            "actual_mixed_order_5_projection": {
                "meaning": "M^[5] means the z^5 coefficient/projection of the full mixed input",
                "M5_sources": z5_sources,
                "coexists_with_common_scalar_grade": False,
                "conflicts": parity_corrected_conflicts,
                "reason": "r2,r4,r6 are scalar grades 0,2,4 by the same-point rule",
            },
            "parity_corrected_nonhomogeneous_source_projection": {
                "meaning": "declare Gr_5^M to include exactly the source combination producing [z^5]M",
                "M5_sources": z5_sources,
                "coexists_with_Lambda1_only_as_block_dependent_grade": True,
                "coexists_with_single_scalar_split_r_equals_sum_Gr_a_r": False,
                "required_new_theorem": (
                    "separate mixed-output grade projection and proof that using "
                    "r2,r4,r6 in M^[5] does not consume or duplicate grade 0,2,4 "
                    "same-point/Frechet sectors"
                ),
            },
        },
        "decision": {
            "cleanest_source_supported_convention": "homogeneous_common_scalar_grade",
            "positive_parity_corrected_M5_supported_from_current_source": False,
            "L1YR1_absent_at_B7_under_homogeneous_convention": True,
            "next_affected_gate": "L_2YR_0 / L_0YR_2",
            "next_gate_reason": (
                "these are the next Y-containing cubic families; they require "
                "second-Frechet tables plus the same mixed-input convention"
            ),
        },
    }

    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(
        json.dumps(
            {
                "output": str(OUT),
                "sha1": digest,
                "z5_sources": z5_sources,
                "decision": manifest["decision"],
                "conflicts": parity_corrected_conflicts,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
