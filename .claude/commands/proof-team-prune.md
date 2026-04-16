# Proof Team Prune

Gracefully shut down all idle agents on the `fannes-proof` team after finalizing their work.

## Steps

1. Read the team config:
   ```bash
   cat ~/.claude/teams/fannes-proof/config.json
   ```

2. For each member that is idle (not the team-lead):
   a. Send a message asking them to:
      - Finalize their lore file (write to `lore/` if not already done)
      - Move any scripts from `scripts/wip/` to `scripts/` (final versions)
      - If any script is a computational verification of something in the paper, create a hardened version in `final-scripts/paper/`
      - Commit all changes
   b. Wait for confirmation
   c. Send a shutdown request

3. Report which agents were pruned and which are still active.

4. Do NOT prune agents that are actively working (non-idle). Only prune idle agents.
