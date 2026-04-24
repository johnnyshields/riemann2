# Follow-up report: C-FS2 actual-formula inspection

## Claim

Route B actual-formula inspection yields a scoped negative, not C-FS2 closure. The paper does not currently define an actual corrected two-atom fixed triple
\[
(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
\]
as an analytic germ, so unconditional C-FS2 cannot be proved from the draft. More strongly, the order-
\(3,5,7\) formula neighborhoods expose a C-visible place where relational/provenance-sensitive data can enter without adding a new codomain coordinate: the septic quotient-defect representative \(R\) contributes through
\[
\det(R,A_{5,1}^{\mathfrak f}),
\]
and the centered order-
\(7\) determinant coefficients are explicitly \(\kappa\)-linear. Thus the actual displayed formulas do not forbid a \(c^2\varepsilon\kappa\) deformation of \(\Delta^{\corr}\); they leave exactly such determinant-level slope/provenance dependence open unless a separate diagonal-merger or state-locality theorem controls the septic quotient defect.

## Status

computational

## Evidence

### 1. No actual two-atom fixed triple is paper-defined

The draft defines the one-pair fixed-sector package and proves raw septic gauge elimination at the one-pair quotient/determinant level. It also states conditional two-pair source criteria. But the searched paper neighborhoods do not define
\[
\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})
\]
as an actual corrected two-atom analytic germ. Source audit already flags the fixed triple as a theorem-ready schema, not a paper-defined object.

### 2. The defect-thickened identity exposes the determinant slot for hidden C-data

In the quantitative defect-thickened strengthened coincidence theorem, the third coordinate obeys
\[
\frac{\Delta_1}{c_1^2}-\frac{\Delta_2}{c_2^2}
=
\frac{-\lambda c_2^2\det(A_{7,2}^{\mathfrak f},E)+c_2^2\det(R,A_{5,1}^{\mathfrak f})+\Delta_2(2\lambda c_2 e-e^2)}{c_1^2c_2^2},
\]
where \(e=E_{12}^{(3)}/a_1\), \(E=E_{12}^{(5)}/a_1\), and \(R\) represents \(-a_1^{-1}\overline E_{12}^{(7;1)}\). The determinant
\[
\det(R,A_{5,1}^{\mathfrak f})
\]
is independent of quotient representative, so it is a legitimate fixed scalar in the C codomain. But \(R\) is not computed for the actual corrected two-atom exceptional divisor. Therefore a relational/provenance-sensitive septic quotient defect can survive as a scalar contribution to \(\Delta^{\corr}\) unless a theorem controls it.

### 3. The centered order-
\(7\) formulas visibly permit \(\kappa\)-linear determinant dependence

The centered Taylor package gives
\[
\Delta_7(s)=D_2s^2+D_4s^4+D_6s^6+\cdots,
\qquad
D_2=\widehat U_1V_1-U_1\widehat V_1.
\]
The displayed formulas for \(\widehat U_1\) and \(\widehat V_1\) both contain a global \(2\kappa\) factor. Abstracting the bracketed channel forms as \(A\) and \(B\),
\[
D_2=2\kappa(A V_1-B U_1).
\]
The paper does not state an identity forcing \(A V_1-B U_1=0\). The check script confirms this formal coefficient structure.

Script:
`/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/centered_delta_kappa_check.py`

Output:

```text
D2 = 2*A*V1*kappa - 2*B*U1*kappa
dD2/dkappa = 2*A*V1 - 2*B*U1
generic_nonzero_condition = 2*(A*V1 - B*U1)
example_value = 2*k
```

This supports the scoped negative: the displayed actual order-
\(7\) template does not forbid \(\kappa\)-linear third-coordinate dependence.

### 4. Three-bin result

- [proved] The draft removes raw septic representative gauge from the one-pair C-level determinant \(\Delta_7\), and pure same-point septic terms vanish in the odd two-point germ.
- [proved/computational] The actual displayed order-
  \(7\) determinant template contains \(\kappa\)-linear transport/provenance channels, and the C-relevant determinant slot \(\det(R,A_5^{\mathfrak f})\) can carry scalar quotient-defect data.
- [missing] No source constructs the actual two-atom fixed triple, computes \(R\) on the exceptional divisor, or proves that \(\det(R,A_5^{\mathfrak f})\) is determined by the reduced base rather than by relational/provenance data.

## Baseline / delta

Baseline: the previous follow-up proved by formal countermodel that C-FS3 cannot be derived from fixed codomain, \(\mathcal R\), blow-up analyticity, swap-evenness, or scalar normalization. The new task asked whether actual order-
\(3,5,7\) formulas forbid that deformation or reveal extra C-state.

