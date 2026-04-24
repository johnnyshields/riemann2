from fractions import Fraction


# Polynomial algebra in variables (a1, a2, m, d).
# This keeps the counterterm test exact and leaves a cited artifact.


NAMES = ("a1", "a2", "m", "d")


def const(c):
    c = Fraction(c)
    return {} if c == 0 else {(0, 0, 0, 0): c}


def var(i):
    exp = [0, 0, 0, 0]
    exp[i] = 1
    return {tuple(exp): Fraction(1)}


def add(p, q):
    out = dict(p)
    for exp, coeff in q.items():
        out[exp] = out.get(exp, Fraction(0)) + coeff
        if out[exp] == 0:
            del out[exp]
    return out


def neg(p):
    return {exp: -coeff for exp, coeff in p.items()}


def sub(p, q):
    return add(p, neg(q))


def mul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            exp = tuple(e1[i] + e2[i] for i in range(4))
            out[exp] = out.get(exp, Fraction(0)) + c1 * c2
            if out[exp] == 0:
                del out[exp]
    return out


def scale(c, p):
    c = Fraction(c)
    if c == 0:
        return {}
    return {exp: c * coeff for exp, coeff in p.items()}


def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out


def subst_zero(p, i):
    return {exp: coeff for exp, coeff in p.items() if exp[i] == 0}


def d_remainder_mod_d2(p):
    return {exp: coeff for exp, coeff in p.items() if exp[3] < 2}


def d_first_order(p):
    return {exp: coeff for exp, coeff in p.items() if exp[3] == 1}


def swap_atoms(p):
    out = {}
    for (e1, e2, em, ed), coeff in p.items():
        exp = (e2, e1, em, ed)
        signed = -coeff if ed % 2 else coeff
        out[exp] = out.get(exp, Fraction(0)) + signed
        if out[exp] == 0:
            del out[exp]
    return out


def subst_a2_neg_a1(p):
    out = {}
    for (e1, e2, em, ed), coeff in p.items():
        exp = (e1 + e2, 0, em, ed)
        signed = -coeff if e2 % 2 else coeff
        out[exp] = out.get(exp, Fraction(0)) + signed
        if out[exp] == 0:
            del out[exp]
    return out


def brief(p, limit=10):
    if not p:
        return "0"
    pieces = []
    for exp, coeff in sorted(p.items())[:limit]:
        mon = []
        for name, e in zip(NAMES, exp):
            if e == 1:
                mon.append(name)
            elif e > 1:
                mon.append(f"{name}^{e}")
        pieces.append(f"{coeff}*{'*'.join(mon) if mon else '1'}")
    if len(pieces) < len(p):
        pieces.append(f"... ({len(p)} terms)")
    return " + ".join(pieces)


def T(x, degrees):
    out = {}
    for coeff, degree in degrees:
        out = add(out, scale(coeff, power(x, degree)))
    return out


def X(h):
    return add(add(const(2), h), scale(3, power(h, 2)))


def cross_effect_counterterm(degrees):
    a1 = var(0)
    a2 = var(1)
    m = var(2)
    d = var(3)

    h1 = sub(m, scale(Fraction(1, 2), d))
    h2 = add(m, scale(Fraction(1, 2), d))
    x1 = X(h1)
    x2 = X(h2)
    xm = X(m)

    cross = sub(sub(T(add(mul(a1, x1), mul(a2, x2)), degrees), T(mul(a1, x1), degrees)), T(mul(a2, x2), degrees))
    diagonal_self = sub(sub(T(mul(add(a1, a2), xm), degrees), T(mul(a1, xm), degrees)), T(mul(a2, xm), degrees))
    return sub(cross, diagonal_self)


CASES = {
    "quadratic_transfer": [(1, 2)],
    "cubic_transfer": [(1, 3)],
    "mixed_transfer": [(3, 1), (5, 2), (7, 3), (11, 4)],
}


for name, degrees in CASES.items():
    renorm = cross_effect_counterterm(degrees)
    first = d_first_order(renorm)
    first_on_cancellation = subst_a2_neg_a1(first)

    print(f"[{name}]")
    print(f"one_amplitude_left_zero = {subst_zero(renorm, 0) == {}}")
    print(f"one_amplitude_right_zero = {subst_zero(renorm, 1) == {}}")
    print(f"swap_difference_zero = {sub(renorm, swap_atoms(renorm)) == {}}")
    print(f"diagonal_value_zero = {subst_zero(renorm, 3) == {}}")
    print(f"divisible_by_delta_squared = {d_remainder_mod_d2(renorm) == {}}")
    print(f"first_delta_terms = {brief(first)}")
    print(f"first_delta_terms_after_a2_equals_minus_a1 = {brief(first_on_cancellation)}")
    print()
