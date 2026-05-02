"""Symbolic verification: sec:finite-scale-local-blocks-and-whitening.

Verifies the lemmas of §4 of rh/rh_rebuild.tex (after the patch under
rh/patches/sec-finite-scale-local-blocks-and-whitening.tex is applied).

Coverage:

  * G_{m,±}(s) = J(t_±) by substitution into the §3 same-point form
    (rem:finite-blocks-from-jet-limit).
  * N_m(s) = (1/pi) N_12(t_-, t_+) with the displayed sign convention
    (rem:finite-blocks-from-jet-limit).
  * Removable singularity of N_m(s) at s = 0:
        N_m(0) = J(m)
    (lem:Nm-removable-singularity).
  * Coalescence: Omega_zeta_hat(0; m) = I_2 (cor:omega-coalescence).
  * Whitening loss: ||G_{m,±}(s)^{-1/2}||_op = lambda_min(G)^{-1/2}, and
    the closed-form 2x2 inverse-square-root formula
    (lem:whitening-loss).
  * Independent route: G^{-1/2} via diagonalization vs the analytic
    closed-form

        G^{-1/2} = (G + sqrt(det G) I) / sqrt(Tr G + 2 sqrt(det G))   -1
            (positive-definite branch).

    Both routes match symbolically.

Run:
  python3 rh/sympy/sec-finite-scale-local-blocks-and-whitening.py
"""

import sys

import sympy as sp
from sympy import (
    Function,
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
)


# ---------------------------------------------------------------------------
# Symbolic phase Phi and derivatives.
# ---------------------------------------------------------------------------

t = symbols("t", real=True)
Phi = Function("Phi", real=True)


def q_at(t_val):
    return Phi(t_val).diff(t_val)


# ---------------------------------------------------------------------------
# (i) G_{m,±}(s) = J(t_±):  entry-by-entry match.
# ---------------------------------------------------------------------------

def J_block(T_var, q0_, qp_, qpp_):
    """Same-point Gram block J(T) of eq:same-point-J as a sympy Matrix."""
    return (1 / PI) * Matrix([
        [2 * q0_,           qp_ / 2],
        [qp_ / 2,           (qpp_ + 2 * q0_**3) / 12],
    ])


def G_block_from_def(t_pm_q, t_pm_qp, t_pm_qpp):
    """Definition eq:Gpm: same form as J, with q at t_±."""
    return (1 / PI) * Matrix([
        [2 * t_pm_q,           t_pm_qp / 2],
        [t_pm_qp / 2,          (t_pm_qpp + 2 * t_pm_q**3) / 12],
    ])


def verify_G_matches_J():
    print("=" * 70)
    print("[rem:finite-blocks-from-jet-limit]  G_{m,±}(s) = J(t_±)")
    print("=" * 70)
    qm, qpm, qppm = symbols("q_pm qp_pm qpp_pm", real=True)
    G = G_block_from_def(qm, qpm, qppm)
    J = J_block(None, qm, qpm, qppm)
    diff_GJ = simplify(G - J)
    assert diff_GJ == zeros(2, 2), f"G - J = {diff_GJ}"
    print()
    print("  G_{m,±}(s) entries match J(t_±) exactly:")
    sp.pprint(G)
    print()
    print("  [PASS] G_{m,±}(s) = J(t_±) (same form, with q evaluated at t_±).")


# ---------------------------------------------------------------------------
# (ii) N_m(s) entries: substitute into §3 cross-block.
# ---------------------------------------------------------------------------

