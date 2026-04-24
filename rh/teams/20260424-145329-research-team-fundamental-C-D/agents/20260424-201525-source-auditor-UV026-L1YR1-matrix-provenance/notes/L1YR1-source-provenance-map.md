# UV-026 L1YR1 Source Provenance Map

## Nearest paper notation

- `proof_of_rh.tex:1693-1732` writes the first-order matrix whitening split.
  The paper names the inverse-square-root derivative outputs
  `X_-:=D(G^{-1/2})_{G_-^{(0)}}[R_-]` and similarly `X_+`; it does not name
  these `L_{-,i}` or `R_{+,i}`.
- `proof_of_rh.tex:1784-1799` displays only the first Frechet whitening term
  `D W_0[R_-, \widetilde R, R_+]`.
- `proof_of_rh.tex:1916-1927` gives the Loewner formula for the first derivative
  of `x^{-1/2}`.
- `proof_of_rh.tex:2458-2467` defines a weighted perturbation triple
  `X=(X_-,Y,X_+)` and `\delta G_\pm=D_Q^{-1}X_\pm`,
  `\delta N=D_Q^{-1}Y`, but this is the scalar transfer setup after
  `\Phi_K` is applied in the definition of `T_{Q,R}`.
- `proof_of_rh.tex:2653-2664` defines the one-pair scaled input
  `X_\rho=(X_{\rho,-},Y_\rho,X_{\rho,+})` with
  `X_{\rho,\pm}=D_Q(\delta G_{\rho,\pm})`, `Y_\rho=D_Q(\delta N_\rho)`.
- `paper-updates.md:94-109` stages the UV-025 source-linear input
  `Lin_K D_Q(B_2-B_0)=tau1 a1 L_h1+tau2 a2 L_h2`, but this `L_h` is a
  pre-whitening corrected-block triple, not the inverse-square-root factor
  `L_{-,i}^{[1]}` in the L1YR1 product notation.

## Translation of requested symbols

If the requested product is to be translated into paper notation, it should be:

- `L_{-,i}^{[1]}` = grade-1 part of the left inverse-square-root derivative
  output `D(G_-^{-1/2})[delta G_{i,-}]`.
- `Y_i^{[5]}` = grade-5 part of the scaled mixed input
  `Y_i=D_Q(delta N_i)`, before `Phi_K`.
- `R_{+,i}^{[1]}` = grade-1 part of the right inverse-square-root derivative
  output `D(G_+^{-1/2})[delta G_{i,+}]`.

This translation is not yet an existing formula in the paper.  It is the
smallest consistent dictionary from the read source.

## Missing source formula

The audited source does not contain the actual matrices

`L_{-,1}^{[1]}Y_1^{[5]}R_{+,2}^{[1]}`
+ `L_{-,1}^{[1]}Y_2^{[5]}R_{+,1}^{[1]}`
+ `L_{-,2}^{[1]}Y_1^{[5]}R_{+,1}^{[1]}`

nor the swapped tag expression.  It also does not compute their
`\pi_f [z^7]` fixed-sector projection or prove proportionality to
`A_5^f(m)`.

The exact missing theorem/formula is:

For the UV-025 tagged pre-whitening block, compute the grade `(1,5,1)`
component of
`D(G_-^{-1/2})[delta G_-] * delta N * D(G_+^{-1/2})[delta G_+]`
for source tags `tau1^2 tau2` and `tau1 tau2^2`, express the
`z^7` fixed-sector projection in the `I,S` basis, and prove it lies in
`C A_5^f(m)`.
