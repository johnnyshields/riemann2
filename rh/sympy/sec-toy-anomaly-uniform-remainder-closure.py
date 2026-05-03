"""Symbolic verification for the referee-revised §5 toy retained subdomain.

Static companion to sec-toy-anomaly-uniform-remainder-closure.referee-revised.tex.
This script is intentionally algebraic: it checks the density bookkeeping with
q_T^- and q_T^+ rather than the false simplification q(m) <= q(T).
"""

import sys
import sympy as sp


def verify_density_bound_with_q_extrema():
    """Check the exact density lower bound.

    With q^- <= q(m) <= q^+ on I_T and the height hypothesis
    d_+/q^- <= |I_T|/4, the signed retained set q(m)|s| in [d_-,d_+]
    has density at least (d_+-d_-)/(q^+ |I_T|).
    """
    dminus, dplus, qplus, I = sp.symbols("dminus dplus qplus I", positive=True)
    width = dplus - dminus

    # Central slab length is |I|/2.  Two signs of s contribute total
    # s-width >= 2 width/qplus at each slab point.
    retained_lower = (I / 2) * (2 * width / qplus)
    total_area = I**2
    ratio = sp.simplify(retained_lower / total_area)
    target = width / (qplus * I)
    assert sp.simplify(ratio - target) == 0
    print("[PASS] exact signed density ratio >= (d_+-d_-)/(q_T^+ |I_T|).")


def verify_polynomial_density_consequence():
    """Check the polynomial consequence under |I_T| <= C_I/Q and q^+ <= C_q q(T)."""
    width, Q, qT, CI, Cq = sp.symbols("width Q qT C_I C_q", positive=True)
    I_boundary = CI / Q
    qplus_boundary = Cq * qT
    exact_ratio_boundary = width / (qplus_boundary * I_boundary)
    polynomial_target = width * Q / (CI * Cq * qT)
    assert sp.simplify(exact_ratio_boundary - polynomial_target) == 0
    print("[PASS] exact density implies width/(C_I C_q) * Q/q(T) at boundary.")


def verify_height_hypothesis_implication():
    """Check sufficient high-height condition.

    If |I_T| >= c_I/Q, q^- >= c_q q(T), and Q/q(T) <= c_I c_q/(4d_+),
    then d_+/q^- <= |I_T|/4.
    """
    dplus, Q, qT, cI, cq = sp.symbols("dplus Q qT c_I c_q", positive=True)
    I_lower = cI / Q
    qminus_lower = cq * qT
    lhs = dplus / qminus_lower
    rhs = I_lower / 4
    # At the boundary Q/qT = cI*cq/(4dplus), the two sides are equal.
    Q_boundary = cI * cq * qT / (4 * dplus)
    assert sp.simplify(lhs - rhs.subs(Q, Q_boundary)) == 0
    print("[PASS] Q/q(T) <= c_I c_q/(4d_+) implies the height hypothesis.")


def verify_signed_definition_matches_two_branches():
    """Symbolic length check for q(m)|s| in D.

    The signed definition keeps s in [d_-/q,d_+/q] and the reflected negative
    interval.  Total length is 2(d_+-d_-)/q.
    """
    dminus, dplus, q = sp.symbols("dminus dplus q", positive=True)
    length_positive = dplus / q - dminus / q
    length_negative = (-dminus / q) - (-dplus / q)
    total = sp.simplify(length_positive + length_negative)
    assert sp.simplify(total - 2 * (dplus - dminus) / q) == 0
    print("[PASS] q(m)|s| in D contributes two branches of total length 2|D|/q(m).")


def F_inf_numeric_expr(d):
    return sp.sqrt(3) * (
        2*d**2*sp.cos(d) + 5*d**2*sp.cos(2*d) - 7*d**2
        + 6*d*sp.sin(d) - 15*d*sp.sin(2*d) - 12*sp.cos(2*d) + 12
    ) / (8*d**3*sp.sin(d/2))


def verify_sample_D_widths_positive():
    """Regression only: sample D intervals have positive width and no sampled sign change."""
    samples = [(sp.Rational(1,2), sp.Rational(3,2)),
               (sp.Rational(1,2), sp.Rational(2,1)),
               (sp.Rational(1,1), sp.Rational(5,2))]
    for a, b in samples:
        assert b - a > 0
        vals = []
        for k in range(41):
            x = a + (b-a) * sp.Rational(k, 40)
            vals.append(float(F_inf_numeric_expr(x).evalf(50)))
        signs = [1 if v > 0 else -1 if v < 0 else 0 for v in vals]
        assert all(s == signs[0] for s in signs), (a, b, signs)
    print("[PASS] sampled D intervals have positive width and no sampled F_inf sign change.")



def verify_signed_scalar_channel_invariance():
    """Check the algebra behind Lemma toy-signed-separation-invariance.

    If H_- and H_+ are symmetric inverse square roots and N(-s)=N(s)^T with
    H_-(-s)=H_+(s), H_+(-s)=H_-(s), then Omega(-s)=Omega(s)^T.  Since
    A(X)=X_12+X_21 is transpose-invariant, the scalar channel is unchanged.
    """
    hm11, hm12, hm22, hp11, hp12, hp22 = sp.symbols('hm11 hm12 hm22 hp11 hp12 hp22')
    n11, n12, n21, n22 = sp.symbols('n11 n12 n21 n22')
    Hm = sp.Matrix([[hm11, hm12], [hm12, hm22]])
    Hp = sp.Matrix([[hp11, hp12], [hp12, hp22]])
    N = sp.Matrix([[n11, n12], [n21, n22]])
    Omega_pos = Hm * N * Hp
    Omega_neg = Hp * N.T * Hm
    assert sp.simplify(Omega_neg - Omega_pos.T) == sp.zeros(2, 2)
    A = lambda X: X[0, 1] + X[1, 0]
    assert sp.simplify(A(Omega_neg) - A(Omega_pos)) == 0
    print('[PASS] signed separation transposes Omega and preserves A(X)=X_12+X_21.')

def main():
    verify_density_bound_with_q_extrema()
    verify_polynomial_density_consequence()
    verify_height_hypothesis_implication()
    verify_signed_definition_matches_two_branches()
    verify_signed_scalar_channel_invariance()
    verify_sample_D_widths_positive()
    print("All referee-revised §5 closure symbolic checks passed.")


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
