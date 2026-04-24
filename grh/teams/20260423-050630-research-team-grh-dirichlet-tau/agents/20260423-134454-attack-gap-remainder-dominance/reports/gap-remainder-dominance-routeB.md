# Claim

Once a family theorem supplies the exact positive `S`-slot scalar in the decomposition
\[
\Delta_{\mathcal F}(m,\sigma)=S_{\mathcal F}(m)A_{\val}(x)+R_{\mathcal F}(m,\sigma),
\]
the next real bottleneck is remainder dominance, not a second leading-coefficient theorem. The smallest family-specific replacement for the zeta remainder step is a theorem that makes the family analogue of the corrected remainder negligible after calibration. In the paper's notation, the minimal target is either the direct calibrated form
\[
\Psi_{x,d}(R_{\mathcal F})=o\!\left(\frac{x}{B_{\mathcal F}(m)}S_{\mathcal F}(m)\right),
\]
or, more structurally, a family analogue of
\[
|\Psi_{x,d}(R_\zeta)|\ll \frac{S_2}{Q^3}
\quad\text{plus}\quad
S_{2,\mathcal F}=o\!\bigl(xQ^2S_{\mathcal F}(m)\bigr).
\]
The `Q^{-3}` calibration transfer is mostly local-analytic. The hard new content is source-specific control of the family curvature/tail quantity replacing `S_2`, together with cutoff admissibility and any family denominator/whitening input needed to keep that estimate uniform.

# Status

`proved`:

- In the zeta draft, exact `S(m)`-slot identification already removes the need for any further leading-channel coefficient theorem.
- In the zeta draft, once `S_2=o(xQ^2S(m))`, the calibrated remainder is negligible.
- In the zeta draft, the map from entrywise remainder control to calibrated `Q^{-3}` decay is already implemented by local whitening/pairing algebra.

`conditional`:

- If a family theorem gives the exact background-subtracted scalar occupying the manuscript's `S(m)` slot, and if the family admits the same local block scales and denominator comparability, then the manuscript's local argument should transfer with `S_2` replaced by a family curvature/remainder quantity `S_{2,\mathcal F}`.
- Under those hypotheses, a family theorem of the form `S_{2,\mathcal F}=o(xQ^2S_{\mathcal F})` is enough to replace the zeta remainder step.

`missing`:

- A family theorem that controls the analogue of `S_2` strongly enough to imply remainder dominance in the calibrated regime.
- Verification that the family's corrected same-point and mixed-block perturbations have the same entrywise scales used in the `Q^{-3}` transfer.
- Verification that the cutoff condition needed to force `S_{2,\mathcal F}=o(xQ^2S_{\mathcal F})` is compatible with the family's admissible local regime, especially if `x` must shrink as in the variable-`x` remark.

# Evidence

The positive-`S` note already isolates the logical point: once a family theorem yields the exact scalar in the manuscript's `S(m)` slot, the manuscript already supplies the leading-channel coefficient theorem; what remains are remainder dominance, the odd/transverse package, and family-specific denominator/whitening/boundary control. That note explicitly warns against saying quotient positivity alone solves the problem.

The paper's calibration section matches that split. Proposition `canonical-calibration` reduces the toy comparison to the estimate
\[
\Psi_{x,d}(\Delta_\zeta)=c_{x,d}\frac{x}{B}S(m)+\Psi_{x,d}(R_\zeta),
\]
so the only obstruction after exact scalar identification is the remainder term. Corollary `sharpened-calibration-remainder` proves
\[
|\Psi_{x,d}(R_\zeta)|\ll_D \frac{S_2}{Q^3},
\]
and the same corollary shows that `S_2=o(xQ^2S(m))` is exactly what turns this into
\[
\Psi_{x,d}(R_\zeta)=o\!\left(\frac{x}{B_\zeta(m)}S(m)\right).
\]
Proposition `calibration-remainder-cutoff` then reduces that condition further to a cutoff-driven tail-curvature bound.

This shows the minimal family replacement is not a new theorem identifying another leading coefficient. It is a theorem that supplies the family analogue of the zeta input `S_2=o(xQ^2S(m))`, or directly the resulting calibrated negligibility estimate. Everything between those statements and the calibrated conclusion is already local algebra in the draft.

