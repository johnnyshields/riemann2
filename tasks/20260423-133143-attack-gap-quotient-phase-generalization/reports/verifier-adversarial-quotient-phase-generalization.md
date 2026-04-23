Claim

Unimodularity of the completed quotient on the critical line is enough to revise the earlier Dirichlet and Ramanujan-\(\tau\) notes only at the boundary-phase level, not at the value-channel level.

More precisely, if
\[
\phi_F(s):=\frac{\Lambda_F(2s-1)}{\Lambda_F(2s)}
\]
for a completed \(L\)-function satisfying the standard functional equation and conjugation symmetry used in `gap-quotient-phase-routeA.md`, then on \(s=\tfrac12+it\) one gets a natural unimodular boundary phase object. From current scope alone, this supports only the following safe revisions.

1. Primitive Dirichlet: the single completed quotient is no longer only a bare reality candidate. Conditional on a source theorem identifying the manuscript phase with this quotient phase, it is a legitimate phase-channel candidate.
2. Ramanujan-\(\tau\): the quotient is an even cleaner phase-channel candidate because self-duality removes the \((\chi,\bar\chi)\)-type asymmetry.
3. Neither family gets a realized analogue of the manuscript's value-channel coefficient \(S(m)\), positivity of the background-subtracted scalar, corrected whitening, denominator comparability, or boundary hierarchy from unimodularity alone.

So the strongest safe Dirichlet/\(\tau\) statement now is:

- `[confirmed]` a completed quotient of the form \(\Lambda_F(2s-1)/\Lambda_F(2s)\) is the right phase object to try to realize, because on the critical line it is naturally \(U(1)\)-valued.
- `[conditional on a source theorem linking the manuscript phase to that quotient]` the single-channel Dirichlet route upgrades from `reality candidate` to `phase-channel candidate`.
- `[confirmed]` the scalar-amplitude problem remains open: no current argument shows that the induced background-subtracted quantity is the positive sign-compatible coefficient of the leading local value channel used in the manuscript.

Claims that need scoped weakening are exactly the ones that pass from `unimodular phase object` to `realized local package` or from `phase derivative exists` to `the right positive \(S(m)\)-analogue exists`.

Status

proved

Evidence

Proved.

The manuscript phase architecture uses only a real phase \(\Phi\) and its derivative \(q=\Phi'\) at the front end; see `paper/proof_of_rh.tex:149-159`. Separately, the manuscript's local contradiction uses the background-subtracted scalar
\[
q(t)=B_\zeta(t)+S(t),\qquad S(m)=q_\zeta(m)-B_\zeta(m),
\]
and then feeds \(S(m)\) into the leading value-channel deformation
\[
\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
\]
the calibration relation \(u^2\asymp (x/B)S(m)\), and the microscopic remainder/boundary bounds; see `paper/proof_of_rh.tex:273-287`, `748-778`, `1528-1566`, `2060-2087`, and `2218-2232`.

That separation is decisive. A quotient that is unimodular on \(\Re(s)=\tfrac12\) gives, at most, a natural boundary phase and hence a candidate source for \(q\). It does not by itself produce the manuscript's stronger value-channel package.

The archive note already points to the zeta quotient template
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},\qquad \phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
\]
and to an exact zero-kernel decomposition for the resulting phase derivative; see `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`. Route A correctly shows that the boundary identity
\[
\phi_F\!\left(\tfrac12+it\right)=\varepsilon_F\,\frac{\overline{\Lambda_F(1+2it)}}{\Lambda_F(1+2it)}
\]
forces \(|\phi_F(\tfrac12+it)|=1\) under the standard completed-\(L\) functional equation and conjugation package; see `gap-quotient-phase-routeA.md:21-48,56-100`. Route B correctly identifies the limitation: this is a `phase-channel upgrade only`, not a realized `S(m)A_{\val}` theorem; see `gap-quotient-phase-routeB.md:15-43,68-80`.

Therefore the earlier notes should be revised only as follows.

1. `notes/dirichlet_channel.md` should weaken `only a weaker reality candidate` to `phase-channel candidate conditional on a source theorem`, but it should keep the stronger scalar-amplitude caution. The note's present missing items remain missing: a realized local block, a real sign-compatible scalar amplitude replacing \(S(m)\), corrected whitening, denominator comparability, and boundary estimates; see `notes/dirichlet_channel.md:16-23,25-42,54-72`.
2. `notes/tau_localization.md` should sharpen `candidate object` to `phase object/source-split candidate`, but should keep the five degree-sensitive checkpoints unchanged; see `notes/tau_localization.md:18-21,23-35,36-50`.
3. `notes/scattering_generalization.md` should be read as already close to correct, but any phrase that can be heard as producing a positive scalar analogue from the quotient alone needs scope. The safe reading is `candidate-object sharpening` or `phase-channel upgrade only`; see `notes/scattering_generalization.md:39-58,69-79`.

