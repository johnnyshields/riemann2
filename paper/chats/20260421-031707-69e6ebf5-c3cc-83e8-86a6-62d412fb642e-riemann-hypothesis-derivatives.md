# Riemann Hypothesis Derivatives

- Source: https://chatgpt.com/c/69e6ebf5-c3cc-83e8-86a6-62d412fb642e
- Created: 2026-04-21 03:17:07 UTC
- Default model: gpt-5-4-thinking

---

## User (2026-04-21 03:17:05)

We are trying to prove the Riemann Hypothesis. Please see attached paper.

In particular, I'd like you to help on the 2-point theorem, by doing derivative geometry to help support the effort:

Message from the 2-point teamlead:

Yes — there are three derivative-geometry tasks I’d hand off right now, and they’re all genuinely useful to the current attack.

The highest-value one is a **freeze-the-(\lambda)-shear lemma**. The mixed two-point attack is now naturally expressed in the (\lambda)-sheared source functions
[
A=c-\eta\lambda,\qquad B=v_5-\xi\lambda,\qquad F=u_5-\gamma\lambda,
]
and the goal is to show that a close exact mixed two-point bad branch yields a subsequence with convergent branch-generated shears ((\eta_n,\xi_n,\gamma_n)\to(\eta_*,\xi_*,\gamma_*)), so the branch becomes a fixed-shear repeated-source problem rather than a moving-parameter problem. A chat focused only on proving this freeze lemma from the current local setup would help a lot, because everything downstream becomes much cleaner once the shear is fixed. This is exactly the kind of source-level burden the current draft still flags on the 2-point side.

The second one is a **criticality-to-obstruction theorem on the fixed-shear overlap patch**. Once the shear is frozen, the mixed branch looks like a repeated-value / repeated-source problem for a fixed source-coupled ratio map, and the current draft already has the mixed low-order obstruction list and the derivative-geometric (K_v)-branch on the lifted (v)-patch. What I want another chat to do is: starting from the fixed-shear conditions, prove that a close mixed branch must force either the existing mixed low-order obstruction types ((1,2),(1,4),(2,4)) or accumulation on the (K_v=0) curvature locus. In other words, turn the current fixed-shear criticality into a theorem that it cannot remain genuinely generic. That would connect the two-point attack directly to the derivative-geometry machinery that is already mature.

The third one is a **(K_v)-transfer theorem**. If a close mixed two-point branch accumulates on (K_v=0), can one show it actually feeds into the existing lifted 3-point branch machinery rather than remaining an independent 2-point obstruction? The draft’s 3-point package is now explicitly derivative-geometric, with shrinking exact lifted 3-point circuits tied to the osculating determinant and (K_v=0), plus local classification and global continuation/nonrecurrence. A dedicated chat that tries to prove “mixed 2-point accumulation on (K_v=0) forces entry into the lifted 3-point branch” would be very high-value.

---

YOUR TASK: Assume a close exact mixed two-point bad branch on a good overlap patch. Prove or disprove that the branch-generated (\lambda)-shears ((\eta_n,\xi_n,\gamma_n)) admit a convergent subsequence and that the exact branch equations reduce to a fixed-shear repeated-source problem for (A,B,F). Ignore all 3-point and 4-point branches except insofar as needed to justify the reduction.

## Assistant (2026-04-21 03:17:07)

I’m reading the draft around the mixed 2-point setup and the sheared source functions, then I’ll try to either prove the freeze reduction cleanly or pinpoint the exact gap where it fails.

I’ve isolated the key issue: the current draft already proves the reduction only conditionally on an affine λ-shear limit. The real question is whether the branch gives affine compactness, or only projective compactness. That distinction looks decisive here.

_Thought for 8m 28s_

The statement as written is false in two separate ways.

Write
\[
\delta_n f:=f(h_{1,n})-\Lambda_n f(h_{2,n}).
\]
Then the moving \(\lambda\)-shear equations are exactly
\[
\delta_n(c)=\eta_n\,\delta_n(\lambda),\qquad
\delta_n(v_5)=\xi_n\,\delta_n(\lambda),\qquad
\delta_n(u_5)=\gamma_n\,\delta_n(\lambda).
\]
So whenever \(\delta_n(\lambda)\neq 0\),
\[
\eta_n=\frac{\delta_n(c)}{\delta_n(\lambda)},\qquad
\xi_n=\frac{\delta_n(v_5)}{\delta_n(\lambda)},\qquad
\gamma_n=\frac{\delta_n(u_5)}{\delta_n(\lambda)}.
\]

What is automatic is only the projective class
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
=
[\eta_n:\xi_n:\gamma_n:1]\in \mathbf P^3.
\]
That always has a convergent subsequence after normalization. But affine convergence of
\((\eta_n,\xi_n,\gamma_n)\) in the \(\delta(\lambda)\neq 0\) chart is not automatic.

A clean counterexample is:
\[
c(h)=1+h,\qquad v_5(h)=1+2h,\qquad u_5(h)=1+3h,\qquad \lambda(h)=1+h^2.
\]
On a small neighborhood of \(0\),
\[
c\neq 0,\quad u_5\neq 0,\quad v_5\neq 0,\quad
M=c\,v_5'-c'v_5=(1+h)\cdot 2-1\cdot(1+2h)=1\neq 0,
\]
so this is a good overlap patch. Take
\[
h_{2,n}=0,\qquad h_{1,n}=t_n\to 0,\qquad \Lambda_n=1.
\]
Then
\[
\eta_n=\frac{c(t_n)-c(0)}{\lambda(t_n)-\lambda(0)}
=\frac{t_n}{t_n^2}=\frac1{t_n},
\]
\[
\xi_n=\frac{2t_n}{t_n^2}=\frac2{t_n},\qquad
\gamma_n=\frac{3t_n}{t_n^2}=\frac3{t_n}.
\]
So the exact moving-shear equations hold, but the affine \(\lambda\)-shears have no finite convergent subsequence.

This already disproves the first claim.

The second claim also fails even if the affine \(\lambda\)-shears do converge.

Take instead
\[
c(h)=1+h+h^2,\qquad v_5(h)=1+2h,\qquad u_5(h)=1+3h,\qquad \lambda(h)=1+h,
\]
again with
\[
M=c\,v_5'-c'v_5=(1+h+h^2)\cdot 2-(1+2h)(1+2h)=1-2h-2h^2,
\]
so \(M\neq 0\) near \(0\). With the same choice
\[
h_{2,n}=0,\qquad h_{1,n}=t_n\to 0,\qquad \Lambda_n=1,
\]
one gets
\[
\eta_n=\frac{t_n+t_n^2}{t_n}=1+t_n\to 1,\qquad
\xi_n=\frac{2t_n}{t_n}=2,\qquad
\gamma_n=\frac{3t_n}{t_n}=3.
\]
So the affine shears do converge:
\[
(\eta_n,\xi_n,\gamma_n)\to (1,2,3).
\]

But the frozen limit functions are
\[
A=c-\lambda=h^2,\qquad
B=v_5-2\lambda=-1,\qquad
F=u_5-3\lambda=-2.
\]
For \(\Lambda_n=1\),
\[
A(h_{1,n})=t_n^2\neq 0=A(h_{2,n}),
\]
so the frozen branch does not satisfy exact repeated-source transport for \(A\). Thus convergence of the shears does not give exact reduction to one fixed-shear repeated-source problem.

The right identity is
\[
\delta_n(A)=\delta_n(c-\eta_*\lambda)
=(\eta_n-\eta_*)\,\delta_n(\lambda),
\]
and similarly
\[
\delta_n(B)=(\xi_n-\xi_*)\,\delta_n(\lambda),\qquad
\delta_n(F)=(\gamma_n-\gamma_*)\,\delta_n(\lambda).
\]
So what freezing gives is only an asymptotic fixed-shear reduction, not an exact one.

The corrected statement is:

