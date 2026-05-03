"""Numerical simulation: sec:toy-anomaly-and-transverse-obstruction.

Numerical regression harness for the migration of §5 staged at
rh/patches/sec-toy-anomaly-and-transverse-obstruction.tex.

Coverage:

  * Phi_toy derivatives q_toy, q_toy', q_toy'' at sampled points;
    cross-check against the closed form of
    Lemma~\ref{lem:toy-phase-derivatives}.
  * G_{toy,±}(s; m, u) ≻ 0 on a (d, q_0, u)-grid
    (Lemma~\ref{lem:toy-block-positivity}).
  * Anomaly u^2 scaling: at fixed (d, q_0), fit
    log |A_toy(Omega_toy)| against log u and assert slope ≈ 2 over the
    range where the leading term dominates the O(u^4) remainder.
  * Anomaly lower bound on compact d-range at several large q_0 values:
    assert |A_toy(Omega_toy(s; m, u))| >= c u^2 for d in a sampled
    compact D and q_0 in a sampled high-frequency ladder.
  * q_0-independence of the exponent: at fixed (d,u), sweep q_0 directly
    and confirm A_toy(Omega_toy)/u^2 remains bounded away from zero and
    approaches the q_0 -> infinity coefficient F_inf(d).
  * Rescaled compactness sweep: after S(q_0)=diag(q_0^{1/2},q_0^{3/2}),
    the rescaled G and N blocks stay uniformly bounded across a q_0 ladder.
  * Sign-independence in u: A_toy(Omega_toy(s; m, u)) is even in u
    (Lemma~\ref{lem:toy-anomaly-leading}, no u^1 term).
  * Cross-check the empirical leading u^2 coefficient against the
    sympy closed form F_inf(d) of eq:F-toy-closed-form.

All checks are assertions.  No numpy, no math, no built-in float in
the verification loop.

Run:
  python3 rh/simulation/sec-toy-anomaly-and-transverse-obstruction.py
"""

import sys

from mpmath import (
    cos as mp_cos,
    eye as mp_eye,
    fabs,
    log as mp_log,
    matrix as mp_matrix,
    mp,
    mpf,
    pi as MP_PI,
    sin as mp_sin,
    sqrt as mp_sqrt,
)


mp.dps = 40  # plenty for the leading-order regression


# ---------------------------------------------------------------------------
# Toy phase and its derivatives.
# ---------------------------------------------------------------------------

def Phi_toy(t, u, m0, q0):
    t = mpf(t); u = mpf(u); m0 = mpf(m0); q0 = mpf(q0)
    return q0 * (t - m0) + u**2 * (1 - mp_cos(q0 * (t - m0)))


def q_toy(tau, u, q0):
    tau = mpf(tau); u = mpf(u); q0 = mpf(q0)
    return q0 + u**2 * q0 * mp_sin(q0 * tau)


def qp_toy(tau, u, q0):
    tau = mpf(tau); u = mpf(u); q0 = mpf(q0)
    return u**2 * q0**2 * mp_cos(q0 * tau)


def qpp_toy(tau, u, q0):
    tau = mpf(tau); u = mpf(u); q0 = mpf(q0)
    return -u**2 * q0**3 * mp_sin(q0 * tau)


# ---------------------------------------------------------------------------
# §4 blocks G_{m,±}, N_m, evaluated for the toy phase.
# ---------------------------------------------------------------------------

def G_at_center(q_val, qp_val, qpp_val):
    """G_{m,±}(s) of eq:Gpm: same form as the §3 same-point block J(t_±)."""
    return mp_matrix([
        [2 * q_val / MP_PI,        qp_val / (2 * MP_PI)],
        [qp_val / (2 * MP_PI),     (qpp_val + 2 * q_val**3) / (12 * MP_PI)],
    ])


def G_toy_pm(s, m, u, q0, sign):
    tau = sign * mpf(s) / 2
    qv = q_toy(tau, u, q0)
    qpv = qp_toy(tau, u, q0)
    qppv = qpp_toy(tau, u, q0)
    return G_at_center(qv, qpv, qppv)


