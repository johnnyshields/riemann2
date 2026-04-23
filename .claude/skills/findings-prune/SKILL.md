---
name: findings-prune
description: When <team-dir>/findings.md exceeds 200 lines, prune. Promote stale-but-proven bullets into the paper, move grep-worthy entries to <paper>/findings-in-paper.md, and remove noise. Keeps findings.md briefing-size.
---

# Findings Prune

Maintenance pass when `<team-dir>/findings.md` outgrows brief-size (~200
lines).

## Protocol

Read the file. For each bullet, assign one of:

- **Keep** — active: open gap still blocking, Negative still guiding
  retry avoidance, Goodie still reused, Structural still informing
  cycles.
- **Promote** — matured into a theorem / remark belonging in
  `proof_of_rh.tex`. This skill does NOT promote; draft a TODO in the
  next session-handoff or a lore note.
- **Archive** — still useful reference but no longer needs briefing-
  paste. Move to `<paper>/findings-in-paper.md` (create if absent)
  with a trailing `Archived-on: <yyyymmdd>` line. Typical: structural
  findings fully absorbed into a paper theorem; goodies with
  well-known grep-able locations.
- **Remove** — redundant paraphrase, explicit supersession. Delete;
  git log preserves.

Apply. Verify `wc -l <team-dir>/findings.md ≤ 180` (ideally ≤150).

If creating `findings-in-paper.md`, head it:

```markdown
# Findings (in paper)
Entries that were active in `findings.md` but have since been absorbed
into `<paper>/<main>.tex`. Grep index — not authoritative.

---
```

Stage both files by name. Commit
`findings: prune <N> (promote/archive/remove: A/B/C)`. Body lists
counts and queued `Promote` follow-ups.

## When

After a `research-capture` pushes the file over 180 lines (early
warning), or over 200 (hard threshold). Never during an active cycle —
agents may be using the current briefing. Age alone isn't a prune
trigger; relevance is.