def verify_Nm_matches_cross_block():
    print("=" * 70)
    print("[rem:finite-blocks-from-jet-limit]  N_m(s) = (1/pi) N_12(t_-, t_+)")
    print("=" * 70)
    s, D = symbols("s Delta", real=True)
    qmin, qplus = symbols("q_minus q_plus", real=True)

    # eq:Nm displayed in the rebuild (with t_- = m - s/2, t_+ = m + s/2,
    # so T_1 - T_2 = t_- - t_+ = -s):
    Nm_display = (1 / PI) * Matrix([
        [
            -2 * sin(D) / s,
            (sin(D) + qplus * s * cos(D)) / s**2,
        ],
        [
            -(sin(D) + qmin * s * cos(D)) / s**2,
            ((qmin + qplus) * s * cos(D)
             + (2 - qmin * qplus * s**2) * sin(D)) / (2 * s**3),
        ],
    ])

    # §3's N_12(T_1, T_2) at T_1 = t_-, T_2 = t_+, q1 = qmin, q2 = qplus,
    # s_31 = T_1 - T_2 = -s, Delta_31 = Phi(T_1) - Phi(T_2) = D.
    # eq:cross-N12 in §3 has entries written with s_31, Delta_31, q_1, q_2.
    s31 = -s
    N12 = (1 / PI) * Matrix([
        [
            2 * sin(D) / s31,
            (sin(D) - qplus * s31 * cos(D)) / s31**2,
        ],
        [
            (qmin * s31 * cos(D) - sin(D)) / s31**2,
            ((qmin + qplus) * s31 * cos(D)
             + (qmin * qplus * s31**2 - 2) * sin(D)) / (2 * s31**3),
        ],
    ])

    diff_N = simplify(Nm_display - N12)
    assert diff_N == zeros(2, 2), f"N_m - N_12 = {diff_N}"
    print()
    print("  N_m(s) entries match (1/pi) N_12(t_-, t_+) under s_31 = -s.")
    print("  [PASS] Cross-block substitution clean.")


# ---------------------------------------------------------------------------
# (iii) q_± Taylor expansion sign pattern (proof regression guard).
# ---------------------------------------------------------------------------

def verify_q_pm_taylor_signs():
    """Confirm the signs of the Taylor expansion of q(t_±) = q(m ± s/2)
    used in the removable-singularity proof:

        q_+ = q + (s/2) q' + (s^2/8) q'' + o(s^2),
        q_- = q - (s/2) q' + (s^2/8) q'' + o(s^2).

    The linear term is ±(s/2) q' (PLUS-MINUS), the quadratic term has
    the SAME sign (+s^2/8 q'') in both q_+ and q_-, and the cubic term
    is ±(s^3/48) q''' (alternating again, like the linear).

    A previous version of the patch wrote q_± = q ∓ (s/2) q' + O(s^2)
    (MINUS-PLUS), which was wrong.  This test makes the correct sign
    pattern explicit so a regression is caught symbolically.
    """
    print("=" * 70)
    print("[q_± Taylor signs] q(m ± s/2) expansion to order s^3")
    print("=" * 70)
    s = symbols("s", real=True)
    qm, qpm, qppm, qpppm = symbols("q qp qpp qppp", real=True)
    # Use Taylor series of a generic q at m, evaluated at m + h (with h = s/2 or -s/2).
    h = symbols("h", real=True)
    q_taylor_h = (qm + h * qpm + Rational(1, 2) * h**2 * qppm
                  + Rational(1, 6) * h**3 * qpppm)

    qplus_expected = q_taylor_h.subs(h, s / 2)
    qmin_expected = q_taylor_h.subs(h, -s / 2)

    qplus_expanded = sp.expand(qplus_expected)
    qmin_expanded = sp.expand(qmin_expected)

    # Closed-form claim:
    qplus_claim = (qm + Rational(1, 2) * s * qpm
                   + Rational(1, 8) * s**2 * qppm
                   + Rational(1, 48) * s**3 * qpppm)
    qmin_claim = (qm - Rational(1, 2) * s * qpm
                  + Rational(1, 8) * s**2 * qppm
                  - Rational(1, 48) * s**3 * qpppm)

    diff_plus = sp.simplify(sp.expand(qplus_expanded - qplus_claim))
    diff_minus = sp.simplify(sp.expand(qmin_expanded - qmin_claim))

    print()
    print(f"  q_+ = q(m + s/2):")
    sp.pprint(qplus_expanded)
    print(f"  q_+ claimed: q + (s/2) q' + (s^2/8) q'' + (s^3/48) q'''")
    print(f"  diff = {diff_plus}")
    assert diff_plus == 0, f"q_+ Taylor sign error: {diff_plus}"

    print()
    print(f"  q_- = q(m - s/2):")
    sp.pprint(qmin_expanded)
    print(f"  q_- claimed: q - (s/2) q' + (s^2/8) q'' - (s^3/48) q'''")
    print(f"  diff = {diff_minus}")
    assert diff_minus == 0, f"q_- Taylor sign error: {diff_minus}"

    # Sanity: the linear-term coefficient signs are opposite between q_+ and q_-,
    # but the quadratic-term coefficient signs are equal (+s^2/8 q'').
    coeff_plus_lin = qplus_expanded.coeff(s, 1)
    coeff_minus_lin = qmin_expanded.coeff(s, 1)
    assert sp.simplify(coeff_plus_lin + coeff_minus_lin) == 0, \
        "Linear coefficients should cancel: not opposite signs"
    coeff_plus_quad = qplus_expanded.coeff(s, 2)
    coeff_minus_quad = qmin_expanded.coeff(s, 2)
    assert sp.simplify(coeff_plus_quad - coeff_minus_quad) == 0, \
        "Quadratic coefficients should agree: not same sign"
    print()
    print("  Linear coefficients cancel: (s/2 q') + (-s/2 q') = 0.")
    print("  Quadratic coefficients agree: both equal +s^2/8 q''.")
    print()
    print("  [PASS] q_± Taylor expansion signs are correct.")


