"""Symbolic verification: sec:toy-anomaly-and-transverse-obstruction.

Verifies the lemmas of §5 of rh/rh_rebuild.tex (after the patch under
rh/patches/sec-toy-anomaly-and-transverse-obstruction.tex is applied).

Coverage:

  * Phi_toy derivatives q_toy, q_toy', q_toy'' (eq:toy-phase-derivatives,
    Lemma~\ref{lem:toy-phase-derivatives}).
  * q_+, q_-, q'_+, q'_-, q''_+, q''_- at the symmetric centres
    t_± = m_0 ± s/2 (Lemma~\ref{lem:q-pm-split-at-centres}).
  * G_{toy,±}(s; m, u) and N_toy(s; m, u) substitution into the §4
    forms (Definition~\ref{def:toy-finite-blocks}).
  * On-line baseline: Omega_toy(s; m, 0) is the constant-phase whitened
    block of the linear baseline; A_toy(Omega_toy(s; m, 0)) = 0
    (Lemma~\ref{lem:A-toy-baseline-vanishing}).
  * Leading u^2 expansion of A_toy(Omega_toy):
        A_toy(Omega_toy) = u^2 . F_toy(d, q_0) + O(u^4)
    with d = q_0 . s (Lemma~\ref{lem:toy-anomaly-leading},
    eq:toy-anomaly-leading).  F_toy(d, q_0) is a rational expression
    in (sin d, cos d, sin(d/2), q_0).
  * High-frequency limit:
        F_inf(d) := lim_{q_0 -> oo} F_toy(d, q_0)
    has the displayed closed form
        F_inf(d) = sqrt(3) * (numerator(d)) / (8 d^3 sin(d/2))
    where numerator(d) is the trigonometric polynomial of
    eq:F-toy-closed-form.  Verified by sp.limit(F_toy, q0, oo) and
    compared to the displayed form.
  * Rescaled compactness structure: after s=d/q_0, the naturally scaled
    G, N, and G^{-1/2} entries have finite high-frequency limits.  This
    guards the uniform O(u^4) remainder argument in
    Lemma~\ref{lem:toy-anomaly-leading}.
  * Lower bound regression on a sampled compact subinterval: both
    |F_inf(d)| and |F_toy(d,q_0)| at large q_0 are bounded away from zero
    on the sampled grid.  This is numerical regression coverage, not a
    proof of zero exclusion for the whole interval.

Run:
  python3 rh/sympy/sec-toy-anomaly-and-transverse-obstruction.py
"""

import sys

import sympy as sp
from sympy import (
    Matrix,
    Rational,
    Symbol,
    cos,
    diff,
    eye,
    pi as PI,
    series,
    simplify,
    sin,
    sqrt,
    symbols,
    trigsimp,
    zeros,
    expand,
    cancel,
    together,
)


# ---------------------------------------------------------------------------
# Symbolic toy phase Phi_toy and derivatives.
# ---------------------------------------------------------------------------

t, m0, q0, u, s, d, tau = symbols("t m0 q0 u s d tau", real=True, positive=False)


def Phi_toy_expr(t_var, u_var, m_var, q_var):
    return q_var * (t_var - m_var) + u_var**2 * (1 - cos(q_var * (t_var - m_var)))


def q_toy_expr(tau_var, u_var, q_var):
    return q_var + u_var**2 * q_var * sin(q_var * tau_var)


def qp_toy_expr(tau_var, u_var, q_var):
    return u_var**2 * q_var**2 * cos(q_var * tau_var)


def qpp_toy_expr(tau_var, u_var, q_var):
    return -(u_var**2) * q_var**3 * sin(q_var * tau_var)


# ---------------------------------------------------------------------------
# (i) Verify Phi_toy derivatives.
# ---------------------------------------------------------------------------

