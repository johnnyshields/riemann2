---
name: paper-cut
description: Move a passage from paper/proof_of_rh.tex to paper/cut-for-time.md with full provenance (original location, reason, broken refs), then commit.
---

# Paper Cut

Move a passage from `paper/proof_of_rh.tex` to `paper/cut-for-time.md`
with provenance.

## Steps

1. **Identify the passage.** The user specifies by description, line
   numbers, or `\label`.

2. **Read the passage** in `paper/proof_of_rh.tex`. Note exact content
   and surrounding context.

3. **Check references.** Before cutting, grep `\ref{...}` and
   `\eqref{...}` for any `\label{...}` inside the passage. If references
   exist, note them — either redirect or record as broken in the
   provenance block.

4. **Remove the passage** from `paper/proof_of_rh.tex`. Ensure the
   surrounding text flows; adjust transitions if needed.

5. **Append to `paper/cut-for-time.md`** with this format:

   ```markdown
   ---

   ## From: [Section name] ([context: after/before what])

   **Cut date:** [YYYY-MM-DD]
   **Original location:** paper/proof_of_rh.tex, [line range or label]
   **Reason:** [brief reason for cutting]
   **Broken refs:** [list of `\ref{}` sites that now point nowhere, if any]

   \`\`\`latex
   [exact LaTeX content that was cut]
   \`\`\`
   ```

6. **Commit** the paper edit and `cut-for-time.md` update together.
   Stage by name. Subject: `cut: <one-line summary of what moved>`.

## Notes

- Preserve LaTeX verbatim so the passage can be restored by copy-paste.
- If the passage contains a `rem:wip-*` label tied to a UV-NNN entry in
  `unverified.tex`, update that UV entry (either redirect its `Source in
  paper:` line to the new home or mark the UV as `blocked` with
  explanation). See `CLAUDE.md` §6.
- If the user provides a reason, use it; otherwise infer (redundant, too
  detailed, process documentation, etc.).
