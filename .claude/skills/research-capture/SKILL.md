---
name: research-capture
description: Synchronous coordinator append of a single structural / negative / goodie / gap entry to paper/findings.md, with provenance, then commit.
---

# Research Capture

Synchronous coordinator action: append one entry to
`paper/findings.md` and commit. No delegation. No teammates. No task dir.

See `CLAUDE.md` §4 and §10 (provenance is mandatory).

## Arguments

`$ARGUMENTS` format: `<section> <one-line summary>` where
`<section>` ∈ `structural | negative | goodie | gap`.

The full entry body is provided by the coordinator (inline block below
the command, or as a follow-up message).

Examples:
- `/research-capture negative tangent-separator fails at W=0 inflections`
- `/research-capture goodie reusable quintic normal form at §12.3.2`
- `/research-capture gap mixed 4-point factorization still open`
- `/research-capture structural same-tower closure proved in §10.2`

## Protocol

1. Read current `paper/findings.md`.
2. De-dup: if the same or near-same claim already exists, UPDATE its
   `Provenance:` line instead of adding a new bullet.
3. Format the entry per the section's schema (see `CLAUDE.md` §2):
   - **Structural / Goodie / Gap**: bullet with `Provenance:` line
     (file:line, chat path, lore ref, commit SHA, UV-NNN, or task-dir
     report path).
   - **Negative**: bullet with `Provenance:` AND a `Do-not-retry:`
     line describing the specific move to avoid.
4. Append under the correct `##` heading in `paper/findings.md`.
5. Size-check: if `paper/findings.md` exceeds \(200\) lines, the
   coordinator must prune (consider promoting into the paper, merging
   similar bullets, or moving stale entries to
   `paper/findings-in-paper.md` / `paper/unverified-rejected.md`).
6. Stage and commit:

```
git add paper/findings.md
git commit -m "findings: capture <section> — <summary>"
```

If the entry came out of a task-dir session, cite the task dir in the
commit body.

## Anti-patterns

- Do NOT add entries without provenance.
- Do NOT add a `Negative` entry without `Do-not-retry:`.
- Do NOT add status annotations (e.g., "[promoted]", "[rejected]") to
  entries — active files carry no status; removal is the signal.
