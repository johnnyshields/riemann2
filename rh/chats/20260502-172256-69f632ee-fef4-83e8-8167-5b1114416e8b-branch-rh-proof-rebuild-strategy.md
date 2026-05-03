# Branch · RH Proof Rebuild Strategy

- Source: https://chatgpt.com/c/69f632ee-fef4-83e8-8167-5b1114416e8b
- Created: 2026-05-02 17:22:56 UTC
- Default model: gpt-5-5-pro

---

## User (2026-05-01 12:05:07)

I have a draft of a proof of the RH. It got very large and messy, and there are some major gaps, particularly in the hardy source-transfer work. As it exists currently the draft does not prove RH--I am well aware of that.

I would like to rebuild this paper cleanly, from scratch, starting from the jet-gram side, in a series of edits, and referee every step of the way so nothing is missed. I would like to strip out all no-gos/remarks/archived work that are not core to the active proof frontier (they can we retained in an older version file that we can refer to as needed.)

How do you recommend we attack this? Can you write a skeleton as a new latex file that we begin inserting into, verifying each step as we go? Or can you think of a better way to approach it?

## Assistant (2026-05-01 12:05:23)

I’ll treat this as a rebuild/referee workflow, using the existing draft only as source material. I’ll isolate the jet–Gram spine and create a lean LaTeX scaffold with explicit proof-status gates.

## User (2026-05-01 12:07:12)

We should treat the Hardy part as "extra energy from zeta" that MIGHT be needed to prove the two-point and four-point cases. But it also might not be. So we should leave that open in the structure

## Assistant (2026-05-01 12:07:25)

I found the draft’s useful live structure: a conditional finite-survival chain with explicit open inputs, while the historical no-go material should be excluded. Hardy/zeta transfer will be an optional energy module for the two- and four-point closures.

The skeleton will first record what the jet–Gram route proves unaided, then separately name any remaining two- or four-point energy deficit before invoking Hardy.

_Thought for 14m 12s_

I recommend **not patching the old draft directly**. Treat it as an archive/source mine and rebuild a clean proof file with strict status labels: core, optional, open, conditional, verified, archive.

I created a new LaTeX scaffold that does this.

Files:

- [Clean LaTeX skeleton](sandbox:/mnt/data/rh_jetgram_clean_skeleton.tex)
- [Compiled PDF preview](sandbox:/mnt/data/rh_jetgram_clean_skeleton.pdf)
- [Archived copy of the prior draft](sandbox:/mnt/data/proof_of_rh_archive_798.tex)

The skeleton keeps the Hardy material exactly as you specified: **Hardy/source-transfer is an optional energy-supply module**, not the mandatory upstream spine. The two-point and four-point sections each have two explicitly separated paths:

1. **Pure jet–Gram closure**: prove the needed estimate from local jet–Gram geometry alone.
2. **Hardy-assisted closure**: use extra zeta/Hardy energy only if the pure route does not close.

The main structural recommendation is:

### 1. Start with the jet–Gram side only

First lock down the local objects:

- phase kernel \(K_\Phi(x,y)\);
- point-to-jet transform \(P_h\);
- same-point jet–Gram block \(J(T)\);
- cross-block \(N_{12}\);
- finite symmetric blocks \(G_{m,\pm}(s)\), \(N_m(s)\);
- whitening conventions and Gram lower bounds.

The skeleton marks the same-point and cross-block formulas as **CORE + OPEN** because they should be re-proved cleanly, even if the formulas were already in the old draft.

### 2. Freeze the quotient before proving anything downstream

The biggest risk in this kind of reconstruction is quotient drift: choosing a transverse projection after seeing what needs to vanish. The skeleton therefore has a dedicated section:

```tex
\section{Jet--Gram invariants and quotient targets}
```

with an explicit open problem:

```tex
\begin{problem}[Choose the minimal invariant package]
...
\end{problem}
```

That should be solved before importing any toy anomaly or zeta suppression theorem.

### 3. Separate toy visibility from zeta suppression

The scaffold keeps these as distinct targets:

```tex
\begin{theorem}[Toy anomaly visibility]
...
\end{theorem}
```

and

```tex
\begin{hypothesis}[Actual-zeta transverse suppression]
...
\end{hypothesis}
```

This prevents the old draft’s architecture from silently merging “toy has a surviving mode” with “zeta has no such mode.”

### 4. Treat the two-point and four-point cases as independent closure targets

The skeleton has:

```tex
\section{Two-point closure target}
```

and

```tex
\section{Four-point closure target}
```

Each one has a pure local problem and a Hardy-assisted problem. This leaves open the possibility that Hardy energy is unnecessary.

### 5. Only then use Hardy/source-transfer, if needed

The Hardy section is placed downstream:

```tex
\section{Optional energy-supply module}
```

with this explicit rule:

> Its role is to provide optional extra energy from actual zeta data if the two-point or four-point closures cannot be proved purely locally.

That section currently contains abstract placeholders for:

- source-energy estimates;
- energy-to-jet–Gram transfer;
- Hardy-assisted source normalization.

### 6. Every inserted result gets a referee card

The skeleton includes a reusable audit format requiring:

- exact hypotheses;
- coordinate convention;
- gauge convention;
- whitening loss;
- energy use or no energy use;
- downstream citation;
- failure modes.

This is the main mechanism for preventing the new draft from becoming messy again.

The first concrete edit I would make next is to fill in the proof of the same-point jet–Gram limit,

\[
J(T)=\frac1\pi
\begin{pmatrix}
2q(T) & \frac12 q'(T)\\
\frac12 q'(T) & \frac1{12}(q''(T)+2q(T)^3)
\end{pmatrix},
\]

with all convention checks: whether the point pair is \(T\pm h\) or \(T\pm h/2\), whether \(P_h\) matches that convention, and where the \(\frac1{12}\) coefficient enters.
## User (2026-05-01 12:53:07)

See this draft, it has roughly the right structure, but it is too ELI5 and doesn't feel like a professional math paper. Re-do this into a more professionally labelled paper, referring to the original draft

## Assistant (2026-05-01 12:53:23)

I’ll rewrite the rebuild as a professional mathematical manuscript, using the old draft only as a source archive while preserving the open Hardy architecture and adding precise labels.

I’ve identified the main upgrade: keep the dependency graph, but replace tutorial prose and overclaiming theorem labels with a conditional/reduction structure and archive provenance.

_Thought for 18m 4s_

Done. I created a more professional rebuild as a new LaTeX file and compiled PDF:

- [Professional LaTeX rebuild](sandbox:/mnt/data/rh_rebuild_professional.tex)
- [Compiled PDF preview](sandbox:/mnt/data/rh_rebuild_professional.pdf)

Main changes:

1. **Retitled and reframed the paper**
   - Changed from an overclaiming “proof” style to a professional conditional program:
   ```tex
   A Jet--Gram Reconstruction of the Riemann Hypothesis Program
   ```
   - The abstract now states that all unresolved assertions are isolated as explicit open inputs.

2. **Replaced ELI5 section titles**
   - For example:
     - “What the toy off-line model sees” became  
       `Off-line toy model and transverse visibility`
     - “What actual zeta does instead” became  
       `Actual-zeta transverse suppression`
     - “Two zeros at once” became  
       `Two-point and four-point closure`

3. **Introduced a formal status system**
   - The informal `wip` mechanism is replaced by:
   ```tex
   \newtheorem{openinput}[theorem]{Open Input}
   ```
   - Unproved load-bearing assertions are now explicitly labelled as `Open Input`, not disguised as completed results.

4. **Made the Hardy material optional**
   - The Hardy/source-transfer section is now:
   ```tex
   \section{Optional Hardy source-energy module}
   ```
   - It is explicitly described as an auxiliary interface whose only permitted role is to prove the zeta-side suppression inputs for the two-point or four-point closures.

5. **Added a source concordance to the original draft**
   - Appendix A maps each new section to the relevant sections of `proof_of_rh(798).tex`.
   - Archived/no-go/route-history material is explicitly not migrated into the active proof line.

6. **Corrected a jet-normalization issue**
   - The prior rebuild used
   ```tex
   P_h = \frac12
   \begin{pmatrix}
   1 & 1\\
   -1/h & 1/h
   \end{pmatrix},
   ```
   but that normalization does not match the displayed same-point block with leading entry \(2q/\pi\).
   - I changed it to the orthonormal value/derivative normalization:
   ```tex
   P_h
   =
   \frac1{\sqrt2}
   \begin{pmatrix}
   1 & 1\\
   -1/(2h) & 1/(2h)
   \end{pmatrix}.
   ```
   This is now flagged in a normalization-audit remark.

7. **Compiled and rendered the PDF**
   - The file compiles cleanly with resolved cross-references.
   - I rendered the PDF and spot-checked the layout.
## User (2026-05-01 15:55:17)

Corrected a jet-normalization issue --> regarding this, what does the existing paper use? what is most natural to use?

## Assistant (2026-05-01 15:55:38)

I’ll compare the original, rebuild, and displayed jet–Gram formula to distinguish the manuscript’s actual \(P_h\) convention from the cleanest normalization for the new paper.

I found a substantive convention mismatch: the archive uses the average/difference \(P_h\), while the displayed \(J(T)\) has coefficients corresponding to another scaling.

_Thought for 5m 52s_

The existing paper is not using one clean convention. It has a normalization mismatch.

In the old archive, the printed point-to-jet matrix is

\[
P_h^{\mathrm{old}}
=
\frac12
\begin{pmatrix}
1&1\\
-1/h&1/h
\end{pmatrix},
\]

and immediately afterward the paper states the jet-limit block

\[
J(T)
=
\frac1\pi
\begin{pmatrix}
2q(T)&\frac12q'(T)\\
\frac12q'(T)&\frac1{12}(q''(T)+2q(T)^3)
\end{pmatrix}.
\]

