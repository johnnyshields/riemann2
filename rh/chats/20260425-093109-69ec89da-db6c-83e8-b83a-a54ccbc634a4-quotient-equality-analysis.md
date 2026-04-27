# Quotient Equality Analysis

- Source: https://chatgpt.com/c/69ec89da-db6c-83e8-b83a-a54ccbc634a4
- Created: 2026-04-25 09:31:09 UTC
- Default model: gpt-5-5-thinking

---

## User (2026-04-25 09:31:06)

YOUR TASK: You are Agent 4

Agent 4 — hidden-state / ΦK-visible bridge

The existing prompt is good, but it should demand a theorem-or-counterexample.

You are attacking the package-to-transform hidden-state bridge.

Work only from the latest paper draft.

Target:
Determine whether quotient package equality implies equality of the first \(\Phi_K\)-visible corrected odd coefficient entering \(\Xi_\zeta^{(N)}\).

Central issue:
The reduced package forgets
\[
A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f},
\]
but
\[
\Phi_K(A_5^{\mathfrak f})=2v_5.
\]
Therefore quotient equality does not automatically imply hidden-state equality.

Tasks:
1. Define the minimal state needed to determine the first \(\Phi_K\)-visible corrected odd coefficient.
2. Decide whether this state is determined by:
   (a) the quotient class,
   (b) the quotient class plus \(A_5^{\mathfrak f}\),
   (c) the diagnostic tuple \(\widetilde\Psi_{\min}\),
   (d) additional raw septic representative data.
3. Either prove state-locality modulo \(\ker\Phi_K\), or construct a formal countermodel showing why the current reduced data are insufficient.
4. Identify the precise extra theorem needed to make quotient closure feed the two-point and mixed four-point branches.
5. Give exact LaTeX insertions.

---

Now, do your task as per above.

## Assistant (2026-04-25 09:31:09)

I’ll treat `proof_of_rh(416).tex` as the controlling draft and audit only its definitions/theorems around quotient extraction, \(\Phi_K\), fixed-sector representatives, and transform input. Then I’ll give a theorem-or-countermodel conclusion plus exact LaTeX patches.

I found the relevant structure in the draft: the reduced package records \(A_5^{\mathfrak f}\) and the septic quotient \([A_7^{\mathfrak f}]\), while the current text already warns that the affine lift \(A_7^{\mathfrak f}\mapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}\) is \(\Phi_K\)-visible when \(v_5\neq0\). The remaining question is therefore not computational; it is an identifiability theorem.

_Thought for 2m 24s_

## Agent 4 verdict

The answer is **negative**: the current reduced quotient package does **not** determine the first \(\Phi_K\)-visible corrected odd coefficient. The obstruction is formal, not computational.

The quotient remembers
\[
[A_7^{\mathfrak f}]\in \mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]
so it identifies
\[
A_7^{\mathfrak f}\sim A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}.
\]
But on
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\]
we have
\[
\Phi_K(A_5^{\mathfrak f})=2v_5.
\]
Thus the forgotten quotient direction is \(\Phi_K\)-visible whenever \(v_5\neq0\). This matches the hidden-state warning already in the current handoff material. 

## Minimal state

Let
\[
A_7^{\mathfrak f}=u_7I+v_7S.
\]
Then
\[
\Phi_K(A_7^{\mathfrak f})=2v_7.
\]

So the minimal extra hidden state is the image
\[
[A_7^{\mathfrak f}]_{\Phi}:=A_7^{\mathfrak f}\bmod\ker\Phi_K,
\]
equivalently the scalar \(v_7\), or the normalized scalar \(v_7/c\) if working in \(c\)-normalized coordinates.

Classification:

| Candidate data | Determines first \(\Phi_K\)-visible septic state? | Verdict |
|---|---:|---|
| Quotient class \([A_7^{\mathfrak f}]\) | No | loses affine lift |
| Quotient class plus \(A_5^{\mathfrak f}\) | Generically no | still \(A_7\mapsto A_7+\chi A_5\) and \(\Phi_K\) changes by \(2\chi v_5\) |
| Diagnostic tuple \(\widetilde\Psi_{\min}\) | Locally yes, normalized | because it contains \(T=v_7/c\), but it is diagnostic, not canonical |
| Additional raw septic representative data | Yes | \(v_7\), \(\Phi_K(A_7^{\mathfrak f})\), or \(A_7^{\mathfrak f}\bmod\ker\Phi_K\) suffices |

Special case: on \(v_5=0\), the quotient line is \(\Phi_K\)-invisible, so quotient equality may determine the \(\Phi_K\)-visible state. This is nongeneric relative to the current \(\{c\neq0,v_5\neq0\}\) diagnostic patch.

## Formal countermodel

Take
\[
A_5^{\mathfrak f}=S,
\qquad c=1,
\qquad A_7^{\mathfrak f,\chi}=\chi S.
\]
Then
\[
[A_7^{\mathfrak f,\chi}]=0
\quad\text{in}\quad
\mathfrak f/\mathbf C S
\]
for every \(\chi\), and
\[
\Delta_7=u_7v_5-u_5v_7=0.
\]
So the reduced quotient package is identical for all \(\chi\). But
\[
\Phi_K(A_7^{\mathfrak f,\chi})=2\chi.
\]
Thus quotient package equality does not imply equality of the first \(\Phi_K\)-visible corrected odd coefficient.

## Extra theorem needed

The missing theorem must say that the actual corrected package-to-transform map kills the quotient-forgotten direction, not merely that the quotient class closes.

A usable theorem would be:

\[
P\sim_{\mathrm{red}}P'
\quad\Longrightarrow\quad
A_{7,\Xi}^{\mathfrak f}(P')-A_{7,\Xi}^{\mathfrak f}(P)\in\ker\Phi_K.
\]

Equivalently, the first transform-visible septic coefficient must factor through the reduced package:
\[
\Phi_K\!\left(A_{7,\Xi}^{\mathfrak f}(P)\right)
=
\Theta_{\Phi,7}\!\left(\widehat\Psi_{\mathrm{red}}(P)\right).
\]

Without that state-locality theorem, quotient closure does not feed the two-point or mixed four-point branches.

## Exact LaTeX insertions

Insert this immediately after `rem:reduced-package-equality-not-hidden-state-equality`.

```tex
\begin{definition}[\(\Phi_K\)-visible septic state]
\label{def:phik-visible-septic-state}
On the fixed target fiber
\[
\mathfrak f_m=\mathbf C I\oplus \mathbf C S,
\]
write
\[
A_7^{\mathfrak f}=u_7I+v_7S.
\]
The \(\Phi_K\)-visible septic state is the class
\[
[A_7^{\mathfrak f}]_{\Phi}:=
A_7^{\mathfrak f}\bmod \ker(\Phi_K|_{\mathfrak f_m}),
\]
equivalently the scalar
\[
\phi_7:=\Phi_K(A_7^{\mathfrak f})=2v_7.
\]
If the \(c\)-normalized package is being used, the normalized visible septic
state is
\[
\theta_7:=\frac{\phi_7}{c}=\frac{2v_7}{c}.
\]
\end{definition}

\begin{proposition}[Formal non-descent of the \(\Phi_K\)-visible septic state]
\label{prop:formal-non-descent-phik-visible-septic-state}
On the generic locus \(v_5\neq0\), the quotient class
\[
[A_7^{\mathfrak f}]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)
\]
does not determine the \(\Phi_K\)-visible septic state
\[
[A_7^{\mathfrak f}]_{\Phi}
\in
\mathfrak f_m/\ker(\Phi_K|_{\mathfrak f_m}).
\]
In particular, quotient package equality does not imply equality of the first
\(\Phi_K\)-visible corrected odd coefficient.
\end{proposition}

\begin{proof}
Write
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
A_7^{\mathfrak f}=u_7I+v_7S.
\]
The quotient identifies
\[
A_7^{\mathfrak f}
\sim
A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}.
\]
However
\[
\Phi_K(A_7^{\mathfrak f}+\chi A_5^{\mathfrak f})
-
\Phi_K(A_7^{\mathfrak f})
=
\chi\Phi_K(A_5^{\mathfrak f})
=
2\chi v_5.
\]
Thus, if \(v_5\neq0\), the forgotten quotient direction is visible to
\(\Phi_K\).

Equivalently, take the formal model
\[
A_5^{\mathfrak f}=S,
\qquad
A_7^{\mathfrak f,\chi}=\chi S.
\]
Then
\[
[A_7^{\mathfrak f,\chi}]=0
\quad\text{in}\quad
\mathfrak f_m/\mathbf C S
\]
for every \(\chi\), and the determinant residual is also unchanged:
\[
\Delta_7=u_7v_5-u_5v_7=0.
\]
But
\[
\Phi_K(A_7^{\mathfrak f,\chi})=2\chi.
\]
Hence the reduced quotient package does not determine the
\(\Phi_K\)-visible septic state.
\end{proof}
```

Then replace or extend `rem:local-diagnostic-hidden-septic-state` with this sharpened version:

```tex
\begin{remark}[Diagnostic versus canonical hidden septic state]
\label{rem:diagnostic-versus-canonical-hidden-septic-state}
On the quintic-good patch
\[
\{c\neq0,\ v_5\neq0\},
\]
the diagnostic tuple
\[
\widetilde\Psi_{\min}=(x,Y,S,T)
=
\left(
\frac{v_5}{c},
\frac{u_5}{c},
\frac{\Delta_7}{cv_5},
\frac{v_7}{c}
\right)
\]
does determine the normalized \(\Phi_K\)-visible septic state, since
\[
\frac{\Phi_K(A_7^{\mathfrak f})}{c}=2T.
\]
But this is precisely why \(\widetilde\Psi_{\min}\) is not the same object as
the reduced quotient package: it includes the extra affine-lift coordinate
\(T=v_7/c\), which is not determined by
\[
(c,\ A_5^{\mathfrak f},\ [A_7^{\mathfrak f}])
\]
or by \((c,A_5^{\mathfrak f},\Delta_7)\) alone.  Thus
\(\widetilde\Psi_{\min}\) is a useful local diagnostic for the hidden-state
problem, but not a canonical global theorem object unless the missing
package-to-transform state-locality theorem supplies a canonical lift.
\end{remark}
```

Finally, insert this near the downstream obligations section, preferably before the final “remaining burden” summary.

```tex
\begin{remark}[Needed package-to-transform state-locality theorem]
\label{rem:needed-package-to-transform-state-locality-theorem}
The theorem needed downstream is not merely quotient-septic closure.  It must
identify the first transform-visible corrected odd coefficient as a function of
the reduced corrected package.

A sufficient form is the following state-locality statement.  If two actual
corrected packages \(P,P'\) have the same reduced package datum, then
\[
A_{7,\Xi}^{\mathfrak f}(P')-A_{7,\Xi}^{\mathfrak f}(P)
\in
\ker\Phi_K.
\]
Equivalently, there should exist a package-local functional
\[
\Theta_{\Phi,7}
\]
such that
\[
\Phi_K\!\left(A_{7,\Xi}^{\mathfrak f}(P)\right)
=
\Theta_{\Phi,7}\!\left(\widehat\Psi_{\mathrm{red}}(P)\right).
\]
Only such a theorem allows the corrected quotient package to feed the
two-point and mixed four-point transform branches.  Without it, a residual
affine lift
\[
A_7^{\mathfrak f}\longmapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}
\]
can be invisible in the quotient package while changing the transform-visible
quantity by
\[
2\chi v_5.
\]
\end{remark}
```

Net result: the paper should state this as a **formal non-descent counterexample** plus a **precise theorem obligation**. The current reduced package is insufficient; \(\widetilde\Psi_{\min}\) is sufficient only as a local diagnostic because it explicitly adds the missing \(v_7/c\) lift coordinate.
## User (2026-04-25 09:51:33)

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

# Agent 4 — Bottleneck C: quotient-valued diagonal merger

```text
You are attacking Bottleneck C: exceptional-divisor fiber selection.

Goal:
Prove or refute that the exceptional-divisor trace
\[
B(m,\kappa)=\widetilde\Psi_{\rm red}^{\corr}(m,\kappa,0)
\]
is independent of \(\kappa\).

Known warning:
Analyticity, swap symmetry, fixed codomain, scalar normalization, and
\[
B(m,0)=\widehat\Psi(m)
\]
do not by themselves imply \(\partial_\kappa B=0\).

Collision chart:
\[
h_1=m-\frac{\delta}{2},
\qquad
h_2=m+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta).
\]

Atom swap gives:
\[
\delta\mapsto-\delta,
\qquad
\kappa\mapsto\frac{\kappa}{1+\kappa\delta},
\]
so on \(\delta=0\), \(\kappa\mapsto\kappa\). Thus swap does not kill \(\kappa\)-slope.

Target theorem:
Prove quotient-valued diagonal merger:
\[
B(m,\kappa)=B(m,0)=\widehat\Psi(m)
\]
or equivalently
\[
B_7^{\mathfrak f}(m,\kappa,0)
-
B_7^{\mathfrak f}(m,0,0)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

Tasks:
1. Formalize the corrected two-atom collision functor as the ordered composite:
\[
\mathcal B_2
\to
C_{\mathcal W}^{\rm raw}
\to
(1-\Pi_{1,1})_{\rm mix}
\to
-a_1^{-1}\delta^{-2}
\to
\pi_{\mathfrak f_h}[z^{\le7}]
\to
\tau_{h\to m}
\to
[z^7]
\to
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
2. Check whether this functor factors through the blow-down
\[
(m,\kappa,0)\mapsto m.
\]
3. Identify any actual package property that kills the formal leakage model
\[
\delta^2 Z_0(m)+2\varepsilon\omega\delta E_m,
\qquad
\kappa=2\omega/\delta.
\]
4. Determine whether the \(a_2=-a_1(1+\kappa\delta)\) balancing condition imposes a hidden derivative constraint at \(\delta=0\).
5. Check whether quotienting by \(\mathbf C A_5^{\mathfrak f}\) removes or preserves the possible \(\kappa\)-slope.

Deliverable:
Either a proof of diagonal merger, or a formal quotient-visible leakage model compatible with all current assumptions, plus the exact missing theorem needed to exclude it.
```

## Assistant (2026-04-25 09:53:09)

_Thought for 1m 33s_

## Agent 4 verdict

Bottleneck C is **not closed** by the current draft assumptions. The correct output is a **formal quotient-visible leakage model**.

The draft correctly identifies Bottleneck C as exceptional-divisor fiber selection and says formal properties alone do not force \(\partial_\kappa B=0\); the proof must supply diagonal merger, same-reduced-image, or corrected two-atom collision functoriality. 

The obstruction is real:

\[
B(m,\kappa)
=
\widetilde\Psi_{\rm red}^{\corr}(m,\kappa,0)
\]

need not factor through

\[
(m,\kappa,0)\mapsto m
\]

unless the actual corrected two-atom package supplies an additional quotient-horizontal merger theorem.

---

## 1. Correct ordered functor

The Bottleneck C object is the quotient-valued composite

\[
\mathcal B_2
\longmapsto
C_{\mathcal W}^{\rm raw}
\longmapsto
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\longmapsto
-a_1^{-1}\delta^{-2}
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\]

\[
\longmapsto
\pi_{\mathfrak f_h}[z^{\le 7}]
\longmapsto
\tau_{h\to m}
\longmapsto
[z^7]
\longmapsto
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

So define

\[
\mathcal C_7^q(m,\kappa,\delta)
:=
\left[
[z^7]\,
\tau_{h\to m}
\pi_{\mathfrak f_h}
\left(
-a_1^{-1}\delta^{-2}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W}^{\rm raw}
\right)
\right].
\]

Then

\[
B(m,\kappa)=\mathcal C_7^q(m,\kappa,0).
\]

The desired diagonal merger is exactly

\[
\mathcal C_7^q(m,\kappa,0)=\mathcal C_7^q(m,0,0).
\]

The current definitions construct \(\mathcal C_7^q\), but they do **not** prove this factorization.

---

## 2. Swap does not kill the slope

In the collision chart

\[
h_1=m-\frac{\delta}{2},
\qquad
h_2=m+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta),
\]

