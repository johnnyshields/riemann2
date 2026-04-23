# gap-veronese-richness

- **Claim**: For the ambient order-\(n-1\) Veronese theorem with
  \[
  I_n(u,v)=\frac{\sum_{k=0}^n (uv)^k}{\sqrt{D_n(u)D_n(v)}},
  \qquad
  c_n(u,v)=\frac{\sum_{k=0}^n \binom nk^2 (uv)^k}{\sqrt{B_n(u)B_n(v)}},
  \]
  where
  \[
  D_n(t)=\sum_{k=0}^n t^{2k},
  \qquad
  B_n(t)=\sum_{k=0}^n \binom nk^2 t^{2k},
  \]
  the nontrivial principal-angle cosine \(c_n\) is generically **not** a function of endpoint overlap alone for every \(n\ge 2\). In particular, the Jacobian
  \[
  J_n(u,v):=\det\frac{\partial(I_n,c_n)}{\partial(u,v)}
  \]
  is nonzero at \((u,v)=(0,1)\) for all \(n\ge 2\), so no relation \(c_n=F(I_n)\) can hold even locally there.
- **Status**: proved
- **Evidence**: Proved: at \(u=0\),
  \[
  I_n(0,v)=\frac{1}{\sqrt{D_n(v)}},
  \qquad
  c_n(0,v)=\frac{1}{\sqrt{B_n(v)}}.
  \]
  Also,
  \[
  \partial_u I_n(0,v)=\frac{v}{\sqrt{D_n(v)}},
  \qquad
  \partial_u c_n(0,v)=\frac{n^2v}{\sqrt{B_n(v)}},
  \]
  because the coefficient of \((uv)^1\) is \(1\) for \(I_n\) and \(\binom n1^2=n^2\) for \(c_n\), while the denominator derivatives with respect to \(u\) vanish at \(u=0\). Further,
  \[
  \partial_v I_n(0,v)=-\frac{D_n'(v)}{2D_n(v)^{3/2}},
  \qquad
  \partial_v c_n(0,v)=-\frac{B_n'(v)}{2B_n(v)^{3/2}}.
  \]
  Evaluating at \(v=1\), one has
  \[
  D_n(1)=n+1,
  \qquad
  D_n'(1)=2\sum_{k=1}^n k=n(n+1),
  \]
  and by the standard binomial-square identities
  \[
  B_n(1)=\sum_{k=0}^n \binom nk^2=\binom{2n}{n},
  \qquad
  \sum_{k=1}^n k\binom nk^2=n\binom{2n-1}{n-1}=\frac n2\binom{2n}{n},
  \]
  so
  \[
  B_n'(1)=2\sum_{k=1}^n k\binom nk^2=n\binom{2n}{n}=nB_n(1).
  \]
  Therefore
  \[
  J_n(0,1)=
  \frac{-D_n(1)B_n'(1)+n^2B_n(1)D_n'(1)}{2D_n(1)^{3/2}B_n(1)^{3/2}}
  =
  \frac{n(n^2-1)}{2\sqrt{n+1}\,\sqrt{\binom{2n}{n}}}.
  \]
  This is nonzero for every \(n\ge 2\). Hence \(I_n\) and \(c_n\) are locally functionally independent there, and \(c_n\) is not determined by overlap alone.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-363`; `quantum/findings.md:50-64,115-131`; `quantum/teams/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md:3-43`; `quantum/teams/20260423-194242-attack-veronese-richness/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The deposited ambient Veronese theorem; elementary differentiation; the identities \(\sum_k \binom nk^2=\binom{2n}{n}\) and \(\sum_k k\binom nk^2=n\binom{2n-1}{n-1}\).
- **Strongest objection**: This proves only local functional independence near \((0,1)\), not a global classification of level sets or a global explicit witness pair for every \(n\). It is still enough to rule out any local relation \(c_n=F(I_n)\) there, which is the benchmark-family claim actually needed.
- **Needed for promotion**: Add this as a short corollary to the Veronese benchmark-family material: “for every \(n\ge2\), the nontrivial principal-angle cosine is generically not determined by endpoint overlap alone.” No stronger global claim is required.
