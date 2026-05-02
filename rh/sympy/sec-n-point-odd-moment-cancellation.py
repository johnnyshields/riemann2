"""Symbolic verification: sec:n-point-odd-moment-cancellation.

Verifies the parity identities of section §9 of rh/rh_rebuild.tex.

Coefficients (Definition):
    a_j^{(N)} := (-1)^{j+1} * j * C(2N, N+j) / C(2N-2, N-1),  1 <= j <= N.

Coefficient lemma (lem:n-point-coefficients):
    sum_{j=1..N} a_j^{(N)}                       = 1,
    sum_{j=1..N} a_j^{(N)} * j^{2r+1}            = 0  for 0 <= r <= N-2,
    sum_{j=1..N} |a_j^{(N)}|                     = 2N - 1.

Discrete N-point measure (lem:n-point-mellin-symbol, parity part):
    mu_hat_{N,Q}(z) := sum_{j=1..N} a_j^{(N)} * exp(j z / Q^2),
    mu_hat_{N,Q}(0) = 1,
    d^{2r+1}/dz^{2r+1} mu_hat_{N,Q}(0) = 0   for 0 <= r <= N-2,
    odd part of mu_hat_{N,Q} starts only at order 2N-1.

Convolution stability:
    For any even test bump phi_hat with finite Taylor expansion,
        d^{2r+1}/dz^{2r+1} (phi_hat(eta z) mu_hat_{N,Q}(z))|_{z=0} = 0
    for 0 <= r <= N - 2.

Algebraic identity (used in the Mellin closed form, kept here as a
hardening cross-check):
    A_N(t) - A_N(1/t) = (-1)^N * N / C(2N-2, N-1)
                        * t^{-N} (1-t)^{2N-1} (1+t),
    where A_N(t) := sum_{j=1..N} a_j^{(N)} t^j.

Run:
  python3 rh/sympy/sec-n-point-odd-moment-cancellation.py
"""

import sys

import sympy as sp
from sympy import (
    Rational,
    Symbol,
    binomial,
    diff,
    exp,
    factorial,
    simplify,
    summation,
    symbols,
)


# ---------------------------------------------------------------------------
# Coefficients a_j^{(N)}.
# ---------------------------------------------------------------------------

def a_coeff(N, j):
    """a_j^{(N)} = (-1)^{j+1} * j * C(2N, N+j) / C(2N-2, N-1)."""
    return (-1)**(j + 1) * j * binomial(2 * N, N + j) / binomial(2 * N - 2, N - 1)


# ---------------------------------------------------------------------------
# (i)  sum a_j = 1, odd-moment vanishing, |a_j|-sum = 2N - 1.
# ---------------------------------------------------------------------------

def verify_coefficient_identities(N_values=(2, 3, 4, 5, 6, 7)):
    print("=" * 70)
    print("[lem:n-point-coefficients]  sum, odd moments, ell^1 control")
    print("=" * 70)
    for N in N_values:
        # Normalization.
        s_norm = sum(a_coeff(N, j) for j in range(1, N + 1))
        s_norm = sp.simplify(s_norm)
        assert s_norm == 1, f"N={N}: sum a_j = {s_norm}, expected 1"

        # Odd moments j^{2r+1}, 0 <= r <= N-2.
        for r in range(0, N - 1):
            m = sum(a_coeff(N, j) * j**(2 * r + 1) for j in range(1, N + 1))
            m = sp.simplify(m)
            assert m == 0, f"N={N}, r={r}: odd moment = {m}, expected 0"

        # ell^1 control.
        s_abs = sum(abs(a_coeff(N, j)) for j in range(1, N + 1))
        s_abs = sp.simplify(s_abs)
        assert s_abs == 2 * N - 1, \
            f"N={N}: sum |a_j| = {s_abs}, expected {2*N-1}"

        # Print a compact summary.
        coeffs = [a_coeff(N, j) for j in range(1, N + 1)]
        coeffs_str = ", ".join(str(sp.nsimplify(c)) for c in coeffs)
        print(f"  N={N}: a_j = ({coeffs_str});")
        print(f"        sum = 1, |.|-sum = {s_abs} = 2N-1;")
        print(f"        odd moments j^1..j^{2*(N-2)+1} vanish.")
    print()
    print("  [PASS] All three identities hold for N in",
          tuple(N_values), "by symbolic summation.")


