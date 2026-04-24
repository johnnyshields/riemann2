## Claim

The one-zero determinant/spectral-gap target is false as stated. For the
positive strip-edge kernel
\[
K_{\beta,\gamma}(t)
=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+\frac{\beta}{\beta^2+(2t-\gamma)^2},
\qquad 0<\beta<1,
\]
the UV-017 determinant expression
\[
\mathcal D[q]=2qq''+4q^4-3(q')^2
\]
is not positive for all \(t\). If \(\beta=1/2\), then
\(\mathcal D[K_{\beta,\gamma}]\equiv0\). If \(\beta\ne1/2\), then
\(\mathcal D[K_{\beta,\gamma}](\gamma/2)<0\) and the far tails are also
negative. The sharp positive region is only a finite annulus in
\((2t-\gamma)^2\).

Honest verdict: UV-017 cannot get same-point positivity from a one-zero
determinant positivity lemma for \(K_{\beta,\gamma}\). Any positive theorem
for the actual completed paired source must use aggregate structure beyond a
single unscaled kernel, or keep the determinant/spectral gap as an explicit
local whitening hypothesis.

## Status

rejected

## Evidence

**Proved.**

Put
\[
x=2t-\gamma,\qquad y=x^2,\qquad c=\beta(1-\beta),\qquad u=\sqrt c.
\]
Then \(0<c\le1/4\), \(y\ge0\), and
\[
K_{\beta,\gamma}(t)=Q(y)
=\frac{y+c}{h(c,y)},\qquad
h(c,y)=y^2+(1-2c)y+c^2
=(y+\beta^2)(y+(1-\beta)^2)>0.
\]
Because derivatives in \(\mathcal D\) are \(t\)-derivatives,
\[
\mathcal D[K]=16QQ_y+32yQQ_{yy}+4Q^4-48yQ_y^2.
\]
Exact denominator clearing gives
\[
\mathcal D[K_{\beta,\gamma}](t)=\frac{P(c,y)}{h(c,y)^4},
\]
where
\[
\begin{aligned}
P(c,y)
&=(48c-12)y^4+(-192c^2+48c)y^3\\
&\quad +(288c^3-264c^2+48c)y^2\\
&\quad +(-192c^4+48c^3)y+(48c^5-12c^4).
\end{aligned}
\]
The exact factorization is
\[
P(c,y)=
-12(1-4c)
\bigl(y^2+2(u-c)y+c^2\bigr)
\bigl(y^2-2(u+c)y+c^2\bigr).
\]
The first quadratic is strictly positive for \(y\ge0\). Thus:

- If \(\beta=1/2\), then \(c=1/4\) and \(P\equiv0\), so
  \(\mathcal D[K]\equiv0\). Strict positivity/nondegeneracy fails.
- If \(\beta\ne1/2\), then \(0<c<1/4\). The second quadratic has roots
  \[
  y_\pm=u^2+u\pm u\sqrt{1+2u}.
  \]
  Hence
  \[
  \mathcal D[K_{\beta,\gamma}](t)>0
  \quad\Longleftrightarrow\quad
  y_-<(2t-\gamma)^2<y_+,
  \]
  and \(\mathcal D[K]\le0\) on the complementary center/tail regions.

Two immediate counterchecks are exact:
\[
\mathcal D[K_{\beta,\gamma}](\gamma/2)
=-\frac{12(1-4c)}{c^4}
=-\frac{12(1-2\beta)^2}{\beta^4(1-\beta)^4}<0
\]
for \(\beta\ne1/2\), and
\[
\mathcal D[K_{\beta,\gamma}](t)
\sim -\frac{12(1-4c)}{(2t-\gamma)^8}
\]
in the far tails.

The saved exact-arithmetic script
`scripts/check_one_zero_determinant_gap.py` has SHA256
`B21EF132AC193F05054DED87A76C39B0CA96DD655C1FFB49DFF40EFD54C0156D`.
Relevant output:

- `P factorization over u=sqrt(c) verified: True`;
- `At y=0: D[K] = -12(1-4c)/c^4`;
- `As y -> infinity: D[K] ~ -12(1-4c)/y^4`;
- `NONPOSITIVE_GRID_HIT 1/10000 0 -119952000000000000`.

**Conditional.**

- This rejects only the unscaled one-zero kernel target requested here. It does
  not rule out a determinant gap for an aggregate completed source containing
  multiplicities, functional-equation paired duplication, other zeros, or
  explicit background/correction terms.
- If the actual paired source necessarily contributes a multiple \(\lambda K\)
  rather than \(K\), that is a distinct scaled-kernel problem. It was not used
  to rescue the present one-zero target.

**Missing.**

- A determinant/spectral-gap theorem for the actual completed paired source
  sum remains missing.
- A tail-stability theorem remains missing: adding far zeros can change
  \(q,q',q''\), and \(\mathcal D\) is nonlinear.
- The UV-017 uniform microscopic gap, whitening, freeze-rule remainder, and
  scalar-readout normalization remain open unless assumed.

## Baseline / delta

Baseline: the prior local-admissibility reduction and Sartre audit showed that
same-point positivity for the displayed UV-017 chart is exactly
\[
q>0,\qquad 2qq''+4q^4-3(q')^2>0.
\]
The next proposed sharp target was to prove this determinant gap first for the
one-zero positive strip-edge source.

Delta: this attempt rejects that one-zero route. The one-zero kernel is
positive as a source kernel but fails the determinant gap: it is degenerate on
the critical line and negative at the zero center and tails off the critical
line. The positivity problem must move to aggregate-source structure or remain
an explicit local whitening hypothesis.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:41-87`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:285-305`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:360-374`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-uv017-holomorphy-positivity-audit.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/scripts/check_uv017_local_admissibility.py`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/notes/one_zero_determinant_gap.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-192025-gap-uv017-coefficient-freeze/scripts/check_one_zero_determinant_gap.py`
- script SHA256:
  `B21EF132AC193F05054DED87A76C39B0CA96DD655C1FFB49DFF40EFD54C0156D`

## Dependencies

- Sign-audited positive strip-edge one-zero kernel convention.
- UV-017 local-admissibility reduction identifying the same-point determinant
  condition with \(q>0\) and \(\mathcal D[q]>0\).
- Exact use of \(t\)-derivatives, with \(x=2t-\gamma\). The factor \(2\) in
  \(x_t\) is included in the script and derivation.
- No assumption of GRH. The formula applies for every \(0<\beta<1\).

## Strongest objection

The counterexample is to the single unscaled kernel \(K_{\beta,\gamma}\), not
to every possible aggregate completed paired source. The actual completed
source may contain symmetric duplicate kernels, multiplicities, or additional
zero/background terms. Because \(\mathcal D\) is nonlinear, such aggregation
can change the sign. Therefore the correct negative conclusion is scoped:
one-zero positivity is false from this target alone; actual-source positivity
is still open.

## Needed for promotion

Do not promote a one-zero determinant-positivity lemma. For UV-017 promotion,
one of the following must replace it:

1. a proved determinant/spectral-gap theorem for the full completed paired
   source \(q_\chi^{\mathrm{pair}}\), including multiplicities and all local
   zero contributions;
2. a sharper aggregate model showing that the functional-equation paired or
   multiplicity-scaled zero package restores the determinant gap on the needed
   microscopic window;
3. an explicit local whitening hypothesis retaining
   \(q>0\) and \(\mathcal D[q]\ge\kappa>0\), with holomorphic whitening derived
   conditionally from that hypothesis.

The remaining UV-017 burdens also stay live: uniform pole-clearance radius,
freeze-rule remainder, and scalar-readout normalization.

## Autoresearch next step

continue: attack the scaled/symmetric aggregate kernel next. The natural
follow-up is to compute \(\mathcal D[\lambda K]\), especially \(\lambda=2\),
because a noncritical zero of a completed self-dual product may be accompanied
by its functional-equation partner, which gives the same \(K\). Decide whether
that aggregate has an exact positive factorization or its own obstruction.

verify: ask an adversarial verifier to check the \(t\)-derivative normalization
and the factorization
\[
P=-12(1-4c)(y^2+2(u-c)y+c^2)(y^2-2(u+c)y+c^2).
\]

## Ledger destination

`attempts.md` as a kept rejected route for the one-zero determinant-gap target.
`findings.md` should capture the scoped negative: the positive one-zero
strip-edge kernel fails the UV-017 same-point determinant gap; positivity must
come from aggregate structure or remain a local whitening hypothesis. `uv.md`
should keep UV-017 open and redirect the determinant subgap from one-zero
positivity to aggregate-source spectral gap or explicit hypothesis.