atom swap gives

\[
\delta\mapsto-\delta,
\qquad
\kappa\mapsto\frac{\kappa}{1+\kappa\delta}.
\]

On \(\delta=0\),

\[
\kappa\mapsto\kappa.
\]

So the exceptional divisor has fixed \(\kappa\), not \(\kappa\mapsto-\kappa\). There is no parity reason for

\[
\partial_\kappa B(m,\kappa)
\]

to vanish.

---

## 3. Formal quotient-visible leakage model

Fix a good patch with

\[
A_5^{\mathfrak f}(m)\neq0.
\]

Choose \(E_m\in\mathfrak f_m\) transverse to the quotient line:

\[
\omega_m(E_m,A_5^{\mathfrak f}(m))=1.
\]

Let

\[
T(\kappa,\delta)
=
\left(
\frac{\kappa}{1+\kappa\delta},
-\delta
\right)
\]

be the atom-swap action on \((\kappa,\delta)\). Define the analytic swap-invariant function

\[
H(\kappa,\delta)
:=
\frac12
\left(
\kappa+
\frac{\kappa}{1+\kappa\delta}
\right).
\]

Then

\[
H(T(\kappa,\delta))=H(\kappa,\delta),
\qquad
H(\kappa,0)=\kappa.
\]

Now define a formal normalized septic edge representative by

\[
\mathcal R_\varepsilon(m,\kappa,\delta;z)
=
z^7
\left(
Z_0(m)+\varepsilon H(\kappa,\delta)E_m
\right),
\]

or, before the \(-a_1^{-1}\delta^{-2}\) normalization, by

\[
\mathcal N_\varepsilon
=
-a_1\delta^2 z^7
\left(
Z_0(m)+\varepsilon H(\kappa,\delta)E_m
\right).
\]

This model satisfies:

\[
\mathcal N_\varepsilon=O(a_1\delta^2),
\]

so it is compatible with raw Gate B edge-divisibility.

It is analytic in the blown-up chart.

It is swap-compatible because \(H\) is swap-invariant.

It preserves the central value:

\[
B_\varepsilon(m,0)
=
[Z_0(m)]
=
\widehat\Psi(m).
\]

But on the exceptional divisor,

\[
B_\varepsilon(m,\kappa)
=
[Z_0(m)+\varepsilon\kappa E_m].
\]

Since \([E_m]\neq0\) in

\[
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]

we get

\[
\partial_\kappa B_\varepsilon(m,\kappa)
=
\varepsilon [E_m]\neq0.
\]

Thus quotient-visible \(\kappa\)-leakage is compatible with the currently stated formal properties.

---

## 4. Balancing condition does not add a hidden derivative constraint

The balancing condition

\[
a_2=-a_1(1+\kappa\delta)
\]

only implies

\[
\partial_\kappa a_2=-a_1\delta.
\]

That factor of \(\delta\) is not enough to kill the exceptional slope after dividing by \(\delta^2\). A raw term of the form

\[
-a_1\delta^2\kappa E_m
\]

is perfectly compatible with the normalization and survives as

\[
\kappa E_m.
\]

Equivalently, using \(\kappa=2\omega/\delta\), the leakage term

\[
2\varepsilon\omega\delta E_m
=
\varepsilon\kappa\delta^2 E_m
\]

is exactly of the allowed Gate-B edge order and survives normalization.

So the balancing condition kills the zero-th source moment, but not the projective exceptional slope.

---

## 5. Quotienting preserves the bad slope unless it is parallel to \(A_5\)

Quotienting removes only the direction

\[
\mathbf C A_5^{\mathfrak f}(m).
\]

Therefore a leakage term

\[
\varepsilon\kappa L_m
\]

is killed only if

\[
L_m\in\mathbf C A_5^{\mathfrak f}(m).
\]

For the formal model above, \(L_m=E_m\) and

\[
\omega_m(E_m,A_5^{\mathfrak f}(m))=1,
\]

so the leakage is maximally quotient-visible.

Thus the exact missing theorem is not ordinary analyticity, parity, or normalization. It is:

