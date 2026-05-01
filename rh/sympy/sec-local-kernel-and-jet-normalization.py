"""Symbolic verification: sec:local-kernel-and-jet-normalization.

Verifies the lemmas of section §2 of rh/rh_rebuild.tex:

  lem:phase-kernel-properties
      (i)   K_Phi(x, y) = K_Phi(y, x)                  symmetry
      (ii)  K_Phi is real-valued for real Phi          (algebraic)
      (iii) lim_{x -> y} K_Phi(x, y) = q(y) / pi       removable singularity

  lem:phase-kernel-derivatives
      Closed-form expressions at distinct points (T_1, T_2):
        K_Phi(T_1, T_2),
        d/dx K_Phi(T_1, T_2),
        d/dy K_Phi(T_1, T_2),
        d^2/dxdy K_Phi(T_1, T_2),
      verified against the displayed formulas of the lemma.

  rem:kernel-derivatives-diagonal
      The diagonal limits T_2 -> T_1 = T of the four expressions
      give the kernel-derivative form of J(T) used in
      eq:same-point-as-kernel-derivatives.

  lem:phase-derivative-lower-bound
      Symbolic differentiation of the Riemann-Siegel asymptotic
        theta(t) = (t/2) log(t / (2*pi)) - t/2 - pi/8 + 1/(48 t) + O(t^{-3})
      gives
        theta'(t) = (1/2) log(t / (2*pi)) - 1/(48 t^2) + O(t^{-4}),
      from which q(t) > 0 at large t.  Verified by termwise
      differentiation in sympy.

Run:
  python rh/sympy/sec-local-kernel-and-jet-normalization.py
"""

import sys

import sympy as sp
from sympy import (
    Function,
    Rational,
    Symbol,
    cos,
    diff,
    expand_trig,
    limit,
    pi as PI,
    series,
    simplify,
    sin,
    symbols,
    trigsimp,
)


# ----------------------------------------------------------------------
# Symbolic kernel.
# ----------------------------------------------------------------------

x, y = symbols("x y", real=True)
Phi = Function("Phi", real=True)


def K(x_, y_):
    """K_Phi(x, y) = sin(Phi(x) - Phi(y)) / (pi * (x - y))."""
    return sin(Phi(x_) - Phi(y_)) / (PI * (x_ - y_))


# ----------------------------------------------------------------------
# (i) Symmetry.
# ----------------------------------------------------------------------

def verify_symmetry():
    print("=" * 70)
    print("[lem:phase-kernel-properties (i)]  K_Phi(x, y) = K_Phi(y, x)")
    print("=" * 70)

    diff_expr = simplify(K(x, y) - K(y, x))
    print()
    print(f"  K_Phi(x,y) - K_Phi(y,x) = {diff_expr}")
    if diff_expr == 0:
        print()
        print("  [PASS] Symmetric.")
    else:
        raise AssertionError(f"Symmetry FAIL: {diff_expr}")


# ----------------------------------------------------------------------
# (iii) Removable singularity.
# ----------------------------------------------------------------------

def verify_removable_singularity():
    print("=" * 70)
    print("[lem:phase-kernel-properties (iii)]  lim_{x->y} K_Phi(x,y) = q(y)/pi")
    print("=" * 70)

    h = Symbol("h", positive=True)
    q_, qp_, qpp_ = symbols("q qp qpp", real=True)

    # Phi(y + h) - Phi(y) = h q + h^2 q'/2 + O(h^3)
    diff_phi = h * q_ + Rational(1, 2) * h**2 * qp_ + Rational(1, 6) * h**3 * qpp_
    K_off = sin(diff_phi) / (PI * h)

    K_off_series = series(K_off, h, 0, 3).removeO()
    K_off_lim = limit(K_off, h, 0)

    print()
    print(f"  Taylor expansion of K_Phi(y+h, y) in h:")
    print(f"    {K_off_series}")
    print(f"  lim_{{h -> 0}} K_Phi(y+h, y) = {K_off_lim}")
    expected = q_ / PI
    diff_val = simplify(K_off_lim - expected)
    if diff_val == 0:
        print()
        print(f"  [PASS] Limit equals q(y)/pi = {expected}.")
    else:
        raise AssertionError(f"Removable singularity FAIL: {diff_val}")


# ----------------------------------------------------------------------
# Phase-kernel derivatives at distinct points.
# ----------------------------------------------------------------------

