# v1 → rebuild migration plan

Tracks per-section migration of `rh/proof_of_rh.tex` (the v1 quarry) into
`rh/rh_rebuild.tex` (the active draft).  For migration discipline (per-section
workflow, three-bin status, adversarial review) see `CLAUDE.md` (`Migration
workflow`).  Each rebuild section's `\statusmig` tag in `rh_rebuild.tex` mirrors
the **current** column below.

v1 sections with a `\label` key are noted as `sec:<key>`; the rest are
identified by title + the line number in `proof_of_rh.tex` where the section
header lives.  All v1 line numbers are as of commit `ab0caa5`.

---

## Migration order

Strict dependency, bottom-up, easy-first within tier.  No section migrates
before its prerequisites.  Migration targets and research targets are
distinguished: migration = v1 has the content, work is restate-and-verify;
research = v1 has attempts but no closure, work is open mathematics.

| Order | Rebuild | Type | Status |
|---|---|---|---|
| 1 | §3 Jet-limit local blocks | migration | not-started |
| 2 | §2 Local kernel and jet normalization | migration | not-started |
| 3 | §9 \(N\)-point odd-moment cancellation | migration | not-started |
| 4 | §4 Finite-scale local blocks and whitening | migration | not-started |
| 5 | §5 Toy anomaly and transverse obstruction | migration | not-started |
| 6 | §6 Transverse projection | migration (sensitive) | not-started |
| 7 | §8.1 Two-point comparison | migration | not-started |
| 8 | §10 Aggregation and zero-free strip | migration (light) | not-started |
| 9 | §11 The Riemann hypothesis | migration (light) | not-started |
| 10 | §7.1 Two-point actual-zeta suppression | research | not-started |
| 11 | §7.2 Four-point actual-zeta suppression | research | not-started |
| 12 | §12 Source-energy supply (optional) | migration, only if §7.1/§7.2 standalone fails | not-started |
| 13 | §8.2 Four-point comparison | migration, only after §8.1 closes | not-started |

Always-`n/a` (no migration target):

- §1 Introduction — rebuild-original prose; `\statusmig{n/a}`.
- App.\ A Archive map — meta-pointer; `\statusmig{n/a}`.

---

## §3 Jet-limit local blocks

**Rebuild:** `sec:jet-limit-local-blocks` — the matrices \(J(T)\) and
\(N_{12}(T_1,T_2)\), Gram positivity of \(J(T)\).

**v1 sources:**

- `Local kernel and jet normalization` — line 637, subsection
  `Jet-limit local blocks` at line 960.
  This is the primary source: same-point and cross-block jet limits.
- `Smooth remainder after affine-jet subtraction` — line 1091.
  Curvature/tail material that feeds same-point Gram positivity.
- `Tail curvature bound` — line 1132.

**Migration notes:**

- v1 prints the literal-jet \(P_h^{\mathrm{old}}=\tfrac12\bigl(\begin{smallmatrix}1&1\\-1/h&1/h\end{smallmatrix}\bigr)\)
  but its displayed \(J(T)\) belongs to the Gram-normalized
  \(P_h\) of \eqref{eq:point-to-jet-transform}.  Re-conjugate by
  \(\diag(\sqrt 2, 1/\sqrt 2)\) before importing any v1 lemma; see
  `rem:normalization-audit` in `rh_rebuild.tex`.
- sympy script: re-derive the entries of \(J(T)\) and \(N_{12}\) from
  the kernel-derivative form
  \(J(T)=\bigl(\begin{smallmatrix}2K&K_y\\K_x&\tfrac12 K_{xy}\end{smallmatrix}\bigr)\)
  to confirm the Gram-normalized result entry by entry.  Place at
  `scripts/wip/jet-limit-blocks.py`.

**Closes (when migrated):**
`rem:wip-same-point-jet-limit`, `rem:wip-cross-block-jet-limit`,
`rem:wip-same-point-gram-positivity`.

---

## §2 Local kernel and jet normalization

**Rebuild:** `sec:local-kernel-and-jet-normalization` — local phase chart,
phase kernel, point-to-jet transform.

**v1 sources:**