\[
\partial_\kappa B_7^{\mathfrak f}(m,\kappa,0)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

Equivalently,

\[
\partial_\kappa Q_{7,m}^q(m,\kappa,0)=0.
\]

---

# Exact LaTeX insertions

Insert after `rem:missing-quotient-valued-diagonal-merger`.

```latex
\begin{definition}[Quotient-valued two-atom collision functor]
\label{def:quotient-valued-two-atom-collision-functor}
On a good patch with
\[
A_5^{\mathfrak f}(m)\neq0,
\]
define the order-\(7\) quotient-valued two-atom collision functor by the
ordered composite
\[
\mathcal B_2
\longmapsto
C_{\mathcal W}^{\rm raw}
\longmapsto
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\longmapsto
-a_1^{-1}\delta^{-2}
(1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\]
\[
\longmapsto
\pi_{\mathfrak f_h}[z^{\le7}]
\longmapsto
\tau_{h\to m}
\longmapsto
[z^7]
\longmapsto
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
In formulas,
\[
\mathcal C_7^q(m,\kappa,\delta)
:=
\left[
[z^7]\,
\tau_{h\to m}
\pi_{\mathfrak f_h}
\left(
-a_1^{-1}\delta^{-2}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W}^{\rm raw}
\right)
\right].
\]
The exceptional-divisor trace is
\[
B(m,\kappa)=\mathcal C_7^q(m,\kappa,0).
\]
Thus quotient-valued diagonal merger is precisely the statement that
\[
\mathcal C_7^q(m,\kappa,0)
=
\mathcal C_7^q(m,0,0),
\]
or equivalently that \(\mathcal C_7^q\) factors on the exceptional divisor
through the blow-down map
\[
(m,\kappa,0)\longmapsto m.
\]
\end{definition}

\begin{proposition}[Formal quotient-visible exceptional-slope leakage]
\label{prop:formal-quotient-visible-exceptional-slope-leakage}
The formal properties
\[
\text{analyticity},\qquad
\text{atom-swap compatibility},\qquad
\text{fixed codomain},\qquad
\text{scalar normalization},\qquad
B(m,0)=\widehat\Psi(m)
\]
do not imply quotient-valued diagonal merger.
\end{proposition}

\begin{proof}
Work on a good patch and choose
\[
E_m\in\mathfrak f_m
\]
with
\[
\omega_m(E_m,A_5^{\mathfrak f}(m))=1.
\]
Thus \(E_m\) is nonzero in the quotient
\[
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

In the collision chart
\[
h_1=m-\frac{\delta}{2},
\qquad
h_2=m+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta),
\]
atom-swap acts by
\[
\delta\longmapsto-\delta,
\qquad
\kappa\longmapsto\frac{\kappa}{1+\kappa\delta}.
\]
Define
\[
H(\kappa,\delta)
:=
\frac12
\left(
\kappa+\frac{\kappa}{1+\kappa\delta}
\right).
\]
Then \(H\) is analytic near \((\kappa,\delta)=(0,0)\), satisfies
\[
H\!\left(\frac{\kappa}{1+\kappa\delta},-\delta\right)
=
H(\kappa,\delta),
\]
and restricts to
\[
H(\kappa,0)=\kappa
\]
on the exceptional divisor.

Let \(Z_0(m)\in\mathfrak f_m\) be any representative of
\(\widehat\Psi(m)\), and define the formal normalized septic edge
representative
\[
\mathcal R_\varepsilon(m,\kappa,\delta;z)
=
z^7
\left(
Z_0(m)+\varepsilon H(\kappa,\delta)E_m
\right).
\]
Equivalently, before the edge normalization one may write the raw model as
\[
\mathcal N_\varepsilon
=
-a_1\delta^2 z^7
\left(
Z_0(m)+\varepsilon H(\kappa,\delta)E_m
\right).
\]
This raw model is \(O(a_1\delta^2)\), so it is compatible with raw
edge-divisibility.  It is analytic and atom-swap compatible by construction.

At \(\kappa=0\),
\[
B_\varepsilon(m,0)=[Z_0(m)]=\widehat\Psi(m).
\]
But on the exceptional divisor,
\[
B_\varepsilon(m,\kappa)
=
[Z_0(m)+\varepsilon\kappa E_m],
\]
and hence
\[
\partial_\kappa B_\varepsilon(m,\kappa)
=
\varepsilon [E_m]\neq0
\]
in
\[
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
Therefore the listed formal properties do not force quotient-valued diagonal
merger.
\end{proof}

\begin{remark}[Balancing does not impose hidden \(\kappa\)-horizontality]
\label{rem:balancing-does-not-impose-kappa-horizontality}
The balancing condition
\[
a_2=-a_1(1+\kappa\delta)
\]
gives
\[
\partial_\kappa a_2=-a_1\delta.
\]
This single factor of \(\delta\) does not force the normalized exceptional
slope to vanish after the \(\delta^{-2}\) edge normalization.  A raw term of
the form
\[
-a_1\delta^2\kappa E_m
\]
is still of the allowed Gate-B edge order and survives normalization as
\[
\kappa E_m.
\]
Equivalently, with \(\kappa=2\omega/\delta\), the leakage term
\[
2\varepsilon\omega\delta E_m
=
\varepsilon\kappa\delta^2E_m
\]
is invisible before edge normalization but visible on the exceptional divisor.
Thus balancing kills the zero-th source moment; it does not by itself kill the
projective exceptional slope.
\end{remark}

\begin{theorem}[Missing theorem: exceptional-divisor quotient horizontality]
\label{thm:missing-exceptional-divisor-quotient-horizontality}
To close Bottleneck C it is enough, and in the present setup necessary, to
prove the following quotient-horizontal merger statement for the actual
corrected two-atom package:
\[
\partial_\kappa
B_7^{\mathfrak f}(m,\kappa,0)
\in
\mathbf C A_5^{\mathfrak f}(m)
\]
for all sufficiently small \(\kappa\) on every good patch
\[
A_5^{\mathfrak f}(m)\neq0.
\]
Equivalently,
\[
\partial_\kappa Q_{7,m}^q(m,\kappa,0)=0.
\]
Equivalently again, the quotient-valued collision functor satisfies
\[
\mathcal C_7^q(m,\kappa,0)=\mathcal C_7^q(m,0,0).
\]
This theorem is not a consequence of analyticity, atom-swap symmetry, fixed
codomain, scalar normalization, or the central value
\(B(m,0)=\widehat\Psi(m)\).  It must be proved from actual corrected
two-atom collision functoriality, a same-reduced-image theorem, or a direct
quotient-valued diagonal merger calculation.
\end{theorem}
```

Net: Bottleneck C should remain marked **open**. The current draft has the right warning, but the stronger formal leakage proposition above makes the dependency precise and theorem-ready.
## User (2026-04-25 10:04:31)

You are Agent 4. Read the attached command and do you task.

## Assistant (2026-04-25 10:04:32)

I’ll execute the Agent 4 task from the attached command: focus on actual corrected-package quotient-horizontality, not repeat the earlier formal leakage model except where needed to isolate the live source component.

_Thought for 1m 47s_

## Agent 4 verdict

I **cannot prove quotient-horizontal merger from the current actual-package assumptions**. The first actual corrected-package carrier of quotient-visible \(\kappa\)-slope is the **even transfer-degree \(d=4\), source-bidegree \((1,3)\oplus(3,1)\) edge channel**.

The missing theorem is not generic diagonal merger. It is a **weighted source-bidegree line-gauge identity** for the actual corrected whitening source blocks.

The attached command makes Bottleneck C sharper: Gate B only gives the unweighted balanced edge relation, while diagonal merger requires the stronger weighted derivative relation
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
That is exactly the distinction that exposes the surviving \(d=4\) carrier. 

---

# 1. Quotient-horizontal merger reduces to a weighted source-bidegree identity

Let
\[
F(a_1,a_2,\delta)
=
[z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W}^{\rm raw}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]

Write the first collision edge coefficient as
\[
[\delta^1]F(a_1,a_2,\delta)
=
\sum_{\substack{p,q\ge1\\(p,q)\neq(1,1)}}
a_1^pa_2^qE_{p,q}(m),
\qquad
E_{p,q}(m)\in\mathfrak f_m.
\]

Gate B gives only
\[
\sum_{p,q}
a_1^p(-a_1)^qE_{p,q}(m)=0.
\]

But the exceptional-divisor slope in
\[
a_2=-a_1(1+\kappa\delta)
\]
is controlled by
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
=
\sum_{p,q}
q\,a_1^p(-a_1)^{q-1}E_{p,q}(m).
\]

