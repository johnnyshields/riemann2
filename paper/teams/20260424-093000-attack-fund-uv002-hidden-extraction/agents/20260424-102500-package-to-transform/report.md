## Claim

The hidden extraction step for Bottleneck D reduces to one exact factorization statement. If there exists a reduced finite-core package germ map
\[
\mathcal P_{\mathrm{red}}(\core)
\]
such that the corrected finite-core transverse germ factors as
\[
H_{\core}(s)=\mathfrak H\bigl(\mathcal P_{\mathrm{red}}(\core)\bigr)(s)
\]
with \(\mathfrak H\) analytic and odd, then the first nonzero finite-core transformed scalar
\[
\Xi_{\zeta,\le H}^{(N)}
\]
is determined by \(\mathcal P_{\mathrm{red}}(\core)\). In particular, if the best current candidate reduced-\(\widehat\Psi\) package state carries this factorization, then the first surviving odd order and leading coefficient are package-determined.

The single narrowest exact blocker is therefore: prove that the full corrected odd germ \(H_{\core}\) is constant on fibers of the reduced package germ map (equivalently, two finite cores with the same reduced package germ have the same first surviving odd jet, or stronger the same full odd germ).

## Status

open

## Evidence

- On the zeta side, the extractor is already complete. The draft proves that \(H_m\) is an odd holomorphic germ, that \(\Xi_\zeta^{(N)}\) is an explicit linear functional of \(H_m\), and that the \(N\)-point operator isolates the first surviving odd coefficient through the exact surviving expansion.
- The finite-core localization result already reduces the transformed scalar to the finite core up to exponentially small error. So once \(H_{\core}\) is known from package data, \(\Xi_{\zeta,\le H}^{(N)}\) is formally determined.
- The reduced-\(\widehat\Psi\) package currently controls only quotient-level cubic/quintic/septic coincidence data. The existing package results do not identify the full corrected whitened block \(\widehat\Omega_\zeta^{\corr}\), nor its scalar projection \(H_m=\Phi_K(\widehat\Omega_\zeta^{\corr})\), from that reduced package data.
- Therefore Bottleneck D is not blocked by odd-jet extraction, but by missing fiber-invariance/factorization of \(H_{\core}\) through the reduced package germ.

## Exact refs

- `paper/proof_of_rh.tex:2214-2321` — definition of \(H_m\), odd holomorphic expansion, coefficients \(c_{2r+1}(m)\).
- `paper/proof_of_rh.tex:2953-2969` — first surviving odd coefficient localizes to a fixed finite core.
- `paper/proof_of_rh.tex:3857-4190` — \(\Xi_\zeta^{(N)}\), exact surviving expansion, finite-core localization of \(\Xi_{\zeta,\le H}^{(N)}\).
- `paper/proof_of_rh.tex:10786-10809` — order-7 closure still requires a provenance-sensitive package statement such as same reduced image germ.
- `paper/proof_of_rh.tex:11376-11671` — definition of reduced \(\widehat\Psi\) package and exact strengthened two-pair coincidence through order 7.
- `paper/proof_of_rh.tex:11996-12189` — current merger/diagonal-collapse route is a package theorem, not an extractor theorem.
- `paper/proof_of_rh.tex:12552-12555` — same reduced image germ / collision-functoriality as current package target.
- `paper/proof_of_rh.tex:22472-22529` — state-local package collapse on the involutive branch would make the residual obstruction purely relational/provenance-sensitive.
- `paper/proof_of_rh.tex:24985-25030` and `26369-26398` — endgame status: extractor side is ready, package side remains open.

## Dependencies

- A precise reduced finite-core package germ \(\mathcal P_{\mathrm{red}}\), best current candidate the reduced-\(\widehat\Psi\) package state.
- A theorem that the corrected two-atom / finite-core package descends functorially to \(\mathcal P_{\mathrm{red}}\) with diagonal collapse at coincidence.
- A fiber-invariance theorem for the corrected scalar germ: same reduced package germ \(\Rightarrow\) same \(H_{\core}\), or at minimum same first surviving odd jet.

## Strongest objection

The present reduced-\(\widehat\Psi\) datum is only a quotient-visible order-7 package. By itself it does not encode the full corrected whitening/tail information entering
\[
H_m(s)=\Phi_K\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr),
\]
so no theorem in the draft currently rules out two finite cores with the same reduced package germ but different higher odd jets of \(H_m\). Any positive Bottleneck D theorem must therefore add either full germ-level functoriality or an explicit proof that the first surviving odd jet is already package-measurable.

## Needed for promotion

1. State a package-to-transform theorem in one of the equivalent forms:
\[
H_{\core}=\mathfrak H(\mathcal P_{\mathrm{red}}),
\]
or
\[
\operatorname{ord}_{\mathrm{odd}} H_{\core},\ \text{lead}_{\mathrm{odd}}(H_{\core})
\]
are determined by \(\mathcal P_{\mathrm{red}}\).
2. Prove diagonal collapse / coincidence for the actual corrected reduced package germ.
3. Prove fiber-invariance of \(H_{\core}\) on reduced-package fibers, or a weaker first-surviving-jet version.
4. Then invoke `paper/proof_of_rh.tex:3984-4190` to identify the first nonzero \(\Xi_{\zeta,\le H}^{(N)}\) formally.

Honest verdict: there is theorem-shaped progress, but it is conditional. Bottleneck D has one exact remaining burden: not more zeta-side extraction, but a package-to-transform factorization theorem saying that the corrected odd germ \(H_{\core}\) is determined by the reduced package germ. Without that fiber-invariance statement, reduced-\(\widehat\Psi\) coincidence alone does not yet determine the first nonzero \(\Xi_{\zeta,\le H}^{(N)}\).