- `Local kernel and jet normalization` — line 637, the
  pre-`Jet-limit local blocks' material (chart, kernel definition,
  symmetric-pair convention).
- `Zeta-side decomposition` — line 1060, `Curvature estimate`
  subsection at line 1083.

**Migration notes:**

- v1's `\Ph` chart is fixed in the same gauge; what is missing in v1
  is a clean polynomial lower-bound theorem on chart denominators and
  derivatives.  Migrate the construction prose; leave the polynomial
  bounds as an Open Input until source-side work fills them.
- The Gram-normalized \(P_h\) is already in place (rebuild commit
  `ab0caa5`); v1's \(P_h^{\mathrm{old}}\) is not migrated.

**Closes (when migrated):**
Partial close of `rem:wip-local-phase-chart` (chart construction,
not the polynomial bounds).

---

## §9 \(N\)-point odd-moment cancellation

**Rebuild:** `sec:n-point-odd-moment-cancellation` — parity vanishing
for symmetric \(N\)-point packet measures.

**v1 sources:**

- `\(N\)-point odd-moment cancellation` — line 4312.
  Self-contained parity argument; clean migration.

**Migration notes:**

- Pure parity.  Verify the symmetry packet of v1 matches
  `def:local-phase-chart` of the rebuild before importing.
- sympy script: re-derive
  \(\partial_z^{2r+1}\widehat\mu_{N,Q}(0)=0\) from a generic even
  \(\widehat\mu_{N,Q}\); confirm the smoothed identity for an even
  bump \(\widehat\phi\).  Place at
  `scripts/wip/odd-moment-cancellation.py`.

**Closes (when migrated):**
`rem:wip-n-point-odd-moment-cancellation`.

---

## §4 Finite-scale local blocks and whitening

**Rebuild:** `sec:finite-scale-local-blocks-and-whitening` — finite
\(G_{m,\pm}(s)\), \(N_m(s)\), whitened block
\(\widehat\Om_\z(s;m)\), whitening-loss bound.

**v1 sources:**

- `Finite-\(s\) local blocks` — line 1007 (symmetric placement,
  removable singularity).
- `Corrected finite-\(s\) holomorphic whitening` — line 1641.
  Primary whitening-loss material.
- `Finite Fr\'echet coefficient calculus for the corrected-whitening
  block` — `sec:finite-frechet-coefficient-calculus` at line 51984.
- `Finite coefficient table contracts for the corrected-whitening
  package` — line 54584 (no v1 label).

**Migration notes:**

- The four-table package
  (`Finite Fr\'echet ...` + `Finite coefficient table contracts ...`)
  is large and route-historical in places; mine only the parts
  needed for the whitening-loss bound and the entries of \(N_m(s)\).
- Re-conjugate any imported finite-\(s\) block by
  \(\diag(\sqrt 2, 1/\sqrt 2)\) at both centers (Gram-normalized
  convention applies here as well).
- sympy script: confirm \(N_m(s)\) entries from the kernel-derivative
  form, then symbolically multiply by \(G_{m,-}(s)^{-1/2}\) and
  \(G_{m,+}(s)^{-1/2}\) to inspect the structure of
  \(\widehat\Om_\z(s;m)\).  Place at
  `scripts/wip/finite-blocks-whitening.py`.

**Closes (when migrated):**
`rem:wip-whitening-loss`.

---

## §5 Toy anomaly and transverse obstruction

**Rebuild:** `sec:toy-anomaly-and-transverse-obstruction` — toy phase
\(\Ph_\toy\), toy anomaly visibility lower bound.

**v1 sources:**

- `Toy anomaly and transverse obstruction` — line 1187.
- `Toy microscopic expansion` — line 51895 (no v1 label).
  Microscopic expansion of \(\Ph_\toy\) and its derivatives.

**Migration notes:**

- \(\Ph_\toy\) is parameterized by \((2\beta-1)\) and the local
  coordinate; elementary.
- Define \(\mathcal A_\toy\) explicitly from the entries of
  \(\widehat\Om_\toy(s;m)\) before stating the lower bound; do not
  let \(\mathcal A_\toy\) drift.
- The visibility lower bound \(\|\Pi_\trans \mathcal
  A_\toy\|\ge Q^{-A_\toy}\) is provable in the rebuild's clean
  setup once \(\mathcal A_\toy\) and \(\Pi_\trans\) are fixed.
- sympy script: at \(\beta=\tfrac12\), confirm \(\mathcal
  A_\toy\equiv 0\); for \(\beta\ne\tfrac12\), confirm a polynomial
  lower bound in \((\beta-\tfrac12)\) on the leading entry.  Place
  at `scripts/wip/toy-visibility.py`.