Thus Bottleneck C is equivalent to
\[
\boxed{
\sum_{p,q}
q\,a_1^p(-a_1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
}
\]

Coefficientwise by total source degree \(d=p+q\), the needed identity is
\[
\boxed{
\sum_{\substack{p+q=d\\p,q\ge1\\(p,q)\neq(1,1)}}
q(-1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
}
\]

This is the exact actual source-block identity that would kill \(\kappa\)-leakage.

---

# 2. Why the standard mechanisms do not imply it

## Balanced amplitude relation

Balanced amplitude gives the unweighted identity
\[
\sum_{p+q=d}(-1)^qE_{p,q}=0.
\]

It does **not** imply
\[
\sum_{p+q=d}q(-1)^{q-1}E_{p,q}\in \mathbf C A_5^{\mathfrak f}.
\]

The weights \(q\) are new information. They measure how much of the source-bidegree sits on the second atom, i.e. exactly the exceptional slope direction.

## Source-bidegree projection

The projection
\[
(1-\Pi_{1,1})_{\rm mix}
\]
only removes \((1,1)\). It preserves \((1,3)\), \((3,1)\), \((2,2)\), etc. It does not impose any weighted relation among them.

## \(Y\)-middle parity

\(Y\)-middle parity can remove or pair certain \(Y\)-slot families. It does not control the non-\(Y\), even-degree amplitude derivative channel. In particular, it does not force the fourth-transfer \((1,3)\oplus(3,1)\) edge component to be parallel to \(A_5^{\mathfrak f}\).

## Moving source-frame telescoping

The moving source-frame telescoping theorem cancels source-motion lower-shadow terms. The \(\kappa\)-slope carrier is different: it is the amplitude derivative generated by
\[
a_2=-a_1(1+\kappa\delta).
\]
For even transfer degree \(d=4\), the universal first-collision formula has only the amplitude-derivative term; the endpoint source-motion insertion cancels. So telescoping does not touch the first live Bottleneck C carrier.

## Corrected whitening symmetry

Atom-swap symmetry gives an antisymmetry constraint on the \([\delta^1]\)-edge:
\[
E_{q,p}=-E_{p,q}
\]
for the relevant swapped bidegree pair, up to the standard fixed-sector identification.

This is enough to make some **unweighted** balanced sums vanish for even total degree, but it does not kill the weighted derivative. For \((p,q)=(1,3)\),
\[
3E_{1,3}+1E_{3,1}
=
3E_{1,3}-E_{1,3}
=
2E_{1,3}.
\]
Thus the weighted derivative preserves the antisymmetric pair instead of cancelling it.

## Same-reduced-image functoriality

A genuine same-reduced-image theorem would imply quotient-horizontality. But that is not currently available; it is essentially the missing theorem itself. It cannot be used as an already-proved mechanism.

---

# 3. First actual quotient-visible carrier

The first source-bidegree channel compatible with the current constraints is not cubic. It is quartic.

For total source degree \(d=3\), atom-swap antisymmetry makes the balanced value nonzero unless the corresponding coefficient already vanishes. Hence Gate B kills the total-degree \(3\) antisymmetric edge.

For total source degree \(d=4\), the antisymmetric pair
\[
a_1a_2^3\delta E-a_1^3a_2\delta E
\]
satisfies the balanced Gate B relation:
\[
a_1(-a_1)^3E-a_1^3(-a_1)E
=
-a_1^4E+a_1^4E
=
0.
\]

But its weighted derivative is
\[
\partial_{a_2}
\left(a_1a_2^3\delta E-a_1^3a_2\delta E\right)
=
\delta(3a_1a_2^2-a_1^3)E,
\]
and at \(a_2=-a_1\),
\[
[\delta^1]\partial_{a_2}
=
2a_1^3E.
\]

Therefore the first live carrier is
\[
\boxed{
E_{1,3}(m)-E_{3,1}(m)
}
\]
more precisely the fourth-transfer, one-against-three source-bidegree edge
\[
\boxed{
[z^7]\pi_{\mathfrak f_h}
[\delta^1]
\left(
C_{\mathcal W,(1,3)}^{\rm raw}
-
C_{\mathcal W,(3,1)}^{\rm raw}
\right).
}
\]

In corrected-whitening transfer notation, this is the actual \(d=4\) amplitude-derivative channel
\[
\boxed{
[z^7]\pi_{\mathfrak f_h}
\left(
\mathcal T_4(X_1,X_2,X_2,X_2)
-
\mathcal T_4(X_1,X_1,X_1,X_2)
\right),
}
\]
summed over all labelled ordinary-order \(7\) source-grade multisets, for example the \((1,1,1,4)\), \((1,1,2,3)\), and related grade partitions that survive the actual corrected source-block constraints.

This is not excluded by Gate B. Gate B only sees the balanced unweighted cancellation. Bottleneck C sees the weighted derivative.

---

# 4. Exact missing theorem

The required theorem is:

```latex
\begin{theorem}[Weighted source-bidegree quotient-horizontality]
\label{thm:weighted-source-bidegree-quotient-horizontality}
Let
\[
[\delta^1]F(a_1,a_2,\delta)
=
\sum_{\substack{p,q\ge1\\(p,q)\ne(1,1)}}
a_1^pa_2^qE_{p,q}(m)
\]
be the order-\(7\) fixed-sector first-collision edge coefficient of the
actual corrected-whitening cross-effect.  On every good patch
\[
A_5^{\mathfrak f}(m)\ne0,
\]
one has, for each total source degree \(d\),
\[
\sum_{\substack{p+q=d\\p,q\ge1\\(p,q)\ne(1,1)}}
q(-1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently,
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
Consequently,
\[
\partial_\kappa B_7^{\mathfrak f}(m,\kappa,0)
\in
\mathbf C A_5^{\mathfrak f}(m),
\]
and hence
\[
\partial_\kappa Q_{7,m}^q(m,\kappa,0)=0.
\]
\end{theorem}
```

The first nontrivial coefficient-level case of this theorem is:

```latex
\begin{lemma}[First live Bottleneck C carrier]
\label{lem:first-live-bottleneck-c-carrier}
The first source-bidegree channel not killed by balanced Gate-B cancellation
is the fourth-transfer one-against-three channel
\[
(1,3)\oplus(3,1).
\]
For this channel, atom-swap symmetry gives
\[
E_{3,1}=-E_{1,3},
\]
so the balanced edge contribution vanishes:
\[
(-1)^3E_{1,3}+(-1)^1E_{3,1}=0.
\]
However the exceptional-slope derivative is
\[
3E_{1,3}+E_{3,1}=2E_{1,3}.
\]
Therefore quotient-horizontal merger requires the extra line-gauge condition
\[
E_{1,3}\in \mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently,
\[
[z^7]\pi_{\mathfrak f_h}
\left(
\mathcal T_4(X_1,X_2,X_2,X_2)
-
\mathcal T_4(X_1,X_1,X_1,X_2)
\right)
\in
\mathbf C A_5^{\mathfrak f}(m),
\]
after summing over the actual ordinary-order \(7\) source-grade
specializations.
\end{lemma}
```

---

# 5. Final status

\[
\boxed{
\text{Bottleneck C remains open.}
}
\]

The current actual-package assumptions do not force
\[
\partial_\kappa B_7^{\mathfrak f}(m,\kappa,0)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

The first concrete live obstruction is:

\[
\boxed{
\text{the \(d=4\), \((1,3)\oplus(3,1)\), weighted source-bidegree edge channel.}
}
\]

To close Bottleneck C, the paper needs a theorem proving that this channel, and then all higher even one-against-\((d-1)\) analogues, are \(A_5^{\mathfrak f}\)-line-gauge after actual corrected source-block substitution.
## User (2026-04-25 10:09:20)

continue to attack, and derive anything you need from the paper.

## Assistant (2026-04-25 10:09:21)

I’ll push further on the live \(d=4\) weighted edge channel, using the draft to see whether actual source-block definitions impose a stronger bidegree identity than the formal Gate B relation.

A correction emerged from the draft itself: the homogeneous tower already kills the \(\kappa\)-slope, because the universal first-collision formula makes the \(\kappa\)-term proportional to the same amplitude term annihilated by odd total-grade subset-complement cancellation. The live Bottleneck C obstruction is therefore narrower: it must come from actual-source deviations from that homogeneous tower, not from the homogeneous \(d=4\) amplitude channel itself.

_Thought for 2m 20s_

## Agent 4 continuation — revised attack result

The sharper attack changes the conclusion.

My prior “first live \(d=4\), \((1,3)\oplus(3,1)\)” carrier is valid as a **formal weighted-bidegree countermodel**, but it is **not compatible with the draft’s homogeneous tower mechanism**. The latest draft contains enough structure to kill that carrier in the homogeneous scalar-grade tower.

The live Bottleneck C obstruction is narrower:

\[
\boxed{
\text{Bottleneck C can only leak through actual-source deviation from the homogeneous tower.}
}
\]

The prompt’s sharpened target is exactly the weighted edge derivative law:
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m),
\]
where Gate B only gives the unweighted balanced relation
\[
[\delta^1]F(a_1,-a_1,\delta)=0.
\]
That distinction is the correct Bottleneck C attack surface. 

---

# 1. Bottleneck C is double balanced divisibility modulo the quotient line

Let
\[
P_{7,m}(a_1,a_2)
:=
[z^7][\delta^1]\,
\tau_{h\to m}\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W}^{\rm raw}(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]

Work in the quotient
\[
V_m:=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]
and let
\[
\overline P_{7,m}
\]
denote the image of \(P_{7,m}\) in \(V_m[a_1,a_2]\).

Then:

\[
\boxed{
\text{Gate B}
\iff
\overline P_{7,m}(a_1,-a_1)=0.
}
\]

Equivalently,
\[
\overline P_{7,m}
\in
(a_1+a_2)V_m[a_1,a_2].
\]

Bottleneck C requires the stronger condition
\[
\boxed{
\partial_{a_2}\overline P_{7,m}(a_1,-a_1)=0.
}
\]

Equivalently,

\[
\boxed{
\overline P_{7,m}
\in
(a_1+a_2)^2V_m[a_1,a_2].
}
\]

So the real target is:

\[
\boxed{
[z^7][\delta^1](1-\Pi_{1,1})_{\rm mix}C_{\mathcal W}^{\rm raw}
\text{ has a double balanced zero modulo }\mathbf C A_5^{\mathfrak f}.
}
\]

This is stronger and cleaner than saying “weighted cancellation.” Weighted cancellation is the coefficient form of double divisibility.

---

# 2. The homogeneous tower already gives double divisibility

The draft’s universal first-collision formula says that, for homogeneous transfer degree \(d\),

\[
F_{1,d}
=
[z^7]\pi_{\mathfrak f_h}
\left[
(-1)^{d+1}d\kappa\,\mathcal T_d(X^d)
+
\frac d2(1-(-1)^d)\mathcal T_d(X^{d-1},X_h)
\right].
\]

The important point is that the \(\kappa\)-slope is proportional to the **same diagonal amplitude term**
\[
[z^7]\pi_{\mathfrak f_h}\mathcal T_d(X^d).
\]

But for total homogeneous grade \(7\), the draft’s odd total-grade subset-complement cancellation kills exactly this amplitude term. Gate B is conditionally closed by this mechanism plus moving source-frame telescoping and affine-boundary removal. 

Therefore, in the homogeneous scalar-grade tower,

\[
\boxed{
\partial_\kappa Q_{7,m}^{q,\mathrm{tower}}(m,\kappa,0)=0.
}
\]

So the homogeneous tower does not merely prove the unweighted balanced relation. It also proves the Bottleneck C weighted derivative relation.

---

# 3. What was wrong with the naive \(d=4\) carrier

The formal leakage model
\[
a_1a_2^3\delta E-a_1^3a_2\delta E
\]
has a simple balanced zero:

\[
a_1a_2^3-a_1^3a_2
=
a_1a_2(a_2-a_1)(a_1+a_2).
\]

It vanishes at \(a_2=-a_1\), so it passes Gate B.

But it is not divisible by \((a_1+a_2)^2\), so it fails Bottleneck C.

The homogeneous tower forbids precisely this shape. In source-bidegree notation, write the \(d=4\) edge polynomial as

\[
P_4
=
a_1a_2^3E_{1,3}
+
a_1^2a_2^2E_{2,2}
+
a_1^3a_2E_{3,1}.
\]

Gate B gives

\[
-E_{1,3}+E_{2,2}-E_{3,1}=0.
\]

Bottleneck C gives

\[
3E_{1,3}-2E_{2,2}+E_{3,1}=0
\quad
\text{mod }\mathbf C A_5^{\mathfrak f}(m).
\]

Together, these say that modulo the quotient line,

\[
E_{3,1}=E_{1,3},
\qquad
E_{2,2}=2E_{1,3}.
\]

Equivalently,

\[
P_4
\equiv
E_{1,3}\,a_1a_2(a_1+a_2)^2
\quad
\mod \mathbf C A_5^{\mathfrak f}(m).
\]

Thus the naive two-term countermodel is not a valid homogeneous-tower source block. It omits the compensating \((2,2)\) bidegree and violates the diagonal-polarization identity forced by the homogeneous transfer expansion.

---

# 4. The actual remaining obstruction

The live obstruction is therefore not:

\[
\mathcal T_4^{\mathrm{tower}}(1,3)\oplus\mathcal T_4^{\mathrm{tower}}(3,1).
\]

That is killed by the same diagonal amplitude cancellation that closes the homogeneous part of Gate B.

The live obstruction is:

\[
\boxed{
\text{actual-source simple balanced-zero defect}
}
\]

namely the quotient class

\[
\boxed{
\mathfrak L_{7,m}^{\actual}
:=
\left[
\partial_{a_2}
P_{7,m}^{\actual}(a_1,-a_1)
-
\partial_{a_2}
P_{7,m}^{\mathrm{tower}}(a_1,-a_1)
\right]
\in
V_m.
}
\]

Since the tower term vanishes in \(V_m\), this reduces to

\[
\mathfrak L_{7,m}^{\actual}
=
\left[
\partial_{a_2}
P_{7,m}^{\actual}(a_1,-a_1)
\right].
\]

Equivalently,

\[
\boxed{
\mathfrak L_{7,m}^{\actual}
=
0
\iff
\overline P_{7,m}^{\actual}
\in
(a_1+a_2)^2V_m[a_1,a_2].
}
\]

This is the precise source-block identity that kills Bottleneck C.

---

# 5. Where such a defect can enter

The draft’s tagged pre-whitening source block proves only \(\mathcal K\)-linear additivity before whitening. It explicitly does not prove transfer-domain vanishing, source-bidegree edge divisibility, quotient-output package coincidence, or diagonal merger. The shared status also stresses that Gate B remains conditional on the actual source model, not merely the formal tower. 

Therefore the first possible actual leakage must come from one of these:

\[
\boxed{
\mathcal K\text{-degree }\ge2\text{ remainders in }
G_-^{\corr},N^{\corr},G_+^{\corr}
}
\]

or from failure of the actual source model to realize one of:

\[
\boxed{
\text{homogeneous scalar-grade decomposition,}
}
\]

\[
\boxed{
\text{endpoint parity,}
}
\]

\[
\boxed{
\text{moving source-frame telescoping,}
}
\]

\[
\boxed{
\text{full-tower-before-truncation.}
}
\]

The first actual carrier has the form

\[
\boxed{
\overline P_{7,m}^{\actual}
=
(a_1+a_2)\,\overline R_{7,m}^{\actual},
\qquad
\overline R_{7,m}^{\actual}(a_1,-a_1)\neq0.
}
\]

In coefficient form:

\[
\boxed{
\sum_{p,q}
q\,a_1^p(-a_1)^{q-1}
\overline E_{p,q}^{\actual}(m)
\neq0.
}
\]

The first possible source-bidegree location is still \(d=4\), because \((1,3),(2,2),(3,1)\) are the first non-\((1,1)\) bidegrees capable of producing a simple balanced zero after the cubic/Gate A sector is removed. But it must be an **actual-source defect** in that \(d=4\) polynomial, not the homogeneous \(\mathcal T_4\) tower itself.

---

# 6. The theorem needed now

The missing theorem should be stated as double balanced divisibility, not merely weighted cancellation.

```latex
\begin{theorem}[Actual-source double balanced zero modulo the quotient line]
\label{thm:actual-source-double-balanced-zero-bottleneck-c}
Let
\[
P_{7,m}^{\actual}(a_1,a_2)
:=
[z^7][\delta^1]\,
\tau_{h\to m}\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W,\actual}^{\rm raw}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]
On every good patch with
\[
A_5^{\mathfrak f}(m)\ne0,
\]
let
\[
\overline P_{7,m}^{\actual}
\]
be its image in
\[
V_m[a_1,a_2],
\qquad
V_m:=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
Then Bottleneck C is closed if and only if
\[
\overline P_{7,m}^{\actual}
\in
(a_1+a_2)^2V_m[a_1,a_2].
\]
Equivalently,
\[
P_{7,m}^{\actual}(a_1,-a_1)\in\mathbf C A_5^{\mathfrak f}(m)
\]
and
\[
\partial_{a_2}P_{7,m}^{\actual}(a_1,-a_1)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{theorem}
```

And the homogeneous-tower lemma should be added before it:

```latex
\begin{lemma}[Homogeneous tower has double balanced zero]
\label{lem:homogeneous-tower-double-balanced-zero}
For the homogeneous scalar-grade tower used in Gate~B, the order-\(7\)
edge polynomial
\[
P_{7,m}^{\mathrm{tower}}(a_1,a_2)
\]
satisfies
\[
\overline P_{7,m}^{\mathrm{tower}}
\in
(a_1+a_2)^2
\left(
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)
\right)[a_1,a_2].
\]
In particular,
\[
\partial_{a_2}
P_{7,m}^{\mathrm{tower}}(a_1,-a_1)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{lemma}

\begin{proof}
By the universal first-collision formula, the exceptional-slope term is
proportional to the diagonal amplitude contribution
\[
[z^7]\pi_{\mathfrak f_h}\mathcal T_d(X^d).
\]
For total homogeneous grade \(7\), this amplitude contribution vanishes by
odd total-grade subset-complement cancellation.  The source-motion terms
are handled by the moving source-frame telescoping identity and the affine
boundary is removed by \(2\)-jet source-frame normalization.  Therefore
the balanced edge polynomial has not only a simple zero at \(a_2=-a_1\),
but a double zero modulo the quotient line.
\end{proof}
```

Finally, the actual-source defect should be isolated as:

```latex
\begin{definition}[Bottleneck C actual simple-zero defect]
\label{def:bottleneck-c-actual-simple-zero-defect}
Define the actual simple-zero defect by
\[
\mathfrak L_{7,m}^{\actual}
:=
\left[
\partial_{a_2}
P_{7,m}^{\actual}(a_1,-a_1)
\right]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently, if
\[
[\delta^1]F^{\actual}(a_1,a_2,\delta)
=
\sum_{p,q}a_1^pa_2^qE_{p,q}^{\actual}(m),
\]
then
\[
\mathfrak L_{7,m}^{\actual}
=
\left[
\sum_{p,q}
q\,a_1^p(-a_1)^{q-1}E_{p,q}^{\actual}(m)
\right].
\]
Bottleneck C is closed exactly when
\[
\mathfrak L_{7,m}^{\actual}=0.
\]
\end{definition}
```

---

# 7. Current attack status

\[
\boxed{
\text{Homogeneous Bottleneck C closes.}
}
\]

\[
\boxed{
\text{Actual-source Bottleneck C remains open.}
}
\]

The previous formal \(d=4\) countermodel should be retained only as a warning against “Gate B implies diagonal merger.” It is not a counterexample to the draft’s homogeneous tower, because the homogeneous tower forces double balanced divisibility.

The next attack should target this exact statement:

\[
\boxed{
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\mathrm{tower}}
\in
(a_1+a_2)^2V_m[a_1,a_2].
}
\]

