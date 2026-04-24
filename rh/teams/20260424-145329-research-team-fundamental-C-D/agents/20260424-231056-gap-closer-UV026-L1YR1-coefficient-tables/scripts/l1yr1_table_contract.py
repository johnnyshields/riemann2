#!/usr/bin/env python3
"""Audit and validate the UV-026 L_1YR_1 coefficient-table input.

The script has two jobs.

1. Scan the cited paper/report sources for an explicit order <= 7 table block.
2. If a table JSON is supplied, validate that it contains enough data for the
   already-derived Sylvester/convolution gate.

It deliberately does not infer or fabricate the missing coefficients.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ORDER = 7
SIGNS = ["-", "+"]
TAGS = ["1", "2"]
MATRIX_SHAPE = [2, 2]


def sha1(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest().upper()


def line_window(path: Path, start: int, end: int) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [(idx, lines[idx - 1]) for idx in range(start, min(end, len(lines)) + 1)]


def contains_table_like_display(text: str, name_pattern: str) -> bool:
    """Return true only for an explicit finite coefficient assignment/table."""
    finite_sum = re.compile(
        name_pattern
        + r".{0,240}(?:\\sum_\{[^}]*0\s*(?:\\le|<=|\.{2}|\.\.)\s*[^}]*7|"
        + r"0\s*(?:\\le|<=)\s*[A-Za-z]\s*(?:\\le|<=)\s*7|"
        + r"\[[^\]]*0[^\]]*7[^\]]*\])",
        re.DOTALL,
    )
    return bool(finite_sum.search(text))


def source_audit(paper: Path, prior_reports: list[Path]) -> dict[str, Any]:
    windows = {
        "baseline_scaled_input": (2429, 2466),
        "kernel_linearity": (2628, 2784),
        "wip_target": (12617, 12714),
        "source_level_negative": (12098, 12331),
    }
    scan_text_parts: list[str] = []
    window_hits: dict[str, dict[str, Any]] = {}

    for name, (start, end) in windows.items():
        rows = line_window(paper, start, end)
        text = "\n".join(line for _, line in rows)
        scan_text_parts.append(text)
        window_hits[name] = {
            "path": str(paper),
            "line_range": [start, end],
            "mentions": {
                "D_Q": "\\mathfrak D_Q" in text,
                "Y_scaled_input": "Y_\\rho:=\\mathfrak D_Q" in text or "Y," in text,
                "bounded_baseline": "bounded baseline" in text or "bounded-baseline" in text,
                "M_i_5": "M_i^{[5]}" in text,
                "missing_lists": "[z^r]\\Lambda" in text or "[z^s]M_i^{[5]}" in text,
                "even_weight_negative": "even analytic function of the source weight" in text,
            },
        }

    for report in prior_reports:
        if report.exists():
            scan_text_parts.append(report.read_text(encoding="utf-8"))

    scan_text = "\n".join(scan_text_parts)
    explicit_table_checks = {
        "G_baseline_sqrt_or_invsqrt_order_le_7": contains_table_like_display(
            scan_text, r"G_\\pm\^\{\\\(0\\\).*?(?:-1/2|1/2)"
        ),
        "deltaG_lin_order_le_7": contains_table_like_display(
            scan_text, r"(?:\\delta\s*G_\{i,\\pm\}\^\{\\lin\}|H_\{i,\\pm\})"
        ),
        "M_i_5_order_le_7": contains_table_like_display(
            scan_text, r"M_i\^\{\[5\]\}"
        ),
        "Lambda_order_le_7": contains_table_like_display(
            scan_text, r"\\Lambda_\{i,\\pm\}"
        ),
    }

    return {
        "paper_sha1": sha1(paper),
        "window_hits": window_hits,
        "explicit_table_checks": explicit_table_checks,
        "table_block_found": any(explicit_table_checks.values()),
        "source_reduction": {
            "proved_from_source": [
                "The pre-whitening transfer uses the weighted input Y with delta N = mathfrak D_Q^{-1}Y.",
                "The source displays exact same-point and mixed block formulas and linear-in-kernel estimates.",
                "The WIP L_1YR_1 target names Lambda_{i,pm} and M_i^{[5]} and explicitly lists their coefficient arrays as missing.",
            ],
            "conditional": [
                "The only normalization compatible with the transfer variables is M_i^{[5]} = Gr_5(mathfrak D_Q(delta N_i^{lin})), unless a later theorem overrides the symbol.",
            ],
            "missing": [
                "[z^0..z^7] G_pm^{(0)}(z)^{1/2} and G_pm^{(0)}(z)^{-1/2}.",
                "[z^0..z^7] delta G_{i,pm}^{lin}(z) after the tagged one-atom kernels are fixed.",
                "[z^0..z^7] M_i^{[5]}(z) in the same B_7^f pre-Phi normalization.",
                "The two determinant identities against A_5^f(m).",
            ],
        },
    }


def required_schema() -> dict[str, Any]:
    coeff_keys = [str(i) for i in range(ORDER + 1)]
    return {
        "normalization": {
            "coordinate": "ordinary z coefficients before Phi_K",
            "fixed_sector_basis": ["I", "S"],
            "B7_fixed_sector": "pi_f [z^7]",
            "mixed_input_required": "scaled_Y = mathfrak D_Q(delta N_i^{lin}) before grade extraction",
            "order": ORDER,
        },
        "required_tables": {
            "G_sqrt": {"signs": SIGNS, "coefficients": coeff_keys, "matrix_shape": MATRIX_SHAPE},
            "G_invsqrt": {"signs": SIGNS, "coefficients": coeff_keys, "matrix_shape": MATRIX_SHAPE},
            "deltaG_lin": {"tags": TAGS, "signs": SIGNS, "coefficients": coeff_keys, "matrix_shape": MATRIX_SHAPE},
            "M5": {"tags": TAGS, "coefficients": coeff_keys, "matrix_shape": MATRIX_SHAPE},
            "A5_fixed": {"coordinates": ["u5", "v5"]},
        },
        "derived_outputs_enabled": [
            "Lambda_{i,pm}^{[0..7]} by the Sylvester equation",
            "C112^{L_1YR_1} and C122^{L_1YR_1} by the r+s+t=7 convolution",
            "determinants u112*v5-u5*v112 and u122*v5-u5*v122",
        ],
    }


def validate_matrix(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(row, list) and len(row) == 2 for row in value)
    )


def validate_table_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing: list[str] = []
    shape_errors: list[str] = []

    norm = data.get("normalization", {})
    if norm.get("B7_fixed_sector") != "pi_f [z^7]":
        missing.append("normalization.B7_fixed_sector must be 'pi_f [z^7]'")
    if norm.get("mixed_input") != "scaled_Y":
        missing.append("normalization.mixed_input must be 'scaled_Y'")

    for family in ["G_sqrt", "G_invsqrt"]:
        fam = data.get(family, {})
        for sign in SIGNS:
            sign_block = fam.get(sign, {})
            for r in range(ORDER + 1):
                key = str(r)
                if key not in sign_block:
                    missing.append(f"{family}.{sign}.{key}")
                elif not validate_matrix(sign_block[key]):
                    shape_errors.append(f"{family}.{sign}.{key}")

    for family in ["deltaG_lin"]:
        fam = data.get(family, {})
        for tag in TAGS:
            tag_block = fam.get(tag, {})
            for sign in SIGNS:
                sign_block = tag_block.get(sign, {})
                for r in range(ORDER + 1):
                    key = str(r)
                    if key not in sign_block:
                        missing.append(f"{family}.{tag}.{sign}.{key}")
                    elif not validate_matrix(sign_block[key]):
                        shape_errors.append(f"{family}.{tag}.{sign}.{key}")

    fam = data.get("M5", {})
    for tag in TAGS:
        tag_block = fam.get(tag, {})
        for r in range(ORDER + 1):
            key = str(r)
            if key not in tag_block:
                missing.append(f"M5.{tag}.{key}")
            elif not validate_matrix(tag_block[key]):
                shape_errors.append(f"M5.{tag}.{key}")

    a5 = data.get("A5_fixed", {})
    for key in ["u5", "v5"]:
        if key not in a5:
            missing.append(f"A5_fixed.{key}")

    return {
        "table_path": str(path),
        "table_sha1": sha1(path),
        "valid": not missing and not shape_errors,
        "missing": missing,
        "shape_errors": shape_errors,
    }


def exact_missing_theorem() -> str:
    return (
        "Finite-order normalized L_1YR_1 coefficient-table theorem: "
        "for the UV-025 tagged pre-whitening block B_2, in ordinary z and before Phi_K, "
        "display matrices S_{pm,r}, B_{pm,r}, H_{i,pm,r}, and M_{i,r}^{[5]} for "
        "0<=r<=7 such that G_pm^{(0)1/2}=sum S_{pm,r}z^r+O(z^8), "
        "G_pm^{(0)-1/2}=sum B_{pm,r}z^r+O(z^8), "
        "delta G_{i,pm}^{lin}=sum H_{i,pm,r}z^r+O(z^8), and "
        "M_i^{[5]}=Gr_5(mathfrak D_Q delta N_i^{lin})=sum M_{i,r}^{[5]}z^r+O(z^8). "
        "Using these tables, the Sylvester outputs Lambda_{i,pm}^{[0..7]} must give "
        "pi_f[z^7] of the two L_1YR_1 tag products in C A_5^f(m)."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", type=Path, required=True)
    parser.add_argument("--prior-report", type=Path, action="append", default=[])
    parser.add_argument("--table-json", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    audit = source_audit(args.paper, args.prior_report)
    result: dict[str, Any] = {
        "script": str(Path(__file__)),
        "script_sha1": sha1(Path(__file__)),
        "order": ORDER,
        "schema": required_schema(),
        "source_audit": audit,
        "exact_missing_theorem": exact_missing_theorem(),
    }
    if args.table_json:
        result["table_validation"] = validate_table_json(args.table_json)
    else:
        result["table_validation"] = {
            "valid": False,
            "reason": "no coefficient-table JSON was supplied",
        }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
