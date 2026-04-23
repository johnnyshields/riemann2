# gap-q-notation-routeB

**Claim**

The smallest safe patch-plan is a theorem-facing source subsection at the start of `\section{Zeta-side decomposition}` that declares, once, that in the zeta-source lane the manuscript's generic phase derivative `q` is being specialized to the zeta/scattering source quantity `q_\zeta`, after which the paper writes simply `q`. A single global renaming statement is too broad, and a single local specialization at `S(m):=q_\zeta(m)-B_\zeta(m)` is too weak.

**Status**

proved

**Evidence**

Proved:

- The paper defines the generic phase derivative globally by `q(t):=\Ph'(t)` at `paper/proof_of_rh.tex:149-160`.
- The first zeta-source split occurs exactly at the start of `\section{Zeta-side decomposition}`: `q(t)=B_\zeta(t)+S(t)` at `paper/proof_of_rh.tex:271-287`.
- The only surviving `q_\zeta` occurrence in the paper is `S(m):=q_\zeta(m)-B_\zeta(m)` at `paper/proof_of_rh.tex:285-288`.
- Because `q_\zeta` appears only there, a one-line local edit would remove the literal mismatch, but it would not state where the manuscript passes from the generic phase notation of the earlier sections to the zeta-specific source notation used later.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31` identifies this exact cut point as the place where the draft first starts using zeta-specific source data.

Conditional on the companion normalization patch:

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:24-49` says the safest RH-facing fix is a source-normalization subsection at the start of `Zeta-side decomposition`, and warns that claims such as `q=B_\zeta+S` and `S(m)=q_\zeta(m)-B_\zeta(m)` should currently be read as manuscript notation rather than as a fully normalized canonical source theorem.
- So the strongest safe wording should avoid claiming that the existing draft has already proved a global identity of all phase conventions; it should state only a scoped specialization for the zeta-source discussion.

Missing:

- The paper does not yet contain the source-normalization theorem package that fixes the quotient, boundary phase convention, and the `\phi'/\phi` to `q` bridge flagged in `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`.
- Without that package, a global renaming statement would overstate what has been normalized, and any wording asserting family portability would be unsafe.

Strongest safe wording:

> In this section we pass from the generic phase notation of the local kernel setup to the zeta/scattering source. Let `q_\zeta` denote the zeta-side phase derivative. For the zeta-side decomposition statements below, we specialize the generic quantity `q` to this source quantity and write simply `q=q_\zeta`. Thus the source split is `q(t)=B_\zeta(t)+S(t)`, and in particular `S(m)=q(m)-B_\zeta(m)`.

This is stronger and safer than a bare local replacement `q_\zeta(m) \mapsto q(m)` because it declares the scope once, at the theorem-facing source boundary, without asserting more normalization than the notes currently support.

**Exact refs**

- `paper/proof_of_rh.tex:149-160`
- `paper/proof_of_rh.tex:271-288`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:24-49`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`

**Dependencies**

- The cut-point diagnosis in `rh_patch_plan.md`.
- The scope warning from `quotient_normalization.md`.
- The background-notation advice in `background_unification.md`, which favors one source-side declaration with scoped aliases over diffuse global aliasing.

**Strongest objection**

The proposed subsection is slightly larger than the literal one-line fix, so if the only goal were to remove the token mismatch at line 287, a local edit would be smaller. But that smaller edit leaves the generic-to-zeta specialization implicit at the very place where the draft first becomes source-specific, so it is not the safest patch.

**Needed for promotion**

- Insert the source-facing subsection at the start of `\section{Zeta-side decomposition}`.
- In that subsection, state only the scoped specialization `q=q_\zeta` for the zeta-source lane.
- Replace `S(m):=q_\zeta(m)-B_\zeta(m)` by `S(m):=q(m)-B_\zeta(m)` once that scoped specialization has been declared.
- Keep stronger normalization claims deferred until the quotient/sign/bridge package from `quotient_normalization.md` is actually installed.
- Do not state any endgame consequence or family-portability consequence from this notation repair alone.
