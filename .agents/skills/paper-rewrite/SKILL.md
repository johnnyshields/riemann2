---
name: paper-rewrite
description: Compactness rewrite of a paper main TeX file or specified scope. Tightens prose and removes redundancy while preserving macros, labels, cite keys, theorem statements, notation, and mathematical content. Uses coordinator-selected parallel rewriters when useful.
---

# Paper Rewrite

Compactness pass on `<paper>/<main>.tex` or a scope. Rewriters edit only their own agent dirs; assembly into the paper is coordinator-owned and gated by integrity checks.

`$ARGUMENTS`: empty → full paper; section or line range → scoped pass; `--target-ratio <N>` sets compaction target (default 15%); `--no-agents` means coordinator-only for small scopes; `--preserve-extra "<list>"` adds locked identifiers.

## Non-negotiable Invariants

Any violation aborts assembly.

1. Frozen macro namespace: no new, renamed, or removed `\newcommand`s.
2. Labels, cites, refs: every `\label`, `\cite`, `\ref`, `\eqref` preserved and resolvable.
3. Theorem/proposition/lemma/corollary/remark statements byte-identical except whitespace.
4. Mathematical content, equations, constants, identities, math mode copied verbatim.
5. Notation keeps the same meaning; no symbol-family swaps.
6. Section order and titles preserved; no merges or splits.
7. `rem:wip-*` labels and claim state preserved; no implicit promotion.
8. Scope disclaimers and conditional language preserved.
9. Bibliography untouched; use `paper-biblio` instead.
10. `--preserve-extra` tokens preserved.

Fair game: AI tells, redundant transitions, repeated setups, overlapping remarks, unnecessary hedging, prose redundant with an equation, stale cross-references.

## Preamble

Create `<paper>/teams/<ts>-other-rewrite-<slug>/` with standard team files: copy-forward `findings.md` / `uv.md`, fresh `attempts.md`, `dispatch.md`, `collation.md`, `agents/`. Capture invariants into `notes/`: macros, theorem envs, labels, cite keys, cross-refs, baseline line count. Baseline compile-check must be clean. Partition only when parallelism is useful and scopes can be kept disjoint.

## Dispatch

Record team name `paper-rewrite-<ts>` in `dispatch.md`. Spawn the smallest useful set of `rewriter-<slug>` agents. Brief with the invariant list, `notes/frozen-macros.txt`, input region, labels/cites/refs present, target compaction ratio, exact deposit path, and the contract: replacement block at `agents/<slug>/rewrite.tex`, 9-field report with "Compaction notes", no direct `<main>.tex` edits.

Non-goals: no proof restructuring, removed conditionals, `rem:wip-*` promotion, new labels/macros/cite keys, ordering changes within scope. With `--no-agents`, the coordinator applies the same invariants directly.

## Integrity Checks

For each output, diff against its input notes: label set identical, cite-key set identical, cross-references resolvable, macros preserved, theorem-env bodies byte-identical, isolated compile-check passes. Any failure blocks assembly and is recorded in `collation.md` and `attempts.md`.

## Assembly

Replace each input region with the corresponding `agents/<slug>/rewrite.tex`. Run full compile-check. Diff paper label and cite-key sets against baselines; both diffs must be empty. Any failure is reverted and logged as `crash` or `blocked`.

## Commit

Atomic: only this rewrite. Subject `paper: compactness rewrite <scope> (-<N>%)`. Body: scope, reduction, rewriters, team dir, preserved tokens. Follow up with `paper-harden` on the rewritten scope, at least rigor and consistency.

## Don't

Rewrite during an active research cycle. Skip integrity checks. Combine with a content edit. Rename or reorder anything.
