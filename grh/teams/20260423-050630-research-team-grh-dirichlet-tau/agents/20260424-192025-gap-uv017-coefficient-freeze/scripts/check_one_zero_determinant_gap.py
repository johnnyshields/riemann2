"""Exact check for the UV-017 one-zero determinant gap.

Target:
    D[q] = 2 q q'' + 4 q^4 - 3 (q')^2,

where derivatives are with respect to t and

    q(t) = K_{beta,gamma}(t)
         = (1-beta)/((1-beta)^2 + (2t-gamma)^2)
           + beta/(beta^2 + (2t-gamma)^2).

Put x = 2t-gamma, y = x^2, and c = beta(1-beta).  Since
0 < beta < 1, one has 0 < c <= 1/4 and y >= 0.  The kernel becomes

    Q(y) = (y+c)/(y^2 + (1-2c)y + c^2).

This script performs exact rational polynomial arithmetic in c and y, clears
denominators, prints the numerator coefficients, and checks the elementary
positive-coefficient decomposition used in the report.
"""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path


# A polynomial is a dict {(c_power, y_power): Fraction coefficient}.


def clean(poly):
    return {k: v for k, v in poly.items() if v}


def mon(c_power=0, y_power=0, coeff=1):
    return clean({(c_power, y_power): Fraction(coeff)})


def add(a, b):
    out = dict(a)
    for key, val in b.items():
        out[key] = out.get(key, Fraction(0)) + val
    return clean(out)


def neg(a):
    return {key: -val for key, val in a.items()}


def sub(a, b):
    return add(a, neg(b))


def scale(a, scalar):
    scalar = Fraction(scalar)
    return clean({key: scalar * val for key, val in a.items()})


def mul(a, b):
    out = {}
    for (ci, yi), ai in a.items():
        for (cj, yj), bj in b.items():
            key = (ci + cj, yi + yj)
            out[key] = out.get(key, Fraction(0)) + ai * bj
    return clean(out)


def pow_poly(a, n):
    out = mon()
    for _ in range(n):
        out = mul(out, a)
    return out


def deriv_y(a):
    out = {}
    for (ci, yi), coeff in a.items():
        if yi:
            out[(ci, yi - 1)] = out.get((ci, yi - 1), Fraction(0)) + coeff * yi
    return clean(out)


def coeffs_by_y(poly):
    max_y = max((yi for _, yi in poly), default=0)
    coeffs = []
    for yi in range(max_y, -1, -1):
        coeff = {(ci, 0): val for (ci, yj), val in poly.items() if yj == yi}
        coeffs.append((yi, coeff))
    return coeffs


def c_poly_to_str(poly):
    if not poly:
        return "0"
    terms = []
    # poly entries have y_power 0 here.
    for (ci, _), coeff in sorted(poly.items(), key=lambda item: item[0][0], reverse=True):
        if coeff == 1 and ci:
            base = ""
        elif coeff == -1 and ci:
            base = "-"
        else:
            base = str(coeff)
        if ci == 0:
            term = base or "1"
        elif ci == 1:
            term = f"{base}c"
        else:
            term = f"{base}c^{ci}"
        terms.append(term)
    out = terms[0]
    for term in terms[1:]:
        if term.startswith("-"):
            out += " - " + term[1:]
        else:
            out += " + " + term
    return out


def eval_poly(poly, c_val, y_val):
    c_val = Fraction(c_val)
    y_val = Fraction(y_val)
    total = Fraction(0)
    for (ci, yi), coeff in poly.items():
        total += coeff * (c_val**ci) * (y_val**yi)
    return total


