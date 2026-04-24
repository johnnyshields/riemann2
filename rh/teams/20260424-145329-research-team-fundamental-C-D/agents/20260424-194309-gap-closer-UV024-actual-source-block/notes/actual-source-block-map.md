# UV-024 Actual Source Block Map

Question: can the actual two-atom source-linear corrected-block input be
defined from current source before whitening and before \(\Phi_K\)?

## Source-supported pieces

- `proof_of_rh.tex:1392-1415` defines corrected matrix whitening from corrected
  same-point and mixed blocks before scalar extraction.
- `proof_of_rh.tex:1693-1732` and `1784-1799` give the matrix first-order
  whitening expansion around a baseline block triple.
- `proof_of_rh.tex:2415-2526` gives the homogeneous transfer, but only after
  applying \(\Phi_K\) and dividing by \(w\).
- `proof_of_rh.tex:2659-2787` supports a one-pair pre-whitening linear object:
  after applying \(\mathfrak D_Q\), actual one-pair corrected block entries are
  linear in \(U_\pm,E_\pm,G_\pm,V\) modulo terms with at least two pair kernels.

## Definition-ready candidate

Define the one-pair source-linear block derivative as
\[
L_h:=
\operatorname{Lin}_{U_\pm,E_\pm,G_\pm,V}
\bigl(
\mathfrak D_Q(\delta G_{h,-}),
\mathfrak D_Q(\delta N_h),
\mathfrak D_Q(\delta G_{h,+})
\bigr).
\]

If an actual two-atom pre-whitening corrected block triple
\[
\mathcal B_2(a_1,h_1;a_2,h_2)
=
(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
\]
is defined, the desired source-linear input would be
\[
X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2}.
\]

This is before whitening and before \(\Phi_K\). It can feed the analytic matrix
whitening map or its first homogeneous transfer once the two-atom block theorem
exists.

## Missing theorem

The source does not currently define \(\mathcal B_2\) at the matrix block level
with source tags. It gives a schematic quotient odd germ
`proof_of_rh.tex:11459-11474` and conditional finite-order package hypotheses
`11888-12227`, but those are downstream of the pre-whitening block.

Smallest missing theorem:
\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q\bigl(\mathcal B_2(a_1,h_1;a_2,h_2)-\mathcal B_0\bigr)
=a_1L_{h_1}+a_2L_{h_2},
\]
with \(\mathcal K\) the pair-kernel filtration and with source tags preserved
through the collision chart. The theorem must also specify what happens to
higher pair-kernel terms before the \(\Pi_{1,1}\) projection and before
\(B_7^{\mathfrak f}\) extraction.

## Split recommendation

UV-024 should split. Keep UV-024 for the coefficient map and non-\((1,1)\)
quotient-gauge theorem. Add an upstream UV for the actual two-atom
source-linear pre-whitening block triple and its pair-kernel-linear derivative
theorem.
