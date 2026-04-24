# UV-026 Stage 1 Source-Normalization Map

This note audits what the current paper source supports for the finite
normalized source-table theorem feeding
\[
B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7].
\]
It is a source/normalization map, not a derivation of the tables.

## Source Map

1. Holomorphic whitening is available at the finite-\(s\) level.
   `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1458` proves holomorphy of
   the corrected same-point and mixed blocks and of the inverse square roots.
   It also records that the mixed block's apparent \(s^{-1}\), \(s^{-2}\), and
   \(s^{-3}\) poles are removable.

2. The pre-\(\Phi_K\) matrix object is
   \[
   \mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
   \]
   `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` defines this and
   displays the first Frechet boundary with \(N^{(0)}\) in the ordered matrix
   product.

3. The scaled transfer section is not itself the \(B_7^{\mathfrak f}\) table.
   `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` introduces
   \(w=z/R\), \(s=z/Q^2=Rw/Q^2\), the entrywise operator \(\mathfrak D_Q\), and
   perturbations \(\delta G_\pm=\mathfrak D_Q^{-1}X_\pm\),
   \(\delta N=\mathfrak D_Q^{-1}Y\).  Its quotient
   \(\mathcal T_{Q,R}\) is after \(\Phi_K\) and division by \(w\); it provides
   analytic control, not the pre-\(\Phi_K\) coefficient table.

4. The one-pair source formulas are exact enough to define a Stage 1 expansion.
   `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2674` switches to ordinary
   \(z\) with \(t_\pm=m\pm z/(2Q^2)\) and
   \(\eta(z)=\delta\Delta(z/Q^2)\), then defines the weighted one-pair source
   triple \(X_{\rho,\pm}=\mathfrak D_Q(\delta G_{\rho,\pm})\),
   \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\).

5. The exact corrected same-point and mixed formulas are displayed, but only
   bounded-baseline linearity is proved.  The same-point formula is at
   `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`; the mixed formula and
   its linear Taylor expansion through the removable denominators are at
   `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`.

6. Source tags are available only at the pre-whitening level.
   `C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899` defines the tagged
   two-atom block, the pair-kernel linear projection, and warns that
   \(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), and the cubic gauge theorem remain
   separate obligations.

7. One-pair \(K_5\), \(K_3\), and pure-sector laws cannot certify Stage 1
   tables by themselves.  The \(K_5/K_3\) classes and projected laws are at
   `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7409`, and pure same-point
   elimination is at `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-8048`.
   They apply only after the actual UV-026 term has been identified as one of
   those source classes.

8. The two-point source-level route is downstream and cannot replace the
   pre-\(\Phi_K\) table.  `C:/workspace/riemann2/rh/proof_of_rh.tex:12098-12331`
   records conditional source-level merger inputs and the even-amplitude
   obstruction to the naive source-summed whitened model.

9. The live UV-026 target is exactly pre-\(\Phi_K\),
   \(\pi_{\mathfrak f}[z^7]\), and matrix/fixed-sector.  The paper states the
   \(L_1YR_1\) gate and says the coefficient lists remain missing at
   `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.

## Acceptance Criteria

A claimed Stage 1 finite normalized source-table theorem is acceptable only if
all of the following are explicit.

1. **Ordinary \(z\).**  Coefficients are \([z^r]\), \(0\le r\le7\), after the
   substitution \(s=z/Q^2\).  Tables in \(s\) or \(w=z/R\) are acceptable only
   with the exact conversion factors and with no later \(\Phi_K\) quotient.

2. **Source tags retained.**  Tables retain \(\tau_1,\tau_2\) until after the
   required non-\((1,1)\) tag components \(112\) and \(122\) are isolated.
   Applying \(\tau_1,\tau_2\mapsto1\) before this extraction is not acceptable.

3. **\(\mathfrak D_Q\) convention stated.**  The theorem declares which
   same-point table is raw \(\delta G_{i,\pm}^{\lin}\) and which is weighted
   \(X_{i,\pm}=\mathfrak D_Q\delta G_{i,\pm}^{\lin}\), and includes the
   conversion used by the Frechet derivative.  The mixed table must be
   \[
   M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin}),
   \]
   not raw \(\delta N_i^{\lin}\), unless a full conversion to the same
   \(B_7^{\mathfrak f}\) gate is proved.

4. **Removable singularities expanded.**  For the mixed block, coefficients are
   extracted only after expanding the numerators and proving the cancellations
   across \(s^{-1}\), \(s^{-2}\), and \(s^{-3}\).  Big-O bounded-baseline
   linearity is not a coefficient table.

5. **Baseline data in the same normalization.**  Exact order-\(\le7\) tables
   are supplied for \(G_\pm^{(0)}(z)\), \(G_\pm^{(0)}(z)^{-1/2}\) or enough
   data to compute it, and \(N_0(z)=N^{(0)}(z/Q^2)\) in the same matrix
   coordinates used by \(LNR\).  Baseline scale estimates \(O(Q)\), \(O(Q^2)\),
   \(O(Q^3)\) are not enough.

6. **Enough hidden jets.**  Since the mixed block divides by powers through
   \(s^3\), the source theorem must provide baseline phase and source-kernel
   Taylor data far enough before division to recover every coefficient through
   \([z^7]\) after division.  Listing only post-division objects without this
   cancellation audit leaves a hidden input.

7. **Pre-\(\Phi_K\) output.**  The resulting table feeds matrix products and
   \(B_7^{\mathfrak f}\).  Post-\(\Phi_K\) scalar coefficients, determinant
   charts, quotient coordinates, or diagonal-merger statements are not Stage 1
   source tables.

## Rejection Criteria

Reject or quarantine any claimed table theorem that:

- gives raw \(\delta N_i^{\lin}\) tables in place of
  \(\mathfrak D_Q\delta N_i^{\lin}\);
- gives \(s\)- or \(w\)-coefficients without exact conversion to ordinary
  \(z\);
- augments away source tags before extracting \(112\) and \(122\);
- uses only the Banach transfer estimate after \(\Phi_K\);
- cites the one-pair \(K_5/K_3\) or pure-sector laws before source-class
  identification;
- extracts mixed-block coefficients from denominators without showing the
  removable-singularity expansion;
- supplies determinant scalarization or quotient data instead of the actual
  pre-\(\Phi_K\) fixed-sector matrices.

## Sharp UV-026 Substatement

Prove the Stage 1 normalized source-table theorem:

In ordinary \(z\), after substituting \(s=z/Q^2\), with source tags retained and
before \(\Phi_K\), the tagged source block \(\mathcal B_2\) admits exact
order-\(\le7\) tables for
\[
G_\pm^{(0)}(z),\quad N_0(z),\quad
\delta G_{i,\pm}^{\lin,[1]}(z),\quad
\delta G_{i,\pm}^{\lin,[5]}(z),\quad
M_i^{[1]}(z),\quad M_i^{[5]}(z),
\]
where
\[
M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin}).
\]
The theorem must include the \(\mathfrak D_Q\) conversion for the same-point
Frechet inputs and the removable-singularity expansion of the mixed block.
These tables must be sufficient, without \(\Phi_K\), determinant scalarization,
quotient extraction, or diagonal merger, to compute every
\(\pi_{\mathfrak f}[z^7]\) vector used by the seven UV-026 cubic gates.
