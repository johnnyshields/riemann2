---
name: script-promote
description: Harden a verification script from scripts/wip into a final-scripts paper directory with a clean docstring, paper cross-reference, provenance, and a lore note.
---

# Script Promote

Promote a verification script to a hardened version in `final-scripts/<paper>/`.

`$ARGUMENTS`: a description of what the script verifies, e.g. `"within-zone margin factor of 13"` or `"spectral gap \(\ge 1/2\)"`.

## Preamble

Read the current team dir's `findings.md`, `uv.md`, and relevant reports. Create `<paper>/teams/<ts>-other-script-<slug>/` with copy-forward `findings.md` and `uv.md`, fresh `attempts.md`, run the ledger gate, and create an `agents/<ts>-promoter-<slug>/` deposit dir.

## Dispatch

When delegated teamwork is authorized, record team name `script-promote-<ts>` in `dispatch.md`. Spawn `promoter-<slug>` with a self-contained hardening brief and the inherited Codex model. Include the specific UV-NNN entry the script verifies, if any. Docstrings and lore state what the script proves cleanly — no overclaim.

**Edit-capable exception:** promoter may create a file under `final-scripts/<paper>/` and a new lore file. No other canonical files.

Promoter's job:

1. Find the claim in `<paper>/<main>.tex`: exact wording, line number, math.
2. Search existing scripts under `scripts/`, `scripts/wip/`, `final-scripts/<paper>/`, and `<paper>/teams/*/scripts/`.
3. Produce `final-scripts/<paper>/NN_descriptive_name.py`, based on existing code when possible, self-contained and runnable. Docstring includes paper line ref, `rem:wip-*`, UV-NNN if applicable, provenance.
4. Run it, record stdout in `notes/run-output.txt`.
5. Write `lore/YYYYMMDD-script-<slug>.md`: claim, paper ref, provenance, result, issues, team dir pointer.
6. Deposit the 9-field report under `agents/<ts>-promoter-<slug>/report.md` and stay available.

## Post-cycle

Coordinator reviews per `Ledger separation`: new findings → `findings.md`, new obligations → `uv.md`, promotion route outcome → `attempts.md`, synthesis → `collation.md`. Commit `final-scripts/<paper>/NN_*.py`, lore file, and team dir by named paths.
