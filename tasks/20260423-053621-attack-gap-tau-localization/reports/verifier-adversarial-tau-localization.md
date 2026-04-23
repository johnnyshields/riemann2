# Claim

[confirmed] In the current local scope, Ramanujan-\(\tau\) is not a cleaner proved local test object than zeta. It is only a cleaner candidate channel choice than the complex-Dirichlet case because standard external facts give a primitive self-dual degree-\(2\) completed \(L\)-function with sign \(+1\), so a real critical-line normalization is plausible without first solving a complex-channel ambiguity.

The strongest tau statement currently supported by manuscript-local scope plus explicit external facts is only this:

- [conditional] If one supplies for the completed tau \(L\)-function a realized real microscopic channel whose corrected transverse scalar is odd, holomorphic on a disk \(|s|<\rho_\tau/Q_\tau\), and satisfies the analogue of the manuscript boundary bound needed for Cauchy, then the odd-germ expansion and the universal odd-moment projector transport formally.

Claims that need scoped weakening:

1. "tau is a cleaner test object" should be weakened to "tau is a cleaner channel candidate than complex Dirichlet from current scope alone".
2. Any claim that the present manuscript already gives a tau localization theorem should be weakened to "the manuscript isolates the interface a tau realization would have to satisfy".
3. Any claim that degree \(2\) only changes constants should be weakened to "from current scope alone, the degree-sensitive analytic package must be rederived".
4. Any claim that the current draft already supports tau analogues of UV-001, UV-002, or UV-008 should be weakened to "unsupported from current local scope alone".

# Status

open

# Evidence

Proved from current manuscript scope:

- The phase-kernel, jet-limit, and finite-\(s\) removable-singularity algebra are written for a real phase \(\Phi\) and its derivative \(q\), before any zeta-specific decomposition enters. This is the genuine source-light layer. See `paper/proof_of_rh.tex:149-269`.
- The first explicit zeta-side input enters only at the decomposition
  \[
  q(t)=B_\zeta(t)+S(t),\qquad q(t)=q_{\loc}(t)+g_{\sm}(t)+E_{\est}(t),
  \]
  together with the curvature estimate \(|S''(m)|\ll L(m)S(m)^2\). See `paper/proof_of_rh.tex:273-300`.
- The unconditional portability boundary is exactly the odd-germ/projector layer: once one already has a real odd holomorphic transverse scalar with boundary control, the odd expansion follows by Cauchy and the discrete odd-moment projector is formal. See `paper/proof_of_rh.tex:2214-2322`, `2975-3169`, and `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-42`.
- The manuscript itself does not claim intrinsic local geometry alone closes the late contradiction; it explicitly scopes the endgame as RH-specific and still work-in-progress. See `paper/proof_of_rh.tex:26280-26299`, `26369-26551`.

Conditional on explicit external tau facts:

- [external] LMFDB records the Ramanujan-\(\tau\) \(L\)-function as degree \(2\), primitive, self-dual, with sign \(+1\), and with completed functional equation
  \[
  \Lambda(s)=\Gamma_\C(s+11/2)L(s)=\Lambda(1-s).
  \]
  This supports the limited statement that tau is a cleaner candidate real channel than a genuinely complex primitive Dirichlet character. Ref: `https://www.lmfdb.org/L/ModularForm/GL2/Q/holomorphic/1/12/a/a/`.

Missing from current scope:

- The tau analogue of the zeta-side decomposition `paper/proof_of_rh.tex:273-300` is not proved. There is no manuscript-defined tau replacement for \(B_\zeta\), \(S(m)\), or \(L(m)\).
- The microscopic denominator theorem is zeta-side and uses omitted-zero denominators
  \[
  D_{\rho,\pm}(s)=((2m-\gamma_\rho)\pm s)^2+a_\rho^2,
  \]
  together with the zero-free lower bound \(a_\rho\ge \sigma_0/Q\). See `paper/proof_of_rh.tex:856-946`. From current scope alone, there is no tau proof of the same disk radius, denominator shape, or holomorphy input.
- The preserved whitening hierarchy is proved with specific baseline scales
  \[
  G_\pm^{(0)}=\begin{pmatrix}O(Q)&O(1)\\O(1)&O(Q^3)\end{pmatrix},\qquad
  N^{(0)}=\begin{pmatrix}O(Q)&O(Q^2)\\O(Q^2)&O(Q^3)\end{pmatrix},
  \]
  yielding the claimed \(Q^{-3}\) transverse gain. See `paper/proof_of_rh.tex:1693-1754`, especially `1762-1779`, `1805-2047`. From current scope alone, there is no tau derivation that degree \(2\) preserves this power counting.