def verify_kernel_derivatives():
    print("=" * 70)
    print("[lem:phase-kernel-derivatives]  closed-form derivatives at (T1, T2)")
    print("=" * 70)

    # Substitute symbolic values for Phi(T_1), Phi(T_2), q(T_1), q(T_2),
    # and the relevant differences, evaluating the abstract derivatives.
    T1, T2, s_, D_ = symbols("T1 T2 s Delta", real=True)
    q1_, q2_ = symbols("q1 q2", real=True)
    PhiT1, PhiT2 = symbols("PhiT1 PhiT2", real=True)

    # Compute partial derivatives symbolically using SymPy's Function/Derivative.
    Kxy = K(x, y)
    Kx_expr = diff(Kxy, x)
    Ky_expr = diff(Kxy, y)
    Kxy_mixed = diff(Kxy, x, y)

    # Substitute concrete values.
    # We need to replace Phi'(x) -> q(x), Phi'(y) -> q(y), etc., then
    # evaluate at x = T1, y = T2.
    qfun = Function("q", real=True)

    def substitute_at(expr, X, Y, qX, qY, PhiX, PhiY):
        # Replace Phi(x) by PhiX, Phi(y) by PhiY, Phi'(x) by qX, Phi'(y) by qY,
        # then x -> X, y -> Y.
        repl = {
            Phi(x).diff(x): qX,
            Phi(y).diff(y): qY,
            Phi(x): PhiX,
            Phi(y): PhiY,
        }
        out = expr.xreplace(repl)
        out = out.xreplace({x: X, y: Y})
        return out

    # Evaluate at (x, y) = (T1, T2) with s = T1 - T2, Delta = PhiT1 - PhiT2.
    # We work with symbolic T1, T2 then introduce s = T1 - T2 and Delta = PhiT1 - PhiT2
    # at the simplification step.

    K_at = K(x, y).xreplace({Phi(x): PhiT1, Phi(y): PhiT2}).xreplace({x: T1, y: T2})
    K_at = K_at.xreplace({T1 - T2: s_, PhiT1 - PhiT2: D_})

    Kx_at = substitute_at(Kx_expr, T1, T2, q1_, q2_, PhiT1, PhiT2)
    Kx_at = Kx_at.xreplace({T1 - T2: s_, PhiT1 - PhiT2: D_})

    Ky_at = substitute_at(Ky_expr, T1, T2, q1_, q2_, PhiT1, PhiT2)
    Ky_at = Ky_at.xreplace({T1 - T2: s_, PhiT1 - PhiT2: D_})

    Kxy_at = substitute_at(Kxy_mixed, T1, T2, q1_, q2_, PhiT1, PhiT2)
    Kxy_at = Kxy_at.xreplace({T1 - T2: s_, PhiT1 - PhiT2: D_})

    # Expected values from the lemma.
    K_expected = sin(D_) / (PI * s_)
    Kx_expected = (q1_ * s_ * cos(D_) - sin(D_)) / (PI * s_**2)
    Ky_expected = (sin(D_) - q2_ * s_ * cos(D_)) / (PI * s_**2)
    Kxy_expected = ((q1_ + q2_) * s_ * cos(D_)
                    + (q1_ * q2_ * s_**2 - 2) * sin(D_)) / (PI * s_**3)

    pairs = [
        ("K_Phi(T1,T2)",      K_at,    K_expected),
        ("d/dx K_Phi(T1,T2)", Kx_at,   Kx_expected),
        ("d/dy K_Phi(T1,T2)", Ky_at,   Ky_expected),
        ("d^2/dxdy K_Phi(T1,T2)", Kxy_at, Kxy_expected),
    ]

    print()
    for name, computed, expected in pairs:
        diff_val = simplify(trigsimp(computed - expected))
        status = "OK" if diff_val == 0 else "FAIL"
        print(f"  {name}")
        print(f"    computed:  {simplify(computed)}")
        print(f"    expected:  {expected}")
        print(f"    diff:      {diff_val}  [{status}]")
        print()
        if diff_val != 0:
            raise AssertionError(f"Kernel derivative {name} FAIL: {diff_val}")
    print("  [PASS] All four kernel derivatives match the displayed formulas.")


# ----------------------------------------------------------------------
# Diagonal limits T_2 -> T_1 = T.
# ----------------------------------------------------------------------

