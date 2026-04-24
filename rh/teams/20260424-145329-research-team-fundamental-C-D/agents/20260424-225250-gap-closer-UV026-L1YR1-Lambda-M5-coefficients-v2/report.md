# Claim

The `L_1YR_1` first gate is source-reduced to an explicit finite coefficient
algorithm, but it is not closed.  From the displayed corrected same-point and
mixed block formulas one can derive:

1. the raw source-linear same-point matrix \(H_{i,\pm}=\delta
   G_{i,\pm}^{\lin}\);
2. the raw source-linear mixed matrix \(\delta N_i^{\lin}\) before the
   grade-five projection;
3. a Sylvester recurrence determining every
   \([z^r]\Lambda_{i,\pm}\) once the baseline square-root /
   inverse-square-root coefficients and \(H_{i,\pm}\) coefficients are supplied;
4. the exact \(z^7\) convolution for \(C_{112}^{L_1YR_1}\) and
   \(C_{122}^{L_1YR_1}\).

The actual positive gate still lacks the source coefficient lists
\([z^r]\Lambda_{i,\pm}\) and \([z^s]M_i^{[5]}\), in the same normalization as
\(B_7^{\mathfrak f}\).  Therefore the two determinant identities against
\(A_5^{\mathfrak f}(m)\) cannot yet be evaluated as actual-package statements.

# Status

open

# Evidence

Separate three things: proved / conditional / missing.

- **Proved from current source:** the canonical draft already states the exact
  `L_1YR_1` coefficient gate and the two determinant tests at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.
- **Proved from current source:** the tagged pre-whitening block and pair-kernel
  linear projection are present at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899`, with the explicit
  guardrail that \(B_7^{\mathfrak f}\), \(Q_{7,m}^q\), \(\Pi_{1,1}\), and the
  cubic \(A_5^{\mathfrak f}\)-gauge theorem remain separate obligations.
- **Proved from current source:** the source-linear same-point input is
  \[
  H_{i,\pm}
  =
  \frac1\pi
  \begin{pmatrix}
  2d_{i,\pm} & \frac12e_{i,\pm}\\
  \frac12e_{i,\pm} &
  \frac1{12}(g_{i,\pm}+6q_{0,\pm}^2d_{i,\pm})
  \end{pmatrix}.
  \]
  This follows from the corrected same-point formula at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`.
- **Proved from current source:** differentiating the corrected mixed formula
  at `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2784` gives the raw
  \(\delta N_i^{\lin}\) matrix recorded in
  `notes/l1yr1-coefficient-gate-notes.md`.
- **Proved algebraically:** if \(B_\pm=G_\pm^{(0)-1/2}\) and
  \(S_\pm=G_\pm^{(0)1/2}\), then
  \[
  S_\pm\Lambda_{i,\pm}+\Lambda_{i,\pm}S_\pm=-B_\pm H_{i,\pm}B_\pm.
  \]
  Hence each \(\Lambda_{i,\pm,r}\) is determined recursively by a Sylvester
  equation from the order-\(\le7\) baseline and \(H\)-coefficient lists.
- **Computational bookkeeping:** I wrote and ran
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/scripts/l1yr1_coefficient_gate.py`
  (SHA1 `375C2F718E82A95888440EC63FE20C2B550445BC`).  Output was written to
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/notes/l1yr1_coefficient_gate_output.json`
  (SHA1 `3FA8329FC6AD2CFCFE0493BFDB8D47E233ED2C30`).
- **Script output:** the \(z^7\) gate needs \(32\) \(\Lambda\)-matrices
  \((i=1,2;\ \pm;\ 0\le r\le7)\), \(16\) \(M^{[5]}\)-matrices
  \((i=1,2;\ 0\le s\le7)\), \(36\) triples \(r+s+t=7\) per ordered product,
  and \(108\) matrix products for each tag vector.
- **Conditional:** if the missing lists are supplied, the two vectors are
  exactly
  \[
  C_{112}^{L_1YR_1}
  =
  \pi_{\mathfrak f}
  \sum_{r+s+t=7}
  \bigl(
  \Lambda_{1,-,r}M_{1,s}^{[5]}\Lambda_{2,+,t}
  +\Lambda_{1,-,r}M_{2,s}^{[5]}\Lambda_{1,+,t}
  +\Lambda_{2,-,r}M_{1,s}^{[5]}\Lambda_{1,+,t}
  \bigr),
  \]
  and the analogous \(C_{122}\) formula in the notes and script output.
- **Missing:** the source does not display the order-\(\le7\) coefficient lists
  for \(G_\pm^{(0)-1/2}\), \(G_\pm^{(0)1/2}\),
  \(H_{i,\pm}\), or \(M_i^{[5]}\) in the \(B_7^{\mathfrak f}\) normalization.
- **Missing:** the source names \(M_i^{[5]}\) but does not fix whether this is
  the actual \(\delta N_i^{\lin}\) grade-five block or the scaled
  \(Y_i=\mathfrak D_Q(\delta N_i^{\lin})\) grade-five block.  That choice
  matters for the pre-\(\Phi_K\) matrix coefficient.
- **Missing:** no determinant identities
  \(u_{112}v_5-u_5v_{112}=0\) and
  \(u_{122}v_5-u_5v_{122}=0\) can be checked without the missing lists.

