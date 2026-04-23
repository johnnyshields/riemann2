## Claim

Primitive nonprincipal complex characters are the cleaner first subclass for the paired-source theorem, conditional on standard external Dirichlet-`L` facts: the classical exceptional-zero branch is a real-character phenomenon, so restricting to primitive complex characters removes that case split from the front end. What this buys is a cleaner theorem statement and cleaner external zero-free-region bookkeeping for the paired object `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)` and its strip-edge quotient `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)`. It does not by itself close the exact paired-source theorem or the exact local-slot identification.

## Status

open

## Evidence

Proved from standard external facts:

- For primitive Dirichlet characters, the possible Landau-Siegel exceptional zero is attached only to primitive real characters. Restricting to primitive nonprincipal complex characters removes that exceptional-zero branch from the external input.
- For the paired object, this means there is no need to carry a separate `real exceptional zero near 1` contingency in the first theorem target when the subclass is primitive complex.

Conditional on external facts:

- Using the standard zero-free-region package for primitive complex characters, one may treat the front end of the paired quotient without the extra bookkeeping that real-character exceptional zeros force.
- This supports the priority note's narrower safe wording that the most natural first exact paired-source subclass is primitive nonprincipal complex characters.
- The gain is statement-level and bookkeeping-level cleanliness: cleaner hypothesis set, cleaner boundary-phase packaging, and no exceptional-zero branch in the external background term.

Missing:

- An exact paired-source theorem still needs exact compact-interval source-to-slot identification for the local `S(m)` term.
- The paired route still needs the unified paired background bookkeeping already identified in the paired-source notes; removing exceptional-zero complications does not supply that identification.
- No theorem-level reduction has been shown for denominator comparability, corrected whitening, odd/transverse realization, or boundary control.
- From current scope alone, the safe conclusion is only that primitive complex characters are cleaner than real characters for the first paired-source target, not that the remaining theorem burden is materially smaller.

## Exact refs

- Briefing: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- Priority narrowing to primitive complex subclass: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md:18-23`
- Paired-source target and scoped warnings: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:18-27`, `40-56`, `66-87`
- External input invoked: standard Dirichlet-`L`-theory zero-free-region package for primitive characters, with the exceptional-zero alternative confined to primitive real characters.

## Dependencies

- Standard external Dirichlet-`L`-function facts: analytic continuation, functional equation, and the classical zero-free-region theorem with possible exceptional zero only in the primitive real-character case.
- Internal paired-object setup from the paired-source note: `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)` and `Phi_chi^pair(s)=Xi_chi(2s-1)/Xi_chi(2s)`.

## Strongest objection

This may be only a front-end simplifier. The main open burden in the first theorem target is exact local source-to-slot identification, and the current notes already warn that pairing does not materially shrink that theorem-sized gap. So the subclass restriction may clean the statement without producing much proof-level progress.

## Needed for promotion

- A precise statement of the first theorem target that explicitly isolates where the external zero-free-region input enters.
- Verification that every place where a real-character exceptional-zero branch could appear is genuinely external bookkeeping and not entangled with the exact compact-interval source-identification argument.
- A clean proved/conditional/missing map for the primitive complex subclass showing that the only removed issue is the real exceptional-zero contingency.
- Honest verdict: primitive nonprincipal complex characters are the cleanest safe first subclass for the paired-source theorem because they avoid the classical real exceptional-zero complication, but this does not close the source theorem and may not materially reduce the main proof burden.
