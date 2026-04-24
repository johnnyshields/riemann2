"""Formal witness for the UV-026 L2YR0 / L0YR2 cubic families.

This is not an actual corrected-package computation.  It checks only that
matrix algebra for

    L_2 Y R_0,   L_0 Y R_2

does not force the fixed-sector coefficient to lie in a prescribed
``C A_5^f`` line.  At an identity baseline, the mixed coefficient of
(I + e A + d B)^(-1/2) is 3/8(AB + BA).  Multiplication by a source-linear
mixed input Y can therefore produce a non-gauge fixed-sector vector.
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
    mixed_y: Matrix = ((Fraction(3), Fraction(7)), (Fraction(7), Fraction(3)))

    # Formal tau1^2 tau2 source pattern: two same-point factors in L2 and one
    # mixed source input Y.  The finite-grade assignment is represented only by
    # labels; the matrix check tests algebraic gauge forcing, not source values.
    l2_coeff = second_inverse_sqrt_coeff(ident, ident)
    r2_coeff = second_inverse_sqrt_coeff(ident, ident)

    l2yr0 = matmul(matmul(l2_coeff, mixed_y), ident)
    l0yr2 = matmul(matmul(ident, mixed_y), r2_coeff)

    l2_vec = fixed_coords(l2yr0)
    r2_vec = fixed_coords(l0yr2)
    a5 = (Fraction(2), Fraction(5))

    output = {
        "scope": "formal matrix witness only; not an actual corrected-package coefficient",
        "matrix_level_convention": "baseline L0=N0=R0=I, fixed projection pi_f(A)=1/2(A+J0AJ0)",
        "tag_component": "tau1^2 tau2",
        "finite_grade_pattern": [1, 1, 5],
        "second_inverse_sqrt_coefficient": "3/8 times AB+BA",
        "mixed_input_Y_fixed_sector": ["3", "7"],
        "L2YR0_fixed_sector": fmt_vec(l2_vec),
        "L0YR2_fixed_sector": fmt_vec(r2_vec),
        "A5_fixed_sector": fmt_vec(a5),
        "det_L2YR0_against_A5": fmt(det_against(l2_vec, a5)),
        "det_L0YR2_against_A5": fmt(det_against(r2_vec, a5)),
        "algebra_forces_A5_gauge": det_against(l2_vec, a5) == 0
        and det_against(r2_vec, a5) == 0,
        "classification": "formal algebra does not classify L2YR0 or L0YR2 as A5-gauge; actual coefficient/source-class theorem is required",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