Equivalently, prove that every \(\mathcal K\)-degree \(\ge2\) actual-source remainder either is too high order, is killed by fixed-sector projection, or contributes only a double-balanced-zero polynomial modulo \(\mathbf C A_5^{\mathfrak f}(m)\).
## User (2026-04-25 10:16:26)

Read and do your next attack (given your agent number) in the list.

## Assistant (2026-04-25 10:18:44)

_Thought for 2m 16s_

## Agent 4 next attack result

I **cannot close actual-source double-balanced divisibility** from the current draft plus command. The first actual component that can carry quotient-visible \(\kappa\)-slope is **not** the same-point cubic \(P_\pm\) response. It appears earlier, through the **\(\mathcal K\)-degree \(2\) nonlinear mixed-block Taylor remainder in \(N^{\corr}(d_-,d_+,\eta)\), coupled to one \(\mathcal K\)-linear whitening factor**.

This is exactly within the requested Agent 1 + Agent 4 target: prove/refute
\[
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\in
(a_1+a_2)^2V_m[a_1,a_2],
\qquad
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
The consolidated command identifies this as the next Agent 1 + Agent 4 attack and says to focus on nonlinear actual-source remainders, including nonlinear mixed-block Taylor remainders in \(N^{\corr}\). 

---

# 1. The decisive algebraic reduction

Let
\[
P_{7,m}^{\actual}(a_1,a_2)
:=
[z^7][\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W,\actual}^{\rm raw}.
\]

Bottleneck C is equivalent to
\[
\overline P_{7,m}^{\actual}
\in
(a_1+a_2)^2V_m[a_1,a_2].
\]

Gate B gives only
\[
\overline P_{7,m}^{\actual}(a_1,-a_1)=0,
\]
i.e.
\[
\overline P_{7,m}^{\actual}
\in
(a_1+a_2)V_m[a_1,a_2].
\]

So the actual question is whether every actual-source remainder has a **double balanced zero**, not merely a simple one.

---

# 2. First live actual-source remainder: quadratic mixed-block remainder

Write the actual mixed block as a Taylor expansion in
\[
\xi:=(d_-,d_+,\eta).
\]

The nonlinear mixed-block remainder begins with
\[
Y_{12}^{(2)}
:=
D^2N_0[\xi_1,\xi_2],
\]
where
\[
\xi_i=(d_{i,-},d_{i,+},\eta_i)
\]
is the source data for atom \(i\).

This term has source bidegree \((1,1)\). Alone, it is killed by
\[
(1-\Pi_{1,1})_{\rm mix}.
\]

But after corrected whitening it can couple to one \(\mathcal K\)-linear same-point whitening factor. The first such actual terms are

\[
\mathcal E_{Y,L}
=
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0,
\]
and
\[
\mathcal E_{Y,R}
=
L_0\,
Y_{12}^{(2)}\,
D(G_+^{-1/2})[B_+].
\]

Together,
\[
\mathcal E_Y
:=
\mathcal E_{Y,L}+\mathcal E_{Y,R}.
\]

This is source degree \(3\), with source bidegrees
\[
(2,1)\oplus(1,2).
\]

Its scalar amplitude polynomial has the form
\[
a_1a_2(a_1+a_2).
\]

Therefore
\[
a_1a_2(a_1+a_2)\big|_{a_2=-a_1}=0,
\]
so Gate B sees a simple balanced zero.

But
\[
\partial_{a_2}\bigl(a_1a_2(a_1+a_2)\bigr)\big|_{a_2=-a_1}
=
-a_1^2\neq0.
\]

So Bottleneck C sees the coefficient.

Hence the quotient-horizontal obstruction is

\[
\boxed{
\mathfrak L_{Y,3}(m)
:=
[z^7][\delta^1]\,
\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+]
\right)
\mod \mathbf C A_5^{\mathfrak f}(m).
}
\]

Bottleneck C requires
\[
\boxed{
\mathfrak L_{Y,3}(m)=0
\quad\text{in}\quad
V_m.
}
\]

I do not see a theorem in the current draft that proves this.

---

# 3. Classification of the requested remainder classes

## A. Higher Fréchet responses involving \(P_\pm\)

The same-point cubic source defect
\[
P_\pm\sim d_1^2d_2+d_1d_2^2
\]
has already been narrowed: its **single-insertion first Fréchet response is killed** after fixed-sector projection by endpoint swap and transpose invariance. The command explicitly records this prior result. 

The next terms are

\[
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0,
\]
\[
D(G_-^{-1/2})[P_-]N_0D(G_+^{-1/2})[B_+],
\]
\[
L_0N_0D^2(G_+^{-1/2})[P_+,B_+].
\]

At the diagonal, the \(P_\pm\)-cross term has bidegrees
\[
(2,1)\oplus(1,2),
\]
and multiplying by one linear factor gives source degree \(4\):
\[
(3,1)\oplus(2,2)\oplus(1,3).
\]

At zeroth collision order, the binomial structure gives the double-balanced polynomial
\[
a_1a_2(a_1+a_2)^2.
\]

But at first collision order, source motion differentiates the two atoms oppositely:
\[
X_1=X-\frac{\delta}{2}X_h+O(\delta^2),
\qquad
X_2=X+\frac{\delta}{2}X_h+O(\delta^2).
\]

For the cubic cross term
\[
P_{\rm cross}
=
3a_1^2a_2X_1^2X_2
+
3a_1a_2^2X_1X_2^2,
\]
one obtains
\[
[\delta^1]P_{\rm cross}
=
\frac32a_1a_2(a_2-a_1)X^2X_h.
\]

After multiplication by the diagonal linear factor
\[
A_{\rm tot}=(a_1+a_2)A+O(\delta),
\]
the \(\delta^1\)-edge contains
\[
\frac32a_1a_2(a_2-a_1)(a_1+a_2)X^2X_hA
\]
plus the analogous term with \(A_h\).

This has only **one** factor of \(a_1+a_2\), not two.

So \(P_\pm\)-higher Fréchet terms are not automatically double-balanced. They require a product-source-motion telescoping theorem for the nonlinear \(P_\pm\) source, not merely the homogeneous scalar-source telescoping already used in Gate B.

Classification:
\[
\boxed{
\text{not too high order; not formally double-balanced; live unless nonlinear product-source telescoping is proved.}
}
\]

But this is **not the first** live remainder, because the mixed-block quadratic remainder gives a source-degree \(3\) carrier.

---

## B. Nonlinear mixed-block Taylor remainders in \(N^{\corr}\)

This is the first live class.

The corrected mixed block has nonlinear Taylor terms in
\[
(d_-,d_+,\eta).
\]
The quadratic remainder
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]
\]
is source bidegree \((1,1)\), so it is invisible as a middle insertion by itself after \((1-\Pi_{1,1})_{\rm mix}\).

But after one same-point whitening derivative, it becomes degree \(3\):
\[
(1,1)+(1,0)=(2,1),
\qquad
(1,1)+(0,1)=(1,2).
\]

The amplitude polynomial is
\[
a_1a_2(a_1+a_2).
\]

This is simple-balanced but not double-balanced.

Classification:
\[
\boxed{
\text{first live Bottleneck C carrier unless }
\mathfrak L_{Y,3}(m)\in\mathbf C A_5^{\mathfrak f}(m).
}
\]

The needed identity is

\[
\boxed{
[z^7][\delta^1]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+]
\right)
\in
\mathbf C A_5^{\mathfrak f}(m).
}
\]

This looks closely related to the edge-refined \(Y\)-middle parity problem, but it is not identical: here the \(Y\)-middle term is nonlinear source-bidegree \((1,1)\), then promoted to non-\((1,1)\) by a same-point whitening derivative.

---

## C. Product-source-motion terms

The homogeneous moving source-frame telescoping theorem cancels adjacent grades for scalar homogeneous source slots. It does not automatically apply to products such as
\[
D^2N_0[\xi_1,\xi_2],
\qquad
P_\pm^{(2,1)/(1,2)}.
\]

For a product source
\[
\xi_1(h-\delta/2)\xi_2(h+\delta/2),
\]
the first collision derivative is
\[
[\delta^1]\xi_1(h-\delta/2)\xi_2(h+\delta/2)
=
\frac12\bigl(\xi_1\xi_{2,h}-\xi_{1,h}\xi_2\bigr).
\]

