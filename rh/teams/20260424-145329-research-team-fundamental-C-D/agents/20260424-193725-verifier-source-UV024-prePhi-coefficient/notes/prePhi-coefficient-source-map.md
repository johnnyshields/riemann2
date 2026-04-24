# UV-024 Pre-`\Phi_K` Coefficient Source Map

Owned lane: `verifier-source-UV024-prePhi-coefficient`.

## Proved

- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415` proves holomorphic
  corrected whitening at matrix level:
  `\widehat\Omega_\zeta^{\corr}=G_-^{-1/2}NG_+^{-1/2}`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` gives a matrix-level
  first-order expansion of
  `\widehat\Omega_\zeta^{\corr}-\widehat\Omega_\zeta^{(0)}` before applying
  `\Phi_K`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2327-2413` gives matrix-level
  scaled whitening and explicitly says off-diagonal `Q` powers are matrix-level.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7062` defines
  `\mathfrak f`, one-pair `A_5^{\mathfrak f}`, `A_7^{\mathfrak f}`, and the
  quotient class `[A_7^{\mathfrak f}]`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7065-7191` proves the one-pair
  fixed-sector septic gauge law and determinant invariance.

## Conditional Or Missing

- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587` defines the transfer
  `\mathcal T_{Q,R}` only after applying `\Phi_K` and dividing by `w`; it is a
  scalar transfer, even though it is built from a matrix whitening map.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` supports the one-pair
  pre-whitening input bookkeeping, not a two-atom matrix cross-effect.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` assumes a septic
  quotient defect and then chooses a representative `R`; it does not construct
  `B_7^{\mathfrak f}(C)`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12255` keeps the actual
  source package conditional and warns that quotient/determinant-only routes are
  shear-blind.

## Minimal Missing Definition

The paper needs a definition before `\Phi_K`:

\[
C(a_1,h_1;a_2,h_2;z)
=
\operatorname{Cross}_{\mathcal W}
\bigl(X^{[1]}(a_1,h_1),X^{[1]}(a_2,h_2)\bigr)(z)
\in A_1(M_2),
\]

with source tags preserved, followed by

\[
B_7^{\mathfrak f}(C):=\pi_{\mathfrak f}[z^7]C.
\]

Then define

\[
Q_{7,m}^q(C)=[B_7^{\mathfrak f}(C)]
\in\mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]

Promotion additionally needs the theorem

\[
B_7^{\mathfrak f}((1-\Pi_{1,1})C)\in
\mathbf C A_5^{\mathfrak f}(m).
\]

No inspected source line provides this definition or theorem.
