# UV-016 compact regularization reduction

## Claim

The compact convergence part of UV-016 has a clean theorem target.

Let \(\chi\) be primitive nonprincipal and set
\[
\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline{\chi}).
\]
Assume the standard completed-\(L\) inputs: \(\Xi_\chi\) is entire of order one,
\(\Xi_\chi(s)=\Xi_\chi(1-s)\), and its zero multiset \(Z_\chi^{\rm pair}\) is
counted with multiplicity. Let \(I\subset \mathbb R\) be compact and avoid edge
zeros \(2it\in Z_\chi^{\rm pair}\) and \(1+2it\in Z_\chi^{\rm pair}\).

Then the strip-edge zero series
\[
S_\chi^{\rm edge}(t)
=\sum_{\rho\in Z_\chi^{\rm pair}}
m_\rho\,\Re\left(
\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}
\right)
\]
converges absolutely and uniformly on \(I\). The same is true after any fixed
number of \(t\)-derivatives. It is therefore a legitimate compact-interval
regularized zero contribution, with multiplicity bookkeeping built into the
coefficient \(m_\rho\).

This proves only the compact zero-summation layer. It does not by itself prove
the project-level identity \(q_\chi^{\rm pair}=B_\chi^{\rm pair}
+S_\chi^{\rm pair}\) with the preferred phase sign and explicit
conductor/gamma/trivial-zero background.

## Proof

For an entire function of order one, the genus-one Hadamard product gives
\[
\frac{\Xi_\chi'}{\Xi_\chi}(z)
=b_\chi+\sum_{\rho\in Z_\chi^{\rm pair}}m_\rho
\left(\frac{1}{z-\rho}+\frac{1}{\rho}\right),
\]
in the usual locally uniform regularized sense away from the zeros. Hence, for
\(w_-(t)=2it\) and \(w_+(t)=1+2it\),
\[
\frac{\Xi_\chi'}{\Xi_\chi}(w_+(t))
-\frac{\Xi_\chi'}{\Xi_\chi}(w_-(t))
=
\sum_{\rho\in Z_\chi^{\rm pair}}m_\rho
\left(
\frac{1}{w_+(t)-\rho}
-\frac{1}{w_-(t)-\rho}
\right),
\]
provided the difference series is locally absolutely convergent. The constants
\(b_\chi\) and \(1/\rho\) cancel. This is the actual compact regularization:
two nonabsolute logarithmic-derivative sums are replaced by their edge
difference.

It remains only to check convergence of that difference. Let
\(M=2\sup_{t\in I}|t|+2\). For \(|\rho|>2M\) and \(t\in I\),
\[
|w_\pm(t)-\rho|\ge |\rho|/2.
\]
Therefore
\[
\left|
\frac{1}{w_+(t)-\rho}-\frac{1}{w_-(t)-\rho}
\right|
=
\frac{1}{|(w_+(t)-\rho)(w_-(t)-\rho)|}
\le \frac{4}{|\rho|^2}.
\]
The order-one product gives
\(\sum_{\rho}m_\rho|\rho|^{-2}<\infty\), so the Weierstrass test gives absolute
uniform convergence on \(I\). The finitely many zeros with \(|\rho|\le 2M\) are
harmless because \(I\) avoids edge zeros.

For \(n\ge 1\), the \(n\)-th \(t\)-derivative of each reciprocal is a constant
multiple of \((w_\pm(t)-\rho)^{-n-1}\), hence is \(O_{I,n}(|\rho|^{-n-1})\) for
large \(\rho\). This is summable because \(n+1\ge 2\). Termwise
differentiation follows on \(I\).

If \(\rho=\beta+i\gamma\) with \(0\le \beta\le 1\), the real part of the edge
difference is
\[
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2},
\]
so every one-zero contribution is nonnegative, and it is positive away from the
degenerate edge cases excluded above.

## Phase and background boundary

Set
\[
D_\chi(t)=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
The theorem above proves that \(D_\chi(t)\) is represented by the absolutely
convergent paired edge-difference sum. For
\[
\Phi_\chi^{\rm pair}(s)=
\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)},
\]
one has on \(s=1/2+it\)
\[
\frac{\Phi_\chi^{{\rm pair}\prime}}{\Phi_\chi^{\rm pair}}(s)
=-2D_\chi(t).
\]
Thus the positive kernel orientation is tied to \(D_\chi(t)\). The
source-normalized \(q_\chi^{\rm pair}=B_\chi^{\rm pair}+S_\chi^{\rm pair}\)
identity still needs a sign convention: with this quotient, the positive
edge-kernel side corresponds to the negative boundary-phase convention, or
equivalently to inverting the quotient if the positive boundary convention is
kept.

The unified \(B_\chi^{\rm pair}\) issue is also separate. The argument above
proves compact convergence for the completed paired zero contribution. It does
not identify the theorem-ready component formula for the background term in the
raw \(L\)-factor split. The smallest remaining theorem statements are:

1. A phase-normalization theorem choosing the sign so the positive
   edge-difference is the \(+S_\chi^{\rm pair}\) part of \(q_\chi^{\rm pair}\).
2. A background-split theorem proving that the chosen
   \(B_\chi^{\rm pair}\) equals exactly the conductor/scaling, gamma-derivative,
   trivial-zero or pole, and any Hadamard-constant residue left after the same
   compact edge sum is subtracted.
3. A source-package statement tying the multiplicity convention above to that
   same background split.

## Honest verdict

This route moves UV-016 beyond pure blueprint for compact convergence:
the paired edge-difference zero series is compactly and differentiably
convergent by Hadamard cancellation. From this agent scope alone, full UV-016
still remains open because the explicit \(B_\chi^{\rm pair}\) split and the
phase sign are not closed by the convergence proof.