def N_toy_block(s, m, u, q0):
    """N_toy(s; m, u) of eq:Nm with toy substitutions."""
    s = mpf(s); m = mpf(m); u = mpf(u); q0 = mpf(q0)
    qm_val = q_toy(-s / 2, u, q0)
    qp_val = q_toy(+s / 2, u, q0)
    Delta = -q0 * s
    sd = mp_sin(Delta)
    cd = mp_cos(Delta)
    n11 = -2 * sd / s
    n12 = (sd + qp_val * s * cd) / s**2
    n21 = -(sd + qm_val * s * cd) / s**2
    n22 = ((qm_val + qp_val) * s * cd
           + (2 - qm_val * qp_val * s**2) * sd) / (2 * s**3)
    return mp_matrix([[n11 / MP_PI, n12 / MP_PI],
                      [n21 / MP_PI, n22 / MP_PI]])


# ---------------------------------------------------------------------------
# Closed-form 2x2 SPD inverse-square-root.
# ---------------------------------------------------------------------------

def inv_sqrt_2x2_SPD(M):
    a = M[0, 0]; b = M[0, 1]; c = M[1, 1]
    det_M = a * c - b**2
    s_M = mp_sqrt(det_M)
    tr_M = a + c
    denom = s_M * mp_sqrt(tr_M + 2 * s_M)
    return (1 / denom) * mp_matrix([[c + s_M, -b], [-b, a + s_M]])


def Omega_toy(s, m, u, q0):
    G_minus = G_toy_pm(s, m, u, q0, -1)
    G_plus = G_toy_pm(s, m, u, q0, +1)
    N = N_toy_block(s, m, u, q0)
    Hm = inv_sqrt_2x2_SPD(G_minus)
    Hp = inv_sqrt_2x2_SPD(G_plus)
    return Hm * N * Hp


def A_toy(s, m, u, q0):
    Om = Omega_toy(s, m, u, q0)
    return Om[0, 1] + Om[1, 0]


# ---------------------------------------------------------------------------
# Sympy F_inf(d) closed form, evaluated numerically.
# ---------------------------------------------------------------------------

def F_inf_closed_form(d):
    d = mpf(d)
    num = (
        2 * d**2 * mp_cos(d)
        + 5 * d**2 * mp_cos(2 * d)
        - 7 * d**2
        + 6 * d * mp_sin(d)
        - 15 * d * mp_sin(2 * d)
        - 12 * mp_cos(2 * d)
        + 12
    )
    den = 8 * d**3 * mp_sin(d / 2)
    return mp_sqrt(mpf(3)) * num / den


# ---------------------------------------------------------------------------
# Helpers.
# ---------------------------------------------------------------------------

def mat2_eigs_symmetric(M):
    a = M[0, 0]; b = M[0, 1]; c = M[1, 1]
    tr = a + c
    disc = mp_sqrt((a - c)**2 + 4 * b**2)
    return ((tr - disc) / 2, (tr + disc) / 2)


def mat2_det(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]


def loglog_slope(x1, y1, x2, y2):
    return (mp_log(y2) - mp_log(y1)) / (mp_log(x2) - mp_log(x1))

def mat2_max_abs(M):
    return max(fabs(M[i, j]) for i in range(2) for j in range(2))


def rescale_matrix_for_toy(M, q0):
    """Return S(q0)^{-1} M S(q0)^{-1}, S=diag(q0^{1/2},q0^{3/2})."""
    q0 = mpf(q0)
    left = mp_matrix([[q0**(-mpf("0.5")), 0], [0, q0**(-mpf("1.5"))]])
    return left * M * left


# ---------------------------------------------------------------------------
# Checks.
# ---------------------------------------------------------------------------