The local-versus-source split is also visible in the proofs. The `Q^{-3}` factor in Corollary `sharpened-calibration-remainder` comes from baseline inverse-square-root scales, entrywise perturbation sizes for corrected blocks, and the small-`x` behavior of `A_{\val}` and its pairing with `M(d)`. By contrast, Theorem `tail-curvature` is where zeta-specific source input enters: it turns omitted-zero structure into the scalar bound `S_2\ll \|B_{\Aut}''\|+Q/R^3`. That is the place a family theorem must replace.

The odd-channel section confirms the same dependence. The boundary estimate for `H_m` uses the corrected decomposition together with the `S_2/Q^3` transfer and then inserts the source-level bound `S_2\ll L(m)S(m)^2` on the microscopic boundary. So even after exact `S`-slot identification, the source-specific remainder package is still doing real work in the transverse channel.

Finally, the variable-`x` remark shows that remainder dominance is not fully isolated from scale selection: if one shrinks `x` to keep the toy parameter microscopic, one must preserve uniform remainder control and cutoff admissibility in that shrinking regime. So the minimal family theorem is small in logical form, but it must be uniform in the regime the endgame actually uses.

# Exact refs

- Common brief: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`.
- Positive-`S` implication note: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-38,42-50`.
- Value-channel derivative, small-`x` scale, and pairing:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:471-485`,
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:601-616`,
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:661-737`.
- Canonical calibration and remainder bottleneck:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:739-794`.
- Tail-curvature input:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:361-395`.
- Corrected local decomposition and cutoff compatibility:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1566`,
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1624-1691`.
- Whitened mixed-block `Q^{-3}` transfer:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754`,
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1784-1822`.
- Sharpened calibration remainder and cutoff-driven dominance:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2209`,
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:796-850`.
- Odd/transverse dependence on the same remainder package:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322`.
- Variable-`x` caveat:
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5500-5598`.

# Dependencies

- Exact family theorem identifying the same background-subtracted scalar that occupies the paper's `S(m)` slot.
- Family analogue of local denominator comparability and corrected whitening in the microscopic regime.
- Family analogue of same-point and mixed-block perturbation estimates with entrywise sizes strong enough to recover `O(S_{2,\mathcal F}/Q^3)` after whitening.
- Family source theorem converting omitted-spectrum/tail structure into a scalar bound on `S_{2,\mathcal F}`.
- If the endgame uses shrinking `x`, uniformity of all of the above for `0<x\le x_0(D)`.

# Strongest objection

The phrase "remainder dominance is the next real bottleneck" is correct only after bundling in hidden family hypotheses. Corollary `sharpened-calibration-remainder` is not purely formal: it relies on zeta-specific local perturbation scales and denominator behavior already proved earlier in the draft. For a new family, those inputs may fail or acquire extra conductors, gamma-factor terms, parity effects, or non-self-dual complications. So from the current scope alone, the honest statement is narrower: once the exact `S`-slot scalar is known and once the family preserves the same local whitening architecture, the next unresolved step is remainder dominance.

# Needed for promotion

- State a family theorem in minimal form. Recommended target:
  if the exact `S`-slot decomposition holds, then for admissible microscopic `x` and cutoff `R`,
  \[
  |\Psi_{x,d}(R_{\mathcal F})|\ll \frac{S_{2,\mathcal F}}{Q^3}
  \quad\text{and}\quad
  S_{2,\mathcal F}=o\!\bigl(xQ^2S_{\mathcal F}(m)\bigr).
  \]
- Verify which parts of the zeta proof are unchanged local algebra and which require family input; in particular, isolate the exact replacements for Theorem `tail-curvature`, the perturbation bounds used in Proposition `whitened-mixed-transfer`, and the denominator/pairing uniformity used in Corollary `sharpened-calibration-remainder`.
- Check whether the family theorem remains valid in the variable-`x` regime needed by `rem:wip-calibration-small-u`; otherwise the claimed bottleneck is understated.
- Keep the final wording scoped: no contradiction claim, no endgame claim, and no claim that quotient/phase data alone control the remainder.