# Baseline / delta

Baseline: the prior `L_1YR_1` reports showed that generic Loewner algebra is
not enough, that the audited source did not already contain the actual
grade `1/5/1` matrices, and that the acceptance standard is an explicit
fixed-sector vector plus determinant test.

Delta: this pass derives the coefficient-level recurrence and raw mixed
linearization needed to compute those vectors once source lists exist.  The
blocker is now sharper than "coefficients absent": the exact positive theorem
must supply order-\(\le7\) baseline square-root lists, source-linear same-point
lists, a normalized grade-five mixed list, and then run the finite convolution.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/skills/research-resume/SKILL.md` - read
  because the brief invoked `research-resume`.
- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - full current frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 immediate subtarget.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:861`
  - coordinator theorem target.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-2048` - whitening,
  Frechet derivative, and Loewner formula.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - scaled transfer and
  \(\mathfrak D_Q\) boundary.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2787` - one-pair source
  kernels and corrected same-point/mixed formulas.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899` - tagged two-atom
  pre-whitening source block now present in the draft.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7295` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:7298-7409` - fixed-sector target,
  gauge law, \(K_5\), and \(K_3\) shadow laws.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - exact
  `L_1YR_1` target and missing coefficient-list statement.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/paper-updates.md`
  - staged UV-025 block context.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-201525-gap-closer-UV026-L1YR1-actual-matrices/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-201525-source-auditor-UV026-L1YR1-matrix-provenance/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-200718-verifier-adversarial-UV026-L1YR1-gauge/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/notes/l1yr1-coefficient-gate-notes.md`.
- Own script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/scripts/l1yr1_coefficient_gate.py`
  (SHA1 `375C2F718E82A95888440EC63FE20C2B550445BC`).
- Own script output:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/notes/l1yr1_coefficient_gate_output.json`
  (SHA1 `3FA8329FC6AD2CFCFE0493BFDB8D47E233ED2C30`).

# Dependencies

- The tagged source-linear pre-whitening block.
- A fixed normalization for \(M_i^{[5]}\): actual \(\delta N\) or scaled
  \(Y=\mathfrak D_Q(\delta N)\), matching \(B_7^{\mathfrak f}\).
- Coefficients through order \(7\) for \(G_\pm^{(0)-1/2}\) and
  \(G_\pm^{(0)1/2}\).
- Coefficients through order \(7\) for \(H_{i,\pm}=\delta G_{i,\pm}^{\lin}\).
- Coefficients through order \(7\) for the grade-five mixed input
  \(M_i^{[5]}\).
- Matching \(A_5^{\mathfrak f}(m)=u_5I+v_5S\) coordinates in the same
  fixed-sector basis.

# Strongest objection

The Sylvester recurrence may look like a positive computation of
\(\Lambda_{i,\pm}\), but it is only a deterministic reduction.  It still needs
the actual baseline square-root coefficients and the source-linear input
coefficients through order \(7\).  Likewise, the raw \(\delta N_i^{\lin}\)
formula is not yet the requested \(M_i^{[5]}\) list until the grade-five
projection and normalization are fixed.  Thus this pass does not prove gauge
or produce a counterexample.

# Needed for promotion

Promotion of this `L_1YR_1` gate needs a coefficient theorem of the following
shape.

For \(i=1,2\) and signs \(\pm\), display the order-\(\le7\) lists
\([z^r]G_\pm^{(0)-1/2}\), \([z^r]G_\pm^{(0)1/2}\), and
\([z^r]\delta G_{i,\pm}^{\lin}\), then solve the Sylvester recurrence to
display \([z^r]\Lambda_{i,\pm}\).  In the same normalization, display
\([z^s]M_i^{[5]}\).  Compute \(C_{112}^{L_1YR_1}\) and
\(C_{122}^{L_1YR_1}\) by the finite \(r+s+t=7\) convolution and prove
\[
u_{112}v_5-u_5v_{112}=0,\qquad
u_{122}v_5-u_5v_{122}=0.
\]

# Autoresearch next step

continue: look for an existing finite-order normal-form coefficient table that
gives \(G_\pm^{(0)\pm1/2}\), \(H_{i,\pm}\), and the grade-five mixed input
through order \(7\); if none exists, stage exactly the coefficient theorem
above as a new UV-026 subtarget.

verify: once any coefficient table is proposed, run the `r+s+t=7` convolution
and the two determinant tests before accepting a gauge claim.

blocked: no process blocker.  The mathematical blocker is the missing actual
order-\(\le7\) coefficient lists and the \(M_i^{[5]}\) normalization.

terminal: terminal for producing an actual `L_1YR_1` gauge vector from the
currently displayed source alone.  Not terminal for the coefficient-theorem
route.

Honest verdict: the gate is not proved, but it is now reduced to a finite,
auditable coefficient-list theorem rather than a generic Loewner witness.

# Ledger destination

attempts.md - record this route as `keep`, because it supplies the exact
coefficient recurrence/convolution and sharpens the missing theorem.  uv.md -
keep UV-026 live, optionally refine the immediate `L_1YR_1` subtarget with the
normalization requirement for \(M_i^{[5]}\).  findings.md - optional compact
frontier update: `L_1YR_1` has an explicit Sylvester/convolution gate, but the
actual order-\(\le7\) coefficient lists remain missing.
