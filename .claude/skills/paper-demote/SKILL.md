---
name: paper-demote
description: Structured reverse-promotion. Remove or weaken a claim currently in paper/proof_of_rh.tex, reinstate a UV-NNN entry in paper/unverified.tex, and optionally capture a negative finding — all in one atomic commit. Use when a promoted claim turns out to be wrong or weaker than stated.
---

# Paper Demote

Atomic reverse-promotion: paper edit + UV reinstatement + optional
negative-capture, all in one commit.

`$ARGUMENTS`:
- `<label-or-region>` — what to demote (label, line range, or
  description the coordinator resolves).
- `--weaken` → keep a scoped weaker form in the paper; the original
  strong statement becomes the new UV entry.
- `--reason "<text>"` → appears in the commit body and the new UV's
  "Why unverified."

## Protocol

**Before anything**: if an active team is running on the affected claim,
broadcast the correction first (`SendMessage to: "*"`) BEFORE editing.
Delayed corrections are the high-cost failure.

Edit `proof_of_rh.tex`. With `--weaken`, replace the stronger statement
with the scoped form and keep the label if still apt; otherwise delete
the claim + proof and fix every `\ref{<deleted-label>}` site. Add a new
`rem:wip-demoted-<slug>` remark pointing at the new UV entry, e.g.:

```latex
\begin{remark}\label{rem:wip-demoted-foo}
\emph{Work in progress.} The previous unconditional statement of
Theorem~\thetheorem has been demoted to conditional; see UV-010 in
\texttt{unverified.tex}.
\end{remark}
```

Add the new UV-NNN (next available, monotonic) to `unverified.tex` with
the standard schema, including `Depends on:`. Put the original stronger
claim in the `Claim` field so future work can retry; `Why unverified`
records the `--reason` plus any adversarial finding that triggered the
demote.

If the demote produced a reusable "don't-retry-this-route" lesson, call
`research-capture negative` with a `Do-not-retry:` line in the same
commit.

Compile-check runs via the pre-commit hook.

## Commit

Single atomic commit. Stage `proof_of_rh.tex`, `unverified.tex`, and
(if applicable) `findings.md` by name. Subject
`demote <label-or-UV>: <reason>`. Body: what was removed/weakened, the
new UV-NNN, and any task dir whose adversarial report triggered it.

If teams are still active, `SendMessage` each a short correction notice
so they don't build on the demoted claim.

## Don't

Demote without a trigger. Reuse an old UV-NNN ID. Split the edit +
reinstatement + capture across commits. Bypass the compile-check.