Delta: the actual formulas do not forbid it. They show two concrete source-backed mechanisms for the same obstruction: the uncomputed septic quotient-defect representative \(R\) enters the third \(\widehat\Psi\) coordinate by \(\det(R,A_5^{\mathfrak f})\), and the centered order-
\(7\) determinant coefficients are generically \(\kappa\)-linear. This advances the negative from “formal axioms permit \(B_3=Z+\varepsilon\kappa\)” to “the displayed order-
\(7\) formula language contains an unclosed determinant channel capable of carrying such dependence.”

## Attempt status

keep

## Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7004-7191` — one-pair fixed-sector package, projected septic gauge law, \(\Delta_7\) invariance.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7500-7924` — explicit septic \(K_1\) fixed-sector formulas, \(\Delta_{7,K_1}\), nonzero direct septic witness, quotient-septic closure.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` — defect-thickened third-coordinate identity and determinant term \(\det(R,A_{5,1}^{\mathfrak f})\).
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11888-12228` — source-level criterion remains conditional; naive source-summed model cannot prove one-amplitude linearity.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12230-12255` — quotient/single-determinant routes are shear-blind; mixed burden is source-coupled.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:12385-12511` — collision-cancellation chart and WIP parity/projective factorization.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:23294-23409` — centered Taylor package; \(\widehat U_1\), \(\widehat V_1\), and \(D_2,D_4,D_6\).
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/notes/actual-formula-inspection-CFS2.md` — detailed inspection note.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/scripts/centered_delta_kappa_check.py` — coefficient check script.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md` — prior formal \(B_3=Z+\varepsilon\kappa\) countermodel.

## Dependencies

- The source-backed negative depends on the defect-thickened algebra for \(\widehat\Psi\), especially the quotient-defect representative \(R\).
- It depends on the centered Taylor package formulas for \(u_5,v_5,u_{7,K_1},v_{7,K_1}\) and \(D_2\).
- It depends on the absence, in the audited paper neighborhoods, of an actual constructed \(\mathfrak P_2^{\corr}\) fixed triple or a diagonal-merger identity for its exceptional divisor.
- It does not claim the actual package necessarily has nonconstant \(B\); it claims the displayed formulas do not exclude such dependence and identify where it can enter.

## Strongest objection

The centered \(D_2\) formulas are local and belong to a centered symmetric-placement branch, not the full corrected two-atom exceptional-divisor package. Also, \(R\) in the defect-thickened theorem is an abstract representative of a quotient defect, not a computed actual package component. Therefore the report does not prove a real counterexample to C. It proves a scoped negative: the actual displayed order-
\(3,5,7\) formula language leaves a determinant-level relational/slope channel open, and no cited paper identity kills it.

## Needed for promotion

1. File/carry forward the negative: actual order-
   \(3,5,7\) formulas do not forbid \(c^2\varepsilon\kappa\)-type slope dependence; the uncomputed septic quotient-defect determinant \(\det(R,A_5^{\mathfrak f})\) is the C-visible carrier.
2. To prove C-FS2 positively, construct \(\mathfrak P_2^{\corr}\) and prove its order-
   \(7\) quotient defect representative \(R\) is determined by the fixed C triple and carries no relational/provenance data beyond \(\Delta^{\corr}\).
3. To prove C-FS3, additionally prove \(\det(R,A_5^{\mathfrak f})\) has no exceptional-divisor \(\kappa\)-dependence except that forced by the merged one-pair value. Equivalently, identify the actual formula that sets \(A V_1-B U_1=0\) in the centered coefficient template or prove a package-level merger theorem making that cancellation automatic.
4. Source and adversarial verifiers should test any future C closure against the determinant-slot deformation \(R\mapsto R+R_\kappa\) with \(\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa\).

## Honest verdict

C-FS2 is not proved. The strongest honest return is a source-backed negative/countermodel shape: the fixed C codomain removes raw septic gauge but does not remove determinant-level relational/provenance dependence. The actual formula neighborhoods leave the septic quotient-defect scalar \(\det(R,A_5^{\mathfrak f})\) uncomputed, and the centered determinant coefficients visibly permit \(\kappa\)-linear terms. A future proof must control that determinant slot by genuine actual-package construction plus diagonal merger.

## Autoresearch next step

continue: try to isolate a theorem precisely about the quotient-defect representative \(R\): either compute \(R\) for the actual corrected two-atom package on the exceptional divisor, or prove that \(\det(R,A_5^{\mathfrak f})\) factors through the descended collision state. This is the smallest C-FS2/C-FS3 overlap target.

verify: adversarially test proposed closures by adding an exceptional quotient-defect perturbation \(R_\kappa\) satisfying \(\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa\); source-check whether any actual formula forbids such \(R_\kappa\).

blocked: no coordinator blocker. Mathematical blocker is the missing actual computation or functoriality theorem for the septic quotient-defect determinant slot.

terminal: terminal for the subroute “actual order-
\(3,5,7\) formulas already forbid the \(c^2\varepsilon\kappa\) deformation.” They do not, from the audited scope. Not terminal for C overall.
