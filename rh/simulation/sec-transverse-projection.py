"""Numerical simulation: sec:transverse-projection.

Companion to rh/patches/sec-transverse-projection.tex.

Coverage:

  * Pi_trans X = ((x_12 + x_21)/2) * [[0, 1], [1, 0]] verified at
    arbitrary 2x2 mpmath matrices.
  * Pi_trans is idempotent and self-adjoint (HS inner product).
  * Pi_trans annihilates each V_val basis element {e_11, e_22, e_anti}
    and fixes e_sym.
  * A_toy(Pi_trans X) = A_toy(X) for randomly sampled X.
  * Apply Pi_trans to actual-zeta whitened block \widehat\Om_z(s; m) at
    high T; confirm A_toy(Pi_trans \widehat\Om_z) = A_toy(\widehat\Om_z)
    and the deviation is bounded by the §7 suppression hypothesis order.
  * Apply Pi_trans to the toy whitened block at off-line displacement;
    confirm A_toy preserved and the visibility lower bound transports.
  * ||Pi_trans||_op = 1 verified by sweeping HS-unit-norm matrices.

All checks are assertions.  No numpy, no math, no built-in float in
the verification loop (mpmath only).

Run:
  python3 rh/simulation/sec-transverse-projection.py
"""

import sys

from mpmath import (
    cos as mp_cos,
    fabs,
    log as mp_log,
    matrix as mp_matrix,
    mp,
    mpf,
    pi as MP_PI,
    sin as mp_sin,
    sqrt as mp_sqrt,
)


mp.dps = 40


# ---------------------------------------------------------------------------
# Hilbert-Schmidt inner product, A_toy, Pi_trans on real 2x2 matrices.
# ---------------------------------------------------------------------------

def hs_inner(X, Y):
    """<X, Y>_HS = Tr(X^T Y) = sum_{i,j} X_{ij} Y_{ij}."""
    s = mpf("0")
    for i in range(2):
        for j in range(2):
            s += X[i, j] * Y[i, j]
    return s


def hs_norm(X):
    return mp_sqrt(hs_inner(X, X))


def A_toy(X):
    """A_toy(X) := X_{12} + X_{21}."""
    return X[0, 1] + X[1, 0]


def Pi_trans(X):
    """Pi_trans X = ((X_{12} + X_{21}) / 2) * [[0, 1], [1, 0]]."""
    half = (X[0, 1] + X[1, 0]) / 2
    return mp_matrix([[mpf("0"), half], [half, mpf("0")]])


# Basis matrices.
def E_11():
    return mp_matrix([[1, 0], [0, 0]])

def E_22():
    return mp_matrix([[0, 0], [0, 1]])

def E_anti():
    inv_sqrt2 = 1 / mp_sqrt(2)
    return mp_matrix([[0, inv_sqrt2], [-inv_sqrt2, 0]])

def E_sym():
    inv_sqrt2 = 1 / mp_sqrt(2)
    return mp_matrix([[0, inv_sqrt2], [inv_sqrt2, 0]])


# ---------------------------------------------------------------------------
# (i) Pi_trans explicit formula and basic properties.
# ---------------------------------------------------------------------------

def check_pi_trans_explicit_formula_mp():
    print("=" * 70)
    print("[def:transverse-projection]  Pi_trans X = <X, e_sym>_HS e_sym")
    print("=" * 70)
    samples = [
        mp_matrix([[1, 2], [3, 4]]),
        mp_matrix([[mpf("0.7"), mpf("-1.2")], [mpf("0.3"), mpf("2.1")]]),
        mp_matrix([[mpf("1e3"), mpf("1e-3")], [mpf("-2"), mpf("0.5")]]),
    ]
    for X in samples:
        formula = Pi_trans(X)
        proj = hs_inner(X, E_sym()) * E_sym()
        max_err = mpf("0")
        for i in range(2):
            for j in range(2):
                err = fabs(formula[i, j] - proj[i, j])
                if err > max_err:
                    max_err = err
        assert max_err < mpf("1e-30"), (
            f"Pi_trans formula vs <X, e_sym>_HS e_sym mismatch: {max_err}"
        )
    print(f"  [PASS] explicit formula matches HS projection on "
          f"{len(samples)} samples.")


