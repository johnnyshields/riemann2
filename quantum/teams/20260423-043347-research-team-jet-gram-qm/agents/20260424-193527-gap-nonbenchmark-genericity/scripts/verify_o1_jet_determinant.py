"""Verify the endpoint O1 finite-jet determinant seed for UV-015.

Dependency-free exact arithmetic in Q(sqrt(2)).
"""

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Q2:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other):
        other = q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        other = q2(other)
        return Q2(self.a - other.a, self.b - other.b)

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __mul__(self, other):
        other = q2(other)
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        other = q2(other)
        den = other.a * other.a - 2 * other.b * other.b
        return Q2((self.a * other.a - 2 * self.b * other.b) / den,
                  (self.b * other.a - self.a * other.b) / den)

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        if self.a == 0:
            return f"{self.b}*sqrt(2)"
        sign = "+" if self.b > 0 else "-"
        return f"{self.a} {sign} {abs(self.b)}*sqrt(2)"


def q2(value):
    if isinstance(value, Q2):
        return value
    return Q2(Fraction(value), Fraction(0))


zero = Q2()
one = Q2(Fraction(1))
inv_sqrt2 = Q2(Fraction(0), Fraction(1, 2))


def vec(*entries):
    return list(entries)


def add(p, q):
    return [pi + qi for pi, qi in zip(p, q)]


def scale(s, p):
    return [s * pi for pi in p]


def dot(p, q):
    out = zero
    for pi, qi in zip(p, q):
        out += pi * qi
    return out


e1 = vec(one, zero, zero)
e2 = vec(zero, one, zero)
e3 = vec(zero, zero, one)

x = e1
y = e2
a = scale(inv_sqrt2, add(e2, e3))
c = scale(inv_sqrt2, add(e1, e3))
b = add(scale(Q2(Fraction(-1)), e1), scale(inv_sqrt2, add(e2, scale(Q2(Fraction(-1)), e3))))
d = scale(Q2(Fraction(-1)), e2)

# Here ||a||=||c||=1, so Tx=a and Ty=c.
Tx = a
Ty = c


def subtract_projection(v, unit):
    return add(v, scale(-dot(unit, v), unit))


Ux = subtract_projection(b, Tx)
Uy = subtract_projection(d, Ty)

constraints = {
    "<x,x>": dot(x, x),
    "<y,y>": dot(y, y),
    "<a,x>": dot(a, x),
    "<c,y>": dot(c, y),
    "<b,x> + ||a||^2": dot(b, x) + dot(a, a),
    "<d,y> + ||c||^2": dot(d, y) + dot(c, c),
}

C = dot(Tx, Ty)
Delta = dot(a, y) * dot(Tx, Uy) - dot(x, c) * dot(Ux, Ty)

print("constraints:")
for key, value in constraints.items():
    print(f"{key} = {value}")
print(f"C = {C}")
print(f"Delta = {Delta}")
