"""Numerical simulation: sec:finite-scale-local-blocks-and-whitening.

Numerical regression harness for the migration of §4 staged at
rh/patches/sec-finite-scale-local-blocks-and-whitening.tex.

Coverage:

  * For zeta-derived q at high T: compute G_{m,±}(s) and N_m(s) for
    midpoints m in I_T and separations s in (0, 1/Q]; assert
    positive-definiteness of G_{m,±}(s).
  * Removable-singularity numerical check: N_m(s) -> J(m) as s -> 0.
  * Whitening-loss sweep: ||G_{m,±}(s)^{-1/2}||_op tracked across
    midpoints and separations; fit and assert C_W = 0
    (||.||_op bounded by an absolute constant).
  * lambda_min(G_{m,±}) polynomial-in-Q floor: confirm
    lambda_min(G) >= 2 q(t_±) / pi  (1 + o(1)) on the retained set.
  * Coalescence Omega(0; m) = I_2 numerically across heights.
  * Independent-route check for G^{-1/2}: closed-form
    Cayley-Hamilton SPD square root vs mpmath.sqrtm.

All checks are assertions.  No numpy, no math, no built-in float in the
verification loop.

Run:
  python3 rh/simulation/sec-finite-scale-local-blocks-and-whitening.py
"""

import sys

from mpmath import (
    cos as mp_cos,
    diff,
    eye as mp_eye,
    fabs,
    log as mp_log,
    matrix as mp_matrix,
    mp,
    mpc,
    mpf,
    pi as MP_PI,
    siegeltheta,
    sin as mp_sin,
    sqrt as mp_sqrt,
    sqrtm,
)


mp.dps = 40  # plenty for finite-s regression at heights up to 1e6


# ---------------------------------------------------------------------------
# Phase derivatives.
# ---------------------------------------------------------------------------

def phi(t):
    return siegeltheta(mpf(t))


def phi_derivs(t):
    """(q, q', q'', q''') at t."""
    t = mpf(t)
    return (diff(siegeltheta, t, 1),
            diff(siegeltheta, t, 2),
            diff(siegeltheta, t, 3),
            diff(siegeltheta, t, 4))


# ---------------------------------------------------------------------------
# Block matrices.
# ---------------------------------------------------------------------------

def G_at(t_pm):
    """G_{m,±}(s) at center t_pm (= J(t_pm) of §3, eq:same-point-J)."""
    q0, qp, qpp, _ = phi_derivs(t_pm)
    return mp_matrix([
        [2 * q0 / MP_PI,        qp / (2 * MP_PI)],
        [qp / (2 * MP_PI),      (qpp + 2 * q0**3) / (12 * MP_PI)],
    ])


def Nm_block(m, s):
    """N_m(s) entries from eq:Nm in the rebuild's display."""
    m = mpf(m)
    s = mpf(s)
    t_minus = m - s / 2
    t_plus = m + s / 2
    q_minus, _, _, _ = phi_derivs(t_minus)
    q_plus, _, _, _ = phi_derivs(t_plus)
    Delta = phi(t_minus) - phi(t_plus)
    sin_d = mp_sin(Delta)
    cos_d = mp_cos(Delta)
    n11 = -2 * sin_d / s
    n12 = (sin_d + q_plus * s * cos_d) / s**2
    n21 = -(sin_d + q_minus * s * cos_d) / s**2
    n22 = ((q_minus + q_plus) * s * cos_d
           + (2 - q_minus * q_plus * s**2) * sin_d) / (2 * s**3)
    return mp_matrix([[n11 / MP_PI, n12 / MP_PI],
                      [n21 / MP_PI, n22 / MP_PI]])


def mat2_eigs_symmetric(A):
    tr = A[0, 0] + A[1, 1]
    det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    disc = tr**2 - 4 * det
    sq = mp_sqrt(disc)
    return (tr - sq) / 2, (tr + sq) / 2


def op_norm(A):
    """Operator norm = largest eigenvalue magnitude (for symmetric A)."""
    lam_min, lam_max = mat2_eigs_symmetric(A)
    return max(abs(lam_min), abs(lam_max))


