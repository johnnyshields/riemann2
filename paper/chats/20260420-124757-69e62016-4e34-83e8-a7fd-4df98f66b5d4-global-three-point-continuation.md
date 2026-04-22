# Global Three-Point Continuation

- Source: https://chatgpt.com/c/69e62016-4e34-83e8-a7fd-4df98f66b5d4
- Created: 2026-04-20 12:47:57 UTC
- Default model: gpt-5-4-thinking

---

## User (2026-04-20 12:47:56)

We are trying to prove the Riemann Hypothesis. A paper draft is attached.

## Your Task — global three-point continuation / nonrecurrence

Please work only on the **global three-point branch** in the attached paper draft. Do **not** spend time on the (2)-point theorem or the (4)-point mixed/nonmixed branches unless strictly necessary.

### Objective

Try to close the remaining **global three-point theorem**: continuation / nonrecurrence of the odd-order branch, together with exclusion of infinite-order flatness.

The local three-point branch classification is already mostly done. I want you to work on the **global** step now.

### Current state to assume

From the draft, the broad picture is:

* the local geometry near finite-order (K_v)-zeros is already classified;
* even-order (K_v)-zeros do not produce the opposite-side branch;
* odd-order (K_v)-zeros produce exactly one local branch;
* so the remaining problem is not local classification but:

  * **global continuation** of that odd-order branch,
  * **nonrecurrence / non-return** control,
  * and exclusion of **infinite-order flatness**.

### Your job

Please do all of the following:

1. **State the exact global theorem that the draft still needs on the three-point branch.**
   I want the cleanest theorem statement you can formulate.

2. **Audit what the draft already proves locally.**
   Be exact about what can already be assumed:

   * uniqueness of the odd-order local branch,
   * what happens at even order,
   * what regularity or nondegeneracy assumptions are already available.

3. **Attack the global continuation / nonrecurrence step.**
   Try to prove:

   * branch continuation,
   * no pathological recurrence,
   * no infinite-order flatness,
   * no hidden accumulation mechanism that would keep the three-point bad set alive.

### Routes to attack

Please prioritize these routes:

#### Route A: branch continuation theorem

Take the already-classified local odd-order branch and try to show it extends uniquely until it either exits the good region or hits a controlled endpoint. Then analyze what endpoints are possible.

#### Route B: nonrecurrence / no-return argument

Try to show the odd-order branch cannot recur, self-intersect, or re-enter the same local configuration in a way that preserves the bad-core mechanism.

#### Route C: infinite-order flatness exclusion

Audit whether the draft already nearly rules this out. If not, identify the exact analytic lemma still needed.

#### Route D: compactness / first-zero style global contradiction

If the draft has a first-zero / compact truncation mechanism, see whether it can be upgraded into the missing global theorem.

### Non-goals

Do **not** spend time on:
* the source-level two-point theorem,
* the mixed (4)-point patch dichotomy,
* the nonmixed (4)-point obstruction coefficients
(these will be worked on in other chats)

## Assistant (2026-04-20 12:47:57)

I’m going straight into the draft and isolating just the three-point global branch: what is already local, what the exact missing theorem should be, and whether the existing first-zero machinery can be promoted to the global step.

I found the key local three-point block. There’s a clean adjacent-pair continuation theorem available already from the draft’s setup, and infinite-order flatness looks easier than it sounds: analyticity plus the existing non-affinity lemma should kill it outright.

I’ve got the shape of the answer now. The adjacent-pair continuation is cleaner than it first looks: the repeated-node equation has a one-sided nonvanishing derivative that forces the branch to be a genuine analytic graph. The part that still looks genuinely missing is narrower: ruling out source-coordinate return, which is exactly the same as ruling out an interior common-tangent point on that graph.

_Thought for 15m 6s_

I went through the three-point part only, and the good news is that the global problem is narrower than it looks.

The draft does **not** yet prove the full global three-point closure. But it already proves enough local structure that the remaining global issue can be isolated very sharply:

- **infinite-order flatness is already killable** from the current setup;
- the odd-order local branch can be promoted to a **unique maximal analytic continuation**;
- there is **no hidden interior accumulation or branching**;
- the remaining real gap is a **global no-return / no-common-tangent theorem** for that continued branch.

Here is the clean picture.

---

## 1. The exact global theorem the draft still needs

On a good \(v_5\)-patch, write
\[
x=\frac{v_5}{c},\qquad S(x)=\sigma_v=\frac{\Delta_7}{c\,v_5},
\]
so \(x\) is the local parameter and the repeated-node three-point equation is
\[
H_3(a,u)=S(u)-S(a)-S'(a)(u-a).
\]
This is the tangent-contact equation: the tangent line at \(a\) passes through \(u\).

The clean global theorem still needed is, in my view, the following.

**Global three-point nonrecurrence theorem (needed).**  
Let \(P\Subset\{c\neq0,\ M\neq0,\ v_5\neq0\}\) be a compact good \(v_5\)-patch, and let \(x_0\in x(P)\) be an odd-order zero of \(K_v\). Let \(C_{x_0}\) be the unique local opposite-side branch of
\[
H_3(a,u)=0,\qquad a<u,
\]
whose closure contains \((x_0,x_0)\). Then \(C_{x_0}\) admits a unique maximal continuation in the good region, and its closure can meet the curvature-zero locus only at the birth point \((x_0,x_0)\); equivalently, the tangent-line data generated by the source side does not recur against later branches. Hence no defect-free lifted \(3\)-point bad branch survives on \(P\).

A slightly weaker but still sufficient version is:

**Equivalent sharp form.**  
Along the maximal continuation of the odd-order branch, one never has
\[
H_3(a,u)=0,\qquad \partial_u H_3(a,u)=0.
\]
Since
\[
\partial_u H_3(a,u)=S'(u)-S'(a),
\]
this is exactly the statement that the tangent line at \(a\) never becomes a **common tangent** at \(u\). That is the cleanest “no-return” theorem.

So the global theorem is really a **no common-tangent recurrence theorem** for the lifted planar curve \(\Lambda_v=(x,S)\).

---

## 2. What the draft already proves locally

The draft already gives the following local package.

On a good \(v_5\)-patch:

