## Claim

The unit-coordinate obstruction \(da/dS|_0=1\) is provable for the universal
RH finite-\(s\) phase-kernel block model, but it is not yet proved for the
actual paired theorem because the paired corrected local blocks have not been
installed as literal substitutions into those formulas.

Formal result: for any local phase \(\Theta\), with \(q=\Theta'\), define the
pure value path
\[
\Theta_\alpha(t)=\Theta_0(t)+\alpha(t-m),
\qquad q_\alpha(t)=q_0(t)+\alpha.
\]
Then \(q_\alpha(t_\pm)\) varies with derivative \(1\), \(q_\alpha'\) and
\(q_\alpha''\) have zero \(\alpha\)-variation, and
\[
\Delta_{\alpha,m}(s)
=\Theta_\alpha(t_-)-\Theta_\alpha(t_+)
=\Delta_{0,m}(s)-\alpha s.
\]
Thus, if the local source coordinate is
\[
a=q(m)-B(m)
\]
with \(B(m)\) frozen, then \(S(\alpha)=q_\alpha(m)-B(m)=\alpha\), so
\[
\frac{da}{dS}\bigg|_0=1.
\]

Honest verdict: this proves the unit coordinate for the formal finite-\(s\)
phase-kernel construction. It reduces the actual paired obstruction to the
smallest missing local construction statement: prove that
\(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}\) and
\(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}\) are exactly the RH finite-\(s\)
blocks with \(\Ph=\Theta_\chi^{\mathrm{pair}}\),
\(q=q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\), value coordinate
\(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\), and pure value path
\(q_{\chi,\alpha}^{\mathrm{pair}}=q_{\chi,0}^{\mathrm{pair}}+\alpha\) with
non-value coordinates frozen. UV-017 is not closed because the paired
finite-\(s\) construction, holomorphy/whitening, freeze-rule remainder
criterion, and scalar-readout boundary remain missing.

## Status

open

## Evidence

**Proved.**

- The RH finite-\(s\) same-point block uses
  \(q(t_\pm)\), \(q'(t_\pm)\), and \(q''(t_\pm)\), and the mixed block uses
  \(q(t_\pm)\) and \(\Delta_m(s)=\Ph(t_-)-\Ph(t_+)\). These formulas contain no
  additional source-to-coordinate scalar.
- Along the artificial pure value path
  \(\Theta_\alpha(t)=\Theta_0(t)+\alpha(t-m)\), the finite-\(s\) inputs vary as
  \[
  \partial_\alpha q_\alpha(t_\pm)=1,\qquad
  \partial_\alpha q_\alpha'(t_\pm)=
  \partial_\alpha q_\alpha''(t_\pm)=0,\qquad
  \partial_\alpha\Delta_{\alpha,m}(s)=-s.
  \]
  Hence the local zeroth coordinate \(a=q(m)-B(m)\) has unit derivative with
  respect to \(S=q(m)-B(m)\), provided \(B(m)\) is frozen.
- This matches the RH pure value-channel rule \(q_1=q_2=B+\alpha\) with
  derivative and curvature data frozen and phase gap
  \(\Delta=\Delta_0-\alpha\sigma\).
- Sartre's audit requires exactly this test: the real chart must satisfy
  \(a(S,\eta(S))=S+O(S^2)\), with non-value coordinates having zero first
  variation on the pure source path. The formal finite-\(s\) calculation
  supplies that test for the universal phase-kernel model.

**Conditional.**

- If the paired corrected blocks are defined by literal finite-\(s\)
  substitution from the sign-audited paired phase
  \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\),
  then \(da/dS|_0=1\) follows at the matrix-block level.
- If the promoted theorem uses a downstream scalar functional rather than the
  matrix-level corrected whitened block, this result only controls the matrix
  coordinate; the scalar readout still needs its own unit-normalization check.

**Missing.**

1. Paired finite-\(s\) construction statement: the actual
   \(G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}\) and
   \(N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}\) must be defined as the RH
   finite-\(s\) formulas with \(\Ph=\Theta_\chi^{\mathrm{pair}}\) and
   \(q=q_\chi^{\mathrm{pair}}\).
2. Paired pure source path statement:
   \(q_{\chi,\alpha}^{\mathrm{pair}}(t)
   =q_{\chi,0}^{\mathrm{pair}}(t)+\alpha\) on the microscopic window, with
   derivative, curvature, background, correction, multiplicity, and gauge
   coordinates frozen.
3. Paired holomorphy/whitening: microscopic holomorphy, same-point
   positivity/nondegeneracy, holomorphic inverse square roots, and
   value-parameter differentiability remain hypotheses rather than proved
   paired facts.
