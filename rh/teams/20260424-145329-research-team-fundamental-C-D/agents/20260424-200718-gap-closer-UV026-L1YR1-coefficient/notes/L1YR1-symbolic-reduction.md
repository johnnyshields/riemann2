# L1YR1 Symbolic Reduction Notes

Task: isolate
\[
L_1YR_1=D(G_-^{-1/2})[X_-]\;Y\;D(G_+^{-1/2})[X_+]
\]
at the pre-\(\Phi_K\) matrix/fixed-sector level and decide whether the
non-\((1,1)\), finite-grade \((1,1,5)\), order-7 coefficient is forced into
\(\mathbf C A_5^{\mathfrak f}(m)\).

## What the source gives

- Corrected whitening is a matrix map before \(\Phi_K\):
  \(G_-^{-1/2}N^{\corr}G_+^{-1/2}\);
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415`.
- The whitening map
  \(\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}\) is holomorphic;
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575`.
- The first Frechet terms are displayed at matrix level before scalarization;
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`.
- The derivative \(D(G^{-1/2})[H]\) is given by the Loewner formula;
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:1916-1927`.
- One-pair pair-kernel-linear corrected block data give linear source input
  modulo pair-kernel degree \(\ge2\);
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787`.
- Fixed-sector gauge laws currently classify only identified one-pair \(K_5\)
  and \(K_3\) shadows;
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7295`.

## Formal coefficient shape

Let \(L_{-,i}^{[1]}\) and \(R_{+,i}^{[1]}\) denote the tag-\(\tau_i\)
first-derivative inverse-square-root outputs of finite grade \(1\), and let
\(Y_i^{[5]}\) denote the tag-\(\tau_i\) middle perturbation of finite grade
\(5\).  The non-\((1,1)\) tag parts of the \((1,1,5)\) family have the form
\[
\pi_{\mathfrak f}[z^7]\left(
L_{-,1}^{[1]}Y_1^{[5]}R_{+,2}^{[1]}
+L_{-,1}^{[1]}Y_2^{[5]}R_{+,1}^{[1]}
+L_{-,2}^{[1]}Y_1^{[5]}R_{+,1}^{[1]}
\right)
\]
for the \(\tau_1^2\tau_2\) coefficient, and the swapped expression for
\(\tau_1\tau_2^2\).

Thus the smallest actual symbolic inputs needed for an exact computation are:

1. the order/grade decomposition of \(D(G_-^{-1/2})[X_{i,-}]\) through grade
   \(1\), with matrix entries before \(\Phi_K\);
2. the order/grade decomposition of \(Y_i\) through grade \(5\);
3. the order/grade decomposition of \(D(G_+^{-1/2})[X_{i,+}]\) through grade
   \(1\);
4. the fixed-sector coefficient map \(B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7]\)
   on this matrix product;
5. a proof that the resulting two-vector has zero determinant against
   \(A_5^{\mathfrak f}(m)\).

These inputs are not displayed in the inspected source or staged UV-025 block.

## Formal algebra check

The script
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-200718-gap-closer-UV026-L1YR1-coefficient/scripts/l1yr1_formal_gauge_check.py`
uses a diagonal positive baseline.  In that model, the Loewner derivative for
\(x^{-1/2}\) is entrywise invertible, so prescribed first derivative outputs
can be realized formally.

Choosing \(L_1=I\), \(R_1=I\), and \(Y=3I+7S\) gives
\[
\pi_{\mathfrak f}(L_1YR_1)=(3,7).
\]
Against \(A_5^{\mathfrak f}=(2,5)\), the determinant is
\[
\det\begin{pmatrix}3&2\\7&5\end{pmatrix}=1.
\]
Therefore \(L_1YR_1\) is not forced into \(\mathbf C A_5^{\mathfrak f}\) by
matrix algebra, Loewner invertibility, or source tag bookkeeping alone.

This is a formal witness only.  It does not claim the actual corrected source
coefficients realize \(Y=3I+7S\).  It shows that an actual source coefficient
calculation or theorem is necessary.
