# Claim

The cleanest explicit paired object for a primitive complex Dirichlet character is the paired completed product
\[
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\bar\chi),
\]
used only through its strip-edge quotient
\[
\Phi^{\mathrm{pair}}_\chi(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}
=\frac{\Lambda(2s-1,\chi)\Lambda(2s-1,\bar\chi)}{\Lambda(2s,\chi)\Lambda(2s,\bar\chi)}
=\phi_\chi(s)\phi_{\bar\chi}(s).
\]

This is algebraically the same as the product of the two single quotients, but it is the better theorem-facing presentation because the pairing is fixed first and the strip-edge quotient is then taken on one canonical self-paired object.

The corresponding scalar target should be stated as a paired strip-edge logarithmic-derivative channel, for example
\[
q^{\mathrm{pair}}_\chi(t):=\frac14\Re\!\left[\partial_s\log \Phi^{\mathrm{pair}}_\chi(s)\right]_{s=\frac12+it},
\qquad
S^{\mathrm{pair}}_\chi(t):=q^{\mathrm{pair}}_\chi(t)-B^{\mathrm{pair}}_\chi(t),
\]
with the factor and background fixed only inside a future theorem.

Comparison of plausible paired objects:

1. `Best [candidate]`: `\Phi^{\mathrm{pair}}_\chi(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)`.
   It preserves the manuscript's strip-edge geometry `2s-1` versus `2s`, packages `\chi` and `\bar\chi` into one scalar object, and is the cleanest match to the positive-kernel agenda.
2. `Equivalent but less clean [confirmed]`: `\phi_\chi(s)\phi_{\bar\chi}(s)`.
   This is the same function, but it looks like two separate channels glued together after the fact, so it is weaker as theorem language.
3. `Not enough by itself [confirmed]`: the bare paired product `\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)` without quotienting.
   This fixes pairing but does not by itself produce the strip-edge pole-zero difference that underlies the kernel
   \(
   (1-\beta)/((1-\beta)^2+(2m-\gamma)^2)+\beta/(\beta^2+(2m-\gamma)^2)
   \).

So the best explicit paired completed object is: pair first at the completed-function level, then take the same strip-edge quotient as in zeta.

# Status

open

# Evidence

Proved.

- The current notes already separate the front-end channel question from the local realization theorem. They rank the primitive Dirichlet paired-scalar route as the conservative first scalar target only `from current scope alone`, while the single quotient is now only a conditional phase-channel candidate.
- The scattering note identifies the manuscript target as a strip-edge kernel coming from the quotient pattern `\Lambda(2s-1)/\Lambda(2s)`, not from a raw completed value. Any paired object that drops the `2s-1` versus `2s` quotient geometry misses the feature that produces the zeta kernel.
- The quotient-phase and universal-kernel notes say the quotient geometry is the universal upstairs part: once a family-specific quotient/source theorem exists, the single-zero strip-edge kernel and its positivity are universal upstairs. That points toward keeping the strip-edge quotient unchanged and only changing the underlying completed object.
- If one insists on pairing for primitive complex characters, the most economical way to do that is to form the self-paired completed product `\Xi_\chi=\Lambda(\cdot,\chi)\Lambda(\cdot,\bar\chi)` and then apply the same strip-edge quotient template. This avoids inventing a new object type.
- The formula `\Phi^{\mathrm{pair}}_\chi=\phi_\chi\phi_{\bar\chi}` shows that `product of single quotients` and `quotient of paired completed product` are not competing mathematical objects. They are the same object written in two ways. The real choice is presentation. The paired-product presentation is cleaner because it is canonical before differentiation and before branch choices.

Conditional on [a family-specific paired source theorem].

- The paired quotient should feed an exact-source theorem of the same shape as the zeta candidate source theorem: a decomposition `q^{\mathrm{pair}}_\chi=B^{\mathrm{pair}}_\chi+S^{\mathrm{pair}}_\chi` on compact intervals away from singularities, with `S^{\mathrm{pair}}_\chi` an explicit regularized strip-edge zero sum.
- In that scope, the paired quotient matches the strip-edge kernel / positive scalar agenda better than a bare paired product, because its logarithmic derivative has the same shifted pole-zero bookkeeping that generated the zeta kernel.
- In that same scope, the paired quotient is still better aligned with the positive scalar agenda than the single quotient from current scope alone, because pairing is built into the completed object before local-slot identification is attempted.

Missing.

- No current note proves that the exact normalization is the displayed `1/4` real logarithmic derivative rather than a nearby branch- or factor-adjusted convention.
- No current note proves the paired source decomposition with gamma, trivial-zero, pole, multiplicity, and regularization bookkeeping.
- No current note proves that the resulting `S^{\mathrm{pair}}_\chi` is exactly the coefficient of the manuscript-style leading value channel in a primitive-Dirichlet corrected local deformation.
- No current note proves that the paired quotient materially shortens the downstream denominator-comparability, whitening, boundary, or odd/transverse burdens.

Honest verdict: the clean object choice is now fairly sharp. The clean theorem choice is not `two separate quotients somehow averaged`, and not `a paired completed product without quotienting`. It is `the strip-edge quotient of the paired completed product`. What remains open is the theorem that turns that object into the exact local `S(m)`-slot scalar.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:8-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:35-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:21-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:45-48`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:50-58`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:25-43`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:10-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:25-68`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:100-138`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeA.md:3-18`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeA.md:55-71`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeB.md:13-19`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/verifier-adversarial-dirichlet-paired-source.md:3-19`
- `/mnt/c/workspace/riemann2/tasks/20260423-133143-attack-gap-quotient-phase-generalization/reports/gap-quotient-phase-routeA.md:3-48`

# Dependencies

- The current `grh/` notes are taken as the authority for the proved / conditional / missing boundary.
- The strip-edge kernel in the scattering note is taken as the correct structural target for candidate-object selection.
- The paired object is judged by one criterion only: which explicit completed object best preserves the manuscript's strip-edge zero-kernel architecture while producing a scalar front end for primitive complex characters.
- The equality `\Phi^{\mathrm{pair}}_\chi=\phi_\chi\phi_{\bar\chi}` is used algebraically, so the comparison is about canonical packaging rather than about distinct meromorphic functions.

# Strongest objection

The strongest objection is that the report may be making too much of a presentation choice. Since `\Phi^{\mathrm{pair}}_\chi` and `\phi_\chi\phi_{\bar\chi}` are the same meromorphic function, one could say there is no substantive mathematical preference between `pair first, then quotient` and `take two single quotients, then multiply`. If the eventual theorem is stated only at the logarithmic-derivative level, the distinction may collapse completely. Current notes do not prove that the paired-product presentation buys simpler background or branch bookkeeping; they only suggest that it is the cleaner canonical description.

# Needed for promotion

1. Fix one theorem-facing normalization for the paired scalar channel attached to `\Phi^{\mathrm{pair}}_\chi`.
2. Prove the paired source theorem on singularity-free compact intervals, including background, trivial-zero, pole, multiplicity, and regularization bookkeeping.
3. Prove that the background-subtracted paired scalar is exactly the coefficient of the manuscript-style leading value channel.
4. Only after exact local-slot identification, test whether the paired quotient genuinely helps the downstream denominator / whitening / boundary / odd-transverse package.
5. Keep the safe wording scoped: `best explicit paired object for the exact-source target from current scope alone`, not `canonical paired source theorem already known`.
