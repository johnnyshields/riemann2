# gap-qutrit-O1-witness

- **Claim**: For the qutrit benchmark
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2)^T}{\sqrt{1+t^2+t^4}},
  \]
  an explicit equal-overlap / different-`O_1` witness is given by the pairs
  \[
  (u,v)=(0,1),
  \qquad
  (u',v')=(-2,\beta),
  \]
  where \(\beta\) is any real root of
  \[
  9x^4-16x^3+5x^2-4x-6=0.
  \]
  For example, the negative root is
  \(\beta\approx -0.507264474718434\).
- **Status**: proved
- **Evidence**: Proved: the endpoint overlap is
  \[
  I(u,v)=\frac{1+uv+u^2v^2}{\sqrt{(1+u^2+u^4)(1+v^2+v^4)}}.
  \]
  For \((u,v)=(0,1)\), one has \(I(0,1)=1/\sqrt3\). Fixing \(u'=-2\), the equation
  \(I(-2,v')=1/\sqrt3\) is exactly equivalent to
  \[
  9v'^4-16v'^3+5v'^2-4v'-6=0,
  \]
  so every real root gives equal overlap with the baseline pair. Proved: the `O_1`
  principal-angle cosine is
  \[
  c_{O_1}(u,v)=\frac{|1-u^4-v^4+5uv+4u^3v+4uv^3+5u^3v^3+u^4v^4|}
  {\sqrt{(1+u^2+u^4)(1+v^2+v^4)(1+4u^2+u^4)(1+4v^2+v^4)}}.
  \]
  At the baseline pair \((0,1)\), this equals \(0\). For \(u'=-2\), the numerator becomes
  \[
  15v'^4-48v'^3-42v'-15=3(5v'^4-16v'^3-14v'-5).
  \]
  This polynomial is coprime to \(9v'^4-16v'^3+5v'^2-4v'-6\), so no real root \(\beta\) of the overlap equation can also make the `O_1` cosine numerator vanish. Hence the `O_1` cosine is different. Numerically, for \(\beta\approx -0.507264474718434\),
  \[
  c_{O_1}(-2,\beta)\approx 0.3093859760298697\neq 0.
  \]
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:298-355`; `quantum/findings.md:46-70,105-121,146-160`; `quantum/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:3-29`; `quantum/20260423-184631-attack-qutrit-O1-witness/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The qutrit benchmark formulas for overlap and `O_1` cosine; the benchmark-level identity/scalar-phase setting; elementary polynomial elimination.
- **Strongest objection**: The witness is exact on the overlap side and exact on the nonvanishing side, but the chosen root \(\beta\) is still given numerically in this report. A fully symbolic closed form for \(\beta\) is possible but not illuminating.
- **Needed for promotion**: Add this witness in one sentence to the note if desired, or keep it as support in the benchmark reports. The current exact polynomial description is already strong enough for citation-level internal use.
