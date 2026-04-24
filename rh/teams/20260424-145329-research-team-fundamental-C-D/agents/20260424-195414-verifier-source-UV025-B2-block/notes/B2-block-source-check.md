# UV-025 B2 Block Source Check

## Candidate checked

Source note checked:
`agents/20260424-194928-gap-closer-UV025-B2-definition/notes/B2-definition-block.md`.

The candidate defines source-tagged variables
`d_\pm^{(2)}`, `e_\pm^{(2)}`, `g_\pm^{(2)}`, and `\eta^{(2)}` as additive sums
of one-atom contributions with formal tags `\tau_i`, then substitutes
`q_{2,\pm}=q_{0,\pm}+d_\pm^{(2)}` and
`\Delta_2=\Delta_0+\eta^{(2)}` into the existing corrected same-point and mixed
block formulas.

## Source match

- `proof_of_rh.tex:2617-2626` defines the one-pair phase variables
  `d_\pm`, `e_\pm`, `g_\pm`, and `\eta` after midpoint affine-jet removal.
- `proof_of_rh.tex:2628-2636` writes those variables in the kernels
  `U_\pm`, `E_\pm`, `G_\pm`, and `V`.
- `proof_of_rh.tex:2688-2699` uses exactly
  `q=q_0+d_\pm`, `q'=q_0'+e_\pm`, `q''=q_0''+g_\pm` in the same-point block.
- `proof_of_rh.tex:2724-2742` uses exactly
  `q_\pm=q_{0,\pm}+d_\pm` and `\Delta=\Delta_0+\eta` in the mixed block.

Thus the candidate uses the same corrected phase variables and the same block
formulas as the one-pair source bookkeeping, with source tags added before
linear projection.

## K-linear theorem

The theorem follows for the defined tagged block:

- Same-point entries are linear in `d_\pm`, `e_\pm`, `g_\pm` modulo terms with
  at least two pair kernels by `proof_of_rh.tex:2700-2722`.
- Mixed-block entries are obtained by Taylor expansion in
  `(d_-,d_+,\eta)`, with a linear bounded-baseline part and a quadratic
  remainder, by `proof_of_rh.tex:2744-2787`.
- Since the tagged variables are additive sums of source-one and source-two
  variables, the degree-one part in the filtration counting each tagged kernel
  has no mixed products.  Mixed products first appear in degree at least two.

So
`Lin_K D_Q(B2-B0)=tau1 a1 L_h1 + tau2 a2 L_h2`
is source-supported once `B2`, `K`, and `L_h` are defined.

## Caveat

This verifies UV-025 only at the pre-whitening block level.  It does not identify
the later whitened finite-order quotient package, does not prove UV-024's
coefficient map compatibility, and does not prove UV-026's cubic `(1,1,5)`
`A5^f`-gauge theorem.

Recommended wording fix: call `B2` the "tagged pre-whitening corrected source
lift" or explicitly state that "actual" here means actual for the pre-whitening
block formulas, not yet actual for the downstream quotient-output package.
