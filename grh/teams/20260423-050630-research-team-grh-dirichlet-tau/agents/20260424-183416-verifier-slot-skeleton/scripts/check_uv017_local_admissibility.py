"""Check UV-017 local admissibility algebra for the finite-s chart.

The first attempted version used sympy, which is not installed here. This
version uses exact rational polynomial arithmetic over formal monomials in
q0, q1, q2, q3, q4 and s.
"""

from fractions import Fraction

DEG = 5


def mono(name):
    return ((name,), Fraction(1))


def one():
    return ((), Fraction(1))


def term_str(monomial, coeff):
    if coeff == 0:
        return ""
    pieces = []
    if coeff == 1 and monomial:
        pass
    elif coeff == -1 and monomial:
        pieces.append("-")
    else:
        pieces.append(str(coeff))
    if monomial:
        if pieces and pieces[-1] not in {"-"}:
            pieces.append("*")
        pieces.append("*".join(monomial))
    return "".join(pieces) if pieces else "1"


def add_expr(a, b):
    out = dict(a)
    for mon, coeff in b.items():
        out[mon] = out.get(mon, Fraction(0)) + coeff
        if out[mon] == 0:
            del out[mon]
    return out


def neg_expr(a):
    return {mon: -coeff for mon, coeff in a.items()}


def mul_expr(a, b):
    out = {}
    for mon_a, coeff_a in a.items():
        for mon_b, coeff_b in b.items():
            mon = tuple(sorted(mon_a + mon_b))
            out[mon] = out.get(mon, Fraction(0)) + coeff_a * coeff_b
    return {mon: coeff for mon, coeff in out.items() if coeff}


def scale_expr(a, scalar):
    scalar = Fraction(scalar)
    return {mon: coeff * scalar for mon, coeff in a.items() if coeff * scalar}


def expr_from(name=None, coeff=1):
    if name is None:
        return {(): Fraction(coeff)}
    return {(name,): Fraction(coeff)}


def expr_to_str(expr):
    if not expr:
        return "0"
    items = sorted(expr.items(), key=lambda item: (item[0], item[1]))
    parts = []
    for mon, coeff in items:
        txt = term_str(mon, coeff)
        if not parts:
            parts.append(txt)
        elif txt.startswith("-"):
            parts.append("- " + txt[1:])
        else:
            parts.append("+ " + txt)
    return " ".join(parts)


def add_poly(a, b):
    out = [dict(c) for c in a]
    for i, coeff in enumerate(b):
        out[i] = add_expr(out[i], coeff)
    return out


def neg_poly(a):
    return [neg_expr(c) for c in a]


def scale_poly(a, scalar):
    return [scale_expr(c, scalar) for c in a]


def mul_poly(a, b):
    out = [{} for _ in range(DEG + 1)]
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if not bj or i + j > DEG:
                continue
            out[i + j] = add_expr(out[i + j], mul_expr(ai, bj))
    return out


def pow_poly(a, n):
    out = [{} for _ in range(DEG + 1)]
    out[0] = {(): Fraction(1)}
    for _ in range(n):
        out = mul_poly(out, a)
    return out


def poly_to_str(poly, start=0):
    parts = []
    for i, coeff in enumerate(poly):
        if i < start or not coeff:
            continue
        coeff_str = expr_to_str(coeff)
        if i == 0:
            parts.append(coeff_str)
        elif i == 1:
            parts.append(f"({coeff_str})*s")
        else:
            parts.append(f"({coeff_str})*s^{i}")
    return " + ".join(parts) if parts else "0"


def order(poly):
    for i, coeff in enumerate(poly):
        if coeff:
            return i
    return None


def shift_div(poly, power):
    out = [{} for _ in range(DEG + 1)]
    for i in range(power, DEG + 1):
        out[i - power] = dict(poly[i])
    return out


q0 = expr_from("q0")
q1 = expr_from("q1")
q2 = expr_from("q2")
q3 = expr_from("q3")
q4 = expr_from("q4")

zero_poly = [{} for _ in range(DEG + 1)]

q_plus = [{} for _ in range(DEG + 1)]
q_plus[0] = q0
q_plus[1] = scale_expr(q1, Fraction(1, 2))
q_plus[2] = scale_expr(q2, Fraction(1, 8))
q_plus[3] = scale_expr(q3, Fraction(1, 48))
q_plus[4] = scale_expr(q4, Fraction(1, 384))

q_minus = [{} for _ in range(DEG + 1)]
q_minus[0] = q0
q_minus[1] = scale_expr(q1, Fraction(-1, 2))
q_minus[2] = scale_expr(q2, Fraction(1, 8))
q_minus[3] = scale_expr(q3, Fraction(-1, 48))
q_minus[4] = scale_expr(q4, Fraction(1, 384))

Delta = [{} for _ in range(DEG + 1)]
Delta[1] = scale_expr(q0, -1)
Delta[3] = scale_expr(q2, Fraction(-1, 24))
Delta[5] = scale_expr(q4, Fraction(-1, 1920))

sin_delta = add_poly(
    add_poly(Delta, scale_poly(pow_poly(Delta, 3), Fraction(-1, 6))),
    scale_poly(pow_poly(Delta, 5), Fraction(1, 120)),
)
cos_delta = add_poly(
    add_poly([{(): Fraction(1)}] + [{} for _ in range(DEG)], scale_poly(pow_poly(Delta, 2), Fraction(-1, 2))),
    scale_poly(pow_poly(Delta, 4), Fraction(1, 24)),
)

s_poly = [{} for _ in range(DEG + 1)]
s_poly[1] = {(): Fraction(1)}

n12 = add_poly(sin_delta, mul_poly(mul_poly(q_plus, s_poly), cos_delta))
n21 = add_poly(sin_delta, mul_poly(mul_poly(q_minus, s_poly), cos_delta))
q_sum = add_poly(q_plus, q_minus)
q_prod = mul_poly(q_minus, q_plus)
two_minus_qprod_s2 = add_poly([{(): Fraction(2)}] + [{} for _ in range(DEG)], neg_poly(mul_poly(q_prod, mul_poly(s_poly, s_poly))))
n22 = add_poly(mul_poly(mul_poly(q_sum, s_poly), cos_delta), mul_poly(two_minus_qprod_s2, sin_delta))

det_raw = add_expr(
    mul_expr(scale_expr(q0, 2), scale_expr(add_expr(q2, scale_expr(mul_expr(mul_expr(q0, q0), q0), 2)), Fraction(1, 12))),
    neg_expr(mul_expr(scale_expr(q1, Fraction(1, 2)), scale_expr(q1, Fraction(1, 2)))),
)
det_scaled = scale_expr(det_raw, 12)

print("Delta order:", order(Delta), "series:", poly_to_str(Delta))
print("sin(Delta) order:", order(sin_delta), "series:", poly_to_str(sin_delta))
print("upper numerator order:", order(n12), "series:", poly_to_str(n12))
print("lower numerator interior order:", order(n21), "series:", poly_to_str(n21))
print("(2,2) numerator order:", order(n22), "series:", poly_to_str(n22))
print()
print("After denominator removal:")
print("sin(Delta)/s =", poly_to_str(shift_div(sin_delta, 1)))
print("upper/s^2 =", poly_to_str(shift_div(n12, 2)))
print("lower interior/s^2 =", poly_to_str(shift_div(n21, 2)))
print("(2,2)/s^3 =", poly_to_str(shift_div(n22, 3)))
print()
print("Same-point determinant before global 1/pi^2 factor:")
print("det_raw =", expr_to_str(det_raw))
print("12*det_raw =", expr_to_str(det_scaled))
