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
  `agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md`;
  `agents/20260424-183416-explorer-background-multiplicity/report-background-split.md`;
  `agents/20260424-183416-gap-compact-regularization/report-source-audit.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md`;
  `agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-paper-updates-audit.md`;
  `agents/20260424-183416-gap-compact-regularization/report-citation-fallback-plan.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-paper-updates-final-check.md`.
  Current role: immediate non-zeta frontier.
  Current reduction: compact zero-regularization is adversarially checked under
  standard primitive nonprincipal completed-function inputs; the current
  accepted subclaim is completed-Hadamard normalization with
  `B_chi,comp^pair=0`, provided `S_chi,comp^pair` sums all completed zeros and
  raw gamma/trivial-zero/pole terms are kept in a separate remark. A staged
  draft exists in `paper-updates.md` and has been patched after Sartre's
  multiplicity/realness wording audit. Citation burden is reduced for a
  working-paper draft by the DLMF-plus-Hadamard fallback stack; final textbook
  citations remain a bibliography upgrade. Final wording review is clear from
  the verifier lane. Remaining burden: coordinator decision whether to promote
  as a working source package using the fallback citation stack or keep waiting
  for clean-copy textbook citations. Do not remove this UV yet: this GRH
  directory has no canonical `grh/<main>.tex` promotion target, so the current
  endpoint remains a staged team theorem in `paper-updates.md`.

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
  `agents/20260424-183416-verifier-slot-skeleton/report.md`;
  `agents/20260424-192025-gap-uv017-coefficient-freeze/report.md`;
  `agents/20260424-183416-verifier-slot-skeleton/report-uv017-coefficient-reduction-audit.md`;
  `agents/20260424-192025-gap-uv017-coefficient-freeze/report-unit-coordinate-chart.md`.
  Current role: second-step non-zeta frontier after UV-016.
  Current reduction: source normalization and whitening linearization are not
  the remaining scalar-renormalization sites; UV-017 is now the paired
  unit-coordinate local normal-form lemma. Prove that the corrected paired
  local blocks use zeroth coordinate
  `a=q_chi^pair(m)-B_chi^pair(m)` with unit derivative
  `a(S,eta(S))=S+O(S^2)` and non-value coordinates frozen on the pure value
  path. Also prove paired holomorphy/whitening and define any downstream scalar
  readout at the same level as `A_val` or prove that it does not rescale the
  slot. The universal RH finite-\(s\) phase-kernel chart has the unit
  coordinate by direct calculation; the missing statement is that the actual
  paired corrected finite-\(s\) blocks are literally this chart with
  `Theta=Theta_chi^pair` and `q=q_chi^pair`. The staged `paper-updates.md`
  text now displays the paired `G`, `N`, and whitened block formulas as a chart
  hypothesis/definition; Sartre's formula audit found no entry-level mismatch
  with the RH finite-\(s\) formulas. `paper-updates.md` now also stages a
  conditional matrix value-slot theorem using the completed-Hadamard aliases
  for `B` and `S`, a no-extra-correction-map guard, explicit local
  admissibility hypotheses, and a derivative-form remainder criterion. This is
  still not a proved paired construction lemma. Noether's local-admissibility
  reduction proves fixed-\(m\) holomorphy/removable singularities for the
  literal chart from a local holomorphic paired phase, but leaves uniform
  microscopic radius as a pole-clearance/derivative-control hypothesis.
  Same-point positivity reduces to the explicit determinant/spectral gap
  \(q>0\) and \(2qq''+4q^4-3(q')^2>0\), with holomorphic whitening conditional
  on that gap. Sartre's exact-algebra audit verifies the removable-pole orders
  and determinant formula for the displayed chart. The next sharp target is to
  prove or refute this determinant/spectral gap for the actual completed paired
  source, starting with the one-zero strip-edge kernel and tail stability. If
  "corrected" means anything beyond this literal chart, the correction maps
  must be named and checked for unit value-coordinate derivative; determinant
  gap, uniform radius, freeze-rule remainder, and scalar readout remain open
  unless assumed.

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
  Current role: subgap of UV-016; convention chosen and adversarially checked,
  but live until the source-package rewrite actually installs the convention.