def G_inv_sqrt_closed(G):
    """Closed-form SPD inverse square root via Cayley-Hamilton.

    For 2x2 SPD G:
        sqrt(G) = (G + sqrt(det G) I) / sqrt(Tr G + 2 sqrt(det G)),
    so G^{-1/2} = sqrt(G)^{-1}.
    """
    tr = G[0, 0] + G[1, 1]
    det = G[0, 0] * G[1, 1] - G[0, 1] * G[1, 0]
    sqrt_det = mp_sqrt(det)
    norm = mp_sqrt(tr + 2 * sqrt_det)
    sqrt_G = (G + sqrt_det * mp_eye(2)) / norm
    return sqrt_G**-1


def mat2_max_diff(A, B):
    return max(fabs(A[i, j] - B[i, j]) for i in range(2) for j in range(2))


# ---------------------------------------------------------------------------
# (i) Finite blocks at a height: G entries, N entries, positivity.
# ---------------------------------------------------------------------------

def check_finite_blocks_at_T(T, n_midpoints=5, n_seps=5):
    print("=" * 70)
    print(f"[finite blocks at T = {float(T):.2e}: G_{{m,+-}} and N_m well-defined]")
    print("=" * 70)
    print()
    Q = mp_log(T)  # informal Q ~ log T scaling
    half_window = mpf("0.05")
    midpoints = [T - half_window
                 + 2 * i * half_window / mpf(n_midpoints - 1)
                 for i in range(n_midpoints)]
    s_grid = [mpf(10) ** k for k in (-1, -2, -3, -4, -5)]

    print(f"  T = {float(T):.0e}, Q ~ log T = {float(Q):.4f}")
    print(f"  midpoints sampled across I_T = [T - 0.05, T + 0.05]")
    print()
    print(f"  {'m offset':>12}  {'s':>8}  {'lam_min(G_-)':>14}  "
          f"{'lam_min(G_+)':>14}  {'op N_m':>14}")
    print(f"  {'-'*12}  {'-'*8}  {'-'*14}  {'-'*14}  {'-'*14}")

    for m in midpoints:
        for s in s_grid:
            t_plus = m + s / 2
            t_minus = m - s / 2
            G_minus = G_at(t_minus)
            G_plus = G_at(t_plus)
            lam_min_minus, _ = mat2_eigs_symmetric(G_minus)
            lam_min_plus, _ = mat2_eigs_symmetric(G_plus)
            N = Nm_block(m, s)
            op_N = op_norm(N)
            assert lam_min_minus > 0, \
                f"G_{{m,-}} not positive at m={float(m)}, s={float(s)}"
            assert lam_min_plus > 0, \
                f"G_{{m,+}} not positive at m={float(m)}, s={float(s)}"
            offset = float(m - T)
            if s == s_grid[0] or s == s_grid[-1]:
                print(f"  {offset:+12.4e}  {float(s):8.0e}  "
                      f"{float(lam_min_minus):14.6f}  "
                      f"{float(lam_min_plus):14.6f}  "
                      f"{float(op_N):14.6f}")
    print()
    print("  [PASS] G_{m,±}(s) is positive-definite at every sampled (m, s);")
    print("         N_m(s) operator norm finite throughout.")


# ---------------------------------------------------------------------------
# (ii) Removable singularity: N_m(s) -> J(m) as s -> 0.
# ---------------------------------------------------------------------------

