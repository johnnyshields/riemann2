# UV-023 `L_h` Source Input Map

Owned lane: `explorer-UV023-Lh-source-input`.

## Source-supported candidate

The inspected source supports a one-pair pre-whitening linearization:

\[
L_h :=
\operatorname{Lin}_{U_\pm,E_\pm,G_\pm,V}
\mathfrak D_Q(\delta G_{h,-},\delta N_h,\delta G_{h,+}).
\]

Evidence:

- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2674` defines the weighted
  one-pair perturbation triple and states that every entry is linear in
  \(U_-,U_+,E_-,E_+,G_-,G_+,V\) modulo terms with at least two pair kernels.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722` verifies this for the
  corrected same-point block.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787` verifies this for the
  corrected mixed block.

This is before corrected whitening, so it avoids the post-hoc signed-lift
negative.

## Missing source object

The source does not define the actual two-atom corrected block map whose
pair-kernel-linear derivative is this \(L_h\). Therefore the formal source input

\[
X^{[1]}(a_1,h_1;a_2,h_2)=a_1L_{h_1}+a_2L_{h_2}
\]

is a candidate definition, not a current theorem.

Promotion needs the paper to state:

1. an actual two-atom corrected block triple before whitening;
2. a pair-kernel-linear derivative functor \(\operatorname{Lin}_{\mathcal K}\);
3. identification of \(L_h\) with the one-atom source input feeding the
   corrected-whitening transfer;
4. the vanishing-at-\(w=0\) condition needed for
   \(\mathcal T_{Q,R}(X^{[1]})\);
5. compatibility with the fixed-target quotient extraction \(Q_7^q\).

## Harness result

`scripts/lh_source_input_check.py` confirms:

- linear pair-kernel part is additive in two source tags;
- the linear input can feed \(\mathcal T_1\) formally;
- the nonlinear transfer cross-effect generates bidegrees \((1,1),(1,2),(2,1)\);
- \(\Pi_{1,1}\) keeps the quadratic interaction only;
- signed source-weight lift still leaves higher \(a^3,a^5,\dots\) terms.

Thus the next theorem is definition-first: construct \(L_h\) as an actual
source functor, then prove \(Q_7^q\)-compatibility for non-\((1,1)\) bidegrees.
