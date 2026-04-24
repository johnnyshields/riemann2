# gap-spherical-twist

- **Claim**: A clean non-Veronese benchmark family is the real unit-sphere curve
  \[
  \psi(t)=\bigl(\cos t\cos 2t,\ \cos t\sin 2t,\ \sin t\bigr)^T\in S^2\subset\mathbb R^3.
  \]
  For this family, the first-order ambient plane `A_1(t)=span{\psi(t),\partial_t\psi(t)}` already carries two-point data that is not determined by endpoint overlap alone. Since the family is real and normalized, `O_1(t)=span{\partial_t\psi(t)}` is also canonical, and the same benchmark furnishes non-Veronese richer-than-overlap behavior outside the polynomial line.
- **Status**: proved
- **Evidence**: Proved: the overlap is
  \[
  I(u,v)=\langle\psi(u),\psi(v)\rangle
  =\sin u\sin v+\cos u\cos v\cos 2(u-v).
  \]
  The first-order ambient plane normal is \(n(t)=\psi(t)\times \psi'(t)\), with squared norm
  \[
  \|n(t)\|^2=5-4\sin^2 t,
  \]
  and the nontrivial ambient `A_1` principal-angle cosine is
  \[
  c_{A_1}(u,v)=\frac{\langle n(u),n(v)\rangle}{\sqrt{(5-4\sin^2 u)(5-4\sin^2 v)}}.
  \]
  At the exact point pair \((u,v)=(0,\pi/4)\),
  \[
  I(0,\pi/4)=0,
  \qquad
  c_{A_1}(0,\pi/4)=\frac{\sqrt{15}}{5},
  \]
  and the Jacobian
  \[
  \det\frac{\partial(I,c_{A_1})}{\partial(u,v)}\Big|_{(0,\pi/4)}
  \]
  is numerically nonzero (approximately \(-2.1908902300\)). Therefore the `A_1`
  angle data is locally not determined by overlap alone at that point. Likewise, at \((0,\pi/3)\),
  \[
  I(0,\pi/3)=-\frac14,
  \qquad
  c_{A_1}(0,\pi/3)=\frac{\sqrt{10}}{8},
  \]
  with Jacobian again nonzero. This is enough for a benchmark-level non-Veronese separation result.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:55-89`; `quantum/findings.md:30-33,158-171`; `quantum/teams/20260423-204337-attack-nonveronese/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The family lives in a fixed ambient \(\mathbb R^3\), so the ambient `A_1` plane and its normal are canonical. The criterion used is the exact local Jacobian obstruction to factorization through overlap alone.
- **Strongest objection**: This is a benchmark-level local-separation example, not a new theorem. The nonzero Jacobian is currently only numerical in this report, and the result is stated for the ambient `A_1` data rather than as a full explicit equal-overlap witness pair.
- **Needed for promotion**: If the note wants a non-Veronese benchmark, a short remark with the exact formulas for `I` and `c_{A_1}` and a note that the Jacobian is nonzero at `(0, pi/4)` is likely enough. If a stronger benchmark is wanted, produce an explicit equal-overlap / different-angle witness pair for this family.
