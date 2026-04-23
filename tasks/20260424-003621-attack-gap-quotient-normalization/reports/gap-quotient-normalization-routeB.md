Claim

The minimal paper-facing fix is a canonical source-normalization patch at the start of `\section{Zeta-side decomposition}` that does four things and nothing larger: (1) names the scattering quotient `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, (2) fixes the boundary phase convention by declaring `\phi(\tfrac12+it)=e^{-2 i \Phi(t)}` so that `q(t)=\Phi'(t)` and `\partial_s \log \phi(\tfrac12+it)=2q(t)`, (3) states the compact-interval source formula `q=B_\zeta+S` with the single-zero kernel `f_{\beta,\gamma}`, and (4) explicitly identifies the manuscript’s background names `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` as the same source-background term once localized. This removes the present sign/factor ambiguity without redesigning the local jet, whitening, calibration, or odd-channel sections.

Status

open

Evidence

Proved in the current paper:

- The local phase machinery itself is notation-agnostic once a real phase `\Phi` and derivative `q=\Phi'` are supplied: phase kernel, jet blocks, whitening, and finite-`s` formulas are self-contained local algebra in `paper/proof_of_rh.tex:147-269`.
- The paper’s downstream uses of the zeta source data are concentrated in the first zeta-specific block `paper/proof_of_rh.tex:271-299`, then propagated through the value-channel scaling by `B_\zeta(m)` and `S(m)` in `paper/proof_of_rh.tex:431-486`, `2048-2209`, and `2212-2307`.

Conditional on the missing source theorem:

- `paper/proof_of_rh.tex:273-287` introduces `q(t)=B_\zeta(t)+S(t)` and then `S(m):=q_\zeta(m)-B_\zeta(m)`, but the manuscript does not yet prove which completed quotient produces this `q`, what the phase convention is, or why the factor relating `\partial_s\log \phi` to `q` is `2` rather than `1` or `-2`.
- `paper/proof_of_rh.tex:281`, `1489-1505`, and `1529-1536` use three background names: `B_{\Aut}`, `B_{\bg}`, and `B_\zeta`. The archive notes explicitly flag this as an unresolved identification item, not a settled theorem.
- All later uses of `S(m)` as a positive value-channel scalar depend on the same source package, because the manuscript treats `S(m)` as the exact coefficient occupying the leading local slot in `paper/proof_of_rh.tex:1532-1546`, `2060-2087`, and `2236-2285`.

Archive supplies stronger formula-level information than the main paper:

- The archive gives the exact candidate quotient and boundary phase convention: `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, `\phi(\tfrac12+it)=e^{-2 i \Phi(t)}`, hence `q=\Phi'=-\delta'`, at `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5519-5539`.
- It also gives the derivative-level source formula on compact singularity-free intervals:
  `q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)` with
  `f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}`,
  and shows that one zero contributes `2 f_{\beta,\gamma}` to `\partial_s\log\phi(\tfrac12+it)` because `\partial_s\log\phi(\tfrac12+it)=2q(t)`; see `...insight.md:5541-5598`.
- The GRH/RH notes now summarize this as the first component of the missing zeta source package: quotient / phase normalization first, then single-zero contribution, compact-interval summation, background identification, and multiplicity convention; see `grh/.../notes/zeta_source_package.md:16-30`, `grh/.../notes/rh_patch_plan.md:23-31`, and `grh/.../notes/source_theorem_gap.md:31-40`.

Minimal patch plan implied by those facts:

- Insert one canonical zeta-source subsection at the start of `\section{Zeta-side decomposition}`, exactly where `paper/proof_of_rh.tex:271-299` currently begins using zeta-specific notation.
- State only the normalization shell needed by the rest of the paper:
  `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`;
  on singularity-free compact intervals choose `\Phi` by `\phi(\tfrac12+it)=e^{-2 i \Phi(t)}`;
  define `q=\Phi'` so `\partial_s\log\phi(\tfrac12+it)=2q(t)`.
- Then state the source split with one fixed background name, preferably `B_\zeta`, and a sentence identifying `B_{\Aut}` and `B_{\bg}` as the same term in later local decompositions.
- Replace the isolated `q_\zeta` in `S(m):=q_\zeta(m)-B_\zeta(m)` by the already-defined `q(m)` or define `q_\zeta:=q` once. As written, `q_\zeta` appears only there and creates avoidable ambiguity.
- Leave `A_{\val}`, whitening, corrected deformation, and odd-channel sections unchanged except for dependency wording pointing back to the new source-normalization subsection.

Missing:

- A proved theorem in the paper that the manuscript’s `q=\Phi'` is the boundary phase derivative of `\phi(s)=\Lambda(2s-1)/\Lambda(2s)` with the stated sign and factor-of-2 convention.
- A proved compact-interval regularized summation theorem turning the archived zero-by-zero formula into the manuscript’s exact `q=B_\zeta+S` statement.
- An explicit multiplicity convention and a single canonical background identification.

Exact refs

- Main dependency cut point: `paper/proof_of_rh.tex:271-299`.
- Local notation before zeta specialization: `paper/proof_of_rh.tex:147-269`.
- First value-channel scaling by `B_\zeta` and `x=B_\zeta(m)\sigma`: `paper/proof_of_rh.tex:431-486`.
- Source-dependent corrected deformation and `S(m)` slot: `paper/proof_of_rh.tex:1471-1621`.
- Source-dependent calibration and boundary estimates: `paper/proof_of_rh.tex:2050-2209`, `2212-2307`.
- Ambiguous isolated symbol `q_\zeta`: `paper/proof_of_rh.tex:285-287`.
- Background-name split across `B_\zeta`, `B_{\Aut}`, `B_{\bg}`: `paper/proof_of_rh.tex:275-283`, `1483-1505`, `1529-1536`.
- Archive quotient and phase normalization: `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5519-5539`.
- Archive single-zero and compact-interval formula: `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5541-5598`.
- Patch-plan notes: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`, `.../notes/zeta_source_package.md:16-30`, `.../notes/source_theorem_gap.md:16-40`, `.../notes/scattering_generalization.md:21-37`.

Dependencies

- Quotient / phase normalization theorem for `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`.
- Single-zero source contribution identity on the boundary line.
- Compact-interval convergence / regularization statement for summing the zero contributions.
- Explicit background identification `B_\zeta = B_{\Aut} = B_{\bg}` in manuscript notation.
- Stated zero multiplicity convention.

Strongest objection

From current paper scope alone, the proposed patch is still conditional at its front end: the archive provides a credible normalization formula, but the main draft does not yet prove that its `\Phi` is the branch of the scattering phase satisfying `\phi(\tfrac12+it)=e^{-2 i \Phi(t)}`. Without that theorem, inserting the quotient formula as if already established would overstate the paper. The smallest safe patch is therefore a canonical source-normalization subsection whose claims are explicitly labeled as the needed zeta-source theorem package, not an unqualified retrospective gloss.

Needed for promotion

- Write and prove one short source-normalization theorem at the start of `\section{Zeta-side decomposition}` with the exact convention `\phi(\tfrac12+it)=e^{-2 i \Phi(t)}` and `\partial_s\log\phi(\tfrac12+it)=2q(t)`.
- State the single-zero contribution formula and the compact-interval summation/regularization in the same subsection.
- Collapse the background notation to one canonical symbol and delete the isolated `q_\zeta` ambiguity.
- Then update later dependency language only; no redesign of the surrounding sections is needed.

Honest verdict: the ambiguity is localized and the minimal fix is clear, but it is not yet proved in the main paper. The smallest canonical patch is a front-loaded source-normalization theorem package, not a global rewrite.
