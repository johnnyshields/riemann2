## Claim

The cleanest exact boundary theorem currently used for the odd transverse scalar is Proposition `boundary-estimate` in `paper/proof_of_rh.tex:2223-2292`: on `|s|=\rho_0/Q`,
\[
|H_m(s)|\ll_{\rho_0} \frac{L(m)S(m)^2}{Q^3}.
\]
The theorem chain used in the manuscript is: corrected local decomposition `1497-1622` + cutoff compatibility `1624-1683` + value-channel annihilation `567-589` + whitened mixed-block transfer `1693-1754` + tail curvature input `361-396` + corrected-whitening holomorphy `1392-1458`, with Proposition `odd-expansion` `2294-2322` then taking this boundary bound as its Cauchy input.

## Status

proved

## Evidence

Proved in the current draft:

- Proposition `boundary-estimate` `2223-2292` is the exact boundary theorem actually invoked for the odd transverse scalar `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))` defined at `2214-2217`.
- Its proof explicitly uses Proposition `corrected-local-decomposition` `1497-1622` to write
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
  \]
  with the non-leading part already internal to the full corrected scalar `H_{m,R}`.
- Corollary `PhiK-Aval-zero` `567-589` kills the leading value channel after applying `\Phi_K`, so the boundary stage only needs control of the internal non-leading corrected part.
- Proposition `cutoff-compatibility` `1624-1683` is then used exactly to say that auxiliary near terms, tail terms, jet-correction terms, and estimation terms stay internal to the full corrected scalar, so no external boundary remainder is carried separately.
- Proposition `whitened-mixed-transfer` `1693-1754` supplies the quantitative boundary-scale estimate
  \[
  \Phi_K\bigl(\widehat\Omega_\zeta^{\corr,R}-\widehat\Omega_\zeta^{(0),R}\bigr)\ll S_2/Q^3.
  \]
- The proof at `2275-2285` then inserts the curvature input `S_2\ll L(m)S(m)^2` on the microscopic boundary, citing the tail-curvature theorem `361-396` together with the corrected transfer bounds, and concludes
  \[
  |H_{m,R}(s)|\ll L(m)S(m)^2/Q^3.
  \]
- Proposition `odd-expansion` `2294-2322` uses only two ingredients downstream: oddness/holomorphy and Cauchy on this boundary estimate.

Conditional on [transport to another family]:

- The smallest boundary theorem target is not the whole coefficient-level shell analysis in `2415-2910`. The minimal target is a family-specific corrected transverse realization-and-boundary theorem with the same logical shape as `2223-2292`:
  1. define a corrected odd holomorphic transverse scalar on `|s|<\rho_0/Q`;
  2. identify a leading value channel annihilated by the transverse functional;
  3. prove a corrected-to-baseline transverse transfer bound of size `\ll S_2/Q^3` on the microscopic boundary;
  4. prove the family-specific curvature/tail estimate that converts `S_2` into the desired boundary majorant.
- The note `corrected_whitening_transport.md:8-22` matches this split: corrected-whitening transport is only a partial bundle, while boundary control for the odd scalar remains separate.
- The note `odd_package_transport.md:28-38` states the same bottleneck in transport language: the minimal extra theorem is realized odd scalar + whitening control + the boundary estimate on `|s|=\rho_0/Q`.

Missing:

- No family-independent theorem in the current material transports the actual boundary estimate automatically from corrected whitening alone.
- The coefficient-level propositions in `2415-2910` control one-pair and exterior odd coefficients after a realized odd scalar is already in hand; they do not replace Proposition `boundary-estimate` as the first boundary theorem.
- For transport, the missing piece is therefore the family-specific theorem that realizes the odd scalar and proves its boundary bound with the manuscript's `Q^{-3}` transverse scale.

## Exact refs

- `paper/proof_of_rh.tex:361-396` (`thm:tail-curvature`)
- `paper/proof_of_rh.tex:567-589` (`cor:PhiK-Aval-zero`)
- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)
- `paper/proof_of_rh.tex:1497-1622` (`prop:corrected-local-decomposition`)
- `paper/proof_of_rh.tex:1624-1683` (`prop:cutoff-compatibility`)
- `paper/proof_of_rh.tex:1693-1754` (`prop:whitened-mixed-transfer`)
- `paper/proof_of_rh.tex:2212-2292` (definition of `H_m`, Proposition `boundary-estimate`)
- `paper/proof_of_rh.tex:2294-2322` (Proposition `odd-expansion`)
- `paper/proof_of_rh.tex:2415-2910` (downstream coefficient-level transfer/localization, not the first boundary theorem)
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-22`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:28-38`

## Dependencies

- The report depends only on extracting the theorem chain already written in the draft.
- The transport target depends on preserving three separate structures: an odd holomorphic corrected scalar, a transverse functional that annihilates the leading value channel, and a family-specific curvature/tail estimate at the same microscopic scale.

## Strongest objection

The boundary proof at `2223-2292` compresses one step into the sentence "the tail-curvature theorem and the corrected transfer bounds imply `S_2\ll L(m)S(m)^2` in the corrected regime"; that sentence is enough to identify the dependency chain, but not enough by itself to certify that another family inherits the same `L(m)S(m)^2/Q^3` boundary majorant without a separate family-specific curvature theorem and scale check.

## Needed for promotion

- State the transport target as a standalone family theorem in the exact minimal form above, not as automatic fallout from corrected whitening.
- Verify in the target family that the realized transverse scalar is odd and holomorphic on `|s|<\rho_0/Q`.
- Prove the family analogue of the transverse transfer bound `\Phi_K(\widehat\Omega^{\corr}-\widehat\Omega^{(0)})\ll S_2/Q^3`.
- Prove the family analogue of the boundary curvature/tail estimate that turns `S_2` into the desired boundary majorant.
- Keep `2415-2910` downstream: use it only after the realized odd scalar and its boundary bound already exist.