def check_toy_phase_derivatives_mp():
    print("=" * 70)
    print("[lem:toy-phase-derivatives]  Phi_toy derivatives at sample points")
    print("=" * 70)
    samples = [
        (mpf("0.1"), mpf("0.05"), mpf("3.0")),
        (mpf("0.3"), mpf("0.1"),  mpf("5.0")),
        (mpf("-0.2"), mpf("0.08"), mpf("4.5")),
    ]
    eps = mpf("1e-25")
    for tau, u, q0 in samples:
        # Closed form vs finite-difference cross-check via mpmath.diff.
        from mpmath import diff
        f = lambda x: Phi_toy(x, u, mpf("0"), q0)
        q_expected = q_toy(tau, u, q0)
        q_fd = diff(f, tau, 1)
        assert fabs(q_expected - q_fd) < eps, (
            f"q_toy mismatch at tau={tau}, u={u}, q0={q0}: "
            f"closed={q_expected}, fd={q_fd}, delta={q_expected - q_fd}"
        )
        qp_expected = qp_toy(tau, u, q0)
        qp_fd = diff(f, tau, 2)
        assert fabs(qp_expected - qp_fd) < eps, (
            f"q_toy' mismatch at tau={tau}, u={u}, q0={q0}"
        )
        qpp_expected = qpp_toy(tau, u, q0)
        qpp_fd = diff(f, tau, 3)
        assert fabs(qpp_expected - qpp_fd) < eps, (
            f"q_toy'' mismatch at tau={tau}, u={u}, q0={q0}"
        )
    print(f"  [PASS] q_toy, q_toy', q_toy'' match mpmath.diff at "
          f"{len(samples)} sample points.")


def check_toy_block_positivity_sweep():
    print("=" * 70)
    print("[lem:toy-block-positivity]  G_{toy,±}(s) ≻ 0 on (d, q_0, u)-grid")
    print("=" * 70)
    d_grid = [mpf("0.5"), mpf("1.0"), mpf("1.5"), mpf("2.0"), mpf("2.5")]
    q0_grid = [mpf("3.0"), mpf("5.0"), mpf("8.0"), mpf("12.0")]
    u_grid = [mpf("0.05"), mpf("0.1"), mpf("0.2")]
    min_lambda = None
    min_lambda_over_q0 = None
    samples_checked = 0
    for d in d_grid:
        for q0 in q0_grid:
            s = d / q0
            for u in u_grid:
                for sign in (-1, +1):
                    G = G_toy_pm(s, mpf("0"), u, q0, sign)
                    eigs = mat2_eigs_symmetric(G)
                    lam_min = min(eigs)
                    assert lam_min > 0, (
                        f"G_toy non-positive at d={d}, q0={q0}, u={u}, "
                        f"sign={sign}: lam_min = {lam_min}"
                    )
                    if min_lambda is None or lam_min < min_lambda:
                        min_lambda = lam_min
                    ratio = lam_min / q0
                    if min_lambda_over_q0 is None or ratio < min_lambda_over_q0:
                        min_lambda_over_q0 = ratio
                    samples_checked += 1
    print(f"  Checked {samples_checked} (d, q_0, u, sign) configurations.")
    print(f"  [PASS] min lambda_min(G_{{toy,±}}) >= "
          f"{float(min_lambda):.4e} > 0.")
    print(f"         min lambda_min/q_0 >= {float(min_lambda_over_q0):.4e},")
    print("         consistent with the q_0-growing lower bound in the lemma.")



def check_rescaled_block_compactness_sweep():
    print("=" * 70)
    print("[uniform remainder guard]  rescaled G/N bounded across q_0 ladder")
    print("=" * 70)
    d_grid = [mpf("0.6"), mpf("1.0"), mpf("1.5"), mpf("2.0"), mpf("2.4")]
    q0_grid = [mpf("5.0"), mpf("10.0"), mpf("20.0"), mpf("50.0"), mpf("100.0")]
    u_grid = [mpf("0.0"), mpf("0.05"), mpf("0.10")]
    max_scaled = mpf("0")
    for d in d_grid:
        for q0 in q0_grid:
            s = d / q0
            for u in u_grid:
                for sign in (-1, +1):
                    G = G_toy_pm(s, mpf("0"), u, q0, sign)
                    Gt = rescale_matrix_for_toy(G, q0)
                    max_scaled = max(max_scaled, mat2_max_abs(Gt))
                N = N_toy_block(s, mpf("0"), u, q0)
                Nt = rescale_matrix_for_toy(N, q0)
                max_scaled = max(max_scaled, mat2_max_abs(Nt))
    assert max_scaled < mpf("10"), (
        f"rescaled toy blocks not uniformly bounded; max entry = {max_scaled}"
    )
    print(f"  [PASS] max entry of rescaled G/N blocks <= {float(max_scaled):.4e}")
    print("         on sampled compact D, u-grid, and q_0 ladder.")


