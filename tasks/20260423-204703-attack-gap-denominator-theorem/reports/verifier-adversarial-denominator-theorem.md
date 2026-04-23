# Claim

Denominator comparability is not yet safely framed as a standalone cross-family theorem target. The current paper proves a narrower proposition: once a family already has a realized omitted-zero decomposition with quadratic denominators, a microscopic lower bound on the denominator width, and convergent real-line shell sums for the differentiated omitted terms, one gets microscopic denominator comparability and hence holomorphic extension of the omitted-smooth piece on `|s|<\rho_0/Q`. From current scope alone, the safe theorem target is therefore a packaged corrected-whitening input, not an autonomous family theorem.

The strongest safe wording now is:

`the current denominator proposition transports existing real-line omitted-zero shell control to the microscopic complex disk and supplies the omitted-smooth holomorphy needed for corrected finite-s whitening; whether this separates as an independent cross-family theorem depends on a family-specific realized source package.`

Claims that need scoped weakening:

- `denominator comparability should be treated as a standalone cross-family theorem target` should be weakened to `denominator comparability remains an explicit subtarget inside corrected-whitening transport unless a family-specific realization theorem separates it`.
- `the triangle-inequality step is formal, so denominator transport is a clean independent theorem` should be weakened to `the triangle-inequality step is formal once the denominator model, microscopic lower bound, and real-line shell convergence are already in hand`.
- Any sentence suggesting denominator comparability alone gives the corrected finite-`s` package should be weakened to `it gives only the omitted-smooth holomorphy input for corrected whitening`.

# Status

open

# Evidence

Proved:

- Proposition `prop:denominator-comparability` proves exactly a microscopic two-sided bound for `D_{\rho,\pm}(s)` and then uniform convergence / holomorphy of the omitted-smooth part, provided the corresponding real-line shell sums already converge (`paper/proof_of_rh.tex:856-946`).
- Proposition `prop:corrected-whitening` uses it only for `Holomorphy of the omitted smooth part and its required t-derivatives` before positivity and holomorphic inverse-square-root arguments take over (`paper/proof_of_rh.tex:1417-1457`).
- The proposition is therefore a genuine input, but a narrow one: it moves existing real-line control onto the microscopic complex disk.

Conditional on additional family-specific input:

- Route B is right that the inequality step itself is formal once the denominator architecture is already realized. But the current manuscript does not show that these hypotheses arrive independently of the larger source package in another family.
- The variable-`x` note already warns against isolating a local transport fragment from the shrinking-scale source theorem: `local A_val transport alone is not the full variable-x theorem` (`grh/.../notes/variable_x.md:23-36`). The same caution applies here.
- The odd-package note makes the same structural point more sharply: transport becomes safe only after the family supplies the realized scalar object and its boundary control (`grh/.../notes/odd_package_transport.md:22-49`). Denominator comparability has the same flavor: formal after realization, not before.

Missing:

- No cited result shows that, in a non-zeta family, the denominator model, the lower bound replacing `a_\rho\ge \sigma_0/Q`, and the needed real-line shell convergence split off as a theorem independent of the corrected-whitening/source package.
- No cited result shows the opposite either, namely that these always collapse into one inseparable realized source theorem. So the standalone-theorem framing is presently not proved, but neither is its impossibility from current scope alone.

# Exact refs

- Common brief writing discipline and schema: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- Variable-`x` transport caution: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/variable_x.md:23-36`
- Odd-package transport caution: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:22-49`
- Route A report: `/mnt/c/workspace/riemann2/tasks/20260423-204703-attack-gap-denominator-theorem/reports/gap-denominator-routeA.md:1-75`
- Route B report: `/mnt/c/workspace/riemann2/tasks/20260423-204703-attack-gap-denominator-theorem/reports/gap-denominator-routeB.md:1-51`
- Denominator proposition: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946`
- Corrected whitening use-site: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458`
- Variable-`x` checklist showing denominator estimates are only one item inside a larger shrinking-scale upgrade: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5549-5577`

# Dependencies

- A realized omitted-zero decomposition whose differentiated terms are rational combinations of powers of quadratic denominators of the required microscopic form.
- A family-specific lower bound replacing `a_\rho\ge \sigma_0/Q`.
- Real-line shell convergence for the differentiated omitted-zero sums.
- The downstream corrected-whitening package: positivity of the same-point blocks and holomorphic inverse-square-root control remain separate inputs after denominator comparability.

# Strongest objection

The strongest objection to the standalone-theorem framing is that it mistakes a conditional transport lemma for an independently isolated family theorem. In the present paper, denominator comparability is not derived from abstract quotient algebra or slot transport alone; it is stated only after the zeta omitted-zero terms have already been written in the correct denominator form and only under pre-existing real-line shell convergence. From current scope alone, saying `yes, this is best treated as a standalone cross-family theorem target` is too strong. The most that is supported is: it is an explicit missing subtarget inside corrected-whitening transport, and it may or may not separate cleanly in another family depending on how the realized source theorem is organized.

# Needed for promotion

- For a specific non-zeta family, exhibit the realized omitted-zero denominator model and the analogue of the microscopic lower bound.
- Prove the real-line shell convergence needed for differentiated omitted terms in that same family.
- Decide structurally, from an actual family model rather than analogy, whether these ingredients separate from the larger corrected-whitening/source theorem or arrive together.

Honest verdict: denominator comparability is real and necessary, but the current evidence supports only a narrow packaged role: it is the omitted-smooth holomorphy input feeding corrected whitening. Treating it now as the best standalone cross-family theorem target would overclaim. The safest wording is to keep it as an explicit subtarget inside the corrected-whitening transport package, with the caveat that a future family-specific realization theorem could either isolate it cleanly or absorb it into a larger source theorem.
