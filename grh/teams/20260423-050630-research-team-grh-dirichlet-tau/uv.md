# UV Ledger

## GRH / Dirichlet / Tau

- **UV-016** - paired compact source-package closure.
  Prove a compact-interval source package for primitive Dirichlet pairs built
  from `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)`: one unified theorem-ready
  `B_chi^pair`, multiplicity bookkeeping compatible with the same compact
  identity, and a source-normalization statement using the sign-audited
  convention. Provenance:
  `notes/paired_source_package.md`;
  `agents/20260424-160512-paired-regularization-package-verifier/report.md`;
  `agents/20260424-171036-paired-bookkeeping-block-verifier/report.md`;
  `agents/20260424-183416-explorer-background-multiplicity/report.md`;
  `agents/20260424-183416-gap-compact-regularization/report.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md`.
  Current role: immediate non-zeta frontier.
  Current reduction: compact zero-regularization is adversarially checked under
  standard primitive nonprincipal completed-function inputs; the remaining
  burden is the explicit `B_chi^pair` split in the sign-audited convention plus
  source citations for those standard inputs.

- **UV-017** - exact paired local `S(m)`-slot realization.
  Prove that the scalar `S_chi^pair(m)=q_chi^pair(m)-B_chi^pair(m)` from
  UV-016 is exactly the coefficient in
  `Delta_chi^pair=S_chi^pair A_val,chi^pair+R_chi^pair`, with symmetric local
  normal form, microscopic holomorphy, value-parameter differentiability or
  joint holomorphy, same-point positivity/nondegeneracy, holomorphic whitening,
  explicit freeze rules, and a normalization check excluding
  `c_chi(m) S_chi^pair` or an upstairs-only surrogate. Provenance:
  `notes/paired_slot_hypotheses.md`;
  `agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report.md`.
  Current role: second-step non-zeta frontier after UV-016.

- **UV-018** - corrected odd/transverse realization and boundary package.
  After paired slot realization, construct the corrected odd/transverse scalar,
  boundary estimate, and odd-projector input in a non-zeta family; do not fold
  this into UV-016 or UV-017. Provenance: `notes/odd_package_transport.md`,
  `notes/boundary_package.md`, `notes/corrected_whitening_transport.md`.
  Current role: downstream burden.

- **UV-019** - canonical zeta source theorem for `q` and `S`.
  In the RH draft, promote a normalized compact-interval source theorem for
  `phi(s)=Lambda(2s-1)/Lambda(2s)`, including the phase convention, one-zero
  contribution, compact summation/regularization, background naming, and
  multiplicity convention. Provenance: `notes/zeta_source_package.md`,
  `notes/quotient_normalization.md`, `notes/zeta_source_proof_plan.md`.
  Current role: highest-value RH-facing patch, not the active non-zeta target.

- **UV-020** - tau compact source/localization package.
  For the Ramanujan tau `L`-function, produce a tau-specific compact source
  package and local realization through the five degree-sensitive checkpoints:
  source decomposition, microscopic denominator/holomorphy radius, block
  scaling hierarchy, whitening gain/boundary estimate, and growth bookkeeping.
  Provenance: `notes/tau_localization.md`;
  `agents/20260424-140954-tau-source-package-routeA/report.md`.
  Current role: secondary self-dual stress test behind paired Dirichlet.

- **UV-021** - paired quotient sign normalization.
  Rewrite the source-normalization interface for the fixed paired quotient
  `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)` against the positive strip-edge
  kernel and the desired source split `q_chi^pair=B_chi^pair+S_chi^pair`.
  The adversarially checked convention for the fixed quotient is negative
  boundary exponent with `q=Theta'`, equivalently
  `q_chi^pair=-1/2 Phi'/Phi` at the zero-source level; positive exponent needs
  `q=-Theta'` or inverse quotient. Provenance:
  `agents/20260424-183416-explorer-background-multiplicity/report.md`;
  `agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py`;
  `agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md`;
  `notes/dirichlet_paired_source.md`;
  `paper/dirichlet_paired_source_candidate.tex`.
  Current role: subgap of UV-016; convention chosen, source package rewrite
  still needed.
