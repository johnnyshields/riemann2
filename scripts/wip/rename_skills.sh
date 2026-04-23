#!/usr/bin/env bash
# One-shot mechanical rename sweep for .claude/skills/ to match the new
# CLAUDE.md architecture (team dirs, agents subdirs, per-cycle findings/uv).
# Semantic restructuring (e.g. research-team's "three sibling dirs" → one team
# dir) is handled by manual follow-up edits, not this script.
#
# Idempotent — safe to re-run.

set -euo pipefail

cd /mnt/c/workspace/riemann2/.claude/skills

for f in */SKILL.md; do
  # Order matters: longer/more-specific patterns before their substrings.
  sed -i \
    -e 's|reports/<teammate>\.md|agents/<agent-slug>/report.md|g' \
    -e 's|<teammate>|<agent-slug>|g' \
    -e 's|\bteammates\b|agents|g' \
    -e 's|\bteammate\b|agent|g' \
    -e 's|<task-dir>|<team-dir>|g' \
    -e 's|\btask-dir\b|team-dir|g' \
    -e 's|\btask dirs\b|team dirs|g' \
    -e 's|\btask dir\b|team dir|g' \
    -e 's|paper/proof_of_rh\.tex|<paper>/<main>.tex|g' \
    -e 's|paper/unverified\.tex|<team-dir>/uv.md|g' \
    -e 's|paper/findings\.md|<team-dir>/findings.md|g' \
    -e 's|paper/tasks/|<paper>/teams/|g' \
    -e 's|\btasks/|<paper>/teams/|g' \
    -e 's|\bpaper/|<paper>/|g' \
    -e 's|`proof_of_rh\.tex`|`<paper>/<main>.tex`|g' \
    -e 's|`unverified\.tex`|`<team-dir>/uv.md`|g' \
    -e 's|\\texttt{unverified\.tex}|\\texttt{<team-dir>/uv.md}|g' \
    "$f"
done

echo "sweep complete"
