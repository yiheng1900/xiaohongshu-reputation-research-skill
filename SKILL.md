---
name: xiaohongshu-reputation-research
description: Run Xiaohongshu public reputation research workflows for brands, products, stores, categories, or services. Use when the user asks for 小红书口碑调研, 用户评价分析, 评论区反馈, 避坑/投诉/种草内容判断, raw evidence tables, management reports, HTML visualization, or Cloudflare Pages delivery for a Xiaohongshu-only study.
---

# Xiaohongshu Reputation Research

## Purpose

Execute a Xiaohongshu-only public opinion research workflow that preserves raw evidence, separates real user feedback from marketing content, and produces management-ready conclusions with traceable sample IDs and source links.

Treat this as a research operating procedure, not a generic scraping task. The goal is to answer what real users feel, where the evidence is strong or weak, and what operational actions follow from the data.

## Operating Rules

- Use only publicly accessible Xiaohongshu content. Do not bypass login walls, captchas, paywalls, privacy controls, or platform restrictions.
- Prefer Browser Use, Computer Use, or an available Xiaohongshu research connector for collection. If access is blocked, ask the user to complete the browser-side action or narrow the scope.
- Do not promise a target sample size before collection proves it is feasible. Report raw, valid, and core sample counts separately.
- Keep every key conclusion traceable to original sample rows by ID and link.
- Do not treat brand posts, store sales posts, influencer ads, or vague seed content as core口碑 evidence. Flag them as weak evidence or marketing context.
- Before deploying to Cloudflare Pages or publishing any URL, get explicit user confirmation.
- For Cloudflare deployment details, check current official Cloudflare docs before acting, because deployment commands and product recommendations can change.

## Workflow

0. **Strict three-question intake gate**: At the start of every new research request, use the fixed intake text in `references/intake.md`. The first sentence must be `你好，我是毅恒小红书品牌调研小助手。` The intake must collect exactly three required inputs: research theme, core question, and research depth (`标准版` or `深度版`). Do not add examples, do not rewrite the standard/deep descriptions, do not infer `标准版`, and do not generate keywords, research scope, or collection plans before all three inputs are explicit.
1. **Intake**: Ask only for missing variables after the three required inputs are complete. Read `references/intake.md` when the theme, depth, target sample size, region, time range, competitors, or output format is unclear.
2. **Research brief and plan**: Convert the intake into a reusable execution prompt plus research口径 for user confirmation. Read `references/intake.md` for the confirmation prompt and `references/research-plan.md` for keyword matrix, sample scope, login gate, and collection rules.
3. **Access gate**: For Xiaohongshu collection, ask the user to trigger `@电脑 / Computer Use` and use the local Chrome browser. Verify Xiaohongshu is logged in and that search results, note正文, and comments are visible. If access is blocked, pause and ask the user to complete login or browser-side verification. Do not enter collection until this is confirmed.
4. **Formal collection**: After login/access is confirmed, directly collect Xiaohongshu search results, note text, comments, and reply comments according to the confirmed keyword plan. Preserve source URLs, collection time, publish time when visible, original evidence text, and note/comment relationships.
5. **Raw data and evidence chain**: Save raw JSONL/CSV first, then normalized CSV/XLSX. Use `references/data-schema.md` for required fields and allowed values.
6. **Clean, dedupe, classify**: Classify account type, user stage, sentiment, dimensions, suspected advertising, authenticity level, valid sample flag, and core sample flag. Read `references/classification.md`.
7. **Validate counts**: Run `scripts/validate_xhs_dataset.py` on the normalized CSV before writing final conclusions. Fix schema, denominator, or classification issues before continuing.
8. **Management report**: Write the report from validated data, not from anecdotal impressions. Read `references/report-template.md`.
9. **HTML visualization**: Build a polished visual report using the same numbers as the report for both standard and deep depth unless the user explicitly removes it. It must use high-aesthetic management-report styling and remain clear, readable, and non-overlapping. Read `references/html-template.md`, then open and inspect the page in the browser.
10. **Cloudflare Pages**: Deploy only after the user confirms the HTML and data. Read `references/cloudflare-pages.md` and verify current official Cloudflare instructions.
11. **Final delivery**: Provide report link or local HTML path, raw data table path, evidence/method notes, and unresolved limitations.

## Default Project Layout

Create a per-project folder such as:

```text
<theme>_xhs_research/
├── raw/
│   ├── notes.jsonl
│   ├── comments.jsonl
│   └── collection_log.md
├── work/
│   ├── normalized_samples.csv
│   ├── summary_stats.json
│   └── quote_candidates.json
└── outputs/
    ├── xhs_raw_data.csv
    ├── xhs_raw_data.xlsx
    ├── xhs_management_report.md
    ├── xhs_management_report.html
    └── methodology.md
```

## References

- `references/intake.md`: required user inputs and confirmation template.
- `references/research-plan.md`: Xiaohongshu keyword design, collection protocol, and evidence collection rules.
- `references/data-schema.md`: raw data table schema and allowed values.
- `references/classification.md`: sentiment, dimension, evidence grade, and marketing flag definitions.
- `references/report-template.md`: management report structure and analysis guardrails.
- `references/html-template.md`: dashboard structure, chart denominator rules, visual QA checklist.
- `references/cloudflare-pages.md`: deployment gating and Cloudflare Pages notes.

## Scripts

- `scripts/validate_xhs_dataset.py <csv> --json-out <summary.json>` validates required columns, counts samples, checks allowed values, and produces summary statistics for the report and HTML.

Run validation before finalizing any report. Treat script warnings as issues to inspect, not as automatic blockers.
