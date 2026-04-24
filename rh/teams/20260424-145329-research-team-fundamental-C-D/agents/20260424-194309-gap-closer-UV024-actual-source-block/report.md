# Claim

Current source does **not** define the actual two-atom source-linear
corrected-block input before whitening. It supports a narrow, definition-ready
candidate:
\[
L_h:=
\operatorname{Lin}_{U_\pm,E_\pm,G_\pm,V}
\bigl(
\mathfrak D_Q(\delta G_{h,-}),
\mathfrak D_Q(\delta N_h),
\mathfrak D_Q(\delta G_{h,+})
\bigr),
\]
using the one-pair pair-kernel-linear bookkeeping in
`proof_of_rh.tex:2659-2787`, and then
\[
X^{[1]}(a_1,h_1;a_2,h_2):=a_1L_{h_1}+a_2L_{h_2}.
\]

But the paper lacks the actual two-atom pre-whitening corrected block triple
whose pair-kernel-linear derivative is this \(X^{[1]}\). Therefore UV-024 should
split: an upstream UV should define/prove the actual source-linear two-atom
block input, while UV-024 keeps the pre-determinant coefficient map
\(B_7^{\mathfrak f}\), \(Q_{7,m}^q\), and the non-\((1,1)\)
\(A_5^{\mathfrak f}\)-gauge theorem.

# Status

open

# Evidence

Three-bin separation:

- **Proved from source:** corrected matrix whitening exists before
  \(\Phi_K\). The corrected same-point and mixed blocks define
  \[
  \widehat\Omega_\zeta^{\corr}
  =G_-^{-1/2}N_m^{\corr}G_+^{-1/2}
  \]
  as a holomorphic matrix-valued object at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415`.
- **Proved from source:** the whitening map has a matrix first-order expansion
  before scalar extraction. The perturbative split is at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732`, and the Frechet
  derivative is displayed at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`.
- **Proved from source:** the scaled transfer
  \(\mathcal T_{Q,R}(X)\) is available only after applying \(\Phi_K\) and
  dividing by \(w\), with homogeneous expansion at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2526`. This can use a
  perturbation triple \(X\), but it is not itself the pre-\(\Phi_K\) source
  block.
- **Proved from source:** the best one-pair \(L_h\) candidate is supported by
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787`: after
  \(\mathfrak D_Q\), actual one-pair corrected-block entries are linear in
  \(U_-,U_+,E_-,E_+,G_-,G_+,V\) modulo terms containing at least two pair
  kernels.
- **Conditional from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474`
  gives only a schematic quotient odd-germ two-pair decomposition and says the
  finite-order model has quadratic/divisible projections. This is not an actual
  matrix block triple before whitening.
- **Conditional from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11994-12009`
  assumes the actual corrected two-pair finite-order package through order 7
  admits a source-level realization. It does not define the pre-whitening
  corrected block that would produce that package.
- **Proved source boundary:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189`
  says the remaining two-point issue is verification of the finite-order
  source-level merger statement for the corrected two-atom package.
- **Proved source negative:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rejects the naive post-whitening source-summed model: finite-order whitened
  coefficients are even analytic functions of the source weight.
