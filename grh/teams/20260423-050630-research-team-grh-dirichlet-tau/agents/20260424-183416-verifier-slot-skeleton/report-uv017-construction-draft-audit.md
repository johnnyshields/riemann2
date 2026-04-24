## Claim

The staged paired finite-\(s\) unit-coordinate draft correctly reflects
Noether's result only as a conditional local chart statement. The sign and
unit-coordinate calculation match the audited source convention and the RH
finite-\(s\) formulas: with
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\,\prime},
\]
the pure value path
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
=\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m)
\]
gives \(q_{\chi,\alpha}^{\mathrm{pair}}=q_{\chi,0}^{\mathrm{pair}}+\alpha\),
freezes \(q'\) and \(q''\), and changes the phase gap by \(-\alpha s\). Thus,
if the paired corrected blocks are literally the RH finite-\(s\) phase-kernel
blocks in these variables and \(B_\chi^{\mathrm{pair}}\) is frozen, the local
coordinate \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\) has unit
first derivative with respect to the source slot.

The draft is not promotion-ready as a theorem about the actual paired
Dirichlet construction. The phrase "corrected paired same-point and mixed
blocks are obtained from the finite-\(s\) block formulas" is too strong and too
implicit unless the correction maps are defined or the statement is framed as
an explicit definition/hypothesis. As written, it can be safely used as a
staged hypothesis layer, not as a proved UV-017 construction lemma.

Honest verdict: keep the draft direction, but demote the theorem label or add
the missing formulas. It does not close UV-017.

## Status

open

## Evidence

**Proved.**

- The sign convention in the staged draft matches the audited UV-016 interface:
  \(e^{-2i\Theta_\chi^{\mathrm{pair}}}\) and
  \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\). The source
  theorem immediately above also records
  \(q_\chi^{\mathrm{pair}}=-\frac12\Phi'/\Phi\) on the boundary, so the draft
  does not reintroduce the old positive-exponent sign error. See
  `paper-updates.md:144-151` and `paper-updates.md:28-40`.
- The RH finite-\(s\) same-point formulas use only \(q(t_\pm)\), \(q'(t_\pm)\),
  and \(q''(t_\pm)\), and the mixed block uses
  \(\Delta_m(s)=\Ph(t_-)-\Ph(t_+)\) and \(q_\pm=q(t_\pm)\). See
  `rh/proof_of_rh.tex:222-257`, `rh/proof_of_rh.tex:948-979`, and
  `rh/proof_of_rh.tex:1145-1215`.
- Noether's calculation proves the universal formal chart: adding
  \(\alpha(t-m)\) to the phase adds \(\alpha\) to \(q\), gives zero
  \(\alpha\)-variation in \(q'\) and \(q''\), and changes the phase gap by
  \(-\alpha s\). The staged draft reproduces this at
  `paper-updates.md:165-186`; Noether's source is
  `notes/unit_coordinate_chart_attack.md:7-46`.
- The draft does not claim GRH, does not claim exact slot realization, and
  lists the remaining UV-017 hypotheses: literal construction, microscopic
  holomorphy, same-point positivity/nondegeneracy, holomorphic whitening, a
  derivative-form freeze rule, and scalar-readout normalization. See
  `paper-updates.md:139-140` and `paper-updates.md:190-198`.

**Conditional.**

- The unit-coordinate conclusion is valid only after the paired corrected
  blocks are defined at the same level as the RH finite-\(s\) matrices. In the
  RH manuscript, corrected blocks are not just a slogan; they are finite-\(s\)
  matrices built from corrected \(q\) and corrected phase data, with separate
  holomorphy and positivity arguments. See `rh/proof_of_rh.tex:1497-1524` and
  `rh/proof_of_rh.tex:1392-1457`.
- The line
  \[
  \left.\frac{d a}{d S_{\chi}^{\mathrm{pair}}}\right|_{\alpha=0}=1
  \]
  is meaningful only after defining the pathwise source
  \(S_{\chi,\alpha}^{\mathrm{pair}}(m)
  :=q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\), with
  \(B_\chi^{\mathrm{pair}}\) frozen and the background normalized so
  \(q_{\chi,0}^{\mathrm{pair}}(m)=B_\chi^{\mathrm{pair}}(m)\) if \(\alpha\)
  is to be identified with \(S\) rather than only with \(dS/d\alpha\).
- The phrase "replace \(\Phi\) with \(\Theta_\chi^{\mathrm{pair}}\)" needs
  disambiguation. In the RH finite-\(s\) formulas, \(\Ph\) is the real boundary
  phase function. In the paired source theorem,
  \(\Phi_\chi^{\mathrm{pair}}\) names the quotient. The theorem text should say
  "replace the RH phase function \(\Ph(t)\), not the quotient
  \(\Phi_\chi^{\mathrm{pair}}(s)\), by
  \(\Theta_\chi^{\mathrm{pair}}(t)\)."
- The frozen-coordinate list is directionally right, but should explicitly
  include all non-value coordinates from the prior reduction: derivative,
  mixed-jet/phase-gap background, curvature, background/source-background,
  correction, multiplicity, cutoff, and normalization-gauge data.

**Missing.**

1. Explicit paired correction maps or displayed formulas for
   \(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s)\) and
   \(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)\). Without these, "obtained
   from the finite-\(s\) block formulas" is an assumption, not a construction.
2. A definition of \(S_{\chi,\alpha}^{\mathrm{pair}}(m)\) along the pure value
   path and a statement that \(B_\chi^{\mathrm{pair}}\) is frozen on that path.
3. A baseline clause if the statement wants \(S_{\chi,\alpha}^{\mathrm{pair}}
   (m)=\alpha\), rather than only \(d a/dS=1\): namely
   \(q_{\chi,0}^{\mathrm{pair}}(m)=B_\chi^{\mathrm{pair}}(m)\).
4. The holomorphy/whitening package remains a hypothesis, not a consequence of
   the finite-\(s\) substitution. This matches the notes and should remain
   explicit.
5. The freeze-rule remainder criterion and scalar-readout normalization are
   still outside the displayed lemma.

No computation was run for this audit.

## Baseline / delta

Baseline: Noether reduced UV-017 to the paired unit-coordinate chart. Sartre's
prior audit accepted that reduction but kept two failure modes live:
\(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)+O(S^2)\) and a downstream scalar readout
that rescales the matrix-level slot.

