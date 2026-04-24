# gap-kato-transport

- **Claim**: Let \(I\ni t\mapsto \Pi(t)\) be a \(C^1\) path of orthogonal projections on a Hilbert space, and define the Kato generator
  \[
  K(t):=[\dot\Pi(t),\Pi(t)],
  \qquad
  H_K(t):=i[\dot\Pi(t),\Pi(t)].
  \]
  Then \(K(t)^*=-K(t)\) and \(H_K(t)^*=H_K(t)\). If \(U(t)\) solves
  \[
  \dot U(t)=K(t)U(t)=-iH_K(t)U(t),
  \qquad
  U(0)=I,
  \]
  then \(U(t)\) is unitary and
  \[
  \Pi(t)=U(t)\Pi(0)U(t)^*.
  \]
  So every smooth projector path admits an exact unitary realization by the time-dependent Hamiltonian \(H_K(t)=i[\dot\Pi(t),\Pi(t)]\). Moreover this is the canonical exact choice: it is the unique realizing Hamiltonian with vanishing block-diagonal part relative to \(\Pi(t)\),
  \[
  \Pi(t)H_K(t)\Pi(t)=0,
  \qquad
  (I-\Pi(t))H_K(t)(I-\Pi(t))=0.
  \]
- **Status**: proved
- **Evidence**: Differentiating \(\Pi^2=\Pi\) gives \(\dot\Pi\,\Pi+\Pi\dot\Pi=\dot\Pi\) and \(\Pi\dot\Pi\Pi=0\), hence \([[\dot\Pi,\Pi],\Pi]=\dot\Pi\). Therefore if \(U\) solves \(\dot U=[\dot\Pi,\Pi]U\), then \(Q(t):=U(t)\Pi(0)U(t)^*\) and \(\Pi(t)\) satisfy the same ODE with the same initial condition, so \(Q(t)=\Pi(t)\). The uniqueness of the off-diagonal generator follows because only the off-diagonal block of a self-adjoint Hamiltonian contributes to \(-i[H,\Pi]\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:356-372`; `quantum/findings.md:83-86`; `quantum/teams/20260424-055506-attack-kato-transport/notes/coordinator-brief.md:3-12`.
- **Dependencies**: `C^1` projector path; standard ODE existence/uniqueness for the unitary evolution.
- **Strongest objection**: This is an exact pathwise realization theorem, not a new endpoint-canonical invariant. Different smooth paths with the same endpoints can yield different Kato transport unitaries.
- **Needed for promotion**: Include only as a short corollary of the projector package, with the explicit warning that it is pathwise and not a solution to the endpoint matrix-canonicity problem.
