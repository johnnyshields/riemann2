# UV-010 quotient-line trivialization note

## Local theorem on \(A_5^{\mathfrak f}(m)\neq0\)

Let
\[
\mathfrak f=\operatorname{span}\{I,S\}
\]
with the determinant convention
\[
\det(uI+vS,u'I+v'S)=uv'-vu'
\]
already used by the paper for
\[
\Delta_7=\det(A_7^{\mathfrak f},A_5^{\mathfrak f})
\]
at `rh/proof_of_rh.tex:7029`, `11717`, and `11768-11774`.

Let \(A(h)=A_5^{\mathfrak f}(h)\) be analytic and fix \(m\) with
\[
A(m)\neq0.
\]
Then, after shrinking the collision chart, \(A(h_1)\neq0\) for
\[
h_1=m-\delta/2.
\]
The determinant identifies each moving quotient with \(\mathbf C\):
\[
\Phi_{h_1}\colon \mathfrak f/\mathbf C A(h_1)\to\mathbf C,
\qquad
[X]_{h_1}\mapsto \det(X,A(h_1)).
\]
It also identifies the midpoint quotient with \(\mathbf C\):
\[
\Phi_m\colon \mathfrak f/\mathbf C A(m)\to\mathbf C,
\qquad
[Y]_m\mapsto \det(Y,A(m)).
\]
Hence
\[
T_{h_1\to m}:=\Phi_m^{-1}\Phi_{h_1}
\]
is an analytic trivialization from the moving quotient to the midpoint quotient.
Explicitly, \(T_{h_1\to m}([X]_{h_1})\) is the unique midpoint class \([Y]_m\)
such that
\[
\det(Y,A(m))=\det(X,A(h_1)).
\]

This is well-defined because \(X\mapsto X+\xi A(h_1)\) does not change
\(\det(X,A(h_1))\). It is analytic because \(A(h_1)\) and \(A(m)\) are analytic
and \(\Phi_m^{-1}\) is a fixed local inverse once \(A(m)\neq0\).

Equivalently, choose any local complement vector \(B_m\) satisfying
\[
\det(B_m,A(m))=1.
\]
Then
\[
T_{h_1\to m}([X]_{h_1})=\det(X,A(h_1))[B_m]_m.
\]
The quotient class is independent of the normalized complement choice, since
two such \(B_m\)'s differ by a multiple of \(A(m)\).

## What this proves for UV-010

This proves the quotient-line trivialization component of UV-010 on the patch
\[
A_5^{\mathfrak f}(m)\neq0
\]
once the septic quotient defect is already an analytic moving-quotient section.
Thus a theorem can safely state:
\[
\mathcal H_7^q(m,\kappa,t)
:=
\delta^{-2}T_{h_1\to m}
\bigl(\overline E_{12}^{(7;1)}(m,\omega,\delta)\bigr),
\qquad t=\delta^2,\quad \kappa=2\omega/\delta,
\]
provided the right side is known to be analytic and swap-even/collision-vanishing
in the sense of `rh/proof_of_rh.tex:12452-12469`.

The trivialization does not prove the edge law by itself. The missing input is
still an actual corrected order-7 quotient defect as an analytic moving-quotient
section with second-order collision vanishing.

## Complement or determinant convention

The construction is canonical only after fixing the determinant convention on
\(\mathfrak f\). The paper has already fixed this convention through the basis
\((I,S)\) and the determinant formula for \(\Delta_7\). If a future paper edit
does not want to invoke the determinant, it must instead state an equivalent
normalized complement convention \(B_m\) with \(\det(B_m,A(m))=1\).

Without one of these conventions, the phrase "trivialization to the midpoint
quotient" is underdetermined by a nonzero scalar.

## Exceptional locus \(A_5^{\mathfrak f}(m)=0\)

At \(A_5^{\mathfrak f}(m)=0\), the midpoint target
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)
\]
is \(\mathfrak f\), not a one-dimensional quotient. The rank jumps from one
nearby quotient dimension to two at the midpoint. The determinant map
\[
[Y]_m\mapsto\det(Y,A_5^{\mathfrak f}(m))
\]
is identically zero and cannot invert a quotient scalar.

Therefore UV-010 cannot honestly include the exceptional locus under the same
midpoint quotient language. It needs one of the following extra conventions:

1. restrict the theorem to \(A_5^{\mathfrak f}(m)\neq0\);
2. replace the target at zeros by a projectivized/prepared quotient line, using
   the first nonzero jet of \(A_5^{\mathfrak f}\);
3. define a blow-up quotient bundle over the zero locus and prove the septic
   defect lands analytically in that replacement bundle.

The current paper windows do not provide (2) or (3). The smallest theorem-ready
UV-010 statement should use (1), with a separate UV or clause for the exceptional
zero-locus convention if needed.
