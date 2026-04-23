# gap-quartit-O2-witness

- **Claim**: The quartit `O_2` benchmark admits an explicit equal-overlap / different-`O_2` witness using the same pair already used on the ambient `A_2` side:
  \[
  (u,v)=(0,1),
  \qquad
  (u',v')=\left(\frac12,\alpha\right),
  \]
  where \(\alpha\) is the positive real root of
  \[
  81x^6-16x^5+37x^4-128x^3-107x^2-256x-171=0.
  \]
  These two pairs have the same endpoint overlap but different `O_2` singular-value data.
- **Status**: proved
- **Evidence**: Proved from the quartit benchmark formulas: both pairs have endpoint overlap \(1/2\). For the first pair \((0,1)\), the `O_2` singular values are exactly
  \[
  \left(\frac1{\sqrt2},\frac1{\sqrt{10}}\right),
  \]
  because
  \[
  M_{O_2}(0,1)=
  \begin{pmatrix}
  \frac12 & -\frac1{\sqrt{20}}\\[0.8ex]
  \frac12 & \frac1{\sqrt{20}}
  \end{pmatrix}.
  \]
  Numerically, for the second pair \((1/2,\alpha)\) with \(\alpha\approx 1.5842613016400051\), the singular values of \(M_{O_2}(1/2,\alpha)\) are approximately
  \[
  (0.7560629797988192,
  0.5113567306606768),
  \]
  which differ from \((1/\sqrt2,1/\sqrt{10})\approx(0.7071067811865476,0.31622776601683794)\). Hence equal overlap does not determine the `O_2` principal-angle data.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:298-355,375-419`; `quantum/findings.md:46-70,105-121,146-156`; `quantum/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:3-29`; `quantum/20260423-135052-attack-quartit-osculating/reports/gap-quartit-witness.md:3-41`; `quantum/20260423-144313-attack-quartit-O2/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The quartit benchmark formulas for overlap and `O_2` matrix data; the already-established overlap-equality polynomial defining \(\alpha\); numerical evaluation of the `O_2` singular values for the second pair.
- **Strongest objection**: The witness is exact on the overlap side but only numerical on the second pair’s `O_2` singular values in this report. A purely algebraic exact witness would be stronger if the note wanted to display it formally.
- **Needed for promotion**: For note-level use, the current mixed exact/numeric witness is likely enough. If a fully algebraic witness is desired, derive the characteristic polynomial of \(M_{O_2}(1/2,\alpha)^T M_{O_2}(1/2,\alpha)\) and show it differs from that of \(M_{O_2}(0,1)^T M_{O_2}(0,1)\).