4. Freeze-rule remainder criterion: after subtracting
   \(S_\chi^{\mathrm{pair}}A_{\mathrm{val},\chi}^{\mathrm{pair}}\), the
   remainder must have zero pure value derivative, not merely be defined
   residually.
5. Scalar-readout boundary: any post-whitening scalar functional must be
   checked separately for unit normalization on the value slot.

No scripts were needed; this was a local formula chase.

## Baseline / delta

Baseline: my previous reduction and Sartre's audit put all remaining
renormalization pressure on the local chart map
\[
S_\chi^{\mathrm{pair}}(m)\mapsto a
\]
and required \(da/dS|_0=1\) plus frozen non-value coordinates.

Delta: this pass proves \(da/dS|_0=1\) for the universal finite-\(s\)
phase-kernel chart by direct substitution into the RH block variables. The gap
is therefore no longer "does the RH finite-\(s\) chart have unit coordinate?"
It does. The gap is "has the paired corrected local object been constructed as
that chart?"

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:3-42`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report.md:80-99`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:25-46`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/coefficient_freeze_reduction.md:124-140`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:3-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:68-93`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md:145-170`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:13-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:25-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_aval.md:7-21`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/whitening_interface.md:13-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:13-29`
- `rh/proof_of_rh.tex:222-257`
- `rh/proof_of_rh.tex:446-469`
- `rh/proof_of_rh.tex:948-979`
- `rh/proof_of_rh.tex:1145-1215`
- `rh/proof_of_rh.tex:1392-1457`
- `rh/proof_of_rh.tex:1497-1613`
- `rh/proof_of_rh.tex:1640-1679`
- `rh/proof_of_rh.tex:2381-2385`
- `rh/proof_of_rh.tex:5665-5790`
- `rh/proof_of_rh.tex:6129-6208`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/unit_coordinate_chart_attack.md:7-46`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/unit_coordinate_chart_attack.md:50-59`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/unit_coordinate_chart_attack.md:61-99`

## Dependencies

- Sign-audited paired boundary phase
  \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\)
  and \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\).
- Literal paired finite-\(s\) block construction from the RH formulas.
- Local value coordinate
  \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\).
- Pure value path adding a constant \(\alpha\) to \(q\) on the microscopic
  window, equivalently adding \(\alpha(t-m)\) to the phase.
- Frozen non-value coordinate list: derivative, curvature, background,
  correction, multiplicity, cutoff, and normalization-gauge coordinates.
- Holomorphic paired whitening interface and scalar-readout normalization if
  the theorem proceeds beyond matrix level.

## Strongest objection

The actual paired corrected local blocks are still not on disk as formulas.
Without that construction, the proof above is only a universal phase-kernel
calculation. A paired theorem could still hide the factor by defining its local
coordinate as \(a=c_\chi(m)S_\chi^{\mathrm{pair}}(m)\), or by passing through a
post-whitening scalar functional that rescales the matrix value slot. The
finite-\(s\) formulas rule out those factors only after the paired object is
declared to use them literally and at the same matrix/scalar level as
\(\Delta_\chi^{\mathrm{pair}}\).

## Needed for promotion

1. Add a paired finite-\(s\) construction lemma: with
   \(\Ph=\Theta_\chi^{\mathrm{pair}}\) and
   \(q=q_\chi^{\mathrm{pair}}\), the paired corrected same-point and mixed
   blocks are exactly the RH finite-\(s\) block formulas after the declared
   corrections.
2. Add a unit-coordinate corollary: under the pure value path
   \(\Theta_{\chi,\alpha}^{\mathrm{pair}}
   =\Theta_{\chi,0}^{\mathrm{pair}}+\alpha(t-m)\), the coordinate
   \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\) satisfies
   \(da/dS|_0=1\), and all non-value coordinates have zero first variation.
3. Pair that corollary with the holomorphy/whitening hypothesis block before
   defining \(A_{\mathrm{val},\chi}^{\mathrm{pair}}\).
4. State the freeze-rule remainder criterion as a derivative condition, not
   only as the definition of \(R_\chi^{\mathrm{pair}}\).
5. If the final statement uses a scalar readout, prove its derivative is
   normalized consistently with the matrix value slot.

## Autoresearch next step

continue: write the theorem-facing paired finite-\(s\) construction lemma in
paper style, copying the RH formulas and replacing \(\Ph,q\) with
\(\Theta_\chi^{\mathrm{pair}},q_\chi^{\mathrm{pair}}\); then mark exactly where
holomorphy/positivity remains a hypothesis.

verify: have an adversarial pass check whether the completed-Hadamard
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) convention creates a positivity
or baseline conflict for the local whitening background, without reopening the
UV-016 source identity.
