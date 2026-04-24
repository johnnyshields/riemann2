---
name: findings-prune
description: When <team-dir>/findings.md exceeds 200 lines, prune. Promote stale-but-proven bullets into the paper, move grep-worthy entries to <paper>/findings-in-paper.md, and remove noise. Keeps findings.md briefing-size.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Findings Prune

Maintenance pass when `<team-dir>/findings.md` outgrows brief-size.

## Protocol

Read the file. For each bullet, assign one of:

- **Keep** - active: open gap still blocking, Negative still guiding retry
  avoidance, Goodie still reused, Structural still informing cycles.
- **Promote** - matured into a theorem or remark belonging in
  `<paper>/<main>.tex`. This skill does not promote; draft a TODO in the next
  session-handoff or a lore note.
- **Archive** - still useful reference but no longer needs briefing paste. Move
  to `<paper>/findings-in-paper.md` with `Archived-on: <yyyymmdd>`.
- **Remove** - redundant paraphrase, explicit supersession, or route history
  that belongs only in `attempts.md`.

If a bullet is an open proof obligation, move the precise missing sub-statement
to `uv.md` instead of preserving it as prose.

Apply. Verify `<team-dir>/findings.md` is <=180 lines, ideally <=150.

If creating `findings-in-paper.md`, head it:

```markdown
# Findings (in paper)
Entries that were active in `findings.md` but have since been absorbed into
`<paper>/<main>.tex`. Grep index, not authoritative.

---
```

Stage both files by name. Commit
`findings: prune <N> (promote/archive/remove: A/B/C)`. Body lists counts and
queued `Promote` follow-ups.

## When

After a `research-capture` pushes the file over 180 lines, or over 200 as a
hard threshold. Avoid pruning during an active cycle when agents may be using
the current briefing. Age alone is not a prune trigger; relevance is.
