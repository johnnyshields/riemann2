# UV-023 Filtration Source Map

Base commit in brief: `d510b97`.

## Proved in audited source

- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` defines the analytic
  corrected-whitening transfer `\mathcal T_{Q,R}(X)` and gives the homogeneous
  expansion
  \[
  \mathcal T_{Q,R}(X)=\sum_{p\ge 1}\mathcal T_p(X)
  \]
  with coefficient bounds. This is a Banach-analytic expansion in the full
  perturbation triple. It is not a filtration theorem for the order-7 quotient
  component.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` proves a formal
  quadratic factorization after swap symmetry, exact one-amplitude collapse, and
  diagonal merger are supplied for an actual finite-order package.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12510` gives the
  collision-cancellation chart and the conditional edge-law template: analytic,
  swap-even, collision-vanishing defects have a `\delta^2` edge form.

## Conditional or target-only source

- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12255` rules out the naive
  source-summed whitened model and states that the remaining theorem needs a
  different lift/transport object; determinant-only routes are shear-blind.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12513-12584` lists same reduced
  image germ and collision-functoriality as conditional downstream programs, not
  closure theorems.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23072-23109` reduces the residual
  fixed-shear corner to package-level collapse inputs for actual finite-order
  two-pair defects. It does not prove the UV-023 septic quotient filtration.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:10790-10810` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:21293-21330` also phrase same
  reduced image / collision-functoriality as theorem targets rather than proved
  inputs.

## Missing for UV-023

- No audited line defines a canonical source-weight-linear actual two-atom input
  `X^{[1]}` through order 7.
- No audited line defines a bidegree `(1,1)` projection of the order-7 quotient
  cross-effect.
- No audited line proves that only `\mathcal T_2` contributes to the septic
  quotient channel.
- No audited line proves that every `\mathcal T_{p\ge3}` term is
  quotient-invisible through order 7.
- No audited line proves zero first collision derivative for the renormalized
  order-7 quotient cross-effect without importing diagonal merger, determinant
  scalarization, or downstream package coincidence.

## Sharp candidate lemma

Let `X^{[1]}(h)` be a source-weight-linear corrected block input through order
7, and let `C_7^q(m,\omega,\delta)` be the fixed-target order-7 quotient
component of the corrected-whitening cross-effect after subtracting any
source-honest diagonal term in the same quotient target. UV-023 needs:
\[
\partial_\delta C_7^q(m,\kappa\delta/2,\delta)\big|_{\delta=0}=0
\]
for bounded `\kappa`, equivalently the higher homogeneous transfers
`\mathcal T_{p\ge3}` have zero first collision derivative in the septic quotient
channel, or are quotient-invisible there through order 7.
