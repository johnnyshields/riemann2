# Auto-run default — port of Karpathy's autoresearch loop

Date: 2026-04-23

## Context

Before this change, `CLAUDE.md §3a` ("Auto-run mode") was **opt-in**:
the coordinator only chained research cycles without stopping if the
user had explicitly said so ("keep automatically running" / "do not
stop"). The default posture was still to surface after each dispatch.

The user asked to look up Andrej Karpathy's
[`autoresearch`](https://github.com/karpathy/autoresearch) `program.md`
and incorporate its pattern here. Karpathy's document drives overnight
autonomous ML experiments with three operative ideas:

1. **NEVER STOP** — the agent must not ask "should I keep going?" or
   "is this a good stopping point?"
2. The user is likely asleep / away and expects indefinite work.
3. **When stuck, think harder** — re-read context, combine previous
   near-misses, try more radical angles; "I ran out of ideas" is not
   an acceptable terminal state.

## Decision

Flip §3a from opt-in to default for *research work*
(gap-closing / exploration / verification / synthesis / audit cycles).
Non-research, architectural, or irreversible operations still pause
for user confirmation per §3.

## What changed

Single-file edit: `CLAUDE.md §3a` rewritten (~16 lines → ~49 lines).

Key additions relative to prior §3a:

- Explicit ban on "should I keep going?" questions.
- Numbered **Loop** (state → pick next move → dispatch → collate →
  repeat), referencing §2 (dispatch selector), §5 (briefing rule),
  §8 (claim lifecycle), §10 (git workflow) — no duplication of their
  content.
- Concrete **terminal conditions**: zero open UVs + no outstanding
  `rem:wip-*`, or targeted synthesis clean under `paper-harden` /
  `paper-referee`, or explicit user halt. Compaction / handoff is
  *not* a terminal condition — resume from last recorded state.
- **When stuck** fallback: re-read `findings.md` / recent `lore/` /
  `paper/chats/`; combine near-misses; try radical redirects;
  optionally spin up `trifecta`.
- Attribution link to Karpathy's `autoresearch/program.md`.

No new files, no new skills. Policy stays centralized in CLAUDE.md so
every agent briefing picks up the change automatically.

## Non-goals

- Did **not** add a `program.md` at repo root. That would fragment
  policy that lives cleanly in CLAUDE.md today.
- Did **not** add an `/autoresearch` skill. The loop is a default
  posture, not a trigger.
- Did **not** touch §3 "Coordinator autonomy" — it already covers
  roster sizes, commit wording, slugs, etc., which §3a references
  rather than duplicates.

## Verification

The behavioral verification is the next research session — the
coordinator should chain dispatches without surfacing for routine
approval and should only pause on the §3a "pause only for" triggers.

Files:

- `CLAUDE.md` lines 72–120 (new §3a).

Plan file (out-of-tree):
`~/.claude/plans/enchanted-twirling-hamming.md`.
