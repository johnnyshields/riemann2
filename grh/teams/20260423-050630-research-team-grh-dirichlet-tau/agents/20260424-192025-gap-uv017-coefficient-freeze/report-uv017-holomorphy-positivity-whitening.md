## Claim

For the displayed paired finite-\(s\) chart, fixed-midpoint holomorphy and
removable singularities can be proved from the literal formulas once
\(q_\chi^{\mathrm{pair}}\) is taken as the local holomorphic
logarithmic-derivative source and \(\Theta_\chi^{\mathrm{pair}}\) as a local
holomorphic primitive. The same-point block formulas themselves do not prove
positivity. Positivity/nondegeneracy reduces to an explicit finite determinant
gap, and holomorphic inverse-square-root whitening follows from that gap by the
same functional-calculus mechanism as in the RH draft.

Honest verdict: UV-017 is still open. The local-admissibility subgap is now a
sharp finite list: local holomorphic paired phase on the required microscopic
disk, same-point determinant/spectral gap, holomorphic whitening, derivative
freeze-rule remainder, and scalar-readout normalization if the theorem leaves
matrix level.

## Status

open

## Evidence

**Proved.**

- Fixed \(m\). Since \(\Xi_\chi\) is entire and the staged source package
  excludes \(2im\) and \(1+2im\) from \(Z(\Xi_\chi)\), the logarithmic
  derivative
  \[
  D_\chi(t)=\Xi_\chi'(1+2it)/\Xi_\chi(1+2it)
  -\Xi_\chi'(2it)/\Xi_\chi(2it)
  \]
  is holomorphic on some complex neighborhood of \(m\). On the real interval,
  the staged source convention identifies \(q_\chi^{\mathrm{pair}}\) with this
  function. A local holomorphic primitive supplies the paired phase.
