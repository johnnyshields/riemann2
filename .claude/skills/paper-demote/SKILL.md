---
name: paper-demote
description: Structured reverse-promotion. Remove or weaken a claim currently in paper/proof_of_rh.tex, reinstate a UV-NNN entry in paper/unverified.tex, and optionally capture a negative finding — all in one atomic commit. Use when a promoted claim turns out to be wrong or weaker than stated.
---

# Paper Demote

Reverse-promotion with full audit trail. See `CLAUDE.md` §6 (claim
lifecycle — demote rules), §9 (adversarial before promote), §9a
(broadcast-correction duty), §10 (provenance).

## Arguments

`$ARGUMENTS`:

- `<label-or-region>` — what to demote. Either a theorem/lemma label
  (`\label{thm:foo}`), a line range in `proof_of_rh.tex`, or a short
  description the coordinator resolves to a specific region.
- `--weaken` — reduce the claim in the paper rather than remove it
  outright; the weakened version becomes the paper's new statement,
  the original goes back as a UV entry with its stronger form.
- `--reason "<text>"` — short reason string that will appear in the
  commit subject body and the new UV's "Why unverified" field.

## Mandatory preamble

1. Read the briefing packet:
   - `paper/findings.md` (pasted by coordinator if teammates involved;
     usually this skill is synchronous and does not delegate).
   - The current state of the claim in `proof_of_rh.tex` at the named
     label or region.
   - `paper/unverified.tex` — so the new UV-NNN doesn't collide with
     existing IDs and `Depends on:` can be set correctly.
2. Decide the new UV-NNN ID (next available, e.g. UV-010 if UV-009 is
   the highest current).
3. If any active team is running a cycle that depends on the claim
   being demoted: broadcast the correction per `CLAUDE.md` §9a BEFORE
   editing. `SendMessage to: "*" ...`

## Protocol

### Step 1: Edit `paper/proof_of_rh.tex`

- **`--weaken`** — replace the stronger statement with the weaker
  (scoped) version. Preserve the `\label{}` if the weaker version still
  matches the label's semantic role; otherwise rename carefully (update
  all `\ref{}` sites too).
- **no flag** (full remove) — delete the claim and its proof block.
  Check cross-references: every `\ref{<deleted-label>}` must be fixed
  or explicitly redirected. If the label name is reused semantically
  elsewhere, update the references to the new site; if not, remove the
  references and find a substitute.

Add a new `rem:wip-*` label at the site of the weakening / removal so
the new UV entry can point to it. Example:

```latex
\begin{remark}\label{rem:wip-demoted-foo}
\emph{Work in progress.} The previous unconditional statement of
Theorem~\thetheorem has been demoted to conditional; see UV-010 in
\texttt{unverified.tex}.
\end{remark}
```

### Step 2: Add a new UV-NNN to `paper/unverified.tex`

Use the six-field schema per `CLAUDE.md` §6:

- **Title**: one-line descriptor of the demoted claim.
- **Status**: usually `open` or `heuristic` depending on what we know.
- **Source in paper**: `rem:wip-demoted-<slug>` and line number after
  the demote edit.
- **Claim**: the statement in its original stronger form (we're
  parking it for future work).
- **Why unverified**: the `--reason` text plus any adversarial finding
  that triggered the demote.
- **Needed for promotion**: the specific gap the original claim was
  missing (often: closure of a sub-lemma, a hypothesis that was
  implicitly assumed, or a counterexample that ruled out the stronger
  form).
- **Depends on**: list of other UV-NNN IDs this item depends on, or
  `None`.

### Step 3: Optional — capture negative finding

If the demote produced a reusable "don't-retry-this-route" lesson
(e.g., a whole approach is ruled out), call `research-capture negative`
with a `Do-not-retry:` line.

### Step 4: Compile-check

Per `CLAUDE.md` §11a (and enforced by the pre-commit hook): run
pdflatex on the edited paper, fix any new undefined refs introduced by
the demote.

### Step 5: Single atomic commit

Stage `paper/proof_of_rh.tex`, `paper/unverified.tex`, and (if applicable)
`paper/findings.md` by name. Subject:

```
demote <label-or-UV>: <reason>
```

Body: describe what was removed/weakened, the new UV-NNN, and why.
Cite any task dir that surfaced the correction (e.g., the `verify`
task dir whose adversarial report prompted the demote).

### Step 6: Broadcast if any team is still active

If a cycle is running and received briefing material that referenced
the now-demoted claim, `SendMessage` each teammate with a short
correction notice so they don't build on the flawed assumption.

## Anti-patterns

- Do NOT demote without an explicit reason — every demote must have a
  trigger (adversarial finding, user directive, counterexample, etc.).
- Do NOT reuse an old UV-NNN ID for a new demote — IDs are monotonic.
- Do NOT split the demote across multiple commits — the paper edit,
  the UV reinstatement, and (if applicable) the negative-finding
  capture go together so the audit trail is atomic.
- Do NOT bypass the pre-commit compile-check.