That is also what the current `rh_rebuild.tex` draft repeats: it uses \(T\pm h\), the same \(P_h^{\mathrm{old}}\), and the same displayed \(J(T)\). See `rh_rebuild.tex`, lines 277–287 and 312–326; and `proof_of_rh_archive_798.tex`, lines 803–827.

But those two choices do **not** match if \(A_h\) is the ordinary raw kernel matrix

\[
A_h=\bigl(K_\Phi(T+\epsilon_i h,T+\epsilon_j h)\bigr)_{\epsilon_i,\epsilon_j\in\{-1,1\}}.
\]

With the printed old matrix and the pair \(T\pm h\), one gets the literal central value/derivative jet block

\[
P_h^{\mathrm{old}}A_h(P_h^{\mathrm{old}})^\top
\longrightarrow
\begin{pmatrix}
K(T,T)&K_y(T,T)\\
K_x(T,T)&K_{xy}(T,T)
\end{pmatrix}.
\]

For the phase kernel this is

\[
\frac1\pi
\begin{pmatrix}
q(T)&\frac12q'(T)\\[1ex]
\frac12q'(T)&\frac16\bigl(q''(T)+2q(T)^3\bigr)
\end{pmatrix}.
\]

That is **not** the displayed block in the paper.

The displayed block

\[
\begin{pmatrix}
2K(T,T)&K_y(T,T)\\
K_x(T,T)&\frac12K_{xy}(T,T)
\end{pmatrix}
\]

is obtained instead by using

