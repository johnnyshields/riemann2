"""Numerical simulation: sec:n-point-odd-moment-cancellation.

Numerical regression harness for the parity identities of §9.

Coverage:

  * Coefficient identities (lem:n-point-coefficients) at high N
    (N up to 12), beyond what symbolic verification reaches in
    reasonable time.
  * mu_hat_{N,Q}(z) low odd-jet vanishing at z = 0, computed via
    finite-difference odd derivatives at high mpmath precision.
  * Convolution stability: random even bumps (mpmath-generated)
    paired with mu_hat_{N,Q}; numerical odd derivatives at z = 0
    asserted to vanish to machine precision.
  * Stress: confirm the FIRST surviving odd derivative
    d^{2N-1} mu_hat_{N,Q}(0) is bounded away from zero (positive
    nonzero in absolute value) at high N.

Every check is an assertion.  No numpy, no math, no built-in
float arithmetic in the verification loop.

Run:
  python3 rh/simulation/sec-n-point-odd-moment-cancellation.py
"""

import sys

from mpmath import (
    binomial as mp_binomial,
    exp as mp_exp,
    log as mp_log,
    mp,
    mpf,
    power,
)


mp.dps = 50  # plenty of headroom for the exponential / finite-difference terms


# ---------------------------------------------------------------------------
# Coefficients a_j^{(N)} in mpmath.
# ---------------------------------------------------------------------------

def a_coeff_mp(N, j):
    """a_j^{(N)} = (-1)^{j+1} * j * C(2N, N+j) / C(2N-2, N-1)."""
    sign = mpf(1) if (j % 2 == 1) else mpf(-1)
    num = sign * mpf(j) * mp_binomial(2 * N, N + j)
    den = mp_binomial(2 * N - 2, N - 1)
    return num / den


def coefficients(N):
    return [a_coeff_mp(N, j) for j in range(1, N + 1)]


# ---------------------------------------------------------------------------
# (i) Coefficient identities to high N.
# ---------------------------------------------------------------------------

def check_coefficient_identities(N_values):
    print("=" * 70)
    print("[lem:n-point-coefficients]  numerical at high N")
    print("=" * 70)
    print()
    print(f"  {'N':>4}  {'sum a_j':>20}  {'sum |a_j| - (2N-1)':>22}  "
          f"{'max odd moment':>22}")
    print(f"  {'-'*4}  {'-'*20}  {'-'*22}  {'-'*22}")
    saved_dps = mp.dps
    # The odd-moment cancellation involves alternating sums of binomials
    # that can reach ~ 10^k for N ~ 12; boost precision generously so the
    # cancellation residual is genuinely small relative to the working dps.
    mp.dps = max(saved_dps, 100)
    try:
        for N in N_values:
            a = coefficients(N)
            s_sum = sum(a)
            s_abs = sum(abs(c) for c in a)

            # Identity 1: sum a_j == 1.
            err_sum = abs(s_sum - 1)
            assert err_sum < mpf("1e-50"), \
                f"N={N}: |sum a_j - 1| = {float(err_sum)}"

            # Identity 2: sum |a_j| == 2N - 1.
            err_abs = abs(s_abs - (2 * N - 1))
            assert err_abs < mpf("1e-50"), \
                f"N={N}: |sum |a_j| - (2N-1)| = {float(err_abs)}"

            # Identity 3: sum a_j j^{2r+1} == 0 for 0 <= r <= N-2.
            # The cancellation amplitude scales like the largest |a_j| j^{2r+1}
            # which is at most (2N - 1) N^{2r+1}; require the residual to be
            # smaller than that times an mp.dps-derived tolerance.
            max_odd = mpf(0)
            for r in range(0, N - 1):
                m = sum(a[j - 1] * mpf(j)**(2 * r + 1)
                        for j in range(1, N + 1))
                if abs(m) > max_odd:
                    max_odd = abs(m)
            scale = mpf(2 * N - 1) * mpf(N)**(2 * (N - 2) + 1)
            tol = scale * mpf(10) ** (-(mp.dps - 20))
            assert max_odd < tol, (
                f"N={N}: max odd moment = {float(max_odd):.4e}, "
                f"exceeds {float(tol):.4e} (scale = {float(scale):.4e})"
            )

            print(f"  {N:>4}  {float(s_sum):20.16f}  {float(err_abs):22.4e}  "
                  f"{float(max_odd):22.4e}")
    finally:
        mp.dps = saved_dps
    print()
    print(f"  [PASS] sum a_j = 1, sum |a_j| = 2N-1, all odd moments vanish")
    print(f"         (tolerance scaled by max|a_j j^k|) for "
          f"N in {tuple(N_values)}.")