Conditional on [a family-specific source theorem].

If one proves that the manuscript phase in a Dirichlet or \(\tau\) family is exactly the phase of the completed quotient, then the earlier boundary notes become sharper.

1. Primitive Dirichlet single-channel quotient: upgraded from a mere reality candidate to a genuine phase-channel candidate.
2. Ramanujan-\(\tau\): upgraded from a general completed-object candidate to a concrete self-dual phase-channel candidate.

But even under that extra hypothesis, the current record still does not show that the induced scalar after background subtraction is the right positive coefficient of the leading local value channel. That further step would require a realized zero/background decomposition in the family and the local package theorem, not just unimodularity.

Missing.

1. A source theorem proving that the manuscript phase \(\Phi\) in the target family is the phase of the completed quotient, with branch and normalization fixed.
2. A family-specific decomposition identifying the analogue of \(S(m)\) as a positive sign-compatible coefficient of the leading value channel, not merely as a formal derivative minus background subtraction.
3. Reproved denominator comparability, corrected whitening, and boundary hierarchy in the chosen Dirichlet or \(\tau\) channel.
4. In the non-self-dual Dirichlet case, a proof that the single-channel quotient is structurally sufficient for the later scalar-amplitude steps, rather than merely a phase front end. From current scope alone, the paired \((\chi,\bar\chi)\) route remains the more conservative scalar-amplitude target.

Exact refs

- Common brief and required schema: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`.
- Scattering note boundary: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:39-58,69-79`.
- Dirichlet note current wording and missing items: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:16-23,25-42,44-72`.
- Tau note current wording and missing checkpoints: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:18-35,36-50`.
- Route A unimodularity argument: `/mnt/c/workspace/riemann2/tasks/20260423-133143-attack-gap-quotient-phase-generalization/reports/gap-quotient-phase-routeA.md:21-48,56-100,117-125`.
- Route B phase/value separation and wording fixes: `/mnt/c/workspace/riemann2/tasks/20260423-133143-attack-gap-quotient-phase-generalization/reports/gap-quotient-phase-routeB.md:15-43,68-80`.
- Manuscript phase input: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-159`.
- Manuscript split into background plus zero contribution: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-287`.
- Calibration dependence on \(S(m)\): `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:748-778`.
- Corrected local deformation \(\Delta_\zeta=S(m)A_{\val}+R_\zeta\): `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1528-1566`.
- Remainder estimate relative to the leading value channel: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2060-2087`.
- Boundary estimate still using \(L(m)S(m)^2/Q^3\): `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2218-2232`.
- Archive quotient template and zero-kernel decomposition: `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`.

Dependencies

1. The completed-\(L\) functional equation and conjugation symmetry assumed in Route A for primitive Dirichlet and Ramanujan-\(\tau\).
2. The manuscript's internal distinction between the phase input \(q=\Phi'\) and the value-channel coefficient \(S(m)\).
3. The archive's quotient template as provenance for the candidate phase object.

Strongest objection

The main risk is overreading `unimodular quotient` as `correct channel realized`. That jump is not licensed. Even if the quotient determines a real phase derivative, the manuscript's contradiction uses more than a phase observable: it uses a specific background-subtracted scalar as the coefficient of the leading value channel, with positivity/sign-compatibility, whitening, denominator control, and boundary decay. From completed-\(L\) identities alone, none of those downstream properties follow. In the non-self-dual primitive-Dirichlet case, the boundary unimodularity also does not settle whether the single-channel quotient is better than the paired route for the scalar-amplitude step.

Needed for promotion

1. Prove a source theorem in one target family tying the manuscript phase to a specific completed quotient, including normalization and branch choices.
2. Prove a family-local zero/background decomposition whose background-subtracted scalar is the positive sign-compatible coefficient of the leading local value channel.
3. Reprove the local package: denominator comparability, corrected whitening, oddness transport or replacement, and the microscopic boundary hierarchy.
4. For primitive Dirichlet, decide by proof whether the single-channel quotient suffices beyond the phase front end or whether the paired \((\chi,\bar\chi)\) package is necessary for the scalar-amplitude layer.
5. Scope the notes explicitly as `phase-channel upgrade only` wherever a reader could otherwise infer realized Dirichlet or \(\tau\) localization.

Honest verdict: unimodularity is enough to revise the earlier channel notes, but only narrowly. It upgrades the single completed quotient to a serious boundary phase candidate. It does not overturn the earlier caution that the value-channel theorem is still missing. The strongest safe Dirichlet statement is `single-channel quotient is a conditional phase candidate; paired route remains the conservative scalar-amplitude target`. The strongest safe \(\tau\) statement is `self-dual quotient is the cleanest phase candidate, but none of the localization checkpoints is discharged`. Any claim stronger than `phase-channel upgrade only` needs scoped weakening.