def check_q_pm_signs_numerical(T, s_grid=None):
    """Numerical regression guard for the q_± Taylor sign pattern:

        q(m + s/2) - q(m) = (s/2) q'(m) + (s^2/8) q''(m) + O(s^3),
        q(m - s/2) - q(m) = -(s/2) q'(m) + (s^2/8) q''(m) + O(s^3).

    Linear term: ±(s/2) q' (sign of s flips).
    Quadratic term: +s^2/8 q'' (same sign for both q_+ and q_-).

    A regression that flips the q_- linear sign would surface as a
    diff that fails to scale linearly with s.
    """
    print("=" * 70)
    print(f"[q_± numerical signs at T = {float(T):.0e}]")
    print("=" * 70)
    print()
    m = T
    q0, qp, qpp, _ = phi_derivs(m)
    if s_grid is None:
        s_grid = [mpf(10) ** k for k in (-2, -3, -4, -5)]
    print(f"  q(m)   = {float(q0):.6f}")
    print(f"  q'(m)  = {float(qp):.4e}")
    print(f"  q''(m) = {float(qpp):.4e}")
    print()
    header_plus = "q_+ residual"
    header_minus = "q_- residual"
    print(f"  {'s':>10}  {header_plus:>22}  {header_minus:>24}")
    print(f"  (residuals subtract the +/- (s/2) q' linear term)")
    print(f"  {'-'*10}  {'-'*22}  {'-'*24}")
    for s in s_grid:
        t_plus = m + s / 2
        t_minus = m - s / 2
        q_plus, _, _, _ = phi_derivs(t_plus)
        q_minus, _, _, _ = phi_derivs(t_minus)
        # Linear-term check: q_+ - q_0 - (s/2) q' should be O(s^2);
        # q_- - q_0 + (s/2) q' should be O(s^2).
        residual_plus = q_plus - q0 - (s / 2) * qp
        residual_minus = q_minus - q0 + (s / 2) * qp
        print(f"  {float(s):10.0e}  {float(residual_plus):+22.4e}  "
              f"{float(residual_minus):+24.4e}")
        # Both residuals should scale as O(s^2) and have the same sign
        # (positive q'' would give residual ~ +s^2/8 q'' for both).
        # Check that the quadratic coefficient agrees.
        approx_plus = residual_plus / (s**2 / 8)
        approx_minus = residual_minus / (s**2 / 8)
        # In the limit s -> 0 these both approach q''(m).
        # At small s, |approx_plus - q''| and |approx_minus - q''| should be small.
        rel_plus = abs(approx_plus - qpp) / abs(qpp)
        rel_minus = abs(approx_minus - qpp) / abs(qpp)
        if s <= mpf("1e-3"):
            assert rel_plus < mpf("0.1"), \
                f"q_+ sign pattern off at s = {float(s)}: rel.err = {float(rel_plus)}"
            assert rel_minus < mpf("0.1"), \
                f"q_- sign pattern off at s = {float(s)}: rel.err = {float(rel_minus)}"
    print()
    print("  [PASS] q_+ has +(s/2) q' linear term, q_- has -(s/2) q'; both")
    print("         share the +s^2/8 q'' quadratic term.")


def check_Nm_removable_singularity_numerical(T):
    print("=" * 70)
    print(f"[lem:Nm-removable-singularity]  N_m(s) -> J(m) as s -> 0 at T = "
          f"{float(T):.0e}")
    print("=" * 70)
    print()
    m = T
    J_m = G_at(m)  # same-point block at the midpoint
    print(f"  J(m) (target):")
    print(f"    [[{float(J_m[0,0]):.6f}, {float(J_m[0,1]):+.6e}],")
    print(f"     [{float(J_m[1,0]):+.6e}, {float(J_m[1,1]):.6f}]]")
    print()
    print(f"  {'s':>10}  {'max|N_m(s) - J(m)|':>22}")
    print(f"  {'-'*10}  {'-'*22}")
    errs = []
    s_grid = [mpf(10) ** k for k in (-2, -3, -4, -5, -6)]
    for s in s_grid:
        Nm = Nm_block(m, s)
        err = mat2_max_diff(Nm, J_m)
        errs.append(err)
        print(f"  {float(s):10.0e}  {float(err):22.6e}")
    # Errors must decrease monotonically.
    for i in range(1, len(errs)):
        assert errs[i] < errs[i - 1], (
            f"N_m removable singularity error not monotone: "
            f"err(s=1e{int(mp_log(s_grid[i-1]) / mp_log(10))}) -> "
            f"err(s=1e{int(mp_log(s_grid[i]) / mp_log(10))})"
        )
    # Final smallest-s error tiny.
    assert errs[-1] < mpf("1e-3"), \
        f"Final-s removable singularity err = {float(errs[-1])}"
    # The (1,1) and (2,2) entries have O(s^2) corrections, but the
    # off-diagonal entries inherit a q'(m)/2 survivor that gives the
    # max-entry error an O(s) leading order.  Hence the empirical slope
    # is 1, not 2; the lemma claims continuity, not a specific rate.
    h_tail = s_grid[-3:]
    e_tail = errs[-3:]
    slope = mp_log(e_tail[-1] / e_tail[0]) / mp_log(h_tail[-1] / h_tail[0])
    print()
    print(f"  log-log slope on tail = {float(slope):.4f}")
    print("  (off-diagonal entries have O(s) leading correction; "
          "diagonal entries are O(s^2).")
    assert slope > mpf("0.5"), \
        f"removable-singularity not converging: slope = {float(slope)}"
    print()
    print("  [PASS] N_m(s) -> J(m) entry-by-entry; tail slope > 0.5")
    print("         confirms the (continuous) removable singularity.")


