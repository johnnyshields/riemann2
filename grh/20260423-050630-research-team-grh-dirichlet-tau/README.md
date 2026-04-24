# GRH / Dirichlet / Tau Research Cycle

Date: 2026-04-23
Timestamp: `20260423-050630`

## Scope

Explore how the current RH draft architecture might extend to:

- primitive Dirichlet \(L\)-functions / ERH;
- broader GRH-style completed \(L\)-function settings;
- the Ramanujan \(\tau\) \(L\)-function as a higher-degree test case.

Primary goal: identify insights that can be ported back into
`paper/proof_of_rh.tex`, especially hidden zeta-specific assumptions and any
cleaner completed-\(L\)-function abstractions.

## Task dirs

- `tasks/20260423-050630-attack-gap-grh-dirichlet-tau/`
- `tasks/20260423-050630-attack-fund-grh-dirichlet-tau/`
- `tasks/20260423-050630-verify-grh-dirichlet-tau/`

## Deliverables

- teammate reports in the task dirs;
- coordinator synthesis in this `grh/` subtree.

## Key files

- `synthesis.md` — conservative three-bin synthesis of the research-team cycle.
- `birds-eye-view-for-rh-agent.md` — handoff-style Markdown brief explaining the
  GRH/ERH/RH map, where the current zeta draft sits inside it, and what the
  current non-zeta theorem targets actually are.
- `notes/local_package_theorem.md` — sharpened boundary from the follow-up
  attack: unconditional odd-germ/projector layer, calibration only conditional.
- `notes/dirichlet_channel.md` — current honest stance on primitive Dirichlet
  channels: paired scalar as the more conservative first target, no realized
  portability claim yet.
- `notes/tau_localization.md` — current honest stance on the Ramanujan `\tau`
  case: cleaner self-dual channel candidate, but no realized localization
  package yet.
- `notes/scattering_generalization.md` — sharpened candidate-object note:
  `S(m)` behaves like a positive strip-edge zero kernel, suggesting a completed
  scattering-style target rather than a raw critical-line-value target.
- `notes/source_theorem_gap.md` — precise boundary after the archive-backed
  quotient discovery: kernel theorem proved, source theorem still conditional.
- `notes/quotient_phase.md` — quotient unimodularity update: serious phase
  candidate for Dirichlet and tau, but only at the phase-channel level.
- `notes/positive_s_implication.md` — scoped roadmap update: once a family
  theorem yields the exact `S(m)`-slot scalar, the leading-channel coefficient
  theorem is already in place; the next bottlenecks are remainder dominance and
  the odd/transverse package.
- `notes/remainder_dominance.md` — narrower version of that roadmap: remainder
  dominance is the next bottleneck only for the calibrated value-channel
  subchain, not for the whole program.
- `notes/odd_package_transport.md` — third-stage bottleneck note: after exact
  scalar-slot identification and value-channel remainder dominance, the next
  independent target is the corrected odd/transverse realization-and-boundary
  theorem.
- `notes/universal_source_kernel.md` — scoped simplification note: once a
  family-specific quotient/source theorem exists, the one-zero strip-edge
  kernel is universal upstairs, but the manuscript `S(m)` slot remains
  family-specific.
- `notes/priority.md` — two-criterion roadmap: best first non-zeta realization
  target is the primitive Dirichlet paired-scalar source theorem; best value
  back to the RH draft is the canonical zeta source theorem for `q` and `S`.
- `notes/dirichlet_paired_source.md` — exact statement of that top non-zeta
  target, with scope tightened after the later quotient and universal-kernel
  refinements.
- `notes/zeta_source_package.md` — best value-back-to-RH target, now reduced to
  one localized source-theorem package with three theorem-level parts plus two
  explicit identification/convention items.
- `notes/rh_patch_plan.md` — practical handoff note for an RH agent: where the
  canonical zeta source theorem should be inserted and why that is the
  highest-value, lowest-risk patch.
- `notes/rh_first_actions.md` — condensed action order for an RH agent: the
  exact 4-step sequence to patch the zeta source package with minimal churn.
- `notes/zeta_source_proof_plan.md` — RH-facing proof-plan note for the source
  patch: same 2-step unit, but with the theorem endpoint kept narrower than the
  current surrounding prose.
- `notes/quotient_normalization.md` — source-normalization action item for the
  RH draft: the factor-of-2 is fine, the sign is the real mismatch, and the
  clean fix is a front-loaded quotient/phase-normalization subsection.
- `notes/background_unification.md` — RH-facing notation note: use one
  canonical background symbol with scoped role-level aliases, not a claimed
  identity of `B_zeta`, `B_Aut`, and `B_bg` from the current text alone.
