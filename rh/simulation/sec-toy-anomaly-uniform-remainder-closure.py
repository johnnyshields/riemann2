"""Numerical regression for the referee-revised §5 toy retained subdomain.

Checks the signed retained-domain density using q_T^+ and q_T^- rather than
assuming q(m) <= q(T).  This is regression evidence only; the proof is the
measure estimate in the LaTeX patch.
"""

import sys
from mpmath import mp, mpf, fabs, log as mp_log, pi as MP_PI, quad
from mpmath import sin as mp_sin, cos as mp_cos, sqrt as mp_sqrt

mp.dps = 30


def q_at(t):
    t = mpf(t)
    return mp_log(t / (2 * MP_PI)) / 2 - 1 / (48 * t**2)


def q_bounds(T, I_half):
    # theta q is increasing for the sampled high-height windows.
    return q_at(T - I_half), q_at(T + I_half)


def F_inf(d):
    d = mpf(d)
    num = (2*d**2*mp_cos(d) + 5*d**2*mp_cos(2*d) - 7*d**2
           + 6*d*mp_sin(d) - 15*d*mp_sin(2*d) - 12*mp_cos(2*d) + 12)
    return mp_sqrt(3) * num / (8*d**3*mp_sin(d/2))


def measure_D_T(I_half):
    return (2 * I_half)**2


def measure_D_T_toy(T, I_half, dminus, dplus):
    T = mpf(T); I_half = mpf(I_half)
    dminus = mpf(dminus); dplus = mpf(dplus)

    def integrand(m):
        m = mpf(m)
        smax = 2 * (I_half - fabs(m - T))
        if smax <= 0:
            return mpf(0)
        q_m = q_at(m)
        slo = dminus / q_m
        shi = dplus / q_m
        single = max(mpf(0), min(shi, smax) - min(slo, smax))
        return 2 * single  # signed definition q(m)|s| in D

    return quad(integrand, [T - I_half, T + I_half])


def check_density_at_heights():
    cases = [
        (mpf('1e6'),  mpf('0.5'), (mpf('0.4'), mpf('1.5'))),
        (mpf('1e9'),  mpf('0.7'), (mpf('0.4'), mpf('2.0'))),
        (mpf('1e12'), mpf('0.9'), (mpf('0.4'), mpf('2.5'))),
    ]
    for T, Q, D in cases:
        dminus, dplus = D
        I_half = 1 / (2 * Q)
        qmin, qmax = q_bounds(T, I_half)
        assert dplus / qmin <= (2 * I_half) / 4
        empirical = measure_D_T_toy(T, I_half, dminus, dplus) / measure_D_T(I_half)
        exact_lower = (dplus - dminus) / (qmax * (2 * I_half))
        assert empirical >= exact_lower - mpf('1e-12')
        print(f'T={float(T):.1e}, Q={float(Q):.3f}: empirical={float(empirical):.4e}, exact lower={float(exact_lower):.4e}')
    print('[PASS] signed density lower bound verified on sampled heights.')


def check_density_scaling_in_Q():
    T = mpf('1e9')
    dminus, dplus = mpf('0.4'), mpf('1.5')
    qT = q_at(T)
    for Q in [qT/32, qT/16, qT/8]:
        I_half = 1 / (2 * Q)
        qmin, qmax = q_bounds(T, I_half)
        assert dplus / qmin <= (2 * I_half) / 4
        empirical = measure_D_T_toy(T, I_half, dminus, dplus) / measure_D_T(I_half)
        scaled = empirical / (Q / qT)
        lower_scaled = (dplus - dminus) * qT / qmax
        assert scaled >= lower_scaled - mpf('1e-10')
        print(f'Q={float(Q):.4f}: empirical/(Q/qT)={float(scaled):.4f}, lower={float(lower_scaled):.4f}')
    print('[PASS] density scales like Q/q(T), with q_T^+ correction.')


def check_F_inf_zero_avoidance():
    samples = [(mpf('0.5'), mpf('1.5')), (mpf('0.5'), mpf('2.0')), (mpf('1.0'), mpf('2.5'))]
    for a, b in samples:
        signs = []
        for k in range(51):
            x = a + (b-a) * k / 50
            v = F_inf(x)
            signs.append(1 if v > 0 else -1 if v < 0 else 0)
        assert all(s == signs[0] for s in signs)
        print(f'D=[{float(a):.2f},{float(b):.2f}]: no sampled sign change')
    print('[PASS] sampled D intervals avoid F_inf zeros numerically.')


def main():
    check_F_inf_zero_avoidance()
    check_density_at_heights()
    check_density_scaling_in_Q()
    print('All referee-revised §5 closure simulations passed.')


if __name__ == '__main__':
    sys.exit(main() if main() else 0)