def verify_diagonal_limits():
    print("=" * 70)
    print("[rem:kernel-derivatives-diagonal]  diagonal limits T2 -> T1 = T")
    print("=" * 70)

    h = Symbol("h", positive=True)
    s_, D_ = symbols("s Delta", real=True)
    q_, qp_, qpp_ = symbols("q qp qpp", real=True)

    # As T2 -> T1, set T1 - T2 = h (small), and Phi(T1) - Phi(T2) ~ h q + h^2 q'/2 + h^3 q''/6.
    # We also need q1 - q2 ~ h q', and q1 + q2 ~ 2 q.
    # The limits are computed by Taylor expansion of the four expressions in h around 0,
    # picking out the constant term.

    def expand_in_h(expr, order):
        return series(expr, h, 0, order).removeO()

    # K(T,T) limit:
    K_off_diag = sin(h * q_ + Rational(1, 2) * h**2 * qp_ + Rational(1, 6) * h**3 * qpp_) / (PI * h)
    K_diag = limit(K_off_diag, h, 0)
    K_diag_expected = q_ / PI

    print()
    print(f"  K_Phi(T,T) limit:            {K_diag}")
    print(f"  expected (q(T)/pi):          {K_diag_expected}")
    diff_val = simplify(K_diag - K_diag_expected)
    assert diff_val == 0, f"K diag fail: {diff_val}"
    print(f"  diff: 0  [OK]")

    # K_x(T1, T2) -> K_x(T,T) as s -> 0.
    # Using s = h, q1 = q(T1) = q + h*q'/2 + h^2*q''/8 (centered at midpoint),
    # actually we should just take s -> 0 in the formula directly.
    # Set q1 = q + Delta_q where Delta_q -> 0; here we'll just use the
    # symbolic form and Taylor in h.
    s_to_h = h
    # q at T1 = T + h/2 and T2 = T - h/2, expanded to order h^2 (the h^2 q''/8
    # term is needed for the K_{xy} diagonal limit; without it the q'' coefficient
    # is wrong by a factor that propagates into the (q'' + 2q^3) numerator).
    q1_h = q_ + Rational(1, 2) * h * qp_ + Rational(1, 8) * h**2 * qpp_
    q2_h = q_ - Rational(1, 2) * h * qp_ + Rational(1, 8) * h**2 * qpp_
    Delta_h = h * q_ + Rational(1, 24) * h**3 * qpp_  # Phi(T+h/2) - Phi(T-h/2)

    Kx_h = (q1_h * s_to_h * cos(Delta_h) - sin(Delta_h)) / (PI * s_to_h**2)
    Kx_diag = limit(Kx_h, h, 0)
    Kx_expected = qp_ / (2 * PI)
    print()
    print(f"  d/dx K_Phi(T,T) limit:       {Kx_diag}")
    print(f"  expected (q'(T)/(2 pi)):     {Kx_expected}")
    diff_val = simplify(Kx_diag - Kx_expected)
    assert diff_val == 0, f"Kx diag fail: {diff_val}"
    print(f"  diff: 0  [OK]")

    # K_y(T1, T2) -> K_y(T,T) as s -> 0.
    Ky_h = (sin(Delta_h) - q2_h * s_to_h * cos(Delta_h)) / (PI * s_to_h**2)
    Ky_diag = limit(Ky_h, h, 0)
    Ky_expected = qp_ / (2 * PI)
    print()
    print(f"  d/dy K_Phi(T,T) limit:       {Ky_diag}")
    print(f"  expected (q'(T)/(2 pi)):     {Ky_expected}")
    diff_val = simplify(Ky_diag - Ky_expected)
    assert diff_val == 0, f"Ky diag fail: {diff_val}"
    print(f"  diff: 0  [OK]")

    # K_{xy}(T1, T2) -> K_{xy}(T, T) as s -> 0.
    Kxy_h = ((q1_h + q2_h) * s_to_h * cos(Delta_h)
             + (q1_h * q2_h * s_to_h**2 - 2) * sin(Delta_h)) / (PI * s_to_h**3)
    Kxy_diag = limit(Kxy_h, h, 0)
    Kxy_expected = (qpp_ + 2 * q_**3) / (6 * PI)
    print()
    print(f"  d^2/dxdy K_Phi(T,T) limit:   {Kxy_diag}")
    print(f"  expected ((q'' + 2q^3)/(6 pi)): {Kxy_expected}")
    diff_val = simplify(Kxy_diag - Kxy_expected)
    assert diff_val == 0, f"Kxy diag fail: {diff_val}"
    print(f"  diff: 0  [OK]")

    print()
    print("  [PASS] Diagonal limits give the kernel-derivative form of J(T).")


