# Sharp convention/caveat extract

## Exceptional-divisor normalization for C

- [confirmed] The theorem-shaped symbol
  `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)`
  is well-posed only if it is read as the **exceptional-divisor value after blow-up**: write `2\omega=\kappa\delta`, factor through an analytic germ in `(m,\kappa,\delta^2)`, then evaluate at `\delta=0`.
- [confirmed] Under this convention, the sharp C statement is not a raw diagonal restriction in `(m,\omega,\delta)`, but the claim that the exceptional-divisor trace is canonically anchored to the one-pair datum:
  `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`.
- [confirmed] This is the right place where `\kappa` lives; without the blow-up reading, the symbol at `\delta=0` is ambiguous.

## Caveat on `C => B`

- [confirmed] The post-C queue simplification `C => B` is valid only if C lands in this **sharp normalization**, i.e. canonical diagonal specialization of the actual corrected reduced package on the exceptional divisor.
- [confirmed] A weaker slogan such as “same reduced image germ at coincidence” is not enough if it still allows a free exceptional-divisor trace `B(m,\kappa)` or leaves scalar normalization unfixed.
- [candidate] So the capture-worthy statement is not merely “after C, B is formal,” but the conditional form:
  **after sharp exceptional-divisor C, B is formal; after weaker reduced coincidence language, it is not.**

## Refs

- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-124500-convention-blocker/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-130500-exceptional-divisor-convention/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-130500-post-C/report.md`
- `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-131500-D-after-C/report.md`
