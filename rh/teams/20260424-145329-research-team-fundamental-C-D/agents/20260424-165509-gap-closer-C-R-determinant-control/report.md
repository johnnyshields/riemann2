# Report: C-R determinant control

## Claim

I do not close C-FS2/C-FS3. I prove a smaller reduction: on every patch where
\(A_5^{\mathfrak f}\neq0\), the determinant slot
\[
[R]\longmapsto \det(R,A_5^{\mathfrak f})
\]
is an isomorphism
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}\simeq \mathbf C.
\]
Therefore controlling \(\det(R,A_5^{\mathfrak f})\) is exactly controlling the
septic quotient-defect class \([R]\). The smallest positive target is a
state-locality/descent theorem for that quotient class on the actual corrected
two-atom exceptional divisor, plus diagonal-merger normalization. Without that
theorem, the pinned deformation
\[
R\mapsto R+R_\kappa,\qquad
\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa
\]
is always available at the quotient-class level.

## Status

proved

This is a proved reduction, not a proof of the C package theorem.

## Evidence

The source theorem `rh/proof_of_rh.tex:11587-11775` introduces \(R\) only as a
representative of the quotient class
\[
-a_1^{-1}\overline E_{12}^{(7;1)}
\]
and proves only representative-independence of
\(\det(R,A_{5,1}^{\mathfrak f})\). It does not compute \(R\), and it does not
prove descent to the collision state.

Linear algebra closes the representative issue and identifies the true missing
theorem. Write
\[
A_5^{\mathfrak f}=uI+vS,\qquad R=r_uI+r_vS.
\]
Then
\[
\det(R,A_5^{\mathfrak f})=r_u v-u r_v.
\]
The kernel is exactly \(\mathbf C A_5^{\mathfrak f}\): if \(u\neq0\), then
\(\det(R,A_5^{\mathfrak f})=0\) implies \(r_v=(v/u)r_u\), and if \(v\neq0\)
the symmetric argument applies. Hence the determinant descends to an
isomorphism on \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\).

The deformation objection is therefore sharp. For
\(\tau=c^2\varepsilon\kappa\), the local choices
\[
R_\kappa=-\frac{\tau}{u}S\quad (u\neq0),
\qquad
R_\kappa=\frac{\tau}{v}I\quad (v\neq0)
\]
satisfy
\[
\det(R_\kappa,A_5^{\mathfrak f})=\tau.
\]
Thus fixed codomain, quotient representative-independence, and scalar
normalization do not rule out the \(c^2\varepsilon\kappa\) channel.

Script check:
`rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/scripts/determinant_slot_linear_algebra.js`
(git object `20519687125cd3e142f627db5a3d2e8b6f303db8`) verifies the gauge
shift, local right inverses for the deformation, and the centered template.
Output excerpt:

```text
sample_0_gauge_shift_difference = 0
sample_0_Rk_u_patch_det = 1292
sample_0_Rk_v_patch_det = 1292
sample_0_kernel_span_det = 0
sample_1_gauge_shift_difference = 0
sample_1_Rk_u_patch_det = 126
sample_1_Rk_v_patch_det = 126
sample_1_kernel_span_det = 0
sample_2_gauge_shift_difference = 0
sample_2_Rk_u_patch_det = -825
sample_2_Rk_v_patch_det = -825
sample_2_kernel_span_det = 0
centered_D2 = 3936
centered_dD2_dkappa = 96
symbolic_D2 = 2*kappa*(A*V1 - B*U1)
symbolic_deformation_target = c^2*eps*kappa
```

Three-bin separation:

- proved: \([R]\mapsto\det(R,A_5^{\mathfrak f})\) is an isomorphism on
  \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\) wherever \(A_5^{\mathfrak f}\neq0\).
- conditional: if the actual corrected two-atom septic quotient-defect class is
  state-local and merger-normalized, then the determinant channel is controlled.
- missing: the draft does not construct that actual two-atom quotient-defect
  class on the exceptional divisor, prove its state-locality, or force the
  centered condition \(A V_1-B U_1=0\).

## Baseline / delta

Baseline: the previous C-FS3 countermodel showed that fixed codomain,
\(\mathcal R\), blow-up analyticity, swap-evenness, scalar normalization, and
central \(\widehat\Psi\) value do not kill \(B_3=Z+\varepsilon\kappa\). The
C-FS2 actual-formula inspection then identified the uncomputed determinant slot
\(\det(R,A_5^{\mathfrak f})\) and centered
\[
D_2=2\kappa(A V_1-B U_1)
\]
as the live obstruction.

