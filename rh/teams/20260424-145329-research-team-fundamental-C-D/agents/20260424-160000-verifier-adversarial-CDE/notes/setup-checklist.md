# Setup checklist

Verifier: `20260424-160000-verifier-adversarial-CDE`

Read on 2026-04-24 initial setup:

- `rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-verifier-adversarial-C-D/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-145500-verifier-source-C-D/report.md`

Read on 2026-04-24 after five continuation deposits landed:

- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-C-fiber-selection/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-D-odd-block-state/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-explorer-affine-bundle-holonomy/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-gap-closer-E-finite-core-transfer/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-160000-explorer-incidence-lower-model/report.md`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:168-206`
- `rh/teams/20260424-145329-research-team-fundamental-C-D/attempts.tsv:13-18`

Continuation deposits requested by team lead:

- `agents/20260424-160000-gap-closer-C-fiber-selection/report.md` — present; C-FS1--C-FS4 reduction, C-FS2/C-FS3 live.
- `agents/20260424-160000-gap-closer-D-odd-block-state/report.md` — present; transform-level `\mathscr O_D^{(N)}` isolated, state-locality/holonomy missing.
- `agents/20260424-160000-gap-closer-E-finite-core-transfer/report.md` — present; `E_1` reduced to `D_3=D_5^{\mathfrak f}=\overline D_7=0` or inhomogeneous rank theorem.
- `agents/20260424-160000-explorer-corrected-package-object/report.md` — waiting; required before final six-report adversarial review.
- `agents/20260424-160000-explorer-affine-bundle-holonomy/report.md` — present; ordinary two-section affine holonomy is base-controlled, but relational/provenance data may survive.
- `agents/20260424-160000-explorer-incidence-lower-model/report.md` — present; incidence gives zero/affine constraints, not sign/tail lower control.

Pinned adversarial kill conditions:

- C dies if `B(m,\kappa)` survives or if scalar normalization / regularity is used as a substitute for diagonal merger.
- D dies if hidden `\Phi_K`-visible state survives beyond a patchwise septic proxy, or if the claim is not transform-level modulo `\ker\Phi_K`.
- E dies if it only restates the queue or lacks a contradiction-driving lower theorem replacing the pair-like model.

Updated attack order once corrected-package-object lands:

1. **C package object + fiber selection.** Review `explorer-corrected-package-object` together with `gap-closer-C-fiber-selection`; attack C-FS1 construction, C-FS2 no-extra-state, and C-FS3 diagonal merger. Try to build an analytic model with same reduced base and nonconstant `B(m,\kappa)`.
2. **D transform-level state-locality.** Review `gap-closer-D-odd-block-state` together with `explorer-affine-bundle-holonomy`; accept base-controlled one-pair holonomy only as a scoped negative, then attack whether relational/provenance or higher odd-order state can still affect `\mathscr O_D^{(N)}` outside `\ker\Phi_K`.
3. **E finite-core transfer.** Review `gap-closer-E-finite-core-transfer` together with `explorer-incidence-lower-model`; attack whether projected defects can be nonzero and whether any claimed lower theorem has sign/no-cancellation/tail control.

Current action: five continuation deposits are read, but full six-report adversarial review is intentionally withheld until `explorer-corrected-package-object/report.md` lands.
