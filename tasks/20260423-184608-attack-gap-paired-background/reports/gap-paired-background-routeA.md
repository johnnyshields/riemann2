# Claim

For the theorem-facing paired quotient
\[
\Phi^{\mathrm{pair}}_\chi(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)},
\qquad
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\bar\chi),
\]
the clean exact-source decomposition to expect is a single paired source formula on compact intervals avoiding the real singularities of the background package,
\[
q^{\mathrm{pair}}_\chi(t)=B^{\mathrm{pair}}_\chi(t)+S^{\mathrm{pair}}_\chi(t),
\]
where `the paired background term` should contain all non-nontrivial-zero contributions coming from the logarithmic derivative of `\Phi^{\mathrm{pair}}_\chi`, namely:

1. the conductor / scaling term coming from the completed factors;
2. the archimedean gamma-derivative contribution from the two gamma factors in `\Xi_\chi`;
3. any explicit trivial-zero and pole corrections needed when the formula is rewritten as a sum over nontrivial zeros only.

The corresponding zero term should then be stated as the sum of the strip-edge kernels coming from the nontrivial zeros of the paired completed object, equivalently from the nontrivial zeros of `L(s,\chi)` and `L(s,\bar\chi)` counted with multiplicity.

The cleanest theorem-facing wording is therefore not `background from \chi plus background from \bar\chi plus extra phase constants`, but one unified paired background `B^{\mathrm{pair}}_\chi` absorbing all conductor / gamma / trivial-zero / pole bookkeeping behind the quotient-log-derivative source formula.

What pairing cancels automatically is front-end symmetry data: the root-number factor disappears in the paired completed product, and the boundary value becomes a self-dual scalar phase. What remains is not phase asymmetry but the family-specific background identification and exact local-slot realization.

# Status

open

# Evidence

Proved.

- The paired object note already fixes the correct theorem-facing quotient as
  \[
  \Phi^{\mathrm{pair}}_\chi(s)=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}
  \]
  with `\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\bar\chi)`. So any source theorem should be written for one paired completed object, not for two unrelated single channels.
- The paired-quotient-properties note gives the automatic cancellation that pairing buys at the boundary: multiplying the functional equations removes the residual root number and yields the self-dual identities `\Xi_\chi(s)=\Xi_\chi(1-s)` and `\overline{\Xi_\chi(\bar s)}=\Xi_\chi(s)`. Hence on `s=1/2+it`, `\Phi^{\mathrm{pair}}_\chi` is a `U(1)`-valued scalar phase away from denominator zeros. This is the automatic cancellation piece.
- The universal-source-kernel note isolates what comes from quotient geometry alone: once a family-specific quotient/source theorem exists for a quotient of the form `\Lambda_F(2s-1)/\Lambda_F(2s)`, the one-zero strip-edge kernel is universal upstairs. Therefore the nontrivial-zero part of the paired theorem should have exactly the same strip-edge kernel shape as in zeta, summed over the nontrivial zeros of the paired completed object.
- The source-theorem-gap note says the missing task is to `identify and unify the full background term behind B_zeta, B_Aut, and B_bg`. That points to the cleanest theorem statement here: one unified paired background term, not several partially overlapping background names.

Conditional on [standard completed-`L` facts for primitive Dirichlet characters].

- The expected paired background pieces are exactly the pieces left after extracting the nontrivial-zero contribution from the logarithmic derivative of `\Phi^{\mathrm{pair}}_\chi`: conductor/scaling, gamma-factor derivatives, and any singular corrections associated with trivial zeros or poles on the compact interval statement.
- For primitive nonprincipal complex `\chi`, the clean expectation is that there is no surviving root-number term and no zeta-style pole contribution from `L(s,\chi)` itself; if one states the theorem in a way that also covers pole-bearing exceptional cases, that pole correction still belongs in `B^{\mathrm{pair}}_\chi`, not in `S^{\mathrm{pair}}_\chi`.
- Because `\Xi_\chi` is already paired and self-dual, the clean theorem-facing zero sum may be written either as a sum over zeros of `\Xi_\chi` or as the combined sum over zeros of `L(s,\chi)` and `L(s,\bar\chi)`. The theorem should choose one bookkeeping convention and keep multiplicities explicit.

Missing.

- No supplied note proves one canonical normalization for `q^{\mathrm{pair}}_\chi(t)` analogous to the zeta note's `q=\Phi'`; the factor-of-`2` / factor-of-`4` convention is still theorem-sized bookkeeping.
- No supplied note proves the exact decomposition of the paired background into conductor, gamma, trivial-zero, and possible pole terms inside the canonical draft or the `grh/` notes.
- No supplied note proves whether the cleanest final theorem should absorb trivial-zero effects entirely into the gamma/background package or display them as a separate explicit correction before regrouping into `B^{\mathrm{pair}}_\chi`.
- No supplied note proves the compact-interval convergence / regularization statement for the paired zero sum.
- No supplied note proves that the background-subtracted paired scalar is exactly the coefficient occupying the manuscript-style local `S(m)` slot rather than only an upstairs strip-edge source scalar.

Honest verdict: the clean expected paired background is `all non-nontrivial-zero quotient-log-derivative terms, unified into one B^{pair}`. Pairing automatically cancels the residual root-number phase and the front-end `\chi` versus `\bar\chi` asymmetry. What remains is the real source-theorem work: exact normalization, exact background bookkeeping, convergence/regularization, and exact local-slot identification.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:40-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:33-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:8-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:21-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:112-123`
- `/mnt/c/workspace/riemann2/tasks/20260423-143207-attack-gap-paired-object-candidate/reports/gap-paired-object-routeA.md:16-23`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md:11-18`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md:28-37`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md:107-130`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeB.md:5-36`
- External standard facts used but not reproved here: primitive Dirichlet completed functional equation, conjugation symmetry, and the usual completed-factor decomposition into conductor, gamma, and `L`-zero data.

# Dependencies

- The `grh/` notes are used as the authority for the safe proved / conditional / missing boundary.
- Standard primitive Dirichlet completed-`L` facts are used only at the level of expected source-term decomposition: functional equation, conjugation symmetry, completed-factor structure, and the distinction between nontrivial zeros versus gamma / trivial-zero / pole singularities.
- The universal-source-kernel note is used only for the upstairs one-zero kernel shape, not for any local-slot realization.
- `Background term` is interpreted in the same sense as the zeta candidate source theorem: everything left after isolating the explicit nontrivial-zero strip-edge sum.

# Strongest objection

The main objection is that this report is still partly schematic about the internal splitting of the paired background. The supplied notes support `what kinds of terms must be in the background`, but they do not pin down one exact display formula for the conductor constant, gamma derivative, and trivial-zero corrections, nor do they prove whether trivial zeros should be shown separately before regrouping. So the report is strongest as a theorem-facing decomposition template, not as a proved exact formula.

# Needed for promotion

1. Fix one exact normalization for the paired phase or logarithmic-derivative scalar attached to `\Phi^{\mathrm{pair}}_\chi`.
2. Write and prove the full paired source theorem on compact intervals, with explicit conductor, gamma, trivial-zero, multiplicity, and any pole bookkeeping.
3. Decide one canonical presentation of the background: either a single displayed `B^{\mathrm{pair}}_\chi` or an explicit intermediate split that is immediately unified.
4. Prove the compact-interval convergence / regularization statement for the paired zero sum.
5. Prove that the background-subtracted paired scalar is exactly the manuscript-style local `S(m)`-slot coefficient.