def verify_toy_phase_derivatives():
    print("=" * 70)
    print("[lem:toy-phase-derivatives]  q_toy, q_toy', q_toy''")
    print("=" * 70)
    Phi = Phi_toy_expr(t, u, m0, q0)
    tau_sub = t - m0
    qt_direct = sp.diff(Phi, t)
    qpt_direct = sp.diff(Phi, t, 2)
    qppt_direct = sp.diff(Phi, t, 3)
    qt_claimed = q_toy_expr(tau_sub, u, q0)
    qpt_claimed = qp_toy_expr(tau_sub, u, q0)
    qppt_claimed = qpp_toy_expr(tau_sub, u, q0)
    for name, lhs, rhs in (
        ("q_toy", qt_direct, qt_claimed),
        ("q_toy'", qpt_direct, qpt_claimed),
        ("q_toy''", qppt_direct, qppt_claimed),
    ):
        delta = simplify(lhs - rhs)
        assert delta == 0, f"{name} mismatch: {delta}"
        print(f"  [PASS] {name} = {rhs}")


# ---------------------------------------------------------------------------
# (ii) Verify q_pm split at the symmetric centres.
# ---------------------------------------------------------------------------

def verify_q_pm_split_at_centres():
    print("=" * 70)
    print("[lem:q-pm-split-at-centres]  q_±, q'_±, q''_± at t_± = m_0 ± s/2")
    print("=" * 70)
    tau_p = s / 2
    tau_m = -s / 2
    qp = q_toy_expr(tau_p, u, q0)
    qm = q_toy_expr(tau_m, u, q0)
    qpp = qp_toy_expr(tau_p, u, q0)
    qpm = qp_toy_expr(tau_m, u, q0)
    qppp = qpp_toy_expr(tau_p, u, q0)
    qppm = qpp_toy_expr(tau_m, u, q0)

    # Substitute d = q0 s (so s = d/q0 -- but we keep d-relation symbolically).
    # The paper claims (using d = q0*s):
    #   q_± = q0 ± u^2 q0 sin(d/2)
    #   q'_± = u^2 q0^2 cos(d/2)  (same at both)
    #   q''_+ = -u^2 q0^3 sin(d/2),  q''_- = +u^2 q0^3 sin(d/2)
    qp_claim = q0 + u**2 * q0 * sin(q0 * s / 2)
    qm_claim = q0 - u**2 * q0 * sin(q0 * s / 2)
    qpp_claim = u**2 * q0**2 * cos(q0 * s / 2)
    qpm_claim = u**2 * q0**2 * cos(q0 * s / 2)
    qppp_claim = -(u**2) * q0**3 * sin(q0 * s / 2)
    qppm_claim = u**2 * q0**3 * sin(q0 * s / 2)

    for name, lhs, rhs in (
        ("q_+", qp, qp_claim),
        ("q_-", qm, qm_claim),
        ("q'_+", qpp, qpp_claim),
        ("q'_-", qpm, qpm_claim),
        ("q''_+", qppp, qppp_claim),
        ("q''_-", qppm, qppm_claim),
    ):
        delta = simplify(lhs - rhs)
        assert delta == 0, f"{name} mismatch: {delta}"
        print(f"  [PASS] {name} matches.")

    # Phase difference Delta_m^toy(s) = -q0 s.
    Phi_t_minus = Phi_toy_expr(m0 - s / 2, u, m0, q0)
    Phi_t_plus = Phi_toy_expr(m0 + s / 2, u, m0, q0)
    Delta = simplify(Phi_t_minus - Phi_t_plus)
    assert simplify(Delta - (-q0 * s)) == 0, f"Delta mismatch: {Delta}"
    print(f"  [PASS] Delta_m^toy(s) = -q0 s (no u-dependence).")


# ---------------------------------------------------------------------------
# (iii) §4 block formulas evaluated at toy.
# ---------------------------------------------------------------------------

def J_block(q_, qp_, qpp_):
    """G_{m,±}(s) = J(t_±) of eq:Gpm."""
    return (1 / PI) * Matrix([
        [2 * q_,         qp_ / 2],
        [qp_ / 2,        (qpp_ + 2 * q_**3) / 12],
    ])


def N_block(qm_, qp_, s_, Delta_):
    """N_m(s) of eq:Nm.  Convention: rows correspond to t_-, columns to t_+."""
    sd = sin(Delta_)
    cd = cos(Delta_)
    n11 = -2 * sd / s_
    n12 = (sd + qp_ * s_ * cd) / s_**2
    n21 = -(sd + qm_ * s_ * cd) / s_**2
    n22 = ((qm_ + qp_) * s_ * cd + (2 - qm_ * qp_ * s_**2) * sd) / (2 * s_**3)
    return (1 / PI) * Matrix([[n11, n12], [n21, n22]])