At collision \(\xi_1=\xi_2=\xi\), this vanishes for a scalar product, but not necessarily after applying different endpoint maps, same-point/mixed entries, Fréchet insertions, and fixed-sector projection. In particular, if the two factors enter different matrix slots, the commuted terms need not be literal negatives before projection.

Classification:
\[
\boxed{
\text{not covered by scalar homogeneous telescoping; requires a product-source telescoping theorem.}
}
\]

---

# 4. The first explicit actual-source defect term

The first explicit source component capable of quotient-visible \(\kappa\)-slope is:

\[
\boxed{
\mathfrak L_{Y,3}(m)
=
[z^7][\delta^1]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+]
\right)
\mod \mathbf C A_5^{\mathfrak f}(m).
}
\]

Here
\[
Y_{12}^{(2)}
=
D^2N_0[\xi_1,\xi_2]
\]
is the \(\mathcal K\)-degree \(2\), source-bidegree \((1,1)\) nonlinear Taylor remainder of the actual corrected mixed block.

The corresponding amplitude polynomial is
\[
a_1a_2(a_1+a_2).
\]

Therefore
\[
\overline P(a_1,-a_1)=0,
\]
but
\[
\partial_{a_2}\overline P(a_1,-a_1)
=
-a_1^2[\mathfrak L_{Y,3}(m)].
\]

Thus quotient-horizontal merger requires
\[
\mathfrak L_{Y,3}(m)=0
\quad\text{in}\quad
V_m.
\]

No current stated mechanism forces this.

---

# 5. Exact theorem needed

The missing theorem is stronger than ordinary \(Y\)-middle parity and stronger than homogeneous source-frame telescoping.

It should be stated as:

\[
\boxed{
\text{nonlinear mixed-block promoted-\((1,1)\) line-gauge theorem.}
}
\]

One theorem-ready form:

```latex
\begin{theorem}[Promoted nonlinear mixed-block line-gauge]
\label{thm:promoted-nonlinear-mixed-block-line-gauge}
Let
\[
Y_{12}^{(2)}
:=
D^2N_0[\xi_1,\xi_2]
\]
be the \(\mathcal K\)-degree \(2\), source-bidegree \((1,1)\)
Taylor remainder of the actual corrected mixed block
\(N^{\corr}(d_-,d_+,\eta)\).  Let \(A_-\) and \(B_+\) denote arbitrary
\(\mathcal K\)-linear same-point whitening source inputs of homogeneous
ordinary order compatible with total order \(7\).  Then
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+]
\right)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently, the promoted \((1,1)\) nonlinear mixed-block remainder
contributes a double balanced zero in
\[
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
\end{theorem}
```

A broader theorem covering the \(P_\pm\) terms too:

```latex
\begin{theorem}[Nonlinear actual-source double-balanced divisibility]
\label{thm:nonlinear-actual-source-double-balanced-divisibility}
For every \(\mathcal K\)-degree \(\ge2\) actual-source remainder \(R\)
entering \(G_-^{\corr},N^{\corr},G_+^{\corr}\) through ordinary order \(7\),
the contribution of \(R\) to the projected fixed-sector first-collision
polynomial satisfies
\[
\overline P_{7,m}^{R}(a_1,a_2)
\in
(a_1+a_2)^2
\left(
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)
\right)[a_1,a_2].
\]
\end{theorem}
```

But the first theorem is the immediate local target; the second is the desired global package statement.

---

# 6. Current status

\[
\boxed{
\text{Actual-source double-balanced divisibility remains open.}
}
\]

The earliest live carrier is:

\[
\boxed{
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+].
}
\]

This component passes Gate B’s simple balanced test but can fail Bottleneck C’s weighted derivative test. To kill it, the paper needs a new line-gauge theorem for **promoted nonlinear mixed-block \((1,1)\) remainders**.
## User (2026-04-25 10:29:24)

Read and do your next agent prompt (according to your agent number)

## Assistant (2026-04-25 10:30:18)

_Thought for 52s_

## Agent 4 result — degree-three promoted \(Y_{12}^{(2)}\) carrier

I **cannot prove** actual-source double-balanced divisibility for the degree-three promoted nonlinear mixed-block carrier. The obstruction reduces exactly to one quotient class
\[
E_{A,Y}^q\in V_m
:=
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

The next prompt identifies this as Agent 4’s target: the first live level is the promoted nonlinear mixed-block degree-three contribution, and Bottleneck C reduces to proving that this contribution is zero in \(V_m\). 

---

# 1. The promoted \(Y_{12}^{(2)}\) edge polynomial

Let
\[
Y_{12}^{(2)}
=
D^2N_0[\xi_1,\xi_2]
\]
be the \(\mathcal K^2\), source-bidegree \((1,1)\) nonlinear mixed-block Taylor remainder. In Hessian-block notation,

\[
Y_{12}^{(2)}
=
\sum_{\alpha,\beta\in\{d_-,d_+,\eta\}}
D^2_{\alpha\beta}N_0[
\xi_{1,\alpha},\xi_{2,\beta}
].
\]

So it includes the \(dd\), \(d\eta\), \(\eta d\), and \(\eta\eta\) second-variation pieces:

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

The degree-three promoted contribution is obtained by coupling this \((1,1)\) middle block to one same-point linear whitening slot:

\[
\mathcal E_{A,Y}
:=
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+].
\]

After ordinary-order extraction, the precise fixed-sector representative is

\[
E_{A,Y}(m)
:=
[z^7][\delta^1]\,
\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,Y_{12}^{(2)}\,R_0
+
L_0\,Y_{12}^{(2)}\,D(G_+^{-1/2})[B_+]
\right).
\]

The quotient obstruction is

\[
\boxed{
E_{A,Y}^q(m):=[E_{A,Y}(m)]\in
V_m.
}
\]

Equivalently, on the good determinant patch, if

\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
E_{A,Y}=e_{A,Y}I+f_{A,Y}S,
\]
then

\[
E_{A,Y}^q=0
\quad\Longleftrightarrow\quad
e_{A,Y}v_5-u_5f_{A,Y}=0.
\]

---

# 2. Amplitude factor and balanced derivative

The quadratic mixed block contributes the cross amplitude \(a_1a_2\). The same-point linear whitening slot contributes \(a_1+a_2\). Therefore the promoted degree-three edge polynomial has the form

\[
P_{A,Y}(a_1,a_2)
=
a_1a_2(a_1+a_2)\,E_{A,Y}^q
\in
V_m[a_1,a_2].
\]

At the balanced diagonal,

\[
P_{A,Y}(a_1,-a_1)=0.
\]

So this channel passes Gate B’s simple balanced test.

But

\[
\partial_{a_2}
\left(
a_1a_2(a_1+a_2)
\right)
=
a_1^2+2a_1a_2,
\]
hence

\[
\partial_{a_2}
\left(
a_1a_2(a_1+a_2)
\right)\bigg|_{a_2=-a_1}
=
-a_1^2.
\]

Thus Bottleneck C sees

\[
\partial_{a_2}P_{A,Y}(a_1,-a_1)
=
-a_1^2E_{A,Y}^q.
\]

Therefore:

\[
\boxed{
\text{Bottleneck C closes for this channel}
\iff
E_{A,Y}^q=0
\iff
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m).
}
\]

This is the single condition requested in the prompt. 

---

# 3. Which \(Y_{12}^{(2)}\) terms can contribute to \(z^7\)

Decompose each Hessian block by ordinary order:

\[
Y_{\alpha\beta}^{(2)}
=
\sum_g Y_{\alpha\beta}^{(2,g)}.
\]

Let the same-point linear whitening slot have ordinary order \(r\). Then a term contributes to \([z^7]\) precisely when

\[
r+g=7.
\]

Thus the possible contributing families are:

\[
D(G_-^{-1/2})[A_-^{[r]}]\,
Y_{\alpha\beta}^{(2,g)}\,R_0,
\qquad
r+g=7,
\]

and

\[
L_0\,Y_{\alpha\beta}^{(2,g)}\,
D(G_+^{-1/2})[B_+^{[r]}],
\qquad
r+g=7.
\]

No degree reason removes the \(dd\), \(d\eta\), \(\eta d\), or \(\eta\eta\) Hessian blocks in general. They are live unless one of the following holds for the actual formula:

\[
Y_{\alpha\beta}^{(2,g)}=0,
\]
or its promoted fixed-sector projection is zero, or it is line-gauge relative to \(A_5^{\mathfrak f}\).

The current prompt explicitly says this promoted \(Y_{12}^{(2)}\) channel is the remaining first live actual-source carrier, not an already-removed family. 

---

# 4. Structural identities checked

## Endpoint swap

Endpoint swap gives, at best,

\[
\left(Y_{12}^{(2)}(h_-,h_+)\right)^T
=
Y_{21}^{(2)}(h_+,h_-).
\]

After adding the left- and right-whitening promoted terms, this tends to make the total expression transpose-compatible:

\[
\mathcal E_{A,Y}^T
\sim
\mathcal E_{A,Y}.
\]

That is **not** a vanishing mechanism. Since \(\pi_{\mathfrak f}\) is transpose-invariant and \(\mathfrak f_m\) contains symmetric fixed-sector directions, self-transpose behavior survives projection.

Endpoint swap would kill the term only if it produced a minus sign:

\[
\mathcal E_{A,Y}^T=-\mathcal E_{A,Y}
\]
before fixed-sector projection. The promoted quadratic mixed block has no such forced sign.

## Transpose fixed-sector projection

Transpose projection kills skew-transpose components. The promoted channel is not forced to be skew-transpose. Instead, the left/right pair is naturally transpose-paired:

\[
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0
\quad\leftrightarrow\quad
L_0Y_{21}^{(2)}D(G_+^{-1/2})[B_+].
\]

So transpose projection does not force

\[
E_{A,Y}=0
\]
or

\[
E_{A,Y}\in \mathbf C A_5^{\mathfrak f}.
\]

## \(Y\)-middle parity

The known \(Y\)-middle parity target concerns source-linear middle blocks:

\[
Y_g(h_-,h_+)^T=(-1)^gY_g(h_+,h_-).
\]

But \(Y_{12}^{(2)}\) is source-quadratic. Even if a quadratic analogue holds, it gives parity under endpoint exchange; it does not imply the determinant-line condition

\[
\omega_m(E_{A,Y},A_5^{\mathfrak f})=0.
\]

So \(Y\)-middle parity is relevant, but insufficient by itself.

## Self-adjointness / skew-adjointness of \(D^2N_0\)

If

\[
D^2N_0[\xi_1,\xi_2]^T
=
D^2N_0[\xi_2,\xi_1],
\]
then the promoted pair is self-adjoint after endpoint swap. Again, self-adjointness is not line-gauge.

If it were skew-adjoint, fixed-sector projection could kill it. But the actual mixed block transpose functoriality points to symmetry, not skew-symmetry. The connection prompt explicitly expects transpose functoriality of \(N^{\corr}\), not skew transpose. 

## Direct line-gauge relation with \(A_5^{\mathfrak f}\)

The line-gauge condition is one scalar equation:

\[
\omega_m(E_{A,Y},A_5^{\mathfrak f})=0.
\]

No current source functoriality statement implies this. It would require a genuine second-variation identity tying the promoted Hessian of \(N^{\corr}\) to the quintic fixed-sector line \(A_5^{\mathfrak f}\). I do not see such an identity in the current attack state.

---

