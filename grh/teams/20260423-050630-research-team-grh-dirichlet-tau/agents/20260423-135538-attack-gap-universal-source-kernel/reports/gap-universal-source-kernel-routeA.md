# Proved

## Claim

For any completed object \(\Lambda_F(s)\) and quotient
\[
\phi_F(s):=\frac{\Lambda_F(2s-1)}{\Lambda_F(2s)},
\]
the local contribution of a nontrivial zero \(\rho=\beta+i\gamma\) of multiplicity \(m_\rho\) to the logarithmic derivative of \(\phi_F\) is forced by quotient algebra alone. Writing locally
\[
\Lambda_F(z)=(z-\rho)^{m_\rho}u_\rho(z),\qquad u_\rho(\rho)\neq 0,
\]
the singular part is
\[
m_\rho\!\left(\frac{1}{s-\frac{1+\rho}{2}}-\frac{1}{s-\frac{\rho}{2}}\right).
\]
Hence on the strip edge \(s=\tfrac12+it\), the corresponding real kernel is universal up to the global sign/normalization used to define the family's source scalar:
\[
K_\rho(t):=\Re\!\left(\frac{1}{\frac12+it-\frac{\rho}{2}}-\frac{1}{\frac12+it-\frac{1+\rho}{2}}\right)
=2\Re\!\left((1+2it-\rho)^{-1}-(2it-\rho)^{-1}\right).
\]
Equivalently,
\[
K_\rho(t)=2\left[\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}\right].
\]
So the strip-edge profile itself depends only on \((\beta,\gamma)\) and multiplicity, not on the family.

## Status

proved

## Evidence

The derivation is local. A zero \(\rho\) of \(\Lambda_F\) produces:

1. a zero of the numerator \(\Lambda_F(2s-1)\) at \(s=(1+\rho)/2\);
2. a zero of the denominator \(\Lambda_F(2s)\), hence a pole of \(\phi_F\), at \(s=\rho/2\).

Taking \(\partial_s\log\phi_F\) gives the difference of these two simple fractions, with multiplicity \(m_\rho\). Restricting to \(s=\tfrac12+it\) and taking real parts gives the displayed rational profile. No Euler product input, conductor input, gamma-factor input, or family-specific coefficient input enters this computation.

The sign issue is only a normalization issue: the archive source slice uses the opposite order of the two fractions because its scalar \(q\) is defined with a matching sign convention. That does not change the kernel shape.

## Exact refs

- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5530-5598`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:21-37`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-20,24-39`

## Dependencies

- Only the local factorization of \(\Lambda_F\) near a zero.
- Only the quotient shape \(\phi_F(s)=\Lambda_F(2s-1)/\Lambda_F(2s)\).
- Multiplicity convention: a zero of order \(m_\rho\) contributes \(m_\rho K_\rho\).

## Strongest objection

This proves the universal local kernel for the logarithmic derivative of the quotient, not yet for any manuscript-specific scalar unless that scalar is explicitly identified with a fixed signed/normalized real part of \(\partial_s\log\phi_F(\tfrac12+it)\).

## Needed for promotion

- A clean theorem in project scope stating exactly which family scalar equals which signed/normalized strip-edge restriction of \(\partial_s\log\phi_F\).
- An explicit multiplicity statement in that theorem.

# Conditional on Same Strip-Edge Source Theorem

## Claim

Assume a family \(F\) has a completed quotient source theorem of the same strip-edge form as the archive zeta model: namely, its source scalar is given on singularity-free compact intervals by a family background term plus a fixed signed/normalized strip-edge restriction of \(\partial_s\log\phi_F\) for
\[
\phi_F(s)=\frac{\Lambda_F(2s-1)}{\Lambda_F(2s)}.
\]
Then the single-zero contribution kernel is universal across completed \(L\)-functions. The only family dependence is:

1. which zeros \(\rho\) occur, with what multiplicities;
2. the background term from gamma factors, trivial zeros, and poles;
3. the one global sign/factor built into the source-theorem normalization.

Everything else in the one-zero term is zero-location data only.

## Status

proved

## Evidence

Under that hypothesis, the source theorem does not alter the local singular algebra. Each nontrivial zero still enters through the same numerator-zero / denominator-pole pair at \((1+\rho)/2\) and \(\rho/2\). Therefore every one-zero term is the same translate-and-shape kernel \(K_\rho\), evaluated at the relevant strip-edge parameter.

What depends on zero location only:

1. \(\beta=\Re\rho\) and \(\gamma=\Im\rho\);
2. the translated denominators \((1-\beta)^2+(2t-\gamma)^2\) and \(\beta^2+(2t-\gamma)^2\);
3. positivity of the kernel after the archive sign choice when \(0\le \beta\le 1\).

What depends on the family:

1. the background subtraction;
2. the actual zero multiset;
3. whether the theorem defines the source scalar with \(K_\rho\), \(-K_\rho\), or a fixed scalar multiple;
4. whether the theorem is stated in a \(t\)-variable or a sampled \(m\)-variable.

So the universal statement is: once the same quotient source theorem exists, the one-zero kernel is not a new family-specific object.

## Exact refs

- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5551-5598`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:8-18,39-62`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:10-24,28-50`

## Dependencies

- The family has a completed quotient theorem with the same strip-edge architecture.
- The strip-edge restriction is taken on compact intervals avoiding the finitely many real singularities from background terms.
- The theorem uses completed zeros, not raw uncompleted zeros.

## Strongest objection

For non-self-dual or complex families, the existence of a real strip-edge phase/source scalar is not automatic from the quotient alone. From quotient algebra alone one gets the kernel inside \(\partial_s\log\phi_F\), but not automatically the reality/unimodularity package that lets it occupy the manuscript's positive scalar slot.

## Needed for promotion

- A family-by-family proof of the completed quotient source theorem.
- A proof that the chosen strip-edge scalar is real and matches the manuscript slot exactly.
- A compact-interval convergence / regularization theorem for the full zero sum plus background.

# Missing

## Claim

The repo does not yet contain a proved theorem that this universal kernel statement is realized for completed \(L\)-functions beyond the archive zeta template.

## Status

open

## Evidence

The current notes explicitly stop at a channel-selection upgrade and say the realized family theorems are missing. They also state that the source theorem gap is not only gamma/trivial-zero bookkeeping: one still needs the theorem identifying the family's phase derivative or source scalar with the completed quotient object itself.

So what is missing is concrete and finite:

1. fix the completed quotient object for the family;
2. prove the branch/sign/factor-of-2 normalization;
3. prove the one-zero source contribution identity in the family theorem's notation;
4. state the multiplicity convention;
5. prove compact-interval convergence with the background term;
6. for complex/non-self-dual families, prove the reality or positivity statement actually needed by the scalar slot.

## Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-18,31-40,42-53`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:48-62,73-83`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-38,40-50`

## Dependencies

- A completed-family source theorem.
- A family-specific edge normalization theorem.
- Background-term control.

## Strongest objection

The phrase "universal across completed \(L\)-functions" can overclaim if it is read as a realized portability theorem. From current scope alone, the safe claim is narrower: the local one-zero quotient kernel is universal once the same source architecture is in place.

## Needed for promotion

- One fully written family realization, including the exact scalar slot and background term.
- An adversarial verification pass checking sign, multiplicity, and compact-interval regularization.
- A precise scoped statement separating universal local kernel from family realization.

Honest verdict: the single-zero strip-edge kernel is universal at the quotient-log-derivative level. What is not yet universal in repo scope is the family realization theorem that inserts that kernel into the manuscript's exact scalar channel.
