# Report: gap-closer-E-finite-core-transfer

## Claim

`E_1` does not follow from C and D as currently isolated. The weakest theorem-shaped corrected finite-core hypothesis that upgrades the paper's defect-free affine-dependence theorems to a genuine bad core is **projected total low-order interaction vanishing** for the actual finite core, not full interaction-germ vanishing and not pairwise quadratic factorization.

For a normalized bad finite core
\[
F_{\core}(z)=\sum_{j=1}^k a_jF_{h_j}(z)+\mathcal I_{\ge2}(z)
\]
on a good patch, define the total corrected low-order interaction defects
\[
D_3:=[\mathcal I_{\ge2}]_3,
\qquad
D_5^{\mathfrak f}:=\pi_{\mathfrak f}[\mathcal I_{\ge2}]_5,
\qquad
\overline D_7:=[\pi_{\mathfrak f}[\mathcal I_{\ge2}]_7]
\in \mathfrak f/\mathbf C A_5^{\mathfrak f}.
\]
Then the minimal sufficient `E_1` theorem is:
\[
D_3=0,
\qquad
D_5^{\mathfrak f}=0,
\qquad
\overline D_7=0
\]
for the genuine corrected bad core through the first incidence-relevant order. The planar quintic lane needs only `D_3=D_5^{\mathfrak f}=0`; the lifted `v_5` or `u_5` lane also needs the septic quotient equation. Under these exact projected vanishings, the paper's defect-free results apply unchanged and place the bad core into the existing affine-incidence lanes for `\Xi(h)` and `Q_v(h)`/`Q_u(h)`.

This is the smallest clean target I can isolate. If one refuses exact projected vanishing, then `E_1` must be rewritten as a new inhomogeneous rank theorem: the nonzero corrected defect vector must itself force a homogeneous affine circuit among the same nodes. That theorem is not present in the draft and is not implied by C/D.

## Status

open

## Evidence

The defect-free quintic theorem in `rh/proof_of_rh.tex:12676-12713` assumes only that the multi-pair interaction contributes nothing to the cubic and quintic coefficients. Its proof then reads the bad-core identity coefficientwise and obtains
\[
\sum_j a_j(c(h_j),u_5(h_j),v_5(h_j))=0.
\]
After setting `b_j=a_jc(h_j)`, this is exactly affine dependence of
\[
\Xi(h_j)=\left(u_5(h_j)/c(h_j),v_5(h_j)/c(h_j)\right).
\]
Thus the theorem does not require full interaction-germ vanishing; it requires only projected total vanishing at the cubic and quintic fixed-sector levels.

The lifted theorem in `rh/proof_of_rh.tex:12795-12825` adds only one more projected requirement: the multi-pair interaction contributes nothing to the septic coefficient on the chosen local patch. In the `v_5\neq0` gauge `v_7=0`, the septic equation gives
\[
\sum_j b_j\,\Delta_7(h_j)/(c(h_j)v_5(h_j))=0,
\]
so the lifted points
\[
Q_v(h_j)=\left(u_5/c,\ v_5/c,\ \Delta_7/(cv_5)\right)(h_j)
\]
are affinely dependent. The `u_5` patch is parallel by `rh/proof_of_rh.tex:12981-12998`.

If the total projected defect is not zero, the exact bad-core identities become inhomogeneous:
\[
\sum_j a_j(c_j,u_{5,j},v_{5,j})=-(D_3,D_{5,I},D_{5,S})
\]
and, on a lifted patch,
\[
\sum_j b_j\,\sigma_v(h_j)=-(\text{septic projected defect}).
\]
The existing affine-incidence theorems do not absorb this inhomogeneous right-hand side. They produce incidence only from homogeneous linear relations with coefficient sum zero. Therefore C and D can feed `E_1` only after an additional low-order interaction theorem kills these projected defects or replaces them by a new rank/incidence statement.

The source-level two-point material supports the same reduction. `rh/proof_of_rh.tex:11888-12040` shows that swap / one-amplitude collapse / diagonal merger for the actual finite-order source package would imply quadratic interaction defects for two points, but `rh/proof_of_rh.tex:12192-12228` records that the naive source-summed corrected block cannot prove the needed linear merger law. For general finite cores, the direct analogue needed by `E_1` is weaker than full pairwise factorization: only the total projected corrected defects through cubic/quintic/septic must vanish on the actual bad core.

For `E_2`, the positive-kernel theorem at `rh/proof_of_rh.tex:3583-3609` can bypass incidence only if one proves a direct one-sided weighted-average lower bound for `H_{\core}^{(2N-1)}` or direct lower control of `\Xi_{\core}^{(N)}`. The exact surviving expansion at `rh/proof_of_rh.tex:3984-3996` has a positive universal tail, but the coefficients can have arbitrary signs. Hence a bare lower bound on the first surviving coefficient still smuggles in an unproved no-cancellation or tail-domination theorem.

Separated bins:

- **proved:** the defect-free affine-dependence implications under projected low-order interaction vanishing; the positive-kernel representation; the exact surviving-tail expansion; finite-core localization on the zeta side.
- **conditional on C/D and the new `E_1` vanishing theorem:** a genuine corrected bad core enters the existing `k=2,3,4` affine-incidence lanes.
- **missing:** any theorem proving `D_3=D_5^{\mathfrak f}=\overline D_7=0` for the genuine corrected finite core, or any replacement inhomogeneous rank theorem; any direct `E_2` lower theorem that avoids hidden no-cancellation assumptions.

## Baseline / delta

