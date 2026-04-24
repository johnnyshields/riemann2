## Claim

UV-017 can be reduced to a precise unit-coordinate local normal-form lemma.
With the staged UV-016 completed-Hadamard source theorem, the source scalar is
already normalized as
\[
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(m)
=q_\chi^{\mathrm{pair}}(m)
\]
because \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) and the sign/factor
convention is fixed by
\[
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t)
=-\frac12\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}
{\Phi_\chi^{\mathrm{pair}}}\!\left(\tfrac12+it\right).
\]
Thus no extra scalar comes from the staged source normalization.

The remaining local question is exactly whether the paired corrected local
blocks use this same \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\)
as their zeroth value coordinate. If a paired holomorphic jet chart has zeroth
coordinate
\[
a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)
\]
and the pure value path freezes all non-value coordinates, then the RH draft's
local algebra gives
\[
\Delta_\chi^{\mathrm{pair}}(m,\sigma)
=
S_\chi^{\mathrm{pair}}(m)
A_{\mathrm{val},\chi}^{\mathrm{pair}}(m,\sigma)
+R_\chi^{\mathrm{pair}}(m,\sigma)
\]
with unit coefficient. A replacement \(c_\chi(m)S_\chi^{\mathrm{pair}}(m)\)
would fail the same pure-value derivative test unless \(c_\chi(m)=1\), provided
the tested value-channel derivative is nonzero.

Honest verdict: this is a theorem-ready conditional coefficient/freeze lemma,
not an unconditional closure. The current blocker is the paired
unit-coordinate jet chart, not the completed source scalar.

## Status

open

## Evidence

**Proved.**

- The staged source theorem fixes the paired boundary phase, the bridge from
  \(\Phi'/\Phi\) to \(q\), and \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\).
  In that completed normalization the source scalar is \(S=q\), with no hidden
  sign or factor of \(2\).
- The RH local template defines the pure value derivative by
  \(q_1=q_2=B+\alpha\) while derivative and curvature data are frozen. Thus the
  coefficient of the pure value path is the path parameter \(\alpha\).
- The RH corrected decomposition expands the holomorphic whitening map around
  background value \(S(m)=0\), and the first-order whitening formula is linear
  in the three first-order block variations. Matrix whitening itself does not
  introduce a scalar renormalization once the value coordinate is fixed.

**Conditional on a paired unit-coordinate jet chart.**

- If the paired corrected same-point and mixed blocks are holomorphic functions
  of a local coordinate \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\)
  plus frozen non-value coordinates \(\eta\), then defining
  \[
  A_{\mathrm{val},\chi}^{\mathrm{pair}}
  :=\partial_a\mathcal F_{\chi,m,\sigma}(0,\eta_0)
  \]
  gives the exact coefficient/freeze lemma in
  `notes/coefficient_freeze_reduction.md`.
- Under the pure value path \((a,\eta)=(\alpha,\eta_0)\), the remainder has
  zero first derivative after subtracting
  \(\alpha A_{\mathrm{val},\chi}^{\mathrm{pair}}\). This is the
  non-tautological test that excludes \(c_\chi(m)S_\chi^{\mathrm{pair}}\).

**Missing.**

1. Paired unit-coordinate jet chart: prove that the corrected paired local
   blocks are built from the same boundary phase
   \(\Theta_\chi^{\mathrm{pair}}\) and have zeroth coordinate exactly
   \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\), not
   \(c_\chi(m)(q-B)\).
2. Paired parameter holomorphy and whitening: prove holomorphy in the value
   coordinate and non-value coordinates, plus same-point
   positivity/nondegeneracy for inverse-square-root whitening.
3. Freeze-rule remainder criterion: state that derivative, mixed-jet,
   curvature, background, multiplicity, and normalization-gauge variations are
   non-value directions; they may enter \(R_\chi^{\mathrm{pair}}\), but not the
   pure value derivative defining \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\).
4. Scalar readout boundary: if the promoted statement reads a downstream scalar
   from the matrix block, check separately that this scalar functional adds no
   new normalization factor. This is outside the matrix-level coefficient lemma
   but is a real overclaim risk.

