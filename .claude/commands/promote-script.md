# Promote Script

Promote a computation or verification script to a clean, hardened version in `/final-scripts/paper/`.

**Argument:** `$ARGUMENTS` — a description of the proposition, claim, or paper section the script verifies (e.g., "within-zone margin factor of 13", "spectral gap ≥ 1/2", "rectangle identity").

## Steps

1. **Create a team** using `TeamCreate` for this task.

2. **Spawn an agent** on the team with the following instructions:

   > Your task is to find and harden a verification script for: `$ARGUMENTS`
   >
   > **Step 1: Find the claim in the paper.**
   > Search `paper/paper15-c.tex` for the relevant claim. Note the exact wording, line number, and mathematical content.
   >
   > **Step 2: Find existing scripts.**
   > Search the entire repo for Python scripts related to this claim:
   > - `scripts/` and `scripts/wip/`
   > - `computation/`
   > - `final-scripts/paper/`
   > - `.claude/worktrees/*/` (old worktree copies)
   >
   > Use `Grep` with keywords from the claim. Check docstrings and comments.
   >
   > **Step 3: Create the hardened script.**
   > - If an existing script is found, use it as the base. Clean it up, add proper docstring with paper reference (line number), add clear pass/fail output, and follow the conventions of existing scripts in `final-scripts/paper/` (check a few for style).
   > - If no script exists, write one from scratch.
   > - Name it `final-scripts/paper/NN_descriptive_name.py` where NN is the next available number (check existing files).
   > - The script must be self-contained and runnable with `python3 script.py`.
   > - Use `final-scripts/paper/lib/` for shared utilities if applicable.
   >
   > **Step 4: Run the script** to confirm it passes.
   >
   > **Step 5: Write a lore file** at `lore/YYYYMMDD-script-description.md` documenting:
   > - What claim the script verifies (with paper line reference)
   > - Provenance (which existing script it came from, or "written from scratch")
   > - Results (pass/fail counts)
   > - Any issues found (does the paper's claim hold?)
   >
   > **Step 6: Send report** to "team-lead" via SendMessage. Do NOT shut down — stay idle.

3. **Wait for the agent's report** and relay findings to the user.

4. **Do NOT shut down the agent** unless the user explicitly asks.
