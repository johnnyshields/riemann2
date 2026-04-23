# gap-multiparameter-covariant-jets

- **Claim**: There is an exact multiparameter gauge-covariant jet hierarchy at the **subspace** level. Let \([\psi]:M\to \mathbb P(\mathcal H)\) be a \(C^r\) pure-state ray field on a parameter manifold, choose a normalized local lift \(\psi\), and write
  \[
  P=I-|\psi\rangle\langle\psi|,
  \qquad
  a_a:=\langle \psi,\partial_a\psi\rangle.
  \]
  Define the covariant derivative on vector fields along the lift by
  \[
  \nabla_a\xi:=P\bigl(\partial_a\xi-a_a\xi\bigr).
  \]
  If \(\xi\mapsto e^{i\chi}\xi\) under local phase gauge, then
  \(\nabla_a\xi\mapsto e^{i\chi}\nabla_a\xi\). For every ordered multi-index
  \(I=(a_1,\dots,a_k)\), define recursively
  \[
  h_I:=\nabla_{a_k}\cdots\nabla_{a_1}\psi.
  \]
  Then each \(h_I\) is gauge-covariant, lies in \(\psi^\perp\), and for every
  order \(r\) one has
  \[
  \operatorname{span}\{h_I:1\le |I|\le r\}=O_r,
  \]
  where \(O_r\) is the canonical projected-jet subspace spanned by all
  \(P\partial^\alpha\psi\) with total order \(|\alpha|\le r\). Hence the
  previously proved ambient-subspace theorem can also be generated from an exact
  gauge-covariant hierarchy, even in several parameters. What still does not
  follow is a canonical ordered matrix package, because different orderings and
  frame choices continue to act by non-unitary block-upper-triangular changes.
- **Status**: proved
- **Evidence**: Proved: under \(|\psi\rangle\mapsto e^{i\chi}|\psi\rangle\), one
  has \(a_a\mapsto a_a+i\partial_a\chi\) and \(P\mapsto P\), so
  \[
  \nabla_a(e^{i\chi}\xi)=e^{i\chi}\nabla_a\xi.
  \]
  Thus the hierarchy is exactly gauge-covariant. Proved: for a raw projected
  mixed partial jet \(j_\alpha:=P\partial^\alpha\psi\), one computes
  \[
  \nabla_a j_\alpha
  =P\partial_a(P\partial^\alpha\psi)-a_a j_\alpha
  =j_{\alpha+e_a}-\langle\psi,\partial^\alpha\psi\rangle j_{e_a}-a_a j_\alpha.
  \]
  This is block-upper-triangular with respect to total order: the leading term is
  the raw projected jet of order \(|\alpha|+1\), and the remaining terms lie in
  lower-order jet spans. Starting from \(h_a=\nabla_a\psi=j_{e_a}\), induction on
  total order shows that every covariant jet \(h_I\) is an upper-triangular
  combination of raw mixed partial jets, and conversely every raw mixed partial
  jet lies in the span of the covariant jets of the same or lower order. Hence
  the spans agree at every order. This yields an exact multiparameter
  covariant-jet hierarchy at the subspace level.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:248-277`; `quantum/paper/jet_gram_quantum_note.md:334-339`; `quantum/findings.md:50-61,158-166`; `quantum/teams/20260423-140931-attack-multiparameter-osculating/reports/gap-multiparameter-theorem.md:3-26`; `quantum/teams/20260423-234645-attack-covariant-jets/reports/gap-covariant-jets.md:3-31`; `quantum/teams/20260423-235606-attack-multiparameter-covariant-jets/notes/coordinator-brief.md:3-14`.
- **Dependencies**: Fixed ambient Hilbert space; normalized local lift; Berry connection components \(a_a\); projected mixed partial jets \(j_\alpha=P\partial^\alpha\psi\); projector calculus for \(\partial_aP\); inclusion of all ordered covariant derivatives up to total order \(r\).
- **Strongest objection**: This is still only a subspace theorem. It does not resolve the canonical matrix problem, and it does not remove ordering dependence at the level of specific ordered covariant-jet arrays. The gain is exact gauge covariance together with span equality, not a new matrix-valued invariant.
- **Needed for promotion**: Update the note to say that the remaining open problem is no longer “find any multiparameter covariant hierarchy,” but rather “find a multiparameter covariant hierarchy that yields a canonical matrix package, if such a package exists at all.”