- `notes/q_notation.md` — RH-facing notation blocker: the `q` / `q_zeta` clash
  is localized but still needs a small source-normalization subsection rather
  than a one-line patch.
- `notes/source_package_transfer.md` — bridge note from the canonical zeta
  source package to the paired Dirichlet target: useful blueprint upstairs, but
  the theorem burden remains exact paired `S(m)`-slot realization plus paired
  background/convergence/multiplicity work.
- `notes/paired_slot_realization.md` — current sharpest non-zeta theorem target:
  paired source-plus-slot realization, with upstairs/downstairs split explicit
  and downstream remainder/odd-package burdens left separate.
- `notes/paired_slot_hypotheses.md` — refinement of that target: the exact slot
  theorem already needs minimal local analytic admissibility, not just the
  upstairs paired source theorem.
- `notes/whitening_interface.md` — theorem-facing local hypothesis block for the
  paired exact-slot theorem: microscopic holomorphy, same-point
  positivity/nondegeneracy, holomorphic whitening, and first value-channel
  derivative.
- `notes/paired_aval.md` — theorem-facing note for the paired first-order value
  direction: locally formal once admissibility is in place, but still
  conditional on a paired-family local setup.
- `notes/paired_value_channel.md` — theorem-facing note for the paired one-
  scalar value deformation: still viable, but only after the paired source slot
  and local whitening interface are fixed.
- `notes/paired_normalization_compatibility.md` — theorem-facing note for the
  exact scalar match: the paired source scalar must be the very coefficient in
  the local slot identity, not a renormalized or upstairs-only surrogate.
- `notes/same_point_positivity.md` — local whitening blueprint note: the
  manuscript uses a real perturbative same-point positivity package, but it is
  only safely extractable as a transport blueprint, not yet as a standalone
  cross-family lemma package.
- `notes/aval_transport.md` — narrow transport note: once the local symmetric
  normal form and corrected decomposition are realized, the explicit `A_val`
  matrix and `Phi_K(A_val)=0` are first-order local algebra, but the full
  calibration chain is still separate.
- `notes/variable_x.md` — UV-001 refinement: one theorem-sized gap in the main
  paper, but two-layered for transport work, with shrinking-scale source control
  and cutoff compatibility made explicit.
- `notes/denominator_theorem.md` — corrected-whitening subtarget note:
  denominator comparability is necessary and explicit, but it should be treated
  as one named subtheorem inside the larger transport package.
- `notes/corrected_whitening_transport.md` — narrow intermediate-bundle note:
  holomorphic corrected whitening plus preserved post-`Phi_K` transfer scale,
  with value-slot realization, boundary control, odd-channel transport, and
  remainder dominance still separate.
- `notes/boundary_package.md` — post-whitening refinement: the right standalone
  target is the corrected transverse realization-and-boundary package, not the
  bare boundary theorem in isolation.
- `notes/first_milestone.md` — resolves the milestone question: the first
  non-zeta exact-source milestone is still paired source-plus-slot realization,
  while corrected-whitening transport remains an earlier partial bundle.
- `notes/paired_compact_theorem.md` — theorem-facing shape note for the non-zeta
  side: the paired target should first be stated as a compact-interval source
  package blueprint, not as a global or endgame-strength theorem.
- `notes/paired_source_package.md` — sharpening of that shape: the compact
  paired source theorem must stop before exact slot realization and local
  whitening-interface claims.
- `notes/paired_proof_plan.md` — scoped milestone note: the paired source-plus-
  slot target is now a theorem-facing blueprint with explicit missing burdens,
  not a near-closed theorem.
- `paper/portability_note.tex` — broad portability note for Dirichlet,
  GRH-style settings, and the Ramanujan `\tau` test case.
- `paper/local_odd_projector_note.tex` — standalone note isolating the
  source-light odd-projector layer.
- `paper/scattering_candidate_note.tex` — candidate-object memo: `S(m)` behaves
  like a positive strip-edge zero kernel, suggesting a completed scattering
  package as the right non-zeta target.
- `paper/strip_edge_kernel_note.tex` — conservative theorem note: positive
  single-zero strip-edge kernel plus conditional omitted-tail curvature layer.
- `paper/source_theorem_candidate_note.tex` — exact target theorem for porting
  the archive-backed quotient formula into a canonical source theorem for `q`
  and `S`.
- `paper/dirichlet_paired_source_candidate.tex` — theorem-facing note for the
  current best non-zeta target: exact paired source-and-slot realization for
  primitive Dirichlet characters.
- `paper/dirichlet_paired_source_package_candidate.tex` — theorem-facing note
  for the first step only: the compact paired source-package blueprint that
  precedes exact slot realization.
