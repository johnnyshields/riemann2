## Claim

The smallest standalone same-point positivity package actually used by the manuscript in the holomorphic-whitening step is:

1. a holomorphic same-point block family `G_{m,\pm}^{\corr}(s)` on `|s|<\rho_0/Q`;
2. a baseline same-point family `G_{m,\pm}^{(0)}(s)` with a same-point spectral gap at `s=0`, namely `\lambda_{\min}(G_{m,\pm}^{(0)}(0)) \gg Q`;
3. a microscopic variation bound `\sup_{|s|<\rho_0/Q}\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\| \ll \rho_0 Q`;
4. a perturbation bound `\sup_{|s|<\rho_0/Q}\|G_{m,\pm}^{\corr}(s)-G_{m,\pm}^{(0)}(s)\| = o(Q)`;
5. a holomorphic functional-calculus step saying that a holomorphic matrix family staying inside the positive-definite cone admits holomorphic inverse square roots.

From these five ingredients the draft obtains uniform positivity/nondegeneracy of the same-point blocks on the microscopic disk, hence holomorphic whitening and then the analytic expansion of the whitening map used in the corrected local deformation decomposition.

Generic versus zeta-specific split:

- Generic core: items 3-5 above, plus the perturbative implication
  `spectral gap at one point + small baseline variation + small perturbation => uniform positivity on a neighborhood`, and then `uniform positivity + holomorphy => holomorphic inverse square root => holomorphic whitening map`.
- Zeta-specific input: the explicit form of the same-point blocks in terms of `q,q',q''`; the denominator-comparability theorem used to continue omitted-zero sums holomorphically; the tail-curvature / remainder estimate `S_2=o(Q)`; and the baseline jet-limit spectral-gap statement `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` for the admissible midpoint class.

Three-bin verdict:

- proved in the manuscript: the perturbative transport from baseline gap to diskwise positivity, assuming the cited baseline gap and holomorphy inputs;
- conditional on upstream zeta lemmas: the standalone lemma package as an actual theorem usable across families, because the paper imports rather than proves the baseline spectral gap and the omitted-sum holomorphy package here;
- missing for a clean cross-family package: an abstract standalone lemma that isolates the generic perturbative/functional-calculus argument from the zeta-specific formulas, plus an explicit hypothesis line naming same-point positivity/nondegeneracy instead of leaving it hidden inside corrected-whitening admissibility.

## Status

conditional

## Evidence

The key positivity proof is Proposition `Corrected finite-s holomorphic whitening`. Its proof is structurally short and modular. It first gets holomorphy of the corrected same-point and mixed blocks from denominator comparability and the removable-singularity argument at `s=0`. It then compares `G_{m,\pm}^{\corr}(s)` to the single reference matrix `G_{m,\pm}^{(0)}(0)` by splitting

`G_{m,\pm}^{\corr}(s)-G_{m,\pm}^{(0)}(0) = (G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)) + R_{m,\pm}(s)`.

The manuscript bounds the first term by `\ll \rho_0 Q` (baseline variation) and the second by `o(Q)` (block perturbation plus tail curvature). Since the reference matrix has spectral gap `\gg Q`, choosing `\rho_0` small gives a uniform lower eigenvalue bound on the whole disk. That is the entire same-point positivity mechanism.

The later corrected local deformation proposition uses exactly this output and nothing more sophisticated: it defines the whitening map `\mathcal W(G_-,N,G_+) = G_-^{-1/2} N G_+^{-1/2}` and invokes the corrected finite-`s` whitening theorem to justify analyticity on the open set where `G_\pm` stay uniformly positive definite. So the positivity package needed downstream is just enough to make `G_\pm^{-1/2}` holomorphic and the whitening map differentiable/analytic in the value-channel parameter.

This matches the team notes. `paired_slot_hypotheses.md` and `corrected_whitening_transport.md` both isolate the safe bundle as: denominator/holomorphy input, same-point positivity/nondegeneracy, and holomorphic whitening. They also warn that same-point positivity should be named explicitly rather than buried under a generic admissibility phrase. `denominator_theorem.md` separately states that denominator comparability is only a support theorem for omitted-sum holomorphy and corrected-whitening admissibility, not the full positivity theorem by itself.

So the manuscript appears to use a two-layer package:

1. zeta-side admissibility inputs establishing holomorphy, baseline gap, and small perturbation;
2. a generic perturbative whitening lemma converting those inputs into holomorphic same-point inverse square roots and hence a holomorphic whitening map.

What is not yet cleanly packaged is the second layer as an abstract lemma/theorem with hypotheses stated independently of the zeta formulas.

## Exact refs

- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`): holomorphy, positivity, inverse square roots, whitening holomorphy.
- `paper/proof_of_rh.tex:1418-1424`: zeta-specific holomorphy input from `prop:denominator-comparability` and removable poles.
- `paper/proof_of_rh.tex:1426-1455`: exact perturbative positivity argument.
- `paper/proof_of_rh.tex:857-946` (`prop:denominator-comparability`): omitted-zero denominator comparability and holomorphic extension of `g_{\sm}` and derivatives.
- `paper/proof_of_rh.tex:948-1143` (`prop:block-perturbation`): `\|R_{m,\pm}(s)\| \ll S_2`, hence with tail curvature `o(Q)`.
- `paper/proof_of_rh.tex:1333-1390` (`lem:baseline-variation`): `\sup\|G_{m,\pm}^{(0)}(s)-G_{m,\pm}^{(0)}(0)\| \ll \rho_0 Q`.
- `paper/proof_of_rh.tex:1531-1621`: downstream use of positivity in the analytic whitening map and value-channel expansion.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-52,61-70`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-27`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`.

## Dependencies

- Upstream zeta holomorphy input from `prop:denominator-comparability`.
- Upstream size control from `prop:block-perturbation` plus the tail-curvature theorem (`S_2=o(Q)` as invoked at `paper/proof_of_rh.tex:1426-1429`).
- Upstream baseline local-model derivative scales used in `lem:baseline-variation`.
- An upstream same-point baseline spectral-gap statement at `s=0` for `G_{m,\pm}^{(0)}(0)` on the admissible midpoint class; this is used at `paper/proof_of_rh.tex:1436-1439` but not isolated here as its own lemma.
- Standard holomorphic functional calculus for matrix square roots on the positive-definite cone.

## Strongest objection

The decisive weak point is that the manuscript does not currently expose the baseline same-point spectral gap as a standalone abstract hypothesis/lemma inside this package. The proof at `paper/proof_of_rh.tex:1436-1439` simply states the gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q` for the baseline jet-limit block, and the downstream proposition at `paper/proof_of_rh.tex:1573-1574` treats positivity as already established. So the generic package is visible in the proof pattern, but not yet cleanly theoremized on its own. Without naming that baseline gap and the positivity/nondegeneracy hypothesis explicitly, the package remains manuscript-internal rather than a ready cross-family lemma.

## Needed for promotion

To promote this to a clean standalone lemma package candidate, the draft would need:

1. an abstract lemma of the form `baseline gap at one point + baseline variation + perturbation smallness => uniform positive definiteness on the microscopic disk`;
2. a companion abstract lemma `holomorphic positive-definite matrix family => holomorphic inverse square root`, phrased so whitening analyticity is immediate;
3. an explicit zeta-specific proposition supplying the baseline gap `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`;
4. theorem-facing wording that names `same-point positivity/nondegeneracy for holomorphic whitening` as its own hypothesis line, exactly as suggested in the team notes;
5. if cross-family use is intended, a statement separating the generic perturbative core from the zeta formulas for `q,q',q''` and the omitted-zero denominator theorem.
