# Claim

Choosing a paired object is a real gain only at the front end unless it comes with an exact local realization theorem. From the current notes, the smallest burden that remains after choosing a paired object is still: an exact paired-source theorem that produces a background-subtracted paired scalar and proves that this scalar is exactly the coefficient occupying the manuscript's `S(m)` slot in the corrected local deformation. Without that exact slot identification, the paired move is mostly cosmetic repackaging: it trades `which single complex channel gives a real scalar?` for `which paired scalar is the one the local deformation actually uses?`

Real gain versus cosmetic repackaging separates as follows.

- Real gain: the paired package canonically fixes scalar reality/nonnegativity, fixes the normalization/background bookkeeping, and lands directly in the coefficient slot of `\Delta = S A_{\val} + R`.
- Cosmetic repackaging: the paired package only gives a real or positive strip-edge scalar upstairs, while the theorem still has to prove separately that this is the scalar seen by the local value channel.

Proved / conditional / missing split:

- Proved: pairing is a safer candidate-selection move than a raw single complex channel from current scope alone.
- Conditional on [an exact paired-source theorem with exact local-slot realization]: the manuscript's existing local algebra would then supply the leading-channel coefficient theorem.
- Missing: any theorem that pairing, by itself, removes the exact `S(m)`-slot identification burden rather than relocating it into paired notation.

Honest verdict: the paired-object route is a genuine candidate-selection improvement, not yet a genuine reduction of the theorem-sized gap at the exact `S(m)` slot.

# Status

open

# Evidence

Proved from the supplied notes and draft:

- `dirichlet_paired_source.md` states the safe target as an `exact paired-scalar source theorem with full bookkeeping and exact local-slot identification`, and warns not to say that pairing `materially shrinks the remaining theorem burden`. That already identifies the adversarial boundary: pairing helps, but the exact slot theorem survives intact.
- `positive_s_implication.md` fixes the dependency order. If a family theorem yields the exact background-subtracted scalar occupying the manuscript's `S(m)` slot, then the leading-channel coefficient theorem is already in place. So the essential burden after any candidate-object choice is not positivity alone but exact slot identification.
- `universal_source_kernel.md` says the one-zero strip-edge kernel can be universal only upstairs, conditional on a family-specific quotient/source theorem, while the manuscript `S(m)` slot remains family-specific. This is direct evidence that paired notation does not by itself solve the local identification problem.
- `scattering_candidate_note.tex` sharpens what the target scalar should look like: a real, nonnegative strip-edge zero contribution serving as the coefficient of the leading local value channel. But the same note also says the gain is conceptual candidate-object selection, not realization.
- In the main paper, `S(m)` is not a decorative scalar. It is defined by `S(m):=q_\zeta(m)-B_\zeta(m)` and then appears as the explicit coefficient in
  `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`.
  The corrected transverse scalar then kills the `A_{\val}` channel and leaves only the remainder. Because this slot is load-bearing, any paired reformulation still has to prove that its scalar is exactly this coefficient-type object, not merely an analogous positive quantity.
- `source_theorem_candidate_note.tex` gives the zeta-side template for the smallest honest source theorem: fix the quotient object, normalization, multiplicity, convergence/regularization, and background term so that the background-subtracted scalar is the manuscript's source split. The paired route inherits the same shape of burden unless it proves more than current notes support.

Conditional on [a paired completed-source object being canonically defined]:

- Pairing does appear to remove one front-end ambiguity present in the non-self-dual single-channel route: it makes scalar reality/nonnegativity structurally plausible without relying only on phase normalization of one complex channel.
- If the paired theorem also proves exact local-slot realization, then pairing yields a real gain over a weaker single-channel theorem that supplies only upstairs phase/kernel positivity.

Missing:

- A theorem that the paired object canonically determines the exact background subtraction and normalization needed for the local value-channel coefficient.
- A theorem that the paired scalar enters the corrected local deformation directly, rather than being a merely analogous strip-edge zero density.
- Any evidence that denominator comparability, corrected whitening, odd/transverse realization, or boundary control collapse automatically once the problem is written in paired notation.
- Any result showing that the identification problem at the `S(m)` slot disappears rather than reappears as `which paired scalar is the right one?`

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:18-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:35-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:21-25`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:45-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:10-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:94-139`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:28-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:106-125`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-288`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1560`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2218-2265`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/gap-dirichlet-paired-source-routeB.md:1-34`
- `/mnt/c/workspace/riemann2/tasks/20260423-141819-attack-gap-dirichlet-paired-source/reports/verifier-adversarial-dirichlet-paired-source.md:3-19`

# Dependencies

- The current `grh/` notes are treated as the authority for the proved / conditional / missing boundary.
- `Real gain` is interpreted narrowly: a theorem burden is genuinely reduced only if one of the load-bearing local identification tasks disappears, not merely if the candidate scalar looks cleaner upstairs.
- The manuscript's local algebra is assumed reusable only after exact identification of the scalar occupying the `S(m)` slot.

# Strongest objection

The strongest objection is that the paired package may secretly do more than this report credits. A well-chosen paired completed object might automatically carry the right background subtraction, symmetry, and normalization so that exact local-slot identification becomes almost tautological once the source formula is written down. Current notes do not prove that. From current scope alone, the safe reading is weaker: pairing cleans up the front end, but the main exact-identification burden remains.

# Needed for promotion

1. State one precise paired theorem candidate with exact object, normalization, multiplicities, and regularized zero-source formula.
2. Prove that its background-subtracted scalar is exactly the coefficient of the manuscript-style leading value channel, not just a positive analogue.
3. Show whether pairing also canonically fixes the background term and local denominator architecture; without that, the move remains only partially structural.
4. Keep the claim scoped as `pairing improves candidate selection` unless step 2 is proved.
5. Use `material reduction of theorem burden` only if a paired theorem eliminates, rather than renames, the exact `S(m)`-slot identification problem.
