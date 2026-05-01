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

**Sympy work** (`scripts/wip/jet-limit-blocks.py`):

- Taylor-expand \(\Ph(T\pm h)\) symbolically to order \(h^4\); substitute
  into \(K_\Ph\) at the four pair-pair points; conjugate by the
  Gram-normalized \(P_h\); confirm
  \(P_h A_h(T) P_h^\top \to J(T)\) entry by entry as \(h\to 0\).
- Re-derive \(J(T)\) directly from the kernel-derivative form
  \(\bigl(\begin{smallmatrix}2K&K_y\\K_x&\tfrac12 K_{xy}\end{smallmatrix}\bigr)\)
  and confirm the \(\tfrac1{12}(q''+2q^3)\) corner including the
  cubic correction.
- Cross-block: Taylor-expand
  \(K_\Ph(T_1+\epsilon_1 h, T_2+\epsilon_2 h)\) for
  \(\epsilon_i\in\{\pm 1\}\); conjugate by \(P_h\) on both sides;
  confirm \(N_{12}\) entries entry-by-entry.  Audit signs in the
  off-diagonal entries against the ordering of \(T_1,T_2\).
- Confirm singular powers of \(h\) cancel in every entry of both
  blocks.
- Symbolically compute \(\det J(T)\) and \(\Tr J(T)\); confirm
  positivity in terms of \(q,q',q''\) and a polynomial lower bound
  on \(\lambda_{\min}(J(T))\).

**Simulation work** (`scripts/wip/jet-limit-blocks-sim.py`):

- Compute the actual-\(\zeta\) phase \(\Ph(t)\) on a numerical window
  at heights \(T\in\{10^4,10^5,10^6\}\); estimate \(q,q',q''\) by
  finite differences; evaluate \(J(T)\) and \(N_{12}\) numerically;
  confirm \(J(T)\succ 0\) on the retained windows.
- Sweep \(\lambda_{\min}(J(T))\) across heights; fit
  \(\lambda_{\min}\sim Q^{-c}\) and report \(c\) as an empirical
  estimate of the constant \(C_J\).
- Plot entries of \(N_{12}(T_1,T_2)\) as functions of
  \(s=T_1-T_2\) at matched midpoints; confirm the
  \(\sin\Del/s\)-type leading scaling.

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

**Sympy work** (`scripts/wip/local-kernel.py`):

- Verify \(K_\Ph\) symmetry: \(K_\Ph(x,y)=K_\Ph(y,x)\).
- Confirm the removable-singularity limit
  \(\lim_{x\to y}K_\Ph(x,y)=q(y)/\pi\) symbolically.
- Compute \(\partial_x K_\Ph\), \(\partial_y K_\Ph\),
  \(\partial_{xy} K_\Ph\) at \(x=y=T\); reduce to elementary functions
  of \(q,q',q''\) and confirm the displayed kernel-derivative form
  used in §3.

**Simulation work** (`scripts/wip/local-kernel-sim.py`):

- Build a numerical \(\Ph\) on a window at \(T=10^6\) using the
  Riemann--Siegel phase of \(\zeta\); confirm chart-denominator
  regularity (no poles in the window) and bound \(q,q',q''\) on the
  window numerically.  Report empirical polynomial-in-\(Q\) constants
  for downstream use.
- Verify the chart is real-valued on the retained packet interval; flag
  any height where chart-existence fails so the open input can be
  refined.

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

**Sympy work** (`scripts/wip/odd-moment-cancellation.py`):

- For \(N\in\{2,3,4\}\): construct a generic symmetric \(N\)-point
  packet measure \(\widehat\mu_{N,Q}\) (symbolic, even), confirm
  \(\partial_z^{2r+1}\widehat\mu_{N,Q}(0)=0\) for \(r\in\{0,1,2,3\}\).
- Confirm the convolution identity:
  \(\partial_z^{2r+1}(\widehat\phi(\eta z)\widehat\mu_{N,Q}(z))|_{z=0}=0\)
  for an even bump \(\widehat\phi\).
- Audit the parity-of-coefficients argument in v1's
  \(N\)-point odd-moment cancellation section (line 4312): confirm
  step by step that no implicit asymmetry is introduced by the
  packet weights.

**Simulation work** (`scripts/wip/odd-moment-cancellation-sim.py`):

- Generate random even bumps \(\widehat\phi\) and even packet
  measures \(\widehat\mu_{N,Q}\); compute the smoothed odd
  derivatives at \(z=0\) numerically; confirm vanishing to
  machine precision (\(\sim 10^{-12}\)).
- Test on packet measures derived from actual \(\zeta\) at a high
  height (numerical Fourier transforms of a window); confirm the
  identity holds within numerical noise.

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

**Sympy work** (`scripts/wip/finite-blocks-whitening.py`):

- Substitute \(t_\pm=m\pm s/2\) into the displayed \(J\) form;
  confirm \(G_{m,\pm}(s)\) entries match the rebuild's display.
- Symbolically expand \(N_m(s)\) entries from the kernel-derivative
  form at \((t_-,t_+)\); confirm the displayed
  \(\tfrac{2\sin\Del_m(s)}{\pi s}\) and other entries.
- Compute \(G_{m,\pm}(s)^{-1/2}\) symbolically (closed form for a
  \(2\times 2\) symmetric positive-definite block); confirm the
  operator-norm distortion bound by an explicit polynomial in
  \(\det G_{m,\pm}\) and \(\Tr G_{m,\pm}\).
- Multiply out
  \(\widehat\Om_\z(s;m)=G_{m,-}^{-1/2}N_m G_{m,+}^{-1/2}\)
  symbolically; confirm dimensionlessness and check the leading
  \(s\to 0\) behavior reduces to \(N_{12}\) under
  appropriate rescaling.
- Confirm the whitening-loss bound: derive an explicit polynomial
  \(\|G_{m,\pm}^{-1/2}\|_\op \le P(\lambda_{\min}(G))^{-1/2}\) and
  compose with §3's positivity to bound by \(Q^{C_W}\).

**Simulation work** (`scripts/wip/finite-blocks-whitening-sim.py`):

- For \(\zeta\) at \(T=10^6\): pick midpoints \(m\in I_T\) and
  separations \(s\in(0,1/Q]\); compute \(G_{m,\pm}(s)\),
  \(N_m(s)\), \(\widehat\Om_\z(s;m)\) numerically; track
  \(\|G_{m,\pm}^{-1/2}\|_\op\); fit \(\|\cdot\|_\op\sim Q^{c_W}\)
  to estimate \(C_W\).
- Sweep \(s/Q\in[0.01,1.0]\) and \(m\) across the window; confirm a
  uniform polynomial-in-\(Q\) bound on the whitening loss across
  the retained set.  Flag any \((m,s)\) where
  \(\lambda_{\min}(G_{m,\pm})\) drops below the predicted polynomial
  floor.

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

**Sympy work** (`scripts/wip/toy-visibility.py`):

- Construct \(\Ph_\toy(t;\beta,Q)\) as the explicit split-pair
  phase; compute \(q_\toy,q_\toy',q_\toy''\) symbolically as
  elementary functions of \((2\beta-1)\) and the local coordinate.
- Compute \(G_\toy, N_\toy, \widehat\Om_\toy(s;m)\) symbolically
  using the same Gram-normalized form as §4.
- Define \(\mathcal A_\toy\) as a specific polynomial combination of
  \(\widehat\Om_\toy\) entries selected to vanish at
  \(\beta=\tfrac12\); confirm vanishing symbolically.
- For \(\beta\ne\tfrac12\): expand \(\|\Pi_\trans\mathcal A_\toy\|\)
  to leading order; confirm
  \(\|\Pi_\trans\mathcal A_\toy\|\sim
  c\,(\beta-\tfrac12)^{k}\,Q^{-A_\toy}\) for explicit \(k,A_\toy\)
  and \(c>0\).
- Confirm the lower bound is insensitive to the residual gauge of
  \(\Ph_\toy\) (apply each gauge transformation symbolically; the
  bound persists).

**Simulation work** (`scripts/wip/toy-visibility-sim.py`):

- Sweep \(\beta\in(0.5,0.9)\) at fixed \(Q\); plot
  \(\|\Pi_\trans\mathcal A_\toy(\widehat\Om_\toy(s;m))\|\) at fixed
  \(s,m\); confirm the polynomial-in-\((\beta-\tfrac12)\) leading
  scaling.
- Sweep \(Q\in[10,10^4]\) at fixed \(\beta\); fit a power law and
  recover the exponent \(A_\toy\).
- Sample \((m,s)\) on a polynomial-weight subset; confirm the
  visibility lower bound holds across at least a polynomial-in-\(Q\)
  fraction of the sample.

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

**Sympy work** (`scripts/wip/transverse-projection.py`):

- For each candidate \(\mathcal V_\val\) (value-only;
  value+gauge; value+gauge+background): compute the orthogonal
  projection \(\Pi_\trans\) in the Gram-normalized inner product
  symbolically; confirm \(\Pi_\trans\mathcal V_\val=0\).
- Verify gauge invariance: apply each residual-gauge transformation
  of \(\Ph\) (additive-constant, affine-jet shift, allowed
  background corrections); confirm \(\mathcal V_\val\) maps to
  itself and \(\Pi_\trans\) commutes.
- Compute the operator norm and condition number of \(\Pi_\trans\)
  symbolically on retained packets; confirm a polynomial-in-\(Q\)
  bound.
- Cross-verify three convention choices (corrected fixed-target,
  leading value, projective-rigidity gauge): which one preserves
  toy visibility?  Which one annihilates the surviving zeta-side
  channel?  Document the chosen convention and the reasons the
  others fail.

**Simulation work** (`scripts/wip/transverse-projection-sim.py`):

- Apply \(\Pi_\trans\) numerically to test vectors aligned with
  value, gauge, and background directions; confirm exact (or
  machine-precision) annihilation.
- Apply to off-line "anomaly" direction over a sweep
  \(\beta\in(0.5,0.9), Q\in[10,10^4]\); confirm polynomial-in-\(Q\)
  lower bound on \(\|\Pi_\trans v\|\).
- Test gauge invariance numerically: apply random allowed gauge
  transformations to a packet; confirm \(\|\Pi_\trans v\|\) is
  unchanged.

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

**Sympy work** (`scripts/wip/two-point-comparison.py`):

- Compose Theorem~\ref{thm:toy-anomaly-visibility} (lower) with
  Hypothesis~\ref{hyp:zeta-suppression-two-point} (upper) at matched
  \((m,s)\); track the polynomial losses from \(P_h\), Gram
  positivity (\(Q^{-C_J}\)), and whitening (\(Q^{C_W}\)) explicitly.
- Derive the explicit exponent inequality
  \(A_\toy + 2C_W + C_J < B_{\z,2}\) (or its sharp form); identify
  the critical \(Q^*\) below which the two-point exclusion fails
  numerically.
- Confirm the inequality is preserved under re-conjugation by
  \(\diag(\sqrt 2,1/\sqrt 2)\) (Gram-vs-jet invariance); the
  two-point exclusion should not depend on the choice of
  normalization.

**Simulation work** (`scripts/wip/two-point-comparison-sim.py`):

- Empirical test of the exponent gap: at heights
  \(T\in\{10^4,10^6,10^8\}\), pair \((T_1,T_2)\) chosen near a
  hypothetical off-line zero; compute
  \(\|\Pi_\trans \mathcal A_2(\widehat\Om_\z(s;m))\|\) and
  \(\|\Pi_\trans \mathcal A_\toy(\widehat\Om_\toy(s;m))\|\) at
  matched \((m,s)\); confirm the empirical separation matches the
  theoretical \(A_\toy<B_{\z,2}\).
- Sweep across all known on-line zeros (e.g.\ Odlyzko's tables) at
  one height; confirm the rigidity inequality is consistent with
  empirical \(\zeta\) data (this is a sanity check, not a proof
  test).
- *Note:* if the empirical \(\zeta\)-side decay is shallower than
  predicted, that falsifies
  Hypothesis~\ref{hyp:zeta-suppression-two-point} for those heights
  --- which is itself useful information.

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

**Sympy work** (`scripts/wip/aggregation.py`):

- Combine the per-height polynomial losses \(C_J(Q), C_W(Q),
  A_\toy(Q), B_{\z,2}(Q)\) symbolically along the dyadic ladder
  \(Q_k=2^k\); confirm the combined exponent gap is uniform in
  \(k\).
- Derive an explicit \(T_0\) below which numerical verification is
  required and above which Theorem~\ref{thm:zero-free-strip}
  applies; record the constant.

**Simulation work** (`scripts/wip/aggregation-sim.py`):

- Compute the empirical constants
  \(\hat C_J(Q),\hat C_W(Q),\hat A_\toy(Q),\hat B_{\z,2}(Q)\) at
  \(Q\in\{2^{10},2^{15},2^{20}\}\); confirm polynomial scaling and
  fit explicit polynomial bounds.
- For §11: cross-reference Odlyzko's numerical tables for low-height
  RH verification (no re-computation; cite as bibliography).

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

**Sympy work** (`scripts/wip/zeta-suppression-two-point.py`):

- Compute \(\Pi_\trans \mathcal A_2(\widehat\Om_\z(s;m))\)
  symbolically using the symmetry-quartet structure
  \(\rho\mapsto\bar\rho\) acting on \(\zeta\); identify the leading
  surviving term (if any) under the value/gauge quotient.
- If a leading term survives, compute its scaling in \(Q\); if it
  vanishes at leading order, identify the next surviving order and
  attempt to bound it polynomially in \(Q\) from local data alone.
- Confirm the local data alone (\(q,q',q''\) and their cross-block
  variants) is or is not sufficient to bound the surviving term;
  this distinguishes standalone vs.\ Hardy-assisted regimes.

**Simulation work** (`scripts/wip/zeta-suppression-two-point-sim.py`):

- Heavy: compute
  \(\|\Pi_\trans \mathcal A_2(\widehat\Om_\z(s;m))\|\) for actual
  \(\zeta\) at \(T\in\{10^6,10^9,10^{12}\}\); fit a power-law decay
  in \(Q\); empirically estimate \(B_{\z,2}\).
- Compare empirical \(B_{\z,2}\) against the toy exponent
  \(A_\toy\): does \(B_{\z,2}>A_\toy\) survive at all tested
  heights?
- If empirical \(B_{\z,2}\le A_\toy\) at any tested height, that
  is positive evidence that the standalone hypothesis fails and
  the source-energy route is needed.

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

**Sympy work** (`scripts/wip/zeta-suppression-four-point.py`):

- Construct \(\widehat\Om_\z^{(4)}\) and \(\Pi_\trans^{(4)}\)
  symbolically as the four-center analogue; confirm consistency
  with the two-point versions in the appropriate degeneracy limits.
- Compute \(\Pi_\trans^{(4)}\mathcal A_4(\widehat\Om_\z^{(4)})\)
  using the full quartet symmetry
  \(\{\rho,\bar\rho,1-\rho,1-\bar\rho\}\); identify the leading
  surviving term and its \(Q\)-scaling.
- Confirm the four-point quotient is strictly finer than the
  two-point quotient (i.e.\ the four-point comparison is in fact
  stronger).

**Simulation work** (`scripts/wip/zeta-suppression-four-point-sim.py`):

- Same as §7.1 but applied to the four-center analogue: empirical
  decay of \(\|\Pi_\trans^{(4)}\mathcal A_4(\widehat\Om_\z^{(4)})\|\)
  in \(Q\) at heights \(T\in\{10^6,10^9,10^{12}\}\).
- Cross-check: confirm the four-point empirical bound is at least
  as strong as the two-point empirical bound at the same heights.

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

**Sympy work** (`scripts/wip/source-energy.py`):

- Compute \(q''_\can(t)=\partial_t^3 Z(t)\) symbolically for an
  elementary test phase \(Z\); confirm the operator-on-\(\Ph\)
  identity in the chosen gauge.
- Carrier decomposition: split
  \(q''_\can = u_\car + u_\tail\) into orthogonal carrier and tail
  components; verify
  \(\|q''_\can\|_2^2 = \|u_\car\|_2^2 + \|u_\tail\|_2^2\) and that
  the carrier projector commutes with the gauge.
- Compute the source-to-jet transfer map symbolically; confirm it
  lands the source energy in the transverse channel of
  \(\widehat\Om_\z(s;m)\) (or its four-point analogue).
- Derive the explicit dependence \(B_{\z,2}=B_{\z,2}(A_E)\) and the
  inequality \(B_{\z,2}>A_\toy\) given a polynomial source-energy
  lower bound.

**Simulation work** (`scripts/wip/source-energy-sim.py`):

- Compute \(\int_I |q''_\can(m)|^2\,dm\) numerically for actual
  \(\zeta\) at heights \(T\in\{10^6,10^9,10^{12}\}\); fit a
  polynomial-in-\(Q\) lower bound; estimate \(A_E\).
- Compute the carrier capture
  \(\sum_p\mu_p\|\Pi_\eff\Pi_\car q''_\can\|_{\mathrm{pkt}}^2\)
  numerically; verify polynomial-in-\(Q\) lower bound.
- Confirm the source-side estimate combined with the transfer
  exponent yields a numerical \(B_{\z,2}\) (or \(B_{\z,4}\))
  exceeding \(A_\toy\) at the tested heights.

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

**Sympy work** (`scripts/wip/four-point-comparison.py`):

- Construct \(\widehat\Om_\z^{(4)}\) and \(\Pi_\trans^{(4)}\)
  symbolically as four-center extensions; confirm consistency with
  the two-point setup under degeneracy of the quartet.
- Compose
  \(\|\Pi_\trans^{(4)}\mathcal A_4(\widehat\Om_\toy^{(4)})\|\ge
  Q^{-A_\toy^{(4)}}\) with
  \(\|\Pi_\trans^{(4)}\mathcal A_4(\widehat\Om_\z^{(4)})\|\le
  Q^{-B_{\z,4}}\); track polynomial losses; derive
  \(A_\toy^{(4)}+(\text{losses})<B_{\z,4}\).
- Confirm that the four-point exponent gap is strictly larger than
  the two-point gap (otherwise four-point adds nothing).

**Simulation work** (`scripts/wip/four-point-comparison-sim.py`):

- Empirical four-point exclusion: at heights
  \(T\in\{10^6,10^9\}\), construct synthetic quartets
  \(\{\rho,\bar\rho,1-\rho,1-\bar\rho\}\) at off-line
  \(\beta\in(0.5,0.9)\); compute the four-point
  \(\widehat\Om_\toy^{(4)}\) and confirm
  \(\|\Pi_\trans^{(4)}\mathcal A_4\|\ge Q^{-A_\toy^{(4)}}\).
- For actual \(\zeta\) data: pick a quartet of test heights;
  compute \(\widehat\Om_\z^{(4)}\); confirm empirical
  \(B_{\z,4}>A_\toy^{(4)}\).

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
