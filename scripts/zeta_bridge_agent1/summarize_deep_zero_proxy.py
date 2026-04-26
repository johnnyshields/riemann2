#!/usr/bin/env python3
"""
Cross-band summarizer for the deep actual-zero proxy scan.

Inputs are pairs BAND=path.csv (band tag in {T1e3, T1e4, T1e5, ...}). Each CSV is
the output of gate1_zero_pilot.py; rows already carry status / tail_edge / B_eff /
J_max / tail_drift_rel / quad_drift_rel / Q.

For each band we:
  1. Drop rows with status in {reject_tail_edge, reject_tail_unstable, reject_quad_unstable}.
  2. Count "strict candidate" rows (Section 3 of the deep-scan brief):
        B_eff > 5
        J_max <= Q^-5
        tail_drift_rel <= 1e-3
        quad_drift_rel <= 1e-7
     i.e. simultaneous interval-flatness, finite-jet-flatness at scale Q^-5,
     and drift stability.
  3. Print the top-20 valid rows by B_eff with derived jet_ratio = J_max / Q^-5.
  4. Apply the verdict rules from Section 6: healthy / watch / candidate / serious-warning.

Note: serious-warning per Section 6 also requires a stricter rerun
(R_jet=16, nfit=96, nquad=512) reproducing the candidate behavior. This
summarizer reports candidate behavior; "serious" still requires that
follow-up rerun.

Usage:
    python summarize_deep_zero_proxy.py \
        T1e3=out/zero_proxy_T1e3.<hash>.csv \
        T1e4=out/zero_proxy_T1e4.<hash>.csv \
        T1e5=out/zero_proxy_T1e5.<hash>.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import sys
from collections import defaultdict
from typing import Iterable, List, Tuple


REJECT_STATUSES = {
    "reject_tail_edge",
    "reject_tail_unstable",
    "reject_quad_unstable",
}


def f(x) -> float:
    try:
        return float(x)
    except Exception:
        return float("nan")


def read_rows(path: str, band: str) -> List[dict]:
    rows = []
    with open(path, newline="") as fp:
        for r in csv.DictReader(fp):
            r["band"] = band
            rows.append(r)
    return rows


def is_strict_candidate(r: dict) -> bool:
    """Section 3 strict-candidate gate."""
    Q = f(r.get("Q"))
    J = f(r.get("J_max"))
    B = f(r.get("B_eff"))
    tail = f(r.get("tail_drift_rel"))
    quad = f(r.get("quad_drift_rel"))
    if not all(math.isfinite(x) for x in (Q, J, B, tail, quad)):
        return False
    if Q <= 1:
        return False
    qm5 = Q ** -5
    return (B > 5) and (J <= qm5) and (tail <= 1e-3) and (quad <= 1e-7)


def median(xs: Iterable[float]) -> float:
    arr = sorted(x for x in xs if math.isfinite(x))
    if not arr:
        return float("nan")
    n = len(arr)
    if n % 2:
        return arr[n // 2]
    return 0.5 * (arr[n // 2 - 1] + arr[n // 2])


def cluster_signature(r: dict) -> Tuple[str, float, float]:
    """Identify a "center cluster" by (center_type, rounded m0, c_I)."""
    return (str(r.get("center_type", "")),
            round(f(r.get("m0")), 2),
            round(f(r.get("c_I")), 6))


def candidate_verdict(rows: List[dict]) -> Tuple[str, dict]:
    """
    Apply Section 6 rules to a single band's rows.

    Returns (verdict, evidence_dict). Verdicts:
      - healthy:  no strict candidates, median B_eff < 0, top valid rows have J_max >> Q^-5
      - watch:    a few rows pass B_eff > 5 but fail jet condition or appear in only one kappa
      - candidate: stable cluster with B_eff>5, J_max<=Q^-5 across multiple c_I, multiple W,
                   at least two kappa values
      - serious_warning_pending: candidate behavior in this band; cross-band check + stricter
                                 rerun required to upgrade to "serious warning"
    """
    valid = [r for r in rows if r.get("status") not in REJECT_STATUSES]
    if not valid:
        return ("no_valid_rows", {"valid_count": 0})

    Bs = [f(r.get("B_eff")) for r in valid]
    median_B = median(Bs)

    strict = [r for r in valid if is_strict_candidate(r)]

    # Cluster check for "candidate" verdict
    clusters: dict = defaultdict(list)
    for r in strict:
        clusters[cluster_signature(r)].append(r)

    candidate_clusters = []
    for sig, cluster_rows in clusters.items():
        kappas = {round(f(r.get("kappa")), 6) for r in cluster_rows}
        Ws = {round(f(r.get("W_factor")), 6) for r in cluster_rows}
        c_Is = {round(f(r.get("c_I")), 6) for r in cluster_rows}
        if len(kappas) >= 2 and len(Ws) >= 2 and len(c_Is) >= 1:
            candidate_clusters.append((sig, len(cluster_rows), kappas, Ws, c_Is))

    evidence = {
        "valid_count": len(valid),
        "strict_count": len(strict),
        "median_B_eff": median_B,
        "candidate_clusters": len(candidate_clusters),
        "max_B_eff": max((b for b in Bs if math.isfinite(b)), default=float("nan")),
    }

    if not strict and median_B < 0:
        # Confirm top valid rows have J_max >> Q^-5
        top_valid = sorted(valid, key=lambda r: f(r.get("B_eff")), reverse=True)[:5]
        ratios = []
        for r in top_valid:
            Q = f(r.get("Q"))
            J = f(r.get("J_max"))
            if math.isfinite(Q) and Q > 1 and math.isfinite(J):
                ratios.append(J / (Q ** -5))
        evidence["top5_jet_ratios"] = ratios
        if all(rt > 1 for rt in ratios) and ratios:
            return ("healthy", evidence)
        return ("watch", evidence)

    if candidate_clusters:
        evidence["clusters_detail"] = [
            {"sig": sig, "n": n, "kappas": sorted(ks), "Ws": sorted(Ws), "c_Is": sorted(cIs)}
            for (sig, n, ks, Ws, cIs) in candidate_clusters[:5]
        ]
        return ("candidate", evidence)

    return ("watch", evidence)


def emit_top_table(band: str, valid: List[dict], top_n: int = 20) -> None:
    print(f"top {top_n} valid rows in {band}:")
    print(",".join([
        "band", "status", "center_type", "m0", "Q", "c_I", "kappa",
        "W_factor", "count", "E_I", "B_eff", "S_I", "J_max",
        "Q^-5", "jet_ratio", "tail", "quad", "tail_edge",
    ]))
    top = sorted(valid, key=lambda r: f(r.get("B_eff")), reverse=True)[:top_n]
    for r in top:
        Q = f(r.get("Q"))
        J = f(r.get("J_max"))
        qm5 = Q ** -5 if Q > 1 else float("nan")
        ratio = J / qm5 if math.isfinite(qm5) and qm5 != 0 else float("nan")
        print(",".join([
            band,
            r.get("status", ""),
            r.get("center_type", ""),
            r.get("m0", ""),
            r.get("Q", ""),
            r.get("c_I", ""),
            r.get("kappa", ""),
            r.get("W_factor", ""),
            r.get("local_zero_count", ""),
            r.get("E_I", ""),
            r.get("B_eff", ""),
            r.get("S_I", ""),
            r.get("J_max", ""),
            f"{qm5:.6e}",
            f"{ratio:.6e}",
            r.get("tail_drift_rel", ""),
            r.get("quad_drift_rel", ""),
            r.get("tail_edge", ""),
        ]))


def summarize(pairs: List[Tuple[str, str]]) -> None:
    all_rows: List[dict] = []
    by_band: dict = {}
    for band, path in pairs:
        if not os.path.exists(path):
            print(f"[warn] {band}: file not found: {path}")
            continue
        rows = read_rows(path, band)
        all_rows.extend(rows)
        by_band[band] = rows
        print(f"[load] {band}: {len(rows)} rows from {path}")

    print(f"\ntotal rows: {len(all_rows)}\n")

    band_verdicts: dict = {}
    for band, rows in by_band.items():
        print(f"=== {band} ===")
        valid = [r for r in rows if r.get("status") not in REJECT_STATUSES]
        rejected = len(rows) - len(valid)
        print(f"rows: {len(rows)}  valid: {len(valid)}  rejected: {rejected}")

        # Status breakdown
        status_counts: dict = defaultdict(int)
        for r in rows:
            status_counts[r.get("status", "")] += 1
        for s in sorted(status_counts):
            print(f"  status[{s}] = {status_counts[s]}")

        # Strict-candidate count
        strict = [r for r in valid if is_strict_candidate(r)]
        print(f"strict candidates (B_eff>5, J_max<=Q^-5, tail<=1e-3, quad<=1e-7): {len(strict)}")

        # tail_edge true count
        n_tail_edge = sum(1 for r in rows if str(r.get("tail_edge", "")).lower() in ("true", "1"))
        print(f"tail_edge=True rows: {n_tail_edge}")

        # Top-20 valid table
        emit_top_table(band, valid, top_n=20)
        print()

        verdict, evidence = candidate_verdict(rows)
        band_verdicts[band] = (verdict, evidence)
        print(f"verdict[{band}] = {verdict}")
        for k, v in evidence.items():
            if k == "clusters_detail":
                print(f"  {k}:")
                for c in v:
                    print(f"    {c}")
            else:
                print(f"  {k} = {v}")
        print()

    # Cross-band synthesis
    print("=== cross-band verdict ===")
    candidate_bands = [b for b, (v, _) in band_verdicts.items() if v == "candidate"]
    if len(candidate_bands) >= 2:
        print(f"serious_warning_pending: candidate behavior in bands: {candidate_bands}")
        print("  follow-up rerun required: R_jet=16, nfit=96, nquad=512")
    elif candidate_bands:
        print(f"single-band candidate: {candidate_bands[0]} (cross-band check needed)")
    else:
        watch_bands = [b for b, (v, _) in band_verdicts.items() if v == "watch"]
        if watch_bands:
            print(f"watch: {watch_bands}")
        else:
            print("healthy across bands")


def parse_pair(item: str) -> Tuple[str, str]:
    if "=" not in item:
        raise SystemExit(f"Bad pair {item!r}; expected BAND=path.csv")
    band, path = item.split("=", 1)
    return band.strip(), path.strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("items", nargs="+", help="BAND=path.csv pairs (e.g. T1e3=out/scan.csv)")
    args = ap.parse_args()
    pairs = [parse_pair(p) for p in args.items]
    summarize(pairs)


if __name__ == "__main__":
    main()
