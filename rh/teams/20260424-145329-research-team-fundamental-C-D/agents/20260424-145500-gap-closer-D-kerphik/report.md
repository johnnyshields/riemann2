# Claim

Bottleneck D does not close from equal corrected reduced-package fibers alone on the present draft, but the remaining gap is now sharply reduced in two stages.

First, on the quintic-good patch \(\{c\neq 0,\ v_5\neq 0\}\), after Bottleneck C, equality of
\[
\widehat\Psi=(Y,x,\Delta),\qquad Y=\frac{u_5}{c},\ x=\frac{v_5}{c},\ \Delta=\frac{\Delta_7}{c^2},
\]
leaves exactly one uncontrolled \(\Phi_K\)-visible scalar,
\[
T:=\frac{v_7}{c}.
\]
Equivalently, on that patch the raw septic fixed-sector pair is recovered from \((\widehat\Psi,T)\) by
\[
\frac{u_7}{c}=\frac{\Delta+YT}{x}=S+\frac{YT}{x},
\qquad
\frac{v_7}{c}=T,
\qquad
S:=\frac{\Delta_7}{cv_5}=\frac{\Delta}{x}.
\]

Second, from the current draft alone this is **not** a missing pointwise highest-new scalar problem above normalized septic data. Same-tower closure rules out any second currently explicit local pointwise highest-new generator beyond the affine lift-coordinate \(T\). Therefore any still-live failure of D-min must be genuinely relational / transport-level / provenance-sensitive.

The smallest theorem-shaped bridge now visible is the state-locality axiom:

> **SL\(_{\mathrm D}\)** The \(\Phi_K\)-visible corrected odd block, equivalently the first surviving odd jet modulo \(\ker\Phi_K\), is an analytic functional of a finite descended quotient-visible transport state together with the normalized septic lift, and vanishes on the diagonal.

So the hidden-state theorem D reduces to one concrete unresolved statement: prove that equal corrected reduced-package fibers force equality of \(T\) through the first surviving odd order, or at least force the induced odd corrected-block difference to lie in \(\ker\Phi_K=\mathbf C I\oplus\mathbf C D\oplus\mathbf C K\); and the cleanest currently visible route is the state-locality bridge above, not a new local generator identity.

# Status

open

# Evidence

- \(\Phi_K(X)=x_{12}+x_{21}\) is the symmetric off-diagonal functional, so in the basis
  \[
  I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
  D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
  S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
  K=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
  \]
  one has \(\Phi_K(I)=\Phi_K(D)=\Phi_K(K)=0\) and \(\Phi_K(S)=2\). Hence
  \[
  \ker\Phi_K=\mathbf C I\oplus \mathbf C D\oplus \mathbf C K.
  \]
- The fixed-sector quintic/septic package is
  \[
  A_5^{\mathfrak f}=u_5I+v_5S,
  \qquad
  A_7^{\mathfrak f}=u_7I+v_7S,
  \qquad
  \Delta_7=u_7v_5-u_5v_7.
  \]
  The quotient-level invariant \(\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)\) forgets the raw septic representative modulo the gauge line \(\mathbf C A_5^{\mathfrak f}\).
- Write
  \[
  Y:=\frac{u_5}{c},\qquad x:=\frac{v_5}{c},\qquad U:=\frac{u_7}{c},\qquad T:=\frac{v_7}{c},\qquad \Delta:=\frac{\Delta_7}{c^2}.
  \]
  Then the determinant identity becomes
  \[
  \Delta=Ux-YT.
  \]
  Therefore, on \(x\neq 0\),
  \[
  U=\frac{\Delta+YT}{x}.
  \]
  So after fixing \(\widehat\Psi=(Y,x,\Delta)\), the entire remaining raw septic freedom is exactly the one scalar \(T=v_7/c\).
- This matches the projected septic gauge law
  \[
  A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f},
  \]
  because dividing by \(c\) gives
  \[
  (U,T)\mapsto (U,T)+\chi (Y,x),
  \]
  so the residual raw fiber over fixed \(\widehat\Psi\) is one-dimensional. Its \(\Phi_K\)-visible part is exactly the \(S\)-coefficient, i.e. the change in \(T\), since
  \[
  \Phi_K\!\left(\frac{A_7^{\mathfrak f}}{c}\right)=2T.
  \]
