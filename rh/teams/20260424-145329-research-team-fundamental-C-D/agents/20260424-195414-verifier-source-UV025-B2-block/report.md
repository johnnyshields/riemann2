# Claim

The proposed `\mathcal B_2` definition block passes the UV-025 source check at
the pre-whitening level.  Its tagged substitutions use the same corrected phase
variables and the same corrected same-point/mixed block formulas as
`proof_of_rh.tex:2659-2787`.  Once `\mathcal B_2`, `\mathcal K`, and `L_h` are
added as definitions, the tagged identity
`\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}` follows by the cited same-point and
mixed-block Taylor bookkeeping.

This verifies UV-025 only as a pre-whitening block definition/theorem.  It does
not promote UV-024 or UV-026, and it does not identify the downstream whitened
finite-order quotient package.

# Status

proved

# Evidence

Three-bin separation:

- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2617-2626`
  defines the one-pair corrected phase variables
  `d_\pm`, `e_\pm`, `g_\pm`, and `\eta` after midpoint affine-jet removal.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2628-2636`
  writes those variables as
  `d_\pm=(z^2/Q^4)U_\pm`, `e_\pm=(z/Q^2)E_\pm`,
  `g_\pm=G_\pm`, and `\eta=(z^3/Q^6)V`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2699`
  uses the same-point substitutions
  `q=q_0+d_\pm`, `q'=q_0'+e_\pm`, and `q''=q_0''+g_\pm` in the corrected
  same-point block formula.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2700-2722`
  shows the scaled same-point perturbation entries are linear in the pair
  kernels modulo terms containing at least two pair kernels.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2742`
  uses the mixed-block substitutions
  `q_\pm=q_{0,\pm}+d_\pm` and `\Delta=\Delta_0+\eta`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2744-2787`
  Taylor expands the mixed block in `(d_-,d_+,\eta)`; the linear part is a
  bounded-baseline combination of `U_-`, `U_+`, and `V`, and the remainder is
  quadratic in pair kernels.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2427-2439`
  defines the scaling `\mathfrak D_Q` used on perturbation triples; this is the
  same scaling used by the candidate.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2458-2467`
  treats a weighted pre-whitening perturbation triple before scalar transfer,
  matching the level at which `\mathcal B_2-\mathcal B_0` lives.
- **Conditional/output-level only:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474`,
  `11587-11616`, and `11994-12009` still speak about quotient-output packages
  or assumed defects, not the pre-whitening block.
- **Boundary warning:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rejects the naive post-whitening source-summed coefficient package.  The
  proposed `\mathcal B_2` avoids this only because it is pre-whitening and uses
  `\operatorname{Lin}_{\mathcal K}` before scalar/quotient extraction.
- **Missing from current paper:** the tagged `\mathcal B_2` block, filtration
  `\mathcal K`, and theorem are not yet in `proof_of_rh.tex`; they are in the
  candidate note.

Source-check logic:

- The candidate's tagged variables are additive sums of two copies of exactly
  the one-pair variables listed above:
  `d_\pm^{(2)}`, `e_\pm^{(2)}`, `g_\pm^{(2)}`, `\eta^{(2)}`.
- Because the same-point and mixed-block Taylor remainders are at least
  quadratic in these variables, every mixed source product has
  `\mathcal K`-degree at least two.
- Projection to `\mathcal K`-degree one therefore leaves only the tagged
  source-one linear part plus the tagged source-two linear part:
  `\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}`.

No computational script was needed for this source verification.

# Baseline / delta

Baseline: the prior package-language verifier concluded that current paper
language defines only quotient-output package assumptions, and that UV-025
needed a new pre-whitening `\mathcal B_2` definition plus a source computation.
The subsequent gap-closer proposed such a block in
`B2-definition-block.md`.

Delta: this pass verifies the proposed block against the paper's actual
same-point and mixed-block formulas.  The definition is source-compatible, and
the `\mathcal K`-linear identity follows from the existing Taylor bookkeeping
once the definitions are inserted.  The only wording fix is to avoid saying
that this already proves the downstream "actual corrected two-pair finite-order
package"; call it the tagged pre-whitening corrected source lift until package
coincidence is proved separately.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-025 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:56`
  - UV-025 entry.
