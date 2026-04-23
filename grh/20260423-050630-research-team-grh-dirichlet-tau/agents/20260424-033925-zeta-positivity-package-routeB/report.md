# Claim

The same-point positivity package is only partially separable from the zeta source package.

What is genuinely separable in the current draft is the local matrix-stability shell:

1. denominator comparability gives omitted-smooth holomorphy on the microscopic disk;
2. block-perturbation and baseline-variation estimates reduce positivity on the disk to a baseline spectral-gap input at `s=0`;
3. holomorphic functional calculus then gives the inverse-square-root whitening.

But the positivity package is not source-free. It still imports three source-dependent inputs:

1. source-normalized background/value data, namely `B_\zeta(m)` and `S(m)=q_\zeta(m)-B_\zeta(m)`;
2. the fixed-core source decomposition `q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}` used to define the corrected phase and the whitened object;
3. the identification of the first whitening derivative with the source-side value coefficient `A_{\val}` associated to that core/background normalization.

So the safe verdict is:

- proved: positivity is separable from denominator holomorphy alone;
- conditional: positivity is still tied to source-normalized background/core data in the manuscript interface;
- missing: a theorem-level abstraction showing that the baseline nondegeneracy and first-order value-channel identification can be stated and proved without leaning on the zeta source package.

Accordingly, extracting a standalone lemma package is safe only at blueprint level: as an abstract `if local holomorphy + baseline same-point gap + source-normalized first variation hold, then holomorphic whitening is defined` interface. It is not yet safe as a fully standalone theorem package genuinely independent of the zeta source package.

# Status

conditional

# Evidence

The manuscript itself separates denominator holomorphy from positivity. Proposition `Microscopic denominator comparability and omitted-smooth holomorphy` proves only that the omitted-zero sums and required derivatives extend holomorphically on `|s|<\rho_0/Q`; its endpoint is holomorphy of `T_{\far}(t_\pm)` and `g_{\sm}(t_\pm)`, not positivity of the same-point blocks. See `paper/proof_of_rh.tex:856-946`.

The actual positivity step is Proposition `Corrected finite-s holomorphic whitening`. Its proof uses three ingredients beyond denominator holomorphy: the same-point perturbation bound, the baseline variation bound, and the baseline spectral-gap input `\lambda_{\min}(G_{m,\pm}^{(0)}(0))\gg Q`. Only after those are combined does the draft conclude that `G_{m,\pm}^{\corr}(s)` remain uniformly positive definite and hence admit holomorphic inverse square roots. See `paper/proof_of_rh.tex:1392-1458`, especially `1418-1457`.

That already shows one non-separability boundary: positivity is not automatic from the denominator package. The paired-slot and corrected-whitening notes state the same boundary in note form: the minimal admissibility package contains microscopic holomorphy and same-point positivity/nondegeneracy as distinct clauses, and the corrected-whitening bundle lists positive same-point blocks as its own front-end ingredient. See `paired_slot_hypotheses.md:12-23,31-52` and `corrected_whitening_transport.md:11-22`.

The more important question here is whether positivity can be split off from the zeta source package itself. On the current manuscript interface, not cleanly. The zeta-side decomposition introduces the source-normalized scalar data

`q(t)=B_\zeta(t)+S(t)`, `S(m)=q_\zeta(m)-B_\zeta(m)`

and the later fixed-core decomposition refines this to

`q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}`.

Those data are not optional bookkeeping: they define the corrected phase `\Phi_{\corr,R}`, the corrected same-point and mixed blocks, and the whitened local object whose positivity is being studied. See `paper/proof_of_rh.tex:271-300` and `1497-1588`.

The whitening decomposition then expands the corrected block around the background value parameter `S(m)=0` and identifies the first derivative with the source-side value-channel matrix `A_{\val}(m,\sigma)` associated to the fixed core `\mathcal C`. That is exactly where the positivity package still touches the source package: the object being whitened is organized around source/background normalization, and its linearized leading direction is not abstractly any first variation, but the source-derived `A_{\val}`. See `paper/proof_of_rh.tex:1531-1621`, especially `1540-1549` and `1590-1606`.