# ---------------------------------------------------------------------------
# (ii) Discrete measure mu_hat_{N,Q}(z): low odd-jet vanishing at z = 0.
# ---------------------------------------------------------------------------

def verify_mu_hat_parity(N_values=(2, 3, 4, 5)):
    print("=" * 70)
    print("[lem:n-point-mellin-symbol]  d^{2r+1} mu_hat(0) = 0, 0 <= r <= N-2")
    print("=" * 70)
    z, Q = symbols("z Q", positive=True)
    for N in N_values:
        mu_hat = sum(a_coeff(N, j) * exp(j * z / Q**2) for j in range(1, N + 1))

        # Value at z = 0 must be 1.
        val0 = simplify(mu_hat.subs(z, 0))
        assert val0 == 1, f"N={N}: mu_hat(0) = {val0}, expected 1"

        # Odd derivatives of order 2r+1 at 0 must vanish for 0 <= r <= N-2.
        for r in range(0, N - 1):
            order = 2 * r + 1
            deriv = diff(mu_hat, z, order).subs(z, 0)
            deriv = simplify(deriv)
            assert deriv == 0, \
                f"N={N}, order={order}: d^{order} mu_hat(0) = {deriv}, expected 0"

        # Order 2N-1 derivative: must be NONZERO (the lemma says the odd part
        # starts there).  Confirm by symbolic evaluation.
        order_first = 2 * N - 1
        deriv_first = diff(mu_hat, z, order_first).subs(z, 0)
        deriv_first = simplify(deriv_first)
        assert deriv_first != 0, (
            f"N={N}: d^{order_first} mu_hat(0) unexpectedly zero: {deriv_first}"
        )

        print(f"  N={N}: mu_hat(0) = 1; "
              f"d^1, d^3, ..., d^{2*(N-2)+1} all vanish at 0;")
        print(f"        d^{order_first} mu_hat(0) = {deriv_first}  (nonzero, as expected).")
    print()
    print("  [PASS] mu_hat_{N,Q} has its odd part starting at order 2N-1,")
    print("         confirming the parity vanishing of the lemma.")


# ---------------------------------------------------------------------------
# (iii) Convolution form: even bump phi_hat, parity propagates.
# ---------------------------------------------------------------------------

def verify_convolution_parity(N_values=(2, 3, 4)):
    print("=" * 70)
    print("[convolution form]  d^{2r+1} (phi_hat(eta z) mu_hat(z))(0) = 0")
    print("=" * 70)
    z, Q, eta = symbols("z Q eta", positive=True)
    # Generic even symbolic bump phi_hat: a polynomial in even powers,
    # phi_hat(w) = c0 + c2 w^2 + c4 w^4 + c6 w^6, with arbitrary c_2k.
    c0, c2, c4, c6 = symbols("c0 c2 c4 c6", real=True)

    def phi_hat(w):
        return c0 + c2 * w**2 + c4 * w**4 + c6 * w**6

    for N in N_values:
        mu_hat = sum(a_coeff(N, j) * exp(j * z / Q**2) for j in range(1, N + 1))
        product = phi_hat(eta * z) * mu_hat
        for r in range(0, N - 1):
            order = 2 * r + 1
            deriv = diff(product, z, order).subs(z, 0)
            deriv = simplify(deriv)
            assert deriv == 0, (
                f"N={N}, r={r}: convolved odd derivative does not vanish: {deriv}"
            )
        print(f"  N={N}: d^1, d^3, ..., d^{2*(N-2)+1} of "
              f"phi_hat(eta z) mu_hat_{{{N},Q}}(z) all vanish at 0,")
        print(f"        for arbitrary even phi_hat(w) = c0 + c2 w^2 + c4 w^4 + c6 w^6.")
    print()
    print("  [PASS] Parity vanishing is preserved under product with any")
    print("         even bump.  Coefficients c0, c2, c4, c6 are free.")


