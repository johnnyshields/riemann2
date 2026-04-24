# C-FS2 actual-formula negative review

Reviewed on 2026-04-24:

- `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs2-actual-formulas.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/notes/actual-formula-inspection-CFS2.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/scripts/centered_delta_kappa_check.py`
- `rh/proof_of_rh.tex:11587-11775`
- `rh/proof_of_rh.tex:11888-12228`
- `rh/proof_of_rh.tex:12230-12511`
- `rh/proof_of_rh.tex:23294-23409`

I reran the script:

```text
D2 = 2*A*V1*kappa - 2*B*U1*kappa
dD2/dkappa = 2*A*V1 - 2*B*U1
generic_nonzero_condition = 2*(A*V1 - B*U1)
example_value = 2*k
```

Verdict: the follow-up is a valid scoped negative. The checked formula neighborhoods do not forbid the verified `c^2\varepsilon\kappa` deformation.

Key checks:

1. `rh/proof_of_rh.tex:11603-11775` explicitly introduces a representative `R` of the septic quotient defect and shows the C-visible third-coordinate slot `\det(R,A_{5,1}^{\mathfrak f})`. The proof only shows this determinant is representative-independent; it does not compute `R` or force it to be base-determined.
2. `rh/proof_of_rh.tex:11888-12189` makes one-amplitude collapse and diagonal merger assumptions of the source-level criterion. It does not prove them.
3. `rh/proof_of_rh.tex:12192-12228` says the naive source-summed whitened coefficients cannot supply one-amplitude linearity / coincident additivity, so it does not control `R`.
4. `rh/proof_of_rh.tex:12230-12255` warns quotient/single-determinant routes are shear-blind and the burden is source-coupled. That supports, rather than forbids, hidden relational/provenance dependence.
5. `rh/proof_of_rh.tex:12447-12511` gives parity/projective factorization and edge laws with explicit `\kappa`-dependent terms; no slope-independence result appears there.
6. `rh/proof_of_rh.tex:23345-23408` gives `\widehat U_1=2\kappa A`, `\widehat V_1=2\kappa B` in abstracted notation and `D_2=\widehat U_1V_1-U_1\widehat V_1`; no identity forces `AV_1-BU_1=0`.

Scope caveat: the centered determinant package is local and not the full actual two-atom fixed C triple; `R` is a quotient-defect representative, not a computed package component. Thus this is not a counterexample to C, only a negative against the claim that the displayed formulas already prove C-FS2 or forbid C-FS3 slope dependence.
