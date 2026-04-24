---
name: paper-biblio
description: Alphabetize, de-dupe, verify, and clean up the bibliography of a paper main TeX file. Caches coordinator decisions in paper-specific biblio-known notes.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Biblio

Alphabetize, de-dupe, verify, and clean up the bibliography of
`<paper>/<main>.tex`. Cache decisions in `papers/<name>-biblio-known.md` so
nothing gets re-flagged across runs.

`$ARGUMENTS`: empty -> current paper; file path -> that paper;
`--skip-external` -> no web verification; `--force-recheck` -> ignore cache.

## Scope

Never add `\bibitem` entries or `\cite` references. May remove exact duplicates
and fix conservative formatting issues. Work only inside
`\begin{thebibliography}...\end{thebibliography}` unless reporting a dangling
cite location.

- **Alphabetize** by cite key, case-insensitive, preserving blank lines.
- **Orphan / dangling detection**: bibitems never cited, cites without a
  bibitem. Report only, no auto-fix unless the correction is exact.
- **Duplicate detection**: exact-key dupes auto-removed, keeping first.
  Near-dupes are not removed unless unambiguous; otherwise cache a
  coordinator decision and leave them.
- **Formatting**: title emphasis, journal abbreviations, year placement,
  page-range dashes, trailing periods, arXiv format, and online URLs. Apply only
  conservative fixes; cache unclear decisions.
- **Citation-context audit**: for each `\cite{key}`, verify the surrounding text
  accurately describes what the cited paper proves. Report wrong attribution,
  conjecture/theorem confusion, year mismatch, and survey-vs-original issues.
- **Existence verification**: cached checks newer than 90 days are skipped.
  Otherwise use web search for title + author + year unless `--skip-external`.
- **arXiv-to-journal upgrade**: for arXiv-only citations, search for a published
  version. Replace only when the match is unambiguous; if both are present, keep
  the journal citation.

## Cache Format

```markdown
# Bibliography Known Good (<name>)
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

Always check the cache before flagging; always write back after new decisions;
sort tables by key.

## Report

```markdown
## Bibliography Report: <name>
- Entries: N / alphabetized: yes-no / reordered: M
- Orphans: N / Dangling: N / Duplicates: N
- Formatting issues: N
- Citation-context: checked N, correct N, issues N
- Verification: cached N, newly verified N, discrepancies N, unverifiable N
```

## Rules

Preserve blank lines between `\bibitem` entries on reorder. Be conservative
with "not found"; older papers may not be indexed. Touch only the bibliography
block except for read-only citation-context checks. Stage changed files by name.
