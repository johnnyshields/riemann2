Claim

The C-FS2 actual-formula inspection is a valid scoped negative. The checked formula neighborhoods do not prove C-FS2 and do not forbid the previously verified `c^2\varepsilon\kappa` deformation. They expose a C-visible determinant channel
\[
\det(R,A_{5,1}^{\mathfrak f})
\]
for the septic quotient defect representative `R`, and the centered determinant template has generically nonzero `\kappa`-linear coefficient
\[
D_2=2\kappa(AV_1-BU_1).
\]
From the checked scope, no hidden paper assumption controls `R` or forces `AV_1-BU_1=0`.

Status

computational

Evidence

I reviewed the C-FS2 follow-up report, note, and script, then checked the cited paper neighborhoods. I reran the script:

```text
D2 = 2*A*V1*kappa - 2*B*U1*kappa
dD2/dkappa = 2*A*V1 - 2*B*U1
generic_nonzero_condition = 2*(A*V1 - B*U1)
example_value = 2*k
```

The determinant-slot claim is sourced. In `rh/proof_of_rh.tex:11603-11775`, the defect-thickened strengthened-coincidence theorem chooses a representative `R` of the quotient class `-a_1^{-1}\overline E_{12}^{(7;1)}` and derives
\[
\frac{\Delta_1}{c_1^2}-\frac{\Delta_2}{c_2^2}
=
\frac{-\lambda c_2^2\det(A_{7,2}^{\mathfrak f},E)+c_2^2\det(R,A_{5,1}^{\mathfrak f})+\Delta_2(2\lambda c_2 e-e^2)}{c_1^2c_2^2}.
\]
The proof shows `\det(R,A_{5,1}^{\mathfrak f})` is independent of the representative of `R`. It does not compute `R` for the actual corrected exceptional divisor, and it does not state that this determinant is forced by the reduced base. Thus this is a legitimate C-coordinate slot where relational/provenance data can enter without adding a new codomain coordinate.

The likely hidden-assumption checks do not kill the slot. In `rh/proof_of_rh.tex:11888-12189`, one-amplitude collapse and diagonal merger are assumptions of the source-level criterion, not proved facts. In `rh/proof_of_rh.tex:12192-12228`, the naive source-summed route is explicitly ruled insufficient for one-amplitude linearity / coincident additivity. In `rh/proof_of_rh.tex:12230-12255`, quotient and single-determinant routes are described as shear-blind, with the remaining burden genuinely source-coupled. In `rh/proof_of_rh.tex:12447-12511`, parity/projective factorization allows `\kappa`-dependent edge data and does not assert slope independence.

The centered determinant claim also checks out at the level claimed. In `rh/proof_of_rh.tex:23345-23408`, both `\widehat U_1` and `\widehat V_1` have an overall `2\kappa` factor, and
\[
D_2=\widehat U_1V_1-U_1\widehat V_1.
\]
Abstracting the bracketed expressions as `A` and `B` gives `D_2=2\kappa(AV_1-BU_1)`. I found no identity in that neighborhood forcing `AV_1-BU_1=0`; the script confirms the generic nonzero condition.

Baseline / delta

Baseline: the previous verified countermodel showed that fixed codomain, `\mathcal R`, blow-up analyticity, swap-evenness, scalar normalization, and central-slope `\widehat\Psi` do not force C-FS3; `B_3=Z+\varepsilon\kappa` is a formal scoped countermodel.

Delta: this follow-up makes that negative source-backed. The displayed order-3/5/7 formula neighborhoods themselves leave a determinant-level channel capable of carrying the same slope dependence. The obstruction is not only formal freedom; the audited formula language contains uncomputed objects (`R`, and centered channel combination `AV_1-BU_1`) that would have to be controlled to exclude it.

Attempt status

keep

Exact refs

