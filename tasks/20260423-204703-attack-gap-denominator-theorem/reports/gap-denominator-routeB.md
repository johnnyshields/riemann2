Claim

Denominator transport splits cleanly into a narrow formal lemma and a larger family-specific realization burden. The formal part is this: if a family's omitted local terms are built from quadratic denominators of the form `D_{rho,pm}(s)=(x_rho\pm s)^2+a_rho^2`, if one has a microscopic lower bound `a_rho\ge sigma_0/Q`, and if the differentiated omitted terms are rational combinations of powers of `D_{rho,pm}(s)^{-1}` whose real-line shell sums already converge, then the manuscript's comparability argument and the resulting omitted-smooth holomorphy on `|s|<rho_0/Q` go through with the same proof. What is tied to zeta is not the triangle-inequality step itself, but the fact that the omitted-zero contribution actually has that denominator shape, that `a_rho` is exactly a zero-free-width quantity in `{beta_rho,1-beta_rho}`, and that the needed shell convergence / counting input is already available in the zeta decomposition. From current scope alone, denominator comparability should be treated as a standalone cross-family theorem target, but only in the stronger packaged form `microscopic denominator comparability plus omitted-smooth holomorphy radius (and hence whitening admissibility)` rather than as a bare isolated inequality.

Status

open

Evidence

- The denominator theorem itself is Proposition `prop:denominator-comparability`. Its proof is short and splits into two pieces. First, with `D_{rho,pm}(s)=(x^2+a^2)\pm 2xs+s^2`, the estimate `|2xs+s^2|\le \tfrac12 x^2+3|s|^2` and the lower bound `a\ge sigma_0/Q`, `|s|\le rho_0/Q`, `rho_0\le sigma_0/\sqrt 6` give the comparison `|D_{rho,pm}(s)|\asymp x^2+a^2`. Second, because differentiated omitted-zero terms are rational combinations of `D_{rho,pm}(s)^{-1}`, the same shell sums as on the real line give uniform convergence and holomorphy on the disk.
- That first step is formal. It does not use any zeta identity beyond the denominator model and a lower bound on `a_rho`. So a family with the same local denominator architecture and the same microscopic lower bound would inherit the same comparability proof.
- The second step is not empty bookkeeping. The proposition explicitly assumes the corresponding real-line shell sums converge. In the zeta draft this is supported by the existing omitted-zero decomposition and counting package; outside zeta, that convergence and the compatible local decomposition are separate theorem burdens.
- The manuscript then uses denominator comparability immediately inside corrected whitening: Proposition `prop:corrected-whitening` cites Proposition `prop:denominator-comparability` as the holomorphy input for `T_far(t_pm)` and its derivatives, and the odd-holomorphic package later depends on that disk holomorphy. So this is not merely a cosmetic lemma; it is the gateway from real-line source control to a holomorphic microscopic disk.
- The non-zeta notes already point the same way. `dirichlet_paired_source.md` lists denominator comparability among the items pairing does not fix. `dirichlet_channel.md` lists `reproved corrected whitening, denominator comparability, and boundary estimates` as still missing. `tau_localization.md` isolates `microscopic denominator comparability and holomorphy radius` as its own checkpoint. `portability_note.tex` likewise places microscopic denominator control in the nonportable source layer and in the missing completed-`L` realization theorem.
- This matches the pattern of the variable-`x`, source-package, and odd-package notes: the local algebra can transport, but the finite-`s` holomorphic/whitening package does not transport automatically from the zeta proof skeleton alone.

Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/variable_x.md:23-36`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:8-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:8-38`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:57-74`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_channel.md:26-76`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/tau_localization.md:45-53`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/portability_note.tex:89-104`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/portability_note.tex:169-182`
- `paper/proof_of_rh.tex:856-946` (`prop:denominator-comparability`)
- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)
- `paper/proof_of_rh.tex:2212-2322` (odd holomorphic transverse channel uses the disk holomorphy)

Dependencies

- A family-specific local decomposition whose omitted terms admit the same kind of quadratic denominator model in the microscopic `s` variable.
- A family-specific lower bound replacing `a_rho\ge sigma_0/Q`; in zeta this comes from zero-free-region input, and in other families it may depend on conductor, self-duality class, or the chosen paired/completed object.
- Real-line shell counting / convergence strong enough to justify the uniform differentiated omitted-zero sums on the microscopic disk.
- Baseline same-point positivity / scale hierarchy if one wants to proceed from denominator comparability to corrected whitening and then to boundary estimates.

Strongest objection

The strongest objection is that this report may still overstate the independence of denominator comparability. In some completed-`L` families, once the exact source theorem and the correct local scalar object are written in the right coordinates, the denominator architecture, microscopic lower bound, shell convergence, and whitening-scale hierarchy may arrive together rather than as a genuinely separable theorem. From current scope alone, though, there is no proof of that collapse. The safe statement is only that denominator comparability is not formal from slot transport or quotient algebra alone, and should remain an explicit theorem target until a family-specific realization theorem shows it is subsumed.

Needed for promotion

- State the cross-family target in packaged form: `microscopic denominator comparability plus omitted-smooth holomorphy radius`, not just `denominator comparability`.
- For one non-zeta family, prove the analogue of `prop:denominator-comparability` with an explicit denominator model and explicit lower-bound input replacing the zeta zero-free width.
- Show that the resulting holomorphy is strong enough for the family's corrected same-point and mixed blocks, so Proposition `prop:corrected-whitening` has an actual analogue rather than a formal placeholder.
- Recheck adversarially that no extra zeta-only input is being smuggled into the shell convergence or denominator model.

Honest verdict: the comparability estimate itself is formal once the denominator model and a microscopic lower bound are in hand, but those hypotheses are exactly the part not yet transported beyond zeta. So yes, treat denominator comparability as a standalone cross-family theorem target, but only as part of a denominator-plus-holomorphy package feeding corrected whitening, not as an automatic consequence of earlier transport steps.
