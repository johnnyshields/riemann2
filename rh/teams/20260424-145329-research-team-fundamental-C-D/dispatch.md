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

Every agent gets the full `findings.md`, the relevant individual UV entry only if it is attacking or verifying that UV, the report schema, this non-goal list, its own deposit directory, and the writing discipline from `AGENTS.md`.

## Long-running agent policy

Keep these Codex subagents alive and re-use the same named agents for follow-up prompts while their context is fresh. Do not shut them down after first reports unless the cycle is terminal or the coordinator explicitly ends the team. Verifiers should check stable prior deposits while independent research lanes keep moving.

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

## Resume dispatch 20260424-165509

Resume path: `rh/teams/20260424-145329-research-team-fundamental-C-D`.
Do not create a sibling team dir. New deposits go only under
`agents/20260424-165509-*/`.

### Baseline / frontier

- **Primary C target:** C-FS2/C-FS3. The current paper and verified deposits do
  not construct the actual two-atom fixed triple
  `\mathfrak P_2^{\corr}=(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr})`
  as an analytic germ. They leave the C-visible determinant slot
  `\det(R,A_5^{\mathfrak f})` and centered `D_2=2\kappa(AV_1-BU_1)` channel
  uncontrolled.
- **Secondary D target:** transform-level state-locality modulo `\ker\Phi_K`
  for the first `\Phi_K`-visible corrected odd block. Do not substitute raw
  affine-lift patching for this theorem.
- **Tertiary E target:** projected low-order defect vanishing or inhomogeneous
  rank plus sign/no-cancellation lower control.

### In-scope files and lines

- Team files: `findings.md`, `uv.md`, `attempts.tsv`, `attempts.md`,
  `collation.md`, and this `dispatch.md`.
- C reports: `agents/20260424-160000-gap-closer-C-fiber-selection/report.md`,
  `report-cfs23-followup.md`, `report-cfs2-actual-formulas.md`, notes, and
  scripts in that same agent dir.
- C verifications:
  `agents/20260424-160000-verifier-adversarial-CDE/report-cfs3-countermodel-review.md`,
  `report-cfs2-actual-formula-review.md`,
  `agents/20260424-160000-verifier-source-CDE/report-cfs23-countermodel-source-check.md`,
  and `report-cfs2-actual-formulas-source-check.md`.
- Paper source lines: `rh/proof_of_rh.tex:7004-7191`, `7540-7924`,
  `11587-11775`, `12192-12255`, `12385-12511`, `12448`, `21278`,
  `23294-23409`, and `26370`.

### Protected surfaces

Agents must not edit `rh/proof_of_rh.tex`, `findings.md`, `uv.md`,
`attempts.tsv`, `attempts.md`, `collation.md`, `dispatch.md`, `AGENTS.md`,
`lore/`, `.agents/`, or another agent's directory. Each new agent owns only its
assigned `agents/20260424-165509-<slug>/` directory.

### Targeted UV entries

- `UV-002` / `rem:wip-pairlike-finitecore`: package-side bridge to first
  nonzero odd jet remains the queue head.
- `UV-003` / `rem:wip-parity-projective-factorization-collision-blow-up`: C
  package construction and diagonal-merger support theorem.
- `UV-004` / `rem:wip-explicit-pointwise-bridge-good-patch-detector`: source
  support for any detector or quotient-defect control claim.

### Ground-truth checks and pinned objections

- A positive C-FS2/C-FS3 route must construct or source-identify the actual
  corrected two-atom fixed triple and control `R` on the exceptional divisor.
- Any proof must survive the deformation test
  `R -> R+R_\kappa` with
  `\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa`.
- Do not cite fixed codomain, scalar normalization, blow-up analyticity,
  swap-evenness, one-pair gauge invariance, or displayed order-3/5/7 formulas
  alone as killing `\partial_\kappa B`.
- Separate proved / conditional / missing. `unsupported`, `blocked`, and
  `no progress` are acceptable if the return sharpens the missing statement.

### Resume roster

