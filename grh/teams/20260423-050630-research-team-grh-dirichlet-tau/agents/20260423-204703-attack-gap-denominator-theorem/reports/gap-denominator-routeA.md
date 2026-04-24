# Claim

The cleanest denominator-comparability theorem currently used by the RH draft is Proposition `prop:denominator-comparability`:

`Microscopic denominator comparability and omitted-smooth holomorphy`.

Its exact content is:

- for each omitted zero `\rho`, with
  `D_{\rho,\pm}(s) = ((2m-\gamma_\rho) \pm s)^2 + a_\rho^2` and
  `a_\rho \in \{\beta_\rho, 1-\beta_\rho\}`;
- assuming the zero-free-region lower bound `a_\rho \ge \sigma_0 / Q` on the admissible midpoint class;
- and assuming `|s| \le \rho_0 / Q` with `\rho_0 \le \sigma_0 / \sqrt 6`;

one has the uniform two-sided comparison

`(1/2)((2m-\gamma_\rho)^2 + a_\rho^2) \le |D_{\rho,\pm}(s)| \le (3/2)((2m-\gamma_\rho)^2 + a_\rho^2)`.

The proposition then concludes that the omitted-zero sums defining `T_{\far}(t_\pm)` and all required `t`-derivatives converge uniformly on `|s| < \rho_0 / Q`, provided the corresponding real-line shell sums converge. Hence `g_{\sm}(t_\pm) = B_{\Aut}(t_\pm) + T_{\far}(t_\pm)` and its required derivatives extend holomorphically to the same disk.

This is the theorem-sized denominator input used to justify replacing real-line omitted-zero control by complex-disk control in the corrected finite-`s` package.

# Status

proved

# Evidence

Proved:

- The theorem itself is stated and proved at `paper/proof_of_rh.tex:856-946`.
- Its direct role is explicit in Proposition `prop:corrected-whitening`: `Holomorphy of the omitted smooth part and its required t-derivatives follows from Proposition~\ref{prop:denominator-comparability}` at `paper/proof_of_rh.tex:1417-1424`.
- That holomorphic-whitening step concludes that `G_{m,\pm}^{\corr}(s)`, `N_m^{\corr}(s)`, and therefore `\widehat\Omega_\zeta^{\corr}(s;m)` are holomorphic on `|s| < \rho_0 / Q`; see `paper/proof_of_rh.tex:1392-1458`.
- Downstream, the corrected local deformation decomposition invokes that holomorphic-whitening theorem as the analytic input for the whitening map; see `paper/proof_of_rh.tex:1568-1575`.
- In the focus region `paper/proof_of_rh.tex:2050-2209`, the sharpened calibration remainder estimate is presented as an algebraic / perturbative consequence of the corrected local decomposition plus the whitened mixed-transfer bounds; see `paper/proof_of_rh.tex:2090-2209`. So the denominator theorem enters this corollary indirectly through the prior holomorphic-whitening and corrected-decomposition steps.
- Immediately after the focus region, the odd microscopic expansion states `H_m(s)` is odd and holomorphic, with the proof citing Proposition `prop:corrected-whitening`; see `paper/proof_of_rh.tex:2294-2322`. This is another downstream use of the denominator theorem.
- Later `N`-point localization also cites Proposition `prop:corrected-whitening` as the source of holomorphy for `H_m`; see `paper/proof_of_rh.tex:3896-3905`.

Conditional on stated upstream inputs:

- Proposition `prop:denominator-comparability` assumes the zero-free-region lower bound `a_\rho \ge \sigma_0 / Q` on the admissible midpoint class and also assumes that the corresponding real-line shell sums already converge; see `paper/proof_of_rh.tex:870-895`.
- So the theorem is not a stand-alone derivation of omitted-zero holomorphy from denominator algebra alone. It transports existing real-line shell convergence to the microscopic complex disk.

Missing:

- In the inspected regions, no stronger denominator theorem is used. I did not find a statement here that gives more than comparability plus holomorphic extension of the omitted-smooth piece.
- The proposition does not itself prove the later `Q^{-3}` calibration remainder estimate, positivity of corrected same-point blocks, or the boundary bound for the odd channel. Those require additional perturbation, tail-curvature, pairing, and cutoff-compatibility inputs.

# Exact refs

- Theorem statement and proof: `paper/proof_of_rh.tex:856-946`.
- Direct use in corrected finite-`s` holomorphic whitening: `paper/proof_of_rh.tex:1392-1458`, especially `1417-1424`.
- Use inside corrected local deformation decomposition via holomorphic whitening: `paper/proof_of_rh.tex:1497-1575`, especially `1568-1575`.
- Focus-region downstream corollary: `paper/proof_of_rh.tex:2050-2209`.
- Odd microscopic expansion using the holomorphic-whitening theorem: `paper/proof_of_rh.tex:2294-2322`.
- Later `N`-point localization relying on the same holomorphy: `paper/proof_of_rh.tex:3896-3905`.

# Dependencies

- Zero-free-region lower bound `a_\rho \ge \sigma_0 / Q` on the admissible midpoint class.
- Small-disk restriction `|s| \le \rho_0 / Q` with `\rho_0 \le \sigma_0 / \sqrt 6`.
- Pre-existing convergence of the corresponding real-line shell sums for the omitted-zero terms and required derivatives.
- For downstream use in the calibration remainder corollary: Proposition `prop:corrected-whitening`, Proposition `prop:corrected-local-decomposition`, Proposition `prop:cross-block-perturbation`, Proposition `prop:whitened-mixed-transfer`, Theorem `thm:tail-curvature`, Lemma `lem:Aval-small-x`, and Proposition `prop:pairing`.

# Strongest objection

The denominator-comparability theorem is clean, but its role is narrower than a full corrected-package theorem. It only certifies that omitted-zero denominators do not collapse when the real variable is moved to the microscopic complex disk, so that omitted-smooth terms and their required derivatives remain holomorphic there. From this scope alone, it does not deliver the later calibration bound or the odd-channel boundary estimate. Those later results still depend on several additional perturbative and transfer theorems.

# Needed for promotion

Nothing further is needed to identify this as the cleanest denominator-comparability theorem currently used in the draft; that identification is already supported by the cited statement and direct citation chain.

If one wanted a stronger promoted summary sentence in the manuscript or lore, the safest wording is:

`the current denominator theorem transports real-line omitted-zero shell control to the microscopic complex disk and thereby supplies the holomorphic omitted-smooth input needed for corrected finite-s whitening; it is not, by itself, the full calibration-remainder or odd-package theorem.`