**Closes (when migrated):**
`rem:wip-off-line-toy-phase`, `rem:wip-toy-anomaly-visibility`.

---

## §6 Transverse projection

**Rebuild:** `sec:transverse-projection` — fixed value/gauge subspace
\(\mathcal V_\val\), projection \(\Pi_\trans\).

**v1 sources:**

- `Leading value matrix and canonical calibration` — line 1215.
  v1's primary construction of the value subspace.
- `Corrected fixed-target quotient package` —
  `sec:corrected-fixed-target-quotient-package` at line 53353.
- `Local projective rigidity of the one-pair and multi-pair
  families` — `sec:projective-rigidity` at line 7040
  (subsection `Normalization gauge at the first residual step` at
  line 7505 is directly relevant).

**Migration notes:**

- This is the **most sensitive structural decision in the rebuild**:
  the choice of \(\mathcal V_\val\) must precede
  Theorem~\ref{thm:toy-anomaly-visibility} and
  Hypotheses~\ref{hyp:zeta-suppression-two-point}
  and~\ref{hyp:zeta-suppression-four-point}.  Once chosen, freeze it
  in writing; do not re-choose to fit a downstream cancellation.
- v1 has multiple competing projection conventions across the
  cited sections (corrected fixed-target vs.\ leading value vs.\
  projective rigidity gauge).  Pick one, restate cleanly, document
  why the others were rejected.
- Adopting the Gram-normalized basis (rebuild §2.3) constrains the
  candidates: the projection acts on the Gram-normalized jet space,
  not the literal-jet space.

**Closes (when migrated):**
`rem:wip-transverse-projection` and pins the meaning of
\(\Pi_\trans\) for every downstream comparison.

---

## §8.1 Two-point comparison

**Rebuild:** `sec:projective-rigidity`, `subsec:two-point-comparison` ---
the two-point rigidity theorem
\(A_\toy<B_{\z,2} \Rightarrow \rho\notin\{\zeta=0\}\).

**v1 sources:**

- `Local projective rigidity of the one-pair and multi-pair
  families` — `sec:projective-rigidity` at line 7040, the one-pair
  subsections (lines 7050, 7505, 7952, 8347, 9430).
- `Finite coefficient table contracts for the corrected-whitening
  package` — line 54584 (selected coefficient identities).

**Migration notes:**

- The proof itself is short --- arithmetic on absolute exponents
  --- once §3, §5, §6, and the two-point version of \(\widehat\Om_\z\)
  are migrated.
- v1's one-pair material includes route-history (residual class,
  cubic leading line, fixed-sector refinement); migrate only the
  exponent-inequality proof, not the v1 narrative.
- Cross-checks: confirm \(B_{\z,2}>A_\toy\) survives the polynomial
  whitening loss \(Q^{C_W}\) and the polynomial Gram lower bound
  \(Q^{-C_J}\).

**Closes (when migrated):**
`rem:wip-two-point-rigidity`.  Also frees §10, §11 to migrate as
bookkeeping.

---

## §10 Aggregation and zero-free strip, §11 The Riemann hypothesis

**Rebuild:** `sec:aggregation-and-zero-free-strip`,
`sec:riemann-hypothesis`.

**v1 sources:**

- `Introduction`, `Master conditional theorem` — lines 114, 154.
  v1's master conditional discusses the height-ladder / aggregation
  step inline.

**Migration notes:**

- Once §8.1 closes, §10 is dyadic-ladder bookkeeping: the polynomial
  losses combine into one polynomial-in-\(Q(\gamma)\) factor, and the
  exponent inequality \(A_\toy<B_{\z,2}\) carries through.
- §11 is one paragraph: combine
  Theorem~\ref{thm:zero-free-strip} with standard low-height
  numerical verification.

**Closes (when migrated):**
`rem:wip-zero-free-strip` and `rem:wip-master-conditional`.

---

## §7.1 Two-point actual-zeta suppression  *(research target)*

**Rebuild:** `subsec:two-point-suppression` ---
Hypothesis~\ref{hyp:zeta-suppression-two-point}.

**v1 sources:**

- `Odd holomorphic transverse channel` — line 3001.  Primary v1
  attempt at actual-zeta suppression in the transverse channel.
- `Corrected fixed-target quotient package` —
  `sec:corrected-fixed-target-quotient-package` at line 53353.
