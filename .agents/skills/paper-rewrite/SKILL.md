---
name: paper-rewrite
description: Full-paper compactness rewrite of <paper>/<main>.tex (or a specified scope). Tightens prose, combines redundancy, and removes unnecessary qualifiers while RIGOROUSLY preserving every convention â€” macros, labels, cite keys, theorem statements, notation, mathematical content. Agent-per-section parallel dispatch with heavy compile-check gating.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Paper Rewrite

Compactness pass on `<paper>/<main>.tex` (or a scope). Rewriters
(`Codex agent role: rewriter`) are edit-capable for their own agent dir
only; assembly into the paper is gated behind integrity checks. For Codex, use the inherited model by default; only override the model if the user explicitly asks or the task clearly requires it. Original Claude note: use the original Claude research model for every rewriter, always.

`$ARGUMENTS`: empty â†’ full paper; `Â§<N>` or `Â§<N>.<M>` â†’ that section;
`--line-range <from>-<to>` â†’ specific range; `--target-ratio <N>` â†’
compaction target (default 15%); `--no-agents` â†’ coordinator does it
directly (scopes < 500 lines); `--preserve-extra "<list>"` â†’ additional
locked identifiers.

## Non-negotiable invariants

Any violation aborts assembly.

1. **Frozen macro namespace** â€” no new / renamed / removed
   `\newcommand`s. Body must reuse the input's macros.
2. **Every `\label{...}`** preserved. No renames, deletions, or new
   labels.
3. **Every `\cite{...}` / `\ref{...}` / `\eqref{...}`** remains
   resolvable. No renames.
4. **Theorem / Proposition / Lemma / Corollary / Remark STATEMENTS**
   byte-identical (whitespace-only changes allowed). Tighten surrounding
   prose and proof text only.
5. **Mathematical content** (equations, constants, identities) untouched.
   Math mode copied verbatim.
6. **Notation** â€” every symbol keeps its meaning. No `u â†’ x`, no
   `\phi â†’ \varphi`, no `\mathbb â†” \mathcal` swaps.
7. **Section / subsection order and titles** preserved; no merges or
   splits.
8. **`rem:wip-*` labels and their claim-state** preserved â€” a
   `[conditional]` remark must not become `[proved]`.
9. **Scope disclaimers** (`from [scope] alone`, `conditional on [X]`)
   preserved. Compactness does not override honesty.
10. **Bibliography** untouched (use `paper-biblio` instead).
11. **`--preserve-extra` list**, if supplied.

Fair game: AI tells, redundant transitions, repeated setups, overlapping
remarks, unnecessary hedging, long prose redundant with an equation,
stale cross-references.

## Preamble

Create `<paper>/teams/<ts>-other-rewrite-<slug>/`. Capture invariants into
`notes/`: macros, theorem envs, labels, cite keys, cross-refs, baseline
line count (grep + `wc -l`). Baseline compile-check must be clean before
starting. Partition scope (full = 14 top-level sections + `LaTeX conventions`' six
subsections â†’ up to 19 rewriters; scoped = by subsection,
â‰¤2000 lines per rewriter).

## Dispatch (unless `--no-agents`)

`Codex subagent delegation when explicitly requested team_name: "paper-rewrite-<ts>"`. Spawn one
`rewriter-<slug>` (`Codex agent role: rewriter`, the inherited Codex model by default) per partition. Standard
briefing plus: the full invariant list (verbatim â€” not suggestions),
`notes/frozen-macros.txt`, the input region, the labels/cites/refs
present in it, the target compaction ratio, and the output contract â€”
the replacement block at `agents/<slug>/rewrite.tex`, a 9-field report
with a "Compaction notes" field, and do NOT edit `<main>.tex` directly
(assembly is the coordinator's).

Non-goals: no proof restructuring, no removed conditionals, no
reordering within a subsection, no `rem:wip-*` promotion, no new
labels / macros / cite keys.

With `--no-agents`: coordinator applies the same invariants directly.

## Integrity checks (per rewriter)

Diff every output against its input notes:

- Label set identical â†’ else hard failure.
- Cite-key set identical â†’ else hard failure.
- Every cross-reference still resolves.
- Every macro used in input still used in output (or a semantic
  equivalent using existing macros).
- Every theorem-env body byte-identical to input.
- Isolated compile-check (output + paper preamble) passes.

Any failure â†’ do NOT assemble that rewriter's output.

## Assembly

Replace each input region with the corresponding
`agents/<slug>/rewrite.tex`. Run the full compile-check. Diff the
paper's label set and cite-key set against baselines; both diffs must
be empty. Any failure â†’ revert. Record the achieved line-count
reduction.

## Commit

Atomic: only this rewrite in the commit. Subject
`paper: compactness rewrite <scope> (-<N>%)`. Body: scope, reduction,
rewriters, team dir, any `--preserve-extra` tokens confirmed.

Follow up with `paper-harden` (at minimum rigor + consistency) on the
rewritten scope. Drift surfaced â†’ `paper-demote`.

## Don't

Rewrite during an active research cycle. Skip integrity checks. Combine
with a content edit. Rename or reorder anything.


