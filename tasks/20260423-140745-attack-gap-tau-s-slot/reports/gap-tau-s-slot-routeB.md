# Claim

Tau is not yet meaningfully ahead of Dirichlet on the full localization roadmap. It is ahead only on the front end, and even there the advance is split into two distinct layers.

- Proved: tau is the cleanest self-dual phase-channel candidate now on record, via the completed quotient `\Lambda_\tau(2s-1)/\Lambda_\tau(2s)` and the scoped upstairs one-zero kernel statement.
- Conditional on an exact family-specific quotient/source theorem: once tau supplies the exact scalar occupying the manuscript's `S(m)` slot, the calibrated value-channel subchain no longer needs a new kernel theorem, and its next bottleneck becomes calibrated remainder dominance.
- Missing: that exact `S`-slot identification does not discharge the five degree-sensitive localization checkpoints except by settling checkpoint 1 only in the narrow sense of identifying the leading value-channel scalar. Checkpoints 2 through 5 remain separate missing theorems, and checkpoint 1 still needs the rest of its decomposition/curvature-tail package unless one proves the exact source theorem in full.

Safe replacement for the older `cleanest test object` wording:

- `tau is the cleanest self-dual phase-channel candidate currently on the roadmap; exact S-slot realization and the remaining localization package are still missing.`

If one wants an even tighter sentence tied to the source-kernel note:

- `tau is ahead at the self-dual phase/source front end, not yet at full local realization.`

# Status

open

# Evidence

Proved.

- `notes/tau_localization.md` already weakens tau from a realized local object to a channel candidate and isolates five separate degree-sensitive checkpoints: source decomposition and curvature/tail package; denominator comparability and holomorphy radius; same-point/mixed-block scaling hierarchy; whitening gain and boundary estimate; and crude growth bookkeeping. It also states directly that tau is cleaner only as a channel candidate, not as a realized local test object.
- `notes/quotient_phase.md` upgrades tau only at the phase level: the self-dual quotient is the cleanest phase candidate, but unimodularity alone supplies none of the value-channel data, exact `S(m)` analogue, denominator comparability, whitening, boundary control, localization theorem, or contradiction theorem.
- `notes/universal_source_kernel.md` sharpens the split: the one-zero quotient kernel is universal only upstairs, while the manuscript's exact `S(m)` slot remains family-specific. This is the exact place where `S`-slot identification separates from the other localization checkpoints.
- `notes/remainder_dominance.md` then gives the next-step statement with scope: after exact scalar-slot identification, remainder dominance is the next bottleneck only for the calibrated value-channel subchain, not for the whole portability program.
- The adversarial tau-localization report says the strongest supported sentence is still only a conditional interface theorem and explicitly rejects any reading in which tau is already a cleaner proved local test object. The adversarial quotient-phase, universal-source-kernel, and remainder-dominance reports make the same phase/value and upstairs/downstairs separation.

Conditional on [exact tau `S`-slot theorem].

- If tau proves a family-specific quotient/source theorem that identifies the exact background-subtracted scalar occupying the manuscript's `S(m)` slot, then one major uncertainty is removed: no further search for the one-zero kernel or leading scalar coefficient theorem is needed for the calibrated value-channel comparison.
- Under that hypothesis, the roadmap does improve relative to the older wording. Tau would then be ahead of complex Dirichlet not just as a phase object but as the cleanest self-dual candidate for the calibrated scalar front end.
- Even then, the current notes only justify the scoped sentence from `remainder_dominance.md`: after exact scalar-slot identification, the next bottleneck for that calibrated subchain is remainder dominance. They do not justify saying tau is ahead on the whole localization roadmap.

Missing.

- The exact tau source theorem itself is still missing. The notes do not yet prove the sign, normalization, background subtraction, convergence, and local realization theorem that would put a tau scalar into the manuscript's exact `S(m)` slot.
- Checkpoint 1 is only partially isolated by `S`-slot language. Exact `S`-slot identification would cover the leading scalar/source part of `source decomposition and curvature / tail package`, but the curvature/tail control needed by the local theorem still has to be proved in tau form.
- Checkpoint 2 remains missing: microscopic denominator comparability and holomorphy radius are still family-specific and are not implied by phase unimodularity or upstairs kernel universality.
- Checkpoint 3 remains missing: the same-point and mixed-block baseline scaling hierarchy has not been rederived for degree `2`.
- Checkpoint 4 remains missing: preserved whitening gain and the boundary estimate remain unproved in tau notation.
- Checkpoint 5 remains missing for anything beyond the local theorem: crude growth bookkeeping and any contradiction-strength endgame control are still outside what the current tau notes justify.
- For Dirichlet comparison, the quotient-phase note still treats paired `((chi, bar chi))` or matrix packages as conservative scalar-amplitude fallbacks. So tau is ahead of complex Dirichlet mainly because self-duality simplifies the front end, not because tau has closed more downstream theorems.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:6-18,23-55`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:6-18,25-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:6-18,22-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:6-18,20-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/portability_note.tex:148-167`
- `/mnt/c/workspace/riemann2/tasks/20260423-053621-attack-gap-tau-localization/reports/verifier-adversarial-tau-localization.md:3-15,22-66,98-105`
- `/mnt/c/workspace/riemann2/tasks/20260423-133143-attack-gap-quotient-phase-generalization/reports/verifier-adversarial-quotient-phase-generalization.md:11-21,59-73,97-109`
- `/mnt/c/workspace/riemann2/tasks/20260423-135538-attack-gap-universal-source-kernel/reports/verifier-adversarial-universal-source-kernel.md:3-19,47-66,86-97`
- `/mnt/c/workspace/riemann2/tasks/20260423-134454-attack-gap-remainder-dominance/reports/verifier-adversarial-remainder-dominance.md:3-4,17-27,55-66`

# Dependencies

- A tau-specific quotient/source theorem that fixes sign, normalization, background subtraction, and convergence, and identifies the exact scalar occupying the manuscript's `S(m)` slot.
- A tau curvature/tail package strong enough to replace the zeta-side local source decomposition where needed.
- Tau-side denominator comparability and holomorphy-radius control.
- Tau-side same-point and mixed-block scaling theorems.
- Tau-side preserved whitening and microscopic boundary estimate.
- If any endgame-strength claim is desired, tau-side growth bookkeeping beyond the local theorem.

# Strongest objection

The phrase `exact S-slot identification` is easy to overread. In these notes it isolates the leading scalar/source problem, but it does not by itself prove the rest of localization. Even checkpoint 1 in `tau_localization.md` bundles more than the scalar slot: it also includes the curvature/tail package. So it is still unsafe to say tau is meaningfully ahead of Dirichlet on the roadmap as a whole. The present evidence supports only a narrower verdict: tau is ahead at the self-dual phase/scalar front end, and only conditionally ahead at the calibrated value-channel step once the exact `S`-slot theorem exists.

# Needed for promotion

- Replace `cleanest test object` by `cleanest self-dual phase-channel candidate` or `ahead at the self-dual phase/source front end`.
- Keep any stronger statement explicitly conditional on a tau theorem identifying the exact manuscript `S(m)` slot.
- If that theorem is proved, say separately that only the calibrated value-channel bottleneck shifts to remainder dominance; do not fold checkpoints 2 through 5 into that sentence.
- If checkpoint 1 is discussed, split it into `exact scalar/source identification` versus `curvature/tail control` so the roadmap does not overclaim closure.

Honest verdict: tau is not yet meaningfully ahead of Dirichlet on the full roadmap. It is ahead only at the self-dual phase/scalar front end, with exact `S`-slot realization still conditional and the other localization checkpoints still open.
