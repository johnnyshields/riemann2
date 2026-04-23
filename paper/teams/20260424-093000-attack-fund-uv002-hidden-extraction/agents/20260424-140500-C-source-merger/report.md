# Claim

If the actual corrected two-atom package satisfies the exact source-level merger identities of Lemma `\ref{lem:minimal-source-level-two-point-criterion}` at the relevant output level, then the immediate formal consequence is quadratic interaction factorization, hence the local two-point exclusion route and, on the involutive fixed-shear corner under state-locality, Bottleneck B. Bottleneck C is not then a new formal corollary; it is either bypassed or else requires one extra descent statement identifying the reduced corrected package as a functorial image of that source-level package.

# Status

proved

# Evidence

Lemma `\ref{lem:minimal-source-level-two-point-criterion}` proves that swap symmetry, one-amplitude collapse, and diagonal merger imply
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2.
\]
Corollary `\ref{cor:conditional-quadratic-defect-estimate-two-point-exclusion}` then gives the quadratic defect bounds for the cubic/quintic/septic outputs and excludes close bad two-point cores on good patches.

On the exact fixed-shear involutive lane, Corollary `\ref{cor:stronger-state-local-package-collapse-fixed-shear-corner}` shows that if the corrected two-pair package is state-local in the descended transport state and satisfies the natural merger law on equal states, then the interaction remainder vanishes identically along the involutive branch. Proposition `\ref{prop:conditional-state-local-defect-closure-fixed-shear-corner}` then gives the required `O((h_1-h_2)^2)` vanishing and closes the residual corner on good patches.

By contrast, the draft states Bottleneck C as a separate provenance-sensitive package theorem: same reduced image germ at coincidence / collision-functoriality for the corrected reduced package. The current text treats this as an alternative to the source-level merger route, not as a formal consequence of it. The exact missing step is descent from the source-level corrected package to the reduced blow-up package with exceptional-divisor normalization
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]
Without that descent theorem, source-level merger alone does not formally identify the reduced exceptional-divisor trace.

# Exact refs

- `paper/proof_of_rh.tex:10794-10809`
- `paper/proof_of_rh.tex:11889-12040`
- `paper/proof_of_rh.tex:12042-12151`
- `paper/proof_of_rh.tex:12168-12189`
- `paper/proof_of_rh.tex:12513-12559`
- `paper/proof_of_rh.tex:21752-21763`
- `paper/proof_of_rh.tex:22410-22505`
- `paper/proof_of_rh.tex:24525-24536`
- `paper/proof_of_rh.tex:25011-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-69`

# Dependencies

- The actual corrected two-atom package must realize the source-level package analytically at the relevant output level.
- For Bottleneck B on the involutive branch, one also needs state-locality in the descended transport state as in Corollary `\ref{cor:stronger-state-local-package-collapse-fixed-shear-corner}`.
- To convert source-level merger into Bottleneck C itself, one needs an extra reduction/descent theorem from the source-level package to the corrected reduced package germ on the collision/cancellation blow-up.

# Strongest objection

The source-level merger identities are stated for a finite-dimensional package `\mathfrak P_2` with one-pair datum `F_h`; Bottleneck C is stated for the corrected reduced package on the exceptional divisor. The draft does not currently prove that the reduced package is a functorial image of the source-level package in a way that preserves the merger law and fixes the normalization at `\delta=0`. So C does not follow formally from merger identities alone.

# Needed for promotion

State the theorem chain explicitly as:

1. source-level merger identities for the actual corrected package;
2. Lemma `\ref{lem:minimal-source-level-two-point-criterion}`;
3. Corollary `\ref{cor:conditional-quadratic-defect-estimate-two-point-exclusion}` for the good-patch close branch;
4. if working on the residual exact fixed-shear corner, add state-locality and apply Corollary `\ref{cor:stronger-state-local-package-collapse-fixed-shear-corner}` plus Proposition `\ref{prop:conditional-state-local-defect-closure-fixed-shear-corner}`.

If the goal is Bottleneck C itself, add one more theorem: the reduction/descent functor taking the corrected source-level package to the reduced collision package and carrying diagonal merger to
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

Honest verdict: the clean implication is `merger => B/local exclusion`, not `merger => C` in the present draft. C becomes formal only after an additional descent/functoriality theorem identifying the corrected reduced package as the reduced image of the source-level merger package.
