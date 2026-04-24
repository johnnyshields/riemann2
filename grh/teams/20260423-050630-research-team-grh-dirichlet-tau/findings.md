# Findings

Active GRH / Dirichlet / tau knowledge base for this resumed cycle. Provenance
is the supplied team dir unless another path is named.

## Structural

- **The RH draft has a source-light local layer, then a zeta-source layer.**
  The local phase, jet, whitening, and odd-projector package is the portable
  template; the first explicit zeta-side source input starts at
  `rh/proof_of_rh.tex:271`. Provenance:
  `synthesis.md`, `handoff-status-report.md`,
  `paper/local_odd_projector_note.tex`.
- **`S(m)` is best read as a positive strip-edge zero kernel.** One-zero
  kernel positivity is solid, but the canonical completed-quotient source
  theorem for the paper's `q` remains missing. Provenance:
  `notes/scattering_generalization.md`, `notes/source_theorem_gap.md`,
  `paper/strip_edge_kernel_note.tex`, `paper/source_theorem_candidate_note.tex`.
- **Primitive Dirichlet paired source-plus-slot is the best first non-zeta
  exact-source target from current scope alone.** Use
  `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)` and
  `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)`. Provenance:
  `notes/priority.md`, `notes/dirichlet_paired_source.md`,
  `paper/dirichlet_paired_source_candidate.tex`.
- **The compact paired source package is blueprint/schema only.** The first
  real family-specific burden inside it is compact-interval
  convergence/regularization, with unified `B_chi^pair` and multiplicity
  bookkeeping attached immediately after the theorem rather than hidden in the
  theorem body. Provenance: `notes/paired_source_package.md`,
  `agents/20260424-160512-paired-regularization-package-verifier/report.md`,
  `agents/20260424-171036-paired-bookkeeping-block-verifier/report.md`.
- **The exact paired slot theorem has a clean conditional skeleton.** Once the
  paired source package, symmetric local normal form, microscopic holomorphy,
  same-point positivity/nondegeneracy, and holomorphic whitening exist, the RH
  manuscript's local algebra gives the value-channel expansion. The missing
  point is a non-tautological coefficient lemma: `S_chi^pair(m)` must be the
  pure local value parameter to first order, with value-parameter holomorphy,
  explicit freeze rules, and no hidden scalar renormalization. Provenance:
  `agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md`,
  `agents/20260424-183416-verifier-slot-skeleton/report.md`,
  `notes/paired_slot_hypotheses.md`, `notes/paired_value_channel.md`.
- **The post-theorem bookkeeping block has the right scope.** It may name
  unified `B_chi^pair`, its safe component list, multiplicity bookkeeping, and
  scoped notation aliases; it may not claim exact slot realization, canonical
  source-free coefficient matching, or whitening closure. Provenance:
  `agents/20260424-171036-paired-bookkeeping-block-verifier/report.md`.
- **The paired quotient sign convention is adversarially fixed for the current
  quotient.** For the
  fixed quotient `Xi_chi(2s-1)/Xi_chi(2s)`, Jason's one-zero check finds the
  positive strip-edge kernel as `-1/2 Phi'/Phi`, not `+1/2 Phi'/Phi`, and
  Sartre's adversarial audit confirms the older positive-exponent route is
  inconsistent as written. Use the negative boundary exponent with `q=Theta'`,
  or explicitly change `q`/invert the quotient. Provenance:
  `agents/20260424-183416-explorer-background-multiplicity/report.md`,
  `agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py`,
  `agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md`.
- **Compact zero-regularization reduces to Hadamard edge-difference
  cancellation under standard nonprincipal completed-function inputs.** Beauvoir's proof note argues that subtracting
  the two edge logarithmic-derivative sums cancels the genus-one constants and
  `1/rho` terms, leaving an `O_I(|rho|^{-2})` summand with uniform compact
  convergence and fixed derivative convergence; Sartre's adversarial audit
  accepts the proof in that scoped form. Source citation of the standard
  completed-\(L\) inputs is still needed before paper promotion. Provenance:
  `agents/20260424-183416-gap-compact-regularization/report.md`,
  `agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md`,
  `agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md`.
- **Tau is a self-dual phase-channel stress test, not the first exact `S(m)`
  target.** Tau has only a conditional compact source-package blueprint; paired
  Dirichlet remains sharper for exact source-plus-slot work. Provenance:
  `notes/tau_localization.md`,
  `agents/20260424-131812-tau-vs-dirichlet-routeB/report.md`,
  `agents/20260424-140954-tau-source-package-routeA/report.md`.

## Negative

- **Do not claim the current RH draft extends to GRH, ERH, or tau.**
  Current support stops at formal local templates conditional on new
  family-specific source and local realization theorems. Provenance:
  `handoff-status-report.md`, `synthesis.md`.
- **The single Dirichlet quotient is not yet an exact `S(m)`-slot solution.**
  It is a serious phase-channel candidate, but paired remains the conservative
  scalar-amplitude target from current scope alone. Provenance:
  `notes/dirichlet_channel.md`, `notes/dirichlet_paired_source.md`.
- **Denominator comparability does not by itself give same-point positivity.**
  Positivity/nondegeneracy must stay as an explicit local whitening hypothesis
  until a separate spectral-gap stability argument is proved. Provenance:
  `notes/paired_slot_hypotheses.md`, `notes/whitening_interface.md`.
- **A paired slot identity can be tautological unless the coefficient is fixed
  independently.** Defining `R_chi^pair` after subtracting a chosen linear term
  does not prove source-to-slot realization; UV-017 needs an independent
  normalization/freeze-rule check. Provenance:
  `agents/20260424-183416-verifier-slot-skeleton/report.md`.
- **Compact regularization is not yet a theorem endpoint.** The safe promoted
  endpoint today is still the broader compact paired source-package blueprint.
  Provenance:
  `agents/20260424-143617-paired-regularization-plan-verifier/report.md`,
  `agents/20260424-160512-paired-regularization-package-verifier/report.md`.
- **Do not use the old paired positive-exponent convention as written.** It is
  sign-reversed for the positive source kernel under the fixed quotient.
  Provenance: `agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md`.

## Goodies

- **Abstract odd-germ/projector layer.** `paper/local_odd_projector_note.tex`
  gives a source-light theorem template once an odd holomorphic transverse
  scalar with boundary control is available.
- **Positive strip-edge kernel lemma.** `paper/strip_edge_kernel_note.tex`
  gives the one-zero kernel identity and conditional tail-curvature layer.
- **Paired source-package candidate text.**
  `paper/dirichlet_paired_source_package_candidate.tex` is the current
  theorem-facing blueprint for the first paired Dirichlet source step.
- **Paired source-and-slot candidate text.**
  `paper/dirichlet_paired_source_candidate.tex` records the broader two-step
  target and its deferred local admissibility burden.

## Open Gaps

- **Paired compact source package.** See UV-016.
- **Exact paired source-to-slot realization.** See UV-017.
- **Corrected odd/transverse realization and boundary package.** See UV-018.
- **Canonical zeta source theorem for `q` and `S`.** See UV-019.
- **Tau compact source/localization package.** See UV-020.
- **Paired quotient sign normalization.** See UV-021.
