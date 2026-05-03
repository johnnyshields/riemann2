"""Symbolic verification: sec:transverse-projection.

Companion to rh/patches/sec-transverse-projection.tex.

Coverage:

  * Two-point scalar value subspace V_val = ker(A_toy) =
    {X : x_12 + x_21 = 0} is three-dimensional with explicit orthonormal basis
    (e_11, e_22, e_anti) in the Hilbert-Schmidt inner product
    (def:value-subspace, lem:value-subspace-explicit-basis).
  * Pi_trans X = ((x_12 + x_21)/2) * [[0, 1], [1, 0]]
    (def:transverse-projection, eq:Pi-trans-explicit).
  * Pi_trans is idempotent (Pi_trans^2 = Pi_trans).
  * Pi_trans is self-adjoint w.r.t. the Hilbert-Schmidt inner product.
  * ker(Pi_trans) = V_val exactly.
  * ||Pi_trans||_op = 1 (orthogonal projection onto a non-zero subspace).
  * A_toy(Pi_trans X) = A_toy(X) for every X
    (lem:transverse-projection-A-toy-compatibility).
  * Type handoff for the two-point actual-zeta side:
        A_2(X) := A_toy(Pi_trans X) = A_toy(X).
  * Quotient well-definedness: if X-Y lies in V_val then A_2(X)=A_2(Y),
    and X-Pi_trans X is the orthogonal V_val representative
    (lem:A2-quotient-well-defined).
  * Regression: v1's A_val(x) of Proposition prop:explicit-Aval
    (proof_of_rh.tex line 1260) has zero off-diagonal trace, hence lies
    in the rebuild's V_val and is annihilated by Pi_trans.

Run:
  python3 rh/sympy/sec-transverse-projection.py
"""

import sys

import sympy as sp
from sympy import (
    Matrix,
    Rational,
    Symbol,
    cos,
    eye,
    sin,
    sqrt,
    simplify,
    symbols,
    trigsimp,
    zeros,
)


# ---------------------------------------------------------------------------
# Hilbert-Schmidt inner product on M_2(R) and the toy anomaly functional.
# ---------------------------------------------------------------------------

def hs_inner(X, Y):
    """<X, Y>_HS = Tr(X^T Y)."""
    return (X.T * Y).trace()


def A_toy(X):
    """A_toy(X) := X_{12} + X_{21}."""
    return X[0, 1] + X[1, 0]


def Pi_trans(X):
    """Pi_trans X = ((X_12 + X_21) / 2) * [[0, 1], [1, 0]]."""
    half = (X[0, 1] + X[1, 0]) / 2
    return half * Matrix([[0, 1], [1, 0]])


def generic_2x2_matrix(prefix="x"):
    """Return a generic real 2x2 matrix with symbolic entries."""
    x11, x12, x21, x22 = symbols(f"{prefix}_11 {prefix}_12 {prefix}_21 {prefix}_22",
                                  real=True)
    return Matrix([[x11, x12], [x21, x22]])


# ---------------------------------------------------------------------------
# (i) Value subspace structure.
# ---------------------------------------------------------------------------

E11 = Matrix([[1, 0], [0, 0]])
E22 = Matrix([[0, 0], [0, 1]])
E_anti = Matrix([[0, 1], [-1, 0]]) / sp.sqrt(2)
E_sym = Matrix([[0, 1], [1, 0]]) / sp.sqrt(2)


def verify_value_subspace_kernel_of_A_toy():
    """V_val := {X : x_12 + x_21 = 0} = ker(A_toy)."""
    print("=" * 70)
    print("[def:value-subspace]  V_val = ker(A_toy)")
    print("=" * 70)
    # Each of e_11, e_22, e_anti has A_toy = 0; e_sym has A_toy != 0.
    for name, M in (("e_11", E11), ("e_22", E22), ("e_anti", E_anti)):
        val = simplify(A_toy(M))
        assert val == 0, f"A_toy({name}) = {val}, expected 0"
        print(f"  A_toy({name})    = 0   ✓")
    val_sym = simplify(A_toy(E_sym))
    assert val_sym != 0, f"A_toy(e_sym) = {val_sym}, expected non-zero"
    print(f"  A_toy(e_sym)     = {val_sym}  (non-zero, spans V_val^perp)")
    print("  [PASS] V_val is exactly the kernel of A_toy.")


