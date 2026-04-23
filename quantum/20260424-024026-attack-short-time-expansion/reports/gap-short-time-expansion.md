# gap-short-time-expansion

- **Claim**: Let \(S(t)=e^{-itH}S(0)\) be a finite-dimensional exact unitary subspace orbit in `quantum/`, let \(\Pi_t\) be the orthogonal projector onto \(S(t)\), and define the compressed propagator and projector compression
  \[
  C_t(\Delta):=\Pi_t e^{-i\Delta H}\big|_{S(t)}:S(t)\to S(t),
  \qquad
  K_t(\Delta):=C_t(\Delta)C_t(\Delta)^*
  =\Pi_t\Pi_{t+\Delta}\Pi_t\big|_{S(t)}.
  \]
  Write
  \[
  L_t:=(I-\Pi_t)H\Pi_t,
  \qquad
  M_t:=L_t^*L_t=\Pi_t H(I-\Pi_t)H\Pi_t\big|_{S(t)}.
  \]
  Then the strongest exact small-\(\Delta\) subspace-level asymptotic is
  \[
  K_t(\Delta)=I_{S(t)}-\Delta^2 M_t+O(\Delta^3),
  \]
  so the leading defect from identity is exactly the leakage operator \(M_t\). Equivalently,
  \[
  \operatorname{Tr}\bigl(I-K_t(\Delta)\bigr)=\Delta^2\operatorname{Tr}(M_t)+O(\Delta^3),
  \qquad
  \operatorname{Tr}(M_t)=\frac12\|\dot\Pi_t\|_{HS}^2.
  \]
  In rank one, \(M_t\) reduces to the Hamiltonian variance on the ray.
- **Status**: proved
- **Evidence**: Proved: the exact unitary-orbit formulas already established in the note give \(\dot\Pi_t=-i[H,\Pi_t]\) and \(\frac12\|\dot\Pi_t\|_{HS}^2=\|(I-\Pi_t)H\Pi_t\|_{HS}^2\). Also
  \[
  \Pi_{t+\Delta}=e^{-i\Delta H}\Pi_t e^{i\Delta H}
  =\Pi_t-i\Delta[H,\Pi_t]-\frac{\Delta^2}{2}[H,[H,\Pi_t]]+O(\Delta^3).
  \]
  Multiplying by \(\Pi_t\) on both sides and using \(\Pi_t\dot\Pi_t\Pi_t=0\) gives
  \[
  \Pi_t\Pi_{t+\Delta}\Pi_t
  =\Pi_t-\frac{\Delta^2}{2}\Pi_t[H,[H,\Pi_t]]\Pi_t+O(\Delta^3)
  =\Pi_t-\Delta^2\Pi_t H(I-\Pi_t)H\Pi_t+O(\Delta^3),
  \]
  which is the stated expansion after restricting to \(S(t)\). For rank one, \(M_t\) is scalar and equals the usual Hamiltonian variance, recovering the Fubini-Study/QGT local metric coefficient.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-372`; `quantum/findings.md:73-76`; `quantum/20260424-001425-attack-commutator-metric/reports/gap-commutator-metric.md:3-31`; `quantum/20260424-002612-attack-propagator-subspaces/reports/gap-propagator-subspaces.md:3-29`; `quantum/20260424-024026-attack-short-time-expansion/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Exact unitary subspace orbit hypothesis; differentiability of \(t\mapsto\Pi_t\); the existing commutator formula and compressed-propagator theorem.
- **Strongest objection**: This is an exact short-time corollary, not a new independent invariant. In higher rank the leading coefficient is an operator-valued leakage term, not a single scalar variance.
- **Needed for promotion**: Include it only as a short corollary immediately after the exact unitary-orbit subsection.
