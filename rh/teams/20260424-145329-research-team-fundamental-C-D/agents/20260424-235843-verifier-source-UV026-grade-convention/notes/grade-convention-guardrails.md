# UV-026 Scalar Grade-Projection Guardrails

## Verdict

From the inspected current source alone, do not identify the UV-026 scalar
\(\operatorname{Gr}_5 r_i\) with either:

- the \(q^{(5)}\)/\(X_3\) quintic witness slice; or
- the \(q^{(7)}\)/\(X_5\) direct septic witness slice.

Both are source-supported matrix-slice facts in one-pair witness arguments, but
neither is defined as a scalar grade projection on the affine-removed source
remainder \(r_i\) before \(\Phi_K\) and in the
\(B_7^{\mathfrak f}\) normalization.

Likewise, do not identify scalar \(\operatorname{Gr}_1 r_i\) with the
\(\eta_2\)/\(X_1\) off-diagonal slice as a theorem from current source alone.
The source supports \(\eta_2\) as the off-diagonal \(X_1\) input in the witness
sections, but it does not define a scalar \(\operatorname{Gr}_1\) projection on
\(r_i\) before whitening.

## Source-Supported Facts

- `C:/workspace/riemann2/rh/proof_of_rh.tex:6535-6654`: on the quintic witness
  slice \((K_1,\eta_2,q^{(5)})\), \(q^{(5)}\) first appears in the cubic
  same-point coefficient \(G_3\), and its linear contribution to \(X_3\) is
  diagonal.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7656-7842`: on the direct septic
  slice \((K_1,\eta_2,q^{(7)})\), \(q^{(7)}\) first appears in the quintic
  same-point coefficient \(G_5\), and its linear contribution to \(X_5\) is
  diagonal.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6579-6587`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:7766-7772`, and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:23850-23895`: the \(\eta_2\) slice
  of \(X_1\) is off-diagonal in the witness computations.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`: UV-026 needs
  coefficient lists for \(\Lambda_{i,\pm}\) and \(M_i^{[5]}\), but does not
  define the scalar source projection producing \(M_i^{[5]}\).

## Guardrails

1. A scalar grade theorem must define \(\operatorname{Gr}_1\) and
   \(\operatorname{Gr}_5\) on the affine-removed scalar source remainder
   \(r_i\), not on a later whitened matrix coefficient.
2. The definition must be before \(\Phi_K\), before determinant scalarization,
   and in the normalization feeding
   \[
   B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7].
   \]
3. The theorem must say whether \(\operatorname{Gr}_5\) means the
   \(q^{(5)}\)/\(X_3\) slice, the \(q^{(7)}\)/\(X_5\) slice, or another
   mixed-block scalar grading, and prove compatibility with
   \(M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})\).
4. Matrix witnesses can motivate candidate projections, but cannot define
   scalar source grades unless a source theorem proves the pullback from scalar
   \(r_i\)-jets through same-point/mixed formulas and whitening.
5. The projection must commute with midpoint affine removal, or it must be
   defined after affine removal.  Otherwise the Stage 1 generator assumption
   \((r_i^{[a]})(m)=(r_i^{[a]})'(m)=0\) is not source-supported.
6. A valid theorem must state the full derivative input it supplies:
   \[
   (r_i^{[a]})^{(k)}(m),\qquad a\in\{1,5\},\quad 2\le k\le9,
   \]
   in ordinary \(z\) after \(s=z/Q^2\).

## Sharp Missing Theorem

Define scalar projections \(\operatorname{Gr}_1\) and \(\operatorname{Gr}_5\)
on the affine-removed one-pair source remainder \(r_i\), in ordinary \(z\),
with source tags retained, before \(\Phi_K\), and in the
\(B_7^{\mathfrak f}\) normalization.  Prove that the projected scalar
remainders generate the intended matrix inputs
\[
\delta G_{i,\pm}^{\lin,[1/5]},\qquad
M_i^{[1/5]}=\operatorname{Gr}_{1/5}(\mathfrak D_Q\delta N_i^{\lin})
\]
used by the Stage 1 generator.  The theorem must explicitly choose the
grade-five convention or prove that the competing \(q^{(5)}\)/\(X_3\) and
\(q^{(7)}\)/\(X_5\) labels are transformed into a single scalar convention.