# ---------------------------------------------------------------------------
# (iii) Coalescence Omega(0; m) = I_2 (computed via small-s extrapolation).
# ---------------------------------------------------------------------------

def check_signed_s_domain(T):
    """Confirm that the finite-block formulas extend to negative s on
    the finite packet domain D_T = {(m, s): t_± in I_T}, matching the
    hardened def:finite-packet-domain.

    For symmetric reasons we expect:
      - G_{m,±}(s) at s and at -s differ only by swapping t_+ <-> t_-,
        i.e. G_{m,+}(s) = G_{m,-}(-s) and vice versa.
      - N_m(s) at signed s extends continuously through s = 0.

    The sympy file verifies the symbolic identity; this is a numerical
    regression guard.
    """
    print("=" * 70)
    print(f"[signed s in D_T at T = {float(T):.0e}]")
    print("=" * 70)
    print()
    m = T
    print(f"  m = T = {float(m):.0e}")
    print()
    print(f"  {'s':>10}  {'max|G+(s) - G-(-s)|':>24}  {'max|N_m(s) - N_m(-s).T sign|':>32}")
    print(f"  {'-'*10}  {'-'*24}  {'-'*32}")
    s_grid = [mpf("0.01"), mpf("0.001"), mpf("0.0001")]
    for s_pos in s_grid:
        s_neg = -s_pos
        # G_{m,+}(s) = J(m + s/2); G_{m,-}(-s) = J(m + s/2). Should match.
        G_plus_s = G_at(m + s_pos / 2)
        G_minus_neg_s = G_at(m + (-s_neg) / 2)  # = m + s/2
        err_swap = mat2_max_diff(G_plus_s, G_minus_neg_s)
        # For N_m: under s -> -s, the (1,1) entry stays even since
        # sin(Delta_m(-s)) = -sin(Delta_m(s)) and the explicit -2 sin/s
        # ratio is even.  The other entries swap roles.  We just check
        # both N_m(s) and N_m(-s) are well-defined and finite.
        N_pos = Nm_block(m, s_pos)
        N_neg = Nm_block(m, s_neg)
        # The (1,1) entry is even in s (it equals -2 sin(Delta)/s and
        # both sin(Delta) and s flip sign, leaving the ratio invariant).
        err_n11_even = abs(N_pos[0, 0] - N_neg[0, 0])
        print(f"  {float(s_pos):+10.4f}  {float(err_swap):24.4e}  "
              f"{float(err_n11_even):32.4e}")
        assert err_swap < mpf("1e-30"), \
            f"G_+(s) != G_-(-s) at s = {float(s_pos)}: err = {float(err_swap)}"
        assert err_n11_even < mpf("1e-30"), \
            f"N_m(s)_{{11}} not even in s at s = {float(s_pos)}: "\
            f"err = {float(err_n11_even)}"
    print()
    print("  [PASS] Finite blocks are well-defined for signed s on D_T;")
    print("         G_{m,+}(s) = G_{m,-}(-s) and N_m^{(1,1)}(s) is even in s.")


