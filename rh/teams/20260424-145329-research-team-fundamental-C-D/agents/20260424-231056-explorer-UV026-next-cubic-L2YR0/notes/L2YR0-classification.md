# UV-026 L2YR0 / L0YR2 Classification Notes

## Matrix Convention

Work before `\Phi_K` with
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]
Write
\[
L(z)=G_-^{(0)}(z)^{-1/2}+L_1(z)+L_2(z)+\cdots,
\]
\[
R(z)=G_+^{(0)}(z)^{-1/2}+R_1(z)+R_2(z)+\cdots,
\qquad
N(z)=N_0(z)+Y(z).
\]
The fixed-sector projection is
\[
\pi_{\mathfrak f}(A)=\frac12(A+J_0AJ_0),
\qquad
\mathfrak f=\operatorname{span}\{I,S\}.
\]
The right-hand family is the endpoint-swapped analogue of the left-hand family
under \(z\mapsto -z\), \(-\leftrightarrow+\), with the ordered product \(LNR\)
kept at matrix level.

## Classification

`L_2YR_0` and `L_0YR_2` are not classified by the current source as
source-trivial, one-pair `K_5`, one-pair `K_3`, or pure same-point.  They reduce
to a second-Frechet coefficient theorem coupled to the grade-one/grade-five
mixed input.

Reasons:

- They are not source-trivial.  \(Y\) is the source-linear mixed block from the
  tagged pre-whitening source block, and \(L_2\) or \(R_2\) can carry two
  additional source-linear same-point factors, producing non-`(1,1)` tags
  \(\tau_1^2\tau_2\) and \(\tau_1\tau_2^2\).
- They are not identified as `K_5` unless the actual coefficient is put into
  \(c_2A_5+[B_2,A_5]\).
- They are not identified as `K_3` unless the actual coefficient is put into
  \(c_4A_3+[B_4,A_3]+c_2[B_2,A_3]+A_3B_2^2-B_2A_3B_2\).
- They are not pure same-point because \(Y\) is an actual mixed block
  perturbation.
- They are not proved \(A_5^{\mathfrak f}\)-gauge until the fixed-sector
  \(z^7\) coefficients below are computed and tested against
  \(A_5^{\mathfrak f}(m)\).

## Exact Missing Theorem

Let
\[
\mathcal L_{-,ab}^{\{p,q\}}(z)
\]
denote the tag-\(ab\), finite-grade multiset \(\{p,q\}\) coefficient in the
quadratic homogeneous inverse-square-root output
\[
L_2(z)
=
\frac12D^2(G_-^{(0)}(z)^{-1/2})
[\delta G_-(z),\delta G_-(z)].
\]
The braces mean that both ordered grade placements are included when
\(p\neq q\).  Let \(M_i^{[r]}(z)\) denote the source-linear mixed input of
finite grade \(r\) in the same normalization as \(B_7^{\mathfrak f}\), and let
\[
R_0(z):=G_+^{(0)}(z)^{-1/2}.
\]

For the left family, the \(\tau_1^2\tau_2\) coefficient theorem needed is
\[
C_{112}^{L_2YR_0}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\bigl(
\mathcal L_{-,11}^{\{1,1\}}M_2^{[5]}
+\mathcal L_{-,11}^{\{1,5\}}M_2^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}M_1^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}M_1^{[1]}
\bigr)R_0
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m).
\]
The \(\tau_1\tau_2^2\) coefficient is
\[
C_{122}^{L_2YR_0}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\bigl(
\mathcal L_{-,22}^{\{1,1\}}M_1^{[5]}
+\mathcal L_{-,22}^{\{1,5\}}M_1^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}M_2^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}M_2^{[1]}
\bigr)R_0
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m).
\]

For the right family, define
\[
\mathcal R_{+,ab}^{\{p,q\}}(z)
\]
analogously from
\[
R_2(z)
=
\frac12D^2(G_+^{(0)}(z)^{-1/2})
[\delta G_+(z),\delta G_+(z)],
\]
and set \(L_0(z):=G_-^{(0)}(z)^{-1/2}\).  The required right-family theorem is
the same pair of statements with
\[
\bigl(\cdots\bigr)R_0
\quad\text{replaced by}\quad
L_0\bigl(
M_2^{[5]}\mathcal R_{+,11}^{\{1,1\}}
+M_2^{[1]}\mathcal R_{+,11}^{\{1,5\}}
+M_1^{[5]}\mathcal R_{+,12}^{\{1,1\}}
+M_1^{[1]}\mathcal R_{+,12}^{\{1,5\}}
\bigr)
\]
for \(112\), and by the tag-swapped \(122\) expression.

Equivalently, each of the four coefficients \(C\) must be written as
\[
C=uI+vS
\]
and must satisfy
\[
uv_5-u_5v=0
\]
against \(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

## Formal Witness Boundary

The script `scripts/l2yr0_formal_witness.py` uses an identity baseline and the
mixed second-order coefficient \(3(AB+BA)/8\) of \((I+E)^{-1/2}\).  With
\(Y=3I+7S\), it obtains fixed-sector vector \((9/4,21/4)\) for both
`L_2YR_0` and `L_0YR_2`; the determinant against \(A_5^{\mathfrak f}=(2,5)\)
is \(3/4\).  This is not actual-package evidence.  It only rejects formal
matrix-algebra shortcuts and source-support shortcuts.
