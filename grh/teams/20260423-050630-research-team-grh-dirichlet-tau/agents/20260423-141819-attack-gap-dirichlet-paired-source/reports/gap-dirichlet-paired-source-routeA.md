# Claim

The cleanest primitive-Dirichlet paired realization target is an exact-source theorem for a canonically symmetrized \\((\\chi,\\bar\\chi)\\) strip-edge scalar, normalized so that its background-subtracted part is the exact coefficient of the paper's leading local value channel.

The object I would target is the paired completed strip-edge source scalar
\[
q^{\mathrm{pair}}_\chi(t)
:=
\frac14\Re\!\left[
\partial_s \log \frac{\Lambda(2s-1,\chi)}{\Lambda(2s,\chi)}
+
\partial_s \log \frac{\Lambda(2s-1,\bar\chi)}{\Lambda(2s,\bar\chi)}
\right]_{s=\frac12+it},
\]
equivalently the real contragredient-symmetrized strip-edge logarithmic-derivative channel attached to the primitive completed pair. Let
\[
S^{\mathrm{pair}}_\chi(m):=q^{\mathrm{pair}}_\chi(m)-B^{\mathrm{pair}}_\chi(m).
\]

The theorem one would want is:

For each primitive Dirichlet character \\(\chi\\) and each compact interval \\(I\subset\mathbb R\\) avoiding the archimedean, trivial-zero, and pole singularities of the paired package, the paired scalar admits a source decomposition
\[
q^{\mathrm{pair}}_\chi(t)=B^{\mathrm{pair}}_\chi(t)+S^{\mathrm{pair}}_\chi(t),
\]
where \\(S^{\mathrm{pair}}_\chi(t)\\) is an explicit nonnegative strip-edge zero sum over the paired zero multiset of \\(\Lambda(s,\chi)\\) and \\(\Lambda(s,\bar\chi)\\), with multiplicity and exact normalization fixed inside the theorem. Moreover the paired corrected local deformation satisfies
\[
\Delta^{\mathrm{pair}}_\chi(m,\sigma)
=
S^{\mathrm{pair}}_\chi(m)A_{\val}(m,\sigma)+R^{\mathrm{pair}}_\chi(m,\sigma),
\]
so \\(S^{\mathrm{pair}}_\chi(m)\\) is not merely an upstairs positive source scalar but the manuscript's exact `S(m)`-slot scalar in the paired channel.

What the paired route is supposed to fix relative to the single-channel route is narrower than `positivity somewhere upstairs`. It is supposed to fix the non-self-dual front-end ambiguity before localization: the single completed quotient is currently only a conditional phase-channel candidate, while the paired source is designed to force a scalar that is canonically real, contragredient-symmetric, and sign-compatible at the point where the paper needs the coefficient of \\(A_{\val}\\). From current scope alone, that is the cleanest non-zeta realization target.

Honest verdict: this is the right theorem candidate to state, not a theorem that current notes prove.

# Status

open

# Evidence

Proved from the current notes and paper.

- The paper's leading scalar interface is precise: the useful source scalar is not an arbitrary real critical-line quantity, but the exact coefficient in
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
  \]
  and once that exact scalar slot is identified, the existing local algebra already supplies the leading value-channel coefficient theorem.
- The paper also shows why the scalar slot is stricter than phase reality alone: `A_val` is annihilated by `\Phi_K`, while the corrected odd scalar and boundary estimate live downstream of the exact value-channel decomposition.
- The Dirichlet channel note ranks the paired \\((\\chi,\\bar\\chi)\\) route as the more conservative first scalar target from current scope alone because reality and nonnegativity are built in more naturally at scalar level there than in the rotated single channel.
- The quotient-phase and universal-source-kernel notes narrow the role of the single completed quotient: conditional phase candidate and conditional upstairs one-zero kernel positivity, but not yet exact realization of the manuscript scalar slot.

Conditional on the candidate theorem above.

