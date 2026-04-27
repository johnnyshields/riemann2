# Adversarial Implication Testing

- Source: https://chatgpt.com/c/69ec89a0-922c-83e8-a20f-752465ef5227
- Created: 2026-04-25 09:31:21 UTC
- Default model: gpt-5-5-thinking

---

## User (2026-04-25 09:31:19)

YOUR TASK: You are Agent 8

Agent 8 — adversarial consistency / no-go model builder

This is valuable because many false RH attempts die from formal implications that are not actually valid.

You are the adversarial model-checking agent.

Work only from the latest draft.

Target:
Find formal countermodels to any claimed implication that is not forced by the stated hypotheses.

Test the following implications:
1. Gate B hypotheses imply actual corrected source-package edge divisibility.
2. Quotient package equality implies \(\Phi_K\)-visible hidden-state equality.
3. Analyticity plus swap-evenness implies \(\kappa\)-independence of the exceptional-divisor trace.
4. Local \(Z_j\)-connection cancellation implies global package-to-transform closure.
5. Pair-like asymptotic exclusion implies finite-core exclusion.
6. Good-patch determinant scalarization extends across \(A_5^{\mathfrak f}=0\).

For each implication:
- either prove it from draft assumptions;
- or give a small formal model showing it fails;
- or state the missing hypothesis precisely.

Output:
A table of “valid / invalid / unknown” implications and exact LaTeX warnings or theorem-obligation remarks.

---

Now, do your task as per above.

## Assistant (2026-04-25 09:31:21)

I’ll treat the TeX draft as the controlling source and run this as an adversarial implication audit, not as an attempt to improve the main proof. I’ll look for places where the draft’s hypotheses are weaker than the claimed downstream conclusion.

I found the draft already contains several guardrail remarks around these six implications. The useful contribution here is to sharpen them into formal countermodels and “do not infer” theorem-obligation language, rather than adding more coefficient work.

_Thought for 2m 3s_

Agent 8 verdict: most of the dangerous implications are **already warned against in the draft**, but they should be made into a single adversarial ledger so future agents do not silently promote conditional/local statements into global ones. This is consistent with the current draft posture: Gate B is conditional through order 7, determinant scalarization is only good-patch bookkeeping, quotient equality does not imply hidden-state equality, and the current endgame remains asymptotic/pair-like rather than full finite-core RH closure. L126-L179 L201-L237 L373-L411 L490-L512

## Adversarial implication table

| # | Claimed implication | Verdict | Formal model / reason | Missing hypothesis |
|---:|---|---|---|---|
| 1 | Gate B hypotheses imply actual corrected source-package edge divisibility | **Unknown as stated; conditionally valid only in the narrow Gate-B corollary** | The draft proves the fixed-sector order-7 raw coefficient vanishes if the listed parity/source-frame/full-tower hypotheses are imposed. But that does not itself prove the actual corrected source package satisfies those hypotheses, nor does it prove all-order or unprojected edge divisibility. Formal failure model: take the audited Gate-B formal package \(C_0\) with \(F_1(C_0)=0\), and add an unmodelled admissible source component \(a_1\delta z^7U\) not controlled by the homogeneous source theorem. Then \(F_1(C_0+a_1\delta z^7U)=U\). | Actual-source realization/completeness theorem: every admissible corrected source term must be represented in the homogeneous moving Taylor tower with the stated midpoint/Y/source-frame hypotheses. |
| 2 | Quotient package equality implies \(\Phi_K\)-visible hidden-state equality | **Invalid** | Let \(\mathfrak f=\mathbf C I\oplus \mathbf C S\), \(A_5^{\mathfrak f}=S\), and \(\Phi_K(uI+vS)=2v\). Then \(0\) and \(S\) are equal in \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\), but \(\Phi_K(0)=0\) and \(\Phi_K(S)=2\). | State-locality modulo \(\ker\Phi_K\), or \(A_5^{\mathfrak f}\in\ker\Phi_K\), i.e. \(v_5=0\), or actual transform-level cancellation of the forgotten affine line. |
| 3 | Analyticity plus swap-evenness implies \(\kappa\)-independence of exceptional-divisor trace | **Invalid** | In blow-up variables \(\kappa=2\omega/\delta\), set \(B(m,\kappa)=B_0(m)+\varepsilon\kappa\). Then \(E(m,\omega,\delta)=\delta^2B(m,2\omega/\delta)=\delta^2B_0+2\varepsilon\omega\delta\) is analytic and swap-even under \((\omega,\delta)\mapsto(-\omega,-\delta)\), but \(\partial_\kappa B=\varepsilon\ne0\). | Diagonal merger, same-reduced-image theorem, or collision functoriality of the corrected two-atom package. |
| 4 | Local \(Z_j\)-connection cancellation implies global package-to-transform closure | **Invalid as a formal implication** | Let local package data be \((Q,H)\), where \(Q\) is the quotient package and \(H\) is a hidden transform state. The \(Z_j\)-connection identities can set \(Q=0\), while the transform reads \(T(Q,H)=H\). Choosing \(H\ne0\) gives local connection closure but global transform failure. | Package-to-\(\Xi_\zeta^{(N)}\) bridge / hidden-state theorem proving the transform sees only the corrected package data, or that the hidden state is killed modulo \(\ker\Phi_K\). |
| 5 | Pair-like asymptotic exclusion implies finite-core exclusion | **Invalid** | Pair-like branch excludes a first-odd coefficient model \(a_1u^2+\cdots\) with \(a_1\ne0\). A finite-core model \(F_{\core}(z)=b z^9+O(z^{11})\) has first odd coefficient zero but a genuine higher odd anomaly. The pair-like contradiction never sees it. | Finite-core lower-model transfer theorem for the first nonzero odd coefficient, e.g. control of \(\Xi_{\core}^{(N)}\). |
| 6 | Good-patch determinant scalarization extends across \(A_5^{\mathfrak f}=0\) | **Invalid** | Let \(A_5^{\mathfrak f}(t)=tS\). For \(t\ne0\), \(\mathfrak f/\mathbf C(tS)\) is one-dimensional and determinant scalarization works up to scale. At \(t=0\), the denominator is \(0\), so the quotient jumps to \(\mathfrak f\), dimension two. The scalar coordinate does not extend canonically. | Rank-jump exclusion, stratified quotient convention, or a blow-up/projectivized extension theorem. |

## Exact LaTeX insertion

Place this after:

```tex
\begin{remark}[Shortcut routes excluded for the corrected package theorem]
\label{rem:shortcut-routes-excluded-current-package-theorem}
...
\end{remark}
```

Add:

```tex
\begin{remark}[Adversarial implication ledger]
\label{rem:adversarial-implication-ledger}
The following formal implications are not available from the current package
definitions and should not be used as shortcuts.

\begin{enumerate}
\item \textbf{Gate B hypotheses do not automatically prove the actual source
package.}
Corollary~\ref{cor:gate-b-raw-edge-divisibility-order-seven} proves the
fixed-sector ordinary order-\(7\) raw edge coefficient vanishes under its
listed hypotheses:
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}C_{\mathcal W}^{\mathrm{raw}}=0.
\]
This is a conditional formal implication inside the homogeneous moving-source
model.  It does not by itself prove that the actual corrected source package
has no additional admissible source component outside that model, nor does it
prove all-order or unprojected edge divisibility.

A formal countermodel to the stronger reading is obtained by taking an audited
package \(C_0\) satisfying the Gate~B conclusion and adding an unmodelled
admissible edge source
\[
C_{\mathrm{bad}}=C_0+a_1\delta z^7U,
\qquad
U\in\mathfrak f_h,\quad U\ne0,
\]
not constrained by the homogeneous source-frame hypotheses.  Then the audited
Gate~B cancellation remains true for \(C_0\), but
\[
[z^7][\delta^1]\pi_{\mathfrak f_h}C_{\mathrm{bad}}=U.
\]
Thus the missing positive theorem is an actual-source realization/completeness
statement: every corrected source contribution relevant to the edge coefficient
must be represented in the homogeneous moving Taylor tower with the stated
midpoint parity, \(Y\)-middle parity, telescoping, affine-boundary, and
full-tower-before-truncation hypotheses.

\item \textbf{Quotient equality does not imply \(\Phi_K\)-visible hidden-state
equality.}
In the fixed sector write
\[
\mathfrak f=\mathbf C I\oplus\mathbf C S,
\qquad
A_5^{\mathfrak f}=u_5I+v_5S,
\qquad
\Phi_K(uI+vS)=2v.
\]
If \(v_5\ne0\), then the forgotten quotient direction
\[
A_7^{\mathfrak f}\longmapsto A_7^{\mathfrak f}+\chi A_5^{\mathfrak f}
\]
is \(\Phi_K\)-visible:
\[
\Phi_K(A_7^{\mathfrak f}+\chi A_5^{\mathfrak f})
-\Phi_K(A_7^{\mathfrak f})
=
2\chi v_5.
\]
Equivalently, in the formal model \(A_5^{\mathfrak f}=S\), the representatives
\(0\) and \(S\) define the same quotient class in
\(\mathfrak f/\mathbf C A_5^{\mathfrak f}\), but
\[
\Phi_K(0)=0,
\qquad
\Phi_K(S)=2.
\]
Therefore quotient package equality must be supplemented by a transform-level
state-locality theorem modulo \(\ker\Phi_K\), or by an actual cancellation
showing that the affine septic representative freedom is invisible to the
first \(\Phi_K\)-visible odd coefficient.

\item \textbf{Analyticity and swap-evenness do not force
\(\kappa\)-independence.}
Let \(\kappa=2\omega/\delta\) on the blown-up collision chart.  The formal
exceptional-divisor trace
\[
B(m,\kappa)=B_0(m)+\varepsilon\kappa
\]
is compatible with an analytic swap-even pre-blowup expression:
\[
E(m,\omega,\delta)
=
\delta^2 B\!\left(m,\frac{2\omega}{\delta}\right)
=
\delta^2B_0(m)+2\varepsilon\omega\delta,
\]
since
\[
E(m,-\omega,-\delta)=E(m,\omega,\delta).
\]
But
\[
\partial_\kappa B=\varepsilon.
\]
Thus analyticity, swap-evenness, fixed codomain, scalar normalization, and
the central value \(B(m,0)=\widehat\Psi(m)\) do not imply
\(\partial_\kappa B=0\).  A valid proof must supply diagonal merger,
same-reduced-image, or collision functoriality for the actual corrected
two-atom package.

\item \textbf{Local connection cancellation does not imply global
package-to-transform closure.}
The identities
\[
R_7^{(A)}+\sum_{i=1}^{7}\omega_m(Z_{7-i}[M_A],A_i)=0,
\qquad
R_7^{(C)}+\sum_{i=1}^{7}\omega_m(Z_{7-i}[M_C],A_i)=0
\]
are local quotient-line connection identities.  They do not by themselves
prove that the \(N\)-point transform sees only this local quotient package.

A formal countermodel has local data \((Q,H)\), where \(Q\) is the quotient
package coordinate and \(H\) is an independent hidden transform state.  The
connection calculation may force \(Q=0\), while the transform is
\[
\Xi(Q,H)=H.
\]
Taking \(H\ne0\) gives local connection closure with nonzero global transform
output.  Therefore the missing theorem is a package-to-\(\Xi_\zeta^{(N)}\)
state-locality or odd-block extraction theorem, proving that no hidden
\(\Phi_K\)-visible state survives beyond the corrected package data.

\item \textbf{Pair-like asymptotic exclusion does not exclude the general
finite-core branch.}
The pair-like contradiction controls a model in which the first odd corrected
coefficient is already nonzero:
\[
F_{\pair}(z)=a_1z^{2r+1}+O(z^{2r+3}),
\qquad a_1\ne0.
\]
A finite-core formal model may instead satisfy
\[
F_{\core}(z)=b z^{2R+1}+O(z^{2R+3}),
\qquad R>r,\quad b\ne0,
\]
so the first pair-like odd coefficient cancels while a genuine higher odd
anomaly remains.  Such a model is not ruled out by a theorem whose lower bound
is attached specifically to the pair-like first odd coefficient.  The missing
input is a finite-core lower-model transfer theorem for the first nonzero odd
coefficient, for example a lower law feeding \(\Xi_{\core}^{(N)}\) into the
positive-kernel \(N\)-point formula.

\item \textbf{Good-patch determinant scalarization does not extend across
\(A_5^{\mathfrak f}=0\).}
On a patch where
\[
A_5^{\mathfrak f}=u_5I+v_5S\ne0,
\]
the determinant coordinate
\[
\omega_m(C,A_5^{\mathfrak f})=uv_5-u_5v,
\qquad C=uI+vS,
\]
is a coordinate for the one-dimensional quotient
\[
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
At \(A_5^{\mathfrak f}=0\), however, the denominator line has rank zero and
the quotient jumps from one-dimensional to
\[
\mathfrak f_m/\{0\}\cong\mathfrak f_m.
\]
For example \(A_5^{\mathfrak f}(t)=tS\) gives a valid quotient coordinate for
\(t\ne0\), but no canonical one-dimensional quotient coordinate at \(t=0\).
Thus determinant tests on \(A_5^{\mathfrak f}=0\) are quotient-inconclusive
unless a separate rank-jump exclusion, stratified quotient convention, or
blow-up/projectivized extension theorem is supplied.
\end{enumerate}
\end{remark}
```

## Minimal paper-status wording to keep

I would also keep this one-sentence status warning near the final theorem or endgame status:

```tex
The local Gate~B and connection-package results are package-construction
results; they do not by themselves prove hidden-state equality, exceptional
divisor fiber selection, finite-core exclusion, or a full package-to-transform
contradiction.
```

That captures the adversarial no-go boundary cleanly.
## User (2026-04-25 09:51:56)

Updated paper draft attached.

Now, here's your next instruction. 

## Assistant (2026-04-25 09:54:04)

_Thought for 2m 7s_

## Agent 8 result: source algebra alone does **not** force diagonal merger

I cannot prove  
\[
\partial_\kappa B(m,\kappa)=0
\]
from the currently stated source-algebra mechanisms. There is a small formal model, compatible with the stated Gate-B edge divisibility shape, in which the \(\delta^{-2}\)-normalized exceptional trace has a **quotient-visible \(\kappa\)-linear survivor**.

This does not prove the actual corrected package fails. It proves the proposed mechanisms are insufficient unless the draft adds a stronger “amplitude-ratio derivative of the edge coefficient is line-gauge” lemma. The prompt’s guardrails already mark Bottleneck C as requiring actual diagonal merger / same-reduced-image / collision functoriality, not abstract symmetry.  The broader handoff likewise warns that formal properties do not force \(\partial_\kappa B=0\). 

---

# 1. Two-atom moment expansion

Use the collision chart
\[
h_1=m-\frac{\delta}{2},
\qquad
h_2=m+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta).
\]

For any scalar source moment around \(m\),
\[
M_n:=a_1(h_1-m)^n+a_2(h_2-m)^n,
\]
we get
\[
M_n
=
a_1\left(-\frac{\delta}{2}\right)^n
-a_1(1+\kappa\delta)\left(\frac{\delta}{2}\right)^n.
\]

Thus
\[
M_{2r}
=
-\frac{a_1\kappa}{2^{2r}}\delta^{2r+1},
\]
and
\[
M_{2r+1}
=
-\frac{a_1}{2^{2r}}\delta^{2r+1}
-\frac{a_1\kappa}{2^{2r+1}}\delta^{2r+2}.
\]

Explicitly through the relevant low orders:
\[
M_0=-a_1\kappa\delta,
\]
\[
M_1=-a_1\delta-\frac{a_1\kappa}{2}\delta^2,
\]
\[
M_2=-\frac{a_1\kappa}{4}\delta^3,
\]
\[
M_3=-\frac{a_1}{4}\delta^3-\frac{a_1\kappa}{8}\delta^4,
\]
\[
M_4=-\frac{a_1\kappa}{16}\delta^5,
\]
\[
M_5=-\frac{a_1}{16}\delta^5-\frac{a_1\kappa}{32}\delta^6.
\]

So the balancing condition does **not** remove the exceptional slope at the source-moment level. It moves \(\kappa\) into odd/even moment tails. In particular, before quotienting, there is no moment-level identity forcing all \(\kappa\)-linear data to be line-gauge.

---

# 2. General source-bidegree formula for the \(\kappa\)-slope

Let
\[
F(a_1,a_2,\delta)
:=
[z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\rm mix}
C_{\mathcal W}^{\rm raw}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]

The amplitude-normalized object is
\[
B_{\rm amp}(a_1,\delta,\kappa)
=
-a_1^{-1}\delta^{-2}
F(a_1,-a_1(1+\kappa\delta),\delta).
\]

Differentiate in \(\kappa\):
\[
\partial_\kappa B_{\rm amp}
=
-a_1^{-1}\delta^{-2}
\cdot
\partial_{a_2}F
\cdot
(-a_1\delta)
=
\delta^{-1}\partial_{a_2}F.
\]

Hence on the exceptional divisor,
\[
\boxed{
\left.\partial_\kappa B_{\rm amp}\right|_{\delta=0}
=
\left[
\delta^1
\right]
\partial_{a_2}F(a_1,-a_1,\delta).
}
\]

Gate B gives only
\[
[\delta^1]F(a_1,-a_1,\delta)=0.
\]

It does **not** imply
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)=0
\]
or even that this derivative is in
\[
\mathbf C A_5^{\mathfrak f}(m).
\]

This is the key obstruction.

---

# 3. Formal countermodel

Let
\[
\mathfrak f_m=\mathbf C A\oplus\mathbf C E,
\qquad
A=A_5^{\mathfrak f}(m),
\qquad
[E]\ne0
\quad\text{in}\quad
\mathfrak f_m/\mathbf C A.
\]

Define the \(z^7\), fixed-sector, non-\((1,1)\) raw source component by
\[
F_{\rm raw}
=
z^7\left(
\tau_1\tau_2^3\,a_1a_2^3\,\delta E
-
\tau_1^3\tau_2\,a_1^3a_2\,\delta E
\right).
\]

This is source-mixed and survives
\[
(1-\Pi_{1,1})_{\rm mix},
\]
because its source bidegrees are \((1,3)\) and \((3,1)\), not \((1,1)\).

It is also atom-swap compatible: under
\[
\tau_1\leftrightarrow\tau_2,
\qquad
a_1\leftrightarrow a_2,
\qquad
\delta\mapsto-\delta,
\]
the two displayed terms exchange.

Now impose
\[
a_2=-a_1(1+\kappa\delta).
\]

Then
\[
a_1a_2^3\delta E
=
-a_1^4(1+\kappa\delta)^3\delta E
=
-a_1^4\delta E-3a_1^4\kappa\delta^2E+O(\delta^3),
\]
while
\[
-a_1^3a_2\delta E
=
a_1^4(1+\kappa\delta)\delta E
=
a_1^4\delta E+a_1^4\kappa\delta^2E+O(\delta^3).
\]

Therefore the raw \(\delta^1\) edge term cancels:
\[
[\delta^1]F_{\rm raw}=0.
\]

So this model satisfies the Gate-B-style raw edge divisibility test at order \(\delta^1\).

But after amplitude normalization,
\[
-a_1^{-1}\delta^{-2}F_{\rm raw}
=
2a_1^3\kappa E+O(\delta).
\]

Thus on the exceptional divisor,
\[
\boxed{
\left[
\partial_\kappa B_{\rm amp}(m,\kappa,0)
\right]
=
2a_1^3[E]\ne0
\quad
\text{in}
\quad
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

This is the first quotient-visible \(\kappa\)-linear term.

---

# 4. Survival through the required operations

| Operation | Result |
|---|---|
| \((1-\Pi_{1,1})_{\rm mix}\) | Survives: bidegrees are \((1,3)\), \((3,1)\). |
| \(\pi_{\mathfrak f}\) | Survives by construction: \(E\in\mathfrak f_m\). |
| \(\tau_{h\to m}\) | Survives: at \(\delta=0\), the transport is identity up to higher-order terms; the leading \(E\)-component remains \(E\). |
| quotient by \(\mathbf C A_5^{\mathfrak f}\) | Survives because \(E\notin\mathbf C A_5^{\mathfrak f}\). |

So none of the five candidate source-algebra mechanisms automatically kills the \(\kappa\)-slope.

---

# 5. What exactly is missing

The missing theorem is not ordinary Gate-B edge divisibility. It is a **weighted edge-divisibility / diagonal-merger derivative** statement.

The theorem-ready form is:

```tex
\begin{lemma}[Amplitude-ratio derivative of the edge term is quotient-line valued]
\label{lem:amplitude-ratio-derivative-edge-line-valued}
Let
\[
F(a_1,a_2,\delta)
:=
[z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}
C_{\mathcal W}^{\mathrm{raw}}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]
Assume the Gate~B edge law
\[
[\delta^1]F(a_1,-a_1,\delta)=0.
\]
Then the exceptional-slope derivative satisfies
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
Equivalently,
\[
\left.
\partial_\kappa
\left(
-a_1^{-1}\delta^{-2}
F(a_1,-a_1(1+\kappa\delta),\delta)
\right)
\right|_{\delta=0}
=
0
\quad
\text{in }
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]
\end{lemma}
```

A more source-bidegree-explicit version is:

```tex
\begin{lemma}[Weighted source-bidegree edge cancellation]
\label{lem:weighted-source-bidegree-edge-cancellation}
Write the non-\((1,1)\) mixed edge coefficient as
\[
[\delta^1][z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}
C_{\mathcal W}^{\mathrm{raw}}
=
\sum_{\substack{p,q\ge1\\(p,q)\ne(1,1)}}
a_1^p a_2^q E_{p,q}(m).
\]
Then on the balanced diagonal \(a_2=-a_1\),
\[
\sum_{\substack{p,q\ge1\\(p,q)\ne(1,1)}}
q\,a_1^p(-a_1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{lemma}
```

This is stronger than Gate B. Gate B only gives the same sum **without** the \(q\)-weight after substituting \(a_2=-a_1\). The countermodel above satisfies the unweighted cancellation but violates the weighted one.

---

# 6. Recommended LaTeX insertion

Place this after `rem:missing-quotient-valued-diagonal-merger` or after `rem:formal-c-properties-do-not-rule-out-slope-leakage`.

```tex
\begin{remark}[Source-algebra obstruction to diagonal merger]
\label{rem:source-algebra-obstruction-diagonal-merger}
The balancing chart
\[
h_1=m-\frac{\delta}{2},
\qquad
h_2=m+\frac{\delta}{2},
\qquad
a_2=-a_1(1+\kappa\delta)
\]
does not by itself force the exceptional-divisor quotient class to be
\(\kappa\)-independent.  Let
\[
F(a_1,a_2,\delta)
:=
[z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}
C_{\mathcal W}^{\mathrm{raw}}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]
The amplitude-normalized edge object is
\[
-a_1^{-1}\delta^{-2}
F(a_1,-a_1(1+\kappa\delta),\delta).
\]
Therefore
\[
\partial_\kappa
\left(
-a_1^{-1}\delta^{-2}
F(a_1,-a_1(1+\kappa\delta),\delta)
\right)
=
\delta^{-1}\partial_{a_2}F(a_1,-a_1(1+\kappa\delta),\delta).
\]
Consequently, Gate~B edge divisibility,
\[
[\delta^1]F(a_1,-a_1,\delta)=0,
\]
does not imply
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

Indeed, in a formal fixed-sector model with
\[
\mathfrak f_m=\mathbf C A_5^{\mathfrak f}(m)\oplus \mathbf C E,
\qquad
[E]\ne0,
\]
the source-symmetric non-\((1,1)\) edge term
\[
z^7\left(
\tau_1\tau_2^3 a_1a_2^3\delta E
-
\tau_1^3\tau_2 a_1^3a_2\delta E
\right)
\]
has zero balanced \(\delta^1\)-edge coefficient, but after substituting
\(a_2=-a_1(1+\kappa\delta)\) and normalizing by
\(-a_1^{-1}\delta^{-2}\), it gives
\[
2a_1^3\kappa E+O(\delta).
\]
Thus the exceptional-divisor trace has quotient-visible slope unless the
actual corrected two-atom package supplies the additional weighted edge
cancellation
\[
[\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
This is the precise source-algebra form of the missing diagonal-merger
input.
\end{remark}
```

Bottom line: **Bottleneck C does not close from balancing, projection, edge normalization, or swap-compatible source algebra alone.** The first surviving quotient-visible \(\kappa\)-term is the amplitude-ratio derivative of the raw \(\delta^1\) edge coefficient.
## User (2026-04-25 10:04:41)

You are Agent 8. Read the attached command and do you task.

## Assistant (2026-04-25 10:04:42)

I’ll focus narrowly on Agent 8’s weighted source-bidegree cancellation target. I’ll use the attached command as the task definition and the latest TeX draft as the source of what is actually proved.

The key algebraic point is already visible before any large coefficient table: Gate B is an unweighted balanced-polynomial identity, while Bottleneck C needs a derivative of that identity in the amplitude ratio. Those are not equivalent unless the draft supplies an additional source-bidegree symmetry.

_Thought for 2m 31s_

## Agent 8 verdict

The weighted source-bidegree cancellation is **not forced** by the current draft assumptions.

Gate B gives a **simple balanced-diagonal zero**
\[
P(a_1,-a_1)=0,
\]
where
\[
P(a_1,a_2):=[\delta^1]F(a_1,a_2,\delta).
\]

Bottleneck C needs the stronger **normal derivative / amplitude-ratio derivative** condition
\[
\partial_{a_2}P(a_1,-a_1)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

These are not equivalent. The subset-complement parity used in Gate B supplies the first identity, not the second. The attached command explicitly sharpens Bottleneck C to this weighted derivative law, and the draft’s current guardrails say Gate B is raw edge-divisibility, while Bottleneck C still needs diagonal merger / collision functoriality.  

---

# 1. Source-bidegree decomposition

Set
\[
P(a_1,a_2)
:=
[\delta^1]F(a_1,a_2,\delta).
\]

Decompose by source bidegree:
\[
P(a_1,a_2)
=
\sum_{p,q\ge 1}
a_1^p a_2^q E_{p,q}(m),
\]
after applying
\[
(1-\Pi_{1,1})_{\rm mix},
\qquad
[z^7],
\qquad
\pi_{\mathfrak f_h}.
\]

Gate B gives
\[
P(a_1,-a_1)=0,
\]
i.e.
\[
\sum_{p,q}
a_1^p(-a_1)^qE_{p,q}(m)=0.
\]

For each total source-amplitude degree
\[
d=p+q,
\]
this is
\[
\sum_{p+q=d}
(-1)^q E_{p,q}(m)=0.
\]

But diagonal merger requires
\[
\partial_{a_2}P(a_1,-a_1)
=
\sum_{p,q}
q\,a_1^p(-a_1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

Equivalently, for every total degree \(d\),
\[
\sum_{p+q=d}
q(-1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

So Gate B gives the **unweighted** relation
\[
\sum_{p+q=d}
(-1)^qE_{p,q}=0,
\]
while Bottleneck C needs the **\(q\)-weighted** relation
\[
\sum_{p+q=d}
q(-1)^{q-1}E_{p,q}
\in
\mathbf C A_5^{\mathfrak f}.
\]

No current Gate B mechanism implies this weighted relation.

---

# 2. Equivalent algebraic formulation: simple zero vs double zero

The cleanest formulation is:

\[
P(a_1,-a_1)=0
\]
means
\[
P(a_1,a_2)
\in (a_1+a_2)
\]
as a polynomial in the source amplitudes.

But
\[
\partial_{a_2}P(a_1,-a_1)
\in
\mathbf C A_5^{\mathfrak f}
\]
means
\[
P(a_1,a_2)
\in
(a_1+a_2)^2
\quad
\text{modulo }
\mathbf C A_5^{\mathfrak f}.
\]

Thus Bottleneck C requires a **double balanced-diagonal zero modulo the \(A_5^{\mathfrak f}\)-line**.

Gate B proves only a **simple balanced-diagonal zero**.

This is the core obstruction.

---

# 3. Subset-complement parity gives only the unweighted identity

Suppose a paired bidegree contribution has the form
\[
P_{p,q}
=
a_1^p a_2^q E_{p,q}
+
a_1^q a_2^p E_{q,p}.
\]

Balanced cancellation imposes
\[
(-1)^qE_{p,q}
+
(-1)^pE_{q,p}
=0.
\]

Thus
\[
E_{q,p}
=
-(-1)^{q-p}E_{p,q}.
\]

Now compute the weighted derivative:
\[
\partial_{a_2}P_{p,q}(a_1,-a_1)
=
a_1^{p+q-1}
\left(
q(-1)^{q-1}E_{p,q}
+
p(-1)^{p-1}E_{q,p}
\right).
\]

Substitute the unweighted relation:
\[
\partial_{a_2}P_{p,q}(a_1,-a_1)
=
(q-p)(-1)^{q-1}a_1^{p+q-1}E_{p,q}.
\]

Therefore, unless
\[
p=q
\]
or
\[
E_{p,q}\in \mathbf C A_5^{\mathfrak f}(m),
\]
the weighted derivative survives.

Since the non-\((1,1)\) projection retains precisely asymmetric bidegrees such as
\[
(1,2),(2,1),(1,3),(3,1),\ldots,
\]
subset-complement parity alone cannot prove diagonal merger.

---

# 4. The explicit surviving channel

The prior model
\[
P_{1,3}(a_1,a_2)
=
a_1a_2^3E-a_1^3a_2E
\]
is exactly the minimal obstruction pattern after the accepted Gate-A/Gate-B posture.

It factors as
\[
P_{1,3}
=
a_1a_2(a_2-a_1)(a_1+a_2)E.
\]

Thus
\[
P_{1,3}(a_1,-a_1)=0.
\]

So it satisfies the Gate-B-style unweighted balanced cancellation.

But
\[
\partial_{a_2}P_{1,3}
=
3a_1a_2^2E-a_1^3E,
\]
hence
\[
\partial_{a_2}P_{1,3}(a_1,-a_1)
=
2a_1^3E.
\]

If
\[
E\notin \mathbf C A_5^{\mathfrak f}(m),
\]
then
\[
2a_1^3[E]\ne0
\quad
\text{in }
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

This is the explicit quotient-visible \(\kappa\)-slope channel.

---

# 5. Collision-chart interpretation

Write
\[
a_2=-a_1(1+\kappa\delta).
\]

Let
\[
F(a_1,a_2,\delta)
=
\delta P(a_1,a_2)
+
O(\delta^2).
\]

Then
\[
F(a_1,-a_1(1+\kappa\delta),\delta)
=
\delta P(a_1,-a_1)
-
a_1\kappa\delta^2
\partial_{a_2}P(a_1,-a_1)
+
O(\delta^2).
\]

Since Gate B gives
\[
P(a_1,-a_1)=0,
\]
the first surviving \(\kappa\)-linear contribution after edge normalization is
\[
-a_1^{-1}\delta^{-2}
F(a_1,-a_1(1+\kappa\delta),\delta)
=
\kappa\,\partial_{a_2}P(a_1,-a_1)
+
O(1).
\]

For the channel above, this gives
\[
2\kappa a_1^3E.
\]

Therefore
\[
\partial_\kappa B_7^{\mathfrak f}(m,\kappa,0)
=
2a_1^3E
\]
modulo terms independent of this channel.

If
\[
[E]\ne0
\quad
\text{in }
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]
then
\[
\partial_\kappa Q_{7,m}^q(m,\kappa,0)\ne0.
\]

---

# 6. Does actual corrected whitening forbid \((1,3)/(3,1)\)?

From the current draft posture: **no**.

Reason:

1. The raw corrected-whitening map
   \[
   \mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}
   \]
   is nonlinear in the source blocks, so fourth-transfer mixed bidegrees such as
   \[
   (1,3),\qquad (3,1)
   \]
   are structurally allowed.

2. The projection
   \[
   (1-\Pi_{1,1})_{\rm mix}
   \]
   removes the \((1,1)\) sector, not \((1,3)\) or \((3,1)\).

3. The draft explicitly treats Gate B as an aggregate cancellation mechanism, not placement-level vanishing. Nonzero unsymmetrized transfer placements are not counterexamples to Gate B precisely because Gate B cancels them only after labelled subset-complement aggregation. 

4. The draft’s Bottleneck C guardrail says formal properties and swap symmetry do not force \(\kappa\)-independence; a real proof must add diagonal merger, same-reduced-image, or collision functoriality. 

So the \((1,3)/(3,1)\) bidegree pattern is not excluded by the currently stated mechanisms.

It becomes harmless only if the actual coefficient satisfies
\[
E\in\mathbf C A_5^{\mathfrak f}(m),
\]
or if the full sum over all bidegrees supplies an additional weighted cancellation:
\[
\sum_{p+q=d}
q(-1)^{q-1}E_{p,q}
\in
\mathbf C A_5^{\mathfrak f}(m).
\]

That is exactly the missing theorem.

---

# 7. General obstruction formula

For any paired bidegree \((p,q)\), \(p\ne q\), whose balanced cancellation is achieved only by the relation
\[
(-1)^qE_{p,q}
+
(-1)^pE_{q,p}=0,
\]
the quotient-visible derivative is
\[
\boxed{
\partial_{a_2}P_{p,q}(a_1,-a_1)
=
(q-p)(-1)^{q-1}
a_1^{p+q-1}E_{p,q}.
}
\]

Therefore the exact surviving class is
\[
\boxed{
(q-p)(-1)^{q-1}
a_1^{p+q-1}
[E_{p,q}]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

For \((p,q)=(1,3)\):
\[
\boxed{
2a_1^3[E_{1,3}]
}
\]
is the first explicit quotient-visible \(\kappa\)-slope channel.

---

# 8. Required missing lemma

The missing lemma should be stated as a **double balanced-zero** theorem, not merely as another Gate-B cancellation.

```tex
\begin{lemma}[Weighted source-bidegree cancellation / double balanced-zero]
\label{lem:weighted-source-bidegree-double-balanced-zero}
Let
\[
P(a_1,a_2)
:=
[\delta^1][z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}
C_{\mathcal W}^{\mathrm{raw}}
(a_1,h-\delta/2;\,a_2,h+\delta/2).
\]
Assume the actual corrected two-atom package is evaluated on the good patch
\[
A_5^{\mathfrak f}(m)\ne0.
\]
Then
\[
P(a_1,a_2)
\in
(a_1+a_2)^2\mathfrak f_m
+
(a_1+a_2)\mathbf C A_5^{\mathfrak f}(m)
\]
through ordinary order \(7\).

Equivalently,
\[
P(a_1,-a_1)=0
\]
and
\[
\partial_{a_2}P(a_1,-a_1)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{lemma}
```

Or in coefficient form:

```tex
\begin{lemma}[Weighted source-bidegree edge cancellation]
\label{lem:weighted-source-bidegree-edge-cancellation}
Write
\[
[\delta^1][z^7]\pi_{\mathfrak f_h}
(1-\Pi_{1,1})_{\mathrm{mix}}
C_{\mathcal W}^{\mathrm{raw}}
=
\sum_{p,q\ge1}a_1^pa_2^qE_{p,q}(m).
\]
Then for every total source-amplitude degree \(d\),
\[
\sum_{p+q=d}q(-1)^{q-1}E_{p,q}(m)
\in
\mathbf C A_5^{\mathfrak f}(m).
\]
\end{lemma}
```

This is strictly stronger than Gate B’s unweighted relation
\[
\sum_{p+q=d}(-1)^qE_{p,q}(m)=0.
\]

---

# 9. Conclusion

Agent 8 cannot close Bottleneck C from subset-complement parity or current Gate-B raw edge-divisibility.

The first explicit surviving quotient-visible \(\kappa\)-slope channel is:
\[
\boxed{
a_1a_2^3\delta E-a_1^3a_2\delta E,
\qquad
[E]\ne0
\text{ in }
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

After imposing
\[
a_2=-a_1(1+\kappa\delta)
\]
and normalizing by
\[
-a_1^{-1}\delta^{-2},
\]
this contributes
\[
\boxed{
2\kappa a_1^3[E]
}
\]
to the exceptional-divisor quotient trace.

So the current exact obstruction is:

\[
\boxed{
\text{Gate B gives a simple balanced zero; Bottleneck C needs a double balanced zero modulo }
\mathbf C A_5^{\mathfrak f}.
}
\]
## User (2026-04-25 10:16:42)

Read and do your next attack (given your agent number) in the list.

## Assistant (2026-04-25 10:17:23)

I’ll treat the new “next attack” for Agent 8 as the consolidated Bottleneck C target: test whether actual-source deviations from the homogeneous tower satisfy double balanced divisibility modulo the \(A_5^{\mathfrak f}\)-line.

_Thought for 1m 19s_

## Agent 8 next attack: actual-source double-balanced divisibility

I take the next Agent 8 target to be the joint Bottleneck C / actual-source problem:

\[
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\in
(a_1+a_2)^2V_m[a_1,a_2],
\qquad
V_m:=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
\]

The consolidated report says the homogeneous tower likely has the needed double balanced zero, and the remaining leakage can only come from actual-source deviations. It also identifies the remaining actual-source candidates as higher Fréchet responses involving the same-point cubic \(P_\pm\), nonlinear mixed-block Taylor remainders in \(N^{\corr}\), and product-source-motion terms. 

My result: **I cannot prove actual-source double-balanced divisibility from the stated mechanisms.** The first surviving formal channel is a degree-four actual-source deviation of type

\[
a_1^3a_2E-a_1a_2^3E,
\qquad
[E]\ne0\in V_m.
\]

This channel has the required simple balanced zero, hence it is invisible to ordinary Gate-B edge divisibility, but it fails the derivative condition required for diagonal merger.

---

# 1. Algebraic reduction

Let

\[
\Delta P(a_1,a_2)
:=
\overline P_{7,m}^{\actual}(a_1,a_2)
-
\overline P_{7,m}^{\tower}(a_1,a_2)
\in V_m[a_1,a_2].
\]

Write its source-bidegree decomposition as

\[
\Delta P(a_1,a_2)
=
\sum_{p,q\ge1}a_1^pa_2^q\overline E_{p,q}(m),
\qquad
\overline E_{p,q}\in V_m.
\]

The target is

\[
\Delta P\in(a_1+a_2)^2V_m[a_1,a_2].
\]

Equivalently, for every total source degree \(d=p+q\),

\[
\sum_{p+q=d}(-1)^q\overline E_{p,q}=0
\tag{simple zero}
\]

and

\[
\sum_{p+q=d}q(-1)^{q-1}\overline E_{p,q}=0.
\tag{weighted zero}
\]

Gate B gives the simple zero. Bottleneck C needs the weighted zero. The attached command states this exact distinction: Gate B gives only \([\delta^1]F(a_1,-a_1,\delta)=0\), while diagonal merger needs \([\delta^1]\partial_{a_2}F(a_1,-a_1,\delta)\in \mathbf C A_5^{\mathfrak f}(m)\). 

---

# 2. Pairwise subset-complement parity is insufficient

Consider a paired bidegree contribution

\[
a_1^pa_2^qE_{p,q}
+
a_1^qa_2^pE_{q,p},
\qquad p\ne q.
\]

The simple balanced-zero relation is

\[
(-1)^qE_{p,q}+(-1)^pE_{q,p}=0.
\]

Hence

\[
E_{q,p}
=
-(-1)^{q-p}E_{p,q}.
\]

Now compute the weighted derivative at \(a_2=-a_1\):

\[
\partial_{a_2}
\left(
a_1^pa_2^qE_{p,q}
+
a_1^qa_2^pE_{q,p}
\right)_{a_2=-a_1}
\]

\[
=
a_1^{p+q-1}
\left(
q(-1)^{q-1}E_{p,q}
+
p(-1)^{p-1}E_{q,p}
\right).
\]

Substituting the simple-zero relation gives

\[
(q-p)(-1)^{q-1}a_1^{p+q-1}E_{p,q}.
\]

Thus, for \(p\ne q\), subset-complement cancellation leaves a quotient-visible derivative unless

\[
[E_{p,q}]=0\in V_m.
\]

So pairwise parity proves only simple balanced divisibility. It does **not** prove double balanced divisibility.

---

# 3. First explicit surviving channel

The first dangerous degree-four channel is

\[
\Delta P_{1,3}
=
a_1^3a_2E-a_1a_2^3E.
\]

It factors as

\[
\Delta P_{1,3}
=
a_1a_2(a_1-a_2)(a_1+a_2)E.
\]

Therefore

\[
\Delta P_{1,3}(a_1,-a_1)=0.
\]

So it passes the simple Gate-B balanced test.

But

\[
\partial_{a_2}\Delta P_{1,3}
=
a_1^3E-3a_1a_2^2E,
\]

and hence

\[
\partial_{a_2}\Delta P_{1,3}(a_1,-a_1)
=
-2a_1^3E.
\]

Thus if

\[
[E]\ne0\in V_m,
\]

then

\[
\partial_{a_2}\Delta P_{1,3}(a_1,-a_1)\ne0
\quad\text{in }V_m.
\]

Equivalently, in the collision chart

\[
a_2=-a_1(1+\kappa\delta),
\]

this contributes

\[
2\kappa a_1^3[E]
\]

to the exceptional-divisor quotient trace after the \(-a_1^{-1}\delta^{-2}\) edge normalization, up to the sign convention for \(\Delta P_{1,3}\).

---

# 4. Relation to the remaining actual-source candidates

The previous round killed the **single-insertion first Fréchet response** of the same-point cubic \(P_\pm\), but explicitly did **not** prove \(\Theta_7^{\actual}=0\). The remaining candidates include

\[
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0,
\]

\[
D(G_-^{-1/2})[P_-]\,N_0\,D(G_+^{-1/2})[B_+],
\]

\[
L_0N_0D^2(G_+^{-1/2})[P_+,B_+],
\]

and nonlinear mixed-block Taylor remainders in

\[
N^{\corr}(d_-,d_+,\eta).
\]

These are exactly the kind of terms that can produce degree-four bidegrees \((3,1),(2,2),(1,3)\). The first-insertion cancellation does not imply the second-insertion double-zero relation, because the weighted derivative sees the amplitude-ratio sensitivity of the paired terms, not merely their balanced sum.

In degree four, write

\[
\Delta P_4
=
a_1^3a_2E_{3,1}
+
a_1^2a_2^2E_{2,2}
+
a_1a_2^3E_{1,3}.
\]

Simple balanced zero gives

\[
-E_{3,1}+E_{2,2}-E_{1,3}=0.
\]

Weighted zero gives

\[
E_{3,1}-2E_{2,2}+3E_{1,3}=0.
\]

Together these imply

\[
E_{2,2}=E_{3,1}+E_{1,3},
\]

and

\[
E_{1,3}=E_{3,1}.
\]

So the degree-four actual-source deviation is double balanced iff

\[
E_{3,1}=E_{1,3},
\qquad
E_{2,2}=2E_{3,1}
\quad
\text{in }V_m.
\]

Equivalently,

\[
\Delta P_4
=
a_1a_2(a_1+a_2)^2E
\quad
\text{in }V_m.
\]

The dangerous channel is the antisymmetric failure

\[
E_{1,3}-E_{3,1}\ne0.
\]

Its quotient-visible slope is

\[
2a_1^3(E_{1,3}-E_{3,1})/2
\]

up to the chosen sign convention; for the concrete model \(E_{3,1}=E,\ E_{1,3}=-E\), it is

\[
-2a_1^3E.
\]

---

# 5. What would kill the channel

The needed structural identity is not merely

\[
E_{q,p}\sim E_{p,q}
\]

or subset-complement parity. The necessary and sufficient condition is:

\[
\boxed{
\sum_{p+q=d}q(-1)^{q-1}\overline E_{p,q}=0
\quad
\text{in }V_m
\quad
\text{for every }d.
}
\]

For degree four this becomes the concrete table identity

\[
\boxed{
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}
\quad
\text{in }V_m.
}
\]

This is the exact actual-source replacement for the homogeneous tower’s compensating bidegree structure.

---

# 6. Classification of the remaining actual-source remainders

| Remainder class | Current status | What must be proved |
|---|---|---|
| Single-insertion \(P_\pm\) first Fréchet response | Killed by endpoint swap / transpose per previous result | No further action for simple Gate-B edge. |
| Higher Fréchet responses \(D^2W[P_\pm,A_\pm]\) | **Live for Bottleneck C** | Degree-four bidegree coefficients must satisfy \(E_{1,3}=E_{3,1}\), \(E_{2,2}=2E_{3,1}\) in \(V_m\). |
| Product term \(DW[P_-]\,N_0\,DW[B_+]\) | **Live for Bottleneck C** | Must contribute the missing \(E_{2,2}\) compensation or be quotient-line valued. |
| Right-side mirror \(L_0N_0D^2W[P_+,B_+]\) | **Live for Bottleneck C** | Must match the left-side \(E_{3,1}\) coefficient with the same sign, not the Gate-B cancelling sign. |
| Nonlinear mixed-block Taylor remainders in \(N^{\corr}\) | **Not classified** | Need their \((3,1),(2,2),(1,3)\) quotient classes; they may supply or destroy double divisibility. |
| Product-source-motion terms | **Not classified** | Need the same two balanced moment identities after transport to \(m\). |

---

# 7. Exact missing theorem

The theorem-ready form is:

```tex
\begin{lemma}[Actual-source double balanced divisibility]
\label{lem:actual-source-double-balanced-divisibility}
Let
\[
V_m:=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)
\]
on a good patch \(A_5^{\mathfrak f}(m)\ne0\).  Let
\[
\Delta P_{7,m}
:=
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\in V_m[a_1,a_2]
\]
denote the quotient-valued ordinary order-\(7\), \(\delta^1\)-edge
difference between the actual corrected two-atom source package and the
homogeneous moving Taylor tower.

Then
\[
\Delta P_{7,m}(a_1,a_2)
\in
(a_1+a_2)^2V_m[a_1,a_2].
\]
Equivalently, if
\[
\Delta P_{7,m}
=
\sum_{p,q\ge1}a_1^pa_2^q\overline E_{p,q}(m),
\]
then for every \(d\),
\[
\sum_{p+q=d}(-1)^q\overline E_{p,q}(m)=0,
\]
and
\[
\sum_{p+q=d}q(-1)^{q-1}\overline E_{p,q}(m)=0.
\]
\end{lemma}
```

The first relation is the actual-source Gate-B upgrade. The second relation is the Bottleneck C derivative law.

For the first live degree-four table this specializes to:

```tex
\begin{lemma}[Degree-four actual-source bidegree compensation]
\label{lem:degree-four-actual-source-bidegree-compensation}
For the quotient-valued degree-four actual-source deviation
\[
\Delta P_4
=
a_1^3a_2E_{3,1}
+
a_1^2a_2^2E_{2,2}
+
a_1a_2^3E_{1,3}
\in V_m[a_1,a_2],
\]
one has
\[
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}
\quad
\text{in }V_m.
\]
Equivalently,
\[
\Delta P_4
=
a_1a_2(a_1+a_2)^2E_{3,1}
\quad
\text{in }V_m.
\]
\end{lemma}
```

---

# 8. Bottom line

The next Agent 8 attack does **not** close Bottleneck C. It sharpens the exact first obstruction.

The homogeneous tower may have the double balanced zero, but the actual-source deviation must still satisfy

\[
\overline P_{7,m}^{\actual}
-
\overline P_{7,m}^{\tower}
\in
(a_1+a_2)^2V_m[a_1,a_2].
\]

The first quotient-visible leakage channel is the degree-four antisymmetric bidegree defect

\[
\boxed{
a_1^3a_2E-a_1a_2^3E,
\qquad
[E]\ne0\in V_m.
}
\]

It is invisible to simple Gate-B balanced cancellation but visible to the exceptional-divisor \(\kappa\)-slope. To eliminate it, the actual corrected package must prove the degree-four compensation

\[
\boxed{
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}
\quad
\text{in }
V_m.
}
\]

That is the minimal next table identity.
## User (2026-04-25 10:29:44)

Read and do your next agent prompt (according to your agent number)

## Assistant (2026-04-25 10:30:06)

_Thought for 19s_

## Agent 8 — degree-four actual-source compensation table

I cannot prove the degree-four compensation identities from the stated current mechanisms. The degree-four channel is now reduced to two concrete quotient identities, but the prompt/draft context does not supply the source-block relation needed to force them.

The requested target is:

\[
\Delta P_4
=
a_1^3a_2E_{3,1}
+
a_1^2a_2^2E_{2,2}
+
a_1a_2^3E_{1,3}
\in V_m[a_1,a_2],
\qquad
V_m=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]

and the desired compensation is

\[
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}.
\]

Equivalently,

\[
\Delta P_4=a_1a_2(a_1+a_2)^2E_{3,1}.
\]

The new prompt explicitly asks Agent 8 to specialize the earlier double-balanced-zero obstruction to this degree-four table, and the same background says the actual-source upgrade is still open while the first live obstruction is the nonlinear mixed-block / actual-source deviation problem. 

---

# 1. Algebraic table

Start with

\[
\Delta P_4
=
a_1^3a_2E_{3,1}
+
a_1^2a_2^2E_{2,2}
+
a_1a_2^3E_{1,3}.
\]

Evaluate on the balanced diagonal \(a_2=-a_1\):

\[
\Delta P_4(a_1,-a_1)
=
a_1^4
\left(
-E_{3,1}+E_{2,2}-E_{1,3}
\right).
\]

So simple Gate-B balanced cancellation gives only

\[
\boxed{
E_{2,2}=E_{3,1}+E_{1,3}.
}
\]

Now compute the derivative:

\[
\partial_{a_2}\Delta P_4
=
a_1^3E_{3,1}
+
2a_1^2a_2E_{2,2}
+
3a_1a_2^2E_{1,3}.
\]

At \(a_2=-a_1\),

\[
\partial_{a_2}\Delta P_4(a_1,-a_1)
=
a_1^3
\left(
E_{3,1}-2E_{2,2}+3E_{1,3}
\right).
\]

Thus Bottleneck C requires

\[
\boxed{
E_{3,1}-2E_{2,2}+3E_{1,3}=0
\quad\text{in }V_m.
}
\]

Combining the simple and weighted identities gives

\[
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}.
\]

So the target is exactly equivalent to:

\[
\boxed{
\Delta P_4\in (a_1+a_2)^2V_m[a_1,a_2].
}
\]

---

# 2. Defect coordinates

The two natural obstruction coordinates are:

\[
D_{\rm asym}:=E_{1,3}-E_{3,1},
\]

and

\[
D_{\rm mid}:=E_{2,2}-2E_{3,1}.
\]

Under the simple balanced relation

\[
E_{2,2}=E_{3,1}+E_{1,3},
\]

these are the same obstruction:

\[
D_{\rm mid}
=
E_{1,3}-E_{3,1}
=
D_{\rm asym}.
\]

Therefore, after Gate-B simple cancellation, the whole degree-four Bottleneck C obstruction is one quotient class:

\[
\boxed{
D_4:=E_{1,3}-E_{3,1}\in V_m.
}
\]

The derivative leakage is then

\[
\partial_{a_2}\Delta P_4(a_1,-a_1)
=
a_1^3D_4.
\]

So:

\[
\boxed{
\partial_\kappa Q_{7,m}^q=0
\quad\Longleftrightarrow\quad
D_4=0.
}
\]

---

# 3. Source of the three coefficients

At degree four, the relevant actual-source remainders split as follows.

\[
\begin{array}{c|c|c}
\text{source class} & \text{possible bidegrees} & \text{status} \\
\hline
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0
& (3,1) \text{ primarily}
& \text{left same-point higher Fréchet carrier} \\
D(G_-^{-1/2})[P_-]\,N_0\,D(G_+^{-1/2})[B_+]
& (2,2)
& \text{middle product carrier} \\
L_0N_0D^2(G_+^{-1/2})[P_+,B_+]
& (1,3) \text{ primarily}
& \text{right same-point higher Fréchet carrier} \\
\text{nonlinear mixed-block higher terms in }N^{\corr}
& (3,1),(2,2),(1,3)
& \text{unclassified without actual }N^{\corr}\text{ table} \\
\text{product source-motion terms}
& (3,1),(2,2),(1,3)
& \text{unclassified transport contribution}
\end{array}
\]

The current background says the earlier same-point cubic single-insertion defect was killed, but not the higher Fréchet responses or nonlinear mixed-block remainders; the remaining actual-source carrier is explicitly the promoted nonlinear mixed-block quadratic remainder coupled to one same-point linear whitening slot. 

Thus the degree-four coefficients should be written schematically as

\[
E_{3,1}
=
E_{3,1}^{LL}
+
E_{3,1}^{Y}
+
E_{3,1}^{\rm sm},
\]

\[
E_{2,2}
=
E_{2,2}^{LR}
+
E_{2,2}^{Y}
+
E_{2,2}^{\rm sm},
\]

\[
E_{1,3}
=
E_{1,3}^{RR}
+
E_{1,3}^{Y}
+
E_{1,3}^{\rm sm},
\]

where:

\[
E_{3,1}^{LL}
\sim
[z^7]\pi_{\mathfrak f}
D^2(G_-^{-1/2})[P_-,A_-]N_0R_0,
\]

\[
E_{2,2}^{LR}
\sim
[z^7]\pi_{\mathfrak f}
D(G_-^{-1/2})[P_-]N_0D(G_+^{-1/2})[B_+],
\]

\[
E_{1,3}^{RR}
\sim
[z^7]\pi_{\mathfrak f}
L_0N_0D^2(G_+^{-1/2})[P_+,B_+],
\]

and the \(Y\)-terms are the degree-four nonlinear mixed-block remainders coming from \(N^{\corr}\).

---

# 4. What endpoint-swap gives, and what it does not give

Endpoint swap / transpose can relate left and right terms:

\[
E_{1,3}^{RR}
\equiv
\pm E_{3,1}^{LL}
\quad\text{in }V_m.
\]

But the sign is the whole issue.

For double-balanced compensation, the required sign is:

\[
\boxed{
E_{1,3}=E_{3,1}.
}
\]

If endpoint-swap gives

\[
E_{1,3}=-E_{3,1},
\]

then simple cancellation can still hold after a suitable \(E_{2,2}\), but Bottleneck C fails.

Likewise, even if the endpoint terms match,

\[
E_{1,3}=E_{3,1},
\]

one still needs the middle product term to satisfy

\[
\boxed{
E_{2,2}=2E_{3,1}.
}
\]

That is a binomial \(1:2:1\) law. It is stronger than transpose invariance. It is the statement that the actual-source degree-four deviation depends on \(a_1,a_2\) through

\[
a_1a_2(a_1+a_2)^2
\]

rather than through an arbitrary balanced polynomial.

---

# 5. Formal obstruction table

A simple balanced degree-four polynomial has the general form

\[
\Delta P_4
=
a_1a_2(a_1+a_2)
\left(
a_1U+a_2V
\right),
\qquad
U,V\in V_m.
\]

Expanding:

\[
\Delta P_4
=
a_1^3a_2U
+
a_1^2a_2^2(U+V)
+
a_1a_2^3V.
\]

Thus

\[
E_{3,1}=U,
\qquad
E_{2,2}=U+V,
\qquad
E_{1,3}=V.
\]

Simple balanced cancellation is automatic. Double balanced divisibility is equivalent to

\[
U=V.
\]

The obstruction is

\[
D_4=V-U.
\]

Then

\[
\Delta P_4
=
a_1a_2(a_1+a_2)^2U
+
a_1a_2^2(a_1+a_2)(V-U).
\]

So the exact uncompensated quotient class is:

\[
\boxed{
D_4=E_{1,3}-E_{3,1}.
}
\]

The leakage term is:

\[
\boxed{
\partial_{a_2}\Delta P_4(a_1,-a_1)
=
a_1^3D_4.
}
\]

Under the collision chart

\[
a_2=-a_1(1+\kappa\delta),
\]

the normalized exceptional-divisor contribution is proportional to

\[
\boxed{
\kappa a_1^3D_4.
}
\]

---

# 6. Does corrected whitening force \(1:2:1\)?

Not from the current stated mechanisms.

Corrected whitening is nonlinear, so second Fréchet and product terms naturally generate binomial-looking coefficients. But a binomial-looking expansion only appears if the degree-four actual-source deviation is literally a second variation in the **balanced sum direction**

\[
a_1+a_2.
\]

The stated mechanisms give:

1. endpoint-swap / transpose symmetry;
2. simple Gate-B cancellation;
3. fixed-sector projection;
4. homogeneous tower double-balanced behavior;
5. actual-source deviation still open.

None of these, as stated, implies the actual-source identity

\[
\Delta P_4=a_1a_2(a_1+a_2)^2E.
\]

The missing identity is a second-order source functoriality law: actual-source degree-four deviations must be functions of the merged amplitude \(a_1+a_2\) modulo the \(A_5^{\mathfrak f}\)-line.

---

# 7. Result

The degree-four compensation table is:

\[
\begin{array}{c|c|c}
\text{coefficient} & \text{required value} & \text{defect} \\
\hline
E_{3,1} & E & 0 \\
E_{2,2} & 2E & E_{2,2}-2E_{3,1} \\
E_{1,3} & E & E_{1,3}-E_{3,1}
\end{array}
\]

After imposing simple Gate-B cancellation,

\[
E_{2,2}=E_{3,1}+E_{1,3},
\]

the two defects coincide:

\[
E_{2,2}-2E_{3,1}
=
E_{1,3}-E_{3,1}.
\]

Therefore the first uncompensated quotient class is

\[
\boxed{
D_4:=E_{1,3}-E_{3,1}\in V_m.
}
\]

If

\[
D_4\ne0,
\]

then

\[
\Delta P_4\notin(a_1+a_2)^2V_m[a_1,a_2],
\]

and Bottleneck C fails at degree four.

---

# 8. The exact theorem needed

```tex
\begin{lemma}[Degree-four actual-source binomial compensation]
\label{lem:degree-four-actual-source-binomial-compensation}
Let
\[
V_m:=\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m),
\]
and let
\[
\Delta P_4
=
a_1^3a_2E_{3,1}
+
a_1^2a_2^2E_{2,2}
+
a_1a_2^3E_{1,3}
\in V_m[a_1,a_2]
\]
be the degree-four actual-source deviation from the homogeneous tower in the
ordinary order-\(7\), \(\delta^1\)-edge coefficient. Then
\[
E_{1,3}=E_{3,1},
\qquad
E_{2,2}=2E_{3,1}
\quad\text{in }V_m.
\]
Equivalently,
\[
\Delta P_4
=
a_1a_2(a_1+a_2)^2E_{3,1}
\quad\text{in }V_m[a_1,a_2].
\]
\end{lemma}
```

A sharper version isolates the one remaining obstruction:

```tex
\begin{lemma}[Degree-four antisymmetric defect vanishes]
\label{lem:degree-four-antisymmetric-defect-vanishes}
Assume the simple balanced relation
\[
E_{2,2}=E_{3,1}+E_{1,3}
\quad\text{in }V_m.
\]
Then the degree-four Bottleneck C condition is equivalent to
\[
E_{1,3}-E_{3,1}=0
\quad\text{in }V_m.
\]
\end{lemma}
```

---

# 9. Bottom line

The degree-four actual-source table is not closed.

The exact first obstruction is:

\[
\boxed{
D_4=E_{1,3}-E_{3,1}
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

Equivalently, the middle compensation defect is:

\[
\boxed{
E_{2,2}-2E_{3,1}.
}
\]

The actual corrected whitening must prove a \(1:2:1\) binomial compensation law. Endpoint-swap / transpose symmetry and simple Gate-B cancellation do not by themselves supply it.
## User (2026-04-25 10:42:30)

Do your agent prompt, according to your agent number

## Assistant (2026-04-25 10:42:31)

I’ll execute Agent 8’s current assignment: build a finite coefficient checklist for the \(Y_{12}^{(2)}\) carrier, not try to prove the carrier vanishes. The output will be a table Agent 1/4 can use for the actual computation.

_Thought for 1m 21s_

## Agent 8 — finite \(Y_{12}^{(2)}\) coefficient checklist

I cannot compute numerical \(I,S\)-coordinates from the prompt alone, because the actual Hessian coefficient arrays of \(N^{\corr}(d_-,d_+,\eta)\) are not provided in the command. But the finite bookkeeping table is determined. It reduces the first live carrier to a finite list of symmetric-surviving rows whose only remaining classification is:

\[
0,\qquad 
\mathbf C A_5^{\mathfrak f}\text{-line},\qquad
\text{or quotient-visible}.
\]

This is the right level for Agent 1 and Agent 4: Agent 1 computes the surviving rows; Agent 4 tests their \(\Phi_K\)-visibility.

The current prompt identifies \(Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]\) coupled to one same-point linear whitening slot as the first live actual-source / Bottleneck C carrier, and defines the quotient obstruction \(E_{A,Y}^q\) in \(\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m)\). 

---

# 1. Notation for the finite table

Write the homogeneous ordinary-order slices as

\[
Y_{\alpha\beta}^{(2)}
=
\sum_{g\ge0}Y_{\alpha\beta}^{(2),[g]},
\qquad
\alpha,\beta\in\{d,\eta\}.
\]

Thus

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

Let

\[
\mathcal L_-^{[r]}[A_-]
:=
[z^r]\,D(G_-^{-1/2})[A_-],
\]

\[
\mathcal R_+^{[r]}[B_+]
:=
[z^r]\,D(G_+^{-1/2})[B_+],
\]

and allow baseline expansions

\[
L_0=\sum_{b\ge0}L_0^{[b]},
\qquad
R_0=\sum_{b\ge0}R_0^{[b]}.
\]

If \(L_0,R_0\) are treated as order-zero baselines, set \(b=0\) throughout.

Then the finite carrier is

\[
E_{A,Y}
=
\sum_{\alpha,\beta\in\{d,\eta\}}
\sum_{\substack{r+g+b=7\\ r,g,b\ge0}}
E_{\alpha\beta;r,g,b},
\]

where

\[
E_{\alpha\beta;r,g,b}
:=
[\delta^1]\,
\tau_{h\to m}
\pi_{\mathfrak f_h}
\left(
\mathcal L_-^{[r]}[A_-]\,
Y_{\alpha\beta}^{(2),[g]}\,
R_0^{[b]}
+
L_0^{[b]}\,
Y_{\alpha\beta}^{(2),[g]}\,
\mathcal R_+^{[r]}[B_+]
\right).
\]

If the baseline contributes only in order \(0\), this reduces to

\[
E_{A,Y}
=
\sum_{\alpha,\beta}
\sum_{g=0}^{7}
E_{\alpha\beta;7-g,g,0}.
\]

---

# 2. Ordinary-order assignment

The component \(Y_{\alpha\beta}^{(2)}\) should not be assigned one scalar order. It has homogeneous slices \(Y_{\alpha\beta}^{(2),[g]}\). The finite rule is:

\[
\boxed{
\text{a row contributes iff } r+g+b=7.
}
\]

With baseline \(b=0\), the allowed same-point whitening slot is

\[
\boxed{
r=7-g.
}
\]

So each component contributes only through the following finite order slices:

\[
Y_{\alpha\beta}^{(2),[0]},
Y_{\alpha\beta}^{(2),[1]},
\ldots,
Y_{\alpha\beta}^{(2),[7]}.
\]

Rows with \(g>7\) are too high-order for \([z^7]\). Rows with \(r<0\) do not exist.

---

# 3. Main finite table, baseline order \(b=0\)

| Component | Middle slice | Required whitening slot | Source variables | Edge | Endpoint / transpose behavior | Classification before \(I,S\) computation |
|---|---:|---:|---|---:|---|---|
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[0]}\) | \(A_-^{[7]},B_+^{[7]}\) | \(d_1d_2\) | \(\delta^1\) | left/right pair is transpose-symmetric at total order \(7\) | symmetric-surviving; line-gauge or quotient-visible candidate |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[1]}\) | \(A_-^{[6]},B_+^{[6]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[2]}\) | \(A_-^{[5]},B_+^{[5]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[3]}\) | \(A_-^{[4]},B_+^{[4]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[4]}\) | \(A_-^{[3]},B_+^{[3]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[5]}\) | \(A_-^{[2]},B_+^{[2]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[6]}\) | \(A_-^{[1]},B_+^{[1]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{dd}^{(2)}\) | \(Y_{dd}^{(2),[7]}\) | \(A_-^{[0]},B_+^{[0]}\) | \(d_1d_2\) | \(\delta^1\) | same | same |
| \(Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)}\) | \(Y_{d\eta}^{(2),[g]}+Y_{\eta d}^{(2),[g]}\), \(0\le g\le7\) | \(A_-^{[7-g]},B_+^{[7-g]}\) | \(d_1\eta_2+\eta_1d_2\) | \(\delta^1\) | transpose swaps \(d\eta\leftrightarrow\eta d\); symmetric part survives | symmetric-surviving; line-gauge or quotient-visible candidate |
| \(Y_{d\eta}^{(2)}-Y_{\eta d}^{(2)}\) | antisymmetric \(d\eta/\eta d\) slice | \(A_-^{[7-g]},B_+^{[7-g]}\) | \(d_1\eta_2-\eta_1d_2\) | \(\delta^1\) | transpose-antisymmetric part | skew-killed by fixed-sector projection |
| \(Y_{\eta\eta}^{(2)}\) | \(Y_{\eta\eta}^{(2),[g]}\), \(0\le g\le7\) | \(A_-^{[7-g]},B_+^{[7-g]}\) | \(\eta_1\eta_2\) | \(\delta^1\) | self-paired under transpose | symmetric-surviving; line-gauge or quotient-visible candidate |

So the compact working table is:

\[
\boxed{
\begin{array}{c|c|c|c}
\text{component} & g & r & \text{status}\\
\hline
Y_{dd}^{(2),[g]} & 0\le g\le7 & 7-g &
\operatorname{Sym}_+\text{ survives}\\
Y_{d\eta}^{(2),[g]}+Y_{\eta d}^{(2),[g]} & 0\le g\le7 & 7-g &
\operatorname{Sym}_+\text{ survives}\\
Y_{d\eta}^{(2),[g]}-Y_{\eta d}^{(2),[g]} & 0\le g\le7 & 7-g &
\operatorname{Sym}_-\text{ killed}\\
Y_{\eta\eta}^{(2),[g]} & 0\le g\le7 & 7-g &
\operatorname{Sym}_+\text{ survives}.
\end{array}
}
\]

---

# 4. If \(L_0,R_0\) have nonzero higher baseline order

Use this extension:

\[
r+g+b=7.
\]

For each \(\alpha\beta\in\{dd,d\eta,\eta d,\eta\eta\}\), include all triples

\[
(g,b,r)
\in\mathbf Z_{\ge0}^3,
\qquad
g+b\le7,
\qquad
r=7-g-b.
\]

The row is:

\[
E_{\alpha\beta;r,g,b}
=
[\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
\mathcal L_-^{[r]}[A_-]
Y_{\alpha\beta}^{(2),[g]}
R_0^{[b]}
+
L_0^{[b]}
Y_{\alpha\beta}^{(2),[g]}
\mathcal R_+^{[r]}[B_+]
\right).
\]

This gives at most

\[
4\cdot \#\{(g,b):g+b\le7\}
=
4\cdot36
=
144
\]

component rows before merging \(d\eta/\eta d\) symmetry. With \(b=0\), it is \(4\cdot8=32\) raw rows, or \(3\cdot8=24\) after replacing \(d\eta,\eta d\) by symmetric/antisymmetric combinations.

---

# 5. Endpoint parity and why the rows are not automatically killed

For the \(\delta^1\) edge coefficient, endpoint swap sends

\[
\delta\mapsto-\delta.
\]

Assume the standard parity rules used in the current connection reduction:

\[
\left(\mathcal L_-^{[r]}[A_-]\right)^T
=
(-1)^r\mathcal R_+^{[r]}[B_+],
\]

\[
(R_0^{[b]})^T=(-1)^bL_0^{[b]},
\]

and for the Hessian middle block,

\[
\left(Y_{\alpha\beta}^{(2),[g],\langle1\rangle}\right)^T
=
(-1)^{g+1}
Y_{\beta^\ast\alpha^\ast}^{(2),[g],\langle1\rangle},
\]

where \(\beta^\ast\alpha^\ast\) denotes the endpoint-swapped component.

The total sign for the left row transposed into the right row is then

\[
(-1)^r(-1)^b(-1)^{g+1}
=
(-1)^{r+b+g+1}.
\]

Since every contributing row has

\[
r+b+g=7,
\]

the total sign is

\[
(-1)^8=+1.
\]

Therefore:

\[
\boxed{
\text{every eligible }[z^7][\delta^1]\text{ row is transpose-symmetric, not skew-killed.}
}
\]

This matches the prompt’s warning that at \([z^7\delta^1]\), reflection gives a symmetric fixed-sector class, not automatic cancellation. 

---

# 6. The actual checklist for Agent 1

For each surviving row, Agent 1 should compute

\[
E_{\alpha\beta;r,g,b}
=
e_{\alpha\beta;r,g,b}I
+
f_{\alpha\beta;r,g,b}S.
\]

Then apply these tests:

## Zero test

\[
E_{\alpha\beta;r,g,b}=0
\quad\Longleftrightarrow\quad
e_{\alpha\beta;r,g,b}=0,\quad
f_{\alpha\beta;r,g,b}=0.
\]

## Quotient-line test

\[
E_{\alpha\beta;r,g,b}\in\mathbf C A_5^{\mathfrak f}
\]

where

\[
A_5^{\mathfrak f}=u_5I+v_5S,
\]

iff

\[
\boxed{
e_{\alpha\beta;r,g,b}v_5
-
u_5f_{\alpha\beta;r,g,b}
=
0.
}
\]

## Quotient-visible test

\[
E_{\alpha\beta;r,g,b}^q\ne0
\]

iff

\[
\boxed{
e_{\alpha\beta;r,g,b}v_5
-
u_5f_{\alpha\beta;r,g,b}
\ne0.
}
\]

## Transform-safe test

Since

\[
\Phi_K(eI+fS)=2f,
\]

the scalar transform-safe condition is

\[
\boxed{
f_{\alpha\beta;r,g,b}=0.
}
\]

If the row is line-gauge,

\[
E_{\alpha\beta;r,g,b}=\lambda A_5^{\mathfrak f},
\]

then

\[
\Phi_K(E_{\alpha\beta;r,g,b})=2\lambda v_5.
\]

On the generic \(v_5\ne0\) patch, line-gauge plus transform-safe implies

\[
\lambda=0.
\]

The prompt explicitly separates these two requirements: quotient Bottleneck C needs \(E_{A,Y}^q=0\), while the transform-safe augmented package needs \(\Phi_K(E_{A,Y})=0\). 

---

# 7. Final coefficient table to hand off

\[
\boxed{
E_{A,Y}
=
\sum_{\substack{g+b\le7\\ r=7-g-b}}
\left(
E_{dd;r,g,b}^{+}
+
E_{d\eta+\eta d;r,g,b}^{+}
+
E_{\eta\eta;r,g,b}^{+}
\right),
}
\]

where

\[
E_{dd;r,g,b}^{+}
=
[\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
\mathcal L_-^{[r]}[A_-]
Y_{dd}^{(2),[g]}
R_0^{[b]}
+
L_0^{[b]}
Y_{dd}^{(2),[g]}
\mathcal R_+^{[r]}[B_+]
\right),
\]

\[
E_{d\eta+\eta d;r,g,b}^{+}
=
[\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
\mathcal L_-^{[r]}[A_-]
\bigl(Y_{d\eta}^{(2),[g]}+Y_{\eta d}^{(2),[g]}\bigr)
R_0^{[b]}
+
L_0^{[b]}
\bigl(Y_{d\eta}^{(2),[g]}+Y_{\eta d}^{(2),[g]}\bigr)
\mathcal R_+^{[r]}[B_+]
\right),
\]

\[
E_{\eta\eta;r,g,b}^{+}
=
[\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
\mathcal L_-^{[r]}[A_-]
Y_{\eta\eta}^{(2),[g]}
R_0^{[b]}
+
L_0^{[b]}
Y_{\eta\eta}^{(2),[g]}
\mathcal R_+^{[r]}[B_+]
\right).
\]

The antisymmetric combination

\[
Y_{d\eta}^{(2),[g]}-Y_{\eta d}^{(2),[g]}
\]

is not part of the surviving fixed-sector table; it is transpose-skew and is killed by \(\pi_{\mathfrak f}\).

---

# 8. Classification result

The table does **not** prove

\[
E_{A,Y}=0
\]

or

\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}.
\]

It proves a sharper reduction:

\[
\boxed{
\text{Only the transpose-symmetric }dd,\ d\eta+\eta d,\ \eta\eta
\text{ Hessian rows with }r+g+b=7\text{ need to be computed.}
}
\]

Every such row is a genuine surviving fixed-sector candidate. None is killed by endpoint-swap parity at \([z^7][\delta^1]\).

Therefore the first live actual-source carrier reduces to the finite obstruction

\[
\boxed{
E_{A,Y}^q
=
\left[
\sum_{\substack{g+b\le7\\r=7-g-b}}
\left(
E_{dd;r,g,b}^{+}
+
E_{d\eta+\eta d;r,g,b}^{+}
+
E_{\eta\eta;r,g,b}^{+}
\right)
\right]
\in
\mathfrak f_m/\mathbf C A_5^{\mathfrak f}(m).
}
\]

Agent 1 should now compute the \(I,S\) coefficients of these rows; Agent 4 should apply the quotient and \(\Phi_K\) tests above.
## User (2026-04-25 10:49:47)

Please do this instruction according to your agent number.

## Assistant (2026-04-25 10:50:05)

_Thought for 14s_

The instruction identifies \(E_{A,Y}\) as the main local obstruction and asks Agent 8 to compress the \(Y_{12}^{(2)}\) table into an executable checklist of surviving rows only. 

## Executable \(Y_{12}^{(2)}\) checklist

Define the input coefficients:

\[
\mathcal L_{A}^{[r]}:=[z^r]D(G_-^{-1/2})[A_-],
\]

\[
\mathcal R_{B}^{[r]}:=[z^r]D(G_+^{-1/2})[B_+],
\]

\[
L_0^{[b]}:=[z^b]L_0,
\qquad
R_0^{[b]}:=[z^b]R_0,
\]

\[
Y_{dd}^{[g]}:=[z^g]Y_{dd}^{(2)},
\]

\[
Y_{d\eta+\eta d}^{[g]}
:=
[z^g]\left(Y_{d\eta}^{(2)}+Y_{\eta d}^{(2)}\right),
\]

\[
Y_{\eta\eta}^{[g]}:=[z^g]Y_{\eta\eta}^{(2)}.
\]

The skew row

\[
Y_{d\eta-\eta d}^{[g]}
:=
[z^g]\left(Y_{d\eta}^{(2)}-Y_{\eta d}^{(2)}\right)
\]

is removed.

---

## Master row formula

For every surviving type

\[
\chi\in
\{dd,\ d\eta+\eta d,\ \eta\eta\},
\]

compute

\[
E_{\chi;r,g,b}
:=
[\delta^1]\tau_{h\to m}\pi_{\mathfrak f_h}
\left(
\mathcal L_A^{[r]}Y_{\chi}^{[g]}R_0^{[b]}
+
L_0^{[b]}Y_{\chi}^{[g]}\mathcal R_B^{[r]}
\right),
\]

subject to

\[
r+g+b=7,
\qquad
r,g,b\ge0.
\]

Then

\[
E_{A,Y}
=
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{\substack{r+g+b=7\\r,g,b\ge0}}
E_{\chi;r,g,b}.
\]

---

## Minimal checklist if \(L_0,R_0\) are order-zero only

If

\[
L_0=L_0^{[0]},
\qquad
R_0=R_0^{[0]},
\]

then \(b=0\), \(r=7-g\), and Agent 1 must compute exactly these rows:

| Row | Required coefficient |
|---:|---|
| 1 | \(E_{dd;7,0,0}\) |
| 2 | \(E_{dd;6,1,0}\) |
| 3 | \(E_{dd;5,2,0}\) |
| 4 | \(E_{dd;4,3,0}\) |
| 5 | \(E_{dd;3,4,0}\) |
| 6 | \(E_{dd;2,5,0}\) |
| 7 | \(E_{dd;1,6,0}\) |
| 8 | \(E_{dd;0,7,0}\) |
| 9 | \(E_{d\eta+\eta d;7,0,0}\) |
| 10 | \(E_{d\eta+\eta d;6,1,0}\) |
| 11 | \(E_{d\eta+\eta d;5,2,0}\) |
| 12 | \(E_{d\eta+\eta d;4,3,0}\) |
| 13 | \(E_{d\eta+\eta d;3,4,0}\) |
| 14 | \(E_{d\eta+\eta d;2,5,0}\) |
| 15 | \(E_{d\eta+\eta d;1,6,0}\) |
| 16 | \(E_{d\eta+\eta d;0,7,0}\) |
| 17 | \(E_{\eta\eta;7,0,0}\) |
| 18 | \(E_{\eta\eta;6,1,0}\) |
| 19 | \(E_{\eta\eta;5,2,0}\) |
| 20 | \(E_{\eta\eta;4,3,0}\) |
| 21 | \(E_{\eta\eta;3,4,0}\) |
| 22 | \(E_{\eta\eta;2,5,0}\) |
| 23 | \(E_{\eta\eta;1,6,0}\) |
| 24 | \(E_{\eta\eta;0,7,0}\) |

---

## Extended checklist if \(L_0,R_0\) have baseline order

For each

\[
\chi\in
\{dd,\ d\eta+\eta d,\ \eta\eta\},
\]

compute all rows

\[
E_{\chi;7-g-b,g,b}
\]

for

\[
0\le b\le7,
\qquad
0\le g\le7-b.
\]

Equivalently:

| \(b\) | \(g\)-range | \(r\) |
|---:|---:|---:|
| \(0\) | \(0\le g\le7\) | \(7-g\) |
| \(1\) | \(0\le g\le6\) | \(6-g\) |
| \(2\) | \(0\le g\le5\) | \(5-g\) |
| \(3\) | \(0\le g\le4\) | \(4-g\) |
| \(4\) | \(0\le g\le3\) | \(3-g\) |
| \(5\) | \(0\le g\le2\) | \(2-g\) |
| \(6\) | \(0\le g\le1\) | \(1-g\) |
| \(7\) | \(g=0\) | \(0\) |

Total extended rows:

\[
3\sum_{b=0}^{7}(8-b)
=
3\cdot36
=
108.
\]

---

## Required output from Agent 1 per row

For each row, compute

\[
E_{\chi;r,g,b}
=
e_{\chi;r,g,b}I
+
f_{\chi;r,g,b}S.
\]

Then aggregate:

\[
e_{A,Y}
=
\sum_{\chi,r,g,b}e_{\chi;r,g,b},
\qquad
f_{A,Y}
=
\sum_{\chi,r,g,b}f_{\chi;r,g,b},
\]

so that

\[
E_{A,Y}=e_{A,Y}I+f_{A,Y}S.
\]

Final tests:

\[
E_{A,Y}=0
\iff
e_{A,Y}=0,\quad f_{A,Y}=0.
\]

\[
E_{A,Y}\in\mathbf C A_5^{\mathfrak f}
\iff
e_{A,Y}v_5-u_5f_{A,Y}=0.
\]

\[
\Phi_K(E_{A,Y})=0
\iff
f_{A,Y}=0.
\]
## User (2026-04-25 10:58:36)

Do these instructions per your agent number

## Assistant (2026-04-25 10:58:47)

_Thought for 9s_

Per Agent 8 prompt: executable \(Y_{12}^{(2)}\) row table only; surviving rows are \(Y_{dd}^{(2)}\), \(Y_{d\eta+\eta d}^{(2)}\), \(Y_{\eta\eta}^{(2)}\), with \(Y_{d\eta-\eta d}^{(2)}\) removed as skew-killed. 

## Definitions

\[
\chi\in\mathcal X:=\{dd,\ d\eta+\eta d,\ \eta\eta\}.
\]

\[
r+g+b=7,\qquad \alpha+\beta+\gamma=1.
\]

\[
H^A_{r,\alpha}:=[z^r\delta^\alpha]D(G_-^{-1/2})[A_-],
\]

\[
Y^\chi_{g,\beta}:=[z^g\delta^\beta]Y_\chi^{(2)},
\]

\[
R_{b,\gamma}:=[z^b\delta^\gamma]R_0.
\]

Each executable row is:

\[
\boxed{
\mathcal E_{\chi;r,g,b}^{\alpha,\beta,\gamma}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
H^A_{r,\alpha}Y^\chi_{g,\beta}R_{b,\gamma}
\right)
}
\]

with final sum:

\[
\boxed{
E_{A,Y}
=
\sum_{\chi\in\mathcal X}
\sum_{\substack{r+g+b=7\\ \alpha+\beta+\gamma=1}}
\mathcal E_{\chi;r,g,b}^{\alpha,\beta,\gamma}.
}
\]

---

## Edge-placement rows

For every \(\chi\in\mathcal X\) and every \((r,g,b)\) with \(r+g+b=7\), compute exactly these three rows:

| Edge source | Row | Status |
|---|---|---|
| \(H\)-edge | \(\mathcal E_{\chi;r,g,b}^{1,0,0}= \tau\pi_{\mathfrak f}\operatorname{Sym}(H^A_{r,1}Y^\chi_{g,0}R_{b,0})\) | symmetric-surviving; line-gauge / quotient-visible candidate |
| \(Y\)-edge | \(\mathcal E_{\chi;r,g,b}^{0,1,0}= \tau\pi_{\mathfrak f}\operatorname{Sym}(H^A_{r,0}Y^\chi_{g,1}R_{b,0})\) | symmetric-surviving; line-gauge / quotient-visible candidate |
| \(R\)-edge | \(\mathcal E_{\chi;r,g,b}^{0,0,1}= \tau\pi_{\mathfrak f}\operatorname{Sym}(H^A_{r,0}Y^\chi_{g,0}R_{b,1})\) | symmetric-surviving; line-gauge / quotient-visible candidate |

Removed row:

| Removed coefficient | Status |
|---|---|
| \(Y_{d\eta-\eta d}^{(2)}\) | skew-killed by fixed-sector projection |

---

## Full \((r,g,b)\) index table

For each \(\chi\in\mathcal X\), and for each edge-placement row above, use:

| \(b\) | \(g\) range | \(r=7-g-b\) |
|---:|---:|---:|
| \(0\) | \(0,\ldots,7\) | \(7-g\) |
| \(1\) | \(0,\ldots,6\) | \(6-g\) |
| \(2\) | \(0,\ldots,5\) | \(5-g\) |
| \(3\) | \(0,\ldots,4\) | \(4-g\) |
| \(4\) | \(0,\ldots,3\) | \(3-g\) |
| \(5\) | \(0,\ldots,2\) | \(2-g\) |
| \(6\) | \(0,\ldots,1\) | \(1-g\) |
| \(7\) | \(0\) | \(0\) |

Total rows if \(R_0\) has higher \(z,\delta\)-orders:

\[
3\text{ component types}\times 36\text{ order triples}\times 3\text{ edge placements}=324.
\]

---

## Reduced table if \(R_0,L_0\) are order-zero only

Assume:

\[
R_{b,\gamma}=0
\quad\text{unless}\quad
(b,\gamma)=(0,0).
\]

Then:

\[
b=0,\qquad \gamma=0,\qquad r+g=7,\qquad \alpha+\beta=1.
\]

For each \(\chi\in\mathcal X\), compute:

| \(g\) | \(r=7-g\) | \(H\)-edge row | \(Y\)-edge row |
|---:|---:|---|---|
| \(0\) | \(7\) | \(H^A_{7,1}Y^\chi_{0,0}R_{0,0}\) | \(H^A_{7,0}Y^\chi_{0,1}R_{0,0}\) |
| \(1\) | \(6\) | \(H^A_{6,1}Y^\chi_{1,0}R_{0,0}\) | \(H^A_{6,0}Y^\chi_{1,1}R_{0,0}\) |
| \(2\) | \(5\) | \(H^A_{5,1}Y^\chi_{2,0}R_{0,0}\) | \(H^A_{5,0}Y^\chi_{2,1}R_{0,0}\) |
| \(3\) | \(4\) | \(H^A_{4,1}Y^\chi_{3,0}R_{0,0}\) | \(H^A_{4,0}Y^\chi_{3,1}R_{0,0}\) |
| \(4\) | \(3\) | \(H^A_{3,1}Y^\chi_{4,0}R_{0,0}\) | \(H^A_{3,0}Y^\chi_{4,1}R_{0,0}\) |
| \(5\) | \(2\) | \(H^A_{2,1}Y^\chi_{5,0}R_{0,0}\) | \(H^A_{2,0}Y^\chi_{5,1}R_{0,0}\) |
| \(6\) | \(1\) | \(H^A_{1,1}Y^\chi_{6,0}R_{0,0}\) | \(H^A_{1,0}Y^\chi_{6,1}R_{0,0}\) |
| \(7\) | \(0\) | \(H^A_{0,1}Y^\chi_{7,0}R_{0,0}\) | \(H^A_{0,0}Y^\chi_{7,1}R_{0,0}\) |

Total reduced rows:

\[
3\text{ component types}\times 8\text{ order pairs}\times 2\text{ edge placements}=48.
\]

---

## Final coefficient list Agent 1 must compute

For \(\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}\):

\[
\boxed{
\mathcal E_{\chi;7-g,g,0}^{1,0,0}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
H^A_{7-g,1}Y^\chi_{g,0}R_{0,0}
\right),
\quad
0\le g\le7.
}
\]

\[
\boxed{
\mathcal E_{\chi;7-g,g,0}^{0,1,0}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
H^A_{7-g,0}Y^\chi_{g,1}R_{0,0}
\right),
\quad
0\le g\le7.
}
\]

Then aggregate:

\[
\boxed{
E_{A,Y}
=
\sum_{\chi\in\mathcal X}
\sum_{g=0}^{7}
\left(
\mathcal E_{\chi;7-g,g,0}^{1,0,0}
+
\mathcal E_{\chi;7-g,g,0}^{0,1,0}
\right)
}
\]

if \(R_0,L_0\) are order-zero only.

For each row output:

\[
\mathcal E_{\chi;r,g,b}^{\alpha,\beta,\gamma}
=
e_{\chi;r,g,b}^{\alpha,\beta,\gamma}I
+
f_{\chi;r,g,b}^{\alpha,\beta,\gamma}S.
\]

Final aggregate:

\[
e_{A,Y}=\sum e_{\chi;r,g,b}^{\alpha,\beta,\gamma},
\qquad
f_{A,Y}=\sum f_{\chi;r,g,b}^{\alpha,\beta,\gamma}.
\]

Final tests:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
\qquad
\Phi_K(E_{A,Y})=2f_{A,Y}.
\]
## User (2026-04-25 11:17:12)

Do instruction per your agent number

## Assistant (2026-04-25 11:17:27)

_Thought for 14s_

## Agent 8 — corrected Bottleneck C \(E_{A,Y}^{\mathrm{BC}}\) executable table

The previous \(\alpha+\beta+\gamma=1\) table is parked. For the first Bottleneck C amplitude-ratio carrier, the internal coefficient is frozen:

\[
\alpha=\beta=\gamma=0.
\]

The active object is

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

This correction is required because the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the \(\delta^1\) edge on the collision chart; the local coefficient table should therefore use the frozen internal coefficient, not the internal \([z^7\delta^1]\) source-position coefficient. 

---

# 1. Coefficient normalization

Use:

\[
H^A_{r,0}
=
\sum_{a\in\{1,5\}}
\Lambda^-_{a,r},
\qquad
0\le r\le3,
\]

with the understanding that each \(\Lambda^-_{a,r}\) is built from the corresponding same-point linear source jet

\[
(r_i^{[a]})^{(k)}(m).
\]

Use:

\[
W_{+,b},
\qquad
0\le b\le3,
\]

for the right baseline whitening coefficient.

Use:

\[
Y^\chi_{g,0},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\qquad
4\le g\le7.
\]

Then the atomic row is:

\[
\boxed{
\mathcal E^{a}_{\chi;g,r,b}
:=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
Y^\chi_{g,0}
W_{+,b}
\right),
}
\]

where

\[
a\in\{1,5\},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\qquad
4\le g\le7,
\qquad
r+b=7-g.
\]

Thus

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
\sum_{a\in\{1,5\}}
\mathcal E^{a}_{\chi;g,r,b}.
}
\]

---

# 2. Minimal executable row table

For each \(\chi\in\{dd,d\eta+\eta d,\eta\eta\}\):

| \(g\) | \(r+b=7-g\) | Required rows |
|---:|---:|---|
| \(7\) | \(0\) | \(\mathcal E^a_{\chi;7,0,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0})\) |
| \(6\) | \(1\) | \(\mathcal E^a_{\chi;6,0,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{6,0}W_{+,1})\) |
| \(6\) | \(1\) | \(\mathcal E^a_{\chi;6,1,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{6,0}W_{+,0})\) |
| \(5\) | \(2\) | \(\mathcal E^a_{\chi;5,0,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{5,0}W_{+,2})\) |
| \(5\) | \(2\) | \(\mathcal E^a_{\chi;5,1,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{5,0}W_{+,1})\) |
| \(5\) | \(2\) | \(\mathcal E^a_{\chi;5,2,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^\chi_{5,0}W_{+,0})\) |
| \(4\) | \(3\) | \(\mathcal E^a_{\chi;4,0,3}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{4,0}W_{+,3})\) |
| \(4\) | \(3\) | \(\mathcal E^a_{\chi;4,1,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{4,0}W_{+,2})\) |
| \(4\) | \(3\) | \(\mathcal E^a_{\chi;4,2,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^\chi_{4,0}W_{+,1})\) |
| \(4\) | \(3\) | \(\mathcal E^a_{\chi;4,3,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,3}Y^\chi_{4,0}W_{+,0})\) |

For each row, run \(a=1\) and \(a=5\).

Total rows:

\[
3\ \chi\text{-types}
\times
10\ (g,r,b)\text{-rows}
\times
2\ a\text{-slots}
=
60.
\]

---

# 3. Component expansion

The three surviving component sums are:

\[
E_{dd}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\left[
\mathcal E^a_{dd;7,0,0}
+
\mathcal E^a_{dd;6,0,1}
+
\mathcal E^a_{dd;6,1,0}
+
\mathcal E^a_{dd;5,0,2}
+
\mathcal E^a_{dd;5,1,1}
+
\mathcal E^a_{dd;5,2,0}
+
\mathcal E^a_{dd;4,0,3}
+
\mathcal E^a_{dd;4,1,2}
+
\mathcal E^a_{dd;4,2,1}
+
\mathcal E^a_{dd;4,3,0}
\right],
\]

\[
E_{d\eta+\eta d}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\left[
\mathcal E^a_{d\eta+\eta d;7,0,0}
+
\mathcal E^a_{d\eta+\eta d;6,0,1}
+
\mathcal E^a_{d\eta+\eta d;6,1,0}
+
\mathcal E^a_{d\eta+\eta d;5,0,2}
+
\mathcal E^a_{d\eta+\eta d;5,1,1}
+
\mathcal E^a_{d\eta+\eta d;5,2,0}
+
\mathcal E^a_{d\eta+\eta d;4,0,3}
+
\mathcal E^a_{d\eta+\eta d;4,1,2}
+
\mathcal E^a_{d\eta+\eta d;4,2,1}
+
\mathcal E^a_{d\eta+\eta d;4,3,0}
\right],
\]

\[
E_{\eta\eta}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\left[
\mathcal E^a_{\eta\eta;7,0,0}
+
\mathcal E^a_{\eta\eta;6,0,1}
+
\mathcal E^a_{\eta\eta;6,1,0}
+
\mathcal E^a_{\eta\eta;5,0,2}
+
\mathcal E^a_{\eta\eta;5,1,1}
+
\mathcal E^a_{\eta\eta;5,2,0}
+
\mathcal E^a_{\eta\eta;4,0,3}
+
\mathcal E^a_{\eta\eta;4,1,2}
+
\mathcal E^a_{\eta\eta;4,2,1}
+
\mathcal E^a_{\eta\eta;4,3,0}
\right].
\]

Then

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}^{\mathrm{BC}}
+
E_{d\eta+\eta d}^{\mathrm{BC}}
+
E_{\eta\eta}^{\mathrm{BC}}.
}
\]

---

# 4. Input coefficient table Agent 1 must supply

Agent 1 must provide the fixed-sector coordinates

\[
\mathcal E^a_{\chi;g,r,b}
=
e^a_{\chi;g,r,b}I
+
f^a_{\chi;g,r,b}S
\]

for the 60 rows above.

Equivalently, provide these base coefficient arrays:

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3},
\]

\[
\Lambda^-_{1,0},\Lambda^-_{1,1},\Lambda^-_{1,2},\Lambda^-_{1,3},
\]

\[
\Lambda^-_{5,0},\Lambda^-_{5,1},\Lambda^-_{5,2},\Lambda^-_{5,3},
\]

\[
Y^{dd}_{4,0},Y^{dd}_{5,0},Y^{dd}_{6,0},Y^{dd}_{7,0},
\]

\[
Y^{d\eta+\eta d}_{4,0},
Y^{d\eta+\eta d}_{5,0},
Y^{d\eta+\eta d}_{6,0},
Y^{d\eta+\eta d}_{7,0},
\]

\[
Y^{\eta\eta}_{4,0},
Y^{\eta\eta}_{5,0},
Y^{\eta\eta}_{6,0},
Y^{\eta\eta}_{7,0}.
\]

---

# 5. Required scalar midpoint jets

The draft/prompt does not provide the scalar midpoint jet table needed to evaluate the arrays above. The missing jets are exactly:

\[
\boxed{
q_0^{(k)}(m),
\qquad
0\le k\le9.
}
\]

and

\[
\boxed{
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad
a\in\{1,5\},\quad
2\le k\le9.
}
\]

These are explicitly listed as necessary in the updated command; without them, \(E_{A,Y}^{\mathrm{BC}}=eI+fS\) cannot be evaluated. 

---

# 6. Symmetry status

The following row is removed:

\[
Y_{d\eta-\eta d}^{(2)}.
\]

Reason:

\[
Y_{d\eta-\eta d}^{(2)}
\quad\text{is transpose-skew and is killed by }\pi_{\mathfrak f}.
\]

The surviving rows

\[
Y_{dd}^{(2)},\qquad
Y_{d\eta+\eta d}^{(2)},\qquad
Y_{\eta\eta}^{(2)}
\]

are transpose-symmetric and therefore survive fixed-sector projection.

No stated symmetry forces

\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\]

or

\[
f_{A,Y}=0
\]

without evaluating the 60-row table. The updated command explicitly says the local obstruction cannot yet be evaluated because the scalar midpoint jet table is missing. 

---

# 7. Final aggregate tests after computation

Once the 60 row coordinates are supplied, compute:

\[
e_{A,Y}
=
\sum_{\chi,g,r,b,a}
e^a_{\chi;g,r,b},
\]

\[
f_{A,Y}
=
\sum_{\chi,g,r,b,a}
f^a_{\chi;g,r,b}.
\]

Then:

\[
\boxed{
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y}.
}
\]

\[
\boxed{
\Phi_K(E_{A,Y}^{\mathrm{BC}})
=
2f_{A,Y}.
}
\]

\[
\boxed{
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
}
\]

Current status:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ is reduced to a 60-row frozen coefficient table.}
}
\]

No quotient closure or \(T\)-horizontal closure follows until the missing scalar midpoint jets are supplied.

_Thought for a few seconds_

Per Agent 8 prompt: frozen Bottleneck-C coefficient only, with \(\alpha=\beta=\gamma=0\); exclude the internal \(\delta^1\) source-position table. 

## Definitions

\[
\mathcal E^a_{\chi;g,r,b}
:=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
Y^\chi_{g,0}
W_{+,b}
\right)
\]

\[
a\in\{1,5\},
\qquad
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\},
\qquad
4\le g\le7,
\qquad
r+b=7-g.
\]

All rows below are:

\[
\text{fixed-sector surviving;}
\qquad
\text{line-gauge candidate;}
\qquad
\text{quotient-visible candidate.}
\]

Excluded:

\[
Y_{d\eta-\eta d}^{(2)}
\quad
\text{is skew-killed.}
\]

---

# 60-row executable table

## \(E_{dd}^{\mathrm{BC}}\)

\[
E_{dd}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{dd;g,r,b}
\]

| \(a\) | row |
|---:|---|
| \(1,5\) | \(\mathcal E^a_{dd;7,0,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{dd}_{7,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{dd;6,0,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{dd}_{6,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{dd;6,1,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{dd}_{6,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{dd;5,0,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{dd}_{5,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{dd;5,1,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{dd}_{5,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{dd;5,2,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{dd}_{5,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{dd;4,0,3}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{dd}_{4,0}W_{+,3})\) |
| \(1,5\) | \(\mathcal E^a_{dd;4,1,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{dd}_{4,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{dd;4,2,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{dd}_{4,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{dd;4,3,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,3}Y^{dd}_{4,0}W_{+,0})\) |

---

## \(E_{d\eta+\eta d}^{\mathrm{BC}}\)

\[
E_{d\eta+\eta d}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{d\eta+\eta d;g,r,b}
\]

| \(a\) | row |
|---:|---|
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;7,0,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{d\eta+\eta d}_{7,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;6,0,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{d\eta+\eta d}_{6,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;6,1,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{d\eta+\eta d}_{6,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;5,0,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{d\eta+\eta d}_{5,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;5,1,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{d\eta+\eta d}_{5,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;5,2,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{d\eta+\eta d}_{5,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;4,0,3}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{d\eta+\eta d}_{4,0}W_{+,3})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;4,1,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{d\eta+\eta d}_{4,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;4,2,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{d\eta+\eta d}_{4,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{d\eta+\eta d;4,3,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,3}Y^{d\eta+\eta d}_{4,0}W_{+,0})\) |

---

## \(E_{\eta\eta}^{\mathrm{BC}}\)

\[
E_{\eta\eta}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{\eta\eta;g,r,b}
\]

| \(a\) | row |
|---:|---|
| \(1,5\) | \(\mathcal E^a_{\eta\eta;7,0,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{\eta\eta}_{7,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;6,0,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{\eta\eta}_{6,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;6,1,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{\eta\eta}_{6,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;5,0,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{\eta\eta}_{5,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;5,1,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{\eta\eta}_{5,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;5,2,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{\eta\eta}_{5,0}W_{+,0})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;4,0,3}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^{\eta\eta}_{4,0}W_{+,3})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;4,1,2}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^{\eta\eta}_{4,0}W_{+,2})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;4,2,1}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^{\eta\eta}_{4,0}W_{+,1})\) |
| \(1,5\) | \(\mathcal E^a_{\eta\eta;4,3,0}=\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,3}Y^{\eta\eta}_{4,0}W_{+,0})\) |

where

\[
\mathcal R=
\{(7,0,0),(6,0,1),(6,1,0),(5,0,2),(5,1,1),(5,2,0),
(4,0,3),(4,1,2),(4,2,1),(4,3,0)\}.
\]

---

# Aggregation

\[
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}^{\mathrm{BC}}
+
E_{d\eta+\eta d}^{\mathrm{BC}}
+
E_{\eta\eta}^{\mathrm{BC}}.
\]

For each row:

\[
\mathcal E^a_{\chi;g,r,b}
=
e^a_{\chi;g,r,b}I
+
f^a_{\chi;g,r,b}S.
\]

Then:

\[
e_{A,Y}
=
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
e^a_{\chi;g,r,b},
\]

\[
f_{A,Y}
=
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
f^a_{\chi;g,r,b}.
\]

\[
E_{A,Y}^{\mathrm{BC}}
=
e_{A,Y}I+f_{A,Y}S.
\]

---

# Final tests

\[
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y}.
\]

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})
=
2f_{A,Y}.
\]

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
\]

---

# Scalar midpoint jets required

\[
q_0^{(k)}(m),
\qquad
0\le k\le9.
\]

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,
\qquad
a\in\{1,5\},
\qquad
2\le k\le9.
\]

Equivalent coefficient arrays required:

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3},
\]

\[
\Lambda^-_{1,0},\Lambda^-_{1,1},\Lambda^-_{1,2},\Lambda^-_{1,3},
\]

\[
\Lambda^-_{5,0},\Lambda^-_{5,1},\Lambda^-_{5,2},\Lambda^-_{5,3},
\]

\[
Y^{dd}_{4,0},Y^{dd}_{5,0},Y^{dd}_{6,0},Y^{dd}_{7,0},
\]

\[
Y^{d\eta+\eta d}_{4,0},
Y^{d\eta+\eta d}_{5,0},
Y^{d\eta+\eta d}_{6,0},
Y^{d\eta+\eta d}_{7,0},
\]

\[
Y^{\eta\eta}_{4,0},
Y^{\eta\eta}_{5,0},
Y^{\eta\eta}_{6,0},
Y^{\eta\eta}_{7,0}.
\]
## User (2026-04-25 11:37:37)

do these instructions according to your agent number

## Assistant (2026-04-25 11:37:39)

I’ll execute Agent 8: maintain the \(E_{A,Y}^{\mathrm{BC}}\) frozen-coefficient table, but this time I’ll try to reduce rows from the draft’s definitions before declaring dependencies missing.

_Thought for 29s_

## Agent 8 — minimized executable table for \(E_{A,Y}^{\mathrm{BC}}\)

The active coefficient is the **frozen** Bottleneck-C carrier

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

Do **not** use the internal \([z^7\delta^1]\) table here; the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge in the collision chart. 

---

# Reductions

| Candidate reduction | Result |
|---|---|
| \(Y_{d\eta-\eta d}^{(2)}\) | removed; skew-killed by \(\pi_{\mathfrak f}\) |
| \(g<4\) rows | removed by order; active \(Y^\chi_{g,0}\) starts at \(g=4\) |
| \(g>7\) rows | removed by \([z^7]\) |
| \(\alpha+\beta+\gamma=1\) rows | parked; source-motion layer, not first BC carrier |
| \(a\notin\{1,5\}\) | removed by current same-point source-linear slot convention |
| \(\Lambda^-_{a,3}\) | not proved zero by stated source-grade / affine-removal conventions |
| \(W_{+,b}\) scalar/removable | not established; keep \(b=0,1,2,3\) |
| row forced into \(\ker\pi_{\mathfrak f}\) | only skew \(d\eta-\eta d\) row |
| row forced into \(\ker\Phi_K\) | not established |
| row forced into \(\mathbf C A_5^{\mathfrak f}\) | not established |

So the minimized executable table remains **60 rows**.

---

# Row definition

\[
\mathcal E^a_{\chi;g,r,b}
:=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right),
\]

with

\[
a\in\{1,5\},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\qquad
4\le g\le7,
\qquad
r+b=7-g.
\]

Each surviving row has status:

\[
\boxed{
\text{fixed-sector surviving; line-gauge candidate; quotient-visible candidate.}
}
\]

---

# Index set

\[
\mathcal R
=
\{
(7,0,0),
(6,0,1),(6,1,0),
(5,0,2),(5,1,1),(5,2,0),
(4,0,3),(4,1,2),(4,2,1),(4,3,0)
\},
\]

where each triple is \((g,r,b)\).

---

# Executable rows by \(\chi\)

For each

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}
\]

and each

\[
a\in\{1,5\},
\]

compute:

| \(g\) | \(r\) | \(b\) | row expression | needed coefficient inputs | status |
|---:|---:|---:|---|---|---|
| 7 | 0 | 0 | \(\mathcal E^a_{\chi;7,0,0}\) | \(\Lambda^-_{a,0},Y^\chi_{7,0},W_{+,0}\) | surviving |
| 6 | 0 | 1 | \(\mathcal E^a_{\chi;6,0,1}\) | \(\Lambda^-_{a,0},Y^\chi_{6,0},W_{+,1}\) | surviving |
| 6 | 1 | 0 | \(\mathcal E^a_{\chi;6,1,0}\) | \(\Lambda^-_{a,1},Y^\chi_{6,0},W_{+,0}\) | surviving |
| 5 | 0 | 2 | \(\mathcal E^a_{\chi;5,0,2}\) | \(\Lambda^-_{a,0},Y^\chi_{5,0},W_{+,2}\) | surviving |
| 5 | 1 | 1 | \(\mathcal E^a_{\chi;5,1,1}\) | \(\Lambda^-_{a,1},Y^\chi_{5,0},W_{+,1}\) | surviving |
| 5 | 2 | 0 | \(\mathcal E^a_{\chi;5,2,0}\) | \(\Lambda^-_{a,2},Y^\chi_{5,0},W_{+,0}\) | surviving |
| 4 | 0 | 3 | \(\mathcal E^a_{\chi;4,0,3}\) | \(\Lambda^-_{a,0},Y^\chi_{4,0},W_{+,3}\) | surviving |
| 4 | 1 | 2 | \(\mathcal E^a_{\chi;4,1,2}\) | \(\Lambda^-_{a,1},Y^\chi_{4,0},W_{+,2}\) | surviving |
| 4 | 2 | 1 | \(\mathcal E^a_{\chi;4,2,1}\) | \(\Lambda^-_{a,2},Y^\chi_{4,0},W_{+,1}\) | surviving |
| 4 | 3 | 0 | \(\mathcal E^a_{\chi;4,3,0}\) | \(\Lambda^-_{a,3},Y^\chi_{4,0},W_{+,0}\) | surviving |

This table is repeated for:

\[
\chi=dd,
\qquad
\chi=d\eta+\eta d,
\qquad
\chi=\eta\eta,
\]

and for:

\[
a=1,5.
\]

Total:

\[
3\times 10\times 2=60.
\]

---

# Grouped sums

\[
E_{dd}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{dd;g,r,b}.
\]

\[
E_{d\eta+\eta d}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{d\eta+\eta d;g,r,b}.
\]

\[
E_{\eta\eta}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{\eta\eta;g,r,b}.
\]

\[
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}^{\mathrm{BC}}
+
E_{d\eta+\eta d}^{\mathrm{BC}}
+
E_{\eta\eta}^{\mathrm{BC}}.
\]

---

# Coordinate aggregation

For each row compute

\[
\mathcal E^a_{\chi;g,r,b}
=
e^a_{\chi;g,r,b}I
+
f^a_{\chi;g,r,b}S.
\]

Then

\[
e_{A,Y}
=
\sum_{\chi}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
e^a_{\chi;g,r,b},
\]

\[
f_{A,Y}
=
\sum_{\chi}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
f^a_{\chi;g,r,b}.
\]

\[
E_{A,Y}^{\mathrm{BC}}
=
e_{A,Y}I+f_{A,Y}S.
\]

Final tests:

\[
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y},
\]

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})
=
2f_{A,Y},
\]

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
\]

---

# Dependency map

## \(W_{+,b}\)

Required:

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3}.
\]

Status:

\[
\boxed{\text{derivable by Sylvester recurrence once baseline midpoint jets are supplied.}}
\]

Needed scalar jets:

\[
q_0^{(k)}(m),
\qquad
0\le k\le9.
\]

## \(\Lambda^-_{a,r}\)

Required:

\[
\Lambda^-_{1,0},\Lambda^-_{1,1},\Lambda^-_{1,2},\Lambda^-_{1,3},
\]

\[
\Lambda^-_{5,0},\Lambda^-_{5,1},\Lambda^-_{5,2},\Lambda^-_{5,3}.
\]

Status:

\[
\boxed{\text{derivable by same-point linear whitening recurrence once source jets are supplied.}}
\]

Needed source jets:

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

No stated convention forces:

\[
\Lambda^-_{a,3}=0.
\]

## \(Y^\chi_{g,0}\)

Required:

\[
Y^{dd}_{4,0},Y^{dd}_{5,0},Y^{dd}_{6,0},Y^{dd}_{7,0},
\]

\[
Y^{d\eta+\eta d}_{4,0},
Y^{d\eta+\eta d}_{5,0},
Y^{d\eta+\eta d}_{6,0},
Y^{d\eta+\eta d}_{7,0},
\]

\[
Y^{\eta\eta}_{4,0},
Y^{\eta\eta}_{5,0},
Y^{\eta\eta}_{6,0},
Y^{\eta\eta}_{7,0}.
\]

Status:

\[
\boxed{\text{derivable from the corrected mixed-block Hessian only after the actual source jets }d_{i,\pm}(z),\eta_i(z)\text{ are fixed.}}
\]

Needed source jets:

\[
q_0^{(k)}(m),
\qquad
0\le k\le9,
\]

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

---

# Minimal missing theorem/table

The exact missing input is:

\[
\boxed{
\text{Midpoint source-jet table for }
q_0^{(k)}(m),\ 0\le k\le9,
\quad
(r_i^{[a]})^{(k)}(m),\ i=1,2,\ a\in\{1,5\},\ 2\le k\le9.
}
\]

Equivalent theorem form:

\[
\boxed{
\text{Finite midpoint source-jet realization theorem for }
W_{+,0..3},\ \Lambda^-_{1,0..3},\ \Lambda^-_{5,0..3},
\ Y^{dd}_{4..7,0},\
Y^{d\eta+\eta d}_{4..7,0},\
Y^{\eta\eta}_{4..7,0}.
}
\]

No current structural symmetry in the supplied prompt forces

\[
Q_{A,Y}=0
\]

or

\[
f_{A,Y}=0
\]

before evaluating this 60-row table.

_Thought for 25s_

## Agent 8 — minimized executable table for \(E_{A,Y}^{\mathrm{BC}}\)

I re-ran the coefficient bookkeeping under the corrected rule: this is the **frozen** Bottleneck-C coefficient, so the table uses \(\alpha=\beta=\gamma=0\), not the internal \([z^7\delta^1]\) table. The attached prompt explicitly states that \(a_1a_2(a_1+a_2)\) supplies the first \(\delta\)-edge and that the active object is the frozen coefficient \(E_{A,Y}^{\mathrm{BC}}\). 

The finite contraction is:

\[
E_{A,Y}^{\mathrm{BC}}
=
\sum_{\chi,g,r,b,a}
\mathcal E^a_{\chi;g,r,b},
\]

where

\[
\mathcal E^a_{\chi;g,r,b}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
Y^\chi_{g,0}
W_{+,b}
\right).
\]

Active indices:

\[
a\in\{1,5\},
\qquad
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\},
\qquad
4\le g\le7,
\qquad
r+b=7-g.
\]

---

# 1. Reduction audit

| Possible reduction | Result | Reason |
|---|---:|---|
| remove \(Y_{d\eta-\eta d}^{(2)}\) | yes | transpose-skew; killed by \(\pi_{\mathfrak f}\) |
| remove \(g<4\) | yes | not part of the promoted BC carrier table |
| remove \(g>7\) | yes | cannot contribute to \([z^7]\) |
| remove \(a\notin\{1,5\}\) | yes | active same-point source-linear slots are only \(a=1,5\) |
| set \(\Lambda^-_{a,3}=0\) | no | not forced by affine removal, source-grade reflection, or source-bidegree projection as stated |
| remove \(a=1\) or \(a=5\) | no | no stated one-amplitude collapse removes either slot in this carrier |
| treat \(W_{+,b}\) as scalar/line-preserving | no | Sylvester recurrence defines it, but no scalar/line-preserving theorem is stated |
| force rows into \(\ker\pi_{\mathfrak f}\) | no, except skew row already removed | surviving rows are transpose-symmetric |
| force rows into \(\ker\Phi_K\) | no | would require \(S\)-component cancellation not implied by parity |
| force rows into \(\mathbf C A_5^{\mathfrak f}\) | no | would require \(ev_5-u_5f=0\), not implied structurally |

So the true minimized table remains:

\[
3\cdot 10\cdot 2=60
\]

rows.

---

# 2. Universal row table

Let

\[
\mathcal R
=
\left\{
\begin{array}{l}
(7,0,0),\\
(6,0,1),(6,1,0),\\
(5,0,2),(5,1,1),(5,2,0),\\
(4,0,3),(4,1,2),(4,2,1),(4,3,0)
\end{array}
\right\},
\]

where each triple is \((g,r,b)\).

For each

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}
\]

and

\[
a\in\{1,5\},
\]

compute the following 10 rows:

| \(\chi\) | \(a\) | \(g\) | \(r\) | \(b\) | row | status | needed inputs |
|---|---:|---:|---:|---:|---|---|---|
| \(\chi\) | \(a\) | 7 | 0 | 0 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,0},Y^\chi_{7,0},W_{+,0}\) |
| \(\chi\) | \(a\) | 6 | 0 | 1 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{6,0}W_{+,1})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,0},Y^\chi_{6,0},W_{+,1}\) |
| \(\chi\) | \(a\) | 6 | 1 | 0 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{6,0}W_{+,0})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,1},Y^\chi_{6,0},W_{+,0}\) |
| \(\chi\) | \(a\) | 5 | 0 | 2 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{5,0}W_{+,2})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,0},Y^\chi_{5,0},W_{+,2}\) |
| \(\chi\) | \(a\) | 5 | 1 | 1 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{5,0}W_{+,1})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,1},Y^\chi_{5,0},W_{+,1}\) |
| \(\chi\) | \(a\) | 5 | 2 | 0 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^\chi_{5,0}W_{+,0})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,2},Y^\chi_{5,0},W_{+,0}\) |
| \(\chi\) | \(a\) | 4 | 0 | 3 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,0}Y^\chi_{4,0}W_{+,3})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,0},Y^\chi_{4,0},W_{+,3}\) |
| \(\chi\) | \(a\) | 4 | 1 | 2 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,1}Y^\chi_{4,0}W_{+,2})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,1},Y^\chi_{4,0},W_{+,2}\) |
| \(\chi\) | \(a\) | 4 | 2 | 1 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,2}Y^\chi_{4,0}W_{+,1})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,2},Y^\chi_{4,0},W_{+,1}\) |
| \(\chi\) | \(a\) | 4 | 3 | 0 | \(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{a,3}Y^\chi_{4,0}W_{+,0})\) | surviving; line/quotient candidate | \(\Lambda^-_{a,3},Y^\chi_{4,0},W_{+,0}\) |

This table is instantiated for:

\[
\chi=dd,\quad d\eta+\eta d,\quad \eta\eta
\]

and

\[
a=1,\quad 5.
\]

---

# 3. Grouped executable form

\[
E_{dd}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{dd;g,r,b}.
\]

\[
E_{d\eta+\eta d}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{d\eta+\eta d;g,r,b}.
\]

\[
E_{\eta\eta}^{\mathrm{BC}}
=
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
\mathcal E^a_{\eta\eta;g,r,b}.
\]

\[
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}^{\mathrm{BC}}
+
E_{d\eta+\eta d}^{\mathrm{BC}}
+
E_{\eta\eta}^{\mathrm{BC}}.
\]

---

# 4. Dependency map

## 4.1 \(W_{+,b}\)

Needed:

\[
W_{+,0},W_{+,1},W_{+,2},W_{+,3}.
\]

Derivation status:

\[
W_{+,b}
\text{ is derivable from the inverse-square-root/Sylvester recurrence once }
G_+^{(0)}
\text{ and its midpoint expansion are known.}
\]

Minimal scalar baseline dependency:

\[
q_0^{(k)}(m).
\]

For the row table itself, a safe finite range is:

\[
0\le k\le9.
\]

A sharper range may be possible if the draft gives explicit truncation contracts for \(W_{+,0..3}\), but no such contract is visible in the supplied prompt materials.

## 4.2 \(\Lambda^-_{a,r}\)

Needed:

\[
\Lambda^-_{1,0},\Lambda^-_{1,1},\Lambda^-_{1,2},\Lambda^-_{1,3},
\]

\[
\Lambda^-_{5,0},\Lambda^-_{5,1},\Lambda^-_{5,2},\Lambda^-_{5,3}.
\]

Derivation status:

\[
\Lambda^-_{a,r}
\text{ is derivable from same-point source-linear Fréchet/Sylvester recurrence once }
X^-_{a,n}
\text{ and source jets are known.}
\]

The available source conventions do **not** force

\[
X^-_{a,3}=0
\quad\text{or}\quad
\Lambda^-_{a,3}=0.
\]

They also do **not** remove \(a=1\) or \(a=5\).

Minimal source dependency, safe range:

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

## 4.3 \(Y^\chi_{g,0}\)

Needed:

\[
Y^{dd}_{4,0},Y^{dd}_{5,0},Y^{dd}_{6,0},Y^{dd}_{7,0},
\]

\[
Y^{d\eta+\eta d}_{4,0},Y^{d\eta+\eta d}_{5,0},
Y^{d\eta+\eta d}_{6,0},Y^{d\eta+\eta d}_{7,0},
\]

\[
Y^{\eta\eta}_{4,0},Y^{\eta\eta}_{5,0},Y^{\eta\eta}_{6,0},Y^{\eta\eta}_{7,0}.
\]

Removed:

\[
Y^{d\eta-\eta d}_{g,0}.
\]

Derivation status:

\[
Y^\chi_{g,0}
\text{ is derivable from the corrected mixed-block Hessian }
D^2N_0[\xi_1,\xi_2]
\text{ once }d_{i,\pm}(z),\eta_i(z)
\text{ are fixed.}
\]

Safe source dependency:

\[
q_0^{(k)}(m),\quad 0\le k\le9,
\]

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

---

# 5. Final coordinate formulas

For every surviving row:

\[
\mathcal E^a_{\chi;g,r,b}
=
e^a_{\chi;g,r,b}I
+
f^a_{\chi;g,r,b}S.
\]

Then:

\[
e_{A,Y}
=
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
e^a_{\chi;g,r,b},
\]

\[
f_{A,Y}
=
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{a\in\{1,5\}}
\sum_{(g,r,b)\in\mathcal R}
f^a_{\chi;g,r,b}.
\]

The two output tests are:

\[
Q_{A,Y}
=
e_{A,Y}v_5-u_5f_{A,Y},
\]

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})
=
2f_{A,Y}.
\]

The \(T\)-slope is:

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}.
\]

---

# 6. Minimal missing finite source-jet theorem

The table above is not evaluable to \(e_{A,Y},f_{A,Y}\) unless the following theorem/table is supplied:

\[
\boxed{
\text{Finite midpoint source-jet realization through order }9.
}
\]

Required data:

\[
q_0^{(k)}(m),\qquad 0\le k\le9,
\]

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9.
\]

Equivalent coefficient-table form:

\[
W_{+,0..3},
\quad
\Lambda^-_{1,0..3},
\quad
\Lambda^-_{5,0..3},
\]

\[
Y^{dd}_{4..7,0},
\quad
Y^{d\eta+\eta d}_{4..7,0},
\quad
Y^{\eta\eta}_{4..7,0}.
\]

No supplied structural identity currently forces:

\[
E_{A,Y}^{\mathrm{BC}}=0,
\]

\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

or

\[
f_{A,Y}=0.
\]

The prompt itself notes that earlier work had derived the recurrence shape but not the scalar midpoint jet table needed to evaluate \(E_{A,Y}^{\mathrm{BC}}=eI+fS\). 
## User (2026-04-25 11:50:20)

ok attack that theorem

## Assistant (2026-04-25 11:50:21)

I’ll attack the missing “finite midpoint source-jet realization through order 9” theorem directly: first try to derive the jets/tables from the draft’s definitions, then isolate exactly where derivation stops.

_Thought for 47s_

## Agent 8 — attack on the finite midpoint source-jet realization theorem

I interpret “that theorem” as the missing local theorem:

\[
\boxed{
\text{Finite midpoint source-jet realization through order }9
}
\]

needed to evaluate

\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S.
\]

I attacked it in two ways:

1. Try to derive the required coefficient arrays from the draft’s Fréchet/Sylvester machinery.
2. Test whether the scalar jets are actually determined by the existing source normalizations, affine removal, source-grade reflection, one-amplitude collapse, or collision edge laws.

Result:

\[
\boxed{
\text{The recurrence machinery derives the coefficient arrays from finite jets,}
}
\]

but

\[
\boxed{
\text{the draft does not determine those finite jets.}
}
\]

So the missing theorem is not “write the Sylvester recurrence.” That part is available. The missing theorem is a **finite source-jet closure theorem** saying the required jets are either explicitly fixed or irrelevant modulo the two tests

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
\qquad
f_{A,Y}.
\]

The active \(E_{A,Y}^{\mathrm{BC}}\) carrier is the frozen internal coefficient, not the internal \([z^7\delta^1]\) coefficient, because \(a_1a_2(a_1+a_2)\) already supplies the \(\delta\)-edge on the collision chart. The current finite table depends on \(W_{+,0..3}\), \(\Lambda^-_{a,0..3}\), and \(Y^\chi_{4..7,0}\), and the working prompt identifies \(q_0^{(k)}(m)\) and \((r_i^{[a]})^{(k)}(m)\) as the scalar source jets thought necessary. 

---

# 1. What can be derived

## 1.1 Baseline whitening coefficients \(W_{+,0},\dots,W_{+,3}\)

Let

\[
G_+^{(0)}(z)=G_{+,0}+zG_{+,1}+z^2G_{+,2}+z^3G_{+,3}+O(z^4),
\]

and

\[
W_+(z):=G_+^{(0)}(z)^{-1/2}
=
W_{+,0}+zW_{+,1}+z^2W_{+,2}+z^3W_{+,3}+O(z^4).
\]

Equivalently,

\[
W_+(z)G_+^{(0)}(z)W_+(z)=I.
\]

The coefficients are determined recursively by Sylvester equations.

Define

\[
\mathcal L_+(X):=XG_{+,0}W_{+,0}+W_{+,0}G_{+,0}X.
\]

Then:

\[
W_{+,0}=G_{+,0}^{-1/2}.
\]

For \(n\ge1\),

\[
\boxed{
\mathcal L_+(W_{+,n})
=
-
\sum_{\substack{i+j+k=n\\(i,k)\ne(n,0),(0,n)}}
W_{+,i}G_{+,j}W_{+,k}.
}
\]

Explicitly:

\[
\mathcal L_+(W_{+,1})
=
-W_{+,0}G_{+,1}W_{+,0}.
\]

\[
\mathcal L_+(W_{+,2})
=
-\Bigl(
W_{+,0}G_{+,2}W_{+,0}
+
W_{+,1}G_{+,1}W_{+,0}
+
W_{+,0}G_{+,1}W_{+,1}
+
W_{+,1}G_{+,0}W_{+,1}
\Bigr).
\]

\[
\begin{aligned}
\mathcal L_+(W_{+,3})
=
-\Bigl(&
W_{+,0}G_{+,3}W_{+,0}
+W_{+,1}G_{+,2}W_{+,0}
+W_{+,0}G_{+,2}W_{+,1}\\
&+W_{+,2}G_{+,1}W_{+,0}
+W_{+,0}G_{+,1}W_{+,2}
+W_{+,1}G_{+,1}W_{+,1}\\
&+W_{+,2}G_{+,0}W_{+,1}
+W_{+,1}G_{+,0}W_{+,2}
\Bigr).
\end{aligned}
\]

So \(W_{+,0..3}\) is derivable once \(G_{+,0..3}\) is known.

For the baseline same-point block, \(G_{+,n}\) is determined by the midpoint expansion of the baseline \(q_0\)-jet. Since \(G^{(0)}\) contains \(q_0,q_0',q_0''\), expansion through \(z^3\) requires at least

\[
\boxed{
q_0^{(k)}(m),\qquad 0\le k\le5
}
\]

for \(W_{+,0..3}\) alone.

Thus \(W_{+,0..3}\) does **not** require the full \(q_0^{(0..9)}\) range by itself. The larger range enters through the mixed Hessian rows.

---

## 1.2 Same-point linear whitening coefficients \(\Lambda^-_{a,0},\dots,\Lambda^-_{a,3}\)

Let the same-point source-linear perturbation be

\[
X^-_a(z)
=
X^-_{a,0}+zX^-_{a,1}+z^2X^-_{a,2}+z^3X^-_{a,3}+O(z^4),
\qquad
a\in\{1,5\}.
\]

Let

\[
\Lambda^-_a(z)
:=
D(G_-^{(0)}(z)^{-1/2})[X^-_a(z)]
=
\sum_{r=0}^{3}z^r\Lambda^-_{a,r}+O(z^4).
\]

For each \(z\), the Fréchet inverse-square-root variation \(\Lambda^-_a\) is determined by the linearized equation

\[
\Lambda^-_aG_-^{(0)}W_-
+
W_-X^-_aW_-
+
W_-G_-^{(0)}\Lambda^-_a=0.
\]

Coefficientwise, with

\[
W_-(z)=\sum_{j\ge0}z^jW_{-,j},
\qquad
G_-^{(0)}(z)=\sum_{j\ge0}z^jG_{-,j},
\]

the unknown \(\Lambda^-_{a,r}\) satisfies a Sylvester equation with the same invertible operator

\[
\mathcal L_-(X):=XG_{-,0}W_{-,0}+W_{-,0}G_{-,0}X.
\]

The recursion is:

\[
\boxed{
\mathcal L_-(\Lambda^-_{a,r})
=
-\Bigl[
z^r
\Bigr]
\left(
W_-X^-_aW_-
+
\Lambda^-_aG_-^{(0)}W_-
+
W_-G_-^{(0)}\Lambda^-_a
-
\mathcal L_-(\Lambda^-_{a,r})z^r
\right).
}
\]

Equivalently, \(\Lambda^-_{a,r}\) is determined by:

\[
G_{-,0..r},
\qquad
W_{-,0..r},
\qquad
X^-_{a,0..r}.
\]

The draft’s current conventions do **not** force

\[
X^-_{a,3}=0
\quad\text{or}\quad
\Lambda^-_{a,3}=0.
\]

Nor do they remove either

\[
a=1
\quad\text{or}\quad
a=5.
\]

So both source slots remain live.

For \(\Lambda^-_{a,0..3}\) alone, the minimal source-jet range is at most

\[
(r_i^{[a]})^{(k)}(m),
\qquad
i=1,2,\quad a\in\{1,5\},\quad 2\le k\le5,
\]

assuming the same-point source-linear block depends on up to second derivatives of the source primitive. The safe range remains \(2\le k\le9\), because the mixed Hessian terms below may require it.

---

## 1.3 Mixed Hessian coefficients \(Y^\chi_{g,0}\)

The promoted carrier is

\[
Y_{12}^{(2)}
=
D^2N_0[\xi_1,\xi_2],
\]

with surviving symmetric channels

\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}.
\]

So:

\[
Y^\chi_{g,0}
=
[z^g]Y_\chi^{(2)}\big|_{\delta=0},
\qquad
4\le g\le7.
\]

The skew channel

\[
Y_{d\eta-\eta d}^{(2)}
\]

is killed by fixed-sector projection and remains excluded. The current prompts explicitly say the surviving rows are \(dd\), \(d\eta+\eta d\), and \(\eta\eta\), while the skew row is removed. 

The key point: \(Y^\chi_{g,0}\) is not an independent analytic object. It is a finite polynomial expression in:

\[
q_0^{(j)}(m),
\qquad
(r_i^{[a]})^{(j)}(m),
\]

obtained by differentiating the corrected mixed block

\[
N^{\corr}(q_-,q_+,\Delta;s)
\]

twice in the source directions.

However, the draft does **not** currently provide the finite scalar table for the underlying source jets \(d_{i,\pm}(z)\), \(\eta_i(z)\), or the underlying \(r_i^{[a]}\)-jets through the required order. The latest prompts state that the finite Fréchet/Sylvester machinery gives the shape of \(E_{A,Y}^{\mathrm{BC}}\), but the draft does not yet supply the scalar midpoint jet table needed to evaluate \(eI+fS\). 

For \(Y^\chi_{g,0}\) with \(4\le g\le7\), the safe dependency is:

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

The \(+2\) margin is natural because the corrected same-point and mixed blocks contain second-jet data; extracting \(z^7\) can therefore require source primitives through order \(9\).

---

# 2. Can the theorem be proved structurally without computing the jets?

I tested the available structural mechanisms against the two needed outputs:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

and

\[
f_{A,Y}=0.
\]

## 2.1 Endpoint swap / transpose symmetry

Endpoint swap and transpose symmetry justify using

\[
\operatorname{Sym}(\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b})
\]

and kill the skew \(d\eta-\eta d\) row.

But after symmetrization the surviving rows are precisely fixed-sector rows. They are not skew. Therefore endpoint swap does **not** imply

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

It also does not imply line-gauge:

\[
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f}.
\]

Nor does it imply transform safety:

\[
f_{A,Y}=0.
\]

## 2.2 Source-grade reflection

Source-grade reflection controls signs under endpoint exchange. It was enough to close the \(M_A,M_C\) pre-trivialization connection table, but here the row is deliberately the symmetric survivor. So the same parity mechanism does not remove it.

## 2.3 Affine removal

Affine removal kills the \(2\)-jet affine-boundary mode. It does not kill the grade \(a=1\) and \(a=5\) same-point linear whitening slots in the promoted \(Y_{12}^{(2)}\) carrier. In particular, nothing in the stated convention forces:

\[
\Lambda^-_{1,r}=0
\quad\text{or}\quad
\Lambda^-_{5,r}=0,
\qquad
0\le r\le3.
\]

## 2.4 One-amplitude collapse / source-bidegree projection

One-amplitude collapse removes irrelevant nonmixed layers. But this carrier is explicitly mixed and non-\((1,1)\) after the external amplitude factor:

\[
a_1a_2(a_1+a_2).
\]

This is exactly why it is a Bottleneck-C carrier. The source-bidegree projection does not remove it.

## 2.5 Collision divisibility

Collision divisibility explains why the amplitude factor contributes the first \(\delta\)-edge:

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2).
\]

It does not constrain the frozen internal coefficient

\[
E_{A,Y}^{\mathrm{BC}}.
\]

## 2.6 Fixed-sector structure

The fixed-sector projection maps a surviving symmetric row to

\[
eI+fS.
\]

The quotient test and \(T\)-test are independent:

\[
Q_{A,Y}=ev_5-u_5f,
\qquad
\Phi_K(E_{A,Y}^{\mathrm{BC}})=2f.
\]

Nothing in the current structural package forces either scalar to vanish. The prompts explicitly identify these as the two decisive local tests. 

---

# 3. Formal obstruction to proving the theorem from existing assumptions

The missing theorem would have to say that the finite source jets are fixed, or that all their possible contributions cancel in the two target scalars.

But as currently stated, the finite source jets behave as free local parameters subject only to parity/affine/collision constraints. Those constraints are insufficient.

A small formal model shows the gap.

Let one surviving row contribute

\[
\operatorname{Sym}(\Lambda^-_{1,0}Y^{dd}_{4,0}W_{+,3})
=
\mu I+\nu S.
\]

The existing symmetries only require this row to be fixed-sector symmetric. They do not impose

\[
\mu v_5-u_5\nu=0
\]

or

\[
\nu=0.
\]

By perturbing a single underlying source jet, for example one component of

\[
(r_i^{[1]})^{(9)}(m),
\]

one can formally alter \(\nu\) while preserving endpoint-symmetric status and without changing the abstract parity class. Therefore:

\[
f_{A,Y}
\]

is not structurally fixed by the stated conventions.

This does not prove the actual zeta source has such a perturbation. It proves the current draft has not supplied the theorem that rules it out.

---

# 4. Exact missing theorem, strengthened form

The theorem needed is stronger than “the jets exist.” Existence is automatic for analytic local functions. What is needed is either an explicit finite table or a structural vanishing theorem for the two scalar outputs.

## Option A: explicit finite midpoint source-jet table

```tex
\begin{theorem}[Finite midpoint source-jet realization through order 9]
\label{thm:finite-midpoint-source-jet-realization-order-nine}
On the active good patch, the baseline and source primitives determining the
promoted mixed-block Bottleneck-C carrier have midpoint jets
\[
q_0^{(k)}(m),\qquad 0\le k\le 9,
\]
and
\[
(r_i^{[a]})^{(k)}(m),
\qquad i=1,2,\quad a\in\{1,5\},\quad 2\le k\le9,
\]
given by the explicit finite table
\[
\mathcal J_9(m).
\]
Substituting \(\mathcal J_9(m)\) into the Sylvester recurrences for
\[
W_{+,0..3},
\qquad
\Lambda^-_{1,0..3},
\qquad
\Lambda^-_{5,0..3},
\]
and into the corrected mixed-block Hessian coefficients
\[
Y^{dd}_{4..7,0},
\qquad
Y^{d\eta+\eta d}_{4..7,0},
\qquad
Y^{\eta\eta}_{4..7,0},
\]
determines
\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S.
\]
\end{theorem}
```

This theorem is computational/table-based. It does not by itself prove closure; it makes the computation well-defined.

## Option B: scalar closure theorem, more useful

```tex
\begin{theorem}[Promoted mixed-block Bottleneck-C scalar closure]
\label{thm:promoted-mixed-block-bc-scalar-closure}
For the promoted mixed-block carrier
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b},
\]
write
\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S.
\]
Then
\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\]
and
\[
f_{A,Y}=0.
\]
Equivalently, on the generic \(v_5\ne0\) patch,
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
\end{theorem}
```

This is the theorem that actually closes both quotient Bottleneck C and \(T\)-horizontal merger for this carrier.

## Option C: weaker quotient-only theorem

```tex
\begin{theorem}[Promoted mixed-block quotient-line theorem]
\label{thm:promoted-mixed-block-quotient-line}
The promoted carrier satisfies
\[
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f}(m),
\]
equivalently
\[
e_{A,Y}v_5-u_5f_{A,Y}=0.
\]
\end{theorem}
```

This closes quotient Bottleneck C but not the augmented transform-safe package. If

\[
E_{A,Y}^{\mathrm{BC}}=\lambda A_5^{\mathfrak f},
\]

then

\[
\partial_\kappa T
=
-a_1^2\lambda\frac{v_5}{c},
\]

so on the generic \(v_5\ne0\) patch this still leaks unless \(\lambda=0\).

---

# 5. Conclusion

The attacked theorem does **not** currently follow from the draft.

What follows is:

\[
\boxed{
W_{+,0..3},\ \Lambda^-_{a,0..3},\ Y^\chi_{4..7,0}
\text{ are recursively computable from finite source jets.}
}
\]

What does **not** follow is:

\[
\boxed{
\text{the required finite source jets are fixed by existing definitions,}
}
\]

or

\[
\boxed{
Q_{A,Y}=0,\quad f_{A,Y}=0
\text{ structurally.}
}
\]

So the exact live obstruction remains:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
=
e_{A,Y}I+f_{A,Y}S
}
\]

with unresolved scalars

\[
\boxed{
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y},
\qquad
f_{A,Y}.
}
\]

The minimal missing input is not a vague “coefficient table.” It is one of:

\[
\boxed{
\text{an explicit order-9 midpoint source-jet table,}
}
\]

or preferably

\[
\boxed{
\text{a promoted mixed-block scalar closure theorem proving }
Q_{A,Y}=0
\text{ and }
f_{A,Y}=0.
}
\]
## User (2026-04-25 11:58:01)

you are the "next local agent" here

## Assistant (2026-04-25 11:58:21)

_Thought for 18s_

## Next local agent — attack on promoted mixed-block scalar closure

Target:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

Given contraction:

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

The instruction explicitly says not to rederive the row table; the current task is to attack the structural scalar closure theorem itself. 

My conclusion:

\[
\boxed{
\text{The promoted mixed-block scalar closure theorem is not forced by the stated structural conventions.}
}
\]

More sharply:

\[
\boxed{
\text{endpoint symmetry, source-grade reflection, fixed-sector projection, and symmetrization permit a nonzero }S\text{-component.}
}
\]

So neither

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

nor

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=0
\]

nor

\[
f_{A,Y}=0
\]

follows formally from the current stated hypotheses.

---

# 1. What the structural symmetries actually give

The active coefficient is the frozen Bottleneck-C coefficient, because the amplitude factor

\[
a_1a_2(a_1+a_2)
\]

already supplies the first collision-chart \(\delta\)-edge. The active coefficient is therefore the symmetrized \([z^7]\) contraction, not the internal \([z^7\delta^1]\) source-position coefficient. 

The surviving channels are:

\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta.
\]

The killed channel is:

\[
d\eta-\eta d.
\]

Thus the available symmetries imply only:

\[
E_{A,Y}^{\mathrm{BC}}\in\mathfrak f_m
=
\mathbf C I\oplus \mathbf C S.
\]

They do **not** imply:

\[
E_{A,Y}^{\mathrm{BC}}\in \mathbf C A_5^{\mathfrak f},
\]

and they do **not** imply:

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})=0.
\]

The distinction matters because if

\[
E_{A,Y}^{\mathrm{BC}}=eI+fS,
\]

then quotient Bottleneck-C closure requires

\[
Q_{A,Y}=ev_5-u_5f=0,
\]

while transform-safe / \(T\)-horizontal closure requires

\[
f=0.
\]

The current proof frontier explicitly identifies these as two different tests. 

---

# 2. Channel-by-channel cancellation is not forced

Write:

\[
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}
+
E_{d\eta+\eta d}
+
E_{\eta\eta}.
\]

The current hypotheses allow each channel to land in the fixed sector:

\[
E_{\chi}=e_\chi I+f_\chi S.
\]

Endpoint transpose symmetry only says the row is admissible under the symmetrized fixed-sector projection. It does not impose either:

\[
f_\chi=0
\]

or

\[
e_\chi v_5-u_5f_\chi=0.
\]

Thus no channel-by-channel vanishing theorem follows.

In particular, the \(dd\)-channel can carry an \(S\)-component. The symmetrized \(dd\)-channel is not skew; it is exactly one of the surviving rows.

---

# 3. Cancellation between \(a=1\) and \(a=5\) is not forced

Split:

\[
E_{A,Y}^{\mathrm{BC}}
=
E^{(1)}+E^{(5)}.
\]

The source-grade conventions keep \(a=1\) and \(a=5\) as active same-point linear source slots. No stated convention gives an identity of the form:

\[
E^{(1)}=-E^{(5)},
\]

or even:

\[
f^{(1)}=-f^{(5)}.
\]

Nor does affine removal remove either slot. The current active row set explicitly keeps

\[
a\in\{1,5\}.
\]

Therefore \(a=1/5\) cancellation cannot be used unless a new relation between the source jets is supplied.

---

# 4. Cancellation between \(r,b\) partitions is not forced

At fixed \(g\), the rows are:

\[
\sum_{r+b=7-g}
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}.
\]

This has the form of a convolution, but not a telescoping sum.

A telescoping cancellation would require a relation such as:

\[
\sum_{r+b=N}
\Lambda^-_{a,r}(\cdot)W_{+,b}
=
0
\]

or a Sylvester identity identifying this convolution as a derivative of a normalized identity. The present setup does not give such an identity for the mixed Hessian insertion

\[
Y_{12}^{(2)}.
\]

The Sylvester recurrences define the coefficients \(W_{+,b}\) and \(\Lambda^-_{a,r}\), but they do not force their convolution with \(Y^\chi_{g,0}\) to vanish.

---

# 5. Pairing against \(A_5^{\mathfrak f}\) is not forced

Let

\[
A_5^{\mathfrak f}=u_5I+v_5S.
\]

A row

\[
E=eI+fS
\]

is quotient-invisible iff

\[
ev_5-u_5f=0.
\]

The structural operations

\[
\tau_{h\to m},
\qquad
\pi_{\mathfrak f_h},
\qquad
\operatorname{Sym}
\]

put the row in the fixed sector. They do not impose the determinant relation

\[
ev_5-u_5f=0.
\]

Thus line-gauge closure is an additional theorem, not a consequence of fixed-sector symmetry.

---

# 6. Applying \(\Phi_K\) is not forced to vanish

The transform-visible functional is:

\[
\Phi_K(eI+fS)=2f.
\]

So transform-safe closure is exactly:

\[
f=0.
\]

But \(S\) is a fixed-sector basis direction, not a skew direction. Therefore no transpose/skew argument kills it.

This is the same hidden-state problem already identified: quotient-invisible line shifts can still be \(\Phi_K\)-visible when \(v_5\ne0\). 

---

# 7. Formal model showing nonzero \(f_{A,Y}\)

This model respects the stated local source conventions: it keeps only a surviving symmetric channel, uses the frozen coefficient, and kills the skew channel.

Take the fixed sector

\[
\mathfrak f_m=\mathbf C I\oplus\mathbf C S,
\]

with

\[
\Phi_K(I)=0,
\qquad
\Phi_K(S)=2.
\]

Let

\[
A_5^{\mathfrak f}=u_5I+v_5S.
\]

Choose a trivial baseline whitening model:

\[
W_{+,0}=I,
\qquad
W_{+,b}=0\quad(b>0),
\]

and choose one nonzero same-point whitening source slot:

\[
\Lambda^-_{1,0}=I,
\qquad
\Lambda^-_{a,r}=0
\quad\text{for all other }(a,r).
\]

Choose one surviving mixed Hessian coefficient in the \(dd\)-channel:

\[
Y^{dd}_{7,0}=S,
\]

and set all other \(Y^\chi_{g,0}\) to zero.

Then the active contraction gives:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}(I\cdot S\cdot I)
=
S.
\]

So:

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

Therefore:

\[
\Phi_K(E_{A,Y}^{\mathrm{BC}})=2,
\]

and

\[
\partial_\kappa T=-a_1^2/c.
\]

The quotient determinant is:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=-u_5.
\]

On a generic patch with

\[
u_5\ne0,
\]

quotient Bottleneck-C fails. Even on a patch where \(u_5=0\), the \(T\)-horizontal condition still fails because

\[
f_{A,Y}=1.
\]

Thus the structural conventions permit a nonzero transform-visible obstruction.

---

# 8. Formal model showing line-gauge but \(T\)-leaking

There is also a model showing that quotient closure is insufficient.

Set instead:

\[
Y^{dd}_{7,0}=A_5^{\mathfrak f}.
\]

Then:

\[
E_{A,Y}^{\mathrm{BC}}=A_5^{\mathfrak f}.
\]

Hence:

\[
Q_{A,Y}
=
u_5v_5-u_5v_5
=
0.
\]

So quotient Bottleneck-C closes.

But:

\[
f_{A,Y}=v_5.
\]

On the generic patch

\[
v_5\ne0,
\]

the transform-safe condition fails:

\[
\partial_\kappa T
=
-a_1^2\frac{v_5}{c}
\ne0.
\]

So even a successful line-gauge theorem would not be sufficient for the augmented package. The local theorem needed is full scalar closure:

\[
E_{A,Y}^{\mathrm{BC}}=0
\]

or at least the simultaneous conditions:

\[
Q_{A,Y}=0,
\qquad
f_{A,Y}=0.
\]

---

# 9. Why this is within the current source conventions

The model uses only a surviving row:

\[
\chi=dd,\qquad a=1,\qquad g=7,\qquad r=0,\qquad b=0.
\]

This row is part of the active finite contraction:

\[
\Lambda^-_{1,0}Y^{dd}_{7,0}W_{+,0}.
\]

It does not use the skew row \(Y_{d\eta-\eta d}^{(2)}\).

It does not use the internal \([z^7\delta^1]\) source-position coefficient.

It respects the frozen Bottleneck-C bookkeeping correction.

It lands in the fixed sector after symmetrization.

Therefore it is not excluded by the known parity, projection, or source-grade conventions.

The only way to eliminate it is to add a genuine structural theorem about the actual mixed Hessian coefficient \(Y^{dd}_{7,0}\), or about its contraction with \(\Lambda^-_{a,r}\) and \(W_{+,b}\).

---

# 10. Result

The promoted mixed-block scalar closure theorem is **not proved** and is **not formally implied** by the currently stated local structure.

The exact missing theorem is:

```latex
\begin{theorem}[Promoted mixed-block scalar closure]
For the frozen Bottleneck-C coefficient
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b},
\]
one has
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
Equivalently, if
\[
E_{A,Y}^{\mathrm{BC}}=e_{A,Y}I+f_{A,Y}S,
\]
then
\[
e_{A,Y}v_5-u_5f_{A,Y}=0
\quad\text{and}\quad
f_{A,Y}=0.
\]
\end{theorem}
```

A quotient-only theorem would be:

```latex
\begin{theorem}[Promoted mixed-block quotient closure]
For the same coefficient,
\[
e_{A,Y}v_5-u_5f_{A,Y}=0.
\]
\end{theorem}
```

But this is insufficient for the augmented transform-safe package unless supplemented by:

```latex
\begin{theorem}[Promoted mixed-block \(T\)-horizontal closure]
For the same coefficient,
\[
f_{A,Y}=0.
\]
\end{theorem}
```

Bottom line:

\[
\boxed{
\text{The local proof remains blocked at }E_{A,Y}^{\mathrm{BC}}.
}
\]

The current paper architecture needs a new correction package or a new structural identity that kills the surviving symmetric mixed-Hessian contraction.
## User (2026-04-25 11:59:16)

continue to attack

## Assistant (2026-04-25 11:59:43)

_Thought for 20s_

## Continued local attack — promoted mixed-block scalar closure

I pushed the local theorem one level further. The target remains:

\[
E_{A,Y}^{\mathrm{BC}}=0,
\]

where

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

The current state says this is the frozen Bottleneck-C coefficient, not the internal source-position \([z^7\delta^1]\) coefficient, because the amplitude \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge on the collision chart. 

My conclusion is stronger than before:

\[
\boxed{
\text{The theorem }E_{A,Y}^{\mathrm{BC}}=0
\text{ is not merely unproved; it is formally independent of the stated symmetries.}
}
\]

The current structural assumptions only imply that \(E_{A,Y}^{\mathrm{BC}}\) lands in the fixed sector:

\[
E_{A,Y}^{\mathrm{BC}}\in \mathfrak f_m=\mathbf C I\oplus\mathbf C S.
\]

They do not imply either scalar closure condition:

\[
Q_{A,Y}:=e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

or

\[
f_{A,Y}=0.
\]

Those are the exact quotient and transform-safe conditions identified in the current local target. 

---

# 1. Reduction to row-level obstruction functionals

For each active row define:

\[
\mathcal E^a_{\chi;g,r,b}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)
=
e^a_{\chi;g,r,b}I+f^a_{\chi;g,r,b}S.
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\sum_{a,\chi,g,r,b}\mathcal E^a_{\chi;g,r,b}.
\]

The two decisive scalar functionals are:

\[
\mathcal Q(\mathcal E)
:=
e v_5-u_5f,
\]

\[
\mathcal T(\mathcal E)
:=
f.
\]

Thus:

\[
Q_{A,Y}
=
\sum_{a,\chi,g,r,b}
\mathcal Q(\mathcal E^a_{\chi;g,r,b}),
\]

and

\[
f_{A,Y}
=
\sum_{a,\chi,g,r,b}
\mathcal T(\mathcal E^a_{\chi;g,r,b}).
\]

So the promoted scalar closure theorem is equivalent to the simultaneous identities:

\[
\sum_{a,\chi,g,r,b}
\mathcal Q(\mathcal E^a_{\chi;g,r,b})=0,
\]

\[
\sum_{a,\chi,g,r,b}
\mathcal T(\mathcal E^a_{\chi;g,r,b})=0.
\]

The problem is that the known symmetries do not impose either identity.

---

# 2. Channel-by-channel attack

Split:

\[
E_{A,Y}^{\mathrm{BC}}
=
E_{dd}+E_{d\eta+\eta d}+E_{\eta\eta}.
\]

The skew channel

\[
Y_{d\eta-\eta d}^{(2)}
\]

is killed, but the three displayed channels are explicitly the surviving symmetric channels. The current summary says no further row reduction is justified beyond removing that skew row. 

Therefore each surviving channel may carry:

\[
E_\chi=e_\chi I+f_\chi S.
\]

No available parity principle distinguishes \(I\) from \(S\) inside the fixed sector. Hence no channel-wise theorem follows:

\[
E_\chi=0,
\qquad
e_\chi v_5-u_5f_\chi=0,
\qquad
f_\chi=0.
\]

A formal \(dd\)-only model already violates both desired scalar identities:

\[
E_{dd}=S,\qquad E_{d\eta+\eta d}=0,\qquad E_{\eta\eta}=0.
\]

Then

\[
Q_{A,Y}=-u_5,
\qquad
f_{A,Y}=1.
\]

On a generic patch this is both quotient-visible and \(T\)-visible.

So there is no channel-wise closure.

---

# 3. \(a=1\) versus \(a=5\) cancellation

Split:

\[
E_{A,Y}^{\mathrm{BC}}=E^{(1)}+E^{(5)}.
\]

A cancellation would need:

\[
E^{(1)}=-E^{(5)}
\]

or at least

\[
\mathcal Q(E^{(1)})=-\mathcal Q(E^{(5)}),
\qquad
\mathcal T(E^{(1)})=-\mathcal T(E^{(5)}).
\]

But the active row set explicitly keeps both \(a=1\) and \(a=5\). The known source-grade and affine-removal conventions do not identify the two slots or force one to vanish. Earlier reductions also found that the draft does not force \(X^-_{a,3}=0\), \(\Lambda^-_{a,3}=0\), or removal of either \(a=1\) or \(a=5\). 

Formal obstruction:

\[
E^{(1)}=S,\qquad E^{(5)}=0
\]

is compatible with the stated row-level conventions. Therefore \(a=1/5\) cancellation is not structural.

A theorem closing this route would have to state an actual source identity of the form:

\[
\sum_{g,r,b,\chi}
A_1\Lambda^-_{1,r}Y^\chi_{g,0}W_{+,b}
=
-
\sum_{g,r,b,\chi}
A_5\Lambda^-_{5,r}Y^\chi_{g,0}W_{+,b}
\]

after

\[
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}.
\]

No such identity is present.

---

# 4. \(r,b\)-partition cancellation at fixed \(g\)

At fixed \(a,\chi,g\), the contribution is:

\[
C^a_{\chi,g}
=
\sum_{r+b=7-g}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

This is a convolution in the inverse-square-root coefficients. A cancellation would need a Sylvester-derived telescoping identity:

\[
\sum_{r+b=N}
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\in
\ker \pi_{\mathfrak f},
\]

or

\[
\sum_{r+b=N}
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
=0,
\]

or at least its \(\mathcal Q\)- and \(\mathcal T\)-projections vanish.

But the Sylvester recurrences determine \(W_{+,b}\) and \(\Lambda^-_{a,r}\); they do not imply that a convolution with an arbitrary surviving mixed Hessian coefficient \(Y^\chi_{g,0}\) telescopes.

Formal obstruction at fixed \(g=7\):

\[
r=b=0
\]

is the only partition. There is no \(r,b\)-partition partner available. Therefore any universal \(r,b\)-partition cancellation cannot eliminate the row:

\[
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}).
\]

So if scalar closure is true, it must already kill the top \(g=7\) row by a separate structural property of \(Y^\chi_{7,0}\), not by \(r,b\)-partition telescoping.

---

# 5. Top-row obstruction

The hardest obstruction is the top-order row:

\[
\mathcal E^a_{\chi;7,0,0}
=
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}
\right).
\]

There is no partition cancellation for \(g=7\). There is no \(b>0\) or \(r>0\) term at the same \(g\). Therefore scalar closure requires:

\[
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\mathcal E^a_{\chi;7,0,0}
\]

to vanish, or at least satisfy the two scalar constraints.

This is a much sharper missing theorem:

\[
\boxed{
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}
\right)
=0
}
\]

or at least

\[
\boxed{
\mathcal Q\left(
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0})
\right)=0,
}
\]

\[
\boxed{
\mathcal T\left(
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0})
\right)=0.
}
\]

If the top-row theorem fails, the whole promoted scalar closure theorem fails.

---

# 6. Formal top-row countermodel

Work in the fixed sector:

\[
\mathfrak f_m=\mathbf C I\oplus \mathbf C S.
\]

Choose:

\[
W_{+,0}=I,
\qquad
\Lambda^-_{1,0}=I,
\qquad
A_1=1,
\]

and set all other \(a=5\), \(r>0\), \(b>0\), and non-\(dd\) rows to zero.

Choose:

\[
Y^{dd}_{7,0}=S.
\]

Then:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}(S)
=
S.
\]

Thus:

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

So:

\[
Q_{A,Y}=-u_5,
\]

and

\[
\partial_\kappa T
=
-a_1^2/c.
\]

This model uses only the surviving \(dd\)-channel, the \(a=1\) source slot, and the top \(g=7,r=0,b=0\) row. It does not rely on any killed skew piece or source-position \(\delta^1\) term.

Therefore the currently stated source conventions do not imply scalar closure.

---

# 7. Line-gauge countermodel

The quotient-only theorem is also insufficient for the augmented package.

Set:

\[
Y^{dd}_{7,0}=A_5^{\mathfrak f}=u_5I+v_5S.
\]

Then:

\[
E_{A,Y}^{\mathrm{BC}}=A_5^{\mathfrak f}.
\]

So

\[
Q_{A,Y}=u_5v_5-u_5v_5=0.
\]

But

\[
f_{A,Y}=v_5.
\]

Hence on the generic \(v_5\ne0\) patch:

\[
\partial_\kappa T
=
-a_1^2v_5/c\ne0.
\]

This confirms the current strategic warning: quotient closure alone is not enough because the augmented transform-safe package requires \(T\)-horizontal closure. The current background explicitly separates these two conditions. 

---

# 8. What theorem would actually close the top-row obstruction?

The minimal theorem is not the full 60-row closure. It is first the top-row scalar closure:

```latex
\begin{lemma}[Top-row promoted mixed-block scalar closure]
For the frozen promoted mixed-block carrier, the top row satisfies
\[
\sum_{a\in\{1,5\}}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}
\right)
=0.
\]
Equivalently, if this sum is \(e_7I+f_7S\), then
\[
e_7v_5-u_5f_7=0,
\qquad
f_7=0.
\]
\end{lemma}
```

If this top-row lemma is unavailable, the full theorem is not credible.

If it is available, then the next layers are:

\[
g=6:\quad r+b=1,
\]

\[
g=5:\quad r+b=2,
\]

\[
g=4:\quad r+b=3.
\]

So the promoted closure can be attacked by descending \(g\)-layers:

\[
E_{A,Y}^{\mathrm{BC}}=E_7+E_6+E_5+E_4.
\]

where

\[
E_g
=
\sum_{a,\chi}
\sum_{r+b=7-g}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}).
\]

The required scalar closure is:

\[
E_7+E_6+E_5+E_4=0.
\]

But because \(E_7\) has no \(r,b\)-partition partner, it is the first independent obstruction.

---

# 9. Layer-wise obstruction theorem

The local attack now reduces to the following finite hierarchy:

\[
E_7=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}),
\]

\[
E_6=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{6,0}W_{+,1}
+
A_a\Lambda^-_{a,1}Y^\chi_{6,0}W_{+,0}
\right),
\]

\[
E_5=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{5,0}W_{+,2}
+
A_a\Lambda^-_{a,1}Y^\chi_{5,0}W_{+,1}
+
A_a\Lambda^-_{a,2}Y^\chi_{5,0}W_{+,0}
\right),
\]

\[
E_4=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{4,0}W_{+,3}
+
A_a\Lambda^-_{a,1}Y^\chi_{4,0}W_{+,2}
+
A_a\Lambda^-_{a,2}Y^\chi_{4,0}W_{+,1}
+
A_a\Lambda^-_{a,3}Y^\chi_{4,0}W_{+,0}
\right).
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}=E_7+E_6+E_5+E_4.
\]

A plausible closure theorem would need to prove either:

\[
E_g=0
\quad
\text{for each }g=4,5,6,7,
\]

or a cross-layer cancellation:

\[
E_7+E_6+E_5+E_4=0.
\]

But a cross-layer cancellation would require relations among the independent mixed-Hessian coefficients

\[
Y^\chi_{7,0},Y^\chi_{6,0},Y^\chi_{5,0},Y^\chi_{4,0}.
\]

No current source convention supplies such relations.

---

# 10. Final status of continued attack

The promoted mixed-block scalar closure theorem is blocked already at the top layer:

\[
\boxed{
E_7.
}
\]

The cleanest obstruction is:

\[
\boxed{
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_1\Lambda^-_{1,0}Y^{dd}_{7,0}W_{+,0})
}
\]

because it has no \(r,b\)-partition cancellation partner and lies in a surviving symmetric channel.

A formal model within the current row conventions gives:

\[
E_7=S,
\]

hence:

\[
Q_{A,Y}=-u_5,
\qquad
f_{A,Y}=1.
\]

So the current proof requires a genuinely new top-row identity, not more bookkeeping.

The exact missing theorem is:

\[
\boxed{
E_7=0
}
\]

or at least:

\[
\boxed{
\mathcal Q(E_7)=0
\quad\text{and}\quad
\mathcal T(E_7)=0.
}
\]

Without this, the promoted mixed-block channel remains a live local countermodel to Bottleneck C and to \(T\)-horizontal merger.
## User (2026-04-25 12:00:48)

continue to attack

## Assistant (2026-04-25 12:00:50)

I’ll continue from the top-row obstruction \(E_7\), not repeat the 60-row table. The next useful attack is to see whether \(Y^{dd}_{7,0}\) or the \(a=1,5\) top-row sum is structurally forced to vanish, line-gauge, or \(\Phi_K\)-invisible.

_Thought for 36s_

## Continued attack — hidden parity route for \(E_{A,Y}^{\mathrm{BC}}\)

I attacked the most plausible remaining structural escape: maybe the frozen coefficient is actually killed by a hidden parity under endpoint-transpose reflection. If that worked, it could eliminate \(E_{A,Y}^{\mathrm{BC}}\) without computing the missing source jets.

The result is conditional:

\[
\boxed{
\text{A specific ordinary-order reflection parity would kill the top obstruction,}
}
\]

but

\[
\boxed{
\text{the current draft/prompt state does not supply that parity for }Y_{12}^{(2)}.
}
\]

So this attack produces a sharper missing lemma: **frozen quadratic-Hessian reflection parity**.

The active coefficient remains the frozen Bottleneck-C coefficient

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b},
\]

not the internal source-position edge table; the amplitude \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge on the collision chart. 

---

# 1. Reflection-parity setup

Let \(\mathscr R\) denote the endpoint-swap-plus-transpose involution. For a row

\[
T^a_{\chi;g,r,b}
:=
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b},
\]

the fixed-sector symmetrized projection keeps the \(\mathscr R\)-even part and kills the \(\mathscr R\)-odd part.

So the row is killed if

\[
\mathscr R(T^a_{\chi;g,r,b})=-T^a_{\chi;g,r,b}
\]

after matching left/right endpoints.

A natural parity ansatz is:

\[
\mathscr R(\Lambda^-_{a,r})=(-1)^r\Lambda^+_{a,r},
\]

\[
\mathscr R(W_{+,b})=(-1)^bW_{-,b},
\]

and

\[
\mathscr R(Y^\chi_{g,0})=\varepsilon_\chi(g)Y^\chi_{g,0}.
\]

Then the row parity is

\[
(-1)^{r+b}\varepsilon_\chi(g).
\]

Since

\[
r+b=7-g,
\]

the row parity is

\[
(-1)^{7-g}\varepsilon_\chi(g).
\]

Therefore:

\[
\boxed{
T^a_{\chi;g,r,b}
\text{ is killed if }
(-1)^{7-g}\varepsilon_\chi(g)=-1.
}
\]

It survives if

\[
(-1)^{7-g}\varepsilon_\chi(g)=+1.
\]

---

# 2. The parity that would kill everything

If the frozen quadratic Hessian satisfied the ordinary-order reflection law

\[
\boxed{
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0},
}
\]

then

\[
(-1)^{7-g}\varepsilon_\chi(g)
=
(-1)^{7-g}(-1)^g
=
(-1)^7
=
-1.
\]

So every frozen row would be \(\mathscr R\)-odd and hence killed by the fixed-sector projection.

That would prove the strong theorem:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

This is the cleanest possible local closure. It would not merely prove quotient closure; it would also prove

\[
f_{A,Y}=0,
\]

and therefore

\[
\partial_\kappa T=0.
\]

---

# 3. Why this parity is not currently available

The known source-linear \(Y\)-middle parity from the connection branch had the form

\[
(Y_{g,\beta}^{\langle e\rangle})^T=(-1)^{g+e}Y_{g,\beta}^{\langle e\rangle}.
\]

That was used to close the \(M_A,M_C\) pre-trivialization table. The current branch is different:

\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2].
\]

It is a **quadratic Hessian** source block, not the same source-linear \(Y_g\)-middle block.

The present active table explicitly keeps the symmetric Hessian channels

\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta,
\]

and only removes the skew channel

\[
d\eta-\eta d.
\]

The current prompt states that the skew row is excluded but the symmetric rows remain active. 

Thus the draft presently gives:

\[
Y_{d\eta-\eta d}^{(2)} \in \ker\pi_{\mathfrak f},
\]

but it does **not** give:

\[
Y^\chi_{g,0}\in \ker\pi_{\mathfrak f}
\quad
\text{for all }
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]

So the parity that would kill \(E_{A,Y}^{\mathrm{BC}}\) is not established.

---

# 4. Top-row consequence

For the top layer

\[
g=7,\qquad r=b=0,
\]

the row is

\[
E_7
=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}
\right).
\]

The row parity formula becomes

\[
(-1)^{0}\varepsilon_\chi(7)=\varepsilon_\chi(7).
\]

So the top row is killed iff

\[
\varepsilon_\chi(7)=-1
\]

for all surviving \(\chi\).

Equivalently, we need

\[
\boxed{
\mathscr R(Y^\chi_{7,0})=-Y^\chi_{7,0}
\quad
\text{for }
\chi=dd,d\eta+\eta d,\eta\eta.
}
\]

But the current active table treats these rows as fixed-sector surviving candidates. No current source-grade reflection statement supplies the above top-row oddness for the quadratic Hessian.

Thus the top-row obstruction remains:

\[
\boxed{
E_7
=
\sum_{a,\chi}
\tau\pi_{\mathfrak f}
\operatorname{Sym}
(A_a\Lambda^-_{a,0}Y^\chi_{7,0}W_{+,0}).
}
\]

---

# 5. Formal parity countermodel

Take a model in which the frozen Hessian has **even** reflection parity in the \(dd\)-top row:

\[
\mathscr R(Y^{dd}_{7,0})=+Y^{dd}_{7,0}.
\]

Set

\[
W_{+,0}=I,
\qquad
\Lambda^-_{1,0}=I,
\qquad
Y^{dd}_{7,0}=S,
\]

and all other rows zero.

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\pi_{\mathfrak f}\operatorname{Sym}(S)
=
S.
\]

Hence

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

So

\[
Q_{A,Y}=-u_5,
\]

and

\[
\partial_\kappa T=-a_1^2/c.
\]

This model respects the currently stated row restrictions: it uses a surviving symmetric channel, the frozen coefficient, and no \(d\eta-\eta d\) skew row. It violates only the **unproved** odd reflection parity for \(Y^{dd}_{7,0}\).

Therefore the missing issue is exactly the parity of the frozen quadratic Hessian.

---

# 6. The sharp missing lemma

The next local theorem should not be the full 60-row scalar closure. It should first try to prove this smaller parity lemma:

```latex
\begin{lemma}[Frozen quadratic-Hessian reflection parity]
\label{lem:frozen-quadratic-hessian-reflection-parity}
Let
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]
\]
be the promoted quadratic mixed-block Hessian.  For each surviving symmetric
channel
\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\}
\]
and each frozen ordinary coefficient \(Y^\chi_{g,0}\), one has
\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0},
\]
where \(\mathscr R\) is endpoint-swap followed by transpose.
\]
\end{lemma}
```

If this lemma holds, then for every active row with

\[
r+b+g=7,
\]

we get

\[
\mathscr R
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)
=
(-1)^{r+b+g}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)
=
-
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right),
\]

and therefore

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

This would close both local scalar targets:

\[
Q_{A,Y}=0,
\qquad
f_{A,Y}=0.
\]

---

# 7. Alternative weaker lemma

If the full parity lemma is false, one can still close the top row by proving only:

```latex
\begin{lemma}[Top-row frozen Hessian oddness]
\label{lem:top-row-frozen-hessian-oddness}
For
\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\]
the top frozen coefficient satisfies
\[
\mathscr R(Y^\chi_{7,0})=-Y^\chi_{7,0}.
\]
\end{lemma}
```

This kills

\[
E_7.
\]

Then the remaining layers are:

\[
E_6,\quad E_5,\quad E_4.
\]

But without a full parity theorem, those layers would still need separate identities.

---

# 8. Current status after this attack

The attack found a possible route to full local closure:

\[
\boxed{
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}
}
\]

for the frozen quadratic Hessian.

If this ordinary-order reflection parity is true, then:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

But the current draft/prompt only establishes removal of the skew \(d\eta-\eta d\) channel and keeps the symmetric rows active. It does not state or prove the needed parity for the frozen Hessian channels.

So the local obstruction is now sharpened to a single structural question:

\[
\boxed{
\text{Does }D^2N_0[\xi_1,\xi_2]\text{ satisfy frozen ordinary-order reflection parity?}
}
\]

If yes, local Bottleneck C closes for this carrier.

If no, the top-row formal model

\[
Y^{dd}_{7,0}=S
\]

remains a live quotient- and \(T\)-visible obstruction.
## User (2026-04-25 12:02:27)

continue to attack

## Assistant (2026-04-25 12:02:28)

I’ll push directly on the frozen Hessian parity question: whether \(D^2N_0[\xi_1,\xi_2]\) has the ordinary-order reflection sign needed to kill \(E_{A,Y}^{\mathrm{BC}}\).

_Thought for 20s_

## Continued attack — can the Hessian parity actually be derived?

I pushed the previous “hidden parity” route harder.

The possible escape was:

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0},
\]

where \(\mathscr R\) is endpoint-swap plus transpose. If true for every surviving frozen Hessian channel

\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\]

then each active row has parity

\[
(-1)^r(-1)^b(-1)^g=(-1)^{r+b+g}=(-1)^7=-1,
\]

and therefore the fixed-sector symmetrization kills the whole carrier:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

This would close both quotient Bottleneck C and \(T\)-horizontal merger.

But after differentiating the actual endpoint-swap identity, the parity one gets is **not** automatically \((-1)^g\). It is a parity of the **source directions**, not of the final ordinary \(z\)-coefficient. This is the obstruction.

---

# 1. What endpoint-swap functoriality gives for a Hessian

The mixed block satisfies the endpoint-transpose identity

\[
N^{\corr}(h_-,h_+)^T=N^{\corr}(h_+,h_-).
\]

This identity was enough for the source-linear \(Y_g\)-middle table because the source-linear homogeneous grade extraction obeys

\[
\mathsf P_g\circ\mathsf S=(-1)^g\mathsf S\circ\mathsf P_g,
\]

which then gives

\[
Y_g(h_-,h_+)^T=(-1)^gY_g(h_+,h_-).
\]

That closes the \(M_A,M_C\) branch. 

For the quadratic Hessian, differentiating the swap identity gives instead

\[
\mathscr R\left(D^2N_0[\xi_1,\xi_2]\right)
=
D^2N_0[\mathsf S\xi_2,\mathsf S\xi_1].
\]

Because \(D^2N_0\) is symmetric in its two directions,

\[
D^2N_0[\mathsf S\xi_2,\mathsf S\xi_1]
=
D^2N_0[\mathsf S\xi_1,\mathsf S\xi_2].
\]

If \(\xi_1,\xi_2\) have source-reflection signs

\[
\mathsf S\xi_j=(-1)^{p_j}\xi_j,
\]

then

\[
\mathscr R\left(D^2N_0[\xi_1,\xi_2]\right)
=
(-1)^{p_1+p_2}
D^2N_0[\xi_1,\xi_2].
\]

Thus the actual Hessian parity is:

\[
\boxed{
(-1)^{p_1+p_2},
}
\]

not automatically

\[
\boxed{
(-1)^g.
}
\]

To kill \(E_{A,Y}^{\mathrm{BC}}\), the draft would need the extra compatibility

\[
p_1+p_2\equiv g\pmod 2
\]

for every frozen coefficient

\[
Y^\chi_{g,0}.
\]

That compatibility is not currently established.

---

# 2. Why the source-linear proof does not transfer automatically

For source-linear terms, ordinary order \(g\) and reflection grade are locked by the homogeneous scalar-grade convention. That is exactly the statement

\[
\mathsf P_g\circ\mathsf S=(-1)^g\mathsf S\circ\mathsf P_g.
\]

For the quadratic Hessian

\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]

there are now three contributors to the ordinary order \(g\):

1. the order of source direction \(\xi_1\);
2. the order of source direction \(\xi_2\);
3. the ordinary order contributed by the background mixed kernel expansion.

So generally:

\[
g=p_1+p_2+\ell,
\]

where \(\ell\) is the remaining background kernel order.

The endpoint reflection sign sees

\[
p_1+p_2,
\]

but the active row parity needs

\[
g.
\]

Therefore the desired sign is correct only if

\[
\ell\equiv0\pmod2.
\]

No current theorem says the frozen Hessian coefficients \(Y^\chi_{g,0}\) have only even background remainder order \(\ell\).

---

# 3. Channel-level obstruction

For each channel

\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\]

write a frozen Hessian coefficient as a finite sum

\[
Y^\chi_{g,0}
=
\sum_{p_1+p_2+\ell=g}
Y^\chi_{p_1,p_2,\ell}.
\]

Endpoint-swap gives

\[
\mathscr R(Y^\chi_{p_1,p_2,\ell})
=
(-1)^{p_1+p_2}
Y^\chi_{p_1,p_2,\ell}
\]

up to the \(d\eta\leftrightarrow\eta d\) exchange already symmetrized.

The row is killed only if

\[
(-1)^{r+b}(-1)^{p_1+p_2}=-1.
\]

Since

\[
r+b=7-g,
\]

this condition becomes

\[
(-1)^{7-g+p_1+p_2}=-1.
\]

Using \(g=p_1+p_2+\ell\), this is

\[
(-1)^{7-\ell}=-1.
\]

So the row is killed iff

\[
\ell\equiv0\pmod2.
\]

If \(\ell\) is odd, then the row is **even** and survives.

Thus the local problem reduces further:

\[
\boxed{
\text{Do the frozen quadratic-Hessian coefficients contain odd background-order pieces?}
}
\]

If yes, \(E_{A,Y}^{\mathrm{BC}}\) can survive.

If no, the parity route closes the carrier.

---

# 4. The actual missing lemma is narrower

The previously proposed parity lemma

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}
\]

is too blunt. The sharper theorem is:

```latex
\begin{lemma}[Even-background support for the frozen quadratic Hessian]
\label{lem:even-background-support-frozen-quadratic-hessian}
For each surviving channel
\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\}
\]
and each frozen coefficient \(Y^\chi_{g,0}\) of
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
every nonzero summand in the decomposition
\[
Y^\chi_{g,0}
=
\sum_{p_1+p_2+\ell=g}
Y^\chi_{p_1,p_2,\ell}
\]
has even background remainder order
\[
\ell\equiv0\pmod2.
\]
Equivalently,
\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]
\end{lemma}
```

If this lemma holds, then the promoted carrier vanishes:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

---

# 5. Formal odd-background countermodel

The current hypotheses do not exclude \(\ell\) odd.

Take the top row:

\[
g=7,\qquad r=b=0.
\]

Suppose the \(dd\)-channel has a component with

\[
p_1+p_2=6,\qquad \ell=1.
\]

Then

\[
g=p_1+p_2+\ell=7.
\]

Its endpoint-reflection sign is

\[
(-1)^{p_1+p_2}=+1.
\]

Because \(r+b=0\), the full row is also reflection-even and survives fixed-sector symmetrization.

Choose

\[
W_{+,0}=I,
\qquad
\Lambda^-_{1,0}=I,
\qquad
Y^{dd}_{p_1,p_2,\ell}=S.
\]

Then

\[
E_7=S.
\]

Therefore

\[
f_{A,Y}=1,
\qquad
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]

This model is compatible with:

- endpoint-swap functoriality;
- source-reflection signs;
- removal of the skew \(d\eta-\eta d\) row;
- use of the frozen coefficient;
- fixed-sector projection.

It violates only the unproved even-background support lemma.

---

# 6. Can the kernel structure force even \(\ell\)?

This is the one remaining plausible closure mechanism.

If the frozen Hessian \(Y_{12}^{(2)}\) depends on the background midpoint kernel only through even powers of the endpoint separation at \(\delta=0\), then \(\ell\) would be even.

But the current local object is ordinary order in \(z\), not the collision separation \(\delta\). The frozen coefficient is evaluated at the midpoint, but the ordinary \(z\)-expansion of the phase kernel need not contain only even powers. In particular, a sine-type kernel expansion generically has both even and odd ordinary Taylor pieces unless an additional centering or parity theorem is imposed.

Therefore kernel symmetry alone does not currently prove

\[
\ell\equiv0\pmod2.
\]

The draft would need a theorem saying that, after the corrected mixed-block Hessian and source normalizations are applied, every odd-background ordinary-order piece is either:

\[
0,
\qquad
\ker\pi_{\mathfrak f},
\qquad
\mathbf C A_5^{\mathfrak f},
\qquad
\text{or }\ker\Phi_K.
\]

No such theorem is presently stated.

---

# 7. Final status of this attack

The parity route almost gives a clean closure, but it requires a new support theorem:

\[
\boxed{
\ell\equiv0\pmod2
\text{ for every frozen quadratic-Hessian summand.}
}
\]

Without it, an odd-background component produces a fixed-sector survivor.

Thus the local obstruction is now sharpened from:

\[
E_{A,Y}^{\mathrm{BC}}\ ?=0
\]

to the finer question:

\[
\boxed{
\text{Does }Y_{12}^{(2)}\text{ have odd-background frozen Hessian support?}
}
\]

If no odd-background support exists, then

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

If odd-background support exists, the formal countermodel gives a live quotient- and \(T\)-visible obstruction.

The next theorem to attack is therefore:

```latex
\begin{theorem}[No odd-background frozen Hessian support]
\label{thm:no-odd-background-frozen-hessian-support}
For the promoted quadratic mixed-block Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
all frozen ordinary-order contributions surviving in the channels
\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta
\]
have even background remainder order. Equivalently,
\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}
\]
for
\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]
\end{theorem}
```

This is the narrowest structural theorem that would still close the promoted mixed-block Bottleneck-C carrier without explicitly evaluating the 60-row table.
## User (2026-04-25 12:03:48)

continue to attack

## Assistant (2026-04-25 12:03:49)

I’ll now attack the “no odd-background frozen Hessian support” theorem itself, rather than treating it as an abstract missing lemma. The key is to inspect whether the mixed-block Hessian naturally contains odd-background Taylor pieces before projection.

_Thought for 53s_

## Continued attack — kernel-parity route for \(E_{A,Y}^{\mathrm{BC}}\)

I attacked the remaining structural question:

\[
\boxed{
\text{Does }Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]
\text{ have odd-background frozen Hessian support?}
}
\]

This is the right target because, if the frozen quadratic Hessian satisfies

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0},
\]

then every row in

\[
E_{A,Y}^{\mathrm{BC}}
\]

is reflection-odd, since

\[
r+b+g=7,
\]

and hence

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

The current local obstruction is exactly this frozen Bottleneck-C coefficient, not the internal \([z^7\delta^1]\) coefficient, because the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the first collision-chart \(\delta\)-edge. 

---

# 1. Main new observation

For the raw phase-kernel part, the odd-background obstruction appears to be **absent**.

Let

\[
z=x-y,
\qquad
\Delta_0(z)=\Phi(x)-\Phi(y)
\]

on the midpoint-symmetric chart

\[
x=m+\frac z2,
\qquad
y=m-\frac z2.
\]

Then

\[
\Delta_0(-z)=-\Delta_0(z).
\]

The baseline phase kernel has the regularized form

\[
F(\Delta,z)=\frac{\sin\Delta}{\pi z}.
\]

At the frozen midpoint,

\[
F_0(z):=F(\Delta_0(z),z)
\]

is even because

\[
\sin\Delta_0(z)
\]

is odd and \(z\) is odd.

Now inspect the second derivatives that generate the quadratic Hessian channels.

---

## 1.1 \(dd\)-channel

The \(dd\)-channel differentiates twice in the phase/source variable \(\Delta\):

\[
F_{\Delta\Delta}(\Delta,z)
=
-\frac{\sin\Delta}{\pi z}.
\]

At \(\Delta=\Delta_0(z)\),

\[
F_{\Delta\Delta}(\Delta_0(z),z)
=
-\frac{\sin\Delta_0(z)}{\pi z}.
\]

This is even.

So the frozen \(dd\)-background has only even ordinary powers.

---

## 1.2 \(d\eta+\eta d\)-channel

The mixed \(d\eta\) channel differentiates once in \(\Delta\) and once in endpoint displacement / separation. Model this by \(\partial_\Delta\partial_zF\).

First,

\[
F_\Delta(\Delta,z)=\frac{\cos\Delta}{\pi z}.
\]

At \(\Delta_0(z)\),

\[
F_\Delta(\Delta_0(z),z)
=
\frac{\cos\Delta_0(z)}{\pi z}.
\]

Since \(\cos\Delta_0(z)\) is even and \(z\) is odd, this is odd.

Then

\[
\partial_z F_\Delta(\Delta_0(z),z)
\]

is even.

So the frozen \(d\eta+\eta d\)-background is also even.

The antisymmetric piece

\[
d\eta-\eta d
\]

is already skew-killed and is not part of the active table. The active symmetric \(d\eta+\eta d\) channel has even background support.

---

## 1.3 \(\eta\eta\)-channel

The \(\eta\eta\)-channel differentiates twice in endpoint displacement / separation. It is modeled by

\[
\partial_z^2 F(\Delta_0(z),z).
\]

Since

\[
F(\Delta_0(z),z)
\]

is even, its second derivative is also even.

Thus the frozen \(\eta\eta\)-background also has only even ordinary powers.

---

# 2. Consequence for Hessian reflection parity

Decompose each frozen Hessian coefficient as

\[
Y^\chi_{g,0}
=
\sum_{p_1+p_2+\ell=g}
Y^\chi_{p_1,p_2,\ell},
\]

where:

- \(p_1,p_2\) are the source-reflection grades of the two source directions;
- \(\ell\) is the ordinary background order contributed by the kernel coefficient.

Endpoint-transpose reflection gives

\[
\mathscr R(Y^\chi_{p_1,p_2,\ell})
=
(-1)^{p_1+p_2}
Y^\chi_{p_1,p_2,\ell}.
\]

If the background support is even, then

\[
\ell\equiv0\pmod2.
\]

Since

\[
g=p_1+p_2+\ell,
\]

we get

\[
p_1+p_2\equiv g\pmod2.
\]

Therefore

\[
\boxed{
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
}
\]

This is exactly the missing parity needed to kill the promoted carrier.

---

# 3. Closure of \(E_{A,Y}^{\mathrm{BC}}\), conditional on no extra odd correction term

For each active row,

\[
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b},
\]

the reflection signs are:

\[
\mathscr R(\Lambda^-_{a,r})=(-1)^r\Lambda^+_{a,r},
\]

\[
\mathscr R(W_{+,b})=(-1)^bW_{-,b},
\]

and, by the parity result above,

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]

Thus the full row has reflection sign

\[
(-1)^{r+b+g}.
\]

But every active row satisfies

\[
r+b+g=7.
\]

Therefore every active row is reflection-odd:

\[
(-1)^{r+b+g}=-1.
\]

The fixed-sector symmetrization kills reflection-odd rows. Hence:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

This would imply both decisive scalar conditions:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=0,
\]

and

\[
f_{A,Y}=0.
\]

Therefore:

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
0.
\]

So, under this parity theorem, the promoted mixed-block carrier is harmless for both quotient Bottleneck C and the augmented \(T\)-horizontal condition.

---

# 4. What must still be checked in the actual draft

The argument above proves closure for the raw midpoint-symmetric phase-kernel Hessian and for corrections built functorially from the same even-background regularized kernel data.

The remaining check is whether the paper’s corrected mixed block

\[
N^{\corr}(q_-,q_+,\Delta;s)
\]

contains any extra frozen quadratic correction term with **odd** ordinary background support.

Such a term would look schematically like

\[
\text{odd background scalar}(z)\cdot d_id_j,
\]

or

\[
\text{odd background scalar}(z)\cdot(d_i\eta_j+\eta_id_j),
\]

or

\[
\text{odd background scalar}(z)\cdot\eta_i\eta_j
\]

surviving in the symmetric channels.

If such a term exists, the parity proof fails.

If no such term exists, then the local theorem closes.

The latest summary says the table remains live because the current draft does not explicitly determine the source jets or prove the scalar closure.  The attack here shows a better route: do **not** compute the source jets; prove the even-background support theorem for the corrected Hessian.

---

# 5. Sharpened theorem to insert/prove

The needed theorem is:

```latex
\begin{theorem}[Even-background support of the frozen promoted Hessian]
\label{thm:even-background-support-promoted-hessian}
For the frozen promoted mixed-block Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
every surviving symmetric channel
\[
\chi\in\{dd,\ d\eta+\eta d,\ \eta\eta\}
\]
admits a decomposition
\[
Y^\chi_{g,0}
=
\sum_{p_1+p_2+\ell=g}
Y^\chi_{p_1,p_2,\ell}
\]
in which every nonzero summand has even background order
\[
\ell\equiv0\pmod2.
\]
Equivalently,
\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]
\end{theorem}
```

Then:

```latex
\begin{corollary}[Promoted mixed-block Bottleneck-C scalar closure]
\label{cor:promoted-mixed-block-bc-scalar-closure}
For
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a,\chi,g,r,b}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b},
\]
with
\[
r+b+g=7,
\]
one has
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
Consequently,
\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\qquad
f_{A,Y}=0,
\qquad
\partial_\kappa T=0.
\]
\end{corollary}
```

---

# 6. Remaining adversarial test

To refute this closure, one must now exhibit an odd-background frozen correction term inside

\[
N^{\corr}.
\]

The minimal bad term would be:

\[
Y^{dd}_{p_1,p_2,\ell}
\quad
\text{with}
\quad
\ell\equiv1\pmod2
\]

surviving in

\[
dd,\quad d\eta+\eta d,\quad \eta\eta.
\]

Then one could build the previous obstruction:

\[
E_{A,Y}^{\mathrm{BC}}=S,
\]

and obtain:

\[
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]

So the next concrete audit is narrow:

\[
\boxed{
\text{Inspect }N^{\corr}\text{ for odd-background frozen Hessian terms.}
}
\]

If none exist, the promoted mixed-block local obstruction closes.
## User (2026-04-25 12:05:25)

continue to attack

## Assistant (2026-04-25 12:05:26)

I’ll continue the local attack by auditing the one remaining escape condition: whether the actual corrected mixed block \(N^{\corr}\) contains any frozen odd-background quadratic Hessian terms in the surviving channels.

_Thought for 23s_

## Continued attack — inspect whether odd-background support is actually absent

I attacked the “no odd-background frozen Hessian support” route more adversarially.

Previous possible closure route:

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}
\quad
\Longrightarrow
\quad
E_{A,Y}^{\mathrm{BC}}=0.
\]

This would work because each active row satisfies

\[
r+b+g=7,
\]

so row reflection parity would be

\[
(-1)^r(-1)^b(-1)^g=(-1)^7=-1,
\]

and fixed-sector symmetrization would kill it.

The active coefficient is still the frozen Bottleneck-C carrier, not the internal \([z^7\delta^1]\) source-position coefficient, since the amplitude factor \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge. 

The new result:

\[
\boxed{
\text{The even-background argument is plausible for the pure separation part, but it is not proved for the actual } \eta\text{-dependent Hessian.}
}
\]

More sharply:

\[
\boxed{
\text{the }d\eta+\eta d\text{ and }\eta\eta\text{ channels can contain endpoint-displacement operators that are not pure }z\text{-derivatives.}
}
\]

So the previous parity route is not closed unless the draft proves that all \(\eta\)-directions entering \(Y_{12}^{(2)}\) are parity-compatible in the required sense.

---

# 1. Why the pure kernel argument is insufficient

For the raw midpoint kernel

\[
F(m,z)=\frac{\sin(\Phi(m+z/2)-\Phi(m-z/2))}{\pi z},
\]

we have

\[
F(m,-z)=F(m,z).
\]

So \(F\) is even in \(z\).

That gives a clean parity story for operations built only from:

\[
\partial_z^{2k},
\qquad
\partial_m^j,
\]

because these preserve evenness.

It also handles paired separation derivatives when the total number of \(\partial_z\)-derivatives is even.

But the actual \(\eta\)-directions are endpoint displacement directions, not automatically pure even-preserving operators.

In midpoint/separation coordinates,

\[
x=m+\frac z2,\qquad y=m-\frac z2,
\]

the endpoint derivatives are

\[
\partial_x=\frac12\partial_m+\partial_z,
\]

\[
\partial_y=\frac12\partial_m-\partial_z.
\]

Thus a single endpoint-displacement derivative contains both:

\[
\partial_m
\quad\text{and}\quad
\partial_z.
\]

The \(\partial_z\) part flips \(z\)-parity. The \(\partial_m\) part does not.

Therefore parity depends on whether the corrected Hessian uses the **sum** or **difference** of endpoint-displacement actions.

---

# 2. The decisive distinction: \(\partial_x+\partial_y\) versus \(\partial_x-\partial_y\)

The two natural endpoint combinations are:

\[
\partial_x+\partial_y=\partial_m,
\]

\[
\partial_x-\partial_y=2\partial_z.
\]

If the symmetric \(\eta\)-channel uses the sum, it preserves \(z\)-parity.

If it uses the difference, it flips \(z\)-parity.

For the active row, reflection killing requires:

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]

This is equivalent to saying that the parity of the source grades matches the ordinary order \(g\). That fails exactly when the background operator contributes an odd number of parity-flipping \(\partial_z\)-type actions.

So the real unresolved issue is:

\[
\boxed{
\text{Does the frozen corrected Hessian contain an odd number of separation-derivative operators in a surviving symmetric channel?}
}
\]

If yes, odd-background support exists and \(E_{A,Y}^{\mathrm{BC}}\) can survive.

If no, the parity route closes the carrier.

---

# 3. Channel audit

## 3.1 \(dd\)-channel

The \(dd\)-channel is the cleanest.

If \(d\) is a phase/source variation and not an endpoint displacement, then the \(dd\)-Hessian differentiates twice in the phase/source variable. For the raw phase kernel this gives an even background coefficient.

So the \(dd\)-channel is likely parity-safe **provided** no corrected \(dd\) term inserts an odd endpoint-displacement operator.

This needs an explicit check in \(N^{\corr}\), but the raw kernel part is safe.

Status:

\[
\boxed{
dd\text{ is probably even-background unless corrected source terms add odd endpoint motion.}
}
\]

## 3.2 \(d\eta+\eta d\)-channel

This is the dangerous channel.

One phase/source derivative changes the sine/cosine parity, and one endpoint-displacement derivative may be either \(\partial_m\)-like or \(\partial_z\)-like.

The symmetric channel

\[
d\eta+\eta d
\]

does not automatically mean the endpoint derivative appears as \(\partial_x+\partial_y\). It depends on which source is attached to which endpoint and how \(d_{i,\pm}\), \(\eta_i\) are defined.

If the active symmetric channel contains the \(\partial_x-\partial_y=2\partial_z\) component, then it can produce odd-background support.

A bad term has schematic form:

\[
\text{even/odd source factor}\cdot \partial_z\left(\frac{\cos\Delta_0(z)}{z}\right),
\]

or a related endpoint-difference derivative, with parity not locked to ordinary order \(g\) in the required way.

Status:

\[
\boxed{
d\eta+\eta d\text{ is not parity-safe without an endpoint-sum theorem.}
}
\]

## 3.3 \(\eta\eta\)-channel

The \(\eta\eta\)-channel applies two endpoint-displacement operators. This is safe only if the surviving symmetric combination contains either:

\[
\partial_m^2
\quad\text{or}\quad
\partial_z^2,
\]

both of which preserve evenness.

But a mixed product

\[
\partial_m\partial_z
\]

flips parity and gives odd-background support.

Such a term can arise from

\[
\partial_x^2-\partial_y^2
=
2\partial_m\partial_z.
\]

Therefore \(\eta\eta\) is safe only if the corrected symmetric channel removes the endpoint-antisymmetric square-difference component.

Status:

\[
\boxed{
\eta\eta\text{ is parity-safe only after excluding }\partial_m\partial_z\text{ components.}
}
\]

---

# 4. Formal odd-background survivor in endpoint-operator language

Let the raw frozen background be even:

\[
F(m,z)=F(m,-z).
\]

Suppose a surviving corrected Hessian term contains

\[
\partial_m\partial_zF(m,z).
\]

Then since \(F\) is even,

\[
\partial_zF
\]

is odd, and

\[
\partial_m\partial_zF
\]

is still odd.

Thus this term has odd background support:

\[
\ell\equiv1\pmod2.
\]

Take a summand in \(Y^\chi_{g,0}\) with

\[
g=p_1+p_2+\ell,
\qquad
\ell\equiv1.
\]

Then the endpoint-reflection sign is

\[
(-1)^{p_1+p_2}=(-1)^{g-1},
\]

not

\[
(-1)^g.
\]

The active row sign becomes

\[
(-1)^{r+b}(-1)^{p_1+p_2}
=
(-1)^{7-g}(-1)^{g-1}
=
(+1).
\]

So the row is reflection-even and survives fixed-sector projection.

Taking this survivor to have \(S\)-component gives:

\[
E_{A,Y}^{\mathrm{BC}}=S,
\]

hence

\[
Q_{A,Y}=-u_5,
\qquad
f_{A,Y}=1,
\qquad
\partial_\kappa T=-a_1^2/c.
\]

This is a formal local countermodel to scalar closure unless the draft excludes \(\partial_m\partial_z\)-type frozen Hessian terms.

---

# 5. What exact theorem would close this route?

The previous “even-background support” theorem should be refined. The useful theorem is not just “the kernel is even”; it must constrain the endpoint-displacement content of \(N^{\corr}\).

The sharper theorem is:

```latex
\begin{theorem}[Endpoint-even support of the frozen quadratic Hessian]
For the promoted frozen Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
every surviving symmetric channel
\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta
\]
contains only endpoint-displacement operators with an even number of
separation derivatives \(\partial_z\). Equivalently, after writing
\[
Y^\chi_{g,0}
=
\sum_{p_1+p_2+\ell=g}Y^\chi_{p_1,p_2,\ell},
\]
all nonzero frozen summands have
\[
\ell\equiv0\pmod2.
\]
Consequently,
\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]
\end{theorem}
```

Then the promoted scalar closure follows:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

---

# 6. What theorem would refute it?

A single allowed term of the following type refutes the parity route:

\[
Y^\chi_{\mathrm{bad}}
=
C(m,z)\,\partial_m\partial_zF(m,z)
\]

or any equivalent odd-separation-derivative term surviving in:

\[
d\eta+\eta d
\quad\text{or}\quad
\eta\eta.
\]

The theorem-ready obstruction is:

```latex
\begin{lemma}[Odd-background survivor obstruction]
Suppose the frozen promoted Hessian has a surviving fixed-sector summand
\[
Y^\chi_{p_1,p_2,\ell}
\]
in one of
\[
\chi\in\{d\eta+\eta d,\eta\eta\}
\]
with
\[
\ell\equiv1\pmod2
\]
and nonzero \(S\)-projection after contraction with some
\[
\Lambda^-_{a,r}W_{+,b},
\qquad r+b+p_1+p_2+\ell=7.
\]
Then
\[
E_{A,Y}^{\mathrm{BC}}
\]
is not forced to vanish. In particular, a formal good-patch model gives
\[
f_{A,Y}\ne0
\]
and hence
\[
\partial_\kappa T\ne0.
\]
\end{lemma}
```

---

# 7. Current result of the attack

The parity route is **not yet closed**.

What is established:

\[
\boxed{
\text{The pure midpoint phase-kernel }F(m,z)\text{ is even in }z.
}
\]

What remains unproved:

\[
\boxed{
\text{the actual corrected Hessian uses only even-separation endpoint operators in the surviving channels.}
}
\]

The dangerous terms are not in the \(dd\)-phase Hessian itself; they are in the endpoint-displacement channels:

\[
\boxed{
d\eta+\eta d,
\qquad
\eta\eta.
}
\]

The next concrete attack should inspect \(N^{\corr}\) and determine whether its \(\eta\)-terms contain endpoint-difference operators:

\[
\partial_x-\partial_y
\]

or mixed operators:

\[
\partial_m\partial_z.
\]

If such terms exist and survive \(\pi_{\mathfrak f}\), the promoted mixed-block scalar closure is false under current assumptions.

If they are absent, the even-background theorem closes \(E_{A,Y}^{\mathrm{BC}}\).
## User (2026-04-25 12:06:39)

continue to attack

## Assistant (2026-04-25 12:07:11)

_Thought for 29s_

## Continued local attack — split \(\eta\) into midpoint and separation components

I pushed the endpoint-operator issue one step further. The previous attack showed that \(E_{A,Y}^{\mathrm{BC}}\) closes if the frozen quadratic Hessian has no odd-background support. The remaining danger is now entirely localized in how the \(\eta\)-directions enter the corrected mixed block.

The active coefficient remains:

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

The source-position \([z^7\delta^1]\) table is not the first Bottleneck-C carrier; the amplitude \(a_1a_2(a_1+a_2)\) already supplies the first \(\delta\)-edge.  The row set and decisive scalars are also now fixed: the skew \(d\eta-\eta d\) row is removed, while \(dd\), \(d\eta+\eta d\), and \(\eta\eta\) survive, with closure requiring both \(Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=0\) and \(f_{A,Y}=0\). 

---

# 1. Split the endpoint displacement

In midpoint/separation coordinates,

\[
x=m+\frac z2,\qquad y=m-\frac z2,
\]

endpoint displacement decomposes into midpoint and separation pieces:

\[
\eta^\Sigma:=\frac{\eta_++\eta_-}{2},
\qquad
\eta^\Delta:=\frac{\eta_+-\eta_-}{2}.
\]

Equivalently, the differential operators split as:

\[
\eta_+\partial_x+\eta_-\partial_y
=
\eta^\Sigma\partial_m
+
2\eta^\Delta\partial_z.
\]

Thus:

- \(\eta^\Sigma\) is midpoint-displacement type;
- \(\eta^\Delta\) is separation-displacement type.

Since \(\partial_z\) flips \(z\)-parity and \(\partial_m\) preserves it, the parity of the frozen Hessian depends on whether the surviving \(\eta\)-channels contain \(\eta^\Delta\).

---

# 2. The corrected parity criterion

The promoted row is killed if the total reflection parity is odd:

\[
(-1)^{r+b}\cdot \operatorname{parity}(Y^\chi_{g,0})=-1.
\]

Since

\[
r+b=7-g,
\]

this is equivalent to:

\[
\operatorname{parity}(Y^\chi_{g,0})=(-1)^g.
\]

Now decompose a frozen Hessian summand as:

\[
Y^\chi_{g,0}
=
Y^\chi_{p_1,p_2,\ell},
\qquad
g=p_1+p_2+\ell,
\]

where \(p_1,p_2\) are source-reflection grades and \(\ell\) is background operator order. Endpoint reflection sees:

\[
(-1)^{p_1+p_2}.
\]

So the desired parity holds iff

\[
\ell\equiv 0\pmod 2.
\]

The new point is that \(\ell\) can be read as the number of parity-flipping separation derivatives modulo two. Thus:

\[
\boxed{
\text{closure requires every surviving frozen Hessian summand to contain an even number of }\partial_z\text{-type operators.}
}
\]

---

# 3. Channel audit after \(\eta^\Sigma/\eta^\Delta\) splitting

## 3.1 \(dd\)

The \(dd\)-channel does not contain endpoint displacement. For the raw phase-kernel Hessian, its background parity is even.

So \(dd\) is safe unless \(N^{\corr}\) adds an endpoint-motion correction to the \(dd\)-Hessian itself.

Current status:

\[
\boxed{
dd\text{ is parity-safe modulo exotic corrected }dd\text{-motion terms.}
}
\]

## 3.2 \(d\eta+\eta d\)

Split:

\[
d\eta+\eta d
=
d\eta^\Sigma+\eta^\Sigma d
+
d\eta^\Delta+\eta^\Delta d.
\]

The \(\eta^\Sigma\)-part uses \(\partial_m\), which does not flip separation parity. The \(\eta^\Delta\)-part uses \(\partial_z\), which flips separation parity.

Therefore:

\[
\boxed{
d\eta^\Sigma+\eta^\Sigma d
\text{ is parity-safe;}
}
\]

\[
\boxed{
d\eta^\Delta+\eta^\Delta d
\text{ is parity-dangerous.}
}
\]

Thus the active \(d\eta+\eta d\) row closes only if the corrected source model proves:

\[
\boxed{
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}=0
}
\]

after \(\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}\), or at least proves it lies in both the quotient-safe and \(\Phi_K\)-safe kernels.

## 3.3 \(\eta\eta\)

Split:

\[
\eta\eta
=
\eta^\Sigma\eta^\Sigma
+
2\eta^\Sigma\eta^\Delta
+
\eta^\Delta\eta^\Delta.
\]

The parity behavior is:

\[
\eta^\Sigma\eta^\Sigma:\quad \partial_m^2
\quad\text{safe},
\]

\[
\eta^\Delta\eta^\Delta:\quad \partial_z^2
\quad\text{safe},
\]

\[
\eta^\Sigma\eta^\Delta:\quad \partial_m\partial_z
\quad\text{dangerous}.
\]

So:

\[
\boxed{
\eta\eta\text{ closes by parity iff the mixed }\eta^\Sigma\eta^\Delta\text{ component is absent or killed.}
}
\]

---

# 4. The local obstruction is now much narrower

The full \(E_{A,Y}^{\mathrm{BC}}\) obstruction reduces to two possible parity-bad subchannels:

\[
\boxed{
d\eta^\Delta+\eta^\Delta d
}
\]

and

\[
\boxed{
\eta^\Sigma\eta^\Delta.
}
\]

If both are absent/killed, then every surviving Hessian channel has even background support and:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

If either survives with nonzero fixed-sector \(S\)-projection, then \(T\)-horizontal closure fails.

---

# 5. Formal countermodel using only the dangerous subchannel

Take the \(d\eta^\Delta+\eta^\Delta d\) channel. Let the dangerous frozen Hessian piece be:

\[
Y_{\mathrm{bad}}^{d\eta}
=
S,
\]

arising from a single separation derivative \(\partial_z\), so it has odd background support.

Set:

\[
W_{+,0}=I,
\qquad
\Lambda^-_{1,0}=I,
\]

and all other rows zero.

Then:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}(S)
=
S.
\]

Therefore:

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

So:

\[
Q_{A,Y}=-u_5,
\]

and

\[
\partial_\kappa T=-a_1^2/c.
\]

This model respects the active bookkeeping:

- frozen coefficient;
- surviving symmetric channel;
- no \(d\eta-\eta d\) skew row;
- one same-point whitening slot;
- fixed-sector symmetrization.

It violates only the unproved claim that separation-displacement \(\eta^\Delta\) pieces are absent or killed.

---

# 6. What the next theorem must actually say

The previous “even-background support” theorem should be replaced by the more precise endpoint-displacement theorem:

```latex
\begin{theorem}[No odd endpoint-displacement support in the promoted Hessian]
\label{thm:no-odd-endpoint-displacement-support-promoted-hessian}
For the frozen promoted Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
write the endpoint displacement source as
\[
\eta=\eta^\Sigma+\eta^\Delta,
\]
where \(\eta^\Sigma\) acts by \(\partial_m\) and \(\eta^\Delta\) acts by
\(\partial_z\). Then the fixed-sector projection of the parity-bad
subchannels vanishes:
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}
W_{+,b}
\right)=0,
\]
and
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
Y^{\eta^\Sigma\eta^\Delta}_{g,0}
W_{+,b}
\right)=0
\]
for all active
\[
a\in\{1,5\},\qquad 4\le g\le7,\qquad r+b=7-g.
\]
\end{theorem}
```

Then the remaining safe channels are:

\[
dd,
\qquad
d\eta^\Sigma+\eta^\Sigma d,
\qquad
\eta^\Sigma\eta^\Sigma,
\qquad
\eta^\Delta\eta^\Delta,
\]

all of which have even background support and therefore are killed by the total odd row parity:

\[
r+b+g=7.
\]

---

# 7. Result of this attack

The local obstruction has been reduced again.

It is no longer the whole 60-row table. It is specifically:

\[
\boxed{
\text{Does }N^{\corr}\text{ contain fixed-sector surviving }\eta^\Delta\text{ terms with odd }\partial_z\text{-count?}
}
\]

Equivalently, the only live parity-bad subchannels are:

\[
\boxed{
d\eta^\Delta+\eta^\Delta d
}
\]

and

\[
\boxed{
\eta^\Sigma\eta^\Delta.
}
\]

If the draft proves these vanish after fixed-sector symmetrization, then:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

If not, a formal good-patch model produces:

\[
\boxed{
f_{A,Y}\ne0
}
\]

and hence:

\[
\boxed{
\partial_\kappa T\ne0.
}
\]

So the next concrete audit should inspect the actual definitions of \(\eta_i(z)\) and \(N^{\corr}\) to determine whether \(\eta^\Delta\) appears in the surviving symmetric Hessian channels.
## User (2026-04-25 12:08:47)

continue to attack

## Assistant (2026-04-25 12:08:52)

I’ll now attack the remaining \(\eta^\Delta\) danger directly: whether it is actually part of the surviving symmetric channel, or whether endpoint symmetrization pushes it into the already-killed skew channel.

_Thought for 39s_

## Continued local attack — does \(\eta^\Delta\) vanish at the frozen collision face?

The previous attack reduced the parity-bad part of

\[
E_{A,Y}^{\mathrm{BC}}
\]

to the separation-displacement pieces

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta,
\]

where

\[
\eta^\Sigma=\frac{\eta_++\eta_-}{2},
\qquad
\eta^\Delta=\frac{\eta_+-\eta_-}{2}.
\]

I now attacked whether these terms are even present in the **frozen** coefficient. The key observation is this:

\[
\boxed{
\eta^\Delta\text{ should vanish at the frozen collision face if }\eta_+,\eta_-
\text{ are the same source-motion field evaluated at }h\pm\delta/2.
}
\]

If true, the parity-bad terms are not part of

\[
E_{A,Y}^{\mathrm{BC}},
\]

but belong to the later internal source-position edge layer. That would close the promoted carrier without needing the full 60-row table.

---

# 1. The frozen coefficient uses \(\delta^0\)

The corrected Bottleneck-C carrier is

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7]\,
D(G_-^{-1/2})[A_-]\,
Y_{12}^{(2)}\,
R_0.
\]

Equivalently,

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi}
\sum_{g=4}^{7}
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

The subscript \(0\) in

\[
Y^\chi_{g,0}
\]

is important: it is the **frozen internal source-position coefficient**. It is not the internal \(\delta^1\) source-motion coefficient.

The active local object is frozen because the external amplitude factor

\[
a_1a_2(a_1+a_2)
\]

already supplies the first collision-chart edge:

\[
a_1a_2(a_1+a_2)=a_1^3\kappa\delta+O(\delta^2).
\]

So any term internally proportional to \(\delta\) is one order later for this first Bottleneck-C carrier.

---

# 2. Expansion of \(\eta^\Delta\)

Suppose the endpoint displacement source is generated by a single analytic source-motion field \(\eta(t)\), evaluated at the two nearby endpoints:

\[
\eta_+=\eta\!\left(h+\frac{\delta}{2}\right),
\qquad
\eta_-=\eta\!\left(h-\frac{\delta}{2}\right).
\]

Then

\[
\eta^\Sigma
=
\frac{\eta_++\eta_-}{2}
=
\eta(h)
+\frac{\delta^2}{8}\eta''(h)
+O(\delta^4),
\]

while

\[
\eta^\Delta
=
\frac{\eta_+-\eta_-}{2}
=
\frac{\delta}{2}\eta'(h)
+\frac{\delta^3}{48}\eta'''(h)
+O(\delta^5).
\]

Therefore

\[
\boxed{
[\delta^0]\eta^\Delta=0.
}
\]

So every term containing a factor of \(\eta^\Delta\) vanishes in the frozen coefficient.

This kills exactly the parity-bad subchannels:

\[
[\delta^0](d\eta^\Delta+\eta^\Delta d)=0,
\]

and

\[
[\delta^0](\eta^\Sigma\eta^\Delta)=0.
\]

---

# 3. Consequence for the surviving frozen channels

At the frozen face, the only surviving \(\eta\)-pieces are:

\[
\eta^\Sigma,
\qquad
\eta^\Sigma\eta^\Sigma,
\]

and possibly

\[
\eta^\Delta\eta^\Delta
\]

only at order \(\delta^2\), not at \(\delta^0\).

Thus in the frozen coefficient \(Y^\chi_{g,0}\), the dangerous terms are absent:

\[
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}=0,
\]

\[
Y^{\eta^\Sigma\eta^\Delta}_{g,0}=0,
\]

\[
Y^{\eta^\Delta\eta^\Delta}_{g,0}=0.
\]

The remaining frozen channels are:

\[
dd,
\qquad
d\eta^\Sigma+\eta^\Sigma d,
\qquad
\eta^\Sigma\eta^\Sigma.
\]

These use only midpoint-displacement operators:

\[
\partial_m
\]

and phase/source Hessian operations. They contain no odd number of separation derivatives \(\partial_z\). Therefore their background support is even, giving

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]

Then every active row satisfies

\[
\mathscr R
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right)
=
(-1)^{r+b+g}
\left(
\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right).
\]

Since

\[
r+b+g=7,
\]

each row is reflection-odd:

\[
(-1)^{r+b+g}=-1.
\]

Hence fixed-sector symmetrization kills every row:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

---

# 4. The precise condition needed

The whole argument rests on one source-realization condition:

\[
\boxed{
\eta_+,\eta_-\text{ must be evaluations of the same analytic endpoint-motion field at }h\pm\delta/2.
}
\]

Equivalently:

\[
\eta^\Delta=O(\delta).
\]

If this is part of the paper’s actual source model, then the promoted mixed-block carrier closes.

If instead \(\eta_+\) and \(\eta_-\) are allowed as independent endpoint source variables at the frozen face, then

\[
[\delta^0]\eta^\Delta
\]

can be nonzero, and the dangerous parity-bad channels remain live.

---

# 5. Formal theorem that would close the carrier

The right theorem is now even narrower than the previous “even-background support” theorem.

```latex
\begin{lemma}[Frozen separation-displacement vanishing]
\label{lem:frozen-separation-displacement-vanishing}
In the actual two-atom source model, the endpoint-displacement source
\(\eta\) is generated by a single analytic source-motion field evaluated at
the two endpoints:
\[
\eta_+=\eta(h+\delta/2),
\qquad
\eta_-=\eta(h-\delta/2).
\]
Consequently
\[
\eta^\Delta:=\frac{\eta_+-\eta_-}{2}=O(\delta),
\]
and therefore
\[
[\delta^0]\eta^\Delta=0.
\]
\end{lemma}
```

Then:

```latex
\begin{corollary}[Promoted mixed-block Bottleneck-C carrier vanishes]
\label{cor:promoted-mixed-block-bc-carrier-vanishes}
For the frozen Bottleneck-C coefficient
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{a,\chi,g,r,b}
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b},
\]
one has
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
Hence
\[
Q_{A,Y}=0,
\qquad
f_{A,Y}=0,
\qquad
\partial_\kappa T=0.
\]
\end{corollary}
```

---

# 6. Formal countermodel if the condition fails

If \(\eta_+\) and \(\eta_-\) are independent frozen endpoint variables, choose

\[
\eta_+=1,
\qquad
\eta_-=-1.
\]

Then

\[
\eta^\Delta=1,
\qquad
\eta^\Sigma=0
\]

at \(\delta=0\).

A dangerous frozen subchannel

\[
d\eta^\Delta+\eta^\Delta d
\]

can survive. Choosing the corresponding fixed-sector component to be

\[
S
\]

gives:

\[
E_{A,Y}^{\mathrm{BC}}=S.
\]

Then:

\[
Q_{A,Y}=-u_5,
\]

\[
f_{A,Y}=1,
\]

and

\[
\partial_\kappa T=-a_1^2/c.
\]

So if the source model permits independent frozen endpoint displacements, the promoted carrier is not structurally killed.

---

# 7. Current status

The local obstruction has been reduced to a highly specific source-realization question:

\[
\boxed{
\text{Is }\eta^\Delta=O(\delta)\text{ in the actual two-atom source model?}
}
\]

If yes:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

If no:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}\text{ can carry a quotient- and }T\text{-visible obstruction.}
}
\]

This is the most economical local theorem to attack next. It avoids the 60-row table entirely and targets the only parity-bad subchannels.
## User (2026-04-25 12:11:24)

continue to attack

## Assistant (2026-04-25 12:11:28)

I’ll now attack the remaining source-realization question directly: whether the actual two-atom source model forces \(\eta^\Delta=O(\delta)\), or whether \(\eta_+\) and \(\eta_-\) can be independent at the frozen face.

_Thought for 29s_

## Continued local attack — the \(\eta^\Delta=O(\delta)\) route is not currently justified

I attacked the remaining source-realization question:

\[
\boxed{
\eta^\Delta=O(\delta)?
}
\]

If this were true for the actual source model, then the parity-bad subchannels

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]

would vanish in the frozen coefficient, and the promoted carrier would close:

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

But after checking the current setup, this route is **not justified from the stated definitions/status**. The current materials still treat \(d_{i,\pm}(z)\), \(\eta_i(z)\), and the finite source jets as objects to be derived or supplied; the actual source construction tying the two endpoint \(\eta\)-components together is not presently given. turn56file13

So the strongest honest result is:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0
\text{ follows if the source model is endpoint-diagonal/co-moving,}
}
\]

but

\[
\boxed{
\text{it can fail if the frozen endpoint displacement has an independent separation component.}
}
\]

---

# 1. The exact distinction

For a source direction \(\xi_i\), write its endpoint displacement components as

\[
\eta_{i,+},\qquad \eta_{i,-}.
\]

Define

\[
\eta_i^\Sigma:=\frac{\eta_{i,+}+\eta_{i,-}}2,
\qquad
\eta_i^\Delta:=\frac{\eta_{i,+}-\eta_{i,-}}2.
\]

The closure argument needs:

\[
[\delta^0]\eta_i^\Delta=0
\qquad
\text{for every active source direction }i.
\]

Equivalently,

\[
\eta_{i,+}-\eta_{i,-}=O(\delta).
\]

This is true if \(\eta_{i,+}\) and \(\eta_{i,-}\) are evaluations of the **same analytic endpoint-motion field** at

\[
h+\delta/2,\qquad h-\delta/2.
\]

Then

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2),
\]

so

\[
\eta_i^\Delta
=
\frac{\delta}{2}\eta_i'(h)+O(\delta^3).
\]

But this is a substantive source-realization theorem. It is not a formal consequence of endpoint-swap symmetry alone.

---

# 2. Why endpoint-swap symmetry is insufficient

Endpoint swap gives a relation of the form

\[
N^{\corr}(h_-,h_+)^T=N^{\corr}(h_+,h_-),
\]

and this already closed the \(M_A,M_C\) branch after source-grade reflection. 

But endpoint-swap symmetry only controls how the two endpoints transform under swapping. It does not say that the two endpoint displacement components of a source direction are equal at \(\delta=0\).

Formally, both of the following are swap-compatible:

### Diagonal/co-moving source

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2),
\]

so

\[
\eta_i^\Delta=O(\delta).
\]

### Independent endpoint tangent source

\[
\eta_{i,+}=u_i,
\qquad
\eta_{i,-}=v_i,
\]

with

\[
u_i,v_i
\]

independent frozen tangent data. Then

\[
\eta_i^\Delta=\frac{u_i-v_i}{2}
\]

can be nonzero at \(\delta=0\).

Both models can respect endpoint-transpose functoriality. Only the first kills the parity-bad frozen channels.

---

# 3. Consequence for the active coefficient

The active local object is the frozen coefficient

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

This is explicitly the first Bottleneck-C carrier because the amplitude factor

\[
a_1a_2(a_1+a_2)
\]

already supplies the first \(\delta\)-edge; the internal \([z^7\delta^1]\) table is a later source-motion layer. 

If

\[
[\delta^0]\eta^\Delta=0,
\]

then the frozen \(d\eta^\Delta+\eta^\Delta d\) and \(\eta^\Sigma\eta^\Delta\) pieces vanish, leaving only even-background pieces. Then each active row has odd total reflection parity because

\[
r+b+g=7,
\]

so

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

If

\[
[\delta^0]\eta^\Delta\ne0,
\]

then a parity-bad frozen channel can survive. The current setup keeps the symmetric \(d\eta+\eta d\) and \(\eta\eta\) rows active; only the skew \(d\eta-\eta d\) row is removed. 

---

# 4. Formal obstruction if endpoint displacements are independent

Assume frozen endpoint tangent data with

\[
\eta^\Delta\ne0.
\]

Take one active row:

\[
a=1,\qquad g=7,\qquad r=0,\qquad b=0,
\]

and choose the parity-bad symmetric channel

\[
d\eta^\Delta+\eta^\Delta d.
\]

Set

\[
W_{+,0}=I,
\qquad
\Lambda^-_{1,0}=I,
\qquad
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}=S.
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}(S)
=
S.
\]

So

\[
E_{A,Y}^{\mathrm{BC}}=0\cdot I+1\cdot S.
\]

Therefore

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=-u_5,
\]

and

\[
f_{A,Y}=1.
\]

The induced hidden-state slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
-\frac{a_1^2}{c}.
\]

Thus the carrier is both quotient-visible on a generic \(u_5\ne0\) patch and \(T\)-visible always when \(c\ne0\). The current local tests are exactly these two scalars \(Q_{A,Y}\) and \(f_{A,Y}\). 

---

# 5. What theorem is actually needed

The previous theorem

\[
\eta^\Delta=O(\delta)
\]

should be stated as a source-realization theorem, not as a parity corollary.

```latex
\begin{theorem}[Endpoint-diagonal realization of displacement sources]
\label{thm:endpoint-diagonal-realization-displacement-sources}
For every active source direction \(\xi_i\) entering the promoted quadratic
mixed-block Hessian \(Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]\), the endpoint
displacement components are generated by a single analytic source-motion
field \(\eta_i(t)\):
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Consequently
\[
\eta_i^\Delta
:=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta),
\]
and therefore
\[
[\delta^0]\eta_i^\Delta=0.
\]
\end{theorem}
```

Then the local closure theorem follows:

```latex
\begin{corollary}[Promoted mixed-block Bottleneck-C scalar closure]
\label{cor:promoted-mixed-block-bc-scalar-closure-from-endpoint-diagonal}
Assume Theorem~\ref{thm:endpoint-diagonal-realization-displacement-sources}.
Then the frozen Bottleneck-C carrier satisfies
\[
E_{A,Y}^{\mathrm{BC}}=0.
\]
Hence
\[
Q_{A,Y}=0,
\qquad
f_{A,Y}=0,
\qquad
\partial_\kappa T=0.
\]
\end{corollary}
```

---

# 6. If that theorem is false

If the actual source model permits independent frozen endpoint displacement data, then the correct obstruction theorem is:

```latex
\begin{lemma}[Separation-displacement obstruction]
\label{lem:separation-displacement-obstruction}
Suppose there exists an active source direction \(\xi_i\) with
\[
[\delta^0]\eta_i^\Delta\ne0.
\]
If the corresponding parity-bad frozen Hessian component in either
\[
d\eta^\Delta+\eta^\Delta d
\qquad\text{or}\qquad
\eta^\Sigma\eta^\Delta
\]
has nonzero fixed-sector \(S\)-projection after contraction with some
\[
\Lambda^-_{a,r}W_{+,b},
\qquad
r+b+g=7,
\]
then
\[
f_{A,Y}\ne0
\]
is formally allowed, and the augmented \(T\)-horizontal Bottleneck-C condition
\[
\partial_\kappa T=0
\]
is not forced.
\end{lemma}
```

---

# 7. Current state after this attack

The local obstruction is now reduced to a binary source-model question:

\[
\boxed{
\text{Are endpoint displacement sources diagonal/co-moving at the frozen face?}
}
\]

If yes:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}=0.
}
\]

If no:

\[
\boxed{
E_{A,Y}^{\mathrm{BC}}
\text{ can survive through a separation-displacement channel.}
}
\]

The current supplied draft context does not establish the endpoint-diagonal realization theorem. The materials still instruct agents to search for definitions of

\[
d_{i,\pm}(z),\qquad \eta_i(z),
\]

or the source jets from which they are built, which means this source-realization input is not yet locked down in the current proof state. 
## User (2026-04-25 12:30:23)

You are now "Local Agent 2". continue on your attack as per the attached instructions

## Assistant (2026-04-25 12:31:41)

_Thought for 1m 13s_

## Local Agent 2 — direct Hessian parity / odd-background audit

I attacked the promoted Hessian directly, using the actual corrected mixed block shape. The result is negative for the parity-closure route:

\[
\boxed{
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}
\text{ is not forced.}
}
\]

More sharply:

\[
\boxed{
\text{The actual }N^{\corr}(q_-,q_+,\Delta;s)\text{ contains an odd-background frozen }\eta\eta\text{ Hessian term.}
}
\]

So the route

\[
\text{“all frozen Hessian background orders are even”}
\quad\Longrightarrow\quad
E_{A,Y}^{\mathrm{BC}}=0
\]

fails unless a further cancellation theorem kills this specific \(\eta\eta\) term after whitening and fixed-sector projection.

The active object is the frozen Bottleneck-C coefficient, not the internal \([z^7\delta^1]\) source-position coefficient; this is because \(a_1a_2(a_1+a_2)\) already contributes the first collision-chart \(\delta\)-edge. The local target is exactly to determine whether the frozen Hessian carrier has quotient-visible or \(T\)-visible fixed-sector content. turn60file0

---

# 1. Actual corrected mixed block and variables

The corrected mixed block has the form

\[
N^{\corr}_m(s)=\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta}{s}
&
\dfrac{\sin\Delta+q(t_+)s\cos\Delta}{s^2}
\\[2ex]
-\dfrac{\sin\Delta+q(t_-)s\cos\Delta}{s^2}
&
\dfrac{(q(t_-)+q(t_+))s\cos\Delta+(2-q(t_-)q(t_+)s^2)\sin\Delta}{2s^3}
\end{pmatrix}.
\]

Write

\[
q_\pm=q_{0,\pm}+d_\pm,
\qquad
\Delta=\Delta_0+\eta.
\]

Important point: in this actual formula, \(\eta\) is a **single scalar phase increment** in \(\Delta\). It is not naturally an endpoint pair \((\eta_+,\eta_-)\). Thus the previous \(\eta^\Sigma/\eta^\Delta\) endpoint-displacement split is not the right primitive for this corrected mixed block unless the paper separately defines endpoint displacement variables and proves they feed into this scalar \(\eta\) in a diagonal way.

The prompt itself asks Local Agent 2 to inspect \(N^{\corr}(q_-,q_+,\Delta;s)\) and decompose the frozen Hessian into \(dd,d\eta+\eta d,\eta\eta\) channels. 

---

# 2. Hessian channel calculation

Let

\[
N^{\corr}=N(q_-,q_+,\Delta;s).
\]

The quadratic Hessian

\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2]
\]

has three relevant source channels:

\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta.
\]

The dangerous question is whether each frozen summand

\[
Y^\chi_{p_1,p_2,\ell}
\]

has even background order

\[
\ell\equiv0\pmod2.
\]

If all \(\ell\) are even, then

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0},
\]

and the active rows vanish because

\[
r+b+g=7.
\]

But the actual \(\eta\eta\) channel violates this.

---

# 3. \(\eta\eta\) channel: explicit odd-background term

Consider the \((1,2)\)-entry:

\[
N_{12}
=
\frac{\sin\Delta+q_+s\cos\Delta}{s^2}.
\]

Differentiate twice in \(\Delta\). Since \(\eta\) enters by \(\Delta=\Delta_0+\eta\), this is the \(\eta\eta\) Hessian background coefficient:

\[
\partial_\Delta^2 N_{12}\big|_0
=
\frac{-\sin\Delta_0-q_{0,+}s\cos\Delta_0}{s^2}.
\]

Thus

\[
\partial_\Delta^2 N_{12}\big|_0
=
-\frac{\sin\Delta_0}{s^2}
-
\frac{q_{0,+}\cos\Delta_0}{s}.
\]

Now use midpoint parity:

\[
\Delta_0(-s)=-\Delta_0(s).
\]

Therefore

\[
\sin\Delta_0(s)
\]

is odd, and

\[
\cos\Delta_0(s)
\]

is even.

The first term

\[
-\frac{\sin\Delta_0}{s^2}
\]

is odd because \(s^2\) is even.

The second term

\[
-\frac{q_{0,+}\cos\Delta_0}{s}
\]

contains both even and odd parts through

\[
q_{0,+}=q_0(m+s/2).
\]

Its parity is not purely even. In particular, since \(1/s\) is odd and \(\cos\Delta_0\) is even, the even part of \(q_{0,+}\) produces an odd-background contribution.

So the \((1,2)\) \(\eta\eta\)-Hessian contains frozen odd-background support.

Similarly, the \((2,1)\)-entry is

\[
N_{21}
=
-\frac{\sin\Delta+q_-s\cos\Delta}{s^2},
\]

so

\[
\partial_\Delta^2 N_{21}\big|_0
=
\frac{\sin\Delta_0+q_{0,-}s\cos\Delta_0}{s^2}
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_{0,-}\cos\Delta_0}{s}.
\]

This is the transpose partner. It does not vanish automatically; it is paired by symmetrization.

---

# 4. Why this is an odd-background survivor

The affine removal in the paper gives, for one-pair source perturbations,

\[
\eta(z)=\frac{z^3}{Q^6}V(z).
\]

Thus an \(\eta\)-source direction begins at source-reflection grade \(3\). For an \(\eta\eta\) Hessian term, the two source grades contribute

\[
p_1+p_2=6.
\]

Now the odd background term above has background order

\[
\ell\equiv1\pmod2.
\]

For the active top ordinary order,

\[
g=p_1+p_2+\ell=6+1=7.
\]

This is exactly the top row:

\[
g=7,\qquad r=0,\qquad b=0.
\]

The reflection sign of the source directions is

\[
(-1)^{p_1+p_2}=(-1)^6=+1.
\]

Because

\[
r+b=0,
\]

the full row is reflection-even, not reflection-odd. Therefore fixed-sector symmetrization does **not** kill it.

This directly refutes the proposed universal parity law

\[
\mathscr R(Y^\chi_{g,0})=(-1)^gY^\chi_{g,0}.
\]

For this summand,

\[
(-1)^g=(-1)^7=-1,
\]

but the source-reflection sign is \(+1\).

---

# 5. Minimal surviving term

A minimal odd-background frozen Hessian survivor is:

\[
Y^{\eta\eta}_{7,0}
\supset
-\frac{\sin\Delta_0}{s^2}\,\eta_i\eta_j
\]

in the \((1,2)\)-entry, together with its transpose partner in the \((2,1)\)-entry.

More invariantly, the survivor is the odd part of

\[
\partial_\Delta^2
\left(
\frac{\sin\Delta+q_+s\cos\Delta}{s^2}
\right)_{\Delta=\Delta_0}
\eta_i\eta_j
\]

and the corresponding \((2,1)\) partner.

This term is in the active surviving channel:

\[
\eta\eta.
\]

It is not the killed skew row

\[
d\eta-\eta d.
\]

It does not require \(\eta^\Delta\ne0\). It uses the scalar phase increment \(\eta\) itself. Therefore it is an odd-background survivor **independent of the endpoint-diagonal question**.

This is important coordination-wise: even if Local Agent 1 proves

\[
[\delta^0]\eta^\Delta=0,
\]

that only removes endpoint-separation displacement pieces. It does not remove the scalar phase-increment \(\eta\eta\) term in \(N^{\corr}(q_-,q_+,\Delta;s)\).

---

# 6. Can this survivor contribute to \(f_{A,Y}\) or \(Q_{A,Y}\)?

Formally, yes.

Take the active row:

\[
g=7,\qquad r=0,\qquad b=0.
\]

Let

\[
\Lambda^-_{a,0}=I,
\qquad
W_{+,0}=I,
\]

and assume the fixed-sector projection of the symmetrized \(\eta\eta\) survivor has an \(S\)-component:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
(Y^{\eta\eta}_{7,0})
=
S.
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}=S.
\]

So

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

Therefore

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
=
-u_5,
\]

and

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
-\frac{a_1^2}{c}.
\]

Thus this survivor can be both quotient-visible and \(T\)-visible unless the paper supplies a separate theorem that its fixed-sector \(S\)-projection vanishes or is exactly cancelled by another top-row term.

The active local target requires precisely \(Q_{A,Y}=0\) and \(f_{A,Y}=0\). turn60file10

---

# 7. Does another \(\eta\eta\) term cancel it?

There are potential same-channel companions:

\[
-\frac{q_{0,+}\cos\Delta_0}{s}
\quad\text{and}\quad
\frac{q_{0,-}\cos\Delta_0}{s}.
\]

Their sum/difference under transpose symmetrization depends on the exact fixed-sector projection and the relation between \(q_{0,+}\) and \(q_{0,-}\). But no abstract parity forces cancellation of the \(-\sin\Delta_0/s^2\) component.

At best, one could prove a special identity in the full matrix block:

\[
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left[
\partial_\Delta^2N_0\big|_{\eta\eta,\text{odd}}
\right]
=0.
\]

That is a new theorem. It does not follow from the broad parity mechanism.

---

# 8. Verdict

Local Agent 2 refutes the clean parity closure route.

\[
\boxed{
\text{The frozen Hessian has an odd-background survivor in the }\eta\eta\text{ channel.}
}
\]

The minimal survivor is the \((1,2)/(2,1)\) off-diagonal \(\eta\eta\) Hessian term

\[
-\frac{\sin\Delta_0}{s^2}\eta_i\eta_j
\]

and its transpose partner.

This survivor is independent of the endpoint-diagonal question

\[
[\delta^0]\eta^\Delta=0.
\]

Therefore:

\[
\boxed{
\text{Even if Local Agent 1 proves endpoint-diagonal realization, }E_{A,Y}^{\mathrm{BC}}\text{ is not closed.}
}
\]

The next theorem would need to be a more specific fixed-sector cancellation:

```latex
\begin{lemma}[Off-diagonal \(\eta\eta\) odd-background cancellation]
For the corrected mixed block \(N^{\corr}(q_-,q_+,\Delta;s)\), the odd-background part of
\[
\partial_\Delta^2N_0
\]
in the frozen \(\eta\eta\) channel satisfies
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
W_{+,b}
\right)=0
\]
for every active row \(r+b+g=7\).
\]
\end{lemma}
```

Without this new cancellation, the promoted mixed-block Bottleneck-C carrier remains live.
## User (2026-04-25 12:36:22)

You are also called "Local B". do the attack per these instructions

## Assistant (2026-04-25 12:36:55)

_Thought for 31s_

## Local B — endpoint-diagonal source realization attack

Target:

\[
[\delta^0]\eta_i^\Delta=0,
\qquad
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2.
\]

Verdict:

\[
\boxed{
\text{Endpoint-diagonal realization is not proved by the current source definitions.}
}
\]

More precisely:

\[
\boxed{
[\delta^0]\eta_i^\Delta=0
\text{ follows if } \eta_{i,+},\eta_{i,-}
\text{ are evaluations of one analytic co-moving field,}
}
\]

but

\[
\boxed{
\text{the current local setup does not force that realization.}
}
\]

So Local B cannot close the endpoint-separation subchannels from the present draft state. Also, even if Local B did prove endpoint-diagonal realization, the full local branch would still remain open because Local Agent 2 found an independent frozen \(\eta\eta\) odd-background survivor inside \(N^{\corr}\). 

---

# 1. Conditional proof if the source is endpoint-diagonal

Assume the source displacement is generated by a single analytic co-moving field:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

Then Taylor expansion gives

\[
\eta_{i,+}
=
\eta_i(h)
+\frac{\delta}{2}\eta_i'(h)
+\frac{\delta^2}{8}\eta_i''(h)
+\frac{\delta^3}{48}\eta_i'''(h)
+O(\delta^4),
\]

\[
\eta_{i,-}
=
\eta_i(h)
-\frac{\delta}{2}\eta_i'(h)
+\frac{\delta^2}{8}\eta_i''(h)
-\frac{\delta^3}{48}\eta_i'''(h)
+O(\delta^4).
\]

Therefore

\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
\frac{\delta}{2}\eta_i'(h)
+\frac{\delta^3}{48}\eta_i'''(h)
+O(\delta^5).
\]

Hence

\[
\boxed{
[\delta^0]\eta_i^\Delta=0.
}
\]

Then the endpoint-separation subchannels vanish in the frozen coefficient:

\[
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}=0,
\]

\[
Y^{\eta^\Sigma\eta^\Delta}_{g,0}=0.
\]

So this conditional theorem kills exactly the parity-bad endpoint-separation terms in

\[
E_{A,Y}^{\mathrm{BC}}.
\]

---

# 2. Why this is not forced by the current draft state

The active local coefficient is the frozen Bottleneck-C carrier:

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
[z^7]D(G_-^{-1/2})[A_-]Y_{12}^{(2)}R_0.
\]

The internal \([z^7\delta^1]\) table is not the first Bottleneck-C coefficient, because the amplitude

\[
a_1a_2(a_1+a_2)
\]

already supplies the first \(\delta\)-edge. 

The prompt asks Local B to prove from the paper’s source definitions that

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

But the current consolidated state explicitly says this is not yet proved: endpoint displacement sources are not currently established to be co-moving / endpoint-diagonal. If \(\eta_+\) and \(\eta_-\) are independent frozen endpoint variables, then \([\delta^0]\eta^\Delta\) can survive. 

Thus endpoint-swap symmetry alone is insufficient. It can tell us how the two endpoints transform under interchange, but it does not force the frozen equality

\[
\eta_{i,+}\big|_{\delta=0}
=
\eta_{i,-}\big|_{\delta=0}.
\]

That equality is exactly the missing source-realization input.

---

# 3. Concrete parity-bad survivor if endpoint data are independent

Suppose the source model permits independent frozen endpoint displacement data:

\[
\eta_{i,+}=u_i+O(\delta),
\qquad
\eta_{i,-}=v_i+O(\delta),
\]

with

\[
u_i\ne v_i.
\]

Then

\[
[\delta^0]\eta_i^\Delta
=
\frac{u_i-v_i}{2}
\ne0.
\]

The parity-bad frozen subchannels can then survive:

\[
d\eta^\Delta+\eta^\Delta d,
\]

\[
\eta^\Sigma\eta^\Delta.
\]

Take one active row in the frozen carrier:

\[
r+b+g=7.
\]

Using the actual finite Fréchet index convention of the paper, let \(a\) be any active same-point linear whitening index. The older shorthand \(a\in\{1,5\}\) should be replaced by the paper’s actual index set if it is \(a=2,\ldots,6\). This does not affect the obstruction.

Choose a formal good-patch model:

\[
W_{+,0}=I,
\qquad
\Lambda^-_{a,0}=I,
\]

and a surviving endpoint-separation Hessian piece

\[
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}=S.
\]

Then

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}(S)
=
S.
\]

So

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

The quotient obstruction is

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}
=
-u_5.
\]

The \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
-\frac{a_1^2}{c}.
\]

Thus independent endpoint displacement data allow a quotient-visible and \(T\)-visible survivor.

---

# 4. What Local B can and cannot close

Local B can close the endpoint-separation part under the theorem:

\[
\boxed{
\eta_{i,+},\eta_{i,-}
\text{ are evaluations of one analytic co-moving source-motion field.}
}
\]

Then

\[
[\delta^0]\eta_i^\Delta=0,
\]

and hence

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]

do not contribute to the frozen coefficient.

But Local B cannot close the entire local blocker anymore. The consolidated verdict says there is also an odd-background frozen \(\eta\eta\) survivor directly inside the corrected mixed block \(N^{\corr}(q_-,q_+,\Delta;s)\), independent of the \(\eta^\Delta\) endpoint-separation issue. In particular, differentiating

\[
N_{12}
=
\frac{\sin\Delta+q_+s\cos\Delta}{s^2}
\]

twice in \(\Delta\) produces the odd-background term

\[
-\frac{\sin\Delta_0}{s^2}\eta_i\eta_j,
\]

which lands in the active \(\eta\eta\) channel, not the killed \(d\eta-\eta d\) channel. 

So even a positive Local B theorem would only prove:

\[
\boxed{
\text{endpoint-separation subchannels vanish.}
}
\]

It would not prove

\[
E_{A,Y}^{\mathrm{BC}}=0.
\]

The remaining local theorem would still be the fixed-sector cancellation of the odd \(\eta\eta\) block:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,r}
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
W_{+,b}
\right)=0.
\]

---

# 5. The exact missing theorem

The endpoint-diagonal theorem should be stated separately:

```latex
\begin{theorem}[Endpoint-diagonal realization of displacement sources]
\label{thm:endpoint-diagonal-realization-displacement-sources}
For every active source direction \(\xi_i\) entering the promoted Hessian
\[
Y_{12}^{(2)}=D^2N_0[\xi_1,\xi_2],
\]
the endpoint displacement components are evaluations of one analytic
co-moving field:
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Consequently
\[
\eta_i^\Delta
:=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta),
\]
so
\[
[\delta^0]\eta_i^\Delta=0.
\]
\end{theorem}
```

Then the endpoint-separation corollary is:

```latex
\begin{corollary}[Frozen endpoint-separation subchannels vanish]
\label{cor:frozen-endpoint-separation-subchannels-vanish}
Under Theorem~\ref{thm:endpoint-diagonal-realization-displacement-sources},
the frozen Bottleneck-C coefficient has no contribution from
\[
d\eta^\Delta+\eta^\Delta d
\qquad\text{or}\qquad
\eta^\Sigma\eta^\Delta.
\]
\end{corollary}
```

And the adversarial alternative is:

```latex
\begin{lemma}[Endpoint-separation survivor]
\label{lem:endpoint-separation-survivor}
If the source model permits an active source direction with
\[
[\delta^0]\eta_i^\Delta\ne0,
\]
then the parity-bad endpoint-separation channels
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]
are not structurally killed in the frozen carrier. In particular, a formal
good-patch model can realize
\[
E_{A,Y}^{\mathrm{BC}}=S,
\]
so that
\[
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]
\end{lemma}
```

---

# 6. Final Local B status

\[
\boxed{
\text{Endpoint-diagonal realization remains an unproved source-realization theorem.}
}
\]

If proved, it removes:

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
\]

If false, those subchannels can give:

\[
f_{A,Y}\ne0,
\qquad
Q_{A,Y}\ne0.
\]

But either way, Local B does not close the whole local branch because the odd-background frozen \(\eta\eta\) term in \(N^{\corr}\) remains independent and must be handled by Local A.
## User (2026-04-25 12:40:18)

Do your instruction as per attached

## Assistant (2026-04-25 12:40:41)

_Thought for 21s_

## Local B — endpoint-separation cleanup

Target:

\[
[\delta^0]\eta_i^\Delta=0,
\qquad
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2.
\]

Current verdict:

\[
\boxed{
[\delta^0]\eta_i^\Delta=0
\text{ is not forced by the currently stated source structure.}
}
\]

It is true under an **endpoint-diagonal/co-moving source realization** assumption, but the attached consolidation explicitly says this theorem is not currently proved and that independent frozen endpoint displacement data would allow the endpoint-separation channels to survive. 

Also, even if this cleanup succeeds, it does **not** close the whole local branch anymore, because the separate scalar \(\eta\eta\) odd-background survivor in \(N^{\corr}\) remains live. 

---

# 1. Conditional closure of endpoint-separation channels

Assume each active source direction \(\xi_i\) has a single analytic co-moving endpoint displacement field:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

Then

\[
\eta_i^\Delta
=
\frac{\eta_i(h+\delta/2)-\eta_i(h-\delta/2)}2.
\]

Taylor expansion gives

\[
\eta_i^\Delta
=
\frac{\delta}{2}\eta_i'(h)
+
\frac{\delta^3}{48}\eta_i'''(h)
+
O(\delta^5).
\]

Therefore

\[
[\delta^0]\eta_i^\Delta=0.
\]

Consequently, the frozen coefficient has no contribution from the parity-bad endpoint-separation subchannels:

\[
Y^{d\eta^\Delta+\eta^\Delta d}_{g,0}=0,
\]

\[
Y^{\eta^\Sigma\eta^\Delta}_{g,0}=0.
\]

So under endpoint-diagonal realization, Local B removes exactly:

\[
\boxed{
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
}
\]

---

# 2. Why the current draft state does not prove it

Endpoint-swap symmetry alone only says the two endpoints transform into each other. It does **not** imply the frozen endpoint values are equal:

\[
\eta_{i,+}\big|_{\delta=0}
=
\eta_{i,-}\big|_{\delta=0}.
\]

The attached prompt distinguishes exactly these alternatives:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2)
\]

versus independent frozen endpoint variables. It asks Local B to prove or refute this endpoint-diagonal realization from the paper’s source definitions. 

With the currently supplied source state, I cannot derive the diagonal realization. The source definitions available in the prompt are not enough to exclude:

\[
\eta_{i,+}=u_i+O(\delta),
\qquad
\eta_{i,-}=v_i+O(\delta),
\qquad
u_i\ne v_i.
\]

Then

\[
[\delta^0]\eta_i^\Delta
=
\frac{u_i-v_i}{2}
\ne0.
\]

---

# 3. Explicit endpoint-separation survivor

Assume independent frozen endpoint displacement data. Let

\[
[\delta^0]\eta_i^\Delta\ne0.
\]

Then the channel

\[
d\eta^\Delta+\eta^\Delta d
\]

can survive in the frozen Hessian. Pick one active row with

\[
r+b+g=7.
\]

Use the paper’s actual finite Fréchet index convention for the same-point source slot; the older shorthand \(a\in\{1,5\}\) should not be relied on if the draft uses another index set such as \(a=2,\dots,6\). The attached prompt explicitly warns about this source-index issue. 

A formal surviving row is:

\[
\mathcal E_{\mathrm{sep}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,0}
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}
W_{+,0}
\right).
\]

Choose a good-patch model:

\[
\Lambda^-_{a,0}=I,
\qquad
W_{+,0}=I,
\qquad
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}=S.
\]

Then

\[
\mathcal E_{\mathrm{sep}}=S.
\]

Thus the endpoint-separation piece can contribute:

\[
E_{A,Y}^{\mathrm{BC}}=0\cdot I+1\cdot S.
\]

The two decisive local scalars become:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=-u_5,
\]

\[
f_{A,Y}=1.
\]

Therefore

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
-\frac{a_1^2}{c}.
\]

So if endpoint-displacement data are independent at the frozen face, Local B produces a concrete quotient-visible and \(T\)-visible survivor.

---

# 4. What Local B can conclude

Local B can only establish the following conditional result:

```latex
\begin{theorem}[Endpoint-diagonal cleanup]
Assume every active endpoint-displacement source direction is generated by
one analytic co-moving field,
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Then
\[
[\delta^0]\eta_i^\Delta=0,
\]
and the frozen endpoint-separation subchannels
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]
do not contribute to \(E_{A,Y}^{\mathrm{BC}}\).
\end{theorem}
```

And the adversarial alternative is:

```latex
\begin{lemma}[Endpoint-separation survivor]
If the source model permits an active direction with
\[
[\delta^0]\eta_i^\Delta\ne0,
\]
then the frozen endpoint-separation channels are not structurally killed.
In particular, a formal good-patch model can realize
\[
E_{A,Y}^{\mathrm{BC}}=S,
\]
so that
\[
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]
\end{lemma}
```

---

# 5. Final Local B status

\[
\boxed{
\text{Endpoint-diagonal realization remains an unproved source-realization theorem.}
}
\]

If proved, it removes only the endpoint-separation subchannels:

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
\]

If false, those subchannels can leak through \(S\), giving

\[
f_{A,Y}\ne0.
\]

But Local B no longer closes the entire local blocker, because the current frontier also contains the independent odd-background scalar \(\eta\eta\) block

\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J,
\]

which must be handled by the Local A fixed-sector cancellation theorem. 
## User (2026-04-25 12:47:35)

continue as per your exact prompt instruction

## Assistant (2026-04-25 12:48:01)

_Thought for 23s_

## Local B — endpoint-separation cleanup plus interaction with odd-\(\eta\eta\)

### Verdict

\[
\boxed{
[\delta^0]\eta_i^\Delta=0
\text{ is still only conditional.}
}
\]

It follows if the source model is **endpoint-diagonal / co-moving**:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

But the currently attached instructions do not provide a paper definition forcing this. They explicitly frame endpoint-diagonal realization as the Local B target to prove or refute, and distinguish it from the now-dominant odd-\(\eta\eta\) row. 

Even if endpoint-diagonal realization is proved, it only removes the endpoint-separation subchannels

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
\]

It does **not** kill the independent scalar \(\Delta\)-Hessian odd-\(\eta\eta\) block

\[
A_oJ
=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J.
\]

That block is now the lead local obstruction. turn69file14

---

# 1. Conditional proof of endpoint-separation cleanup

Define

\[
\eta_i^\Sigma=\frac{\eta_{i,+}+\eta_{i,-}}2,
\qquad
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2.
\]

Assume endpoint-diagonal realization:

\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]

Then Taylor expansion gives

\[
\eta_{i,+}
=
\eta_i(h)
+\frac{\delta}{2}\eta_i'(h)
+\frac{\delta^2}{8}\eta_i''(h)
+\frac{\delta^3}{48}\eta_i'''(h)
+O(\delta^4),
\]

\[
\eta_{i,-}
=
\eta_i(h)
-\frac{\delta}{2}\eta_i'(h)
+\frac{\delta^2}{8}\eta_i''(h)
-\frac{\delta^3}{48}\eta_i'''(h)
+O(\delta^4).
\]

Therefore

\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
\frac{\delta}{2}\eta_i'(h)
+
\frac{\delta^3}{48}\eta_i'''(h)
+
O(\delta^5).
\]

So

\[
\boxed{
[\delta^0]\eta_i^\Delta=0.
}
\]

Hence the frozen coefficient has no endpoint-separation contribution from

\[
d\eta^\Delta+\eta^\Delta d,
\]

or from

\[
\eta^\Sigma\eta^\Delta.
\]

So the conditional theorem is:

\[
\boxed{
\text{endpoint-diagonal realization}
\Longrightarrow
\text{frozen endpoint-separation subchannels vanish.}
}
\]

---

# 2. If endpoint data are independent, there is a survivor

If the source model permits independent frozen endpoint displacement data,

\[
\eta_{i,+}=u_i+O(\delta),
\qquad
\eta_{i,-}=v_i+O(\delta),
\]

with

\[
u_i\ne v_i,
\]

then

\[
[\delta^0]\eta_i^\Delta
=
\frac{u_i-v_i}{2}
\ne0.
\]

Then a parity-bad endpoint-separation row can survive. A minimal formal row is

\[
\mathcal E_{\Delta}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,0}
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}
W_{+,0}
\right),
\]

with the source index \(a\) taken from the paper’s actual finite Fréchet convention, not the older shorthand. The current instructions warn that the active convention may use \(a=2,\dots,6\), and the concrete lead obstruction uses \(a=2\). turn68file13

A formal good-patch model is:

\[
\Lambda^-_{a,0}=I,
\qquad
W_{+,0}=I,
\qquad
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}=S.
\]

Then

\[
\mathcal E_\Delta=S.
\]

Thus

\[
e_{A,Y}=0,
\qquad
f_{A,Y}=1.
\]

So the two decisive local tests fail generically:

\[
Q_{A,Y}=e_{A,Y}v_5-u_5f_{A,Y}=-u_5,
\]

and

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
=
-\frac{a_1^2}{c}.
\]

Therefore, if endpoint-diagonal realization is false, the endpoint-separation subbranch itself can leak through both the quotient and \(T\)-horizontal tests.

---

# 3. Interaction with the odd-\(\eta\eta\) row

Endpoint-diagonal realization does **not** impose the needed relation on the scalar \(\eta\eta\) product.

Under endpoint-diagonal realization,

\[
\eta_i^\Sigma
=
\eta_i(h)
+
O(\delta^2),
\]

so the frozen scalar product

\[
[\delta^0](\eta_i\eta_j)
\]

is generally

\[
\eta_i(h)\eta_j(h),
\]

not zero.

Thus endpoint-diagonal cleanup can kill terms containing one factor of \(\eta^\Delta\), but it does not kill a scalar \(\Delta\)-Hessian term of the form

\[
A_oJ\,\eta_i\eta_j.
\]

In particular, it gives no reason for

\[
\nu_{\eta\eta,7}
=
[z^7]\left(
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right)
\]

to vanish.

The current local obstruction is exactly this odd-\(\eta\eta\) row. The attached summary states that the row

\[
(a,r,g,b)=(2,0,7,0),
\qquad
\chi=\eta\eta_{\mathrm{odd}},
\]

can produce a nonzero \(S\)-component and hence nonzero

\[
\partial_\kappa T.
\]

It also notes quotient failure on a generic \(u_5\ne0\) patch. turn69file14

So:

\[
\boxed{
\text{Endpoint-diagonal realization does not close }E_{A,Y}^{\mathrm{BC}}.
}
\]

It only removes the endpoint-separation subchannels.

---

# 4. The precise Local B theorem package

The positive theorem Local B can supply is:

```latex
\begin{theorem}[Endpoint-diagonal cleanup]
Assume every active endpoint-displacement source direction is generated by a
single analytic co-moving field:
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Then
\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta).
\]
Consequently,
\[
[\delta^0]\eta_i^\Delta=0,
\]
and the frozen endpoint-separation subchannels
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]
do not contribute to \(E_{A,Y}^{\mathrm{BC}}\).
\end{theorem}
```

The adversarial alternative is:

```latex
\begin{lemma}[Endpoint-separation survivor]
If the source model allows an active direction with
\[
[\delta^0]\eta_i^\Delta\ne0,
\]
then the frozen endpoint-separation channels are not structurally killed.
A formal good-patch model can realize
\[
E_{A,Y}^{\mathrm{BC}}=S,
\]
and hence
\[
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]
\end{lemma}
```

And the non-interference statement with the lead odd-\(\eta\eta\) obstruction is:

```latex
\begin{remark}[Endpoint cleanup does not remove the scalar \(\eta\eta\) obstruction]
Even under endpoint-diagonal realization, the scalar product
\[
[\delta^0](\eta_i\eta_j)=\eta_i(h)\eta_j(h)
\]
need not vanish. Therefore endpoint-diagonal cleanup does not remove the
odd-background scalar \(\eta\eta\) row
\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J\,\eta_i\eta_j.
\]
That row requires a separate fixed-sector cancellation theorem.
\end{remark}
```

---

# 5. Final Local B status

\[
\boxed{
\text{Local B does not close the local branch.}
}
\]

It produces a conditional cleanup:

\[
\boxed{
\text{endpoint-diagonal realization}
\Rightarrow
d\eta^\Delta+\eta^\Delta d
\text{ and }
\eta^\Sigma\eta^\Delta
\text{ vanish at the frozen face.}
}
\]

If endpoint-diagonal realization is false, there is a concrete endpoint-separation survivor with possible \(S\)-projection.

If endpoint-diagonal realization is true, the lead local blocker remains the independent odd-\(\eta\eta\) row:

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}.
}
\]

Thus the next local work should stay focused on the odd-\(\eta\eta\) fixed-sector cancellation theorem, not on endpoint-separation cleanup.
## User (2026-04-25 12:49:07)

continue your attack

## Assistant (2026-04-25 12:49:29)

_Thought for 19s_

## Local B continued — endpoint-separation cleanup under the actual \(N^{\corr}(q_-,q_+,\Delta;s)\) variables

### Verdict

For the **actual corrected mixed block as currently written**,

\[
N^{\corr}=N^{\corr}(q_-,q_+,\Delta;s),
\]

the primitive source variables are

\[
d_{i,-},\qquad d_{i,+},\qquad \eta_i:=\delta\Delta_i.
\]

There is no independent primitive pair

\[
\eta_{i,+},\eta_{i,-}
\]

inside this displayed \(N^{\corr}\). Therefore the endpoint-separation subbranch

\[
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2
\]

is either:

1. **absent from the actual \(N^{\corr}\) source model**, if \(\eta_i\) is defined only as the scalar variation of \(\Delta\); or  
2. **an additional source-realization layer not specified by the current \(N^{\corr}\) formula**, in which case endpoint-diagonal realization remains an extra theorem.

So Local B can sharpen the status:

\[
\boxed{
\text{No independent endpoint-separation survivor is visible inside }N^{\corr}(q_-,q_+,\Delta;s)\text{ itself.}
}
\]

But this still does **not** close the local branch, because the lead obstruction is now the scalar \(\Delta\)-Hessian \(\eta\eta\) block

\[
A_oJ
=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J,
\]

which is independent of any \(\eta^\Delta\) endpoint split. The attached instructions explicitly identify this odd \(\eta\eta\) row as the lead local obstruction and say endpoint-diagonal cleanup does not handle it. turn70file18

---

# 1. Direct reading of the \(N^{\corr}\) source variables

The corrected mixed block is written as a function of

\[
(q_-,q_+,\Delta;s).
\]

For a source direction \(\xi_i\), the first variation has the form

\[
\xi_i=(d_{i,-},d_{i,+},\eta_i),
\]

where

\[
d_{i,-}=\delta q_-,
\qquad
d_{i,+}=\delta q_+,
\qquad
\eta_i=\delta \Delta.
\]

The Hessian \(D^2N_0[\xi_i,\xi_j]\) therefore has source channels:

\[
dd,
\qquad
d\eta+\eta d,
\qquad
\eta\eta.
\]

But these are scalar-\(\Delta\) channels. The \(\eta\) here is not visibly an endpoint displacement pair. It is the variation of the phase gap

\[
\Delta=\Phi_+-\Phi_-.
\]

Thus the split

\[
\eta^\Sigma=\frac{\eta_++\eta_-}{2},
\qquad
\eta^\Delta=\frac{\eta_+-\eta_-}{2}
\]

is not native to the displayed \(N^{\corr}\). It only applies if the paper separately defines endpoint phase motions

\[
\eta_{i,+},\eta_{i,-}
\]

and then sets

\[
\eta_i=\eta_{i,+}-\eta_{i,-}
\]

or some equivalent expression.

---

# 2. Consequence: endpoint-separation cleanup is either automatic or external

There are two cases.

## Case A: \(\eta_i\) is only the scalar \(\Delta\)-variation

Then there is no independent endpoint-separation source variable in the actual mixed block.

In that case, the endpoint-separation subchannels

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]

are not part of \(D^2N_0[\xi_i,\xi_j]\) as written.

So Local B can mark those endpoint-separation subchannels as absent from \(N^{\corr}\).

But then the scalar channel

\[
\eta\eta
\]

remains fully active, and it is exactly where the odd-background survivor lives.

## Case B: \(\eta_i\) is induced from endpoint motions

Suppose instead the paper defines endpoint motions

\[
\eta_{i,+},\eta_{i,-}
\]

and then the scalar \(\eta_i\) in \(N^{\corr}\) is induced from them.

Then Local B needs an endpoint-diagonal theorem:

\[
\eta_{i,+}=\eta_i^{\mathrm{field}}(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i^{\mathrm{field}}(h-\delta/2).
\]

This implies

\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta).
\]

Then

\[
[\delta^0]\eta_i^\Delta=0,
\]

and the frozen endpoint-separation subchannels vanish.

But this is an additional source-realization theorem. It does not follow merely from endpoint-swap symmetry.

---

# 3. Endpoint-separation survivor if endpoint data are independent

If endpoint data are independent at the frozen face, take

\[
\eta_{i,+}=u_i+O(\delta),
\qquad
\eta_{i,-}=v_i+O(\delta),
\qquad
u_i\ne v_i.
\]

Then

\[
[\delta^0]\eta_i^\Delta
=
\frac{u_i-v_i}{2}
\ne0.
\]

A parity-bad frozen endpoint-separation row can survive:

\[
\mathcal E_\Delta
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,0}
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}
W_{+,0}
\right).
\]

Using a formal good-patch model,

\[
\Lambda^-_{a,0}=I,
\qquad
W_{+,0}=I,
\qquad
Y^{d\eta^\Delta+\eta^\Delta d}_{7,0}=S,
\]

we get

\[
\mathcal E_\Delta=S.
\]

Thus

\[
f_{A,Y}=1,
\qquad
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]

So if independent endpoint displacement data are admitted, endpoint-separation leakage remains possible.

---

# 4. Does endpoint-diagonal cleanup affect the odd \(\eta\eta\) row?

No.

The odd \(\eta\eta\) row comes from differentiating \(N^{\corr}\) twice with respect to the scalar phase-gap variable \(\Delta\):

\[
\left[\partial_\Delta^2N_0\right]_{\eta\eta,\mathrm{odd}}
=
A_oJ,
\]

where

\[
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

This row is scalar-\(\eta\eta\), not endpoint-\(\eta^\Delta\). The current instructions identify the concrete active row as

\[
(a,r,g,b)=(2,0,7,0),
\qquad
\chi=\eta\eta_{\mathrm{odd}},
\]

and state that it can produce a nonzero \(S\)-component, hence nonzero \(f_{A,Y}\) and nonzero \(T\)-slope. turn70file15

Endpoint-diagonal realization would imply

\[
[\delta^0]\eta^\Delta=0,
\]

but it does not imply

\[
[\delta^0](\eta_i\eta_j)=0.
\]

Indeed, under a co-moving field,

\[
\eta_i(h+\delta/2)=\eta_i(h)+O(\delta),
\]

so the frozen scalar product is

\[
[\delta^0](\eta_i\eta_j)=\eta_i(h)\eta_j(h),
\]

which is generally nonzero.

Therefore endpoint-diagonal cleanup does not impose

\[
\nu_{\eta\eta,7}
=
[z^7]\left(A_o\eta_i\eta_j\right)
=0.
\]

---

# 5. Local B deliverable

The clean theorem Local B can provide is conditional:

```latex
\begin{theorem}[Endpoint-separation cleanup]
Assume every endpoint displacement source is generated by one analytic
co-moving field:
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Then
\[
\eta_i^\Delta
=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta).
\]
Consequently the frozen endpoint-separation subchannels
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]
do not contribute to \(E_{A,Y}^{\mathrm{BC}}\).
\end{theorem}
```

The adversarial alternative is:

```latex
\begin{lemma}[Endpoint-separation survivor]
If the source model permits an active direction with
\[
[\delta^0]\eta_i^\Delta\ne0,
\]
then the frozen endpoint-separation channels are not structurally killed.
A formal good-patch model realizes
\[
E_{A,Y}^{\mathrm{BC}}=S,
\]
and hence
\[
Q_{A,Y}=-u_5,
\qquad
\partial_\kappa T=-a_1^2/c.
\]
\end{lemma}
```

And the interaction statement is:

```latex
\begin{remark}[Endpoint cleanup does not remove scalar \(\eta\eta\)]
Even under endpoint-diagonal realization,
\[
[\delta^0](\eta_i\eta_j)=\eta_i(h)\eta_j(h)
\]
is generally nonzero. Hence endpoint cleanup does not remove the odd
scalar \(\eta\eta\) row
\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J\,\eta_i\eta_j.
\]
That row requires a separate fixed-sector cancellation theorem.
\end{remark}
```

---

# 6. Final Local B status

\[
\boxed{
\text{If }\eta\text{ is only the scalar }\Delta\text{-variation in }N^{\corr},
\text{ endpoint-separation channels are absent from }N^{\corr}.
}
\]

\[
\boxed{
\text{If the paper separately allows endpoint displacement variables, endpoint-diagonal realization remains unproved.}
}
\]

Either way:

\[
\boxed{
\text{Local B does not affect the lead odd-\(\eta\eta\) obstruction.}
}
\]

The next local work should remain on

\[
\mathcal E^{2}_{\eta\eta;7,0,0},
\]

specifically whether

\[
\nu_{\eta\eta,7}=0
\]

or whether \(\Lambda^-_{2,0}\) and \(W_{+,0}\) force fixed-sector \(S\)-projection cancellation.
## User (2026-04-25 12:50:24)

continue your attack

## Assistant (2026-04-25 12:50:25)

I’ll continue Local B by cleaning up a variable-level ambiguity: whether the \(\eta^\Delta\) split is a real source degree of freedom or a derived, gauge-dependent decomposition of the scalar \(\Delta\)-variation. This matters because only actual source variables can support a real obstruction.

_Thought for 9s_

## Local B continued — the \(\eta^\Delta\) split is not invariant unless endpoint phases are primitive

### Verdict

The endpoint-separation branch is now sharper:

\[
\boxed{
\text{If }N^{\corr}\text{ is truly formulated only in }(q_-,q_+,\Delta;s),
\text{ then }\eta^\Delta\text{ is not an independent source channel.}
}
\]

In that case, Local B should stop treating

\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]

as genuine \(N^{\corr}\)-Hessian channels. They are artifacts of choosing an endpoint-phase lift of the scalar gap variation

\[
\eta=\delta\Delta.
\]

However:

\[
\boxed{
\text{this does not help the local proof, because the lead obstruction is the scalar }\eta\eta\text{ row.}
}
\]

The latest instructions identify the lead local obstruction as the odd scalar \(\eta\eta\) top row

\[
\mathcal E^2_{\eta\eta;7,0,0},
\]

coming from

\[
A_oJ=
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J.
\]

Endpoint-diagonal cleanup is explicitly secondary and does not remove this row. 

---

# 1. Scalar \(\eta\) versus endpoint lift

The displayed corrected mixed block has primitive variables

\[
N^{\corr}=N^{\corr}(q_-,q_+,\Delta;s).
\]

Thus a source direction has the form

\[
\xi_i=(d_{i,-},d_{i,+},\eta_i),
\qquad
\eta_i=\delta\Delta_i.
\]

There is no visible primitive pair

\[
(\eta_{i,+},\eta_{i,-})
\]

in \(N^{\corr}\). If one introduces endpoint phase variations anyway, they satisfy only

\[
\eta_i=\eta_{i,+}-\eta_{i,-}.
\]

But the decomposition into

\[
\eta_i^\Sigma=\frac{\eta_{i,+}+\eta_{i,-}}2,
\qquad
\eta_i^\Delta=\frac{\eta_{i,+}-\eta_{i,-}}2
\]

is not intrinsic unless \(\eta_{i,+}\) and \(\eta_{i,-}\) are themselves part of the source model.

Indeed,

\[
\eta_i^\Delta=\frac{\eta_i}{2}
\]

if \(\eta_i\) is the gap variation. This is generally nonzero at the frozen face. So the earlier condition

\[
[\delta^0]\eta_i^\Delta=0
\]

is not a consequence of the scalar \(N^{\corr}(q_-,q_+,\Delta;s)\) model. It only makes sense for a different object: endpoint displacement fields evaluated at two nearby collision centers.

---

# 2. Gauge ambiguity of endpoint lifts

If only the scalar gap variation

\[
\eta_i=\eta_{i,+}-\eta_{i,-}
\]

is observable, then endpoint lifts are gauge-dependent:

\[
\eta_{i,+}\mapsto \eta_{i,+}+\rho_i,
\qquad
\eta_{i,-}\mapsto \eta_{i,-}+\rho_i.
\]

This leaves

\[
\eta_i=\eta_{i,+}-\eta_{i,-}
\]

unchanged.

Therefore any theorem phrased in terms of the endpoint average

\[
\eta_i^\Sigma
\]

or endpoint separation

\[
\eta_i^\Delta
\]

must first prove that the endpoint lift is canonical in the paper’s source model.

Without such a canonical lift, the endpoint-separation subchannels are not well-defined source channels of \(N^{\corr}\). The actual Hessian channels are simply:

\[
dd,
\qquad
d\eta+\eta d,
\qquad
\eta\eta.
\]

---

# 3. Endpoint-diagonal realization does not kill scalar \(\eta\)

Suppose, favorably, the paper does define endpoint fields

\[
\eta_{i,+}=\eta_i^{\rm field}(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i^{\rm field}(h-\delta/2).
\]

Then

\[
\eta_{i,+}-\eta_{i,-}
=
\delta(\eta_i^{\rm field})'(h)+O(\delta^3).
\]

This proves that the scalar gap variation induced by a smooth co-moving field is \(O(\delta)\) in the **collision-center separation** variable.

But this is a statement about the source-motion layer. The active Bottleneck-C coefficient is frozen internally; the first \(\delta\)-edge is already supplied externally by

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2).
\]

The current active coefficient is explicitly frozen, not the internal \([z^7\delta^1]\) table. 

So endpoint-diagonal realization can remove endpoint-separation artifacts, but it does not force the scalar product

\[
\eta_i\eta_j
\]

inside

\[
\partial_\Delta^2N_0[\eta_i,\eta_j]
\]

to vanish unless the scalar \(\eta_i\) itself is internal-\(\delta\)-small in the exact coefficient being used. That would be a different order-counting theorem and would need to be stated explicitly.

---

# 4. Consequence for Local B

Local B has two possible clean conclusions, depending on how the paper defines sources.

## Case A: \(N^{\corr}\) only uses scalar \(\Delta\)

Then endpoint-separation subchannels are not actual channels.

The valid statement is:

\[
\boxed{
\text{There is no independent }d\eta^\Delta+\eta^\Delta d
\text{ or }\eta^\Sigma\eta^\Delta
\text{ obstruction inside }N^{\corr}(q_-,q_+,\Delta;s).
}
\]

The local branch reduces to the scalar channels, especially the odd \(\eta\eta\) row.

## Case B: the paper has primitive endpoint fields

Then Local B needs the theorem:

\[
\eta_{i,+}=\eta_i^{\rm field}(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i^{\rm field}(h-\delta/2).
\]

Only under this theorem can we assert:

\[
[\delta^0]\left(\frac{\eta_{i,+}-\eta_{i,-}}2\right)=0.
\]

If endpoint fields are independent at the frozen face, then Local B has a real endpoint-separation survivor.

---

# 5. Updated theorem package

The cleanest Local B theorem is now:

```latex
\begin{theorem}[No independent endpoint-separation channel in scalar \(N^{\corr}\)]
\label{thm:no-independent-endpoint-separation-channel-scalar-Ncorr}
Assume the corrected mixed block is formulated with source variables
\[
(q_-,q_+,\Delta;s)
\]
and source directions
\[
\xi_i=(d_{i,-},d_{i,+},\eta_i),
\qquad
\eta_i=\delta\Delta_i.
\]
Then the promoted Hessian
\[
D^2N_0[\xi_i,\xi_j]
\]
has only the scalar channels
\[
dd,\qquad d\eta+\eta d,\qquad \eta\eta.
\]
In particular, endpoint-lift channels
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta
\]
are not intrinsic channels of \(N^{\corr}\) unless the paper separately
introduces primitive endpoint variables \(\eta_{i,+},\eta_{i,-}\).
\end{theorem}
```

If endpoint variables are primitive, the required theorem is:

```latex
\begin{theorem}[Endpoint-diagonal realization of primitive endpoint fields]
\label{thm:endpoint-diagonal-realization-primitive-fields}
For every primitive endpoint field entering the promoted Hessian,
\[
\eta_{i,+}=\eta_i(h+\delta/2),
\qquad
\eta_{i,-}=\eta_i(h-\delta/2).
\]
Consequently,
\[
\eta_i^\Delta
:=
\frac{\eta_{i,+}-\eta_{i,-}}2
=
O(\delta).
\]
\end{theorem}
```

And the warning should be:

```latex
\begin{remark}[Endpoint cleanup does not remove scalar \(\eta\eta\)]
Even if endpoint-separation channels are absent or killed, the scalar Hessian
channel
\[
\partial_\Delta^2N_0[\eta_i,\eta_j]
\]
remains. In particular, endpoint cleanup does not remove the odd-background
row
\[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)J\,\eta_i\eta_j.
\]
That row requires a separate fixed-sector cancellation theorem.
\end{remark}
```

---

# 6. Final status of this continuation

\[
\boxed{
\text{Local B can probably eliminate endpoint-separation confusion if }N^{\corr}
\text{ is scalar in }\Delta.
}
\]

But:

\[
\boxed{
\text{Local B cannot close the local branch.}
}
\]

The lead obstruction remains:

\[
\boxed{
\mathcal E^2_{\eta\eta;7,0,0}
}
\]

and specifically the question whether

\[
\nu_{\eta\eta,7}
=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right]
\]

vanishes, or whether

\[
\Lambda^-_{2,0}
\quad\text{and}\quad
W_{+,0}
\]

force fixed-sector \(S\)-projection cancellation.
## User (2026-04-25 12:51:30)

continue your attack

## Assistant (2026-04-25 12:51:31)

I’ll continue by testing whether the scalar \(\eta\eta\) row itself can be killed by co-moving phase-gap structure. This is distinct from the endpoint-separation cleanup and targets the current lead row indirectly.

_Thought for 34s_

## Local B continued — co-moving source structure does **not** kill the scalar \(\eta\eta\) row

I pushed the endpoint-diagonal/co-moving route against the current lead local row:

\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]

The result is negative for closure:

\[
\boxed{
\text{Even if endpoint-diagonal realization holds, the scalar }\eta\eta\text{ odd row is generically nonzero.}
}
\]

So Local B can at best remove endpoint-separation artifacts. It cannot help with the current lead obstruction

\[
A_oJ\,\eta_i\eta_j,
\qquad
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

The attached instructions identify this \(A_oJ\) block, especially the row \((a,r,g,b)=(2,0,7,0)\), as the current lead local obstruction. 

---

# 1. Assume the favorable co-moving phase-gap model

Assume the best case for Local B: the phase source is generated by one analytic field \(\varphi_i(t)\), so the scalar gap variation is

\[
\eta_i(s)
=
\varphi_i(m+s/2)-\varphi_i(m-s/2).
\]

Then \(\eta_i\) is odd in \(s\).

After affine removal, the first nonzero term is cubic:

\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+O(s^7).
\]

Likewise,

\[
\eta_j(s)=\alpha_j s^3+\beta_j s^5+O(s^7).
\]

Therefore

\[
\eta_i(s)\eta_j(s)
=
\alpha_i\alpha_j s^6
+
(\alpha_i\beta_j+\beta_i\alpha_j)s^8
+
O(s^{10}).
\]

So endpoint-diagonal/co-moving realization does **not** make

\[
\eta_i\eta_j
\]

vanish at the frozen face. It makes it even in \(s\).

---

# 2. Expansion of the odd scalar multiplier \(A_o\)

Write

\[
q=q_0(m),
\qquad
q_2=q_0''(m).
\]

For the midpoint phase gap,

\[
\Delta_0(s)
=
q s+\frac{q_2}{24}s^3+O(s^5).
\]

For the even endpoint average,

\[
q_e(s)
=
\frac{q_0(m+s/2)+q_0(m-s/2)}2
=
q+\frac{q_2}{8}s^2+O(s^4).
\]

Then

\[
\frac{\sin\Delta_0}{s^2}
=
\frac{q}{s}
+
\left(
\frac{q_2}{24}
-
\frac{q^3}{6}
\right)s
+
O(s^3),
\]

and

\[
\frac{q_e\cos\Delta_0}{s}
=
\frac{q}{s}
+
\left(
\frac{q_2}{8}
-
\frac{q^3}{2}
\right)s
+
O(s^3).
\]

Thus

\[
A_o(s)
=
\frac{2q}{s}
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)s
+
O(s^3).
\]

This matches the current local summary: the companion \(q_e\cos\Delta_0/s\) term does **not** cancel the \(\sin\Delta_0/s^2\) term; it combines with it. 

---

# 3. The \(s^7\) coefficient is generically nonzero

Now compute

\[
A_o(s)\eta_i(s)\eta_j(s).
\]

Using the expansions above:

\[
A_o\eta_i\eta_j
=
\frac{2q}{s}
\left[
\alpha_i\alpha_j s^6
+
(\alpha_i\beta_j+\beta_i\alpha_j)s^8
\right]
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)s
\alpha_i\alpha_j s^6
+
O(s^9).
\]

So

\[
A_o\eta_i\eta_j
=
2q\,\alpha_i\alpha_j s^5
+
\nu_{\eta\eta,7}s^7
+
O(s^9),
\]

where

\[
\boxed{
\nu_{\eta\eta,7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
}
\]

There is no structural reason for this to vanish.

For example, take

\[
\beta_i=\beta_j=0.
\]

Then

\[
\nu_{\eta\eta,7}
=
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
\]

On a good phase patch with

\[
q\ne0
\]

and no special relation

\[
q_2=4q^3,
\]

this is nonzero.

Therefore:

\[
\boxed{
\text{co-moving source realization does not force }\nu_{\eta\eta,7}=0.
}
\]

---

# 4. Consequence for the row \(\mathcal E^2_{\eta\eta;7,0,0}\)

The lead row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right).
\]

Local A’s current reduction gives

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]

For diagonal

\[
W_{+,0}=\operatorname{diag}(u,v),
\]

the row has an \(S\)-coefficient proportional to

\[
\nu_{\eta\eta,7}u.
\]

The current consolidation states precisely that this row can produce

\[
f_{A,Y}\ne0,
\]

and hence

\[
\partial_\kappa T
=
-a_1^2\frac{f_{A,Y}}{c}
\ne0.
\]

It can also be quotient-visible on a generic \(u_5\ne0\) patch. 

Thus the endpoint-diagonal/co-moving source theorem does **not** rescue the odd-\(\eta\eta\) row.

---

# 5. What Local B has now proved/refuted

Local B can still conditionally prove:

\[
[\delta^0]\eta^\Delta=0
\]

for endpoint-separation variables, if they are co-moving endpoint fields.

But Local B now refutes the stronger hope:

\[
\text{endpoint-diagonal/co-moving source}
\quad\Longrightarrow\quad
\nu_{\eta\eta,7}=0.
\]

Indeed, under the most favorable co-moving phase-gap model,

\[
\nu_{\eta\eta,7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j,
\]

which is generically nonzero.

---

# 6. Sharper missing theorem

The needed local theorem is no longer about endpoint-diagonal realization. It must be a specific cancellation theorem for the scalar row:

```latex
\begin{theorem}[Odd-\(\eta\eta\) top-row cancellation]
For the lead odd-background scalar row
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right),
\]
where
\[
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s},
\]
one has
\[
\mathcal E^{2}_{\eta\eta;7,0,0}=0.
\]
\end{theorem}
```

Equivalently, the theorem must prove one of:

\[
\nu_{\eta\eta,7}=0,
\]

\[
\Lambda^-_{2,0}=0,
\]

or

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}J W_{+,0}
\right)
=0.
\]

Local B’s attack shows the first option,

\[
\nu_{\eta\eta,7}=0,
\]

is false generically under co-moving source structure.

So any closure must come from the **matrix fixed-sector contraction**, not from endpoint-diagonal or co-moving scalar source parity.

---

# 7. Final status

\[
\boxed{
\text{Endpoint-diagonal cleanup is no longer a promising route to local closure.}
}
\]

It removes only endpoint-separation artifacts.

The lead obstruction survives even in the favorable co-moving model through

\[
\nu_{\eta\eta,7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
\]

Therefore the next local attack should focus exclusively on the matrix contraction:

\[
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,0}J W_{+,0}
\right),
\]

or on a same-row/top-row cancellation from another active \(\eta\eta\) term.
## User (2026-04-25 12:53:11)

continue your attack

## Assistant (2026-04-25 12:53:12)

I’ll now attack the only remaining possible local escape for this row: the matrix contraction  
\(\tau\pi_{\mathfrak f}\operatorname{Sym}(\Lambda^-_{2,0}J W_{+,0})\).  
The scalar coefficient \(\nu_{\eta\eta,7}\) is generically nonzero, so closure can only come from this matrix factor or cancellation with another top-row term.

_Thought for 29s_

## Local B continued — matrix contraction of the odd-\(\eta\eta\) top row

I attacked the remaining escape:

\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\,\eta_i\eta_j]_7
W_{+,0}
\right)=0,
\]

where

\[
A_o=
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

The attached status identifies this exact row,

\[
(a,r,g,b)=(2,0,7,0),
\qquad
\chi=\eta\eta_{\rm odd},
\]

as the lead local obstruction, with

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]

It also notes that for diagonal \(W_{+,0}\), this row contributes an \(S\)-component and hence can make \(f_{A,Y}\neq0\). 

My conclusion:

\[
\boxed{
\text{The matrix contraction does not vanish structurally.}
}
\]

More sharply:

\[
\boxed{
\text{On a generic good patch, the row is \(S\)-visible unless }
\nu_{\eta\eta,7}=0
\text{ or a separate same-row cancellation is added.}
}
\]

---

# 1. Compute the matrix factor

Let

\[
\Lambda^-_{2,0}=\lambda E_{22},
\qquad
\lambda=-\frac{1}{24\pi q^3}.
\]

Let

\[
W_{+,0}=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix}.
\]

Then

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
u&w
\end{pmatrix}.
\]

Using the fixed-sector projection formula already isolated in the local work,

\[
\pi_{\mathfrak f}\operatorname{Sym}(LJW)
=
[c(u-v)+w(d-a)]I+[ud-av]S
\]

for

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
\end{pmatrix},
\]

we get, for \(L=\lambda E_{22}\),

\[
a=0,\qquad c=0,\qquad d=\lambda.
\]

Therefore

\[
\pi_{\mathfrak f}\operatorname{Sym}(\lambda E_{22}JW_{+,0})
=
\lambda w\,I+\lambda u\,S.
\]

Thus the \(S\)-coefficient is

\[
\boxed{
\lambda u.
}
\]

Since \(W_{+,0}=G_{+,0}^{-1/2}\) is a good-patch inverse square root, its first diagonal coefficient \(u\) is nonzero on the nondegenerate patch. Also

\[
\lambda=-\frac1{24\pi q^3}
\]

is nonzero when \(q\neq0\).

So the matrix factor is generically \(S\)-visible.

---

# 2. Include the scalar coefficient

Let

\[
\nu_{\eta\eta,7}
:=
[z^7]\left(A_o\eta_i\eta_j\right).
\]

Then the row contributes

\[
\mathcal E^2_{\eta\eta;7,0,0}
=
\lambda\nu_{\eta\eta,7}
\left(
wI+uS
\right)
\]

up to the harmless fixed-sector transport \(\tau_{h\to m}\).

Hence

\[
e_{\eta\eta}^{(2,7)}
=
\lambda\nu_{\eta\eta,7}w,
\]

\[
f_{\eta\eta}^{(2,7)}
=
\lambda\nu_{\eta\eta,7}u.
\]

In particular,

\[
\boxed{
f_{\eta\eta}^{(2,7)}
=
-\frac{u}{24\pi q^3}\nu_{\eta\eta,7}.
}
\]

So \(T\)-horizontal closure for this row requires

\[
\boxed{
\nu_{\eta\eta,7}=0
}
\]

or a separate cancellation from another active row.

---

# 3. The scalar coefficient is generically nonzero

Under a favorable co-moving phase-gap model,

\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+O(s^7),
\]

\[
\eta_j(s)=\alpha_j s^3+\beta_j s^5+O(s^7),
\]

and

\[
A_o(s)
=
\frac{2q}{s}
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)s
+
O(s^3).
\]

Then

\[
\nu_{\eta\eta,7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
\]

This has no structural reason to vanish. For example, if

\[
\beta_i=\beta_j=0,
\]

then

\[
\nu_{\eta\eta,7}
=
\left(
\frac{q_2}{6}
-
\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
\]

On a good phase patch with

\[
q\neq0,
\qquad
q_2\neq4q^3,
\qquad
\alpha_i\alpha_j\neq0,
\]

this is nonzero.

So the scalar side does not save the row.

---

# 4. Quotient and \(T\)-visibility

For this row,

\[
e=\lambda\nu_{\eta\eta,7}w,
\qquad
f=\lambda\nu_{\eta\eta,7}u.
\]

The quotient determinant is

\[
Q=e v_5-u_5 f.
\]

Thus

\[
Q
=
\lambda\nu_{\eta\eta,7}
\left(
wv_5-u u_5
\right).
\]

So quotient closure requires

\[
wv_5-u u_5=0
\]

or

\[
\nu_{\eta\eta,7}=0.
\]

For diagonal \(W_{+,0}\), \(w=0\), and therefore

\[
Q=-\lambda\nu_{\eta\eta,7}u\,u_5.
\]

On a generic \(u_5\neq0\) patch, this is nonzero.

The \(T\)-slope is

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
=
-a_1^2\frac{\lambda\nu_{\eta\eta,7}u}{c}.
\]

Thus, generically,

\[
\boxed{
\partial_\kappa T\neq0.
}
\]

---

# 5. Can another top-row term cancel it?

The only possible rescue is a same-order cancellation. It would need another active top-row \(\eta\eta\) contribution with the same scalar coefficient structure and opposite fixed-sector projection.

But the current lead row is already the odd off-diagonal block of

\[
\partial_\Delta^2N_0.
\]

The companion term

\[
\frac{q_e\cos\Delta_0}{s}
\]

has already been included in

\[
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}.
\]

The attached status says this companion does **not** cancel \(\sin\Delta_0/s^2\); near a good patch it reinforces it, with

\[
A_o\sim\frac{2q_0}{s}+O(s).
\]

So cancellation cannot come from splitting \(A_o\). 

A cancellation from another source-index row would require a new identity of the form

\[
\sum_{\text{top rows}}
\lambda_a\nu_a
\left(
w_a I+u_a S
\right)=0.
\]

No current source symmetry or Sylvester recurrence forces this. The \(a=2\) row alone is already \(S\)-visible.

---

# 6. Result

The odd-\(\eta\eta\) top row is a concrete local obstruction.

\[
\boxed{
\mathcal E^2_{\eta\eta;7,0,0}
=
\lambda\nu_{\eta\eta,7}(wI+uS)
}
\]

with

\[
\lambda=-\frac1{24\pi q^3}.
\]

Generically,

\[
\boxed{
f_{A,Y}\supset
-\frac{u}{24\pi q^3}\nu_{\eta\eta,7}\neq0.
}
\]

Therefore,

\[
\boxed{
\partial_\kappa T\neq0
}
\]

unless one proves a new theorem:

\[
\boxed{
\nu_{\eta\eta,7}=0
}
\]

or a new fixed-sector cancellation theorem involving other top-row terms.

The endpoint-diagonal cleanup cannot affect this row, because this is a scalar \(\Delta\)-Hessian \(\eta\eta\) contribution, not an endpoint-separation artifact.
## User (2026-04-25 12:54:53)

continue your attack

## Assistant (2026-04-25 12:54:56)

I’ll continue by attacking the last two possible escape routes for the concrete row: a source-jet identity forcing \(\nu_{\eta\eta,7}=0\), or a baseline/quotient identity forcing the matrix factor to be \(S\)-invisible.

_Thought for 9s_

## Continued attack — can \(\nu_{\eta\eta,7}\) vanish by source-jet locking?

We are now focused on the concrete row

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right),
\]

where

\[
A_o=
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

The attached instruction identifies this exact odd-\(\eta\eta\) row as the current lead local obstruction, with \((a,r,g,b)=(2,0,7,0)\), and notes that it can produce \(f_{A,Y}\neq0\) unless a new cancellation theorem is proved. 

The previous attack showed the matrix factor is generically \(S\)-visible:

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\lambda\nu_{\eta\eta,7}(wI+uS),
\qquad
\lambda=-\frac1{24\pi q^3}.
\]

So the remaining possible escape is:

\[
\boxed{
\nu_{\eta\eta,7}=0.
}
\]

I now attack that condition directly.

---

# 1. Expansion of the scalar coefficient

Assume the favorable co-moving phase-gap form

\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+O(s^7),
\]

\[
\eta_j(s)=\alpha_j s^3+\beta_j s^5+O(s^7).
\]

The odd scalar multiplier has expansion

\[
A_o(s)
=
\frac{2q}{s}
+
\left(
\frac{q_2}{6}
-\frac{2q^3}{3}
\right)s
+
O(s^3),
\]

where

\[
q=q_0(m),
\qquad
q_2=q_0''(m).
\]

Therefore

\[
[A_o\eta_i\eta_j]_{s^7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-\frac{2q^3}{3}
\right)\alpha_i\alpha_j.
\]

So

\[
\boxed{
\nu_{\eta\eta,7}
=
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
C\alpha_i\alpha_j,
}
\]

where

\[
C:=\frac{q_2}{6}-\frac{2q^3}{3}.
\]

---

# 2. What would be required for universal vanishing?

Suppose the proof needs

\[
\nu_{\eta\eta,7}=0
\]

for all active source pairs \((i,j)\).

If \(\alpha_i,\alpha_j\neq0\), divide by \(\alpha_i\alpha_j\):

\[
2q\left(
\frac{\beta_j}{\alpha_j}
+
\frac{\beta_i}{\alpha_i}
\right)
+
C
=
0.
\]

For this to hold for all pairs, one must have

\[
\frac{\beta_i}{\alpha_i}=\rho
\]

independent of \(i\), and then

\[
4q\rho+C=0.
\]

Thus

\[
\boxed{
\beta_i
=
-\frac{C}{4q}\alpha_i
=
\left(
\frac{q^2}{6}
-
\frac{q_2}{24q}
\right)\alpha_i
\quad
\text{for every active source direction }i.
}
\]

This is a very strong source-jet locking law.

It says the \(s^5\)-coefficient of every active phase-gap source is forced by its \(s^3\)-coefficient and by the baseline phase jets \(q,q_2\).

---

# 3. Does affine removal imply this locking?

No.

Affine removal gives a lower-order vanishing condition, schematically

\[
\eta_i(s)=s^3V_i(s),
\]

or

\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+\cdots.
\]

It removes the affine and lower jet components. It does **not** impose the specific relation

\[
\beta_i
=
\left(
\frac{q^2}{6}
-
\frac{q_2}{24q}
\right)\alpha_i.
\]

Thus affine removal explains why the first possible scalar product starts at

\[
\eta_i\eta_j\sim s^6,
\]

but it does not kill the \(s^7\)-coefficient of

\[
A_o\eta_i\eta_j.
\]

So:

\[
\boxed{
\text{affine removal is too weak to force }\nu_{\eta\eta,7}=0.
}
\]

---

# 4. Does co-moving endpoint realization imply this locking?

No.

Co-moving endpoint realization says the source comes from one analytic field, so the phase-gap variation is odd:

\[
\eta_i(s)=\eta_i^{\rm field}(m+s/2)-\eta_i^{\rm field}(m-s/2).
\]

That gives an expansion

\[
\eta_i(s)
=
\eta_i'(m)s
+
\frac{\eta_i'''(m)}{24}s^3
+
\frac{\eta_i^{(5)}(m)}{1920}s^5
+\cdots.
\]

After affine removal, the lower terms are subtracted, leaving

\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+\cdots.
\]

But the fifth derivative of the source field is independent of the third derivative unless a differential equation or special source constraint is imposed.

So co-moving realization does **not** imply

\[
\beta_i
=
\left(
\frac{q^2}{6}
-
\frac{q_2}{24q}
\right)\alpha_i.
\]

Therefore:

\[
\boxed{
\text{co-moving realization does not force }\nu_{\eta\eta,7}=0.
}
\]

This matches the previous conclusion that endpoint-diagonal cleanup cannot kill the scalar \(\eta\eta\) obstruction. The latest consolidation explicitly says endpoint-diagonal cleanup is secondary and that the lead obstruction is now the odd-\(\eta\eta\) top row. 

---

# 5. Does the matrix factor force quotient closure?

The row gives

\[
e=\lambda\nu_{\eta\eta,7}w,
\qquad
f=\lambda\nu_{\eta\eta,7}u.
\]

Thus

\[
Q=e v_5-u_5f
=
\lambda\nu_{\eta\eta,7}(wv_5-u u_5).
\]

For quotient closure independent of \(\nu_{\eta\eta,7}\), one needs

\[
wv_5-u u_5=0.
\]

Equivalently,

\[
\boxed{
\frac{w}{u}=\frac{u_5}{v_5}.
}
\]

This would mean the first column / off-diagonal ratio of the baseline whitening matrix \(W_{+,0}\) is locked to the quotient-line direction \(A_5^{\mathfrak f}=u_5I+v_5S\).

No current structural theorem implies this.

In the diagonal case

\[
w=0,
\]

the condition becomes

\[
-u u_5=0.
\]

Since \(u\neq0\) on a nondegenerate whitening patch, quotient closure would require

\[
u_5=0.
\]

That is not generic.

So:

\[
\boxed{
\text{the matrix factor does not force quotient closure.}
}
\]

---

# 6. Does the matrix factor force \(T\)-horizontal closure?

The \(T\)-horizontal condition is

\[
f=0.
\]

For the row,

\[
f=\lambda\nu_{\eta\eta,7}u.
\]

On a good patch,

\[
\lambda\neq0,
\qquad
u\neq0.
\]

Therefore

\[
f=0
\quad\Longleftrightarrow\quad
\nu_{\eta\eta,7}=0.
\]

Thus no quotient-line or matrix alignment can save \(T\)-horizontal closure. The only options are:

\[
\nu_{\eta\eta,7}=0,
\]

or cancellation against another active row with opposite \(S\)-coefficient.

---

# 7. Can another top-row cancel the \(S\)-coefficient?

The top row has

\[
g=7,
\qquad
r=b=0.
\]

So there are no \(r,b\)-partition partners. Any cancellation must come from another source index or another top-row Hessian channel.

The lead row is the actual \(a=2\), \(\eta\eta_{\rm odd}\) contribution. The current consolidation already identifies this as a concrete surviving row and says no present theorem proves cancellation. 

A cancellation theorem would need the form

\[
\sum_{\text{top }\eta\eta\text{ rows}}
\lambda_a\nu_a u_a
=
0.
\]

Nothing in endpoint symmetry, affine removal, or Sylvester recurrences supplies this identity. It would be a new finite Fréchet coefficient theorem.

---

# 8. Formal countermodel satisfying all current reductions

Choose a good patch with

\[
q\neq0,
\qquad
u\neq0,
\qquad
c\neq0.
\]

Choose source coefficients

\[
\alpha_i=\alpha_j=1,
\qquad
\beta_i=\beta_j=0.
\]

Then

\[
\nu_{\eta\eta,7}
=
\frac{q_2}{6}
-\frac{2q^3}{3}.
\]

On a generic patch with

\[
q_2\neq4q^3,
\]

this is nonzero.

Then

\[
f=
-\frac{u}{24\pi q^3}
\left(
\frac{q_2}{6}
-\frac{2q^3}{3}
\right)
\neq0.
\]

So

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
\neq0.
\]

If additionally \(u_5\neq0\) and \(w=0\), then

\[
Q=-u_5f\neq0.
\]

Thus this row is both \(T\)-visible and quotient-visible on a generic patch.

---

# 9. The sharpened missing theorem

The local proof now requires one of the following very specific statements.

## Option A: source-jet locking

```latex id="03trvk"
\begin{theorem}[Odd-\(\eta\eta\) source-jet locking]
For every active source direction \(i\), after affine removal the scalar
phase-gap variation
\[
\eta_i(s)=\alpha_i s^3+\beta_i s^5+O(s^7)
\]
satisfies
\[
\beta_i
=
\left(
\frac{q^2}{6}
-
\frac{q_2}{24q}
\right)\alpha_i.
\]
Consequently
\[
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right]
=0.
\]
\end{theorem}
```

This seems implausibly strong and is not implied by affine removal or co-moving realization.

## Option B: top-row \(S\)-coefficient cancellation

```latex id="4m95k4"
\begin{theorem}[Odd-\(\eta\eta\) top-row \(S\)-cancellation]
For the full collection of active top-row odd-\(\eta\eta\) contributions,
\[
\sum_{\mathrm{top}\ \eta\eta}
f_{\eta\eta}^{\mathrm{top}}=0.
\]
Equivalently, the \(S\)-component of
\[
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right)
\]
vanishes after summing all active source indices.
\end{theorem}
```

This is now the more realistic missing local theorem.

## Option C: full top-row fixed-sector cancellation

```latex id="t9dn3e"
\begin{theorem}[Odd-\(\eta\eta\) top-row fixed-sector cancellation]
The full top-row odd-\(\eta\eta\) contribution satisfies
\[
\sum_{\mathrm{top}\ \eta\eta}
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{a,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right)=0.
\]
\end{theorem}
```

This would close both quotient and \(T\)-horizontal conditions.

---

# 10. Current final local status

The endpoint-diagonal/co-moving route is exhausted.

It does not kill the scalar odd-\(\eta\eta\) row.

The row survives unless the paper proves a new finite coefficient identity. The cleanest obstruction is:

\[
\boxed{
f_{\eta\eta}^{\mathrm{top}}
=
-\frac{u}{24\pi q^3}
\left[
2q(\alpha_i\beta_j+\beta_i\alpha_j)
+
\left(
\frac{q_2}{6}
-\frac{2q^3}{3}
\right)\alpha_i\alpha_j
\right].
}
\]

This is generically nonzero.

Therefore the local branch is blocked at a concrete top-row \(S\)-coefficient cancellation theorem, not at endpoint realization or parity bookkeeping.
## User (2026-04-25 13:47:00)

Do the local agent attack

## Assistant (2026-04-25 13:48:55)

_Thought for 1m 53s_

## Local attack — search for a missing correction cancelling \(\mathcal E^{2}_{\eta\eta;7,0,0}\)

I treated the row as a live defect, as instructed:

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

I looked for an existing cancellation mechanism in the corrected package: second-order phase-gap correction, connection correction, normalization, source-bidegree projection, quotient projection, or another top-row contribution. The result is negative.

\[
\boxed{
\text{Under the current package architecture, this row is not cancelled.}
}
\]

More precisely:

\[
\boxed{
\text{The current package cannot close Bottleneck C at this row unless a new correction term or new top-row identity is added.}
}
\]

The attached state identifies this row as the concrete local blocker: \(\mathcal E^{2}_{\eta\eta;7,0,0}\), with \(\Lambda^-_{2,0}=-(24\pi q^3)^{-1}E_{22}\), and with \(S\)-coefficient proportional to \(\nu_{21,7}\). It also records that \(\nu_{21,7}\) is nonzero even for the homogeneous source \(r(u)=u^2\) when \(q_0''=0\). 

---

# 1. The defect is not killed by \(\nu_{21,7}=0\)

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

Under the favorable phase-gap integral model, the current reduction gives

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

For the homogeneous source \(r(u)=u^2\), with \(q_0''=0\), this becomes

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]

so it is nonzero on a good patch with \(q_0\neq0\). Thus a scalar source-jet vanishing theorem

\[
\nu_{21,7}=0
\]

is false in the current model unless the source class is further restricted. 

---

# 2. The companion \(q_-\cos\Delta_0/s\) term does not cancel the sine term

The odd block is

\[
A_oJ,
\qquad
A_o=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_e\cos\Delta_0}{s}
\]

or equivalently with the relevant endpoint \(q_-\) in the row coefficient. The current reduction says the companion term does **not** cancel the sine term; near a good phase patch it reinforces it. In particular,

\[
A_o\sim \frac{2q_0}{s}+O(s).
\]

So there is no hidden cancellation inside the off-diagonal \(\eta\eta\) Hessian itself. 

---

# 3. \(\Lambda^-_{2,0}\) is not zero

The actual finite Fréchet source index is \(a=2\), and the row uses

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]

On a good patch with \(q\neq0\), this is nonzero. Therefore the same-point whitening slot does not remove the row. 

This also matters structurally: at the top row

\[
(g,r,b)=(7,0,0),
\]

there is no \(r+b\)-partition partner. Any cancellation must come from another source index or another top-row \(\eta\eta\) term, not from convolution/telescoping among \(r,b\)-pieces.

---

# 4. \(W_{+,0}\) does not force \(S\)-projection cancellation

With

\[
W_{+,0}=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix},
\]

and

\[
\Lambda^-_{2,0}
=
\lambda E_{22},
\qquad
\lambda=-\frac{1}{24\pi q^3},
\]

the matrix factor is

\[
\pi_{\mathfrak f}\operatorname{Sym}(\lambda E_{22}JW_{+,0})
=
\lambda w I+\lambda u S.
\]

So the row contributes

\[
e=\lambda\nu_{21,7}w,
\qquad
f=\lambda\nu_{21,7}u.
\]

On a nondegenerate whitening patch, \(u\neq0\). Hence

\[
f=
-\frac{u}{24\pi q^3}\nu_{21,7}
\]

is generically nonzero. This matches the current consolidated row computation. 

Thus \(W_{+,0}\) and \(\Lambda^-_{2,0}\) do not force

\[
f_{A,Y}=0.
\]

They also do not force quotient closure:

\[
Q=e v_5-u_5f
=
\lambda\nu_{21,7}(wv_5-u u_5).
\]

For diagonal \(W_{+,0}\), \(w=0\), so

\[
Q=-u_5f.
\]

On a generic \(u_5\neq0\) patch, this is nonzero.

---

# 5. Source-bidegree projection does not remove it

The row comes from the promoted quadratic mixed-block Hessian \(Y_{12}^{(2)}\) coupled to one same-point linear whitening slot. Its amplitude factor is

\[
a_1a_2(a_1+a_2).
\]

This is exactly the pattern that supplies the Bottleneck-C \(\delta\)-edge under

\[
a_2=-a_1(1+\kappa\delta).
\]

It is not the removed \((1,1)\) sector. The attached state emphasizes that the frozen coefficient is the active Bottleneck-C carrier and that the internal \([z^7\delta^1]\) coefficient is a later source-motion layer, not the first amplitude-ratio carrier. 

So source-bidegree projection cannot be the missing cancellation.

---

# 6. Connection correction cannot cancel this raw local defect

A connection correction or moving-line correction acts after one has a quotient-level package and a moving quotient line. This row is earlier: it is a raw frozen Bottleneck-C carrier that affects both

\[
Q_{A,Y}=e v_5-u_5f
\]

and the augmented hidden coordinate through

\[
\partial_\kappa T=-a_1^2\frac{f}{c}.
\]

Even if a connection correction could move something along the \(A_5^{\mathfrak f}\)-line, it would not generally kill the \(T\)-visible \(S\)-component. The current state distinguishes quotient closure from the transform-safe condition \(f_{A,Y}=0\). 

Therefore connection correction is not a valid cancellation for this row unless a new correction is explicitly inserted at the raw corrected-whitening level.

---

# 7. Amplitude normalization cannot cancel it

Amplitude normalization rescales the edge contribution. It does not add an opposite \(\eta\eta\) Hessian term.

The row exists precisely because

\[
a_1a_2(a_1+a_2)
=
a_1^3\kappa\delta+O(\delta^2)
\]

turns the frozen coefficient into the Bottleneck-C slope. Normalization exposes the row; it does not cancel it. 

---

# 8. A possible correction term would have to be new and explicit

To cancel the row at the raw local level, one would need an added second-order correction whose top-row contribution is exactly

\[
-\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_7
W_{+,0}
\right).
\]

Equivalently, at the mixed-block level, one would need a counterterm of the form

\[
\Delta N^{\rm ct}_{\eta\eta}
=
- A_oJ\,\eta_i\eta_j
\]

in the relevant odd-background off-diagonal channel, with the correct endpoint-transpose covariance and no collateral damage to lower gates.

But this is not present in the current corrected block

\[
N^{\corr}(q_-,q_+,\Delta;s).
\]

It would also be mathematically nontrivial: it changes the actual second \(\Delta\)-Hessian of the sine kernel. Such a correction would need a new principle, for example a redefined phase-gap coordinate, a second-order normal-coordinate correction, or a new source-bidegree-compatible edge counterterm. None of those is currently part of the package.

---

# 9. Formal obstruction theorem

Under the current package, assume the good-patch conditions

\[
q\neq0,\qquad u\neq0,\qquad c\neq0,
\]

and assume the homogeneous source row with

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}\neq0.
\]

Then

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}
\neq0.
\]

Therefore

\[
\partial_\kappa T
=
-a_1^2\frac{f_{\eta\eta}^{\rm top}}{c}
\neq0.
\]

If additionally \(u_5\neq0\) and \(W_{+,0}\) is diagonal or has no special quotient-line alignment, then

\[
Q_{A,Y}=e v_5-u_5f\neq0.
\]

So the current corrected package fails to prove both:

\[
f_{A,Y}=0,
\]

and, generically,

\[
Q_{A,Y}=0.
\]

---

# 10. Deliverable: no existing correction; exact missing correction theorem

I do not find an existing correction mechanism in the current package that cancels the row. The proof now needs one of the following.

## Option A: explicit new counterterm

```latex
\begin{theorem}[Odd-\(\eta\eta\) edge counterterm]
The corrected mixed block includes a source-bidegree-compatible second-order
edge counterterm \(N^{\rm ct}_{\eta\eta}\) whose top-row contribution satisfies
\[
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[N^{\rm ct}_{\eta\eta}]_{7}
W_{+,0}
\right)
=
-
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_{7}
W_{+,0}
\right).
\]
\end{theorem}
```

## Option B: full top-row cancellation identity

```latex
\begin{theorem}[Odd-\(\eta\eta\) top-row cancellation]
The full active top-row odd-\(\eta\eta\) contribution satisfies
\[
\sum_{\mathrm{top}\ \eta\eta}
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{a,0}
[A_oJ\eta_i\eta_j]_{7}
W_{+,0}
\right)
=0.
\]
\end{theorem}
```

## Option C: hidden-coordinate-safe cancellation

```latex
\begin{theorem}[Odd-\(\eta\eta\) \(T\)-safe cancellation]
The full active top-row odd-\(\eta\eta\) contribution has zero \(S\)-component:
\[
\sum_{\mathrm{top}\ \eta\eta} f_{\eta\eta}^{\mathrm{top}}=0.
\]
\end{theorem}
```

Option C is the minimum needed for the augmented \(T\)-horizontal condition. Option B is needed for full fixed-sector vanishing. Option A is the only route if no identity among existing rows exists.

---

# Final local verdict

\[
\boxed{
\text{The current corrected package cannot close Bottleneck C at the odd-\(\eta\eta\) top row.}
}
\]

The obstruction is concrete:

\[
\boxed{
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7},
\qquad
\nu_{21,7}\neq0
\text{ generically.}
}
\]

Thus the proof requires either a new correction package or a new finite top-row cancellation identity.
## User (2026-04-25 13:52:18)

Do the local package-design agent instruction

## Assistant (2026-04-25 13:52:19)

I’ll treat this as the local package-design attack: assume the row is a real defect and ask whether a principled correction package can cancel it without invalidating the already-closed local gates.

_Thought for 1m 34s_

## Local package-design attack — can we add a principled counterterm?

### Verdict

\[
\boxed{
\text{I do not find a principled modification of the current corrected package that cancels }
\mathcal E^{2}_{\eta\eta;7,0,0}
\text{ without adding new collateral terms.}
}
\]

The only correction that definitely cancels the row is an explicit matrix counterterm in the \(\eta\eta\) odd off-diagonal channel. But that counterterm is not generated by the current \(N^{\corr}(q_-,q_+,\Delta;s)\), by source-bidegree projection, by amplitude normalization, by midpoint trivialization, or by a harmless phase-coordinate change.

So the package-design result is negative:

\[
\boxed{
\text{The current package cannot close Bottleneck C at this row without a new correction principle.}
}
\]

The attached consolidation states the current local defect precisely: the row \(\mathcal E^{2}_{\eta\eta;7,0,0}\) has

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7},
\]

and for the homogeneous source \(r(u)=u^2\), \(q_0''=0\),

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]

which is nonzero on a good phase patch. It also records that the current package mechanisms do not cancel this row. 

---

# 1. The live defect

The row is

\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[A_oJ\eta_i\eta_j]_{7}
W_{+,0}
\right),
\]

with

\[
A_o
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s},
\]

and

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

The actual Fréchet coefficient is

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]

With

\[
W_{+,0}=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix},
\]

the row contributes

\[
\pi_{\mathfrak f}\operatorname{Sym}
(\Lambda^-_{2,0}J W_{+,0})
=
-\frac{1}{24\pi q^3}(wI+uS).
\]

Thus

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

On a good patch,

\[
u\ne0,\qquad q\ne0,
\]

so the only ways out are:

\[
\nu_{21,7}=0,
\]

or cancellation by another row/counterterm.

But \(\nu_{21,7}=0\) is false generically. In particular, the homogeneous source example gives a nonzero value.

---

# 2. Candidate correction 1: source-jet identity

One could try to impose

\[
\nu_{21,7}=0.
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
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]

To force this for all active sources, one needs a rigid relation between the second and fourth source jets:

\[
\rho_{i,4}
=
\Gamma(q_0,q_0'')\rho_{i,2}
\]

with exactly the coefficient needed to cancel the baseline term.

But affine removal only kills lower affine data. It does not lock the fourth source jet to the second source jet. Endpoint symmetry and source-grade parity also do not impose this relation.

Worse, the homogeneous source \(r(u)=u^2\) with \(q_0''=0\) gives

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}\ne0.
\]

So the source-jet identity route is not viable unless the admissible source class is changed.

---

# 3. Candidate correction 2: nonlinear phase-gap coordinate

Try a nonlinear phase coordinate

\[
\widehat \Delta
=
\Delta+\frac12\Gamma(s)(\Delta-\Delta_0)^2.
\]

Then the Hessian changes by

\[
\partial_\Delta^2N_0[\eta_i,\eta_j]
\quad\mapsto\quad
\partial_\Delta^2N_0[\eta_i,\eta_j]
+
\partial_\Delta N_0\,
\Gamma(s)\eta_i\eta_j.
\]

So one might try to choose \(\Gamma(s)\) to cancel the odd \(\eta\eta\) row.

This does **not** work cleanly.

The off-diagonal derivative has the form

\[
\partial_\Delta N_{21}
=
-\frac{\cos\Delta_0-q_-s\sin\Delta_0}{s^2},
\]

while the \((2,2)\)-entry has a stronger singular contribution:

\[
\partial_\Delta N_{22}
=
\frac{-(q_-+q_+)s\sin\Delta_0+(2-q_-q_+s^2)\cos\Delta_0}{2s^3}.
\]

To cancel the top row, \(\Gamma(s)\) must contain low odd powers. Schematically:

\[
\Gamma(s)=\gamma_1s+\gamma_3s^3+\cdots.
\]

The \(\gamma_1s\) term is needed to cancel the part of \(\nu_{21,7}\) involving mixed source jets like \(\rho_{i,2}\rho_{j,4}+\rho_{i,4}\rho_{j,2}\).

But then

\[
\partial_\Delta N_{21}\Gamma(s)\eta_i\eta_j
\]

also creates lower \(s^5\) terms, and

\[
\partial_\Delta N_{22}\Gamma(s)\eta_i\eta_j
\]

creates even lower diagonal terms because \(\partial_\Delta N_{22}\sim s^{-3}\).

Thus a scalar phase-coordinate correction cannot selectively cancel the \(g=7\), \((2,1)\)-off-diagonal \(J\)-row. It introduces collateral lower-order and diagonal contributions that would have to be cancelled separately.

Therefore a phase-gap reparametrization is not a harmless package repair.

---

# 4. Candidate correction 3: connection/covariant Hessian

A more invariant version of the previous idea is to replace the ordinary Hessian by a covariant Hessian:

\[
D^2N_0[\xi_i,\xi_j]
\quad\leadsto\quad
D^2N_0[\xi_i,\xi_j]
+
DN_0[\Gamma(\xi_i,\xi_j)].
\]

If \(\Gamma\) has only a phase-gap component, this is exactly the same obstruction as the nonlinear \(\Delta\)-coordinate change.

It cannot cancel the isolated \(A_oJ\eta_i\eta_j\) top row without also generating unwanted terms through \(\partial_\Delta N_{22}\) and through lower orders.

If \(\Gamma\) is allowed to be matrix-valued or to depend on the target fixed-sector projection, then it can be tuned to cancel the row. But then it is no longer a coordinate connection on the source variables; it is an explicit edge counterterm.

So a covariant-Hessian repair is only principled if the paper adds a canonical connection whose full set of collateral terms is proved harmless. No such connection is currently present.

---

# 5. Candidate correction 4: explicit edge counterterm

The direct counterterm would be

\[
N^{\rm ct}_{\eta\eta}
=
- A_oJ\,\eta_i\eta_j
\]

in the odd \(\eta\eta\) off-diagonal channel, at the relevant source bidegree.

This would cancel the row by construction:

\[
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
[N^{\rm ct}_{\eta\eta}]_7
W_{+,0}
\right)
=
-
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]

But this is not a derived correction. It changes the actual second \(\Delta\)-Hessian of the sine-kernel mixed block.

To be acceptable, the proof would need a new principle saying that the corrected package is allowed to subtract the odd \(\eta\eta\) off-diagonal Hessian while preserving:

\[
N^{\corr}(h_-,h_+)^T=N^{\corr}(h_+,h_-),
\]

Gate A closure,

Gate B homogeneous-tower closure,

the \(M_A,M_C\) connection closure,

and the augmented \(T\)-package interpretation.

That is a substantial new package definition, not a consequence of the existing one.

---

# 6. Candidate correction 5: projection / quotient / connection

These do not solve the problem.

## Source-bidegree projection

The amplitude pattern is the promoted degree-three edge pattern

\[
a_1a_2(a_1+a_2),
\]

which is exactly the Bottleneck-C slope carrier. Projection does not remove it.

## Amplitude normalization

This rescales the row; it does not add an opposite \(\eta\eta\) Hessian.

## Midpoint trivialization

On a good patch, this is invertible. It cannot turn a nonzero \(S\)-component into zero.

## Quotienting

Quotienting can only kill line-gauge components. The augmented package requires the actual \(S\)-component to vanish:

\[
f_{A,Y}=0.
\]

This row has

\[
f_{\eta\eta}^{\rm top}\neq0
\]

generically.

## Connection correction

Connection correction is post-edge. The row is a raw frozen Bottleneck-C carrier. It affects the hidden \(T\)-coordinate:

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}.
\]

A post-edge quotient-line correction cannot erase this unless the package is redefined to include a new raw counterterm.

---

# 7. Package-design conclusion

There is no harmless local package tweak.

The options are:

## Option A — restrict the source class

Impose a source-jet locking theorem forcing

\[
\nu_{21,7}=0.
\]

But this is contradicted by the homogeneous source model unless that source is declared inadmissible.

## Option B — add an explicit counterterm

Add

\[
N^{\rm ct}_{\eta\eta}
=
- A_oJ\,\eta_i\eta_j
\]

or a finite-order top-row variant of it.

This cancels the row but changes the corrected mixed block and requires a new justification.

## Option C — introduce a canonical covariant source connection

Define a source connection \(\Gamma\) such that

\[
D^2_{\Gamma}N
=
D^2N+DN[\Gamma]
\]

has no odd \(\eta\eta\) top-row \(S\)-component.

But the connection must also cancel all collateral lower-order and diagonal contributions. The current draft has no such construction.

---

# 8. The exact theorem the package now needs

The clean theorem would be:

```latex id="73sz99"
\begin{theorem}[Odd-\(\eta\eta\) package correction]
The corrected mixed block used in the Bottleneck-C package is not the raw
second \(\Delta\)-Hessian of
\[
N^{\corr}(q_-,q_+,\Delta;s),
\]
but the renormalized Hessian
\[
D^2_{\mathrm{pkg}}N_0[\xi_i,\xi_j]
=
D^2N_0[\xi_i,\xi_j]+C_{\eta\eta}^{\mathrm{pkg}}[\xi_i,\xi_j],
\]
where the package correction satisfies
\[
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
C_{\eta\eta}^{\mathrm{pkg}}[\xi_i,\xi_j]
+
A_oJ\,\eta_i\eta_j
\right]_7
W_{+,0}
\right)=0.
\]
Moreover \(C_{\eta\eta}^{\mathrm{pkg}}\) is endpoint-transpose covariant,
source-bidegree compatible, and produces no new order-\(\le7\) raw edge
defects in Gate A, Gate B, or the \(M_A,M_C\) connection package.
\end{theorem}
```

Without such a theorem, the local package fails at the concrete row.

---

# 9. Final verdict

\[
\boxed{
\text{The existing corrected package cannot close the local Bottleneck-C branch.}
}
\]

The obstruction is not bookkeeping. It is the actual second phase-gap Hessian of the corrected mixed block:

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}.
}
\]

The only plausible repair is a new, explicitly justified second-order \(\eta\eta\) package correction. A scalar phase-coordinate reparametrization or existing quotient/connection machinery does not cancel the row without creating additional obligations.
## User (2026-04-25 15:33:24)

Here is the latest paper draft. Please review and ensure we've captured everything in your push, including key structural findings, derivations, goodies, negative results and no-gos, etc. Please also check for any stale items. Please give exact latex insertions/edits and exactly where to make them.

## Assistant (2026-04-25 15:33:26)

I’ll review the latest TeX for whether the local package-design findings are already present, stale, or missing. I’ll focus on substantive mathematical edits: the odd-\(\eta\eta\) top row, endpoint-separation cleanup, and the no-go around existing package mechanisms.

The draft already contains a substantial amount of the latest audit material: the frozen \(E_{A,Y}^{\mathrm{BC}}\) correction, the \(\Theta_\pm\) no-go, the finite-core non-concentration dependency, and the \(dd\)-interaction feature-balance obstruction. The remaining issue is mostly stale emphasis: the draft still presents the broad \(E_{A,Y}^{\mathrm{BC}}\) table as the live local task, while the latest push has narrowed the live local blocker to the explicit odd-\(\eta\eta\) top row.

_Thought for 1m 45s_

I reviewed `proof_of_rh(446).tex`. Most of the push is already captured: the frozen \(E_{A,Y}^{\mathrm{BC}}\) bookkeeping correction, the \(T=v_7/c\) augmented package, the \(\Theta_\pm\)-normal-form no-go, finite-core sampled vector non-concentration, and \(dd\)-interaction feature-balance are all present.

The main missing/stale point is that the draft still frames the local problem as the broad finite \(E_{A,Y}^{\mathrm{BC}}\) table. The latest local push has narrowed this to the concrete odd-\(\eta\eta\) top row
\[
\mathcal E^{2}_{\eta\eta;7,0,0},
\]
with explicit \(S\)-visible coefficient. The draft should record that sharper obstruction and update the stale source-index notation \(\{1,5\}\). This is not a cosmetic issue: the latest result says the current package fails locally unless \(\nu_{21,7}=0\), a full top-row \(S\)-cancellation holds, or a new second-order phase-gap correction is added. turn80file6

---

## Edit 1 — fix stale source-index notation in the executable table

**Where:** In `remark`:

```latex
\begin{remark}[Executable table for \(E_{A,Y}^{\mathrm{BC}}\) (current section)]
\label{rem:executable-table-eay-bc-current}
```

**Replace this block:**

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
a\in\mathcal A_{\lin},
\qquad
\chi\in\{dd,d\eta+\eta d,\eta\eta\}.
\]
Here \(\mathcal A_{\lin}\) denotes the active same-point source-linear
Fréchet index set in the finite coefficient table.  Earlier audit notation
used \(a\in\{1,5\}\), but the concrete odd-\(\eta\eta\) top-row obstruction
uses the actual finite Fréchet index \(a=2\).  The index convention must
therefore be read from the finite Fréchet table, not from the older shorthand.
```

**Also replace later in the same remark:**

```latex
\sum_{a\in\{1,5\}}
```

**with:**

```latex
\sum_{a\in\mathcal A_{\lin}}
```

This removes a stale convention. The recent audits explicitly warn that the current concrete row uses \(a=2\), not the older \(\{1,5\}\) shorthand. turn80file6

---

## Edit 2 — revise the “Status of \(E_{A,Y}^{\mathrm{BC}}\)” remark

**Where:** In:

```latex
\begin{remark}[Status of the frozen promoted mixed-block coefficient (current section)]
\label{rem:status-eay-bc-current}
```

**Replace the final paragraph beginning:**

```latex
At present no available symmetry forces
...
Thus \(E_{A,Y}^{\mathrm{BC}}\) remains the first unresolved local
actual-source/Bottleneck~C coefficient.
```

**with:**

```latex
The latest local audit sharpens this further.  The obstruction is no longer
merely the broad finite table.  The first concrete surviving candidate is the
odd-background scalar \(\eta\eta\) top row
\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]
It arises from the off-diagonal \(\Delta\)-Hessian of the corrected mixed block
and is governed by
\[
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)
\eta_i\eta_j
\right]_{7}
W_{+,0}.
\]
With
\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]
this row has \(S\)-coefficient
\[
f_{\eta\eta}^{\top}
=
-\frac{u}{24\pi q^3}\nu_{21,7},
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
Thus the local branch is presently blocked by this explicit top-row scalar,
not merely by an unevaluated \(60\)-row table.  At present no available
symmetry forces
\[
\nu_{21,7}=0,
\qquad
e_{A,Y}v_5-u_5f_{A,Y}=0,
\qquad
\text{or}
\qquad
f_{A,Y}=0.
\]
Consequently the local proof now requires either a source-jet identity forcing
\(\nu_{21,7}=0\), a full top-row \(S\)-cancellation after summing all active
rows, or a new second-order phase-gap correction/counterterm.
```

This brings the status remark up to the latest local result.

---

## Edit 3 — insert a concrete odd-\(\eta\eta\) top-row obstruction subsection

**Where:** Insert immediately after:

```latex
\begin{remark}[\(\Theta_\pm\) no-go versus the frozen Bottleneck-C coefficient]
\label{rem:theta-nogo-versus-frozen-bc-coefficient}
...
\end{remark}
```

and before:

```latex
\subsection{Finite-core sampled vector non-concentration}
```

**Insert:**

```latex
\subsection{Concrete odd-\(\eta\eta\) top-row obstruction}
\label{subsec:concrete-odd-etaeta-top-row-obstruction}

The local package audits isolate a concrete top-row survivor inside the frozen
Bottleneck~C coefficient.  The relevant row is
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
J\,\eta_i\eta_j
\right]_{7}
W_{+,0}
\right),
\]
where
\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
This is the actual finite Fréchet source index \(a=2\), not the older
shorthand \(a\in\{1,5\}\).

The row comes from the \((2,1)\)-off-diagonal entry
\[
N_{21}
=
-\frac{\sin\Delta+q_-s\cos\Delta}{s^2}.
\]
Twice differentiating in the scalar phase-gap variable \(\Delta\) gives
\[
\partial_\Delta^2N_{21}\big|_0
=
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}.
\]
Thus the odd-background \(\eta\eta\) block is not an endpoint-separation
artifact.  It is a scalar \(\Delta\)-Hessian term.

For the active finite Fréchet row one has
\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22}.
\]
If
\[
W_{+,0}
=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix},
\]
then
\[
\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,0}JW_{+,0}
\right)
=
-\frac{1}{24\pi q^3}(wI+uS).
\]
Consequently, if
\[
\nu_{21,7}
:=
[z^7]\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)\eta_i\eta_j
\right],
\]
then this row contributes
\[
\mathcal E^{2}_{\eta\eta;7,0,0}
=
-\frac{\nu_{21,7}}{24\pi q^3}(wI+uS),
\]
up to the harmless good-patch transport \(\tau_{h\to m}\).  In particular,
\[
f_{\eta\eta}^{\top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
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
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]
For the homogeneous source \(r(u)=u^2\), with \(q_0''=0\), this gives
\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}},
\]
which is nonzero on a good phase patch.

Therefore the row is generically \(T\)-visible:
\[
\partial_\kappa T
=
-a_1^2\frac{f_{\eta\eta}^{\top}}{c}
\ne0.
\]
It is also quotient-visible on a generic \(u_5\ne0\) patch; for example, if
\(w=0\), then
\[
Q_{\eta\eta}^{\top}
=
-u_5 f_{\eta\eta}^{\top}.
\]

\begin{remark}[Endpoint cleanup does not remove this row]
Endpoint-diagonal realization, if proved, removes only endpoint-separation
subchannels such as
\[
d\eta^\Delta+\eta^\Delta d,
\qquad
\eta^\Sigma\eta^\Delta.
\]
It does not remove the scalar \(\eta\eta\) term above, since that term comes
from \(\partial_\Delta^2N_0[\eta_i,\eta_j]\).  Thus the older route
\[
[\delta^0]\eta^\Delta=0
\quad\Longrightarrow\quad
E_{A,Y}^{\mathrm{BC}}=0
\]
is no longer sufficient.
\end{remark}

\begin{remark}[No existing package mechanism cancels the row]
The present package mechanisms do not cancel
\(\mathcal E^{2}_{\eta\eta;7,0,0}\):
source-bidegree projection does not remove the promoted degree-three amplitude
pattern \(a_1a_2(a_1+a_2)\); amplitude normalization only rescales the row;
midpoint trivialization is invertible on a good patch; connection correction is
post-edge and cannot cancel a raw frozen coefficient; and quotienting is
insufficient because the augmented transform-safe package requires the
\(S\)-component itself to vanish.
\end{remark}

Thus the local branch is in the following binary state.  Either one proves a
new source-jet identity
\[
\nu_{21,7}=0,
\]
or one proves a full top-row \(S\)-cancellation
\[
\sum_{\mathrm{top}\ \eta\eta} f_{\eta\eta}^{\top}=0,
\]
or one adds a new second-order phase-gap correction/counterterm cancelling this
row.  Without one of these inputs, the current corrected package does not close
Bottleneck~C or the \(T\)-horizontal condition at this row.
```

This is the highest-value missing insertion. It records the concrete coefficient, the homogeneous-source nonzero check, and the no-go for existing package mechanisms.

---

## Edit 4 — make the \(\Theta_\pm\) no-go explicitly subordinate to the row

The current \(\Theta_\pm\) section is good, but it should not obscure the concrete row. Add this sentence at the **end** of:

```latex
\begin{remark}[\(\Theta_\pm\) no-go versus the frozen Bottleneck-C coefficient]
\label{rem:theta-nogo-versus-frozen-bc-coefficient}
```

**Add before `\end{remark}`:**

```latex
In particular, the concrete obstruction recorded in
Subsection~\ref{subsec:concrete-odd-etaeta-top-row-obstruction} is not removed
by changing to \(\Theta_\pm\)-normal variables.  The normal variables may move
the term between formal package coordinates and the physical hidden coordinate,
but they do not prove the required physical condition \(f_{A,Y}=0\).
```

This ties the no-go to the concrete row and prevents a stale reading that \(\Theta_\pm\) “solves” the local issue.

---

## Edit 5 — add a finite-core bad-branch definition in the finite-core subsection

The draft already has `Hypothesis~\ref{hyp:sampled-finite-core-vector-nonconcentration}` and `Definition~\ref{def:interaction-aligned-finite-core-branch}`. That captures most of the latest finite-core push. I would add one short remark after:

```latex
\begin{remark}[Status of the finite-core branch]
\label{rem:status-finite-core-branch-current}
...
\end{remark}
```

**Insert:**

```latex
\begin{remark}[Why sampled non-concentration is a pointwise input]
\label{rem:sampled-nonconcentration-is-pointwise-input}
The sampled vector non-concentration hypothesis is not a consequence of
finite determinacy, compactness, pairwise zero-spacing, endpoint-gap control,
or Remez--{\L}ojasiewicz volume estimates.  Those tools control qualitative
vanishing, boundary/collision behavior, or small-value volume.  The proof
requires a pointwise exclusion for the actual zeta sample
\(\theta(m)\):
\[
\theta(m)\notin\mathcal Z_k\cup\mathcal E_{\rm geom}
\quad\Longrightarrow\quad
\|P_{\rm fd}(\theta(m))+J_{\rm fd}(\theta(m))\|_\infty
\ge \Lambda(m,Q).
\]
Equivalently, the unresolved branch is the interaction-aligned radial
smallness set
\[
\mathcal N_k^{\rm align}(m,Q).
\]
\end{remark}
```

The latest finite-core result is already well represented; this just clarifies that it is a pointwise dependency rather than something supplied by existing compactness/determinacy tools. 

---

## Edit 6 — add the concrete \(k=3\) centered-kernel spectral test

The current `dd`-interaction section records the feature-balance obstruction and possible spectral route. It does **not** yet capture the concrete \(k=3\) obstruction \(A\ge B/4\), nor the transported-covariance coefficient test. Add both.

**Where:** After:

```latex
\begin{remark}[Needed input for the \(dd\)-interaction branch]
\label{rem:feature-balance-or-spectral-positivity-dd-needed}
...
\end{remark}
```

**Insert:**

```latex
\begin{remark}[Concrete \(k=3\) centered-kernel test]
\label{rem:concrete-k3-centered-kernel-test}
Even under the favorable separation-kernel reduction
\[
\mathfrak j_{ij}^{dd}=K_{dd}(u_i-u_j;m),
\qquad
K_{dd}(t)=K_{dd}(-t),
\qquad
K_{dd}(0)=0,
\]
conditional one-sidedness is a nontrivial spectral constraint.  For
\[
u=(-1,0,1),
\]
set
\[
A=K_{dd}(1;m),
\qquad
B=K_{dd}(2;m).
\]
For a balanced vector \(a=(x,y,-x-y)\), the quadratic form has the model shape
\[
J_{dd}
=
-Bx^2-Bxy-Ay^2.
\]
Thus, in the real negative-type convention, the centered form is one-sided only
if
\[
B\ge0,
\qquad
A\ge0,
\qquad
A\ge \frac{B}{4},
\]
up to the chosen phase/sign convention.  Evenness, analyticity, collision
divisibility, same-scale compactness, and pair-like positivity do not imply
this inequality.  The signature-changing locus
\[
K_{dd}(1;m)=\frac14K_{dd}(2;m)
\]
is not presently among the controlled incidence equations.
\end{remark}

\begin{remark}[Transported covariance coefficient obstruction]
\label{rem:transported-covariance-coefficient-obstruction}
If the \(dd\)-kernel has the transported covariance form
\[
K_{dd}(t;m)
=
t^2
\left\langle
v\!\left(m+\frac t2\right),
v\!\left(m-\frac t2\right)
\right\rangle,
\]
then the first nonquadratic coefficient is
\[
\kappa_4
=
\frac14
\left(
\langle v_0,v_2\rangle-\langle v_1,v_1\rangle
\right),
\]
where \(v_j\) denotes the \(j\)-th local coefficient of the transported
feature.  A conditionally one-sided representation would require, after phase
rotation, the appropriate alternating sign pattern for this coefficient and all
higher nonquadratic coefficients.  The current source geometry does not prove
that spectral-measure condition.
\end{remark}
```

This captures the interaction “goodies” from the latest push: the \(A\ge B/4\) test and the \(\kappa_4\) obstruction. 

---

## Edit 7 — update the final frontier remark

**Where:** In:

```latex
\begin{remark}[Current proof frontier after the local package audits]
\label{rem:current-proof-frontier-after-local-package-audits}
```

**Replace item 2:**

```latex
\item The promoted quadratic mixed-block Bottleneck~C coefficient
\[
E_{A,Y}^{\mathrm{BC}}
\]
is the first unresolved local actual-source coefficient.  The quotient test is
...
```

**with:**

```latex
\item The promoted quadratic mixed-block Bottleneck~C coefficient
\[
E_{A,Y}^{\mathrm{BC}}
\]
has been sharpened to the concrete odd-\(\eta\eta\) top-row obstruction
\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]
The row has generically nonzero \(S\)-coefficient
\[
f_{\eta\eta}^{\top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]
Thus the local branch now requires one of:
\[
\nu_{21,7}=0,
\qquad
\sum_{\mathrm{top}\ \eta\eta}f_{\eta\eta}^{\top}=0,
\]
or a new source-bidegree-compatible second-order phase-gap correction.
The quotient test is
\[
e_{A,Y}v_5-u_5f_{A,Y}=0,
\]
and the transform-safe test is
\[
f_{A,Y}=0.
\]
```

This makes the final proof-state ledger match the latest local conclusion.

---

## Items already captured well

No further edit is needed for these unless you want more verbosity:

1. **\(M_A,M_C\) connection closure** is captured as closed under source-grade reflection.
2. **Mixed four-point dependency-only status** is captured.
3. **Finite determinacy qualitative theorem** is captured as done.
4. **Augmented package \((\widehat\Psi_{\rm red},T)\)** is captured.
5. **\(\Theta_\pm\)-normal repair no-go** is captured and is a useful package-design negative result.

---

## One caution

The draft currently contains both older broad-table language and newer \(\Theta_\pm\) no-go language. After the insertions above, the local story should read as:

\[
E_{A,Y}^{\mathrm{BC}}
\quad\leadsto\quad
\mathcal E^{2}_{\eta\eta;7,0,0}
\quad\leadsto\quad
\nu_{21,7}\neq0\text{ generically}
\quad\leadsto\quad
\text{need new identity/counterterm.}
\]

That is the correct latest local proof state.
## User (2026-04-25 15:52:38)

You are Local Agent B. Attached the latest paper draft, plus a background summary and the next attack instructions--do your attack.

## Assistant (2026-04-25 15:53:09)

_Thought for 30s_

## Local Agent B — source-jet identity route for \(\nu_{21,7}=0\)

### Verdict

\[
\boxed{
\text{The current draft does not force }\nu_{21,7}=0.
}
\]

More strongly, under the currently stated admissibility/normalization data, the homogeneous source test

\[
r_i(u)=r_j(u)=u^2,\qquad q_0''=0
\]

is not excluded, and it gives

\[
\boxed{
\nu_{21,7}=-\frac{q_0^3}{216Q^{14}}\neq0
}
\]

on a good phase patch. This directly refutes a universal source-jet identity \(\nu_{21,7}=0\). The attached background explicitly identifies this homogeneous test as surviving affine removal, endpoint symmetry, source-grade parity, frozen Bottleneck-C bookkeeping, and the actual \(a=2,r=0\) Fréchet row. turn83file9

---

# 1. The coefficient under attack

The lead local obstruction is

\[
\mathcal E^{2}_{\eta\eta;7,0,0},
\]

with

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

The coefficient is

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

In the favorable phase-gap integral model,

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
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
\rho_{i,2}\rho_{j,2}
\right].
\]

This is the exact source-jet identity target requested for Local Agent B. 

---

# 2. What identity would be required?

Assume \(\rho_{i,2}\rho_{j,2}\neq0\). Set

\[
\lambda_i:=\frac{\rho_{i,4}}{\rho_{i,2}},
\qquad
\lambda_j:=\frac{\rho_{j,4}}{\rho_{j,2}}.
\]

Then \(\nu_{21,7}=0\) is equivalent to

\[
\frac{q_0}{480}(\lambda_i+\lambda_j)
+
\frac{1}{144}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
=0.
\]

Equivalently,

\[
\lambda_i+\lambda_j
=
-\frac{480}{144q_0}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
=
-\frac{10}{3q_0}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right).
\]

For this to hold for **all** active source pairs \((i,j)\), all active sources must have a common ratio

\[
\lambda_i=\lambda_\star,
\]

and that ratio must satisfy

\[
2\lambda_\star
=
-\frac{10}{3q_0}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right).
\]

So the required source-jet locking law is

\[
\boxed{
\frac{\rho_{i,4}}{\rho_{i,2}}
=
-\frac{5}{3q_0}
\left(
\frac{q_0''}{6}
-
\frac{2q_0^3}{3}
\right)
=
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}
}
\]

for every active source direction \(i\).

That is a very strong fourth-jet/second-jet locking condition.

---

# 3. Existing normalizations do not imply this

The known mechanisms do not impose the required ratio:

\[
\frac{\rho_{i,4}}{\rho_{i,2}}
=
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}.
\]

Specifically:

- **Affine removal** removes low affine data; it does not lock the fourth source jet to the second source jet.
- **Endpoint symmetry / source-grade parity** controls parity/sign behavior; it does not impose a numerical relation between \(\rho_{i,2}\) and \(\rho_{i,4}\).
- **Frozen Bottleneck-C bookkeeping** identifies the correct coefficient; it does not add a source-jet equation.
- **The actual \(a=2,r=0\) Fréchet row** is active and nonzero, not removed by the package.

The attached summaries explicitly say the row survives these mechanisms and that the current local proof now requires either \(\nu_{21,7}=0\), aggregate top-row \(S\)-cancellation, or a new correction package. turn83file2

---

# 4. Homogeneous source test

For

\[
r_i(u)=r_j(u)=u^2,
\qquad
q_0''=0,
\]

the current local audit gives

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}.
\]

On a good phase patch,

\[
q_0\neq0,
\]

so

\[
\nu_{21,7}\neq0.
\]

Thus, if the homogeneous source is admissible, universal \(\nu_{21,7}=0\) is false.

I find no stated admissibility constraint in the attached/current proof state excluding this homogeneous source. On the contrary, the latest consolidated summaries explicitly use it as the decisive source test and state that it survives affine removal, endpoint symmetry, source-grade parity, frozen Bottleneck-C bookkeeping, and the actual finite Fréchet row. turn84file6

Therefore the current proof state supports:

\[
\boxed{
\text{the homogeneous good-patch model is admissible under the stated source constraints.}
}
\]

If a future draft wants to exclude it, it must add a new admissibility condition, such as a fourth-jet locking law or a source differential equation.

---

# 5. If homogeneous \(r(u)=u^2\) were declared inadmissible

Then the exact missing admissibility constraint must imply

\[
\frac{\rho_{i,4}}{\rho_{i,2}}
=
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}
\]

for every active source \(i\), or at least imply the pairwise identity

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
=0
\]

for every active pair \((i,j)\).

This is not a mild technical condition. It is a highly specific source-jet equation.

A theorem-ready version would be:

```latex
\begin{theorem}[Odd-\(\eta\eta\) source-jet locking]
For every active source direction \(i\), the phase-gap source jets satisfy
\[
\rho_{i,4}
=
\left(
\frac{10q_0^2}{9}
-
\frac{5q_0''}{18q_0}
\right)\rho_{i,2}.
\]
Consequently, for all active pairs \(i,j\),
\[
\nu_{21,7}=0.
\]
\end{theorem}
```

But this theorem is not presently available, and it would exclude the homogeneous test unless that test is explicitly removed from the admissible source class.

---

# 6. Consequence for the local branch

The source-jet identity route fails under the current source model.

\[
\boxed{
\nu_{21,7}=0
\text{ is not derivable and is refuted by the homogeneous good-patch test.}
}
\]

Therefore the local proof cannot be repaired by source-jet identities alone. The remaining possibilities are exactly:

\[
\boxed{
\sum_{\mathrm{top}\ \eta\eta} f_{\eta\eta}^{\rm top}=0
}
\]

as a structural aggregate top-row cancellation, or

\[
\boxed{
\text{a new second-order phase-gap correction/counterterm.}
}
\]

This matches the current local conclusion in the attached background: the proof now requires cancellation of \(\nu_{21,7}\), aggregate top-row \(S\)-cancellation, or a correction package; endpoint-diagonal realization is no longer the relevant missing theorem. 
## User (2026-04-25 16:20:36)

Do your specific instruction

## Assistant (2026-04-25 16:21:22)

_Thought for 45s_

## Local Agent B — frozen Bottleneck-C row-table completeness audit

### Target

Audit whether the frozen Bottleneck-C table is complete around

\[
\mathcal E^{2}_{\eta\eta;7,0,0}.
\]

The alleged survivor has signature

\[
\eta_i\eta_j,\qquad [z^7],\qquad (a,r,g,b)=(2,0,7,0),
\]

and

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

The current handover says this is the decisive local fork: the local package fails unless the homogeneous good-patch model is inadmissible or the frozen row table is incomplete. 

---

# 1. Reconstruct the active frozen table

The active Bottleneck-C coefficient is the frozen coefficient

\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\sum_{\chi\in\{dd,d\eta+\eta d,\eta\eta\}}
\sum_g
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b}.
\]

The source-position edge table

\[
[z^7\delta^1]
\]

is not part of this first Bottleneck-C carrier; the amplitude

\[
a_1a_2(a_1+a_2)
\]

already supplies the first \(\delta\)-edge. turn89file7

The row decomposition is

\[
H^A_{r,0}
=
\sum_{a\in\mathcal A_{\rm BC}}
A_a\Lambda^-_{a,r},
\]

so an individual frozen row is

\[
\mathcal E^a_{\chi;g,r,b}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,r}Y^\chi_{g,0}W_{+,b}
\right),
\]

with

\[
\chi\in\{dd,d\eta+\eta d,\eta\eta\},
\qquad
4\le g\le7,
\qquad
r+b=7-g.
\]

The older shorthand \(a\in\{1,5\}\) is stale; the concrete row uses the actual finite Fréchet index \(a=2\). turn89file12

---

# 2. Candidate rows with the same ordinary order and source profile

The target row has

\[
g=7,\qquad r=0,\qquad b=0.
\]

Because

\[
r+b=7-g,
\]

there are no \(r,b\)-partition partners at \(g=7\). Therefore no row with \(r>0\) or \(b>0\) can share this top-row ordinary-order signature.

The only possible same-order cancellation rows must therefore be

\[
\mathcal E^a_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}
\operatorname{Sym}
\left(
A_a\Lambda^-_{a,0}Y^{\eta\eta}_{7,0}W_{+,0}
\right)
\]

for other active \(a\in\mathcal A_{\rm BC}\).

Now split

\[
Y^{\eta\eta}_{7,0}
\]

into the odd off-diagonal scalar-\(\Delta\)-Hessian part and any other \(\eta\eta\) top terms. The identified odd term is

\[
Y^{\eta\eta_{\rm odd}}_{7,0}
=
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)J\eta_i\eta_j
\right]_7.
\]

The concrete row is

\[
\mathcal E^2_{\eta\eta;7,0,0}
=
\tau\pi_{\mathfrak f}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
Y^{\eta\eta_{\rm odd}}_{7,0}
W_{+,0}
\right).
\]

The current draft state identifies

\[
\Lambda^-_{2,0}
=
-\frac{1}{24\pi q^3}E_{22},
\]

and the row gives

\[
f_{\eta\eta}^{\rm top}
=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

turn89file4

---

# 3. Candidate-row table

Rows with the same \(\eta_i\eta_j\), \([z^7]\), \(r=b=0\) signature:

| Candidate | Source monomial | \(Q\)-homogeneity | Left primitive | Right slot | \(S\)-coefficient status |
|---|---|---:|---|---|---|
| \((a,\chi,g,r,b)=(2,\eta\eta_{\rm odd},7,0,0)\) | \(\eta_i\eta_j\) | \(Q^{-14}\) | \(\Lambda^-_{2,0}=-(24\pi q^3)^{-1}E_{22}\) | \(W_{+,0}\) | \(f=-u(24\pi q^3)^{-1}\nu_{21,7}\), generically nonzero |
| \((a,\eta\eta_{\rm odd},7,0,0)\), \(a\ne2\) | \(\eta_i\eta_j\) | would need \(Q^{-14}\) | \(\Lambda^-_{a,0}\) | \(W_{+,0}\) | no forced opposite coefficient shown by finite Fréchet table |
| \((a,\eta\eta_{\rm even},7,0,0)\) | \(\eta_i\eta_j\) | possible but parity-even/odd split differs | \(\Lambda^-_{a,0}\) | \(W_{+,0}\) | no forced cancellation of odd \(J\)-block; different matrix/parity structure |
| \((a,d\eta+\eta d,7,0,0)\) | \(d_i\eta_j+\eta_i d_j\) | different source monomial | \(\Lambda^-_{a,0}\) | \(W_{+,0}\) | cannot cancel \(\eta_i\eta_j\) coefficient structurally |
| \((a,dd,7,0,0)\) | \(d_id_j\) | different source monomial | \(\Lambda^-_{a,0}\) | \(W_{+,0}\) | cannot cancel \(\eta_i\eta_j\) coefficient structurally |

Rows with \(g<7\) have \(r+b>0\). They can be \(S\)-visible, but they do **not** share the same top-row source-jet profile:

\[
[z^7]\left(A_o\eta_i\eta_j\right),
\qquad r=b=0.
\]

They require extra \(W_{+,b}\) or \(\Lambda^-_{a,r}\) expansion and therefore have different baseline/source-jet profiles. They are not structural cancellation partners for \(\mathcal E^2_{\eta\eta;7,0,0}\).

---

# 4. Why the obvious “partners” do not count

## 4.1 Formal \(\Theta_\pm\) counterterms do not count

The instructions explicitly exclude formal counterterms and \(\Theta_\pm\) coordinate rewrites. The current state also says \(\Theta_\pm\) normal coordinates can hide the formal package obstruction but reintroduce it into the physical hidden coordinate \(T^{\rm phys}\). turn89file11

So no \(\Theta_\pm\) row is a physical frozen-row cancellation.

## 4.2 Later source-motion rows do not count

Rows with internal source-position edge

\[
[z^7\delta^1]
\]

belong to a later source-motion layer and are not the first Bottleneck-C amplitude derivative coefficient. They cannot cancel the frozen \(\delta^0\) row at this level. turn89file7

## 4.3 Quotient-line cancellation does not count

Even if a row made the total quotient determinant

\[
e v_5-u_5f
\]

vanish, that would not close the augmented package unless the \(S\)-component vanishes:

\[
f=0.
\]

The current local bookkeeping explicitly distinguishes quotient closure from \(T\)-horizontal closure. turn89file12

## 4.4 Accidental parameter cancellation does not count

A cancellation requiring

\[
\nu_{21,7}=0
\]

or a special relation among

\[
q_0,\ q_0'',\ \rho_{i,2},\ \rho_{i,4}
\]

is a source-jet identity, not row-table completeness. It belongs to Local Audit Agent 1, not this row-table audit.

---

# 5. The key isolation point

At top order

\[
g=7,
\]

the equation

\[
r+b=7-g
\]

forces

\[
r=b=0.
\]

Therefore there is no convolutional cancellation among

\[
\Lambda^-_{a,r}
\quad\text{and}\quad
W_{+,b}
\]

inside the top row. The row is isolated in the \(r,b\)-partition sense.

The only possible same-level cancellation would have to be another \(a\)-index top row with the **same** scalar \(\eta_i\eta_j\) odd-background profile and an exactly opposite fixed-sector \(S\)-coefficient. The finite Fréchet data reported in the handover singles out

\[
a=2,\qquad
\Lambda^-_{2,0}=-(24\pi q^3)^{-1}E_{22},
\]

as the relevant actual primitive for this signature. No companion primitive with opposite forced \(S\)-coefficient is identified in the draft/handover. turn89file7

Thus, within the current frozen table, the row is isolated.

---

# 6. Good-patch no-go model

Use the confirmed row:

\[
\mathcal E^2_{\eta\eta;7,0,0}
=
-\frac{\nu_{21,7}}{24\pi q^3}(wI+uS),
\]

with

\[
W_{+,0}
=
\begin{pmatrix}
u&w\\
w&v
\end{pmatrix}.
\]

On a diagonal leading right-whitening patch,

\[
w=0,\qquad u\ne0,
\]

so

\[
e=0,
\qquad
f=
-\frac{u}{24\pi q^3}\nu_{21,7}.
\]

For the homogeneous good-patch source test,

\[
\nu_{21,7}
=
-\frac{q_0^3}{216Q^{14}}
\neq0.
\]

Thus

\[
f=
\frac{u q_0^3}{5184\pi q^3Q^{14}}
\neq0.
\]

Therefore

\[
\partial_\kappa T
=
-a_1^2\frac{f}{c}
\neq0.
\]

If additionally

\[
u_5\ne0,
\]

then the quotient determinant also fails:

\[
Q=e v_5-u_5f=-u_5f\ne0.
\]

This is the requested row-level no-go in a good-patch model. It is exactly the local failure mode identified in the coordinator readout. turn89file14

---

# 7. Row-isolation theorem

```latex
\begin{theorem}[Top-row odd-\(\eta\eta\) isolation]
In the frozen Bottleneck-C coefficient
\[
E_{A,Y}^{\mathrm{BC}}
=
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\sum_{\chi}
\sum_g
\sum_{r+b=7-g}
H^A_{r,0}Y^\chi_{g,0}W_{+,b},
\]
the odd scalar \(\eta\eta\) row
\[
\mathcal E^2_{\eta\eta;7,0,0}
=
\tau_{h\to m}\pi_{\mathfrak f_h}\operatorname{Sym}
\left(
\Lambda^-_{2,0}
\left[
\left(
\frac{\sin\Delta_0}{s^2}
+
\frac{q_-\cos\Delta_0}{s}
\right)J\eta_i\eta_j
\right]_7
W_{+,0}
\right)
\]
has no structural cancellation partner in the frozen row table with the same
\(\eta_i\eta_j\) source profile, \(Q\)-homogeneity, and forced opposite
\(S\)-coefficient.  In particular, for the good-patch model with diagonal
\(W_{+,0}\), \(u\ne0\), \(q\ne0\), and
\[
\nu_{21,7}\ne0,
\]
one has
\[
f_{A,Y}\ne0.
\]
\end{theorem}
```

---

# 8. Final deliverable

\[
\boxed{
\text{No missing physical frozen row was found.}
}
\]

\[
\boxed{
\mathcal E^{2}_{\eta\eta;7,0,0}
\text{ is isolated at the frozen top row.}
}
\]

\[
\boxed{
f_{A,Y}\neq0
\text{ in the homogeneous good-patch model, provided that model is admissible.}
}
\]

So the local package now has only two remaining escape routes:

1. prove the homogeneous good-patch source is inadmissible or otherwise force
   \[
   \nu_{21,7}=0;
   \]
2. add a genuine new second-order phase-gap correction/counterterm.

The frozen row table itself does not provide the cancellation.
