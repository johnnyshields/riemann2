## Claim

Noether's reduction is sound with one important scope refinement: UV-017 has
indeed been reduced to the paired unit-coordinate local normal-form problem,
provided the theorem is kept at the matrix-level corrected whitened block and
the pure value coordinate is proved to be the actual source scalar to first
order. The staged UV-016 source theorem removes the sign/factor ambiguity, and
matrix whitening is not a separate scalar-renormalization site once
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) is defined as the derivative of the
post-whitened block with respect to the chosen local value coordinate.

The two adversarial failure modes remain exactly where Noether places them:

1. the local coordinate may be
   \(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)+O(S^2)\), not the unit coordinate;
2. a downstream scalar readout applied after the matrix-level expansion may
   rescale the matrix slot unless its derivative is explicitly included in the
   definition of \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) or separately checked.

The pure value freeze rule is a useful non-tautological test only if it includes
the actual source-to-coordinate derivative \(da/dS|_{S=0}=1\) and proves that
non-value coordinates have zero first variation along that pure source path. If
one merely defines \(R\) after subtracting a chosen linear term, the identity is
tautological and does not close UV-017.

Honest verdict: keep Noether's reduction. It does not close UV-017, but it
sharpens the missing theorem to a unit-coordinate normal-form lemma plus a
scalar-readout normalization check if any downstream scalar functional is used.

## Status

open

## Evidence

**Proved.**

- UV-016 now fixes the source sign/factor in the completed-Hadamard convention:
  \(\Phi=e^{-2i\Theta}\), \(q=\Theta'\), and
  \(q=-\frac12\Phi'/\Phi\), with
  \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\). Thus the source scalar itself
  no longer supplies a hidden factor of \(2\), sign change, or background
  scalar. See `paper-updates.md:16-87` and
  `agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:7-23`.
- The prior UV-017 verifier already isolated the same obstruction: the
  coefficient must be fixed independently, with exact freeze rules and no
  scalar renormalization. See
  `agents/20260424-183416-verifier-slot-skeleton/report.md:1-18` and
  `:145-175`.
- Noether's matrix-level lemma is valid as local algebra. If
  \(\mathcal F_{\chi,m,\sigma}(a,\eta)\) is holomorphic and
  \(a=S_\chi^{\mathrm{pair}}(m)\) is the actual zeroth value coordinate while
  \(\eta\) contains frozen non-value data, then
  \(A_{\mathrm{val},\chi}^{\mathrm{pair}}=\partial_a\mathcal F(0,\eta_0)\)
  gives the stated first-order coefficient. See
  `agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:25-87`.
- Matrix whitening is not a scalar-renormalization site under that definition.
  The whitening map can change the matrix derivative, but that changed matrix
  derivative is exactly what \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) denotes.
  Any factor inside the post-whitening derivative is absorbed into
  \(A_{\mathrm{val}}\), not into the scalar coefficient.

**Conditional.**

- The statement that source sign/factor and matrix whitening are no longer
  scalar-renormalization sites is conditional on using the staged completed
  source theorem and on defining \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) at
  the same post-whitened matrix level as \(\Delta_\chi^{\mathrm{pair}}\).
- The exclusion of \(c_\chi(m)S_\chi^{\mathrm{pair}}\) requires a real test of
  the actual local chart:
  \[
  a(S,\eta(S))=S_\chi^{\mathrm{pair}}(m)+O(S^2)
  \]
  with unit first derivative. If the local construction only proves
  \(a=c_\chi(m)S+O(S^2)\), the coefficient is
  \(c_\chi(m)A_{\mathrm{val},\chi}^{\mathrm{pair}}\).
- The freeze rule is non-tautological only when it says which coordinates are
  held fixed and proves their first variation vanishes on the pure source path.
  The displayed equality with
  \(R=\mathcal F(S,\eta_\chi)-\mathcal F(0,\eta_0)-SA_{\mathrm{val}}\) is by
  itself a residual definition.
- If the promoted UV-017 statement applies a scalar functional after the
  matrix expansion, then the scalar derivative must be included:
  either define the scalar \(A_{\mathrm{val}}\) as the derivative after readout,
  or prove the readout has unit normalization on the matrix value slot.

**Missing.**

