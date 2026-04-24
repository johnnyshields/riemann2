#!/usr/bin/env python3
"""Coefficient gate for the UV-026 L_1YR_1 subtarget.

This script does not fabricate source coefficients.  It records the exact
finite convolution and the Frechet inverse-square-root coefficient recurrence
needed to turn source coefficient lists into the two fixed-sector vectors
C_112 and C_122.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ORDER = 7


def convolution_triples(order: int = ORDER) -> list[list[int]]:
    return [[r, s, order - r - s] for r in range(order + 1) for s in range(order + 1 - r)]


def lambda_recurrence(sign: str, r: int) -> str:
    """Return the coefficient recurrence for Lambda_{i,sign}^{[r]}."""
    left = f"S_{{{sign},0}} Lambda_{{i,{sign},{r}}} + Lambda_{{i,{sign},{r}}} S_{{{sign},0}}"
    b_terms = (
        f"sum_{{a+b+c={r}}} B_{{{sign},a}} H_{{i,{sign},b}} B_{{{sign},c}}"
    )
    if r == 0:
        rhs = f"- {b_terms}"
    else:
        rhs = (
            f"- {b_terms} - "
            f"sum_{{a=1..{r}}}(S_{{{sign},a}} Lambda_{{i,{sign},r-a}} "
            f"+ Lambda_{{i,{sign},r-a}} S_{{{sign},a}})"
        )
    return f"solve Sylvester({left} = {rhs})"


def source_formulas() -> dict[str, str]:
    return {
        "deltaG_lin": (
            "H_{i,pm}=delta G_{i,pm}^{lin}=(1/pi)[[2 d_{i,pm}, (1/2)e_{i,pm}], "
            "[(1/2)e_{i,pm}, (1/12)(g_{i,pm}+6 q_{0,pm}^2 d_{i,pm})]]"
        ),
        "mixed_linear_before_grade_projection": (
            "Let s=z/Q^2, c0=cos(Delta_0), s0=sin(Delta_0). "
            "delta N_i^{lin}=(1/pi)[[ -2 c0 eta_i/s, "
            "(c0 eta_i + s c0 d_{i,+} - s q_{0,+} s0 eta_i)/s^2 ], "
            "[ -(c0 eta_i + s c0 d_{i,-} - s q_{0,-} s0 eta_i)/s^2, "
            "((s c0-s^2 q_{0,+} s0)d_{i,-} + (s c0-s^2 q_{0,-} s0)d_{i,+} "
            "+ (-(q_{0,-}+q_{0,+})s s0 + (2-q_{0,-}q_{0,+}s^2)c0) eta_i)/(2s^3) ]]"
        ),
        "M5_definition_needed": (
            "M_i^{[5]} must be the grade-5 component of the mixed input in the same "
            "normalization used in B_7^f.  If the weighted input Y=mathfrak D_Q(delta N) "
            "is intended, apply mathfrak D_Q before taking grade 5; if the actual "
            "matrix delta N is intended, do not.  The present source names M_i^{[5]} "
            "but does not fix this coefficient list."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, help="write JSON summary to this path")
    args = parser.parse_args()

    triples = convolution_triples()
    c112_terms = [
        ["Lambda_1,-", "M_1^[5]", "Lambda_2,+"],
        ["Lambda_1,-", "M_2^[5]", "Lambda_1,+"],
        ["Lambda_2,-", "M_1^[5]", "Lambda_1,+"],
    ]
    c122_terms = [
        ["Lambda_1,-", "M_2^[5]", "Lambda_2,+"],
        ["Lambda_2,-", "M_1^[5]", "Lambda_2,+"],
        ["Lambda_2,-", "M_2^[5]", "Lambda_1,+"],
    ]

    script_sha1 = hashlib.sha1(Path(__file__).read_bytes()).hexdigest().upper()
    data = {
        "script_sha1": script_sha1,
        "order": ORDER,
        "ordinary_z_coefficients_needed": {
            "Lambda_indices": {"i": [1, 2], "sign": ["-", "+"], "r": list(range(ORDER + 1))},
            "M5_indices": {"i": [1, 2], "s": list(range(ORDER + 1))},
            "matrix_counts": {"Lambda": 32, "M5": 16, "total": 48},
        },
        "convolution_triples_r_s_t_for_z7": triples,
        "triple_count_per_ordered_product": len(triples),
        "ordered_product_count_per_tag_vector": 3,
        "matrix_products_per_tag_vector": 3 * len(triples),
        "C112_ordered_products": c112_terms,
        "C122_ordered_products": c122_terms,
        "C112_formula": (
            "pi_f sum_{r+s+t=7}(Lambda_{1,-,r} M_{1,s}^{[5]} Lambda_{2,+,t} "
            "+ Lambda_{1,-,r} M_{2,s}^{[5]} Lambda_{1,+,t} "
            "+ Lambda_{2,-,r} M_{1,s}^{[5]} Lambda_{1,+,t})"
        ),
        "C122_formula": (
            "pi_f sum_{r+s+t=7}(Lambda_{1,-,r} M_{2,s}^{[5]} Lambda_{2,+,t} "
            "+ Lambda_{2,-,r} M_{1,s}^{[5]} Lambda_{2,+,t} "
            "+ Lambda_{2,-,r} M_{2,s}^{[5]} Lambda_{1,+,t})"
        ),
        "Lambda_recurrence": {
            sign: [lambda_recurrence(sign, r) for r in range(ORDER + 1)]
            for sign in ["-", "+"]
        },
        "source_formulas": source_formulas(),
        "missing_source_data_for_positive_gate": [
            "[z^0..z^7] coefficients B_{pm,a} of G_pm^(0)(z)^(-1/2)",
            "[z^0..z^7] coefficients S_{pm,a} of G_pm^(0)(z)^(1/2)",
            "[z^0..z^7] coefficients of H_{i,pm}=delta G_{i,pm}^{lin} after substituting the tagged one-atom kernels",
            "[z^0..z^7] coefficients of the grade-5 mixed input M_i^{[5]} in the B_7^f normalization",
            "coordinates u_5,v_5 of A_5^f(m) in the same fixed-sector basis",
        ],
        "determinant_tests_after_coefficients_exist": [
            "write C112=u112 I+v112 S and check u112*v5-u5*v112=0",
            "write C122=u122 I+v122 S and check u122*v5-u5*v122=0",
        ],
    }

    text = json.dumps(data, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