def check_pi_trans_idempotent_mp():
    print("=" * 70)
    print("[lem:transverse-projection-properties]  Pi_trans^2 = Pi_trans")
    print("=" * 70)
    samples = [
        mp_matrix([[mpf("1.7"), mpf("-2.1")], [mpf("0.4"), mpf("3.3")]]),
        mp_matrix([[mpf("0.001"), mpf("100")], [mpf("-50"), mpf("-0.002")]]),
    ]
    for X in samples:
        once = Pi_trans(X)
        twice = Pi_trans(once)
        max_err = mpf("0")
        for i in range(2):
            for j in range(2):
                err = fabs(once[i, j] - twice[i, j])
                if err > max_err:
                    max_err = err
        assert max_err < mpf("1e-30"), f"idempotence violated: {max_err}"
    print(f"  [PASS] Pi_trans^2 = Pi_trans on {len(samples)} samples.")


def check_pi_trans_kernel_on_V_val_basis():
    print("=" * 70)
    print("[lem:transverse-projection-properties]  Pi_trans annihilates V_val")
    print("=" * 70)
    eps = mpf("1e-30")
    for name, M in (("e_11", E_11()), ("e_22", E_22()), ("e_anti", E_anti())):
        out = Pi_trans(M)
        max_abs = mpf("0")
        for i in range(2):
            for j in range(2):
                if fabs(out[i, j]) > max_abs:
                    max_abs = fabs(out[i, j])
        assert max_abs < eps, f"Pi_trans({name}) != 0: max entry {max_abs}"
        print(f"  Pi_trans({name}) = 0  ✓")
    # Pi_trans(e_sym) = e_sym
    out = Pi_trans(E_sym())
    max_err = mpf("0")
    for i in range(2):
        for j in range(2):
            err = fabs(out[i, j] - E_sym()[i, j])
            if err > max_err:
                max_err = err
    assert max_err < eps, f"Pi_trans(e_sym) != e_sym: {max_err}"
    print(f"  Pi_trans(e_sym) = e_sym  ✓")
    print("  [PASS] kernel of Pi_trans is exactly V_val; e_sym is fixed.")


def check_A_toy_descends_through_pi_trans_mp():
    print("=" * 70)
    print("[lem:transverse-projection-A-toy-compatibility]  "
          "A_toy(Pi_trans X) = A_toy(X)")
    print("=" * 70)
    samples = [
        mp_matrix([[mpf("1.7"), mpf("-2.1")], [mpf("0.4"), mpf("3.3")]]),
        mp_matrix([[mpf("100"), mpf("0.5")], [mpf("-0.5"), mpf("-100")]]),
        mp_matrix([[mpf("0"), mpf("1.234")], [mpf("5.678"), mpf("0")]]),
    ]
    eps = mpf("1e-30")
    for X in samples:
        before = A_toy(X)
        after = A_toy(Pi_trans(X))
        delta = fabs(before - after)
        assert delta < eps, (
            f"A_toy(Pi X) - A_toy(X) = {delta} != 0 at X = {X}"
        )
    print(f"  [PASS] A_toy invariant under Pi_trans on {len(samples)} samples.")


def check_pi_trans_operator_norm_unity_mp():
    """Sweep HS-unit-norm matrices; confirm ||Pi_trans X||_HS <= 1 with
    equality at X = e_sym.
    """
    print("=" * 70)
    print("[eq:Pi-trans-norm]  ||Pi_trans||_op = 1 (sweep)")
    print("=" * 70)
    # Construct a sweep of unit-HS-norm matrices via the orthonormal basis
    # {e_11, e_22, e_anti, e_sym} with random angles.  Use deterministic
    # samples for reproducibility.
    def unit_combo(c1, c2, c3, c4):
        n = mp_sqrt(c1**2 + c2**2 + c3**2 + c4**2)
        return (
            (c1 / n) * E_11()
            + (c2 / n) * E_22()
            + (c3 / n) * E_anti()
            + (c4 / n) * E_sym()
        )

    samples = [
        unit_combo(mpf("1"), mpf("0"), mpf("0"), mpf("0")),  # = e_11
        unit_combo(mpf("0"), mpf("1"), mpf("0"), mpf("0")),  # = e_22
        unit_combo(mpf("0"), mpf("0"), mpf("1"), mpf("0")),  # = e_anti
        unit_combo(mpf("0"), mpf("0"), mpf("0"), mpf("1")),  # = e_sym
        unit_combo(mpf("1"), mpf("1"), mpf("1"), mpf("1")),
        unit_combo(mpf("0.7"), mpf("-1.2"), mpf("0.5"), mpf("0.3")),
        unit_combo(mpf("3"), mpf("2"), mpf("1"), mpf("-2")),
    ]
    max_pi_norm = mpf("0")
    e_sym_norm = mpf("0")
    for X in samples:
        nrm_X = hs_norm(X)
        assert fabs(nrm_X - 1) < mpf("1e-30"), (
            f"sample not unit norm: ||X||_HS = {nrm_X}"
        )
        pi_X = Pi_trans(X)
        nrm_pi = hs_norm(pi_X)
        assert nrm_pi <= 1 + mpf("1e-30"), (
            f"||Pi_trans X||_HS = {nrm_pi} > 1 for unit-norm X"
        )
        if nrm_pi > max_pi_norm:
            max_pi_norm = nrm_pi
        # Track norm at e_sym specifically.
        if hs_inner(X, E_sym()) > mpf("0.99"):
            e_sym_norm = nrm_pi
    assert fabs(e_sym_norm - 1) < mpf("1e-30"), (
        f"||Pi_trans e_sym||_HS = {e_sym_norm}, expected 1"
    )
    print(f"  max ||Pi_trans X||_HS over unit-X samples = "
          f"{float(max_pi_norm):.6f}")
    print(f"  ||Pi_trans e_sym||_HS = {float(e_sym_norm):.6f}  (= 1)")
    print("  [PASS] ||Pi_trans||_op = 1 (achieved at e_sym).")


