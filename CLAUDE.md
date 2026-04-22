# Project notes

- The main paper lives at `C:\workspace\riemann2\paper\proof_of_rh.tex` (WSL path: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex`). Treat it as the canonical source of record.

## LaTeX conventions

- This is a LaTeX-first project. Use LaTeX-native math delimiters everywhere — `\(...\)` for inline and `\[...\]` for display math — in `.tex`, `.md`, `.txt`, commit messages, lore notes, and any other prose. Do not convert to `$...$` / `$$...$$` for GitHub rendering.
- When extracting or cleaning prose from external sources (ChatGPT exports, agent transcripts, etc.) for this repo, preserve `\(...\)` / `\[...\]` as-is.

## Git workflow

- **Auto-commit after each major edit.** When a meaningful edit to the paper (or other tracked source) is complete and self-contained, stage the relevant files and create a commit without asking. Use a concise imperative-mood subject summarizing what changed and why. Do not push — commit only.
- A "major edit" means a finished logical unit: a remark rewrite, an insertion of one or more new blocks, a proof change, a structural reorganization. Minor in-progress touches during an ongoing edit do not each need their own commit.
- Stage files by name; do not use `git add -A` or `git add .`.
- Follow the existing commit-message style (see `git log`).

## Coordinator protocol

- The main chat is the team lead and the only default editor of `paper/proof_of_rh.tex`.
- Treat `paper/proof_of_rh.tex` as the canonical draft and `paper/unverified.tex` as the quarantine ledger for claims, repairs, and endgame steps that are not yet verified.
- Use `lore/` for workflow plans, agent syntheses, verification notes, and session summaries.
- When a native team tool is unavailable, use `Task` subagents as the team members. Prefer separate research and verification agents over a single persuasive agent.
- Delegated agents are read-only by default. They must not edit `paper/proof_of_rh.tex`, `CLAUDE.md`, or commit unless the coordinator explicitly asks for that exact action.
- Every delegated report must separate `proved`, `computational`, `heuristic`, `open`, and `rejected` claims.
- Every delegated report must include exact provenance: file paths, line references, cited lemmas, scripts, or calculations actually used.
- Every delegated report must include a strongest objection or failure mode. Agents should prefer `unsupported` over confident speculation.
- Any new claim, repair, or conjectural bridge goes to `paper/unverified.tex` first unless it is already fully grounded and independently checked.
- Promotion from `paper/unverified.tex` into `paper/proof_of_rh.tex` requires one adversarial verification pass plus coordinator review.
- When a quarantined item is promoted, rejected, or reframed, update `paper/unverified.tex` immediately so the proof state stays synchronized.
