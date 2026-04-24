# Paper Updates

Staged coordinator text for the GRH Dirichlet-tau resume team. Not applied to
any canonical paper. Current status: mathematically verifier-cleared for the
completed-Hadamard source package, with citation quality still requiring a
coordinator promotion decision.

## Completed-Hadamard Paired Source Package Draft

Proposed replacement for the Stage 1 source-package wording in
`paper/dirichlet_paired_source_package_candidate.tex` and the corresponding
Stage 1 paragraph in `paper/dirichlet_paired_source_candidate.tex`.

```tex
\section{Completed paired source package}

Let \(\chi\) be a primitive nonprincipal Dirichlet character. Put
\[
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\qquad
\Phi_\chi^{\mathrm{pair}}(s):=
\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}.
\]
Let \(I\subset\mathbb R\) be compact and assume that
\[
2it\notin Z(\Xi_\chi),\qquad 1+2it\notin Z(\Xi_\chi)
\]
for every \(t\in I\). On \(I\) choose a real \(C^1\) boundary phase by
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t).
\]
Equivalently,
\[
q_\chi^{\mathrm{pair}}(t)
=-\frac12
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}
{\Phi_\chi^{\mathrm{pair}}}\!\left(\tfrac12+it\right).
\]

Define
\[
D_\chi(t):=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
With this boundary convention \(D_\chi(t)\) is real; we keep the real-part
notation below to display the scalar kernel identity. Then
\(q_\chi^{\mathrm{pair}}(t)=\Re D_\chi(t)\), and
\[
\Re D_\chi(t)
=
\Re\sum_{\rho\in Z(\Xi_\chi)}
m_\rho
\left(
\frac{1}{1+2it-\rho}
-\frac{1}{2it-\rho}
\right),
\]
where the sum runs over distinct zeros \(\rho\) of \(\Xi_\chi\), and
\(m_\rho\) is analytic multiplicity in the product
\(\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\overline\chi)\).
The series converges absolutely and uniformly on \(I\), and the same is true
after any fixed number of \(t\)-derivatives.

Thus, in the completed-Hadamard normalization,
\[
q_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
=B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
+S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t),
\qquad
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=0,
\]
with
\[
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
:=
\Re\sum_{\rho\in Z(\Xi_\chi)}
m_\rho
\left(
\frac{1}{1+2it-\rho}
-\frac{1}{2it-\rho}
\right).
\]
Here again the sum is over distinct completed zeros of \(\Xi_\chi\), with
analytic multiplicity supplied by \(m_\rho\).
```

Proposed raw-bookkeeping remark, separate from the theorem:

```tex
\begin{remark}[Raw \(L\)-factor bookkeeping]
The preceding source package uses completed zeros of
\(\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\overline\chi)\), counted by
analytic multiplicity. In that normalization there is no additional gamma,
trivial-zero, pole, conductor, or Hadamard-exponential background term. If one
rewrites the same identity using raw \(L(s,\chi)\) and
\(L(s,\overline\chi)\) zeros only, the gamma, trivial-zero, pole, and
raw-Hadamard edge-difference terms must be placed in a separate raw
background. They must not be added to the completed-zero theorem, or the source
statement mixes two normalizations.
\end{remark}
```

Citation stack for a working-paper draft:

- Primitive nonprincipal completed \(L\)-function package:
  DLMF \(\S 25.15(i)\)-\((ii)\), especially \((25.15.1)\),
  \((25.15.5)\)-\((25.15.6)\), \((25.15.7)\)-\((25.15.9)\). Define the
  paper's \(\Lambda(s,\chi)\) explicitly and derive the parity-normalized
  completed form in text.
- Order-one Hadamard product, zero summability, and logarithmic derivative:
  either cite a clean Davenport/Montgomery-Vaughan source, or include a short
  order-one derivation from DLMF \((25.15.3)\), DLMF \((25.15.5)\), and
  Stirling's formula in DLMF \(\S 5.11(i)\), then cite a standard
  complex-analysis Hadamard factorization theorem such as Conway,
  `Functions of One Complex Variable I`, Ch. XI, \(\S 3\).
- \(L(1,\chi)\ne0\) and the zero-at-origin exclusion:
  DLMF \((25.15.9)\) plus the functional equation; keep a finite-factor clause
  if a broader variant ever permits \(\rho=0\).

Bibliography upgrade still open:

- Verify exact Davenport or Montgomery-Vaughan page/equation references for a
  final textbook-grade citation package. This is not a hard blocker for a
  working-paper draft if the DLMF-plus-Hadamard stack above is used carefully.

Provenance:
`agents/20260424-183416-explorer-background-multiplicity/report-background-split.md`;
`agents/20260424-183416-gap-compact-regularization/report-source-audit.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md`;
`agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md`;
`agents/20260424-183416-gap-compact-regularization/report-citation-fallback-plan.md`.

## Paired Finite-\(s\) Unit-Coordinate Chart Hypothesis Draft

