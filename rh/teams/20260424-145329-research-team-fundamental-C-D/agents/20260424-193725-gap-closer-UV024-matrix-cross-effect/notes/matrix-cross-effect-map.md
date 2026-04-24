# UV-024 Matrix Cross-Effect Map

Own lane: `gap-closer-UV024-matrix-cross-effect`.

## Conditional Construction

The matrix whitening map already exists:
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]
On the analytic Banach neighborhood from `prop:differentiated-whitening-transfer`,
if a source-linear input \(L_h=(L_{h,-},M_h,L_{h,+})\) exists before whitening,
then the matrix cross-effect can be defined before \(\Phi_K\) by
\[
C_{\mathcal W}(a_1,h_1;a_2,h_2)
:=
\mathcal W(B+a_1L_{h_1}+a_2L_{h_2})
-\mathcal W(B+a_1L_{h_1})
-\mathcal W(B+a_2L_{h_2})
+\mathcal W(B),
\]
where \(B=(G_-^{(0)},N^{(0)},G_+^{(0)})\).

If this object is the actual corrected-whitening two-atom cross-effect, the
coefficient map is simply
\[
B_7^{\mathfrak f}(C_{\mathcal W})
:=
\pi_{\mathfrak f}[z^7]C_{\mathcal W}.
\]
Then
\[
Q_{7,m}^q(C_{\mathcal W})
:=
[B_7^{\mathfrak f}(C_{\mathcal W})]
\in \mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]
This construction is quotient-valued before determinant scalarization.

## What Current Source Proves

- `rh/proof_of_rh.tex:1392-1458`: finite-\(s\) corrected whitening is
  holomorphic and matrix-valued before scalar extraction.
- `rh/proof_of_rh.tex:1569-1575`, `1784-1799`: the matrix whitening map is
  analytic and has a first-order expansion around a background block.
- `rh/proof_of_rh.tex:2324-2587`: the scaled transfer proposition defines a
  scalar \(\Phi_K\)-visible transfer. Its proof uses matrix analyticity, but
  the stated output is scalar.
- `rh/proof_of_rh.tex:2659-2787`: one-pair weighted corrected-block entries are
  linear in pair kernels modulo higher pair-kernel terms.
- `rh/proof_of_rh.tex:6976-7062`, `7742-8033`: fixed-sector quotient geometry
  exists for one-pair order-7 data.

## Missing Source Step

The current source does not define the actual two-atom source-linear corrected
block triple \(L_h\) or \(X^{[1]}\), and therefore does not identify
\(C_{\mathcal W}\) with the actual corrected-whitening cross-effect of the
two-atom package. The construction above is a valid conditional definition, not
a source theorem.

The current scalar transfer \(\mathcal T_{Q,R}\) is not enough for UV-024
because it applies \(\Phi_K\) before coefficient extraction. A term can be
\(\Phi_K\)-hidden and still nonzero in
\(\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)\).

## Cubic Witness Test

The compatibility theorem is equivalent to
\[
B_7^{\mathfrak f}((1-\Pi_{1,1})C_{\mathcal W})
\in \mathbf C A_5^{\mathfrak f}(m).
\]
A cubic homogeneous transfer with finite grades \((1,1,5)\) can reach order
\(7\). The fixed-sector vector of that witness must be proved proportional to
\(A_5^{\mathfrak f}(m)\). Finite-order grading, source bidegree bookkeeping, or
scalar invisibility under \(\Phi_K\) does not imply this.

## Minimal Missing Theorem

Let \(C_{\mathcal W}\) be the actual matrix cross-effect from the
source-linear corrected-block input. Then every non-\((1,1)\) source-bidegree
component of \(\pi_{\mathfrak f}[z^7]C_{\mathcal W}\) lies in
\(\mathbf C A_5^{\mathfrak f}(m)\).

This theorem, plus the actual source-linear input definition, is the remaining
promotion target for UV-024.
