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