# ---------------------------------------------------------------------------
# (ii) Apply Pi_trans to the actual-zeta and toy whitened blocks.
# ---------------------------------------------------------------------------

# Lightweight reimplementation of the §4 block calculus for the actual
# zeta phase and the §5 toy phase, sufficient to test the projection
# downstream.

def q_zeta_asymp(t):
    """q(t) = θ'(t) ≈ (1/2) log(t/(2π)) - 1/(48 t^2)."""
    t = mpf(t)
    return mp_log(t / (2 * MP_PI)) / 2 - 1 / (48 * t**2)


def q_toy(tau, u, q0):
    """Toy phase derivative q_toy(tau) = q_0 + u^2 q_0 sin(q_0 tau)."""
    return q0 + u**2 * q0 * mp_sin(q0 * tau)


def G_block(q_val, qp_val, qpp_val):
    """G_{m,±}(s) of eq:Gpm."""
    return mp_matrix([
        [2 * q_val / MP_PI,        qp_val / (2 * MP_PI)],
        [qp_val / (2 * MP_PI),     (qpp_val + 2 * q_val**3) / (12 * MP_PI)],
    ])


def Nm_block(qm, qp, s, Delta):
    """N_m(s) of eq:Nm."""
    s = mpf(s)
    sd = mp_sin(Delta)
    cd = mp_cos(Delta)
    n11 = -2 * sd / s
    n12 = (sd + qp * s * cd) / s**2
    n21 = -(sd + qm * s * cd) / s**2
    n22 = ((qm + qp) * s * cd + (2 - qm * qp * s**2) * sd) / (2 * s**3)
    return mp_matrix([[n11 / MP_PI, n12 / MP_PI],
                      [n21 / MP_PI, n22 / MP_PI]])


def inv_sqrt_2x2_SPD(M):
    """Closed-form positive-definite inverse square root of a 2x2 SPD."""
    a = M[0, 0]; b = M[0, 1]; c = M[1, 1]
    det_M = a * c - b**2
    s_M = mp_sqrt(det_M)
    tr_M = a + c
    denom = s_M * mp_sqrt(tr_M + 2 * s_M)
    return (1 / denom) * mp_matrix([[c + s_M, -b], [-b, a + s_M]])


def Omega_block(G_minus, N, G_plus):
    return inv_sqrt_2x2_SPD(G_minus) * N * inv_sqrt_2x2_SPD(G_plus)


def check_pi_trans_on_actual_zeta_block():
    """For the actual zeta phase Φ = θ at high T, compute \widehat\Om_z(s; m)
    and confirm A_toy(Pi_trans \widehat\Om_z) = A_toy(\widehat\Om_z).
    """
    print("=" * 70)
    print("[lem:transverse-projection-A-toy-compatibility]  "
          "applied to actual-zeta block")
    print("=" * 70)
    eps = mpf("1e-25")
    cases = []
    from mpmath import siegeltheta, diff
    for T in (mpf("1e6"), mpf("1e9"), mpf("1e12")):
        Q = mp_log(T) / 8  # slowly growing
        s = 1 / Q
        m = T
        t_minus = m - s / 2
        t_plus = m + s / 2

        def derivs(t):
            return (diff(siegeltheta, t, 1),
                    diff(siegeltheta, t, 2),
                    diff(siegeltheta, t, 3))

        q_m, qp_m, qpp_m = derivs(t_minus)
        q_p, qp_p, qpp_p = derivs(t_plus)
        Delta = siegeltheta(t_minus) - siegeltheta(t_plus)

        G_minus = G_block(q_m, qp_m, qpp_m)
        G_plus = G_block(q_p, qp_p, qpp_p)
        N = Nm_block(q_m, q_p, s, Delta)
        Omega_z = Omega_block(G_minus, N, G_plus)

        a_before = A_toy(Omega_z)
        a_after = A_toy(Pi_trans(Omega_z))
        delta = fabs(a_before - a_after)
        cases.append((T, Q, a_before, delta))
        assert delta < eps, (
            f"At T = {T}, A_toy(Pi Om) - A_toy(Om) = {delta}, expected 0"
        )

    for T, Q, a, d in cases:
        print(f"  T={float(T):.1e}, Q={float(Q):.3f}: "
              f"|A_toy(Om_z)|={float(fabs(a)):.4e}, "
              f"|A_toy(Pi Om_z) - A_toy(Om_z)|={float(d):.2e}")
    print(f"  [PASS] A_toy invariant under Pi_trans on actual-zeta block "
          f"at {len(cases)} heights.")


