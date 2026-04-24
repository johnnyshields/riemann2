# UV-023 Q7q Extractor Map

Own lane: `gap-closer-UV023-Q7q-extractor`.

## Candidate Definition

On a good patch with \(A_5^{\mathfrak f}(m)\neq0\), the clean fixed target is
\[
V_m^q:=\mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]
If the corrected-whitening cross-effect \(C\) has a fixed-sector order-7
coefficient
\[
B_7^{\mathfrak f}(C;m,\omega,\delta)\in\mathfrak f
\]
before determinant scalarization, then the definition-first extractor should be
\[
Q_{7,m}^q(C):=[B_7^{\mathfrak f}(C;m,\omega,\delta)]_{V_m^q}.
\]
This is quotient-valued. The determinant pairing
\[
[B]\mapsto \det(B,A_5^{\mathfrak f}(m))
\]
is then only a coordinate on \(V_m^q\) after \(Q_{7,m}^q(C)\) exists.

If the natural source object first lives in a moving quotient
\(\mathfrak f/\mathbf C A_5^{\mathfrak f}(h_1)\), the good-patch
moving-to-midpoint trivialization can be used after the quotient class is
constructed. It should not replace construction of \(B_7^{\mathfrak f}(C)\) or
of the moving quotient class.

## What Source Supplies

- `rh/proof_of_rh.tex:7004-7062`: one-pair fixed-sector \(A_5^{\mathfrak f}\),
  \(A_7^{\mathfrak f}\), and quotient class
  \([A_7^{\mathfrak f}]\in\mathfrak f/\mathbf C A_5^{\mathfrak f}\).
- `rh/proof_of_rh.tex:7892-8033`: one-pair quotient-septic closure.
- `rh/proof_of_rh.tex:11587-11775`: finite-delta theorem assumes
  \(\overline E_{12}^{(7;1)}\) already exists in a moving quotient and then
  uses \(\det(R,A_{5,1}^{\mathfrak f})\).
- `rh/proof_of_rh.tex:2415-2587`: corrected-whitening transfer
  \(\mathcal T_{Q,R}(X)\) after \(\Phi_K\), with homogeneous expansion.

## Missing Lift

The source does not define a matrix/fixed-sector coefficient
\[
B_7^{\mathfrak f}(C)
\]
for the actual source-linear corrected-whitening cross-effect before applying a
scalar channel. The proposition at `2415--2587` outputs the scalar
\(\Phi_K\)-visible transfer, not the quotient-valued fixed-sector class.

Thus the smallest extractor-side missing definition is not the quotient target;
it is the map
\[
C\longmapsto B_7^{\mathfrak f}(C)\in\mathfrak f
\]
for the actual pre-determinant cross-effect.

## Compatibility Reduction

If \(Q_{7,m}^q\) is defined as above and \(C\) has a source-bidegree
decomposition, then \(Q_{7,m}^q\) is linear over that decomposition. However,
\[
Q_{7,m}^q((1-\Pi_{1,1})C)=0
\]
is equivalent to saying every non-\((1,1)\) order-7 fixed-sector coefficient is
a multiple of \(A_5^{\mathfrak f}(m)\). This is a theorem, not a consequence of
the quotient definition.

A cubic finite-order witness of type \((1,1,5)\) can reach total grade \(7\).
Unless its fixed-sector vector lands in \(\mathbf C A_5^{\mathfrak f}(m)\), the
fixed-target quotient extractor sees it.

## Minimal Open List

Definitions still missing:

1. \(L_h\) / \(X^{[1]}\): source-linear corrected-block input before whitening.
2. \(B_7^{\mathfrak f}(C)\): pre-determinant fixed-sector order-7 coefficient
   of the actual corrected-whitening cross-effect.
3. \(\Pi_{1,1}\): source-bidegree projection before \(Q_{7,m}^q\).

Theorem still missing:

4. \(B_7^{\mathfrak f}((1-\Pi_{1,1})C)\in
   \mathbf C A_5^{\mathfrak f}(m)\), equivalently
   \(Q_{7,m}^q((1-\Pi_{1,1})C)=0\).