def check_anomaly_u2_scaling():
    print("=" * 70)
    print("[lem:toy-anomaly-leading]  A_toy(Omega_toy) ~ u^2 at fixed d")
    print("=" * 70)
    test_points = [
        (mpf("1.0"), mpf("8.0")),
        (mpf("1.5"), mpf("12.0")),
        (mpf("2.0"), mpf("16.0")),
    ]
    u_pair = (mpf("0.005"), mpf("0.01"))
    for d, q0 in test_points:
        s = d / q0
        a1 = fabs(A_toy(s, mpf("0"), u_pair[0], q0))
        a2 = fabs(A_toy(s, mpf("0"), u_pair[1], q0))
        assert a1 > 0 and a2 > 0, f"|A_toy| zero at d={d}, q0={q0}"
        slope = loglog_slope(u_pair[0], a1, u_pair[1], a2)
        deviation = fabs(slope - 2)
        assert deviation < mpf("0.01"), (
            f"slope at d={d}, q0={q0} is {slope}, expected ~2; "
            f"deviation = {deviation}"
        )
        print(f"  d={float(d):.2f}, q0={float(q0):.1f}: "
              f"slope = {float(slope):.6f} (expected ≈ 2.0)")
    print(f"  [PASS] |A_toy(Omega_toy)| ~ u^2 verified over "
          f"{len(test_points)} grid points.")


def check_anomaly_lower_bound_on_compact_d():
    print("=" * 70)
    print("[eq:F-toy-lower-bound]  |A_toy| >= c u^2 on compact D, q_0 ladder")
    print("=" * 70)
    d_grid = [mpf(f"{p}") for p in (
        "0.6", "0.8", "1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.2"
    )]
    q0_grid = [mpf("20.0"), mpf("50.0"), mpf("100.0")]
    u = mpf("0.01")
    global_min_ratio = None
    for q0 in q0_grid:
        min_ratio = None
        for d in d_grid:
            s = d / q0
            a = fabs(A_toy(s, mpf("0"), u, q0))
            ratio = a / u**2
            assert ratio > mpf("1e-3"), (
                f"|A_toy|/u^2 = {ratio} at d={d} (q0={q0}) too small"
            )
            min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
            global_min_ratio = ratio if global_min_ratio is None else min(global_min_ratio, ratio)
        print(f"  q0={float(q0):6.1f}: min_d |A_toy|/u^2 >= {float(min_ratio):.4e}")
    print(f"  [PASS] global min over D and q_0 ladder >= {float(global_min_ratio):.4e}.")


def check_anomaly_height_independence():
    print("=" * 70)
    print("[A_toy = 0 visibility exponent]  q_0-independence sweep")
    print("=" * 70)
    d = mpf("1.5")
    u = mpf("0.01")
    q0_grid = [mpf("5.0"), mpf("10.0"), mpf("20.0"), mpf("50.0"), mpf("100.0")]
    ratios = []
    F_inf_at_d = F_inf_closed_form(d)
    print(f"  d = {float(d):.2f}, F_inf(d) = {float(F_inf_at_d):.6f}")
    for q0 in q0_grid:
        s = d / q0
        a = A_toy(s, mpf("0"), u, q0)
        ratio = a / u**2
        ratios.append((q0, ratio))
        print(f"  q_0 = {float(q0):7.2f}, A_toy/u^2 = {float(ratio):.6f}")
    abs_F = fabs(F_inf_at_d)
    sign_F = +1 if F_inf_at_d > 0 else -1
    diffs = []
    for (q0, ratio) in ratios:
        sign_ratio = +1 if ratio > 0 else -1
        assert sign_ratio == sign_F, (
            f"Sign flip at q0={q0}: ratio={ratio}, F_inf={F_inf_at_d}"
        )
        assert mpf("0.3") * abs_F <= fabs(ratio) <= mpf("1.3") * abs_F, (
            f"At q0={q0}: |A_toy/u^2| = {fabs(ratio)}, "
            f"out of [{0.3 * float(abs_F)}, {1.3 * float(abs_F)}]"
        )
        diffs.append(fabs(ratio - F_inf_at_d))
    assert diffs[-1] / abs_F < mpf("0.05"), (
        f"Final q0={q0_grid[-1]} relative error too large: {diffs[-1] / abs_F}"
    )
    assert diffs[-1] < diffs[0], (
        f"High-frequency error did not improve: first={diffs[0]}, final={diffs[-1]}"
    )
    print(f"  [PASS] A_toy/u^2 has the same sign as F_inf, remains bounded "
          f"away from zero, and is within 5% of F_inf at the largest q_0 "
          f"(visibility exponent A_toy = 0).")


