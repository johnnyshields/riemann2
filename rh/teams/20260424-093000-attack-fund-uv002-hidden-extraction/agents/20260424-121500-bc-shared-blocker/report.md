## Claim

Bottlenecks B and C do not yet collapse to exactly the same missing theorem. They still differ by one extra scalar-level condition: C only needs reduced diagonal-collapse to the one-pair reduced package `\widehat\Psi(m)` (equivalently coincidence modulo overall scalar), while B needs the stronger raw diagonal merger / diagonal vanishing of the actual corrected cubic and quintic defects.

## Status

proved

## Evidence

The raw two-atom merger criterion is explicit: Lemma `minimal-source-level-two-point-criterion` requires the diagonal law
`\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h`, and `rem:wip-source-level-reduction-two-point-branch` says this is exactly the remaining source-level merger input. On the exact fixed-shear corner, Proposition `conditional-state-local-defect-closure-fixed-shear-corner` only needs the cubic/quintic defects to vanish at the diagonal transport state, and the stronger package corollary again uses the raw merger law.

By contrast, the strengthened-coincidence identities show that equality of reduced data is weaker than defect vanishing. At coincidence `h_1=h_2=m`, the first two reduced-coordinate differences are
`(u_5 e-c e_u)/c^2` and `(v_5 e-c e_v)/c^2`; setting them to zero forces only `E=(e/c)A_5^{\mathfrak f}`, not `e=0` and `E=0`. So reduced-package coincidence allows a diagonal scalar rescaling that B does not allow. This matches the current Bottleneck C phrasing: the corrected reduced package may collapse to a `\kappa`-independent value equal to `\widehat\Psi(m)` without proving the raw linear merger needed for B.

## Exact refs

- `paper/proof_of_rh.tex:11888-11930`
- `paper/proof_of_rh.tex:12168-12189`
- `paper/proof_of_rh.tex:12447-12469`
- `paper/proof_of_rh.tex:22409-22505`
- `paper/proof_of_rh.tex:11650-11669`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:24-33`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:45-54`

## Dependencies

- The draft's reduced package is the amplitude-invariant datum `\widehat\Psi` and its corrected two-atom analogue.
- The comparison uses the existing strengthened-coincidence algebra, not any new computation.

## Strongest objection

The present paper does not yet define the corrected reduced two-atom package in one fully canonical displayed formula, so part of the argument uses the existing `\widehat\Psi` defect identities as the proxy for what reduced coincidence means. If the intended Bottleneck C package secretly retains an extra normalization fixing the overall scalar, then the gap between B and C would disappear. Nothing in the cited slices indicates that stronger normalization is already built in.

## Needed for promotion

State the distinction explicitly in the team collation: B requires raw diagonal merger / defect-zero on the diagonal, while C requires only reduced diagonal-collapse to `\widehat\Psi(m)`. If the coordinator wants them unified, the missing extra theorem is precisely a scalar-normalization law upgrading reduced coincidence to raw merger.

Honest verdict: B and C still differ by one extra condition. C is reduced coincidence modulo scalar; B additionally needs the scalar fixed so that the actual corrected cubic/quintic defects vanish on the diagonal.