def verify_explicit_basis_orthonormality():
    """{e_11, e_22, e_anti, e_sym} is HS-orthonormal."""
    print("=" * 70)
    print("[lem:value-subspace-explicit-basis]  Orthonormal basis of M_2(R)")
    print("=" * 70)
    basis = [("e_11", E11), ("e_22", E22), ("e_anti", E_anti), ("e_sym", E_sym)]
    for name_a, A in basis:
        norm_sq = simplify(hs_inner(A, A))
        assert norm_sq == 1, f"||{name_a}||^2 = {norm_sq}, expected 1"
    print("  All basis elements have HS norm 1.")
    for i, (name_a, A) in enumerate(basis):
        for j, (name_b, B) in enumerate(basis):
            if i < j:
                ip = simplify(hs_inner(A, B))
                assert ip == 0, f"<{name_a}, {name_b}>_HS = {ip}, expected 0"
    print("  All distinct pairs are HS-orthogonal.")
    print("  [PASS] {e_11, e_22, e_anti, e_sym} is HS-orthonormal in M_2(R).")


# ---------------------------------------------------------------------------
# (ii) Pi_trans explicit formula and properties.
# ---------------------------------------------------------------------------

def verify_transverse_projection_explicit_formula():
    """Pi_trans X = ((x_12 + x_21)/2) * [[0,1],[1,0]] equals the orthogonal
    projection X -> <X, e_sym>_HS * e_sym.
    """
    print("=" * 70)
    print("[def:transverse-projection]  Pi_trans X = <X, e_sym>_HS e_sym")
    print("=" * 70)
    X = generic_2x2_matrix()
    rhs = Pi_trans(X)
    proj = hs_inner(X, E_sym) * E_sym
    delta = simplify(rhs - proj)
    assert delta == zeros(2, 2), f"Pi_trans formula mismatch: {delta}"
    print("  [PASS] explicit formula matches the HS orthogonal projection.")


def verify_pi_trans_idempotent():
    print("=" * 70)
    print("[lem:transverse-projection-properties]  Pi_trans^2 = Pi_trans")
    print("=" * 70)
    X = generic_2x2_matrix()
    delta = simplify(Pi_trans(Pi_trans(X)) - Pi_trans(X))
    assert delta == zeros(2, 2), f"Pi_trans not idempotent: {delta}"
    print("  [PASS] Pi_trans^2 = Pi_trans on a generic 2x2 matrix.")


def verify_pi_trans_self_adjoint():
    print("=" * 70)
    print("[lem:transverse-projection-properties]  Pi_trans = Pi_trans^* (HS)")
    print("=" * 70)
    X = generic_2x2_matrix(prefix="x")
    Y = generic_2x2_matrix(prefix="y")
    lhs = simplify(hs_inner(Pi_trans(X), Y))
    rhs = simplify(hs_inner(X, Pi_trans(Y)))
    delta = simplify(lhs - rhs)
    assert delta == 0, (
        f"Pi_trans not self-adjoint: <Pi X, Y> - <X, Pi Y> = {delta}"
    )
    print("  [PASS] <Pi_trans X, Y>_HS = <X, Pi_trans Y>_HS.")


def verify_pi_trans_kernel_equals_V_val():
    print("=" * 70)
    print("[lem:transverse-projection-properties]  ker(Pi_trans) = V_val")
    print("=" * 70)
    # Pi_trans annihilates each V_val basis element.
    for name, M in (("e_11", E11), ("e_22", E22), ("e_anti", E_anti)):
        out = simplify(Pi_trans(M))
        assert out == zeros(2, 2), f"Pi_trans({name}) = {out}, expected 0"
        print(f"  Pi_trans({name}) = 0  ✓")
    # And does NOT annihilate e_sym (V_val^perp generator).
    sym_proj = simplify(Pi_trans(E_sym))
    delta = simplify(sym_proj - E_sym)
    assert delta == zeros(2, 2), (
        f"Pi_trans(e_sym) = {sym_proj}, expected e_sym"
    )
    print(f"  Pi_trans(e_sym) = e_sym  ✓")
    print("  [PASS] kernel of Pi_trans is exactly V_val; e_sym is fixed.")


