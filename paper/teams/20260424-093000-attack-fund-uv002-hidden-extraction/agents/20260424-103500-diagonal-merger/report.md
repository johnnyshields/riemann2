## Claim

The diagonal merger law
\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h
\]
for the actual corrected two-atom package is not proved by the present draft, and it is sharply obstructed from the only explicit naive source-summed corrected-block model currently on the page. Consequently the equivalent diagonal coincidence input
\[
E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0
\]
on the residual exact fixed-shear involutive branch remains the single exact missing package theorem. Any proof now has to come from a different lift/transport object or from an independent package-level coincidence/functoriality theorem, not from the raw source-summed whitened coefficients.

## Status

proved

## Evidence

- Lemma `minimal-source-level-two-point-criterion` isolates the exact needed identity: swap symmetry, one-amplitude collapse, and diagonal merger are sufficient, and once they hold the quadratic factorization is formal.
- The residual exact fixed-shear closure theorem later needs only swap-evenness plus diagonal vanishing at coincidence: `E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0` on the involutive branch. So the diagonal merger law is stronger than necessary, but it is exactly one clean sufficient route.
- The draft also proves that the obvious weighted one-atom/source-summed corrected-block route cannot yield that merger law. Along a weighted one-atom datum `q_{a,h}=a q_h`, the corrected whitened block coefficients are even analytic in the source weight `a`; therefore they cannot realize analytic one-atom linearity `\mathfrak P_2(a\delta_h)=aF_h`, hence cannot produce the diagonal law `(a_1+a_2)F_h` except in the trivial vanishing case.
- The endgame-status remarks repeat the same obstruction: the current residual burden is package-level coincidence/functoriality, not transport classification, and the naive source-summed model cannot supply the required linear merger law.
- Therefore the exact blocker is sharp: the present paper reduces UV-002 locally to proving either diagonal merger for the actual corrected package or the weaker equivalent diagonal coincidence statement behind `E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0`; existing quotient-visible transport descent does not furnish that vanishing by itself.

## Exact refs

- `paper/proof_of_rh.tex:11888-11932` — lemma isolating diagonal merger as sufficient for quadratic factorization.
- `paper/proof_of_rh.tex:12168-12228` — exact remaining source-level input and the even-amplitude obstruction for the naive source-summed model.
- `paper/proof_of_rh.tex:22409-22505` — conditional exact fixed-shear closure from state-locality and the stronger merger law.
- `paper/proof_of_rh.tex:22966-23096` — residual involutive defect criterion and package-level reduction to swap invariance plus vanishing on coincident atoms.
- `paper/proof_of_rh.tex:24518-24530` and `paper/proof_of_rh.tex:24987-25004` — live attack routes and explicit statement that the naive source-summed corrected-block model cannot provide the linear merger law.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:24-33` — current formulation of the blocker as diagonal merger / diagonal value-zero.

## Dependencies

- Analytic definition of the actual corrected two-atom package on the collision/cancellation or exact fixed-shear quotient-diagonal lane.
- A theorem proving package-level coincidence/functoriality at coincidence, e.g. same reduced `\widehat\Psi` image germ or collision-functoriality.
- Alternatively, a new lift/transport object whose one-atom extraction is genuinely linear in amplitude, unlike the naive source-summed whitened coefficients.

## Strongest objection

This report proves only a negative result about the current explicit model. It does not rule out the possibility that the actual corrected package, defined by a different provenance-sensitive construction, satisfies diagonal merger or at least diagonal coincidence. So the obstruction is sharp only relative to the package objects currently made explicit in the draft.

## Needed for promotion

1. Construct the actual corrected two-atom package on the live residual lane by an object not subject to the even-amplitude obstruction.
2. Prove either the full diagonal merger law or the weaker exact diagonal coincidence statement implying `E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0`.
3. Then apply `paper/proof_of_rh.tex:22966-23096` (or the stronger state-local package collapse route) to remove the residual exact fixed-shear corner.

Honest verdict: the diagonal merger law is not presently proved, and from the current naive source-summed corrected-block formulas it cannot be proved. The live missing theorem is exactly package-level diagonal coincidence for the actual corrected two-atom package.
