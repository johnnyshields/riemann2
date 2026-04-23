## Claim

The current draft does not prove the package-to-transform factorization
\[
H_{\core}=\mathfrak H(\mathcal P_{\mathrm{red}})
\]
and does not even force constancy of the first surviving odd jet on reduced-package fibers. The sharp exact blocker is a missing hidden-state lemma: if two finite cores have the same reduced package state (equivalently the same reduced `\widehat\Psi` coincidence germ / package fiber), one still needs a theorem that their corrected transverse blocks differ only by directions annihilated by `\Phi_K` up to the first surviving odd order. Nothing in the present paper identifies that kernel quotient with `\mathcal P_{\mathrm{red}}`.

## Status

open

## Evidence

`H_m` is defined from the full corrected block, not from the reduced package: `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))`. The odd-jet extractor and the `N`-point transform then act on this full scalar and isolate the first surviving odd coefficient formally once `H_m` is known. So the extractor side is complete, but only after one has already supplied the full corrected scalar.

The reduced-package side controls only the projective coincidence data. The strengthened datum `\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)` is introduced exactly as the amplitude-invariant package for multi-pair coincidence, and the two-pair theorem shows equality of `\widehat\Psi` under exact cubic/quintic/septic coincidence through order `7`. The minimal-core reduction then converts bad finite cores into affine dependence / coincidence / collinearity / coplanarity statements for these reduced coordinates. This is geometric/incidence control, not a map from the package fiber to `H_m` or to the odd Taylor coefficients of `H_m`.

The paper explicitly says the remaining order-`7` burden is provenance-sensitive and not merely quotient-septic. In particular, cubic/quintic merger does not yet force the odd-reparametrization comparability needed to identify the honest order-`7` package, and no theorem from arbitrary quotient-septic geometry alone can close the branch. This is exactly the obstruction to fiber constancy: equal reduced package leaves hidden provenance/reparametrization freedom, and `H_m` is currently sensitive to the full corrected block carrying that hidden freedom.

Therefore the strongest theorem presently visible is conditional: package-to-transform factorization would follow from an additional statement of the form
\[
\mathcal P_{\mathrm{red}}(\core_1)=\mathcal P_{\mathrm{red}}(\core_2)
\Longrightarrow
\Phi_K\bigl(\widehat\Omega^{\corr}_{\core_1}-\widehat\Omega^{\corr}_{\core_2}\bigr)
=O\bigl(s^{2N+1}\bigr)
\]
for the first surviving odd order `2N-1` (or identically in `s` for full factorization). No result in the current draft supplies this implication.

## Exact refs

- `paper/proof_of_rh.tex:2214-2321` (`H_m` defined from `\widehat\Omega_\zeta^{\corr}` and odd expansion)
- `paper/proof_of_rh.tex:2953-2969` (finite-core localization of the extracted odd coefficient)
- `paper/proof_of_rh.tex:3853-4037` (`\Xi_\zeta^{(N)}` and exact first-surviving-jet extraction from `H_m`)
- `paper/proof_of_rh.tex:4039-4088` (finite-core localization of `\Xi_{\zeta,\le H}^{(N)}`)
- `paper/proof_of_rh.tex:10780-10843` (honest order-`7` target is package/provenance-sensitive; quotient-septic geometry alone is insufficient)
- `paper/proof_of_rh.tex:11368-11585` (`\widehat\Psi` definition, scaling law, and exact two-pair coincidence)
- `paper/proof_of_rh.tex:12586-12609` (finite-core program framed as first extracting `\widehat\Psi` coincidence, then converting to affine incidence constraints)
- `paper/proof_of_rh.tex:12669-12979` (minimal bad core reduction to affine dependence / coincidence / collinearity / coplanarity of reduced-package coordinates)
- `paper/proof_of_rh.tex:21293-21329` (remaining burden is nonlocal transport / collision-functoriality / provenance-sensitive two-atom structure)
- `paper/proof_of_rh.tex:24985-25030` (current live targets stop at edge-law, quotient transport, and package-level coincidence)
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:51-61`

## Dependencies

- A proved reduced-`\widehat\Psi` coincidence / collision-functoriality theorem on the actual corrected two-atom package.
- A new hidden-state lemma identifying equal reduced-package fibers with equality of the corrected transverse scalar modulo `\ker \Phi_K` to the relevant odd order.
- For full factorization, a stronger statement that the entire corrected scalar germ is determined by the reduced package, not just its first surviving odd jet.

## Strongest objection

This obstruction is theorem-level but not a formal impossibility proof. It shows only that the present draft does not contain enough structure to deduce fiber constancy from reduced-package coincidence alone. A new package theorem could still close it if it upgrades reduced coincidence into an actual corrected-block equivalence modulo `\Phi_K`-invisible directions.

## Needed for promotion

1. State the reduced package `\mathcal P_{\mathrm{red}}` for the actual corrected finite core precisely enough that equality on fibers is meaningful beyond pair-level/projective data.
2. Prove a hidden-state / kernel theorem: equal reduced package implies equality of the corrected transverse scalar to the first surviving odd order, or of the full scalar germ.
3. Then the existing `H_m` odd expansion and `\Xi_\zeta^{(N)}` machinery promote immediately to first-surviving-jet constancy, and in the stronger form to `H_{\core}=\mathfrak H(\mathcal P_{\mathrm{red}})`.

Honest verdict: I did not prove package-to-transform factorization. I reduced the blocker to one exact missing theorem: reduced-package coincidence must control the full corrected block modulo `\Phi_K`-invisible directions. Without that, neither full factorization nor first surviving odd-jet constancy is formal from the current draft.
