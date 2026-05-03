# RH Proof Rebuild Strategy

- Source: https://chatgpt.com/c/69f496f4-0c70-83e8-ac5f-5cab58ecf4a3
- Created: 2026-05-01 12:05:09 UTC
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
## User (2026-05-02 18:08:23)

check the updated patch as a referee, and also the sympy and simulation (check its content, do not run it). referee the patch, and ensure the python has complete coverage. give me a new patch if needed, and let me know what's missing from the python

## Assistant (2026-05-02 18:08:39)

I’ll audit Section 4 mathematically, then review the symbolic and numerical scripts as coverage artifacts without executing them. I’ll patch only proof gaps or unsafe coverage boundaries.

The core Section 4 formulas now look stable, including the \(s_{12}=-s\) sign conversion. I’m narrowing the audit to whitening uniformity, coalescence, and script coverage boundaries.

_Thought for 16m 42s_

Referee verdict: **the mathematical patch is essentially correct, but I would merge a small hardened version rather than the submitted one verbatim.** The remaining defects are not formula errors; they are domain/scope issues around \(s=0\) and one overstrong introductory sentence.

I created a tightened patch and diff:

- [Hardened Section 4 patch v2](sandbox:/mnt/data/sec-finite-scale-local-blocks-and-whitening.referee-hardened2.tex)
- [Diff against your submitted patch](sandbox:/mnt/data/sec-finite-scale-local-blocks-and-whitening.referee-hardened2.diff)

I did **not** run the Python files. I reviewed their content only.

## Paper-content audit

The core formulas are correct.

The finite same-point blocks

\[
G_{m,\pm}(s)=J(t_\pm)
\]

are in the right Gram-normalized convention, and the mixed block

\[
N_m(s)=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin\Delta_m(s)}{s}
&
\dfrac{\sin\Delta_m(s)+q_+s\cos\Delta_m(s)}{s^2}
\\[2.4ex]
-\dfrac{\sin\Delta_m(s)+q_-s\cos\Delta_m(s)}{s^2}
&
\dfrac{(q_-+q_+)s\cos\Delta_m(s)+(2-q_-q_+s^2)\sin\Delta_m(s)}{2s^3}
\end{pmatrix}
\]

has the correct sign convention for \(t_-=m-s/2\), \(t_+=m+s/2\), so that \(T_1-T_2=-s\).

The removable-singularity proof is now sound. The sign pattern

\[
q_+=q+\frac{s}{2}q'+\frac{s^2}{8}q''+o(s^2),
\qquad
q_-=q-\frac{s}{2}q'+\frac{s^2}{8}q''+o(s^2)
\]

is correct, and the expansion

\[
\Delta_m(s)=-qs-\frac{q''}{24}s^3+o(s^3)
\]

gives

\[
N_m(0)=J(m)
\]

entry by entry.

The whitening-loss lemma is also correct for its stated real-axis theta-phase scope:

\[
\|G_{m,\pm}(s)^{-1/2}\|_{\mathrm{op}}
\le
\sqrt{\frac{\pi}{2q(t_\pm)}}(1+\varepsilon_T),
\qquad \varepsilon_T\to0,
\]

and the \(C_W=0\) conclusion follows after raising the lower-height cutoff.

## What I changed in the hardened patch

I made five content-level edits.

First, I changed the introductory paragraph. The submitted version said Section 4 “produces the input consumed by every comparison theorem” downstream. That is too strong. Section 4 only records the finite real-axis block package and whitening-factor loss. It does **not** produce source-energy transfer or actual-zeta transverse suppression. The hardened patch says that explicitly.

Second, I changed the domain of \(G_{m,\pm}(s)\). In the submitted patch, the subsection starts by fixing

\[
(m,s)\in\mathcal D_T^\times,
\]

so technically \(G_{m,\pm}(0)\) was not defined when later used in the coalescence corollary. I changed this to define \(G_{m,\pm}(s)\) for all

\[
(m,s)\in\mathcal D_T,
\]

and reserve \(N_m(s)\)'s displayed singular formula for \(s\ne0\).

Third, I changed the exact finite-block interpretation lemma to say

\[
G_{m,\pm}(s)=J(t_\pm)
\quad\text{for all }(m,s)\in\mathcal D_T,
\]

while the kernel-derivative interpretation of \(N_m(s)\) is only asserted on \(\mathcal D_T^\times\).

Fourth, I sharpened the removable-singularity lemma to say that \(s\to0\) is taken with

\[
(m,s)\in\mathcal D_T^\times,
\]

and that \(m\in I_T\). This removes a minor but real domain ambiguity.

Fifth, I added the convention that, after the removable-singularity lemma,

\[
N_m(0)
\]

means the continuous extension. Then the whitened finite block is defined on \(\mathcal D_T\), with \(N_m(0)\) understood by extension.

These edits are small, but they prevent later sections from citing \(G_{m,\pm}(0)\), \(N_m(0)\), or \(\widehat\Omega_\zeta(0;m)\) before those objects have actually been defined.

## Python coverage audit

The Python coverage is useful but should not be described as complete proof verification yet.

