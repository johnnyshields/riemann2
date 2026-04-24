## Claim

The UV-017 determinant gap cannot be proved from positive zero kernels alone.
Noether's exact one-zero calculation rejects the unpaired kernel route:
\(\mathcal D[K]\equiv0\) on the critical line and
\(\mathcal D[K](\gamma/2)<0\) off the critical line. The paired-completed
functional-equation reflection does, however, repair the off-critical
one-ordinate obstruction: the reflected double \(2K_{\beta,\gamma}\) satisfies
\(\mathcal D[2K_{\beta,\gamma}]>0\) for every real \(t\), every
\(0<\beta<1\), and every \(\gamma\). A simple noncentral critical-line zero
is still degenerate until its conjugate ordinate, multiplicity, or another
source term is included. Full completed-orbit sums remain open: numerical
searches found no negative examples for sums of reflected/full orbits, but no
aggregate inequality has been proved. Therefore the
determinant-gap route is rejected from source positivity alone and must be
replaced by either an aggregate reflected-orbit theorem or an explicit local
whitening gap hypothesis.

## Status

open

## Evidence

**Proved.** Noether's report gives the exact unpaired one-zero obstruction.
For
\[
K_{\beta,\gamma}(t)
=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+\frac{\beta}{\beta^2+(2t-\gamma)^2},
\]
with \(c=\beta(1-\beta)\), \(y=(2t-\gamma)^2\), and
\(h=(y+\beta^2)(y+(1-\beta)^2)\), Noether proves
\[
\mathcal D[K]=P(c,y)/h(c,y)^4.
\]
The factorization implies \(\mathcal D[K]\equiv0\) for \(\beta=1/2\) and
\[
\mathcal D[K](\gamma/2)
=-\frac{12(1-2\beta)^2}{\beta^4(1-\beta)^4}<0
\]
for \(\beta\ne1/2\). Thus the unpaired positive one-zero kernel is not a
determinant-positive atom.

**Proved.** The reflected same-ordinate double repairs that atom. Since
\[
\mathcal D[\lambda K]
=\lambda^2\mathcal D[K]+4\lambda^2(\lambda^2-1)K^4,
\]
Noether's one-zero numerator gives, for \(\lambda=2\),
\[
\mathcal D[2K]=\frac{N_2(c,y)}{h(c,y)^4},
\]
where
\[
\begin{aligned}
N_2(c,y)
&=192cy^4+384c(1-2c)y^3\\
&\quad+192c(6c^2-4c+1)y^2\\
&\quad+384c^3(1-2c)y+192c^5.
\end{aligned}
\]
For \(0<c\le1/4\), all coefficients are positive. Hence
\(\mathcal D[2K_{\beta,\gamma}](t)>0\) for every real \(t\). This is the
exact repair supplied off the critical line by the functional-equation
reflected partner \(\beta\mapsto1-\beta\), whose kernel is identical to
\(K_{\beta,\gamma}\). On the critical line away from \(\gamma=0\), that
reflection is not a distinct same-ordinate zero in general; a simple
critical-line kernel remains degenerate until the conjugate ordinate,
multiplicity, or another source contribution is added.

**Computational.** The saved script
`scripts/determinant_gap_orbit_repair.py` has SHA256
`826d229c9d67414c0494653b59d26cc067b5092eb1eb885f5b921fb10ca41bcd`.
Relevant output:

- `Thus D[2K]>0 for every real t, beta in (0,1), and gamma.`
- `unpaired_one_zero_beta_1_50: min_D=-74937539.040809944`
- `reflected_double_beta_1_50: min_D=3.6919150596235626e-08`
- `critical_conjugate_pair_gamma_5: min_D=3.0111415205872163e-06`
- `full_orbit_beta_1_50_gamma_5: min_D=1.2253369227142641e-05`
- `two_full_orbits_nearby: min_D=5.9372644481954593e-05`
- `full_orbit_sums_general: best_D=1.1219262069218306e-06`
- `full_orbit_sums_near_edge: best_D=1.1911493914193663e-06`
- `generic_critical_conjugate_sums: best_D=2.6538410041086631e-07`

The earlier broader search script `scripts/determinant_gap_search.py` has
SHA256 `f604621d7b90c53d005bf76b33117b44de254e707a5f7c773e15988c7fc56491`.
It independently found negative unpaired/off-symmetry configurations and no
negative full-quartet hits in the tested random families.

**Conditional.** For an actual completed nonreal off-critical orbit one expects
\[
q_{\mathrm{orb}}(t)=2K_{\beta,\gamma}(t)+2K_{\beta,-\gamma}(t)
\]
with analytic multiplicity. A generic noncentral critical-line conjugate pair
has \(K_{1/2,\gamma}+K_{1/2,-\gamma}\) instead. The positivity of each \(2K\)
summand does not prove positivity of the sum because \(\mathcal D\) is
nonlinear. Tails can
preserve a pre-existing compact gap by continuity: if
\(q_0\ge q_*>0\), \(\mathcal D[q_0]\ge\kappa>0\), and a tail \(r\) is small in
\(C^2\), then \(\mathcal D[q_0+r]\ge\kappa/2\) under an explicit smallness
bound. This does not force positivity when the core gap is zero or negative.

