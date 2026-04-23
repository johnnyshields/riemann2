# gap-Or-vs-Ar

- **Claim**: On both requested benchmarks, the value-channel-free subspace already carries richer two-point geometry than endpoint overlap alone. For the qutrit first-order family, `O_1` already separates equal-overlap pairs, so adding `span{psi}` in `A_1` is not essential to see richer geometry. For the quartit second-order family, `O_2` is actually finer than `A_2` at the benchmark level: `A_2` collapses to one nontrivial principal-angle cosine, while `O_2` has a genuinely two-angle package. Recommended role split: use `O_r` as the benchmark object for value-channel-free geometry; use `A_r` when the ambient state line itself is part of the intended invariant.
- **Status**: proved
- **Evidence**: Proved: for the qutrit curve \(\psi(t)=(1,t,t^2)^T/\sqrt{1+t^2+t^4}\), the family is real and normalized, so \(j_1(t)=h_t=\partial_t\psi(t)\) and \(O_1(t)=\mathrm{span}\{h_t\}\). Hence the unique principal-angle cosine for `O_1(u),O_1(v)` is
  \[
  c_{O_1}(u,v)=\frac{|\langle h_u,h_v\rangle|}{\|h_u\|\|h_v\|}
  =\frac{|1-u^4-v^4+5uv+4u^3v+4uv^3+5u^3v^3+u^4v^4|}
  {\sqrt{(1+u^2+u^4)(1+v^2+v^4)(1+4u^2+u^4)(1+4v^2+v^4)}}.
  \]
  This is not a function of the endpoint overlap
  \[
  I(u,v)=\frac{1+uv+u^2v^2}{\sqrt{(1+u^2+u^4)(1+v^2+v^4)}},
  \]
  because
  \[
  \det\frac{\partial(I,c_{O_1})}{\partial(u,v)}\Big|_{(0,1)}=\frac{5\sqrt6}{18}\neq 0.
  \]
  So `O_1` already carries richer two-point data than overlap alone. Proved: this differs from the ambient `A_1` datum, whose nontrivial principal-angle cosine is
  \[
  c_{A_1}(u,v)=\frac{|1+4uv+u^2v^2|}{\sqrt{(1+4u^2+u^4)(1+4v^2+v^4)}}.
  \]
  Thus `A_1` is not needed to obtain richness, only a different packaging of it.

  Proved: for the quartit curve \(\psi(t)=(1,t,t^2,t^3)^T/\sqrt{1+t^2+t^4+t^6}\), let
  \[
  n(t)=(-t^3,3t^2,-3t,1)^T,\qquad \nu(t)=\frac{n(t)}{\sqrt{1+9t^2+9t^4+t^6}}.
  \]
  Since \(A_2(t)=n(t)^\perp\) and \(A_2(t)=\mathrm{span}\{\psi(t)\}\oplus O_2(t)\), one has
  \[
  O_2(t)=\psi(t)^\perp\cap n(t)^\perp,\qquad O_2(t)^\perp=\mathrm{span}\{\psi(t),\nu(t)\}.
  \]
  Therefore the principal angles of `O_2(u),O_2(v)` are exactly the singular values of
  \[
  M_{O_2}(u,v)=
  \begin{pmatrix}
  \frac{1+uv+u^2v^2+u^3v^3}{\sqrt{D_4(u)D_4(v)}} & \frac{(u-v)^3}{\sqrt{D_4(u)N_4(v)}}\\[1.2ex]
  -\frac{(u-v)^3}{\sqrt{N_4(u)D_4(v)}} & \frac{1+9uv+9u^2v^2+u^3v^3}{\sqrt{N_4(u)N_4(v)}}
  \end{pmatrix},
  \]
  with \(D_4(t)=1+t^2+t^4+t^6\) and \(N_4(t)=1+9t^2+9t^4+t^6\). The ambient `A_2` datum is only the codimension-one normal cosine
  \[
  c_{A_2}(u,v)=\frac{|1+9uv+9u^2v^2+u^3v^3|}{\sqrt{N_4(u)N_4(v)}},
  \]
  giving principal cosines \((1,1,c_{A_2})\). By contrast, `O_2` has two generally nontrivial cosines. At \((u,v)=(0,1)\),
  \[
  M_{O_2}(0,1)=
  \begin{pmatrix}
  \frac12 & -\frac1{\sqrt{20}}\\[0.8ex]
  \frac12 & \frac1{\sqrt{20}}
  \end{pmatrix},
  \]
  so the `O_2` principal cosines are exactly
  \[
  \left(\frac1{\sqrt2},\frac1{\sqrt{10}}\right),
  \]
  while the `A_2` nontrivial cosine is only \(1/\sqrt{20}\). Proved: `O_2` is not determined by overlap alone, because with \(I_4(u,v)=\langle\psi(u),\psi(v)\rangle\),
  \[
  \det\frac{\partial(I_4,\det M_{O_2})}{\partial(u,v)}\Big|_{(0,1)}=\frac{3\sqrt5}{20}\neq 0.
  \]
  So `O_2` already carries richer second-order geometry, and on this benchmark it is finer than `A_2`, not poorer.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:298-355,375-419`; `quantum/findings.md:50-69,105-121`; `quantum/20260423-132614-attack-richer-family/reports/gap-richer-family.md:3-29`; `quantum/20260423-135052-attack-quartit-osculating/reports/gap-quartit-principal-angles.md:3-43`; `quantum/20260423-142558-attack-Or-vs-Ar-benchmarks/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The benchmark families themselves; the proved subspace facts \(O_r=\mathrm{span}\{j_1,\dots,j_r\}\) and \(A_r=\mathrm{span}\{\psi\}\oplus O_r\); standard principal-angle invariance under orthogonal complementation for equal-dimensional subspaces in finite-dimensional Euclidean space; the qutrit first-order orthonormal-frame overlap formula; the quartit codimension-one normal formula.
- **Strongest objection**: The quartit comparison is exact at the subspace/principal-angle level, but not a rescue of a canonical higher-jet matrix invariant. A referee who wants entrywise higher-jet matrix canonicity can still object that the safe object is `O_2` as a subspace, not any raw second-jet Gram matrix.
- **Needed for promotion**: State the benchmark theorem explicitly in the note as: “On the qutrit and quartit benchmarks, `O_r` already detects richer two-point geometry than overlap alone; on the quartit benchmark it is strictly finer than `A_r` at the level of principal-angle data.” If desired, add one clean quartit equal-overlap witness for `O_2` using the same \((0,1)\) and \((1/2,\alpha)\) pair from the note, with \(\alpha\) the positive root of \(81x^6-16x^5+37x^4-128x^3-107x^2-256x-171=0\).