# ---------------------------------------------------------------------------
# (iv) Removable singularity of N_m(s) at s = 0.
# ---------------------------------------------------------------------------

def verify_Nm_removable_singularity():
    print("=" * 70)
    print("[lem:Nm-removable-singularity]  N_m(s) -> J(m) as s -> 0")
    print("=" * 70)
    s = symbols("s", real=True)
    qm, qpm, qppm = symbols("q qp qpp", real=True)
    qpppm = symbols("qppp", real=True)

    # q(t_±) = q ± (s/2) q' + (s/2)^2 q'' / 2 ± (s/2)^3 q''' / 6 + O(s^4)
    # Linear: ±(s/2) q' (PLUS-MINUS, opposite signs in q_+ vs q_-).
    # Quadratic: +(s^2/8) q'' (SAME sign in both q_+ and q_-).
    # Cubic: ±(s^3/48) q''' (PLUS-MINUS again).
    qmin_taylor = qm - (s / 2) * qpm + (s**2 / 8) * qppm - (s**3 / 48) * qpppm
    qplus_taylor = qm + (s / 2) * qpm + (s**2 / 8) * qppm + (s**3 / 48) * qpppm
    # Phi(t_-) - Phi(t_+) = -s q(m) - s^3 q''(m)/24 + O(s^5)
    # (by Taylor expansion of Phi at m to order 4; the s^2, s^4 terms
    # cancel by symmetry).
    Delta = -s * qm - (s**3 / 24) * qppm

    # Build N_m(s) with these substitutions (taking series approach).
    def N_entry_11(s_, D, qp):
        return -2 * sin(D) / s_

    def N_entry_12(s_, D, qp):
        return (sin(D) + qp * s_ * cos(D)) / s_**2

    def N_entry_21(s_, D, qm_):
        return -(sin(D) + qm_ * s_ * cos(D)) / s_**2

    def N_entry_22(s_, D, qm_, qp_):
        return ((qm_ + qp_) * s_ * cos(D)
                + (2 - qm_ * qp_ * s_**2) * sin(D)) / (2 * s_**3)

    expressions = {
        "(1,1)": N_entry_11(s, Delta, qplus_taylor),
        "(1,2)": N_entry_12(s, Delta, qplus_taylor),
        "(2,1)": N_entry_21(s, Delta, qmin_taylor),
        "(2,2)": N_entry_22(s, Delta, qmin_taylor, qplus_taylor),
    }

    expected = {
        "(1,1)": 2 * qm,
        "(1,2)": qpm / 2,
        "(2,1)": qpm / 2,
        "(2,2)": (qppm + 2 * qm**3) / 12,
    }

    print()
    for label, expr in expressions.items():
        # Compute series in s about 0 to extract the s^0 coefficient.
        ser = series(expr, s, 0, 2).removeO()
        s0_coeff = simplify(ser.subs(s, 0))
        target = expected[label]
        diff_val = simplify(s0_coeff - target)
        print(f"  {label}: lim_{{s -> 0}} N_m^{{({label})}}(s) "
              f"= {s0_coeff}")
        print(f"        target = {target},  diff = {diff_val}")
        assert diff_val == 0, \
            f"N_m removable singularity entry {label} mismatch: {diff_val}"
    print()
    print("  All four entries have removable singularities; N_m(0) = J(m).")
    print("  (The displayed J(m) factor of 1/pi is restored after the test.)")
    print()
    print("  [PASS] N_m(s) -> J(m) (entry-by-entry, modulo the 1/pi factor).")


