# UV-026 Adversarial Witness Notes

## Fixed proof standard

UV-026 requires fixed-sector proportionality:

`B_7^{\mathfrak f}(T) \in \mathbf C A_5^{\mathfrak f}(m)`

for every actual non-`(1,1)` cubic finite-order source term `T` of type
`(1,1,5)`.

The following do not count:

- scalar invisibility under `\Phi_K`;
- determinant scalarization or good-patch chart bookkeeping;
- swap symmetry without a line-image theorem;
- one-pair projected gauge law without identifying the actual two-source term
  as `A_5^{\mathfrak f}`-gauge.

## Effect of UV-025

The staged UV-025 block in `paper-updates.md:21-32` explicitly says it is
pre-whitening, before `\Phi_K`, before determinant/quotient extraction, and
does not assert `B_7^{\mathfrak f}`, `Q_{7,m}^q`, or UV-026 gauge.  Its scope
remark at `paper-updates.md:131-138` repeats that UV-026 remains separate.

Therefore UV-025 supplies upstream source-linear provenance for the block input,
but it does not kill the cubic witness.

## Harness result

The local script keeps the prior witness:

- `A5=(2,5)`;
- cubic `(1,1,5)` witness vector `(3,7)`;
- determinant against `A5` equals `1`.

Stress tests:

- swap-symmetric vector `(6,14)` has determinant `2`;
- generic mirrored sum `(7,13)` has determinant `9`;
- adding `11 A5` gives `(25,62)` and still determinant `1`.

Conclusion: the witness remains a formal countermodel to shortcut proofs.  It
is not a genuine actual-package obstruction yet, because no source or staged
paper update computes `B_7^{\mathfrak f}` for the actual cubic term.
