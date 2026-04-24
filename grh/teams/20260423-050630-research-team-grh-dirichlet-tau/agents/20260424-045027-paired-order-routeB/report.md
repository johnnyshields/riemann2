# Claim

Keeping same-point positivity/nondegeneracy as a mere hypothesis in a 2-step paired patch is not the safest presentation. The safer route is to expose a separate local positivity/whitening step between the paired source package and the paired slot theorem, while stating that step only conditionally on the local spectral-gap/perturbative inputs the current notes actually support.

# Status

open

# Evidence

Proved:
- The notes consistently say denominator comparability/holomorphy does not by itself supply same-point positivity; positivity needs an additional local spectral-gap stability argument.
- The paired slot theorem is therefore not source alone: its well-posedness already imports microscopic holomorphy, same-point positivity/nondegeneracy, and holomorphic whitening admissibility.
- The current theorem-facing milestone is only a blueprint with explicit missing burdens, not a near-closed theorem.

Conditional on stated local inputs:
- A separate local theorem step is safer if formulated narrowly as: from center spectral gap + baseline variation + perturbation smallness, obtain same-point positivity/nondegeneracy and hence holomorphic whitening for the local paired block.
- That conditional local step can then feed the paired slot theorem without hiding the real burden inside a vague `minimal admissibility` clause.

Missing:
- A clean standalone cross-family positivity theorem independent of source-normalized background data is not yet available.
- It is not safe to claim that the compact paired source package automatically supplies the baseline same-point gap.
- The exact paired slot match, compact-source closure, and downstream remainder/odd-transverse/boundary work remain open.

Strongest safe roadmap sentence:

`Proceed in three explicit layers: paired source package, conditional local same-point positivity/holomorphic-whitening theorem under spectral-gap and perturbative hypotheses, then the paired exact-slot theorem using that interface.`

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-10`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:25-29`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:39-59`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:7-23`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:25-46`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_proof_plan.md:8-18`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/first_milestone.md:20-23`
- Deposited report: `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-045027-paired-order-routeB/report.md`

# Dependencies

- The local positivity blueprint in `same_point_positivity.md`.
- The slot-stage admissibility boundary in `paired_slot_hypotheses.md`.
- The theorem-facing blueprint limitations in `paired_proof_plan.md`.
- The milestone ordering note in `first_milestone.md`.

# Strongest objection

Calling this an explicit separate theorem step may itself overstate closure, because the notes also say the positivity package is only transportable as a conditional interface and still imports manuscript-internal source-normalized background/core data rather than standing as a clean autonomous theorem.

# Needed for promotion

- State a precise local theorem with hypotheses matching the actual perturbative inputs: baseline same-point spectral gap, baseline variation control, perturbation smallness, and the holomorphic mixed-block input.
- Verify that the theorem outputs exactly the positivity/nondegeneracy and inverse-square-root whitening needed by the paired slot theorem, with no hidden extra assumptions.
- Show where the baseline same-point gap comes from in the non-zeta paired family, or else keep it explicit as an external local hypothesis.
- Then restate the paired patch order so the slot theorem cites this local theorem rather than burying positivity inside `minimal admissibility`.