# 5. Concrete quotient obstruction

The obstruction class is:

\[
\boxed{
E_{A,Y}^q(m)
=
\left[
[z^7][\delta^1]\,
\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,D^2N_0[\xi_1,\xi_2]\,R_0
+
L_0\,D^2N_0[\xi_1,\xi_2]\,D(G_+^{-1/2})[B_+]
\right)
\right].
}
\]

Equivalently, after Hessian-block decomposition,

\[
E_{A,Y}^q
=
\sum_{\alpha,\beta\in\{d_-,d_+,\eta\}}
\left[
[z^7][\delta^1]\,
\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-]\,
D^2_{\alpha\beta}N_0[
\xi_{1,\alpha},\xi_{2,\beta}
]\,R_0
+
L_0\,
D^2_{\alpha\beta}N_0[
\xi_{1,\alpha},\xi_{2,\beta}
]\,
D(G_+^{-1/2})[B_+]
\right)
\right].
\]

Bottleneck C for this carrier is exactly

\[
\boxed{
E_{A,Y}^q=0.
}
\]

If

\[
E_{A,Y}^q\neq0,
\]
then the promoted nonlinear mixed-block channel contributes

\[
-a_1^2E_{A,Y}^q
\]
to the exceptional \(\kappa\)-slope, and actual-source double-balanced divisibility fails.

---

# 6. Final classification

For the degree-three promoted nonlinear mixed-block carrier:

| Candidate mechanism | Result |
|---|---|
| Balanced amplitude relation | Only simple zero |
| Source-bidegree projection | Does not remove promoted \((2,1)\oplus(1,2)\) |
| Endpoint swap | Gives transpose pairing, not line-gauge |
| Transpose fixed-sector projection | Does not kill self-transpose fixed-sector terms |
| \(Y\)-middle parity | Source-linear; insufficient for quadratic promoted term |
| Self-adjointness of \(D^2N_0\) | Not line-gauge |
| Same-reduced-image functoriality | Would solve it, but is exactly missing |

So the attack result is:

\[
\boxed{
\text{actual-source double-balanced divisibility remains open at }E_{A,Y}^q.
}
\]

The exact missing theorem is:

\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}(m).
}
\]

A theorem-ready statement is:

```latex
\begin{theorem}[Promoted quadratic mixed-block double-balanced line-gauge]
\label{thm:promoted-quadratic-mixed-block-double-balanced-line-gauge}
Let
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]
\]
be the source-bidegree \((1,1)\), \(\mathcal K^2\) nonlinear Taylor
remainder of the actual corrected mixed block.  Then, for every ordinary
order decomposition \(r+g=7\),
\[
[z^7][\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
D(G_-^{-1/2})[A_-^{[r]}]Y_{12}^{(2,g)}R_0
+
L_0Y_{12}^{(2,g)}D(G_+^{-1/2})[B_+^{[r]}]
\right)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently, the promoted quadratic mixed-block contribution has a double
balanced zero in
\[
\left(\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)\right)[a_1,a_2].
\]
\end{theorem}
```

Until this theorem is proved, the first concrete obstruction remains

\[
\boxed{
E_{A,Y}^q
=
\left[
[z^7][\delta^1]\pi_{\mathfrak f}
\bigl(
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0
+
L_0Y_{12}^{(2)}D(G_+^{-1/2})[B_+]
\bigr)
\right].
}
\]
## User (2026-04-25 10:42:12)

Do your agent prompt, according to your agent number

## Assistant (2026-04-25 10:42:29)

_Thought for 15s_

## Agent 4 result — scalar classification of \(E_{A,Y}\)

The stronger augmented-package condition is **not** implied by quotient Bottleneck C.

The current first live actual-source carrier is still
\[
E_{A,Y}
=
[z^7][\delta^1]\pi_{\mathfrak f}
\left(
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0
+
L_0Y_{12}^{(2)}D(G_+^{-1/2})[B_+]
\right),
\]
where
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2].
\]
The prompt explicitly marks this as the first live actual-source / Bottleneck C carrier and says quotient closure requires \(E_{A,Y}^q=0\), while the transform-safe augmented package requires the stronger scalar condition \(\Phi_K(E_{A,Y})=0\). 

---

# 1. Fixed-sector coordinates

Write
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
E_{A,Y}=eI+fS.
\]

Then
\[
\boxed{\Phi_K(E_{A,Y})=2f.}
\]

The quotient obstruction is the determinant class
\[
E_{A,Y}^q=0
\quad\Longleftrightarrow\quad
e v_5-u_5 f=0.
\]

So the two tests are different:

\[
\boxed{
\text{quotient Bottleneck C: }e v_5-u_5 f=0,
}
\]
but
\[
\boxed{
\text{transform-safe Bottleneck C: }f=0.
}
\]

On the generic \(v_5\neq0\) patch, quotient closure plus transform-safety forces
\[
E_{A,Y}=0.
\]

Indeed, if
\[
e v_5-u_5f=0
\]
and
\[
f=0,
\]
then
\[
e v_5=0,
\]
so \(e=0\) when \(v_5\neq0\).

---

# 2. Three-case classification

## Case A: \(E_{A,Y}=0\)

Then
\[
E_{A,Y}^q=0
\]
and
\[
\Phi_K(E_{A,Y})=0.
\]

So both quotient diagonal merger and \(T\)-horizontal merger close for this carrier.

\[
\boxed{
E_{A,Y}=0
\quad\Longrightarrow\quad
\text{quotient-safe and transform-safe.}
}
\]

---

## Case B: \(E_{A,Y}\in\mathbf C A_5^{\mathfrak f}\setminus\{0\}\)

Write
\[
E_{A,Y}=\lambda A_5^{\mathfrak f}
=
\lambda u_5I+\lambda v_5S.
\]

Then
\[
e=\lambda u_5,
\qquad
f=\lambda v_5.
\]

The quotient determinant vanishes:
\[
e v_5-u_5f
=
\lambda u_5v_5-u_5\lambda v_5
=
0.
\]

So quotient Bottleneck C closes.

But
\[
\Phi_K(E_{A,Y})
=
2f
=
2\lambda v_5.
\]

Therefore, on the generic \(v_5\neq0\) patch,
\[
\Phi_K(E_{A,Y})=0
\quad\Longleftrightarrow\quad
\lambda=0.
\]

Thus a nonzero line-gauge \(E_{A,Y}\) is quotient-invisible but transform-visible.

\[
\boxed{
E_{A,Y}=\lambda A_5^{\mathfrak f},\ \lambda\neq0,\ v_5\neq0
\quad\Longrightarrow\quad
\text{quotient-safe but \(T\)-leaking.}
}
\]

This matches the shared warning that a line-gauge exceptional slope changes \(T\) by \(\lambda v_5/c\). 

---

## Case C: \(E_{A,Y}^q\neq0\)

Equivalently,
\[
e v_5-u_5f\neq0.
\]

Then quotient Bottleneck C already fails. Whether \(\Phi_K(E_{A,Y})\) vanishes is irrelevant to quotient merger, although it still matters for the two-point scalar transform.

There is a subcase:

\[
f=0,\qquad e v_5\neq0.
\]

Then
\[
\Phi_K(E_{A,Y})=0
\]
but
\[
E_{A,Y}^q\neq0.
\]

So \(T\)-horizontal closure does not imply quotient closure either.

\[
\boxed{
\Phi_K(E_{A,Y})=0
\not\Longrightarrow
E_{A,Y}^q=0.
}
\]

---

# 3. Induced \(T\)-slope

The promoted carrier has amplitude factor
\[
a_1a_2(a_1+a_2),
\]
so
\[
\partial_{a_2}\bigl(a_1a_2(a_1+a_2)\bigr)\bigg|_{a_2=-a_1}
=
-a_1^2.
\]

The scalar transform-visible slope is therefore
\[
\partial_\kappa T
=
-a_1^2\frac{\Phi_K(E_{A,Y})}{2c}
=
-a_1^2\frac{f}{c}.
\]

If \(E_{A,Y}\) is line-gauge,
\[
E_{A,Y}=\lambda A_5^{\mathfrak f},
\]
then
\[
f=\lambda v_5,
\]
so
\[
\boxed{
\partial_\kappa T
=
-a_1^2\lambda\frac{v_5}{c}.
}
\]

Therefore:

\[
\boxed{
\partial_\kappa T=0
\quad\Longleftrightarrow\quad
f=0.
}
\]

On the generic \(v_5\neq0\) line-gauge patch:

\[
\boxed{
\partial_\kappa T=0
\quad\Longleftrightarrow\quad
\lambda=0
\quad\Longleftrightarrow\quad
E_{A,Y}=0.
}
\]

---

# 4. What available identities can prove

The available structural identities can at most plausibly prove one of these:

\[
E_{A,Y}^q=0,
\qquad\text{or}\qquad
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}.
\]

That is enough for quotient Bottleneck C.

But for the augmented package
\[
\widehat\Psi_{\rm red}^{+}
=
(\widehat\Psi_{\rm red},T),
\qquad
T=\frac{v_7}{c},
\]
the needed condition is
\[
\Phi_K(E_{A,Y})=0.
\]

Since
\[
\Phi_K(A_5^{\mathfrak f})=2v_5,
\]
line-gauge is not enough on \(v_5\neq0\). The shared background states the same obstruction: quotient merger controls \(\Delta_7\), not \(T\), and a line-gauge exceptional slope is quotient-invisible but changes \(T\). 

Thus the missing identity is stronger:

\[
\boxed{
E_{A,Y}=0
\quad\text{on the generic }v_5\neq0\text{ patch}.
}
\]

A theorem proving only
\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\]
would close quotient Bottleneck C but leave the two-point transform bridge open.

---

# 5. Final scalar classification

Let
\[
E_{A,Y}=eI+fS.
\]

| Condition on \(E_{A,Y}\) | Quotient Bottleneck C | \(T\)-horizontal merger |
|---|---:|---:|
| \(E_{A,Y}=0\) | closes | closes |
| \(e v_5-u_5f=0\), \(f\neq0\) | closes | fails |
| \(e v_5-u_5f\neq0\), \(f=0\) | fails | closes |
| \(e v_5-u_5f\neq0\), \(f\neq0\) | fails | fails |

The first transform-visible leakage carrier is therefore

\[
\boxed{
f_{A,Y}
=
\frac12\Phi_K(E_{A,Y}).
}
\]

The exact induced hidden-state slope is

\[
\boxed{
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
}
\]

So the strengthened theorem needed for the augmented package is:

```latex
\begin{theorem}[Transform-safe promoted quadratic mixed-block cancellation]
\label{thm:transform-safe-promoted-quadratic-mixed-block-cancellation}
For the promoted quadratic mixed-block carrier
\[
E_{A,Y}
=
[z^7][\delta^1]\pi_{\mathfrak f}
\left(
D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0
+
L_0Y_{12}^{(2)}D(G_+^{-1/2})[B_+]
\right),
\]
one has
\[
\Phi_K(E_{A,Y})=0.
\]
Equivalently, if
\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S,
\]
then
\[
f_{A,Y}=0.
\]
On the generic \(v_5\ne0\) patch, if quotient line-gauge
\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\]
is also known, this is equivalent to
\[
E_{A,Y}=0.
\]
\end{theorem}
```

Current status:

\[
\boxed{
\text{quotient line-gauge is insufficient for the augmented package.}
}
\]

