"""Formal UV-026 L1YR1 gauge check.

This is not an actual corrected-source coefficient computation.  It tests the
weaker algebraic question needed by the report: whether the matrix-level form

    D(G_-^{-1/2})[X_-] * Y * D(G_+^{-1/2})[X_+]

forces the fixed-sector coefficient to lie in C A5^f before actual source
coefficient restrictions are imposed.  A diagonal positive baseline makes the
Loewner Frechet derivative entrywise invertible, so arbitrary first derivative
outputs can be realized formally.
"""

from fractions import Fraction
import hashlib
from pathlib import Path


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def fixed_sector(M):
    """Projection onto span{I,S}: return coefficients (I,S)."""
    return ((M[0][0] + M[1][1]) / 2, (M[0][1] + M[1][0]) / 2)


def det_pair(u, v):
    return u[0] * v[1] - u[1] * v[0]


def f_inv_sqrt(x):
    return Fraction(1, 1) if x == 1 else Fraction(1, 3)


def loewner_coeffs_for_inv_sqrt(lambdas):
    coeffs = []
    for i, li in enumerate(lambdas):
        row = []
        for j, lj in enumerate(lambdas):
            if i == j:
                # d/dx x^{-1/2} at x=1 or x=9.
                row.append(Fraction(-1, 2) if li == 1 else Fraction(-1, 54))
            else:
                row.append((f_inv_sqrt(li) - f_inv_sqrt(lj)) / (li - lj))
        coeffs.append(row)
    return coeffs


def invertible_entrywise(coeffs):
    return all(c != 0 for row in coeffs for c in row)


def elementwise_preimage(target, coeffs):
    return [
        [target[i][j] / coeffs[i][j] for j in range(2)]
        for i in range(2)
    ]


def main():
    I = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    S = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]

    A5 = (Fraction(2), Fraction(5))

    # Formal witness: choose first derivative outputs L=I and R=I, and a
    # grade-5 middle coefficient whose fixed-sector part is not parallel to A5.
    L1 = I
    R1 = I
    Y5 = [
        [Fraction(3), Fraction(7)],
        [Fraction(7), Fraction(3)],
    ]

    product = matmul(matmul(L1, Y5), R1)
    coeff = fixed_sector(product)
    determinant = det_pair(coeff, A5)

    lambdas = [Fraction(1), Fraction(9)]
    loewner = loewner_coeffs_for_inv_sqrt(lambdas)
    preimage_L = elementwise_preimage(L1, loewner)
    preimage_R = elementwise_preimage(R1, loewner)

    print("A5_fixed_sector =", tuple(map(str, A5)))
    print("L1YR1_fixed_sector =", tuple(map(str, coeff)))
    print("det(L1YR1_fixed_sector, A5) =", determinant)
    print("loewner_coefficients =", [[str(x) for x in row] for row in loewner])
    print("loewner_entrywise_invertible =", invertible_entrywise(loewner))
    print("one_preimage_for_L1 =", [[str(x) for x in row] for row in preimage_L])
    print("one_preimage_for_R1 =", [[str(x) for x in row] for row in preimage_R])
    print(
        "conclusion = formal L1YR1 algebra does not force "
        "C*A5^f proportionality without actual source coefficient constraints"
    )

    digest = hashlib.sha1(Path(__file__).read_bytes()).hexdigest().upper()
    print("script_sha1 =", digest)


if __name__ == "__main__":
    main()
