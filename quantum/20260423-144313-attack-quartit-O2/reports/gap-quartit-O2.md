# gap-quartit-O2

- **Claim**: For the quartit cubic benchmark
  \[
  |\psi(t)\rangle=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}},
  \]
  the value-channel-free second-order object \(O_2(t)\) has a compact exact two-point representative. Writing
  \[
  D_4(t)=1+t^2+t^4+t^6,
  \qquad
  N_4(t)=1+9t^2+9t^4+t^6,
  \]
  the principal-angle cosines of \(O_2(u),O_2(v)\) are the singular values of
  \[
  M_{O_2}(u,v)=
  \begin{pmatrix}
  \frac{1+uv+u^2v^2+u^3v^3}{\sqrt{D_4(u)D_4(v)}} & \frac{(u-v)^3}{\sqrt{D_4(u)N_4(v)}}\\[1.2ex]
  -\frac{(u-v)^3}{\sqrt{N_4(u)D_4(v)}} & \frac{1+9uv+9u^2v^2+u^3v^3}{\sqrt{N_4(u)N_4(v)}}
  \end{pmatrix}.
  \]
  In particular,
  \[
  \det M_{O_2}(u,v)=\frac{|1+9uv+9u^2v^2+u^3v^3|}{\sqrt{N_4(u)N_4(v)}},
  \]
  which equals the nontrivial ambient `A_2` cosine. Thus `O_2` refines `A_2`: the latter keeps only the product of the two `O_2` singular values, while `O_2` keeps both.
- **Status**: proved
- **Evidence**: Proved in the benchmark comparison: since \(A_2(t)=\mathrm{span}\{\psi(t)\}\oplus O_2(t)\) and \(A_2(t)=n(t)^\perp\) with quartit normal \(n(t)=(-t^3,3t^2,-3t,1)^T\), one has
  \[
  O_2(t)^\perp=\mathrm{span}\{\psi(t),\nu(t)\},
  \qquad
  \nu(t)=\frac{n(t)}{\sqrt{N_4(t)}}.
  \]
  Therefore the principal-angle cosines of \(O_2(u),O_2(v)\) are the singular values of the cross-Gram between the orthonormal bases \((\psi(u),\nu(u))\) and \((\psi(v),\nu(v))\), which is exactly the displayed matrix \(M_{O_2}(u,v)\). Proved: at \((u,v)=(0,1)\),
  \[
  M_{O_2}(0,1)=
  \begin{pmatrix}
  \frac12 & -\frac1{\sqrt{20}}\\[0.8ex]
  \frac12 & \frac1{\sqrt{20}}
  \end{pmatrix},
  \]
  so the `O_2` principal-angle cosines are exactly \((1/\sqrt2,1/\sqrt{10})\). This exhibits directly that `O_2` has two nontrivial principal-angle cosines, while `A_2` has only one nontrivial cosine \(1/\sqrt{20}\). Conditional: this formula is the identity/scalar-phase representative in the common ambient space. Missing: a fully factorized closed form for the two singular values as explicit algebraic functions of \((u,v)\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:298-355,375-419`; `quantum/findings.md:46-70,105-121,146-156`; `quantum/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:3-29`; `quantum/20260423-144313-attack-quartit-O2/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The quartit benchmark and its normal-vector formula; the exact relation \(A_2=\mathrm{span}\{\psi\}\oplus O_2\); principal-angle invariance under orthogonal complement in finite-dimensional Euclidean space; identity/scalar-phase transport in the common ambient space.
- **Strongest objection**: This is a benchmark-level subspace formula, not a canonical higher-jet matrix invariant. It is exact only as a representative of the `O_2` principal-angle data inside the fixed common ambient space.
- **Needed for promotion**: Add the matrix formula and one witness pair to the note if brevity permits. If not, keep it in the reports and cite only the qualitative consequence: `O_2` is strictly finer than `A_2` on the quartit benchmark.
