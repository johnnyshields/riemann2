# Source check: C-FS2/C-FS3 formal countermodel

Date: 2026-04-24

Audited files:

- `agents/20260424-160000-gap-closer-C-fiber-selection/report-cfs23-followup.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/notes/formal-countermodel-CFS23.md`
- `agents/20260424-160000-gap-closer-C-fiber-selection/scripts/formal_countermodel.py`

Script rerun output:

```text
R = (Y, X, Z + eps*kappa + r*t)
B = (Y, X, Z + eps*kappa)
swap_invariant = True
dB3/dkappa = eps
B_at_kappa_0 = (Y, X, Z)
```

Source verdict:

- The countermodel stays within the currently audited weak formal properties: fixed codomain, reduction `\mathcal R`, blow-up analyticity in `(m,\kappa,t)` with `t=\delta^2`, swap-evenness in the blown-up chart, scalar-normalization degrees, and central-slope match.
- It does not claim realizability by the actual corrected two-atom formulas; this scope is stated correctly.
- I found no paper line, apart from the explicitly missing diagonal merger / same-reduced-image-germ / collision-functoriality targets, that forbids adding `c^2\varepsilon\kappa` to `\Delta` at the formal fixed-codomain level.

Key paper refs:

- `rh/proof_of_rh.tex:11368-11450`: `\widehat\Psi` and scaling; does not force `\kappa`-independence.
- `rh/proof_of_rh.tex:11888-12189`: diagonal merger is an input, not proved.
- `rh/proof_of_rh.tex:12385-12511`: `\kappa=2\omega/\delta` chart and parity/projective factorization are WIP/reduction.
- `rh/proof_of_rh.tex:12513-12560` and `12562-12584`: same reduced image germ / collision-functoriality remain conditional downstream targets.
- `rh/proof_of_rh.tex:10780-10844`: quotient-level order-7 closure remains locally free; successful route must be provenance-sensitive.
