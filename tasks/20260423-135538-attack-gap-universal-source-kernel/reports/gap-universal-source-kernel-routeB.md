# Claim

[confirmed] If the quotient-phase theorem is supplied, then the single-zero strip-edge kernel and its pointwise positivity are plausibly universal at the completed-object level, but the local theorem used by the manuscript is still not universal. What remains family-specific is the realization package: the exact background term, compact-interval convergence and regularization, the identification of the background-subtracted scalar with the leading local value channel, and the denominator / whitening / boundary estimates needed to use that scalar.

This changes the roadmap only by sharpening the split of labor.

- [proved] The kernel theorem and its positivity can be treated as family-agnostic once they are derived from a completed quotient of the form `\phi_F(s)=\Lambda_F(2s-1)/\Lambda_F(2s)`.
- [conditional] Dirichlet and Ramanujan-`\tau` then stop needing a new single-zero kernel search. They still need family-specific source theorems and local realization theorems.
- [missing] No current note closes the step from `phase-channel candidate` to `realized positive value-channel coefficient` in either family.

# Status

open

# Evidence

## Proved

1. The current notes already separate the kernel layer from the source/realization layer. `source_theorem_gap.md` says the safe boundary is `kernel theorem proved; source theorem still conditional`, and lists the missing source items as quotient identification, normalization, multiplicity, convergence, and full background bookkeeping. So the notes already support a universal-kernel reading more strongly than a universal source theorem or realization theorem.

2. `scattering_generalization.md` identifies the robust object as a positive strip-edge zero kernel rather than a raw critical-line value surrogate, with single-zero contribution
\[
f_{\beta,\gamma}(m)=\Re\!\left((1+2im-\rho)^{-1}-(2im-\rho)^{-1}\right).
\]
That note also says explicitly that the upgrade is only in candidate-object selection and does not supply Dirichlet or tau realization theorems.

3. `quotient_phase.md` pushes the same separation one step further: the completed quotient
\[
\phi_F(s)=\Lambda_F(2s-1)/\Lambda_F(2s)
\]
is a serious boundary phase candidate for primitive Dirichlet and tau, but only at the phase-channel level. The note is explicit that this does not produce a realized positive `S(m)`-analogue, the leading value-channel coefficient theorem, denominator comparability, whitening, microscopic boundary control, or localization.

4. `tau_localization.md` confirms that even in the cleaner self-dual degree-`2` case, the open work is not the existence of a plausible phase object but the five family-specific checkpoints: source decomposition and curvature/tail package, denominator comparability and holomorphy radius, same-point/mixed-block scaling hierarchy, whitening gain and boundary estimate, and any crude growth bookkeeping beyond the local theorem.

These four notes together support the split:

- universal single-zero kernel: yes, at the level of the candidate completed quotient and its strip-edge zero contribution;
- universal positivity: yes, because positivity is built into the same one-zero kernel formula once `0\leq \beta\leq 1`;
- family-specific background / convergence / realization: still yes, and still the actual obstruction.

## Conditional on [the quotient/source theorem for the family]

5. If one proves for a family `F` that the manuscript phase derivative comes from the quotient `\phi_F`, then the single-zero contribution formula is expected to be uniform across zeta, primitive Dirichlet, and tau up to the family's background terms and normalization conventions. Under that hypothesis, the roadmap improves because one no longer needs separate kernel inventions for each family. One can instead attack three narrower family-specific targets:

- source theorem: identify `q_F` with the completed quotient phase derivative, with correct sign, branch, factor-of-`2`, and multiplicity convention;
- background/convergence theorem: isolate the full gamma/trivial-zero/pole/Hadamard background and prove the compact-interval regularized zero-sum statement;
- realization theorem: show that the resulting background-subtracted scalar is the positive coefficient of the leading local value channel with the same denominator and boundary architecture used by the manuscript.

6. Under that conditional split, Dirichlet benefits in two ways. First, the quotient theorem would remove pressure to discover a new family-specific one-zero kernel. Second, it clarifies that the remaining choice is about realization, not kernel sign: whether a single rotated channel already yields the correct positive scalar amplitude, whether the safer paired `((\chi,\bar\chi))` scalar route is needed, or whether one must pass to a matrix package. The quotient idea narrows the search, but does not decide among these realization modes.

