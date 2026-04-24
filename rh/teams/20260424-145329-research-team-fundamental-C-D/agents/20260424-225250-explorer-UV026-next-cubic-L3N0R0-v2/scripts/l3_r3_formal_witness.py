"""Formal witness for the UV-026 all-left/all-right cubic families.

This is not an actual-package computation.  It checks the matrix-level
algebraic obstruction to proving the families

    L_3 N_0 R_0,   L_0 N_0 R_3

from source support alone.  At a diagonal identity baseline, the cubic
coefficient of (I + E)^(-1/2) is -5/16 E^3.  A non-(1,1) tagged
grade (1,1,5) input can therefore produce a fixed-sector vector not lying in a
chosen A_5^f line.
"""

from __future__ import annotations

from fractions import Fraction
import json
from itertools import permutations


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def matadd(*items: Matrix) -> Matrix:
    return (
        (sum(item[0][0] for item in items), sum(item[0][1] for item in items)),
        (sum(item[1][0] for item in items), sum(item[1][1] for item in items)),
    )


def scale(c: Fraction, a: Matrix) -> Matrix:
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def sym_cubic_coeff(a: Matrix, b: Matrix, c: Matrix) -> Matrix:
    """Coefficient of abc in the cubic term of (I + E)^(-1/2)."""
    terms = [matmul(matmul(x, y), z) for x, y, z in permutations((a, b, c))]
    return scale(Fraction(-5, 16), matadd(*terms))


def fixed_coords(m: Matrix) -> tuple[Fraction, Fraction]:
    """Coordinates of pi_f(m) in span {I,S}."""
    u = Fraction(1, 2) * (m[0][0] + m[1][1])
    v = Fraction(1, 2) * (m[0][1] + m[1][0])
    return u, v


def det_against(vec: tuple[Fraction, Fraction], a5: tuple[Fraction, Fraction]) -> Fraction:
    return vec[0] * a5[1] - a5[0] * vec[1]


def fmt(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def fmt_vec(vec: tuple[Fraction, Fraction]) -> list[str]:
    return [fmt(vec[0]), fmt(vec[1])]


def main() -> None:
    ident: Matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))

    # Non-(1,1) tag tau1^2 tau2 with finite grades (1,5,1).
    h_1_grade_1 = ident
    h_1_grade_5 = ident
    h_2_grade_1 = ident

    l3_coeff = sym_cubic_coeff(h_1_grade_1, h_1_grade_5, h_2_grade_1)
    r3_coeff = sym_cubic_coeff(h_1_grade_1, h_1_grade_5, h_2_grade_1)

    # Identity source-free baselines N0 R0 and L0 N0 keep the same coefficient.
    l3_vec = fixed_coords(l3_coeff)
    r3_vec = fixed_coords(r3_coeff)
    a5 = (Fraction(2), Fraction(5))

    output = {
        "scope": "formal matrix witness only; not an actual corrected-package coefficient",
        "matrix_level_convention": "baseline L0=N0=R0=I, fixed projection pi_f(A)=1/2(A+J0AJ0)",
        "tag_component": "tau1^2 tau2",
        "finite_grade_pattern": [1, 1, 5],
        "cubic_inverse_sqrt_coefficient": "-5/16 times the ordered cubic product sum",
        "L3N0R0_fixed_sector": fmt_vec(l3_vec),
        "L0N0R3_fixed_sector": fmt_vec(r3_vec),
        "A5_fixed_sector": fmt_vec(a5),
        "det_L3_against_A5": fmt(det_against(l3_vec, a5)),
        "det_R3_against_A5": fmt(det_against(r3_vec, a5)),
        "algebra_forces_A5_gauge": det_against(l3_vec, a5) == 0
        and det_against(r3_vec, a5) == 0,
        "classification": "formal algebra does not classify L3N0R0 or L0N0R3 as A5-gauge; actual coefficient/source-class theorem is required",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
