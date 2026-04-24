# Actual Matrix Reduction for \(L_1YR_1\)

Target:
\[
L_1YR_1=D(G_-^{-1/2})[X_-]\;Y\;D(G_+^{-1/2})[X_+]
\]
at the pre-\(\Phi_K\) matrix/fixed-sector level.

## Source-level first-order block matrices

The corrected same-point formula gives, for one tagged source \(i\),
\[
\delta G_{i,\pm}^{\lin}
=
\frac1\pi
\begin{pmatrix}
2d_{i,\pm} & \frac12 e_{i,\pm}\\[0.8ex]
\frac12 e_{i,\pm} &
\frac1{12}\bigl(g_{i,\pm}+6q_{0,\pm}^2d_{i,\pm}\bigr)
\end{pmatrix}
\]
before quadratic and cubic pair-kernel terms.  This is read from
`C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722` together with the exact
same-point formula at `C:/workspace/riemann2/rh/proof_of_rh.tex:227-232`.

The corrected mixed formula gives, with \(c_0=\cos\Delta_0\) and
\(s_0=\sin\Delta_0\),
\[
(\delta N_i^{\lin})_{11}
=-\frac{2}{\pi s}c_0\eta_i,
\]
\[
(\delta N_i^{\lin})_{12}
=\frac1{\pi s^2}
\left(c_0\eta_i+s c_0d_{i,+}-q_{0,+}s s_0\eta_i\right),
\]
\[
(\delta N_i^{\lin})_{21}
=-\frac1{\pi s^2}
\left(c_0\eta_i+s c_0d_{i,-}-q_{0,-}s s_0\eta_i\right),
\]
and
\[
(\delta N_i^{\lin})_{22}
=
\frac1{2\pi s^3}
\left[
(s c_0-q_{0,+}s^2s_0)d_{i,-}
+(s c_0-q_{0,-}s^2s_0)d_{i,+}
\right.
\]
\[
\left.
\quad+
\bigl(-(q_{0,-}+q_{0,+})ss_0+
(2-q_{0,-}q_{0,+}s^2)c_0\bigr)\eta_i
\right].
\]
This is the linear Taylor part of the displayed mixed block
`C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2784`, matching the exact
formula at `C:/workspace/riemann2/rh/proof_of_rh.tex:235-248`.

The one-pair kernels satisfy
\[
d_{i,\pm}=z^2Q^{-4}U_{i,\pm},\qquad
e_{i,\pm}=zQ^{-2}E_{i,\pm},\qquad
g_{i,\pm}=G_{i,\pm},\qquad
\eta_i=z^3Q^{-6}V_i,
\]
from `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2637`.

## Where exact extraction stops

Define the actual first Frechet output matrices by
\[
\Lambda_{i,\pm}(z)
:=
D(G_\pm^{(0)}(z)^{-1/2})[\delta G_{i,\pm}^{\lin}(z)].
\]
The source gives the Loewner formula and scale estimates for this operator at
`C:/workspace/riemann2/rh/proof_of_rh.tex:1916-1969`, but it does not display
the \(z\)-coefficient expansion of \(\Lambda_{i,\pm}\).

Let
\[
M_i^{[5]}(z):=\text{the finite-grade \(5\) component of }\delta N_i^{\lin}(z).
\]
The source gives the linear mixed-block expression above, but it does not
display the grade-5 coefficient matrix \(M_i^{[5]}\) or the baseline/kernal
coefficients needed to extract it.

Thus the actual non-\((1,1)\) tag coefficient must be
\[
C_{112}^{L_1YR_1}
=
\pi_{\mathfrak f}[z^7]\left(
\Lambda_{1,-}M_1^{[5]}\Lambda_{2,+}
+\Lambda_{1,-}M_2^{[5]}\Lambda_{1,+}
+\Lambda_{2,-}M_1^{[5]}\Lambda_{1,+}
\right),
\]
with \(C_{122}^{L_1YR_1}\) given by swapping \(1\leftrightarrow2\).

The missing displayed source formula is exactly the coefficient list
\[
[z^r]\Lambda_{i,\pm}\quad\text{and}\quad [z^s]M_i^{[5]}
\quad (r+s+t=7)
\]
in the same normalization as \(B_7^{\mathfrak f}\), followed by the determinant
identity against \(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

Current source supplies estimates and bounded-baseline placeholders, not those
actual coefficient matrices.
