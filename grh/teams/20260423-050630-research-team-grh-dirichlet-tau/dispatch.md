# Dispatch

## Resume dispatch 20260424-183416

Team name: `research-resume-grh-dirichlet-tau-20260424-183416`

Base commit: `b03da4c`

Resume target: continue the existing team dir
`grh/teams/20260423-050630-research-team-grh-dirichlet-tau` in place. Do not
create a sibling team dir.

Roster:

- Beauvoir (`019dbeda-2b9e-7a53-89c1-2218ff892545`):
  `agents/20260424-183416-gap-compact-regularization/` - UV-016 gap-closer.
- Jason (`019dbeda-2c40-7ed0-a5ba-a9076f939fc7`):
  `agents/20260424-183416-explorer-background-multiplicity/` - UV-016
  source/bookkeeping explorer.
- Sartre (`019dbeda-2d23-7da1-adf1-a557dccad97b`):
  `agents/20260424-183416-verifier-slot-skeleton/` - UV-017 adversarial
  verifier for the current paired slot skeleton.
- Noether (`019dbf02-0a72-7c51-8106-50d5e29b27fa`):
  `agents/20260424-192025-gap-uv017-coefficient-freeze/` - UV-017 gap-closer
  for the coefficient/freeze-rule lemma after the staged UV-016 source theorem.

Verifier queue: the UV-017 skeleton in
`agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md` is useful
but not yet adversarially checked. Verify it while UV-016 work continues.

Current targets:

- UV-016: prove, reduce, or sharply obstruct the compact paired
  source-package closure. Ground truth: a theorem-strength compact-interval
  regularization argument plus theorem-ready `B_chi^pair` and multiplicity
  bookkeeping, or the smallest concrete substatement blocking that package.
- UV-017: verify the paired slot proof skeleton against hidden assumptions.
  Ground truth: decide whether the skeleton cleanly separates manuscript-local
  algebra from the genuinely missing paired-family content.
- UV-017 follow-up: prove, reduce, or sharply obstruct the coefficient /
  freeze-rule lemma saying the source scalar is the pure local value parameter
  to first order, with no hidden `c_chi(m) S_chi^pair` renormalization.

In-scope files and lines:

- `findings.md`, `uv.md`, `attempts.md`, this `dispatch.md`, `collation.md`.
- `handoff-status-report.md`, `synthesis.md`, `birds-eye-view-for-rh-agent.md`.
- `notes/priority.md`, `notes/dirichlet_paired_source.md`,
  `notes/paired_source_package.md`, `notes/paired_compact_theorem.md`,
  `notes/paired_proof_plan.md`, `notes/paired_slot_hypotheses.md`,
  `notes/paired_slot_realization.md`, `notes/paired_value_channel.md`,
  `notes/paired_normalization_compatibility.md`,
  `notes/whitening_interface.md`.
- `paper/dirichlet_paired_source_package_candidate.tex`,
  `paper/dirichlet_paired_source_candidate.tex`,
  `paper/source_theorem_candidate_note.tex`,
  `paper/strip_edge_kernel_note.tex`.
- `rh/proof_of_rh.tex:271-301`, `426-469`, `1392-1457`,
  `1497-1613`, `1640-1679`, `5711-5790`.
- Prior reports:
  `agents/20260424-160512-paired-regularization-package-verifier/report.md`,
  `agents/20260424-171036-paired-bookkeeping-block-verifier/report.md`,
  `agents/20260424-175245-paired-slot-proof-skeleton-routeA/report.md`,
  plus any report named in the target notes.

Protected surfaces for agents:

- Do not edit `rh/proof_of_rh.tex`, `AGENTS.md`, `lore/`, top-level team
  files (`findings.md`, `uv.md`, `attempts.md`, `dispatch.md`,
  `collation.md`, `paper-updates.md`), existing notes, existing paper notes,
  or other agents' dirs.
- Agents may write only under their assigned fresh `agents/<slug>/` dir:
  `report.md`, `notes/`, and `scripts/`.

Non-goals:

- Do not try to prove GRH/ERH/tau.
- Do not promote anything into `rh/proof_of_rh.tex`.
- Do not relitigate tau priority unless it directly changes UV-016.
- Do not treat the compact paired package as already theorem-safe.

Budgets/timeouts:

- First deposit target: one concise report per agent, focused on a theorem,
  sharp obstruction, or smallest missing substatements.
- Any computation must be written to a file under the agent's `scripts/` before
  execution and cited in the report.
