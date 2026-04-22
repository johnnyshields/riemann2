# OpenCode Research Workflow

Date: 2026-04-22

## Goal

Use the main chat as a strict coordinator for the RH project: delegate research
and checking to agents, keep the canonical paper synchronized, and keep all
unverified material quarantined until it survives an adversarial verification
pass.

## Canonical artifacts

- `paper/proof_of_rh.tex`: canonical draft
- `paper/unverified.tex`: quarantine ledger for claims that are not yet ready
  for promotion
- `lore/`: workflow plans, agent syntheses, verification reports, session notes
- `CLAUDE.md`: coordinator policy that future sessions should inherit
- `.claude/commands/coordinate-paper.md`: tool-specific front-end for the
  coordinator loop

## Core principle

There are two separate pipelines:

1. Exploration pipeline
   Research agents may suggest derivations, locate dependencies, test local
   normal forms, and map proof-state options.
2. Canonical proof pipeline
   Only the coordinator updates `paper/proof_of_rh.tex`, and only after a claim
   is grounded, checked, and synchronized with `paper/unverified.tex`.

This keeps speculative agent output from silently becoming part of the proof.

## Claim lifecycle

1. Intake
   A new idea, repair, or objection arrives from the user, an agent, or the
   current paper.
2. Quarantine
   The coordinator creates or updates an item in `paper/unverified.tex` with a
   stable ID, source, status, obstruction, and promotion condition.
3. Research
   One or more research agents work on the item in read-only mode. Their job is
   to derive, cite, localize dependencies, or narrow the bottleneck.
4. Adversarial verification
   A different agent, or the coordinator directly, tries to break the claim:
   missing hypotheses, circularity, hidden appeals to numerics, ineffective
   constants, and stale citations.
5. Promotion or rejection
   If the claim survives, the coordinator edits `paper/proof_of_rh.tex` and
   marks the queue item `promoted`. If it fails, the item becomes `blocked` or
   `rejected` with a short reason.
6. Audit trail
   Any major workflow decision or closed item gets summarized in `lore/`.

## Agent roles

Use narrow roles instead of prestige framing. Good defaults:

- `research agent`: derive a claim, trace dependencies, or locate references
- `source auditor`: verify that each cited statement is actually present and used
  correctly
- `adversarial checker`: assume the claim is false until the evidence supports
  it
- `notation checker`: look for stale names, hidden branch changes, or scope
  drift

When a native team primitive is unavailable, use `Task` subagents as the team.
Prefer at least two agents when the result could change the proof state: one to
push the claim forward and one to push against it.

## Required report format

Every agent report should contain the same fields:

- `Claim`
- `Status`: `proved`, `computational`, `heuristic`, `open`, or `rejected`
- `Evidence`
- `Exact refs`
- `Dependencies`
- `Strongest objection`
- `Needed for promotion`

The main anti-sycophancy rule is simple: a delegate must be allowed to return
`unsupported`, `blocked`, or `no progress` without being penalized.

## Hallucination controls

1. Quote-first grounding
   Ask agents to cite exact file paths, line ranges, labels, or formulas before
   paraphrasing.
2. Read-only defaults
   Delegated agents should not edit the canonical paper or commit.
3. Explicit status labels
   Force every result into one of `proved`, `computational`, `heuristic`,
   `open`, `rejected`.
4. Adversarial check before promotion
   Any proof-state-changing claim must get an independent attack.
5. No citation invention
   If a source is not checked locally or from a reliable external reference, it
   stays unverified.
6. Distinguish proof from numerics
   Numerical evidence can support a queue item but cannot close it unless the
   paper explicitly adopts a computer-assisted theorem with verified bounds.
7. Sync the queue immediately
   If the paper changes, update `paper/unverified.tex` in the same session.

## Initial queue policy

Seed `paper/unverified.tex` from explicit `Work in progress` remarks already in
the manuscript. Those are the cleanest current markers of unsettled proof-state.
Over time, additional queue items can be added even if the paper does not use
that exact phrase, but explicit WIP remarks are the best initial spine.

## Portability notes

- `CLAUDE.md` is definitely active in this environment, because OpenCode loads
  it into the working context.
- `.claude/commands/*.md` are useful as repo-local command adapters, but they
  are tool-specific rather than universal standards.
- The actual skill mechanism is not currently exposed in this runtime, so the
  portable layer should live in plain repo files: `CLAUDE.md`, `lore/`, and the
  TeX ledgers.
- Treat any other runner's compatibility with `CLAUDE.md`, slash commands, or
  skills as unknown until confirmed by its own docs.

## Recommended operating rhythm

1. Start from one queue item in `paper/unverified.tex`.
2. Launch one research agent and one adversarial checker.
3. Update the queue based on both reports.
4. Edit `paper/proof_of_rh.tex` only if the item is now grounded.
5. Record the session result in `lore/` when the proof state changes in a
   meaningful way.

This is the smallest workflow that still gives us provenance, skepticism, and a
clean boundary between exploration and the paper.
