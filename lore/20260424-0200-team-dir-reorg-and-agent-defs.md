# 2026-04-24 02:00 — team-dir reorg, agent defs, handoff discipline

Meta-flow reorg of the coordinator policy: directory structure, agent
provenance rules, cross-cycle handoff. No research results here —
those go in per-cycle team dirs (see `feedback_lore_scope.md` memory).

## Overview

Three linked changes driven by observed handoff bugs:

1. **Directory structure.** Replace `tasks/<ts>-<type>-<slug>/` with
   `<paper>/teams/<ts>-<team-slug>/`, and nest per-agent work under
   `<paper>/teams/.../agents/<ts>-<agent-slug>/`. One team dir per
   dispatch (not three siblings). `<paper>` is the paper subtree
   (`paper`, `grh`, `quantum`, ...).

2. **Canonical state moves into team dirs.** `findings.md` and `uv.md`
   (markdown, replacing `unverified.tex`) now live inside each team
   dir, not at paper root. New `paper-updates.md` is the team lead's
   staged edits destined for `<main>.tex`. Cross-cycle persistence is
   achieved by *forward-carry*: first act of a new cycle is to copy
   the prior team dir's `findings.md` / `uv.md` in, prune, then brief.

3. **Agent provenance is always the agent's job.** New
   `.claude/agents/` directory with 10 role defs + a shared
   `_provenance.md` copied into each. Agents deposit `report.md`,
   `scripts/`, `notes/` under their own subdir; team leads brief,
   collate, commit — they do not ghost-write. Scripts must be written
   to a file before running (no `-c`, no heredoc pipes).

## Key decisions and rationale

- **Team dirs authoritative, no canonical findings/unverified at
  paper root.** Alternative was to keep both (dual ledger). Rejected
  because two sources of truth drift. Forward-carry makes the handoff
  an explicit, reviewable act instead of implicit shared state.

- **uv.md as markdown, drop unverified.tex.** The paper no longer
  `\input`s a UV ledger. UVs are workflow artifacts, not paper
  content; keeping them in LaTeX was forcing compile-dependency for
  no rendering benefit.

- **UV-NNN stays globally unique across team dirs.** Team lead takes
  `max(UV-NNN) + 1` across all `teams/*/uv.md` when filing a new one.
  Alternative (per-cycle renumbering) would break cross-cycle
  references.

- **One team dir per `research-team` cycle (8 agent subdirs), not
  three siblings.** Old three-sibling model forced the team lead to
  remember which dir was which; new model groups by dispatch.

- **`_provenance.md` copied verbatim into each agent def.** Alternative
  was a "read this file first" pointer; rejected because agents
  skipping the pointer would miss rules. Duplication is the cost of
  guaranteed enforcement; a sync script `scripts/wip/rename_skills.sh`
  pattern can extend to a provenance-sync helper if the block drifts.

- **Handoff bug is primarily a capture problem.** §8a "capture before
  shutdown" + "forward-carry at dispatch" addresses this directly:
  team lead walks every agent report before `TeamDelete` and files
  UVs/findings/demotes; next cycle starts from those files, not from
  agent reports 30 subdirs deep.

## Files created / modified

**Modified:**
- `CLAUDE.md` — full policy rewrite. §1 files table, §3 autonomy,
  §3a loop step 1, §5 briefing, §6 team-dir tree, §8 lifecycle,
  §8a (new) capture + forward-carry, §9 provenance, §10 commit-while-
  agents-work, §12 LaTeX conventions. Also `paper/` → `<paper>/`,
  `teammate` → `agent`, `task-dir` → `team-dir` throughout.
- All 19 `.claude/skills/*/SKILL.md` — mechanical sweep + targeted
  rewrites for `research-team`, `research-attack`, `paper-referee`,
  `paper-harden`, `research-audit`, `trifecta`, `cycle-status`,
  `session-handoff`, `paper-rewrite`.

**Created:**
- `.claude/agents/_provenance.md` — shared meta rules.
- `.claude/agents/{gap-closer, explorer, verifier-adversarial,
  verifier-source, auditor, fixer, referee, rewriter, harden-reviewer,
  trifecta-analyst}.md` — role defs with provenance block inlined +
  role-specific instructions.
- `scripts/wip/rename_skills.sh` — one-shot mechanical sed sweep used
  for the skills pass. Idempotent; keep for future similar renames.

## Dependencies

None. Pure policy / markdown / shell-script.

## Security considerations

None — internal workflow reorg.

## Testing approach

No automated tests. Verification:

- `grep -r` sweeps confirm no stale references (`unverified.tex`,
  `proof_of_rh.tex`, `task-dir`, `teammate`, bare `paper/`) remain in
  `.claude/` or `CLAUDE.md`.
- Architecture dry-runs happen on the next live dispatch — if an
  agent's deposit structure doesn't match `<paper>/teams/.../agents/...`
  or if the team lead catches themselves ghost-writing, tighten the
  relevant skill / agent def.

## Migration

Existing state in `quantum/`, `grh/`, and `paper/` predates this
reorg. Not migrating proactively:

- Old top-level `findings.md` / `unverified.tex`: will be absorbed
  into the *next* cycle's team-dir forward-carry. At that point the
  old files can be removed in the same commit.
- Existing `tasks/` dirs and `<paper>/tasks/` trees: leave in place as
  historical; new dispatches create `<paper>/teams/...`.

## Future enhancements

- Provenance-sync helper: a `scripts/wip/sync_provenance.sh` that
  re-copies `_provenance.md` into every agent def between the shared-
  block markers. Only needed if the block drifts.
- Machine-readable `dispatch.md` schema so `cycle-status` can parse
  expected vs landed deposits without heuristics.
- Consider a lightweight `teams/INDEX.md` per paper mapping UV-NNN →
  which team dir currently owns it (for fast lookup across cycles).
  Defer until cross-team UV lookup becomes a pain.
