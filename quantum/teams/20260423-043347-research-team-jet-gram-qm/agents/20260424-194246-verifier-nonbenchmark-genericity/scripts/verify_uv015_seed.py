"""Independent exact check of the UV-015 endpoint O1 determinant seed.

The arithmetic is in Q(sqrt(2)).  It verifies the normalized endpoint
2-jet constraints and recomputes C=<Tx,Ty> and
Delta=d(I,C)/d(u,v) for the seed in the gap report.
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Qsqrt2:
    rat: Fraction = Fraction(0)
    sqrt2: Fraction = Fraction(0)

    def __add__(self, other):
        other = coerce(other)
        return Qsqrt2(self.rat + other.rat, self.sqrt2 + other.sqrt2)

    def __sub__(self, other):
        other = coerce(other)
        return Qsqrt2(self.rat - other.rat, self.sqrt2 - other.sqrt2)

    def __neg__(self):
        return Qsqrt2(-self.rat, -self.sqrt2)

    def __mul__(self, other):
        other = coerce(other)
        return Qsqrt2(
            self.rat * other.rat + 2 * self.sqrt2 * other.sqrt2,
            self.rat * other.sqrt2 + self.sqrt2 * other.rat,
        )

    def __str__(self):
        if self.sqrt2 == 0:
            return str(self.rat)
        if self.rat == 0:
            return f"{self.sqrt2}*sqrt(2)"
        sign = "+" if self.sqrt2 > 0 else "-"
        return f"{self.rat} {sign} {abs(self.sqrt2)}*sqrt(2)"


def coerce(value):
    if isinstance(value, Qsqrt2):
        return value
    return Qsqrt2(Fraction(value), Fraction(0))


zero = Qsqrt2()
one = Qsqrt2(Fraction(1))
minus_one = Qsqrt2(Fraction(-1))
inv_sqrt2 = Qsqrt2(Fraction(0), Fraction(1, 2))


def vec(*entries):
    return list(entries)


def add(v, w):
    return [vi + wi for vi, wi in zip(v, w)]


def scale(alpha, v):
    return [alpha * vi for vi in v]


def dot(v, w):
    total = zero
    for vi, wi in zip(v, w):
        total += vi * wi
    return total


def project_off(v, unit):
    return add(v, scale(-dot(unit, v), unit))


e1 = vec(one, zero, zero)
e2 = vec(zero, one, zero)
e3 = vec(zero, zero, one)

x = e1
y = e2
a = scale(inv_sqrt2, add(e2, e3))
c = scale(inv_sqrt2, add(e1, e3))
b = add(scale(minus_one, e1), scale(inv_sqrt2, add(e2, scale(minus_one, e3))))
d = scale(minus_one, e2)

Tx = a
Ty = c
Ux = project_off(b, Tx)
Uy = project_off(d, Ty)

checks = [
    ("<x,x>", dot(x, x), one),
    ("<y,y>", dot(y, y), one),
    ("<a,x>", dot(a, x), zero),
    ("<c,y>", dot(c, y), zero),
    ("<b,x> + ||a||^2", dot(b, x) + dot(a, a), zero),
    ("<d,y> + ||c||^2", dot(d, y) + dot(c, c), zero),
    ("||a||^2", dot(a, a), one),
    ("||c||^2", dot(c, c), one),
]

C = dot(Tx, Ty)
d_u_I = dot(a, y)
d_v_I = dot(x, c)
d_u_C = dot(Ux, Ty)
d_v_C = dot(Tx, Uy)
Delta = d_u_I * d_v_C - d_v_I * d_u_C

for label, observed, expected in checks:
    print(f"{label} = {observed} expected {expected}")
    assert observed == expected

print(f"C = {C}")
print(f"d_u_I = {d_u_I}")
print(f"d_v_I = {d_v_I}")
print(f"d_u_C = {d_u_C}")
print(f"d_v_C = {d_v_C}")
print(f"Delta = {Delta}")

assert C == Qsqrt2(Fraction(1, 2), Fraction(0))
assert Delta == Qsqrt2(Fraction(0), Fraction(1, 4))
