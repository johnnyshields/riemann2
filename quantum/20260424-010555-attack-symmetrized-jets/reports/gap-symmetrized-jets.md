# gap-symmetrized-jets

- **Claim**: In the multiparameter covariant-jet hierarchy, ordering does not matter at the **subspace** level. Let
  \[
  \nabla_a\xi:=P\bigl(\partial_a\xi-a_a\xi\bigr),
  \qquad
  a_a:=\langle\psi,\partial_a\psi\rangle,
  \qquad
  h_I:=\nabla_{a_k}\cdots\nabla_{a_1}\psi.
  \]
  Then for every total order \(r\), the span of all ordered covariant jets \(h_I\) with \(|I|\le r\) is equal to the span of the **symmetrized** covariant jets of total order at most \(r\). Equivalently, ordering dependence is pushed entirely into lower-order terms.
- **Status**: proved
- **Evidence**: Proved: for \(\xi\in\psi^\perp\), the commutator has the exact form
  \[
  [\nabla_a,\nabla_b]\xi
  =h_a\langle h_b,\xi\rangle-h_b\langle h_a,\xi\rangle-F_{ab}\,\xi,
  \qquad
  F_{ab}:=\partial_a a_b-\partial_b a_a.
  \]
  So \([\nabla_a,\nabla_b]\) is a zero-th order operator on the moving horizontal space: it sends any vector already in the order-\(r\) covariant-jet span back into that same span and does not create higher-order terms. Therefore, whenever two adjacent covariant derivatives are swapped, the difference between the two ordered words is a lower-filtration term. By induction on total order, every ordered word is equal to its full symmetrization modulo lower-order covariant jets, and conversely every symmetrized jet lies in the span of ordered ones. Hence the spans agree at each order.
- **Exact refs**: `quantum/findings.md:50-61`; `quantum/20260423-235606-attack-multiparameter-covariant-jets/reports/gap-multiparameter-covariant-jets.md:3-25`; `quantum/20260424-010555-attack-symmetrized-jets/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The exact multiparameter covariant-jet hierarchy; the projected Berry connection components \(a_a\); the horizontal first jets \(h_a=\nabla_a\psi\); basic filtration/induction on total order.
- **Strongest objection**: This is still a subspace theorem, not a canonical ordered matrix theorem. Symmetrization removes ordering dependence only at the level of the generated span, not at the level of a fully canonical basis or matrix package.
- **Needed for promotion**: Update the note to say that in several parameters, ordered covariant jets are available, but their span can be generated just as well by symmetrized covariant jets. This lets the remaining open problem be stated more sharply: not “ordering,” but whether any canonical matrix/frame package exists beyond the symmetrized subspace data.
