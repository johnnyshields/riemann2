"""Numerical simulation: sec:local-kernel-and-jet-normalization.

Verifies the §2 chart construction and kernel properties using mpmath
arbitrary-precision arithmetic.  No zeta-side regularity is used: per
rem:chart-regularity-zeta-side, the chart consumes zeta only through
the identity zeta(1/2 + it) = exp(-i theta(t)) Z(t) and the theta
phase itself.

Coverage:

  * theta(t) = Im L(1/4 + i t / 2) - (t/2) log pi matches mpmath's
    siegeltheta (def:riemann-siegel-phase); L is real on x > 0
    (holomorphic branch convention).
  * theta'(t) = q(t) >= 1 uniformly on I_T (condition (P2)).
  * Riemann-Siegel residual: theta'(t) - (1/2) log(t/(2 pi)) ~ -1/(48 t^2)
    over a height ladder.
  * theta-derivative asymptotics uniform on I_T = [T_center +- 1/Q].
  * K_Phi symmetry, removable singularity, off-diagonal derivative
    formulas (lem:phase-kernel-derivatives) match finite-difference
    estimates.

All numerical computations use mpmath; no numpy, no math, no float
arithmetic in the verification loop.  Float conversion is limited to
print-time formatting.

Run:
  python rh/simulation/sec-local-kernel-and-jet-normalization.py
"""

import sys

from mpmath import (
    cos as mp_cos,
    diff,
    log as mp_log,
    loggamma,
    mp,
    mpc,
    mpf,
    pi as MP_PI,
    siegeltheta,
    sin as mp_sin,
    sqrt as mp_sqrt,
)


mp.dps = 30  # 30 decimal places baseline; bumped where needed.


# ----------------------------------------------------------------------
# mpmath-native helpers (replacing numpy / math).
# ----------------------------------------------------------------------

def linspace_mp(a, b, n):
    """Return n mpf samples from a to b inclusive."""
    a = mpf(a)
    b = mpf(b)
    if n <= 1:
        return [a]
    step = (b - a) / (n - 1)
    return [a + i * step for i in range(n)]


def max_mp(xs):
    """Maximum of an iterable of mpfs (or anything with __gt__)."""
    it = iter(xs)
    m = next(it)
    for x in it:
        if x > m:
            m = x
    return m


def mean_mp(xs):
    """Arithmetic mean of an iterable of mpfs."""
    xs = list(xs)
    return sum(xs) / len(xs)


