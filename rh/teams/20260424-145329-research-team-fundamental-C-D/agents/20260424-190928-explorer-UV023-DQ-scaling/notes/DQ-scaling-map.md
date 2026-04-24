# UV-023 DQ Scaling Map

Own lane: `explorer-UV023-DQ-scaling`.

## Source bins

- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587` defines
  `\mathfrak D_Q`, the scaled perturbation triple, and the homogeneous
  corrected-whitening transfer
  `\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)`. The result is analytic
  and gives coefficient bounds. It is not a quotient-filtration theorem.
- Proved adjacent bookkeeping: `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2674`
  introduces actual one-pair weighted perturbation triples via
  `\mathfrak D_Q`, and `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2787`
  checks the actual corrected formulas. After scaling, some linear weighted
  entries have no forced positive `w`-order, while other entries start at
  `w` or `w^2`.
- Proved adjacent grading clue: `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-7835`
  shows that, for the one-pair quotient-septic determinant, the weight-one
  `q^{(7)}` slice is carried by the direct `K_1` transport sector. This is a
  positive clue for a quadratic/bidegree route, not a theorem about the
  two-atom corrected-whitening cross-effect.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` gives the
  formal quadratic two-point factor only after swap symmetry, exact
  one-amplitude collapse, and diagonal merger are supplied for an actual
  finite-order package.
- Proved negative: `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  says the naive source-summed whitened coefficients are even in source weight.
  They cannot supply the source-weight-linear input needed here.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12584`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:21293-21330`, and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:23072-23109` point to
  collision-functoriality, same reduced image, and package-level collapse as
  theorem targets, not proved inputs.

## Bookkeeping result

The script
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-190928-explorer-UV023-DQ-scaling/scripts/dq_scaling_filtration_check.py`
separates three filters.

1. `\mathfrak D_Q` scaling plus the coefficient bound does not exclude
   `\mathcal T_{p\ge3}`. Because the actual weighted inputs have channels with
   no forced positive `w`-order, a cubic homogeneous term can contribute through
   order `7`.
2. Finite-order grading by itself does not exclude higher homogeneous transfer:
   with the one-pair clue that `q^{(7)}` first appears at grade `5`, a cubic
   term with grades `(1,1,5)` can still reach septic grade `7`.
3. A true source bidegree `(1,1)` projection would kill every `p>=3`
   cross-effect term, because the mixed bidegrees of a homogeneous degree `p`
   term are `(i,p-i)`, `1<=i<=p-1`, and only `p=2` contains `(1,1)`.

## Minimal missing statement

The positive route is not raw `\mathfrak D_Q` scaling. The needed theorem is:
after defining the actual source-weight-linear corrected two-atom input
`X^{[1]}`, the order-7 quotient component of the corrected-whitening
cross-effect equals its source bidegree `(1,1)` part, or every
`\mathcal T_{p\ge3}` contribution is quotient-invisible through order `7`.

An alternative sufficient theorem would be stronger but less likely from the
current formulas: the actual quotient-visible `X^{[1]}` is `w^3`-divisible in
the channel feeding the septic output.
