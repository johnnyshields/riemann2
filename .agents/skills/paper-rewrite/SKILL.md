---
name: paper-rewrite
description: Full-paper compactness rewrite of <paper>/<main>.tex (or a specified scope). Tightens prose, combines redundancy, and removes unnecessary qualifiers while RIGOROUSLY preserving every convention â€” macros, labels, cite keys, theorem statements, notation, mathematical content. Agent-per-section parallel dispatch with heavy compile-check gating.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Rewrite

Compactness pass on `<paper>/<main>.tex` (or a scope). Rewriters
(`role prompt: rewriter`) are edit-capable for their own agent dir
only; assembly into the paper is gated behind integrity checks. Use the inherited Codex model by default.

`$ARGUMENTS`: empty -> full paper; section or line range -> scoped pass;
`--target-ratio <N>` sets compaction target (default 15%); `--no-agents`
means coordinator-only for small scopes; `--preserve-extra "<list>"` adds
locked identifiers.

## Non-negotiable invariants

Any violation aborts assembly.

1. **Frozen macro namespace**: no new / renamed / removed `\newcommand`s.
2. **Labels, cites, refs**: every `\label{...}`, `\cite{...}`, `\ref{...}`,
   and `\eqref{...}` is preserved and resolvable.
3. **Theorem / Proposition / Lemma / Corollary / Remark STATEMENTS**
   byte-identical (whitespace-only changes allowed). Tighten surrounding
   prose and proof text only.
4. **Mathematical content** (equations, constants, identities) untouched.
   Math mode copied verbatim.
5. **Notation**: every symbol keeps its meaning; no symbol-family swaps.
6. **Section / subsection order and titles** preserved; no merges or splits.
7. **`rem:wip-*` labels and their claim-state** preserved: a `[conditional]`
   remark must not become `[proved]`.
8. **Scope disclaimers** (`from [scope] alone`, `conditional on [X]`)
   preserved. Compactness does not override honesty.
9. **Bibliography** untouched (use `paper-biblio` instead).
10. **`--preserve-extra` list**, if supplied.

Fair game: AI tells, redundant transitions, repeated setups, overlapping
remarks, unnecessary hedging, long prose redundant with an equation,
stale cross-references.

## Preamble

Create `<paper>/teams/<ts>-other-rewrite-<slug>/`. Capture invariants into
`notes/`: macros, theorem envs, labels, cite keys, cross-refs, baseline
line count. Baseline compile-check must be clean before starting. Partition by
section/subsection, aiming for no more than 2000 lines per rewriter.

## Dispatch (unless `--no-agents`)

When delegated teamwork is authorized, record team name `paper-rewrite-<ts>` in `dispatch.md`. Spawn one
`rewriter-<slug>` (`role prompt: rewriter`, inherited Codex model) per partition. Standard
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


