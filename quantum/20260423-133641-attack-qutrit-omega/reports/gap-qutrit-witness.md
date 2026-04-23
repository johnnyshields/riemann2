# gap-qutrit-witness

- **Claim**: For the qutrit polynomial family, an explicit equal-overlap / different-\(s_2\) witness is
  \[
  (u,v)=\left(-5,\frac65\right),\qquad (u',v')=\left(-\frac52,-\frac35\right).
  \]
  These satisfy
  \[
  I(u,v)=I(u',v')=\frac{25\sqrt{39}}{273},
  \]
  but
  \[
  s_2(u,v)=\frac{325\sqrt{33126}}{364386}\approx 0.162332761652,
  \qquad
  s_2(u',v')=\frac{925\sqrt{1671846}}{1671846}\approx 0.715391206435.
  \]
- **Status**: proved
- **Evidence**: Proved: from the established formulas
  \[
  I(a,b)=\frac{1+ab+a^2b^2}{\sqrt{(1+a^2+a^4)(1+b^2+b^4)}},
  \qquad
  s_2(a,b)=\frac{|1+4ab+a^2b^2|}{\sqrt{(1+4a^2+a^4)(1+4b^2+b^4)}},
  \]
  exact substitution gives
  \[
  I\!\left(-5,\frac65\right)^2=\frac{625}{1911}=I\!\left(-\frac52,-\frac35\right)^2,
  \]
  hence both overlaps equal \(25\sqrt{39}/273\). Proved: the second singular values differ exactly, since
  \[
  s_2\!\left(-5,\frac65\right)^2=\frac{105625}{4008246},
  \qquad
  s_2\!\left(-\frac52,-\frac35\right)^2=\frac{855625}{1671846},
  \]
  and their difference is strictly positive. So equal endpoint overlap does not determine the second singular value, even for explicit rational endpoints. Conditional: this is in the reduced scalar-phase transport class / identity transport setting already used for the qutrit benchmark. Missing: no independent re-derivation of the full \(2\times2\) whitened block \(\Omega(u,v)\) is included here.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:300-315`; `quantum/findings.md:85-90`; `quantum/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`; `quantum/20260423-133641-attack-qutrit-omega/notes/coordinator-brief.md:5-13`.
- **Dependencies**: The proved qutrit formulas for endpoint overlap \(I(u,v)\) and second singular value \(s_2(u,v)\); the first-horizontal-jet / scalar-phase transport framework already fixed in the note.
- **Strongest objection**: This witness proves endpoint-overlap nonuniqueness for \(s_2\), but by itself it does not show the full whitened matrix \(\Omega(u,v)\) in closed form; a referee may still want the direct matrix formula, not only the singular-value witness.
- **Needed for promotion**: Add this exact witness pair and the displayed exact values to the qutrit benchmark paragraph in the note, with the scalar-phase transport caveat in the same paragraph.