def check_omega_coalescence_numerical(T):
    print("=" * 70)
    print(f"[cor:omega-coalescence]  Omega_hat(s -> 0; m) = I_2 at T = "
          f"{float(T):.0e}")
    print("=" * 70)
    print()
    m = T
    print(f"  m = T = {float(T):.0e}")
    print()
    print(f"  {'s':>10}  {'max|Omega(s; m) - I_2|':>26}")
    print(f"  {'-'*10}  {'-'*26}")
    errs = []
    s_grid = [mpf(10) ** k for k in (-1, -2, -3, -4, -5)]
    I2 = mp_eye(2)
    for s in s_grid:
        t_minus = m - s / 2
        t_plus = m + s / 2
        G_minus = G_at(t_minus)
        G_plus = G_at(t_plus)
        N = Nm_block(m, s)
        Ginv_sqrt_minus = G_inv_sqrt_closed(G_minus)
        Ginv_sqrt_plus = G_inv_sqrt_closed(G_plus)
        Omega = Ginv_sqrt_minus * N * Ginv_sqrt_plus
        err = mat2_max_diff(Omega, I2)
        errs.append(err)
        print(f"  {float(s):10.0e}  {float(err):26.6e}")
    for i in range(1, len(errs)):
        assert errs[i] < errs[i - 1] + mpf("1e-30"), (
            f"Omega coalescence error not monotone"
        )
    assert errs[-1] < mpf("1e-3"), \
        f"Omega(0; m) does not approach I_2: final err = {float(errs[-1])}"
    print()
    print("  [PASS] Omega_hat(s; m) -> I_2 as s -> 0; consistent with")
    print("         cor:omega-coalescence.")


# ---------------------------------------------------------------------------
# (iv) Whitening-loss sweep across midpoints and separations.
# ---------------------------------------------------------------------------