- **Missing:** no inspected source line defines an actual two-atom corrected
  block triple
  \[
  \mathcal B_2(a_1,h_1;a_2,h_2)
  =(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
  \]
  before whitening and before \(\Phi_K\).
- **Missing:** no inspected source line proves
  \[
  \operatorname{Lin}_{\mathcal K}
  \mathfrak D_Q(\mathcal B_2-\mathcal B_0)
  =a_1L_{h_1}+a_2L_{h_2}
  \]
  with source tags preserved, where \(\mathcal K\) is the pair-kernel
  filtration.
- **Missing:** no inspected source line proves that higher pair-kernel or
  higher source-weight terms are either killed by \(\Pi_{1,1}\) before
  coefficient extraction or land in \(\mathbf C A_5^{\mathfrak f}(m)\) after
  \(B_7^{\mathfrak f}\).

No computational script was needed for this source-provenance pass.

# Baseline / delta

Baseline: UV-022 identified \(\mathcal T_1\) as the whitening-side candidate
once a source-linear input \(X^{[1]}\) exists. UV-023/UV-024 work then isolated
the pre-determinant target \(B_7^{\mathfrak f}(C)\) and the quotient
\(Q_{7,m}^q(C)=[B_7^{\mathfrak f}(C)]\), but left the actual source input
unproved. The signed source-weight lift is already rejected because it leaves
higher \(a^3,a^5,\dots\) terms.

Delta: this pass pins down the smallest missing source object. The one-pair
pair-kernel-linear \(L_h\) is source-supported as a candidate derivative, but
only an actual two-atom pre-whitening block theorem can turn
\(a_1L_{h_1}+a_2L_{h_2}\) into the UV-024 input. Thus the present route is
definition-ready but not source-proved.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-023/UV-024 frontier and signed-lift negative.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-024 entry.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415` - corrected finite-\(s\)
  holomorphic matrix whitening.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` - matrix whitening
  perturbation split before \(\Phi_K\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799` - explicit matrix
  Frechet derivative \(D\mathcal W_{(0)}\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2526` - scalar
  corrected-whitening transfer after \(\Phi_K\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` - one-pair
  pair-kernel-linear pre-whitening block bookkeeping.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474` - schematic two-pair
  quotient odd-germ decomposition.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11616` - defect theorem
  assumes cubic/quintic/septic quotient defects.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-11932` - abstract source
  criterion after an actual package is supplied.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11994-12009` - conditional
  source-level realization of the actual corrected two-pair finite-order
  package.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12227` - remaining
  source-level input and rejection of the naive source-summed whitened model.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-verifier-source-UV024-prePhi-coefficient/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-192320-explorer-UV023-Lh-source-input/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-184004-gap-closer-UV022-linearized-whitening-functor/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194309-gap-closer-UV024-actual-source-block/notes/actual-source-block-map.md`.

# Dependencies

- A definition of the actual two-atom corrected pre-whitening block triple
  \(\mathcal B_2(a_1,h_1;a_2,h_2)\) with source tags.
- A pair-kernel filtration \(\mathcal K\) on that block triple compatible with
  the one-pair kernels \(U_\pm,E_\pm,G_\pm,V\).
- A theorem identifying the pair-kernel-linear derivative of
  \(\mathcal B_2\) with \(a_1L_{h_1}+a_2L_{h_2}\).
- A definition of the matrix cross-effect \(C\) produced from this
  \(X^{[1]}\), still before \(\Phi_K\).
- UV-024's downstream coefficient and quotient-gauge data:
  \(B_7^{\mathfrak f}(C)\), \(Q_{7,m}^q(C)\), \(\Pi_{1,1}\), and
  \(B_7^{\mathfrak f}((1-\Pi_{1,1})C)\in
  \mathbf C A_5^{\mathfrak f}(m)\).

# Strongest objection

The one-pair \(L_h\) candidate is only a linear part of one-pair block
bookkeeping. Without an actual two-atom block triple, \(X^{[1]}\) could be a
postulated input rather than a source-derived object. That would repeat the
same mistake as the rejected signed source-weight lift: it would impose
linearity after choosing a transport object, rather than proving source
linearity before whitening and before \(\Phi_K\).

# Needed for promotion

1. Add an upstream definition of
   \[
   \mathcal B_2(a_1,h_1;a_2,h_2)
   =(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
   \]
   in the collision chart before whitening.
2. Define \(L_h\) as the one-pair pair-kernel-linear derivative of the
   \(\mathfrak D_Q\)-scaled corrected block triple.
3. Prove the actual two-atom source-linear derivative theorem
   \[
   \operatorname{Lin}_{\mathcal K}
   \mathfrak D_Q(\mathcal B_2-\mathcal B_0)
   =a_1L_{h_1}+a_2L_{h_2}.
   \]
4. Specify how higher pair-kernel terms are kept separate from source bidegrees
   before applying \(\Pi_{1,1}\).
5. Then return to UV-024 proper: define \(C\), \(B_7^{\mathfrak f}(C)\),
   \(Q_{7,m}^q(C)\), and prove the non-\((1,1)\)
   \(A_5^{\mathfrak f}\)-gauge theorem.

# Autoresearch next step

continue: split the target and attack the upstream definition. Draft the
minimal source theorem for \(\mathcal B_2\) and its
\(\operatorname{Lin}_{\mathcal K}\) derivative, using
`proof_of_rh.tex:2659-2787` as the one-pair model and explicitly excluding the
post-whitening signed source lift.

verify: source verifier should check whether any existing "actual corrected
two-pair finite-order package" language can be upgraded to a pre-whitening
matrix block triple, or whether it is only a quotient-output assumption.

blocked: no process blocker. Mathematical blocker is the missing actual
two-atom pre-whitening block triple and its pair-kernel-linear derivative
theorem.

terminal: terminal for claiming current source already supplies the actual
source block. Not terminal for the route once the new upstream definition is
added.

Honest verdict: the route fails from current sources as a proof, but it gives a
clean next object. The smallest missing object is the actual two-atom
pre-whitening corrected block triple \(\mathcal B_2\) plus the theorem that its
pair-kernel-linear derivative is \(a_1L_{h_1}+a_2L_{h_2}\).

# Ledger destination

uv.md - propose a new upstream UV for the actual source-linear two-atom
pre-whitening block theorem; attempts.md - record this route as `keep` because
it reduces UV-024 to the smallest missing source object and recommends the
split.