\[
P_h^{\mathrm{Gram}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\[0.6ex]
-1/(2h)&1/(2h)
\end{pmatrix}
\]

for the pair \(T-h,T+h\). This is the normalization I inserted into the professional rebuild.

So the precise diagnosis is:

\[
\boxed{
\text{The existing paper prints }P_h^{\mathrm{old}},\text{ but its displayed }J(T)
\text{ belongs to }P_h^{\mathrm{Gram}}.
}
\]

I would not describe this as merely a typo in \(P_h\) or merely a typo in \(J(T)\). It is a convention collision.

The cleanest choice depends on what you want the jet coordinates to mean.

If you want literal Taylor jet coordinates, use

\[
P_h^{\mathrm{jet}}
=
\begin{pmatrix}
1/2&1/2\\[0.6ex]
-1/(2h)&1/(2h)
\end{pmatrix}.
\]

Then the same-point limit is

\[
J_{\mathrm{jet}}(T)
=
\frac1\pi
\begin{pmatrix}
q(T)&\frac12q'(T)\\[1ex]
\frac12q'(T)&\frac16(q''(T)+2q(T)^3)
\end{pmatrix}.
\]

This is conceptually natural if the coordinates are literally

\[
(f(T),f'(T)).
\]

But it does **not** match the existing displayed \(J(T)\), nor the existing cross-block formulas with \(2K\) and \(\frac12K_{xy}\).

If you want a Gram/whitening normalization, use

\[
P_h^{\mathrm{Gram}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\[0.6ex]
-1/(2h)&1/(2h)
\end{pmatrix}.
\]

Then

\[
P_h^{\mathrm{Gram}}A_h(P_h^{\mathrm{Gram}})^\top
\longrightarrow
\frac1\pi
\begin{pmatrix}
2q(T)&\frac12q'(T)\\[1ex]
\frac12q'(T)&\frac1{12}(q''(T)+2q(T)^3)
\end{pmatrix},
\]

which is exactly the block already used downstream.

My recommendation: **keep the displayed \(J(T)\), but explicitly change the transform to \(P_h^{\mathrm{Gram}}\)** and call it the **Gram-normalized coalescing even/odd basis**, not the literal value/derivative basis.

The wording in the rebuild should probably be revised from “orthonormal value/derivative normalization” to something sharper:

```tex
For the symmetric pair \(T-h,T+h\), we use the Gram-normalized
coalescing even/odd transform
\[
P_h^{\mathrm{G}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\[0.6ex]
-1/(2h)&1/(2h)
\end{pmatrix}.
\]
Equivalently, this is obtained from the literal central value/derivative
jet transform by the fixed diagonal congruence
\[
P_h^{\mathrm{G}}
=
\operatorname{diag}(\sqrt2,1/\sqrt2)\,
\begin{pmatrix}
1/2&1/2\\[0.6ex]
-1/(2h)&1/(2h)
\end{pmatrix}.
\]
This convention gives
\[
J(T)=
\begin{pmatrix}
2K(T,T)&K_y(T,T)\\
K_x(T,T)&\frac12K_{xy}(T,T)
\end{pmatrix},
\]
and hence the displayed phase-kernel formula.
```

That is the convention I think is most natural for this paper because the downstream object is not a raw Taylor jet; it is a **whitened Gram block**. Normalizing the even and odd point modes first is the cleaner Hilbert-space convention. The literal jet convention is also valid, but then all same-point blocks, cross-blocks, quotient covectors, and finite-\(s\) formulas must be rescaled consistently.
## User (2026-05-01 17:11:40)

OK. See finalized rh_rebuild doc attached. I've also attached a latex patch to migrate section 3 into this draft.

Please audit this patch as a referee for completeness. Focus specifically on this patch, don't worry about other unproved claims in the draft.

FYI Note:

  Sympy results:
  - P_h A_h(T) P_h^T → J(T) — verified entry-by-entry, diff = 0
  - P_h C_h(T_1,T_2) P_h^T → (1/π) N_{12} — verified entry-by-entry, diff = 0
  - Trace = (2q³ + 24q + q'')/(12π), det = (4q⁴ + 2qq'' − 3q'²)/(12π²) — match the proof identities exactly; asymptotic det/Tr
   ∼ 2q/π → ∞

  Simulation results (mpmath, dps=30):
  - J(T) ≻ 0 at every tested height in {10³, 10⁴, 10⁵, 10⁶, 10⁷}
  - λ_min(J(T)) ∼ T^{0.165} — empirically grows with T (positive power, consistent with q ∼ log T); the constant C_J in λ_min
  ≥ Q^{-C_J} is effectively zero or negative across the tested range
  - Direct numerical conjugation P_h A_h P_h^T → J(T): error decreases as O(h²) from h=10⁻² down to 10⁻⁴ before float64
  precision saturates around h=10⁻⁵
  - Same convergence rate for the cross-block

(Also attached is the original paper.)

Please critique the patch, and give a revised patch if you want to change anything, or if anything is missing/unclear/non-referee safe.

## Assistant (2026-05-01 17:11:57)

I’ll audit only the Section 3 migration patch against the finalized rebuild and original source, checking mathematical content, notation compatibility, LaTeX integration, and referee safety.

The jet-limit identities and Gram-normalized \(P_h\) are checking out; the main problem is the same-point positivity lemma, which needs a stronger margin assumption or safer replacement.
## User (2026-05-01 17:15:26)

don't worry about running the python, just treat it as for reference

## Assistant (2026-05-01 17:15:39)

I’ll treat the Python outputs only as corroborating notes, not as part of the audited proof; the LaTeX must stand on definitions, hypotheses, and logic.

I’ll revise only that point: keep the limit lemmas as proved identities, and replace positivity with an algebraic criterion plus a separate retained-packet dominance input.

_Thought for 16m 12s_

Referee verdict: **the Taylor-limit part is acceptable; the Gram-positivity closure is not yet referee-safe as written.** I revised the patch accordingly.

Files:

- [Revised Section 3 patch, referee-safe v2](sandbox:/mnt/data/sec-jet-limit-local-blocks.referee-revised-v2.tex)
- [Integrated rebuild with revised Section 3](sandbox:/mnt/data/rh_rebuild_sec3_referee_patched_v2.tex)
- [LaTeX draft-mode compile log](sandbox:/mnt/data/rh_rebuild_sec3_referee_patched_v2.compile.log)

I treated the Python files and your reported results as reference only, per your instruction. I did not run the Python. I did run a LaTeX draft-mode compile of the integrated file; it completed. The remaining warnings are unresolved references elsewhere in the rebuild, not Section 3 syntax failures.

## Main audit result

The patch correctly fixes the **jet-limit identities** in the Gram-normalized convention:

\[
P_h=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1/(2h)&1/(2h)
\end{pmatrix}.
\]

The submitted symbolic script uses exactly this convention and checks

\[
P_hA_h(T)P_h^\top\to J(T),
\qquad
P_hC_h(T_1,T_2)P_h^\top\to (1/\pi)N_{12},
\]

which matches the current rebuild normalization. turn4file13

The part I would **not** let through as a referee is the submitted proof of same-point Gram positivity. The algebraic trace and determinant identities are correct,

\[
\operatorname{Tr} J(T)
=
\frac{2q(T)^3+24q(T)+q''(T)}{12\pi},
\]

\[
\det J(T)
=
\frac{4q(T)^4+2q(T)q''(T)-3q'(T)^2}{12\pi^2},
\]

and those are also the identities checked in the symbolic verification script. 

But the submitted argument then says, in effect, that from

\[
q\ge Q^{-c_q},\qquad |q'|,|q''|\le Q^{C_d},
\]

the \(q^3\) term dominates the trace and the \(4q^4\) term dominates the determinant. That does **not** follow. Those assumptions allow, for example, \(q=Q^{-1}\), \(q'=1\), \(q''=0\), in which case

\[
4q^4+2qq''-3q'^2<0.
\]

So the original Gram-positivity proof proves the right thing only under stronger asymptotic information than the current draft has actually stated.

## What I changed

I replaced the Gram-positivity proof with a referee-safe split:

1. **Formal Taylor identities**  
   The same-point and cross-block limits are proved directly.

2. **Algebraic Gram criterion**  
   Define

   \[
   D_J(T):=4q(T)^4+2q(T)q''(T)-3q'(T)^2.
   \]

   Then

   \[
   J(T)\succ0
   \quad\Longleftrightarrow\quad
   q(T)>0\ \text{and}\ D_J(T)>0.
   \]

3. **Explicit retained-packet hypothesis**  
   I introduced:

   ```tex
   \begin{hypothesis}[Same-point Gram regularity on retained packets]
   ...
   D_J(T)\ge Q^{-C_D}.
   \end{hypothesis}
   ```

4. **Conditional positivity lemma**  
   The downstream label

   ```tex
   \label{lem:same-point-gram-positivity}
   ```

   is preserved, but the lemma now reads:

   \[
   \text{Hypothesis~\ref{hyp:same-point-gram-regularity}}
   \Longrightarrow
   J(T)\succ0,\qquad
   \lambda_{\min}(J(T))\ge Q^{-C_J}.
   \]

This keeps the downstream draft structurally stable while preventing the paper from silently closing an unproved positivity input.

## Smaller referee edits

I also made the row/column conventions explicit.

For the same-point block:

\[
A_h(T)=
\begin{pmatrix}
K_\Phi(T-h,T-h)&K_\Phi(T-h,T+h)\\
K_\Phi(T+h,T-h)&K_\Phi(T+h,T+h)
\end{pmatrix},
\]

with row and column order \((T-h,T+h)\).

For the cross-block:

\[
C_h(T_1,T_2)=
\begin{pmatrix}
K_\Phi(T_1-h,T_2-h)&K_\Phi(T_1-h,T_2+h)\\
K_\Phi(T_1+h,T_2-h)&K_\Phi(T_1+h,T_2+h)
\end{pmatrix}.
\]

This removes the sign ambiguity in the \((1,2)\) and \((2,1)\) entries of \(N_{12}\).

## Referee-safe status

I would mark the section as:

```tex
\statuspaper{LIVE}
\statusmig{migrated}
\statusreferee{in-progress}
\statussympy{verified}
\statussim{partial}
\statuslean{not-started}
```

Reason:

- The **same-point jet limit** passes.
- The **cross-block jet limit** passes.
- The **trace/determinant algebra** passes.
- The **Gram lower bound** is not proved by the submitted assumptions and should remain an explicit retained-packet input.
- The numerical checks are useful sanity checks, especially for signs and normalization, but they should not be cited as proof of same-point Gram regularity. The numerical script itself is framed as a simulation against selected zeta data and convergence tests. 

## One possible future closure

If the phase in this section is ultimately specialized to the pure Riemann--Siegel theta phase, then the Gram-regularity hypothesis should be replaceable by a direct asymptotic lemma using

\[
q(T)\sim \tfrac12\log(T/2\pi),
\qquad
q'(T)=O(T^{-1}),
\qquad
q''(T)=O(T^{-2}).
\]

Then

\[
D_J(T)=4q(T)^4+o(q(T)^4),
\]

and the determinant lower bound is immediate for high \(T\). But that is a separate zeta-phase asymptotic lemma; it is not contained in the current P1--P2 formulation.
## User (2026-05-02 07:45:25)

Review and referee this patch rigorously. It now covers both sections 2 and 3

## Assistant (2026-05-02 07:45:40)

I’ll audit Sections 2–3 as a local patch, treating Python only as support, and check normalization, dependencies, labels, and whether claims exceed stated hypotheses.

Initial integration checks show the patch compiles in draft mode, but its optional-argument status macros are not merge-safe and need removal or macro redesign.
## User (2026-05-02 07:49:03)

don't worry about the status macros

## Assistant (2026-05-02 07:49:15)

Understood; I’ll set aside the status macro issue and focus only on mathematical content and integration safety.

## User (2026-05-02 07:49:32)

focus as a referee on the paper content. is everything rigorous? if not, give a revised patch

## Assistant (2026-05-02 07:50:16)

One substantive issue is emerging: some \(\theta\)-asymptotic claims rely on differentiating a big-O expansion without explicitly invoking a differentiated Stirling formula.

The jet-limit formulas look improved, but I’m also checking phase-chart assumptions, positivity claims, and the determinant normalization for referee-safe consistency.

The remaining gap is localized: I’m revising the patch so theta-specific asymptotics and positivity are stated explicitly, while preserving the sound Taylor-block material.

_Thought for 25m 11s_

Referee verdict: **not quite rigorous as submitted**, but the defects are local and repairable. I revised the patch.

Files:

- [Revised Sections 2–3 patch](sandbox:/mnt/data/jet-gram-foundation.referee-revised.tex)
- [Integrated rebuild with revised Sections 2–3](sandbox:/mnt/data/rh_rebuild_sections23_referee_revised.tex)
- [Compiled PDF preview](sandbox:/mnt/data/rh_rebuild_sections23_referee_revised.pdf)
- [Final compile log](sandbox:/mnt/data/rh_rebuild_sections23_referee_revised.compile3.log)

The integrated file compiles. The remaining compile notes are only minor overfull boxes elsewhere/status-line formatting; there are no unresolved references or Section 2–3 LaTeX failures.

## Referee assessment

The **core jet-limit formulas are correct** in the Gram-normalized convention. The symbolic reference script uses

\[
P_h=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1/(2h)&1/(2h)
\end{pmatrix},
\]

and verifies both

\[
P_hA_h(T)P_h^\top\to J(T)
\]

and

\[
P_hC_h(T_1,T_2)P_h^\top\to \frac1\pi N_{12}.
\]

That matches the current normalization. 

The original draft had the right displayed \(J(T)\)-shape but did not give enough normalization control; it also recorded a determinant coefficient inconsistent with the Gram-normalized block, giving \(1/(24\pi^2)\) where the correct determinant for the displayed \(J(T)\) is

\[
\det J(T)=
\frac{4q(T)^4+2q(T)q''(T)-3q'(T)^2}{12\pi^2}.
\]

The symbolic reference script confirms the \(1/(12\pi^2)\) coefficient.  

## Main issues I corrected

1. **The theta phase needed a precise definition.**  
   I replaced the informal phase discussion with

   \[
   \theta(t)=
   \Im\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
   -\frac t2\log\pi,
   \]

   with a continuous branch convention. This makes the phase chart a genuine mathematical object, not an implicit appeal to the functional equation.

2. **The derivative estimates needed to be uniform on \(I_T\).**  
   The submitted patch used theta asymptotics, but the window uniformity was not fully nailed down. The revised patch assumes

   \[
   I_T\subset [T/2,2T],
   \qquad |I_T|\ll Q(T)^{-1},
   \]

   and proves, uniformly on \(I_T\),

   \[
   q(t)=\frac12\log\frac{t}{2\pi}-\frac{1}{48t^2}+O(t^{-4}),
   \]

   \[
   q'(t)=\frac{1}{2t}+O(t^{-3}),
   \qquad
   q''(t)=-\frac{1}{2t^2}+O(t^{-4}).
   \]

3. **The diagonal kernel derivatives needed their own lemma.**  
   I separated the removable singularity computation from the off-diagonal derivative formulas. The revised patch proves

   \[
   K_\Phi(T,T)=\frac{q(T)}{\pi},
   \qquad
   K_x(T,T)=K_y(T,T)=\frac{q'(T)}{2\pi},
   \]

   \[
   K_{xy}(T,T)=\frac{q''(T)+2q(T)^3}{6\pi}.
   \]

4. **The cross-block \(O(h^2)\) claim needed a fourth-order parity argument.**  
   The submitted proof used only a second-order bivariate Taylor expansion but concluded \(O(h^2)\). That does not follow from the displayed expansion alone, because the \((2,2)\) entry is divided by \(h^2\). I revised the proof to expand to total order four and explicitly use the four sign weights

   \[
   1,\quad \sigma_2,\quad \sigma_1,\quad \sigma_1\sigma_2.
   \]

   This makes the \(O(h^2)\) rate referee-safe.

5. **The same-point positivity theorem needed to be explicitly theta-specific.**  
   The revised patch separates:

   \[
   D_J(T)=4q(T)^4+2q(T)q''(T)-3q'(T)^2
   \]

   and the algebraic criterion

   \[
   J(T)\succ0
   \Longleftrightarrow
   q(T)>0 \text{ and } D_J(T)>0.
   \]

   Then, only for \(\Phi_T=\theta\), it proves

   \[
   D_J(T)=4q(T)^4(1+o(1))>0
   \]

   and

   \[
   \lambda_{\min}(J(T))
   =
   \frac{2q(T)}{\pi}(1+o(1))
   =
   \frac1\pi\log\frac{T}{2\pi}(1+o(1)).
   \]

6. **I added a scope guardrail.**  
   The revised patch states explicitly that same-point Gram positivity for theta does **not** prove unrelated anisotropy lower bounds such as

   \[
   |q''-6q+2q^3|\ge Q^{-A},
   \]

   and does **not** supply Hardy/source-transfer information. That prevents later sections from citing this lemma for more than it proves.

## Final referee status

I would now mark Sections 2–3 as acceptable for the active rebuild, with this scope:

- **proved:** theta phase chart, phase-kernel identities, same-point jet limit, cross-block jet limit, algebraic Gram criterion;
- **proved for theta:** same-point positive definiteness and polynomial spectral lower bound;
- **not proved here:** any actual-zeta transverse suppression, Hardy energy transfer, or Gram-anisotropy/non-isotropy lower bound beyond \(J(T)\succ0\).
## User (2026-05-02 08:25:55)

Going forward, avoid explicit usage "Hardy" in this new draft and simply say "source-energy" or "source-energy transfer". We want to stay generic as we don't actually know that Hardy will be used.

## Assistant (2026-05-02 08:26:51)

_Thought for 49s_

Understood. Going forward, I’ll use:

- **source-energy**
- **source-energy transfer**
- **source-energy module**
- **zeta-side source energy**
- **auxiliary source-energy input**

and avoid naming a specific mechanism unless the paper later proves that this is the mechanism actually being used.

For the draft structure, I would relabel the optional module as something like:

```tex
\section{Optional source-energy transfer}
```

or, more formally,

```tex
\section{Auxiliary source-energy transfer}
```

The intended meaning will be:

> This section provides an abstract interface for importing additional zeta-side energy estimates into the jet--Gram closure argument, without committing to any particular analytic source of that energy.

I’ll also avoid using the older terminology in theorem names, labels, remarks, and status comments.
## User (2026-05-02 08:29:00)

check the latest version of the patch one more time, as a referee. If anything more to change, give me your hardened revised patch.

## Assistant (2026-05-02 08:29:16)

I’ll audit the latest Sections 2–3 patch strictly as mathematics, ignoring status macros and checking normalization, hypotheses, limits, asymptotics, positivity, and downstream citation safety.

The latest patch is cleaner, but I see one substantive issue: the final eigenvalue asymptotic appears overstated, though positivity itself should be salvageable.
## User (2026-05-02 08:47:44)

don't worry about status macros

## Assistant (2026-05-02 08:52:19)

I found no coefficient or sign failure. Remaining hardening is limited to branch conventions, uniformity, error-constant scope, and making positivity uniform on \(I_T\).

_Thought for 36m 21s_

Referee verdict: **the patch is very close, but I would still harden it before treating Sections 2–3 as closed.** I made a revised version.

Files:

- [Hardened Sections 2–3 patch](sandbox:/mnt/data/jet-gram-foundation.hardened.tex)
- [Diff against your latest patch](sandbox:/mnt/data/jet-gram-foundation.hardened.diff)
- [Integrated draft with hardened Sections 2–3](sandbox:/mnt/data/rh_rebuild_sections23_hardened.tex)
- [Compiled PDF preview](sandbox:/mnt/data/rh_rebuild_sections23_hardened.pdf)
- [Final compile log](sandbox:/mnt/data/rh_rebuild_sections23_hardened.compile_final.log)

I did **not** run the Python scripts.

The mathematical content is now referee-safe for its intended scope. The formulas for \(J(T)\), \(N_{12}\), \(\operatorname{Tr}J\), \(\det J\), and the theta-specific positivity argument are sound.

The main thing I changed is the proof of the diagonal derivative identities. The submitted proof wrote

\[
\Phi(T+u)-\Phi(T+v)
=
q(u-v)+\frac{q'}2(u^2-v^2)+\frac{q''}{6}(u^3-v^3)+O(|(u,v)|^4)
\]

and then divided by \(u-v\). That is not fully referee-safe near the diagonal, because an unfactored \(O(|(u,v)|^4)\) remainder cannot simply be divided by \(u-v\) uniformly as \(u\to v\). The revised proof factors first:

\[
\Phi(T+u)-\Phi(T+v)=(u-v)A(u,v),
\]

with

\[
A(u,v)=\int_0^1 q(T+v+\tau(u-v))\,d\tau.
\]

Then

\[
A(u,v)
=
q+\frac{q'}2(u+v)+\frac{q''}{6}(u^2+uv+v^2)+O(r^3),
\qquad r=|u|+|v|.
\]

This makes the diagonal expansion legitimate and preserves the same coefficients:

\[
K_x(T,T)=K_y(T,T)=\frac{q'(T)}{2\pi},
\qquad
K_{xy}(T,T)=\frac{q''(T)+2q(T)^3}{6\pi}.
\]

I also hardened the Riemann–Siegel phase definition by introducing the holomorphic branch \(L(z)=\log\Gamma z\) on \(\Re z>0\), rather than leaving the branch convention informal.

Other changes are local:

- made the differentiated Stirling argument explicitly uniform on \(I_T\);
- stated that the \(O(h^2)\) jet-limit errors are entrywise;
- recorded the dependence of the cross-block error constant on \(|T_1-T_2|^{-1}\);
- displayed the Taylor expansion of \(q(T\pm h)\) used in the same-point proof;
- explicitly used \(h<|s|/3\) in the cross-block proof to keep the sampled rectangle away from the diagonal;
- kept all terminology generic: **source-energy**, not the older mechanism-specific wording.

The integrated file compiles. The only remaining overfull boxes are status-line/path formatting, which you told me not to worry about.
## User (2026-05-02 09:17:00)

check this revised patch. did it capture everything?

## Assistant (2026-05-02 09:17:16)

I’ll do a content-only referee audit against the hardened criteria: definitions, normalization, diagonal and cross-block limits, theta-specific positivity, proof dependencies, terminology, and scope.

The revised patch appears to capture the main hardening fixes. I’m now checking residual risks around differentiated theta asymptotics, cross-block neighborhood control, and overstrong conclusions.
## User (2026-05-02 09:35:34)

don't overly worry about latex compilation, focus on refereeing the content. another agent will take care of the final latex aspects

## Assistant (2026-05-02 09:40:59)

_Thought for 23m 57s_

Referee verdict: **the revised patch captured the substantive mathematical corrections, but I would still make a final hardening pass before calling Sections 2–3 referee-safe.** The remaining issues are small, local, and mostly about preventing later misuse.

Files:

- [Hardened final Sections 2–3 patch](sandbox:/mnt/data/jet-gram-foundation.hardened-final3.tex)
- [Diff against your latest patch](sandbox:/mnt/data/jet-gram-foundation.hardened-final3.diff)
- [Integrated draft with hardened Sections 2–3 and generic source-energy wording](sandbox:/mnt/data/rh_rebuild_sections23_hardened_final3_sourceenergy.tex)
- [PDF preview](sandbox:/mnt/data/rh_rebuild_sections23_hardened_final3_sourceenergy.pdf)

I treated the symbolic and numerical scripts as reference only. The symbolic script uses the same Gram-normalized transform and checks the same-point limit, cross-block limit, and trace/determinant identities; the numerical script is sanity-check evidence only, not part of the proof.  

## What the latest patch did capture

Mathematically, it now has the main required pieces:

1. A precise Riemann–Siegel phase definition via a holomorphic branch of \(\log\Gamma z\) on \(\Re z>0\).

2. Uniform theta derivative asymptotics on \(I_T\):

\[
q(t)=\frac12\log\frac{t}{2\pi}-\frac{1}{48t^2}+O(t^{-4}),
\]

\[
q'(t)=\frac{1}{2t}+O(t^{-3}),
\qquad
q''(t)=-\frac{1}{2t^2}+O(t^{-4}).
\]

3. The correct Gram-normalized point-to-jet transform:

\[
P_h=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1/(2h)&1/(2h)
\end{pmatrix}.
\]

4. The correct same-point limit:

\[
P_h A_h(T)P_h^\top
=
J(T)+O(h^2),
\]

with

\[
J(T)=
\frac1\pi
\begin{pmatrix}
2q(T)&\frac12q'(T)\\[0.7ex]
\frac12q'(T)&\frac1{12}(q''(T)+2q(T)^3)
\end{pmatrix}.
\]

5. The correct off-diagonal two-center limit:

\[
P_h C_h(T_1,T_2)P_h^\top
=
\frac1\pi N_{12}(T_1,T_2)+O(h^2).
\]

6. The correct determinant identity:

\[
\det J(T)=
\frac{4q(T)^4+2q(T)q''(T)-3q'(T)^2}{12\pi^2}.
\]

7. A theta-specific proof that \(J(T)\succ0\) for high retained \(T\), with

\[
\lambda_{\min}(J(T))
=
\frac{2q(T)}{\pi}(1+o(1)).
\]

So yes: the latest patch captured the main proof content.

## What I still changed

I made five final referee-hardening edits.

First, the theta-asymptotic proof said the displayed remainder was differentiable twice. But the section uses \(q''=\theta'''\), so the theta expansion needs three differentiated remainders. I changed this to:

```tex
again with the displayed remainder admitting three differentiations with
the corresponding differentiated bounds.
```

Second, I restored the statement that the local phase chart is a **specialized theta chart**, not a general phase-chart axiom. This matters because the positivity proof uses theta asymptotics, not just an abstract \(q\)-lower bound.

Third, I made the diagonal kernel proof more explicit at the removable singularity. The expansion

\[
\frac{\sin(\Phi(T+u)-\Phi(T+v))}{u-v}
\]

is first justified for \(u\ne v\), then extended to \(u=v\) by continuity. This prevents a referee from objecting that the displayed quotient is being manipulated directly on the diagonal.

Fourth, I changed the point-to-jet wording from “fixed diagonal congruence” to “fixed diagonal rescaling; at the level of Gram blocks this induces the corresponding diagonal congruence.” That is more precise: \(P_h\) is a coordinate transform, while the Gram matrix changes by congruence.

Fifth, I hardened the cross-block lemma. The latest patch had the right fixed-separation proof, but I made explicit that:

\[
0<h<|s|/3
\]

is accompanied by \(h\) being small enough that all sampled points stay inside the chosen neighborhoods of \(T_1\) and \(T_2\). I also changed the error dependence from “depends on \(|s|^{-1}\)” to “depends on a finite power of \(|s|^{-1}\),” because higher off-diagonal derivatives of the kernel can produce higher powers of \(1/s\).

I also restored this guardrail:

```tex
\begin{remark}[Fixed-separation scope]
Lemma~\ref{lem:cross-block-jet-limit} is an off-diagonal jet limit at
fixed separation. It is not a collision expansion for \(T_1\to T_2\);
any two-center blow-up or near-coalescence analysis must be derived from
a separate scaling argument.
\end{remark}
```

That remark is important. Without it, a later section might accidentally cite the cross-block \(O(h^2)\) expansion in a regime where \(s=T_1-T_2\) is also varying or shrinking.

## Referee conclusion

With the hardening edits, I would mark Sections 2–3 as **mathematically acceptable for the active draft**, with the following scope:

- proved: theta phase chart and derivative bounds;
- proved: phase-kernel diagonal derivative identities;
- proved: Gram-normalized same-point jet limit;
- proved: fixed-separation cross-block jet limit;
- proved: trace/determinant identities for \(J(T)\);
- proved for theta: same-point positivity and spectral asymptotic;
- not proved here: any finite-scale whitening theorem, transverse suppression, source-energy transfer, near-collision block asymptotics, or higher-point closure.

The latest patch was already close. The hardened version mainly prevents scope creep and makes the derivative/remainder bookkeeping referee-safe.
## User (2026-05-02 16:31:15)

The previous patch has now been merged. Now, referee this new patch for section 4

## Assistant (2026-05-02 16:31:32)

I’ll referee Section 4 in isolation against the merged Sections 2–3, checking definitions, dependencies, normalization, whitening claims, and downstream citability.

The finite block signs look consistent with the Section 3 convention, so the likely issues are regularity, finite-\(s\) uniformity, and the claimed \(C_W=0\) whitening loss.

_Thought for 10m 50s_

Referee verdict: **the Section 4 patch has the right formulas, but I would not merge it unchanged.** The remaining problems are local proof-hardening issues, not structural failures.

I produced a hardened replacement patch:

- [Hardened Section 4 patch](sandbox:/mnt/data/sec-finite-scale-local-blocks-and-whitening.hardened.tex)
- [Diff against your submitted Section 4 patch](sandbox:/mnt/data/sec-finite-scale-local-blocks-and-whitening.hardened.diff)
- [Integrated draft with hardened Section 4](sandbox:/mnt/data/rh_rebuild_section4_hardened.tex)

I did not run the symbolic/numerical scripts, and I did not focus on LaTeX compilation.

## Main referee findings

The displayed formulas for

\[
G_{m,\pm}(s)
\]

and

\[
N_m(s)
\]

are correct. In particular, the sign conversion from Section 3 is right:

\[
T_1=t_- ,\qquad T_2=t_+,\qquad s_{12}=T_1-T_2=-s.
\]

Thus

\[
N_m(s)=\pi^{-1}N_{12}(t_-,t_+)
\]

with the signs in your displayed \(N_m(s)\).

The patch’s proof of the removable singularity, however, had a sign error in the Taylor line for \(q_\pm\). It wrote, effectively,

\[
q_\pm=q(m)\mp \frac{s}{2}q'(m)+O(s^2),
\]

but with \(t_\pm=m\pm s/2\), the correct expansion is

\[
q_+=q(m)+\frac{s}{2}q'(m)+\frac{s^2}{8}q''(m)+o(s^2),
\]

\[
q_-=q(m)-\frac{s}{2}q'(m)+\frac{s^2}{8}q''(m)+o(s^2).
\]

The final limits in the submitted patch were consistent with the correct signs, but the proof line itself was wrong. I fixed this.

## Other hardening changes

I added a finite packet domain

\[
\mathcal D_T
=
\{(m,s):m-s/2\in I_T,\ m+s/2\in I_T\},
\]

with signed \(s\). Applications can still use \(s>0\), but allowing signed \(s\) makes the \(s\to0\) removable-singularity statement precise.

I promoted the “connection to Section 3” from a remark to a lemma:

\[
G_{m,\pm}(s)=J(t_\pm),
\]

and

\[
N_m(s)=
\begin{pmatrix}
2K_\Phi(t_-,t_+) & \partial_yK_\Phi(t_-,t_+)\\
\partial_xK_\Phi(t_-,t_+) & \frac12\partial_{xy}K_\Phi(t_-,t_+)
\end{pmatrix}.
\]

That makes the finite block interpretation formally citeable downstream.

I rewrote the removable-singularity proof using little-\(o\) Taylor expansions instead of an unjustified \(O(s^5)\) remainder. The strengthened proof uses

\[
\Delta_m(s)
=
-qs-\frac{q''}{24}s^3+o(s^3),
\]

\[
q_+
=
q+\frac{s}{2}q'+\frac{s^2}{8}q''+o(s^2),
\qquad
q_-
=
q-\frac{s}{2}q'+\frac{s^2}{8}q''+o(s^2),
\]

and then obtains

\[
N_m(0)=J(m)
\]

entry by entry.

I added a guardrail remark clarifying that the \(s\to0\) coalescence of \(N_m(s)\) is **not** obtained by applying the Section 3 cross-block jet limit uniformly as \(s\to0\). It is a separate Taylor computation in the center-separation parameter.

I also hardened the whitening proof. The submitted argument used the Section 3 lower bound, but the uniformity over \((m,s)\) needed to be stated more cleanly. The revised proof explicitly uses

\[
t_\pm\in I_T\subset[T/2,2T],
\]

so the theta asymptotics are uniform at both endpoints. It then proves uniformly on \(\mathcal D_T\) that

\[
\lambda_{\min}(G_{m,\pm}(s))
=
\frac{2q(t_\pm)}{\pi}(1+o(1)),
\]

and hence

\[
\bigl\|G_{m,\pm}(s)^{-1/2}\bigr\|_{\mathrm{op}}
\le
\sqrt{\frac{\pi}{2q(t_\pm)}}(1+\varepsilon_T),
\qquad
\varepsilon_T\to0.
\]

Finally, I made the \(C_W=0\) conclusion depend explicitly on the enlarged lower-height cutoff:

\[
\lambda_{\min}(J(t))\to\infty
\]

uniformly for \(t\in I_T\), so after raising the cutoff,

\[
\|G_{m,\pm}(s)^{-1/2}\|_{\mathrm{op}}\le1\le Q(T)^0.
\]

## Scope after hardening

I would now regard Section 4 as referee-safe for the following claims:

- exact finite-center same-point blocks \(G_{m,\pm}=J(t_\pm)\);
- exact finite-center mixed block \(N_m(s)\);
- correct sign conversion from Section 3;
- continuous removable singularity \(N_m(0)=J(m)\);
- coalescence normalization \(\widehat\Omega_\zeta(0;m)=I_2\);
- uniform real-axis whitening loss for theta-phase retained packets.

It still does **not** prove any actual-zeta transverse suppression, source-energy transfer, complex-\(s\) whitening, holomorphic disk bounds, or a uniform bound on \(\widehat\Omega_\zeta(s;m)\) itself beyond the whitening-factor loss. If a later comparison theorem needs one of those stronger statements, it should be stated separately.
## User (2026-05-02 17:22:54)

are we essentially doing proofs of phase cancellations of the riemann-siegel function? have similar proofs been tried before?

## Assistant (2026-05-02 17:23:21)

I’ll separate what Sections 2–4 actually prove from the larger strategy, then compare that local phase/kernel work with historically adjacent RH approaches.

_Thought for 4m 14s_

Yes, but with an important qualification.

What we are currently proving is **not yet cancellation of the Riemann–Siegel \(Z(t)\)-function itself**. In Sections 2–4, we are proving **local phase-kernel cancellations** for the Riemann–Siegel phase \(\theta(t)\), especially the cancellations caused by symmetric coalescence and the Gram-normalized even/odd basis.

Concretely, the current local package proves cancellations of the form

\[
P_h A_h(T)P_h^\top \to J(T),
\]

where the singular \(h^{-1}\) and \(h^{-2}\) terms cancel after passing to the even/odd jet basis, and similarly

\[
N_m(s)\to J(m)
\]

as \(s\to0\), despite the displayed formula for \(N_m(s)\) having apparent \(s^{-1},s^{-2},s^{-3}\) singularities. That is definitely a **phase-cancellation proof**, but it is a cancellation proof for the kernel

\[
K_\Phi(x,y)=\frac{\sin(\Phi(x)-\Phi(y))}{\pi(x-y)}
\]

with \(\Phi=\theta\), not yet for the full oscillatory object

\[
Z(t)=e^{i\theta(t)}\zeta(1/2+it).
\]

Your symbolic verification scripts are exactly checking this local phase-kernel layer: the same-point jet limit, the cross-block jet limit, and the trace/determinant identities for \(J(T)\).  The numerical script likewise tests these identities against the Riemann–Siegel theta phase and confirms positive definiteness of \(J(T)\) at sampled heights. 

So the right description is:

> We are proving **Riemann–Siegel phase-kernel cancellation identities**, and building a normalized finite-dimensional Gram calculus from them. We are not yet proving cancellation of the full \(Z(t)\)-sum or of \(\zeta(1/2+it)\) itself.

The distinction matters. Classical Riemann–Siegel work studies

\[
Z(t)
=
2\sum_{n\le \sqrt{t/2\pi}}
\frac{\cos(\theta(t)-t\log n)}{\sqrt n}
+
R(t),
\]

where the difficult cancellation is among many arithmetic oscillatory terms. That is a different level of cancellation from the local kernel identities we are currently proving. The Riemann–Siegel formula and its refinements are the standard computational tool for evaluating \(Z(t)\) and verifying zeros numerically, but they do not by themselves yield RH. citeturn802119search5turn802119search8turn802119search11

## Have similar proofs been tried?

Yes, in broad families. I do **not** know of a prior attempt with exactly this **jet–Gram / finite-block / transverse-quotient** architecture, but several older approaches are adjacent.

### 1. Classical sign-change and critical-line methods

The oldest critical-line strategy proves sign changes of \(Z(t)\) or related real critical-line functions. The classical theorem that there are infinitely many critical-line zeros is of this type: it extracts sign changes or oscillation from an integral representation. Modern expositions still frame it as a critical-line real-function argument. citeturn802119search0turn802119search3

This is philosophically related to what we are doing, because both approaches try to exploit the real phase normalization on the critical line. But technically it is different: those proofs use global integrals or sign changes of \(Z(t)\), while our current Sections 2–4 prove local Gram-kernel identities before any sign-change or source-energy argument enters.

### 2. Riemann–Siegel formula and explicit phase cancellation

A large body of work uses the Riemann–Siegel formula to compute \(Z(t)\), study Gram points, detect zeros, and understand the oscillatory sum

\[
\cos(\theta(t)-t\log n).
\]

That is probably the most direct historical precedent for “phase cancellation of the Riemann–Siegel function.” But those methods typically study cancellation in the long trigonometric sum, not in a local jet–Gram kernel. citeturn802119search5turn802119search11turn802119search16

So if later sections of our paper try to prove the needed source-energy transfer by estimating actual \(Z(t)\)-oscillation, we will be entering heavily explored territory.

### 3. Mollifier and moment methods

The Levinson–Conrey line of work proves that a positive proportion of zeros lie on the critical line using mollifiers and moment estimates. These methods are also cancellation/energy arguments, but they are global and arithmetic: they use mean values of \(\zeta\), mollified \(\zeta\), or derivatives to force critical-line zeros. Conrey’s refinement pushed the known proportion beyond two fifths; later work combines mollifiers with zero-detection and higher moment estimates. citeturn802119search10turn802119search7turn802119search4

Our phrase **source-energy transfer** is closest in spirit to this tradition. The difference is that we are trying to route source energy into a finite local transverse jet–Gram obstruction, instead of directly counting zeros by global mollified moments.

### 4. de Bruijn–Newman / heat-flow methods

Another adjacent family deforms the Riemann \(\xi\)-function under a heat flow. The de Bruijn–Newman constant \(\Lambda\) measures when the deformed function has only real zeros; RH is equivalent to \(\Lambda\le0\), and Rodgers–Tao proved Newman’s conjecture \(\Lambda\ge0\). citeturn787611search2turn787611search6

This is related at a high level because it studies how zero configurations and local zero dynamics respond to perturbations. But it is not the same as our present finite jet–Gram calculation. Their object is a heat-flow deformation of the completed \(\xi\)-function, whereas our current object is a local phase kernel derived from \(\theta(t)\).

### 5. de Branges / reproducing-kernel positivity approaches

The closest conceptual neighbor is probably de Branges theory: Hilbert spaces of entire functions, reproducing kernels, phase functions, and positivity conditions. Those approaches are explicitly kernel/positivity-based and have long been discussed in connection with RH. citeturn145005search2turn145005search6

But there is a serious warning here: Conrey and Li studied de Branges-type positivity conditions related to zeta and \(L\)-functions and found examples showing that the proposed positivity conditions are not satisfied by the relevant defining functions. citeturn145005search1turn145005search3

That warning is relevant to us. It means we should be careful not to let “positive local Gram block” become “therefore global RH positivity.” Our local \(J(T)\succ0\) result is real and useful, but it is much weaker than the kind of global reproducing-kernel positivity that has historically run into obstructions.

## What seems genuinely different here

The distinctive part of our current architecture is not merely “use the Riemann–Siegel phase.” That has been done extensively. The distinctive part is the sequence

\[
\text{phase kernel}
\to
\text{coalescing even/odd jet basis}
\to
\text{finite same-point and mixed blocks}
\to
\text{whitening}
\to
\text{transverse quotient}
\to
\text{off-line split-pair obstruction}.
\]

I do not know a standard RH attempt that packages the local Riemann–Siegel phase this way and then tries to compare an off-line split-pair toy model against an actual zeta-side transverse suppression theorem. The closest historical analogues are de Branges-type kernel positivity and mollified moment/source-energy methods, but neither appears to be the same mechanism.

## Referee warning

If the future proof only establishes cancellations of the theta-phase kernel, it will not prove RH. The theta phase is mainly the gamma-factor phase; it does not contain the arithmetic oscillation of \(\zeta\). To reach RH, the later sections must prove that actual zeta-side source energy or suppression enters the same transverse quotient.

So the clean way to frame the paper is:

> Sections 2–4 prove the deterministic local phase-kernel calculus. The hard RH-relevant step is not these cancellations themselves, but the later source-energy transfer or actual-zeta transverse suppression theorem that connects this calculus to the arithmetic \(Z(t)\)-object.

That framing keeps the paper honest and positions the current work relative to the historical literature.
## User (2026-05-02 17:30:55)

Our local J(T)≻0 result is real and useful, but it is much weaker than the kind of global reproducing-kernel positivity that has historically run into obstructions. --> is "weaker" in this context a good or bad thing in terms of a proof?

what is the likelihood we will ultimately succeed here? or is this an obvious deadend? 

## Assistant (2026-05-02 17:31:22)

I’ll separate strategic value from proof probability: local positivity is safer but weaker, and the decisive question is whether source-energy/transverse suppression can quantitatively reach the quotient obstruction.

_Thought for 3m 46s_

“Weaker” is **good for avoiding known obstructions**, but **bad if it remains the strongest fact in the paper**.

The local result

\[
J(T)\succ0
\]

is a safe, real, useful piece of analysis. It says the **coalesced theta-phase jet block** is positive and well-conditioned. That is good because it is not making an overambitious global positivity claim of the kind that de Branges-style RH programs have historically struggled with; Conrey–Li specifically examined de Branges-type positivity conditions and found serious difficulties/counterexamples for that line of attack. citeturn263439search4

But exactly because it is local, it is not close to RH by itself. It is positivity of a deterministic phase-kernel object built from the Riemann–Siegel phase. The current symbolic package verifies the same-point limit, cross-block limit, and trace/determinant identities for this local jet block; that is legitimate, but it is still a local phase calculation rather than an arithmetic statement about all nontrivial zeros. 

So:

\[
\boxed{\text{Weaker is good as a foundation; bad if it is the whole mechanism.}}
\]

## What would make this a real proof program?

The local \(J(T)\succ0\) result gives you a stable coordinate system: same-point Gram blocks can be inverted, finite blocks can be whitened, and singular-looking expressions have removable limits. That is necessary infrastructure.

But the proof needs a **separate forcing mechanism**. In our language, the hard target is not

\[
J(T)\succ0.
\]

The hard target is something like:

\[
\text{off-line zero packet}
\quad\Longrightarrow\quad
\text{nonzero transverse toy anomaly},
\]

while actual zeta satisfies

\[
\text{actual zeta transverse component}
\quad\text{is too small or incompatible}.
\]

The current Sections 2–4 prove the local calculus required to state that comparison cleanly. They do **not** yet prove the comparison.

The decisive future theorem is the **source-energy transfer / actual-zeta transverse suppression** theorem. If that theorem is real, this becomes a serious program. If that theorem cannot be stated without smuggling in RH-equivalent assumptions, the program collapses.

## Is this an obvious dead end?

No. It is not an obvious dead end at the level of Sections 2–4.

The local jet–Gram construction is mathematically coherent:

\[
P_h A_h(T)P_h^\top\to J(T),
\qquad
P_h C_h(T_1,T_2)P_h^\top\to \frac1\pi N_{12},
\]

and the positivity/whitening package is real. That means the framework is not failing immediately on normalization, signs, removable singularities, or local Gram degeneracy. Those are common places where speculative RH programs die early.

But it is also not yet evidence of a proof of RH. It is evidence that the **local coordinate system is viable**.

The danger is that theta-phase information is mostly gamma-factor information. The arithmetic part lives in

\[
Z(t)=e^{i\theta(t)}\zeta(1/2+it),
\]

or more generally in the zeta-side source terms. Classical Riemann–Siegel and zero-verification methods use this real critical-line function, but proving RH requires controlling all off-line zeros, not just building a good critical-line phase coordinate. The RH remains one of Clay’s Millennium problems, and the official problem description still frames it as the assertion that all non-obvious zeros have real part \(1/2\). citeturn263439search0

So the honest status is:

\[
\boxed{\text{Not an obvious dead end, but far from a proof.}}
\]

## My probability estimate

A numerical probability would be artificial, but I can give a calibrated assessment.

At the current stage, with Sections 2–4 only:

\[
\text{chance of this already implying RH} = 0.
\]

It does not yet touch enough arithmetic.

As a complete future proof program, I would assign it a **low prior probability**, because almost every RH program fails at exactly the point we are approaching: converting a clean local/functional-analytic structure into a global arithmetic obstruction. The local package is promising as infrastructure, but the decisive source-energy transfer theorem is still unproved.

If forced to put it into qualitative bins:

\[
\boxed{\text{Current state: credible local framework, unproven global engine.}}
\]

Not:

\[
\text{obvious proof}.
\]

Not:

\[
\text{obvious dead end}.
\]

Rather:

\[
\text{high-risk program with a clear bottleneck}.
\]

## What would convince me it is becoming viable?

Three things.

First, the quotient must be fixed **before** the zeta-side estimates are proved. If the transverse quotient is adjusted after seeing which coefficient works, the proof becomes circular.

Second, the off-line toy anomaly must produce a quantitative lower bound:

\[
\|\Pi_{\mathrm{tr}}\A_{\mathrm{toy}}\|\ge Q^{-A}.
\]

Third, actual zeta must satisfy an independently proved upper bound or incompatibility in the same quotient:

\[
\|\Pi_{\mathrm{tr}}\A_{\zeta}\|\le Q^{-B},
\qquad B>A,
\]

after all packet, whitening, source-transfer, and localization losses.

If those three are achieved, the program becomes substantially more serious.

## What would make it fail?

The program likely fails if one of the following happens:

\[
\text{actual zeta transverse term is the same size as the toy anomaly};
\]

or

\[
\text{the source-energy transfer theorem is secretly RH-equivalent};
\]

or

\[
\text{the quotient kills the toy anomaly once all gauge freedoms are included};
\]

or

\[
\text{branch entry from an off-line zero requires an assumption as strong as the desired conclusion}.
\]

Those are the failure modes I would watch most aggressively.

## Bottom line

The local positivity being “weaker” is strategically good because it avoids overclaiming global kernel positivity. It gives a stable analytic coordinate system rather than a dubious global positivity principle.

But a proof of RH will not come from that positivity alone. The whole program now depends on whether the source-energy/transverse-suppression layer can be proved in the same normalization.

My current assessment:

\[
\boxed{
\text{The local framework is not dead. The decisive theorem is still missing.}
}
\]

The next major referee test should be: can the two-point or four-point section state a fixed, non-circular transverse functional and prove a real zeta-side bound against it?
## User (2026-05-02 18:06:18)

is it possible that zeta tranverse term could be shown to cancel within this stable analytic coordinate system?

## Assistant (2026-05-02 18:06:44)

I’ll answer at the proof-program level: what cancellation would be needed, why the coordinate system helps, and where the likely obstruction lies.

The key distinction is whether cancellation follows from fixed symmetry and normalization, or whether it requires a genuinely arithmetic estimate.

_Thought for 4m 8s_

Yes. It is possible in principle. In fact, that is probably the **only way this program can become a proof**: the stable jet–Gram coordinate system must expose a zeta-side transverse cancellation that is invisible, or at least hard to isolate, in raw coordinates.

But the distinction is crucial:

\[
\text{stable coordinates can reveal cancellation;}
\]

they cannot by themselves create cancellation.

Sections 2–4 give us a well-conditioned local coordinate system. The symbolic checks verify that the same-point and cross-block singularities cancel correctly in the Gram-normalized jet basis, and that the trace/determinant identities for \(J(T)\) are internally consistent.  The numerical checks support that the same coordinate system behaves stably for the Riemann–Siegel theta phase at tested heights. 

So the right question is now:

\[
\boxed{
\text{Does actual zeta have an additional transverse cancellation in this coordinate system?}
}
\]

That is plausible enough to investigate, but it is not automatic.

## What “zeta transverse cancellation” would mean

Suppose the downstream object is some whitened finite block

\[
\widehat\Omega_\zeta(s;m)
=
G_{m,-}^{-1/2}N_m(s)G_{m,+}^{-1/2},
\]

or a corrected/source-bearing version of it. Then we eventually choose a transverse projection or functional

\[
\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_\zeta).
\]

A zeta-side transverse cancellation theorem would say something like:

\[
\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_\zeta)
=
O(Q^{-B})
\]

or even

\[
\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_\zeta)=0
\]

to leading order, while the off-line toy model has

\[
\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_{\mathrm{toy}})
\ge Q^{-A},
\qquad B>A.
\]

That would be the decisive kind of cancellation.

In words:

> The off-line model leaves a transverse residue, but actual zeta cancels that residue in the stable jet–Gram coordinates.

That is exactly the kind of mechanism we should be looking for.

## Why the stable coordinates may help

The current coordinates remove several nuisances:

\[
h^{-1},\quad h^{-2},\quad s^{-1},\quad s^{-2},\quad s^{-3}
\]

singularities are normalized away. Same-point blocks become positive definite, inverse square roots are controlled, and coalescence gives

\[
\widehat\Omega_\zeta(0;m)=I_2.
\]

That means a transverse term can no longer hide inside bad scaling, coordinate singularities, or Gram degeneracy. If a zeta-side cancellation exists, this system is a reasonable place to try to see it.

This is the good news.

The bad news is that the coordinate system currently comes mostly from the **theta phase**, which is gamma-factor geometry. Actual zeta cancellation must involve the arithmetic/source part. The theta phase gives stable local kinematics; it does not itself force the arithmetic transverse term to vanish.

## How such a cancellation could occur

There are a few realistic possibilities.

### 1. Exact symmetry cancellation

The functional equation, conjugation symmetry, and even/odd packet symmetrization may force certain transverse coefficients to vanish identically.

This would be the strongest case. A theorem might look like:

\[
\Pi_{\mathrm{tr}}\mathcal A_{\zeta}^{(k)}=0
\]

for the first nontrivial orders \(k\), because those coefficients are odd under a symmetry that the actual zeta packet respects.

This is the cleanest route if it exists.

### 2. Parity cancellation after packet symmetrization

Even if individual local terms do not vanish, the packet measure might kill them:

\[
\int \Pi_{\mathrm{tr}}\mathcal A_\zeta(m,s)\,d\mu(m,s)=0
\]

or

\[
\sum_{\text{symmetric packet}}
\Pi_{\mathrm{tr}}\mathcal A_\zeta(m,s)=0.
\]

This would fit naturally with the odd-moment cancellation material, provided the transverse coefficient is genuinely odd in the packet variable and the symmetrization is exact.

The danger is that approximate symmetry is not enough unless all errors are power-controlled.

### 3. Oscillatory source cancellation

The zeta-side source terms may oscillate fast enough that their transverse projection is small after localization:

\[
\Pi_{\mathrm{tr}}\mathcal A_\zeta
=
\text{oscillatory average}
=
O(Q^{-B}).
\]

This would be a source-energy transfer theorem. It is plausible in spirit, but this is where the hard arithmetic enters. One would need to prove the cancellation without assuming something equivalent to RH.

### 4. Gauge cancellation

Some transverse-looking terms may turn out to be gauge artifacts once the quotient is correctly fixed.

This is useful but dangerous. If the quotient is chosen after inspecting the zeta term, the argument risks becoming circular. The quotient must be fixed first, then the toy and zeta terms must be tested in the same quotient.

## What would make me confident?

I would want to see the following pipeline.

First, fix the transverse quotient:

\[
\Pi_{\mathrm{tr}}
\]

independently of the zeta-side computation.

Second, expand the actual zeta-side object in the stable coordinates:

\[
\Pi_{\mathrm{tr}}\mathcal A_\zeta
=
c_0(m,s)+c_1(m,s)+c_2(m,s)+\cdots.
\]

Third, classify each leading coefficient:

\[
c_j=0
\]

by exact symmetry, or

\[
c_j=O(Q^{-B_j})
\]

by a proved source-energy estimate.

Fourth, compute the same functional on the off-line toy model and show

\[
\Pi_{\mathrm{tr}}\mathcal A_{\mathrm{toy}}
\]

does **not** satisfy the same cancellation.

That last contrast is essential. If the same cancellation holds for the toy model, it cannot prove anything.

## What would make it fail?

This route likely fails if the actual zeta transverse term is not small. For example, if after all normalizations one finds

\[
\Pi_{\mathrm{tr}}\mathcal A_\zeta
\asymp
\Pi_{\mathrm{tr}}\mathcal A_{\mathrm{toy}},
\]

then the obstruction disappears.

It also fails if the cancellation theorem only works after allowing the quotient to depend on the zeta packet. The quotient must be fixed and non-adaptive.

It also fails if the needed cancellation is basically equivalent to RH. For example, a statement like “off-line contributions cancel in every transverse packet” may be true only because there are no off-line zeros. That would be circular unless proved from independent analytic input.

## My current view

Yes, zeta transverse cancellation inside this coordinate system is possible. It is not an obvious fantasy. The point of the local jet–Gram work is precisely to create a coordinate system where such a cancellation could be stated cleanly.

But I would frame it as an **open central target**, not as something already suggested by Sections 2–4.

The current work proves:

\[
\text{the coordinates are stable}.
\]

The next decisive theorem must prove:

\[
\text{actual zeta cancels, suppresses, or cannot support the transverse toy residue}.
\]

A good section title for the next frontier would be something like:

```tex
\section{Actual-zeta transverse cancellation target}
```

or more neutrally:

```tex
\section{Source-side transverse cancellation}
```

The first theorem target could be:

```tex
\begin{frontier}[Source-side transverse cancellation]
Fix the transverse projection \(\Pi_{\mathrm{tr}}\) and anomaly functional
\(\mathcal A\).  Prove that the actual zeta-side packet satisfies
\[
\|\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_\zeta)\|
\le Q^{-B}
\]
on retained packets, with \(B\) exceeding the toy visibility exponent after
all whitening and packet losses.
\end{frontier}
```

That is the theorem that determines whether this architecture has real RH potential.
## User (2026-05-02 19:20:13)

is the whitening loss potentially fatal for this proof? here's latest draft by the way

## Assistant (2026-05-02 19:20:31)

I’ll audit whether whitening only imposes the proven Section 4 loss or whether downstream source-side and quotient uses can erase the needed transverse exponent gap.

_Thought for 4m 19s_

It is **not fatal in the current real-axis theta-phase Section 4**. But it **could become fatal downstream** if lower bounds are pushed through whitening without a two-sided whitening ledger.

In the latest draft, Section 4 proves the safe one-sided estimate

\[
\bigl\|G_{m,\pm}(s)^{-1/2}\bigr\|_{\mathrm{op}}
\le Q(T)^{C_W},
\qquad C_W=0,
\]

after a high enough lower-height cutoff. Since

\[
G_{m,\pm}(s)=J(t_\pm),
\]

and the theta-phase calculation gives

\[
\lambda_{\min}(J(t))
=
\frac{2q(t)}{\pi}(1+o(1))
\sim
\frac1\pi\log\frac{t}{2\pi},
\]

the inverse square-root norm is actually

\[
\|J(t)^{-1/2}\|_{\mathrm{op}}
\sim
\sqrt{\frac{\pi}{2q(t)}}
\sim
\frac{\sqrt{\pi}}{\sqrt{\log t}}.
\]

So on the actual real-axis theta packets, whitening does **not** amplify. It contracts. The symbolic and numerical checks you supplied support the underlying \(J(T)\)-formula and the positivity behavior at the sampled heights.  

So, for **upper bounds** like

\[
\|\Pi_{\mathrm{tr}}\mathcal A(\widehat\Omega_\zeta)\|
\le Q^{-B_\z},
\]

the same-point whitening factors are not the danger. They are bounded by \(1\) after cutoff in the current normalization.

## The real danger: lower-bound attenuation

The subtle issue is that Section 4’s current whitening lemma is a **one-sided upper operator-norm bound**:

\[
\|G^{-1/2}\|_{\mathrm{op}}\le 1.
\]

That is enough to prevent upper-bound blowup. It is **not** enough to preserve lower bounds.

If some later argument proves a lower bound before whitening, say

\[
\|X\|\ge Q^{-A},
\]

and then passes to

\[
G_-^{-1/2}XG_+^{-1/2},
\]

then one also needs a lower singular-value estimate for the whitening map:

\[
\|G_-^{-1/2}XG_+^{-1/2}\|
\ge
\sigma_{\min}(G_-^{-1/2})
\sigma_{\min}(G_+^{-1/2})
\|X\|.
\]

Now

\[
\sigma_{\min}(G^{-1/2})
=
\lambda_{\max}(G)^{-1/2}.
\]

For the theta block,

\[
\lambda_{\max}(J(t))
\sim
\frac{q(t)^3}{6\pi},
\]

so

\[
\sigma_{\min}(J(t)^{-1/2})
\sim
\sqrt{6\pi}\,q(t)^{-3/2}.
\]

Two-sided whitening can therefore cost roughly

\[
q(t_-)^{-3/2}q(t_+)^{-3/2}
\sim
(\log T)^{-3}.
\]

That is not fatal if the exponent budget includes it. But it **is** fatal if the proof silently assumes that a lower bound survives whitening unchanged.

## Current draft status

The draft is safe if the toy and zeta exponents are already **post-whitening** exponents.

That is, if

\[
\|\Pi_{\mathrm{tr}}\mathcal A_{\mathrm{toy}}(\widehat\Omega_{\mathrm{toy}})\|
\ge Q^{-A_{\mathrm{toy}}}
\]

and

\[
\|\Pi_{\mathrm{tr}}\mathcal A_{\zeta}(\widehat\Omega_{\zeta})\|
\le Q^{-B_\z}
\]

are both stated after whitening, then the comparison theorem does not need to spend additional whitening loss. The whitening loss has already been absorbed into the definitions of \(A_{\mathrm{toy}}\) and \(B_\z\).

But if later sections prove toy visibility or source-energy transfer in **unwhitened** coordinates and then convert to whitened coordinates, the draft needs an explicit two-sided whitening-loss lemma.

## What I would add

I would add a small “two-sided whitening ledger” after Lemma `lem:whitening-loss`.

Something like:

```tex
\begin{lemma}[Two-sided whitening ledger]
\label{lem:two-sided-whitening-ledger}
Assume \(\Phi_T=\theta\) on \(I_T\), and assume in addition that
\(q(t)\le Q(T)^{C_q^+}\) uniformly for \(t\in I_T\).  Then for every
\(2\times2\) matrix \(X\) and every retained \((m,s)\in\mathcal D_T\),
\[
Q(T)^{-3C_q^+}\,\|X\|_{\op}
\;\ll\;
\|G_{m,-}(s)^{-1/2}XG_{m,+}(s)^{-1/2}\|_{\op}
\;\le\;
\|X\|_{\op},
\]
after increasing the lower-height cutoff.
\end{lemma}
```

The exact exponent can be tuned, but the important point is structural: lower-bound propagation through whitening costs a known polynomial factor.

The proof is simple:

\[
\lambda_{\min}(J(t))\sim \frac{2q(t)}{\pi},
\qquad
\lambda_{\max}(J(t))\sim \frac{q(t)^3}{6\pi}.
\]

Therefore

\[
\|J(t)^{-1/2}\|_{\op}
=
\lambda_{\min}(J(t))^{-1/2}
\ll 1,
\]

while

\[
\sigma_{\min}(J(t)^{-1/2})
=
\lambda_{\max}(J(t))^{-1/2}
\gg q(t)^{-3/2}.
\]

Multiplying left and right gives a loss \(\gg q(t_-)^{-3/2}q(t_+)^{-3/2}\), hence polynomial in \(Q\) once \(q(t)\le Q^{C_q^+}\) is part of the packet ledger.

## Potential fatal cases

Whitening becomes dangerous in four situations.

First, if the toy visibility lower bound is proved before whitening and the post-whitening lower bound is assumed rather than proved.

Second, if source-energy transfer gives energy in an unwhitened source coordinate and the proof does not pay the \(q^{-3}\)-type two-sided whitening cost.

Third, if later work needs complex-\(s\) whitening or four-point whitening. Section 4 only controls real-axis \(2\times2\) same-point theta blocks. It does not prove complex-disk spectral stability or four-center Gram nondegeneracy.

Fourth, if the transverse projection is fixed in pre-whitened coordinates but compared after whitening. The quotient should be fixed in the same normalized coordinates in which toy visibility and actual-zeta suppression are stated.

## Bottom line

For the current Section 4 result:

\[
\boxed{\text{whitening loss is not fatal; it is essentially } C_W=0.}
\]

For the full RH program:

\[
\boxed{\text{whitening could become fatal only if lower-bound transfer is not ledgered.}}
\]

The fix is straightforward: keep all toy and zeta exponents post-whitening, or add an explicit two-sided whitening ledger and subtract that loss from the exponent gap.

The comparison theorem should ultimately use an effective inequality of the form

\[
A_{\mathrm{toy}}^{\mathrm{eff}}
<
B_\z^{\mathrm{eff}},
\]

where both exponents are already in the whitened transverse coordinate system.
## User (2026-05-03 05:03:16)

here's the latest paper draft. give a patch for the whitening ledger + proof

## Assistant (2026-05-03 05:03:33)

I’ll add a focused Section 4 insertion: a two-sided whitening ledger proving both upper-bound safety and quantified lower-bound attenuation in the current real-axis theta normalization.

_Thought for 7m 17s_

I added the whitening ledger as a focused Section 4 patch.

Files:

- [Whitening ledger patch](sandbox:/mnt/data/sec4-whitening-ledger-patch.tex)
- [Integrated draft with whitening ledger](sandbox:/mnt/data/rh_rebuild_with_whitening_ledger.tex)
- [Diff against latest draft](sandbox:/mnt/data/rh_rebuild_with_whitening_ledger.diff)
- [Draft-mode compile log](sandbox:/mnt/data/rh_rebuild_with_whitening_ledger.compile2.log)

I inserted the new material immediately after the existing scope remark for `lem:whitening-loss`.

The patch is consistent with the Gram-normalized \(P_h\) convention already used in the current verification layer. 

## What the patch adds

It adds a new subsection:

```tex
\subsection{Two-sided whitening ledger}
\label{subsec:two-sided-whitening-ledger}
```

with three main statements.

First, it proves the spectral sizes of the finite same-point blocks:

\[
\lambda_{\min}(G_{m,\pm}(s))
=
\frac{2q(t_\pm)}{\pi}(1+o_T(1)),
\]

and

\[
\lambda_{\max}(G_{m,\pm}(s))
=
\frac{q(t_\pm)^3}{6\pi}(1+o_T(1)).
\]

Second, it defines the whitening map

\[
\mathsf W_{m,s}(X)
=
G_{m,-}(s)^{-1/2}XG_{m,+}(s)^{-1/2}
\]

and proves the two-sided operator-norm ledger

\[
c\,(q(t_-)q(t_+))^{-3/2}\|X\|_{\op}
\le
\|\mathsf W_{m,s}(X)\|_{\op}
\le
C\,(q(t_-)q(t_+))^{-1/2}\|X\|_{\op}.
\]

Since \(q(t_\pm)\asymp\log T\), the lower-bound attenuation is

\[
(q(t_-)q(t_+))^{-3/2}
\asymp
(\log T)^{-3}.
\]

Third, it gives a polynomial \(Q\)-ledger version. If the packet scale records the upper phase-slope bound

\[
q(t)\le Q(T)^{C_q^+},
\]

then a pre-whitening lower bound

\[
\|X\|_{\op}\ge Q(T)^{-A}
\]

becomes the post-whitening lower bound

\[
\|\mathsf W_{m,s}(X)\|_{\op}
\ge
c\,Q(T)^{-(A+3C_q^+)}.
\]

That is the main useful bookkeeping result.

## Why the extra \(q(t)\le Q^{C_q^+}\) condition is necessary

The draft already proves \(q(t)\asymp\log T\) on \(I_T\), but the paper’s \(Q(T)\) scale is still abstract. To convert the exact log-loss

\[
(\log T)^{-3}
\]

into a power of \(Q\), the proof needs an explicit ledger relation between \(q\) and \(Q\). The patch therefore does **not** silently assume this. It states the needed condition as

```tex
q(t)\le Q(T)^{C_q^+}.
```

If later the paper fixes \(Q(T)=1+\log T\), then \(C_q^+=1\) works.

## Referee-safe interpretation

This patch prevents two common downstream mistakes.

First, it prevents using

\[
\|G^{-1/2}\|_{\op}\le 1
\]

as if it also preserved lower bounds. It does not. Lower bounds pay the two-sided cost

\[
(q_-q_+)^{-3/2}.
\]

Second, it separates post-whitening and pre-whitening estimates. If a toy visibility theorem is already stated after whitening, no additional loss is charged. If it is proved before whitening, this ledger must be consumed.

The patch does **not** claim actual-zeta suppression, source-energy transfer, complex-disk whitening, or four-point whitening. It only proves the real-axis two-sided same-point whitening ledger.