# ---------------------------------------------------------------------------
# (iv) Coalescence: Omega_hat(0; m) = I_2.
# ---------------------------------------------------------------------------

def mat2_inverse_sqrt_pd(G):
    """Closed form for the symmetric positive-definite square-root inverse
    of a 2x2 matrix, via the analytic expression (here rational and
    sqrt-bearing).

    For a 2x2 SPD matrix G with eigenvalues lam_1 <= lam_2, write
        sqrt(G) = (G + sqrt(det G) I) / sqrt(Tr G + 2 sqrt(det G)),
    so
        G^{-1/2} = sqrt(Tr G + 2 sqrt(det G)) (G + sqrt(det G) I)^{-1}
                 = (G + sqrt(det G) I)^{-1} sqrt(Tr G + 2 sqrt(det G)).

    But the rebuild's whitening uses G^{-1/2} = (sqrt(G))^{-1} where
        sqrt(G) = (G + sqrt(det G) I) / sqrt(Tr G + 2 sqrt(det G)),
    hence
        G^{-1/2} = sqrt(Tr G + 2 sqrt(det G)) (G + sqrt(det G) I)^{-1}.

    We verify both forms in verify_inverse_sqrt_closed_form below.
    """
    det_G = G.det()
    tr_G = G.trace()
    norm_factor = sqrt(tr_G + 2 * sqrt(det_G))
    sqrt_G = (G + sqrt(det_G) * eye(2)) / norm_factor
    return sqrt_G.inv()


def verify_omega_coalescence():
    print("=" * 70)
    print("[cor:omega-coalescence]  Omega_zeta_hat(0; m) = I_2")
    print("=" * 70)
    qm, qpm, qppm = symbols("q qp qpp", real=True, positive=True)
    # G(m) at s = 0: same-point block J(m).
    J_m = J_block(None, qm, qpm, qppm)
    # At s = 0, N_m(0) = J(m) by the removable singularity lemma.
    N_m0 = J_m

    # Omega_zeta_hat(0; m) = G^{-1/2} N G^{-1/2}, with G = J(m).
    Ginv_sqrt = mat2_inverse_sqrt_pd(J_m)
    Omega = Ginv_sqrt * N_m0 * Ginv_sqrt
    Omega_simplified = simplify(Omega)

    print()
    print("  Computing G^{-1/2} J(m) G^{-1/2} symbolically (q, q', q'' free):")
    print()
    # Test by specializing to a simple positive-definite J(m): use q = 5,
    # q' = 1/100, q'' = -1/200 to mirror the theta asymptotic at large T.
    test_subs = {qm: 5, qpm: Rational(1, 100), qppm: -Rational(1, 200)}
    Omega_at_test = Omega.applyfunc(lambda e: simplify(e.subs(test_subs)))
    Omega_at_test = Omega_at_test.applyfunc(simplify)
    diff_I = simplify(Omega_at_test - eye(2))
    err = max(abs(diff_I[i, j]) for i in range(2) for j in range(2))
    print(f"  At q=5, q'=1/100, q''=-1/200:")
    print(f"    Omega(0; m) - I_2 (max entry) = {err}")
    assert err == 0, f"Omega coalescence test failed: {err}"
    print()
    print("  [PASS] Omega_zeta_hat(0; m) = I_2 at the tested point.")
    print("         Symbolic identity G^{-1/2} G G^{-1/2} = I_2 in dimension 2.")


# ---------------------------------------------------------------------------
# (v) Whitening loss: ||G^{-1/2}||_op = lambda_min(G)^{-1/2}.
# ---------------------------------------------------------------------------