1. `gap-closer-C-R-determinant-control`: attack the smallest positive C target:
   compute/control the quotient-defect representative `R`, or prove that
   `\det(R,A_5^{\mathfrak f})` descends to the collision state and has no
   exceptional slope/provenance dependence.
2. `explorer-C-actual-package-construction`: mine the source and prior reports
   for the most economical construction of the actual corrected two-atom fixed
   triple and its fiber definition; return a theorem-ready statement or a proof
   that the draft only has a schema.
3. `verifier-adversarial-C-R-channel`: adversarially pressure-test any C route
   against the `R_\kappa` determinant deformation, the formal countermodel, and
   the centered `D_2` channel.
4. `verifier-source-C-R-channel`: source-audit the same target with line refs,
   basis conventions, and proved/conditional/missing separation.

### Non-goals

Do not open pair-like quantitative cleanup (`UV-009 -> UV-001 -> UV-008`), pure
planar refinements, endpoint-gap work, three-run overlap work, or a D/E proof
attempt unless it directly resolves the C determinant-slot target.

## Resume dispatch 20260424-173642

Team name: `research-resume-research-team-fundamental-C-D-20260424-173642`.
Resume path: `rh/teams/20260424-145329-research-team-fundamental-C-D`.
Current commit at dispatch: `cb27adcccd4be054172832d04b6c5ad1a9047ea9`.
New deposits go only under `agents/20260424-173642-*/`.

### Baseline / frontier

- **Immediate target:** UV-010, definition-only. Construct the actual corrected
  order-7 quotient-defect edge package `\mathcal H_7^q` for
  `\overline E_{12}^{(7;1)}` with quotient-line trivialization to the midpoint
  quotient, without assuming diagonal merger.
- **Ordering:** edge package first; state-locality/descent second; diagonal
  merger normalization third. Do not merge these targets.
- **Pinned obstruction:** lower cubic/quintic edge laws plus abstract source
  axioms allow a formal `a_1a_2\delta^2P(m,\kappa)` septic quotient term.
  Any positive UV-010 proof must identify the actual formula or theorem that
  defines or forbids this freedom.

### In-scope files and lines

- Team files: `findings.md`, `uv.md`, `attempts.md`, `attempts.tsv`,
  `collation.md`, and this `dispatch.md`.
- Recent deposits:
  `agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md`,
  `agents/20260424-165509-gap-closer-C-R-determinant-control/report-edge-law-followup.md`,
  `agents/20260424-165509-verifier-adversarial-C-R-channel/report-UV010-adversarial.md`,
  and `agents/20260424-165509-verifier-source-C-R-channel/report-UV010-source.md`.
- Paper source ranges:
  `rh/proof_of_rh.tex:11587-11775`, `11888-12189`, `12385-12584`,
  `24520-24610`, and `24990-25030`.
- Current labels:
  `rem:wip-parity-projective-factorization-collision-blow-up` at
  `rh/proof_of_rh.tex:12448`.

### Protected surfaces

Agents must not edit `rh/proof_of_rh.tex`, `findings.md`, `uv.md`,
`attempts.tsv`, `attempts.md`, `collation.md`, `dispatch.md`, `AGENTS.md`,
`lore/`, `.agents/`, or another agent's directory. Each agent owns only its
assigned `agents/20260424-173642-<slug>/` directory.

### Ground-truth checks

- A UV-010 positive result must define the actual order-7 quotient defect as an
  analytic section in a fixed quotient bundle and prove the edge law
  `\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q(m,\kappa,\delta^2)`.
- It must state the quotient target, moving-line-to-midpoint trivialization,
  amplitude convention for `-a_1^{-1}`, and patch hypotheses, especially
  `A_5^{\mathfrak f}(m)\neq0` or an explicit replacement convention.
- It must not prove UV-010 by assuming diagonal merger, state-locality, descent,
  or `\kappa`-independence.
- If full closure is too hard, reduce to the smallest concrete missing
  substatement. `unsupported`, `blocked`, and `no progress` are acceptable.

