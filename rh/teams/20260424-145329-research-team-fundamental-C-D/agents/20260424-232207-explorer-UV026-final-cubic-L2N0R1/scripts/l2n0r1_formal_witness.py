"""Formal witness for the UV-026 L2N0R1 / L1N0R2 cubic families.

This is not an actual corrected-package computation.  It checks only that
matrix algebra for

    L_2 N_0 R_1,   L_1 N_0 R_2

does not force the fixed-sector coefficient to lie in a prescribed
``C A_5^f`` line.  At an identity baseline, the mixed second-order coefficient
of (I + e A + d B)^(-1/2) is 3/8(AB + BA), and the first-order coefficient is
-C/2.  Their product can be non-gauge even before any scalar extraction.
"""

from __future__ import annotations

from fractions import Fraction
import json


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


def matadd(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0][0] + b[0][0], a[0][1] + b[0][1]),
        (a[1][0] + b[1][0], a[1][1] + b[1][1]),
    )


def scale(c: Fraction, a: Matrix) -> Matrix:
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def second_inverse_sqrt_coeff(a: Matrix, b: Matrix) -> Matrix:
    """Coefficient of e*d in (I + e*a + d*b)^(-1/2)."""
    return scale(Fraction(3, 8), matadd(matmul(a, b), matmul(b, a)))


def first_inverse_sqrt_coeff(c: Matrix) -> Matrix:
    """Coefficient of t in (I + t*c)^(-1/2)."""
    return scale(Fraction(-1, 2), c)


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
    same_point_c: Matrix = ((Fraction(3), Fraction(7)), (Fraction(7), Fraction(3)))

    # Formal tau1^2 tau2 source pattern: two same-point factors in L2 (or R2)
    # and one first-Frechet same-point factor on the opposite side.
    l2_coeff = second_inverse_sqrt_coeff(ident, ident)
    r2_coeff = second_inverse_sqrt_coeff(ident, ident)
    l1_coeff = first_inverse_sqrt_coeff(same_point_c)
    r1_coeff = first_inverse_sqrt_coeff(same_point_c)

    l2n0r1 = matmul(matmul(l2_coeff, ident), r1_coeff)
    l1n0r2 = matmul(matmul(l1_coeff, ident), r2_coeff)

    l2n0r1_vec = fixed_coords(l2n0r1)
    l1n0r2_vec = fixed_coords(l1n0r2)
    a5 = (Fraction(2), Fraction(5))

    output = {
        "scope": "formal matrix witness only; not an actual corrected-package coefficient",
        "matrix_level_convention": "baseline L0=N0=R0=I, fixed projection pi_f(A)=1/2(A+J0AJ0)",
        "tag_component": "tau1^2 tau2",
        "finite_grade_pattern": [1, 1, 5],
        "second_inverse_sqrt_coefficient": "3/8 times AB+BA",
        "first_inverse_sqrt_coefficient": "-C/2",
        "first_side_input_fixed_sector": ["3", "7"],
        "L2N0R1_fixed_sector": fmt_vec(l2n0r1_vec),
        "L1N0R2_fixed_sector": fmt_vec(l1n0r2_vec),
        "A5_fixed_sector": fmt_vec(a5),
        "det_L2N0R1_against_A5": fmt(det_against(l2n0r1_vec, a5)),
        "det_L1N0R2_against_A5": fmt(det_against(l1n0r2_vec, a5)),
        "algebra_forces_A5_gauge": det_against(l2n0r1_vec, a5) == 0
        and det_against(l1n0r2_vec, a5) == 0,
        "classification": "formal algebra does not classify L2N0R1 or L1N0R2 as A5-gauge; actual coefficient/source-class theorem is required",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