The symbolic script covers the main algebraic formulas: \(G_{m,\pm}=J(t_\pm)\), \(N_m(s)=\pi^{-1}N_{12}(t_-,t_+)\), the \(q_\pm\) Taylor signs, the removable singularity \(N_m(0)=J(m)\), coalescence, whitening loss, and an inverse-square-root route check. Its own coverage header lists these items. 

The numerical script covers positive definiteness of sampled \(G_{m,\pm}\), \(N_m(s)\to J(m)\), whitening-loss sweeps, lambda-minimum checks, coalescence, and a closed-form inverse-square-root comparison. Its coverage header also says it is an assertion-based mpmath regression harness. 

But there are several coverage gaps or overclaims.

### 1. The symbolic inverse-square-root verification is not fully symbolic

The symbolic script says both inverse-square-root routes match symbolically, but the displayed code specializes to

\[
q=5,\qquad q'=1/100,\qquad q''=-1/200
\]

for the coalescence and inverse-square-root comparisons. The coalescence check therefore verifies a representative SPD point, not the full symbolic identity for a general \(2\times2\) SPD matrix. 

What to add:

Use generic SPD symbols

\[
G=
\begin{pmatrix}
a&b\\ b&d
\end{pmatrix},
\qquad a>0,\quad \Delta=ad-b^2>0,
\]

and verify algebraically that

\[
S=\sqrt{\operatorname{tr}G+2\sqrt{\Delta}}\,
(G+\sqrt{\Delta}I)^{-1}
\]

satisfies

\[
SGS=I.
\]

That would close the symbolic coverage for \(G^{-1/2}GG^{-1/2}=I\).

### 2. The signed-\(s\) numerical check is incomplete

The simulation claims to check the signed-\(s\) domain, but it only checks

\[
G_{m,+}(s)=G_{m,-}(-s)
\]

and the evenness of the \((1,1)\)-entry of \(N_m(s)\). The code comments explicitly say that the other \(N_m\) entries merely swap roles and are not checked. 

What to add:

Check the full symmetry

\[
N_m(-s)=N_m(s)^\top.
\]

Then, once whitening is included, also check

\[
\widehat\Omega_\zeta(-s;m)
=
\widehat\Omega_\zeta(s;m)^\top.
\]

That is not needed for the current Section 4 proof, but it is the natural regression guard for signed-\(s\) conventions.

### 3. The numerical “operator norm” of \(N_m(s)\) is not reliable

The numerical script defines an `op_norm` routine using the symmetric \(2\times2\) eigenvalue formula. That is valid for symmetric matrices, but \(N_m(s)\) is generally not symmetric when \(s\ne0\). The script uses this value for `op_N` in the finite-block sweep.

This does **not** damage the paper, because Section 4 does not claim a uniform operator-norm bound for \(N_m(s)\). But the script should not call that number an operator norm unless it computes singular values.

What to add:

Either remove the `op_N` reporting, or replace it with a true singular-value norm, i.e. the square root of the largest eigenvalue of

\[
N_m(s)^\ast N_m(s).
\]

### 4. The simulation does not consistently enforce \((m,s)\in\mathcal D_T\)

The paper domain is

\[
\mathcal D_T=\{(m,s):m-s/2\in I_T,\ m+s/2\in I_T\}.
\]

Some numerical sweeps choose midpoints and separations separately. For example, a midpoint near the edge of the sampled window combined with \(s\approx 1/Q\) can put \(t_\pm\) outside the window that was informally called \(I_T\). This is harmless for theta, because theta is globally defined, but it means the simulation is not exactly testing the finite packet domain.

What to add:

Define an explicit sampled interval

\[
I_T=[T-\rho/Q,T+\rho/Q],
\]

then generate only pairs \((m,s)\) satisfying

\[
m\pm s/2\in I_T.
\]

### 5. The numerical coalescence check is not actually across heights

The numerical script’s coverage header says “Coalescence Omega(0;m)=I_2 numerically across heights,” but the main function calls the coalescence check only at the anchor height \(T=10^5\). The main function then calls height sweeps for whitening loss and lambda-minimum, but not for \(\widehat\Omega_\zeta(s;m)\to I_2\). 

What to add:

Run `check_omega_coalescence_numerical(T)` over the same height ladder used for whitening, for example

\[
T\in\{10^3,10^4,10^5,10^6\}.
\]

### 6. The lambda-minimum wording should be weakened

The numerical script says it confirms

\[
\lambda_{\min}(G)\ge \frac{2q(t_\pm)}{\pi}(1+o(1)).
\]

The paper’s rigorous statement is better:

\[
\lambda_{\min}(G)
=
\frac{2q(t_\pm)}{\pi}(1+o(1)),
\]

or, for lower bounds,

\[
\lambda_{\min}(G)
\ge
\frac{2q(t_\pm)}{\pi}(1-\delta_T),
\qquad \delta_T\to0.
\]

The simulation should use the same wording.

## Final recommendation

Merge the hardened v2 patch, not the submitted patch verbatim.

Treat the Python status as:

\[
\texttt{sympy: partial/strong regression},\qquad
\texttt{simulation: partial/strong regression},
\]

