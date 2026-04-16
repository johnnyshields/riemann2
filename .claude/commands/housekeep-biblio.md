# Housekeep Bibliography

Alphabetize, verify, and clean up the bibliography of a LaTeX paper.

## Arguments

The user's arguments are: $ARGUMENTS

Parse the arguments:
- If empty: housekeep the main paper (most recent `paper/*.tex` not in `paper/old/`)
- If a file path (e.g., `paper/paper15-c.tex`): housekeep that paper
- If `--skip-external`: skip web verification of unconfirmed entries
- If `--force-recheck`: ignore the known-good cache and re-verify everything

## Overview

This skill performs the following checks on a LaTeX `\begin{thebibliography}...\end{thebibliography}` section:

1. **Alphabetize** — Sort `\bibitem` entries by cite key (case-insensitive)
2. **Orphan detection** — Find `\bibitem` entries never referenced by `\cite{}`
3. **Dangling cite detection** — Find `\cite{}` keys with no matching `\bibitem`
4. **Duplicate detection** — Remove exact duplicates; ask user about near-duplicates
5. **Formatting consistency** — Check formatting and ask user to approve fixes
6. **Citation-context audit** — Verify each paper is cited correctly where it appears
7. **Existence verification** — Confirm each paper exists and citation details are correct
8. **Update known-good cache** — Write verified entries + all user decisions to `papers/<name>-biblio-known.md`

**IMPORTANT**: This skill NEVER adds bibliography entries. It may remove exact duplicates and fix formatting with user approval via AskUserQuestion.

## Step 1: Identify the paper

Find the target `.tex` file. Extract the paper's base name (e.g., `paper15-c` from `paper/paper15-c.tex`). This becomes `<name>` for the cache file.

## Step 2: Parse the bibliography

Read the full `.tex` file. Extract:

1. **All `\bibitem{key}` entries** — Each entry is the `\bibitem{key}` line through to (but not including) the next `\bibitem` or `\end{thebibliography}`. Record the key and full text of each entry.
2. **All `\cite{key}` references** — Scan the entire document. Note that `\cite{A, B, C}` contains three keys. Collect every cited key with its line number.

## Step 3: Load the known-good cache

Read `papers/<name>-biblio-known.md` if it exists. This file has the format:

```markdown
# Bibliography — Known Good (<name>)

Last updated: YYYY-MM-DD

## Verified Entries

| Key | Title | Verified | Notes |
|-----|-------|----------|-------|
| AdiprasitoHuhKatz2018 | Hodge theory for combinatorial geometries | 2026-03-22 | Ann. of Math. 188 (2018) |
| ... | ... | ... | ... |

## Near-Duplicate Decisions

Pairs reviewed by user — do not re-flag these in future runs.

| Key A | Key B | Decision | Date |
|-------|-------|----------|------|
| Tao2010sumset | TaoChowla2016 | keep both — different papers | 2026-03-22 |

## Formatting Decisions

Formatting choices confirmed by user — do not re-flag these in future runs.

| Issue | Entries | Decision | Date |
|-------|---------|----------|------|
| page range uses hyphen not en-dash | FooBar2020 | fix → en-dash | 2026-03-22 |
| mixed journal abbreviation style | Baz2019, Qux2021 | leave as-is | 2026-03-22 |

## Citation-Context Decisions

Citation usage reviewed by user — do not re-flag these in future runs.

| Key | Section | Line(s) | Issue | Decision | Date |
|-----|---------|---------|-------|----------|------|
| Karlin1968 | SVD proof chain | 1531 | cited for eigenvalue result — correct (Ch. 5) | confirmed correct | 2026-03-22 |
```

Parse the table into a set of known-good keys with their verification dates.

## Step 4: Alphabetize

Sort all `\bibitem` entries by their cite key, case-insensitive. If the bibliography is already sorted, report "already alphabetized" and skip the edit. Otherwise, rewrite the bibliography section in the `.tex` file with entries in sorted order, preserving blank lines between entries and the `\begin`/`\end` wrapper.

**Be careful**: Only touch the bibliography section. Do not modify anything outside `\begin{thebibliography}` ... `\end{thebibliography}`.

## Step 5: Orphan and dangling detection

Compare the two sets:
- `bibitem_keys` = set of all `\bibitem` keys
- `cited_keys` = set of all keys appearing in `\cite{}`

Report:
- **Orphan bibitems**: keys in `bibitem_keys` but not in `cited_keys` (defined but never cited)
- **Dangling cites**: keys in `cited_keys` but not in `bibitem_keys` (cited but never defined)

Do NOT remove orphans or add missing bibitems — just report them.

## Step 6: Duplicate and near-duplicate detection

Check for:
- **Exact duplicate keys**: same `\bibitem` key appearing more than once. If true duplicates are found (identical key, same content), **remove the duplicate** — keep the first occurrence.
- **Near-duplicates**: entries where the first author surname AND year match (e.g., two entries both by "Tao" in "2016"). Use **AskUserQuestion** to present the near-duplicate pairs and ask whether to merge, keep both, or remove one. Record the user's decision in the `## Near-Duplicate Decisions` section of `papers/<name>-biblio-known.md` so the same pair is not flagged again in future runs.

## Step 7: Formatting consistency checks

Scan each `\bibitem` entry for:
- **Title emphasis**: titles should use `\emph{...}` consistently (all or none)
- **Journal abbreviations**: flag mixed use (e.g., both `J. Amer. Math. Soc.` and `Journal of the American Mathematical Society`)
- **Year format**: years should appear consistently (in parentheses after volume, or at end)
- **Page ranges**: should use `--` (en-dash), not `-` (hyphen) or `---` (em-dash)
- **Trailing periods**: each entry should end with a period (or closing brace before period)
- **arXiv format**: arXiv entries should have a consistent format (e.g., `arXiv:XXXX.XXXXX, YYYY`)
- **URLs for online sources**: blog posts, web pages, and other internet-only references must include a `\texttt{URL}` so readers can locate the source. Check that every `[blog post]`, `[online]`, or similar entry has a URL.