**Missing.** There is still no theorem that positive sums of full
paired-completed orbits satisfy \(\mathcal D[q]>0\) on the needed microscopic
window. There is also no quantitative tail theorem giving a uniform lower
bound from completed-zero bookkeeping alone.

## Baseline / delta

Baseline: UV-017 had been reduced by Noether and Sartre to the exact
same-point positivity condition
\[
q>0,\qquad \mathcal D[q]=2qq''+4q^4-3(q')^2>0.
\]
Noether then rejected the one-zero determinant route.

Delta: this lane confirms the redirect. The one-zero route is dead from
source positivity alone, but the functional-equation reflected double
\(2K\) has an exact positive numerator off the critical line. Critical-line
simple kernels still need conjugate/multiplicity repair. Multi-zero/full-orbit
stability is now the real target: plausible from searches, not proved, and not
safe to promote without an aggregate inequality or explicit local gap
hypothesis.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-87` states UV-017 and the determinant/spectral-gap reduction.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md:151-163` records that positivity is exactly the determinant gap for the displayed chart.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:289-305` states the conditional local-admissibility hypothesis.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:360-374` lists the determinant/spectral gap as remaining open work.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-one-zero-determinant-gap.md:1-24` states Noether's one-zero rejection.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-one-zero-determinant-gap.md:31-126` gives the exact one-zero algebra and remaining aggregate/tail gaps.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/report-uv017-one-zero-determinant-gap.md:172-195` scopes the strongest objection and next promotion needs.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-holomorphy-positivity-audit.md:1-23` verifies the determinant condition and says UV-017 remains open.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-holomorphy-positivity-audit.md:50-92` verifies the same-point determinant algebra and conditional whitening scope.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md:45-67` records the sign-audited positive kernel convention used here.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py:1-28` is the prior one-zero sign script.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/determinant_gap_orbit_repair.py` with SHA256 `826d229c9d67414c0494653b59d26cc067b5092eb1eb885f5b921fb10ca41bcd`.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/determinant_gap_search.py` with SHA256 `f604621d7b90c53d005bf76b33117b44de254e707a5f7c773e15988c7fc56491`.
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/notes/determinant_gap_stability.md:1` records the supporting derivation note for this lane.

## Dependencies

- Sign-audited convention: the positive zero source is the strip-edge kernel
contribution to \(-\frac12\Phi'/\Phi\).
- UV-017 local-admissibility reduction:
\(\mathcal D[q]>0\) is necessary and sufficient for the displayed real
same-point chart block at \(s=0\), together with \(q>0\).
- Noether's exact one-zero determinant calculation.
- Functional-equation/reflection bookkeeping for the completed paired product:
off-critical zeros occur with the reflected \(\beta\mapsto1-\beta\) partner,
giving a same-ordinate double \(2K\), while generic noncentral critical-line
zeros contribute through conjugate ordinates rather than a forced
same-ordinate double.
- Any tail or multi-orbit promotion depends on compact \(C^2\) control or a
new aggregate inequality for sums of reflected/full orbits.

## Strongest objection

The exact positive result is only for the same-ordinate reflected double
\(2K_{\beta,\gamma}\). A full completed orbit and a real source contain sums
of such pieces, and \(\mathcal D\) is nonlinear; positive determinant gap for
each piece does not automatically survive addition. The numerical searches
are useful failure probes, not proof. Therefore the report cannot promote a
paired source determinant theorem.

## Needed for promotion

1. Prove an aggregate inequality for sums of reflected doubles
\(q=\sum_j 2m_jK_{\beta_j,\gamma_j}\), and then for full conjugate-reflected
orbits if the theorem needs real boundary symmetry.
2. Or state a compact local whitening hypothesis:
\[
q_\chi^{\mathrm{pair}}>0,\qquad
\mathcal D[q_\chi^{\mathrm{pair}}]\ge\kappa>0
\]
on the microscopic window, with tail terms controlled in \(C^2\).
3. Keep Noether's one-zero rejection visible so no one promotes a one-zero
source-kernel determinant lemma.
4. Verify the reflected-double formula adversarially against Noether's
\(P(c,y)\) normalization and the \(t\)-derivative factors.

## Autoresearch next step

continue: attack the aggregate reflected-double inequality. The clean target is
to decide whether
\[
\mathcal D\left[\sum_j 2m_jK_{\beta_j,\gamma_j}\right]>0
\]
holds for all finite positive integer sums, or to find a counterexample. If no
global inequality appears, reduce UV-017 to the explicit compact hypothesis
\(q>0\), \(\mathcal D[q]\ge\kappa>0\), plus a \(C^2\) tail-smallness lemma.

verify: ask an adversarial checker to confirm the exact \(D[2K]\) numerator
and to stress-test addition of two reflected doubles, especially near-edge
zeros with close ordinates.

## Ledger destination

`findings.md`: capture the scoped negative and repair: unpaired one-zero
determinant positivity is rejected, but the off-critical completed reflected
double \(2K\) has an exact positive determinant gap; full-orbit/sum stability
remains unproved. `attempts.md`: keep as a determinant-gap stability explorer route.
`uv.md`: keep UV-017 open, with the determinant subgap sharpened to aggregate
reflected-orbit positivity or an explicit local whitening gap hypothesis.