Delta: this pass proves the determinant slot is the whole one-dimensional
quotient-defect class. The next target is no longer "representative control" but
the sharper theorem: the actual corrected exceptional-divisor class
\([R]\) must factor through the descended collision state and be constant on any
independent exceptional slope/provenance fiber.

## Attempt status

keep

## Exact refs

- `C:/workspace/riemann2/CLAUDE.md` and
  `C:/workspace/riemann2/.agents/agents/_autoresearch.md` for
  writing discipline and deposit requirements.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  C package-level coincidence and negative C-FS2/C-FS3 entries.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:11-21`
  for UV-002, UV-003, UV-004.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md:124-209`
  for the resume baseline, target, protected surfaces, and pinned objections.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:242-290`
  for the verified C-FS2/C-FS3 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md`
  for the formal \(B_3=Z+\varepsilon\kappa\) countermodel.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md`
  and
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/actual-formula-inspection-CFS2.md`
  for the determinant-slot obstruction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/report-cfs2-actual-formula-review.md`
  and
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-source-CDE/report-cfs2-actual-formulas-source-check.md`
  for adversarial/source verification.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7004-7191` for the one-pair fixed
  package and \(\Delta_7\) gauge invariance.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7540-7924` for direct septic
  \(K_1\) slice and quotient-septic closure.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` for the defect-thickened
  identity and representative-independent determinant.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` for conditional
  source-level merger and diagonal-collapse context.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12255` for the naive
  source-summed obstruction and shear-blindness warning.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12511` for the
  collision-cancellation chart and WIP edge law.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:21142-21304` for same-tower closure
  and UV-004 pointwise bridge context.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:22409-22515` for conditional
  state-local package collapse.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23294-23409` for the centered
  determinant template.
- This note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/notes/determinant-slot-reduction.md`.
- Script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/scripts/determinant_slot_linear_algebra.js`,
  git object `20519687125cd3e142f627db5a3d2e8b6f303db8`.

## Dependencies

- The reduction uses \(A_5^{\mathfrak f}\neq0\). This is compatible with the
  C-good/quintic-generic patches used in the cited source neighborhoods, but an
  exceptional \(A_5^{\mathfrak f}=0\) locus would need separate treatment.
- It uses only the two-dimensional fixed sector
  \(\mathfrak f=\operatorname{span}\{I,S\}\) and the determinant convention in
  the draft.
- It depends on the current absence of an actual constructed
  \(\mathfrak P_2^{\corr}\) and of an exceptional-divisor formula for the
  quotient-defect class. If a future source computation supplies those, this
  report gives the exact scalar that must be checked.

## Strongest objection

This report does not compute the actual corrected two-atom \(R\). It proves that
the determinant slot is the right scalar and that the adversarial deformation is
available unless the actual package restricts the quotient class. A genuine
diagonal-merger, collision-functoriality, or state-locality theorem could still
close C; that theorem is precisely what remains missing.

## Needed for promotion

1. Construct the actual corrected two-atom finite-order package through order
   \(7\), including a normalized septic quotient-defect class
   \(\mathcal R_7(m,\kappa,t)\in\mathfrak f/\mathbf C A_5^{\mathfrak f}\) in the
   collision chart \(2\omega=\kappa\delta,\ t=\delta^2\).
2. Prove exceptional-divisor state-locality:
   \[
   \mathcal R_7(m,\kappa,0)
   \]
   factors through the descended collision state and has no independent
   provenance parameter.
3. Prove C-fiber constancy:
   \[
   \partial_\kappa\det(\mathcal R_7(m,\kappa,0),A_5^{\mathfrak f}(m))=0
   \]
   along every fixed descended collision state, or equivalently kill the
   residual class after subtracting the descended value.
4. Prove merger normalization to the one-pair value on the diagonal. In centered
   variables this must either force \(A V_1-B U_1=0\) or show that this expression
   is not an independent exceptional-fiber slope.
5. Send the resulting theorem through adversarial review against
   \(R_\kappa\) and source review against the actual order-\(3,5,7\) formulas.

## Autoresearch next step

continue: source-mine or construct the actual exceptional-divisor quotient
class \(\mathcal R_7(m,\kappa,0)\). The first concrete target should be an edge
law for
\[
\overline E_{12}^{(7;1)}
\]
parallel to the WIP cubic/quintic edge laws at `rh/proof_of_rh.tex:12477-12489`.

verify: ask adversarial/source verifiers to check whether any proposed edge law
really controls the whole quotient class, not just a representative or a fixed
codomain coordinate.

blocked: no process blocker. Mathematical blocker is the missing actual package
construction/state-locality theorem for \([R]\).

terminal: terminal for the subroute "representative gauge control could kill the
determinant deformation." It cannot. Not terminal for C-FS2/C-FS3 via actual
package state-locality or diagonal merger.
