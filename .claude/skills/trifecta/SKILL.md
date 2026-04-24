---
name: trifecta
description: Post-work synthesis — three parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

# Trifecta

Three-angle post-work synthesis via `subagent_type: trifecta-analyst`.
Follows CLAUDE.md `Briefing rule`, `Team dirs and agent self-deposit`, `Capture before shutdown, forward-carry at dispatch`.

`$ARGUMENTS`: empty → analyze most recent work (git log + recent
lore); topic phrase → focus all three; lore file path → analyze that
file.

## Preamble (forward-carry first — `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`, recent
   `lore/` entries, and `git log --oneline -n 20`. Skim relevant paper
   sections.
2. Write a ≤30-line key-findings summary; it's pasted into all three
   briefings.
3. Create `<paper>/teams/<ts>-trifecta-<slug>/`. Copy forward
   `findings.md`; prune.

## Dispatch

`TeamCreate team_name: "trifecta-<slug>"`. Spawn three analysts
(`subagent_type: trifecta-analyst`) with the standard briefing (full
`findings.md`, 7-field schema, writing-discipline reminder, self-
deposit checklist), **no `uv.md` content** (trifecta analysts are the
textbook spoiler-prone case), and the key-findings summary.

- **`analyst-deep-insights`** — internal structural analysis per
  section: what recent findings reveal, hidden connections, new
  directions. Observations only, no new theorems.
- **`analyst-lit-search`** — external literature via WebSearch. For
  each connection: problem, how our result connects, whether it
  provides progress, key refs with URLs/DOIs. No paper-change
  proposals.
- **`analyst-under-nose`** — bold / speculative connections to
  fundamental math. Before proposing, must check `findings.md`
  §Negative and flag any match instead of re-proposing a ruled-out
  route.

Individual per-analyst lore files are forbidden — the coordinator
writes one consolidated entry.

## Post-cycle (capture before shutdown — `Capture before shutdown, forward-carry at dispatch`)

Verify deposits. Walk each report, process findings through `Claim lifecycle (git-as-archive)` —
append Negative / Goodie / Open-gap bullets to this team dir's
`findings.md`, file new UVs where speculative connections reveal
gaps, stage paper-ready additions in `paper-updates.md`.

Write ONE lore file `lore/<yyyymmdd>-trifecta-<slug>.md`: top-level
summary, section-by-section, literature ranked by strength, under-
the-nose connections ranked by actionability (with Negative overlaps
resolved), suggested paper additions, new references.

Shut down, `TeamDelete`, commit lore + team dir, cite the dir.
