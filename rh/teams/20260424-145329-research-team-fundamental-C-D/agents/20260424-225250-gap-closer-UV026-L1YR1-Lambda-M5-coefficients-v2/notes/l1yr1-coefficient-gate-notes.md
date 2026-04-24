# L1YR1 Coefficient Gate Notes

## Fixed Harness

Target: UV-026 first gate `L_1YR_1` for the source-bidegree corrected-whitening
gauge.

Ground truth check:
\[
C_{112}^{L_1YR_1}, C_{122}^{L_1YR_1}\in \mathbf C A_5^{\mathfrak f}(m)
\]
before \(\Phi_K\), determinant scalarization, quotient extraction, or diagonal
merger.

Canonical source already records the narrowed target at
`rh/proof_of_rh.tex:12617-12714`.  It names
\[
\Lambda_{i,\pm}(z)=
D(G_\pm^{(0)}(z)^{-1/2})[\delta G_{i,\pm}^{\lin}(z)]
\]
and \(M_i^{[5]}(z)=\sum_s M_{i,s}^{[5]}z^s\), then gives the two tag
expressions \(C_{112}^{L_1YR_1}\) and \(C_{122}^{L_1YR_1}\).  The same remark
states that the coefficient lists and determinant identities remain missing.

## Source-Level Formulas Actually Derivable

From the same-point block formula at `rh/proof_of_rh.tex:2688-2722`, the
source-linear same-point perturbation is
\[
H_{i,\pm}:=\delta G_{i,\pm}^{\lin}
=
\frac1\pi
\begin{pmatrix}
2d_{i,\pm} & \frac12 e_{i,\pm}\\
\frac12 e_{i,\pm} &
\frac1{12}(g_{i,\pm}+6q_{0,\pm}^2d_{i,\pm})
\end{pmatrix}.
\]

From the mixed block formula at `rh/proof_of_rh.tex:2724-2784`, set
\[
s=z/Q^2,\qquad c_0=\cos\Delta_0,\qquad s_0=\sin\Delta_0.
\]
The linearized mixed perturbation before any grade-five projection is
\[
\delta N_i^{\lin}
=\frac1\pi
\begin{pmatrix}
-2c_0\eta_i/s &
(c_0\eta_i+sc_0d_{i,+}-s q_{0,+}s_0\eta_i)/s^2\\
-(c_0\eta_i+sc_0d_{i,-}-s q_{0,-}s_0\eta_i)/s^2 &
\mathcal M_{22}
\end{pmatrix},
\]
where
\[
\mathcal M_{22}
=
\frac{
(sc_0-s^2q_{0,+}s_0)d_{i,-}
+(sc_0-s^2q_{0,-}s_0)d_{i,+}
+\bigl(-(q_{0,-}+q_{0,+})ss_0+(2-q_{0,-}q_{0,+}s^2)c_0\bigr)\eta_i
}{2s^3}.
\]

Thus a positive coefficient theorem can define
\[
M_i^{[5]}=\operatorname{Gr}_5(\delta N_i^{\lin})
\]
or, if the scaled input \(Y=\mathfrak D_Q(\delta N)\) is intended,
\[
M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin}).
\]
The current text names \(M_i^{[5]}\) but does not display this coefficient list
or fix this normalization at the \(B_7^{\mathfrak f}\) gate.

## Frechet Coefficient Recurrence

