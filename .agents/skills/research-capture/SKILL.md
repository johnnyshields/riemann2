---
name: research-capture
description: Synchronous coordinator append of a single structural, negative, goodie, or gap entry to a team findings.md, with provenance, then commit.
---

# Research Capture

Synchronous append of one entry to `<team-dir>/findings.md`. No delegation. Provenance mandatory. Use only for durable briefable knowledge — route history → `attempts.md`, live missing sub-statements → `uv.md`, no-action rationale → `collation.md`.

`$ARGUMENTS` format: `<section> <one-line summary>`, section in `structural | negative | goodie | gap`. Body inline or in a follow-up message.

Examples:
- `/research-capture negative tangent-separator fails at W=0 inflections`
- `/research-capture goodie reusable quintic normal form at Section 12.3.2`
- `/research-capture gap mixed 4-point factorization still open`

## Protocol

Read current `findings.md`. If the same claim already exists, refine its `Provenance:` instead of duplicating. Append under the right `##` heading with `Provenance:` always, plus `Do-not-retry:` for Negative entries.

If the file exceeds 200 lines after the append, run `findings-prune`.

Stage `findings.md` by name and commit `findings: capture <section> - <summary>`. Cite the team dir if applicable.

## Don't

No entries without provenance. No Negative without `Do-not-retry:`. No route-history rows or duplicate UV text. No status annotations — presence is the signal.
