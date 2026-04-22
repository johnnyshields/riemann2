# Cut from Paper

Move a passage from the paper to the cut-for-time document, tracking provenance.

## Steps

1. **Identify the passage to cut.** The user will specify what to cut (by description, line numbers, or label).

2. **Read the passage** in paper/paper15-c.tex. Note the exact content and surrounding context (what comes before and after).

3. **Remove the passage** from paper/paper15-c.tex. Ensure the surrounding text still flows naturally — adjust transitions if needed.

4. **Append to the cut-for-time document** at `paper/paper15-c-cut-for-time.md`. Use this format:

```markdown
---

## From: [Section name] ([context: after/before what])

**Cut date:** [YYYY-MM-DD]
**Original location:** paper/paper15-c.tex, [line range or description]
**Reason:** [Brief reason for cutting]

\`\`\`latex
[exact LaTeX content that was cut]
\`\`\`
```

5. **Commit** the paper edit and the cut-for-time update together with a descriptive message.

## Notes

- Always preserve the exact LaTeX so it can be restored later by copy-paste.
- If the cut passage contains `\label{}` or `\ref{}`, note any broken references in the reason field.
- If the user provides a reason, use it. Otherwise infer from context (redundant, too detailed, process documentation, etc.).