Staged UV-017 text. Not promoted. This is a construction/hypothesis layer for
the paired local chart, not exact slot realization.

```tex
\begin{definition}[Paired finite-\(s\) unit-coordinate chart hypothesis]
Fix \(m\in I\) and use the sign-audited boundary phase
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t).
\]
Assume that the corrected paired same-point and mixed blocks
\[
G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s),
\qquad
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
\]
are given, in a local chart, by the finite-\(s\) block formulas of the
zeta-side local model after replacing the RH phase function \(\Ph(t)\) by
\(\Theta_\chi^{\mathrm{pair}}(t)\) and \(q\) by
\(q_\chi^{\mathrm{pair}}\). The quotient remains
\(\Phi_\chi^{\mathrm{pair}}(s)\). More explicitly, for
\(t_\pm=m\pm s/2\), put
\[
q_{\chi,\pm}^{\mathrm{pair}}(s):=
q_\chi^{\mathrm{pair}}(t_\pm),
\qquad
\Delta_{\chi,m}^{\mathrm{pair}}(s):=
\Theta_\chi^{\mathrm{pair}}(t_-)
-\Theta_\chi^{\mathrm{pair}}(t_+).
\]
The local chart uses
\[
G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s)
:=
\frac1\pi
\begin{pmatrix}
2q_{\chi,\pm}^{\mathrm{pair}}(s)
&
\frac12 q_\chi^{\mathrm{pair}\,\prime}(t_\pm)
\\[1ex]
\frac12 q_\chi^{\mathrm{pair}\,\prime}(t_\pm)
&
\frac1{12}
\left(
q_\chi^{\mathrm{pair}\,\prime\prime}(t_\pm)
+2q_{\chi,\pm}^{\mathrm{pair}}(s)^3
\right)
\end{pmatrix}
\]
and
\[
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
:=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)}{s}
&
\dfrac{
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,+}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{s^2}
\\[2ex]
-\dfrac{
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,-}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{s^2}
&
\dfrac{
\left(q_{\chi,-}^{\mathrm{pair}}(s)+q_{\chi,+}^{\mathrm{pair}}(s)\right)
s\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
+\left(
2-q_{\chi,-}^{\mathrm{pair}}(s)q_{\chi,+}^{\mathrm{pair}}(s)s^2
\right)
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{2s^3}
\end{pmatrix}.
\]
When the same-point blocks are positive definite, define the paired whitened
block by
\[
\widehat\Omega_{\chi}^{\mathrm{pair},\mathrm{corr}}(s;m)
:=
G_{\chi,m,-}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
G_{\chi,m,+}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}.
\]
Use the local value coordinate
\[
a=q_\chi^{\mathrm{pair}}(m)
-B_\chi^{\mathrm{pair}}(m).
\]
Let the pure value path on the microscopic window be
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
=\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m),
\qquad
q_{\chi,\alpha}^{\mathrm{pair}}(t)
=q_{\chi,0}^{\mathrm{pair}}(t)+\alpha,
\]
with derivative, curvature, background, correction, multiplicity, cutoff, and
normalization-gauge coordinates frozen. Define the pathwise source coordinate
\[
S_{\chi,\alpha}^{\mathrm{pair}}(m)
:=q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m),
\]
with \(B_\chi^{\mathrm{pair}}(m)\) frozen on the path. If the baseline is
chosen so that \(q_{\chi,0}^{\mathrm{pair}}(m)=B_\chi^{\mathrm{pair}}(m)\),
then \(S_{\chi,\alpha}^{\mathrm{pair}}(m)=\alpha\). In any case, the local
coordinate
\[
a(\alpha)=q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)
\]
satisfies the unit derivative relation
\[
\left.\frac{d a}{d S_{\chi}^{\mathrm{pair}}}\right|_{\alpha=0}=1.
\]
Writing
\[
\Delta_{\chi,0}^{\mathrm{pair}}(s)
:=\Theta_{\chi,0}^{\mathrm{pair}}(m-s/2)
-\Theta_{\chi,0}^{\mathrm{pair}}(m+s/2),
\]
the phase-gap variation along this path is
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(m-s/2)
-\Theta_{\chi,\alpha}^{\mathrm{pair}}(m+s/2)
=
\Delta_{\chi,0}^{\mathrm{pair}}(s)-\alpha s.
\]
\end{definition}
```

Remaining hypotheses before UV-017 promotion:

- construct the paired corrected finite-\(s\) blocks literally as above;
- prove microscopic holomorphy, same-point positivity/nondegeneracy, and
  holomorphic inverse-square-root whitening for those paired blocks;
- state the freeze-rule remainder criterion as a derivative condition, not
  only as the definition of \(R_\chi^{\mathrm{pair}}\);
- if a downstream scalar readout is used, prove its derivative is normalized
  consistently with the matrix value slot.

Provenance:
`agents/20260424-192025-gap-uv017-coefficient-freeze/report.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md`;
`agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md`;
`agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md`.
