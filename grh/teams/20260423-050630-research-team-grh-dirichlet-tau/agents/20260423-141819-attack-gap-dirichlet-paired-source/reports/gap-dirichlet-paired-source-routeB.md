# Claim

The paired `((\chi,\bar\chi))` route is still the best non-zeta source-theorem target from current scope alone, but pairing does **not** reduce the main gap to a substantially smaller theorem than the single-channel route. It removes only the front-end scalar reality/nonnegativity ambiguity. The smallest theorem still needed after pairing is an **exact paired-scalar source theorem** that identifies a background-subtracted paired Dirichlet scalar with the manuscript's exact leading value-channel coefficient `S(m)` slot, with the needed normalization, source decomposition, and compact-interval bookkeeping. Pairing narrows the route selection problem; it does not close the realization problem.

# Status

open

# Evidence

Proved from current notes and draft:

- The repository's safe ranking is explicit but scoped: `priority.md` says the best non-zeta realization target is the `primitive Dirichlet paired-scalar exact-source theorem`, while `dirichlet_channel.md` says this is the conservative first scalar target only `from current scope alone` because reality and nonnegativity are built in at the scalar level. That is a route-selection advantage, not a proved closure theorem.
- `quotient_phase.md` and `universal_source_kernel.md` isolate what recent progress actually buys. The single completed quotient now has only a `phase-channel upgrade`, and the one-zero strip-edge kernel is universal only upstairs once a family-specific quotient/source theorem exists. These notes explicitly say that realized positive `S(m)`-slot identification, background bookkeeping, convergence, denominator comparability, whitening, and boundary control remain family-specific.
- `positive_s_implication.md` gives the key dependency ordering. If a family theorem yields the **exact** scalar occupying the manuscript's `S(m)` slot, then the leading-channel coefficient theorem is already supplied by the paper's local algebra. But quotient positivity or an analogous positive scalar does not suffice. So the theorem one still needs after pairing is not `some positive paired scalar exists`; it is `the paired scalar is exactly the scalar in the corrected local deformation`.
- The manuscript makes that exact slot load-bearing. In `proof_of_rh.tex`, `S(m)=q_\zeta(m)-B_\zeta(m)` is the coefficient in
  `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`.
  The odd/transverse scalar then annihilates the leading value channel and depends only on the remainder package. This architecture shows why pairing does not bypass realization: the route must still deliver the exact scalar entering the corrected local deformation, not merely a real boundary object.
- The single-channel pressure tests already identify the same boundary from the opposite side. They conclude that the single route would catch up only if one proved the stronger theorem that its background-subtracted scalar is exactly the manuscript-style `S(m)` slot. That means the genuine difference between paired and single routes is the plausibility of scalar sign/reality, not the size of the remaining exact-source theorem.

Conditional on [the paired scalar being defined by a completed Dirichlet quotient/source package]:

- Pairing plausibly removes one obstruction that is specific to non-self-dual primitive Dirichlet characters: one no longer has to recover a real scalar from a single complex channel by phase normalization alone. The paired object is the safer candidate for a real nonnegative scalar amplitude.
- If one proves that the paired background-subtracted scalar is exactly the value-channel coefficient used by the corrected local deformation, then the manuscript's existing local algebra already supplies the `\Delta = S A_{\val} + R` step. In that scoped sense, pairing does reduce the gap versus a weak single-channel source theorem that only gives upstairs quotient positivity.
- But even under that favorable scope, the route still leaves the same downstream items open: remainder dominance, the independent odd/transverse package, and family-specific denominator/whitening/boundary control.

Missing:

- A precise primitive-Dirichlet theorem that fixes the paired completed source object, the branch/sign/factor normalization, multiplicity convention, and compact-interval regularized zero-sum formula for a paired scalar analogue of `q_F=B_F+S_F`.
- A proof that the paired background-subtracted scalar is **exactly** the manuscript's leading value-channel coefficient, not merely a positive or real scalar built from `\chi` and `\bar\chi`.
- A proof that the paired route gives the same local denominator architecture and corrected whitening hypotheses needed to form the corrected whitened block and its transverse scalar.
- Any theorem showing that pairing collapses the remaining realization burden below the single-channel route once exact `S`-slot realization is demanded. Current notes support only a safer front end, not a smaller end-to-end theorem.

Honest verdict: pairing is the best current non-zeta target because it makes the scalar sign problem cleaner. It does not materially shrink the theorem-sized gap after one asks for the manuscript's exact `S(m)` slot. The smallest remaining theorem is still an exact paired-scalar source theorem with explicit source bookkeeping and exact local-slot identification.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:8-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:14-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:50-86`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:25-43`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-288`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1566`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322`
- `/mnt/c/workspace/riemann2/tasks/20260423-053136-attack-gap-dirichlet-channel/reports/gap-dirichlet-channel-routeB.md:1-37`
- `/mnt/c/workspace/riemann2/tasks/20260423-140208-attack-gap-dirichlet-single-channel/reports/gap-dirichlet-single-routeA.md:13-35`
- `/mnt/c/workspace/riemann2/tasks/20260423-140208-attack-gap-dirichlet-single-channel/reports/gap-dirichlet-single-routeB.md:11-20`
- `/mnt/c/workspace/riemann2/tasks/20260423-141258-attack-gap-priority-target/reports/gap-priority-target-routeA.md:14-19`

# Dependencies

- The current `grh/` notes are taken as the authoritative boundary for what is proved, conditional, and missing.
- The manuscript's local algebra is assumed portable only after exact family-specific identification of the scalar occupying the `S(m)` slot.
- The comparison between paired and single routes treats `route quality` as `how much theorem burden is removed before exact local realization`, not as `which route is aesthetically cleaner`.

# Strongest objection

The strongest objection is that the paired route may in practice reduce more than this report credits. If the paired scalar automatically packages the correct background subtraction, normalization, and local denominator structure once one writes the right completed quotient, then the remaining theorem could turn out materially shorter than the analogous single-channel statement. Current notes do not prove that collapse. They support only the narrower conclusion that pairing makes the scalar reality/sign issue safer at the front end.

# Needed for promotion

1. State one primitive-Dirichlet paired theorem with exact object, normalization, and conclusion: a paired scalar decomposition `q_{\mathrm{pair}}=B_{\mathrm{pair}}+S_{\mathrm{pair}}` on singularity-free compact intervals.
2. Prove a regularized zero-source formula for `S_{\mathrm{pair}}` with multiplicities and full background bookkeeping.
3. Prove that `S_{\mathrm{pair}}(m)` is exactly the coefficient of the manuscript-style leading value channel, not merely a positive surrogate.
4. Then separate the remaining downstream tasks explicitly: remainder dominance, odd/transverse realization, and family-specific denominator/whitening/boundary estimates.
5. Keep the claim scoped as: pairing improves route selection, but the smallest remaining theorem is still an exact paired-scalar source theorem.