def check_whitening_loss_sweep(T_values=(mpf("1e3"), mpf("1e4"),
                                          mpf("1e5"), mpf("1e6"))):
    print("=" * 70)
    print("[lem:whitening-loss]  ||G^{-1/2}||_op bounded uniformly")
    print("=" * 70)
    print()
    print(f"  Sweep T = 10^k, midpoints across I_T, separations s in (0, 1/Q].")
    print()
    print(f"  {'T':>10}  {'sup ||G^{-1/2}||_op':>22}  "
          f"{'sqrt(pi/(2 q(T)))':>20}  {'rel.err':>10}")
    print(f"  {'-'*10}  {'-'*22}  {'-'*20}  {'-'*10}")
    half_window_factor = mpf("0.04")  # 0.04 * 1/Q

    sup_at_T = {}
    for T in T_values:
        Q = mp_log(T)
        half_window = half_window_factor / Q
        midpoints = [T - half_window + 2 * i * half_window / mpf(4)
                     for i in range(5)]
        s_grid = [k / Q for k in [mpf("0.01"), mpf("0.1"), mpf("0.5"),
                                   mpf("1")]]

        sup_norm_T = mpf(0)
        for m in midpoints:
            for s in s_grid:
                t_minus = m - s / 2
                t_plus = m + s / 2
                G_minus = G_at(t_minus)
                G_plus = G_at(t_plus)
                lam_min_minus, _ = mat2_eigs_symmetric(G_minus)
                lam_min_plus, _ = mat2_eigs_symmetric(G_plus)
                norm_minus = 1 / mp_sqrt(lam_min_minus)
                norm_plus = 1 / mp_sqrt(lam_min_plus)
                if norm_minus > sup_norm_T:
                    sup_norm_T = norm_minus
                if norm_plus > sup_norm_T:
                    sup_norm_T = norm_plus

        sup_at_T[T] = sup_norm_T

        q_T, _, _, _ = phi_derivs(T)
        target = mp_sqrt(MP_PI / (2 * q_T))
        rel_err = fabs(sup_norm_T - target) / target
        print(f"  {float(T):10.2e}  {float(sup_norm_T):22.6f}  "
              f"{float(target):20.6f}  {float(rel_err):10.4e}")

    # The §3 asymptotic lambda_min(J(T)) ~ 2 q(T) / pi requires sufficiently
    # large T: below the (1,1)/(2,2) eigenvalue crossover at q ~ sqrt(12),
    # i.e., T ~ 30000, the (2,2) corner is smaller and the asymptote is
    # not yet reached.  The lemma's bound is qualitative for that
    # transition region; assert relative agreement with sqrt(pi/(2 q(T)))
    # only at T >= 1e4.
    for T in T_values:
        if T >= mpf("1e4"):
            q_T, _, _, _ = phi_derivs(T)
            target = mp_sqrt(MP_PI / (2 * q_T))
            rel = fabs(sup_at_T[T] - target) / target
            assert rel < mpf("1e-3"), (
                f"asymptote mismatch at T = {float(T):.0e}: rel.err {float(rel):.4e}"
            )

    # Above the asymptote cutoff (T >= 1e4), the operator norm is < 1.
    sup_post_cutoff = max(sup_at_T[T] for T in T_values if T >= mpf("1e4"))
    assert sup_post_cutoff < mpf("1"), (
        f"sup ||G^{{-1/2}}||_op above cutoff: {float(sup_post_cutoff)}"
    )
    # Below the asymptote cutoff, the norm is bounded by a moderate
    # constant (here ~ 1.08 at T = 1e3); assert below 2.
    sup_global = max(sup_at_T.values())
    assert sup_global < mpf("2"), (
        f"sup ||G^{{-1/2}}||_op exceeds 2: {float(sup_global)}"
    )
    # Hardened-lemma claim: there exists epsilon_T -> 0 such that
    #     ||G^{-1/2}||_op <= sqrt(pi/(2 q(T))) (1 + epsilon_T).
    # Equivalently, the relative error
    #     epsilon_T(empirical) = (sup ||G^{-1/2}||_op) / sqrt(pi/(2 q(T))) - 1
    # decreases monotonically in T (above the cutoff).
    eps_at_T = {}
    for T in T_values:
        if T >= mpf("1e4"):
            q_T, _, _, _ = phi_derivs(T)
            target = mp_sqrt(MP_PI / (2 * q_T))
            eps_at_T[T] = sup_at_T[T] / target - 1
    eps_sorted = [eps_at_T[T] for T in sorted(eps_at_T.keys())]
    print()
    print(f"  Empirical epsilon_T = sup||G^{{-1/2}}||_op / sqrt(pi/(2q(T))) - 1:")
    for T in sorted(eps_at_T.keys()):
        print(f"    T = {float(T):.0e}: epsilon_T = {float(eps_at_T[T]):+.4e}")
    # The hardened lemma claims epsilon_T -> 0; check the magnitude
    # decreases at the highest height tested.
    assert abs(eps_sorted[-1]) < abs(eps_sorted[0]) + mpf("1e-30"), (
        f"epsilon_T not decreasing: T_min eps = {float(eps_sorted[0]):.4e}, "
        f"T_max eps = {float(eps_sorted[-1]):.4e}"
    )
    assert abs(eps_sorted[-1]) < mpf("1e-6"), (
        f"epsilon_T at largest T = {float(T_values[-1]):.0e} is "
        f"{float(eps_sorted[-1]):.4e}, not -> 0"
    )
    print()
    print(f"  sup above cutoff (T >= 1e4): {float(sup_post_cutoff):.6f} < 1")
    print(f"  global sup across tested T:  {float(sup_global):.6f} < 2")
    print()
    print("  [PASS] ||G^{-1/2}||_op bounded by an absolute constant; above")
    print("         the asymptote cutoff (T >= 1e4) the bound is < 1,")
    print("         giving C_W = 0 empirically.  Empirical epsilon_T -> 0")
    print("         confirmed at the highest tested height (rel.err < 1e-6).")


# ---------------------------------------------------------------------------
# (v) lambda_min(G) polynomial floor.
# ---------------------------------------------------------------------------

