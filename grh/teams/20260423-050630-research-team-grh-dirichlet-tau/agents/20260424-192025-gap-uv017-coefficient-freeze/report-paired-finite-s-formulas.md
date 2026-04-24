## Claim

The paired finite-\(s\) same-point and mixed block formulas can be displayed by
literal substitution from the RH finite-\(s\) block formulas as a local chart
package. With
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t),
\]
and \(t_\pm=m\pm s/2\), put
\[
q_{\chi,\pm}^{\mathrm{pair}}(s):=q_\chi^{\mathrm{pair}}(t_\pm),
\qquad
\Delta_{\chi,m}^{\mathrm{pair}}(s)
:=\Theta_\chi^{\mathrm{pair}}(t_-)-\Theta_\chi^{\mathrm{pair}}(t_+).
\]
Then the literal same-point chart is
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
\left(q_\chi^{\mathrm{pair}\,\prime\prime}(t_\pm)
+2q_{\chi,\pm}^{\mathrm{pair}}(s)^3\right)
\end{pmatrix},
\]
and the literal mixed chart is
\[
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
:=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)}{s}
&
\dfrac{\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,+}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)}{s^2}
\\[2ex]
-\dfrac{\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,-}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)}{s^2}
&
\dfrac{
\left(q_{\chi,-}^{\mathrm{pair}}(s)+q_{\chi,+}^{\mathrm{pair}}(s)\right)
s\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
+\left(2-q_{\chi,-}^{\mathrm{pair}}(s)q_{\chi,+}^{\mathrm{pair}}(s)s^2\right)
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)}
{2s^3}
\end{pmatrix}.
\]
This closes the display-formula subtask, but not UV-017. The formulas are safe
as a definition or explicit local chart hypothesis. They are not yet a proof
that the actual paired Dirichlet corrected blocks supply this chart.

## Status

open

## Evidence

**Proved.**

- The formula package in `notes/paired_finite_s_formula_package.md` displays
  the paired same-point matrix, mixed matrix, and whitened block by direct
  substitution from the RH finite-\(s\) model.
- The unit-coordinate path in the same note gives
  \(q_{\chi,\alpha}^{\mathrm{pair}}=q_{\chi,0}^{\mathrm{pair}}+\alpha\),
  freezes \(q'\) and \(q''\), changes the phase gap by \(-\alpha s\), and gives
  \(da/dS_\chi^{\mathrm{pair}}|_{\alpha=0}=1\) when
  \(B_\chi^{\mathrm{pair}}(m)\) is frozen.
- These displays answer the narrow construction-draft objection that the
  paired finite-\(s\) matrices had not been written out.

**Conditional.**

- The displays prove only a literal local chart package. Promotion as a theorem
  about the actual paired Dirichlet construction requires either defining these
  matrices to be the paired corrected blocks or supplying correction maps that
  reduce to these formulas.
- The paired whitened block
  \[
  \widehat\Omega_{\chi}^{\mathrm{pair},\mathrm{corr}}
  =
  G_{\chi,m,-}^{-1/2}N_{\chi,m}G_{\chi,m,+}^{-1/2}
  \]
  is meaningful only under same-point positivity/nondegeneracy sufficient for
  holomorphic inverse square roots.

**Missing.**

1. A construction or definition declaring the displayed matrices to be the
   actual corrected paired local blocks.
2. Microscopic holomorphy and removable singularity control for the paired
   phase on the \(s\)-disk.
3. Same-point positivity/nondegeneracy and holomorphic inverse-square-root
   whitening.
4. A derivative-form freeze-rule remainder criterion.
5. Scalar-readout normalization if UV-017 leaves the matrix level.

No computation was run for this report.

## Baseline / delta

Baseline: `report-unit-coordinate-chart.md` proved \(da/dS|_0=1\) for the
universal RH finite-\(s\) phase-kernel chart, but left the paired finite-\(s\)
matrices unwritten. Sartre's construction-draft audit therefore kept the
objection that "obtained from RH finite-\(s\) formulas" was too implicit.

Delta: `notes/paired_finite_s_formula_package.md` now writes the paired
\(G\), \(N\), and \(\widehat\Omega\) formulas explicitly. The remaining
obstruction is no longer absence of displayed formulas; it is whether these
formulas are adopted as definitions/hypotheses for the actual paired corrected
blocks, or whether additional correction maps must be named.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:7-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:30-89`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:91-139`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:141-157`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:1-41`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md:1-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md:173-193`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-216`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1145-1215`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- Sign-audited paired boundary phase and
  \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\).
- The RH finite-\(s\) block formulas.
- Frozen \(B_\chi^{\mathrm{pair}}(m)\) on the pure value path.
- A choice to treat the displayed matrices either as the definition of the
  paired corrected local chart or as an explicit hypothesis.
- Paired holomorphy, positivity/nondegeneracy, holomorphic whitening, derivative
  freeze-rule remainder, and scalar-readout checks before UV-017 promotion.

## Strongest objection

The word "corrected" is still doing work. If the actual paired corrected blocks
mean literal substitution into the RH finite-\(s\) formulas, the displayed
matrices provide the chart. If "corrected" includes additional paired
correction maps, those maps have not been named here and could reintroduce the
hidden scalar UV-017 is trying to exclude.

## Needed for promotion

1. Decide whether the displayed matrices are definitions of the paired local
   chart or hypotheses about the paired construction.
2. If they are definitions, state that no further correction map is present at
   this chart level.
3. If they are not definitions, name the correction maps and prove that their
   value-coordinate derivative has unit coefficient.
4. Add the holomorphy/positivity/whitening hypothesis block.
5. Add the derivative-form freeze-rule remainder criterion and scalar-readout
   normalization check before any UV-017 closure claim.

## Autoresearch next step

continue: convert the displayed package into a theorem-facing
`Definition/Hypothesis (paired finite-\(s\) local chart)` and then ask a
verifier to check whether any intended correction map remains unnamed.

verify: audit the use of "corrected" in the paired chart against the RH
corrected block construction; the only question is whether literal
substitution is a definition or whether extra maps must be tracked.
