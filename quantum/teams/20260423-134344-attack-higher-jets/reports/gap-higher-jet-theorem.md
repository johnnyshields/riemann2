# gap-higher-jet-theorem

- **Claim**: Let \(\lambda \mapsto |\psi(\lambda)\rangle\) be a normalized \(C^r\) one-parameter local lift, \(P(\lambda)=I-|\psi(\lambda)\rangle\langle\psi(\lambda)|\), and \(j_k(\lambda)=P(\lambda)\partial_\lambda^k\psi(\lambda)\) for \(1\le k\le r\). Then the pointwise raw higher-jet osculating subspace
  \[
  O_r(\lambda):=\operatorname{span}\{j_1(\lambda),\dots,j_r(\lambda)\}
  \]
  is invariant under both local phase gauge and any \(C^r\) local reparameterization \(\mu=\phi(\lambda)\) with \(\phi'(\lambda)\neq 0\). This is the maximal safe higher-jet repair for the raw projected coordinate jets. What is not proved, and in general is false without extra structure, is invariance of the ordered raw jet matrix, its Gram block, or its bilaterally whitened two-point matrix.
- **Status**: proved
- **Evidence**: Proved: under a local phase change \(\tilde\psi=e^{i\chi}\psi\), \(P\) is unchanged and
  \[
  \tilde j_k=e^{i\chi}\sum_{m=1}^k a_{km}(\chi',\dots,\chi^{(k-m+1)})\,j_m,
  \qquad a_{kk}=1,
  \]
  so the jet coordinates change by an invertible upper-triangular map. The explicit second-order formula \(\tilde j_2=e^{i\chi}(j_2+2i\chi'j_1)\) is the first nontrivial instance. Hence \(O_r\) is gauge-invariant even though the individual \(j_k\) are not covariant for \(k\ge2\). Proved: under a reparameterization \(\mu=\phi(\lambda)\), with \(\alpha=d\lambda/d\mu\), Faà di Bruno gives
  \[
  j_k^{(\mu)}=\sum_{m=1}^k b_{km}(\alpha,\alpha',\dots,\alpha^{(k-m)})\,j_m,
  \qquad b_{kk}=\alpha^k,
  \]
  again an invertible upper-triangular change whenever \(\phi'\neq0\). So \(O_r\) is reparameterization-invariant as a subspace; orientation only affects signs of some coordinates, not the span. Proved: this does not upgrade to a raw higher-jet matrix theorem, because whitening is not invariant under general non-unitary triangular jet-coordinate changes. Conditional: with a fixed gauge-covariant transport rule and locally constant \(\dim O_r\), the transported subspaces can be compared at two points, and singular values/principal angles are the honest candidate invariants. Missing: any proof that raw higher-jet whitened matrices from \(j_k=P\partial_\lambda^k\psi\) are canonical, or that a canonical higher-order covariant-jet/frame/transport package exists.
- **Exact refs**: `quantum/teams/20260423-043347-research-team-jet-gram-qm/reports/gap-closer-gauge.md:3-9`; `quantum/teams/20260423-051725-attack-jet-qgt-core/reports/gap-matrix-vs-subspace.md:3-9`; `quantum/findings.md:35-49,95-124`; `quantum/paper/jet_gram_quantum_note.md:174-247`; `quantum/teams/20260423-134344-attack-higher-jets/notes/coordinator-brief.md:3-16`.
- **Dependencies**: \(C^r\) normalized local lift; \(C^r\) local phase \(\chi\); \(C^r\) local reparameterization \(\phi\) with \(\phi'\neq0\); projector identity \(P\psi=0\); Leibniz rule/Faà di Bruno; linear-algebra fact that invertible upper-triangular coordinate changes preserve span but not whitened matrices. For two-point subspace comparisons: a fixed gauge-covariant transport rule and locally constant rank.
- **Strongest objection**: The theorem is only subspace-level. It does not rescue the paper-style higher-jet matrix built from the ordered raw jets, and it does not by itself give a canonical transported matrix on ray space. If rank jumps, if \(\phi'=0\), or if one asks for matrix entries rather than the span, the statement weakens or fails.
- **Needed for promotion**: The note can safely state a proved theorem only in the form above: raw projected higher jets define a gauge- and reparameterization-invariant osculating subspace, not a canonical higher-jet matrix. To promote further, one would need a deposited proof of one of: a canonical higher-order covariant-jet hierarchy, a canonical transport rule, a canonical frame-selection theorem on \(O_r\), or a proof that only subspace invariants such as principal angles/singular values are the intended endpoint data.
