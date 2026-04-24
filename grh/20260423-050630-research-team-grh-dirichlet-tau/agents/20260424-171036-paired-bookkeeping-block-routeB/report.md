## Claim

The safest placement is a two-step theorem package:

1. the theorem itself stays at blueprint level for the compact paired source package;
2. an immediately following bookkeeping block records exactly the pieces that later arguments must reuse without reinterpretation.

What must stay immediately after the theorem:

- the canonical theorem-adjacent bookkeeping symbol `B_\chi^{pair}`;
- its safe contents: conductor/scaling, gamma-derivative, and trivial-zero or pole corrections;
- the multiplicity bookkeeping tied to the same compact summation/regularization package;
- scoped parenthetical aliases explaining how this bookkeeping corresponds to earlier lane-specific notation, without asserting exact identity.

What can wait:

- exact paired `S(m)` slot realization inside the later decomposition;
- any claim that the coefficient match is canonical or source-free;
- any local whitening-interface statement;
- any exact theorem-body identification of old background symbols with `B_\chi^{pair}`.

Strongest safe roadmap sentence:

`Immediately after the compact paired source-package theorem, we fix the paired bookkeeping convention by naming the unified background term B_\chi^{pair} and its multiplicity corrections; later, once compact-interval regularization and source-normalized compatibility are proved, we show that the decomposition coefficient is the same source scalar S_\chi^{pair}(m), with exact slot realization postponed to that later step.`

Separation:

- proved: theorem-adjacent bookkeeping is the safest placement for unified background and multiplicity, and the safe named content of that block is limited to the background pieces above;
- conditional: the later decomposition should use the same source scalar `S_\chi^{pair}(m)` rather than a renormalized substitute;
- missing: compact-interval regularization, exact scalar-slot realization, canonical/source-free normalization, and any whitening interface.

## Status

proved

## Evidence

`paired_source_package.md` is decisive on placement: it says multiplicity and unified `B_\chi^{pair}` should stay out of the theorem body but be placed immediately after the theorem as explicit bookkeeping tied to the compact source package, and it limits the safe content of that block to conductor/scaling, gamma-derivative, and trivial-zero or pole corrections. The same note also marks exact `S(m)` realization and whitening as too early.

`background_unification.md` supports the same boundary: one canonical symbol is safe only with scoped role-level aliases, while exact identity between prior background symbols is not yet safe.

`paired_normalization_compatibility.md` sharpens what must be deferred: the coefficient should eventually be the same `S_\chi^{pair}(m)`, but only as a conditional source-normalized interface, not as a canonical or source-free fact already available at theorem-adjacent bookkeeping stage.

Together these notes force a narrow placement verdict: immediate post-theorem bookkeeping must fix notation and bookkeeping data that later sections will reuse verbatim, but it must not already claim the later scalar-realization theorem.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:37-67`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:69-71`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-11`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:24-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`

## Dependencies

- the placement verdict depends on the source-package note's theorem/body vs post-theorem bookkeeping split;
- the background notation part depends on the unification note's canonical-symbol plus scoped-alias rule;
- the deferral of exact `S_\chi^{pair}(m)` matching depends on the normalization-compatibility note's conditional status.

## Strongest objection

The phrase `later, once compact-interval regularization and source-normalized compatibility are proved` is still only a roadmap promise: the notes do not yet prove that this later interface can be closed without additional bookkeeping beyond what is named here, so even the roadmap sentence must not be read as evidence that the later scalar-match theorem is already structurally complete.

## Needed for promotion

- a proved compact-interval regularization/convergence result for the paired package;
- a proved source-normalized interface showing the later coefficient is exactly `S_\chi^{pair}(m)` and not a renormalized surrogate;
- a checked insertion point in the draft showing that the immediate post-theorem block is sufficient for all downstream references without forcing extra theorem-body content;
- continued avoidance of any canonical/source-free or whitening claims until separately established.