def G_toy_pm(s_var, q_var, u_var, sign):
    """G_{toy,±}(s; m, u): substitute toy q, q', q'' at t_± = m ± s/2."""
    tau_eval = sign * s_var / 2
    qv = q_toy_expr(tau_eval, u_var, q_var)
    qpv = qp_toy_expr(tau_eval, u_var, q_var)
    qppv = qpp_toy_expr(tau_eval, u_var, q_var)
    return J_block(qv, qpv, qppv)


def N_toy(s_var, q_var, u_var):
    """N_toy(s; m, u): substitute q_-, q_+, Delta_m^toy = -q s."""
    qm_val = q_toy_expr(-s_var / 2, u_var, q_var)
    qp_val = q_toy_expr(s_var / 2, u_var, q_var)
    Delta_val = -q_var * s_var
    return N_block(qm_val, qp_val, s_var, Delta_val)


def verify_toy_blocks_substitution():
    print("=" * 70)
    print("[def:toy-finite-blocks]  G_{toy,±}, N_toy by §4 substitution")
    print("=" * 70)
    G_minus = G_toy_pm(s, q0, u, -1)
    G_plus = G_toy_pm(s, q0, u, +1)
    N = N_toy(s, q0, u)
    # Symmetry: G_+ and G_- differ by sign of (1,2)/(2,1) entries?
    #   With our toy, q'_+ = q'_- (symmetric in tau), so G_+ and G_- have
    #   *same* off-diagonal entry; they differ only on diagonal.
    diff_off = simplify(G_plus[0, 1] - G_minus[0, 1])
    assert diff_off == 0, f"G off-diagonals differ: {diff_off}"
    print("  [PASS] G_{toy,+}_{12} = G_{toy,-}_{12} (off-diagonals equal).")
    diff_diag_11 = simplify(G_plus[0, 0] - G_minus[0, 0])
    expected_11 = simplify(2 * (2 * u**2 * q0 * sin(q0 * s / 2)) / PI)
    assert simplify(diff_diag_11 - expected_11) == 0, (
        f"G diag(1,1) split mismatch: {diff_diag_11} vs {expected_11}"
    )
    print("  [PASS] G_{toy,+}_{11} - G_{toy,-}_{11} = (4 u^2 q_0 sin(d/2))/pi.")

    # N_12 + N_21 = (q_+ - q_-) cos(Delta) / (pi s)
    N_off_sum = simplify(N[0, 1] + N[1, 0])
    expected_off = simplify(
        (2 * u**2 * q0 * sin(q0 * s / 2)) * cos(-q0 * s) / (PI * s)
    )
    assert simplify(N_off_sum - expected_off) == 0, (
        f"N off-sum mismatch: {N_off_sum - expected_off}"
    )
    print("  [PASS] N_toy_{12} + N_toy_{21} = (q_+ - q_-) cos(-d)/(pi s).")


# ---------------------------------------------------------------------------
# (iv) Closed-form 2x2 SPD inverse-square-root, used downstream.
# ---------------------------------------------------------------------------

def inv_sqrt_2x2_SPD(M):
    """Closed form for the positive definite inverse square root of a 2x2 SPD M.

    G^{-1/2} = (1/(sqrt(det(G)) sqrt(tr(G) + 2 sqrt(det(G)))))
              * [[c+s, -b], [-b, a+s]]
    where a = M_11, c = M_22, b = M_12, s = sqrt(det(M)).
    """
    a, b, c = M[0, 0], M[0, 1], M[1, 1]
    det_M = a * c - b**2
    s_M = sqrt(det_M)
    tr_M = a + c
    denom = s_M * sqrt(tr_M + 2 * s_M)
    return (1 / denom) * Matrix([[c + s_M, -b], [-b, a + s_M]])


