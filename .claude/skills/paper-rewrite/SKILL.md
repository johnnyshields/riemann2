---
name: paper-rewrite
description: Full-paper compactness rewrite of paper/proof_of_rh.tex (or a specified scope). Tightens prose, combines redundancy, and removes unnecessary qualifiers while RIGOROUSLY preserving every convention — macros, labels, cite keys, theorem statements, notation, mathematical content. Agent-per-section parallel dispatch with heavy compile-check gating.
---

# Paper Rewrite

Compactness pass on `paper/proof_of_rh.tex` that tightens prose while
preserving every invariant. Rewriters are edit-capable for this skill
(explicit exception); the coordinator gates assembly behind multiple
compile- and integrity-checks. See `CLAUDE.md` §3, §3a, §11a.

## Arguments

`$ARGUMENTS`:

- **empty** — full-paper rewrite (all 14 sections).
- `§<N>` or `§<N>.<M>` — rewrite that section only.
- `--line-range <from>-<to>` — rewrite a specific line range.
- `--target-ratio <N>` — aim to reduce length by ~N % (default 15 %).
- `--no-agents` — single-coordinator rewrite (for scopes \(< 500\) lines).
- `--preserve-extra "<list>"` — additional identifiers the user wants
  locked (e.g. `--preserve-extra "\\Uhl, \\Gap, phi, psi"`).

## Non-negotiable invariants

The coordinator and every rewriter MUST preserve the following. Any
violation is a hard failure; the assembly is aborted.

1. **Frozen macro namespace.** Every `\newcommand` / `\renewcommand` in
   the preamble is locked. Names, argument arities, and expansions are
   unchanged. Do not introduce new macros. Do not remove existing
   macros. Body text must use the existing macros wherever the input
   did.
2. **Labels.** Every `\label{...}` currently in the paper must appear
   in the output. No renames. No deletions. New labels are NOT
   introduced by a rewrite.
3. **Cite keys.** Every `\cite{key}` and `\eqref{...}` / `\ref{...}`
   target must remain resolvable. Citation keys are not renamed.
4. **Theorem / Proposition / Lemma / Corollary / Remark STATEMENTS.**
   The body of every `\begin{theorem} ... \end{theorem}` (and the other
   numbered environments) is preserved **verbatim**. Only surrounding
   prose and proof text may be tightened.
5. **Mathematical content.** No numerical constants, equations, or
   identities are altered. Math-mode blocks are copied verbatim; only
   LaTeX formatting (whitespace, single vs. display) may change, and
   only when it doesn't alter meaning.
6. **Notation and variable names.** Every symbol used in input must
   appear in the output with identical meaning. No renames (no
   `u \to x`, no `\phi \to \varphi`). Greek-Latin swaps and font-style
   swaps (`\mathbb` ↔ `\mathcal`) are forbidden.
7. **Section and subsection order and titles.** Preserved as-is.
   Sections are not merged or split.
8. **`rem:wip-*` labels and their surrounding remarks.** These anchor
   UV-NNN entries in `unverified.tex` (§6, `uv-sync`). Preserve both
   the label AND the claim state — a `[conditional]` remark must not
   become `[proved]`.
9. **Scope disclaimers.** Every "from [scope] alone" / "conditional on
   [X]" / "only for [Y]" clause stays. Compactness does not override
   honesty (`CLAUDE.md` §3a).
10. **Bibliography.** Not touched by this skill. Use `paper-biblio` for
    bib cleanup.
11. **The user's `--preserve-extra` list**, if supplied.

Anything not in the invariant list is fair game for tightening: AI
tells, redundant transitions, repeated setups, overlapping remarks,
unnecessary hedging, long-form prose that says the same thing as an
equation, and cross-references to things said two paragraphs earlier.

## Mandatory preamble (before dispatch)

1. Create task dir:
   `tasks/<ts>-other-rewrite-<slug>/` with `reports/`, `scripts/`,
   `notes/`. `<slug>` describes the scope (e.g. `§12.3`, `full`,
   `post-referee`). Announce it.

2. **Extract invariants** and save to `notes/`:

   ```sh
   # All macros defined in preamble
   grep -n '^\\\(new\|renew\)command' paper/proof_of_rh.tex > tasks/<dir>/notes/frozen-macros.txt

   # All theorem environments
   grep -n '^\\newtheorem' paper/proof_of_rh.tex > tasks/<dir>/notes/frozen-theorems.txt

   # All labels (sorted unique)
   grep -oE '\\label\{[^}]+\}' paper/proof_of_rh.tex | sort -u > tasks/<dir>/notes/labels-before.txt

   # All cite keys referenced in body
   grep -oE '\\cite\{[^}]+\}' paper/proof_of_rh.tex | sort -u > tasks/<dir>/notes/citekeys-before.txt

   # All cross-references
   grep -oE '\\(ref|eqref|Cref|autoref)\{[^}]+\}' paper/proof_of_rh.tex | sort -u > tasks/<dir>/notes/refs-before.txt

   # Baseline line count
   wc -l paper/proof_of_rh.tex > tasks/<dir>/notes/lines-before.txt
   ```

3. **Baseline compile-check** (`CLAUDE.md` §11a). Must be clean before
   proceeding; if not, surface to the user first — do not start a
   rewrite on top of a broken tree.

4. **Partition scope.** For a full rewrite, one rewriter per top-level
   section (14 sections). §12 (~20k lines) is re-partitioned into its
   6 subsections → 6 rewriters. Total: up to 19 rewriters. For a
   specified scope, partition by subsection; aim for rewrites of
   \(\le 2000\) lines each.

5. Read `paper/findings.md` in full (for the coordinator; pasted into
   every rewriter briefing per `CLAUDE.md` §7).

