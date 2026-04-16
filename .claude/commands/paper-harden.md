# Paper Harden

Rigorous review of the paper from three perspectives: mathematical rigor, holistic consistency, and formatting/presentation.

## Agents

Spin up 3 agents:

### 1. referee
**Focus:** Mathematical rigor, correctness, and honest framing.
- Read the FULL paper
- For each proof section, check every claim is justified
- Flag handwavy arguments, unjustified steps, missing hypotheses
- Check that theorem statements match their proofs
- Verify cross-references between proofs are correct
- **No overclaiming:** Flag any result stated as "proved" that is only computationally verified, any "for all" that should be "for tested configurations," any claim stronger than what the proof actually establishes
- **No hedging:** Flag unnecessary qualifiers ("it is worth noting," "we are unaware of," "it should be noted") — state facts directly or remove
- Think like an Annals referee: what would you challenge?
- Report issues ranked by severity

### 2. consistency
**Focus:** Holistic consistency and staleness.
- Read the FULL paper
- Check all notation is consistent (no stale renames, no overloading conflicts)
- Verify all "N proofs" counts match throughout (title, abstract, intro, hierarchy, conclusion)
- Check that comparison tables match actual proof content
- Verify notation summary matches actual usage
- Check beautiful findings appendix references all resolve
- Grep for any orphaned labels or broken references
- Flag anything that feels out of place after recent edits

### 3. formatting
**Focus:** LaTeX formatting and presentation.
- Compile the PDF (pdflatex twice)
- Check for undefined references, multiply-defined labels
- Check for overfull/underfull hboxes (significant ones only)
- Verify \texorpdfstring on all math-in-titles
- Check spacing: no triple blank lines, no orphaned remarks
- Verify bibliography: consistent abbreviation style, all entries cited
- Check that all \begin{} have matching \end{}
- Verify enumerate/itemize formatting consistency
- Report any LaTeX warnings beyond cosmetic hyperref ones

### 4. voice
**Focus:** AI tells, tone, and professional voice.
- Read the FULL paper
- **AI tells:** Flag phrases LLMs produce but mathematicians don't ("it is worth noting," "this provides a framework," "interestingly," "remarkable," "we leverage/utilize/employ," "to the best of our knowledge")
- **Structural AI patterns:** Identically-structured remarks (same template repeated), perfectly parallel bullet lists, overly symmetric structure that reads as generated
- **Voice consistency:** Flag switches between "we" and passive voice within a paragraph, inconsistency in formality
- **Marketing language:** Flag self-congratulatory text ("this is a significant result"), editorial commentary that doesn't add mathematical content, explaining the paper's own title
- **Overclaiming:** Flag claims grander than the actual result, "first to" claims without verification, speculative connections stated as established
- Rank findings: HIGH (would embarrass), MEDIUM (noticeable), LOW (minor style)

## Instructions for all agents
- Read the full paper before starting
- Search relevant lore for context
- Do NOT make changes — report only (unless fixing trivial formatting)
- Write lore documenting findings
- Do NOT shut down after completing