- Same-tower closure then sharpens the interpretation of this fiber. For the **current explicit pointwise package** on a good overlap patch, every currently explicit highest-new field lies in one source tower over
  \[
  r=q^{(7)},
  \]
  and no second primitive pointwise highest-new generator appears. So from the tested scope of the current explicit package formulas, D-min is no longer a missing local pointwise visible scalar problem beyond the affine lift-coordinate.
- The exact fixed-shear corner package sharpens the remaining obstruction further. The draft proves a conditional state-local defect closure statement: if the corrected cubic/quintic defects factor analytically through a finite descended transport state
  \[
  \mathcal T_N(t)=\bigl(\Theta_0(t),\dots,\Theta_N(t)\bigr)
  \]
  and vanish on the diagonal state, then evenness of the descended transport jet forces
  \[
  E_{12}^{(3)}(t)=O(t^2),\qquad E_{12}^{(5)}(t)=O(t^2),
  \]
  excluding the residual involutive bad branch on a compact good patch.
- The stronger package-collapse corollary adds the natural merger law and makes the interaction remainder vanish identically, but the remarks immediately after it say that any still-live obstruction is genuinely relational / provenance-sensitive or non-finite-order. So merger is an upgrade, not the minimal bridge.
- Combining the previous two bullets with the one-dimensional septic reduction gives the current clean D-min reformulation: equal reduced-package fibers leave one visible affine lift-coordinate \(T\), same-tower closure rules out a second explicit local pointwise source, and the smallest remaining theorem-shaped target is state-locality of the D-min-visible corrected odd block in finite descended transport state plus normalized septic lift.
- Once that state-locality bridge is proved, the existing odd-jet machinery already identifies the first surviving odd coefficient of
  \[
  H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))
  \]
  and hence the first nonzero transformed scalar \(\Xi_{\zeta,\le H}^{(N)}\).
- What is still missing is the comparison step: the fixed-shear conditional proposition is written for cubic/quintic defect channels, not yet for the transform-level \(\Phi_K\)-visible odd block itself. So the last unresolved translation is to identify the exact D-min-visible odd-block functional that belongs to this state-local framework.

# Exact refs

- `rh/proof_of_rh.tex:406-415` — definition of \(\Phi_K\).
- `rh/proof_of_rh.tex:6981-7059` — basis \((I,S,D,J)\), fixed-sector package, quotient-level septic datum.
- `rh/proof_of_rh.tex:7065-7190` — projected septic gauge law and gauge invariance of \(\Delta_7\).
- `rh/proof_of_rh.tex:7892-8033` — quotient-septic closure and local gauge-fixing of raw septic representatives.
- `rh/proof_of_rh.tex:11399-11408` — invariant \(\widehat\Psi=(u_5/c,v_5/c,\Delta_7/c^2)\).
- `rh/proof_of_rh.tex:12777-12792` — local coordinates \(Y=u_5/c\), \(x=v_5/c\), \(S=\Delta_7/(cv_5)\) on a \(v_5\)-patch.
- `rh/proof_of_rh.tex:21142-21217` — same-tower closure for the current explicit highest-new overlap/canonical package.
- `rh/proof_of_rh.tex:21219-21253` — rank-two coupling still same-tower over \(r=q^{(7)}\).
- `rh/proof_of_rh.tex:2214-2307` — corrected odd scalar \(H_m\) and odd Taylor coefficients.
- `rh/proof_of_rh.tex:22303-22407` — finite transport-jet quotient descent and rank-one quotient-visible transport state.
- `rh/proof_of_rh.tex:22409-22470` — conditional state-local defect closure from factorization through \(\mathcal T_N\).
- `rh/proof_of_rh.tex:22472-22505` — stronger package collapse when state-locality and merger law both hold.
- `rh/proof_of_rh.tex:22507-22619` — remarks isolating the remaining residual obstruction as relational / provenance-sensitive.
- `rh/proof_of_rh.tex:23072-23109` — package-level reduction and the no-hidden-reset / package-level formulation of the residual fixed-shear corner.
- `rh/proof_of_rh.tex:23123-23155` — coefficient-extraction basis \((I,D,S,K)\).
- `rh/proof_of_rh.tex:2953-2969` — finite-core localization of the first surviving odd coefficient.
- `rh/proof_of_rh.tex:3984-4190` — exact surviving expansion and finite-core localization of \(\Xi_\zeta^{(N)}\).
- Prior notes in this agent dir:
  - `notes/followup-finite-determination.md`
  - `notes/followup-Dmin-sametower-reduction.md`
  - `notes/followup-Dmin-state-locality-axiom.md`