- If a primitive-Dirichlet paired source theorem identifies the exact scalar occupying the manuscript `S(m)` slot, then the positive-`S` note says no new leading-coefficient theorem is needed. The existing local algebra already turns that exact scalar into the coefficient of `A_val`.
- In that scope the paired theorem would solve the front-end scalar-selection problem more cleanly than the current single-channel route, because the paired package is built to output a real sign-compatible scalar before one asks for corrected whitening, remainder dominance, and the odd/transverse package.

Missing.

- No current note proves that the displayed paired object is the right exact normalization rather than a nearby variant.
- No current note proves the full paired source bookkeeping: branch/sign conventions, factor-of-`2` normalization, gamma contribution, trivial-zero terms, pole terms, Hadamard regularization, or multiplicity conventions.
- No current note proves that the paired corrected local deformation exists with
  \[
  \Delta^{\mathrm{pair}}_\chi=S^{\mathrm{pair}}_\chi A_{\val}+R^{\mathrm{pair}}_\chi
  \]
  in the Dirichlet channel.
- No current note proves the downstream paired denominator comparability, corrected whitening hierarchy, microscopic boundary estimate, remainder dominance, or odd/transverse realization.

The paired route is therefore a target theorem shape, not a closed theorem chain.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:8-19`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:21-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:50-59`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:61-86`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:25-43`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/universal_source_kernel.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-16`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:10-15`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:26-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:25-68`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:100-135`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:285-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:426-779`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1566`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364`
- `/mnt/c/workspace/riemann2/tasks/20260423-053136-attack-gap-dirichlet-channel/reports/gap-dirichlet-channel-routeB.md:21-35`
- `/mnt/c/workspace/riemann2/tasks/20260423-140208-attack-gap-dirichlet-single-channel/reports/gap-dirichlet-single-routeA.md:5-35`
- `/mnt/c/workspace/riemann2/tasks/20260423-141258-attack-gap-priority-target/reports/gap-priority-target-routeA.md:16-19`
- `/mnt/c/workspace/riemann2/tasks/20260423-141258-attack-gap-priority-target/reports/gap-priority-target-routeA.md:42-45`

# Dependencies

- A decision that the paired primitive object should be the symmetrized strip-edge logarithmic-derivative channel, or an explicit nearby normalization with the same exact `S`-slot output.
- A paired source theorem fixing the branch/sign/factor-of-`2` normalization and the full background term `B^{\mathrm{pair}}_\chi`.
- An explicit statement of the paired zero sum, with multiplicity and convergence/regularization conventions.
- A proof that the paired corrected local deformation exists and has the exact leading-channel form `\Delta^{\mathrm{pair}}_\chi=S^{\mathrm{pair}}_\chi A_{\val}+R^{\mathrm{pair}}_\chi`.
- Separate paired analogues of denominator comparability, corrected whitening, microscopic boundary control, and any conductor-uniform shell/counting input.
- After exact slot identification, the later paired remainder-dominance and odd/transverse theorems.

# Strongest objection

The strongest objection is that my proposed paired object may still be one normalization step away from the truly canonical one. The notes justify the need for an exact real sign-compatible scalar in the manuscript slot, but they do not yet prove that the right paired primitive object is exactly the symmetrized strip-edge logarithmic derivative written above rather than a rotated single-channel source, a different paired quotient, or a minimal matrix package. So the theorem shape is clearer than the formula.

# Needed for promotion

1. Fix the paired completed object and its normalization as a theorem, not as a heuristic formula.
2. Prove the paired source decomposition with explicit background, trivial-zero, pole, and multiplicity bookkeeping.
3. Prove that the resulting background-subtracted scalar is exactly the coefficient of the paired corrected local deformation's value channel.
4. Only after that, attack the paired remainder-dominance step and then the paired odd/transverse realization-and-boundary package.
5. Keep the current wording scoped: `best non-zeta realization target` yes; `proved paired source theorem` no.