- The tau boundary estimate is absent. The manuscript bound
  \[
  |H_m(s)|\ll L(m)S(m)^2/Q^3
  \]
  depends on the zeta-side corrected decomposition, the value-channel annihilation, and the zeta-tail curvature package. See `paper/proof_of_rh.tex:2223-2292`. Without a tau replacement for those ingredients, the odd expansion cannot be promoted from formal template to realized tau statement.
- Any endgame-strength tau statement is farther out of scope. The current manuscript's crude scale bound \(S(m)\ll Q^2\) and the final contradiction bookkeeping are explicitly zeta-side and still only asymptotic even there. See `paper/proof_of_rh.tex:26301-26551`.

Adversarial conclusion on the main question:

- Tau is cleaner only as a channel choice. Self-duality and sign \(+1\) address the "which real object should one study?" interface better than the complex Dirichlet case.
- Tau is not yet a cleaner proved local test object. The degree-sensitive realization package, microscopic denominator package, whitening hierarchy, and boundary bound all remain missing theorems.

# Exact refs

- Common brief: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- Cycle synthesis: `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:11-18`, `35-49`, `51-66`, `79-96`
- Local portability boundary: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-18`, `29-52`
- Route A report: `tasks/20260423-053621-attack-gap-tau-localization/reports/gap-tau-localization-routeA.md:3-12`, `25-54`, `81-93`
- Route B report: `tasks/20260423-053621-attack-gap-tau-localization/reports/gap-tau-localization-routeB.md:3-13`, `28-43`, `62-72`
- Source-light local layer: `paper/proof_of_rh.tex:149-269`
- First explicit zeta-side layer: `paper/proof_of_rh.tex:273-300`
- Canonical calibration package: `paper/proof_of_rh.tex:426-850`
- Microscopic denominator comparability: `paper/proof_of_rh.tex:856-946`
- Preserved whitening gain: `paper/proof_of_rh.tex:1693-1754`
- Sharpened calibration remainder: `paper/proof_of_rh.tex:2050-2210`
- Odd transverse scalar and boundary estimate: `paper/proof_of_rh.tex:2214-2322`
- Matrix-level caution on where extra \(Q\)-gain can come from: `paper/proof_of_rh.tex:2327-2385`
- Crude zeta-side scale bound and current endgame status: `paper/proof_of_rh.tex:26301-26551`
- External tau facts: `https://www.lmfdb.org/L/ModularForm/GL2/Q/holomorphic/1/12/a/a/`

# Dependencies

- A completed-tau realization theorem producing the actual real microscopic channel and corrected transverse scalar.
- A tau replacement for the zeta-side decomposition \(q=B_\zeta+S\) and its local refinement.
- A tau microscopic denominator-comparability theorem with explicit disk radius.
- A tau derivation of the same-point and mixed-block baseline scales, or an explicit revised scale hierarchy if they differ.
- A tau proof of the corrected boundary estimate strong enough to feed Cauchy and the odd-moment projector.
- If any contradiction-level claim is desired, tau-side effective substitutes for the zeta quantities used in `paper/proof_of_rh.tex:26301-26551`.

# Strongest objection

The strongest positive sentence available here still depends on importing a full tau realization package that the manuscript does not contain. External self-duality and sign data identify a plausible real channel, but they do not prove the tau analogue of the corrected scalar, do not prove the microscopic denominator theorem, do not prove the \(Q^{-3}\) whitening gain, and do not prove the boundary estimate. So from current local scope alone, "tau is cleaner" is a statement about interface geometry, not a realized localization theorem.

# Needed for promotion

- Replace "cleaner test object" by "cleaner self-dual channel candidate than complex Dirichlet" whenever the claim is meant to be supported now.
- Replace any realized tau-localization wording by the conditional interface theorem: if tau supplies a real odd holomorphic scalar with the required boundary control, then the odd-germ/projector layer transports.
- Keep all claims about microscopic radius, denominator shape, whitening powers, and boundary size explicitly conditional until tau-specific proofs are written.
- Keep all UV-style portability claims for tau outside the proved zone until the tau realization package covers the same checkpoints as `paper/proof_of_rh.tex:273-300`, `856-946`, `1693-1754`, and `2223-2292`.

Honest verdict: tau is cleaner only as a channel choice, not as a proved local test object. The strongest supported tau statement is a conditional interface theorem for the odd-germ/projector layer plus explicit external self-duality facts. Any stronger wording needs scoped weakening until the tau decomposition, denominator, whitening, and boundary theorems are actually proved.