- Prior cycle theorem-shaping: `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/20260424-145000-kerphik-hidden-state/report.md` and `rh/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:120-169`.

# Dependencies

- Bottleneck C in the sharp form \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)\).
- Work on a quintic-good patch \(\{c\neq 0,\ v_5\neq 0\}\) for the explicit scalar reduction above; a parallel \(u_5\neq 0\) version should exist with roles swapped.
- Existing zeta-side extractor and finite-core localization for \(H_m\) and \(\Xi_{\zeta,\le H}^{(N)}\).

# Strongest objection

The reduction above is still patchwise and algebraic. It does **not** prove that the actual corrected coincidence package controls \(T=v_7/c\), and it does not show that the first surviving odd corrected block depends only on the order-7 raw fixed-sector representative. Higher odd orders could carry additional hidden \(\Phi_K\)-visible state unless one proves a full inductive package-to-transform theorem, not just the septic reduction.

# Needed for promotion

1. Prove the package-side hidden-state lemma on corrected reduced-package fibers:
   \[
   \mathcal P_1\sim \mathcal P_2
   \Longrightarrow
   \Delta\widehat\Omega^{\corr}(s)\in \ker\Phi_K+O(s^{2N+1})
   \]
   through the first surviving odd order \(2N-1\).
2. Minimal finite reduction of that lemma: on \(\{v_5\neq 0\}\), prove equal corrected reduced-package fibers force equality of the single visible hidden scalar \(T=v_7/c\) through order \(2N-1\); equivalently, prove the raw-to-reduced quotient forgets only \(\Phi_K\)-invisible directions.
3. Check the complementary \(u_5\neq 0\) patch and the transition across \(v_5=0\) so the one-dimensional reduction is canonical rather than chart-dependent.
4. Then invoke the existing odd-jet extractor to conclude that the minimal \(N\) with nonzero \(\Xi_{\zeta,\le H}^{(N)}\), and its leading value, are package-determined.

Honest verdict: I did not prove Bottleneck D. I did sharpen it to a concrete finite reduction: after C, the corrected reduced package leaves exactly one visible hidden scalar on a \(v_5\)-patch, namely \(T=v_7/c\). Same-tower closure then removes the possibility that the missing theorem is another currently explicit local pointwise highest-new scalar, and the exact fixed-shear corner package isolates the smallest theorem-shaped next target as state-locality of the D-min-visible odd block in descended transport state. So D is no longer a vague hidden-state problem; it is the problem of killing that one scalar, and then extending the result from the patchwise septic model to the first surviving odd order by the state-locality bridge.

# Autoresearch next step

- continue: identify the exact D-min-visible corrected odd-block functional that should replace the cubic/quintic defect channels in the fixed-shear state-locality proposition, and test whether corrected-whitening analyticity puts it in the same finite descended transport-state framework.
- verify: have the source/adversarial verifier check whether the fixed-shear conditional propositions can legitimately be repurposed for the transform-level \(\Phi_K\)-visible odd block, or whether they are confined to cubic/quintic defect channels only.
- blocked: coordinator intervention is only needed if this comparison requires a broader cross-cycle search for an already-written package-to-odd-block identification theorem.
- terminal: not terminal; the deposit now records the final sharp reduction of D-min to the state-locality bridge and the remaining comparison step.