Baseline from `agents/20260424-145500-gap-closer-UV002-contradiction/report.md` was the split
\[
C\to D\to E_1\to E_2,
\]
with `E_1` described as descent from corrected finite-core data to defect-free affine-incidence lanes and `E_2` as weighted-average/direct-`\Xi` lower control. This report sharpens `E_1` from a vague descent into the precise projected low-order vanishings needed by the cited paper theorems. It improves the frontier by replacing “defect-free descent” with the exact minimal total-defect equations in the cubic, quintic fixed-sector, and septic quotient layers.

## Attempt status

keep

## Exact refs

- `UV-002` — `rem:wip-pairlike-finitecore`, `rh/proof_of_rh.tex:5604-5643`.
- `UV-007` — `rem:wip-final-endgame-status`, `rh/proof_of_rh.tex:26369-26398`.
- `rh/proof_of_rh.tex:3520-3687` — positive-kernel representation and downstream target for first surviving derivative control.
- `rh/proof_of_rh.tex:3853-4190` — corrected `N`-point scalar, exact surviving expansion, and finite-core localization.
- `rh/proof_of_rh.tex:11368-11585` — `\widehat\Psi` and exact strengthened two-pair coincidence in the defect-free/projected setting.
- `rh/proof_of_rh.tex:11888-12040` — finite-order two-point source criterion and conditional quadratic defect estimate.
- `rh/proof_of_rh.tex:12192-12228` — naive source-summed route fails to prove one-atom linearity / merger.
- `rh/proof_of_rh.tex:12586-12610` — `rem:minimal-core-reformulation`: two-stage `\widehat\Psi` then affine-incidence problem.
- `rh/proof_of_rh.tex:12669-12979` — defect-free quintic circuit and lifted affine-dependence theorems.
- `rh/proof_of_rh.tex:13933-15239` — lifted incidence derivative geometry and exact contact controls.
- `rh/proof_of_rh.tex:24985-25030` — finite-core endgame split and source/package burden.
- `rh/proof_of_rh.tex:26369-26609` — current pair-like final endgame and first-nonzero-odd-jet warning.
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-UV002-contradiction/report.md:57-77` — prior split of theorem E into `E_1` and `E_2`.
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-E-finite-core-transfer/notes/e1-minimal-reduction.md` — scratch reduction deposited with this report.
- Scripts: none run.

## Dependencies

- C: corrected reduced-package diagonal collapse / collision-functoriality.
- D: transform-level package-to-first-surviving-odd-state locality modulo `\ker\Phi_K`.
- New `E_1` low-order theorem: projected total corrected finite-core interaction vanishing through the incidence-relevant layers, or a replacement inhomogeneous rank theorem.
- Existing defect-free affine-incidence theorems for `\Xi`, `Q_v`, and `Q_u`.
- `E_2`: direct transformed-scalar lower control or weighted-average derivative control strong enough to feed the positive-kernel `N`-point formula.

## Strongest objection

The proposed `E_1` vanishing theorem may be false for genuine finite cores. Existing two-point audits already show that naive source-summed corrected packages are even in source weights and cannot supply the needed one-atom linearity; a general finite core may have nonzero projected interaction defects that are neither negligible nor removable. If such defects survive, the bad-core equations are inhomogeneous and the present affine-incidence lanes do not apply. In that case the correct target is not vanishing but a new inhomogeneous finite-core incidence theorem, and this report has only isolated that alternative rather than proved it.

## Needed for promotion

1. State a corrected finite-core low-order interaction theorem in one of two forms:
   - **preferred vanishing form:** for every genuine corrected minimal bad core on a good patch, the total projected defects satisfy
     \[
     D_3=0,
     \qquad D_5^{\mathfrak f}=0,
     \qquad \overline D_7=0
     \]
     through the first incidence-relevant order; or
   - **replacement rank form:** even with nonzero projected defects, the inhomogeneous equations force a homogeneous affine circuit among the same nodes in the `\Xi` or lifted `Q_v`/`Q_u` coordinates.
2. Prove the theorem for the actual corrected finite-core package, not for the naive source-summed whitened block.
3. Verify patch compatibility between `v_5` and `u_5` gauges and explicitly state the exceptional-locus handoff.
4. After `E_1`, prove `E_2` in a genuinely sufficient form: direct `\Xi_{\core}^{(N)}` lower control, or one-sided weighted-average/pointwise control of `H_{\core}^{(2N-1)}` on `0\le s\le N/Q^2`.
5. If using a coefficient-side `E_2`, add a sign/variation/tail-domination theorem preventing cancellation in the universal positive tail.
6. Submit the resulting `E_1/E_2` stack to adversarial and source verification before any paper promotion.

## Honest verdict

`E_1` is still open, but the gap is now smaller and theorem-shaped. The paper's defect-free incidence results can be reused if the actual corrected finite core has zero total projected interaction through cubic/quintic/septic quotient layers. C and D do not currently imply that. A direct positive-kernel route for `E_2` can bypass incidence only by proving derivative-side or direct-`\Xi` lower control; otherwise it hides the same missing no-cancellation theorem under a coefficient lower bound.

## Autoresearch next step

continue: try to prove or refute the projected total low-order interaction-vanishing theorem for genuine corrected finite cores, starting with the two-point source criterion and then checking whether a multi-core inclusion-exclusion/merger law can give `D_3=D_5^{\mathfrak f}=\overline D_7=0` without full pairwise factorization.

verify: adversarially test whether C/D plus corrected package fiber equality can leave a nonzero inhomogeneous defect vector; source-audit the definitions of `D_3`, `D_5^{\mathfrak f}`, and `\overline D_7` against the actual finite-order package objects.

blocked: no coordinator action required unless the team wants the low-order defect objects promoted to named UV entries.

terminal: not terminal; `E_1` has been reduced to projected low-order interaction-vanishing or an explicit inhomogeneous rank replacement.
