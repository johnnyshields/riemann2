---
name: paper-biblio
description: Alphabetize, de-dupe, verify, and clean up the bibliography of <paper>/<main>.tex. Caches user decisions in papers/<name>-biblio-known.md.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Biblio

Alphabetize, de-dupe, verify, and clean up the bibliography of
`<paper>/<main>.tex`. Cache user decisions in
`papers/<name>-biblio-known.md` so nothing gets re-flagged across runs.

`$ARGUMENTS`: empty â†’ `<paper>/<main>.tex` (do NOT use an mtime
heuristic â€” `<team-dir>/uv.md` is more recent); file path â†’ that paper;
`--skip-external` â†’ no web verification; `--force-recheck` â†’ ignore
cache.

## What this skill does

Never adds `\bibitem` entries or `\cite` references. May remove exact
duplicates and fix conservative formatting issues. Works only inside
`\begin{thebibliography}...\end{thebibliography}`.

- **Alphabetize** by cite key (case-insensitive), preserving blank
  lines.
- **Orphan / dangling detection** â€” bibitems never cited, cites without
  a bibitem. Report only, no auto-fix.
- **Duplicate detection** â€” exact-key dupes auto-removed (keep first);
  near-dupes (same first-author surname + year) surfaced as batched
  user questions only when the conservative choice is unclear; cache
  the decision.
- **Formatting** â€” title emphasis consistency, journal abbreviation
  consistency, year placement, page-range dashes (`--`), trailing
  periods, arXiv format, URLs for online sources. Batch unclear issues
  into concise user questions and cache decisions.
- **Citation-context audit** â€” for each `\cite{key}`, verify the
  surrounding text accurately describes what the cited paper proves.
  Common errors: wrong attribution, conjecture vs theorem, year
  mismatch, survey-vs-original. Cached decisions skipped.
- **Existence verification** â€” cached (â‰¤ 90 days) skipped; else web
  search for title + author + year, confirm venue/volume/pages. Batch
  5, brief pauses. `--skip-external` skips this step.
- **arXiv-to-journal upgrade** â€” for arXiv-only citations, search for
  a published journal version; if found and unambiguous, replace. If
  both are present, keep the journal citation only.

## Cache format â€” `papers/<name>-biblio-known.md`

```markdown
# Bibliography â€” Known Good (<name>)
Last updated: YYYY-MM-DD

## Verified Entries
| Key | Title | Verified | Notes |

## Near-Duplicate Decisions
| Key A | Key B | Decision | Date |

## Formatting Decisions
| Issue | Entries | Decision | Date |

## Citation-Context Decisions
| Key | Section | Line(s) | Issue | Decision | Date |
```

Always check the cache before flagging; always write back after new
decisions; sort tables by key.

## Report

```
## Bibliography Report: <name>
- Entries: N / alphabetized: yes-no / reordered: M
- Orphans: N / Dangling: N / Duplicates: N
- Formatting issues: N
- Citation-context: checked N, correct N, issues N
- Verification: cached N, newly verified N, discrepancies N, unverifiable N
```

## Rules

- Preserve blank lines between `\bibitem` entries on reorder.
- Be conservative with "not found" â€” older papers may not be indexed;
  flag `unverifiable` rather than `nonexistent`.
- Touch only the bibliography block â€” nothing outside.