For each formatting inconsistency found, use **AskUserQuestion** to present the issue with the specific entries and ask whether to fix it or leave as-is. Batch related issues together (e.g., all page-range dash issues in one question). Record the user's decisions in the `## Formatting Decisions` section of `papers/<name>-biblio-known.md` so the same issues are not flagged again in future runs.

## Step 7b: Citation-context audit

For each `\cite{key}` in the paper, verify the citation is used correctly in context:

1. **Read the surrounding sentence/paragraph** where the citation appears.
2. **Read the `\bibitem` entry** to understand what the paper actually proves/covers.
3. **Check correctness**: Does the citing text accurately describe what the cited paper does? Common errors:
   - Attributing a result to the wrong paper (e.g., citing Karlin 1968 for a result that's actually from Karlin-Rinott 1980)
   - Citing a paper for a theorem it doesn't contain
   - Misattributing a conjecture vs. a theorem (e.g., saying "X proved" when the paper only conjectured)
   - Getting the year wrong in running text vs. the bibitem (e.g., text says "Tao (2015)" but bibitem says 2016)
   - Citing a survey when the original source would be more appropriate (or vice versa)
4. **Check the known-good cache** — if `papers/<name>-biblio-known.md` has a `## Citation-Context Decisions` section with a prior ruling for this key+line, skip it.
5. **Flag issues** via **AskUserQuestion**, presenting the citing text alongside what the paper actually covers. Record decisions in `## Citation-Context Decisions` in the cache file, including the **section name** (e.g., "SVD proof chain", "Negative dependence", "Number-theoretic applications") — use the `\section`/`\subsection` title or a short contextual description, not the section number.

This step can use your knowledge of well-known mathematical results and their standard attributions. For less-known papers, rely on the existence verification results from Step 8.

## Step 8: Existence verification

For each `\bibitem` entry:

1. **Check the known-good cache first**. If the key is in `papers/<name>-biblio-known.md` and was verified within the last 90 days, skip external verification.

2. **For uncached/stale entries**, verify via web search:
   - Search for the paper title + first author + year
   - Confirm: (a) the paper exists, (b) authors match, (c) journal/venue matches, (d) year matches, (e) volume/pages match if available
   - For arXiv preprints: confirm the arXiv ID exists and matches
   - For books: confirm publisher and edition
   - For blog posts: confirm the URL/source is correct

3. **Record results**:
   - **Confirmed**: all details match — add to known-good cache
   - **Minor discrepancy**: paper exists but some detail differs (e.g., page numbers off by one, slightly different title) — report the discrepancy, add to cache with a note
   - **Not found**: could not confirm the paper exists — flag prominently

**Rate limiting**: Add a brief pause between web searches to avoid rate limiting. Process entries in batches of 5.

If `--skip-external` was passed, skip this step entirely and just report which entries are not yet in the cache.

## Step 8b: arXiv-to-journal upgrade

For each `\bibitem` entry that cites **only** an arXiv preprint (i.e., the citation contains an arXiv ID but no journal/volume/pages):

1. **Search for a journal publication** — search for the paper title + authors to check if it has since been published in a peer-reviewed journal or conference proceedings.
2. **If published**: replace the arXiv-only citation with the full journal citation (journal, volume, year, pages). Remove the arXiv ID — if the paper is published, the arXiv reference is redundant.
3. **If still a preprint**: leave the arXiv citation as-is. Ensure the year matches the arXiv posting date (the YYMM in the arXiv ID), not a later revision date.
4. **If both arXiv and journal are already present**: remove the arXiv ID, keeping only the journal citation.

Use **AskUserQuestion** to confirm before making changes, presenting the current arXiv citation alongside the found journal details.

## Step 9: Update the known-good cache

Write the updated cache to `papers/<name>-biblio-known.md` with the format shown in Step 3. Include all previously-known entries (updated if re-verified) plus newly verified entries. Sort the table alphabetically by key.

## Step 10: Report

Print a structured report:

```
## Bibliography Housekeeping Report: <name>

### Summary
- Total entries: N
- Alphabetized: yes/no (reordered M entries)
- Orphan bibitems: N (list them)
- Dangling cites: N (list them)
- Duplicates: N (list them)
- Formatting issues: N

### Citation-Context Audit
- Citations checked: N
- Correct usage: N
- Misattributions / issues found: N (list them with line numbers)
- Previously reviewed (from cache): N

### Verification
- Already confirmed (from cache): N
- Newly verified: N
- Minor discrepancies: N (list them)
- Not found / unverifiable: N (list them)

### Formatting Issues
(list each issue with line context and user decision)

### Recommended Actions
(prioritized list of remaining issues)
```

## Important Rules

- **NEVER add `\bibitem` entries** — only reorder or remove exact duplicates
- **Remove exact duplicate `\bibitem` keys** automatically (keep first occurrence)
- **Near-duplicates require user approval** via AskUserQuestion before any action
- **Formatting fixes require user approval** via AskUserQuestion before any action
- **NEVER add or remove `\cite{}` references** — only report mismatches
- **Always preserve blank lines** between `\bibitem` entries when reordering
- **Always update the cache file** after verification, including near-duplicate and formatting decisions
- **Check decision history** in `papers/<name>-biblio-known.md` before re-flagging near-duplicates or formatting issues already reviewed by the user
- **Be conservative with "not found"** — some older papers may not be indexed online; flag them as "unverifiable" rather than "nonexistent"