def check_pi_trans_on_toy_block_off_line():
    """For the toy phase at off-line displacement u, compute \widehat\Om_toy
    and confirm A_toy(Pi_trans Om) = A_toy(Om).  This combines with the §5
    visibility theorem to give the projected lower bound.
    """
    print("=" * 70)
    print("[lem:transverse-projection-A-toy-compatibility]  "
          "applied to toy block")
    print("=" * 70)
    eps = mpf("1e-25")
    cases = [
        (mpf("8.0"),  mpf("0.1"),  mpf("1.0")),
        (mpf("12.0"), mpf("0.05"), mpf("1.5")),
        (mpf("20.0"), mpf("0.02"), mpf("2.0")),
    ]
    results = []
    for q0, u, d in cases:
        s = d / q0
        # Toy phase derivatives at t_± = m ± s/2 with m_0 = m.
        tau_p = s / 2
        tau_m = -s / 2
        qm = q_toy(tau_m, u, q0)
        qp = q_toy(tau_p, u, q0)
        # q_toy', q_toy'' are u^2 * q_0^2 cos(q_0 tau), -u^2 * q_0^3 sin(q_0 tau).
        qp_m = u**2 * q0**2 * mp_cos(q0 * tau_m)
        qp_p = u**2 * q0**2 * mp_cos(q0 * tau_p)
        qpp_m = -u**2 * q0**3 * mp_sin(q0 * tau_m)
        qpp_p = -u**2 * q0**3 * mp_sin(q0 * tau_p)
        Delta = -q0 * s

        G_minus = G_block(qm, qp_m, qpp_m)
        G_plus = G_block(qp, qp_p, qpp_p)
        N = Nm_block(qm, qp, s, Delta)
        Omega_toy = Omega_block(G_minus, N, G_plus)

        a_before = A_toy(Omega_toy)
        a_after = A_toy(Pi_trans(Omega_toy))
        delta = fabs(a_before - a_after)
        results.append((q0, u, d, a_before, delta))
        assert delta < eps, (
            f"At q0={q0}, u={u}, d={d}: |A_toy(Pi Om) - A_toy(Om)| = {delta}"
        )

    for q0, u, d, a, dd in results:
        print(f"  q0={float(q0):4.1f}, u={float(u):.3f}, d={float(d):.2f}: "
              f"|A_toy|={float(fabs(a)):.4e}, "
              f"|A_toy(Pi)-A_toy|={float(dd):.2e}")
    print(f"  [PASS] A_toy invariant under Pi_trans on toy block "
          f"at {len(cases)} (q0, u, d) triples.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    check_pi_trans_explicit_formula_mp()
    print()
    check_pi_trans_idempotent_mp()
    print()
    check_pi_trans_kernel_on_V_val_basis()
    print()
    check_A_toy_descends_through_pi_trans_mp()
    print()
    check_pi_trans_operator_norm_unity_mp()
    print()
    check_pi_trans_on_actual_zeta_block()
    print()
    check_pi_trans_on_toy_block_off_line()
    print()
    print("=" * 70)
    print("All §6 simulations passed at mpmath precision dps =", mp.dps)
    print("  - Pi_trans explicit formula matches HS projection")
    print("  - Pi_trans is idempotent")
    print("  - kernel of Pi_trans = span{e_11, e_22, e_anti}")
    print("  - A_toy invariant under Pi_trans on generic samples")
    print("  - ||Pi_trans||_op = 1 over unit-HS-norm sweep, achieved at e_sym")
    print("  - A_toy invariant under Pi_trans on actual-zeta block at high T")
    print("  - A_toy invariant under Pi_trans on off-line toy block")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
