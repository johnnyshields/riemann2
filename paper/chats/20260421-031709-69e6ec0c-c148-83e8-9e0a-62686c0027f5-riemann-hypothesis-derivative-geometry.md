# Riemann Hypothesis Derivative Geometry

- Source: https://chatgpt.com/c/69e6ec0c-c148-83e8-9e0a-62686c0027f5
- Created: 2026-04-21 03:17:09 UTC
- Default model: gpt-5-4-thinking

---

## User (2026-04-21 03:17:08)

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

YOUR TASK: Starting from a fixed-shear mixed branch for (A,B,F), prove that the branch must either satisfy one of the existing mixed low-order obstruction types or accumulate on (K_v=0). Express everything in the current (v)-patch derivative-geometry language.

## Assistant (2026-04-21 03:17:09)

I’m pulling the exact mixed 2-point and \(K_v\)-patch machinery out of the draft first, then I’ll try to turn the fixed-shear branch conditions into a derivative-geometry dichotomy. If the draft already has a near-matching lemma under a different name, I’ll fold that in rather than reinventing it.

I found the key point in the current draft: it already reduces the frozen branch to accumulation on \(\{S=0\}\cup\{K_v=0\}\). So the real job is now to show that points with \(S=0\) but \(K_v\neq 0\) are not a genuinely new lane; either they force the known mixed low-order jets, or they are harmless.

_Thought for 11m 36s_

I think the clean derivative-geometric theorem is slightly different from the one in the handoff, and stronger in the right way.

Away from \(K_v=0\), a frozen mixed \(2\)-point branch does **not** naturally reduce to the mixed low-order list. It reduces to the already-developed **nonmixed repeated-source** geometry governed by
\[
\mathcal Z=\frac{Y''}{S''},\qquad \mathcal R=\mathcal Z'=\frac{T_v}{K_v^2}.
\]
So the honest dichotomy is:

- either the frozen mixed branch accumulates on \(K_v=0\), where the existing mixed low-order list \((1,2),(1,4),(2,4)\) lives;
- or, on \(\{K_v\neq 0\}\), it transfers into the nonmixed repeated-source \(\mathcal R\)-branch.

That is probably the right theorem to add.

Here is the core statement in draft-ready form.

```latex
\begin{proposition}[Frozen mixed $2$-point branch: nonmixed transfer or $K_v$-accumulation]
\label{prop:frozen-mixed-two-point-nonmixed-transfer-or-Kv}
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
Fix
\[
(\eta,\xi,\gamma)\in\mathbf C^3,
\]
and define the frozen sheared ratio map
\[
\Phi(x):=
\left(
\frac{x-\xi S}{1-\eta S},
\frac{Y-\gamma S}{1-\eta S}
\right).
\]

Assume there exist sequences
\[
x_{1,n}\neq x_{2,n},
\qquad
x_{1,n},x_{2,n}\to a\in U,
\]
such that
\[
\Phi(x_{1,n})=\Phi(x_{2,n})
\qquad\text{for all }n.
\]
Then either
\[
K_v(a)=0,
\]
or else
\[
K_v(a)\neq 0,\qquad S(a)=0,\qquad S_x(a)\neq 0,
\]
and the branch is absorbed by the nonmixed repeated-source geometry at $a$.

More precisely, set
\[
\mathcal Z:=\frac{Y''}{S''},
\qquad
\mathcal R:=\mathcal Z'=\frac{T_v}{K_v^2},
\]
and let
\[
\nu:=\operatorname{ord}_a\mathcal R.
\]
Then, after an affine change of target and an analytic reparametrization of the
source, the tangent-projection germ of $\Phi$ at $a$ has normal form
\[
t\longmapsto (t^2,t^{\nu+3}).
\]
In particular, if $\nu$ is even then there is no local exact close two-point
branch through $a$, while if $\nu$ is odd then the branch is exactly the
already-existing odd-zero repeated-source branch on the nonmixed side.
\end{proposition}

\begin{proof}
By the fixed-shear reduction, the branch gives nearby repeated values of
\[
\Phi(x)=\left(\frac{x-\xi S}{1-\eta S},\frac{Y-\gamma S}{1-\eta S}\right).
\]
Hence, by Rolle on each component,
\[
\Phi_x(\zeta_n)=0
\]
for some $\zeta_n$ between $x_{1,n}$ and $x_{2,n}$, and therefore
\[
\Phi_x(a)=0.
\]

Now Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction}
already shows that any such accumulation point lies in
\[
\{S=0\}\cup\{K_v=0\}.
\]
So if $K_v(a)\neq 0$, then necessarily $S(a)=0$.

Write
\[
\Phi=(\Phi_1,\Phi_2).
\]
A direct differentiation gives
\[
\Phi_{1,x}
=
\frac{1-\eta S+(\eta x-\xi)S_x}{(1-\eta S)^2},
\qquad
\Phi_{2,x}
=
\frac{(1-\eta S)Y_x+(\eta Y-\gamma)S_x}{(1-\eta S)^2}.
\]
Evaluating at $a$ and using $S(a)=0$ yields
\[
0=\Phi_{1,x}(a)=1+(\eta x(a)-\xi)S_x(a).
\]
Hence $S_x(a)\neq 0$. So $a$ is a simple zero of $S$.

Now pass to the tangent-projection normal form. Translate $a$ to $0$ in the
$x$-coordinate and replace $Y$ by
\[
\widetilde Y(x)
:=
Y(x)-Y(0)-Y_x(0)x-\mathcal Z(0)\bigl(S(x)-S(0)-S_x(0)x\bigr).
\]
Then
\[
\widetilde Y(0)=\widetilde Y_x(0)=\widetilde Y_{xx}(0)=0,
\qquad
\widetilde Y''=S''\bigl(\mathcal Z-\mathcal Z(0)\bigr).
\]
Since $K_v(0)\neq 0$, one has $S''(0)\neq 0$. If
\[
\nu=\operatorname{ord}_0\mathcal R,
\]
then
\[
\mathcal Z(x)-\mathcal Z(0)=c_\nu x^{\nu+1}+O(x^{\nu+2}),
\qquad c_\nu\neq 0,
\]
and therefore
\[
\widetilde Y(x)=\widetilde c_\nu x^{\nu+3}+O(x^{\nu+4}),
\qquad \widetilde c_\nu\neq 0.
\]

On the other hand, since $S(0)=0$ and $S_x(0)\neq 0$,
\[
x-\frac{S}{S_x}
=
\frac{S''(0)}{2S_x(0)}x^2+O(x^3).
\]
Likewise,
\[
\widetilde Y-\frac{S}{S_x}\widetilde Y_x
=
\widetilde c_\nu x^{\nu+3}+O(x^{\nu+4}).
\]
Thus, after affine target normalization and analytic reparametrization, the
projected germ is
\[
x\longmapsto (x^2,x^{\nu+3}).
\]

Finally, the germ
\[
t\mapsto (t^2,t^m)
\]
has a local exact close two-point branch iff $m$ is even. Here
\[
m=\nu+3,
\]
so this happens exactly when $\nu$ is odd. That is precisely the parity rule
for the nonmixed repeated-source branch governed by $\mathcal R$.
\end{proof}
```

