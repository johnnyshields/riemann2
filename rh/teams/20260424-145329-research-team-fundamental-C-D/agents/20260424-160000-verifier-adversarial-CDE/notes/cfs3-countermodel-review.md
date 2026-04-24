# C-FS3 countermodel review

Reviewed on 2026-04-24:

- `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/notes/formal-countermodel-CFS23.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/scripts/formal_countermodel.py`
- `rh/proof_of_rh.tex:11368-11585`
- `rh/proof_of_rh.tex:11888-12228`
- `rh/proof_of_rh.tex:12385-12511`

I reran the script:

```text
R = (Y, X, Z + eps*kappa + r*t)
B = (Y, X, Z + eps*kappa)
swap_invariant = True
dB3/dkappa = eps
B_at_kappa_0 = (Y, X, Z)
```

Verdict: the countermodel is valid as a scoped negative. It proves that C-FS3 cannot be derived from the listed formal properties alone:

- fixed C codomain `\mathbf C\times\mathfrak f\times\mathbf C`;
- reduction `\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)`;
- blow-up analyticity in `(m,\kappa,t)` with `t=\delta^2`;
- swap-evenness in the blown-up chart;
- homogeneous scalar normalization of degrees `(1,1,2)`;
- central-slope match `B(m,0)=\widehat\Psi(m)`.

No audited paper assumption among the checked lines forbids the `\varepsilon\kappa` term. The relevant paper lines instead state diagonal merger / diagonal collapse as an extra missing input:

- `rh/proof_of_rh.tex:11888-12189` makes diagonal merger a hypothesis of the source-level criterion.
- `rh/proof_of_rh.tex:12042-12166` makes diagonal collapse an assumption of the weaker quotient route.
- `rh/proof_of_rh.tex:12192-12228` warns the naive source-summed route cannot supply one-atom linearity.
- `rh/proof_of_rh.tex:12447-12511` gives parity/projective factorization for defects, compatible with `\kappa`-dependent edge data; it does not impose slope independence.

Scope caveat: the model does not show the actual corrected package has nonconstant `B`; it only shows the weaker formal package properties do not exclude it. A real collision-functoriality / diagonal-merger theorem would kill the model, but that is exactly the missing C-FS3 theorem.