def check_anomaly_sign_independence_in_u():
    print("=" * 70)
    print("[lem:toy-anomaly-leading]  A_toy(u) = A_toy(-u) (even in u)")
    print("=" * 70)
    d = mpf("1.2")
    q0 = mpf("10.0")
    s = d / q0
    eps = mpf("1e-30")
    for u in (mpf("0.05"), mpf("0.1"), mpf("0.15")):
        a_pos = A_toy(s, mpf("0"), u, q0)
        a_neg = A_toy(s, mpf("0"), -u, q0)
        delta = fabs(a_pos - a_neg)
        assert delta < eps, (
            f"A_toy not even in u at u={u}: A(+u)={a_pos}, A(-u)={a_neg}"
        )
    print(f"  [PASS] A_toy(Omega_toy(s; m, u)) is even in u "
          f"(no u^1 term, by Phi_toy ~ u^2).")


def check_F_toy_against_sympy():
    print("=" * 70)
    print("[eq:F-toy-closed-form]  Empirical leading coefficient vs F_inf(d)")
    print("=" * 70)
    # F_toy(d, q_0) -> F_inf(d) at rate O(1/q_0); take q_0 = 500 for ~0.2%
    # convergence to assert match within 1% tolerance.
    q0 = mpf("500.0")
    u = mpf("0.001")  # small u so the u^4 remainder doesn't pollute.
    d_grid = [mpf(p) for p in ("0.7", "1.0", "1.3", "1.6", "1.9", "2.2")]
    max_rel = mpf("0")
    for d in d_grid:
        s = d / q0
        empirical = A_toy(s, mpf("0"), u, q0) / u**2
        closed = F_inf_closed_form(d)
        err = fabs(empirical - closed)
        rel = err / fabs(closed) if fabs(closed) > 0 else err
        assert rel < mpf("0.01"), (
            f"At d={d}, q0={q0}, u={u}: empirical={empirical}, "
            f"closed={closed}, rel err={rel}"
        )
        if rel > max_rel:
            max_rel = rel
    print(f"  [PASS] Empirical A_toy/u^2 matches F_inf(d) on sampled D "
          f"at q_0 = 500 (max rel err = {float(max_rel):.4e}).")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    check_toy_phase_derivatives_mp()
    print()
    check_toy_block_positivity_sweep()
    print()
    check_rescaled_block_compactness_sweep()
    print()
    check_anomaly_u2_scaling()
    print()
    check_anomaly_lower_bound_on_compact_d()
    print()
    check_anomaly_sign_independence_in_u()
    print()
    check_F_toy_against_sympy()
    print()
    check_anomaly_height_independence()
    print()
    print("=" * 70)
    print("All §5 checks passed at mpmath precision dps =", mp.dps)
    print("  - Phi_toy derivatives match closed form via mpmath.diff")
    print("  - G_{toy,±} ≻ 0 on (d, q_0, u)-grid")
    print("  - rescaled G/N blocks remain bounded across q_0 ladder")
    print("  - |A_toy(Omega_toy)| ~ u^2 (slope ≈ 2 in log-log)")
    print("  - |A_toy|/u^2 bounded below on compact D at large q_0")
    print("  - A_toy is even in u")
    print("  - Empirical A_toy/u^2 matches F_inf(d) closed form")
    print("  - Visibility exponent A_toy = 0 verified across heights")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