- Candidate checked:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194928-gap-closer-UV025-B2-definition/notes/B2-definition-block.md`.
- Prior verifier:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194928-verifier-source-UV025-package-language/report.md`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-2048` - corrected blocks,
  whitening map, and matrix perturbation context.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - scaling
  `\mathfrak D_Q`, pre-whitening perturbation triple, and scalar transfer
  boundary.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2597-2787` - one-pair phase
  variables, kernel representation, same-point formula, mixed-block formula,
  and Taylor-linear bookkeeping.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11775` - quotient-output
  two-pair decomposition and defect assumptions.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12255` - abstract output
  source criterion, conditional package language, and post-whitening negative.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-195414-verifier-source-UV025-B2-block/notes/B2-block-source-check.md`.

# Dependencies

- Add the candidate definition of `\mathcal B_2` to the paper.
- Add the formal source tags `\tau_1,\tau_2`.
- Define `\mathcal K` and `\operatorname{Lin}_{\mathcal K}` before applying
  whitening, `\Phi_K`, determinant scalarization, or quotient extraction.
- Define `L_h` as the one-atom `\mathcal K`-linear scaled corrected-block
  triple.
- Keep downstream package-coincidence, UV-024 coefficient compatibility, and
  UV-026 cubic gauge theorem separate.

# Strongest objection

The proposed `\mathcal B_2` is actual for the pre-whitening block formulas only
after the paper declares it as the tagged source lift.  The existing paper does
not yet prove that the quotient-output package `\mathfrak P_2` is induced from
this lift after whitening and coefficient extraction.  Without that later
package-coincidence theorem, UV-025 can be closed while UV-024/UV-026 remain
fully open.

# Needed for promotion

1. Insert the `\mathcal B_2` definition using the candidate's tagged variables.
2. State explicitly that `d_{h_i,\pm}`, `e_{h_i,\pm}`, `g_{h_i,\pm}`, and
   `\eta_{h_i}` are the one-atom variables defined as in
   `proof_of_rh.tex:2617-2626`, with the affine jet removed before tagging.
3. Define `\mathcal K` on tagged kernels
   `\tau_iU_{i,\pm}`, `\tau_iE_{i,\pm}`, `\tau_iG_{i,\pm}`, and `\tau_iV_i`.
4. Prove the tagged identity by citing the same-point linear/remainder split
   at `proof_of_rh.tex:2700-2722` and the mixed-block Taylor split at
   `proof_of_rh.tex:2744-2787`.
5. Add a boundary sentence: this theorem is pre-whitening and does not assert
   quotient-output package coincidence or any UV-024/UV-026 gauge result.

# Autoresearch next step

continue: prepare a paper-updates candidate from `B2-definition-block.md` with
the wording fix above: "tagged pre-whitening corrected source lift" rather than
unqualified "actual corrected two-pair finite-order package."

verify: after insertion text is drafted, run an adversarial/source pass focused
only on two risks: tags being forgotten before `\operatorname{Lin}_{\mathcal K}`,
and accidental promotion of downstream quotient package coincidence.

blocked: no process blocker.  UV-025's remaining blocker is coordinator paper
insertion; downstream mathematical blockers stay in UV-024/UV-026.

terminal: terminal for the source-check question.  The candidate uses the same
phase variables/formulas and the `\mathcal K`-linear theorem follows from the
cited Taylor bookkeeping, within UV-025's pre-whitening scope.

Honest verdict: positive for UV-025.  This is a definition/theorem addition,
not a new hard source computation, provided the text keeps the downstream
quotient-package claims out of scope.

# Ledger destination

paper-updates.md - stage the verified `\mathcal B_2` definition/theorem with
the wording guardrail; attempts.md - record this source verification as `keep`.