# ---------------------------------------------------------------------------
# (ii) Numerical odd-derivative vanishing of mu_hat_{N,Q}(z) at z = 0.
# ---------------------------------------------------------------------------

def mu_hat(N, Q, z):
    """mu_hat_{N,Q}(z) = sum a_j^{(N)} exp(j z / Q^2)."""
    a = coefficients(N)
    return sum(a[j - 1] * mp_exp(mpf(j) * z / Q**2) for j in range(1, N + 1))


def central_finite_diff_odd(f, z0, order):
    """High-precision odd-order derivative via mpmath.diff.

    mpmath.diff uses an adaptive central difference; with mp.dps boosted,
    it returns f^{(n)}(z0) to the working precision for analytic f.
    """
    from mpmath import diff as mp_diff
    return mp_diff(f, z0, order)


def check_mu_hat_odd_vanishing(N_values=(2, 3, 4, 5, 6, 7)):
    print("=" * 70)
    print("[mu_hat_{N,Q}]  d^{2r+1} mu_hat(0) = 0 for 0 <= r <= N-2,")
    print("                d^{2N-1} mu_hat(0) is nonzero (first surviving)")
    print("=" * 70)
    print()
    # Choose Q = 2 so that the first surviving derivative
    #     d^{2N-1} mu_hat(0) = C_N / Q^{2(2N-1)}
    # remains numerically robust at the highest tested N.
    Q = mpf(2)
    print(f"  Q = {float(Q)} (chosen so the first surviving order at high N")
    print(f"   is comfortably above the FD noise floor)")
    print()
    print(f"  {'N':>4}  {'order':>6}  {'d^{order} mu_hat(0)':>26}  "
          f"{'expected':>10}")
    print(f"  {'-'*4}  {'-'*6}  {'-'*26}  {'-'*10}")
    saved_dps = mp.dps
    mp.dps = max(saved_dps, 80)
    try:
        for N in N_values:
            f = lambda z, _N=N, _Q=Q: mu_hat(_N, _Q, z)
            for r in range(0, N - 1):
                order = 2 * r + 1
                d = central_finite_diff_odd(f, mpf(0), order)
                # mpmath.diff returns essentially the working-precision value;
                # require the residual to be at most the kernel scale times
                # 1e-20 (very loose since the value is identically zero
                # symbolically).
                tol = mpf("1e-20") * (mpf(1) / Q**(2 * order))
                assert abs(d) < tol, (
                    f"N={N}, order={order}: d^{order} mu_hat(0) = "
                    f"{float(d):.4e}, tol = {float(tol):.4e}"
                )
                print(f"  {N:>4}  {order:>6}  {float(d):+26.6e}  {'~ 0':>10}")
            # First surviving order: 2N - 1.  Expected value
            #     d^{2N-1} mu_hat(0) = C_N / Q^{2(2N-1)}, with
            #     C_N = (-1)^{N+1} (2N-1) N! (N-1)!.
            order_first = 2 * N - 1
            d_first = central_finite_diff_odd(f, mpf(0), order_first)
            from mpmath import factorial as mp_fact
            C_N = ((-1)**(N + 1) * mpf(2 * N - 1)
                   * mp_fact(N) * mp_fact(N - 1))
            expected = C_N / Q**(2 * order_first)
            err_first = abs(d_first - expected) / abs(expected)
            assert err_first < mpf("1e-15"), (
                f"N={N}: d^{order_first} mu_hat(0) = {float(d_first):.4e}, "
                f"expected {float(expected):.4e}, rel.err {float(err_first):.4e}"
            )
            print(f"  {N:>4}  {order_first:>6}  {float(d_first):+26.6e}  "
                  f"{'!= 0':>10}")
    finally:
        mp.dps = saved_dps
    print()
    print("  [PASS] mu_hat_{N,Q} odd-jet vanishing confirmed numerically;")
    print("         first surviving odd derivative at order 2N-1 matches the")
    print("         closed form C_N / Q^{2(2N-1)} with C_N = (-1)^{N+1}")
    print("                                            (2N-1) N! (N-1)!.")