### Roster

Gap closers:

1. `gap-closer-UV010-theorem-formulation`: formulate the paper-ready UV-010
   theorem and test what current mechanisms prove.
2. `gap-closer-UV010-quotient-trivialization`: attack the analytic
   moving-quotient-to-midpoint trivialization and patch hypotheses.
3. `gap-closer-UV010-septic-hessian`: source-mine or compute the actual
   order-7 quotient interaction Hessian `\mathcal J_2^{(7)}` / `\mathfrak O_7`.

Explorers:

4. `explorer-UV010-source-language`: mine exact paper language and notation for
   a clean definition block and for hidden existing equivalents.
5. `explorer-UV010-quotient-geometry`: study quotient-bundle geometry,
   constant-rank patches, exceptional `A_5^{\mathfrak f}=0`, and determinant
   trivializations.
6. `explorer-UV010-prior-miner`: mine prior reports/chats and later summaries
   for any parked order-7 edge package, quotient transport, or `H_7` analogue.

Verifiers:

7. `verifier-adversarial-UV010`: wait for the six research deposits, then
   pressure-test against `a_1a_2\delta^2P(m,\kappa)` and hidden merger/descent.
8. `verifier-source-UV010`: wait for the six research deposits, then source
   audit definitions, line refs, quotient target, patch hypotheses, and proof
   status.

### Non-goals

Do not attack D, E, pair-like quantitative cleanup, finite-core lower transfer,
or paper promotion in this wave. This wave is UV-010 only.

## Verifier pass 20260424-182546

Base commit: `518b43bc6c71026abcc9bf08b1c6f8de2a0ad3b9`.

The first six UV-010 deposits are captured in `attempts.md`, `attempts.tsv`,
`findings.md`, and `collation.md`. Because the runtime allows only six live
Codex subagent threads, the coordinator may close completed first-wave agents
after their committed deposits solely to free capacity for the two verifier
roles.

Verifier scope:

- `verifier-adversarial-UV010-first-wave`: attack the first-wave UV-010
  formulation, determinant trivialization, good-patch hypotheses, and hidden
  scalarization assumptions. Ground-truth pressure test is the formal
  `a_1a_2\delta^2P(m,\kappa)` septic quotient perturbation plus the `A_5=0`
  rank-jump objection.
- `verifier-source-UV010-first-wave`: source-audit the same claims against
  `rh/proof_of_rh.tex:7004-7062`, `7065-7191`, `7892-8033`, `11603-11775`,
  `11888-12189`, `12385-12510`, `24520-24610`, and `24990-25030`.

Both verifiers own only their assigned `agents/20260424-182546-<slug>/`
directory. They must not edit team ledgers, `rh/proof_of_rh.tex`, `lore/`,
`.agents/`, or another agent directory.

## UV-022 cross-effect continuation 20260424-184643

Base commit: `573a1690e1508cde25bbcbfbb5d70b51ed145e98`.

Current target:

- **UV-022** -- `rem:wip-parity-projective-factorization-collision-blow-up`.
  Define an invariant source-weight-linear input for corrected blocks through
  order 7 and an analytic corrected-whitening cross-effect package with exact
  one-amplitude collapse; then prove its order-7 quotient component is
  collision-vanishing in the UV-010 chart.

Current frontier:

- The good-patch determinant chart for UV-010 is verified.
- Direct promotion of one-pair `K_1` / `\Delta_7` / centered `D_2` to the
  actual two-atom quotient Hessian is rejected.
- The whitening-side tangent `\mathcal T_1` exists, but the two-atom interaction
  lives in the analytic cross-effect
  `\mathcal T(a_1X_1+a_2X_2)-\mathcal T(a_1X_1)-\mathcal T(a_2X_2)`.
- The cross-effect has exact one-amplitude collapse and an `a_1a_2` channel,
  but its diagonal quotient component need not vanish. That is the immediate
  obstruction.

Roster:

