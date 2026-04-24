# Research Workflow

Current coordinator policy lives in `AGENTS.md`. Repo-local Codex skills and
agent reference prompts live in `.agents/`.

Per-dispatch research state lives under:

```
<paper>/teams/YYYYMMDD-HHMMSS-<team-slug>/
├── findings.md
├── uv.md
├── attempts.md
├── dispatch.md
├── collation.md
├── chat.md
└── agents/
    └── YYYYMMDD-HHMMSS-<agent-slug>/
        ├── report.md
        ├── scripts/
        └── notes/
```

See `AGENTS.md` for the authoritative conventions. Use
`.agents/skills/chat-backup/SKILL.md` for structured `chat.md` summaries when
raw Codex transcripts are unavailable.

Directories are not pruned; git history is the archive.