not as complete formal coverage. The symbolic script covers the formulas and Taylor signs well; the simulation is useful for normalization and sign regressions. The missing Python pieces are mostly inverse-square-root generality, full signed-\(s\) symmetry, true nonsymmetric operator norms if reported, exact \(\mathcal D_T\) sampling, and height-ladder coalescence.
## User (2026-05-02 18:28:15)

do similar checks of the sympy/simulation for sections 2 & 3

## Assistant (2026-05-02 18:28:43)

I’ll audit the Section 2–3 scripts as text-only regression evidence, not proof, checking claimed coverage against the merged paper and flagging overclaims or missing guards.

Initial finding: the scripts are strong regression harnesses, and the paper likely needs no mathematical patch from this check. I’m now isolating header overclaims and print-only checks.
## User (2026-05-02 18:38:24)

if python times out, don't worry. just focus on the structure/case coverage for now

## Assistant (2026-05-02 18:40:38)

There appear to be newer current scripts and older partial ones; I’m separating them so obsolete artifacts do not inflate the claimed coverage.

_Thought for 22m 26s_

Referee verdict: **Sections 2–3 Python coverage is strong, but not quite “complete” as submitted.** The symbolic scripts cover the load-bearing algebra well. The simulation scripts are useful regression harnesses, but a few checks were print-only while the headers said “every check is an assertion.” I hardened those.

I did **not** run the Python.

Files:

- [Hardened §2 symbolic script](sandbox:/mnt/data/sec-local-kernel-and-jet-normalization.sympy.referee-hardened.py)
- [Diff for §2 symbolic script](sandbox:/mnt/data/sec-local-kernel-and-jet-normalization.sympy.referee-hardened.diff)
- [Hardened §2 simulation script](sandbox:/mnt/data/sec-local-kernel-and-jet-normalization.sim.referee-hardened.py)
- [Diff for §2 simulation script](sandbox:/mnt/data/sec-local-kernel-and-jet-normalization.sim.referee-hardened.diff)
- [Hardened §3 symbolic script](sandbox:/mnt/data/sec-jet-limit-local-blocks.sympy.referee-hardened.py)
- [Diff for §3 symbolic script](sandbox:/mnt/data/sec-jet-limit-local-blocks.sympy.referee-hardened.diff)
- [Hardened §3 simulation script](sandbox:/mnt/data/sec-jet-limit-local-blocks.sim.referee-hardened.py)
- [Diff for §3 simulation script](sandbox:/mnt/data/sec-jet-limit-local-blocks.sim.referee-hardened.diff)

## Overall assessment

The §2 symbolic script checks the core phase-kernel material: symmetry, removable singularity, off-diagonal derivative formulas, diagonal derivative limits, theta derivative asymptotics, the factored Taylor proof, and joint-continuity form. That is the right symbolic coverage for Section 2. 

The §3 symbolic script checks the core jet-limit material: the Gram-normalized same-point limit, cross-block limit, trace/determinant identities, theta-asymptotic positivity, explicit \(O(h^2)\) same-point rate, parity selection for the cross-block proof, finite-power dependence on \(|s|^{-1}\), and the two-sided \(\lambda_{\min}\) asymptotic. That is the right algebraic coverage for Section 3. 

The simulations for §2 and §3 are appropriate as numerical regression tests, not proof artifacts. The §2 simulation checks the theta definition, derivative asymptotics, uniform window behavior, kernel symmetry, diagonal continuity, diagonal derivatives, and off-diagonal derivative formulas.  The §3 simulation checks positivity, \(D_J/(4q^4)\to1\), direct \(P_h A_hP_h^\top\to J\), direct \(P_h C_hP_h^\top\to\pi^{-1}N_{12}\), \(O(h^2)\) rates, fixed-separation constraints, near-collision stress, and the two-sided \(\lambda_{\min}\) bracket. 

## Main issues I found

### 1. §2 simulation had print-only “PASS/WARN” checks

Several checks were described as verified but did not actually assert failure conditions:

- the comparison between `siegeltheta(t)` and the defining expression using `loggamma`;
- the branch-realness check for \(L(x)=\log\Gamma(x)\) on \(x>0\);
- the single-window P2 check;
- the height-ladder residual check for  
  \[
  T^2\left(q(T)-\frac12\log\frac{T}{2\pi}\right)\to -\frac1{48}.
  \]

I hardened these into actual assertions.

### 2. §2 simulation did not explicitly finite-difference \(K_y(T,T)\)

It checked \(K_x(T,T)\) and \(K_{xy}(T,T)\), but the paper states

