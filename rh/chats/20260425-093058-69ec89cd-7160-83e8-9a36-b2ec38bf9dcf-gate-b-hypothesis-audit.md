# Gate B Hypothesis Audit

- Source: https://chatgpt.com/c/69ec89cd-7160-83e8-9a36-b2ec38bf9dcf
- Created: 2026-04-25 09:30:58 UTC
- Default model: gpt-5-5-thinking

---

## User (2026-04-25 09:30:57)

YOUR TASK: You are Agent 1

Agent 1 — Gate B hypothesis hardener

Use this agent to prevent building on a conditional theorem that later collapses.

You are auditing whether Gate B’s hypotheses are genuinely supplied by the actual corrected source model, not merely assumed as formal source-frame conventions.

Work only from the latest paper draft.

Target:
Determine whether Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven} is a theorem of the actual corrected package or still conditional on unproved source-model hypotheses.

Focus on:
- all-subset midpoint parity;
- symmetry of same-point subset coefficients;
- leading \(Y\)-middle parity;
- moving homogeneous source-frame telescoping;
- \(2\)-jet affine boundary removal;
- full Taylor source tower before ordinary-order truncation.

Tasks:
1. For each hypothesis, classify it as:
   (a) proved from the corrected block definitions,
   (b) proved only under an explicit convention,
   (c) asserted but not derived,
   (d) false or convention-dependent.
2. Check whether the tagged two-atom pre-whitening source block actually induces the homogeneous scalar-grade source tower used in Gate B.
3. Check whether affine removal is legitimate for the actual \(\mathfrak D_Q\)-scaled source variables, not just for a formal Taylor model.
4. Check whether full-tower-before-truncation creates any upper-boundary terms at ordinary order \(7\).
5. Produce exact LaTeX edits: either promote Gate B language from conditional to theorem, or sharpen the conditional wording.

---

Now, do your task as per above.

## Assistant (2026-04-25 09:30:58)

I’ll audit the named Gate B mechanisms against the draft’s actual definitions and theorem statements, then give concrete LaTeX insertions that preserve the correct logical status.

I found the key issue: the draft already phrases Gate B as a conditional raw edge-divisibility result, but several “lemmas” used by the corollary are not yet derived from the actual corrected block functor. I’m checking which are merely normalization conventions versus source-model theorems.

_Thought for 2m 6s_

## Verdict

Do **not** promote Corollary `cor:gate-b-raw-edge-divisibility-order-seven` to an unconditional theorem of the actual corrected package.

The present draft is already mostly correct in treating Gate B as **conditional raw edge-divisibility**, but the wording should be sharpened further: the hypotheses are not yet all derived from the actual tagged corrected source block and corrected-whitening transfer. This matches the handoff status: Gate B is promising but conditional, and the highest-value work is hardening its hypotheses. 

## Classification of Gate B hypotheses

| Hypothesis | Classification | Audit result |
|---|---:|---|
| Gate A aggregate closure | **(b)** | Proved under active homogeneous scalar-grade convention and third-Fréchet midpoint parity. Not unconditional source-model output. |
| all-subset midpoint parity | **(b)/(c)** | Stated as Lemma `lem:all-subset-midpoint-parity`; scoped to leading homogeneous coefficient + midpoint/Frechet convention. Not derived from the actual inverse-square-root corrected block recursion. Treat as explicit convention plus missing functorial derivation. |
| symmetry of same-point subset coefficients | **(a)/(c)** | Plausible from symmetric same-point blocks and symmetric inverse square root, but the all-subset Fréchet coefficient symmetry is stated without proof. Needs a one-paragraph derivation from \(G_\pm^{\corr}=G_\pm^{\corr,T}\) and analytic functional calculus. |
| transpose-invariance of \(\pi_{\mathfrak f_h}\) | **(a)** | This is structural, assuming the fixed-sector basis \(I,S\) and projection are as defined. Safe. |
| leading \(Y\)-middle parity | **(b)** | Proved only inside the active homogeneous scalar-grade convention. The draft correctly quarantines the ordinary matrix-output \(M^{[5]}\) route. |
| moving homogeneous source-frame telescoping | **(b)** | Algebraically proved for the formal homogeneous scalar tower, but not derived as a theorem that the actual corrected source block induces exactly that tower through whitening. |
| \(2\)-jet affine boundary removal | **(a)/(b)** | Legitimate for the actual \(\mathfrak D_Q\)-scaled holomorphic source variables: affine modes force poles in \(U_\pm,E_\pm\). But it depends on the residual source being explicitly \(2\)-jet normalized at the moving midpoint. |
| full Taylor source tower before ordinary-order truncation | **(b)/(c)** | Correct as a procedural hypothesis. It avoids an artificial upper-boundary term, but the draft has not proved that the actual corrected package functor commutes with this infinite-tower differentiation/truncation order. |

## Specific checks

### 1. Does the tagged two-atom pre-whitening block induce the Gate B homogeneous source tower?

Not yet.

`def:tagged-two-atom-prewhitening-source-block` and `lem:tagged-pair-kernel-linearity-source-block` prove **pre-whitening \(\mathcal K\)-linear additivity**:

\[
\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=
\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}.
\]

But Gate B needs more: it needs the actual corrected-whitening cross-effect to respect the homogeneous scalar-grade tower, subset-complement parity, source-motion telescoping, and full-tower-before-truncation after applying

\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]

The draft itself says the tagged block is pre-whitening and does **not** prove quotient-output package coincidence, \(B_7^{\mathfrak f}\), \(Q_{7,m}^q\), or the projector \(\Pi_{1,1}\). So Gate B remains conditional on source-model identification.

### 2. Is affine removal legitimate for actual \(\mathfrak D_Q\)-scaled variables?

Mostly yes, but it should be stated as a source-admissibility theorem, not merely a formal Taylor convention.

The strongest existing argument is in `lem:affine-boundary-removal-moving-source-frame`: for an affine perturbation \(\psi(t)=t-h\),

\[
d_\pm(z)=\frac{z^2}{Q^4}U_\pm(z),
\qquad
e_\pm(z)=\frac{z}{Q^2}E_\pm(z)
\]

would force \(U_\pm,E_\pm\) to have poles. Hence affine modes are outside the holomorphic \(\mathfrak D_Q\)-scaled source sector. That is a real source-model argument.

The missing sharpening: explicitly say this uses the residual source

\[
r(t)=f(t)-f(h)-f'(h)(t-h)
\]

or its moving-midpoint analogue. Without that normalization, affine removal is not automatic.

### 3. Does full-tower-before-truncation create upper-boundary terms at ordinary order \(7\)?

It creates them only if one truncates too early.

The identity

\[
(\partial_h\operatorname{Gr}_{g-1}r)_{\rm same}
+
(\partial_h\operatorname{Gr}_{g}r)_{\rm lower}=0
\]

means the apparent top boundary at grade \(7\) is paired with the lower part of grade \(8\). Therefore, to prove ordinary order \(7\), the source tower must include grade \(8\) before applying \(\partial_h\), then truncate. If the tower is truncated first, an artificial upper-boundary residual can appear.

So the current hypothesis is right, but it is still a hypothesis about the actual corrected source functor.

## Exact LaTeX edits

### Edit 1 — rename and sharpen the Gate B corollary

Replace:

```latex
\begin{corollary}[Gate B raw edge-divisibility through ordinary order \(7\)]
\label{cor:gate-b-raw-edge-divisibility-order-seven}
Assume:
```

with:

```latex
\begin{corollary}[Conditional Gate B raw edge-divisibility through ordinary order \(7\)]
\label{cor:gate-b-raw-edge-divisibility-order-seven}
Assume that the following source-frame hypotheses have been verified for the
actual \(\mathfrak D_Q\)-scaled corrected source model, not merely for a
formal homogeneous Taylor model:
```

Then replace the sentence after the displayed conclusion:

```latex
Equivalently,
```

with:

```latex
Under these same hypotheses, equivalently,
```

### Edit 2 — add a hypothesis-hardening audit after `rem:dependency-ledger-gate-b`

Insert immediately after `\end{remark}` for `rem:dependency-ledger-gate-b`:

```latex
\begin{remark}[Hypothesis-hardening status for Gate B]
\label{rem:gate-b-hypothesis-hardening-status}
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven} should not yet
be read as an unconditional theorem of the tagged corrected source block.
Its dependencies have the following status.

\[
\begin{array}{c|c|p{0.56\linewidth}}
\text{Input} & \text{status} & \text{meaning} \\
\hline
\text{Gate A aggregate closure}
&
\text{conditional}
&
Closed under the active homogeneous scalar-grade convention and the stated
midpoint/third-Fr\'echet parity conventions; not an unconditional consequence
of the source block alone.
\\
\text{all-subset midpoint parity}
&
\text{convention-dependent}
&
Lemma~\ref{lem:all-subset-midpoint-parity} is a leading homogeneous
midpoint-chart statement.  To use it as a source-model theorem one still
needs the functorial derivation that the actual same-point
inverse-square-root Fr\'echet subset coefficients satisfy the same
subset-complement parity.
\\
\text{same-point subset symmetry}
&
\text{partly structural}
&
Symmetry follows from symmetric corrected same-point blocks and the symmetric
analytic inverse square root, provided the Fr\'echet coefficient convention
is preserved.  The all-subset coefficient-level symmetry should be recorded
as this functional-calculus consequence, not as an independent table
assumption.
\\
\text{leading \(Y\)-middle parity}
&
\text{homogeneous-grade only}
&
Lemma~\ref{lem:leading-y-middle-parity} applies to the active homogeneous
scalar-grade convention.  It does not apply to the quarantined ordinary
matrix-output \(M^{[5]}\) convention without a separate no-double-counting
theorem against grades \(0,2,4\).
\\
\text{moving source-frame telescoping}
&
\text{formal source-tower theorem}
&
Theorem~\ref{thm:moving-homogeneous-source-frame-telescoping} proves the
algebraic cancellation for the homogeneous scalar Taylor tower.  The
remaining source-model obligation is to prove that the actual corrected
source block induces this tower through the corrected-whitening transfer.
\\
\text{\(2\)-jet affine boundary removal}
&
\text{source-admissibility}
&
Lemma~\ref{lem:affine-boundary-removal-moving-source-frame} is legitimate
for the \(\mathfrak D_Q\)-scaled holomorphic source sector: affine modes
would force poles in \(U_\pm,E_\pm\).  This depends on using residual
sources normalized by subtracting their moving midpoint affine jet.
\\
\text{full tower before truncation}
&
\text{procedural hypothesis}
&
The tower must be differentiated before ordinary-order truncation.  In
particular, the grade \(8\) lower term is included when proving ordinary
order \(7\), so no artificial upper-boundary residual is created by
premature truncation.
\end{array}
\]

Thus the corollary is a proved implication from these hypotheses, not yet a
proof that the hypotheses are forced by
Definition~\ref{def:tagged-two-atom-prewhitening-source-block} alone.
\end{remark}
```

### Edit 3 — sharpen the tagged source block scope

Replace the current `rem:scope-tagged-source-block` with:

```latex
\begin{remark}[Scope of the tagged source block]
\label{rem:scope-tagged-source-block}
The definitions and lemma above are pre-whitening statements.  They prove
tagged \(\mathcal K\)-linear additivity of the corrected source block before
the nonlinear corrected-whitening transfer
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]
They do not by themselves prove transfer-domain vanishing,
source-bidegree edge divisibility, quotient-output package coincidence,
diagonal merger, the coefficient \(B_7^{\mathfrak f}\), the quotient
\(Q_{7,m}^q\), the projector \(\Pi_{1,1}\), or the cubic
\((1,1,5)\) \(A_5^{\mathfrak f}\)-gauge theorem.

In particular, the tagged pre-whitening block does not automatically induce
the homogeneous scalar-grade source tower used in
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven}.  That
identification is a separate source-model theorem: the actual
\(\mathfrak D_Q\)-scaled corrected source variables must be shown to feed
the corrected-whitening cross-effect with the same homogeneous grades,
midpoint parities, source-motion telescoping, and full-tower-before-truncation
used in Gate~B.
\end{remark}
```

### Edit 4 — add an affine-removal caveat inside `lem:affine-boundary-removal-moving-source-frame`

After:

```latex
Thus constant and affine modes are not independent raw source inputs.
```

insert:

```latex
This statement is a source-admissibility assertion for the holomorphic
\(\mathfrak D_Q\)-scaled corrected source variables.  It is not a license to
discard lower homogeneous grades.  It uses the residual-source convention in
which the moving midpoint affine jet has already been subtracted; without
that convention an affine component would not be killed by a formal
coefficient argument alone.
```

### Edit 5 — add a full-tower warning after the proof of affine removal

Insert after the proof of `lem:affine-boundary-removal-moving-source-frame`:

```latex
\begin{remark}[No premature ordinary-order truncation]
\label{rem:no-premature-ordinary-order-truncation-gate-b}
The cancellation in
Theorem~\ref{thm:moving-homogeneous-source-frame-telescoping} is a statement
about the full moving Taylor source tower.  For ordinary order \(7\), one
must include the next homogeneous grade before differentiating: the lower
part of \(\partial_h\operatorname{Gr}_{8}r\) cancels the apparent upper
boundary coming from the same-basis derivative of
\(\operatorname{Gr}_{7}r\).  If the tower is truncated at grade \(7\) before
\(\partial_h\) is applied, this cancellation is artificially destroyed.

Thus ``through ordinary order \(7\)'' means: differentiate the full
homogeneous source tower first, perform the adjacent-grade telescoping, and
only then discard ordinary powers above \(7\).
\end{remark}
```

## Bottom line

Gate B is a valid **conditional implication** in the draft. It is not yet a theorem of the actual corrected package unless the draft adds a source-model theorem connecting the tagged pre-whitening block to the homogeneous scalar-grade tower after corrected whitening. The safest paper language is therefore conditional, not promoted.
## User (2026-04-25 09:51:20)

Updated paper draft attached.

Now, here's your next instruction. First, the background:

You are working on a live RH proof attempt from the latest paper draft. Work **only from the latest draft**, plus this prompt. Do not propose cosmetic edits unless they expose a mathematical obstruction or close a real dependency.

Current accepted posture:

[
\boxed{\text{Gate A is aggregate-closed under the active homogeneous scalar-grade convention.}}
]

[
\boxed{\text{Gate B is conditionally closed through ordinary order }7.}
]

The main unfinished mathematical targets are:

[
\boxed{\text{actual-source realization of Gate B hypotheses}}
]

[
\boxed{\text{the }Z_j[M_A],Z_j[M_C]\text{ connection tables}}
]

[
\boxed{\Phi_K\text{-visible package-to-transform state-locality}}
]

[
\boxed{\text{quotient-valued diagonal merger / no }\kappa\text{-slope leakage}}
]

[
\boxed{\text{finite-core lower transfer beyond the pair-like branch}}
]

Do not reopen old coefficient hunting unless it attacks one of these five targets.

Key guardrails:

1. Gate B is raw edge-divisibility, not post-edge quotient compatibility:

[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})*{\rm mix}C*{\mathcal W}^{\rm raw}=0.
]

2. (Z_j[M]), not (B_j[M]), enters the connection formula:

[
q_{\mathrm{conn},7}[M]
======================

\sum_{i=1}^{7}\omega_m(Z_{7-i}[M],A_i).
]

3. Quotient equality does **not** imply (\Phi_K)-visible hidden-state equality:

[
A_7^{\mathfrak f}\sim A_7^{\mathfrak f}+\chi A_5^{\mathfrak f},
\qquad
\Phi_K(\chi A_5^{\mathfrak f})=2\chi v_5.
]

4. Atom-swap symmetry does **not** force (\kappa\mapsto-\kappa) on the exceptional divisor.

5. The final contradiction is currently pair-like/asymptotic. Non-pair-like finite-core closure remains open.

Your output should be mathematical: prove, reduce, compute, or produce a formal countermodel. If you cannot close the target, isolate the exact missing lemma in theorem-ready form.

---

# Agent 1 — Actual-source realization of Gate B

```text
You are attacking the actual-source realization problem behind Gate B.

Goal:
Upgrade Gate B from a conditional formal homogeneous-source implication to a theorem of the actual \(\mathfrak D_Q\)-scaled corrected source package, or isolate the exact obstruction.

Work from the latest draft only.

Current issue:
Gate B assumes the following source-frame hypotheses:
\[
\text{all-subset midpoint parity},
\quad
\text{leading \(Y\)-middle parity},
\quad
\text{moving source-frame telescoping},
\quad
\text{\(2\)-jet affine-boundary removal},
\quad
\text{full tower before truncation}.
\]
But these are not yet fully derived from the actual tagged corrected source block after the nonlinear whitening map
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]

Target theorem:
Prove or reduce the following.

For every actual admissible \(\mathfrak D_Q\)-scaled corrected source contribution entering
\[
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\]
through ordinary order \(7\), its edge coefficient is represented by the homogeneous moving Taylor source tower satisfying the Gate B hypotheses.

Tasks:
1. Start from `def:tagged-two-atom-prewhitening-source-block` and `lem:tagged-pair-kernel-linearity-source-block`.
2. Trace exactly how the actual source variables enter \(G_-,N,G_+\) and then \(G_-^{-1/2}NG_+^{-1/2}\).
3. Determine whether analytic functional calculus for \(G_\pm^{-1/2}\) preserves the labelled subset symmetries needed for all-subset midpoint parity.
4. Prove or refute that same-point Fréchet coefficients satisfy the required subset-complement parity after whitening.
5. Prove or refute that moving source-frame telescoping survives the nonlinear whitening transfer.
6. Check whether any admissible source component can produce an unmodelled term of the form
\[
a_1\delta z^7U,\qquad U\in\mathfrak f_h,
\]
not captured by the formal homogeneous tower.
7. Treat \(2\)-jet affine-boundary removal carefully: show it follows from holomorphic \(\mathfrak D_Q\)-scaled source admissibility, not merely from convention.

Deliverable:
Either:
- a proof of actual-source realization for Gate B through ordinary order \(7\), or
- a minimal counterexample / missing theorem stating exactly which source component is not controlled.

Do not:
- re-audit Gate A numerically;
- use post-edge quotient compatibility to prove raw edge-divisibility;
- treat lower shadows \(0,2,4\) as discarded baseline data.
```

## Assistant (2026-04-25 09:52:02)

The updated draft has absorbed the previous conditional-status edits. The remaining question is narrower: whether the actual \(\mathfrak D_Q\)-scaled variables force the formal homogeneous tower after whitening.

_Thought for 2m 30s_

## Result

I cannot upgrade Gate B to an unconditional theorem of the actual corrected package from the latest draft.

The draft now correctly states Gate B as a conditional raw edge-divisibility theorem. The remaining gap is not the formal Gate B cancellation; it is the identification

\[
C_{\mathcal W,\actual}^{\rm raw}
\equiv
C_{\mathcal W,\mathrm{tower}}^{\rm raw}
\quad
\text{through }[z^7][\delta^1]\pi_{\mathfrak f_h}(1-\Pi_{1,1})_{\rm mix}.
\]

Equivalently, the exact obstruction is

\[
\boxed{
\Theta_7^{\actual}
:=
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
C_{\mathcal W,\actual}^{\rm raw}
-
C_{\mathcal W,\mathrm{tower}}^{\rm raw}
\right).
}
\]

The existing Gate B proof shows

\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W,\mathrm{tower}}^{\rm raw}
=0.
\]

So the actual-source realization theorem is exactly:

\[
\boxed{\Theta_7^{\actual}=0.}
\]

This is not proved in the draft. The handoff correctly flags Gate B as conditionally closed and warns that the hypotheses must be attacked directly rather than replaced by post-edge quotient compatibility. 

---

## What can be proved from the current draft

### 1. Functional calculus does preserve subset parity, once endpoint source parity is supplied

The nonlinear whitening map itself is not the enemy. Suppose the actual same-point source block satisfies, for every homogeneous source label \(g\),

\[
A_+^{[g]}=(-1)^g A_-^{[g]},
\qquad
(A_\pm^{[g]})^T=A_\pm^{[g]},
\]

in the midpoint Taylor/Frechet convention used by the draft.

Let

\[
F(G)=G^{-1/2}.
\]

Since \(F\) is analytic on the good patch, its Taylor coefficients are multilinear Frechet coefficients. For a labelled subset \(K\),

\[
L_K^- :=
[\epsilon_K]\,
F\!\left(G_-^{(0)}+\sum_{i\in K}\epsilon_i A_-^{[g_i]}\right),
\]

\[
R_K^+ :=
[\epsilon_K]\,
F\!\left(G_+^{(0)}+\sum_{i\in K}\epsilon_i A_+^{[g_i]}\right).
\]

Using \(G_+^{(0)}=G_-^{(0)}\) in the midpoint fiber and multilinearity,

\[
R_K^+
=
[\epsilon_K]\,
F\!\left(G_-^{(0)}+\sum_{i\in K}\epsilon_i(-1)^{g_i}A_-^{[g_i]}\right)
=
(-1)^{|K|}L_K^-.
\]

Thus the all-subset midpoint parity follows from actual endpoint parity of the pre-whitening same-point source block.

Also, if the baseline and all \(A_\pm^{[g]}\) are symmetric, then the formal matrix inside \(F\) is symmetric, hence \(F\) is symmetric, hence every Taylor coefficient is symmetric:

\[
(L_K^-)^T=L_K^-,
\qquad
(R_K^+)^T=R_K^+.
\]

So same-point subset symmetry is not an independent obstruction once actual endpoint parity is proven.

### 2. Moving source-frame telescoping survives whitening if it holds at the actual source-block level

The nonlinear whitening transfer expands into multilinear transfer tensors

\[
\mathcal T_d(X_1,\ldots,X_d).
\]

If the actual source block satisfies the adjacent-grade identity

\[
X_{\mathrm{same}}^{[g-1]}
+
X_{\mathrm{lower}}^{[g]}
=0
\]

as an equality of actual source-block inputs, then for every transfer slot,

\[
\mathcal T_d(\ldots,X_{\mathrm{same}}^{[g-1]},\ldots)
+
\mathcal T_d(\ldots,X_{\mathrm{lower}}^{[g]},\ldots)
=0.
\]

So the nonlinear whitening map does not break telescoping. The missing point is earlier: the draft has proved the telescoping identity for the formal scalar tower

\[
\operatorname{Gr}_g r
=
\frac{r^{(g+2)}(h)}{(g+2)!}(t-h)^{g+2},
\]

but has not yet proved that the actual corrected source block sends this tower functorially into the same \(X^{[g]}\)-tower through ordinary order \(7\).

### 3. \(2\)-jet affine-boundary removal is genuinely actual-source, not merely conventional

This part is solid.

For a constant source \(\psi(t)=c\),

\[
d_\pm(z)=c.
\]

But admissibility requires

\[
d_\pm(z)=\frac{z^2}{Q^4}U_\pm(z)
\]

with \(U_\pm\) holomorphic. Thus \(U_\pm\sim cQ^4/z^2\), a pole unless \(c=0\).

For an affine source \(\psi(t)=b(t-h)\),

\[
\psi(t_\pm)=\pm\frac{bz}{2Q^2},
\qquad
\psi'(t_\pm)=b.
\]

Then

\[
d_\pm(z)=\frac{z^2}{Q^4}U_\pm(z)
\]

would force \(U_\pm\sim Q^2/z\), and

\[
e_\pm(z)=\frac{z}{Q^2}E_\pm(z)
\]

would force \(E_\pm\sim Q^2/z\). Again these are poles.

Therefore holomorphic \(\mathfrak D_Q\)-scaled admissibility genuinely excludes constant and affine modes. The tower starts at grade \(0\), i.e. second derivative source data.

---

## What remains unproved

The unresolved issue is not functional calculus. It is the actual-source-to-tower identification.

The draft proves only the tagged pre-whitening \(\mathcal K\)-linear statement:

\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=
\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}.
\]

But Gate B needs more. It needs every actual admissible contribution entering

\[
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\]

through ordinary order \(7\) to be represented by the homogeneous moving Taylor tower, including all contributions generated by:

\[
G_-^{\corr},\qquad
N^{\corr},\qquad
G_+^{\corr},
\qquad
G_-^{-1/2}NG_+^{-1/2}.
\]

The current draft has not proved that the \(\mathcal K\)-degree \(\ge2\) pre-whitening remainders either:

\[
\text{(i) obey the same homogeneous source-frame parity/telescoping,}
\]

or

\[
\text{(ii) are too high-order to contribute to }[z^7][\delta^1],
\]

or

\[
\text{(iii) vanish after }(1-\Pi_{1,1})_{\rm mix}\pi_{\mathfrak f_h}.
\]

That is the live obstruction.

---

## Minimal formal countermodel to the current implication

The following is not a counterexample to the actual formula; it is a countermodel to the logical implication

\[
\text{tagged pre-whitening linearity}
\Longrightarrow
\text{actual Gate B source realization}.
\]

Let the same-point source block satisfy tagged additivity, but add a holomorphic same-point source component in grade \(g\):

\[
A_+^{[g]}
=
(-1)^gA_-^{[g]}+\varepsilon K,
\qquad
K^T=K,
\qquad
\varepsilon\ne0,
\]

with \(K\) chosen so that a fixed-sector projection of a corresponding transfer placement is nonzero. This does not violate tagged \(\mathcal K\)-linear additivity; it only violates midpoint endpoint parity.

Then for a labelled total-grade \(7\) multiset \(J\), the subset-complement pair

\[
I
\longleftrightarrow
J\setminus I
\]

no longer gives opposite transposed terms. The paired contribution becomes

\[
\pi_{\mathfrak f_h}
\left(
L_I^-N_0R_{J\setminus I}^+
+
L_{J\setminus I}^-N_0R_I^+
\right),
\]

and the \(\varepsilon K\)-defect contributes generically nonzero fixed-sector mass. Thus an unmodelled term

\[
a_1\delta z^7U,
\qquad
U\in\mathfrak f_h,
\]

can survive unless actual endpoint parity is proved.

So the present draft cannot promote Gate B from conditional to actual-source theorem merely from `lem:tagged-pair-kernel-linearity-source-block`.

---

## The exact missing lemma

This is the theorem-ready target.

```latex
\begin{theorem}[Actual-source realization of the Gate B source frame]
\label{thm:actual-source-realization-gate-b}
Let \(r\) be an admissible \(\mathfrak D_Q\)-scaled corrected source
input, holomorphic in the endpoint variable and \(2\)-jet normalized at the
moving midpoint \(h\):
\[
r(h)=0,\qquad r'(h)=0.
\]
Let
\[
\mathcal B_h(r)
=
(G_-^{\corr}(r),N^{\corr}(r),G_+^{\corr}(r))
\]
be the actual corrected source block, and let
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}.
\]

Through ordinary order \(7\), after applying
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix},
\]
the actual corrected-whitening cross-effect
\(C_{\mathcal W,\actual}^{\rm raw}\) is represented by the moving
homogeneous scalar source tower
\[
\operatorname{Gr}_g r
=
\frac{r^{(g+2)}(h)}{(g+2)!}(t-h)^{g+2},
\qquad
g\ge0,
\]
with the following properties.

\begin{enumerate}
\item \textbf{Same-point endpoint parity.}
For every labelled homogeneous subset \(K\),
\[
R_K^+=(-1)^{|K|}L_K^-.
\]

\item \textbf{Same-point symmetry.}
For every labelled homogeneous subset \(K\),
\[
(L_K^-)^T=L_K^-,
\qquad
(R_K^+)^T=R_K^+.
\]

\item \textbf{Leading mixed-middle parity.}
The leading homogeneous mixed-middle coefficient satisfies
\[
Y_{\lead}^{[a]}=0\quad(a\ \mathrm{odd}),
\qquad
(Y_{\lead}^{[a]})^T=Y_{\lead}^{[a]}\quad(a\ \mathrm{even}).
\]

\item \textbf{Moving source-frame telescoping.}
The actual source-block image of the homogeneous tower satisfies
\[
X_{\mathrm{same}}^{[g-1]}+
X_{\mathrm{lower}}^{[g]}=0
\qquad(g\ge1)
\]
slotwise before symmetrization.

\item \textbf{Affine boundary removal.}
The only lower boundary produced by differentiating
\(\operatorname{Gr}_0 r\) is affine and is killed by the source-frame
projection \(\Pi_{\ge2,h}\).

\item \textbf{Full tower before truncation.}
The source tower is differentiated before ordinary-order truncation; in
particular the grade \(8\) lower term is retained when proving ordinary
order \(7\).
\end{enumerate}

Equivalently,
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
C_{\mathcal W,\actual}^{\rm raw}
-
C_{\mathcal W,\mathrm{tower}}^{\rm raw}
\right)
=0.
\]
\end{theorem}
```

And then the promotion theorem is immediate:

```latex
\begin{corollary}[Gate B as an actual-source theorem]
\label{cor:gate-b-actual-source}
Assume Theorem~\ref{thm:actual-source-realization-gate-b}.  Then
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W,\actual}^{\rm raw}
=0.
\]
Equivalently,
\[
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W,\actual}^{\rm raw}
=
O(a_1\delta^2)
\]
through ordinary order \(7\) in fixed sector.
\end{corollary}

\begin{proof}
By Theorem~\ref{thm:actual-source-realization-gate-b}, the actual
cross-effect and the homogeneous-tower cross-effect have the same
\([z^7][\delta^1]\pi_{\mathfrak f_h}(1-\Pi_{1,1})_{\rm mix}\)-coefficient.
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven} proves that
this coefficient vanishes for the homogeneous-tower representative under
the listed Gate B source-frame hypotheses.  Hence it vanishes for the
actual corrected source package.
\end{proof}
```

## Recommended paper insertion

Add this after `rem:gate-b-source-model-hardening`:

```latex
\begin{remark}[Exact remaining obstruction to actual-source Gate B]
\label{rem:exact-obstruction-actual-source-gate-b}
The remaining obstruction to promoting
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven} is the
actual-source defect
\[
\Theta_7^{\actual}
:=
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
C_{\mathcal W,\actual}^{\rm raw}
-
C_{\mathcal W,\mathrm{tower}}^{\rm raw}
\right).
\]
The formal Gate B argument proves the vanishing of the homogeneous-tower
term.  Therefore Gate B is a theorem of the actual corrected package
through ordinary order \(7\) if and only if
\[
\Theta_7^{\actual}=0.
\]

The tagged pre-whitening source lemma proves only
\(\mathcal K\)-linear additivity before the nonlinear whitening transfer.
It does not by itself prove that all higher \(\mathcal K\)-degree
pre-whitening source remainders, nor their images under
\(G_-^{-1/2}NG_+^{-1/2}\), are represented by the same moving homogeneous
source tower with the same endpoint parity, \(Y\)-middle parity, source
telescoping, affine-boundary removal, and full-tower-before-truncation.
That identification is precisely the missing actual-source realization
theorem.
\end{remark}
```

## Bottom line

The actual-source Gate B upgrade is reduced to a single sharp theorem:

\[
\boxed{\Theta_7^{\actual}=0.}
\]

The draft already proves that the formal homogeneous tower has zero Gate B edge coefficient. What remains is to prove that the actual \(\mathfrak D_Q\)-scaled corrected block has no additional source component at \([z^7][\delta^1]\) outside that tower.
## User (2026-04-25 10:04:22)

You are Agent 1. Read the attached command and do you task.

## Assistant (2026-04-25 10:06:19)

_Thought for 1m 54s_

## Agent 1 result: actual-source Gate B is **not closed** from the current draft

I cannot prove

\[
\Theta_7^{\actual}=0.
\]

The first live obstruction is not in the formal homogeneous Gate B mechanism. It is already present **before whitening**, inside the actual corrected same-point block, from the nonlinear \(q^3\) term in

\[
G_{\pm}^{\corr}.
\]

The attached command asks Agent 1 to attack exactly this defect, namely to prove or refute that the actual corrected source cross-effect differs from the homogeneous-tower representative by zero after

\[
[z^7][\delta^1]\pi_{\mathfrak f_h}(1-\Pi_{1,1})_{\rm mix}.
\]

It also specifically requires classifying \(\mathcal K\)-degree \(\ge2\) remainders and finding the first live defect if closure fails. 

The conclusion is:

\[
\boxed{
\Theta_7^{\actual}
\text{ is not proved zero; the first uncontrolled defect is a cubic same-point source-block term.}
}
\]

---

# 1. Actual corrected source contributions through ordinary order \(7\)

The actual corrected blocks use

\[
q_\pm=q_{0,\pm}+d_\pm,\qquad
q_\pm'=q_{0,\pm}'+e_\pm,\qquad
q_\pm''=q_{0,\pm}''+g_\pm,
\]

with

\[
d_\pm=\frac{z^2}{Q^4}U_\pm,\qquad
e_\pm=\frac{z}{Q^2}E_\pm,\qquad
g_\pm=G_\pm,\qquad
\eta=\frac{z^3}{Q^6}V.
\]

For two atoms,

\[
d_\pm^{(2)}=a_1d_{1,\pm}+a_2d_{2,\pm},
\]

and similarly for \(e,g,\eta\).

The corrected same-point block is

\[
G_{\pm}^{\corr}
=
\frac1\pi
\begin{pmatrix}
2q_\pm & \frac12 q_\pm'\\[0.8ex]
\frac12 q_\pm' &
\frac1{12}\left(q_\pm''+2q_\pm^3\right)
\end{pmatrix}.
\]

Therefore its source contributions separate as follows.

## A. \(\mathcal K\)-linear tower terms

These are the terms used by the formal homogeneous Gate B tower:

\[
(1,1):\quad 2d_\pm,
\]

\[
(1,2),(2,1):\quad \frac12 e_\pm,
\]

\[
(2,2):\quad g_\pm+6q_{0,\pm}^2d_\pm
\]

up to the common factor \(1/(12\pi)\) in the \((2,2)\)-entry.

These are represented by the homogeneous moving Taylor source tower.

## B. \(\mathcal K\)-degree \(\ge2\) same-point remainders

From

\[
(q_0+d)^3-q_0^3
=
3q_0^2d+3q_0d^2+d^3,
\]

the nonlinear same-point source remainders are

\[
\boxed{
\frac{1}{2\pi}q_{0,\pm}d_\pm^2\,E_{22}
}
\]

and

\[
\boxed{
\frac{1}{6\pi}d_\pm^3\,E_{22}
}
\]

before two-atom cross-effect subtraction.

After the raw two-atom cross-effect

\[
\mathcal B_2-\mathcal B_1(a_1,h_1)-\mathcal B_1(a_2,h_2)+\mathcal B_0,
\]

the same-point nonlinear residue is

\[
\boxed{
\Delta G_{\pm,\mathrm{quad}}^{\actual}
=
\frac1\pi q_{0,\pm}
\,a_1a_2 d_{1,\pm}d_{2,\pm}E_{22}
}
\]

and

\[
\boxed{
\Delta G_{\pm,\mathrm{cub}}^{\actual}
=
\frac1{2\pi}
\left(
a_1^2a_2d_{1,\pm}^2d_{2,\pm}
+
a_1a_2^2d_{1,\pm}d_{2,\pm}^2
\right)E_{22}.
}
\]

The quadratic term has source bidegree \((1,1)\) and is killed by \((1-\Pi_{1,1})_{\rm mix}\) if it appears alone.

The cubic term has source bidegrees

\[
(2,1),\qquad (1,2),
\]

so it is **not** killed by \((1-\Pi_{1,1})_{\rm mix}\).

This is the first live defect.

## C. \(\mathcal K\)-degree \(\ge2\) mixed-block remainders

The mixed block has Taylor remainders in

\[
(d_-,d_+,\eta).
\]

These include terms of schematic type

\[
d_-d_+,\qquad d_\pm\eta,\qquad \eta^2,
\qquad
d_-d_+\eta,\qquad d_\pm\eta^2,\qquad \eta^3,\ldots
\]

After two-atom subtraction, bidegrees \((1,1)\) are killed directly by \((1-\Pi_{1,1})_{\rm mix}\), but bidegrees

\[
(2,1),(1,2),(2,2),\ldots
\]

are not automatically killed. These mixed-block nonlinear remainders are also not yet represented by the formal homogeneous tower.

However, the **first clean explicit obstruction** is already the same-point cubic term above, because it is algebraically visible and does not require reconstructing the full mixed \(N^{\corr}\) Taylor table.

## D. Source-motion terms

The formal source-motion identity

\[
(\partial_h\operatorname{Gr}_{g-1}r)_{\rm same}
+
(\partial_h\operatorname{Gr}_g r)_{\rm lower}
=0
\]

applies to a **linear scalar tower**.

It does not automatically apply to nonlinear block terms such as

\[
d_{1,\pm}^2d_{2,\pm}.
\]

For example,

\[
\partial_h(d_1^2d_2)
=
2d_1(\partial_hd_1)d_2+d_1^2(\partial_hd_2),
\]

and this is not one labelled scalar source slot satisfying the adjacent-grade telescoping identity. It is a product-rule tower. The draft does not prove product-rule telescoping for actual nonlinear block remainders.

## E. Affine-boundary terms

Affine removal is solid for the **linear residual source variables**:

\[
r(h)=r'(h)=0.
\]

Thus constant and affine modes are not admissible holomorphic \(\mathfrak D_Q\)-scaled source variables.

But this does not remove the cubic same-point defect, since

\[
d_i=\frac{z^2}{Q^4}U_i
\]

is already \(2\)-jet normalized. The product

\[
d_1^2d_2
\]

is not affine; it starts at order \(z^6\). Therefore affine-boundary removal does not kill it.

---

# 2. The first live actual-source defect

Define

\[
P_{\pm}^{(2,1)}
:=
\frac{1}{2\pi}
a_1^2a_2d_{1,\pm}^2d_{2,\pm}E_{22},
\]

\[
P_{\pm}^{(1,2)}
:=
\frac{1}{2\pi}
a_1a_2^2d_{1,\pm}d_{2,\pm}^2E_{22}.
\]

Then the actual same-point block contains

\[
P_{\pm}^{(2,1)}+P_{\pm}^{(1,2)}
\]

inside \(G_\pm^{\corr}\), but the homogeneous tower model used in the Gate B proof does not include it as a source-linear input.

Under whitening, the first-order response of

\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}
\]

to this same-point defect is

\[
\mathcal D_-
=
D(G_-^{-1/2})_{G_-^{(0)}}[P_-]\,
N_0\,R_0,
\]

and

\[
\mathcal D_+
=
L_0\,N_0\,
D(G_+^{-1/2})_{G_+^{(0)}}[P_+],
\]

where

\[
P_\pm=P_\pm^{(2,1)}+P_\pm^{(1,2)}.
\]

So the explicit actual-source defect contains

\[
\boxed{
\Theta_{7,\mathrm{same}}^{\actual}
=
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right).
}
\]

This term is:

\[
\boxed{\text{not represented by the formal homogeneous source-linear tower,}}
\]

\[
\boxed{\text{not removed by }\Pi_{1,1},}
\]

\[
\boxed{\text{not affine,}}
\]

\[
\boxed{\text{not too high order, since }d_1^2d_2\sim z^6\text{ and }[z^7]\text{ can read a first baseline coefficient.}}
\]

Thus it is live unless a new nonlinear-source cancellation theorem is proved.

---

# 3. Why endpoint parity does not close this defect

For the linear homogeneous tower, endpoint parity is

\[
A_+^{[g]}=(-1)^gA_-^{[g]}.
\]

For \(d\)-variables,

\[
d_\pm^{[g]}\sim (\pm z)^{g+2},
\]

so

\[
d_+^{[g]}=(-1)^g d_-^{[g]}.
\]

For the cubic product,

\[
d_{1,+}^{[g_1]}d_{1,+}^{[g_2]}d_{2,+}^{[g_3]}
=
(-1)^{g_1+g_2+g_3}
d_{1,-}^{[g_1]}d_{1,-}^{[g_2]}d_{2,-}^{[g_3]}.
\]

So endpoint parity itself **does extend multiplicatively**.

But that is insufficient. The Gate B cancellation needs the term to enter the labelled subset-complement transfer calculus as a collection of source-linear slots. Here it enters as a **single nonlinear same-point block insertion** of bidegree \((2,1)\) or \((1,2)\). The existing all-subset proof does not pair this object with a complement term inside the formal source-linear transfer expansion.

In other words:

\[
\boxed{
\text{parity survives, but the transfer-combinatorics model changes.}
}
\]

The draft proves parity for source-linear Fréchet slots. It does not prove cancellation for nonlinear block-source slots such as \(d_1^2d_2E_{22}\).

---

# 4. Why moving source-frame telescoping does not close it

For a scalar homogeneous source,

\[
\operatorname{Gr}_g r
=
\frac{r^{(g+2)}(h)}{(g+2)!}(t-h)^{g+2},
\]

the draft’s telescoping identity is

\[
(\partial_h\operatorname{Gr}_{g-1}r)_{\rm same}
+
(\partial_h\operatorname{Gr}_g r)_{\rm lower}
=0.
\]

But for the actual cubic same-point defect,

\[
P^{(2,1)}\sim d_1^2d_2,
\]

one needs a product-tower identity of the form

\[
\partial_h
\left(
\operatorname{Gr}_{g_1}r_1
\operatorname{Gr}_{g_2}r_1
\operatorname{Gr}_{g_3}r_2
\right)
\]

telescoping against adjacent nonlinear product grades.

That theorem is not in the draft.

So the existing source-frame telescoping proves

\[
\Theta_{7,\mathrm{linear\ tower}}=0,
\]

not

\[
\Theta_{7,\mathrm{nonlinear\ source\ block}}=0.
\]

---

# 5. Classification of \(\mathcal K\)-degree \(\ge2\) remainders

| Remainder type | Example | Bidegree | Status |
|---|---:|---:|---|
| Same-point quadratic \(q_0d_1d_2\) | \(q_0a_1a_2d_{1,\pm}d_{2,\pm}E_{22}\) | \((1,1)\) | Killed if isolated by \((1-\Pi_{1,1})_{\rm mix}\), but can re-enter when combined with extra linear slots in whitening. |
| Same-point cubic | \(a_1^2a_2d_{1,\pm}^2d_{2,\pm}E_{22}\) | \((2,1)\) | **Live defect.** |
| Same-point cubic mirror | \(a_1a_2^2d_{1,\pm}d_{2,\pm}^2E_{22}\) | \((1,2)\) | **Live defect.** |
| Mixed quadratic | \(d_{1,-}d_{2,+}\), \(\eta_1\eta_2\), \(d_i\eta_j\) | usually \((1,1)\) | Killed if isolated; not controlled once inserted with additional source-linear slots. |
| Mixed cubic | \(d_id_j\eta_k\), \(d_i\eta_j\eta_k\), \(\eta_i\eta_j\eta_k\) | \((2,1),(1,2)\), etc. | Potentially live; not yet tabled. |
| Product source-motion | \(\partial_h(d_1^2d_2)\) | \((2,1)\) | Not controlled by scalar telescoping. |
| Affine boundary | constant/affine \(r\) | — | Removed by holomorphic \(\mathfrak D_Q\)-admissibility. |

---

# 6. Minimal countermodel to the current actual-source implication

The current Gate B implication would be valid if all actual nonlinear source-block remainders were either killed or represented by the formal homogeneous tower.

But the same-point cubic term gives a formal countermodel.

Let \(E_{22}\) be inserted as above and assume a generic baseline such that

\[
[z^1]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[E_{22}]N_0R_0
+
L_0N_0D(G_+^{-1/2})[E_{22}]
\right)
\ne0.
\]

Take grade-zero residuals, so

\[
d_{i,\pm}=c_i z^2+O(z^3).
\]

Then

\[
d_{1,\pm}^2d_{2,\pm}
=
c_1^2c_2z^6+O(z^7).
\]

Therefore the defect contributes to \([z^7]\) through the first baseline coefficient. Since its bidegree is \((2,1)\), it survives

\[
(1-\Pi_{1,1})_{\rm mix}.
\]

On the collision chart,

\[
a_2=-a_1(1+\kappa\delta),
\]

the amplitude dependence of

\[
a_1^2a_2,\qquad a_1a_2^2
\]

also produces a \(\delta^1\)-coefficient unless a separate weighted bidegree cancellation is proved.

Thus the current draft does not force

\[
\Theta_7^{\actual}=0.
\]

The obstruction is not hypothetical; it is generated by the actual \(q^3\) term in \(G_\pm^{\corr}\).

---

# 7. Exact missing theorem

To close Agent 1’s target, the draft needs a nonlinear-source realization theorem, not merely source-linear tagged additivity.

```latex
\begin{theorem}[Nonlinear actual-source realization for Gate B]
\label{thm:nonlinear-actual-source-realization-gate-b}
Let
\[
C_{\mathcal W,\actual}^{\rm raw}
\]
be the raw corrected-whitening cross-effect formed from the actual
corrected source blocks, including all nonlinear source-block terms in
\(G_\pm^{\corr}\) and \(N^{\corr}\).  Let
\[
C_{\mathcal W,\tower}^{\rm raw}
\]
be the homogeneous moving Taylor tower representative used in
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven}.  Then
through ordinary order \(7\),
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
C_{\mathcal W,\actual}^{\rm raw}
-
C_{\mathcal W,\tower}^{\rm raw}
\right)=0.
\]

Equivalently, every nonlinear \(\mathcal K\)-degree \(\ge2\) source-block
remainder, including the same-point terms
\[
q_{0,\pm}d_{1,\pm}d_{2,\pm}E_{22},
\qquad
d_{1,\pm}^2d_{2,\pm}E_{22},
\qquad
d_{1,\pm}d_{2,\pm}^2E_{22},
\]
and the mixed-block Taylor remainders in
\[
(d_-,d_+,\eta),
\]
is either:
\begin{enumerate}
\item represented by the same moving homogeneous source tower;
\item too high-order to contribute to
\([z^7][\delta^1]\);
\item killed by
\((1-\Pi_{1,1})_{\rm mix}\pi_{\mathfrak f_h}\);
or
\item cancelled by a nonlinear product-tower analogue of moving
source-frame telescoping.
\end{enumerate}
\end{theorem}
```

Without this theorem, Gate B remains actual-source conditional.

---

# 8. Recommended immediate attack

The next Agent 1 subproblem should be:

\[
\boxed{
\text{Evaluate the fixed-sector projection of the same-point cubic defect}
}
\]

namely

\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right).
\]

If this expression vanishes by transpose/subset symmetry, Gate B may still be rescued. If it does not, the actual-source theorem requires an explicit counterterm or an enlarged source tower including nonlinear block-source products.

Current status:

\[
\boxed{
\Theta_7^{\actual}=0
\text{ is reduced to a new nonlinear-source cancellation theorem, and the first live term is }
d_1^2d_2+d_1d_2^2
\text{ in }G_\pm^{\corr}_{22}.
}
\]
## User (2026-04-25 10:08:07)

ok attack that subproblem

## Assistant (2026-04-25 10:08:09)

I’ll focus on the explicit same-point cubic defect in \(G_\pm^{\corr}_{22}\): derive its endpoint parity, push it through the first Fréchet response of \(G^{-1/2}\), and see whether fixed-sector projection at \([z^7][\delta^1]\) is forced to vanish or remains live.

The cubic defect is not automatically fatal. Its product parity is multiplicative, so the left/right insertion has the same subset-complement shape as a one-slot transfer if the cubic product is treated as a composite homogeneous source slot. The decisive issue is its effective homogeneous grade at the \([z^7]\) edge.

_Thought for 2m 31s_

## Result

The specific subproblem

\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right)
\]

**vanishes**.

So the same-point cubic defect

\[
d_1^2d_2+d_1d_2^2
\]

is **not** the first live actual-source obstruction at the single-insertion level. It is killed by the same endpoint-swap / transpose-invariant fixed-sector mechanism, not by \(\Pi_{1,1}\), not by affine removal, and not by source-tower telescoping. The attached command’s target remains \(\Theta_7^{\actual}=0\), but this particular candidate defect is eliminated. 

---

# 1. The cubic same-point defect

From

\[
G_{\pm,22}^{\corr}
=
\frac1{12\pi}\left(q_\pm''+2q_\pm^3\right),
\]

write

\[
q_\pm=q_{0,\pm}+d_\pm.
\]

The cubic part contributes

\[
\frac1{6\pi}d_\pm^3.
\]

For two atoms,

\[
d_\pm=a_1d_{1,\pm}+a_2d_{2,\pm}.
\]

After subtracting the one-atom blocks, the genuinely mixed cubic same-point defect is

\[
P_\pm
=
\frac1{2\pi}
\left(
a_1^2a_2d_{1,\pm}^2d_{2,\pm}
+
a_1a_2^2d_{1,\pm}d_{2,\pm}^2
\right)E_{22},
\]

where

\[
E_{22}=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]

This term has source bidegrees \((2,1)\) and \((1,2)\), so it is not killed by \((1-\Pi_{1,1})_{\rm mix}\).

---

# 2. Collision expansion does produce a \(\delta^1\) coefficient

On the collision chart

\[
h_1=h-\frac{\delta}{2},
\qquad
h_2=h+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta),
\]

write, at \(\delta=0\),

\[
d_{1,\pm}=d_\pm-\frac{\delta}{2}\dot d_\pm+O(\delta^2),
\qquad
d_{2,\pm}=d_\pm+\frac{\delta}{2}\dot d_\pm+O(\delta^2).
\]

Then

\[
d_{1,\pm}^2d_{2,\pm}
=
d_\pm^3-\frac{\delta}{2}d_\pm^2\dot d_\pm+O(\delta^2),
\]

\[
d_{1,\pm}d_{2,\pm}^2
=
d_\pm^3+\frac{\delta}{2}d_\pm^2\dot d_\pm+O(\delta^2).
\]

Therefore

\[
[P_\pm]_{\delta^1}
=
\frac{a_1^3}{2\pi}
\left(
d_\pm^2\dot d_\pm+\kappa d_\pm^3
\right)E_{22}.
\]

So the term is not absent by order counting. It genuinely reaches the \(\delta^1\) edge.

The reason it still dies is left/right transpose symmetry.

---

# 3. Endpoint-swap identity

The same-point endpoint swap gives

\[
d_+(z,\delta)=d_-(-z,\delta),
\qquad
\dot d_+(z,\delta)=\dot d_-(-z,\delta).
\]

Hence

\[
P_+(z,\delta)=P_-(-z,\delta).
\]

The baseline blocks satisfy

\[
G_+^{(0)}(z)=G_-^{(0)}(-z),
\]

\[
R_0(z)=L_0(-z),
\]

and

\[
N_0(-z)^T=N_0(z).
\]

Because \(P_\pm\) is symmetric and \(X\mapsto X^{-1/2}\) is analytic functional calculus on symmetric matrices,

\[
D(G_+^{-1/2})[P_+](z)
=
D(G_-^{-1/2})[P_-](-z).
\]

Define

\[
H_-(z):=D(G_-^{-1/2})[P_-](z),
\qquad
H_+(z):=D(G_+^{-1/2})[P_+](z).
\]

Then

\[
H_+(z)=H_-(-z).
\]

Also \(H_-(z)^T=H_-(z)\).

---

# 4. The cancellation

Let

\[
T(z):=H_-(z)N_0(z)R_0(z).
\]

The right-insertion term is

\[
L_0(z)N_0(z)H_+(z)
=
L_0(z)N_0(z)H_-(-z).
\]

But

\[
T(-z)^T
=
\left(
H_-(-z)N_0(-z)R_0(-z)
\right)^T.
\]

Using

\[
H_-(-z)^T=H_-(-z),
\qquad
N_0(-z)^T=N_0(z),
\qquad
R_0(-z)^T=L_0(z),
\]

we get

\[
T(-z)^T
=
L_0(z)N_0(z)H_-(-z).
\]

Therefore the full single-insertion cubic defect is

\[
C_P(z)
=
T(z)+T(-z)^T.
\]

Taking the \(z^7\)-coefficient,

\[
[z^7]C_P
=
T_7- T_7^T.
\]

Since the fixed-sector projection is transpose-invariant,

\[
\pi_{\mathfrak f_h}(T_7-T_7^T)=0.
\]

Thus

\[
\boxed{
[z^7]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right)
=0.
}
\]

Since this identity holds coefficientwise in \(\delta\),

\[
\boxed{
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right)
=0.
}
\]

---

# 5. Interpretation

This closes the first suspected actual-source defect:

\[
d_1^2d_2+d_1d_2^2
\quad\text{inside}\quad
G_{\pm,22}^{\corr}.
\]

It is not represented by the formal source-linear tower, but its **single-insertion first Fréchet response is fixed-sector invisible at odd ordinary order**.

So the previous live-defect statement should be revised:

\[
\boxed{
\text{The same-point cubic \(q^3\) defect is not live at first response.}
}
\]

The actual-source realization problem remains open, but the first candidate obstruction is eliminated.

---

# 6. What remains live

The next possible actual-source defects are not this single-insertion term. The remaining candidates are:

\[
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0,
\]

\[
D(G_-^{-1/2})[P_-]\,N_0\,D(G_+^{-1/2})[B_+],
\]

\[
L_0N_0D^2(G_+^{-1/2})[P_+,B_+],
\]

and nonlinear mixed-block remainders in

\[
N^{\corr}(d_-,d_+,\eta).
\]

The same endpoint-swap proof may kill many of these as well, but it must be checked at the full labelled aggregate level. The single-insertion same-point cubic term is no longer a valid counterexample.

---

# 7. LaTeX insertion

Insert after `rem:exact-obstruction-actual-source-gate-b`, or near the actual-source Gate B hardening remarks.

```latex
\begin{lemma}[Single-insertion same-point cubic defect is odd-order fixed-sector invisible]
\label{lem:single-insertion-same-point-cubic-defect-invisible}
Let
\[
P_\pm
=
\frac1{2\pi}
\left(
a_1^2a_2d_{1,\pm}^2d_{2,\pm}
+
a_1a_2^2d_{1,\pm}d_{2,\pm}^2
\right)E_{22}
\]
be the genuinely mixed cubic same-point defect produced by the
\(q_\pm^3\)-term in \(G_{\pm}^{\corr}\).  Then its first Fr\'echet response
inside the corrected-whitening map satisfies
\[
[z^{2n+1}]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right)=0
\]
for every \(n\ge0\).  In particular,
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
\left(
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+]
\right)=0.
\]
\end{lemma}

\begin{proof}
The endpoint swap \(z\mapsto -z\) interchanges the same-point endpoints, so
\[
P_+(z,\delta)=P_-(-z,\delta).
\]
Moreover
\[
G_+^{(0)}(z)=G_-^{(0)}(-z),
\qquad
R_0(z)=L_0(-z),
\qquad
N_0(-z)^T=N_0(z).
\]
Since \(P_\pm\) is symmetric and the inverse square root is analytic
functional calculus on symmetric matrices,
\[
D(G_+^{-1/2})[P_+](z)
=
D(G_-^{-1/2})[P_-](-z).
\]
Set
\[
H_-(z)=D(G_-^{-1/2})[P_-](z),
\qquad
T(z)=H_-(z)N_0(z)R_0(z).
\]
Then the right-insertion term is \(T(-z)^T\).  Hence the total
single-insertion cubic contribution is
\[
T(z)+T(-z)^T.
\]
Its \(z^{2n+1}\)-coefficient is
\[
T_{2n+1}-T_{2n+1}^T,
\]
whose projection to the transpose-invariant fixed sector
\(\mathfrak f_h\) is zero.
\end{proof}
```

And add this caution immediately after:

```latex
\begin{remark}[What this does not close]
\label{rem:single-insertion-cubic-not-full-actual-source-closure}
Lemma~\ref{lem:single-insertion-same-point-cubic-defect-invisible} removes
the first suspected same-point cubic actual-source defect.  It does not
prove
\[
\Theta_7^{\actual}=0.
\]
The remaining nonlinear-source candidates include higher Fr\'echet
responses containing \(P_\pm\) together with additional same-point source
slots, and the nonlinear mixed-block Taylor remainders in
\((d_-,d_+,\eta)\).  These must be checked by the same endpoint-swap /
labelled-aggregate mechanism before Gate~B can be promoted from the formal
homogeneous tower to the actual corrected source package.
\end{remark}
```
## User (2026-04-25 10:16:17)

Read and do your next attack (given your agent number) in the list.

## Assistant (2026-04-25 10:16:36)

I’m moving from raw Gate B to the combined Agent 1/4 target: whether actual-source deviations have a **double balanced zero modulo the quotient line**, not merely a simple balanced zero.

_Thought for 3m 14s_

## Agent 1 attack result

I **cannot prove** the actual-source double-balanced divisibility target

\[
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\in
(a_1+a_2)^2V_m[a_1,a_2],
\qquad
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

But the attack makes a useful reduction:

\[
\boxed{
\text{all higher Fréchet responses involving only the same-point cubic }P_\pm
\text{ are killed by endpoint-swap/transpose.}
}
\]

The **first remaining live double-balanced obstruction** is not \(P_\pm\). It is a nonlinear **mixed-block quadratic remainder** in

\[
N^{\corr}(d_-,d_+,\eta),
\]

combined with one same-point linear whitening slot. This is exactly within the attached next-wave target: check nonlinear actual-source remainders and classify them as too high-order, invisible, double-balanced, or live. 

---

# 1. Same-point \(P_\pm\) higher Fréchet responses are killed

Recall the same-point cubic defect

\[
P_\pm
=
\frac1{2\pi}
\left(
a_1^2a_2d_{1,\pm}^2d_{2,\pm}
+
a_1a_2^2d_{1,\pm}d_{2,\pm}^2
\right)E_{22}.
\]

The previous calculation killed the first Fréchet response

\[
D(G_-^{-1/2})[P_-]N_0R_0
+
L_0N_0D(G_+^{-1/2})[P_+].
\]

The same endpoint-swap proof extends to **all same-point-only words** containing \(P_\pm\).

Let \(F(X)=X^{-1/2}\). For any same-point slots \(A^{(1)},\ldots,A^{(r)}\) satisfying the actual endpoint relation

\[
A^{(j)}_+(z)=A^{(j)}_-(-z),
\]

one has

\[
D^{r+1}F(G_+^{(0)}(z))
[P_+(z),A^{(1)}_+(z),\ldots,A^{(r)}_+(z)]
=
D^{r+1}F(G_-^{(0)}(-z))
[P_-(-z),A^{(1)}_-(-z),\ldots,A^{(r)}_-(-z)].
\]

Therefore each left/right paired same-point word has the form

\[
T(z)+T(-z)^T.
\]

Its odd coefficient is

\[
[z^{2n+1}]\bigl(T(z)+T(-z)^T\bigr)
=
T_{2n+1}-T_{2n+1}^T,
\]

whose fixed-sector projection vanishes.

Thus

\[
\boxed{
[z^7]\pi_{\mathfrak f_h}
\left(\text{any same-point-only aggregate word containing }P_\pm\right)=0.
}
\]

This covers the previously listed candidates

\[
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0,
\]

\[
D(G_-^{-1/2})[P_-]N_0D(G_+^{-1/2})[B_+],
\]

\[
L_0N_0D^2(G_+^{-1/2})[P_+,B_+],
\]

provided the middle is baseline or already belongs to the formal tower with the existing transpose parity.

So the same-point cubic \(q^3\) defect is no longer a live actual-source double-balanced obstruction.

---

# 2. The first live channel: nonlinear mixed-block quadratic remainder

The actual mixed block has

\[
N_m^{\corr}(s)=\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta}{s}
&
\dfrac{\sin\Delta+q_+s\cos\Delta}{s^2}
\\[2ex]
-\dfrac{\sin\Delta+q_-s\cos\Delta}{s^2}
&
\dfrac{F(q_-,q_+,\Delta;s)}{2s^3}
\end{pmatrix},
\]

where

\[
F(q_-,q_+,\Delta;s)
=
(q_-+q_+)s\cos\Delta
+
(2-q_-q_+s^2)\sin\Delta.
\]

Substitute

\[
q_\pm=q_{0,\pm}+d_\pm,
\qquad
\Delta=\Delta_0+\eta.
\]

The \(\mathcal K^2\) mixed-block remainder contains, in the \((2,2)\)-entry, at least the following two explicit mixed terms:

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22},
\]

and

\[
Y_{\eta\eta}^{(2)}
=
\frac{1}{2\pi s^3}
\left(\partial_\Delta^2F\right)_0
\eta_1\eta_2\,E_{22}.
\]

These are genuine \(a_1a_2\)-terms in the two-atom block. They are killed by \((1-\Pi_{1,1})_{\rm mix}\) **only if isolated**. They are not killed once multiplied by one extra same-point source slot from the whitening expansion.

---

# 3. The leaking amplitude pattern

Let \(Y_{12}^{(2)}\) denote either of the above quadratic mixed-block remainders, and let

\[
A_\pm=a_1A_{1,\pm}+a_2A_{2,\pm}
\]

be a same-point linear source slot entering \(G_\pm^{-1/2}\). The relevant whitening terms are

\[
\mathcal E_A
=
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
+
L_0\,
Y_{12}^{(2)}\,
D(G_+^{-1/2})[A_+].
\]

At the collision center \(\delta=0\),

\[
A_{1,\pm}=A_{2,\pm}=A_\pm^{(0)},
\]

so the amplitude factor is

\[
a_1a_2(a_1+a_2).
\]

Thus the quotient edge contribution has the schematic form

\[
\overline P_{\mathcal E_A}(a_1,a_2)
=
a_1a_2(a_1+a_2)\,[E_A]
\quad\text{in }V_m.
\]

This is compatible with Gate B’s **simple balanced zero**:

\[
\overline P_{\mathcal E_A}(a_1,-a_1)=0.
\]

But it is not double-balanced unless

\[
[E_A]=0
\quad\text{in }V_m.
\]

Indeed,

\[
\partial_{a_2}
\left(a_1a_2(a_1+a_2)\right)\bigg|_{a_2=-a_1}
=
-a_1^2.
\]

Therefore

\[
\partial_{a_2}\overline P_{\mathcal E_A}(a_1,-a_1)
=
-a_1^2[E_A].
\]

So this channel carries quotient-visible \(\kappa\)-slope unless

\[
E_A\in \mathbf C A_5^{\mathfrak f}(m).
\]

This is precisely the Bottleneck C failure mode: simple balanced vanishing does not imply double balanced divisibility. The consolidated command identifies this double-balanced divisibility as the actual-source/Bottleneck C joint target. 

---

# 4. Order check: this channel is not too high

The channel is not excluded by ordinary order.

For example,

\[
d_{i,\pm}\sim z^2,
\]

so

\[
Y_{dd}^{(2)}
\sim
\frac{d_{1,-}d_{2,+}}{s}\sin\Delta_0
\sim
z^4
\]

up to baseline scale factors.

A same-point \(g_\pm\)-slot from \(q''\) has ordinary order \(0\). Baseline whitening coefficients can supply the remaining powers up to \(z^7\). Thus the channel can reach

\[
[z^7].
\]

Similarly,

\[
\eta_i\sim z^3,
\]

and

\[
Y_{\eta\eta}^{(2)}
=
\frac{1}{2\pi s^3}
(\partial_\Delta^2F)_0\eta_1\eta_2E_{22}
\]

also begins low enough, after the \(s^{-3}\) factor and baseline expansion, to contribute to order \(7\).

So this is not a high-order artefact.

---

# 5. Classification of the current nonlinear actual-source remainders

| Remainder | Status |
|---|---|
| Same-point cubic \(P_\pm=d_1^2d_2+d_1d_2^2\), first Fréchet response | killed by endpoint-swap/transpose |
| Higher Fréchet responses involving \(P_\pm\), with no nonlinear middle remainder | killed by same endpoint-swap/transpose word pairing |
| Product-source-motion of same-point-only \(P_\pm\)-words | killed by the same reflection argument, since \(\partial_h\) preserves the paired word structure |
| Isolated mixed-block quadratic \(Y_{12}^{(2)}\) | killed by \((1-\Pi_{1,1})_{\rm mix}\) if no extra source slot appears |
| Mixed-block quadratic \(Y_{12}^{(2)}\) plus one same-point linear whitening slot | **live Bottleneck C carrier** unless its fixed-sector coefficient lies in \(\mathbf C A_5^{\mathfrak f}\) |
| Cubic/higher mixed-block remainders | not yet tabled; lower priority than the explicit \(Y_{12}^{(2)}\times A\) channel |

---

# 6. Exact reduced obstruction

Define

\[
E_{A,Y}
:=
[z^7]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
+
L_0\,
Y_{12}^{(2)}\,
D(G_+^{-1/2})[A_+]
\right),
\]

where \(A_\pm\) ranges over the order-relevant same-point linear slots, especially the grade-zero \(g_\pm E_{22}\)-slot, and \(Y_{12}^{(2)}\) ranges over the quadratic nonlinear mixed-block remainders such as \(Y_{dd}^{(2)}\) and \(Y_{\eta\eta}^{(2)}\).

Then the actual-source double-balanced target is reduced, at the first live level, to:

\[
\boxed{
[E_{A,Y}]=0
\quad\text{in}\quad
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

Equivalently,

\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m).
}
\]

If this fails for any order-relevant \(A,Y\), then

\[
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\notin
(a_1+a_2)^2V_m[a_1,a_2].
\]

---

# 7. Minimal theorem needed to close this attack

```latex
\begin{theorem}[Quadratic mixed-remainder line-gauge theorem]
\label{thm:quadratic-mixed-remainder-line-gauge}
Let \(Y_{12}^{(2)}\) be the \(\mathcal K^2\) mixed-block remainder of
\(N^{\corr}(d_-,d_+,\eta)\), after subtracting the two one-atom blocks and
projecting to source bidegree \((1,1)\).  Let \(A_\pm\) range over the
same-point linear source slots in \(G_\pm^{\corr}\) whose whitening response
can contribute through ordinary order \(7\).  Then
\[
[z^7]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
+
L_0\,
Y_{12}^{(2)}\,
D(G_+^{-1/2})[A_+]
\right)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{theorem}
```

This theorem is now the precise local obstruction for Agent 1/4. It is stronger than Gate B’s simple balanced zero and exactly supplies the missing double-balanced quotient condition.

---

## Bottom line

The attack kills the same-point nonlinear \(P_\pm\) family as a live obstruction.

The first remaining actual-source component that can carry quotient-visible \(\kappa\)-slope is:

\[
\boxed{
\text{quadratic nonlinear mixed-block remainder }
Y_{12}^{(2)}
\text{ combined with one same-point linear whitening slot.}
}
\]

The proof now needs the finite table/identity

\[
E_{A,Y}\in \mathbf C A_5^{\mathfrak f}(m).
\]

Without that, actual-source double-balanced divisibility remains open.
## User (2026-04-25 10:28:49)

Read and do your next agent prompt (according to your agent number)

## Assistant (2026-04-25 10:30:10)

_Thought for 1m 14s_

## Agent 1 result — promoted nonlinear mixed-block carrier

The attack splits into two different statements.

1. **Frozen midpoint / no \(\delta\)-edge:** the displayed \([z^7]\) line-gauge expression is actually stronger than line-gauge: it is zero after fixed-sector projection.

2. **Bottleneck C / \([\delta^1]\)-edge:** the same endpoint-swap mechanism no longer kills the term. It turns the edge contribution into a symmetric fixed-sector class, and there is no current identity forcing that class into \(\mathbf C A_5^{\mathfrak f}(m)\).

So the promoted nonlinear mixed-block channel is **not refuted as a Bottleneck C obstruction**. It is reduced to one explicit quotient class.

This matches the current prompt: the first live actual-source carrier is \(Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]\) coupled to one same-point linear whitening slot, and the key question is whether the resulting fixed-sector contribution lies in \(\mathbf C A_5^{\mathfrak f}(m)\). 

---

# 1. Explicit \(Y_{12}^{(2)}\) table

Use

\[
N^{\corr}
=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta}{s}
&
\dfrac{\sin\Delta+q_+s\cos\Delta}{s^2}
\\[2ex]
-\dfrac{\sin\Delta+q_-s\cos\Delta}{s^2}
&
\dfrac{F(q_-,q_+,\Delta;s)}{2s^3}
\end{pmatrix},
\]

with

\[
F(q_-,q_+,\Delta;s)
=
(q_-+q_+)s\cos\Delta
+
(2-q_-q_+s^2)\sin\Delta .
\]

This is the corrected mixed-block formula recorded in the source notes. 

Set

\[
q_\pm=q_{0,\pm}+d_\pm,
\qquad
\Delta=\Delta_0+\eta,
\qquad
c_0=\cos\Delta_0,
\qquad
\ell_0=\sin\Delta_0.
\]

For two source atoms,

\[
d_\pm=a_1d_{1,\pm}+a_2d_{2,\pm},
\qquad
\eta=a_1\eta_1+a_2\eta_2.
\]

The source-bidegree \((1,1)\) nonlinear mixed-block coefficient is

\[
Y_{12}^{(2)}
=
a_1a_2
\begin{pmatrix}
Y_{11}^{(2)}&Y_{12}^{(2)}\\
Y_{21}^{(2)}&Y_{22}^{(2)}
\end{pmatrix},
\]

where, suppressing the common \(a_1a_2\),

\[
Y_{11}^{(2)}
=
\frac{2\ell_0}{\pi s}\eta_1\eta_2.
\]

\[
Y_{12}^{(2)}
=
\frac1\pi
\left[
-\frac{\ell_0}{s}
(d_{1,+}\eta_2+d_{2,+}\eta_1)
+
\frac{-\ell_0-q_{0,+}s c_0}{s^2}\eta_1\eta_2
\right].
\]

\[
Y_{21}^{(2)}
=
\frac1\pi
\left[
\frac{\ell_0}{s}
(d_{1,-}\eta_2+d_{2,-}\eta_1)
+
\frac{\ell_0+q_{0,-}s c_0}{s^2}\eta_1\eta_2
\right].
\]

For the \((2,2)\)-entry,

\[
\begin{aligned}
Y_{22}^{(2)}
=
\frac1{2\pi s^3}
\Big[
&
-s^2\ell_0(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})
\\
&+(-s\ell_0-q_{0,+}s^2c_0)(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+(-s\ell_0-q_{0,-}s^2c_0)(d_{1,+}\eta_2+d_{2,+}\eta_1)
\\
&+\bigl(-(q_{0,-}+q_{0,+})sc_0-(2-q_{0,-}q_{0,+}s^2)\ell_0\bigr)\eta_1\eta_2
\Big].
\end{aligned}
\]

So the quadratic mixed-block remainder has three families:

\[
dd,\qquad d\eta,\qquad \eta\eta.
\]

The previously identified \((2,2)\) \(dd\)-term is

\[
Y_{dd}^{(2)}
=
-\frac{\ell_0}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

---

# 2. Order check

All three families can reach ordinary order \(z^7\) after one same-point linear whitening slot.

Using

\[
d_\pm\sim z^2,
\qquad
\eta\sim z^3,
\qquad
s\sim z,
\]

one gets:

\[
dd/s\sim z^3,
\]

\[
d\eta/s\sim z^4,
\qquad
d\eta/s^2\cdot s^2\text{-baseline terms}\sim z^4,
\]

\[
\eta\eta/s^3\cdot s\text{-baseline terms}\sim z^4,
\]

and

\[
\eta\eta/s\sim z^5.
\]

A same-point linear whitening slot can start at ordinary order \(0\), especially through the \(g_\pm=q''_\pm\) source slot. Baseline \(L_0,R_0\) coefficients can supply the remaining powers. Therefore none of

\[
dd,\qquad d\eta,\qquad \eta\eta
\]

is excluded by order.

---

# 3. Frozen midpoint identity: killed, not merely line-gauge

Let

\[
H_-(z)
=
D(G_-^{-1/2})[A_-](z),
\]

and define

\[
T(z)
=
H_-(z)Y_{12}^{(2)}(z)R_0(z).
\]

At the frozen collision midpoint \(\delta=0\), endpoint swap gives

\[
Y_{12}^{(2)}(z)^T=Y_{12}^{(2)}(-z),
\]

\[
H_+(z)=H_-(-z),
\qquad
R_0(-z)^T=L_0(z).
\]

Hence the promoted left/right aggregate is

\[
T(z)+T(-z)^T.
\]

Therefore

\[
[z^7]\bigl(T(z)+T(-z)^T\bigr)
=
T_7-T_7^T.
\]

Because \(\pi_{\mathfrak f_h}\) is transpose-invariant,

\[
\pi_{\mathfrak f_h}(T_7-T_7^T)=0.
\]

Thus the frozen statement is:

\[
\boxed{
[z^7]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0
+
L_0Y_{12}^{(2)}D(G_+^{-1/2})[B_+]
\right)=0.
}
\]

So, at \(\delta=0\), this channel is zero, not merely line-gauge.

---

# 4. Why Bottleneck C is still live

The Bottleneck C edge is not the frozen \(\delta=0\) coefficient. It is the \(\delta^1\)-edge.

With moving atoms,

\[
h_1=h-\frac{\delta}{2},
\qquad
h_2=h+\frac{\delta}{2}.
\]

The endpoint-swap relation becomes

\[
C(z,\delta)
=
T(z,\delta)+T(-z,-\delta)^T.
\]

Extracting \([z^7\delta^1]\),

\[
[z^7\delta^1]C
=
T_{7,1}+T_{7,1}^T,
\]

because

\[
(-1)^7(-1)^1=+1.
\]

This is symmetric, not skew. Therefore transpose-invariance of \(\pi_{\mathfrak f_h}\) no longer kills it. Instead,

\[
\boxed{
E_{A,Y}
:=
\pi_{\mathfrak f_h}
\left(T_{7,1}+T_{7,1}^T\right)
}
\]

is the first actual quotient class.

There is no formal reason in the present draft forcing

\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m).
\]

That is exactly the missing line-gauge theorem.

---

# 5. Amplitude polynomial

The quadratic mixed block contributes \(a_1a_2\). The same-point linear whitening slot contributes

\[
a_1A_{1,\pm}+a_2A_{2,\pm}.
\]

At the collision center,

\[
A_{1,\pm}=A_{2,\pm},
\]

so the promoted channel has amplitude

\[
a_1a_2(a_1+a_2).
\]

This is simple-balanced:

\[
a_1a_2(a_1+a_2)\big|_{a_2=-a_1}=0,
\]

but not double-balanced:

\[
\partial_{a_2}\left(a_1a_2(a_1+a_2)\right)\bigg|_{a_2=-a_1}
=
-a_1^2.
\]

Therefore the Bottleneck C derivative is

\[
-a_1^2[E_{A,Y}]
\quad
\text{in }
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

So double-balanced divisibility for this channel is equivalent to

\[
\boxed{
[E_{A,Y}]=0
\quad\text{in }V_m.
}
\]

---

# 6. First explicit quotient class

The first quotient representative is

\[
\boxed{
E_{A,Y}
=
\pi_{\mathfrak f_h}
[z^7\delta^1]
\left(
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
+
L_0\,
Y_{12}^{(2)}\,
D(G_+^{-1/2})[B_+]
\right).
}
\]

Using the reflection reduction, this is equivalently

\[
\boxed{
E_{A,Y}
=
\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
[z^7\delta^1]
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
\right),
}
\]

where

\[
\operatorname{Sym}(M)=M+M^T.
\]

In good-patch determinant coordinates, if

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S,
\qquad
A_5^{\mathfrak f}=u_5I+v_5S,
\]

then the quotient obstruction is

\[
\boxed{
\omega_m(E_{A,Y},A_5^{\mathfrak f})
=
e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

Thus the first explicit nonzero quotient class is not a single scalar already evaluable from the paper; it is this finite coefficient:

\[
\boxed{
[E_{A,Y}]
=
\left[
\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7\delta^1]
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
\right]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

The present source formulas do not give a table proving this class vanishes.

---

# 7. Structural tests

| Candidate mechanism | Result |
|---|---|
| Endpoint swap | Kills frozen odd \(z\)-coefficient; at \([z^7\delta^1]\), produces symmetric fixed-sector output instead. |
| Transpose fixed-sector projection | Kills skew part only; the edge term is symmetric. |
| \((Y)\)-middle parity | Gives correct reflection law, but not proportionality to \(A_5^{\mathfrak f}\). |
| Self/skew-adjointness of \(D^2N_0[\xi_1,\xi_2]\) | Controls transpose parity, not quotient-line membership. |
| Source-bidegree projection | Does not kill the promoted term: \(Y_{12}^{(2)}\) is \((1,1)\), but multiplying by one same-point slot gives \((2,1)+(1,2)\). |
| Amplitude balance | Gives simple zero only, not double zero. |
| Line-gauge relation with \(A_5^{\mathfrak f}\) | Not proved; exactly the missing theorem. |

---

## Verdict

The frozen promoted nonlinear mixed-block expression is zero by endpoint-swap/transpose.

But the actual Bottleneck C edge is not closed. The \([z^7\delta^1]\) promoted mixed-block coefficient reduces to the explicit quotient class

\[
[E_{A,Y}]
=
\left[
\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7\delta^1]
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
\right].
\]

The next theorem must prove

\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m)
\]

for every order-relevant same-point linear slot \(A_\pm\) and every contributing \(dd,d\eta,\eta\eta\) component of \(Y_{12}^{(2)}\). Without that finite table/identity, actual-source double-balanced divisibility remains open.
## User (2026-04-25 10:42:01)

Do your agent prompt, according to your agent number

## Assistant (2026-04-25 10:42:02)

I’ll treat this as the Agent 1 coefficient-reduction task: reduce \(E_{A,Y}\) as far as possible, separating the \(dd,d\eta,\eta d,\eta\eta\) Hessian pieces and identifying whether the obstruction is zero, line-gauge, or quotient-visible.

_Thought for 1m 15s_

## Agent 1 result: \(E_{A,Y}\) is reduced, not closed

I cannot prove

\[
E_{A,Y}\in \mathbf C A_5^{\mathfrak f}(m),
\]

and I also cannot prove

\[
E_{A,Y}=0.
\]

The attack reduces the first live actual-source carrier to a finite quotient representative:

\[
\boxed{
E_{A,Y}^q
=
\left[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7\delta^1]\,
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0
\right]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

The prompt identifies this exact object as the current first live actual-source/Bottleneck C carrier: the promoted quadratic mixed-block remainder \(Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]\), coupled to one same-point linear whitening slot. Quotient Bottleneck C requires \(E_{A,Y}^q=0\), while the augmented transform-safe package would require the stronger scalar condition \(\Phi_K(E_{A,Y})=0\). 

So the classification is:

\[
\boxed{
E_{A,Y}
\text{ is a quotient-visible candidate, not currently zero or line-gauge.}
}
\]

---

# 1. Hessian expansion of \(Y_{12}^{(2)}\)

Use the corrected mixed block

\[
N^{\corr}
=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta}{s}
&
\dfrac{\sin\Delta+q_+s\cos\Delta}{s^2}
\\[2ex]
-\dfrac{\sin\Delta+q_-s\cos\Delta}{s^2}
&
\dfrac{F(q_-,q_+,\Delta;s)}{2s^3}
\end{pmatrix},
\]

with

\[
F(q_-,q_+,\Delta;s)
=
(q_-+q_+)s\cos\Delta
+
(2-q_-q_+s^2)\sin\Delta .
\]

Set

\[
q_\pm=q^0_\pm+d_\pm,
\qquad
\Delta=\Delta_0+\eta,
\qquad
\sigma=\sin\Delta_0,
\qquad
\gamma=\cos\Delta_0 .
\]

For source atoms \(1,2\),

\[
d_\pm=a_1d_{1,\pm}+a_2d_{2,\pm},
\qquad
\eta=a_1\eta_1+a_2\eta_2.
\]

The source-bidegree \((1,1)\) Hessian piece is

\[
Y_{12}^{(2)}
=
Y_{dd}^{(2)}
+
Y_{d\eta}^{(2)}
+
Y_{\eta d}^{(2)}
+
Y_{\eta\eta}^{(2)}.
\]

## \(dd\)-piece

Only the \((2,2)\)-entry contributes:

\[
\boxed{
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22}.
}
\]

## \(d\eta\) and \(\eta d\)-pieces

The off-diagonal entries are

\[
(Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}
\left(
d_{1,+}\eta_2+d_{2,+}\eta_1
\right),
\]

\[
(Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}
\left(
d_{1,-}\eta_2+d_{2,-}\eta_1
\right).
\]

The \((2,2)\)-entry is

\[
\begin{aligned}
(Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)})_{22}
=
\frac1{2\pi s^3}
\Big[
&
(-s\sigma-q^0_+s^2\gamma)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
(-s\sigma-q^0_-s^2\gamma)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

Here \(d\eta\) means the \(d\)-source is atom \(1\) and the \(\eta\)-source is atom \(2\); \(\eta d\) is the atom-swapped part.

## \(\eta\eta\)-piece

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
\frac{-\sigma-q^0_+s\gamma}{\pi s^2}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac{\sigma+q^0_-s\gamma}{\pi s^2}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac{
-(q^0_-+q^0_+)s\gamma
-
(2-q^0_-q^0_+s^2)\sigma
}{2\pi s^3}
\eta_1\eta_2 .
\]

These are the four Hessian families that must be tabled.

---

# 2. Ordinary-order contribution check

Use the \(\mathfrak D_Q\)-scaled source orders

\[
d_\pm\sim z^2,
\qquad
\eta\sim z^3,
\qquad
s\sim z,
\qquad
\sigma=\sin\Delta_0\sim z.
\]

Then the lowest possible orders are:

| Component | Lowest ordinary order | Can contribute to \([z^7]\) after one same-point slot? |
|---|---:|---|
| \(Y_{dd}^{(2)}\sim \sigma d d/s\) | \(4\) | yes |
| \(Y_{d\eta}^{(2)}\), \(Y_{\eta d}^{(2)}\) | \(4\) or \(5\), depending on entry | yes |
| \(Y_{\eta\eta}^{(2)}\) | \(4\) or \(5\), depending on entry | yes |

Thus no Hessian family is too high-order. Each can contribute to \([z^7]\) through some finite combination of:

\[
D(G_-^{-1/2})[A_-],
\qquad
Y_{12}^{(2)},
\qquad
R_0,
\]

where the remaining ordinary degree is supplied by the same-point linear slot and baseline \(R_0,L_0\) expansion.

---

# 3. Finite coefficient reduction

Write

\[
H_-(z,\delta)
=
D(G_-^{-1/2})[A_-](z,\delta),
\]

and decompose

\[
Y_{12}^{(2)}
=
\sum_{\chi\in\{dd,d\eta,\eta d,\eta\eta\}}
Y_\chi .
\]

Then

\[
E_{A,Y}
=
\sum_{\chi}
E_\chi,
\]

where

\[
\boxed{
E_\chi
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7\delta^1]\,
H_-(z,\delta)Y_\chi(z,\delta)R_0(z,\delta).
}
\]

Equivalently, if

\[
H_-=\sum H_{i,e_H}z^i\delta^{e_H},
\qquad
Y_\chi=\sum Y_{\chi,j,e_Y}z^j\delta^{e_Y},
\qquad
R_0=\sum R_{k,e_R}z^k\delta^{e_R},
\]

then the finite table is

\[
\boxed{
E_\chi
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\substack{i+j+k=7\\ e_H+e_Y+e_R=1}}
H_{i,e_H}\,
Y_{\chi,j,e_Y}\,
R_{k,e_R}.
}
\]

Only finitely many \(j\) occur because each \(Y_\chi\) begins at ordinary order at least \(4\), so \(i+k\le3\) for the lowest-order pieces.

---

# 4. Endpoint-swap / transpose test

At frozen midpoint, the endpoint-swap relation has the form

\[
Y_\chi(z,0)^T=Y_\chi(-z,0),
\]

\[
H_+(z,0)=H_-(-z,0),
\qquad
R_0(-z,0)^T=L_0(z,0).
\]

Therefore the frozen expression is

\[
T(z,0)+T(-z,0)^T.
\]

The \([z^7]\)-coefficient is skew:

\[
T_{7,0}-T_{7,0}^T,
\]

so fixed-sector projection kills it.

But the required Bottleneck C object is not frozen. At the edge,

\[
T(z,\delta)+T(-z,-\delta)^T
\]

gives

\[
[z^7\delta^1]
=
T_{7,1}+T_{7,1}^T.
\]

This is symmetric. Hence fixed-sector projection does **not** kill it.

So the endpoint-swap mechanism proves only:

\[
[z^7\delta^0]\pi_{\mathfrak f_h}=0,
\]

not

\[
[z^7\delta^1]\pi_{\mathfrak f_h}=0.
\]

This is exactly the warning in the current prompt: at \([z^7\delta^1]\), reflection gives a symmetric fixed-sector class, not automatic cancellation. 

---

# 5. Amplitude polynomial and double-balanced failure

The Hessian middle term has source bidegree \((1,1)\), hence amplitude

\[
a_1a_2.
\]

The same-point linear whitening slot contributes

\[
a_1A_{1,-}+a_2A_{2,-}.
\]

At the collision center,

\[
A_{1,-}=A_{2,-},
\]

so the promoted carrier has amplitude

\[
\boxed{
a_1a_2(a_1+a_2).
}
\]

This is simple-balanced:

\[
a_1a_2(a_1+a_2)\big|_{a_2=-a_1}=0,
\]

but not double-balanced:

\[
\partial_{a_2}
\left[
a_1a_2(a_1+a_2)
\right]_{a_2=-a_1}
=
-a_1^2.
\]

Thus the Bottleneck C derivative sees

\[
-a_1^2 E_{A,Y}^q.
\]

Therefore:

\[
\boxed{
\text{Bottleneck C for this channel is equivalent to }E_{A,Y}^q=0.
}
\]

---

# 6. \(I,S\)-basis quotient representative

Write

\[
E_{A,Y}
=
e_{A,Y}I+f_{A,Y}S.
\]

Then

\[
e_{A,Y}
=
\epsilon_I\!\left(
\tau_{h\to m}
\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
[z^7\delta^1]\,
H_-Y_\chi R_0
\right),
\]

\[
f_{A,Y}
=
\epsilon_S\!\left(
\tau_{h\to m}
\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
[z^7\delta^1]\,
H_-Y_\chi R_0
\right),
\]

where \(\epsilon_I,\epsilon_S\) are the fixed-sector coordinate functionals.

If

\[
A_5^{\mathfrak f}(m)=u_5I+v_5S,
\]

then the quotient test is

\[
\boxed{
E_{A,Y}^q=0
\quad\Longleftrightarrow\quad
e_{A,Y}v_5-u_5f_{A,Y}=0
}
\]

on a good quotient patch.

The draft currently supplies no identity forcing

\[
e_{A,Y}v_5-u_5f_{A,Y}=0.
\]

So the first explicit quotient representative is:

\[
\boxed{
E_{A,Y}^q
=
\left[
e_{A,Y}I+f_{A,Y}S
\right],
\qquad
\omega_m(E_{A,Y},A_5^{\mathfrak f})
=
e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

---

# 7. Classification table

| Piece | Formula source | Can reach \([z^7\delta^1]\)? | Endpoint-swap effect | Current classification |
|---|---|---:|---|---|
| \(Y_{dd}^{(2)}\) | \(-\sigma(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}/(2\pi s)\) | yes | symmetric survives at \(\delta^1\) | quotient-visible candidate |
| \(Y_{d\eta}^{(2)}\) | \(d_1\eta_2\) Hessian terms | yes | symmetric survives at \(\delta^1\) | quotient-visible candidate |
| \(Y_{\eta d}^{(2)}\) | \(\eta_1d_2\) Hessian terms | yes | symmetric survives at \(\delta^1\) | quotient-visible candidate |
| \(Y_{\eta\eta}^{(2)}\) | \(\eta_1\eta_2\) Hessian terms | yes | symmetric survives at \(\delta^1\) | quotient-visible candidate |

No row is killed by order. No row is killed by transpose at the \([z^7\delta^1]\)-edge. No row is proved proportional to \(A_5^{\mathfrak f}\).

---

## Verdict

The promoted nonlinear mixed-block carrier does not close by the available structural symmetries.

The result is the finite quotient obstruction:

\[
\boxed{
E_{A,Y}^q
=
\left[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta,\eta d,\eta\eta\}}
[z^7\delta^1]\,
D(G_-^{-1/2})[A_-]\,
Y_\chi\,
R_0
\right].
}
\]

Current classification:

\[
\boxed{
E_{A,Y}=0 \quad\text{not proved,}
}
\]

\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m) \quad\text{not proved,}
}
\]

\[
\boxed{
E_{A,Y}^q\ne0 \quad\text{is the first unresolved quotient-visible candidate.}
}
\]

To close this branch, the next theorem must prove the determinant identity

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0
}
\]

for the finite coefficient expression above. Without that identity, actual-source Bottleneck C remains open at the promoted \(Y_{12}^{(2)}\) channel.
## User (2026-04-25 10:49:33)

Please do this instruction according to your agent number.

## Assistant (2026-04-25 10:49:53)

_Thought for 19s_

## Agent 1 result — \(E_{A,Y}\) reduced to the minimal finite coefficient table

I cannot compute numerical/scalar \(e_{A,Y},f_{A,Y}\) from the draft as given, because the draft does not provide the required finite coefficient tables for

\[
D(G_-^{-1/2})[A_-],\qquad
R_0,\qquad
Y_{12}^{(2)}
\]

through the required \([z^7\delta^1]\) edge. The current attached instruction identifies this as the main remaining local obstruction: compute \(E_{A,Y}\), or reduce it to the smallest missing finite coefficient table. 

The reduction is:

\[
\boxed{
E_{A,Y}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{\substack{r+g+b=7\\ \alpha+\beta+\gamma=1}}
H^{A}_{r,\alpha}\,
Y^{\chi}_{g,\beta}\,
R_{b,\gamma}.
}
\]

Here

\[
H^{A}_{r,\alpha}
=
[z^r\delta^\alpha]\,D(G_-^{-1/2})[A_-],
\]

\[
Y^{\chi}_{g,\beta}
=
[z^g\delta^\beta]\,Y_{\chi}^{(2)},
\]

\[
R_{b,\gamma}
=
[z^b\delta^\gamma]\,R_0.
\]

The quotient test is

\[
\boxed{
E_{A,Y}^q=0
\Longleftrightarrow
e_{A,Y}v_5-u_5f_{A,Y}=0,
}
\]

where

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S.
\]

At present, neither

\[
E_{A,Y}=0
\]

nor

\[
E_{A,Y}\in \mathbf C A_5^{\mathfrak f}(m)
\]

is forced by the known symmetries.

---

# 1. Surviving \(Y_{12}^{(2)}\) pieces

Agent 8’s compressed table says only the transpose-symmetric rows survive at \([z^7\delta^1]\):

\[
Y_{dd}^{(2)},\qquad
Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)},\qquad
Y_{\eta\eta}^{(2)}.
\]

The antisymmetric row

\[
Y_{d\eta}^{(2)}-Y_{\eta d}^{(2)}
\]

is skew-killed after fixed-sector projection.

Thus

\[
Y_{12}^{(2),\mathrm{surv}}
=
Y_{dd}^{(2)}
+
Y_{d\eta+\eta d}^{(2)}
+
Y_{\eta\eta}^{(2)}.
\]

---

# 2. Explicit surviving Hessian components

Let

\[
q_\pm=q_\pm^0+d_\pm,\qquad
\Delta=\Delta_0+\eta,
\]

\[
\sigma=\sin\Delta_0,
\qquad
\gamma=\cos\Delta_0.
\]

## \(dd\)-row

\[
\boxed{
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
\left(
d_{1,-}d_{2,+}
+
d_{2,-}d_{1,+}
\right)E_{22}.
}
\]

## \(d\eta+\eta d\)-row

\[
\boxed{
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}
\left(
d_{1,+}\eta_2+d_{2,+}\eta_1
\right).
}
\]

\[
\boxed{
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}
\left(
d_{1,-}\eta_2+d_{2,-}\eta_1
\right).
}
\]

\[
\boxed{
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
\frac1{2\pi s^3}
\Big[
&
(-s\sigma-q_+^0s^2\gamma)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
(-s\sigma-q_-^0s^2\gamma)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
}
\]

## \(\eta\eta\)-row

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{12}
=
\frac{-\sigma-q_+^0s\gamma}{\pi s^2}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{21}
=
\frac{\sigma+q_-^0s\gamma}{\pi s^2}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{22}
=
\frac{
-(q_-^0+q_+^0)s\gamma
-
(2-q_-^0q_+^0s^2)\sigma
}{2\pi s^3}\eta_1\eta_2.
}
\]

These are the only \(Y\)-middle components Agent 1 needs for \(E_{A,Y}\).

---

# 3. Minimal executable coefficient table

Let

\[
\mathcal H_{r,\alpha}^{A}:=[z^r\delta^\alpha]D(G_-^{-1/2})[A_-],
\]

\[
\mathcal R_{b,\gamma}:=[z^b\delta^\gamma]R_0,
\]

\[
\mathcal Y_{\chi,g,\beta}:=[z^g\delta^\beta]Y_{\chi}^{(2)}.
\]

Then the surviving rows are exactly:

\[
\boxed{
E_{A,Y}
=
\sum_{\chi}
E_\chi
}
\]

with

\[
\boxed{
E_\chi
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\substack{g=4,5,6,7\\ r+b=7-g\\ \alpha+\beta+\gamma=1}}
\mathcal H_{r,\alpha}^{A}
\mathcal Y_{\chi,g,\beta}
\mathcal R_{b,\gamma}.
}
\]

Explicitly:

| \(Y\)-row \(\chi\) | \(g\) | required \(r+b\) | coefficient sum |
|---|---:|---:|---|
| \(dd\) | \(4\) | \(3\) | \(\sum_{r+b=3}\sum_{\alpha+\beta+\gamma=1} \mathcal H_{r,\alpha}^{A}\mathcal Y_{dd,4,\beta}\mathcal R_{b,\gamma}\) |
| \(dd\) | \(5\) | \(2\) | \(\sum_{r+b=2}\sum_{\alpha+\beta+\gamma=1} \mathcal H_{r,\alpha}^{A}\mathcal Y_{dd,5,\beta}\mathcal R_{b,\gamma}\) |
| \(dd\) | \(6\) | \(1\) | \(\sum_{r+b=1}\sum_{\alpha+\beta+\gamma=1} \mathcal H_{r,\alpha}^{A}\mathcal Y_{dd,6,\beta}\mathcal R_{b,\gamma}\) |
| \(dd\) | \(7\) | \(0\) | \(\sum_{\alpha+\beta+\gamma=1} \mathcal H_{0,\alpha}^{A}\mathcal Y_{dd,7,\beta}\mathcal R_{0,\gamma}\) |
| \(d\eta+\eta d\) | \(4\) | \(3\) | same with \(\mathcal Y_{d\eta+\eta d,4,\beta}\) |
| \(d\eta+\eta d\) | \(5\) | \(2\) | same with \(\mathcal Y_{d\eta+\eta d,5,\beta}\) |
| \(d\eta+\eta d\) | \(6\) | \(1\) | same with \(\mathcal Y_{d\eta+\eta d,6,\beta}\) |
| \(d\eta+\eta d\) | \(7\) | \(0\) | same with \(\mathcal Y_{d\eta+\eta d,7,\beta}\) |
| \(\eta\eta\) | \(4\) | \(3\) | same with \(\mathcal Y_{\eta\eta,4,\beta}\) |
| \(\eta\eta\) | \(5\) | \(2\) | same with \(\mathcal Y_{\eta\eta,5,\beta}\) |
| \(\eta\eta\) | \(6\) | \(1\) | same with \(\mathcal Y_{\eta\eta,6,\beta}\) |
| \(\eta\eta\) | \(7\) | \(0\) | same with \(\mathcal Y_{\eta\eta,7,\beta}\) |

This is the smallest missing finite table.

Everything outside this table is either:

\[
r+g+b\ne7,
\]

or skew-killed,

\[
Y_{d\eta-\eta d}^{(2)},
\]

or belongs to the already-killed same-point cubic \(P_\pm\) branch.

---

# 4. \(I,S\)-coordinate extraction

Define fixed-sector coordinate functionals

\[
\epsilon_I,\epsilon_S:\mathfrak f_m\to\mathbf C
\]

by

\[
X=\epsilon_I(X)I+\epsilon_S(X)S.
\]

Then

\[
\boxed{
e_{A,Y}
=
\epsilon_I(E_{A,Y})
}
\]

and

\[
\boxed{
f_{A,Y}
=
\epsilon_S(E_{A,Y}).
}
\]

Equivalently,

\[
\boxed{
e_{A,Y}
=
\epsilon_I
\left[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi,g,r,b,\alpha,\beta,\gamma}
\mathcal H_{r,\alpha}^{A}
\mathcal Y_{\chi,g,\beta}
\mathcal R_{b,\gamma}
\right],
}
\]

\[
\boxed{
f_{A,Y}
=
\epsilon_S
\left[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi,g,r,b,\alpha,\beta,\gamma}
\mathcal H_{r,\alpha}^{A}
\mathcal Y_{\chi,g,\beta}
\mathcal R_{b,\gamma}
\right].
}
\]

The quotient obstruction is therefore

\[
\boxed{
\omega_m(E_{A,Y},A_5^{\mathfrak f})
=
e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

The transform-visible obstruction is

\[
\boxed{
\Phi_K(E_{A,Y})=2f_{A,Y}.
}
\]

---

# 5. Classification

Current classification:

\[
\boxed{
E_{A,Y}=0
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m)
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}^q
=
[e_{A,Y}I+f_{A,Y}S]
\quad\text{is the first unresolved quotient-visible candidate.}
}
\]

To close the quotient branch, one must prove the finite determinant identity

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0.
}
\]

To close the augmented transform-safe branch, one must prove the stronger identity

\[
\boxed{
f_{A,Y}=0.
}
\]

On the generic \(v_5\ne0\) patch, proving both quotient closure and transform-safe closure forces

\[
\boxed{
E_{A,Y}=0.
}
\]

Thus the next computation should not broaden the search. It should fill exactly the coefficient table

\[
\boxed{
\left\{
\mathcal H_{r,\alpha}^{A},\,
\mathcal Y_{\chi,g,\beta},\,
\mathcal R_{b,\gamma}
:
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\ g=4,\ldots,7,\ r+b=7-g,\ \alpha+\beta+\gamma=1
\right\}.
}
\]
## User (2026-04-25 10:58:03)

Do these instructions per your agent number

## Assistant (2026-04-25 10:58:06)

I’ll continue as Agent 1 and focus only on the direct \(E_{A,Y}=eI+fS\) computation/reduction. I will not reopen Gate A, same-point cubic \(P_\pm\), or the closed \(M_A,M_C\) branch.

_Thought for 1m 21s_

## Agent 1 result — \(E_{A,Y}\) reduced further

I still cannot compute explicit numerical/scalar coordinates

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S
\]

from the current draft data. The missing information is now smaller and more precise than before.

The current prompt identifies \(E_{A,Y}\) as the first live local actual-source/Bottleneck C carrier, with only the symmetric \(Y_{12}^{(2)}\) rows surviving at \([z^7\delta^1]\), and with the decisive tests reduced to

\[
e_{A,Y}v_5-u_5f_{A,Y}
\]

and

\[
f_{A,Y}.
\]

That is the object I attack below. 

---

# 1. Key reduction

The direct expression is

\[
E_{A,Y}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{\substack{r+g+b=7\\ \alpha+\beta+\gamma=1}}
H^A_{r,\alpha}
Y^\chi_{g,\beta}
R_{b,\gamma}.
\]

But the symmetric \(Y\)-rows have **no first source-collision edge**:

\[
Y^\chi_{g,1}=0
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]

Reason: each surviving row is atom-symmetric. For source variables

\[
\xi_1=\xi-\frac{\delta}{2}\dot\xi+O(\delta^2),
\qquad
\xi_2=\xi+\frac{\delta}{2}\dot\xi+O(\delta^2),
\]

the symmetric products satisfy

\[
\xi_1\zeta_2+\xi_2\zeta_1
=
2\xi\zeta+O(\delta^2),
\]

so the \(\delta^1\) coefficient cancels.

Also, \(R_0\) is the baseline right-whitening factor and has no source-collision dependence, so

\[
R_{b,1}=0.
\]

Therefore the literal source-motion \([z^7\delta^1]\) edge reduces to

\[
\boxed{
E_{A,Y}^{\mathrm{pos}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{\substack{r+g+b=7}}
H^A_{r,1}
Y^\chi_{g,0}
R_{b,0}.
}
\]

The Bottleneck C weighted-amplitude edge uses the frozen same-point slot instead:

\[
\boxed{
E_{A,Y}^{\mathrm{wt}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{\substack{r+g+b=7}}
H^A_{r,0}
Y^\chi_{g,0}
R_{b,0}.
}
\]

The amplitude derivative contributes the scalar factor

\[
\partial_{a_2}\bigl(a_1a_2(a_1+a_2)\bigr)\big|_{a_2=-a_1}
=
-a_1^2.
\]

So the live quotient/hidden-state obstruction is controlled by \(E_{A,Y}^{\mathrm{wt}}\), while \(E_{A,Y}^{\mathrm{pos}}\) belongs to the ordinary source-motion edge.

This distinction matters: mixing the two double-counts the \(\delta\)-edge.

---

# 2. Surviving \(Y\)-rows

Only these rows remain:

\[
Y_{dd}^{(2)},\qquad
Y_{d\eta+\eta d}^{(2)},\qquad
Y_{\eta\eta}^{(2)}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is fixed-sector killed and should not be included.

The required coefficients are:

\[
Y^\chi_{g,0}
=
[z^g]Y_\chi^{(2)},
\qquad
g=4,5,6,7.
\]

The \(g\)-range starts at \(4\) because the worst denominators in the mixed block lower the apparent order of the \(dd,d\eta,\eta\eta\) Hessian pieces to ordinary order \(4\), and only \(g\le 7\) can contribute to \([z^7]\).

---

# 3. Minimal coefficient table

The remaining table is:

\[
\boxed{
E_{A,Y}^{\mathrm{wt}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{\substack{r+b=7-g}}
H^A_{r,0}Y^\chi_{g,0}R_{b,0}.
}
\]

Explicitly:

| \(Y\)-row | \(g\) | Needed \(H,R\) coefficients |
|---|---:|---|
| \(Y_{dd}^{(2)}\) | 4 | \(H^A_{0,0}R_{3,0},H^A_{1,0}R_{2,0},H^A_{2,0}R_{1,0},H^A_{3,0}R_{0,0}\) |
| \(Y_{dd}^{(2)}\) | 5 | \(H^A_{0,0}R_{2,0},H^A_{1,0}R_{1,0},H^A_{2,0}R_{0,0}\) |
| \(Y_{dd}^{(2)}\) | 6 | \(H^A_{0,0}R_{1,0},H^A_{1,0}R_{0,0}\) |
| \(Y_{dd}^{(2)}\) | 7 | \(H^A_{0,0}R_{0,0}\) |
| \(Y_{d\eta+\eta d}^{(2)}\) | 4 | \(H^A_{0,0}R_{3,0},H^A_{1,0}R_{2,0},H^A_{2,0}R_{1,0},H^A_{3,0}R_{0,0}\) |
| \(Y_{d\eta+\eta d}^{(2)}\) | 5 | \(H^A_{0,0}R_{2,0},H^A_{1,0}R_{1,0},H^A_{2,0}R_{0,0}\) |
| \(Y_{d\eta+\eta d}^{(2)}\) | 6 | \(H^A_{0,0}R_{1,0},H^A_{1,0}R_{0,0}\) |
| \(Y_{d\eta+\eta d}^{(2)}\) | 7 | \(H^A_{0,0}R_{0,0}\) |
| \(Y_{\eta\eta}^{(2)}\) | 4 | \(H^A_{0,0}R_{3,0},H^A_{1,0}R_{2,0},H^A_{2,0}R_{1,0},H^A_{3,0}R_{0,0}\) |
| \(Y_{\eta\eta}^{(2)}\) | 5 | \(H^A_{0,0}R_{2,0},H^A_{1,0}R_{1,0},H^A_{2,0}R_{0,0}\) |
| \(Y_{\eta\eta}^{(2)}\) | 6 | \(H^A_{0,0}R_{1,0},H^A_{1,0}R_{0,0}\) |
| \(Y_{\eta\eta}^{(2)}\) | 7 | \(H^A_{0,0}R_{0,0}\) |

Thus the smallest missing coefficient set for the weighted Bottleneck C carrier is:

\[
\boxed{
\left\{
H^A_{r,0}:0\le r\le3
\right\},
\qquad
\left\{
R_{b,0}:0\le b\le3
\right\},
}
\]

\[
\boxed{
\left\{
Y^{dd}_{g,0},
Y^{d\eta+\eta d}_{g,0},
Y^{\eta\eta}_{g,0}
:4\le g\le7
\right\}.
}
\]

For the literal source-motion edge, replace \(H^A_{r,0}\) by \(H^A_{r,1}\):

\[
\boxed{
E_{A,Y}^{\mathrm{pos}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,1}Y^\chi_{g,0}R_{b,0}.
}
\]

---

# 4. Coordinate extraction

Once the table is filled,

\[
E_{A,Y}^{\mathrm{wt}}
=
e_{A,Y}I+f_{A,Y}S.
\]

The quotient obstruction is

\[
\boxed{
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

The transform-safe obstruction is

\[
\boxed{
\Phi_K(E_{A,Y}^{\mathrm{wt}})
=
2f_{A,Y}.
}
\]

Thus:

\[
Q_{A,Y}=0
\]

is only quotient Bottleneck C, while

\[
f_{A,Y}=0
\]

is the augmented \(T\)-horizontal condition.

On the generic \(v_5\ne0\) patch, both together force

\[
E_{A,Y}^{\mathrm{wt}}=0.
\]

---

# 5. Current classification

The current classification remains:

\[
\boxed{
E_{A,Y}^{\mathrm{wt}}=0
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}^{\mathrm{wt}}\in\mathbf C A_5^{\mathfrak f}(m)
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}^{\mathrm{wt},q}
\text{ is the first unresolved quotient-visible candidate.}
}
\]

The table above is the minimal finite computation now required.
## User (2026-04-25 11:01:06)

Can you do that computation?

## Assistant (2026-04-25 11:01:45)

I can do the formal finite computation, but not produce a numerical \(e,f\) pair from the draft alone. The draft/prompt defines the carrier and the surviving rows, but it does not give the coefficient arrays \(H^A_{r,\alpha}\), \(Y^\chi_{g,\beta}\), \(R_{b,\gamma}\), nor the fixed-sector coordinate functionals needed to evaluate \(e_{A,Y},f_{A,Y}\).

_Thought for 1m 6s_

Not completely from the current draft alone.

I can do the **formal finite computation** and reduce it to explicit coefficient contractions, but I cannot produce actual scalar values

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S
\]

unless the draft supplies the missing coefficient arrays

\[
H^A_{r,\alpha},\qquad
Y^\chi_{g,\beta},\qquad
R_{b,\gamma},
\]

and the fixed-sector coordinate projection \(\pi_{\mathfrak f_h}\to \langle I,S\rangle\). The current instruction defines \(E_{A,Y}\), the surviving \(Y\)-rows, and the decisive tests \(e v_5-u_5 f\) and \(f\), but it does not provide the actual finite coefficient values. 

The exact computable expression is:

\[
E_{A,Y}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{\substack{r+g+b=7\\ \alpha+\beta+\gamma=1}}
H^A_{r,\alpha}
Y^\chi_{g,\beta}
R_{b,\gamma}.
\]

The surviving rows are only:

\[
Y_{dd}^{(2)},\qquad
Y_{d\eta+\eta d}^{(2)},\qquad
Y_{\eta\eta}^{(2)}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is killed.

So the computation requires these finite inputs:

\[
H^A_{r,\alpha}
=
[z^r\delta^\alpha]D(G_-^{-1/2})[A_-],
\]

\[
Y^\chi_{g,\beta}
=
[z^g\delta^\beta]Y_\chi^{(2)},
\]

\[
R_{b,\gamma}
=
[z^b\delta^\gamma]R_0,
\]

with

\[
r+g+b=7,\qquad \alpha+\beta+\gamma=1.
\]

If we restrict to the weighted Bottleneck C edge, where the amplitude derivative supplies the \(\delta\)-edge, the needed table collapses to

\[
\boxed{
E_{A,Y}^{\mathrm{wt}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}R_{b,0}.
}
\]

Then

\[
E_{A,Y}^{\mathrm{wt}}=e_{A,Y}I+f_{A,Y}S,
\]

and the two tests are

\[
\boxed{
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
}
\]

for quotient closure, and

\[
\boxed{
f_{A,Y}=0
}
\]

for \(T\)-horizontal / transform-safe closure.

So: I can compute the final \(e,f\) once the draft has either:

\[
\{H^A_{r,0}\}_{0\le r\le3},
\qquad
\{R_{b,0}\}_{0\le b\le3},
\qquad
\{Y^\chi_{g,0}\}_{\chi,\ 4\le g\le7},
\]

or the raw Taylor coefficients of \(G_-^{(0)},G_+^{(0)},A_-\), and \(Y_\chi\) from which those arrays are derived.

Without those, the honest result is:

\[
\boxed{
E_{A,Y}
\text{ is not computable to } eI+fS \text{ from the current draft data alone.}
}
\]

The next useful insertion into the paper is not another qualitative remark; it is a finite coefficient appendix tabulating exactly these \(H,Y,R\) entries.
## User (2026-04-25 11:03:24)

here's the latest draft. try to derive what's missing

## Assistant (2026-04-25 11:04:21)

I’ll use the latest TeX directly and separate what is now derivable from what remains a genuine finite-table gap. The important distinction is whether the draft gives actual coefficient values or only recursions/contracts.

_Thought for 2m 55s_

I inspected `proof_of_rh(432).tex` directly. The latest draft **does derive more than before**, but it still does **not** contain enough concrete coefficient data to output

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S
\]

as actual scalars. The main local obstruction is still the promoted quadratic mixed-block class \(E_{A,Y}\), and the current attack surface is exactly to decide whether it is zero, line-gauge, or quotient-visible. turn39file1

The useful new finding is sharper:

\[
\boxed{
\text{For Bottleneck C, the required first-edge carrier should use the frozen coefficient, not the internal }\delta^1\text{ coefficient.}
}
\]

---

## 1. Important correction: the amplitude already supplies the \(\delta^1\)

The promoted channel has amplitude

\[
a_1a_2(a_1+a_2).
\]

On the collision chart

\[
a_2=-a_1(1+\kappa\delta),
\]

we get

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2).
\]

So if the matrix coefficient is

\[
K(\delta)=K_0+\delta K_1+O(\delta^2),
\]

then

\[
a_1a_2(a_1+a_2)K(\delta)
=
a_1^3\kappa\delta K_0+O(\delta^2).
\]

Therefore the actual Bottleneck C first-edge obstruction is

\[
\boxed{
K_0,
}
\]

not \(K_1\).

So I would distinguish two objects:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7]\,
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0,
\]

versus the literal source-position edge

\[
E_{A,Y}^{\mathrm{pos}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7\delta^1]\,
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0.
\]

The Bottleneck C / \(\kappa\)-slope carrier is

\[
\boxed{
E_{A,Y}^{\mathrm{BC}},
}
\]

because the amplitude factor already contributes the \(\delta^1\).

That means the operative finite sum is

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}\,
Y^\chi_{g,0}\,
R_{b,0}.
}
\]

The table with

\[
\alpha+\beta+\gamma=1
\]

computes the next source-position edge \(K_1\). It does **not** control the first Bottleneck C amplitude derivative unless the amplitude derivative has already been divided out in the notation.

---

## 2. What I can derive explicitly: \(Y_{12}^{(2)}\)

From the actual corrected mixed block

\[
N^{\corr}
=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta}{s}
&
\dfrac{\sin\Delta+q_+s\cos\Delta}{s^2}
\\[1.4ex]
-\dfrac{\sin\Delta+q_-s\cos\Delta}{s^2}
&
\dfrac{(q_-+q_+)s\cos\Delta+(2-q_-q_+s^2)\sin\Delta}{2s^3}
\end{pmatrix},
\]

write

\[
q_\pm=q_\pm^0+d_\pm,\qquad
\Delta=\Delta_0+\eta,\qquad
\sigma=\sin\Delta_0,\qquad
\gamma=\cos\Delta_0.
\]

Then the source-bidegree \((1,1)\) quadratic Hessian piece decomposes as

\[
Y_{12}^{(2)}
=
Y_{dd}^{(2)}
+
Y_{d\eta+\eta d}^{(2)}
+
Y_{\eta\eta}^{(2)}
+
Y_{d\eta-\eta d}^{(2)}.
\]

The antisymmetric row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is skew-killed, so only the following survive.

### \(dd\)-row

\[
\boxed{
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
\left(
d_{1,-}d_{2,+}
+
d_{2,-}d_{1,+}
\right)E_{22}.
}
\]

### \(d\eta+\eta d\)-row

\[
\boxed{
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}
\left(
d_{1,+}\eta_2+d_{2,+}\eta_1
\right).
}
\]

\[
\boxed{
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}
\left(
d_{1,-}\eta_2+d_{2,-}\eta_1
\right).
}
\]

\[
\boxed{
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
\frac1{2\pi s^3}
\Big[
&
(-s\sigma-q_+^0s^2\gamma)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
(-s\sigma-q_-^0s^2\gamma)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
}
\]

### \(\eta\eta\)-row

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{12}
=
\frac{-\sigma-q_+^0s\gamma}{\pi s^2}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{21}
=
\frac{\sigma+q_-^0s\gamma}{\pi s^2}\eta_1\eta_2.
}
\]

\[
\boxed{
(Y_{\eta\eta}^{(2)})_{22}
=
\frac{
-(q_-^0+q_+^0)s\gamma
-
(2-q_-^0q_+^0s^2)\sigma
}{2\pi s^3}\eta_1\eta_2.
}
\]

So \(Y^\chi_{g,0}\) is fully derivable from the draft **as a coefficient extraction problem**:

\[
Y^\chi_{g,0}=[z^g]Y_\chi^{(2)},\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},\quad 4\le g\le 7.
\]

---

## 3. What the draft gives for \(H^A_{r,0}\) and \(R_{b,0}\)

The draft now gives the right recursion infrastructure.

Let

\[
R_{b,0}=W_{+,b},
\]

where

\[
G_+^{(0)-1/2}=\sum_{b\ge0}W_{+,b}z^b.
\]

For the same-point linear whitening slot,

\[
H^A_{r,0}
=
[z^r]D(G_-^{-1/2})[A_-].
\]

In the draft’s notation this is a linear combination of the first Fréchet coefficients

\[
\Lambda^-_{a,r}.
\]

The recursion is:

\[
S_{\varepsilon,n}^a
=
\Sigma_\varepsilon
\left(
X_{\varepsilon,n}^a
-
\sum_{j=1}^{n}
\bigl(
P_{\varepsilon,j}S_{\varepsilon,n-j}^a
+
S_{\varepsilon,n-j}^aP_{\varepsilon,j}
\bigr)
\right),
\]

\[
\Lambda_{\varepsilon,n}^{a}
=
-\sum_{i+j+k=n}
W_{\varepsilon,i}S_{\varepsilon,j}^aW_{\varepsilon,k}.
\]

Therefore

\[
\boxed{
H^A_{r,0}
=
\sum_a A_a\,\Lambda^-_{a,r}
}
\]

for the relevant same-point source slot \(A_-=\sum_a A_aX_-^a\).

---

## 4. The minimal missing table

To compute

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S,
\]

the remaining required data are exactly:

\[
\boxed{
W_{+,0},W_{+,1},W_{+,2},W_{+,3},
}
\]

\[
\boxed{
\Lambda^-_{a,r}
\quad
\text{for every order-relevant source index }a
\text{ and }0\le r\le3,
}
\]

\[
\boxed{
Y^{dd}_{g,0},
\quad
Y^{d\eta+\eta d}_{g,0},
\quad
Y^{\eta\eta}_{g,0},
\qquad
4\le g\le7.
}
\]

Then the finite contraction is

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
}
\]

Equivalently,

\[
e_{A,Y}
=
\epsilon_I(E_{A,Y}^{\mathrm{BC}}),
\qquad
f_{A,Y}
=
\epsilon_S(E_{A,Y}^{\mathrm{BC}}).
\]

The quotient and transform-safe tests are then:

\[
\boxed{
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
}
\]

\[
\boxed{
\Phi_K(E_{A,Y}^{\mathrm{BC}})=2f_{A,Y}.
}
\]

---

## 5. Why this still cannot be completed numerically from the draft

The draft gives table **contracts**, not all table **values**.

The missing entries are:

### A. Baseline square-root / inverse-square-root coefficients

The draft defines \(P_{\varepsilon,0}\), \(P_{\varepsilon,j}\), and \(W_{\varepsilon,j}\), but does not tabulate

\[
W_{+,0..3}.
\]

They are derivable from the baseline same-point block \(G_+^{(0)}\), but only after fixing the baseline jets

\[
q_0^{(k)}(m)
\]

to sufficient order.

The needed recursion is:

\[
P_0^2=G_0,
\]

\[
P_0P_n+P_nP_0
=
G_n-\sum_{i=1}^{n-1}P_iP_{n-i},
\]

\[
W_0=P_0^{-1},
\]

\[
W_n
=
-W_0\sum_{i=1}^nP_iW_{n-i}.
\]

### B. Same-point source primitives beyond the shown low-order table

The draft explicitly lists \(X_{\varepsilon,n}^a\) only for \(n\le2\). But the \(E_{A,Y}\) contraction can require

\[
H^A_{3,0},
\]

and hence

\[
\Lambda^-_{a,3}.
\]

Computing \(\Lambda^-_{a,3}\) requires \(X^-_{a,3}\), unless it is known to vanish by source normal form. The draft does not currently tabulate that.

So the missing item is:

\[
\boxed{
X^-_{a,3}
\quad
\text{for all same-point source indices }a
\text{ that can enter }A_-.
}
\]

If a source-normal-form theorem proves \(X^-_{a,3}=0\) for all relevant \(a\), then the table collapses. But the current draft does not state that.

### C. Frozen \(Y\)-Hessian coefficients

The formulas above reduce \(Y^\chi_{g,0}\) to coefficient extraction, but the draft does not tabulate the actual coefficient values through \(g=7\). These require frozen source jets for

\[
d_{i,\pm}(z),\qquad
\eta_i(z),
\]

through the necessary order.

So the missing finite table is:

\[
\boxed{
[z^g]Y_{dd}^{(2)},\quad
[z^g]Y_{d\eta+\eta d}^{(2)},\quad
[z^g]Y_{\eta\eta}^{(2)},
\qquad 4\le g\le7.
}
\]

---

## 6. Bottom line

The latest draft lets us derive the **shape** of the computation and the full \(Y_{12}^{(2)}\) Hessian. It does **not** yet let us evaluate

\[
E_{A,Y}=eI+fS.
\]

The exact missing finite table is:

\[
\boxed{
\mathcal T_{EAY}
=
\left\{
W_{+,0..3},\ 
\Lambda^-_{a,0..3},\ 
Y^{dd}_{4..7,0},\
Y^{d\eta+\eta d}_{4..7,0},\
Y^{\eta\eta}_{4..7,0}
\right\}.
}
\]

And the most important correction is:

\[
\boxed{
\text{For the Bottleneck C amplitude derivative, use the frozen coefficient } 
\alpha+\beta+\gamma=0,
\text{ not the internal } \delta^1 \text{ coefficient.}
}
\]

The theorem-ready missing lemma is:

```latex
\begin{lemma}[Promoted mixed-block coefficient table]
\label{lem:promoted-y12-coefficient-table}
In the normalization of
Definition~\ref{def:promoted-quadratic-mixed-block-obstruction},
the frozen Bottleneck-C coefficient of the promoted quadratic mixed-block
channel is
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]
Moreover,
\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S,
\]
with quotient obstruction
\[
e_{A,Y}v_5-u_5f_{A,Y}
\]
and transform-safe obstruction
\[
f_{A,Y}.
\]
\end{lemma}
```

Then the paper needs either a computed table proving

\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\]

and

\[
f_{A,Y}=0,
\]

or it must leave \(E_{A,Y}\) as the first unresolved local obstruction.
## User (2026-04-25 11:07:12)

ok, derive the remaining missing items from the draft

## Assistant (2026-04-25 11:07:14)

I’ll now inspect the actual TeX for the coefficient-table machinery rather than relying on the prompt summaries. The goal is to see whether \(W_{+,0..3}\), \(\Lambda^-_{a,0..3}\), and the \(Y^\chi_{4..7,0}\) coefficients are derivable inside the draft or still require an added appendix.

_Thought for 2m 25s_

I tried to push the latest draft as far as it will go. The result is:

\[
\boxed{
\text{The missing items can be derived as finite symbolic coefficient formulas,}
}
\]

but

\[
\boxed{
\text{the draft still does not supply the scalar midpoint jet table needed to evaluate }E_{A,Y}=eI+fS.
}
\]

This is not a matter of effort; the draft explicitly says the finite Fréchet recurrences are **table contracts, not completed source tables**, and that promotion requires a source theorem supplying the required midpoint jets. 

Below is the full derivation of the remaining missing items.

---

# 1. Baseline same-point coefficients \(G_{\varepsilon,n}^{(0)}\)

Let

\[
\varepsilon\in\{-1,+1\},
\qquad
t_\varepsilon=m+\varepsilon\frac{z}{2Q^2}.
\]

Write

\[
q_j:=q_0^{(j)}(m),
\qquad
q_\varepsilon(z):=q_0(t_\varepsilon).
\]

Then

\[
q_\varepsilon(z)
=
\sum_{n\ge0}
\varepsilon^n
\frac{q_n}{n!(2Q^2)^n}z^n.
\]

The baseline same-point block is

\[
G_\varepsilon^{(0)}(z)
=
\frac1\pi
\begin{pmatrix}
2q_\varepsilon
&
\frac12q_\varepsilon'
\\[0.8ex]
\frac12q_\varepsilon'
&
\frac1{12}\bigl(q_\varepsilon''+2q_\varepsilon^3\bigr)
\end{pmatrix}.
\]

Hence

\[
G_\varepsilon^{(0)}(z)=\sum_{n\ge0}G_{\varepsilon,n}^{(0)}z^n,
\]

with

\[
\boxed{
(G_{\varepsilon,n}^{(0)})_{11}
=
\frac{2}{\pi}
\varepsilon^n
\frac{q_n}{n!(2Q^2)^n}.
}
\]

\[
\boxed{
(G_{\varepsilon,n}^{(0)})_{12}
=
(G_{\varepsilon,n}^{(0)})_{21}
=
\frac{1}{2\pi}
\varepsilon^n
\frac{q_{n+1}}{n!(2Q^2)^n}.
}
\]

\[
\boxed{
(G_{\varepsilon,n}^{(0)})_{22}
=
\frac{1}{12\pi}
\varepsilon^n
\frac{
q_{n+2}+2(q_0^3)^{(n)}(m)
}{
n!(2Q^2)^n
}.
}
\]

This gives \(G_{\varepsilon,0},G_{\varepsilon,1},G_{\varepsilon,2},G_{\varepsilon,3}\), provided the draft/source supplies

\[
q_0^{(k)}(m),\qquad 0\le k\le 5
\]

for this piece. The Stage 1 contract asks for \(q_0^{(k)}(m)\) through \(k=9\), so this is within the stated finite jet window. 

---

# 2. Square-root and inverse-square-root coefficients \(W_{\varepsilon,0..3}\)

Let

\[
G_\varepsilon^{(0)}(z)^{1/2}
=
P_{\varepsilon,0}+P_{\varepsilon,1}z+P_{\varepsilon,2}z^2+P_{\varepsilon,3}z^3+\cdots,
\]

\[
G_\varepsilon^{(0)}(z)^{-1/2}
=
W_{\varepsilon,0}+W_{\varepsilon,1}z+W_{\varepsilon,2}z^2+W_{\varepsilon,3}z^3+\cdots.
\]

Then

\[
\boxed{
P_{\varepsilon,0}^2=G_{\varepsilon,0}^{(0)}.
}
\]

For \(n=1,2,3\),

\[
\boxed{
P_{\varepsilon,0}P_{\varepsilon,n}
+
P_{\varepsilon,n}P_{\varepsilon,0}
=
G_{\varepsilon,n}^{(0)}
-
\sum_{i=1}^{n-1}
P_{\varepsilon,i}P_{\varepsilon,n-i}.
}
\]

Equivalently,

\[
\boxed{
P_{\varepsilon,n}
=
\Sigma_\varepsilon
\left(
G_{\varepsilon,n}^{(0)}
-
\sum_{i=1}^{n-1}
P_{\varepsilon,i}P_{\varepsilon,n-i}
\right),
}
\]

where

\[
\Sigma_\varepsilon(C)
\]

solves

\[
P_{\varepsilon,0}Z+ZP_{\varepsilon,0}=C.
\]

Then

\[
\boxed{
W_{\varepsilon,0}=P_{\varepsilon,0}^{-1},
}
\]

and for \(n=1,2,3\),

\[
\boxed{
W_{\varepsilon,n}
=
-W_{\varepsilon,0}
\sum_{i=1}^{n}
P_{\varepsilon,i}W_{\varepsilon,n-i}.
}
\]

So the previously missing

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3}
\]

are fully derivable as Sylvester-recursive expressions from

\[
G_{+,0}^{(0)},G_{+,1}^{(0)},G_{+,2}^{(0)},G_{+,3}^{(0)}.
\]

They are **not** simplified scalar matrices unless one supplies the actual \(q_0\)-jet table and chooses an explicit square-root branch.

---

# 3. Source-linear same-point primitives \(X_{\varepsilon,n}^a\)

The draft gives \(X_{\varepsilon,n}^a\) only for \(n\le2\), but we can derive the general formula from the same-point block.

Let the source residual be

\[
\delta q_a(t)=r_a\frac{(t-m)^a}{a!}.
\]

At

\[
t_\varepsilon=m+\varepsilon\frac{z}{2Q^2},
\]

we have

\[
\delta q_a(t_\varepsilon)
=
r_a\frac{\varepsilon^a z^a}{a!(2Q^2)^a},
\]

\[
\delta q_a'(t_\varepsilon)
=
r_a\frac{\varepsilon^{a-1}z^{a-1}}{(a-1)!(2Q^2)^{a-1}},
\]

\[
\delta q_a''(t_\varepsilon)
=
r_a\frac{\varepsilon^{a-2}z^{a-2}}{(a-2)!(2Q^2)^{a-2}}.
\]

The source-linear same-point perturbation is

\[
\delta G_\varepsilon^{\lin}
=
\frac1\pi
\begin{pmatrix}
2\delta q_a
&
\frac12\delta q_a'
\\[0.8ex]
\frac12\delta q_a'
&
\frac1{12}\bigl(\delta q_a''+6q_\varepsilon^2\delta q_a\bigr)
\end{pmatrix}.
\]

After applying

\[
\mathfrak D_Q(M)=
\begin{pmatrix}
Q^2m_{11}&Qm_{12}\\
Qm_{21}&m_{22}
\end{pmatrix},
\]

write

\[
X_{\varepsilon,n}^a=[z^n]\mathfrak D_Q(\delta G_\varepsilon^{\lin})/r_a.
\]

Then \(X_{\varepsilon,n}^a\) has entries:

\[
\boxed{
(X_{\varepsilon,n}^a)_{11}
=
\mathbf 1_{n=a}
\frac{
\varepsilon^a
}{
\pi\,2^{a-1}a!\,Q^{2a-2}
}.
}
\]

\[
\boxed{
(X_{\varepsilon,n}^a)_{12}
=
(X_{\varepsilon,n}^a)_{21}
=
\mathbf 1_{n=a-1}
\frac{
\varepsilon^{a-1}
}{
\pi\,2^a(a-1)!\,Q^{2a-3}
}.
}
\]

\[
\boxed{
\begin{aligned}
(X_{\varepsilon,n}^a)_{22}
={}&
\mathbf 1_{n=a-2}
\frac{
\varepsilon^{a-2}
}{
12\pi\,2^{a-2}(a-2)!\,Q^{2a-4}
}
\\
&+
\mathbf 1_{n\ge a}
\frac{
\varepsilon^n
(q_0^2)^{(n-a)}(m)
}{
2\pi\,2^n a!(n-a)!\,Q^{2n}
}.
\end{aligned}
}
\]

Equivalently, in the \(I,D,S\) basis,

\[
X_{\varepsilon,n}^a
=
\frac{A_{\varepsilon,n}^a+C_{\varepsilon,n}^a}{2}I
+
\frac{A_{\varepsilon,n}^a-C_{\varepsilon,n}^a}{2}D
+
B_{\varepsilon,n}^aS,
\]

where \(A,B,C\) are the \((11),(12),(22)\) entries above.

This reproduces the draft’s listed \(n\le2\) table, and it gives the missing \(n=3\) table.

For \(n=3\), explicitly:

\[
\boxed{
X_{\varepsilon,3}^2
=
\frac{\varepsilon(q_0^2)'(m)}{64\pi Q^6}(I-D).
}
\]

\[
\boxed{
X_{\varepsilon,3}^3
=
\frac{\varepsilon}{24\pi Q^4}I
+
\frac{\varepsilon}{24\pi Q^4}D
+
\frac{\varepsilon(q_0^2)(m)}{96\pi Q^6}(I-D).
}
\]

\[
\boxed{
X_{\varepsilon,3}^4
=
\frac{\varepsilon}{64\pi Q^5}S.
}
\]

\[
\boxed{
X_{\varepsilon,3}^5
=
\frac{\varepsilon}{2304\pi Q^6}(I-D).
}
\]

All other \(X_{\varepsilon,3}^a\) with \(2\le a\le6\) vanish, except for higher \(q_0^2\)-coupling terms already included by the general formula when \(n\ge a\).

This is a real derivation from the draft’s block formula and \(\mathfrak D_Q\)-scaling. It removes the earlier “\(X_{a,3}\) missing” problem.

---

# 4. First Fréchet coefficients \(\Lambda_{\varepsilon,n}^a\)

The draft defines

\[
\Lambda_{\varepsilon,n}^{a}
=
-\sum_{i+j+k=n}
W_{\varepsilon,i}S_{\varepsilon,j}^aW_{\varepsilon,k},
\]

with

\[
S_{\varepsilon,n}^a
=
\Sigma_\varepsilon
\left(
X_{\varepsilon,n}^a
-
\sum_{j=1}^{n}
\bigl(
P_{\varepsilon,j}S_{\varepsilon,n-j}^a
+
S_{\varepsilon,n-j}^aP_{\varepsilon,j}
\bigr)
\right).
\]

Thus the missing \(H^A_{r,0}\) are

\[
\boxed{
H^A_{r,0}
=
\sum_a A_a\Lambda^-_{a,r},
}
\]

where \(A_-=\sum_a A_aX_-^a\) is the same-point linear source slot.

For \(r=0,1,2,3\), this gives:

\[
\boxed{
S^-_{a,0}
=
\Sigma_-(X^-_{a,0}).
}
\]

\[
\boxed{
S^-_{a,1}
=
\Sigma_-
\left(
X^-_{a,1}
-
P_{-,1}S^-_{a,0}
-
S^-_{a,0}P_{-,1}
\right).
}
\]

\[
\boxed{
S^-_{a,2}
=
\Sigma_-
\left(
X^-_{a,2}
-
P_{-,1}S^-_{a,1}
-
S^-_{a,1}P_{-,1}
-
P_{-,2}S^-_{a,0}
-
S^-_{a,0}P_{-,2}
\right).
}
\]

\[
\boxed{
\begin{aligned}
S^-_{a,3}
=
\Sigma_-
\Big(
X^-_{a,3}
&-
P_{-,1}S^-_{a,2}
-
S^-_{a,2}P_{-,1}
\\
&-
P_{-,2}S^-_{a,1}
-
S^-_{a,1}P_{-,2}
\\
&-
P_{-,3}S^-_{a,0}
-
S^-_{a,0}P_{-,3}
\Big).
\end{aligned}
}
\]

Then

\[
\boxed{
\Lambda^-_{a,0}
=
-W_{-,0}S^-_{a,0}W_{-,0}.
}
\]

\[
\boxed{
\Lambda^-_{a,1}
=
-\bigl(
W_{-,1}S^-_{a,0}W_{-,0}
+
W_{-,0}S^-_{a,1}W_{-,0}
+
W_{-,0}S^-_{a,0}W_{-,1}
\bigr).
}
\]

\[
\boxed{
\Lambda^-_{a,2}
=
-\sum_{i+j+k=2}
W_{-,i}S^-_{a,j}W_{-,k}.
}
\]

\[
\boxed{
\Lambda^-_{a,3}
=
-\sum_{i+j+k=3}
W_{-,i}S^-_{a,j}W_{-,k}.
}
\]

This derives the missing \(H\)-side of the \(E_{A,Y}\) table.

---

# 5. The \(Y^\chi_{g,0}\) coefficients

Let

\[
s=\frac{z}{Q^2},
\qquad
\sigma(z)=\sin\Delta_0(z),
\qquad
\gamma(z)=\cos\Delta_0(z),
\]

and define coefficient operators

\[
C_p[F]_n:=[z^n]\frac{F(z)}{s^p}
=
Q^{2p}[z^{n+p}]F(z).
\]

Let

\[
d_{i,\varepsilon}(z)=\sum_{n\ge0}d_{i,\varepsilon,n}z^n,
\qquad
\eta_i(z)=\sum_{n\ge0}\eta_{i,n}z^n.
\]

The surviving Hessian rows are:

\[
Y_{dd}^{(2)},\qquad
Y_{d\eta+\eta d}^{(2)},\qquad
Y_{\eta\eta}^{(2)}.
\]

The skew row \(Y_{d\eta-\eta d}^{(2)}\) is killed and should not be included.

## \(dd\)-row

\[
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22}.
\]

Thus

\[
\boxed{
Y^{dd}_{g,0}
=
-\frac1{2\pi}
[z^g]
\frac{\sigma}{s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22}.
}
\]

Equivalently,

\[
\boxed{
Y^{dd}_{g,0}
=
-\frac1{2\pi}
\sum_{i+j+k=g}
C_1[\sigma]_i
\left(
d_{1,-,j}d_{2,+,k}
+
d_{2,-,j}d_{1,+,k}
\right)E_{22}.
}
\]

## \(d\eta+\eta d\)-row

The entries are:

\[
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}
(d_{1,+}\eta_2+d_{2,+}\eta_1),
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}
(d_{1,-}\eta_2+d_{2,-}\eta_1),
\]

\[
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
-\frac1{2\pi}
\Big[
&
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

So \(Y^{d\eta+\eta d}_{g,0}\) is obtained by taking \([z^g]\) entrywise in these formulas.

## \(\eta\eta\)-row

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
-\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac1{2\pi}
\left[
-\frac{(q_-^0+q_+^0)\gamma}{s^2}
-\frac{2\sigma}{s^3}
+\frac{q_-^0q_+^0\sigma}{s}
\right]\eta_1\eta_2.
\]

Again,

\[
\boxed{
Y^{\eta\eta}_{g,0}
=
[z^g]Y_{\eta\eta}^{(2)}.
}
\]

This gives every \(Y^\chi_{g,0}\) for \(4\le g\le7\) by finite convolution of source jets.

---

# 6. Final finite contraction for \(E_{A,Y}\)

The Bottleneck-C amplitude derivative uses the frozen internal coefficient. The relevant object is therefore

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}
Y^\chi_{g,0}
W_{+,b}.
}
\]

Substituting

\[
H^A_{r,0}=\sum_aA_a\Lambda^-_{a,r},
\]

we get the fully derived finite contraction:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
\sum_a
A_a
\Lambda^-_{a,r}
Y^\chi_{g,0}
W_{+,b}.
}
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
e_{A,Y}I+f_{A,Y}S.
\]

The two decisive tests are:

\[
\boxed{
Q_{A,Y}:=e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

\[
\boxed{
\Phi_K(E_{A,Y}^{\mathrm{BC}})=2f_{A,Y}.
}
\]

So quotient closure is

\[
Q_{A,Y}=0,
\]

while transform-safe \(T\)-horizontal closure is

\[
f_{A,Y}=0.
\]

---

# 7. What still cannot be evaluated from the draft

Even after deriving the remaining formulas, the draft still does not give enough data to decide whether

\[
E_{A,Y}^{\mathrm{BC}}=0,
\]

or

\[
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f}(m),
\]

or

\[
E_{A,Y}^{q}\ne0.
\]

The remaining non-derived inputs are exactly the scalar source jets:

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le9,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
}
\]

The draft’s own Stage 1 contract states that these are required and that the current source supports ungraded one-pair source jets after affine removal, but does **not** yet supply the graded source jets as a proved theorem. 

So the honest status is:

\[
\boxed{
\text{The coefficient machinery is now derived.}
}
\]

\[
\boxed{
\text{The finite scalar source-jet table is still missing.}
}
\]

\[
\boxed{
E_{A,Y}\text{ remains the first unresolved local obstruction.}
}
\]

The next mathematical target is no longer “derive the recurrences”; it is:

\[
\boxed{
\text{prove the finite source-jet table or prove directly that the above contraction has }
Q_{A,Y}=0
\text{ and }f_{A,Y}=0.
}
\]
## User (2026-04-25 11:16:46)

Do instruction per your agent number

## Assistant (2026-04-25 11:17:15)

_Thought for 27s_

## Agent 1 result — finite \(E_{A,Y}^{\mathrm{BC}}\) table derived as far as possible

Using the corrected Bottleneck C carrier, the active local object is

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

This is the frozen internal coefficient. The \(\delta^1\)-edge is already supplied by

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2)
\]

on the chart \(a_2=-a_1(1+\kappa\delta)\), so the internal \(\alpha+\beta+\gamma=1\) table is not the first Bottleneck C carrier. 

I can derive the full coefficient machinery, but the scalar midpoint source jets are still not fixed by the draft. Thus the result is a **closed finite symbolic table**, not an evaluated scalar pair \(e_{A,Y},f_{A,Y}\).

---

# 1. Baseline block coefficients

Let

\[
t_\varepsilon=m+\varepsilon\frac{z}{2Q^2},
\qquad
\varepsilon\in\{-1,+1\},
\]

and write

\[
q_j=q_0^{(j)}(m).
\]

Then

\[
q_\varepsilon(z)
=
\sum_{n\ge0}
\varepsilon^n
\frac{q_n}{n!(2Q^2)^n}z^n.
\]

The baseline same-point block is

\[
G_\varepsilon^{(0)}(z)
=
\frac1\pi
\begin{pmatrix}
2q_\varepsilon&
\frac12q_\varepsilon'
\\[0.6ex]
\frac12q_\varepsilon'&
\frac1{12}\left(q_\varepsilon''+2q_\varepsilon^3\right)
\end{pmatrix}
=
\sum_{n\ge0}G_{\varepsilon,n}^{(0)}z^n.
\]

Thus

\[
(G_{\varepsilon,n}^{(0)})_{11}
=
\frac{2}{\pi}
\varepsilon^n
\frac{q_n}{n!(2Q^2)^n},
\]

\[
(G_{\varepsilon,n}^{(0)})_{12}
=
(G_{\varepsilon,n}^{(0)})_{21}
=
\frac{1}{2\pi}
\varepsilon^n
\frac{q_{n+1}}{n!(2Q^2)^n},
\]

\[
(G_{\varepsilon,n}^{(0)})_{22}
=
\frac{1}{12\pi}
\varepsilon^n
\frac{q_{n+2}+2(q_0^3)^{(n)}(m)}
{n!(2Q^2)^n}.
\]

For \(E_{A,Y}^{\mathrm{BC}}\), only \(n\le3\) is needed here.

---

# 2. \(W_{+,0},\ldots,W_{+,3}\)

Define

\[
P_\varepsilon(z)=G_\varepsilon^{(0)}(z)^{1/2}
=
\sum_{n\ge0}P_{\varepsilon,n}z^n,
\]

\[
W_\varepsilon(z)=G_\varepsilon^{(0)}(z)^{-1/2}
=
\sum_{n\ge0}W_{\varepsilon,n}z^n.
\]

Then

\[
P_{\varepsilon,0}^2=G_{\varepsilon,0}^{(0)}.
\]

For \(1\le n\le3\),

\[
P_{\varepsilon,0}P_{\varepsilon,n}
+
P_{\varepsilon,n}P_{\varepsilon,0}
=
G_{\varepsilon,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{\varepsilon,i}P_{\varepsilon,n-i}.
\]

Equivalently,

\[
P_{\varepsilon,n}
=
\Sigma_\varepsilon\!\left(
G_{\varepsilon,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{\varepsilon,i}P_{\varepsilon,n-i}
\right),
\]

where \(\Sigma_\varepsilon(C)\) is the Sylvester-solver

\[
P_{\varepsilon,0}Z+ZP_{\varepsilon,0}=C.
\]

Then

\[
W_{\varepsilon,0}=P_{\varepsilon,0}^{-1},
\]

and for \(1\le n\le3\),

\[
W_{\varepsilon,n}
=
-W_{\varepsilon,0}
\sum_{i=1}^{n}P_{\varepsilon,i}W_{\varepsilon,n-i}.
\]

So \(W_{+,0..3}\) is fully determined by \(q_0^{(k)}(m)\) through \(k=5\), subject to the chosen square-root branch.

---

# 3. Same-point source-linear coefficients \(H^A_{r,0}\)

Let a same-point source primitive be

\[
\delta q_\mu(t)
=
\rho_\mu\frac{(t-m)^\mu}{\mu!}.
\]

At

\[
t_\varepsilon=m+\varepsilon\frac{z}{2Q^2},
\]

the source-linear same-point perturbation is

\[
\delta G_\varepsilon^{\lin}
=
\frac1\pi
\begin{pmatrix}
2\delta q_\mu&
\frac12\delta q_\mu'
\\[0.6ex]
\frac12\delta q_\mu'&
\frac1{12}\left(\delta q_\mu''+6q_\varepsilon^2\delta q_\mu\right)
\end{pmatrix}.
\]

After applying the \(\mathfrak D_Q\)-scaling, define

\[
X_{\varepsilon,n}^{\mu}
=
[z^n]\mathfrak D_Q(\delta G_\varepsilon^{\lin})/\rho_\mu.
\]

Then

\[
(X_{\varepsilon,n}^{\mu})_{11}
=
\mathbf 1_{n=\mu}
\frac{\varepsilon^\mu}
{\pi\,2^{\mu-1}\mu!\,Q^{2\mu-2}},
\]

\[
(X_{\varepsilon,n}^{\mu})_{12}
=
(X_{\varepsilon,n}^{\mu})_{21}
=
\mathbf 1_{n=\mu-1}
\frac{\varepsilon^{\mu-1}}
{\pi\,2^\mu(\mu-1)!\,Q^{2\mu-3}},
\]

\[
\begin{aligned}
(X_{\varepsilon,n}^{\mu})_{22}
={}&
\mathbf 1_{n=\mu-2}
\frac{\varepsilon^{\mu-2}}
{12\pi\,2^{\mu-2}(\mu-2)!\,Q^{2\mu-4}}
\\
&+
\mathbf 1_{n\ge\mu}
\frac{\varepsilon^n(q_0^2)^{(n-\mu)}(m)}
{2\pi\,2^n\mu!(n-\mu)!\,Q^{2n}}.
\end{aligned}
\]

For \(n=3\), the nonzero primitive entries are:

\[
X_{\varepsilon,3}^{2}
=
\frac{\varepsilon(q_0^2)'(m)}{64\pi Q^6}(I-D),
\]

\[
X_{\varepsilon,3}^{3}
=
\frac{\varepsilon}{24\pi Q^4}I
+
\frac{\varepsilon}{24\pi Q^4}D
+
\frac{\varepsilon(q_0^2)(m)}{96\pi Q^6}(I-D),
\]

\[
X_{\varepsilon,3}^{4}
=
\frac{\varepsilon}{64\pi Q^5}S,
\]

\[
X_{\varepsilon,3}^{5}
=
\frac{\varepsilon}{2304\pi Q^6}(I-D).
\]

This removes the earlier \(X_{\varepsilon,3}^\mu\) gap.

---

# 4. \(\Lambda^-_{\mu,0..3}\) and \(H^A_{r,0}\)

Let

\[
S_{\varepsilon,n}^{\mu}
=
[z^n]\,D(G_\varepsilon^{(0)1/2})[X^\mu_\varepsilon],
\]

so that

\[
S_{\varepsilon,n}^{\mu}
=
\Sigma_\varepsilon\!\left(
X_{\varepsilon,n}^{\mu}
-
\sum_{j=1}^{n}
\left(
P_{\varepsilon,j}S_{\varepsilon,n-j}^{\mu}
+
S_{\varepsilon,n-j}^{\mu}P_{\varepsilon,j}
\right)
\right).
\]

Explicitly,

\[
S_{\varepsilon,0}^{\mu}=\Sigma_\varepsilon(X_{\varepsilon,0}^{\mu}),
\]

\[
S_{\varepsilon,1}^{\mu}
=
\Sigma_\varepsilon(X_{\varepsilon,1}^{\mu}
-P_{\varepsilon,1}S_{\varepsilon,0}^{\mu}
-S_{\varepsilon,0}^{\mu}P_{\varepsilon,1}),
\]

\[
S_{\varepsilon,2}^{\mu}
=
\Sigma_\varepsilon(X_{\varepsilon,2}^{\mu}
-P_{\varepsilon,1}S_{\varepsilon,1}^{\mu}
-S_{\varepsilon,1}^{\mu}P_{\varepsilon,1}
-P_{\varepsilon,2}S_{\varepsilon,0}^{\mu}
-S_{\varepsilon,0}^{\mu}P_{\varepsilon,2}),
\]

\[
\begin{aligned}
S_{\varepsilon,3}^{\mu}
=
\Sigma_\varepsilon\Big(&
X_{\varepsilon,3}^{\mu}
-P_{\varepsilon,1}S_{\varepsilon,2}^{\mu}
-S_{\varepsilon,2}^{\mu}P_{\varepsilon,1}
\\
&-P_{\varepsilon,2}S_{\varepsilon,1}^{\mu}
-S_{\varepsilon,1}^{\mu}P_{\varepsilon,2}
-P_{\varepsilon,3}S_{\varepsilon,0}^{\mu}
-S_{\varepsilon,0}^{\mu}P_{\varepsilon,3}
\Big).
\end{aligned}
\]

The inverse-square-root Fréchet coefficients are

\[
\Lambda_{\varepsilon,n}^{\mu}
=
-\sum_{i+j+k=n}
W_{\varepsilon,i}S_{\varepsilon,j}^{\mu}W_{\varepsilon,k}.
\]

Hence

\[
H^A_{r,0}
=
\sum_{\mu}A_\mu\Lambda^-_{\mu,r}.
\]

This is fully recursive for \(r=0,1,2,3\), once the source slot \(A_-=\sum_\mu A_\mu X_-^\mu\) is fixed.

---

# 5. \(Y^{\chi}_{g,0}\) coefficient extraction

Let

\[
s=\frac{z}{Q^2},
\qquad
\sigma(z)=\sin\Delta_0(z),
\qquad
\gamma(z)=\cos\Delta_0(z).
\]

Let

\[
d_{i,\varepsilon}(z)=\sum_{n\ge0}d_{i,\varepsilon,n}z^n,
\qquad
\eta_i(z)=\sum_{n\ge0}\eta_{i,n}z^n.
\]

Only these rows survive:

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}.
\]

The \(dd\)-row is

\[
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

So

\[
Y_{g,0}^{dd}
=
-\frac1{2\pi}
[z^g]\frac{\sigma}{s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

The \(d\eta+\eta d\)-row is

\[
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}(d_{1,+}\eta_2+d_{2,+}\eta_1),
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}(d_{1,-}\eta_2+d_{2,-}\eta_1),
\]

\[
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
-\frac1{2\pi}
\Big[
&
\left(\frac{\sigma}{s^2}+\frac{q_+^0\gamma}{s}\right)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
\left(\frac{\sigma}{s^2}+\frac{q_-^0\gamma}{s}\right)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

The \(\eta\eta\)-row is

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
-\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac1{2\pi}
\left[
-\frac{(q_-^0+q_+^0)\gamma}{s^2}
-\frac{2\sigma}{s^3}
+
\frac{q_-^0q_+^0\sigma}{s}
\right]\eta_1\eta_2.
\]

Then

\[
Y^\chi_{g,0}=[z^g]Y_\chi^{(2)},
\qquad
4\le g\le7.
\]

These are finite convolutions of the midpoint jets of

\[
q_0,\quad \Delta_0,\quad d_{i,\pm},\quad \eta_i.
\]

---

# 6. Final executable contraction

The Bottleneck C coefficient is

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
\sum_{\mu}
A_\mu
\Lambda^-_{\mu,r}
Y^\chi_{g,0}
W_{+,b}.
}
\]

Write

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S.
\]

Then

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
\]

and

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
\]

---

# 7. Exactly what is still missing

The finite recurrence table is now derived. The remaining non-derived data are the scalar midpoint source jets needed to evaluate the entries:

\[
q_0^{(k)}(m)
\]

to the order needed for \(G_{\varepsilon,0..3}^{(0)}\), \(W_{\varepsilon,0..3}\), and the \(q_\pm^0\gamma/s\), \(q_-^0q_+^0\sigma/s\) terms in \(Y^\chi\). The safe draft-level jet window is

\[
0\le k\le9.
\]

For the atom source variables, the missing jets are

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9,
\]

equivalently the midpoint Taylor coefficients of

\[
d_{i,\pm}(z),
\qquad
\eta_i(z)
\]

through the orders contributing to

\[
Y^\chi_{g,0},\qquad 4\le g\le7.
\]

The current shared prompt also identifies this as the finite scalar source-jet table required for the local computation. 

---

# 8. Does symmetry force \(Q_{A,Y}=0\) or \(f_{A,Y}=0\)?

No.

The available endpoint-swap / transpose symmetry only gives the reduction to

\[
\operatorname{Sym}
\left(
\Lambda^-_{\mu,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

At the frozen Bottleneck C coefficient, this produces a symmetric fixed-sector element. It does **not** force that element to be:

\[
0,
\]

or proportional to

\[
A_5^{\mathfrak f},
\]

or \(S\)-free.

Thus none of the following is forced by current symmetry:

\[
E_{A,Y}^{\mathrm{BC}}=0,
\]

\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

\[
f_{A,Y}=0.
\]

So the status is:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ remains the first unresolved local coefficient.}
}
\]

The next concrete theorem must either supply the missing scalar source-jet table and compute the contraction, or prove a new structural identity forcing both

\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\quad\text{and}\quad
f_{A,Y}=0.
\]

_Thought for 11s_

## Agent 1 deliverable — \(E_{A,Y}^{\mathrm{BC}}\) remains unevaluated; minimal missing jet table identified

I used the corrected Bottleneck-C carrier:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

I did **not** use the internal \([z^7\delta^1]\) table, because the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge on the Bottleneck-C collision chart, as specified in the prompt. 

The result is:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ cannot yet be evaluated to } eI+fS
\text{ from the draft data alone.}
}
\]

The exact obstruction is the absence of a finite scalar midpoint jet table for the baseline and source variables.

---

# 1. Executable finite contraction

For source slots \(a\in\{1,5\}\),

\[
H^A_{r,0}
=
\sum_{a\in\{1,5\}}A_a\Lambda^-_{a,r}.
\]

Therefore

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}
Y^\chi_{g,0}
W_{+,b}.
}
\]

Write

\[
E_{A,Y}^{\mathrm{BC}}
=
e_{A,Y}I+f_{A,Y}S.
\]

Then the two decisive tests are

\[
\boxed{
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
}
\]

and

\[
\boxed{
f_{A,Y}=0.
}
\]

The first is quotient Bottleneck C. The second is \(T\)-horizontal / transform-safe closure.

---

# 2. \(W_{+,0..3}\) table contract

Let

\[
G_+^{(0)}(z)=\sum_{n\ge0}G_{+,n}^{(0)}z^n,
\]

\[
P_+(z)=G_+^{(0)}(z)^{1/2}
=
\sum_{n\ge0}P_{+,n}z^n,
\]

\[
W_+(z)=G_+^{(0)}(z)^{-1/2}
=
\sum_{n\ge0}W_{+,n}z^n.
\]

Then

\[
P_{+,0}^2=G_{+,0}^{(0)},
\]

and for \(1\le n\le3\),

\[
P_{+,0}P_{+,n}+P_{+,n}P_{+,0}
=
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}.
\]

Thus

\[
P_{+,n}
=
\Sigma_+
\left(
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}
\right),
\]

where \(\Sigma_+\) solves the Sylvester equation

\[
P_{+,0}Z+ZP_{+,0}=C.
\]

Then

\[
W_{+,0}=P_{+,0}^{-1},
\]

and

\[
W_{+,n}
=
-W_{+,0}\sum_{i=1}^{n}P_{+,i}W_{+,n-i},
\qquad 1\le n\le3.
\]

So \(W_{+,0..3}\) is derivable **if** the draft supplies

\[
G_{+,0}^{(0)},G_{+,1}^{(0)},G_{+,2}^{(0)},G_{+,3}^{(0)}.
\]

Those require baseline midpoint jets

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le5
}
\]

at minimum, and the prompt’s safe window is \(0\le k\le9\). 

---

# 3. \(\Lambda^-_{a,0..3}\) table contract

For \(a\in\{1,5\}\), let

\[
X^-_{a,n}
\]

be the same-point source-linear perturbation coefficient in \(G_-^{\corr}\). Define

\[
S^-_{a,n}
=
[z^n]D(G_-^{(0)1/2})[X^-_a].
\]

Then

\[
S^-_{a,n}
=
\Sigma_-
\left(
X^-_{a,n}
-
\sum_{j=1}^{n}
\left(
P_{-,j}S^-_{a,n-j}
+
S^-_{a,n-j}P_{-,j}
\right)
\right).
\]

The inverse-square-root Fréchet coefficient is

\[
\boxed{
\Lambda^-_{a,n}
=
-\sum_{i+j+k=n}
W_{-,i}S^-_{a,j}W_{-,k}.
}
\]

Thus the required entries are

\[
\boxed{
\Lambda^-_{a,r},
\qquad
a\in\{1,5\},
\quad 0\le r\le3.
}
\]

These are derivable **if** the draft supplies the same-point source primitives

\[
\boxed{
X^-_{a,n},
\qquad
a\in\{1,5\},
\quad 0\le n\le3.
}
\]

Equivalently, it needs the midpoint source jets for the two active source families \(a=1,5\):

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad
a\in\{1,5\},
\quad 2\le k\le9.
}
\]

That range is exactly the safe finite source-jet window identified in the current instructions. 

---

# 4. \(Y^\chi_{g,0}\) table contract

Only the symmetric rows enter:

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is excluded.

The required coefficients are

\[
\boxed{
Y^\chi_{g,0}=[z^g]Y_\chi^{(2)},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\quad 4\le g\le7.
}
\]

Using

\[
s=\frac{z}{Q^2},\qquad
\sigma=\sin\Delta_0,\qquad
\gamma=\cos\Delta_0,
\]

the rows are:

\[
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}(d_{1,+}\eta_2+d_{2,+}\eta_1),
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}(d_{1,-}\eta_2+d_{2,-}\eta_1),
\]

\[
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
-\frac1{2\pi}
\Big[
&
\left(\frac{\sigma}{s^2}+\frac{q_+^0\gamma}{s}\right)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
\left(\frac{\sigma}{s^2}+\frac{q_-^0\gamma}{s}\right)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
-\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac1{2\pi}
\left[
-\frac{(q_-^0+q_+^0)\gamma}{s^2}
-\frac{2\sigma}{s^3}
+
\frac{q_-^0q_+^0\sigma}{s}
\right]\eta_1\eta_2.
\]

So this table is derivable **if** the draft supplies the midpoint Taylor coefficients of

\[
d_{i,\pm}(z),\qquad \eta_i(z),\qquad q_\pm^0(z),\qquad \Delta_0(z),
\]

through the orders contributing to \([z^g]\) for \(4\le g\le7\).

The missing scalar jets are again contained in

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le9,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad
a\in\{1,5\},
\quad 2\le k\le9.
}
\]

---

# 5. Minimal missing finite scalar source-jet table

The exact missing table is:

\[
\boxed{
\mathcal J_{\mathrm{base}}
=
\{q_0^{(k)}(m):0\le k\le9\}.
}
\]

\[
\boxed{
\mathcal J_{\mathrm{src}}
=
\{(r_i^{[a]})^{(k)}(m):
i=1,2,\ a\in\{1,5\},\ 2\le k\le9\}.
}
\]

From \(\mathcal J_{\mathrm{base}}\), one derives:

\[
G_{\pm,0..3}^{(0)},
\qquad
P_{\pm,0..3},
\qquad
W_{\pm,0..3}.
\]

From \(\mathcal J_{\mathrm{src}}\), one derives:

\[
X^-_{a,0..3},
\qquad
\Lambda^-_{a,0..3},
\qquad
Y^\chi_{4..7,0}.
\]

Then \(E_{A,Y}^{\mathrm{BC}}\) is obtained by the finite contraction above.

---

# 6. Structural symmetry test

No current structural symmetry forces either decisive vanishing.

Endpoint-swap / transpose symmetry reduces the carrier to the symmetric projection

\[
\operatorname{Sym}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

But this only places the result in the fixed sector after \(\pi_{\mathfrak f_h}\). It does **not** force

\[
E_{A,Y}^{\mathrm{BC}}=0,
\]

nor

\[
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f},
\]

nor

\[
f_{A,Y}=0.
\]

Therefore neither

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0
}
\]

nor

\[
\boxed{
f_{A,Y}=0
}
\]

is structurally proved from the current identities.

---

## Final status

The deliverable is option **3** from the Agent 1 prompt:

\[
\boxed{
\text{a minimal missing finite scalar source-jet table.}
}
\]

The exact missing entries are:

\[
\boxed{
q_0^{(k)}(m),\quad 0\le k\le9,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\quad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
}
\]

Without these, the first live local coefficient remains unresolved:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=eI+fS
\text{ cannot yet be evaluated.}
}
\]
## User (2026-04-25 11:37:28)

do these instructions according to your agent number

## Assistant (2026-04-25 11:37:52)

_Thought for 22s_

## Agent 1 result — deep derivation of \(E_{A,Y}^{\mathrm{BC}}\)

I pushed the derivation again under the corrected Bottleneck-C convention. The active object is the **frozen** coefficient

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

I did **not** use the internal \([z^7\delta^1]\) coefficient, because the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge on the Bottleneck-C chart \(a_2=-a_1(1+\kappa\delta)\). This is explicitly the current bookkeeping correction in the prompt. 

Final status:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=eI+fS
\text{ is not evaluable from the draft alone.}
}
\]

But the remaining missing data are now exactly isolated.

---

# 1. Fully derived contraction

For \(a\in\{1,5\}\),

\[
H^A_{r,0}
=
\sum_{a\in\{1,5\}}A_a\Lambda^-_{a,r}.
\]

Thus the live coefficient is

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}.
}
\]

where

\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is excluded.

Writing

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S,
\]

the decisive tests are

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
\]

and

\[
f_{A,Y}=0.
\]

The first is quotient Bottleneck C; the second is \(T\)-horizontal / transform-safe closure.

---

# 2. Baseline inverse-square-root coefficients \(W_{+,0..3}\)

These are derivable from the paper’s Sylvester recurrence once the baseline midpoint jets are supplied.

Let

\[
G_+^{(0)}(z)=\sum_{n\ge0}G_{+,n}^{(0)}z^n,
\]

\[
P_+(z)=G_+^{(0)}(z)^{1/2}
=
\sum_{n\ge0}P_{+,n}z^n,
\]

\[
W_+(z)=G_+^{(0)}(z)^{-1/2}
=
\sum_{n\ge0}W_{+,n}z^n.
\]

Then

\[
P_{+,0}^2=G_{+,0}^{(0)},
\]

and for \(1\le n\le3\),

\[
P_{+,0}P_{+,n}+P_{+,n}P_{+,0}
=
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}.
\]

Equivalently,

\[
P_{+,n}
=
\Sigma_+
\left(
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}
\right),
\]

where

\[
P_{+,0}Z+ZP_{+,0}=C.
\]

Then

\[
W_{+,0}=P_{+,0}^{-1},
\]

and

\[
W_{+,n}
=
-W_{+,0}\sum_{i=1}^nP_{+,i}W_{+,n-i},
\qquad 1\le n\le3.
\]

So \(W_{+,0..3}\) require only

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le5.
}
\]

The broader \(0\le k\le9\) window is safe, but \(0..5\) is the minimal range for \(W_{+,0..3}\).

---

# 3. Same-point source-linear coefficients \(\Lambda^-_{a,0..3}\)

The same-point source-linear perturbation coefficients are

\[
X^-_{a,n},
\qquad
a\in\{1,5\},
\quad
0\le n\le3.
\]

The square-root Fréchet coefficients are

\[
S^-_{a,n}
=
\Sigma_-
\left(
X^-_{a,n}
-
\sum_{j=1}^{n}
(P_{-,j}S^-_{a,n-j}+S^-_{a,n-j}P_{-,j})
\right).
\]

The inverse-square-root coefficients are

\[
\boxed{
\Lambda^-_{a,n}
=
-\sum_{i+j+k=n}
W_{-,i}S^-_{a,j}W_{-,k}.
}
\]

This derives \(\Lambda^-_{a,0..3}\) from

\[
X^-_{a,0..3}
\]

and the already-derived baseline \(W_-,P_-\) coefficients.

No source normalization in the current draft forces

\[
X^-_{a,3}=0
\]

or

\[
\Lambda^-_{a,3}=0.
\]

Affine removal kills constant and affine source modes; it does **not** kill the grade/order-three terms entering \(X^-_{a,3}\). Source-grade reflection gives parity, not vanishing. Therefore \(r=3\) rows must stay in the table.

---

# 4. \(Y^\chi_{g,0}\) coefficients

The surviving Hessian rows are derivable from the corrected mixed-block formula.

Let

\[
s=\frac{z}{Q^2},
\qquad
\sigma=\sin\Delta_0,
\qquad
\gamma=\cos\Delta_0.
\]

## \(dd\)

\[
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

So

\[
\boxed{
Y^{dd}_{g,0}
=
-\frac1{2\pi}
[z^g]
\frac{\sigma}{s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
}
\]

## \(d\eta+\eta d\)

\[
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}(d_{1,+}\eta_2+d_{2,+}\eta_1),
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}(d_{1,-}\eta_2+d_{2,-}\eta_1),
\]

\[
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
-\frac1{2\pi}
\Big[
&
\left(\frac{\sigma}{s^2}+\frac{q_+^0\gamma}{s}\right)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
\left(\frac{\sigma}{s^2}+\frac{q_-^0\gamma}{s}\right)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

Then

\[
\boxed{
Y^{d\eta+\eta d}_{g,0}
=
[z^g]Y_{d\eta+\eta d}^{(2)}.
}
\]

## \(\eta\eta\)

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
-\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac1{2\pi}
\left[
-\frac{(q_-^0+q_+^0)\gamma}{s^2}
-\frac{2\sigma}{s^3}
+
\frac{q_-^0q_+^0\sigma}{s}
\right]\eta_1\eta_2.
\]

Then

\[
\boxed{
Y^{\eta\eta}_{g,0}
=
[z^g]Y_{\eta\eta}^{(2)}.
}
\]

The required range is

\[
4\le g\le7.
\]

---

# 5. Exact missing scalar jets

The prompt asks not to stop at “source jets are missing,” so I tested whether source normalizations, affine removal, one-amplitude collapse, collision edge laws, and source-grade conventions determine them.

They do not.

They impose admissibility, parity, affine-mode removal, and some divisibility/edge constraints. They do **not** assign the actual midpoint Taylor coefficients needed to evaluate the finite products above.

The exact missing data are:

## Baseline jets

Minimal for the current \(E_{A,Y}^{\mathrm{BC}}\) contraction:

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le7.
}
\]

Reason:

- \(W_{+,0..3}\) needs \(q_0^{(0..5)}(m)\).
- \(Y_{\eta\eta}^{(2)}\) contains \(q_-^0q_+^0\sigma/s\), \(q_\pm^0\gamma/s\), and \((q_-^0+q_+^0)\gamma/s^2\); extracting through \(g=7\) requires \(q_0\)-jets through the same \(z^7\) window.

The broader table

\[
q_0^{(k)}(m),\qquad 0\le k\le9
\]

is safe and matches the working prompt, but \(0..7\) is the minimal range for this carrier.

## Source jets

For the two source families actually used in this carrier:

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad
a\in\{1,5\},
\quad
2\le k\le9.
}
\]

Reason:

- \(d_{i,\pm}\) begins after affine removal and is read through the \(Y_{g,0}\), \(4\le g\le7\), coefficients.
- \(\eta_i\) enters with denominators up to \(s^{-3}\), so its source Taylor data must be known several orders beyond the nominal \(g\le7\) target.
- The draft’s own active local prompt identifies precisely this safe range for the \(E_{A,Y}^{\mathrm{BC}}\) table. 

I cannot reduce \(a\in\{1,5\}\) further: both families appear in \(H^A_{r,0}\), and no current source-grade convention kills either family.

---

# 6. Structural cancellation tests

I tested the available structural mechanisms.

## Endpoint swap

Endpoint swap reduces the two-sided expression to

\[
\operatorname{Sym}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

It does not make the term skew. Therefore it does not kill the fixed-sector projection.

## Transpose invariance of \(\pi_{\mathfrak f}\)

Transpose invariance kills skew terms. The \(Y_{d\eta-\eta d}^{(2)}\) row is killed this way. The surviving rows are symmetric-surviving.

## Source-grade reflection

Source-grade reflection gives parity of coefficients under endpoint swap. It does not imply proportionality to

\[
A_5^{\mathfrak f}.
\]

## Affine removal

Affine removal removes constant and affine source modes. It does not remove the \(d,\eta\) quadratic Hessian terms in \(Y_{12}^{(2)}\), and it does not force \(\Lambda^-_{a,3}=0\).

## One-amplitude collapse / collision divisibility

These explain the amplitude factor

\[
a_1a_2(a_1+a_2),
\]

but they give only the Bottleneck-C edge carrier. They do not force the frozen matrix coefficient to vanish or lie on the \(A_5^{\mathfrak f}\)-line.

## Fixed-sector structure

After projection,

\[
E_{A,Y}^{\mathrm{BC}}=eI+fS.
\]

The known structure supplies the tests

\[
ev_5-u_5f=0
\]

and

\[
f=0,
\]

but no current identity implies either.

Therefore:

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0
\text{ is not structurally forced.}
}
\]

\[
\boxed{
f_{A,Y}=0
\text{ is not structurally forced.}
}
\]

---

# 7. The exact missing theorem

The missing theorem is not another parity lemma. It is a finite scalar source-jet theorem or an explicit coefficient-table theorem.

A theorem-ready statement is:

\[
\boxed{
\textbf{Promoted mixed-block coefficient theorem.}
}
\]

For the actual zeta source jets satisfying the paper’s source normalizations, affine removal, and collision edge laws, the coefficient

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a,\chi,g,r,b}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\]

satisfies

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0
}
\]

and

\[
\boxed{
f_{A,Y}=0.
}
\]

On the generic \(v_5\ne0\) patch, this is equivalent to

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

No theorem currently in the draft proves this.

---

## Final deliverable

The correct deliverable is option **3**:

\[
\boxed{
\text{minimal missing finite scalar source-jet table plus exact missing theorem.}
}
\]

The minimal table is:

\[
\boxed{
q_0^{(k)}(m),\quad 0\le k\le7,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\quad
i=1,2,\quad
a\in\{1,5\},\quad
2\le k\le9.
}
\]

The safe working table is:

\[
\boxed{
q_0^{(k)}(m),\quad 0\le k\le9,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\quad
i=1,2,\quad
a\in\{1,5\},\quad
2\le k\le9.
}
\]

Without this table, the first live local coefficient remains:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ unresolved.}
}
\]

_Thought for 42s_

## Agent 1 result — deep derivation of \(E_{A,Y}^{\mathrm{BC}}\)

I attacked the coefficient again from the draft definitions, recurrences, source normalizations, and table contracts. The result is not just “missing coefficients.” It is:

\[
\boxed{
\text{All transfer-side coefficient machinery is derivable.}
}
\]

\[
\boxed{
\text{The actual scalar source-jet theorem needed to evaluate }E_{A,Y}^{\mathrm{BC}}
\text{ is still absent.}
}
\]

The active coefficient is the frozen Bottleneck-C carrier

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

I did **not** use the internal \([z^7\delta^1]\) table. The prompt explicitly says the amplitude \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge on \(a_2=-a_1(1+\kappa\delta)\), so the Bottleneck-C carrier is the frozen internal coefficient. 

---

# 1. What is fully derivable

## 1.1 \(W_{+,0..3}\)

The baseline same-point block is

\[
G_+^{(0)}(z)=\sum_{n\ge0}G_{+,n}^{(0)}z^n.
\]

Let

\[
P_+(z)=G_+^{(0)}(z)^{1/2}=\sum_{n\ge0}P_{+,n}z^n,
\]

\[
W_+(z)=G_+^{(0)}(z)^{-1/2}=\sum_{n\ge0}W_{+,n}z^n.
\]

Then

\[
P_{+,0}^2=G_{+,0}^{(0)},
\]

and for \(1\le n\le3\),

\[
P_{+,0}P_{+,n}+P_{+,n}P_{+,0}
=
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}.
\]

So

\[
P_{+,n}
=
\Sigma_+
\left(
G_{+,n}^{(0)}
-
\sum_{i=1}^{n-1}P_{+,i}P_{+,n-i}
\right),
\]

where \(\Sigma_+\) solves

\[
P_{+,0}Z+ZP_{+,0}=C.
\]

Then

\[
W_{+,0}=P_{+,0}^{-1},
\]

\[
W_{+,n}
=
-W_{+,0}\sum_{i=1}^{n}P_{+,i}W_{+,n-i},
\qquad 1\le n\le3.
\]

So \(W_{+,0..3}\) is derivable from the finite baseline jets of \(G_+^{(0)}\). No additional structural theorem is needed for the transfer recurrence.

---

## 1.2 \(\Lambda^-_{a,0..3}\)

For the same-point source-linear slot, the draft’s Fréchet/Sylvester calculus gives

\[
S^-_{a,n}
=
\Sigma_-
\left(
X^-_{a,n}
-
\sum_{j=1}^{n}
\bigl(
P_{-,j}S^-_{a,n-j}
+
S^-_{a,n-j}P_{-,j}
\bigr)
\right),
\]

and

\[
\Lambda^-_{a,n}
=
-\sum_{i+j+k=n}
W_{-,i}S^-_{a,j}W_{-,k}.
\]

Thus

\[
H^A_{r,0}
=
\sum_{a\in\{1,5\}}A_a\Lambda^-_{a,r}.
\]

The paper’s affine removal kills constant and affine source modes, but it does **not** imply

\[
X^-_{a,3}=0
\]

or

\[
\Lambda^-_{a,3}=0.
\]

Source-grade reflection gives endpoint parity; it does not give vanishing. One-amplitude collapse and collision divisibility control amplitude structure; they do not remove \(a=1\) or \(a=5\).

So all rows with \(r=0,1,2,3\) remain admissible.

---

## 1.3 \(Y^\chi_{g,0}\)

From the corrected mixed block

\[
N^{\corr}(q_-,q_+,\Delta;s),
\]

the surviving quadratic Hessian rows are exactly

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{(2)}
\]

is excluded.

Let

\[
s=\frac{z}{Q^2},
\qquad
\sigma=\sin\Delta_0,
\qquad
\gamma=\cos\Delta_0.
\]

Then:

\[
Y_{dd}^{(2)}
=
-\frac{\sigma}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{12}
=
-\frac{\sigma}{\pi s}(d_{1,+}\eta_2+d_{2,+}\eta_1),
\]

\[
(Y_{d\eta+\eta d}^{(2)})_{21}
=
\frac{\sigma}{\pi s}(d_{1,-}\eta_2+d_{2,-}\eta_1),
\]

\[
\begin{aligned}
(Y_{d\eta+\eta d}^{(2)})_{22}
=
-\frac1{2\pi}
\Big[
&
\left(\frac{\sigma}{s^2}+\frac{q_+^0\gamma}{s}\right)
(d_{1,-}\eta_2+d_{2,-}\eta_1)
\\
&+
\left(\frac{\sigma}{s^2}+\frac{q_-^0\gamma}{s}\right)
(d_{1,+}\eta_2+d_{2,+}\eta_1)
\Big].
\end{aligned}
\]

\[
(Y_{\eta\eta}^{(2)})_{11}
=
\frac{2\sigma}{\pi s}\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{12}
=
-\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_+^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{21}
=
\frac1\pi
\left(
\frac{\sigma}{s^2}
+
\frac{q_-^0\gamma}{s}
\right)\eta_1\eta_2,
\]

\[
(Y_{\eta\eta}^{(2)})_{22}
=
\frac1{2\pi}
\left[
-\frac{(q_-^0+q_+^0)\gamma}{s^2}
-\frac{2\sigma}{s^3}
+
\frac{q_-^0q_+^0\sigma}{s}
\right]\eta_1\eta_2.
\]

Therefore

\[
Y^\chi_{g,0}=[z^g]Y_\chi^{(2)},
\qquad
4\le g\le7.
\]

This is a finite convolution problem once the midpoint jets of \(q_0,\Delta_0,d_{i,\pm},\eta_i\) are known.

---

# 2. Final finite contraction

Substituting the Fréchet coefficient formula into the Bottleneck-C carrier gives the fully reduced expression

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}.
}
\]

Write

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S.
\]

The two decisive tests are

\[
\boxed{
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
}
\]

and

\[
\boxed{
f_{A,Y}=0.
}
\]

The current prompt also records exactly these two tests: quotient Bottleneck-C closure requires \(Q_{A,Y}=0\), and \(T\)-horizontal closure requires \(f_{A,Y}=0\). 

---

# 3. Structural cancellation tests

I tested the available paper mechanisms.

## Endpoint swap

Endpoint swap pairs the two-sided expression and reduces it to a symmetric projection:

\[
\operatorname{Sym}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

This kills the skew \(d\eta-\eta d\) row, but it does not kill the three surviving rows.

## Transpose invariance of \(\pi_{\mathfrak f}\)

Transpose invariance kills skew matrices. After applying \(\operatorname{Sym}\), the surviving rows are explicitly symmetric-surviving. No additional cancellation follows.

## Source-grade reflection

Source-grade reflection controls parity under endpoint swap. It does not imply

\[
E_\chi\in\mathbf C A_5^{\mathfrak f}
\]

and does not imply

\[
\Phi_K(E_\chi)=0.
\]

## Affine removal

Affine removal removes constant and affine source modes. The surviving \(dd\), \(d\eta+\eta d\), and \(\eta\eta\) rows are quadratic in admissible post-affine source variables, so affine removal does not remove them.

## One-amplitude collapse and collision divisibility

These explain the amplitude factor

\[
a_1a_2(a_1+a_2).
\]

They do not force the frozen coefficient

\[
E_{A,Y}^{\mathrm{BC}}
\]

to vanish, to lie on the \(A_5^{\mathfrak f}\)-line, or to be \(S\)-free.

## Fixed-sector structure

After projection, all that is known is

\[
E_{A,Y}^{\mathrm{BC}}=eI+fS.
\]

The fixed-sector structure supplies the tests

\[
ev_5-u_5f=0
\]

and

\[
f=0,
\]

but it does not imply them.

So no available structural mechanism proves either quotient closure or \(T\)-horizontal closure.

---

# 4. Why the scalar jets are not derivable from the paper

The paper’s coefficient section says the finite Fréchet/Sylvester machinery is a **table contract**, not a completed source table. It requires a finite midpoint-jet theorem for

\[
q_0^{(k)}(m),\qquad 0\le k\le9,
\]

and

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

The prompt repeats this and instructs agents to try deriving those jets rather than merely restating the gap. After testing source normalization, affine removal, one-amplitude collapse, collision edge laws, and coefficient contracts, those mechanisms still do not determine the scalar jet values. 

More precisely:

## Baseline jets

For \(W_{+,0..3}\), the transfer recurrence minimally needs

\[
q_0^{(k)}(m),\qquad 0\le k\le5.
\]

For \(Y^\chi_{g,0}\), because terms include

\[
\frac{q_\pm^0\gamma}{s},
\qquad
\frac{(q_-^0+q_+^0)\gamma}{s^2},
\qquad
\frac{q_-^0q_+^0\sigma}{s},
\]

and we extract \([z^g]\) for \(4\le g\le7\), the minimal safe baseline window is

\[
q_0^{(k)}(m),\qquad 0\le k\le7.
\]

The paper’s Stage 1 contract uses the larger safe window

\[
q_0^{(k)}(m),\qquad 0\le k\le9.
\]

## Source jets

For \(Y^\chi_{g,0}\), the source variables

\[
d_{i,\pm}(z),\qquad \eta_i(z)
\]

must be known through the orders contributing to \(g=4,\ldots,7\), including denominator shifts up to \(s^{-3}\). The safe required table is

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

No theorem in the draft derives these graded source jets from lower package data.

---

# 5. Minimal missing finite source-jet theorem

The exact missing theorem is:

\[
\boxed{
\textbf{Stage 1 graded source-jet realization theorem.}
}
\]

It must state that, in the paper’s ordinary-\(z\), pre-\(\Phi_K\), tagged normalization, the actual zeta source model supplies the finite table

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le9,
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
}
\]

Moreover, it must do so in a way compatible with the same normalization used for

\[
B_7^{\mathfrak f}
\quad\text{and}\quad
Q_{7,m}^q.
\]

Once that theorem is supplied, \(E_{A,Y}^{\mathrm{BC}}\) is obtained from the finite contraction above, and the paper must check:

\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

\[
f_{A,Y}=0.
\]

---

# 6. Final classification

Current status:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f}
\quad\text{not proved.}
}
\]

\[
\boxed{
\Phi_K(E_{A,Y}^{\mathrm{BC}})=0
\quad\text{not proved.}
}
\]

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ remains the first unresolved local obstruction.}
}
\]

Deliverable type: **minimal missing finite source-jet theorem**, with the transfer-side formulas fully derived.
## User (2026-04-25 11:49:39)

Can you attack this: The actual scalar source-jet theorem needed to evaluate EA,YBC​ is still absent.​

## Assistant (2026-04-25 11:49:40)

I’ll attack the missing “actual scalar source-jet theorem” directly: whether the required jets are independent inputs, formally derivable from the local source model, or constrained enough by admissibility/collision laws to force the \(E_{A,Y}^{\mathrm{BC}}\) tests.

_Thought for 31s_

## Attack result

The “actual scalar source-jet theorem” cannot be derived from the current draft’s stated mechanisms. More strongly, in the formal source category defined by the draft’s current normalization rules, the theorem is **false unless an additional zeta-specific jet-realization identity is added**.

The reason is not just “some table is missing.” The problem is structural:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}
\]

depends on finite scalar jets that remain formally free after affine removal, source-grade reflection, one-amplitude collapse, and collision divisibility. The current instructions identify this as the live coefficient and specify the needed coefficient families \(W_{+,0..3}\), \(\Lambda^-_{a,0..3}\), and \(Y^\chi_{g,0}\), with source jets \(q_0^{(k)}(m)\) and \((r_i^{[a]})^{(k)}(m)\) as the suspected inputs. 

---

# 1. What the missing theorem would have to prove

The needed theorem is not merely:

\[
\text{the jets exist.}
\]

They obviously exist formally if the source functions are holomorphic. The needed theorem is much stronger:

\[
\boxed{
\text{the actual zeta-side scalar jets force }
E_{A,Y}^{\mathrm{BC}}
\text{ to be quotient-safe and }T\text{-safe.}
}
\]

Concretely, writing

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S,
\]

it must prove both

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0
}
\]

and

\[
\boxed{
f_{A,Y}=0.
}
\]

The first is quotient Bottleneck C. The second is \(T\)-horizontal / transform-safe closure; the prompt notes the induced slope

\[
\partial_\kappa T=-a_1^2\frac{f_{A,Y}}{c}.
\]

So on a generic \(v_5\ne0\) patch, the missing theorem effectively has to prove

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

---

# 2. What is derivable from the current draft

The transfer machinery is derivable.

One can derive

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3}
\]

from the Sylvester recursion for \(G_+^{(0)-1/2}\), once the baseline scalar jets \(q_0^{(k)}(m)\) are supplied.

One can derive

\[
\Lambda^-_{a,0},\Lambda^-_{a,1},\Lambda^-_{a,2},\Lambda^-_{a,3}
\]

from the Fréchet inverse-square-root recursion, once the same-point source-linear primitives \(X^-_{a,n}\) are supplied.

One can derive

\[
Y^{dd}_{g,0},\quad
Y^{d\eta+\eta d}_{g,0},\quad
Y^{\eta\eta}_{g,0},
\qquad 4\le g\le7,
\]

from the corrected mixed block \(N^{\corr}(q_-,q_+,\Delta;s)\).

But these are only **recurrence contracts**. They do not determine the scalar values of

\[
q_0^{(k)}(m),
\qquad
(r_i^{[a]})^{(k)}(m).
\]

The current prompt explicitly instructs us to try deriving those jets from source normalizations, affine removal, one-amplitude collapse, collision edge laws, and finite coefficient contracts before declaring them missing. I do not find such a derivation in the stated machinery. 

---

# 3. Why affine removal does not determine the table

Affine removal gives

\[
r(h)=0,\qquad r'(h)=0.
\]

Equivalently, it removes constant and affine source modes.

But the live \(E_{A,Y}^{\mathrm{BC}}\) carrier uses quadratic and higher post-affine data through

\[
d_{i,\pm}(z),
\qquad
\eta_i(z),
\]

and through the same-point source-linear slot

\[
A_-=\sum_{a\in\{1,5\}}A_aX^-_a.
\]

Affine removal imposes no relation such as

\[
(r_i^{[a]})^{(k)}(m)=0
\qquad k\ge2.
\]

In particular, it does not force

\[
X^-_{a,3}=0,
\qquad
\Lambda^-_{a,3}=0,
\]

nor does it remove either source family

\[
a=1,\quad a=5.
\]

So affine removal is too weak.

---

# 4. Why source-grade reflection does not determine the table

Source-grade reflection gives parity under endpoint swap. Schematically,

\[
A_+^{[g]}=(-1)^gA_-^{[g]}.
\]

This is enough to kill skew rows, such as

\[
Y_{d\eta-\eta d}^{(2)},
\]

and it explains why the surviving Bottleneck carrier can be written with

\[
\operatorname{Sym}(\cdots).
\]

But after symmetrization the surviving rows are exactly the problematic ones:

\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta.
\]

Source-grade reflection does not imply

\[
\operatorname{Sym}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)=0,
\]

nor does it imply membership in

\[
\mathbf C A_5^{\mathfrak f},
\]

nor does it imply \(S\)-coordinate vanishing.

So parity is not the missing theorem.

---

# 5. Why one-amplitude collapse and collision divisibility do not determine the table

One-amplitude collapse / collision divisibility explains the amplitude pattern

\[
a_1a_2(a_1+a_2).
\]

On

\[
a_2=-a_1(1+\kappa\delta),
\]

this supplies

\[
a_1a_2(a_1+a_2)=a_1^3\kappa\delta+O(\delta^2).
\]

That is why the active coefficient is the **frozen** coefficient, not the internal \([z^7\delta^1]\) source-motion coefficient. This bookkeeping is now fixed. 

But the amplitude law does not constrain the frozen matrix coefficient

\[
E_{A,Y}^{\mathrm{BC}}.
\]

It gives a simple balanced zero. It does not give the stronger quotient condition

\[
E_{A,Y}^{\mathrm{BC}}\in\mathbf C A_5^{\mathfrak f},
\]

and it certainly does not give

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})=0.
\]

So amplitude structure is also too weak.

---

# 6. Formal countermodel to the scalar source-jet theorem

Here is the cleanest way to see the obstruction.

Work in a good local patch and freeze the baseline to the leading model:

\[
W_{+,0}\ne0,
\qquad
W_{+,b}=0\quad(b>0)
\]

for the purpose of testing formal independence. Choose one same-point source slot, say \(a=1\), with

\[
\Lambda^-_{1,0}\ne0.
\]

Now use the \(dd\)-row at \(g=7\):

\[
Y^{dd}_{7,0}
=
-\frac1{2\pi}
[z^7]\frac{\sigma}{s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

The source jets entering

\[
d_{1,-},\quad d_{2,+}
\]

are post-affine jets. Affine removal only says the source has no constant or affine part; it does not fix these higher jets. Therefore we can vary the relevant coefficient of \(d_{1,-}d_{2,+}+d_{2,-}d_{1,+}\) while preserving:

\[
r(h)=0,\qquad r'(h)=0,
\]

endpoint parity,

source-grade reflection,

and the amplitude factor \(a_1a_2(a_1+a_2)\).

The corresponding contribution is

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{1,0}
Y^{dd}_{7,0}
W_{+,0}
\right).
\]

For generic allowed values of the post-affine source jet, this has a nonzero fixed-sector \(S\)-coordinate. There is no current identity tying this \(S\)-coordinate to the quotient line

\[
\mathbf C A_5^{\mathfrak f}.
\]

Thus, in the formal category presently defined by the draft, one can vary a permitted source jet and change

\[
f_{A,Y}
\]

without changing the structural normalization assumptions. Therefore the theorem

\[
f_{A,Y}=0
\]

is not derivable from those assumptions.

Likewise, since

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
\]

is a nontrivial linear functional on the fixed sector, the same variation generically changes \(Q_{A,Y}\). Hence the quotient closure condition is not forced either.

So the missing theorem is not a bookkeeping lemma; it must be a genuine **zeta-specific scalar jet identity** or a direct cancellation theorem.

---

# 7. Minimal theorem that could close the gap

The strongest useful theorem would be:

\[
\boxed{
\textbf{Promoted mixed-block scalar cancellation theorem.}
}
\]

For the actual zeta-side source jets satisfying the paper’s corrected source construction,

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

Expanded:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
=0.
\]

This would close both

\[
Q_{A,Y}=0
\]

and

\[
f_{A,Y}=0.
\]

A weaker quotient-only theorem would be:

\[
\boxed{
e_{A,Y}v_5-u_5f_{A,Y}=0.
}
\]

But that would still leave the \(T\)-slope open unless also

\[
f_{A,Y}=0.
\]

So for the augmented transform-safe proof, the needed theorem is effectively the full vanishing theorem.

---

# 8. Minimal finite source-jet theorem, if one wants a table route

If the proof is to proceed by table evaluation rather than a structural cancellation identity, the missing theorem must supply the following actual scalar jets.

Minimal baseline window:

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le7.
}
\]

Safe baseline window used by the current contracts:

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le9.
}
\]

Source window:

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
}
\]

But merely “supplying” these jets is not enough unless the table then evaluates to

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

or at least to

\[
Q_{A,Y}=0,\qquad f_{A,Y}=0.
\]

Thus the table theorem should be stated as:

\[
\boxed{
\textbf{Stage-1 promoted mixed-block table theorem.}
}
\]

The actual zeta source jets in the finite window above satisfy the finite contraction identity

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

This is the exact finite theorem needed.

---

# 9. Final verdict

The scalar source-jet theorem, as a derivation from existing source normalizations, is **not available** and is formally **not implied** by them.

Current status:

\[
\boxed{
\text{Affine removal removes too little.}
}
\]

\[
\boxed{
\text{Source-grade reflection gives parity, not vanishing.}
}
\]

\[
\boxed{
\text{One-amplitude collapse gives }a_1a_2(a_1+a_2),\text{ not }E_{A,Y}^{\mathrm{BC}}=0.
}
\]

\[
\boxed{
\text{Fixed-sector projection keeps the symmetric rows.}
}
\]

Therefore the next valid mathematical target is one of:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0
\text{ by direct promoted mixed-block cancellation,}
}
\]

or

\[
\boxed{
\text{a finite zeta-specific source-jet table proving }Q_{A,Y}=0
\text{ and }f_{A,Y}=0.
}
\]

Without one of those, \(E_{A,Y}^{\mathrm{BC}}\) remains the first live local obstruction.
## User (2026-04-25 11:58:03)

you are the "next local agent" here

## Assistant (2026-04-25 11:59:22)

_Thought for 1m 17s_

## Local-agent attack result

The promoted mixed-block scalar closure theorem is **not derivable** from the current source conventions. More strongly, there is a formal good-patch model satisfying the paper’s current structural rules in which

\[
E_{A,Y}^{\mathrm{BC}}\neq 0,
\qquad
f_{A,Y}\neq 0,
\qquad
e_{A,Y}v_5-u_5f_{A,Y}\neq0.
\]

So the missing theorem cannot be a bookkeeping lemma. It must be a genuinely new **actual-zeta source-jet cancellation theorem** or a new correction term that cancels this carrier. The attached handoff correctly identifies this as the local blocker: the row table is specified, but the theorem \(E_{A,Y}^{\mathrm{BC}}=0\) is not proved. 

---

# 1. Target

We attack:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}.
\]

Write

\[
E_{A,Y}^{\mathrm{BC}}=eI+fS.
\]

The two required closures are:

\[
Q_{A,Y}:=ev_5-u_5f=0,
\]

and

\[
f=0.
\]

The second is the \(T\)-horizontal condition, since

\[
\partial_\kappa T=-a_1^2\frac{f}{c}.
\]

---

# 2. Channel-by-channel test

The dangerous row is already present in the \(dd\)-channel:

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

This row is:

\[
\chi=dd,
\qquad
a=1,
\qquad
g=4,
\qquad
r=3,
\qquad
b=0.
\]

It contributes

\[
\mathcal E_{dd;4,3,0}^{1}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{1,3}Y^{dd}_{4,0}W_{+,0}
\right).
\]

No present convention removes this row:

- \(Y_{dd}^{(2)}\) is symmetric-surviving, not skew-killed.
- \(a=1\) remains in the active same-point source slot list.
- \(r=3\) is not killed by affine removal.
- \(W_{+,0}\) is invertible on a good patch.
- Source-grade reflection gives parity, not vanishing.
- One-amplitude collapse gives \(a_1a_2(a_1+a_2)\), not matrix cancellation.

Thus, if this single row can produce a nonzero \(S\)-component, full closure cannot follow structurally.

---

# 3. Formal good-patch model

Work in a good patch with

\[
\tau_{h\to m}=\mathrm{id},
\qquad
\pi_{\mathfrak f}(X)=\text{the }(I,S)\text{-fixed-sector part of }X.
\]

Choose baseline whitening

\[
W_{+,0}=I,
\qquad
W_{+,b}=0\quad(b>0).
\]

Choose one active same-point source Fréchet coefficient

\[
\Lambda^-_{1,3}=S,
\]

and set all other \(\Lambda^-_{a,r}\) to zero.

Choose the \(dd\)-Hessian coefficient

\[
Y^{dd}_{4,0}=E_{22}
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\]

and set all other \(Y^\chi_{g,0}\) to zero.

This is compatible with the current formal source conventions:

- \(Y^{dd}_{4,0}\) comes from two post-affine \(d\)-sources beginning at order \(z^2\), so affine removal is respected.
- \(\Lambda^-_{1,3}\) is not forced zero by the Sylvester/Frechet recurrence.
- The skew \(d\eta-\eta d\) row is absent.
- Endpoint-swap parity is irrelevant after the row has been reduced to the frozen symmetric coefficient.

Then the whole coefficient reduces to

\[
E_{A,Y}^{\mathrm{BC}}
=
\pi_{\mathfrak f}
\operatorname{Sym}
\left(
S E_{22}
\right).
\]

But

\[
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
SE_{22}
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

so

\[
\operatorname{Sym}(SE_{22})
=
SE_{22}+E_{22}S
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
=
S.
\]

Therefore

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=S.
}
\]

Thus

\[
e=0,
\qquad
f=1.
\]

The transform-safe condition fails:

\[
\boxed{
f\neq0.
}
\]

The induced hidden-state slope is

\[
\boxed{
\partial_\kappa T=-a_1^2/c\neq0.
}
\]

Now choose a generic quotient line

\[
A_5^{\mathfrak f}=u_5I+v_5S
\]

with

\[
u_5=1,\qquad v_5=1.
\]

Then

\[
Q_{A,Y}=ev_5-u_5f
=
0\cdot 1-1\cdot1
=
-1.
\]

So quotient Bottleneck C also fails:

\[
\boxed{
Q_{A,Y}\neq0.
}
\]

---

# 4. What this proves

This is not a counterexample to the actual zeta function. It is a countermodel to the implication

\[
\text{current source conventions}
\Longrightarrow
E_{A,Y}^{\mathrm{BC}}=0.
\]

The current axioms leave enough freedom in the post-affine scalar source jets to realize a nonzero \(S\)-component in the promoted \(dd\)-row.

Therefore the desired theorem

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

is not a consequence of:

\[
\text{affine removal},
\]

\[
\text{source-grade reflection},
\]

\[
\text{endpoint swap},
\]

\[
\text{one-amplitude collapse},
\]

\[
\text{collision divisibility},
\]

\[
\text{fixed-sector projection}.
\]

It needs an additional identity.

---

# 5. Tests requested in the prompt

## Channel-by-channel

The \(dd\)-channel alone can produce

\[
E_{dd}^{\mathrm{BC}}=S.
\]

So channel-by-channel vanishing fails formally.

## Between \(a=1\) and \(a=5\)

No forced cancellation exists. The model uses only \(a=1\). Since \(a=5\) can be set to zero without violating the current formal conventions, cancellation between \(a=1\) and \(a=5\) is not structural.

## Between \((r,b)\)-partitions

No forced cancellation exists. The model uses only

\[
r=3,\qquad b=0.
\]

All other partitions can be set to zero formally.

## After \(\tau_{h\to m}\pi_{\mathfrak f}\operatorname{Sym}\)

The term survives:

\[
\pi_{\mathfrak f}\operatorname{Sym}(SE_{22})=S.
\]

## After pairing against \(A_5^{\mathfrak f}\)

For \(A_5^{\mathfrak f}=I+S\),

\[
\omega(E,A_5)=ev_5-u_5f=-1.
\]

So quotient closure is not structural.

## After applying \(\Phi_K\)

Since

\[
\Phi_K(eI+fS)=2f,
\]

we get

\[
\Phi_K(E)=2.
\]

So \(T\)-horizontal closure is not structural.

---

# 6. The exact missing theorem

The missing theorem must be stated as a **zeta-specific promoted mixed-block cancellation theorem**, not as a parity theorem.

A theorem-ready form:

```latex
\begin{theorem}[Promoted mixed-block Bottleneck-C scalar closure]
\label{thm:promoted-mixed-block-bottleneck-c-scalar-closure}
For the actual zeta-side corrected source jets in the promoted quadratic
mixed-block channel, one has
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
=0.
\]
Equivalently,
\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\qquad
f_{A,Y}=0.
\]
\end{theorem}
```

A weaker theorem,

\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

would close quotient Bottleneck C but would still leave

\[
\partial_\kappa T=-a_1^2f_{A,Y}/c
\]

open. The augmented package needs \(f_{A,Y}=0\) as well.

---

# 7. Verdict

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0
\text{ is not structurally forced by the current draft.}
}
\]

\[
\boxed{
Q_{A,Y}=0
\text{ is not structurally forced.}
}
\]

\[
\boxed{
f_{A,Y}=0
\text{ is not structurally forced.}
}
\]

The \(dd\)-row formal model gives a nonzero \(S\)-component and a nonzero quotient determinant. Therefore the local proof remains blocked unless the paper proves a new zeta-specific scalar cancellation theorem or modifies the corrected package to cancel this promoted mixed-block channel.
## User (2026-04-25 11:59:51)

continue to attack

## Assistant (2026-04-25 11:59:53)

I’ll continue by treating the formal \(dd\)-row countermodel as a diagnostic: either find a hidden constraint that invalidates it, or convert it into a sharper no-go theorem and identify the minimal repair needed.

_Thought for 29s_

## Continued local attack: stronger formal obstruction

I tightened the previous countermodel. The earlier model used an arbitrary choice such as

\[
\Lambda^-_{1,3}=S.
\]

That was useful diagnostically, but one could object that \(\Lambda^-_{a,r}\) is not arbitrary: it must come from the Fréchet derivative of \(G_-^{-1/2}\). So the next attack is:

\[
\boxed{
\text{Does the actual Fréchet/Sylvester structure itself force }E_{A,Y}^{\mathrm{BC}}=0?
}
\]

Answer:

\[
\boxed{
\text{No. Even with the Fréchet structure imposed, the closure is not formal.}
}
\]

The obstruction already appears in the lowest frozen row

\[
r=0,\qquad b=0,\qquad g=7
\]

of the \(dd\)-channel. The current consolidated prompt identifies this exact coefficient as the stabilized local frontier: \(E_{A,Y}^{\mathrm{BC}}\) is finite-table reduced, the skew row is gone, and no further row reduction is currently justified. turn57file7

---

# 1. Work on a normalized good patch

Choose a good patch where the baseline square-root data are normalized at the midpoint:

\[
G_-^{(0)}(0)=G_+^{(0)}(0)=I,
\]

so

\[
P_{\pm,0}=I,
\qquad
W_{\pm,0}=I.
\]

This does not change the structural question: if the closure theorem is formal, it must survive this good-patch specialization.

For the inverse square-root Fréchet derivative,

\[
D(G^{-1/2})_I[X]=-\frac12 X.
\]

Thus at \(r=0\),

\[
\Lambda^-_{a,0}=-\frac12X^-_{a,0}.
\]

So the row

\[
(r,b,g)=(0,0,7)
\]

contributes

\[
\mathcal E^a_{\chi;7,0,0}
=
-\frac12
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
X^-_{a,0}Y^\chi_{7,0}
\right).
\]

There is no higher Sylvester ambiguity here. This is the direct first Fréchet derivative at the identity baseline.

---

# 2. Specialize to the \(dd\)-row

The \(dd\)-row is

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
\left(
d_{1,-}d_{2,+}
+
d_{2,-}d_{1,+}
\right)E_{22}.
\]

So

\[
Y^{dd}_{7,0}
=
\lambda E_{22}
\]

for some scalar \(\lambda\), where \(\lambda\) is a finite source-jet contraction of the post-affine \(d\)-jets.

The current source conventions do not force

\[
\lambda=0.
\]

Affine removal only removes constant and affine source modes; it does not kill the higher post-affine \(d\)-jet product that feeds \([z^7]\). Source-grade reflection gives parity, not zero. One-amplitude collapse gives the amplitude \(a_1a_2(a_1+a_2)\), not the matrix coefficient. This is precisely why the existing handoff says the draft still does not determine the scalar midpoint source jets needed to evaluate the table. 

Thus the \(dd\)-row contributes

\[
-\frac{\lambda}{2}
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
X^-_{a,0}E_{22}
\right).
\]

---

# 3. The decisive matrix calculation

The only way this row is structurally killed is if every admissible \(X^-_{a,0}\) satisfies

\[
\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
X^-_{a,0}E_{22}
\right)=0
\]

or lies in a direction that cancels against other rows.

But the current conventions do not impose that.

Take an admissible same-point source primitive with off-diagonal \(S\)-component at \(X^-_{a,0}\):

\[
X^-_{a,0}=S.
\]

Then

\[
\operatorname{Sym}(SE_{22})
=
SE_{22}+E_{22}S.
\]

Since

\[
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
E_{22}=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix},
\]

we get

\[
SE_{22}
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
E_{22}S
=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\]

hence

\[
\operatorname{Sym}(SE_{22})
=
S.
\]

Therefore the row gives

\[
\mathcal E^a_{dd;7,0,0}
=
-\frac{\lambda}{2}S.
\]

So

\[
e=0,
\qquad
f=-\frac{\lambda}{2}.
\]

If \(\lambda\neq0\), then

\[
f\neq0.
\]

Thus

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
=
a_1^2\frac{\lambda}{2c}
\neq0.
\]

The \(T\)-horizontal condition fails.

Moreover, for a generic quotient line

\[
A_5^{\mathfrak f}=u_5I+v_5S
\]

with \(u_5\neq0\),

\[
Q_{A,Y}=ev_5-u_5f
=
-u_5f
=
u_5\frac{\lambda}{2}
\neq0.
\]

So quotient Bottleneck C also fails.

---

# 4. Does \(X^-_{a,0}=S\) violate source conventions?

This is the critical check.

A same-point source-linear perturbation enters

\[
G_\pm^{\corr}
=
\frac1\pi
\begin{pmatrix}
2q_\pm & \frac12q_\pm'\\
\frac12q_\pm' & \frac1{12}(q_\pm''+2q_\pm^3)
\end{pmatrix}.
\]

An off-diagonal source component comes from a \(q'\)-source contribution. Affine removal removes raw affine modes in the residual source, but it does not generally impose that every endpoint \(q'\)-source contribution vanishes after the \(\mathfrak D_Q\)-scaled normalization. In the current active table, the \(a\in\{1,5\}\) slots are explicitly retained, and no source-grade convention removes either \(a=1\) or \(a=5\). The local frontier summary also says no further row reduction is currently justified. 

Therefore \(X^-_{a,0}=S\) is a legitimate formal test direction unless the paper adds a theorem explicitly excluding the corresponding off-diagonal source-linear slot.

That theorem is not currently present.

---

# 5. Could other rows cancel this one?

A structural theorem cannot rely on accidental numeric cancellation between independent source jets unless the source model imposes the needed relation.

The row above depends on the scalar coefficient

\[
\lambda=[z^7]Y_{dd}^{(2)}.
\]

Other rows involve different independent scalar contractions:

\[
Y^{dd}_{g,0}\quad(g<7),
\]

\[
Y^{d\eta+\eta d}_{g,0},
\]

\[
Y^{\eta\eta}_{g,0},
\]

and different \((r,b)\)-partitions.

The current source conventions do not impose a relation of the form

\[
\lambda \cdot \pi_{\mathfrak f}\operatorname{Sym}(SE_{22})
+
\sum_{\text{other rows}}
(\text{other independent source contractions})
=0.
\]

Thus cancellation between rows is not structural.

One can set the other scalar contractions formally to zero while keeping

\[
\lambda\neq0
\]

without violating affine removal, endpoint parity, or one-amplitude collapse. That leaves the \(S\)-term above.

---

# 6. Stronger conclusion

The promoted mixed-block scalar closure theorem

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

is **not a consequence of the paper’s current structural source conventions**.

The quotient-only closure

\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\]

is also not structural.

The transform-safe closure

\[
f_{A,Y}=0
\]

is also not structural.

The \(dd\)-row alone supplies a formal good-patch countermodel.

---

# 7. Exact missing local theorem

The missing theorem must be stronger than “derive the finite table.”

It must rule out the \(dd\)-row \(S\)-leakage above. A theorem-ready version is:

```latex
\begin{theorem}[Promoted \(dd\)-row scalar cancellation]
\label{thm:promoted-dd-row-scalar-cancellation}
For the actual zeta-side corrected source jets, the \(dd\)-row contribution
\[
E_{dd}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^{dd}_{g,0}W_{+,b}
\]
satisfies
\[
E_{dd}^{\mathrm{BC}}=0.
\]
\end{theorem}
```

If this is too strong, the minimum needed for the augmented package is:

\[
\boxed{
\Phi_K(E_{dd}^{\mathrm{BC}})=0
}
\]

and

\[
\boxed{
\omega_m(E_{dd}^{\mathrm{BC}},A_5^{\mathfrak f})=0.
}
\]

But the formal test above shows neither follows from the current draft.

---

# 8. Possible repair directions

There are only three mathematically distinct repair paths.

## Repair 1: prove a zeta-specific jet identity

Show that the actual zeta-side source jets force

\[
[z^7]Y_{dd}^{(2)}=0
\]

in every \(S\)-visible contraction, or force cancellation with \(d\eta+\eta d\) and \(\eta\eta\) rows.

This would be a genuine finite source-jet theorem.

## Repair 2: add a correction term

Modify the corrected package so the promoted quadratic mixed-block term has an explicit counterterm cancelling

\[
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-Y_{12}^{(2)}W_+
\right)
\]

at the frozen Bottleneck-C coefficient.

This is a package-design repair, not a proof from the current package.

## Repair 3: weaken the global goal

If the \(S\)-leakage survives but lies on the \(A_5\)-line, quotient Bottleneck C could still close. But the \(T\)-augmented bridge still leaks because

\[
\Phi_K(\lambda A_5^{\mathfrak f})=2\lambda v_5
\]

on the generic \(v_5\neq0\) patch. Therefore this does not repair the full augmented package unless the hidden-state theorem is changed again.

---

## Verdict

The next local obstruction is now even sharper:

\[
\boxed{
\text{the \(dd\)-row }(a,r,g,b)=(a,0,7,0)
\text{ can produce a pure }S\text{-leak.}
}
\]

Unless the actual zeta source model proves this row vanishes or is cancelled by other rows, the promoted mixed-block Bottleneck-C scalar closure fails.
## User (2026-04-25 12:01:14)

continue to attack

## Assistant (2026-04-25 12:01:40)

I found a significant correction to the prior diagnostic model: in the actual draft’s source-linear normal form, the zeroth same-point source primitive is diagonal, not \(S\)-off-diagonal. So the previous \(X^-_{a,0}=S\) countermodel was too loose. I’ll now redo the obstruction using the actual \(X_{\varepsilon,n}^a\) table.

_Thought for 45s_

## Continued local attack — correction and sharper obstruction

I found a material correction to my previous formal model.

The earlier diagnostic used

\[
X^-_{a,0}=S.
\]

That is **not compatible with the actual source-linear normal form in the latest draft**. The draft’s finite Fréchet section gives the source-linear same-point primitives as

\[
X_{\varepsilon,0}^{2}=\frac{1}{24\pi}(I-D),
\]

\[
X_{\varepsilon,1}^{2}=\frac{\varepsilon}{4\pi Q}S,
\qquad
X_{\varepsilon,1}^{3}=\frac{\varepsilon}{48\pi Q^2}(I-D),
\]

\[
X_{\varepsilon,2}^{3}=\frac{1}{16\pi Q^3}S,
\]

with all other \(X_{\varepsilon,n}^a\) for \(n\le2,\ 2\le a\le6\) vanishing. So the actual table has **no off-diagonal \(S\)-source at \(n=0\)**. The first direct off-diagonal source row appears at \(n=1\). This invalidates the \(r=0,g=7,b=0\) pure-\(S\) countermodel. The current local frontier still concerns the frozen \(E_{A,Y}^{\mathrm{BC}}\) coefficient and its two tests \(Q_{A,Y}=e v_5-u_5 f\), \(f=0\). turn60file0

That correction does **not** close the obstruction. It changes the first dangerous row.

---

# 1. Revised first dangerous rows

Because \(X_{\varepsilon,0}^2\) is diagonal,

\[
X_{\varepsilon,0}^{2}\propto I-D=2E_{22},
\]

the \(r=0,g=7,b=0\) \(dd\)-row is not immediately \(S\)-visible on a diagonal baseline.

The first unavoidable issue becomes one of these two mechanisms:

## Mechanism A — quotient-visible diagonal leakage

Take

\[
r=0,\qquad g=7,\qquad b=0,
\]

with the \(dd\)-row.

On the diagonal normalized patch

\[
W_{+,0}=I,
\qquad
\Lambda^-_{2,0}\propto E_{22},
\qquad
Y^{dd}_{7,0}\propto E_{22},
\]

the contribution is

\[
\operatorname{Sym}(E_{22}E_{22})
=
2E_{22}
=
I-D.
\]

After projection to the fixed sector \(\mathfrak f=\mathrm{span}\{I,S\}\), the \(D\)-part drops and the row contributes an \(I\)-component:

\[
\pi_{\mathfrak f}(I-D)=I
\quad
\text{up to normalization.}
\]

So this row is \(T\)-safe because \(f=0\), but it is **not quotient-safe** on the generic \(v_5\ne0\) patch:

\[
Q_{A,Y}=e v_5-u_5 f=e v_5.
\]

Unless either

\[
e=0
\]

or

\[
v_5=0,
\]

this violates quotient Bottleneck C.

But \(v_5=0\) is explicitly not the generic transform-safe patch; the global bridge was repaired precisely because \(v_5\neq0\) makes the hidden \(T\)-coordinate visible.

So the revised formal obstruction is:

\[
\boxed{
\text{even the diagonal \(dd\)-row can be quotient-visible.}
}
\]

## Mechanism B — \(S\)-leakage from the first off-diagonal primitive

The first actual direct \(S\)-source primitive occurs at

\[
X_{\varepsilon,1}^{2}\propto S.
\]

So take the row

\[
r=1,\qquad g=6,\qquad b=0
\]

in the \(dd\)-channel.

If

\[
\Lambda^-_{2,1}
\]

has a nonzero \(S\)-component inherited from \(X^-_{2,1}\), and

\[
Y^{dd}_{6,0}\propto E_{22},
\]

then

\[
\operatorname{Sym}(SE_{22})
=
S.
\]

This gives

\[
e=0,\qquad f\neq0,
\]

so the transform-safe condition fails:

\[
\partial_\kappa T=-a_1^2\frac{f}{c}\neq0.
\]

This is closer to the earlier pure-\(S\) model, but now it uses the actual table-compatible row \(r=1,g=6,b=0\), not the invalid \(r=0,g=7,b=0\) row.

Thus the corrected first \(T\)-visible candidate is:

\[
\boxed{
\mathcal E^{2}_{dd;6,1,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
}
\]

---

# 2. Does the Sylvester recursion kill \(\Lambda^-_{2,1}\)?

No. The source table itself shows

\[
X^-_{2,1}\propto -S.
\]

The first Fréchet recursion gives

\[
S^-_{2,1}
=
\Sigma_-\!\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right).
\]

Then

\[
\Lambda^-_{2,1}
=
-\left(
W_{-,1}S^-_{2,0}W_{-,0}
+
W_{-,0}S^-_{2,1}W_{-,0}
+
W_{-,0}S^-_{2,0}W_{-,1}
\right).
\]

On a normalized patch where

\[
P_{-,0}=I,\qquad W_{-,0}=I,
\]

and where first baseline variation is suppressed for diagnostic purposes,

\[
P_{-,1}=0,\qquad W_{-,1}=0,
\]

we get

\[
S^-_{2,1}=\frac12X^-_{2,1},
\]

and

\[
\Lambda^-_{2,1}=-S^-_{2,1}
=
-\frac12X^-_{2,1}.
\]

Since

\[
X^-_{2,1}\propto S,
\]

we get

\[
\Lambda^-_{2,1}\propto S.
\]

So the first off-diagonal row survives the actual Sylvester structure.

This is a much better countermodel than the previous arbitrary \(\Lambda=S\) choice: it uses the draft’s actual \(X_{\varepsilon,1}^{2}\) primitive.

---

# 3. Is \(Y^{dd}_{6,0}\) forced zero?

No structural rule forces it zero.

The \(dd\)-row is

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

The coefficient

\[
Y^{dd}_{6,0}
\]

is a finite convolution of:

\[
\sin\Delta_0/s,
\qquad
d_{1,\pm},
\qquad
d_{2,\pm}.
\]

Affine removal only says the underlying residual source has no constant or affine mode. It does not kill post-affine \(d\)-jets. Source reflection gives parity. One-amplitude collapse gives the amplitude pattern. None of these imply

\[
Y^{dd}_{6,0}=0.
\]

So, within the current source conventions, \(Y^{dd}_{6,0}\) can be nonzero.

---

# 4. Corrected formal good-patch model

Use the actual source table row

\[
X^-_{2,1}=c_S S,\qquad c_S\ne0.
\]

Choose a good normalized patch:

\[
W_{+,0}=I,
\qquad
W_{\pm,b}=0\ (b>0),
\]

\[
P_{\pm,0}=I,
\qquad
P_{\pm,1}=0.
\]

Then

\[
\Lambda^-_{2,1}=\lambda_S S,
\qquad
\lambda_S\ne0.
\]

Choose the \(dd\)-source coefficient

\[
Y^{dd}_{6,0}=\mu E_{22},
\qquad
\mu\ne0,
\]

and set all other \(Y\)-coefficients to zero. This respects the present formal source rules because \(Y^{dd}\) is a post-affine quadratic source row.

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\pi_{\mathfrak f}
\operatorname{Sym}(\lambda_S S\cdot \mu E_{22})
=
\lambda_S\mu\,\pi_{\mathfrak f}(S)
=
\lambda_S\mu\,S.
\]

Thus

\[
e=0,
\qquad
f=\lambda_S\mu\ne0.
\]

So

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
\ne0.
\]

And for a quotient line with \(u_5\ne0\),

\[
Q_{A,Y}=ev_5-u_5f=-u_5f\ne0.
\]

This is a formal good-patch countermodel **inside the actual source-linear primitive table**, not relying on the invalid \(X_{a,0}=S\) shortcut.

---

# 5. Consequence

The promoted mixed-block scalar closure theorem is not implied by the current draft:

\[
E_{A,Y}^{\mathrm{BC}}=0
\quad\text{is not structurally forced.}
\]

Nor are the weaker conditions:

\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

\[
f_{A,Y}=0.
\]

The \(dd\)-row alone still provides the obstruction, but the correct first \(T\)-visible diagnostic row is:

\[
\boxed{
(a,\chi,g,r,b)=(2,dd,6,1,0),
}
\]

using

\[
X^-_{2,1}\propto S.
\]

And the first quotient-visible diagonal row is:

\[
\boxed{
(a,\chi,g,r,b)=(2,dd,7,0,0),
}
\]

using

\[
X^-_{2,0}\propto I-D.
\]

---

# 6. Important notation correction

The active summaries have often written

\[
a\in\{1,5\}.
\]

But the finite Fréchet table in the latest draft’s “Source-linear same-point primitives” section uses source indices

\[
a=2,3,4,5,6,
\]

and explicitly lists \(X_{\varepsilon,n}^a\) for \(2\le a\le6\). For the actual \(dd\)-row obstruction above, the relevant source index is

\[
a=2.
\]

So the next local table should be aligned to the draft’s actual source index convention. The \(\{1,5\}\) notation appears to belong to a different layer or an earlier agent shorthand. For the current finite Fréchet primitive table, using \(\{1,5\}\) risks indexing the wrong objects.

---

# 7. Missing theorem, now sharpened

The missing theorem should no longer be stated only as “all promoted mixed-block rows cancel.” The first necessary piece is:

```latex
\begin{theorem}[Promoted \(dd\)-row cancellation]
For the actual zeta-side source jets in the finite Fréchet normalization,
the \(dd\)-row contribution
\[
E_{dd}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
\Lambda^-_{2,r}Y^{dd}_{g,0}W_{+,b}
\]
satisfies
\[
E_{dd}^{\mathrm{BC}}=0.
\]
\end{theorem}
```

A weaker but still necessary pair of conditions is:

\[
\omega_m(E_{dd}^{\mathrm{BC}},A_5^{\mathfrak f})=0,
\]

\[
\Phi_K(E_{dd}^{\mathrm{BC}})=0.
\]

The formal rows above show neither follows from the current source conventions.

---

## Verdict

The attack did not close \(E_{A,Y}^{\mathrm{BC}}\), but it improved the diagnosis:

\[
\boxed{
\text{previous \(X_{a,0}=S\) countermodel invalid;}
}
\]

\[
\boxed{
\text{actual source table still gives a valid \(S\)-leak via }X^-_{2,1}\propto S;
}
\]

\[
\boxed{
\text{actual source table also gives quotient-visible diagonal leakage via }X^-_{2,0}\propto I-D.
}
\]

So the local proof remains blocked, and the blocking theorem is now specifically the promoted \(dd\)-row cancellation in the actual finite Fréchet index convention.
## User (2026-04-25 12:02:47)

continue to attack

## Assistant (2026-04-25 12:03:15)

_Thought for 25s_

## Continued local attack — can the \(r=1,g=6\) \(dd\)-leak be killed?

I attacked the corrected first \(T\)-visible row:

\[
\mathcal E^{2}_{dd;6,1,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
\]

This row remains live under the current formal package. I do **not** find a source-grade, parity, amplitude, or fixed-sector mechanism that kills it. The local obstruction is now sharper:

\[
\boxed{
\text{it suffices to prove or refute }
\pi_{\mathfrak f_h}\operatorname{Sym}
(\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0})=0.
}
\]

This is a strict subproblem of the full \(E_{A,Y}^{\mathrm{BC}}\) closure. The current handoff identifies \(E_{A,Y}^{\mathrm{BC}}\) as the stabilized local blocker and says the frozen coefficient, not the internal \(\delta^1\)-coefficient, is the active Bottleneck-C object. turn62file5

---

# 1. Re-evaluate the row with actual source parity

The \(dd\)-middle row is

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22}.
\]

The \(r=1\) same-point primitive from the actual finite Fréchet table is

\[
X^-_{2,1}\propto -S.
\]

Under the normalized baseline test

\[
P_{-,0}=I,\qquad W_{-,0}=I,\qquad P_{-,1}=0,\qquad W_{-,1}=0,
\]

we get

\[
\Lambda^-_{2,1}\propto S.
\]

Thus the row becomes

\[
\operatorname{Sym}
\left(
S\cdot Y^{dd}_{6,0}\cdot W_{+,0}
\right).
\]

On the lowest good-patch test

\[
W_{+,0}=I,
\qquad
Y^{dd}_{6,0}=\mu E_{22},
\]

this gives

\[
\operatorname{Sym}(S E_{22})=\operatorname{Sym}
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
=
S.
\]

So

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\mu' S,
\]

with \(\mu'\neq0\) unless the scalar \(dd\)-coefficient itself vanishes.

Therefore:

\[
f\neq0,
\]

and the hidden-state slope is nonzero:

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}\neq0.
\]

This directly violates the augmented transform-safe condition.

---

# 2. Does endpoint swap kill it?

No.

Endpoint swap is already used to reduce the two-sided expression to

\[
\operatorname{Sym}(\cdots).
\]

That kills the skew row

\[
Y_{d\eta-\eta d}^{(2)},
\]

but it does not kill the symmetric \(dd\)-row.

For this row, the endpoint-swap result is precisely the symmetric matrix

\[
S,
\]

which survives fixed-sector projection.

So endpoint symmetry explains why this row is visible, not why it vanishes.

---

# 3. Does source-grade reflection kill it?

No.

The relevant components have compatible parity:

- \(X^-_{2,1}\) is an odd endpoint coefficient and carries an \(S\)-matrix.
- \(Y^{dd}_{6,0}\) is frozen and symmetric.
- The total Bottleneck-C carrier is frozen internally; the \(\delta^1\)-edge is supplied by amplitude.

Source-grade reflection supplies the sign needed for endpoint pairing. It does not impose

\[
Y^{dd}_{6,0}=0
\]

or

\[
\Lambda^-_{2,1}=0.
\]

So the reflection convention does not remove the row.

---

# 4. Does affine removal kill it?

No.

Affine removal removes source terms with

\[
r(h)=0,\qquad r'(h)=0
\]

imposed after subtracting constant and affine parts. But the \(dd\)-middle term uses

\[
d_{i,\pm}
=
\frac{z^2}{Q^4}U_{i,\pm}(z),
\]

so it is already post-affine. The row \(Y^{dd}_{6,0}\) is built from products of these post-affine \(d\)-sources and from \(\sin\Delta_0/s\). No affine mode is being used.

Likewise, \(X^-_{2,1}\propto S\) comes from the endpoint derivative of an allowed quadratic source primitive. It is not an affine source mode.

Therefore affine removal does not remove this contribution.

---

# 5. Does the amplitude law kill it?

No.

The amplitude factor for the promoted carrier is

\[
a_1a_2(a_1+a_2).
\]

On the Bottleneck-C chart,

\[
a_2=-a_1(1+\kappa\delta),
\]

we have

\[
a_1a_2(a_1+a_2)=a_1^3\kappa\delta+O(\delta^2).
\]

This is exactly why the frozen coefficient matters. The amplitude law supplies the first edge; it does not impose any matrix cancellation on the frozen coefficient.

So the amplitude law turns the surviving \(S\)-component into a \(T\)-slope. It does not kill it.

---

# 6. Does quotient projection hide it?

No.

For

\[
E=\mu S,
\]

we have

\[
e=0,\qquad f=\mu.
\]

The quotient determinant is

\[
Q(E)=ev_5-u_5f=-u_5\mu.
\]

Thus, on a generic \(u_5\neq0\) patch,

\[
Q(E)\neq0.
\]

So this row is not only \(T\)-visible; it is quotient-visible unless the quotient patch lies on \(u_5=0\). The generic \(v_5\neq0\) transform patch does not imply \(u_5=0\), so quotient Bottleneck C is not structurally safe either.

The full status table for this row is:

\[
E=\mu S,\quad \mu\ne0
\]

\[
\Rightarrow\quad
Q_{A,Y}=-u_5\mu,
\]

\[
\Rightarrow\quad
\Phi_K(E)=2\mu,
\]

\[
\Rightarrow\quad
\partial_\kappa T=-a_1^2\mu/c.
\]

---

# 7. Can row-sum cancellation be structural?

Only if the paper proves a relation tying this \(dd\)-coefficient to other rows. No current identity does that.

The dangerous scalar is

\[
\mu
=
[z^6]\left[
-\frac{\sin\Delta_0}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})
\right].
\]

Other rows involve different scalar contractions:

\[
Y^{dd}_{g,0}\quad(g\neq6),
\]

\[
Y^{d\eta+\eta d}_{g,0},
\]

\[
Y^{\eta\eta}_{g,0},
\]

and different \((r,b)\)-partitions. The draft’s current identities do not impose a linear relation forcing the aggregate \(S\)-coordinate to cancel.

Thus row-sum cancellation would have to be a new finite source-jet theorem, not a consequence of the existing structural package.

---

# 8. Even stronger reduction: a one-row missing theorem

The local obstruction can now be reduced to the following one-row theorem.

```latex
\begin{lemma}[First promoted \(dd\)-row vanishing]
\label{lem:first-promoted-dd-row-vanishing}
For the actual zeta-side source jets in the finite Fréchet normalization,
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right)=0.
\]
\end{lemma}
```

If this lemma fails, then in general:

\[
E_{A,Y}^{\mathrm{BC}}\neq0,
\]

\[
Q_{A,Y}\neq0,
\]

and

\[
\partial_\kappa T\neq0.
\]

So this single row is enough to block the local proof.

---

# 9. Formal countermodel, now table-compatible

A formal good-patch countermodel satisfying the current table structure is:

\[
W_{+,0}=I,
\]

\[
\Lambda^-_{2,1}=S,
\]

\[
Y^{dd}_{6,0}=E_{22},
\]

with all other rows set to zero.

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\pi_{\mathfrak f}
\operatorname{Sym}(SE_{22})
=
S.
\]

So

\[
e=0,\qquad f=1.
\]

Then:

\[
Q_{A,Y}=-u_5,
\]

and

\[
\partial_\kappa T=-a_1^2/c.
\]

This is compatible with the current row table and the currently retained source conventions. It is not a counterexample to zeta, but it is a counterexample to deriving the closure from the current formal source axioms.

---

# 10. Updated verdict

The proof is locally blocked unless one proves a **specific promoted \(dd\)-row cancellation theorem**.

The new sharp obstruction is:

\[
\boxed{
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
}
\]

This row can carry both:

\[
\boxed{
\text{quotient leakage }Q_{A,Y}\neq0
}
\]

and

\[
\boxed{
\text{\(T\)-leakage }f_{A,Y}\neq0.
}
\]

The next attack should not be broad \(E_{A,Y}\)-closure. It should try to prove or refute exactly:

\[
\boxed{
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\text{ has zero fixed-sector symmetric projection.}
}
\]

At the current stage, no source-grade, affine-removal, endpoint-swap, or amplitude-divisibility theorem gives that.
## User (2026-04-25 12:03:59)

continue to attack

## Assistant (2026-04-25 12:04:01)

I’ll now attack the one-row obstruction itself, rather than the whole \(E_{A,Y}^{\mathrm{BC}}\) table: compute the parity and leading-source content of \(Y^{dd}_{6,0}\), then see whether the row can vanish for structural reasons.

_Thought for 27s_

## Continued attack — \(Y^{dd}_{6,0}\) is generically nonzero

I attacked the specific one-row obstruction:

\[
\mathcal E^{2}_{dd;6,1,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
\]

This is the right next local target because the previous round reduced the local blocker to \(E_{A,Y}^{\mathrm{BC}}\), and specifically identified the promoted \(dd\)-row as the first row capable of carrying both quotient leakage and \(T\)-leakage. The latest handoff also says the row table is specified and no further row reduction is justified from the current draft. 

The attack result is negative:

\[
\boxed{
Y^{dd}_{6,0}\text{ is not structurally zero.}
}
\]

More precisely, its coefficient can be written explicitly, and the current source conventions do not force it to vanish.

---

# 1. Expand the \(dd\)-row

The \(dd\)-row is

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
\left(
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\right)E_{22}.
\]

Write

\[
K(z):=\frac{\sin\Delta_0(z)}{s}.
\]

Since \(\Delta_0(z)\) is odd in the endpoint separation \(z\), \(\sin\Delta_0(z)\) is odd and \(s=z/Q^2\) is odd, so

\[
K(z)
\]

is even:

\[
K(z)=K_0+K_2z^2+K_4z^4+\cdots.
\]

Write the plus-end source expansion as

\[
d_{i,+}(z)
=
a_{i,2}z^2+a_{i,3}z^3+a_{i,4}z^4+\cdots.
\]

Endpoint reflection gives

\[
d_{i,-}(z)=d_{i,+}(-z)
=
a_{i,2}z^2-a_{i,3}z^3+a_{i,4}z^4-\cdots.
\]

Then

\[
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
\]

is even. Its first terms are:

\[
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
=
P_4z^4+P_6z^6+O(z^8),
\]

where

\[
P_4=2a_{1,2}a_{2,2},
\]

and

\[
P_6=
2(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3}).
\]

Therefore

\[
Y^{dd}_{6,0}
=
-\frac{1}{2\pi}
\left(
K_0P_6+K_2P_4
\right)E_{22}.
\]

Equivalently,

\[
\boxed{
Y^{dd}_{6,0}
=
-\frac{1}{\pi}
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right]E_{22}.
}
\]

This is the explicit scalar row.

---

# 2. Nothing currently forces this scalar to vanish

The scalar coefficient is

\[
\mu_{dd,6}
:=
-\frac{1}{\pi}
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right].
\]

The draft’s current structural rules impose:

- affine removal: \(a_{i,0}=a_{i,1}=0\);
- endpoint reflection: signs alternate between \(+\) and \(-\);
- source-grade parity;
- amplitude factor \(a_1a_2(a_1+a_2)\);
- fixed-sector projection after symmetrization.

But none of these imply

\[
\mu_{dd,6}=0.
\]

Indeed, after affine removal the coefficients

\[
a_{i,2},\quad a_{i,3},\quad a_{i,4}
\]

remain available post-affine source jets. Endpoint reflection was already used in deriving the even combination. It does not set the even coefficient to zero.

So the one-row theorem

\[
Y^{dd}_{6,0}=0
\]

is false in the formal source category unless the actual zeta source model supplies an additional relation:

\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
=0.
\]

No such identity is currently present.

---

# 3. Now include the actual \(\Lambda^-_{2,1}\) structure

The actual finite Fréchet source table gives the first off-diagonal primitive

\[
X^-_{2,1}\propto S.
\]

At a normalized good patch with diagonal baseline square-root,

\[
P_{-,0}\ \text{diagonal},
\qquad
W_{-,0}\ \text{diagonal},
\]

the first inverse-square-root Fréchet coefficient has an \(S\)-component:

\[
\Lambda^-_{2,1}
=
-\sum_{i+j+k=1}W_{-,i}S^-_{2,j}W_{-,k}.
\]

If the first baseline variation is suppressed for diagnostic purposes,

\[
P_{-,1}=0,\qquad W_{-,1}=0,
\]

then

\[
S^-_{2,1}
=
\Sigma_-(X^-_{2,1}),
\]

and since \(X^-_{2,1}\propto S\), one gets

\[
\Lambda^-_{2,1}\propto S.
\]

Even without suppressing \(P_{-,1}\), there is no structural identity forcing the \(S\)-component of \(\Lambda^-_{2,1}\) to vanish; additional terms merely add more baseline-dependent contributions.

Thus the row contains a term of the form

\[
\operatorname{Sym}(S\cdot \mu_{dd,6}E_{22}\cdot W_{+,0}).
\]

For diagonal invertible \(W_{+,0}\), this has an \(S\)-component proportional to \(\mu_{dd,6}\).

---

# 4. The row produces \(T\)-leakage

On the simplest normalized patch

\[
W_{+,0}=I,
\qquad
\Lambda^-_{2,1}=\lambda S,
\qquad
Y^{dd}_{6,0}=\mu_{dd,6}E_{22},
\]

we obtain

\[
\operatorname{Sym}
(\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0})
=
\lambda\mu_{dd,6}\operatorname{Sym}(SE_{22}).
\]

But

\[
\operatorname{Sym}(SE_{22})=S.
\]

Hence

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\lambda\mu_{dd,6}S.
\]

Therefore

\[
e=0,\qquad f=\lambda\mu_{dd,6}.
\]

If

\[
\lambda\mu_{dd,6}\ne0,
\]

then

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
=
-a_1^2\frac{\lambda\mu_{dd,6}}{c}
\ne0.
\]

So the row violates \(T\)-horizontal closure.

---

# 5. The row also produces quotient leakage generically

For

\[
E=\lambda\mu_{dd,6}S,
\]

the quotient determinant is

\[
Q(E)=ev_5-u_5f
=
-u_5\lambda\mu_{dd,6}.
\]

Thus on any patch with

\[
u_5\ne0,
\]

the same row also violates quotient Bottleneck C.

Even if one worked on a special \(u_5=0\) patch, the row would still be \(T\)-visible unless

\[
f=0.
\]

So the augmented package cannot ignore this row.

---

# 6. Could \(K_0\) or \(K_2\) kill it?

No structurally.

Since

\[
K(z)=\frac{\sin\Delta_0(z)}{s},
\]

the leading term is

\[
K_0
=
\frac{\Delta_0'(0)}{s'(0)}
\]

up to the fixed \(Q\)-normalization. In the phase-kernel setting this is essentially the local baseline slope \(q_0(m)\), not structurally zero on a good patch.

The \(K_2\) coefficient contains curvature of the baseline phase and the cubic term from \(\sin\Delta_0\). Again, no current hypothesis forces the specific cancellation

\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}=0.
\]

Thus the obstruction is not killed by baseline phase parity.

---

# 7. Sharpened missing theorem

The missing local theorem can now be reduced to a scalar jet identity for the first \(T\)-visible \(dd\)-row.

A theorem-ready version:

```latex id="p9d3fs"
\begin{lemma}[First \(dd\)-row source-jet cancellation]
\label{lem:first-dd-row-source-jet-cancellation}
For the actual zeta-side source jets in the promoted mixed-block
Bottleneck-C coefficient, write
\[
\frac{\sin\Delta_0(z)}{s}
=
K_0+K_2z^2+O(z^4),
\]
and
\[
d_{i,+}(z)
=
a_{i,2}z^2+a_{i,3}z^3+a_{i,4}z^4+O(z^5).
\]
Then
\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
=0.
\]
\end{lemma}
```

This lemma would imply

\[
Y^{dd}_{6,0}=0.
\]

Without it, the \(r=1,g=6,b=0\) row remains live.

If the actual proof wants cancellation only after full aggregation, the theorem must instead state:

\[
\sum_{a,\chi,g,r,b}
\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)
=0,
\]

but the scalar identity above is the first visible sub-identity.

---

# 8. Verdict

The attack improves the obstruction from a matrix-level row to an explicit scalar source-jet combination:

\[
\boxed{
\mu_{dd,6}
=
-\frac{1}{\pi}
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right].
}
\]

The current draft does not force

\[
\mu_{dd,6}=0.
\]

If

\[
\mu_{dd,6}\ne0,
\]

then the actual source table’s off-diagonal primitive

\[
X^-_{2,1}\propto S
\]

feeds an \(S\)-component into

\[
E_{A,Y}^{\mathrm{BC}},
\]

giving both

\[
f_{A,Y}\ne0
\]

and, generically,

\[
Q_{A,Y}\ne0.
\]

Thus the local proof is now blocked by the scalar \(dd\)-row jet identity above.
## User (2026-04-25 12:05:09)

continue to attack

## Assistant (2026-04-25 12:05:37)

_Thought for 24s_

## Continued attack — the obstruction survives the actual Fréchet derivative

The remaining possible escape was:

\[
\Lambda^-_{2,1}
\]

might be killed by the actual inverse-square-root Fréchet/Sylvester structure, even though

\[
X^-_{2,1}\propto S.
\]

It is **not** killed. In fact, on any nonsingular good patch, the Fréchet derivative of \(G^{-1/2}\) is an injective linear map on the symmetric \(2\times2\) source block. Therefore a nonzero \(X^-_{2,1}\) cannot be sent to zero. The only remaining hope would be that its image always lands in a direction invisible after multiplication by \(Y^{dd}_{6,0}E_{22}\), symmetrization, and \(\pi_{\mathfrak f}\). That also fails generically.

So the local obstruction is sharper:

\[
\boxed{
X^-_{2,1}\neq0
\Longrightarrow
\Lambda^-_{2,1}\neq0
\quad\text{on a good patch,}
}
\]

and the \(dd\)-row can generically create an \(S\)-component in

\[
E_{A,Y}^{\mathrm{BC}}.
\]

This is exactly the active local coefficient the handoff identifies: the frozen Bottleneck-C carrier \(E_{A,Y}^{\mathrm{BC}}\), not the internal \([z^7\delta^1]\) table. 

---

# 1. Fréchet derivative is injective

Let

\[
F(G)=G^{-1/2}.
\]

On a good patch, \(G\) is invertible and the chosen square-root branch is nonsingular. The Fréchet derivative

\[
DF_G[X]
\]

is injective on symmetric \(2\times2\) perturbations.

One way to see this is by diagonalizing \(G\). In a basis where

\[
G=\operatorname{diag}(\lambda_1,\lambda_2),
\qquad
\lambda_i\neq0,
\]

the Fréchet derivative of \(f(t)=t^{-1/2}\) is the Loewner operator

\[
(DF_G[X])_{ij}
=
f^{[1]}(\lambda_i,\lambda_j)X_{ij},
\]

where

\[
f^{[1]}(\lambda_i,\lambda_j)
=
\begin{cases}
\dfrac{\lambda_i^{-1/2}-\lambda_j^{-1/2}}{\lambda_i-\lambda_j},
&\lambda_i\neq\lambda_j,\\[2ex]
-\dfrac12\lambda_i^{-3/2},
&\lambda_i=\lambda_j.
\end{cases}
\]

These divided differences are nonzero on a good branch. Hence

\[
DF_G[X]=0
\quad\Longrightarrow\quad
X=0.
\]

Therefore the nonzero source primitive

\[
X^-_{2,1}\propto S
\]

cannot be annihilated by the inverse-square-root Fréchet map.

So

\[
\boxed{
\Lambda^-_{2,1}\neq0
}
\]

unless the source primitive itself is removed, which the current source conventions do not do.

---

# 2. What \(\Lambda^-_{2,1}\) looks like

At the identity-normalized baseline,

\[
G_-^{(0)}(0)=I,
\]

we get

\[
DF_I[X]=-\frac12X.
\]

So

\[
\Lambda^-_{2,1}
=
-\frac12X^-_{2,1}
+
\text{baseline-variation terms}.
\]

Since the actual primitive table gives

\[
X^-_{2,1}\propto S,
\]

the leading component is

\[
\Lambda^-_{2,1}
=
\lambda_S S+\lambda_I I+\lambda_DD,
\]

with

\[
\lambda_S\neq0
\]

on a generic good patch.

The \(I,D\) components may be modified by baseline terms, but no current identity forces the \(S\)-coefficient to vanish. The handoff explicitly says no further row reduction is currently justified for the finite \(E_{A,Y}^{\mathrm{BC}}\) table. 

---

# 3. Multiplication by the \(dd\)-row exposes the \(S\)-component

The dangerous \(dd\)-row is

\[
Y^{dd}_{6,0}=\mu_{dd,6}E_{22}.
\]

Thus the relevant product is

\[
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
\right).
\]

In the identity-normalized right patch,

\[
W_{+,0}=I,
\]

and for

\[
\Lambda^-_{2,1}=\lambda_S S+\lambda_I I+\lambda_DD,
\]

we compute:

\[
\operatorname{Sym}(IE_{22})=2E_{22}=I-D,
\]

\[
\operatorname{Sym}(DE_{22})=-2E_{22}=-(I-D),
\]

\[
\operatorname{Sym}(SE_{22})=S.
\]

Therefore

\[
\pi_{\mathfrak f}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}
\right)
=
(\lambda_I-\lambda_D)I+\lambda_SS.
\]

So the \(S\)-coefficient is exactly

\[
f=\lambda_S\mu_{dd,6}.
\]

Since neither

\[
\lambda_S
\]

nor

\[
\mu_{dd,6}
\]

is structurally zero, the row is generically \(T\)-visible.

---

# 4. The scalar \(\mu_{dd,6}\) remains free

Earlier we derived

\[
Y^{dd}_{6,0}
=
\mu_{dd,6}E_{22},
\]

where

\[
\mu_{dd,6}
=
-\frac{1}{\pi}
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right],
\]

with

\[
\frac{\sin\Delta_0(z)}{s}=K_0+K_2z^2+O(z^4),
\]

\[
d_{i,+}(z)=a_{i,2}z^2+a_{i,3}z^3+a_{i,4}z^4+O(z^5).
\]

The current source conventions impose affine removal, endpoint parity, and amplitude structure; they do not impose the scalar identity

\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}=0.
\]

Thus

\[
\boxed{
\mu_{dd,6}\neq0
\quad\text{is formally allowed.}
}
\]

---

# 5. Consequences for quotient and \(T\)

For the row

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\mu_{dd,6}
\pi_{\mathfrak f}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
\right),
\]

we get, on the identity-normalized patch,

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\mu_{dd,6}
\left[
(\lambda_I-\lambda_D)I+\lambda_SS
\right].
\]

Hence

\[
e=\mu_{dd,6}(\lambda_I-\lambda_D),
\]

\[
f=\mu_{dd,6}\lambda_S.
\]

The transform-safe condition is

\[
f=0.
\]

This requires

\[
\mu_{dd,6}\lambda_S=0.
\]

Neither factor is structurally zero.

The quotient condition is

\[
Q=ev_5-u_5f
=
\mu_{dd,6}\left[
(\lambda_I-\lambda_D)v_5-u_5\lambda_S
\right].
\]

This is not structurally zero either. For generic

\[
(u_5,v_5)
\]

and generic

\[
(\lambda_I-\lambda_D,\lambda_S),
\]

the quotient determinant is nonzero.

So the row can violate both:

\[
Q_{A,Y}=0
\]

and

\[
f_{A,Y}=0.
\]

---

# 6. Can a non-identity \(W_{+,0}\) save it?

No generically.

Let \(W_{+,0}\) be an arbitrary good-patch invertible symmetric matrix:

\[
W_{+,0}
=
\alpha I+\beta D+\gamma S.
\]

Then

\[
\operatorname{Sym}
\left(
S E_{22} W_{+,0}
\right)
\]

has a nonzero \(S\)-component for an open set of \((\alpha,\beta,\gamma)\). In particular, the identity case

\[
(\alpha,\beta,\gamma)=(1,0,0)
\]

already gives \(S\). Since vanishing of the \(S\)-component would be an algebraic condition on \(\alpha,\beta,\gamma\), it cannot be forced on a good patch unless the paper states a special baseline constraint. It does not.

Thus right whitening does not structurally remove the row.

---

# 7. Could other rows cancel this one?

Only by a new source-jet identity.

The \(S\)-component from this row is proportional to

\[
\lambda_S\mu_{dd,6}.
\]

Other rows involve different scalar source contractions:

\[
Y^{dd}_{g,0}\quad(g\neq6),
\]

\[
Y^{d\eta+\eta d}_{g,0},
\]

\[
Y^{\eta\eta}_{g,0},
\]

and different Fréchet coefficients

\[
\Lambda^-_{a,r}.
\]

No current identity links these contractions so that the aggregate \(S\)-coordinate must cancel. The handoff says that the next local theorem to attack is exactly the promoted mixed-block scalar closure theorem \(E_{A,Y}^{\mathrm{BC}}=0\); if it fails, the local proof likely fails unless a new correction package cancels the channel. 

---

# 8. Stronger formal no-go statement

The current source conventions allow a local formal model with:

\[
\mu_{dd,6}\neq0,
\qquad
\lambda_S\neq0,
\]

and all other promoted rows set to zero.

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\mu_{dd,6}\lambda_S S.
\]

Therefore

\[
f_{A,Y}\neq0,
\]

\[
\partial_\kappa T=-a_1^2f_{A,Y}/c\neq0,
\]

and, if \(u_5\neq0\),

\[
Q_{A,Y}=-u_5f_{A,Y}\neq0.
\]

So:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0
\text{ is not derivable from the current structural package.}
}
\]

\[
\boxed{
Q_{A,Y}=0
\text{ is not derivable.}
}
\]

\[
\boxed{
f_{A,Y}=0
\text{ is not derivable.}
}
\]

---

# 9. Exact theorem needed now

The local missing theorem can be stated narrowly:

```latex
\begin{theorem}[First \(dd\)-row promoted Bottleneck-C cancellation]
For the actual zeta-side source jets and the actual finite Fréchet
normalization, the coefficient
\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right)
\]
satisfies
\[
E_{dd;6,1,0}^{\mathrm{BC}}=0.
\]
\end{theorem}
```

Expanded, this requires at least one of the following actual-zeta identities:

\[
\lambda_S=0,
\]

or

\[
\mu_{dd,6}=0,
\]

or an exact cancellation against other rows.

But the current draft proves none of these.

---

## Verdict

The obstruction survives a stricter attack using the actual Fréchet derivative. The row

\[
\boxed{
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
}
\]

is the first concrete local blocker.

It can produce a nonzero \(S\)-component, hence nonzero \(T\)-slope, and generically a nonzero quotient determinant. The local proof cannot advance without a new zeta-specific cancellation theorem or a correction term that cancels this promoted \(dd\)-row.
## User (2026-04-25 12:06:20)

continue to attack

## Assistant (2026-04-25 12:06:24)

I’ll tighten the obstruction by removing the remaining “identity baseline” simplification. The key question is whether a general diagonal good patch can still carry the \(X^-_{2,1}\to S\) leakage through the Sylvester and inverse-square-root recurrences.

_Thought for 18s_

## Continued attack — the \(S\)-leak survives a general diagonal good patch

I removed the remaining simplification \(G^{(0)}=I\). The obstruction still survives on a general diagonal good patch. The relevant row remains

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
\]

This is the correct local object because the active Bottleneck-C coefficient is the frozen internal coefficient \(E_{A,Y}^{\mathrm{BC}}\), not the internal \([z^7\delta^1]\) coefficient. 

The result is still negative:

\[
\boxed{
\text{The first \(dd\)-row can produce an \(S\)-component on an open good patch.}
}
\]

So the local proof still needs a new zeta-specific cancellation theorem.

---

# 1. General diagonal baseline

Work at the frozen midpoint and choose a good patch where

\[
P_{-,0}
=
\begin{pmatrix}
p&0\\
0&q
\end{pmatrix},
\qquad
p,q\neq0,
\]

so

\[
W_{-,0}
=
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix}.
\]

This is already more general than the identity-normalized model.

The Sylvester solver

\[
\Sigma_-(C)=Z
\]

is defined by

\[
P_{-,0}Z+ZP_{-,0}=C.
\]

For the off-diagonal source primitive

\[
X^-_{2,1}=cS
=
c
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad c\neq0,
\]

we get

\[
\Sigma_-(X^-_{2,1})
=
\frac{c}{p+q}S.
\]

Thus the square-root Fréchet coefficient has a nonzero \(S\)-component unless \(p+q=\infty\) or \(c=0\), neither of which is allowed on a good patch.

---

# 2. Include the inverse-square-root derivative

Ignoring baseline first-order variation for the moment, the leading contribution is

\[
\Lambda^-_{2,1}
=
-W_{-,0}\Sigma_-(X^-_{2,1})W_{-,0}
+
\text{baseline-variation terms}.
\]

Therefore

\[
\Lambda^-_{2,1}
=
-\frac{c}{p+q}
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix}
S
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix}
+
\cdots
\]

and hence

\[
\Lambda^-_{2,1}
=
-\frac{c}{pq(p+q)}S+\cdots.
\]

So the \(S\)-coefficient of \(\Lambda^-_{2,1}\) is nonzero on an open set.

The omitted baseline-variation terms are algebraic in

\[
P_{-,1},\quad W_{-,1},\quad S^-_{2,0}.
\]

They may modify the coefficient, but they cannot force it to vanish identically unless the paper proves a special relation among baseline and source jets. No current source-grade, affine-removal, or collision-divisibility statement supplies such a relation.

Thus

\[
\boxed{
\lambda_S(\Lambda^-_{2,1})\not\equiv0.
}
\]

---

# 3. Multiply by the \(dd\)-row

The row has

\[
Y^{dd}_{6,0}
=
\mu_{dd,6}E_{22},
\]

where

\[
\mu_{dd,6}
=
-\frac{1}{\pi}
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right].
\]

No current theorem forces

\[
\mu_{dd,6}=0.
\]

Now let

\[
W_{+,0}
=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}
\]

on a diagonal right good patch, with \(u,v\neq0\).

Then the \(S\)-part of the row is governed by

\[
\operatorname{Sym}
\left(
S E_{22}W_{+,0}
\right).
\]

Compute:

\[
S E_{22}
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\]

so

\[
S E_{22}W_{+,0}
=
\begin{pmatrix}
0&v\\
0&0
\end{pmatrix}.
\]

Thus

\[
\operatorname{Sym}
\left(
S E_{22}W_{+,0}
\right)
=
\begin{pmatrix}
0&v\\
v&0
\end{pmatrix}
=
vS.
\]

Therefore the row has an \(S\)-component

\[
f_{dd;6,1,0}
=
-\frac{c}{pq(p+q)}\,\mu_{dd,6}\,v
+
\text{baseline-variation corrections}.
\]

This is not identically zero.

---

# 4. Baseline variation cannot structurally save it

The full \(\Lambda^-_{2,1}\) is

\[
\Lambda^-_{2,1}
=
-\left(
W_{-,1}S^-_{2,0}W_{-,0}
+
W_{-,0}S^-_{2,1}W_{-,0}
+
W_{-,0}S^-_{2,0}W_{-,1}
\right).
\]

Here

\[
S^-_{2,1}
=
\Sigma_-
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right).
\]

The term from \(X^-_{2,1}\) is already nonzero in the \(S\)-direction. The remaining baseline-variation terms could cancel it only if the baseline jets satisfy a special algebraic relation.

But the current draft does not impose such a relation. The handoff explicitly says no further row reduction is currently justified and that the theorem to attack is the promoted mixed-block scalar closure \(E_{A,Y}^{\mathrm{BC}}=0\). 

Thus the cancellation is not structural.

---

# 5. Consequence for quotient and \(T\)

For this row,

\[
E_{dd;6,1,0}^{\mathrm{BC}}
=
eI+fS
\]

with generically

\[
f\neq0.
\]

Therefore the \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c_{\mathrm{norm}}},
\]

where \(c_{\mathrm{norm}}\) is the package normalization scalar. Hence

\[
\boxed{
\partial_\kappa T\neq0
}
\]

generically.

The quotient determinant is

\[
Q=ev_5-u_5f.
\]

Even if the row’s \(I\)-component happened to vanish, the \(S\)-component gives

\[
Q=-u_5f,
\]

so quotient Bottleneck C also fails on a generic \(u_5\neq0\) patch.

Thus the first \(dd\)-row can break both:

\[
Q_{A,Y}=0
\]

and

\[
f_{A,Y}=0.
\]

---

# 6. Sharper missing identity

The proof now needs either:

\[
\boxed{
\mu_{dd,6}=0,
}
\]

or

\[
\boxed{
\lambda_S(\Lambda^-_{2,1})=0,
}
\]

or an exact cancellation against other rows.

Expanded, the first option is the scalar source-jet identity:

\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
=0.
\]

The second option is an inverse-square-root Fréchet identity saying the \(S\)-component of \(\Lambda^-_{2,1}\) vanishes despite

\[
X^-_{2,1}\propto S.
\]

But the Fréchet derivative calculation shows this is false on a generic good patch.

So the only plausible repair is a genuine source-jet cancellation or an aggregate cancellation with other rows.

---

# 7. Formal no-go statement

A theorem-ready no-go lemma is:

```latex
\begin{lemma}[Formal survival of the first promoted \(dd\)-row]
In the formal source category determined by affine removal, endpoint
reflection, source-grade parity, one-amplitude collapse, and the finite
Fréchet/Sylvester coefficient calculus, the coefficient
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right)
\]
is not forced to vanish, is not forced to lie in
\(\mathbf C A_5^{\mathfrak f}\), and is not forced to lie in
\(\ker\Phi_K\).
\]
\end{lemma}
```

This is not a counterexample to zeta. It is a no-go for deriving the local closure from the present formal source axioms alone.

---

## Verdict

The obstruction survives the general diagonal good-patch computation.

The first concrete blocking coefficient is still

\[
\boxed{
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right).
}
\]

It can generically produce a nonzero \(S\)-component, hence a nonzero \(T\)-slope, and generically a nonzero quotient determinant. The proof now needs a new zeta-specific identity or an added correction that cancels this row.
## User (2026-04-25 12:07:18)

continue to attack

## Assistant (2026-04-25 12:07:30)

I’ll push one level deeper: isolate a single source monomial inside \(Y^{dd}_{6,0}\) and check whether it can be cancelled by other rows or by the \(r+b=1\) partition sum.

_Thought for 23s_

## Continued local attack — isolate a single uncancellable source monomial

I pushed the \(dd\)-row obstruction one step further. The goal was to test whether the dangerous row

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}Y^{dd}_{6,0}W_{+,0}
\right)
\]

could be cancelled by another row in the same \(E_{A,Y}^{\mathrm{BC}}\) table.

The answer is still negative. A single source monomial inside \(Y^{dd}_{6,0}\) can be isolated so that no \(d\eta+\eta d\), \(\eta\eta\), lower \(dd\)-row, or \(r+b\)-partition cancellation is structurally available.

This reinforces the current local diagnosis: the frozen \(E_{A,Y}^{\mathrm{BC}}\) coefficient is the active Bottleneck-C carrier, and the decisive tests remain \(Q_{A,Y}=e v_5-u_5 f\) and \(f=0\). 

---

# 1. Isolate a source monomial in \(Y^{dd}_{6,0}\)

Recall

\[
Y_{dd}^{(2)}
=
-\frac{\sin\Delta_0}{2\pi s}
(d_{1,-}d_{2,+}+d_{2,-}d_{1,+})E_{22}.
\]

Write

\[
\frac{\sin\Delta_0(z)}{s}
=
K_0+K_2z^2+O(z^4),
\]

and

\[
d_{i,+}(z)
=
a_{i,2}z^2+a_{i,3}z^3+a_{i,4}z^4+O(z^5),
\]

\[
d_{i,-}(z)
=
a_{i,2}z^2-a_{i,3}z^3+a_{i,4}z^4+O(z^5).
\]

Then

\[
d_{1,-}d_{2,+}+d_{2,-}d_{1,+}
=
2a_{1,2}a_{2,2}z^4
+
2(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})z^6
+
O(z^8).
\]

Therefore

\[
Y^{dd}_{6,0}
=
-\frac1\pi
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right]E_{22}.
\]

Now isolate the monomial

\[
\boxed{
a_{1,2}a_{2,4}.
}
\]

Its coefficient in \(Y^{dd}_{6,0}\) is

\[
\boxed{
-\frac{K_0}{\pi}E_{22}.
}
\]

On a good phase patch,

\[
K_0\neq0
\]

generically.

---

# 2. This monomial does not occur in the other \(Y\)-channels

The other surviving channels are

\[
Y_{d\eta+\eta d}^{(2)},
\qquad
Y_{\eta\eta}^{(2)}.
\]

They contain \(\eta\)-source variables. The monomial

\[
a_{1,2}a_{2,4}
\]

is purely \(dd\). It cannot be cancelled by \(d\eta\) or \(\eta\eta\) rows unless the source model imposes a relation identifying \(d\)-jets with \(\eta\)-jets.

No current source convention does this. The prompt’s local branch keeps the surviving rows

\[
dd,\quad d\eta+\eta d,\quad \eta\eta
\]

as separate coefficient families, with the skew \(d\eta-\eta d\) row removed, not as constrained dependent variables. 

So cancellation with \(d\eta+\eta d\) or \(\eta\eta\) is not structural.

---

# 3. This monomial does not occur in lower \(dd\)-rows

The lower \(dd\)-rows are:

\[
Y^{dd}_{4,0},\qquad
Y^{dd}_{5,0}.
\]

Their source monomials are:

\[
Y^{dd}_{4,0}:\quad a_{1,2}a_{2,2},
\]

\[
Y^{dd}_{5,0}:\quad a_{1,2}a_{2,3}-a_{1,3}a_{2,2}
\quad
\text{or its symmetrized analogue}.
\]

They do not contain

\[
a_{1,2}a_{2,4}.
\]

The \(K_2a_{1,2}a_{2,2}\) part of \(Y^{dd}_{6,0}\) can mix conceptually with lower baseline curvature, but the monomial

\[
a_{1,2}a_{2,4}
\]

is isolated in \(Y^{dd}_{6,0}\).

Thus lower \(g\)-rows cannot cancel the isolated coefficient unless there is a source-jet relation expressing \(a_{2,4}\) in terms of lower jets. The draft does not currently supply such a relation.

---

# 4. Only two \(r+b\) partitions can touch it

For \(g=6\), the Bottleneck-C table condition

\[
r+b=7-g
\]

gives only

\[
(r,b)=(1,0),
\qquad
(r,b)=(0,1).
\]

Thus the isolated \(a_{1,2}a_{2,4}\)-piece of the \(dd\)-row contributes

\[
-\frac{K_0}{\pi}a_{1,2}a_{2,4}\,
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right).
\]

This is the exact partition-level obstruction.

Call the matrix coefficient

\[
\boxed{
\mathcal M_{dd,6}
:=
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right).
}
\]

Then the isolated source monomial contributes

\[
-\frac{K_0}{\pi}a_{1,2}a_{2,4}\mathcal M_{dd,6}.
\]

To kill this monomial structurally, the paper would need

\[
\boxed{
\mathcal M_{dd,6}=0.
}
\]

---

# 5. The partition sum is not structurally zero

On a good patch, choose a baseline with

\[
W_{+,1}=0.
\]

This is compatible with a locally constant first baseline jet in the formal model and does not violate the fixed good-patch assumptions.

Then

\[
\mathcal M_{dd,6}
=
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
\right).
\]

As shown earlier, the actual source-linear table gives

\[
X^-_{2,1}\propto S,
\]

and the inverse-square-root Fréchet derivative is injective on a good patch. Hence

\[
\Lambda^-_{2,1}
\]

has a generically nonzero \(S\)-component.

On a diagonal right-whitening patch

\[
W_{+,0}=\operatorname{diag}(u,v),
\qquad u,v\neq0,
\]

we get

\[
\operatorname{Sym}
\left(
S E_{22} W_{+,0}
\right)
=
vS.
\]

Therefore

\[
\mathcal M_{dd,6}
\]

has a generically nonzero \(S\)-component.

So the partition sum is not identically zero.

---

# 6. Consequences

The isolated source monomial gives

\[
E_{A,Y}^{\mathrm{BC}}
\supset
C\,a_{1,2}a_{2,4}\,S,
\qquad C\neq0
\]

in the formal good-patch model.

Therefore

\[
f_{A,Y}\neq0.
\]

The \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
\neq0.
\]

The quotient determinant is

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}.
\]

For the isolated \(S\)-component, \(e=0\), hence

\[
Q_{A,Y}=-u_5f_{A,Y}.
\]

On a generic \(u_5\neq0\) patch,

\[
Q_{A,Y}\neq0.
\]

Thus the same monomial can break both the quotient Bottleneck-C condition and the transform-safe \(T\)-horizontal condition.

---

# 7. New sharper missing theorem

The local closure requires at least the following partition-level identity:

```latex
\begin{lemma}[Isolated \(dd\)-jet partition cancellation]
For the actual zeta-side source jets and the actual finite Fréchet
normalization,
\[
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right)=0.
\]
\end{lemma}
```

Alternatively, the source jets would need to satisfy

\[
a_{1,2}a_{2,4}=0
\]

or a relation cancelling this monomial against other \(dd\)-terms. Neither is implied by affine removal, endpoint reflection, source-grade parity, or one-amplitude collapse.

---

# 8. Updated verdict

The obstruction is now isolated to one monomial and one matrix identity:

\[
\boxed{
a_{1,2}a_{2,4}
\quad\text{inside}\quad
Y^{dd}_{6,0}
}
\]

and

\[
\boxed{
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right).
}
\]

Unless the paper proves that this matrix coefficient vanishes, or that the actual zeta source jets eliminate the isolated \(a_{1,2}a_{2,4}\) monomial, the promoted mixed-block scalar closure theorem fails.

This is a sharper local blocker than the full \(E_{A,Y}^{\mathrm{BC}}\) table.
## User (2026-04-25 12:08:55)

continue to attack

## Assistant (2026-04-25 12:09:02)

I’ll now attack the only plausible structural cancellation left in that isolated monomial: the two partition terms \((r,b)=(1,0)\) and \((0,1)\). The question is whether the Sylvester recurrences force their sum to vanish.

_Thought for 45s_

## Continued attack — include the \((r,b)=(0,1)\) partition

The prior obstruction used only

\[
(r,b)=(1,0):
\qquad
\operatorname{Sym}(\Lambda^-_{2,1}E_{22}W_{+,0}).
\]

But for \(g=6\), the full \(r+b=1\) contribution is

\[
\boxed{
\mathcal M_{dd,6}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right).
}
\]

So the right question is whether the \((0,1)\) row cancels the \(S\)-leak from the \((1,0)\) row. This is exactly the kind of partition-level cancellation the latest local-agent handoff says must be attacked directly, rather than re-deriving the full table. 

The result:

\[
\boxed{
\text{there is a partial Sylvester cancellation, but a residual covariant source derivative remains.}
}
\]

The local closure would require a new identity

\[
\boxed{
X^-_{2,1}
=
P_{-,1}S^-_{2,0}+S^-_{2,0}P_{-,1}
\quad
\text{in the off-diagonal slot.}
}
\]

That identity is not in the draft and is not implied by affine removal, source-grade reflection, or one-amplitude collapse.

---

# 1. Work on a general diagonal good patch

Let

\[
P_{-,0}
=
\begin{pmatrix}
p&0\\
0&q
\end{pmatrix},
\qquad
W_{-,0}
=
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix}.
\]

Let

\[
P_{-,1}
=
\begin{pmatrix}
a&b\\
b&d
\end{pmatrix}.
\]

The source primitive table gives

\[
X^-_{2,0}=xE_{22},
\qquad
X^-_{2,1}=yS,
\]

with \(x\neq0\) and \(y\neq0\) in the actual finite Fréchet normalization.

The zeroth square-root Fréchet coefficient is

\[
S^-_{2,0}
=
\Sigma_-(X^-_{2,0})
=
\frac{x}{2q}E_{22}.
\]

Write

\[
s_0:=\frac{x}{2q}.
\]

---

# 2. Compute \(S^-_{2,1}\)

By the Sylvester recurrence,

\[
S^-_{2,1}
=
\Sigma_-
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right).
\]

Now

\[
P_{-,1}S^-_{2,0}+S^-_{2,0}P_{-,1}
=
\begin{pmatrix}
0&bs_0\\
bs_0&2ds_0
\end{pmatrix}.
\]

Thus the off-diagonal numerator in \(S^-_{2,1}\) is

\[
y-bs_0.
\]

Since the Sylvester denominator for off-diagonal entries is \(p+q\),

\[
(S^-_{2,1})_{12}
=
\frac{y-bs_0}{p+q}.
\]

So the first source derivative survives unless

\[
\boxed{
y=bs_0.
}
\]

This is already the key condition.

---

# 3. Include the inverse-square-root and \(W_{+,1}\) partition

The inverse-square-root coefficient is

\[
\Lambda^-_{2,1}
=
-\left(
W_{-,1}S^-_{2,0}W_{-,0}
+
W_{-,0}S^-_{2,1}W_{-,0}
+
W_{-,0}S^-_{2,0}W_{-,1}
\right).
\]

The \((r,b)=(0,1)\) partition contributes

\[
\Lambda^-_{2,0}E_{22}W_{+,1}.
\]

Endpoint reflection gives

\[
W_{+,1}=-W_{-,1}.
\]

Carrying out the off-diagonal calculation, the \(W_{\pm,1}\)-dependent pieces cancel, and the total \(S\)-coefficient of

\[
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right)
\]

is proportional to

\[
\boxed{
-\frac{p^{-1}q^{-2}}{p+q}(y-bs_0).
}
\]

So the full partition sum kills only the connection terms caused by \(W_1\). It does **not** kill the covariant source derivative

\[
y-bs_0.
\]

---

# 4. Interpretation

The two-partition sum is not arbitrary. It computes a covariant derivative of the source slot relative to the moving square-root frame.

The obstruction is therefore not just

\[
X^-_{2,1}\propto S.
\]

It is the covariant mismatch

\[
\boxed{
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
}
\]

in the off-diagonal direction.

The promoted \(dd\)-row survives exactly when this mismatch is nonzero.

Thus the next possible cancellation theorem must be a **parallel-transport identity** for the actual zeta source primitive:

\[
\boxed{
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)=0.
}
\]

No current draft theorem states this.

---

# 5. Does the draft imply \(y=bs_0\)?

No.

The quantities have different origins:

- \(y\) is the off-diagonal coefficient in the source-linear primitive \(X^-_{2,1}\).
- \(b\) is the off-diagonal coefficient of the baseline square-root coefficient \(P_{-,1}\).
- \(s_0=x/(2q)\) is determined by the diagonal source coefficient \(X^-_{2,0}\) and the baseline square-root eigenvalue \(q\).

Affine removal does not connect \(y\) to \(b\). It removes constant and affine source modes.

Source-grade reflection gives the sign behavior of \(y\), not the identity \(y=bs_0\).

One-amplitude collapse gives the amplitude factor

\[
a_1a_2(a_1+a_2),
\]

not a baseline/source square-root transport equation.

Thus

\[
y-bs_0
\]

is not structurally forced to vanish.

---

# 6. Consequence for the isolated monomial

Recall the isolated source monomial

\[
a_{1,2}a_{2,4}
\]

inside

\[
Y^{dd}_{6,0}
\]

has coefficient

\[
-\frac{K_0}{\pi}E_{22}.
\]

Therefore the full \(r+b=1\) contribution of this monomial is proportional to

\[
-\frac{K_0}{\pi}
a_{1,2}a_{2,4}
\cdot
\left[
-\frac{p^{-1}q^{-2}}{p+q}(y-bs_0)
\right]S.
\]

So unless

\[
K_0=0,
\]

or

\[
a_{1,2}a_{2,4}=0,
\]

or

\[
y=bs_0,
\]

the promoted \(dd\)-row gives

\[
f_{A,Y}\neq0.
\]

On a good phase patch, \(K_0\) is not structurally zero. The source jets \(a_{1,2}\), \(a_{2,4}\) are not killed by affine removal. And the draft does not prove \(y=bs_0\).

Therefore the row remains live.

---

# 7. Sharper missing theorem

The previous missing theorem was:

\[
E_{dd;6,1,0}^{\mathrm{BC}}=0.
\]

After including the \((0,1)\) partition, the sharper theorem is:

```latex id="az6s2j"
\begin{lemma}[First \(dd\)-row covariant source-transport identity]
\label{lem:first-dd-row-covariant-source-transport}
For the actual zeta-side source primitive \(X^-_{2}\), let
\[
S^-_{2,0}=\Sigma_-(X^-_{2,0}).
\]
Then the off-diagonal component satisfies
\[
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)=0.
\]
Equivalently, in a diagonal good patch,
\[
y=bs_0.
\]
\end{lemma}
```

If this lemma holds, the dangerous \(S\)-component from the \(r+b=1\), \(g=6\), \(dd\)-row is killed.

If it fails, the row produces \(T\)-leakage and generically quotient leakage.

---

# 8. Updated verdict

The attack found a real partial cancellation: the \((r,b)=(0,1)\) term cancels the frame-derivative parts of \(\Lambda^-_{2,1}\).

But a residual remains:

\[
\boxed{
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right).
}
\]

This is the new minimal local blocker.

The local proof now depends on a covariant source-transport identity for the actual zeta source primitive. Without it,

\[
E_{A,Y}^{\mathrm{BC}}
\]

still has a live \(dd\)-row \(S\)-leak.
## User (2026-04-25 12:11:16)

continue to attack

## Assistant (2026-04-25 12:11:17)

I’ll now attack the covariant source-transport identity itself. The key is to compute the scalar condition \(y=bs_0\) from the actual \(X^-_{2,0},X^-_{2,1}\) table and the first baseline square-root coefficient \(P_{-,1}\).

_Thought for 33s_

## Continued attack — the covariant identity fails in a valid formal good patch

I attacked the proposed escape identity

\[
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)=0.
\]

This was the only plausible structural cancellation left for the isolated \(dd\)-row. It does **not** follow from the draft’s current source conventions. In fact, it fails in a simple formal good patch compatible with the current finite Fréchet source table.

The active local object is still the frozen Bottleneck-C coefficient \(E_{A,Y}^{\mathrm{BC}}\), with the \(dd\)-row included among the surviving symmetric rows. 

---

# 1. Use the actual source primitive values

From the finite source-linear table:

\[
X^-_{2,0}=\frac{1}{24\pi}(I-D)=\frac{1}{12\pi}E_{22},
\]

so

\[
x=\frac{1}{12\pi}
\]

in

\[
X^-_{2,0}=xE_{22}.
\]

Also

\[
X^-_{2,1}=-\frac{1}{4\pi Q}S,
\]

so

\[
y=-\frac{1}{4\pi Q}
\]

in

\[
X^-_{2,1}=yS.
\]

Let

\[
P_{-,0}=\begin{pmatrix}p&0\\0&q\end{pmatrix},
\qquad p,q\neq0.
\]

Then

\[
S^-_{2,0}
=
\Sigma_-(X^-_{2,0})
=
\frac{x}{2q}E_{22}.
\]

Set

\[
s_0=\frac{x}{2q}=\frac{1}{24\pi q}.
\]

---

# 2. Compute the covariant source derivative

Let

\[
P_{-,1}=
\begin{pmatrix}
a&b\\
b&d
\end{pmatrix}.
\]

Then

\[
P_{-,1}S^-_{2,0}+S^-_{2,0}P_{-,1}
=
\begin{pmatrix}
0&bs_0\\
bs_0&2ds_0
\end{pmatrix}.
\]

Therefore the off-diagonal numerator in the covariant source derivative is

\[
y-bs_0.
\]

The proposed cancellation identity is exactly:

\[
\boxed{
y=bs_0.
}
\]

Substituting \(y,s_0\),

\[
-\frac{1}{4\pi Q}
=
\frac{b}{24\pi q},
\]

or

\[
\boxed{
b=-\frac{6q}{Q}.
}
\]

So the identity requires a very specific relation between the off-diagonal baseline square-root coefficient \(b=(P_{-,1})_{12}\) and the zeroth baseline square-root eigenvalue \(q\).

No current source convention imposes this.

---

# 3. Express \(b\) through the baseline coefficient

Since

\[
P_{-,0}P_{-,1}+P_{-,1}P_{-,0}=G_{-,1}^{(0)},
\]

the off-diagonal entry gives

\[
(p+q)b=(G_{-,1}^{(0)})_{12}.
\]

Thus the required identity becomes

\[
(G_{-,1}^{(0)})_{12}
=
-\frac{6q(p+q)}{Q}.
\]

But \((G_{-,1}^{(0)})_{12}\) is determined by the first baseline Taylor coefficient of the off-diagonal same-point block. In the phase-kernel normalization it is controlled by the baseline \(q_0''(m)\)-type jet. There is no structural reason it must equal

\[
-\frac{6q(p+q)}{Q}.
\]

This is not a parity law, not affine removal, and not one-amplitude collapse. It is a new scalar baseline/source transport equation.

---

# 4. Formal good-patch counterexample

Choose a good baseline patch with

\[
(G_{-,1}^{(0)})_{12}=0.
\]

Equivalently,

\[
b=0.
\]

This can be realized formally by taking the relevant first off-diagonal baseline jet to vanish while keeping

\[
P_{-,0}=\operatorname{diag}(p,q)
\]

nonsingular.

Then

\[
y-bs_0
=
-\frac{1}{4\pi Q}
\neq0.
\]

Thus

\[
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)
\neq0.
\]

So the covariant source-transport identity fails in a valid formal good patch.

This is stronger than the previous diagnostic: it uses the actual source primitive values

\[
X^-_{2,0}=\frac1{12\pi}E_{22},
\qquad
X^-_{2,1}=-\frac1{4\pi Q}S.
\]

---

# 5. Consequence for \(\Lambda^-_{2,1}\)

The Sylvester solution gives

\[
(S^-_{2,1})_{12}
=
\frac{y-bs_0}{p+q}.
\]

With \(b=0\),

\[
(S^-_{2,1})_{12}
=
-\frac{1}{4\pi Q(p+q)}
\neq0.
\]

Then

\[
\Lambda^-_{2,1}
=
-\left(
W_{-,1}S^-_{2,0}W_{-,0}
+
W_{-,0}S^-_{2,1}W_{-,0}
+
W_{-,0}S^-_{2,0}W_{-,1}
\right)
\]

has a nonzero \(S\)-component. If \(W_{-,1}=0\) in the same formal patch, then explicitly

\[
\Lambda^-_{2,1}
=
-W_{-,0}S^-_{2,1}W_{-,0},
\]

so

\[
\lambda_S(\Lambda^-_{2,1})
=
\frac{1}{4\pi Q\,pq(p+q)}
\neq0.
\]

---

# 6. Feed into the isolated \(dd\)-monomial

The previously isolated monomial in

\[
Y^{dd}_{6,0}
\]

was

\[
a_{1,2}a_{2,4}
\]

with coefficient

\[
-\frac{K_0}{\pi}E_{22}.
\]

Choose a phase patch with

\[
K_0\neq0
\]

and source jets with

\[
a_{1,2}a_{2,4}\neq0.
\]

Then

\[
Y^{dd}_{6,0}
\]

has a nonzero \(E_{22}\)-coefficient.

The \(r+b=1\) contribution for this monomial is

\[
-\frac{K_0}{\pi}a_{1,2}a_{2,4}
\,
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
\Lambda^-_{2,1}E_{22}W_{+,0}
+
\Lambda^-_{2,0}E_{22}W_{+,1}
\right).
\]

In the same formal patch, take

\[
W_{+,1}=0,
\qquad
W_{+,0}=\operatorname{diag}(u,v),
\quad v\neq0.
\]

Then the \(S\)-component is nonzero:

\[
\operatorname{Sym}(S E_{22}W_{+,0})=vS.
\]

Hence

\[
f_{A,Y}\neq0.
\]

So

\[
\partial_\kappa T=-a_1^2\frac{f_{A,Y}}{c}\neq0.
\]

And generically,

\[
Q_{A,Y}=e v_5-u_5f\neq0.
\]

---

# 7. Sharper no-go theorem

The current formal source axioms do not imply the promoted \(dd\)-row cancellation. A precise no-go statement is:

```latex
\begin{lemma}[Formal failure of first \(dd\)-row covariant cancellation]
In the formal source category satisfying affine removal, endpoint reflection,
source-grade parity, one-amplitude collapse, and the finite
Fréchet/Sylvester coefficient calculus, the identity
\[
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)=0
\]
is not forced.
Equivalently, in a diagonal good patch the condition
\[
y=bs_0
\]
is an additional scalar constraint, not a consequence of the existing
source conventions.
\end{lemma}
```

---

# 8. Updated local blocker

The local proof now requires one of these new statements:

## Option A — source-transport identity

\[
\operatorname{offdiag}
\left(
X^-_{2,1}
-
P_{-,1}S^-_{2,0}
-
S^-_{2,0}P_{-,1}
\right)=0.
\]

In scalar form:

\[
(G_{-,1}^{(0)})_{12}
=
-\frac{6q(p+q)}{Q}.
\]

## Option B — \(dd\)-source jet cancellation

\[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
=0.
\]

## Option C — aggregate cancellation

The \(dd\)-row survives individually, but is cancelled by other \(dd,d\eta+\eta d,\eta\eta\) rows through a zeta-specific finite jet identity.

No current draft theorem supplies A, B, or C.

---

## Verdict

The obstruction survives another level of attack.

The first local blocker is now a concrete product of two independent scalar failures:

\[
\boxed{
(y-bs_0)
\cdot
\left[
K_0(a_{1,2}a_{2,4}+a_{1,4}a_{2,2}-a_{1,3}a_{2,3})
+
K_2a_{1,2}a_{2,2}
\right].
}
\]

The present source conventions do not force either factor to vanish. Thus the promoted mixed-block Bottleneck-C scalar closure remains unproved, and formal source models satisfying the current rules can make \(E_{A,Y}^{\mathrm{BC}}\) leak through both quotient and \(T\).
## User (2026-04-25 12:30:20)

You are now "Local Agent 1". continue on your attack as per the attached instructions

## Assistant (2026-04-25 12:31:00)

_Thought for 34s_

## Local Agent 1 result — endpoint-diagonal realization is **not proved**

I attacked the endpoint-diagonal route:

\[
[\delta^0]\eta_i^\Delta=0,
\qquad
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2.
\]

This route would close the local obstruction if the paper proved that the endpoint displacement sources are evaluations of a single co-moving analytic source field,

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

Then

\[
\eta_i^\Delta
=
\frac{\eta_i(h+\delta/2)-\eta_i(h-\delta/2)}2
=
\frac{\delta}{2}\eta_i'(h)+O(\delta^3),
\]

so

\[
[\delta^0]\eta_i^\Delta=0.
\]

This would remove the parity-bad frozen subchannels

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta,
\]

leaving only even-background channels. Since every active row has

\[
r+b+g=7,
\]

the surviving rows would be reflection-odd and killed by fixed-sector symmetrization. That would prove

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

But the current draft state, as summarized in the attached instructions, explicitly says this endpoint-diagonal realization is **not yet proved**. The active Bottleneck-C coefficient is the frozen coefficient \(E_{A,Y}^{\mathrm{BC}}\), and the possible parity closure depends precisely on proving that endpoint displacement sources are co-moving/endpoint-diagonal. turn68file3

---

# 1. What the paper appears to define

The corrected mixed block is organized around variables of the form

\[
N^{\corr}(q_-,q_+,\Delta;s),
\]

with endpoint data

\[
q_-,\qquad q_+,
\]

and a mixed phase-gap/source-motion datum

\[
\Delta.
\]

The local actual-source variables are then schematically

\[
d_{i,-},\quad d_{i,+},\quad \eta_i,
\]

where \(d_{i,\pm}\) are endpoint \(q\)-source variations and \(\eta_i\) is the phase-gap variation entering \(\Delta\). The current local branch splits the \(\eta\)-endpoint data into

\[
\eta^\Sigma=\frac{\eta_++\eta_-}{2},
\qquad
\eta^\Delta=\frac{\eta_+-\eta_-}{2}.
\]

The problem is that the draft has not yet identified \(\eta_+\) and \(\eta_-\) as two evaluations of the **same** analytic field at the two moving endpoints. It only has the mixed-block variables and the source table/Fréchet machinery. The attached instructions explicitly warn that if \(\eta_+\) and \(\eta_-\) are independent frozen endpoint variables, then \([\delta^0]\eta^\Delta\) can survive and \(E_{A,Y}^{\mathrm{BC}}\) can remain quotient-visible and \(T\)-visible. turn68file2

So the endpoint-diagonal theorem is currently a missing source-realization theorem, not a consequence of the existing definitions.

---

# 2. Concrete parity-bad survivor if endpoint-diagonal realization is absent

Assume the frozen endpoint-separation component survives:

\[
\zeta_i:=[\delta^0]\eta_i^\Delta\neq0.
\]

Then the \(d\eta+\eta d\) Hessian channel contains frozen parity-bad terms of the schematic form

\[
d_i\,\zeta_j+\zeta_i\,d_j.
\]

More concretely, from the mixed-block Hessian formulas previously isolated, the \(d\eta\)-sector contains terms such as

\[
-\frac{\sin\Delta_0}{\pi s}(d_{1,+}\eta_2+d_{2,+}\eta_1)
\]

in the \((1,2)\)-entry and

\[
\frac{\sin\Delta_0}{\pi s}(d_{1,-}\eta_2+d_{2,-}\eta_1)
\]

in the \((2,1)\)-entry, with additional \((2,2)\)-entry terms involving

\[
\left(\frac{\sin\Delta_0}{s^2}
+
\frac{q_\pm^0\cos\Delta_0}{s}
\right)(d\,\eta).
\]

Splitting

\[
\eta=\eta^\Sigma+\eta^\Delta
\]

produces the parity-bad pieces

\[
d\eta^\Delta+\eta^\Delta d.
\]

If

\[
[\delta^0]\eta^\Delta\neq0,
\]

these pieces survive in the frozen Bottleneck-C coefficient.

---

# 3. They can carry \(S\)-projection

This survivor is not automatically killed by fixed-sector projection.

Take a good formal patch where the same-point Fréchet slot has an \(S\)-component. This is compatible with the actual finite Fréchet primitive table: the draft uses source indices \(a=2,\dots,6\), and the first off-diagonal primitive appears in the \(a=2\), \(n=1\) row, not in the older shorthand \(a\in\{1,5\}\). The attached prompt warns agents to align to this actual finite Fréchet convention. 

Let the same-point whitening response contain

\[
\Lambda^-_{2,1}\sim S.
\]

Let a frozen \(d\eta^\Delta\)-piece contribute a diagonal matrix such as \(E_{22}\), or an off-diagonal matrix that has nonzero fixed-sector projection after multiplication. Then

\[
\operatorname{Sym}(S E_{22})=S.
\]

Thus the frozen parity-bad survivor can produce

\[
E_{A,Y}^{\mathrm{BC}}\supset \mu S,
\qquad
\mu\neq0.
\]

Then

\[
f_{A,Y}=\mu\neq0,
\]

and the augmented \(T\)-horizontal condition fails because

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
\neq0.
\]

The quotient determinant is

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}.
\]

For a pure \(S\)-survivor,

\[
e_{A,Y}=0,
\qquad
Q_{A,Y}=-u_5f_{A,Y},
\]

so quotient Bottleneck-C also fails on a generic \(u_5\neq0\) patch.

---

# 4. Endpoint-diagonal realization would close the local branch

If the paper adds or proves the source-realization theorem

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2),
\]

then

\[
[\delta^0]\eta_i^\Delta=0.
\]

Consequently,

\[
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}=0,
\]

and

\[
Y^{\eta^\Sigma\eta^\Delta}_{g,0}=0.
\]

The only frozen Hessian channels left are even-background channels. Then, under the reflection convention,

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]

The whitening/source row contributes \((-1)^r\), the right baseline contributes \((-1)^b\), and every active row satisfies

\[
r+g+b=7.
\]

Therefore the full row is reflection-odd:

\[
(-1)^{r+g+b}=-1.
\]

After endpoint pairing and fixed-sector symmetrization, the row is skew in the fixed-sector sense and vanishes. Hence

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

This is the cleanest local closure route.

---

# 5. But the theorem is absent

The current paper state does not yet prove the required endpoint-diagonal realization. The attached instructions explicitly state the gap:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2)
\]

is not established, and independent frozen endpoint variables would allow \([\delta^0]\eta^\Delta\) to survive. turn68file1

Thus Local Agent 1 cannot close \(E_{A,Y}^{\mathrm{BC}}\) from the current draft. The exact parity-bad survivor is:

\[
\boxed{
[\delta^0]\eta_i^\Delta\neq0
}
\]

feeding the frozen Hessian channels

\[
\boxed{
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
}
\]

These can carry an \(S\)-projection after multiplication by the same-point whitening slot and hence can leak through \(T\).

---

# 6. Missing theorem

The missing theorem should be stated directly.

```latex
\begin{theorem}[Endpoint-diagonal realization of source-motion variables]
\label{thm:endpoint-diagonal-source-motion}
For every active source direction \(\xi_i\) entering the promoted mixed-block
Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
there exists a single analytic source-motion field \(\eta_i(t)\), co-moving
with the midpoint \(h\), such that
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Consequently
\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=O(\delta),
\]
and hence
\[
[\delta^0]\eta_i^\Delta=0.
\]
\end{theorem}
```

Then add the immediate corollary:

```latex
\begin{corollary}[Promoted mixed-block Bottleneck-C closure]
Under Theorem~\ref{thm:endpoint-diagonal-source-motion},
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
\end{corollary}
```

Proof sketch:

1. \([\delta^0]\eta^\Delta=0\) kills \(d\eta^\Delta+\eta^\Delta d\) and \(\eta^\Sigma\eta^\Delta\).
2. Remaining frozen Hessian channels have even background.
3. Each active row has \(r+b+g=7\).
4. Hence each row is reflection-odd and fixed-sector symmetrization kills it.

---

## Verdict

Endpoint-diagonal realization would close the local obstruction, but it is not currently proved.

The concrete survivor if it fails is:

\[
\boxed{
[\delta^0]\eta^\Delta
}
\]

inside

\[
\boxed{
d\eta^\Delta+\eta^\Delta d
\quad\text{and}\quad
\eta^\Sigma\eta^\Delta.
}
\]

This survivor can produce \(S\)-projection, hence

\[
f_{A,Y}\neq0,
\qquad
\partial_\kappa T\neq0,
\]

and generically

\[
Q_{A,Y}\neq0.
\]

So the local proof now hinges on the endpoint-diagonal source-motion theorem.
## User (2026-04-25 12:36:19)

You are also called "Local A". do the attack per these instructions

## Assistant (2026-04-25 12:37:19)

_Thought for 57s_

## Local A attack — odd \(\eta\eta\) block does **not** cancel structurally

I attacked the new local target:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
W_{+,b}
\right)=0.
\]

The result is negative. The odd-background frozen \(\eta\eta\) block contains a genuine off-diagonal skew matrix \(J\), and after multiplication by the same-point whitening response and right whitening it generically produces an \(S\)-component. Thus the block can be both \(T\)-visible and quotient-visible.

This matches the attached instruction’s update: endpoint-diagonal realization alone is not enough anymore, because an odd-background frozen \(\eta\eta\) Hessian survivor occurs directly inside \(N^{\corr}(q_-,q_+,\Delta;s)\). L1-L17

---

# 1. Compute the full off-diagonal \(\eta\eta\) Hessian block

Start from

\[
N_{12}
=
\frac{\sin\Delta+q_+s\cos\Delta}{s^2},
\]

\[
N_{21}
=
-\frac{\sin\Delta+q_-s\cos\Delta}{s^2}.
\]

Twice differentiating in \(\Delta\) gives

\[
\partial_\Delta^2 N_{12}\big|_0
=
-\frac{\sin\Delta_0}{s^2}
-
\frac{q_+\cos\Delta_0}{s},
\]

and

\[
\partial_\Delta^2 N_{21}\big|_0
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}.
\]

Define endpoint-even and endpoint-odd pieces

\[
q_e:=\frac{q_++q_-}{2},
\qquad
q_o:=\frac{q_+-q_-}{2}.
\]

Then the off-diagonal \(\eta\eta\) Hessian block decomposes as

\[
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{off}}
=
A_o J
-
A_e S,
\]

where

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

and

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s},
\]

\[
A_e
=
\frac{q_o\cos\Delta_0}{s}.
\]

The important part is:

\[
\boxed{
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
=
A_oJ.
}
\]

Here \(A_o\) is odd-background: \(\sin\Delta_0/s^2\) is odd, and \(q_e\cos\Delta_0/s\) is also odd.

The companion term does **not** cancel \(-\sin\Delta_0/s^2\). It combines with it into

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

On a good phase patch, this is generically nonzero. If \(\Delta_0\sim q_0s+O(s^3)\) and \(q_e\sim q_0+O(s^2)\), then

\[
A_o
\sim
\frac{2q_0}{s}+O(s),
\]

so the two terms add at leading order rather than cancel.

---

# 2. Apply endpoint transpose and symmetrization

Let

\[
L:=\Lambda^-_{a,r},
\qquad
W:=W_{+,b}.
\]

Both \(L\) and \(W\) are symmetric matrices in the good finite Fréchet setup. The odd \(\eta\eta\) block contributes

\[
\operatorname{Sym}(L\,A_oJ\,W)
=
A_o\operatorname{Sym}(LJW).
\]

Since

\[
J^T=-J,
\]

and \(L,W\) are symmetric,

\[
\operatorname{Sym}(LJW)
=
LJW-WJL.
\]

Thus the odd-background block survives precisely through the commutator-like expression

\[
\boxed{
LJW-WJL.
}
\]

There is no automatic cancellation.

---

# 3. Fixed-sector projection of the odd block

Write

\[
L=
\begin{pmatrix}
a&c\\
c&d
\end{pmatrix},
\qquad
W=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix}.
\]

A direct calculation gives

\[
LJW-WJL
=
\begin{pmatrix}
2(cu-aw)&ud-av\\
ud-av&2(dw-cv)
\end{pmatrix}.
\]

Therefore the fixed-sector coordinates are:

\[
I\text{-coefficient}
=
c(u-v)+w(d-a),
\]

\[
S\text{-coefficient}
=
ud-av.
\]

So after applying \(\pi_{\mathfrak f_h}\),

\[
\pi_{\mathfrak f_h}\operatorname{Sym}(L A_oJ W)
=
A_o
\left(
[c(u-v)+w(d-a)]I
+
[ud-av]S
\right).
\]

The \(S\)-coefficient is

\[
\boxed{
A_o(ud-av).
}
\]

This is generically nonzero.

---

# 4. Concrete \(S\)-visible survivor

Take a diagonal good patch:

\[
L=
\begin{pmatrix}
a&0\\
0&d
\end{pmatrix},
\qquad
W=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}.
\]

Then

\[
\pi_{\mathfrak f_h}\operatorname{Sym}(L A_oJ W)
=
A_o(ud-av)S.
\]

Unless

\[
\frac a d=\frac u v,
\]

this has a nonzero \(S\)-component.

Nothing in the current source conventions forces this ratio identity. \(L\) is a same-point source Fréchet response; \(W\) is a baseline right-whitening coefficient. They are generated by different coefficient recurrences. Endpoint transpose relates left and right placements; it does not force \(L\) and \(W\) to be proportional.

Thus the odd \(\eta\eta\) block can give

\[
f_{A,Y}\neq0.
\]

Then

\[
\partial_\kappa T=-a_1^2\frac{f_{A,Y}}{c}\neq0.
\]

So the augmented transform-safe condition fails.

---

# 5. Quotient determinant

For the same diagonal survivor, the fixed-sector output is pure \(S\):

\[
E=\mu S.
\]

Hence

\[
e=0,
\qquad
f=\mu.
\]

The quotient determinant is

\[
Q_{A,Y}=ev_5-u_5f=-u_5\mu.
\]

On a generic \(u_5\neq0\) patch,

\[
Q_{A,Y}\neq0.
\]

So the odd \(\eta\eta\) survivor is not merely \(T\)-visible; it is generically quotient-visible as well.

---

# 6. Why the \(q_\pm\cos\Delta_0/s\) companion does not save it

The only plausible cancellation inside the off-diagonal Hessian would be

\[
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
=0.
\]

Equivalently,

\[
\sin\Delta_0+s q_e\cos\Delta_0=0.
\]

But \(q_e\) is the endpoint-even baseline slope, while \(\Delta_0\) is the phase gap. In the standard phase-gap relation, for small separation,

\[
\Delta_0=q_0s+O(s^3),
\qquad
q_e=q_0+O(s^2).
\]

Then

\[
\sin\Delta_0+s q_e\cos\Delta_0
=
2q_0s+O(s^3).
\]

This is not zero on a good patch with \(q_0\neq0\).

Thus the \(q_\pm\cos\Delta_0/s\) companion reinforces the odd-background term at leading order.

---

# 7. Relation to endpoint-diagonal realization

This obstruction is independent of

\[
[\delta^0]\eta^\Delta=0.
\]

Even if endpoint-diagonal realization later proves

\[
\eta^\Delta=O(\delta),
\]

the block above uses the ordinary \(\eta\eta\) Hessian in \(\Delta\) itself. It is present inside

\[
\partial_\Delta^2N_0
\]

before any endpoint-separation splitting. That is exactly why the new local verdict says endpoint-diagonal realization is no longer sufficient by itself. L1-L17

---

# 8. Minimal missing theorem

The necessary local theorem is now:

```latex
\begin{lemma}[Odd \(\eta\eta\) off-diagonal fixed-sector cancellation]
For every active row \(r+b+g=7\),
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J
\right]_{g}
W_{+,b}
\right)=0.
\]
\end{lemma}
```

Equivalently, rowwise, this requires

\[
A_o(ud-av)=0
\]

for the \(S\)-coordinate and

\[
A_o[c(u-v)+w(d-a)]=0
\]

for the \(I\)-coordinate. The current draft proves neither.

---

## Verdict

The off-diagonal odd-background \(\eta\eta\) block is a concrete survivor:

\[
\boxed{
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)
J.
}
\]

After same-point whitening and right whitening, it contributes

\[
\boxed{
\pi_{\mathfrak f_h}\operatorname{Sym}(LJW)
=
[c(u-v)+w(d-a)]I+(ud-av)S.
}
\]

The \(S\)-coefficient is generically nonzero. Therefore the local closure

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

is not structurally proved. The proof now needs a specific odd-\(\eta\eta\) fixed-sector cancellation theorem or a correction term cancelling this block.
## User (2026-04-25 12:40:14)

Do your instruction as per attached

## Assistant (2026-04-25 12:40:41)

_Thought for 25s_

## Local A result — odd \(\eta\eta\) block has a concrete surviving row

I attacked the updated local target:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
[A_oJ]_g
W_{+,b}
\right)=0,
\]

where

\[
A_oJ
=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J,
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

The target fails structurally. There is a concrete active row

\[
\boxed{
(a,r,g,b)=(2,0,7,0)
}
\]

that can produce a nonzero \(S\)-component. Therefore the odd \(\eta\eta\) block is not killed by endpoint transpose, symmetrization, the Sylvester recurrence, or fixed-sector projection.

This is exactly the new local blocker identified in the attached instructions: endpoint-diagonal realization does not address the scalar \(\Delta\)-Hessian \(\eta\eta\) odd-background survivor. 

---

# 1. Odd off-diagonal \(\eta\eta\) block

Start from

\[
N_{12}
=
\frac{\sin\Delta+q_+s\cos\Delta}{s^2},
\]

\[
N_{21}
=
-\frac{\sin\Delta+q_-s\cos\Delta}{s^2}.
\]

Twice differentiating in \(\Delta\) gives

\[
\partial_\Delta^2N_{12}\big|_0
=
-\frac{\sin\Delta_0}{s^2}
-
\frac{q_+\cos\Delta_0}{s},
\]

\[
\partial_\Delta^2N_{21}\big|_0
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}.
\]

Write

\[
q_e=\frac{q_++q_-}{2},
\qquad
q_o=\frac{q_+-q_-}{2}.
\]

Then the off-diagonal block decomposes as

\[
\partial_\Delta^2N_{\mathrm{off}}\big|_0
=
A_oJ-A_eS,
\]

with

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s},
\]

\[
A_e
=
\frac{q_o\cos\Delta_0}{s}.
\]

The odd-background survivor is

\[
\boxed{
A_oJ.
}
\]

The two terms inside \(A_o\) do not cancel. In the usual small-separation expansion,

\[
\Delta_0=q_0s+O(s^3),
\qquad
q_e=q_0+O(s^2),
\]

so

\[
A_o
=
\frac{2q_0}{s}+O(s).
\]

Thus \(A_o\) is generically nonzero on a good phase patch.

---

# 2. Include the \(\eta_i\eta_j\) source product

The odd \(\eta\eta\) row is really

\[
A_oJ\,\eta_i\eta_j.
\]

Write

\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,4}z^4+\alpha_{i,5}z^5+\cdots,
\]

and

\[
A_o(z)=A_{-1}z^{-1}+A_1z+A_3z^3+\cdots,
\]

with \(A_{-1}\neq0\) generically.

Then the \(g=7\) coefficient is

\[
[A_o\eta_i\eta_j]_{7}
=
A_{-1}
(\alpha_{i,3}\alpha_{j,5}+\alpha_{i,5}\alpha_{j,3}+\alpha_{i,4}\alpha_{j,4})
+
A_1\alpha_{i,3}\alpha_{j,3}.
\]

No current source convention forces this scalar to vanish. Affine removal does not remove \(\eta\)-source data of this order. Endpoint-diagonal realization, even if proved, does not touch this scalar \(\Delta\)-Hessian term.

Denote the scalar coefficient by

\[
\nu_{\eta\eta,7}:=[z^7](A_o\eta_i\eta_j).
\]

Generically,

\[
\boxed{
\nu_{\eta\eta,7}\neq0.
}
\]

Thus

\[
[A_oJ]_7=\nu_{\eta\eta,7}J.
\]

---

# 3. Use actual finite Fréchet source index \(a=2\)

The actual finite Fréchet primitive table uses indices \(a=2,\ldots,6\). For \(a=2\), the zeroth same-point primitive is diagonal:

\[
X^-_{2,0}
=
\frac{1}{24\pi}(I-D)
=
\frac{1}{12\pi}E_{22}.
\]

Let

\[
P_{-,0}=
\begin{pmatrix}
p&0\\
0&q
\end{pmatrix},
\qquad
p,q\neq0.
\]

The Sylvester solution for the square-root Fréchet coefficient is

\[
S^-_{2,0}
=
\Sigma_-(X^-_{2,0})
=
\frac{1}{24\pi q}E_{22}.
\]

Then

\[
\Lambda^-_{2,0}
=
-W_{-,0}S^-_{2,0}W_{-,0}.
\]

Since

\[
W_{-,0}=
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix},
\]

we get

\[
\boxed{
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
}
\]

This is not arbitrary. It follows from the actual source primitive \(X^-_{2,0}\) and the Sylvester/Frechet recurrence.

---

# 4. Evaluate the active row \((a,r,g,b)=(2,0,7,0)\)

For the row

\[
(a,r,g,b)=(2,0,7,0),
\]

the contribution is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ]_7
W_{+,0}
\right).
\]

Take a diagonal right good patch

\[
W_{+,0}
=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix},
\qquad
u,v\neq0.
\]

Substitute

\[
\Lambda^-_{2,0}
=
\ell E_{22},
\qquad
\ell=-\frac{1}{24\pi q^3},
\]

and

\[
[A_oJ]_7=\nu_{\eta\eta,7}J.
\]

Then

\[
\Lambda^-_{2,0}[A_oJ]_7W_{+,0}
=
\ell\nu_{\eta\eta,7}E_{22}JW_{+,0}.
\]

Now

\[
E_{22}J=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\]

so

\[
E_{22}JW_{+,0}
=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix}.
\]

Symmetrizing gives

\[
\operatorname{Sym}(E_{22}JW_{+,0})
=
\begin{pmatrix}
0&u\\
u&0
\end{pmatrix}
=
uS.
\]

Therefore

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\ell\nu_{\eta\eta,7}u\,S
}
\]

after fixed-sector projection.

Since

\[
\ell\neq0,\qquad
u\neq0,
\]

and \(\nu_{\eta\eta,7}\) is not structurally zero,

\[
\boxed{
f_{A,Y}\neq0
}
\]

in the formal good-patch model.

---

# 5. Consequences for \(T\) and quotient closure

For this row,

\[
E=\ell\nu_{\eta\eta,7}u\,S.
\]

Thus

\[
e=0,
\qquad
f=\ell\nu_{\eta\eta,7}u.
\]

The \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
=
-a_1^2\frac{\ell\nu_{\eta\eta,7}u}{c}.
\]

Generically this is nonzero.

The quotient determinant is

\[
Q_{A,Y}=ev_5-u_5f=-u_5f.
\]

On a generic \(u_5\neq0\) patch,

\[
Q_{A,Y}\neq0.
\]

Therefore this single odd \(\eta\eta\) row can break both Bottleneck-C quotient closure and \(T\)-horizontal closure.

---

# 6. Does the \(q_\pm\cos\Delta_0/s\) companion cancel it?

No.

The odd block coefficient is

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

For cancellation one would need

\[
\sin\Delta_0+s q_e\cos\Delta_0=0.
\]

But with

\[
\Delta_0=q_0s+O(s^3),
\qquad
q_e=q_0+O(s^2),
\]

one has

\[
\sin\Delta_0+s q_e\cos\Delta_0
=
2q_0s+O(s^3).
\]

So the companion reinforces the leading term rather than cancelling it.

---

# 7. Does the Sylvester recurrence force \(ud-av=0\)?

For this concrete row,

\[
L=\Lambda^-_{2,0}=\ell E_{22},
\qquad
W=W_{+,0}.
\]

In the diagonal patch,

\[
L=
\begin{pmatrix}
0&0\\
0&\ell
\end{pmatrix},
\qquad
W=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}.
\]

The general \(S\)-coefficient of

\[
\operatorname{Sym}(LJW)
\]

is

\[
ud-av.
\]

Here

\[
a=0,\qquad d=\ell,
\]

so

\[
ud-av=u\ell.
\]

This is nonzero on a good patch. Hence the ratio condition is not forced; it fails generically.

---

# 8. Minimal missing theorem

The needed theorem is now even narrower than full \(E_{A,Y}^{\mathrm{BC}}\)-closure.

```latex id="t83rm6"
\begin{lemma}[Odd \(\eta\eta\) row cancellation]
For the actual zeta-side source jets and finite Fréchet normalization,
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J
\eta_i\eta_j
\right]_{7}
W_{+,0}
\right)=0.
\]
\end{lemma}
```

Equivalently, this requires one of:

\[
\nu_{\eta\eta,7}=0,
\]

\[
\Lambda^-_{2,0}=0,
\]

or a fixed-sector cancellation against other active rows.

The current draft proves none of these.

---

## Verdict

The odd-background \(\eta\eta\) block gives a concrete row-level obstruction:

\[
\boxed{
(a,r,g,b)=(2,0,7,0),
\qquad
\chi=\eta\eta_{\mathrm{odd}}.
}
\]

It contributes

\[
\boxed{
\ell\nu_{\eta\eta,7}u\,S
}
\]

on a diagonal good patch, generically nonzero.

Therefore

\[
\boxed{
f_{A,Y}\neq0,
}
\]

so

\[
\boxed{
\partial_\kappa T\neq0.
}
\]

And generically

\[
\boxed{
Q_{A,Y}\neq0.
}
\]

Thus the local closure is not structurally proved; it now hinges on a specific odd-\(\eta\eta\) row cancellation theorem or a correction term that removes this block.
## User (2026-04-25 12:47:31)

continue as per your exact prompt instruction

## Assistant (2026-04-25 12:48:21)

_Thought for 44s_

## Local Agent 1 — continued attack on the concrete odd-\(\eta\eta\) top row

I attacked the specific row

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
A_oJ\,\eta_i\eta_j
\right]_7
W_{+,0}
\right),
\]

where

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s},
\qquad
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

This is the lead local obstruction specified in the current prompt. The prompt also emphasizes that this is the frozen Bottleneck-C coefficient, not the internal \([z^7\delta^1]\) source-position coefficient. 

The row does **not** vanish structurally. It produces a concrete \(S\)-component on a good patch.

---

# 1. Compute \(A_o\) more explicitly

Let

\[
s=\frac{z}{Q^2}.
\]

Write the baseline phase gap and endpoint-even slope as

\[
\Delta_0
=
q_0s+\frac{q_0''}{24}s^3+O(s^5),
\]

\[
q_e
=
\frac{q_++q_-}{2}
=
q_0+\frac{q_0''}{8}s^2+O(s^4).
\]

Then

\[
\sin\Delta_0
=
q_0s+
\left(
\frac{q_0''}{24}
-
\frac{q_0^3}{6}
\right)s^3
+
O(s^5),
\]

and

\[
q_e\cos\Delta_0
=
q_0+
\left(
\frac{q_0''}{8}
-
\frac{q_0^3}{2}
\right)s^2
+
O(s^4).
\]

Therefore

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\]

has expansion

\[
\boxed{
A_o
=
\frac{2q_0}{s}
+
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)s
+
O(s^3).
}
\]

So the companion term

\[
\frac{q_e\cos\Delta_0}{s}
\]

does **not** cancel

\[
\frac{\sin\Delta_0}{s^2}.
\]

It doubles the leading \(q_0/s\) term.

Thus, on any good patch with

\[
q_0\neq0,
\]

\[
A_o
\]

is nonzero.

This agrees with the attached summary: the \(q_e\cos\Delta_0/s\) term reinforces rather than cancels the odd-background term. 

---

# 2. Compute \(\nu_{\eta\eta,7}\)

Let

\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,4}z^4+\alpha_{i,5}z^5+O(z^6),
\]

\[
\eta_j(z)
=
\alpha_{j,3}z^3+\alpha_{j,4}z^4+\alpha_{j,5}z^5+O(z^6).
\]

In \(z\)-coordinates,

\[
A_o(z)
=
A_{-1}z^{-1}+A_1z+O(z^3),
\]

with

\[
A_{-1}=2q_0Q^2,
\]

\[
A_1=
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right).
\]

Then

\[
\nu_{\eta\eta,7}
=
[z^7]\bigl(A_o\eta_i\eta_j\bigr)
\]

is

\[
\boxed{
\nu_{\eta\eta,7}
=
A_{-1}
\bigl(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\bigr)
+
A_1\alpha_{i,3}\alpha_{j,3}.
}
\]

Substituting \(A_{-1},A_1\),

\[
\boxed{
\begin{aligned}
\nu_{\eta\eta,7}
={}&
2q_0Q^2
\bigl(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\bigr)
\\
&+
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}.
\end{aligned}
}
\]

There is no generic parity reason for this to vanish. It is an even product of two \(\eta\)-source fields multiplied by an odd-background coefficient whose denominator shifts the order.

So

\[
\boxed{
\nu_{\eta\eta,7}=0
}
\]

would require a genuine source-jet identity:

\[
2q_0Q^2
\bigl(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\bigr)
+
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}
=0.
\]

The current local source conventions do not imply this identity.

---

# 3. Use the exact finite Fréchet row \(\Lambda^-_{2,0}\)

For source index \(a=2\),

\[
X^-_{2,0}
=
\frac{1}{24\pi}(I-D)
=
\frac{1}{12\pi}E_{22}.
\]

Let

\[
P_{-,0}
=
\begin{pmatrix}
p&0\\
0&q
\end{pmatrix}.
\]

Then the Sylvester solution gives

\[
S^-_{2,0}
=
\Sigma_-(X^-_{2,0})
=
\frac{1}{24\pi q}E_{22}.
\]

Since

\[
W_{-,0}
=
\begin{pmatrix}
p^{-1}&0\\
0&q^{-1}
\end{pmatrix},
\]

the inverse-square-root Fréchet coefficient is

\[
\Lambda^-_{2,0}
=
-W_{-,0}S^-_{2,0}W_{-,0}.
\]

Hence

\[
\boxed{
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
}
\]

This is the exact row data already identified in the prompt; it is not an arbitrary matrix. 

So set

\[
\ell:=-\frac{1}{24\pi q^3}.
\]

Then

\[
\Lambda^-_{2,0}=\ell E_{22}.
\]

---

# 4. Use exact diagonal right whitening

Let the right zeroth whitening be

\[
W_{+,0}
=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}.
\]

The row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
\ell E_{22}
\cdot
\nu_{\eta\eta,7}J
\cdot
W_{+,0}
\right).
\]

Now

\[
E_{22}J
=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\]

so

\[
E_{22}JW_{+,0}
=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix}.
\]

Therefore

\[
\operatorname{Sym}(E_{22}JW_{+,0})
=
\begin{pmatrix}
0&u\\
u&0
\end{pmatrix}
=
uS.
\]

Thus

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\ell\,\nu_{\eta\eta,7}\,u\,S.
}
\]

So the fixed-sector coefficient is

\[
\boxed{
e=0,
\qquad
f=\ell\,\nu_{\eta\eta,7}\,u.
}
\]

As long as

\[
q\neq0,\qquad u\neq0,\qquad \nu_{\eta\eta,7}\neq0,
\]

we get

\[
\boxed{
f\neq0.
}
\]

Since \(q,u\) are nonzero on a good whitening patch, the only possible scalar escape is

\[
\nu_{\eta\eta,7}=0.
\]

---

# 5. \(T\)-visibility and quotient visibility

The induced \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}.
\]

Substituting \(f\),

\[
\boxed{
\partial_\kappa T
=
-a_1^2\frac{\ell\,\nu_{\eta\eta,7}\,u}{c}.
}
\]

Generically this is nonzero.

The quotient determinant is

\[
Q=e v_5-u_5f.
\]

Since \(e=0\),

\[
\boxed{
Q
=
-u_5\ell\nu_{\eta\eta,7}u.
}
\]

Therefore the row is quotient-visible on any generic patch with

\[
u_5\neq0.
\]

So this row is not merely \(T\)-visible. It generically breaks both quotient Bottleneck-C and \(T\)-horizontal closure.

---

# 6. Could another top-row \(\eta\eta\) term cancel it?

Not structurally.

The odd off-diagonal block is specifically

\[
A_oJ.
\]

The endpoint-even companion block is the \(S\)-type piece coming from

\[
A_eS,
\qquad
A_e=\frac{q_o\cos\Delta_0}{s}.
\]

But this has different endpoint-background parity and different matrix type. It cannot cancel the \(J\)-block rowwise unless the source jets and baseline whitening satisfy an additional algebraic identity.

Within the same \((a,r,g,b)=(2,0,7,0)\) row, the \(J\)-block gives a pure \(S\)-fixed-sector output in the diagonal patch. A cancellation would require another \(\eta\eta\) contribution producing exactly

\[
-\ell\nu_{\eta\eta,7}uS.
\]

No current symmetry forces such a paired term.

The current instructions explicitly identify this concrete row as the lead local obstruction and ask for either a proof that it vanishes or a surviving \(eI+fS\) coefficient. 

We have the latter.

---

# 7. Conclusion

The row survives with concrete coefficient

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
=
0\cdot I
+
\ell\,\nu_{\eta\eta,7}\,u\,S,
}
\]

where

\[
\ell=-\frac{1}{24\pi q^3},
\]

and

\[
\boxed{
\begin{aligned}
\nu_{\eta\eta,7}
={}&
2q_0Q^2
\bigl(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\bigr)
\\
&+
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}.
\end{aligned}
}
\]

Thus

\[
\boxed{
f_{A,Y}=\ell\nu_{\eta\eta,7}u.
}
\]

And

\[
\boxed{
Q_{A,Y}=-u_5\ell\nu_{\eta\eta,7}u.
}
\]

So the row is:

\[
\boxed{
\text{\(T\)-visible if }\nu_{\eta\eta,7}\neq0,
}
\]

and

\[
\boxed{
\text{quotient-visible if additionally }u_5\neq0.
}
\]

The only remaining way for this row to vanish is the source-jet identity

\[
\boxed{
\nu_{\eta\eta,7}=0.
}
\]

Expanded:

\[
\boxed{
2q_0Q^2
\bigl(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\bigr)
+
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}
=0.
}
\]

The draft does not currently prove this. Therefore the concrete odd-\(\eta\eta\) top row remains a live local obstruction.
## User (2026-04-25 12:49:01)

continue your attack

## Assistant (2026-04-25 12:49:03)

I’ll continue from the concrete odd-\(\eta\eta\) row and attack the only remaining escape: whether the source definition of \(\eta_i\) forces the scalar coefficient \(\nu_{\eta\eta,7}\) to vanish.

I’ll now test the strongest possible rescue for the odd-\(\eta\eta\) row: assume \(\eta_i\) is not an independent source but the actual phase-gap integral of the same post-affine \(q\)-source. If even that does not force \(\nu_{\eta\eta,7}=0\), the obstruction is harder.

_Thought for 24s_

## Continued Local Agent 1 attack — even phase-gap integral realization does not kill the odd \(\eta\eta\) row

I attacked the strongest plausible rescue:

\[
\eta_i \text{ is not an independent endpoint variable, but the phase-gap integral of the same source field.}
\]

This is stronger than endpoint-diagonal realization. It assumes the most favorable source model:

\[
\eta_i(s)=\int_{-s/2}^{s/2} r_i(u)\,du,
\]

where \(r_i\) is the post-affine \(q\)-source perturbation, and \(s\) is the endpoint separation.

Even under this favorable assumption, the top-row scalar

\[
\nu_{\eta\eta,7}=[z^7](A_o\eta_i\eta_j)
\]

is **not structurally zero**.

The current prompt identifies this row as the lead local obstruction:

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\,\eta_i\eta_j]_7
W_{+,0}
\right),
\]

with

\[
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

It also records that this is the frozen Bottleneck-C coefficient, because the amplitude \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge. 

---

# 1. Favorable source-integral model

Assume the post-affine source field has Taylor expansion

\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,3}u^3+\rho_{i,4}u^4+O(u^5).
\]

Affine removal has already killed the \(u^0\) and \(u^1\) terms.

Assume the phase-gap source is the actual symmetric endpoint integral:

\[
\eta_i(s)
=
\int_{-s/2}^{s/2}r_i(u)\,du.
\]

Then odd powers integrate to zero, so

\[
\eta_i(s)
=
\frac{\rho_{i,2}}{12}s^3
+
\frac{\rho_{i,4}}{80}s^5
+
O(s^7).
\]

In \(z\)-coordinates, with

\[
s=\frac{z}{Q^2},
\]

this gives

\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,5}z^5+O(z^7),
\]

where

\[
\alpha_{i,3}=\frac{\rho_{i,2}}{12Q^6},
\qquad
\alpha_{i,4}=0,
\qquad
\alpha_{i,5}=\frac{\rho_{i,4}}{80Q^{10}}.
\]

This is the strongest natural structural restriction on the \(\eta\)-jets: it kills \(\alpha_{i,4}\).

---

# 2. Expansion of \(A_o\)

The odd-background coefficient is

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

Using

\[
\Delta_0=q_0s+\frac{q_0''}{24}s^3+O(s^5),
\]

\[
q_e=q_0+\frac{q_0''}{8}s^2+O(s^4),
\]

one gets

\[
A_o
=
\frac{2q_0}{s}
+
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)s
+
O(s^3).
\]

Equivalently, in \(z\)-coordinates,

\[
A_o(z)=A_{-1}z^{-1}+A_1z+O(z^3),
\]

with

\[
A_{-1}=2q_0Q^2,
\]

\[
A_1=
\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right).
\]

So the companion term \(q_e\cos\Delta_0/s\) still does not cancel \(\sin\Delta_0/s^2\). It contributes to the same leading \(2q_0/s\) behavior.

---

# 3. Compute \(\nu_{\eta\eta,7}\) under this favorable model

In general,

\[
\nu_{\eta\eta,7}
=
[z^7](A_o\eta_i\eta_j).
\]

With

\[
\eta_i=\alpha_{i,3}z^3+\alpha_{i,5}z^5+O(z^7),
\]

and similarly for \(\eta_j\), the \(z^7\)-coefficient is

\[
\nu_{\eta\eta,7}
=
A_{-1}
(\alpha_{i,3}\alpha_{j,5}+\alpha_{i,5}\alpha_{j,3})
+
A_1\alpha_{i,3}\alpha_{j,3}.
\]

Substituting the integral coefficients,

\[
\boxed{
\nu_{\eta\eta,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
}
\]

This is not identically zero.

---

# 4. Why this does not vanish structurally

For \(\nu_{\eta\eta,7}=0\) to follow from the source-integral model, one would need

\[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
=0.
\]

This is a nontrivial scalar relation between:

\[
\rho_{i,2},\rho_{i,4},\rho_{j,2},\rho_{j,4},
\]

and the baseline phase jets

\[
q_0,\qquad q_0''.
\]

Affine removal does not imply it.

Endpoint-diagonal realization does not imply it.

Source-grade parity does not imply it.

The definition of \(\eta_i\) as a phase-gap integral does not imply it.

For example, set

\[
\rho_{i,4}=\rho_{j,4}=0,
\qquad
\rho_{i,2}\rho_{j,2}\neq0.
\]

Then

\[
\nu_{\eta\eta,7}
=
\frac{1}{144Q^{14}}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}.
\]

This is nonzero on a generic baseline patch where

\[
q_0''\neq 4q_0^3.
\]

If that special baseline relation happened to hold, choosing nonzero \(\rho_{i,4}\) or \(\rho_{j,4}\) would generically make \(\nu_{\eta\eta,7}\neq0\) as long as \(q_0\neq0\).

Thus the row is not killed by the strongest natural \(\eta\)-realization hypothesis.

---

# 5. Fixed-sector consequence remains the same

The row uses

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]

and, on a diagonal right good patch,

\[
W_{+,0}=\operatorname{diag}(u,v).
\]

Then

\[
\operatorname{Sym}(E_{22}JW_{+,0})=uS.
\]

Therefore

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
-\frac{1}{24\pi q^3}
\nu_{\eta\eta,7}
u\,S.
\]

So

\[
e=0,
\]

\[
f=
-\frac{u}{24\pi q^3}\nu_{\eta\eta,7}.
\]

Hence

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
=
a_1^2
\frac{u}{24\pi q^3c}
\nu_{\eta\eta,7}.
\]

If \(\nu_{\eta\eta,7}\neq0\), then

\[
\partial_\kappa T\neq0.
\]

The quotient determinant is

\[
Q=e v_5-u_5 f=-u_5 f.
\]

So on a generic \(u_5\neq0\) patch,

\[
Q\neq0.
\]

This matches the current local target: the row is both \(T\)-visible and generically quotient-visible if the scalar \(\nu_{\eta\eta,7}\) survives. 

---

# 6. Stronger missing theorem

The missing theorem can now be made sharper.

It is **not enough** to prove endpoint-diagonal realization or phase-gap integral realization. The needed theorem is a specific fourth-order source/baseline jet identity:

\[
\boxed{
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
=0
}
\]

for every active pair \(i,j\) entering the promoted \(\eta\eta\) Hessian row.

Equivalently,

\[
\boxed{
\nu_{\eta\eta,7}=0.
}
\]

No current theorem in the draft gives this.

A theorem-ready statement:

```latex
\begin{lemma}[Odd \(\eta\eta\) top-row source-jet cancellation]
For the actual zeta-side promoted source-motion fields, write
\[
\eta_i(s)=\frac{\rho_{i,2}}{12}s^3+\frac{\rho_{i,4}}{80}s^5+O(s^7)
\]
and
\[
A_o(s)=\frac{2q_0}{s}
+
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)s
+O(s^3).
\]
Then for every active pair \(i,j\),
\[
[z^7]A_o(z)\eta_i(z)\eta_j(z)=0.
\]
\end{lemma}
```

But the calculation above shows this is not a formal consequence of the current source model.

---

## Verdict

The odd \(\eta\eta\) top row survives even under the favorable assumption that \(\eta_i\) is the phase-gap integral of one co-moving post-affine source field.

The obstruction is now the explicit scalar

\[
\boxed{
\nu_{\eta\eta,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
}
\]

Unless the actual zeta source construction proves this scalar vanishes or supplies a compensating row, the local Bottleneck-C closure fails at the odd \(\eta\eta\) top row.
## User (2026-04-25 12:50:17)

continue your attack

## Assistant (2026-04-25 12:50:19)

I’ll now include the full \(\eta\eta\) Hessian, not just the off-diagonal \(J\)-block, to test whether diagonal \((1,1)/(2,2)\) Hessian entries or the endpoint-even \(S\)-block can cancel the odd \(J\)-block after fixed-sector projection.

## User (2026-04-25 12:50:36)

continue your attack

## User (2026-04-25 12:51:00)

continue your attack

## Assistant (2026-04-25 12:51:00)

I’ll now test whether the full \(\eta\eta\) Hessian can cancel the off-diagonal odd \(J\)-row. The key check is whether diagonal entries or the endpoint-even \(S\)-block contribute an \(S\)-component of the same source monomial and opposite sign.

_Thought for 1m 21s_

## Continued Local A attack — full \(\eta\eta\) Hessian still leaves an \(S\)-survivor

I expanded the **full off-diagonal \(\eta\eta\) Hessian**, not only the odd \(J\)-piece. This matters because the off-diagonal Hessian is actually

\[
A_oJ-A_eS,
\]

so the endpoint-even \(S\)-piece is the only plausible internal cancellation partner for the odd \(J\)-piece. It does **not** structurally cancel it.

The active row remains the concrete top row

\[
(a,r,g,b)=(2,0,7,0),
\]

inside the frozen Bottleneck-C coefficient \(E_{A,Y}^{\mathrm{BC}}\), which the attached summary identifies as the current lead local obstruction. 

---

# 1. Full off-diagonal \(\eta\eta\) Hessian

From

\[
N_{12}=\frac{\sin\Delta+q_+s\cos\Delta}{s^2},
\qquad
N_{21}=-\frac{\sin\Delta+q_-s\cos\Delta}{s^2},
\]

we have

\[
\partial_\Delta^2N_{12}\big|_0
=
-\frac{\sin\Delta_0}{s^2}
-\frac{q_+\cos\Delta_0}{s},
\]

\[
\partial_\Delta^2N_{21}\big|_0
=
\frac{\sin\Delta_0}{s^2}
+\frac{q_-\cos\Delta_0}{s}.
\]

Let

\[
q_e=\frac{q_++q_-}{2},
\qquad
q_o=\frac{q_+-q_-}{2}.
\]

Then the off-diagonal \(\eta\eta\) Hessian is

\[
\partial_\Delta^2N_{\mathrm{off}}\big|_0
=
A_oJ-A_eS,
\]

where

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s},
\]

\[
A_e
=
\frac{q_o\cos\Delta_0}{s},
\]

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The previous attack treated \(A_oJ\). Now we include \(-A_eS\).

---

# 2. The active source row \(a=2,r=0\)

For the actual finite Fréchet source index \(a=2\),

\[
\Lambda^-_{2,0}
=
\ell E_{22},
\qquad
\ell=-\frac{1}{24\pi q^3}.
\]

Let

\[
W_{+,0}=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}.
\]

Then

\[
E_{22}J W_{+,0}
=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix},
\]

and

\[
E_{22}S W_{+,0}
=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix}.
\]

So both off-diagonal pieces land in the **same fixed-sector \(S\)-direction**, with opposite signs inherited from

\[
A_oJ-A_eS.
\]

Therefore the \(S\)-coefficient of the full off-diagonal row is controlled by

\[
\boxed{
[z^7]\bigl((A_o-A_e)\eta_i\eta_j\bigr).
}
\]

Thus the correct scalar is not merely

\[
[z^7](A_o\eta_i\eta_j),
\]

but

\[
\boxed{
\nu_{\mathrm{off},7}:=[z^7]\bigl((A_o-A_e)\eta_i\eta_j\bigr).
}
\]

The row contributes

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\ell\,u\,\nu_{\mathrm{off},7}\,S
}
\]

on the diagonal good patch.

---

# 3. Expand \(A_o-A_e\)

Using

\[
\Delta_0=q_0s+\frac{q_0''}{24}s^3+O(s^5),
\]

\[
q_e=q_0+\frac{q_0''}{8}s^2+O(s^4),
\]

\[
q_o=\frac{q_0'}2s+O(s^3),
\]

we get

\[
A_o
=
\frac{2q_0}{s}
+
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)s
+O(s^3),
\]

and

\[
A_e
=
\frac{q_o\cos\Delta_0}{s}
=
\frac{q_0'}2
+
O(s^2).
\]

So

\[
A_o-A_e
=
\frac{2q_0}{s}
-\frac{q_0'}2
+
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)s
+O(s^2).
\]

The \(A_e\)-term is different parity/order from the leading \(A_o\)-term. It cannot cancel the leading \(2q_0/s\) part.

---

# 4. Compute the full \([z^7]\) scalar

Write

\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,4}z^4+\alpha_{i,5}z^5+O(z^6),
\]

\[
\eta_j(z)
=
\alpha_{j,3}z^3+\alpha_{j,4}z^4+\alpha_{j,5}z^5+O(z^6).
\]

Let

\[
A_o(z)=A_{-1}z^{-1}+A_1z+O(z^3),
\]

\[
A_e(z)=E_0+O(z^2),
\]

where

\[
A_{-1}=2q_0Q^2,
\]

\[
A_1=\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right),
\]

\[
E_0=\frac{q_0'}2.
\]

Then

\[
\eta_i\eta_j
=
\beta_6z^6+\beta_7z^7+\beta_8z^8+O(z^9),
\]

with

\[
\beta_6=\alpha_{i,3}\alpha_{j,3},
\]

\[
\beta_7=\alpha_{i,3}\alpha_{j,4}+\alpha_{i,4}\alpha_{j,3},
\]

\[
\beta_8=
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}.
\]

Therefore

\[
\boxed{
\nu_{\mathrm{off},7}
=
A_{-1}\beta_8
+
A_1\beta_6
-
E_0\beta_7.
}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
\nu_{\mathrm{off},7}
={}&
2q_0Q^2
\left(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\right)
\\
&+
\frac1{Q^2}
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}
\\
&-
\frac{q_0'}2
\left(
\alpha_{i,3}\alpha_{j,4}
+
\alpha_{i,4}\alpha_{j,3}
\right).
\end{aligned}
}
\]

This is the full off-diagonal \(\eta\eta\) scalar for the top row.

---

# 5. Does this vanish under phase-gap integral realization?

If \(\eta_i\) is the symmetric phase-gap integral of a post-affine source field, then

\[
\alpha_{i,4}=0,
\qquad
\alpha_{j,4}=0.
\]

Then

\[
\beta_7=0,
\]

so the \(A_e\)-term drops out. We return to

\[
\nu_{\mathrm{off},7}
=
A_{-1}(\alpha_{i,3}\alpha_{j,5}+\alpha_{i,5}\alpha_{j,3})
+
A_1\alpha_{i,3}\alpha_{j,3}.
\]

This is exactly the earlier obstruction. Thus even under the favorable integral realization, the endpoint-even \(S\)-block does not save the row.

If \(\alpha_{4}\)-terms are allowed, the \(A_e\)-piece merely adds the extra term

\[
-\frac{q_0'}2
(\alpha_{i,3}\alpha_{j,4}+\alpha_{i,4}\alpha_{j,3}),
\]

which does not structurally cancel the \(A_o\)-terms.

---

# 6. Diagonal Hessian entries cannot cancel the \(S\)-survivor

The full \(\eta\eta\) Hessian also has diagonal entries.

But for the active row

\[
\Lambda^-_{2,0}=\ell E_{22},
\qquad
W_{+,0}=\mathrm{diag}(u,v),
\]

a diagonal Hessian contribution \(D_{\eta\eta}\) gives

\[
E_{22}D_{\eta\eta}W_{+,0},
\]

which is diagonal. After symmetrization and fixed-sector projection, it can contribute to the \(I\)-coordinate but not to the \(S\)-coordinate.

Therefore diagonal Hessian entries cannot cancel the \(S\)-component

\[
\ell u\nu_{\mathrm{off},7}S.
\]

So \(T\)-visibility remains controlled only by

\[
\nu_{\mathrm{off},7}=0.
\]

---

# 7. Consequences

The row gives

\[
E=
\ell u\nu_{\mathrm{off},7}S
+
(\text{possible }I\text{-terms from diagonal Hessian}).
\]

Therefore

\[
\boxed{
f_{A,Y}=\ell u\nu_{\mathrm{off},7}.
}
\]

The \(T\)-slope is

\[
\boxed{
\partial_\kappa T
=
-a_1^2\frac{\ell u\nu_{\mathrm{off},7}}{c}.
}
\]

Thus \(T\)-horizontal closure requires

\[
\boxed{
\nu_{\mathrm{off},7}=0.
}
\]

The quotient determinant is

\[
Q=e v_5-u_5f.
\]

Even if diagonal Hessian entries contribute an \(I\)-term \(e\), there is no structural relation tying it to

\[
f=\ell u\nu_{\mathrm{off},7}
\]

so that

\[
e v_5-u_5f=0.
\]

In particular, on a patch or submodel where diagonal entries are absent or projected away,

\[
Q=-u_5f,
\]

which is generically nonzero for \(u_5\neq0\).

---

# 8. Updated minimal missing theorem

The previous missing theorem

\[
[z^7](A_o\eta_i\eta_j)=0
\]

must be replaced by the full off-diagonal condition

\[
\boxed{
\nu_{\mathrm{off},7}
=
[z^7]\bigl((A_o-A_e)\eta_i\eta_j\bigr)=0.
}
\]

Expanded:

\[
\boxed{
\begin{aligned}
0={}&
2q_0Q^2
\left(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\right)
\\
&+
\frac1{Q^2}
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}
\\
&-
\frac{q_0'}2
\left(
\alpha_{i,3}\alpha_{j,4}
+
\alpha_{i,4}\alpha_{j,3}
\right).
\end{aligned}
}
\]

This is not implied by the current source conventions.

A theorem-ready statement:

```latex id="okwau4"
\begin{lemma}[Full off-diagonal odd \(\eta\eta\) top-row cancellation]
For every active pair of promoted source-motion fields \(\eta_i,\eta_j\),
\[
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
-
\frac{q_o\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right]=0.
\]
Equivalently,
\[
[z^7]\bigl((A_o-A_e)\eta_i\eta_j\bigr)=0.
\]
\end{lemma}
```

---

## Verdict

Including the full off-diagonal \(\eta\eta\) Hessian does **not** close the row.

The concrete \(S\)-visible coefficient is

\[
\boxed{
f_{A,Y}=\ell u\,\nu_{\mathrm{off},7},
}
\]

where

\[
\boxed{
\nu_{\mathrm{off},7}
=
[z^7]\bigl((A_o-A_e)\eta_i\eta_j\bigr).
}
\]

No current theorem forces

\[
\nu_{\mathrm{off},7}=0.
\]

Diagonal Hessian entries cannot cancel this \(S\)-component on the active \(a=2,r=0,b=0\) row. Therefore the local obstruction survives.
## User (2026-04-25 12:52:20)

continue your attack

## Assistant (2026-04-25 12:52:31)

I’ll now remove another simplification: include the full \(\eta\eta\) Hessian matrix, including \(N_{11}\) and \(N_{22}\), and test whether those diagonal entries can cancel the \(S\)-component from the off-diagonal odd block.

_Thought for 28s_

## Continued Local A attack — full \(\eta\eta\) Hessian does **not** cancel the \(S\)-leak

I included the full \(\eta\eta\) Hessian matrix, including the diagonal \(N_{11}\) and \(N_{22}\) entries. This was the remaining possible internal cancellation mechanism for the top row

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[\partial_\Delta^2N_0\cdot\eta_i\eta_j\right]_7
W_{+,0}
\right).
\]

The conclusion is:

\[
\boxed{
\text{the diagonal Hessian entries cannot cancel the \(S\)-component of this row.}
}
\]

The local obstruction remains the same scalar

\[
\boxed{
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
}
\]

This is the concrete lead local obstruction requested in the latest Local Agent 1 prompt. 

---

# 1. Full \(\eta\eta\) Hessian of \(N^{\corr}\)

For the corrected mixed block entries

\[
N_{11}=-\frac{2\sin\Delta}{s},
\]

\[
N_{12}=\frac{\sin\Delta+q_+s\cos\Delta}{s^2},
\]

\[
N_{21}=-\frac{\sin\Delta+q_-s\cos\Delta}{s^2},
\]

\[
N_{22}=
\frac{(q_-+q_+)s\cos\Delta+(2-q_-q_+s^2)\sin\Delta}{2s^3},
\]

twice differentiating in \(\Delta\) gives

\[
H_{\eta\eta}
:=
\partial_\Delta^2N^{\corr}\big|_{\Delta=\Delta_0}.
\]

Entrywise:

\[
(H_{\eta\eta})_{11}
=
\frac{2\sin\Delta_0}{s},
\]

\[
(H_{\eta\eta})_{12}
=
-\frac{\sin\Delta_0}{s^2}
-
\frac{q_+\cos\Delta_0}{s},
\]

\[
(H_{\eta\eta})_{21}
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s},
\]

\[
(H_{\eta\eta})_{22}
=
-\frac{(q_-+q_+)\cos\Delta_0}{2s^2}
-
\frac{(2-q_-q_+s^2)\sin\Delta_0}{2s^3}.
\]

So the full matrix is

\[
H_{\eta\eta}
=
\begin{pmatrix}
2\sin\Delta_0/s
&
-\sin\Delta_0/s^2-q_+\cos\Delta_0/s
\\[1ex]
\sin\Delta_0/s^2+q_-\cos\Delta_0/s
&
-\dfrac{(q_-+q_+)\cos\Delta_0}{2s^2}
-\dfrac{(2-q_-q_+s^2)\sin\Delta_0}{2s^3}
\end{pmatrix}.
\]

Multiplication by \(\eta_i\eta_j\) is understood.

---

# 2. Insert the exact \(a=2,r=0\) Fréchet row

For the actual finite Fréchet index \(a=2\),

\[
\Lambda^-_{2,0}
=
\ell E_{22},
\qquad
\ell=-\frac{1}{24\pi q^3}
\]

on a diagonal good patch.

Let

\[
W_{+,0}
=
\begin{pmatrix}
u&0\\
0&v
\end{pmatrix}.
\]

Then

\[
\Lambda^-_{2,0}H_{\eta\eta}W_{+,0}
=
\ell E_{22}H_{\eta\eta}W_{+,0}.
\]

Because \(E_{22}\) selects the second row,

\[
E_{22}H_{\eta\eta}W_{+,0}
=
\begin{pmatrix}
0&0\\
uH_{21}&vH_{22}
\end{pmatrix}.
\]

Symmetrizing gives

\[
\operatorname{Sym}
\left(E_{22}H_{\eta\eta}W_{+,0}\right)
=
\begin{pmatrix}
0&uH_{21}\\
uH_{21}&2vH_{22}
\end{pmatrix}.
\]

After fixed-sector projection to

\[
\mathfrak f=\operatorname{span}\{I,S\},
\]

the \(S\)-coordinate is exactly

\[
\boxed{
uH_{21}.
}
\]

The diagonal \(H_{22}\) contributes only to the diagonal sector, hence at most to the \(I\)-coordinate after projection. It cannot cancel the \(S\)-coordinate.

The entries \(H_{11}\) and \(H_{12}\) do not enter this \(a=2,r=0\) row at all, because \(E_{22}\) selects the second row before multiplication by \(W_{+,0}\).

Therefore the full Hessian gives

\[
\boxed{
f_{\eta\eta;7,0,0}^{(2)}
=
\ell u\,[z^7]\left(H_{21}\eta_i\eta_j\right).
}
\]

---

# 3. The real scalar is the \((2,1)\)-entry

Since

\[
H_{21}
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s},
\]

the row’s \(S\)-coefficient is

\[
\boxed{
f_{\eta\eta;7,0,0}^{(2)}
=
\ell u\,
[z^7]
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right].
}
\]

This is slightly sharper than the earlier \(A_o-A_e\) notation, since

\[
A_o-A_e
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}.
\]

So the relevant scalar is

\[
\boxed{
\nu_{21,7}
:=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right].
}
\]

---

# 4. Expansion of \(\nu_{21,7}\)

Use

\[
q_-(s)=q_0-\frac{q_0'}2s+\frac{q_0''}{8}s^2+O(s^3),
\]

and

\[
\Delta_0
=
q_0s+\frac{q_0''}{24}s^3+O(s^5).
\]

Then

\[
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\]

expands as

\[
\frac{2q_0}{s}
-\frac{q_0'}2
+
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)s
+O(s^2).
\]

In \(z\)-coordinates,

\[
s=\frac{z}{Q^2},
\]

so write

\[
B_{21}(z)
:=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
=
B_{-1}z^{-1}+B_0+B_1z+O(z^2),
\]

where

\[
B_{-1}=2q_0Q^2,
\]

\[
B_0=-\frac{q_0'}2,
\]

\[
B_1=\frac{1}{Q^2}
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right).
\]

Let

\[
\eta_i
=
\alpha_{i,3}z^3+\alpha_{i,4}z^4+\alpha_{i,5}z^5+O(z^6),
\]

\[
\eta_j
=
\alpha_{j,3}z^3+\alpha_{j,4}z^4+\alpha_{j,5}z^5+O(z^6).
\]

Then

\[
\eta_i\eta_j
=
\beta_6z^6+\beta_7z^7+\beta_8z^8+O(z^9),
\]

with

\[
\beta_6=\alpha_{i,3}\alpha_{j,3},
\]

\[
\beta_7=\alpha_{i,3}\alpha_{j,4}+\alpha_{i,4}\alpha_{j,3},
\]

\[
\beta_8=
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}.
\]

Thus

\[
\boxed{
\nu_{21,7}
=
B_{-1}\beta_8+B_0\beta_7+B_1\beta_6.
}
\]

Expanded:

\[
\boxed{
\begin{aligned}
\nu_{21,7}
={}&
2q_0Q^2
\left(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\right)
\\
&-
\frac{q_0'}2
\left(
\alpha_{i,3}\alpha_{j,4}
+
\alpha_{i,4}\alpha_{j,3}
\right)
\\
&+
\frac1{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}.
\end{aligned}
}
\]

This is the full scalar controlling the \(S\)-component of the concrete row.

---

# 5. Does symmetric phase-gap integral realization kill it?

If

\[
\eta_i(s)=\int_{-s/2}^{s/2}r_i(u)\,du
\]

with post-affine

\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,3}u^3+\rho_{i,4}u^4+\cdots,
\]

then

\[
\alpha_{i,4}=0.
\]

So

\[
\beta_7=0,
\]

and the \(B_0\beta_7\) term drops.

But

\[
\nu_{21,7}
=
B_{-1}\beta_8+B_1\beta_6
\]

remains:

\[
\nu_{21,7}
=
2q_0Q^2
(\alpha_{i,3}\alpha_{j,5}+\alpha_{i,5}\alpha_{j,3})
+
\frac1{Q^2}
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}.
\]

This is not structurally zero.

Thus even the favorable phase-gap integral realization does not kill the row.

---

# 6. Does the diagonal Hessian cancel the quotient determinant?

The diagonal Hessian can contribute an \(I\)-coordinate \(e\), but not the \(S\)-coordinate \(f\) for this row. Therefore it cannot help with \(T\)-horizontal closure, which requires

\[
f=0.
\]

For quotient closure,

\[
Q=e v_5-u_5f.
\]

In principle, a diagonal Hessian \(I\)-term could accidentally satisfy

\[
e v_5=u_5f.
\]

But this would be a new scalar relation between unrelated diagonal Hessian source contractions and the off-diagonal \(H_{21}\) contraction. The current source symmetries do not impose it.

Moreover, on submodels or patches where the diagonal contribution is absent or projected out, the row remains purely \(S\)-visible. Thus quotient closure is not structural.

---

# 7. Concrete survivor

The concrete fixed-sector coefficient is:

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
=
e_{\mathrm{diag}}I
+
\ell u\nu_{21,7}S,
}
\]

where

\[
\ell=-\frac{1}{24\pi q^3}.
\]

The \(S\)-coordinate is

\[
\boxed{
f=\ell u\nu_{21,7}.
}
\]

Thus

\[
\boxed{
\partial_\kappa T
=
-a_1^2\frac{\ell u\nu_{21,7}}{c}.
}
\]

And

\[
\boxed{
Q
=
e_{\mathrm{diag}}v_5-u_5\ell u\nu_{21,7}.
}
\]

Without a theorem forcing

\[
\nu_{21,7}=0
\]

or a very specific quotient-line identity for \(e_{\mathrm{diag}}\), this row survives.

---

# 8. Minimal missing theorem

The concrete theorem needed is:

```latex id="mrx6g5"
\begin{lemma}[Odd \(\eta\eta\) \((2,1)\)-entry top-row cancellation]
For every active pair of promoted source-motion fields \(\eta_i,\eta_j\),
\[
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]=0.
\]
\end{lemma}
```

Expanded, this is:

\[
\boxed{
\begin{aligned}
0={}&
2q_0Q^2
\left(
\alpha_{i,3}\alpha_{j,5}
+
\alpha_{i,5}\alpha_{j,3}
+
\alpha_{i,4}\alpha_{j,4}
\right)
\\
&-
\frac{q_0'}2
\left(
\alpha_{i,3}\alpha_{j,4}
+
\alpha_{i,4}\alpha_{j,3}
\right)
\\
&+
\frac1{Q^2}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\alpha_{i,3}\alpha_{j,3}.
\end{aligned}
}
\]

This is not currently proved by parity, endpoint-diagonal realization, phase-gap integral realization, or fixed-sector symmetrization.

---

## Verdict

The full \(\eta\eta\) Hessian does not cancel the odd top-row obstruction.

The concrete survivor is governed by

\[
\boxed{
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
}
\]

If

\[
\nu_{21,7}\neq0,
\]

then

\[
f_{A,Y}\neq0,
\]

so

\[
\partial_\kappa T\neq0.
\]

Generically, quotient Bottleneck-C also fails. The local branch remains blocked by this single scalar source-jet identity.
## User (2026-04-25 12:53:34)

continue your attack

## Assistant (2026-04-25 12:53:36)

I’ll attack the remaining scalar \(\nu_{21,7}\) using the strongest structural identity available: interpret \(\Delta_0\) and \(\eta_i\) as endpoint integrals, then see whether \(H_{21}\eta_i\eta_j\) becomes a total derivative or boundary term that vanishes.

_Thought for 22s_

## Continued Local A attack — reduce \(\nu_{21,7}=0\) to a rank-one source-jet locking theorem

I attacked the remaining scalar obstruction

\[
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
\]

The goal was to see whether \(\nu_{21,7}=0\) follows if \(\eta_i\) is realized in the strongest natural way: as the actual phase-gap integral of a post-affine source field. It still does **not** vanish structurally.

The obstruction now reduces to a very specific **rank-one source-jet locking condition**. Without that condition, the row

\[
(a,r,g,b)=(2,0,7,0),\qquad \chi=\eta\eta_{\rm odd}
\]

remains \(S\)-visible and therefore \(T\)-visible. This row is the lead local blocker identified in the current prompt. 

---

# 1. Integral realization of \(\eta_i\)

Assume the favorable source model

\[
\eta_i(s)=\int_{-s/2}^{s/2} r_i(u)\,du
\]

with post-affine source field

\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,3}u^3+\rho_{i,4}u^4+O(u^5).
\]

Then

\[
\eta_i(s)
=
\frac{\rho_{i,2}}{12}s^3
+
\frac{\rho_{i,4}}{80}s^5
+
O(s^7),
\]

because the odd \(u^3\)-term integrates to zero.

In \(z\)-coordinates, \(s=z/Q^2\), so

\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,5}z^5+O(z^7),
\]

with

\[
\alpha_{i,3}=\frac{\rho_{i,2}}{12Q^6},
\qquad
\alpha_{i,5}=\frac{\rho_{i,4}}{80Q^{10}}.
\]

Thus the integral realization kills \(\alpha_{i,4}\), but it does not kill the \(\alpha_{i,3}\) or \(\alpha_{i,5}\) data.

---

# 2. Expansion of the \((2,1)\)-entry coefficient

The relevant scalar is

\[
B_{21}
:=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}.
\]

Using

\[
\Delta_0=q_0s+\frac{q_0''}{24}s^3+O(s^5),
\]

\[
q_-=q_0-\frac{q_0'}2s+\frac{q_0''}{8}s^2+O(s^3),
\]

one gets

\[
B_{21}
=
\frac{2q_0}{s}
-\frac{q_0'}2
+
\left(
\frac{q_0''}{6}
-\frac{2q_0^3}{3}
\right)s
+
O(s^2).
\]

Under the integral realization, \(\eta_i\eta_j\) has no \(z^7\)-term because \(\alpha_4=0\). Hence the \(-q_0'/2\) term does not contribute to \([z^7]\). The surviving coefficient is

\[
\nu_{21,7}
=
[z^7](B_{21}\eta_i\eta_j).
\]

Substituting the integral coefficients gives

\[
\boxed{
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
}
\]

This is the exact scalar controlling the \(S\)-component of the concrete top row under the favorable phase-gap integral model.

---

# 3. Bilinear form interpretation

Define

\[
R_0
:=
\frac{q_0''}{6}-\frac{2q_0^3}{3}.
\]

Then, up to the common factor \(Q^{-14}\),

\[
\nu_{21,7}
\]

is the symmetric bilinear form

\[
\mathcal B((\rho_2,\rho_4),(\sigma_2,\sigma_4))
=
\frac{q_0}{480}(\rho_2\sigma_4+\rho_4\sigma_2)
+
\frac{R_0}{144}\rho_2\sigma_2.
\]

So local closure for all active source pairs requires

\[
\mathcal B(v_i,v_j)=0
\]

for all active source-jet vectors

\[
v_i=(\rho_{i,2},\rho_{i,4}).
\]

This is a strong rank condition on the active source-jet subspace.

---

# 4. Consequences

## If the active \(\eta\)-source space has dimension \(\ge 2\)

Then requiring

\[
\mathcal B(v_i,v_j)=0
\]

for all pairs \(i,j\) forces the active source subspace to be totally isotropic for \(\mathcal B\).

For generic

\[
q_0\neq0,
\]

the bilinear form

\[
\mathcal B
\]

has matrix

\[
\begin{pmatrix}
R_0/144 & q_0/480\\[0.4ex]
q_0/480 & 0
\end{pmatrix},
\]

whose determinant is

\[
-\frac{q_0^2}{480^2}\neq0.
\]

So it is nondegenerate. In a two-dimensional source-jet plane, it cannot vanish identically. Hence the active source subspace would have to be at most one-dimensional and isotropic.

No current draft theorem imposes that.

## If the active \(\eta\)-source space is one-dimensional

Suppose all active sources satisfy

\[
\rho_{i,4}=\lambda \rho_{i,2}.
\]

Then

\[
\nu_{21,7}=0
\]

for all pairs would require

\[
\frac{q_0}{240}\lambda+\frac{R_0}{144}=0.
\]

Thus

\[
\boxed{
\lambda
=
-\frac{5}{3}\frac{R_0}{q_0}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right).
}
\]

Equivalently,

\[
\boxed{
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}
}
\]

for every active source \(i\).

This is a very specific fourth-order/second-order jet-locking law. It is not affine removal. It is not endpoint diagonalization. It is not phase-gap integral realization. It is a new zeta-specific source-jet constraint.

---

# 5. Formal source-model counterexamples

The obstruction survives in simple cases.

## Case 1: \(\rho_4=0\)

Take

\[
\rho_{i,4}=\rho_{j,4}=0,
\qquad
\rho_{i,2}\rho_{j,2}\neq0.
\]

Then

\[
\nu_{21,7}
=
\frac{R_0}{144Q^{14}}\rho_{i,2}\rho_{j,2}.
\]

If

\[
R_0\neq0,
\]

the row survives.

## Case 2: \(R_0=0\)

Even if

\[
R_0=0,
\]

choose

\[
\rho_{i,2}\neq0,\qquad \rho_{j,4}\neq0,
\]

with \(q_0\neq0\). Then

\[
\nu_{21,7}
=
\frac{q_0}{480Q^{14}}\rho_{i,2}\rho_{j,4}
\neq0.
\]

Thus no generic baseline identity such as \(R_0=0\) is enough unless it is paired with source-space collapse.

---

# 6. Fixed-sector consequence

Recall

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]

and for diagonal

\[
W_{+,0}=\operatorname{diag}(u,v),
\]

we computed

\[
\operatorname{Sym}(E_{22}JW_{+,0})=uS.
\]

Therefore the concrete row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
-\frac{u}{24\pi q^3}\nu_{21,7}\,S.
\]

So

\[
\boxed{
f_{A,Y}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
}
\]

Thus

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
a_1^2\frac{u}{24\pi q^3c}\nu_{21,7}.
\]

If

\[
\nu_{21,7}\neq0,
\]

then

\[
\partial_\kappa T\neq0.
\]

The quotient determinant is

\[
Q=e v_5-u_5f.
\]

For this pure \(S\)-row,

\[
e=0,
\qquad
Q=-u_5f.
\]

So on a generic \(u_5\neq0\) patch,

\[
Q\neq0.
\]

---

# 7. Missing theorem, sharpened

The local branch now requires one of the following.

## Strong source-space collapse

All active promoted \(\eta\)-source fields must have jet vectors

\[
(\rho_{i,2},\rho_{i,4})
\]

lying in a one-dimensional isotropic line for

\[
\mathcal B.
\]

Equivalently,

\[
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)\rho_{i,2}
\]

for every active \(i\).

## Or direct top-row cancellation

For every active pair \(i,j\),

\[
\nu_{21,7}=0.
\]

A theorem-ready version:

```latex id="m92cri"
\begin{lemma}[Odd \(\eta\eta\) top-row source-jet locking]
For every active promoted source-motion field \(r_i\), write
\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,4}u^4+O(u^5)
\]
after affine removal.  Then
\[
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)\rho_{i,2}.
\]
Consequently,
\[
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]=0
\]
for all active \(i,j\).
\end{lemma}
```

No theorem in the current draft appears to imply this locking law.

---

## Verdict

Even under the strongest natural realization

\[
\eta_i(s)=\int_{-s/2}^{s/2}r_i(u)\,du,
\]

the odd \(\eta\eta\) top row survives unless the active source jets satisfy a very specific fourth-order/second-order locking condition.

The local obstruction is now:

\[
\boxed{
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
}
\]

The current source model does not force this to vanish. Therefore the concrete odd-\(\eta\eta\) top row remains a live \(T\)- and quotient-visible blocker.
## User (2026-04-25 12:54:47)

continue your attack

## Assistant (2026-04-25 12:54:53)

I’ll now test the proposed locking law against the actual homogeneous source basis. If the active source directions include the quadratic source \(r(u)=u^2\), the odd-\(\eta\eta\) row should already survive generically.

_Thought for 8s_

## Continued Local A attack — homogeneous source basis refutes the locking law

The last remaining escape was the source-jet locking condition

\[
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)\rho_{i,2}.
\]

I attacked this against the **homogeneous source basis** itself. It fails generically.

So the odd-\(\eta\eta\) top-row obstruction is not only formally possible; it already appears if the active promoted source space contains the quadratic homogeneous source direction. The latest prompt identifies this row as the lead local obstruction and asks specifically to attack

\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]

---

# 1. Recall the surviving scalar

Under the strongest favorable realization

\[
\eta_i(s)=\int_{-s/2}^{s/2}r_i(u)\,du,
\]

we derived

\[
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]

The row contributes

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
-\frac{u}{24\pi q^3}\nu_{21,7}\,S
\]

on a diagonal good patch, so

\[
f_{A,Y}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

Thus the top row is \(T\)-safe only if

\[
\nu_{21,7}=0.
\]

---

# 2. Test the pure quadratic homogeneous source

Take the homogeneous post-affine source

\[
r(u)=u^2.
\]

Then

\[
\rho_2=1,\qquad \rho_4=0.
\]

For the pair \(i=j\), the obstruction becomes

\[
\nu_{21,7}
=
\frac{1}{144Q^{14}}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right).
\]

So the row vanishes for this source only if

\[
\boxed{
q_0''=4q_0^3.
}
\]

There is no current theorem in the draft imposing this baseline differential identity.

Indeed, for the simplest locally constant good phase model,

\[
q_0\neq0,\qquad q_0''=0,
\]

we get

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}\neq0.
\]

Therefore the pure quadratic homogeneous source already gives a nonzero odd-\(\eta\eta\) top-row coefficient.

---

# 3. Test the pure quartic homogeneous source

Take

\[
r(u)=u^4.
\]

Then

\[
\rho_2=0,\qquad \rho_4=1.
\]

For \(i=j\),

\[
\nu_{21,7}=0,
\]

because the product \(\eta_i\eta_i\) begins too high for this top row.

But for a mixed pair

\[
r_i(u)=u^2,\qquad r_j(u)=u^4,
\]

we get

\[
\rho_{i,2}=1,\quad \rho_{i,4}=0,
\qquad
\rho_{j,2}=0,\quad \rho_{j,4}=1,
\]

and hence

\[
\nu_{21,7}
=
\frac{q_0}{480Q^{14}}.
\]

On a good phase patch

\[
q_0\neq0,
\]

this is nonzero.

So if the active source space contains both quadratic and quartic homogeneous directions, the odd-\(\eta\eta\) top row survives even if

\[
q_0''=4q_0^3.
\]

---

# 4. What source-space restriction would be needed?

For all active source pairs to satisfy

\[
\nu_{21,7}=0,
\]

the active two-jet/four-jet vectors

\[
v_i=(\rho_{i,2},\rho_{i,4})
\]

must lie in a totally isotropic subspace for the symmetric bilinear form

\[
\mathcal B(v_i,v_j)
=
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{R_0}{144}\rho_{i,2}\rho_{j,2},
\]

where

\[
R_0=\frac{q_0''}{6}-\frac{2q_0^3}{3}.
\]

The matrix of \(\mathcal B\) is

\[
\begin{pmatrix}
R_0/144 & q_0/480\\[0.4ex]
q_0/480 & 0
\end{pmatrix}.
\]

Its determinant is

\[
-\frac{q_0^2}{480^2}.
\]

So on a good phase patch \(q_0\neq0\), this form is nondegenerate.

Thus a two-dimensional active source space cannot be totally isotropic. At most, all active sources could lie on a single isotropic line

\[
\rho_4=\lambda\rho_2,
\]

where

\[
\lambda
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right).
\]

That is exactly the previously identified locking law.

The homogeneous source basis \(\{u^2,u^4\}\) does **not** lie on such a line. Therefore the locking theorem is incompatible with retaining both homogeneous source directions as independent active inputs.

---

# 5. Consequence for the local proof

The local proof now needs one of the following strong statements.

## Option A: active source collapse

The promoted \(\eta\)-source space must be one-dimensional in the \((\rho_2,\rho_4)\)-projection and must lie on the special isotropic line

\[
\rho_4
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\frac{\rho_2}{q_0}.
\]

Equivalently, all active source fields must satisfy

\[
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)\rho_{i,2}.
\]

## Option B: baseline differential identity plus source exclusion

If the source space contains \(u^2\) only, then one could kill the \(u^2,u^2\) pair by imposing

\[
q_0''=4q_0^3.
\]

But this still does not kill the mixed \(u^2,u^4\) pair unless the \(u^4\) direction is excluded or \(q_0=0\), which is not a good phase patch.

## Option C: added correction term

Introduce a correction to the package cancelling

\[
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]_7
W_{+,0}
\]

at the fixed-sector level.

No existing source symmetry supplies this.

---

# 6. The sharp countermodel

A compact formal countermodel is:

\[
q_0\neq0,\qquad q_0''=0,
\]

\[
r_i(u)=r_j(u)=u^2.
\]

Then

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}\neq0.
\]

The row contributes

\[
E
=
-\frac{u}{24\pi q^3}\nu_{21,7}\,S.
\]

So

\[
f_{A,Y}\neq0,
\]

and

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
\neq0.
\]

If \(u_5\neq0\), then

\[
Q_{A,Y}
=
-u_5f_{A,Y}
\neq0.
\]

This countermodel respects:

- affine removal, since \(u^2\) has no constant or affine part;
- endpoint symmetry, since \(\eta(s)=\int_{-s/2}^{s/2}u^2\,du\);
- source-grade parity;
- the frozen Bottleneck-C bookkeeping;
- the actual \(a=2,r=0\) Fréchet row.

So the desired local cancellation is not a consequence of the current package.

---

# 7. Missing theorem, now sharpened

A theorem capable of killing this row must explicitly say one of the following:

```latex
\begin{lemma}[Active promoted source-space isotropy]
For every active promoted source-motion field \(r_i\), the pair of Taylor
coefficients \((\rho_{i,2},\rho_{i,4})\) lies on the isotropic line
\[
\rho_{i,4}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)\rho_{i,2}.
\]
\end{lemma}
```

or:

```latex
\begin{lemma}[Odd \(\eta\eta\) top-row cancellation]
For every active pair \(i,j\),
\[
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]=0.
\]
\end{lemma}
```

The first is a source-space collapse theorem. The second is the direct row cancellation theorem. The current draft proves neither.

---

## Verdict

The attack shows that the odd-\(\eta\eta\) top row survives even in the favorable phase-gap integral model if the active source space includes the quadratic homogeneous direction.

The simplest surviving scalar is:

\[
\boxed{
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}
\quad
\text{for }r_i=r_j=u^2,\ q_0''=0.
}
\]

Thus the local proof is blocked unless the draft proves a new active-source isotropy/collapse theorem, a direct odd-\(\eta\eta\) cancellation theorem, or adds a correction term.
## User (2026-04-25 13:46:57)

Do the local agent attack

## Assistant (2026-04-25 13:46:59)

I’ll treat the odd \(\eta\eta\) row as genuinely live and now look for a missing **correction mechanism** in the package: second-order phase-gap correction, normalization, source-bidegree projection, midpoint transport, or connection terms that could contribute the opposite \(S\)-coefficient.

_Thought for 43s_

## Local A continued — no existing correction mechanism cancels the odd \(\eta\eta\) top row

I treated the row as a live defect and searched the package mechanisms that could plausibly cancel it:

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right]_7
W_{+,0}
\right).
\]

Result:

\[
\boxed{
\text{No existing package mechanism cancels this row.}
}
\]

The current package cannot close Bottleneck C at this row unless the draft adds either:

\[
\boxed{\nu_{21,7}=0}
\]

as a zeta-specific source-jet theorem, or an explicit new correction term with the opposite \(S\)-coefficient.

The attached latest summary identifies exactly this row as the lead local obstruction and records its \(S\)-coefficient

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

It also says the local proof now requires cancellation of \(\nu_{21,7}\), full top-row \(S\)-cancellation, or a new correction package. 

---

# 1. The live row

The row is governed by

\[
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right].
\]

Under the favorable phase-gap integral model,

\[
\eta_i(s)=\int_{-s/2}^{s/2}r_i(u)\,du,
\]

with

\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,4}u^4+\cdots,
\]

this becomes

\[
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]

For the homogeneous source

\[
r_i=r_j=u^2,
\qquad q_0''=0,
\]

we get

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]

which is nonzero on a good phase patch \(q_0\ne0\). This is compatible with affine removal, endpoint symmetry, source-grade parity, and the frozen Bottleneck-C bookkeeping. 

The fixed-sector contribution is

\[
E_{\eta\eta}^{\rm top}
=
0\cdot I
-
\frac{u}{24\pi q^3}\nu_{21,7}\,S.
\]

Thus

\[
f_{A,Y}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

So

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
a_1^2\frac{u}{24\pi q^3c}\nu_{21,7}.
\]

If \(u_5\ne0\), then the quotient determinant also survives:

\[
Q_{A,Y}
=
e v_5-u_5f
=
u_5\frac{u}{24\pi q^3}\nu_{21,7}.
\]

---

# 2. Source-bidegree projection does not cancel it

The row has the amplitude pattern

\[
a_1a_2(a_1+a_2).
\]

The middle Hessian \(Y_{12}^{(2)}\) is source-bidegree \((1,1)\), but the same-point whitening slot contributes one additional source factor. Therefore the promoted term is degree three:

\[
(2,1)+(1,2).
\]

It is not killed by the \((1,1)\)-projection. This is exactly why the amplitude factor is

\[
a_1a_2(a_1+a_2),
\]

and why it creates the Bottleneck-C \(\kappa\)-edge on the balanced collision chart.

So source-bidegree projection cannot remove the row.

---

# 3. Amplitude normalization does not cancel it

Amplitude normalization can rescale the promoted carrier. It does not create a matrix term with the required opposite \(S\)-coefficient.

The row is

\[
-\frac{u}{24\pi q^3}\nu_{21,7}S.
\]

A scalar amplitude normalization could only multiply this by a scalar or introduce lower-degree amplitude corrections. It cannot produce the specific counterterm

\[
+\frac{u}{24\pi q^3}\nu_{21,7}S
\]

unless the normalization is explicitly defined to depend on this \(\eta\eta\) Hessian coefficient. No such normalization exists in the current package.

Thus amplitude normalization does not close the row.

---

# 4. Connection correction cannot be used here

The connection correction belongs to the post-edge / post-trivialization package. It is not a raw cancellation mechanism for the frozen Bottleneck-C coefficient.

The current local object is the frozen internal carrier:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}[z^7]
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0.
\]

The bookkeeping correction is crucial: this is not the later source-motion \([z^7\delta^1]\) coefficient. The amplitude already supplies the \(\delta\)-edge. 

A connection term can alter how an already-formed edge package is transported or quotiented. It cannot prove the raw frozen coefficient is zero. Using post-edge connection correction to cancel the raw Bottleneck-C carrier would reverse the order of operations.

So connection correction cannot be used as a closure proof for this row.

---

# 5. Midpoint trivialization / \(\tau_{h\to m}\) does not cancel it

The row is already evaluated at the frozen face. The map

\[
\tau_{h\to m}
\]

is a transport/trivialization into the \(m\)-fiber. It is linear and invertible on a good patch. It cannot annihilate a nonzero \(S\)-component unless the row lies in the transport kernel, and there is no such kernel on a good patch.

Thus

\[
\tau_{h\to m}
\]

cannot be the missing cancellation.

---

# 6. Fixed-sector quotienting is insufficient

If the row were line-gauge,

\[
E=\lambda A_5^{\mathfrak f},
\]

then quotient Bottleneck C would close. But the augmented transform-safe package still fails unless

\[
\Phi_K(E)=0.
\]

Since

\[
\Phi_K(A_5^{\mathfrak f})=2v_5,
\]

a nonzero line-gauge row leaks through \(T\) on the generic \(v_5\ne0\) patch. The current framework already split Bottleneck C into quotient closure and \(T\)-horizontal closure for exactly this reason. 

Our row is a pure \(S\)-component in the diagonal good patch:

\[
E
=
-\frac{u}{24\pi q^3}\nu_{21,7}S.
\]

Even if a special patch made it quotient-invisible, it remains \(T\)-visible unless

\[
\nu_{21,7}=0.
\]

Therefore quotienting cannot repair the full augmented package.

---

# 7. The only viable correction term

A correction term would need to contribute precisely

\[
C_{\eta\eta}^{\rm corr}
=
+\frac{u}{24\pi q^3}\nu_{21,7}S
\]

to the frozen Bottleneck-C coefficient.

At the matrix level, before fixed-sector projection, it would need the form

\[
\Delta Y_{\eta\eta}^{\rm corr}
=
-
\left[
\partial_\Delta^2N_0
\right]_{\eta\eta,\mathrm{odd}}
\]

in the active \((2,1)\)-entry seen by

\[
\Lambda^-_{2,0}=\ell E_{22}.
\]

Equivalently, it must subtract

\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\]

from the \((2,1)\)-entry of the promoted mixed-block Hessian at the relevant \(z^7\)-coefficient.

That is not currently part of the corrected package. Adding it would be a genuine package-design change, not a consequence of the existing definitions.

---

# 8. No current package closure

Therefore the current package cannot close Bottleneck C at this row.

A theorem-ready no-go statement:

```latex
\begin{lemma}[Odd \(\eta\eta\) top-row is not cancelled by the current package]
In the current corrected-package construction, the mechanisms of
source-bidegree projection, amplitude normalization, midpoint
trivialization, connection correction, and fixed-sector quotienting do not
produce a term cancelling
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right]_7
W_{+,0}
\right).
\]
Consequently, the current package closes this row only if
\[
\nu_{21,7}=0
\]
or if an additional correction term is added to cancel the row.
\end{lemma}
```

---

## Verdict

The attack finds no hidden cancellation mechanism in the current package.

The local proof now has a binary choice:

\[
\boxed{
\text{prove the zeta-specific source-jet identity }\nu_{21,7}=0,
}
\]

or

\[
\boxed{
\text{add a new second-order phase-gap correction cancelling this row.}
}
\]

Without one of these, the current corrected package cannot close Bottleneck C or the \(T\)-horizontal condition at the concrete row

\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]
## User (2026-04-25 13:52:15)

Do the local package-design agent instruction

## Assistant (2026-04-25 13:52:17)

I’ll treat the odd \(\eta\eta\) top row as a genuine defect and test package-design repairs: phase-gap reparametrization, Hessian subtraction, source-coordinate normal form, and post-edge correction.

_Thought for 55s_

## Local package-design attack — current package needs a new off-diagonal phase-gap normal form

I treated the concrete local defect

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}
\]

as genuinely live and searched for a package-level repair. The latest shared state says exactly this: the current package does not cancel the row, and the local branch is now binary—either prove \(\nu_{21,7}=0\) by a new zeta-specific source-jet identity, or add a new second-order phase-gap correction/counterterm. 

My conclusion:

\[
\boxed{
\text{A scalar reparametrization of }\Delta\text{ is insufficient.}
}
\]

\[
\boxed{
\text{A principled repair is possible only by changing the off-diagonal phase-gap coordinate.}
}
\]

The natural candidate is to use the **off-diagonal numerator variables**

\[
\Theta_+ := \sin\Delta+q_+s\cos\Delta,
\qquad
\Theta_- := \sin\Delta+q_-s\cos\Delta,
\]

so that

\[
N_{12}=\frac{\Theta_+}{s^2},
\qquad
N_{21}=-\frac{\Theta_-}{s^2}.
\]

In these variables the off-diagonal entries are affine, so the dangerous pure \(\eta\eta\) Hessian in \(N_{12},N_{21}\) disappears by construction.

---

# 1. Why the current package fails

The live row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]_7
W_{+,0}
\right).
\]

With

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]

and diagonal

\[
W_{+,0}=\operatorname{diag}(u,v),
\]

this gives

\[
E_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}S.
\]

So

\[
f_{A,Y}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

The current package mechanisms do not cancel it:

- source-bidegree projection keeps the promoted degree-three carrier;
- amplitude normalization only rescales;
- midpoint trivialization is invertible;
- connection correction is post-edge and cannot cancel the raw frozen coefficient;
- quotienting is insufficient because the augmented package requires \(f_{A,Y}=0\), not only quotient-line invisibility.

This agrees with the current round’s conclusion. 

---

# 2. Scalar phase-gap reparametrization is not enough

Try a scalar second-order reparametrization

\[
\Delta=\Theta+\frac12 c\,\Theta^2+O(\Theta^3).
\]

For any mixed-block entry \(N_{\alpha\beta}(\Delta)\), the second \(\Theta\)-derivative becomes

\[
\partial_\Theta^2N_{\alpha\beta}
=
\partial_\Delta^2N_{\alpha\beta}
+
c\,\partial_\Delta N_{\alpha\beta}.
\]

To cancel the \((2,1)\)-entry, one needs

\[
c=c_-,
\]

where

\[
c_-
=
-\frac{\partial_\Delta^2 N_{21}}{\partial_\Delta N_{21}}
=
\frac{\sin\Delta_0+q_-s\cos\Delta_0}
{\cos\Delta_0-q_-s\sin\Delta_0}.
\]

To cancel the \((1,2)\)-entry, one needs

\[
c=c_+,
\]

where

\[
c_+
=
-\frac{\partial_\Delta^2 N_{12}}{\partial_\Delta N_{12}}
=
\frac{\sin\Delta_0+q_+s\cos\Delta_0}
{\cos\Delta_0-q_+s\sin\Delta_0}.
\]

Generically,

\[
q_+\neq q_-,
\]

so

\[
c_+\neq c_-.
\]

Thus one scalar phase-gap coordinate cannot simultaneously flatten both off-diagonal entries while preserving endpoint-transpose symmetry. It can kill the row seen from one side, but not the transpose mate in a structurally valid package.

So the repair cannot be “choose a better scalar \(\Delta\)” unless an additional theorem proves \(q_+=q_-\) to the needed order, which is false away from the diagonal.

---

# 3. Off-diagonal numerator coordinates do cancel the defect

Define

\[
F_+(\Delta,q_+;s)
=
\sin\Delta+q_+s\cos\Delta,
\]

\[
F_-(\Delta,q_-;s)
=
\sin\Delta+q_-s\cos\Delta.
\]

Then set

\[
\Theta_+ := F_+,
\qquad
\Theta_- := F_-.
\]

The off-diagonal entries become

\[
N_{12}=\frac{\Theta_+}{s^2},
\qquad
N_{21}=-\frac{\Theta_-}{s^2}.
\]

Therefore

\[
D^2_{\Theta_+}N_{12}=0,
\qquad
D^2_{\Theta_-}N_{21}=0.
\]

So the dangerous term

\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\]

in \(N_{21}\) is absent in the \(\Theta_-\)-coordinate. Likewise, the transpose partner in \(N_{12}\) is absent in the \(\Theta_+\)-coordinate.

This is not an arbitrary subtraction. It is the normal coordinate in which the off-diagonal entries of the mixed block are their own source coordinates.

---

# 4. Equivalent second-order counterterm

If the draft does not want to change coordinates globally, the same repair can be implemented as a second-order counterterm in the promoted mixed-block Hessian:

\[
\Delta Y_{\eta\eta,\mathrm{off}}^{(2)}
=
-
\left[
D_\Delta^2N_0
\right]_{\eta\eta,\mathrm{off}}.
\]

Entrywise:

\[
(\Delta Y_{\eta\eta,\mathrm{off}}^{(2)})_{12}
=
+
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_+\cos\Delta_0}{s}
\right)\eta_i\eta_j,
\]

\[
(\Delta Y_{\eta\eta,\mathrm{off}}^{(2)})_{21}
=
-
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j.
\]

Then, for the active row,

\[
\Lambda^-_{2,0}
\left[
D_\Delta^2N_0+\Delta Y_{\eta\eta,\mathrm{off}}^{(2)}
\right]_{21}
W_{+,0}
=
0.
\]

Hence

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]

is cancelled.

This is the local counterterm required by the current package failure.

---

# 5. Does this break first-order structure?

No, at least formally.

The correction is second order in the phase-gap source:

\[
\eta_i\eta_j.
\]

So it does not alter first-order source-linearity, tagged pre-whitening additivity, or the first-order source tower.

It also does not affect affine removal: \(\eta\) is already a post-affine/source-motion variable.

It is source-bidegree \((1,1)\) in the mixed middle, so it targets exactly the promoted nonlinear mixed-block carrier that caused the defect.

---

# 6. What must be rechecked

This repair is not free. It changes the corrected package.

The following checks are required.

## A. Endpoint transpose covariance

The counterterm must satisfy

\[
(\Delta Y_{12})^T
=
\Delta Y_{21}
\]

under endpoint swap. The numerator-coordinate version does, because

\[
\Theta_+(h_-,h_+)
\leftrightarrow
\Theta_-(h_+,h_-).
\]

So transpose covariance is plausible.

## B. Gate B homogeneous tower

The correction is quadratic in the mixed-middle source and degree-three only after multiplication by one same-point whitening source. It does not touch the old source-linear homogeneous tower directly, but it changes the actual-source realization theorem.

So the actual-source Gate B theorem must be restated using the off-diagonal normal coordinate.

## C. \(M_A,M_C\) connection closure

The previous \(M_A,M_C\) closure used the actual mixed-block swap identity and source-grade parity. The new off-diagonal variables preserve endpoint swap if \(\Theta_\pm\) are paired correctly, but the \(Y\)-middle parity table must be rechecked in the new coordinate.

## D. Diagonal \(\eta\eta\) terms

The top-row \(S\)-leak came from the \((2,1)\)-entry because \(\Lambda^-_{2,0}=E_{22}\) selected the second row and \(W_{+,0}\) turned that into \(S\). Diagonal \(N_{22}\) terms do not produce the same \(S\)-leak in this row. Still, in non-diagonal baseline patches, diagonal terms can mix; the full finite table must be rechecked.

## E. Package-to-transform \(T\)

The repair is designed to kill the \(S\)-component of this row, so it directly targets \(T\)-horizontal leakage. But it may alter the definition of \(T=v_7/c\) by changing the raw representative. The augmented package must specify whether \(T\) is computed before or after this normal-coordinate correction.

---

# 7. No existing correction in the current package

I do not find an existing mechanism that is equivalent to the numerator-coordinate correction.

- Current \(N^{\corr}\) is written in \(\Delta\), not \(\Theta_\pm\).
- Existing amplitude normalization does not subtract \(D_\Delta^2N\).
- Existing connection correction is post-edge and cannot alter the raw frozen Bottleneck-C carrier.
- Existing quotienting cannot remove \(T\)-visible \(S\)-leakage.

So this would be a genuine package-design modification.

---

# 8. The package-design theorem needed

A theorem-ready formulation:

```latex
\begin{definition}[Off-diagonal phase-gap normal coordinates]
Define
\[
\Theta_+
=
\sin\Delta+q_+s\cos\Delta,
\qquad
\Theta_-
=
\sin\Delta+q_-s\cos\Delta.
\]
The off-diagonal corrected mixed-block entries are written as
\[
N_{12}^{\mathrm{off}}
=
\frac{\Theta_+}{s^2},
\qquad
N_{21}^{\mathrm{off}}
=
-\frac{\Theta_-}{s^2}.
\]
\end{definition}
```

Then:

```latex
\begin{lemma}[Cancellation of the odd \(\eta\eta\) top row]
In off-diagonal phase-gap normal coordinates,
\[
D^2N_{12}^{\mathrm{off}}[\eta_i,\eta_j]=0,
\qquad
D^2N_{21}^{\mathrm{off}}[\eta_i,\eta_j]=0.
\]
Consequently the promoted top-row contribution
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]
from the off-diagonal \(\eta\eta\) Hessian vanishes.
\end{lemma}
```

This would remove the concrete row

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

---

## Verdict

The current package cannot close the odd \(\eta\eta\) top row.

A simple scalar reparametrization of \(\Delta\) cannot repair it because \(N_{12}\) and \(N_{21}\) require different second-order flattening coefficients when \(q_+\neq q_-\).

The principled repair is to switch to **off-diagonal phase-gap normal coordinates**

\[
\Theta_\pm=\sin\Delta+q_\pm s\cos\Delta,
\]

or equivalently add the second-order off-diagonal counterterm

\[
\Delta Y_{\eta\eta,\mathrm{off}}^{(2)}
=
-
[D_\Delta^2N_0]_{\eta\eta,\mathrm{off}}.
\]

This cancels the concrete local defect, but it is a real corrected-package modification. It must be followed by a recheck of Gate B actual-source realization, \(Y\)-middle parity, and the augmented \(T\)-state definition.
## User (2026-04-25 13:59:50)

do this instruction:

Answer: Can the off-diagonal numerator-coordinate package be made coherent without breaking closed gates?
	​
Audit the proposed off-diagonal phase-gap normal coordinates:
\[
\Theta_+=\sin\Delta+q_+s\cos\Delta,
\qquad
\Theta_-=\sin\Delta+q_-s\cos\Delta.
\]

Target:
Determine whether rewriting
\[
N_{12}=\Theta_+/s^2,\qquad N_{21}=-\Theta_-/s^2
\]
can be used as a principled package correction that cancels
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]
without breaking the rest of the proof.

Tasks:
1. Check endpoint-transpose covariance of \(\Theta_\pm\).
2. Recompute the promoted \(\eta\eta\) Hessian in \(\Theta_\pm\)-coordinates.
3. Check whether diagonal entries \(N_{11},N_{22}\) create new order-\(\le7\) fixed-sector defects.
4. Check compatibility with source-bidegree projection and amplitude normalization.
5. Check whether Gate A, Gate B, and \(M_A,M_C\) connection closure survive under this coordinate change.
6. State whether \(T=v_7/c\) is computed before or after this correction and whether the augmented package remains well-defined.

Deliverable:
Either a coherent corrected-package redesign, or a no-go showing that the local obstruction cannot be fixed by \(\Theta_\pm\) coordinates.

## Assistant (2026-04-25 14:01:01)

_Thought for 1m 9s_

## Verdict

\[
\boxed{
\text{The \(\Theta_\pm\) proposal is coherent as an off-diagonal normal-form correction,}
}
\]

but

\[
\boxed{
\text{it is not, by itself, a complete local package repair.}
}
\]

It cancels the concrete off-diagonal odd-\(\eta\eta\) top row

\[
\mathcal E^{2}_{\eta\eta;7,0,0},
\]

and it appears not to disturb the already closed **source-linear** gates. But it changes the actual corrected package and leaves two nontrivial obligations:

1. diagonal \(\eta\eta\) terms in \(N_{11},N_{22}\) must be re-audited;
2. \(T=v_7/c\) must be defined **after** the \(\Theta_\pm\)-normal-form correction, otherwise the old \(T\)-leak remains.

This matches the current proof state: the existing package fails at the odd \(\eta\eta\) row, and \(\Theta_\pm\) is the only plausible package-level repair suggested so far, but it is explicitly not a harmless edit. 

---

# 1. Endpoint-transpose covariance

Define

\[
\Theta_+=\sin\Delta+q_+s\cos\Delta,
\qquad
\Theta_-=\sin\Delta+q_-s\cos\Delta.
\]

Under endpoint swap,

\[
+\leftrightarrow -,
\qquad
s\mapsto -s,
\qquad
\Delta\mapsto -\Delta,
\qquad
q_+\leftrightarrow q_-.
\]

Then

\[
\Theta_+
\mapsto
\sin(-\Delta)+q_-(-s)\cos(-\Delta)
=
-\sin\Delta-q_-s\cos\Delta
=
-\Theta_-.
\]

Likewise,

\[
\Theta_-\mapsto -\Theta_+.
\]

Therefore

\[
N_{12}=\frac{\Theta_+}{s^2}
\]

transforms to

\[
\frac{-\Theta_-}{s^2}
=
N_{21}.
\]

So the off-diagonal numerator coordinates are endpoint-transpose covariant, provided they are paired as

\[
\Theta_+\leftrightarrow-\Theta_-.
\]

This is good.

---

# 2. Promoted \(\eta\eta\) Hessian in \(\Theta_\pm\)-coordinates

In the old \(\Delta\)-coordinate,

\[
N_{12}
=
\frac{\sin\Delta+q_+s\cos\Delta}{s^2},
\]

\[
N_{21}
=
-\frac{\sin\Delta+q_-s\cos\Delta}{s^2}.
\]

The live defect came from

\[
\partial_\Delta^2N_{21}\big|_0
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s},
\]

feeding

\[
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right].
\]

This row is generically nonzero; for \(r_i=r_j=u^2\), \(q_0''=0\), one gets

\[
\nu_{21,7}=-\frac{q_0^3}{216Q^{14}}\neq0,
\]

so the old package cannot prove \(f_{A,Y}=0\) or generic quotient closure. 

In \(\Theta_\pm\)-coordinates,

\[
N_{12}^{\rm off}=\frac{\Theta_+}{s^2},
\qquad
N_{21}^{\rm off}=-\frac{\Theta_-}{s^2}.
\]

These are affine in \(\Theta_\pm\). Hence

\[
D^2_{\Theta_+}N_{12}^{\rm off}=0,
\qquad
D^2_{\Theta_-}N_{21}^{\rm off}=0.
\]

So the pure off-diagonal \(\eta\eta\) Hessian disappears:

\[
\boxed{
\left[D^2N_0\right]_{\eta\eta,\mathrm{off}}^{\Theta}=0.
}
\]

In particular,

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0,\mathrm{off}}=0.
}
\]

So the \(\Theta_\pm\) correction does cancel the specific row that was blocking \(T\)-horizontal and quotient closure.

---

# 3. Diagonal entries \(N_{11},N_{22}\)

The diagonal entries are not automatically repaired by \(\Theta_\pm\):

\[
N_{11}=-\frac{2\sin\Delta}{s},
\]

\[
N_{22}
=
\frac{(q_-+q_+)s\cos\Delta+(2-q_-q_+s^2)\sin\Delta}{2s^3}.
\]

If the package only changes the off-diagonal coordinates, the diagonal entries still have \(\Delta\)-Hessians. Therefore the redesign must audit whether diagonal \(\eta\eta\) terms create new order-\(\le7\) fixed-sector defects.

For the concrete old top row, the dangerous \(S\)-leak came from the \((2,1)\)-entry because

\[
\Lambda^-_{2,0}\propto E_{22},
\qquad
E_{22}J W_{+,0}
\]

has an \(S\)-projection. Diagonal Hessian entries behave differently:

\[
E_{22}
\begin{pmatrix}
* & 0\\
0 & *
\end{pmatrix}
W_{+,0}.
\]

On a diagonal whitening patch, this contributes only diagonally, hence to the \(I/D\) sector, not \(S\). But on a general non-diagonal \(W_{+,0}\), diagonal Hessian terms can still mix into \(S\).

Therefore:

\[
\boxed{
\Theta_\pm\text{ cancels the off-diagonal defect, but does not prove the full local package safe.}
}
\]

A coherent redesign must include a separate diagonal \(\eta\eta\) audit. If diagonal terms are not killed by parity or fixed-sector projection, one may need diagonal normal coordinates as well.

---

# 4. Source-bidegree projection and amplitude normalization

The original defect has source-bidegree \((1,1)\) in the mixed middle and becomes a promoted degree-three carrier after multiplication by one same-point whitening source. That degree-three amplitude pattern is

\[
a_1a_2(a_1+a_2).
\]

On

\[
a_2=-a_1(1+\kappa\delta),
\]

this already supplies the first \(\delta\)-edge:

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2).
\]

So the Bottleneck-C carrier is the frozen coefficient \(E_{A,Y}^{\rm BC}\), not the internal \([z^7\delta^1]\) coefficient. 

The \(\Theta_\pm\) correction is still source-bidegree \((1,1)\) at the mixed-middle Hessian level. It does not violate source-bidegree projection; it removes the offending \((1,1)\) off-diagonal Hessian component before promotion.

Amplitude normalization is also not fundamentally broken. It still sees the same promoted amplitude pattern. The correction changes the matrix coefficient, not the amplitude polynomial.

Thus:

\[
\boxed{
\text{source-bidegree and amplitude bookkeeping can be kept coherent.}
}
\]

But the actual-source realization theorem must be rewritten in the \(\Theta_\pm\)-normal form.

---

# 5. Gate A

Gate A is a source-linear / homogeneous scalar-grade aggregate closure statement. The \(\Theta_\pm\) correction begins at second order in the phase-gap source: it kills a quadratic \(\eta\eta\) Hessian.

Therefore it does not alter the source-linear first-variation tables that Gate A uses.

So, conditional on keeping the same first-order source convention,

\[
\boxed{
\text{Gate A should survive.}
}
\]

It should still be re-stated carefully: Gate A remains closed for the same homogeneous scalar-grade source-linear package, while the \(\Theta_\pm\) normal form is part of the nonlinear actual-source realization layer.

---

# 6. Gate B

Gate B is more delicate.

The formal homogeneous-tower part of Gate B was conditionally closed, but the actual-source upgrade is exactly where the promoted nonlinear mixed-block defect arose. The current construction fails at the odd \(\eta\eta\) row; the \(\Theta_\pm\) normal form removes that row. 

So the redesign helps Gate B, but it also changes the actual-source package. One must reprove:

\[
C_{\mathcal W,\actual}^{\rm raw}
-
C_{\mathcal W,\tower}^{\rm raw}
\]

has no residual promoted nonlinear mixed-block terms through ordinary order \(7\).

In other words:

\[
\boxed{
\text{Gate B does not break automatically, but its actual-source realization must be reproved.}
}
\]

The old actual-source obstruction is removed only if the normal-form correction is part of the definition of the corrected package before forming \(C_{\mathcal W}^{\rm raw}\).

---

# 7. \(M_A,M_C\) connection closure

The \(M_A,M_C\) connection closure relied on the source-linear mixed-block swap/parity structure. The \(\Theta_\pm\) correction does not change the first derivative of the off-diagonal entries if \(\Theta_\pm\) are defined as the off-diagonal numerator variables.

Indeed, linearly,

\[
\delta \Theta_\pm
=
(\cos\Delta_0-q_\pm s\sin\Delta_0)\delta\Delta
+
s\cos\Delta_0\,\delta q_\pm.
\]

Then

\[
\delta N_{12}=\frac{\delta\Theta_+}{s^2}
\]

matches the original first variation of \(N_{12}\), and similarly for \(N_{21}\).

Thus source-linear \(Y\)-middle parity should survive, provided endpoint-transpose covariance

\[
\Theta_+\mapsto-\Theta_-
\]

is built into the convention.

So:

\[
\boxed{
M_A,M_C\text{ should survive, but the \(Y\)-middle parity lemma should be restated in \(\Theta_\pm\)-coordinates.}
}
\]

This is a recheck, not an apparent no-go.

---

# 8. The augmented \(T\)-state

This is the most important bookkeeping point.

The old augmented package uses

\[
T=\frac{v_7}{c}.
\]

The old package fails because the row contributes an \(S\)-component, hence changes \(v_7\), and therefore gives

\[
\partial_\kappa T=-a_1^2\frac{f}{c}\neq0.
\]

With the \(\Theta_\pm\)-normal-form correction, \(v_7\) must be computed **after** the correction.

So the repaired package must define

\[
\boxed{
T^{\Theta}:=\frac{v_7^{\Theta}}{c}.
}
\]

The package-to-transform bridge must then be stated for the corrected finite-\(s\) scalar germ in \(\Theta\)-normal form. If \(T\) is computed before the correction, the old leak remains and the repair is meaningless.

Therefore:

\[
\boxed{
T\text{ is well-defined only as }T^\Theta\text{ after normal-form correction.}
}
\]

This is coherent, but it changes the local package datum.

---

# 9. Is this a harmless coordinate change or a new package?

It is a new package unless one proves that \(\Theta_\pm\) are merely a coordinate chart on the same actual finite-\(s\) transform.

The issue is that \(\Theta_+\) and \(\Theta_-\) are two off-diagonal numerator variables built from one scalar \(\Delta\) and two endpoint slopes \(q_\pm\). They are not an arbitrary pair of independent variables in the original kernel; they obey a compatibility relation.

If the package treats \(\Theta_\pm\) as independent normal coordinates without carrying that relation, it may no longer represent the actual zeta-side mixed block.

Thus the coherent redesign must be formulated as a **normal-form map**:

\[
(q_-,q_+,\Delta)
\longmapsto
(q_-,q_+,\Theta_-,\Theta_+)
\]

with the constraint

\[
\Theta_\pm=\sin\Delta+q_\pm s\cos\Delta.
\]

The corrected package then discards the second-order off-diagonal curvature in these normal coordinates, but it must preserve enough data to reconstruct the finite-\(s\) transform or prove that the discarded curvature is gauge.

That is a genuine new theorem.

---

# 10. Final answer

## What works

\[
\boxed{
\Theta_\pm\text{ are endpoint-transpose covariant.}
}
\]

\[
\boxed{
N_{12}=\Theta_+/s^2,\quad N_{21}=-\Theta_-/s^2
\text{ are affine in }\Theta_\pm.
}
\]

\[
\boxed{
\text{Therefore the offending off-diagonal }\eta\eta\text{ Hessian row is cancelled.}
}
\]

\[
\boxed{
\text{Source-bidegree and amplitude bookkeeping can remain coherent.}
}
\]

\[
\boxed{
\text{Gate A and \(M_A,M_C\) likely survive because their source-linear tables are unchanged.}
}
\]

## What does not automatically work

\[
\boxed{
\text{Diagonal \(\eta\eta\) terms must be re-audited.}
}
\]

\[
\boxed{
\text{Gate B actual-source realization must be reproved.}
}
\]

\[
\boxed{
T\text{ must become }T^\Theta=v_7^\Theta/c\text{, computed after correction.}
}
\]

\[
\boxed{
\Theta_\pm\text{ must be treated as constrained normal coordinates, not free independent variables.}
}
\]

---

## Package-redesign statement

A coherent corrected-package redesign is possible only in this conditional form:

```latex
\begin{definition}[Off-diagonal numerator normal form]
Set
\[
\Theta_+=\sin\Delta+q_+s\cos\Delta,\qquad
\Theta_-=\sin\Delta+q_-s\cos\Delta.
\]
The off-diagonal mixed-block entries are represented in the normal form
\[
N_{12}^{\Theta}=\Theta_+/s^2,\qquad
N_{21}^{\Theta}=-\Theta_-/s^2,
\]
with the endpoint-swap convention
\[
\Theta_+\longleftrightarrow-\Theta_-.
\]
The variables \(\Theta_\pm\) are constrained normal coordinates induced by
\((q_-,q_+,\Delta)\), not independent source variables.
\end{definition}
```

Then:

```latex
\begin{lemma}[Off-diagonal odd-\(\eta\eta\) cancellation]
In the off-diagonal numerator normal form,
\[
D^2_{\Theta_\pm}N_{12}^{\Theta}
=
D^2_{\Theta_\pm}N_{21}^{\Theta}
=
0.
\]
Consequently the off-diagonal contribution to
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]
vanishes.
\end{lemma}
```

But the redesign also needs the following theorem:

```latex
\begin{theorem}[Coherence of the \(\Theta\)-normal corrected package]
The off-diagonal numerator normal form preserves:
\[
\text{Gate A aggregate closure,}
\]
\[
\text{Gate B actual-source realization through ordinary order }7,
\]
\[
M_A,M_C\text{ connection closure,}
\]
and defines the augmented hidden state by
\[
T^\Theta=\frac{v_7^\Theta}{c}.
\]
Moreover, all remaining diagonal \(\eta\eta\) terms are either fixed-sector
invisible, quotient-line invisible and \(T^\Theta\)-invisible, or cancelled
by the corrected package.
\end{theorem}
```

---

## Bottom line

\[
\boxed{
\text{The \(\Theta_\pm\) proposal can coherently cancel the known off-diagonal local defect.}
}
\]

But:

\[
\boxed{
\text{It is a real package redesign, not a harmless coordinate relabeling.}
}
\]

It does not break the closed source-linear gates on its face, but it forces a new proof obligation:

\[
\boxed{
\text{Gate B actual-source realization and \(T^\Theta\)-state coherence must be reproved in the \(\Theta\)-normal package.}
}
\]

So the final answer is:

\[
\boxed{
\text{yes, conditionally coherent as a package redesign;}
}
\]

\[
\boxed{
\text{no, not yet a completed repair until the diagonal terms and \(T^\Theta\) bridge are re-audited.}
}
\]
## User (2026-04-25 15:33:19)

Here is the latest paper draft. Please review and ensure we've captured everything in your push, including key structural findings, derivations, goodies, negative results and no-gos, etc. Please also check for any stale items. Please give exact latex insertions/edits and exactly where to make them.

## Assistant (2026-04-25 15:33:21)

I’ll audit the latest draft against the local-package push: the odd \(\eta\eta\) row, the \(\Theta_\pm\) normal-form proposal, finite-core dependency, and interaction no-go status. I’ll focus on mathematical/staleness edits, not prose polish.

_Thought for 1m 43s_

I reviewed `proof_of_rh(445).tex`. Most of the push is now captured, including the frozen Bottleneck-C bookkeeping, the \(\Theta_\pm\) no-go, sampled finite-core non-concentration, and the \(dd\)-interaction feature-balance obstruction.

The main stale item is that the draft still treats \(E_{A,Y}^{\mathrm{BC}}\) primarily as an unevaluated finite table in a few places, while the latest local work has sharpened the first live row to the concrete odd-\(\eta\eta\) row \((a,r,g,b)=(2,0,7,0)\), with an explicit \(S\)-visible coefficient. Also, the old active source-index shorthand \(a\in\{1,5\}\) is stale in the \(E_{A,Y}^{\mathrm{BC}}\) table; the latest finite Fréchet normalization uses \(a=2,\ldots,6\), and the lead row uses \(a=2\). The latest agent summary also explicitly identifies \(\mathcal E^2_{\eta\eta;7,0,0}\), \(\nu_{21,7}\), and the \(\Theta_\pm\)-normal repair as the active local issue. turn87file11turn87file14

Below are the exact edits I recommend.

---

## Edit 1 — fix stale source-index notation in the first \(E_{A,Y}^{\mathrm{BC}}\) table

**Where:** In `\begin{remark}[Executable table for \(E_{A,Y}^{\mathrm{BC}}\)]`, label:

```latex
\label{rem:executable-table-eay-bc}
```

**Replace:**

```latex
where
\[
a\in\{1,5\},\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\]
```

**with:**

```latex
where \(\mathcal A_{\sp}\) denotes the active same-point source-index set in
the finite Fréchet primitive table:
\[
a\in\mathcal A_{\sp},\qquad
\mathcal A_{\sp}\subset\{2,\ldots,6\},\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]
The concrete leading odd-\(\eta\eta\) row isolated below uses \(a=2\).
```

**Then replace:**

```latex
\sum_{a\in\{1,5\}}
```

**with:**

```latex
\sum_{a\in\mathcal A_{\sp}}
```

in the displayed formula immediately below.

---

## Edit 2 — fix stale source-index notation in the first status remark

**Where:** In `\begin{remark}[Status of \(E_{A,Y}^{\mathrm{BC}}\)]`, label:

```latex
\label{rem:status-eay-bc}
```

**Replace:**

```latex
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
```

**with:**

```latex
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\mathcal A_{\sp},\quad 2\le k\le9.
```

**Then replace the final sentence:**

```latex
Thus \(E_{A,Y}^{\mathrm{BC}}\) remains the first unresolved local
actual-source/Bottleneck-C obstruction.
```

**with:**

```latex
The broad finite table remains relevant for possible aggregate cancellation.
However, the first concrete live row is now the odd-\(\eta\eta\) top row
\[
(a,r,g,b)=(2,0,7,0),
\]
recorded in Lemma~\ref{lem:odd-etaeta-top-row-survivor}.  Thus the local
Bottleneck-C obstruction has sharpened from an unevaluated table to a
specific row-level source-jet identity, together with the possibility of
aggregate cancellation against other rows.
```

---

## Edit 3 — insert the concrete odd-\(\eta\eta\) survivor lemma

**Where:** Insert immediately after:

```latex
\end{lemma}
```

for

```latex
\begin{lemma}[Scalar tests for the frozen promoted mixed-block coefficient]
\label{lem:scalar-tests-eay-bc}
```

and before the next remark.

**Insert:**

```latex
\begin{lemma}[Concrete odd-\(\eta\eta\) top-row survivor]
\label{lem:odd-etaeta-top-row-survivor}
Consider the \(\eta\eta\)-Hessian contribution from the \((2,1)\)-entry of
the corrected mixed block:
\[
H_{21}^{\eta\eta}
=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j .
\]
For the finite Fréchet source index \(a=2\), one has
\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}
\]
on a diagonal good patch.  If
\[
W_{+,0}=\begin{pmatrix}u&0\\0&v\end{pmatrix},
\]
then the top row
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
:=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[H_{21}^{\eta\eta}]_7
W_{+,0}
\right)
\]
has fixed-sector \(S\)-coefficient
\[
f_{\eta\eta}^{\top}
=
-\frac{u}{24\pi q^3}\nu_{21,7},
\]
where
\[
\nu_{21,7}
:=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
\]
Consequently, if \(\nu_{21,7}\ne0\), then the row is \(\Phi_K\)-visible and
produces a nonzero \(T\)-slope.
\end{lemma}

\begin{proof}
The identity for \(\Lambda^-_{2,0}\) follows from the finite Fréchet
primitive
\[
X^-_{2,0}=\frac{1}{24\pi}(I-D)=\frac{1}{12\pi}E_{22}.
\]
Solving the zeroth Sylvester equation gives
\[
S^-_{2,0}=\frac{1}{24\pi q}E_{22},
\]
and hence
\[
\Lambda^-_{2,0}
=
-W_{-,0}S^-_{2,0}W_{-,0}
=
-\frac{1}{24\pi q^3}E_{22}
\]
on a diagonal good patch.

Since
\[
E_{22}
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}
W_{+,0}
=
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix},
\]
symmetrization gives
\[
\operatorname{Sym}
\begin{pmatrix}
0&0\\
u&0
\end{pmatrix}
=
uS.
\]
The asserted \(S\)-coefficient follows.
\end{proof}
```

This captures the key structural finding: the local obstruction is not just “a missing table”; it is the explicit \(S\)-visible row \(\mathcal E^2_{\eta\eta;7,0,0}\). The existing summary identifies this as the current lead local blocker. turn87file17

---

## Edit 4 — insert the explicit \(\nu_{21,7}\) expansion and the \(u^2\) no-go model

**Where:** Immediately after Lemma `\ref{lem:odd-etaeta-top-row-survivor}`.

**Insert:**

```latex
\begin{lemma}[Expansion of the odd-\(\eta\eta\) top-row scalar]
\label{lem:nu-21-7-expansion}
Assume the favorable phase-gap integral realization
\[
\eta_i(s)=\int_{-s/2}^{s/2}r_i(u)\,du
\]
with post-affine source field
\[
r_i(u)=\rho_{i,2}u^2+\rho_{i,4}u^4+O(u^5).
\]
Then
\[
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]
In particular, for the homogeneous source \(r_i=r_j=u^2\) and \(q_0''=0\),
\[
\nu_{21,7}=-\frac{q_0^3}{216Q^{14}},
\]
which is nonzero on a good phase patch \(q_0\ne0\).
\end{lemma}

\begin{proof}
The integral realization gives
\[
\eta_i(s)=\frac{\rho_{i,2}}{12}s^3+\frac{\rho_{i,4}}{80}s^5+O(s^7).
\]
Writing \(s=z/Q^2\), one has
\[
\eta_i(z)
=
\alpha_{i,3}z^3+\alpha_{i,5}z^5+O(z^7),
\qquad
\alpha_{i,3}=\frac{\rho_{i,2}}{12Q^6},
\quad
\alpha_{i,5}=\frac{\rho_{i,4}}{80Q^{10}}.
\]
Also
\[
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
=
\frac{2q_0}{s}
+
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)s
+O(s^2)
\]
after the phase-gap expansion.  Extracting the \(z^7\)-coefficient gives the
displayed formula.
\end{proof}
```

---

## Edit 5 — add a concise “local binary state” remark

**Where:** After Lemma `\ref{lem:nu-21-7-expansion}`.

**Insert:**

```latex
\begin{remark}[Binary local package state]
\label{rem:binary-local-package-state}
The current corrected local package therefore has only two possible routes for
this row:
\[
\nu_{21,7}=0
\]
by a zeta-specific source-jet identity, or a package correction/counterterm
which cancels
\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]
The existing mechanisms do not supply such a cancellation: source-bidegree
projection keeps the promoted degree-three carrier, amplitude normalization
only rescales it, midpoint trivialization is invertible on a good patch,
fixed-sector quotienting is insufficient because the transform-safe condition
requires \(f=0\), and connection correction is post-edge and cannot remove
the raw frozen coefficient.
\end{remark}
```

This captures the no-go/goodie from the latest package-design push: the current package fails locally unless repaired, and \(\Theta_\pm\) is a proposed package-level repair rather than an existing theorem. turn87file5

---

## Edit 6 — fix the duplicate current-section table source-index notation

**Where:** In the later status section, inside:

```latex
\begin{remark}[Executable table for \(E_{A,Y}^{\mathrm{BC}}\) (current section)]
\label{rem:executable-table-eay-bc-current}
```

**Replace:**

```latex
where
\[
a\in\{1,5\},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\]
```

**with:**

```latex
where
\[
a\in\mathcal A_{\sp},
\qquad
\mathcal A_{\sp}\subset\{2,\ldots,6\},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]
The concrete top-row obstruction isolated in
Lemma~\ref{lem:odd-etaeta-top-row-survivor} uses \(a=2\).
```

**Then replace:**

```latex
\sum_{a\in\{1,5\}}
```

**with:**

```latex
\sum_{a\in\mathcal A_{\sp}}
```

in the aggregation formula in that same remark.

---

## Edit 7 — revise the later status remark so it does not understate the row-level obstruction

**Where:** In:

```latex
\begin{remark}[Status of the frozen promoted mixed-block coefficient (current section)]
\label{rem:status-eay-bc-current}
```

**Replace the whole final paragraph starting with:**

```latex
At present no available symmetry forces
```

through:

```latex
Thus \(E_{A,Y}^{\mathrm{BC}}\) remains the first unresolved local
actual-source/Bottleneck~C coefficient.
```

**with:**

```latex
At present no available symmetry forces the scalar tests
\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\qquad
f_{A,Y}=0.
\]
Moreover, Lemma~\ref{lem:odd-etaeta-top-row-survivor} gives a concrete
row-level survivor:
\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]
Thus the local obstruction is sharper than an unevaluated table.  The broad
table remains relevant for aggregate cancellation, but the first live local
task is cancellation of the odd-\(\eta\eta\) top row, equivalently the
source-jet identity
\[
\nu_{21,7}=0
\]
or a correction term cancelling that row.
```

---

## Edit 8 — clarify the \(\Theta_\pm\) subsection title and scope

The current subsection is already strong and useful, but I would make the title less ambiguous. It is not saying \(\Theta_\pm\) is algebraically useless; it is saying \(\Theta_\pm\) cannot be treated as a transform-faithful free normal-form repair unless the physical residual is carried back.

**Where:** Change:

```latex
\subsection{No-go for the \(\Theta_\pm\)-normal repair}
\label{subsec:no-go-theta-normal-repair}
```

**to:**

```latex
\subsection{No-go for a transform-faithful free \(\Theta_\pm\)-normal repair}
\label{subsec:no-go-theta-normal-repair}
```

**Then, after the paragraph ending:**

```latex
It does not, however, close the physical Bottleneck~C obstruction.
```

**insert:**

```latex
The distinction is important.  As a formal normal coordinate, \(\Theta_\pm\)
makes the off-diagonal entries affine.  As a physical coordinate induced from
\((q_-,q_+,\Delta)\), however, \(\Theta_\pm\) is constrained and its
source-curvature must either remain in the raw package or be carried by the
hidden physical readout.  The following no-go concerns the latter,
transform-faithful interpretation.
```

This preserves the nuance from the package-design audit: \(\Theta_\pm\) can cancel the formal off-diagonal Hessian, but only by moving the physical residual unless a new identity is added. turn87file14

---

## Edit 9 — fix the \(\kappa\)-chart notation in the \(\Theta_\pm\) no-go proof

**Where:** In the proof of:

```latex
\begin{proposition}[Physical edge obstruction survives in a good-patch model]
\label{prop:theta-physical-edge-obstruction-good-patch}
```

The proof currently uses:

```latex
Along
\[
a_2=-a_1+\kappa
\]
one has
...
```

This is potentially stale/confusing because everywhere else the Bottleneck-C chart is

\[
a_2=-a_1(1+\kappa\delta),
\]

and the frozen coefficient is obtained after the \(\delta\)-edge is supplied by the amplitude.

**Replace that block with:**

```latex
After extracting the frozen Bottleneck-C matrix coefficient, the remaining
amplitude derivative is the derivative of
\[
a_1a_2(a_1+a_2)
\]
in the transverse amplitude direction at the balanced point \(a_2=-a_1\).
Equivalently, using the local edge coordinate \(\kappa_{\amp}=a_2+a_1\),
\[
a_1a_2(a_1+a_2)
=
a_1(-a_1+\kappa_{\amp})\kappa_{\amp}
=
-a_1^2\kappa_{\amp}+O(\kappa_{\amp}^2),
\]
so
\[
\left.
\partial_{\kappa_{\amp}}
\bigl(a_1a_2(a_1+a_2)\bigr)
\right|_{\kappa_{\amp}=0}
=
-a_1^2.
\]
This is the same scalar edge factor obtained from the collision chart
\(a_2=-a_1(1+\kappa\delta)\) after the first \(\delta\)-edge has been
factored into the frozen Bottleneck-C coefficient.
```

This removes a possible inconsistency between the amplitude chart used in the proof and the rest of the draft.

---

## Edit 10 — finite-core and interaction sections are mostly captured; no major insertion needed

The latest draft’s `\subsection{Finite-core sampled vector non-concentration}` already captures the dependency theorem, the bad branch \(\mathcal N_k^{\rm align}\), and the lower-transfer implication. That matches the latest finite-core status: the proof now needs a named sampled vector non-concentration input, not more finite determinacy work. turn87file15

The `\subsection{\(dd\)-interaction feature-balance obstruction}` also captures the main interaction no-go: the \(dd\)-interaction requires feature balance, conditional spectral positivity, or incidence containment; ordinary amplitude balance and rank-one locking are insufficient. turn87file6

I would only add one sentence to the end of `\begin{remark}[Needed input for the \(dd\)-interaction branch]`:

```latex
In particular, pair-like positivity of the one-body kernel is not by itself a
centered-kernel spectral theorem for the covariance-weighted \(dd\)-interaction.
```

This guards against a common stale inference from earlier drafts.

---

## Summary of what is captured vs. stale

**Captured well:**

- Frozen Bottleneck-C coefficient, not internal \([z^7\delta^1]\).
- The split between quotient test \(e v_5-u_5f=0\) and transform-safe test \(f=0\).
- \(\Theta_\pm\) no-go as a physical/readout obstruction.
- Finite-core sampled vector non-concentration dependency.
- \(dd\)-interaction feature-balance/spectral rigidity dependency.

**Needs correction:**

- Replace stale \(a\in\{1,5\}\) with \(\mathcal A_{\sp}\subset\{2,\ldots,6\}\), and explicitly mark the leading row as \(a=2\).
- Add the explicit row-level obstruction \(\mathcal E^2_{\eta\eta;7,0,0}\), \(\nu_{21,7}\), and the \(u^2\) good-patch no-go.
- Clarify that the broad \(E_{A,Y}^{\mathrm{BC}}\) table is no longer merely “missing”; the first live local obstruction is the concrete odd-\(\eta\eta\) top row.
- Clarify the \(\Theta_\pm\) subsection title and the amplitude edge chart notation.
## User (2026-04-25 15:52:32)

You are Local Agent A. Attached the latest paper draft, plus a background summary and the next attack instructions--do your attack.

## Assistant (2026-04-25 15:53:02)

_Thought for 28s_

## Local Agent A attack — aggregate cancellation does **not** remove \(\mathcal E^{2}_{\eta\eta;7,0,0}\)

I attacked the concrete row-level obstruction by asking whether any other active frozen Bottleneck-C row can cancel its \(S\)-coefficient.

The answer is negative in a good-patch model. The row

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]

has an isolated \(S\)-visible contribution that no other active row is structurally forced to cancel. This gives a concrete countermodel with

\[
f_{A,Y}\neq 0,
\qquad
\partial_\kappa T\neq0,
\]

and, on a generic \(u_5\neq0\) patch,

\[
Q_{A,Y}\neq0.
\]

This is exactly the local-agent target: determine whether the concrete odd-\(\eta\eta\) top row is cancelled by any other frozen Bottleneck-C row. The prompt identifies this row as the highest-priority local obstruction and gives its \(S\)-coefficient
\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7},
\]
with \(\nu_{21,7}\neq0\) in the homogeneous \(r(u)=u^2\), \(q_0''=0\) good-patch test. 

---

# 1. The active row

The row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]_7
W_{+,0}
\right).
\]

The actual finite Fréchet coefficient is

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]

On a diagonal right-whitening patch

\[
W_{+,0}=\operatorname{diag}(u,v),
\qquad u,v\neq0,
\]

the \((2,1)\)-entry of the \(\eta\eta\)-Hessian gives

\[
\operatorname{Sym}(E_{22}JW_{+,0})=uS.
\]

Hence

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
-\frac{u}{24\pi q^3}\nu_{21,7}S
+
(\text{diagonal contributions}),
\]

where

\[
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
\]

Thus the relevant \(S\)-coefficient is

\[
\boxed{
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
}
\]

---

# 2. Rows with the same source-jet profile

The source-jet profile of this row is:

\[
\eta_i\eta_j,
\qquad
[z^7],
\qquad
a=2,\quad r=0,\quad g=7,\quad b=0.
\]

Because

\[
r+b+g=7,
\]

if \(g=7\), then necessarily

\[
r=0,\qquad b=0.
\]

So the only rows with the same \(g=7\) top profile are:

\[
\mathcal E^{a}_{\eta\eta;7,0,0}
\]

for whatever finite Fréchet source indices \(a\) have nonzero \(\Lambda^-_{a,0}\).

But in the actual primitive table, the only zeroth source primitive among the low active indices is

\[
X^-_{2,0}\propto E_{22}.
\]

The other source indices begin at higher \(z\)-order or in off-diagonal rows. Therefore they do **not** produce a competing \((a,r,g,b)=(a,0,7,0)\) top-row term with the same \(\eta_i\eta_j\) profile.

So the same-profile top row is isolated at \(a=2\).

---

# 3. Could other \(\eta\eta\) entries cancel it?

The full \(\eta\eta\)-Hessian includes diagonal entries and both off-diagonal entries. For the active row, left multiplication by

\[
\Lambda^-_{2,0}\propto E_{22}
\]

selects the **second row** of the Hessian. Thus only \(H_{21}\) and \(H_{22}\) matter.

The \(H_{21}\) entry gives the \(S\)-component above.

The \(H_{22}\) entry is diagonal. On the diagonal right-whitening patch,

\[
E_{22}H_{22}W_{+,0}
\]

is diagonal, so after symmetrization it contributes only to the diagonal sector. It cannot cancel an \(S\)-component.

The \(H_{11}\) and \(H_{12}\) entries do not enter this row at all, because \(E_{22}\) kills the first row before multiplication by \(W_{+,0}\).

Therefore, within the same \(\eta\eta\) top row, the only \(S\)-visible part is the \(H_{21}\) component. There is no internal Hessian cancellation for its \(S\)-coefficient.

---

# 4. Could \(dd\) or \(d\eta+\eta d\) rows cancel it?

No structurally.

The row’s source monomial is

\[
\eta_i\eta_j.
\]

The \(dd\)-rows contain only

\[
d_i d_j.
\]

The \(d\eta+\eta d\)-rows contain

\[
d_i\eta_j+\eta_i d_j.
\]

These are distinct source monomial families. A cancellation between

\[
\eta_i\eta_j
\]

and

\[
d_i d_j
\quad\text{or}\quad
d_i\eta_j+\eta_i d_j
\]

would require a source-model identity relating \(d\)-jets and \(\eta\)-jets. No such identity is part of the existing package. Endpoint-diagonal realization, even if proved, relates endpoint copies of \(\eta\); it does not identify \(\eta\eta\) with \(dd\) or \(d\eta\).

Thus cancellation against \(dd\) or \(d\eta+\eta d\) would be accidental parameter cancellation, not a structural identity.

---

# 5. Good-patch countermodel isolating the row

Take a good patch with:

\[
W_{+,0}=\operatorname{diag}(u,v),
\qquad u\neq0,
\]

\[
\Lambda^-_{2,0}=-\frac{1}{24\pi q^3}E_{22},
\qquad q\neq0.
\]

Use the homogeneous source test:

\[
r_i(u)=r_j(u)=u^2,
\qquad q_0''=0.
\]

Then

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]

which is nonzero when

\[
q_0\neq0.
\]

Set all other independent source monomial families to zero:

\[
dd=0,
\qquad
d\eta+\eta d=0,
\]

and retain only this \(\eta\eta\) top source component. This respects the row-level formal package: the \(\eta\eta\) Hessian is independent as a second \(\Delta\)-source variation.

Then the row gives

\[
E_{A,Y}^{\rm BC}
\supset
-\frac{u}{24\pi q^3}\nu_{21,7}S.
\]

Hence

\[
f_{A,Y}
=
-\frac{u}{24\pi q^3}\nu_{21,7}
=
\frac{u q_0^3}{5184\pi q^3Q^{14}}
\neq0.
\]

Therefore

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
\neq0.
\]

And if

\[
u_5\neq0,
\]

then

\[
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y}
=
-u_5f_{A,Y}
\neq0
\]

in this pure \(S\)-row submodel.

---

# 6. Why this is structural, not just a missing calculation

The countermodel uses:

- the actual active finite Fréchet index \(a=2\);
- the actual zeroth coefficient \(\Lambda^-_{2,0}\propto E_{22}\);
- the actual \((2,1)\)-entry of the \(\eta\eta\)-Hessian;
- the frozen Bottleneck-C coefficient, not the internal \([z^7\delta^1]\) edge;
- a homogeneous post-affine source \(r(u)=u^2\), which is allowed by affine removal.

The only way to kill it is one of the following new inputs:

\[
\nu_{21,7}=0
\]

for the actual zeta source class;

or

\[
\sum_{\mathrm{top}\ \eta\eta} f_{\eta\eta}^{\rm top}=0
\]

by an explicit same-source-family aggregate identity;

or a physical correction term cancelling this \(S\)-row.

None follows from:

- endpoint swap;
- fixed-sector symmetrization;
- source-bidegree projection;
- amplitude normalization;
- midpoint trivialization;
- post-edge connection correction;
- quotienting, since \(T\)-horizontal closure requires \(f=0\).

---

# 7. Row-level no-go theorem

A theorem-ready no-go statement is:

```latex
\begin{lemma}[Row-level survival of the odd-\(\eta\eta\) top term]
In the current corrected package, the row
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
\]
is not structurally cancelled by any other frozen Bottleneck-C row.  On a
good patch with \(q_0\ne0\), \(q_0''=0\), \(u\ne0\), and \(q\ne0\), the
homogeneous source \(r_i=r_j=u^2\) gives
\[
f_{A,Y}
=
\frac{u q_0^3}{5184\pi q^3Q^{14}}
\ne0.
\]
Consequently
\[
\partial_\kappa T=-a_1^2 f_{A,Y}/c\ne0,
\]
and, on a generic \(u_5\ne0\) quotient patch,
\[
Q_{A,Y}=-u_5f_{A,Y}\ne0.
\]
\end{lemma}
```

---

## Verdict

No structural aggregate cancellation is available in the current package.

The concrete row

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
}
\]

survives in a good-patch model and gives

\[
\boxed{
f_{A,Y}\neq0.
}
\]

Therefore the current local Bottleneck-C package fails unless the paper adds a new zeta-specific source identity, proves an explicit same-source-family aggregate cancellation, or introduces a genuinely physical correction term.
## User (2026-04-25 16:20:33)

Do your specific instruction

## Assistant (2026-04-25 16:20:45)

I’ll run the admissibility audit as Local Agent A: whether the homogeneous post-affine source \(r(u)=u^2,\ q_0''=0,\ q_0\ne0\) is actually allowed by the draft’s source definitions, not merely “not forbidden.”

_Thought for 1m 17s_

## Local Agent A — admissibility verdict

**Verdict:** the homogeneous good-patch model

\[
r_i(u)=r_j(u)=u^2,\qquad q_0''=0,\qquad q_0\neq0
\]

is **admissible in the draft’s local formal corrected-source category after affine removal**, but the latest draft does **not** prove that it is literally realized by an actual exterior zeta zero pair. Therefore:

\[
\boxed{
\text{The model is a valid local-source countermodel to the current package axioms.}
}
\]

\[
\boxed{
\text{It is not yet a certified literal zeta-source counterexample.}
}
\]

That is enough to kill the universal formal claim

\[
\nu_{21,7}=0
\]

from the currently stated source normalizations. To exclude this model, the paper needs an additional **actual zeta source-realization restriction** relating

\[
q_0,\quad q_0'',\quad \rho_{i,2},\quad \rho_{i,4}.
\]

No such restriction is currently stated.

---

# 1. What the draft’s source definitions actually impose

The draft defines a one-pair perturbation by taking a one-pair phase-derivative contribution \(f_\rho(t)\) and subtracting its midpoint affine jet:

\[
r_\rho(t)=f_\rho(t)-f_\rho(m)-f_\rho'(m)(t-m).
\]

It then defines endpoint source variables

\[
d_\pm(z)=r_\rho(t_\pm),\qquad
e_\pm(z)=r_\rho'(t_\pm),\qquad
g_\pm(z)=r_\rho''(t_\pm),
\]

and the phase-gap source variable

\[
\eta(z)=\int_{t_+}^{t_-}r_\rho(u)\,du.
\]

The resulting kernels satisfy

\[
d_\pm(z)=\frac{z^2}{Q^4}U_\pm(z),\quad
e_\pm(z)=\frac{z}{Q^2}E_\pm(z),\quad
g_\pm(z)=G_\pm(z),\quad
\eta(z)=\frac{z^3}{Q^6}V(z).
\]

So affine removal imposes only

\[
r_\rho(m)=0,\qquad r_\rho'(m)=0.
\]

It does **not** impose a relation between \(r_\rho^{(2)}(m)\) and \(r_\rho^{(4)}(m)\).

The tagged two-atom source block then substitutes the source kernels additively into

\[
q_{\pm},\quad q'_{\pm},\quad q''_{\pm},\quad \Delta,
\]

with

\[
\eta^{(2)}=\tau_1a_1\eta_{h_1}+\tau_2a_2\eta_{h_2}.
\]

This confirms that \(\eta\) is built from the residual source integral, but it does not add a fourth-order/two-jet locking law. The current handover also identifies the same source setup and the odd-\(\eta\eta\) row as the concrete local obstruction. 

---

# 2. The homogeneous model satisfies the stated local source constraints

Take

\[
r(u)=u^2.
\]

Then

\[
r(0)=0,\qquad r'(0)=0,
\]

so affine removal is respected.

The phase-gap integral is

\[
\eta(s)=\int_{-s/2}^{s/2}u^2\,du=\frac{s^3}{12}.
\]

Thus in the notation

\[
r(u)=\rho_2u^2+\rho_4u^4+\cdots,
\]

we have

\[
\rho_2=1,\qquad \rho_4=0.
\]

This obeys the draft’s post-affine source normal form. It also obeys endpoint symmetry and source-grade parity.

The current local obstruction is

\[
\nu_{21,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right].
\]

Under the favorable phase-gap integral model,

\[
\nu_{21,7}
=
\frac{1}{Q^{14}}
\left[
\frac{q_0}{480}
(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2})
+
\frac{1}{144}
\left(
\frac{q_0''}{6}-\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]

For \(r_i=r_j=u^2\), \(q_0''=0\), this gives

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]

which is nonzero on a good phase patch \(q_0\neq0\). This is the exact local survivor recorded in the handover. turn95file5

---

# 3. The draft does not force the locking law

The locking law needed to kill the row is

\[
\frac{\rho_{i,4}}{\rho_{i,2}}
=
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}.
\]

For \(r=u^2\),

\[
\frac{\rho_4}{\rho_2}=0.
\]

If also \(q_0''=0\), the locking law would require

\[
0=\frac{10q_0^2}{9}.
\]

That contradicts the good-patch condition

\[
q_0\neq0.
\]

So if the draft imposed the locking law, it would exclude the homogeneous model. But I find no such relation in the draft’s stated source machinery:

- affine removal only kills constant and affine source modes;
- endpoint normalization controls endpoint symmetry/parity, not \(\rho_4/\rho_2\);
- same-scale normalization controls scale/good-patch behavior, not a fourth/second derivative locking law;
- source-grade parity organizes signs by grade, not baseline/source jet ratios;
- phase-gap geometry gives \(\eta=\int r\), but that only sets the parity of \(\eta\)-jets and still leaves \(\rho_2,\rho_4\) free.

Thus the current definitions do not exclude

\[
r=u^2,\qquad q_0''=0,\qquad q_0\neq0.
\]

The handover explicitly frames this as the decisive audit: unless the homogeneous good-patch model is inadmissible or the frozen row table is incomplete, the local package has a hard obstruction. 

---

# 4. Literal zeta-source versus formal source-category admissibility

There is one important qualification.

The draft defines \(r_\rho\) as coming from a one-pair phase-derivative contribution \(f_\rho\). It does **not** explicitly prove that every post-affine polynomial germ \(r(u)\) is realized by some actual exterior zeta zero pair. Therefore, the homogeneous model

\[
r(u)=u^2
\]

should be read as:

\[
\boxed{
\text{admissible in the local formal source category stated by the current package,}
}
\]

not as:

\[
\boxed{
\text{proved to occur as an actual individual zeta zero-pair source.}
}
\]

This distinction matters. The local countermodel refutes the claim that the current package formalism itself forces

\[
\nu_{21,7}=0.
\]

To save the proof, the draft would need a new theorem saying the actual zeta source class is strictly smaller than the formal post-affine holomorphic source category and satisfies the locking law above or an equivalent cancellation identity.

No such theorem is currently present.

---

# 5. Local consequence

Because the homogeneous model is admissible under the currently stated local source constraints, the universal source-jet identity

\[
\nu_{21,7}=0
\]

is not derivable.

For the concrete row,

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]

and on a diagonal right-whitening patch,

\[
W_{+,0}=\operatorname{diag}(u,v),
\]

the \(S\)-coefficient is

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

For \(r_i=r_j=u^2,\ q_0''=0\),

\[
f_{\eta\eta}^{\rm top}
=
\frac{u q_0^3}{5184\pi q^3Q^{14}},
\]

which is nonzero on a good patch

\[
u q_0 q\neq0.
\]

Thus

\[
\partial_\kappa T=-a_1^2\frac{f_{\eta\eta}^{\rm top}}{c}\neq0.
\]

On a generic \(u_5\neq0\) patch, the quotient determinant also fails:

\[
Q_{A,Y}=-u_5f_{\eta\eta}^{\rm top}\neq0.
\]

This matches the coordinator’s current assessment: if the homogeneous good-patch model is admissible and the row table is complete, the current local package has a hard obstruction. 

---

# 6. Final admissibility verdict

\[
\boxed{
r_i=r_j=u^2,\quad q_0''=0,\quad q_0\neq0
\text{ is admissible under the draft’s stated formal local source constraints.}
}
\]

\[
\boxed{
\text{The draft does not state an actual-zeta locking law excluding it.}
}
\]

\[
\boxed{
\text{Therefore this model kills the universal route }\nu_{21,7}=0.
}
\]

The exact missing theorem, if the proof is to be rescued without changing the package, is:

```latex
\begin{theorem}[Actual zeta source-jet locking]
For every actual zeta-side promoted source field \(r_i\), after affine removal,
\[
\frac{\rho_{i,4}}{\rho_{i,2}}
=
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}.
\]
Equivalently, for every active pair \(i,j\),
\[
\nu_{21,7}=0.
\]
\end{theorem}
```

Without that theorem, or a physical correction term cancelling the row, the current local Bottleneck-C package does not close.