1. `gap-closer-UV022-diagonal-counterterm`: source-mine or construct a
   same-reduced-image germ, collision-functoriality lemma, polarization
   identity, or source-honest diagonal counterterm that kills the order-7
   quotient diagonal cross-effect without assuming downstream merger
   normalization.
2. `verifier-adversarial-UV022-cross-effect`: pressure-test any such
   counterterm or vanishing claim against the free `a_1a_2\delta^2P(m,\kappa)`
   model, the `A_5^{\mathfrak f}=0` rank jump, scalar-only routes, and hidden
   use of diagonal merger.

In-scope sources:

- `rh/proof_of_rh.tex:2415-2553` corrected-whitening transfer.
- `rh/proof_of_rh.tex:11888-12189` source criterion and diagonal merger input.
- `rh/proof_of_rh.tex:12192-12255` failure of naive source-summed routes.
- `rh/proof_of_rh.tex:12385-12510` collision-cancellation chart.
- Agent reports under `agents/20260424-183418-*`, `20260424-183713-*`,
  `20260424-184004-*`, and `20260424-184202-*`.

Protected surfaces are unchanged: agents write only to their own
`agents/20260424-184643-<slug>/` directory and must not edit team ledgers,
`rh/proof_of_rh.tex`, `lore/`, `.agents/`, or sibling agent dirs.

## UV-023 transfer-filtration attack 20260424-190438

Base commit: `52ba67f35e9929c9266bcc123ee066e8ee84420b`.

Target:

- **UV-023** -- prove that the order-7 quotient component of the
  corrected-whitening cross-effect has zero first collision derivative after
  source-weight linearization, either because only the quadratic homogeneous
  transfer `\mathcal T_2` contributes or because all `\mathcal T_{p\ge3}`
  terms are quotient-invisible through order 7.

Current frontier:

- UV-022 cross-effect package shape is still the best package layer.
- Diagonal self-subtraction alone is rejected: generic cubic and higher
  transfer terms pass one-amplitude/swap/diagonal-value tests but leave
  order-`\delta` terms.
- The next target is a source theorem about the homogeneous-transfer filtration,
  not another formal counterterm.

Roster:

1. `gap-closer-UV023-transfer-filtration`: source-mine and attempt a positive
   theorem that the septic quotient channel sees only `\mathcal T_2` or that
   `\mathcal T_{p\ge3}` is quotient-invisible through order 7.
2. `verifier-source-UV023-filtration`: source-audit the positive claim space;
   decide whether the paper already proves, conditionally proves, or misses the
   required homogeneous-transfer filtration / first-collision derivative lemma.

Ground-truth checks:

- A positive result must cite source lines for the homogeneous expansion,
  order bookkeeping, quotient extraction, and the reason higher homogeneous
  transfer pieces cannot contribute to the order-7 quotient first collision
  derivative.
- It must not assume diagonal merger, same-reduced-image collapse, determinant
  scalarization, or downstream package coincidence.
- If the source does not contain the theorem, reduce to the smallest missing
  substatement and state the exact candidate lemma.

Protected surfaces are unchanged: agents write only to their own
`agents/20260424-190438-<slug>/` directory and must not edit ledgers, paper,
`lore/`, `.agents/`, or sibling agent dirs.

## UV-023 bidegree / grading attack 20260424-190928

Base commit: `c23af1b0f502e588c6797858e2f4ff78c3bf71fc`.

Current target: UV-023 remains open. Source and gap audit agree that the paper
does not prove septic homogeneous-transfer filtration from the analytic
expansion alone. The next positive routes are:

- define a source-weight bidegree `(1,1)` projection for the actual corrected
  two-atom input `X^{[1]}` and prove the order-7 quotient extraction is
  invariant under it; or
- use `\mathfrak D_Q` scaling / finite-order grading to prove
  `\mathcal T_{p\ge3}` cannot reach the septic quotient first-collision channel.

Roster:

1. `gap-closer-UV023-bidegree-projection`: attempt the bidegree `(1,1)`
   projection route. Find a source-defined projection or prove the smallest
   missing source statement needed to make it theorem-ready.