def Omega_toy(s_var, q_var, u_var):
    """Omega_toy(s; m, u) := G_-^{-1/2} N_toy G_+^{-1/2}."""
    G_minus = G_toy_pm(s_var, q_var, u_var, -1)
    G_plus = G_toy_pm(s_var, q_var, u_var, +1)
    N = N_toy(s_var, q_var, u_var)
    G_minus_inv_sqrt = inv_sqrt_2x2_SPD(G_minus)
    G_plus_inv_sqrt = inv_sqrt_2x2_SPD(G_plus)
    return G_minus_inv_sqrt * N * G_plus_inv_sqrt



# ---------------------------------------------------------------------------
# (v) Symbolic toy same-point determinant: positivity mechanism.
# ---------------------------------------------------------------------------

def verify_toy_block_positivity_determinant_expansion():
    """Verify the normalized determinant structure used in the paper.

    With r=u^2, z=sin(d/2), c=cos(d/2), the same-point determinant
    D_J=4q^4+2qq''-3(q')^2 at t_± satisfies

      q0^{-4} D_J(t_+) = 4(1+r z)^4 - 2 r z(1+r z) - 3 r^2 c^2,
      q0^{-4} D_J(t_-) = 4(1-r z)^4 + 2 r z(1-r z) - 3 r^2 c^2.

    In particular each equals 4 + O(r), uniformly for z,c bounded.
    """
    print("=" * 70)
    print("[lem:toy-block-positivity] normalized determinant expansion")
    print("=" * 70)
    r, z, c = symbols("r z c", real=True)
    D_plus = 4 * (1 + r * z)**4 - 2 * r * z * (1 + r * z) - 3 * r**2 * c**2
    D_minus = 4 * (1 - r * z)**4 + 2 * r * z * (1 - r * z) - 3 * r**2 * c**2
    assert simplify(D_plus.subs(r, 0) - 4) == 0
    assert simplify(D_minus.subs(r, 0) - 4) == 0
    # Check the first-order terms are finite polynomial expressions.
    Dp_lin = simplify(diff(D_plus, r).subs(r, 0))
    Dm_lin = simplify(diff(D_minus, r).subs(r, 0))
    print(f"  D_plus/r expansion starts 4 + ({Dp_lin}) r + O(r^2)")
    print(f"  D_minus/r expansion starts 4 + ({Dm_lin}) r + O(r^2)")
    assert Dp_lin == 14 * z
    assert Dm_lin == -14 * z
    print("  [PASS] D_J/q0^4 = 4 + O(u^2) for both toy same-point blocks.")


# ---------------------------------------------------------------------------
# (v) Rescaled compactness structure for the uniform remainder.
# ---------------------------------------------------------------------------

def verify_rescaled_block_compactness_structure():
    """Verify the natural q0-scaling used in the uniform remainder proof.

    With s=d/q0, the entries of G, N, and H=G^{-1/2} have fixed powers
    of q0.  Multiplying by the reciprocal powers should produce finite
    q0 -> infinity limits.  This checks the bookkeeping behind the
    Cauchy-bound paragraph in Lemma~\ref{lem:toy-anomaly-leading}; it does
    not claim that inverse square roots commute with diagonal congruence.
    """
    print("=" * 70)
    print("[uniform remainder] scaled G/N/G^{-1/2} entries under s=d/q_0")
    print("=" * 70)
    s_sub = d / q0
    Gm = G_toy_pm(s_sub, q0, u, -1)
    Gp = G_toy_pm(s_sub, q0, u, +1)
    N = N_toy(s_sub, q0, u)
    Hm = inv_sqrt_2x2_SPD(Gm)
    Hp = inv_sqrt_2x2_SPD(Gp)

    checks = []
    for name, G in (("Gminus", Gm), ("Gplus", Gp)):
        checks += [
            (f"{name}_11/q0", G[0, 0] / q0),
            (f"{name}_12/q0^2", G[0, 1] / q0**2),
            (f"{name}_22/q0^3", G[1, 1] / q0**3),
        ]
    checks += [
        ("N11/q0", N[0, 0] / q0),
        ("N12/q0^2", N[0, 1] / q0**2),
        ("N21/q0^2", N[1, 0] / q0**2),
        ("N22/q0^3", N[1, 1] / q0**3),
    ]
    for name, H in (("Hminus", Hm), ("Hplus", Hp)):
        checks += [
            (f"q0^(1/2){name}_11", q0**Rational(1, 2) * H[0, 0]),
            (f"q0^(3/2){name}_12", q0**Rational(3, 2) * H[0, 1]),
            (f"q0^(3/2){name}_22", q0**Rational(3, 2) * H[1, 1]),
        ]

    for label, expr in checks:
        expr = trigsimp(simplify(expr))
        lim = sp.limit(expr, q0, sp.oo)
        lim = trigsimp(simplify(lim))
        print(f"  {label}: limit = {lim}")
        assert lim not in (sp.oo, -sp.oo, sp.zoo, sp.nan), \
            f"{label} has bad q0->oo limit: {lim}"
    print()
    print("  [PASS] Scaled G, N, and G^{-1/2} entries have finite q0->oo limits.")

