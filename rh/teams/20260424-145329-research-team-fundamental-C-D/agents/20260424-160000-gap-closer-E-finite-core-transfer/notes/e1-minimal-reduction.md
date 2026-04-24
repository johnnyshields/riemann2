# E1 minimal reduction notes

Target: descend from genuine corrected finite-core data to the defect-free affine-incidence lanes in `rh/proof_of_rh.tex:12676-12979`.

## Baseline

The defect-free theorems do not use full vanishing of the interaction germ. They use only projected low-order vanishing:

- quintic circuit lane: the multi-pair interaction contributes nothing to the cubic scalar and quintic fixed-sector coefficients; then `V(h)=(c,u_5,v_5)` gives affine dependence of `Xi(h)=(u_5/c,v_5/c)`.
- lifted `v_5` lane: the interaction contributes nothing to cubic, quintic, and the local septic fixed-sector coefficient after choosing the `v_7=0` gauge; then `Q_v(h)=(u_5/c,v_5/c,Delta_7/(cv_5))` is affinely dependent.

Thus the relevant low-order interaction object is not the full pairwise interaction germ, but the total projected defect of the whole finite core in
\[
\mathbf C\oplus \mathfrak f\oplus (\mathfrak f/\mathbf C A_5^{\mathfrak f})
\]
or in the chosen local gauge.

## Weakest sufficient E1 hypothesis

For a bad finite core `sum_j a_jF_{h_j}+I_{>=2}=0`, define projected total corrected defects
\[
D_3=[I_{>=2}]_3,
\quad D_5^{\mathfrak f}=\pi_{\mathfrak f}[I_{>=2}]_5,
\quad \bar D_7=[\pi_{\mathfrak f}[I_{>=2}]_7]\in \mathfrak f/\mathbf C A_5^{\mathfrak f}.
\]
Then the clean theorem-ready condition is
\[
D_3=0,
\quad D_5^{\mathfrak f}=0,
\quad \bar D_7=0
\]
on the relevant patch. This is weaker than full interaction-germ vanishing and weaker than pairwise quadratic factorization. It is exactly the projected information needed to run the defect-free affine-dependence proofs unchanged.

For the quintic planar lane, only the first two equations are needed. For lifted `v_5`/`u_5` lanes, the septic quotient equation is also needed.

## Sharp obstruction

C and D identify package fibers / transformed first odd state, but they do not imply these projected low-order interaction defects vanish. If the projected defect vector is nonzero, the bad-core equations become inhomogeneous:
\[
\sum_j a_j(c_j,u_{5,j},v_{5,j})=- (D_3,D_{5,I},D_{5,S}),
\]
not an affine dependence relation. Existing incidence theorems do not absorb this inhomogeneous term.

A weaker but less theorem-ready alternative is to prove directly that the inhomogeneous system nevertheless has a nontrivial homogeneous affine circuit among the same nodes. That is a rank/incidence theorem on the corrected defect vector, not currently present in the draft.

## E2 bypass note

The positive-kernel route bypasses incidence only if it supplies one-sided weighted-average control of `H_core^(2N-1)` or direct lower control of `Xi_core^(N)`. A lower bound for the first surviving coefficient alone is insufficient without sign/variation/tail-domination control for the universal positive tail.
