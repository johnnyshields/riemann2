## Writing discipline

Applies to coordinator paper edits and every agent brief.

- **Facts directly.** No AI tells ("it is worth noting," "interestingly," "we leverage / utilize / employ," "to the best of our knowledge").
- **No overclaim.** Computational ≠ proved. "For tested configurations" ≠ "for all." Non-effective bound ≠ effective.
- **Three bins** on every audit / synthesis / status: `proved` / `conditional on [X]` / `missing`. Never blur.
- **Gap reduction over closure.** A gap is a precise missing sub-statement, not "further analysis needed." Vague gaps become UVs.
- **Scoped negation.** "Ruled out" carries "from [scope] alone."
- **Pre-tag merged sources** `[confirmed]` / `[conditional on X]` / `[candidate]`. Only `[confirmed]` reaches the paper.
- **Honest verdict** closes audits.
- **When in doubt, quarantine.** UV first, promote later.
- **Compute before asserting.** Computational claims (bound, identity, inequality, convergence) get a 10-line sympy/numpy/mpmath check. Write the script to a file first, then run it — amend and rerun. No stdin, no `-c`, no heredoc throwaways. Cite path + relevant output in the report.
- **Simplicity.** At equal proof value, prefer fewer definitions, assumptions, dependencies, scripts, paper edits.
- **Fixed-harness.** Judge each route against the same target, paper state, `findings.md`, `uv.md`, and verification standard it was briefed with.
- **Adversarial by default.** Don't agree to make the user feel good. Challenge premises, name the load-bearing assumption, and say so when a request rests on a wrong frame. Strongest deference owed to evidence, not to the prompt.
- **Double-check load-bearing claims.** Re-derive a key step, re-run a script, or re-grep the source before merging. If a claim hinges on one identity or one number, verify it twice from independent angles. Cheap to recheck; expensive to ship a quietly wrong row.
- **Surface disagreement.** If you think a teammate or the coordinator is wrong, say so plainly with the specific objection. "Looks fine" without reasons is worse than silence.

### Idioms that license candor

Paste verbatim where they apply:

- "Separate three things: proved / conditional / missing."
- "What is the cleanest target here?"
- "Give me the honest verdict."
- "If full closure is too hard, reduce to the smallest list of concrete unresolved sub-statements."
- "Qualify any impossibility claim with 'from [scope] alone.'"
- "Label each claim with a confidence tag before merging."
- "`unsupported`, `blocked`, `no progress` are acceptable returns."

## LaTeX

- Math delimiters everywhere are `\(...\)` / `\[...\]`, including `.md`, commit messages, lore. Never `$...$`; preserve on extraction from chats.
- Frozen macro namespace in the preamble (\(\sim 30\) `\newcommand`s). Don't redefine or invent macros; quarantine any need for one as a UV.
- `rem:wip-*` labels mark in-paper WIP; each should have a matching UV-NNN in the current team dir's `uv.md`.

## Migration workflow (rh paper)

Active proof file: `rh/rh_rebuild.tex`. Source archive: `rh/proof_of_rh.tex` (read-only quarry). Migration runs section by section.

### Order — strict dependency, bottom-up, easy-first within tier

No section migrates before its prerequisites. Within tiers of equal depth, do the section that is easiest to verify first, to validate the workflow before the hard ones. Committed order:

1. **§3 Jet-limit local blocks** first (\(J(T)\), \(N_{12}\) are computable; verifies the workflow).
2. **§2 Local kernel and jet normalization** (chart-existence work + kernel definition).
3. **§9 \(N\)-point odd-moment cancellation** (clean parity argument; do early because it's verifiable in 10 lines).
4. **§4 Finite-scale local blocks and whitening** (locks down \(\widehat\Om_\z(s;m)\) and the whitening loss bound).
5. **§5 Toy anomaly and transverse obstruction** (\(\Ph_\toy\) is explicit elementary functions of \((2\beta-1)\)).
6. **§6 Transverse projection** (the \(\mathcal V_\val\) choice is the most sensitive structural decision; freeze in writing once chosen).
7. **§8.1 Two-point comparison** (exponent arithmetic once §3, §5, §6 are migrated).
8. **§10 Aggregation, §11 RH** (bookkeeping).
9. **§7.1, §7.2 (zeta-suppression hypotheses)** are *research targets*, not migration targets — v1 has attempts, not closure. Treat after §1–§6 and §8.1 are solid.
10. **§12 Hardy reservoir** — migrate only if §7.1 or §7.2 standalone fails. Don't migrate prematurely.
11. **§8.2 Four-point comparison** — wait until §8.1 fully closes; some four-point machinery may not be needed if two-point closes.

### Per-section workflow (mandatory, before commit)

1. **Restate, don't paste.** Every imported result is rewritten in the rebuild's conventions (\(T\pm h\) pair, orthonormal \(P_h\) of \eqref{eq:point-to-jet-transform}, `rem:wip-*` labels). Pasting v1 prose imports v1's silent normalization bugs.
2. **Compute every formula.** A sympy/numpy script under `scripts/wip/<section>.py` re-derives every matrix entry, parity identity, or Taylor coefficient symbolically. Cite the script path in the proof or in a verification remark. (Hard rule from `Writing discipline`.)
3. **Adversarial review.** Spawn a researcher in `verify` mode against the migrated block. Their job is to find a sign error, an off-by-2 factor, or a missing case. The \(P_h\) bug is the canonical example — it lived in v1 for months because nobody adversarially checked the conjugation.
4. **Demote `wip` only when fully closed.** Remove the `wip` for the section's main statement only when the proof is filled in. If only part is closed, leave a *narrower* `wip` flagging the residual gap. Never blanket-promote.
5. **Commit per section.** Subject names the section, lists the closed `rem:wip-*` labels.

### Two strategic principles

- **Don't conflate migration with research.** Migration targets are sections where v1 has the content and the work is restate-and-verify. Research targets are sections where v1 has *attempts*, not closure. Treating them the same way is what got v1 to 60k lines.
- **Stop migrating when you hit a real gap.** If section \(k\) cannot be closed by migration (the v1 prose is genuinely non-rigorous, not just messy), don't paper over it — leave a sharper `wip` describing the remaining gap and proceed to section \(k+1\). An honest hole beats a half-migrated proof.

### Per-section status block

Every section in `rh_rebuild.tex` carries six status indicators under its heading, one per axis, each as its own macro so axes can be edited independently:

```latex
\statuspaper{<value>}\quad
\statusmig{<value>}\quad
\statusreferee{<value>}\quad
\statussympy[<sympy script path>]{<value>}\quad
\statussim[<simulation script path>]{<value>}\quad
\statuslean[<lean source path>]{<value>}
\par\medskip
```

The three computational axes (`\statussympy`, `\statussim`, `\statuslean`) take an *optional* path argument in square brackets that points to the verification artefact and is rendered next to the status pill (e.g.\ `sympy: [verified] rh/sympy/sec-jet-limit-local-blocks.py`).  Omit the optional argument when there is no artefact yet (e.g.\ `\statussympy{not-started}`, `\statussim{n/a}`).

Status values:

- **paper** \(\in\) `LIVE | FINITE AUDIT | ARCHIVED | SUPERSEDED | NO-GO | DIAGNOSTIC`.
- **v1** (migration from `proof_of_rh.tex`) \(\in\) `not-started | in-progress | partial | migrated | n/a` (rebuild-original sections).
- **referee** \(\in\) `not-started | in-progress | passed | failed`.
- **sympy** (symbolic/formula verification: sympy/numpy re-derivation of matrix entries, identities, Taylor coefficients) \(\in\) `n/a | not-started | partial | verified`.
- **sim** (numerical simulation: empirical behavior at specific heights, sweeps, Monte Carlo --- *not* formula verification) \(\in\) `n/a | not-started | partial | verified`.
- **lean** (Lean formalization) \(\in\) `n/a | not-started | in-progress | formalized`.

Each axis is updated in the same commit as the status change. The six together are the one-glance health of each section.

## Paper drafting (`rh_rebuild.tex`)

Applies to every edit of `rh/rh_rebuild.tex`, including section migrations, refinements, and structural reorganizations.

**Tone.** Annals register: direct, terse, theorem-proof-remark. Let the proofs and lemma statements carry the content; remarks only when they genuinely clarify (a convention, a numeric value, a forward reference, an unconditional aside).

**Avoid:**

- Editorial framing ("we therefore", "we never use \(\zeta\) again", "the algebra is unconditional and reduces to...", "load-bearing", "isolates", "structural separation").
- Section-opening proof outlines ("This section computes...", "The strategy is...").  Section titles are descriptive enough.
- ELI5 motivation, narrative bridges, and "the reader should note" phrasing.
- Meta-commentary about authorship, agent names, referee reports, or `proof_of_rh.tex` history.  Provenance, if strictly required, goes outside the paper (lore, commit message, or a separate provenance block under `lore/`); avoid adding it to the paper at all.
- Per-lemma "Symbolic verification: \texttt{...}" remarks.  Put script paths in the section-header status macros (`\statussympy[<path>]{...}`, etc.) instead.
- "We" pronouns where the passive or a definite construction works.

**Wips and conditionals.** The goal is a *full unconditional proof*.  Every `\begin{wip}` in `rh_rebuild.tex` is an explicit liability, and every `\begin{hypothesis}` carried into a closure step makes the whole closure conditional.  When a gap surfaces:

1. Narrow it to the smallest precise sub-statement.
2. Try to discharge it from a previously migrated section (often the asymptotic estimates of \S\ref{sec:local-kernel-and-jet-normalization} are enough).
3. If neither works, surface to the user *before* adding new `wip` language or new `Hypothesis` blocks.  Don't quietly inflate the conditional surface of the paper.

**Verification artefacts.** Every migration that adds a lemma or theorem ships with verification artefacts under `rh/`:

- a sympy script `rh/sympy/<section-label>.py` covering symbolic identities and the algebraic content;
- where applicable, a simulation script `rh/simulation/<section-label>.py` covering numerical sanity at concrete heights;
- where applicable, a Lean source `rh/lean/<section-label>.lean` covering the formalization.

Wire each to the section-header status macros: `\statussympy[<path>]{verified}`, `\statussim[<path>]{partial}`, `\statuslean[<path>]{...}`.  The artefact is the verification record; the paper does not need a separate script-reference remark.