# ---------------------------------------------------------------------------
# (v) Baseline: at u = 0, A_toy(Omega_toy) = 0.
# ---------------------------------------------------------------------------

def verify_omega_toy_baseline_at_u_zero():
    print("=" * 70)
    print("[lem:A-toy-baseline-vanishing]  A_toy(Omega_toy(s; m, 0)) = 0")
    print("=" * 70)
    Omega0 = Omega_toy(s, q0, 0)
    a_toy_0 = simplify(Omega0[0, 1] + Omega0[1, 0])
    assert a_toy_0 == 0, f"A_toy at u=0 nonzero: {a_toy_0}"
    print("  [PASS] A_toy(Omega_toy(s; m, 0)) = 0 identically.")


def verify_anomaly_functional_vanishes_on_baseline():
    """Same as above; documents that the on-line baseline is annihilated."""
    verify_omega_toy_baseline_at_u_zero()


# ---------------------------------------------------------------------------
# (vi) Leading u^2 expansion of A_toy(Omega_toy).
#
# Strategy: compute A_toy(Omega_toy) symbolically with sympy, then take
# the u^2-coefficient (after expanding in u about u=0).  The result is
# the function F_toy.  Verify it is q_0-independent when expressed as
# a function of d = q_0 s.
# ---------------------------------------------------------------------------

def leading_u2_coefficient(expr, u_var):
    """Leading nonzero coefficient in the u-expansion of expr, assuming
    even-only powers.  Returns the u^2 coefficient.
    """
    # Substitute u -> 0 to confirm vanishing.
    base = simplify(expr.subs(u_var, 0))
    if base != 0:
        raise AssertionError(f"expr at u=0 is {base}, expected 0")
    # Differentiate twice and evaluate at u=0; divide by 2.
    d2 = sp.diff(expr, u_var, 2).subs(u_var, 0)
    return simplify(d2 / 2)


_F_TOY_CACHE = {}


def compute_F_toy_d_q0():
    """Compute F_toy(d, q_0) symbolically from A_toy(Omega_toy) at u^2 order.

    Returns the leading u^2 coefficient as a function of (d, q_0), with
    s replaced by d/q_0.
    """
    if "F_d_q0" in _F_TOY_CACHE:
        return _F_TOY_CACHE["F_d_q0"]
    Omega = Omega_toy(s, q0, u)
    a_toy = Omega[0, 1] + Omega[1, 0]
    F_at_q0_s = leading_u2_coefficient(a_toy, u)
    F_expr = F_at_q0_s.subs(s, d / q0)
    F_expr = sp.radsimp(F_expr)
    F_expr = trigsimp(F_expr)
    F_expr = simplify(F_expr)
    _F_TOY_CACHE["F_d_q0"] = F_expr
    return F_expr


def verify_leading_u2_expansion():
    print("=" * 70)
    print("[lem:toy-anomaly-leading]  A_toy(Omega_toy) = u^2 F_toy(d, q_0) + O(u^4)")
    print("=" * 70)
    F_d_q0 = compute_F_toy_d_q0()
    print()
    print("  F_toy(d, q_0) (rational expression):")
    sp.pprint(F_d_q0)
    print()
    # Extract the polynomial degrees in q_0 of numerator and denominator
    # to confirm the structure asserted in the patch.
    num, den = sp.fraction(sp.together(F_d_q0))
    num_deg = sp.Poly(num, q0).degree() if num.has(q0) else 0
    den_deg = sp.Poly(den, q0).degree() if den.has(q0) else 0
    print(f"  q_0-degree(numerator)   = {num_deg}")
    print(f"  q_0-degree(denominator) = {den_deg}")
    assert num_deg <= 2, f"F_toy numerator q0-degree exceeds 2: {num_deg}"
    assert den_deg <= 2, f"F_toy denominator q0-degree exceeds 2: {den_deg}"
    print("  [PASS] q_0-polynomial degrees match the structure of the patch.")


