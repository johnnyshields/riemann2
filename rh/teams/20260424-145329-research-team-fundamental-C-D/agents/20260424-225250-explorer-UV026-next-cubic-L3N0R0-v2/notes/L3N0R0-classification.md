# UV-026 L3N0R0 / L0N0R3 Classification Notes

## Matrix convention

Work before `\Phi_K` with
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]
Write
\[
L(z)=G_-^{(0)}(z)^{-1/2}+L_1(z)+L_2(z)+L_3(z)+\cdots,
\]
\[
R(z)=G_+^{(0)}(z)^{-1/2}+R_1(z)+R_2(z)+R_3(z)+\cdots,
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
under \(z\mapsto -z\), \(-\leftrightarrow+\), with the same ordered matrix
product convention.  This symmetry does not commute with passing to a scalar;
all claims here are matrix/fixed-sector claims.

## Classification

`L_3N_0R_0` and `L_0N_0R_3` are not classified by the current source as
source-trivial, one-pair `K_5`, one-pair `K_3`, or pure same-point.  They reduce
to the exact missing third-Frechet coefficient theorem below.

Reasons:

- They have no source perturbation in the mixed block, but they are not
  source-trivial for UV-026: the cubic inverse-square-root term can contain
  non-`(1,1)` source tags \(\tau_1^2\tau_2\) and \(\tau_1\tau_2^2\) of
  finite-grade type \((1,1,5)\).
- They are not identified with the one-pair `K_5` source class unless their
  actual fixed-sector coefficient is put into the displayed form
  \(c_2A_5+[B_2,A_5]\).
- They are not identified with the one-pair `K_3` source class unless their
  actual coefficient is put into
  \(c_4A_3+[B_4,A_3]+c_2[B_2,A_3]+A_3B_2^2-B_2A_3B_2\).
- They are not safely pure same-point: \(N_0R_0\) or \(L_0N_0\) is still an
  ordered-pair baseline matrix factor, so the pure same-point parity lemma
  cannot be invoked without first proving the relevant coefficient has no
  transport factor in the lemma's sense.

## Exact missing theorem

Let \(\mathcal L_{-,112}^{(3;1,1,5)}(z)\) be the coefficient of
\(\tau_1^2\tau_2\) and finite grades \((1,1,5)\) in the cubic homogeneous
third-Frechet inverse-square-root output on the left:
\[
L_3(z)=\frac1{6}D^3(G_-^{(0)}(z)^{-1/2})
[\delta G_-(z),\delta G_-(z),\delta G_-(z)].
\]
Define \(\mathcal L_{-,122}^{(3;1,1,5)}\) analogously for
\(\tau_1\tau_2^2\).  The left-family coefficient theorem needed is
\[
\pi_{\mathfrak f}[z^7]\,
\mathcal L_{-,112}^{(3;1,1,5)}(z)N_0(z)G_+^{(0)}(z)^{-1/2}
\in \mathbf C A_5^{\mathfrak f}(m),
\]
and the same statement with \(112\) replaced by \(122\).

For the right family, let \(\mathcal R_{+,112}^{(3;1,1,5)}\) and
\(\mathcal R_{+,122}^{(3;1,1,5)}\) be the analogous third-Frechet outputs for
\(G_+^{(0)}(z)^{-1/2}\).  The missing theorem is
\[
\pi_{\mathfrak f}[z^7]\,
G_-^{(0)}(z)^{-1/2}N_0(z)\mathcal R_{+,112}^{(3;1,1,5)}(z)
\in \mathbf C A_5^{\mathfrak f}(m),
\]
and the same statement with \(112\) replaced by \(122\).

Equivalently, if these four fixed-sector coefficients are written
\[
uI+vS,
\]
then each must satisfy
\[
uv_5-u_5v=0
\]
against \(A_5^{\mathfrak f}(m)=u_5I+v_5S\), before `\Phi_K`,
determinant scalarization, quotient extraction, diagonal merger, or one-pair
gauge laws.

## Formal witness boundary

The script `scripts/l3_r3_formal_witness.py` uses an identity baseline and the
cubic coefficient \(-5E^3/16\) of \((I+E)^{-1/2}\).  For a
\(\tau_1^2\tau_2\), grade \((1,1,5)\) input it produces fixed-sector vector
\((-15/8,0)\) for both all-left and all-right families.  Against
\(A_5^{\mathfrak f}=(2,5)\), the determinant is \(-75/8\).  This is not an
actual-package counterexample; it only rejects source-support or formal
matrix-algebra shortcuts.
