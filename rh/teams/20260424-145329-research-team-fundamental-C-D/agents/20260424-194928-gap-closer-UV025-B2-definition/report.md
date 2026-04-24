# Claim

UV-025 is best classified as a **definition addition plus a short theorem gap**,
not as a genuine obstruction. Current source does not already define
\[
\mathcal B_2(a_1,h_1;a_2,h_2)
=(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
\]
before whitening with source tags. However, the existing corrected block
formulas support a minimal paper-ready definition: introduce formal tags
\(\tau_1,\tau_2\), insert the additive tagged source perturbations
\[
d_\pm^{(2)}=\tau_1a_1d_{h_1,\pm}+\tau_2a_2d_{h_2,\pm},
\quad
e_\pm^{(2)}=\tau_1a_1e_{h_1,\pm}+\tau_2a_2e_{h_2,\pm},
\]
\[
g_\pm^{(2)}=\tau_1a_1g_{h_1,\pm}+\tau_2a_2g_{h_2,\pm},
\quad
\eta^{(2)}=\tau_1a_1\eta_{h_1}+\tau_2a_2\eta_{h_2}
\]
into the existing corrected same-point and mixed block formulas, and only then
forget tags after taking \(\operatorname{Lin}_{\mathcal K}\).

With that definition added, the theorem
\[
\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=a_1L_{h_1}+a_2L_{h_2}
\]
follows by the same Taylor-linear bookkeeping as
`proof_of_rh.tex:2659-2787`, with tags retained through the linear projection.
This does not close UV-024/UV-026, because it does not prove the downstream
pre-determinant coefficient map or the non-\((1,1)\)
\(A_5^{\mathfrak f}\)-gauge theorem.

# Status

open

# Evidence

Three-bin separation:

- **Proved from source:** corrected whitening is built from corrected
  same-point and mixed blocks before \(\Phi_K\):
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415`.
- **Proved from source:** the matrix whitening map
  \(\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}\) is used before scalar
  extraction, with matrix first-order expansion at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`.
- **Proved from source:** the baseline scaling is matrix-level, and the later
  extra \(Q\)-power belongs to scalar normalization, not to the matrix identity:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2327-2413`.
- **Proved from source:** the scalar transfer
  \(\mathcal T_{Q,R}(X)\) accepts a pre-whitening perturbation triple, but is
  defined after \(\Phi_K\) and division by \(w\):
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2526`.
- **Proved from source:** the one-pair scaled perturbation triple is
  \[
  X_{\rho,\pm}:=\mathfrak D_Q(\delta G_{\rho,\pm}),\qquad
  Y_\rho:=\mathfrak D_Q(\delta N_\rho),
  \]
  and each entry is linear in
  \(U_-,U_+,E_-,E_+,G_-,G_+,V\) modulo terms with at least two pair kernels:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2674`.
- **Proved from source:** the same-point proof shows the linear part and
  higher-\(\mathcal K\) remainder explicitly. In particular, the \((2,2)\)
  entry has a \(G_\pm\) and baseline-times-\(U_\pm\) linear part, with
  \(U_\pm^2,U_\pm^3\) higher:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`.
- **Proved from source:** the mixed-block proof Taylor expands in
  \((d_-,d_+,\eta)\); its linear part is a bounded-baseline combination of
  \(U_-\), \(U_+\), and \(V\), and the remainder is quadratic:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`.
- **Conditional from source:** the current two-pair decomposition is only a
  schematic quotient odd germ, not a tagged pre-whitening block definition:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474`.
- **Conditional from source:** the defect theorem assumes cubic/quintic/septic
  quotient defects already exist:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11616`.
- **Conditional from source:** the source criterion starts after an abstract
  actual package \(\mathfrak P_2\in V\) is supplied:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11994-12009`.
- **Proved source boundary:** the draft says the remaining issue is verifying
  source-level merger for the corrected two-atom package:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189`.
- **Proved source negative:** the naive post-whitening source-summed route is
  invalid because finite-order whitened coefficients are even in source weight:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`.
- **Architecture caveat:** the paper separately says verification of the actual
  corrected two-atom package remains architectural at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11303-11307`, and that the actual
  two-pair package/state-locality is not proved at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:22604-22611` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:25474-25479`.
- **Missing from current source:** no inspected line defines the tagged
  pre-whitening \(\mathcal B_2\), the pair-kernel filtration
  \(\mathcal K\) on that object, or the tagged theorem
  \[
  \operatorname{Lin}_{\mathcal K}
  \mathfrak D_Q(\mathcal B_2-\mathcal B_0)
  =\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}.
  \]
- **Paper-ready addition:** the definition/theorem block in
  `notes/B2-definition-block.md` gives the minimal source object and proof
  skeleton without using the rejected post-whitening signed lift.

No computational script was needed. This is a source-definition and local
Taylor-bookkeeping pass.

# Baseline / delta

Baseline: UV-024 was split because current source lacked an actual source-linear
two-atom block input. Prior reports identified the one-pair
pair-kernel-linear derivative \(L_h\) as the right candidate, and the conditional
matrix cross-effect \(C_{\mathcal W}\) as ready once \(X^{[1]}\) exists.

Delta: this pass gives the minimal paper-ready definition of
\(\mathcal B_2\) and \(\mathcal K\). It also classifies UV-025: the missing
piece is not a post-whitening source lift and not a determinant/quotient
problem. It is a pre-whitening definition addition plus a short theorem using
the already displayed same-point and mixed-block Taylor expansions. The
downstream quotient-gauge problems remain UV-024/UV-026.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-023/UV-024/UV-025 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:56`
  - UV-025 entry.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415` - corrected block
  whitening before \(\Phi_K\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` - matrix transfer split
  before scalar extraction.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799` - matrix Frechet
  derivative.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2327-2413` - baseline-scaled
  matrix identity.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2526` - scalar transfer after
  \(\Phi_K\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` - one-pair
  pair-kernel-linear theorem model.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474` - schematic two-pair
  quotient decomposition.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11616` - assumed quotient
  defects.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12009` - abstract source
  criterion and conditional actual package.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12227` - remaining
  source-level input and post-whitening negative.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11303-11307`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:22604-22611`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:25474-25479` - actual-package caveats.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194309-gap-closer-UV024-actual-source-block/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-verifier-source-UV024-prePhi-coefficient/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194928-gap-closer-UV025-B2-definition/notes/B2-definition-block.md`.

# Dependencies

- Existing corrected same-point and mixed block formulas.
- Existing \(\mathfrak D_Q\) scaling and Banach-germ transfer setup.
- A new formal source-tag convention \(\tau_1,\tau_2\).
- A new pair-kernel filtration \(\mathcal K\) counting
  \(\tau_iU_{i,\pm},\tau_iE_{i,\pm},\tau_iG_{i,\pm},\tau_iV_i\) as degree one.
- A definition of one-atom \(L_h\) as the \(\mathcal K\)-linear part of the
  scaled corrected block triple.
- Downstream UV-024/UV-026 definitions and gauge theorems before quotient
  promotion.

# Strongest objection

The proposed \(\mathcal B_2\) is a source lift. It is actual as a pre-whitening
corrected block object only if the paper explicitly declares that the
two-atom corrected source is obtained by additive tagged substitution into the
same corrected block formulas. That is a reasonable and minimal definition, but
it does not prove that downstream scalarized finite-order quotient packages
coincide with the UV-010 edge object. Without a later package-coincidence
theorem, \(\mathcal B_2\) could be a clean lift that still does not close the
actual quotient defect problem.

# Needed for promotion

1. Add the tagged pre-whitening definition of
   \(\mathcal B_2(a_1,h_1;a_2,h_2)\) by substituting
   \(q_{2,\pm}=q_{0,\pm}+d_\pm^{(2)}\) and
   \(\Delta_2=\Delta_0+\eta^{(2)}\) into the existing corrected block formulas.
2. Define \(\mathcal K\) and \(\operatorname{Lin}_{\mathcal K}\) with source
   tags retained.
3. Define \(L_h\) as the one-atom \(\mathcal K\)-linear scaled corrected-block
   triple.
4. Prove the tagged theorem
   \[
   \operatorname{Lin}_{\mathcal K}
   \mathfrak D_Q(\mathcal B_2-\mathcal B_0)
   =\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2},
   \]
   then forget tags to obtain the displayed UV-025 identity.