2. `explorer-UV023-DQ-scaling`: mine `\mathfrak D_Q`, finite-order grading,
   and coefficient-order bookkeeping for a positive exclusion of
   `\mathcal T_{p\ge3}` in the septic quotient component.

Ground-truth checks:

- A positive result must define the object before quotient extraction and cite
  the lines proving invariance/visibility.
- A negative result must name the exact missing source statement: bidegree
  projection, grading bound, quotient invisibility, or source-weight-linear
  actual input.
- Do not assume diagonal merger, same-reduced-image collapse, determinant
  scalarization, or package coincidence.

Protected surfaces are unchanged: agents write only to
`agents/20260424-190928-<slug>/`.

## UV-023 source-bidegree compatibility attack 20260424-191517

Base commit: `2cea6fc9f872b62605a9d3df35cea0eb9d6f9017`.

Current target: prove or sharply reduce the source-bidegree
quotient-compatibility lemma:

`Q_7^q(C)=Q_7^q(\Pi_{1,1}C)`

for the corrected-whitening cross-effect `C` built from the actual
source-weight-linear corrected-block input `X^{[1]}`.

Roster:

1. `gap-closer-UV023-source-tags`: construct the source-tagged input
   `X^{[1]}` and projector `\Pi_{1,1}` as source objects, or identify the exact
   missing definition that blocks them.
2. `verifier-adversarial-UV023-projection`: attack any proposed
   source-bidegree projection against cubic homogeneous transfer witnesses,
   quotient extraction nonlinearity, determinant scalarization, and hidden use
   of package coincidence.

Ground-truth checks:

- The projector must be defined before quotient extraction, not after a scalar
  determinant chart.
- The proof must show compatibility with the fixed-target order-7 quotient
  extraction `Q_7^q`.
- Any negative return must name the smallest missing object among
  `X^{[1]}`, `\Pi_{1,1}`, `Q_7^q`, and the compatibility lemma.

Protected surfaces are unchanged: agents write only to
`agents/20260424-191517-<slug>/`.

## UV-023 definition-first compatibility attack 20260424-192320

Base commit: `671a94e`.

Current target: build the missing source-bidegree quotient-compatibility
package instead of trying to infer it from downstream scalar data:

`Q_7^q((1-\Pi_{1,1})C)=0`.

The previous pass kept the formal `(1,1)` projection mechanism but rejected
post-quotient projection, determinant scalarization, finite-order grading
alone, diagonal merger, and downstream package coincidence as justifications.

Roster:

1. `gap-closer-UV023-Q7q-extractor`: define or sharply reduce the fixed-target
   quotient-valued coefficient extractor `Q_7^q` before determinant
   scalarization. Read `rh/proof_of_rh.tex` lines 2415--2587, 2659--2787,
   7742--8033, 10790--10810, 11888--12255, 12385--12584, 21293--21330, and
   23072--23109; also read the UV-010 first-wave reports and the UV-023
   reports from `20260424-190438-*`, `20260424-190928-*`, and
   `20260424-191517-*`.
2. `explorer-UV023-Lh-source-input`: define or reject the source-linear
   corrected-block input `L_h` / `X^{[1]}` before whitening. Decide whether it
   can be obtained as a pair-kernel-linear derivative of the actual corrected
   two-atom block, and list the exact source lines or missing theorem needed.

Ground-truth checks:

- `Q_7^q` must be quotient-valued and fixed-target before determinant
  scalarization.
- `L_h` / `X^{[1]}` must be a source object before the corrected-whitening
  transfer, not a post-hoc amplitude multiplier of an even source sum.
- A positive route must explicitly test cubic finite-order witnesses of type
  `(1,1,5)` and quotient-extraction nonlinearity.
- A negative route must reduce to the smallest missing definition or theorem:
  `L_h`, `X^{[1]}`, `\Pi_{1,1}`, `Q_7^q`, or the compatibility statement.

Protected surfaces are unchanged: agents write only to
`agents/20260424-192320-<slug>/`.
