# Dispatch

Date: 2026-04-24
Team slug: `research-team-fundamental-C-D`
Prior team: `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/`

## Deep prior-cycle read

The prior hidden-extraction cycle did not close `UV-002`, but it made the active theorem stack sharp. The zeta-side extractor is already complete; the obstacle is package-side. The fundamental queue is now:

1. **C**: corrected reduced-package diagonal-collapse / collision-functoriality
   \[
   \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
   \]
2. **D**: hidden-state / package-to-transform factorization, i.e. first nonzero `\Xi_{\zeta,\le H}^{(N)}` is constant on corrected package fibers modulo `\ker\Phi_K`.
3. finite-core contradiction using the already-built extractor.

The prior terminal reports sharpened this further:

- `agents/20260424-145000-Bmkappa-killer/report.md`: the least theorem-ready corrected two-atom package object for C is
  `\mathfrak P^{\corr}_2=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`, with reduction
  `\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)`.
- `agents/20260424-143000-C-proof-obligations/report.md`: C decomposes into exceptional-divisor trace, `\kappa`-independence, and identification with `\widehat\Psi`; the real blocker is `\kappa`-independence / diagonal merger.
- `agents/20260424-145000-corrected-package-object/report.md`: the killer for the free trace `B(m,\kappa)` is canonical diagonal collision-functoriality, not more blow-up regularity.
- `agents/20260424-145000-kerphik-hidden-state/report.md`: D should be transform-level; equal package fibers must force corrected-block differences into `\ker\Phi_K=\mathbf C I\oplus\mathbf C D\oplus\mathbf C K` through the first surviving odd order.

## Active queue

Primary queue remains `UV-002`-first, but this cycle is a fundamental attack on C and D, not a local-lane audit.

1. Attack C directly: prove or reduce the corrected reduced-package diagonal-collapse theorem.
2. Attack D directly: prove or reduce the hidden-state / `\ker\Phi_K` package-to-transform theorem.
3. Use 2-point and 4-point mixed material only when it informs C or D.

## Roster

### Gap closers

1. `gap-closer-C-diagonal-merger`: attack Bottleneck C, especially diagonal collision-functoriality / `\kappa`-independence for `\mathfrak P^{\corr}_2`.
2. `gap-closer-D-kerphik`: attack Bottleneck D, especially the `\ker\Phi_K` hidden-state theorem through the first surviving odd order.
3. `gap-closer-UV002-contradiction`: try to compose C + D into the finite-core contradiction; if C or D remains open, reduce to the smallest missing sub-statements.

### Explorers

4. `explorer-package-functoriality`: search for structural routes to collision functoriality / diagonal merger from package definitions and source provenance.
5. `explorer-hidden-state-geometry`: search for the invariant geometry behind the `\Phi_K`-visible hidden scalar and whether it is canonical or removable.
6. `explorer-support-lanes`: inspect 2-point and 4-point mixed only as support for C/D; report any theorem that genuinely informs the fundamental attack.
7. `explorer-prior-treasure-hunt`: summarize and mine `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/` and its `agents/` reports for overlooked C/D lemmas, negative results, exact proof obligations, and reusable theorem statements.

### Verifiers

8. `verifier-adversarial-C-D`: after the seven research reports land, attack any proposed C/D closure or reduction.
9. `verifier-source-C-D`: after the seven research reports land, source-audit definitions, line refs, and dependencies for C/D claims.

## Non-goals

- Do not drift into pair-like quantitative cleanup (`UV-009 -> UV-001 -> UV-008`).
- Do not search for a second primitive explicit pointwise highest-new field.
- Do not treat exact fixed-shear, 2-point, or 4-point mixed as independent queue heads.
- Do not reopen pure planar, endpoint-gap, or three-run overlap work unless it directly supports C or D.
- Do not promote computational or heuristic statements to proof status.

## Briefing discipline

Every agent gets the full `findings.md`, the relevant individual UV entry only if it is attacking or verifying that UV, the report schema, this non-goal list, its own deposit directory, and the writing discipline from `CLAUDE.md` §4.

## Long-running agent policy

Keep these TeamCreate agents alive and re-use the same named agents for follow-up prompts while their context is fresh. Do not shut them down after first reports unless the cycle is terminal or the coordinator explicitly ends the team. Verifiers should wait for research deposits, then remain available for second-pass attacks on revised claims.

Every report must use exactly these fields:

