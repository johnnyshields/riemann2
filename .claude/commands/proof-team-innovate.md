# Proof Team Innovate

Brainstorm and launch new angles of attack that no active agent is currently pursuing.

## Steps

1. **Survey the landscape:**
   - Read the team config (`~/.claude/teams/fannes-proof/config.json`) to see all active agents
   - Read the master synthesis lore (`lore/20260322-fannes-master-synthesis.md`) and final status (`lore/20260322-fannes-final-status.md`) for the current state
   - Read any recent agent lore files for the latest findings
   - Check the task list for active tasks

2. **Identify the current gap:**
   - What is the specific analytical statement that remains unproved?
   - What approaches are currently being pursued by active agents?

3. **Brainstorm new angles:**
   - Think of 2-5 genuinely new approaches that NO active agent is trying
   - For each, assess: plausibility (high/medium/low), novelty (is this truly different from what's been tried?), and effort (1 agent or 2-3?)
   - Eliminate any approach that is equivalent to or a subset of something already tried (check the "Definitively Ruled Out" list in the synthesis)

4. **Filter and launch:**
   - For high-plausibility ideas: spin up 1-3 agents immediately (use TeamCreate tool)
   - For medium-plausibility ideas: spin up 1 agent
   - For low/far-fetched ideas: use AskUserQuestion to ask the user before spinning up
   - Each agent should be given:
     - The specific analytical gap to close
     - Full context from the synthesis lore
     - The specific novel approach to try
     - Instructions to write lore and preserve scripts per CLAUDE.md

5. **Report:**
   - List the new agents and their approaches
   - Explain why each approach is genuinely different from what's been tried
   - Note any ideas you considered but rejected (and why)