The explicit `A_{\val}` section depends on background source data in a second way. The formula is written in the constant-background symmetric regime with `B:=B_\zeta(m)` and `x=B\sigma`; the same-point jet Gram matrix being differentiated is the background block at `B+\alpha`. So even before the later corrected-whitening argument, the leading whitening derivative is already encoded using source-normalized background data, not a source-free abstract positivity lemma. See `paper/proof_of_rh.tex:426-565`.

There is also a second nontrivial source-facing residue in the baseline nondegeneracy input. In the whitening proof, the spectral gap at `s=0` is simply invoked. Elsewhere in the pair-local quotient discussion, the draft treats `x_1\neq x_2` and background same-point nondegeneracy as explicit structural assumptions, not formal consequences of denominator holomorphy. See `paper/proof_of_rh.tex:5996-6084`. So the manuscript currently does not provide a source-independent theorem that the baseline same-point block has the required gap; it imports that nondegeneracy from the source-normalized baseline object.

Putting these together gives the honest split:

- proved: one can conceptually separate denominator holomorphy from same-point positivity;
- conditional: the positivity package still uses source/background/core normalization to define the corrected object and its leading value direction;
- missing: an abstract lemma package proving the baseline same-point gap and the first-order value-channel identification without citing the zeta source framework.

Honest verdict:

- safe as extraction blueprint: yes;
- safe as a theorem-level standalone lemma package independent of the zeta source package: no;
- exact residue: source-normalized background scalar `B_\zeta`, value scalar `S(m)`, fixed-core decomposition, and the identification of the first whitening derivative with `A_{\val}`.

# Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-300` (`q=B_\zeta+S`, `S(m)=q_\zeta(m)-B_\zeta(m)`, curvature estimate provenance)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:426-565` (`A_{\val}` in the constant-background symmetric regime with `B:=B_\zeta(m)`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946` (`Microscopic denominator comparability and omitted-smooth holomorphy`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:948-1143` (`Entry-by-entry perturbation estimate for the corrected same-point blocks`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1332-1458` (`Baseline same-point variation`; `Corrected finite-s holomorphic whitening`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1683` (`Corrected local deformation decomposition with fixed core`; `Core-stable cutoff compatibility`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5996-6084` (`background same-point block is nondegenerate`, `x_1\neq x_2`, `B(h)\not\equiv 0`)
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:12-23,31-52`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:11-22,24-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-37`

# Dependencies

- The manuscript's whitening interface in `paper/proof_of_rh.tex`, especially the decomposition of the corrected object around `S(m)=0` and the definition of `A_{\val}`.
- The note-level source-package conclusion that the source gap is a 2-step package: quotient/phase normalization plus one bundled localized source theorem.
- The prior positivity notes establishing that denominator comparability and same-point positivity are distinct local inputs.

# Strongest objection

One could object that I am conflating two different notions of `standalone`: maybe the intended extraction keeps `B_\zeta`, `S(m)`, and the fixed core as frozen parameters and only factors out the matrix-analytic whitening lemmas. Under that weaker notion, a standalone positivity package is already available. I agree with that limited reading. But under the stronger reading in the mission statement, namely separation from the zeta source package itself, the package is not cleanly standalone, because the current proof still defines its baseline object and first variation through source-normalized background/core data.

# Needed for promotion

- State an abstract whitening lemma package whose hypotheses are fully explicit: microscopic holomorphy, baseline same-point gap/nondegeneracy, and a named first-order value-channel direction.
- Prove that the baseline gap/nondegeneracy hypothesis follows from a source-independent local model, or else mark it permanently as an imported source-side assumption.
- Prove an abstract identification theorem showing when the first derivative of the whitened block equals the intended source scalar times a canonical matrix, instead of hardwiring `A_{\val}` through the zeta background normalization.
- Decide the paper-facing message conservatively: `standalone positivity package` is currently safe only as blueprint/interface language, not as a claim of theorem-level independence from the zeta source package.