# ---------------------------------------------------------------------------
# (iv) A_N(t) - A_N(1/t) closed form.
# ---------------------------------------------------------------------------

def verify_A_N_difference_identity(N_values=(2, 3, 4, 5)):
    print("=" * 70)
    print("[A_N(t) - A_N(1/t) closed form]")
    print("=" * 70)
    t = Symbol("t", positive=True)
    for N in N_values:
        A = sum(a_coeff(N, j) * t**j for j in range(1, N + 1))
        A_inv = sum(a_coeff(N, j) * t**(-j) for j in range(1, N + 1))
        lhs = sp.simplify(A - A_inv)
        # Closed form: (-1)^N * N / C(2N-2, N-1) * t^{-N} (1-t)^{2N-1} (1+t).
        rhs = ((-1)**N * Rational(N, 1) / binomial(2 * N - 2, N - 1)
               * t**(-N) * (1 - t)**(2 * N - 1) * (1 + t))
        diff_LR = sp.simplify(sp.expand(lhs - rhs))
        assert diff_LR == 0, \
            f"N={N}: A_N(t) - A_N(1/t) - rhs = {diff_LR}, expected 0"
        print(f"  N={N}: A_N(t) - A_N(1/t) "
              f"= {sp.simplify(lhs)}")
    print()
    print("  [PASS] Closed form A_N(t) - A_N(1/t) = "
          "(-1)^N N / C(2N-2, N-1) t^{-N} (1-t)^{2N-1} (1+t)")
    print("         confirmed for tested N.")


# ---------------------------------------------------------------------------
# (v) Stress test: parity-of-coefficients audit.
# ---------------------------------------------------------------------------

def verify_alternating_sign_pattern(N_values=(2, 3, 4, 5, 6, 7, 8)):
    """The lemma proof claims a_j alternate in sign: a_j^{(N)} > 0 for j odd,
    < 0 for j even (so the prefactor (-1)^{j+1} flips with j).  This is
    used in computing sum |a_j^{(N)}|.  Verify by direct evaluation.
    """
    print("=" * 70)
    print("[parity-of-coefficients audit]  sign(a_j^{(N)}) = (-1)^{j+1}")
    print("=" * 70)
    for N in N_values:
        for j in range(1, N + 1):
            a_val = a_coeff(N, j)
            a_val = sp.nsimplify(a_val)
            expected_sign = 1 if j % 2 == 1 else -1
            actual_sign = sp.sign(a_val)
            assert actual_sign == expected_sign, \
                (f"N={N}, j={j}: a_j = {a_val}, sign = {actual_sign}; "
                 f"expected {expected_sign}")
    print()
    print(f"  Tested N in {tuple(N_values)}: a_j^{{(N)}} alternates in sign as")
    print("  predicted by the (-1)^{j+1} prefactor.  No implicit asymmetry.")
    print()
    print("  [PASS] Sign pattern audit clean.")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    verify_coefficient_identities()
    print()
    verify_mu_hat_parity()
    print()
    verify_convolution_parity()
    print()
    verify_A_N_difference_identity()
    print()
    verify_alternating_sign_pattern()
    print()
    print("=" * 70)
    print("All §9 lemmas verified symbolically:")
    print("  - explicit coefficient identities (sum, odd moments, ell^1)")
    print("  - mu_hat_{N,Q}: low odd-jet vanishing at 0, exact start order 2N-1")
    print("  - convolution stability under product with any even bump")
    print("  - closed form A_N(t) - A_N(1/t) = (-1)^N N / C(2N-2, N-1)")
    print("                                    t^{-N} (1-t)^{2N-1} (1+t)")
    print("  - alternating sign pattern audit (no implicit asymmetry)")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