For every close exact mixed two-point bad branch, the projective defect directions
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]\in \mathbf P^3
\]
admit a convergent subsequence. If the limit lies in the affine chart with nonzero \(\lambda\)-coordinate, then the affine \(\lambda\)-shears converge along that subsequence. But the resulting frozen functions \(A,B,F\) satisfy only asymptotic transport, with defects exactly given by the three formulas above. Exact fixed-shear transport requires an extra theorem forcing the defect direction to be constant, not merely convergent.

The good news is that the projective-shadow part does not actually need exact freezing. For each \(n\), eliminating the moving shears already gives the same secant-shadow formulas, independent of \((\eta_n,\xi_n,\gamma_n)\). So the derivative-geometry reduction to the secant/tangent shadow and the accumulation obstruction on the non-immersive locus can still be run projectively. What fails is only the stronger claim that the whole branch becomes one exact fixed-shear repeated-source branch.

So my verdict is:

- affine \(\lambda\)-shear subsequence convergence: false in general;
- exact frozen repeated-source reduction: false even when affine convergence holds;
- projective subsequence convergence: true;
- asymptotic frozen reduction in a chosen affine chart: true.

The proposition in the draft should be weakened exactly in that way.
## User (2026-04-21 03:27:36)

anything further to push on or should we update the latex? if the latter, give me the latex insertions to make

## Assistant (2026-04-21 03:27:37)

I’m checking the current draft around the 2-point shear/freezing discussion so I can give edit-ready insertions that match what is already there and avoid conflicting with nearby statements.

_Thought for 3m 6s_

I’d update the latex now.

The main new takeaway is not another exclusion theorem. It is a correction of the 2-point route’s formulation:

- what is automatic is **projective compactness** of the defect direction;
- affine \(\lambda\)-shear freezing is only conditional on landing in the \(\delta(\lambda)\neq 0\) chart;
- even then, one gets only **asymptotically frozen** transport, not exact transport for one fixed triple \((\eta_*,\xi_*,\gamma_*)\).

The next push after this edit is to restate the downstream secant-shadow argument entirely projectively, so it no longer depends on exact affine freezing.

Here are the edits I would make.

---

### 1. Insert a new proposition + remark after Remark `\ref{rem:audit-shear-blind-two-point-determinantal-routes}`

Insert immediately after
```latex
\end{remark}
```
that closes Remark `\ref{rem:audit-shear-blind-two-point-determinantal-routes}`.

```latex
\begin{proposition}[Projective compactness of the moving $\lambda$-shear defects]
\label{prop:projective-compactness-moving-lambda-shear-two-point}
Assume a close exact mixed two-point bad branch on a compact good overlap patch
\[
U\Subset\{c\neq 0,\ v_5\neq 0,\ M\neq 0\},
\]
and write
\[
\Lambda_n:=-\frac{a_{2,n}}{a_{1,n}},
\qquad
\delta_n f:=f(h_{1,n})-\Lambda_n f(h_{2,n}),
\qquad
\lambda=\frac{\Delta_7}{v_5}.
\]
Then the mixed branch equations are equivalent to the existence of branch-generated
moving shears $(\eta_n,\xi_n,\gamma_n)$ such that
\[
\delta_n(c)=\eta_n\,\delta_n(\lambda),\qquad
\delta_n(v_5)=\xi_n\,\delta_n(\lambda),\qquad
\delta_n(u_5)=\gamma_n\,\delta_n(\lambda).
\]

Set
\[
d_n:=\bigl(\delta_n(c),\delta_n(v_5),\delta_n(u_5),\delta_n(\lambda)\bigr)\in\mathbf R^4.
\]
Then, after passing to a subsequence, exactly one of the following holds.

\begin{enumerate}
\item
$d_n=0$ for all $n$ in the subsequence. Equivalently, along that subsequence one already has exact repeated-source transport simultaneously for
\[
c,\qquad v_5,\qquad u_5,\qquad \lambda.
\]

\item
$d_n\neq 0$ for all $n$ in the subsequence, and the normalized defect directions
\[
\widehat d_n:=\frac{d_n}{\|d_n\|}\in S^3
\]
converge. Equivalently, the projective classes
\[
[d_n]
=
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\in \mathbf P^3
\]
admit a convergent subsequence.
\end{enumerate}

Moreover, on any subsequence for which $\delta_n(\lambda)\neq 0$ and the projective
limit lies in the affine chart with nonzero $\lambda$-coordinate, the affine
$\lambda$-shears converge:
\[
\eta_n=\frac{\delta_n(c)}{\delta_n(\lambda)}\to\eta_*,
\qquad
\xi_n=\frac{\delta_n(v_5)}{\delta_n(\lambda)}\to\xi_*,
\qquad
\gamma_n=\frac{\delta_n(u_5)}{\delta_n(\lambda)}\to\gamma_*.
\]

For the limiting affine shear one has only the asymptotic fixed-shear identities
\[
\delta_n(c-\eta_*\lambda)=(\eta_n-\eta_*)\,\delta_n(\lambda),
\]
\[
\delta_n(v_5-\xi_*\lambda)=(\xi_n-\xi_*)\,\delta_n(\lambda),
\]
\[
\delta_n(u_5-\gamma_*\lambda)=(\gamma_n-\gamma_*)\,\delta_n(\lambda).
\]
Hence a close exact mixed branch automatically reduces only to a
\emph{projectively frozen secant-shadow problem}. In general it does \emph{not}
reduce to exact repeated-source transport for a single fixed triple
\[
(\eta_*,\xi_*,\gamma_*).
\]
\end{proposition}

\begin{proof}
The identities
\[
\delta_n(c)=\eta_n\,\delta_n(\lambda),\qquad
\delta_n(v_5)=\xi_n\,\delta_n(\lambda),\qquad
\delta_n(u_5)=\gamma_n\,\delta_n(\lambda)
\]
are just a rewriting of the branch equations. If $d_n=0$ infinitely often, pass
to that subsequence. Otherwise $d_n\neq 0$ for all large $n$, and compactness of
the unit sphere gives a convergent subsequence of $\widehat d_n$, equivalently
of the associated projective classes in $\mathbf P^3$.

On the affine chart $\delta_n(\lambda)\neq 0$, the projective coordinates are
exactly
\[
\eta_n=\frac{\delta_n(c)}{\delta_n(\lambda)},\qquad
\xi_n=\frac{\delta_n(v_5)}{\delta_n(\lambda)},\qquad
\gamma_n=\frac{\delta_n(u_5)}{\delta_n(\lambda)},
\]
so convergence in that chart is precisely convergence of the affine
$\lambda$-shears. The last three identities are immediate from the definitions.
\end{proof}

\begin{remark}[Affine freezing is stronger than projective freezing on the mixed two-point branch]
\label{rem:affine-freezing-stronger-than-projective-two-point}
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point}
shows that the automatic compactness on the mixed two-point branch is
projective, not affine. Even on a good overlap patch, the affine
$\lambda$-shears can diverge if $\delta_n(\lambda)$ vanishes to higher order
than $\delta_n(c),\delta_n(v_5),\delta_n(u_5)$. And even when
\[
(\eta_n,\xi_n,\gamma_n)\to(\eta_*,\xi_*,\gamma_*),
\]
one gets only asymptotic transport for
\[
c-\eta_*\lambda,\qquad
v_5-\xi_*\lambda,\qquad
u_5-\gamma_*\lambda,
\]
not exact transport at each stage of the branch. Therefore the downstream
derivative-geometric reduction should be formulated in terms of the projective
defect direction
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)],
\]
or equivalently in any affine chart on which the projective limit has nonzero
coordinate, rather than as an exact frozen-$\lambda$ repeated-source branch.
\end{remark}
```

---

### 2. Replace the mixed-\(\lambda\)-shear paragraph in Remark `\ref{rem:what-remains-two-pair-rewrite}`

In Remark `\ref{rem:what-remains-two-pair-rewrite}`, replace the paragraph beginning

```latex
Third, on a good overlap patch in the mixed regime, the derivative-geometric
attack now naturally passes through the $\lambda$-sheared source transport
system
```

and ending just before

```latex
So the genuinely remaining two-point work is either the verification of the
finite-order source-level merger criterion, ...
```

with:

