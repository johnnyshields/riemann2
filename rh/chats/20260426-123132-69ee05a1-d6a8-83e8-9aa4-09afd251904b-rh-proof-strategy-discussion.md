# RH Proof Strategy Discussion

- Source: https://chatgpt.com/c/69ee05a1-d6a8-83e8-9aa4-09afd251904b
- Created: 2026-04-26 12:31:32 UTC
- Default model: gpt-5-5-thinking

---

## User (2026-04-26 12:31:29)

We are trying to prove RH. See paper draft attached. You will get instructions from a coordinator throughout this chat, and you will be "Agent 1" (or Agent A if letters are used.) The instructions will typically contain instructions for all agents, but you should do the specific instruction for "Agent 1". Please first read the paper draft, then await your next instruction.

## Assistant (2026-04-26 12:31:32)

I’ll ingest the LaTeX draft structurally first: title/abstract, theorem targets, current status markers, and appendices. Then I’ll stand by as Agent 1/A for coordinator instructions.

_Thought for 33s_

Read the draft.

I’ll operate as **Agent 1 / Agent A** going forward. My working map of the draft is:

- Current architecture is **not yet a closed RH proof**.
- Local machinery has produced substantial obstruction/visibility structure.
- The present frontier is the **actual-zeta source-curvature / source-jet nonflatness problem**, especially interval observability of \(q''\) on off-line packet intervals.
- The main live alternatives are:
  - prove actual-zeta source nonflatness,
  - find a source-robust row/invariant not divisible by \(H=yq''\),
  - or obtain a global affine/projective transport/index theorem with correction control.
- Gate A/Gate B and local rank-two fixed-sector structures are part of the established local package, but not by themselves proof-closing.

Standing by for the coordinator’s Agent 1 instruction.

I’ll execute the Agent 1/A task: isolate the draft’s actual definitions of \(q,q'',q_0,I_\rho,Q\), determine what “source curvature” currently means, and produce insertion-ready LaTeX plus open normalization dependencies.

I found the key convention conflict: the draft uses \(q=\Phi'\) globally, but later source-convention sections distinguish the full phase derivative \(q\), the rebuilt baseline \(q_0^{\new}\), and the affine-subtracted zero-source \(G^{\new}\). I’m going to resolve \(q''_{\rm can}\) as the full physical second derivative used by the rank-two rows, while keeping an optional “source-complement curvature” as a separate diagnostic.

_Thought for 2m 32s_

Agent 1 result: **canonicalize \(q''\)**. The coordinator’s requested deliverable is a proposition fixing \(q''_{\rm can}\), with zero-side and prime/AFE-side formulas, not an observability proof. 

## Verdict

Use

\[
\boxed{
q''_{\rm can}(m):=\frac{d^2}{dm^2}q_\zeta(m)
=\frac{d^3}{dm^3}\Phi_\zeta(m)
}
\]

where \(q_\zeta=\Phi_\zeta'\) is the **full actual-zeta phase derivative used in the same-point Gram block**.

So \(q''_{\rm can}\) is:

- **not** whitened curvature;
- **not** an AFE-normalized observable;
- **not** merely a projective/quotient invariant;
- **not automatically** the complement-source curvature \(G''\) after source/core splitting.

The source/core split should only partition \(q''_{\rm can}\) into pieces. If we need the complement-only curvature, call it separately

\[
q''_{\source,R}(m):=(G^{\new})''(m),
\]

not \(q''_{\rm can}\). This prevents the current overload between full Gram curvature and affine-subtracted source-complement curvature.

---

## Exact insertion

Insert immediately after:

```latex
\begin{definition}[Canonical source-curvature representation problem]
\label{def:canonical-source-curvature-representation-problem}
...
\end{definition}
```

or replace that definition with the following stronger version.

```latex
\begin{proposition}[Canonical source-curvature representation]
\label{prop:canonical-source-curvature-representation}
Fix the actual-zeta phase convention used in the finite-\(s\) Gram blocks,
so that
\[
q_\zeta(t)=\Phi_\zeta'(t)
\]
is the full physical phase derivative appearing in
\[
G_{m,\pm}(s)=\frac1\pi
\begin{pmatrix}
2q_\zeta(t_\pm) & \frac12 q_\zeta'(t_\pm)\\[1ex]
\frac12 q_\zeta'(t_\pm) &
\frac1{12}\bigl(q_\zeta''(t_\pm)+2q_\zeta(t_\pm)^3\bigr)
\end{pmatrix}.
\]
Define the canonical source-curvature object by
\[
\boxed{
q''_{\can}(m):=q_\zeta''(m)=\Phi_\zeta'''(m).
}
\]
This is the raw actual-zeta phase-derivative curvature in the local Gram
normalization.  It is not whitened, projectivized, divided by a Gram scale, or
defined by an approximate functional equation.  Approximate functional
equations and zero expansions are representations of this object, not its
definition.

Let the fixed source/core convention decompose the actual phase derivative as
\[
q_\zeta(t)
=
B_\zeta(t)+\sum_{\rho}^{\mathrm{reg}} K_0(t;\rho),
\]
where \(B_\zeta\) contains the gamma/background, pole, trivial-zero, and other
smooth completed-factor contributions in the chosen normalization, and
\(K_0(t;\rho)\) is the zero-packet contribution of the nontrivial zero packet
\(\rho\), with the sum interpreted in the same regularized sense used in the
local zeta-side decomposition.  Then, on a reduced good patch where the
selected source/core labels are fixed,
\[
\boxed{
q''_{\can}(m)
=
B_2(m)+\sum_{\rho}^{\mathrm{reg}}K_2(m;\rho),
}
\]
where
\[
B_2(m):=B_\zeta''(m),
\qquad
K_2(m;\rho):=\partial_m^2K_0(m;\rho).
\]
For example, for a single Cauchy packet in the draft's same-scale normalization
\[
K_0(m;c,\gamma)=\frac{c}{c^2+4(m-\gamma)^2},
\]
one has
\[
K_2(m;c,\gamma)
=
\frac{8c\bigl(12(m-\gamma)^2-c^2\bigr)}
{\bigl(c^2+4(m-\gamma)^2\bigr)^3}.
\]
For a symmetry packet, \(K_2(m;\rho)\) denotes the sum of this expression over
the packet members with the signs, multiplicities, and normalizing constants
dictated by the chosen completed-phase convention.

Equivalently, after choosing a smooth log-derivative AFE cutoff \(W\), write
the actual-zeta phase derivative on the patch in the form
\[
q_\zeta(m)
=
B_\zeta(m)
-
\Re\sum_{n\ge1}
b_n n^{-1/2-im}W(n/X)
+
\Re D_0(m;X,W)
+
E_0(m;X,W).
\]
In the standard logarithmic-derivative normalization,
\[
b_n=\Lambda(n),
\]
including prime powers.  The term \(D_0\) denotes the functional-equation dual
term, including the cutoff transform and any \(\chi\)-factor contribution not
already placed into \(B_\zeta\).  The term \(E_0\) is the residual error of the
chosen smoothed AFE on the patch.

Differentiating twice gives the prime/AFE-side representation
\[
\boxed{
q''_{\can}(m)
=
B_2(m)
+
\Re\sum_{n\ge1}
b_n(\log n)^2 n^{-1/2-im}W(n/X)
+
D_2(m;X,W)
+
E_2(m;X,W),
}
\]
where
\[
D_2(m;X,W):=\partial_m^2\Re D_0(m;X,W),
\qquad
E_2(m;X,W):=\partial_m^2E_0(m;X,W).
\]
If the opposite sign convention is chosen for the prime log-derivative main
sum, then the sign is absorbed into the definition of \(b_n\).  What is
canonical is the full object \(q_\zeta''(m)\), not the sign convention used to
write the oscillatory representation.
\end{proposition}

\begin{remark}[Full curvature versus complement-source curvature]
\label{rem:full-curvature-versus-complement-source-curvature}
The affine-subtracted rebuilt source
\[
G^{\new}=q_{\aux,R}+T_{\far,R}
\]
has its own curvature
\[
q''_{\source,R}(m):=(G^{\new})''(m).
\]
This is useful for Bottleneck-C source bookkeeping.  However it should not be
identified silently with \(q''_{\can}\).  The canonical object used in the
Gram anisotropy expressions
\[
\Gamma_G=q''-6q_0+2q_0^3,
\qquad
\Gamma_{G,2}=(1-q_0^2)q''-\frac16q^{(4)}
\]
is the full actual-zeta phase curvature unless a later subsection explicitly
rebuilds the entire finite-\(s\) row with \(q''_{\source,R}\) in place of
\(q''_{\can}\).
\end{remark}

\begin{remark}[Error scale required for observability]
\label{rem:canonical-source-curvature-error-scale}
For the interval observability theorem, the AFE error must be controlled on
each admissible reduced packet interval \(I_\rho\) at the derivative level
actually used.  A sufficient bookkeeping condition is: for every chosen
observability exponent \(B\), choose the smoothing and truncation parameters so
that
\[
\|E_2(\cdot;X,W)\|_{L^2(I_\rho)}
\le
\frac12 Q^{-B/2}|I_\rho|^{1/2},
\]
or else keep \(E_2\) inside the main observable.  For the finite-jet version,
one needs the stronger uniform derivative control
\[
\max_{0\le r\le R}
Q^{-r}\sup_{m\in I_\rho}
\left|
\partial_m^rE_2(m;X,W)
\right|
\le Q^{-B}.
\]
Without such a derivative-level error convention, the phrase
``prime-side source-curvature observability'' is not yet a precise theorem.
\end{remark}
```

---

## Unresolved normalization dependencies

1. **Exact phase convention.** The draft must fix whether \(\Phi_\zeta\) is the completed \(\xi\)-phase, Hardy \(Z\)-phase, scattering phase, or another equivalent normalization. This determines the sign of \(b_n\), the gamma term, and the zero-packet constants.

2. **Zero-packet atom normalization.** The packet kernel currently appears in the same-scale form
\[
K_0(m;c,\gamma)=\frac{c}{c^2+4(m-\gamma)^2}.
\]
If the actual completed-phase convention uses \(2c/(c^2+(m-\gamma)^2)\), or another rescaling, then \(K_2\) changes by a fixed scale. The proposition is written so that \(K_2=\partial_m^2K_0\) remains canonical once \(K_0\) is fixed.

3. **Full curvature vs. complement curvature.** The next agents should use \(q''_{\can}=q_\zeta''\). If an attack needs the affine-subtracted complement source, use \(q''_{\source,R}=(G^{\new})''\). Do not overload both as \(q''\).

4. **Background term \(B_2\).** \(B_2=B_\zeta''\) must explicitly include or exclude gamma, pole, trivial-zero, and \(\chi\)-factor contributions according to one fixed completed-phase convention.

5. **AFE dual term.** The dual term \(D_2\) is not optional unless the chosen AFE is one-sided with a proven error at the required derivative scale. Agent 4 must treat \(D_2\) as part of the fixed object, not as noise.

6. **Error scale.** The useful error is not a pointwise \(E_0\) bound. It must control \(E_2\), and for finite-jet nonrecurrence it must control \(\partial_m^rE_2\) up to \(R\asymp \log Q/\log\log Q\) or \(O(\log Q)\).

7. **Interval and \(Q\)-scale.** The proposition is independent of the exact \(I_\rho\) scale, but the observability theorem is not. The paper should explicitly state whether \(Q\sim q_0\), \(Q\sim\log T\), or another local height parameter on each reduced good patch.

The draft already has the arithmetic source-curvature subsection, but it still leaves three notational hazards: bare \(q''\) in the new observability subsection, a local shorthand where \(q''=(q_0^{\new})''\), and \(q''_R\) which can be confused with \(q''_{\source,R}\).

_Thought for 1m 57s_

Agent 1/A stress test complete. The coordinator’s instruction is to stabilize the convention \(q''_{\can}=q_\zeta''=\Phi_\zeta'''\), reserve \(q''_{\source,R}=(G^{\new})''\), and decide whether the Gram anisotropy notation needs explicit \(\can\)-decorations. 

## Verdict

Keep the main notation light:

\[
\Gamma_G,\qquad \Gamma_{G,2}
\]

do **not** need to become \(\Gamma_G(q_{\can})\), \(\Gamma_{G,2}(q_{\can})\) everywhere.

But the paper needs one explicit convention saying that, in the rank-two row section,

\[
q''=q''_{\can}=q_\zeta''=\Phi_\zeta''',
\qquad
q^{(4)}=(q_\zeta)^{(4)}.
\]

When ambiguity is possible, use decorated notation:

\[
\Gamma_G^{\can},
\qquad
\Gamma_{G,2}^{\can}.
\]

The main ambiguous spots I found are:

1. the current arithmetic source-curvature subsection still uses bare \(q''\);
2. the off-line conditional form uses \(q''_R\), which can be confused with \(q''_{\source,R}\);
3. the rebuilt split defines \(G^{\new}\) and affine-subtracted \(r_G\), but never names \(q''_{\source,R}\);
4. the Bottleneck-C defect subsection locally sets \(q'':=(q_0^{\new})''\), which now collides with the global convention;
5. the meromorphic ODE no-go uses “\(G=q\)” and \(q''/q\), which should be identified as the full actual phase derivative if it is meant as a full-phase test.

---

# Exact LaTeX edits

## Edit 1 — Add the missing macro

**Where:** In the macro block near the top, after:

```latex
\newcommand{\actual}{\mathrm{actual}}
```

**Insert:**

```latex
\newcommand{\can}{\mathrm{can}}
```

---

## Edit 2 — Add global canonical curvature convention

**Where:** After the first definition of the phase derivative, immediately after:

```latex
q(t):=\Ph'(t).
```

**Insert:**

```latex
\begin{definition}[Canonical actual-zeta phase curvature]
\label{def:canonical-actual-zeta-phase-curvature}
When the local phase is the actual zeta phase, we write
\[
\Ph=\Phi_\zeta,\qquad q_\zeta(t):=\Phi_\zeta'(t).
\]
The canonical source-curvature object used by the rank-two Gram rows is
\[
\boxed{
q''_{\can}(m):=q_\zeta''(m)=\Phi_\zeta'''(m).
}
\]
Thus \(q''_{\can}\) is the full actual-zeta phase-derivative curvature in the
same-point Gram normalization.  It is not a whitened, projectivized, AFE-normalized,
or affine-subtracted complement quantity.

When no ambiguity is possible, later centered rank-two formulas may write
\(q,q'',q^{(4)}\) for
\[
q_\zeta,\qquad q''_{\can},\qquad (q_\zeta)^{(4)}.
\]
If a source/core split is being discussed, the complement-source curvature is
instead denoted
\[
q''_{\source,R}(m):=(G^{\new})''(m),
\]
and should not be identified with \(q''_{\can}\) unless a separate rederived
row formula explicitly says so.
\end{definition}
```

---

## Edit 3 — Clarify the \(G^{\new}\) / affine-subtracted source block

**Where:** After:

```latex
This affine absorption is necessary: otherwise the source would contain value
and linear jets and would reopen lower source-grade gates.
```

**Insert:**

```latex
\begin{remark}[Complement-source curvature]
\label{rem:complement-source-curvature-notation}
For the rebuilt source split, define
\[
q''_{\source,R}(m):=(G^{\new})''(m).
\]
Since
\[
r_G(t)=G^{\new}(t)-G^{\new}(m)-G^{\new\,\prime}(m)(t-m),
\]
one has
\[
r_G''(m)=q''_{\source,R}(m).
\]
This is the curvature of the affine-subtracted non-core zero complement.  It is
not the full canonical actual-zeta curvature
\[
q''_{\can}(m)=q_\zeta''(m),
\]
which also includes the core, background, and all remaining completed-phase
contributions in the fixed actual-zeta normalization.
\end{remark}
```

---

## Edit 4 — Fix the Gram anisotropy definition once, then keep notation light

**Where:** In:

```latex
\begin{definition}[First and second Gram-anisotropy functionals]
\label{def:gram-anisotropy-functionals}
```

replace the opening part:

```latex
On a centered reduced patch define
\[
\Gamma_G
:=
q''-6q_0+2q_0^3 .
\]
```

with:

```latex
On a centered reduced patch, unless explicitly stated otherwise, \(q_0\),
\(q''\), and \(q^{(4)}\) mean the full actual-zeta centered jets
\[
q_0=q_\zeta(m),\qquad
q''=q''_{\can}(m)=q_\zeta''(m),\qquad
q^{(4)}=(q_\zeta)^{(4)}(m).
\]
Define
\[
\Gamma_G^{\can}
:=
q''_{\can}-6q_0+2q_0^3 .
\]
For readability we usually suppress the superscript and write
\(\Gamma_G=\Gamma_G^{\can}\).
```

Then replace:

```latex
\[
\Gamma_{G,2}
:=
(1-q_0^2)q''-\frac16q^{(4)}.
\]
```

with:

```latex
\[
\Gamma_{G,2}^{\can}
:=
(1-q_0^2)q''_{\can}-\frac16(q_\zeta)^{(4)}.
\]
Again, when the canonical convention is fixed, we write
\(\Gamma_{G,2}=\Gamma_{G,2}^{\can}\).
```

No global replacement of \(\Gamma_G\) or \(\Gamma_{G,2}\) is needed after this.

---

## Edit 5 — Replace the current canonical source-curvature definition

**Where:** Replace the full current block:

```latex
\begin{definition}[Canonical source-curvature representation problem]
\label{def:canonical-source-curvature-representation-problem}
...
\end{definition}
```

with:

```latex
\begin{proposition}[Canonical source-curvature representation]
\label{prop:canonical-source-curvature-representation}
In the actual-zeta normalization of
Definition~\ref{def:canonical-actual-zeta-phase-curvature}, the canonical
source-curvature object is
\[
\boxed{
q''_{\can}(m)=q_\zeta''(m)=\Phi_\zeta'''(m).
}
\]
This is the full physical phase-derivative curvature appearing in the same-point
Gram block.  Zero-side expansions and approximate functional equations are
representations of this object, not definitions of a different object.

With the source/core convention fixed, write the completed actual-zeta phase
derivative schematically as
\[
q_\zeta(t)
=
B_\zeta(t)+\sum_{\rho}^{\rm reg}K_0(t;\rho),
\]
where \(B_\zeta\) contains the smooth completed-factor contribution
(gamma/background, pole, trivial-zero, and convention-dependent smooth terms),
and \(K_0(t;\rho)\) is the nontrivial-zero packet contribution in the chosen
zero-side normalization.  Then
\[
\boxed{
q''_{\can}(m)
=
B_2(m)+\sum_{\rho}^{\rm reg}K_2(m;\rho),
}
\]
where
\[
B_2(m):=B_\zeta''(m),
\qquad
K_2(m;\rho):=\partial_m^2K_0(m;\rho).
\]

Equivalently, after choosing a smoothed log-derivative AFE cutoff \(W\), one
has a prime/AFE representation of the form
\[
\boxed{
q''_{\can}(m)
=
B_2(m)
+
\Re\sum_{n\le X}
b_n(\log n)^2 n^{-1/2-im}W(n/T)
+
D_2(m;X,W)
+
E_2(m;X,W).
}
\]
Here \(b_n\) is fixed by the actual zeta coefficients in the chosen convention
(for instance \(\Lambda(n)\)-type log-derivative weights), \(D_2\) is the dual
or functional-equation contribution, and \(E_2\) is the differentiated AFE
error.  The point is to forbid replacing the arithmetic object by an arbitrary
Dirichlet polynomial with tunable coefficients.
\end{proposition}
```

---

## Edit 6 — Update the observability subsection to use \(q''_{\can}\)

**Where:** In the opening of:

```latex
\subsection{Arithmetic source-curvature observability: the next attack}
```

replace:

```latex
\sup_{m\in I_\rho}|q''(m)|\ge Q^{-B}.
```

with:

```latex
\sup_{m\in I_\rho}|q''_{\can}(m)|\ge Q^{-B}.
```

and replace:

```latex
\int_{I_\rho}|q''(m)|^2\,dm
\ge
Q^{-B}|I_\rho|.
```

with:

```latex
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge
Q^{-B}|I_\rho|.
```

---

## Edit 7 — Update the source-curvature observability hypothesis

**Where:** In:

```latex
\begin{hypothesis}[Off-line-packet source-curvature observability]
\label{hyp:offline-packet-source-curvature-observability}
```

replace the body with:

```latex
Let \(I_\rho\) be an admissible reduced good-patch interval attached to a
hypothetical off-line packet \(\rho\).  Actual zeta data satisfy
\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge
Q^{-B}|I_\rho|
\]
for some fixed \(B\), outside the already named reduced-base and correction
incidence loci.
Equivalently, in a weaker pointwise form,
\[
\sup_{m\in I_\rho}|q''_{\can}(m)|\ge Q^{-B}.
\]
```

---

## Edit 8 — Rename \(q''_R\) in the off-line conditional form

**Where:** In:

```latex
\begin{remark}[Off-line-packet conditional form]
\label{rem:offline-packet-conditional-source-observability}
```

replace the displayed decomposition and following paragraph:

```latex
q''=q''_P+q''_R,
```

through

```latex
q''_R(m)=-q''_P(m)+O(Q^{-B})
```

with:

```latex
q''_{\can}=q''_P+q''_{\mathrm{rest}},
\]
where \(q''_P\) is the contribution of the distinguished off-line packet and
\(q''_{\mathrm{rest}}\) is the contribution of every other term in the full
actual-zeta phase curvature: core, non-core zero tail, smooth background,
dual/AFE terms, and errors, according to the fixed convention.  This
\(q''_{\mathrm{rest}}\) is not the same object as the complement-source
curvature \(q''_{\source,R}=(G^{\new})''\).

The interval observability claim may be sharpened to
\[
\int_{I_\rho}|q''_P(m)+q''_{\mathrm{rest}}(m)|^2\,dm
\ge
Q^{-B}|I_\rho|.
\]
Equivalently, the rest term cannot satisfy
\[
q''_{\mathrm{rest}}(m)=-q''_P(m)+O(Q^{-B})
```

The final sentence “throughout the packet interval...” can remain unchanged.

---

## Edit 9 — Update the prime-side formulation to include \(D_2,E_2\)

**Where:** In:

```latex
\begin{remark}[Prime-side observability formulation]
\label{rem:prime-side-source-curvature-observability-formulation}
```

replace:

```latex
Writing
\[
q''(m)=B_2(m)+P_2(m),
\]
where \(P_2\) is the oscillatory prime/AFE part, source collapse means
\[
P_2(m)\approx -B_2(m)
\quad\text{throughout }I_\rho.
\]
The desired arithmetic theorem is therefore an observability estimate of the
form
\[
\int_{I_\rho}|B_2(m)+P_2(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
\]
```

with:

```latex
Writing
\[
q''_{\can}(m)=B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]
where \(P_2\) is the oscillatory fixed-coefficient prime/AFE part, \(D_2\) is
the dual or functional-equation contribution, and \(E_2\) is the differentiated
error, source collapse means
\[
P_2(m)\approx -B_2(m)-D_2(m)-E_2(m)
\quad\text{throughout }I_\rho.
\]
If \(E_2\) has already been made negligible at the required derivative scale,
the desired arithmetic theorem becomes an observability estimate of the form
\[
\int_{I_\rho}|B_2(m)+P_2(m)+D_2(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
\]
Otherwise \(E_2\) must remain inside the observable.
```

---

## Edit 10 — Fix finite-jet notation

**Where:** In:

```latex
\begin{remark}[Finite-jet version of the arithmetic problem]
\label{rem:finite-jet-source-nonflatness-problem}
```

replace:

```latex
(q'')^{(r)}(m_0),\qquad 0\le r\le R,
```

with:

```latex
\partial_m^r q''_{\can}(m_0),\qquad 0\le r\le R,
```

replace:

```latex
\sum_n b_n(-i\log n)^r e^{-im_0\log n}
\approx
-B_2^{(r)}(m_0),
```

with:

```latex
\partial_m^r\bigl(B_2+P_2+D_2\bigr)(m_0)
\approx 0,
```

and replace:

```latex
\left|
(q'')^{(r)}(m_0)
\right|
```

with:

```latex
\left|
\partial_m^r q''_{\can}(m_0)
\right|
```

---

## Edit 11 — Disambiguate the Bottleneck-C local shorthand

**Where:** In:

```latex
\subsection{Global obstruction-class interpretation of the Bottleneck-C defect}
```

replace:

```latex
For this subsection write, for readability,
\[
G:=G^{\new}=q_{\mathrm{aux},R}+T_{\mathrm{far},R},
\qquad
A_2:=\frac{G''(m)}{2},
\qquad
A_4:=\frac{G^{(4)}(m)}{24},
\]
and
\[
q:=q_0^{\new},
\qquad
q'':=(q_0^{\new})''.
\]
```

with:

```latex
For this subsection write, for readability,
\[
G:=G^{\new}=q_{\mathrm{aux},R}+T_{\mathrm{far},R},
\qquad
A_2:=\frac{G''(m)}{2}=\frac12q''_{\source,R}(m),
\qquad
A_4:=\frac{G^{(4)}(m)}{24},
\]
and use the baseline-local notation
\[
q_b:=q_0^{\new},
\qquad
q_b^{(2)}:=(q_0^{\new})''.
\]
The notation \(q_b^{(2)}\) is deliberately not written as \(q''\), because
\(q''\) is reserved in the rank-two arithmetic sections for the full canonical
curvature \(q''_{\can}\).
```

Then, **within this same subsection only**, mechanically replace algebraic occurrences as follows:

```latex
qA_2A_4              -> q_bA_2A_4
qA_2A_2''            -> q_bA_2A_2''
qA_2A_2'             -> q_bA_2A_2'
q(A_2')^2            -> q_b(A_2')^2
q'A_2^2              -> q_b'A_2^2
q'A_2A_2'            -> q_b'A_2A_2'
q''A_2^2             -> q_b^{(2)}A_2^2
\frac{q''}{6}        -> \frac{q_b^{(2)}}{6}
\frac{23}{6}q''      -> \frac{23}{6}q_b^{(2)}
\frac{q''}{q}        -> \frac{q_b^{(2)}}{q_b}
q^3                  -> q_b^3
q^2                  -> q_b^2
K(m):=\frac{q''(m)}{6}-\frac{2q(m)^3}{3}
                      -> K_b(m):=\frac{q_b^{(2)}(m)}{6}-\frac{2q_b(m)^3}{3}
```

This is a local cleanup only; it does not change the mathematics.

---

## Edit 12 — Clarify the meromorphic ODE no-go full-phase notation

**Where:** In:

```latex
\subsection{Meromorphic ODE principal-part no-go}
```

replace:

```latex
or by the same equation with \(G=q\).
```

with:

```latex
or by the same equation with \(G=q_\zeta\), the full actual-zeta phase derivative.
```

Then replace the displayed full-phase local model:

```latex
q(t)=\frac{R}{t-p}+O(1),
```

with:

```latex
q_\zeta(t)=\frac{R}{t-p}+O(1),
```

and replace:

```latex
\frac{q''}{q}
```

with:

```latex
\frac{q''_{\can}}{q_\zeta}
```

in that meromorphic principal-part discussion.

---

# Final notation policy

After these edits, the paper’s convention is:

\[
q''_{\can}=q_\zeta''=\Phi_\zeta'''
\]

is the **full actual-zeta curvature** used by the Gram rows.

\[
q''_{\source,R}=(G^{\new})''
\]

is the **affine-subtracted complement-source curvature**.

\[
q''_{\mathrm{rest}}
\]

is the **rest term in a full actual-zeta decomposition** of \(q''_{\can}\), not the complement-source curvature.

\[
\Gamma_G,\Gamma_{G,2}
\]

can remain undecorated after Definition~\(\ref{def:gram-anisotropy-functionals}\), because that definition will explicitly say they mean the canonical full-phase versions unless otherwise stated.
## User (2026-04-26 13:03:31)

The paper has been updated with some corrections attached. Please read then await your next instruction.

## Assistant (2026-04-26 13:03:34)

I’ll verify the updated draft against the attached repair list, focusing only on whether the canonical \(q''_{\can}\), Gate 1/Gate 2 language, and corrected ODE identity are now present and internally consistent.

_Thought for 31s_

Read the updated draft and attached correction list. I verified the key repairs are present:

- \(q''_{\can}=q_\zeta''=\Phi_\zeta'''\) is now explicitly canonical.
- \(q''_{\source,R}=(G^{\new})''\) is separated from full canonical curvature.
- Gate 1 / Gate 2 are stated separately.
- The ODE identity uses the corrected derivative:
  \[
  \Gamma_G''=u''-6u+12q(q')^2+6q^2u,
  \qquad
  \Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
  \]
- Bottleneck-C notation now uses \(q_b,q_b^{(2)}\), avoiding collision with \(q''_{\can}\).
- The meromorphic ODE no-go is disambiguated with \(G=q_\zeta\).  

The attached correction list identifies these as the intended repair-only changes, including the important \(6q^2u\) coefficient correction. 

Standing by as **Agent 1 / A** for the next instruction.
## User (2026-04-26 13:04:57)

Do your next agent prompt as per your number in the attached.

## Assistant (2026-04-26 13:05:02)

_Stopped thinking_

## User (2026-04-26 13:05:15)

Continue

## Assistant (2026-04-26 13:05:16)

I’ll perform the Agent 1/A audit against the current draft: existing derivative/control lemmas, what they actually imply, what Gate 2 still needs, and insertion-ready weakest analytic package if it is missing.

The audit result is already clear enough: the draft has several local analytic ingredients, but it does not yet contain a theorem that propagates Gate 2 smallness from weighted positive-measure information to a controlled interval. I’ll formulate that missing package minimally rather than overstate what the draft proves.

_Thought for 2m 16s_

Agent 1/A audit complete.

## Verdict

**Gate 2 requires a new good-patch analytic lemma.**

The current draft has useful local analytic infrastructure, but it does **not** yet prove the analytic package needed to pass from

\[
\int_{I_\rho}|q''_{\can}|^2\,dm\ge Q^{-B}|I_\rho|
\]

to

\[
\int_{I_\rho}|q''_{\can}|^2
(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge Q^{-A}|I_\rho|.
\]

The missing ingredient is not prime/AFE arithmetic. It is a **local analytic propagation / base-locus rigidity package** for

\[
u=q''_{\can},\qquad \Gamma_G,\qquad \Gamma_{G,2},\qquad \Gamma_G''.
\]

The attached coordinator prompt correctly frames this as the next task: inventory whether the paper already gives polynomial Bernstein/Cauchy/Remez control for \(q\) through \(q^{(6)}\), and for the anisotropy functions. It also records the corrected identity

\[
\Gamma_G''
=
u''-6u+12q(q')^2+6q^2u,
\qquad
\Gamma_{G,2}
=
2q(q')^2-\frac16\Gamma_G''.
\]

That identity is usable, but only after adding explicit analytic complexity and propagation hypotheses. 

---

# 1. Existing draft machinery that helps Gate 2

The draft contains several ingredients that are **supportive**, but not yet enough.

## 1.1 Canonical curvature convention

The draft now fixes

\[
q''_{\can}=q_\zeta''=\Phi_\zeta'''
\]

as the full actual-zeta phase curvature, and separates it from

\[
q''_{\source,R}=(G^{\new})''.
\]

This is necessary for Gate 2 because the anisotropy functions use the full actual-zeta centered jets, not the affine-subtracted complement curvature. The repair list also explicitly states this convention and the repaired Gate 1/Gate 2 language. 

## 1.2 Local curvature estimate for the source scale

Early in the draft, there is a zeta-side local curvature estimate of the form

\[
|S''(m)|\ll L(m)S(m)^2.
\]

This is valuable, but it is not a Gate 2 analytic package. It controls the background-subtracted source scale \(S\), not the full collection

\[
q,\ q',\ q'',\ q^{(3)},\ q^{(4)},\ q^{(5)},\ q^{(6)}
\]

on an enlarged interval \(I_\rho^\ast\).

## 1.3 Jet-corrected phase transfer and tail curvature

The draft has a jet-corrected phase transfer theorem: if

\[
\|g_{\sm}''\|_{L^\infty(I)}\le S_2,
\]

then affine subtraction gives standard bounds for the residual phase and derivative. It also has a tail curvature theorem bounding \(S_2\) by a background term plus omitted-zero tail terms, with \(S_2=o(Q)\) under an expanding cutoff.

This supports error control for local block perturbations. It does **not** provide all derivative bounds through order six for the full \(q_\zeta\).

## 1.4 Same-point and mixed-block perturbation estimates

The draft has entrywise perturbation estimates assuming bounds of the form

\[
|\delta q|\ll L_I^2S_2,\qquad
|\delta q'|\ll L_I S_2,\qquad
|\delta q''|\ll S_2.
\]

These are useful for corrected finite-\(s\) Gram/mixed block control. However, they only assume/control up to second derivative of the perturbation. Gate 2 needs at least enough control to handle

\[
\Gamma_G''.
\]

Since

\[
\Gamma_G=u-6q+2q^3,\qquad u=q''_{\can},
\]

we have

\[
\Gamma_G''=q^{(4)}-6q''+12q(q')^2+6q^2q''.
\]

So even evaluating \(\Gamma_G''\) requires \(q^{(4)}\), and propagating smallness of \(\Gamma_G''\) or \(\Gamma_{G,2}\) by Bernstein/Remez arguments naturally asks for bounds beyond \(q^{(4)}\), typically through \(q^{(6)}\).

## 1.5 Holomorphy/Cauchy estimates for the finite-\(s\) scalar \(H_m(s)\)

The draft has Cauchy estimates for the corrected finite-\(s\) scalar \(H_m(s)\) and its odd microscopic expansion. These are strong within the \(s\)-variable expansion machinery.

But Gate 2 is an \(m\)-interval statement for

\[
q_\zeta(m),\quad q_\zeta'(m),\quad q_\zeta''(m),\quad \Gamma_G(m),\quad \Gamma_{G,2}(m).
\]

Cauchy control in the \(s\)-disk does not automatically give Bernstein/Remez control in the \(m\)-variable on \(I_\rho^\ast\).

## 1.6 Reduced good-patch reach and openness

The reduced good-patch reach hypothesis gives open geometric control: stable core selection, no packet boundary collapse, no Gram/whitening singularity, and controlled exceptional sets.

That is necessary context, but it is not an analytic complexity theorem. It does not prove

\[
\sup_{I_\rho^\ast}|q^{(r)}|\le Q^{C_r},
\qquad 0\le r\le 6,
\]

nor does it prove propagation of smallness for \(\Gamma_G\) or \(\Gamma_{G,2}\).

## 1.7 Negative Taylor--Bernstein source-flattening discussion

The draft already uses Taylor--Bernstein reasoning in a negative direction: finite same-scale quadrature can flatten source jets to polynomial tolerance on a microscopic interval. This is important because it shows why local source positivity alone is insufficient.

But this is not the same as a positive Gate 2 lemma. It shows the need for a real analytic-good-patch package plus actual-zeta arithmetic.

---

# 2. Missing analytic-good-patch assumptions

The current draft does **not** yet contain the following.

## Missing A — uniform derivative bounds through order six

Gate 2 needs a statement like

\[
\sup_{m\in I_\rho^\ast}|q_\zeta^{(r)}(m)|\le Q^{C_r},
\qquad 0\le r\le 6.
\]

Without this, one cannot control

\[
u=q''_{\can},\qquad
\Gamma_G,\qquad
\Gamma_{G,2},\qquad
\Gamma_G''
\]

with polynomial complexity.

## Missing B — \(L^2\)-mass to thick-subinterval propagation for \(u\)

Gate 1 gives only

\[
\int_{I_\rho}|u|^2\ge Q^{-B}|I_\rho|.
\]

To use ODE rigidity, we need a way to pass from this to a subinterval \(J\subset I_\rho^\ast\) where

\[
|u|\ge Q^{-C}
\]

throughout \(J\), with

\[
|J|\ge Q^{-C}|I_\rho|.
\]

This can follow from polynomial bounds on \(u'\), but the draft does not yet package it as a lemma.

## Missing C — Remez/Bernstein propagation for \(\Gamma_G,\Gamma_{G,2}\)

If the Gate 2 vector energy is assumed small,

\[
\int_I |u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\ll Q^{-A}|I|,
\]

and \(u\) is known to be large on a thick subinterval, then one must turn this into controlled smallness of

\[
\Gamma_G,\qquad \Gamma_{G,2}
\]

on a smaller interval. This requires Remez/Bernstein/propagation-of-smallness control.

The draft mentions Remez--Łojasiewicz volume estimates in status language, but does not provide a theorem of the required form.

## Missing D — derivative propagation from \(\Gamma_G\) to \(\Gamma_G''\)

The ODE identity uses \(\Gamma_G''\). Smallness of \(\Gamma_G\) alone does not imply smallness of \(\Gamma_G''\) unless one has analytic complexity control on a complex tube or a Bernstein-type derivative estimate.

Needed form:

\[
|\Gamma_G|\le Q^{-M}\ \text{on a thick set}
\quad\Longrightarrow\quad
|\Gamma_G''|\le Q^{-M+C}
\ \text{on a smaller interval}.
\]

This is absent.

## Missing E — quantitative base-locus rigidity

The exact base locus is rigid:

\[
\Gamma_G=0,\qquad \Gamma_{G,2}=0
\]

forces, via

\[
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G'',
\]

a strong ODE constraint. In the exact case, if \(\Gamma_G\equiv0\) and \(\Gamma_{G,2}\equiv0\) on an interval, then

\[
q''=6q-2q^3,
\qquad
q(q')^2=0.
\]

This forces \(q''=0\) on the relevant branches, so it is incompatible with \(u=q''\) carrying source mass.

But the paper needs a **quantitative** version:

\[
|u|\ge Q^{-B_0}
\quad\text{on a polynomially thick interval}
\]

should imply

\[
\sup_J\left(|\Gamma_G|+|\Gamma_{G,2}|\right)\ge Q^{-B_1}.
\]

That lemma is not currently proved.

---

# 3. Weakest analytic package needed

Insert the following as a new hypothesis/lemma package. Best location: immediately after

```latex
\begin{remark}[ODE form of the reintegration problem]
\label{rem:ode-form-source-anisotropy-reintegration}
...
\end{remark}
```

## Exact LaTeX insertion

```latex
\begin{hypothesis}[Gate-2 analytic good-patch package]
\label{hyp:gate-two-analytic-good-patch-package}
Let \(I_\rho\) be an admissible reduced good-patch interval and let
\(I_\rho^\ast\) be a fixed enlargement with the same center and
\[
|I_\rho^\ast|\asymp |I_\rho|.
\]
Put
\[
u=q''_{\can},
\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)}.
\]
Assume the following analytic complexity and propagation bounds hold on
\(I_\rho^\ast\).

\begin{enumerate}
\item \emph{Polynomial derivative complexity.}
There are constants \(C_r\), independent of \(Q\), such that
\[
\sup_{m\in I_\rho^\ast}
|q^{(r)}(m)|
\le Q^{C_r},
\qquad
0\le r\le 6.
\]
Consequently
\[
\sup_{I_\rho^\ast}
\left(
|u|+|u'|+|u''|
+|\Gamma_G|+|\Gamma_G'|+|\Gamma_G''|
+|\Gamma_{G,2}|+|\Gamma_{G,2}'|
\right)
\le Q^{C_\ast}
\]
for some \(C_\ast\).

\item \emph{Source-mass thickening.}
If
\[
\int_{I_\rho}|u(m)|^2\,dm
\ge Q^{-B}|I_\rho|,
\]
then there is a subinterval \(J\subset I_\rho^\ast\) such that
\[
|J|\ge Q^{-C_1}|I_\rho|
\]
and
\[
|u(m)|\ge Q^{-C_1}
\qquad (m\in J).
\]

\item \emph{Remez--Bernstein propagation for anisotropy.}
Let \(J\subset I_\rho^\ast\) be any interval with
\[
|J|\ge Q^{-C}|I_\rho|.
\]
If
\[
\int_J
\left(\Gamma_G^2+\Gamma_{G,2}^2\right)\,dm
\le Q^{-M}|J|,
\]
then there is a subinterval \(J'\subset J\), with
\[
|J'|\ge Q^{-C'}|J|,
\]
on which
\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|
\le Q^{-M/C'}.
\]
Here \(C'\) may depend on the good-patch complexity constants but not on \(Q\).

\item \emph{Quantitative ODE base-locus rigidity.}
For every \(C_0\) there exists \(C_2\) such that no subinterval
\(J'\subset I_\rho^\ast\) of length
\[
|J'|\ge Q^{-C_0}|I_\rho|
\]
can satisfy simultaneously
\[
|u|\ge Q^{-C_0},
\qquad
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|
\le Q^{-C_2}
\]
throughout \(J'\).
\end{enumerate}
\end{hypothesis}

\begin{lemma}[Conditional Gate-2 transfer from the analytic good-patch package]
\label{lem:conditional-gate-two-transfer-from-agp}
Assume Hypothesis~\ref{hyp:gate-two-analytic-good-patch-package}.  Then
Gate~1 implies Gate~2, after weakening the exponent.  More precisely, if
\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|,
\]
then there exists \(A=A(B)\) such that
\[
\int_{I_\rho}
|q''_{\can}(m)|^2
\left(
\Gamma_G(m)^2+\Gamma_{G,2}(m)^2
\right)\,dm
\ge Q^{-A}|I_\rho|.
\]
\end{lemma}

\begin{proof}[Proof sketch]
Write \(u=q''_{\can}\).  By source-mass thickening, Gate~1 gives a polynomially
large subinterval \(J\subset I_\rho^\ast\) on which
\[
|u|\ge Q^{-C_1}.
\]
If the Gate~2 integral were smaller than \(Q^{-A}|I_\rho|\) for \(A\) large,
then on \(J\) one would have
\[
\int_J(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\le Q^{-M}|J|
\]
for arbitrarily large \(M\), after increasing \(A\).  Remez--Bernstein
propagation would then give a smaller polynomially large interval \(J'\) on
which
\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le Q^{-M/C'}.
\]
Taking \(M\) large enough contradicts the quantitative ODE base-locus rigidity
part of Hypothesis~\ref{hyp:gate-two-analytic-good-patch-package}.  Hence the
Gate~2 integral has a polynomial lower bound.
\end{proof}

\begin{remark}[Status of the Gate-2 analytic package]
\label{rem:status-gate-two-analytic-good-patch-package}
The current draft contains several supporting analytic estimates: local
source-curvature control, affine-jet subtraction estimates, tail-curvature
bounds, corrected block perturbation estimates, and Cauchy bounds for the
finite-\(s\) corrected scalar.  These do not yet imply
Hypothesis~\ref{hyp:gate-two-analytic-good-patch-package}.  In particular, the
draft still needs an \(m\)-variable polynomial derivative-complexity theorem
through order six and a Remez--Bernstein propagation lemma for
\[
u=q''_{\can},\qquad
\Gamma_G,\qquad
\Gamma_{G,2},\qquad
\Gamma_G''.
\]
Thus Gate~2 is not currently a consequence of Gate~1.
\end{remark}
```

---

# 4. Why this is the weakest useful package

The proposed package separates four logically distinct needs.

First, derivative complexity through \(q^{(6)}\) is the minimum natural level because

\[
\Gamma_{G,2}
=
(1-q^2)q''-\frac16q^{(4)}
\]

uses \(q^{(4)}\), and controlling propagation of \(\Gamma_G''\) or \(\Gamma_{G,2}\) under Bernstein/Cauchy estimates requires derivatives beyond that.

Second, Gate 1 is an \(L^2\) statement. It does not say \(u\) is large on a usable interval. Source-mass thickening is needed to prevent all source mass from hiding in a tiny set.

Third, the Gate 2 failure mode is weighted:

\[
|u|^2(\Gamma_G^2+\Gamma_{G,2}^2).
\]

Once \(u\) is thickened, small vector energy must become smallness of \(\Gamma_G,\Gamma_{G,2}\) on a real interval. That is exactly a Remez/Bernstein propagation problem.

Fourth, the ODE identity gives a real obstruction only after propagation reaches \(\Gamma_G''\). The base-locus rigidity component is where the identity is actually used:

\[
\Gamma_G\approx0,\qquad
\Gamma_{G,2}\approx0
\]

implies

\[
q''\approx6q-2q^3,
\qquad
\Gamma_G''\approx12q(q')^2.
\]

If \(\Gamma_G\) is also small with propagated second derivative control, the system forces \(q(q')^2\) small. On a polynomially thick interval where \(|q''|\) is bounded below, this is incompatible with \(q'\) staying small and \(q''\) carrying mass, except near the algebraic roots \(q=0,\pm\sqrt3\); those root regimes also force \(q''\) small through

\[
q''\approx6q-2q^3.
\]

This is the core ODE rigidity mechanism.

---

# 5. Final audit table

| Needed for Gate 2 | Present in draft? | Status |
|---|---:|---|
| Canonical \(q''_{\can}\) convention | Yes | Fixed |
| Gate 1 / Gate 2 separation | Yes | Fixed |
| Correct ODE identity | Yes | Fixed after coefficient correction |
| Bounds for \(q,q',q'',q^{(3)},q^{(4)},q^{(5)},q^{(6)}\) on \(I_\rho^\ast\) | No | Missing |
| \(L^2\)-mass to thick-subinterval lemma for \(u=q''_{\can}\) | No | Missing |
| Remez/Bernstein propagation for \(\Gamma_G,\Gamma_{G,2}\) | No | Missing |
| Propagation from \(\Gamma_G\) to \(\Gamma_G''\) | No | Missing |
| Quantitative ODE base-locus rigidity | No | Missing |
| Gate 2 from Gate 1 | No | Requires new lemma |

## Final verdict

\[
\boxed{
\text{Gate 2 requires a new good-patch analytic package.}
}
\]

It may be provable using the current architecture, but it is **not currently proved by the draft**. The next useful local push should prove or disprove Hypothesis~\(\ref{hyp:gate-two-analytic-good-patch-package}\), especially the quantitative ODE base-locus rigidity and the Remez/Bernstein propagation step.
## User (2026-04-26 13:22:55)

Here is one more round of paper revisions + latest paper draft reflecting these. Please read then await your next instruction.

## Assistant (2026-04-26 13:22:57)

I’ll read the revised draft against the latest repair list and only check status/notation consistency, not start a new attack.

_Thought for 24s_

Read the revision packet and latest draft.

I confirmed the new draft reflects the status/ledger repairs around:

- \(H=yq''_{\can}\)
- the two-gate framing
- source-weighted interval non-concentration as the two-gate arithmetic problem
- the source-weighted layered residual definition
- the local-kernel notation guard for the same-scale model

The revision packet explicitly frames these as status/ledger repairs only: canonicalizing \(q''_{\can}\), replacing stale “Gate 1 alone” language, and adding the optional same-scale notation guard. 

Standing by as **Agent 1 / A** for the next instruction.
## User (2026-04-26 13:25:19)

Do your agent prompt as per your agent number.

## Assistant (2026-04-26 13:25:25)

I’ll handle Agent 1 only: source-mass thickening. I’ll first check whether the latest draft already contains a usable derivative/Lipschitz bound for \(u=q''_{\can}\), then give the weakest lemma if not.

The source-mass thickening component is elementary once one assumes a scale-normalized \(C^1\) bound for \(u=q''_{\can}\). The draft’s larger missing problem is proving that bound for the full actual-zeta phase; the thickening step itself is not the hard part.

_Thought for 47s_

Agent 1/A result: **source-mass thickening**.

## Verdict

The source-mass thickening step is provable from a very weak local analytic hypothesis:

\[
\boxed{
|I_\rho|\cdot \|u'\|_{L^\infty(I_\rho^\ast)}\le Q^{D},
\qquad u=q''_{\can}.
}
\]

Equivalently,

\[
\boxed{
|I_\rho|\cdot \|(q''_{\can})'\|_{L^\infty(I_\rho^\ast)}
=
|I_\rho|\cdot \|q_\zeta^{(3)}\|_{L^\infty(I_\rho^\ast)}
\le Q^D.
}
\]

This is much weaker than the full Gate-2 analytic package. It only needs first-derivative control of \(u\), i.e. third-derivative control of \(q_\zeta\). The later Remez/Bernstein and ODE-rigidity steps need higher derivatives, but **source-mass thickening does not**.

The current draft/status notes already say the full Gate-2 good-patch package is not proved and must include polynomial derivative complexity, source-mass thickening, Remez/Bernstein propagation, and ODE base-locus rigidity.  The specific Agent 1 instruction asks exactly for this thickening component under polynomial good-patch hypotheses. 

---

# Exact LaTeX insertion

Insert this after the Gate-2 analytic-good-patch discussion, preferably immediately before the Remez/Bernstein propagation lemma, or inside the new Gate-2 analytic package subsection.

```latex
\begin{lemma}[Source-mass thickening from a polynomial Lipschitz bound]
\label{lem:source-mass-thickening-polynomial-lipschitz}
Let \(I=I_\rho\) be an admissible reduced good-patch interval and let
\(I^\ast=I_\rho^\ast\) be a fixed enlargement with \(I\subset I^\ast\).  Put
\[
u=q''_{\can}.
\]
Assume the Gate~1 source-energy lower bound
\[
\int_I |u(m)|^2\,dm\ge Q^{-B}|I|
\]
and the scale-normalized polynomial Lipschitz bound
\[
|I|\cdot \|u'\|_{L^\infty(I^\ast)}\le Q^D.
\]
Then there exists a subinterval \(J\subset I\subset I^\ast\) such that
\[
|J|\ge c\,Q^{-(B/2+D)}|I|
\]
and
\[
|u(m)|\ge \frac12 Q^{-B/2}
\qquad (m\in J),
\]
where \(c>0\) is an absolute constant.  In particular, after weakening the
exponent, there is a constant \(C=C(B,D)\) such that
\[
|J|\ge Q^{-C}|I|,
\qquad
|u(m)|\ge Q^{-C}
\qquad (m\in J).
\]
\end{lemma}

\begin{proof}
By the \(L^2\) lower bound, there exists \(m_0\in I\) such that
\[
|u(m_0)|^2\ge Q^{-B},
\]
and hence
\[
a:=|u(m_0)|\ge Q^{-B/2}.
\]
Let
\[
M:=\|u'\|_{L^\infty(I^\ast)}.
\]
If \(M=0\), then \(u\) is constant on \(I^\ast\), and the conclusion holds
with \(J=I\).  Assume \(M>0\).  Define
\[
r:=\min\left\{\frac{|I|}{4},\,\frac{a}{4M}\right\}.
\]
Since \(m_0\in I\), at least one of the one-sided intervals
\[
[m_0-r,m_0]\cap I,
\qquad
[m_0,m_0+r]\cap I
\]
contains a subinterval \(J\subset I\) of length comparable to \(r\).  On this
subinterval, the Lipschitz bound gives
\[
|u(m)|
\ge
|u(m_0)|-M|m-m_0|
\ge
a-Mr
\ge
\frac34 a
\ge
\frac12 Q^{-B/2}.
\]
Using
\[
M\le Q^D |I|^{-1}
\]
and \(a\ge Q^{-B/2}\), we have
\[
r
\ge
\frac14 Q^{-(B/2+D)}|I|,
\]
after decreasing the absolute constant if necessary.  This proves the stated
lower bound for \(|J|\) and the pointwise lower bound for \(|u|\) on \(J\).
\end{proof}
```

---

# Minimal hypothesis to add to the good-patch package

The weakest missing assumption for this component is:

```latex
\begin{hypothesis}[Source Lipschitz complexity]
\label{hyp:source-lipschitz-complexity}
On every admissible reduced good-patch interval \(I_\rho\) with fixed
enlargement \(I_\rho^\ast\), the canonical source curvature
\[
u=q''_{\can}
\]
satisfies
\[
|I_\rho|\cdot
\|u'\|_{L^\infty(I_\rho^\ast)}
\le Q^D
\]
for some fixed exponent \(D\).  Equivalently,
\[
|I_\rho|\cdot
\|q_\zeta^{(3)}\|_{L^\infty(I_\rho^\ast)}
\le Q^D.
\]
\end{hypothesis}
```

Then the good-patch package can cite it as:

```latex
By Hypothesis~\ref{hyp:source-lipschitz-complexity} and
Lemma~\ref{lem:source-mass-thickening-polynomial-lipschitz}, Gate~1 gives a
polynomially large interval \(J\subset I_\rho^\ast\) on which
\[
|q''_{\can}|\ge Q^{-C}.
\]
```

---

# If the paper wants to derive the Lipschitz bound from derivative complexity

If the draft later proves the stronger derivative package

\[
\sup_{I_\rho^\ast}|q_\zeta^{(r)}|\le Q^{C_r},
\qquad 0\le r\le6,
\]

then source Lipschitz follows immediately from the \(r=3\) case, provided the interval scale is polynomial:

\[
|I_\rho|\ge Q^{-\kappa}.
\]

Add this corollary if useful:

```latex
\begin{corollary}[Source thickening from derivative complexity]
\label{cor:source-thickening-from-derivative-complexity}
Assume
\[
|I_\rho|\ge Q^{-\kappa}
\]
and
\[
\sup_{I_\rho^\ast}|q_\zeta^{(3)}|\le Q^{C_3}.
\]
Then
\[
|I_\rho|\cdot
\|(q''_{\can})'\|_{L^\infty(I_\rho^\ast)}
\le Q^{C_3}
\]
after increasing the exponent by \(\kappa\) if necessary.  Hence
Lemma~\ref{lem:source-mass-thickening-polynomial-lipschitz} applies.
\end{corollary}
```

A slightly cleaner version is:

```latex
\[
|I_\rho|\cdot
\|(q''_{\can})'\|_{L^\infty(I_\rho^\ast)}
\le
Q^{C_3-\kappa}
\]
```

if \(|I_\rho|\asymp Q^{-\kappa}\) is fixed precisely. For status bookkeeping, the coarse bound \(Q^{C_3+\kappa}\) is safer.

---

# Why this is the weakest useful lemma

Without a derivative or continuity modulus, the statement is false. A function can have

\[
\int_I |u|^2\ge Q^{-B}|I|
\]

while concentrating all its mass on a set of arbitrarily tiny measure. Then no polynomially long interval \(J\) with \(|u|\ge Q^{-C}\) is forced.

With the scale-normalized Lipschitz bound

\[
|I|\|u'\|_\infty\le Q^D,
\]

a spike of height at least \(Q^{-B/2}\) must persist for at least polynomial relative length. That is exactly the thickening needed before applying the Remez/Bernstein and ODE base-locus steps.

So the thickening subproblem is closed conditionally:

\[
\boxed{
\text{Gate 1}+\text{polynomial Lipschitz complexity of }q''_{\can}
\Longrightarrow
\text{source-mass thickening.}
}
\]

The remaining burden is for Agent 4’s derivative-complexity work: prove the required bound for the full actual-zeta \(q_\zeta^{(3)}\) on \(I_\rho^\ast\), including core packet, far tail, gamma/background, AFE error, and zero regularization.
## User (2026-04-26 13:32:49)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:33:21)

I’ll execute the new Agent 1/A prompt: prove a sharp conditional derivative-complexity theorem through order six by decomposing \(q_\zeta\) into background, finite core, and far tail, and isolate the exact assumptions needed.

_Thought for 1m 25s_

Agent 1/A — derivative complexity through order six.

## Executive verdict

The derivative-complexity package is **conditionally provable** from the current source/core architecture, but the current draft appears to have the required pieces only up to the already packaged tail-curvature level. What is still needed is not a new idea, but a **finite-order extension of the tail shell estimate through \(r=6\)**, plus explicit bookkeeping assumptions on core size/separation and residual regularization.

The target assigned to Agent 1 is exactly:

\[
\sup_{m\in I_\rho^\ast}|q_\zeta^{(r)}(m)|\le Q^{C_r},
\qquad 0\le r\le6,
\]

using

\[
q_\zeta=B_\zeta+q_{\core}+T_{\far}.
\]

The prompt also correctly identifies the likely missing estimate:

\[
\sup_{I_\rho^\ast}|T_{\far}^{(r)}|
\ll
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\ll Q^{C_r},
\qquad 0\le r\le6.
\]

This is the main finite-order bookkeeping lemma needed for Gate 2. 

---

# Conditional theorem

Let \(I=I_\rho\) and \(I^\ast=I_\rho^\ast\). Suppose on \(I^\ast\) we have the decomposition

\[
q_\zeta(t)=B_\zeta(t)+q_{\core}(t)+T_{\far}(t)+E(t),
\]

where \(E\) denotes any residual explicit-formula, smoothing, or zero-regularization error not already absorbed into the three displayed terms. The draft’s canonical source-curvature convention requires all such pieces to be in the same actual-zeta normalization as \(q''_{\can}=q_\zeta''\), not in the affine-subtracted complement convention. 

Assume the following.

## Assumption A — background derivative complexity

For \(0\le r\le6\),

\[
\sup_{I^\ast}|B_\zeta^{(r)}|\le Q^{b_r}.
\]

This is standard if \(B_\zeta\) is the gamma/Riemann--Siegel/pole/trivial-zero background and \(Q\) dominates the local logarithmic height, e.g.

\[
Q\gtrsim \log(3+T),
\qquad T\asymp m.
\]

For the completed zeta phase, Stirling gives

\[
B_\zeta(t)=\frac12\log\frac{t}{2\pi}+O(t^{-1})
\]

up to harmless normalization constants, so

\[
B_\zeta^{(0)}=O(Q),
\qquad
B_\zeta^{(r)}=O_r(1)
\quad (1\le r\le6)
\]

on high intervals away from \(t=0\). Thus \(B_\zeta\) is not the obstruction.

## Assumption B — finite-core size and separation

Write the core as a finite sum of packet kernels:

\[
q_{\core}(t)=\sum_{\lambda\in\mathcal L} c_\lambda K_\lambda(t),
\]

with

\[
\#\mathcal L\le Q^{N},
\qquad
|c_\lambda|\le Q^{W}.
\]

For each packet, assume a polynomial denominator lower bound on \(I^\ast\). A convenient form is

\[
\delta_\lambda(t)
:=
\sqrt{a_\lambda^2+(2t-\gamma_\lambda)^2}
\ge Q^{-\sigma}
\qquad(t\in I^\ast),
\]

where \(a_\lambda\) denotes the vertical packet parameter, e.g. \(a_\lambda=\beta_\lambda\) or \(1-\beta_\lambda\) in the one-zero kernel.

Then for \(0\le r\le6\),

\[
\sup_{I^\ast}|K_\lambda^{(r)}|
\le C_r Q^{(r+1)\sigma},
\]

and hence

\[
\sup_{I^\ast}|q_{\core}^{(r)}|
\le C_r Q^{N+W+(r+1)\sigma}.
\]

If one uses only horizontal separation

\[
|2t-\gamma_\lambda|\ge Q^{-\sigma},
\]

rather than the Euclidean denominator \(\delta_\lambda\), then the safer bound is

\[
\sup_{I^\ast}|K_\lambda^{(r)}|
\le C_r Q^{(r+2)\sigma}.
\]

Either version is polynomial.

## Assumption C — finite-order far-tail shell estimate

Let

\[
T_{\far}(t)=\sum_{\rho\notin\mathcal L}K_\rho(t),
\]

where the one-zero pieces have the draft’s form

\[
K_\rho(t)
=
\frac{1-\beta_\rho}{(1-\beta_\rho)^2+(2t-\gamma_\rho)^2}
+
\frac{\beta_\rho}{\beta_\rho^2+(2t-\gamma_\rho)^2}.
\]

For each omitted zero define

\[
\Delta_\rho:=\dist(2I^\ast,\gamma_\rho).
\]

Assume the omitted set satisfies

\[
\Delta_\rho\ge R,
\qquad
R\ge Q^{-\tau}.
\]

Then the one-zero derivative bound is

\[
|K_\rho^{(r)}(t)|
\le C_r\Delta_\rho^{-(r+2)}
\qquad(t\in I^\ast,\ 0\le r\le6).
\]

This exponent is consistent with the draft’s tail-curvature theorem: for \(r=2\), the tail curvature estimate uses \(\Delta_\rho^{-4}\). The new requirement is simply to package the same shell argument for \(r=0,1,\ldots,6\).

Now decompose omitted zeros into dyadic shells:

\[
\mathcal S_j
=
\{\rho\notin\mathcal L:2^jR\le\Delta_\rho<2^{j+1}R\}.
\]

A weak but sufficient local zero-counting input is

\[
\#\mathcal S_j
\le
Q^\nu(1+2^jR).
\]

Then

\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\le
\sum_{j\ge0}
Q^\nu(1+2^jR)(2^jR)^{-(r+2)}.
\]

Thus

\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\ll_r
Q^\nu
\left(R^{-(r+2)}+R^{-(r+1)}\right)
\ll_r
Q^{\nu+(r+2)\tau}
\]

for \(R\ge Q^{-\tau}\). Therefore

\[
\sup_{I^\ast}|T_{\far}^{(r)}|
\le Q^{C_{\far,r}},
\qquad
C_{\far,r}=\nu+(r+2)\tau+O_r(1).
\]

If the stronger linear shell occupancy

\[
\#\mathcal S_j\le Q^\nu 2^jR
\]

is available at all tail scales, the sharper bound is

\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\ll_r Q^\nu R^{-(r+1)}.
\]

But the weaker \(Q^\nu(1+2^jR)\) version already gives polynomial derivative complexity, provided \(R\) is not sub-polynomially small.

## Assumption D — residual derivative complexity

For any residual term \(E\),

\[
\sup_{I^\ast}|E^{(r)}|\le Q^{e_r},
\qquad 0\le r\le6.
\]

If there is no residual term after the exact zero-side decomposition, take \(E=0\). If \(E\) represents AFE smoothing, truncation, or zero-regularization, this derivative bound must be explicitly stated. Without it, derivative complexity for the full \(q_\zeta\) is not proved.

---

# Proof

For \(0\le r\le6\),

\[
q_\zeta^{(r)}
=
B_\zeta^{(r)}
+
q_{\core}^{(r)}
+
T_{\far}^{(r)}
+
E^{(r)}.
\]

The background term satisfies

\[
\sup_{I^\ast}|B_\zeta^{(r)}|\le Q^{b_r}.
\]

For the core, the one-packet kernel derivative bound gives

\[
\sup_{I^\ast}|K_\lambda^{(r)}|
\le C_r Q^{(r+1)\sigma}
\]

under Euclidean denominator separation. Therefore

\[
\sup_{I^\ast}|q_{\core}^{(r)}|
\le
\sum_{\lambda\in\mathcal L}
|c_\lambda|\sup_{I^\ast}|K_\lambda^{(r)}|
\le
C_r Q^{N+W+(r+1)\sigma}.
\]

For the far tail,

\[
\sup_{I^\ast}|T_{\far}^{(r)}|
\le
\sum_{\rho\notin\mathcal L}
\sup_{I^\ast}|K_\rho^{(r)}|
\le
C_r\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}.
\]

Using the dyadic shell estimate above,

\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\ll_r
Q^{\nu+(r+2)\tau}.
\]

Finally,

\[
\sup_{I^\ast}|E^{(r)}|\le Q^{e_r}.
\]

Combining the four estimates gives

\[
\sup_{I^\ast}|q_\zeta^{(r)}|
\le
Q^{C_r}
\]

with, for example,

\[
C_r=
\max\{
b_r,\,
N+W+(r+1)\sigma,\,
\nu+(r+2)\tau,\,
e_r
\}
+O_r(1).
\]

This proves the derivative-complexity package through order six, conditionally on the stated polynomial source/core/tail assumptions.

---

# Component-by-component status

## 1. Background \(B_\zeta\)

**Status: controlled.**

The gamma/background term should be polynomial under the usual height convention \(Q\sim\log T\). This is not the hard piece.

Needed assumption:

\[
\sup_{I^\ast}|B_\zeta^{(r)}|\le Q^{b_r},
\qquad 0\le r\le6.
\]

This can be proved from Stirling-type bounds for the completed zeta gamma factor.

## 2. Finite core \(q_{\core}\)

**Status: controlled once denominator separation and core cardinality are explicit.**

Needed assumptions:

\[
\#\mathcal L\le Q^N,
\]

and either

\[
\sqrt{a_\lambda^2+(2m-\gamma_\lambda)^2}\ge Q^{-\sigma}
\qquad(m\in I^\ast)
\]

or the stronger horizontal variant

\[
|2m-\gamma_\lambda|\ge Q^{-\sigma}.
\]

The distinguished off-line packet is not a singularity as long as its vertical displacement/depth and horizontal distance from the real sampling interval remain polynomially separated in the reduced good patch. If the off-line zero approaches the real line or the sampling pole at sub-polynomial distance, core derivative complexity fails.

Quartet symmetry does not hurt the bound. It may cancel leading odd/even pieces, but for derivative complexity it only improves constants.

## 3. Far tail \(T_{\far}\)

**Status: main missing packaged lemma.**

The draft already has a tail-curvature theorem at the \(r=2\) level. The required Gate-2 derivative package needs the same shell proof through \(r=6\). The prompt correctly identifies this as the likely missing finite-order shell estimate. 

The required extension is:

\[
\sup_{I^\ast}|T_{\far}^{(r)}|
\ll_r
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\ll
Q^{C_r},
\qquad 0\le r\le6.
\]

This follows if:

\[
\Delta_\rho\ge R\ge Q^{-\tau}
\]

and shell occupancy is polynomial:

\[
\#\{\rho:2^jR\le\Delta_\rho<2^{j+1}R\}
\le Q^\nu(1+2^jR).
\]

If the cutoff \(R\) is allowed to be exponentially or super-polynomially small, the estimate fails. Such zeros must be included in the core instead.

## 4. Residual \(E\)

**Status: must be named or killed.**

The current proof is clean only if the zero-side decomposition is exact:

\[
q_\zeta=B_\zeta+q_{\core}+T_{\far}.
\]

If an \(E_{\est}\), AFE error, smoothing error, or zero-regularization term remains, then one needs

\[
\sup_{I^\ast}|E^{(r)}|\le Q^{e_r},
\qquad 0\le r\le6.
\]

Otherwise the full \(q_\zeta\) derivative complexity is not proved.

---

# Weakest assumptions needed

The package needs exactly the following.

## Core size

\[
\#\mathcal L\le Q^N.
\]

This is enough; no fixed core size is necessary.

## Core separation

For each core packet,

\[
\inf_{m\in I^\ast}
\sqrt{a_\lambda^2+(2m-\gamma_\lambda)^2}
\ge Q^{-\sigma}.
\]

This is the right denominator condition. Horizontal separation alone is stronger but not necessary.

## Tail cutoff

\[
R:=\inf_{\rho\notin\mathcal L}\Delta_\rho\ge Q^{-\tau}.
\]

Equivalently: every zero closer than polynomial distance to the tube/interval must be included in \(\mathcal L\).

## Local zero counting

A sufficient shell count is

\[
\#\mathcal S_j\le Q^\nu(1+2^jR).
\]

The stronger shell count \(\#\mathcal S_j\ll Q^\nu 2^jR\) gives better exponents, but is not required for mere polynomial complexity.

## Tube width

For the direct real-axis kernel proof, a complex tube is not strictly necessary. If the paper wants to derive derivative bounds by Cauchy estimates instead, it needs a tube of width

\[
\eta\ge Q^{-\tau_\eta}
\]

free of omitted poles, with polynomial sup bounds on the tube. Then

\[
|q_\zeta^{(r)}|\le r!\eta^{-r}\sup_{\text{tube}}|q_\zeta|
\]

is polynomial for \(r\le6\). But the direct kernel derivative proof is sharper and avoids relying on complex-tube sup control.

---

# Failure modes

The derivative package fails in exactly these cases.

1. **A core zero has sub-polynomial denominator distance:**

\[
\inf_{I^\ast}\sqrt{a_\lambda^2+(2m-\gamma_\lambda)^2}<Q^{-A}
\]

for every fixed \(A\). Then \(q_{\core}^{(r)}\) may be super-polynomial.

2. **The tail cutoff is sub-polynomial:**

\[
R< Q^{-A}
\]

for every fixed \(A\). Then

\[
\sum_{\rho\notin\mathcal L}\Delta_\rho^{-(r+2)}
\]

can be super-polynomial.

3. **Zero counting is not polynomial in shells.**

If a shell can contain super-polynomially many omitted zeros, the tail bound fails. This is not expected for actual zeta, but it must be an explicit input.

4. **A residual \(E\) remains uncontrolled through six derivatives.**

Then the decomposition does not prove derivative complexity for full \(q_\zeta\).

---

# Final theorem statement

A compact theorem version:

\[
\boxed{
\textbf{Derivative-complexity theorem, conditional form.}
}
\]

Let \(I^\ast=I_\rho^\ast\) be a reduced good-patch enlargement and suppose

\[
q_\zeta=B_\zeta+q_{\core}+T_{\far}+E.
\]

Assume:

\[
\sup_{I^\ast}|B_\zeta^{(r)}|\le Q^{b_r},
\qquad 0\le r\le6;
\]

\[
q_{\core}=\sum_{\lambda\in\mathcal L}c_\lambda K_\lambda,
\qquad
\#\mathcal L\le Q^N,\quad |c_\lambda|\le Q^W,
\]

and

\[
\inf_{m\in I^\ast}
\sqrt{a_\lambda^2+(2m-\gamma_\lambda)^2}
\ge Q^{-\sigma};
\]

\[
T_{\far}=\sum_{\rho\notin\mathcal L}K_\rho,
\qquad
\Delta_\rho\ge R\ge Q^{-\tau},
\]

with shell occupancy

\[
\#\{\rho:2^jR\le\Delta_\rho<2^{j+1}R\}
\le Q^\nu(1+2^jR);
\]

and

\[
\sup_{I^\ast}|E^{(r)}|\le Q^{e_r},
\qquad 0\le r\le6.
\]

Then for each \(0\le r\le6\),

\[
\sup_{m\in I^\ast}|q_\zeta^{(r)}(m)|
\le Q^{C_r},
\]

where one may take

\[
C_r=
\max\{
b_r,\,
N+W+(r+1)\sigma,\,
\nu+(r+2)\tau,\,
e_r
\}
+O_r(1).
\]

This is sufficient for the derivative-complexity component of the Gate-2 analytic package. The remaining work is to prove the assumptions—especially the finite-order far-tail shell estimate and the residual derivative bound—in the actual reduced good-patch construction.
## User (2026-04-26 13:43:30)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:43:31)

I’ll execute Agent 1/A: inspect the draft’s core/tail definitions and reduced-patch conditions, then decide whether they already imply “all polynomially near packets are in the core,” especially for the distinguished off-line packet.

_Thought for 44s_

Agent 1/A — near-zero inclusion and finite-core definition.

## Verdict

The current draft has the right **mechanism**, but not under the name “fixed core” alone.

The draft’s actual split is:

\[
q(t)=q_{\core}(t)+q_{\aux,R}(t)+g_{\sm,R}(t)+E_{\est,R}(t),
\qquad
g_{\sm,R}=B_{\bg}+T_{\far,R}.
\]

Here:

\[
q_{\core}
\]

comes from the fixed anomaly core \(\mathcal C\);

\[
q_{\aux,R}
\]

comes from zeros outside \(\mathcal C\) but inside the \(R\)-near shell;

\[
T_{\far,R}
\]

comes from zeros outside the near shell. The draft states exactly this fixed-core / auxiliary-near / far split. 

Therefore:

\[
\nu\notin \mathcal C
\quad\Longrightarrow\quad
\Delta_\nu(I_\rho^\ast)\ge Q^{-C_R}
\]

is **false** in general, because \(\nu\) could be an auxiliary-near zero:

\[
\nu\in\mathcal A_R,\qquad
\nu\notin\mathcal C,\qquad
\Delta_\nu(I_\rho^\ast)<R.
\]

But the correct derivative-complexity statement is true if we define the derivative-complexity finite core as

\[
\boxed{
\mathcal L_R^{\der}:=\mathcal C\cup\mathcal A_R,
}
\]

where \(\mathcal A_R\) is the symmetry-closed set of all non-core packets with

\[
\Delta_\nu(I_\rho^\ast)\le R.
\]

Then

\[
\nu\notin\mathcal L_R^{\der}
\quad\Longrightarrow\quad
\Delta_\nu(I_\rho^\ast)>R.
\]

If we choose

\[
R\ge Q^{-C_R},
\]

this gives the required near-zero exclusion:

\[
\boxed{
\nu\notin\mathcal L_R^{\der}
\quad\Longrightarrow\quad
\Delta_\nu(I_\rho^\ast)\ge Q^{-C_R}.
}
\]

This is exactly the condition needed to prevent a sub-polynomially close zero from being misclassified into the far tail. The latest prompt identifies this as the key risk for Gate 2 derivative complexity. 

---

# 1. Exact core/tail split currently used

The current draft uses a **two-level split**.

First, it fixes a finite anomaly core:

\[
\mathcal C.
\]

This core contains the candidate off-line anomaly, for example the designated off-line pair and its symmetry-forced companions. 

Then, for each cutoff \(R\ge R_0\), it decomposes the remaining zero contribution into:

\[
q_{\aux,R}
\]

and

\[
T_{\far,R}.
\]

So the full phase derivative is written as

\[
q(t)=q_{\core}(t)+q_{\aux,R}(t)+g_{\sm,R}(t)+E_{\est,R}(t),
\qquad
g_{\sm,R}=B_{\bg}+T_{\far,R}.
\]

The draft also has a tail-curvature theorem with the omitted set defined by

\[
\Delta_\rho>R.
\]

In that theorem,

\[
T_{\far}(t)=\sum_{\rho\notin\mathcal L}f_{\beta_\rho,\gamma_\rho}(t),
\]

and the proof explicitly uses the fact that omitted zeros satisfy the cutoff condition \(\Delta_\rho>R\). 

So the operational split is:

\[
\text{fixed anomaly core } \mathcal C
\quad+\quad
\text{auxiliary near set } \mathcal A_R
\quad+\quad
\text{far tail } \mathcal F_R.
\]

For Gate 2 derivative complexity, the relevant “finite core” cannot be only \(\mathcal C\). It must be

\[
\boxed{
\mathcal L_R^{\der}=\mathcal C\cup\mathcal A_R.
}
\]

---

# 2. Does the reduced good-patch definition already force all polynomially near packets into \(\mathcal L\)?

Not if \(\mathcal L=\mathcal C\).

The draft’s fixed-core construction deliberately keeps \(\mathcal C\) stable as \(R\) changes. That is good for the toy anomaly comparison, but it means \(\mathcal C\) is not designed to absorb every polynomially near zero.

Instead, the \(R\)-dependent auxiliary set absorbs the near zeros outside the fixed anomaly core. This was the purpose of the fixed-core repair: the toy comparison is attached only to \(\mathcal C\), while \(q_{\aux,R}\), \(T_{\far,R}\), and \(E_{\est,R}\) are absorbed into the corrected zeta-side scalar. 

Therefore the draft already prevents polynomially near zeros from being in the **far tail**, but it does not force them into the **fixed anomaly core**.

So:

\[
\nu\notin\mathcal C
\Rightarrow
\Delta_\nu\ge Q^{-C_R}
\]

is false.

But:

\[
\nu\notin(\mathcal C\cup\mathcal A_R)
\Rightarrow
\Delta_\nu>R
\]

is true by definition of the cutoff split.

---

# 3. Proof of the corrected implication

Define the packet denominator distance on the enlarged interval by

\[
\Delta_\nu(I_\rho^\ast)
:=
\inf_{m\in I_\rho^\ast}
\sqrt{c_\nu^2+(m-\gamma_\nu)^2}.
\]

Use the paper’s precise denominator if it differs by harmless constants, e.g. \(2m-\gamma_\nu\). Constants do not matter for polynomial separation.

Fix a polynomial cutoff

\[
R=Q^{-C_R}
\]

or more generally

\[
R\ge Q^{-C_R}.
\]

Define:

\[
\mathcal A_R
:=
\{\nu\notin\mathcal C:
\Delta_\nu(I_\rho^\ast)\le R\},
\]

closed under conjugation and functional-equation symmetries. Then define

\[
\mathcal L_R^{\der}:=\mathcal C\cup\mathcal A_R.
\]

The far tail is

\[
\mathcal F_R
:=
\{\nu:\nu\notin\mathcal L_R^{\der}\}.
\]

By construction,

\[
\nu\in\mathcal F_R
\Rightarrow
\Delta_\nu(I_\rho^\ast)>R.
\]

Since \(R\ge Q^{-C_R}\),

\[
\nu\notin\mathcal L_R^{\der}
\Rightarrow
\Delta_\nu(I_\rho^\ast)>R\ge Q^{-C_R}.
\]

Thus the near-zero inclusion rule is established, but only for the derivative-complexity core \(\mathcal L_R^{\der}\), not for the fixed anomaly core \(\mathcal C\).

---

# 4. Weakest additional core-selection rule needed

The weakest rule is:

\[
\boxed{
\mathcal L_R^{\der}
\text{ must include every packet } \nu
\text{ with }
\Delta_\nu(I_\rho^\ast)\le R,
\quad R\ge Q^{-C_R}.
}
\]

More explicitly:

1. Start with the fixed anomaly core \(\mathcal C\).
2. Choose a polynomial cutoff \(R\ge Q^{-C_R}\).
3. Add every zero packet satisfying

\[
\Delta_\nu(I_\rho^\ast)\le R.
\]

4. Close the set under the required symmetries:

\[
\rho,\quad \bar\rho,\quad 1-\rho,\quad 1-\bar\rho.
\]

5. Call the resulting set \(\mathcal L_R^{\der}\).

The fixed toy comparison should continue to use \(\mathcal C\). The derivative-complexity proof should use \(\mathcal L_R^{\der}\).

This distinction is essential:

\[
\mathcal C
=
\text{fixed anomaly core},
\]

\[
\mathcal L_R^{\der}
=
\text{finite near-zero set used for derivative estimates}.
\]

Conflating them either breaks cutoff stability or leaves near zeros in the far tail.

---

# 5. Distinguished off-line packet

The distinguished off-line packet is safe under the current setup because \(\mathcal C\) is defined to contain the candidate off-line anomaly, including the designated off-line pair and symmetry-forced companions. 

Thus:

\[
\rho_{\mathrm{off}}\in\mathcal C\subset\mathcal L_R^{\der}.
\]

It is not in the far tail.

If the paper ever considers a formulation where the distinguished packet is not included in \(\mathcal C\), then one must impose either:

\[
\rho_{\mathrm{off}}\in\mathcal L_R^{\der},
\]

or

\[
\Delta_{\rho_{\mathrm{off}}}(I_\rho^\ast)\ge Q^{-C}.
\]

But the second option is unnatural for an interval attached to that packet. The correct rule is to include it.

---

# 6. Can any zero remain in the tail at sub-polynomial distance?

No, not if the derivative-complexity core is defined correctly.

If

\[
\mathcal L_R^{\der}
=
\mathcal C\cup
\{\nu:\Delta_\nu(I_\rho^\ast)\le R\}
\]

with

\[
R\ge Q^{-C_R},
\]

then every tail zero satisfies

\[
\Delta_\nu(I_\rho^\ast)>R\ge Q^{-C_R}.
\]

So no tail zero can remain at sub-polynomial distance.

But under the **fixed anomaly core alone**, yes: a zero may satisfy

\[
\nu\notin\mathcal C,
\qquad
\Delta_\nu(I_\rho^\ast)\ll Q^{-A}
\]

for some large \(A\), and then it is only safe if it lies in \(q_{\aux,R}\), not \(T_{\far,R}\).

Therefore the exact answer is:

\[
\boxed{
\text{No sub-polynomially close zero may remain in }T_{\far,R}.
}
\]

But:

\[
\boxed{
\text{sub-polynomially close non-anomaly zeros may exist outside }\mathcal C;
\text{ they must be placed in }q_{\aux,R}.
}
\]

---

# 7. Counterexample to the uncorrected statement

Suppose \(\mathcal C\) contains only the distinguished off-line packet and its symmetry companions. Suppose another zero packet \(\nu\) lies near \(I_\rho^\ast\) with

\[
\Delta_\nu(I_\rho^\ast)=Q^{-100}.
\]

If the cutoff is, say,

\[
R=Q^{-10},
\]

then

\[
\nu\notin\mathcal C
\]

but

\[
\Delta_\nu(I_\rho^\ast)<R.
\]

Thus the statement

\[
\nu\notin\mathcal C
\Rightarrow
\Delta_\nu(I_\rho^\ast)\ge Q^{-C_R}
\]

is false.

However, by the corrected split,

\[
\nu\in\mathcal A_R
\subset\mathcal L_R^{\der},
\]

so the tail implication

\[
\nu\notin\mathcal L_R^{\der}
\Rightarrow
\Delta_\nu(I_\rho^\ast)\ge Q^{-C_R}
\]

remains true.

---

# 8. Final theorem

The clean statement is:

\[
\boxed{
\textbf{Near-zero inclusion theorem for derivative complexity.}
}
\]

Let \(I_\rho^\ast\) be the enlarged interval and define

\[
\Delta_\nu(I_\rho^\ast)
=
\inf_{m\in I_\rho^\ast}
\sqrt{c_\nu^2+(m-\gamma_\nu)^2}.
\]

Fix a polynomial cutoff

\[
R\ge Q^{-C_R}.
\]

Let \(\mathcal C\) be the fixed anomaly core, containing the distinguished off-line packet and all required symmetry companions. Define the derivative near-core by

\[
\mathcal L_R^{\der}
=
\mathcal C
\cup
\{\nu\notin\mathcal C:\Delta_\nu(I_\rho^\ast)\le R\},
\]

with symmetry closure. Let \(T_{\far,R}\) be the contribution of packets outside \(\mathcal L_R^{\der}\). Then every omitted tail packet satisfies

\[
\Delta_\nu(I_\rho^\ast)>R\ge Q^{-C_R}.
\]

Consequently, no zero packet at sub-polynomial distance from \(I_\rho^\ast\) is left in the tail.

This proves the near-zero inclusion rule conditionally on choosing the derivative-complexity core as \(\mathcal L_R^{\der}\). It does **not** prove that the fixed anomaly core \(\mathcal C\) alone contains all polynomially near zeros, and the draft should not require that.
## User (2026-04-26 13:46:49)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:47:51)

_Thought for 59s_

Agent 1/A — denominator-separation audit.

## Verdict

\[
\boxed{
\text{Polynomial denominator separation is missing and mathematically substantive.}
}
\]

The current draft has mechanisms that protect the **far tail** and the **finite-\(s\) omitted-zero holomorphy** package, but I do **not** see a theorem or hypothesis that guarantees

\[
\inf_{\nu\in\mathcal L_R^{\der}}
\inf_{m\in I_\rho^\ast}
\Delta_\nu(m)\ge Q^{-C_{\sep}}
\]

for **every packet in the derivative-complexity core**

\[
\mathcal L_R^{\der}=\mathcal C\cup\mathcal A_R.
\]

This matters because the Gate 2 derivative-complexity package requires polynomial control of the full canonical phase derivative

\[
\sup_{I_\rho^\ast}|q_\zeta^{(r)}|\le Q^{C_r},
\qquad 0\le r\le6,
\]

and the finite core is controlled only if both cardinality and denominator separation are polynomial. The latest coordinator message correctly identifies this denominator issue as the remaining fork: if a core packet center lies inside \(I_\rho^\ast\), then the denominator lower bound is essentially its transverse depth, so a packet with depth \(e^{-Q}\) breaks derivative complexity. 

---

# 1. Inventory of relevant draft conditions

## A. Tail cutoff condition

The draft has a tail curvature theorem with omitted zeros satisfying

\[
\Delta_\rho>R.
\]

This gives protection for the far tail:

\[
\rho\notin\mathcal L
\quad\Rightarrow\quad
\Delta_\rho(I_\rho^\ast)>R.
\]

That is enough to prevent a near zero from being accidentally left in \(T_{\far,R}\), provided the derivative-complexity core is defined as

\[
\mathcal L_R^{\der}:=\mathcal C\cup\mathcal A_R.
\]

This was already settled in the previous near-zero inclusion pass: the fixed anomaly core \(\mathcal C\) alone is not enough; \(\mathcal A_R\) must absorb every packet within cutoff distance \(R\) of \(I_\rho^\ast\). The current synthesis states exactly this: \(\nu\notin\mathcal L_R^{\der}\Rightarrow \Delta_\nu(I_\rho^\ast)>R\ge Q^{-C_R}\). 

**But this is not denominator separation for core packets.** It only says omitted packets are far.

## B. Denominator comparability for omitted zeros

The draft also has a finite-\(s\) denominator-comparability statement for omitted zeros. It assumes a zero-free-region type lower bound

\[
a_\rho\ge \frac{\sigma_0}{Q}
\]

for omitted zero denominators and then proves comparability for

\[
D_{\rho,\pm}(s)
=
((2m-\gamma_\rho)\pm s)^2+a_\rho^2
\]

on the microscopic \(s\)-disk.

This again protects omitted smooth terms. It does **not** imply

\[
\Delta_\nu(m)\ge Q^{-C_{\sep}}
\]

for all packets in \(\mathcal C\cup\mathcal A_R\).

## C. Fixed anomaly core and auxiliary-near split

The draft’s actual decomposition is not merely

\[
q_\zeta=B_\zeta+q_{\core}+T_{\far}.
\]

It is more accurately

\[
q
=
q_{\core}
+
q_{\aux,R}
+
g_{\sm,R}
+
E_{\est,R},
\qquad
g_{\sm,R}=B_{\bg}+T_{\far,R}.
\]

Here:

\[
\mathcal C
\]

is the fixed anomaly core;

\[
\mathcal A_R
\]

is the cutoff-dependent auxiliary near set;

\[
T_{\far,R}
\]

contains only omitted packets beyond the cutoff.

This split is excellent for keeping the toy/anomaly core fixed while still preventing near omitted zeros from polluting the far tail. But it does not impose denominator separation inside \(\mathcal C\) or inside \(\mathcal A_R\).

## D. Reduced good-patch reach

The reduced good-patch reach hypothesis appears to be a non-swallowing / persistence assertion: it says the reduced patch survives after removing named incidence loci. It protects the local row/whitening/reduced-base setup.

But as currently used, it does not explicitly say:

\[
\Delta_\nu(m)\ge Q^{-C_{\sep}}
\qquad
(\nu\in\mathcal L_R^{\der},\ m\in I_\rho^\ast).
\]

So it is not enough for derivative complexity.

## E. Strict core gap / endpoint separation / Gram positivity

These conditions are useful for the local obstruction model and finite countermodel bookkeeping. They prevent various degeneracies in the toy geometry: core collision, endpoint swallowing, bad Gram signs, etc.

They do **not** obviously exclude a core packet with very small transverse denominator. In particular, a packet can be selected into the core precisely because it is near; selection alone does not make its denominator polynomially bounded below.

---

# 2. Distinguishing \(\mathcal C\) from \(\mathcal A_R\)

This distinction is now critical.

## Fixed anomaly core \(\mathcal C\)

\(\mathcal C\) contains the distinguished hypothetical off-line packet and its symmetry companions. It is fixed so that the local anomaly comparison is not constantly changing as \(R\) changes.

For \(\nu\in\mathcal C\), denominator separation is **not automatic**. If the distinguished packet has a very small transverse depth and ordinate inside \(I_\rho^\ast\), then

\[
\inf_{m\in I_\rho^\ast}\Delta_\nu(m)
\]

can be super-polynomially small.

Thus:

\[
\nu\in\mathcal C
\quad\not\Rightarrow\quad
\Delta_\nu\ge Q^{-C}.
\]

## Auxiliary near set \(\mathcal A_R\)

\(\mathcal A_R\) contains non-core packets within the near cutoff \(R\). Its purpose is to prevent near packets from sitting in the far tail.

For \(\nu\in\mathcal A_R\), the only thing we know from membership is:

\[
\Delta_\nu(I_\rho^\ast)\le R.
\]

This is an **upper** bound, not a lower bound. There is no contradiction if

\[
\Delta_\nu(I_\rho^\ast)\ll Q^{-C}
\]

for every fixed \(C\). Such a packet is near; it belongs in \(\mathcal A_R\), but its derivatives may be huge.

So:

\[
\nu\in\mathcal A_R
\quad\not\Rightarrow\quad
\Delta_\nu\ge Q^{-C}.
\]

## Far tail

For \(\nu\notin\mathcal L_R^{\der}\), we do get:

\[
\Delta_\nu(I_\rho^\ast)>R.
\]

If \(R\ge Q^{-C_R}\), this is polynomial separation for omitted packets.

So:

\[
\nu\notin\mathcal L_R^{\der}
\quad\Rightarrow\quad
\Delta_\nu\ge Q^{-C_R}.
\]

This is settled. It is not the remaining issue.

---

# 3. Is denominator separation already a theorem, hypothesis, or missing?

It is **missing** for \(\mathcal L_R^{\der}\).

More precisely:

\[
\boxed{
\text{Tail separation is already built into the cutoff.}
}
\]

\[
\boxed{
\text{Core denominator separation is not currently implied.}
}
\]

A correct derivative-complexity theorem needs both:

\[
\nu\notin\mathcal L_R^{\der}
\Rightarrow
\Delta_\nu\ge R\ge Q^{-C_R}
\]

and

\[
\nu\in\mathcal L_R^{\der}
\Rightarrow
\Delta_\nu\ge Q^{-C_{\sep}}.
\]

The first is definitional. The second is substantive.

---

# 4. Distinguished off-line packet

The distinguished off-line packet is protected from being in the **tail** because it is part of the fixed anomaly core:

\[
\rho_{\off}\in\mathcal C\subset\mathcal L_R^{\der}.
\]

But it is **not protected from having a very small denominator**.

If the packet center lies inside or very near \(I_\rho^\ast\), then

\[
\Delta_{\rho_{\off}}(I_\rho^\ast)
\asymp c_{\rho_{\off}},
\]

where \(c_{\rho_{\off}}\) is the relevant transverse denominator in the local packet kernel.

If

\[
c_{\rho_{\off}}\ll Q^{-C}
\quad\text{for every fixed }C,
\]

then the derivative-complexity estimate through order six fails for the smooth-core proof.

This is the substantive issue: adding

\[
c_{\rho_{\off}}\ge Q^{-C_{\sep}}
\]

may exclude very shallow off-line zeros, depending on what \(c_{\rho_{\off}}\) means in the canonical zero-kernel normalization.

If \(c_{\rho_{\off}}\) is literally the distance from the critical line, then this is a zero-free-strip-type assumption for off-line zeros near the critical line and is not harmless. If \(c_{\rho_{\off}}\) is only a coordinate denominator after a regularizing transform, it may be a patch regularity condition. The draft needs to disambiguate this.

---

# 5. Critical-line zeros inside \(I_\rho^\ast\)

This depends on the exact zero-kernel convention.

There are two possible conventions.

## Convention A — completed/log-derivative kernel with denominators \(\beta\) and \(1-\beta\)

The draft’s displayed zero-side tail kernel has the form

\[
f_{\beta,\gamma}(t)
=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]

In that convention, a critical-line zero has \(\beta=1/2\), so the denominator parameter is not zero:

\[
\beta=1-\beta=1/2.
\]

Then a critical-line zero at ordinate inside \(I_\rho^\ast\) is **regular** in this kernel. It does not create a \(1/(m-\gamma)\) singularity. It may make the kernel large only by ordinary bounded constants, not by a vanishing transverse denominator.

Under this convention, critical-line zeros are not the main denominator-separation problem.

## Convention B — packet kernel measured by transverse distance to the critical line

Some local packet models use a kernel like

\[
K_c(m-\gamma)
=
\frac{c}{c^2+(m-\gamma)^2}.
\]

If \(c=0\) for critical-line zeros, then such zeros would be singular or distributional unless regularized separately.

In that convention, \(I_\rho^\ast\) must either avoid critical-line ordinates polynomially:

\[
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C},
\]

or the critical-line contribution must be placed in a separate regularized term, not treated as an ordinary finite-core packet.

## Current audit conclusion

The draft’s canonical zero-side kernel appears closer to Convention A for the completed actual-zeta phase derivative. Therefore critical-line zeros are probably **regularized by the completed phase convention**, not singular.

However, the local packet-model notation still sometimes uses a transverse-depth kernel. So the safe conclusion is:

\[
\boxed{
\text{Critical-line zeros are not automatically a problem in the completed-kernel convention,}
}
\]

but

\[
\boxed{
\text{the paper must not import the }c=0\text{ local packet denominator into }
q_\zeta\text{ derivative-complexity estimates without regularization.}
}
\]

---

# 6. Counterexample under current setup

Assume the current admissible reduced patch requires only:

- fixed anomaly core selection;
- strict core gap in the toy coordinates;
- endpoint separation;
- Gram/whitening nondegeneracy;
- all \(R\)-near non-core zeros moved into \(\mathcal A_R\);
- far tail cutoff \(\Delta>R\).

Now place a core packet \(\nu\in\mathcal C\) with center in \(I_\rho^\ast\) and transverse denominator

\[
c_\nu=e^{-Q}.
\]

Then:

\[
\nu\in\mathcal L_R^{\der},
\]

so it is not in the tail. The near-zero inclusion rule is satisfied.

But:

\[
\inf_{m\in I_\rho^\ast}\Delta_\nu(m)
\asymp e^{-Q},
\]

so no polynomial lower bound holds. Its \(r\)-th derivative can be of size roughly

\[
e^{(r+1)Q}
\]

or worse depending on kernel normalization. Hence

\[
\sup_{I_\rho^\ast}|q_\zeta^{(r)}|
\le Q^{C_r}
\]

fails.

Nothing in the known good-patch reach or fixed-core selection rules, as currently stated, excludes this.

Therefore denominator separation is not implied.

---

# 7. Weakest additional condition

The weakest useful condition is not “all near zeros are in the core.” That is already the right tail-safety condition.

The missing condition is:

\[
\boxed{
\textbf{Core denominator regularity.}
}
\]

For some fixed \(C_{\sep}\),

\[
\inf_{\nu\in\mathcal L_R^{\der}}
\inf_{m\in I_\rho^\ast}
\Delta_\nu(m)
\ge Q^{-C_{\sep}}.
\]

Equivalently:

1. all packets closer than the cutoff \(R\) are included in \(\mathcal L_R^{\der}\);
2. every packet included in \(\mathcal L_R^{\der}\) has only polynomially small denominator on \(I_\rho^\ast\);
3. if a packet violates this, it belongs to a separate **singular-packet regime**, not the smooth Gate 2 analytic package.

This gives a clean two-regime split:

\[
\text{Regime I: denominator-separated smooth patch;}
\]

\[
\text{Regime II: singular or shallow-core packet.}
\]

Gate 2 is currently proved only in Regime I.

---

# 8. Is it harmless to add?

Not obviously.

If the excluded packets are only coordinate poles or critical-line artifacts that are regular under the completed phase, then it is harmless.

But if it excludes a hypothetical off-line zero with transverse depth

\[
c_\nu\ll Q^{-C}
\]

for every fixed \(C\), and if \(c_\nu\) is actual distance from the critical line, then adding denominator separation is mathematically substantive. It would be imposing a polynomial zero-free strip around the critical line for the very off-line zeros the proof is supposed to rule out.

Thus the correct verdict is not “harmless to add.” It is:

\[
\boxed{
\text{missing and mathematically substantive unless singular-packet regimes are handled separately.}
}
\]

---

# 9. Final answer to the six tasks

1. **Inventory.** Tail cutoff and omitted-zero denominator comparability exist; fixed anomaly core, auxiliary-near split, reduced good-patch reach, strict core gap, and endpoint separation do not by themselves give core denominator separation.

2. **\(\mathcal C\) vs. \(\mathcal A_R\).** \(\mathcal C\) contains the distinguished packet; \(\mathcal A_R\) contains cutoff-near non-core packets. Neither membership condition implies a lower denominator bound.

3. **Status.** Denominator separation for all \(\nu\in\mathcal L_R^{\der}\) is missing. It is not a theorem currently.

4. **Distinguished off-line packet.** It is protected from the tail but not protected from being shallow. If its transverse denominator is super-polynomially small, derivative complexity fails unless a separate large/singular-core argument handles it.

5. **Critical-line zeros.** In the completed-kernel convention, critical-line zeros appear regular; in a raw transverse-depth kernel, they are singular and require interval avoidance or regularization. This is a separate convention issue that must be fixed before using denominator separation language globally.

6. **Verdict.**

\[
\boxed{
\text{Missing and mathematically substantive.}
}
\]

The smooth Gate 2 package should be kept, but it must be paired with a singular-packet alternative:

\[
\boxed{
\text{Either denominator-separated smooth Gate 2 applies,}
}
\]

or

\[
\boxed{
\text{a very-near/shallow core packet gives a separate lower-bound mechanism.}
}
\]

Absent that second-regime analysis, the proof still has a real gap at the denominator-separation point.
## User (2026-04-26 13:51:12)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:51:14)

I’ll do Agent 1/A: isolate a single near packet \(K_c\), compute the singular scales of \(q,u,q^{(4)},\Gamma_G,\Gamma_{G,2}\), and prove a direct Gate 2 lower bound under an explicit non-cancellation/dominance condition.

_Thought for 34s_

Agent 1/A — singular-packet dominance theorem.

## Verdict

A single sub-polynomially shallow packet **does force Gate 2 directly** on any interval that contains a comparable-width neighborhood of its center, unless the rest of the zero/background data cancels the packet’s singular jet vector at the same scale.

So the singular branch splits cleanly:

\[
\boxed{
\text{near-packet dominance} \Rightarrow \text{Gate 2 with huge margin}
}
\]

or

\[
\boxed{
\text{Gate 2 failure} \Rightarrow \text{same-scale singular cancellation certificate.}
}
\]

This matches the two-regime architecture in the coordinator note: denominator separation cannot be assumed globally; the singular regime must be handled by dominance or reduced to anti-quadrature/cancellation. 

---

# 1. Model packet and derivative scales

Let

\[
K_c(x)=\frac{c}{x^2+c^2}
=
c^{-1} f(s),
\qquad
s=\frac{x}{c},
\qquad
f(s)=\frac1{1+s^2}.
\]

Then

\[
\frac{d^r}{dx^r}K_c(x)
=
c^{-r-1}f^{(r)}(s).
\]

Thus on \(|x|\lesssim c\),

\[
q_P=K_c\asymp c^{-1},
\]

\[
u_P=q_P''\asymp c^{-3},
\]

\[
q_P^{(4)}\asymp c^{-5}.
\]

More explicitly,

\[
q_P''(x)
=
\frac{2c(3x^2-c^2)}{(x^2+c^2)^3}
=
c^{-3} f''(s),
\]

where

\[
f''(s)=\frac{2(3s^2-1)}{(1+s^2)^3}.
\]

At the packet center,

\[
q_P(0)=c^{-1},
\qquad
u_P(0)=-2c^{-3}.
\]

Also

\[
q_P^{(4)}(x)=c^{-5}f^{(4)}(s),
\]

and

\[
f^{(4)}(0)=24.
\]

So

\[
q_P^{(4)}(0)=24c^{-5}.
\]

---

# 2. Induced anisotropy scales

Recall

\[
\Gamma_G=u-6q+2q^3,
\]

\[
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)}.
\]

If \(q=q_P\) only, then

\[
\Gamma_G
=
c^{-3}\bigl(f''+2f^3\bigr)-6c^{-1}f.
\]

Since

\[
f''+2f^3
=
\frac{6s^2}{(1+s^2)^3},
\]

we get

\[
\Gamma_G
=
c^{-3}\frac{6s^2}{(1+s^2)^3}
-
6c^{-1}\frac1{1+s^2}.
\]

So \(\Gamma_G\) is typically \(c^{-3}\) away from \(s=0\), but at the exact center the \(c^{-3}\) terms cancel and

\[
\Gamma_G(0)=-6c^{-1}.
\]

Thus \(\Gamma_G\) alone is not the best dominance witness at the packet center.

For the second anisotropy,

\[
\Gamma_{G,2}
=
(1-q_P^2)q_P''-\frac16q_P^{(4)}.
\]

At \(x=0\),

\[
\Gamma_{G,2}(0)
=
(1-c^{-2})(-2c^{-3})-\frac16(24c^{-5})
=
-2c^{-3}+2c^{-5}-4c^{-5}
=
-2c^{-5}-2c^{-3}.
\]

Hence

\[
|\Gamma_{G,2}(0)|\asymp c^{-5}.
\]

By continuity of the normalized profile, there exists an absolute \(\eta>0\), for example any sufficiently small fixed \(\eta\), such that on

\[
|x|\le \eta c
\]

we have

\[
|u_P(x)|\ge a_0c^{-3},
\]

and

\[
|\Gamma_{G,2}^{(P)}(x)|\ge b_0c^{-5},
\]

for absolute constants \(a_0,b_0>0\). The exact constants are irrelevant; the important fact is the scale

\[
|u_P|^2|\Gamma_{G,2}^{(P)}|^2
\asymp
c^{-6}c^{-10}
=
c^{-16}.
\]

Integrating over a length-\(\asymp c\) packet neighborhood gives

\[
\int |u_P|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\gtrsim
c^{-15}.
\]

This is enormous when \(c\ll Q^{-C}\) for arbitrarily large \(C\).

---

# 3. A clean non-cancellation condition

The scalar condition

\[
|u_{\mathrm{rest}}|\le \frac12 |u_P|
\]

is sufficient to keep \(u\) large, but not by itself sufficient to keep \(\Gamma_{G,2}\) large, because \(\Gamma_{G,2}\) also involves \(q\) and \(q^{(4)}\). The correct dominance condition should be a weighted jet-vector condition.

On a packet neighborhood

\[
J_\eta=[\gamma-\eta c,\gamma+\eta c],
\]

assume

\[
|q_{\mathrm{rest}}|\le \varepsilon c^{-1},
\]

\[
|q_{\mathrm{rest}}''|\le \varepsilon c^{-3},
\]

\[
|q_{\mathrm{rest}}^{(4)}|\le \varepsilon c^{-5},
\]

with \(\varepsilon>0\) sufficiently small depending only on \(\eta\). Equivalently,

\[
\sup_{J_\eta}
\left(
c|q_{\mathrm{rest}}|
+
c^3|q_{\mathrm{rest}}''|
+
c^5|q_{\mathrm{rest}}^{(4)}|
\right)
\le\varepsilon.
\]

Then

\[
q=q_P+q_{\mathrm{rest}},
\qquad
u=u_P+q_{\mathrm{rest}}'',
\qquad
q^{(4)}=q_P^{(4)}+q_{\mathrm{rest}}^{(4)}
\]

satisfy, on a smaller neighborhood \(J_{\eta'}\subset J_\eta\),

\[
|u|\ge a c^{-3},
\]

and

\[
|\Gamma_{G,2}|\ge b c^{-5},
\]

for constants \(a,b>0\).

This follows because \(\Gamma_{G,2}\), after scaling by \(c^5\), is a smooth polynomial/rational expression in the normalized variables

\[
c q,\qquad c^3q'',\qquad c^5q^{(4)}.
\]

For the pure packet, this normalized expression is bounded away from zero on \(|s|\le \eta'\). Small weighted perturbations cannot destroy that lower bound.

A slightly more invariant condition is:

\[
\sup_{J_\eta}
\left\|
\bigl(cq_{\mathrm{rest}},c^3u_{\mathrm{rest}},c^5q_{\mathrm{rest}}^{(4)}\bigr)
\right\|
\le
\varepsilon
\inf_{J_{\eta'}}
\left\|
\bigl(cq_P,c^3u_P,c^5q_P^{(4)}\bigr)
\right\|.
\]

But the explicit weighted form above is easier to use.

---

# 4. Dominance lower bound

Assume

\[
J:=I_\rho\cap[\gamma-\eta'c,\gamma+\eta'c]
\]

has length

\[
|J|\ge \kappa c
\]

for some fixed or polynomially bounded \(\kappa\ge Q^{-L}\). Then under the weighted non-cancellation condition,

\[
|u|\ge a c^{-3},
\qquad
|\Gamma_{G,2}|\ge b c^{-5}
\qquad(m\in J).
\]

Therefore

\[
\int_{I_\rho}
|u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge
\int_J |u|^2|\Gamma_{G,2}|^2\,dm.
\]

Thus

\[
\int_{I_\rho}
|u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge
a^2b^2 |J| c^{-16}
\ge
a^2b^2\kappa c^{-15}.
\]

If \(\kappa\ge Q^{-L}\), this becomes

\[
\int_{I_\rho}
|u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge
C Q^{-L} c^{-15}.
\]

In the singular regime,

\[
c<Q^{-M}
\]

for arbitrarily large \(M\). Hence for any prescribed \(A\), after choosing \(M\) large enough,

\[
Q^{-L}c^{-15}
\gg
Q^{-A}|I_\rho|
\]

as long as \(|I_\rho|\) is at most polynomially large/small in \(Q\), which is the intended good-patch scale.

So Gate 2 holds with a huge margin.

---

# 5. Packet center near but not inside \(I_\rho\)

There are three cases.

## Case 1 — comparable overlap

If

\[
|I_\rho\cap[\gamma-\eta c,\gamma+\eta c]|\ge Q^{-L}c,
\]

the theorem above still applies, with \(\kappa=Q^{-L}\). Endpoint proximity only changes constants and polynomial exponents.

## Case 2 — center outside, distance \(d\lesssim c\)

If the packet center is outside \(I_\rho\), but

\[
d:=\operatorname{dist}(\gamma,I_\rho)\le C_0c,
\]

then a one-sided packet neighborhood inside \(I_\rho\) still has comparable length provided \(I_\rho\) itself reaches into that packet scale. Again the same lower bound holds with polynomial overlap.

## Case 3 — no packet-scale overlap

If

\[
\operatorname{dist}(\gamma,I_\rho)\gg c
\]

and \(I_\rho\) does not contain any length comparable to \(c\) where the packet has size \(\asymp c^{-1}\), then the singular-packet dominance theorem in its strongest form does not apply directly.

One can still formulate a weaker version in terms of

\[
\delta:=\Delta_P(I_\rho)
=
\inf_{m\in I_\rho}\sqrt{c^2+(m-\gamma)^2}.
\]

Near the closest point,

\[
|q_P^{(r)}|\asymp c\,\delta^{-r-2}
\]

rather than \(c^{-r-1}\). If \(\delta\) is still sub-polynomially small and \(I_\rho\) contains a polynomial fraction of the corresponding variation scale \(\delta\), the same dominance mechanism works with powers of \(\delta\) and \(c\). But this endpoint/off-center case is less clean and should be treated as a separate near-endpoint singular regime.

For the attached prompt’s assumption — “center lies in or has polynomial overlap with \(I_\rho\)” — the comparable-overlap theorem is sufficient. 

---

# 6. Strongest theorem proved

Let \(P\) be a packet in \(\mathcal L_R^{\der}\) with center \(\gamma\) and scale \(c\), and suppose

\[
c<Q^{-M}
\]

for arbitrarily large \(M\). Let

\[
q=q_P+q_{\mathrm{rest}},
\qquad
q_P(m)=K_c(m-\gamma).
\]

Assume there exists a packet neighborhood

\[
J_\eta
=
I_\rho\cap[\gamma-\eta c,\gamma+\eta c]
\]

with

\[
|J_\eta|\ge Q^{-L}c.
\]

Assume also the weighted non-cancellation condition

\[
\sup_{J_\eta}
\left(
c|q_{\mathrm{rest}}|
+
c^3|q_{\mathrm{rest}}''|
+
c^5|q_{\mathrm{rest}}^{(4)}|
\right)
\le
\varepsilon_0
\]

for a sufficiently small absolute \(\varepsilon_0>0\).

Then there are constants \(a,b>0\) and a subinterval \(J\subset J_\eta\) with

\[
|J|\ge c_0Q^{-L}c
\]

such that

\[
|q''_{\can}(m)|\ge ac^{-3},
\]

and

\[
|\Gamma_{G,2}(m)|\ge bc^{-5}
\]

for all \(m\in J\). Consequently,

\[
\int_{I_\rho}
|q''_{\can}|^2
(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge
C Q^{-L}c^{-15}.
\]

In particular, for every fixed \(A\), if \(M\) is sufficiently large relative to \(A,L\), then

\[
\int_{I_\rho}
|q''_{\can}|^2
(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge
Q^{-A}|I_\rho|.
\]

So Gate 2 holds automatically in the dominant singular-packet regime.

---

# 7. What failure of dominance means

If Gate 2 fails in the presence of a sub-polynomially shallow packet with packet-scale overlap, then the weighted non-cancellation condition must fail. That is, on every packet neighborhood where \(P\) is large, at least one of

\[
c|q_{\mathrm{rest}}|,
\qquad
c^3|q_{\mathrm{rest}}''|,
\qquad
c^5|q_{\mathrm{rest}}^{(4)}|
\]

is order one or larger.

More sharply, to suppress Gate 2 one must arrange approximate cancellation not only of

\[
u_P=q_P''
\]

but also of the anisotropy combination

\[
(1-q^2)u-\frac16q^{(4)}.
\]

That requires the rest data to carry a **same-scale singular jet vector** comparable to

\[
\bigl(
c^{-1},
c^{-3},
c^{-5}
\bigr).
\]

Thus singular Gate 2 failure forces a same-scale finite-jet cancellation certificate. It is not a smooth-patch derivative-complexity failure; it is the singular version of the already identified quadrature/cancellation obstruction.

Final classification:

\[
\boxed{
\text{A single shallow packet with no same-scale jet cancellation is easy.}
}
\]

\[
\boxed{
\text{The only hard singular case is shallow same-scale cancellation.}
}
\]
## User (2026-04-26 13:56:43)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:56:45)

I’ll handle Agent 1/A only: define the unified scale-normalized packet model, translate Gate 1 into normalized source-flatness, and state the exact “no same-scale source-flattening quadrature” theorem needed.

_Thought for 22s_

Agent 1/A — unified ordinary/singular Gate 1 anti-quadrature theorem.

## 0. Verdict

The correct Gate 1 theorem is a **scale-invariant actual-zeta anti-design theorem**:

\[
\boxed{
\text{Actual zeta zero packets cannot form a same-scale finite-jet quadrature
that makes }q''_{\can}\text{ flat on }I_\rho.
}
\]

This must cover both:

\[
\text{ordinary packet scale } \lambda=d,
\]

and

\[
\text{singular/shallow packet scale } \lambda=c.
\]

After rescaling, both cases reduce to the same normalized problem. This matches the current synthesis: smooth Gate 2 is local analysis, while singular Gate 2 reduces back to Gate 1 anti-quadrature unless dominance already gives Gate 2 directly. 

---

# 1. Unified scale-normalized packet model

Let \(I_\rho\) be the packet interval attached to a hypothetical off-line packet. Choose the relevant local scale

\[
\lambda =
\begin{cases}
d, & \text{ordinary same-scale packet geometry},\\
c, & \text{singular/shallow packet geometry}.
\end{cases}
\]

Write

\[
m=m_0+\lambda x,
\]

where \(x\) is a normalized coordinate on an interval

\[
X_\rho=\lambda^{-1}(I_\rho-m_0).
\]

Typically \(X_\rho\) has length \(\asymp 1\) in the same-scale packet analysis. If the physical interval is larger, the theorem should be applied to a packet-scale subinterval with polynomial overlap.

For a packet contribution of Cauchy type,

\[
K_\lambda(m-\gamma)
=
\frac{\lambda}{(m-\gamma)^2+\lambda^2},
\]

write

\[
K_\lambda(m_0+\lambda x-\gamma)
=
\lambda^{-1} k(x-\xi),
\]

where

\[
\xi=\frac{\gamma-m_0}{\lambda},
\qquad
k(x)=\frac{1}{1+x^2}.
\]

A same-scale packet cluster therefore contributes

\[
q_{\near}(m_0+\lambda x)
=
\lambda^{-1}Q_{\near}(x),
\]

with

\[
Q_{\near}(x)=\sum_{j} w_j k_j(x),
\]

where \(w_j>0\) in the positive packet model, and \(k_j\) denotes the normalized kernel of the \(j\)-th packet, including quartet companions if required.

Then

\[
q_{\near}''(m_0+\lambda x)
=
\lambda^{-3}Q_{\near}''(x),
\]

and more generally

\[
q_{\near}^{(r)}(m_0+\lambda x)
=
\lambda^{-r-1}Q_{\near}^{(r)}(x).
\]

Thus the singular case differs only by making \(\lambda=c\) very small. The normalized equations are the same.

---

# 2. Gate 1 in normalized form

Gate 1 is

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge
Q^{-B}|I_\rho|.
\]

On a packet-scale interval \(I_\lambda=m_0+\lambda X\), with \(|X|\asymp1\), write

\[
q''_{\can}(m_0+\lambda x)
=
\lambda^{-3}F_\lambda(x),
\]

where

\[
F_\lambda(x)=Q_{\near}''(x)+F_{\rest,\lambda}(x).
\]

Then

\[
\int_{I_\lambda}|q''_{\can}(m)|^2\,dm
=
\lambda^{-5}
\int_X |F_\lambda(x)|^2\,dx.
\]

Gate 1 on \(I_\lambda\) becomes

\[
\lambda^{-5}\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda,
\]

or equivalently

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda^6.
}
\]

This is the correct scale-invariant normalized target.

If \(\lambda\ge Q^{-C_\lambda}\), then it is enough to prove

\[
\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B'}
\]

for some fixed \(B'\).

If \(\lambda\ll Q^{-C}\) for every fixed \(C\), then the threshold

\[
Q^{-B}\lambda^6
\]

is extremely small. In that singular regime, Gate 1 fails only if the normalized source curvature \(F_\lambda\) is extraordinarily flat. That is exactly the singular same-scale cancellation certificate.

---

# 3. Source flatness as finite-jet conditions

Let

\[
F_\lambda(x)=Q_{\near}''(x)+F_{\rest,\lambda}(x).
\]

Interval source-flatness means

\[
\int_X |F_\lambda(x)|^2\,dx
\ll Q^{-B}\lambda^6.
\]

A finite-jet sufficient condition for source-flatness is

\[
F_\lambda^{(r)}(x_0)
=
Q_{\near}^{(r+2)}(x_0)
+
F_{\rest,\lambda}^{(r)}(x_0)
\approx 0,
\qquad
0\le r\le R.
\]

Equivalently,

\[
Q_{\near}^{(2)}(x_0)\approx -F_{\rest,\lambda}(x_0),
\]

\[
Q_{\near}^{(3)}(x_0)\approx -F_{\rest,\lambda}'(x_0),
\]

and so on through

\[
Q_{\near}^{(R+2)}(x_0)
\approx
-F_{\rest,\lambda}^{(R)}(x_0).
\]

For a purely local packet-quadrature adversary, \(F_{\rest,\lambda}\) is another same-scale packet sum, so the obstruction becomes a finite moment/design condition among same-scale packets.

---

# 4. Minimal jet depth \(R\)

The necessary \(R\) depends on the available analytic complexity.

## Analytic-radius version

Assume \(F_\lambda\) extends holomorphically to a fixed complex neighborhood of \(X\) in normalized coordinates and satisfies

\[
\sup |F_\lambda|\le Q^C.
\]

If

\[
|F_\lambda^{(r)}(x_0)|\le Q^{-M}
\qquad
0\le r\le R,
\]

then Taylor/Cauchy bounds make \(F_\lambda\) small on a fixed subinterval once

\[
R\asymp \log Q.
\]

So the conservative jet depth is

\[
\boxed{
R=O(\log Q).
}
\]

## Band-limited / finite-frequency version

If the normalized profile has effective frequency \(O(R_0)\) and the Taylor tail is bounded by a factorial term, then

\[
R\asymp \frac{\log Q}{\log\log Q}
\]

may suffice. This is the heuristic already appearing in the prime-log recurrence discussion.

For a theorem statement, use the robust choice:

\[
\boxed{
R(Q)=C\log Q.
}
\]

For exploratory arithmetic recurrence estimates, also track the sharper possible depth:

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}.
\]

---

# 5. Same-scale quadrature equations

For ordinary same-scale positive packets one may parameterize the normalized packet locations by

\[
x_j=d\cos\theta_j,
\qquad
c_j=d\sin\theta_j,
\]

or, after rescaling,

\[
\xi_j=\cos\theta_j,
\qquad
\eta_j=\sin\theta_j.
\]

The normalized packet profile is

\[
Q_{\near}(x)=
\sum_j w_j
\frac{\eta_j}{(x-\xi_j)^2+\eta_j^2}.
\]

Source-flatness through order \(R\) at \(x_0=0\) is

\[
Q_{\near}^{(r+2)}(0)
\approx
-F_{\rest}^{(r)}(0),
\qquad
0\le r\le R.
\]

In the pure positive quadrature model with no external rest term, this becomes

\[
Q_{\near}^{(k)}(0)\approx0,
\qquad
2\le k\le R+2.
\]

The known continuous same-scale quadrature model gives an exactly constant aggregate profile, hence

\[
Q_{\near}^{(k)}(0)=0
\qquad(k\ge1),
\]

and finite positive quadrature can match this through any finite order. This is the local/Hadamard-side no-go.

Thus actual zeta arithmetic must forbid the actual zero packets from realizing, to polynomial accuracy, a configuration satisfying these finite-jet equations.

---

# 6. Unified theorem target

Here is the clean theorem to aim for.

## Actual-zeta no same-scale source-flattening quadrature

Let \(I_\rho\) be an admissible packet interval attached to a hypothetical off-line packet. Let \(\lambda\) be the relevant packet scale, either ordinary or singular, and write

\[
m=m_0+\lambda x.
\]

Let

\[
F_\lambda(x):=\lambda^3 q''_{\can}(m_0+\lambda x).
\]

Then for some constants \(B,C>0\), actual zeta data satisfy

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda^6
}
\]

on a normalized packet-scale interval \(X\) with polynomial overlap with \(I_\rho\).

Equivalently, in physical variables,

\[
\boxed{
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge
Q^{-B}|I_\rho|.
}
\]

A finite-jet version is:

For

\[
R=C\log Q
\]

or, if justified,

\[
R\asymp \frac{\log Q}{\log\log Q},
\]

one has

\[
\boxed{
\max_{0\le r\le R}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B}\lambda^3
}
\]

in the normalization strong enough to imply the interval estimate. More invariantly, one should state it as:

\[
\boxed{
\text{Actual zeta packets cannot satisfy}
\quad
\partial_x^rF_\lambda(x_0)=O(Q^{-M}\lambda^3)
\quad(0\le r\le R)
}
\]

for arbitrarily large \(M\), on an admissible off-line packet interval.

The theorem must cover:

1. ordinary same-scale packets with \(\lambda=d\);
2. singular/shallow packets with \(\lambda=c\);
3. finite positive quadrature approximations;
4. quartet-closed packet sets;
5. background, tail, and dual/AFE terms in the canonical \(q''_{\can}\) convention.

---

# 7. What is local geometry vs. arithmetic?

## Purely local geometry

Local geometry alone permits source flattening.

Specifically, positive same-scale packet measures can make the normalized aggregate profile constant near the center:

\[
Q_{\near}(x)\equiv \text{constant}
\]

to arbitrary finite jet order. Hence

\[
Q_{\near}''(0)=Q_{\near}^{(3)}(0)=\cdots=Q_{\near}^{(R+2)}(0)=0.
\]

By finite quadrature, this can be realized with finitely many positive packets.

This remains true after singular rescaling: the powers of \(\lambda^{-1}\) factor out, and the normalized equations are unchanged.

So local packet positivity, quartet symmetry, same-scale geometry, and finite Hadamard constraints do **not** prove Gate 1.

## Actual-zeta arithmetic

The required arithmetic input is that actual zeta zeros cannot arrange themselves into the needed same-scale finite design.

This could come from:

- zero-side arithmetic constraints on actual zero ordinates and off-critical depths;
- prime/AFE fixed-coefficient nonrecurrence;
- a trace/Weil positivity theorem;
- or some currently unknown source-robust global invariant.

But it cannot come from the local packet model alone.

---

# 8. Would this theorem close Gate 1 in all regimes?

Yes, modulo canonical decomposition/error bookkeeping.

If the no same-scale source-flattening theorem is proved for the full canonical object

\[
q''_{\can}=q_\zeta'',
\]

then Gate 1 holds in both ordinary and singular packet scales:

\[
\int_{I_\rho}|q''_{\can}|^2\,dm
\ge Q^{-B}|I_\rho|.
\]

Then Gate 2 follows by the current two-regime analysis:

- in the smooth denominator-separated regime, Gate 1 plus derivative complexity gives Gate 2;
- in the singular regime, dominance gives Gate 2 unless there is same-scale cancellation;
- same-scale cancellation is precisely ruled out by the unified Gate 1 anti-quadrature theorem.

So the current route reduces to:

\[
\boxed{
\text{Prove actual-zeta no same-scale source-flattening quadrature.}
}
\]

This is now the central missing arithmetic theorem.
## User (2026-04-26 14:02:08)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:02:28)

_Thought for 18s_

Agent 1/A — unified Gate 1 theorem, formal version.

## 1. Rescaling Gate 1

Let

\[
I_\rho=m_0+\lambda X,
\]

where \(X\subset\mathbb R\) is a normalized interval and

\[
m=m_0+\lambda x.
\]

The scale is

\[
\lambda=d
\]

in the ordinary same-scale packet regime, and

\[
\lambda=c
\]

in the singular/shallow-packet regime. Define

\[
F_\lambda(x):=\lambda^3 q''_{\can}(m_0+\lambda x).
\]

Then

\[
q''_{\can}(m_0+\lambda x)=\lambda^{-3}F_\lambda(x),
\qquad
dm=\lambda\,dx.
\]

Therefore

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
=
\lambda^{-5}\int_X |F_\lambda(x)|^2\,dx.
\]

Gate 1,

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|,
\]

is equivalent to

\[
\lambda^{-5}\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda |X|.
\]

Thus the normalized form is

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda^6 |X|.
}
\]

Equivalently,

\[
\boxed{
|X|^{-1}\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda^6.
}
\]

This is the correct unified ordinary/singular scaling. The current strategic notes use exactly this normalization: \(F_\lambda(x)=\lambda^3q''_{\can}(m_0+\lambda x)\), and Gate 1 becomes the normalized anti-design lower bound \(\int_X |F_\lambda|^2\ge Q^{-B}\lambda^6\). 

---

## 2. Normalized interval \(X\)

The clean formulation should require a normalized interval

\[
X\subset[-C_0,C_0],
\qquad
|X|\ge Q^{-C_X},
\]

with \(C_0\) fixed and \(C_X\) polynomially bounded.

The most natural case is

\[
|X|\asymp1,
\]

meaning \(I_\rho\) has genuine packet-scale overlap. But allowing

\[
|X|\ge Q^{-C_X}
\]

is safer because packet centers may lie near endpoints, especially in singular/shallow regimes.

Then the normalized Gate 1 target is

\[
\boxed{
\int_X |F_\lambda|^2\,dx
\ge
Q^{-B}\lambda^6 |X|.
}
\]

If \(|X|\asymp1\), this is simply

\[
\int_X |F_\lambda|^2\,dx
\ge
Q^{-B}\lambda^6.
\]

---

## 3. Finite-jet version

Let \(x_0\in X\), and let \(R=R(Q)\). The conservative analytic choice is

\[
R(Q)=C\log Q.
\]

A sharper but less robust choice is

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}.
\]

The finite-jet Gate 1 theorem should be stated as a **nonflatness alternative**:

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B_{\jet}}\lambda^3.
}
\]

The \(\lambda^3\) threshold is the natural one because \(F_\lambda=\lambda^3q''_{\can}\), and physical Gate 1 is an \(L^2\)-lower bound for \(q''_{\can}\). More invariantly, one can state the jet theorem in normalized \(L^2\) units:

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B_{\jet}}
\left(
\lambda^6 |X|
\right)^{1/2}
=
Q^{-B_{\jet}}\lambda^3 |X|^{1/2}.
}
\]

If \(|X|\asymp1\), this reduces to

\[
\max_{0\le r\le R(Q)}
|\partial_x^rF_\lambda(x_0)|
\ge
Q^{-B_{\jet}}\lambda^3.
\]

A practical theorem should include analytic-complexity assumptions in normalized coordinates. For example, if \(F_\lambda\) is holomorphic on a fixed complex neighborhood of \(X\) and has polynomial growth there, then failure of the \(L^2\) lower bound forces a finite jet at some interior \(x_0\) to be tiny through \(R=O(\log Q)\). Conversely, a finite-jet nonflatness theorem at every admissible packet center gives the interval lower bound by standard Taylor/Cauchy propagation.

The current project notes identify this exact finite-jet obstruction: source flatness corresponds to \(\partial_x^rF_\lambda(x_0)\approx0\) for \(0\le r\le R(Q)\), with \(R(Q)\asymp \log Q/\log\log Q\) or conservatively \(O(\log Q)\). 

---

## 4. Correct threshold dependence

Let

\[
I_\rho=m_0+\lambda X.
\]

Then

\[
|I_\rho|=\lambda |X|.
\]

The physical Gate 1 lower bound is

\[
\int_{I_\rho}|q''_{\can}|^2\,dm
\ge Q^{-B}\lambda |X|.
\]

The normalized equivalent is

\[
\int_X |F_\lambda|^2\,dx
\ge Q^{-B}\lambda^6|X|.
\]

Thus the normalized \(L^2\)-norm threshold is

\[
\|F_\lambda\|_{L^2(X)}
\ge Q^{-B/2}\lambda^3|X|^{1/2}.
\]

Accordingly, any finite-jet lower bound strong enough to imply Gate 1 should have threshold at least

\[
Q^{-B_{\jet}}\lambda^3|X|^{1/2}.
\]

If \(|X|\ge Q^{-C_X}\), this can be simplified to

\[
Q^{-B'_{\jet}}\lambda^3.
\]

So the clean polynomial form is:

\[
\boxed{
\max_{0\le r\le R(Q)}
|\partial_x^rF_\lambda(x_0)|
\ge
Q^{-B'}\lambda^3.
}
\]

For ordinary scales with \(\lambda\ge Q^{-C_\lambda}\), this is a purely polynomial lower bound.

For singular scales with \(\lambda\ll Q^{-C}\) for every fixed \(C\), the right-hand side becomes extremely small. That is correct: singular Gate 1 can fail only under very accurate normalized cancellation. Without such cancellation, singular packets create large source curvature and hence no Gate 1 problem.

---

## 5. Ordinary-variable theorem

A clean ordinary-variable Gate 1 theorem is:

\[
\boxed{
\textbf{Actual-zeta source-curvature observability.}
}
\]

For every admissible packet interval \(I_\rho\), attached either to an ordinary same-scale packet or to a singular/shallow packet, there exists \(B>0\) such that

\[
\boxed{
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
}
\]

Here

\[
q''_{\can}=q_\zeta''=\Phi_\zeta'''
\]

is the full canonical actual-zeta phase curvature. The theorem must apply after all core, tail, background, and regularized completed-factor contributions are included in the canonical \(q''_{\can}\).

Equivalently, it says: actual zeta does not allow the distinguished packet contribution to be cancelled by the rest of the actual zero/background/prime data so accurately that \(q''_{\can}\) is source-flat on \(I_\rho\).

---

## 6. Normalized theorem

The scale-normalized version is sharper.

Let \(\lambda\) be the packet scale, with

\[
\lambda=d
\]

in the ordinary regime and

\[
\lambda=c
\]

in the singular regime. Let

\[
I_\rho=m_0+\lambda X,
\qquad
|X|\ge Q^{-C_X}.
\]

Define

\[
F_\lambda(x)=\lambda^3q''_{\can}(m_0+\lambda x).
\]

Then actual zeta data satisfy

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge Q^{-B}\lambda^6|X|.
}
\]

Finite-jet version:

There are constants \(B_{\jet},C_R>0\) such that for

\[
R(Q)=C_R\log Q
\]

—or, if justified by the analytic complexity model,

\[
R(Q)\asymp\frac{\log Q}{\log\log Q},
\]

one has, at every admissible packet center \(x_0\),

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B_{\jet}}\lambda^3|X|^{1/2}.
}
\]

If \(|X|\asymp1\), this is

\[
\boxed{
\max_{0\le r\le R(Q)}
|\partial_x^rF_\lambda(x_0)|
\ge Q^{-B_{\jet}}\lambda^3.
}
\]

This is the formal “no same-scale source-flattening finite-jet quadrature” statement.

---

## 7. Same-scale packet model

In normalized variables, a same-scale packet cluster has the form

\[
q_{\near}(m_0+\lambda x)=\lambda^{-1}Q_{\near}(x),
\]

so

\[
q_{\near}''(m_0+\lambda x)=\lambda^{-3}Q_{\near}''(x).
\]

Thus the near-packet part of \(F_\lambda\) is

\[
F_{\near,\lambda}(x)=Q_{\near}''(x).
\]

Source flatness is

\[
F_\lambda(x)=Q_{\near}''(x)+F_{\rest,\lambda}(x)\approx0
\]

on \(X\), or in finite-jet form,

\[
Q_{\near}^{(r+2)}(x_0)
+
F_{\rest,\lambda}^{(r)}(x_0)
\approx0,
\qquad
0\le r\le R(Q).
\]

In the pure local quadrature model where \(F_{\rest,\lambda}\) is another same-scale packet sum, this becomes a same-scale finite-design condition.

The important point is that the equations do not fundamentally depend on whether \(\lambda=d\) or \(\lambda=c\). The singular powers factor out. This is why the singular Gate 2 failure reduces to the same source-flat quadrature obstruction in normalized variables. 

---

## 8. Actual-zeta no same-scale source-flattening theorem

The final theorem should be stated as follows.

\[
\boxed{
\textbf{No same-scale source-flattening quadrature for actual zeta.}
}
\]

Let \(I_\rho=m_0+\lambda X\) be an admissible packet interval, ordinary or singular, and define

\[
F_\lambda(x)=\lambda^3q''_{\can}(m_0+\lambda x).
\]

Then actual zeta data cannot satisfy a same-scale finite-jet cancellation system

\[
\partial_x^rF_\lambda(x_0)
=
O(Q^{-M}\lambda^3|X|^{1/2}),
\qquad
0\le r\le R(Q),
\]

for arbitrarily large \(M\), on an admissible off-line packet interval. Equivalently, for some fixed \(B\),

\[
\int_X |F_\lambda(x)|^2\,dx
\ge Q^{-B}\lambda^6|X|.
\]

This theorem must cover:

1. ordinary same-scale packets;
2. singular/shallow same-scale packets;
3. finite positive quadrature approximations;
4. quartet-closed packet sets;
5. the complete canonical object \(q''_{\can}\), including background, tail, dual/AFE, and regularization terms.

The reason actual arithmetic is necessary is that local same-scale positive packet geometry can make \(Q_{\near}\) locally constant to arbitrary finite order, so local geometry alone can force

\[
Q_{\near}''=Q_{\near}^{(3)}=\cdots=0
\]

to finite order. Known zero-side local inputs do not currently rule this out. 

---

## 9. Why this closes Gate 1 in all regimes

If the normalized theorem holds, then immediately

\[
\int_X |F_\lambda|^2\,dx
\ge Q^{-B}\lambda^6|X|.
\]

By the rescaling identity,

\[
\int_{I_\rho}|q''_{\can}|^2\,dm
=
\lambda^{-5}\int_X |F_\lambda|^2\,dx,
\]

so

\[
\int_{I_\rho}|q''_{\can}|^2\,dm
\ge
\lambda^{-5}Q^{-B}\lambda^6|X|
=
Q^{-B}\lambda|X|
=
Q^{-B}|I_\rho|.
\]

That is exactly Gate 1.

It covers the smooth regime because \(\lambda=d\) and the interval is ordinary same-scale.

It covers the singular regime because \(\lambda=c\), and the singular powers have been absorbed into \(F_\lambda\). If a shallow packet is not cancelled, Gate 1 is much stronger than needed. If it is cancelled, the cancellation is exactly a same-scale source-flattening design in \(F_\lambda\), which the theorem forbids.

So the clean reduction is:

\[
\boxed{
\text{No same-scale source-flattening for actual zeta}
\Rightarrow
\text{Gate 1 in ordinary and singular regimes}.
}
\]

Given the current status—that Gate 2 is local/singular analysis once Gate 1 is supplied—the unified Gate 1 theorem is now the central arithmetic theorem of the whole route.
## User (2026-04-26 14:06:02)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:06:53)

_Thought for 50s_

Agent 1/A — zero-side anti-design theorem.

## Verdict

\[
\boxed{
\text{Zero-side local constraints are insufficient.}
}
\]

A purely zero-side proof of Gate 1 is not currently credible unless it introduces a genuinely new **actual-zeta anti-design theorem**. The local same-scale packet model can satisfy the finite moment conditions needed to flatten \(q''_{\can}\), and the known constraints—Riemann–von Mangoldt counting, zero-density, pair correlation, quartet symmetry, simplicity, and the functional equation—do not rule this out at the required finite-jet accuracy.

This matches the current project status: Gate 1 is now the central missing theorem, and the same-scale quadrature obstruction is the key local no-go. 

---

# 1. Actual-zeta zeros as a constrained same-scale packet design

In normalized packet coordinates, write

\[
m=m_0+\lambda x,
\qquad
F_\lambda(x)=\lambda^3 q''_{\can}(m_0+\lambda x).
\]

A same-scale zero packet contributes a normalized Cauchy/Poisson-type kernel

\[
K_\theta(x)
=
\frac{\sin\theta}{(x-\cos\theta)^2+\sin^2\theta},
\qquad
0<\theta<\pi.
\]

The same-scale packet cluster has the form

\[
Q(x)=\sum_{j=1}^N w_j K_{\theta_j}(x),
\qquad
w_j>0.
\]

The exact normalization can vary by harmless constants, but the crucial identity is

\[
K_\theta^{(n)}(0)=n!\sin((n+1)\theta).
\]

Thus source flattening through finite jet order means imposing trigonometric moment conditions.

Actual zeta zeros impose the following zero-side constraints beyond arbitrary positivity:

1. **Functional-equation quartet closure.** If \(\rho\) occurs, then the symmetry partners \(\bar\rho,1-\rho,1-\bar\rho\) occur.
2. **Integer multiplicity / simplicity.** For simple zeros the packet weights are not continuously tunable in a literal zero model; however, finite positive weights can be approximated by clusters of nearby simple packets unless one has a strong spacing theorem forbidding such clusters.
3. **Riemann–von Mangoldt counting.** The number of zeros in a height window is controlled by the usual local counting estimates.
4. **Zero-density constraints.** Off-line packets are constrained in aggregate by density estimates, but these are too coarse to exclude \(O(R)\) packets in a small finite design unless the design requires many deeply off-line zeros.
5. **Pair-spacing constraints.** Known pair-correlation information is either conjectural, averaged, or too weak to forbid a deterministic finite cluster.
6. **Global arithmetic compatibility.** Actual zeros must be compatible with the Euler product / explicit formula. This is not a local zero-geometry constraint; it is exactly the arithmetic input currently missing.

So the actual-zero design problem is a finite positive trigonometric moment problem with quartet closure and counting constraints, plus a global arithmetic compatibility condition. The first group of constraints does not exclude flattening.

---

# 2. Moment equations for source flattening

Since

\[
Q^{(n)}(0)
=
n!\sum_{j=1}^N w_j\sin((n+1)\theta_j),
\]

the conditions

\[
Q''(0)\approx0,\quad
Q^{(3)}(0)\approx0,\quad
\ldots,\quad
Q^{(R+2)}(0)\approx0
\]

become

\[
\sum_{j=1}^N w_j\sin(k\theta_j)\approx0,
\qquad
3\le k\le R+3.
\]

If we only require even curvature jets,

\[
Q''(0),\ Q^{(4)}(0),\ldots,Q^{(2M)}(0)
\]

to vanish, the conditions become

\[
\sum_{j=1}^N w_j\sin((2\ell+1)\theta_j)\approx0,
\qquad
1\le \ell\le M.
\]

This is precisely the finite moment system appearing in the current handoff. 

A background/tail/core contribution \(\mathcal B_k\) modifies the equations to

\[
\sum_{j=1}^N w_j\sin(k\theta_j)+\mathcal B_k\approx0,
\qquad
3\le k\le R+3.
\]

A zero-side anti-design theorem would need to show

\[
\max_{3\le k\le R+3}
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}
\]

for actual zeta zero packets. I do not see a known zero-side theorem that gives this.

---

# 3. Why known zero-side theorems do not rule this out

## Riemann–von Mangoldt counting

A finite quadrature needs only

\[
N=O(R)
\]

nodes, with

\[
R\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R=O(\log Q).
\]

Local zero-counting bounds near height \(T\) do not prohibit \(O(R)\) zeros in a relevant packet window, especially when \(Q\) is polylogarithmic in \(T\). Riemann–von Mangoldt counting controls the number of zeros, not their finite trigonometric moment design.

## Zero-density estimates

Zero-density estimates restrict how many zeros can lie off the critical line in large regions. They do not rule out a small finite quartet-closed packet cluster arranged to satisfy \(O(R)\) moment equations, unless the design requires an off-line population far exceeding density bounds. The quadrature adversary only needs \(O(R)\) nodes.

## Pair correlation / spacing

Pair correlation, even if assumed, is an averaged statistical statement. It does not forbid a deterministic exceptional finite cluster at one height. Known rigorous pair-spacing results are much weaker than what would be required to exclude a finite same-scale design.

## Quartet symmetry

Quartet symmetry is compatible with the construction. One simply symmetrizes the node set. Symmetrization changes the moment equations but does not remove the design degrees of freedom.

## Simplicity

Simplicity only prevents exact multiplicity at one point. It does not prevent replacing a weighted node by several nearby simple nodes. Perturbing nodes slightly preserves moment matching to polynomial accuracy.

## Functional equation

The functional equation enforces the quartet structure and global symmetry. It does not by itself impose a local anti-design inequality of the form

\[
\max_k\left|\sum_j w_j\sin(k\theta_j)+\mathcal B_k\right|\ge Q^{-B}.
\]

The arithmetic force of the functional equation appears through the explicit formula / primes, not through local zero geometry alone.

---

# 4. Concrete finite packet countermodel

The known local countermodel is already strong. Define a positive continuous same-scale measure on

\[
x^2+c^2=d^2
\]

using

\[
d\mu(\theta)=\frac{2}{\pi}\sin\theta\,d\theta.
\]

For the normalized kernel \(K_\theta\),

\[
\int_0^\pi K_\theta(x)\,d\mu(\theta)
\]

is constant near the midpoint. Equivalently,

\[
\int_0^\pi K_\theta^{(n)}(0)\,d\mu(\theta)=0
\qquad(n\ge1),
\]

because

\[
K_\theta^{(n)}(0)=n!\sin((n+1)\theta)
\]

and

\[
\int_0^\pi \sin((n+1)\theta)\sin\theta\,d\theta=0
\qquad(n\ge1).
\]

Therefore,

\[
Q''(0)=Q^{(3)}(0)=\cdots=Q^{(R+2)}(0)=0
\]

for every finite \(R\).

By Tchakaloff/Carathéodory finite quadrature, for any finite \(R\) this continuous positive measure can be replaced by finitely many positive nodes

\[
\{(\theta_j,w_j)\}_{j=1}^{N_R}
\]

with

\[
N_R\le R+O(1)
\]

or at worst \(N_R=O(R)\), such that

\[
\sum_j w_j\sin(k\theta_j)=0
\qquad
3\le k\le R+3.
\]

This gives a finite same-scale positive packet design satisfying the source-flat finite-jet equations exactly.

Now enforce the standard local zero-side constraints:

- **Quartet symmetry:** include the symmetry companions of each packet. This increases \(N_R\) by a bounded factor.
- **Simplicity:** replace a weighted node by nearby distinct simple nodes with rational approximating weights. Moment errors remain \(O(Q^{-M})\) if the perturbations are sufficiently small.
- **Counting:** choose \(N_R=O(R)\), which is compatible with known local counting bounds at the level currently used.
- **Endpoint/core gap/Gram positivity:** choose the packet shell away from endpoints and with positive weights; these are open conditions and survive small perturbations.
- **Riemann–von Mangoldt-like density:** distribute the finite packets inside a local window without violating crude zero-counting.

Thus there is a finite packet countermodel satisfying the currently named local zero-side constraints and making

\[
F_\lambda(x)
\]

finite-jet flat to order \(R\). This is not a zeta zero set; it is a local zero-side model. But it proves that **local zero-side constraints alone cannot imply Gate 1**. The earlier shared background states the same local no-go: same-scale positive packet geometry can flatten \(q''\) and higher source jets while preserving \(q_0>0\), Gram positivity, and live anisotropy. 

---

# 5. Why the proposed lower bound cannot be local

The desired local lower bound would be

\[
\max_{3\le k\le R+3}
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}.
\]

But the finite quadrature construction gives

\[
\sum_j w_j\sin(k\theta_j)=0
\]

for all \(3\le k\le R+3\), and more generally finite positive quadrature can match prescribed finite moment vectors within a neighborhood of zero. If \(\mathcal B_k\) is itself only locally constrained, one can absorb it into an enlarged finite packet design or adjust the auxiliary/background model within the currently allowed local freedoms.

So a lower bound of this form cannot follow from:

\[
\text{positivity}+\text{quartet symmetry}+\text{simplicity}+\text{local counting}.
\]

It would need actual zeta arithmetic, for example:

- prime/AFE fixed-coefficient rigidity;
- a global trace/Weil-positive obstruction;
- a theorem linking zero locations to prime-log phases strongly enough to prevent finite trigonometric designs.

---

# 6. Exact missing zero-side theorem

The missing theorem would need to say something like:

\[
\boxed{
\textbf{Actual-zeta zero anti-design theorem.}
}
\]

Let \(I_\rho=m_0+\lambda X\) be an admissible ordinary or singular packet interval attached to a hypothetical off-line packet. Let the actual zeta zero packets in the relevant same-scale shell define normalized coordinates

\[
(\theta_j,w_j)
\]

together with canonical background/tail moments \(\mathcal B_k\). Then for

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R(Q)=O(\log Q),
\]

there exist \(B>0\) and some

\[
3\le k\le R(Q)+3
\]

such that

\[
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}.
\]

Equivalently,

\[
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge Q^{-B}\lambda^3|X|^{1/2}.
\]

Or in interval form,

\[
\int_X |F_\lambda(x)|^2\,dx
\ge Q^{-B}\lambda^6|X|.
\]

This theorem must be about **actual zeta zeros**, not arbitrary quartet-closed same-scale packet configurations.

---

# 7. Does zero-side arithmetic suffice?

At the level of known zero-side results: no.

A purely zero-side proof would require a new deterministic anti-design theorem for actual zeta zeros, significantly stronger than standard counting, density, spacing, simplicity, or quartet-symmetry statements.

So the realistic conclusion is:

\[
\boxed{
\text{The zero-side route requires a new anti-design theorem.}
}
\]

If such a theorem can be proved, it would close Gate 1 directly. But it is not derivable from current local zero geometry.

Given the current state, actual-zeta arithmetic probably must enter through one of:

1. **Prime/AFE fixed-coefficient nonrecurrence**, proving that the prime-log phase flow cannot simultaneously create an off-line packet and source-flat jets;
2. **Global trace / Weil-positive obstruction**, if a packet-adapted positive form can be found;
3. **A genuinely new zero-prime compatibility theorem**, converting Euler-product rigidity into a zero-side anti-design inequality.

---

# 8. Final classification

\[
\boxed{
\text{Zero-side local constraints are insufficient.}
}
\]

More precisely:

- The finite moment system

\[
\sum_j w_j\sin(k\theta_j)\approx0,
\qquad
3\le k\le R+3,
\]

is locally feasible with \(O(R)\) positive same-scale packets.

- Known actual-zero constraints do not forbid such a finite design to polynomial accuracy.

- A local finite packet countermodel can satisfy quartet symmetry, simplicity-by-splitting, same-scale geometry, local counting, core-gap, endpoint separation, Gram positivity, and live anisotropy.

- Therefore Gate 1 cannot be proved from local zero-side geometry alone.

The correct status is:

\[
\boxed{
\text{zero-side route requires a new actual-zeta anti-design theorem;}
}
\]

otherwise the proof must use prime/AFE nonrecurrence or a global trace/Weil-type arithmetic input.
## User (2026-04-26 14:10:28)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:10:41)

_Thought for 10s_

Agent 1/A — zero-side anti-design, sharpened to actual-zeta constraints.

## Verdict

Known zero-side arithmetic **does not currently rule out** the same-scale finite-jet design needed to defeat Gate 1.

It gives partial restrictions in some regimes, especially if the quadrature requires many zeros far from the critical line or near \(\Re s=1\). But the dangerous design can use only

\[
N=O(R(Q))
\]

packets, with

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R(Q)=O(\log Q),
\]

and can be arranged in shallow/near-critical or same-scale local clusters. Existing zero-density, zero-free, spacing, quartet, and simplicity inputs do not exclude that at polynomial accuracy.

So the zero-side route still requires a genuinely new theorem:

\[
\boxed{
\text{actual zeta zeros cannot realize same-scale source-flattening finite designs.}
}
\]

This is exactly the Gate 1 arithmetic bottleneck identified in the coordinator prompt. 

---

# 1. Constraints actual zeta zeros impose beyond the abstract packet model

The abstract packet model assumes positive same-scale packets satisfying moment equations

\[
\sum_j w_j\sin(k\theta_j)\approx-\mathcal B_k,
\qquad 3\le k\le R+3.
\]

Actual zeta adds these constraints:

1. **Riemann–von Mangoldt counting.**  
   The number of zero ordinates in a window of length \(H\) near height \(T\) is constrained by

   \[
   N(T+H)-N(T-H)\approx \frac{H}{\pi}\log \frac{T}{2\pi}+O(\log T).
   \]

   This controls population size, not finite trigonometric moment cancellation.

2. **Zero-free region.**  
   Zeta has no zeros very close to \(\Re s=1\), with classical zero-free regions of de la Vallée Poussin type. This only blocks packets whose construction needs zeros extremely close to the edge \(\Re s=1\). It does not block zeros near the critical line or modest off-line quartets.

3. **Zero-density estimates.**  
   Bounds for

   \[
   N(\sigma,T)
   =
   \#\{\rho:\Re\rho\ge\sigma,\ |\Im\rho|\le T\}
   \]

   restrict how many zeros can lie far to the right of the critical line. They become much weaker near \(\sigma=1/2\), exactly where shallow off-line packets would live.

4. **Functional-equation quartet symmetry.**  
   Actual off-line zeros occur in symmetry quartets

   \[
   \rho,\quad \bar\rho,\quad 1-\rho,\quad 1-\bar\rho.
   \]

   The local packet construction can be quartet-closed. This symmetry does not prevent moment cancellation.

5. **Simplicity or bounded multiplicity.**  
   Simplicity prevents literal repeated nodes. It does not prevent replacing a weighted packet by a small cluster of nearby simple packets, preserving finitely many moments to polynomial accuracy.

6. **Pair correlation / spacing.**  
   Pair-correlation information is averaged and largely conditional at the needed level. It does not forbid a deterministic exceptional finite cluster at one height.

7. **Explicit formula compatibility.**  
   This is the serious condition. But once we use the explicit formula, we are no longer in a purely zero-side local argument; we are importing prime/AFE or global trace arithmetic. That is likely necessary.

---

# 2. Can known constraints rule out the finite moment system?

The finite moment system is

\[
\sum_j w_j\sin(k\theta_j)\approx-\mathcal B_k,
\qquad 3\le k\le R+3.
\]

A positive quadrature design with \(O(R)\) nodes can solve such equations to high finite order in the abstract packet model.

Known zero-side constraints do not rule it out:

## Counting does not rule it out

The design needs only \(O(R)\) nodes. Even with

\[
R=O(\log Q),
\]

this is tiny compared with the error tolerance of many local zero-counting estimates near height \(T\). If \(Q\) is polylogarithmic in \(T\), then \(O(\log Q)\) packets are not excluded by Riemann–von Mangoldt local bounds.

Counting can rule out designs requiring too many zeros in a very short interval, but the current quadrature adversary does not inherently require a population beyond known bounds.

## Zero-density only helps far from the critical line

If the design required many zeros with

\[
\Re\rho\ge \frac12+\eta
\]

for a fixed \(\eta>0\), then zero-density estimates could become meaningful. But the dangerous singular/shallow regime can place packets close to the critical line, where density estimates do not give a strong exclusion without something close to RH itself.

So zero-density partially helps only in a **deep off-critical regime**, not in the main shallow same-scale regime.

## Zero-free regions only exclude edge packets

The classical zero-free region prevents zeros too close to \(\Re s=1\), but the quadrature can be built away from that edge. The obstruction is not forced to use near-\(1\) zeros.

## Quartet symmetry is compatible

Because

\[
\sin(k\theta)
\]

moment equations are linear, one can enforce quartet closure by adding symmetry partners and solving the resulting symmetrized linear system. This changes the admissible basis but not the basic feasibility.

## Simplicity is compatible

Weighted quadrature nodes can be approximated by multiple nearby simple zeros. The finite moment conditions are stable under small perturbations. Therefore simplicity does not exclude polynomial-accuracy cancellation.

## Pair correlation is too weak

Pair correlation is a statistical input and, in the strength usually available, cannot forbid one exceptional \(O(R)\)-packet design. A theorem strong enough to forbid this would be a new deterministic local rigidity theorem for zeta zeros.

---

# 3. Off-critical depths needed by the quadrature

In normalized ordinary same-scale coordinates, one may write

\[
x_j=\cos\theta_j,
\qquad
c_j=\sin\theta_j,
\]

so each packet lies on a common scale shell

\[
x_j^2+c_j^2=1.
\]

The quadrature density used in the local no-go has support on

\[
0<\theta<\pi,
\]

with weights comparable to

\[
\sin\theta\,d\theta.
\]

This includes a range of depths:

\[
c_j=\sin\theta_j.
\]

Finite quadrature nodes can be chosen away from the endpoints

\[
\theta=0,\pi,
\]

so the normalized depths can be bounded below by a fixed constant if desired. In physical variables, this means depths comparable to the packet scale \(\lambda\).

In the singular version, \(\lambda=c\) may itself be sub-polynomially small, but after rescaling the normalized depths are again \(O(1)\). Thus the singular construction does not require extreme normalized degeneracy; it only requires a same-scale cluster at a tiny physical scale.

Known zero-density estimates do not rule out an \(O(R)\)-sized cluster at such a scale unless the physical depths are far enough from the critical line to fall under strong density constraints. The most dangerous case is shallow near-critical clustering, where zero-density has little force.

---

# 4. Is singular/shallow quadrature easier or harder for actual zeta?

From local geometry, singular quadrature is **scale-invariant**. Set

\[
m=\gamma+c x.
\]

Then

\[
q_{\near}(m)=c^{-1}Q(x),
\qquad
q_{\near}''(m)=c^{-3}Q''(x).
\]

The large powers of \(c^{-1}\) factor out. The finite-jet equations for cancellation are the same equations in \(Q\).

So, locally, singular quadrature is neither harder nor easier; it is the same normalized design.

For actual zeta, singular quadrature may be constrained by:

- availability of zeros at very small transverse depth;
- local spacing around the ordinate;
- compatibility with zero-density near \(\Re s=1/2+\epsilon\);
- explicit formula / prime-side effects.

But none of the standard zero-side estimates provides a deterministic exclusion of an \(O(R)\)-node shallow same-scale design.

Thus singular quadrature is not ruled out by known zero-side arithmetic. It becomes a prime/explicit-formula compatibility problem.

---

# 5. Partial regimes where known zero-side arithmetic helps

There are limited regimes where known zero-side estimates could help.

## Deep off-critical packet regime

If every packet in the design has depth corresponding to

\[
\Re\rho\ge \frac12+\eta
\]

for fixed \(\eta>0\), and the design requires \(O(R)\) such zeros in a very short height window, then zero-density estimates may constrain the design.

But this does not cover shallow packets with \(\eta\to0\), which are RH-relevant.

## Near-\(\Re s=1\) regime

The zero-free region excludes packets too close to \(\Re s=1\). But the quadrature construction does not require such zeros.

## Excessive node-count regime

If one could prove the quadrature needs far more than \(O(R)\) nodes under actual zeta constraints, local counting could rule it out. But abstract positive quadrature already gives \(O(R)\), and quartet closure only multiplies by a constant.

So the known constraints partially help only in named, non-central regimes. They do not close Gate 1.

---

# 6. Exact strengthened zero-side theorem needed

A usable zero-side theorem would be:

\[
\boxed{
\textbf{Actual-zeta same-scale anti-design theorem.}
}
\]

Let \(I_\rho=m_0+\lambda X\) be an admissible ordinary or singular packet interval, and let the same-scale actual zero packets in the relevant shell have normalized parameters

\[
(\theta_j,w_j).
\]

Let \(\mathcal B_k\) denote the canonical contribution of background, tail, nonshell packets, and regularization to the normalized source-curvature moments. Then for

\[
R(Q)=O(\log Q)
\]

or

\[
R(Q)\asymp\frac{\log Q}{\log\log Q},
\]

there exist constants \(B>0\) and \(3\le k\le R(Q)+3\) such that

\[
\boxed{
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}.
}
\]

Equivalently, in normalized physical form,

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B}\lambda^3|X|^{1/2}.
}
\]

Or in interval form,

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge
Q^{-B}\lambda^6|X|.
}
\]

This theorem must use actual zeta arithmetic, not merely local packet geometry.

---

# 7. Final verdict

\[
\boxed{
\text{Known zero-side arithmetic only partially helps in deep off-critical or edge regimes.}
}
\]

\[
\boxed{
\text{It does not rule out the core same-scale finite-design obstruction.}
}
\]

Therefore:

\[
\boxed{
\text{The zero-side route requires a new actual-zeta anti-design theorem.}
}
\]

A purely local zero-side proof of Gate 1 is not plausible with currently identified inputs. The next serious attack should either:

1. prove this new zero-side anti-design theorem using explicit-formula compatibility;
2. move to the prime/AFE fixed-coefficient nonrecurrence route;
3. or seek a global trace/Weil-positive obstruction.
## User (2026-04-26 14:16:15)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:16:17)

I’ll execute Agent 1/A: focus only on zero-side actual-zeta rigidity beyond the abstract packet model, and classify whether any known zero-side theorem can plausibly prove Gate 1.

_Thought for 14s_

Agent 1/A — zero-side anti-design: actual-zeta rigidity search.

## Verdict

\[
\boxed{
\text{Known zero-side arithmetic does not presently prove Gate 1.}
}
\]

The zero-side local model can satisfy the same-scale source-flattening moment equations with only \(O(R)\) packets, and the known constraints on actual zeta zeros do not exclude that finite design at polynomial accuracy. The zero-side route remains possible only if we prove a **new actual-zeta anti-design theorem** linking zero locations, off-critical depths, and background/tail moments more rigidly than current zero-counting, zero-density, quartet symmetry, simplicity, or pair-correlation inputs do. The attached prompt identifies Gate 1 as the decisive bottleneck and asks specifically for actual-zeta rigidity beyond the abstract packet model. 

---

# 1. Actual-zeta constraints beyond the abstract packet model

The abstract local packet model treats same-scale packets as freely placeable positive nodes

\[
Q(x)=\sum_j w_jK_{\theta_j}(x),
\qquad
K_\theta(x)=\frac{\sin\theta}{(x-\cos\theta)^2+\sin^2\theta}.
\]

The source-flat moment equations are

\[
\sum_j w_j\sin(k\theta_j)\approx -\mathcal B_k,
\qquad 3\le k\le R+3.
\]

Actual zeta adds these constraints:

\[
\text{functional-equation quartet closure},
\]

\[
\text{integer multiplicity, expected simplicity},
\]

\[
\text{Riemann--von Mangoldt global and local counting},
\]

\[
\text{zero-free region near }\Re s=1,
\]

\[
\text{zero-density bounds away from the critical line},
\]

\[
\text{possible spacing / pair-correlation constraints},
\]

\[
\text{explicit-formula compatibility with primes}.
\]

The first six are still essentially **zero-side geometric/statistical constraints**. The last one is the real arithmetic constraint, but once it is used seriously the proof has moved into the prime/AFE or global trace side.

---

# 2. Do known zero-density or zero-free-region bounds block the design?

Only in non-central regimes.

## Zero-free region

The de la Vallée Poussin zero-free region excludes zeros very close to

\[
\Re s=1.
\]

But the same-scale quadrature design does not need zeros near \(\Re s=1\). It can use packets with normalized depths bounded away from the endpoints, or shallow packets near the critical line after singular rescaling. Thus the zero-free region does not attack the main obstruction.

## Zero-density estimates

Zero-density estimates can obstruct a design that requires many zeros with

\[
\Re\rho \ge \frac12+\eta
\]

for fixed \(\eta>0\), especially over large height ranges. But the quadrature needs only

\[
N=O(R)
\]

packets, with

\[
R\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R=O(\log Q).
\]

That is far too small for standard zero-density estimates to exclude locally, unless the design demands an implausibly dense cluster of zeros far off the critical line. The dangerous regime is not that: it is same-scale or shallow same-scale clustering near the critical line, where density estimates are weakest.

## Local zero counting

Riemann–von Mangoldt controls the number of zeros in a height window roughly by

\[
N(T+H)-N(T-H)\sim \frac{H}{\pi}\log T+O(\log T).
\]

This can rule out **too many** nodes in an interval, but the quadrature construction needs only \(O(R)\) nodes. If \(Q\) is polylogarithmic in \(T\), then \(O(\log Q)\) nodes are not excluded by local counting at the precision needed here.

So counting and density do not prove a lower bound of the form

\[
\max_{3\le k\le R+3}
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}.
\]

---

# 3. What depths does the quadrature need?

In ordinary same-scale coordinates,

\[
x_j=\cos\theta_j,
\qquad
c_j=\sin\theta_j,
\]

so all packets lie on the same normalized shell

\[
x_j^2+c_j^2=1.
\]

The continuous positive quadrature measure may be supported away from the endpoints \(\theta=0,\pi\), so normalized depths \(c_j\) can be bounded below by a fixed constant. In physical variables, that means

\[
\text{off-critical packet depth} \asymp \lambda.
\]

For an ordinary packet scale \(\lambda=d\), this is just an ordinary same-scale shell.

For a singular packet scale \(\lambda=c\ll Q^{-C}\), the physical depths are tiny, but after rescaling

\[
m=\gamma+cx
\]

the normalized depths are still \(O(1)\). Thus the singular design is not geometrically harder. It is the same finite moment design at a smaller physical scale.

Known zero-density estimates do not exclude a small finite same-scale cluster near the critical line. They would help only if the construction required fixed-depth off-critical zeros in a region where density estimates imply scarcity. The core obstruction can live in the shallow regime, so this help is partial at best.

---

# 4. Quartet symmetry

Quartet symmetry does not defeat the adversary.

If a zero packet is included, the actual zeta configuration must include the partners

\[
\rho,\quad \bar\rho,\quad 1-\rho,\quad 1-\bar\rho.
\]

In normalized packet variables, this imposes symmetry on the node set and modifies the effective weights. But the moment equations are linear, and quartet closure can be built into the finite design from the start.

At worst, quartet closure multiplies the number of nodes by a bounded factor. It does not change the fact that \(O(R)\) packets are enough to satisfy \(O(R)\) moment equations.

So quartet symmetry is a constraint, but not a rigidity theorem.

---

# 5. Simplicity and zero repulsion

Simplicity also does not defeat the construction. A quadrature weight \(w_j\) can be approximated by a small cluster of nearby simple nodes, preserving finitely many moments to polynomial accuracy.

Zero-repulsion phenomena are not strong enough here. For zeta itself, there is no Landau–Page-style exceptional zero mechanism analogous to real Dirichlet \(L\)-functions that would directly prohibit such a local finite packet design. Known spacing information is averaged or conditional, and does not forbid one exceptional deterministic \(O(R)\)-node configuration.

Thus simplicity and repulsion do not currently yield the needed anti-design inequality.

---

# 6. Explicit-formula compatibility

This is the only promising actual-zeta-specific zero-side constraint.

The packet design is not an arbitrary finite measure if it must be part of the actual zero set of \(\zeta\). The actual zeros are tied to primes by the explicit formula. A true anti-design theorem would have to say that a same-scale finite packet cluster satisfying

\[
\sum_j w_j\sin(k\theta_j)\approx-\mathcal B_k
\]

for

\[
3\le k\le R+3
\]

is incompatible with the prime-side fixed coefficients.

But that is no longer a purely local zero-side proof. It is a zero-prime compatibility theorem, equivalent in spirit to the prime/AFE nonrecurrence problem.

So the strongest conclusion is:

\[
\boxed{
\text{zero-side geometry alone fails; zero-prime compatibility is needed.}
}
\]

---

# 7. Concrete local countermodel satisfying known zero-side constraints

The local no-go is explicit.

Since

\[
K_\theta^{(n)}(0)=n!\sin((n+1)\theta),
\]

source flattening through order \(R+2\) is the finite moment system

\[
\sum_j w_j\sin(k\theta_j)=0,
\qquad 3\le k\le R+3.
\]

There is a continuous positive same-scale measure, for example of the form

\[
d\mu(\theta)\propto \sin\theta\,d\theta,
\]

whose aggregate packet profile is locally constant, so all nonzero derivatives vanish at the center.

By finite positive quadrature, for any finite \(R\) there exists a positive finite node set

\[
\{(\theta_j,w_j)\}_{j=1}^{N_R},
\qquad
N_R=O(R),
\]

matching those moments through order \(R+2\).

This model can be made to satisfy:

\[
\text{same-scale geometry},
\]

\[
\text{positive weights},
\]

\[
\text{quartet closure},
\]

\[
\text{simplicity by node splitting},
\]

\[
\text{local counting at }O(R)\text{ scale},
\]

\[
\text{endpoint separation},
\]

\[
\text{Gram positivity},
\]

\[
\text{live anisotropy}.
\]

It is not an actual zeta zero set, but it proves that the currently identified local zero-side constraints are insufficient.

---

# 8. Strengthened zero-side theorem needed

The missing theorem should be stated as:

\[
\boxed{
\textbf{Actual-zeta same-scale anti-design theorem.}
}
\]

Let

\[
I_\rho=m_0+\lambda X,
\qquad
F_\lambda(x)=\lambda^3q''_{\can}(m_0+\lambda x),
\]

where \(\lambda\) is ordinary or singular packet scale. Let the actual zeta zero packets in the same-scale shell have normalized parameters \((\theta_j,w_j)\). Let \(\mathcal B_k\) denote canonical background, tail, non-shell, and regularization moments. Then for

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R(Q)=O(\log Q),
\]

there exist constants \(B>0\) and some \(3\le k\le R(Q)+3\) such that

\[
\boxed{
\left|
\sum_j w_j\sin(k\theta_j)+\mathcal B_k
\right|
\ge Q^{-B}.
}
\]

Equivalent normalized finite-jet form:

\[
\boxed{
\max_{0\le r\le R(Q)}
|\partial_x^rF_\lambda(x_0)|
\ge
Q^{-B}\lambda^3|X|^{1/2}.
}
\]

Equivalent interval form:

\[
\boxed{
\int_X |F_\lambda(x)|^2\,dx
\ge Q^{-B}\lambda^6|X|.
}
\]

This theorem must use actual-zeta arithmetic beyond local zero constraints.

---

# 9. Final verdict

\[
\boxed{
\text{Known zero-side arithmetic helps only in limited named regimes.}
}
\]

It may help if the adversary requires many zeros far off the critical line, near the \(\Re s=1\) edge, or in violation of coarse local counts. But the main same-scale quadrature adversary can use only \(O(R)\) packets and can live near the critical line.

Therefore:

\[
\boxed{
\text{Zero-side Gate 1 proof is possible only with a new zero-prime arithmetic input.}
}
\]

A purely local zero-side proof is not currently viable. The next serious attacks should be either:

\[
\text{prime/AFE fixed-coefficient nonrecurrence},
\]

\[
\text{explicit-formula anti-design},
\]

or

\[
\text{global trace/Weil-positive pivot}.
\]
## User (2026-04-26 14:20:35)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:21:00)

_Thought for 24s_

Agent 1/A — zero-prime compatibility theorem.

## Verdict

Zero-prime compatibility currently **does not add independent leverage** beyond the prime/AFE finite-jet nonrecurrence problem.

A same-scale zero-side anti-design failure translates cleanly into a system of prime-side finite-jet cancellation equations. But I do not see a sign, positivity, coercivity, or size obstruction on the prime side that would make those equations impossible. The resulting theorem is essentially the already identified missing theorem:

\[
\boxed{
\text{No simultaneous off-line-zero/source-flat finite-jet recurrence.}
}
\]

So the zero-prime route is real, but at present it is a **reformulation** of Gate 1’s prime/AFE nonrecurrence problem, not a shortcut. The current shared state already identifies Gate 1 as central and says the next concrete attacks are zero-prime compatibility, one-parameter prime-log nonrecurrence, and numerical Gate 1 stress tests. 

---

# 1. Translating zero-side moments into explicit-formula constraints

In normalized packet coordinates,

\[
m=m_0+\lambda x,
\qquad
F_\lambda(x)=\lambda^3 q''_{\can}(m_0+\lambda x).
\]

Gate 1 source flatness means

\[
F_\lambda(x)\approx 0
\]

on \(X\), or in finite-jet form,

\[
\partial_x^rF_\lambda(x_0)\approx0,
\qquad
0\le r\le R.
\]

Since

\[
\partial_x^rF_\lambda(x_0)
=
\lambda^{r+3}
\partial_m^r q''_{\can}(m_0+\lambda x_0),
\]

the zero-side finite-jet conditions are equivalent to

\[
\partial_m^r q''_{\can}(m_\ast)\approx0,
\qquad
0\le r\le R,
\]

where \(m_\ast=m_0+\lambda x_0\), after rescaling the error threshold by \(\lambda^{-(r+3)}\).

On the zero side, a same-scale packet shell gives moment conditions of the form

\[
\sum_j w_j\sin(k\theta_j)+\mathcal B_k\approx0,
\qquad
3\le k\le R+3.
\]

Here \(\mathcal B_k\) represents background, nonshell packets, tail, and regularized completed-factor contributions.

On the prime/AFE side, write

\[
q''_{\can}(m)=B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

with

\[
P_2(m)=\Re\sum_{n\le X} a_n e^{-im\log n}.
\]

Then

\[
\partial_m^r q''_{\can}(m_\ast)
=
B_2^{(r)}(m_\ast)
+
D_2^{(r)}(m_\ast)
+
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_\ast\log n}
+
E_2^{(r)}(m_\ast).
\]

So zero-side source flattening translates to

\[
\boxed{
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_\ast\log n}
\approx
-\bigl(B_2+D_2+E_2\bigr)^{(r)}(m_\ast),
\qquad 0\le r\le R.
}
\]

This is the exact prime-side image of the zero-side moment equations.

If the off-line packet center condition is included, one also has

\[
Z_\alpha(m_0)=0,
\]

or the draft’s equivalent actual-zeta off-line-packet equation. The shared status already records that the prime/AFE route reduces to this kind of center-conditioned finite-jet nonrecurrence and is not yet closed. 

---

# 2. Does a same-scale source-flattening design force a detectable prime imbalance?

Not automatically.

The prime-side constraints above do not say a prime sum is abnormally large. They say a vector of prime sums lands near a prescribed target:

\[
\left(
S_0(m_\ast),S_1(m_\ast),\ldots,S_R(m_\ast)
\right)
\approx
-\left(
T_0(m_\ast),T_1(m_\ast),\ldots,T_R(m_\ast)
\right),
\]

where

\[
S_r(m):=\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im\log n},
\]

and

\[
T_r(m):=(B_2+D_2+E_2)^{(r)}(m).
\]

This is a recurrence or interpolation event, not a size contradiction.

A detectable imbalance would require one of the following:

1. **Magnitude obstruction:** the target vector is outside the natural range of \((S_0,\ldots,S_R)\);
2. **Sign/coercivity obstruction:** some positive combination of the equations has a fixed sign that cannot vanish;
3. **Transversality plus one-parameter nonrecurrence:** the actual orbit \(m\mapsto(e^{-im\log p})_p\) cannot enter the bad tube often enough or at all;
4. **Weil-positive obstruction:** a positive explicit-formula test detects the zero-side packet design and forces a positive prime-side contradiction.

I do not see any of these from the current local formulation. The zero-side design creates cancellations, but cancellations are exactly what oscillatory prime sums can do.

So the prime-side “abnormality” is not a large value. It is a highly specific finite-jet recurrence.

---

# 3. Candidate theorem

The zero-prime compatibility route would need the following theorem.

\[
\boxed{
\textbf{Zero-prime anti-design compatibility theorem.}
}
\]

Let \(I_\rho=m_0+\lambda X\) be an admissible ordinary or singular packet interval, and let \(m_\ast=m_0+\lambda x_0\). Suppose \(m_0\) satisfies the off-line packet condition

\[
Z_\alpha(m_0)=0.
\]

Then for some fixed \(B>0\) and

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R(Q)=O(\log Q),
\]

one has

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_m^r q''_{\can}(m_\ast)
\right|
\ge Q^{-B}\lambda^{-3-r}.
}
\]

Equivalently, in normalized variables,

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\partial_x^rF_\lambda(x_0)
\right|
\ge
Q^{-B}\lambda^3 |X|^{1/2}.
}
\]

Using the AFE representation, this becomes

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_\ast\log n}
+
(B_2+D_2+E_2)^{(r)}(m_\ast)
\right|
\ge
Q^{-B}\lambda^{-3-r}.
}
\]

Together with the zero equation

\[
Z_\alpha(m_0)=0,
\]

this is precisely a **no simultaneous off-line-zero/source-flat finite-jet recurrence** theorem.

This candidate theorem would close Gate 1. But at present it is a statement to prove, not a consequence of existing explicit-formula compatibility.

---

# 4. Prime-side quantity that becomes abnormal

The relevant quantity is the finite jet vector

\[
\mathcal S_R(m)
:=
\left(
\partial_m^r q''_{\can}(m)
\right)_{0\le r\le R}.
\]

In prime/AFE form,

\[
\mathcal S_R(m)
=
\left(
B_2^{(r)}(m)+D_2^{(r)}(m)+E_2^{(r)}(m)
+
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im\log n}
\right)_{0\le r\le R}.
\]

So the “abnormal” event is not

\[
|\mathcal S_R(m)|\gg 1.
\]

It is the opposite:

\[
\boxed{
\|\mathcal S_R(m)\|\ll Q^{-B}
}
\]

simultaneously with

\[
Z_\alpha(m)=0.
\]

Thus the prime-side quantity to monitor is a **small-ball event** for a log-weighted Dirichlet-polynomial jet vector, conditioned on the off-line zero equation.

This is why generic large-sieve or mean-square tools do not immediately help. They usually control average size, not exclusion of a small-ball hit at an arithmetically constrained center.

---

# 5. Is this route different from prime/AFE finite-jet nonrecurrence?

Only in language, not in substance.

The zero-side anti-design equations

\[
\sum_jw_j\sin(k\theta_j)+\mathcal B_k\approx0
\]

are just the zero-side expression of

\[
\partial_x^rF_\lambda(x_0)\approx0.
\]

The explicit formula translates the same statement into

\[
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_\ast\log n}
+
(B_2+D_2+E_2)^{(r)}(m_\ast)
\approx0.
\]

So the zero-prime compatibility theorem is equivalent to saying:

\[
\boxed{
\text{the actual prime-log orbit cannot realize the same finite-jet source-flatness.}
}
\]

That is exactly the prime/AFE nonrecurrence theorem already identified as missing. The current status notes say the phase-relaxed model is underdetermined and the one-parameter orbit makes hitting rare but not implausible; hence the missing prime theorem remains a no simultaneous off-line-zero/source-flat recurrence statement. 

Thus zero-prime compatibility does not currently add an independent lever unless one can produce a new positivity or rigidity principle.

---

# 6. Possible leverage points

There are three possible ways this route could become nontrivial.

## 6.1 Positive explicit-formula test

Construct a packet-adapted test \(w\) such that source flattening forces a zero-side quadratic form to be small, while Weil positivity or a prime-side identity forces it to be large.

Candidate object:

\[
\mathcal E_w(m_0)
=
\int w(m-m_0)|q''_{\can}(m)|^2\,dm.
\]

But the existing status says global trace is not currently a shortcut: this energy is nonnegative but still needs coercivity against same-scale cancellation. 

## 6.2 Small-ball repulsion for fixed zeta coefficients

Prove a theorem of the form

\[
\inf_{m:Z_\alpha(m)=0}
\left\|
\left(
\partial_m^r q''_{\can}(m)
\right)_{r\le R}
\right\|
\ge Q^{-B}.
\]

This is exactly the center-conditioned fixed-coefficient nonrecurrence theorem.

## 6.3 Zero-density plus depth constraints

If the anti-design necessarily required many zeros far off the line, zero-density might help. But the dangerous design can use \(O(R)\) same-scale packets near the critical line, so zero-density does not currently supply enough rigidity.

---

# 7. Final explanation of why no contradiction is visible

The explicit formula is an identity. A zero-side same-scale design that flattens source curvature simply tells us that the prime-side Dirichlet-polynomial jet vector has landed near a certain target. It does not, by itself, violate any known prime-side size, sign, or positivity bound.

Formally, zero-side flatness gives

\[
\partial_m^r q''_{\can}(m_\ast)\approx0.
\]

Prime side says

\[
\partial_m^r q''_{\can}(m_\ast)
=
B_r(m_\ast)+D_r(m_\ast)+S_r(m_\ast)+E_r(m_\ast).
\]

Therefore

\[
S_r(m_\ast)\approx -B_r(m_\ast)-D_r(m_\ast)-E_r(m_\ast).
\]

This is a finite list of phase constraints on

\[
e^{-im_\ast\log p}.
\]

Unless one proves those constraints cannot be met at an admissible off-line packet center, there is no contradiction.

---

# 8. Final verdict

\[
\boxed{
\text{Zero-prime compatibility currently adds no independent leverage.}
}
\]

It gives the exact translation:

\[
\text{same-scale zero anti-design failure}
\Longleftrightarrow
\text{prime/AFE finite-jet source-flat recurrence}.
\]

The theorem needed is:

\[
\boxed{
Z_\alpha(m_0)=0
\Rightarrow
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r q''_{\can}(m_0)
\right|
\ge Q^{-B}.
}
\]

This must be proved using fixed actual-zeta coefficient rigidity, a new small-ball/nonrecurrence theorem, or a genuinely positive global trace/Weil construction. Without one of those, the zero-prime compatibility route remains a restatement of Gate 1, not a proof of it.
## User (2026-04-26 14:24:32)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:24:36)

I’ll execute Agent 1/A: produce an implementable Gate 1 numerical blueprint, including zero-side and AFE computations, interval families, validation controls, thresholds, pseudocode, and result schema.

_Thought for 4s_

Agent 1/A — numerical Gate 1 execution blueprint.

## Objective

Measure

\[
E_I=|I|^{-1}\int_I |q''_{\can}(m)|^2\,dm,
\qquad
B_I^{\rm eff}=-\frac{\log E_I}{\log Q},
\]

on many intervals

\[
I=[m_0-c_I/Q,\ m_0+c_I/Q],
\]

and detect whether actual zeta exhibits interval-level source-flatness. The coordinator explicitly asks for an executable blueprint, not another audit of Gate 1’s importance. 

The numerical question is:

\[
\boxed{
\text{Does actual }q''_{\can}\text{ ever behave like the same-scale quadrature adversary?}
}
\]

---

# 1. Canonical numerical object

Use two independent computations of

\[
q''_{\can}(m)=q_\zeta''(m)=\Phi_\zeta'''(m).
\]

## 1.1 Zero-side computation

Use

\[
q''_{\can}(m)
=
B_2(m)
+
\sum_{\rho}^{\rm reg}K_2(m;\rho).
\]

For a zero packet kernel of Cauchy/Poisson type

\[
K_0(m;c,\gamma)=\frac{c}{c^2+4(m-\gamma)^2},
\]

the second derivative is

\[
K_2(m;c,\gamma)
=
\partial_m^2 K_0(m;c,\gamma)
=
\frac{8c\left(12(m-\gamma)^2-c^2\right)}
{\left(c^2+4(m-\gamma)^2\right)^3}.
\]

For a quartet or completed-packet contribution, sum the relevant components with the signs/normalizations used by the canonical completed-phase convention.

### Zero-side evaluation

At each evaluation point \(m\):

1. Include zeros with

   \[
   |\gamma-m|\le W_{\rm near}.
   \]

2. Add the background term

   \[
   B_2(m).
   \]

3. Treat the far tail by one of:

   - symmetric cutoff plus Richardson/extrapolation in \(W_{\rm near}\);
   - analytic tail approximation from Riemann–von Mangoldt density;
   - compare multiple cutoffs until \(E_I\) stabilizes.

4. Record a tail-stability error:

   \[
   \epsilon_{\rm tail}
   =
   \max_{m\in I}
   |q''_{\can,W_2}(m)-q''_{\can,W_1}(m)|.
   \]

Require

\[
\epsilon_{\rm tail}^2 \ll E_I
\]

for a trusted measurement.

---

## 1.2 AFE-side computation

Use

\[
q''_{\can}(m)
=
B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

with

\[
P_2(m)
=
\Re\sum_{n\le X}
a_n(\log n)^2 n^{-1/2-im}W(n/T),
\]

where \(a_n\) are fixed actual-zeta coefficients in the chosen log-derivative normalization, typically \(\Lambda(n)\)-type weights including prime powers.

The dual term is

\[
D_2(m;X,W),
\]

including \(\chi\)-factor / functional-equation differentiated contributions not absorbed into \(B_2\).

AFE cross-check requirements:

\[
\epsilon_{\rm AFE}(m)
=
q''_{\can,\rm zero}(m)-q''_{\can,\rm AFE}(m).
\]

Trust only intervals where

\[
|I|^{-1}\int_I|\epsilon_{\rm AFE}(m)|^2\,dm
\le
\eta_{\rm AFE} E_I
\]

with, for example,

\[
\eta_{\rm AFE}\le 10^{-2}.
\]

If the AFE is only approximate, it is sufficient for diagnostic purposes if it ranks flat intervals similarly to the zero-side computation.

---

# 2. Choice of \(Q\)

Use a primary and secondary convention.

Primary:

\[
Q=\log\frac{m_0}{2\pi}
\]

or

\[
Q=\log(3+m_0).
\]

Secondary stress test:

\[
Q=q_0(m_0)
\]

if \(q_0\) is numerically available and stable.

All reported tables should include both if possible:

\[
Q_{\log}=\log(3+m_0),
\qquad
Q_q=q_\zeta(m_0).
\]

The effective exponent is sensitive to \(Q\), so record the convention explicitly.

---

# 3. Interval families

Use

\[
I(m_0,c_I)
=
[m_0-c_I/Q,\ m_0+c_I/Q].
\]

Run at several widths:

\[
c_I\in\{0.25,0.5,1,2,4\}.
\]

Scan centers \(m_0\) from:

1. **Gram points** \(g_n\).
2. **Critical-line zero ordinates** \(\gamma_n\).
3. **Zero-gap midpoints**

   \[
   \frac{\gamma_n+\gamma_{n+1}}2.
   \]

4. **Small-gap neighborhoods**, including centers

   \[
   \gamma_n+\tau(\gamma_{n+1}-\gamma_n),
   \qquad
   \tau\in\{0.25,0.5,0.75\}.
   \]

5. **Random centers** uniformly in height windows.
6. **Synthetic off-line packet centers**: inject a packet at chosen \((c,\gamma)\), compute synthetic \(q''_{\can}\), and verify dominance/cancellation behavior.
7. **Near-flat candidate centers** found by minimizing finite-jet objective

   \[
   J_R(m_0)
   =
   \sum_{r=0}^{R}
   \left|
   \Delta^r\partial_m^r q''_{\can}(m_0)
   \right|^2,
   \qquad
   \Delta=1/Q.
   \]

---

# 4. Quadrature method for \(E_I\)

Use Gauss–Legendre quadrature on \(I\), with adaptive refinement.

For each interval:

1. Start with \(N_{\rm quad}=64\) nodes.
2. Double to \(128,256,512\).
3. Accept if

   \[
   \frac{|E_I^{(2N)}-E_I^{(N)}|}
   {\max(E_I^{(2N)},10^{-300})}
   \le \eta_{\rm quad},
   \]

   with

   \[
   \eta_{\rm quad}=10^{-6}
   \]

   for exploratory runs and

   \eta_{\rm quad}=10^{-10}

   for candidate flat intervals.

Also compute

\[
S_I=\max_{m\in \text{quad nodes}}|q''_{\can}(m)|.
\]

If \(S_I\) is achieved sharply at one node, refine locally to avoid missing spikes.

---

# 5. Finite-jet diagnostics

For each interval center \(m_0\), compute

\[
J_r(m_0)
=
\Delta^r\partial_m^r q''_{\can}(m_0),
\qquad
0\le r\le R,
\]

where

\[
\Delta=|I|/2=c_I/Q.
\]

Use

\[
R\in\{4,8,12,16,24\}
\]

for numerics; the theoretical \(R\sim \log Q\) may be too large initially.

Use either:

- analytic derivatives of the zero-side kernel;
- high-order complex-step / spectral differentiation on a local grid;
- polynomial/Chebyshev fit on \(I\).

Define

\[
J_{\max}=\max_{0\le r\le R}|J_r|,
\qquad
J_{\rm rms}
=
\left(\sum_{r=0}^R |J_r|^2\right)^{1/2}.
\]

A serious warning requires both:

\[
E_I\ \text{small}
\]

and

\[
J_{\max}\ \text{small}.
\]

Isolated small \(q''_{\can}(m_0)\) is not meaningful.

---

# 6. Negative controls

## 6.1 Same-scale quadrature negative control

Use normalized packets

\[
K_\theta(x)
=
\frac{\sin\theta}
{(x-\cos\theta)^2+\sin^2\theta}.
\]

Construct

\[
Q(x)=\sum_jw_jK_{\theta_j}(x)
\]

such that

\[
Q''(0),Q^{(3)}(0),\ldots,Q^{(R+2)}(0)
\]

are tiny.

Then set

\[
q_{\rm synth}(m_0+\lambda x)=\lambda^{-1}Q(x),
\qquad
q_{\rm synth}''(m_0+\lambda x)=\lambda^{-3}Q''(x).
\]

Expected result:

\[
E_I
=
|I|^{-1}\int_I |q_{\rm synth}''(m)|^2\,dm
\]

collapses by many orders relative to a random packet cluster.

The pipeline must detect this as:

\[
B_I^{\rm eff}\gg 1.
\]

If it does not, the numerical test is not sensitive enough.

## 6.2 Singular dominance synthetic test

Use

\[
K_c(x)=\frac{c}{x^2+c^2}
\]

with \(c\ll Q^{-C}\). Center the interval on the packet.

Expected:

\[
q''\sim c^{-3},
\qquad
E_I\sim c^{-6}
\]

up to scale factors. The test should show overwhelming nonflatness.

## 6.3 Singular cancellation synthetic test

Construct two or more same-scale shallow packets so that normalized source jets cancel:

\[
Q''(0)\approx Q^{(3)}(0)\approx\cdots\approx0.
\]

Expected:

- dominance test: huge \(E_I\);
- cancellation test: collapsed \(E_I\);
- confirms that singular failure is cancellation/quadrature, not mere shallowness.

---

# 7. Pass/fail thresholds

Let

\[
B_I^{\rm eff}=-\frac{\log E_I}{\log Q}.
\]

Because \(E_I\) may be larger than \(1\), \(B_I^{\rm eff}\) can be negative. That is healthy.

Suggested interpretation:

## Healthy / supports Gate 1

Across height windows and interval families:

\[
B_I^{\rm eff}\le B_0
\]

with stable fixed \(B_0\), e.g.

\[
B_0\in[5,20],
\]

and no upward drift with height.

Also:

\[
J_{\max}\not\to0
\]

with height in candidate intervals.

## Threatens Gate 1

Find intervals where:

\[
B_I^{\rm eff}
\]

grows systematically with height, or where for increasing \(Q\),

\[
E_I\le Q^{-B}
\]

for all tested \(B\) in a trend-compatible way.

Finite-jet warning:

\[
J_{\max}\le Q^{-B_J}
\]

with \(B_J\) growing across height.

## Route likely non-closing

A robust family of actual-zeta intervals with:

\[
E_I \ll Q^{-B}|I|^0
\]

for increasing \(B\), plus

\[
J_r(m_0)\approx0,
\qquad
0\le r\le R,
\]

and agreement between zero-side and AFE computations.

One-off numerical smallness is not enough; it must be stable under:

- increased precision;
- tail cutoff escalation;
- interval width variation;
- AFE cross-check;
- derivative/jet verification.

---

# 8. Precision and cutoff requirements

## Zero data

For a height window centered at \(T\):

- Need verified zeros in

  \[
  [T-W_{\rm zero},T+W_{\rm zero}]
  \]

  with

  \[
  W_{\rm zero}\gg c_I/Q
  \]

  and large enough to stabilize the tail.

- Start with

  \[
  W_{\rm zero}\in\{10/Q,100/Q,1000/Q,1,10\}
  \]

  depending on height and data availability.

- Escalate until \(E_I\) changes by less than tolerance.

## Precision

Use arbitrary precision. Minimum:

\[
\text{working precision}
\ge
\max(80,\ 4|\log_{10} E_I|+50)
\]

decimal digits for candidate flat intervals.

For exploratory scans:

\[
80\text{--}120
\]

digits may suffice.

## Tail cutoff escalation

For each interval compute

\[
E_I(W_1),E_I(W_2),E_I(W_3)
\]

with increasing zero cutoffs.

Accept only if

\[
|E_I(W_{j+1})-E_I(W_j)|
\le
\eta_{\rm tail}E_I(W_{j+1})
\]

for two consecutive levels.

If not, mark as “tail unstable.”

## AFE cross-check

For top \(N\) flattest intervals per height window, compute AFE-side \(q''_{\can}\). Accept candidate only if:

\[
\frac{\int_I |q''_{\zero}-q''_{\AFE}|^2}
{\int_I |q''_{\zero}|^2}
\le
10^{-2}
\]

initially, tightened to \(10^{-4}\) for serious candidates.

---

# 9. Pseudocode

```text
INPUT:
  height windows W_T = [(T_min,T_max), ...]
  zero database Z
  interval widths c_I_list
  center families C_families
  Q convention
  zero cutoffs W_zero_list
  quadrature sizes N_quad_list
  derivative order R_list

FOR each height window:
  generate centers m0 from:
    Gram points
    zero ordinates
    gap midpoints
    small-gap neighborhoods
    random points

  FOR each center m0:
    Q = Q_convention(m0)

    FOR each c_I in c_I_list:
      I = [m0 - c_I/Q, m0 + c_I/Q]

      FOR each zero cutoff W_zero:
        define qpp_zero(m):
          return B2(m) + sum_{rho: |gamma-rho - m0| <= W_zero} K2(m;rho)
                 + tail_regularization(m,W_zero)

        FOR N_quad in N_quad_list:
          nodes, weights = GaussLegendre(I,N_quad)
          vals = [qpp_zero(node) for node in nodes]
          E[N_quad,W_zero] = (1/|I|) * sum weights_i * |vals_i|^2
          S[N_quad,W_zero] = max |vals_i|

        test quadrature convergence for fixed W_zero

      test tail convergence across W_zero

      compute B_eff = -log(E_final)/log(Q)

      compute finite jets J_r at m0 for r<=R
        via analytic kernel derivatives or Chebyshev fit

      store result row

  select flattest intervals by E and B_eff
  run AFE cross-check on top candidates
  run higher precision validation on serious candidates

RUN negative controls:
  build same-scale quadrature packet design
  compute E, B_eff, jets
  verify collapse is detected

RUN singular synthetic tests:
  dominance packets
  cancellation packets
  verify expected behavior

OUTPUT:
  result table
  candidate flat intervals
  convergence diagnostics
  plots of B_eff vs height, center type, width
```

---

# 10. Result table schema

| field | description |
|---|---|
| `run_id` | unique run identifier |
| `height_window` | \([T_{\min},T_{\max}]\) |
| `center_type` | Gram / zero / midpoint / random / synthetic |
| `m0` | interval center |
| `Q_log` | \(\log(3+m_0)\) |
| `Q_q` | optional \(q_\zeta(m_0)\) |
| `c_I` | interval half-width factor |
| `I_left`, `I_right` | endpoints |
| `zero_cutoff` | final zero cutoff |
| `N_quad` | final quadrature nodes |
| `E_I` | mean \(L^2\) source curvature |
| `S_I` | sup estimate |
| `B_eff` | \(-\log E_I/\log Q\) |
| `tail_error_rel` | cutoff stability metric |
| `quad_error_rel` | quadrature stability metric |
| `AFE_error_rel` | AFE vs zero-side metric |
| `R_jet` | derivative order tested |
| `J_max` | max normalized jet |
| `J_rms` | RMS normalized jet |
| `status` | healthy / candidate / rejected / unstable |
| `notes` | diagnostics |

---

# 11. Initial experimental sequence

Run in this order.

## Stage 0 — pipeline validation

1. Same-scale quadrature negative control.
2. Random packet cluster positive control.
3. Singular dominance test.
4. Singular cancellation test.

Do not scan actual zeta until these pass.

## Stage 1 — low/medium-height actual zero-side scan

Use available verified zeros. Scan:

- zero ordinates;
- zero-gap midpoints;
- Gram points;
- random centers.

Report distribution of \(B_I^{\rm eff}\).

## Stage 2 — candidate refinement

For the flattest 0.1% of intervals:

- increase precision;
- increase quadrature nodes;
- increase zero cutoff;
- compute finite jets;
- run AFE cross-check.

## Stage 3 — surrogate comparison

Run fixed-prime/AFE phase surrogates using the same intervals and diagnostics. Determine whether surrogates show source-flat intervals more often than actual zeta.

## Stage 4 — height trend

Repeat over height bands. Gate 1 is numerically threatened only if flatness worsens systematically with \(Q\).

---

# 12. Final interpretation

The experiment supports Gate 1 if actual-zeta scans show:

\[
B_I^{\rm eff}=O(1)
\]

with no upward trend, while the quadrature negative control shows large \(B_I^{\rm eff}\), confirming sensitivity.

The experiment threatens Gate 1 if actual zeta produces stable intervals with:

\[
E_I\ll Q^{-B}
\]

for increasing \(B\), accompanied by finite-jet suppression:

\[
J_r\approx0,\qquad0\le r\le R,
\]

and validated by both zero-side and AFE-side computations.

The experiment suggests the rank-two route is non-closing if such source-flat intervals persist under all validation checks and resemble the same-scale quadrature adversary.
## User (2026-04-26 14:29:08)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:29:12)

I’ll implement the negative control as a normalized packet model first. The key is to construct positive quadrature for the measure proportional to \(\sin\theta\,d\theta\), because that makes all nonconstant kernel derivatives vanish at the center.

_Thought for 27s_

Agent 1/A — same-scale quadrature negative control.

## Goal

Build a synthetic packet configuration where

\[
E_I=|I|^{-1}\int_I |q''_{\can}(m)|^2\,dm
\]

collapses. This is the required negative control before trusting actual-zeta Gate 1 scans. The current round’s instruction explicitly asks for executable numerical/surrogate work rather than more strategic auditing. 

Work in normalized coordinates first:

\[
m=m_0+\lambda x,
\qquad
q(m_0+\lambda x)=\lambda^{-1}Q(x),
\]

so

\[
q''(m_0+\lambda x)=\lambda^{-3}Q''(x).
\]

The negative control constructs \(Q\) so that \(Q''\) and its first many derivatives vanish at \(x=0\).

---

# 1. Kernel derivative identity

Use

\[
K_\theta(x)=\frac{\sin\theta}{(x-\cos\theta)^2+\sin^2\theta}.
\]

Observe that

\[
K_\theta(x)
=
\Im\frac{1}{x-e^{i\theta}}.
\]

For \(|x|<1\),

\[
\frac{1}{x-e^{i\theta}}
=
-e^{-i\theta}\frac{1}{1-xe^{-i\theta}}
=
-\sum_{n\ge0}x^n e^{-i(n+1)\theta}.
\]

Taking imaginary parts,

\[
K_\theta(x)
=
\sum_{n\ge0}x^n\sin((n+1)\theta).
\]

Therefore

\[
\boxed{
K_\theta^{(n)}(0)=n!\sin((n+1)\theta).
}
\]

For

\[
Q(x)=\sum_j w_jK_{\theta_j}(x),
\]

we get

\[
Q^{(n)}(0)
=
n!\sum_j w_j\sin((n+1)\theta_j).
\]

Since the Gate 1 source term is

\[
F(x)=Q''(x),
\]

its finite jets are

\[
J_r:=F^{(r)}(0)
=
Q^{(r+2)}(0)
=
(r+2)!\sum_j w_j\sin((r+3)\theta_j).
\]

Thus source-flatness through order \(R\) requires

\[
\sum_jw_j\sin(k\theta_j)\approx0,
\qquad
3\le k\le R+3.
\]

---

# 2. Exact deterministic positive quadrature

Use the discrete sine grid

\[
\theta_j=\frac{j\pi}{N+1},
\qquad
1\le j\le N,
\]

with positive weights

\[
\boxed{
w_j=\frac{2}{N+1}\sin\theta_j.
}
\]

The discrete sine orthogonality identity is

\[
\sum_{j=1}^{N}
\sin(a\theta_j)\sin(b\theta_j)
=
\frac{N+1}{2}\delta_{ab},
\qquad
1\le a,b\le N.
\]

Therefore

\[
\sum_{j=1}^Nw_j\sin(k\theta_j)
=
\frac{2}{N+1}
\sum_{j=1}^N
\sin\theta_j\sin(k\theta_j)
=
\delta_{k1}
\qquad(1\le k\le N).
\]

So:

\[
\boxed{
\sum_jw_j\sin\theta_j=1,
}
\]

and

\[
\boxed{
\sum_jw_j\sin(k\theta_j)=0
\qquad
2\le k\le N.
}
\]

Choose

\[
N\ge R+3.
\]

Then

\[
J_r=0,
\qquad
0\le r\le R.
\]

This is an exact positive finite quadrature, not a numerical optimizer. It is the cleanest negative control.

---

# 3. Continuous-measure interpretation

The deterministic construction discretizes the continuous positive measure

\[
d\mu(\theta)=\frac{2}{\pi}\sin\theta\,d\theta.
\]

Indeed,

\[
\int_0^\pi \sin(k\theta)\,d\mu(\theta)
=
\frac{2}{\pi}\int_0^\pi \sin(k\theta)\sin\theta\,d\theta
=
\delta_{k1}.
\]

Thus the continuous packet aggregate has

\[
Q(0)=1,
\qquad
Q^{(n)}(0)=0
\quad(n\ge1).
\]

The finite sine-grid quadrature matches this through order \(N-1\).

---

# 4. Nonnegative least-squares / linear-programming construction

As a second construction, choose a dense grid

\[
\theta_j=\frac{j\pi}{N_{\rm grid}+1},
\qquad
1\le j\le N_{\rm grid}.
\]

Solve

\[
Aw\approx b,
\qquad
w_j\ge0,
\]

where

\[
A_{0j}=\sin\theta_j,
\qquad
b_0=1,
\]

and for \(3\le k\le R+3\),

\[
A_{kj}=\sin(k\theta_j),
\qquad
b_k=0.
\]

Optionally also impose

\[
\sum_j w_j\sin(2\theta_j)=0
\]

to kill \(Q'(0)\).

Objective:

\[
\min_{w_j\ge0}
\|Aw-b\|_2^2+\eta\|w\|_2^2.
\]

This produces a robust numerical negative control even if later one wants additional constraints, such as excluding endpoint nodes or enforcing quartet-style paired packets.

But the deterministic sine-grid construction above is preferable for the baseline validation because it gives exact cancellation through the prescribed order.

---

# 5. Normalized curvature and diagnostics

Define

\[
Q_N(x)=\sum_{j=1}^N w_jK_{\theta_j}(x),
\]

with

\[
\theta_j=\frac{j\pi}{N+1},
\qquad
w_j=\frac{2}{N+1}\sin\theta_j.
\]

Then for \(|x|<1\),

\[
Q_N(x)=1+\sum_{n\ge N} \mu_{n+1}x^n,
\]

where

\[
\mu_k=\sum_jw_j\sin(k\theta_j).
\]

Hence

\[
F_N(x):=Q_N''(x)
=
\sum_{n\ge N}n(n-1)\mu_{n+1}x^{n-2}.
\]

All finite jets satisfy

\[
F_N^{(r)}(0)=0
\qquad
0\le r\le N-3.
\]

Thus choosing

\[
N=R+3
\]

kills \(F,F',\ldots,F^{(R)}\) at \(0\).

Define the normalized interval

\[
X=[-X_0,X_0],
\]

and compute

\[
E_X
=
|X|^{-1}\int_X |F_N(x)|^2\,dx,
\]

\[
J_r=F_N^{(r)}(0),
\qquad
0\le r\le R.
\]

Expected:

\[
J_r=0
\qquad(0\le r\le R)
\]

up to floating-point / arbitrary-precision error.

---

# 6. Expected scaling of \(E_X\)

For \(|x|\le X_0<1\),

\[
|F_N(x)|
\le
\sum_{n\ge N}n(n-1)|\mu_{n+1}|X_0^{n-2}.
\]

Since \(|\mu_k|\le \sum_jw_j=O(1)\),

\[
|F_N(x)|
\ll
\frac{N^2X_0^{N-2}}{(1-X_0)^3}.
\]

Therefore

\[
\boxed{
E_X
\ll
\frac{N^4X_0^{2N-4}}{(1-X_0)^6}.
}
\]

So for fixed \(X_0<1\), the negative control collapses exponentially in \(N\).

Practical expectations:

- \(X_0=0.25\): very rapid collapse.
- \(X_0=0.5\): strong collapse.
- \(X_0=0.75\): still visible but requires larger \(N\).
- \(X_0\to1\): collapse is weaker because the packet poles lie at unit distance from \(0\).

Recommended baseline:

\[
X_0=0.5,
\qquad
R=12,
\qquad
N=R+3=15.
\]

Then

\[
E_X
\]

should be many orders smaller than a random same-scale packet cluster.

---

# 7. Physical rescaling

Given packet scale \(\lambda\), define

\[
m=m_0+\lambda x,
\]

\[
q_{\rm synth}(m_0+\lambda x)=\lambda^{-1}Q_N(x),
\]

\[
q_{\rm synth}''(m_0+\lambda x)=\lambda^{-3}F_N(x).
\]

On the physical interval

\[
I=m_0+\lambda X,
\]

the physical energy is

\[
E_I
=
|I|^{-1}\int_I |q_{\rm synth}''(m)|^2\,dm.
\]

Since

\[
dm=\lambda dx,
\qquad
|I|=\lambda |X|,
\]

we have

\[
E_I
=
\lambda^{-6}E_X.
\]

Thus the normalized collapse is measured by \(E_X\), while the physical value scales like \(\lambda^{-6}\). For validating the Gate 1 diagnostic, record both:

\[
E_X
\]

and

\[
\lambda^6E_I=E_X.
\]

This avoids falsely interpreting the singular scaling \(\lambda^{-6}\) as nonflatness or flatness.

---

# 8. Recommended parameter sets

## Baseline exact quadrature

\[
R=12,
\qquad
N=15,
\qquad
X_0=0.5.
\]

Expected:

\[
J_r=0
\quad(0\le r\le12),
\]

and

\[
E_X\ll 1.
\]

## Strong negative control

\[
R=24,
\qquad
N=27,
\qquad
X_0=0.5.
\]

Expected:

\[
E_X
\]

collapses roughly like

\[
0.5^{2N}
\]

up to polynomial factors.

## Stress interval

\[
R=24,
\qquad
N=27,
\qquad
X_0=0.75.
\]

Expected:

still flat, but less dramatic; useful for testing whether the numerical pipeline detects more delicate flattening.

## NNLS construction

\[
R=24,
\qquad
N_{\rm grid}=200,
\qquad
X_0=0.5.
\]

Use nonnegative least squares to solve the moment system. Expected:

\[
\max_{3\le k\le R+3}
\left|
\sum_jw_j\sin(k\theta_j)
\right|
\le 10^{-p}
\]

depending on precision and solver tolerance.

---

# 9. Pseudocode: deterministic sine quadrature

```text
function build_sine_quadrature(R):
    N = R + 3
    theta = []
    w = []
    for j in 1..N:
        th = pi*j/(N+1)
        theta.append(th)
        w.append(2/(N+1)*sin(th))
    return theta, w

function K(theta, x):
    return sin(theta)/((x - cos(theta))^2 + sin(theta)^2)

function Q(theta_list, w_list, x):
    total = 0
    for theta, w in zip(theta_list, w_list):
        total += w*K(theta,x)
    return total

function K_derivative(theta, n, x):
    # recommended: use automatic differentiation or analytic recurrence.
    # for x=0, exact formula:
    if x == 0:
        return factorial(n)*sin((n+1)*theta)
    else:
        return analytic_derivative_or_AD(K(theta,.), n, x)

function F(theta_list, w_list, x):
    # F = Q''
    total = 0
    for theta, w in zip(theta_list, w_list):
        total += w*K_derivative(theta, 2, x)
    return total

function jet(theta_list, w_list, r):
    # J_r = F^{(r)}(0)=Q^{(r+2)}(0)
    n = r + 2
    total = 0
    for theta, w in zip(theta_list, w_list):
        total += w*factorial(n)*sin((n+1)*theta)
    return total

function compute_E_X(theta_list, w_list, X0, Nquad):
    nodes, weights = gauss_legendre(-X0, X0, Nquad)
    integral = 0
    for x, wg in zip(nodes, weights):
        val = F(theta_list,w_list,x)
        integral += wg*abs(val)^2
    return integral/(2*X0)

# main
R = 24
X0 = 0.5
theta, w = build_sine_quadrature(R)

moments = []
for k in 1..R+3:
    moments[k] = sum_j w[j]*sin(k*theta[j])

jets = []
for r in 0..R:
    jets[r] = jet(theta,w,r)

E_X = compute_E_X(theta,w,X0,Nquad=256)

print(max_abs(moments[3:R+3]))
print(max_abs(jets[0:R]))
print(E_X)
```

Expected:

\[
\max_{3\le k\le R+3}|\mu_k|
\]

near numerical zero,

\[
\max_{0\le r\le R}|J_r|
\]

near numerical zero, and small \(E_X\).

---

# 10. Pseudocode: NNLS / LP quadrature

```text
function build_nnls_quadrature(R, Ngrid, include_k2=true):
    theta_j = pi*j/(Ngrid+1), j=1..Ngrid

    rows = []
    b = []

    # normalization sum w sin(theta)=1
    rows.append([sin(theta_j) for theta_j in theta])
    b.append(1)

    if include_k2:
        rows.append([sin(2*theta_j) for theta_j in theta])
        b.append(0)

    for k in 3..R+3:
        rows.append([sin(k*theta_j) for theta_j in theta])
        b.append(0)

    solve min ||A w - b||_2 subject to w >= 0

    prune weights below tolerance
    return theta_active, w_active
```

Use this to test robustness and to impose extra constraints, e.g. no nodes near endpoints:

\[
\theta_j\in[\theta_{\min},\pi-\theta_{\min}].
\]

Recommended:

\[
R=24,
\qquad
N_{\rm grid}=200,
\qquad
\theta_{\min}=0.05\pi.
\]

---

# 11. Output schema for the negative control

| field | meaning |
|---|---|
| `method` | deterministic sine / NNLS / LP |
| `R` | jet order killed |
| `N_nodes` | number of active nodes |
| `X0` | normalized half-width |
| `moment_max` | \(\max_{3\le k\le R+3}|\sum w_j\sin(k\theta_j)|\) |
| `normalization` | \(\sum w_j\sin\theta_j\) |
| `jet_max` | \(\max_{0\le r\le R}|J_r|\) |
| `E_X` | normalized interval energy |
| `S_X` | \(\sup_X |F|\) |
| `precision` | working precision |
| `quadrature_nodes` | integration nodes |
| `status` | pass/fail |

Pass criteria:

\[
|\sum w_j\sin\theta_j-1|\le 10^{-p},
\]

\[
\max_{3\le k\le R+3}|\mu_k|\le 10^{-p},
\]

\[
\max_{0\le r\le R}|J_r|\le 10^{-p}\cdot \max(1,(R+2)!),
\]

and

\[
E_X
\]

is many orders smaller than random-packet controls.

---

# 12. Comparison controls

To validate sensitivity, compare against random packet clusters.

## Random positive cluster

Choose

\[
\theta_j\sim \mathrm{Uniform}(0,\pi),
\qquad
w_j>0
\]

normalized by

\[
\sum_jw_j\sin\theta_j=1.
\]

Expected:

\[
J_0=Q''(0)
\]

and \(E_X\) are \(O(1)\) or at least not exponentially small in \(R\).

## Quadrature negative control

Expected:

\[
J_r=0
\quad(0\le r\le R),
\]

and

\[
E_X\ll1.
\]

The ratio

\[
\frac{E_X^{\rm quadrature}}{E_X^{\rm random}}
\]

should be tiny.

This confirms the Gate 1 numerical pipeline can distinguish genuine finite-jet source flattening from generic same-scale packets.

---

# 13. Expected output ranges

For deterministic sine quadrature:

- `moment_max`: near working precision, e.g. \(10^{-80}\) with 100-digit arithmetic.
- `jet_max`: near working precision times factorial scaling.
- `E_X`: roughly bounded by

\[
E_X\lesssim C\frac{N^4X_0^{2N-4}}{(1-X_0)^6}.
\]

For \(R=24,N=27,X_0=0.5\), expect very strong collapse.

For \(X_0=0.75\), expect less collapse but still much smaller than random controls.

---

# 14. Final recommendation

Use the deterministic sine quadrature as the mandatory first negative control:

\[
\theta_j=\frac{j\pi}{R+4},
\qquad
w_j=\frac{2}{R+4}\sin\theta_j,
\qquad
1\le j\le R+3.
\]

This exactly enforces

\[
\sum_jw_j\sin(k\theta_j)=0,
\qquad
2\le k\le R+3,
\]

and

\[
\sum_jw_j\sin\theta_j=1.
\]

It is positive, finite, stable, and simple to implement. If the Gate 1 diagnostic cannot detect collapse here, the actual-zeta numerical scan is not yet trustworthy.
## User (2026-04-26 14:34:22)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:34:29)

_Thought for 5s_

Agent 1/A — executable same-scale quadrature negative-control design.

The control validates that the Gate 1 pipeline can detect the known adversary before scanning actual zeta. The attached instruction asks for concrete code/pseudocode and parameter choices, not another strategic audit. 

## Mathematical construction

Use

\[
K_\theta(x)=\frac{\sin\theta}{(x-\cos\theta)^2+\sin^2\theta}.
\]

Since

\[
K_\theta(x)=\Im\frac{1}{x-e^{i\theta}},
\]

we have, for \(|x|<1\),

\[
K_\theta(x)=\sum_{n\ge0}x^n\sin((n+1)\theta),
\]

so

\[
\boxed{
K_\theta^{(n)}(0)=n!\sin((n+1)\theta).
}
\]

Set

\[
\theta_j=\frac{j\pi}{N+1},
\qquad
w_j=\frac{2}{N+1}\sin\theta_j,
\qquad
1\le j\le N.
\]

By discrete sine orthogonality,

\[
\sum_{j=1}^N w_j\sin(k\theta_j)=\delta_{k1},
\qquad
1\le k\le N.
\]

Therefore, if \(N\ge R+3\),

\[
\sum_j w_j\sin(k\theta_j)=0,
\qquad
3\le k\le R+3,
\]

and for

\[
Q(x)=\sum_j w_jK_{\theta_j}(x),
\qquad
F(x)=Q''(x),
\]

we get

\[
J_r:=F^{(r)}(0)=Q^{(r+2)}(0)=0,
\qquad
0\le r\le R.
\]

This is an exact positive finite quadrature negative control.

---

## Implementation-ready Python

```python
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def build_sine_quadrature(R: int, N: int | None = None):
    """
    Deterministic positive quadrature killing source-curvature jets through order R.

    Nodes:
        theta_j = j*pi/(N+1)
    Weights:
        w_j = 2/(N+1) * sin(theta_j)

    Need N >= R + 3.
    """
    if N is None:
        N = R + 3
    if N < R + 3:
        raise ValueError("Need N >= R + 3")

    j = np.arange(1, N + 1, dtype=float)
    theta = j * math.pi / (N + 1)
    weights = (2.0 / (N + 1)) * np.sin(theta)
    return theta, weights

def K(theta, x):
    s = np.sin(theta)
    c = np.cos(theta)
    return s / ((x - c) ** 2 + s ** 2)

def K_second(theta, x):
    """
    Analytic second derivative of K_theta(x).

    K = s / ((x-c)^2+s^2)
    K'' = s * (6(x-c)^2 - 2s^2) / ((x-c)^2+s^2)^3
    """
    s = np.sin(theta)
    c = np.cos(theta)
    y = x - c
    denom = y * y + s * s
    return s * (6.0 * y * y - 2.0 * s * s) / (denom ** 3)

def Q(theta, weights, x):
    return np.sum(weights * K(theta, x))

def F(theta, weights, x):
    """
    F(x) = Q''(x).
    """
    return np.sum(weights * K_second(theta, x))

def moment(theta, weights, k: int):
    """
    mu_k = sum_j w_j sin(k theta_j).
    """
    return float(np.sum(weights * np.sin(k * theta)))

def jet(theta, weights, r: int):
    """
    J_r = F^(r)(0) = Q^(r+2)(0)
        = (r+2)! * sum_j w_j sin((r+3) theta_j)
    """
    n = r + 2
    k = n + 1
    return math.factorial(n) * moment(theta, weights, k)

def compute_E_X(theta, weights, X0=0.5, nquad=256):
    """
    E_X = |X|^{-1} int_{-X0}^{X0} |F(x)|^2 dx.
    """
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts

    vals = np.array([F(theta, weights, x) for x in xs])
    integral = float(np.sum(ws * np.abs(vals) ** 2))
    return integral / (2.0 * X0)

def compute_S_X(theta, weights, X0=0.5, ngrid=2001):
    """
    Sup diagnostic on a dense grid.
    """
    xs = np.linspace(-X0, X0, ngrid)
    vals = np.array([abs(F(theta, weights, x)) for x in xs])
    return float(np.max(vals))

def run_negative_control(R=24, X0=0.5, N=None, nquad=512):
    theta, weights = build_sine_quadrature(R, N=N)

    # Moment checks
    normalization = moment(theta, weights, 1)
    moment_max_2_to_R3 = max(abs(moment(theta, weights, k)) for k in range(2, R + 4))
    moment_max_3_to_R3 = max(abs(moment(theta, weights, k)) for k in range(3, R + 4))

    # Jet checks
    jets = np.array([jet(theta, weights, r) for r in range(R + 1)])
    jet_max = float(np.max(np.abs(jets)))
    jet_rms = float(np.sqrt(np.sum(np.abs(jets) ** 2)))

    # Interval diagnostics
    E_X = compute_E_X(theta, weights, X0=X0, nquad=nquad)
    S_X = compute_S_X(theta, weights, X0=X0)

    return {
        "R": R,
        "N": len(theta),
        "X0": X0,
        "normalization_mu1": normalization,
        "moment_max_2_to_R3": moment_max_2_to_R3,
        "moment_max_3_to_R3": moment_max_3_to_R3,
        "jet_max": jet_max,
        "jet_rms": jet_rms,
        "E_X": E_X,
        "S_X": S_X,
        "theta": theta,
        "weights": weights,
    }

def random_positive_control(N=27, X0=0.5, nquad=512, seed=0):
    """
    Random positive packet cluster for comparison.
    Normalized so sum w_j sin(theta_j) = 1.
    """
    rng = np.random.default_rng(seed)
    theta = np.sort(rng.uniform(0.05 * math.pi, 0.95 * math.pi, size=N))
    raw_w = rng.exponential(scale=1.0, size=N)
    weights = raw_w / np.sum(raw_w * np.sin(theta))

    E_X = compute_E_X(theta, weights, X0=X0, nquad=nquad)
    S_X = compute_S_X(theta, weights, X0=X0)
    return {
        "N": N,
        "X0": X0,
        "normalization_mu1": moment(theta, weights, 1),
        "E_X": E_X,
        "S_X": S_X,
        "theta": theta,
        "weights": weights,
    }

if __name__ == "__main__":
    for R in [12, 24, 40]:
        for X0 in [0.25, 0.5, 0.75]:
            result = run_negative_control(R=R, X0=X0, nquad=512)
            print({
                k: result[k]
                for k in [
                    "R",
                    "N",
                    "X0",
                    "normalization_mu1",
                    "moment_max_3_to_R3",
                    "jet_max",
                    "E_X",
                    "S_X",
                ]
            })

    rnd = random_positive_control(N=27, X0=0.5)
    print("Random control:", {k: rnd[k] for k in ["N", "X0", "E_X", "S_X"]})
```

---

## Recommended parameter sets

Use these first:

| Run | \(R\) | \(N\) | \(X_0\) | Purpose |
|---:|---:|---:|---:|---|
| 1 | 12 | 15 | 0.25 | easy sanity check |
| 2 | 12 | 15 | 0.5 | baseline negative control |
| 3 | 24 | 27 | 0.5 | strong negative control |
| 4 | 24 | 27 | 0.75 | wider interval stress test |
| 5 | 40 | 43 | 0.5 | high-order collapse test |

For each run, compare against random positive clusters with the same \(N\) and \(X_0\).

---

## Expected output ranges

For deterministic quadrature:

\[
\sum_jw_j\sin\theta_j=1
\]

to numerical precision.

\[
\max_{3\le k\le R+3}
\left|\sum_jw_j\sin(k\theta_j)\right|
\]

should be near machine precision, usually \(10^{-14}\) to \(10^{-15}\) in double precision. With arbitrary precision, it should drop accordingly.

\[
J_r=F^{(r)}(0)
\]

should be near numerical zero for \(0\le r\le R\). Because factorials grow quickly, inspect both raw \(J_r\) and normalized moments

\[
\mu_{r+3}=\sum_jw_j\sin((r+3)\theta_j).
\]

For \(X_0<1\), the energy should decay approximately like

\[
E_X
\lesssim
C\,N^4X_0^{2N-4}(1-X_0)^{-6}.
\]

So:

- \(X_0=0.25\): collapse should be very strong.
- \(X_0=0.5\): strong collapse.
- \(X_0=0.75\): visible but less dramatic.
- Random positive controls should have much larger \(E_X\).

---

## Physical rescaling

For a physical packet scale \(\lambda\),

\[
m=m_0+\lambda x,
\]

\[
q_{\rm synth}(m_0+\lambda x)=\lambda^{-1}Q(x),
\]

\[
q_{\rm synth}''(m_0+\lambda x)=\lambda^{-3}F(x).
\]

For

\[
I=m_0+\lambda[-X_0,X_0],
\]

the physical energy is

\[
E_I=|I|^{-1}\int_I |q_{\rm synth}''(m)|^2\,dm
=\lambda^{-6}E_X.
\]

Therefore record both:

\[
E_I
\]

and the normalized energy

\[
\lambda^6E_I=E_X.
\]

The normalized energy \(E_X\) is the meaningful negative-control flatness diagnostic.

---

## Pass/fail checklist

The negative control passes if:

1. **Normalization holds:**

\[
\left|\sum_jw_j\sin\theta_j-1\right|\le 10^{-12}
\]

in double precision, or near working precision in arbitrary precision.

2. **Moments vanish:**

\[
\max_{3\le k\le R+3}
\left|\sum_jw_j\sin(k\theta_j)\right|
\le 10^{-12}.
\]

3. **Jets vanish:**

\[
\max_{0\le r\le R}|F^{(r)}(0)|
\]

is consistent with moment precision after factorial scaling.

4. **Energy collapses:**

\[
E_X^{\rm quadrature}\ll E_X^{\rm random}.
\]

A useful criterion:

\[
\frac{E_X^{\rm quadrature}}{E_X^{\rm random}}\le 10^{-4}
\]

for the baseline \(R=12,X_0=0.5\), and far smaller for \(R=24,X_0=0.5\).

5. **Width sensitivity behaves correctly:**

\[
E_X(X_0=0.25)<E_X(X_0=0.5)<E_X(X_0=0.75)
\]

up to constants, because the finite-jet flatness is centered at \(0\) and weakens as the interval approaches the pole circle.

---

## Output schema

| field | meaning |
|---|---|
| `method` | deterministic sine / NNLS / random control |
| `R` | killed jet depth |
| `N` | number of nodes |
| `X0` | normalized half-width |
| `normalization_mu1` | \(\sum_jw_j\sin\theta_j\) |
| `moment_max_3_to_R3` | max killed moment |
| `jet_max` | max raw killed jet |
| `jet_rms` | RMS killed jets |
| `E_X` | normalized interval energy |
| `S_X` | normalized sup |
| `E_random` | random packet energy |
| `ratio_to_random` | \(E_X/E_{\rm random}\) |
| `status` | pass / fail |

---

## Minimum implementation sequence

1. Run deterministic sine quadrature with:

\[
R=12,\quad N=15,\quad X_0=0.5.
\]

2. Run random positive control with:

\[
N=15,\quad X_0=0.5.
\]

3. Confirm:

\[
E_X^{\rm quadrature}\ll E_X^{\rm random}.
\]

4. Repeat with:

\[
R=24,\quad N=27,\quad X_0=0.5.
\]

5. Repeat with \(X_0=0.75\) to ensure the control remains detectable on wider intervals.

Only after this control passes should actual-zero or AFE scans be trusted.
## User (2026-04-26 14:37:55)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:37:56)

I’ll handle Agent 1/A: review the deterministic quadrature control for numerical pitfalls, choose analytic evaluation paths, and provide expected output ranges and pass/fail criteria.

_Thought for 3m 20s_

Agent 1/A — negative-control code review and expected output table.

## 1. Main code-review findings

The deterministic sine-quadrature control is mathematically exact:

\[
\theta_j=\frac{j\pi}{N+1},
\qquad
w_j=\frac{2}{N+1}\sin\theta_j,
\qquad
1\le j\le N,
\]

and

\[
\sum_{j=1}^N w_j\sin(k\theta_j)=\delta_{k1},
\qquad 1\le k\le N.
\]

So for \(N\ge R+3\),

\[
J_r=F^{(r)}(0)=0,
\qquad 0\le r\le R.
\]

This is the right first negative control for the Gate 1 harness. The attached prompt asks specifically for code-review, expected output, and pass/fail criteria for this control. 

---

# 2. Numerical pitfalls and fixes

## Pitfall A — factorial overflow / misleading raw \(J_r\)

Since

\[
J_r=F^{(r)}(0)
=
(r+2)!\sum_j w_j\sin((r+3)\theta_j),
\]

raw \(J_r\) is dangerous at large \(R\). Even if the moment residual is only \(10^{-15}\), multiplying by \((r+2)!\) can produce huge-looking values.

For example, at \(r=40\),

\[
42!\approx 1.4\times10^{51}.
\]

So double precision moment error \(10^{-15}\) becomes raw jet error \(\sim10^{36}\).

**Fix:** always report normalized jets

\[
\widehat J_r
:=
\frac{J_r}{(r+2)!}
=
\sum_jw_j\sin((r+3)\theta_j).
\]

For negative-control validation, use \(\widehat J_r\), not raw \(J_r\), unless using arbitrary precision.

---

## Pitfall B — floating-point cancellation in moments

The moments vanish by exact discrete orthogonality, but floating arithmetic evaluates large cancelling sums. In double precision, expect residuals around

\[
10^{-14}\text{ to }10^{-15}
\]

for \(R\le 40\). That is fine for smoke tests but not for high-order jet validation.

**Fixes:**

1. For moment tests, use the closed-form identity when validating logic:

\[
\sum_j w_j\sin(k\theta_j)=\delta_{k1}.
\]

2. For numerical implementation testing, compute with `mpmath` at 80–150 decimal digits for \(R=40\).

3. Record both:
   - `moment_max_normalized`;
   - `raw_jet_max`, clearly marked as factorial-amplified.

---

## Pitfall C — numerical differentiation

Do not compute

\[
F=Q''
\]

by finite differences. Finite differences will corrupt the cancellation, especially for \(R=24,40\).

**Use analytic derivatives.**

Given

\[
K_\theta(x)=\frac{s}{(x-c)^2+s^2},
\qquad
s=\sin\theta,\quad c=\cos\theta,
\]

we have

\[
K_\theta''(x)
=
\frac{s\left(6(x-c)^2-2s^2\right)}
{\left((x-c)^2+s^2\right)^3}.
\]

Therefore

\[
F(x)=Q''(x)=\sum_j w_jK_{\theta_j}''(x).
\]

This is stable enough for the first runs.

---

## Pitfall D — \(X_0\to1\) approaches the pole circle

The normalized kernels have poles at

\[
x=e^{\pm i\theta}
\]

at distance one from the origin. The Taylor/quadrature flattening is strongest well inside \(|x|<1\). As \(X_0\to1\), the high-order tail matters and \(E_X\) grows.

So:

\[
X_0=0.25
\]

should show dramatic collapse,

\[
X_0=0.5
\]

should be the baseline,

\[
X_0=0.75
\]

is a stress test, not the first-pass criterion.

Do not use \(X_0\ge0.9\) in the initial validation.

---

## Pitfall E — quadrature errors near narrow features

For \(X_0=0.75\) and larger \(N\), \(F(x)\) can have structure near the ends of the interval. Gauss–Legendre quadrature should be refined.

Use:

\[
N_{\rm quad}=256
\]

for smoke tests,

\[
N_{\rm quad}=512\text{ or }1024
\]

for \(R=24,40\),

and require relative stability under doubling.

---

# 3. Recommended implementation choices

## Use analytic \(F=Q''\)

Use:

```python
def K_second(theta, x):
    s = sin(theta)
    c = cos(theta)
    y = x - c
    den = y*y + s*s
    return s * (6*y*y - 2*s*s) / den**3
```

Then:

```python
F(x) = sum_j w_j * K_second(theta_j, x)
```

## Use normalized jet moments

Instead of raw:

\[
J_r=F^{(r)}(0),
\]

report:

\[
\widehat J_r
=
\sum_j w_j\sin((r+3)\theta_j).
\]

Then optionally compute raw jets in log form:

\[
\log |J_r|
=
\log((r+2)!)+\log|\widehat J_r|.
\]

## Use high precision for \(R=40\)

Recommended:

| \(R\) | precision |
|---:|---:|
| 12 | double OK; 80-digit preferred |
| 24 | double OK for \(E_X\), 80-digit for moments |
| 40 | 120–150 digit precision recommended |

---

# 4. Expected output table

The exact values depend on implementation precision, but these are the expected order ranges. The key comparison is against random positive packet clusters with the same \(N\) and \(X_0\).

Use:

\[
N=R+3.
\]

## Table A — deterministic quadrature expected output

| \(R\) | \(N\) | \(X_0\) | `moment_max_normalized` | `normalized_jet_max` | expected \(E_X\) | expected \(S_X\) |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 15 | 0.25 | \(10^{-14}\) double / \(10^{-70}\) mp | same | \(10^{-8}\)–\(10^{-12}\) | \(10^{-4}\)–\(10^{-6}\) |
| 12 | 15 | 0.50 | \(10^{-14}\) double / \(10^{-70}\) mp | same | \(10^{-3}\)–\(10^{-6}\) | \(10^{-1}\)–\(10^{-3}\) |
| 12 | 15 | 0.75 | \(10^{-14}\) double / \(10^{-70}\) mp | same | \(10^{-1}\)–\(10^{1}\) | \(10^0\)–\(10^1\) |
| 24 | 27 | 0.25 | \(10^{-13}\) double / \(10^{-100}\) mp | same | \(10^{-20}\)–\(10^{-30}\) | \(10^{-9}\)–\(10^{-13}\) |
| 24 | 27 | 0.50 | \(10^{-13}\) double / \(10^{-100}\) mp | same | \(10^{-8}\)–\(10^{-12}\) | \(10^{-4}\)–\(10^{-6}\) |
| 24 | 27 | 0.75 | \(10^{-13}\) double / \(10^{-100}\) mp | same | \(10^{-2}\)–\(10^{0}\) | \(10^{-1}\)–\(10^0\) |
| 40 | 43 | 0.25 | \(10^{-12}\) double / \(10^{-120}\) mp | same | \(10^{-35}\)–\(10^{-50}\) | \(10^{-16}\)–\(10^{-22}\) |
| 40 | 43 | 0.50 | \(10^{-12}\) double / \(10^{-120}\) mp | same | \(10^{-15}\)–\(10^{-22}\) | \(10^{-7}\)–\(10^{-10}\) |
| 40 | 43 | 0.75 | \(10^{-12}\) double / \(10^{-120}\) mp | same | \(10^{-4}\)–\(10^{-1}\) | \(10^{-2}\)–\(10^{-1}\) |

These are ranges, not exact commitments. The robust expectation is monotonic:

\[
E_X(R=40)<E_X(R=24)<E_X(R=12)
\]

for fixed \(X_0<1\), and

\[
E_X(X_0=0.25)<E_X(X_0=0.5)<E_X(X_0=0.75)
\]

for fixed \(R\).

## Table B — ratio to random packet controls

| \(R\) | \(X_0\) | expected \(E_X^{\rm quad}/E_X^{\rm random}\) |
|---:|---:|---:|
| 12 | 0.25 | \(\le 10^{-6}\) |
| 12 | 0.50 | \(\le 10^{-3}\) to \(10^{-5}\) |
| 12 | 0.75 | may be only \(10^{-1}\) to \(1\); stress case |
| 24 | 0.25 | \(\le 10^{-15}\) |
| 24 | 0.50 | \(\le 10^{-6}\) to \(10^{-10}\) |
| 24 | 0.75 | \(\le 10^{-2}\) to \(10^{-4}\) if stable |
| 40 | 0.25 | \(\le 10^{-25}\) |
| 40 | 0.50 | \(\le 10^{-12}\) to \(10^{-18}\) |
| 40 | 0.75 | \(\le 10^{-3}\) to \(10^{-6}\) if stable |

If the ratio is not small at \(X_0=0.5\), the implementation is likely wrong.

---

# 5. Exact pass/fail thresholds

## Smoke-test thresholds, double precision

For \(R=12,N=15,X_0=0.5\):

Pass if:

\[
\left|\sum_jw_j\sin\theta_j-1\right|\le10^{-12},
\]

\[
\max_{3\le k\le R+3}
\left|\sum_jw_j\sin(k\theta_j)\right|\le10^{-12},
\]

\[
\max_{0\le r\le R}|\widehat J_r|\le10^{-12},
\]

\[
\frac{E_X^{\rm quad}}{E_X^{\rm random}}\le10^{-3}.
\]

Strong pass if:

\[
\frac{E_X^{\rm quad}}{E_X^{\rm random}}\le10^{-5}.
\]

## Production-control thresholds, high precision

For \(R=24,N=27,X_0=0.5\), with at least 80-digit arithmetic:

Pass if:

\[
\max_{3\le k\le R+3}|\mu_k|\le10^{-50},
\]

\[
\max_{0\le r\le R}|\widehat J_r|\le10^{-50},
\]

\[
\frac{E_X^{\rm quad}}{E_X^{\rm random}}\le10^{-6}.
\]

Strong pass:

\[
\frac{E_X^{\rm quad}}{E_X^{\rm random}}\le10^{-10}.
\]

## High-order stress

For \(R=40,N=43,X_0=0.5\), with 120–150 digit arithmetic:

Pass if:

\[
\max_{3\le k\le R+3}|\mu_k|\le10^{-80},
\]

\[
\frac{E_X^{\rm quad}}{E_X^{\rm random}}\le10^{-12}.
\]

---

# 6. Recommended precision settings

| Run | Precision | Notes |
|---|---:|---|
| \(R=12\) smoke | double OK | moments around \(10^{-14}\) acceptable |
| \(R=12\) validation | 80 digits | confirms exact cancellation |
| \(R=24\) baseline | 80 digits | recommended default |
| \(R=40\) stress | 120–150 digits | avoid factorial/moment amplification |
| \(X_0=0.75\) | +20 extra digits | endpoint stress, more cancellation sensitivity |

For \(R=40\), do not use raw \(J_r\) in double precision.

---

# 7. Ready-to-run checklist

## Before run

- [ ] Use deterministic nodes

\[
\theta_j=j\pi/(N+1).
\]

- [ ] Use positive weights

\[
w_j=\frac{2}{N+1}\sin\theta_j.
\]

- [ ] Set \(N\ge R+3\).
- [ ] Use analytic \(K_\theta''(x)\), not finite differences.
- [ ] Report normalized jets \(\widehat J_r=J_r/(r+2)!\).
- [ ] Use \(X_0=0.5\) for baseline.
- [ ] Use random positive packet cluster as comparison.

## During run

- [ ] Check

\[
\sum_jw_j\sin\theta_j\approx1.
\]

- [ ] Check killed moments

\[
\mu_k\approx0,\quad3\le k\le R+3.
\]

- [ ] Check normalized killed jets

\[
\widehat J_r\approx0,\quad0\le r\le R.
\]

- [ ] Compute \(E_X\) with Gauss–Legendre quadrature.
- [ ] Double quadrature order and confirm stability.
- [ ] Compute \(S_X=\sup_X|F|\) on a dense grid.

## After run

- [ ] Compare against random packet control.
- [ ] Confirm \(E_X^{\rm quad}/E_X^{\rm random}\) is small.
- [ ] Confirm larger \(R\) improves flatness at fixed \(X_0<1\).
- [ ] Confirm larger \(X_0\) weakens flatness, especially near \(0.75\).
- [ ] If any of these fail, debug before actual-zeta scans.

---

# 8. Minimal run suite

Run in this order:

1. **Smoke:**

\[
R=12,\quad N=15,\quad X_0=0.5,\quad \text{double precision}.
\]

2. **Baseline:**

\[
R=24,\quad N=27,\quad X_0=0.5,\quad 80\text{-digit precision}.
\]

3. **Width check:**

\[
R=24,\quad X_0=0.25,0.5,0.75.
\]

4. **High-order stress:**

\[
R=40,\quad N=43,\quad X_0=0.5,\quad 120\text{-digit precision}.
\]

5. **Random controls:**

For each \((R,X_0)\), run at least 20 random positive clusters with the same \(N\), normalized by

\[
\sum_jw_j\sin\theta_j=1.
\]

Report median and minimum random \(E_X\).

---

# 9. Final readiness verdict

\[
\boxed{
\text{The negative-control construction is ready to run.}
}
\]

Use analytic \(F=Q''\), normalized jets, and \(X_0=0.5\) as the baseline. The deterministic sine quadrature should produce exact moment and jet cancellation through order \(R\), and \(E_X\) should be far below random positive packet controls.

If this control does not pass, no actual-zero Gate 1 scan should be trusted.
## User (2026-04-26 14:42:00)

OK run it

## Assistant (2026-04-26 14:42:05)

I’ll run the deterministic sine-quadrature negative control and compare it against random positive packet clusters. I’ll report normalized moments/jets, \(E_X\), \(S_X\), and ratio-to-random for the requested \(R,X_0\) grid.

_Thought for 6m 17s_

I attempted to run the deterministic sine-quadrature negative control, but the execution backend timed out even on trivial commands, so I cannot honestly report real numeric output from this session.

What I can confirm from the mathematical construction is that the deterministic control should pass exactly up to numerical precision:

\[
\theta_j=\frac{j\pi}{N+1},\qquad
w_j=\frac{2}{N+1}\sin\theta_j,
\]

\[
\sum_{j=1}^N w_j\sin(k\theta_j)=\delta_{k1},\qquad 1\le k\le N.
\]

Thus for \(N\ge R+3\),

\[
F^{(r)}(0)=0,\qquad 0\le r\le R.
\]

This is the mandatory first negative-control test requested in the latest execution prompt. 

## Ready-to-run script

```python
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def build_sine_quadrature(R, N=None):
    if N is None:
        N = R + 3
    if N < R + 3:
        raise ValueError("Need N >= R + 3")
    j = np.arange(1, N + 1, dtype=float)
    theta = j * math.pi / (N + 1)
    weights = (2.0 / (N + 1)) * np.sin(theta)
    return theta, weights

def K_second(theta, x):
    s = np.sin(theta)
    c = np.cos(theta)
    y = x - c
    den = y*y + s*s
    return s * (6*y*y - 2*s*s) / den**3

def F(theta, weights, x):
    return float(np.sum(weights * K_second(theta, x)))

def moment(theta, weights, k):
    return float(np.sum(weights * np.sin(k * theta)))

def normalized_jet(theta, weights, r):
    # F^(r)(0)/(r+2)! = sum_j w_j sin((r+3) theta_j)
    return moment(theta, weights, r + 3)

def compute_E_X(theta, weights, X0=0.5, nquad=512):
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts
    vals = np.array([F(theta, weights, x) for x in xs])
    integral = np.sum(ws * vals * vals)
    return float(integral / (2 * X0))

def compute_S_X(theta, weights, X0=0.5, ngrid=5001):
    xs = np.linspace(-X0, X0, ngrid)
    vals = np.array([abs(F(theta, weights, x)) for x in xs])
    return float(np.max(vals))

def random_positive_control(N, X0=0.5, seed=0, nquad=512):
    rng = np.random.default_rng(seed)
    theta = np.sort(rng.uniform(0.05 * math.pi, 0.95 * math.pi, size=N))
    raw = rng.exponential(size=N)
    weights = raw / np.sum(raw * np.sin(theta))
    return compute_E_X(theta, weights, X0=X0, nquad=nquad)

def run_case(R, X0, nquad=512):
    theta, weights = build_sine_quadrature(R)
    N = len(theta)

    mu1 = moment(theta, weights, 1)
    killed_moment_max = max(abs(moment(theta, weights, k)) for k in range(3, R + 4))
    norm_jet_max = max(abs(normalized_jet(theta, weights, r)) for r in range(R + 1))

    E_X = compute_E_X(theta, weights, X0=X0, nquad=nquad)
    S_X = compute_S_X(theta, weights, X0=X0)

    random_Es = [random_positive_control(N, X0=X0, seed=s, nquad=256) for s in range(20)]
    random_median = float(np.median(random_Es))
    ratio = E_X / random_median

    return {
        "R": R,
        "N": N,
        "X0": X0,
        "mu1": mu1,
        "killed_moment_max": killed_moment_max,
        "normalized_jet_max": norm_jet_max,
        "E_X": E_X,
        "S_X": S_X,
        "random_E_median": random_median,
        "ratio_to_random": ratio,
    }

if __name__ == "__main__":
    cases = [
        (12, 0.25), (12, 0.50), (12, 0.75),
        (24, 0.25), (24, 0.50), (24, 0.75),
        (40, 0.25), (40, 0.50), (40, 0.75),
    ]

    for R, X0 in cases:
        row = run_case(R, X0)
        print(row)
```

## Pass criteria

For the baseline \(R=12,N=15,X_0=0.5\), it should pass if:

\[
|\mu_1-1|\le 10^{-12},
\]

\[
\max_{3\le k\le R+3}|\mu_k|\le 10^{-12},
\]

\[
\max_{0\le r\le R}|\widehat J_r|\le 10^{-12},
\]

and

\[
E_X^{\rm quadrature}/E_X^{\rm random}\le 10^{-3}.
\]

For \(R=24,X_0=0.5\), the ratio should be much smaller; with high precision, typically \(\le 10^{-6}\) and often far below that.
## User (2026-04-26 15:03:34)

OK run the next step

## Assistant (2026-04-26 15:03:39)

I’ll run the next control stage: singular/shallow packet dominance versus singular same-scale cancellation. I’ll compute normalized source energy and Gate 2 mass for \(c=10^{-2},10^{-3},10^{-4}\), comparing a single packet, random cluster, and quadrature-cancelled cluster.

_Stopped thinking_
## User (2026-04-26 15:04:15)

Try to re-run what failed

## Assistant (2026-04-26 15:04:17)

I’ll retry the failed deterministic sine-quadrature run first, then report the actual numeric table. If it succeeds, I’ll keep this to the baseline negative-control grid before moving to singular controls.

_Thought for 7s_

The first retry hit the 60-second visible-code limit during the random-control comparisons. I’ll rerun a vectorized version and keep the random controls to 5 samples per case so we get actual numbers quickly.

The optimized run still timed out, likely during the repeated random-control integrations. I’ll strip it to the deterministic control only, which is the failed core test, then add random comparisons later if needed.

_Thought for 7m 0s_

Tried to rerun the failed deterministic negative-control test, but the execution environment is still timing out, including on a trivial `print("hello")` command. So this is not a code-performance issue in the quadrature script; the backend execution channel itself is currently not returning.

What I attempted:

1. Full deterministic quadrature + random controls.
2. Vectorized deterministic quadrature + reduced random controls.
3. Deterministic-only quadrature with no random controls.
4. Minimal shell/Python sanity check.

All timed out.

The test remains mathematically ready to run. The key exact check is:

\[
\theta_j=\frac{j\pi}{N+1},\qquad
w_j=\frac{2}{N+1}\sin\theta_j,
\]

\[
\sum_{j=1}^{N} w_j\sin(k\theta_j)=\delta_{k1}.
\]

Thus for \(N\ge R+3\),

\[
F^{(r)}(0)=0,\qquad 0\le r\le R.
\]

This is exactly the deterministic negative control the latest agent prompt asked us to execute first. 

Given the execution failure, the next practical move is to run the ready-to-run script locally or in a fresh execution environment. I should not fabricate numeric \(E_X\), \(S_X\), or ratio-to-random values from a run that did not complete.
## User (2026-04-26 15:11:55)

retry running everything on a fresh environment

## Assistant (2026-04-26 15:11:56)

I’ll rerun the deterministic control and singular controls using a fresh internal execution path, then report only completed numerical results. I’ll keep the first pass lean: deterministic quadrature table, random comparison table, then singular dominance/cancellation scalings.

_Stopped thinking_
## User (2026-04-26 15:14:31)

ok give me the exact python script to run, then I'll run it for you

## Assistant (2026-04-26 15:14:33)

Save this as `gate1_controls.py` and run:

```bash
python gate1_controls.py
```

It uses only `numpy` and standard-library modules.

```python
#!/usr/bin/env python3
"""
Gate 1 numerical controls:
1. Deterministic same-scale quadrature negative control.
2. Random positive packet comparison.
3. Singular/shallow packet dominance and cancellation controls.

Run:
    python gate1_controls.py

Optional:
    python gate1_controls.py --fast
    python gate1_controls.py --out gate1_controls_results.csv
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss

# ----------------------------
# Shared normalized packet model
# ----------------------------

def build_sine_quadrature(R: int, N: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    """
    Deterministic positive same-scale quadrature.

    theta_j = j*pi/(N+1), j=1..N
    w_j = 2/(N+1) sin(theta_j)

    Then sum_j w_j sin(k theta_j) = delta_{k1}, 1 <= k <= N.
    Need N >= R+3 to kill F^(r)(0), r=0..R, where F=Q''.
    """
    if N is None:
        N = R + 3
    if N < R + 3:
        raise ValueError(f"Need N >= R+3; got N={N}, R={R}")

    j = np.arange(1, N + 1, dtype=np.float64)
    theta = j * math.pi / (N + 1)
    weights = (2.0 / (N + 1)) * np.sin(theta)
    return theta, weights

def build_random_positive_cluster(
    N: int,
    seed: int,
    theta_min: float = 0.05 * math.pi,
    theta_max: float = 0.95 * math.pi,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Random positive packet cluster, normalized by sum_j w_j sin(theta_j)=1.
    """
    rng = np.random.default_rng(seed)
    theta = np.sort(rng.uniform(theta_min, theta_max, size=N))
    raw = rng.exponential(scale=1.0, size=N)
    weights = raw / np.sum(raw * np.sin(theta))
    return theta, weights

def moments(theta: np.ndarray, weights: np.ndarray, ks: Iterable[int]) -> np.ndarray:
    return np.array([np.sum(weights * np.sin(k * theta)) for k in ks], dtype=np.float64)

def K(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    K_theta(x) = sin(theta) / ((x-cos(theta))^2 + sin(theta)^2)

    Vectorized:
      theta shape: (N,)
      x shape: (M,)
      returns shape: (M,N)
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    return s / ((xx - c) ** 2 + s ** 2)

def K_second(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Analytic second derivative of K_theta(x).

    K = s / ((x-c)^2 + s^2)
    K'' = s * (6(x-c)^2 - 2s^2) / ((x-c)^2+s^2)^3
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y * y + s * s
    return s * (6.0 * y * y - 2.0 * s * s) / (den ** 3)

def K_fourth(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Analytic fourth derivative of K_theta(x).

    Let y=x-c, a=s. For K=a/(y^2+a^2):
    K'''' = 24*a*(16*y^4 - 12*a^2*y^2 + a^4) / (y^2+a^2)^5
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y * y + s * s
    numerator = 24.0 * s * (16.0 * y**4 - 12.0 * s**2 * y**2 + s**4)
    return numerator / (den**5)

def eval_Q(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    return K(theta, x) @ weights

def eval_F(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    """F(x)=Q''(x)."""
    return K_second(theta, x) @ weights

def eval_Q4(theta: np.ndarray, weights: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Q^{(4)}(x)."""
    return K_fourth(theta, x) @ weights

def compute_E_and_S(
    theta: np.ndarray,
    weights: np.ndarray,
    X0: float,
    nquad: int = 256,
    ngrid: int = 2001,
) -> tuple[float, float]:
    """
    E_X = |X|^{-1} int_X |F(x)|^2 dx, X=[-X0,X0]
    S_X = sup_X |F(x)| approximated on a dense grid.
    """
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts
    F_vals = eval_F(theta, weights, xs)
    E_X = float(np.sum(ws * F_vals * F_vals) / (2.0 * X0))

    grid = np.linspace(-X0, X0, ngrid)
    S_X = float(np.max(np.abs(eval_F(theta, weights, grid))))
    return E_X, S_X

@dataclass
class NegativeControlRow:
    R: int
    N: int
    X0: float
    mu1_error: float
    killed_moment_max: float
    normalized_jet_max: float
    E_X: float
    S_X: float
    random_E_median: float
    ratio_to_random: float

def run_negative_control_case(
    R: int,
    X0: float,
    nquad: int,
    ngrid: int,
    n_random: int,
) -> NegativeControlRow:
    theta, weights = build_sine_quadrature(R)
    N = len(theta)

    mu1_error = abs(float(np.sum(weights * np.sin(theta))) - 1.0)

    ks = range(3, R + 4)
    killed_moment_max = float(np.max(np.abs(moments(theta, weights, ks))))
    normalized_jet_max = killed_moment_max  # F^(r)(0)/(r+2)! = moment k=r+3

    E_X, S_X = compute_E_and_S(theta, weights, X0, nquad=nquad, ngrid=ngrid)

    random_Es = []
    for seed in range(n_random):
        th_r, w_r = build_random_positive_cluster(N, seed=10_000 + 997 * R + 31 * seed)
        E_r, _ = compute_E_and_S(th_r, w_r, X0, nquad=max(64, nquad // 2), ngrid=max(501, ngrid // 4))
        random_Es.append(E_r)

    random_E_median = float(np.median(random_Es))
    ratio_to_random = float(E_X / random_E_median) if random_E_median > 0 else float("nan")

    return NegativeControlRow(
        R=R,
        N=N,
        X0=X0,
        mu1_error=mu1_error,
        killed_moment_max=killed_moment_max,
        normalized_jet_max=normalized_jet_max,
        E_X=E_X,
        S_X=S_X,
        random_E_median=random_E_median,
        ratio_to_random=ratio_to_random,
    )

# ----------------------------
# Singular controls
# ----------------------------

@dataclass
class SingularRow:
    label: str
    c: float
    X0: float
    E_u_norm: float
    E_u_physical: float
    gate2_norm: float
    gate2_physical: float
    S_u_norm: float
    S_gammaG_norm: float
    S_gammaG2_norm: float

def compute_singular_diagnostics(
    theta: np.ndarray,
    weights: np.ndarray,
    c_scale: float,
    X0: float,
    label: str,
    nquad: int = 256,
    ngrid: int = 2001,
) -> SingularRow:
    """
    Normalized model:
      q(m)=c^{-1} Q(x)
      u=q''=c^{-3} Q''(x)
      q^(4)=c^{-5} Q^(4)(x)

    Physical dm = c dx. Physical interval length = c |X|.
    Mean physical E_u = |I|^{-1} int |u|^2 dm = c^{-6} * mean_X |Q''|^2.

    Gate2 physical mean:
      |I|^{-1} int |u|^2 (GammaG^2+GammaG2^2) dm
    computed directly from scaled quantities.
    """
    nodes, wgts = leggauss(nquad)
    xs = X0 * nodes
    ws = X0 * wgts

    Q = eval_Q(theta, weights, xs)
    Q2 = eval_F(theta, weights, xs)
    Q4 = eval_Q4(theta, weights, xs)

    q = c_scale ** -1 * Q
    u = c_scale ** -3 * Q2
    q4 = c_scale ** -5 * Q4

    gammaG = u - 6.0 * q + 2.0 * q**3
    gammaG2 = (1.0 - q**2) * u - (1.0 / 6.0) * q4

    E_u_physical = float(np.sum(ws * u * u) / (2.0 * X0))
    gate2_physical = float(np.sum(ws * (u * u) * (gammaG * gammaG + gammaG2 * gammaG2)) / (2.0 * X0))

    # Normalized diagnostics:
    # E_u_norm = mean_X |Q''|^2
    E_u_norm = float(np.sum(ws * Q2 * Q2) / (2.0 * X0))

    # Gate2 normalized by dominant singular c^{-16} factor:
    # integrand dominated by u^2 * gammaG2^2 ~ c^{-16}, so multiply by c^16.
    gate2_norm = gate2_physical * (c_scale ** 16)

    grid = np.linspace(-X0, X0, ngrid)
    Qg = eval_Q(theta, weights, grid)
    Q2g = eval_F(theta, weights, grid)
    Q4g = eval_Q4(theta, weights, grid)

    qg = c_scale ** -1 * Qg
    ug = c_scale ** -3 * Q2g
    q4g = c_scale ** -5 * Q4g
    gammaGg = ug - 6.0 * qg + 2.0 * qg**3
    gammaG2g = (1.0 - qg**2) * ug - (1.0 / 6.0) * q4g

    return SingularRow(
        label=label,
        c=c_scale,
        X0=X0,
        E_u_norm=E_u_norm,
        E_u_physical=E_u_physical,
        gate2_norm=gate2_norm,
        gate2_physical=gate2_physical,
        S_u_norm=float(np.max(np.abs(Q2g))),
        S_gammaG_norm=float(np.max(np.abs(gammaGg * c_scale**3))),   # rough c^3-normalization
        S_gammaG2_norm=float(np.max(np.abs(gammaG2g * c_scale**5))), # rough c^5-normalization
    )

def build_single_packet() -> tuple[np.ndarray, np.ndarray]:
    """
    Single centered packet Q(x)=1/(1+x^2), represented as theta=pi/2.
    """
    return np.array([math.pi / 2.0]), np.array([1.0])

def run_singular_controls(
    c_values: list[float],
    X0: float,
    R_cancel: int,
    nquad: int,
    ngrid: int,
) -> list[SingularRow]:
    rows = []

    th_single, w_single = build_single_packet()
    th_cancel, w_cancel = build_sine_quadrature(R_cancel)
    th_random, w_random = build_random_positive_cluster(R_cancel + 3, seed=424242)

    for c in c_values:
        rows.append(compute_singular_diagnostics(th_single, w_single, c, X0, "single", nquad, ngrid))
        rows.append(compute_singular_diagnostics(th_random, w_random, c, X0, "random_cluster", nquad, ngrid))
        rows.append(compute_singular_diagnostics(th_cancel, w_cancel, c, X0, "quadrature_cancelled", nquad, ngrid))

    return rows

# ----------------------------
# Reporting
# ----------------------------

def sci(x: float) -> str:
    return f"{x:.6e}"

def print_negative_rows(rows: list[NegativeControlRow]) -> None:
    print("\n=== Deterministic same-scale quadrature negative control ===")
    header = [
        "R", "N", "X0", "mu1_err", "killed_moment_max",
        "E_X", "S_X", "random_E_med", "ratio"
    ]
    print(",".join(header))
    for r in rows:
        print(",".join([
            str(r.R),
            str(r.N),
            f"{r.X0:.2f}",
            sci(r.mu1_error),
            sci(r.killed_moment_max),
            sci(r.E_X),
            sci(r.S_X),
            sci(r.random_E_median),
            sci(r.ratio_to_random),
        ]))

def print_singular_rows(rows: list[SingularRow]) -> None:
    print("\n=== Singular/shallow packet controls ===")
    header = [
        "label", "c", "X0", "E_u_norm", "E_u_physical",
        "gate2_norm", "gate2_physical", "S_u_norm",
        "S_gammaG_norm", "S_gammaG2_norm"
    ]
    print(",".join(header))
    for r in rows:
        print(",".join([
            r.label,
            sci(r.c),
            f"{r.X0:.2f}",
            sci(r.E_u_norm),
            sci(r.E_u_physical),
            sci(r.gate2_norm),
            sci(r.gate2_physical),
            sci(r.S_u_norm),
            sci(r.S_gammaG_norm),
            sci(r.S_gammaG2_norm),
        ]))

def write_csv(path: str, neg_rows: list[NegativeControlRow], sing_rows: list[SingularRow]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["section", "R", "N", "X0", "mu1_error", "killed_moment_max",
                         "normalized_jet_max", "E_X", "S_X", "random_E_median", "ratio_to_random"])
        for r in neg_rows:
            writer.writerow([
                "negative_control", r.R, r.N, r.X0, r.mu1_error, r.killed_moment_max,
                r.normalized_jet_max, r.E_X, r.S_X, r.random_E_median, r.ratio_to_random
            ])

        writer.writerow([])
        writer.writerow(["section", "label", "c", "X0", "E_u_norm", "E_u_physical",
                         "gate2_norm", "gate2_physical", "S_u_norm",
                         "S_gammaG_norm", "S_gammaG2_norm"])
        for r in sing_rows:
            writer.writerow([
                "singular_control", r.label, r.c, r.X0, r.E_u_norm, r.E_u_physical,
                r.gate2_norm, r.gate2_physical, r.S_u_norm,
                r.S_gammaG_norm, r.S_gammaG2_norm
            ])

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="Run a faster reduced test suite.")
    parser.add_argument("--out", type=str, default="", help="Optional CSV output path.")
    args = parser.parse_args()

    if args.fast:
        neg_cases = [(12, 0.5), (24, 0.5)]
        nquad = 128
        ngrid = 801
        n_random = 5
        singular_c_values = [1e-2, 1e-3]
    else:
        neg_cases = [
            (12, 0.25), (12, 0.5), (12, 0.75),
            (24, 0.25), (24, 0.5), (24, 0.75),
            (40, 0.25), (40, 0.5), (40, 0.75),
        ]
        nquad = 256
        ngrid = 2001
        n_random = 20
        singular_c_values = [1e-2, 1e-3, 1e-4]

    neg_rows = [
        run_negative_control_case(R, X0, nquad=nquad, ngrid=ngrid, n_random=n_random)
        for R, X0 in neg_cases
    ]

    sing_rows = run_singular_controls(
        c_values=singular_c_values,
        X0=0.5,
        R_cancel=24,
        nquad=nquad,
        ngrid=ngrid,
    )

    print_negative_rows(neg_rows)
    print_singular_rows(sing_rows)

    if args.out:
        write_csv(args.out, neg_rows, sing_rows)
        print(f"\nWrote CSV: {args.out}")

if __name__ == "__main__":
    main()
```

Run the fast check first:

```bash
python gate1_controls.py --fast --out fast_results.csv
```

Then the full run:

```bash
python gate1_controls.py --out full_results.csv
```

Send me the printed tables or the CSV contents, and I’ll interpret them.

## User (2026-04-26 15:18:12)

there are the output

## Assistant (2026-04-26 15:18:14)

I’ll read both CSVs, check whether the negative controls passed, then inspect the singular dominance/cancellation scaling. After that I’ll give the next recommended run adjustments.

_Thought for 2m 19s_

The runs look successful. Both mandatory controls passed.

Files read:

- [fast_results.csv](sandbox:/mnt/data/fast_results.csv)
- [full_results.csv](sandbox:/mnt/data/full_results.csv)

## 1. Deterministic quadrature negative control passed

The killed moments are at double-precision noise level:

\[
\max_{3\le k\le R+3}\left|\sum_j w_j\sin(k\theta_j)\right|
\sim 10^{-15}.
\]

Representative full-run results:

| \(R\) | \(X_0\) | killed moment max | \(E_X\) | random median \(E_X\) | ratio |
|---:|---:|---:|---:|---:|---:|
| 12 | 0.50 | \(4.06\times10^{-16}\) | \(9.68\times10^{-14}\) | \(7.87\times10^{-1}\) | \(1.23\times10^{-13}\) |
| 24 | 0.50 | \(1.65\times10^{-15}\) | \(2.09\times10^{-27}\) | \(1.03\) | \(2.03\times10^{-27}\) |
| 40 | 0.50 | \(2.14\times10^{-15}\) | \(9.93\times10^{-33}\) | \(8.07\times10^{-1}\) | \(1.23\times10^{-32}\) |

This is exactly what we wanted: the pipeline detects the same-scale quadrature adversary by showing massive collapse in \(E_X\), while random positive packet clusters stay \(O(1)\).

The \(X_0=0.75\) stress cases also passed:

| \(R\) | \(X_0\) | \(E_X\) | ratio |
|---:|---:|---:|---:|
| 12 | 0.75 | \(1.94\times10^{-4}\) | \(1.11\times10^{-4}\) |
| 24 | 0.75 | \(1.31\times10^{-9}\) | \(5.77\times10^{-10}\) |
| 40 | 0.75 | \(5.65\times10^{-17}\) | \(2.45\times10^{-17}\) |

So even on the wider interval, the negative control remains clearly distinguishable.

## 2. Singular controls behaved as predicted

The single-packet and random-cluster controls show huge physical source and Gate 2 mass, while the quadrature-cancelled cluster collapses normalized source energy.

### Source energy scaling

For the single packet:

\[
E_u^{\rm norm}\approx 1.9513
\]

is constant, while physical energy scales as \(c^{-6}\):

| \(c\) | \(E_u^{\rm physical}\) |
|---:|---:|
| \(10^{-2}\) | \(1.95\times10^{12}\) |
| \(10^{-3}\) | \(1.95\times10^{18}\) |
| \(10^{-4}\) | \(1.95\times10^{24}\) |

For the quadrature-cancelled singular cluster:

\[
E_u^{\rm norm}\approx 2.09\times10^{-27}.
\]

That confirms it is source-flat in normalized coordinates.

Physical source energy is:

| \(c\) | quadrature-cancelled \(E_u^{\rm physical}\) |
|---:|---:|
| \(10^{-2}\) | \(2.09\times10^{-15}\) |
| \(10^{-3}\) | \(2.09\times10^{-9}\) |
| \(10^{-4}\) | \(2.09\times10^{-3}\) |

This is the expected \(c^{-6}\) rescaling.

### Gate 2 mass

Single-packet physical Gate 2 mass scales like \(c^{-16}\):

| \(c\) | single-packet Gate 2 physical |
|---:|---:|
| \(10^{-2}\) | \(3.66\times10^{32}\) |
| \(10^{-3}\) | \(3.66\times10^{48}\) |
| \(10^{-4}\) | \(3.66\times10^{64}\) |

Random clusters are also huge.

The quadrature-cancelled cluster has tiny normalized Gate 2 mass:

\[
\text{Gate2}_{\rm norm}\approx 4.65\times10^{-25},
\]

but physical Gate 2 mass still grows as \(c^{-16}\):

| \(c\) | quadrature-cancelled Gate 2 physical |
|---:|---:|
| \(10^{-2}\) | \(4.65\times10^{7}\) |
| \(10^{-3}\) | \(4.65\times10^{23}\) |
| \(10^{-4}\) | \(4.65\times10^{39}\) |

This is useful: the singular cancellation control validates the Gate 1 source-collapse mechanism, while also showing that downstream Gate 2 quantities can remain huge depending on normalization and residual anisotropy. That supports the current branch logic: singular dominance is harmless; singular source cancellation is the thing to track for Gate 1.

## 3. Interpretation

The harness is behaving correctly:

\[
\text{random packets} \Rightarrow E_X=O(1),
\]

\[
\text{deterministic quadrature} \Rightarrow E_X\ll1,
\]

\[
\text{single singular packet} \Rightarrow E_u^{\rm physical}\sim c^{-6},\quad \text{Gate2}\sim c^{-16},
\]

\[
\text{singular quadrature cancellation} \Rightarrow E_u^{\rm norm}\ll1.
\]

So the controls are passed. This means the next step is justified: run the zero-kernel-only actual-zero pilot scan.

## 4. Next run to perform

Run the actual-zero pilot as a deliberately labeled proxy:

\[
q''_{\zero,\varepsilon}(m)
=
\sum_{\gamma\in\mathcal Z_W(m_0)}
\frac{2\varepsilon(3(m-\gamma)^2-\varepsilon^2)}
{\left((m-\gamma)^2+\varepsilon^2\right)^3}.
\]

Use:

\[
\varepsilon=\kappa/Q,
\qquad
\kappa\in\{0.25,0.5,1.0\},
\]

\[
c_I\in\{0.1,0.2,0.5,1.0\},
\]

and centers:

- zero ordinates,
- gap midpoints,
- small-gap neighborhoods,
- random centers.

The first pilot does not need \(B_2\) yet; label it **zero-kernel-only proxy**. The goal is to see whether the pipeline finds quadrature-like collapse in actual zero geometry.
## User (2026-04-26 15:34:38)

ok give me the next python script to run

## Assistant (2026-04-26 15:34:40)

Save this as `gate1_zero_pilot.py`.

It runs a **zero-kernel-only proxy** pilot. It does not claim to compute final canonical \(q''_{\can}\), because \(B_2\), completed-phase constants, and regularized tails are not included yet. It is meant to test whether actual zero geometry shows quadrature-like source flattening under the pilot kernel.

Run:

```bash
python gate1_zero_pilot.py --zeros zeros.txt --out zero_pilot_results.csv
```

Expected zero file format: one ordinate per line, e.g.

```text
14.134725141734693790
21.022039638771554993
25.010857580145688763
...
```

CSV with headers is also accepted if one column is named `gamma`, `zero`, `zeros`, `ordinate`, or `t`.

```python
#!/usr/bin/env python3
"""
Gate 1 actual-zero pilot scan, zero-kernel-only proxy.

This script tests the Gate 1 source-curvature diagnostic on actual zero ordinates
using a deliberately simplified proxy kernel:

    K(m; gamma, eps) = eps / ((m-gamma)^2 + eps^2)

    K2(m; gamma, eps) = d^2/dm^2 K
        = 2 eps (3(m-gamma)^2 - eps^2) / ((m-gamma)^2 + eps^2)^3

Proxy object:

    qpp_zero_eps(m) = sum_{gamma in cutoff window} K2(m; gamma, eps)

This is NOT the final canonical q''_can. It omits B2, completed-phase constants,
tail regularization, and quartet/completed-zero normalization. Use it as a
geometry/pipeline pilot only.

Run:
    python gate1_zero_pilot.py --zeros zeros.txt --out zero_pilot_results.csv
    python gate1_zero_pilot.py --zeros zeros.csv --fast --out zero_pilot_fast.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import os
from dataclasses import dataclass, asdict
from typing import Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss

# ----------------------------
# Input
# ----------------------------

def load_zeros(path: str) -> np.ndarray:
    """
    Load zero ordinates from:
      - plain text, one float per line
      - CSV with column gamma/zero/zeros/ordinate/t
      - CSV-like first column fallback

    Lines beginning with # are ignored.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    # Try CSV/header mode.
    with open(path, "r", newline="") as f:
        sample = f.read(4096)
        f.seek(0)

        # If header-ish, use csv.DictReader.
        first_nonempty = None
        for line in sample.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                first_nonempty = line
                break

        if first_nonempty and any(name in first_nonempty.lower().split(",") for name in ["gamma", "zero", "zeros", "ordinate", "t"]):
            reader = csv.DictReader(f)
            candidates = ["gamma", "zero", "zeros", "ordinate", "t"]
            col = None
            lower_map = {c.lower(): c for c in (reader.fieldnames or [])}
            for cand in candidates:
                if cand in lower_map:
                    col = lower_map[cand]
                    break
            if col is None:
                raise ValueError(f"Could not find zero ordinate column in {reader.fieldnames}")
            vals = []
            for row in reader:
                raw = (row.get(col) or "").strip()
                if raw:
                    vals.append(float(raw))
            arr = np.array(vals, dtype=np.float64)
            arr.sort()
            return arr

    # Plain/fallback mode.
    vals = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # accept comma-separated; take first parseable field
            parts = [p.strip() for p in line.replace("\t", ",").split(",")]
            for p in parts:
                if not p:
                    continue
                try:
                    vals.append(float(p))
                    break
                except ValueError:
                    continue

    arr = np.array(vals, dtype=np.float64)
    arr = arr[np.isfinite(arr)]
    arr.sort()
    if len(arr) == 0:
        raise ValueError("No zero ordinates loaded.")
    return arr

# ----------------------------
# Proxy kernel and derivatives
# ----------------------------

def K2_eps(m: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    """
    Return matrix K2(m_i; gamma_j, eps), shape (len(m), len(gammas)).

    K2 = 2 eps (3 x^2 - eps^2) / (x^2 + eps^2)^3
    """
    x = m[:, None] - gammas[None, :]
    den = x * x + eps * eps
    return 2.0 * eps * (3.0 * x * x - eps * eps) / (den ** 3)

def K2_deriv_at_center(gammas: np.ndarray, m0: float, eps: float, r: int) -> float:
    """
    Numerically stable-ish finite-difference-free derivatives for small r by
    polynomial recurrence would be ideal. For pilot, use complex-step-like
    polynomial fitting instead elsewhere. This placeholder is not used directly.
    """
    raise NotImplementedError

def qpp_proxy_values(ms: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    if len(gammas) == 0:
        return np.zeros_like(ms)
    return np.sum(K2_eps(ms, gammas, eps), axis=1)

# ----------------------------
# Interval computations
# ----------------------------

def Q_of_m(m0: float, mode: str = "log") -> float:
    if mode == "log":
        return max(1.0, math.log(3.0 + abs(m0)))
    raise ValueError(f"Unknown Q mode: {mode}")

def select_zeros_in_window(zeros: np.ndarray, center: float, W: float) -> np.ndarray:
    lo = np.searchsorted(zeros, center - W, side="left")
    hi = np.searchsorted(zeros, center + W, side="right")
    return zeros[lo:hi]

def compute_interval_energy(
    zeros: np.ndarray,
    m0: float,
    c_I: float,
    kappa: float,
    W_factor: float,
    Q_mode: str,
    nquad: int,
) -> tuple[float, float, float, int]:
    """
    Compute:
      Q = log-ish scale
      eps = kappa/Q
      I = [m0-c_I/Q, m0+c_I/Q]
      W = W_factor/Q
      qpp = sum_{|gamma-m0|<=W} K2
      E_I = mean |qpp|^2 over I
      S_I = max over quadrature nodes
    """
    Q = Q_of_m(m0, Q_mode)
    eps = kappa / Q
    half = c_I / Q
    W = W_factor / Q

    local_zeros = select_zeros_in_window(zeros, m0, W)

    nodes, weights = leggauss(nquad)
    ms = m0 + half * nodes
    ws = half * weights

    vals = qpp_proxy_values(ms, local_zeros, eps)
    integral = float(np.sum(ws * vals * vals))
    E_I = integral / (2.0 * half)
    S_I = float(np.max(np.abs(vals))) if len(vals) else 0.0
    return E_I, S_I, Q, len(local_zeros)

def chebyshev_jet_proxy(
    zeros: np.ndarray,
    m0: float,
    c_I: float,
    kappa: float,
    W_factor: float,
    Q_mode: str,
    R: int,
    nfit: int,
) -> tuple[float, float]:
    """
    Compute normalized finite jets J_r = Delta^r f^(r)(m0), r=0..R,
    via Chebyshev/polynomial fit over [-Delta, Delta].

    We fit f(m0 + Delta*x) as polynomial in x:
        f ~ sum a_r x^r
    Then Delta^r f^(r)(m0) = r! a_r.

    Returns:
      J_max, J_rms
    """
    Q = Q_of_m(m0, Q_mode)
    eps = kappa / Q
    Delta = c_I / Q
    W = W_factor / Q

    local_zeros = select_zeros_in_window(zeros, m0, W)

    # Chebyshev-ish nodes in x.
    j = np.arange(nfit)
    x = np.cos((2 * j + 1) * math.pi / (2 * nfit))
    ms = m0 + Delta * x
    vals = qpp_proxy_values(ms, local_zeros, eps)

    # Fit ordinary polynomial in x up to degree R.
    # Use overdetermined least squares.
    V = np.vander(x, N=R + 1, increasing=True)
    coeffs, *_ = np.linalg.lstsq(V, vals, rcond=None)

    jets = np.array([math.factorial(r) * coeffs[r] for r in range(R + 1)], dtype=np.float64)
    J_max = float(np.max(np.abs(jets)))
    J_rms = float(np.sqrt(np.sum(jets * jets)))
    return J_max, J_rms

# ----------------------------
# Center families
# ----------------------------

def gram_like_centers(zeros: np.ndarray, max_count: int) -> np.ndarray:
    """
    Placeholder 'Gram-like' centers: evenly spaced between min/max zero range.
    True Gram points require theta(t), not included in this proxy script.
    """
    if len(zeros) < 2:
        return zeros.copy()
    lo, hi = float(zeros[0]), float(zeros[-1])
    return np.linspace(lo, hi, min(max_count, max(2, len(zeros) // 2)))

def generate_centers(
    zeros: np.ndarray,
    max_per_family: int,
    seed: int,
) -> list[tuple[str, float]]:
    rng = np.random.default_rng(seed)
    centers: list[tuple[str, float]] = []

    # zero ordinates
    for g in zeros[:max_per_family]:
        centers.append(("zero", float(g)))

    # gap midpoints and small-gap neighborhoods
    gaps = np.diff(zeros)
    if len(gaps) > 0:
        idx_sorted_small = np.argsort(gaps)[:max_per_family]
        idx_sorted_large = np.argsort(gaps)[-max_per_family:]

        for i in idx_sorted_small:
            a, b = zeros[i], zeros[i + 1]
            centers.append(("small_gap_mid", float(0.5 * (a + b))))
            centers.append(("small_gap_q25", float(a + 0.25 * (b - a))))
            centers.append(("small_gap_q75", float(a + 0.75 * (b - a))))

        for i in idx_sorted_large:
            a, b = zeros[i], zeros[i + 1]
            centers.append(("large_gap_mid", float(0.5 * (a + b))))

    # gap midpoints first max_per_family
    for i in range(min(max_per_family, max(0, len(zeros) - 1))):
        centers.append(("gap_mid", float(0.5 * (zeros[i] + zeros[i + 1]))))

    # gram-like placeholder
    for g in gram_like_centers(zeros, max_per_family):
        centers.append(("gram_like_even", float(g)))

    # random centers within zero range
    if len(zeros) >= 2:
        lo, hi = float(zeros[0]), float(zeros[-1])
        for m in rng.uniform(lo, hi, size=max_per_family):
            centers.append(("random", float(m)))

    # Deduplicate approximately
    seen = set()
    deduped = []
    for typ, m in centers:
        key = (typ, round(m, 12))
        if key not in seen:
            seen.add(key)
            deduped.append((typ, m))
    return deduped

# ----------------------------
# Result row
# ----------------------------

@dataclass
class ScanRow:
    center_type: str
    m0: float
    Q: float
    c_I: float
    kappa: float
    W_factor: float
    nquad: int
    R_jet: int
    local_zero_count: int
    E_I: float
    S_I: float
    B_eff: float
    J_max: float
    J_rms: float
    tail_drift_rel: float
    quad_drift_rel: float
    status: str

def safe_B_eff(E_I: float, Q: float) -> float:
    if E_I <= 0 or Q <= 1:
        return float("nan")
    return -math.log(E_I) / math.log(Q)

def rel_diff(a: float, b: float) -> float:
    denom = max(abs(a), abs(b), 1e-300)
    return abs(a - b) / denom

def classify_row(row: ScanRow, tail_tol: float, quad_tol: float) -> str:
    if row.tail_drift_rel > tail_tol:
        return "reject_tail_unstable"
    if row.quad_drift_rel > quad_tol:
        return "reject_quad_unstable"
    # Proxy thresholds only.
    if row.B_eff > 20 and row.J_max < 1e-8:
        return "serious_proxy_warning"
    if row.B_eff > 10:
        return "candidate_proxy_flat"
    if row.B_eff > 5:
        return "watch"
    return "healthy"

def run_scan(
    zeros: np.ndarray,
    centers: list[tuple[str, float]],
    c_I_values: list[float],
    kappa_values: list[float],
    W_factor_values: list[float],
    Q_mode: str,
    nquad: int,
    R_jet: int,
    nfit: int,
    tail_tol: float,
    quad_tol: float,
) -> list[ScanRow]:
    rows: list[ScanRow] = []
    for center_type, m0 in centers:
        # Avoid centers too near boundary for large windows.
        for c_I in c_I_values:
            for kappa in kappa_values:
                for W_factor in W_factor_values:
                    # Main energy.
                    E, S, Q, count = compute_interval_energy(
                        zeros, m0, c_I, kappa, W_factor, Q_mode, nquad
                    )

                    # Quadrature drift: compare with half nquad.
                    E_half, _, _, _ = compute_interval_energy(
                        zeros, m0, c_I, kappa, W_factor, Q_mode, max(32, nquad // 2)
                    )
                    quad_drift = rel_diff(E, E_half)

                    # Tail drift: compare current W to 2W if possible.
                    E_2W, _, _, _ = compute_interval_energy(
                        zeros, m0, c_I, kappa, 2.0 * W_factor, Q_mode, nquad
                    )
                    tail_drift = rel_diff(E, E_2W)

                    try:
                        J_max, J_rms = chebyshev_jet_proxy(
                            zeros, m0, c_I, kappa, W_factor, Q_mode, R_jet, nfit
                        )
                    except Exception:
                        J_max, J_rms = float("nan"), float("nan")

                    B_eff = safe_B_eff(E, Q)

                    row = ScanRow(
                        center_type=center_type,
                        m0=m0,
                        Q=Q,
                        c_I=c_I,
                        kappa=kappa,
                        W_factor=W_factor,
                        nquad=nquad,
                        R_jet=R_jet,
                        local_zero_count=count,
                        E_I=E,
                        S_I=S,
                        B_eff=B_eff,
                        J_max=J_max,
                        J_rms=J_rms,
                        tail_drift_rel=tail_drift,
                        quad_drift_rel=quad_drift,
                        status="",
                    )
                    row.status = classify_row(row, tail_tol, quad_tol)
                    rows.append(row)
    return rows

def write_rows(path: str, rows: list[ScanRow]) -> None:
    fields = list(asdict(rows[0]).keys()) if rows else []
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))

def print_summary(rows: list[ScanRow], top_n: int) -> None:
    print("\n=== Gate 1 actual-zero pilot summary: zero-kernel-only proxy ===")
    print(f"rows: {len(rows)}")

    by_status = {}
    for r in rows:
        by_status[r.status] = by_status.get(r.status, 0) + 1
    print("status counts:")
    for k, v in sorted(by_status.items()):
        print(f"  {k}: {v}")

    rows_sorted = sorted(rows, key=lambda r: (math.nan_to_num(-r.B_eff, nan=1e999)))
    # Actually want largest B_eff.
    rows_sorted = sorted(rows, key=lambda r: (-math.nan_to_num(r.B_eff, nan=-1e999), r.tail_drift_rel, r.quad_drift_rel))

    print(f"\nTop {top_n} by B_eff:")
    header = [
        "rank", "status", "center_type", "m0", "Q", "c_I", "kappa", "W_factor",
        "count", "E_I", "S_I", "B_eff", "J_max", "tail_drift", "quad_drift"
    ]
    print(",".join(header))
    for i, r in enumerate(rows_sorted[:top_n], start=1):
        print(",".join([
            str(i),
            r.status,
            r.center_type,
            f"{r.m0:.12g}",
            f"{r.Q:.6g}",
            f"{r.c_I:.3g}",
            f"{r.kappa:.3g}",
            f"{r.W_factor:.3g}",
            str(r.local_zero_count),
            f"{r.E_I:.6e}",
            f"{r.S_I:.6e}",
            f"{r.B_eff:.6g}",
            f"{r.J_max:.6e}",
            f"{r.tail_drift_rel:.3e}",
            f"{r.quad_drift_rel:.3e}",
        ]))

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeros", required=True, help="Path to zero ordinates file.")
    parser.add_argument("--out", default="zero_pilot_results.csv", help="Output CSV path.")
    parser.add_argument("--fast", action="store_true", help="Small fast pilot.")
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument("--top", type=int, default=20)
    args = parser.parse_args()

    zeros = load_zeros(args.zeros)
    print(f"Loaded {len(zeros)} zeros: [{zeros[0]}, {zeros[-1]}]")

    if args.fast:
        max_per_family = 8
        c_I_values = [0.2, 0.5]
        kappa_values = [0.5, 1.0]
        W_factor_values = [10.0, 25.0]
        nquad = 96
        R_jet = 6
        nfit = 24
        tail_tol = 5e-2
        quad_tol = 1e-4
    else:
        max_per_family = 25
        c_I_values = [0.1, 0.2, 0.5, 1.0]
        kappa_values = [0.25, 0.5, 1.0]
        W_factor_values = [10.0, 25.0, 50.0, 100.0]
        nquad = 160
        R_jet = 8
        nfit = 36
        tail_tol = 2e-2
        quad_tol = 1e-5

    centers = generate_centers(zeros, max_per_family=max_per_family, seed=args.seed)
    print(f"Generated {len(centers)} centers.")

    rows = run_scan(
        zeros=zeros,
        centers=centers,
        c_I_values=c_I_values,
        kappa_values=kappa_values,
        W_factor_values=W_factor_values,
        Q_mode="log",
        nquad=nquad,
        R_jet=R_jet,
        nfit=nfit,
        tail_tol=tail_tol,
        quad_tol=quad_tol,
    )

    write_rows(args.out, rows)
    print_summary(rows, top_n=args.top)
    print(f"\nWrote CSV: {args.out}")
    print("\nNOTE: This is a zero-kernel-only proxy. It omits B2 and final canonical regularization.")

if __name__ == "__main__":
    main()
```

Run fast first:

```bash
python gate1_zero_pilot.py --zeros zeros.txt --fast --out zero_pilot_fast.csv
```

Then full:

```bash
python gate1_zero_pilot.py --zeros zeros.txt --out zero_pilot_full.csv
```

Send me the printed summary or the CSV outputs.

## User (2026-04-26 15:47:06)

here are the csvs

## Assistant (2026-04-26 15:55:44)

_Thought for 8m 34s_

I can see the files were uploaded, but the execution environment is currently timing out when reading them, even for simple operations like `head`, `wc`, `stat`, and CSV parsing. I should not invent the results.

Please run this local summarizer against the two CSVs and paste the output:

```python
#!/usr/bin/env python3
import csv
import math
import sys
from collections import Counter

def fnum(x):
    try:
        return float(x)
    except Exception:
        return float("nan")

def summarize(path):
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"\n=== {path} ===")
    print(f"rows: {len(rows)}")

    status = Counter(r.get("status", "") for r in rows)
    print("status counts:")
    for k, v in status.most_common():
        print(f"  {k}: {v}")

    def val(row, col):
        return fnum(row.get(col, "nan"))

    numeric_cols = [
        "E_I", "S_I", "B_eff", "J_max", "J_rms",
        "tail_drift_rel", "quad_drift_rel", "local_zero_count",
    ]

    print("\nsummary:")
    for col in numeric_cols:
        xs = [val(r, col) for r in rows]
        xs = [x for x in xs if math.isfinite(x)]
        if not xs:
            continue
        xs.sort()
        def pct(p):
            return xs[int(p * (len(xs) - 1))]
        print(
            f"  {col}: "
            f"min={xs[0]:.6e}, "
            f"p25={pct(0.25):.6e}, "
            f"median={pct(0.50):.6e}, "
            f"p75={pct(0.75):.6e}, "
            f"max={xs[-1]:.6e}"
        )

    print("\nTop 20 by B_eff:")
    top = sorted(rows, key=lambda r: val(r, "B_eff"), reverse=True)[:20]
    cols = [
        "status", "center_type", "m0", "Q", "c_I", "kappa",
        "W_factor", "local_zero_count", "E_I", "S_I", "B_eff",
        "J_max", "tail_drift_rel", "quad_drift_rel",
    ]
    print(",".join(cols))
    for r in top:
        print(",".join(str(r.get(c, "")) for c in cols))

    print("\nRows with B_eff > 5:")
    print(sum(1 for r in rows if val(r, "B_eff") > 5))

    print("Rows with B_eff > 10:")
    print(sum(1 for r in rows if val(r, "B_eff") > 10))

    print("Rows with tail_drift_rel > 0.02:")
    print(sum(1 for r in rows if val(r, "tail_drift_rel") > 0.02))

    print("Rows with quad_drift_rel > 1e-5:")
    print(sum(1 for r in rows if val(r, "quad_drift_rel") > 1e-5))

if __name__ == "__main__":
    for path in sys.argv[1:]:
        summarize(path)
```

Run:

```bash
python summarize_zero_pilot.py zero_pilot_fast.csv zero_pilot_full.csv
```

From the few lines I was able to read before the environment stalled, the early rows looked **healthy**: \(E_I\) was large, \(B_I^{\rm eff}\) was negative, and tail/quadrature drift were tiny. But I need the full summary above before giving a real verdict on whether any candidate flat intervals appeared.

_Thought for a couple of seconds_

The pilot output is healthy.

## Summary verdict

No zero-kernel-only proxy flat-interval signal appeared.

Key points from the pasted summary:

- **No rows with \(B_I^{\rm eff}>10\)** in either fast or full CSV.
- Typical intervals are strongly non-flat:
  \[
  \operatorname{median}(B_I^{\rm eff})\approx -5.74 \text{ fast},\qquad -5.26 \text{ full}.
  \]
  Negative \(B_I^{\rm eff}\) means \(E_I>1\), i.e. not source-flat.
- Elevated \(B_I^{\rm eff}>5\) rows exist, but they cluster at the **lowest-height / smallest-\(Q\)** large-gap midpoints, where the exponent is amplified because \(\log Q\) is small.
- **Quadrature drift is negligible**:
  \[
  \max D_{\rm quad}\approx 10^{-11},
  \]
  so numerical integration is not the issue.
- The main rejected cases are tail-window artifacts:
  \[
  D_{\rm tail}>0.02
  \]
  for low cutoff \(W=10/Q\), including cases where the local window catches too few or zero zeros.
- The elevated surviving “watch” rows have \(J_{\max}\sim S_I\), so they do **not** show hidden high-order flatness.

This matches the intended validation protocol: reject isolated/tail-unstable smallness, require interval and finite-jet stability, and avoid over-reading low-\(Q\) proxy artifacts. The pasted output explicitly states that the run found “no proxy flat-interval candidates” and that all elevated-\(B_{\rm eff}\) rows are explained by low \(Q\), visible non-hidden smallness, and tail-window sensitivity. 

## Interpretation

This is a good first actual-zero proxy result:

\[
\text{zero-kernel-only actual pilot} \not\approx \text{quadrature negative control}.
\]

It does **not** prove Gate 1, because the proxy omits:

\[
B_2,
\]

completed-phase constants,

regularized tails,

and the final canonical \(q''_{\can}\) normalization.

But it says the harness is behaving correctly and that the first crude actual-zero geometry scan did not immediately find the same-scale source-flattening adversary.

## Recommended next run

Run the same pilot at a higher zero range and avoid the very low-\(Q\) first zeros. Use:

- discard centers with \(Q<5\) or \(m_0<150\);
- use only \(W_{\rm factor}\in\{50,100,200\}\);
- add a stricter candidate rule:
  \[
  B_I^{\rm eff}>8,\quad D_{\rm tail}<10^{-3},\quad J_{\max}<10^{-3}S_I.
  \]
  The last condition catches genuine finite-jet flattening rather than merely small amplitude.

The next useful script change is to add `--min-m0`, `--min-Q`, and larger `W_factor` options.
## User (2026-04-26 16:01:26)

ok give me the parameters to run it with

## Assistant (2026-04-26 16:01:28)

Use these for the next proxy scan.

## Recommended next run parameters

Filter out the low-height artifacts:

```bash
--min-m0 150
--min-Q 5
```

Use more stable tail windows only:

```bash
--W-factors 50,100,200
```

Use the same interval and regularization grid, but skip the smallest unstable tail setting:

```bash
--c-I-values 0.1,0.2,0.5,1.0
--kappa-values 0.25,0.5,1.0
```

Use slightly stronger numerical settings:

```bash
--nquad 256
--R-jet 10
--nfit 48
--tail-tol 1e-3
--quad-tol 1e-7
```

Limit row count initially:

```bash
--max-per-family 50
```

## If your current script does not support those flags

Run the same script after editing these constants in `main()`:

```python
max_per_family = 50
c_I_values = [0.1, 0.2, 0.5, 1.0]
kappa_values = [0.25, 0.5, 1.0]
W_factor_values = [50.0, 100.0, 200.0]
nquad = 256
R_jet = 10
nfit = 48
tail_tol = 1e-3
quad_tol = 1e-7
```

And add a simple zero filter after loading:

```python
zeros = zeros[zeros >= 150.0]
```

For \(Q\), since the script uses \(Q=\log(3+m_0)\), this already gives \(Q>5\) for \(m_0\ge150\).

## Command if you add the flags

```bash
python gate1_zero_pilot.py \
  --zeros zeros.txt \
  --out zero_pilot_m150_stable.csv \
  --min-m0 150 \
  --min-Q 5 \
  --W-factors 50,100,200 \
  --c-I-values 0.1,0.2,0.5,1.0 \
  --kappa-values 0.25,0.5,1.0 \
  --nquad 256 \
  --R-jet 10 \
  --nfit 48 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 50
```

## What to paste back

The summary output plus the top 20 by \(B_{\rm eff}\). The key checks are:

\[
B_{\rm eff}>8,\quad D_{\rm tail}<10^{-3},\quad D_{\rm quad}<10^{-7},
\]

and whether

\[
J_{\max}\ll S_I
\]

for any high-\(B_{\rm eff}\) row.

## User (2026-04-26 17:18:56)

we've updated your scripts. please check them.:

  scripts/zeta_bridge_agent1/gate1_zero_pilot.py

  - Math Q_of_m rewritten: max(1, log(3 + |m0|)) → log(m0 / (2π)). Docstring notes caller must filter Q ≤ 1; no clamp.
  - Centers generate_centers family names changed to unified vocabulary:
    - zero → zero_ordinate
    - gap_mid → gap_midpoint
    - large_gap_mid → large_gap_midpoint
    - dropped small_gap_q25 and small_gap_q75; kept small_gap_midpoint only
    - gram_like_even → gram_placeholder (function gram_like_centers → gram_placeholder_centers)
    - added uniform family (linspace)
  - Resume --resume flipped to default-on; --no-resume opt-out added. Existing-file behavior: resume appends, --no-resume truncates.
  - Filter --min-Q default now 1.0 (was None); centers with Q ≤ 1 auto-skipped via m0 > 2π·e ≈ 17.08.
  - Logging added log(msg) helper prefixing [HH:MM:SS]; converted print() calls in main() (status loads, filters, workers, hash, output path, resume status,
  final wrote/note) to log().
  - Earlier in the session: added BLAS pinning (5 vars), ProcessPoolExecutor with _worker_init carrying zeros, --workers defaulting to cpu_count - 2,
  --progress-every heartbeat, streaming CSV write (flush per row), compute_params_hash over zeros-file SHA + every numeric param, derive_output_path inserting
  .<12-hash>.csv before extension.

  scripts/zeta_bridge_agent1/gate1_controls.py

  - Added BLAS env-var pinning (5 vars to "1") before any numpy import.
  - Added log(msg) helper.
  - No math, schema, or CLI changes (controls have their own row schemas: NegativeControlRow, SingularRow — intentionally not unified).

  scripts/zeta_bridge_agent1/summarize_zero_pilot.py

  - Added log(msg) helper for cross-script consistency.
  - No CSV-parsing changes (the script already reads agent1's column names, which are the unified spec).

## Assistant (2026-04-26 17:18:57)

I’ll review the uploaded scripts for correctness, focusing on the changed \(Q\) convention, resume/hash behavior, multiprocessing, CSV output, and the numerical formulas.

_Thought for 1m 2s_

I reviewed the two uploaded scripts statically. Overall the operational changes look good: BLAS pinning, hash-derived output paths, default resume, streaming CSV, unified family names, and the updated \(Q=\log(m_0/2\pi)\) convention are coherent. The main issue I found is one mathematical formula bug in `gate1_controls.py`. 

## Critical fix: `K_fourth` formula is wrong

Current code:

```python
numerator = 24.0 * s * (16.0 * y**4 - 12.0 * s**2 * y**2 + s**4)
return numerator / (den**5)
```

For

\[
K(x)=\frac{s}{(x-c)^2+s^2},
\]

the correct fourth derivative is:

\[
K^{(4)}(x)
=
\frac{24s\left(5y^4-10s^2y^2+s^4\right)}{(y^2+s^2)^5},
\qquad y=x-c.
\]

Patch:

```python
def K_fourth(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    Analytic fourth derivative of K_theta(x).

    Let y=x-c, a=s. For K=a/(y^2+a^2):
    K'''' = 24*a*(5*y^4 - 10*a^2*y^2 + a^4) / (y^2+a^2)^5
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y * y + s * s
    numerator = 24.0 * s * (5.0 * y**4 - 10.0 * s**2 * y**2 + s**4)
    return numerator / (den**5)
```

Why it matters: this affects the singular controls through

\[
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)}.
\]

The deterministic Gate 1 negative control using \(F=Q''\) is unaffected.

---

## Recommended cleanup: `Q_of_m`

The new convention is right:

\[
Q=\log\frac{m_0}{2\pi}.
\]

But the implementation uses `abs(m0)`. Since zero ordinates should be positive and the meaning is not symmetric under \(m_0\mapsto -m_0\), I would make invalid inputs explicit:

```python
def Q_of_m(m0: float, mode: str = "log") -> float:
    """Q = log(m0 / (2*pi)); valid for positive m0 only."""
    if mode == "log":
        if m0 <= 0:
            return float("-inf")
        return math.log(m0 / (2.0 * math.pi))
    raise ValueError(f"Unknown Q mode: {mode}")
```

This makes the `--min-Q` filtering more semantically clean. In practice your current positive-zero workflow is fine.

---

## Minor doc mismatch

In `gate1_zero_pilot.py`, `_DEFAULT_OUT_DIR` is:

```python
_DEFAULT_OUT_DIR = os.path.normpath(os.path.join(_SCRIPT_DIR, "out"))
```

but one help string says:

```text
Default lands in <script>/../out/.
```

Change that to:

```python
help="Output CSV path. Default lands in <script>/out/."
```

The behavior is fine; only the help text is stale. 

---

## Resume/hash behavior looks sound

The hash includes:

- zero file SHA-256,
- all numeric scan parameters,
- `seed`,
- `min_m0`,
- `min_Q`,
- schema version.

Then `derive_output_path()` inserts the short hash before `.csv`, so default-on resume is safe against accidental parameter mixing. Streaming CSV with flush-per-row is also the right choice for long scans. 

One small future-proofing note: increment `schema_version` if you change row columns or row-key semantics.

---

## Suggested next run after patch

After fixing `K_fourth`, rerun controls:

```bash
python scripts/zeta_bridge_agent1/gate1_controls.py --fast --out controls_fast.csv
python scripts/zeta_bridge_agent1/gate1_controls.py --out controls_full.csv
```

Then rerun the stable actual-zero pilot with the corrected script set:

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zeros.txt \
  --out zero_pilot_stable.csv \
  --min-m0 150 \
  --min-Q 5 \
  --W-factors 50,100,200 \
  --c-I-values 0.1,0.2,0.5,1.0 \
  --kappa-values 0.25,0.5,1.0 \
  --nquad 256 \
  --R-jet 10 \
  --nfit 48 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 50 \
  --progress-every 500
```

The zero-pilot math and workflow otherwise look consistent with the intended proxy scan.
## User (2026-04-26 17:23:24)

check now?

## Assistant (2026-04-26 17:23:31)

_Thought for 4s_

Checked the updated files. The previous issues are fixed.

## Confirmed fixed

In `gate1_controls(1).py`, the fourth derivative formula is now correct:

\[
K^{(4)}(x)=\frac{24s(5y^4-10s^2y^2+s^4)}{(y^2+s^2)^5}.
\]

The code now uses:

```python
numerator = 24.0 * s * (5.0 * y**4 - 10.0 * s**2 * y**2 + s**4)
```

That fixes the singular-control \(\Gamma_{G,2}\) computation. 

In `gate1_zero_pilot(1).py`, `Q_of_m` no longer uses `abs(m0)` silently for valid positive zero ordinates. It now returns \(-\infty\) for \(m_0\le0\), and otherwise computes:

\[
Q=\log(m_0/(2\pi)).
\]

That is the right behavior for filtering with `--min-Q`. The stale output help text was also corrected to `<script>/out/`. 

## No blocking issues found

The resume/hash/streaming CSV behavior still looks coherent:

- hash includes zero file SHA and numerical parameters;
- output path embeds the hash;
- resume skips completed row keys;
- `--no-resume` truncates;
- streamed CSV flushes per row;
- summary reloads all rows when resuming.

The center-family vocabulary changes are consistent with the reported plan.

## Minor optional improvement

`_ROW_KEY_FIELDS` is defined but not used. That is harmless; keep or remove later.

## Run these next

First rerun controls because the \(K^{(4)}\) fix affects singular rows:

```bash
python scripts/zeta_bridge_agent1/gate1_controls.py --fast --out controls_fast.csv
python scripts/zeta_bridge_agent1/gate1_controls.py --out controls_full.csv
```

Then rerun the stable pilot:

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zeros.txt \
  --out zero_pilot_stable.csv \
  --min-m0 150 \
  --min-Q 5 \
  --W-factors 50,100,200 \
  --c-I-values 0.1,0.2,0.5,1.0 \
  --kappa-values 0.25,0.5,1.0 \
  --nquad 256 \
  --R-jet 10 \
  --nfit 48 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 50 \
  --progress-every 500
```
## User (2026-04-26 17:40:51)

Check your latest file updates. Are all fixes now in? Everything good? anything else to fix?

====
See change notes attached.

❯ should we add tail_edge to the schema?

● Yes, recommend adding it. The reasoning:

  Information tail_edge carries that nothing else does. tail_drift_rel is computed from E_I(W) vs E_I(2W). If both windows truncate against the same zero-list
  edge, the drift can look small for the wrong reason. From the persisted columns alone, you cannot tell whether a small tail_drift_rel is genuine convergence or
   shared truncation — you'd need the original zeros file again.

  Why status alone isn't enough. If you ever want to re-grade rows with looser thresholds (e.g., relax tail_tol after the fact), status == "reject_tail_edge"
  tells you the row was tossed but doesn't survive a re-classification pass. Persisting the underlying boolean keeps post-hoc filtering self-contained.

  Cost. One bool column, ~5 bytes/row, and three small touch-ups per main script:
  1. Add tail_edge: bool = False to ScanRow (default keeps loaders backward-compatible — old CSVs without the column construct fine).
  2. Set it in the row build, drop the kwarg-only path in classify_row.
  3. Bump schema_version in compute_params_hash so new runs land at new hash slugs.

  The default-value trick avoids breaking any existing CSV that's still readable. Resume against an old CSV would just see tail_edge=False for prior rows, which
  is fine because those were already classified using their status column directly.

  Unified row schema (18 columns):
  center_type, m0, Q, c_I, kappa, W_factor, nquad, R_jet, local_zero_count,
  E_I, S_I, B_eff, J_max, J_rms, tail_drift_rel, quad_drift_rel, tail_edge, status

  Per-agent application:

  ┌────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                 Agent                  │                                                     Change                                                      │
  ├────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │                                        │ Added tail_edge: bool = False to ScanRow; classify_row now reads row.tail_edge (kwarg removed); _scan_one       │
  │ 1 (gate1_zero_pilot.py)                │ writes the boolean into the row; _load_rows_for_summary parses tail_edge from CSV with default False;           │
  │                                        │ schema_version bumped 1 → 2.                                                                                    │
  ├────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ 2                                      │ Already persists tail_edge (added previous turn); classify_row already reads row.get("tail_edge", False). No    │
  │ (gate1_actual_zero_proxy_zone_scan.py) │ further change.                                                                                                 │
  ├────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │                                        │ Added "tail_edge" to _PROXY_FIELDNAMES (between quad_drift_rel and status); _process_center writes "tail_edge": │
  │ 3 (gate1_pilot.py)                     │  tail_edge into the row dict; _load_existing_rows parses tail_edge as bool with setdefault(False) for pre-v2    │
  │                                        │ CSVs; schema_version bumped 1 → 2.                                                                              │
  └────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

  Backward compatibility: old CSVs without the column still load — agent1's loader defaults via d.get("tail_edge", "False") == "True", and agent3's loader sets
  parsed.setdefault("tail_edge", False) after the per-row parse. They'll just show tail_edge=False for prior rows, which is fine because their status was already
   finalized at write time.

  Hash impact: schema_version: 2 shifts the hash slug, so all future runs land at fresh filenames. Old CSVs at the v1 slug remain undisturbed under whatever
  filename they had.

## Assistant (2026-04-26 17:40:55)

I’ll verify the final `gate1_zero_pilot.py` against the intended `tail_edge`, schema-version, classifier, and \(Q\)-guard changes, then call out anything still inconsistent or worth tightening.

_Thought for 20s_

Yes — the intended fixes are now in, and I do not see a blocking issue in the two files you uploaded.

## Confirmed

### `gate1_controls.py`

The earlier \(K^{(4)}\) formula bug is fixed. The code now uses the correct coefficient pattern:

\[
5,\ -10,\ 1
\]

in

\[
K^{(4)}(x)=\frac{24s(5y^4-10s^2y^2+s^4)}{(y^2+s^2)^5}.
\]

That resolves the singular-control \(\Gamma_{G,2}\) issue. 

### `gate1_zero_pilot.py`

The key changes are present:

- `Q_of_m()` uses the positive-only convention:
  \[
  Q=\log(m_0/(2\pi)),
  \]
  returning `-inf` for \(m_0\le0\), so low/invalid centers are filtered cleanly. 
- `tail_edge: bool = False` is added to `ScanRow`.
- `_scan_one()` computes:
  ```python
  tail_edge = bool((m0 - W2 < zeros[0]) or (m0 + W2 > zeros[-1]))
  ```
  using \(W_2=2W_{\rm factor}/Q\).
- `classify_row()` rejects `tail_edge` first via:
  ```python
  if row.tail_edge:
      return "reject_tail_edge"
  ```
- `candidate_proxy_flat` now requires finite \(B_{\rm eff}\), finite \(J_{\max}\), \(B_{\rm eff}>10\), and \(J_{\max}<10^{-6}\).
- `serious_proxy_warning` similarly requires \(B_{\rm eff}>20\) and \(J_{\max}<10^{-8}\).
- `schema_version` is bumped to `2`, so new runs get new hash slugs.
- `_load_rows_for_summary()` reads old CSVs safely with:
  ```python
  tail_edge=(d.get("tail_edge", "False") == "True")
  ```
- Help text now says default output lands in `<script>/out/`. 

## One clarification

The pasted change note says:

> agent1's column set is unchanged (the edge state lives only in status)

That is no longer true for the uploaded `gate1_zero_pilot.py`: `tail_edge` is now part of the `ScanRow` dataclass and therefore persisted via `asdict(row)` in the CSV. That is good; it matches the earlier recommendation to persist the boolean for post-hoc filtering. The row schema is now effectively 18 columns, not 17. turn61file1

## Optional non-blocking cleanup

`_ROW_KEY_FIELDS` is still unused. Harmless.

The threshold summary still counts:

```python
("tail_drift_rel > 0.02", ...)
```

but does not separately count `tail_edge`. I would add this to `_THRESHOLD_CHECKS` for visibility:

```python
("tail_edge", lambda r: bool(r.tail_edge)),
```

Not required, but useful.

## Verdict

\[
\boxed{\text{All required fixes are in.}}
\]

The scripts are good to rerun. Use the same stable command as before; the hash will change because `schema_version=2`, and `tail_edge` rows will now be explicitly persisted and rejected.
## User (2026-04-26 17:49:30)

Edits made, please re-check holistically

## Assistant (2026-04-26 17:49:36)

_Thought for 5s_

Holistic re-check: yes, the `tail_edge` edits are now properly in `gate1_zero_pilot.py`, and I do not see any remaining blocking issue.

## Confirmed in the latest file

The script now has:

- `tail_edge: bool = False` in `ScanRow`.
- `_scan_one()` computes `tail_edge` using the doubled cutoff:
  \[
  W_2=2W_{\rm factor}/Q
  \]
  and checks whether the requested doubled window exceeds the available zero-list span.
- `classify_row()` rejects edge-truncated rows first:
  ```python
  if row.tail_edge:
      return "reject_tail_edge"
  ```
- `candidate_proxy_flat` now requires both high \(B_{\rm eff}\) and small finite-jet signal:
  ```python
  B_eff > 10 and J_max < 1e-6
  ```
- `serious_proxy_warning` similarly requires:
  ```python
  B_eff > 20 and J_max < 1e-8
  ```
- `schema_version` is now `2`, so future runs get new hash slugs.
- `_load_rows_for_summary()` is backward compatible:
  ```python
  tail_edge=(d.get("tail_edge", "False") == "True")
  ```
- `_THRESHOLD_CHECKS` now includes a `tail_edge` count.
- The top-\(B_{\rm eff}\) printed summary now includes `tail_edge`.
- `Q_of_m()` is positive-only and returns `-inf` for invalid \(m_0\le0\). 

## One small bug to fix

When creating the CSV header in `run_scan()`, the dummy `ScanRow` does **not** explicitly pass `tail_edge`. Because the dataclass default is `False`, this still works; `asdict()` will include `tail_edge`. So this is not broken.

No required patch there.

## Optional cleanup

`K2_deriv_at_center()` is still an unused placeholder that raises `NotImplementedError`. It is harmless because nothing calls it. To avoid future confusion, either delete it or change the docstring to:

```python
# Reserved for future analytic jet computation. Current pilot uses chebyshev_jet_proxy().
```

Not required.

## Verdict

\[
\boxed{\text{Everything required is now in.}}
\]

Run the stable v2 scan with:

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zeros.txt \
  --out zero_pilot_stable.csv \
  --min-m0 150 \
  --min-Q 5 \
  --W-factors 50,100,200 \
  --c-I-values 0.1,0.2,0.5,1.0 \
  --kappa-values 0.25,0.5,1.0 \
  --nquad 256 \
  --R-jet 10 \
  --nfit 48 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 50 \
  --progress-every 500
```

The new output file will get a fresh hash due to `schema_version=2`.
## User (2026-04-26 17:54:14)

Final script FYI

## Assistant (2026-04-26 17:54:21)

_Thought for 5s_

Noted. I checked the final `gate1_zero_pilot(6).py`; the cleanup is in place.

Confirmed:

- `tail_edge` is persisted as a real column in `ScanRow`.
- `classify_row()` rejects `tail_edge` before drift checks.
- `candidate_proxy_flat` and `serious_proxy_warning` now require small \(J_{\max}\), not just high \(B_{\rm eff}\).
- `schema_version` remains `2`.
- `_THRESHOLD_CHECKS` includes `tail_edge`.
- Top-\(B_{\rm eff}\) summary prints `tail_edge`.
- `K2_deriv_at_center()` now has a clearer “reserved” docstring.
- \(Q=\log(m_0/(2\pi))\) with invalid positive-only handling is intact.
- Default output path help text is correct. 

I do not see further required fixes. The script is ready for the stable v2 scan.
## User (2026-04-26 17:55:27)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 17:55:41)

_Thought for 13s_

Agent 1 / A — deep actual-zero proxy scan plan.

The control stage is done. The next Agent 1 task is to run deeper actual-zero proxy scans using the validated zero-kernel-only object

\[
q''_{\zero,\varepsilon}(m)
=
\sum_{\gamma\in\mathcal Z_W(m_0)}
\frac{2\varepsilon(3(m-\gamma)^2-\varepsilon^2)}
{\left((m-\gamma)^2+\varepsilon^2\right)^3},
\qquad
\varepsilon=\kappa/Q.
\]

The current script is suitable for this proxy-stage work and correctly labels the result as non-canonical: it omits \(B_2\), completed-phase constants, final regularization, and quartet/completed-zero normalization. 

## 1. Run design

Use three height bands, as high as the zero table permits:

\[
T\sim 10^3,\qquad 10^4,\qquad 10^5.
\]

Because `gate1_zero_pilot.py` currently supports `--min-m0` but not `--max-m0`, create band-specific zero files first.

### Helper script: `make_zero_bands.py`

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def load_zeros(path):
    vals = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.replace("\t", ",").split(",")
            for p in parts:
                try:
                    vals.append(float(p.strip()))
                    break
                except ValueError:
                    pass
    vals = sorted(v for v in vals if v > 0)
    return vals

def write_band(vals, lo, hi, out):
    band = [v for v in vals if lo <= v <= hi]
    with open(out, "w") as f:
        for v in band:
            f.write(f"{v:.15f}\n")
    print(f"{out}: {len(band)} zeros in [{lo}, {hi}]")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros", required=True)
    ap.add_argument("--out-dir", default="zero_bands")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    vals = load_zeros(args.zeros)

    bands = [
        (800, 1200, "zeros_T1e3.txt"),
        (8000, 12000, "zeros_T1e4.txt"),
        (80000, 120000, "zeros_T1e5.txt"),
    ]

    for lo, hi, name in bands:
        write_band(vals, lo, hi, os.path.join(args.out_dir, name))

if __name__ == "__main__":
    main()
```

Run:

```bash
python make_zero_bands.py --zeros zeros.txt --out-dir zero_bands
```

If the zero table does not reach \(10^5\), replace the unavailable band with the highest available band, e.g. `[30000, 50000]`.

---

## 2. Deep scan commands

Use the expanded parameter grid requested by the coordinator:

\[
c_I\in\{0.05,0.1,0.2,0.5,1.0\},
\qquad
\kappa\in\{0.125,0.25,0.5,1.0\}.
\]

Use stable tail windows:

\[
W_{\rm factor}\in\{50,100,200,500\}.
\]

Use stricter numerical settings:

\[
R_{\rm jet}=12,\qquad n_{\rm fit}=64,\qquad n_{\rm quad}=320.
\]

### \(T\sim10^3\)

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zero_bands/zeros_T1e3.txt \
  --out out/zero_proxy_T1e3.csv \
  --min-Q 5 \
  --W-factors 50,100,200,500 \
  --c-I-values 0.05,0.1,0.2,0.5,1.0 \
  --kappa-values 0.125,0.25,0.5,1.0 \
  --nquad 320 \
  --R-jet 12 \
  --nfit 64 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 75 \
  --progress-every 500
```

### \(T\sim10^4\)

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zero_bands/zeros_T1e4.txt \
  --out out/zero_proxy_T1e4.csv \
  --min-Q 5 \
  --W-factors 50,100,200,500 \
  --c-I-values 0.05,0.1,0.2,0.5,1.0 \
  --kappa-values 0.125,0.25,0.5,1.0 \
  --nquad 320 \
  --R-jet 12 \
  --nfit 64 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 75 \
  --progress-every 500
```

### \(T\sim10^5\)

```bash
python scripts/zeta_bridge_agent1/gate1_zero_pilot.py \
  --zeros zero_bands/zeros_T1e5.txt \
  --out out/zero_proxy_T1e5.csv \
  --min-Q 5 \
  --W-factors 50,100,200,500 \
  --c-I-values 0.05,0.1,0.2,0.5,1.0 \
  --kappa-values 0.125,0.25,0.5,1.0 \
  --nquad 320 \
  --R-jet 12 \
  --nfit 64 \
  --tail-tol 1e-3 \
  --quad-tol 1e-7 \
  --max-per-family 75 \
  --progress-every 500
```

For very large files, set `--workers` explicitly to avoid machine saturation:

```bash
--workers 8
```

---

## 3. Candidate criteria

Treat a row as merely “watch” unless all four hold:

\[
B_I^{\rm eff}>5,
\]

\[
J_{\max}\le Q^{-5},
\]

\[
D_{\tail}\le10^{-3},
\qquad
D_{\quad}\le10^{-7},
\]

and the row is not `reject_tail_edge`.

Because this is still \(\varepsilon\)-regularized proxy data, also require regularization stability across \(\kappa\):

\[
\kappa=0.125,\ 0.25,\ 0.5,\ 1.0
\]

should produce the same center-family / interval-width cluster. If high \(B_{\rm eff}\) appears only for one \(\kappa\), classify as `proxy_artifact_risk`.

---

## 4. Band-level report schema

For each height band, report the top rows by \(B_{\rm eff}\), but only after filtering out:

```text
status in {reject_tail_edge, reject_tail_unstable, reject_quad_unstable}
```

Report:

| band | center_type | \(m_0\) | \(Q\) | \(c_I\) | \(\kappa\) | \(W\) | count | \(E_I\) | \(B_{\rm eff}\) | \(S_I\) | \(J_{\max}\) | \(Q^{-5}\) | tail | quad | status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|

Add a derived column:

\[
\texttt{jet\_ratio}=J_{\max}/Q^{-5}.
\]

A serious candidate needs:

\[
\texttt{jet\_ratio}\le1.
\]

---

## 5. Post-run summarizer

Run this after the three scans.

```python
#!/usr/bin/env python3
import argparse
import csv
import math
from collections import defaultdict

BAD = {"reject_tail_edge", "reject_tail_unstable", "reject_quad_unstable"}

def f(x):
    try:
        return float(x)
    except Exception:
        return float("nan")

def read_rows(path, band):
    rows = []
    with open(path, newline="") as fp:
        for r in csv.DictReader(fp):
            r["band"] = band
            rows.append(r)
    return rows

def summarize(paths):
    all_rows = []
    for band, path in paths:
        all_rows.extend(read_rows(path, band))

    print(f"total rows: {len(all_rows)}")
    by_band = defaultdict(list)
    for r in all_rows:
        by_band[r["band"]].append(r)

    for band, rows in by_band.items():
        print(f"\n=== {band} ===")
        print(f"rows: {len(rows)}")
        valid = [r for r in rows if r.get("status") not in BAD]
        print(f"valid rows: {len(valid)}")

        strong = []
        for r in valid:
            Q = f(r["Q"])
            J = f(r["J_max"])
            B = f(r["B_eff"])
            tail = f(r["tail_drift_rel"])
            quad = f(r["quad_drift_rel"])
            qminus5 = Q ** -5 if Q > 0 else float("nan")
            if B > 5 and J <= qminus5 and tail <= 1e-3 and quad <= 1e-7:
                strong.append(r)

        print(f"strict candidates: {len(strong)}")

        top = sorted(valid, key=lambda r: f(r["B_eff"]), reverse=True)[:20]
        print("top valid rows:")
        print("band,status,center_type,m0,Q,c_I,kappa,W_factor,count,E_I,B_eff,S_I,J_max,Q^-5,jet_ratio,tail,quad")
        for r in top:
            Q = f(r["Q"])
            J = f(r["J_max"])
            qminus5 = Q ** -5 if Q > 0 else float("nan")
            ratio = J / qminus5 if qminus5 and math.isfinite(qminus5) else float("nan")
            print(",".join([
                band,
                r.get("status", ""),
                r.get("center_type", ""),
                r.get("m0", ""),
                r.get("Q", ""),
                r.get("c_I", ""),
                r.get("kappa", ""),
                r.get("W_factor", ""),
                r.get("local_zero_count", ""),
                r.get("E_I", ""),
                r.get("B_eff", ""),
                r.get("S_I", ""),
                r.get("J_max", ""),
                f"{qminus5:.6e}",
                f"{ratio:.6e}",
                r.get("tail_drift_rel", ""),
                r.get("quad_drift_rel", ""),
            ]))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("items", nargs="+", help="Pairs: BAND=path.csv")
    args = ap.parse_args()

    pairs = []
    for item in args.items:
        band, path = item.split("=", 1)
        pairs.append((band, path))
    summarize(pairs)
```

Run:

```bash
python summarize_deep_zero_proxy.py \
  T1e3=out/zero_proxy_T1e3.<hash>.csv \
  T1e4=out/zero_proxy_T1e4.<hash>.csv \
  T1e5=out/zero_proxy_T1e5.<hash>.csv
```

---

## 6. Verdict rules

### Healthy

No strict candidates in any band, median \(B_{\rm eff}<0\), and top valid rows have

\[
J_{\max}\gg Q^{-5}.
\]

### Watch

A few valid rows satisfy

\[
B_{\rm eff}>5
\]

but fail the jet condition or appear only in one \(\kappa\)-slice.

### Candidate

A stable center cluster satisfies:

\[
B_{\rm eff}>5,\quad J_{\max}\le Q^{-5},
\]

for multiple \(c_I\), multiple \(W\), and at least two \(\kappa\) values.

### Serious warning

Candidate behavior appears in at least two height bands and survives stricter rerun with:

\[
R_{\rm jet}=16,\qquad n_{\rm fit}=96,\qquad n_{\rm quad}=512.
\]

---

## 7. Expected current outcome

Based on the prior low-height proxy runs, the expected result is:

\[
\text{healthy or watch, not candidate.}
\]

The main thing to check is whether top \(B_{\rm eff}\) rows at higher height still have large \(J_{\max}\), which would mean “small amplitude / gap effect,” not finite-jet source flattening.
## User (2026-04-26 19:04:50)

  ┌──────┬──────────────────┬───────┬───────┬───────┬───────────┬──────────────┬──────────────┬───────────────┐
  │ Band │      Range       │ Zeros │ Rows  │ Valid │ max B_eff │ median B_eff │ Strict cand. │ Top jet_ratio │
  ├──────┼──────────────────┼───────┼───────┼───────┼───────────┼──────────────┼──────────────┼───────────────┤
  │ T1e3 │ [550, 1450]      │   721 │ 16400 │ 13902 │      2.50 │        -4.74 │            0 │          ~497 │
  ├──────┼──────────────────┼───────┼───────┼───────┼───────────┼──────────────┼──────────────┼───────────────┤
  │ T1e4 │ [7750, 12250]    │  5274 │ 42000 │ 32317 │      1.60 │        -5.02 │            0 │        ~4 034 │
  ├──────┼──────────────────┼───────┼───────┼───────┼───────────┼──────────────┼──────────────┼───────────────┤
  │ T1e5 │ [94750, 105250]† │ 16166 │ 42000 │ 32500 │      0.90 │        -5.42 │            0 │       ~30 100 │
  └──────┴──────────────────┴───────┴───────┴───────┴───────────┴──────────────┴──────────────┴───────────────┘

  †T1e5 was narrowed from the spec'd [80000,120000] to [95000,105000] so zero-gen finished in ~38 min instead of ~2 h; t~10^5 height is still tested.

  Cross-band verdict: HEALTHY. All three bands max B_eff well below the watch threshold of 5. Median B_eff increasingly negative with height. Top rows in every
  band are large_gap_midpoint with J_max >> Q^-5 (jet_ratio grows ~10× per decade), confirming the Section 7 expectation: top B_eff is gap effect, not finite-jet
   source flattening. No strict candidates, no candidate clusters — no need to escalate to a stricter R_jet=16, nfit=96, nquad=512 rerun.

  Artifacts committed and pushed at c43a54d:
  - scripts/zeta_bridge_agent1/make_zero_bands.py
  - scripts/zeta_bridge_agent1/summarize_deep_zero_proxy.py
  - scripts/zeta_bridge_agent1/out/zero_bands/zeros_T1e{3,4,5}.txt
  - scripts/zeta_bridge_agent1/out/zero_proxy_T1e{3,4,5}.<hash>.csv

## Assistant (2026-04-26 19:05:01)

_Thought for 9s_

This is a clean **healthy** result for Agent 1/A’s deep proxy scan.

## Verdict

\[
\boxed{\text{HEALTHY: no Gate 1 proxy warning across }T\sim10^3,10^4,10^5.}
\]

The key facts are:

| Band | max \(B_{\rm eff}\) | median \(B_{\rm eff}\) | strict candidates | interpretation |
|---|---:|---:|---:|---|
| \(T\sim10^3\) | 2.50 | -4.74 | 0 | healthy |
| \(T\sim10^4\) | 1.60 | -5.02 | 0 | healthy |
| \(T\sim10^5\) | 0.90 | -5.42 | 0 | healthy |

This is exactly the favorable pattern: the maximum \(B_{\rm eff}\) decreases with height, the median becomes more negative, and no row passes the strict joint condition

\[
B_{\rm eff}>5,\qquad J_{\max}\le Q^{-5}.
\]

The three zero-band files also look computationally credible: the \(T\sim10^3\) band has 721 zeros in \([550,1450]\), the \(T\sim10^4\) band has 5,274 zeros in \([7750,12250]\), and the \(T\sim10^5\) band has 16,166 zeros in \([94750,105250]\).   

## Interpretation

The current proxy scan is not seeing the quadrature adversary in actual zero geometry.

The top rows remain large-gap midpoint effects, not finite-jet flattening:

\[
J_{\max}\gg Q^{-5}.
\]

In fact, the top jet ratio grows by about an order of magnitude per height decade:

\[
\sim 497,\quad \sim 4034,\quad \sim 30100.
\]

That is the opposite of a source-flat finite-jet pattern. It says the best-looking low-energy proxy rows are still visibly non-flat at the jet level.

## What this proves and does not prove

This supports Gate 1 at the **proxy geometry** level:

\[
q''_{\zero,\varepsilon}
\]

did not show stable quadrature-like collapse.

It still does not prove canonical Gate 1, because this scan omits:

\[
B_2,
\]

canonical critical-line treatment,

completed-phase constants,

and a final regularized tail.

But as an execution result, it is useful and favorable.

## Recommended next fork

Agent 1/A’s current deep proxy work is basically complete unless you want broader sampling. I would now pivot Agent 1 to either:

1. **rerun only after Agent 2 canonicalizes \(B_2\) / critical-line treatment**, or  
2. **add a small random-height stress scan** across scattered bands, not just \(10^3,10^4,10^5\), to check for accidental band selection.

The main next bottleneck is now Agent 2’s canonicalization upgrade.
## User (2026-04-26 19:26:07)

Please note Agent 2's canonicalization of B2

## Assistant (2026-04-26 19:26:19)

_Thought for 10s_

Noted. Agent 2’s \(B_2\) canonicalization is now settled.

## Accepted \(B_2\) formula

Use

\[
\boxed{
B_2(t)=\theta'''(t)
=
-\frac18\Re\psi^{(2)}\!\left(\frac14+\frac{it}{2}\right).
}
\]

Reference implementation:

```python
import mpmath as mp

def B2_exact(t, dps=50):
    mp.mp.dps = dps
    z = mp.mpf("0.25") + 0.5j * mp.mpf(t)
    return float(-mp.re(mp.polygamma(2, z)) / 8.0)
```

For scan work, the approved fast default should be the 3-term expansion for \(t\ge50\):

\[
\boxed{
B_2(t)\approx
-\frac1{2t^2}
-\frac1{8t^4}
-\frac7{64t^6}.
}
\]

```python
def B2_fast_3term(t, dps=50):
    if t >= 50:
        t2 = t * t
        return -1/(2*t2) - 1/(8*t2*t2) - 7/(64*t2*t2*t2)
    return B2_exact(t, dps=dps)
```

The validation table shows the 3-term approximation is already extremely accurate at the relevant watch points, with relative error dropping from about \(10^{-7}\) at \(m_0\approx27.7\) to \(10^{-11}\) by \(m_0\approx200\). 

## Implementation policy

Going forward:

\[
q''_{\can}(m)\approx B_2(m)+\sum_\rho^{\rm reg}K_2(m;\rho)
\]

should include \(B_2\) by default in all zero-side scans.

Keep `--no-include-B2` only as a diagnostic switch to measure `B2_drift_rel`.

Rows using `B2_only` must be excluded from Gate 1 candidate statuses. Gate 1 is about the full object, not the background alone. 

## Remaining canonical blockers

\(B_2\) is no longer blocking Agent 1/3/4/5 numerical work.

Remaining zero-side fidelity blockers are:

\[
\text{critical-line zero treatment / }\eta\text{-regularization},
\]

and

\[
\text{regularized tail completion}.
\]

So the next Agent 1 scan can safely add \(B_2\) as the first canonicalization upgrade, while still labeling the run as not fully canonical until the critical-line and tail treatments are finalized.
## User (2026-04-26 19:26:56)

Do the next prompt in the attached message as per your agent number.

## Assistant (2026-04-26 19:27:10)

_Thought for 11s_

Agent 1 / A — pivot accepted. Broad proxy scanning should stop unless a new candidate appears.

The Agent 1 task is now: **package canonical cross-check targets**, not run more \(\eta\)-regularized proxy scans. The attached coordinator note says the proxy-script branch has completed its useful job, with no proxy source-flat candidates across the deep scans and a clean 5k broad scan result: 46,408 rows, no watch rows, no candidates, max \(B_{\rm eff}=0.87\). 

## Deliverable

Prepare the **top 50 highest-\(B_{\rm eff}\)** rows from the 5k broad scan as a compact target list for:

- Agent 2’s canonical zero-side upgrade,
- Agent 4’s AFE-side cross-check.

Each target row should preserve:

\[
m_0,\ Q,\ c_I,\ \kappa,\ W,\ E_I,\ B_{\rm eff},\ S_I,\ J_{\max},
\]

plus:

\[
\text{center type},\quad D_{\tail},\quad D_{\quad},\quad \texttt{tail\_edge},\quad \texttt{status}.
\]

Also add derived fields:

\[
Q^{-5},\qquad \texttt{jet\_ratio}=J_{\max}/Q^{-5}.
\]

Since the broad scan already found no serious rows, this target list is **not a candidate list**. It is a ranked “hardest proxy rows” list for canonical/AFE verification.

---

## Extraction script

Save as:

```bash
scripts/zeta_bridge_agent1/extract_canonical_targets.py
```

```python
#!/usr/bin/env python3
"""
Extract top proxy rows for canonical zero-side and AFE cross-checks.

Input:
    gate1_zero_pilot.py CSV from the 5k broad scan.

Output:
    Compact top-N target CSV sorted by B_eff descending after excluding rejected rows.

Usage:
    python extract_canonical_targets.py \
      --input out/zero_proxy_5k.<hash>.csv \
      --out out/canonical_targets_top50.csv \
      --top 50
"""

from __future__ import annotations

import argparse
import csv
import math

REJECT_STATUSES = {
    "reject_tail_edge",
    "reject_tail_unstable",
    "reject_quad_unstable",
}

KEEP_COLUMNS = [
    "rank",
    "target_id",
    "status",
    "center_type",
    "m0",
    "Q",
    "c_I",
    "kappa",
    "W_factor",
    "local_zero_count",
    "E_I",
    "S_I",
    "B_eff",
    "J_max",
    "J_rms",
    "Q_minus_5",
    "jet_ratio",
    "tail_drift_rel",
    "quad_drift_rel",
    "tail_edge",
]

def f(x, default=float("nan")):
    try:
        return float(x)
    except Exception:
        return default

def q_minus_5(Q: float) -> float:
    if not math.isfinite(Q) or Q <= 0:
        return float("nan")
    return Q ** -5

def load_rows(path: str) -> list[dict]:
    with open(path, newline="") as fp:
        return list(csv.DictReader(fp))

def valid_for_target_pack(row: dict) -> bool:
    status = row.get("status", "")
    if status in REJECT_STATUSES:
        return False
    if str(row.get("tail_edge", "")).lower() in {"true", "1"}:
        return False

    B = f(row.get("B_eff"))
    Q = f(row.get("Q"))
    E = f(row.get("E_I"))
    J = f(row.get("J_max"))
    tail = f(row.get("tail_drift_rel"))
    quad = f(row.get("quad_drift_rel"))

    return all(math.isfinite(x) for x in [B, Q, E, J, tail, quad])

def decorate(row: dict, rank: int) -> dict:
    Q = f(row.get("Q"))
    J = f(row.get("J_max"))
    qm5 = q_minus_5(Q)
    jet_ratio = J / qm5 if math.isfinite(qm5) and qm5 != 0 else float("nan")

    target_id = f"T{rank:03d}_{row.get('center_type','unknown')}_{f(row.get('m0')):.6f}"

    out = {
        "rank": rank,
        "target_id": target_id,
        "status": row.get("status", ""),
        "center_type": row.get("center_type", ""),
        "m0": row.get("m0", ""),
        "Q": row.get("Q", ""),
        "c_I": row.get("c_I", ""),
        "kappa": row.get("kappa", ""),
        "W_factor": row.get("W_factor", ""),
        "local_zero_count": row.get("local_zero_count", ""),
        "E_I": row.get("E_I", ""),
        "S_I": row.get("S_I", ""),
        "B_eff": row.get("B_eff", ""),
        "J_max": row.get("J_max", ""),
        "J_rms": row.get("J_rms", ""),
        "Q_minus_5": f"{qm5:.12e}" if math.isfinite(qm5) else "",
        "jet_ratio": f"{jet_ratio:.12e}" if math.isfinite(jet_ratio) else "",
        "tail_drift_rel": row.get("tail_drift_rel", ""),
        "quad_drift_rel": row.get("quad_drift_rel", ""),
        "tail_edge": row.get("tail_edge", "False"),
    }
    return out

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=50)
    args = ap.parse_args()

    rows = load_rows(args.input)
    valid = [r for r in rows if valid_for_target_pack(r)]
    valid_sorted = sorted(valid, key=lambda r: f(r.get("B_eff")), reverse=True)
    top = valid_sorted[: args.top]

    decorated = [decorate(r, i + 1) for i, r in enumerate(top)]

    with open(args.out, "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=KEEP_COLUMNS)
        writer.writeheader()
        writer.writerows(decorated)

    print(f"input rows: {len(rows)}")
    print(f"valid rows: {len(valid)}")
    print(f"wrote top {len(decorated)} targets to {args.out}")

    if decorated:
        print("\nTop 10:")
        print(",".join(KEEP_COLUMNS))
        for row in decorated[:10]:
            print(",".join(str(row.get(c, "")) for c in KEEP_COLUMNS))

if __name__ == "__main__":
    main()
```

---

## Run command

```bash
python scripts/zeta_bridge_agent1/extract_canonical_targets.py \
  --input scripts/zeta_bridge_agent1/out/zero_proxy_5k.<hash>.csv \
  --out scripts/zeta_bridge_agent1/out/canonical_targets_top50.csv \
  --top 50
```

Replace `<hash>` with the actual 5k broad-scan hash.

---

## Target-list interpretation

The extracted rows should be treated as:

\[
\boxed{\text{canonical cross-check targets, not Gate 1 candidates.}}
\]

Classification for the target set:

- **healthy target**: \(B_{\rm eff}<5\), \(J_{\max}\gg Q^{-5}\).
- **watch target**: \(B_{\rm eff}>5\) but \(J_{\max}>Q^{-5}\).
- **candidate target**: \(B_{\rm eff}>5\), \(J_{\max}\le Q^{-5}\), stable drift.
- **serious target**: candidate survives canonical zero-side and AFE cross-checks.

Based on the coordinator’s note, the 5k broad scan should produce no watch/candidate rows, since it had max \(B_{\rm eff}=0.87\). 

---

## Hand-off package for Agents 2 and 4

Give Agent 2 the CSV plus this instruction:

> Rerun these top 50 proxy targets under \(+B_2\), canonical critical-line treatment, and regularized tail completion. Report whether ranked rows persist, disappear, or reorder.

Give Agent 4 the same CSV plus:

> Evaluate AFE/fixed-prime surrogate source jets and interval energies at these \(m_0,c_I\) targets. Check whether any target shows simultaneous low interval energy and finite-jet flatness after exact \(\chi\)-derivative and \(B_2\) inclusion.

## Agent 1 verdict

\[
\boxed{
\text{Agent 1 broad proxy search is closed.}
}
\]

Next Agent 1 action is only packaging and forwarding the top target rows. Further proxy scans are unnecessary unless canonicalization creates a new stable candidate.
## User (2026-04-26 19:31:51)

  Deliverable: scripts/zeta_bridge_agent1/out/canonical_targets_top50.csv — top 50 healthy proxy rows from agent3's 5k broad scan
  (actual_zero_proxy_small.bdcb358d6dcb.csv, 46408 input → 46396 valid → top 50 by B_eff).

  Range: B_eff ∈ [~0.83, ~0.87], all healthy, all tail_edge=False. J_max ~10³·Q⁻⁵ for the top rows (jet_ratio ≈ 1500 for #1 → ~5000 by #50) — confirms "hardest
  proxy rows," not Gate 1 candidates.

  One observation worth flagging in the hand-off: ranks come in pairs because gap_midpoint and large_gap_midpoint are dual family labels assigned to the same
  physical center when that gap is among the largest-N. So 50 rows cover ~25 unique (m₀, c_I, κ, W_factor) tuples. If Agents 2/4 want 50 distinct physical
  centers, dedupe on (m₀, c_I, κ, W_factor) before running canonical/AFE work, or rerun the extractor with --top 100 and dedupe.

## Assistant (2026-04-26 19:31:52)

Received. Agent 1/A packaging is complete.

Key handoff points:

- File: `scripts/zeta_bridge_agent1/out/canonical_targets_top50.csv`
- Source scan: `actual_zero_proxy_small.bdcb358d6dcb.csv`
- Input rows: 46,408
- Valid rows: 46,396
- Extracted: top 50 by \(B_{\rm eff}\)
- Range:
  \[
  B_{\rm eff}\approx 0.83\text{–}0.87
  \]
- All rows: `healthy`
- All rows: `tail_edge=False`
- Top rows have:
  \[
  J_{\max}\sim 10^3 Q^{-5}
  \]
  with `jet_ratio` roughly \(1500\to5000\), so these are **hardest healthy proxy rows**, not Gate 1 candidates.

Important handoff caveat: the top 50 contain paired duplicates because `gap_midpoint` and `large_gap_midpoint` can label the same physical center. So the 50 rows cover about 25 unique physical tuples:

\[
(m_0,\ c_I,\ \kappa,\ W_{\rm factor}).
\]

For Agent 2/4 canonical and AFE reruns, I recommend deduping by that tuple unless they explicitly want family-label duplication as a check.

## Next action for Agent 2/4

Use `canonical_targets_top50.csv` as the target set for:

\[
\text{proxy}
\to
+B_2
\to
+\text{canonical critical-line treatment}
\to
+\text{regularized tail}
\]

and for AFE-side cross-check with exact \(\chi\)-derivatives / \(B_2\).

Agent 1/A status:

\[
\boxed{\text{closed for broad proxy search; targets packaged for canonical cross-check.}}
\]
