#!/usr/bin/env python3
"""
UV-026 source-linear scaled mixed-input parity audit.

Expands the exact linearized mixed formulas in ordinary z through order 7 with
formal baseline q_j and source r_k symbols.  No external packages are used.
The goal is to characterize which source Taylor derivative orders can
contribute to odd/even powers of M = D_Q delta N^lin.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "mixed_parity_audit.json"
MAX_PRE = 12
MAX_OUT = 7


def merge_monomials(a, b):
    return tuple(sorted(a + b))


@dataclass(frozen=True)
class Poly:
    # map (z_power, monomial_tuple) -> Fraction coefficient
    terms: dict

    @staticmethod
    def zero():
        return Poly({})

    @staticmethod
    def one():
        return Poly({(0, ()): Fraction(1)})

    @staticmethod
    def z(power=1, coeff=Fraction(1), mon=()):
        if coeff == 0:
            return Poly.zero()
        return Poly({(power, tuple(sorted(mon))): Fraction(coeff)})

    def clean(self):
        return Poly({k: v for k, v in self.terms.items() if v})

    def trunc(self, max_power=MAX_PRE, min_power=0):
        return Poly({k: v for k, v in self.terms.items() if min_power <= k[0] <= max_power and v})

    def __add__(self, other):
        out = dict(self.terms)
        for k, v in other.terms.items():
            out[k] = out.get(k, Fraction(0)) + v
            if out[k] == 0:
                del out[k]
        return Poly(out)

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, c):
        c = Fraction(c)
        if c == 0:
            return Poly.zero()
        return Poly({k: c * v for k, v in self.terms.items() if c * v})

    def shift(self, dz):
        return Poly({(p + dz, mon): c for (p, mon), c in self.terms.items() if p + dz >= 0})

    def mul(self, other, max_power=MAX_PRE):
        out = {}
        for (p1, m1), c1 in self.terms.items():
            for (p2, m2), c2 in other.terms.items():
                p = p1 + p2
                if p > max_power:
                    continue
                mon = merge_monomials(m1, m2)
                key = (p, mon)
                out[key] = out.get(key, Fraction(0)) + c1 * c2
                if out[key] == 0:
                    del out[key]
        return Poly(out)

    def pow(self, n, max_power=MAX_PRE):
        out = Poly.one()
        base = self
        for _ in range(n):
            out = out.mul(base, max_power=max_power)
        return out

    def by_power(self, power):
        return {mon: c for (p, mon), c in self.terms.items() if p == power}

    def support_by_source(self):
        out = {}
        for (p, mon), coeff in self.terms.items():
            source = sorted({x for x in mon if x.startswith("r")})
            if len(source) != 1:
                continue
            out.setdefault(source[0], {}).setdefault(p, 0)
            out[source[0]][p] += 1
        return {r: sorted(powers) for r, powers in out.items()}


def symbol(name, power, coeff=Fraction(1)):
    return Poly.z(power, coeff, (name,))


def series_sin(x):
    out = Poly.zero()
    for n in range(0, 7):
        degree = 2 * n + 1
        term = x.pow(degree).scale(Fraction((-1) ** n, math.factorial(degree)))
        out = out + term
    return out.trunc()


def series_cos(x):
    out = Poly.one()
    for n in range(1, 7):
        degree = 2 * n
        term = x.pow(degree).scale(Fraction((-1) ** n, math.factorial(degree)))
        out = out + term
    return out.trunc()


def q_pm(sign):
    out = Poly.zero()
    for j in range(0, 10):
        coeff = Fraction(sign ** j, (2 ** j) * math.factorial(j))
        out = out + symbol(f"q{j}", j, coeff)
    return out.trunc()


def delta0():
    out = Poly.zero()
    for j in range(0, 10):
        coeff = Fraction(((-1) ** (j + 1) - 1), (2 ** (j + 1)) * math.factorial(j + 1))
        if coeff:
            out = out + symbol(f"q{j}", j + 1, coeff)
    return out.trunc()


def source_d(sign):
    out = Poly.zero()
    for k in range(2, 10):
        coeff = Fraction(sign ** k, (2 ** k) * math.factorial(k))
        out = out + symbol(f"r{k}", k, coeff)
    return out.trunc()


def source_eta():
    out = Poly.zero()
    for k in range(2, 10):
        coeff = Fraction(((-1) ** (k + 1) - 1), (2 ** (k + 1)) * math.factorial(k + 1))
        if coeff:
            out = out + symbol(f"r{k}", k + 1, coeff)
    return out.trunc()


def mon_to_string(mon):
    if not mon:
        return "1"
    counts = {}
    for item in mon:
        counts[item] = counts.get(item, 0) + 1
    parts = []
    for key in sorted(counts):
        count = counts[key]
        parts.append(key if count == 1 else f"{key}^{count}")
    return "*".join(parts)


def coeff_expr(poly, power):
    terms = poly.by_power(power)
    if not terms:
        return "0"
    pieces = []
    for mon, coeff in sorted(terms.items(), key=lambda kv: mon_to_string(kv[0])):
        pieces.append(f"{coeff}*{mon_to_string(mon)}")
    return " + ".join(pieces)


def source_support_at(poly, power):
    out = {}
    for mon, coeff in poly.by_power(power).items():
        sources = sorted({x for x in mon if x.startswith("r")})
        if len(sources) == 1 and coeff:
            out.setdefault(sources[0], set()).add(mon_to_string(tuple(x for x in mon if not x.startswith("r"))))
    return {k: sorted(v) for k, v in sorted(out.items())}


def powers_by_source(poly):
    out = {}
    for (power, mon), coeff in poly.terms.items():
        if power > MAX_OUT or not coeff:
            continue
        sources = sorted({x for x in mon if x.startswith("r")})
        if len(sources) == 1:
            out.setdefault(sources[0], set()).add(power)
    return {k: sorted(v) for k, v in sorted(out.items())}


def main():
    qplus = q_pm(1)
    qminus = q_pm(-1)
    dplus = source_d(1)
    dminus = source_d(-1)
    eta = source_eta()
    d0 = delta0()
    sin0 = series_sin(d0)
    cos0 = series_cos(d0)
    z = Poly.z(1)

    # Linearized scaled mixed entries. D_Q scales by Q powers only, not z powers,
    # so it is irrelevant to ordinary-z parity and support.
    m11 = cos0.mul(eta).shift(-1).scale(-2).trunc(MAX_OUT)
    m12 = (
        cos0.mul(eta)
        + dplus.mul(z).mul(cos0)
        - qplus.mul(z).mul(sin0).mul(eta)
    ).shift(-2).trunc(MAX_OUT)
    m21 = (
        cos0.mul(eta)
        + dminus.mul(z).mul(cos0)
        - qminus.mul(z).mul(sin0).mul(eta)
    ).scale(-1).shift(-2).trunc(MAX_OUT)
    f_q = (
        (dminus + dplus).mul(z).mul(cos0)
        - (qminus + qplus).mul(z).mul(sin0).mul(eta)
        - (dminus.mul(qplus) + qminus.mul(dplus)).mul(z.pow(2)).mul(sin0)
        + (Poly.one().scale(2) - qminus.mul(qplus).mul(z.pow(2))).mul(cos0).mul(eta)
    )
    m22 = f_q.shift(-3).scale(Fraction(1, 2)).trunc(MAX_OUT)

    entries = {"11": m11, "12": m12, "21": m21, "22": m22}
    parity_by_entry = {}
    powers_by_entry = {}
    for name, poly in entries.items():
        powers = sorted({p for (p, _mon) in poly.terms if p <= MAX_OUT})
        powers_by_entry[name] = powers
        parity_by_entry[name] = {
            "even_powers": [p for p in powers if p % 2 == 0],
            "odd_powers": [p for p in powers if p % 2 == 1],
            "only_even": all(p % 2 == 0 for p in powers),
        }

    z5_support = {name: source_support_at(poly, 5) for name, poly in entries.items()}
    source_power_map = {name: powers_by_source(poly) for name, poly in entries.items()}
    z5_expr = {name: coeff_expr(poly, 5) for name, poly in entries.items()}

    # Source derivative order summary through z^7.
    by_r = {}
    for rk in [f"r{k}" for k in range(2, 10)]:
        by_r[rk] = {}
        for name, poly in entries.items():
            powers = sorted(
                p
                for (p, mon), coeff in poly.terms.items()
                if p <= MAX_OUT and coeff and rk in mon
            )
            by_r[rk][name] = powers

    manifest = {
        "scope": "source-linear scaled mixed input M=D_Q delta N^lin through z^7",
        "exact_formula_used": {
            "M11": "-2*cos(Delta0)*eta/s",
            "M12": "(cos(Delta0)*eta + d_+*s*cos(Delta0) - q_{0,+}*s*sin(Delta0)*eta)/s^2",
            "M21": "-(cos(Delta0)*eta + d_-*s*cos(Delta0) - q_{0,-}*s*sin(Delta0)*eta)/s^2",
            "M22": "linearization of F divided by 2*s^3",
        },
        "parity_by_entry": parity_by_entry,
        "powers_by_entry": powers_by_entry,
        "powers_by_source_derivative": by_r,
        "source_power_map": source_power_map,
        "z5_support": z5_support,
        "z5_coefficients": z5_expr,
        "theorem_summary": {
            "not_only_even": True,
            "diagonal_entries_only_even_through_z7": parity_by_entry["11"]["only_even"] and parity_by_entry["22"]["only_even"],
            "offdiagonal_entries_have_odd_powers": bool(parity_by_entry["12"]["odd_powers"] or parity_by_entry["21"]["odd_powers"]),
            "odd_source_derivatives_contribute_only_even_powers_through_z7": all(
                all(p % 2 == 0 for entry in by_r[f"r{k}"].values() for p in entry)
                for k in [3, 5, 7, 9]
            ),
            "z5_can_be_nonzero": any(z5_support[name] for name in z5_support),
            "z5_source_derivatives": sorted({rk for entry in z5_support.values() for rk in entry}),
            "z5_not_from_odd_derivative_r7": "r7" not in {rk for entry in z5_support.values() for rk in entry},
        },
    }
    OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    digest = hashlib.sha1(OUT.read_bytes()).hexdigest().upper()
    print(json.dumps({
        "output": str(OUT),
        "sha1": digest,
        "parity_by_entry": parity_by_entry,
        "z5_support": z5_support,
        "theorem_summary": manifest["theorem_summary"],
    }, indent=2))


if __name__ == "__main__":
    main()
