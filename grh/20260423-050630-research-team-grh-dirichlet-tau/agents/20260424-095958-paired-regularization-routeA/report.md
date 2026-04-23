## Claim

The cleanest theorem-facing compact-interval summation/regularization statement needed for the paired source package is:

**Candidate theorem (paired compact-interval source identity, pre-slot form).** Let `chi` be a primitive Dirichlet character, set
`Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)`, and define the paired quotient
`Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)`.
Fix a compact interval `I` on which the boundary-phase normalization attached to
`Phi_chi^pair(1/2+it)` is regular. Then the needed theorem unit is a localized identity on `I`
of the form

`q_chi^pair(t)=B_chi^pair(t)+sum_I^reg K_{rho,chi}^pair(t),  t in I,`

where `sum_I^reg K_{rho,chi}^pair(t)` denotes the compact-interval regularized sum of the paired one-zero strip-edge kernel contributions, and `B_chi^pair(t)` is one unified background term absorbing the conductor/scaling, gamma-derivative, and trivial-zero or pole bookkeeping. Repeated zeros are handled by an explicit multiplicity convention internal to this localized regularized identity.

The theorem must assert only this compact-interval source decomposition and its bookkeeping shell. It must stop before any claim that the resulting paired source scalar already equals the manuscript's exact local `S(m)` slot, and before any local whitening-interface theorem.

Formal from the zeta blueprint:

- the quotient/phase-normalization shell;
- the upstairs one-zero strip-edge kernel shape;
- the idea that the first theorem endpoint is a localized compact-interval source identity rather than a global slot theorem.

Genuinely new for the paired family:

- proving paired compact-interval convergence/regularization;
- identifying one theorem-ready unified paired background `B_chi^pair`;
- closing theorem-facing multiplicity bookkeeping in the paired setting.

Proved / conditional / missing:

- **Proved:** the safe theorem target is only a compact-interval paired source-package blueprint, and the transferable zeta content is limited to the quotient shell, the upstairs one-zero kernel shape, and the blueprint idea of a localized compact-interval source theorem.
- **Conditional on a family-specific paired source theorem:** one may aim for the exact paired identity above for `Phi_chi^pair`, with one unified `B_chi^pair` and explicit multiplicity bookkeeping on `I`.
- **Missing:** an actual proof of paired compact-interval convergence/regularization, theorem-ready unified paired background identification, theorem-facing multiplicity closure, exact realization of the manuscript's `S(m)` slot, and any transport to a local whitening/positivity theorem.

Honest verdict: this compact-interval identity is the right theorem-facing statement to target, but at present it is only the clean blueprint target, not a proved paired theorem.

## Status

open

## Evidence

`paired_source_package.md` says the safe compact paired-source theorem is only a compact-interval source-package blueprint and explicitly identifies paired compact-interval convergence/regularization, unified `B_chi^pair`, and multiplicity bookkeeping as the first real theorem burdens, while stopping before exact paired `S(m)`-slot realization and any whitening-interface claim. `source_package_transfer.md` gives the formal transfer boundary: from zeta one gets only the quotient shell, upstairs one-zero kernel shape, and the idea of a localized compact-interval source theorem; one does not get exact paired `S(m)`-slot realization, unified paired background identification, paired compact-interval convergence/regularization, or paired multiplicity bookkeeping for free. `universal_source_kernel.md` matches this by treating the single-zero strip-edge kernel as universal only in a scoped upstairs sense, conditional on a family-specific quotient/source theorem, while leaving background identification, convergence/regularization, and local slot realization family-specific.

Taken together, these notes force the theorem split above. The clean theorem-facing regularization statement is one localized identity for the paired quotient on a compact interval, with the regularized zero-sum and unified background inside the theorem, and with exact manuscript-slot realization kept outside as a later theorem step.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:11-15`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:19-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-15`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:22-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-093552-paired-summation-routeA/report.md:3-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-093552-paired-summation-routeB/report.md:3-19`

## Dependencies

This theorem target depends on fixing the paired quotient `Phi_chi^pair`, the associated compact-interval boundary-phase normalization, the paired one-zero strip-edge kernel, and a family-specific proof that the paired zero contributions can be regularized on `I` into one exact localized source identity with one unified background term and explicit multiplicity convention. Any downstream use depends separately on exact source-to-slot identification and on the local analytic package behind whitening/positivity.

## Strongest objection

Even this statement can overstate the current record if read as already-established mathematics. The notes support it only as the clean theorem target. Writing the paired identity without an explicit scope reminder risks smuggling in the still-open convergence/regularization, unified background, and multiplicity closure as if they had already transferred from the zeta case.

## Needed for promotion

1. A family-specific proof that the paired one-zero contributions admit an exact compact-interval regularization on `I`.
2. A theorem-ready identification of one unified paired background term `B_chi^pair` covering conductor/scaling, gamma-derivative, and trivial-zero or pole terms.
3. An explicit multiplicity convention stable under the compact-interval regularized identity.
4. A separate proof that the resulting paired source scalar realizes the manuscript's exact local `S(m)` slot.
5. If needed downstream, a separate local whitening-interface theorem or an explicitly isolated conditional hypothesis block.