```latex
Third, on a good overlap patch in the mixed regime, the derivative-geometric
attack now naturally passes through the moving $\lambda$-sheared source
transport system
\[
(c-\eta_n\lambda)(h_{1,n})=\Lambda_n(c-\eta_n\lambda)(h_{2,n}),
\qquad
(v_5-\xi_n\lambda)(h_{1,n})=\Lambda_n(v_5-\xi_n\lambda)(h_{2,n}),
\qquad
(u_5-\gamma_n\lambda)(h_{1,n})=\Lambda_n(u_5-\gamma_n\lambda)(h_{2,n}),
\]
with
\[
\lambda=\frac{\Delta_7}{v_5},
\qquad
\Lambda_n=-\frac{a_{2,n}}{a_{1,n}}.
\]
By Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point},
what is automatic from an exact close mixed branch is not affine freezing of
\[
(\eta_n,\xi_n,\gamma_n),
\]
but projective compactness of the defect directions
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)],
\qquad
\delta_n(f):=f(h_{1,n})-\Lambda_n f(h_{2,n}).
\]
On any subsequence whose projective limit lies in the affine $\lambda$-chart,
one obtains a convergent affine $\lambda$-shear subsequence; in general the
exact frozen repeated-source reduction is not automatic. The associated
projective secant shadow can nevertheless accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
```

---

### 3. Replace the mixed-\(\lambda\)-shear paragraph in Remark `\ref{rem:live-attack-routes}`

In Remark `\ref{rem:live-attack-routes}`, inside item 1, replace

```latex
The genuinely new derivative-geometric lane is the $\lambda$-shear route on a good
overlap patch, where
\[
\lambda=\frac{\Delta_7}{v_5},
\qquad
A=c-\eta\lambda,\quad
B=v_5-\xi\lambda,\quad
F=u_5-\gamma\lambda
\]
satisfy exact repeated-source transport along the branch. After freezing a
$\lambda$-shear subsequence, the associated projective secant shadow can
accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or source-coupled control of
the mixed $\lambda$-shear exceptional loci.
```

with:

```latex
The genuinely new derivative-geometric lane is the $\lambda$-shear route on a
good overlap patch, where
\[
\lambda=\frac{\Delta_7}{v_5}
\]
and an exact mixed branch generates moving shears
\[
(\eta_n,\xi_n,\gamma_n)
\]
for which
\[
A_n:=c-\eta_n\lambda,\qquad
B_n:=v_5-\xi_n\lambda,\qquad
F_n:=u_5-\gamma_n\lambda
\]
satisfy exact repeated-source transport along the branch. By
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point},
the automatic compactness is projective:
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\]
admits a convergent subsequence, and only on a subsequence whose limit lies in
the affine $\lambda$-chart does one obtain a convergent affine
$\lambda$-shear. Even then the frozen triple yields only asymptotic, not exact,
fixed-shear transport. The associated projective secant shadow can nevertheless
accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or source-coupled control of
the mixed $\lambda$-shear exceptional loci.
```

---

### 4. Replace the two-point summary paragraph in the long global summary remark near line 21360

Replace

```latex
At present the two-point side therefore splits into three conditional lanes:
the finite-order source-level merger route of
Lemma~\ref{lem:minimal-source-level-two-point-criterion}, the weaker
quotient-diagonal exact exclusion route of
Proposition~\ref{prop:conditional-exact-two-point-exclusion-qabs}, and the
mixed $\lambda$-shear / projective-shadow route on good overlap patches. In the
last route, after freezing a $\lambda$-shear subsequence the mixed branch
becomes repeated-source transport for
\[
c-\eta\lambda,\qquad v_5-\xi\lambda,\qquad u_5-\gamma\lambda,
\qquad
\lambda=\frac{\Delta_7}{v_5},
\]
and its projective secant shadow can accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
So the remaining structural issue on the two-point side is either verification
of the finite-order merger criterion or source-coupled control of these
explicit mixed exceptional loci.
```

with:

```latex
At present the two-point side therefore splits into three conditional lanes:
the finite-order source-level merger route of
Lemma~\ref{lem:minimal-source-level-two-point-criterion}, the weaker
quotient-diagonal exact exclusion route of
Proposition~\ref{prop:conditional-exact-two-point-exclusion-qabs}, and the
mixed $\lambda$-shear / projective-shadow route on good overlap patches. In the
last route, an exact mixed branch generates moving $\lambda$-shears through
\[
\lambda=\frac{\Delta_7}{v_5},
\]
and
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point}
shows that the automatic compactness is projective:
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\]
admits a convergent subsequence. Only when the projective limit lies in the
affine $\lambda$-chart does one obtain a convergent affine $\lambda$-shear
subsequence, and even then the frozen triple gives only asymptotic, not exact,
fixed-shear transport. The associated projective secant shadow can nevertheless
accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
So the remaining structural issue on the two-point side is either verification
of the finite-order merger criterion or source-coupled control of these
explicit mixed exceptional loci.
```

---

### 5. Replace the first paragraph of Remark `\ref{rem:post-draft-findings-established-provisional-live}`

Replace the paragraph beginning

```latex
First, on the two-point branch, the exact finite-order source criterion remains
...
```

down through

```latex
So the remaining two-point issue is no longer a single broad interaction
ansatz, but a choice among these three explicit closure mechanisms.
```

with:

```latex
First, on the two-point branch, the exact finite-order source criterion remains
the clean algebraic route, but the naive source-summed corrected block model
cannot prove it: along a weighted one-atom path the extracted finite-order
coefficients are even analytic in the source weight. So the remaining two-point
issue now splits into three conditional lanes: the finite-order source-level
merger route, the weaker quotient-diagonal exact exclusion route, and the mixed
$\lambda$-shear / projective-shadow route on good overlap patches. In the last
route, a close exact mixed two-point bad branch generates moving shears through
\[
\lambda=\frac{\Delta_7}{v_5},
\]
and
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point}
shows that the automatic compactness is projective:
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\]
admits a convergent subsequence. Only when the projective limit lies in the
affine $\lambda$-chart does one obtain a convergent affine $\lambda$-shear
subsequence, and even then the limiting triple yields only asymptotic, not
exact, fixed-shear transport. The associated projective secant shadow can
nevertheless accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
So the remaining two-point issue is no longer a single broad interaction
ansatz, but a choice among these three explicit closure mechanisms.
```

---

### 6. Make one small wording fix in Remark `\ref{rem:live-attack-routes}` item 1

Replace

```latex
The genuinely new derivative-geometric lane is the $\lambda$-shear route on a good
overlap patch, where
```

with

```latex
The genuinely new derivative-geometric lane is the $\lambda$-shear route on a
good overlap patch, where an exact mixed branch generates moving shears and
```

if you prefer to keep that sentence short before the larger replacement above.

---

The one further push I’d do after these edits is to write the downstream secant-shadow theorem in a fully projective form, so the 2-point route no longer mentions “freezing a \(\lambda\)-shear subsequence” except as an optional affine-chart refinement.
## User (2026-04-21 03:35:06)

can you do the math push on this: downstream secant-shadow theorem in a fully projective form

## Assistant (2026-04-21 03:35:08)

I’m pulling the exact surrounding definitions from the draft so I can rewrite the shadow theorem in the same notation rather than inventing a parallel version.

_Thought for 7m 40s_

Yes. This push works, and it is cleaner than the frozen-affine version.

The key point is:

The secant-shadow reduction does **not** need a convergent affine \(\lambda\)-shear subsequence at all.  
It is already exact, pointwise along the branch, at the level of a projective common value.

Here is the clean projective theorem.

---

### Exact projective secant-shadow reduction for the mixed \(2\)-point branch

Work on a good overlap patch
\[
U\Subset \{c\neq 0,\ u_5\neq 0,\ v_5\neq 0,\ M\neq 0\}.
\]
Set
\[
\lambda:=\frac{\Delta_7}{v_5},\qquad
x:=\frac{v_5}{c},\qquad
Y:=\frac{u_5}{c},\qquad
S:=\frac{\lambda}{c}=\frac{\Delta_7}{c\,v_5}.
\]

