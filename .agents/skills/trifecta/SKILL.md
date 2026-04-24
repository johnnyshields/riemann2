---
name: trifecta
description: Post-work synthesis with parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Trifecta

Post-work synthesis via `role prompt: trifecta-analyst`. Follow
`.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`State ledger separation`, and `Capture before shutdown, forward-carry at
dispatch`. Use the inherited Codex model by default.

`$ARGUMENTS`: empty -> analyze most recent work; topic phrase -> focus all
analysts; lore file path -> analyze that file.

## Preamble

1. Read the most recent team dir's `findings.md` and `uv.md`, recent `lore/`
   entries, `git log --oneline -n 20`, and relevant paper sections.
2. Write a <=30-line key-findings summary for all briefings.
3. Create `<paper>/teams/<ts>-trifecta-<slug>/`. Copy forward `findings.md` and
   `uv.md`, initialize `attempts.md`, prune, and write `dispatch.md`.

## Dispatch

When delegated teamwork is authorized, record team name `trifecta-<slug>` in
`dispatch.md`. Spawn the analyst lanes needed for the question; a full pass uses
deep internal insights, literature, and under-the-nose connections. Brief with
the autoresearch metaprompt, full `findings.md`, 9-field schema,
writing-discipline reminder, self-deposit checklist, no `uv.md` content, and
the key-findings summary.

- **`analyst-deep-insights`** - internal structural analysis: what recent
  findings reveal, hidden connections, and new directions.
- **`analyst-lit-search`** - external literature via official sources, papers,
  and web search when available. Return problem, connection, progress level,
  and refs with URLs/DOIs.
- **`analyst-under-nose`** - bold or speculative connections to fundamental
  math. Check `findings.md` Negative first and flag overlaps.

Individual per-analyst lore files are forbidden; the coordinator writes one
consolidated entry.

## Continuing Cycle

Verify deposits. Walk each report by `State ledger separation`: reusable
synthesis to `findings.md`, new proof obligations to `uv.md`, route outcomes to
`attempts.md`, paper-ready additions to `paper-updates.md`, and consolidated
synthesis to lore.

Write ONE lore file `lore/<yyyymmdd>-trifecta-<slug>.md`: top-level summary,
section-by-section notes, literature ranked by strength, under-the-nose
connections ranked by actionability with Negative overlaps resolved, suggested
paper additions, and new references.

Keep analysts alive for follow-up synthesis and adjacent angles while their
context is fresh. Use `send_input` to push promising threads or ask for scoped
negative checks. Use `close_agent` only at a terminal condition, explicit user
halt, stale long-idle team, or when replacement is clearly better. Commit lore
and team dir by named paths.
