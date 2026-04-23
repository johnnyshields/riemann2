Claim

For an exact paired-source theorem inside primitive Dirichlet families, the cleanest first subclass is primitive nonprincipal complex characters, with an optional first-pass restriction to one fixed parity at a time. Real primitive nonprincipal characters are cleaner as self-dual single-channel objects, but that same self-duality makes a paired theorem less natural there: pairing no longer resolves a front-end ambiguity and instead repackages one channel as a square. By contrast, for genuinely complex primitive characters the paired object
\[
\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi),
\qquad
\Phi^{\mathrm{pair}}_\chi(s)=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}
\]
is already the repo's conservative theorem-facing choice, because pairing removes the non-self-dual front-end asymmetry and gives a canonical scalar package. The parity restriction is only a theorem-statement simplifier: it freezes the archimedean case split in the background term, but it is not currently proved to reduce the deeper source-to-slot burden.

Status

heuristic

Evidence

Proved.

- The project-level ranking already says that, from current scope alone, the best non-zeta realization target is the primitive-Dirichlet paired-scalar exact-source theorem. That is direct support for choosing a paired theorem in the primitive complex Dirichlet setting rather than in a new matrix package or a single rotated channel.
- The paired-object and paired-quotient notes identify the clean theorem-facing paired package explicitly: `\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\bar\chi)` and `\Phi^{\mathrm{pair}}_\chi=\Xi_\chi(2s-1)/\Xi_\chi(2s)`. They also prove the front-end gain that pairing buys: self-duality of `\Xi_\chi`, cancellation of the residual root number, and a scalar `U(1)` boundary phase.
- The Dirichlet channel note ranks the paired scalar route above the rotated single channel exactly because the draft needs more than critical-line reality: it needs a real sign-compatible scalar amplitude, a one-dimensional leading value channel, corrected whitening, oddness in the realized channel, and denominator/boundary control. For non-self-dual complex characters the paired route is the conservative scalar-amplitude target from current scope alone.
- The portability verifier and local-package reports repeatedly separate the real/self-dual Dirichlet case from the genuinely complex non-self-dual case. They say the real/self-dual case is less problematic and that, in that case, the odd-scalar formulation may survive with little conceptual change. That is evidence against choosing real characters as the first subclass for a paired theorem specifically: if the source is already self-dual, the cleaner first theorem is plausibly a self-dual single-channel theorem, not a doubled paired one.

Conditional on standard facts / theorem-facing convenience.

- For a primitive nonprincipal real character, `\chi=\bar\chi`, so the paired object collapses to `\Xi_\chi(s)=\Lambda(s,\chi)^2`. That should remove the non-self-dual ambiguity automatically, but it also turns the paired theorem into duplicated bookkeeping for one self-dual source. From standard completed-`L` facts, that means repeated-zero and repeated-background accounting rather than a genuinely new scalar package.
- For primitive nonprincipal complex characters, the paired theorem is more natural because pairing is doing real work: it converts a non-self-dual source into a self-dual scalar object. This is the only subclass for which the current paired theorem is not merely a repackaging trick.
- Restricting to one parity at a time should give the cleanest first statement because the archimedean factor type is then frozen across the theorem, so the background term does not need an `a_\chi\in\{0,1\}` case split. This is a presentation advantage, not a proved reduction of the main gap.

Missing.

- No current note proves that the real-character paired theorem is strictly worse than the real-character single-channel theorem; the point here is theorem naturalness, not a proved impossibility.
- No current note proves that fixed parity materially shrinks the analytic burden beyond simplifying gamma-bookkeeping in the statement.
- No current note proves the exact paired source theorem itself even for primitive complex characters: exact normalization, unified background bookkeeping, compact-interval convergence/regularization, and exact local-slot identification are all still open.
- No current note proves that the complex-character paired theorem reduces the downstream localization burden more than the real-character self-dual route would; only the front-end candidate selection is currently supported.

Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:10-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:40-55`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:8-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:50-58`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md:11-18`
- `/mnt/c/workspace/riemann2/tasks/20260423-144416-attack-gap-paired-quotient-properties/reports/gap-paired-quotient-routeA.md:118-132`
- `/mnt/c/workspace/riemann2/tasks/20260423-184608-attack-gap-paired-background/reports/gap-paired-background-routeA.md:21-24`
- `/mnt/c/workspace/riemann2/tasks/20260423-184608-attack-gap-paired-background/reports/gap-paired-background-routeA.md:44-56`
- `/mnt/c/workspace/riemann2/tasks/20260423-052540-attack-gap-local-package-portability/reports/gap-local-package-routeB.md:26-29`
- `/mnt/c/workspace/riemann2/tasks/20260423-052540-attack-gap-local-package-portability/reports/gap-local-package-routeB.md:74-78`
- `/mnt/c/workspace/riemann2/tasks/20260423-050630-attack-gap-grh-dirichlet-tau/reports/gap-closer-finite-core-portability.md:13-15`
- `/mnt/c/workspace/riemann2/tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md:24-31`
- `/mnt/c/workspace/riemann2/tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md:50-53`

Dependencies

- The project's existing candidate-selection boundary between paired scalar, rotated single-channel, and matrix-valued Dirichlet packages.
- Standard primitive Dirichlet completed-`L` facts: functional equation, conjugation symmetry, and the distinction between real/self-dual and genuinely complex non-self-dual characters.
- Standard parity dependence of the archimedean factor, used only for the optional fixed-parity narrowing.
- The repo's current distinction between front-end object choice and the much larger exact-source/local-slot theorem burden.

Strongest objection

This recommendation optimizes for theorem naturalness, not for a proved reduction in total proof difficulty. A reasonable counter-position is that primitive nonprincipal real characters should come first because they are self-dual and therefore simpler. From a full-roadmap viewpoint that may be right. The reason I still rank primitive complex characters first for an exact paired-source theorem is narrower: in the real case the clean object is probably no longer genuinely paired, while in the complex case pairing is exactly the device that removes the front-end ambiguity the repo keeps flagging.

Needed for promotion

1. Write one theorem-facing model statement for primitive nonprincipal complex characters and one for primitive nonprincipal real characters, then compare exact front-end bookkeeping side by side.
2. Decide by proof, not by taste, whether the real-character route should be formulated as a self-dual single-channel theorem instead of a paired theorem.
3. Check whether a fixed-parity restriction actually removes any substantive source-term complications beyond gamma-case splitting.
4. Prove the exact paired source theorem in the chosen complex subclass: normalization, unified background term, regularized zero sum, and exact manuscript-slot identification.
5. Honest verdict: for an exact paired-source theorem specifically, primitive nonprincipal complex characters are the cleanest first subclass, with fixed parity as an optional cosmetic narrowing. Primitive nonprincipal real characters are cleaner only if the project is allowed to leave the paired formulation and switch to a self-dual single-channel theorem.
