#!/usr/bin/env python3
"""
b2_canonical.py -- canonical gamma curvature term B_2(t).

The completed-phase background contribution to q''_can(t). This module is the
single source of truth for B_2 across agent2 (and any other agent that wants
to import it). Treat it as frozen: do not edit without coordination.

Definition (canonical handoff):

    B_2(t) = theta'''(t) = -(1/8) Re psi^(2)(1/4 + i t/2),

where theta is the Riemann-Siegel theta function and psi^(2) is the second
polygamma function.

Asymptotic expansion for large t:

    B_2(t) = -1/(2 t^2) - 1/(8 t^4) - 7/(64 t^6) + O(t^-8).

The leading 1-term asymptotic agrees with the exact polygamma value to
~3e-4 relative error at t=27 and below 1e-5 above t=200. The 3-term
expansion agrees to ~1e-7 at t=27 and below 1e-10 above t=100. Use
the leading approximation for pilot work and the 3-term version when
near-exact agreement is wanted at negligible cost. Run-as-script
reproduces the validation table.

Public API:
  B2_exact(t, dps=50)            - exact via mpmath polygamma
  B2_fast(t, dps=50)             - leading asymptotic for t >= cutoff, else exact
  B2_fast_3term(t, dps=50)       - 3-term asymptotic for t >= cutoff, else exact
  B2_array(xs, dps=30, mode=...) - vectorized; mode="leading"|"3term"
  B2_array_cached(xs, dps=30, mode=...)
                                 - process-local cache; reuse across sweeps

Default policy for all callers:

    B_2 should be included by default in every zero-side proxy / canonical
    scan. Diagnostic toggling is allowed only for measuring B2_drift_rel; a
    B2-only object is never a valid Gate-1 candidate on its own.
"""

import math
from typing import Dict, Tuple

import numpy as np
import mpmath as mp


# Centers above this height use the closed-form asymptotic; centers below
# fall back to mpmath. The cutoff was chosen so the 1-term asymptotic
# is accurate to better than 1e-4 relative at and above the cutoff
# (see validation table).
B2_ASYMPTOTIC_CUTOFF = 50.0


def B2_exact(t: float, dps: int = 50) -> float:
    """Exact B_2(t) = -(1/8) Re psi^(2)(1/4 + i t/2) via mpmath."""
    mp.mp.dps = dps
    z = mp.mpc(mp.mpf("0.25"), mp.mpf(t) / 2)
    return float(-mp.re(mp.polygamma(2, z)) / 8.0)


def _b2_leading(t: float) -> float:
    return -0.5 / (t * t)


def _b2_3term(t: float) -> float:
    t2 = t * t
    t4 = t2 * t2
    t6 = t4 * t2
    return -1.0 / (2.0 * t2) - 1.0 / (8.0 * t4) - 7.0 / (64.0 * t6)


def B2_fast(t: float, dps: int = 50) -> float:
    """Leading-order asymptotic for t >= cutoff; exact polygamma below."""
    if t >= B2_ASYMPTOTIC_CUTOFF:
        return _b2_leading(t)
    return B2_exact(t, dps=dps)


def B2_fast_3term(t: float, dps: int = 50) -> float:
    """3-term asymptotic for t >= cutoff; exact polygamma below."""
    if t >= B2_ASYMPTOTIC_CUTOFF:
        return _b2_3term(t)
    return B2_exact(t, dps=dps)


def B2_array(xs: np.ndarray, dps: int = 30, mode: str = "leading") -> np.ndarray:
    """Vectorized B_2 over a grid.

    Asymptotic where xs >= cutoff (`mode = "leading"` for the 1-term form
    or `"3term"` for the 3-term form), else exact mpmath polygamma.
    """
    out = np.empty_like(xs, dtype=float)
    mask_large = xs >= B2_ASYMPTOTIC_CUTOFF
    if mask_large.any():
        large = xs[mask_large]
        if mode == "leading":
            out[mask_large] = -0.5 / (large * large)
        elif mode == "3term":
            t2 = large * large
            t4 = t2 * t2
            t6 = t4 * t2
            out[mask_large] = -1.0 / (2.0 * t2) - 1.0 / (8.0 * t4) - 7.0 / (64.0 * t6)
        else:
            raise ValueError(f"unknown mode: {mode!r}")
    if not mask_large.all():
        small_idx = np.where(~mask_large)[0]
        for i in small_idx:
            out[i] = B2_exact(float(xs[i]), dps=dps)
    return out


# Process-local FIFO cache. Same xs grid is reused across stability_W /
# stability_kappa / B2-toggle / cutoff-toggle / density-toggle variants of
# every interval_metrics call; only stability_nquad changes the grid shape.
# Cache hit avoids redundant polygamma sweeps for low-t centers where the
# asymptotic does not fire.
_B2_CACHE: Dict[Tuple[float, float, int, int, str], np.ndarray] = {}
_B2_CACHE_MAX = 4096


def B2_array_cached(xs: np.ndarray, dps: int = 30, mode: str = "leading") -> np.ndarray:
    if len(xs) == 0:
        return np.empty(0, dtype=float)
    key = (
        round(float(xs[0]), 9),
        round(float(xs[-1]), 9),
        int(len(xs)),
        int(dps),
        str(mode),
    )
    cached = _B2_CACHE.get(key)
    if cached is not None and cached.shape == xs.shape:
        return cached
    result = B2_array(xs, dps=dps, mode=mode)
    if len(_B2_CACHE) >= _B2_CACHE_MAX:
        _B2_CACHE.pop(next(iter(_B2_CACHE)))
    _B2_CACHE[key] = result
    return result


def _validation_table():
    """Reproduce the canonical handoff validation table (section 6)."""
    rows = [27.7179, 109.099, 171.662, 199.640, 308.664]
    print(
        f"{'m_0':>10}  {'B2_exact':>22}  {'-1/(2 m_0^2)':>22}  "
        f"{'rel_err_lead':>14}  {'B2_3term':>22}  {'rel_err_3term':>14}"
    )
    for m0 in rows:
        b_ex = B2_exact(m0, dps=50)
        b_lead = _b2_leading(m0)
        b_3 = _b2_3term(m0)
        e_lead = abs(b_lead - b_ex) / abs(b_ex)
        e_3 = abs(b_3 - b_ex) / abs(b_ex)
        print(
            f"{m0:>10.4f}  {b_ex:>22.13e}  {b_lead:>22.13e}  "
            f"{e_lead:>14.4e}  {b_3:>22.13e}  {e_3:>14.4e}"
        )


if __name__ == "__main__":
    _validation_table()