No scripts were needed; this was a local algebra and normalization reduction.

## Baseline / delta

Baseline: the prior UV-017 skeleton and verifier already identified the hidden
risk: the displayed identity is tautological unless the coefficient is fixed
independently, with explicit freeze rules and no scalar renormalization.

Delta: the obstruction is now localized to a single map,
\[
S_\chi^{\mathrm{pair}}(m)\mapsto a,
\]
from the staged source scalar to the paired local zeroth value coordinate. The
matrix whitening and source sign/factor conventions are not the remaining
renormalization sites. If \(a=S_\chi^{\mathrm{pair}}(m)\), the coefficient is
unit; if \(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)+O(S^2)\), the coefficient is
\(c_\chi(m)\).

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-52`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:28-40`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:68-88`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:8-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:83-105`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report.md:145-175`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md:3-35`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md:43-64`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-084758-paired-normalization-compat-routeB/report.md:5-20`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-084758-paired-normalization-compat-routeB/report.md:33-39`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:13-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:25-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_aval.md:7-13`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:13-29`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:28-31`
- `rh/proof_of_rh.tex:285-288`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:1640-1679`
- `rh/proof_of_rh.tex:5665-5790`
- `rh/proof_of_rh.tex:2381-2385`
- `rh/proof_of_rh.tex:6129-6208`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:25-87`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:89-107`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:109-144`

## Dependencies

- The staged UV-016 completed-Hadamard paired source theorem with its
  sign-audited boundary phase and \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\).
- A paired corrected local family built from the same boundary phase
  \(\Theta_\chi^{\mathrm{pair}}\).
- A paired unit-coordinate jet chart whose zeroth coordinate is exactly
  \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\).
- Value-parameter holomorphy or joint holomorphy in the local coordinates.
- Same-point positivity/nondegeneracy and holomorphic inverse-square-root
  whitening for the paired corrected blocks.
- A declared freeze-rule remainder criterion separating pure value variation
  from non-value jet/background/gauge variations.

## Strongest objection

The current record still has no proof that the paired local normal form uses the
staged source scalar as a unit coordinate. A local construction could silently
choose
\[
a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)
\]
or could read the source scalar only upstairs before applying a different
downstairs normalization. The RH algebra would then faithfully produce the
coefficient of \(a\), not prove that \(a=S_\chi^{\mathrm{pair}}(m)\). This is
the exact remaining UV-017 obstruction.

## Needed for promotion

1. State a paired coefficient/freeze lemma using the unit-coordinate chart in
   `notes/coefficient_freeze_reduction.md:25-87`.
2. Prove or explicitly assume that the paired corrected blocks are constructed
   from \(\Theta_\chi^{\mathrm{pair}}\) with value coordinate
   \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\).
3. Install the paired holomorphic-whitening hypothesis block: microscopic
   holomorphy, same-point positivity/nondegeneracy, inverse square roots, and
   value-parameter differentiability.
4. Add the freeze-rule criterion that \(R_\chi^{\mathrm{pair}}\) has zero pure
   value derivative after subtracting
   \(S_\chi^{\mathrm{pair}}A_{\mathrm{val},\chi}^{\mathrm{pair}}\).
5. If a scalar functional is used after the matrix expansion, add a separate
   normalization check for that scalar readout.

## Autoresearch next step

continue: Try to prove the paired unit-coordinate jet chart directly from the
RH finite-\(s\) block formulas by replacing \(\Phi\) with
\(\Theta_\chi^{\mathrm{pair}}\) and tracking the coordinates
\((q(m),q'(m),q''(m),\ldots)\).

verify: Ask an adversarial verifier to test the lemma against two failure
modes: \(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)\) and a downstream scalar
functional that rescales the matrix-level slot.

blocked: No coordinator action is needed unless the next pass is meant to
promote a paper lemma; then the coordinator must decide whether UV-017 may be
stated with the unit-coordinate chart as an explicit hypothesis or requires a
full paired local construction first.
