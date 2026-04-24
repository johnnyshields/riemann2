Claim

Fifth follow-up attack on Bottleneck C: the patch-transition problem for the local affine lift coordinate is not itself the hidden obstruction. On the two canonical good-patch gauges one has local section values
\[
S:=\frac{\lambda}{c}=\frac{\Delta_7}{c v_5}
\qquad (v_5\neq 0),
\]
and
\[
S_u:=-\frac{\Delta_7}{c u_5}
\qquad (u_5\neq 0).
\]
On the overlap \(u_5v_5\neq 0\), these satisfy
\[
S_u=-\frac{v_5}{u_5}S=-\frac{x}{Y}S,
\qquad
Y=\frac{u_5}{c},\ x=\frac{v_5}{c}.
\]
Equivalently, the overlap scalar
\[
\tau:=\frac{\Delta_7}{u_5v_5}=\frac{\Delta_7/c^2}{(u_5/c)(v_5/c)}
\]
is already determined by the reduced datum
\[
\widehat\Psi=\left(\frac{u_5}{c},\frac{v_5}{c},\frac{\Delta_7}{c^2}\right).
\]
So the patch cocycle of the one-dimensional affine lift coordinate is controlled by reduced-package data and is **not** an additional hidden state.

This sharpens the current reduction of C once more. The hidden obstruction is not patching of the local lift coordinate; it is the unresolved choice of a point in the affine fiber itself. Therefore the best present theorem shape for C is:

- base data = descended quotient-visible collision state together with reduced package data \(\widehat\Psi\);
- residual fiber = a one-dimensional affine septic-lift coordinate whose transition law is already determined by the base;
- Bottleneck C must canonically select or collapse that affine fiber at coincidence, thereby forcing
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
  \]

So after this pass, the cleanest target is not “patch the local lift coordinate globally,” but “prove that diagonal merger canonically fixes the affine septic-lift fiber over the reduced base.”

Status

open

Evidence

The fixed-shear package still provides the ceiling: from that tested scope alone, no extra finite quotient-visible transport scalar or finite hidden reset survives. So if C remains open, the obstruction must live in extra package-side fiber data, not in another transport invariant.

The local septic gauge-fixing remarks give two canonical local sections of the affine line of raw septic representatives. On \(v_5\neq 0\), one sets \(v_7^{\new}=0\) and gets \(u_7^{\new}=\Delta_7/v_5\). On \(u_5\neq 0\), one sets \(u_7^{\new}=0\) and gets \(v_7^{\new}=-\Delta_7/u_5\). Dividing by \(c\) gives the two local section values above.

Now the key new point: their overlap relation depends only on reduced package coordinates. Since
\[
S=\frac{\Delta_7}{c v_5},\qquad Y=\frac{u_5}{c},\qquad x=\frac{v_5}{c},
\]
one has
\[
S_u=-\frac{\Delta_7}{c u_5}=-\frac{x}{Y}S,
\]
and the overlap scalar
\[
\tau=\frac{\Delta_7}{u_5v_5}=\frac{\Delta_7/c^2}{(u_5/c)(v_5/c)}
\]
is a function of \(\widehat\Psi\) alone. So the cocycle for changing local section is already visible in the reduced base. This means the cocycle itself is not the hidden state. What remains hidden is which point of the affine fiber the actual corrected two-atom package chooses on the exceptional divisor.

That makes the theorem target more precise than before. The affine-bundle picture remains right, but the hard part is no longer transition control; it is diagonal fiber-collapse / canonical section selection at coincidence.

Exact refs

- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:7992-8033` — affine line of raw septic representatives and the two local gauge-fixing sections.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:8414-8429` — definition of `\lambda=\Delta_7/v_5` on `v_5\neq 0`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:10790-10844` — order-7 target is provenance-sensitive; quotient-septic closure remains locally free.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:11368-11408` — reduced datum `\widehat\Psi`.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:22380-22618` — quotient-visible finite transport state exhausted on the tested fixed-shear scope.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:23098-23108` — residual exact fixed-shear corner reduced to package-level collapse / no-hidden-reset question.
- `/mnt/c/workspace/riemann2/rh/proof_of_rh.tex:24380-24385` — good `v_5`-patch reduced coordinates `Y=u_5/c`, `x=v_5/c`, `S=\Delta_7/(c v_5)`.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-explorer-hidden-state-geometry/notes/transport-formulations.md:1-60` — affine-line/lift geometry and overlap cocycle `-\Delta_7/(u_5v_5)`.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:63-65` — affine lift-coordinate interpretation.
- `/mnt/c/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-gap-closer-C-diagonal-merger/notes/20260424-followup-patch-transition-controlled.md` — present calculation that the cocycle is reduced-data-controlled.
- UV refs: `UV-002`, `UV-003`, `UV-007`; labels `rem:wip-pairlike-finitecore`, `rem:wip-parity-projective-factorization-collision-blow-up`, `rem:wip-final-endgame-status`.

Dependencies

- The quotient-visible/state-local ceiling from the fixed-shear package analysis.
- The affine-line interpretation of raw septic representatives over the reduced package base.
- A corrected two-atom theorem showing that the exceptional-divisor package really is an affine fiber over the reduced base with this local model.
- A diagonal-merger theorem canonically selecting the fiber point at coincidence.

Strongest objection

The new calculation is still derived from one-pair local gauge sections, not from a constructed corrected two-atom exceptional-divisor object. So it proves only that the candidate local cocycle is base-controlled in the one-pair model. The actual corrected two-atom package might still carry extra hidden dependence that is invisible in this local affine-lift picture.

Needed for promotion

- Construct or isolate the corrected two-atom exceptional-divisor state as an affine fiber over the reduced base, with local sections modeled by the current septic gauge-fixing formulas.
- Prove that no extra package-side datum survives beyond this affine fiber.
- Prove diagonal merger / collision-functoriality canonically selects the fiber point at coincidence.
- Conclude the exceptional-divisor trace is unique:
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
  \]

Honest verdict: I still do not see a proof of C. But the hidden structure is now cleaner. The patch-transition scalar for the local lift coordinate is already controlled by reduced data \(\widehat\Psi\), so patching is not the real gap. The real remaining theorem is fiber selection: prove the actual corrected two-atom package has only this one-dimensional affine lift freedom over the reduced base, and that diagonal merger kills it.

Autoresearch next step

- continue: attack the final remaining issue in this local model — whether the actual corrected two-atom exceptional-divisor package can be shown to have only a one-dimensional affine fiber over the reduced base, with no further hidden package datum.
- verify: adversarially test whether the local affine-lift picture misses any extra two-atom datum not visible in the one-pair septic gauge model.
- blocked: coordinator may want the package-functoriality explorer to cross-check whether prior chats already identified a secant-shadow / collision state whose fiber over `\widehat\Psi` is exactly affine one-dimensional.
- terminal: not terminal; the next concrete move is to test whether the affine fiber is the whole hidden state.