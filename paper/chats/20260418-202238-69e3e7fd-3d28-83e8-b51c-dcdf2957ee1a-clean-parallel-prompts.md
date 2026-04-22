# Clean parallel prompts

- Source: https://chatgpt.com/c/69e3e7fd-3d28-83e8-b51c-dcdf2957ee1a
- Created: 2026-04-18 20:22:38 UTC
- Default model: gpt-5-4-thinking

---

## User (2026-04-18 20:22:37)

Yes. Here are clean parallel prompts you can paste into separate chats.

I would use three chats.

---

### Chat 1: first-order / ECT / local rigor
Please audit the attached TeX draft as a referee, focusing only on these items:

1. `audit-first-order-surjectivity`
   Check whether the first-order generator map is explicit enough, and whether generic surjectivity onto (M_2(\mathbf C)) is actually proved or still only asserted. If still open, tell me exactly what finite-dimensional rank computation is needed.

2. `audit-ect-criterion-usage`
   Check whether the use of the ECT criterion for the triple ((c,v_5,\Delta_7)) is mathematically correct under the draft’s stated hypotheses. Be precise about regularity, nonvanishing of successive initial Wronskians, and whether the proposition as written is justified.

3. `audit-first-zero-compactness` and `audit-first-zero-implies-tangency`
   Check whether the compact truncation / first-zero / implicit-function-theorem argument is airtight as written. If not, identify the exact missing hypothesis or reformulation needed.

Please do not comment on RH broadly. I only want a careful audit of those three local/global rigor points, using the draft’s exact statements and labels.

---

### Chat 2: quintic and septic local algebra

Use this prompt:

Please audit the attached TeX draft as a referee, focusing only on these items:

1. `audit-quintic-pure-value-trace`
   Check whether the draft actually proves that trace annihilates the quintic pure-value slice (V_{\val}^{(5)}(h)), or whether this is still conditional. If conditional, tell me exactly what remains to be shown and whether the current formulation is honest.

2. `audit-direct-septic-witness`
   Check whether the direct (q^{(7)})-driven septic witness is really established generically nonzero at the level claimed in the draft. Focus on the graded-slice argument and whether the displayed order-7 formulas are enough.

3. `audit-full-septic-fixed-sector`
   Check whether the draft truly has the full total septic fixed-sector pair ((u_7,v_7)), or only the (K_1)-transport contribution plus the direct (q^{(7)})-slice. Identify exactly what is still missing.

Please ignore the later global geometry. I only want a precise audit of the local order-5 / order-7 algebra and whether the current audit remarks are correctly scoped.

---

### Chat 3: adjacent slope ranges / tangent-separator theorem subpieces

Use this prompt:

Please audit the attached TeX draft as a referee, focusing only on the geometry around adjacent ECT intervals.

I want you to check these items:

1. `audit-adjacent-slope-range-hypotheses`
   Do the stated generic boundary hypotheses really imply disjoint interior tangent-slope ranges for adjacent ECT intervals in the two cases:

* (W=0), (M\neq 0), with continuous (m=N/M),
* (M=0), (M'\neq 0), (N\neq 0)?

2. The kernel
   [
   K(s,t)=\det(F(s),F'(s),F(t)),\qquad F=(c,v_5,\Delta_7)
   ]
   as tangent-separator:
   is the interpretation mathematically correct as written?

3. The conditional theorem “adjacent tangent-separator sign regularity implies global no-secant / no-four-secant”:
   is that deduction correct, assuming the adjacent sign theorem itself?

Please do not try to solve the full adjacent sign-regularity theorem unless you have a genuinely rigorous argument. I mainly want an audit of the subclaims that the draft already uses around it.

---

### What to keep in this thread

I would keep these here rather than delegate broadly:

* the full adjacent tangent-separator sign-regularity theorem,
* the full RH endgame plausibility / synthesis,
* any attempt to turn the geometric kernel argument into a finished no-4-secant proof.

Those are the places where parallel chats are most likely to either overclaim or just restate the problem.

### What I would ask them to return

For each chat, ask for:

* “proved as written,”
* “conditional but honestly stated,” or
* “still a real gap,”

for each item, plus exact label names and exact suggested edits if they think something should change.

## Assistant (2026-04-18 20:22:40)

_Stopped thinking_
