---
name: paper-demote
description: Structured reverse-promotion. Remove or weaken a claim currently in <paper>/<main>.tex, reinstate a UV-NNN entry in <team-dir>/uv.md, and optionally capture a negative finding â€” all in one atomic commit. Use when a promoted claim turns out to be wrong or weaker than stated.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Demote

Atomic reverse-promotion: paper edit + UV reinstatement + optional
negative-capture, all in one commit.

`$ARGUMENTS`:
- `<label-or-region>` â€” what to demote (label, line range, or
  description the coordinator resolves).
- `--weaken` â†’ keep a scoped weaker form in the paper; the original
  strong statement becomes the new UV entry.
- `--reason "<text>"` â†’ appears in the commit body and the new UV's
  "Why unverified."

## Protocol

**Before anything**: if an active team is running on the affected claim,
broadcast the correction first with one `send_input` per active agent BEFORE editing.
Delayed corrections are the high-cost failure.

Edit `<paper>/<main>.tex`. With `--weaken`, replace the stronger statement
with the scoped form and keep the label if still apt; otherwise delete
the claim + proof and fix every `\ref{<deleted-label>}` site. Add a new
`rem:wip-demoted-<slug>` remark pointing at the new UV entry, e.g.:

```latex
\begin{remark}\label{rem:wip-demoted-foo}
\emph{Work in progress.} The previous unconditional statement of
Theorem~\thetheorem has been demoted to conditional; see UV-010 in
\texttt{<team-dir>/uv.md}.
\end{remark}
```

Add the new UV-NNN (next available, monotonic) to `<team-dir>/uv.md` with
the standard schema, including `Depends on:`. Put the original stronger
claim in the `Claim` field so future work can retry; `Why unverified`
records the `--reason` plus any adversarial finding that triggered the
demote.

If the demote produced a reusable "don't-retry-this-route" lesson, call
`research-capture negative` with a `Do-not-retry:` line in the same
commit.

Compile-check runs via the pre-commit hook.

## Commit

Single atomic commit. Stage `<paper>/<main>.tex`, `<team-dir>/uv.md`, and
(if applicable) `findings.md` by name. Subject
`demote <label-or-UV>: <reason>`. Body: what was removed/weakened, the
new UV-NNN, and any team dir whose adversarial report triggered it.

If teams are still active, `send_input` each a short correction notice
so they don't build on the demoted claim.

## Don't

Demote without a trigger. Reuse an old UV-NNN ID. Split the edit +
reinstatement + capture across commits. Bypass the compile-check.