Assume there is a close exact mixed two-point bad branch
\[
(h_{1,n},h_{2,n},\Lambda_n),\qquad h_{1,n}\neq h_{2,n},\qquad h_{1,n},h_{2,n}\to a\in U,
\]
with branch-generated moving shears \((\eta_n,\xi_n,\gamma_n)\) satisfying
\[
(c-\eta_n\lambda)(h_{1,n})=\Lambda_n(c-\eta_n\lambda)(h_{2,n}),
\]
\[
(v_5-\xi_n\lambda)(h_{1,n})=\Lambda_n(v_5-\xi_n\lambda)(h_{2,n}),
\]
\[
(u_5-\gamma_n\lambda)(h_{1,n})=\Lambda_n(u_5-\gamma_n\lambda)(h_{2,n}).
\]

Define
\[
A_n:=c-\eta_n\lambda,\qquad
B_n:=v_5-\xi_n\lambda,\qquad
F_n:=u_5-\gamma_n\lambda.
\]

Then for each \(n\) the common projective value
\[
\Sigma_n:=
[B_n(h_{1,n}):F_n(h_{1,n}):A_n(h_{1,n})]
=
[B_n(h_{2,n}):F_n(h_{2,n}):A_n(h_{2,n})]
\in \mathbf P^2
\]
is well-defined, and depends only on \((h_{1,n},h_{2,n})\), not on the shears or on \(\Lambda_n\). In fact
\[
\Sigma_n
=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1],
\]
where \(x_i=x(h_{i,n})\), \(Y_i=Y(h_{i,n})\), \(S_i=S(h_{i,n})\).

Equivalently, in raw coordinates,
\[
\Sigma_n
=
[v_{5,1}\lambda_2-v_{5,2}\lambda_1:\ u_{5,1}\lambda_2-u_{5,2}\lambda_1:\ c_1\lambda_2-c_2\lambda_1].
\]

As \(h_{2,n}\to h_{1,n}=a\), these secant shadows converge to the tangent shadow
\[
\Pi(a):=
[xS_x-S:\ YS_x-SY_x:\ S_x]\big|_{x=x(a)},
\]
equivalently
\[
\Pi_{\rm raw}(a):=
[v_5\lambda'-v_5'\lambda:\ u_5\lambda'-u_5'\lambda:\ c\lambda'-c'\lambda]\big|_{a}.
\]

