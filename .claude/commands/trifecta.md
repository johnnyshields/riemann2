# Trifecta: Deep Insights, Literature, and Hidden Connections

Post-work synthesis across three complementary angles:

1. **deep-insights** — connect recent findings to each section of the
   paper (internal structural analysis).
2. **lit-search** — search external literature for connections to open
   problems (web search).
3. **under-nose** — find hidden connections to fundamental mathematics
   (bold, speculative, honest about proven-vs-conjectured).

Answers: "what does it mean for the paper", "what does the field know",
and "what are we missing." See `CLAUDE.md` §5, §7, §8.

## Arguments

`$ARGUMENTS`:
- **empty** — analyze the most recent work (check git log + recent lore).
- **topic phrase** — focus all three on that topic.
- **lore file path** — analyze the findings in that specific lore file.

## Mandatory preamble

1. Read the briefing packet:
   - `paper/findings.md` in full.
   - `paper/unverified.tex` in full.
   - `paper/proof_of_rh.tex` — section structure (grep `\\(sub\\)*section`)
     plus any sections relevant to `$ARGUMENTS`.
   - Recent `lore/` entries (last 3–5 by date).
   - Recent `git log --oneline -n 20` for context on what's new.
2. Produce a short **key-findings summary** (≤30 lines) that will be
   pasted into all three teammate prompts.
3. Create task dir `tasks/<ts>-other-trifecta-<slug>/` with `reports/`,
   `scripts/`, `notes/`. Announce it.

## Dispatch

`TeamCreate team_name: "trifecta-<slug>"`, spawn 3 named teammates in
parallel: `analyst-deep-insights`, `analyst-lit-search`,
`analyst-under-nose`. Each briefing MUST include:
- Full `paper/findings.md` (pasted).
- **NO `paper/unverified.tex` content.** Trifecta analysts are the
  textbook spoiler-prone case per `CLAUDE.md` §7; they work against
  the verified proof state only.
- The key-findings summary from step 2.
- The 7-field report schema.
- The writing-discipline reminder (`CLAUDE.md` §3a): state findings
  directly, no overclaim, no hedge, honest scope disclaimers welcome.
- The self-deposit checklist: final report in
  `tasks/<dir>/reports/<teammate>.md`; no standalone per-teammate
  lore file (the coordinator will write one consolidated lore).
- Explicit non-goals per role below.

### analyst-deep-insights
**Focus**: Internal structural analysis. For each section of the paper,
ask:
- What do the recent findings REVEAL about this section's content?
- Hidden connections missed?
- New "WHY" explanations?
- New directions opening up?
Look for: hidden beauty, structural insights, sign/magnitude dualities,
algebraic vs. topological distinctions.
Non-goals: do not propose new theorems; observations only.

### analyst-lit-search
**Focus**: External literature connections — WebSearch-based.
For each connection: describe the problem, how our result connects,
whether it provides progress, cite key references (with URLs or DOIs).
Broad buckets to probe (not exhaustive): nearby analytic number theory,
recent zeta / L-function advances, any active program that touches the
specific findings in the briefing.
Non-goals: do not propose changes to the paper; return a connections
report.

### analyst-under-nose
**Focus**: Hidden / bold connections to fundamental mathematics.
**Critical constraint**: before proposing any connection, check
`findings.md` §Negative. If a proposal is materially similar to an
entry listed there (especially with a `Do-not-retry:` line), do NOT
propose it — flag the Negative match in your report so the coordinator
can confirm the veto is current.
Bold / speculative welcome, but label `proved` vs `conjectured`
honestly.

## After teammates report

1. Read all 3 reports from `tasks/<dir>/reports/`.
2. Write ONE consolidated lore file at
   `lore/<yyyymmdd>-trifecta-<slug>.md` with sections:
   - Top-level summary of deepest findings.
   - Section-by-section (from deep-insights).
   - Literature connections ranked by strength (from lit-search).
   - "Under our nose" connections ranked by actionability (from
     under-nose), with Negative-overlap flags resolved.
   - Suggested paper additions (remarks, open questions, references).
   - Key new references to add.
3. Emit `findings.md` deltas via `research-capture` for any reusable
   new goodies / structural observations / recurring gaps that surfaced.
4. `SendMessage` each teammate `{type:"shutdown_request"}`, `TeamDelete`.
5. Commit the lore file + task dir + any `findings.md` updates. Cite
   the task dir in the body. Stage by name.
