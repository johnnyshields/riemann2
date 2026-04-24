# Claim

The exact D-min-visible corrected odd-block functional is the package-fiber difference of the paper's corrected transverse scalar
\[
H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr),
\]
not a new cubic/quintic defect channel. For two corrected packages in the same corrected reduced-package fiber, define
\[
\mathscr H_{12}(t;s)
:=
\Phi_K\!\left(
\widehat\Omega^{\corr}_{\mathcal P_1(t)}(s)-
\widehat\Omega^{\corr}_{\mathcal P_2(t)}(s)
\right).
\]
Its first D-min-visible odd block is
\[
\mathscr O_D^{(N)}(t)
:=
\Phi_K\!\left([s^{2N-1}]
(\widehat\Omega^{\corr}_{\mathcal P_1(t)}-
 \widehat\Omega^{\corr}_{\mathcal P_2(t)})
\right),
\]
where \(2N-1\) is the first surviving odd order; equivalently one can use the transformed scalar
\[
\mathscr X_D^{(N)}(t):=
\sum_{j=1}^N a_j^{(N)}\mathscr H_{12}(t;s_j),
\]
because the paper's exact odd-tail expansion makes its leading term the same first surviving corrected odd coefficient.

Corrected-whitening analyticity proves that this functional is analytic in the corrected block perturbation triple. It does **not** prove that the functional is state-local in the fixed-shear descended transport state. The minimal missing theorem is therefore a finite descended affine-bundle transport/holonomy lemma: after fixing the corrected reduced-package fiber and normalized septic lift, all remaining package variation contributes to \(\mathscr O_D^{(N)}\) only through \(\ker\Phi_K\) up to order \(2N-1\).

# Status

open

# Evidence

- The paper defines the transform-level corrected odd scalar as
  \[
  H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr)
  \]
  and states that the leading value channel is annihilated by \(\Phi_K\), leaving curvature, tail, and corrected finite-\(s\) remainder channels.
- Corrected finite-\(s\) holomorphic whitening proves holomorphy of
  \[
  \widehat\Omega_\zeta^{\corr}(s;m)
  =G_{m,-}^{\corr}(s)^{-1/2}N_m^{\corr}(s)G_{m,+}^{\corr}(s)^{-1/2}.
  \]
  Therefore any package-fiber difference of corrected whitened blocks is holomorphic where the packages supply holomorphic corrected block data.
- The uniform scaled corrected-whitening transfer defines an analytic functional
  \[
  \mathcal T_{Q,R}(X)(w)
  =\frac{Q}{Rw}\Phi_K\!\left(
  \mathcal W(G^{(0)}_-+\delta G_-,N^{(0)}+\delta N,G^{(0)}_++\delta G_+)
  -\mathcal W(G^{(0)}_-,N^{(0)},G^{(0)}_+)
  \right)
  \]
  with an absolutely convergent homogeneous expansion and coefficient bounds. This is the analytic engine behind \(\mathscr H_{12}\), but it is an analytic dependence statement, not a state-locality theorem.
- The odd expansion gives
  \[
  H_m(z/Q^2)=\sum_{r\ge0}c_{2r+1}(m)\frac{z^{2r+1}}{Q^{2r+4}}.
  \]
  The corrected \(N\)-point scalar
  \[
  \Xi_\zeta^{(N)}(m)=\sum_{j=1}^Na_j^{(N)}H_m(s_j)
  \]
  has the exact surviving expansion whose leading term is the first surviving corrected odd coefficient \(c_{2N-1}(m)\). Thus \(\mathscr X_D^{(N)}\) is the transformed version of \(\mathscr O_D^{(N)}\), not a separate object.
- The fixed-shear state-locality proposition has the schematic mechanism needed for D-min: if a diagonal-vanishing analytic functional factors through the descended even transport state \(\mathcal T_N(t)\), then it is \(O(t^2)\). Replacing \(E_{12}^{(3)},E_{12}^{(5)}\) by \(\mathscr O_D^{(N)}\) would give the D-min bridge **conditional on** a new state-locality statement for the actual corrected package-to-transform map.
- The paper explicitly records the limitation: the actual corrected two-pair defect/package is not proved to be state-local in the descended transport state. It also says any remaining obstruction must be genuinely relational/provenance-sensitive or non-finite-order.
- The affine-lift/septic evidence explains why this new lemma is necessary. On \(\{c\neq0,v_5\neq0\}\), equal reduced data leave a visible local septic lift coordinate \(T=v_7/c\); source audit forbids treating \(T\) as canonical global package data. Hence the theorem-level claim must be modulo \(\ker\Phi_K\) for the transform-level block, not equality of raw septic representatives.

# Baseline / delta

Baseline: the prior D-kerphik report reduced D-min on the \(v_5\neq0\) patch to one local visible septic proxy \(T=v_7/c\), then warned that D remains transform-level and global modulo \(\ker\Phi_K\). The hidden-state geometry explorer reframed this as affine-bundle descent of the septic lift line. Verifiers objected that \(T\) is not canonical global package data and that the fixed-shear state-locality proposition is only conditional for cubic/quintic defects.

Delta: this report identifies the replacement functional requested in the brief: \(\mathscr O_D^{(N)}\), the first \(\Phi_K\)-visible odd coefficient of the corrected whitened-block difference, or equivalently \(\mathscr X_D^{(N)}\), its \(N\)-point transformed scalar. It also separates what corrected-whitening analyticity proves from what is missing: analyticity of the functional is proved; finite descended state-locality/holonomy is missing.

# Attempt status

keep

# Exact refs

