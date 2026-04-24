# UV-024 A5 Gauge Source Map

## Proved from inspected source

- `rh/proof_of_rh.tex:6976-7062` defines the fixed-sector projection
  `\pi_{\mathfrak f}`, the one-pair fixed-sector coefficients
  `A_5^{\mathfrak f}`, `A_7^{\mathfrak f}`, and the quotient
  `\mathfrak f/\mathbf C A_5^{\mathfrak f}`.
- `rh/proof_of_rh.tex:7065-7191` proves the projected septic gauge law:
  an admissible one-pair normalization change shifts
  `A_7^{\mathfrak f}` by `c_2 A_5^{\mathfrak f}`, so the determinant
  coordinate is invariant.
- `rh/proof_of_rh.tex:7742-8033` proves one-pair quotient-septic closure:
  the `K_5` shadow is `A_5^{\mathfrak f}`-gauge and the `K_1` slice carries
  the one-pair quotient class.
- `rh/proof_of_rh.tex:11888-12255` keeps the actual source-coupled two-pair
  package conditional and warns that quotient/determinant-only routes are
  shear-blind.

## Conditional or missing

- The projected septic gauge law is a one-pair representative-gauge statement.
  It does not say that a two-atom non-`(1,1)` source bidegree lands in
  `\mathbf C A_5^{\mathfrak f}(m)`.
- The one-pair `K_5` gauge statement does not apply to a cubic finite-order
  two-source witness of type `(1,1,5)` unless the actual source-linear
  corrected-whitening package identifies that witness with a `K_5` shadow.
- The inspected source does not state the needed theorem:
  for every actual non-`(1,1)` cubic order-7 source term `T`,
  `B_7^{\mathfrak f}(T)\in\mathbf C A_5^{\mathfrak f}(m)`.

## Script result

`scripts/a5_gauge_witness_check.py` models the tested formal constraints:
positive support in both sources, total order `1+1+5=7`, swap symmetrization,
and one-pair `A_5` gauge invariance.

The witness vector `(3,7)` against `A_5=(2,5)` has determinant
`3*5-2*7=1`, hence is not `A_5`-gauge.  Adding a gauge shift leaves the
determinant invariant.  Symmetric doubling gives determinant `2`; the prior
generic mirrored-pair sum `(3,7)+(4,6)=(7,13)` gives determinant `9`.

Conclusion from the harness: the inspected constraints do not kill the cubic
`(1,1,5)` witness.  A real proof needs a source-specific theorem, not
determinant bookkeeping or scalar invisibility after `\Phi_K`.