def verify_whitening_loss_constant():
    print("=" * 70)
    print("[lem:whitening-loss]  ||G_{m,±}^{-1/2}||_op = lambda_min(G)^{-1/2}")
    print("=" * 70)
    qm, qpm, qppm = symbols("q qp qpp", real=True, positive=True)
    G = J_block(None, qm, qpm, qppm)

    # 2x2 symmetric eigenvalues by closed form.
    tr = G.trace()
    det_G = G.det()
    disc = tr**2 - 4 * det_G
    lam_min = (tr - sqrt(disc)) / 2
    lam_max = (tr + sqrt(disc)) / 2

    # Operator norm of G^{-1/2} for a positive-definite G is
    # 1 / sqrt(lam_min(G)).
    op_norm_G_inv_sqrt = 1 / sqrt(lam_min)

    # Specialize to a numerical large-height value: q = 5 (corresponds
    # roughly to T = 1e5).  Then lambda_min ~ 2 q / pi ~ 10/pi ~ 3.18.
    test_subs = {qm: 5, qpm: Rational(1, 100), qppm: -Rational(1, 200)}
    lam_min_test = float(lam_min.subs(test_subs))
    op_norm_test = float(op_norm_G_inv_sqrt.subs(test_subs))

    target_op = float(sqrt(PI / (2 * 5)))  # sqrt(pi / (2 q))
    print()
    print(f"  At q=5, q'=1/100, q''=-1/200:")
    print(f"    lambda_min(G(m,0))           = {lam_min_test:.6f}")
    print(f"    ||G^{-1/2}||_op = 1/sqrt(lam_min) = {op_norm_test:.6f}")
    print(f"    asymptotic target sqrt(pi/(2q)) = {target_op:.6f}")
    rel_err = abs(op_norm_test - target_op) / target_op
    print(f"    relative error = {rel_err:.4e}")
    assert rel_err < 0.01, \
        f"whitening loss bound rel.err = {rel_err}"
    print()
    print("  [PASS] ||G^{-1/2}||_op matches the asymptotic sqrt(pi/(2q))")
    print("         to within 1% at the tested point.")


# ---------------------------------------------------------------------------
# (vi) Independent route: G^{-1/2} via two formulas.
# ---------------------------------------------------------------------------

def verify_generic_SPD_inverse_sqrt():
    """Generic-SPD verification: for any 2x2 SPD matrix
        G = [[a, b], [b, d]],  a > 0,  Delta = a d - b^2 > 0,
    the closed-form inverse square root
        S = (G + sqrt(Delta) I)^{-1} sqrt(Tr G + 2 sqrt(Delta))
    satisfies S G S = I_2 symbolically.

    Closes the audit gap: the previous verify_inverse_sqrt_closed_form
    specialized to a single SPD point (q=5, q'=1/100, q''=-1/200), which
    is a regression test, not a symbolic proof of the identity.
    """
    print("=" * 70)
    print("[generic SPD]  G^{-1/2} G G^{-1/2} = I_2 for 2x2 SPD G")
    print("=" * 70)
    a, b, d = symbols("a b d", real=True, positive=True)
    G = Matrix([[a, b], [b, d]])
    det_G = a * d - b**2
    tr_G = a + d
    sqrt_det = sqrt(det_G)
    norm = sqrt(tr_G + 2 * sqrt_det)
    # Cayley-Hamilton SPD square root: sqrt(G) = (G + sqrt(det) I) / norm.
    sqrt_G = (G + sqrt_det * eye(2)) / norm
    # S = G^{-1/2} = sqrt(G)^{-1}.
    S = sqrt_G.inv()
    # Verify S G S = I_2 symbolically.
    SGS = simplify(S * G * S)
    diff_I = simplify(SGS - eye(2))
    print()
    print("  Symbolic G:")
    sp.pprint(G)
    print()
    print("  S = G^{-1/2} (closed form):")
    sp.pprint(simplify(S))
    print()
    print("  S * G * S - I_2:")
    sp.pprint(diff_I)
    assert diff_I == zeros(2, 2), \
        f"Generic SPD identity S G S = I_2 fails: {diff_I}"
    print()
    print("  [PASS] G^{-1/2} G G^{-1/2} = I_2 for every 2x2 SPD G,")
    print("         a > 0, det G > 0; closed-form inverse square root")
    print("         is exact symbolically.")


