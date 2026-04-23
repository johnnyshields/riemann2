## Claim

The candidate reduced package state

\[
\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr),
\qquad
\widehat\Psi=(Y,x,xS),
\]

with

\[
x=\frac{v_5}{c},\qquad Y=\frac{u_5}{c},\qquad S=\frac{\Delta_7}{c\,v_5}=\frac{\lambda}{c},
\]

is the sharpest current reduced secant/tangent shadow of the mixed two-point package, but on the present draft it does **not** yet determine the first surviving odd jet / first nonzero `\Xi_{\zeta,\le H}^{(N)}`. The exact missing point is a hidden-state lemma showing that the quotient from the raw projective defect state

\[
[\delta c:\delta v_5:\delta u_5:\delta\lambda]
\]

to

\[
\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)
\]

forgets only `\Phi_K`-invisible directions through the first surviving odd order.

## Status

open

## Evidence

1. The paper already identifies `\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)` as the amplitude-invariant strengthened datum and the correct algebraic bridge for two-pair coincidence; on a `v_5\neq 0` patch this is exactly `\widehat\Psi=(Y,x,xS)`.

2. The secant/tangent geometry of the lifted curve is formulated entirely in the reduced coordinates `Q_v=(Y,x,S)`. In particular the repeated-node tangent-plane package and the nonmixed quadratic-envelope factorization live on `Q_v`, and the mixed overlap reduction gives an exact projective secant shadow determined by `(x,Y,S)` alone. So `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)` is geometrically the right reduced shadow.

3. But the mixed two-point branch is first compactified at the raw projective defect level `[\delta c:\delta v_5:\delta u_5:\delta\lambda]`, not directly at `[\delta x:\delta Y:\delta S]`. Linearizing the reduced coordinates gives

\[
\delta x=\frac{\delta v_5-x\,\delta c}{c},\qquad
\delta Y=\frac{\delta u_5-Y\,\delta c}{c},\qquad
\delta S=\frac{\delta\lambda-S\,\delta c}{c}.
\]

Hence the passage from raw to reduced defects has kernel

\[
\ker L=\mathbf C\,(1,x,Y,S),
\]

equivalently the radial/raw scaling direction `\mathbf C\,(c,v_5,u_5,\lambda)`. So equal `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)` fibers can still differ by this lost raw direction.

4. The present draft does not show that this lost direction is `\Phi_K`-invisible. In fact `A_5^{\mathfrak f}=u_5I+v_5S`, `\Phi_K(X)=x_{12}+x_{21}`, and `S=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)`, so

\[
\Phi_K(A_5^{\mathfrak f})=2v_5
\]

generically. Therefore raw radial variation changes a `\Phi_K`-visible quintic component unless an additional cancellation lemma is proved.

5. This matches the draft's own obstruction picture: quotient-level and gauge-level routes are shear-blind, and the hidden extraction bottleneck is exactly to show that equal reduced-package fibers agree modulo `\Phi_K`-invisible directions through the first surviving odd order. That theorem is not yet in the paper.

6. Since the extractor side is already complete, the reduced secant/tangent candidate would become sufficient once one proves the missing hidden-state lemma: constancy of the first surviving odd jet on fibers of `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)`, or equivalently that every extra raw-fiber variation is killed by `\Phi_K` through the first surviving odd order.

## Exact refs

- `paper/proof_of_rh.tex:11368-11449` (`\widehat\Psi` and its amplitude invariance)
- `paper/proof_of_rh.tex:12586-12610` (finite-core extraction should pass through `\widehat\Psi` first)
- `paper/proof_of_rh.tex:12780-12980` (`Q_v=(Y,x,S)` lifted geometry on a `v_5`-patch)
- `paper/proof_of_rh.tex:14216-14243` (repeated-node tangent-plane package `H_4` for `Q_v`)
- `paper/proof_of_rh.tex:15712-15796` (exact factorization on `Q_v=(Y,x,S)`)
- `paper/proof_of_rh.tex:12230-12383` (shear-blind audit and raw projective defect compactness `[\delta c:\delta v_5:\delta u_5:\delta\lambda]`)
- `paper/proof_of_rh.tex:20853-21079` (projective secant shadow depends only on `(x,Y,S)`)
- `paper/proof_of_rh.tex:2214-2307` (`H_m` and odd-jet expansion)
- `paper/proof_of_rh.tex:3984-4189` (first surviving odd coefficient / `\Xi_{\zeta,\le H}^{(N)}` extractor)
- `paper/proof_of_rh.tex:408-418` and `paper/proof_of_rh.tex:23132-23135` (`\Phi_K` and the matrix `S`)
- `paper/proof_of_rh.tex:7019-7029` (`A_5^{\mathfrak f}=u_5I+v_5S`, `\Delta_7`)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:55-87`

## Dependencies

- Work on `UV-002`, especially Extraction front D.
- The amplitude-invariant strengthened datum `\widehat\Psi`.
- The overlap-patch secant/tangent reduction to `Q_v=(Y,x,S)`.
- The odd-jet / `\Xi_\zeta^{(N)}` extractor already proved on the zeta side.
- A new hidden-state / `\ker\Phi_K` theorem not yet present in the draft.

## Strongest objection

The kernel calculation above is a first-order/formal obstruction, not yet a no-go theorem. It rules out promotion of the reduced secant/tangent package from the present draft alone, but it does not prove that the candidate is false. A new theorem could still show that the lost raw radial direction is dynamically constrained or `\Phi_K`-invisible through the first surviving odd order on genuine finite-core fibers.

## Needed for promotion

1. State the raw-to-reduced quotient map from `[\delta c:\delta v_5:\delta u_5:\delta\lambda]` to `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)` inside the paper's package notation.
2. Prove a hidden-state lemma: equal reduced secant/tangent package fibers imply equality of the corrected block modulo `\ker\Phi_K` through the first surviving odd order.
3. Or prove an equivalent constancy statement: the first surviving odd jet of `H_m` is constant on fibers of `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)`.
4. Then invoke the existing `\Xi_{\zeta,\le H}^{(N)}` surviving-expansion machinery.

Honest verdict: `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)` is the best reduced geometric candidate now visible, because it captures the secant/tangent shadow of `Q_v=(Y,x,S)`. But it is not presently sufficient: the reduction from raw defects forgets a radial direction that the draft does not show to be `\Phi_K`-invisible, and that hidden-state lemma is exactly the remaining blocker.
