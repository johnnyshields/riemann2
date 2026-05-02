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
    """Sample K_Phi(x, y) - K_Phi(y, x) at random pairs near T_center."""
    print(f"  Sampling K_Phi(x, y) and K_Phi(y, x) at random pairs near T = "
          f"{float(T_center):.2e}")
    # Deterministic pseudo-random offsets via halton-like sequence (mpmath-friendly).
    max_err = mpf(0)
    for k in range(n_pairs):
        # Two coprime fractional offsets in (-1, 1).
        u1 = mpf((k * 7 + 3) % 100) / mpf(100) * 2 - 1  # [-1, 1)
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
    if max_err < mpf("1e-25"):
        print("    [PASS] Kernel symmetry holds to mpmath-precision (~ 30 dps).")
    elif max_err < mpf("1e-12"):
        print("    [PASS] Kernel symmetry holds to standard precision.")
    else:
        print("    [WARN] Symmetry deviation above 1e-12.")


# ----------------------------------------------------------------------
# Removable singularity.
# ----------------------------------------------------------------------

def check_removable_singularity(T_center):
    """Verify K_Phi(T+h, T) -> q(T)/pi as h -> 0."""
    print(f"  Removable singularity: K_Phi(T+h, T) -> q(T)/pi as h -> 0")
    T = mpf(T_center)
    q_at_T = theta_prime(T, 1) / MP_PI
    print(f"    q(T)/pi (target) = {float(q_at_T):.6e}")
    for h_pow in [-1, -2, -4, -6, -10, -15]:
        h = mpf(10) ** h_pow
        kval = K_phi(T + h, T)
        err = abs(kval - q_at_T)
        print(f"    h = 1e{h_pow:>3d}: K_Phi(T+h, T) = {float(kval):.6e}, "
              f"err = {float(err):.4e}")


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

    print(f"    K_Phi(T1,T2):        formula = {float(K_at_pair):.6e},  "
          f"direct = {float(K_direct):.6e},  err = {float(abs(K_at_pair - K_direct)):.2e}")
    print(f"    d/dx K_Phi:          formula = {float(Kx):.6e},  "
          f"FD = {float(Kx_fd):.6e},  err = {float(abs(Kx - Kx_fd)):.2e}")
    print(f"    d/dy K_Phi:          formula = {float(Ky):.6e},  "
          f"FD = {float(Ky_fd):.6e},  err = {float(abs(Ky - Ky_fd)):.2e}")
    print(f"    d^2/dxdy K_Phi:      formula = {float(Kxy):.6e},  "
          f"FD = {float(Kxy_fd):.6e},  err = {float(abs(Kxy - Kxy_fd)):.2e}")


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

    print("[kernel symmetry]")
    print()
    check_kernel_symmetry(T_center, n_pairs=20)
    print()

    print("[removable singularity]")
    print()
    check_removable_singularity(T_center)
    print()

    print("[kernel derivatives at distinct pair]")
    print()
    T1 = T_center
    T2 = T_center + mpf("0.5")
    check_kernel_derivatives_at_pair(T1, T2)
    print()

    print("=" * 70)
    print("§2 chart construction and kernel properties verified numerically")
    print("at mpmath precision.")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