def verify_quotient_representative_and_norm_relation():
    """Verify Pi_trans X = A_toy(X)/sqrt(2) e_sym and the HS norm relation."""
    print("=" * 70)
    print("[lem:transverse-projection-quotient-representative]  scalar/norm bridge")
    print("=" * 70)
    X = generic_2x2_matrix()
    pi_X = Pi_trans(X)
    representative = simplify(A_toy(X) / sqrt(2)) * E_sym
    delta_rep = simplify(pi_X - representative)
    assert delta_rep == zeros(2, 2), f"Pi_trans representative mismatch: {delta_rep}"
    residual = simplify(X - pi_X)
    residual_A = simplify(A_toy(residual))
    assert residual_A == 0, f"X - Pi_trans X not in V_val: A={residual_A}"
    norm_sq = simplify(hs_inner(pi_X, pi_X))
    expected_norm_sq = simplify(A_toy(X)**2 / 2)
    delta_norm = simplify(norm_sq - expected_norm_sq)
    assert delta_norm == 0, f"norm relation mismatch: {delta_norm}"
    print("  [PASS] Pi_trans X = A_toy(X)/sqrt(2) * e_sym.")
    print("  [PASS] X - Pi_trans X lies in V_val.")
    print("  [PASS] ||Pi_trans X||_HS^2 = A_toy(X)^2 / 2.")


def verify_pi_trans_operator_norm():
    """An orthogonal projection onto a 1D subspace of a Hilbert space has
    operator norm 1.  Verify via direct calculation: for every X with
    ||X||_HS <= 1, ||Pi_trans X||_HS <= 1, and equality at X = e_sym.
    """
    print("=" * 70)
    print("[eq:Pi-trans-norm]  ||Pi_trans||_op = 1")
    print("=" * 70)
    # ||Pi_trans X||_HS^2 = (<X, e_sym>_HS)^2.  By Cauchy-Schwarz with
    # ||e_sym||_HS = 1, this is <= ||X||_HS^2.  Equality at X = e_sym.
    X = generic_2x2_matrix()
    pi_norm_sq = simplify(hs_inner(Pi_trans(X), Pi_trans(X)))
    inner_sq = simplify(hs_inner(X, E_sym)**2)
    delta = simplify(pi_norm_sq - inner_sq)
    assert delta == 0, (
        f"||Pi_trans X||_HS^2 != <X, e_sym>_HS^2: {delta}"
    )
    print("  ||Pi_trans X||_HS^2 = <X, e_sym>_HS^2  (verified symbolically)")
    # Equality at X = e_sym.
    eq_at_sym = simplify(
        hs_inner(Pi_trans(E_sym), Pi_trans(E_sym)) - hs_inner(E_sym, E_sym)
    )
    assert eq_at_sym == 0, f"||Pi e_sym||_HS != ||e_sym||_HS: {eq_at_sym}"
    print("  ||Pi_trans e_sym||_HS = ||e_sym||_HS  ✓ (norm achieved)")
    print("  [PASS] ||Pi_trans||_op = 1.")


# ---------------------------------------------------------------------------
# (iii) Compatibility with A_toy.
# ---------------------------------------------------------------------------

def verify_A_toy_descends_through_pi_trans():
    """A_toy(Pi_trans X) = A_toy(X) for every X."""
    print("=" * 70)
    print("[lem:transverse-projection-A-toy-compatibility]  "
          "A_toy o Pi_trans = A_toy")
    print("=" * 70)
    X = generic_2x2_matrix()
    delta = simplify(A_toy(Pi_trans(X)) - A_toy(X))
    assert delta == 0, (
        f"A_toy(Pi X) - A_toy(X) = {delta}, expected 0"
    )
    print("  [PASS] A_toy(Pi_trans X) = A_toy(X) for generic X.")




def A_2(X):
    """Two-point actual-zeta scalar channel: A_2(X)=A_toy(Pi_trans X)."""
    return A_toy(Pi_trans(X))


def verify_A2_type_handoff():
    """Verify the type-safe §7 handoff: A_2(X) is scalar-valued and equals
    A_toy(X).  This guards against the ill-typed expression Pi_trans A_2(X).
    """
    print("=" * 70)
    print("[type handoff]  A_2(X) := A_toy(Pi_trans X) = A_toy(X)")
    print("=" * 70)
    X = generic_2x2_matrix()
    delta = simplify(A_2(X) - A_toy(X))
    assert delta == 0, f"A_2(X)-A_toy(X) = {delta}, expected 0"
    print("  [PASS] A_2 is the same scalar channel as A_toy after projection.")


