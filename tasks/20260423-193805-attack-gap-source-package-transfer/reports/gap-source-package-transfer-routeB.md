## Claim

The transfer from the zeta source package to the paired Dirichlet source theorem is only partly formal. The formal part is the upstairs quotient layer: once one has a family-specific paired source theorem for
\[
\Phi_\chi^{\mathrm{pair}}(s)=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)},
\qquad
\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi),
\]
the one-zero strip-edge kernel and its positivity transfer formally from the zeta package.

The transfer stops being formal at three exact points:

1. identifying the manuscript-style phase derivative with the paired quotient and fixing the branch / sign / factor-of-`2` normalization;
2. proving that the paired background-subtracted scalar is exactly the local value-channel coefficient occupying the manuscript's `S(m)` slot, not merely an upstairs positive scalar;
3. proving the family-specific compact-interval background / regularization / multiplicity package and the downstream denominator / whitening / boundary compatibility needed by the local deformation.

So the paired Dirichlet target is not safely described as only `zeta source package + family-specific background`. That wording understates the main gap. The safer statement is:

`zeta source package + family-specific source identification + exact local-slot realization + family-specific background/convergence bookkeeping`.

## Status

open

## Evidence

Proved.

- The zeta-side package is already localized as three theorem-level items plus two convention items: quotient / phase normalization, single-zero contribution, compact-interval summation / regularization, plus background-term unification and multiplicity convention. That identifies what could even be transferred.
- The universal-source-kernel result gives the exact formal part of the transfer. For any family quotient of the form `Lambda_F(2s-1)/Lambda_F(2s)`, once a family-specific quotient/source theorem exists, the single-zero quotient-log-derivative kernel has the same strip-edge shape as in zeta, and positivity of that one-zero kernel is automatic upstairs.
- The paired Dirichlet notes identify `Phi_chi^pair` as the clean theorem-facing object and explicitly state that pairing removes the residual root-number/front-end asymmetry. So the zeta package does transfer formally at the quotient-kernel level after passing from `Lambda` to `Xi_chi`.

Conditional on [an exact paired source theorem for `Phi_chi^pair`].

- If the paired theorem supplies the exact background-subtracted scalar occupying the manuscript's paired `S(m)` slot, then the existing local algebra already gives the leading-channel coefficient theorem. In that scoped sense, the zeta package would transfer together with family-specific realization data.
- Under that same condition, positivity of the paired manuscript `S(m)` slot would be automatic, because the universal upstairs kernel positivity would then attach to the exact local scalar used by the corrected local deformation.

Missing.

- No note proves the first non-formal step: that the manuscript-style paired phase derivative is actually the derivative coming from `Phi_chi^pair`, with the correct branch/sign/factor normalization. On the zeta side this is itself listed as theorem content, not bookkeeping; nothing in the paired Dirichlet notes shows it becomes automatic after pairing.
- No note proves the second and main non-formal step: that the paired background-subtracted scalar is exactly the coefficient of the local value channel, rather than a related upstairs strip-edge density. Multiple prior pressure tests say this exact `S(m)`-slot identification is the load-bearing missing theorem.
- No note proves the third non-formal step: the full paired background theorem on compact intervals. Pairing removes the residual root number, but the notes still treat conductor/scaling, gamma-derivative, trivial-zero/pole corrections, multiplicities, and regularization as theorem-sized family-specific work collected into one `B_chi^pair`.
- Even after exact slot identification, the paired route still needs family-specific denominator comparability, corrected whitening, and boundary control. Those are not part of the formal zeta-to-paired transfer.

This is why `zeta source package + family-specific background` is too weak. The family-specific work is not only background subtraction. The central missing item is exact local realization of the scalar that the manuscript actually uses.

Honest verdict: the transfer is formal only upstairs. Pairing genuinely simplifies the front end, but from current scope alone it does not collapse the problem to background bookkeeping. The main gap remains a family-specific source-to-slot realization theorem.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-31`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:106-125`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:40-56`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:66-87`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:21-25`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:61-86`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-38`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeB.md:13-34`
- `/mnt/c/workspace/riemann2/tasks/20260423-143207-attack-gap-paired-object-candidate/reports/gap-paired-object-routeB.md:26-45`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeB.md:5-36`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeB.md:40-69`
- `/mnt/c/workspace/riemann2/tasks/20260423-184608-attack-gap-paired-background/reports/gap-paired-background-routeB.md:11-22`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:3-20`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:50-56`

## Dependencies

- The zeta source package is taken in the localized form recorded in `notes/zeta_source_package.md`.
- The scoped universal-kernel conclusion is taken as the exact statement of what transfers formally upstairs.
- The paired object is taken to be `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)` with `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)`.
- The manuscript local algebra is assumed reusable only after exact identification of the paired background-subtracted scalar with the manuscript-style `S(m)` slot.

## Strongest objection

The strongest objection is that this report may still be too pessimistic about how much pairing buys. A well-chosen paired quotient might force the correct background subtraction and make local-slot identification nearly tautological once the paired source formula is written carefully. Current notes do not prove that collapse. From current scope alone, the safe reading is that pairing removes one obstruction class at the front end, while the main theorem-sized source-to-slot identification gap remains.

## Needed for promotion

1. State a paired analogue of the zeta source theorem with exact quotient object, branch/sign/factor normalization, multiplicity convention, and compact-interval regularized zero-sum formula.
2. Prove that the resulting paired background-subtracted scalar is exactly the coefficient of the manuscript-style leading value channel.
3. Prove one unified paired background theorem identifying `B_chi^pair`, including conductor, gamma-derivative, and trivial-zero/pole corrections, with no hidden leftover term.
4. Separate explicitly what remains after that: denominator comparability, corrected whitening, and boundary control.
5. Keep the safe summary scoped as: `formal upstairs transfer plus family-specific local realization`, not `zeta package plus background`.
