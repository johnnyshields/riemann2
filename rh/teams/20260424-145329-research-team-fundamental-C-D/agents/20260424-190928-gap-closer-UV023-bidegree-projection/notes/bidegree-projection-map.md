# UV-023 bidegree projection map

Base brief: `9cf771b`; team dispatch section
`UV-023 bidegree / grading attack 20260424-190928`.

## Source bins

- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` defines the
  corrected-whitening transfer
  `\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)` for a weighted perturbation
  triple `X=(X_-,Y,X_+)`. The grading there is homogeneous degree in `X`, not a
  source-weight bidegree in two atom tags.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2429-2467` defines
  `\mathfrak D_Q` as an entrywise matrix scaling used to normalize perturbation
  triples. It does not define a source bidegree projector.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2536-2551` gives
  coefficient bounds for `T_{p,n}`. These bounds do not preserve or project
  source bidegree.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` gives
  quadratic two-point factorization once an actual package has swap symmetry,
  exact one-amplitude collapse, and diagonal merger. It is not a source-defined
  bidegree projection for the corrected-whitening cross-effect.
- Source negative: `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rules out the naive source-summed corrected block model as the needed
  source-weight-linear input; its extracted coefficients are even in the source
  weight.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12584`,
  `21293-21330`, and `23072-23109` put the needed package-level
  functoriality/collapse on the downstream target list.

## Formal bidegree calculation

If a source-weight-linear input existed in the form
`X=a_1X_1+a_2X_2`, then the homogeneous cross-effect
\[
\mathcal T_p(a_1X_1+a_2X_2)-\mathcal T_p(a_1X_1)-\mathcal T_p(a_2X_2)
\]
has mixed source bidegrees `(i,p-i)` for `1<=i<=p-1`. Therefore the
source-bidegree `(1,1)` projection keeps only `p=2` and kills every
`\mathcal T_{p\ge3}` formally.

The harness
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190928-gap-closer-UV023-bidegree-projection/scripts/bidegree_projection_check.py`
records exactly this:

```text
p=2 mixed_bidegrees=[(1, 1)] projection_11={(1, 1): 2}
p=3 mixed_bidegrees=[(1, 2), (2, 1)] projection_11=none
p=4 mixed_bidegrees=[(1, 3), (2, 2), (3, 1)] projection_11=none
bidegree_11_kills_p_ge_3_formally = True
requires_source_defined_projection_before_quotient = true
requires_commutation_with_order7_quotient_extraction = true
```

This proves only the formal algebraic reduction. It does not supply the missing
source object.

## Smallest missing source statement

**Source-bidegree quotient-compatibility lemma.** Let `X^{[1]}_h` be the actual
source-weight-linear corrected-block perturbation through order `7`, and let
`Q_7^q` be the fixed-target order-7 quotient extraction used for UV-010 before
determinant scalarization. There is a source-defined projection `\Pi_{1,1}` on
the two-atom source variables such that
\[
Q_7^q\bigl(\operatorname{Cross}_{\mathcal T}(X^{[1]}_1,X^{[1]}_2)\bigr)
=
Q_7^q\bigl(\Pi_{1,1}\operatorname{Cross}_{\mathcal T}(X^{[1]}_1,X^{[1]}_2)\bigr),
\]
or equivalently every non-`(1,1)` source bidegree is quotient-invisible through
septic order.

Under this lemma, only the quadratic homogeneous transfer `\mathcal T_2` can
contribute to the septic quotient first-collision channel. The current source
does not define `X^{[1]}`, `\Pi_{1,1}`, or the commutation of `\Pi_{1,1}` with
`Q_7^q`.
