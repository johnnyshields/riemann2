# gap-generic-local-independence

- **Claim**: A correct local Jacobian criterion exists: if `I(u,v)` is overlap and `a(u,v)` is any smooth scalar invariant extracted from the canonical subspace-angle package, then a nonzero Jacobian `det ∂(I,a)/∂(u,v)` at a point certifies that the subspace-angle data is not locally determined by overlap alone there.
- **Status**: proved
- **Evidence**: If `a = F(I)` locally, then `da` is proportional to `dI`, so the Jacobian must vanish. Therefore nonzero Jacobian is an exact obstruction to local functional dependence through overlap alone. The Veronese richness results are benchmark applications of this criterion.
- **Exact refs**: `quantum/findings.md:141-151`; `quantum/teams/20260423-203246-attack-generic-local-independence/notes/coordinator-brief.md:3-13`.
- **Dependencies**: Smooth scalar spectral invariants of the canonical projector compression.
- **Strongest objection**: This is a criterion, not a generic theorem.
- **Needed for promotion**: Keep as background method rather than note theorem.