- A paired local construction proving that the corrected same-point and mixed
  blocks are built from the same \(\Theta_\chi^{\mathrm{pair}}\) as the source
  package and use the zeroth coordinate
  \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\) with
  \(da/dS=1\).
- A paired holomorphic-whitening package: microscopic holomorphy,
  same-point positivity/nondegeneracy, holomorphic inverse-square-root
  whitening, and value-parameter differentiability. This is still explicit in
  the paired hypotheses and whitening notes.
- A scalar-readout normalization lemma if the final target is not exactly the
  matrix-level corrected whitened block.

No computation was run for this audit.

## Baseline / delta

Baseline: prior UV-017 audits left a broad coefficient-normalization gap:
source sign, freeze rules, local coordinate choice, whitening, and possible
readout normalization could all hide a scalar factor.

Delta: after UV-016 source normalization, the sign/factor and completed-source
background are no longer plausible scalar-renormalization sites. Noether's
reduction correctly concentrates UV-017 on the unit-coordinate chart
\(S_\chi^{\mathrm{pair}}(m)\mapsto a\). This audit sharpens the caveat that the
pure freeze rule must test the actual source-to-coordinate derivative, not only
define a residual.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-62`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:16-87`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:3-42`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:50-79`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:80-99`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:101-115`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:164-191`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:7-23`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:25-87`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:89-107`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:109-144`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:1-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:83-105`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:145-175`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:31-59`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:7-19`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:21-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/whitening_interface.md:7-28`

## Dependencies

- UV-016 completed-Hadamard source package with sign-audited convention.
- A paired corrected local family built from the same boundary phase
  \(\Theta_\chi^{\mathrm{pair}}\).
- A holomorphic local chart \(\mathcal F_{\chi,m,\sigma}(a,\eta)\) whose value
  coordinate satisfies \(da/dS|_{S=0}=1\).
- Explicit freeze rule: derivative, mixed-jet, curvature, background,
  multiplicity, cutoff/correction, and normalization-gauge coordinates are
  non-value directions and are frozen for the pure value derivative.
- Same-point positivity/nondegeneracy and holomorphic whitening for the paired
  corrected blocks.
- Scalar-readout normalization if the theorem moves beyond the matrix-level
  \(\Delta_\chi^{\mathrm{pair}}\).

## Strongest objection

Noether's lemma can be made tautological if the unit-coordinate hypothesis is
not separately proved. Defining
\[
R_\chi^{\mathrm{pair}}
=\mathcal F(S,\eta_\chi)-\mathcal F(0,\eta_0)
-S A_{\mathrm{val}}
\]
always yields the displayed identity. What matters is the independent chart
statement that the actual paired local coordinate has unit derivative with
respect to the source scalar and that no non-value coordinate contributes to
the pure first variation.

## Needed for promotion

1. State UV-017 as a conditional local normal-form lemma with hypotheses:
   paired corrected blocks, unit coordinate \(a=S_\chi^{\mathrm{pair}}(m)\),
   non-value coordinates \(\eta\), holomorphy, same-point
   positivity/nondegeneracy, and holomorphic whitening.
2. Include the adversarial unit test
   \(a(S,\eta(S))=S+O(S^2)\), not merely \(a=c_\chi(m)S+O(S^2)\).
3. Define \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) at the same level as
   \(\Delta_\chi^{\mathrm{pair}}\): matrix-level if \(\Delta\) is matrix-level,
   scalar-after-readout if \(\Delta\) is scalar-level.
4. Require a scalar-readout check if any downstream functional is applied after
   the matrix whitening expansion.
5. Keep UV-017 separate from UV-016; source normalization is an input, not a
   proof of the unit-coordinate chart.

## Autoresearch next step

continue: attack the paired unit-coordinate chart directly by writing the local
block coordinates in terms of \(\Theta_\chi^{\mathrm{pair}}\) and proving that
the zeroth coordinate has derivative \(1\) with respect to
\(S_\chi^{\mathrm{pair}}(m)\) while all non-value coordinates are frozen.

verify: if a scalar readout is proposed, audit its Fréchet derivative on
\(A_{\mathrm{val},\chi}^{\mathrm{pair}}\) before allowing the coefficient
claim to leave the matrix level.
