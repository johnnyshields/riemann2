# Claim

The single-zero strip-edge kernel is universal only in the following scoped sense: once a family has a proved quotient/source theorem identifying its relevant strip-edge scalar with a fixed signed and normalized restriction of
\[
\partial_s\log \phi_F(s),\qquad \phi_F(s)=\frac{\Lambda_F(2s-1)}{\Lambda_F(2s)},
\]
the one-zero contribution is forced by local quotient algebra and has the same rational profile across families, up to multiplicity and one global sign/factor convention.

The stronger conclusion is not safe. From current repo scope alone, the kernel is not yet universal as a manuscript-level source object, because the paper uses a specific background-subtracted scalar `S(m)` inside a leading local value-channel theorem, and that realization package is still family-specific.

The strongest safe roadmap sentence is:

`Once a family-specific quotient/source theorem identifies the exact S-slot scalar, no new one-zero kernel theorem is needed; the remaining work is family-specific background, convergence, and local realization.`

Claims needing scoped weakening:

- weaken `the kernel is universal across completed L-functions` to `the one-zero quotient kernel is universal once the same quotient/source architecture is proved`;
- weaken `only bookkeeping remains` to `after quotient identification, the remaining gap is explicit background, normalization, convergence, and local realization bookkeeping, not a new kernel search`;
- weaken any statement that the quotient theorem already gives the manuscript scalar to `the quotient theorem supplies only the upstairs phase/kernel channel unless the exact S-slot realization is separately proved`.

# Status

open

# Evidence

## Proved

The archive source slice gives an exact zeta-model decomposition with
\[
q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)
\]
on compact intervals away from real singularities, where a single zero contributes the strip-edge profile obtained from the numerator-zero / denominator-pole pair of
\(
\phi(s)=\Lambda(2s-1)/\Lambda(2s)
\).
This local derivation uses only quotient algebra near a zero, so the rational profile itself is family-agnostic at that level.

The two upstream notes already separate this kernel layer from the source-realization layer. `scattering_generalization.md` says the candidate object is a positive strip-edge zero kernel, but also says this is only a channel-selection upgrade and does not yet realize Dirichlet or tau theorems. `source_theorem_gap.md` is more explicit: `kernel theorem proved; source theorem still conditional`.

The manuscript also shows why the stronger universality claim is unsafe. Its local theorem is not stated directly in terms of the quotient kernel. It is stated in terms of a specific scalar `S(m)` that enters the corrected local deformation as the coefficient of the leading value channel,
\[
\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
\]
and downstream boundary and odd-microscopic estimates are expressed in that same `S(m)` slot. So universality of the one-zero quotient kernel does not by itself imply universality of the manuscript's source scalar.

## Conditional on [family-specific quotient/source theorem]

If a family `F` proves the analogue of the archived zeta formula with the exact scalar occupying the manuscript's `S(m)` slot, then the one-zero contribution is indeed universal upstairs: every nontrivial zero contributes through the same pair
\(
s=\rho/2
\)
and
\(
s=(1+\rho)/2
\),
hence through the same strip-edge rational kernel, with only multiplicity, background, and one global normalization depending on the family.

Under that hypothesis, the roadmap does simplify. One no longer needs a new family-specific one-zero kernel invention. The remaining work is to prove the full family source theorem, isolate the background term, control compact-interval regularization/convergence, and show that the resulting background-subtracted scalar is exactly the positive leading value-channel coefficient used by the local deformation.

## Missing

The decisive missing step is the downstairs realization package. The notes explicitly say the repo does not yet prove an explicit completed-quotient formula for the draft's own `q`, nor the sign/branch/factor-of-`2` normalization theorem, nor the one-zero source identity in family notation, nor the compact-interval convergence and background unification, nor the identification of the background-subtracted scalar with the manuscript's leading local value channel.

For non-self-dual or complex families the gap is sharper: quotient algebra alone does not automatically yield the real positive scalar needed by the manuscript. Even if the local kernel inside `\partial_s\log \phi_F` is universal, the actual scalar feeding calibration, whitening, and boundary estimates may still require pairing, rotation, or matrix packaging. From quotient algebra alone, that realization is missing.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:6-18,39-62,73-83`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-18,22-53`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-16,17-24,28-50`
- `/mnt/c/workspace/riemann2/tasks/20260423-135538-attack-gap-universal-source-kernel/reports/gap-universal-source-kernel-routeA.md:5-26,57-63,68-78,111-123,137-168`
- `/mnt/c/workspace/riemann2/tasks/20260423-135538-attack-gap-universal-source-kernel/reports/gap-universal-source-kernel-routeB.md:3-9,17-25,41-63,77-95`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5530-5598`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1498-1565,2060-2087,2214-2232`

# Dependencies

- A family-specific theorem identifying the relevant phase/source scalar with a fixed signed and normalized strip-edge restriction of `\partial_s\log \phi_F`.
- An explicit multiplicity convention for zero contributions.
- A full family background theorem isolating gamma, trivial-zero, pole, conductor, and any Hadamard terms.
- A compact-interval convergence or regularization theorem for the zero-kernel sum plus background.
- A local realization theorem proving that the resulting background-subtracted scalar is exactly the manuscript's leading value-channel coefficient.

# Strongest objection

`Universal kernel` can be technically true and still be too weak to matter. The manuscript never uses the one-zero strip-edge kernel in isolation; it uses a very specific scalar `S(m)` inside a corrected local deformation, then pushes that scalar through whitening, boundary control, and odd-channel localization. If a family realizes the quotient phase but not the same positive `S`-slot coefficient, then the universality claim is only an upstairs algebra fact and not a universal source theorem in the sense that the draft needs.

# Needed for promotion

- State the theorem with a hard boundary: `the one-zero quotient kernel is universal once the same quotient/source theorem exists`.
- State separately that `background, convergence, normalization, and S-slot realization remain family-specific`.
- Produce one non-zeta family realization with full sign, branch, factor-of-`2`, multiplicity, and background bookkeeping.
- Check explicitly, especially in non-self-dual settings, whether the realized scalar is a genuine real positive scalar, a paired scalar, or only a matrix-valued object.

Honest verdict: the single-zero strip-edge kernel survives the attack only in a scoped upstairs sense. It is not yet safe to call it a universal manuscript-level source kernel merely from the existence of the quotient/source template; the safe conclusion is a modular roadmap, not a realized universality theorem.
