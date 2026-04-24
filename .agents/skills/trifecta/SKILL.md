---
name: trifecta
description: Post-work synthesis with parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

# Trifecta

Post-work synthesis via `role: trifecta-analyst`. See `Dispatch` (long-lived agents), `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: empty → analyze most recent work; topic phrase → focus all analysts; lore file path → analyze that file.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`, recent `lore/`, `git log --oneline -n 20`, relevant paper sections.
2. Write a ≤30-line key-findings summary for all briefings.
3. Create `<paper>/teams/<ts>-trifecta-<slug>/`. Copy forward `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `trifecta-<slug>` in `dispatch.md`. Spawn the analyst lanes needed; full pass uses deep internal insights, literature, and under-the-nose connections. Brief with `_autoresearch.md`, full `findings.md`, 9-field schema, writing-discipline reminder, self-deposit checklist, no `uv.md` content, the key-findings summary.

- **`analyst-deep-insights`** — internal structural analysis: what recent findings reveal, hidden connections, new directions.
- **`analyst-lit-search`** — external literature via official sources, papers, web search when available. Return problem, connection, progress level, refs with URLs/DOIs.
- **`analyst-under-nose`** — bold or speculative connections to fundamental math. Check `findings.md` Negative first and flag overlaps.

No per-analyst lore files; the coordinator writes one consolidated entry.

## Continuing Cycle

Verify deposits. Walk each report per `Ledger separation`: synthesis → `findings.md`, new obligations → `uv.md`, outcomes → `attempts.md`, paper-ready additions → `paper-updates.md`, consolidated synthesis → lore. Every proposed connection gets a route row citing the report or a `collation.md` no-action note.

Write ONE lore file `lore/<yyyymmdd>-trifecta-<slug>.md`: top-level summary, section-by-section notes, literature ranked by strength, under-the-nose connections ranked by actionability with Negative overlaps resolved, suggested paper additions, new references.

Keep analysts alive for follow-up synthesis and adjacent angles. `send_input` to push promising threads or ask for scoped negative checks. `close_agent` only at terminal condition, halt, stale team, or clear better replacement. Commit lore and team dir by named paths.
