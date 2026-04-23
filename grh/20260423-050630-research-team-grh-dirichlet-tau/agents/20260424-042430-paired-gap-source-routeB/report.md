## Claim

The strongest safe boundary sentence is:

`The compact paired source package may safely supply the holomorphic source-side data and the value-channel interface, but same-point positivity/nondegeneracy for holomorphic whitening should remain an explicit family-local hypothesis line unless a separate paired spectral-gap stability argument is proved.`

On the present notes, folding the baseline same-point gap entirely into the compact source package would overstate what is supported. The notes support a theorem-facing blueprint in which denominator comparability and source bookkeeping feed holomorphy, while same-point positivity/nondegeneracy still enters as a separate local whitening clause. They do not yet support a source-free compact package theorem showing that holomorphy alone, or the current compact source data alone, yields the needed same-point positivity on the microscopic disk.

Three-bin verdict:

- proved: in the manuscript model, holomorphy and positivity are established by distinct steps inside the whitening proposition; denominator comparability feeds holomorphy, while positivity comes from a baseline spectral gap plus perturbative control.
- conditional on a future paired analogue: one could eventually absorb the same-point gap into a compact paired source package if that package is enlarged to include a proved paired spectral-gap stability theorem for the corrected same-point blocks.
- missing: such a paired theorem/package is not contained in the current notes, which instead keep same-point positivity/nondegeneracy as a separate local interface condition.

## Status

conditional

## Evidence

The manuscript’s controlling model is Proposition `Corrected finite-s holomorphic whitening`. Its proof first gets holomorphy from denominator comparability plus removable singularities, and only afterwards gets positivity/nondegeneracy by comparing the corrected same-point blocks to a baseline matrix with spectral gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0)) \gg Q`. The proof then uses `\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\| \ll \rho_0 Q` and `\|R_{m,\pm}(s)\|=o(Q)` to keep the corrected blocks inside the positive-definite cone on the microscopic disk. So the manuscript itself separates `holomorphy input` from `same-point spectral-gap stability input`; positivity is not obtained from denominator holomorphy alone.

The notes sharpen that same distinction in theorem-facing language. `paired_slot_hypotheses.md` first says the paired slot theorem is not source alone, and then explicitly lists corrected-whitening admissibility as including microscopic holomorphy, same-point positivity/nondegeneracy, and well-defined inverse-square-root whitening. It then states even more sharply that same-point positivity/nondegeneracy should not stay hidden inside a generic admissibility phrase and that the safest theorem-facing wording is an explicit local clause for holomorphic whitening. `same_point_positivity.md` says the manuscript does contain a real same-point positivity package, but only as a manuscript-internal perturbative argument, and that this package is theorem-level transportable only as a conditional interface, not yet as a source-free theorem package. `paired_proof_plan.md` likewise downgrades the paired milestone from a closed theorem to a theorem-facing blueprint with explicit missing burdens.

Taken together, the safest reading is: the compact source package can carry source normalization, unified `S_\chi^{\pair}` bookkeeping, and the value-channel derivative interface, but the baseline same-point gap should remain a separately named family-local hypothesis until the paired route proves the analogue of the manuscript’s spectral-gap stability step. Treating it as already subsumed into the compact source package would blur the present proved/conditional/missing boundary.

## Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-891` (`prop:denominator-comparability`): denominator comparability supplies omitted-sum holomorphy.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`): holomorphy separated from positivity; inverse square roots require uniform positive definiteness.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1418-1456`: exact split between holomorphy input and baseline spectral-gap stability.
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1606`: downstream use of the whitening map in the corrected local deformation/value-channel expansion.
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:31-52`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:61-70`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:17-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_proof_plan.md:8-34`

## Dependencies

- The manuscript’s corrected-whitening proposition as the only fully written proof template for how same-point positivity is obtained.
- The team notes `paired_slot_hypotheses.md`, `same_point_positivity.md`, and `paired_proof_plan.md`.
- The current assumption that the paired route seeks an analogue of the manuscript’s corrected-whitening setup, rather than a different source-side mechanism proving positivity automatically.

## Strongest objection

This conclusion relies on extrapolating from the zeta manuscript’s whitening proof and from theorem-facing notes, not from an already written paired-family proof. If the compact paired source theorem were later strengthened to include an explicit paired baseline gap and perturbative stability result, then the gap could be absorbed into the source package without overstatement. The present notes simply do not show that yet.

## Needed for promotion

1. A paired analogue of `prop:corrected-whitening` that proves uniform positivity/nondegeneracy of the corrected same-point blocks on the microscopic disk from clearly stated paired hypotheses.
2. A decision on whether that paired proof is part of the compact source package or is intentionally kept as a separate local whitening lemma.
3. Theorem-facing wording that preserves the current safe split if no such proof is available: source package for holomorphic/value-channel data, plus an explicit separate local clause `same-point positivity/nondegeneracy for holomorphic whitening`.
4. An adversarial check that the paired route really gives diskwise positivity, not merely base-point nondegeneracy or denominator holomorphy.
