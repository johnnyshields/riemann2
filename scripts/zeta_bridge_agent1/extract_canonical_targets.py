#!/usr/bin/env python3
"""
Extract top proxy rows for canonical zero-side and AFE cross-checks.

Input:
    gate1_zero_pilot.py CSV from the 5k broad scan.

Output:
    Compact top-N target CSV sorted by B_eff descending after excluding rejected rows.

Usage:
    python extract_canonical_targets.py \
      --input out/zero_proxy_5k.<hash>.csv \
      --out out/canonical_targets_top50.csv \
      --top 50
"""

from __future__ import annotations

import argparse
import csv
import math


REJECT_STATUSES = {
    "reject_tail_edge",
    "reject_tail_unstable",
    "reject_quad_unstable",
}


KEEP_COLUMNS = [
    "rank",
    "target_id",
    "status",
    "center_type",
    "m0",
    "Q",
    "c_I",
    "kappa",
    "W_factor",
    "local_zero_count",
    "E_I",
    "S_I",
    "B_eff",
    "J_max",
    "J_rms",
    "Q_minus_5",
    "jet_ratio",
    "tail_drift_rel",
    "quad_drift_rel",
    "tail_edge",
]


def f(x, default=float("nan")):
    try:
        return float(x)
    except Exception:
        return default


def q_minus_5(Q: float) -> float:
    if not math.isfinite(Q) or Q <= 0:
        return float("nan")
    return Q ** -5


def load_rows(path: str) -> list[dict]:
    with open(path, newline="") as fp:
        return list(csv.DictReader(fp))


def valid_for_target_pack(row: dict) -> bool:
    status = row.get("status", "")
    if status in REJECT_STATUSES:
        return False
    if str(row.get("tail_edge", "")).lower() in {"true", "1"}:
        return False

    B = f(row.get("B_eff"))
    Q = f(row.get("Q"))
    E = f(row.get("E_I"))
    J = f(row.get("J_max"))
    tail = f(row.get("tail_drift_rel"))
    quad = f(row.get("quad_drift_rel"))

    return all(math.isfinite(x) for x in [B, Q, E, J, tail, quad])


def decorate(row: dict, rank: int) -> dict:
    Q = f(row.get("Q"))
    J = f(row.get("J_max"))
    qm5 = q_minus_5(Q)
    jet_ratio = J / qm5 if math.isfinite(qm5) and qm5 != 0 else float("nan")

    target_id = f"T{rank:03d}_{row.get('center_type','unknown')}_{f(row.get('m0')):.6f}"

    out = {
        "rank": rank,
        "target_id": target_id,
        "status": row.get("status", ""),
        "center_type": row.get("center_type", ""),
        "m0": row.get("m0", ""),
        "Q": row.get("Q", ""),
        "c_I": row.get("c_I", ""),
        "kappa": row.get("kappa", ""),
        "W_factor": row.get("W_factor", ""),
        "local_zero_count": row.get("local_zero_count", ""),
        "E_I": row.get("E_I", ""),
        "S_I": row.get("S_I", ""),
        "B_eff": row.get("B_eff", ""),
        "J_max": row.get("J_max", ""),
        "J_rms": row.get("J_rms", ""),
        "Q_minus_5": f"{qm5:.12e}" if math.isfinite(qm5) else "",
        "jet_ratio": f"{jet_ratio:.12e}" if math.isfinite(jet_ratio) else "",
        "tail_drift_rel": row.get("tail_drift_rel", ""),
        "quad_drift_rel": row.get("quad_drift_rel", ""),
        "tail_edge": row.get("tail_edge", "False"),
    }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=50)
    args = ap.parse_args()

    rows = load_rows(args.input)
    valid = [r for r in rows if valid_for_target_pack(r)]
    valid_sorted = sorted(valid, key=lambda r: f(r.get("B_eff")), reverse=True)
    top = valid_sorted[: args.top]

    decorated = [decorate(r, i + 1) for i, r in enumerate(top)]

    with open(args.out, "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=KEEP_COLUMNS)
        writer.writeheader()
        writer.writerows(decorated)

    print(f"input rows: {len(rows)}")
    print(f"valid rows: {len(valid)}")
    print(f"wrote top {len(decorated)} targets to {args.out}")

    if decorated:
        print("\nTop 10:")
        print(",".join(KEEP_COLUMNS))
        for row in decorated[:10]:
            print(",".join(str(row.get(c, "")) for c in KEEP_COLUMNS))


if __name__ == "__main__":
    main()
