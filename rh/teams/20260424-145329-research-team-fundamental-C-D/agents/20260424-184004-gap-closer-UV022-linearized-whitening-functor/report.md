# Claim

UV-022 has a credible candidate functor: the first homogeneous term
\(\mathcal T_1\) of the corrected-whitening transfer. The paper already proves
that corrected whitening admits a linear term in block perturbations, and the
scaled transfer package defines a homogeneous expansion
\[
\mathcal T_{Q,R}(X)=\sum_{p\ge 1}\mathcal T_p(X).
\]

This does not close UV-022. The missing input is the actual source-weight
linear perturbation triple \(X^{[1]}\) for the corrected two-atom order-7 block
package, together with a proof that applying \(\mathcal T_1\) and extracting the
septic quotient output gives the UV-010 object.

# Status

open

# Evidence

Three-bin separation:

- **Proved / source-supported:** the whitening map is analytic:
  \[
  \mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
  \]
  Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575`.
- **Proved / source-supported:** around a background block, corrected whitening
  has a first-order term
  \[
  D\mathcal W_{(0)}[R_-,\widetilde R,R_+]
  \]
  plus a quadratic error. The displayed formula is
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`. The same-point
  derivative is controlled by a Frechet derivative of \(G^{-1/2}\) at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1826-1935`.
- **Proved / source-supported:** the scaled transfer theorem defines, for a
  weighted perturbation triple \(X=(X_-,Y,X_+)\), the quotient scalar
  \(\mathcal T_{Q,R}(X)\) at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2458-2502`, and proves the
  homogeneous expansion
  \[
  \mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)
  \]
  at `C:/workspace/riemann2/rh/proof_of_rh.tex:2504-2526`.
- **Candidate:** \(\mathcal T_1\) is exactly the invariant linearized-whitening
  functor UV-022 was asking for at the analytic whitening layer. It is canonical
  once the baseline blocks and the perturbation triple \(X\) are fixed.
- **Missing:** the paper does not provide the source-weight linear perturbation
  triple \(X^{[1]}\) for an actual corrected two-atom order-7 package. The
  one-pair exterior perturbation triple \(X_\rho\) at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2653-2674` is a useful model, but
  it is not the two-atom collision package required by UV-010.
- **Missing:** no source line proves that the septic quotient component of
  \(\mathcal T_1(X^{[1]})\) is
  \(\mathcal J_2^{(7)}\), \(\mathfrak O_7\), or
  \(\mathcal H_7^q\).

# Baseline / delta

Baseline: the source-weight linearization pass showed that a signed lift
\(aW(a)\) is not enough. Exact one-amplitude collapse needs an invariant
source-weight linear projection or a theorem making higher source-weight terms
quotient-invisible.

Delta: this pass identifies the existing analytic functor to use after such a
projection is available. The correct candidate is not finite-amplitude
whitening; it is the first homogeneous corrected-whitening transfer
\(\mathcal T_1\). The next missing step is to construct the input
\(X^{[1]}\) from actual corrected two-atom blocks and then inspect its order-7
quotient output.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575` - analytic whitening map.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799` - first-order whitening
  expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1826-1935` - same-point Frechet
  derivative.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2553` - uniform scaled
  corrected-whitening transfer and homogeneous expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2653-2674` - one-pair perturbation
  triple as a model for the missing two-atom input.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227` - finite-amplitude
  source-summed route fails, so the linearized route must be a new lift.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-183713-explorer-UV010-source-weight-linearization/report.md`
  - prior UV-022 source-weight obstruction.

# Dependencies

- A baseline corrected block triple in the collision-cancellation chart.
- A source-weight linear perturbation triple \(X^{[1]}\) for the actual
  corrected two-atom order-7 package.
- Proof that \(X^{[1]}\) satisfies the vanishing-at-\(w=0\) condition needed to
  define \(\mathcal T_{Q,R}\).
- Extraction of the cubic/quintic/septic quotient outputs from
  \(\mathcal T_1(X^{[1]})\).
- Good-patch quotient-line trivialization for the resulting order-7 output.

# Strongest objection

\(\mathcal T_1\) is a scalar/whitened transfer functor, not yet a
quotient-valued two-atom package. It can only solve UV-022 if the source-weight
linear block input \(X^{[1]}\) is defined canonically and if its order-7 output
matches the UV-010 quotient target. The current source proves the transfer
technology, not that match.

# Needed for promotion

1. Define \(X^{[1]}(a_1,h_1;a_2,h_2)\) as the source-weight linear coefficient
   of the actual corrected two-atom block triple, not the finite-amplitude
   whitened package.
2. Prove \(X^{[1]}\) is swap-compatible and has exact one-amplitude collapse.
3. Apply \(\mathcal T_1\) and prove the resulting corrected odd output has the
   cubic/quintic/septic quotient components required by the UV-010 package.
4. Extract the order-7 quotient component and test it against the free
   \(a_1a_2\delta^2P(m,\kappa)\) perturbation.

# Autoresearch next step

continue: construct the actual \(X^{[1]}\) input. Mine the corrected same-point
and mixed block formulas for a source-weight linear coefficient in the
two-atom collision chart, then feed that coefficient through \(\mathcal T_1\).

verify: source-check that \(\mathcal T_1\) is being used only on linearized
block perturbations, not on the finite-amplitude even whitened package.

blocked: no process blocker. Mathematical blocker is the missing
source-weight-linear two-atom perturbation triple \(X^{[1]}\).

terminal: terminal for the subroute "UV-022 has no whitening-side candidate."
It does have one: \(\mathcal T_1\). Not terminal for UV-022, because the input
and order-7 quotient extraction are missing.
