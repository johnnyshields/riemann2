---
name: trifecta
description: Post-work synthesis — three parallel analysts covering deep internal insights, external literature, and hidden connections to fundamental math. Produces one consolidated lore entry.
---

# Trifecta

Three-angle post-work synthesis: deep internal insights, external
literature, hidden links to fundamental math.

`$ARGUMENTS`: empty → analyze most recent work (git log + recent lore);
topic phrase → focus all three; lore file path → analyze that file.

## Preamble

Read `findings.md`, recent `lore/` entries, and `git log --oneline -n
20`. Skim relevant paper sections. Write a ≤30-line key-findings
summary; it's pasted into all three briefings. Create
`<paper>/teams/<ts>-other-trifecta-<slug>/`.

## Dispatch

`TeamCreate team_name: "trifecta-<slug>"`. Spawn three parallel
agents with the standard briefing (full `findings.md`, 7-field
schema, writing-discipline reminder, self-deposit checklist),
**no `unverified.tex` content** (trifecta analysts are the textbook
spoiler-prone case), and the key-findings summary. Paste: "Label each
connection with a confidence tag before merging" and
"`unsupported`/`blocked`/`no progress` are acceptable returns."

- **`analyst-deep-insights`** — internal structural analysis per
  section: what recent findings reveal, hidden connections, new
  directions. Observations only, no new theorems.
- **`analyst-lit-search`** — external literature via WebSearch. For each
  connection: problem, how our result connects, whether it provides
  progress, key refs with URLs/DOIs. No paper-change proposals.
- **`analyst-under-nose`** — bold / speculative connections to
  fundamental math. Before proposing, must check `findings.md`
  §Negative and flag any match instead of re-proposing a ruled-out
  route.

Individual per-agent lore files are forbidden; the coordinator writes
one consolidated entry.

## Post-cycle

Verify deposits. Write ONE lore file
`lore/<yyyymmdd>-trifecta-<slug>.md`: top-level summary,
section-by-section, literature ranked by strength, under-the-nose
connections ranked by actionability (with Negative overlaps resolved),
suggested paper additions, new references.

Emit `findings.md` deltas via `research-capture` for reusable
goodies / structural observations / recurring gaps. Shut down,
`TeamDelete`, commit lore + team dir + findings edits, cite the dir.
