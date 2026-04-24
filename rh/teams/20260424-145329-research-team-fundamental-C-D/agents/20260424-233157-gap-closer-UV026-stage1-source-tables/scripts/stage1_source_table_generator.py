#!/usr/bin/env python3
"""Stage-1 UV-026 source-table generator.

Standard-library finite power-series implementation of the pre-Phi_K source
formulas.  Given midpoint derivatives of the baseline phase derivative q_0 and
source remainders r_i^[1], r_i^[5], it generates ordinary-z coefficient tables
through z^7 for:

* G_pm^(0)
* N_0
* delta G_{i,pm}^{lin,[1/5]}
* M_i^[1/5] = Gr_{1/5}(D_Q delta N_i^lin)

No zeta-specific derivative values are asserted here.  With no --input file,
the script runs an admissible toy input to check the finite algebra and emits
the exact input schema needed for the real source theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import factorial
from pathlib import Path
from typing import Any


ORDER = 7
WORK_ORDER = 10
BASE_DERIV_ORDER = 9
SOURCE_DERIV_MIN = 2
SOURCE_DERIV_MAX = 9
TAGS = ("1", "2")
GRADES = ("1", "5")
SIGNS = ("-", "+")


Poly = list[Fraction]
Matrix = list[list[Poly]]


def sha1(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest().upper()


def frac(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, float):
        return Fraction(value).limit_denominator()
    raise TypeError(f"unsupported coefficient value {value!r}")


def zero(n: int = WORK_ORDER) -> Poly:
    return [Fraction(0) for _ in range(n + 1)]


def const(c: Fraction, n: int = WORK_ORDER) -> Poly:
    p = zero(n)
    p[0] = c
    return p


def add(a: Poly, b: Poly, n: int = WORK_ORDER) -> Poly:
    return [a[i] + b[i] for i in range(n + 1)]


def sub(a: Poly, b: Poly, n: int = WORK_ORDER) -> Poly:
    return [a[i] - b[i] for i in range(n + 1)]


def scale(a: Poly, c: Fraction, n: int = WORK_ORDER) -> Poly:
    return [c * a[i] for i in range(n + 1)]


def mul(a: Poly, b: Poly, n: int = WORK_ORDER) -> Poly:
    out = zero(n)
    for i in range(n + 1):
        if a[i] == 0:
            continue
        for j in range(n + 1 - i):
            out[i + j] += a[i] * b[j]
    return out


def pow_poly(a: Poly, k: int, n: int = WORK_ORDER) -> Poly:
    out = const(Fraction(1), n)
    for _ in range(k):
        out = mul(out, a, n)
    return out


def div_by_s_power(a: Poly, k: int, q_value: Fraction, n_out: int = ORDER) -> tuple[Poly, list[str]]:
    """Divide by s^k=(z/Q^2)^k and return z^0..z^n_out coefficients."""
    bad = []
    for j in range(k):
        if a[j] != 0:
            bad.append(f"z^{j-k}: {format_frac(a[j] * q_value ** (2 * k))}")
    out = [Fraction(0) for _ in range(n_out + 1)]
    factor = q_value ** (2 * k)
    for m in range(n_out + 1):
        src = m + k
        if src < len(a):
            out[m] = a[src] * factor
    return out + [Fraction(0) for _ in range(WORK_ORDER - n_out)], bad


def series_sin(a: Poly, n: int = WORK_ORDER) -> Poly:
    out = zero(n)
    for j in range((n // 2) + 1):
        power = 2 * j + 1
        term = scale(pow_poly(a, power, n), Fraction((-1) ** j, factorial(power)), n)
        out = add(out, term, n)
    return out


def series_cos(a: Poly, n: int = WORK_ORDER) -> Poly:
    out = zero(n)
    for j in range((n // 2) + 1):
        power = 2 * j
        term = scale(pow_poly(a, power, n), Fraction((-1) ** j, factorial(power)), n)
        out = add(out, term, n)
    return out


def taylor_from_derivs(vals: list[Fraction], sign: str, q_value: Fraction, max_power: int = WORK_ORDER) -> Poly:
    eps = Fraction(1) if sign == "+" else Fraction(-1)
    out = zero(WORK_ORDER)
    for k, v in enumerate(vals):
        if k > max_power:
            break
        out[k] += v * (eps / (2 * q_value**2)) ** k / factorial(k)
    return out


def derivative_taylor(vals: list[Fraction], sign: str, q_value: Fraction, d_order: int) -> Poly:
    eps = Fraction(1) if sign == "+" else Fraction(-1)
    out = zero(WORK_ORDER)
    for n in range(WORK_ORDER + 1):
        k = n + d_order
        if k >= len(vals):
            break
        out[n] += vals[k] * (eps / (2 * q_value**2)) ** n / factorial(n)
    return out


def integral_difference(vals: list[Fraction], q_value: Fraction, k_min: int, k_max: int) -> Poly:
    out = zero(WORK_ORDER)
    x_minus = Fraction(-1, 2 * q_value**2)
    x_plus = Fraction(1, 2 * q_value**2)
    for k in range(k_min, min(k_max, len(vals) - 1) + 1):
        degree = k + 1
        if degree > WORK_ORDER:
            break
        out[degree] += vals[k] * (x_minus**degree - x_plus**degree) / factorial(degree)
    return out


def trunc(a: Poly, n: int = ORDER) -> Poly:
    out = zero(WORK_ORDER)
    for i in range(n + 1):
        out[i] = a[i]
    return out


def mat_trunc(m: Matrix) -> Matrix:
    return [[trunc(m[i][j]) for j in range(2)] for i in range(2)]


def format_frac(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def format_poly_coeffs(p: Poly, order: int = ORDER) -> list[str]:
    return [format_frac(p[i]) for i in range(order + 1)]


def format_matrix_coeffs(m: Matrix, order: int = ORDER) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    for n in range(order + 1):
        tables.append([[format_frac(m[i][j][n]) for j in range(2)] for i in range(2)])
    return tables


def default_demo_input() -> dict[str, Any]:
    r_template = [0, 0, 1, -2, 3, -1, 2, 0, -1, 1]
    return {
        "Q": "1",
        "pi": "1",
        "q": ["2", "1", "-1", "2", "0", "1", "-2", "1", "0", "1"],
        "r": {
            tag: {
                grade: [str(x + (int(tag) - 1) + (0 if grade == "1" else 2)) if k >= 2 else "0"
                        for k, x in enumerate(r_template)]
                for grade in GRADES
            }
            for tag in TAGS
        },
    }


def parse_input(data: dict[str, Any]) -> tuple[Fraction, Fraction, list[Fraction], dict[str, dict[str, list[Fraction]]]]:
    q_value = frac(data.get("Q", "1"))
    pi_value = frac(data.get("pi", "1"))
    q_derivs = [frac(v) for v in data["q"]]
    if len(q_derivs) < BASE_DERIV_ORDER + 1:
        raise ValueError("q must contain q_0^(0)(m)..q_0^(9)(m)")
    r: dict[str, dict[str, list[Fraction]]] = {}
    for tag in TAGS:
        r[tag] = {}
        for grade in GRADES:
            vals = [frac(v) for v in data["r"][tag][grade]]
            if len(vals) < SOURCE_DERIV_MAX + 1:
                raise ValueError(f"r[{tag}][{grade}] must contain derivatives 0..9")
            r[tag][grade] = vals
    return q_value, pi_value, q_derivs, r


def build_tables(data: dict[str, Any]) -> dict[str, Any]:
    q_value, pi_value, q_derivs, r_derivs = parse_input(data)

    s_factor = Fraction(1, q_value**2)
    q = {sgn: taylor_from_derivs(q_derivs, sgn, q_value) for sgn in SIGNS}
    qp = {sgn: derivative_taylor(q_derivs, sgn, q_value, 1) for sgn in SIGNS}
    qpp = {sgn: derivative_taylor(q_derivs, sgn, q_value, 2) for sgn in SIGNS}
    delta0 = integral_difference(q_derivs, q_value, 0, BASE_DERIV_ORDER)
    sin_delta = series_sin(delta0)
    cos_delta = series_cos(delta0)

    G0: dict[str, Matrix] = {}
    for sgn in SIGNS:
        q_sq = mul(q[sgn], q[sgn])
        q_cu = mul(q_sq, q[sgn])
        G0[sgn] = mat_trunc(
            [
                [scale(q[sgn], Fraction(2, 1) / pi_value), scale(qp[sgn], Fraction(1, 2) / pi_value)],
                [
                    scale(qp[sgn], Fraction(1, 2) / pi_value),
                    scale(add(qpp[sgn], scale(q_cu, Fraction(2))), Fraction(1, 12) / pi_value),
                ],
            ]
        )

    s_poly = zero()
    s_poly[1] = s_factor
    s2_poly = mul(s_poly, s_poly)
    n0_num_22 = add(
        mul(mul(add(q["-"], q["+"]), s_poly), cos_delta),
        mul(sub(const(Fraction(2)), mul(mul(q["-"], q["+"]), s2_poly)), sin_delta),
    )
    n0_entries_raw = [
        [scale(sin_delta, Fraction(-2, 1) / pi_value), scale(add(sin_delta, mul(mul(q["+"], s_poly), cos_delta)), Fraction(1, 1) / pi_value)],
        [
            scale(add(sin_delta, mul(mul(q["-"], s_poly), cos_delta)), Fraction(-1, 1) / pi_value),
            scale(n0_num_22, Fraction(1, 2) / pi_value),
        ],
    ]
    n0_divs = [[1, 2], [2, 3]]
    n0_bad: list[str] = []
    N0 = [[zero(), zero()], [zero(), zero()]]
    for i in range(2):
        for j in range(2):
            N0[i][j], bad = div_by_s_power(n0_entries_raw[i][j], n0_divs[i][j], q_value)
            n0_bad.extend([f"N0_{i+1}{j+1}:{b}" for b in bad])
    N0 = mat_trunc(N0)

    H: dict[str, dict[str, dict[str, Matrix]]] = {}
    M: dict[str, dict[str, Matrix]] = {}
    m_bad: list[str] = []
    source_leading: dict[str, Any] = {}
    for tag in TAGS:
        H[tag] = {}
        M[tag] = {}
        for grade in GRADES:
            vals = r_derivs[tag][grade]
            d = {sgn: taylor_from_derivs(vals, sgn, q_value) for sgn in SIGNS}
            e = {sgn: derivative_taylor(vals, sgn, q_value, 1) for sgn in SIGNS}
            g = {sgn: derivative_taylor(vals, sgn, q_value, 2) for sgn in SIGNS}
            eta = integral_difference(vals, q_value, SOURCE_DERIV_MIN, SOURCE_DERIV_MAX)
            source_leading[f"tag{tag}_grade{grade}"] = {
                "d_minus_z2": format_frac(d["-"][2]),
                "d_plus_z2": format_frac(d["+"][2]),
                "eta_z3": format_frac(eta[3]),
            }

            H[tag][grade] = {}
            for sgn in SIGNS:
                q_sq = mul(q[sgn], q[sgn])
                H[tag][grade][sgn] = mat_trunc(
                    [
                        [scale(d[sgn], Fraction(2, 1) / pi_value), scale(e[sgn], Fraction(1, 2) / pi_value)],
                        [
                            scale(e[sgn], Fraction(1, 2) / pi_value),
                            scale(add(g[sgn], scale(mul(q_sq, d[sgn]), Fraction(6))), Fraction(1, 12) / pi_value),
                        ],
                    ]
                )

            raw11 = scale(mul(cos_delta, eta), Fraction(-2, 1) / pi_value)
            raw12_num = add(
                add(mul(cos_delta, eta), mul(mul(s_poly, cos_delta), d["+"])),
                scale(mul(mul(mul(q["+"], s_poly), sin_delta), eta), Fraction(-1)),
            )
            raw21_num = add(
                add(mul(cos_delta, eta), mul(mul(s_poly, cos_delta), d["-"])),
                scale(mul(mul(mul(q["-"], s_poly), sin_delta), eta), Fraction(-1)),
            )
            raw22_num = add(
                add(
                    mul(sub(mul(s_poly, cos_delta), mul(mul(mul(s2_poly, q["+"]), sin_delta), const(Fraction(1)))), d["-"]),
                    mul(sub(mul(s_poly, cos_delta), mul(mul(mul(s2_poly, q["-"]), sin_delta), const(Fraction(1)))), d["+"]),
                ),
                mul(
                    add(
                        scale(mul(mul(add(q["-"], q["+"]), s_poly), sin_delta), Fraction(-1)),
                        mul(sub(const(Fraction(2)), mul(mul(q["-"], q["+"]), s2_poly)), cos_delta),
                    ),
                    eta,
                ),
            )
            raw_entries = [
                [raw11, scale(raw12_num, Fraction(1, 1) / pi_value)],
                [scale(raw21_num, Fraction(-1, 1) / pi_value), scale(raw22_num, Fraction(1, 2) / pi_value)],
            ]
            raw_divs = [[1, 2], [2, 3]]
            scaled_entries = [[zero(), zero()], [zero(), zero()]]
            scale_after = [[q_value**2, q_value], [q_value, Fraction(1)]]
            for i in range(2):
                for j in range(2):
                    divided, bad = div_by_s_power(raw_entries[i][j], raw_divs[i][j], q_value)
                    if bad:
                        m_bad.extend([f"M_tag{tag}_grade{grade}_{i+1}{j+1}:{b}" for b in bad])
                    scaled_entries[i][j] = scale(divided, scale_after[i][j])
            M[tag][grade] = mat_trunc(scaled_entries)

    return {
        "normalization": {
            "coordinate": "ordinary z with s=z/Q^2",
            "pre_Phi_K": True,
            "mixed_input": "M_i^[a] = Gr_a(mathfrak D_Q delta N_i^lin)",
            "tags": list(TAGS),
            "grades": list(GRADES),
            "order": ORDER,
        },
        "minimal_scalar_inputs": {
            "baseline": [f"q{k}=q_0^({k})(m)" for k in range(BASE_DERIV_ORDER + 1)],
            "source": [
                f"r{tag}_{grade}_{k}=(r_i^[{grade}])^({k})(m)"
                for tag in TAGS
                for grade in GRADES
                for k in range(SOURCE_DERIV_MIN, SOURCE_DERIV_MAX + 1)
            ],
            "counts": {
                "baseline_q_derivatives": BASE_DERIV_ORDER + 1,
                "source_r_derivatives": len(TAGS) * len(GRADES) * (SOURCE_DERIV_MAX - SOURCE_DERIV_MIN + 1),
                "total": (BASE_DERIV_ORDER + 1)
                + len(TAGS) * len(GRADES) * (SOURCE_DERIV_MAX - SOURCE_DERIV_MIN + 1),
            },
        },
        "derived_relations": {
            "q_pm": "q_0(m +/- z/(2Q^2))",
            "Delta0": "Phi_0(t_-)-Phi_0(t_+) = sum q_k (x_-^(k+1)-x_+^(k+1))/(k+1)!",
            "d_e_g": "d=r(t_pm), e=r'(t_pm), g=r''(t_pm)",
            "eta": "eta=int_{t_+}^{t_-} r(u)du = sum r_k (x_-^(k+1)-x_+^(k+1))/(k+1)!",
        },
        "removable_singularity_check": {
            "N0_negative_powers": n0_bad,
            "M_negative_powers": m_bad,
            "passed": not n0_bad and not m_bad,
        },
        "source_leading_terms": source_leading,
        "tables": {
            "G0": {sgn: format_matrix_coeffs(G0[sgn]) for sgn in SIGNS},
            "N0": format_matrix_coeffs(N0),
            "deltaG_lin": {
                tag: {grade: {sgn: format_matrix_coeffs(H[tag][grade][sgn]) for sgn in SIGNS} for grade in GRADES}
                for tag in TAGS
            },
            "M_scaled": {
                tag: {grade: format_matrix_coeffs(M[tag][grade]) for grade in GRADES}
                for tag in TAGS
            },
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="optional JSON with Q, pi, q[0..9], and r[tag][grade][0..9]")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    if args.input:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        input_kind = "user-supplied"
    else:
        data = default_demo_input()
        input_kind = "built-in-admissible-demo"

    result = build_tables(data)
    result["input_kind"] = input_kind
    result["script"] = str(Path(__file__))
    result["script_sha1"] = sha1(Path(__file__))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "input_kind": input_kind,
        "script_sha1": result["script_sha1"],
        "minimal_scalar_input_count": result["minimal_scalar_inputs"]["counts"],
        "removable_singularity_check": result["removable_singularity_check"],
        "output": str(args.out),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