Let
\[
B_\pm(z)=G_\pm^{(0)}(z)^{-1/2}=\sum_{a=0}^7B_{\pm,a}z^a+O(z^8),
\]
\[
S_\pm(z)=G_\pm^{(0)}(z)^{1/2}=\sum_{a=0}^7S_{\pm,a}z^a+O(z^8),
\]
and
\[
H_{i,\pm}(z)=\sum_{b=0}^7H_{i,\pm,b}z^b+O(z^8).
\]
The derivative \(\Lambda_{i,\pm}=D(G_\pm^{(0)}{}^{-1/2})[H_{i,\pm}]\) is
characterized by differentiating \(BGB=I\):
\[
S_\pm\Lambda_{i,\pm}+\Lambda_{i,\pm}S_\pm=-B_\pm H_{i,\pm}B_\pm.
\]
Therefore, recursively for \(0\le r\le7\),
\[
S_{\pm,0}\Lambda_{i,\pm,r}+\Lambda_{i,\pm,r}S_{\pm,0}
=
-\sum_{a+b+c=r}B_{\pm,a}H_{i,\pm,b}B_{\pm,c}
-\sum_{a=1}^r
\bigl(S_{\pm,a}\Lambda_{i,\pm,r-a}
+\Lambda_{i,\pm,r-a}S_{\pm,a}\bigr).
\]
Since \(S_{\pm,0}\) has positive spectrum, the Sylvester equation is uniquely
solvable.  This is an exact coefficient-list reduction: once \(B_{\pm,a}\),
\(S_{\pm,a}\), and \(H_{i,\pm,b}\) are supplied through order \(7\), the
\(\Lambda_{i,\pm,r}\) list is determined.

## C112/C122 Data Needed

The script
`scripts/l1yr1_coefficient_gate.py` computes the finite bookkeeping.  Through
ordinary \(z^7\), the gate needs:

- \(\Lambda_{i,\pm,r}\) for \(i=1,2\), signs \(\pm\), and \(0\le r\le7\):
  \(32\) matrices.
- \(M_{i,s}^{[5]}\) for \(i=1,2\) and \(0\le s\le7\): \(16\) matrices.
- \(36\) triples \((r,s,t)\) with \(r+s+t=7\) for each ordered product.
- \(108\) matrix products for each of \(C_{112}\) and \(C_{122}\).

The exact convolution is
\[
C_{112}^{L_1YR_1}
=\pi_{\mathfrak f}
\sum_{r+s+t=7}
\bigl(
\Lambda_{1,-,r}M_{1,s}^{[5]}\Lambda_{2,+,t}
+\Lambda_{1,-,r}M_{2,s}^{[5]}\Lambda_{1,+,t}
+\Lambda_{2,-,r}M_{1,s}^{[5]}\Lambda_{1,+,t}
\bigr),
\]
and
\[
C_{122}^{L_1YR_1}
=\pi_{\mathfrak f}
\sum_{r+s+t=7}
\bigl(
\Lambda_{1,-,r}M_{2,s}^{[5]}\Lambda_{2,+,t}
+\Lambda_{2,-,r}M_{1,s}^{[5]}\Lambda_{2,+,t}
+\Lambda_{2,-,r}M_{2,s}^{[5]}\Lambda_{1,+,t}
\bigr).
\]

After writing
\[
C_{112}=u_{112}I+v_{112}S,\qquad C_{122}=u_{122}I+v_{122}S,
\]
promotion requires
\[
u_{112}v_5-u_5v_{112}=0,\qquad u_{122}v_5-u_5v_{122}=0.
\]

## Exact Missing Theorem

The current source is insufficient for a positive `L_1YR_1` gate.  The exact
missing theorem/formula is:

For the tagged two-atom pre-whitening block in the \(B_7^{\mathfrak f}\)
normalization, display the order-\(\le7\) coefficient lists
\[
[z^r]G_\pm^{(0)}(z)^{-1/2},\quad
[z^r]G_\pm^{(0)}(z)^{1/2},\quad
[z^r]\delta G_{i,\pm}^{\lin}(z),
\]
derive \([z^r]\Lambda_{i,\pm}\) by the Sylvester recurrence above, display the
grade-five mixed coefficient list \([z^s]M_i^{[5]}\), and verify the two
determinant identities against the same-basis
\(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

This is sharper than the prior absence result: the coefficient recurrence and
finite convolution are now explicit, but the actual source coefficient lists
are still not present.