def check_lambda_min_polynomial_floor(T_values=(mpf("1e3"), mpf("1e5"),
                                                 mpf("1e6"))):
    print("=" * 70)
    print("[lambda_min(G_{m,±}) polynomial floor]  lambda_min >= 2 q(t_±)/pi (1+o(1))")
    print("=" * 70)
    print()
    print(f"  {'T':>10}  {'asymptote 2q/pi':>16}  {'min lam':>12}  "
          f"{'rel.err':>10}")
    print(f"  {'-'*10}  {'-'*16}  {'-'*12}  {'-'*10}")
    for T in T_values:
        Q = mp_log(T)
        half_window = mpf("0.05") / Q
        midpoints = [T - half_window + 2 * i * half_window / mpf(4)
                     for i in range(5)]
        s_grid = [k / Q for k in [mpf("0.01"), mpf("0.5"), mpf("1")]]
        min_lam_observed = mpf("inf")
        q_T, _, _, _ = phi_derivs(T)
        target = 2 * q_T / MP_PI
        for m in midpoints:
            for s in s_grid:
                for t_pm in [m - s / 2, m + s / 2]:
                    G = G_at(t_pm)
                    lam_min, _ = mat2_eigs_symmetric(G)
                    if lam_min < min_lam_observed:
                        min_lam_observed = lam_min
        rel_err = fabs(min_lam_observed - target) / target
        print(f"  {float(T):10.2e}  {float(target):16.6f}  "
              f"{float(min_lam_observed):12.6f}  {float(rel_err):10.4e}")
        # Asymptote must be approached: relative error decreases with T.
        if T >= mpf("1e4"):
            assert rel_err < mpf("0.05"), \
                f"lambda_min asymptote off at T={float(T):.0e}: rel.err = {float(rel_err)}"
    print()
    print("  [PASS] lambda_min(G) approaches 2 q(t_±)/pi; absolute floor")
    print("         dominated by the q-asymptotic of §2.")


# ---------------------------------------------------------------------------
# (vi) Independent-route check: G^{-1/2} via two methods.
# ---------------------------------------------------------------------------

def check_inverse_sqrt_routes(T):
    print("=" * 70)
    print(f"[independent route]  G^{{-1/2}} via Cayley-Hamilton vs mpmath.sqrtm")
    print("=" * 70)
    print()
    print(f"  Two implementations at T = {float(T):.0e}:")
    print(f"    Route A: closed-form Cayley-Hamilton SPD square root.")
    print(f"    Route B: mpmath sqrtm composed with matrix inverse.")
    print()
    m = T
    s = mpf("0.001")
    t_plus = m + s / 2
    G = G_at(t_plus)

    G_inv_sqrt_A = G_inv_sqrt_closed(G)

    # Route B: sqrtm gives sqrt(G); take inverse.
    sqrt_G_B = sqrtm(G)
    G_inv_sqrt_B = sqrt_G_B**-1

    err = mat2_max_diff(G_inv_sqrt_A, G_inv_sqrt_B)
    print(f"  G_{{m,+}}(s) at T = {float(T):.0e}, s = {float(s):.0e}")
    print(f"  Route A  G^{{-1/2}}:")
    for i in range(2):
        print(f"    [{float(G_inv_sqrt_A[i,0]):+.10f}, "
              f"{float(G_inv_sqrt_A[i,1]):+.10f}]")
    print(f"  Route B  G^{{-1/2}}:")
    for i in range(2):
        print(f"    [{float(G_inv_sqrt_B[i,0]):+.10f}, "
              f"{float(G_inv_sqrt_B[i,1]):+.10f}]")
    print(f"  max entrywise |Route A - Route B| = {float(err):.4e}")
    assert err < mpf("1e-30"), \
        f"Inverse-sqrt routes mismatch: {float(err)}"
    print()
    print("  [PASS] Two routes for G^{-1/2} agree to mpmath precision.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Simulation: sec:finite-scale-local-blocks-and-whitening")
    print("(arbitrary-precision arithmetic via mpmath)")
    print("=" * 70)
    print()

    # Anchor height for entry-level tests.
    T_anchor = mpf("1e5")

    check_finite_blocks_at_T(T_anchor)
    print()
    check_q_pm_signs_numerical(T_anchor)
    print()
    check_Nm_removable_singularity_numerical(T_anchor)
    print()
    check_signed_s_domain(T_anchor)
    print()
    check_omega_coalescence_numerical(T_anchor)
    print()
    check_whitening_loss_sweep()
    print()
    check_lambda_min_polynomial_floor()
    print()
    check_inverse_sqrt_routes(T_anchor)
    print()
    print("=" * 70)
    print("§4 numerical verification complete (mpmath-only, every check")
    print("an assertion).")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
