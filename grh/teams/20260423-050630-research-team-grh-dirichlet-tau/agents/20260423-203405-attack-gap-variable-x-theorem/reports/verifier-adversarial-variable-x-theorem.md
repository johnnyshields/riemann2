# Claim

The safe adversarial summary is:

- in the main paper, UV-001 is still one theorem-sized gap;
- for transport or portability purposes, that gap splits into two layers: `(i)` a local layer that is already proved for `0<x\le x_0(D)` at the level of `A_{\val}`, pairing, and calibration normalization, and `(ii)` a source-level shrinking-scale theorem that is still missing and must carry the corrected finite-`s` package, the calibrated remainder estimate, and cutoff compatibility into the adaptive `x=x(m)` regime.

So `one theorem-sized gap in the main paper, but two-layered for transport` is essentially the right summary, provided the second layer is stated broadly enough to include both the shrinking-scale corrected package and the cutoff/remainder burden.

# Status

open

# Evidence

Proved:

- The local `A_{\val}` algebra is already uniform for small `x`. Proposition `prop:pairing` proves `|\langle A_{\val}(x),M(d)\rangle_\F|\asymp x/B` uniformly for `0<x\le x_0(D)`, and Proposition `prop:canonical-calibration` then gives `\Psi_{x,d}(A_{\val}(x))\asymp x/B` on the same range. This is the proved local transport layer.
- The denominator-comparability statement is already phrased on the whole microscopic disk `|s|<\rho_0/Q`, not only on the fixed-scaled slice `|s|\asymp Q^{-1}`. So from that proposition alone, shrinking `x=B\sigma` inside the disk does not create a new denominator singularity.

Conditional on missing source-level input:

- The sharpened remainder theorem is still explicitly fixed-scaled. Corollary `cor:sharpened-calibration-remainder` assumes `x=B_\zeta(m)\sigma` with `|\sigma|\asymp Q^{-1}`. Its proof imports the perturbation and whitening chain whose stated hypotheses use `L_I\asymp x_0/Q` and `|s|\asymp L_I`. That is the real theorem-sized hole behind adaptive `x(m)`.
- Proposition `prop:calibration-remainder-cutoff` adds a separate quantitative burden: when `x` shrinks, one must still realize `R^3\gg 1/(xQS(m))` inside the admissible cutoff class. The current paper does not prove that compatibility in the adaptive regime.

Claims needing scoped weakening:

- `rem:status-sharpened-calibration-remainder` is too broad as written. The safe version is not that the calibration remainder step is globally finished, but that it is finished in the current fixed-scaled regime.
- `rem:wip-calibration-small-u`, item `(1)`, is too coarse. Pairing uniformity in `x` is already proved. Denominator comparability on the microscopic disk is also already available. The missing part is not the bare existence of the denominator control; it is propagation of the full corrected perturbation/whitening/remainder package to shrinking scale.
- `rem:wip-calibration-small-u`, item `(3)`, should be read as conditional on the shrinking-scale corrected package, not as an independent local issue. From the current text alone, the normalized remainder estimate is proved only after the fixed-scaled source inputs are imported.
- `rem:wip-calibration-small-u`, item `(5)`, is an endgame reformulation issue, not part of the present theorem-sized local gap. It should be scoped separately if the goal is only the variable-`x` theorem.

Strongest safe wording now:

`The local calibration transport for A_{\val} is proved uniformly for 0<x\le x_0(D). What remains open is a shrinking-scale source theorem showing that the corrected finite-s decomposition, whitening/perturbation bounds, calibrated remainder estimate, and admissible cutoff choice persist when x=B_\zeta(m)\sigma is allowed to vary down to the adaptive regime x=x(m).`

# Exact refs

- `paper/proof_of_rh.tex:661-794` (`prop:pairing`, `prop:canonical-calibration`)
- `paper/proof_of_rh.tex:856-903` (`prop:denominator-comparability`)
- `paper/proof_of_rh.tex:948-1199` (`prop:block-perturbation`, `prop:cross-block-perturbation`; fixed-scaled hypotheses through `L_I\asymp x_0/Q` and `|s|\asymp L_I`)
- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)
- `paper/proof_of_rh.tex:1497-1566` (`prop:corrected-local-decomposition`)
- `paper/proof_of_rh.tex:796-839` (`prop:calibration-remainder-cutoff`)
- `paper/proof_of_rh.tex:2050-2209` (`cor:sharpened-calibration-remainder`, explicitly fixed-scaled at lines `2056-2059`)
- `paper/proof_of_rh.tex:841-849` (`rem:status-sharpened-calibration-remainder`)
- `paper/proof_of_rh.tex:5500-5598` (`rem:wip-calibration-small-u`)
- `paper/unverified.tex:43-64` (UV-001)
- `tasks/20260423-203405-attack-gap-variable-x-theorem/reports/gap-variable-x-routeA.md`
- `tasks/20260423-203405-attack-gap-variable-x-theorem/reports/gap-variable-x-routeB.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/aval_transport.md:8-30`

# Dependencies

- UV-009 remains a dependency for the toy-side microscopic threshold and the quantitative `u^4` remainder.
- The missing variable-`x` theorem depends on a shrinking-scale source package replacing the currently fixed-scaled use of perturbation transfer and corrected whitening.
- The same upgrade must also prove cutoff admissibility for `R^3\gg 1/(xQS(m))` when `x=x(m)` shrinks.

# Strongest objection

The current paper mixes two different senses of `variable-x`. The local calibration functional really is uniform for small `x`, but the source-side analytic package used to control `R_\zeta` is not yet written or proved on the same shrinking-scale regime. Because of that mismatch, a reader could mistakenly treat `0<x\le x_0(D)` as already transported through the full theorem chain. From the current text alone, that stronger conclusion is unsupported.

# Needed for promotion

- Replace the broad UV-001 summary by a split promotion target: proved local transport versus missing shrinking-scale source theorem.
- Rewrite any status sentence that sounds global so it says `in the fixed-scaled regime` unless it genuinely survives for adaptive `x`.
- Prove one shrinking-scale theorem covering the corrected finite-`s` decomposition, perturbation/whitening transfer, and calibrated remainder estimate for `|\sigma|\le cQ^{-1}` or equivalent `0<x\le x_*(D)` language.
- Prove separately that the cutoff condition `R^3\gg 1/(xQS(m))` is still admissible under adaptive `x=x(m)`.

Honest verdict: the main paper still has one real UV-sized gap, but the adversarially correct transport diagnosis is two-layered. Local `A_{\val}` transport is in place. The missing theorem is the shrinking-scale source package, with cutoff compatibility attached. Any wording that suggests the full variable-`x` conclusion is already proved should be weakened to that scope.
