# RH Proof Collaboration

- Source: https://chatgpt.com/c/69ee055c-dccc-83e8-b7f5-f4d3a457d0b9
- Created: 2026-04-26 12:31:31 UTC
- Default model: gpt-5-5-thinking

---

## User (2026-04-26 12:31:29)

We are trying to prove RH. See paper draft attached. You will get instructions from a coordinator throughout this chat, and you will be "Agent 3" (or Agent C if letters are used.) The instructions will typically contain instructions for all agents, but you should do the specific instruction for "Agent 3". Please first read the paper draft, then await your next instruction.

## Assistant (2026-04-26 12:31:31)

I’ll read the draft as a working paper rather than only scan headings, then I’ll keep my response minimal and wait for the coordinator’s Agent 3 instruction.

_Thought for 1m 0s_

Read the attached draft.

I’ll operate as **Agent 3 / Agent C** for this chat. My working understanding is:

- The draft is now a **local obstruction / diagnostic architecture**, not a closed RH proof.
- The scalar Bottleneck-C route is blocked by the \(S\)-visible \(\eta\eta\) row.
- The viable local language is the **rank-two fixed-sector bundle** with order-seven/order-nine visibility.
- The main unresolved gate is now **actual-zeta source-curvature observability**, especially lower bounds of the form  
  \[
  \int_{I_\rho}|q''(m)|^2\,dm \ge Q^{-B}|I_\rho|
  \]
  or a source-robust invariant not divisible by \(H=yq''\).
- Order-11/local anisotropy work appears diagnostic unless it breaks the \(H\)-divisibility/source-collapse wall.

Ready for the coordinator’s Agent 3 instruction.

I’ll take the Agent 3 lane: zero-side quadrature obstruction. I’ll focus on whether actual zeta zeros can realize the same-scale positive packet flattening model, not on prime/AFE observability or order-11 algebra.

I found the operative handoff: Agent 3’s target is specifically the same-scale packet adversary, with the required deliverable either an exclusion theorem or a statement that zero-side constraints alone are insufficient.

_Thought for 2m 32s_

## Agent 3 / C — Zero-side quadrature obstruction

### Verdict

I do **not** see a credible zero-side-only exclusion theorem from the currently available constraints. The same-scale positive packet quadrature adversary survives zero counting, quartet symmetry, simplicity, spacing heuristics, and known zero-density input. The correct deliverable is therefore a **precise insufficiency statement**, plus a candidate theorem spelling out the extra actual-zeta anti-quadrature input that would be needed. This matches the coordinator’s Agent 3 assignment: test whether actual zeta zeros can realize or approximate the source-flattening quadrature, and either exclude it or state why zero-side constraints are insufficient. 

---

# 1. Formalizing the quadrature adversary

Use local coordinate

\[
u=t-m,
\]

and model one same-scale off-line packet by parameters

\[
x=d\cos\theta,\qquad c=d\sin\theta,\qquad 0<\theta<\pi,
\]

where \(x\) is the ordinate displacement from \(m\), \(c\) is the off-critical depth, and

\[
x^2+c^2=d^2
\]

is the same-scale constraint.

Up to harmless global normalization constants, the positive packet profile is the Poisson/Cauchy kernel

\[
K_{\theta,d}(u)
=
\frac{d\sin\theta}{(u-d\cos\theta)^2+d^2\sin^2\theta}.
\]

For \(|u|<d\),

\[
K_{\theta,d}(u)
=
-\Im \frac{1}{de^{i\theta}-u}
=
\sum_{r\ge0}d^{-r-1}\sin((r+1)\theta)u^r.
\]

The continuous positive same-scale distribution

\[
d\mu(\theta)=\frac{2}{\pi}\sin\theta\,d\theta
\]

satisfies

\[
\int_0^\pi K_{\theta,d}(u)\,d\mu(\theta)
=
\frac1d,
\qquad |u|<d.
\]

Indeed,

\[
\frac{2}{\pi}\int_0^\pi
\sin\theta\sin((r+1)\theta)\,d\theta
=
\begin{cases}
1,&r=0,\\
0,&r\ge1.
\end{cases}
\]

Therefore the continuous packet distribution has

\[
q_\mu(0)>0,
\qquad
q_\mu^{(r)}(0)=0\quad(r\ge1).
\]

In particular,

\[
q_\mu''(0)=q_\mu^{(4)}(0)=\cdots=0,
\]

while the source mass \(q_0=q_\mu(0)\) remains positive.

For the paper’s first anisotropy functional,

\[
\Gamma_G=q''-6q_0+2q_0^3.
\]

If \(q''=0\) and \(q_0=2\), then

\[
\Gamma_G=-12+16=4.
\]

So the model gives exactly the dangerous Regime B pattern:

\[
q''=0,
\qquad
H=yq''=0,
\qquad
\Gamma_G\asymp1.
\]

This is source collapse with anisotropy live.

---

# 2. Finite quadrature: how many packets are needed?

For a finite packet collection

\[
\mathcal Q=\{(\theta_j,w_j)\}_{j=1}^N,
\qquad w_j>0,
\]

define

\[
q_{\mathcal Q}(u)=\sum_{j=1}^N w_jK_{\theta_j,d}(u).
\]

Then

\[
q_{\mathcal Q}^{(r)}(0)
=
r!\,d^{-r-1}
\sum_{j=1}^N w_j\sin((r+1)\theta_j).
\]

To flatten source curvature through order \(2M\), it is enough to impose

\[
\sum_{j=1}^N w_j\sin((2k+1)\theta_j)=0,
\qquad 1\le k\le M,
\]

while keeping

\[
\sum_{j=1}^N w_j\sin\theta_j>0.
\]

By Tchakaloff/Carathéodory-type positive quadrature, the continuous measure above can be replaced by a positive finite quadrature using at most

\[
N\le M+1
\]

weighted nodes for the \(M+1\)-dimensional moment system

\[
\sin\theta,\ \sin3\theta,\ \ldots,\ \sin(2M+1)\theta.
\]

If one insists on centered symmetry under \(x\mapsto -x\), symmetrize the nodes by replacing each \(\theta_j\) with the pair

\[
\theta_j,\quad \pi-\theta_j.
\]

This gives at most

\[
2(M+1)
\]

same-scale local packets and automatically kills odd \(u\)-derivatives.

Thus the packet count required for flattening is only

\[
O(M).
\]

If the desired source-flatness on \(I_\rho\) requires

\[
M\asymp \log Q
\]

or even

\[
M\asymp \frac{\log Q}{\log\log Q},
\]

the required packet count is still very small relative to the weakest known local zero-counting upper bounds.

---

# 3. Spacing and off-critical depth of the quadrature packets

A standard positive quadrature can be chosen with nodes in \((0,\pi)\). For Gauss/Jacobi-type nodes, the angular spacing is typically

\[
\Delta\theta\asymp M^{-1}
\]

in the bulk, with endpoint distance roughly

\[
\theta_{\min}\asymp M^{-2}.
\]

Therefore

\[
x_j=d\cos\theta_j,
\qquad
c_j=d\sin\theta_j.
\]

The smallest off-critical depth may be as small as

\[
c_{\min}\asymp dM^{-2}.
\]

If

\[
d\asymp Q^{-1},
\qquad
M=O(\log Q),
\]

then

\[
c_{\min}\asymp \frac{1}{Q(\log Q)^2}.
\]

This is still a legitimate off-critical depth and is far too close to the critical line for standard zero-density estimates to rule out locally.

The closest vertical spacing near the endpoints is also of order

\[
\Delta x_{\min}\asymp \frac{d}{M^2}.
\]

With \(d\asymp Q^{-1}\) and \(M=O(\log Q)\),

\[
\Delta x_{\min}\asymp \frac{1}{Q(\log Q)^2}.
\]

There is no unconditional lower spacing theorem for zeta zeros that excludes such clustering, even with simple zeros.

---

# 4. Testing candidate blockers

## 4.1 Zero counting in \(T\pm Q^{-1}\)

If \(Q\sim \log T\), the expected number of zeros in an interval of length \(Q^{-1}\) is \(O(1)\). However, the usable unconditional local bound has an error term of size roughly \(O(\log T)=O(Q)\), not \(O(1)\). Thus zero counting does **not** exclude a cluster of

\[
O(\log Q)
\]

or even substantially more zeros inside a \(Q^{-1}\)-scale interval.

Conclusion: **zero counting does not rule out the finite quadrature adversary** unless one adds a much sharper microscopic local zero-counting theorem.

## 4.2 Off-critical zero-density estimates

Zero-density estimates control aggregate counts of zeros with

\[
\Re\rho\ge \frac12+\eta
\]

over long height ranges. They do not prohibit a special microscopic cluster near one height, and they weaken badly as

\[
\eta\to0.
\]

The quadrature adversary may place packets at depths as small as

\[
c_j\asymp \frac{1}{Q(\log Q)^2}
\]

or smaller, exactly where ordinary density estimates are least useful.

Conclusion: **zero-density estimates do not block the model**.

## 4.3 Functional-equation and conjugation quartet constraints

The construction is compatible with quartet symmetry. Each local off-line packet can be closed under

\[
\rho\mapsto 1-\rho,
\qquad
\rho\mapsto \bar\rho.
\]

The functional-equation mirror pair is precisely what makes the local packet contribution positive. Quartet symmetry is not an obstruction; it is part of the adversary.

Conclusion: **quartet symmetry is already built into the bad model**.

## 4.4 Pair correlation and spacing

Pair correlation is not available as an unconditional theorem in the required form. It is also primarily a statement about critical-line ordinates, while this model concerns hypothetical off-line packets with both ordinate displacement and off-critical depth.

Even assuming simple zeros does not help. Simplicity forbids exact collision but does not impose a polynomial lower bound on spacing.

Conclusion: **pair-spacing input is currently heuristic only**.

## 4.5 Same-scale constraint

The same-scale condition

\[
x_j^2+c_j^2=d^2
\]

looks restrictive, but no known zeta-side theorem prevents several off-line packets from lying approximately on such a circle in the \((x,c)\)-plane.

If one demands exact same-scale equality, the model is idealized. But the proof only needs polynomially small source curvature, not exact equality. Approximate same-scale placement within a sufficiently small tolerance is enough to preserve the countermodel to finite order.

Conclusion: **same-scale geometry alone does not exclude the adversary**.

## 4.6 Integer multiplicity / simple-zero replacement

The clean quadrature uses positive real weights. Actual zeros have integer multiplicities, and expectedly multiplicity one.

But this is not a decisive blocker. Positive weights can be rationally approximated, and multiplicities can be split into nearby simple zeros. For finite-order matching to polynomial accuracy, the required number of simple replacement packets is still finite and can remain far below the weakest known local zero-counting upper bounds.

Conclusion: **integer/simple-zero constraints do not presently rescue the zero-side route**.

---

# 5. Precise insufficiency statement

The strongest statement I can justify from this lane is the following.

```latex
\begin{proposition}[Zero-side constraints do not exclude source-flattening quadrature]
\label{prop:zero-side-constraints-do-not-exclude-source-flattening}
Fix \(M\ge1\) and \(d>0\).  In the same-scale packet model
\[
x^2+c^2=d^2,\qquad c>0,
\]
there exists a finite positive, symmetry-closed packet collection
\(\mathcal Q_M\), with \(O(M)\) same-scale packets, such that its local source
profile satisfies
\[
q_{\mathcal Q_M}(0)>0,
\qquad
q_{\mathcal Q_M}^{(2)}(0)
=
q_{\mathcal Q_M}^{(4)}(0)
=
\cdots
=
q_{\mathcal Q_M}^{(2M)}(0)
=
0.
\]
Moreover the construction is compatible with centered ordinate symmetry,
functional-equation pairing, conjugation symmetry, positivity of the packet
weights, Gram positivity, and strict same-scale core separation after an
arbitrarily small perturbation.  In particular, for \(q_0=2\) one has
\[
\Gamma_G
=
q''-6q_0+2q_0^3
=
4
\]
while \(q''=0\).  Hence the known local zero-packet constraints alone do not
imply a polynomial lower bound for source curvature.
\end{proposition}
```

Proof sketch: use the continuous identity

\[
\int_0^\pi K_{\theta,d}(u)\frac{2}{\pi}\sin\theta\,d\theta=\frac1d
\]

for \(|u|<d\), then replace the measure by a positive finite quadrature matching the moments

\[
\sin\theta,\sin3\theta,\ldots,\sin(2M+1)\theta.
\]

---

# 6. Candidate theorem actually needed

To close Agent 3’s route, one would need a new arithmetic theorem of the following type.

```latex
\begin{theorem}[No actual-zeta same-scale source-flattening quadrature]
\label{thm:no-actual-zeta-source-flattening-quadrature}
Let \(I_\rho\) be an admissible reduced packet interval attached to a
hypothetical off-critical packet of actual \(\zeta\), and let
\(\mathcal A(m,d,\varepsilon)\) denote the actual-zeta zeros whose local packet
coordinates satisfy
\[
|x_\rho^2+c_\rho^2-d^2|\le \varepsilon d^2.
\]
For some constants \(B,M,\varepsilon>0\), depending only on the reduced-patch
parameters, the actual zero packet vector satisfies
\[
\max_{1\le k\le M}
\left|
\sum_{\rho\in\mathcal A(m,d,\varepsilon)}
w_\rho
\sin((2k+1)\theta_\rho)
+
\mathcal B_k(m)
\right|
\ge Q^{-B},
\]
where \(\mathcal B_k(m)\) denotes the controlled background/core/gamma
contribution in the paper's canonical source convention.
Equivalently, actual zeta zeros cannot form a positive same-scale quadrature
which cancels
\[
q'',q^{(4)},\ldots,q^{(2M)}
\]
to polynomial accuracy on \(I_\rho\).
\end{theorem}
```

This theorem is **not** a consequence of known zero counting, zero-density, quartet symmetry, or pair-spacing input. It is essentially an actual-zeta anti-design theorem for the off-line packet coordinates.

---

# 7. Agent 3 handoff

The zero-side route does not currently close. The finite positive same-scale quadrature construction gives a robust local adversary:

\[
q''=q^{(4)}=\cdots=q^{(2M)}=0,
\qquad
q_0>0,
\qquad
\Gamma_G\asymp1.
\]

Known zero-side constraints do not exclude actual zeros from approximating this pattern at the level required for the current proof architecture. Therefore Agent 3’s conclusion is:

\[
\boxed{
\text{Zero-side local constraints are insufficient; a new actual-zeta anti-quadrature theorem is required.}
}
\]

The next useful work is not more local packet geometry. It is either:

\[
\text{prime/AFE fixed-coefficient observability}
\]

or a genuinely new theorem showing that actual zeta zeros cannot form the above same-scale positive quadrature.

I’ll now test the bridge itself. The key question is whether the identity forces anisotropy when \(q''\) has \(L^2\)-mass, or whether one can build good-patch countermodels near the base locus.

_Thought for 1m 38s_

## Agent 3 / C — Quantitative ODE rigidity for source–anisotropy reintegration

I focused on the assigned bridge problem:

\[
u=q'',\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)}
\]

and the identity

\[
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
\]

This is exactly the new Agent 3 target in the coordinator instruction. 

---

# 1. Main verdict

The bridge theorem is **plausible**, but only with explicit analytic good-patch assumptions. Source observability alone,

\[
\int_I |u|^2\,dm\ge Q^{-B}|I|,
\]

does **not** automatically imply

\[
\int_I |u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\ge Q^{-A}|I|.
\]

However, the ODE identity strongly suggests the bridge can be proved if the paper has, or adds, a quantitative analytic-complexity package: Bernstein/Cauchy derivative bounds, propagation of smallness, and nonconcentration for \(u=q''\).

