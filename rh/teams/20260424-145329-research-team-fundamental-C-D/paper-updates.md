# Paper Updates

Staged candidate edits for `rh/proof_of_rh.tex`. These are coordinator-owned
and not yet applied to the canonical paper.

## UV-025 tagged pre-whitening source block

Suggested placement: after the one-pair weighted corrected-block bookkeeping
around `proof_of_rh.tex:2659--2787`, before downstream quotient-output package
language.

Verification:

- Source check:
  `agents/20260424-195414-verifier-source-UV025-B2-block/report.md`.
- Adversarial overclaim check:
  `agents/20260424-195414-verifier-adversarial-UV025-B2-overclaim/report.md`.
- Candidate source:
  `agents/20260424-194928-gap-closer-UV025-B2-definition/notes/B2-definition-block.md`.

Guardrails:

- This block is before whitening, before `\Phi_K`, and before determinant or
  quotient extraction.
- It defines a tagged pre-whitening corrected source lift; it is not already
  supplied by existing quotient-output `\mathfrak P_2` language.
- Source tags are retained through `\operatorname{Lin}_{\mathcal K}`.
- `\mathcal K` is pair-kernel degree, not `\Pi_{1,1}` and not a quotient-gauge
  theorem.
- This block does not assert package coincidence, one-amplitude collapse of
  finite-order quotients, diagonal merger, `B_7^{\mathfrak f}`, `Q_{7,m}^q`,
  or UV-026 gauge.

Proposed insertion:

```tex
\begin{definition}[Tagged two-atom pre-whitening source block]
\label{def:tagged-two-atom-prewhitening-source-block}
Introduce formal source tags \(\tau_1,\tau_2\).  For a normalized two-atom
core \((a_1,h_1;a_2,h_2)\), define the tagged corrected source perturbations by
additive substitution into the corrected phase variables:
\[
d_\pm^{(2)}:=\tau_1a_1d_{h_1,\pm}+\tau_2a_2d_{h_2,\pm},
\qquad
e_\pm^{(2)}:=\tau_1a_1e_{h_1,\pm}+\tau_2a_2e_{h_2,\pm},
\]
\[
g_\pm^{(2)}:=\tau_1a_1g_{h_1,\pm}+\tau_2a_2g_{h_2,\pm},
\qquad
\eta^{(2)}:=\tau_1a_1\eta_{h_1}+\tau_2a_2\eta_{h_2}.
\]
Equivalently,
\[
q_{2,\pm}=q_{0,\pm}+d_\pm^{(2)},\qquad
q'_{2,\pm}=q'_{0,\pm}+e_\pm^{(2)},\qquad
q''_{2,\pm}=q''_{0,\pm}+g_\pm^{(2)},\qquad
\Delta_2=\Delta_0+\eta^{(2)}.
\]
Define
\[
\mathcal B_2(a_1,h_1;a_2,h_2)
:=(G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})
\]
by the same corrected same-point and mixed block formulas used above for the
one-pair corrected block, with \(q_\pm,\Delta\) replaced by
\(q_{2,\pm},\Delta_2\).  Set
\[
\mathcal B_0:=(G_-^{(0)},N^{(0)},G_+^{(0)}).
\]
\end{definition}

\begin{definition}[Pair-kernel linear part]
\label{def:pair-kernel-linear-part}
Let \(\mathcal K\) be the filtration on entries of
\(\mathfrak D_Q(\mathcal B_2-\mathcal B_0)\) in which each tagged source kernel
\[
\tau_iU_{i,\pm},\qquad \tau_iE_{i,\pm},\qquad
\tau_iG_{i,\pm},\qquad \tau_iV_i
\]
has \(\mathcal K\)-degree \(1\), while baseline factors, the amplitudes \(a_i\),
\(Q\)-scales, and bounded analytic coefficients have degree \(0\).  Let
\(\operatorname{Lin}_{\mathcal K}\) denote projection to
\(\mathcal K\)-degree \(1\).

Define the one-atom source-linear triple by
\[
L_h:=\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_1(h)-\mathcal B_0),
\]
where \(\mathcal B_1(h)\) is the one-atom corrected block obtained from the
same corrected block formulas.
\end{definition}

\begin{lemma}[Tagged pair-kernel linearity of the source block]
\label{lem:tagged-pair-kernel-linearity-source-block}
With source tags retained,
\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q\bigl(\mathcal B_2(a_1,h_1;a_2,h_2)-\mathcal B_0\bigr)
=
\tau_1a_1L_{h_1}+\tau_2a_2L_{h_2}.
\]
After this tagged \(\mathcal K\)-linear projection is taken, applying the
augmentation \(\tau_1,\tau_2\mapsto1\) gives
\[
\operatorname{Lin}_{\mathcal K}
\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=a_1L_{h_1}+a_2L_{h_2}.
\]
\end{lemma}

\begin{proof}
For the same-point blocks \(G_{2,\pm}^{\corr}\), the \((1,1)\) and
off-diagonal entries are linear in \(d_\pm^{(2)}\) and \(e_\pm^{(2)}\).  The
\((2,2)\) entry has the form
\[
g_\pm^{(2)}
+\text{baseline}\cdot d_\pm^{(2)}
+\text{terms of }\mathcal K\text{-degree at least }2,
\]
by the same expansion as in the one-pair corrected block calculation.

For the mixed block \(N_2^{\corr}\), Taylor expansion in
\((d_-^{(2)},d_+^{(2)},\eta^{(2)})\) gives a bounded-baseline linear
combination of those variables and a remainder of \(\mathcal K\)-degree at
least \(2\).  Since the tagged variables are additive sums of the two source
contributions, the \(\mathcal K\)-linear part is the sum of the two one-atom
\(\mathcal K\)-linear parts, with tags still attached.
\end{proof}

\begin{remark}[Scope of the tagged source block]
\label{rem:scope-tagged-source-block}
The definitions and lemma above are pre-whitening statements.  They do not
assert transfer-domain vanishing, quotient-output package coincidence,
diagonal merger, the coefficient \(B_7^{\mathfrak f}\), the quotient
\(Q_{7,m}^q\), the projector \(\Pi_{1,1}\), or the cubic
\((1,1,5)\) \(A_5^{\mathfrak f}\)-gauge theorem.  Those remain separate
UV-024 and UV-026 obligations.
\end{remark}
```
