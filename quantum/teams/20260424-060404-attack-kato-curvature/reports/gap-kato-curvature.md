# gap-kato-curvature

- **Claim**: Let \(M\ni x\mapsto \Pi(x)\) be a \(C^2\) field of orthogonal projections on a fixed Hilbert space, and let \(E_x=\operatorname{Ran}\Pi(x)\). The exact Kato connection on the projector bundle \(E\to M\) is
  \[
  \nabla_a^{K}s:=\Pi\,\partial_a s
  \qquad (s\ \text{a local section with}\ \Pi s=s),
  \]
  whose pathwise parallel transport along \(\gamma\) is exactly Kato transport:
  \[
  \nabla_{\dot\gamma}^{K}s=0
  \iff
  \dot s=[\dot\Pi,\Pi]s,
  \qquad
  \dot U_\gamma=[\dot\Pi,\Pi]U_\gamma.
  \]
  Its exact curvature is
  \[
  R_{ab}^{K}s=[\nabla_a^{K},\nabla_b^{K}]s
  =\Pi[\partial_a\Pi,\partial_b\Pi]\Pi\,s,
  \]
  equivalently \(R^K=\Pi(d\Pi\wedge d\Pi)\Pi\). Hence:

  1. Local path dependence is obstructed exactly by \(R^K\): for a small coordinate rectangle in the \((a,b)\)-plane based at \(x\), the Kato holonomy on \(E_x\) is
     \[
     I+\delta a\,\delta b\,R_{ab}^{K}(x)+o(\delta a\,\delta b).
     \]
     So if \(R_{ab}^{K}(x)\neq 0\), Kato transport is not endpoint-independent near \(x\).

  2. On a simply connected neighborhood \(U\), Kato transport depends only on endpoints for all paths in \(U\) if and only if \(R^K\equiv 0\) on \(U\). On a non-simply-connected \(U\), zero curvature gives only homotopy-class independence; full endpoint-independence also requires trivial monodromy.

  3. In rank one, \(\Pi=|\psi\rangle\langle\psi|\),
     \[
     R_{ab}^{K}=iF_{ab}\Pi,
     \qquad
     F_{ab}=2\,\Im\langle D_a\psi\mid D_b\psi\rangle,
     \]
     so the obstruction is exactly Berry curvature.
- **Status**: proved
- **Evidence**: Differentiating \(\Pi^2=\Pi\) gives \(\Pi(\partial_a\Pi)\Pi=0\). For any section \(s\) with \(\Pi s=s\), one has \((I-\Pi)\partial_a s=(\partial_a\Pi)s\). Therefore
  \[
  [\nabla_a^K,\nabla_b^K]s
  =\Pi(\partial_a\Pi)(\partial_b\Pi)s-\Pi(\partial_b\Pi)(\partial_a\Pi)s
  =\Pi[\partial_a\Pi,\partial_b\Pi]\Pi\,s.
  \]
  Along a path, \(\nabla_{\dot\gamma}^K s=0\iff \Pi\dot s=0\iff \dot s=\dot\Pi s=[\dot\Pi,\Pi]s\), recovering the Kato ODE. The small-rectangle holonomy expansion is standard connection/curvature theory. In rank one, direct substitution gives \(R^K=iF\Pi\) with Berry curvature \(F\).
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:73-80`; `quantum/paper/jet_gram_quantum_note.md:279-299`; `quantum/paper/jet_gram_quantum_note.md:494-506`; `quantum/findings.md:58-72`; `quantum/teams/20260424-055506-attack-kato-transport/reports/gap-kato-transport.md:3-30`; `quantum/teams/20260424-060404-attack-kato-curvature/notes/coordinator-brief.md:3-12`.
- **Dependencies**: `C^2` projector field on a fixed Hilbert space; standard connection/holonomy facts; the exact Kato transport theorem.
- **Strongest objection**: This is an exact pathwise/no-go theorem for transport, not a positive endpoint matrix theorem. It explains why endpoint-independent transport generally fails in several parameters rather than constructing a stronger canonical matrix package.
- **Needed for promotion**: Add it to the note as the sharp obstruction to endpoint-independent Kato transport, with the rank-one Berry-curvature specialization explicitly mentioned.
