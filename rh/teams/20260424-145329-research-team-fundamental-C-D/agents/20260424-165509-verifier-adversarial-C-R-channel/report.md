# Adversarial verifier report: C R-determinant channel

## Claim

The current C-FS2/C-FS3 frontier does not survive the \(R_\kappa\) determinant
pressure test from the audited scope alone. The perturbation
\[
R\longmapsto R+R_\kappa,
\qquad
\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa
\]
shifts the reduced third C coordinate by \(\varepsilon\kappa\). This matches the
existing C-FS3 formal countermodel and is not excluded by the C-FS2
actual-formula neighborhoods, where the centered channel remains
\[
D_2=2\kappa(AV_1-BU_1).
\]
Therefore any future C closure must prove an actual-package theorem killing the
determinant slot: construction/control of \(R\), descent of
\(\det(R,A_5^{\mathfrak f})\) to the collision state, diagonal merger, or an
actual formula identity such as \(AV_1-BU_1=0\). Fixed codomain, scalar
normalization, blow-up analyticity, swap-evenness, central-slope agreement, and
the displayed order-\(3,5,7\) formulas alone do not promote C.

## Status

proved

## Evidence

Three-bin separation:

- **proved:** In Theorem
  `rh/proof_of_rh.tex:11587-11775`, the third coordinate difference contains
  the representative-independent scalar
  \(\det(R,A_{5,1}^{\mathfrak f})\). If \(R\) is replaced by
  \(R+R_\kappa\) with
  \(\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa\), then
  \[
  \frac{\Delta+c^2\varepsilon\kappa}{c^2}-\frac{\Delta}{c^2}
  =\varepsilon\kappa.
  \]
  Thus the reduced exceptional trace is slope-dependent unless a separate
  theorem forbids the perturbation.
- **proved:** Representative-gauge invariance does not kill this test. The
  proof at `rh/proof_of_rh.tex:11768-11774` only says that adding
  \(\xi A_5^{\mathfrak f}\) to \(R\) leaves the determinant unchanged. The test
  changes the determinant by a prescribed scalar, so it is a quotient-defect
  control problem, not a raw representative problem.
- **proved/computational:** The script
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/scripts/r_channel_pressure_test.js`
  checks the reduced-coordinate shift, chartwise determinant witnesses when
  \(A_5^{\mathfrak f}\neq0\), and the centered \(D_2\) template. Output:

```text
symbolic det_Rk_A5 = c^2*eps*kappa
symbolic reduced_third_coordinate_shift = eps*kappa
symbolic d_shift_dkappa = eps
symbolic v_chart_det = c^2*eps*kappa
symbolic u_chart_det = c^2*eps*kappa
symbolic D2 = 2*kappa*(A*V1 - B*U1)
symbolic dD2_dkappa = 2*(A*V1 - B*U1)
sample det_Rk_A5 = 315
sample reduced_shift = 35
sample v_chart_det = 315
sample u_chart_det = 315
sample D2 = 1092
sample dD2_coeff = 156
```

- **conditional:** If the actual corrected two-atom package
  \(\mathfrak P_2^{\corr}\) is constructed and a diagonal-merger,
  collision-functoriality, or state-locality theorem proves that
  \(\det(R,A_5^{\mathfrak f})\) factors through the descended collision state,
  then this perturbation is excluded. The checked source treats those as missing
  inputs, not proved facts.
- **missing:** No audited source constructs the actual corrected two-atom fixed
  triple as an analytic germ, defines its corrected reduced-package fibers on
  the exceptional divisor, computes \(R\) there, proves
  \(\partial_\kappa\det(R,A_5^{\mathfrak f})=0\), or proves
  \(AV_1-BU_1=0\) in the centered template.

Scoped failures:

- The route "C-FS3 follows from fixed codomain, \(\mathcal R\), blow-up
  analyticity, swap-evenness, scalar normalization, and
  \(B(m,0)=\widehat\Psi(m)\)" fails from that formal-properties-only scope.
  This is exactly the existing C-FS3 countermodel baseline.
- The route "the displayed order-\(3,5,7\) formula neighborhoods already forbid
  \(c^2\varepsilon\kappa\)" fails from the audited formula-neighborhood scope
  alone. They expose \(\det(R,A_5^{\mathfrak f})\) and
  \(D_2=2\kappa(AV_1-BU_1)\), but do not control them.
- The route "C-FS2 no-extra-codomain-state automatically implies C-FS3" fails
  from C-FS2 alone. The formal model has no extra C codomain coordinate and
  still has nonconstant exceptional trace.

## Baseline / delta

Baseline: `report-cfs23-followup.md` and
`report-cfs3-countermodel-review.md` verify a formal fixed-codomain
countermodel with \(B_3=Z+\varepsilon\kappa\). `report-cfs2-actual-formulas.md`
and `report-cfs2-actual-formula-review.md` verify that the actual
order-\(3,5,7\) formula neighborhoods leave the C-visible determinant slot
\(\det(R,A_5^{\mathfrak f})\) and the centered channel
\(D_2=2\kappa(AV_1-BU_1)\) uncontrolled.

Delta: this report packages those two negatives into a single adversarial
acceptance test for any future C closure. A proposed proof must explicitly say
why the deformation
\[
R\mapsto R+R_\kappa,\qquad
\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa
\]
is not an admissible actual-package variation. If it cannot, it has not closed
C-FS2/C-FS3. The result is a pressure test and scoped negative, not a promotion
or a disproof of C for the actual corrected package.

## Attempt status

keep

## Exact refs

- Current team findings:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`,
  especially the negative entry "Current reduced-package blow-up hypotheses do
  not force diagonal collapse."
