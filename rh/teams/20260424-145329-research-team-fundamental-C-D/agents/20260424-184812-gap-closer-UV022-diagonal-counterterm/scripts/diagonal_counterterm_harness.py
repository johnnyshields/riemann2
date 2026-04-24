from fractions import Fraction


# Polynomials in (a1, a2, m, d), represented by exponent tuples.


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


def T(x):
    out = {}
    for coeff, degree in [(3, 1), (5, 2), (7, 3), (11, 4)]:
        out = add(out, scale(coeff, power(x, degree)))
    return out


def X(h):
    return add(add(const(2), h), scale(3, power(h, 2)))


def subst_zero(p, i):
    return {exp: coeff for exp, coeff in p.items() if exp[i] == 0}


def swap_atoms(p):
    out = {}
    for (e1, e2, em, ed), coeff in p.items():
        new_exp = (e2, e1, em, ed)
        new_coeff = -coeff if ed % 2 else coeff
        out[new_exp] = out.get(new_exp, Fraction(0)) + new_coeff
        if out[new_exp] == 0:
            del out[new_exp]
    return out


def d_remainder_mod_d2(p):
    return {exp: coeff for exp, coeff in p.items() if exp[3] < 2}


def sample_value(p, vals):
    total = Fraction(0)
    for exp, coeff in p.items():
        term = coeff
        for base, e in zip(vals, exp):
            term *= Fraction(base) ** e
        total += term
    return total


def brief(p, limit=8):
    if not p:
        return "0"
    pieces = []
    names = ["a1", "a2", "m", "d"]
    for exp, coeff in sorted(p.items())[:limit]:
        mon = []
        for name, e in zip(names, exp):
            if e == 1:
                mon.append(name)
            elif e > 1:
                mon.append(f"{name}^{e}")
        pieces.append(f"{coeff}*{'*'.join(mon) if mon else '1'}")
    if len(pieces) < len(p):
        pieces.append(f"... ({len(p)} terms)")
    return " + ".join(pieces)


a1 = var(0)
a2 = var(1)
m = var(2)
d = var(3)

h1 = sub(m, scale(Fraction(1, 2), d))
h2 = add(m, scale(Fraction(1, 2), d))
x1 = X(h1)
x2 = X(h2)
xm = X(m)

cross = sub(sub(T(add(scale(1, mul(a1, x1)), scale(1, mul(a2, x2)))), T(mul(a1, x1))), T(mul(a2, x2)))
diag_self = sub(sub(T(mul(add(a1, a2), xm)), T(mul(a1, xm))), T(mul(a2, xm)))
renorm = sub(cross, diag_self)

tests = {
    "one_amplitude_left_zero": subst_zero(renorm, 0) == {},
    "one_amplitude_right_zero": subst_zero(renorm, 1) == {},
    "swap_difference_zero": sub(renorm, swap_atoms(renorm)) == {},
    "diagonal_value_zero": subst_zero(renorm, 3) == {},
    "divisible_by_delta_squared": d_remainder_mod_d2(renorm) == {},
    "original_diagonal_cross_effect_zero": subst_zero(cross, 3) == {},
    "original_diagonal_sample_at_a1_2_a2_-3_m_5": sample_value(
        subst_zero(cross, 3), [2, -3, 5, 0]
    ),
    "renormalized_sample_at_a1_2_a2_-3_m_5_d_7": sample_value(
        renorm, [2, -3, 5, 7]
    ),
    "renormalized_polynomial_brief": brief(renorm),
}

for name, value in tests.items():
    print(f"{name} = {value}")