- C-FS2 follow-up report: `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md:1-141`.
- C-FS2 inspection note: `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/actual-formula-inspection-CFS2.md:1-98`.
- Script: `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/centered_delta_kappa_check.py:1-27`; rerun output quoted above.
- Prior verified C-FS3 countermodel review: `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/report-cfs3-countermodel-review.md`.
- This verifier note: `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-verifier-adversarial-CDE/notes/cfs2-actual-formula-review.md`.
- Paper: `rh/proof_of_rh.tex:11587-11775` for the defect-thickened third-coordinate identity and determinant `\det(R,A_{5,1}^{\mathfrak f})`.
- Paper: `rh/proof_of_rh.tex:11888-12189` for source-level merger as an assumption.
- Paper: `rh/proof_of_rh.tex:12192-12228` for the naive source-summed obstruction.
- Paper: `rh/proof_of_rh.tex:12230-12255` for quotient/single-determinant shear blindness.
- Paper: `rh/proof_of_rh.tex:12385-12511` for collision blow-up and parity/projective factorization.
- Paper: `rh/proof_of_rh.tex:23294-23409` for the centered determinant template and `D_2`.

Dependencies

- The negative is scoped to the audited formula neighborhoods and the abstracted centered-channel calculation.
- It does not construct the actual corrected two-atom fixed triple.
- It does not prove the actual package has nonconstant `B(m,\kappa)`.
- It depends on the absence, in the checked scope, of a theorem computing `R`, proving `\det(R,A_5^{\mathfrak f})` descends to the reduced base, or forcing `AV_1-BU_1=0`.

Strongest objection

The two pieces of evidence are not themselves an actual counterexample. The defect-thickened `R` is an abstract representative of a quotient defect, not a computed actual corrected-package component. The centered `D_2` template is local to a centered symmetric-placement branch, not the full exceptional-divisor package. A genuine package-level diagonal-merger, state-locality, or actual formula computation could still set `\det(R,A_5^{\mathfrak f})` to the base value and force `AV_1-BU_1=0`. But those are precisely the missing stronger theorems; I found no checked paper assumption that already supplies them.

Needed for promotion

- Capture as a negative: actual displayed order-3/5/7 formula neighborhoods do not by themselves prove C-FS2 or forbid `c^2\varepsilon\kappa` slope dependence.
- A positive C-FS2 theorem must construct the actual `\mathfrak P_2^{\corr}` fixed triple and show every C-visible determinant contribution is represented by `(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})` with no hidden relational/provenance state.
- A positive C-FS3 theorem must additionally compute or constrain the septic quotient-defect determinant slot, e.g. prove `\det(R,A_5^{\mathfrak f})` factors through the descended collision state and has no exceptional `\kappa`-dependence, or prove a package-level diagonal merger that forces this.
- Any future closure should be tested against the perturbation `R\mapsto R+R_\kappa` with `\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa`, and against the centered condition `AV_1-BU_1\neq0`.

Honest verdict

The C-FS2 follow-up survives adversarial review as a scoped negative. It does not disprove C for the actual corrected package, but it rules out the subroute “the displayed actual formulas already forbid the verified `c^2\varepsilon\kappa` deformation.” They do not. The live C target is now narrower: compute/control the septic quotient-defect determinant slot `\det(R,A_5^{\mathfrak f})` by actual package construction, state-locality, or diagonal merger.

Autoresearch next step

continue: attack or compute the actual exceptional-divisor quotient-defect representative `R`; if computation is not available, formulate the weakest state-locality theorem forcing `\det(R,A_5^{\mathfrak f})` to factor through the descended collision state.
verify: source verifier should check whether any later paper section defines `R` for the actual corrected package or proves the cancellation `AV_1-BU_1=0`; adversarial verifier should test all future C-FS2/C-FS3 claims against the `R_\kappa` determinant perturbation.
blocked: no process blocker; mathematical blocker is missing actual-package computation or merger theorem for the determinant slot.
terminal: terminal for the subroute “displayed order-3/5/7 formulas already forbid the slope deformation”; not terminal for C-FS2/C-FS3 via a stronger theorem.