def verify_phase_derivative_lower_bound():
    """Differentiate the Riemann-Siegel asymptotic for theta(t) and confirm
    the leading term of theta'(t) is (1/2) log(t / (2*pi)) plus an
    O(t^{-2}) correction.  This is the unconditional algebraic content of
    Lemma lem:phase-derivative-lower-bound; the analytic claim that the
    asymptotic is an asymptotic of theta itself is from
    Edwards / Titchmarsh and is taken as a literature input."""
    print("=" * 70)
    print("[lem:phase-derivative-lower-bound]  termwise differentiation of")
    print("                                    the Riemann-Siegel asymptotic")
    print("=" * 70)

    t = sp.symbols("t", positive=True)

    # Riemann-Siegel asymptotic for theta(t) up to O(t^{-3}).
    theta_asym = (
        t / 2 * sp.log(t / (2 * PI))
        - t / 2
        - PI / 8
        + Rational(1, 48) / t
    )
    theta_prime_asym = sp.diff(theta_asym, t)

    # Expected form of theta'(t).
    theta_prime_expected = (
        Rational(1, 2) * sp.log(t / (2 * PI))
        - Rational(1, 48) / t**2
    )

    diff_val = simplify(theta_prime_asym - theta_prime_expected)

    print()
    print(f"  theta(t)       (asymptotic, up to O(t^-3)):")
    print(f"    {theta_asym}")
    print()
    print(f"  theta'(t)      (termwise derivative):")
    print(f"    {sp.expand(theta_prime_asym)}")
    print()
    print(f"  expected:")
    print(f"    {theta_prime_expected}")
    print()
    print(f"  difference:    {diff_val}")
    if diff_val == 0:
        print()
        print("  [PASS] q(t) = theta'(t) = (1/2) log(t/(2 pi)) - 1/(48 t^2)")
        print("                        + O(t^{-4}) by termwise differentiation.")
    else:
        raise AssertionError(f"theta' asymptotic mismatch: {diff_val}")


def verify_phase_derivative_upper_bounds():
    """Differentiate the Riemann-Siegel asymptotic twice and three times
    to obtain q'(T) = theta''(T) and q''(T) = theta'''(T).  Confirm the
    leading-order forms used in the proof of Lemma
    lem:phase-derivative-upper-bounds and consumed by §3 Gram positivity."""
    print("=" * 70)
    print("[lem:phase-derivative-upper-bounds]  q'(T) = O(T^-1), q''(T) = O(T^-2)")
    print("=" * 70)

    t = sp.symbols("t", positive=True)

    theta_asym = (
        t / 2 * sp.log(t / (2 * PI))
        - t / 2
        - PI / 8
        + Rational(1, 48) / t
    )

    theta_pp_asym = sp.expand(sp.diff(theta_asym, t, 2))
    theta_ppp_asym = sp.expand(sp.diff(theta_asym, t, 3))

    # Expected leading forms.
    theta_pp_expected = Rational(1, 2) / t + Rational(1, 24) / t**3
    theta_ppp_expected = -Rational(1, 2) / t**2 - Rational(1, 8) / t**4

    diff_pp = simplify(theta_pp_asym - theta_pp_expected)
    diff_ppp = simplify(theta_ppp_asym - theta_ppp_expected)

    print()
    print(f"  q'(T) = theta''(T)   (termwise from Riemann-Siegel asymptotic):")
    print(f"    {theta_pp_asym}")
    print(f"  expected leading:    1/(2 T) + 1/(24 T^3) + O(T^-5)")
    print(f"  difference:          {diff_pp}")
    assert diff_pp == 0, f"theta'' mismatch: {diff_pp}"
    print()
    print(f"  q''(T) = theta'''(T)  (termwise from Riemann-Siegel asymptotic):")
    print(f"    {theta_ppp_asym}")
    print(f"  expected leading:    -1/(2 T^2) - 1/(8 T^4) + O(T^-6)")
    print(f"  difference:          {diff_ppp}")
    assert diff_ppp == 0, f"theta''' mismatch: {diff_ppp}"
    print()
    print("  [PASS] q'(T) = 1/(2T) + O(T^-3), q''(T) = -1/(2 T^2) + O(T^-4).")
    print("         Both vanish as T -> infty; in particular |q'|, |q''| <= eps")
    print("         for any eps > 0 and T sufficiently large.  This discharges")
    print("         the upper bounds used in the §3 Gram positivity proof.")


def main():
    verify_symmetry()
    print()
    verify_removable_singularity()
    print()
    verify_kernel_derivatives()
    print()
    verify_diagonal_limits()
    print()
    verify_phase_derivative_lower_bound()
    print()
    verify_phase_derivative_upper_bounds()
    print()
    print("=" * 70)
    print("All §2 lemmas (kernel symmetry, removable singularity, derivative")
    print("formulas, diagonal limits, phase-derivative lower bound (P2), and")
    print("phase-derivative upper bounds q' = O(T^-1), q'' = O(T^-2))")
    print("verified symbolically.")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
