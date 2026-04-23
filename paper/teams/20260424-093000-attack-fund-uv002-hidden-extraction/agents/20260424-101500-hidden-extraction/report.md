## Claim

The single narrowest exact blocker for Bottleneck D is now identifiable: one needs a finite-jet factorization theorem stating that the corrected odd germ
\[
H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr)
\]
depends on a finite core only through the reduced coincidence germ of the corrected two-atom package (equivalently a slightly enlarged reduced package state built from `\widehat\Psi`). A sufficient theorem shape is:

For each odd order `2r+1`, there is a universal holomorphic functional `\mathfrak C_r` on the `(2r+1)`-jet of the reduced package germ such that
\[
c_{2r+1}(m)=\mathfrak C_r\bigl(j^{2r+1}\Psi_{\mathrm{red}}(m)\bigr).
\]

Then the first nonzero odd order and its leading coefficient are determined by the reduced package germ, and the existing extracted-jet / `\Xi_{\zeta}^{(N)}` machinery closes formally.

## Status

open

## Evidence

The extractor side is already complete: `H_m` is odd holomorphic with coefficients `c_{2r+1}(m)`, the `N`-point operator isolates the first surviving odd coefficient, and finite-core localization already reduces that coefficient and `\Xi_{\zeta,\le H}^{(N)}` to any fixed finite core. Separately, the draft has already converged on `\widehat\Psi` as the correct amplitude-invariant package datum for downstream minimal-core extraction, and repeatedly states that the remaining burden is a provenance-sensitive package theorem such as same reduced image germ at coincidence / collision-functoriality. What is still absent is exactly the bridge from that reduced package datum to the odd Taylor coefficients of `H_m`. No theorem currently identifies any `c_{2r+1}(m)` as a function of `\widehat\Psi` or of a reduced package germ.

## Exact refs

- `paper/proof_of_rh.tex:2214-2307` — definition of `H_m` and odd microscopic expansion.
- `paper/proof_of_rh.tex:2953-2969` — core localization of the extracted odd jet.
- `paper/proof_of_rh.tex:3986-4190` — `\Xi_\zeta^{(N)}` isolates the first surviving odd coefficient and is finite-core localized.
- `paper/proof_of_rh.tex:11368-11671` — definition of amplitude-invariant strengthened datum `\widehat\Psi` and exact coincidence algebra through order `7`.
- `paper/proof_of_rh.tex:12586-12610` — explicit two-stage reformulation: first extract corrected coincidence information for `\widehat\Psi`, then convert it downstream.
- `paper/proof_of_rh.tex:24985-25030` — current finite-core endgame split; live targets are package-level coincidence/functoriality.
- `paper/proof_of_rh.tex:26377-26398` — general finite-core branch must use the first nonzero odd jet, not necessarily the first odd coefficient.

## Dependencies

- A reduced-package coincidence theorem for the actual corrected two-atom package (same reduced image germ at coincidence or collision-functoriality).
- A holomorphic factorization statement from that reduced package germ to `H_m` (or directly to `c_{2r+1}` / `\Xi_{\zeta,\le H}^{(N)}`).

## Strongest objection

The draft does not yet define the reduced package germ as an input to the corrected whitening map `\widehat\Omega_\zeta^{\corr}`. So the proposed factorization theorem is sharply formulated, but not yet even partially proved from existing notation alone: there is still a genuine possibility that `H_m` retains provenance-sensitive data not captured by the present reduced `\widehat\Psi` package.

## Needed for promotion

1. State a precise reduced package germ `\Psi_{\mathrm{red}}` for the actual corrected two-atom package.
2. Prove functoriality: two finite cores with the same reduced package germ give the same odd germ `H_m` up to the corresponding jet order.
3. Deduce that the first nonzero odd coefficient, hence the first nonzero `\Xi_{\zeta,\le H}^{(N)}`, is determined by that reduced package germ.

Honest verdict: Bottleneck D has not moved to a proof, but it has sharpened to one exact missing lemma family. The blocker is no longer "package to extractor somehow"; it is the absence of a jet-factorization theorem from the reduced corrected two-atom package germ to the odd Taylor coefficients of `H_m`.
