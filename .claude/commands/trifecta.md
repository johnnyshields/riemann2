# Trifecta: Deep Insights, Literature, and Hidden Connections

Spawn three parallel research agents to analyze recent work from three complementary angles:

1. **deep-insights** — Connect findings to each section of the paper (internal structural analysis)
2. **lit-search** — Search the literature for connections to open problems (web search)
3. **under-nose** — Find hidden connections to fundamental mathematics (bold/speculative)

The trifecta of "what does it mean for the paper", "what does the field know", and "what are we missing."

## Arguments

The user's focus is: $ARGUMENTS

Parse the arguments:
- If empty: analyze the most recent work (check git log for recent commits, read recent lore files)
- If a topic (e.g., `continuous II theorem`): focus all three agents on that specific topic
- If a lore file path: analyze the findings in that specific lore file
- Examples:
  - `/trifecta` — analyze whatever was just done
  - `/trifecta continuous II theorem` — focus on the continuous extension
  - `/trifecta lore/20260321-proof-e-DEFINITIVE.md` — analyze Proof E findings

## Setup

1. **Determine what to analyze**: Read recent git log, recent lore files, and/or the user's argument to identify:
   - What was recently proved/discovered
   - Which paper(s) are relevant (check `paper/` directory)
   - What the key findings and structural facts are

2. **Read the paper**: Identify the main paper (most recent `paper/*.tex` that isn't in `paper/old/`). Read it to understand sections, structure, and existing connections.

3. **Read recent lore**: Read the most recent lore files (by date) to understand the current state of the work.

4. **Summarize the key findings** in a compact bullet list that will be shared with all three agents.

## Agent Prompts

**IMPORTANT**: Always use the **TeamCreate** tool first to create a team named `trifecta-{topic}` (e.g., `trifecta-continuous-ii`). Then spawn all three agents as teammates using the **Agent** tool with `team_name` set to the team name. This enables task tracking and inter-agent messaging.

Spawn all three agents **in parallel** using the Agent tool. Each agent MUST:
- Read the full paper
- Read the relevant lore files
- Produce a structured analysis
- **Write their own lore file** to the current branch (e.g., `lore/YYYYMMDD-trifecta-{agent}-{topic}.md`) and commit it
- Send a summary of their findings to team-lead

### Agent 1: deep-insights

**Focus**: Internal structural analysis — connect recent findings to every section of the paper.

For each section of the paper, ask:
- What do the recent findings REVEAL about this section's content?
- Are there hidden connections we missed?
- What new "WHY" explanations emerge?
- What new directions open up?

Look for: hidden beauty, structural insights, "the discrete proof was secretly continuous all along" type revelations, sign/magnitude dualities, algebraic vs. topological distinctions.

### Agent 2: lit-search

**Focus**: External literature connections — search the web for connections to open problems.

Search for connections to active research programs:
- KLS conjecture and log-concave geometry
- Spectral/entropic independence (Anari, Gharan, Oveis)
- Approximate tensorization of entropy
- Strong data processing inequalities (Polyanskiy, Wu)
- Stochastic localization (Eldan, Chen, Klartag)
- Mixing times for Gibbs samplers on structured measures
- Partial information decomposition
- Entropy power inequalities for log-concave distributions
- Optimal transport and displacement convexity
- Any other relevant open problems discovered during search

For each connection: explain the problem, how our result connects, whether it provides progress, and cite key references.

### Agent 3: under-nose

**Focus**: Hidden connections to fundamental mathematics — bold, speculative, "under our nose" links.

Look for connections to:
- The Riemann Hypothesis (via Bost-Connes, Jensen-Polya, zeta zeros)
- Random matrix theory (spectral universality, eigenvalue statistics)
- Algebraic geometry / Hodge theory (Lorentzian polynomials, matroid LC)
- Representation theory (orthogonal polynomials, Bochner classification)
- Quantum information (quantum Gibbs samplers, strong subadditivity)
- Convex geometry (Brunn-Minkowski lineage, displacement convexity)
- Phase transitions and universality (rigidity, topological protection)
- Free probability (non-commutative analogs)
- Any other fundamental areas the findings might touch

Be bold. Be speculative where warranted but honest about what's proven vs. conjectured. The goal is to find connections that could elevate the paper or open entirely new research directions.

## After Agents Report

1. **Consolidate**: Write a single comprehensive lore file `lore/YYYYMMDD-trifecta-{topic}.md` combining all three agents' findings, with:
   - Top-level summary of deepest findings
   - Section-by-section connections (from deep-insights)
   - Literature connections ranked by strength (from lit-search)
   - "Under our nose" connections ranked by actionability (from under-nose)
   - Suggested paper additions (remarks, open questions, references)
   - Key new references to add

2. **Cross-check agent lores**: Read each agent's **individual lore file** (they committed their own) and compare against the consolidated lore. Add any findings that were missed in the consolidation. This is critical — agents often include details in their lore files that they didn't include in their team-lead message.

3. **Commit**: Commit the consolidated lore file with a descriptive message listing the key findings.

4. **Report** to the user with the highlights.
