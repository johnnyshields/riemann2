# UV-026 L2N0R1 / L1N0R2 Classification Notes

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
The right-heavy family is the endpoint-swapped analogue of the left-heavy
family under \(z\mapsto -z\), \(-\leftrightarrow+\), with the ordered product
\(LNR\) kept at matrix level.

## Classification

`L_2N_0R_1` and `L_1N_0R_2` are not classified by current source as
source-trivial, one-pair `K_5`, one-pair `K_3`, or pure same-point.  They reduce
to a mixed first/second-Frechet coefficient theorem with the baseline ordered
mixed block \(N_0\) in the middle.

Reasons:

- They are not source-trivial: the three source-linear same-point factors can
  carry non-`(1,1)` tags \(\tau_1^2\tau_2\) and \(\tau_1\tau_2^2\) of finite
  grade \((1,1,5)\).
- They are not identified as `K_5` unless their actual coefficient is put into
  \(c_2A_5+[B_2,A_5]\).
- They are not identified as `K_3` unless their actual coefficient is put into
  \(c_4A_3+[B_4,A_3]+c_2[B_2,A_3]+A_3B_2^2-B_2A_3B_2\).
- They are not pure same-point: \(N_0\) is an ordered-pair baseline mixed
  factor, and the source factors sit on both sides of it.
- They are not proved \(A_5^{\mathfrak f}\)-gauge until the fixed-sector
  \(z^7\) coefficients below are computed and tested against
  \(A_5^{\mathfrak f}(m)\).

## Exact Missing Theorem

Let
\[
\mathcal L_{-,ab}^{\{p,q\}}(z)
\]
denote the tag-\(ab\), finite-grade multiset \(\{p,q\}\) coefficient in
\[
L_2(z)
=
\frac12D^2(G_-^{(0)}(z)^{-1/2})
[\delta G_-(z),\delta G_-(z)].
\]
Let \(\Lambda_{i,\pm}^{[g]}(z)\) denote the finite-grade \(g\) part of the
first-Frechet output
\[
D(G_\pm^{(0)}(z)^{-1/2})[\delta G_{i,\pm}^{\lin}(z)].
\]
Let \(N_0(z)=N^{(0)}(z)\).  Then the left-heavy family needs
\[
C_{112}^{L_2N_0R_1}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\mathcal L_{-,11}^{\{1,1\}}N_0\Lambda_{2,+}^{[5]}
+\mathcal L_{-,11}^{\{1,5\}}N_0\Lambda_{2,+}^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}N_0\Lambda_{1,+}^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}N_0\Lambda_{1,+}^{[1]}
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m),
\]
and
\[
C_{122}^{L_2N_0R_1}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\mathcal L_{-,22}^{\{1,1\}}N_0\Lambda_{1,+}^{[5]}
+\mathcal L_{-,22}^{\{1,5\}}N_0\Lambda_{1,+}^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}N_0\Lambda_{2,+}^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}N_0\Lambda_{2,+}^{[1]}
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m).
\]

For the right-heavy family, define
\[
\mathcal R_{+,ab}^{\{p,q\}}(z)
\]
analogously from
\[
R_2(z)
=
\frac12D^2(G_+^{(0)}(z)^{-1/2})
[\delta G_+(z),\delta G_+(z)].
\]
Then the missing theorem is
\[
C_{112}^{L_1N_0R_2}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\Lambda_{2,-}^{[5]}N_0\mathcal R_{+,11}^{\{1,1\}}
+\Lambda_{2,-}^{[1]}N_0\mathcal R_{+,11}^{\{1,5\}}
+\Lambda_{1,-}^{[5]}N_0\mathcal R_{+,12}^{\{1,1\}}
+\Lambda_{1,-}^{[1]}N_0\mathcal R_{+,12}^{\{1,5\}}
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m),
\]
and
\[
C_{122}^{L_1N_0R_2}
:=
\pi_{\mathfrak f}[z^7]\Bigl(
\Lambda_{1,-}^{[5]}N_0\mathcal R_{+,22}^{\{1,1\}}
+\Lambda_{1,-}^{[1]}N_0\mathcal R_{+,22}^{\{1,5\}}
+\Lambda_{2,-}^{[5]}N_0\mathcal R_{+,12}^{\{1,1\}}
+\Lambda_{2,-}^{[1]}N_0\mathcal R_{+,12}^{\{1,5\}}
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m).
\]

Equivalently, each of the four coefficients \(C=uI+vS\) must satisfy
\[
uv_5-u_5v=0
\]
against \(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

## Formal Witness Boundary

The script `scripts/l2n0r1_formal_witness.py` uses an identity baseline,
the mixed second-order coefficient \(3(AB+BA)/8\), and the first-order
coefficient \(-C/2\) of \((I+E)^{-1/2}\).  With a first-side input
\(3I+7S\), it obtains fixed-sector vector \((-9/8,-21/8)\) for both
`L_2N_0R_1` and `L_1N_0R_2`; the determinant against
\(A_5^{\mathfrak f}=(2,5)\) is \(-3/8\).  This is not actual-package evidence.
It only rejects formal matrix-algebra shortcuts and source-support shortcuts.

## Inventory Status

Together with the prior reports, all seven cubic families now have a sharp
classification boundary:

- `L_1YR_1`: first-Frechet/mixed/first-Frechet coefficient table theorem.
- `L_3N_0R_0`, `L_0N_0R_3`: third-Frechet coefficient theorem.
- `L_2YR_0`, `L_0YR_2`: second-Frechet plus mixed-input theorem.
- `L_2N_0R_1`, `L_1N_0R_2`: second-Frechet plus baseline mixed block plus
  first-Frechet theorem.
