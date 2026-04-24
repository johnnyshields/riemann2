---
name: trifecta
description: Post-work synthesis â€” three parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Trifecta

Three-angle post-work synthesis via `role prompt: trifecta-analyst`.
Follows `.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default.

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

When delegated teamwork is authorized, record team name `trifecta-<slug>` in `dispatch.md`. Spawn three analysts
(`role prompt: trifecta-analyst`, inherited Codex model) with the standard briefing,
the full `.agents/references/agents/_autoresearch.md` metaprompt, full `findings.md`,
9-field schema, writing-discipline reminder, self-deposit checklist, **no
`uv.md` content** (trifecta analysts are the textbook spoiler-prone case), and
the key-findings summary.

- **`analyst-deep-insights`** â€” internal structural analysis per
  section: what recent findings reveal, hidden connections, new
  directions. Observations only, no new theorems.
- **`analyst-lit-search`** -- external literature via official sources, papers, and web search when available. For
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


