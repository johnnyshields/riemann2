# Report: UV-010 quotient geometry

## Claim

On the constant-rank patch
\[
A_5^{\mathfrak f}(m)\neq0,
\]
UV-010 does not need an arbitrary complement choice or a projectivized
convention to compare the moving \(h_1\)-quotient with the midpoint quotient.
The determinant pairing gives a canonical analytic trivialization:
\[
\tau_h:\mathfrak f/\mathbf C A_5^{\mathfrak f}(h)\to\mathbf C,
\qquad
\tau_h([R])=\det(R,A_5^{\mathfrak f}(h)).
\]
Thus
\[
T_{h_1\to m}:=\tau_m^{-1}\circ\tau_{h_1}
\]
is a canonical moving-line-to-midpoint quotient identification on
\(A_5^{\mathfrak f}(h_1)\neq0\), \(A_5^{\mathfrak f}(m)\neq0\). This gives the
clean local geometry needed by UV-010.

At \(A_5^{\mathfrak f}=0\), the quotient dimension jumps. A
projectivized/blow-up convention is needed only if the paper wants UV-010 to
cross that exceptional locus; otherwise the correct theorem should be stated on
the constant-rank good patch.

## Status

proved

This proves a local quotient-geometry lemma and a precise obstruction list. It
does not construct the actual order-7 edge package \(\mathcal H_7^q\), so
UV-010 remains open.

## Evidence

The paper defines
\[
\mathfrak f=\operatorname{span}\{I,S\}
\]
and writes
\[
A_5^{\mathfrak f}=u_5I+v_5S,\qquad
A_7^{\mathfrak f}=u_7I+v_7S
\]
at `rh/proof_of_rh.tex:6976-7022`. It identifies the canonical order-7 content
as
\[
[A_7^{\mathfrak f}]\in\mathfrak f/\mathbf C A_5^{\mathfrak f}
\]
or equivalently the determinant
\[
\Delta_7=u_7v_5-u_5v_7
\]
at `rh/proof_of_rh.tex:7046-7059`, and proves the septic gauge law
\[
(A_7^{\mathfrak f})^{\new}=A_7^{\mathfrak f}+c_2A_5^{\mathfrak f}
\]
at `rh/proof_of_rh.tex:7065-7191`.

The quotient-septic closure theorem later confirms that the raw representative
is irrelevant: the class \([A_7^{\mathfrak f}]\) equals the direct
\(K_1\)-class in \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\), and
\(\Delta_7=\Delta_{7,K_1}\). Refs: `rh/proof_of_rh.tex:7540-7974` and
`rh/proof_of_rh.tex:7980-8001`.

The two-pair theorem uses the moving \(h_1\)-quotient:
\[
a_1[A_{7,1}^{\mathfrak f}]+a_2[A_{7,2}^{\mathfrak f}]
+\overline E_{12}^{(7;1)}=0
\quad\text{in}\quad
\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f},
\]
then chooses \(R\) as a representative of
\(-a_1^{-1}\overline E_{12}^{(7;1)}\). Refs:
`rh/proof_of_rh.tex:11587-11775`. The paper only identifies a common quotient
line after a strong quintic identity at `rh/proof_of_rh.tex:11491-11499`; it
does not give a general midpoint trivialization there.

The determinant pairing supplies that missing local geometry on good patches.
For \(A=uI+vS\neq0\) and \(R=r_uI+r_vS\),
\[
\det(R,A)=r_uv-ur_v.
\]
The kernel of \(R\mapsto\det(R,A)\) is exactly \(\mathbf C A\). Hence the map
descends to an isomorphism
\[
\mathfrak f/\mathbf C A\simeq\mathbf C.
\]
On \(u\neq0\), scalar \(s\) is represented by \(R=-sS/u\). On \(v\neq0\), it is
represented by \(R=sI/v\). On the overlap these representatives differ by a
multiple of \(A\), so the class is independent of complement choice.

I checked the patch formulas and rank jump in
`rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-173642-explorer-UV010-quotient-geometry/scripts/quotient_trivialization_check.js`.
Git object: `122896d2615392e084288979b2ec5f7df7b46f98`.
Output excerpt:

```text
sample_0_source_scalar = 53
sample_0_midpoint_u_lift_scalar = 53
sample_0_midpoint_v_lift_scalar = 53
sample_0_patch_difference_is_gauge = true
sample_0_source_gauge_invariant = true
sample_1_source_scalar = -28
sample_1_midpoint_u_lift_scalar = -28
sample_1_midpoint_v_lift_scalar = -28
sample_1_patch_difference_is_gauge = true
sample_1_source_gauge_invariant = true
exceptional_determinant_map_rank = 0
exceptional_quotient_dimension_without_line_convention = 2
```

Three-bin separation:

- proved: on \(A_5^{\mathfrak f}\neq0\), the determinant pairing canonically
  trivializes \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\) and gives the
  moving-to-midpoint quotient identification.
- conditional: if the actual finite-delta septic defect is an analytic section
  of the moving quotient and vanishes to order \(\delta^2\) in the collision
  chart, the determinant trivialization converts it into a midpoint-valued
  analytic \(\mathcal H_7^q\).
- missing: the draft does not construct the actual order-7 quotient defect,
  prove its \(\delta^2\) edge law, or define a convention across
  \(A_5^{\mathfrak f}=0\).

## Baseline / delta

