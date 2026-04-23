## Claim

The single narrowest exact blocker for Bottleneck D is now precise: prove a factorization / jet-detection theorem saying that, on the live finite-core collision package, the odd scalar germ

\[
H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr)
\]

depends on the package only through the reduced coincidence germ of the amplitude-invariant package datum `\widehat\Psi` (or an equivalent reduced package state), strongly enough that the first nonzero odd jet of `H_m` is determined by the first nonzero odd jet of that reduced package germ. Without exactly this bridge, same reduced image germ / collision-functoriality on the package side does not yet identify either the order or the leading coefficient of the first surviving odd term of `H_m`.

## Status

open

## Evidence

- The extractor side is already complete: `H_m` is an odd holomorphic germ with coefficients `c_{2r+1}(m)`, and the `N`-point transform isolates the first surviving odd coefficient exactly and localizes it to any fixed finite core.
- The current finite-core remarks already state that the endgame must be reformulated in terms of the first nonzero odd jet of the corrected transverse scalar, not the first odd jet specifically.
- The package side has been reduced to a provenance-sensitive coincidence theorem for the strengthened datum `\widehat\Psi`, and the paper explicitly says the finite-core endgame is a two-stage problem: first extract defect-corrected coincidence information for `\widehat\Psi`, then convert that information downstream.
- But the draft also says quotient-septic data remain locally free after quotient closure; therefore package coincidence at the quotient-visible level alone cannot determine the odd scalar germ unless one proves an additional theorem linking `H_m` to the reduced package germ.
- So Bottleneck D is not “find the odd-jet extractor” but “prove that the corrected scalar germ seen by `\Phi_K` factors through the reduced collision package in a way that preserves the first nonzero odd jet.”

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` — definition of `H_m` and its odd Taylor coefficients `c_{2r+1}(m)`.
- `paper/proof_of_rh.tex:2953-2969` — fixed-finite-core localization of the extracted odd jet.
- `paper/proof_of_rh.tex:3978-4036` — exact surviving expansion for `\Xi_\zeta^{(N)}`; the leading term is the first surviving odd coefficient.
- `paper/proof_of_rh.tex:4039-4190` — finite-core localization of `\Xi_{\zeta,\le H}^{(N)}`.
- `paper/proof_of_rh.tex:5604-5643` — finite-core branch requires the first nonzero odd jet, not specifically the first odd jet.
- `paper/proof_of_rh.tex:10794-10843` — quotient-septic closure is not enough; the remaining issue is provenance-sensitive package data, and `\Delta_7` remains locally free.
- `paper/proof_of_rh.tex:11368-11584` — definition of the amplitude-invariant strengthened package datum `\widehat\Psi` and exact strengthened coincidence.
- `paper/proof_of_rh.tex:12586-12610` — explicit two-stage formulation: first extract corrected coincidence information for `\widehat\Psi`, then convert it downstream.
- `paper/proof_of_rh.tex:24985-25030` — current finite-core stack places package-level coincidence before the hidden extraction step.
- `paper/proof_of_rh.tex:26369-26398` — current endgame status: general finite-core branch still open.

## Dependencies

- A proved package-level coincidence / same reduced image germ theorem on the actual corrected two-atom package.
- A reduced-state theorem identifying the corrected scalar germ `H_m` as a function of that reduced package germ (or of an equivalent reduced collision functor).
- Mixed `4`-point source-level factorization remains downstream for the full finite-core contradiction, but it is not the narrow blocker isolated here.

## Strongest objection

This reduction still stops short of a theorem because the paper does not yet exhibit the candidate reduced scalar functional explicitly. It is possible that `H_m` depends on hidden provenance data more finely than `\widehat\Psi` alone, in which case the correct blocker would be a factorization through a larger reduced package state rather than through `\widehat\Psi` itself.

## Needed for promotion

1. State the exact reduced package state on the collision/cancellation locus that survives coincidence.
2. Prove that `H_m(s)` factors through that reduced state to the order needed for odd-jet detection.
3. Deduce that equality of reduced package germs forces equality of the first nonzero odd order and of its leading coefficient for `H_m`.
4. Feed that coefficient into the already-proved exact surviving expansion / finite-core localization for `\Xi_\zeta^{(N)}`.

Honest verdict: Bottleneck D has been reduced to one exact missing bridge. The missing statement is not an extractor identity on the zeta side; it is a factorization theorem from reduced package coincidence data to the first nonzero odd jet of `H_m`. Without that theorem, package coincidence remains too weak to determine the hidden odd coefficient.
