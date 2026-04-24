## Claim

The patch unit is close to the right granularity, but only in the narrow two-step sense already isolated upstream: one source-normalization subsection, then one bundled localized source theorem on a compact singularity-free interval. The proof skeleton is not yet safe if it is read as proving more than the normalized source identity itself. The strongest safe RH-facing theorem-proof plan is:

"After fixing the quotient/phase normalization and the scoped identification of the active zeta-source phase derivative, prove on any compact interval avoiding the real singular set one bundled localized source theorem that establishes only the normalized identity
\[
q(t)=B_{\mathrm{src}}(t)+\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(t)
\]
in the theorem's stated regularized sense; then recover the manuscript notation `q=B_\zeta+S` and the midpoint scalar `S(m)` by immediate scoped convention/corollary text."

Three-bin separation.

- proved: the paper's real insertion point is local and early in `\section{Zeta-side decomposition}`; downstream dependence is concentrated in the scalar slot `S(m)`; the one-zero kernel calculation is not the main unresolved obstacle.
- conditional on the normalization package: the theorem-sized unit should be one bundled compact-interval source theorem, not several mini-theorems.
- missing: a canonical paper-level compact-interval summation/regularization statement in exactly the manuscript-facing normalization, and a theorem-level proof of any exact background-name identification.

Claims that need scoped weakening:

- `q=B_\zeta+S` should not be presented as already canonical source-theorem output until the quotient, boundary phase, and `q`/`q_\zeta` bridge are fixed in the paper.
- `S(m)=q_\zeta(m)-B_\zeta(m)` should be treated as manuscript notation specialized from the normalized source object, not as an already justified canonical identity.
- Any sentence that says the new theorem "justifies the manuscript's `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`" needs weakening to a scoped correspondence statement unless exact aliasing is proved at theorem level.
- Any sentence that says the bundle gives the decomposition without qualification should specify "on compact intervals avoiding the real singular set" and, where needed, "in the theorem's stated regularized sense."

## Status

open

## Evidence

[confirmed] Granularity.

- The upstream patch-plan note, source-package note, and route B all converge on the same safe unit: first normalize the quotient/phase bridge, then prove one bundled localized source theorem, with background identification and multiplicity handled after the theorem rather than overloaded into it.
- This matches the actual cut point in the paper, where the draft first shifts from abstract phase geometry to zeta-specific source data through `q=B_\zeta+S`, `g_{\sm}=B_{\Aut}+T_{\far}`, and `S(m)=q_\zeta(m)-B_\zeta(m)`.

[confirmed] What is already genuinely upstream.

- The paper already defines the abstract phase derivative `q(t):=\Phi'(t)` before the zeta-side section.
- The archived source derivation supplies the quotient-side template: decompose `\partial_s\log\phi`, isolate one zero's pole-zero pair, take the real part, and then sum over zeros on a compact singularity-free interval.
- The one-zero computation itself is therefore not the main adversarial target. The target is the jump from that atomic identity to a theorem the paper can honestly cite in its own normalization.

[conditional on fixed normalization] What is supportable.

- If the paper fixes
  \[
  \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
  \qquad
  \phi\!\left(\tfrac12+it\right)=e^{2i\Phi(t)},
  \qquad
  \left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t),
  \]
  then one bundled compact-interval theorem is the right theorem-sized unit.
- But the theorem body is safe only if it concludes the normalized source identity itself, with its interval and summation scope stated explicitly.

[missing] What still blocks a stronger paper-facing claim.

- The current paper does not yet contain a canonical theorem-proof block for the compact-interval limit or regularization step. Route A names this as the key summation step; the archive derivation states the result but does not discharge the paper-level promotion burden by itself.
- The current draft uses three background names with different local roles: `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`. The background-unification note explicitly says exact identity is not yet safe theorem-body content.
- The current draft also mixes `q` and `q_\zeta` locally. The q-notation note says this clash is local enough for a subsection repair, but not local enough for a one-line silent identification.
- The archived chat still uses the negative boundary convention `\phi(1/2+it)=e^{-2i\Phi(t)}`. The normalization note says the factor-of-2 is fine but the sign is live. So any proof skeleton that treats normalization as already harmless is overstated.

Honest proof-state separation.

- proved: the patch is localized, the cut point is right, and one bundled theorem is the right theorem-sized object after normalization.
- conditional on the fixed normalization package: the theorem can feed the later `S(m)`-driven local machinery without redesigning the endgame.
- missing: theorem-level summation/regularization language, theorem-level exact background aliasing, and theorem-level justification for any silent `q=q_\zeta` identification.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-32`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/q_notation.md:8-36`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63,106-125`
- `/mnt/c/workspace/riemann2/tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/reports/gap-zeta-source-proof-skeleton-routeA.md:3-94,124-184`
- `/mnt/c/workspace/riemann2/tasks/20260424-024455-attack-gap-zeta-source-proof-skeleton/reports/gap-zeta-source-proof-skeleton-routeB.md:5-31,47-67`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-301`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1505`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1527-1622`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2058-2209`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26326`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:620-661`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`

## Dependencies

- A front-loaded source-normalization subsection fixing the quotient, boundary-phase orientation, and the scoped specialization from the active manuscript `q` to the zeta-source derivative.
- An explicit theorem statement on a compact interval avoiding the real singular set.
- A canonical compact-interval summation or regularization statement in exactly the normalization used by the theorem.
- A scoped post-theorem correspondence block for background notation and multiplicity, unless those are proved in the theorem body itself.
- A later-language audit so downstream uses of `q`, `q_\zeta`, `B_\zeta`, `B_{\Aut}`, `B_{\bg}`, and `S(m)` do not claim stronger provenance than the theorem actually gives.

## Strongest objection

The strongest objection is that the current proof skeleton is still vulnerable to notation laundering. It can look finished because the one-zero kernel computation is clear and the downstream paper already uses `S(m)`, but the real unresolved burden is the theorem-level passage from quotient log-derivative bookkeeping to a compact-interval normalized source identity in a stated summation mode. If that burden is hidden inside phrases like "bundled localized source theorem" or "justify the manuscript notation," then the patch will overstate what has been proved. A second objection is that exact aliasing among `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` is not yet safe from current scope alone; claiming that aliasing inside the theorem would be stronger than the cited notes support.

## Needed for promotion

- Keep the patch unit exactly two-step: normalization subsection first, bundled source theorem second.
- Keep the theorem body narrow: conclude only the normalized compact-interval source identity, with interval scope and summation mode stated explicitly.
- State the bridge to manuscript notation as scoped convention/corollary text immediately after the theorem, not as silent theorem-body fallout.
- Weaken all exact-background-identification language to correspondence-in-scope language unless exact aliasing is separately proved.
- Weaken all `q=B_\zeta+S` and `S(m)=q_\zeta(m)-B_\zeta(m)` language to manuscript-facing specialization language until the source-normalization subsection has fixed the `q`/`q_\zeta` bridge.
- Keep multiplicities explicit wherever the theorem introduces or sums over zeros.

Honest verdict: the patch unit is now basically right, but the proof skeleton is safe only if the theorem is narrower than its surrounding prose. The safe endpoint is one normalized compact-interval source identity. Exact background aliasing, silent `q=q_\zeta`, and any unqualified passage from regularized source sums to manuscript notation still need scoped weakening.
