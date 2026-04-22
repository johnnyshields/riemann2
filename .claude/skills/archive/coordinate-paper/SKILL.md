---
name: archive-coordinate-paper
description: RETIRED. Policy content merged into CLAUDE.md. Kept for reference only — do not invoke.
---

# Coordinate Paper

Coordinate the RH research loop without letting speculative agent output flow directly into the canonical draft.

## Arguments

The current topic, claim batch, or section focus is: $ARGUMENTS

## Canonical files

- `paper/proof_of_rh.tex` — canonical draft
- `paper/unverified.tex` — quarantine ledger
- `lore/` — workflow plans, verification notes, and agent syntheses
- `CLAUDE.md` — coordinator rules

## Rules

1. The main chat is the coordinator and the only default editor of `paper/proof_of_rh.tex`.
2. Delegated agents are read-only by default.
3. If a native team tool is unavailable, use `Task` subagents (`general` or `explore`) as the team.
4. Do not promote agent prose straight into the paper.
5. Any unsettled claim, repair, or new route goes to `paper/unverified.tex` first.
6. Promotion into the paper requires an independent adversarial check.

## Delegation template

For each research agent, require this output format:

- `Claim`
- `Status`: `proved`, `computational`, `heuristic`, `open`, or `rejected`
- `Evidence`
- `Exact refs`
- `Dependencies`
- `Strongest objection`
- `Needed for promotion`

For each verification agent, require this stance:

- Assume the claim is false or incomplete until the cited material supports it.
- Search for hidden hypotheses, circularity, missing constants, and unsupported leaps.
- Return either `verified`, `blocked`, or `rejected`, with exact reasons.

## Coordinator loop

1. Read the relevant part of `paper/proof_of_rh.tex`, the matching items in `paper/unverified.tex`, and the latest lore notes.
2. Split the task into research, source-audit, derivation, or verification subtasks.
3. Launch at least one adversarial checker for any claim that might change the proof state.
4. Update `paper/unverified.tex` before touching the canonical draft.
5. Edit `paper/proof_of_rh.tex` only after the claim is grounded and the dependencies are explicit.
6. Record the outcome in `lore/` when the session changes the operating plan or closes a significant proof-state item.