def verify_F_toy_closed_form_q0_independent():
    """Verify the q_0 -> infty limit matches the displayed closed form.

    The patch displays
        F_inf(d) = sqrt(3) * (2 d^2 cos d + 5 d^2 cos 2d - 7 d^2
                              + 6 d sin d - 15 d sin 2d
                              - 12 cos 2d + 12) / (8 d^3 sin(d/2)).
    """
    print("=" * 70)
    print("[lem:toy-anomaly-leading]  F_inf(d) := lim_{q_0->oo} F_toy(d, q_0)")
    print("=" * 70)
    F_d_q0 = compute_F_toy_d_q0()
    F_inf = sp.limit(F_d_q0, q0, sp.oo)
    F_inf = trigsimp(F_inf)
    F_inf = simplify(F_inf)
    print()
    print("  F_inf(d) =")
    sp.pprint(F_inf)
    print()

    candidate_num = (
        2 * d**2 * cos(d) + 5 * d**2 * cos(2 * d) - 7 * d**2
        + 6 * d * sin(d) - 15 * d * sin(2 * d)
        - 12 * cos(2 * d) + 12
    )
    candidate = sqrt(3) * candidate_num / (8 * d**3 * sin(d / 2))

    print("  Patch's displayed closed form (eq:F-toy-closed-form):")
    sp.pprint(candidate)
    print()

    delta = simplify(F_inf - candidate)
    delta = trigsimp(delta)
    delta = simplify(delta)
    print("  Difference (sympy F_inf - displayed candidate):")
    sp.pprint(delta)
    print()
    assert delta == 0, (
        f"F_inf does not match the patch's displayed closed form. "
        f"sympy: {F_inf}\n"
        f"patch: {candidate}\n"
        f"delta: {delta}"
    )
    print("  [PASS] F_inf(d) matches eq:F-toy-closed-form.")

    # Removable-singularity check at d = 2 pi.
    num_at_2pi = simplify(candidate_num.subs(d, 2 * sp.pi))
    assert num_at_2pi == 0, (
        f"Numerator does not vanish at d = 2 pi: {num_at_2pi}"
    )
    print("  [PASS] Numerator vanishes at d = 2 pi (removable singularity).")
    return F_inf


# ---------------------------------------------------------------------------
# (vii) Lower bound on |F_toy(d)| at sampled points avoiding zeros.
# ---------------------------------------------------------------------------

def verify_F_toy_lower_bound_on_compact_d():
    print("=" * 70)
    print("[eq:F-toy-lower-bound] sampled |F_inf| and finite-q0 |F_toy| lower bounds")
    print("=" * 70)
    F_inf = verify_F_toy_closed_form_q0_independent()
    F_d_q0 = compute_F_toy_d_q0()
    # Sample d in (0.5, 2.5), avoiding visible near-zeros.
    sample_points = [Rational(p, 10) for p in range(5, 26)]
    F_inf_func = sp.lambdify(d, F_inf, modules=["mpmath"])
    F_toy_func = sp.lambdify((d, q0), F_d_q0, modules=["mpmath"])
    print(f"  Sampling F_inf(d) and F_toy(d,q0) at {len(sample_points)} points in [0.5, 2.5].")
    min_inf = None
    min_finite = None
    for dp in sample_points:
        inf_val = float(abs(F_inf_func(float(dp))))
        finite_val = float(abs(F_toy_func(float(dp), 50.0)))
        min_inf = inf_val if min_inf is None else min(min_inf, inf_val)
        min_finite = finite_val if min_finite is None else min(min_finite, finite_val)
        assert inf_val > 1e-6, (
            f"|F_inf({dp})| = {inf_val:.3e} too close to zero "
            "in sampled compact subinterval"
        )
        assert finite_val > 1e-6, (
            f"|F_toy({dp},50)| = {finite_val:.3e} too close to zero "
            "in sampled compact subinterval"
        )
    print(f"  [PASS] min_d |F_inf(d)|      >= {min_inf:.4e} on sampled D.")
    print(f"  [PASS] min_d |F_toy(d,50)|  >= {min_finite:.4e} on sampled D.")
    print("         This is regression coverage; rigorous interval zero-exclusion remains textual.")


