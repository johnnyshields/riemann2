# RH paper clean rebuild plan

**Date:** 2026-05-01
**Trigger:** `proof_of_rh.tex` reached 60k lines with structural drift,
unresolved Hardy source-transfer gap, and accumulated archive material
(no-go ledgers, framing-map sections, route history).  Decision: rebuild
from the jet-Gram side into a fresh file, treat `proof_of_rh.tex` as a
read-only quarry, and discipline the new draft to a story-first format.

## New file

`rh/rh_rebuild.tex` --- the active draft going forward.  Compiles cleanly.

## Conventions

- **Macro namespace:** identical to `proof_of_rh.tex` (no churn).  One new
  theorem environment, `wip` (counter shared with `theorem`), titled
  ``Gap.''  Removed at journal time.
- **Status discipline:** binary.  A statement is proved iff it has no
  attached `\begin{wip}...\end{wip}` block.  No fbox-tag zoo, no
  `Core/Open/Optional/Conditional/Verified/Imported` matrix.
- **Gap labels:** every gap carries a `rem:wip-<semantic-name>` label; the
  semantic name matches the theorem/lemma it accompanies (so `lem:foo` ↔
  `rem:wip-foo`).  No numeric `UV-NNN` layer, no team-dir `uv.md`, no
  external bookkeeping.  All gap context lives inside the remark body.
- **Story prose first:** every section opens with 1--2 paragraphs of plain
  prose explaining what is happening and why, *before* any definition or
  theorem.
- **microtype:** loaded with `expansion=false` because auto font expansion
  fails on the default Computer Modern setup in this TeX install
  (page-2 fatal during shipout).  Cosmetic only.

## Spine

| § | Title | Role |
|---|---|---|
| 1 | The argument in one paragraph | Whole proof in two paragraphs + master conditional theorem. |
| 2 | The local microscope: phase kernels and jet coordinates | Local chart, phase \(\Ph\), kernel \(K_\Ph\), point-to-jet transform \(P_h\). |
| 3 | Same-point and cross-block jet-Gram limits | The matrices \(J(T)\), \(N_{12}\); same-point Gram positivity. |
| 4 | Finite-scale packet blocks and whitening | \(G_{m,\pm}(s)\), \(N_m(s)\), whitened block \(\widehat\Om_\z(s;m)\); whitening loss bound. |
| 5 | What the toy off-line model sees | Toy phase, transverse projection \(\Pi_\trans\) (frozen here, never re-chosen), toy visibility lower bound. |
| 6 | What actual \(\zeta\) does instead | Actual-zeta transverse suppression upper bound (the load-bearing gap). |
| 7 | Two zeros at once: pairwise rigidity | Two-point closure. |
| 8 | Four zeros in a symmetric quartet: stronger rigidity | Four-point closure. |
| 9 | Odd-moment cancellation across \(N\) points | Symmetry-driven remainder kill. |
| 10 | From local obstruction to a zero-free strip | Aggregation. |
| 11 | The Riemann Hypothesis | Strip + low-height verification. |
| 12 | (Optional) Extra source energy from \(\zeta\): the Hardy reservoir | Self-contained interface; \(\int |q''_\can|^2\) lower bound + transfer to §6 suppression.  Forward-referenced from §7/§8 only. |
| App. A | Archive map | Section-by-section pointers into `proof_of_rh.tex` for prose mining. |

## Hardy positioning (key user constraint)

Hardy is a *sibling* input, not a chain link.  It sits at the end of the
file and is referenced only by the two-point and four-point closure
remarks, and only if their standalone forms fall short.  This leaves open
the possibility that Hardy is unnecessary --- the structure does not
silently consume Hardy energy through notation like \(q''_\can\).

## Migration discipline

For each section, prose and computations from `proof_of_rh.tex` are
candidates for migration but must be restated in the rebuild's
conventions before insertion.  The archive map in Appendix A names the v1
sections relevant to each new section.  Sections of v1 that are *not*
migrated:

- ``Endgame architecture and remaining propagation problem''
- ``Downstream local closure package''
- ``Unified finite-survival architecture''
- ``Current proof state after the local package audits''
- ``How the older framing maps to the new framing''
- ``No-go and audit ledger''

These are route history and process bookkeeping, not active proof
material.

## Current state

`rh_rebuild.tex` is a skeleton with:

- Full preamble and macro namespace.
- All 12 sections + appendix written, with story prose openings, formal
  statements (definitions/lemmas/theorems/hypotheses), and 17 `wip`
  remarks marking the gaps.
- Compiles cleanly to 8 pages.

No proofs are filled in.  The next migration step (per user direction
when ready) is the same-point jet-Gram limit, Lemma 3.1: import the v1
Taylor expansion into the rebuild's \(T\pm h\) convention and verify
the \(1/12\) coefficient and \(2q(T)^3\) cubic correction independently.
