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

## Paired Finite-\(s\) Unit-Coordinate Chart and Conditional Slot Draft

Staged UV-017 text. Not promoted. This is a conditional matrix-level local
chart package, not exact paired construction and not UV-017 closure.

```tex
\begin{definition}[Paired finite-\(s\) unit-coordinate chart]
Fix \(m\in I\) and use the sign-audited boundary phase
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t).
\]
Define the abstract paired same-point and mixed chart blocks
\[
G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s),
\qquad
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
\]
by the finite-\(s\) block formulas of the zeta-side local model after
replacing the RH phase function \(\Ph(t)\) by
\(\Theta_\chi^{\mathrm{pair}}(t)\) and \(q\) by
\(q_\chi^{\mathrm{pair}}\). The quotient remains
\(\Phi_\chi^{\mathrm{pair}}(s)\). No further correction map is included in
this local chart; any additional correction must be named and checked for unit
value-coordinate derivative. More explicitly, for
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

\begin{hypothesis}[Paired chart realization and local admissibility]
Interpret \(B_\chi^{\mathrm{pair}}\) and \(S_\chi^{\mathrm{pair}}\) in the
completed-Hadamard normalization of the paired source package:
\[
B_\chi^{\mathrm{pair}}=B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0,
\qquad
S_\chi^{\mathrm{pair}}=S_{\chi,\mathrm{comp}}^{\mathrm{pair}}.
\]
Assume that the actual paired corrected finite-\(s\) local object is
represented by the preceding chart, with no further correction map. Assume a
local holomorphic paired phase on the required microscopic disk; if the theorem
is used uniformly in \(m\), assume the corresponding pole-clearance and
derivative-control radius. Assume same-point positivity and nondegeneracy,
for example the real-window spectral gap
\[
q_\chi^{\mathrm{pair}}(t)>0,\qquad
2q_\chi^{\mathrm{pair}}(t)q_\chi^{\mathrm{pair}\,\prime\prime}(t)
+4q_\chi^{\mathrm{pair}}(t)^4
-3q_\chi^{\mathrm{pair}\,\prime}(t)^2
\ge \kappa>0,
\]
or an equivalent lower spectral bound for the same-point blocks. Assume
holomorphic inverse-square-root whitening from this gap. Along the pure value
path, all
non-value coordinates--derivative, curvature, mixed-jet, background,
correction, multiplicity, cutoff, and normalization-gauge data--are frozen to
first order. If a scalar readout is taken after the matrix-level whitened
block, define the value derivative after that readout or separately prove that
the readout has unit derivative on the matrix value slot.
\end{hypothesis}

\begin{theorem}[Conditional paired matrix value-slot]
Assume the completed-Hadamard paired source package and the preceding paired
chart-realization and local-admissibility hypothesis. Let
\[
\mathcal F_{\chi,m,\sigma}(a,\eta)
\]
denote the post-whitened matrix-level local deformation in this chart, where
\[
a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)
\]
is the value coordinate and \(\eta\) denotes the frozen non-value coordinates.
Define
\[
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
:=
\partial_a\mathcal F_{\chi,m,\sigma}(0,\eta_0).
\]
For the actual paired data, put
\[
R_\chi^{\mathrm{pair}}(m,\sigma)
:=
\mathcal F_{\chi,m,\sigma}
\bigl(S_\chi^{\mathrm{pair}}(m),\eta_\chi(m)\bigr)
-\mathcal F_{\chi,m,\sigma}(0,\eta_0)
-S_\chi^{\mathrm{pair}}(m)
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma).
\]
Then the matrix-level corrected local deformation satisfies
\[
\Delta_\chi^{\mathrm{pair}}(m,\sigma)
=
S_\chi^{\mathrm{pair}}(m)
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
+R_\chi^{\mathrm{pair}}(m,\sigma).
\]
Moreover, along the pure value path \((a,\eta)=(\alpha,\eta_0)\), the
remainder has zero first derivative after the displayed value term is
subtracted:
\[
\left.
\frac{\partial}{\partial\alpha}
\left(
\mathcal F_{\chi,m,\sigma}(\alpha,\eta_0)
-\mathcal F_{\chi,m,\sigma}(0,\eta_0)
-\alpha A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
\right)
\right|_{\alpha=0}
=0.
\]
\end{theorem}
```

Remaining open work before UV-017 closure:

- prove that the actual paired corrected finite-\(s\) blocks realize the
  displayed chart, rather than assume it;
- promote the fixed-\(m\) holomorphy/removable-singularity lemma for the
  literal chart if the paper needs that lemma stated separately;
- prove a uniform microscopic pole-clearance radius if the later theorem needs
  one;
- prove the same-point determinant/spectral gap, or keep it as an explicit
  local whitening hypothesis;
- derive holomorphic inverse-square-root whitening from that gap;
- prove the derivative-form freeze-rule remainder criterion for the actual
  local object, not only inside the conditional chart theorem;
- if a downstream scalar readout is used, prove its derivative is normalized
  consistently with the matrix value slot.

Provenance:
`agents/20260424-192025-gap-uv017-coefficient-freeze/report.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md`;
`agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md`;
`agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-uv017-finite-s-formula-audit.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-uv017-conditional-theorem-framing-audit.md`;
`agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-holomorphy-positivity-whitening.md`;
`agents/20260424-183416-verifier-slot-skeleton/report-uv017-holomorphy-positivity-audit.md`;
`agents/20260424-183416-verifier-slot-skeleton/scripts/check_uv017_local_admissibility.py`.
