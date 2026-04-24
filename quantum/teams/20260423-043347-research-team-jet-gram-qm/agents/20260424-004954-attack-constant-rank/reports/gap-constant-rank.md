# gap-constant-rank

- **Claim**: In the exact unitary/Krylov setting \(\psi(t)=e^{-itH}\psi_0\), both canonical subspace families
  \[
  A_r(t)=e^{-itH}A_r(0),
  \qquad
  O_r(t)=e^{-itH}O_r(0)
  \]
  have exactly constant rank and move by conjugation in the Grassmannian. Consequently:
  \[
  \Pi_{A_r(t)}=e^{-itH}\Pi_{A_r(0)}e^{itH},
  \qquad
  \Pi_{O_r(t)}=e^{-itH}\Pi_{O_r(0)}e^{itH},
  \]
  the local projector metrics are smooth for all \(t\), and the multiplicity pattern of the two-point principal-angle spectra between \(A_r(t_-)\) and \(A_r(t_+)\), or between \(O_r(t_-)\) and \(O_r(t_+)\), depends only on the time difference \(\Delta=t_+-t_-\).
- **Status**: proved
- **Evidence**: Proved: the exact unitary/Krylov theorem gives \(A_r(t)=e^{-itH}A_r(0)\) and \(O_r(t)=e^{-itH}O_r(0)\). Therefore their dimensions are constant, their projectors evolve by conjugation, and every subspace invariant built from the endpoint pair reduces to the pair \((S(0),e^{-i\Delta H}S(0))\). In particular, the projector-compression spectra and principal-angle multiplicities are functions of \(\Delta\) alone, and the local projector metric formulas from the commutator attack hold globally along the orbit without rank-jump caveats.
- **Exact refs**: `quantum/teams/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md:3-41`; `quantum/teams/20260424-002612-attack-propagator-subspaces/reports/gap-propagator-subspaces.md:3-29`; `quantum/teams/20260424-001425-attack-commutator-metric/reports/gap-commutator-metric.md:3-31`; `quantum/teams/20260424-004954-attack-constant-rank/notes/coordinator-brief.md:3-10`.
- **Dependencies**: Exact unitary evolution with sufficient domain regularity so the Krylov identities hold through order \(r\).
- **Strongest objection**: This is a useful cleanup corollary, not a new theorem with independent content.
- **Needed for promotion**: At most add one sentence in the note that exact unitary orbits avoid rank-jump issues entirely.