Moreover,
\[
\Pi(x)\wedge \partial_x\Pi(x)
=
S(x)\,\bigl(S_xY_{xx}-S_{xx}Y_x,\ S_{xx},\ -S_{xx}\bigr),
\]
so \(\Pi\) is projectively immersive wherever
\[
S\neq 0,\qquad S_{xx}\neq 0.
\]
Since on a good \(v_5\)-patch
\[
K_v=(x')^3S_{xx},
\]
the projective-shadow degeneration locus is contained in
\[
\{S=0\}\cup \{K_v=0\}.
\]

So the shadow theorem really is fully projective: no affine freezing is needed.

---

### Why the exact projective formula is true

The transport equations give
\[
A_n(h_{1,n})=\Lambda_nA_n(h_{2,n}),\quad
B_n(h_{1,n})=\Lambda_nB_n(h_{2,n}),\quad
F_n(h_{1,n})=\Lambda_nF_n(h_{2,n}),
\]
hence
\[
[B_1:F_1:A_1]=[B_2:F_2:A_2].
\]

Now write, at a fixed branch index \(n\),
\[
A_i=c_i(1-\eta S_i),\qquad
B_i=c_i(x_i-\xi S_i),\qquad
F_i=c_i(Y_i-\gamma S_i).
\]
Since \([B_1:A_1]=[B_2:A_2]\), we have
\[
A_1B_2-A_2B_1=0.
\]
Expanding and simplifying gives
\[
(S_2-S_1)B_1-(x_1S_2-x_2S_1)A_1=0.
\]
Likewise, from \(A_1F_2-A_2F_1=0\),
\[
(S_2-S_1)F_1-(Y_1S_2-Y_2S_1)A_1=0.
\]
These two homogeneous relations force
\[
[B_1:F_1:A_1]=[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1].
\]
That is the exact secant-shadow formula, and no convergence hypothesis on the shears appears anywhere.

The diagonal limit is just first-order expansion:
\[
x_2=x_1+x'(a)\,\delta+o(\delta),\quad
Y_2=Y_1+Y'(a)\,\delta+o(\delta),\quad
S_2=S_1+S'(a)\,\delta+o(\delta),
\]
then divide by \(\delta\) and convert from \(h\)- to \(x\)-derivatives using \(x'\neq 0\) on the good patch.

---

### What this buys you

This upgrades the current mixed \(2\)-point route substantially.

You can replace the present conditional statement

“after freezing a \(\lambda\)-shear subsequence…”

with the stronger statement

“every exact mixed \(2\)-point branch already determines an exact projective secant shadow, independent of the moving shears.”

So the remaining burden is no longer affine-freezing. It is only:

1. analyze the explicit exceptional set
\[
\{S=0\}\cup\{K_v=0\},
\]
2. show that accumulation on \(S=0\) falls into the existing mixed low-order obstruction package or lower-core collapse,
3. show that accumulation on \(K_v=0\) transfers into the lifted \(3\)-point machinery.

That is a real cleanup.

---

### One caveat

This does **not** produce a single fixed-shear repeated-source problem for one limiting triple \((\eta_*,\xi_*,\gamma_*)\). That stronger affine claim is still false in general.

But for the derivative-geometric shadow route, you do not need it.

The projective secant-shadow theorem is the right downstream formulation.

If you want, I can now turn this into exact latex insertions replacing Proposition `prop:conditional-mixed-lambda-shear-projective-shadow-reduction` and its downstream remarks.
## User (2026-04-21 03:49:46)

yes, here's the latest draft, please give me the latex insertions

## Assistant (2026-04-21 03:49:48)

I’m locating the current mixed 2-point projective-shadow proposition and nearby remarks in the latest draft so I can give clean replacements rather than generic inserts.

_Thought for 3m 46s_

Yes. In the latest draft, the main thing to do is replace the current conditional/frozen-shear proposition by an exact projective-shadow proposition, and then update the status remark to match.

I would make these two edits.

---

Replace the entire block from

```latex
\begin{proposition}[Conditional mixed $\lambda$-shear reduction on an overlap patch]
\label{prop:conditional-mixed-lambda-shear-projective-shadow-reduction}
```

through its `\end{proof}` with:

```latex
\begin{proposition}[Projective secant-shadow reduction on an overlap patch]
\label{prop:conditional-mixed-lambda-shear-projective-shadow-reduction}
Let
\[
U\Subset\{c\neq 0,\ u_5\neq 0,\ v_5\neq 0,\ M\neq 0\}
\]
be a good overlap patch. Set
\[
\lambda:=\frac{\Delta_7}{v_5},
\qquad
x:=\frac{v_5}{c},
\qquad
Y:=\frac{u_5}{c},
\qquad
S:=\frac{\lambda}{c}=\frac{\Delta_7}{c\,v_5}.
\]

Assume there exists a close exact mixed two-point bad branch
\[
(h_{1,n},h_{2,n},\Lambda_n),
\qquad
h_{1,n}\neq h_{2,n},
\qquad
h_{1,n},h_{2,n}\in U,
\qquad
h_{1,n},h_{2,n}\to m\in U,
\]
and let $(\eta_n,\xi_n,\gamma_n)$ be the branch-generated moving
$\lambda$-shears, so that
\[
(c-\eta_n\lambda)(h_{1,n})=\Lambda_n(c-\eta_n\lambda)(h_{2,n}),
\]
\[
(v_5-\xi_n\lambda)(h_{1,n})=\Lambda_n(v_5-\xi_n\lambda)(h_{2,n}),
\]
\[
(u_5-\gamma_n\lambda)(h_{1,n})=\Lambda_n(u_5-\gamma_n\lambda)(h_{2,n}).
\]
For each $n$, set
\[
A_n:=c-\eta_n\lambda,
\qquad
B_n:=v_5-\xi_n\lambda,
\qquad
F_n:=u_5-\gamma_n\lambda.
\]

Then, after discarding finitely many terms, the branch determines the exact
projective secant shadow
\[
\mathbf\Sigma(h_{1,n},h_{2,n})
:=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1],
\]
where
\[
x_i=x(h_{i,n}),
\qquad
Y_i=Y(h_{i,n}),
\qquad
S_i=S(h_{i,n}).
\]
More precisely, for all large $n$ one has the exact identity
\[
[B_n(h_{1,n}):F_n(h_{1,n}):A_n(h_{1,n})]
=
[B_n(h_{2,n}):F_n(h_{2,n}):A_n(h_{2,n})]
=
\mathbf\Sigma(h_{1,n},h_{2,n}).
\]
In particular, the secant shadow is independent of the moving shears
$(\eta_n,\xi_n,\gamma_n)$ and of $\Lambda_n$.

Equivalently, in raw coordinates,
\[
\mathbf\Sigma(h_1,h_2)
=
[v_{5,1}\lambda_2-v_{5,2}\lambda_1:\ u_{5,1}\lambda_2-u_{5,2}\lambda_1:\ c_1\lambda_2-c_2\lambda_1].
\]

As $h_2\to h_1=a$, the secant shadow converges projectively to the tangent
shadow
\[
\mathbf\Pi(a)
:=
[xS_x-S:\ YS_x-SY_x:\ S_x]\big|_{x=x(a)}.
\]
A direct calculation gives
\[
\mathbf\Pi(x)\wedge \partial_x\mathbf\Pi(x)
=
S(x)\,
\bigl(
S_xY_{xx}-S_{xx}Y_x,\ S_{xx},\ -S_{xx}
\bigr).
\]
Hence $\mathbf\Pi$ is projectively immersive wherever
\[
S\neq 0
\qquad\text{and}\qquad
S_{xx}\neq 0.
\]
Since on the $v_5$-patch
\[
K_v=(x')^3S_{xx},
\]
any such close exact mixed two-point bad branch can accumulate only on
\[
\{S=0\}\cup\{K_v=0\}.
\]
\end{proposition}

\begin{proof}
Since
\[
x'=\left(\frac{v_5}{c}\right)'=\frac{M}{c^2},
\]
the hypothesis $M\neq 0$ implies that $x=v_5/c$ is a local coordinate near
$m$. After discarding finitely many terms we may therefore assume
\[
x(h_{1,n})\neq x(h_{2,n}).
\]

Fix such an $n$, and abbreviate
\[
\eta=\eta_n,\qquad \xi=\xi_n,\qquad \gamma=\gamma_n.
\]
Write
\[
p_i:=(x_i,Y_i,1)\in\mathbf R^3,
\qquad
V:=(\xi,\gamma,\eta)\in\mathbf R^3,
\qquad
i=1,2.
\]
Since
\[
A_n=c(1-\eta S),
\qquad
B_n=c(x-\xi S),
\qquad
F_n=c(Y-\gamma S),
\]
the exact repeated-source equations imply
\[
[B_n(h_{1,n}):F_n(h_{1,n}):A_n(h_{1,n})]
=
[p_1-S_1V]
\]
and
\[
[B_n(h_{2,n}):F_n(h_{2,n}):A_n(h_{2,n})]
=
[p_2-S_2V].
\]
Because these two projective points are equal, there is a common projective
value.

If $S_1=S_2$, then
\[
[p_1-S_1V]=[p_2-S_1V]
\]
forces $p_1=p_2$, hence $x_1=x_2$, contradicting the choice of local
coordinate. Therefore
\[
S_1\neq S_2.
\]
Subtracting
\[
p_1-S_1V=p_2-S_2V
\]
gives
\[
p_1-p_2=(S_1-S_2)V,
\]
hence
\[
V=\frac{p_1-p_2}{S_1-S_2}.
\]
Substituting back,
\[
p_1-S_1V
=
p_1-S_1\frac{p_1-p_2}{S_1-S_2}
=
\frac{S_2p_1-S_1p_2}{S_2-S_1}.
\]
Therefore the common projective value is exactly
\[
[S_2p_1-S_1p_2]
=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1],
\]
which is the asserted secant shadow and is independent of
$(\eta_n,\xi_n,\gamma_n)$ and of $\Lambda_n$. The raw-coordinate formula is the
same identity multiplied through by $c_1c_2$.

Now divide the homogeneous secant vector by $x_2-x_1$ and let $h_2\to h_1=a$.
The three components converge to
\[
xS_x-S,\qquad YS_x-SY_x,\qquad S_x,
\]
so the secant shadow converges projectively to
\[
\mathbf\Pi(a)
=
[xS_x-S:\ YS_x-SY_x:\ S_x].
\]

Differentiating $\mathbf\Pi$ in the local $x$-coordinate gives
\[
\mathbf\Pi(x)\wedge \partial_x\mathbf\Pi(x)
=
S(x)\,
\bigl(
S_xY_{xx}-S_{xx}Y_x,\ S_{xx},\ -S_{xx}
\bigr).
\]
Therefore $\mathbf\Pi$ is projectively immersive wherever $S\neq 0$ and
$S_{xx}\neq 0$. On a close bad branch the secant shadows converge to tangent
shadows, so accumulation is possible only where immersion fails, i.e. on
\[
\{S=0\}\cup\{S_{xx}=0\}.
\]
Finally, on the $v_5$-patch one has
\[
K_v=(x')^3S_{xx},
\]
so $\{S_{xx}=0\}=\{K_v=0\}$ on $U$.
\end{proof}
```

---

Then replace the entire remark

```latex
\begin{remark}[Status of the mixed $\lambda$-shear route]
\label{rem:wip-mixed-lambda-shear-route-status}
...
\end{remark}
```

with:

```latex
\begin{remark}[Status of the mixed $\lambda$-shear route]
\label{rem:wip-mixed-lambda-shear-route-status}
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction}
shows that the downstream secant-shadow reduction is already exact and fully
projective: a close exact mixed two-point bad branch determines the projective
secant shadow
\[
\mathbf\Sigma(h_1,h_2)
=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1],
\qquad
S=\frac{\Delta_7}{c\,v_5},
\]
independently of any affine freezing of the branch-generated $\lambda$-shears.
Thus the generic mixed two-point branch is already reduced either to the
septic-zero slice
\[
S=0
\]
or to the lifted curvature locus
\[
K_v=0.
\]
The remaining unresolved work is to show that accumulation on $S=0$ either
falls into the existing mixed low-order obstruction types or transfers into a
lower-core tangency mechanism, while accumulation on $K_v=0$ is absorbed by
the existing lifted three-point branch machinery.
\end{remark}
```

---

I do not think you need any other changes for this pass. The rest of the draft already points the two-point story toward projective compactness rather than exact affine freezing, so these two replacements should make the section internally consistent.
## User (2026-04-21 03:57:37)

here's the updated paper with your edits. another chat wants to do the attached insertions. can you review them and remove any stale language, and give me a finalized version of them to insert along with where to do so.

## Assistant (2026-04-21 03:57:39)

I’m checking the proposed proposition against the current draft’s actual labels and against the newer projective-shadow formulation, because parts of it may have gone stale after the last round.

_Thought for 5m 19s_

I would not insert the attached theorem package verbatim. The stale part is the step that treats the fixed-shear projection \(\Phi\) as already affine-target-equivalent to the nonmixed normalized chart just because \(1-\eta_*S\) is a unit; that is too strong after the projective rewrite. I’d keep the sharpening, but scope it to what is actually proved now. 

Here is the version I’d insert.

Replace the current block

```latex
\begin{remark}[Status of the mixed $\lambda$-shear route]
\label{rem:wip-mixed-lambda-shear-route-status}
...
\end{remark}
```

with this proposition + remark:

```latex
\begin{proposition}[Exact fixed-shear overlap branches off $K_v=0$ force a fold at $S=0$]
\label{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
Work on the overlap patch of
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction},
and write
\[
\Phi(x):=
\left(
\frac{x-\xi_* S}{1-\eta_* S},
\frac{Y-\gamma_* S}{1-\eta_* S}
\right),
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
Assume there is a close exact fixed-shear mixed $2$-point branch
\[
x_{1,n}\neq x_{2,n},
\qquad
x_{1,n},x_{2,n}\to a,
\qquad
\Phi(x_{1,n})=\Phi(x_{2,n})
\quad(n\ge 1).
\]
If
\[
K_v(a)\neq 0,
\]
then
\[
S(a)=0,
\qquad
\Phi'(a)=0,
\qquad
S_x(a)\neq 0.
\]
More precisely,
\[
0=\Phi_1'(a)=1-(\xi_*-\eta_* x(a))S_x(a),
\]
\[
0=\Phi_2'(a)=Y_x(a)-(\gamma_*-\eta_* Y(a))S_x(a).
\]
In particular, setting
\[
\beta:=\xi_*-\eta_* x(a)=\frac{1}{S_x(a)},
\]
the first-coordinate fold model
\[
U(x):=x-\beta S(x)
\]
satisfies
\[
U(a)=0,
\qquad
U_x(a)=0,
\qquad
U_{xx}(a)=-\beta S_{xx}(a)\neq 0.
\]
Hence, after analytic source reparametrization, the first coordinate of the
fixed-shear projected germ is
\[
t^2.
\]
So any exact fixed-shear mixed branch away from $K_v=0$ is already forced into
the same fold regime that underlies the nonmixed odd-zero analysis; the only
remaining issue there is the second-coordinate parity package.
\end{proposition}

\begin{proof}
A fixed-shear branch is, in particular, a close exact mixed two-point bad branch
on the same overlap patch. By
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction},
any accumulation point of such a branch lies in
\[
\{S=0\}\cup\{K_v=0\}.
\]
So if $K_v(a)\neq 0$, then necessarily
\[
S(a)=0.
\]

Because
\[
\Phi(x_{1,n})=\Phi(x_{2,n}),
\qquad
x_{1,n}\neq x_{2,n},
\qquad
x_{1,n},x_{2,n}\to a,
\]
the mean value theorem applied to each coordinate of $\Phi$ gives points
\[
\zeta_{1,n},\zeta_{2,n}\in(x_{1,n},x_{2,n})
\]
such that
\[
\Phi_1'(\zeta_{1,n})=0,
\qquad
\Phi_2'(\zeta_{2,n})=0.
\]
Passing to the limit yields
\[
\Phi'(a)=0.
\]

Differentiating the two coordinates of $\Phi$ gives
\[
\Phi_1'
=
\frac{1-(\xi_*-\eta_* x)S_x-\eta_* S}{(1-\eta_* S)^2},
\]
\[
\Phi_2'
=
\frac{Y_x-(\gamma_*-\eta_* Y)S_x-\eta_* S\,Y_x}{(1-\eta_* S)^2}.
\]
Evaluating at $x=a$ and using $S(a)=0$ yields the displayed identities
\[
0=\Phi_1'(a)=1-(\xi_*-\eta_* x(a))S_x(a),
\]
\[
0=\Phi_2'(a)=Y_x(a)-(\gamma_*-\eta_* Y(a))S_x(a).
\]
The first identity implies
\[
S_x(a)\neq 0
\qquad\text{and}\qquad
\beta:=\xi_*-\eta_* x(a)=\frac{1}{S_x(a)}.
\]

Now set
\[
U(x):=x-\beta S(x).
\]
Then
\[
U(a)=a-\beta S(a)=a,
\]
so after translating the source coordinate we may assume $U(a)=0$, and
\[
U_x(a)=1-\beta S_x(a)=0.
\]
Moreover,
\[
U_{xx}(a)=-\beta S_{xx}(a).
\]
Since on the $v_5$-patch
\[
K_v=(x')^3S_{xx},
\qquad
x'=\frac{M}{c^2}\neq 0,
\]
the hypothesis $K_v(a)\neq 0$ implies
\[
S_{xx}(a)\neq 0.
\]
Hence
\[
U_{xx}(a)\neq 0.
\]
By the analytic Morse lemma in one variable, after analytic source
reparametrization the first coordinate is $t^2$.
\end{proof}

\begin{remark}[Status of the mixed $\lambda$-shear route]
\label{rem:wip-mixed-lambda-shear-route-status}
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction}
shows that the downstream secant-shadow reduction is already exact and fully
projective: a close exact mixed two-point bad branch determines the projective
secant shadow
\[
\mathbf\Sigma(h_1,h_2)
=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1],
\qquad
S=\frac{\Delta_7}{c\,v_5},
\]
independently of any affine freezing of the branch-generated $\lambda$-shears.

Proposition~\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
sharpens the \emph{conditional exact fixed-shear} lane: if one does obtain an
exact fixed-shear overlap reduction and the accumulation point lies off
\[
K_v=0,
\]
then the complementary slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime. So, in that fixed-shear
lane, the only missing step is to identify the second-coordinate parity with
the existing nonmixed odd-zero $\mathcal R$-package. In particular, the only
clearly genuinely mixed accumulation locus already visible on the overlap patch
is
\[
K_v=0.
\]

What remains unresolved on the two-point side as a whole is therefore:
the finite-order source-level merger route;
the quotient-diagonal continuity/diagonal-collapse route; and, on the
derivative-geometric side, either a projective control of the
\[
S=0
\]
slice without exact freezing, or a proof that the exact fixed-shear overlap
lane is absorbed by the nonmixed odd-zero package. The explicit mixed low-order
obstruction list remains the finite Wronskian-order list recorded in
Remark~\ref{rem:wronskian-order-reformulation-mixed-list}.
\end{remark}
```

Then, in `Remark~\ref{rem:live-attack-routes}`, item 1, replace the final sentence

```latex
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or source-coupled control of
the mixed $\lambda$-shear exceptional loci.
```

with:

```latex
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or source-coupled control of
the mixed $\lambda$-shear exceptional loci. In the conditional exact
fixed-shear overlap lane,
Proposition~\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
shows that the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime. Thus the only clearly
genuinely mixed fixed-shear locus left on the overlap patch is
\[
K_v=0,
\]
while the missing step off $K_v=0$ is the identification of the resulting
second-coordinate parity with the existing nonmixed odd-zero
\[
\mathcal R=\frac{T_v}{K_v^2}
\]
package.
```

The two changes from the attached version are the important ones:

- I scoped everything explicitly to the **conditional exact fixed-shear lane**, instead of making it sound like freezing is now automatic.
- I removed the stale “affine-target-equivalent to the nonmixed normalized chart” step, and only recorded the part that is already cleanly justified: off \(K_v=0\), fixed-shear accumulation forces a fold at \(S=0\).
## User (2026-04-21 04:08:17)

ok can you double check the latest draft to make sure you captured all your structural findings and goodies, and updated all stale remarks?

## Assistant (2026-04-21 04:08:19)

I’m auditing the latest TeX directly for the mixed 2-point section and for downstream summary remarks, looking for stale “freeze” wording, outdated status summaries, and any missed projective-shadow findings.

I found one concrete stale point already: the new fixed-shear proposition says “\(U(a)=0\)” but its proof still computes \(U(a)=a\). That needs a tiny proof fix. I’m checking whether the summary remarks also still overstate what is proved off \(K_v=0\).

_Thought for 2m 48s_

I checked the latest draft closely. The main structure is in good shape: the projective compactness lemma is in, the exact projective secant-shadow proposition is in, the fixed-shear fold proposition is in, and the stale “automatic affine freezing” language is mostly gone.

I only see four edits worth making.

First, there is one real bug in the fixed-shear fold proposition: the statement and proof define
\[
U(x):=x-\beta S(x)
\]
but then claim \(U(a)=0\). As written, \(U(a)=x(a)\), not \(0\). So that needs a centered definition.

Second, two global summary remarks still do not fully reflect the new sharpening: they do not mention that in the conditional exact fixed-shear lane, the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already reduced to a fold-type projection regime, and one of them also still undercounts the three two-point routes by omitting the quotient-diagonal lane in its closing sentence.

Third, the earlier “What remains in the two-pair rewrite” remark is still accurate, but it can now be tightened in the same way.

Here are the finalized edits.

---

### 1. Fix the centered fold model in Proposition `\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}`

In the **statement** of Proposition `\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}`, replace

```latex
In particular, setting
\[
\beta:=\xi_*-\eta_* x(a)=\frac{1}{S_x(a)},
\]
the first-coordinate fold model
\[
U(x):=x-\beta S(x)
\]
satisfies
\[
U(a)=0,
\qquad
U_x(a)=0,
\qquad
U_{xx}(a)=-\beta S_{xx}(a)\neq 0.
\]
```

with

```latex
In particular, setting
\[
\beta:=\xi_*-\eta_* x(a)=\frac{1}{S_x(a)},
\]
and centering the local $x$-coordinate at $a$, the first-coordinate fold model
\[
U(x):=(x-x(a))-\beta S(x)
\]
satisfies
\[
U(a)=0,
\qquad
U_x(a)=0,
\qquad
U_{xx}(a)=-\beta S_{xx}(a)\neq 0.
\]
```

Then in the **proof** of the same proposition, replace

```latex
Now set
\[
U(x):=x-\beta S(x).
\]
Then
\[
U(a)=a-\beta S(a)=a,
\]
so after translating the source coordinate we may assume $U(a)=0$, and
\[
U_x(a)=1-\beta S_x(a)=0.
\]
Moreover,
\[
U_{xx}(a)=-\beta S_{xx}(a).
\]
```

with

```latex
Now center the local $x$-coordinate at $a$ and set
\[
U(x):=(x-x(a))-\beta S(x).
\]
Then
\[
U(a)=0,
\qquad
U_x(a)=1-\beta S_x(a)=0,
\qquad
U_{xx}(a)=-\beta S_{xx}(a).
\]
```

---

### 2. Tighten Remark `\ref{rem:what-remains-two-pair-rewrite}`

In Remark `\ref{rem:what-remains-two-pair-rewrite}`, replace the final paragraph beginning

```latex
By Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point},
what is automatic from an exact close mixed branch is not affine freezing of
```

and ending with

```latex
or the source-coupling analysis of the mixed $\lambda$-shear route on those
explicit exceptional loci.
```

by:

```latex
By Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point},
what is automatic from an exact close mixed branch is not affine freezing of
\[
(\eta_n,\xi_n,\gamma_n),
\]
but projective compactness of the defect directions
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)],
\qquad
\delta_n(f):=f(h_{1,n})-\Lambda_n f(h_{2,n}).
\]
On any subsequence whose projective limit lies in the affine $\lambda$-chart,
one obtains a convergent affine $\lambda$-shear subsequence; in general the
exact frozen repeated-source reduction is not automatic. The associated
projective secant shadow can nevertheless accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
In the additional conditional exact fixed-shear overlap lane,
Proposition~\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
shows that the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime. Thus the only clearly
genuinely mixed fixed-shear locus left on the overlap patch is
\[
K_v=0,
\]
while the remaining off-$K_v=0$ step is to match the resulting second-coordinate
parity with the existing nonmixed odd-zero
\[
\mathcal R=\frac{T_v}{K_v^2}
\]
package.

So the genuinely remaining two-point work is either the verification of the
finite-order source-level merger criterion, the construction of the actual
corrected two-atom quotient germ with continuity and exact diagonal collapse,
or the source-coupling analysis of the mixed $\lambda$-shear route on those
explicit exceptional loci. More precisely, on the derivative-geometric side one
now needs either projective control of the
\[
S=0
\]
slice without exact freezing, or a proof that the conditional exact fixed-shear
overlap lane is absorbed by the nonmixed odd-zero package.
```

---

### 3. Tighten the long global two-point summary near “At present the two-point side therefore splits into three conditional lanes”

In the long global summary remark, replace the paragraph beginning

```latex
At present the two-point side therefore splits into three conditional lanes:
```

and ending with

```latex
So the remaining structural issue on the two-point side is either verification
of the finite-order merger criterion or source-coupled control of these
explicit mixed exceptional loci.
```

with:

```latex
At present the two-point side therefore splits into three conditional lanes:
the finite-order source-level merger route of
Lemma~\ref{lem:minimal-source-level-two-point-criterion}, the weaker
quotient-diagonal exact exclusion route of
Proposition~\ref{prop:conditional-exact-two-point-exclusion-qabs}, and the
mixed $\lambda$-shear / projective-shadow route on good overlap patches. In the
last route, an exact mixed branch generates moving $\lambda$-shears through
\[
\lambda=\frac{\Delta_7}{v_5},
\]
and
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point}
shows that the automatic compactness is projective:
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\]
admits a convergent subsequence. Only when the projective limit lies in the
affine $\lambda$-chart does one obtain a convergent affine $\lambda$-shear
subsequence, and even then the frozen triple gives only asymptotic, not exact,
fixed-shear transport. The associated projective secant shadow can nevertheless
accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
In the additional conditional exact fixed-shear overlap lane,
Proposition~\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
shows that the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime, so the only clearly
genuinely mixed fixed-shear locus left on the overlap patch is
\[
K_v=0.
\]
So the remaining structural issue on the two-point side is one of three
things: verification of the finite-order merger criterion; the
quotient-diagonal continuity/diagonal-collapse route; or source-coupled
control of these explicit mixed exceptional loci.
```

This fixes the stale omission of the quotient-diagonal route in the last sentence.

---

### 4. Tighten the first paragraph of Remark `\ref{rem:post-draft-findings-established-provisional-live}`

Replace the first paragraph of that remark, from

```latex
First, on the two-point branch, the exact finite-order source criterion remains
```

through

```latex
So the remaining two-point issue is no longer a single broad interaction
ansatz, but a choice among these three explicit closure mechanisms.
```

with:

```latex
First, on the two-point branch, the exact finite-order source criterion remains
the clean algebraic route, but the naive source-summed corrected block model
cannot prove it: along a weighted one-atom path the extracted finite-order
coefficients are even analytic in the source weight. So the remaining two-point
issue now splits into three conditional lanes: the finite-order source-level
merger route, the weaker quotient-diagonal exact exclusion route, and the mixed
$\lambda$-shear / projective-shadow route on good overlap patches. In the last
route, a close exact mixed two-point bad branch generates moving shears through
\[
\lambda=\frac{\Delta_7}{v_5},
\]
and
Proposition~\ref{prop:projective-compactness-moving-lambda-shear-two-point}
shows that the automatic compactness is projective:
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]
\]
admits a convergent subsequence. Only when the projective limit lies in the
affine $\lambda$-chart does one obtain a convergent affine $\lambda$-shear
subsequence, and even then the limiting triple yields only asymptotic, not
exact, fixed-shear transport. The associated projective secant shadow can
nevertheless accumulate only on
\[
\{S=0\}\cup\{K_v=0\},
\qquad
S=\frac{\Delta_7}{c\,v_5}.
\]
In the additional conditional exact fixed-shear overlap lane,
Proposition~\ref{prop:fixed-shear-overlap-branch-off-Kv-forces-fold-at-S-zero}
shows that the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime. Thus the only clearly
genuinely mixed fixed-shear locus left on the overlap patch is
\[
K_v=0,
\]
while the off-$K_v=0$ missing step is to match the resulting second-coordinate
parity with the existing nonmixed odd-zero
\[
\mathcal R=\frac{T_v}{K_v^2}
\]
package. So the remaining two-point issue is no longer a single broad
interaction ansatz, but a choice among these three explicit closure mechanisms.
```

---

After these four edits, I think the draft does capture the current structural picture cleanly:

- projective compactness, not automatic affine freezing;
- exact projective secant-shadow reduction;
- conditional fixed-shear sharpening off \(K_v=0\) to a fold-type regime;
- the only clearly genuinely mixed fixed-shear locus left on the overlap patch is \(K_v=0\);
- and the three two-point lanes are described consistently in the global summaries.
## User (2026-04-21 04:12:45)

ok give me a full summary of what you learned to hand back to the two-point team lead

## Assistant (2026-04-21 04:13:09)

_Thought for 22s_

Here is the handback I’d give the two-point lead.

The main conclusion is that the original “freeze the \(\lambda\)-shear” target needs to be weakened, but the derivative-geometric route actually comes out cleaner after that weakening.

What is false is the strong affine freezing claim. If one writes
\[
\delta_n f:=f(h_{1,n})-\Lambda_n f(h_{2,n}),
\]
then the mixed branch equations are
\[
\delta_n(c)=\eta_n\,\delta_n(\lambda),\qquad
\delta_n(v_5)=\xi_n\,\delta_n(\lambda),\qquad
\delta_n(u_5)=\gamma_n\,\delta_n(\lambda).
\]
So on the chart \(\delta_n(\lambda)\neq 0\),
\[
\eta_n=\frac{\delta_n(c)}{\delta_n(\lambda)},\qquad
\xi_n=\frac{\delta_n(v_5)}{\delta_n(\lambda)},\qquad
\gamma_n=\frac{\delta_n(u_5)}{\delta_n(\lambda)}.
\]
But these affine shears need not admit a finite convergent subsequence. They can blow up if \(\delta_n(\lambda)\) vanishes to higher order than the other defects. I checked this explicitly: there are clean good-overlap examples with exact moving-shear identities and \((\eta_n,\xi_n,\gamma_n)\to\infty\). So automatic affine freezing is not a theorem.

Even when the affine shears do converge, that still does not produce exact repeated-source transport for one fixed limiting triple \((\eta_*,\xi_*,\gamma_*)\). What one gets is only
\[
\delta_n(c-\eta_*\lambda)=(\eta_n-\eta_*)\,\delta_n(\lambda),
\]
\[
\delta_n(v_5-\xi_*\lambda)=(\xi_n-\xi_*)\,\delta_n(\lambda),
\]
\[
\delta_n(u_5-\gamma_*\lambda)=(\gamma_n-\gamma_*)\,\delta_n(\lambda),
\]
so the frozen system is only asymptotic, not exact. That is the second place where the naive freeze lemma fails.

What is true, and is enough for the derivative geometry, is projective compactness. The exact close mixed branch always gives a projective defect direction
\[
[\delta_n(c):\delta_n(v_5):\delta_n(u_5):\delta_n(\lambda)]\in\mathbf P^3,
\]
and after subsequence this always converges. So the right compactness statement is projective, not affine. Affine \(\lambda\)-freezing only occurs conditionally, on a subsequence whose projective limit lands in the \(\delta(\lambda)\neq 0\) chart.

The strongest positive result is that the downstream secant-shadow theorem does not need affine freezing at all. It is already exact, pointwise, along the moving-shear branch. On a good overlap patch, with
\[
\lambda=\frac{\Delta_7}{v_5},\qquad
x=\frac{v_5}{c},\qquad
Y=\frac{u_5}{c},\qquad
S=\frac{\lambda}{c}=\frac{\Delta_7}{c\,v_5},
\]
an exact mixed branch with moving shears determines an exact common projective value
\[
\Sigma_n=[B_n(h_{1,n}):F_n(h_{1,n}):A_n(h_{1,n})]
      =[B_n(h_{2,n}):F_n(h_{2,n}):A_n(h_{2,n})],
\]
where
\[
A_n=c-\eta_n\lambda,\qquad
B_n=v_5-\xi_n\lambda,\qquad
F_n=u_5-\gamma_n\lambda.
\]
And this common value is independent of the moving shears and of \(\Lambda_n\). Explicitly,
\[
\Sigma_n
=
[x_1S_2-x_2S_1:\ Y_1S_2-Y_2S_1:\ S_2-S_1].
\]
Equivalently, in raw coordinates,
\[
\Sigma_n
=
[v_{5,1}\lambda_2-v_{5,2}\lambda_1:\ u_{5,1}\lambda_2-u_{5,2}\lambda_1:\ c_1\lambda_2-c_2\lambda_1].
\]

So the moving-shear branch already collapses exactly to a projective secant-shadow problem. This is better than the original fixed-shear plan: the shadow theorem is exact without any freezing hypothesis.

On the diagonal, these secant shadows converge to the tangent shadow
\[
\Pi(a)=
[xS_x-S:\ YS_x-SY_x:\ S_x]\big|_{a},
\]
and the projective immersion defect is controlled by
\[
\Pi(x)\wedge \partial_x\Pi(x)
=
S(x)\bigl(S_xY_{xx}-S_{xx}Y_x,\ S_{xx},\ -S_{xx}\bigr).
\]
Hence the tangent shadow is projectively immersive wherever
\[
S\neq 0,\qquad S_{xx}\neq 0.
\]
On the \(v_5\)-patch one has
\[
K_v=(x')^3S_{xx},
\]
so any close exact mixed two-point branch can accumulate only on
\[
\{S=0\}\cup\{K_v=0\}.
\]

That is the central derivative-geometric reduction. It is now exact, projective, and unconditional.

There is also a useful conditional sharpening in the exact fixed-shear lane. If one separately assumes an exact fixed-shear overlap branch
\[
\Phi(x)=\left(\frac{x-\xi_*S}{1-\eta_*S},\frac{Y-\gamma_*S}{1-\eta_*S}\right),
\qquad
\Phi(x_{1,n})=\Phi(x_{2,n}),
\]
and the accumulation point satisfies \(K_v(a)\neq 0\), then the projective-shadow theorem forces
\[
S(a)=0.
\]
Moreover the fixed-shear repeated-value condition forces
\[
\Phi'(a)=0,
\]
and in particular
\[
0=\Phi_1'(a)=1-(\xi_*-\eta_*x(a))S_x(a),
\]
so
\[
S_x(a)\neq 0.
\]
If
\[
\beta:=\xi_*-\eta_*x(a)=\frac1{S_x(a)},
\]
then the first-coordinate model
\[
U(x)=(x-x(a))-\beta S(x)
\]
satisfies
\[
U(a)=0,\qquad U_x(a)=0,\qquad U_{xx}(a)=-\beta S_{xx}(a)\neq 0,
\]
because \(K_v(a)\neq 0\) implies \(S_{xx}(a)\neq 0\). So off \(K_v=0\), the exact fixed-shear lane is already forced into a fold-type projection regime. The only missing step there is to identify the second-coordinate parity with the existing nonmixed odd-zero \(\mathcal R\)-package. I do not think the draft currently proves that identification yet, so it should be described as the remaining off-\(K_v=0\) task, not as done.

So the current structural picture for the two-point side is:

The automatic compactness theorem is projective compactness of defect directions, not affine freezing of \((\eta_n,\xi_n,\gamma_n)\).

The downstream secant-shadow reduction is exact and fully projective. No affine freezing is needed to get the derivative-geometric obstruction.

The exact mixed branch can accumulate only on
\[
\{S=0\}\cup\{K_v=0\}.
\]

In the additional conditional exact fixed-shear overlap lane, the slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already forced into a fold-type projection regime. So the only clearly genuinely mixed fixed-shear locus left on the overlap patch is
\[
K_v=0.
\]

The big remaining tasks are now very sharply split into three lanes:

First, the finite-order source-level merger route.

Second, the quotient-diagonal continuity / exact diagonal-collapse route.

Third, the mixed \(\lambda\)-shear derivative-geometric route, which now itself splits into two subproblems: either control the
\[
S=0
\]
slice projectively without exact freezing, or prove that the conditional exact fixed-shear overlap lane off \(K_v=0\) is absorbed by the existing nonmixed odd-zero \(\mathcal R\)-package. And on the genuinely mixed side, show that accumulation on
\[
K_v=0
\]
is absorbed by the existing lifted \(3\)-point machinery.

So the handback in one sentence is: the strong freeze lemma is false, but the secant-shadow theorem becomes exact and cleaner in projective form, and this reduces the two-point derivative-geometric burden to the explicit exceptional set
\[
\{S=0\}\cup\{K_v=0\},
\]
with only \(K_v=0\) still looking clearly genuinely mixed.