def main():
    # h = y^2 + (1-2c)y + c^2, n = y+c.
    y = mon(0, 1)
    c = mon(1, 0)
    one = mon()
    n = add(y, c)
    h = add(add(pow_poly(y, 2), mul(sub(one, scale(c, 2)), y)), pow_poly(c, 2))

    # Q_y = u/h^2, Q_yy = v/h^3.
    u = sub(mul(deriv_y(n), h), mul(n, deriv_y(h)))
    v = sub(mul(deriv_y(u), h), scale(mul(u, deriv_y(h)), 2))

    # D = 16 Q Q_y + 32 y Q Q_yy + 4 Q^4 - 48 y Q_y^2
    # after x=2t-gamma, y=x^2.  Clearing h^4 gives P below.
    P = add(
        add(scale(mul(mul(n, u), h), 16), scale(mul(mul(mul(y, n), v), one), 32)),
        add(scale(pow_poly(n, 4), 4), scale(mul(y, pow_poly(u, 2)), -48)),
    )

    # Polynomial factorization over u=sqrt(c):
    #
    # P = -12(1-4c)
    #       (y^2 + 2(u-c)y + c^2)
    #       (y^2 - 2(u+c)y + c^2).
    #
    # The script checks this by substituting c=u^2 and comparing exact
    # bivariate polynomials in u and y.
    u = mon(1, 0)
    # Reuse the same polynomial functions, now with the first variable named u.
    c_as_u2 = pow_poly(u, 2)
    y_u = y
    P_u = {}
    for (ci, yi), coeff in P.items():
        P_u[(2 * ci, yi)] = P_u.get((2 * ci, yi), Fraction(0)) + coeff
    P_u = clean(P_u)
    factorized_u = scale(
        mul(
            sub(one, scale(c_as_u2, 4)),
            mul(
                add(add(pow_poly(y_u, 2), scale(mul(sub(u, c_as_u2), y_u), 2)), pow_poly(c_as_u2, 2)),
                add(add(pow_poly(y_u, 2), scale(mul(add(u, c_as_u2), y_u), -2)), pow_poly(c_as_u2, 2)),
            ),
        ),
        -12,
    )

    print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest().upper())
    print("Q(y) = (y+c)/(y^2 + (1-2c)y + c^2)")
    print("D[K] = P(c,y) / h(c,y)^4")
    print("h(c,y) = y^2 + (1-2c)y + c^2")
    print()
    print("P coefficients by powers of y:")
    for yi, coeff in coeffs_by_y(P):
        print(f"  y^{yi}: {c_poly_to_str(coeff)}")
    print()
    print("P factorization over u=sqrt(c) verified:", P_u == factorized_u)
    print("P = -12(1-4c)(y^2 + 2(u-c)y + c^2)(y^2 - 2(u+c)y + c^2)")
    print("where u=sqrt(c), 0<u<=1/2, y=(2t-gamma)^2")
    print("At y=0: D[K] = -12(1-4c)/c^4")
    print("As y -> infinity: D[K] ~ -12(1-4c)/y^4")
    print("For 0<c<1/4, D[K]>0 only when")
    print("  u^2 + u - u*sqrt(1+2u) < y < u^2 + u + u*sqrt(1+2u)")
    print()

    samples = [
        (Fraction(1, 4), Fraction(0)),
        (Fraction(1, 4), Fraction(1)),
        (Fraction(2, 9), Fraction(0)),
        (Fraction(2, 9), Fraction(1)),
        (Fraction(9, 100), Fraction(10)),
        (Fraction(99, 10000), Fraction(100)),
    ]
    print("sample P/h^4 values:")
    for c_val, y_val in samples:
        h_val = eval_poly(h, c_val, y_val)
        p_val = eval_poly(P, c_val, y_val)
        d_val = p_val / (h_val**4)
        print(f"  c={c_val}, y={y_val}: P={p_val}, h={h_val}, D={float(d_val):.17g}")

    min_val = None
    min_pair = None
    for i in range(1, 2501):
        c_val = Fraction(i, 10000)  # scans 0.0001 to 0.2500
        for j in range(0, 501):
            y_val = Fraction(j, 20)
            h_val = eval_poly(h, c_val, y_val)
            p_val = eval_poly(P, c_val, y_val)
            d_val = p_val / (h_val**4)
            if min_val is None or d_val < min_val:
                min_val = d_val
                min_pair = (c_val, y_val)
            if d_val <= 0:
                print("NONPOSITIVE_GRID_HIT", c_val, y_val, d_val)
                return
    print("grid_min_positive", min_pair, float(min_val), min_val)


if __name__ == "__main__":
    main()