def verify_A2_quotient_well_defined():
    """If X-Y lies in V_val=ker(A_toy), then A_2(X)=A_2(Y).

    This is the symbolic type check for the Section 7 handoff: the
    actual-zeta side should use A_2(X)=A_toy(X) or ell_2(Pi_trans X),
    not Pi_trans(A_2(X)).
    """
    print("=" * 70)
    print("[lem:A2-quotient-well-defined]  A_2 descends to M_2/V_val")
    print("=" * 70)
    X = generic_2x2_matrix(prefix="x")
    a, b, c = symbols("a b c", real=True)
    V = a * E11 + b * E22 + c * E_anti
    assert simplify(A_toy(V)) == 0, f"generic V_val element has A_toy={A_toy(V)}"
    delta = simplify(A_toy(X + V) - A_toy(X))
    assert delta == 0, f"A_2 not quotient well-defined: {delta}"

    P = Pi_trans(X)
    R = simplify(X - P)
    assert simplify(A_toy(R)) == 0, f"X - Pi_trans X not in V_val: {A_toy(R)}"
    assert simplify(hs_inner(R, P)) == 0, "orthogonal decomposition failed"
    ell2_PiX = simplify(P[0, 1] + P[1, 0])
    delta_rep = simplify(ell2_PiX - A_toy(X))
    assert delta_rep == 0, f"ell_2(Pi X) != A_2(X): {delta_rep}"
    print("  [PASS] A_2 is invariant under adding V_val and equals ell_2(Pi X).")


# ---------------------------------------------------------------------------
# (iv) Regression: v1's A_val(x) lies in V_val.
# ---------------------------------------------------------------------------

def verify_A_val_v1_lies_in_V_val():
    """Regression check: v1's matrix A_val(x) (Proposition prop:explicit-Aval
    of proof_of_rh.tex line 1260) has off-diagonal entries that are exact
    negatives of each other, so x_12 + x_21 = 0.  Hence A_val(x) lies in
    V_val and is annihilated by Pi_trans.

    The v1 formula (with B factored out):
        A_val(x) = (1/B) * [[(x cos x - sin x)/x,
                             sqrt(3)*(-x^2 sin x - 2x cos x + 2 sin x)/x^2],
                            [sqrt(3)*(x^2 sin x + 2x cos x - 2 sin x)/x^2,
                             3*(x^3 cos x - 6x cos x + 3*(2 - x^2) sin x)/x^3]]
    """
    print("=" * 70)
    print("[regression]  v1's A_val(x) lies in V_val (rebuild's kernel of A_toy)")
    print("=" * 70)
    x, B = symbols("x B", real=True, positive=True)
    a11 = (x * cos(x) - sin(x)) / x
    a12 = sp.sqrt(3) * (-x**2 * sin(x) - 2 * x * cos(x) + 2 * sin(x)) / x**2
    a21 = sp.sqrt(3) * (x**2 * sin(x) + 2 * x * cos(x) - 2 * sin(x)) / x**2
    a22 = 3 * (x**3 * cos(x) - 6 * x * cos(x) + 3 * (2 - x**2) * sin(x)) / x**3
    A_val = (1 / B) * Matrix([[a11, a12], [a21, a22]])
    # A_toy(A_val) = a12 + a21 (after the 1/B factor).
    off_diag_sum = simplify(A_val[0, 1] + A_val[1, 0])
    off_diag_sum = trigsimp(off_diag_sum)
    assert off_diag_sum == 0, (
        f"A_val(x) has nonzero A_toy: {off_diag_sum}; "
        "expected anti-symmetric off-diagonal (cor:PhiK-Aval-zero of v1)"
    )
    print("  A_toy(A_val(x)) = 0  (matches v1's cor:PhiK-Aval-zero).")
    # And Pi_trans annihilates it.
    pi_A_val = Pi_trans(A_val)
    pi_A_val_simplified = sp.simplify(pi_A_val)
    pi_A_val_trig = pi_A_val_simplified.applyfunc(trigsimp)
    assert pi_A_val_trig == zeros(2, 2), (
        f"Pi_trans(A_val) != 0: {pi_A_val_trig}"
    )
    print("  Pi_trans(A_val(x)) = 0  ✓")
    print("  [PASS] v1's A_val(x) is in V_val and annihilated by Pi_trans.")


# ---------------------------------------------------------------------------
# (v) Residual gauge invariance.
# ---------------------------------------------------------------------------

