# Proof Team Status

Show the current status of all agents on the `fannes-proof` team.

## Steps

1. Read the team config to get all members:
   ```bash
   cat ~/.claude/teams/fannes-proof/config.json
   ```

2. For each member, check if they are active or terminated.

3. Read the task list to see what each agent is assigned to.

4. Present a table:
   | Agent | Status | Current Task / Last Result |
   |-------|--------|---------------------------|

5. Summarize: how many active, how many idle, how many shut down. What is the current analytical gap being attacked.
