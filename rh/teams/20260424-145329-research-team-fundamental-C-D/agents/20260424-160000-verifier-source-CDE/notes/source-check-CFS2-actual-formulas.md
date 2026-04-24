# Source check: C-FS2 actual-formula inspection

Date: 2026-04-24

Audited files:

- `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/notes/actual-formula-inspection-CFS2.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/scripts/centered_delta_kappa_check.py`

Script rerun output:

```text
D2 = 2*A*V1*kappa - 2*B*U1*kappa
dD2/dkappa = 2*A*V1 - 2*B*U1
generic_nonzero_condition = 2*(A*V1 - B*U1)
example_value = 2*k
```

Source verdict:

- Supported: the paper defines the one-pair fixed-sector package and quotient-septic closure, not an actual two-atom fixed triple `\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`. Exact string searches for `C^{\corr}`, `A^{\mathfrak f,\corr}`, `Delta^{\corr}`, and `mathfrak P_2^{\corr}` found no paper definition.
- Supported: `rh/proof_of_rh.tex:11625-11669` and proof lines `11705-11774` expose `\det(R,A_{5,1}^{\mathfrak f})` as a representative-independent scalar in the third `\widehat\Psi` coordinate. The source does not compute `R` for an actual exceptional-divisor corrected two-atom package.
- Supported: centered formulas `rh/proof_of_rh.tex:23337-23408` give `\widehat U_1=2\kappa A`, `\widehat V_1=2\kappa B` in bracket shorthand and `D_2=\widehat U_1V_1-U_1\widehat V_1`, hence `D_2=2\kappa(AV_1-BU_1)`. I found no identity at those lines forcing `AV_1-BU_1=0`.
- Scope: this is a source-backed negative, not an actual counterexample. The centered formulas are local; `R` is an abstract quotient-defect representative. The claim is only that the cited paper neighborhoods do not forbid the determinant-level `\kappa` channel and do not prove C-FS2.

Key paper refs:

- `rh/proof_of_rh.tex:7004-7191`, `7540-7924`: one-pair fixed-sector package, determinant, direct septic slice, quotient-septic closure.
- `rh/proof_of_rh.tex:11587-11775`: defect-thickened identity with `\det(R,A_{5,1}^{\mathfrak f})` and representative-independence.
- `rh/proof_of_rh.tex:12192-12255`: naive source-summed model obstruction and shear-blindness of quotient/single-determinant routes.
- `rh/proof_of_rh.tex:12385-12511`: collision chart and WIP parity/projective factorization.
- `rh/proof_of_rh.tex:23294-23409`: centered Taylor package and `D_2` formula.