The useful concrete jet expansion hiding inside that proof is this. After the affine normalization that kills the constant, linear, and quadratic tangential part of the second coordinate, the tangent-projection germ has
\[
u(t)=\frac{K_v(a)}{2S_x(a)}\,t^2+O(t^3),
\]
and
\[
v(t)= -\frac{K_v(a)}{3}\,\mathcal R(a)\,t^3
      -\frac{K_v(a)}{8}\,\mathcal R_x(a)\,t^4
      +O(t^5).
\]
So:

- if \(\mathcal R(a)\neq 0\), you get the ordinary cusp type \((t^2,t^3)\), which is locally one-to-one and cannot support a close exact \(2\)-point branch;
- if \(\mathcal R(a)=0\) and \(\mathcal R_x(a)\neq 0\), you get the first even type \((t^2,t^4)\);
- higher odd-order zeros of \(\mathcal R\) give the higher even types \((t^2,t^6)\), \((t^2,t^8)\), etc.

So the real takeaway is:

the frozen \(\lambda\)-shear route does not leave a genuinely generic exceptional set on \(\{K_v\neq 0\}\). It collapses into the already-built nonmixed repeated-source \(\mathcal R\)-theory. The only genuinely mixed accumulation lane left is \(K_v=0\), and that is exactly where your existing mixed low-order obstruction list
\[
(\operatorname{ord}J_\lambda,\operatorname{ord}J_{u_5})=(1,2),(1,4),(2,4)
\]
belongs.

I would follow this proposition with a short remark like this:

```latex
\begin{remark}[What remains on the frozen mixed $2$-point route]
\label{rem:frozen-mixed-two-point-what-remains}
Proposition~\ref{prop:frozen-mixed-two-point-nonmixed-transfer-or-Kv} shows
that the fixed-shear mixed $2$-point route does not create a new generic
exceptional branch on the nonmixed region $\{K_v\neq 0\}$. Away from $K_v=0$,
it transfers into the already-existing repeated-source branch governed by
\[
\mathcal R=\frac{T_v}{K_v^2}.
\]
Accordingly, the only genuinely mixed accumulation lane left for the
fixed-shear overlap-patch attack is the curvature locus
\[
K_v=0,
\]
and that is precisely the locus on which the existing mixed low-order
obstruction types
\[
(\operatorname{ord}J_\lambda,\operatorname{ord}J_{u_5})
=(1,2),\ (1,4),\ (2,4)
\]
live.
\end{remark}
```

