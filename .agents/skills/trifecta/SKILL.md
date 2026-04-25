---
name: trifecta
description: Post-work synthesis with researchers in synthesis mode, one per axis (internal insights, external literature, hidden connections). Produces one consolidated lore entry.
---

# Trifecta

Post-work synthesis via researchers in `synthesis` mode, one per axis. See `Dispatch`, `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: empty → analyze most recent work; topic phrase → focus all axes; lore file path → analyze that file.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`, recent `lore/`, `git log --oneline -n 20`, relevant paper sections.
2. Write a ≤30-line key-findings summary for all briefings.
3. Create `<paper>/teams/<ts>-trifecta-<slug>/`. Copy forward `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `trifecta-<slug>` in `dispatch.md`. Spawn one researcher per axis the question needs; full pass uses all three. Brief with `_autoresearch.md`, full `findings.md`, 9-field schema, writing-discipline reminder, deposit path, self-deposit checklist, no `uv.md` content, the key-findings summary.

Axes (one researcher each, `synthesis` mode + axis tag in brief):

- **internal insights** — internal structural analysis: what recent findings reveal, hidden connections, new directions.
- **literature** — external literature via official sources, papers, web search when available. Return problem, connection, progress level, refs with URLs/DOIs.
- **under-the-nose** — bold or speculative connections to fundamental math. Check `findings.md` Negative first and flag overlaps.

No per-axis lore files; the coordinator writes one consolidated entry.

## Continuing Cycle

Verify deposits. Walk each report per `Ledger separation`: synthesis → `findings.md`, new obligations → `uv.md`, outcomes → `attempts.md`, paper-ready → `paper-updates.md`, consolidated synthesis → lore. Every proposed connection gets a route row citing the report or a `collation.md` no-action note.

Write ONE lore file `lore/<yyyymmdd>-trifecta-<slug>.md`: top-level summary, section-by-section notes, literature ranked by strength, under-the-nose connections ranked by actionability with Negative overlaps resolved, suggested paper additions, new references.

Keep researchers alive for follow-up synthesis and adjacent angles. `send_input` to push promising threads or ask for scoped negative checks. `close_agent` only at terminal condition, halt, stale team, or clear better replacement. Commit lore and team dir by named paths.
