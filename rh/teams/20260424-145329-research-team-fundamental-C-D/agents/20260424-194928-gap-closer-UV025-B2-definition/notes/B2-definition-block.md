# UV-025 Proposed Definition Block

This note records the smallest paper-ready source-block addition found in this
pass. It is a pre-whitening object; no \(\Phi_K\), determinant, or quotient
extraction appears here.

## Definition

Introduce formal source tags \(\tau_1,\tau_2\). For a normalized two-atom core
\((a_1,h_1;a_2,h_2)\), define the tagged corrected source perturbations by
additive substitution into the corrected phase variables:
\[
d_\pm^{(2)}:=\tau_1a_1d_{h_1,\pm}+\tau_2a_2d_{h_2,\pm},
\qquad
e_\pm^{(2)}:=\tau_1a_1e_{h_1,\pm}+\tau_2a_2e_{h_2,\pm},
\]
\[
g_\pm^{(2)}:=\tau_1a_1g_{h_1,\pm}+\tau_2a_2g_{h_2,\pm},
\qquad
\eta^{(2)}:=\tau_1a_1\eta_{h_1}+\tau_2a_2\eta_{h_2}.
\]
Equivalently,
\[
q_{2,\pm}=q_{0,\pm}+d_\pm^{(2)},\qquad
q'_{2,\pm}=q'_{0,\pm}+e_\pm^{(2)},\qquad
q''_{2,\pm}=q''_{0,\pm}+g_\pm^{(2)},\qquad
\Delta_2=\Delta_0+\eta^{(2)}.
\]

Define
\[
\mathcal B_2(a_1,h_1;a_2,h_2)
:=(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
\]
by the same corrected same-point and mixed block formulas used in
`proof_of_rh.tex:2688-2735`, with \(q_\pm,\Delta\) replaced by
\(q_{2,\pm},\Delta_2\).

Set \(\mathcal B_0=(G_-^{(0)},N^{(0)},G_+^{(0)})\).

## Pair-kernel filtration

Let \(\mathcal K\) be the filtration on entries of
\(\mathfrak D_Q(\mathcal B_2-\mathcal B_0)\) in which each tagged source kernel
\[
\tau_iU_{i,\pm},\quad \tau_iE_{i,\pm},\quad
\tau_iG_{i,\pm},\quad \tau_iV_i
\]
has \(\mathcal K\)-degree \(1\), while baseline factors, \(a_i\), \(Q\)-scales,
and bounded analytic coefficients have degree \(0\). Let
\(\operatorname{Lin}_{\mathcal K}\) denote projection to \(\mathcal K\)-degree
one.

Define the one-atom source-linear triple
\[
L_h:=\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_1(h)-\mathcal B_0),
\]
where \(\mathcal B_1(h)\) is the one-atom corrected block obtained from the same
formulas.

## Theorem

With source tags retained,
\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_2(a_1,h_1;a_2,h_2)-\mathcal B_0)
=\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}.
\]
Forgetting the tags gives the UV-025 target
\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=a_1L_{h_1}+a_2L_{h_2}.
\]

## Proof Skeleton

For \(G_{2,\pm}^{\corr}\), the \((1,1)\) and off-diagonal entries are linear in
\(d_\pm^{(2)}\) and \(e_\pm^{(2)}\). The \((2,2)\) entry is
\[
g_\pm^{(2)}+
\text{baseline}\cdot d_\pm^{(2)}
+\text{terms of }\mathcal K\text{-degree}\ge2,
\]
matching `proof_of_rh.tex:2688-2722`.

For \(N_2^{\corr}\), Taylor expansion in
\((d_-^{(2)},d_+^{(2)},\eta^{(2)})\) gives a bounded-baseline linear
combination of those variables and a remainder of \(\mathcal K\)-degree at
least two, matching `proof_of_rh.tex:2724-2787`.

Since the tagged variables are additive sums of the two source contributions,
the \(\mathcal K\)-linear part splits as the sum of the two one-atom
\(\mathcal K\)-linear parts, with tags still attached.

## Classification

UV-025 is a definition addition plus a short theorem gap. It is not a genuine
source-level obstruction at the pre-whitening block level. The genuine
obstructions remain downstream: identifying the matrix cross-effect with the
finite-order quotient package and proving the UV-024/UV-026 quotient-gauge
claims.
