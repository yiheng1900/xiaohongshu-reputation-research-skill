#!/usr/bin/env python3
"""Validate and summarize a normalized Xiaohongshu reputation dataset.

The script intentionally uses only the Python standard library so it can run in
most Codex workspaces without dependency setup.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ALIASES = {
    "sample_id": ["序号", "sample_id", "id", "样本ID"],
    "source_type": ["来源类型", "source_type"],
    "note_title": ["笔记标题", "note_title", "title"],
    "url": ["链接", "url", "note_url", "source_url"],
    "published_at": ["发布时间", "published_at", "publish_time"],
    "collected_at": ["采集时间", "collected_at", "collection_time"],
    "city_store": ["城市 / 门店信息", "城市/门店信息", "城市门店", "city_store"],
    "account_type": ["账号类型", "account_type"],
    "user_stage": ["用户阶段", "user_stage"],
    "sentiment": ["情绪倾向", "sentiment"],
    "dimensions": ["评价维度", "dimensions", "dimension"],
    "evidence_text": ["原文关键证据", "evidence_text", "evidence"],
    "comment_context": ["评论区有价值信息", "comment_context"],
    "suspected_ad": ["是否疑似广告或软文", "suspected_ad", "ad_flag"],
    "authenticity_level": ["真实性等级", "authenticity_level", "evidence_level"],
    "valid_sample": ["是否有效样本", "valid_sample", "is_valid"],
    "core_sample": ["是否核心样本", "core_sample", "is_core"],
}

REQUIRED = [
    "sample_id",
    "source_type",
    "note_title",
    "url",
    "published_at",
    "collected_at",
    "city_store",
    "account_type",
    "user_stage",
    "sentiment",
    "dimensions",
    "evidence_text",
    "comment_context",
    "suspected_ad",
    "authenticity_level",
]

ALLOWED = {
    "source_type": {"笔记", "评论", "回复评论"},
    "sentiment": {"正面", "中性", "负面", "混合"},
    "suspected_ad": {"是", "否", "不确定"},
    "authenticity_level": {"A", "B", "C", "D"},
}

TRUTHY = {"是", "true", "1", "yes", "y", "valid", "有效", "核心"}
FALSY = {"否", "false", "0", "no", "n", "invalid", "无效", "非核心"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, help="Normalized CSV dataset")
    parser.add_argument("--json-out", type=Path, help="Write summary JSON")
    parser.add_argument("--max-examples", type=int, default=20, help="Max validation examples to print")
    return parser.parse_args()


def find_header(fieldnames: list[str], canonical: str) -> str | None:
    aliases = ALIASES[canonical]
    for alias in aliases:
        if alias in fieldnames:
            return alias
    normalized = {re.sub(r"\s+", "", name).lower(): name for name in fieldnames}
    for alias in aliases:
        key = re.sub(r"\s+", "", alias).lower()
        if key in normalized:
            return normalized[key]
    return None


def clean(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def split_dimensions(value: str) -> list[str]:
    parts = re.split(r"[;；,，、|/]+", value)
    return [part.strip() for part in parts if part.strip()]


def boolish(value: str) -> bool | None:
    normalized = value.strip().lower()
    if normalized in TRUTHY:
        return True
    if normalized in FALSY:
        return False
    return None


def infer_valid(row: dict[str, str]) -> bool:
    explicit = boolish(row.get("valid_sample", ""))
    if explicit is not None:
        return explicit
    has_evidence = bool(row.get("evidence_text"))
    is_relevant_level = row.get("authenticity_level") in {"A", "B", "C"}
    return has_evidence and is_relevant_level


def infer_core(row: dict[str, str], valid: bool) -> bool:
    explicit = boolish(row.get("core_sample", ""))
    if explicit is not None:
        return explicit
    return (
        valid
        and row.get("authenticity_level") in {"A", "B", "C"}
        and row.get("suspected_ad") != "是"
    )


def pct(count: int, denominator: int) -> float:
    return round(count * 100 / denominator, 1) if denominator else 0.0


def main() -> int:
    args = parse_args()
    if not args.csv_path.exists():
        print(f"[ERROR] CSV not found: {args.csv_path}", file=sys.stderr)
        return 2

    with args.csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            print("[ERROR] CSV has no header row", file=sys.stderr)
            return 2

        header_map = {canonical: find_header(reader.fieldnames, canonical) for canonical in ALIASES}
        inferred_valid_flag = header_map.get("valid_sample") is None
        inferred_core_flag = header_map.get("core_sample") is None
        missing = [field for field in REQUIRED if header_map.get(field) is None]
        rows: list[dict[str, str]] = []
        issues: list[str] = []

        for row_number, raw in enumerate(reader, start=2):
            row = {
                canonical: clean(raw.get(source)) if source else ""
                for canonical, source in header_map.items()
            }
            rows.append(row)

            for field, allowed_values in ALLOWED.items():
                value = row.get(field, "")
                if value and value not in allowed_values:
                    issues.append(
                        f"Row {row_number}: invalid {field}={value!r}; allowed={sorted(allowed_values)}"
                    )

            if not row.get("url"):
                issues.append(f"Row {row_number}: missing source URL")
            if not row.get("evidence_text"):
                issues.append(f"Row {row_number}: missing evidence text")

    source_counts: Counter[str] = Counter()
    sentiment_counts: Counter[str] = Counter()
    evidence_counts: Counter[str] = Counter()
    dimension_counts: Counter[str] = Counter()
    account_counts: Counter[str] = Counter()
    stage_counts: Counter[str] = Counter()
    ad_counts: Counter[str] = Counter()

    valid_count = 0
    core_count = 0
    core_rows: list[dict[str, str]] = []

    for row in rows:
        valid = infer_valid(row)
        core = infer_core(row, valid)
        if valid:
            valid_count += 1
        if core:
            core_count += 1
            core_rows.append(row)

        source_counts[row.get("source_type") or "空值"] += 1
        evidence_counts[row.get("authenticity_level") or "空值"] += 1
        account_counts[row.get("account_type") or "空值"] += 1
        stage_counts[row.get("user_stage") or "空值"] += 1
        ad_counts[row.get("suspected_ad") or "空值"] += 1

    for row in core_rows:
        sentiment_counts[row.get("sentiment") or "空值"] += 1
        for dimension in split_dimensions(row.get("dimensions", "")):
            dimension_counts[dimension] += 1

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "csv_path": str(args.csv_path),
        "total_rows": len(rows),
        "valid_samples": valid_count,
        "core_samples": core_count,
        "valid_sample_inferred": inferred_valid_flag,
        "core_sample_inferred": inferred_core_flag,
        "missing_required_columns": missing,
        "issues_count": len(issues),
        "issues_preview": issues[: args.max_examples],
        "source_type_counts": dict(source_counts.most_common()),
        "sentiment_counts_core": dict(sentiment_counts.most_common()),
        "sentiment_percent_core": {
            key: pct(value, core_count) for key, value in sentiment_counts.most_common()
        },
        "authenticity_counts_all": dict(evidence_counts.most_common()),
        "account_type_counts_all": dict(account_counts.most_common()),
        "user_stage_counts_all": dict(stage_counts.most_common()),
        "suspected_ad_counts_all": dict(ad_counts.most_common()),
        "dimension_counts_core": dict(dimension_counts.most_common()),
        "dimension_percent_core": {
            key: pct(value, core_count) for key, value in dimension_counts.most_common()
        },
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if missing:
        print(f"[WARN] Missing required columns: {', '.join(missing)}", file=sys.stderr)
    if inferred_valid_flag:
        print("[WARN] valid sample count was inferred because 是否有效样本/valid_sample is missing", file=sys.stderr)
    if inferred_core_flag:
        print("[WARN] core sample count was inferred because 是否核心样本/core_sample is missing", file=sys.stderr)
    if issues:
        print(f"[WARN] Found {len(issues)} row-level issues; inspect issues_preview", file=sys.stderr)

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
