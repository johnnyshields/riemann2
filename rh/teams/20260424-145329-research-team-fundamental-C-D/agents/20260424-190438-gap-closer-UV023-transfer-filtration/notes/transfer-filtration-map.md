# UV-023 transfer-filtration map

Base brief: `d510b97`; team dispatch section `UV-023 transfer-filtration attack 20260424-190438`.

## Source bins

- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` defines the
  corrected-whitening transfer
  `\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)` and gives the coefficient
  bound for `T_{p,n}`.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2555-2587` proves only
  uniform analyticity and the homogeneous expansion. It does not give a
  vanishing or quotient-filtration statement for `\mathcal T_{p\ge3}`.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` makes the
  quadratic factor formal only after an actual package has swap symmetry,
  one-amplitude collapse, and diagonal merger.
- Proved negative: `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  says the naive source-summed whitened package is even in source weight, so it
  cannot be the source-weight-linear input needed for UV-022/UV-023.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:12447-12469` gives the
  collision edge template only for an already-defined analytic, swap-even, and
  collision-vanishing defect.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:12541-12559`,
  `21752-21763`, `22472-22504`, and `23072-23109` describe package-level
  state-locality, merger, or collision-functoriality as downstream hypotheses,
  not proved filtration.

## Order-count result

The coefficient bound allows `\mathcal T_{p\ge3}` to contribute to `T_{p,n}`
with `n<=7` unless the source-weight-linear input has `w`-order at least `3`.
The smallest witnesses are:

- input order `0`: `p=3`, `n=0`;
- input order `1`: `p=3`, `n=3`;
- input order `2`: `p=3`, `n=6`;
- input order `3`: no `p>=3` contribution through order `7`.

Thus a positive source proof needs one of:

1. a source theorem that the actual `X^{[1]}` is `w^3`-divisible in the quotient
   channel relevant to the septic output;
2. a quotient-projection theorem annihilating the `\mathcal T_{p\ge3}` output
   through order `7`;
3. an explicitly defined bidegree `(1,1)` source-weight projection, with a
   proof that the actual order-7 quotient package equals this projection.

The third route is algebraically clean: the full cross-effect of a homogeneous
degree `p` transfer has mixed source bidegrees `(i,p-i)`, `1<=i<=p-1`; only
`p=2` contains bidegree `(1,1)`. The paper does not currently define such a
projection for the actual corrected order-7 quotient package.

## Minimal missing lemma

**Septic homogeneous-transfer filtration lemma.** Let `X^{[1]}_h` be the actual
source-weight-linear corrected-block perturbation through order `7`. In the
UV-010 good-patch quotient chart, the order-7 quotient component of the
renormalized corrected-whitening cross-effect has zero first collision
derivative. Equivalently, its septic quotient first-collision channel is
computed by the bidegree `(1,1)` / quadratic homogeneous transfer
`\mathcal T_2(X^{[1]}_1,X^{[1]}_2)` alone, while every
`\mathcal T_{p\ge3}` contribution is quotient-invisible through order `7`.

The current paper provides the analytic ambient transfer and the downstream
edge template, but not this lemma.