5. State explicitly that this is before whitening and before \(\Phi_K\), and
   that post-whitening signed source lift is not being used.
6. Keep separate downstream obligations: \(C_{\mathcal W}\),
   \(B_7^{\mathfrak f}\), \(Q_{7,m}^q\), \(\Pi_{1,1}\), and UV-026's cubic
   \((1,1,5)\) \(A_5^{\mathfrak f}\)-gauge theorem.

# Autoresearch next step

continue: turn `notes/B2-definition-block.md` into a paper-updates candidate
near `proof_of_rh.tex:2659-2787`, with a short proof that directly references
the same-point and mixed-block Taylor expansions.

verify: a source verifier should check that the proposed
\(\mathcal B_2\) uses the same corrected phase variables as the existing block
formulas and that tags are not specialized before
\(\operatorname{Lin}_{\mathcal K}\). An adversarial verifier should check that
this definition is not silently claiming downstream quotient package
coincidence.

blocked: no process blocker. Mathematical blocker for UV-025 is only that the
definition/theorem is absent from the paper; the genuine harder blockers are
downstream UV-024/UV-026.

terminal: terminal for treating UV-025 as a genuine obstruction or trying to
obtain it from post-whitening signed source lift. Not terminal for promotion:
the definition/theorem block still needs source review and paper insertion.

Honest verdict: UV-025 is not currently proved in the source, but it is
definition-ready. Add the tagged pre-whitening \(\mathcal B_2\), define
\(\mathcal K\), and prove the \(\mathcal K\)-linear identity by the existing
Taylor-linear block argument.

# Ledger destination

paper-updates.md - propose the definition/theorem block from
`notes/B2-definition-block.md`; attempts.md - record this route as `keep`
because it reduces UV-025 to a concrete paper addition and leaves UV-024/UV-026
as downstream obligations.