\[
K_v=(x')^3 S''(x),
\]
so \(K_v=0\) is exactly the lifted curvature-zero set.

Also, on any connected interval where \(K_v\) has fixed nonzero sign, the triple
\[
1,\ x,\ S
\]
is an ECT system. So within one such interval, no affine line meets \(\Lambda_v\) in three points. That means any three-point bad set must cross the \(K_v=0\) locus.

The draft also proves:

- shrinking exact lifted \(3\)-point circuits concentrate into \(K_v=0\);
- repeated-node limits are governed by \(H_3(a,u)=0\);
- near an isolated finite-order zero of \(K_v\), after affine normalization
  \[
  S(x)=x^m+O(x^{m+1}),\qquad m=r+2,\quad r=\ord_0 K_v,
  \]
  one has:
  - if \(r\) is even, there is **no** opposite-side branch;
  - if \(r\) is odd, there is **exactly one** real-analytic opposite-side branch.

So the local picture is already strong enough to justify your summary:

- even-order \(K_v\)-zeros are sterile for the opposite-side branch;
- odd-order \(K_v\)-zeros create exactly one local branch;
- the remaining problem is global continuation / nonrecurrence, not local ambiguity.

The regularity available is also enough: on a good patch, \(x\) is an analytic coordinate because \(M\neq0\), so \(S\) is analytic as a function of \(x\), and \(H_3(a,u)\) is analytic in both variables.

---

## 3. What can actually be proved now on the global step

This is the main useful part.

### A. Infinite-order flatness is already excluded

I think this part is essentially done already from the draft’s present ingredients.

Because \(x\) is an analytic coordinate on a good patch and
\[
K_v=(x')^3S''(x),
\]
the function \(S''(x)\) is analytic.

If \(K_v\) had an infinite-order zero at some interior point \(x_*\), then \(S''\) would also vanish to infinite order there. Since \(S''\) is analytic, that forces
\[
S''\equiv 0
\]
on a neighborhood of \(x_*\). Hence \(S\) is affine in \(x\) on that neighborhood.

But the draft already proves that \(S=\sigma_v\) is **not affine in \(x\)** on any connected good interval.

So:

**Conclusion.** Every zero of \(K_v\) on a good \(v_5\)-patch is automatically of finite order. There is no infinite-order flatness left to exclude by a new hard theorem.

That means the “infinite-order flatness” item can be downgraded from a major open obstruction to a short analytic corollary.

---

### B. The odd-order branch has a unique maximal continuation

This part also goes through cleanly.

Differentiate:
\[
H_3(a,u)=S(u)-S(a)-S'(a)(u-a).
\]
Then
\[
\partial_a H_3(a,u)=-(u-a)S''(a),
\qquad
\partial_u H_3(a,u)=S'(u)-S'(a).
\]

Now fix the source interval \(I_-\) immediately to the left of an odd-order zero \(x_0\), so \(S''\neq0\) on \(I_-\), and look at
\[
\mathcal T:=\{(a,u): a\in I_-,\ u>x_0,\ H_3(a,u)=0\}.
\]

On \(\mathcal T\), since \(u>a\), one has
\[
\partial_a H_3(a,u)=-(u-a)S''(a)\neq 0.
\]
Therefore every connected component of \(\mathcal T\) is locally an analytic graph
\[
a=A(u).
\]

In fact it is globally a graph on each connected component. The reason is simple: if one component hit the same \(u\)-value twice, then along a path inside that component the function \(u\) would have an interior extremum; at such a point the tangent vector would satisfy \(u'=0\), and differentiating \(H_3=0\) along the path would force \(\partial_a H_3=0\), impossible.

So the unique local odd-order branch born at \((x_0,x_0)\) extends uniquely to a **maximal analytic graph**
\[
a=A(u),\qquad u\in U
\]
for some maximal open interval \(U\subset(x_0,\beta)\) inside the patch.

This gives:

- unique continuation;
- no self-intersection;
- no interior branching;
- no hidden interior accumulation.

So Route A is basically solved in the following precise sense:

**What is proved now.** The local odd-order branch does continue uniquely and analytically as long as the source side stays in the same ECT interval. The only possible failures are boundary phenomena, not local or interior ones.

---

### C. Nonrecurrence reduces exactly to common tangency

This is the sharp reduction.

Since \(a=A(u)\) along the maximal branch,
\[
A'(u)=-\frac{\partial_u H_3}{\partial_a H_3}
=
\frac{S'(u)-S'(a)}{(u-a)S''(a)}.
\]

Therefore:
\[
A'(u)=0 \iff S'(u)=S'(a).
\]

But together with \(H_3(a,u)=0\), the condition
\[
S'(u)=S'(a)
\]
means the tangent line at \(a\) is also tangent at \(u\). So it is a **common tangent**.

This is the exact obstruction to no-return.

- If \(A'(u)\neq0\) everywhere on the continued branch, then \(u\) can also be solved as a graph of \(a\), so the source coordinate never turns around or returns.
- If the source coordinate ever returns to a previously visited value, then by Rolle there must be a point where \(A'(u)=0\), hence a common tangent point.

So Route B reduces to one very sharp lemma:

**Missing lemma.** Along the maximal odd-order branch, there is no interior point with
\[
H_3(a,u)=0,\qquad \partial_u H_3(a,u)=0.
\]

Equivalently: no common tangent can occur along that branch.

That is, in my view, the exact global theorem the draft still lacks.

---

### D. No hidden accumulation mechanism remains

On a compact good patch, \(K_v\) is analytic and not identically zero on any interval, so its zero set is finite. Even-order zeros are sterile, odd-order zeros seed exactly one local branch.

Combine that with the maximal-graph result above:

- there are only finitely many odd-order seed points;
- each seed gives at most one maximal analytic continuation arc;
- each such arc is a genuine graph in the target variable \(u\);
- there is no interior branching or diffuse accumulation.

So the three-point bad set, on a compact good patch, is forced into a **finite analytic arc geometry**. There is no longer any plausible “wild” mechanism that keeps it alive.

The only remaining survival modes are finite and rigid:

1. a continued arc reaches the patch boundary / exits the good region; or
2. it develops a common-tangent return.

That is a strong upgrade of Route D.

---

## 4. What I think the paper can already claim, honestly

I would not claim the full global three-point theorem yet.

But I do think the paper can already claim a much sharper intermediate theorem than it currently does:

**Proved reduction theorem.**  
On a good \(v_5\)-patch, every \(K_v\)-zero is finite order; every odd-order zero seeds exactly one local repeated-node three-point branch; and that branch admits a unique maximal analytic continuation as a graph in the target variable. Hence the only remaining obstruction to global three-point closure is common-tangent recurrence of that graph (equivalently \(\partial_u H_3=0\) somewhere along it), not continuation ambiguity, not infinite-order flatness, and not hidden accumulation.

That is a real advance.

---

## 5. Bottom line

My honest assessment is:

- **Infinite-order flatness:** already dead.
- **Branch continuation:** essentially done, in the precise “maximal analytic graph” sense.
- **Nonrecurrence / no-return:** not yet done.
- **Exact remaining theorem:** exclude interior common-tangent recurrence along the maximal odd-order branch.

So the global three-point problem is now much more focused than “global continuation/nonrecurrence” makes it sound. The continuation part is basically under control. The real missing theorem is a **global no-common-tangent recurrence theorem for the lifted curve \(\Lambda_v=(x,S)\)**.

If you want, the next best step is for me to turn this into exact LaTeX insertions: one theorem for “no infinite-order flatness,” one proposition for “maximal graph continuation,” and one remark/theorem target isolating the no-common-tangent lemma as the only remaining global three-point gap.
## User (2026-04-20 13:05:16)

attack the missing theorem!

## Assistant (2026-04-20 13:05:17)

I’m drilling into the repeated-node equation itself now. The key is whether the common-tangent condition can be turned into an immediate contradiction, or at least reduced to one rigid auxiliary ODE/monotonicity statement already latent in the draft.

I found a real lever. The right parameter is not \(u\) but the source tangent slope \(m=S'(a)\): the tangent intercept gap between the source branch and any target tangent branch has derivative exactly “target point minus source point,” so it is strictly monotone. That kills interior common tangency.

_Thought for 13m 39s_

I think there is a real theorem here, and it is stronger than the earlier reduction.

Let me write it in the draft’s \(x\)-chart language:
\[
x=\frac{v_5}{c},\qquad S(x)=\sigma_v(x)=\frac{\Delta_7}{c\,v_5},
\]
so on a good \(v_5\)-patch
\[
K_v=(x')^3 S''(x),
\qquad
H_3(a,u)=S(u)-S(a)-S'(a)(u-a).
\]

Take an isolated odd-order zero \(x_0\) of \(K_v\). After the same affine normalization already used in the local theorem, we may assume
\[
x_0=0,\qquad S(0)=S'(0)=0,
\]
and we choose the source side so that
\[
S''<0 \text{ on } I_-=(\alpha,0),\qquad S''>0 \text{ on } I_1=(0,\beta_1).
\]
That is exactly the local odd-order birth configuration.

What follows is the global theorem I think you can now prove.

---

## The theorem

**Theorem (global continuation / nonrecurrence of the odd-order lifted \(3\)-point branch).**  
Let \(x_0=0\) be an isolated odd-order zero of \(K_v\) on a good \(v_5\)-patch, with source interval \(I_-=(\alpha,0)\) as above. Then:

1. every zero of \(K_v\) on the patch is finite order;

2. the unique local opposite-side branch from
\[
H_3(a,u)=0,\qquad a<0<u,
\]
extends to a unique maximal connected branch \(\mathcal C\);

3. \(\mathcal C\) admits a piecewise-real-analytic parametrization by the source tangent slope
\[
m=S'(a);
\]
in particular the source coordinate is strictly monotone, so there is no source-side recurrence and no self-return of the branch;

4. on every open segment of \(\mathcal C\),
\[
\partial_u H_3(a,u)=S'(u)-S'(a)\neq 0,
\]
so there is no interior common-tangent event and no interior failure of continuation;

5. if \(\mathcal C\) reaches a target-side zero \(u_*\) of \(K_v\), then that endpoint is completely controlled:
   - if \(\ord_{u_*}K_v\) is even, the branch terminates there;
   - if \(\ord_{u_*}K_v\) is odd, the branch crosses uniquely into the next ECT interval.

Hence the odd-order branch has no pathological recurrence, no interior accumulation, and no infinite-order flatness. Its only possible endpoints are controlled \(K_v\)-boundary hits or exit from the ambient good region.

---

## Why this works

The key move is to parametrize by the **source tangent slope**, not by \(a\) or \(u\).

On the source interval \(I_-\), since \(S''\neq 0\), the slope map
\[
a\mapsto m=S'(a)
\]
is a real-analytic diffeomorphism onto an open interval \(J_-\). Write its inverse as \(a=a(m)\).

Define the source tangent intercept
\[
\tau_-(m):=S(a(m))-m\,a(m).
\]
A standard envelope calculation gives
\[
\tau_-'(m)=-a(m).
\]

Now take any target interval \(I\) on the right of \(0\) on which \(S''\) has fixed sign, and suppose \(m\) lies in the slope range of \(I\). Then there is a unique tangent point \(u_I(m)\in I\) with
\[
S'(u_I(m))=m.
\]
Define its tangent intercept
\[
\tau_I(m):=S(u_I(m))-m\,u_I(m).
\]
Again,
\[
\tau_I'(m)=-u_I(m).
\]

So the intercept gap
\[
D_I(m):=\tau_-(m)-\tau_I(m)
\]
satisfies the exact identity
\[
D_I'(m)=u_I(m)-a(m).
\]
Because every target point is to the right of the source point,
\[
u_I(m)-a(m)>0,
\]
hence
\[
\boxed{D_I'(m)>0.}
\]

That monotonicity is the whole game.

---

## Step 1: infinite-order flatness is already gone

This part is immediate from the current draft.

On a good patch, \(S''\) is analytic and
\[
K_v=(x')^3S''.
\]
If \(K_v\) vanished to infinite order at some interior point, then \(S''\) would too, hence \(S''\equiv 0\) locally by analyticity. So \(S\) would be affine in \(x\), contradicting the draft’s non-affinity proposition for \(\sigma_v\).

So every \(K_v\)-zero is finite order. There is no infinite-order flatness left.

---

## Step 2: the first branch is born with positive intercept gap

The local theorem already proves that at the odd-order birth point \(0\), there is a unique local branch
\[
H_3(a,u)=0,\qquad a<0<u.
\]

In slope language, for \(m>0\) small, the tangent line from the source point \(a(m)\) meets the first right-hand interval \(I_1\) at a genuine point \(u(m)\), but is **not** tangent there. Since \(I_1\) is convex, that means the source tangent line lies strictly above the right-hand tangent line of the same slope. Equivalently,
\[
D_{I_1}(m)>0
\qquad (m>0 \text{ small}).
\]

Because \(D_{I_1}'(m)>0\), this immediately propagates:

\[
\boxed{D_{I_1}(m)>0 \text{ on the whole connected overlap of slope ranges.}}
\]

So an interior common tangent with the first target interval is impossible.

---

## Step 3: common tangency is impossible on any later interval too

Suppose the continued branch later enters some further target interval \(I_j\) on the right, through a boundary point \(x_j\in\{K_v=0\}\).

At the entry slope \(m_j\), continuity gives
\[
\tau_-(m_j)=S(x_j)-m_j x_j.
\]
But the boundary point \(x_j\) is itself the tangent point of \(I_j\) at slope \(m_j\), so
\[
\tau_{I_j}(m_j)=S(x_j)-m_j x_j.
\]
Hence
\[
D_{I_j}(m_j)=0.
\]

Now use monotonicity:
\[
D_{I_j}'(m)=u_{I_j}(m)-a(m)>0.
\]
Therefore, for every \(m\) after the entry point,
\[
D_{I_j}(m)>0.
\]

But interior common tangency on \(I_j\) would mean exactly
\[
\tau_-(m)=\tau_{I_j}(m),
\]
that is,
\[
D_{I_j}(m)=0,
\]
which is impossible.

So once a new interval is entered, the branch can never suffer an interior common-tangent failure there.

This proves the missing no-return/nonrecurrence statement in the precise sense that the only possible singular events are at controlled boundary hits, never in the interior.

---

## Step 4: why the branch continues uniquely on open segments

Let
\[
\Phi(m,u):=S(u)-m\,u-\tau_-(m).
\]
The branch is \(\Phi(m,u)=0\).

Differentiate:
\[
\partial_u\Phi(m,u)=S'(u)-m.
\]

On an open segment of the branch, interior common tangency has just been excluded, so
\[
\partial_u\Phi\neq 0.
\]
Hence by the implicit function theorem, the branch is a real-analytic graph
\[
u=u(m)
\]
on each open segment.

Differentiate the identity \(\Phi(m,u(m))=0\):
\[
(S'(u)-m)u'(m)=u-a(m).
\]
So
\[
\boxed{
u'(m)=\frac{u-a(m)}{S'(u)-m}.
}
\]
In particular \(u'(m)\neq 0\) on every regular segment, because \(u>a(m)\) and \(S'(u)-m\neq 0\). So the branch cannot stall or fold inside a segment.

Also
\[
a'(m)=\frac1{S''(a(m))}<0
\]
on the chosen source side, so the source coordinate is strictly monotone throughout. That kills source-side recurrence.

---

## Step 5: what happens at a boundary \(K_v=0\) hit

Now suppose the branch reaches a target-side boundary point \(u_*\) where \(K_v(u_*)=0\). Set
\[
m_*:=S'(u_*).
\]
Then
\[
\Phi(m_*,u_*)=0,\qquad \partial_u\Phi(m_*,u_*)=0.
\]

Expand in \(u-u_*\):
\[
\Phi(m_*,u)
=
\sum_{k\ge 2}\frac{S^{(k)}(u_*)}{k!}(u-u_*)^k.
\]
If
\[
r=\ord_{u_*}K_v=\ord_{u_*}S'',
\]
then the first nonzero term occurs at order
\[
r+2.
\]

So locally
\[
\Phi(m_*,u)=c\,(u-u_*)^{r+2}+O\!\bigl((u-u_*)^{r+3}\bigr),
\qquad c\neq 0.
\]

Now the parity is decisive.

If \(r\) is even, then \(r+2\) is even. The root is one-sided: no sign change, so the branch cannot pass through. It stops there.

If \(r\) is odd, then \(r+2\) is odd. The root changes sign, so the zero crosses uniquely through \(u_*\). The branch continues into the next interval.

So the endpoint classification is completely controlled by the same parity that already appears in the local theorem.

---

## What this buys you

I think this genuinely closes the “global three-point branch” theorem in the sense you asked for:

- **continuation**: yes, piecewise-analytic maximal continuation exists;
- **nonrecurrence / no-return**: yes, because the source slope parameter is monotone and interior common tangency is impossible;
- **no infinite-order flatness**: yes, already forced by analyticity plus non-affinity;
- **no hidden accumulation**: yes, because \(K_v\)-zeros are discrete and finite on compact patches, and the branch can only change behavior at those controlled points.

So the three-point branch is no longer a vague global topological problem. It is a rigid one-dimensional object with explicitly classified transitions.

The one thing this theorem does **not** automatically give is a final contradiction saying the branch cannot reach the outer edge of whatever compact patch you are working on. If your intended endgame is “there is no three-point bad set anywhere,” you would still need one last endpoint argument to prevent escape through the ambient boundary. But the continuation / nonrecurrence / flatness theorem itself looks closed.

If you want, I’ll turn this into exact LaTeX insertions with theorem/proposition/lemma statements and proofs in the draft’s notation.
## User (2026-04-20 13:24:20)

yes, please turn this into the final latex insertions for the draft. capture not just the theorem/proof but any useful identities/structural findings/goodies, and update all related sections, also remove related wip-* and audit-* remarks where appropriate. If we need a wip saying "we aren't saying branch cannot reach the outer edge..." then add it, otherwise, if its clearly implicit in the draft structure, no wip is needed.

## Assistant (2026-04-20 13:24:22)

I’m mapping the exact insertion points now: the repeated-node equation, the local odd-order branch theorem, and the current WIP/audit remarks around three-point global continuation so I can give you precise replacements rather than loose prose.

_Thought for 15m 21s_

Here are the exact LaTeX edits I would make.

## 1) Insert the global three-point package

Insert this entire block **immediately after**
`Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero}`
and its proof, and **before**
`Remark~\ref{rem:nonmixed-four-point-zeros-can-carry-preexisting-branches}`.

```latex
\begin{corollary}[No infinite-order flatness for $K_v$ on a good $v_5$-patch]
\label{cor:no-infinite-order-flatness-Kv-good-vpatch}
On a good $v_5$-patch, every zero of $K_v$ has finite order.
Equivalently, the lifted curvature $S''(x)$ has no infinite-order zero on such a
patch.
\end{corollary}

\begin{proof}
By Proposition~\ref{prop:exact-x-coordinate-identities-lifted-four-point},
\[
K_v=(x')^3S''(x),
\]
and on a good $v_5$-patch one has $x'\neq 0$. Thus $K_v$ and $S''$ have the
same zero set and the same vanishing order.

If $K_v$ had an infinite-order zero at some interior point $x_*$, then so would
$S''$. Since $S''$ is analytic in the local coordinate $x$, this would force
\[
S''\equiv 0
\]
on a neighborhood of $x_*$. Hence $S$ would be affine in $x$ there, contrary to
Proposition~\ref{prop:sigmav-not-affine-in-x}.
\end{proof}

\begin{lemma}[Slope--intercept parametrization for the lifted $3$-point branch]
\label{lem:slope-intercept-parametrization-lifted-three-point}
Assume the affine normalization from
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero},
so that
\[
S(0)=S'(0)=0,
\qquad
S''<0\ \text{on the source side }I_-=(\alpha,0).
\]
Let
\[
I_+=(0,\beta)
\]
be the maximal open interval to the right of $0$ on which $S'$ is strictly
increasing. Equivalently, $S''$ does not change sign on $I_+$, and any zeros of
$S''$ there are isolated even-order zeros.

For
\[
m\in J_-:=S'(I_-),
\]
define the inverse source point
\[
a=a(m):=(S'|_{I_-})^{-1}(m),
\]
and the source tangent intercept
\[
\tau_-(m):=S(a(m))-m\,a(m).
\]
For
\[
m\in J_+:=S'(I_+),
\]
define the inverse target tangent point
\[
u_+(m):=(S'|_{I_+})^{-1}(m),
\]
and the target tangent intercept
\[
\tau_+(m):=S(u_+(m))-m\,u_+(m).
\]
Then
\[
\tau_-'(m)=-a(m),
\qquad
\tau_+'(m)=-u_+(m).
\]
Hence on
\[
J:=J_-\cap J_+
\]
the intercept gap
\[
D(m):=\tau_-(m)-\tau_+(m)
\]
satisfies
\[
D'(m)=u_+(m)-a(m)>0.
\]
\end{lemma}

\begin{proof}
Differentiate
\[
\tau_-(m)=S(a(m))-m\,a(m)
\]
to obtain
\[
\tau_-'(m)=S'(a(m))a'(m)-a(m)-m\,a'(m)=-a(m),
\]
because $S'(a(m))=m$. The same computation gives
\[
\tau_+'(m)=-u_+(m).
\]
Subtracting yields
\[
D'(m)=u_+(m)-a(m).
\]
Since $a(m)<0<u_+(m)$, the derivative is strictly positive.
\end{proof}

\begin{theorem}[Global continuation / nonrecurrence of the odd-order lifted $3$-point branch]
\label{thm:global-continuation-nonrecurrence-odd-three-point-branch}
Assume the hypotheses and affine normalization of
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero},
and suppose that $r=\operatorname{ord}_0K_v$ is odd, so the unique local
opposite-side branch exists.

Let
\[
I_-=(\alpha,0)
\]
be the source interval on which $S''<0$, and let
\[
I_+=(0,\beta)
\]
be the maximal open interval to the right of $0$ on which $S'$ is strictly
increasing. Set
\[
J:=S'(I_-)\cap S'(I_+).
\]
Then there exists a unique maximal open interval
\[
J_{\mathrm{br}}=(0,m_*)\subset J
\]
and a unique real-analytic function
\[
u:J_{\mathrm{br}}\to I_+
\]
such that
\[
H_3(a(m),u(m))=0,
\qquad
a(m):=(S'|_{I_-})^{-1}(m),
\qquad
u(m)>0,
\]
and for small $m>0$ this branch agrees with the local branch from
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero}.

Moreover:
\begin{enumerate}
\item the intercept gap
\[
D(m):=\tau_-(m)-\tau_+(m)
\]
is strictly positive on all of $J$, and
\[
D'(m)=u_+(m)-a(m)>0;
\]

\item along the branch one has
\[
\partial_u H_3(a(m),u(m))
=
S'(u(m))-m
\neq 0,
\]
so there is no interior common-tangent event;

\item the branch is uniquely continued on $J_{\mathrm{br}}$, with
\[
u'(m)=\frac{u(m)-a(m)}{S'(u(m))-m},
\]
and the source coordinate is strictly monotone,
\[
a'(m)=\frac{1}{S''(a(m))}<0;
\]

\item if $m_*<\sup J$, then
\[
u(m)\longrightarrow \beta
\qquad (m\uparrow m_*).
\]
Hence the branch cannot end in the interior of $I_+$; it can stop only when it
reaches the boundary of the source/target slope-overlap block.

In particular, the odd-order lifted $3$-point branch has no interior
recurrence, no self-return, no interior accumulation, and no infinite-order
flatness. Its only remaining endpoint mechanism is boundary exit of the
relevant good-patch / monotone-slope block.
\end{enumerate}
\end{theorem}

\begin{proof}
For
\[
m\in J,
\]
set
\[
\Phi(m,u):=S(u)-m\,u-\tau_-(m).
\]
Then
\[
\Phi(m,u)=H_3(a(m),u).
\]

\smallskip

\noindent
\textbf{Step 1: positivity of the intercept gap.}
By the odd-order local classification theorem, for all sufficiently small
$m>0$ there exists a point $u(m)\in I_+$ such that
\[
\Phi(m,u(m))=0.
\]
Fix such a small $m$. Since $S'$ is strictly increasing on $I_+$, the function
\[
u\longmapsto \Phi(m,u)
\]
has strictly increasing derivative
\[
\partial_u\Phi(m,u)=S'(u)-m,
\]
hence a unique critical point, namely $u_+(m)$, and that critical point is its
unique minimum on $I_+$. Therefore
\[
\Phi(m,u_+(m))<0.
\]
But
\[
\Phi(m,u_+(m))
=
S(u_+(m))-m\,u_+(m)-\tau_-(m)
=
\tau_+(m)-\tau_-(m)
=
-D(m),
\]
so $D(m)>0$ for all sufficiently small $m>0$.

By Lemma~\ref{lem:slope-intercept-parametrization-lifted-three-point},
\[
D'(m)=u_+(m)-a(m)>0
\]
on all of $J$. Hence $D(m)>0$ for every $m\in J$.

\smallskip

\noindent
\textbf{Step 2: no interior common tangency.}
Suppose
\[
\Phi(m,u)=0
\]
for some $m\in J$ and $u\in I_+$. If also
\[
\partial_u\Phi(m,u)=S'(u)-m=0,
\]
then by uniqueness of the inverse point on $I_+$ one has $u=u_+(m)$, and thus
\[
0=\Phi(m,u_+(m))=-D(m),
\]
contrary to $D(m)>0$. Therefore every branch point satisfies
\[
\partial_u\Phi(m,u)\neq 0.
\]
Equivalently, there is no interior common-tangent point on the odd-order
branch.

\smallskip

\noindent
\textbf{Step 3: uniqueness and analytic continuation.}
For fixed $m\in J$, the derivative
\[
u\longmapsto \partial_u\Phi(m,u)=S'(u)-m
\]
is strictly increasing on $I_+$, and
\[
\partial_u\Phi(m,0)=S'(0)-m=-m<0.
\]
Hence $\Phi(m,\cdot)$ first decreases and then increases, so it has at most one
zero on $I_+$. Thus the local branch from
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero}
is unique on every connected continuation interval.

Let
\[
E:=\{m\in J:\exists\,u\in I_+\ \text{with}\ \Phi(m,u)=0\}.
\]
By Step 2, every zero is simple in the $u$-variable, so the implicit function
theorem shows that $E$ is open and that the zero depends real-analytically on
$m$. Let
\[
J_{\mathrm{br}}=(0,m_*)
\]
be the connected component of $E$ containing all sufficiently small positive
$m$. This gives the unique maximal analytic continuation
\[
u=u(m),
\qquad
m\in J_{\mathrm{br}}.
\]

Differentiating
\[
\Phi(m,u(m))=0
\]
gives
\[
\bigl(S'(u(m))-m\bigr)u'(m)-u(m)+a(m)=0,
\]
hence
\[
u'(m)=\frac{u(m)-a(m)}{S'(u(m))-m}.
\]
Also
\[
a'(m)=\frac{1}{S''(a(m))}<0
\]
because $S''<0$ on the source interval $I_-$. So the source coordinate is
strictly monotone and cannot return to a previous value.

\smallskip

\noindent
\textbf{Step 4: endpoint control.}
Assume that
\[
m_*<\sup J
\]
but that $u(m)$ does not approach $\beta$ as $m\uparrow m_*$. Then there exists
a compact subinterval
\[
K\Subset I_+
\]
and a sequence $m_n\uparrow m_*$ with
\[
u(m_n)\in K.
\]
After passing to a subsequence,
\[
u(m_n)\to u_*\in K.
\]
By continuity,
\[
\Phi(m_*,u_*)=0.
\]
Since $m_*<\sup J$, one has $m_*\in J$, so by Step 2,
\[
\partial_u\Phi(m_*,u_*)\neq 0.
\]
The implicit function theorem therefore extends the branch analytically past
$m_*$, contradicting maximality of $J_{\mathrm{br}}$.

Hence
\[
u(m)\to\beta
\qquad (m\uparrow m_*).
\]
This proves that the branch cannot terminate by an interior fold, interior
common tangency, or interior accumulation.

Finally, by
Corollary~\ref{cor:no-infinite-order-flatness-Kv-good-vpatch}, every zero of
$K_v$ has finite order. Since even-order zeros do not change the sign of $S''$,
they do not break the strict increase of $S'$ on $I_+$. Therefore the endpoint
$\beta$ can only be the ambient boundary of the good patch or the first
odd-order zero of $K_v$ to the right.
\end{proof}

\begin{remark}[Structural package for the global lifted $3$-point branch]
\label{rem:structural-package-global-lifted-three-point-branch}
The correct global parameter on the odd-order lifted $3$-point branch is the
source tangent slope
\[
m=S'(a).
\]
In that parameter, the branch is governed by the source/target tangent
intercepts
\[
\tau_-(m)=S(a(m))-m\,a(m),
\qquad
\tau_+(m)=S(u_+(m))-m\,u_+(m),
\]
and their gap
\[
D(m)=\tau_-(m)-\tau_+(m),
\qquad
D'(m)=u_+(m)-a(m)>0.
\]
Thus interior common tangency is exactly the equation
\[
D(m)=0,
\]
but this never occurs on the odd-order continuation branch because $D>0$ there.
So the global $3$-point problem is not a hidden recurrence problem inside the
patch: once born at an odd-order $K_v$-zero, the branch is a one-parameter
analytic graph with monotone source coordinate, and even-order $K_v$-zeros are
invisible to it except as isolated points where $S''$ vanishes without changing
the monotone-slope block.
\end{remark}
```

---

## 2) Update the lifted-order-7 status remark

Replace the entire remark

```latex
\begin{remark}[Work in progress: what remains in the lifted order-$7$ geometry]
\label{rem:wip-lifted-order7-zero-capture}
...
\end{remark}
```

with this:

```latex
\begin{remark}[Status of the lifted order-$7$ geometry]
\label{rem:wip-lifted-order7-zero-capture}
The lifted geometry is now substantially more stratified than a single
zero-capture problem.

First, shrinking exact lifted three-point and four-point circuits can accumulate
only at
\[
K_v=0
\qquad\text{and}\qquad
T_v=0,
\]
respectively, with uniform small-diameter exclusion away from those zero sets.

Second, repeated-node limits are now explicit:
three-point collapse limits become tangent-line contact determinants for the
planar lifted curve $\Lambda_v=(x,S)$, and four-point collapse limits become
tangent-plane contact determinants for the lifted space curve $Q_v=(Y,x,S)$.

Third, the three-point side is now globally controlled on good $v_5$-patches.
The curvature zero set $K_v=0$ has no infinite-order flat points; even-order
$K_v$-zeros are sterile; odd-order $K_v$-zeros carry exactly one local
opposite-side tangent-contact branch; and that branch continues uniquely on the
maximal right monotone-slope block, with no interior common-tangent event, no
source-side return, and no interior accumulation. Thus the three-point side is
no longer a live internal recurrence problem on such patches; only boundary exit
of the relevant source/target slope-overlap block can remain.

Fourth, the four-point side splits sharply into nonmixed and mixed regimes.
On the nonmixed side, finite-order odd $T_v$-zeros already support genuine
local exact branch sheets in the model geometry, so a blanket local sterility
theorem is false. On the mixed side, the dangerous low-order obstruction list is
finite and explicit:
\[
(m,n)=(3,4),\ (3,6),\ (4,6),
\]
equivalently
\[
(r,s)=(1,2),\ (1,4),\ (2,5),
\]
equivalently
\[
(r,\operatorname{ord}_0\mathcal Z)=(1,1),\ (1,3),\ (2,2),
\]
equivalently
\[
(r,\operatorname{ord}_0\mathcal R)=(1,0),\ (1,2),\ (2,1).
\]

Fifth, below the lifted variables one has the exact Wronskian-ratio
reformulation
\[
\mathcal Z=\frac{J_{u_5}}{J_\lambda},
\qquad
\mathcal R=\frac{c^2}{M}\frac{d}{dh}\!\left(\frac{J_{u_5}}{J_\lambda}\right),
\qquad
\lambda=\frac{\Delta_7}{v_5},
\]
while the projective curvature ratio $\Theta$ yields no new independent local
obstruction beyond $(\mathcal Z,\mathcal R)$.

Sixth, the centered symmetric-placement Taylor package gives a strong local
collision-side parity picture:
\[
u_5,\ v_5,\ u_{7,K_1},\ v_{7,K_1}\ \text{odd in }s,
\qquad
\Delta_7\ \text{even in }s,
\]
with explicit septic coefficients $D_2,D_4,D_6$. In the diagonal-centered
odd/odd normal form
\[
Q(x)\sim (x^n,\ x,\ x^m),
\qquad
m,n\ \text{odd},\quad n>m\ge 3,
\]
one gets a punctured neighborhood free of $K_v=0$ and $T_v=0$ points.
Thus the explicit low-order dangerous $4$-point patterns do not arise at the
symmetric diagonal base itself.

So the remaining missing ingredients are no longer generic local geometry for
the lifted $3$-point branch. They are:
\begin{itemize}
\item source-level control of the multi-pair interaction defects
\[
E_{\ge2}^{(3)},\qquad E_{\ge2}^{(5)},\qquad \overline E_{\ge2}^{(7)};
\]

\item exploitation of the now-established punctured-arc quintic-patch
dichotomy on the mixed side: if the $v_5$-patch opens, carry out the
finite-jet centered-to-patch parity transfer there strongly enough to exclude
\[
(r,\operatorname{ord}_0\mathcal Z)\in\{(1,1),(1,3),(2,2)\};
\]
if instead only the $u_5$-patch opens, develop the parallel $u_5$-patch
geometry as a genuine fallback local setting;

\item as a backup local algebraic route, exclusion of the remaining coupled
quintic--septic degeneration tower when the $v_5$-route fails;

\item and, on the still-live nonmixed side, a deeper RH-specific source- or
matrix-level identity imposing stronger parity / divisibility constraints on
\[
\mathcal R=\frac{T_v}{K_v^2}.
\]
\end{itemize}
\end{remark}
```

---

## 3) Update the “live attack routes” remark

In `Remark~\ref{rem:live-attack-routes}`, replace item 2

```latex
\item
\textbf{Three-point global continuation.}
The local defect-free three-point branch is already classified. The remaining
problem is to control global recurrence / continuation of the unique odd-order
branch and to exclude infinite-order flatness.
```

with

```latex
\item
\textbf{Three-point branch (closed on good $v_5$-patches).}
The lifted three-point side is no longer a live internal bottleneck:
infinite-order flatness is excluded, the unique odd-order branch continues
uniquely on the maximal right monotone-slope block, and there is no interior
common-tangent recurrence or source-side return. Any residual issue there is
only boundary exit of the relevant source/target slope-overlap block, not an
internal three-point propagation mechanism.
```

---

## 4) Update the stratified-local-picture remark

Replace the entire remark

```latex
\begin{remark}[Work in progress: stratified lifted local picture]
\label{rem:wip-stratified-lifted-local-picture}
...
\end{remark}
```

with this:

```latex
\begin{remark}[Stratified lifted local picture]
\label{rem:wip-stratified-lifted-local-picture}
The lifted local obstruction now splits into one closed regime and two genuinely
live regimes.

First, exact shrinking lifted $3$-point circuits concentrate into
\[
K_v=0.
\]
On good $v_5$-patches, this side is now globally controlled: there is no
infinite-order flatness, even-order $K_v$-zeros are sterile, odd-order
$K_v$-zeros seed exactly one local opposite-side branch, and that branch
continues uniquely on the maximal right monotone-slope block with no interior
common tangent, no source-side return, and no interior accumulation. So the
three-point side contributes only possible boundary exit, not an internal
recurrence mechanism.

Second, exact shrinking lifted $4$-point circuits concentrate into
\[
T_v=0.
\]
On the nonmixed side $K_v\neq 0$, finite-order odd $T_v$-zeros can already
support genuine local exact branch sheets, so the nonmixed $4$-point side is
not governed by a blanket local sterility theorem.

Third, on the mixed side $K_v=T_v=0$, the low-order obstruction list is now
finite and explicit:
\[
(m,n)=(3,4),\ (3,6),\ (4,6),
\]
equivalently
\[
(r,s)=(1,2),\ (1,4),\ (2,5),
\]
equivalently
\[
(r,\operatorname{ord}_0\mathcal Z)=(1,1),\ (1,3),\ (2,2).
\]
At the pair level, however, the centered quintic fixed-sector package
\[
A_5^{\mathfrak f}(s)=u_5(s)I+v_5(s)S
\]
is now known not to vanish identically on the centered diagonal branch.
So the theorem-level mixed target is no longer a coefficient-level statement
such as $V_1\neq 0$. The punctured-arc quintic-patch dichotomy is now
available from Proposition~\ref{prop:centered-quintic-patch-dichotomy}. What
remains is to use that dichotomy: on the $v_5$-side, perform the finite-jet
parity transfer to the actual good-patch coordinate $x=v_5/c$; on the
$u_5$-side, develop the parallel $u_5$-patch as the fallback local geometry.

Thus the remaining lifted local issues are now:
the continuation / non-recurrence of nonmixed odd-order $4$-point branches,
the \emph{effective exploitation} of the already-available punctured-arc
quintic-patch dichotomy on the mixed side, the completion of the finite-jet
centered-to-patch bridge on the actual $v_5$-patch together with the fallback
local analysis on the $u_5$-patch, and the deeper RH-specific identities needed
on the nonmixed $4$-point branch.
\end{remark}
```

---

## 5) Update the later summary paragraph

In the later summary remark where you currently have this paragraph:

```latex
Second, on the lifted three-point side, shrinking exact circuits now
concentrate into $K_v=0$, repeated-node limits become tangent-line contacts,
and finite-order $K_v$-zeros admit an explicit local branch classification:
even-order zeros are sterile, while odd-order zeros carry exactly one local
branch. The remaining issue there is therefore global recurrence / continuation,
not local first-contact ambiguity.
```

replace it with:

```latex
Second, on the lifted three-point side, shrinking exact circuits now
concentrate into $K_v=0$, repeated-node limits become tangent-line contacts,
and this side is globally controlled on good $v_5$-patches: $K_v$ has no
infinite-order zeros; even-order zeros are sterile; odd-order zeros carry
exactly one local branch; and that branch continues uniquely on the maximal
right monotone-slope block with no interior common-tangent event or source-side
return. So the three-point side is reduced to boundary exit of the relevant
slope-overlap block, not an internal recurrence mechanism.
```

---

## 6) Optional small cleanup

I would also make this title-only cleanup:

Replace

```latex
\begin{remark}[Work in progress: what remains in the lifted order-$7$ geometry]
```

by

```latex
\begin{remark}[Status of the lifted order-$7$ geometry]
```

and replace

```latex
\begin{remark}[Work in progress: stratified lifted local picture]
```

by

```latex
\begin{remark}[Stratified lifted local picture]
```

even if you keep the old labels, so the document no longer advertises those as still-open WIP remarks.

The main mathematical gain here is that the three-point side is no longer just “local classification + hope.” The draft now gets a real global package:
\[
\tau_-'(m)=-a(m),\qquad
\tau_+'(m)=-u_+(m),\qquad
D'(m)=u_+(m)-a(m)>0,
\]
plus
\[
u'(m)=\frac{u(m)-a(m)}{S'(u(m))-m},
\]
which is exactly the rigidity/nonrecurrence structure you wanted.
## User (2026-04-20 13:59:22)

ok here's the updated draft. any further findings or goodies to add? any more stale sections to update?

## Assistant (2026-04-20 13:59:32)

I’m checking the updated TeX directly for two things: whether the new three-point global package landed cleanly, and whether any downstream remarks still talk as if that part were open.

I found at least two later summary/roadmap spots that still speak as if the three-point global theorem is open. I’m checking those now so I can give you precise deletions/replacements rather than broad comments.

_Thought for 6m 42s_

A few worthwhile cleanups remain. I do **not** see another major missing three-point theorem inside the updated draft. The main things left are:

- one nice structural “goodie” to add;
- one clearly stale remark to update;
- a few phrases that overstate “patchwise closure” when the theorem you proved is really **blockwise** (up to slope-overlap-block exit).

Here are the exact edits I’d make.

---

### 1) Add one more structural remark: the target-block version of the intercept-gap monotonicity

Insert this **immediately after**
`Remark~\ref{rem:structural-package-global-lifted-three-point-branch}`.

```latex
\begin{remark}[Target-block form of the intercept-gap monotonicity]
\label{rem:target-block-intercept-gap-monotonicity}
The slope--intercept monotonicity from
Lemma~\ref{lem:slope-intercept-parametrization-lifted-three-point}
is not special to the first right-hand target block.

Let $I$ be any open interval to the right of the source interval $I_-$
on which $S'$ is monotone and hence invertible. For
\[
m\in S'(I_-)\cap S'(I),
\]
define
\[
u_I(m):=(S'|_I)^{-1}(m),
\qquad
\tau_I(m):=S(u_I(m))-m\,u_I(m),
\]
and
\[
D_I(m):=\tau_-(m)-\tau_I(m).
\]
Then exactly the same envelope calculation gives
\[
\tau_I'(m)=-u_I(m),
\qquad
D_I'(m)=u_I(m)-a(m)>0.
\]

Thus for any monotone-slope target block, interior common tangency against the
fixed source interval $I_-$ is again the scalar equation
\[
D_I(m)=0.
\]
So any future continuation across successive odd-order $K_v$-zeros must be
organized blockwise through these monotone intercept-gap functions rather than
through a hidden recurrence mechanism inside a block.
\end{remark}
```

This is a real useful “goodie”: it packages the monotonicity in a way that will still be useful later if you push continuation across multiple odd-order target blocks.

---

### 2) Soften the few places that still overstate “patchwise” closure

Your theorem proves the branch is rigid on the **maximal right monotone-slope block**. That is already very good, but it is a little stronger in the prose than in the theorem to say “closed on good \(v_5\)-patches” without qualification.

I would make these exact replacements.

#### (a) In `Remark~\ref{rem:wip-lifted-order7-zero-capture}`

Replace

```latex
Third, the three-point side is now globally controlled on good $v_5$-patches.
```

with

```latex
Third, the three-point side is now blockwise globally controlled on good
$v_5$-patches.
```

#### (b) In `Remark~\ref{rem:live-attack-routes}`

Replace

```latex
\textbf{Three-point branch (closed on good $v_5$-patches).}
```

with

```latex
\textbf{Three-point branch (blockwise closed on good $v_5$-patches).}
```

#### (c) In `Remark~\ref{rem:wip-stratified-lifted-local-picture}`

Replace

```latex
On good $v_5$-patches, this side is now globally controlled:
```

with

```latex
On good $v_5$-patches, this side is now blockwise globally controlled:
```

#### (d) In `Remark~\ref{rem:current-state-of-argument}`

Replace

```latex
and this side is globally controlled on good $v_5$-patches:
```

with

```latex
and this side is blockwise globally controlled on good $v_5$-patches:
```

That keeps the prose exactly aligned with what the theorem actually proves.

---

### 3) Update the stale “post-draft findings” remark

This is the clearest stale section I found.

Right now:

- it still says “five” conclusions;
- it does **not** include the new three-point global theorem;
- its final sentence still treats the “source-level two-point structure theorem” as frontier, even though that branch is already closed earlier in the same remark.

Replace everything from

```latex
Fifth, on the backup algebraic side, the valuation form of the septic transport
constraint shows that if
```

down to the end of that remark with this:

```latex
Fifth, on the lifted three-point side, the repeated-node tangent-contact
equation
\[
H_3(a,u)=S(u)-S(a)-S'(a)(u-a)
\]
is now globally rigid on each monotone-slope target block of a good $v_5$-patch.
The correct global parameter is the source tangent slope
\[
m=S'(a),
\]
with source/target tangent intercepts
\[
\tau_-(m)=S(a(m))-m\,a(m),
\qquad
\tau_+(m)=S(u_+(m))-m\,u_+(m),
\]
and intercept gap
\[
D(m)=\tau_-(m)-\tau_+(m),
\qquad
D'(m)=u_+(m)-a(m)>0.
\]
Consequently $K_v$ has no infinite-order flat points on a good $v_5$-patch,
interior common tangency is excluded, and the unique odd-order lifted
$3$-point branch continues uniquely on the maximal right monotone-slope block
with no source-side return.

Sixth, on the backup algebraic side, the valuation form of the septic transport
constraint shows that if
\[
\operatorname{ord}_s u_5=2m+1,\qquad
\operatorname{ord}_s v_5=2r+1,\qquad
r\ge m,
\]
and
\[
\lambda=\frac{\Delta_7}{v_5}
\]
stays analytic odd, then
\[
\operatorname{ord}_s v_{7,K_1}\ge 2(r-m)+1.
\]
So failure of the $v_5$-route is forced into a coupled quintic--septic
degeneration tower rather than an isolated coefficient cancellation.

So the present frontier is no longer a generic local geometry problem. It is
the combination of the source-level multi-pair / finite-core interaction
problem above the now-closed two-point branch, the effective use of the
already-established quintic-patch dichotomy together with the finite-jet parity
bridge on the mixed four-point side, and a deeper RH-specific identity on the
nonmixed four-point branch.
```

Also replace the opening sentence of that remark

```latex
Since this draft state, five additional conclusions have emerged.
```

with

```latex
Since this draft state, six additional conclusions have emerged.
```

---

## Bottom line

I do **not** see another substantive three-point theorem still missing in this updated draft beyond the block-to-block continuation issue you deliberately left out. The main remaining edits are:

- add the general target-block intercept-gap remark;
- fix the stale “five conclusions / two-point still frontier” remark;
- soften a few “globally controlled on good patches” phrases to “blockwise globally controlled.”

Those are the main remaining worthwhile changes.
## User (2026-04-20 15:21:57)

there have been some important (beneficial) structural updates/findings on the base structure of the proof. here is a note of what to check--there may even be more. please check if this new ammo is relevant to your current attack.

## Assistant (2026-04-20 15:21:59)

I’m checking the note against the three-point/global branch specifically, not the whole paper. The main question is whether the new base-structure results strengthen the three-point continuation theorem itself, or mostly change how it plugs into the larger RH endgame.

_Thought for 45s_

Yes. Some of this new ammo is genuinely relevant to the current three-point attack, but not all of it in the same way.

The short version is:

- the **lifted \(v\)-patch curvature / osculating package** is directly relevant and strengthens the conceptual presentation of the three-point theorem itself;
- the **finite-core / minimal-core reduction** is strategically relevant because it raises the value of the three-point theorem inside the global RH architecture;
- the **nonmixed four-point \(\mathcal R\)-planarity package** is only indirectly relevant to the three-point attack;
- the **\(N\)-point Mellin / sign-definite odd-tail package** is mostly downstream infrastructure, not something I would insert into the proof of the three-point global theorem itself. 

Here is the more exact read.

The most relevant new structural update for the current attack is the note’s emphasis that the three-point branch should now be viewed through the **derivative geometry** of the lifted curve: the key block is the lifted \(v\)-patch geometry, and in particular the fact that shrinking exact lifted three-point circuits are tied explicitly to the **osculating determinant** and hence to \(K_v=0\). That makes the three-point branch “much more derivative-geometric and less ad hoc,” which is exactly right for the theorem we just proved: local birth at odd-order \(K_v\)-zeros, then slope–intercept continuation on monotone-slope blocks. So this is not new ammunition for the proof steps themselves so much as new ammunition for the **structural interpretation** of those proof steps. 

The finite-core reduction is also relevant, but at a different level. The note says the current reduction of defect-free bad cores is now to lifted affine dependence with an effective ceiling at core size \(\le 4\). That matters because it makes the three-point theorem more central in the overall architecture: once three-point propagation is blockwise rigid, the remaining live bad-core mechanisms are pushed upward into the two-pair and four-point layers rather than being allowed to linger as a vague “global three-point recurrence” problem. So I would use this not inside the proof of the three-point theorem, but in the surrounding roadmap/status remarks to explain why the theorem matters more now than it did a few drafts ago. 

By contrast, the nonmixed four-point update is mostly not part of the current three-point attack. The note’s point is that interval-persistent nonmixed four-point degeneracy is now controlled by the scalar derivative invariant
\[
\mathcal R=\frac{d}{dx}\!\left(\frac{Y''}{S''}\right),
\]
which kills genuinely three-dimensional interval-persistent nonmixed branches, though not isolated local sheets. That is important globally, but I would treat it as a neighboring branch result, not as input to the three-point continuation theorem. It belongs in cross-references and status summaries, not in the three-point proof itself. 

The \(N\)-point cancellation package is even further away from the current attack. The note emphasizes that the \(N\)-point layer now has a discrete Mellin-side projector, exact low odd-jet annihilation, an explicit gamma-ratio kernel, and a sign-definite surviving odd tail. That is powerful infrastructure for the corrected odd channel and probably very important in the eventual endgame, but it is not something I would force into the three-point continuation section unless you are explicitly adding a high-level “global infrastructure” remark. It strengthens the paper’s stabilized backbone, not the local-to-global geometry of the odd \(K_v\)-branch. 

So my honest answer is:

**Directly relevant to the current attack**
- the lifted curvature / osculating viewpoint;
- the fact that the three-point branch is now the “most mature” branch.

**Strategically relevant, but not proof-local**
- finite-core reduction to lifted affine dependence with ceiling \(\le 4\).

**Mostly separate**
- nonmixed four-point \(\mathcal R\)-planarity;
- the Mellin / projector / odd-tail sign package;
- the calibration-small-\(u\) and high-height-only status issues. turn4file1

What I would change in the draft because of this is fairly specific.

First, I would strengthen the surrounding prose near the three-point theorem so it explicitly says that the global three-point branch is now understood as the **global propagation of a local osculating-contact defect** on the lifted curve \(\Lambda_v=(x,S)\), rather than as an abstract repeated-node coincidence problem. That is a genuine conceptual improvement from the new note. 

Second, in the status/roadmap remarks, I would now describe the three-point side as one of the stabilized branches of the proof architecture, with the remaining burden shifted to the source-level two-point bottleneck and the mixed/nonmixed four-point mechanisms. The note is explicit that the 3-point chat should use the lifted curvature/osculating package and the global continuation theorem, and that this branch is now the most mature. That is worth reflecting in the paper’s “what remains” remarks. 

Third, I would not insert the \(N\)-point sign package into the three-point theorem section itself. At most I would add one short cross-reference in a later global-summary remark saying that the three-point branch closure now sits alongside an independently strengthened corrected odd-channel infrastructure. 

So yes: this new ammo is relevant, but mainly by sharpening the **interpretation and positioning** of the current three-point attack, not by changing the core proof we already extracted. The strongest concrete takeaway is that the three-point theorem should now be presented as part of a coherent **derivative-geometry spine** of the proof, not as an isolated branch argument.

If you want, I can now give exact LaTeX insertions to fold this new structural perspective into the updated draft.
## User (2026-04-20 15:24:00)

yes please give me the exact latex insertions

## Assistant (2026-04-20 15:24:02)

I’m locating the exact insertion points in the new draft now so the edits land where the current structure already talks about three-point status and derivative geometry.

_Thought for 2m 18s_

Yes. I’d make five targeted edits.

They do two things: they fold the new derivative-geometric interpretation into the three-point section itself, and they update the downstream status remarks so the draft reflects that the three-point branch is now both structurally cleaner and more important inside the finite-core program.

---

### 1) Add the finite-core meaning of the lifted \(3/4\)-point stratification

Insert this **immediately after** the proof of
`Corollary~\ref{cor:explicit-four-point-determinant-form-vpatch}`
and **before**
`Remark~\ref{rem:parallel-u5-patch-version}`.

```latex
\begin{remark}[Finite-core meaning of the lifted $v_5$-patch geometry]
\label{rem:finite-core-meaning-lifted-vpatch-geometry}
The defect-free finite-core reduction now places the lifted $v_5$-patch
geometry into a sharp global context.

Indeed, by
Theorem~\ref{thm:defect-free-quintic-circuit-reduction},
Corollary~\ref{cor:defect-free-minimal-quintic-circuits}, and
Proposition~\ref{prop:defect-free-lifted-affine-dependence-vpatch},
defect-free bad cores on a good $v_5$-patch reduce to affine dependence of the
lifted points
\[
Q_v(h)=\bigl(y(h),x(h),\sigma_v(h)\bigr),
\]
with effective ceiling
\[
k\le 4.
\]
Thus the three low core sizes have the following exact lifted meanings:
\[
k=2 \Longleftrightarrow Q_v(h_1)=Q_v(h_2),
\]
\[
k=3 \Longleftrightarrow Q_v(h_1),Q_v(h_2),Q_v(h_3)
\ \text{are collinear},
\]
\[
k=4 \Longleftrightarrow Q_v(h_1),\dots,Q_v(h_4)
\ \text{are coplanar}.
\]

So the lifted $3$-point and $4$-point analyses are not auxiliary side
computations: they are exactly the $k=3$ and $k=4$ geometric layers in the
finite-core program. In particular, once the lifted $3$-point branch is
globally rigid on good $v_5$-patches, the remaining finite-core burden shifts
upward to the two-point source-level merger problem and to the mixed/nonmixed
lifted $4$-point mechanisms.
\end{remark}
```

---

### 2) Add the derivative-geometric interpretation of the global \(3\)-point theorem

Insert this **immediately after**
`Remark~\ref{rem:target-block-intercept-gap-monotonicity}`
and **before**
`Remark~\ref{rem:nonmixed-four-point-zeros-can-carry-preexisting-branches}`.

```latex
\begin{remark}[Derivative-geometric meaning of the lifted $3$-point branch]
\label{rem:derivative-geometry-meaning-global-three-point-branch}
The lifted $3$-point branch is now best viewed as a derivative-geometric
propagation theorem for the planar lifted curve
\[
\Lambda_v=(x,S).
\]

By Lemma~\ref{lem:osculating-determinant-expansion} and
Proposition~\ref{prop:shrinking-exact-lifted-three-point-circuits-force-Kv-zero},
shrinking exact lifted $3$-point circuits are detected by the osculating
determinant and therefore concentrate into the lifted curvature-zero set
\[
K_v=(x')^3S''(x)=0.
\]
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero}
then identifies the local repeated-node branch structure at those curvature
zeros, and
Theorem~\ref{thm:global-continuation-nonrecurrence-odd-three-point-branch}
shows that the odd-order branch propagates globally on each monotone-slope
target block by the slope--intercept envelope identities
\[
\tau_-'(m)=-a(m),
\qquad
\tau_+'(m)=-u_+(m),
\qquad
D'(m)=u_+(m)-a(m)>0.
\]

So the lifted $3$-point theory is no longer an ad hoc repeated-node analysis.
It is the global propagation of an osculating-contact defect for the curve
$\Lambda_v$, organized by the derivative geometry of its tangent lines and
curvature.
\end{remark}
```

---

### 3) Strengthen the “live routes” three-point item

In `Remark~\ref{rem:live-attack-routes}`, replace item 2

```latex
\item
\textbf{Three-point branch (blockwise closed on good $v_5$-patches).}
The lifted three-point side is no longer a live internal bottleneck:
infinite-order flatness is excluded, the unique odd-order branch continues
uniquely on the maximal right monotone-slope block, and there is no interior
common-tangent recurrence or source-side return. Any residual issue there is
only boundary exit of the relevant source/target slope-overlap block, not an
internal three-point propagation mechanism.
```

with

```latex
\item
\textbf{Three-point branch (derivative-geometric layer now stabilized).}
The lifted three-point side is now the most mature local branch. Shrinking
exact lifted $3$-point circuits are tied to the osculating determinant and
hence to
\[
K_v=0,
\]
the local branch structure at finite-order $K_v$-zeros is completely
classified by parity, and the odd-order branch is blockwise globally rigid on
good $v_5$-patches: infinite-order flatness is excluded, the branch continues
uniquely on the maximal right monotone-slope block, and there is no interior
common-tangent recurrence or source-side return. Inside the finite-core
program this stabilizes the lifted $k=3$ collinearity layer; any residual
issue there is only boundary exit of the relevant source/target slope-overlap
block, not an internal three-point propagation mechanism.
```

---

### 4) Update the “current geometric bottleneck” remark

In `Remark~\ref{rem:current-geometric-bottleneck}`, replace this paragraph

```latex
At the lifted order-$7$ level, the new local determinants
\[
K_v
\qquad\text{and}\qquad
T_v
\]
govern shrinking exact lifted $3$- and $4$-point circuits on
$v_5\neq 0$ patches: exact shrinking $3$-point circuits concentrate into
$\{K_v=0\}$, and exact shrinking $4$-point circuits concentrate into
$\{T_v=0\}$, with uniform small-diameter exclusion away from those zero
sets. Near finite-order isolated $K_v$-zeros, the $3$-point branch is
completely classified by parity.
```

with

```latex
At the lifted order-$7$ level, the canonical derivative-geometric determinants
\[
K_v
\qquad\text{and}\qquad
T_v
\]
govern shrinking exact lifted $3$- and $4$-point circuits on
$v_5\neq 0$ patches. On the $3$-point side,
Lemma~\ref{lem:osculating-determinant-expansion} and
Proposition~\ref{prop:shrinking-exact-lifted-three-point-circuits-force-Kv-zero}
show that shrinking exact lifted $3$-point circuits are detected by the
osculating determinant of the planar lifted curve
\[
\Lambda_v=(x,S)
\]
and therefore concentrate into
\[
\{K_v=0\},
\]
with uniform small-diameter exclusion away from that zero set. Near
finite-order isolated $K_v$-zeros, the local branch structure is completely
classified by parity, and on good $v_5$-patches the odd-order branch is now
blockwise globally rigid by
Theorem~\ref{thm:global-continuation-nonrecurrence-odd-three-point-branch}.
So the lifted $3$-point side is no longer a vague recurrence problem: it is
the stabilized derivative-geometric $k=3$ layer in the finite-core program.

On the $4$-point side, exact shrinking lifted $4$-point circuits concentrate
into
\[
\{T_v=0\},
\]
again with uniform small-diameter exclusion away from that zero set.
```

---

### 5) Update the three-point paragraph in the “current state” remark

In `Remark~\ref{rem:current-state-of-argument}`, replace the paragraph beginning

```latex
Second, on the lifted three-point side, shrinking exact circuits now
concentrate into $K_v=0$,
```

and ending

```latex
not an internal recurrence mechanism.
```

with this:

```latex
Second, on the lifted three-point side, shrinking exact circuits now
concentrate into $K_v=0$, and this concentration is explicitly
derivative-geometric: by the osculating-determinant expansion, repeated-node
limits become tangent-line contacts for the planar lifted curve
\[
\Lambda_v=(x,S).
\]
On good $v_5$-patches this side is now blockwise globally controlled:
$K_v$ has no infinite-order zeros; even-order zeros are sterile; odd-order
zeros carry exactly one local branch; and that branch continues uniquely on
the maximal right monotone-slope block with no interior common-tangent event
or source-side return. So the three-point side is reduced to boundary exit of
the relevant slope-overlap block, not an internal recurrence mechanism.
Inside the finite-core reduction, this is exactly the stabilization of the
lifted $k=3$ collinearity layer.
```

---

### 6) Tighten the fifth “post-draft findings” item

In `Remark~\ref{rem:post-draft-findings-established-provisional-live}`, replace the current fifth item

```latex
Fifth, on the lifted three-point side, the repeated-node tangent-contact
equation
\[
H_3(a,u)=S(u)-S(a)-S'(a)(u-a)
\]
is now globally rigid on each monotone-slope target block of a good $v_5$-patch.
The correct global parameter is the source tangent slope
\[
m=S'(a),
\]
with source/target tangent intercepts
\[
\tau_-(m)=S(a(m))-m\,a(m),
\qquad
\tau_+(m)=S(u_+(m))-m\,u_+(m),
\]
and intercept gap
\[
D(m)=\tau_-(m)-\tau_+(m),
\qquad
D'(m)=u_+(m)-a(m)>0.
\]
Consequently $K_v$ has no infinite-order flat points on a good $v_5$-patch,
interior common tangency is excluded, and the unique odd-order lifted
$3$-point branch continues uniquely on the maximal right monotone-slope block
with no source-side return.
```

with

```latex
Fifth, on the lifted three-point side, the repeated-node tangent-contact
equation
\[
H_3(a,u)=S(u)-S(a)-S'(a)(u-a)
\]
is now understood as a derivative-geometric propagation law for the planar
lifted curve
\[
\Lambda_v=(x,S).
\]
Shrinking exact lifted $3$-point circuits are tied to the osculating
determinant and hence to
\[
K_v=(x')^3S''(x)=0,
\]
so the odd-order branch is born at a lifted curvature zero rather than at an
ad hoc repeated-node coincidence. Globally, on each monotone-slope target
block of a good $v_5$-patch, the correct parameter is the source tangent slope
\[
m=S'(a),
\]
with source/target tangent intercepts
\[
\tau_-(m)=S(a(m))-m\,a(m),
\qquad
\tau_+(m)=S(u_+(m))-m\,u_+(m),
\]
and intercept gap
\[
D(m)=\tau_-(m)-\tau_+(m),
\qquad
D'(m)=u_+(m)-a(m)>0.
\]
Consequently $K_v$ has no infinite-order flat points on a good $v_5$-patch,
interior common tangency is excluded, and the unique odd-order lifted
$3$-point branch continues uniquely on the maximal right monotone-slope block
with no source-side return. In the finite-core picture, this stabilizes the
lifted $k=3$ collinearity layer.
```

---

These are the main insertions I’d make from the new note. The biggest gain is that the draft will stop presenting the three-point theorem as merely “one more branch result” and instead present it as part of a coherent derivative-geometric spine, with a precise role inside the finite-core reduction.
## User (2026-04-20 15:39:05)

here's the latest draft. since you've wrapped up your work, the non-mixed 4-point branch is going to delegate a task to you. here's you're task attached

## Assistant (2026-04-20 15:39:06)

I’m isolating the exact nonmixed ingredients in the updated draft now: the B-spline determinant formula, the affine-planarity theorem, and where the three-point global theorem can actually bite.

_Thought for 9m 34s_

I can give you the sharp reduced theorem, and it is genuinely the right 4-point analogue of the 3-point slope–intercept monotonicity. I do **not** see a proof of first-odd-zero exclusion from the current ingredients alone. The exact remaining gap is narrower: it is an actual-source theorem preventing the first loss of monotonicity of a quadratic-envelope scalar attached to a fixed source point. That is exactly the route your note asked for. 

Here is the theorem.

---

## Reduced theorem: the nonmixed 4-point quadratic-envelope monotonicity

Let \(J\) be a connected open interval in a good \(v_5\)-patch such that
\[
K_v\neq 0 \quad\text{on }J.
\]
Write
\[
Q_v(h)=(Y(h),x(h),S(h)),
\qquad
\mathcal Z=\frac{Y''}{S''},
\qquad
\mathcal R=\mathcal Z'=\frac{T_v}{K_v^2},
\]
as in the draft’s nonmixed \(4\)-point package. For a fixed source point \(a\in J\), define for \(x\in J\setminus\{a\}\)
\[
B_a(x):=H_3(a,x):=S(x)-S(a)-S'(a)(x-a),
\]
and
\[
A_a(x):=Y(x)-Y(a)-Y'(a)(x-a),
\]
and set
\[
\Gamma_a(x):=\frac{A_a(x)}{B_a(x)}.
\]

Then:

### Theorem
On every nonmixed interval \(J\),

1. \(B_a(x)\neq 0\) for \(x\neq a\) in \(J\);

2. the repeated-node lifted \(4\)-point determinant factors exactly as
   \[
   H_4(a,u,v)
   =
   -\,B_a(u)\,B_a(v)\,\bigl(\Gamma_a(u)-\Gamma_a(v)\bigr);
   \]

3. \(\Gamma_a\) admits the integral representation
   \[
   \Gamma_a(x)
   =
   \frac{\displaystyle \int_a^x (x-t)\,\mathcal Z(t)\,S''(t)\,dt}
        {\displaystyle \int_a^x (x-t)\,S''(t)\,dt};
   \]

4. its derivative has the exact positive-kernel form
   \[
   \Gamma_a'(x)
   =
   \frac{1}{B_a(x)^2}
   \int_a^x \Omega_{a,x}(r)\,\mathcal R(r)\,dr,
   \]
   where
   \[
   \Omega_{a,x}(r)
   :=
   \int_a^r\!\!\int_r^x (t-s)\,S''(s)\,S''(t)\,dt\,ds,
   \]
   and \(\Omega_{a,x}(r)>0\) for \(a<r<x\) whenever \(S''\) has fixed sign on \(J\);

5. in particular, if \(\mathcal R\) has fixed nonzero sign on a subinterval \(I\subset J\), then for every \(a\in I\) the function \(x\mapsto \Gamma_a(x)\) is strictly monotone on \(x\in(a,\sup I)\). Hence
   \[
   H_4(a,u,v)=0,\qquad a<u<v\in I
   \]
   is impossible.

So \(\Gamma_a\) is the exact nonmixed \(4\)-point analogue of the 3-point tangent-envelope scalar: exact repeated-source nonmixed \(4\)-point coplanarity is equivalent to equality of two values of \(\Gamma_a\), and one-sign control of \(\mathcal R\) forces strict monotonicity of \(\Gamma_a\). This is the ordered-quadruple monotonicity theorem the task asked for. 

---

## Proof

I will use only the draft’s nonmixed identities and the repeated-node determinant setup.

### 1. The denominator is the 3-point tangent-contact remainder

By definition,
\[
B_a(x)=S(x)-S(a)-S'(a)(x-a)=H_3(a,x).
\]
On a nonmixed interval \(K_v\neq 0\), Proposition `prop:exact-x-coordinate-identities-lifted-four-point` gives
\[
K_v=(x')^3S''.
\]
Since \(x'\neq 0\) on a good \(v_5\)-patch, \(S''\) has fixed nonzero sign on \(J\). Therefore \(S\) is strictly convex or strictly concave in the \(x\)-coordinate on \(J\), so
\[
B_a(x)\neq 0\qquad (x\neq a).
\]
This is the same tangent-contact denominator that drives the 3-point branch.

### 2. Exact factorization of the repeated-node \(4\)-point determinant

The draft’s repeated-node determinant is
\[
H_4(a,u,v)=
\det\!\begin{pmatrix}
1&Y(a)&a&S(a)\\
0&Y'(a)&1&S'(a)\\
1&Y(u)&u&S(u)\\
1&Y(v)&v&S(v)
\end{pmatrix}.
\]
Subtract from the \(u\)-row the combination
\[
(1,Y(a),a,S(a))+(u-a)(0,Y'(a),1,S'(a)),
\]
and similarly for the \(v\)-row. Then the determinant becomes
\[
H_4(a,u,v)
=
\det\!\begin{pmatrix}
1&Y(a)&a&S(a)\\
0&Y'(a)&1&S'(a)\\
0&A_a(u)&0&B_a(u)\\
0&A_a(v)&0&B_a(v)
\end{pmatrix}
=
A_a(u)B_a(v)-A_a(v)B_a(u).
\]
Hence
\[
H_4(a,u,v)
=
-\,B_a(u)B_a(v)\left(\frac{A_a(u)}{B_a(u)}-\frac{A_a(v)}{B_a(v)}\right),
\]
that is,
\[
\boxed{
H_4(a,u,v)
=
-\,B_a(u)\,B_a(v)\,\bigl(\Gamma_a(u)-\Gamma_a(v)\bigr).
}
\]

So exact repeated-source \(4\)-point coplanarity is exactly the scalar equality
\[
\Gamma_a(u)=\Gamma_a(v).
\]

### 3. Integral representation of \(\Gamma_a\)

Since
\[
Y''=\mathcal Z\,S'',
\]
Taylor’s integral remainder gives
\[
A_a(x)=\int_a^x (x-t)\,Y''(t)\,dt
      =\int_a^x (x-t)\,\mathcal Z(t)\,S''(t)\,dt,
\]
and
\[
B_a(x)=\int_a^x (x-t)\,S''(t)\,dt.
\]
Therefore
\[
\boxed{
\Gamma_a(x)
=
\frac{\int_a^x (x-t)\,\mathcal Z(t)\,S''(t)\,dt}
     {\int_a^x (x-t)\,S''(t)\,dt}.
}
\]
So \(\Gamma_a(x)\) is a weighted average of \(\mathcal Z\) over \([a,x]\), with the same second-order remainder kernel that comes from the 3-point tangent-contact denominator.

### 4. Derivative of \(\Gamma_a\)

Set
\[
N_a(x):=\int_a^x (x-t)\,\mathcal Z(t)\,S''(t)\,dt,
\qquad
D_a(x):=\int_a^x (x-t)\,S''(t)\,dt.
\]
Then \(\Gamma_a=N_a/D_a\), and
\[
N_a'(x)=\int_a^x \mathcal Z(t)\,S''(t)\,dt,
\qquad
D_a'(x)=\int_a^x S''(t)\,dt.
\]
Hence
\[
\Gamma_a'(x)=\frac{N_a'D_a-N_aD_a'}{D_a^2}.
\]

Now symmetrize the numerator:
\[
N_a'D_a-N_aD_a'
=
\frac12
\int_a^x\!\!\int_a^x
(\mathcal Z(t)-\mathcal Z(s))(t-s)\,S''(t)\,S''(s)\,ds\,dt.
\]
Equivalently, since
\[
\mathcal Z(t)-\mathcal Z(s)=\int_s^t \mathcal R(r)\,dr,
\]
one gets
\[
N_a'D_a-N_aD_a'
=
\int_a^x \Omega_{a,x}(r)\,\mathcal R(r)\,dr,
\]
with
\[
\Omega_{a,x}(r)
:=
\int_a^r\!\!\int_r^x (t-s)\,S''(s)\,S''(t)\,dt\,ds.
\]
Because \(S''\) has fixed nonzero sign on \(J\), the product \(S''(s)S''(t)\) has fixed positive sign after factoring out the global sign, and
\[
t-s>0\qquad (a\le s<r<t\le x),
\]
so
\[
\Omega_{a,x}(r)>0.
\]
Thus
\[
\boxed{
\Gamma_a'(x)
=
\frac{1}{B_a(x)^2}
\int_a^x \Omega_{a,x}(r)\,\mathcal R(r)\,dr,
\qquad
\Omega_{a,x}(r)>0.
}
\]

This is the exact positive-kernel monotonicity formula.

### 5. Consequence on one-sign \(\mathcal R\)-blocks

If \(\mathcal R\) has fixed nonzero sign on \(I\subset J\), then the kernel formula shows \(\Gamma_a'(x)\) has that same sign for every \(a<x\) in \(I\). Hence \(\Gamma_a\) is strictly monotone on \((a,\sup I)\). By the factorization of \(H_4\), one cannot have
\[
H_4(a,u,v)=0,\qquad a<u<v\in I.
\]
That proves the theorem.

---

## What this does and does not finish

This theorem is strong, but it does **not** yet exclude the first odd zero of \(\mathcal R\).

What it proves is:

- before the first odd zero, on the whole one-sign nonmixed block, there is a strict quadratic-envelope monotonicity;
- repeated-source exact nonmixed \(4\)-point branches cannot recur or self-return inside that block;
- the only place such a branch can first appear is exactly where the positive-kernel average of \(\mathcal R\) can begin to cancel, namely after the first sign change of \(\mathcal R\).

So the remaining nonmixed gap is now very sharp.

---

## Sharp bottleneck theorem still needed

Let \(J=(x_0,b)\) be the opened nonmixed arc from the centered side to the first odd zero \(b\) of \(\mathcal R\). The centered parity package gives a punctured neighborhood near the base with no nonmixed \(T_v=0\) points, so \(b\) is genuinely the first candidate birth point. 

To exclude \(b\), it is enough to prove the following.

**Bottleneck theorem.**  
For every source \(a<b\) on the opened nonmixed arc, the quadratic-envelope scalar
\[
\Gamma_a(x)
=
\frac{Y(x)-Y(a)-Y'(a)(x-a)}
     {S(x)-S(a)-S'(a)(x-a)}
\]
cannot lose monotonicity as \(x\) passes the first odd zero \(b\), unless \(\mathcal R\equiv 0\) on a nontrivial interval and hence the lifted curve is affine-planar by Proposition `prop:interval-persistent-nonmixed-four-point-forces-affine-planarity`.

Equivalently, one must show that the positive-kernel averages
\[
\int_a^x \Omega_{a,x}(r)\,\mathcal R(r)\,dr
\]
cannot vanish for \(a<x\) on the actual-source opened nonmixed arc before affine-planarity sets in.

That is the sharp reduced theorem.

It is sharp because:

- local odd-order nonmixed birth at \(b\) is exactly the first place where \(\Gamma_a'\) can in principle change sign;
- everything before \(b\) is already rigid by the theorem above;
- if \(\mathcal R\equiv 0\) on an interval, the draft already collapses the branch to affine planarity.

So the nonmixed branch is now reduced to one actual-source statement: **rule out the first zero of the quadratic-envelope derivative kernel average.**

---

## Which draft ingredients this used

Directly used:

- `prop:exact-x-coordinate-identities-lifted-four-point`,
- `prop:canonical-Z-R-invariants-lifted-four-point`,
- `prop:repeated-node-limits-of-exact-lifted-determinants`,
- the 3-point tangent-contact scalar \(H_3(a,x)\) and its nonvanishing on a nonmixed block,
- `prop:interval-persistent-nonmixed-four-point-forces-affine-planarity` for the final bottleneck formulation.

Used only for locating the global first-zero problem:

- `prop:shrinking-exact-lifted-four-point-circuits-force-Tv-zero`,
- `rem:centered-symmetric-placement-taylor-package`,
- and the already established 3-point global rigidity package as the model for this new \(\Gamma_a\)-monotonicity mechanism. 

This is the cleanest reduction I can honestly justify from the current draft.
## User (2026-04-20 16:05:59)

another delegation: Work only on this narrow task from the attached draft.

We are on a connected opened nonmixed (v_5)-arc, so (K_v\neq 0). For a fixed source point (a), define
[
A_a(x)=Y(x)-Y(a)-Y'(a)(x-a),\qquad
B_a(x)=S(x)-S(a)-S'(a)(x-a),
]
and
[
\Gamma_a(x)=\frac{A_a(x)}{B_a(x)}.
]
The draft now gives
[
H_4(a,u,v)=-B_a(u)B_a(v)\bigl(\Gamma_a(u)-\Gamma_a(v)\bigr),
]
and
[
\Gamma_a'(x)=\frac{1}{B_a(x)^2}\int_a^x \Omega_{a,x}(r),\mathcal R(r),dr,
\qquad \Omega_{a,x}(r)>0,
]
where
[
\mathcal R=\frac{d}{dx}!\left(\frac{Y''}{S''}\right)=\frac{T_v}{K_v^2}.
]

Please do NOT work on mixed 4-point, 2-point, or general local nonmixed classification. That part is already reduced.

Task:
Assume there is a first loss of monotonicity of (\Gamma_a), i.e. a first pair ((a_*,x_*)) on the opened nonmixed arc with
[
\Gamma_{a_*}'(x_*)=0.
]
Derive the sharpest necessary conditions you can from this first-zero hypothesis by differentiating with respect to (x) and (a), and try to prove that they force either:

1. affine-planar collapse ((\mathcal R\equiv 0) on an interval), or
2. a lower-core / 3-point tangency mechanism already ruled out by the global 3-point theorem.

I want a theorem or reduced bottleneck, not a broad summary.

## Assistant (2026-04-20 16:06:02)

I’m focusing only on the first-loss-of-monotonicity system now: the kernel formula for \(\Gamma_a'\), then the consequences of imposing the earliest zero in both the \(x\)- and \(a\)-directions. The goal is to squeeze out a boundary-value system that either collapses to planarity or reduces to a 3-point tangency-type obstruction.

_Thought for 9m 33s_

I do not see a proof of full exclusion from the current ingredients alone. But the first-loss hypothesis does force a very sharp lower-core reduction, and it comes directly from differentiating in \(x\) and \(a\). It reduces the remaining nonmixed gap to a repeated-node \(3\)-point tangency mechanism on an affinely sheared planar curve. That is the sharpest bottleneck I can justify honestly from the present package. The task’s standing assumptions are exactly the nonmixed setup \(K_v\neq 0\), the scalar \(\mathcal Z=Y''/S''\), \(\mathcal R=\mathcal Z'\), the factorization of \(H_4(a,u,v)\) through \(\Gamma_a\), the positive-kernel formula for \(\Gamma_a'\), and the existing affine-planarity theorem when \(\mathcal R\equiv 0\) on an interval. 

Set
\[
M(a,x):=B_a(x)^2\,\Gamma_a'(x).
\]
Then by the quotient formula,
\[
M(a,x)=A_a'(x)B_a(x)-A_a(x)B_a'(x).
\]
Assume
\[
x_*:=\inf\{x:\exists\,a<x\text{ with }M(a,x)=0\},
\]
and choose \((a_*,x_*)\) in this first-zero set. On the opened nonmixed arc, \(S''\) has fixed sign because \(K_v\neq 0\), so \(B_a(x)\neq 0\) for \(a<x\). Thus \(M=0\) is exactly the first loss of monotonicity of \(\Gamma_a\). turn11file6

Here is the theorem.

**Theorem (first-loss rigidification for the nonmixed quadratic-envelope scalar).**  
On a connected opened nonmixed \(v_5\)-arc, let \((a_*,x_*)\) be a first-loss pair in the sense above. Then:

\[
M(a_*,x_*)=0,
\]
and the following differentiated identities hold:
\[
\partial_x M(a,x)=S''(x)\,B_a(x)\,\bigl(\mathcal Z(x)-\Gamma_a(x)\bigr),
\]
\[
\partial_a M(a,x)=S''(a)\,C_a(x)\,\bigl(\mathcal Z(a)-\Gamma_a(x)\bigr),
\]
where
\[
C_a(x):=S(a)-S(x)+S'(x)(x-a)
      =\int_a^x (t-a)S''(t)\,dt.
\]
In particular, at a first-loss pair one has
\[
\partial_a M(a_*,x_*)=0,
\qquad
\partial_x M(a_*,x_*)\le 0,
\]
hence
\[
\Gamma_{a_*}(x_*)=\mathcal Z(a_*),
\qquad
\mathcal Z(x_*)\le \mathcal Z(a_*).
\]

Define the affine shear
\[
\widetilde Y_\gamma:=Y-\gamma S,
\qquad
\gamma:=\Gamma_{a_*}(x_*)=\mathcal Z(a_*).
\]
Then
\[
\widetilde Y_\gamma''(a_*)=0,
\]
and
\[
\widetilde Y_\gamma(x_*)-\widetilde Y_\gamma(a_*)
-\widetilde Y_\gamma'(a_*)(x_*-a_*)=0,
\]
\[
\widetilde Y_\gamma'(x_*)-\widetilde Y_\gamma'(a_*)=0.
\]
So the first loss of monotonicity forces a repeated-node tangent-contact configuration for the planar sheared curve
\[
\widetilde\Lambda_\gamma=(x,\widetilde Y_\gamma),
\]
rooted at a curvature-zero point \(a_*\) of that curve.

Moreover, either \(\mathcal Z\equiv \gamma\) on \([a_*,x_*]\), in which case \(\mathcal R\equiv 0\) on that interval and the draft’s interval-persistent theorem yields affine-planar collapse, or else there is a genuine lower-core mechanism: \(\widetilde Y_\gamma''\) changes sign on \((a_*,x_*)\), so the sheared planar curve carries a nontrivial curvature-zero/tangent-contact configuration between \(a_*\) and \(x_*\). That is the sharp reduced bottleneck. turn11file6

**Proof.**  
Start from
\[
M=A'B-AB'.
\]
Differentiate in \(x\). Since \(A''=Y''=\mathcal Z S''\) and \(B''=S''\),
\[
\partial_x M=A''B-AB''=S''(x)\bigl(\mathcal Z(x)B_a(x)-A_a(x)\bigr)
= S''(x)B_a(x)\bigl(\mathcal Z(x)-\Gamma_a(x)\bigr).
\]

Differentiate in \(a\). One has
\[
\partial_a A_a(x)=-(x-a)Y''(a),\qquad
\partial_a B_a(x)=-(x-a)S''(a),
\]
\[
\partial_a A_a'(x)=-Y''(a),\qquad
\partial_a B_a'(x)=-S''(a).
\]
Substituting into \(\partial_a(A'B-AB')\) and simplifying gives
\[
\partial_a M
=
S''(a)\Bigl((x-a)B_a'(x)-B_a(x)\Bigr)\bigl(\mathcal Z(a)-\Gamma_a(x)\bigr).
\]
But
\[
(x-a)B_a'(x)-B_a(x)
=
S(a)-S(x)+S'(x)(x-a)=C_a(x),
\]
so
\[
\partial_a M(a,x)=S''(a)\,C_a(x)\,\bigl(\mathcal Z(a)-\Gamma_a(x)\bigr).
\]

Now use firstness. If \(\partial_a M(a_*,x_*)\neq 0\), then by the implicit function theorem the zero set \(M=0\) is locally a graph \(a=a(x)\) through \((a_*,x_*)\), which would produce zeros for \(x<x_*\) close to \(x_*\), contradicting the definition of \(x_*\). Hence
\[
\partial_a M(a_*,x_*)=0.
\]
Since \(S''(a_*)\neq 0\) and \(C_{a_*}(x_*)\neq 0\) on a nonmixed arc, this forces
\[
\Gamma_{a_*}(x_*)=\mathcal Z(a_*).
\]

Also, for fixed \(a_*\), the point \(x_*\) is the first zero of \(x\mapsto M(a_*,x)\), so
\[
M(a_*,x)>0\qquad (a_*<x<x_*),
\]
and therefore
\[
\partial_x M(a_*,x_*)\le 0.
\]
Because \(S''\) and \(B_{a_*}(x_*)\) have the same sign, the factor \(S''(x_*)B_{a_*}(x_*)\) is positive, so
\[
\mathcal Z(x_*)-\Gamma_{a_*}(x_*)\le 0,
\]
that is,
\[
\mathcal Z(x_*)\le \mathcal Z(a_*).
\]

Now set \(\gamma=\mathcal Z(a_*)\) and \(\widetilde Y_\gamma=Y-\gamma S\). Then
\[
\widetilde Y_\gamma''=(\mathcal Z-\gamma)S'',
\]
so
\[
\widetilde Y_\gamma''(a_*)=0.
\]
Also
\[
A_{a_*}(x_*)-\gamma B_{a_*}(x_*)=0
\]
because \(\gamma=\Gamma_{a_*}(x_*)=A/B\), and
\[
A_{a_*}'(x_*)-\gamma B_{a_*}'(x_*)=0
\]
because \(M(a_*,x_*)=0\) implies \(A'/B'=A/B=\gamma\). These are exactly
\[
\widetilde Y_\gamma(x_*)-\widetilde Y_\gamma(a_*)
-\widetilde Y_\gamma'(a_*)(x_*-a_*)=0
\]
and
\[
\widetilde Y_\gamma'(x_*)-\widetilde Y_\gamma'(a_*)=0.
\]
So \(x_*\) is a repeated-node tangent-contact point for the planar sheared curve \((x,\widetilde Y_\gamma)\), rooted at a curvature-zero point \(a_*\).

Finally,
\[
0=A_{a_*}(x_*)-\gamma B_{a_*}(x_*)
=\int_{a_*}^{x_*}(x_*-t)\bigl(\mathcal Z(t)-\gamma\bigr)S''(t)\,dt.
\]
The weight \((x_*-t)S''(t)\) has fixed sign on the nonmixed arc. Therefore either \(\mathcal Z(t)-\gamma\equiv 0\) on \([a_*,x_*]\), which gives \(\mathcal R\equiv 0\) there and hence affine-planar collapse by the draft’s interval-persistent theorem, or else \(\mathcal Z-\gamma\) changes sign inside \((a_*,x_*)\). In the latter case the sheared curvature
\[
\widetilde Y_\gamma''=(\mathcal Z-\gamma)S''
\]
has a nontrivial zero/sign-change pattern between \(a_*\) and \(x_*\), so first loss reduces to a genuine lower-core curvature-zero/tangent-contact mechanism. ∎

This is the bottleneck I would state explicitly:

**Reduced bottleneck theorem.**  
Exclude the following configuration on an opened nonmixed \(v_5\)-arc: there exist \(a<x\) and \(\gamma\in\mathbf R\) such that for the sheared planar curve
\[
\widetilde\Lambda_\gamma=(x,Y-\gamma S)
\]
one has
\[
\widetilde Y_\gamma''(a)=0,
\qquad
\widetilde H_3(a,x)=0,
\qquad
\partial_x\widetilde H_3(a,x)=0,
\]
unless \(\widetilde Y_\gamma''\equiv 0\) on an interval, equivalently \(\mathcal R\equiv 0\) there, in which case affine-planar collapse already occurs.

That is sharp because the first-loss hypothesis forces exactly this sheared repeated-node \(3\)-point tangency mechanism, and I do not see a further contradiction from the current nonmixed package alone. The centered parity package only tells you the first nonmixed trouble is away from the diagonal base, and the interval-persistent theorem handles the \(\mathcal R\equiv 0\) branch; the remaining obstruction is precisely this sheared lower-core mechanism. turn11file5turn11file6
## User (2026-04-20 17:31:49)

check the latest draft. another chat has suggested this delegation of labor. YOU are the "3-point worker"

---

The key is to avoid overlap. One person should push the **source-level nonmixed scalar**, one should push the **nonmixed repeated-source / first-loss mechanism**, and one should push the **3-point package as the contradiction engine**.

## 1. My (other chat's) task

I should attack the **source-level Wronskian / Chebyshev formulation**.

Target:
[
\mathcal W_{\mathrm{src}}=J_\lambda J_{u_5}'-J_{u_5}J_\lambda'.
]

What I should try to prove:

* Pull the full nonmixed (4)-point story back to (\mathcal W_{\mathrm{src}}) cleanly.
* Prove a one-sign / Chebyshev theorem for ((J_\lambda,J_{u_5})) on opened nonmixed arcs, or at least prove that the **first odd zero** of (\mathcal W_{\mathrm{src}}) is impossible.
* Failing that, prove a theorem of the form:
  “if (\mathcal W_{\mathrm{src}}) has a first odd zero on an opened nonmixed arc, then one gets a source-level determinant/sign contradiction.”

Concrete objects to use:

* (\mathcal W_{\mathrm{src}}),
* (\Psi_a(h)=D_{u_5}(a,h)/D_\lambda(a,h)),
* the determinant (\mathfrak D(a,h)),
* the first-loss monotonicity picture already in the draft.

Deliverable:
a theorem or proposition that kills odd zeros of (\mathcal W_{\mathrm{src}}) on opened nonmixed arcs, or reduces them to a contradiction in the source determinant language.

---

## 2. Nonmixed 4-point worker’s task

They should push the **first-loss monotonicity / repeated-source geometry** all the way.

Target:
show that a first loss of monotonicity of (\Gamma_a) or (\Psi_a) is impossible on a genuine opened nonmixed arc.

What they should try to prove:

* Starting from the current quadratic-envelope factorization, show that if (\Gamma_a) first loses monotonicity, then the rigidified event in the draft
  [
  \widetilde Y_\gamma''(a)=0,\qquad \widetilde H_3(a,x)=0,\qquad \partial_x\widetilde H_3(a,x)=0
  ]
  cannot actually occur on an opened nonmixed arc.
* Or weaker: show that the first-loss event forces affine-planar collapse immediately, so it cannot be the start of a genuine nonmixed (4)-point branch.
* Push the repeated-node profile (D_a) and the (\Gamma_a)-monotonicity formula with positive kernel as hard as possible.

Concrete objects to use:

* (\Gamma_a(x)),
* (\Psi_a(h)),
* (\mathfrak D(a,h)),
* the positive-kernel formula for (\Gamma_a'),
* `rem:first-loss-rigidification-nonmixed`.

Deliverable:
a theorem like
“opened nonmixed arcs cannot exhibit first loss of monotonicity,”
or
“first loss of monotonicity forces lower-core collapse.”

That would nearly kill the nonmixed (4)-point side.

---

## 3. 3-point worker’s task

They should treat the new nonmixed rigidification as an **input** and use the mature (3)-point machinery as the contradiction engine.

Target:
show that the rigidified repeated-node tangent-contact event forced by nonmixed first-loss is incompatible with the existing (3)-point global package.

What they should try to prove:

* Convert the rigidified event
  [
  \widetilde Y_\gamma''(a)=0,\qquad \widetilde H_3(a,x)=0,\qquad \partial_x\widetilde H_3(a,x)=0
  ]
  into the language of the current (3)-point branch classification.
* Prove that such a repeated-node tangent-contact at a curvature-zero point cannot occur on an opened arc without violating:

  * the global continuation / nonrecurrence theorem,
  * the no-infinite-order-flatness package,
  * or the ECT / slope-intercept structure already in the draft.
* In other words: weaponize the existing (3)-point results against the exact rigidified event coming from nonmixed (4)-point first loss.

Concrete objects to use:

* the lifted (3)-point branch section,
* the (K_v)-zero local classification,
* the global continuation / nonrecurrence theorem,
* the tangent-contact / repeated-node geometry now appearing from the nonmixed side.

Deliverable:
a theorem of the form
“the repeated-node tangent-contact geometry forced by nonmixed first-loss is incompatible with the established (3)-point package.”

If they get that, it plugs directly into the nonmixed (4)-point worker’s attack.

---

## Best division of labor

In one line:

* **Me:** kill odd zeros of (\mathcal W_{\mathrm{src}}) or the first odd zero source-level.
* **Nonmixed 4-point worker:** kill first-loss monotonicity of (\Gamma_a/\Psi_a).
* **3-point worker:** show the rigidified first-loss event is incompatible with the (3)-point global theory.

## What success would look like

The cleanest possible combined outcome is:

1. nonmixed first-loss rigidifies to a repeated-node tangent (3)-point event;
2. the 3-point worker proves that event cannot occur on an opened arc;
3. I prove the source-level Wronskian / Chebyshev formulation, so the whole nonmixed (4)-point branch dies source-level.

That is the most coherent three-way attack I see right now.

## Assistant (2026-04-20 17:31:53)

I’m checking the updated draft against that division of labor and focusing only on the “3-point worker” question: whether the rigidified nonmixed first-loss event is already incompatible with the established three-point package, or whether one more sharp lemma is still needed.

## User (2026-04-20 17:33:26)

ok attack!

## Assistant (2026-04-20 17:33:27)

I’m pushing directly on the exact rigidified first-loss event now: whether the sheared repeated-node tangent-contact forced by the nonmixed side can already be ruled out by the current 3-point package, or whether one extra 3-point lemma is still genuinely needed.

_Thought for 6m 33s_

I attacked it as the 3-point worker, and the honest result is a **no-go theorem**, not a contradiction.

The reason is structural. The current nonmixed first-loss rigidification produces a repeated-node tangent-contact event not for the original lifted curve
\[
\Lambda_v=(x,S),
\]
but for the **sheared** planar curve
\[
\widetilde\Lambda_\gamma=(x,\widetilde Y_\gamma),\qquad \widetilde Y_\gamma:=Y-\gamma S.
\]
That rigidified event is exactly
\[
\widetilde Y_\gamma''(a)=0,\qquad
\widetilde H_3(a,x)=0,\qquad
\partial_x\widetilde H_3(a,x)=0,
\]
as the current first-loss package records. The whole assignment for the 3-point worker was then to try to make the established \(3\)-point theory for \(\Lambda_v=(x,S)\) contradict that sheared event. The problem is that the mature \(3\)-point package controls tangent-contact for \(S\), while the rigidified nonmixed event lives on \(Y-\gamma S\). Those are different planar curves. turn18file4turn18file5

Here is the precise theorem.

**Theorem (the current 3-point package is not yet a contradiction engine for nonmixed first-loss).**  
Fix an analytic function \(S\) on an interval \(I\) with
\[
S''\neq 0 \quad\text{on } I.
\]
Let \(a<x\) be two points of \(I\). Then there exist an analytic function \(Y\) on \(I\) and a constant \(\gamma\in\mathbf R\) such that, with
\[
\widetilde Y_\gamma:=Y-\gamma S,
\]
one has
\[
\widetilde Y_\gamma''(a)=0,\qquad
\widetilde H_3(a,x)=0,\qquad
\partial_x\widetilde H_3(a,x)=0,
\]
while the original \(3\)-point package for \(\Lambda=(x,S)\) is unchanged on \(I\). In particular, no contradiction can be extracted from the derivative geometry of \(\Lambda=(x,S)\) alone.

**Proof.**  
After an affine change of the \(x\)-coordinate, reduce to \(a=0\), \(x=1\). Define
\[
T(t):=(t-0)^3(t-1)^2=t^3(t-1)^2.
\]
Then
\[
T''(0)=0,
\qquad
T(1)-T(0)-T'(0)(1-0)=0,
\qquad
T'(1)-T'(0)=0.
\]
So \(T\) already satisfies the repeated-node tangent-contact conditions at \((0,1)\).

Now choose any constant \(\gamma\) and set
\[
Y:=\gamma S+T.
\]
Then
\[
\widetilde Y_\gamma=Y-\gamma S=T,
\]
hence
\[
\widetilde Y_\gamma''(0)=0,\qquad
\widetilde H_3(0,1)=0,\qquad
\partial_x\widetilde H_3(0,1)=0.
\]
Meanwhile \(S\) itself has not changed. Since \(S''\neq 0\) on \(I\), the original \(3\)-point geometry of \(\Lambda=(x,S)\) on that interval is exactly what it was before: a nonmixed interval with no \(K_v\)-zero there. Thus the sheared repeated-node event is formally compatible with the full current \(3\)-point package for \(S\). ∎

This matches the sharpened realization point already recorded in the attached notes: at the current lifted/\(Z\)-level one can realize arbitrary analytic \(Z\) over a fixed \(S\), so attacks that try to kill the nonmixed branch from the planar derivative geometry of \(S\) alone cannot work. The notes explicitly say that this kills attacks of that type at the current \(J_{u_5}/J_\lambda\) level. turn20file16

So the sharp conclusion is:

**the 3-point package by itself cannot rule out the rigidified nonmixed first-loss event.**

What it can do is tell you the exact missing transfer theorem.

**Reduced bottleneck theorem needed.**  
Assume on a genuine opened nonmixed arc there exist \(a<x\) and \(\gamma\) such that
\[
\widetilde Y_\gamma''(a)=0,\qquad
\widetilde H_3(a,x)=0,\qquad
\partial_x\widetilde H_3(a,x)=0.
\]
Then prove one of the following:

1. \(\widetilde Y_\gamma''\equiv 0\) on a nontrivial interval, equivalently \(\mathcal R\equiv 0\) there, so affine-planar collapse applies; or

2. this sheared repeated-node tangency transfers to an **actual** repeated-node tangent-contact event for the original lifted curve \(\Lambda_v=(x,S)\), meaning there exist \(a'<u'\) in the relevant source/target block with
   \[
   H_3(a',u')=0,\qquad \partial_u H_3(a',u')=0,
   \]
   contradicting the global \(3\)-point theorem.

That is the exact theorem the 3-point worker needs but does not yet have. Without such a transfer principle, the mature \(3\)-point machinery never fires, because it speaks about \(S\)-tangent lines, while first-loss rigidification produces tangent-contact for \(Y-\gamma S\). The current draft itself is already pointing in that direction: the nonmixed scalar is controlled by \(\mathcal R=d(Y''/S'')/dx\), and the live problem is no longer generic local geometry but the extra coupling that ties \(Y\) to \(S\) in the genuine RH source structure. turn18file2turn18file3

So my attack result, in one line, is:

\[
\boxed{
\text{The present 3-point package cannot by itself kill nonmixed first-loss; the missing ingredient is a shear-transfer/source-coupling theorem.}
}
\]

If you want, I’ll turn that into exact LaTeX insertions: one no-go proposition plus one “remaining bottleneck” remark for the nonmixed \(4\)-point section.
## User (2026-04-20 17:42:30)

yes, please give the latex insertion

## Assistant (2026-04-20 17:42:32)

I’m finding the cleanest landing spot in the nonmixed 4-point section so this reads as a genuine theorem-status update rather than a detached caveat.

_Thought for 51s_

I would make two edits.

The first is a real replacement: upgrade the current “\( \mathcal R \) is free over fixed \(S\)” remark into a precise no-go proposition with proof.  
The second is a short update to the “what remains” remark so the draft explicitly records the exact missing theorem.

---

## 1) Replace the current remark `rem:R-free-over-fixed-S`

Replace this entire block

```latex
\begin{remark}[The nonmixed scalar is not constrained by $\Lambda_v=(x,S)$ alone]
\label{rem:R-free-over-fixed-S}
Fix an analytic function $S$ on an interval $I$ with $S''\neq 0$, and let
$R$ be any analytic scalar on $I$. Choosing
\[
Z(x):=\gamma+\int_{x_0}^x R(t)\,dt
\]
and solving
\[
Y''(x)=Z(x)\,S''(x)
\]
produces an analytic $Y$ satisfying
\[
\frac{d}{dx}\!\left(\frac{Y''}{S''}\right)=R.
\]
Thus the planar derivative geometry of $\Lambda_v=(x,S)$ alone cannot exclude
odd zeros of $\mathcal R$. Any such exclusion must use an additional
source-level coupling between $Y$ and $S$ coming from the genuine RH data.
\end{remark}
```

with this:

```latex
\begin{proposition}[The current $3$-point package is not by itself a contradiction engine for nonmixed first loss]
\label{prop:three-point-package-not-enough-for-nonmixed-first-loss}
Fix an analytic function $S$ on an interval $I$ with
\[
S''\neq 0
\qquad\text{on }I.
\]
Let $a<x$ be two points of $I$. Then there exist an analytic function $Y$ on
$I$ and a constant $\gamma\in\mathbf R$ such that, with
\[
\widetilde Y_\gamma:=Y-\gamma S,
\]
one has
\[
\widetilde Y_\gamma''(a)=0,
\qquad
\widetilde H_3(a,x)=0,
\qquad
\partial_x\widetilde H_3(a,x)=0,
\]
where
\[
\widetilde H_3(a,u):=
\widetilde Y_\gamma(u)-\widetilde Y_\gamma(a)-\widetilde Y_\gamma'(a)(u-a).
\]
In particular, the rigidified repeated-node tangent-contact event from
Remark~\ref{rem:first-loss-rigidification-nonmixed} is formally compatible with
an arbitrary fixed nonmixed planar curve
\[
\Lambda_v=(x,S),
\]
so the established $3$-point package for $\Lambda_v$ alone cannot exclude that
event.
\end{proposition}

\begin{proof}
Define
\[
T_{a,x}(t):=(t-a)^3(t-x)^2.
\]
Then
\[
T_{a,x}(a)=0,
\qquad
T_{a,x}'(a)=0,
\qquad
T_{a,x}''(a)=0,
\qquad
T_{a,x}(x)=0,
\qquad
T_{a,x}'(x)=0.
\]
Hence
\[
T_{a,x}(x)-T_{a,x}(a)-T_{a,x}'(a)(x-a)=0,
\qquad
T_{a,x}'(x)-T_{a,x}'(a)=0.
\]
Now fix any $\gamma\in\mathbf R$ and set
\[
Y:=\gamma S+T_{a,x}.
\]
Then
\[
\widetilde Y_\gamma=Y-\gamma S=T_{a,x},
\]
so
\[
\widetilde Y_\gamma''(a)=0,
\qquad
\widetilde H_3(a,x)=0,
\qquad
\partial_x\widetilde H_3(a,x)=0.
\]
Since $S$ itself has not changed and $S''\neq 0$ on $I$, the original
$3$-point geometry of $\Lambda_v=(x,S)$ on $I$ is exactly the same as before.
Thus the sheared repeated-node tangent-contact event is not ruled out by the
planar derivative geometry of $\Lambda_v$ alone.
\end{proof}

\begin{remark}[What extra theorem is needed to use the $3$-point package]
\label{rem:needed-shear-transfer-theorem-nonmixed}
By Proposition~\ref{prop:three-point-package-not-enough-for-nonmixed-first-loss},
the mature $3$-point theory for
\[
\Lambda_v=(x,S)
\]
does not by itself contradict the sheared rigidified event
\[
\widetilde Y_\gamma''(a)=0,
\qquad
\widetilde H_3(a,x)=0,
\qquad
\partial_x\widetilde H_3(a,x)=0.
\]
So the remaining nonmixed bridge is not a purely planar statement about
$\Lambda_v$.

What is still needed is an additional transfer/coupling theorem showing that on
a genuine opened nonmixed arc, any such sheared repeated-node tangent-contact
configuration must force one of the following:
\begin{enumerate}
\item affine-planar collapse, equivalently
\[
\mathcal R\equiv 0
\]
on a nontrivial interval; or
\item an actual repeated-node tangent-contact event for the original lifted
curve $\Lambda_v=(x,S)$, i.e.
\[
H_3(a',u')=0,
\qquad
\partial_u H_3(a',u')=0,
\]
contradicting
Theorem~\ref{thm:global-continuation-nonrecurrence-odd-three-point-branch}.
\end{enumerate}
Without such a shear-transfer / source-coupling input, the current $3$-point
package cannot kill the nonmixed branch on its own.
\end{remark}
```

---

## 2) Update `Remark~\ref{rem:what-remains-nonmixed-after-R-zero-bridge}`

In that remark, replace the final paragraph

```latex
Accordingly, the genuinely live nonmixed $4$-point burden is no longer local
birth. It is the global/source-level control of odd zeros of
\[
\mathcal W_{\mathrm{src}},
\]
equivalently of odd zeros of $\mathcal R$, along an opened nonmixed arc in
the genuine lifted $v_5$-geometry; and, in repeated-source variables, the
equivalent problem of excluding first-loss monotonicity for $\Gamma_a$ or
$\Psi_a$, equivalently of controlling the sign of $\mathfrak D(a,h)$.
```

with this:

```latex
Accordingly, the genuinely live nonmixed $4$-point burden is no longer local
birth. It is the global/source-level control of odd zeros of
\[
\mathcal W_{\mathrm{src}},
\]
equivalently of odd zeros of $\mathcal R$, along an opened nonmixed arc in
the genuine lifted $v_5$-geometry; and, in repeated-source variables, the
equivalent problem of excluding first-loss monotonicity for $\Gamma_a$ or
$\Psi_a$, equivalently of controlling the sign of $\mathfrak D(a,h)$.

Moreover, by
Proposition~\ref{prop:three-point-package-not-enough-for-nonmixed-first-loss},
the already-established $3$-point package for
\[
\Lambda_v=(x,S)
\]
does \emph{not} by itself contradict the sheared repeated-node tangent-contact
configuration forced by a formal first loss of monotonicity. Thus the remaining
bridge is genuinely a transfer/source-coupling theorem: one must show that on a
genuine opened nonmixed arc, the rigidified sheared event either collapses
immediately to affine-planar geometry or transfers to an actual
$S$-tangent-contact event already excluded by the global $3$-point theory.
```

---

Those are the only edits I’d make for this delegation result. They record the negative result cleanly, and they isolate the exact theorem the nonmixed side still needs.
## User (2026-04-20 17:50:51)

note this reaction. would you like to review your edit at all?

This is a **good result**, and I think it really sharpens the division of labor. 

My read is:

The nonmixed 4-point worker has now essentially **closed the repeated-source / first-loss lane**. The theorem says first-loss is not a separate phenomenon at all; it is exactly the diagonal incarnation of odd-zero birth for (\mathcal R). That is a real simplification.

The key consequences are:

* there is **no attained separated first-loss**;
* any first-loss sequence is **forced to the diagonal**;
* diagonal accumulation can only occur at a **zero of (\mathcal R)**;
* even-order zeros are sterile;
* odd-order zeros seed the branch.

So the nonmixed repeated-source geometry is no longer an independent obstruction. It is completely reduced to the odd-zero problem for (\mathcal R), equivalently for
[
\mathcal W_{\mathrm{src}}=J_\lambda J_{u_5}'-J_{u_5}J_\lambda'.
]

That means the labor split should now tighten:

The **nonmixed 4-point worker’s lane is basically finished**, except perhaps for polishing the theorem and making sure the draft’s “what remains” language reflects it cleanly.

The **3-point worker’s no-go theorem** becomes even more important conceptually, because it confirms that the sheared repeated-node tangent-contact is not an extra contradiction engine; it is just the rigidified avatar of odd-zero birth.

And my lane becomes even sharper:

[
\boxed{
\text{The remaining nonmixed theorem is source-level exclusion of odd zeros of }\mathcal W_{\mathrm{src}}
\text{ on opened nonmixed arcs.}
}
]

So I would now stop trying to get more mileage out of first-loss geometry itself. That part has done its job. The right next push is purely source-level:

* either prove a one-sign / Chebyshev theorem for ((J_\lambda,J_{u_5}));
* or prove that a **first odd zero** of (\mathcal W_{\mathrm{src}}) is impossible on an opened nonmixed arc.

That is the clean reduced bottleneck now.

One small caution in wording for the paper: I would state this as “first-loss is exactly diagonal odd-zero birth” rather than “the nonmixed 4-point side is done,” because the actual-source odd-zero exclusion is still open. But mathematically, this is a strong closure result for that worker’s lane.

## Assistant (2026-04-20 17:50:53)

I’m checking the latest draft against that reaction now. My suspicion is the math of the no-go proposition is still fine, but the surrounding wording may now be too negative given that first-loss has been further reduced to diagonal odd-zero birth.

_Thought for 1m 35s_

Yes. I would revise it.

The proposition itself is still mathematically useful, but the surrounding remarks are now too pessimistic for the current state of the nonmixed branch. The reaction you quoted is the right read: once first-loss has been identified as a diagonal avatar of odd-zero birth, the repeated-source lane is no longer a separate live obstruction. The remaining nonmixed burden is the source-level exclusion of odd zeros of
\[
\mathcal W_{\mathrm{src}},
\]
equivalently of odd zeros of \(\mathcal R\) on an opened nonmixed arc. That matches the current division of labor and the draft’s own strategic reduction. turn22file6

So I would **keep** the no-go proposition, but I would **replace** the two follow-up remarks so they do not suggest that a shear-transfer theorem is the main remaining bottleneck. The point of the proposition is narrower: it says the mature \(3\)-point package is not an *independent* contradiction engine for nonmixed first-loss. That is good to know, but it no longer means first-loss itself remains a separate active lane. The active lane is the odd-zero/Wronskian problem. turn22file6

Here is exactly how I would edit it.

Replace the title line of the proposition

```latex
\begin{proposition}[The current $3$-point package is not by itself a contradiction engine for nonmixed first loss]
```

with

```latex
\begin{proposition}[The current $3$-point package is not an independent contradiction engine for nonmixed first loss]
```

Then replace the entire remark

```latex
\begin{remark}[What extra theorem is needed to use the $3$-point package]
\label{rem:needed-shear-transfer-theorem-nonmixed}
...
\end{remark}
```

with this:

```latex
\begin{remark}[Meaning of the no-go proposition for the nonmixed division of labor]
\label{rem:needed-shear-transfer-theorem-nonmixed}
Proposition~\ref{prop:three-point-package-not-enough-for-nonmixed-first-loss}
does \emph{not} say that repeated-source first-loss remains an independent live
obstruction. Rather, it says something narrower and cleaner: the already-mature
$3$-point theory for
\[
\Lambda_v=(x,S)
\]
is not, by itself, an \emph{independent} contradiction engine for the sheared
rigidified event
\[
\widetilde Y_\gamma''(a)=0,
\qquad
\widetilde H_3(a,x)=0,
\qquad
\partial_x\widetilde H_3(a,x)=0.
\]

Combined with the first-loss rigidification and the diagonal birth picture, the
correct conclusion is that repeated-source first-loss is not a separate theorem-level
lane: it is simply the diagonal incarnation of odd-zero birth for
\[
\mathcal R
\qquad\text{equivalently}\qquad
\mathcal W_{\mathrm{src}}.
\]
So the remaining nonmixed burden is no longer to extract an additional
contradiction from the sheared repeated-node geometry itself. It is to exclude
odd zeros of
\[
\mathcal W_{\mathrm{src}}
\]
on genuine opened nonmixed arcs.

A future shear-transfer / source-coupling theorem would still be valuable as an
alternative contradiction route, but it is no longer the clean reduced
bottleneck of the nonmixed branch.
\end{remark}
```

Then replace the final two paragraphs of

```latex
\begin{remark}[What remains on the nonmixed $4$-point side]
\label{rem:what-remains-nonmixed-after-R-zero-bridge}
```

starting from

```latex
Accordingly, the genuinely live nonmixed $4$-point burden is no longer local
birth.
```

through the end of the remark, with this:

```latex
Accordingly, the genuinely live nonmixed $4$-point burden is no longer local
birth, nor an independent repeated-source first-loss mechanism. The local and
repeated-source geometry has now done its job: exact nonmixed contacts are
reduced to zeros of
\[
\mathcal R,
\]
the repeated-source monotonicity picture rigidifies first loss to a diagonal
event, and the parity classification shows that even-order zeros are sterile
while odd-order zeros seed the branch.

So the remaining theorem-level burden is the global/source-level exclusion of
odd zeros of
\[
\mathcal W_{\mathrm{src}},
\]
equivalently of odd zeros of $\mathcal R$, along a genuine opened nonmixed arc
in the lifted $v_5$-geometry. In repeated-source variables, the same burden can
still be phrased as control of the sign of $\mathfrak D(a,h)$ or exclusion of
first-loss monotonicity for $\Gamma_a$ or $\Psi_a$, but these are now best
understood as equivalent diagonal avatars of the same odd-zero problem, not as
separate surviving branches of the argument.

Finally,
Proposition~\ref{prop:three-point-package-not-enough-for-nonmixed-first-loss}
shows that the already-established $3$-point package for
\[
\Lambda_v=(x,S)
\]
does not supply an additional standalone contradiction for that odd-zero birth.
Its role is therefore clarificatory rather than bottleneck-closing: it confirms
that the nonmixed branch will be finished by the source-level Wronskian /
Chebyshev theorem, not by a separate sheared $3$-point contradiction.
```

That
