# Tasks

Per-dispatch work bundles. One directory per `research-team` / `research-audit`
/ `research-attack` / `paper-rewrite` / etc. cycle, named
`yyyymmdd-hhmmss-<type>-<slug>/` where `<type>` \(\in\) `attack-gap | attack-fund
| audit | verify | other`.

Each task dir contains at minimum:

```
<task-dir>/
├── chat.md         # periodic session transcript backup
├── reports/        # 7-field report per teammate
├── scripts/        # any .py / .sh / .tex produced
└── notes/          # optional per-teammate scratch
```

See `CLAUDE.md` §5 for the full convention; `.claude/skills/chat-backup/SKILL.md`
for how `chat.md` gets populated.

Directories are not pruned — git history is the archive.
