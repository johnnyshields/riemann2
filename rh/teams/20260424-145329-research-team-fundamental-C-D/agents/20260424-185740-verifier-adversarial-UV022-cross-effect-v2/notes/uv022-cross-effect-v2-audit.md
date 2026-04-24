# UV-022 cross-effect v2 adversarial audit

Base commit: `f9be20c1d56806a5a44de2e03758de6dafea76fb`.

I inspected the abandoned scratch script
`agents/20260424-184643-verifier-adversarial-UV022-cross-effect/scripts/uv022_cross_effect_adversarial_check.js`
only as scratch input. The cited computation for this replacement pass is
`scripts/uv022_cross_effect_v2_adversarial_check.js`.

## Ground-truth check

The UV-022 route must survive four tests:

- diagonal subtraction must imply the required `delta^2` edge divisibility in
  the order-7 quotient component;
- the subtraction must not import same-reduced-image or diagonal merger as a
  hidden assumption;
- determinant scalarization must not hide an unforced quotient edge coordinate;
- the formal `a_1a_2 delta^2 P(m,kappa)` model must be killed by source
  structure, not by choosing a counterterm that already knows `P`.

## Result

The current diagonal-counterterm route is not source-justified.

The formal diagonal subtraction
\[
C(a_1,h_1;a_2,h_2)-C(a_1,m;a_2,m)
\]
kills the literal diagonal value. For a nonlinear analytic corrected-whitening
cross-effect, that is not enough to force `delta^2` divisibility: higher
amplitude terms leave first-order-in-`delta` pieces unless an additional
bidegree `(1,1)` / source-weight-linearity theorem is supplied.

In the restricted scalar model where the source-honest diagonal term is exactly
the `delta=0` value, the corrected expression becomes `a_1a_2 delta^2 P`. This
has the edge form, but the free `P(m,kappa)` survives. Killing `P` requires a
counterterm depending on the off-diagonal/free quotient term itself, which is
not a source-honest diagonal counterterm.

Determinant bookkeeping is representative-invariant on
`A_5^{\mathfrak f}(m) != 0`, but it does not remove the free edge value. At
`A_5^{\mathfrak f}=0`, the rank jump remains.

## Script output excerpt

```text
renorm_one_amplitude_left_zero = true
renorm_one_amplitude_right_zero = true
renorm_swap_difference_zero = true
raw_diagonal_zero = false
renorm_diagonal_zero = true
renorm_delta2_divisible = false
renorm_terms_below_delta2 = 28
corrected_edge_value = 180
free_P_survives_source_honest_counterterm = true
unsourced_full_counterterm_residual = 0
unsourced_full_counterterm_is_source_honest = false
determinant_chart_free_edge_value = 180
determinant_chart_kills_free_P = false
A5_zero_rank_jump_detected = true
```