- `Corrected finite-\(s\) holomorphic whitening` — line 1641
  (suppression-relevant parts).

**Status:** *research target, not migration target.*  v1 has
**attempts**, not closure, on this gap.  Treat after §1–§6 and §8.1
are solid: the rebuild's clean Gram-normalized framework may admit a
suppression argument that v1's tangled framework did not.  If a
standalone proof fails after honest effort, fall back to the
source-energy route via §12.

---

## §7.2 Four-point actual-zeta suppression  *(research target)*

**Rebuild:** `subsec:four-point-suppression` ---
Hypothesis~\ref{hyp:zeta-suppression-four-point}.

**v1 sources:**

- `Local projective rigidity of the one-pair and multi-pair
  families` — `sec:projective-rigidity` at line 7040, the
  multi-pair / two-pair subsections (`From the one-pair residual
  germ to two-pair and minimal-core rigidity` at line 12638).
- `Endgame architecture and remaining propagation problem outside
  the clean mixed four-point case` — line 29911.

**Status:** *research target, not migration target.*  Same disposition
as §7.1.  Wait until §8.1 (two-point comparison) closes; the
four-point machinery may not be needed if two-point closes the
program.

---

## §12 Source-energy supply  *(optional, only if §7.1 or §7.2 standalone fails)*

**Rebuild:** `sec:source-energy-supply` --- canonical source curvature
\(q''_\can=\partial_t^3 Z(t)\), source-energy lower bound
(`hyp:source-energy-bound`), energy-to-suppression transfer
(`lem:source-energy-to-suppression`).

**v1 sources:**

- `Upstream Gate--1 arithmetic inputs after the ordinary-route
  audit` — `sec:upstream-gate-one-arithmetic-inputs` at line 55102.
- `Certified downstream status after the canonical source-graded
  closure` — `sec:final-status-after-downstream-closure-repairs`
  at line 60323.
- *(literal v1 prose pointer, kept as quotation)* the
  `Hardy-curvature mass-good packet source block` material
  embedded in the later v1 sections.

**Migration notes:**

- **Do not migrate prematurely.**  The Hardy/source-transfer work
  is what made v1 unmanageable.  Migrate only after §7.1 or §7.2
  standalone proof attempts have been seriously tried and failed.
- Active claim is now neutral: the source is a real critical-line
  scalar \(Z(t)\); whether it is Hardy-normalized is open.  Strip
  any imported v1 prose of `Hardy-normalized' assertions; leave
  v1 section names intact only where they are literal pointers.
- The transfer lemma now implies *one of* the two suppression
  hypotheses depending on which carrier transfer is established,
  not both.

**Closes (when migrated):**
`rem:wip-canonical-source-curvature`, `rem:wip-source-energy-bound`,
`rem:wip-source-energy-to-suppression`.

---

## §8.2 Four-point comparison  *(only after §8.1 closes)*

**Rebuild:** `sec:projective-rigidity`,
`subsec:four-point-comparison-symmetric-quartet`.

**v1 sources:** same as §7.2 multi-pair material above.

**Migration notes:**

- Wait until §8.1 (two-point) fully closes.  If two-point closes the
  program, four-point may be unnecessary; if it does not, the
  four-point material is the next attempt.
- Migrating four-point requires defining \(\widehat\Om_\z^{(4)}\)
  and \(\Pi_\trans^{(4)}\); these are absent from the rebuild as
  stated and must be constructed.

**Closes (when migrated):**
`rem:wip-four-point-rigidity`.

---

## v1 sections deliberately not migrated

These v1 sections are route history, archive, or process bookkeeping;
they are excluded from the rebuild's active proof line.

| v1 line | v1 section |
|---|---|
| 29911 | Endgame architecture and remaining propagation problem outside the clean mixed four-point case |
| 30820 | Downstream local closure package: Gate 2, wall escape, and carrier rows (`sec:downstream-local-closure-package`) |
| 30855 | Unified finite-survival architecture (`sec:unified-finite-survival-architecture`) |
| 32566 | Current proof state after the local package audits (`sec:current-proof-state-after-local-audits`) |
| 51154 | How the older framing maps to the new framing (`sec:old-to-new-framing`) |
| 51189 | No-go and audit ledger (`sec:no-go-and-audit-ledger`) |

Specific computations within these sections may be cited via the
appendix `Archive map` if they support a rebuild migration; the v1
prose itself is not pulled in.
