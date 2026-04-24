# UV-025 Package Language Source Map

## Existing language that is usable downstream

- `rh/proof_of_rh.tex:11459-11474` defines a schematic two-pair quotient odd
  germ decomposition
  `F_(a1,h1;a2,h2)=a1 F_h1+a2 F_h2+I_12`.  This is output-germ language,
  not a pre-whitening block triple.
- `rh/proof_of_rh.tex:11994-12009` gives the best reusable phrase:
  "the actual corrected two-pair finite-order package through order 7 admits a
  source-level realization" in
  `C \oplus f \oplus (f / C A5^f)`, with
  `F_h=(c(h),A5^f(h),[A7^f](h))`.  This can be reused to define the
  quotient-output package `P_2`.
- `rh/proof_of_rh.tex:12168-12189` isolates the desired output identities:
  swap symmetry, one-amplitude collapse, and diagonal merger.
- `rh/proof_of_rh.tex:12225-12227` explicitly says the remaining theorem must
  use a different lift/transport object, not the raw source-summed whitened
  coefficients.

## Existing language that supports a future B2 definition

- `rh/proof_of_rh.tex:1392-1415` defines corrected same-point and mixed blocks
  and their matrix whitening.
- `rh/proof_of_rh.tex:1569-1575` names the analytic whitening map
  `W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}`.
- `rh/proof_of_rh.tex:1693-1732` writes corrected blocks as baseline plus
  perturbations `R_\pm`, `\widetilde R`.
- `rh/proof_of_rh.tex:1784-1799` gives the matrix Frechet derivative.
- `rh/proof_of_rh.tex:2659-2787` gives one-pair scaled perturbations
  `D_Q(delta G_{\rho,\pm})`, `D_Q(delta N_\rho)` and shows pair-kernel
  linearity modulo higher pair-kernel terms.

## Missing for UV-025

- No inspected source line defines an actual two-atom pre-whitening corrected
  block triple
  `B_2(a1,h1;a2,h2)=(G_{2,-}^corr,N_2^corr,G_{2,+}^corr)` with source tags.
- No inspected source line defines a pair-kernel filtration `K` on that
  two-atom block.
- No inspected source line proves
  `Lin_K D_Q(B_2-B_0)=a1 L_h1+a2 L_h2`.
- Existing `P_2` language assumes quotient-output data after extraction; it
  does not construct the pre-whitening block that UV-024 needs.

## Classification

The missing object has two parts.

1. Definition addition: introduce `B_2`, source tags, and the pair-kernel
   filtration before whitening.
2. Theorem requiring new source computation: prove the pair-kernel-linear
   derivative identity and show the quotient-output package is induced by this
   block rather than assumed.