7. Under the same conditional split, tau benefits more cleanly because self-duality makes the scalar phase channel less ambiguous. So tau becomes the cleanest test case for a family-specific realization theorem built on a universal kernel. But `tau_localization.md` is explicit that none of the five localization checkpoints is discharged by that alone, so the gain is roadmap simplification, not closure.

## Missing

8. There is still no theorem in these notes that turns the universal kernel into a universal local theorem. The missing bridge is not only source bookkeeping. It is also the family-local identification of the positive background-subtracted scalar with the coefficient of the manuscript's leading value channel. Without that step, one has a positive kernel sum but not yet the object that drives calibration, whitening, and contradiction.

9. The family-specific background remains real work. Even if the zero kernel is universal, the gamma factor, trivial zeros, poles, conductor terms, and any Hadamard constant are family-dependent. Their subtraction and normalization determine what the correct `B_F` is and therefore what `S_F=q_F-B_F` actually means.

10. The compact-interval convergence/regularization statement remains family-specific in practice. Different degrees and archimedean factors change the bookkeeping for shell convergence, termwise differentiation, and the exact background needed to convert the quotient-side expression into an honest scalar on singularity-free compact intervals.

11. The microscopic realization remains family-specific. For Dirichlet and tau, nothing in the quotient-phase or scattering notes proves the analogue of the manuscript's corrected local deformation with a positive scalar coefficient, nor the denominator comparability, preserved whitening gain, or `Q^{-3}`-scale boundary estimate that the odd-germ/projector layer uses.

12. Honest verdict: if the quotient theorem exists, the universal-kernel idea survives pressure-testing. But it buys only a cleaner modular roadmap: universal kernel and positivity upstairs, family-specific realization downstairs. The actual gap for Dirichlet and tau remains the downstairs realization package.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:6-18,39-62,73-83`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:6-18,22-40,42-53`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:6-18,25-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:6-22,23-49,50-55`
- `/mnt/c/workspace/riemann2/tasks/20260423-132333-attack-gap-source-theorem-gap/reports/gap-source-theorem-routeB.md:3-31,75-94`
- `/mnt/c/workspace/riemann2/tasks/20260423-133143-attack-gap-quotient-phase-generalization/reports/gap-quotient-phase-routeB.md:5-43,68-80`
- `/mnt/c/workspace/riemann2/tasks/20260423-053621-attack-gap-tau-localization/reports/gap-tau-localization-routeB.md:7-14,23-43,62-72`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299,753-777,1528-1566,2060-2087,2214-2322,2977-3169`

# Dependencies

- A family-by-family quotient/source theorem identifying the manuscript phase derivative with `\phi_F(s)=\Lambda_F(2s-1)/\Lambda_F(2s)` and fixing sign, branch, factor-of-`2`, and multiplicity.
- An explicit family background theorem isolating gamma, trivial-zero, pole, conductor, and any Hadamard terms into `B_F`.
- A compact-interval convergence and regularization theorem for the resulting zero-kernel sum.
- A family-local realization theorem proving that the background-subtracted scalar enters the corrected local deformation as the leading positive value-channel coefficient.
- Family-specific denominator comparability, whitening, and microscopic boundary control.

# Strongest objection

The universal-kernel split could be too optimistic. Even if the one-zero formula is formally identical across completed quotients, the manuscript does not use the kernel in isolation. It uses a specific scalar `S(m)` inside a local value-channel theorem with calibration and boundary estimates. If some family realizes the quotient phase but fails to turn `q_F-B_F` into the right positive local coefficient, then the kernel is universal in a weak sense only and the real theorem remains family-specific almost from the start.

# Needed for promotion

- Prove the quotient/source theorem in at least one non-zeta family with full normalization and background bookkeeping.
- State the universal theorem with a strict boundary: `single-zero kernel and positivity universal once the quotient theorem exists`.
- State separately the family-specific theorem: `background, convergence, and local realization remain to be proved family by family`.
- For primitive Dirichlet, decide whether the realized positive scalar comes from a single rotated channel, a paired `((\chi,\bar\chi))` scalar, or a matrix package.
- For tau, attack the five localization checkpoints as the cleanest first realization test.
