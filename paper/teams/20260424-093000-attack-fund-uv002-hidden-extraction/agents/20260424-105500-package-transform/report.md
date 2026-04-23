## Claim

The cleanest exact package-to-transform theorem the current notation supports is the following.

**Proposed theorem (package-to-transform factorization modulo `\ker\Phi_K`).**
Fix `0<\alpha<\rho_0`, let `N=\lfloor \alpha Q\rfloor`, and fix `H>\alpha`. Let
\[
H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr),
\qquad
\Xi_{\zeta,\le H}^{(N)}(m)
=
\Xi_\zeta^{(N)}(m)-\Xi_{\zeta,\out}^{(N)}(m;H).
\]
Assume that the actual corrected finite-core package on depth `\le H` admits a reduced coincidence state `\mathcal C_{\le H}(m)` extending the reduced `\widehat\Psi` data, with the property that whenever two finite cores `m,\widetilde m` satisfy
\[
\mathcal C_{\le H}(m)=\mathcal C_{\le H}(\widetilde m),
\]
their finite-core corrected whitened blocks agree modulo `\Phi_K`-invisible odd jets through order `2N-1`, i.e.
\[
\Phi_K\!\left(
\partial_s^{2r+1}
\bigl(
\widehat\Omega_{\zeta,\le H}^{\corr}(s;m)
-
\widehat\Omega_{\zeta,\le H}^{\corr}(s;\widetilde m)
\bigr)\Big|_{s=0}
\right)=0
\qquad (0\le r\le N-1).
\]
Then the first `N` odd coefficients of the finite-core transverse scalar are constant on reduced-package fibers:
\[
c_{2r+1,\le H}(m)=c_{2r+1,\le H}(\widetilde m)
\qquad (0\le r\le N-1),
\]
and hence the transformed finite-core scalars are fiber-invariant:
\[
\Xi_{\zeta,\le H}^{(k)}(m)=\Xi_{\zeta,\le H}^{(k)}(\widetilde m)
\qquad (1\le k\le N).
\]
In particular, if `2N-1` is the first odd order at which the finite-core scalar does not vanish, then both the first surviving odd coefficient and the first nonzero transformed scalar are determined by the reduced package state:
\[
c_{2N-1,\le H}(m)=\mathfrak c_{2N-1}\bigl(\mathcal C_{\le H}(m)\bigr),
\qquad
\Xi_{\zeta,\le H}^{(N)}(m)=\mathfrak X_N\bigl(\mathcal C_{\le H}(m)\bigr).
\]

This is the exact theorem shape that incorporates the hidden-state issue correctly: equal reduced `\widehat\Psi` fibers alone are not yet enough; what is needed is equality modulo `\ker\Phi_K` through the first surviving odd order, or an enlarged reduced package state that absorbs those invisible directions.

## Status

heuristic

## Evidence

- `H_m` is already defined as the `\Phi_K`-projection of the corrected whitened block, so only `\Phi_K`-visible odd jets can affect the odd coefficients or the `N`-point transform.
- The zeta-side extractor is already exact: once the odd coefficients are fixed, `\Xi_\zeta^{(N)}` and `\Xi_{\zeta,\le H}^{(N)}` are fixed by the surviving-expansion and finite-core localization formulas.
- The finite-core reformulation already says the downstream problem is two-stage: first extract defect-corrected coincidence information for `\widehat\Psi`, then convert it into the affine/transformed constraint.
- The current two-point/package remarks already identify reduced-image-germ / collision-functoriality as the honest theorem target, while the latest team collation sharpens the remaining obstacle to `\Phi_K`-invisible directions.
- Because `\Phi_K(X)=x_{12}+x_{21}`, its kernel consists exactly of the diagonal/value modes together with the antisymmetric off-diagonal shear mode. Those are precisely the hidden directions that can vary without changing `H_m` unless one proves control only up to the first surviving odd order.

## Exact refs

- `paper/proof_of_rh.tex:406-423` — definition of `\Phi_K`.
- `paper/proof_of_rh.tex:567-598` — value channel is `\Phi_K`-invisible.
- `paper/proof_of_rh.tex:2214-2307` — definition of `H_m` and odd expansion coefficients `c_{2r+1}(m)`.
- `paper/proof_of_rh.tex:3853-4190` — exact `N`-point transform, surviving expansion, and finite-core localization for `\Xi_\zeta^{(N)}` / `\Xi_{\zeta,\le H}^{(N)}`.
- `paper/proof_of_rh.tex:10796-10809` — same reduced image germ / collision-functoriality as the honest package theorem target.
- `paper/proof_of_rh.tex:12586-12610` — minimal-core reformulation via `\widehat\Psi`.
- `paper/proof_of_rh.tex:12168-12228` — exact source-level package criterion and failure of the naive source-summed route.
- `paper/proof_of_rh.tex:24985-25030` — current three-layer finite-core endgame compression.
- `paper/proof_of_rh.tex:26370-26398` — first nonzero odd jet is the correct general finite-core endgame datum.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-70` — Bottleneck D sharpened to the `\Phi_K`-invisible-direction issue.

## Dependencies

- A precise definition of the finite-core corrected package state `\mathcal C_{\le H}` on the actual corrected two-atom package.
- A package theorem from Bottleneck C: same reduced image germ / collision-functoriality, or a slightly enlarged reduced package state.
- A hidden-state lemma proving that residual package variation lies in `\ker\Phi_K` through the first surviving odd order.

## Strongest objection

The theorem is exact only after introducing the hypothesis that equal reduced-package fibers force agreement modulo `\Phi_K`-invisible odd jets through order `2N-1`. The present draft does not yet supply that hidden-state lemma, and it also does not yet define a canonical reduced package state `\mathcal C_{\le H}` beyond the heuristic role played by reduced `\widehat\Psi`. So this is the right theorem shape, but not yet a theorem already latent in the paper word-for-word.

## Needed for promotion

1. Define the actual reduced finite-core package state at depth `\le H` in paper notation.
2. Prove Bottleneck C in a form that either identifies equal reduced-package fibers or enlarges the package state canonically.
3. Prove the hidden-state lemma: package variation inside a reduced fiber is `\Phi_K`-invisible through the first surviving odd order.
4. Then the exact surviving-expansion and finite-core localization machinery promote the statement immediately to `\Xi_{\zeta,\le H}^{(N)}` and `c_{2N-1,\le H}`.

Honest verdict: the strongest supportable theorem statement is not `H_{\core}=\mathfrak H(\widehat\Psi_{\mathrm{red}})` outright. It is fiber-invariance of the first surviving odd jet and of `\Xi_{\zeta,\le H}^{(N)}` on reduced-package fibers modulo `\ker\Phi_K`, with the diagonal/value and antisymmetric shear directions named as the exact hidden obstruction.