# ---------------------------------------------------------------------------
# (iii) Convolution stability: random even bumps phi_hat.
# ---------------------------------------------------------------------------

def random_even_bump(seed_index, max_degree=8):
    """Deterministic even bump phi_hat(w) = c0 + c2 w^2 + c4 w^4 + ...,
    with coefficients drawn from a deterministic mpmath sequence.
    """
    # Deterministic pseudo-random mpmath sequence.
    coeffs = []
    for k in range(max_degree // 2 + 1):
        # Use a hash-like map that produces non-trivial mpf values.
        c = mpf((seed_index * 17 + k * 31) % 100) / mpf(100)
        coeffs.append(c)

    def phi_hat(w):
        return sum(coeffs[i] * w**(2 * i) for i in range(len(coeffs)))

    return phi_hat, coeffs


def check_convolution_parity(N_values=(2, 3, 4, 5), n_bumps=5):
    print("=" * 70)
    print("[convolution form]  d^{2r+1} (phi_hat(eta z) mu_hat(z))(0) = 0")
    print("=" * 70)
    print()
    Q = mpf(10)
    eta = mpf("0.7")
    print(f"  Q = {float(Q)}, eta = {float(eta)}; {n_bumps} random even bumps each.")
    print()
    print(f"  {'N':>4}  {'bump':>6}  {'order':>6}  "
          f"{'derivative at 0':>22}")
    print(f"  {'-'*4}  {'-'*6}  {'-'*6}  {'-'*22}")

    saved_dps = mp.dps
    mp.dps = max(saved_dps, 80)
    try:
        for N in N_values:
            for b in range(n_bumps):
                phi_hat, _ = random_even_bump(b)

                def f(z, _N=N, _Q=Q, _eta=eta, _phi=phi_hat):
                    return _phi(_eta * z) * mu_hat(_N, _Q, z)

                for r in range(0, N - 1):
                    order = 2 * r + 1
                    d = central_finite_diff_odd(f, mpf(0), order)
                    tol = mpf("1e-30")
                    assert abs(d) < tol, (
                        f"N={N}, bump={b}, order={order}: "
                        f"convolved derivative = {float(d):.4e}"
                    )
                    if r in (0, N - 2):  # print first and last for readability
                        print(f"  {N:>4}  {b:>6}  {order:>6}  "
                              f"{float(d):+22.6e}")
    finally:
        mp.dps = saved_dps
    print()
    print("  [PASS] Random even bumps preserve the parity vanishing under")
    print("         product with mu_hat_{N,Q}, confirmed to ~ 1e-7.")


# ---------------------------------------------------------------------------
# (iv) ell^1 control vs N: stress test for large N.
# ---------------------------------------------------------------------------

def check_ell1_growth(N_values=(2, 5, 10, 20, 30, 50)):
    print("=" * 70)
    print("[ell^1 control]  sum |a_j^{(N)}| = 2N - 1 across a wide N ladder")
    print("=" * 70)
    print()
    print(f"  {'N':>4}  {'sum |a_j|':>16}  {'2N - 1':>10}  {'rel. err':>12}")
    print(f"  {'-'*4}  {'-'*16}  {'-'*10}  {'-'*12}")
    for N in N_values:
        a = coefficients(N)
        s = sum(abs(c) for c in a)
        target = mpf(2 * N - 1)
        rel = abs(s - target) / target
        assert rel < mpf("1e-30"), \
            f"N={N}: sum|a_j| - (2N-1) = {float(s - target):.4e}, "\
            f"rel.err = {float(rel):.4e}"
        print(f"  {N:>4}  {float(s):16.4f}  {2*N-1:>10}  {float(rel):12.4e}")
    print()
    print("  [PASS] ell^1 identity holds across N up to 50; relative error")
    print("         below 1e-30 in every case.")


# ---------------------------------------------------------------------------
# (v) Scope stress: with a NON-EVEN bump, parity is broken.
# ---------------------------------------------------------------------------

def check_parity_broken_for_odd_bump(N=4):
    """Stress test rem:n-point-parity-needs-even-bump (scope statement):
    if phi_hat is allowed to have an odd component, parity vanishing
    fails.  This shows the convolution lemma's hypothesis "phi_hat even"
    is load-bearing.
    """
    print("=" * 70)
    print("[scope check]  non-even bump breaks parity vanishing")
    print("=" * 70)
    print()
    Q = mpf(10)
    eta = mpf("0.5")

    def odd_contaminated_bump(w):
        # phi_hat(w) = 1 + 0.3 w + 0.5 w^2  -- has an odd 0.3 w term.
        return 1 + mpf("0.3") * w + mpf("0.5") * w**2

    def f(z, _N=N, _Q=Q, _eta=eta):
        return odd_contaminated_bump(_eta * z) * mu_hat(_N, _Q, z)

    print(f"  N = {N}, Q = {float(Q)}, eta = {float(eta)}")
    print(f"  bump: phi_hat(w) = 1 + 0.3 w + 0.5 w^2 (NOT even).")
    print()
    saw_nonzero = False
    for r in range(0, N - 1):
        order = 2 * r + 1
        d = central_finite_diff_odd(f, mpf(0), order)
        is_nonzero = abs(d) > mpf("1e-7")
        marker = "NONZERO" if is_nonzero else "~ 0"
        print(f"    order {order}: derivative = {float(d):+.6e}   [{marker}]")
        if is_nonzero:
            saw_nonzero = True
    assert saw_nonzero, (
        "Parity vanishing did NOT break for an odd-contaminated bump; "
        "scope guardrail is not load-bearing as claimed."
    )
    print()
    print("  [PASS] At least one odd derivative is NONZERO when phi_hat has")
    print("         an odd component.  The convolution lemma's even-bump")
    print("         hypothesis is therefore necessary, not ornamental.")


# ---------------------------------------------------------------------------
# (vi) Independent route: closed-form (1-t)^{2N-1}(1+t) generating identity.
# ---------------------------------------------------------------------------

def check_difference_identity_numerical(N_values=(2, 3, 4, 5, 6, 8)):
    """Compare A_N(t) - A_N(1/t) computed two ways at random t > 0, t != 1:
       (a) directly from the coefficients,
       (b) via the closed form (-1)^N N / C(2N-2, N-1) t^{-N} (1-t)^{2N-1} (1+t).
    """
    print("=" * 70)
    print("[independent route]  A_N(t) - A_N(1/t) closed form vs direct sum")
    print("=" * 70)
    print()
    print(f"  {'N':>4}  {'t':>10}  {'direct':>22}  {'closed form':>22}  "
          f"{'|diff|':>10}")
    print(f"  {'-'*4}  {'-'*10}  {'-'*22}  {'-'*22}  {'-'*10}")
    test_ts = [mpf("0.5"), mpf("1.7"), mpf("0.13"), mpf("3.9")]
    for N in N_values:
        a = coefficients(N)
        for t in test_ts:
            direct = sum(a[j - 1] * (t**j - t**(-j)) for j in range(1, N + 1))
            closed = ((-1)**N * mpf(N) / mp_binomial(2 * N - 2, N - 1)
                      * t**(-N) * (1 - t)**(2 * N - 1) * (1 + t))
            err = abs(direct - closed)
            assert err < mpf("1e-30"), \
                f"N={N}, t={float(t)}: direct - closed = {float(err):.4e}"
            print(f"  {N:>4}  {float(t):10.4f}  {float(direct):+22.10e}  "
                  f"{float(closed):+22.10e}  {float(err):10.2e}")
    print()
    print("  [PASS] Direct coefficient sum and closed-form expression agree")
    print("         to << 1e-30 at every tested (N, t).")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Simulation: sec:n-point-odd-moment-cancellation")
    print("(arbitrary-precision arithmetic via mpmath)")
    print("=" * 70)
    print()

    check_coefficient_identities(N_values=(2, 3, 4, 5, 6, 7, 8, 10, 12))
    print()
    check_mu_hat_odd_vanishing()
    print()
    check_convolution_parity()
    print()
    check_ell1_growth()
    print()
    check_parity_broken_for_odd_bump()
    print()
    check_difference_identity_numerical()
    print()
    print("=" * 70)
    print("§9 numerical verification complete (mpmath-only, every check")
    print("an assertion).")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
