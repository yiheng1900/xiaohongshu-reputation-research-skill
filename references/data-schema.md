# Data Schema

Use this schema for normalized Xiaohongshu research data. Chinese field names are preferred for client-facing tables; English aliases are acceptable for scripts if mapped clearly.

## Required Columns

| Chinese field | English alias | Required | Notes |
| --- | --- | --- | --- |
| 序号 | sample_id | Yes | Stable sample ID used in report citations. |
| 来源类型 | source_type | Yes | 笔记 / 评论 / 回复评论. |
| 笔记标题 | note_title | Yes | Use `无法判断` if unavailable. |
| 链接 | url | Yes | Xiaohongshu note URL or share URL. |
| 发布时间 | published_at | Yes | Use visible publish time, or `无法判断`. |
| 采集时间 | collected_at | Yes | Local timestamp when captured. |
| 城市 / 门店信息 | city_store | Yes | Use `无法判断` if absent. |
| 账号类型 | account_type | Yes | See allowed values. |
| 用户阶段 | user_stage | Yes | See allowed values. |
| 情绪倾向 | sentiment | Yes | 正面 / 中性 / 负面 / 混合. |
| 评价维度 | dimensions | Yes | Multi-label; separate with `;`. |
| 原文关键证据 | evidence_text | Yes | Preserve original wording as much as possible. |
| 评论区有价值信息 | comment_context | Yes | Use `无` if not applicable. |
| 是否疑似广告或软文 | suspected_ad | Yes | 是 / 否 / 不确定. |
| 真实性等级 | authenticity_level | Yes | A / B / C / D. |
| 是否有效样本 | valid_sample | Recommended | 是 / 否. If missing, infer cautiously. |
| 是否核心样本 | core_sample | Recommended | 是 / 否. If missing, infer from validity + evidence grade. |

## Allowed Values

### 来源类型

- 笔记
- 评论
- 回复评论

### 账号类型

- 真实用户
- 装修博主
- 行业博主
- 设计师
- 门店销售
- 品牌号
- 疑似商家
- 无法判断

Adjust industry-specific labels when needed, but keep commercial identities separate from real users.

### 用户阶段

- 咨询中
- 已报价
- 已下单
- 安装中
- 已入住
- 售后中
- 对比中
- 无法判断

### 情绪倾向

- 正面
- 中性
- 负面
- 混合

### 评价维度

Use multi-label values separated by `;`.

- 价格
- 设计
- 产品质量
- 板材
- 环保
- 安装
- 交付
- 售后
- 门店服务
- 性价比
- 合同/增项
- 竞品对比
- 内容营销
- 其他

Adapt dimensions to the industry, but define the adapted set before classification.

### 真实性等级

- A: Strong real-user evidence. Mentions purchase, order, quote, contract, installation, use, after-sales, store, city, date, price, or other concrete facts.
- B: Strong consultation or decision evidence. Mentions store visit, quote comparison, specific concern, or decision barrier, but purchase is not confirmed.
- C: Reference information. Blogger, designer, industry summary, or experience post with some useful content but unclear commercial status.
- D: Weak evidence or likely marketing. Brand/store promotion, vague seed content, no concrete experience, obvious ad, or unverifiable general statement.

## Evidence Chain Files

Recommended files:

- `raw/notes.jsonl`: raw note-level capture.
- `raw/comments.jsonl`: raw comments and replies.
- `raw/collection_log.md`: collection dates, keywords, pages visited, blocking issues.
- `work/normalized_samples.csv`: cleaned table before Excel formatting.
- `work/summary_stats.json`: counts used in report and HTML.
- `outputs/xhs_raw_data.csv`: client-facing raw table.
- `outputs/xhs_raw_data.xlsx`: formatted workbook when spreadsheet output is requested.

## Privacy and Compliance

- Do not collect private messages or non-public account information.
- Avoid unnecessary personal identifiers. If usernames are needed for dedupe, store hashed or shortened versions when possible.
- Do not expose phone numbers, addresses, order numbers, or other sensitive user data in final reports.
- Keep raw evidence sufficient for traceability but avoid turning the dataset into a personal data archive.