Baseline: the prior determinant-control report proved that
\[
[R]\mapsto \det(R,A_5^{\mathfrak f})
\]
is the whole one-dimensional quotient-defect class on
\(A_5^{\mathfrak f}\neq0\). The source audit then filed UV-010 because the
paper lacks \(\mathcal H_7^q\), the midpoint quotient trivialization, and the
exceptional \(A_5^{\mathfrak f}=0\) convention.

Delta: this report separates those issues. The midpoint trivialization is not a
missing theorem on constant-rank patches; it follows from the determinant
pairing. The missing geometry is exactly the exceptional rank-jump convention,
and the missing analysis remains the actual order-7 edge law. This narrows
UV-010 to:
\[
\text{actual septic quotient edge section on }A_5^{\mathfrak f}\neq0,
\]
plus a separately stated choice to either exclude or blow up the
\(A_5^{\mathfrak f}=0\) locus.

## Attempt status

keep

## Exact refs

- `C:/workspace/riemann2/CLAUDE.md` and
  `C:/workspace/riemann2/.agents/agents/_autoresearch.md` for
  writing discipline, provenance, and report requirements.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  for the current UV-010 frontier and C ordering.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md`
  under "Resume dispatch 20260424-173642" for the UV-010 target and non-goals.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  for the UV-010 entry.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md`
  for the determinant-slot reduction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-source-C-R-channel/report-UV010-source.md`
  for the source audit of UV-010.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md`
  for the finite-delta versus edge-class dependency graph.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report-edge-law-followup.md`
  for the septic Hessian obstruction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report-UV010-adversarial.md`
  for the formal \(a_1a_2\delta^2P(m,\kappa)\) pressure test.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7191` for
  \(\mathfrak f\), \(A_5^{\mathfrak f}\), \(A_7^{\mathfrak f}\),
  \(\Delta_7\), and the septic gauge law.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7540-7974` for quotient-septic
  closure and the \(K_1\) residual determinant.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7980-8001` for raw representative
  nonuniqueness versus quotient class and determinant.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11491-11499` for common quotient
  line identification only after the strong quintic identity.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` for the finite-delta
  septic quotient defect and representative \(R\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` for the conditional
  source criterion and abstract quadratic interaction remainder.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12584` for the collision
  chart, cubic/quintic edge template, and downstream package-theorem split.
- Note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-173642-explorer-UV010-quotient-geometry/notes/quotient-bundle-geometry.md`.
- Script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-173642-explorer-UV010-quotient-geometry/scripts/quotient_trivialization_check.js`.
  Git object: `122896d2615392e084288979b2ec5f7df7b46f98`.

## Dependencies

- Constant-rank patch \(A_5^{\mathfrak f}\neq0\), with \(h_1\) and \(m\) in
  that patch.
- The fixed basis \(I,S\) and determinant convention already used in the draft.
- A nonzero amplitude convention for turning
  \(\overline E_{12}^{(7;1)}\) into \(-a_1^{-1}\overline E_{12}^{(7;1)}\).
- An actual corrected order-7 quotient defect. The quotient geometry does not
  construct it.
- If the target is global across \(A_5^{\mathfrak f}=0\), an extra
  projectivized/blow-up line convention is required.

## Strongest objection

The determinant trivialization may look too coordinate-dependent because it
uses the basis \(I,S\). In this draft that is not a defect: the determinant
\(\Delta_7=u_7v_5-u_5v_7\) and the finite-delta formula for
\(\det(R,A_{5,1}^{\mathfrak f})\) already use the same fixed-sector
determinant convention. The real limitation is not coordinate dependence; it is
that the construction collapses at \(A_5^{\mathfrak f}=0\).

## Needed for promotion

1. State UV-010 on a constant-rank patch:
   \(A_5^{\mathfrak f}(m)\neq0\), with nearby \(h_1,h_2\) also in that patch.
2. Define the midpoint quotient target using
   \(T_{h_1\to m}=\tau_m^{-1}\circ\tau_{h_1}\).
3. Construct the actual corrected order-7 quotient defect
   \(\overline E_{12}^{(7;1)}\) as an analytic moving-quotient section.
4. Prove the edge law after midpoint trivialization:
   \[
   T_{h_1\to m}\bigl(\overline E_{12}^{(7;1)}\bigr)
   =
   \delta^2\mathcal H_7^q(m,\kappa,\delta^2).
   \]
5. State explicitly that \(\mathcal H_7^q\) may depend on \(\kappa\) and
   provenance; descent and diagonal merger are later theorems.
6. For \(A_5^{\mathfrak f}=0\), either exclude the locus from UV-010 or add a
   new projectivized/blow-up convention with a chosen limiting line
   \(\ell\in\mathbf P(\mathfrak f)\).

## Autoresearch next step

continue: hand this local lemma to the UV-010 theorem-formulation and
trivialization agents. The best next bounded task is to rewrite the UV-010
statement on \(A_5^{\mathfrak f}\neq0\) using
\(T_{h_1\to m}=\tau_m^{-1}\circ\tau_{h_1}\), then isolate the remaining
non-geometric missing input: actual analytic construction of
\(\overline E_{12}^{(7;1)}\).

verify: source verifier should check that the determinant convention matches
the paper's \(\Delta_7\) and \(R\)-determinant formulas. Adversarial verifier
should check that the theorem does not claim \(\kappa\)-independence or
descended state-locality.

blocked: no process blocker. Mathematical blocker is global treatment of
\(A_5^{\mathfrak f}=0\) if the coordinator wants UV-010 beyond constant-rank
patches.

terminal: terminal for the subroute "a complement or projectivized convention
is needed on \(A_5^{\mathfrak f}\neq0\)." It is not. Not terminal for UV-010,
because the actual order-7 edge defect is still missing.