- `rh/proof_of_rh.tex:406-415` — definition of \(\Phi_K\).
- `rh/proof_of_rh.tex:1392-1458` — corrected finite-\(s\) holomorphic whitening for \(\widehat\Omega_\zeta^{\corr}\).
- `rh/proof_of_rh.tex:1497-1566` — corrected local deformation and internal full corrected scalar \(H_{m,R}\).
- `rh/proof_of_rh.tex:1693-1754` — whitened mixed-block transfer after applying \(\Phi_K\).
- `rh/proof_of_rh.tex:2214-2322` — definition of \(H_m\), oddness, and odd expansion.
- `rh/proof_of_rh.tex:2415-2595` — analytic corrected-whitening transfer map \(\mathcal T_{Q,R}\) and coefficient bounds.
- `rh/proof_of_rh.tex:2953-2969` — core localization of the extracted odd jet.
- `rh/proof_of_rh.tex:3978-4037` — exact surviving expansion for \(\Xi_\zeta^{(N)}\) and leading corrected odd coefficient.
- `rh/proof_of_rh.tex:22302-22407` — finite transport-jet quotient descent and no third reset.
- `rh/proof_of_rh.tex:22409-22470` — conditional state-local defect closure for \(E_{12}^{(3)},E_{12}^{(5)}\).
- `rh/proof_of_rh.tex:22472-22619` — stronger conditional package collapse and explicit limitation that actual package state-locality is not proved.
- `rh/proof_of_rh.tex:23072-23109` — residual fixed-shear corner as package-level/no-hidden-reset problem.
- `rh/proof_of_rh.tex:7004-7190`, `7892-8033`, `12777-12792` — fixed-sector quintic/septic package, gauge line, local septic lift coordinates.
- `rh/proof_of_rh.tex:21142-21253` — same-tower closure and best current rank-two coupling; no second primitive pointwise highest-new generator in the current explicit package.
- Prior reports/notes: `agents/20260424-145500-gap-closer-D-kerphik/report.md`, `agents/20260424-145500-gap-closer-D-kerphik/notes/followup-Dmin-state-locality-axiom.md`, `agents/20260424-145500-explorer-hidden-state-geometry/report.md`, `agents/20260424-145500-explorer-hidden-state-geometry/notes/fixed-shear-state-locality-bridge.md`, `agents/20260424-145500-explorer-hidden-state-geometry/notes/state-locality-audit.md`, `agents/20260424-145500-verifier-source-C-D/report.md`, `agents/20260424-145500-verifier-adversarial-C-D/report.md`.
- This agent note: `agents/20260424-160000-gap-closer-D-odd-block-state/notes/odd-block-functional.md`.
- UV targets: UV-002 / `rem:wip-pairlike-finitecore`; UV-004 / `rem:wip-explicit-pointwise-bridge-good-patch-detector`; UV-007 / `rem:wip-final-endgame-status`.

# Dependencies

- Bottleneck C or an equivalent definition of corrected reduced-package fibers.
- The existing \(\Phi_K\), corrected whitening, odd expansion, and \(N\)-point extraction machinery.
- The local affine-lift reduction on good patches only as a diagnostic; theorem-level D must be transform-level modulo \(\ker\Phi_K\).
- A new state-locality/holonomy lemma for the actual corrected package-to-transform map.

# Strongest objection

The proposed \(\mathscr O_D^{(N)}\) is a clean transform-level functional, but this report does not prove it factors through the descended fixed-shear transport state or the corrected reduced-package fiber. Corrected-whitening analyticity only says the functional is analytic in the block inputs; an analytic function may still depend on a genuinely relational/provenance-sensitive hidden variable not encoded in \(\mathcal T_N\) or the normalized septic lift. Also, \(N\) is itself the first surviving odd order; without a package-to-transform theorem, higher odd-order leakage can survive even if the septic proxy is fixed.

# Needed for promotion

1. State and prove the D-min state-locality lemma:
   \[
   \mathscr O_D^{(N)}(t)=\mathfrak o_D(\mathcal T_M(t),L(t)),
   \qquad
   \mathfrak o_D(\mathcal T_M(0),L(0))=0,
   \]
   where \(L\) is the normalized septic affine-lift data and all remaining lift variation is interpreted modulo \(\ker\Phi_K\).
2. Prove the affine-bundle transport/holonomy assertion that along corrected reduced-package fibers, changes of lift or higher package memory map into \(\ker\Phi_K+O(s^{2N+1})\) in the corrected whitened block.
3. Check patch transitions between \(v_5\neq0\) and \(u_5\neq0\) so the statement does not promote \(T=v_7/c\) to global data.
4. Have source/adversarial verifiers check that the proof is transform-level and does not merely repackage the conditional cubic/quintic defect proposition.

Honest verdict: the replacement odd-block functional is identified, but D is not closed. The paper already supplies the analytic transform-level object \(H_m\), its coefficient extractor, and the fixed-shear state-locality mechanism. The missing bridge is precisely that the first \(\Phi_K\)-visible odd coefficient of a corrected package-fiber difference is state-local in the descended transport state plus affine lift, with all remaining affine-bundle holonomy invisible modulo \(\ker\Phi_K\). That is a sharper gap, not a proof.

# Autoresearch next step

continue: attack the affine-bundle transport/holonomy lemma directly by tracing the corrected block perturbation triple \((\delta G_-,\delta N,\delta G_+)\) through the local lift transition and identifying the first term that could depend on relational/provenance-sensitive data.

verify: ask source/adversarial verifiers to check whether \(\mathscr O_D^{(N)}\) as defined here is already legitimate notation from existing \(H_m\)/\(\Xi_\zeta^{(N)}\) machinery, and whether the proposed state-locality lemma is weaker than full package collapse.

blocked: no coordinator action needed unless the next step requires a broader search for actual formulas for the corrected two-pair block perturbation triple.

terminal: not terminal; D-min remains open with the minimal missing transport/holonomy lemma isolated.