If you want, I can next turn this into a tighter insertion that explicitly references the existing repeated-source theorem labels already in the draft, so it meshes cleanly with the current nonmixed package.
## User (2026-04-21 03:31:10)

yes, please give it to me as a tighter insertion: If you want, I can next turn this into a tighter insertion that explicitly references the existing repeated-source theorem labels already in the draft, so it meshes cleanly with the current nonmixed package.

## Assistant (2026-04-21 03:31:11)

I’m matching this to the draft’s exact theorem labels now so the insertion drops in without fighting the current structure. I’ll also check whether the “mixed low-order list” is already packaged as a proposition/corollary that should be cited directly.

_Thought for 6m 31s_

Yes — here is a tighter insertion that meshes with the current draft’s actual theorem labels and sharpens the status of the frozen \(\lambda\)-shear route.

I would make two edits.

First, **replace** the current Remark~\ref{rem:wip-mixed-lambda-shear-route-status} with the following proposition + remark.

```latex
\begin{proposition}[Off $K_v=0$, the frozen mixed $2$-point route is already the nonmixed odd-zero route]
\label{prop:frozen-mixed-two-point-off-Kv-is-nonmixed-odd-zero}
Work on the overlap patch of
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction},
and write
\[
\Phi(x):=
\left(
\frac{x-\xi_* S}{1-\eta_* S},
\frac{Y-\gamma_* S}{1-\eta_* S}
\right).
\]
Assume there is a close exact frozen mixed $2$-point branch
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
S_x(a)\neq 0,
\qquad
\mathcal R(a)=0,
\]
where
\[
\mathcal Z=\frac{Y''}{S''},
\qquad
\mathcal R=\mathcal Z'=\frac{T_v}{K_v^2}.
\]

More precisely, if
\[
\nu:=\operatorname{ord}_a \mathcal R,
\]
then after analytic source reparametrization centered at $a$ and affine target
normalization, the frozen repeated-value germ takes the form
\[
t\longmapsto
\bigl(t^2,\ c_{\nu+3} t^{\nu+3}+O(t^{\nu+4})\bigr),
\qquad
c_{\nu+3}\neq 0.
\]
Consequently, an actual close exact frozen mixed $2$-point branch on
\[
\{K_v\neq 0\}
\]
can occur only when $\nu$ is odd. Equivalently, off $K_v=0$ the frozen mixed
route is already forced onto the odd-zero $\mathcal R$-geometry of the
nonmixed repeated-source problem.
\end{proposition}

\begin{proof}
By
Proposition~\ref{prop:conditional-mixed-lambda-shear-projective-shadow-reduction},
any accumulation point of the frozen branch lies in
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
\zeta_{1,n},\zeta_{2,n}\in (x_{1,n},x_{2,n})
\]
such that
\[
\partial_x\Phi_1(\zeta_{1,n})=0,
\qquad
\partial_x\Phi_2(\zeta_{2,n})=0.
\]
Hence
\[
\partial_x\Phi(a)=0.
\]

Now
\[
\partial_x\Phi_1
=
\frac{1-(\xi_*-\eta_* x)S_x-\eta_* S}{(1-\eta_* S)^2},
\]
so at $x=a$, using $S(a)=0$, one gets
\[
0=\partial_x\Phi_1(a)=1-(\xi_*-\eta_* x(a))S_x(a).
\]
Thus
\[
S_x(a)\neq 0,
\qquad
\beta:=\xi_*-\eta_* x(a)=\frac{1}{S_x(a)}.
\]

Set
\[
U(x):=x-\beta S(x).
\]
Then
\[
U(a)=0,
\qquad
U_x(a)=0,
\qquad
U_{xx}(a)=-\beta S_{xx}(a).
\]
Since
\[
K_v=(x')^3 S_{xx}
\]
on the $v_5$-patch and $K_v(a)\neq 0$, one has
\[
S_{xx}(a)\neq 0,
\]
hence
\[
U_{xx}(a)\neq 0.
\]

Because the denominator $1-\eta_* S$ is a unit near $a$, the germ $\Phi$ is
affine-target-equivalent to a germ of the form
\[
x\longmapsto (U(x),V(x)),
\]
where $V$ differs from $Y$ by an element of
\[
\operatorname{span}\{1,x,S\}.
\]
Choose the affine normalization so that
\[
V(a)=V_x(a)=V_{xx}(a)=0.
\]
Then the first nonzero degree of $V$ is exactly the first nonzero degree of the
nonmixed normalized height function from
Remark~\ref{rem:nonmixed-four-point-zeros-can-carry-preexisting-branches}.
Equivalently, if
\[
\nu=\operatorname{ord}_a\mathcal R,
\]
then
\[
V(x)=\widetilde c_{\nu+3}(x-a)^{\nu+3}+O\!\bigl((x-a)^{\nu+4}\bigr),
\qquad
\widetilde c_{\nu+3}\neq 0.
\]

Finally, since $U_{xx}(a)\neq 0$, an analytic source reparametrization gives
\[
U=t^2.
\]
So the frozen repeated-value germ is analytically equivalent to
\[
t\longmapsto
\bigl(t^2,\ c_{\nu+3} t^{\nu+3}+O(t^{\nu+4})\bigr),
\qquad
c_{\nu+3}\neq 0.
\]
If $\nu$ is even, then $\nu+3$ is odd, and
\[
\bigl(c_{\nu+3} t^{\nu+3}+O(t^{\nu+4})\bigr)
-
\bigl(c_{\nu+3} (-t)^{\nu+3}+O(t^{\nu+4})\bigr)
=
2c_{\nu+3} t^{\nu+3}+O(t^{\nu+4})\neq 0
\]
for all sufficiently small $t\neq 0$. Since equality of first coordinates
forces the two source points to be opposite to first order, no exact nearby
repeated values are then possible. Therefore a close exact frozen mixed
$2$-point branch on $\{K_v\neq 0\}$ requires $\nu$ odd, and in particular
\[
\mathcal R(a)=0.
\]
\end{proof}

\begin{remark}[What the frozen $\lambda$-shear reduction now leaves]
\label{rem:frozen-mixed-two-point-route-status-sharpened}
Proposition~\ref{prop:frozen-mixed-two-point-off-Kv-is-nonmixed-odd-zero}
shows that the fixed-shear overlap-patch route does \emph{not} leave a new
generic exceptional set on
\[
\{K_v\neq 0\}.
\]
Away from $K_v=0$, any close exact frozen mixed $2$-point branch is already
forced onto the same odd/even $\mathcal R$-parity regime that governs the
nonmixed repeated-source problem
(Remark~\ref{rem:nonmixed-four-point-zeros-can-carry-preexisting-branches} and
Proposition~\ref{prop:parity-classification-isolated-nonmixed-R-zeros}).

Thus, on the nonmixed side, the relevant source-level control is already the
existing repeated-source package: the born odd-zero branch is uniformly
unrooted near its seed by
Proposition~\ref{prop:odd-zero-critical-branch-uniformly-unrooted} and its
source-determinant form
(Proposition~\ref{prop:source-determinant-form-odd-zero-unrooted-defect}),
while any rooted realization along an opened nonmixed arc is constrained by
Proposition~\ref{prop:first-rooting-requires-second-odd-zero-repeated-source}
and excluded entirely when there is at most one odd zero by
Proposition~\ref{prop:at-most-one-odd-zero-no-genuine-repeated-source-obstruction}.

Accordingly, after freezing the $\lambda$-shear, the only genuinely mixed
accumulation lane still left on the overlap patch is
\[
K_v=0.
\]
That is exactly the derivative-geometric lifted-$3$-point locus already
governed by
Proposition~\ref{prop:shrinking-exact-lifted-three-point-circuits-force-Kv-zero},
Corollary~\ref{cor:uniform-small-diameter-exclusion-away-from-Kv-zero},
Theorem~\ref{thm:local-classification-lifted-three-point-branch-near-Kv-zero},
and
Theorem~\ref{thm:global-continuation-nonrecurrence-odd-three-point-branch}.
The explicit mixed low-order obstruction list remains the finite
Wronskian-order list recorded in
Remark~\ref{rem:wronskian-order-reformulation-mixed-list}.
\end{remark}
```

That replacement does two useful things. It removes the stale “\(S=0\) or lower-core tangency” wording, and it says cleanly that \(S=0\) off \(K_v=0\) is no longer a separate mixed lane at all.

Second, I would tighten the corresponding paragraph in Remark~\ref{rem:live-attack-routes}. In item 1, replace the final sentence

```latex
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or source-coupled control of
the mixed $\lambda$-shear exceptional loci.
```

with

```latex
So the remaining two-point work is either finite-order source-level merger,
quotient-diagonal continuity/diagonal collapse, or control of the \emph{genuinely
mixed} frozen-$\lambda$-shear locus
\[
K_v=0.
\]
Indeed, by
Proposition~\ref{prop:frozen-mixed-two-point-off-Kv-is-nonmixed-odd-zero},
the complementary slice
\[
\{S=0\}\cap\{K_v\neq 0\}
\]
is already absorbed into the existing nonmixed repeated-source odd-zero
$\mathcal R$-package rather than creating a new mixed obstruction lane.
```

This is the sharper version I’d put in the paper.
