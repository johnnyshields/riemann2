# Claim

Equal reduced-package fibers determine the canonical quotient package only up to the existing quotient/gauge identifications, but the present draft does **not** prove that this already forces agreement of the corrected local block modulo `\Phi_K`-invisible directions through the first surviving odd order. The sharp positive statement currently supported is narrower:

if two one-pair states have the same reduced package
\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right),
\]
then their cubic/quintic/septic quotient data agree after scalar rescaling and septic gauge along the quintic fixed-sector line. What is still missing is a theorem that every remaining hidden direction in the corrected-block jet is annihilated by `\Phi_K` up to the first surviving odd order.

# Status

open

# Evidence

The paper proves exact strengthened coincidence only for the reduced package `\widehat\Psi`; this identifies the canonical quotient data `(c, A_5^{\mathfrak f}, [A_7^{\mathfrak f}])` up to the expected scalar law and septic gauge. It does **not** identify a unique raw septic representative, and the draft says this ambiguity is real rather than cosmetic.

More importantly for the hidden-state lemma, the paper separately records that the odd coefficients of the corrected local block still bundle together multiple ambiguity sources: raw pure-value odd jets plus normalization/basis-gauge directions. That is exactly the hidden-state room one would need to kill before concluding package-fiber invariance of the first surviving `\Phi_K`-visible odd jet.

The strongest negative evidence is the explicit audit that the naive source-summed corrected-block model is even analytic in the source weight. So that model cannot prove the one-atom linearity / diagonal merger law needed to collapse hidden state on reduced-package fibers. This blocks the intended route from package coincidence to a `\Phi_K`-visible odd-jet factorization.

So the present exact obstruction is:

1. `\widehat\Psi` closes the quotient package through order `7`.
2. Raw corrected-block odd jets still contain extra hidden directions beyond that quotient package.
3. No theorem in the draft shows those extra directions lie in `\ker \Phi_K` through the first surviving odd order.

# Exact refs

- `paper/proof_of_rh.tex:5932-5951` — `V_{\val}^{(2j+1)}` explicitly bundles raw pure-value odd jets with normalization/basis-gauge ambiguity.
- `paper/proof_of_rh.tex:6998-7061` — canonical order-`7` data are `A_5^{\mathfrak f}` and `\Delta_7`; raw `(u_7,v_7)` is not canonical.
- `paper/proof_of_rh.tex:7079-7179` — septic gauge law `(A_7^{\mathfrak f})^{\new}=A_7^{\mathfrak f}+c_2A_5^{\mathfrak f}` and `\Delta_7` invariance.
- `paper/proof_of_rh.tex:7998-8033` — local gauge-fixing exists, but only as an auxiliary noncanonical choice.
- `paper/proof_of_rh.tex:11368-11584` — exact strengthened coincidence yields equality of `\widehat\Psi` on exact two-pair coincidence.
- `paper/proof_of_rh.tex:11888-11932` — the desired package-collapse route would follow from one-atom linearity + diagonal merger for a source-level package.
- `paper/proof_of_rh.tex:12192-12227` — naive source-summed corrected-block model is even in source weight, so it cannot prove that merger law.
- `paper/proof_of_rh.tex:2214-2307` — `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))` and odd-jet extraction are already set up, so the missing step is package-to-`\Phi_K` factorization, not the extractor.
- `paper/proof_of_rh.tex:24985-25030` — current endgame compression identifies package-level coincidence/functoriality as the live burden.
- `paper/proof_of_rh.tex:26369-26397` — order-`7` quotient package is canonically closed, but raw representative choice remains.

# Dependencies

- A theorem that the actual corrected two-atom package descends functorially to a reduced package state at coincidence, or at least satisfies the source-level merger hypotheses of `Lemma~\ref{lem:minimal-source-level-two-point-criterion}`.
- A factorization statement from corrected-block odd jets to reduced package fibers strong enough to show that fiberwise differences are `\Phi_K`-invisible up to the first surviving odd order.

# Strongest objection

Equal `\widehat\Psi` fibers only control the canonical quotient package through septic order. The paper does not identify the corrected local block, or its odd Taylor coefficients under `\Phi_K`, as a function of that quotient package. Because `V_{\val}^{(2j+1)}` still contains extra hidden directions and the naive merger model fails by even-amplitude parity, there is currently no basis for asserting that those hidden directions are `\Phi_K`-invisible through the first surviving odd order.

# Needed for promotion

Prove one of the following theorem-strength upgrades:

1. A corrected two-atom package theorem giving one-atom linearity and diagonal merger for the actual package, so that reduced-package fibers force coincidence of the full relevant package modulo a proved `\ker \Phi_K` subspace.
2. A direct odd-jet factorization theorem
   \[
   c_{2r+1}=\mathfrak c_{2r+1}(\mathcal P_{\mathrm{red}})
   \]
   for all odd orders up to the first nonzero one, or equivalently fiberwise constancy of `H_m` modulo `\Phi_K`-invisible directions through that order.

Honest verdict: I do not see a proof of the hidden-state lemma in the current draft. The sharpest supported result is an obstruction: reduced-package equality closes the canonical quotient data through order `7`, but the draft still lacks the theorem that the remaining corrected-block hidden state is `\Phi_K`-invisible up to the first surviving odd order.
