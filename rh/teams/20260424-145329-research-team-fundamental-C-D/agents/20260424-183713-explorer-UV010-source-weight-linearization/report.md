# Claim

The natural "signed source-weight lift" workaround does not by itself solve the
UV-010 package-definition problem. It restores oddness in the source amplitude,
but it still fails the exact one-amplitude collapse required by the source
criterion unless all higher \(a^3,a^5,\dots\) terms vanish or are removed by a
new justified projection.

The viable construction target is therefore narrower: define a package-level
linearization functor that extracts the source-amplitude linear coefficient, or
prove that the higher even-in-\(a\) terms are irrelevant in the order-7 quotient
interaction. The current paper does neither.

# Status

computational

# Evidence

Source basis:

- The paper identifies the naive obstruction at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`: corrected blocks have
  the form
  \[
  G^{\corr}_{a,h,\pm}(s)=a\mathcal G_{h,\pm}(a^2;s),
  \qquad
  N^{\corr}_{a,h}(s)=a\mathcal N_h(a^2;s),
  \]
  and whitening cancels the overall \(a\), leaving fixed finite-order
  coefficients even analytic in \(a\). That cannot satisfy exact one-amplitude
  linearity.
- The same remark states that the two-point theorem must use a different
  lift/transport object, not the raw source-summed whitened coefficients.

I tested the most obvious lift in
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183713-explorer-UV010-source-weight-linearization/scripts/source_weight_linearization_toy.js`.
The toy uses \(B(a)=a(F_0+F_2a^2+F_4a^4)\), \(W(a)=B(a)/a\), and candidates
\(W(a)\), \(aW(a)\), and \(aF_0\). Output:

```text
whitened_even_difference = 0
whitened_one_amplitude_error = 1138
signed_lift_odd_sum = 0
signed_lift_one_amplitude_error = 3456
linear_projection_one_amplitude_error = 0
higher_source_weight_terms = 3456
```

Three-bin separation:

- **proved/computational:** raw whitened coefficients are even in source weight;
  signed lift \(aW(a)\) is odd but still has higher \(a^3,a^5,\dots\) terms.
- **conditional:** the linear projection \(aF_0\) has exact one-amplitude
  collapse, but promoting it requires a theorem that this projection is the
  actual corrected two-atom finite-order package seen by the quotient odd germ.
- **missing:** no source line defines such a projection functor or proves that
  the higher source-weight terms are quotient-invisible at order 7.

# Baseline / delta

Baseline: the actual Hessian construction pass reduced UV-010 to the missing
definition of an actual two-atom order-7 package
\(\mathfrak P_{2,7}^{\corr}\) with linear one-amplitude collapse.

Delta: this pass tests the simplest way to get that linearity from existing
corrected block formulas. Multiplying the even whitened package by \(a\) is
insufficient. The only toy operation that satisfies exact one-amplitude collapse
is taking the source-weight linear coefficient, which is not currently a
paper-defined package.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227` - even-amplitude
  obstruction and need for a different lift/transport object.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932` - source criterion
  requiring exact one-amplitude collapse.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189` - exact finite-order
  source-level inputs still required for the corrected two-atom package.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:24520-24540` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:24998-25004` - later summaries
  repeat that the naive source-summed corrected block model does not prove the
  source criterion.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183418-gap-closer-UV010-actual-hessian-construction/report.md`
  - prior positive construction reduction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183713-explorer-UV010-source-weight-linearization/scripts/source_weight_linearization_toy.js`
  - toy parity/linearity harness.

# Dependencies

- The toy models only source-weight parity. It does not model the full corrected
  block matrices or the actual quotient odd germ.
- A real construction would need an invariant definition of the source-weight
  linear projection and a proof that it is functorial under whitening and
  quotient extraction.
- Any such projection must still produce the order-7 quotient interaction
  remainder and survive the \(a_1a_2\delta^2P(m,\kappa)\) adversarial test.

# Strongest objection

The signed lift might still be useful as part of a larger construction if the
higher \(a^3,a^5,\dots\) terms are absorbed by normalization, quotienting, or a
transport equivalence. This report does not rule that out. It rules out only the
simple claim that \(a\) times the even whitened coefficients already gives the
exact one-amplitude package required by the source criterion.

# Needed for promotion

1. Define a source-weight linear projection or lift/transport object on the
   corrected block triple.
2. Prove it is invariant under the allowed normalizations and commutes with
   extracting the cubic/quintic/septic quotient outputs.
3. Prove exact one-amplitude collapse
   \[
   \mathfrak P_2(0,h_1;a,h_2)=aF_{h_2},
   \qquad
   \mathfrak P_2(a,h_1;0,h_2)=aF_{h_1}.
   \]
4. Extract the order-7 quotient interaction component and apply the good-patch
   determinant chart.

# Autoresearch next step

continue: search for an invariant way to define the source-weight linear
coefficient of the corrected block triple, then test whether that coefficient
commutes with whitening and quotient extraction through order 7.

verify: any candidate must be source-checked against the even-amplitude
obstruction and adversarially tested against free septic quotient perturbations.

blocked: no process blocker. Mathematical blocker is the absence of a
paper-defined linearization functor.

terminal: terminal for the subroute "multiply the even whitened package by the
source amplitude and get exact one-amplitude collapse." Not terminal for a
proper linear-projection lift.
