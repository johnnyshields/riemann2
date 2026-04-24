# Corrected package object map

## Baseline sources read

- `findings.md:105-118`: current C obstruction is package-level coincidence; patch transitions for the affine lift are base-controlled, fiber selection remains.
- `dispatch.md:103-106`: assignment asks for the most explicit definition of `\mathfrak P^{\corr}_2=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`, fixed codomain, and missing swap / one-amplitude / diagonal merger data.
- `proof_of_rh.tex:7004-7062`: one-pair fixed-sector package `(c,A_5^{\mathfrak f},\Delta_7)`; raw `(u_7,v_7)` not canonical.
- `proof_of_rh.tex:11368-11450`: target `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` and scaling law.
- `proof_of_rh.tex:11888-12189`: abstract finite-dimensional package lemma with swap symmetry, one-amplitude collapse, and diagonal merger; current draft says these are still open for the actual corrected two-atom package.
- Prior reports `20260424-145000-corrected-package-object`, `20260424-143000-reduced-package-object`, `20260424-143000-C-proof-obligations`, `20260424-145000-Bmkappa-killer`.

## Object map

[confirmed] The fixed codomain supported by current sources is
\[
V_C=\mathbf C\times\mathfrak f\times\mathbf C,
\qquad \mathfrak f=\operatorname{span}\{I,S\}.
\]
A theorem-ready corrected two-atom object would be
\[
\mathfrak P^{\corr}_2(m,\omega,\delta)=
(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
\in V_C,
\qquad A^{\mathfrak f,\corr}=U^{\corr}I+V^{\corr}S.
\]

[confirmed] The reduction map is
\[
\mathcal R(C,UI+VS,\Delta)=\left(U/C,V/C,\Delta/C^2\right),\qquad C\ne0.
\]
The corrected reduced package is intended to be
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P^{\corr}_2.
\]

[confirmed] The desired C identity, in blow-up coordinates `2\omega=\kappa\delta`, is
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

## C-FS map

- C-FS1: define / construct the analytic corrected exceptional-divisor package in fixed codomain and prove reduced extension to `\delta=0`.
- C-FS2: prove no extra C-codomain state survives after reduction beyond the trace `B(m,\kappa)`; current sources do not prove this, but the codomain choice removes raw septic representatives by design.
- C-FS3: prove diagonal merger / slope-independence `B(m,\kappa)=B_0(m)` for the actual corrected package; current sources explicitly leave this open.
- C-FS4: identify the common value with `\widehat\Psi(m)` using one-amplitude collapse / merged one-pair compatibility and the scaling law.

## Negative boundary

[confirmed] Scalar normalization is not diagonal collapse. The map `\mathcal R` gives amplitude-invariant comparison but does not prove that the actual corrected package merges on the diagonal. Analyticity and swap-evenness in the blow-up chart allow an arbitrary trace `B(m,\kappa)`.
