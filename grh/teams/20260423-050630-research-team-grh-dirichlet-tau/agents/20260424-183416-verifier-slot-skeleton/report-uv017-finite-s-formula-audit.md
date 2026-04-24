## Claim

The displayed paired finite-\(s\) chart formulas in `paper-updates.md` are
faithful literal substitutions of the RH finite-\(s\) same-point, mixed, and
whitened block formulas. I found no sign, \(t_\pm\), phase-gap, \(q_\pm\),
power of \(s\), \(1/\pi\), or transpose/asymmetry mismatch in the displayed
\(G\), \(N\), or \(\widehat\Omega\) formulas.

The staged text also now avoids the main overclaim from the previous audit: it
uses a `definition` titled "unit-coordinate chart hypothesis", says the blocks
are "given, in a local chart", and keeps the remaining construction,
holomorphy, positivity/whitening, freeze-rule, and scalar-readout burdens
outside the display. This verifies the formula-display subtask only. It does
not prove that the actual paired Dirichlet corrected blocks supply this chart
or close UV-017.

Honest verdict: formula audit passes. No entry correction is needed for the
displayed \(G\), \(N\), or whitened block.

## Status

proved

## Evidence

**Proved.**

- Same-point block: RH has
  \[
  G_{m,\pm}(s)=\frac1\pi
  \begin{pmatrix}
  2q(t_\pm)&\frac12q'(t_\pm)\\
  \frac12q'(t_\pm)&\frac1{12}(q''(t_\pm)+2q(t_\pm)^3)
  \end{pmatrix},
  \quad t_\pm=m\pm s/2.
  \]
  The staged paired display replaces \(q(t_\pm)\) by
  \(q_{\chi,\pm}^{\mathrm{pair}}(s)=q_\chi^{\mathrm{pair}}(t_\pm)\) and keeps
  \(\frac1\pi\), \(2q\), \(\frac12q'\), symmetry, and
  \(\frac1{12}(q''+2q^3)\). See `rh/proof_of_rh.tex:222-232`,
  `rh/proof_of_rh.tex:948-960`, and `paper-updates.md:163-190`.
- Mixed block: RH has
  \[
  N_m(s)=\frac1\pi
  \begin{pmatrix}
  -2\sin\Delta/s&
  (\sin\Delta+q_+s\cos\Delta)/s^2\\
  -(\sin\Delta+q_-s\cos\Delta)/s^2&
  ((q_-+q_+)s\cos\Delta+(2-q_-q_+s^2)\sin\Delta)/(2s^3)
  \end{pmatrix}.
  \]
  The staged paired display keeps the same signs, \(q_+\) in the upper-right,
  \(q_-\) in the lower-left, the lower-left minus sign, the \((2,2)\)
  numerator, \(2s^3\), and the global \(1/\pi\). See
  `rh/proof_of_rh.tex:234-253`, `rh/proof_of_rh.tex:1201-1215`, and
  `paper-updates.md:193-219`.
- Phase gap and endpoint convention: RH uses
  \(t_\pm=m\pm s/2\) and \(\Delta_m(s)=\Ph(t_-)-\Ph(t_+)\). The staged
  display uses the same orientation:
  \[
  \Delta_{\chi,m}^{\mathrm{pair}}(s)
  =\Theta_\chi^{\mathrm{pair}}(t_-)-\Theta_\chi^{\mathrm{pair}}(t_+).
  \]
  This is compatible with the pure value path producing
  \(\Delta_{\chi,0}^{\mathrm{pair}}(s)-\alpha s\). See
  `paper-updates.md:163-171` and `paper-updates.md:260-272`.
- Whitened block: RH uses left same-point block \(G_{m,-}^{-1/2}\), mixed
  block \(N_m\), and right same-point block \(G_{m,+}^{-1/2}\). The staged
  paired display exactly matches this left/right order. See
  `rh/proof_of_rh.tex:255-257`, `rh/proof_of_rh.tex:1407-1414`,
  `rh/proof_of_rh.tex:1518-1524`, and `paper-updates.md:221-229`.
- Scope control: `paper-updates.md` now frames the block display as a local
  chart hypothesis, not an unconditional paired construction. It explicitly
  leaves construction of the paired corrected finite-\(s\) blocks, microscopic
  holomorphy, same-point positivity/nondegeneracy, holomorphic whitening,
  derivative-form freeze rules, and scalar-readout normalization as remaining
  hypotheses. See `paper-updates.md:137-143`, `paper-updates.md:152-162`, and
  `paper-updates.md:276-284`.

**Conditional.**

- The formula pass is conditional only in the expected sense: these displays
  are correct as a definition or chart hypothesis. If "corrected" later means
  an additional paired correction map beyond literal substitution into these
  matrices, that map must still be named and separately checked for a unit
  value-coordinate derivative.
- The inverse-square-root expression is only a formal displayed block until
  same-point positivity/nondegeneracy and holomorphic whitening are assumed or
  proved. The staged text says "When the same-point blocks are positive
  definite," which is the right scope for the display.

**Missing.**

1. No missing entry in the displayed \(G\), \(N\), or whitened block formulas.
2. No proof yet that the actual paired Dirichlet corrected blocks are this
   chart; the staged statement remains a chart hypothesis.
3. No paired holomorphy/removable-singularity proof, positivity/nondegeneracy
   proof, or holomorphic inverse-square-root proof.
4. No derivative-form freeze-rule remainder theorem or scalar-readout
   normalization theorem.

No computation was run for this audit.

## Baseline / delta

Baseline: Sartre's prior construction-draft audit accepted the finite-\(s\)
unit-coordinate idea but rejected the wording as too implicit because the
paired \(G\) and \(N\) formulas were not displayed and "obtained from the
finite-\(s\) block formulas" could hide the correction maps.

Delta: the current staged text displays the matrices and has downgraded the
statement to a chart hypothesis/definition. This removes the display-formula
objection. The remaining UV-017 gap is now genuinely the advertised local
admissibility/construction gap, not a hidden sign or matrix-entry mismatch.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-162`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:163-190`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:193-229`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:230-272`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:276-284`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md:1-63`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md:84-108`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-paired-finite-s-formulas.md:158-176`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:7-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:30-89`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/paired_finite_s_formula_package.md:91-157`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md:1-34`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-construction-draft-audit.md:182-209`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1145-1215`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- Sign-audited paired boundary phase
  \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\)
  and \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\).
- The RH finite-\(s\) block formulas and their left/right convention
  \(t_\pm=m\pm s/2\).
- The staged choice to treat the paired displays as a local chart
  definition/hypothesis, not as an already-proved construction from Dirichlet
  data.
- Future paired local admissibility: holomorphy, removable singularities,
  same-point positivity/nondegeneracy, holomorphic whitening, freeze-rule
  remainder, and scalar-readout normalization.

## Strongest objection

The formulas are correct, but the word "corrected" remains a live scope risk.
If future text silently adds a correction map before or after these displayed
matrices, the current formula audit will no longer certify the value-coordinate
coefficient. The matrix-entry check only covers the literal local chart as
displayed.

## Needed for promotion

1. No formula correction is needed for \(G_{\chi,m,\pm}^{\mathrm{pair},
   \mathrm{corr}}\), \(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}\), or
   \(\widehat\Omega_{\chi}^{\mathrm{pair},\mathrm{corr}}\).
2. Keep the `definition`/`chart hypothesis` framing unless the actual paired
   construction is proved.
3. Add a guard sentence if promoted: "No further correction map is included in
   this local chart; any additional correction must be separately checked for
   unit value-coordinate derivative."
4. Minor notation cleanup only: in the phase-gap path line, replace the
   post-definition `:=` by `=` after
   \(\Delta_{\chi,0}^{\mathrm{pair}}(s)\) has already been defined. This is not
   a matrix-entry correction.
5. Continue to require paired holomorphy/whitening and scalar-readout checks
   before any UV-017 closure claim.

## Autoresearch next step

continue: audit whether the local chart hypothesis plus UV-016 completed
source package is enough to state a clean conditional UV-017 theorem, with the
remaining holomorphy/whitening/freeze/readout hypotheses explicitly separated.

verify: if the coordinator adds any correction map around the displayed
matrices, re-run this audit against that map's first value-coordinate
derivative; the current pass covers only literal substitution.

Ledger destination: `attempts.md` as a kept verifier pass and
`collation.md/no-action` for formula corrections, since no displayed
\(G\), \(N\), or whitened-block entry needs correction. UV-017 remains open.