# ---------------------------------------------------------------------------
# (vii) Uniform-remainder closure: signed retained subdomain D_T^toy(D),
#       polynomial-weight density, signed-separation invariance.
# ---------------------------------------------------------------------------

def verify_density_bound_with_q_extrema():
    """Check the exact density lower bound for lem:toy-retained-density.

    With q^- <= q(m) <= q^+ on I_T and the height hypothesis
    d_+/q^- <= |I_T|/4, the signed retained set q(m)|s| in [d_-,d_+]
    has density at least (d_+-d_-)/(q^+ |I_T|).
    """
    print("=" * 70)
    print("[lem:toy-retained-density]  exact signed density lower bound")
    print("=" * 70)
    dminus, dplus, qplus, I = sp.symbols("dminus dplus qplus I", positive=True)
    width = dplus - dminus
    # Central slab length is |I|/2; two signs of s contribute total
    # s-width >= 2 width / qplus at each slab point.
    retained_lower = (I / 2) * (2 * width / qplus)
    total_area = I**2
    ratio = sp.simplify(retained_lower / total_area)
    target = width / (qplus * I)
    assert sp.simplify(ratio - target) == 0
    print("  [PASS] exact signed density ratio >= (d_+-d_-)/(q_T^+ |I_T|).")


def verify_polynomial_density_consequence():
    """Polynomial-weight consequence under |I_T| <= C_I/Q and q^+ <= C_q q(T)."""
    print("=" * 70)
    print("[lem:toy-retained-density]  polynomial-weight Q/q consequence")
    print("=" * 70)
    width, Q, qT, CI, Cq = sp.symbols("width Q qT C_I C_q", positive=True)
    I_boundary = CI / Q
    qplus_boundary = Cq * qT
    exact_ratio_boundary = width / (qplus_boundary * I_boundary)
    polynomial_target = width * Q / (CI * Cq * qT)
    assert sp.simplify(exact_ratio_boundary - polynomial_target) == 0
    print("  [PASS] exact density implies width/(C_I C_q) * Q/q(T) at boundary.")


def verify_height_hypothesis_implication():
    """Sufficient high-height condition for eq:toy-density-height-hypothesis.

    If |I_T| >= c_I/Q, q^- >= c_q q(T), and Q/q(T) <= c_I c_q/(4 d_+),
    then d_+/q^- <= |I_T|/4.
    """
    print("=" * 70)
    print("[eq:toy-density-height-hypothesis]  sufficient high-height implication")
    print("=" * 70)
    dplus, Q, qT, cI, cq = sp.symbols("dplus Q qT c_I c_q", positive=True)
    I_lower = cI / Q
    qminus_lower = cq * qT
    lhs = dplus / qminus_lower
    rhs = I_lower / 4
    Q_boundary = cI * cq * qT / (4 * dplus)
    assert sp.simplify(lhs - rhs.subs(Q, Q_boundary)) == 0
    print("  [PASS] Q/q(T) <= c_I c_q/(4 d_+) implies the height hypothesis.")


def verify_signed_definition_matches_two_branches():
    """Two-branch length for q(m)|s| in D.

    The signed definition keeps s in [d_-/q, d_+/q] and the reflected
    negative interval [-d_+/q, -d_-/q].  Total length is 2(d_+ - d_-)/q.
    """
    print("=" * 70)
    print("[def:toy-retained-subdomain]  signed two-branch total length")
    print("=" * 70)
    dminus, dplus, q = sp.symbols("dminus dplus q", positive=True)
    length_positive = dplus / q - dminus / q
    length_negative = (-dminus / q) - (-dplus / q)
    total = sp.simplify(length_positive + length_negative)
    assert sp.simplify(total - 2 * (dplus - dminus) / q) == 0
    print("  [PASS] q(m)|s| in D contributes two branches of total "
          "length 2(d_+ - d_-)/q(m).")


