# Claim

- [confirmed] From the current draft alone, the formula-level scattering-quotient interpretation is not yet a proved manuscript theorem. What is proved in the cited source layer is the decomposition
  \[
  q(t)=B_\zeta(t)+S(t),
  \qquad
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m),
  \]
  with each kernel nonnegative. What is only reconstructed from those formulas is the stronger identification with a completed strip-edge quotient such as
  \[
  \frac12\ImPart\!\left(\frac{d}{dt}\log\frac{\xi(1+2it)}{\xi(2it)}\right).
  \]
- [confirmed] The strongest safe statement about \(S(m)\) now is:
  \[
  S(m)=\sum_\rho \left(\frac{1-\beta_\rho}{(1-\beta_\rho)^2+(2m-\gamma_\rho)^2}+\frac{\beta_\rho}{\beta_\rho^2+(2m-\gamma_\rho)^2}\right)>0,
  \]
  and each summand is exactly
  \[
  \RePart\!\left(\frac{1}{1+2im-\rho}-\frac{1}{2im-\rho}\right).
  \]
  So \(S(m)\) is a positive strip-edge zero kernel and the background-subtracted scalar coefficient of the local value channel. Conditional on a separate completed-\(L\) realization theorem, this is the zero part of a completed-log-derivative difference.
- [confirmed] For the Dirichlet / \(\tau\) program, this improves candidate selection only. It points to a better target object than a raw critical-line value or mere reality surrogate: one wants a realized completed-object package whose background-subtracted zero contribution is a real nonnegative scalar playing the role of \(S(m)\). It does not, from current draft scope alone, advance localization, whitening, denominator comparability, boundary control, or contradiction.
- [confirmed] Claims that need scoped weakening are:
  1. Any statement that the draft already proves a completed scattering-quotient formula for \(q\) or \(S\).
  2. Any statement that Dirichlet or \(\tau\) analogues are already realized once one notices the kernel identity.
  3. Any statement that the scattering reading does more than improve the choice of candidate channel.
  4. Any statement that a full completed-\(L\) realization theorem already exists.

# Status

- open

# Evidence

- The draft defines a general real phase \(\Phi\) and \(q(t)=\Phi'(t)\) before specializing to zeta input. It then states
  \[
  q(t)=B_\zeta(t)+S(t)
  \]
  with \(B_\zeta\) called the explicit background contribution and \(S\) the background-subtracted zero contribution.
- The omitted-zero tail is written as a sum of kernels
  \[
  f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2},
  \]
  and later the draft states exactly
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
  \]
  This is the strongest explicit formula currently in the manuscript for \(S(m)\).
- Algebraically, for \(\rho=\beta+i\gamma\),
  \[
  f_{\beta,\gamma}(m)=\RePart\!\left(\frac{1}{1+2im-\rho}-\frac{1}{2im-\rho}\right).
  \]
  So the zero kernel matches the strip-edge difference of simple poles. That makes a completed-quotient reading natural.
- But the cited source layer never writes an explicit identity equating the manuscript's phase derivative \(q\) with the argument derivative of a completed quotient, never fixes the factor-of-\(2\) normalization, and never itemizes the exact remainder as gamma factor, trivial zeros, pole term, and Hadamard exponential constant.
- The local package uses \(S(m)\) structurally as the coefficient in
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
  \]
  and in the calibration relation \(u^2\asymp (x/B)S(m)\). So the manuscript needs a positive scalar amplitude, not just a real observable.
- The GRH / Dirichlet / \(\tau\) notes already place the portability boundary at candidate selection plus a missing completed-\(L\) realization theorem. The scattering reading is consistent with that boundary and does not move it.

# Exact refs

- `paper/proof_of_rh.tex:149-160` for the abstract phase and `q(t)=\Phi'(t)`.
- `paper/proof_of_rh.tex:273-299` for `q(t)=B_\zeta(t)+S(t)`, `S(m):=q_\zeta(m)-B_\zeta(m)`, and the curvature estimate.
- `paper/proof_of_rh.tex:345-369` for the omitted-zero tail and the explicit kernel `f_{\beta,\gamma}`.
- `paper/proof_of_rh.tex:753-777` for calibration using `S(m)`.
- `paper/proof_of_rh.tex:1471-1621` for the corrected local deformation and the decomposition `\Delta_\zeta=S(m)A_{\val}+R_\zeta`.
- `paper/proof_of_rh.tex:26301-26327` for the explicit identity `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:8-18,22-32,43-58` for the present Dirichlet boundary.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:8-27,39-43` for the present `\tau` boundary.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:37-66,79-85` for the cycle-level portability boundary and missing theorems.
- `tasks/20260423-130548-attack-gap-scattering-generalization/reports/gap-scattering-generalization-routeA.md:3-30,81-104`.
- `tasks/20260423-130548-attack-gap-scattering-generalization/reports/gap-scattering-generalization-routeB.md:3-12,35-47,67-76`.

# Dependencies

- A manuscript-level theorem identifying the actual `q(t)` with a specific completed strip-edge quotient or equivalent scattering matrix phase derivative.
- Exact normalization bookkeeping: whether the phase is full argument, half-argument, or a sign-reversed convention.
- Exact decomposition of the background term into gamma factors, trivial zeros, pole cancellation, and any Hadamard constant.
- For portability claims: a realized completed-`L` local package in which the analogue of `S(m)` is the actual leading scalar coefficient of the corrected local deformation.

# Strongest objection

- The present interpretation may be only a clean repackaging of the zero kernel, not a new theorem about the manuscript's source object. From current draft scope alone, one cannot pass from
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
  \]
  to
  \[
  q(t)=\frac12\ImPart\!\left(\frac{d}{dt}\log\frac{\xi(1+2it)}{\xi(2it)}\right)
  \]
  with all constants and background terms matched. Therefore the apparent gain for Dirichlet or `\tau` may be only that it identifies a better candidate channel from current scope alone, not that it reduces the hard portability work.

# Needed for promotion

- State and prove one explicit source theorem giving the exact completed-quotient realization of `q`, including normalization.
- Rewrite `S(m)` as the residual zero contribution of that theorem after explicit subtraction of the full background term.
- Decide the sharp wording for portability: `better candidate channel` versus `realized analogue`.
- For primitive Dirichlet characters, prove whether a paired scalar object or some other quotient actually yields a nonnegative scalar `S`-analogue in the corrected local block.
- For `\tau`, prove the corresponding completed-object decomposition and the preservation of whitening, denominator, and boundary estimates.
- Honest verdict: the scattering-quotient reading is mathematically natural and likely the right way to name the kernel behind `S(m)`. It is not yet supported as a formula-level theorem of the draft, and from current scope alone it improves the Dirichlet / `\tau` program only by sharpening the candidate object, not by closing any realized portability gap.
