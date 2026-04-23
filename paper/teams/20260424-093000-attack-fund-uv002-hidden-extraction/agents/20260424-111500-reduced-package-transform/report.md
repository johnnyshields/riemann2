## Claim

The reduced secant/tangent package of the lifted curve
\[
Q_v=(Y,x,S),
\qquad x=\frac{v_5}{c},\ Y=\frac{u_5}{c},\ S=\frac{\Delta_7}{c\,v_5},
\]
is the sharpest draft-native reduced state now visible for Bottleneck D, but the present draft does **not** prove the target theorem that the first surviving odd jet of
\[
H_m(s)=\Phi_K\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr)
\]
or equivalently the first nonzero finite-core scalar \(\Xi_{\zeta,\le H}^{(N)}\) is constant on its fibers. The strongest supportable positive statement is conditional: this constancy would follow if equal reduced secant/tangent fibers forced agreement of the corrected block modulo \(\ker\Phi_K\) through the first surviving odd order.

## Status

open

## Evidence

- The extractor side is already complete. The draft defines the odd holomorphic scalar \(H_m\), proves its odd Taylor expansion, proves core localization of the first surviving odd coefficient, and proves that the \(N\)-point transform isolates the first surviving odd coefficient and hence the first nonzero \(\Xi_{\zeta,\le H}^{(N)}\).
- The reduced secant/tangent package is genuinely draft-native. On good overlap patches the paper introduces
  \(x=v_5/c\), \(Y=u_5/c\), \(S=\Delta_7/(c v_5)\), the lifted space curve \(Q_v=(Y,x,S)\), the exact projective secant shadow, and the tangent-plane contact interpretation of the mixed four-point geometry.
- What this package controls is secant/tangent geometry of \(Q_v\) and the projectivized \(\lambda\)-shear shadow. Nothing in the cited Bottleneck D slices identifies the corrected local block, or its first \(\Phi_K\)-visible odd jet, as a function of that reduced package state.
- The current convergence files sharpen the missing step exactly this way: the obstacle is a hidden-state lemma saying that equal reduced-package fibers force corrected-block agreement modulo \(\Phi_K\)-invisible directions through the first surviving odd order. Without that lemma, fiberwise constancy of the first surviving odd jet is not formal from the present text.

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` — definition and odd expansion of `H_m`.
- `paper/proof_of_rh.tex:2953-2969` — finite-core localization of the first surviving odd coefficient.
- `paper/proof_of_rh.tex:3984-4190` — exact surviving expansion and finite-core localization of `\Xi_\zeta^{(N)}`.
- `paper/proof_of_rh.tex:14216-14242` — tangent-contact determinants on a `v_5`-patch with `(Y,x,S)` and `Q_v` tangent-plane meaning.
- `paper/proof_of_rh.tex:15712-15737` — explicit use of `Q_v(h)=(Y(h),x(h),S(h))` on a nonmixed interval.
- `paper/proof_of_rh.tex:20853-20939` — exact projective secant-shadow reduction with `x,Y,S` and shear-independence.
- `paper/proof_of_rh.tex:24425-24428` — repeated-node limits become tangent-plane contacts for `Q_v=(Y,x,S)`.
- `paper/proof_of_rh.tex:24985-25030` — current endgame compression to local blow-up regularity, quotient transport, and package-level coincidence.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:53-87` — current exact Bottleneck D blocker and reduced secant/tangent package candidate.

## Dependencies

- A hidden-state theorem: equal fibers of the reduced secant/tangent package imply corrected-block agreement modulo `\ker\Phi_K` through odd order `2N-1`, where `2N-1` is the first surviving odd order.
- Or a stronger package theorem identifying the corrected block itself as a function of the reduced secant/tangent package.
- Package-side coincidence/functoriality for the actual corrected two-atom package on the live residual lane.

## Strongest objection

The reduced secant/tangent package is built from quotient/projective data of `Q_v=(Y,x,S)` and from the secant-shadow reduction, so it controls geometric contact data rather than the full corrected two-atom block seen by `\Phi_K`. The present draft gives no theorem excluding additional fiberwise variation in the corrected block that is invisible to the secant/tangent package but still changes the first `\Phi_K`-visible odd jet.

## Needed for promotion

1. Prove that equal reduced secant/tangent fibers force equality of the corrected odd germ modulo `\ker\Phi_K` through the first surviving odd order.
2. Deduce from that hidden-state lemma that the first surviving odd jet of `H_m` is fiber-constant on reduced secant/tangent fibers.
3. Invoke `paper/proof_of_rh.tex:3984-4190` to conclude constancy of the first nonzero `\Xi_{\zeta,\le H}^{(N)}` on those fibers.

Honest verdict: I do not see a proof of the requested theorem candidate in the present draft. The reduced secant/tangent package `Q_v=(Y,x,S)` is the right sharp candidate state for Bottleneck D, but the exact missing step is still the hidden-state lemma from equal reduced-package fibers to corrected-block equality modulo `\ker\Phi_K` through the first surviving odd order.