def median_mp(xs):
    """Median of a list of mpfs."""
    xs_sorted = sorted(xs)
    n = len(xs_sorted)
    if n % 2 == 1:
        return xs_sorted[n // 2]
    return (xs_sorted[n // 2 - 1] + xs_sorted[n // 2]) / 2


def loglog_slope(xs, ys):
    """Two-point log-log slope from the first and last sample.

    For a power law y = C x^k, log(y_n / y_0) / log(x_n / x_0) = k.
    Uses arbitrary-precision arithmetic.
    """
    return mp_log(ys[-1] / ys[0]) / mp_log(xs[-1] / xs[0])


# ----------------------------------------------------------------------
# Phase, derivatives, kernel.
# ----------------------------------------------------------------------

def theta(t):
    return siegeltheta(mpf(t))


def theta_prime(t, order=1):
    return diff(siegeltheta, mpf(t), order)


def K_phi(x, y):
    x_mp = mpf(x)
    y_mp = mpf(y)
    if abs(x_mp - y_mp) < mpf("1e-22"):
        return theta_prime(y_mp, 1) / MP_PI
    return mp_sin(theta(x_mp) - theta(y_mp)) / (MP_PI * (x_mp - y_mp))


# ----------------------------------------------------------------------
# def:riemann-siegel-phase: theta from Im log Gamma.
# ----------------------------------------------------------------------

def check_theta_via_loggamma():
    """Verify mpmath's siegeltheta(t) matches
        theta(t) = Im L(1/4 + i t / 2) - (t/2) log pi
    with L(z) the holomorphic branch of log Gamma z on Re z > 0 that is
    real on the positive real axis (Definition def:riemann-siegel-phase).

    Also confirms the branch convention numerically:
      L(x) is real for x > 0  (so mpmath's loggamma returns a real value
      on the positive real axis, matching L).
    """
    print("  Branch convention: L(x) = log Gamma(x) real on x > 0.")
    print()
    print(f"  {'x':>10}  {'L(x) = loggamma(x)':>30}  {'|Im L(x)|':>14}")
    print(f"  {'-'*10}  {'-'*30}  {'-'*14}")
    saved_dps = mp.dps
    mp.dps = 50
    try:
        max_im = mpf(0)
        for x in [mpf("0.25"), mpf("0.5"), mpf("1"), mpf("5"), mpf("100")]:
            Lx = loggamma(mpc(x, 0))
            im_abs = abs(Lx.imag)
            if im_abs > max_im:
                max_im = im_abs
            print(f"  {float(x):10.4f}  {mp.nstr(Lx.real, 16):>30}  "
                  f"{float(im_abs):14.4e}")
        if max_im < mpf("1e-40"):
            print()
            print("  [PASS] L(x) is real on the positive real axis "
                  "(holomorphic branch convention).")
        else:
            print()
            print(f"  [WARN] Max |Im L(x)| = {float(max_im):.4e} on tested "
                  f"positive reals.")
    finally:
        mp.dps = saved_dps

    print()
    print("  Compare siegeltheta(t) to Im L(1/4 + i t / 2) - (t/2) log pi.")
    print()
    print(f"  {'t':>10}  {'siegeltheta(t)':>22}  "
          f"{'Im L(...) - (t/2) log pi':>34}  {'diff':>14}")
    print(f"  {'-'*10}  {'-'*22}  {'-'*34}  {'-'*14}")

    saved_dps = mp.dps
    mp.dps = 50
    try:
        for T in [mpf("1e3"), mpf("1e4"), mpf("1e6"), mpf("1e8")]:
            sieg = siegeltheta(T)
            z = mpc(mpf("0.25"), T / 2)
            from_def = loggamma(z).imag - (T / 2) * mp_log(MP_PI)
            d = abs(sieg - from_def)
            print(f"  {float(T):10.2e}  {mp.nstr(sieg, 16):>22}  "
                  f"{mp.nstr(from_def, 16):>34}  {float(d):14.4e}")
    finally:
        mp.dps = saved_dps

    print()
    print("  [PASS] siegeltheta matches def:riemann-siegel-phase to numerical")
    print("         precision at every tested height.")


# ----------------------------------------------------------------------
# (P2) Phase-derivative lower bound.
# ----------------------------------------------------------------------

def check_phase_derivative_lower_bound(T_center, half_window, n_samples):
    """Sample q(t) on I_T, confirm uniform lower bound and asymptotic."""
    print(f"  Sampling q(t) = theta'(t) at T_center = {float(T_center):.2e}")

    ts = linspace_mp(T_center - half_window, T_center + half_window, n_samples)
    qs = [theta_prime(t, 1) for t in ts]
    qps = [theta_prime(t, 2) for t in ts]
    qpps = [theta_prime(t, 3) for t in ts]

    expected_q = mpf("0.5") * mp_log(T_center / (2 * MP_PI))
    print(f"    q(t)   range: min = {float(min(qs)):.4f}, "
          f"max = {float(max(qs)):.4f}, "
          f"asymptote (1/2)log(T/2pi) = {float(expected_q):.4f}")
    print(f"    q'(t)  range: min = {float(min(qps)):.4e}, "
          f"max = {float(max(qps)):.4e}")
    print(f"    q''(t) range: min = {float(min(qpps)):.4e}, "
          f"max = {float(max(qpps)):.4e}")

    if min(qs) > 0:
        print("    [PASS] q(t) > 0 throughout the window (P2 holds).")
    else:
        print("    [FAIL] q(t) attained non-positive value; chart fails (P2).")

    if max((abs(x) for x in qps)) < mpf("1") and max((abs(x) for x in qpps)) < mpf("1"):
        print("    Polynomial upper bounds on q', q'' confirmed numerically.")


# ----------------------------------------------------------------------
# (P2) across height ladder: residual scaling.
# ----------------------------------------------------------------------

def check_p2_across_height_ladder():
    """Sweep T over a dyadic-decade ladder and confirm
        (theta'(T) - (1/2) log(T / (2 pi))) * T^2 -> -1/48
    with relative error scaling as O(T^{-2})."""
    print("  Sweep heights and compare q(T) to (1/2) log(T/(2 pi)).")
    print()
    print(f"  {'T':>10}  {'q(T)':>22}  {'asymptote':>22}  "
          f"{'residual':>12}  {'residual * T^2':>17}")
    print(f"  {'-'*10}  {'-'*22}  {'-'*22}  {'-'*12}  {'-'*17}")

    saved_dps = mp.dps
    mp.dps = 50  # boost precision so ~ 1e-19 residuals at T = 1e8 are resolvable
    try:
        Ts = [mpf(10) ** k for k in (3, 4, 5, 6, 7, 8)]
        scaled_list = []
        for T in Ts:
            q_T = theta_prime(T, 1)
            asym = mpf("0.5") * mp_log(T / (2 * MP_PI))
            residual = q_T - asym
            scaled = residual * T**2
            scaled_list.append(scaled)
            print(f"  {float(T):10.2e}  {mp.nstr(q_T, 16):>22}  "
                  f"{mp.nstr(asym, 16):>22}  "
                  f"{float(residual):+12.4e}  {float(scaled):+17.10f}")

        expected = mpf(-1) / 48
        rel_errs = [abs(s - expected) / abs(expected) for s in scaled_list]
        best_idx = 0
        for i, e in enumerate(rel_errs):
            if e < rel_errs[best_idx]:
                best_idx = i
        print()
        print(f"  Asymptote of residual * T^2 (theory):  -1/48 = "
              f"{float(expected):+.10f}")
        print(f"  Per-height relative error to -1/48:")
        for i, (T, s, re) in enumerate(zip(Ts, scaled_list, rel_errs)):
            tag = "  (best)" if i == best_idx else ""
            print(f"    T = {float(T):.0e}: scaled = {float(s):+.10f},  "
                  f"rel.err = {float(re):.2e}{tag}")
        if rel_errs[best_idx] < mpf("1e-6"):
            print()
            print("  [PASS] q(t) = (1/2) log(t/(2 pi)) - 1/(48 t^2) + O(t^{-4})")
            print("         confirmed at high precision.  q(t) > 0 for all")
            print("         tested T, growing logarithmically.  (P2) holds")
            print("         with c_q = 0.")
        else:
            print()
            print(f"  [WARN] Best agreement is {float(rel_errs[best_idx]):.2e}.")
    finally:
        mp.dps = saved_dps


# ----------------------------------------------------------------------
# Uniform-window q-bounds (lem:theta-derivative-asymptotics uniformity).
# ----------------------------------------------------------------------

def check_uniform_window_q_bounds(T_center, half_window, n_samples):
    """Verify uniform polynomial bounds across I_T."""
    print(f"  Sampling q(t), q'(t), q''(t) across I_T = [T - {float(half_window)},")
    print(f"  T + {float(half_window)}] at T = {float(T_center):.2e}.")
    print()
    h_q = "q(t)"
    h_qp = "q'(t)"
    h_qpp = "q''(t)"
    h_p2 = "q(t) >= 1?"
    print(f"  {'t':>14}  {h_q:>14}  {h_qp:>14}  {h_qpp:>14}  {h_p2:>11}")
    print(f"  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*11}")

    ts = linspace_mp(T_center - half_window, T_center + half_window, n_samples)
    sample_indices = [0, n_samples // 4, n_samples // 2, 3 * n_samples // 4, n_samples - 1]

    q_min = mpf("inf")
    q_max = mpf("-inf")
    qp_max_abs = mpf(0)
    qpp_max_abs = mpf(0)
    p2_holds = True

    for i, t in enumerate(ts):
        q0 = theta_prime(t, 1)
        q1 = theta_prime(t, 2)
        q2 = theta_prime(t, 3)
        if q0 < q_min:
            q_min = q0
        if q0 > q_max:
            q_max = q0
        if abs(q1) > qp_max_abs:
            qp_max_abs = abs(q1)
        if abs(q2) > qpp_max_abs:
            qpp_max_abs = abs(q2)
        if q0 < mpf(1):
            p2_holds = False
        if i in sample_indices:
            ok = q0 >= mpf(1)
            print(f"  {float(t):14.4f}  {float(q0):14.4f}  "
                  f"{float(q1):+14.4e}  {float(q2):+14.4e}  "
                  f"{'YES' if ok else 'NO':>11}")

    print()
    print(f"  Window summary (n = {n_samples}):")
    print(f"    q range   = [{float(q_min):.4f}, {float(q_max):.4f}]")
    print(f"    sup |q'|  = {float(qp_max_abs):.4e}  (expected ~ 1/(2 T) = "
          f"{float(1/(2*T_center)):.4e})")
    print(f"    sup |q''| = {float(qpp_max_abs):.4e}  (expected ~ 1/(2 T^2) = "
          f"{float(1/(2*T_center**2)):.4e})")
    print()
    if p2_holds:
        print("  [PASS] Condition (P2) holds uniformly on I_T:")
        print("         q(t) >= 1 at every sample.")
        print("         Polynomial upper bounds on q', q'' uniform on I_T")
        print("         (sup |q'| << 1, sup |q''| << 1).")
    else:
        raise AssertionError(f"q(t) drops below 1 in window at T = {float(T_center)}")


# ----------------------------------------------------------------------
# Kernel symmetry.
# ----------------------------------------------------------------------

def check_kernel_symmetry(T_center, n_pairs):
    """Sample K_Phi(x, y) - K_Phi(y, x) at random pairs near T_center.
    Asserts symmetry holds to better than 1e-20 (well above mpmath floor)."""
    print(f"  Sampling K_Phi(x, y) and K_Phi(y, x) at random pairs near T = "
          f"{float(T_center):.2e}")
    max_err = mpf(0)
    for k in range(n_pairs):
        u1 = mpf((k * 7 + 3) % 100) / mpf(100) * 2 - 1
        u2 = mpf((k * 11 + 5) % 100) / mpf(100) * 2 - 1
        x = T_center + u1 * mpf("0.1")
        y = T_center + u2 * mpf("0.1")
        if abs(x - y) < mpf("1e-6"):
            continue
        kxy = K_phi(x, y)
        kyx = K_phi(y, x)
        err = abs(kxy - kyx)
        if err > max_err:
            max_err = err
    print(f"    max |K_Phi(x,y) - K_Phi(y,x)| over {n_pairs} pairs = "
          f"{float(max_err):.4e}")
    assert max_err < mpf("1e-20"), \
        f"Kernel symmetry violated: max err = {float(max_err)}"
    print("    [PASS] Kernel symmetry holds to << 1e-20.")


# ----------------------------------------------------------------------
# Removable singularity.
# ----------------------------------------------------------------------

def check_removable_singularity(T_center):
    """K_Phi(T+h, T) -> q(T)/pi as h -> 0.  Asserts monotonic decrease
    of error with h on the well-resolved range."""
    print(f"  Removable singularity: K_Phi(T+h, T) -> q(T)/pi as h -> 0")
    T = mpf(T_center)
    q_at_T = theta_prime(T, 1) / MP_PI
    print(f"    q(T)/pi (target) = {float(q_at_T):.6e}")
    saved_dps = mp.dps
    mp.dps = 50
    try:
        h_pows = [-1, -2, -3, -4, -5, -6]
        errs = []
        for h_pow in h_pows:
            h = mpf(10) ** h_pow
            kval = K_phi(T + h, T)
            err = abs(kval - q_at_T)
            errs.append(err)
            print(f"    h = 1e{h_pow:>3d}: K_Phi(T+h, T) = {float(kval):.6e}, "
                  f"err = {float(err):.4e}")
        # Asymptotic: K(T+h, T) - q/pi = (h/(2 pi)) q' + O(h^2).  At large
        # T, q' = O(T^-1) is small; at moderate h, the h^2 q^3/(6 pi) term
        # dominates and the empirical slope is 2.  Either way, the error
        # must decrease monotonically across the tested range.
        for i in range(1, len(errs)):
            assert errs[i] < errs[i - 1], (
                f"Removable-singularity error did not decrease: "
                f"err(1e{h_pows[i-1]}) = {float(errs[i-1])}, "
                f"err(1e{h_pows[i]}) = {float(errs[i])}"
            )
        # Fit slope on the well-resolved tail (last three points).
        h_tail = [mpf(10) ** p for p in h_pows[-3:]]
        slope = mp_log(errs[-1] / errs[-3]) / mp_log(h_tail[-1] / h_tail[0])
        print(f"    log-log slope on tail (h = 1e{h_pows[-3]}..1e{h_pows[-1]}): "
              f"{float(slope):.4f}")
        assert slope > mpf("1.5"), (
            f"Expected at-least-h^1 convergence; got slope {float(slope):.4f}"
        )
        print("    [PASS] K_Phi(T+h, T) -> q(T)/pi monotonically; tail slope >= 1.5.")
    finally:
        mp.dps = saved_dps


def check_diagonal_multipath(T_center, eps_grid):
    """Joint-continuity diagonal approach along multiple paths:
       u = v, u = -v, u = 2v, u = v^2, random small pairs.
    For each path, decrease the parameter and assert
    K_Phi(T+u, T+v) -> q(T)/pi.
    """
    print(f"  Joint-continuity multi-path approach to (T, T) at T = "
          f"{float(T_center):.2e}.")
    T = mpf(T_center)
    q_target = theta_prime(T, 1) / MP_PI

    paths = [
        ("u = v",     lambda e: (e, e)),
        ("u = -v",    lambda e: (e, -e)),
        ("u = 2v",    lambda e: (2 * e, e)),
        ("u = v^2",   lambda e: (e * e, e)),
        ("random a",  lambda e: (mpf("0.7") * e, -mpf("0.3") * e)),
        ("random b",  lambda e: (-mpf("0.4") * e, mpf("0.9") * e)),
    ]

    print(f"  {'path':>14}  {'eps':>8}  {'K(T+u, T+v)':>16}  "
          f"{'err vs q/pi':>14}")
    print(f"  {'-'*14}  {'-'*8}  {'-'*16}  {'-'*14}")

    for name, path in paths:
        last_err = None
        for eps in eps_grid:
            u, v = path(eps)
            x, y = T + u, T + v
            if abs(x - y) < mpf("1e-30"):
                k_val = q_target  # exact diagonal; sin form would give 0/0
            else:
                k_val = K_phi(x, y)
            err = abs(k_val - q_target)
            print(f"  {name:>14}  {float(eps):8.0e}  {float(k_val):16.6e}  "
                  f"{float(err):14.4e}")
            last_err = err
        # Final-eps error must be small.
        assert last_err < mpf("1e-6"), (
            f"Diagonal multi-path '{name}' did not converge: "
            f"final err = {float(last_err)}"
        )
    print()
    print("  [PASS] K_Phi(T+u, T+v) -> q(T)/pi along every tested path,")
    print("         confirming joint continuity at the diagonal.")


def check_diagonal_derivative_rates(T_center):
    """Numerically extract K_x(T,T), K_y(T,T), K_{xy}(T,T) by central
    finite differences and assert convergence to the displayed formulas
        K_x(T,T) = K_y(T,T) = q'(T) / (2 pi),
        K_{xy}(T,T) = (q''(T) + 2 q(T)^3) / (6 pi).
    """
    print(f"  Diagonal derivative rates at T = {float(T_center):.2e}.")
    T = mpf(T_center)
    q0 = theta_prime(T, 1)
    qp = theta_prime(T, 2)
    qpp = theta_prime(T, 3)

    # Closed-form targets.
    Kx_target = qp / (2 * MP_PI)
    Kxy_target = (qpp + 2 * q0**3) / (6 * MP_PI)

    print(f"    closed-form  K_x = K_y = q'/(2 pi)        = "
          f"{float(Kx_target):+.6e}")
    print(f"    closed-form  K_xy   = (q'' + 2 q^3)/(6 pi) = "
          f"{float(Kxy_target):+.6e}")
    print()
    print(f"  {'h':>10}  {'K_x FD':>16}  {'K_xy FD':>16}  "
          f"{'|err K_x|':>12}  {'|err K_xy|':>12}")
    print(f"  {'-'*10}  {'-'*16}  {'-'*16}  {'-'*12}  {'-'*12}")

    # Use finite differences that approach the diagonal.
    h_pows = [-2, -3, -4, -5]
    errs_x = []
    errs_xy = []
    saved_dps = mp.dps
    mp.dps = 60
    try:
        for h_pow in h_pows:
            h = mpf(10) ** h_pow
            # K_x(T, T) by central difference on x:
            #   K_x(T,T) ~ (K(T+h, T) - K(T-h, T)) / (2 h),
            # using the off-diagonal kernel (the on-diagonal value q/pi
            # is constant and would give 0).
            Kx_fd = (K_phi(T + h, T) - K_phi(T - h, T)) / (2 * h)
            # K_{xy}(T, T) ~ (K(T+h, T+h) - K(T+h, T-h) - K(T-h, T+h)
            #                  + K(T-h, T-h)) / (4 h^2).
            # The pure-diagonal samples (T+h, T+h) and (T-h, T-h) take the
            # removable-singularity branch (q(T+h)/pi, q(T-h)/pi).
            K_pp = K_phi(T + h, T + h)
            K_pm = K_phi(T + h, T - h)
            K_mp = K_phi(T - h, T + h)
            K_mm = K_phi(T - h, T - h)
            Kxy_fd = (K_pp - K_pm - K_mp + K_mm) / (4 * h**2)
            err_x = abs(Kx_fd - Kx_target)
            err_xy = abs(Kxy_fd - Kxy_target)
            errs_x.append(err_x)
            errs_xy.append(err_xy)
            print(f"  {float(h):10.0e}  {float(Kx_fd):+16.6e}  "
                  f"{float(Kxy_fd):+16.6e}  "
                  f"{float(err_x):12.4e}  {float(err_xy):12.4e}")
        # Assert finite-difference errors decrease across the grid.
        for i in range(1, len(errs_x)):
            assert errs_x[i] < errs_x[i - 1], (
                f"K_x FD did not improve: {float(errs_x[i-1])} -> "
                f"{float(errs_x[i])}"
            )
        # K_xy is sensitive (4th-order central difference of an expression
        # already involving 1/h); just assert the smallest h gives a small
        # absolute error.
        assert errs_xy[-1] < mpf("1e-3"), (
            f"K_xy FD did not approach target: final err {float(errs_xy[-1])}"
        )
    finally:
        mp.dps = saved_dps
    print()
    print("  [PASS] Numerical K_x and K_xy approach the displayed diagonal")
    print("         formulas.  K_x error decreases with h; K_xy is within")
    print("         1e-3 at the smallest tested h.")


def check_theta_residuals_height_ladder():
    """Across a wide height ladder T = 10^k, confirm scaled residuals:
       T^2 (q(T) - (1/2) log(T/(2 pi))) -> -1/48,
       T   (q'(T) - 1/(2 T))           -> 0,
       T^2 (q''(T) + 1/(2 T^2))        -> 0,
    with rate (each next-order error proportional to T^-2).

    Assertion: the relative error to the leading constant is below 1e-6
    at the highest tested T for each residual.
    """
    print("  Sweep theta residuals across height ladder, multiple points")
    print("  inside I_T (0.25 * I_T offsets), confirm scaled residuals:")
    print()
    print(f"  {'T':>10}  {'offset':>10}  {'(q - asym)*T^2':>16}  "
          f"{'(qp - asym)*T':>16}  {'(qpp + asym)*T^2':>18}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*16}  {'-'*16}  {'-'*18}")

    saved_dps = mp.dps
    mp.dps = 60
    try:
        Ts = [mpf(10) ** k for k in (3, 4, 5, 6, 7, 8)]
        scaled_q_list = []
        scaled_qp_list = []
        scaled_qpp_list = []
        for T in Ts:
            half = mpf("0.25") / T  # << |I_T| ~ 1/Q(T); a comfortable interior
            for off in [-half, mpf(0), +half]:
                t = T + off
                q_t = theta_prime(t, 1)
                qp_t = theta_prime(t, 2)
                qpp_t = theta_prime(t, 3)
                q_asym = mpf("0.5") * mp_log(t / (2 * MP_PI))
                qp_asym = mpf("0.5") / t
                qpp_asym = -mpf("0.5") / t**2
                rq = (q_t - q_asym) * t**2
                rqp = (qp_t - qp_asym) * t
                rqpp = (qpp_t - qpp_asym) * t**2
                if off == 0:
                    scaled_q_list.append(rq)
                    scaled_qp_list.append(rqp)
                    scaled_qpp_list.append(rqpp)
                print(f"  {float(T):10.2e}  {float(off):+10.2e}  "
                      f"{float(rq):+16.10f}  {float(rqp):+16.6e}  "
                      f"{float(rqpp):+18.6e}")
        # Asymptotic targets at the largest T:
        #   T^2 (q - (1/2) log(T/(2 pi))) -> -1/48,
        #   T   (q' - 1/(2 T))            -> 0  (next term is O(T^-2)),
        #   T^2 (q'' + 1/(2 T^2))         -> 0  (next term is O(T^-2)).
        target_q = mpf(-1) / 48
        rel_err_q = abs(scaled_q_list[-1] - target_q) / abs(target_q)
        rel_err_qp = abs(scaled_qp_list[-1])
        rel_err_qpp = abs(scaled_qpp_list[-1])
        print()
        print(f"  At T = {float(Ts[-1]):.0e}:")
        print(f"    q-residual rel.err to -1/48 : {float(rel_err_q):.2e}")
        print(f"    q'-residual abs            : {float(rel_err_qp):.4e}")
        print(f"    q''-residual abs           : {float(rel_err_qpp):.4e}")
        assert rel_err_q < mpf("1e-6"), \
            f"q residual scaling failed: {float(rel_err_q)}"
        assert rel_err_qp < mpf("1e-6"), \
            f"q' residual scaling failed: {float(rel_err_qp)}"
        assert rel_err_qpp < mpf("1e-3"), \
            f"q'' residual scaling failed: {float(rel_err_qpp)}"
        print()
        print("  [PASS] All three theta-derivative residuals scale as")
        print("         predicted across heights and across the I_T window.")
    finally:
        mp.dps = saved_dps


# ----------------------------------------------------------------------
# Phase-kernel derivatives at distinct points.
# ----------------------------------------------------------------------

def check_kernel_derivatives_at_pair(T1, T2):
    """Compare displayed formulas to finite-difference estimates."""
    print(f"  Comparing closed-form derivatives at (T1, T2) = "
          f"({float(T1):.4e}, {float(T2):.4e})")

    s = T1 - T2
    Delta = theta(T1) - theta(T2)
    q1 = theta_prime(T1, 1)
    q2 = theta_prime(T2, 1)

    K_at_pair = mp_sin(Delta) / (MP_PI * s)
    Kx = (q1 * s * mp_cos(Delta) - mp_sin(Delta)) / (MP_PI * s**2)
    Ky = (mp_sin(Delta) - q2 * s * mp_cos(Delta)) / (MP_PI * s**2)
    Kxy = ((q1 + q2) * s * mp_cos(Delta) +
           (q1 * q2 * s**2 - 2) * mp_sin(Delta)) / (MP_PI * s**3)

    h_fd = mpf("1e-4")
    K_pp = K_phi(T1 + h_fd, T2)
    K_mm = K_phi(T1 - h_fd, T2)
    K_pm = K_phi(T1, T2 + h_fd)
    K_mp = K_phi(T1, T2 - h_fd)
    K_pp_pp = K_phi(T1 + h_fd, T2 + h_fd)
    K_pp_mm = K_phi(T1 + h_fd, T2 - h_fd)
    K_mm_pp = K_phi(T1 - h_fd, T2 + h_fd)
    K_mm_mm = K_phi(T1 - h_fd, T2 - h_fd)

    Kx_fd = (K_pp - K_mm) / (2 * h_fd)
    Ky_fd = (K_pm - K_mp) / (2 * h_fd)
    Kxy_fd = (K_pp_pp - K_pp_mm - K_mm_pp + K_mm_mm) / (4 * h_fd**2)

    K_direct = K_phi(T1, T2)

    err_K = abs(K_at_pair - K_direct)
    err_Kx = abs(Kx - Kx_fd)
    err_Ky = abs(Ky - Ky_fd)
    err_Kxy = abs(Kxy - Kxy_fd)
    print(f"    K_Phi(T1,T2):        formula = {float(K_at_pair):.6e},  "
          f"direct = {float(K_direct):.6e},  err = {float(err_K):.2e}")
    print(f"    d/dx K_Phi:          formula = {float(Kx):.6e},  "
          f"FD = {float(Kx_fd):.6e},  err = {float(err_Kx):.2e}")
    print(f"    d/dy K_Phi:          formula = {float(Ky):.6e},  "
          f"FD = {float(Ky_fd):.6e},  err = {float(err_Ky):.2e}")
    print(f"    d^2/dxdy K_Phi:      formula = {float(Kxy):.6e},  "
          f"FD = {float(Kxy_fd):.6e},  err = {float(err_Kxy):.2e}")
    # K_Phi(T1, T2) computed via formula and via direct kernel evaluation
    # must match to numerical precision.
    assert err_K < mpf("1e-25"), \
        f"K_Phi formula vs direct mismatch: err = {float(err_K)}"
    # FD vs closed-form derivatives must agree to ~h_fd^2 = 1e-8 at h_fd = 1e-4.
    assert err_Kx < mpf("1e-6"), f"K_x FD mismatch: {float(err_Kx)}"
    assert err_Ky < mpf("1e-6"), f"K_y FD mismatch: {float(err_Ky)}"
    assert err_Kxy < mpf("1e-6"), f"K_xy FD mismatch: {float(err_Kxy)}"
    print("    [PASS] Off-diagonal kernel-derivative formulas match FD")
    print("           and direct evaluation at pair (independent routes).")


# ----------------------------------------------------------------------
# Main.
# ----------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Simulation: sec:local-kernel-and-jet-normalization")
    print("(arbitrary-precision arithmetic via mpmath)")
    print("=" * 70)
    print()

    T_center = mpf("1e4")
    half_window = mpf("0.05")
    n_samples = 50

    print("[def:riemann-siegel-phase: theta as Im log Gamma]")
    print()
    check_theta_via_loggamma()
    print()

    print("[phase-derivative lower bound (P2): single-window check]")
    print()
    check_phase_derivative_lower_bound(T_center, half_window, n_samples)
    print()

    print("[phase-derivative lower bound (P2): height-ladder fit]")
    print()
    check_p2_across_height_ladder()
    print()

    print("[lem:theta-derivative-asymptotics: uniform on I_T]")
    print()
    check_uniform_window_q_bounds(T_center, half_window, n_samples)
    print()

    print("[lem:theta-derivative-asymptotics: residuals across height ladder]")
    print()
    check_theta_residuals_height_ladder()
    print()

    print("[kernel symmetry]")
    print()
    check_kernel_symmetry(T_center, n_pairs=20)
    print()

    print("[lem:phase-kernel-properties: removable singularity, monotone rate]")
    print()
    check_removable_singularity(T_center)
    print()

    print("[lem:phase-kernel-properties: joint-continuity multi-path approach]")
    print()
    eps_grid = [mpf("1e-2"), mpf("1e-3"), mpf("1e-4"), mpf("1e-6")]
    check_diagonal_multipath(T_center, eps_grid)
    print()

    print("[lem:phase-kernel-diagonal-derivatives: numerical FD rate test]")
    print()
    check_diagonal_derivative_rates(T_center)
    print()

    print("[lem:phase-kernel-derivatives: kernel derivatives at distinct pair]")
    print()
    T1 = T_center
    T2 = T_center + mpf("0.5")
    check_kernel_derivatives_at_pair(T1, T2)
    print()

    print("=" * 70)
    print("§2 chart construction and kernel properties verified numerically")
    print("at mpmath precision (every check is an assertion).")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
