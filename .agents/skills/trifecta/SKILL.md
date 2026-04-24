---
name: trifecta
description: Post-work synthesis â€” three parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Trifecta

Three-angle post-work synthesis via `Codex agent role: trifecta-analyst`.
Follows `.agents/references/agents/_autoresearch.md`, CLAUDE.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default for
every analyst, always.

`$ARGUMENTS`: empty â†’ analyze most recent work (git log + recent
lore); topic phrase â†’ focus all three; lore file path â†’ analyze that
file.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`, recent
   `lore/` entries, and `git log --oneline -n 20`. Skim relevant paper
   sections.
2. Write a â‰¤30-line key-findings summary; it's pasted into all three
   briefings.
3. Create `<paper>/teams/<ts>-trifecta-<slug>/`. Copy forward
   `findings.md`; prune.

## Dispatch

`Codex subagent delegation when explicitly requested team_name: "trifecta-<slug>"`. Spawn three analysts
(`Codex agent role: trifecta-analyst`, the inherited Codex model by default) with the standard briefing,
the full `.agents/references/agents/_autoresearch.md` metaprompt, full `findings.md`,
9-field schema, writing-discipline reminder, self-deposit checklist, **no
`uv.md` content** (trifecta analysts are the textbook spoiler-prone case), and
the key-findings summary.

- **`analyst-deep-insights`** â€” internal structural analysis per
  section: what recent findings reveal, hidden connections, new
  directions. Observations only, no new theorems.
- **`analyst-lit-search`** â€” external literature via WebSearch. For
  each connection: problem, how our result connects, whether it
  provides progress, key refs with URLs/DOIs. No paper-change
  proposals.
- **`analyst-under-nose`** â€” bold / speculative connections to
  fundamental math. Before proposing, must check `findings.md`
  Â§Negative and flag any match instead of re-proposing a ruled-out
  route.

Individual per-analyst lore files are forbidden â€” the coordinator
writes one consolidated entry.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

Verify deposits. Walk each report, process findings through `Claim lifecycle (git-as-archive)` â€”
append Negative / Goodie / Open-gap bullets to this team dir's
`findings.md`, file new UVs where speculative connections reveal
gaps, stage paper-ready additions in `paper-updates.md`.

Write ONE lore file `lore/<yyyymmdd>-trifecta-<slug>.md`: top-level
summary, section-by-section, literature ranked by strength, under-
the-nose connections ranked by actionability (with Negative overlaps
resolved), suggested paper additions, new references.

Keep analysts alive for follow-up synthesis and adjacent angles while their
context is fresh. Use `send_input` to push promising threads or ask for scoped
negative checks. Use `close_agent` only at a terminal condition, explicit user
halt, stale long-idle team, or when replacement is clearly better. Commit lore +
team dir, cite the dir.


