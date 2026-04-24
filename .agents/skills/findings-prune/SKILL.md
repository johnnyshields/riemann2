---
name: findings-prune
description: When a team findings.md exceeds 200 lines, prune. Promote stale-but-proven bullets into the paper, move grep-worthy entries to a paper findings-in-paper.md, and remove noise. Keeps findings.md briefing-size.
---

# Findings Prune

Maintenance pass when `<team-dir>/findings.md` outgrows brief-size.

## Protocol

For each bullet, assign:

- **Keep** — active: open gap still blocking, Negative still guiding retry avoidance, Goodie still reused, Structural still informing cycles.
- **Promote** — matured into a theorem or remark belonging in `<paper>/<main>.tex`. Don't promote here; draft a TODO in the next session-handoff or a lore note.
- **Archive** — useful reference but no longer needs briefing paste. Move to `<paper>/findings-in-paper.md` with `Archived-on: <yyyymmdd>`.
- **Remove** — redundant paraphrase, explicit supersession, or route history that belongs in `attempts.md`.

If a bullet is an open proof obligation, move the precise missing sub-statement to `uv.md` instead of preserving it as prose.

Apply. Verify `<team-dir>/findings.md` ≤180 lines, ideally ≤150.

If creating `findings-in-paper.md`, head it:

```markdown
# Findings (in paper)
Entries that were active in `findings.md` but have since been absorbed into
`<paper>/<main>.tex`. Grep index, not authoritative.

---
```

Stage both files by name. Commit `findings: prune <N> (promote/archive/remove: A/B/C)`. Body lists counts and queued `Promote` follow-ups.

## When

After a `research-capture` pushes the file over 180, or 200 as a hard threshold. Avoid pruning during an active cycle when agents may be using the briefing. Age alone isn't a trigger; relevance is.