\[
K_x(T,T)=K_y(T,T)=\frac{q'(T)}{2\pi}.
\]

The symbolic script covers both, but the numerical simulation only explicitly finite-differenced \(K_x\). I added a \(K_y\) finite-difference check and monotonic error assertion.

### 3. §2 simulation checked off-diagonal derivatives at only one signed separation

The formulas are sign-sensitive in

\[
s=T_1-T_2.
\]

I added the same off-diagonal derivative regression at both \(T_2=T_1+0.5\) and \(T_2=T_1-0.5\).

### 4. §2 symbolic Stirling check was too permissive

The symbolic script’s Stirling verification had an `INFO` branch for a nonzero retained residual. That is not referee-safe for a verification artifact. If the retained \(t^0\) or \(t^{-1}\) coefficient is wrong, the script should fail.

I changed that branch to raise an assertion if the leading retained residual does not vanish.

### 5. §3 symbolic script had one unsafe explanatory phrase

It printed an “asymptotic dominance check” under “\(q\to\infty\), \(q'\) and \(q''\) polynomial.” That phrasing is mathematically unsafe: arbitrary polynomial-size \(q'\) or \(q''\) can dominate logarithmic \(q\).

The actual paper’s proof is theta-specific:

\[
q(T)\sim \frac12\log T,\qquad q'(T)=O(T^{-1}),\qquad q''(T)=O(T^{-2}).
\]

I changed the script wording to match that.

### 6. §3 symbolic finite-\(|s|^{-1}\) check did not assert all denominator tests

The script computed whether denominators were pure finite powers of \(s\), but if a denominator failed that test it only printed `CHECK` and continued. I changed this into an assertion failure.

### 7. §3 simulation had two wording overclaims

The simulation’s finite-range power fit for \(\lambda_{\min}(J(T))\) was described as “polynomial in log \(T\).” That is not the right interpretation. The actual theorem says

\[
\lambda_{\min}(J(T))
\sim \frac1\pi\log\frac{T}{2\pi}.
\]

A finite-range fit to \(T^c\) is descriptive only. I changed the wording.

Also, the cross-block \(|s|^{-1}\) stress test was described too much like proof of the finite-power dependence. I relabeled it as a numerical stress test; the symbolic/Taylor argument is the proof.

## Coverage after hardening

I would now rate the Python artifacts as follows.

For §2:

- **Symbolic coverage:** strong.
- **Numerical coverage:** strong regression coverage after hardening.
- **Still not formal proof:** analytic Stirling remainder bounds, holomorphic branch existence, and functional-equation reality of \(Z(t)\) remain mathematical/literature inputs, not proved by Python.

For §3:

- **Symbolic coverage:** strong for the displayed algebra, normalization, limits, trace/determinant, parity, and theta asymptotic positivity.
- **Numerical coverage:** strong regression coverage for signs, rates, positivity, and fixed-separation scope.
- **Still not formal proof:** uniform big-\(O\) constants, rigorous interval-certified numerics, and all analytic smoothness hypotheses are not established by simulation.

## Remaining Python gaps

Nothing missing is fatal, but these are the remaining non-covered or only partially covered items:

1. The simulations are not interval-arithmetic proofs. They should not be cited as establishing theorem-level estimates.

2. The §2 symbolic script checks the retained Stirling algebra, but not the analytic theorem that the differentiated remainder is uniform in the sector. That belongs in the paper as a cited classical asymptotic fact, not in Python.

3. The §3 same-point \(O(h^2)\) symbolic check verifies the absence of subquadratic terms, but does not compute the full \(h^2\) coefficient with every higher theta derivative retained. That is fine for the lemma’s rate, but it should not be described as verifying the complete next-order expansion.

4. The §3 near-collision material is correctly treated as a stress test only. It does not and should not be used as a collision expansion.

Final recommendation: merge the current paper content, and replace the §2–§3 verification scripts with the hardened versions above.
## User (2026-05-02 19:11:38)

review the current structure of the Lean files. Aside from any remaining sorrys, is the rest correct and conforming with the paper? please check for anything amiss.

## Assistant (2026-05-02 19:12:00)

I’ll audit the Lean files against the merged Sections 2–3 structure, focusing on conventions, theorem statements, dependencies, and non-`sorry` mathematical content.

The block normalizations and sign conventions appear aligned; the substantive issue is the Lean theta definition using principal `Complex.log`, which changes derivative targets.

_Thought for 11m 42s_

Referee verdict: **not fully conforming yet.** The Lean structure is broadly aligned with the paper’s Sections 2–3, and the core matrix normalizations are correct, but there is one serious foundational mismatch and several coverage gaps. I would not treat the Lean files as paper-conforming beyond “spec-level scaffolding” until these are fixed.

Files reviewed:

- [RiemannSiegelTheta.lean](sandbox:/mnt/data/RiemannSiegelTheta.lean)
- [LocalKernelJetNormalization.lean](sandbox:/mnt/data/LocalKernelJetNormalization.lean)
- [JetLimitLocalBlocks.lean](sandbox:/mnt/data/JetLimitLocalBlocks.lean)

I did **not** compile them. There is no `lean`/`lake` executable available in the container, so this is a mathematical and structural audit, not a Lean kernel audit.

## Main issue: the Lean theta is not the paper theta

The paper defines \(\theta\) using the holomorphic branch \(L(z)=\log\Gamma z\) on \(\Re z>0\), normalized to be real on the positive real axis. In the Lean file, however, `theta` is defined using

```lean
Complex.log (Complex.Gamma (...))
```

i.e. the principal logarithm.

That is not referee-safe. The principal logarithm of \(\Gamma(z)\) can jump when \(\Gamma(z)\) crosses the principal branch cut. The paper avoided exactly this issue by choosing the global holomorphic branch of \(\log\Gamma\) on the right half-plane. The Lean comment says the two phases differ by a piecewise constant \(2\pi k(t)\), and that the kernel is invariant under \(2\pi\)-shifts. That may be harmless for raw \(\sin(\theta(x)-\theta(y))\) values away from jumps, but it is **not** harmless for the derivative definitions

```lean
q t := deriv theta t
qPrime t := deriv (deriv theta) t
qDoublePrime t := deriv (deriv (deriv theta)) t
```

At branch crossings, the derivative of the principal-branch expression is not the derivative of the continuous Riemann–Siegel phase. Therefore the global theorem

```lean
theta_derivative_asymptotics
```

is not safely true for the current concrete definition of `theta`.

### Recommended fix

Do **not** use the principal branch as the foundational definition. For now, make `theta` an abstract analytic object matching the paper branch, and keep the log-Gamma construction as a future bridge theorem.

A structurally safer root module would look like this:

```lean
/-- The continuous Riemann--Siegel phase defined from the holomorphic
branch of log Γ on `Re z > 0`, normalized to be real on the positive
real axis.  This is the object used in the paper. -/
constant theta : ℝ → ℝ

noncomputable def q (t : ℝ) : ℝ := deriv theta t
noncomputable def qPrime (t : ℝ) : ℝ := deriv (deriv theta) t
noncomputable def qDoublePrime (t : ℝ) : ℝ := deriv (deriv (deriv theta)) t
```

Then move the current principal-branch expression to a separate auxiliary definition:

```lean
/-- Principal-branch expression.  This is not used as the paper theta. -/
noncomputable def thetaPrincipal (t : ℝ) : ℝ :=
  (Complex.log (Complex.Gamma ((1 : ℂ) / 4 + Complex.I * (t : ℂ) / 2))).im
    - (t / 2) * Real.log Real.pi
```

and add a future theorem, with `sorry`, relating it to the paper branch away from branch-cut crossings if needed. The active proof should not depend on `thetaPrincipal`.

## Correct parts

The following are structurally correct and conform to the current paper:

1. **The Gram-normalized point-to-jet transform is correct.**

```lean
(1 / Real.sqrt 2) • !![1, 1; -1/(2*h), 1/(2*h)]
```

This matches

\[
P_h=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1/(2h)&1/(2h)
\end{pmatrix}.
\]

2. **The same-point block \(J(T)\) is correct.**

```lean
(1 / Real.pi) • !![2 * q T, qPrime T / 2;
                   qPrime T / 2, (qDoublePrime T + 2 * (q T)^3) / 12]
```

This matches the paper’s Gram-normalized \(J(T)\).

3. **The cross-block \(N_{12}\) sign convention is correct.**

The Lean definition of `N12` uses

\[
s=T_1-T_2,\qquad \Delta=\theta(T_1)-\theta(T_2),
\]

and the entries match the paper’s displayed \(N_{12}\). The theorem target

```lean
(nhds ((1 / Real.pi) • N12 T₁ T₂))
```

is also correct because `N12` itself excludes the external \(1/\pi\).

4. **The determinant coefficient is correct.**

The Lean theorem

```lean
(J T).det = D_J T / (12 * Real.pi^2)
```

uses the correct \(1/(12\pi^2)\) coefficient.

5. **The algebraic Gram criterion is mathematically sound.**

The equivalence

\[
J(T)\succ0
\quad\Longleftrightarrow\quad
q(T)>0,\ D_J(T)>0
\]

is correct. The Lean proof uses a sum-of-squares identity rather than Sylvester’s criterion, but the identity is valid:

\[
24q\pi\, x^\top Jx
=
3(4qx_0+q'x_1)^2+D_Jx_1^2.
\]

That is a good formalization route.

## Coverage gaps relative to the paper

### 1. The Lean phase-window theorem does not match the paper’s \(I_T\) formulation

The paper works on retained windows \(I_T\subset[T/2,2T]\). The Lean theorem

```lean
theta_derivative_asymptotics
```

uses the surrogate window

```lean
T - 1 ≤ t → t ≤ T + 1
```

This is not wrong as a local high-\(T\) surrogate, but it is not the paper’s actual retained-packet interface.

A better Lean statement would be dyadic:

```lean
theorem theta_derivative_asymptotics_dyadic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T t : ℝ, T₀ ≤ T → T / 2 ≤ t → t ≤ 2 * T →
      |q t - ((1/2) * Real.log (t / (2 * Real.pi)) - 1 / (48 * t^2))|
        ≤ C / t^4 ∧
      |qPrime t - 1 / (2 * t)| ≤ C / t^3 ∧
      |qDoublePrime t - (-1) / (2 * t^2)| ≤ C / t^4 := by
  sorry
```

Then the paper’s \(I_T\subset[T/2,2T]\) condition can be consumed directly.

### 2. The kernel continuity theorem is weaker than the paper

The paper proves joint continuity at the diagonal:

\[
K_\Phi(x,y)\to q(T)/\pi
\qquad (x,y)\to(T,T).
\]

Lean currently has only

```lean
Filter.Tendsto (fun x => phaseKernel x y) (nhds y) (nhds (q y / Real.pi))
```

That is a one-variable limit with \(y\) fixed. It is not the same as joint continuity.

Add:

```lean
theorem phase_kernel_joint_diagonal_limit (T : ℝ) :
    Filter.Tendsto
      (fun p : ℝ × ℝ => phaseKernel p.1 p.2)
      (nhds (T, T))
      (nhds (q T / Real.pi)) := by
  sorry
```

This matters because the same-point block samples both coordinates simultaneously.

### 3. The Lean kernel module formalizes only the theta phase, not a general \(\Phi\)

The paper states the phase-kernel lemmas for a general real \(C^1\) or \(C^4\) phase \(\Phi\), then specializes to \(\Phi_T=\theta\). The Lean file defines only

```lean
phaseKernel x y
```

using the global `theta`.

That is acceptable if the Lean goal is “formalize only the active theta specialization,” but the comments should say that explicitly. Otherwise the file overstates its correspondence to the paper.

I would add a comment like:

```lean
/- This module formalizes the theta-specialized kernel used downstream.
   The paper states several lemmas for a general phase Φ; those are not
   represented here as parameterized Lean theorems. -/
```

### 4. The jet-limit theorems omit the paper’s \(O(h^2)\) rate

The paper proves entrywise

\[
P_h A_h(T)P_h^\top=J(T)+O(h^2),
\]

and

\[
P_h C_h(T_1,T_2)P_h^\top=\frac1\pi N_{12}(T_1,T_2)+O(h^2),
\]

with fixed-separation scope and finite-power dependence on \(|T_1-T_2|^{-1}\).

Lean currently states only Tendsto limits:

```lean
same_point_jet_limit
cross_block_jet_limit
```

Those are weaker. They are not wrong, but they do not fully conform to the paper.

I would add separate rate theorems, even if left as `sorry`:

```lean
theorem same_point_jet_limit_rate (T : ℝ) :
    -- entrywise residual is O(h^2) as h → 0⁺
    True := by
  sorry

theorem cross_block_jet_limit_rate (T₁ T₂ : ℝ) (hT : T₁ ≠ T₂) :
    -- entrywise residual is O(h^2), with constant depending on a finite
    -- power of |T₁ - T₂|^{-1}
    True := by
  sorry
```

The actual Lean formulation can use `IsBigO`/`IsBigOWith` once you settle notation.

### 5. `same_point_gram_positivity` is weaker than the paper lemma

The paper’s lemma proves more than eventual positive definiteness. It also proves

\[
\lambda_{\min}(J(T))
=
\frac{2q(T)}{\pi}(1+o(1))
=
\frac1\pi\log\frac{T}{2\pi}(1+o(1)),
\]

and after raising the cutoff,

\[
\lambda_{\min}(J(T))\ge 1.
\]

Lean currently states only:

```lean
∃ T₀ : ℝ, 0 < T₀ ∧ ∀ T : ℝ, T₀ ≤ T → (J T).PosDef
```

That is a valid consequence, but it does not capture the whitening-relevant spectral floor.

A better formal target is a quadratic-form lower bound, avoiding eigenvalue machinery:

```lean
theorem same_point_gram_uniform_floor :
    ∃ T₀ : ℝ, 0 < T₀ ∧
      ∀ T : ℝ, T₀ ≤ T →
      ∀ x : Fin 2 → ℝ,
        x ⬝ᵥ (J T *ᵥ x) ≥ x ⬝ᵥ x := by
  sorry
```

This is equivalent to \(\lambda_{\min}(J(T))\ge1\) for real symmetric \(2\times2\) matrices and is more directly useful for whitening.

You can keep the current theorem, but rename it to something narrower:

```lean
same_point_gram_posdef_eventual
```

and reserve `same_point_gram_positivity` for the full paper-strength package.

## Smaller issues

The comments in `RiemannSiegelTheta.lean` say the principal branch differs from the continuous branch by a piecewise constant \(2\pi k(t)\). That should not be stated as a harmless fact unless a theorem proves where this holds and how derivatives are handled. Replace it with a warning.

The `q_eq_digamma` theorem is conditional on a slit-plane hypothesis. For the paper branch, no principal-log slit-plane condition should appear in the final theorem. The branch is holomorphic on \(\Re z>0\), and the derivative formula should be unconditional for real \(t\) once the branch is formalized.

The files use no mechanism-specific “Hardy” terminology, which is consistent with the current source-energy convention.

There is no Section 4 Lean file in the uploaded set. If Section 4 has now been merged in the paper, the Lean side does not yet cover finite-scale blocks \(G_{m,\pm}\), \(N_m(s)\), removable singularity \(N_m(0)=J(m)\), or whitening.

## Bottom line

The matrix side is in good shape:

\[
P_h,\quad J(T),\quad N_{12},\quad D_J,\quad \operatorname{tr}J,\quad \det J
\]

are normalized correctly. The algebraic same-point Gram criterion is also sound.

The structural blocker is the **principal-log definition of \(\theta\)**. That should be replaced or quarantined before these Lean files are considered conforming to the paper. After that, the main missing pieces are joint kernel continuity, \(O(h^2)\) rate statements, and the paper-strength spectral floor for \(J(T)\).
## User (2026-05-03 05:01:33)

review the latest progress. give patches to fix sorrys and fix anything incorrect/non-optimal

## Assistant (2026-05-03 05:01:48)

I’ll audit the three Lean modules against the merged Sections 2–3, patch nonconforming definitions or weak theorem targets, remove avoidable algebraic `sorry`s, and quarantine genuine analytic inputs as explicit stubs.

The main update is that the principal-branch issue is largely fixed, but `theta` may still be a hidden `def ... := sorry`; I’ll make analytic inputs explicit.

_Thought for 10m 59s_

Referee verdict: **latest Lean progress is structurally much better, but I would not merge it unchanged.** The main issue is that several analytic/Taylor inputs are still hidden as `sorry`, including the foundational definition

```lean
noncomputable def theta : ℝ → ℝ := sorry
```

That is not ideal Lean architecture. For this stage, it is cleaner to expose unresolved analytic content as explicit axioms/proof obligations, while keeping the algebraic matrix work as real Lean theorems.

I produced hardened patches:

- [RiemannSiegelTheta.referee-hardened.lean](sandbox:/mnt/data/RiemannSiegelTheta.referee-hardened.lean)
- [RiemannSiegelTheta diff](sandbox:/mnt/data/RiemannSiegelTheta.referee-hardened.diff)
- [LocalKernelJetNormalization.referee-hardened.lean](sandbox:/mnt/data/LocalKernelJetNormalization.referee-hardened.lean)
- [LocalKernelJetNormalization diff](sandbox:/mnt/data/LocalKernelJetNormalization.referee-hardened.diff)
- [JetLimitLocalBlocks.referee-hardened.lean](sandbox:/mnt/data/JetLimitLocalBlocks.referee-hardened.lean)
- [JetLimitLocalBlocks diff](sandbox:/mnt/data/JetLimitLocalBlocks.referee-hardened.diff)
- [Combined Lean diff](sandbox:/mnt/data/lean-sections23.referee-hardened.combined.diff)

I could not compile: there is no `lean` or `lake` executable available in the container. This is therefore a structural/mathematical patch, not a kernel-certified patch.

## Main fixes

### 1. Replaced hidden `theta := sorry`

The submitted file still had:

```lean
noncomputable def theta : ℝ → ℝ := sorry
```

I replaced this with:

```lean
constant theta : ℝ → ℝ
```

This is more honest. The current Lean development does not yet construct the continuous holomorphic-branch Riemann–Siegel phase; therefore `theta` should be an explicit primitive, not a fake definition backed by `sorry`.

### 2. Quarantined the principal branch more carefully

The file already improved the principal-branch issue, but one comment still overclaimed that `thetaPrincipal` equals `theta` modulo a piecewise constant. I weakened this.

The patched wording says no global equality or derivative statement is asserted for the principal-branch expression. That matters because the paper’s active \(\theta\) is the continuous branch from the holomorphic \(\log\Gamma\), while

```lean
Complex.log (Complex.Gamma ...)
```

is the principal branch and is not derivative-safe at branch jumps.

### 3. Turned heavyweight analytic inputs into explicit axioms

I changed the remaining analytic `sorry`s in `RiemannSiegelTheta` into explicit axioms:

```lean
axiom theta_differentiableAt ...
axiom theta_derivative_asymptotics ...
axiom theta_derivative_asymptotics_dyadic ...
```

This does **not** prove the analytic content. It makes the axiom budget visible. That is better for this draft than hiding the same content inside theorem bodies with `sorry`.

### 4. Added the dyadic lower-bound interface

The paper’s retained packets use the dyadic condition

\[
I_T \subset [T/2,2T].
\]

The latest Lean file still leaned heavily on the surrogate window `[T - 1, T + 1]`. I added:

```lean
theorem phase_derivative_lower_bound_dyadic :
    ∃ T₀ C : ℝ, 0 < T₀ ∧ 0 ≤ C ∧
    ∀ T t : ℝ, T₀ ≤ T → T / 2 ≤ t → t ≤ 2 * T →
    q t ≥ (1/2) * Real.log (T / (4 * Real.pi)) - C / T^2
```

and changed `analytic_bounds_eventual` in `JetLimitLocalBlocks` to consume the dyadic version.

This is more conforming with the paper.

### 5. Made diagonal Taylor inputs explicit in `LocalKernelJetNormalization`

The following were still `sorry`:

```lean
phase_kernel_joint_diagonal_limit
phase_kernel_diagonal_partial_x
phase_kernel_diagonal_partial_y
phase_kernel_diagonal_partial_xy
```

These are exactly the local Taylor/factored-Taylor inputs from Section 2. I converted them into explicit axioms rather than unfinished theorem bodies.

I also added:

```lean
theorem phase_kernel_diagonal_limit_theta
```

which uses the new smoothness input

```lean
theta_differentiableAt
```

to specialize the one-variable diagonal limit to the actual theta phase.

### 6. Made jet-limit Taylor inputs explicit in `JetLimitLocalBlocks`

The following were still `sorry`:

```lean
same_point_jet_limit
cross_block_jet_limit
same_point_jet_limit_rate
cross_block_jet_limit_rate
```

I converted these into explicit axioms. These are not algebraic one-liners; they are the Section 3 Taylor/conjugation estimates. Treating them as named inputs is cleaner until their Taylor proofs are formalized.

### 7. Hardened the uniform spectral floor

The current file had:

```lean
theorem same_point_gram_uniform_floor : ... := by
  sorry
```

with a complicated SOS proof sketch. I changed this to an explicit axiom:

```lean
axiom same_point_gram_uniform_floor :
    ∃ T₀ : ℝ, 0 < T₀ ∧
      ∀ T : ℝ, T₀ ≤ T →
      ∀ x : Fin 2 → ℝ,
        x ⬝ᵥ ((J T) *ᵥ x) ≥ x ⬝ᵥ x
```

This is the whitening-relevant strengthening of eventual positive definiteness. It should eventually be proved from theta asymptotics after raising the cutoff, but it should not remain as an unfinished theorem body.

## What remains mathematically good

The following parts are structurally correct and conforming:

- `pointToJetTransform` uses the correct Gram-normalized matrix.
- `J(T)` has the correct entries.
- `N12(T₁,T₂)` has the correct sign convention and omits the outer \(1/\pi\), so the limit target is `(1 / Real.pi) • N12`.
- `D_J(T)` is correct.
- `J_trace` and `J_det` have the correct coefficients, including the determinant denominator \(12\pi^2\).
- `algebraic_gram_criterion` is mathematically the right theorem.
- `D_J_lower_bound` is mathematically sound under \(q\ge2\), \(|q'|\le1\), \(|q''|\le1\).
- `same_point_gram_posdef_eventual` has the right proof structure: analytic bounds → determinant positivity → algebraic Gram criterion.

## Current formal status after patch

The hardened files contain **no textual `sorry` occurrences**. The remaining unproved content is exposed as axioms.

That means the Lean development is now closer to a clean “paper formalization map”:

- **Axioms:** analytic phase construction, theta asymptotics, diagonal Taylor facts, jet-limit Taylor facts, uniform spectral floor.
- **Lean theorems:** algebraic matrix identities, determinant/trace formulas, algebraic positivity criterion, eventual positive definiteness from stated analytic bounds.

This is the right separation for now. The next useful Lean target is to prove the easy algebraic spectral-floor lemma from coarse bounds \(q\ge5\), \(|q'|\le1\), \(|q''|\le1\), then reduce the remaining `same_point_gram_uniform_floor` axiom to only the analytic statement that those bounds hold eventually.
## User (2026-05-03 08:26:12)

does anything from the lean need to be backported to the paper? perhaps a clarifying note about theta?

## Assistant (2026-05-03 08:26:33)

I’ll compare the current paper’s theta/phase wording with the Lean audit and propose only minimal paper-facing clarifications, not Lean-internal scaffolding.

_Thought for 4m 47s_

Yes. The main Lean-to-paper backport is a **theta branch clarification**.

The paper already defines \(\theta\) correctly using the holomorphic branch \(L(z)=\log\Gamma z\) on \(\Re z>0\), normalized to be real on \(x>0\). The Lean audit exposed one potential ambiguity: readers or formalizers may accidentally replace this by the principal logarithm of \(\Gamma(z)\), which is not derivative-safe. The §2 numerical script already treats the intended convention as “\(L\) is the holomorphic branch of \(\log\Gamma z\) on \(\Re z>0\)” and compares it with `siegeltheta` only as a numerical regression check. 

I made a minimal backport patch:

- [Theta branch backport patch](sandbox:/mnt/data/rh_rebuild_theta_branch_backport.diff)
- [Patched TeX file](sandbox:/mnt/data/rh_rebuild_theta_branch_backport.tex)

What it changes:

1. Adds a remark immediately after `Definition~\ref{def:riemann-siegel-phase}`:

```latex
\begin{remark}[Branch convention for the Riemann--Siegel phase]
...
The branch \(L\) ... is the holomorphic logarithm of \(\Gamma\)
on the half-plane \(\Re z>0\), not the principal logarithm applied
pointwise to \(\Gamma(z)\).
...
A discontinuous branch, such as a principal-branch representative with
jumps, is not part of the definition and cannot be used for derivative
identities.
\end{remark}
```

2. Changes the theta-asymptotics proof line from

```latex
after truncating \(\log\Gamma z\) ...
```

to

```latex
after truncating \(L(z)\) ...
```

This prevents a referee from reading the proof as using an unspecified branch of \(\log\Gamma\).

3. Removes two remaining legacy “Hardy-curvature” strings and replaces them with generic **source-energy** wording, consistent with your current terminology rule.

I would **not** backport the Lean choice of treating `theta` as an abstract constant. That is a Lean engineering move to avoid principal-branch formalization trouble. In the paper, the constructive holomorphic-branch definition is preferable and more professional. The right paper fix is just the branch-convention remark above.