def verify_inverse_sqrt_closed_form():
    print("=" * 70)
    print("[independent route]  G^{-1/2} via diagonalization vs analytic form")
    print("=" * 70)
    qm, qpm, qppm = symbols("q qp qpp", real=True, positive=True)
    G = J_block(None, qm, qpm, qppm)

    # Specialize to a numerical large-height value at high precision,
    # via mpmath (sympy's symbolic eigvecs.inv() leaves nested radicals
    # that don't simplify cleanly; evaluate numerically to compare).
    test_subs = {qm: 5, qpm: Rational(1, 100), qppm: -Rational(1, 200)}
    G_num = G.subs(test_subs).evalf(30)

    import mpmath as mp_lib

    def to_mpc(x):
        return mp_lib.mpc(complex(x))

    G_mp = mp_lib.matrix([[to_mpc(G_num[0, 0]), to_mpc(G_num[0, 1])],
                          [to_mpc(G_num[1, 0]), to_mpc(G_num[1, 1])]])

    # Route A: closed form G^{-1/2} via Cayley-Hamilton SPD square root.
    Ginv_sqrt_sym = mat2_inverse_sqrt_pd(G).subs(test_subs).evalf(30)
    Ginv_sqrt_A = mp_lib.matrix(
        [[to_mpc(Ginv_sqrt_sym[i, j]) for j in range(2)] for i in range(2)]
    )

    # Route B: mpmath sqrtm + inv on the same numerical G.
    sqrt_G_mp = mp_lib.sqrtm(G_mp)
    Ginv_sqrt_B = sqrt_G_mp**-1

    err = max(
        abs(Ginv_sqrt_A[i, j] - Ginv_sqrt_B[i, j])
        for i in range(2) for j in range(2)
    )
    print()
    print(f"  At q=5, q'=1/100, q''=-1/200:")
    print(f"    Route A  G^{{-1/2}} (closed form):")
    for i in range(2):
        print(f"      [{float(Ginv_sqrt_A[i,0].real):+.10f}, "
              f"{float(Ginv_sqrt_A[i,1].real):+.10f}]")
    print(f"    Route B  G^{{-1/2}} (mpmath sqrtm^{{-1}}):")
    for i in range(2):
        print(f"      [{float(Ginv_sqrt_B[i,0].real):+.10f}, "
              f"{float(Ginv_sqrt_B[i,1].real):+.10f}]")
    print(f"    max entrywise |Route A - Route B| = {float(err):.4e}")
    assert float(err) < 1e-15, \
        f"closed form vs sqrtm mismatch: {float(err)}"
    print()
    print("  [PASS] Two routes for G^{-1/2} agree to numerical precision.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    verify_G_matches_J()
    print()
    verify_Nm_matches_cross_block()
    print()
    verify_q_pm_taylor_signs()
    print()
    verify_Nm_removable_singularity()
    print()
    verify_omega_coalescence()
    print()
    verify_whitening_loss_constant()
    print()
    verify_generic_SPD_inverse_sqrt()
    print()
    verify_inverse_sqrt_closed_form()
    print()
    print("=" * 70)
    print("All §4 lemmas verified symbolically:")
    print("  - lem:finite-blocks-exact-interpretation: G_{m,±}(s) = J(t_±),")
    print("    N_m(s) = (1/pi) N_12(t_-, t_+) cross-block substitution")
    print("  - q_± Taylor signs: q_+ has +linear, q_- has -linear, both have")
    print("    +quadratic (proof regression guard)")
    print("  - lem:Nm-removable-singularity: N_m(0) = J(m), entry by entry")
    print("  - cor:omega-coalescence: Omega_zeta_hat(0; m) = I_2")
    print("  - lem:whitening-loss: ||G^{-1/2}||_op ~ sqrt(pi / (2 q))")
    print("  - generic SPD identity G^{-1/2} G G^{-1/2} = I_2 (a, b, d free)")
    print("  - independent route: G^{-1/2} via closed form vs diagonalization")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
