---
name: paper-biblio
description: Alphabetize, de-dupe, verify, and clean up the bibliography of <paper>/<main>.tex. Caches user decisions in papers/<name>-biblio-known.md.
---

# Paper Biblio

Alphabetize, de-dupe, verify, and clean up the bibliography of
`<paper>/<main>.tex`. Cache user decisions in
`papers/<name>-biblio-known.md` so nothing gets re-flagged across runs.

`$ARGUMENTS`: empty → `<paper>/<main>.tex` (do NOT use an mtime
heuristic — `unverified.tex` is more recent); file path → that paper;
`--skip-external` → no web verification; `--force-recheck` → ignore
cache.

## What this skill does

Never adds `\bibitem` entries or `\cite` references. May remove exact
duplicates and fix formatting with user approval. Works only inside
`\begin{thebibliography}...\end{thebibliography}`.

- **Alphabetize** by cite key (case-insensitive), preserving blank
  lines.
- **Orphan / dangling detection** — bibitems never cited, cites without
  a bibitem. Report only, no auto-fix.
- **Duplicate detection** — exact-key dupes auto-removed (keep first);
  near-dupes (same first-author surname + year) surfaced via
  `AskUserQuestion`, decision cached.
- **Formatting** — title emphasis consistency, journal abbreviation
  consistency, year placement, page-range dashes (`--`), trailing
  periods, arXiv format, URLs for online sources. Each issue
  `AskUserQuestion`-batched, decisions cached.
- **Citation-context audit** — for each `\cite{key}`, verify the
  surrounding text accurately describes what the cited paper proves.
  Common errors: wrong attribution, conjecture vs theorem, year
  mismatch, survey-vs-original. Cached decisions skipped.
- **Existence verification** — cached (≤ 90 days) skipped; else web
  search for title + author + year, confirm venue/volume/pages. Batch
  5, brief pauses. `--skip-external` skips this step.
- **arXiv-to-journal upgrade** — for arXiv-only citations, search for
  a published journal version; if found, replace (user-confirmed). If
  both are present, keep the journal citation only.

## Cache format — `papers/<name>-biblio-known.md`

```markdown
# Bibliography — Known Good (<name>)
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
- Be conservative with "not found" — older papers may not be indexed;
  flag `unverifiable` rather than `nonexistent`.
- Touch only the bibliography block — nothing outside.