- Targeted UVs:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:11-20`
  for UV-002, UV-003, and UV-004.
- Resume dispatch:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md:132-185`
  for the C target and pinned \(R_\kappa\) objection.
- Verified frontier:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:242-290`.
- C-FS3 formal countermodel:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md:1-150`.
- C-FS3 adversarial review:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/report-cfs3-countermodel-review.md:1-90`.
- C-FS2 actual-formula negative:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md:1-142`.
- C-FS2 adversarial review:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/report-cfs2-actual-formula-review.md:1-95`.
- Paper determinant slot:
  `rh/proof_of_rh.tex:11587-11775`.
- Source-level merger as assumption and not proof:
  `rh/proof_of_rh.tex:11888-12189`.
- Naive source-summed obstruction and shear-blind determinant warning:
  `rh/proof_of_rh.tex:12192-12255`.
- Collision-cancellation / parity-projective frontier:
  `rh/proof_of_rh.tex:12385-12511`.
- Centered \(D_2\) template:
  `rh/proof_of_rh.tex:23294-23409`.
- This deposit note:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/notes/r-channel-pressure-test.md`.
- This deposit script:
  `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/scripts/r_channel_pressure_test.js`.

## Dependencies

- The pressure test depends on the determinant convention for coordinates in
  \(\mathfrak f=\operatorname{span}\{I,S\}\), as used in the cited
  \(\Delta_7=\det(A_7^{\mathfrak f},A_5^{\mathfrak f})\) identities.
- It depends on the good-patch/nonzero-vector condition
  \(A_5^{\mathfrak f}\neq0\) for the explicit chartwise witnesses to
  \(R_\kappa\). If a future proof works on an \(A_5^{\mathfrak f}=0\) locus,
  it needs a separate exceptional-locus argument.
- It depends on the audited absence of an actual construction or computation of
  \(\mathfrak P_2^{\corr}\) and \(R\), not on a claim that such a construction
  cannot exist.
- It uses the centered \(D_2\) template only as an adversarial channel, not as a
  full actual-package counterexample.

## Strongest objection

The pressure test is not an actual corrected-package counterexample. A real
construction of \(\mathfrak P_2^{\corr}\) could make \(R_\kappa\) inadmissible,
could force \(\det(R,A_5^{\mathfrak f})\) to descend to the collision state, or
could prove \(AV_1-BU_1=0\) for the actual centered branch. That objection is
exactly the remaining proof obligation. Until such a theorem is supplied, the
current C closure fails only from the formal/displayed-formula scope described
above, not from the full actual package.

## Needed for promotion

No promotion is recommended. For a future C promotion to survive this review, it
must provide all of the following:

1. A source-defined actual corrected two-atom fixed triple
   \[
   \mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
   \]
   as an analytic germ, including the exceptional divisor convention after
   \(2\omega=\kappa\delta\).
2. A corrected reduced-package fiber definition for that triple.
3. Either an actual computation of the quotient-defect representative \(R\) on
   the exceptional divisor, or a theorem proving
   \(\det(R,A_5^{\mathfrak f})\) factors through the descended collision state
   with no independent \(\kappa\) or provenance dependence.
4. A proof excluding
   \[
   R\mapsto R+R_\kappa,\qquad
   \det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa.
   \]
5. A separate handling of the centered \(D_2\) channel: prove
   \(AV_1-BU_1=0\), prove the centered channel is not C-visible for the actual
   package, or derive diagonal merger strongly enough that this cancellation is
   automatic.
6. Adversarial and source verification after those ingredients are written.

## Autoresearch next step

continue: ask the C gap-closer or source verifier to compute the actual
exceptional-divisor quotient-defect representative \(R\), or formulate the
minimal descent theorem
\(\det(R,A_5^{\mathfrak f})=\mathcal D(\text{descended collision state})\) with
\(\partial_\kappa\mathcal D=0\).

verify: any proposed positive proof must be rerun against the explicit
\(R_\kappa\) perturbation and the centered condition
\(AV_1-BU_1\neq0\).

blocked: no process blocker. The mathematical blocker is the missing actual
package construction/control theorem for \(R\).

terminal: terminal for the subroutes "formal C properties force C-FS3" and
"the displayed order-\(3,5,7\) formulas already forbid the slope deformation."
Not terminal for C-FS2/C-FS3 via a stronger actual-package theorem.
