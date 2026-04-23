Claim

The clean remainder-dominance chain in the current draft is:

1. Proposition `prop:corrected-local-decomposition` writes the corrected zeta-side local deformation exactly as
   `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(x)+R_\zeta(m,\sigma)`.
2. Proposition `prop:canonical-calibration` applies the scalar functional
   `\Psi_{x,d}(X)=\langle A_{\val}(x),X\rangle_\F/\langle A_{\val}(x),M(d)\rangle_\F`
   and converts that exact decomposition into
   `\Psi_{x,d}(\Delta_\zeta)=c_{x,d}(x/B)S(m)+\Psi_{x,d}(R_\zeta)`, with `c_{x,d}\asymp 1`.
3. The same proposition applies to the toy expansion `\Delta_{\toy}(u;d)=u^2M(d)+O(u^4)` and gives
   `\Psi_{x,d}(\Delta_{\toy}(u;d))=u^2+O(u^4)`.
4. If the zeta remainder obeys `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`, then Proposition `prop:canonical-calibration` yields
   `u^2\asymp (x/B)S(m)`.

After exact identification of the scalar occupying the manuscript's `S(m)` slot, the remaining inequality is exactly the remainder-dominance condition
`\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`.
Using Corollary `cor:sharpened-calibration-remainder`, this is reduced to the concrete quantitative condition
`S_2=o(xQ^2S(m))`, since `|\Psi_{x,d}(R_\zeta)|\ll_D S_2/Q^3` and `B_\zeta(m)\asymp Q`.

Proved / conditional / missing separation:

- proved: the exact decomposition, the calibration functional, the toy-side `u^2` extraction, and the reduction of remainder dominance to `S_2=o(xQ^2S(m))`.
- conditional on the draft's stated cutoff choice: Proposition `prop:calibration-remainder-cutoff` obtains remainder dominance if one may choose `R` so that `R^3\gg 1/(xQ\,S(m))` and the fixed-core/cutoff hypotheses apply.
- missing: an unconditional proof inside the current draft that the needed inequality `S_2=o(xQ^2S(m))` holds in the intended calibration regime, and, if `x` is allowed to vary to keep `u` microscopic, the uniform variable-`x` version recorded in `rem:wip-calibration-small-u`.

Status

open

Evidence

Proved.

- Proposition `prop:corrected-local-decomposition` is the exact scalar extraction theorem already in the draft. It defines `R_\zeta` by subtraction of the explicit value-channel term, so no second identification theorem is missing once the correct `S(m)` slot is known.
- Lemma `lem:Aval-small-x` and Proposition `prop:pairing` give the calibration denominator and show `\Psi_{x,d}(A_{\val}(x))\asymp x/B` uniformly on compact `d`-ranges for `0<x\le x_0(D)`.
- Proposition `prop:canonical-calibration` then packages the zeta-side and toy-side expansions into the exact implication
  `\Psi_{x,d}(R_\zeta)=o((x/B)S(m)) \Rightarrow u^2\asymp (x/B)S(m)`.
- Corollary `cor:sharpened-calibration-remainder` proves the normalized remainder bound
  `|\Psi_{x,d}(R_\zeta)|\ll_D S_2/Q^3`.
  Comparing this with the main scale `(x/B_\zeta(m))S(m)` gives the concrete target inequality
  `S_2=o(xQ^2S(m))`.

Conditional on stated hypotheses.

- Proposition `prop:calibration-remainder-cutoff` says that if the cutoff can be chosen with
  `R^3\gg 1/(xQ\,S(m))`, then `S_2=o(xQ^2S(m))`, hence `\Psi_{x,d}(R_\zeta)=o((x/B_\zeta(m))S(m))`.
- This is a sufficient route to remainder dominance, but it is not phrased as an unconditional theorem for the final calibration regime; it is explicitly tied to a quantitative cutoff choice plus the fixed-core/cutoff compatibility package.

Missing.

- The draft sections examined do not prove, without further regime input, that the inequality `S_2=o(xQ^2S(m))` holds where calibration is finally invoked.
- The work-in-progress remark `rem:wip-calibration-small-u` records an additional unresolved issue: if `x` must shrink with `m` to force `|u|<u_0(D)`, then the whole calibration chain must be made uniform in variable `x`, including the remainder bound and the cutoff admissibility condition.

Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:602-737` (`lem:Aval-small-x`, `prop:pairing`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:739-850` (`prop:canonical-calibration`, `prop:calibration-remainder-cutoff`, `rem:status-sharpened-calibration-remainder`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1683` (`prop:corrected-local-decomposition`, `prop:cutoff-compatibility`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754` (`prop:whitened-mixed-transfer`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2209` (`cor:sharpened-calibration-remainder`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5300-5498` (`prop:toy-n-point-direct`, `eq:Xi-toy`, `eq:Xi-toy-calibrated`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5500-5598` (`rem:wip-calibration-small-u`)
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-38`

Dependencies

- Exact source-level identification of the family scalar with the manuscript's `S(m)` slot, as summarized in `positive_s_implication.md`.
- Lemma `lem:Aval-small-x`.
- Proposition `prop:pairing`.
- Proposition `prop:corrected-local-decomposition`.
- Proposition `prop:whitened-mixed-transfer`.
- Corollary `cor:sharpened-calibration-remainder`.
- Proposition `prop:toy-n-point-direct` for the toy-side `u^2` preservation.
- For the cutoff-based route: Proposition `prop:cutoff-compatibility`, Theorem `thm:tail-curvature`, and Proposition `prop:calibration-remainder-cutoff`.

Strongest objection

The draft has reduced the gap to a single explicit inequality, but it has not closed that inequality in the final regime from the sections reviewed. The strongest obstruction is that the manuscript proves only the implication
`S_2=o(xQ^2S(m)) \Rightarrow \Psi_{x,d}(R_\zeta)=o((x/B)S(m))`, and a sufficient cutoff criterion for forcing that implication, not a standalone theorem that the inequality holds where the contradiction argument needs it. A second objection is that `rem:wip-calibration-small-u` shows the fixed-scale calibration may not keep `u` in the microscopic toy regime, so a variable-`x` rewrite may still be required before the calibrated theorem chain is usable in the endgame.

Needed for promotion

1. Prove in the intended calibration regime that `S_2=o(xQ^2S(m))`, or prove an equivalent statement that implies `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`.
2. If the proof uses the cutoff route, prove that one can choose `R` with `R^3\gg 1/(xQ\,S(m))` while remaining inside the admissible corrected-cutoff framework actually used later.
3. If `x` must vary with `m` to ensure `|u|<u_0(D)`, upgrade the fixed-scale calibration, transfer, and remainder estimates to the variable-`x` regime recorded in `rem:wip-calibration-small-u`.
4. Honest verdict: after exact `S`-slot scalar identification, remainder dominance is not a bookkeeping issue. The clean remaining mathematical target is the inequality `S_2=o(xQ^2S(m))` or an equivalent direct proof of `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`.
