# Claim

If the objective is the shortest credible path to a realized non-zeta theorem in the current GRH subtree, the best single next theorem target is **Candidate 3: the primitive Dirichlet paired-scalar source theorem**.

Ranking by shortest credible path:

1. **Primitive Dirichlet paired-scalar source theorem**.
2. **Tau quotient/source theorem**.
3. **Primitive Dirichlet single-channel source theorem**.
4. **Canonical zeta source theorem for `q` and `S`**.
5. **Family-specific remainder-dominance theorem**.
6. **Family-specific odd/transverse realization-and-boundary theorem**.

Reason for the top choice:

- The roadmap note is already explicit that the first family target should be a **source theorem with exact scalar slot**, and only after that come remainder dominance and the odd/transverse package.
- Among non-zeta families, the Dirichlet note ranks the paired `((\chi,\bar\chi))` scalar route as the **more conservative first scalar target from current scope alone**.
- Tau is cleaner at the phase front end, but the tau note still lists five fresh degree-sensitive localization checkpoints, so the path is not shorter in a closure-relevant sense.
- The zeta source theorem is probably the nearest theorem in absolute difficulty, but it is not itself a realized non-zeta theorem. If the optimization criterion is specifically `shortest path to a realized non-zeta theorem`, it is a template-improver, not the best next target.

# Status

open

# Evidence

Proved from the notes reviewed:

- The current safe roadmap is already ordered as: **(1) source theorem with exact scalar slot; (2) remainder-dominance package; (3) transverse odd-channel package**. So Candidates 5 and 6 are downstream, not the best next target (`notes/positive_s_implication.md:17-39`, `notes/remainder_dominance.md:8-38`, `notes/odd_package_transport.md:22-49`).
- The remainder-dominance note says its bottleneck status is only scoped: it becomes the next bottleneck **after exact scalar-slot identification** for the calibrated value-channel subchain, and it does not solve denominator, whitening, or odd-package issues (`notes/remainder_dominance.md:8-38`).
- The odd-package note says the odd/transverse theorem is an **independent theorem target** only **after exact scalar-slot identification and value-channel remainder dominance** (`notes/odd_package_transport.md:22-49`).
- The Dirichlet note ranks the paired route first: it is the **more conservative first scalar target** because reality and nonnegativity are built in at the scalar level, while the single completed channel is only a conditional phase-channel candidate from current scope alone (`notes/dirichlet_channel.md:14-24`, `50-59`, `81-86`).
- The tau note gives the opposite shape: tau is cleaner only as a **self-dual phase-channel candidate**, but the manuscript does not yet realize the tau decomposition, denominator theorem, whitening hierarchy, or boundary estimate, and the note isolates five fresh degree-2 checkpoints (`notes/tau_localization.md:8-17`, `23-54`, `57-60`).
- The source-theorem-gap note shows why Candidate 1 is not the right optimization target here. It is a real, specific gap, but it remains a zeta theorem: kernel theorem proved, source theorem still conditional, with explicit normalization and bookkeeping still missing (`notes/source_theorem_gap.md:6-18`, `22-40`).

Conditional on the interpretation of `shortest path`:

- If `shortest path` meant `smallest theorem gap anywhere`, independent of family, then Candidate 1 would likely rank first, because that note isolates a narrow normalization-and-bookkeeping bridge rather than a new family realization program.
- If `shortest path` means what the mission states, namely the shortest path to a **realized non-zeta theorem in grh**, then Candidate 3 is the correct top target, because it is already a family source theorem and the current notes rank it as the conservative scalar-amplitude route.
- Tau could overtake Candidate 3 only if later work collapses several of the five tau localization checkpoints into a single reusable self-dual package. Nothing in the current notes proves that collapse.

Missing:

- A primitive Dirichlet theorem that outputs the exact background-subtracted scalar in the manuscript's `S(m)` slot through the paired scalar route.
- A proof that the paired scalar package feeds the corrected local deformation with the needed normalization and sign compatibility.
- Any note proving that tau's self-dual front-end advantage removes the five localization checkpoints; current scope does not support that.
- Any support for starting with Candidates 5 or 6 before exact scalar-slot identification; the roadmap notes cut against that ordering.

Honest verdict: for a non-zeta theorem target, the clean next bet is the primitive Dirichlet paired-scalar source theorem. It is not proved to be easy, but it is the only candidate that current notes both place at the front of the dependency chain and rank as the conservative family realization route from current scope alone.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/README.md:34-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/README.md:43-60`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:14-24`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:50-59`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:61-86`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:8-21`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:23-54`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:6-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:22-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:22-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:18-35`

# Dependencies

- The dependency ordering from `positive_s_implication.md`: exact `S`-slot source theorem first, then remainder dominance, then odd/transverse realization.
- The Dirichlet channel note's ranking of paired scalar over single-channel as the conservative scalar-amplitude route.
- The tau localization note's restriction of tau's current advantage to channel choice rather than realized localization.
- The source-theorem-gap note's distinction between a narrow zeta-side bridge and a genuine non-zeta realization theorem.

# Strongest objection

The strongest objection is that Candidate 1 may still be the fastest practical move because it is the narrowest isolated theorem gap and could supply a canonical template for both Dirichlet and tau. If one optimizes for `fastest theorem that most helps later non-zeta work`, rather than `fastest realized non-zeta theorem`, then Candidate 1 could reasonably move to the top. The ranking above therefore depends on taking the mission statement literally: the target theorem itself should already be non-zeta.

# Needed for promotion

1. State the primitive Dirichlet paired-scalar source theorem with exact output: the real background-subtracted scalar must be the manuscript's `S(m)`-slot quantity, not only an upstairs quotient or phase object.
2. Prove the paired package supplies the required normalization, sign compatibility, and local value-channel realization.
3. Only after that, attack the now-scoped next bottleneck: family-specific remainder dominance.
4. After remainder dominance, isolate the separate odd/transverse realization-and-boundary theorem.
5. Honest verdict: choose Candidate 3 next. Candidate 2 is the cleaner phase candidate but not yet the shorter credible realization path; Candidates 5 and 6 are downstream; Candidate 1 is useful but misses the mission's non-zeta target.
