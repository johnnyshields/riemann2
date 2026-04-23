# Paired Value Channel Note

Date: 2026-04-24

## Main conclusion

The theorem-facing paired value-channel deformation can still be treated as a
one-scalar perturbation, but only after the paired source slot and local
whitening interface are fixed.

Safe statement:

- `common paired value slot = B_chi^pair(m) + alpha`, equivalently
  `S_chi^pair(m) = alpha`, with the non-value local data frozen.

The verifier sharpened this scope one step further:

- strongest safe phrasing is `conditional, source-normalized interface`;
- not yet `canonical`, `purely local`, or `source-free`.

## Safe scope

This is not source-free.

`A_{val,chi}^{pair}` becomes meaningful only after:

- paired corrected same-point and mixed blocks are defined;
- microscopic holomorphy is available;
- same-point positivity/nondegeneracy for holomorphic whitening is available.
- explicit slot identification and exact freeze rules are fixed.

The later freeze-rules attack makes the theorem-facing convention explicit:

- vary only the common paired value slot;
- freeze derivative and curvature data at paired background value;
- then define `A_{val,chi}^{pair}` as the first-order whitening linearization in
  that pure paired value direction.

## Report refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-070213-paired-value-channel-routeA/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-070213-paired-value-channel-routeB/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-072820-paired-value-channel-verifier/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-081055-paired-freeze-rules-routeA/report.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-081055-paired-freeze-rules-routeB/report.md`
