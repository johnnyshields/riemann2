# Claim

Current source does not define or imply the baseline \(q_0\) derivative table
needed by the UV-026 Stage 1 generator.  It defines \(q=\Phi'\), introduces
baseline objects \(q_0,\Phi_0\), uses \(q_0(t_\pm)\), \(q_0'(t_\pm)\), and
\(q_0''(t_\pm)\) in the baseline block formulas, and supplies scale estimates.
It does not display exact formulas or values for
\[
q_0^{(k)}(m),\qquad 0\le k\le9,
\]
nor does it state a theorem reducing these ten jets to explicit baseline
objects in the same ordinary-\(z\), pre-\(\Phi_K\) normalization used by
\[
B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7].
\]

Source verdict: the baseline \(q_0\)-jet theorem remains missing.  Scale
estimates for \(q_0,q_0',q_0'',q_0'''\), holomorphy, and the
\(\mathfrak D_Q\) transfer bounds are not coefficient tables.

# Status

open

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The paper defines the phase derivative by
\[
q(t):=\Phi'(t).
\]
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:157-160`.

**Proved from source.**  The finite mixed variables use
\[
q_\pm(s):=q(t_\pm),\qquad \Delta_m(s):=\Phi(t_-)-\Phi(t_+).
\]
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:249-253`.

**Proved from source.**  The zeta-side decomposition writes
\[
q(t)=q_{\loc}(t)+g_{\sm}(t)+E_{\est}(t),\qquad
g_{\sm}=B_{\Aut}+T_{\far},
\]
and the jet-corrected phase has derivative
\[
\Phi_{\jet}'(t)=q_{\loc}(t)+J_1[g_{\sm}](t)+E_{\est}(t).
\]
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:273-283` and
`C:/workspace/riemann2/rh/proof_of_rh.tex:323-327`.

**Proved from source.**  The baseline same-point block is built from
\[
q(t)=q_0(t)+\delta q(t),
\]
where \(q_0\) is described as the baseline local-model-plus-affine-jet part.
The displayed baseline same-point block uses \(q_0(t_\pm)\),
\(q_0'(t_\pm)\), and \(q_0''(t_\pm)\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:964-974`.

**Proved from source.**  The corrected mixed block baseline uses
\[
q=q_0+\delta q,\qquad \Phi=\Phi_0+\delta\Phi,\qquad
\Delta_0(s)=\Phi_0(t_-)-\Phi_0(t_+).
\]
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:1149-1164`.

**Proved from source.**  The paper later uses only baseline entry scales for
\(G_\pm^{(0)}\), \(G_\pm^{(0)-1/2}\), and \(N^{(0)}\), read from formulas and
local scales for \(q_0,q_0',q_0''\).  These are scale estimates, not
coefficient tables.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:1760-1795`.

**Proved from source.**  The coefficient-level transfer fixes the relevant
coordinate conversion
\[
s=\frac{z}{Q^2}=\frac{Rw}{Q^2}
\]
and defines \(\mathfrak D_Q\), but the transfer proposition is after
\(\Phi_K\) and supplies analytic bounds, not pre-\(\Phi_K\) baseline tables.
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587`.

**Proved from nearby source.**  The baseline variation lemma says
\(G_{m,\pm}^{(0)}\) is built from the explicit local model together with the
affine jet \(J_1[g_{\sm}]\), and supplies local scales for
\[
q_0,\quad q_0',\quad q_0'',\quad q_0'''.
\]
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:1332-1378`.

**Proved from generator deposit.**  The Stage 1 generator manifest requires ten
baseline scalar inputs:
\[
q_0^{(k)}(m),\qquad 0\le k\le9.
\]
It reconstructs
\[
q_{0,\pm}(z)=q_0(m\pm z/(2Q^2))
\]
and
\[
\Delta_0(z)=\Phi_0(t_-)-\Phi_0(t_+)
\]
from those inputs.  Source:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md`
and
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json`.

**Conditional.**  The source plausibly reduces \(q_0\) to
\[
q_{\loc}+J_1[g_{\sm}]+E_{\est}
\]
because the jet-corrected phase derivative has this form and the baseline is
described as local-model plus affine jet.  But no inspected source states the
exact equality \(q_0=q_{\loc}+J_1[g_{\sm}]+E_{\est}\) as the Stage 1 baseline
definition, nor gives the ten midpoint derivatives that would follow.

**Missing.**  No inspected source displays
\[
q_0^{(k)}(m),\qquad 0\le k\le9,
\]
or formulas for those derivatives in terms of \(q_{\loc}\),
\(J_1[g_{\sm}]\), \(E_{\est}\), \(B_{\Aut}\), \(T_{\far}\), or other named
baseline objects.

**Missing.**  No inspected source provides ordinary-\(z\) coefficient tables
for \(G_\pm^{(0)}(z)\), \(N_0(z)\), or \(\Delta_0(z)\) through \(z^7\) using
actual baseline \(q_0\) jets.

**Missing.**  No inspected source proves that the residual bookkeeping term
\(E_{\est}\) is zero, negligible, quotient-invisible, or otherwise removable
from the Stage 1 \(B_7^{\mathfrak f}\) baseline tables.

No computational claim is made in this audit; no script was needed.

Guardrails are deposited at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-verifier-source-UV026-baseline-q0-jets/notes/baseline-q0-jet-guardrails.md`.

# Baseline / delta

Baseline: the Stage 1 generator has been verified as infrastructure.  The
current UV-026 source-table input has two independent blockers: the scalar
grade projection for \(r_i^{[1/5]}\), and the baseline \(q_0^{(0..9)}(m)\)
jets.  This task audits only the second blocker.

Delta: this audit confirms that \(q_0\) is a source-named baseline object, but
only at the level of definitions and scale estimates.  The exact baseline
coefficient theorem is still missing, sharpened to ten midpoint derivatives or
an explicit reduction of those derivatives to named baseline objects.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/skills/research-resume/SKILL.md` - read
  because this is a resumed UV-026 research lane.
- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read before
  acting.
- Current repository head while auditing:
  `2e29dc0 capture UV-026 scalar grade reduction`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 immediate source-jet subtarget.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:157-160` - \(q=\Phi'\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:249-253` - \(q_\pm\) and
  \(\Delta_m\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:273-283` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:323-327` - zeta-side split and
  jet-corrected phase derivative.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:964-974` - \(q_0\) split and
  baseline same-point formula.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1149-1164` - \(q_0,\Phi_0\), and
  \(\Delta_0\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1332-1378` - baseline variation
  and local scales.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1760-1795` - baseline entry
  scales and first Frechet boundary.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - ordinary
  \(z\)/\(s=z/Q^2\), \(\mathfrak D_Q\), and transfer bounds.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md`
  - Stage 1 generator report.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json`
  - Stage 1 manifest.
- Own note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-verifier-source-UV026-baseline-q0-jets/notes/baseline-q0-jet-guardrails.md`.

# Dependencies

- Stage 1 generator's ordinary-\(z\), pre-\(\Phi_K\) normalization.
- A definition of \(q_0\) as a scalar germ at the midpoint \(m\).
- Exact baseline derivative formulas through order \(9\), or a theorem
  reducing them to \(q_{\loc}\), \(J_1[g_{\sm}]\), \(E_{\est}\), and any other
  named baseline pieces.
- A proof that any residual bookkeeping term included or omitted from \(q_0\)
  is treated correctly in \(B_7^{\mathfrak f}\) tables.

# Strongest objection

The phrase "baseline local-model-plus-affine-jet" may be intended to define
\(q_0\) implicitly, and the jet-corrected phase derivative
\(q_{\loc}+J_1[g_{\sm}]+E_{\est}\) gives a plausible reduction.  But the
inspected source does not turn that into the ten exact midpoint derivatives
needed by the generator, and scale estimates cannot be substituted for
coefficient tables.

# Needed for promotion

Add or cite a baseline \(q_0\)-jet theorem with these exact contents:

1. Define \(q_0(t)\) explicitly in the Stage 1 normalization, for example as
   \(q_{\loc}(t)+J_1[g_{\sm}](t)+E_{\est}(t)\), or state the exact alternative.
2. Give formulas for \(q_0^{(k)}(m)\), \(0\le k\le9\), in terms of named paper
   baseline objects.
3. Prove that substituting \(s=z/Q^2\) yields the ordinary-\(z\) generator
   inputs for \(G_\pm^{(0)}\), \(N_0\), and \(\Delta_0\).
4. State how \(E_{\est}\) participates in those coefficients, or prove why it
   is absent in the Stage 1 \(B_7^{\mathfrak f}\) normalization.
5. Keep this theorem independent of the scalar grade-projection theorem for
   \(r_i^{[1/5]}\).

# Autoresearch next step

continue: attack the baseline \(q_0\)-jet theorem directly.  First decide and
state the exact baseline germ \(q_0\) used by \(G_\pm^{(0)}\) and \(N^{(0)}\);
then compute or source \(q_0^{(0)},\ldots,q_0^{(9)}\) at \(m\) in the
ordinary-\(z\), pre-\(\Phi_K\) Stage 1 normalization.

# Ledger destination

`uv.md`, `findings.md`, and `attempts.md`: record this route as `keep`.  It
separates the baseline \(q_0\)-jet blocker from the scalar grade-projection
blocker and sharpens the missing UV-026 substatement to an exact ten-jet
baseline theorem.