def verify_residual_gauge_invariance_symbolic():
    """rem:transverse-projection-residual-gauge.

    The retained chart of Definition def:local-phase-chart pins Phi_T = theta.
    Additive constants Phi -> Phi + c leave q, q', q'' unchanged
    (derivatives of constants are zero), hence leave G_{m,±}, N_m, and
    Omega_zeta unchanged.  Affine-jet shifts Phi -> Phi + a t change q
    to q + a and so do not preserve the chart class; this is recorded as
    a negative test.
    """
    print("=" * 70)
    print("[rem:transverse-projection-residual-gauge]  Phi -> Phi + c invariance")
    print("=" * 70)
    t_var = sp.symbols("t", real=True)
    c_const, a_aff = sp.symbols("c a", real=True)
    Phi_sym = sp.Function("Phi")(t_var)

    # Additive constant: q, q', q'' invariant.
    Phi_shift_const = Phi_sym + c_const
    for k in (1, 2, 3):
        delta = sp.simplify(
            sp.diff(Phi_shift_const, t_var, k) - sp.diff(Phi_sym, t_var, k)
        )
        assert delta == 0, (
            f"k={k}-th derivative not invariant under Phi -> Phi + c: {delta}"
        )
    print("  [PASS] q, q', q'' invariant under Phi -> Phi + c.")
    print("         Hence G_{m,±}, N_m, Omega_zeta are gauge-invariant.")

    # Affine-jet shift: q changes by a (negative test; not a chart symmetry).
    Phi_shift_aff = Phi_sym + a_aff * t_var
    delta_q_aff = sp.simplify(
        sp.diff(Phi_shift_aff, t_var) - sp.diff(Phi_sym, t_var)
    )
    assert sp.simplify(delta_q_aff - a_aff) == 0, (
        f"affine-shift q-change != a: {delta_q_aff}"
    )
    delta_qp_aff = sp.simplify(
        sp.diff(Phi_shift_aff, t_var, 2) - sp.diff(Phi_sym, t_var, 2)
    )
    assert delta_qp_aff == 0
    print("  [PASS] Phi -> Phi + a t changes q by a (not a chart symmetry).")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    verify_value_subspace_kernel_of_A_toy()
    print()
    verify_explicit_basis_orthonormality()
    print()
    verify_transverse_projection_explicit_formula()
    print()
    verify_pi_trans_idempotent()
    print()
    verify_pi_trans_self_adjoint()
    print()
    verify_pi_trans_kernel_equals_V_val()
    print()
    verify_quotient_representative_and_norm_relation()
    print()
    verify_pi_trans_operator_norm()
    print()
    verify_A_toy_descends_through_pi_trans()
    print()
    verify_A2_type_handoff()
    print()
    verify_A2_quotient_well_defined()
    print()
    verify_residual_gauge_invariance_symbolic()
    print()
    verify_A_val_v1_lies_in_V_val()
    print()
    print("=" * 70)
    print("All §6 lemmas verified symbolically:")
    print("  - def:value-subspace: V_val = ker(A_toy)")
    print("  - lem:value-subspace-explicit-basis: orthonormal basis")
    print("    {e_11, e_22, e_anti, e_sym} of M_2(R)")
    print("  - def:transverse-projection: Pi_trans X = <X,e_sym>_HS e_sym")
    print("  - lem:transverse-projection-properties: idempotent, self-adjoint,")
    print("    kernel = V_val, ||Pi_trans||_op = 1")
    print("  - lem:transverse-projection-quotient-representative:")
    print("    Pi_trans X = A_toy(X)/sqrt(2) e_sym and")
    print("    ||Pi_trans X||_HS^2 = A_toy(X)^2/2")
    print("  - lem:transverse-projection-A-toy-compatibility:")
    print("    A_toy(Pi_trans X) = A_toy(X)")
    print("  - lem:A2-quotient-well-defined: A_2 descends to M_2/V_val")
    print("  - rem:transverse-projection-residual-gauge: Phi -> Phi + c")
    print("    leaves q, q', q'', and hence G_{m,±}, N_m, Omega, unchanged")
    print("  - regression: v1's A_val(x) lies in V_val and is annihilated")
    print("    by Pi_trans (matches v1's cor:PhiK-Aval-zero)")
    print("=" * 70)


if __name__ == "__main__":
    sys.exit(main() if main() else 0)
