---
name: research-capture
description: Synchronous coordinator append of a single structural / negative / goodie / gap entry to <team-dir>/findings.md, with provenance, then commit.
---

# Research Capture

Synchronous append of one entry to `<team-dir>/findings.md`. No delegation.
Provenance is mandatory.

`$ARGUMENTS` format: `<section> <one-line summary>`, section \(\in\)
`structural | negative | goodie | gap`. The entry body is provided
inline or in a follow-up message.

Examples:
- `/research-capture negative tangent-separator fails at W=0 inflections`
- `/research-capture goodie reusable quintic normal form at §12.3.2`
- `/research-capture gap mixed 4-point factorization still open`
- `/research-capture structural same-tower closure proved in §10.2`

## Protocol

Read current `findings.md`. If the same claim already exists, refine its
`Provenance:` instead of adding a duplicate. Append under the right `##`
heading with `Provenance:` always, plus `Do-not-retry:` for Negative
entries.

If the file exceeds 200 lines after this append, run `findings-prune`.

Stage `findings.md` by name and commit
`findings: capture <section> — <summary>`. If the entry came out of a
team-dir session, cite the dir in the body.

## Don't

Add entries without provenance. Add a Negative without `Do-not-retry:`.
Add status annotations inside entries — presence is the signal, removal
is promotion or rejection.