- With such a phase, \(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s)\) is
  holomorphic because its entries are polynomials in
  \(q(m\pm s/2)\), \(q'(m\pm s/2)\), and \(q''(m\pm s/2)\).
- For the mixed block, \(\Delta(s)=\Theta(m-s/2)-\Theta(m+s/2)\) is holomorphic
  and odd. The derivative relation \(q=\Theta'\) forces the apparent pole
  numerators to vanish to the required orders:
  \[
  \sin\Delta=O(s),\quad
  \sin\Delta+q(m\pm s/2)s\cos\Delta=O(s^2),
  \]
  and the \((2,2)\) numerator is \(O(s^3)\). Thus the displayed \(N\) entries
  extend holomorphically through \(s=0\).
- The unit value-coordinate calculation is preserved by these admissibility
  checks. Along
  \[
  \Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
  =\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m),
  \]
  one still has \(q_\alpha=q_0+\alpha\), frozen \(q'\), frozen \(q''\),
  phase-gap variation \(-\alpha s\), and
  \(d(q_\alpha(m)-B_\chi^{\mathrm{pair}}(m))/d\alpha=1\) with \(B\) frozen.

**Conditional.**

- A uniform microscopic disk \(|s|<\rho_0/Q\) over a range of \(m\)'s does not
  follow merely from fixed-\(m\) holomorphy. It needs a pole-clearance and
  derivative-control hypothesis for the paired edge logarithmic derivatives.
- Same-point positivity is conditional on an explicit spectral gap. At \(s=0\),
  with \(q_j=q_\chi^{\mathrm{pair}\,(j)}(m)\), the real boundary same-point
  block is positive definite exactly if
  \[
  q_0>0,\qquad 2q_0q_2+4q_0^4-3q_1^2>0.
  \]
  A uniform version should require this determinant gap, or an equivalent
  spectral gap, on the real microscopic window and then a small-variation
  condition on the complex \(s\)-disk.
- Holomorphic inverse-square-root whitening follows once the same-point blocks
  are holomorphic and their spectra stay away from \(0\). This is a conditional
  functional-calculus consequence, not an independent source theorem.
- Matrix-level whitening does not rescale the source coefficient: its
  derivative is by definition \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\). A
  downstream scalar readout still needs a separate unit-normalization check.

**Missing / unsupported.**

- From the displayed formulas and staged source package alone, same-point
  positivity/nondegeneracy is unsupported. Formula-shape positivity is false
  from this scope alone: for a general local phase with
  \(q(t)=1+K(t-m)\), the displayed \(G(m,0)\) has determinant negative for
  large \(K\).
- No proved uniform microscopic pole-clearance radius is currently supplied
  for the paired phase.
- No derivative-form freeze-rule remainder theorem is supplied.
- No scalar-readout normalization theorem is supplied.

No computation was run for this report; the determinant and removable
singularity checks are direct algebra from the displayed formulas.

## Baseline / delta

Baseline: prior reports had reduced UV-017 to a displayed finite-\(s\) chart
with unit value coordinate, while Sartre's formula audit found no entry-level
mismatch. The remaining advertised gap was local admissibility:
holomorphy/removable singularities, positivity/nondegeneracy, whitening,
freeze-rule remainder, and scalar readout.

Delta: this report proves the fixed-\(m\) holomorphy/removable-singularity part
for the literal chart and gives the exact same-point determinant gap needed for
positivity. It also separates fixed-\(m\) holomorphy from a uniform
microscopic radius. The positivity and whitening burden is now a sharp
finite hypothesis, not a vague "needs admissibility" clause.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-73`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-162`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:163-229`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:230-284`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:7-62`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:64-101`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:103-120`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/holomorphy_positivity_whitening_reduction.md:122-158`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-finite-s-formula-audit.md`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- Staged completed-Hadamard source package and sign-audited paired boundary
  convention.
- Literal finite-\(s\) paired chart formulas.
- Local edge-zero exclusion at the midpoint, and a stronger pole-clearance
  hypothesis if uniform microscopic radius is needed.
- Same-point determinant/spectral gap:
  \(q>0\) and \(2qq''+4q^4-3(q')^2\ge \kappa>0\) on the real microscopic
  window, or an equivalent nondegeneracy statement.
- Holomorphic functional calculus for inverse square roots once the spectral
  gap is available.
- Derivative-form freeze-rule remainder and scalar-readout unit normalization
  before any UV-017 promotion.

## Strongest objection

Same-point positivity is not a formal consequence of the displayed block
formulas or the staged source theorem. The determinant condition contains
\(q'\) and \(q''\), so positivity can fail for a general local phase even when
\(q>0\). Therefore any wording that derives paired whitening from the source
identity alone would overclaim. The correct next theorem layer must either
prove this determinant gap from paired Dirichlet data or state it as an
explicit local whitening hypothesis.

## Needed for promotion

1. Add a fixed-\(m\) holomorphy/removable-singularity lemma for the displayed
   paired chart, using the local holomorphic logarithmic derivative and
   primitive.
2. If the theorem needs uniform microscopic control, add a pole-clearance and
   derivative-control hypothesis giving a disk \(|s|<\rho_0/Q\).
3. State or prove the same-point gap:
   \(q>0\) and \(2qq''+4q^4-3(q')^2\ge\kappa>0\), or an equivalent spectral
   gap for \(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}\).
4. Derive holomorphic inverse-square-root whitening from that spectral gap by
   functional calculus.
5. Add the derivative-form freeze-rule remainder criterion and scalar-readout
   normalization check. UV-017 cannot close before these are in place.

## Autoresearch next step

continue: attack the determinant/spectral-gap condition for the paired source
kernel. The sharp target is whether
\[
2qq''+4q^4-3(q')^2>0
\]
can be proved from the completed paired strip-edge source on the microscopic
window, or whether it must remain an explicit local whitening hypothesis.

verify: ask an adversarial verifier to check the removable-singularity order
claims and the determinant condition against the displayed \(G\) and \(N\)
formulas.

## Ledger destination

`attempts.md` as a kept gap reduction for UV-017; `uv.md` should retain UV-017
open with the narrowed missing hypotheses. A reusable finding may be captured:
fixed-\(m\) holomorphy/removable singularities are formal for the literal chart,
but same-point positivity reduces to the explicit determinant gap and is not
proved by the source package alone.