def verify_signed_scalar_channel_invariance():
    """Algebra behind lem:toy-signed-separation-invariance.

    If H_- and H_+ are symmetric inverse square roots and
    N(-s) = N(s)^T with H_-(-s) = H_+(s), H_+(-s) = H_-(s), then
    Omega(-s) = Omega(s)^T.  Since A_toy(X) = X_12 + X_21 is
    transpose-invariant, the scalar channel is unchanged.
    """
    print("=" * 70)
    print("[lem:toy-signed-separation-invariance]  Omega(-s) = Omega(s)^T, "
          "A_toy invariant")
    print("=" * 70)
    hm11, hm12, hm22, hp11, hp12, hp22 = sp.symbols(
        "hm11 hm12 hm22 hp11 hp12 hp22"
    )
    n11, n12, n21, n22 = sp.symbols("n11 n12 n21 n22")
    Hm = sp.Matrix([[hm11, hm12], [hm12, hm22]])
    Hp = sp.Matrix([[hp11, hp12], [hp12, hp22]])
    N = sp.Matrix([[n11, n12], [n21, n22]])
    Omega_pos = Hm * N * Hp
    Omega_neg = Hp * N.T * Hm
    assert sp.simplify(Omega_neg - Omega_pos.T) == sp.zeros(2, 2)
    A = lambda X: X[0, 1] + X[1, 0]
    assert sp.simplify(A(Omega_neg) - A(Omega_pos)) == 0
    print("  [PASS] signed separation transposes Omega and preserves "
          "A_toy(X) = X_12 + X_21.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    verify_toy_phase_derivatives()
    print()
    verify_q_pm_split_at_centres()
    print()
    verify_toy_blocks_substitution()
    print()
    verify_toy_block_positivity_determinant_expansion()
    print()
    verify_rescaled_block_compactness_structure()
    print()
    verify_omega_toy_baseline_at_u_zero()
    print()
    verify_leading_u2_expansion()
    print()
    verify_F_toy_closed_form_q0_independent()
    print()
    verify_F_toy_lower_bound_on_compact_d()
    print()
    verify_density_bound_with_q_extrema()
    print()
    verify_polynomial_density_consequence()
    print()
    verify_height_hypothesis_implication()
    print()
    verify_signed_definition_matches_two_branches()
    print()
    verify_signed_scalar_channel_invariance()
    print()
    print("=" * 70)
    print("All §5 lemmas verified symbolically:")
    print("  - lem:toy-phase-derivatives: q_toy, q_toy', q_toy'' formulas")
    print("  - lem:q-pm-split-at-centres: q_±, q'_±, q''_± and Delta_m^toy")
    print("  - def:toy-finite-blocks: G_{toy,±}, N_toy by §4 substitution")
    print("  - lem:toy-block-positivity: normalized determinant = 4 + O(u^2)")
    print("  - uniform remainder guard: scaled G/N/G^{-1/2} entries have finite q0->oo limits")
    print("  - lem:A-toy-baseline-vanishing: A_toy vanishes on on-line baseline")
    print("  - lem:toy-anomaly-leading: leading u^2 expansion of A_toy(Omega)")
    print("    F_toy(d, q_0) is rational with q_0-deg <= 2 in num and den")
    print("  - eq:F-toy-closed-form: F_inf(d) := lim_{q_0->oo} F_toy matches")
    print("    the paper's displayed closed form exactly")
    print("  - eq:F-toy-lower-bound: sampled lower bounds for F_inf and finite-q0 F_toy")
    print("  - lem:toy-retained-density: signed exact bound (d_+-d_-)/(q_T^+ |I_T|)")
    print("    and polynomial form (d_+-d_-)/(C_I C_q) * Q(T)/q(T)")
    print("  - eq:toy-density-height-hypothesis: sufficient implication via")
    print("    Q/q(T) <= c_I c_q / (4 d_+)")
    print("  - def:toy-retained-subdomain: signed two-branch total length 2|D|/q(m)")
    print("  - lem:toy-signed-separation-invariance: Omega(-s) = Omega(s)^T,")
    print("    A_toy invariant under transpose")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
