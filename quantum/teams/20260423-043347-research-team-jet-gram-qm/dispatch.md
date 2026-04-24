# Dispatch

## Resume dispatch 20260424-183112

Commit at dispatch preparation: `5dcbe43`.

Team name: `research-resume-20260423-043347-research-team-jet-gram-qm-20260424-183112`.

Existing team dir:
`quantum/teams/20260423-043347-research-team-jet-gram-qm`.

Main draft:
`quantum/paper/jet_gram_quantum_note.md`.

Recovered frontier:
- `quantum/paper/jet_gram_quantum_note.md:783-794` lists four open problems:
  multiparameter matrix/frame canonicity, matrix-valued two-point data beyond
  principal-angle/projector spectra, `O_r` versus `A_r`, and a natural
  dynamical/experimental model.
- `HANDOFF-20260424.md` adds the same strategic priority: finish the
  matrix-story closure, then compact the note if no stronger matrix package
  appears quickly.
- `findings.md` records the present positive core and the missing items.
- `INDEX.md` maps proof deposits for the operator/subspace, benchmark, and
  dynamical packages.

Resume checkpoint files initialized:
- `uv.md`: UV-011 through UV-015.
- `attempts.md`: standard attempts table plus frontier summary.
- `collation.md`: capture sweep and no-report note for the stale
  biunitary-classification subdir.

Protected surfaces for all agents:
- Do not edit `quantum/paper/jet_gram_quantum_note.md`,
  `quantum/paper/benchmark_map.md`, `findings.md`, `uv.md`, `attempts.md`,
  `dispatch.md`, `collation.md`, `paper-updates.md`, `AGENTS.md`, `lore/`, or
  any other agent directory.
- Deposit only under the assigned fresh
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183112-<agent-slug>/`
  directory.

Non-goals:
- Do not modify the RH draft.
- Do not add more isolated benchmark examples unless they prove a genericity
  theorem or kill one.
- Do not call a matrix/frame object canonical unless the exact invariance class
  is stated.
- Do not promote computational evidence to proof.

Fixed harness:
- `quantum/paper/jet_gram_quantum_note.md`.
- `quantum/paper/benchmark_map.md`.
- This team dir's `findings.md`, `uv.md`, `attempts.md`, `collation.md`.
- Prior reports cited in `INDEX.md` and in the assigned brief.

Ground-truth checks:
- UV-011: either an explicit multiparameter matrix/frame theorem with its
  hypotheses, or a sharp no-go showing why the subspace package is the maximal
  canonical object from the given data.
- UV-012: either a canonical two-point matrix object beyond
  `(C,K_\pm,V)` or a proof that frame comparison matrices are exactly the
  biunitary orbit with singular values/principal angles as complete data.
- UV-013: a criterion or scoped negative for `A_r` versus `O_r`.
- UV-014: a concrete dynamical/experimental protocol not merely restating
  projector products, or a scoped negative.
- UV-015: a theorem-level genericity statement or a precise obstruction.

Roster decision after user redirection:
- The user clarified that a 3+3+2 roster is not required and asked for the best
  continuation after deeply reading the directory.
- Deep read result is recorded in `notes/resume-readthrough-20260424.md`.
- Best next move is a focused UV-012 attack, because the prior agents already
  developed the subspace/operator package and left exactly one stale no-deposit
  target: `agents/20260424-040334-attack-biunitary-classification/`.

Focused roster:
- Gap closer:
  `agents/20260424-183451-gap-biunitary-matrix-finality/` targets UV-012.
- Adversarial verifier:
  `agents/20260424-183451-verifier-biunitary-finality/` attacks the gap-closer
  theorem and decides whether UV-012 can be closed negatively.

Run budget:
- First return should be a deposited report, not a chat-only summary.
- Computational claims require scripts written under the agent's `scripts/`
  directory before execution and cited from the report.
- If full closure is too hard, reduce to the smallest list of concrete
  unresolved sub-statements.
