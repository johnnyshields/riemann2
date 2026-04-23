# gap-zeta-source-proof-skeleton-routeB

**Claim**

The smallest theorem package that is safe to promote into `paper/proof_of_rh.tex` is a two-step proof-skeleton patch at the start of `\section{Zeta-side decomposition}`: first a source-normalization subsection fixing the quotient, boundary-phase orientation, and the scoped identification of the manuscript's `q` with the zeta-source derivative; then one bundled compact-interval localized source theorem whose theorem body states only the normalized source identity needed to justify `q=B_\zeta+S` and `S(m)` on singularity-free compact intervals. Background-name unification and multiplicity should appear immediately after as scoped convention/corollary text, not inside the theorem body.

**Status**

conditional

**Evidence**

proved:
- The exact paper-facing cut point is `paper/proof_of_rh.tex:271-301`, where the draft first stops speaking in generic phase-kernel language and starts using zeta-specific source data through `q=B_\zeta+S`, `g_{\sm}=B_{\Aut}+T_{\far}`, and `S(m):=q_\zeta(m)-B_\zeta(m)`. This matches the patch-plan note's cut point and promotion target.
- Downstream sections already use one scalar slot, namely `S(m)`, as the load-bearing source input for calibration and the corrected local deformation. So one localized source theorem can feed the later proof skeleton without pulling in endgame redesign. See `paper/proof_of_rh.tex:739-779`, `paper/proof_of_rh.tex:1527-1621`, `paper/proof_of_rh.tex:2058-2209`.
- The archive and source-theorem note support the intended source object `\phi(s)=\Lambda(2s-1)/\Lambda(2s)` and a compact-interval source theorem shape, but they also separate what is already safe from what is still conditional. See `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63,64-77,106-125`.

conditional on prior normalization:
- The proof skeleton can safely absorb the notation cleanup `q=q_\zeta` inside the new source-normalization subsection, because the clash is local at the section boundary and the rest of the proof mainly uses `S(m)` and `B_\zeta(m)`. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/q_notation.md:8-36`.
- The proof skeleton can also absorb one canonical background symbol there, with role-level aliases for existing lane names. But exact equality of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` is not yet safe theorem-body content. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`.
- The compact-interval source theorem is the right theorem-sized unit, but only after the quotient/phase bridge is fixed and the source sum is stated at the correct theorem level. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:23-32` and `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:106-125`.

missing:
- A canonical orientation choice compatible with the manuscript-wide convention `q(t):=\Phi'(t)`. The sign issue is live, and until it is fixed the draft should not present `q=B_\zeta+S` as already normalized source theorem content. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49` and `paper/proof_of_rh.tex:149-160,271-299`.
- A theorem-facing compact-interval convergence/regularization statement that turns the archived source derivation into canonical paper content, rather than leaving it as manuscript-level intent. See `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:112-123`.
- A theorem-level proof of exact background aliasing and theorem-level multiplicity handling. Those belong after the theorem for now.

Three-bin separation for the proof skeleton:
- proved: the right insertion point; the need for a front-loaded normalization block; the fact that downstream dependence is concentrated in `S(m)` rather than in a large unrelated source package.
- conditional on one front-loaded normalization block: promoting one bundled compact-interval localized source theorem that justifies the proof skeleton's first zeta-side inputs.
- missing: a fully canonical quotient/phase theorem with settled sign, theorem-body background aliasing, and theorem-body multiplicity.

**Exact refs**

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-301`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:739-779`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1527-1621`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2058-2209`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-32`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/q_notation.md:8-36`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63,64-77,106-125`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:620-641,684-690`

**Dependencies**

- One source-normalization subsection that fixes `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, chooses a boundary-phase orientation compatible with the manuscript's `q`, and states the scope `q=q_\zeta` for the zeta-source lane.
- One bundled compact-interval source theorem proving the localized source identity in normalized notation.
- Immediate post-theorem scoped text for background correspondence and multiplicity bookkeeping.
- A downstream audit so later uses of `S(m)`, `B_\zeta`, `B_{\Aut}`, `B_{\bg}`, and `q_\zeta` do not silently claim more than the theorem proved.

**Strongest objection**

The strongest objection is that even this narrow package may still be too optimistic if the localized source theorem silently needs theorem-body assertions about exact background aliasing or multiplicity-weighted summation. From current paper scope, those items are not yet proved at the same level as the normalized source identity. So the proof-skeleton patch is safe only if the theorem body stays narrow and the cleanup items are explicitly quarantined to post-theorem scoped remarks/corollaries.

**Needed for promotion**

- Insert the source-normalization subsection exactly at the start of `\section{Zeta-side decomposition}`.
- In that subsection, fix the quotient and sign convention before any use of `q=B_\zeta+S` or `S(m)`.
- State one compact-interval localized source theorem whose theorem body justifies the normalized source split and the definition of `S(m)`.
- Keep `q`/`q_\zeta` specialization and one canonical background symbol inside the proof skeleton.
- Move exact background aliasing and multiplicity to immediately following scoped convention/corollary text.
- Audit later language so the rest of the proof skeleton depends only on what this promoted package actually proves.

Honest verdict: the proof skeleton can absorb a small front-loaded zeta-source package, but not the whole cleanup backlog. Promote one normalization subsection plus one localized compact-interval source theorem. Keep `q`/`q_\zeta` and one canonical background symbol inside that patch. Leave exact background aliasing and multiplicity outside the theorem body until they are proved at the same level.
