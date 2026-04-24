Claim

Let

\[
\phi_F(s):=\frac{\Lambda_F(2s-1)}{\Lambda_F(2s)}.
\]

For any completed \(L\)-function \(\Lambda_F\) normalized to satisfy the standard functional equation

\[
\Lambda_F(s)=\varepsilon_F\,\Lambda_{F^\vee}(1-s),\qquad |\varepsilon_F|=1,
\]

and the standard conjugation identity

\[
\overline{\Lambda_F(\bar s)}=\Lambda_{F^\vee}(s),
\]

one has on the critical line \(s=\tfrac12+it\)

\[
\phi_F\!\left(\tfrac12+it\right)=\varepsilon_F\,\frac{\overline{\Lambda_F(1+2it)}}{\Lambda_F(1+2it)}
\]

whenever \(\Lambda_F(1+2it)\neq 0\). Hence

\[
\left|\phi_F\!\left(\tfrac12+it\right)\right|=1.
\]

Applied to primitive Dirichlet characters \(\chi\), this gives

\[
\phi_\chi\!\left(\tfrac12+it\right)=\varepsilon_\chi\,\frac{\overline{\Lambda(1+2it,\chi)}}{\Lambda(1+2it,\chi)}
=\varepsilon_\chi\,e^{-2i\arg \Lambda(1+2it,\chi)},
\]

and applied to the recentered Ramanujan-\(\tau\) completed function \(\Lambda_\tau\) with self-dual equation \(\Lambda_\tau(s)=\varepsilon_\tau\Lambda_\tau(1-s)\), it gives

\[
\phi_\tau\!\left(\tfrac12+it\right)=\varepsilon_\tau\,\frac{\overline{\Lambda_\tau(1+2it)}}{\Lambda_\tau(1+2it)}.
\]

So the strip-edge quotient is naturally unimodular on the critical line for primitive Dirichlet and for tau, conditional only on those standard completed-\(L\) identities.

This resolves the phase channel only at the boundary-selection level: the quotient already lands in \(U(1)\) on \(\Re(s)=\tfrac12\), so a phase function \(\Phi_F(t)\) with \(\phi_F(\tfrac12+it)=\varepsilon_F e^{-2i\Phi_F(t)}\) is formally natural away from zeros. It does not resolve any local realization theorem, positivity of the background-subtracted scalar, corrected whitening, denominator comparability, oddness transport, or contradiction mechanism.

Status

proved

Evidence

Proved:

Take \(s=\tfrac12+it\). Then \(2s-1=2it\) and \(2s=1+2it\). By the completed functional equation,

\[
\Lambda_F(2it)=\varepsilon_F\,\Lambda_{F^\vee}(1-2it).
\]

By the conjugation identity,

\[
\Lambda_{F^\vee}(1-2it)=\overline{\Lambda_F(1+2it)}.
\]

Therefore

\[
\phi_F\!\left(\tfrac12+it\right)
=\frac{\Lambda_F(2it)}{\Lambda_F(1+2it)}
=\varepsilon_F\,\frac{\overline{\Lambda_F(1+2it)}}{\Lambda_F(1+2it)}.
\]

Since \(|\varepsilon_F|=1\) and \(|\overline{z}/z|=1\) for \(z\neq 0\), unimodularity follows.

Conditional on external completed-\(L\) facts:

1. Primitive Dirichlet: the standard completed function satisfies \(\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi)\) with \(|\varepsilon_\chi|=1\), and \(\overline{\Lambda(\bar s,\chi)}=\Lambda(s,\bar\chi)\).
2. Tau: after the standard central recentering of the Ramanujan-\(\tau\) \(L\)-function, the completed function satisfies \(\Lambda_\tau(s)=\varepsilon_\tau\Lambda_\tau(1-s)\) with \(\varepsilon_\tau\in\{\pm1\}\), together with \(\overline{\Lambda_\tau(\bar s)}=\Lambda_\tau(s)\).

What this resolves about the phase channel:

1. The archived zeta quotient mechanism at `phi(s)=Lambda(2s-1)/Lambda(2s)` is not zeta-specific at the level of critical-line modulus; it extends formally to any normalized completed \(L\)-function with the same FE/conjugation package.
2. For primitive Dirichlet and tau, the quotient itself is already a natural boundary phase object. No extra rotation is needed to make its modulus \(1\); at most one absorbs the constant root number \(\varepsilon_F\).

What this does not resolve:

1. It does not produce the derivative decomposition from zeros plus background used in the archive unless one separately imports a zero-expansion/log-derivative argument in that family.
2. It does not prove that the resulting phase derivative is the manuscript's needed positive strip-edge scalar or even a sign-compatible scalar analogue of `S(m)`.
3. It does not realize the local block, calibration interface, odd transverse scalar, whitening hierarchy, denominator control, or final contradiction in either family.

Missing:

1. A family-specific theorem turning this unimodular quotient into the corrected local package.
2. A proof that the background-subtracted zero contribution in the Dirichlet or tau case is real nonnegative in the required sense.
3. For non-self-dual Dirichlet \(\chi\), a proof that the single-channel quotient rather than a paired \((\chi,\bar\chi)\) package is the right scalar for the manuscript's later steps.

Exact refs

- Common brief and schema: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`.
- Archived quotient provenance: `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`.
- Scattering sharpening: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:24-35,39-58,69-79`.
- Dirichlet boundary and missing items: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:20-23,39-42,54-72`.
- Tau boundary and missing items: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:18-34,36-50`.
- External facts used but not proved here: standard completed functional equations and conjugation identities for primitive Dirichlet \(L\)-functions and the centered Ramanujan-\(\tau\) completed \(L\)-function.

Dependencies

1. Standard primitive-Dirichlet completed functional equation and conjugation symmetry.
2. Standard central normalization of the Ramanujan-\(\tau\) completed \(L\)-function to a \(1-s\) functional equation.
3. The archive's candidate-object choice `phi(s)=Lambda(2s-1)/Lambda(2s)` as the phase-channel template.

Strongest objection

This argument is only a boundary-modulus observation. It shows \(|\phi(\tfrac12+it)|=1\), but from completed-L facts alone it does not show that this quotient feeds the manuscript's actual local scalar package. In the non-self-dual primitive-Dirichlet case, it also does not decide whether the single quotient is structurally better than a paired \((\chi,\bar\chi)\) scalar channel for later positivity and oddness steps.

Needed for promotion

1. A verified zero-log-derivative decomposition in the primitive-Dirichlet and tau families matching the archive's zeta pattern, with external facts clearly separated from in-repo claims.
2. A proof that the resulting family-specific scalar is the right analogue of the manuscript's background-subtracted positive strip-edge coefficient, not merely a unimodular boundary quotient.
3. A realized local theorem in one chosen family showing corrected local block, denominator comparability, whitening/boundary control, and oddness transport.
4. An adversarial check that no hidden non-self-dual obstruction appears in the primitive-Dirichlet single-channel route.
5. If one wants a canonical statement, a precise normalization convention for tau and for primitive Dirichlet characters must be fixed in the paper-facing language.
