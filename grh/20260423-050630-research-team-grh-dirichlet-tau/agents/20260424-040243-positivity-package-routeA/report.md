## Claim

The cleanest theorem-facing local package visible in the manuscript is a two-step perturbative whitening package.

Lemma package candidate:

1. `Local same-point positivity transport.` Let `G_{m,\pm}^{(0)}(s)` and `G_{m,\pm}^{\corr}(s)` be holomorphic `2\times 2` same-point block families on `|s|<\rho_0/Q`, with
   `G_{m,\pm}^{\corr}(s)=G_{m,\pm}^{(0)}(s)+R_{m,\pm}(s)`.
   Assume:
   - baseline gap at the center: `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\ge cQ`;
   - small baseline variation: `\sup_{|s|<\rho_0/Q}\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\le \varepsilon Q`;
   - small perturbation: `\sup_{|s|<\rho_0/Q}\|R_{m,\pm}(s)\|\le \eta Q`;
   - `\varepsilon+\eta<c/2`.
   Then `G_{m,\pm}^{\corr}(s)` remain uniformly positive definite on `|s|<\rho_0/Q`, with `\lambda_{\min}(G_{m,\pm}^{\corr}(s))\ge (c/2)Q`.

2. `Holomorphic whitening from positive same-point blocks.` If in addition the corrected mixed block `N_m^{\corr}(s)` is holomorphic on the same disk, then `G_{m,\pm}^{\corr}(s)^{-1/2}` are holomorphic there, and therefore
   `\widehat\Omega^{\corr}(s;m)=G_{m,-}^{\corr}(s)^{-1/2}N_m^{\corr}(s)G_{m,+}^{\corr}(s)^{-1/2}`
   is holomorphic there.

This is the smallest local package actually used later in the corrected local deformation step: it supplies exactly the holomorphic whitening map needed to expand around the background value-channel parameter.

Three-bin split:

- proved in the manuscript: the zeta-instance of this package, by the proof of `prop:corrected-whitening`;
- conditional as a reusable theorem-facing package: the abstract two-step lemma formulation above, because the manuscript still imports rather than isolates some inputs;
- missing: a standalone abstract lemma statement and a clean standalone source for the baseline same-point gap.

Honest verdict: the perturbative mechanism is real and compact, but at present it is manuscript-internal rather than a clean promoted local lemma package.

## Status

conditional

## Evidence

The proof at `paper/proof_of_rh.tex:1417-1458` is already almost the desired package. It does four things.

1. It gets holomorphy of `G_{m,\pm}^{\corr}(s)` and `N_m^{\corr}(s)` on `|s|<\rho_0/Q` from omitted-sum holomorphy plus removable singularities at `s=0`.
2. It compares `G_{m,\pm}^{\corr}(s)` to the single reference matrix `G_{m,\pm}^{(0)}(0)` by
   `G_{m,\pm}^{\corr}(s)-G_{m,\pm}^{(0)}(0) = (G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)) + R_{m,\pm}(s)`.
3. It bounds the two error terms by `\ll \rho_0 Q` and `o(Q)`, while asserting the baseline center gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`.
4. It concludes uniform positivity on the disk and invokes holomorphic functional calculus to get holomorphic inverse square roots.

That is exactly the perturbative transport lemma plus whitening corollary above.

The downstream use in `paper/proof_of_rh.tex:1569-1621` confirms that no stronger local statement is needed. There the manuscript defines the whitening map
`\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}`
and uses the corrected finite-`s` holomorphic-whitening theorem only to justify that this map is analytic on the open set where the same-point blocks stay uniformly positive definite. The later value-channel expansion is then just analyticity of this whitening map plus the definition of `A_{\val}`.

The team notes align with this reading. `same_point_positivity.md` identifies the blueprint as baseline spectral gap, small baseline variation, small perturbation, and holomorphic functional calculus. `paired_slot_hypotheses.md` says the safest theorem-facing wording is an explicit local clause `same-point positivity/nondegeneracy for holomorphic whitening`. `corrected_whitening_transport.md` treats the positivity-plus-whitening step as a partial intermediate bundle, not the whole slot theorem.

## Exact refs

- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`): full local positivity and holomorphic whitening argument.
- `paper/proof_of_rh.tex:1418-1424`: holomorphy of corrected same-point and mixed blocks.
- `paper/proof_of_rh.tex:1426-1455`: perturbative comparison with the baseline center matrix and positivity transport.
- `paper/proof_of_rh.tex:857-946` (`prop:denominator-comparability`): omitted-smooth holomorphy input used at `1418-1424`.
- `paper/proof_of_rh.tex:948-1003` (`prop:block-perturbation`): `\|R_{m,\pm}(s)\|\ll S_2`.
- `paper/proof_of_rh.tex:1332-1390` (`lem:baseline-variation`): `\sup\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\|\ll \rho_0 Q`.
- `paper/proof_of_rh.tex:1436-1439`: imported baseline center gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`.
- `paper/proof_of_rh.tex:1531-1621`: downstream use in the corrected local deformation decomposition.
- `paper/proof_of_rh.tex:465-486` (`eq:A-val-def`, `prop:explicit-Aval`): definition and role of the pure value-channel derivative used after whitening analyticity is available.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:5-23`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-18,39-52,61-70`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-27`.

## Dependencies

- Microscopic holomorphy of the corrected blocks, supplied in the zeta manuscript by denominator comparability plus removable-singularity cancellation.
- Baseline same-point variation bound on the microscopic disk.
- Small perturbation estimate `R_{m,\pm}(s)=o(Q)`, coming from block perturbation plus the invoked tail-curvature input.
- Baseline same-point center gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` on the admissible midpoint class.
- Holomorphic functional calculus for the matrix square root on the positive-definite cone.

## Strongest objection

The manuscript does not yet expose the center-gap input as a standalone proposition inside this local package. At `paper/proof_of_rh.tex:1436-1439` the proof simply invokes `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` for the baseline jet-limit block, and then proceeds. So the abstract perturbative lemma is visible, but its most important quantitative hypothesis is still imported from the manuscript architecture rather than packaged as a self-contained local theorem. That keeps the package from being cleanly reusable across families.

## Needed for promotion

1. State the positivity transport step as its own abstract lemma, with hypotheses exactly of the form `center spectral gap + baseline variation + perturbation smallness`.
2. State the whitening corollary separately: `holomorphic positive-definite same-point blocks + holomorphic mixed block => holomorphic inverse-square-root whitening`.
3. Add or cite a standalone proposition giving the baseline same-point gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`.
4. In theorem-facing formulations, name `same-point positivity/nondegeneracy for holomorphic whitening` explicitly rather than hiding it inside generic admissibility language.
5. If the package is meant to travel beyond zeta, separate the generic perturbative step from the zeta-specific holomorphy and remainder inputs.