- Claim
- Status (`proved | computational | heuristic | open | rejected`)
- Evidence
- Exact refs
- Dependencies
- Strongest objection
- Needed for promotion

End with `Honest verdict:`.

`unsupported`, `blocked`, and `no progress` are acceptable returns. If full closure is too hard, reduce to the smallest list of concrete unresolved sub-statements.

## Continuation wave — 2026-04-24

User instruction: reuse this existing team dir and create only new agent subdirectories under `agents/`. Do not forward-carry into a new team dir for this continuation.

### Frontier after first wave

- **C fiber selection.** Patch transitions for the local affine septic-lift coordinate are base-controlled: on overlap, `S_u=-(x/Y)S` and `\tau=\Delta_7/(u_5v_5)` is determined by `\widehat\Psi`. Patching is not the hidden obstruction. The live target is fiber selection: show the actual corrected two-atom exceptional-divisor package has only this affine fiber over the reduced base and diagonal merger kills it.
- **D affine-bundle transport.** On `\{c\neq0,v_5\neq0\}`, equal reduced-package fibers leave exactly one `\Phi_K`-visible local septic scalar, `T=v_7/c`, but the source audit forbids promoting `T` to a global theorem object. The live target is transform-level state-locality / affine-bundle descent through the first surviving odd order modulo `\ker\Phi_K`.
- **E finite-core transfer.** After C and D, `UV-002` still needs a real first-nonzero-odd-jet finite-core lower-model theorem. The current sharp split is `E_1` descent from genuine corrected finite-core data to the defect-free affine-incidence lanes, then `E_2` weighted-average or direct-`\Xi` lower control.
- **Verifier posture.** C dies if `B(m,\kappa)` survives; D dies if hidden `\Phi_K`-visible state survives beyond a patchwise septic proxy; E dies if it only restates the queue without replacing the pair-like lower model.

### Continuation roster

Gap closers:

1. `gap-closer-C-fiber-selection`: attack the final C local-model issue: construct or refute the theorem that the actual corrected two-atom exceptional-divisor package has only the one-dimensional affine septic-lift fiber over `\widehat\Psi`, and that diagonal merger selects the fiber point.
2. `gap-closer-D-odd-block-state`: identify the exact D-min-visible corrected odd-block functional that should replace cubic/quintic defect channels in the fixed-shear state-locality proposition; test whether corrected whitening analyticity puts it in a finite descended transport-state framework.
3. `gap-closer-E-finite-core-transfer`: attack `E_1` first, the descent from corrected finite-core package data to the defect-free affine-incidence lanes; if blocked, reduce to the weakest low-order interaction-vanishing theorem needed.

Explorers:

4. `explorer-corrected-package-object`: mine paper and prior reports for the most explicit definition of `\mathfrak P^{\corr}_2=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`, its codomain, and exactly what is missing for swap symmetry, one-amplitude collapse, and diagonal merger.
5. `explorer-affine-bundle-holonomy`: study the affine lift line as a bundle over the reduced base, including local sections, overlaps, exceptional loci `u_5=0` / `v_5=0`, and whether any corrected two-atom holonomy term can survive while remaining compatible with the fixed-shear descent.
6. `explorer-incidence-lower-model`: mine the finite-core incidence geometry and positive-kernel sections for a direct route from `\widehat\Psi`-side incidence constraints to weighted-average/direct-`\Xi` lower control, including no-cancellation or tail-domination alternatives.

Verifiers:

7. `verifier-adversarial-CDE`: wait for the six research deposits, then attack C fiber-selection, D odd-block state-locality, and E lower-transfer claims against the pinned objections above.
8. `verifier-source-CDE`: wait for the six research deposits, then source-audit line refs, definitions, basis conventions, patch hypotheses, and whether claims are paper-proved, conditional, or missing.

### Exact current label lines

- `rem:wip-pairlike-finitecore`: `rh/proof_of_rh.tex:5605`.
- `rem:wip-highest-new-scalar-direct-slice`: `rh/proof_of_rh.tex:10847`.
- `rem:wip-parity-projective-factorization-collision-blow-up`: `rh/proof_of_rh.tex:12448`.
- `rem:minimal-core-reformulation`: `rh/proof_of_rh.tex:12587`.
- `rem:wip-explicit-pointwise-bridge-good-patch-detector`: `rh/proof_of_rh.tex:21278`.
- `rem:wip-final-endgame-status`: `rh/proof_of_rh.tex:26370`.
