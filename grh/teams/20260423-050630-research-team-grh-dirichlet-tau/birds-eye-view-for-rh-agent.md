# Bird's-Eye View For RH Agent

Date: 2026-04-23
Audience: agent focused on the main RH draft who needs the `grh/` map quickly.

## Executive map

- `RH` here means the current zeta draft in `paper/proof_of_rh.tex`.
- `ERH` here means primitive Dirichlet `L`-functions.
- `GRH` here means the broader completed-`L`-function picture.
- `tau` means the Ramanujan `\tau` `L`-function, used as a self-dual degree-2 stress test.

The current conclusion is:

- the RH draft contains a real generic local package;
- the actual zeta realization and endgame are still source-specific;
- the first serious non-zeta target is not full ERH/GRH, but an exact paired Dirichlet source-and-slot theorem;
- the best immediate value back to the RH draft is still the canonical zeta source theorem for `q` and `S`.

## Where RH sits in the bigger picture

Think of the current zeta draft as having six layers.

1. Local phase geometry.
   Phase kernel, jet normalization, whitening, removable singularity structure.
   This is the most portable part.

2. Source package.
   The zeta/scattering split `q = B_zeta + S`, with `S(m)` a positive strip-edge zero scalar.
   This is not yet written as a canonical source theorem in the main paper.

3. Value-channel interface.
   The local linearization `A_val`, the pairing with the toy anomaly, and the formal calibration interface.
   This is largely local algebra once the exact scalar slot is realized.

4. Remainder dominance.
   The calibrated chain needs `Psi(R) = o((x/B)S)`. In the current draft this reduces to `S_2 = o(x Q^2 S)` plus the variable-`x` issue.

5. Odd/transverse package.
   Corrected odd scalar, boundary theorem, Cauchy bounds, universal `N`-point odd-moment projector.

6. Endgame.
   The late contradiction and propagation package are explicitly RH-specific in the current manuscript.

RH is the only place where all six layers are even partially assembled. GRH/ERH work is currently about understanding which of these six layers are genuinely universal and which are not.

## What is genuinely portable now

Safe to treat as portable template:

- the local kernel / jet / whitening package;
- the odd-germ / odd-projector algebra once an odd holomorphic scalar with boundary control exists;
- the first-order local `A_val` algebra once the exact local slot and symmetric normal form exist;
- the one-zero strip-edge kernel upstairs, conditional on a quotient/source theorem.

Not safe to call portable yet:

- the zeta source theorem itself;
- any Dirichlet or tau analogue of the exact `S(m)` slot;
- remainder dominance;
- the corrected odd/transverse realization-and-boundary theorem;
- any endgame or contradiction theorem.

## The key structural insight from `grh/`

The scalar `S(m)` in the RH draft should be thought of as a positive strip-edge zero kernel, not as a raw critical-line-value surrogate.

The candidate zeta source object is:

`phi(s) = Lambda(2s-1) / Lambda(2s)`

with boundary phase on `s = 1/2 + it`.

At kernel level, one zero `rho = beta + i gamma` contributes

`Re((1+2it-rho)^(-1) - (2it-rho)^(-1))`

which is exactly the positive kernel used in the draft.

So the non-zeta problem is not “find a real value.” It is “find a completed-object source theorem whose background-subtracted zero contribution occupies the manuscript’s exact `S(m)` slot.”

## ERH picture

For primitive Dirichlet `L`-functions, current scope supports this map.

- Single-channel quotient is now a serious `phase-channel candidate`.
- It is not yet a proved `scalar-amplitude candidate` at the manuscript `S(m)` slot.
- The conservative exact-source target remains a paired object.

Current best paired object:

`Xi_chi(s) = Lambda(s,chi) Lambda(s,bar chi)`

`Phi_chi^pair(s) = Xi_chi(2s-1) / Xi_chi(2s)`

Why this is preferred from current scope alone:

- cleaner self-dual scalar phase;
- no residual root-number nuisance at the boundary;
- automatic upstairs strip-edge kernel positivity if the paired source theorem exists.

But even here the actual theorem burden is still:

1. upstairs paired source realization;
2. downstairs exact local-slot identification.

Only after those do you get the manuscript-style paired `S(m)` slot.

## Tau picture

Tau is not yet the best exact-`S` target.

Safe statement:

- tau is the cleanest self-dual phase-channel candidate;
- tau is a good higher-degree test object for the local package;
- tau is not yet a realized localization theorem;
- the five degree-sensitive checkpoints remain open.

Those checkpoints are:

1. source decomposition and curvature / tail package;
2. microscopic denominator comparability and holomorphy radius;
3. same-point / mixed-block scaling hierarchy;
4. preserved whitening gain and boundary estimate;
5. growth bookkeeping if one wants anything past the local theorem.

So tau is best understood as a self-dual stress test, not yet as the main first non-zeta theorem target.

## GRH picture

The honest GRH map is:

- first isolate the source-light local package;
- then prove a family-specific source theorem giving the exact scalar slot;
- then prove remainder dominance for the calibrated value-channel subchain;
- then prove the corrected odd/transverse realization-and-boundary package;
- only after that ask about contradiction-level statements.

So GRH is not one missing theorem. It is a layered realization program.

## Best current priorities

Use two criteria.

Best first non-zeta exact-source target:

- primitive Dirichlet paired source-plus-slot realization;
- most natural first subclass from current scope alone: primitive nonprincipal complex characters;
- fixed parity is only statement cleanup, not a major theorem simplifier;
- exceptional-zero avoidance is helpful but only a secondary front-end simplifier.

Best value back to the main RH draft:

- canonical zeta source theorem for `q` and `S`.

This is now best described as one localized source-theorem package with:

- quotient / phase normalization;
- single-zero contribution;
- compact-interval summation / regularization;
- plus background identification and multiplicity convention.

## Smallest honest milestones

Do not confuse `partial transport` with `exact-source milestone`.

- `corrected-whitening transport` is a real partial bundle.
- The first non-zeta exact-source milestone is still the paired source-plus-slot realization.

What that milestone would not yet include:

- remainder dominance;
- odd/transverse realization;
- boundary theorem;
- any ERH/GRH consequence.

## Safe / unsafe claims

Safe:

- the RH draft already contains a source-light local package;
- zeta is the base case where all layers are visible;
- Dirichlet paired source-plus-slot is the cleanest current non-zeta exact-source target from current scope alone;
- tau is the cleanest self-dual phase-channel candidate, not a realized localization theorem.

Unsafe:

- the current draft already extends to GRH or ERH;
- complex Dirichlet is almost done once the quotient is unimodular;
- tau differs only by constants;
- only bookkeeping remains;
- remainder dominance is the whole remaining non-zeta burden.

## Recommended handoff to an RH-focused agent

If the agent is working primarily for the main RH draft, the most valuable actions are:

1. Treat the main zeta source theorem for `q` and `S` as the top paper-facing gap.
2. Keep the local generic package and the zeta source package sharply separated.
3. Use the `grh/` notes mainly as a map of what is generic, what is source-specific, and what is still conditional.
4. If the agent wants to help the non-zeta side, target the paired Dirichlet source-and-slot theorem, not a general GRH statement.

## Best file pointers

- `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/priority.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/portability_note.tex`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_candidate.tex`
