---
name: findings-prune
description: When paper/findings.md exceeds 200 lines, prune. Promote stale-but-proven bullets into the paper, move grep-worthy entries to paper/findings-in-paper.md, and remove noise. Keeps findings.md briefing-size.
---

# Findings Prune

Maintenance pass on `paper/findings.md` when it outgrows brief-size.
See `CLAUDE.md` §2 (findings.md is pasted in full into every delegation
prompt; must stay ≤200 lines).

## When to run

Trigger conditions:

- `wc -l paper/findings.md` returns > 200.
- Or the last `research-capture` commit pushed it over 180 lines (early
  warning).
- Or the user explicitly invokes.

Run after a cycle commits findings, not during.

## Protocol

### Step 1: Snapshot + classify

```sh
wc -l paper/findings.md
```

Read the file in full. For each bullet under each section, assign one
of four dispositions:

- **Keep** — active finding, still informing ongoing work.
- **Promote** — the finding has matured into a theorem / lemma /
  remark that should live in `paper/proof_of_rh.tex`. Coordinator
  schedules the promotion as a separate edit (this skill does not
  promote).
- **Archive** — the finding is still useful reference but no longer
  needs to be briefing-pasted. Move to
  `paper/findings-in-paper.md` (create if absent).
- **Remove** — the finding turned out to be redundant with a `Keep`
  entry, or was superseded. Delete outright; git log preserves it.

### Step 2: Draft the pruned file

Criteria for `Keep`:

- Recurring-open-gaps still open.
- Negative findings still guiding Do-not-retry rules.
- Goodies still actively reused in new work.
- Structural findings that inform current cycles.

Criteria for `Archive` (move to `findings-in-paper.md`):

- Structural findings fully absorbed into a paper theorem / remark
  (the paper now says it, so agents no longer need the briefing bullet
  to know it).
- Goodies whose `Location:` is already well-known and grep-able.

Criteria for `Remove`:

- Redundant paraphrases of another active bullet.
- Explicit supersessions (a later bullet strictly subsumes an earlier).

### Step 3: Apply

1. If `paper/findings-in-paper.md` doesn't exist and any entry is
   being archived, create it with a skeleton explaining its role:

   ```markdown
   # Findings (in paper)

   Entries that were active in `findings.md` but have since been
   absorbed into `paper/proof_of_rh.tex`. Kept here as a grep index
   so context about prior findings is retrievable without replaying
   git log.

   ---
   ```

2. Move `Archive` entries (whole bullet) to `findings-in-paper.md` at
   the end, with a trailing `Archived-on: <yyyymmdd>` line.
3. Delete `Remove` entries from `findings.md`.
4. For `Promote` entries, draft a short followup TODO in a lore note
   or in the next session-handoff — do NOT edit the paper from this
   skill.
5. Verify `wc -l paper/findings.md` is now ≤180 (ideally ≤150).

### Step 4: Commit

```sh
git add paper/findings.md paper/findings-in-paper.md
git commit -m "findings: prune <N> entries (promote/archive/remove: A/B/C)"
```

Body: list the counts per disposition and any `Promote` entries
queued for follow-up.

### Step 5: Auto-push

Per `CLAUDE.md` §11. This is a maintenance commit; batch with
neighboring commits if the auto-push cadence is satisfied.

## Anti-patterns

- Do NOT prune during an active cycle — teammates may be relying on
  the current briefing. Wait for the cycle to complete and commit.
- Do NOT archive a finding merely because it's old — age is not the
  criterion. Active relevance is.
- Do NOT promote a finding into the paper from this skill. Promote is
  a separate deliberate coordinator action with compile-check and the
  usual adversarial gate.
