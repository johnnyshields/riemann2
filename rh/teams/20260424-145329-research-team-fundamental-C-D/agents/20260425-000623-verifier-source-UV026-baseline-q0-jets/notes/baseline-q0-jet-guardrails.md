# UV-026 Baseline \(q_0\)-Jet Guardrails

## Verdict

Current source does not provide the baseline \(q_0^{(k)}(m)\), \(0\le k\le9\),
tables needed by the Stage 1 generator.

What current source supports:

- \(q=\Phi'\) is defined.
- \(q_\pm(s)=q(t_\pm)\) and
  \(\Delta_m(s)=\Phi(t_-)-\Phi(t_+)\) are defined.
- \(q=q_0+\delta q\) and \(\Phi=\Phi_0+\delta\Phi\) are used for the
  baseline/corrected split.
- The baseline same-point block is expressed in terms of
  \(q_0(t_\pm)\), \(q_0'(t_\pm)\), and \(q_0''(t_\pm)\).
- The transfer section fixes ordinary \(z\) by \(s=z/Q^2\).
- Scale estimates for \(q_0,q_0',q_0'',q_0'''\) are supplied.

What current source does not support:

- exact values or formulas for \(q_0^{(k)}(m)\), \(0\le k\le9\);
- an exact theorem reducing these jets to \(q_{\loc}\), \(J_1[g_{\sm}]\), and
  \(E_{\est}\);
- ordinary-\(z\) coefficient tables for \(G_\pm^{(0)}\), \(N_0\), or
  \(\Delta_0\) derived from those jets;
- replacement of those tables by scale estimates.

## Accepted Reduction Shape

A valid baseline theorem may reduce the ten jets to existing objects, but it
must be explicit.  One acceptable shape is:

\[
q_0(t)=q_{\loc}(t)+J_1[g_{\sm}](t)+E_{\est}(t)
\]
in the same baseline normalization as \(G_\pm^{(0)}\) and \(N^{(0)}\), followed
by formulas for
\[
q_0^{(k)}(m),\qquad 0\le k\le9.
\]

For \(k\ge2\), the affine jet contributes zero, so such a theorem would need
to supply
\[
q_{\loc}^{(k)}(m)+E_{\est}^{(k)}(m)
\]
and the \(k=0,1\) formulas including the affine jet contribution.  If
\(E_{\est}\) is to be discarded or normalized away, that must be stated and
proved in the Stage 1 normalization.

## Rejection Criteria

Reject or quarantine any proposed Stage 1 baseline table that:

- gives only \(O(Q^j)\) scales for \(q_0^{(j)}\);
- lists \(s\)- or \(w\)-coefficients without converting through \(s=z/Q^2\);
- uses post-\(\Phi_K\) transfer coefficients;
- silently identifies \(q_0\) with \(q_{\loc}\) alone;
- drops \(E_{\est}\) without a theorem;
- gives \(G_\pm^{(0)}\) or \(N_0\) tables generated from demo data rather than
  actual baseline jets.

## Sharp Missing Substatement

Prove a baseline \(q_0\)-jet theorem in ordinary \(z\), before \(\Phi_K\), in
the same normalization used by the Stage 1 source-table generator:

1. define \(q_0\) explicitly as a scalar germ at the midpoint \(m\);
2. give formulas for \(q_0^{(k)}(m)\), \(0\le k\le9\), or reduce them to
   named paper baseline objects with displayed formulas;
3. prove that substituting \(s=z/Q^2\) gives the generator's ordinary-\(z\)
   inputs for \(G_\pm^{(0)}\), \(N_0\), and \(\Delta_0\);
4. keep this theorem independent of the scalar source-grade projection
   \(r_i^{[1/5]}\).