Without those assumptions, I can construct soft countermodels by hiding \(u\)-mass on tiny subintervals or by making \(\Gamma_G\) small-amplitude/high-frequency so that \(\Gamma_G''\) cancels \(2q(q')^2\). With polynomial analytic-complexity bounds, those countermodels only produce **polynomial** losses, so they do not kill the desired \(Q^{-A}\)-type theorem.

So the correct status is:

\[
\boxed{
\text{Source observability + analytic good-patch control plausibly implies vector observability.}
}
\]

but

\[
\boxed{
\text{Source observability alone is insufficient.}
}
\]

This matches the updated two-gate architecture: source observability is Gate 1, and source–anisotropy reintegration is an independent Gate 2. 

---

# 2. Algebraic reduction

Let

\[
f(q)=6q-2q^3=2q(3-q^2).
\]

Then

\[
\Gamma_G=u-f(q).
\]

The first anisotropy wall is therefore

\[
u\approx f(q).
\]

Now differentiate:

\[
\Gamma_G''
=
q^{(4)}-6q''+12q(q')^2+6q^2q''.
\]

Hence

\[
-\frac16\Gamma_G''
=
-\frac16q^{(4)}+q''-2q(q')^2-q^2q'',
\]

so

\[
2q(q')^2-\frac16\Gamma_G''
=
(1-q^2)q''-\frac16q^{(4)}
=
\Gamma_{G,2}.
\]

Thus the simultaneous smallness regime is

\[
\Gamma_G\approx0,
\qquad
\Gamma_{G,2}\approx0,
\]

equivalently

\[
q''\approx f(q),
\qquad
\Gamma_G''\approx 12q(q')^2.
\]

This is the key rigidity structure.

---

# 3. Exact base locus over an interval

If

\[
\Gamma_G\equiv0
\]

on an interval, then

\[
q''=f(q)=6q-2q^3.
\]

Then

\[
\Gamma_{G,2}
=
2q(q')^2.
\]

Therefore, if also

\[
\Gamma_{G,2}\equiv0,
\]

then

\[
q(q')^2\equiv0.
\]

On any open interval, this forces either:

1. \(q\equiv0\), hence \(u=q''\equiv0\); or
2. \(q'\equiv0\), hence \(q\) is constant. Then \(u=0\), and \(\Gamma_G=0\) forces
   \[
   q\in\{0,\pm\sqrt3\}.
   \]

So the exact base locus has no source mass:

\[
\Gamma_G\equiv\Gamma_{G,2}\equiv0
\quad\Longrightarrow\quad
u\equiv0.
\]

This is the structural reason the bridge is plausible.

---

# 4. Quantitative rigidity lemma to aim for

The paper should aim for a lemma of the following form.

```latex
\begin{lemma}[Quantitative source--anisotropy rigidity]
\label{lem:source-anisotropy-rigidity}
Let \(I\) be an admissible good-patch interval of length
\(|I|\asymp Q^{-1}\).  Put
\[
u=q'',\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)}.
\]
Assume the source-curvature lower bound
\[
\int_I |u|^2\,dm\ge Q^{-B}|I|.
\]
Assume also the good-patch analytic-complexity bounds
\[
\|q^{(r)}\|_{L^\infty(I^\ast)}\le Q^{C_r}
\qquad 0\le r\le 6,
\]
on a fixed enlargement \(I^\ast\supset I\), together with the corresponding
Bernstein/Remez propagation bounds for the analytic functions
\(u,\Gamma_G,\Gamma_{G,2}\).  Then there exists
\(A=A(B,C_0,\ldots,C_6)\) such that
\[
\int_I |u|^2
\left(\Gamma_G^2+\Gamma_{G,2}^2\right)\,dm
\ge Q^{-A}|I|.
\]
\end{lemma}
```

The phrase “corresponding Bernstein/Remez propagation bounds” should not be left vague in the final paper. It should mean something like:

```latex
For every analytic good-patch function \(F\) arising from the local source
package, smallness of \(F\) on a subset of \(I\) of measure at least
\(Q^{-C}|I|\) propagates to polynomially controlled \(C^2\)-smallness on a
subinterval \(J\subset I\) of length at least \(Q^{-C'}|I|\).
```

This is the analytic input needed to prevent concentration and high-frequency cancellation.

---

# 5. Proof skeleton

Prove the lemma by contrapositive.

Assume

\[
V_I:=
\int_I |u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\le Q^{-A}|I|
\]

with \(A\) very large.

Because

\[
\int_I |u|^2\,dm\ge Q^{-B}|I|,
\]

and \(\|u\|_\infty\le Q^C\), there is a set \(E\subset I\) of polynomial measure,

\[
|E|\ge Q^{-C_1}|I|,
\]

on which

\[
|u|\ge Q^{-C_2}.
\]

On most of this set, the weighted smallness of \(V_I\) forces

\[
|\Gamma_G|+|\Gamma_{G,2}|\le Q^{-C_3}
\]

after choosing \(A\) sufficiently large.

By analytic propagation, there is a subinterval \(J\subset I\), with

\[
|J|\ge Q^{-C_4}|I|,
\]

on which

\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|
\le Q^{-C_5}.
\]

Now use

\[
\Gamma_G=u-f(q),
\]

so on \(J\),

\[
u=q''=f(q)+O(Q^{-C_5}).
\]

Also use

\[
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G'',
\]

so

\[
2q(q')^2=O(Q^{-C_5})
\]

on \(J\).

There are then three cases.

## Case 1: \(q\) near a root of \(f\)

The roots are

\[
q=0,\qquad q=\pm\sqrt3.
\]

If \(q\) stays within \(Q^{-c}\) of these roots and \(\Gamma_G\) is small, then

\[
u=f(q)+O(\Gamma_G)
\]

is also small. That contradicts the fact that \(u\) has polynomial mass on \(J\), unless \(\Gamma_G\) is already polynomially large. In that latter case, \(V_I\) is already bounded below.

## Case 2: \(q\) bounded away from \(0,\pm\sqrt3\)

Then \(|f(q)|\) is polynomially bounded below wherever \(|u|\) is. Hence

\[
|q''|=|u|\ge Q^{-C}.
\]

But

\[
2q(q')^2=O(Q^{-C_5})
\]

forces \(q'\) to be small. A function with \(q''\) polynomially large on a subinterval of length \(Q^{-C}|I|\) cannot keep \(q'\) polynomially smaller than the corresponding \(q''\)-accumulation scale. Quantitatively,

\[
\sup_J |q'|
\ge
\frac12 |J|\inf_J |q''|
\ge Q^{-C_6}.
\]

Therefore

\[
|q(q')^2|
\ge Q^{-C_7}
\]

on a smaller subinterval, which forces

\[
|\Gamma_{G,2}|+\frac16|\Gamma_G''|\ge Q^{-C_7}.
\]

If \(\Gamma_G''\) is small by propagation, then \(\Gamma_{G,2}\) is polynomially large. If \(\Gamma_G''\) is not small, then \(\Gamma_G\) must have polynomial amplitude by Bernstein, and \(\Gamma_G\) itself contributes to \(V_I\).

Either way,

\[
V_I\ge Q^{-A'}|I|.
\]

## Case 3: high-frequency cancellation

The only way to keep

\[
\Gamma_{G,2}
=
2q(q')^2-\frac16\Gamma_G''
\]

small while \(2q(q')^2\) is polynomially large is to arrange

\[
\Gamma_G''\approx 12q(q')^2.
\]

If \(\Gamma_G\) has analytic frequency at most polynomial in \(Q\), Bernstein gives

\[
\|\Gamma_G''\|_\infty
\le Q^C \|\Gamma_G\|_\infty.
\]

Thus cancellation of a polynomial-sized \(2q(q')^2\) requires

\[
\|\Gamma_G\|_\infty\ge Q^{-C'}.
\]

Then \(\Gamma_G\) itself contributes polynomially to the vector energy.

So high-frequency cancellation is not fatal unless the good-patch class permits super-polynomial frequencies.

---

# 6. Escape scenario audit

## Escape 1: \(\Gamma_G\) small on most \(u\)-mass

This is not fatal. It forces

\[
q''\approx 6q-2q^3.
\]

The second identity then gives

\[
\Gamma_{G,2}\approx 2q(q')^2
\]

up to the \(\Gamma_G''\) term. Thus either \(\Gamma_{G,2}\) becomes visible, or \(\Gamma_G''\) must cancel it.

## Escape 2: \(\Gamma_G''\) cancels \(2q(q')^2\)

This is the main technical risk. But with analytic Bernstein bounds, cancellation costs amplitude:

\[
\Gamma_G''\sim Q^{C}\Gamma_G.
\]

So a polynomial-sized cancellation requires polynomial-sized \(\Gamma_G\). This is compatible with the desired theorem because the theorem only asks for a polynomial lower bound.

Without Bernstein/analytic-complexity control, this escape is real.

## Escape 3: \(q\) near \(0\) or \(\pm\sqrt3\)

These are precisely the roots of

\[
f(q)=6q-2q^3.
\]

Near them, \(\Gamma_G\approx0\) implies \(u\approx0\). Thus source mass cannot live there unless \(\Gamma_G\) itself is large. So these base points are not dangerous under source observability.

## Escape 4: high-frequency oscillation in \(\Gamma_G\)

Dangerous only if the local good-patch theory allows super-polynomial frequency. If the analytic scale is \(Q^{-1}\) or a polynomial refinement thereof, high-frequency oscillation loses only polynomial powers and can be absorbed into \(A\).

## Escape 5: source mass concentrated on tiny subintervals

Source observability is an \(L^2\) statement, so concentration is possible unless ruled out. With only

\[
\int_I |u|^2\ge Q^{-B}|I|,
\]

one can hide mass on a very small set. Therefore the bridge needs nonconcentration, either as a direct good-patch hypothesis or as a consequence of analytic derivative bounds/Remez propagation.

---

# 7. Countermodel if good-patch assumptions are too weak

If the paper only assumes \(L^2\)-source mass and pointwise smoothness, the bridge is false.

Sketch: choose a small subinterval \(J\subset I\) of length \(\ell\ll |I|\), put \(u=q''\) mostly on \(J\), and choose \(q\) so that on \(J\)

\[
q''\approx 6q-2q^3,
\qquad
q'\approx0.
\]

Then

\[
\Gamma_G\approx0,
\qquad
\Gamma_{G,2}\approx 2q(q')^2\approx0
\]

on the source-supporting region, while

\[
\int_I |u|^2
\]

can be kept at size \(Q^{-B}|I|\) by increasing the amplitude of \(u\) on \(J\).

Derivative bounds prevent \(\ell\) from being arbitrarily small. If those derivative bounds are polynomial in \(Q\), the countermodel only defeats overly ambitious constants; it does not defeat a \(Q^{-A}\) theorem with sufficiently large \(A\). But without a fixed analytic-complexity exponent, no quantitative bridge follows.

---

# 8. Recommended paper insertion

Add this after the statement that source observability is necessary but not sufficient.

```latex
\begin{remark}[The source--anisotropy bridge is an ODE rigidity problem]
\label{rem:source-anisotropy-ode-rigidity}
Source-curvature observability alone does not yet recover the rank-two row
lower bound.  The missing bridge is the vector estimate
\[
\int_{I_\rho}|q''|^2
\left(\Gamma_G^2+\Gamma_{G,2}^2\right)\,dm
\ge Q^{-A}|I_\rho|.
\]
Writing
\[
u=q'',\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=(1-q^2)u-\frac16q^{(4)},
\]
one has the identity
\[
\boxed{\;
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
\;}
\]
Indeed,
\[
\Gamma_G''
=
q^{(4)}-6q''+12q(q')^2+6q^2q'',
\]
which gives the displayed formula.  Thus the simultaneous smallness of
\(\Gamma_G\) and \(\Gamma_{G,2}\) is not a purely algebraic base-locus
condition: if \(\Gamma_G\approx0\), then \(q\) approximately solves
\[
q''=6q-2q^3,
\]
while \(\Gamma_{G,2}\approx0\) forces
\[
\Gamma_G''\approx 12q(q')^2.
\]
In particular, exact vanishing on an interval implies \(q''\equiv0\).
The quantitative bridge should therefore be formulated as an analytic
good-patch rigidity lemma: source \(L^2\)-mass plus Bernstein/Remez
propagation for \(q,\Gamma_G,\Gamma_{G,2}\) should force a polynomial lower
bound for the vector anisotropy energy.  Without such analytic
nonconcentration and frequency-control hypotheses, source mass can be hidden
on small subintervals or masked by high-frequency cancellation in
\(\Gamma_G''\).
\end{remark}
```

Then add the lemma target:

```latex
\begin{lemma}[Target source--anisotropy rigidity lemma]
\label{lem:target-source-anisotropy-rigidity}
Let \(I_\rho\) be an admissible good-patch interval.  Assume
\[
\int_{I_\rho}|q''|^2\,dm\ge Q^{-B}|I_\rho|
\]
and assume the local analytic-complexity bounds for
\(q,\Gamma_G,\Gamma_{G,2}\), including polynomial Bernstein and propagation
of smallness on \(I_\rho\).  Then there is \(A=A(B,\mathrm{patch})\) such that
\[
\int_{I_\rho}|q''|^2
\left(\Gamma_G^2+\Gamma_{G,2}^2\right)\,dm
\ge Q^{-A}|I_\rho|.
\]
\end{lemma}
```

---

# 9. Final Agent 3 status

\[
\boxed{
\text{The ODE identity gives a viable bridge route, but not a free one.}
}
\]

The paper should not claim that Gate 1 automatically implies Gate 2. It should state Gate 2 as a separate quantitative ODE/analytic rigidity lemma whose proof requires polynomial analytic-complexity control.

The most important next technical task is to inventory the current “good-patch” hypotheses and verify whether they already imply the needed Bernstein/Remez/nonconcentration package. If yes, this bridge may be provable with a large but finite exponent \(A\). If not, that package must be added as a new missing lemma.
## User (2026-04-26 13:03:31)

The paper has been updated with some corrections attached. Please read then await your next instruction.

## Assistant (2026-04-26 13:03:58)

_Thought for 18s_

Read the updated draft and the repair patch.

I see the corrections have been incorporated around:

- \(q''_{\can}=q_\zeta''=\Phi_\zeta'''\) as the canonical full actual-zeta phase curvature.
- \(q''_{\source,R}=(G^{\new})''\) as the affine-subtracted complement-source curvature, kept separate.
- Gate 1: source-curvature observability.
- Gate 2: source–anisotropy vector observability.
- The repaired ODE identity:
  \[
  \Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
  \]
- The status language that source observability is necessary but not sufficient, and the rank-two route remains conditional without Gate 1 + Gate 2 or a source-robust/global replacement. 

Ready for the next Agent 3 / Agent C instruction.
## User (2026-04-26 13:05:01)

Do your next agent prompt as per your number in the attached.

## Assistant (2026-04-26 13:05:05)

I’ll handle Agent 3 / C: canonical Gate 1 numerics. I’ll first pin down the draft’s current \(q''_{\can}\), \(Q\), and interval convention, then give either runnable diagnostics or a completed small numerical probe if the environment supports it.

_Thought for 5m 17s_

## Agent 3 / C — Gate 1 canonical actual-zeta numerics

### 0. Scope

The assigned Agent 3 task is now **Gate 1 canonical actual-zeta numerics**:

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm\ge Q^{-B}|I_\rho|,
\qquad
q''_{\can}=q_\zeta''=\Phi_\zeta'''.
\]

The repair patch explicitly fixes \(q''_{\can}\) as the full actual-zeta phase curvature, not \(q''_{\source,R}=(G^{\new})''\), and asks for Gate 1 to be tested separately from Gate 2.  The attached prompt asks Agent 3/C to run or specify three tests: zero-side canonical scan, prime/AFE scan, and same-scale quadrature negative control. 

---

# 1. Important computational warning

A direct computation using

\[
\arg \xi(1/2+it)
\]

is **not** a valid canonical scan. On the critical line, \(\xi(1/2+it)\) is real-valued, so its argument is piecewise \(0\) or \(\pi\), with jumps at zeros. Numerically differentiating that argument gives a false “zero curvature” signal away from zeros and spike artifacts near zeros.

So the canonical numerical test must use one of:

\[
q''_{\can}=B_2+\sum_{\rho}^{\rm reg}K_2(m;\rho),
\]

or

\[
q''_{\can}=B_2+P_2+D_2+E_2,
\]

with the paper’s regularization/background conventions fixed.

At present, the draft has fixed the **object** \(q''_{\can}\), but the exact numerical representation still has unresolved choices: zero regularization, background/tail treatment, AFE smoothing, \(b_n\), \(D_2\), and \(E_2\). Therefore I ran a proof-relevant **zero-side regularized proxy** and a **negative-control quadrature model**, and I give reproducible pseudocode for the full prime/AFE scan.

---

# 2. Test A — zero-side regularized proxy

## Formula used

I used low-height zeta zero ordinates \(\gamma\) and the regularized packet kernel

\[
K_\varepsilon(x)=\frac{\varepsilon}{x^2+\varepsilon^2}.
\]

Then

\[
K_\varepsilon''(x)
=
\frac{2\varepsilon(3x^2-\varepsilon^2)}{(x^2+\varepsilon^2)^3}.
\]

The tested proxy was

\[
q''_{\zero,\varepsilon}(m)
=
\sum_{\gamma\in\mathcal Z_{\rm trunc}}
K_\varepsilon''(m-\gamma),
\]

with

\[
Q=\log(m_0/2\pi),
\qquad
I=[m_0-0.2/Q,m_0+0.2/Q],
\qquad
\varepsilon=0.5/Q.
\]

For each interval:

\[
S_I=\sup_{m\in I}|q''_{\zero,\varepsilon}(m)|,
\]

\[
E_I=|I|^{-1}\int_I |q''_{\zero,\varepsilon}(m)|^2\,dm,
\]

\[
B_I^{\rm eff}
=
-\frac{\log E_I}{\log Q}.
\]

This is **not yet the full canonical scan** because \(B_2\), tail, and exact regularization are not fixed. It is a useful sanity check: does actual zero geometry show source-flat behavior resembling the quadrature adversary?

## Low-height proxy output

Centers were chosen at midpoints between adjacent zero ordinates to avoid intentionally placing the interval center on a singularity.

| \(m_0\) | \(Q\) | half-width | \(\varepsilon\) | \(S_I\) | \(E_I\) | \(B_I^{\rm eff}\) |
|---:|---:|---:|---:|---:|---:|---:|
| 104.586 | 2.812 | 0.07112 | 0.17780 | 3.622 | 12.1607 | -2.416 |
| 115.273 | 2.909 | 0.06874 | 0.17186 | 2.369 | 5.2887 | -1.560 |
| 125.887 | 2.998 | 0.06672 | 0.16681 | 0.303 | 0.0894 | 2.199 |
| 136.436 | 3.078 | 0.06498 | 0.16244 | 0.267 | 0.0699 | 2.367 |
| 146.712 | 3.151 | 0.06348 | 0.15870 | 6.786 | 42.277 | -3.263 |
| 156.855 | 3.217 | 0.06216 | 0.15540 | 5.719 | 30.226 | -2.917 |
| 166.361 | 3.276 | 0.06104 | 0.15261 | 3.762 | 13.291 | -2.180 |
| 175.598 | 3.330 | 0.06005 | 0.15014 | 3.414 | 10.982 | -1.992 |
| 185.237 | 3.384 | 0.05911 | 0.14777 | 70.178 | 4149.58 | -6.834 |
| 194.173 | 3.431 | 0.05829 | 0.14574 | 1.254 | 1.5148 | -0.337 |

## Interpretation

This proxy shows **no super-polynomial source-flatness**. The smallest energy found was

\[
E_I\approx 6.99\times 10^{-2},
\qquad
B_I^{\rm eff}\approx 2.37,
\]

at very small \(Q\), where \(B_I^{\rm eff}\) is numerically unstable. That is not a quadrature-like collapse. It is polynomially healthy.

Verdict for Test A:

\[
\boxed{
\text{Zero-side regularized actual-zero proxy supports Gate 1; it does not threaten it.}
}
\]

But this remains only proxy evidence.

---

# 3. Test B — prime/AFE scan design

The correct prime/AFE test should use the canonical representation:

\[
q''_{\can}(m)
=
B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

with

\[
P_2(m)
=
\Re
\sum_{n\le X}
b_n(\log n)^2 n^{-1/2-im}W(n/T).
\]

For each center \(m_0\):

\[
Q=\log(m_0/2\pi),
\qquad
I=[m_0-c/Q,m_0+c/Q].
\]

Then compute:

\[
F_X(m)=B_2(m)+D_2(m)+
\Re
\sum_{n\le X}
b_n(\log n)^2n^{-1/2-im}W(n/T),
\]

and report:

\[
S_I=\max_{m\in I}|F_X(m)|,
\]

\[
E_I=\frac1N\sum_{j=1}^{N}|F_X(m_j)|^2,
\]

\[
B_I^{\rm eff}=-\frac{\log E_I}{\log Q}.
\]

## Pseudocode

```python
def P2(m, X, coeffs, W, T):
    total = 0j
    for n in range(1, X+1):
        total += coeffs[n] * (log(n)**2) * n**(-0.5 - 1j*m) * W(n/T)
    return total.real

def qpp_can_AFE(m):
    return B2(m) + P2(m, X, coeffs, W, T) + D2(m)

def interval_stats(m0, c=0.2, N=201):
    Q = log(m0/(2*pi))
    half = c/Q
    grid = [m0-half + 2*half*j/(N-1) for j in range(N)]
    vals = [qpp_can_AFE(x) for x in grid]
    S = max(abs(v) for v in vals)
    E = sum(v*v for v in vals)/N
    B_eff = -log(E)/log(Q)
    return S, E, B_eff
```

## Blocking issue

This test cannot be responsibly run until the draft fixes:

\[
b_n,\quad W,\quad X,\quad T,\quad D_2,\quad B_2,\quad E_2.
\]

Running it with arbitrary \(b_n\) or arbitrary smoothing would test a surrogate Dirichlet polynomial, not actual \(q''_{\can}\).

Verdict for Test B:

\[
\boxed{
\text{Prime/AFE Gate 1 scan is specified, but not runnable canonically until the AFE normalization is fixed.}
}
\]

---

# 4. Test C — same-scale quadrature negative control

This is the adversarial control that should artificially create source-flatness.

Use same-scale packets:

\[
x=d\cos\theta,
\qquad
c=d\sin\theta,
\]

\[
K_{\theta,d}(u)
=
\frac{d\sin\theta}{(u-d\cos\theta)^2+d^2\sin^2\theta}.
\]

With positive density

\[
d\mu(\theta)=\frac2\pi\sin\theta\,d\theta,
\]

the aggregate profile is constant for \(|u|<d\):

\[
\int_0^\pi K_{\theta,d}(u)\,d\mu(\theta)=\frac1d.
\]

Therefore

\[
\frac{d^2}{du^2}
\int_0^\pi K_{\theta,d}(u)\,d\mu(\theta)
=
0.
\]

I numerically integrated this negative-control model at \(Q\approx3.078\), \(d=1/Q\), \(I=[-0.2/Q,0.2/Q]\). The result was:

\[
S_I\approx5.7\times10^{-15},
\]

\[
E_I\approx3.5\times10^{-30},
\]

\[
B_I^{\rm eff}\approx60.3.
\]

This is the expected artificial source-flatness signature.

Verdict for Test C:

\[
\boxed{
\text{The quadrature control produces extreme flatness; the actual-zero proxy did not resemble it.}
}
\]

---

# 5. Runnable zero-side proxy code

```python
import mpmath as mp
import math

mp.mp.dps = 30

zeros = [float(mp.im(mp.zetazero(n))) for n in range(1, 121)]

def qpp_zero_reg(t, zeros, eps):
    s = 0.0
    for gamma in zeros:
        x = t - gamma
        den = x*x + eps*eps
        s += 2*eps*(3*x*x - eps*eps)/(den**3)
    return s

def interval_stats_zero_reg(m0, c=0.20, kappa=0.50, n=101):
    Q = math.log(m0/(2*math.pi))
    half = c/Q
    eps = kappa/Q
    vals = [
        qpp_zero_reg(m0-half+2*half*j/(n-1), zeros, eps)
        for j in range(n)
    ]
    E = sum(v*v for v in vals)/len(vals)
    S = max(abs(v) for v in vals)
    B_eff = -math.log(E)/math.log(Q) if E > 0 and Q > 1 else float("nan")
    return S, E, B_eff
```

---

# 6. Final verdict

\[
\boxed{
\text{Gate 1 is numerically plausible and not currently threatened.}
}
\]

The strongest statement supported by this run is narrower:

\[
\boxed{
\text{A low-height, regularized zero-side actual-zero proxy does not show source-flat intervals.}
}
\]

The negative-control same-scale quadrature model does show extreme source-flatness, so the diagnostic is capable of detecting the bad behavior when it is present.

The next numerical step should be to make the scan genuinely canonical by fixing the exact \(B_2+\sum K_2\) regularization and the exact \(B_2+P_2+D_2+E_2\) AFE normalization. Until then, the evidence supports Gate 1 but does not prove it and should not be cited as more than a sanity check.
## User (2026-04-26 13:22:55)

Here is one more round of paper revisions + latest paper draft reflecting these. Please read then await your next instruction.

## Assistant (2026-04-26 13:22:59)

_Thought for a couple of seconds_

Read the latest revisions and draft.

The paper now appears aligned with the current two-gate status:

\[
\text{Gate 1: }\int_{I_\rho}|q''_{\can}(m)|^2\,dm\ge Q^{-B}|I_\rho|
\]

and

\[
\text{Gate 2: }\int_{I_\rho}|q''_{\can}(m)|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm\ge Q^{-A}|I_\rho|.
\]

The attached repair list focuses on canonicalizing \(q''_{\can}\), replacing stale “Gate 1 alone” language, and preserving the same-scale model as a local/Hadamard-side no-go with its own local-kernel notation guard. 

Ready for the next Agent 3 / Agent C instruction.
## User (2026-04-26 13:25:19)

Do your agent prompt as per your agent number.

## Assistant (2026-04-26 13:25:20)

I’ll attack the requested local ODE rigidity directly. The critical point is a turning-point escape: exact base-locus contact can occur at a point, so the question is whether it can persist on a polynomially large interval.

_Thought for 54s_

## Agent 3 / C — Quantitative ODE base-locus rigidity

### Verdict

The base-locus rigidity component is **provable** once Agents 1–2 have produced a polynomially large interval \(J'\) on which

\[
|u|\ge Q^{-C_0},
\qquad
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le Q^{-C_2}.
\]

There is no genuine interval-level escape. The only apparent escape is a **finite-type turning-point contact** at a point, but it cannot persist on a polynomially large interval unless the smallness exponent \(C_2\) is only polynomially weak. Thus this piece fits the Gate-2 package described in the latest coordinator note. 

---

# 1. Setup

Let

\[
u=q''_{\can},
\]

\[
\Gamma_G=u-6q+2q^3,
\]

and use the corrected identity

\[
\Gamma_{G,2}
=
2q(q')^2-\frac16\Gamma_G''.
\]

Equivalently,

\[
\Gamma_G=u-f(q),
\qquad
f(q)=6q-2q^3=2q(3-q^2).
\]

The target contradiction hypothesis is:

\[
|u|\ge \delta,
\]

and

\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le \varepsilon
\]

on an interval \(J\) of length \(\ell\), where in applications

\[
\delta=Q^{-C_0},
\qquad
\ell\ge Q^{-L},
\qquad
\varepsilon=Q^{-C_2}.
\]

Assume also the standard good-patch size bound

\[
|q|\le M
\]

on \(J\), with \(M\le Q^{C_q}\). This is the only local size bound needed for the rigidity step.

---

# 2. Core rigidity lemma

```latex
\begin{lemma}[Quantitative ODE base-locus rigidity]
\label{lem:quantitative-ode-base-locus-rigidity}
Let \(J\) be an interval of length \(\ell\).  Put
\[
u=q'',\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
\]
Assume on \(J\) that
\[
|q|\le M,
\qquad
|u|\ge \delta,
\]
and
\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le \varepsilon.
\]
If \(\varepsilon\le \delta/4\), then necessarily
\[
\varepsilon
\ge
c\,\frac{\delta^3\ell^2}{3+M^2}
\]
for an absolute constant \(c>0\).  Consequently, if
\[
\varepsilon
<
c\,\frac{\delta^3\ell^2}{3+M^2},
\]
no such interval \(J\) exists.
\end{lemma}
```

### Proof

Since

\[
\Gamma_G=u-f(q),
\qquad
f(q)=6q-2q^3,
\]

we have

\[
|f(q)|\ge |u|-|\Gamma_G|
\ge \delta-\varepsilon
\ge \frac34\delta.
\]

In particular \(f(q)\) does not vanish on \(J\), so its sign is constant. Hence \(u=f(q)+\Gamma_G\) also has a fixed sign on \(J\), and

\[
|u|\ge\delta.
\]

Next,

\[
|f(q)|
=
|2q(3-q^2)|
\le 2|q|(3+M^2).
\]

Thus

\[
|q|
\ge
\frac{|f(q)|}{2(3+M^2)}
\ge
\frac{3\delta}{8(3+M^2)}.
\]

Using

\[
\Gamma_{G,2}
=
2q(q')^2-\frac16\Gamma_G'',
\]

we get

\[
2|q||q'|^2
\le
|\Gamma_{G,2}|+\frac16|\Gamma_G''|
\le
2\varepsilon,
\]

after harmless adjustment of constants. Therefore

\[
|q'|^2
\le
\frac{\varepsilon}{|q|}
\le
C\frac{(3+M^2)\varepsilon}{\delta},
\]

so

\[
\sup_J |q'|
\le
C
\left(
\frac{(3+M^2)\varepsilon}{\delta}
\right)^{1/2}.
\]

On the other hand, since \(u=q''\) has fixed sign and \(|u|\ge\delta\),

\[
|q'(b)-q'(a)|
=
\left|\int_a^b q''(m)\,dm\right|
\ge
\delta\ell
\]

for the endpoints \(a,b\) of \(J\). But the previous bound gives

\[
|q'(b)-q'(a)|
\le
2\sup_J|q'|
\le
C
\left(
\frac{(3+M^2)\varepsilon}{\delta}
\right)^{1/2}.
\]

Therefore

\[
\delta\ell
\le
C
\left(
\frac{(3+M^2)\varepsilon}{\delta}
\right)^{1/2},
\]

and hence

\[
\varepsilon
\ge
c\,\frac{\delta^3\ell^2}{3+M^2}.
\]

This proves the lemma.

---

# 3. Polynomial \(Q\)-form

In the Gate-2 application, suppose

\[
\delta=Q^{-C_0},
\qquad
\ell\ge Q^{-L},
\qquad
M\le Q^{C_q}.
\]

Then the lemma says that simultaneous base-locus smallness on \(J\) forces

\[
\varepsilon
\ge
Q^{-(3C_0+2L+2C_q+O(1))}.
\]

Therefore, if the propagation step gives

\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|
\le
Q^{-C_2}
\]

with

\[
C_2>3C_0+2L+2C_q+O(1),
\]

then the base-locus interval is impossible.

So the precise output for the Gate-2 package is:

\[
\boxed{
\text{Polynomially thick source mass + sufficiently strong propagated anisotropy smallness contradict ODE rigidity.}
}
\]

---

# 4. Turning-point finite-type model

The only local subtlety is a turning point where the base-locus equations hold at a single point.

Take

\[
q(0)=a,
\qquad
q'(0)=0,
\qquad
q''(0)=u_0=6a-2a^3,
\qquad
q^{(3)}(0)=0.
\]

Then

\[
\Gamma_G(0)=u_0-6a+2a^3=0.
\]

Also,

\[
\Gamma_{G,2}
=
2q(q')^2-\frac16\Gamma_G'',
\]

so if \(\Gamma_G''(0)=0\), then

\[
\Gamma_{G,2}(0)=0.
\]

Thus there is a genuine **pointwise contact** with

\[
u_0\ne0,
\qquad
\Gamma_G(0)=0,
\qquad
\Gamma_{G,2}(0)=0,
\qquad
\Gamma_G''(0)=0.
\]

This means one cannot prove Gate 2 by pointwise algebra alone.

Now verify the claimed finite-type degeneracy. If the second base-locus relation

\[
\Gamma_{G,2}=0
\]

is imposed to second order near the point, then

\[
\Gamma_G''=12q(q')^2.
\]

Differentiate twice:

\[
\Gamma_G^{(4)}
=
12\frac{d^2}{dm^2}\left(q(q')^2\right).
\]

Since \(q'(0)=0\), \(q''(0)=u_0\), and \(q^{(3)}(0)=0\),

\[
\frac{d^2}{dm^2}\left(q(q')^2\right)\bigg|_{m=0}
=
2a u_0^2.
\]

Therefore

\[
\boxed{
\Gamma_G^{(4)}(0)=24a u_0^2.
}
\]

This is the finite-type obstruction: unless

\[
a=0
\quad\text{or}\quad
u_0=0,
\]

the base-locus contact opens at fourth order. But

\[
u_0=6a-2a^3=2a(3-a^2),
\]

so \(u_0=0\) precisely at

\[
a=0,\quad a=\pm\sqrt3.
\]

Those are exactly the zero-source base points. They are incompatible with \(|u|\ge\delta\).

Thus a nonzero-source turning point can mimic the base locus at a point, but the finite type is four and the contact cannot remain small on an interval longer than a polynomial scale unless the smallness threshold is correspondingly weak.

---

# 5. Escape-case audit

## 5.1 \(q\) near \(0,\pm\sqrt3\)

These are the roots of

\[
f(q)=6q-2q^3.
\]

If \(\Gamma_G\) is small and \(q\) is near one of these roots, then

\[
u=f(q)+\Gamma_G
\]

is small. This contradicts

\[
|u|\ge\delta
\]

unless \(\Gamma_G\) is already polynomially large. Therefore these points do not produce an interval escape.

## 5.2 \(q'\) tiny while \(q''\) has mass

This is impossible on a polynomially large interval. If

\[
|q''|\ge\delta
\]

with fixed sign, then \(q'\) changes by at least

\[
\delta\ell.
\]

But smallness of \(\Gamma_{G,2}\) and \(\Gamma_G''\) forces

\[
|q'|^2
\lesssim
\frac{\varepsilon}{|q|}.
\]

For \(\varepsilon\) sufficiently small, the two estimates contradict.

## 5.3 \(\Gamma_G''\) cancels \(12q(q')^2\)

The prompt includes \(\Gamma_G''\) itself among the small quantities. Therefore cancellation is not available at this rigidity stage. If

\[
|\Gamma_G''|\le\varepsilon
\]

and

\[
|\Gamma_{G,2}|\le\varepsilon,
\]

then

\[
|2q(q')^2|\le O(\varepsilon).
\]

So the cancellation branch has already been eliminated by the propagation step.

## 5.4 High-frequency oscillation in \(\Gamma_G\)

Again, once Agent 2’s propagation gives direct smallness of \(\Gamma_G''\), high frequency is irrelevant to this local lemma. High frequency is a risk for the propagation lemma, not for the base-locus ODE step.

## 5.5 \(u\)-mass concentrated on tiny subintervals

This is not handled by the base-locus lemma. It is exactly why Agent 1 must prove source-mass thickening. Once a polynomially large interval \(J\) with \(|u|\ge\delta\) is extracted, the ODE lemma applies.

---

# 6. Counterexample if the interval hypothesis is removed

There is a genuine pointwise counterexample:

\[
q(0)=a,\quad q'(0)=0,\quad q''(0)=6a-2a^3,\quad q^{(3)}(0)=0,
\]

with \(a\notin\{0,\pm\sqrt3\}\), and choose \(q^{(4)}(0)\) so that

\[
\Gamma_G''(0)=0.
\]

Then

\[
u(0)\ne0,
\qquad
\Gamma_G(0)=0,
\qquad
\Gamma_{G,2}(0)=0,
\qquad
\Gamma_G''(0)=0.
\]

So **pointwise algebra cannot prove Gate 2**. The proof must use interval thickness and propagation.

This is not a counterexample to the interval theorem. It only confirms the current architecture: Gate 2 needs the full good-patch analytic package.

---

# 7. LaTeX-ready insertion

```latex
\begin{lemma}[Quantitative ODE base-locus rigidity]
\label{lem:quantitative-ode-base-locus-rigidity}
Let \(J\) be an interval of length \(\ell\).  Put
\[
u=q''_{\can},
\qquad
\Gamma_G=u-6q+2q^3,
\qquad
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''.
\]
Assume on \(J\) that
\[
|q|\le M,\qquad |u|\ge\delta,
\]
and
\[
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le\varepsilon.
\]
If \(\varepsilon\le\delta/4\), then
\[
\varepsilon
\ge
c\,\frac{\delta^3\ell^2}{3+M^2}
\]
for an absolute constant \(c>0\).  Hence, for
\[
\varepsilon
<
c\,\frac{\delta^3\ell^2}{3+M^2},
\]
no such interval \(J\) exists.
\end{lemma}

\begin{proof}
Write
\[
f(q)=6q-2q^3.
\]
Since
\[
\Gamma_G=u-f(q),
\]
we have
\[
|f(q)|\ge |u|-|\Gamma_G|
\ge \delta-\varepsilon
\ge \frac34\delta .
\]
Thus \(f(q)\) has constant sign on \(J\).  Since
\[
|f(q)|=|2q(3-q^2)|\le 2|q|(3+M^2),
\]
we also have
\[
|q|\ge \frac{3\delta}{8(3+M^2)}.
\]
The identity
\[
\Gamma_{G,2}=2q(q')^2-\frac16\Gamma_G''
\]
then gives
\[
2|q||q'|^2
\le
|\Gamma_{G,2}|+\frac16|\Gamma_G''|
\le C\varepsilon,
\]
and therefore
\[
\sup_J |q'|
\le
C\left(\frac{(3+M^2)\varepsilon}{\delta}\right)^{1/2}.
\]
On the other hand, \(u=q''\) has fixed sign on \(J\), because
\(u=f(q)+\Gamma_G\) and \(|\Gamma_G|\le\varepsilon<\delta/4\).  Hence, if
\(a,b\) are the endpoints of \(J\),
\[
|q'(b)-q'(a)|
=
\left|\int_a^b q''(m)\,dm\right|
\ge
\delta\ell.
\]
Combining the two estimates gives
\[
\delta\ell
\le
C\left(\frac{(3+M^2)\varepsilon}{\delta}\right)^{1/2},
\]
or
\[
\varepsilon
\ge
c\,\frac{\delta^3\ell^2}{3+M^2}.
\]
\end{proof}
```

And the turning-point remark:

```latex
\begin{remark}[Finite-type turning-point contact]
\label{rem:finite-type-turning-point-contact}
The base locus has genuine pointwise contacts, so the preceding lemma cannot
be replaced by pointwise algebra.  Let
\[
q(0)=a,\qquad q'(0)=0,\qquad q''(0)=u_0=6a-2a^3,
\qquad q^{(3)}(0)=0.
\]
Then
\[
\Gamma_G(0)=0.
\]
If \(q^{(4)}(0)\) is chosen so that \(\Gamma_G''(0)=0\), then also
\[
\Gamma_{G,2}(0)=0.
\]
Thus one may have \(u_0\ne0\) and simultaneous pointwise vanishing of the two
anisotropy factors.

However, if the second base-locus relation
\[
\Gamma_{G,2}=0
\]
is imposed to second order, then
\[
\Gamma_G''=12q(q')^2.
\]
Consequently
\[
\Gamma_G^{(4)}(0)
=
12\frac{d^2}{dm^2}\left(q(q')^2\right)\bigg|_{m=0}
=
24a u_0^2.
\]
For \(a\notin\{0,\pm\sqrt3\}\), this quantity is nonzero.  Hence the
base-locus contact is finite type and cannot persist on a polynomially large
interval with super-polynomial smallness.  This is why Gate~2 requires
source-mass thickening and propagation of smallness, not merely pointwise
algebra.
\end{remark}
```

---

# 8. Final Agent 3 handoff

The base-locus rigidity step is now clean:

\[
\boxed{
|u|\ge Q^{-C_0}
\quad\text{on a polynomially long interval}
}
\]

plus

\[
\boxed{
|\Gamma_G|+|\Gamma_{G,2}|+|\Gamma_G''|\le Q^{-C_2}
}
\]

is impossible when \(C_2\) is chosen sufficiently large relative to the source lower bound, interval length, and polynomial size bound for \(q\).

Thus Agent 3’s component of Gate 2 is not the bottleneck. The bottlenecks are now:

1. extracting the polynomially long interval where \(|u|\) is bounded below;
2. propagating small anisotropy energy to pointwise smallness of \(\Gamma_G,\Gamma_{G,2},\Gamma_G''\);
3. proving the required derivative/analytic-complexity bounds for full \(q_\zeta\).
## User (2026-04-26 13:32:49)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:33:37)

_Thought for 46s_

## Agent 3 / C — Core-packet denominator and finite-core derivative bounds

### Verdict

The finite-core derivative-complexity bound is straightforward **conditional on one indispensable good-patch hypothesis**:

\[
\inf_{\nu\in\mathcal L}\inf_{m\in I_\rho^\ast}
\Delta_\nu(m)\ge Q^{-C_{\rm sep}},
\]

where \(\Delta_\nu(m)\) is the distance from \(m\) to the singularity/packet center in the local zero-kernel denominator.

Under this polynomial separation and a polynomial core-size bound,

\[
|\mathcal L|\le Q^{C_{\rm core}},
\]

one obtains

\[
\sup_{m\in I_\rho^\ast}|q_{\core}^{(r)}(m)|
\le Q^{C_r},
\qquad 0\le r\le6.
\]

So the finite-core part is **not** the bottleneck, provided the reduced good-patch construction really excludes exponentially shallow or nearly singular core packets. The latest coordinator prompt identifies this as Agent 3’s assigned component of the derivative-complexity package. 

---

# 1. One-packet kernel

For one off-critical packet with local ordinate \(\gamma_\nu\), depth \(c_\nu>0\), and weight/sign \(\omega_\nu\), the standard local source kernel for the phase derivative has the form

\[
K_\nu(m)
=
\omega_\nu
\frac{c_\nu}{(m-\gamma_\nu)^2+c_\nu^2}.
\]

Equivalently,

\[
K_\nu(m)
=
\omega_\nu\,\Im\frac{1}{m-\gamma_\nu-ic_\nu}.
\]

Let

\[
x_\nu(m)=m-\gamma_\nu,
\qquad
D_\nu(m)=x_\nu(m)^2+c_\nu^2,
\qquad
\Delta_\nu(m)=D_\nu(m)^{1/2}.
\]

Then

\[
K_\nu(m)=\omega_\nu\frac{c_\nu}{D_\nu(m)}.
\]

The finite core is

\[
q_{\core}(m)
=
\sum_{\nu\in\mathcal L}K_\nu(m),
\]

up to harmless quartet multiplicity constants. If the paper groups zeros into quartets, each quartet is just a finite sum of at most four such kernels with conjugation/reflection-related parameters.

---

# 2. Derivative bound for one packet

Since

\[
\frac{c}{x^2+c^2}
=
\Im\frac{1}{x-ic},
\]

we have

\[
\frac{d^r}{dm^r}
\frac{c_\nu}{(m-\gamma_\nu)^2+c_\nu^2}
=
(-1)^r r!\,
\Im\frac{1}{(m-\gamma_\nu-ic_\nu)^{r+1}}.
\]

Therefore

\[
|K_\nu^{(r)}(m)|
\le
|\omega_\nu|\,r!\,
\Delta_\nu(m)^{-(r+1)}.
\]

If one uses the squared denominator \(D_\nu\) rather than the Euclidean distance \(\Delta_\nu\), the same estimate is

\[
|K_\nu^{(r)}(m)|
\le
|\omega_\nu|\,r!\,
D_\nu(m)^{-(r+1)/2}.
\]

For \(0\le r\le6\),

\[
|K_\nu^{(r)}(m)|
\ll_r
|\omega_\nu|\Delta_\nu(m)^{-(r+1)}.
\]

If the draft’s normalization uses a differentiated curvature kernel rather than the phase-derivative kernel itself, the exponent shifts by the number of extra derivatives. But for the assigned target

\[
q_{\core}^{(r)},\qquad 0\le r\le6,
\]

the natural exponent is \(r+1\).

---

# 3. Good-patch denominator condition

The required good-patch condition is:

\[
\Delta_\nu(m)
=
\sqrt{(m-\gamma_\nu)^2+c_\nu^2}
\ge Q^{-C_{\rm sep}}
\]

for all

\[
m\in I_\rho^\ast,\qquad \nu\in\mathcal L.
\]

Equivalently,

\[
D_\nu(m)\ge Q^{-2C_{\rm sep}}.
\]

If the paper writes the condition as

\[
\operatorname{denom}_\nu(m)\ge Q^{-C},
\]

then it must specify whether \(\operatorname{denom}\) means \(\Delta_\nu\) or \(D_\nu\). The derivative exponent depends on that convention:

\[
\Delta_\nu\ge Q^{-C}
\quad\Rightarrow\quad
|K_\nu^{(r)}|\ll_r Q^{(r+1)C};
\]

\[
D_\nu\ge Q^{-C}
\quad\Rightarrow\quad
|K_\nu^{(r)}|\ll_r Q^{(r+1)C/2}.
\]

Either convention is fine, but it must be fixed.

---

# 4. Finite-core derivative bound

Assume:

\[
|\mathcal L|\le Q^{C_{\rm core}},
\]

\[
|\omega_\nu|\le Q^{C_\omega},
\]

and

\[
\Delta_\nu(m)\ge Q^{-C_{\rm sep}}
\qquad
(m\in I_\rho^\ast,\ \nu\in\mathcal L).
\]

Then for \(0\le r\le6\),

\[
\begin{aligned}
|q_{\core}^{(r)}(m)|
&\le
\sum_{\nu\in\mathcal L}
|K_\nu^{(r)}(m)|\\
&\ll_r
\sum_{\nu\in\mathcal L}
|\omega_\nu|\Delta_\nu(m)^{-(r+1)}\\
&\ll_r
Q^{C_{\rm core}}
Q^{C_\omega}
Q^{(r+1)C_{\rm sep}}.
\end{aligned}
\]

Thus

\[
\sup_{m\in I_\rho^\ast}
|q_{\core}^{(r)}(m)|
\le
Q^{C_r^{\core}},
\]

with

\[
C_r^{\core}
=
C_{\rm core}+C_\omega+(r+1)C_{\rm sep}+O_r(1).
\]

For \(r\le6\), one can take

\[
C_r^{\core}
\le
C_{\rm core}+C_\omega+7C_{\rm sep}+O(1).
\]

So the finite-core derivative-complexity estimate is polynomial with explicit exponent loss.

---

# 5. Quartet symmetry

Quartet symmetry does **not** worsen the bound.

A quartet contribution is a finite sum such as

\[
K_{\nu}^{\quartet}
=
K_{\gamma,c}
+
K_{-\gamma,c}
+
K_{\gamma,-c}
+
K_{-\gamma,-c},
\]

or the equivalent real/phase-normalized variant used in the draft. The precise signs depend on the phase convention, but for derivative bounds this is irrelevant:

\[
|(K_{\nu}^{\quartet})^{(r)}|
\le
4\max_{\eta\in\quartet}|K_\eta^{(r)}|.
\]

Thus quartet symmetry only changes constants. It may improve cancellations, but no cancellation is needed for the upper bound.

Conclusion:

\[
\boxed{
\text{Quartet symmetry improves constants at best; it is not needed for finite-core derivative control.}
}
\]

---

# 6. Distinguished off-line packet

The distinguished off-line packet is safe **only if** the reduced good patch keeps its denominator polynomially bounded below on \(I_\rho^\ast\).

For the packet \(P\),

\[
K_P(m)=\omega_P\frac{c_P}{(m-\gamma_P)^2+c_P^2}.
\]

If \(I_\rho^\ast\) contains \(m=\gamma_P\), then

\[
\Delta_P(\gamma_P)=c_P.
\]

Therefore,

\[
|K_P^{(r)}(\gamma_P)|
\asymp
c_P^{-(r+1)}
\]

for the relevant even/odd derivatives up to constants. Hence:

- If \(c_P\ge Q^{-C}\), then the distinguished packet is polynomially controlled.
- If \(c_P=e^{-Q}\), then
  \[
  |K_P^{(r)}(\gamma_P)|\asymp e^{(r+1)Q},
  \]
  and derivative complexity fails.
- If \(c_P=0\), corresponding to a critical-line singular packet in this simplified kernel model, the kernel is singular at \(m=\gamma_P\), so \(I_\rho^\ast\) must exclude that point by a reduced-gap condition.

Thus the reduced good-patch construction must include either:

\[
c_P\ge Q^{-C_{\rm sep}},
\]

or

\[
\inf_{m\in I_\rho^\ast}|m-\gamma_P|\ge Q^{-C_{\rm sep}},
\]

or the combined denominator condition

\[
\inf_{m\in I_\rho^\ast}
\sqrt{(m-\gamma_P)^2+c_P^2}
\ge Q^{-C_{\rm sep}}.
\]

This is essential. Without it, the finite-core derivative package is false.

---

# 7. Sharp conditional theorem

The finite-core component can be stated as:

\[
\textbf{Finite-core derivative-complexity theorem.}
\]

Let

\[
q_{\core}(m)
=
\sum_{\nu\in\mathcal L}
\omega_\nu
\frac{c_\nu}{(m-\gamma_\nu)^2+c_\nu^2}
\]

or any quartet grouping of this finite sum. Suppose on \(I_\rho^\ast\):

\[
|\mathcal L|\le Q^{C_{\rm core}},
\]

\[
|\omega_\nu|\le Q^{C_\omega},
\]

and

\[
\Delta_\nu(m)
=
\sqrt{(m-\gamma_\nu)^2+c_\nu^2}
\ge Q^{-C_{\rm sep}}
\quad
\text{for all }m\in I_\rho^\ast,\ \nu\in\mathcal L.
\]

Then for every \(0\le r\le6\),

\[
\sup_{m\in I_\rho^\ast}
|q_{\core}^{(r)}(m)|
\ll_r
Q^{C_{\rm core}+C_\omega+(r+1)C_{\rm sep}}.
\]

In particular,

\[
\sup_{m\in I_\rho^\ast}
|q_{\core}^{(r)}(m)|
\le
Q^{C_r}
\qquad
(0\le r\le6)
\]

for polynomial exponents \(C_r\).

---

# 8. Necessary assumptions

The finite-core proof needs exactly these hypotheses:

1. **Polynomial core size**
   \[
   |\mathcal L|\le Q^{C_{\rm core}}.
   \]

2. **Polynomial weights/multiplicities**
   \[
   |\omega_\nu|\le Q^{C_\omega}.
   \]
   For simple zeros and fixed quartet grouping, \(C_\omega=0\).

3. **Polynomial denominator separation**
   \[
   \inf_{\nu\in\mathcal L}
   \inf_{m\in I_\rho^\ast}
   \Delta_\nu(m)
   \ge Q^{-C_{\rm sep}}.
   \]

4. **Uniform validity of the kernel representation on \(I_\rho^\ast\)**  
   No branch jumps, unregularized critical-line singularities, or hidden affine-subtraction changes inside the enlarged interval.

No zero-density theorem is needed for the finite core itself, once \(\mathcal L\) is finite and polynomially bounded. Zero counting is only needed to justify

\[
|\mathcal L|\le Q^{C_{\rm core}}.
\]

---

# 9. Counterexample if separation is omitted

Take a single packet

\[
K(m)=\frac{c}{m^2+c^2}
\]

with

\[
c=e^{-Q}.
\]

On an interval containing \(0\),

\[
K(0)=e^Q,
\]

and

\[
K^{(2)}(0)\asymp -2e^{3Q}.
\]

More generally,

\[
|K^{(r)}(0)|\asymp e^{(r+1)Q}
\]

for the relevant nonzero parity derivatives. This violates every polynomial derivative-complexity bound.

Therefore denominator separation is not a technical convenience. It is logically necessary.

---

# 10. Final handoff

The finite-core derivative bound is closed conditionally:

\[
\boxed{
\text{finite core + polynomial size + polynomial denominator separation}
\Rightarrow
\sup_{I_\rho^\ast}|q_{\core}^{(r)}|\le Q^{C_r},\ 0\le r\le6.
}
\]

The remaining checks belong to other agents:

- Agent 1 must combine this with \(B_\zeta\) and \(T_{\far}\).
- Agent 2 must prove the far-tail shell estimate.
- The draft must ensure that the reduced good-patch construction explicitly gives polynomial denominator separation for every core packet, including the distinguished off-line packet.
## User (2026-04-26 13:43:30)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:43:31)

I’ll focus only on Agent 3’s denominator-separation task: whether the reduced/good-patch hypotheses actually keep every core packet polynomially away from singular denominators on \(I_\rho^\ast\).

_Thought for 23s_

## Agent 3 / C — Core denominator separation on \(I_\rho^\ast\)

### Verdict

Core denominator separation is **not automatic** from “put all near packets into the finite core.” It is a separate good-patch condition.

The finite-core derivative bound is valid if we assume

\[
|\mathcal L|\le Q^{C_{\core}}
\]

and

\[
\inf_{\nu\in\mathcal L}\inf_{m\in I_\rho^\ast}
\Delta_\nu(m)\ge Q^{-C_{\sep}},
\qquad
\Delta_\nu(m)=\sqrt{c_\nu^2+(m-\gamma_\nu)^2}.
\]

But this lower bound is not forced merely by quartet symmetry, endpoint separation, strict core gap, or by including all polynomially near zeros in \(\mathcal L\). The attached instruction correctly isolates this as Agent 3’s current task: determine whether every core denominator is polynomially separated on \(I_\rho^\ast\), including the distinguished off-line packet. 

---

# 1. What assumptions actually keep denominators away from zero?

The needed assumption is exactly a **polynomial denominator-separation condition**:

\[
\Delta_\nu(I_\rho^\ast)
:=
\inf_{m\in I_\rho^\ast}
\sqrt{c_\nu^2+(m-\gamma_\nu)^2}
\ge Q^{-C_{\sep}}
\qquad(\nu\in\mathcal L).
\]

Equivalent forms are:

\[
(m-\gamma_\nu)^2+c_\nu^2\ge Q^{-2C_{\sep}},
\]

or, if the draft defines denominator as the squared quantity,

\[
D_\nu(m):=(m-\gamma_\nu)^2+c_\nu^2\ge Q^{-C_D}.
\]

These are equivalent after changing exponents.

The usual qualitative good-patch assumptions are not enough:

- **Finite core** only says the number of packets is finite.
- **Near-zero inclusion** only says close packets are placed in \(\mathcal L\), not that their denominators are bounded below.
- **Endpoint separation** only protects against centers lying too close to endpoints; it does not protect against a center lying inside \(I_\rho^\ast\).
- **Strict core gap** separates core from tail; it does not separate core packets from the sampling interval.
- **Quartet symmetry** gives algebraic pairing, not denominator lower bounds.

Thus the required good-patch hypothesis must explicitly say either:

\[
\Delta_\nu(I_\rho^\ast)\ge Q^{-C_{\sep}}
\]

for every core packet, or give assumptions that imply it case by case.

---

# 2. Case analysis

## Case A — packet center lies inside \(I_\rho^\ast\)

If

\[
\gamma_\nu\in I_\rho^\ast,
\]

then

\[
\inf_{m\in I_\rho^\ast}\Delta_\nu(m)=c_\nu.
\]

Therefore denominator separation is equivalent to

\[
c_\nu\ge Q^{-C_{\sep}}.
\]

If \(c_\nu\) is sub-polynomially small, for example

\[
c_\nu=e^{-Q},
\]

then the denominator condition fails even though the packet is correctly classified as core.

For the kernel

\[
K_\nu(m)=\frac{c_\nu}{(m-\gamma_\nu)^2+c_\nu^2},
\]

one has

\[
K_\nu(\gamma_\nu)=c_\nu^{-1},
\]

and higher derivatives grow like

\[
|K_\nu^{(r)}(\gamma_\nu)|\asymp c_\nu^{-(r+1)}
\]

for the relevant parity. Thus \(c_\nu=e^{-Q}\) gives exponential derivative complexity.

Conclusion:

\[
\boxed{
\gamma_\nu\in I_\rho^\ast
\quad\Rightarrow\quad
\text{need }c_\nu\ge Q^{-C_{\sep}}.
}
\]

This is especially important for the distinguished off-line packet.

---

## Case B — packet center lies near an endpoint

If

\[
\gamma_\nu\notin I_\rho^\ast
\]

but lies within distance \(d_\nu\) of an endpoint, then

\[
\Delta_\nu(I_\rho^\ast)=\sqrt{d_\nu^2+c_\nu^2}.
\]

Hence polynomial separation follows if either

\[
d_\nu\ge Q^{-C_{\sep}}
\]

or

\[
c_\nu\ge Q^{-C_{\sep}}.
\]

Endpoint separation alone is enough only if it quantitatively says:

\[
\operatorname{dist}(\gamma_\nu,\partial I_\rho^\ast)\ge Q^{-C}
\]

or

\[
\operatorname{dist}(\gamma_\nu,I_\rho^\ast)\ge Q^{-C}.
\]

A qualitative statement such as “not at the endpoint” is insufficient.

---

## Case C — packet has very small off-critical depth \(c_\nu\)

If

\[
c_\nu<Q^{-C}
\]

for every fixed \(C\), then denominator separation can still hold only if the center is horizontally separated:

\[
\operatorname{dist}(\gamma_\nu,I_\rho^\ast)\ge Q^{-C_{\sep}}.
\]

If such a shallow packet lies inside or sub-polynomially near \(I_\rho^\ast\), derivative complexity fails.

Therefore the good-patch rule must exclude the joint event

\[
c_\nu<Q^{-C}
\quad\text{and}\quad
\operatorname{dist}(\gamma_\nu,I_\rho^\ast)<Q^{-C}
\]

for core packets, unless that packet is removed by regularization and not included in \(q_{\core}\).

---

## Case D — critical-line or near-critical-line packet

For a critical-line zero in this local denominator model,

\[
c_\nu=0.
\]

Then

\[
\Delta_\nu(m)=|m-\gamma_\nu|.
\]

If

\[
\gamma_\nu\in I_\rho^\ast,
\]

then

\[
\inf_{m\in I_\rho^\ast}\Delta_\nu(m)=0.
\]

So an unregularized critical-line packet inside the enlarged interval breaks finite-core derivative complexity.

There are only three ways out:

1. \(I_\rho^\ast\) avoids all critical-line centers by polynomial distance:
   \[
   \operatorname{dist}(\gamma_\nu,I_\rho^\ast)\ge Q^{-C_{\sep}}.
   \]

2. Critical-line packets are not represented by singular core kernels, but by a regularized canonical contribution with explicit polynomial derivative bounds.

3. The interval is punctured or reduced so the singular center is outside the working interval.

Without one of these, the core derivative estimate is false.

---

# 3. Distinguished off-line packet

The distinguished packet \(P\) must be handled explicitly.

If \(P\in\mathcal L\) and its ordinate center \(\gamma_P\) lies in \(I_\rho^\ast\), then

\[
\Delta_P(I_\rho^\ast)=c_P.
\]

Therefore the derivative package requires

\[
c_P\ge Q^{-C_{\sep}}.
\]

This is a serious condition. A hypothetical off-line zero could a priori have

\[
0<c_P<Q^{-C}
\]

for every fixed \(C\), unless the proof setup deliberately restricts to polynomially off-line packets or proves a zero-free strip-like lower bound on the transverse depth. There is no known general theorem excluding zeros at sub-polynomial distance from the critical line.

So the clean statement is:

\[
\boxed{
\text{Either the distinguished packet has polynomial off-critical depth, or the finite-core derivative package fails near its center.}
}
\]

If the proof intends to handle arbitrarily shallow off-line zeros, \(I_\rho^\ast\) cannot be centered directly on \(\gamma_P\) using an unregularized kernel without additional renormalization.

---

# 4. Can very small denominators be harmless by cancellation?

No, not for the derivative-complexity package as currently used.

Quartet symmetry can cancel some odd terms or improve constants, but it does not uniformly cancel all derivatives through order six. A single shallow denominator produces terms like

\[
\Delta^{-(r+1)}
\]

or, for differentiated curvature-level kernels, even stronger powers. Unless the quartet contribution is identically regularized by construction, the absolute derivative bound

\[
\sup_{I_\rho^\ast}|q_{\core}^{(r)}|\le Q^{C_r}
\]

fails.

A simple counterexample is one symmetric pair with kernel

\[
K(m)=\frac{c}{(m-\gamma)^2+c^2}
\]

and \(c=e^{-Q}\). At \(m=\gamma\),

\[
K(\gamma)=e^Q,
\]

so even \(r=0\) is already non-polynomial. No cancellation from adding reflected packets at distant ordinates changes this local blowup.

Thus:

\[
\boxed{
\text{Small core denominators are not harmless unless the kernel itself is regularized or subtracted.}
}
\]

---

# 5. Conditional finite-core derivative theorem

Assume:

\[
|\mathcal L|\le Q^{C_{\core}},
\]

\[
|\omega_\nu|\le Q^{C_\omega},
\]

and

\[
\Delta_\nu(m)\ge Q^{-C_{\sep}}
\qquad
(\nu\in\mathcal L,\ m\in I_\rho^\ast).
\]

For a phase-derivative-level packet

\[
K_\nu(m)=\omega_\nu\frac{c_\nu}{(m-\gamma_\nu)^2+c_\nu^2},
\]

we have

\[
|K_\nu^{(r)}(m)|
\ll_r
|\omega_\nu|\Delta_\nu(m)^{-(r+1)}.
\]

Therefore, for \(0\le r\le6\),

\[
\begin{aligned}
\sup_{m\in I_\rho^\ast}|q_{\core}^{(r)}(m)|
&\le
\sum_{\nu\in\mathcal L}
\sup_{m\in I_\rho^\ast}|K_\nu^{(r)}(m)|\\
&\ll_r
|\mathcal L|Q^{C_\omega}Q^{(r+1)C_{\sep}}\\
&\le
Q^{C_{\core}+C_\omega+(r+1)C_{\sep}+O_r(1)}.
\end{aligned}
\]

Thus

\[
\boxed{
|\mathcal L|\le Q^{C_{\core}},
\quad
\Delta_\nu\ge Q^{-C_{\sep}}
\quad\Longrightarrow\quad
\sup_{I_\rho^\ast}|q_{\core}^{(r)}|\le Q^{C_r},
\quad 0\le r\le6.
}
\]

The exponent may be taken as

\[
C_r=C_{\core}+C_\omega+(r+1)C_{\sep}+O_r(1).
\]

If the kernel is already curvature-level rather than phase-derivative-level, replace \(r+1\) by the appropriate shifted exponent, usually \(r+3\). The conclusion remains polynomial under the same denominator condition.

---

# 6. Explicit failure mode

If the reduced good-patch construction allows a core packet with

\[
\Delta_\nu(I_\rho^\ast)<Q^{-C}
\]

for every fixed \(C\), derivative complexity can fail.

Take

\[
c_\nu=e^{-Q},
\qquad
\gamma_\nu\in I_\rho^\ast.
\]

Then

\[
\Delta_\nu(I_\rho^\ast)=e^{-Q},
\]

and for the one-packet kernel,

\[
\sup_{I_\rho^\ast}|K_\nu^{(r)}|
\gg e^{(r+1)Q}
\]

for appropriate \(r\). This is super-polynomial. The finite core may have cardinality one; the failure is entirely due to denominator collapse.

So the obstruction is not core size. It is **core denominator degeneracy**.

---

# 7. Final answer to the assigned question

The denominator-separation statement is **conditional**, not currently a consequence of merely having a finite core.

The proof architecture needs one of the following as an explicit good-patch rule:

\[
\boxed{
\inf_{\nu\in\mathcal L}\inf_{m\in I_\rho^\ast}
\sqrt{c_\nu^2+(m-\gamma_\nu)^2}
\ge Q^{-C_{\sep}}.
}
\]

or the equivalent split condition:

\[
\boxed{
\forall \nu\in\mathcal L,\quad
c_\nu\ge Q^{-C_{\sep}}
\quad\text{or}\quad
\operatorname{dist}(\gamma_\nu,I_\rho^\ast)\ge Q^{-C_{\sep}}.
}
\]

This must include the distinguished off-line packet. If the distinguished packet is centered in \(I_\rho^\ast\), then one must assume or prove

\[
c_P\ge Q^{-C_{\sep}}.
\]

No core packet with sub-polynomial denominator distance can remain in the unregularized finite core. Quartet symmetry does not rescue it.
## User (2026-04-26 13:46:49)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:46:51)

I’ll treat critical-line zeros as a separate regularization issue from shallow off-line packets. The decisive question is whether the canonical \(q_\zeta\) is a smooth phase derivative across critical zeros or a punctured/log-derivative object.

_Thought for 21s_

## Agent 3 / C — Critical-line zeros inside \(I_\rho^\ast\)

### Verdict

Critical-line zeros are a **separate regularization/interval-avoidance issue**, not merely another instance of shallow off-line denominator separation.

If the canonical object \(q_\zeta=\Phi_\zeta'\) is represented through a raw log-derivative or zero-kernel decomposition, then a critical-line zero with ordinate \(\gamma\in I_\rho^\ast\) creates either:

\[
\frac{1}{m-\gamma}
\]

principal-value behavior, or a phase-jump / delta-type contribution, depending on the exact phase convention. In neither case is \(q_\zeta\) an ordinary \(C^6\) function across \(\gamma\). Therefore the Gate-2 derivative-complexity package requires one of two explicit mechanisms:

\[
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C}
\]

for every critical-line zero represented by a singular kernel, or a canonical regularization that removes the singularity and proves polynomial bounds through order six.

The current denominator-separation discussion in the latest coordinator instruction explicitly identifies critical-line zeros inside \(I_\rho^\ast\) as one of the unresolved cases. 

---

# 1. Local behavior near a critical-line zero

Let

\[
\rho=\frac12+i\gamma
\]

be a simple critical-line zero. Near \(t=\gamma\), the completed real Hardy function

\[
\Xi(t)=\xi\!\left(\frac12+it\right)
\]

has local form

\[
\Xi(t)=a(t-\gamma)+O((t-\gamma)^2),
\qquad a\ne0.
\]

Thus

\[
\frac{d}{dt}\log \Xi(t)
=
\frac{1}{t-\gamma}+O(1).
\]

So any canonical representation based on a raw logarithmic derivative has a pole at \(t=\gamma\).

If instead the phase is defined as an argument, then \(\Xi(t)\) is real on the critical line, so its argument is piecewise constant and jumps by \(\pi\) at a simple zero. Its derivative is not an ordinary function; it is distributional:

\[
\frac{d}{dt}\arg \Xi(t)
\sim \pi\delta(t-\gamma).
\]

Thus the singularity is not eliminated by switching from log-derivative language to phase-jump language. It merely changes from a principal-value pole to a distributional jump.

---

# 2. Off-line kernel limit as \(c\to0\)

For an off-line packet with transverse depth \(c>0\), the usual local Poisson kernel is

\[
K_c(m-\gamma)
=
\frac{c}{(m-\gamma)^2+c^2}.
\]

As \(c\to0^+\),

\[
K_c \to \pi\delta_\gamma
\]

in distributions. Pointwise, at \(m=\gamma\),

\[
K_c(\gamma)=\frac1c.
\]

Higher derivatives grow like

\[
|K_c^{(r)}(\gamma)|\asymp c^{-(r+1)}
\]

for the relevant parity. Thus the critical-line case \(c=0\) is not a harmless finite value. It is a singular limit.

So if critical-line zeros are represented as \(c=0\) packets in the same core kernel model, then any interval \(I_\rho^\ast\) crossing \(\gamma\) destroys ordinary derivative complexity.

---

# 3. Is \(I_\rho^\ast\) allowed to cross critical-line zeros?

There are two possible setups.

## Setup A — punctured smooth phase intervals

If \(q_\zeta\) is meant to be a classical function on \(I_\rho^\ast\), then \(I_\rho^\ast\) must avoid every critical-line zero ordinate by a polynomial margin:

\[
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C_{\rm crit}}.
\]

Then for a critical-line zero kernel

\[
K_\gamma(m)=\frac{1}{m-\gamma}
\]

or its differentiated variants,

\[
|K_\gamma^{(r)}(m)|
\ll_r
\operatorname{dist}(I_\rho^\ast,\gamma)^{-(r+1)}
\le
Q^{(r+1)C_{\rm crit}},
\]

which is polynomial.

This makes critical-line zeros part of the denominator-separation condition, with \(c_\nu=0\):

\[
\Delta_\nu(m)=|m-\gamma_\nu|.
\]

## Setup B — regularized completed phase

If the paper defines \(q_\zeta\) after subtracting phase jumps, taking symmetric principal values, or using a smoothed counting/regularized explicit formula, then critical-line zeros may be allowed inside \(I_\rho^\ast\). But then the derivative-complexity package must be proved for the **regularized** object, not for the raw kernel.

The required theorem would be:

\[
\sup_{m\in I_\rho^\ast}
\left|
\partial_m^r q_{\zeta,\mathrm{reg}}(m)
\right|
\le Q^{C_r},
\qquad 0\le r\le6.
\]

This cannot be inferred from the raw zero-kernel expression if \(I_\rho^\ast\) crosses a zero. It must come from the regularization definition itself.

---

# 4. Does the completed/Hardy convention make the singularity disappear?

Not automatically.

The Hardy function \(Z(t)\) is real, and its sign changes at simple critical zeros. This can make the **continuous phase convention** look smoother away from zeros, but the sign change still forces a \(\pi\)-jump if one tracks argument continuously modulo \(2\pi\). The derivative of that jump is distributional.

For \(\zeta\) itself,

\[
\zeta\!\left(\frac12+it\right)
=
e^{-i\theta(t)}Z(t),
\]

so

\[
\arg \zeta\!\left(\frac12+it\right)
=
-\theta(t)+\arg Z(t).
\]

The \(\arg Z(t)\) term jumps at zeros. Therefore

\[
\frac{d}{dt}\arg \zeta\!\left(\frac12+it\right)
\]

is not a classical smooth function through zeros unless the jumps are explicitly removed or regularized.

Thus “completed phase” or “Hardy phase” does not by itself prove polynomial \(C^6\) bounds across critical zeros.

---

# 5. Required interval-avoidance condition if singular

If critical-line zeros are represented by singular or distributional kernels, the good-patch definition must include:

\[
\boxed{
\operatorname{dist}(I_\rho^\ast,\gamma)
\ge Q^{-C_{\rm crit}}
\quad
\text{for every critical-line zero ordinate }\gamma
\text{ whose singular contribution is not regularized.}
}
\]

Equivalently,

\[
\inf_{\nu:c_\nu=0}
\inf_{m\in I_\rho^\ast}
\Delta_\nu(m)
=
\inf_{\nu:c_\nu=0}
\inf_{m\in I_\rho^\ast}
|m-\gamma_\nu|
\ge Q^{-C_{\rm crit}}.
\]

Then critical-line zeros fit into the same denominator-separation framework.

Without this, \(q_\zeta^{(r)}\) is not polynomially bounded, and in fact may not be an ordinary function on \(I_\rho^\ast\).

---

# 6. If regularized, what must be proved?

If the draft intends to allow \(I_\rho^\ast\) to cross critical-line zeros, then the local kernel should not be treated as

\[
\frac{1}{m-\gamma}
\]

or as the \(c\to0\) limit of

\[
\frac{c}{(m-\gamma)^2+c^2}.
\]

Instead, it must define a regularized phase object, for example by subtracting the jump/counting contribution:

\[
q_{\zeta,\mathrm{reg}}
=
q_\zeta-\pi\sum_{\gamma\in I_\rho^\ast}\delta_\gamma
\]

in distributional language, or by using a smoothed explicit formula.

Then the needed estimate is:

\[
\sup_{I_\rho^\ast}
|q_{\zeta,\mathrm{reg}}^{(r)}|
\le Q^{C_r},
\qquad 0\le r\le6.
\]

This is no longer a denominator-separation theorem. It is a **regularization theorem**. It must specify:

1. the exact subtraction or smoothing;
2. the width of smoothing;
3. how the smoothing interacts with \(q''_{\can}\);
4. whether Gate 1 and Gate 2 are being proved for the same regularized object;
5. how jump/delta terms are reinserted or shown irrelevant to the rank-two rows.

Until those are fixed, critical-line crossings should be excluded from \(I_\rho^\ast\).

---

# 7. Are critical-line zeros part of the denominator-separation problem?

They split into two cases.

## If unregularized

Yes. They are the \(c_\nu=0\) edge case of denominator separation:

\[
\Delta_\nu(m)=|m-\gamma_\nu|.
\]

Then the condition must be:

\[
\operatorname{dist}(I_\rho^\ast,\gamma_\nu)\ge Q^{-C}.
\]

## If regularized

No. They become a separate regularization/error-control problem. The derivative package must then control the regularized object rather than the raw packet kernel.

Either way, they cannot be ignored.

---

# 8. Final classification

\[
\boxed{
\text{Critical-line zeros inside }I_\rho^\ast\text{ are singular for raw canonical phase/log-derivative kernels.}
}
\]

Therefore the Gate-2 derivative-complexity package requires one of:

\[
\boxed{
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C}
\text{ for every unregularized critical-line zero,}
}
\]

or

\[
\boxed{
\text{an explicit regularized phase convention with }C^6\text{ polynomial bounds.}
}
\]

The second option is possible in principle, but it must be stated as a theorem or hypothesis. The first option is simpler and fits the denominator-separation package, but it restricts admissible intervals to avoid critical-line zero ordinates by a polynomial margin.
## User (2026-04-26 13:51:12)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:51:13)

I’ll answer the Agent 3 branch only. The key issue is whether the canonical phase is defined as a classical smooth object across critical zeros or whether those zeros must be avoided/regularized before Gate 2 derivative estimates can even be stated.

_Thought for 20s_

## Agent 3 / C — Critical-line regularization branch

### Verdict

Under the repaired canonical convention,

\[
q_\zeta=\Phi_\zeta',
\qquad
q''_{\can}=q_\zeta''=\Phi_\zeta''',
\]

a critical-line zero inside \(I_\rho^\ast\) is **not automatically harmless**. Unless the draft has explicitly regularized phase jumps, \(q_\zeta\) is not an ordinary \(C^6\) function across a critical-line zero. It has either a principal-value pole in log-derivative form or a jump/delta contribution in phase form.

So critical-line zeros should not be silently included in the smooth denominator-separated regime. They require either:

\[
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C}
\]

for every unregularized critical-line zero ordinate \(\gamma\), or a separate **regularized-jump regime** with polynomial derivative bounds for the regularized object. This is exactly the critical-line branch identified in the latest two-regime/singular-regime prompt. 

---

# 1. Local behavior near a critical-line zero

Let

\[
\rho=\frac12+i\gamma
\]

be a simple critical-line zero. For the completed real function

\[
\Xi(t)=\xi\!\left(\frac12+it\right),
\]

near \(t=\gamma\),

\[
\Xi(t)=a(t-\gamma)+O((t-\gamma)^2),
\qquad a\ne0.
\]

Therefore,

\[
\frac{d}{dt}\log \Xi(t)
=
\frac{1}{t-\gamma}+O(1).
\]

So in raw log-derivative language, a critical-line zero contributes a pole.

In phase language, \(\Xi(t)\) is real-valued on the critical line. At a simple zero, its sign changes. Hence its argument jumps by \(\pi\). Therefore,

\[
\frac{d}{dt}\arg \Xi(t)
\]

is not an ordinary smooth function across \(t=\gamma\); distributionally it contains a delta mass:

\[
\frac{d}{dt}\arg \Xi(t)
\sim \pi \delta(t-\gamma).
\]

Thus a critical-line zero is singular in either raw representation.

---

# 2. Relation to the off-line packet kernel

The usual off-line packet kernel has the model form

\[
K_c(x)=\frac{c}{x^2+c^2},
\qquad x=m-\gamma,
\]

where \(c>0\) is transverse depth.

As \(c\to0^+\),

\[
K_c \to \pi\delta_0
\]

in distributions, and pointwise

\[
K_c(0)=\frac1c.
\]

Higher derivatives scale as

\[
|K_c^{(r)}(0)|\asymp c^{-(r+1)}
\]

for the relevant parity. Therefore the critical-line case \(c=0\) is the singular endpoint of the shallow-packet regime. It is not covered by ordinary polynomial derivative complexity unless the interval avoids the zero or the kernel is regularized.

---

# 3. Is \(q_\zeta\) \(C^6\) across a critical-line zero?

Not under the raw canonical interpretation.

Using the Hardy decomposition,

\[
\zeta\!\left(\frac12+it\right)=e^{-i\theta(t)}Z(t),
\]

where \(Z(t)\) is real. Then

\[
\arg \zeta\!\left(\frac12+it\right)
=
-\theta(t)+\arg Z(t).
\]

The \(-\theta(t)\) term is smooth. But \(\arg Z(t)\) jumps by \(\pi\) at each simple critical-line zero. Hence

\[
\frac{d}{dt}\arg \zeta\!\left(\frac12+it\right)
\]

contains jump/delta behavior unless the jumps are explicitly subtracted.

Therefore, unless the draft’s canonical \(\Phi_\zeta\) is already a **regularized phase** with jumps removed or smoothed, \(q_\zeta\) is not \(C^6\) across critical-line zeros.

---

# 4. If singular: required interval-avoidance condition

If critical-line zeros are represented by raw singular kernels, then the smooth Gate-2 package requires:

\[
\boxed{
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C_{\crit}}
}
\]

for every critical-line zero ordinate \(\gamma\) whose singular contribution is not regularized.

Equivalently, treating critical-line zeros as \(c_\nu=0\) packets,

\[
\Delta_\nu(m)=|m-\gamma_\nu|,
\]

and the denominator condition becomes

\[
\inf_{\nu:c_\nu=0}\inf_{m\in I_\rho^\ast}|m-\gamma_\nu|
\ge Q^{-C_{\crit}}.
\]

Under this condition,

\[
\left|\frac{d^r}{dm^r}\frac{1}{m-\gamma}\right|
\ll_r
Q^{(r+1)C_{\crit}},
\]

so critical-line contributions are polynomially bounded through order six.

This puts avoided critical-line zeros inside the **smooth denominator-separated regime**.

---

# 5. If regularized: what must be proved?

If the canonical phase convention regularizes critical-line jumps, then the object is not the raw \(q_\zeta\), but something like

\[
q_{\zeta,\reg}
=
q_\zeta-\pi\sum_{\gamma\in I_\rho^\ast}\delta_\gamma
\]

in distributional language, or a smoothed/renormalized explicit-formula object.

Then the needed theorem is:

\[
\boxed{
\sup_{m\in I_\rho^\ast}
\left|
\partial_m^r q_{\zeta,\reg}(m)
\right|
\le Q^{C_r},
\qquad 0\le r\le6.
}
\]

But this proof must specify:

1. the exact regularization;
2. the smoothing/subtraction scale;
3. whether \(q''_{\can}\) in Gate 1 and Gate 2 is the same regularized object;
4. how jump/delta terms affect the rank-two rows;
5. whether the regularization changes the local anisotropy formulas.

Without those details, regularization cannot be assumed.

---

# 6. Which regime should critical-line zeros belong to?

There are three logically distinct cases.

## Case 1 — avoided critical-line zeros

If

\[
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C},
\]

then critical-line zeros are part of the **smooth denominator-separated regime**. They contribute polynomially to derivative complexity.

## Case 2 — unregularized critical-line zero inside \(I_\rho^\ast\)

Then \(q_\zeta\) is not classically \(C^6\) on \(I_\rho^\ast\). This is not merely a shallow off-line packet with \(c\ll Q^{-C}\); it is the endpoint \(c=0\), producing poles or distributions.

This should be treated as a **singular/jump regime**, not as part of the smooth Gate-2 proof.

## Case 3 — regularized critical-line zero inside \(I_\rho^\ast\)

If the phase convention smooths or subtracts the jump, then critical-line zeros form a **regularized-jump regime**. It may be harmless, but only after proving the regularized \(C^6\) bounds and checking compatibility with the canonical \(q''_{\can}\).

---

# 7. Can critical-line crossings help Gate 2 automatically?

Only in a distributional or regularized sense, and not safely in the present classical integral formulation.

A raw critical-line zero gives infinite or distributional source mass. One might hope this makes Gate 2 trivially true by largeness. But the Gate-2 integral is stated as a classical quantity:

\[
\int_{I_\rho}|q''_{\can}|^2
(\Gamma_G^2+\Gamma_{G,2}^2)\,dm.
\]

If \(q''_{\can}\) contains derivatives of delta functions or nonintegrable poles, the integral is not a standard finite lower-bound object. It is undefined or infinite depending on regularization. Either way, the smooth proof does not apply.

If one mollifies at scale \(\epsilon\), then the contribution is large, of order powers of \(\epsilon^{-1}\), and likely forces Gate 2 unless there is coordinated cancellation. But that becomes part of the **singular-packet dominance/cancellation branch**, not the smooth derivative-complexity branch.

---

# 8. Final classification

\[
\boxed{
\text{Critical-line zeros inside }I_\rho^\ast
\text{ are not covered by smooth denominator separation unless avoided.}
}
\]

The correct architecture is:

\[
\boxed{
\text{Smooth regime:}
\quad
\operatorname{dist}(I_\rho^\ast,\gamma)\ge Q^{-C}
\text{ for raw critical-line zeros.}
}
\]

\[
\boxed{
\text{Singular/jump regime:}
\quad
\gamma\in I_\rho^\ast
\text{ and the raw phase/log derivative is used.}
}
\]

\[
\boxed{
\text{Regularized regime:}
\quad
\text{critical-line jumps are subtracted/smoothed and }C^6
\text{ bounds are proved for the same canonical object.}
}
\]

Therefore, critical-line zeros are either part of the denominator-separation problem if unregularized, or a separate regularization problem if the canonical phase removes the jump. They cannot be ignored in the Gate-2 derivative-complexity package.
## User (2026-04-26 13:56:43)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 13:56:45)

I’ll now switch from the zero-side/singularity branches to the assigned Agent 3 prime/AFE route: finite-jet source-flatness plus the off-line packet center condition.

_Thought for 6s_

## Agent 3 / C — Prime/AFE center-conditioned source nonrecurrence

### Verdict

The off-line packet center condition does **not obviously defeat prime-log recurrence**. It adds real constraints, but not enough under current information to prove Gate 1. The prime/AFE route therefore reduces to a sharp missing theorem:

\[
\boxed{
\text{No simultaneous off-line-zero/source-flat finite-jet recurrence for actual zeta coefficients.}
}
\]

This is exactly the assigned Agent 3 task: attack Gate 1 from the prime/AFE side using the fact that \(I_\rho\) is attached to a hypothetical off-line packet, not an arbitrary interval. 

---

# 1. Gate 1 in prime/AFE form

Use the canonical representation

\[
q''_{\can}(m)
=
B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

with

\[
P_2(m)
=
\Re\sum_{n\le X}a_n e^{-im\log n}.
\]

Here:

- \(B_2\) is the gamma/background contribution;
- \(D_2\) is the dual/functional-equation contribution;
- \(E_2\) is the differentiated AFE or truncation error;
- \(P_2\) has **fixed actual-zeta coefficients**, not adjustable coefficients.

Gate 1 asks for

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
\]

Let

\[
I_\rho=[m_0-\Delta,m_0+\Delta],
\qquad
\Delta\asymp Q^{-1}.
\]

If \(q''_{\can}\) is flat on \(I_\rho\), then finite Taylor data at \(m_0\) must be small:

\[
\Delta^r
\frac{d^r}{dm^r}
\left(B_2+D_2+P_2\right)(m_0)
\approx 0,
\qquad
0\le r\le R(Q),
\]

where a natural scale audit gives

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or conservatively

\[
R(Q)=O(\log Q).
\]

Equivalently,

\[
P_2^{(r)}(m_0)
\approx
-\left(B_2+D_2\right)^{(r)}(m_0),
\qquad
0\le r\le R(Q).
\]

Since

\[
P_2^{(r)}(m_0)
=
\Re
\sum_{n\le X}
a_n(-i\log n)^r e^{-im_0\log n},
\]

this is a finite system of weighted prime-log phase constraints.

---

# 2. Adding the off-line center condition

The extra structural information is that \(m_0\) is not arbitrary. It is the ordinate/center of a hypothetical off-line packet.

Abstractly, write the off-line zero condition as

\[
Z_\alpha(m_0)=0,
\]

where \(\alpha\) records transverse displacement or off-critical packet parameter. In a zeta model this represents something like

\[
\zeta\!\left(\frac12+\alpha+im_0\right)=0,
\]

or the completed/scattering-normalized equivalent.

This contributes two real equations:

\[
\Re Z_\alpha(m_0)=0,
\qquad
\Im Z_\alpha(m_0)=0.
\]

But if \(\alpha\) is itself free, then \((\alpha,m_0)\) gives two real parameters if \(\alpha\) is one real transverse parameter and \(m_0\) is one real ordinate. Thus the off-line zero equation does **not** necessarily overdetermine the center. It may define isolated centers or a constrained discrete set, but it does not automatically create a large codimension obstruction to source-flat recurrence.

The combined system is roughly:

\[
Z_\alpha(m_0)=0,
\]

and

\[
\Delta^r
\partial_m^r
\left(B_2+D_2+P_2\right)(m_0)
\approx0,
\qquad
0\le r\le R(Q).
\]

The source-flat conditions add about

\[
R(Q)+1
\]

real constraints, while the zero condition contributes two real constraints but also introduces the off-line parameter \(\alpha\).

So the effective codimension is still approximately

\[
K\approx R(Q)+O(1),
\]

not qualitatively larger.

---

# 3. Prime-log phase model

At the prime phase level, define

\[
\theta_p(m)=m\log p \pmod {2\pi}.
\]

Then the finite-prime phase vector is

\[
m\mapsto
\left(e^{-im\log p}\right)_{p\le X}.
\]

The finite-jet source-flat target is a tube in this torus:

\[
\mathcal T_{\mathrm{flat}}
=
\left\{
\theta:
\Delta^r
\partial_m^r
(B_2+D_2+P_2)(m)
\approx0,
\quad 0\le r\le R
\right\}.
\]

The off-line zero condition defines another target tube:

\[
\mathcal T_{\mathrm{zero}}
=
\{\theta: Z_\alpha(m)\approx0\}.
\]

The combined bad event is recurrence into

\[
\mathcal T_{\mathrm{bad}}
=
\mathcal T_{\mathrm{zero}}\cap \mathcal T_{\mathrm{flat}}.
\]

Because \(m\mapsto(m\log p)_{p\le X}\) is a one-parameter flow, generic recurrence into a codimension-\(K\) tube of radius \(\eta\) costs heuristically

\[
\eta^{-K}.
\]

If the required accuracy is polynomial,

\[
\eta=Q^{-C},
\]

and

\[
K\asymp R(Q)\asymp \frac{\log Q}{\log\log Q},
\]

then the recurrence cost is roughly

\[
Q^{C K}
=
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

This is large, but still far below \(e^Q\). Therefore scale alone does not rule out recurrence over high ordinates.

This is the same obstruction seen before: finite-jet flatness is a finite-codimension tube, not a full-dimensional impossibility.

---

# 4. Does the center condition help more than codimension suggests?

It might, but only if one proves a **compatibility theorem** showing that the prime phases required to form an off-line zero are incompatible with the prime phases required to flatten source curvature.

The available equation

\[
Z_\alpha(m_0)=0
\]

uses the same prime phases as \(P_2\), so in principle it could be powerful. But structurally, it is also just another finite set of oscillatory constraints. Without positivity, monotonicity, or a sign-definite energy identity, it does not give an immediate contradiction.

In AFE language, the off-line zero equation looks schematically like

\[
A_\alpha(m_0)+
\sum_{n\le X}
b_n(\alpha)n^{-1/2-\alpha-im_0}
+
\chi_\alpha(m_0)
\sum_{n\le X^\ast}
b_n^\ast(\alpha)n^{-1/2+\alpha+im_0}
+
\mathrm{err}
=0.
\]

The source-flat equations involve differentiated/log-weighted versions:

\[
\sum_{n\le X}
a_n(\log n)^r n^{-1/2-im_0}
\approx
\text{specified target},
\qquad
0\le r\le R.
\]

These are related but not obviously inconsistent. The zero equation fixes a weighted sum; the source-flat equations fix a finite number of different weighted sums. A Dirichlet polynomial with many phases can plausibly satisfy several such constraints unless fixed-coefficient arithmetic prevents it.

Thus the center condition is useful, but not presently proof-closing.

---

# 5. Codimension estimate for the combined target

Let:

\[
R=R(Q)\asymp \frac{\log Q}{\log\log Q}.
\]

The source-flat finite-jet equations contribute approximately

\[
R+1
\]

real conditions if one treats \(q''_{\can}\) as real-valued.

The off-line zero equation contributes two real equations:

\[
\Re Z_\alpha(m_0)=0,\qquad \Im Z_\alpha(m_0)=0.
\]

If \(\alpha\) is free, subtract one real degree of freedom. Thus the effective extra codimension is about one.

So:

\[
K_{\mathrm{bad}}
\approx
R+2
\quad\text{or}\quad
R+1
\]

depending on whether \(\alpha\) is fixed or variable.

The recurrence cost is therefore still

\[
Q^{C(R+O(1))}
=
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

This does not exceed natural height budgets in the problem. Therefore a pure dimension-counting or Kronecker-flow argument is insufficient.

---

# 6. What theorem would actually be needed?

A viable prime-side Gate 1 theorem would have to say something like:

\[
\boxed{
\textbf{Center-conditioned finite-jet source nonrecurrence.}
}
\]

For every admissible hypothetical off-line packet center \((\alpha,m_0)\) satisfying

\[
Z_\alpha(m_0)=0,
\]

and every corresponding interval

\[
I_\rho=[m_0-c/Q,m_0+c/Q],
\]

one has

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r
\partial_m^r
q''_{\can}(m_0)
\right|
\ge Q^{-B}.
\]

Equivalently,

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r
\partial_m^r
\left(B_2+D_2+P_2\right)(m_0)
\right|
\ge Q^{-B},
\]

with \(E_2\) absorbed.

This theorem must use the **actual fixed coefficients** and the **off-line center condition**. It cannot follow from generic large-sieve bounds or arbitrary Dirichlet-polynomial approximation results.

---

# 7. Possible ways to strengthen the center condition

The only promising route would be to extract more equations from the off-line packet hypothesis than just

\[
Z_\alpha(m_0)=0.
\]

Candidates:

## 7.1 Simplicity / multiplicity conditions

If one assumes a simple off-line zero, then

\[
Z_\alpha(m_0)=0,
\qquad
Z_\alpha'(m_0)\ne0.
\]

But nonvanishing is an open condition, not a coercive equation. It does not directly prevent source flatness.

## 7.2 Quartet symmetry

Functional equation gives the quartet:

\[
\rho,\quad 1-\rho,\quad \bar\rho,\quad 1-\bar\rho.
\]

This enforces symmetry of local zero packets but does not prevent same-scale cancellation; indeed, the zero-side quadrature model is already compatible with quartet symmetry.

## 7.3 AFE zero equation plus differentiated source equations

One might hope that the zero equation and source-flat equations overuse the same Dirichlet polynomial degrees of freedom. But the number of available prime phases up to \(X\) is large compared to \(R(Q)\), so finite-dimensional overdetermination is not obvious.

## 7.4 Sign or positivity from \(\chi\)/gamma terms

The gamma and dual terms contribute structured drift, but no sign-definite coercive form has been identified. They may shift the target tube; they do not obviously eliminate it.

Conclusion:

\[
\boxed{
\text{The center condition is not yet strong enough without a new fixed-coefficient theorem.}
}
\]

---

# 8. Relation to Gate 1 anti-quadrature

The prime/AFE theorem is the prime-side counterpart of the zero-side anti-quadrature theorem.

Zero side:

\[
\text{actual zeros cannot form same-scale finite-jet source-flattening quadrature.}
\]

Prime side:

\[
\text{actual fixed prime phases cannot recur into an off-line-zero/source-flat finite-jet tube.}
\]

These are not obviously different theorems; they are dual formulations of the same missing arithmetic obstruction.

Thus if the zero-side anti-quadrature theorem is proved, the prime-side theorem may follow by explicit formula. Conversely, a prime-side nonrecurrence theorem would imply the desired zero-side obstruction.

---

# 9. Final Agent 3 conclusion

The center-conditioned prime/AFE route is precise but still open.

\[
\boxed{
\text{Off-line center conditioning adds constraints, but does not by itself defeat recurrence.}
}
\]

The missing theorem is:

\[
\boxed{
\text{No simultaneous off-line-zero/source-flat finite-jet recurrence for actual zeta.}
}
\]

A useful formal target is:

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r
\partial_m^r
q''_{\can}(m_0)
\right|
\ge Q^{-B},
\]

for every admissible off-line packet center \(m_0\), with

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or \(O(\log Q)\).

At present, generic phase recurrence heuristics still make failure plausible in surrogates. The proof must use actual zeta fixed coefficients, not generic Dirichlet-polynomial technology.
## User (2026-04-26 14:02:08)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:02:21)

_Thought for 12s_

## Agent 3 / C — Prime/AFE off-line-center nonrecurrence

### Executive verdict

The prime/AFE route is now sharply formulated, but not closed. The off-line center condition

\[
Z_\alpha(m_0)=0
\]

does add structure, but it does **not** by itself defeat finite-jet source-flat recurrence. It contributes only finitely many constraints and mostly shifts the finite-jet target. The missing theorem is therefore:

\[
\boxed{
\text{No simultaneous off-line-zero/source-flat finite-jet recurrence for actual zeta coefficients.}
}
\]

This is the prime-side form of Gate 1, matching the shared strategic reduction to actual-zeta source-curvature observability. 

---

# 1. Prime/AFE setup

Work with the canonical representation

\[
q''_{\can}(m)
=
B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

where

\[
P_2(m)=\Re\sum_{n\le X}a_ne^{-im\log n}.
\]

The coefficients \(a_n\) are fixed by actual zeta/AFE data. They are not adjustable.

Let

\[
I_\rho=[m_0-\Delta,m_0+\Delta],
\qquad
\Delta\asymp Q^{-1}.
\]

If Gate 1 fails strongly, then \(q''_{\can}\) is small on \(I_\rho\). By Taylor expansion, this forces finite-jet cancellation at \(m_0\):

\[
\Delta^r
\partial_m^r
\left(B_2+D_2+P_2\right)(m_0)
\approx 0,
\qquad
0\le r\le R(Q),
\]

after absorbing \(E_2\), where

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or conservatively \(R(Q)=O(\log Q)\).

Since

\[
\partial_m^rP_2(m_0)
=
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_0\log n},
\]

the source-flat condition is a finite system of log-weighted phase equations.

---

# 2. Combined bad system

The center is not arbitrary. It belongs to a hypothetical off-line packet. Write the off-line zero condition abstractly as

\[
Z_\alpha(m_0)=0,
\]

where \(\alpha\) is the transverse displacement from the critical line. For example, morally,

\[
Z_\alpha(m_0)
=
\zeta\!\left(\frac12+\alpha+im_0\right)
\]

or its completed/scattering-normalized equivalent.

The combined bad system is:

\[
Z_\alpha(m_0)=0,
\]

and

\[
\Delta^r
\partial_m^r
\left(B_2+D_2+P_2\right)(m_0)
=
O(Q^{-B_r}),
\qquad
0\le r\le R(Q).
\]

In expanded prime-phase form, this is approximately:

\[
\sum_{n\le X}
b_n(\alpha)n^{-im_0}
+
\chi_\alpha(m_0)
\sum_{n\le X^\ast}
b_n^\ast(\alpha)n^{im_0}
+
\mathrm{background}
\approx 0,
\]

together with

\[
\Re\sum_{n\le X}
a_n(-i\log n)^r n^{-im_0}
\approx
-\partial_m^r(B_2+D_2)(m_0),
\qquad
0\le r\le R(Q).
\]

The same prime phases

\[
e^{-im_0\log p}
\]

drive both the off-line zero equation and the source-flat jet equations.

---

# 3. Effective codimension

The off-line equation

\[
Z_\alpha(m_0)=0
\]

is complex, so it gives two real equations:

\[
\Re Z_\alpha(m_0)=0,
\qquad
\Im Z_\alpha(m_0)=0.
\]

But \((\alpha,m_0)\) has two real degrees of freedom. Thus, at the most naive dimension-counting level, the off-line zero condition does not create a large codimension obstruction. It selects isolated or discrete candidate centers, but it does not by itself make source-flatness impossible.

The source-flat jet equations contribute approximately

\[
R(Q)+1
\]

real scalar constraints, because \(q''_{\can}\) is real-valued on the real \(m\)-axis.

Thus the combined target has effective codimension roughly

\[
K_{\mathrm{bad}}
\approx R(Q)+O(1),
\]

not a qualitatively larger codimension.

If \(\alpha\) is fixed in advance rather than free, the off-line equation contributes two additional real constraints, so

\[
K_{\mathrm{bad}}\approx R(Q)+2.
\]

But in the actual off-line-zero search, \(\alpha\) is usually a free transverse parameter, so the extra codimension is at most \(O(1)\).

---

# 4. Prime-log recurrence cost

Consider the finite-dimensional phase map

\[
m\mapsto
\left(e^{-im\log p}\right)_{p\le X}.
\]

The bad event is recurrence of this one-parameter flow into a small tube:

\[
\mathcal T_{\mathrm{bad}}
=
\mathcal T_{\mathrm{zero}}
\cap
\mathcal T_{\mathrm{flat}}.
\]

If each of \(K\) constraints must be satisfied to accuracy

\[
\eta=Q^{-C},
\]

then generic recurrence into such a tube costs about

\[
\eta^{-K}=Q^{CK}.
\]

With

\[
K\asymp R(Q)\asymp \frac{\log Q}{\log\log Q},
\]

this is

\[
Q^{C R(Q)}
=
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

That is large, but not impossibly large relative to the available height scale in high-\(T\) zeta dynamics. Therefore a recurrence heuristic does **not** rule out the bad system.

If one uses the more conservative

\[
R(Q)=O(\log Q),
\]

then the cost becomes

\[
\exp(O((\log Q)^2)).
\]

Still subexponential in \(Q\). Thus scale/codimension alone does not prove Gate 1.

---

# 5. Does the off-line center condition genuinely help?

It helps only if one proves a compatibility theorem. Structurally, the center condition does not currently produce a sign, positivity, monotonicity, or coercivity statement.

The zero equation controls a weighted Dirichlet polynomial value:

\[
\sum_{n\le X}b_n(\alpha)n^{-im_0}
+
\text{dual/background}
\approx 0.
\]

The source-flat equations control log-weighted derivatives:

\[
\sum_{n\le X}a_n(\log n)^r n^{-im_0}
\approx
\text{specified target},
\qquad 0\le r\le R.
\]

These are related, but not obviously inconsistent. A finite-dimensional phase vector with many prime phases can plausibly hit both a zero condition and several derivative conditions unless actual fixed coefficients impose hidden rigidity.

So the off-line condition currently does this:

\[
\boxed{
\text{It shifts/restricts the target tube, but does not eliminate it.}
}
\]

It does **not** currently do this:

\[
\boxed{
\text{It does not by itself prove source-curvature nonflatness.}
}
\]

---

# 6. What actual-zeta coefficient rigidity would be needed?

A successful theorem must exploit at least one of the following non-generic features:

## 6.1 Shared-coefficient incompatibility

Show that the coefficients appearing in the off-line zero AFE and the coefficients appearing in \(q''_{\can}\) finite jets cannot simultaneously satisfy:

\[
Z_\alpha(m_0)=0
\]

and

\[
\Delta^r\partial_m^r q''_{\can}(m_0)=O(Q^{-B}),
\qquad 0\le r\le R.
\]

This would be the cleanest direct theorem.

## 6.2 Positivity/coercivity identity

Construct a positive form such as

\[
\mathcal Q(m_0,\alpha)
\]

whose smallness is equivalent to source-flatness, but whose value is forced large by the off-line zero equation and the functional equation.

No such form is presently identified.

## 6.3 Overdetermined AFE compatibility

Use the zero equation and its \(\alpha\)-dependence to generate more constraints than the single complex equation. For example, if admissibility forced not just

\[
Z_\alpha(m_0)=0
\]

but also several differentiated or symmetry constraints, one might get a larger codimension system. But ordinary simple-zero admissibility gives nonvanishing derivative conditions, which are open inequalities, not equations.

## 6.4 Arithmetic nonrecurrence of prime phases

Prove that the actual prime-log flow cannot hit the combined target tube at off-line-zero centers:

\[
m_0\mapsto (m_0\log p)_{p\le X}
\]

has no recurrence into

\[
\mathcal T_{\mathrm{zero}}\cap\mathcal T_{\mathrm{flat}}
\]

at the required scale. This is far stronger than generic Diophantine recurrence and would need actual zeta arithmetic.

---

# 7. Formal missing theorem

A precise target is:

\[
\boxed{
\textbf{Center-conditioned source-curvature nonrecurrence.}
}
\]

For every admissible hypothetical off-line packet \((\alpha,m_0)\), with

\[
Z_\alpha(m_0)=0,
\]

and

\[
I_\rho=[m_0-\Delta,m_0+\Delta],
\qquad
\Delta\asymp Q^{-1},
\]

there exist constants \(B\) and \(R(Q)\), with

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or \(R(Q)=O(\log Q)\), such that

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r
\partial_m^r
q''_{\can}(m_0)
\right|
\ge Q^{-B}.
\]

Equivalently,

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r
\partial_m^r
\left(B_2+D_2+P_2\right)(m_0)
\right|
\ge Q^{-B},
\]

with \(E_2\) absorbed into the error budget.

This theorem would imply the finite-jet version of Gate 1.

---

# 8. Relation to the zero-side anti-quadrature theorem

The prime/AFE statement is the dual formulation of the zero-side anti-quadrature statement.

Zero-side version:

\[
\text{actual zeros cannot form same-scale finite-jet source-flattening quadrature.}
\]

Prime-side version:

\[
\text{actual fixed prime phases cannot realize off-line-zero/source-flat finite-jet recurrence.}
\]

Neither is currently easier on the evidence. The zero side is geometrically clear but lacks a known obstruction. The prime side has the Euler product, but generic recurrence still looks plausible without a new coefficient rigidity theorem.

---

# 9. Final conclusion

\[
\boxed{
\text{The prime/AFE route is precise but still conditional on a new arithmetic theorem.}
}
\]

The off-line center condition

\[
Z_\alpha(m_0)=0
\]

is essential to state the correct theorem, but it does not by itself close Gate 1. It adds only \(O(1)\) effective codimension once \(\alpha\) is free.

Thus the next prime-side work should not be generic large-sieve estimates. It should target the actual fixed-coefficient incompatibility:

\[
\boxed{
Z_\alpha(m_0)=0
\quad\text{and}\quad
\Delta^r\partial_m^r q''_{\can}(m_0)\approx0
\ (0\le r\le R)
\text{ cannot occur simultaneously for actual zeta.}
}
\]
## User (2026-04-26 14:06:02)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:06:03)

I’ll take the Agent 3 task: check whether a global explicit-formula/Weil-positive energy can prove Gate 1, or whether it collapses back to the same fixed-coefficient nonrecurrence problem.

_Thought for 8s_

## Agent 3 / C — Global trace / Weil-positive backup for Gate 1

### Verdict

A global trace/explicit-formula route is **plausible only as a major pivot**, not as a short backup proof of Gate 1.

For the local Gate 1 target

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|,
\]

a smoothed global energy

\[
\mathcal E_w(m_0)
=
\int_{\mathbb R} w(m-m_0)|q''_{\can}(m)|^2\,dm
\]

does produce natural zero-side and prime-side quadratic forms. But after expansion, the hard part is still to prevent localized destructive interference of the same-scale packet contributions. In other words, the trace formulation repackages Gate 1; it does not obviously bypass the same anti-quadrature / fixed-coefficient nonrecurrence problem identified in the latest shared brief. 

My final classification:

\[
\boxed{
\text{Global trace currently reduces to prime nonrecurrence unless one builds a new Weil-positive packet test.}
}
\]

A genuinely successful Weil-positive version would be RH-level technology, not a small local repair.

---

# 1. Smoothed Gate 1 energy

Let \(w\ge0\) be a smooth bump adapted to a window of width \(L\), with

\[
w_L(m-m_0)=w\!\left(\frac{m-m_0}{L}\right).
\]

Define

\[
\mathcal E_w(m_0)
=
\int_{\mathbb R}
w_L(m-m_0)
|q''_{\can}(m)|^2\,dm.
\]

The local Gate 1 estimate corresponds to

\[
L\asymp |I_\rho|\asymp Q^{-1}.
\]

A broader trace test would take

\[
L=Q^{-1}L_0(Q),
\]

where \(L_0(Q)\) is slowly growing.

---

# 2. Zero-side expansion

Suppose locally

\[
q''_{\can}(m)
=
B_2(m)+\sum_{\nu}K_{2,\nu}(m),
\]

where \(K_{2,\nu}\) is the second-curvature contribution of the zero or packet \(\nu\), and \(B_2\) collects background, gamma, tail regularization, and other smooth terms.

Then

\[
\mathcal E_w
=
\int w_L |B_2|^2
+
2\Re\sum_\nu \int w_L B_2 \overline{K_{2,\nu}}
+
\sum_{\mu,\nu}
\int w_L K_{2,\mu}\overline{K_{2,\nu}}.
\]

So the zero-side energy is a quadratic form

\[
\mathcal E_w
=
\langle a,\mathsf K_w a\rangle
+
\text{background cross terms},
\]

where \(a_\nu\) are packet weights and

\[
(\mathsf K_w)_{\mu\nu}
=
\int w_L(m-m_0)
K_{2,\mu}(m)\overline{K_{2,\nu}(m)}\,dm.
\]

Because \(w_L\ge0\), the full quadratic form in the **actual function**

\[
\sum_\nu a_\nu K_{2,\nu}
\]

is nonnegative. But this does not give a useful lower bound. A positive quadratic form can be nearly zero if the packet combination itself is nearly zero on the support of \(w_L\).

That is exactly the same-scale quadrature obstruction.

So zero-side trace positivity gives:

\[
\mathcal E_w\ge0,
\]

but Gate 1 needs:

\[
\mathcal E_w\ge Q^{-B}L.
\]

The missing step is a coercivity estimate:

\[
\left\|
B_2+\sum_\nu K_{2,\nu}
\right\|_{L^2(w_L)}^2
\ge Q^{-B}L.
\]

That is precisely anti-quadrature.

---

# 3. Prime/AFE-side expansion

On the prime/AFE side, write

\[
q''_{\can}(m)=B_2(m)+D_2(m)+P_2(m)+E_2(m),
\]

where

\[
P_2(m)=\Re\sum_{n\le X}a_ne^{-im\log n}.
\]

Ignoring \(E_2\) for readability and combining \(B_2+D_2\) into \(C_2\), the energy is

\[
\mathcal E_w
=
\int w_L |C_2+P_2|^2.
\]

The prime-prime term becomes

\[
\int w_L |P_2(m)|^2\,dm
=
\sum_{n,k\le X}
a_n\overline{a_k}
\widehat w_L(\log n-\log k)
e^{-im_0(\log n-\log k)}
\]

up to real-part bookkeeping.

Since

\[
\widehat w_L(\xi)=L\widehat w(L\xi),
\]

the window selects pairs with

\[
|\log n-\log k|\lesssim L^{-1}.
\]

If \(L\asymp Q^{-1}\), this admits many near-diagonal and off-diagonal pairs. The resulting bilinear Dirichlet-polynomial form is not sign-definite in any coefficient-independent way once the background cross term is included:

\[
2\Re\int w_L C_2\overline{P_2}.
\]

Even if the prime-prime term is positive, it controls \(\|P_2\|_2\), not \(\|C_2+P_2\|_2\). Source-flatness is exactly the possibility that

\[
P_2\approx -C_2
\]

on the window.

So the prime energy route again becomes:

\[
\boxed{
\text{fixed-coefficient non-approximation of }-C_2\text{ by }P_2\text{ on }I_\rho.
}
\]

That is the same prime/AFE Gate 1 theorem already identified.

---

# 4. Does broadening the window help?

Take

\[
L=Q^{-1}L_0(Q),
\qquad L_0(Q)\ge1.
\]

Broadening helps in one limited sense: source-flatness on a longer interval requires more finite-jet control. If

\[
q''_{\can}
\]

is analytic with polynomial derivative complexity, then keeping it small on a longer interval forces more Taylor coefficients to be small, roughly up to an order depending on \(L_0(Q)\).

But this does not remove the obstruction. It only changes the finite-jet recurrence target:

\[
\partial_m^r q''_{\can}(m_0)\approx0,
\qquad 0\le r\le R(Q,L_0).
\]

A broad window may make recurrence less likely, but unless \(L_0\) is so large that the test ceases to be local to \(I_\rho\), the proof still needs a fixed-coefficient nonrecurrence theorem.

If \(L_0\) is made very large, the test may become global enough to use classical mean-value estimates. But then it no longer proves the original local Gate 1 estimate on \(I_\rho\). It proves average nonflatness over a larger region, which still allows a narrow source-flat hole at the packet interval.

So:

\[
\boxed{
\text{Moderate broadening strengthens diagnostics but does not bypass Gate 1.}
}
\]

---

# 5. Beurling–Selberg / Weil-positive tests

A Weil-positive route would try to select a test function \(h\) or \(w\) such that the explicit formula gives a sign-definite expression detecting the off-line packet.

The dream statement would look like:

\[
\mathcal W_h(\text{zeros})
=
\text{positive contribution from off-line packet}
-
\text{controlled prime/background terms}
\ge Q^{-B}.
\]

But there are two problems.

First, Gate 1 is about

\[
|q''_{\can}|^2,
\]

which is quadratic in the zero/prime data. The classical explicit formula is linear. Squaring creates pair correlations of zeros or bilinear prime sums. A Weil-positive linear test does not directly give coercivity for the local squared curvature.

Second, the same-scale quadrature adversary can make the **local linear packet sum**

\[
q''_{\can}
\]

small. Any quadratic energy built from that same local sum is then small. To defeat this, the Weil test must detect not just the presence of packets, but their forbidden arrangement as an approximate design. That is a packet-adapted anti-design theorem, not ordinary Weil positivity.

A genuinely new test might exist, but it would need to prove something like:

\[
\text{actual zero packets cannot make the local curvature kernel vanish to finite order}
\]

using global positivity. That is essentially a new RH-level trace theorem.

---

# 6. Zero-side coercivity obstruction

The core obstruction can be stated abstractly.

Let

\[
\mathcal K_\nu(x)
\]

be normalized same-scale curvature kernels. Gate 1 asks for

\[
\left\|
\sum_{\nu\in\mathcal A}
a_\nu \mathcal K_\nu
+
\mathcal B
\right\|_{L^2(X)}^2
\ge Q^{-B}|X|.
\]

A positive energy only says the left side is nonnegative. To obtain the lower bound, one must show

\[
-\mathcal B
\]

is not approximable by the span/cone of the local packet kernels with actual-zeta coefficients and positions.

But finite positive quadrature says local geometry alone permits such approximation to high order. Therefore any coercivity must be arithmetic.

This is the same missing theorem as before.

---

# 7. Prime-side bilinear obstruction

On the prime side, the bilinear form

\[
\sum_{n,k}
a_n\overline{a_k}
\widehat w_L(\log n-\log k)
e^{-im_0\log(n/k)}
\]

is positive for \(\|P_2\|_{L^2(w)}^2\), but Gate 1 needs positivity for

\[
\|C_2+P_2\|_{L^2(w)}^2.
\]

The bad event is

\[
P_2\approx -C_2.
\]

So the needed theorem is a lower bound for the distance from a fixed target \( -C_2\) to the actual Dirichlet polynomial trajectory. That is a nonrecurrence/non-approximation statement, not a generic mean-square estimate.

---

# 8. Possible useful trace backup

A trace route may still be useful in two narrower ways.

## 8.1 Larger-window early warning

A broader energy

\[
\int_{|m-m_0|\le L}|q''_{\can}(m)|^2\,dm
\]

could show that source flatness cannot persist beyond some length. This might reduce the required finite-jet order or constrain the shape of a source-flat interval.

But it does not by itself give the \(Q^{-1}\)-scale lower bound.

## 8.2 Anti-design via global constraints

A packet-adapted trace theorem might prove that a same-scale quadrature design forces a compensating global imbalance in the explicit formula. This would be valuable, but it is a new global anti-quadrature theorem.

The target would be:

\[
\text{same-scale source-flat packet design}
\Rightarrow
\text{impossible prime-side trace imbalance}.
\]

This is plausible as a research direction, but not presently available.

---

# 9. Final classification

The global trace route has three possible statuses:

### Weak trace / standard explicit formula

\[
\boxed{
\text{Reduces to prime nonrecurrence.}
}
\]

It expands Gate 1 into a bilinear form but does not supply coercivity.

### Packet-adapted Weil-positive test

\[
\boxed{
\text{Potential major pivot.}
}
\]

Would need a new positivity theorem detecting same-scale source-flat designs. This is likely RH-level.

### Broad-window energy

\[
\boxed{
\text{Useful diagnostic, not a local Gate 1 proof.}
}
\]

May show flatness cannot persist too long, but does not exclude \(Q^{-1}\)-scale flattening.

---

# 10. Agent 3 conclusion

\[
\boxed{
\text{Global trace does not currently bypass Gate 1.}
}
\]

It either:

\[
\boxed{
\text{repackages Gate 1 as fixed-coefficient prime nonrecurrence,}
}
\]

or requires:

\[
\boxed{
\text{a new packet-adapted Weil-positive anti-design theorem.}
}
\]

Therefore, the best use of the global trace branch is as a **backup pivot**, not the main line. The main line remains the direct Gate 1 arithmetic theorem:

\[
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
\]
## User (2026-04-26 14:10:28)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:10:30)

I’ll test the relaxed prime-phase model first. The key diagnostic is whether the bad equations are overdetermined before the one-parameter recurrence restriction is restored.

_Thought for 13s_

## Agent 3 / C — Prime/AFE nonrecurrence: finite-dimensional model test

### Verdict

In the phase-relaxed model, the bad system is **strongly underdetermined**. The Jacobian is generically full rank, but that does **not** help prove Gate 1; it means the simultaneous off-line-zero/source-flat system typically has a positive-dimensional solution set once the prime phases are allowed to vary independently.

When the one-parameter flow

\[
m\mapsto (e^{-im\log p})_{p\le X}
\]

is restored, hitting the bad tube has a recurrence cost roughly

\[
\exp\!\left(O(R\log Q)\right),
\]

which is subexponential in \(Q\) for

\[
R\asymp \frac{\log Q}{\log\log Q}
\]

and still only

\[
\exp(O((\log Q)^2))
\]

for \(R=O(\log Q)\). So generic recurrence remains plausible. Gate 1 therefore needs actual zeta coefficient rigidity, not just dimension counting. This matches the current shared target: actual zeta must forbid same-scale finite-jet flattening of \(q''_{\can}\). 

---

# 1. Phase-relaxed variables

Let

\[
\mathcal P_X=\{p\le X\},
\qquad
N=\pi(X).
\]

Introduce independent prime phases

\[
z_p=e^{-i\theta_p}\in S^1,
\qquad p\le X.
\]

For each integer \(n\le X\), write

\[
n=\prod_{p\le X}p^{v_p(n)},
\qquad
z^n:=\prod_{p\le X}z_p^{v_p(n)}.
\]

Then a Dirichlet polynomial term becomes

\[
n^{-im}=\prod_{p\le X}e^{-imv_p(n)\log p}
\leadsto
z^n.
\]

In the relaxed model,

\[
P_2(z)=\Re\sum_{n\le X}a_n z^n.
\]

The \(r\)-th source jet becomes

\[
\mathcal S_r(z)
=
\Delta^r\Re
\sum_{n\le X}
a_n(-i\log n)^r z^n
+
\Delta^r\partial_m^r(B_2+D_2)(m_0).
\]

The bad source-flat conditions are

\[
\mathcal S_r(z)\approx0,
\qquad
0\le r\le R.
\]

The off-line zero condition becomes a complex equation

\[
Z_\alpha(z)=0,
\]

where schematically

\[
Z_\alpha(z)
=
A_\alpha+
\sum_{n\le X}b_n(\alpha)z^n
+
\chi_\alpha
\sum_{n\le X^\ast}b_n^\ast(\alpha)\bar z^n
+
\text{error}.
\]

This contributes two real equations:

\[
\Re Z_\alpha(z)=0,
\qquad
\Im Z_\alpha(z)=0.
\]

---

# 2. Equation count

The relaxed unknowns are:

\[
\theta_p\in\mathbb R/2\pi\mathbb Z,
\qquad p\le X,
\]

and possibly the transverse parameter

\[
\alpha.
\]

So the real variable count is either:

\[
N
\]

if \(\alpha\) is fixed, or

\[
N+1
\]

if \(\alpha\) is free.

The constraints are:

\[
R+1
\]

real source-flat equations, plus two real zero equations. Therefore

\[
K=R+3
\]

real constraints.

If \(\alpha\) is free, the expected dimension is

\[
N+1-(R+3)=N-R-2.
\]

If \(\alpha\) is fixed, the expected dimension is

\[
N-(R+3).
\]

Since

\[
N=\pi(X)
\]

is enormous compared with

\[
R\asymp\frac{\log Q}{\log\log Q}
\quad\text{or}\quad
R=O(\log Q),
\]

the relaxed bad set is expected to have large positive dimension.

Thus the relaxed system is not overdetermined.

---

# 3. Jacobian rank

Let \(\theta=(\theta_p)_{p\le X}\). For any Dirichlet monomial

\[
z^n=e^{-i\sum_p v_p(n)\theta_p},
\]

we have

\[
\frac{\partial z^n}{\partial \theta_p}
=
-i v_p(n)z^n.
\]

Therefore

\[
\frac{\partial \mathcal S_r}{\partial \theta_p}
=
\Delta^r
\Re
\sum_{n\le X}
a_n(-i\log n)^r(-iv_p(n))z^n.
\]

In the prime-only toy truncation

\[
P_2(z)\approx \Re\sum_{p\le X}A_p z_p,
\]

this reduces to rows of the form

\[
\frac{\partial \mathcal S_r}{\partial \theta_p}
\approx
\Delta^r(\log p)^r
\Re(-i A_p z_p).
\]

So the source-jet Jacobian resembles a weighted Vandermonde system in the values

\[
\log p.
\]

For generic phases and nonzero coefficients \(A_p\), the rows

\[
r=0,\ldots,R
\]

have rank \(R+1\), provided at least \(R+1\) useful primes contribute.

The zero equation adds two rows corresponding to

\[
\nabla_\theta \Re Z_\alpha,
\qquad
\nabla_\theta \Im Z_\alpha.
\]

Generically these are independent of the log-weighted source-jet rows unless the zero-equation coefficients \(b_n(\alpha)\) lie in the span of

\[
a_n(\log n)^r,
\qquad 0\le r\le R.
\]

No such coefficient identity is apparent. Thus the expected Jacobian rank is

\[
\operatorname{rank}J=R+3
\]

for fixed \(\alpha\), and still full constraint rank with \(\alpha\) free.

But full rank here means the bad set is a smooth submanifold of codimension \(R+3\), not that it is empty.

---

# 4. Consequence: relaxed system has many solutions

Assuming generic rank, the relaxed solution set has dimension

\[
N-R-3
\]

for fixed \(\alpha\), or

\[
N-R-2
\]

for free \(\alpha\).

Since

\[
N\gg R,
\]

the phase-relaxed model should contain many solutions to

\[
Z_\alpha(z)=0,
\]

and

\[
\mathcal S_r(z)=0,
\qquad 0\le r\le R.
\]

This is the main negative conclusion: coefficient transversality, by itself, does not make the system inconsistent. It merely makes the bad set a smooth lower-dimensional target.

The source-flat bad set is small, but not empty.

---

# 5. Restoring the one-parameter flow

The actual phases are not independent. They lie on the one-parameter orbit

\[
\theta_p(m)=m\log p \pmod{2\pi}.
\]

So the true question is whether this one-dimensional flow hits the bad target tube

\[
\mathcal T_{\bad}
=
\{z: Z_\alpha(z)\approx0,\ \mathcal S_0(z)\approx\cdots\approx \mathcal S_R(z)\approx0\}.
\]

If the target tube has codimension

\[
K\approx R+3
\]

and accuracy

\[
\eta=Q^{-C},
\]

then its expected measure is roughly

\[
\eta^K=Q^{-CK}.
\]

A generic equidistributed flow would hit it after time roughly

\[
\eta^{-K}=Q^{CK}.
\]

For

\[
R\asymp \frac{\log Q}{\log\log Q},
\]

this is

\[
Q^{C R}
=
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

For

\[
R=O(\log Q),
\]

this is

\[
\exp(O((\log Q)^2)).
\]

Both are large, but still not prohibitive in a high-height zeta problem. Thus generic recurrence does not disprove Gate 1, but it makes Gate 1 nontrivial: one needs actual arithmetic rigidity beyond generic torus dynamics.

---

# 6. Does the off-line center condition help?

In the phase-relaxed count, the off-line condition contributes two real constraints:

\[
\Re Z_\alpha=0,
\qquad
\Im Z_\alpha=0.
\]

But because \(\alpha\) is free, it effectively adds only about one net constraint to the recurrence problem. If \(\alpha\) is fixed, it adds two.

Either way, this is only \(O(1)\) compared with the \(R+1\) source-flat equations.

Therefore the off-line center condition does not fundamentally change the recurrence scale. It restricts the target tube, but does not make it empty.

It could help only if the coefficient structure of \(Z_\alpha\) is incompatible with the source-jet coefficient structure. That would be a genuine fixed-coefficient theorem, not a dimension-counting fact.

---

# 7. Phase-relaxed countermodel

The relaxed model provides a conceptual counterexample to any proof based only on equation count or generic transversality.

Take \(N\) independent phases with

\[
N\ge R+4.
\]

Assume the Jacobian of

\[
(\Re Z_\alpha,\Im Z_\alpha,\mathcal S_0,\ldots,\mathcal S_R)
\]

has full rank \(R+3\) at some approximate solution. Then by the implicit function theorem, the solution set has positive dimension.

Even if exact solvability requires adjusting background targets, the underdetermined structure shows there is no algebraic obstruction at the level of relaxed phases.

So any successful theorem must use one of:

1. the one-parameter nature of \(m\mapsto(e^{-im\log p})\);
2. the exact arithmetic of \(\log p\);
3. the actual zeta coefficients \(a_n,b_n(\alpha)\);
4. an explicit-formula positivity/global trace input;
5. a zero-side anti-design theorem.

Generic finite-dimensional transversality is insufficient.

---

# 8. What rigidity would be needed?

The missing theorem must say that the actual one-parameter orbit avoids the bad tube at polynomial scale:

\[
m\mapsto (e^{-im\log p})_{p\le X}
\notin
\mathcal T_{\bad}(Q^{-C})
\]

for every admissible off-line center.

A useful formulation is:

\[
\boxed{
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r q''_{\can}(m_0)
\right|
\ge Q^{-B}
}
\]

whenever

\[
Z_\alpha(m_0)=0.
\]

This is not a generic transversality theorem. It is a fixed-coefficient, center-conditioned nonrecurrence theorem.

---

# 9. Final conclusion

\[
\boxed{
\text{The finite-dimensional phase-relaxed system is underdetermined and generically solvable.}
}
\]

\[
\boxed{
\text{Restoring the one-parameter prime-log flow makes the event rare but not implausible.}
}
\]

\[
\boxed{
\text{Gate 1 therefore requires genuine actual-zeta arithmetic rigidity.}
}
\]

The current prime/AFE line should focus on proving nonrecurrence of the actual orbit into the off-line-zero/source-flat tube. Generic coefficient transversality or equation counting will not suffice.
## User (2026-04-26 14:16:15)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:16:17)

I’ll run the phase-relaxed countermodel again at the more explicit Gate 1 level: independent prime phases first, then restore the one-parameter orbit and estimate recurrence.

_Thought for a few seconds_

## Agent 3 / C — Finite-dimensional phase-relaxed countermodel

### Verdict

The phase-relaxed model strongly suggests that Gate 1 cannot be proved by equation counting, generic transversality, or finite-dimensional coefficient independence alone.

If the prime phases

\[
z_p=e^{-im_0\log p}
\]

are allowed to vary independently on a torus, the combined system

\[
Z_\alpha(z)=0,
\qquad
\mathcal S_r(z)=0,\quad 0\le r\le R
\]

is heavily underdetermined. The Jacobian is generically full rank, but full rank means the bad set is a smooth positive-dimensional submanifold, not empty. Restoring the one-parameter orbit makes the bad event rare, but not implausible at the scale required. This reinforces the current strategic conclusion: Gate 1 needs actual-zeta arithmetic rigidity, not generic phase geometry. 

---

# 1. Phase-relaxed model

Let

\[
\mathcal P_X=\{p\le X\},\qquad N=\pi(X),
\]

and introduce independent phase variables

\[
z_p\in S^1,\qquad p\le X.
\]

For

\[
n=\prod_{p\le X}p^{v_p(n)},
\]

write

\[
z^n=\prod_{p\le X} z_p^{v_p(n)}.
\]

The prime/AFE source term becomes

\[
P_2(z)
=
\Re\sum_{n\le X}a_n z^n.
\]

The scaled source-flat jet equations are

\[
\mathcal S_r(z)
=
\Delta^r
\Re\sum_{n\le X}
a_n(-i\log n)^r z^n
+
\Delta^r\partial_m^r(B_2+D_2)(m_0)
=
0,
\qquad
0\le r\le R.
\]

The off-line center equation becomes

\[
Z_\alpha(z)=0,
\]

a complex equation, hence two real equations.

So the relaxed bad system is

\[
\Re Z_\alpha(z)=0,
\]

\[
\Im Z_\alpha(z)=0,
\]

\[
\mathcal S_0(z)=\cdots=\mathcal S_R(z)=0.
\]

---

# 2. Variables versus constraints

The real variable count is

\[
N=\pi(X)
\]

if \(\alpha\) is fixed, and

\[
N+1
\]

if \(\alpha\) is allowed to vary as a transverse off-line parameter.

The real constraint count is

\[
(R+1)+2=R+3.
\]

Thus the expected dimension of the relaxed bad set is:

\[
N-(R+3)
\]

for fixed \(\alpha\), and

\[
N+1-(R+3)=N-R-2
\]

for free \(\alpha\).

Since \(N=\pi(X)\) is vastly larger than

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or even

\[
R(Q)=O(\log Q),
\]

the relaxed bad system is not overdetermined.

Unless \(X\) is absurdly tiny, the relaxed torus has more than enough degrees of freedom to satisfy the zero equation and all source-flat jet equations.

---

# 3. Generic Jacobian rank

Use angular coordinates

\[
z_p=e^{-i\theta_p}.
\]

For a monomial

\[
z^n=e^{-i\sum_p v_p(n)\theta_p},
\]

we have

\[
\frac{\partial z^n}{\partial \theta_p}
=
-i\,v_p(n)z^n.
\]

Therefore,

\[
\frac{\partial \mathcal S_r}{\partial \theta_p}
=
\Delta^r
\Re\sum_{n\le X}
a_n(-i\log n)^r(-iv_p(n))z^n.
\]

In a prime-only toy truncation,

\[
P_2(z)\approx \Re\sum_{p\le X}A_p z_p,
\]

this becomes

\[
\frac{\partial \mathcal S_r}{\partial \theta_p}
\approx
\Delta^r(\log p)^r
\Re(-iA_p z_p).
\]

The rows indexed by \(r=0,\ldots,R\) resemble a weighted Vandermonde system in

\[
\log p.
\]

For generic phases and nonzero coefficients, those rows have rank \(R+1\) as soon as at least \(R+1\) primes contribute effectively.

The two rows coming from

\[
\Re Z_\alpha,\quad \Im Z_\alpha
\]

are generically independent of the source-jet rows, unless the zero-equation coefficient vector happens to lie in the span of the log-weighted source vectors

\[
a_n(\log n)^r,\qquad 0\le r\le R.
\]

No such structural dependence is visible.

Thus one expects

\[
\operatorname{rank}J=R+3
\]

generically. But since the ambient dimension is \(N\gg R+3\), generic full rank implies a smooth solution set of positive dimension, not emptiness.

---

# 4. Phase-relaxed conclusion

The relaxed system should generically have many solutions. Its expected dimension is

\[
N-R-3
\]

or

\[
N-R-2
\]

if \(\alpha\) is free.

Therefore, any argument of the following form fails:

\[
\text{“There are many source-flat equations, so the bad system is impossible.”}
\]

It is not impossible in the phase-relaxed model. The system is underdetermined.

This gives a useful countermodel to naive coefficient-transversality arguments: transversality makes the bad set thin, but it does not remove it.

---

# 5. Restoring the one-parameter prime-log flow

Actual zeta does not allow independent phases. The phases lie on the one-parameter orbit

\[
m\mapsto
\left(e^{-im\log p}\right)_{p\le X}.
\]

Let

\[
\mathcal T_{\bad}(\eta)
\]

be an \(\eta\)-tube around the relaxed bad set, with

\[
\eta=Q^{-C}.
\]

If the bad set has codimension

\[
K=R+3
\]

in the \(N\)-torus, then the tube volume is heuristically

\[
\operatorname{vol}\mathcal T_{\bad}(\eta)
\asymp \eta^K
=
Q^{-C(R+3)}.
\]

A generic equidistributed one-parameter orbit would hit such a tube after time about

\[
Q^{C(R+3)}.
\]

For

\[
R\asymp\frac{\log Q}{\log\log Q},
\]

this gives recurrence time

\[
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

For the conservative choice

\[
R=O(\log Q),
\]

it gives

\[
\exp(O((\log Q)^2)).
\]

These recurrence times are large, but not large enough to exclude occurrences at high zeta heights. They are subexponential in \(Q\). Thus the one-parameter restriction makes the bad event rare, but not generically impossible.

---

# 6. Role of the off-line parameter \(\alpha\)

If \(\alpha\) is fixed, the zero condition adds two real constraints.

If \(\alpha\) is free, the variable count increases by one, so the net codimension contribution of the off-line zero equation is roughly one.

Either way, the off-line center condition changes the bad-tube codimension only by

\[
O(1).
\]

The dominant codimension remains the source-flat jet count

\[
R+1.
\]

Therefore the center condition is important for the exact theorem, but it does not change the recurrence heuristic enough to prove Gate 1.

---

# 7. What actual-zeta arithmetic would need to add

To defeat the phase-relaxed countermodel, one needs a theorem that uses something not present in the relaxed model.

Possible forms:

## 7.1 One-parameter orbit nonrecurrence

Show that the actual orbit

\[
m\mapsto(e^{-im\log p})_{p\le X}
\]

does not enter the bad tube near any admissible off-line zero center:

\[
Z_\alpha(m)=0
\quad\Longrightarrow\quad
\max_{0\le r\le R}
|\Delta^r\partial_m^r q''_{\can}(m)|
\ge Q^{-B}.
\]

This is the cleanest prime-side Gate 1 theorem.

## 7.2 Fixed-coefficient incompatibility

Show that the coefficient vectors in the zero equation and source-jet equations have a hidden arithmetic incompatibility, not visible from generic rank:

\[
Z_\alpha(m_0)=0
\]

cannot coexist with

\[
\Delta^r\partial_m^r(B_2+D_2+P_2)(m_0)\approx0,
\qquad 0\le r\le R.
\]

This would be stronger than transversality: it would be a forbidden-intersection theorem for the actual zeta coefficients.

## 7.3 Global trace obstruction

Show that if the orbit enters the bad tube, an explicit-formula or trace identity produces a global contradiction. This is effectively the global trace/Weil pivot.

---

# 8. Final verdict

\[
\boxed{
\text{The phase-relaxed model predicts that source-flat recurrences are plausible.}
}
\]

More precisely:

\[
\boxed{
\text{The relaxed bad system has positive-dimensional solution sets.}
}
\]

\[
\boxed{
\text{The one-parameter flow makes hitting rare, but not implausible.}
}
\]

\[
\boxed{
\text{Gate 1 needs actual-zeta rigidity beyond generic transversality.}
}
\]

So the prime/AFE line should not spend effort on generic dimension counting. It must prove a genuinely arithmetic nonrecurrence theorem for the actual prime-log orbit at admissible off-line centers.
## User (2026-04-26 14:20:35)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:20:41)

I’ll take the Agent 3 role and look for countermodels rather than another proof attempt: fixed-prime, AFE-like, and progressively constrained surrogates that can produce source-flat intervals.

_Thought for 10s_

## Agent 3 / C — Gate 1 countermodel search in realistic surrogates

### Verdict

Gate 1 remains **unproven and plausibly false in realistic surrogates**, but I do **not** have evidence that it is false for actual zeta.

The important distinction is:

\[
\boxed{
\text{phase-relaxed and fixed-prime/AFE-like surrogates can plausibly source-flatten;}
}
\]

but

\[
\boxed{
\text{actual zeta may still forbid this through arithmetic compatibility not present in the surrogates.}
}
\]

So the countermodel search strengthens the current diagnosis: Gate 1 needs actual-zeta arithmetic, not generic Dirichlet-polynomial or local packet arguments. This is exactly the Agent 3 assignment in the latest coordinator instruction. 

---

# 1. Surrogate class

Use a canonical prime/AFE-type source curvature model

\[
F(m)=B_2(m)+D_2(m)+P_2(m),
\]

with

\[
P_2(m)=\Re\sum_{n\le X}a_n e^{-im\log n}.
\]

For actual-like amplitudes one should take

\[
a_n\sim b_n(\log n)^2n^{-1/2}W(n/T),
\]

where \(W\) is a smooth AFE cutoff and \(b_n\) is fixed by the zeta/AFE normalization.

Gate 1 failure on

\[
I=[m_0-\Delta,m_0+\Delta],
\qquad
\Delta\asymp Q^{-1},
\]

is modeled by finite-jet suppression:

\[
\Delta^rF^{(r)}(m_0)\approx0,
\qquad
0\le r\le R.
\]

Since

\[
F^{(r)}(m_0)
=
\partial_m^r(B_2+D_2)(m_0)
+
\Re\sum_{n\le X}a_n(-i\log n)^r e^{-im_0\log n},
\]

this is a finite set of oscillatory cancellation conditions.

---

# 2. Phase-relaxed surrogate: countermodels are abundant

First allow the phases

\[
z_p=e^{-im_0\log p}
\]

to vary independently on the torus. Then the system

\[
\Delta^rF^{(r)}(m_0)=0,
\qquad 0\le r\le R,
\]

is \(R+1\) real equations in

\[
N=\pi(X)
\]

phase variables, with \(N\gg R\).

Even after adding an off-line center equation

\[
Z_\alpha(z)=0,
\]

which contributes two real equations but also often introduces the free transverse parameter \(\alpha\), the relaxed system remains underdetermined.

Expected relaxed dimension:

\[
N-(R+3)
\]

for fixed \(\alpha\), or

\[
N-R-2
\]

with \(\alpha\) free.

Thus phase-relaxed countermodels are not exceptional. They are expected.

Conclusion:

\[
\boxed{
\text{Any proof based only on finite-dimensional transversality fails.}
}
\]

---

# 3. One-parameter fixed-prime surrogate

Now restore the actual one-parameter orbit

\[
m\mapsto (e^{-im\log p})_{p\le X}.
\]

The bad set has approximate codimension

\[
K\approx R+O(1).
\]

If the target accuracy is

\[
\eta=Q^{-C},
\]

then a generic equidistributed orbit hits the bad tube after time roughly

\[
\eta^{-K}=Q^{CK}.
\]

For

\[
R\asymp \frac{\log Q}{\log\log Q},
\]

this is

\[
\exp\!\left(
O\!\left(\frac{(\log Q)^2}{\log\log Q}\right)
\right).
\]

For the conservative choice

\[
R=O(\log Q),
\]

this is

\[
\exp(O((\log Q)^2)).
\]

That cost is large, but not prohibitive on zeta-height scales. So fixed-prime recurrence remains plausible.

Conclusion:

\[
\boxed{
\text{The one-parameter restriction makes source-flatness rare, not impossible.}
}
\]

---

# 4. Adding AFE structure

Add:

\[
D_2(m),
\]

the \(\chi\)-factor derivatives, and gamma/background terms.

These terms change the target from

\[
P_2^{(r)}(m_0)\approx0
\]

to

\[
P_2^{(r)}(m_0)\approx
-\partial_m^r(B_2+D_2)(m_0).
\]

That is important numerically, but structurally it is still a finite target tube in the same prime-phase torus.

The dual term does not obviously introduce positivity or coercivity. It adds more fixed oscillatory structure, but unless one proves an incompatibility theorem, it merely shifts or bends the target.

Conclusion:

\[
\boxed{
\text{AFE completion does not by itself remove the surrogate countermodels.}
}
\]

---

# 5. Adding the off-line center condition

The off-line packet condition is

\[
Z_\alpha(m_0)=0.
\]

In AFE form this is another fixed-coefficient Dirichlet-polynomial equation using the same prime phases:

\[
A_\alpha(m_0)+
\sum_{n\le X}b_n(\alpha)n^{-im_0}
+
\chi_\alpha(m_0)
\sum_{n\le X^\ast}b_n^\ast(\alpha)n^{im_0}
\approx0.
\]

This adds a serious compatibility condition, but only finitely many equations. With \(\alpha\) free, its net codimension cost is small.

So the combined bad system remains:

\[
Z_\alpha(m_0)=0,
\]

\[
\Delta^rF^{(r)}(m_0)\approx0,
\qquad 0\le r\le R.
\]

This is rare but still plausible in generic prime-phase models.

Conclusion:

\[
\boxed{
\text{The off-line center condition is necessary for the theorem, but not sufficient to prove it.}
}
\]

---

# 6. Zero-side quartet constraints

On the zero side, quartet symmetry is already compatible with the same-scale quadrature construction.

The normalized kernel identity

\[
K_\theta^{(n)}(0)=n!\sin((n+1)\theta)
\]

turns source flattening into moment equations

\[
\sum_j w_j\sin(k\theta_j)\approx0.
\]

Positive finite quadrature can solve these with

\[
O(R)
\]

nodes.

Quartet closure changes constants and enforces symmetry, but it does not prevent the design. It often helps by naturally symmetrizing odd/even moment conditions.

Conclusion:

\[
\boxed{
\text{Quartet symmetry does not eliminate the source-flat countermodel.}
}
\]

---

# 7. Mechanism of source-flat intervals in surrogates

The mechanism is finite-codimension recurrence into a jet-flat tube.

In prime language:

\[
\Re\sum a_n(-i\log n)^r e^{-im_0\log n}
\]

simultaneously matches prescribed targets for \(0\le r\le R\).

In zero language:

\[
\sum_j w_jK_{\theta_j}^{(r+2)}(x_0)
\]

simultaneously cancels for \(0\le r\le R\).

These are the same phenomenon viewed through the explicit formula.

The common structure is:

\[
\boxed{
\text{many oscillatory degrees of freedom, finitely many jet constraints.}
}
\]

That is why surrogates can source-flatten.

---

# 8. What would make the surrogate more realistic?

A serious numerical countermodel should add constraints in this order:

1. **Fixed amplitudes**  
   Use actual-like \(a_n\), not adjustable coefficients.

2. **Actual logarithms**  
   Use \(e^{-im\log n}\), not independent phases.

3. **AFE dual term**  
   Include \(D_2\) and \(\chi\)-derivatives.

4. **Gamma/background**  
   Include \(B_2\).

5. **Off-line center equation**  
   Enforce \(Z_\alpha(m_0)=0\) or a proxy.

6. **Zero-side quartet symmetry**  
   If working with packet models, enforce quartet closure.

7. **Same-scale packet restrictions**  
   Enforce \(x_j^2+c_j^2=d^2\) or the singular rescaled analogue.

If source-flat intervals persist after steps 1–5, Gate 1 becomes numerically threatened. If they disappear only after step 5, the center-conditioned arithmetic is likely the key.

---

# 9. Concrete computational search objective

For fixed \(Q,\Delta,R\), define

\[
\mathcal J(m_0,\alpha)
=
|Z_\alpha(m_0)|^2
+
\sum_{r=0}^{R}
\left|
\Delta^r
\partial_m^rF(m_0)
\right|^2.
\]

Search for small values of \(\mathcal J\).

A source-flat candidate is serious if:

\[
|Z_\alpha(m_0)|\le Q^{-C},
\]

and

\[
\max_{0\le r\le R}
\left|
\Delta^r
\partial_m^rF(m_0)
\right|
\le Q^{-C}.
\]

Then verify directly on the interval:

\[
E_I
=
|I|^{-1}
\int_I |F(m)|^2\,dm
\ll Q^{-B}.
\]

The key diagnostic is interval smallness, not just pointwise jet coincidence.

---

# 10. Verdict by surrogate level

| Model | Source-flat intervals? | Interpretation |
|---|---:|---|
| Arbitrary same-scale packets | Yes | Local geometry insufficient |
| Positive finite quadrature | Yes | Strong zero-side no-go |
| Phase-relaxed prime model | Yes, generically | Transversality insufficient |
| One-parameter fixed-prime model | Plausible | Recurrence rare but possible |
| AFE with dual/gamma | Unknown; likely still plausible absent theorem | Needs testing |
| AFE + off-line center equation | Unknown | This is the real Gate 1 theorem |
| Actual zeta | Unknown | Decisive open point |

---

# 11. Final conclusion

\[
\boxed{
\text{Gate 1 is likely true or false only for genuinely arithmetic reasons.}
}
\]

Surrogates strongly suggest that source-flat intervals are plausible unless the actual zeta coefficients and the off-line zero condition impose hidden rigidity.

So my verdict is:

\[
\boxed{
\text{Gate 1 is undecidable from current surrogate analysis, but realistic surrogates threaten it enough that numerical testing is urgent.}
}
\]

The exact mechanism to watch for is:

\[
\boxed{
\text{finite-jet source-flat recurrence of the actual prime-log orbit, possibly conditioned on }Z_\alpha(m_0)=0.
}
\]
## User (2026-04-26 14:24:32)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:24:37)

I’ll sharpen the prime/AFE theorem statement rather than re-argue recurrence. The output will be a precise target theorem, the bad tube, error requirements, and candidate proof tools.

_Thought for 5s_

## Agent 3 / C — Prime/AFE nonrecurrence: sharpened Gate 1 theorem

### Verdict

The prime/AFE Gate 1 theorem should be stated as a **center-conditioned finite-jet nonrecurrence theorem** for the actual one-parameter prime-log orbit. The theorem must not be phrased as generic Dirichlet-polynomial non-approximation, because phase-relaxed and fixed-prime surrogates remain too flexible. The theorem must use the actual zeta coefficients, AFE dual structure, and the off-line center condition simultaneously. This is the Agent 3 task in the latest instruction. 

---

# 1. Precise theorem target

Let

\[
I_\rho=[m_0-\Delta,m_0+\Delta],
\qquad
\Delta=c_IQ^{-1},
\]

where \(I_\rho\) is the admissible packet interval attached to a hypothetical off-line packet. Let

\[
q''_{\can}(m)=B_2(m)+P_2(m)+D_2(m)+E_2(m),
\]

with

\[
P_2(m)=\Re\sum_{n\le X}a_n e^{-im\log n}.
\]

The off-line center condition is

\[
Z_\alpha(m_0)=0,
\]

where \(\alpha\) is the transverse off-critical parameter.

The theorem should be:

\[
\boxed{
Z_\alpha(m_0)=0
\quad\Longrightarrow\quad
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r q''_{\can}(m_0)
\right|
\ge Q^{-B}.
}
\]

A stronger interval form is:

\[
\boxed{
\int_{m_0-\Delta}^{m_0+\Delta}
|q''_{\can}(m)|^2\,dm
\ge Q^{-B}\Delta.
}
\]

The finite-jet theorem implies the interval theorem under the existing analytic-complexity package, provided \(R(Q)\) is high enough.

---

# 2. Parameter choices

The natural choices are:

\[
\Delta=c_IQ^{-1},
\]

and either

\[
R(Q)\asymp \frac{\log Q}{\log\log Q},
\]

or the more conservative

\[
R(Q)=C_R\log Q.
\]

The first is the minimal analytic-continuation/Taylor-control scale suggested by prior audits. The second is safer for numerics and for crude Cauchy/Remez bounds.

The theorem should explicitly state that \(B\), \(C_R\), and \(c_I\) are fixed constants independent of \(m_0,Q,T\), except through the admissible patch constants.

---

# 3. Error absorption for \(E_2\)

The finite-jet theorem should be formulated for the main computable object

\[
F_2(m):=B_2(m)+P_2(m)+D_2(m),
\]

with an error hypothesis:

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r E_2(m_0)
\right|
\le \frac12 Q^{-B}.
\]

Then it is enough to prove

\[
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r F_2(m_0)
\right|
\ge 2Q^{-B}.
\]

If \(E_2\) is only polynomially bounded, not small, then it cannot be ignored for Gate 1. Polynomial boundedness suffices for Gate 2 derivative complexity, but **Gate 1 needs \(E_2\) small enough to absorb**, because Gate 1 is a lower-bound theorem.

Thus the AFE theorem requires a differentiated error bound through order \(R(Q)\), or the AFE representation must be replaced by an exact zero-side regularized formula.

---

# 4. Coefficient vectors

For the source jets,

\[
\partial_m^rP_2(m_0)
=
\Re\sum_{n\le X}
a_n(-i\log n)^r e^{-im_0\log n}.
\]

Thus the \(r\)-th source-jet coefficient vector is

\[
v_r(n):=a_n(-i\log n)^r.
\]

After scaling by \(\Delta^r\),

\[
\widetilde v_r(n):=a_n(-i\Delta\log n)^r.
\]

The bad equations are:

\[
\Re\sum_{n\le X}
\widetilde v_r(n)e^{-im_0\log n}
\approx
-\Delta^r\partial_m^r(B_2+D_2)(m_0),
\qquad
0\le r\le R(Q).
\]

The off-line zero equation has AFE-type coefficient vectors:

\[
w_\alpha(n):=b_n(\alpha)n^{-1/2-\alpha}
\]

and a dual vector

\[
w_\alpha^\ast(n):=\chi_\alpha(m_0)b_n^\ast(\alpha)n^{-1/2+\alpha},
\]

schematically giving

\[
Z_\alpha(m_0)
=
A_\alpha(m_0)
+
\sum_{n\le X} w_\alpha(n)e^{-im_0\log n}
+
\sum_{n\le X^\ast} w_\alpha^\ast(n)e^{+im_0\log n}
+
\mathrm{err}.
\]

So the source jets use log-weighted curvature vectors

\[
a_n(\log n)^r,
\]

while the zero equation uses AFE value vectors

\[
b_n(\alpha)n^{-\alpha}
\]

plus the dual \(\chi\)-weighted reflection.

The hoped-for rigidity must come from incompatibility among these specific vectors along the **same one-parameter orbit**.

---

# 5. Bad tube definition

Let

\[
\Theta_X(m)
=
(e^{-im\log p})_{p\le X}.
\]

Define the bad tube in the finite prime phase torus by

\[
\mathcal T_{\bad}(Q^{-B})
=
\left\{
\theta:
|Z_\alpha(\theta)|\le Q^{-B},
\quad
|\mathcal S_r(\theta,\alpha)|\le Q^{-B}
\ \text{for }0\le r\le R(Q)
\right\},
\]

where

\[
\mathcal S_r(\theta,\alpha)
=
\Delta^r\partial_m^r
(B_2+D_2+P_2)(m_0)
\]

written as a function of the phases.

Then the required nonrecurrence bound is:

\[
\boxed{
\Theta_X(m_0)\notin \mathcal T_{\bad}(Q^{-B})
\quad
\text{for every admissible off-line center }(\alpha,m_0).
}
\]

Equivalently,

\[
\boxed{
\inf_{\substack{(\alpha,m_0)\ \mathrm{admissible}\\ Z_\alpha(m_0)=0}}
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r q''_{\can}(m_0)
\right|
\ge Q^{-B}.
}
\]

This is the exact prime/AFE Gate 1 theorem.

---

# 6. Sufficient quantitative nonrecurrence bound

A sufficient statement would be:

For some \(B,C>0\), the set of \(m\in[T,2T]\) satisfying

\[
|Z_\alpha(m)|\le Q^{-C},
\]

and

\[
\max_{0\le r\le R(Q)}
|\Delta^r\partial_m^rF_2(m)|
\le Q^{-C}
\]

is empty for all admissible \(\alpha\), or at least contains no point satisfying the reduced off-line packet hypotheses.

A weaker counting version would be:

\[
\#\left\{
m\in[T,2T]:
\exists\alpha,\ |Z_\alpha(m)|\le Q^{-C},
\ 
\max_{r\le R}
|\Delta^r\partial_m^rF_2(m)|\le Q^{-C}
\right\}
=0.
\]

A density estimate is not enough unless it excludes all admissible packet centers, because even one source-flat off-line packet can break the rank-two contradiction route.

---

# 7. Candidate proof tools

## 7.1 Fixed-coefficient transversality

Potential use: prove the zero-equation coefficient vector is quantitatively incompatible with the span of source-jet coefficient vectors.

Obstacle: phase-relaxed analysis suggests the system is underdetermined. Transversality alone gives a codimension-\(R\) tube, not emptiness.

Verdict:

\[
\text{Useful for measuring rarity, insufficient alone.}
\]

## 7.2 Small-ball estimates

One could try to show that the joint small-ball event

\[
Z_\alpha(m)\approx0,
\qquad
\mathcal S_0(m)\approx\cdots\approx\mathcal S_R(m)\approx0
\]

has extremely small probability along \(m\in[T,2T]\).

Obstacle: a small probability estimate does not exclude all occurrences. Also, deterministic zeta phases are not random independent phases.

Verdict:

\[
\text{Useful for numerics/probabilistic evidence, unlikely to prove theorem directly.}
\]

## 7.3 Explicit formula imbalance

If source-flatness forces a zero-side same-scale quadrature certificate, then one might push that certificate through the explicit formula and show a prime-side imbalance.

Obstacle: previous trace analysis shows this reduces to fixed-coefficient nonrecurrence unless a genuinely coercive packet-adapted functional is found.

Verdict:

\[
\text{Promising only if it produces a new positive/coercive form.}
\]

## 7.4 AFE main/dual incompatibility

The zero equation uses both main and dual AFE sums. Source jets mostly probe log-weighted curvature of the same completed phase. There may be a compatibility obstruction involving the \(\chi\)-factor derivatives and the dual reflection.

Potential theorem:

\[
Z_\alpha(m_0)=0
\quad\Rightarrow\quad
\text{some log-weighted derivative of the completed phase is not small}.
\]

Obstacle: no sign-definite identity is currently known. The dual term may simply move the target.

Verdict:

\[
\text{Most plausible prime-side structural tool, but still undeveloped.}
\]

## 7.5 Zero-prime compatibility

Translate zero-side anti-design moments into explicit-formula identities and prove that the required packet design would force an impossible prime correlation pattern.

Obstacle: this appears equivalent to the same nonrecurrence theorem unless a new global positivity principle is added.

Verdict:

\[
\text{Equivalent formulation unless strengthened by global positivity.}
\]

---

# 8. The theorem in finite-jet and interval forms

Finite-jet form:

\[
\boxed{
\forall(\alpha,m_0)\ \mathrm{admissible},\quad
Z_\alpha(m_0)=0
\Rightarrow
\max_{0\le r\le R(Q)}
\left|
\Delta^r\partial_m^r q''_{\can}(m_0)
\right|
\ge Q^{-B}.
}
\]

Interval form:

\[
\boxed{
\forall I_\rho,\quad
\int_{I_\rho}|q''_{\can}(m)|^2\,dm
\ge Q^{-B}|I_\rho|.
}
\]

The finite-jet form implies the interval form if analytic complexity gives a Taylor/Remez implication:

\[
\int_{I_\rho}|q''_{\can}|^2\ll Q^{-B'}|I_\rho|
\quad\Rightarrow\quad
\max_{r\le R}
|\Delta^r\partial_m^r q''_{\can}(m_0)|
\ll Q^{-B}.
\]

This implication should be stated as an analytic lemma separate from the arithmetic theorem.

---

# 9. Final sharpened missing theorem

The missing prime-side theorem is:

\[
\boxed{
\textbf{Actual-zeta off-line-center source-jet nonrecurrence.}
}
\]

It says that the actual prime-log orbit cannot simultaneously satisfy:

\[
Z_\alpha(m_0)=0
\]

and

\[
\Delta^r
\partial_m^r
(B_2+P_2+D_2)(m_0)
\approx0,
\qquad
0\le r\le R(Q),
\]

with differentiated AFE error \(E_2\) absorbed.

This theorem is stronger than generic transversality and stronger than a standard large-sieve estimate. It must use actual zeta coefficient rigidity, AFE main/dual compatibility, or a new explicit-formula positivity principle.
## User (2026-04-26 14:29:08)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:29:09)

I’ll specify the actual zero-side Gate 1 scan in implementable terms: kernel convention, data handling, interval families, diagnostics, and convergence checks.

_Thought for a few seconds_

## Agent 3 / C — Actual-zero Gate 1 scan protocol

### Verdict

The actual-zero scan should be implemented **after** the synthetic quadrature negative control passes, because the zero-side computation is normalization-sensitive. The scan must measure interval energy, not just pointwise values:

\[
E_I=|I|^{-1}\int_I |q''_{\can}(m)|^2\,dm.
\]

A serious Gate 1 warning requires stable interval-level flatness under tail cutoff, quadrature refinement, and normalization cross-checks. This is the Agent 3 task in the current round. 

---

# 1. Zero-side object to compute

The canonical object is

\[
q''_{\can}(m)=q_\zeta''(m)=\Phi_\zeta'''(m).
\]

For numerical zero-side testing, use a regularized zero-kernel representation of the form

\[
q''_{\can}(m)
=
B_2(m)+\sum_{\rho}^{\rm reg}K_2(m;\rho).
\]

The exact constants depend on the paper’s normalization of \(\Phi_\zeta\), but the **flatness diagnostics are invariant up to a fixed scalar factor**:

\[
E_I,\quad S_I,\quad B_I^{\rm eff}
\]

change predictably under

\[
q''_{\can}\mapsto Cq''_{\can}.
\]

Thus the first implementation can use a consistent normalized kernel, then later match constants to the draft.

---

# 2. Recommended kernel normalization

For an off-critical zero packet with ordinate \(\gamma\) and transverse depth \(c>0\), use the Poisson packet

\[
K(m;\gamma,c)=\frac{c}{(m-\gamma)^2+c^2}.
\]

Then

\[
K_2(m;\gamma,c)
=
\frac{d^2}{dm^2}K(m;\gamma,c)
=
\frac{2c\bigl(3(m-\gamma)^2-c^2\bigr)}
{\bigl((m-\gamma)^2+c^2\bigr)^3}.
\]

So the zero-side proxy is

\[
q''_{\zero}(m)
=
B_2(m)
+
\sum_{\rho\in\mathcal Z_{\rm win}} w_\rho K_2(m;\gamma_\rho,c_\rho)
+
T_{\rm tail}^{(2)}(m).
\]

For critical-line zeros, \(c=0\) is singular in this raw model. Therefore use one of two protocols:

1. **Avoidance scan:** do not center intervals crossing critical-line ordinates; require
   \[
   \operatorname{dist}(I,\gamma)\ge \epsilon_{\rm reg}.
   \]
2. **Mollified scan:** replace \(c=0\) by a regularization width
   \[
   c=\epsilon_{\rm reg},
   \]
   and run stability checks as \(\epsilon_{\rm reg}\) varies.

For a first numerical Gate 1 scan, use the mollified scan but explicitly tag any interval whose result depends strongly on \(\epsilon_{\rm reg}\).

---

# 3. Quartet grouping

For a hypothetical off-line zero, include the functional-equation and conjugation quartet. In local packet coordinates, this means summing all reflected contributions:

\[
\rho,\quad 1-\rho,\quad \bar\rho,\quad 1-\bar\rho.
\]

Numerically, implement this as a packet group:

\[
K_{2,\quartet}
=
\sum_{\rho'\in Q(\rho)} w_{\rho'}K_2(m;\gamma_{\rho'},c_{\rho'}).
\]

For actual verified critical-line zeros, quartet grouping collapses to conjugate symmetry around the real axis and gives a real-valued contribution on the \(m\)-axis. The kernel must be implemented so that the computed \(q''_{\zero}(m)\) is real to numerical precision.

Quality check:

\[
\max_{m\in I}|\Im q''_{\zero}(m)|
\]

should be near working precision.

---

# 4. Background and tail handling

Split

\[
q''_{\can}
=
B_2+q''_{\core}+T_{\far}^{(2)}.
\]

## Background \(B_2\)

Use the gamma/completed-phase contribution from the draft normalization. If unavailable in the first run, start with

\[
B_2=0
\]

and label the result as a **zero-packet-only diagnostic**. Then add \(B_2\) once fixed.

The scan table must record:

\[
E_I^{\rm zero-only},
\qquad
E_I^{\rm zero+B_2}.
\]

## Tail cutoff

For a center \(m_0\), choose a zero window

\[
|\gamma-m_0|\le W_{\rm zero}.
\]

Compute with escalating cutoffs:

\[
W_{\rm zero}^{(1)}<W_{\rm zero}^{(2)}<W_{\rm zero}^{(3)}.
\]

Accept an interval only if

\[
\frac{|E_I(W_3)-E_I(W_2)|}{E_I(W_3)}
\le \tau_{\rm tail},
\]

with a starting threshold such as

\[
\tau_{\rm tail}=10^{-2}
\]

and stricter reruns at

\[
10^{-3},\ 10^{-4}.
\]

If the tail is regularized analytically, also compute

\[
T_{\far}^{(2)}(m)
\]

and compare against brute-force cutoff escalation.

---

# 5. Interval families

Use intervals

\[
I=[m_0-c_I/Q,m_0+c_I/Q],
\]

with

\[
c_I\in\{0.1,0.2,0.5,1.0\}.
\]

Use the draft’s \(Q\). If still ambiguous numerically, record both:

\[
Q_1=\log\frac{m_0}{2\pi},
\qquad
Q_2=\log m_0.
\]

Scan centers:

1. **Gram points**
   \[
   \theta(g_n)=n\pi.
   \]

2. **Zero ordinates**
   \[
   m_0=\gamma_n.
   \]
   These need mollification or exclusion if raw critical-line singularities are used.

3. **Zero-gap midpoints**
   \[
   m_0=\frac{\gamma_n+\gamma_{n+1}}{2}.
   \]

4. **Small-gap neighborhoods**
   Choose gaps with
   \[
   \gamma_{n+1}-\gamma_n
   \]
   in the lowest percentile, then scan several centers inside the gap.

5. **Large-gap neighborhoods**
   Same for upper percentile gaps.

6. **Random centers**
   Uniformly sample \(m_0\in[T,2T]\).

7. **Synthetic off-line packet centers**
   Add an artificial packet at \(m_0\) with depth \(c\) and test whether the pipeline sees the predicted singular dominance or cancellation.

---

# 6. Diagnostics

For each interval \(I\), compute:

\[
E_I=|I|^{-1}\int_I |q''_{\can}(m)|^2\,dm,
\]

\[
S_I=\sup_{m\in I}|q''_{\can}(m)|,
\]

\[
B_I^{\rm eff}
=
-\frac{\log E_I}{\log Q}.
\]

Also compute finite jets at \(m_0\):

\[
J_r
=
\Delta^r\partial_m^r q''_{\can}(m_0),
\qquad
0\le r\le R,
\]

where

\[
\Delta=c_I/Q.
\]

Use

\[
R\in\{4,8,12,16\}
\]

initially, with later runs using

\[
R(Q)\asymp \frac{\log Q}{\log\log Q}
\]

or

\[
R=O(\log Q).
\]

Record:

\[
J_{\max}=\max_{0\le r\le R}|J_r|,
\]

and

\[
J_{\rm rms}
=
\left(\frac1{R+1}\sum_{r=0}^R |J_r|^2\right)^{1/2}.
\]

A serious source-flat candidate must have both:

\[
E_I\ll Q^{-B}
\]

and

\[
J_{\max}\ll Q^{-B'}.
\]

Pointwise smallness alone is insufficient.

---

# 7. Quadrature and integration

Use Gauss-Legendre or Clenshaw-Curtis quadrature on \(I\). The integrand can be sharply peaked near zeros, so use adaptive subdivision.

Recommended first pass:

- 129-point Clenshaw-Curtis on the interval.
- If interval contains or approaches a zero, split at the nearest zero ordinates or regularization centers.
- Rerun with 257 and 513 nodes.

Accept only if:

\[
\frac{|E_I(N_{\rm quad}^{(2)})-E_I(N_{\rm quad}^{(1)})|}
{E_I(N_{\rm quad}^{(2)})}
\le \tau_{\rm quad}.
\]

Use

\[
\tau_{\rm quad}=10^{-3}
\]

for screening, then

\[
10^{-5}
\]

for candidate verification.

---

# 8. Precision escalation

Use multiprecision arithmetic if the regularization width is small or if \(E_I\) is tiny.

Initial precision:

\[
80\text{ bits or }30\text{ decimal digits}.
\]

Candidate rerun:

\[
160\text{--}256\text{ bits}.
\]

Reject any candidate if \(B_I^{\rm eff}\) changes materially under precision escalation.

---

# 9. Convergence requirements

A candidate interval is valid only if all of the following hold:

1. **Tail stability**
   \[
   E_I(W_2)\approx E_I(W_3).
   \]

2. **Quadrature stability**
   \[
   E_I(N_{\rm quad})\approx E_I(2N_{\rm quad}).
   \]

3. **Regularization stability**
   If using \(c=\epsilon_{\rm reg}\), results are stable over at least two nearby \(\epsilon_{\rm reg}\) values or the dependence is explicitly explained.

4. **Background stability**
   Including \(B_2\) does not radically change conclusions unless the change is understood.

5. **Jet-energy consistency**
   Small \(E_I\) must correspond to small normalized jets through the chosen \(R\), unless the interval flatness is non-Taylor-like.

6. **AFE agreement**
   Once AFE implementation exists:
   \[
   \operatorname{Err}_I
   =
   |I|^{-1}\int_I
   |q''_{\zero}(m)-q''_{\AFE}(m)|^2\,dm
   \ll E_I
   \]
   for any claimed source-flat interval.

---

# 10. Algorithm

Pseudocode:

```text
Input:
  height range [T1,T2]
  verified zeros gamma_n
  interval widths c_I_list
  zero windows W_list
  quadrature node counts Nq_list
  regularization eps_reg_list
  center families C

For each center m0 in C:
    Q = log(m0/(2*pi))
    For each c_I:
        Delta = c_I / Q
        I = [m0 - Delta, m0 + Delta]

        For each eps_reg:
            For each tail cutoff W:
                Select zeros with |gamma - m0| <= W
                Build qpp_zero(m):
                    qpp = B2(m)
                    For each zero gamma:
                        c = eps_reg if critical-line zero
                        qpp += weight * K2(m; gamma, c)
                    qpp += optional analytic tail correction

                For each quadrature size Nq:
                    Compute E_I(Nq,W,eps_reg)
                    Compute S_I(Nq,W,eps_reg)

                Compute finite jets J_r at m0
                    either analytic derivatives of K2
                    or high-order automatic differentiation

        Check stability across W, Nq, eps_reg
        Record final diagnostics
```

---

# 11. Table schema

Each row should include:

| Field | Meaning |
|---|---|
| `height_band` | e.g. \([T,2T]\) |
| `center_type` | Gram / zero / midpoint / small-gap / large-gap / random |
| `m0` | interval center |
| `Q` | chosen scale parameter |
| `c_I` | interval half-width multiplier |
| `Delta` | \(c_I/Q\) |
| `zero_window_W` | zero cutoff |
| `eps_reg` | regularization width |
| `N_quad` | quadrature nodes |
| `E_I` | interval energy |
| `S_I` | sup norm |
| `B_eff` | \(-\log E_I/\log Q\) |
| `J_max_R4` | max normalized jet through \(R=4\) |
| `J_max_R8` | max normalized jet through \(R=8\) |
| `tail_rel_change` | cutoff stability |
| `quad_rel_change` | quadrature stability |
| `reg_rel_change` | regularization stability |
| `AFE_Err` | AFE cross-check error, if available |
| `classification` | healthy / watch / candidate / reject |

---

# 12. Interpretation

## Healthy interval

\[
B_I^{\rm eff}
\]

is bounded or negative, and there is no simultaneous jet suppression.

Typical classification:

\[
E_I\asymp 1
\quad\text{or}\quad
E_I\ge Q^{-B_0}
\]

for modest \(B_0\).

## Watch interval

\[
B_I^{\rm eff}
\]

is moderately positive, but the interval fails stability checks or finite jets are not all small.

## Candidate flat interval

All of:

\[
E_I\le Q^{-B_0},
\]

\[
J_{\max}\le Q^{-B_1},
\]

tail/quadrature/regularization are stable.

## Serious Gate 1 warning

A family of candidate flat intervals with

\[
B_I^{\rm eff}
\]

growing with height or width refinement, especially if confirmed by AFE.

## Route-threatening result

A stable sequence of actual-zeta intervals satisfying

\[
E_I\ll Q^{-B}|I|
\]

for increasing \(B\) or growing effective exponent, with matching finite-jet flatness and AFE agreement.

---

# 13. Final recommendation

Run in this order:

1. Same-scale quadrature negative control.
2. Singular synthetic packet dominance/cancellation controls.
3. Low-height actual-zero proxy scan.
4. Higher-height actual-zero scan with tail escalation.
5. AFE cross-check on suspicious intervals.
6. Fixed-prime/AFE surrogate comparison.

The first actual-zero result to look for is whether actual zeta produces anything resembling the quadrature control. If not, Gate 1 remains numerically plausible. If yes, the rank-two route becomes threatened and the source-flat mechanism should be isolated immediately.
## User (2026-04-26 14:34:22)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:34:32)

_Thought for 9s_

## Agent 3 / C — Actual-zero pilot scan harness

### Objective

Implement a pilot zero-side Gate 1 scan for

\[
q''_{\can}(m)=B_2(m)+\sum_{\rho}^{\rm reg}K_2(m;\rho),
\]

with the first run allowed to use a clearly labeled proxy kernel before the final canonical normalization is fixed. The current operational instruction explicitly prioritizes executable negative controls and pilot scans over further strategic audit. 

---

# 1. Pilot kernel

For the first pilot, use the regularized Poisson packet

\[
K(m;\gamma,\varepsilon)=\frac{\varepsilon}{(m-\gamma)^2+\varepsilon^2},
\]

and define

\[
K_2(m;\gamma,\varepsilon)
=
\partial_m^2K(m;\gamma,\varepsilon)
=
\frac{2\varepsilon\left(3(m-\gamma)^2-\varepsilon^2\right)}
{\left((m-\gamma)^2+\varepsilon^2\right)^3}.
\]

Then the pilot object is

\[
q''_{\zero,\varepsilon}(m)
=
\sum_{\gamma\in\mathcal Z_W(m_0)}K_2(m;\gamma,\varepsilon)
\]

for the zero-kernel-only pilot.

This is **not yet the final canonical \(q''_{\can}\)**. It is a normalized, regularized zero-side proxy designed to test whether the pipeline detects interval-level source flatness.

For critical-line zeros, use the same \(\varepsilon\)-regularization:

\[
c_\gamma=\varepsilon.
\]

Recommended initial choice:

\[
\varepsilon=\kappa/Q,\qquad \kappa\in\{0.25,0.5,1.0\}.
\]

Any candidate whose flatness changes substantially as \(\kappa\) varies is rejected or labeled regularization-dependent.

---

# 2. Background \(B_2(m)\)

Pilot stage 1 should be explicitly labeled:

\[
B_2=0,\qquad \text{“zero-kernel-only proxy.”}
\]

Pilot stage 2 should add a smooth background term once the canonical convention is fixed. The table should therefore include both fields:

\[
E_I^{\rm zero},
\qquad
E_I^{\rm zero+B_2}.
\]

If \(B_2\) is not yet canonical, do not tune it to reduce \(E_I\). Treat it as absent or use only a predetermined formula.

---

# 3. Tail handling

For each center \(m_0\), define a symmetric zero cutoff window:

\[
\mathcal Z_W(m_0)=\{\gamma:|\gamma-m_0|\le W\}.
\]

Run at escalating cutoffs:

\[
W\in\{10/Q,\ 25/Q,\ 50/Q,\ 100/Q\}
\]

for low-height pilots, and also try fixed ordinate windows:

\[
W\in\{5,\ 10,\ 20\}
\]

where zero data availability permits.

Tail stability metric:

\[
\mathrm{tail\_drift}
=
\frac{|E_I(W_{\rm large})-E_I(W_{\rm mid})|}
{\max(E_I(W_{\rm large}),10^{-300})}.
\]

Screening threshold:

\[
\mathrm{tail\_drift}\le10^{-2}.
\]

Candidate threshold:

\[
\mathrm{tail\_drift}\le10^{-4}.
\]

Use symmetric windows only; asymmetric truncation can create artificial curvature.

---

# 4. Center families

Use intervals

\[
I=[m_0-c_I/Q,\ m_0+c_I/Q],
\qquad
Q=\log(m_0/2\pi).
\]

Run

\[
c_I\in\{0.1,\ 0.2,\ 0.5,\ 1.0\}.
\]

Center families:

1. **Zero ordinates**
   \[
   m_0=\gamma_n.
   \]
   These are regularization-sensitive. Include them, but tag them as `zero_center`.

2. **Gap midpoints**
   \[
   m_0=\frac{\gamma_n+\gamma_{n+1}}2.
   \]
   These are the cleanest first actual-zero scan points.

3. **Small-gap neighborhoods**  
   Select gaps in the lowest 5% by normalized spacing. Test:
   \[
   m_0=\gamma_n+\eta(\gamma_{n+1}-\gamma_n),
   \qquad
   \eta\in\{0.25,0.5,0.75\}.
   \]

4. **Large-gap neighborhoods**  
   Same for top 5% gaps.

5. **Gram points**  
   If Gram points are available, scan them. Otherwise skip in pilot v1.

6. **Random centers**
   Uniform random \(m_0\) over the available zero-data height range, excluding points closer than a configurable tolerance to endpoints.

---

# 5. Diagnostics

For every interval compute:

\[
E_I=|I|^{-1}\int_I |q''_{\zero,\varepsilon}(m)|^2\,dm,
\]

\[
S_I=\sup_{m\in I}|q''_{\zero,\varepsilon}(m)|,
\]

\[
B_I^{\rm eff}=-\frac{\log E_I}{\log Q}.
\]

Let

\[
\Delta=c_I/Q.
\]

Compute finite jets:

\[
J_r=\Delta^r\partial_m^r q''_{\zero,\varepsilon}(m_0),
\qquad
0\le r\le R.
\]

For the pilot, use

\[
R\in\{4,8,12\}.
\]

Record:

\[
J_{\max,R}=\max_{0\le r\le R}|J_r|,
\]

\[
J_{\rm rms,R}=
\left(\frac1{R+1}\sum_{r=0}^R|J_r|^2\right)^{1/2}.
\]

A candidate is only meaningful if both interval energy and finite jets are small.

---

# 6. Numerical integration

Use adaptive Gauss-Legendre or Clenshaw-Curtis quadrature.

Pilot recommendation:

- Start with 257 Clenshaw-Curtis nodes.
- Rerun with 513 and 1025 nodes for low-energy intervals.
- If an interval contains a zero ordinate, split the interval at that ordinate before quadrature.

Quadrature drift:

\[
\mathrm{quad\_drift}
=
\frac{|E_I(N_2)-E_I(N_1)|}
{\max(E_I(N_2),10^{-300})}.
\]

Screening threshold:

\[
\mathrm{quad\_drift}\le10^{-3}.
\]

Candidate threshold:

\[
\mathrm{quad\_drift}\le10^{-5}.
\]

---

# 7. Pseudocode

```python
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def K2_poisson(m, gamma, eps):
    x = m - gamma
    den = x*x + eps*eps
    return 2.0 * eps * (3.0*x*x - eps*eps) / (den**3)

def qpp_zero_proxy(m, gammas, eps, B2=None):
    val = 0.0
    for gamma in gammas:
        val += K2_poisson(m, gamma, eps)
    if B2 is not None:
        val += B2(m)
    return val

def integrate_interval(func, a, b, n_nodes=257):
    xs, ws = leggauss(n_nodes)
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)
    pts = mid + half * xs
    vals = np.array([func(float(x)) for x in pts])
    integral = half * np.sum(ws * vals * vals)
    sup_norm = np.max(np.abs(vals))
    return integral, sup_norm

def finite_difference_jets(func, m0, Delta, R, h_factor=1e-3):
    # For pilot only. Replace with analytic derivatives or AD later.
    # Use polynomial interpolation on a symmetric stencil.
    h = h_factor * Delta
    stencil_radius = max(R + 3, 12)
    xs = np.arange(-stencil_radius, stencil_radius + 1) * h
    ys = np.array([func(m0 + x) for x in xs])

    # Fit polynomial around 0.
    deg = min(2 * stencil_radius, R + 8)
    coeffs = np.polynomial.polynomial.polyfit(xs, ys, deg)

    jets = []
    for r in range(R + 1):
        deriv = math.factorial(r) * coeffs[r]
        jets.append((Delta**r) * deriv)
    return np.array(jets)

def select_zeros(zeros, m0, W):
    return [g for g in zeros if abs(g - m0) <= W]

def scan_interval(zeros, m0, c_I, kappa, W, R, n_nodes, B2=None):
    Q = math.log(m0 / (2.0 * math.pi))
    Delta = c_I / Q
    eps = kappa / Q
    a, b = m0 - Delta, m0 + Delta

    gammas = select_zeros(zeros, m0, W)

    def f(m):
        return qpp_zero_proxy(m, gammas, eps, B2=B2)

    integral, S_I = integrate_interval(f, a, b, n_nodes=n_nodes)
    E_I = integral / (2.0 * Delta)
    B_eff = -math.log(max(E_I, 1e-300)) / math.log(Q)

    jets = finite_difference_jets(f, m0, Delta, R)
    J_max = float(np.max(np.abs(jets)))
    J_rms = float(np.sqrt(np.mean(jets * jets)))

    return {
        "m0": m0,
        "Q": Q,
        "c_I": c_I,
        "Delta": Delta,
        "eps": eps,
        "kappa": kappa,
        "W": W,
        "R": R,
        "n_nodes": n_nodes,
        "num_zeros": len(gammas),
        "E_I": E_I,
        "S_I": S_I,
        "B_eff": B_eff,
        "J_max": J_max,
        "J_rms": J_rms,
    }
```

---

# 8. Center generation pseudocode

```python
def gap_midpoints(zeros, start_idx, end_idx):
    centers = []
    for i in range(start_idx, end_idx):
        centers.append(("gap_midpoint", 0.5 * (zeros[i] + zeros[i+1]), i))
    return centers

def zero_centers(zeros, start_idx, end_idx):
    return [("zero", zeros[i], i) for i in range(start_idx, end_idx + 1)]

def small_large_gap_centers(zeros, start_idx, end_idx, pct=0.05):
    gaps = []
    for i in range(start_idx, end_idx):
        gaps.append((zeros[i+1] - zeros[i], i))
    gaps_sorted = sorted(gaps)

    k = max(1, int(len(gaps_sorted) * pct))
    small = gaps_sorted[:k]
    large = gaps_sorted[-k:]

    centers = []
    for label, selected in [("small_gap", small), ("large_gap", large)]:
        for gap, i in selected:
            for eta in [0.25, 0.5, 0.75]:
                centers.append((label, zeros[i] + eta * gap, i))
    return centers

def random_centers(zeros, start_idx, end_idx, n_random=100, seed=0):
    rng = np.random.default_rng(seed)
    lo = zeros[start_idx]
    hi = zeros[end_idx]
    return [("random", float(rng.uniform(lo, hi)), None) for _ in range(n_random)]
```

---

# 9. Full scan loop

```python
def run_pilot_scan(zeros, start_idx, end_idx):
    centers = []
    centers += gap_midpoints(zeros, start_idx, end_idx)
    centers += zero_centers(zeros, start_idx, end_idx)
    centers += small_large_gap_centers(zeros, start_idx, end_idx)
    centers += random_centers(zeros, start_idx, end_idx, n_random=200)

    c_I_list = [0.1, 0.2, 0.5, 1.0]
    kappa_list = [0.25, 0.5, 1.0]
    W_mult_list = [10, 25, 50, 100]
    R_list = [4, 8, 12]
    n_nodes_list = [257, 513]

    rows = []

    for center_type, m0, ref_idx in centers:
        Q = math.log(m0 / (2.0 * math.pi))
        for c_I in c_I_list:
            for kappa in kappa_list:
                for R in R_list:
                    for W_mult in W_mult_list:
                        W = W_mult / Q
                        for n_nodes in n_nodes_list:
                            try:
                                row = scan_interval(
                                    zeros=zeros,
                                    m0=m0,
                                    c_I=c_I,
                                    kappa=kappa,
                                    W=W,
                                    R=R,
                                    n_nodes=n_nodes,
                                    B2=None
                                )
                                row["center_type"] = center_type
                                row["ref_idx"] = ref_idx
                                row["W_mult"] = W_mult
                                row["run_label"] = "zero_kernel_only_proxy"
                                rows.append(row)
                            except Exception as e:
                                rows.append({
                                    "center_type": center_type,
                                    "m0": m0,
                                    "error": str(e),
                                })
    return rows
```

---

# 10. Required input data format

CSV or array with one column:

| column | meaning |
|---|---|
| `gamma` | imaginary part of verified zero \(1/2+i\gamma\) |

Optional columns:

| column | meaning |
|---|---|
| `index` | zero index \(n\) |
| `is_verified` | boolean |
| `multiplicity` | expected 1 |
| `source` | Odlyzko/mpmath/etc. |

For the pilot, assume all zeros are critical-line zeros and use mollification width \(\varepsilon=\kappa/Q\).

---

# 11. Output table schema

| field | meaning |
|---|---|
| `run_label` | `zero_kernel_only_proxy` / later `zero_plus_B2` |
| `center_type` | zero / midpoint / small_gap / large_gap / random / Gram |
| `ref_idx` | nearby zero index |
| `m0` | interval center |
| `Q` | \(\log(m_0/2\pi)\) |
| `c_I` | interval width multiplier |
| `Delta` | \(c_I/Q\) |
| `kappa` | regularization multiplier |
| `eps` | \(\kappa/Q\) |
| `W_mult` | tail cutoff multiplier |
| `W` | cutoff window |
| `num_zeros` | zeros used |
| `R` | jet depth |
| `n_nodes` | quadrature nodes |
| `E_I` | mean interval energy |
| `S_I` | sampled sup norm |
| `B_eff` | \(-\log E_I/\log Q\) |
| `J_max` | max normalized jet |
| `J_rms` | rms normalized jet |
| `tail_drift` | computed in postprocessing |
| `quad_drift` | computed in postprocessing |
| `reg_drift` | computed in postprocessing |
| `classification` | healthy/watch/candidate/reject |

---

# 12. Stability postprocessing

Group rows by:

\[
(m_0,c_I,kappa,R)
\]

and compare across \(W\) to compute tail drift.

Group rows by:

\[
(m_0,c_I,kappa,W,R)
\]

and compare across quadrature nodes to compute quadrature drift.

Group rows by:

\[
(m_0,c_I,W,R)
\]

and compare across \(\kappa\) to compute regularization drift.

Reject candidate if any of:

\[
\mathrm{tail\_drift}>10^{-4},
\]

\[
\mathrm{quad\_drift}>10^{-5},
\]

\[
\mathrm{reg\_drift}>10^{-2}.
\]

The regularization drift threshold is looser for the first pilot because critical-line mollification is not canonical.

---

# 13. Candidate classification

Use this first-pass rule:

### Healthy

\[
B_I^{\rm eff}\le 2
\]

or jets are not simultaneously small.

### Watch

\[
2<B_I^{\rm eff}\le5
\]

with partial jet suppression or moderate instability.

### Candidate flat

\[
B_I^{\rm eff}>5,
\qquad
J_{\max,R}\le Q^{-3}
\]

for at least \(R=8\), with stable tail and quadrature.

### Serious warning

Candidate flat persists for:

- multiple \(c_I\);
- multiple \(R\);
- stable \(\kappa\);
- larger zero windows;
- and later AFE agreement.

### Reject

Any isolated point smallness without interval energy collapse, or instability in tail/quadrature/regularization.

---

# 14. Immediate pilot parameters

Start with a small, fast pilot:

\[
n=1,\ldots,500
\]

zeros.

Use centers:

- all gap midpoints for \(n=50,\ldots,450\);
- all zero centers for \(n=50,\ldots,450\);
- 50 small-gap centers;
- 50 large-gap centers;
- 200 random centers.

Use:

\[
c_I\in\{0.2,0.5\},
\quad
\kappa\in\{0.5,1.0\},
\quad
R\in\{4,8\},
\quad
W\in\{25/Q,50/Q,100/Q\},
\quad
N_{\rm quad}\in\{257,513\}.
\]

After the pipeline is stable, expand to:

\[
R=12,\quad
c_I\in\{0.1,0.2,0.5,1.0\},
\quad
\kappa\in\{0.25,0.5,1.0\}.
\]

---

# 15. Final note

This pilot is not a proof and not yet the final canonical computation. Its purpose is to detect whether actual zero data behaves remotely like the same-scale quadrature negative control.

The key comparison is:

\[
B_I^{\rm eff}\ \text{and}\ J_{\max}
\]

for:

1. deterministic quadrature negative control;
2. actual zero-kernel-only proxy;
3. later \(B_2\)-corrected zero computation;
4. later AFE cross-check.

If actual-zero intervals produce stable, quadrature-like collapse in \(E_I\) and \(J_r\), Gate 1 is numerically threatened. If they do not, Gate 1 remains numerically plausible.
## User (2026-04-26 14:37:55)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 14:37:57)

I’ll refine the actual-zero pilot into a small first run that can expose pipeline bugs quickly, then a larger scan only after stability checks pass.

_Thought for 8s_

## Agent 3 / C — Actual-zero pilot scan parameter refinement

### Verdict

The first actual-zero pilot should be deliberately small and labeled as a **zero-kernel-only proxy**. Its purpose is not to establish Gate 1, but to verify that the harness behaves sensibly after the deterministic quadrature and singular controls pass. The attached instruction asks specifically for parameter refinement, expected costs, artifact risks, and a staged pilot plan. 

---

# 1. Minimal pilot dataset

Use the first **500 nontrivial zero ordinates** for a smoke/small scan.

Recommended bands:

| stage | zero indices | purpose |
|---|---:|---|
| smoke | 50–100 | verify code, stability fields, output schema |
| small scan | 50–500 | first meaningful proxy scan |
| expanded scan | 500–5,000 or higher | only after controls pass |

Avoid the first few zeros for the first scan because \(Q=\log(m/2\pi)\) is small and \(B_I^{\rm eff}\) is unstable.

Use

\[
Q=\log(m_0/2\pi).
\]

If \(Q\le 2\), tag rows as low-scale and exclude them from trend interpretation.

---

# 2. Center families for first run

For the small scan over zero indices \(50,\ldots,500\), use:

1. **Gap midpoints**  
   All:
   \[
   m_0=\frac{\gamma_n+\gamma_{n+1}}2.
   \]
   These are the cleanest because they avoid placing \(m_0\) exactly on a mollified singularity.

2. **Zero centers**  
   Every 5th zero:
   \[
   m_0=\gamma_n.
   \]
   These are regularization-sensitive; include only to validate behavior near singularities.

3. **Small-gap neighborhoods**  
   Lowest 5% of gaps, with:
   \[
   \eta\in\{0.25,0.5,0.75\}.
   \]

4. **Large-gap neighborhoods**  
   Highest 5% of gaps, same \(\eta\).

5. **Random centers**  
   100 random centers uniformly over:
   \[
   [\gamma_{50},\gamma_{500}].
   \]

Skip Gram points in pilot v1 unless a reliable Gram-point generator is already available.

Expected row count before parameter expansion:

| center type | approximate centers |
|---|---:|
| gap midpoints | 450 |
| zero centers every 5th | 90 |
| small-gap neighborhoods | \(0.05\cdot450\cdot3\approx68\) |
| large-gap neighborhoods | \(0.05\cdot450\cdot3\approx68\) |
| random | 100 |
| total centers | \(\approx776\) |

---

# 3. Initial parameter values

Keep the first run compact:

\[
c_I\in\{0.2,0.5\},
\]

\[
\kappa\in\{0.5,1.0\},
\qquad
\varepsilon=\kappa/Q,
\]

\[
W\in\{25/Q,50/Q,100/Q\},
\]

\[
R\in\{4,8\},
\]

\[
N_{\rm quad}\in\{257,513\}.
\]

This yields roughly:

\[
776\times 2\times2\times3\times2\times2
\approx 37{,}248
\]

raw rows. That is acceptable if the kernel loop is vectorized. If not vectorized, cut random centers to 25 and use only \(R=4\) for smoke.

For the smoke test:

\[
c_I=0.5,\quad \kappa=1.0,\quad W=50/Q,\quad R=4,\quad N_{\rm quad}=257.
\]

---

# 4. Pilot kernel and artifact risks

Use:

\[
q''_{\zero,\varepsilon}(m)
=
\sum_{\gamma\in\mathcal Z_W(m_0)}
K_2(m;\gamma,\varepsilon),
\]

where

\[
K_2(m;\gamma,\varepsilon)
=
\frac{2\varepsilon(3(m-\gamma)^2-\varepsilon^2)}
{\left((m-\gamma)^2+\varepsilon^2\right)^3}.
\]

This is a proxy for the canonical zero-side object, not the final \(q''_{\can}\).

## Expected artifacts

### 4.1 Regularization dependence

Since all verified zeros are critical-line zeros, replacing \(c=0\) by

\[
\varepsilon=\kappa/Q
\]

creates an artificial scale. Near zero centers,

\[
K_2(\gamma;\gamma,\varepsilon)
=
-\frac{2}{\varepsilon^3},
\]

so values can be dominated by \(\kappa\). Therefore zero-centered intervals should not be used as evidence for or against Gate 1 in pilot v1.

### 4.2 Tail imbalance

The raw zero sum is not guaranteed to be absolutely stable without the canonical background/tail correction. Symmetric cutoff escalation is mandatory.

### 4.3 Endpoint effects

If \(I\) is close to the edge of the available zero list, the tail window is incomplete. Reject or tag rows where:

\[
m_0-W < \gamma_{\min}
\quad\text{or}\quad
m_0+W > \gamma_{\max}.
\]

### 4.4 Low-\(Q\) instability

At low heights, \(Q\) is small, and

\[
B_I^{\rm eff}=-\frac{\log E_I}{\log Q}
\]

can overreact. Treat it as a diagnostic, not an asymptotic estimate.

---

# 5. Stability tests

## Tail stability

For fixed

\[
(m_0,c_I,\kappa,R,N_{\rm quad}),
\]

compare

\[
W=50/Q
\quad\text{and}\quad
W=100/Q.
\]

Define

\[
D_{\tail}
=
\frac{|E_I(100/Q)-E_I(50/Q)|}
{\max(E_I(100/Q),10^{-300})}.
\]

Screening pass:

\[
D_{\tail}\le 10^{-2}.
\]

Candidate pass:

\[
D_{\tail}\le 10^{-4}.
\]

## Regularization stability

For fixed

\[
(m_0,c_I,W,R,N_{\rm quad}),
\]

compare \(\kappa=0.5\) and \(\kappa=1.0\):

\[
D_{\reg}
=
\frac{|E_I(\kappa=1.0)-E_I(\kappa=0.5)|}
{\max(E_I(\kappa=1.0),10^{-300})}.
\]

For pilot proxy data, use loose interpretation:

- \(D_{\reg}\le10^{-1}\): stable enough for watch.
- \(D_{\reg}\le10^{-2}\): candidate-quality.
- \(D_{\reg}>10^{-1}\): likely regularization artifact.

## Quadrature stability

Compare

\[
N_{\rm quad}=257
\quad\text{and}\quad
513.
\]

\[
D_{\quad}
=
\frac{|E_I(513)-E_I(257)|}
{\max(E_I(513),10^{-300})}.
\]

Screening:

\[
D_{\quad}\le10^{-3}.
\]

Candidate:

\[
D_{\quad}\le10^{-5}.
\]

---

# 6. First-run table schema

Minimum fields:

| field | description |
|---|---|
| `run_id` | unique scan ID |
| `run_label` | `zero_kernel_only_proxy` |
| `zero_range` | e.g. `50-500` |
| `center_type` | midpoint / zero / small_gap / large_gap / random |
| `zero_index_ref` | nearby zero index |
| `m0` | interval center |
| `Q` | \(\log(m_0/2\pi)\) |
| `c_I` | interval multiplier |
| `Delta` | \(c_I/Q\) |
| `kappa` | regularization multiplier |
| `eps` | \(\kappa/Q\) |
| `W_mode` | e.g. `25_over_Q` |
| `W` | tail window |
| `N_quad` | quadrature nodes |
| `R` | jet depth |
| `num_zeros_used` | zeros inside cutoff |
| `edge_truncated` | true/false |
| `E_I` | interval energy |
| `S_I` | sampled sup norm |
| `B_eff` | \(-\log E_I/\log Q\) |
| `J_max` | max normalized jet |
| `J_rms` | RMS normalized jet |
| `D_tail` | postprocessed tail drift |
| `D_quad` | postprocessed quadrature drift |
| `D_reg` | postprocessed regularization drift |
| `classification` | healthy/watch/candidate/reject |
| `notes` | artifact notes |

Expected small-scan raw row count:

\[
\approx 37{,}000.
\]

Postprocessed grouped summaries should be much smaller, roughly one row per:

\[
(m_0,c_I,R)
\]

after selecting stable \(W,\kappa,N_{\rm quad}\).

---

# 7. Computational cost estimate

Each energy computation evaluates:

\[
N_{\rm quad}\times N_{\rm zero-window}
\]

kernel terms.

At height near the first 500 zeros, \(Q\) is small and \(W=100/Q\) may include \(O(10)\) to \(O(100)\) zeros depending on \(m_0\). The first pilot is cheap.

Rough upper bound:

\[
37{,}000 \times 513 \times 100
\approx 1.9\times10^9
\]

kernel evaluations if run naively. That is too high in pure Python.

Recommended implementation:

- Vectorize over quadrature points and zeros using NumPy.
- Cache selected zero windows per \((m_0,W)\).
- For smoke, use only one \(W\), one \(\kappa\), one \(N_{\rm quad}\).
- For small scan, compute stability only for intervals with promising \(B_I^{\rm eff}\) or suspiciously low \(E_I\).

Practical staged approach:

1. Smoke: ~1,000 rows.
2. Small screening: ~5,000–10,000 rows.
3. Stability expansion only for top 1–5% lowest \(E_I\) or highest \(B_I^{\rm eff}\).

---

# 8. Staged pilot plan

## Stage 0 — Controls must pass first

Before actual zeros:

1. Deterministic sine-quadrature negative control must produce:
   \[
   J_{\max}\approx 0
   \]
   through requested \(R\), and very small \(E_X\).

2. Random packet control must not usually collapse.

3. Singular single-packet control must show huge Gate 2 mass.

4. Singular quadrature cluster must show Gate 1 collapse.

If these fail, do not run actual-zero scans.

---

## Stage 1 — Smoke test

Use:

\[
n=50,\ldots,100.
\]

Centers:

- 50 gap midpoints;
- 10 zero centers;
- 25 random centers.

Parameters:

\[
c_I=0.5,\quad \kappa=1.0,\quad W=50/Q,\quad R=4,\quad N_{\rm quad}=257.
\]

Expected output:

- No candidate claims.
- Verify no NaNs/infinities.
- Verify zero centers show larger regularization-sensitive values.
- Verify midpoint rows are numerically stable.

---

## Stage 2 — Small scan

Use:

\[
n=50,\ldots,500.
\]

Centers as above.

Parameters:

\[
c_I\in\{0.2,0.5\},
\quad
\kappa\in\{0.5,1.0\},
\quad
W\in\{25/Q,50/Q,100/Q\},
\quad
R\in\{4,8\},
\quad
N_{\rm quad}\in\{257,513\}.
\]

But run full stability only for suspicious rows.

Suspicious preliminary criterion:

\[
B_I^{\rm eff}>2
\quad\text{or}\quad
J_{\max,R=4}<Q^{-2}.
\]

---

## Stage 3 — Expanded scan

Only after Stage 2 is stable.

Use:

\[
n=500,\ldots,5000
\]

or a high Odlyzko block if available.

Add:

\[
c_I\in\{0.1,1.0\},
\quad
\kappa=0.25,
\quad
R=12.
\]

Add Gram points if available.

---

## Stage 4 — Candidate rerun

For any candidate:

- increase zero window by \(2\times\);
- run \(N_{\rm quad}=1025\) or adaptive integration;
- add \(R=16\);
- run \(\kappa\in\{0.25,0.5,1.0,2.0\}\);
- add \(B_2\) if canonical background is available;
- compare with AFE once implemented.

---

# 9. Candidate interpretation in pilot

For this proxy scan, do **not** call any result a Gate 1 failure.

Use language:

- `healthy_proxy`
- `watch_proxy`
- `flat_proxy_candidate`
- `regularization_artifact`
- `tail_artifact`
- `quadrature_artifact`

Pilot candidate flat interval:

\[
B_I^{\rm eff}>5,
\]

\[
J_{\max,R=8}<Q^{-3},
\]

\[
D_{\tail}<10^{-4},
\]

\[
D_{\quad}<10^{-5},
\]

\[
D_{\reg}<10^{-2}.
\]

Anything less is only a watch item.

---

# 10. Final recommendation

Run the first actual-zero pilot with:

\[
\boxed{
n=50\ldots500,\quad
c_I\in\{0.2,0.5\},\quad
\kappa\in\{0.5,1.0\},\quad
R\in\{4,8\}.
}
\]

Use gap midpoints as the primary evidence set. Treat zero-centered intervals as regularization tests only.

The first question is simple:

\[
\boxed{
\text{Does the actual zero-kernel proxy ever look like the sine-quadrature negative control?}
}
\]

If no, Gate 1 remains numerically plausible. If yes, rerun those intervals with strict stability checks and AFE cross-check before drawing any conclusion.
## User (2026-04-26 14:40:35)

OK run it

## Assistant (2026-04-26 14:40:37)

I’ll run the executable parts now: deterministic quadrature control, singular controls, and a zero-kernel-only actual-zero pilot. I’ll skip the AFE cross-check because the canonical \(B_2+D_2+E_2\) normalization is not yet fixed.

_Thought for 5m 41s_

_Thought for 7m 13s_

I attempted to run the pilot harness, but the execution backend timed out even on trivial checks, so I do **not** have trustworthy numerical outputs to report.

What I was going to run first:

1. deterministic sine-quadrature negative control;
2. singular dominance/cancellation controls;
3. zero-kernel-only actual-zero pilot over roughly zeros 50–500;
4. stability checks across \(W,\kappa,N_{\rm quad}\).

I should not fabricate a results table. The next best concrete output I can give is a single local Python script that runs the pilot end-to-end on your machine or in a fresh notebook, including CSV output and the negative-control validation.
## User (2026-04-26 15:03:52)

OK run the next step

## Assistant (2026-04-26 15:04:22)

_Stopped thinking_

## User (2026-04-26 15:04:27)

Try to re-run what failed

## Assistant (2026-04-26 15:04:28)

I’ll rerun with a smaller, controlled sequence first: exact quadrature control, singular scaling sanity check, then a small actual-zero proxy scan. I’ll report only outputs that complete and pass basic sanity checks.

_Thought for 8m 0s_

I retried. The backend still timed out on the actual-zero pilot scan, including a trivial container check, so I cannot honestly report a completed actual-zero table.

I did get two useful partial runs before the timeout:

## 1. Deterministic quadrature negative control: passed

Using

\[
\theta_j=\frac{j\pi}{N+1},
\qquad
w_j=\frac{2}{N+1}\sin\theta_j,
\]

the moment residuals were at floating-point noise level:

| \(R\) | \(X_0\) | \(E_X\) | \(S_X\) | max moment residual |
|---:|---:|---:|---:|---:|
| 12 | 0.25 | \(2.20\times10^{-30}\) | \(1.12\times10^{-14}\) | \(4.06\times10^{-16}\) |
| 12 | 0.50 | \(9.68\times10^{-14}\) | \(2.32\times10^{-6}\) | \(4.06\times10^{-16}\) |
| 12 | 0.75 | \(1.94\times10^{-4}\) | \(9.90\times10^{-2}\) | \(4.06\times10^{-16}\) |
| 24 | 0.25 | \(2.66\times10^{-32}\) | \(5.27\times10^{-16}\) | \(1.65\times10^{-15}\) |
| 24 | 0.50 | \(2.09\times10^{-27}\) | \(4.65\times10^{-13}\) | \(1.65\times10^{-15}\) |
| 24 | 0.75 | \(1.31\times10^{-9}\) | \(3.59\times10^{-4}\) | \(1.65\times10^{-15}\) |
| 40 | 0.25 | \(1.69\times10^{-32}\) | \(2.64\times10^{-16}\) | \(2.14\times10^{-15}\) |
| 40 | 0.50 | \(1.37\times10^{-32}\) | \(2.91\times10^{-16}\) | \(2.14\times10^{-15}\) |
| 40 | 0.75 | \(5.65\times10^{-17}\) | \(9.59\times10^{-8}\) | \(2.14\times10^{-15}\) |

Interpretation: the negative control works. It produces the expected source-collapse signature, especially for larger \(R\). This validates that the diagnostic can detect the known adversary. 

## 2. Singular dominance control: passed

For a single shallow packet with

\[
Q(x)=\frac{1}{1+x^2},
\]

the Gate 2 mass scaled as expected:

\[
\int |u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm
\asymp c^{-15}.
\]

| \(c\) | Gate 2 mass | mass \(\times c^{15}\) |
|---:|---:|---:|
| \(10^{-2}\) | \(3.91\times10^{30}\) | \(3.91\) |
| \(10^{-3}\) | \(3.91\times10^{45}\) | \(3.91\) |
| \(10^{-4}\) | \(3.91\times10^{60}\) | \(3.91\) |

Interpretation: singular dominance is not dangerous; it gives overwhelming mass. The dangerous singular case remains quadrature cancellation, i.e. Gate 1 again.

## 3. Actual-zero pilot: still failed to complete

I successfully generated 150 zeta zero ordinates using `mpmath.zetazero`, but the scan loop timed out before returning even a smoke-test result table. I then tried an even smaller vectorized scan and a trivial container check; those also timed out.

So the status is:

\[
\text{controls: partial success}
\]

\[
\text{actual-zero scan: not completed due execution timeout}
\]

I do not have evidence yet for or against actual-zeta Gate 1 from the scan.
## User (2026-04-26 15:12:45)

OK retry running what failed in a fresh environment

## Assistant (2026-04-26 15:12:46)

I’ll rerun in a fresh Python kernel path with a much smaller smoke test first, then expand only if the smoke run completes. I’ll treat the output as proxy diagnostics, not proof evidence.

_Thought for 2m 23s_

I retried in a fresh execution path, including a minimal sanity check (`echo hello` and a one-line Python version print). The execution environment is still timing out before even trivial commands return, so I cannot run the failed actual-zero pilot here right now.

Status:

| Component | Result |
|---|---|
| deterministic
## User (2026-04-26 15:15:22)

give me the script you want to run and I'll run it locally

## Assistant (2026-04-26 15:15:44)

_Thought for 15s_

Below is a single local Python script for the Gate 1 pilot harness: deterministic quadrature negative control, singular dominance control, and the zero-kernel-only actual-zero proxy scan described in the latest execution plan. 

Install:

```bash
pip install numpy mpmath
```

Run controls first:

```bash
python gate1_pilot.py --mode controls --outdir gate1_out
```

Run a small actual-zero smoke scan:

```bash
python gate1_pilot.py --mode actual --outdir gate1_out --zeros 500 --start-index 50 --end-index 500
```

Full script:

```python
#!/usr/bin/env python3
"""
Gate 1 pilot harness.

Modes:
  controls  - deterministic same-scale quadrature negative control + singular dominance control
  actual    - zero-kernel-only proxy scan using zeta zero ordinates from mpmath
  all       - controls + actual

Outputs CSV files in --outdir.

This is NOT the final canonical q''_can computation. The actual-zero scan uses:
  qpp_zero_eps(m) = sum_gamma K2(m; gamma, eps)
with
  K(m; gamma, eps) = eps / ((m-gamma)^2 + eps^2)
  K2 = d^2/dm^2 K
as a labeled zero-kernel-only proxy.
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

# ----------------------------
# Utility
# ----------------------------

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def safe_log(x: float, floor: float = 1e-300) -> float:
    return math.log(max(float(x), floor))

def write_csv(path: str, rows: List[Dict]) -> None:
    if not rows:
        return
    keys = sorted({k for row in rows for k in row.keys()})
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in rows:
            w.writerow(row)

def summarize_top(rows: List[Dict], key: str, n: int = 10, reverse: bool = True) -> List[Dict]:
    clean = [r for r in rows if key in r and isinstance(r[key], (int, float)) and math.isfinite(r[key])]
    return sorted(clean, key=lambda r: r[key], reverse=reverse)[:n]

# ----------------------------
# Negative control: same-scale quadrature
# ----------------------------

def quadrature_nodes_weights(R: int, N: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Deterministic sine quadrature:
      theta_j = j*pi/(N+1)
      w_j = 2/(N+1) sin(theta_j)
    For 1 <= k <= N:
      sum_j w_j sin(k theta_j) = delta_{k1}
    """
    if N is None:
        N = R + 3
    j = np.arange(1, N + 1, dtype=float)
    theta = j * math.pi / (N + 1)
    w = 2.0 / (N + 1) * np.sin(theta)
    return theta, w

def Ktheta(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    K_theta(x) = sin(theta) / ((x - cos(theta))^2 + sin(theta)^2)
    Vectorized over x and theta.
    Returns shape (len(x), len(theta)).
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    den = (xx - c) ** 2 + s ** 2
    return s / den

def Ktheta_second(theta: np.ndarray, x: np.ndarray) -> np.ndarray:
    """
    d^2/dx^2 K_theta(x)
    = 2s(3y^2 - s^2)/(y^2+s^2)^3, y=x-cos(theta).
    """
    s = np.sin(theta)[None, :]
    c = np.cos(theta)[None, :]
    xx = x[:, None]
    y = xx - c
    den = y ** 2 + s ** 2
    return 2.0 * s * (3.0 * y ** 2 - s ** 2) / (den ** 3)

def integrate_on_interval_values(func_values: Callable[[np.ndarray], np.ndarray],
                                 a: float,
                                 b: float,
                                 n_nodes: int = 1001) -> Tuple[float, float]:
    """
    Integrate |f|^2 over [a,b] and compute sampled sup norm.
    """
    xs, ws = leggauss(n_nodes)
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)
    pts = mid + half * xs
    vals = func_values(pts)
    integral = half * float(np.sum(ws * vals * vals))
    supnorm = float(np.max(np.abs(vals)))
    return integral, supnorm

def run_negative_control(outdir: str) -> List[Dict]:
    rows: List[Dict] = []
    for R in [12, 24, 40]:
        N = R + 3
        theta, w = quadrature_nodes_weights(R, N=N)

        # Moment checks through R+3
        residuals = []
        for k in range(1, R + 4):
            target = 1.0 if k == 1 else 0.0
            val = float(np.sum(w * np.sin(k * theta)))
            residuals.append(abs(val - target))
        moment_max = max(residuals)

        for X0 in [0.25, 0.5, 0.75]:
            def F_vals(x: np.ndarray) -> np.ndarray:
                return Ktheta_second(theta, x).dot(w)

            integral, S_X = integrate_on_interval_values(F_vals, -X0, X0, n_nodes=1001)
            E_X = integral / (2.0 * X0)

            # Approximate jets by fitting F near 0; exact moments already validate jets.
            h = min(1e-3, X0 / 200.0)
            stencil = np.arange(-80, 81, dtype=float) * h
            y = F_vals(stencil)
            deg = min(80, R + 12)
            coeffs = np.polynomial.polynomial.polyfit(stencil, y, deg)
            jets = []
            for r in range(R + 1):
                jets.append(math.factorial(r) * coeffs[r])
            jet_max = float(np.max(np.abs(jets)))

            rows.append({
                "control": "sine_quadrature_negative",
                "R": R,
                "N": N,
                "X0": X0,
                "moment_max": moment_max,
                "jet_max_fit_proxy": jet_max,
                "E_X": E_X,
                "S_X": S_X,
                "classification": "pass" if moment_max < 1e-12 and E_X < 1e-3 else "check",
            })

    path = os.path.join(outdir, "negative_control.csv")
    write_csv(path, rows)
    return rows

# ----------------------------
# Singular controls
# ----------------------------

def Q_single(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + x * x)

def Q_single_second(x: np.ndarray) -> np.ndarray:
    return 2.0 * (3.0 * x * x - 1.0) / ((1.0 + x * x) ** 3)

def Q_single_fourth(x: np.ndarray) -> np.ndarray:
    return 24.0 * (1.0 - 10.0 * x * x + 5.0 * x ** 4) / ((1.0 + x * x) ** 5)

def singular_gate2_mass_single(c: float, X0: float = 5.0, n_nodes: int = 2001) -> Tuple[float, float]:
    """
    Single packet q(gamma+c x)=c^-1 Q(x). dm = c dx.
    u=q''=c^-3 Q''
    q4=c^-5 Q^(4)
    Gamma_G = u - 6q + 2q^3
    Gamma_G2 = (1-q^2)u - q4/6
    Returns gate2 mass and scaled mass * c^15.
    """
    xs, ws = leggauss(n_nodes)
    x = X0 * xs
    q = (c ** -1) * Q_single(x)
    u = (c ** -3) * Q_single_second(x)
    q4 = (c ** -5) * Q_single_fourth(x)
    gamma_g = u - 6.0 * q + 2.0 * q ** 3
    gamma_g2 = (1.0 - q ** 2) * u - q4 / 6.0
    integrand = u ** 2 * (gamma_g ** 2 + gamma_g2 ** 2)
    # integral over m: dm = c dx = c * X0 * ds
    mass = c * X0 * float(np.sum(ws * integrand))
    return mass, mass * (c ** 15)

def run_singular_controls(outdir: str) -> List[Dict]:
    rows: List[Dict] = []
    for c in [1e-2, 1e-3, 1e-4]:
        mass, scaled = singular_gate2_mass_single(c)
        rows.append({
            "control": "singular_single_packet_dominance",
            "c": c,
            "gate2_mass": mass,
            "gate2_mass_times_c15": scaled,
            "expected_scaling": "mass ~ c^-15",
            "classification": "pass" if math.isfinite(mass) and scaled > 0 else "check",
        })
    path = os.path.join(outdir, "singular_control.csv")
    write_csv(path, rows)
    return rows

# ----------------------------
# Zeta zeros
# ----------------------------

def load_or_generate_zeros(outdir: str, n_zeros: int, dps: int = 50) -> List[float]:
    """
    Load zeros from CSV if present, otherwise generate via mpmath.zetazero.
    File path: outdir/zeros_N.csv
    """
    path = os.path.join(outdir, f"zeros_{n_zeros}.csv")
    if os.path.exists(path):
        vals = []
        with open(path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                vals.append(float(row["gamma"]))
        return vals

    mp.mp.dps = dps
    rows = []
    vals = []
    for n in range(1, n_zeros + 1):
        z = mp.zetazero(n)
        gamma = float(mp.im(z))
        vals.append(gamma)
        rows.append({"index": n, "gamma": gamma})
        if n % 50 == 0:
            print(f"generated zero {n}/{n_zeros}: gamma={gamma}")

    write_csv(path, rows)
    return vals

def K2_poisson_values(points: np.ndarray, gammas: np.ndarray, eps: float) -> np.ndarray:
    """
    Sum K2 over gammas at all points.
    K2 = 2 eps (3x^2 - eps^2)/(x^2 + eps^2)^3.
    """
    x = points[:, None] - gammas[None, :]
    den = x * x + eps * eps
    vals = 2.0 * eps * (3.0 * x * x - eps * eps) / (den ** 3)
    return np.sum(vals, axis=1)

def select_zeros(zeros: Sequence[float], m0: float, W: float) -> np.ndarray:
    return np.array([g for g in zeros if abs(g - m0) <= W], dtype=float)

def integrate_zero_proxy(zeros: Sequence[float],
                         m0: float,
                         Delta: float,
                         eps: float,
                         W: float,
                         n_nodes: int = 257) -> Tuple[float, float, int]:
    gammas = select_zeros(zeros, m0, W)
    if len(gammas) == 0:
        return float("nan"), float("nan"), 0

    xs, ws = leggauss(n_nodes)
    pts = m0 + Delta * xs
    vals = K2_poisson_values(pts, gammas, eps)
    integral = Delta * float(np.sum(ws * vals * vals))
    E_I = integral / (2.0 * Delta)
    S_I = float(np.max(np.abs(vals)))
    return E_I, S_I, int(len(gammas))

def finite_difference_jets_zero_proxy(zeros: Sequence[float],
                                      m0: float,
                                      Delta: float,
                                      eps: float,
                                      W: float,
                                      R: int,
                                      h_factor: float = 1e-3) -> Tuple[float, float]:
    gammas = select_zeros(zeros, m0, W)
    if len(gammas) == 0:
        return float("nan"), float("nan")

    h = h_factor * Delta
    radius = max(R + 8, 20)
    offsets = np.arange(-radius, radius + 1, dtype=float) * h
    pts = m0 + offsets
    vals = K2_poisson_values(pts, gammas, eps)

    deg = min(2 * radius, R + 12)
    coeffs = np.polynomial.polynomial.polyfit(offsets, vals, deg)
    jets = []
    for r in range(R + 1):
        deriv = math.factorial(r) * coeffs[r]
        jets.append((Delta ** r) * deriv)
    jets = np.array(jets, dtype=float)
    return float(np.max(np.abs(jets))), float(np.sqrt(np.mean(jets * jets)))

# ----------------------------
# Center generation
# ----------------------------

def make_centers(zeros: Sequence[float],
                 start_index: int,
                 end_index: int,
                 random_count: int = 100,
                 seed: int = 0) -> List[Tuple[str, float, Optional[int]]]:
    """
    start_index/end_index are 1-based zeta zero indices.
    """
    rng = random.Random(seed)
    z = list(zeros)
    # convert to zero-based inclusive-ish bounds
    s = max(1, start_index) - 1
    e = min(len(z) - 2, end_index - 1)

    centers: List[Tuple[str, float, Optional[int]]] = []

    # gap midpoints
    for i in range(s, e):
        centers.append(("gap_midpoint", 0.5 * (z[i] + z[i + 1]), i + 1))

    # every 5th zero center
    for i in range(s, e + 1, 5):
        centers.append(("zero_center", z[i], i + 1))

    # small/large gap neighborhoods
    gaps = [(z[i + 1] - z[i], i) for i in range(s, e)]
    gaps_sorted = sorted(gaps, key=lambda t: t[0])
    k = max(1, int(0.05 * len(gaps_sorted)))
    for label, subset in [("small_gap", gaps_sorted[:k]), ("large_gap", gaps_sorted[-k:])]:
        for gap, i in subset:
            for eta in [0.25, 0.5, 0.75]:
                centers.append((label, z[i] + eta * gap, i + 1))

    # random centers
    lo, hi = z[s], z[e]
    for _ in range(random_count):
        centers.append(("random", rng.uniform(lo, hi), None))

    return centers

# ----------------------------
# Actual-zero proxy scan
# ----------------------------

def run_actual_zero_proxy_scan(outdir: str,
                               n_zeros: int,
                               start_index: int,
                               end_index: int,
                               smoke: bool = False) -> List[Dict]:
    zeros = load_or_generate_zeros(outdir, n_zeros=n_zeros)

    if smoke:
        centers = make_centers(zeros, start_index, min(start_index + 50, end_index), random_count=10)
        c_I_list = [0.5]
        kappa_list = [1.0]
        W_mult_list = [50.0]
        R_list = [4]
        n_quad_list = [257]
    else:
        centers = make_centers(zeros, start_index, end_index, random_count=100)
        c_I_list = [0.2, 0.5]
        kappa_list = [0.5, 1.0]
        W_mult_list = [25.0, 50.0, 100.0]
        R_list = [4, 8]
        n_quad_list = [257, 513]

    rows: List[Dict] = []

    for idx, (center_type, m0, ref_idx) in enumerate(centers):
        Q = math.log(m0 / (2.0 * math.pi))
        if Q <= 1.0:
            continue

        for c_I in c_I_list:
            Delta = c_I / Q
            for kappa in kappa_list:
                eps = kappa / Q
                for W_mult in W_mult_list:
                    W = W_mult / Q
                    edge_truncated = (m0 - W < zeros[0]) or (m0 + W > zeros[-1])
                    for R in R_list:
                        for n_quad in n_quad_list:
                            E_I, S_I, num_used = integrate_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                n_nodes=n_quad
                            )
                            if not math.isfinite(E_I):
                                continue

                            B_eff = -safe_log(E_I) / math.log(Q)
                            J_max, J_rms = finite_difference_jets_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                R=R
                            )

                            rows.append({
                                "run_label": "zero_kernel_only_proxy",
                                "center_type": center_type,
                                "ref_idx": ref_idx,
                                "m0": m0,
                                "Q": Q,
                                "c_I": c_I,
                                "Delta": Delta,
                                "kappa": kappa,
                                "eps": eps,
                                "W_mult": W_mult,
                                "W": W,
                                "R": R,
                                "N_quad": n_quad,
                                "num_zeros_used": num_used,
                                "edge_truncated": edge_truncated,
                                "E_I": E_I,
                                "S_I": S_I,
                                "B_eff": B_eff,
                                "J_max": J_max,
                                "J_rms": J_rms,
                            })

        if idx % 100 == 0:
            print(f"scanned centers: {idx}/{len(centers)}")

    suffix = "smoke" if smoke else "small"
    path = os.path.join(outdir, f"actual_zero_proxy_{suffix}.csv")
    write_csv(path, rows)

    # Top diagnostics
    top_path = os.path.join(outdir, f"actual_zero_proxy_{suffix}_top_by_Beff.csv")
    write_csv(top_path, summarize_top(rows, "B_eff", n=50, reverse=True))

    return rows

# ----------------------------
# Main
# ----------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["controls", "actual", "all"], default="controls")
    ap.add_argument("--outdir", default="gate1_out")
    ap.add_argument("--zeros", type=int, default=500)
    ap.add_argument("--start-index", type=int, default=50)
    ap.add_argument("--end-index", type=int, default=500)
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()

    ensure_dir(args.outdir)

    if args.mode in ("controls", "all"):
        print("Running deterministic same-scale quadrature negative control...")
        neg_rows = run_negative_control(args.outdir)
        print(f"Wrote {len(neg_rows)} rows to negative_control.csv")
        for r in neg_rows[:3]:
            print(r)

        print("Running singular dominance control...")
        sing_rows = run_singular_controls(args.outdir)
        print(f"Wrote {len(sing_rows)} rows to singular_control.csv")
        for r in sing_rows:
            print(r)

    if args.mode in ("actual", "all"):
        print("Running actual-zero zero-kernel-only proxy scan...")
        rows = run_actual_zero_proxy_scan(
            outdir=args.outdir,
            n_zeros=args.zeros,
            start_index=args.start_index,
            end_index=args.end_index,
            smoke=args.smoke,
        )
        print(f"Wrote {len(rows)} rows to actual_zero_proxy CSV")
        top = summarize_top(rows, "B_eff", n=10, reverse=True)
        print("Top rows by B_eff:")
        for r in top:
            print({
                "center_type": r.get("center_type"),
                "m0": r.get("m0"),
                "Q": r.get("Q"),
                "c_I": r.get("c_I"),
                "kappa": r.get("kappa"),
                "W_mult": r.get("W_mult"),
                "R": r.get("R"),
                "N_quad": r.get("N_quad"),
                "E_I": r.get("E_I"),
                "B_eff": r.get("B_eff"),
                "J_max": r.get("J_max"),
                "num_zeros_used": r.get("num_zeros_used"),
                "edge_truncated": r.get("edge_truncated"),
            })

if __name__ == "__main__":
    main()
```

Suggested run sequence:

```bash
# 1. Controls
python gate1_pilot.py --mode controls --outdir gate1_out

# 2. Very small actual-zero smoke test
python gate1_pilot.py --mode actual --outdir gate1_out --zeros 150 --start-index 50 --end-index 120 --smoke

# 3. Small actual-zero pilot
python gate1_pilot.py --mode actual --outdir gate1_out --zeros 500 --start-index 50 --end-index 500
```

After running, send back:

```text
gate1_out/negative_control.csv
gate1_out/singular_control.csv
gate1_out/actual_zero_proxy_smoke.csv
gate1_out/actual_zero_proxy_smoke_top_by_Beff.csv
```

or paste the printed “Top rows by B_eff” section.
## User (2026-04-26 16:45:38)

here's some initial results

## Assistant (2026-04-26 16:46:39)

_Thought for 59s_

## Initial readout

The controls passed, and the actual-zero smoke scan shows **no Gate 1 warning**.

The main actual-zero proxy result:

\[
\max B_I^{\rm eff}=1.412,\qquad
\min E_I=0.1847,
\]

with the best row still having

\[
J_{\max}\approx0.421,
\]

so the scan did **not** find simultaneous interval flatness and finite-jet flatness.

That is healthy for Gate 1, within the limits of this being a **zero-kernel-only proxy**.

---

## 1. Negative control

The deterministic sine quadrature control worked.

Moment residuals are at floating-point noise:

\[
\max |\text{moment residual}|\sim 10^{-15}.
\]

The energy collapse is clear, especially for higher \(R\):

| \(R\) | \(X_0\) | \(E_X\) | \(S_X\) |
|---:|---:|---:|---:|
| 12 | 0.25 | \(2.23\times10^{-30}\) | \(1.15\times10^{-14}\) |
| 12 | 0.50 | \(9.68\times10^{-14}\) | \(2.32\times10^{-6}\) |
| 12 | 0.75 | \(1.94\times10^{-4}\) | \(9.91\times10^{-2}\) |
| 24 | 0.50 | \(2.09\times10^{-27}\) | \(4.66\times10^{-13}\) |
| 40 | 0.75 | \(5.65\times10^{-17}\) | \(9.61\times10^{-8}\) |

One caveat: `jet_max_fit_proxy` is garbage for high \(R\) because polynomial fitting high derivatives is ill-conditioned and factorial-weighted. The reliable checks here are `moment_max`, \(E_X\), and \(S_X\). For the negative control, compute jets analytically from the sine moments, not by polynomial fit.

Verdict:

\[
\boxed{\text{Negative control passed. The harness can detect source collapse.}}
\]

---

## 2. Singular control

Passed exactly as expected:

| \(c\) | Gate 2 mass | mass \(\times c^{15}\) |
|---:|---:|---:|
| \(10^{-2}\) | \(3.91\times10^{30}\) | \(3.914\) |
| \(10^{-3}\) | \(3.91\times10^{45}\) | \(3.913\) |
| \(10^{-4}\) | \(3.91\times10^{60}\) | \(3.913\) |

So the scaling

\[
\int |u|^2(\Gamma_G^2+\Gamma_{G,2}^2)\,dm\asymp c^{-15}
\]

is confirmed.

Verdict:

\[
\boxed{\text{Singular dominance is harmless; it gives huge Gate 2 mass.}}
\]

---

## 3. Actual-zero smoke scan

The smoke scan has 83 rows. Summary:

| Metric | Value |
|---|---:|
| rows | 83 |
| max \(B_I^{\rm eff}\) | 1.4118 |
| min \(B_I^{\rm eff}\) | -6.5803 |
| avg \(B_I^{\rm eff}\) | -3.1629 |
| min \(E_I\) | 0.1847 |
| max \(E_I\) | 4371.44 |
| rows with \(B_I^{\rm eff}>0\) | 9 |
| rows with \(B_I^{\rm eff}>1\) | 5 |
| rows with \(B_I^{\rm eff}>2\) | 0 |
| rows with \(E_I<1\) | 9 |
| rows with \(J_{\max}<1\) | 9 |
| rows with \(J_{\max}<0.1\) | 0 |

Best row:

\[
B_I^{\rm eff}=1.4118,\quad
E_I=0.1847,\quad
J_{\max}=0.4212,\quad
S_I=0.4528.
\]

This is **not** a source-flat candidate. It is mildly low energy, but nowhere near a quadrature-like collapse, and the finite jets are not small.

By center type:

| center type | count | avg \(B_I^{\rm eff}\) | max \(B_I^{\rm eff}\) | min \(E_I\) |
|---|---:|---:|---:|---:|
| gap_midpoint | 50 | -2.339 | 1.412 | 0.185 |
| large_gap | 6 | -0.739 | 1.412 | 0.185 |
| random | 10 | -3.517 | 1.166 | 0.248 |
| small_gap | 6 | -5.676 | -5.649 | \(1.0\times10^3\) |
| zero_center | 11 | -6.536 | -6.505 | \(1.81\times10^3\) |

Zero-centered intervals are predictably huge because the mollified critical-line kernel dominates. They should remain tagged as regularization tests, not Gate 1 evidence.

Verdict:

\[
\boxed{\text{No actual-zero proxy evidence of Gate 1 failure in this smoke run.}}
\]

---

## 4. Interpretation

This result is encouraging but weak:

\[
\text{quadrature control collapses strongly, actual-zero proxy does not.}
\]

That is exactly what we wanted from the first smoke test.

But it is still only a proxy because:

\[
B_2=0,
\]

critical-line zeros are mollified with

\[
\varepsilon=\kappa/Q,
\]

and the canonical completed-phase normalization has not yet been used.

So the right conclusion is:

\[
\boxed{\text{Gate 1 remains numerically plausible in this smoke proxy.}}
\]

Not:

\[
\text{Gate 1 is verified.}
\]

---

## 5. Recommended next run

Run the expanded scan, but avoid wasting work on zero-centered rows for now.

Suggested command shape:

```bash
python gate1_pilot.py --mode actual --outdir gate1_out_expanded --zeros 500 --start-index 50 --end-index 500
```

Then send:

```text
actual_zero_proxy_small_top_by_Beff.csv
actual_zero_proxy_small.csv
```

Suggested refinement before rerun:

1. Keep primary evidence to `gap_midpoint`, `large_gap`, `small_gap`, and `random`.
2. Add \(R=8\) and \(R=12\).
3. Add \(\kappa=0.25,0.5,1.0\).
4. Add tail windows \(25/Q,50/Q,100/Q\).
5. For top rows only, rerun with \(N_{\rm quad}=1025\).

Candidate threshold remains:

\[
B_I^{\rm eff}>5,\qquad
J_{\max}\le Q^{-3},
\]

plus tail/quadrature/regularization stability.

Current best row has:

\[
B_I^{\rm eff}=1.41,
\]

so it is not close.
## User (2026-04-26 17:20:38)

we've updated your scripts. please check them:

  - Math Q stays as log(m0 / (2π)) — already the unified definition. (Agent3 was the source of this choice.)
  - Centers make_centers renamed:
    - zero_center → zero_ordinate
    - small_gap (q25/0.5/0.75 sub-positions) → small_gap_midpoint (only midpoint kept)
    - large_gap (q25/0.5/0.75 sub-positions) → large_gap_midpoint (only midpoint kept)
    - gap_midpoint, random unchanged
    - added uniform family (linspace, gated by new --uniform-count)
  - Schema _PROXY_FIELDNAMES rewritten to the unified 17-column ScanRow:
    - dropped run_label, ref_idx, Delta, eps, W (absolute), edge_truncated
    - renamed W_mult → W_factor, N_quad → nquad, R → R_jet, num_zeros_used → local_zero_count
    - added J_rms, tail_drift_rel, quad_drift_rel, status
  - Drift + status added _process_center now computes tail_drift_rel (re-integrate at 2*W_factor) and quad_drift_rel (re-integrate at nquad/2), then runs
  _classify_row (agent1 thresholds) to populate status.
  - Param hash added _zeros_content_hash, compute_params_hash, and derive_output_path matching agent1's signatures. _param_hash (old 8-char SHA1 of grid only)
  removed.
  - Filename changed from actual_zero_proxy_<suffix>_<8hex>.csv (underscore + 8 chars) to actual_zero_proxy_<suffix>.<12hash>.csv (dot + 12 chars). Top-by-Beff
  sidecar uses the same convention.
  - Resume key _load_done_centers (keyed (center_type, m0)) replaced with _load_done_keys (full unified row key including c_I, kappa, W_factor, nquad, R_jet).
  The center-skip logic in run_actual_zero_proxy_scan was rewritten to skip a center only when every (c_I, kappa, W_factor, R_jet, nquad) tuple for that center
  is already present.
  - _load_existing_rows field-type sets updated to the new column names (drops ref_idx, R, N_quad, num_zeros_used, Delta, eps, W_mult, W, edge_truncated; adds
  nquad, R_jet, local_zero_count, tail_drift_rel, quad_drift_rel).
  - CLI flags added: --no-resume, --seed, --random-count, --uniform-count, --hash-len. --resume is on by default.
  - Top-N print rebuilt to use the unified column names (status, c_I, kappa, W_factor, R_jet, nquad, tail_drift_rel, quad_drift_rel, local_zero_count) instead of
   W_mult, R, N_quad, num_zeros_used, edge_truncated.
  - Untouched: BLAS pinning was already there. The log() helper was already there. The negative_control.csv and singular_control.csv schemas (with their own
  classification column) are intentionally unchanged — controls stay separate from the unified actual-zero ScanRow.

## Assistant (2026-04-26 17:20:39)

I’ll review the updated script against the intended scan semantics, not the RH strategy. I’ll check for schema/resume/hash correctness, numerical pitfalls, and any logic bugs that could affect pilot outputs.

_Thought for 1m 8s_

Reviewed statically. The changes are mostly sound and the unified schema is much cleaner, but I see **four issues worth fixing before trusting the next run**.

## 1. Resume can duplicate partially completed centers

You replaced center-level resume with full row keys, which is directionally correct. But the current skip logic only skips a center if **all** parameter tuples for that center are already done. If a previous run was interrupted halfway through a center, the rerun recomputes **all** rows for that center and appends duplicates for the already completed tuples.

Current logic checks `all_done` at the center level, then sends the full center task to `_process_center`. The worker has no `done_keys` filter. 

Fix: either split work into row-level tasks, or filter worker results before writing:

```python
for row in result:
    if _row_key(row) in done_keys:
        continue
    writer.writerow(row)
    done_keys.add(_row_key(row))
    rows.append(row)
```

Then remove the unconditional `rows.extend(result)`.

## 2. Multiprocessing will break on Windows unless `fork` is available

The script hardcodes:

```python
ctx = mp_proc.get_context("fork")
```

That is fine on Linux/macOS with fork support, but it will fail on Windows. Since you may run this locally from Windows, make it portable:

```python
method = "fork" if "fork" in mp_proc.get_all_start_methods() else "spawn"
ctx = mp_proc.get_context(method)
```

The worker initializer already passes the zero list, so `spawn` should work, just with more overhead.

## 3. `np.exceptions.RankWarning` may fail on older NumPy

This line is version-sensitive:

```python
warnings.filterwarnings("ignore", category=np.exceptions.RankWarning)
```

Some NumPy versions expose `RankWarning` differently. Safer:

```python
try:
    rank_warning = np.exceptions.RankWarning
except AttributeError:
    rank_warning = np.RankWarning

warnings.filterwarnings("ignore", category=rank_warning)
```

This is a startup-risk issue, not a math issue. 

## 4. Smoke-run hash does not reflect effective smoke parameters

In smoke mode, the script uses:

```python
centers = make_centers(
    zeros,
    start_index,
    min(start_index + 50, end_index),
    random_count=10,
    ...
)
```

but `compute_params_hash` receives the original `end_index` and `random_count`. So the hash can change when the actual smoke rows do not, or fail to reflect the effective center-generation parameters. The center-generation rename itself looks good: `zero_ordinate`, `small_gap_midpoint`, `large_gap_midpoint`, `gap_midpoint`, `random`, and optional `uniform` are implemented as described. 

Fix by computing effective values first:

```python
if smoke:
    effective_end_index = min(start_index + 50, end_index)
    effective_random_count = 10
else:
    effective_end_index = end_index
    effective_random_count = random_count
```

Then use those in both `make_centers` and `compute_params_hash`.

---

## Classification concern

The current classifier marks `candidate_proxy_flat` based only on:

```python
B_eff > 10
```

without requiring small `J_max`; only `serious_proxy_warning` checks `J_max < 1e-8`. Since the whole point is simultaneous interval and finite-jet flatness, I would make `candidate_proxy_flat` require a jet condition too:

```python
if B_eff > 20 and J_max < 1e-8:
    return "serious_proxy_warning"
if B_eff > 10 and J_max < 1e-6:
    return "candidate_proxy_flat"
if B_eff > 5:
    return "watch"
```

Otherwise a high-energy/low-integration artifact could be overclassified.

---

## Operational concern: tail-edge truncation is no longer visible

You dropped `edge_truncated`, which is fine for the unified 17-column schema, but the computation still needs to avoid false stability when `2*W_factor/Q` extends beyond available zeros. The current `tail_drift_rel` compares \(W\) and \(2W\), but if the data edge truncates both windows, the drift can look stable for the wrong reason.

Since the schema is fixed, fold this into `status`:

```python
tail_edge = (m0 - W2 < zeros[0]) or (m0 + W2 > zeros[-1])
if tail_edge:
    status = "reject_tail_edge"
else:
    status = _classify_row(...)
```

This matters most for smoke and low-zero-count runs.

---

## Things that look good

The unified field names are consistent in `_PROXY_FIELDNAMES`, row production, CSV loading, and top-N printing. The \(Q=\log(m_0/2\pi)\) definition is preserved. The new center names are implemented correctly, and keeping only midpoint subpositions for small/large gaps is a good simplification. The dot-plus-12-hash filename convention is implemented correctly via `derive_output_path`. 

Controls staying outside the unified actual-zero schema is fine; `negative_control.csv` and `singular_control.csv` have different semantics.

## Minimal patch priority

Apply these in order:

1. Portable multiprocessing context.
2. Resume duplicate filter.
3. NumPy `RankWarning` compatibility.
4. Tail-edge rejection status.
5. Smoke effective-parameter hash.
6. Candidate classification requires `J_max`.

After that, the script is ready for the expanded proxy run.
## User (2026-04-26 17:40:54)

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

## Assistant (2026-04-26 17:41:27)

_Thought for 31s_

Static review: **yes, the fixes I flagged are now in `gate1_pilot.py`**.

Confirmed in the updated file:

- `tail_edge` is now persisted in the unified proxy schema, written per row, parsed on load, and included in classification. The schema is now 18 columns as intended. turn42file1
- `schema_version` is bumped to `2`, so new runs get fresh hash slugs and do not collide with old v1 CSVs. 
- Candidate classification now rejects `tail_edge` first and requires `J_max < 1e-6` for `candidate_proxy_flat`. Good. 
- Resume dedupe is now row-level at write time via `seen_keys`, so interrupted partial centers should no longer duplicate rows on resume. 
- Multiprocessing start method is now portable: `fork` when available, otherwise `spawn`. 
- Smoke effective parameters are now resolved before hashing, so the hash matches actual generated rows. 
- `RankWarning` compatibility is guarded across NumPy versions. 
- Center names and family changes are present: `zero_ordinate`, `small_gap_midpoint`, `large_gap_midpoint`, `gap_midpoint`, `random`, and optional `uniform`. 

One minor optional improvement: include `tail_edge` in the printed Top-N summary, not just in the CSV. The CSV has it, so this is only for console ergonomics.

```python
"tail_edge": r.get("tail_edge"),
```

I tried a local `py_compile` in the sandbox, but the execution environment timed out again before returning, so this is a **static review**, not a runtime validation.

Verdict: **good to run.** Suggested smoke command:

```bash
python gate1_pilot.py --mode actual --outdir gate1_out_v2 --zeros 150 --start-index 50 --end-index 120 --smoke --workers 1 --no-resume
```

Then run controls and the small scan after the smoke output looks sane.
## User (2026-04-26 17:49:55)

Edits made, please re-check holistically

## Assistant (2026-04-26 17:49:58)

I’ll do a final static pass against the updated file: correctness of the fixes, runtime risks, and anything that could distort scan interpretation.

_Thought for 11s_

Holistic static review: **the previously flagged fixes are now in, and the script is good to run.** I do not see any blocking issue in the updated `gate1_pilot.py`. 

Confirmed:

- `tail_edge` is now in the persisted schema and in Top-N console output.
- `schema_version` is now `2`, so new CSVs get fresh hash slugs.
- `candidate_proxy_flat` now requires both high \(B_I^{\rm eff}\) and small `J_max`.
- `reject_tail_edge` is classified before tail/quad drift.
- Resume dedupe is row-level via `seen_keys`, so partial interrupted centers should not duplicate already-written rows.
- Multiprocessing now uses `fork` only if available, otherwise `spawn`.
- Smoke effective params are resolved before hashing.
- `RankWarning` compatibility is guarded.
- Center names are unified: `zero_ordinate`, `gap_midpoint`, `small_gap_midpoint`, `large_gap_midpoint`, `random`, `uniform`.
- Top-N print now includes `tail_edge`.

Minor non-blocking notes:

1. `finite_difference_jets_zero_proxy` still uses polynomial fitting, so `J_max` can be noisy for higher \(R\). For pilot screening this is acceptable; for any candidate, rerun jets with analytic kernel derivatives or automatic differentiation.

2. The default `workers=max(1, cpu_count-2)` may be aggressive on Windows because `spawn` copies more state. For the first v2 smoke/small run, I would use `--workers 1` or a small explicit value like `--workers 4`.

3. If you later load old v1 CSVs manually, `tail_edge` defaults to `False`; that is fine because v2 filenames are hash-separated by `schema_version: 2`.

Recommended run sequence:

```bash
python gate1_pilot.py --mode controls --outdir gate1_out_v2
python gate1_pilot.py --mode actual --outdir gate1_out_v2 --zeros 150 --start-index 50 --end-index 120 --smoke --workers 1 --no-resume
python gate1_pilot.py --mode actual --outdir gate1_out_v2 --zeros 500 --start-index 50 --end-index 500 --workers 4 --no-resume
```

Verdict: **ready for the next pilot run.**
## User (2026-04-26 17:55:27)

Do the agent instruction in the message as per your agent number.

## Assistant (2026-04-26 17:55:28)

I’ll do the Agent 3 rerun task as a targeted watch-interval stress test. I’ll use the listed watch centers and focus on whether their low energy survives width, regularization, tail-window, and jet-depth changes.

_Thought for 4m 6s_

## Agent 3 / C — Watch-interval rerun plan and provisional classification

The requested Agent 3 task is to stress-test the existing watch intervals, not re-audit Gate 1. The relevant watch centers are:

\[
m_0\approx 27.7179,\quad 109.099,\quad 171.662,\quad 199.640.
\]

The goal is to decide whether their low proxy energy is genuine local flattening, a smooth gap-midpoint effect, \(\varepsilon\)-regularization dependence, or low-\(Q\) artifact. 

I could not complete a reliable local rerun in this environment, so below is the concrete rerun grid, classification logic, and provisional status based on the previous smoke outputs.

---

# 1. Rerun grid for each watch interval

For each \(m_0\), rerun:

\[
c_I\in\{0.025,0.05,0.1,0.2,0.5,1.0\},
\]

\[
\kappa\in\{0.0625,0.125,0.25,0.5,1.0,2.0\},
\]

\[
R\in\{4,8,12,16\}.
\]

Use absolute tail windows if enough zero data is available:

\[
W\in\{20,50,100,200,500\}.
\]

If the zero table is too short, mark `tail_edge=True` and do not classify the row as a candidate.

For each row compute:

\[
E_I,\quad B_I^{\rm eff},\quad S_I,\quad J_{\max},\quad J_{\rm rms},
\]

plus:

\[
D_{\tail},\quad D_{\quad},\quad D_{\rm reg},\quad D_{\rm width}.
\]

---

# 2. Candidate criterion

A watch interval only upgrades to a candidate if all of these hold:

\[
B_I^{\rm eff}>5,
\]

\[
J_{\max}\le Q^{-5},
\]

\[
D_{\tail}<10^{-4},
\]

\[
D_{\quad}<10^{-5},
\]

\[
D_{\rm reg}<10^{-2},
\]

and the effect persists for at least two nearby interval widths \(c_I\).

Anything that fails the jet condition is not a source-flat candidate, even if \(E_I\) is low.

---

# 3. Provisional classification of known watch centers

| \(m_0\) | Approx. \(Q=\log(m_0/2\pi)\) | Current concern | Provisional status |
|---:|---:|---|---|
| 27.7179 | 1.48 | Very low \(Q\); \(B_I^{\rm eff}\) is not asymptotically meaningful | reject as low-\(Q\) / calibration-only |
| 109.099 | 2.85 | Mild low-energy gap-midpoint behavior; needs width/reg check | watch |
| 171.662 | 3.31 | Mild low-energy gap-midpoint behavior; not yet jet-flat | watch |
| 199.640 | 3.46 | Mild low-energy gap-midpoint behavior; not yet jet-flat | watch |

None of these should currently be called a candidate. In the previous smoke scan, the best row had roughly:

\[
B_I^{\rm eff}\approx 1.41,\qquad E_I\approx0.185,\qquad J_{\max}\approx0.42,
\]

which is far from the candidate threshold.

---

# 4. Interpretation rules for the rerun

## A. Genuine local flattening

Would require:

\[
E_I\ll1
\]

and

\[
J_r\approx0,\qquad 0\le r\le R,
\]

stably across \(W,\kappa,c_I\).

Expected classification:

\[
\texttt{candidate\_flat}
\quad\text{or}\quad
\texttt{serious\_proxy\_warning}.
\]

## B. Smooth gap-midpoint effect

Likely if:

\[
E_I
\]

is moderately low at gap midpoints, but:

\[
J_{\max}
\]

is not small, or the effect disappears under \(c_I\) changes.

Expected classification:

\[
\texttt{watch}
\rightarrow
\texttt{healthy}.
\]

## C. \(\varepsilon\)-regularization artifact

Likely if:

\[
E_I(\kappa)
\]

changes substantially across:

\[
\kappa=0.0625,\ldots,2.0.
\]

Expected classification:

\[
\texttt{reject\_regularization}.
\]

## D. Low-\(Q\) artifact

Likely for \(m_0\approx27.7179\), because:

\[
Q\approx1.48.
\]

Expected classification:

\[
\texttt{reject\_low\_Q}
\]

or keep only as calibration.

---

# 5. Target output table

For each \(m_0\), the rerun summary should look like:

| \(m_0\) | best \(B_I^{\rm eff}\) | best \(E_I\) | best \(J_{\max}\) | stable \(W\)? | stable \(\kappa\)? | stable \(c_I\)? | classification |
|---:|---:|---:|---:|---|---|---|---|
| 27.7179 | — | — | — | — | — | — | low-\(Q\) calibration |
| 109.099 | fill | fill | fill | yes/no | yes/no | yes/no | healthy/watch/candidate |
| 171.662 | fill | fill | fill | yes/no | yes/no | yes/no | healthy/watch/candidate |
| 199.640 | fill | fill | fill | yes/no | yes/no | yes/no | healthy/watch/candidate |

Also include a matched comparison for each center:

\[
m_0^{\rm random}\approx m_0+\eta/Q
\]

and a deterministic quadrature control at matched \(Q,c_I\).

---

# 6. Verdict before rerun

Current evidence supports:

\[
\boxed{\text{healthy/watch, not candidate.}}
\]

The known watch intervals are not quadrature-like yet. They have modestly low proxy energy but do not show simultaneous interval and finite-jet collapse. The decisive check is whether any row survives:

\[
R=12,16,
\quad
\kappa\text{-sweep},
\quad
W\text{-sweep},
\quad
c_I\text{-sweep}.
\]

If no watch interval achieves:

\[
B_I^{\rm eff}>5
\quad\text{and}\quad
J_{\max}\le Q^{-5},
\]

then this branch remains numerically favorable to Gate 1.
## User (2026-04-26 18:00:30)

ok does this re-run use your previous script? if so, give me the parameters to run. if changes in the script are needed, give me those too

## Assistant (2026-04-26 18:00:42)

_Thought for 7s_

Yes: the broad expanded scan uses the previous `gate1_pilot.py`.

But the **targeted watch-interval rerun I described does not fit the current script exactly**, because the current script has:

- fixed parameter grids for `smoke` / `small`;
- generated centers only, not explicit `m0` watch centers;
- tail windows expressed as `W = W_factor / Q`, not absolute windows like `W=20,50,100,200,500`.

So you have two options.

## Option A — Run the existing script as-is

This gives the expanded generic scan, not the targeted watch rerun:

```bash
python gate1_pilot.py \
  --mode actual \
  --outdir gate1_out_v2 \
  --zeros 500 \
  --start-index 50 \
  --end-index 500 \
  --workers 4 \
  --no-resume
```

For a more conservative first pass:

```bash
python gate1_pilot.py \
  --mode actual \
  --outdir gate1_out_v2 \
  --zeros 500 \
  --start-index 50 \
  --end-index 500 \
  --workers 1 \
  --no-resume
```

This will use the current hardcoded small-grid:

\[
c_I\in\{0.2,0.5\},\quad
\kappa\in\{0.5,1.0\},\quad
W_{\rm factor}\in\{25,50\},\quad
R=4,\quad
nquad=257.
\]

Useful, but not enough for the watch rerun.

---

## Option B — Add a small targeted watch-rerun script

Create this file next to `gate1_pilot.py` as:

```bash
gate1_watch_rerun.py
```

Then run it against the same zero cache/output folder.

```python
#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import math
import os
from typing import Dict, List

from gate1_pilot import (
    ensure_dir,
    load_or_generate_zeros,
    integrate_zero_proxy,
    finite_difference_jets_zero_proxy,
    _classify_row,
    _rel_diff,
    safe_log,
    write_csv,
)

WATCH_CENTERS = [27.7179, 109.099, 171.662, 199.640]

def run_watch_rerun(
    outdir: str,
    n_zeros: int,
    centers: List[float],
    c_I_values: List[float],
    kappa_values: List[float],
    W_abs_values: List[float],
    R_values: List[int],
    nquad_values: List[int],
) -> List[Dict]:
    ensure_dir(outdir)
    zeros = load_or_generate_zeros(outdir, n_zeros=n_zeros)

    rows: List[Dict] = []

    for m0 in centers:
        Q = math.log(m0 / (2.0 * math.pi))
        if Q <= 1.0:
            print(f"Skipping m0={m0}: Q={Q:.4f} <= 1")
            continue

        for c_I in c_I_values:
            Delta = c_I / Q

            for kappa in kappa_values:
                eps = kappa / Q

                for W_abs in W_abs_values:
                    W = W_abs
                    W2 = 2.0 * W_abs
                    tail_edge = (m0 - W2 < zeros[0]) or (m0 + W2 > zeros[-1])

                    for R_jet in R_values:
                        for nquad in nquad_values:
                            E_I, S_I, local_zero_count = integrate_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                n_nodes=nquad,
                            )
                            if not math.isfinite(E_I):
                                continue

                            E_half, _, _ = integrate_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                n_nodes=max(32, nquad // 2),
                            )
                            quad_drift_rel = (
                                _rel_diff(E_I, E_half)
                                if math.isfinite(E_half)
                                else float("nan")
                            )

                            E_2W, _, _ = integrate_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W2,
                                n_nodes=nquad,
                            )
                            tail_drift_rel = (
                                _rel_diff(E_I, E_2W)
                                if math.isfinite(E_2W)
                                else float("nan")
                            )

                            J_max, J_rms = finite_difference_jets_zero_proxy(
                                zeros=zeros,
                                m0=m0,
                                Delta=Delta,
                                eps=eps,
                                W=W,
                                R=R_jet,
                            )

                            B_eff = -safe_log(E_I) / math.log(Q)

                            status = _classify_row(
                                B_eff=B_eff,
                                J_max=J_max,
                                tail_drift_rel=tail_drift_rel,
                                quad_drift_rel=quad_drift_rel,
                                tail_edge=tail_edge,
                            )

                            rows.append({
                                "center_type": "watch_center",
                                "m0": m0,
                                "Q": Q,
                                "c_I": c_I,
                                "Delta": Delta,
                                "kappa": kappa,
                                "eps": eps,
                                "W_abs": W_abs,
                                "W_factor_equiv": W_abs * Q,
                                "nquad": nquad,
                                "R_jet": R_jet,
                                "local_zero_count": local_zero_count,
                                "E_I": E_I,
                                "S_I": S_I,
                                "B_eff": B_eff,
                                "J_max": J_max,
                                "J_rms": J_rms,
                                "tail_drift_rel": tail_drift_rel,
                                "quad_drift_rel": quad_drift_rel,
                                "tail_edge": tail_edge,
                                "status": status,
                            })

        print(f"Finished watch center m0={m0}")

    out_path = os.path.join(outdir, "watch_rerun.csv")
    write_csv(out_path, rows)

    top = sorted(
        [r for r in rows if math.isfinite(float(r["B_eff"]))],
        key=lambda r: float(r["B_eff"]),
        reverse=True,
    )[:50]
    write_csv(os.path.join(outdir, "watch_rerun_top_by_Beff.csv"), top)

    return rows

def parse_float_list(s: str) -> List[float]:
    return [float(x.strip()) for x in s.split(",") if x.strip()]

def parse_int_list(s: str) -> List[int]:
    return [int(x.strip()) for x in s.split(",") if x.strip()]

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="gate1_out_v2")
    ap.add_argument("--zeros", type=int, default=500)
    ap.add_argument(
        "--centers",
        default="27.7179,109.099,171.662,199.640",
    )
    ap.add_argument(
        "--c-I",
        default="0.025,0.05,0.1,0.2,0.5,1.0",
    )
    ap.add_argument(
        "--kappa",
        default="0.0625,0.125,0.25,0.5,1.0,2.0",
    )
    ap.add_argument(
        "--W-abs",
        default="20,50,100,200,500",
    )
    ap.add_argument(
        "--R",
        default="4,8,12,16",
    )
    ap.add_argument(
        "--nquad",
        default="257,513,1025",
    )
    args = ap.parse_args()

    rows = run_watch_rerun(
        outdir=args.outdir,
        n_zeros=args.zeros,
        centers=parse_float_list(args.centers),
        c_I_values=parse_float_list(args.c_I),
        kappa_values=parse_float_list(args.kappa),
        W_abs_values=parse_float_list(args.W_abs),
        R_values=parse_int_list(args.R),
        nquad_values=parse_int_list(args.nquad),
    )

    print(f"Wrote {len(rows)} rows.")
    print(f"CSV: {os.path.join(args.outdir, 'watch_rerun.csv')}")
    print(f"Top: {os.path.join(args.outdir, 'watch_rerun_top_by_Beff.csv')}")

if __name__ == "__main__":
    main()
```

Run:

```bash
python gate1_watch_rerun.py \
  --outdir gate1_out_watch \
  --zeros 500
```

For a fast first pass:

```bash
python gate1_watch_rerun.py \
  --outdir gate1_out_watch_fast \
  --zeros 500 \
  --c-I 0.05,0.1,0.2,0.5 \
  --kappa 0.125,0.25,0.5,1.0 \
  --W-abs 20,50,100 \
  --R 4,8,12 \
  --nquad 257,513
```

Send back:

```text
gate1_out_watch/watch_rerun_top_by_Beff.csv
gate1_out_watch/watch_rerun.csv
```

or the fast version equivalents.

## What to look for

A real concern would need all of:

\[
B_I^{\rm eff}>5,
\qquad
J_{\max}\le Q^{-5},
\qquad
\texttt{status} \notin \{\texttt{reject\_*}\}.
\]

If the best rows remain around \(B_I^{\rm eff}\sim1\)–\(2\), or `J_max` stays \(O(10^{-1})\) / \(O(1)\), the watch intervals should stay classified as healthy/watch rather than candidate.
## User (2026-04-26 18:08:45)

We did option B. 
● Watch rerun done in 70s on 10 workers. Verdict matches the upstream Agent 3 prediction — none of the four watch intervals upgrade to candidate.

  Status distribution (8,640 rows total):
  - reject_tail_edge: 6,480 (75%) — wide W_abs values exceed the zero-table coverage
  - healthy: 1,728
  - watch: 432
  - candidate_proxy_flat / serious_proxy_warning: 0

  Best post-gate row per watch center:

  ┌─────────┬──────┬────────────┬────────┬───────┬────────┬──────────────────────────┬────────────────────────┐
  │   m₀    │  Q   │ best B_eff │  E_I   │ J_max │  Q⁻⁵   │         jet test         │         status         │
  ├─────────┼──────┼────────────┼────────┼───────┼────────┼──────────────────────────┼────────────────────────┤
  │ 27.7179 │ 1.48 │ —          │ —      │ —     │ —      │ n/a — all rows tail-edge │ low-Q calibration only │
  ├─────────┼──────┼────────────┼────────┼───────┼────────┼──────────────────────────┼────────────────────────┤
  │ 109.099 │ 2.85 │ 7.25       │ 5.0e-4 │ 0.022 │ 5.3e-3 │ fails (J_max ≫ Q⁻⁵)      │ watch                  │
  ├─────────┼──────┼────────────┼────────┼───────┼────────┼──────────────────────────┼────────────────────────┤
  │ 171.662 │ 3.31 │ 5.93       │ 8.3e-4 │ 0.029 │ 2.5e-3 │ fails                    │ watch                  │
  ├─────────┼──────┼────────────┼────────┼───────┼────────┼──────────────────────────┼────────────────────────┤
  │ 199.640 │ 3.46 │ 5.38       │ 1.3e-3 │ 0.035 │ 2.0e-3 │ fails                    │ watch                  │
  └─────────┴──────┴────────────┴────────┴───────┴────────┴──────────────────────────┴────────────────────────┘

  Interpretation:
  - m₀=27.7179 falls past the lower zero-table edge with W_abs ≥ 20 (2W = 40 reaches m₀ − 12.3 < γ₁ ≈ 14.13). All 2,160 rows are reject_tail_edge. Consistent
  with the "low-Q calibration only" provisional classification.
  - m₀ ∈ {109.099, 171.662, 199.640} clear B_eff > 5 even at the tightest grid points (c_I=0.025, κ=0.0625, W_abs=20) — but J_max is one to two orders of
  magnitude above the Q⁻⁵ jet bound. Low interval energy without finite-jet collapse → smooth gap-midpoint effect, not source flatness.

  Verdict: healthy/watch, not candidate. The branch remains numerically favorable to Gate 1.

  Outputs:
  - gate1_out_watch/watch_rerun.csv (8,640 rows)
  - gate1_out_watch/watch_rerun_top_by_Beff.csv (top 50)

## Assistant (2026-04-26 18:08:52)

_Thought for 6s_

This is a good result. It confirms the earlier interpretation:

\[
\boxed{\text{The watch intervals remain watch-level only; none are Gate 1 candidates.}}
\]

The key reason is that even when \(E_I\) is low enough to produce \(B_I^{\rm eff}>5\), the finite-jet test fails:

\[
J_{\max} \gg Q^{-5}.
\]

That is exactly the distinction we needed. Low interval energy alone can occur at smooth gap midpoints; Gate 1 danger requires simultaneous interval and finite-jet flattening.

## Readout

### Status distribution

Out of 8,640 rows:

| status | count | interpretation |
|---|---:|---|
| `reject_tail_edge` | 6,480 | expected, because \(W_{\rm abs}\ge20\) with only 500 zeros often hits table edges |
| `healthy` | 1,728 | stable, non-flat |
| `watch` | 432 | low-ish \(E_I\), but not finite-jet flat |
| `candidate_proxy_flat` | 0 | no candidate |
| `serious_proxy_warning` | 0 | no serious warning |

### Best rows

| \(m_0\) | \(Q\) | best \(B_I^{\rm eff}\) | \(E_I\) | \(J_{\max}\) | \(Q^{-5}\) | verdict |
|---:|---:|---:|---:|---:|---:|---|
| 27.7179 | 1.48 | — | — | — | — | low-\(Q\), tail-edge only |
| 109.099 | 2.85 | 7.25 | \(5.0\times10^{-4}\) | 0.022 | \(5.3\times10^{-3}\) | watch |
| 171.662 | 3.31 | 5.93 | \(8.3\times10^{-4}\) | 0.029 | \(2.5\times10^{-3}\) | watch |
| 199.640 | 3.46 | 5.38 | \(1.3\times10^{-3}\) | 0.035 | \(2.0\times10^{-3}\) | watch |

The best row at \(m_0\approx109.099\) is closest, but still fails the jet criterion by about a factor of 4 relative to \(Q^{-5}\). More importantly, \(J_{\max}\sim10^{-2}\), not near a quadrature-like collapse.

## Interpretation

This supports:

\[
\boxed{\text{smooth gap-midpoint low energy, not source-flat quadrature.}}
\]

It does **not** support:

\[
\text{actual-zero proxy Gate 1 failure.}
\]

The \(m_0\approx27.7179\) branch should be discarded from evidence for now. It is too low-\(Q\), and all rows are tail-edge due to the absolute \(W\)-sweep hitting the zero-table boundary.

## Recommended next step

Run a higher-zero-count watch rerun so the absolute tail windows do not edge-reject most rows. Same script, but with more zeros:

```bash
python gate1_watch_rerun.py \
  --outdir gate1_out_watch_5000 \
  --zeros 5000 \
  --centers 109.099,171.662,199.640 \
  --c-I 0.025,0.05,0.1,0.2,0.5,1.0 \
  --kappa 0.0625,0.125,0.25,0.5,1.0,2.0 \
  --W-abs 20,50,100,200 \
  --R 4,8,12,16 \
  --nquad 257,513,1025 \
  --workers 10
```

Drop \(27.7179\). Keep \(W_{\rm abs}=500\) only if the 5,000-zero table covers it cleanly for all centers; otherwise it will just add tail-edge rows.

After that, if the same best rows remain watch-only, the existing watch branch can be demoted.
## User (2026-04-26 18:55:43)

  Best post-gate rows per center (5,184 rows):

  ┌─────────┬──────┬───────┬────────┬───────┬────────┬──────────────────────┬────────┐
  │   m₀    │  Q   │ B_eff │  E_I   │ J_max │  Q⁻⁵   │       jet test       │ status │
  ├─────────┼──────┼───────┼────────┼───────┼────────┼──────────────────────┼────────┤
  │ 109.099 │ 2.85 │ 7.25  │ 5.0e-4 │ 0.022 │ 5.3e-3 │ fails (×4 too large) │ watch  │
  ├─────────┼──────┼───────┼────────┼───────┼────────┼──────────────────────┼────────┤
  │ 171.662 │ 3.31 │ 5.93  │ 8.3e-4 │ 0.029 │ 2.5e-3 │ fails (×11)          │ watch  │
  ├─────────┼──────┼───────┼────────┼───────┼────────┼──────────────────────┼────────┤
  │ 199.640 │ 3.46 │ 5.38  │ 1.3e-3 │ 0.035 │ 2.0e-3 │ fails (×17)          │ watch  │
  └─────────┴──────┴───────┴────────┴───────┴────────┴──────────────────────┴────────┘

  These are bit-identical to the 500-zero run because the optimal config sits at W_abs=20 (tight window) — already inside the 500-zero table for all three
  centers, so the bigger zero table doesn't change those rows.

  Status distribution (5,184 rows):
  - reject_tail_edge: 3,024 (W_abs ∈ {50, 100, 200} extends past γ₁=14.13 for low m₀)
  - healthy: 1,728
  - watch: 432
  - candidate_proxy_flat / serious_proxy_warning: 0

  Confirms:
  - The watch intervals are not source-flat candidates — low interval energy without finite-jet collapse, just smooth gap-midpoint behavior.
  - The 5k-zero coverage rules out tail-table-truncation as a hidden factor: where the optimum lives (W_abs=20), the larger table doesn't change anything.
  - The earlier verdict stands: the existing watch branch can be demoted.

  Outputs:
  - gate1_out_watch_5000/watch_rerun.csv (5,184 rows)
  - gate1_out_watch_5000/watch_rerun_top_by_Beff.csv (top 50)
  - gate1_out_watch_5000/zeros_5000.csv (cached for future runs)

## Assistant (2026-04-26 18:55:44)

Confirmed. This 5k-zero rerun demotes the watch branch.

The important point is that the best configurations are **bit-identical** to the 500-zero run because they occur at:

\[
W_{\rm abs}=20,
\]

which was already fully covered by the 500-zero table for \(m_0=109.099,171.662,199.640\). So the previous result was not a tail-table artifact.

## Updated classification

| center | classification | reason |
|---:|---|---|
| \(109.099\) | watch, demoted | \(B_{\rm eff}=7.25\), but \(J_{\max}=0.022>Q^{-5}=0.0053\) |
| \(171.662\) | watch, demoted | \(J_{\max}\) fails by \(\sim 11\times\) |
| \(199.640\) | watch, demoted | \(J_{\max}\) fails by \(\sim 17\times\) |

No rows satisfy:

\[
B_I^{\rm eff}>5
\quad\text{and}\quad
J_{\max}\le Q^{-5}.
\]

No `candidate_proxy_flat`; no `serious_proxy_warning`.

## Interpretation

This supports the prior diagnosis:

\[
\boxed{\text{low interval energy at these centers is smooth gap-midpoint behavior, not source-flat quadrature.}}
\]

and:

\[
\boxed{\text{the current actual-zero proxy evidence remains favorable to Gate 1.}}
\]

## Next best run

Now move away from the hand-picked watch centers and run a broader high-count scan using the 5k cached zeros, but with less waste on tail-edge windows:

```bash
python gate1_pilot.py \
  --mode actual \
  --outdir gate1_out_5000_broad \
  --zeros 5000 \
  --start-index 500 \
  --end-index 4500 \
  --workers 10 \
  --random-count 300 \
  --uniform-count 300 \
  --no-resume
```

This avoids low table edges and tests whether new high-\(Q\) watch/candidate intervals appear.

## User (2026-04-26 18:59:04)

  46,408 rows, 5,801 centers, range m₀ ∈ [γ₅₀₀ ≈ 811, γ₄₅₀₀ ≈ 4920]

  Status distribution:
  - healthy: 46,396 (99.97%)
  - reject_tail_unstable: 12 (~0%)
  - watch, candidate_proxy_flat, serious_proxy_warning, reject_tail_edge: 0

  Rows with B_eff > 5 (the "watch" threshold): 0
  Top B_eff anywhere: 0.87 (at m₀ ≈ 897.93, Q ≈ 4.96), with J_max ≈ 0.50.

  Interpretation:
  - Across 4,000 zeros' worth of high-Q gap-midpoints, zero ordinates, gap-extreme midpoints, 300 random + 300 uniform centers, nothing crosses even the watch
  threshold (B_eff > 5) — let alone the candidate threshold (B_eff > 5 ∧ J_max ≤ Q⁻⁵).
  - The four hand-picked low-m₀ watch centers (B_eff ~ 5–7) do not generalize: at higher Q, the smooth gap-midpoint effect that produced their B_eff dies out as
  zero density grows.
  - 12 reject_tail_unstable rows are noise, not signal — they're rejected upstream.

  Verdict: the actual-zero proxy evidence is now strongly favorable to Gate 1. No new candidate intervals appear at higher Q, and the previously-watch low-Q
  intervals have been demoted. The watch branch can be removed.

  Outputs:
  - gate1_out_5000_broad/actual_zero_proxy_small.bdcb358d6dcb.csv (46,408 rows)
  - gate1_out_5000_broad/actual_zero_proxy_small_top_by_Beff.bdcb358d6dcb.csv (top 50)

## Assistant (2026-04-26 18:59:05)

This is a strong proxy result in favor of Gate 1.

The broad scan is much more informative than the four watch-center reruns because it moved to:

\[
m_0\in[\gamma_{500},\gamma_{4500}]
\approx[811,4920],
\]

with 5,801 centers and 46,408 rows. The result:

\[
\max B_I^{\rm eff}=0.87,\qquad J_{\max}\approx0.50,
\]

is nowhere near the watch threshold, let alone the candidate threshold.

## Updated numerical status

| Test branch | Result | Gate 1 implication |
|---|---|---|
| deterministic quadrature control | strong collapse detected | harness can detect the adversary |
| singular dominance control | \(c^{-15}\) scaling confirmed | singular dominance harmless |
| low-\(Q\) watch rerun | no candidate; jet test fails | watch branch demoted |
| 5k broad scan | 99.97% healthy, no watch rows | strongly favorable proxy evidence |

## Interpretation

The most important observation is that the previous low-\(Q\) watch behavior does **not** persist at higher \(Q\). If actual zeros were locally forming quadrature-like source-flat packet designs, this scan should have produced at least some elevated \(B_I^{\rm eff}\) or small-jet rows. It did not.

So the current evidence supports:

\[
\boxed{
\text{actual-zero proxy data does not resemble the same-scale quadrature adversary.}
}
\]

and:

\[
\boxed{
\text{Gate 1 remains numerically plausible.}
}
\]

Not proven, but now materially more credible.

## Next best step

Move from proxy evidence toward canonical fidelity. The priority is no longer more broad proxy scans; it is upgrading the object:

\[
q''_{\zero,\varepsilon}
\quad\longrightarrow\quad
q''_{\can}
=
B_2+\sum_\rho^{\rm reg}K_2(m;\rho).
\]

Recommended next work:

1. Add the completed/gamma background \(B_2\).
2. Replace the artificial \(c=0\mapsto\varepsilon=\kappa/Q\) critical-line mollification with a canonical regularization.
3. Add a tail correction rather than relying only on symmetric cutoff.
4. Rerun the 5k broad scan with the upgraded object.
5. Then do an AFE-side cross-check on the top 50 highest \(B_I^{\rm eff}\) rows from this run.

The watch branch can be removed from active concern.

## User (2026-04-26 19:26:07)

Please note Agent 2's canonicalization of B2

## Assistant (2026-04-26 19:26:17)

_Thought for 8s_

Noted.

Key implementation point:

\[
B_2(t)=\theta'''(t)
=
-\frac18\Re\psi^{(2)}\!\left(\frac14+\frac{it}{2}\right).
\]

For future scans, \(B_2\) should be included by default in:

\[
q''_{\can}(m)=B_2(m)+\sum_\rho^{\rm reg}K_2(m;\rho).
\]

Use the 3-term fast approximation for \(t\ge50\):

\[
B_2(t)\approx
-\frac1{2t^2}
-\frac1{8t^4}
-\frac7{64t^6}.
\]

Also noted: `B2_only` rows are diagnostics only and should never be classified as Gate 1 candidates. The remaining canonical zero-side blockers are now critical-line zero treatment / \(\eta\)-regularization and regularized tail completion, not \(B_2\). 
## User (2026-04-26 19:26:56)

Do the next prompt in the attached message as per your agent number.

## Assistant (2026-04-26 19:27:04)

_Thought for 7s_

## Agent 3 / C — Watch-branch closure report

### Verdict

The old watch branch should be closed.

\[
\boxed{
\text{The old watch intervals are not source-flat candidates.}
}
\]

They are best classified as a mix of low-\(Q\) calibration behavior, smooth gap-midpoint low-energy behavior, and \(\eta=\kappa/Q\) proxy sensitivity—not actual quadrature-like source flattening. This matches the latest coordination instruction: stop more broad \(\eta\)-regularized proxy scans and retire the watch rerun line unless the canonical zero-side upgrade creates a new stable candidate. 

---

# 1. Evidence summary

The original watch centers were:

\[
m_0\approx 27.7179,\quad 109.099,\quad 171.662,\quad 199.640.
\]

The targeted reruns showed:

| \(m_0\) | classification | reason |
|---:|---|---|
| \(27.7179\) | reject / calibration only | too low \(Q\); tail-edge issues dominate with broad absolute windows |
| \(109.099\) | watch, demoted | low \(E_I\), but \(J_{\max}\) fails the \(Q^{-5}\) jet test |
| \(171.662\) | watch, demoted | low \(E_I\), but finite jets remain live |
| \(199.640\) | watch, demoted | low \(E_I\), but finite jets remain live |

The 5k-zero rerun confirmed the same result: the best rows were bit-identical where \(W_{\rm abs}=20\), so the old watch behavior was not caused by insufficient zero-table coverage. The broader 5k scan over \(\gamma_{500}\) to \(\gamma_{4500}\) found no watch rows and no candidates.

The decisive criterion remains:

\[
B_I^{\rm eff}>5
\quad\text{and}\quad
J_{\max}\le Q^{-5}.
\]

No old watch interval satisfies this.

---

# 2. Interpretation

The old watch intervals show:

\[
E_I \text{ moderately low},
\]

but not:

\[
\Delta^r\partial_m^r q''_{\can}(m_0)\approx0
\qquad 0\le r\le R.
\]

So they are not finite-jet flat. This points to ordinary smooth gap-midpoint behavior, not same-scale source-flattening quadrature.

In particular:

\[
\boxed{
\text{low interval energy without jet collapse is not a Gate 1 threat.}
}
\]

The deterministic quadrature negative control proves the harness can detect genuine source-collapse. Actual-zero proxy data has not produced that signature.

---

# 3. Closure rule

Close the watch branch under the current \(\eta\)-regularized zero-kernel proxy.

No further reruns of:

\[
27.7179,\ 109.099,\ 171.662,\ 199.640
\]

are warranted unless one of the following occurs:

1. Agent 2’s canonical critical-line / completed-phase treatment materially changes the object;
2. exact \(B_2\) plus regularized tail creates a new stable row with:
   \[
   B_I^{\rm eff}>5,\qquad J_{\max}\le Q^{-5};
   \]
3. AFE cross-check validates a row that the proxy classified as only watch-level.

Absent those, the watch branch should remain retired.

---

# 4. Canonical rerun grid for future use

Once Agent 2 provides the canonical critical-line/tail treatment, rerun only a compact canonical grid:

### Centers

Use:

1. Top 50 highest-\(B_I^{\rm eff}\) rows from the 5k broad scan.
2. The three demoted watch centers:
   \[
   109.099,\quad 171.662,\quad 199.640
   \]
   as regression tests only.
3. 50 random healthy rows from the 5k scan as controls.

Skip \(27.7179\) except as low-\(Q\) calibration.

### Parameters

\[
c_I\in\{0.05,0.1,0.2,0.5\},
\]

\[
R\in\{8,12,16\},
\]

and whatever canonical smoothing/tail parameter Agent 2 defines.

Do not run broad \(\kappa\)-sweeps once the canonical regularization replaces artificial \(\varepsilon=\kappa/Q\). If a smoothing scale remains, test only a small stability set around the canonical value.

### Required diagnostics

\[
E_I,\quad B_I^{\rm eff},\quad S_I,\quad J_{\max},\quad J_{\rm rms},
\]

plus canonical-tail drift and AFE agreement if available.

Candidate threshold remains:

\[
B_I^{\rm eff}>5,\qquad J_{\max}\le Q^{-5},
\]

with stability under width, tail, and canonical smoothing.

---

# 5. Final status

\[
\boxed{
\text{Watch branch closed under the current proxy.}
}
\]

\[
\boxed{
\text{No further watch reruns unless canonical zero-side treatment creates a new stable candidate.}
}
\]

The next Agent 3 work should be downstream of Agent 2’s canonical upgrade: rerun a compact canonical target set, not broaden the old proxy search.
