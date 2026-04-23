# gap-simple-spectrum-benchmarks

- **Claim**: The conditional simple-spectrum principal-frame corollary is genuinely applicable on the current benchmark families, not just in isolated cases.

  1. On the qutrit first-order benchmarks (`A_1` and `O_1`), there is only one nontrivial principal-angle cosine, so the moving nontrivial block is automatically simple.
  2. On the quartit `O_2` benchmark, the two nontrivial principal-angle cosines are distinct on a nonempty open set; for example at \((u,v)=(0,1)\) they are exactly
     \[
     \frac{1}{\sqrt2},\qquad \frac{1}{\sqrt{10}}.
     \]
  3. More generally, on the Veronese `O_{n-1}` family, the nontrivial complement-spectrum is not identically degenerate. At the sample point \((u,v)=(0,1)\), the explicit `2x2` complement matrix has distinct singular values for every \(n\ge2\): for odd \(n\) they are
     \[
     \sqrt{\frac{2}{n+1}},
     \qquad
     \sqrt{\frac{2}{\binom{2n}{n}}},
     \]
     and for even \(n\) they are one positive singular value and one zero singular value. Hence the degeneracy locus is a proper algebraic subset, so the simple-spectrum frame corollary applies on an open dense set of endpoint pairs.
- **Status**: proved
- **Evidence**: Proved: the qutrit `A_1` and `O_1` benchmark formulas have only one nontrivial angle datum, so there is no nontrivial multiplicity issue on that moving block. Proved: for the quartit `O_2` benchmark, the explicit `2x2` complement matrix at \((0,1)\) is
  \[
  M_{O_2}(0,1)=
  \begin{pmatrix}
  \frac12 & -\frac1{\sqrt{20}}\\[0.8ex]
  \frac12 & \frac1{\sqrt{20}}
  \end{pmatrix},
  \]
  so the singular values are exactly \((1/\sqrt2,1/\sqrt{10})\), hence distinct. Proved: for the Veronese `O_{n-1}` family, the deposited all-`n` complement matrix specializes at \((0,1)\) to
  \[
  M_n(0,1)=
  \begin{pmatrix}
  \frac{1}{\sqrt{n+1}} & \frac{(-1)^n}{\sqrt{\binom{2n}{n}}}\\[1.2ex]
  \frac{1}{\sqrt{n+1}} & \frac{1}{\sqrt{\binom{2n}{n}}}
  \end{pmatrix}.
  \]
  If \(n\) is odd, the columns are orthogonal, so the singular values are the square roots of the column norms, i.e.
  \(\sqrt{2/(n+1)}\) and \(\sqrt{2/\binom{2n}{n}}\), which are distinct for all \(n\ge3\) because \(\binom{2n}{n}>n+1\). If \(n\) is even, the two rows coincide, so the singular values are one positive value and one zero value, again distinct. Therefore the discriminant of the nontrivial singular block is not identically zero, and its zero set is a proper algebraic subset. That proves generic simplicity in the benchmark-family sense.
- **Exact refs**: `quantum/teams/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`; `quantum/teams/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:3-29`; `quantum/teams/20260423-144313-attack-quartit-O2/reports/gap-quartit-O2.md:3-21`; `quantum/teams/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md:3-23`; `quantum/teams/20260424-003729-attack-canonical-frames/notes/coordinator-brief.md:3-13`; `quantum/teams/20260424-004443-attack-simple-spectrum-benchmarks/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The explicit qutrit, quartit, and Veronese complement matrices already proved in the benchmark reports; basic algebra of singular values of `2x2` matrices; the standard fact that the vanishing of a discriminant defines a proper algebraic subset once it is shown not to be identically zero.
- **Strongest objection**: This is still benchmark-family genericity, not a theorem about arbitrary subspace pairs. It only says the simple-spectrum frame corollary is truly available on a large set inside these benchmark families; it does not make simple spectrum a generic fact in the full quantum note.
- **Needed for promotion**: A short remark in the note or findings is justified: the simple-spectrum principal-frame corollary applies on an open dense set for the current benchmark families, so the conditional diagonal normal form is practically available there.
