# Claim

Variable-`x` is not a single local-analytic lemma. The draft already contains the local first-order transport needed to define and normalize `\Psi_{x,d}` uniformly for `0<x\le x_0(D)`, but the step from fixed `x=x_0(D)` to adaptive `x=x(m)` still depends on source-specific uniform control of the corrected finite-`s` package, the tail/remainder bound, and cutoff compatibility in a shrinking-`x` regime. In `grh`, this should be treated as a standalone theorem target only in split form: a local transport theorem plus a separate source-level variable-scale theorem.

# Status

open

# Evidence

Proved:

- The local `A_{\val}` package is genuinely local and already uniform in `x` on compact `d`-ranges. Proposition `prop:explicit-Aval` gives an explicit `A_{\val}(x)` formula. Lemma `lem:Aval-small-x` gives the small-`x` expansion and `\|A_{\val}(x)\|_F\asymp x/B`. Proposition `prop:pairing` proves `|\langle A_{\val}(x),M(d)\rangle_F|\asymp x/B` uniformly for `0<x\le x_0(D)`, `d\in D`. Proposition `prop:canonical-calibration` then defines `\Psi_{x,d}` for every such `x` and shows the main term scales like `(x/B)S(m)` by linearity. This is the clean local-analytic transport piece.
- The decomposition `\Delta_\zeta=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)` is structural rather than endgame-specific. Proposition `prop:corrected-local-decomposition` packages the non-leading part into `R_\zeta`, and Proposition `prop:cutoff-compatibility` shows that enlarging the cutoff does not change the fixed-core objects `M(d)` and `A_{\val}`. So the toy-side comparison object and the calibration functional are stable under cutoff bookkeeping.

Conditional on source-specific input:

- The sharpened remainder estimate is uniform in the value of `x` only because the current proof works in the source regime `x=B_\zeta(m)\sigma` with `|\sigma|\asymp Q^{-1}`. Corollary `cor:sharpened-calibration-remainder` states the bound for `0<x\le x_0(D)`, but its proof invokes Proposition `prop:corrected-local-decomposition`, Proposition `prop:cross-block-perturbation`, the baseline inverse-square-root scales, and Theorem `thm:tail-curvature`. Those inputs are proved from the corrected finite-`s` zeta package, not from local toy algebra alone.
- The holomorphic whitening and perturbation chain is source-specific. Proposition `prop:denominator-comparability` uses the zeta zero-free region `a_\rho\ge \sigma_0/Q` to control omitted-zero denominators on `|s|<\rho_0/Q`. Propositions `prop:block-perturbation` and `prop:cross-block-perturbation` assume microscopic remainder bounds for `\delta q`, `\delta q'`, `\delta q''`, and `\delta\Delta`, plus baseline scales `|q_0(t_\pm)|\asymp Q` and `|s|\asymp L_I\asymp Q^{-1}`. Proposition `prop:corrected-whitening` then uses admissible-midpoint spectral-gap input and `S_2=o(Q)`. None of this is a formal consequence of the local `A_{\val}` computation.
- The cutoff condition for the remainder theorem is also source-side. Proposition `prop:calibration-remainder-cutoff` needs `R^3\gg 1/(xQS(m))` and then invokes Theorem `thm:tail-curvature`, whose proof uses shell counting for omitted zeros near height `m`. This is exactly the kind of family/source theorem that a GRH version would have to replace.

Missing:

- The draft does not prove a shrinking-scale replacement for the fixed-scaled regime `x=B_\zeta(m)\sigma`, `|\sigma|\asymp Q^{-1}`. The open item in `rem:wip-calibration-small-u` is therefore real: one must upgrade the source-side corrected finite-`s` package to a regime `|\sigma|\le cQ^{-1}` or an equivalent formulation genuinely uniform for all `0<x\le x_0(D)`.
- The draft also does not prove that the normalized remainder `|\Psi_{x,d}(R_\zeta)|` stays independent of `x`, or at least mild enough as `x\to 0`, under adaptive choices `x=x(m)`. The corollary gives an `x`-free upper bound only after importing the fixed-scaled perturbation estimates; it does not show that those estimates persist under a new shrinking-scale theorem.
- The cutoff condition may become stronger when `x` shrinks. The current manuscript does not show that `R^3\gg 1/(xQS(m))` remains compatible with the admissible cutoff regime after replacing fixed `x_0(D)` by `x(m)\asymp B_\zeta(m)/S(m)` or smaller.
- For `grh`, variable-`x` should not be advertised as a single portable theorem. The honest theorem target is a two-piece package: `(i)` local transport of `A_{\val}`, pairing, and calibration normalization; `(ii)` source-level uniform control of denominator comparability, corrected whitening, perturbation transfer, and remainder/cutoff estimates in the shrinking-`x` regime.

# Exact refs

- `paper/proof_of_rh.tex:361-396` (`thm:tail-curvature`)
- `paper/proof_of_rh.tex:426-794` (`prop:explicit-Aval`, `lem:Aval-small-x`, `prop:pairing`, `prop:canonical-calibration`)
- `paper/proof_of_rh.tex:796-839` (`prop:calibration-remainder-cutoff`)
- `paper/proof_of_rh.tex:856-946` (`prop:denominator-comparability`)
- `paper/proof_of_rh.tex:948-1143` (`prop:block-perturbation`)
- `paper/proof_of_rh.tex:1145-1458` (`prop:cross-block-perturbation`, `lem:baseline-variation`, `prop:corrected-whitening`)
- `paper/proof_of_rh.tex:1498-1683` (`prop:corrected-local-decomposition`, `prop:cutoff-compatibility`)
- `paper/proof_of_rh.tex:2050-2209` (`cor:sharpened-calibration-remainder`)
- `paper/proof_of_rh.tex:5500-5598` (`rem:wip-calibration-small-u`)
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/aval_transport.md:8-30`

# Dependencies

- Local symmetric normal form and explicit toy anomaly matrix `M(d)`.
- Source theorem replacing zeta-specific denominator comparability on the shrinking microscopic disk.
- Source theorem replacing the corrected finite-`s` perturbation bounds for `\delta q`, `\delta\Delta`, and the baseline whitening scales.
- Source theorem replacing tail curvature / omitted-zero counting and showing the cutoff condition remains admissible when `x` shrinks.

# Strongest objection

The manuscript states several conclusions for `0<x\le x_0(D)`, but the proofs of the remainder and whitening bounds are still anchored to the specific zeta regime `x=B_\zeta(m)\sigma` with `|\sigma|\asymp Q^{-1}` and to zeta zero-counting / zero-free-region input. So one could argue that there is no separate variable-`x` theorem at all yet, only a local notation that hides a fixed-scaled source theorem. From the present draft alone, treating variable-`x` as already transported would overstate what has been proved.

# Needed for promotion

- State the target in split form. Local theorem: uniform `A_{\val}` / pairing / `\Psi_{x,d}` transport for `0<x\le x_0(D)`. Source theorem: corrected finite-`s` package and cutoff/remainder estimates on a shrinking-scale regime sufficient for adaptive `x=x(m)`.
- Prove a source-level analogue of Propositions `prop:denominator-comparability`, `prop:block-perturbation`, `prop:cross-block-perturbation`, and `prop:corrected-whitening` with hypotheses expressed in a family-portable way and valid for `|\sigma|\le cQ^{-1}` or equivalent.
- Prove that Corollary `cor:sharpened-calibration-remainder` survives with constants uniform in the adaptive regime, including the cutoff condition `R^3\gg 1/(xQS(m))`.
- Only after those source-level upgrades should `grh` treat variable-`x` as a standalone theorem target. Before that, the safe verdict is: local transport yes; family/source portability open.
