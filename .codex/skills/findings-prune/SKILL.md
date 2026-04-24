---
name: findings-prune
description: When <team-dir>/findings.md exceeds 200 lines, prune. Promote stale-but-proven bullets into the paper, move grep-worthy entries to <paper>/findings-in-paper.md, and remove noise. Keeps findings.md briefing-size.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Findings Prune

Maintenance pass when `<team-dir>/findings.md` outgrows brief-size (~200
lines).

## Protocol

Read the file. For each bullet, assign one of:

- **Keep** â€” active: open gap still blocking, Negative still guiding
  retry avoidance, Goodie still reused, Structural still informing
  cycles.
- **Promote** â€” matured into a theorem / remark belonging in
  `<paper>/<main>.tex`. This skill does NOT promote; draft a TODO in the
  next session-handoff or a lore note.
- **Archive** â€” still useful reference but no longer needs briefing-
  paste. Move to `<paper>/findings-in-paper.md` (create if absent)
  with a trailing `Archived-on: <yyyymmdd>` line. Typical: structural
  findings fully absorbed into a paper theorem; goodies with
  well-known grep-able locations.
- **Remove** â€” redundant paraphrase, explicit supersession. Delete;
  git log preserves.

Apply. Verify `wc -l <team-dir>/findings.md â‰¤ 180` (ideally â‰¤150).

If creating `findings-in-paper.md`, head it:

```markdown
# Findings (in paper)
Entries that were active in `findings.md` but have since been absorbed
into `<paper>/<main>.tex`. Grep index â€” not authoritative.

---
```

Stage both files by name. Commit
`findings: prune <N> (promote/archive/remove: A/B/C)`. Body lists
counts and queued `Promote` follow-ups.

## When

After a `research-capture` pushes the file over 180 lines (early
warning), or over 200 (hard threshold). Never during an active cycle â€”
agents may be using the current briefing. Age alone isn't a prune
trigger; relevance is.


