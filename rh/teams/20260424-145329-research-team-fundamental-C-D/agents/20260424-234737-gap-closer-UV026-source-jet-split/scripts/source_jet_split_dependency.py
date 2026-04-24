#!/usr/bin/env python3
"""
UV-026 source-jet split audit.

This script records the finite source-jet constraints that follow from the
displayed source formulas, without assuming an unsourced finite-grade split.
It writes a compact JSON manifest used by the accompanying report.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "source_jet_split_dependency.json"


def add_poly(p, q):
    out = dict(p)
    for mon, coeff in q.items():
        out[mon] = out.get(mon, 0) + coeff
        if out[mon] == 0:
            del out[mon]
    return out


def mul_monomial(p, da, dx, coeff=1):
    return {
        (pa + da, px + dx): c * coeff
        for (pa, px), c in p.items()
        if c * coeff
    }


def deriv_x(p):
    out = {}
    for (pa, px), coeff in p.items():
        if px:
            out[(pa, px - 1)] = out.get((pa, px - 1), 0) + coeff * px
    return {mon: coeff for mon, coeff in out.items() if coeff}


def poly_to_string(p):
    if not p:
        return "0"
    terms = []
    for (pa, px), coeff in sorted(p.items(), key=lambda item: (-sum(item[0]), -item[0][1], -item[0][0])):
        pieces = []
        if pa == 1:
            pieces.append("a")
        elif pa:
            pieces.append(f"a^{pa}")
        if px == 1:
            pieces.append("x")
        elif px:
            pieces.append(f"x^{px}")
        mon = "*".join(pieces) if pieces else "1"
        terms.append((coeff, mon))

    rendered = []
    for index, (coeff, mon) in enumerate(terms):
        sign = "-" if coeff < 0 else "+"
        mag = abs(coeff)
        body = mon if mag == 1 and mon != "1" else f"{mag}" if mon == "1" else f"{mag}*{mon}"
        if index == 0:
            rendered.append(body if coeff > 0 else f"-{body}")
        else:
            rendered.append(f" {sign} {body}")
    return "".join(rendered)


def derivative_polynomials(max_k=9):
    # P_k is defined by d^k/dx^k (a^2+x^2)^(-1)
    # = P_k(a,x)/(a^2+x^2)^(k+1).
    polys = [{(0, 0): 1}]
    for k in range(max_k):
        pk = polys[-1]
        next_poly = add_poly(mul_monomial(deriv_x(pk), 2, 0), mul_monomial(deriv_x(pk), 0, 2))
        next_poly = add_poly(next_poly, mul_monomial(pk, 0, 1, coeff=-2 * (k + 1)))
        polys.append(next_poly)
    return polys


def main():
    polys = derivative_polynomials(9)
    derivative_formula = {
        "term": "F_a(t)=a/(a^2+(2*t-gamma)^2)",
        "variables": {"x": "2*m-gamma"},
        "formula": "F_a^(k)(m)=2^k*a*P_k(a,x)/(a^2+x^2)^(k+1)",
        "P_k": {str(k): poly_to_string(polys[k]) for k in range(10)},
        "source_atom_formula": (
            "f_{beta,gamma}^{(k)}(m)=F_{1-beta}^{(k)}(m)+F_beta^{(k)}(m)"
        ),
        "affine_removed_remainder": (
            "r_rho(m)=r_rho'(m)=0 and r_rho^(k)(m)=f_{beta,gamma}^{(k)}(m) for k>=2"
        ),
    }

    manifest = {
        "claim_scope": "pre-Phi_K source-jet constraints only; no finite-grade split assumed",
        "baseline_inputs_still_needed": [f"q0_{k}" for k in range(10)],
        "source_inputs_if_no_grade_split_theorem": [
            f"r{i}_grade{grade}_{k}"
            for i in (1, 2)
            for grade in (1, 5)
            for k in range(2, 10)
        ],
        "counts": {
            "baseline_q_derivatives": 10,
            "graded_source_derivatives_without_extra_theorem": 32,
            "prior_generator_total": 42,
            "ungraded_source_derivatives_per_atom": 8,
            "ungraded_source_atom_parameters_in_displayed_f_formula": ["beta", "gamma"],
        },
        "relations_for_any_scalar_germ_h_after_affine_removal": {
            "point_sample_plus_coeff_z_n": "h^(n)(m)/(n!*(2*Q^2)^n)",
            "point_sample_minus_coeff_z_n": "(-1)^n times the plus coefficient",
            "h_prime_minus_coeff_z_n": "(-1)^n times h_prime_plus coefficient",
            "h_second_minus_coeff_z_n": "(-1)^n times h_second_plus coefficient",
            "integral_eta_uses_only_even_h_derivatives": [2, 4, 6, 8],
            "integral_eta_k_to_z_power": "h^(k)(m) contributes to z^(k+1); odd k cancels",
        },
        "baseline_delta_relations": {
            "Delta0_uses_only_even_q0_derivatives_through_order_8": [0, 2, 4, 6, 8],
            "q0_plus_minus_point_tables_are_one_jet": "minus z^n coefficient is (-1)^n times plus for each derivative sample",
        },
        "conditional_witness_slice_reading": {
            "grade_1_candidate": {
                "source_slice": "eta_2",
                "supported_matrix_role": "X_1 off-diagonal input",
                "if_imported_to_scalar_r": "would be controlled by the quadratic source jet r^(2)(m)",
            },
            "higher_candidates": [
                {
                    "source_slice": "q^(5)",
                    "supported_matrix_role": "X_3 diagonal input in the quintic witness",
                    "if_imported_to_scalar_r": "would be controlled by r^(5)(m)",
                },
                {
                    "source_slice": "q^(7)",
                    "supported_matrix_role": "X_5 diagonal input in the direct septic witness",
                    "if_imported_to_scalar_r": "would be controlled by r^(7)(m)",
                },
            ],
            "status": "current source does not define r_i^[1] or r_i^[5] by any of these scalar projections",
        },
        "displayed_source_derivative_formula": derivative_formula,
        "missing_exact_substatements": [
            "Define Gr_1 and Gr_5 on the scalar source remainder r_i after midpoint-affine removal.",
            "State whether UV-026 grade 5 is the q^(5)/X_3 quintic slice, the q^(7)/X_5 septic slice, or a different pre-whitening mixed-block grading.",
            "Prove projection commutes with affine removal, so (r_i^[a])(m)=(r_i^[a])'(m)=0.",
            "Give formulas for q0^(k)(m), 0<=k<=9, in the same baseline normalization.",
            "Give formulas for (r_i^[a])^(k)(m), a in {1,5}, 2<=k<=9, or a projection rule from the displayed f_{beta,gamma} derivatives.",
        ],
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({
        "output": str(OUT),
        "sha1": digest,
        "prior_generator_total_inputs": manifest["counts"]["prior_generator_total"],
        "ungraded_source_formula": derivative_formula["source_atom_formula"],
        "missing_grade_split": manifest["missing_exact_substatements"][0],
    }, indent=2))


if __name__ == "__main__":
    main()