\[
\boxed{
\text{the scalar obstruction is }f_{A,Y},\text{ the }S\text{-coefficient of }E_{A,Y}.}
}
\]
## User (2026-04-25 10:49:39)

Please do this instruction according to your agent number.

## Assistant (2026-04-25 10:49:47)

_Thought for 5s_

## Agent 4 — scalar and quotient tests for \(E_{A,Y}\)

The current instruction assigns Agent 4 to **Prompt B: scalar and quotient tests**. The input is a future or external Agent 1 computation
\[
E_{A,Y}=eI+fS,
\]
and the tests are
\[
ev_5-u_5f=0,
\qquad
f=0.
\]
This matches the consolidated frontier: \(E_{A,Y}\) is the main local obstruction, and Agent 4’s role is to decide whether it is quotient-visible, line-gauge but \(\Phi_K\)-visible, or transform-safe. 

---

# 1. Scalar tests

Let
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
E_{A,Y}=eI+fS.
\]

The quotient determinant is
\[
\omega(E_{A,Y},A_5^{\mathfrak f})
=
ev_5-u_5f.
\]

Thus
\[
E_{A,Y}^q=0
\quad\Longleftrightarrow\quad
ev_5-u_5f=0.
\]

The \(\Phi_K\)-visible scalar is
\[
\Phi_K(E_{A,Y})=2f.
\]

Thus
\[
\Phi_K(E_{A,Y})=0
\quad\Longleftrightarrow\quad
f=0.
\]

So the two conditions are independent:

\[
\boxed{
\text{quotient closure} \iff ev_5-u_5f=0,
}
\]
while
\[
\boxed{
\text{transform-safe closure} \iff f=0.
}
\]

---

# 2. Classification table

On the generic \(v_5\neq0\) patch:

| Case | Conditions | Classification |
|---|---|---|
| \(E_{A,Y}=0\) | \(e=0,\ f=0\) | zero; quotient-safe and transform-safe |
| quotient-visible | \(ev_5-u_5f\neq0\) | quotient Bottleneck C fails |
| line-gauge but \(\Phi_K\)-visible | \(ev_5-u_5f=0,\ f\neq0\) | quotient-safe, but \(T\)-leaking |
| transform-safe but quotient-visible | \(f=0,\ ev_5\neq0\) | \(T\)-safe, but quotient Bottleneck C fails |

The important nonzero line-gauge case is:
\[
E_{A,Y}=\lambda A_5^{\mathfrak f}.
\]
Then
\[
e=\lambda u_5,
\qquad
f=\lambda v_5,
\]
so
\[
ev_5-u_5f=0,
\]
but
\[
\Phi_K(E_{A,Y})=2\lambda v_5.
\]

Hence, if \(v_5\neq0\),
\[
\Phi_K(E_{A,Y})=0
\quad\Longleftrightarrow\quad
\lambda=0.
\]

Therefore:

\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\text{ is not enough for the augmented package.}
}
\]

On the generic \(v_5\neq0\) patch, quotient closure plus transform-safe closure forces
\[
E_{A,Y}=0.
\]

---

# 3. \(T\)-slope

The promoted \(Y_{12}^{(2)}\) carrier has amplitude factor
\[
a_1a_2(a_1+a_2).
\]

Since
\[
\partial_{a_2}
\bigl(a_1a_2(a_1+a_2)\bigr)
=
a_1^2+2a_1a_2,
\]
we get
\[
\partial_{a_2}
\bigl(a_1a_2(a_1+a_2)\bigr)\big|_{a_2=-a_1}
=
-a_1^2.
\]

Thus the induced hidden-state slope is
\[
\partial_\kappa T
=
-a_1^2\frac{\Phi_K(E_{A,Y})}{2c}
=
-a_1^2\frac{f}{c}.
\]

If
\[
E_{A,Y}=\lambda A_5^{\mathfrak f},
\]
then
\[
f=\lambda v_5,
\]
so
\[
\partial_\kappa T
=
-a_1^2\lambda\frac{v_5}{c}.
\]

Therefore, on the \(v_5\neq0\) patch,
\[
\boxed{
\partial_\kappa T=0
\quad\Longleftrightarrow\quad
f=0,
}
\]
and if line-gauge is already known,
\[
\boxed{
\partial_\kappa T=0
\quad\Longleftrightarrow\quad
E_{A,Y}=0.
}
\]

---

# 4. The theorem actually needed

The quotient theorem is:

```latex
\[
ev_5-u_5f=0.
\]
```

But the augmented transform-safe theorem is stronger:

```latex
\[
f=0.
\]
```

Equivalently:

```latex
\begin{theorem}[Transform-safe scalar cancellation for \(E_{A,Y}\)]
\label{thm:transform-safe-scalar-cancellation-eay}
Let
\[
E_{A,Y}=eI+fS.
\]
Then the promoted quadratic mixed-block carrier is transform-safe if and only if
\[
f=0.
\]
Equivalently,
\[
\Phi_K(E_{A,Y})=0.
\]
On the generic \(v_5\neq0\) patch, if quotient line-gauge
\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\]
is also known, this is equivalent to
\[
E_{A,Y}=0.
\]
\end{theorem}
```

Current status:

\[
\boxed{
\text{Without Agent 1's explicit }(e,f)\text{ table, Agent 4 can only classify conditionally.}
}
\]

Once \(E_{A,Y}=eI+fS\) is computed, the classification is immediate by the two scalars:
\[
\boxed{ev_5-u_5f}
\qquad\text{and}\qquad
\boxed{f}.
\]
## User (2026-04-25 10:58:22)

Do these instructions per your agent number

## Assistant (2026-04-25 10:58:32)

_Thought for 6s_

## Agent 4 — quotient and scalar tests for \(E_{A,Y}\)

The current Agent 4 instruction is conditional on Agent 1 producing
\[
E_{A,Y}=eI+fS.
\]
Until \(e,f\) are computed, the best possible result is the decisive scalar reduction. The attached command states that the local problem has collapsed to computing or controlling exactly:
\[
e_{A,Y}v_5-u_5f_{A,Y},
\qquad
f_{A,Y}.
\]
It also gives the induced \(T\)-slope formula for this carrier. 

---

# 1. Two decisive tests

Let
\[
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
E_{A,Y}=eI+fS.
\]

The quotient obstruction is
\[
Q_{A,Y}:=\omega(E_{A,Y},A_5^{\mathfrak f})
=ev_5-u_5f.
\]

Therefore
\[
\boxed{
E_{A,Y}^q=0
\Longleftrightarrow
Q_{A,Y}=ev_5-u_5f=0.
}
\]

The transform-visible scalar is
\[
\Phi_K(E_{A,Y})=2f.
\]

Therefore
\[
\boxed{
\Phi_K(E_{A,Y})=0
\Longleftrightarrow
f=0.
}
\]

Thus quotient Bottleneck C and augmented \(T\)-horizontal Bottleneck C are logically distinct.

---

# 2. Classification

Given \(E_{A,Y}=eI+fS\), classify as follows.

## Case 1: fully safe

\[
e=0,\qquad f=0.
\]

Then
\[
Q_{A,Y}=0,
\qquad
\Phi_K(E_{A,Y})=0.
\]

So both quotient merger and \(T\)-horizontal merger close.

\[
\boxed{
E_{A,Y}=0
\Rightarrow
\text{fully safe.}
}
\]

---

## Case 2: quotient-visible

\[
Q_{A,Y}=ev_5-u_5f\neq0.
\]

Then quotient Bottleneck C fails.

Even if \(f=0\), the quotient obstruction remains:
\[
Q_{A,Y}=ev_5.
\]

So
\[
\boxed{
Q_{A,Y}\neq0
\Rightarrow
\text{quotient Bottleneck C fails.}
}
\]

---

## Case 3: line-gauge but \(\Phi_K\)-visible

\[
Q_{A,Y}=0,
\qquad
f\neq0.
\]

Then
\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f},
\]
but
\[
\Phi_K(E_{A,Y})=2f\neq0.
\]

This closes quotient Bottleneck C but leaks through the augmented hidden coordinate \(T\).

Equivalently, write
\[
E_{A,Y}=\lambda A_5^{\mathfrak f}.
\]
Then
\[
e=\lambda u_5,
\qquad
f=\lambda v_5.
\]

So
\[
Q_{A,Y}=0,
\]
but
\[
\Phi_K(E_{A,Y})=2\lambda v_5.
\]

On the generic \(v_5\neq0\) patch, this vanishes only if
\[
\lambda=0.
\]

Thus
\[
\boxed{
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\text{ is not enough for the augmented package.}
}
\]

---

## Case 4: \(T\)-safe but quotient-visible

\[
f=0,
\qquad
Q_{A,Y}=ev_5\neq0.
\]

Then
\[
\Phi_K(E_{A,Y})=0,
\]
but quotient Bottleneck C fails.

So
\[
\boxed{
T\text{-horizontal closure does not imply quotient closure.}
}
\]

---

# 3. Induced \(T\)-slope

The dangerous amplitude factor is
\[
a_1a_2(a_1+a_2).
\]

Since
\[
\partial_{a_2}\bigl(a_1a_2(a_1+a_2)\bigr)
=
a_1^2+2a_1a_2,
\]
we get
\[
\partial_{a_2}\bigl(a_1a_2(a_1+a_2)\bigr)\big|_{a_2=-a_1}
=
-a_1^2.
\]

Therefore
\[
\partial_\kappa T
=
-a_1^2\frac{\Phi_K(E_{A,Y})}{2c}
=
-a_1^2\frac{f}{c}.
\]

If
\[
E_{A,Y}=\lambda A_5^{\mathfrak f},
\]
then
\[
f=\lambda v_5,
\]
and hence
\[
\boxed{
\partial_\kappa T
=
-a_1^2\lambda\frac{v_5}{c}.
}
\]

So on the generic \(v_5\neq0\) patch:
\[
\boxed{
\partial_\kappa T=0
\Longleftrightarrow
f=0.
}
\]

If line-gauge is also known, then:
\[
\boxed{
\partial_\kappa T=0
\Longleftrightarrow
E_{A,Y}=0.
}
\]

---

# 4. What the augmented package requires

The quotient package only needs:
\[
ev_5-u_5f=0.
\]

The transform-safe augmented package needs:
\[
f=0.
\]

On the generic \(v_5\neq0\) patch, proving both requires:
\[
E_{A,Y}=0.
\]

Therefore the correct target is stronger than line-gauge:

\[
\boxed{
\text{Augmented Bottleneck C requires full vanishing of }E_{A,Y}
\text{ on the generic line-gauge patch.}
}
\]

The theorem-ready form is:

```latex
\begin{theorem}[Augmented safety test for the promoted mixed-block carrier]
\label{thm:augmented-safety-test-eay}
Let
\[
E_{A,Y}=eI+fS,
\qquad
A_5^{\mathfrak f}=u_5I+v_5S.
\]
Then quotient Bottleneck C for the promoted quadratic mixed-block carrier is
equivalent to
\[
ev_5-u_5f=0.
\]
The augmented \(T\)-horizontal condition is equivalent to
\[
f=0.
\]
Consequently, on the generic \(v_5\ne0\) patch, quotient closure together
with \(T\)-horizontal closure is equivalent to
\[
E_{A,Y}=0.
\]
\end{theorem}
```

Current status:

\[
\boxed{
\text{Agent 4 is blocked only on the explicit Agent 1 computation of }(e,f).
}
\]

Once \(e,f\) are known, the classification is immediate.