Delta: the staged draft captures the finite-\(s\) unit-coordinate calculation
but still lacks theorem-grade definitions of the paired corrected blocks. This
audit narrows the wording fix: either display the actual paired finite-\(s\)
matrices and correction maps, or label the statement as a local chart
hypothesis/definition. Without that change, the draft overstates construction.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:137-187`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:190-198`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:28-40`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-67`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:1-41`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:73-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md:170-198`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/unit_coordinate_chart_attack.md:7-46`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/unit_coordinate_chart_attack.md:61-99`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:1-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:119-140`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-29`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:21-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/whitening_interface.md:13-28`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1145-1215`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:5665-5790`

## Dependencies

- UV-016 completed-Hadamard source convention with
  \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\)
  and \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\).
- Literal paired finite-\(s\) block definitions, or an explicit local chart
  hypothesis saying the paired blocks are defined by those formulas.
- A frozen \(B_\chi^{\mathrm{pair}}(m)\) and pathwise source
  \(S_{\chi,\alpha}^{\mathrm{pair}}(m)
  =q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\).
- Microscopic holomorphy, same-point positivity/nondegeneracy, and holomorphic
  inverse-square-root whitening for the paired corrected blocks.
- Freeze-rule remainder condition and scalar-readout normalization if UV-017
  proceeds beyond the matrix-level local chart.

## Strongest objection

The draft's central hypothesis currently names undefined corrected paired
blocks and says they are "obtained" from RH finite-\(s\) formulas. That wording
can be read as a proved construction of the actual paired local object, but the
record only proves the universal formal calculation. Until the correction maps
are displayed or the statement is renamed as a definition/hypothesis, the
claim can still hide the very scalar mismatch UV-017 is meant to exclude.

## Needed for promotion

Smallest concrete wording edits:

1. Change the environment title from a theorem-like construction lemma to
   `Hypothesis/Definition (Paired finite-\(s\) unit-coordinate chart)`, or
   display the actual formulas for
   \(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}\) and
   \(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}\).
2. Replace "are obtained from the finite-\(s\) block formulas" by either
   "we define them by the following finite-\(s\) formulas" or "assume a local
   chart in which they are given by the following finite-\(s\) formulas."
3. Disambiguate the phase notation: replace the RH phase function \(\Ph(t)\)
   by \(\Theta_\chi^{\mathrm{pair}}(t)\), while the quotient remains
   \(\Phi_\chi^{\mathrm{pair}}(s)\).
4. Define
   \(S_{\chi,\alpha}^{\mathrm{pair}}(m)
   :=q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\), state
   that \(B_\chi^{\mathrm{pair}}(m)\) is frozen, and add
   \(q_{\chi,0}^{\mathrm{pair}}(m)=B_\chi^{\mathrm{pair}}(m)\) if the text
   identifies \(S_{\chi,\alpha}^{\mathrm{pair}}(m)\) with \(\alpha\).
5. Define
   \(\Delta_{\chi,0}^{\mathrm{pair}}(s)
   :=\Theta_{\chi,0}^{\mathrm{pair}}(m-s/2)
   -\Theta_{\chi,0}^{\mathrm{pair}}(m+s/2)\) before using it, and use equality
   rather than a defining `:=` on the left-hand phase-gap line.
6. Keep the remaining-hypotheses paragraph. It is necessary and correctly
   prevents an accidental UV-017 or GRH promotion.

## Autoresearch next step

continue: draft the minimal replacement wording as a hypothesis/definition
with displayed \(G\) and \(N\) formulas copied from the RH finite-\(s\) model,
then separately state the unit-coordinate derivative corollary.

verify: after that rewrite, check whether the displayed corrected paired
blocks still leave any hidden scalar in the post-whitened matrix derivative or
in a later scalar readout.

Ledger destination: `paper-updates.md` for the wording edits above, and
`attempts.md` as a kept verifier reduction; no `uv.md` change, since UV-017
already records this construction gap.