## Dispatch (unless `--no-agents`)

`TeamCreate team_name: "paper-rewrite-<ts>"`. Spawn one
`rewriter-<section-slug>` per partition unit, in parallel.

Each rewriter's briefing MUST include:

- The task dir path and `notes/` location.
- Full `paper/findings.md` (pasted).
- The **full invariant list** above (copy verbatim — these are not
  suggestions).
- `notes/frozen-macros.txt` contents.
- The exact input text for their assigned region (line range).
- All `\label{}`, `\cite{}`, and cross-reference tokens appearing in
  their region — the rewriter must reproduce each in the output.
- The target compactness ratio (default 15 %, override per
  `--target-ratio`).
- The writing-discipline reminder (`CLAUDE.md` §3a) — especially
  "state facts directly; no overclaim; no hedge; honest scope
  disclaimers welcome."
- The **output contract**:
  - Deposit the rewritten region at
    `tasks/<dir>/scripts/section-<slug>.tex` (the complete replacement
    block, nothing more).
  - Deposit a 7-field report at
    `tasks/<dir>/reports/rewriter-<slug>.md` with a "Compaction notes"
    field listing high-level changes (e.g. "merged Remarks 3.2 and
    3.4; removed 5 redundant qualifiers").
  - Do NOT edit `paper/proof_of_rh.tex` directly. Assembly is the
    coordinator's job after all invariants are verified.
- Explicit non-goals:
  - Do not restructure proofs.
  - Do not remove conditional qualifiers.
  - Do not change the order of claims within a subsection.
  - Do not promote any `rem:wip-*` remark to an unconditional statement.
  - Do not introduce new labels, macros, or cite keys.

With `--no-agents`, the coordinator does the rewrite directly,
following the same invariant list.

## Self-deposit audit

Before any assembly:

```sh
ls tasks/<dir>/scripts/    # expect one section-*.tex per partition
ls tasks/<dir>/reports/    # expect one rewriter-*.md per partition
```

Missing outputs → chase via `SendMessage` or document at
`notes/_missing-deposit.md`. Do NOT assemble a partial rewrite.

## Per-rewriter integrity check

For each `scripts/section-<slug>.tex` produced:

1. **Label preservation.** Every label listed in the rewriter's input
   must appear in their output. Diff:

   ```sh
   grep -oE '\\label\{[^}]+\}' scripts/section-<slug>.tex | sort -u > notes/labels-<slug>-after.txt
   comm -23 notes/labels-<slug>-before.txt notes/labels-<slug>-after.txt
   ```

   Any missing label is a **hard failure** for that rewriter. Surface
   and do NOT incorporate.

2. **Cite-key preservation.** Same treatment for `\cite{}`.

3. **Cross-reference integrity.** Every `\ref{}` / `\eqref{}` /
   `\Cref{}` must still resolve within the full paper's label set.

4. **Macro usage.** Every macro used in the input must still be used
   in the output (or the output must be semantically equivalent using
   different existing macros). Do not allow a macro to disappear
   silently.

5. **Theorem-statement preservation.** For each
   `\begin{theorem} ... \end{theorem}` (and other numbered envs) in the
   input, the corresponding block in the output must be byte-identical
   to the input up to whitespace.

6. **Isolated compile-check.** Extract the rewriter's output plus the
   paper preamble into a standalone temp file and run
   `pdflatex -interaction=nonstopmode -draftmode`. No new errors or
   undefined refs beyond what the isolated scope can resolve.

## Assembly (coordinator)

Only after every rewriter's output passes the per-rewriter integrity
check:

1. Replace each input region in `paper/proof_of_rh.tex` with the
   corresponding `scripts/section-<slug>.tex`. Use explicit line-range
   replacements; do not let one rewrite bleed into a neighbor.
2. **Full compile-check** per `CLAUDE.md` §11a. Any new error / warning
   / undefined ref / multiply-defined label → revert the assembly and
   return to per-rewriter investigation.
3. **Full label diff:**

   ```sh
   grep -oE '\\label\{[^}]+\}' paper/proof_of_rh.tex | sort -u > notes/labels-after.txt
   diff notes/labels-before.txt notes/labels-after.txt
   ```

   Must be empty. Any difference → revert.
4. **Full cite-key diff** — must be empty. Any difference → revert.
5. **Cross-reference resolution** — no new undefined refs in the
   compile log.
6. **Line-count record:**

   ```sh
   wc -l paper/proof_of_rh.tex > notes/lines-after.txt
   ```

   Record achieved compaction ratio in the commit body.

## Commit

Stage `paper/proof_of_rh.tex` and the task dir by name. Commit with
subject `paper: compactness rewrite <scope> (-<N>%)` and body listing:

- Scope covered.
- Achieved line-count reduction.
- Which rewriters contributed.
- Any invariants that were relaxed with explicit user approval
  (normally none).
- Task dir path.

If the user supplied `--preserve-extra`, list those tokens and confirm
they were preserved.

## Post-commit verification

Run `paper-harden` (or at least its `reviewer-rigor` and
`reviewer-consistency` roles) on the rewritten scope before declaring
the rewrite complete. Compactness must not introduce drift or subtle
overclaims. Drift caught here → `demote` per `CLAUDE.md` §6.

## Never

- Never rewrite during an ongoing research cycle — wait for the cycle
  to complete and commit first.
- Never skip the per-rewriter integrity checks to save time.
- Never accept an assembly that failed any invariant check, even if
  the compile-check passes.
- Never rename, renumber, or reorder across this skill.
- Never merge this into the same commit as a content edit — a
  compactness rewrite commit should contain ONLY the rewrite.
