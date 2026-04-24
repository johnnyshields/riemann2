---
name: paper-rewrite
description: Full-paper compactness rewrite of <paper>/<main>.tex (or a specified scope). Tightens prose, combines redundancy, and removes unnecessary qualifiers while RIGOROUSLY preserving every convention — macros, labels, cite keys, theorem statements, notation, mathematical content. Agent-per-section parallel dispatch with heavy compile-check gating.
---

# Paper Rewrite

Compactness pass on `<paper>/<main>.tex` (or a scope). Rewriters
(`subagent_type: rewriter`) are edit-capable for their own agent dir
only; assembly into the paper is gated behind integrity checks.

`$ARGUMENTS`: empty → full paper; `§<N>` or `§<N>.<M>` → that section;
`--line-range <from>-<to>` → specific range; `--target-ratio <N>` →
compaction target (default 15%); `--no-agents` → coordinator does it
directly (scopes < 500 lines); `--preserve-extra "<list>"` → additional
locked identifiers.

## Non-negotiable invariants

Any violation aborts assembly.

1. **Frozen macro namespace** — no new / renamed / removed
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
6. **Notation** — every symbol keeps its meaning. No `u → x`, no
   `\phi → \varphi`, no `\mathbb ↔ \mathcal` swaps.
7. **Section / subsection order and titles** preserved; no merges or
   splits.
8. **`rem:wip-*` labels and their claim-state** preserved — a
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
subsections → up to 19 rewriters; scoped = by subsection,
≤2000 lines per rewriter).

## Dispatch (unless `--no-agents`)

`TeamCreate team_name: "paper-rewrite-<ts>"`. Spawn one
`rewriter-<slug>` (`subagent_type: rewriter`) per partition. Standard
briefing plus: the full invariant list (verbatim — not suggestions),
`notes/frozen-macros.txt`, the input region, the labels/cites/refs
present in it, the target compaction ratio, and the output contract —
the replacement block at `agents/<slug>/rewrite.tex`, a 7-field report
with a "Compaction notes" field, and do NOT edit `<main>.tex` directly
(assembly is the coordinator's).

Non-goals: no proof restructuring, no removed conditionals, no
reordering within a subsection, no `rem:wip-*` promotion, no new
labels / macros / cite keys.

With `--no-agents`: coordinator applies the same invariants directly.

## Integrity checks (per rewriter)

Diff every output against its input notes:

- Label set identical → else hard failure.
- Cite-key set identical → else hard failure.
- Every cross-reference still resolves.
- Every macro used in input still used in output (or a semantic
  equivalent using existing macros).
- Every theorem-env body byte-identical to input.
- Isolated compile-check (output + paper preamble) passes.

Any failure → do NOT assemble that rewriter's output.

## Assembly

Replace each input region with the corresponding
`agents/<slug>/rewrite.tex`. Run the full compile-check. Diff the
paper's label set and cite-key set against baselines; both diffs must
be empty. Any failure → revert. Record the achieved line-count
reduction.

## Commit

Atomic: only this rewrite in the commit. Subject
`paper: compactness rewrite <scope> (-<N>%)`. Body: scope, reduction,
rewriters, team dir, any `--preserve-extra` tokens confirmed.

Follow up with `paper-harden` (at minimum rigor + consistency) on the
rewritten scope. Drift surfaced → `paper-demote`.

## Don't

Rewrite during an active research cycle. Skip integrity checks. Combine
with a content edit. Rename or reorder anything.
