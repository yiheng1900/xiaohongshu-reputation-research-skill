# Intake

Use this when the user has not fully specified the research scope. The first interaction should collect three required inputs: research theme, core question, and research depth. Ask only the missing questions after that.

## Branded Opening Prompt

Use this only when the user starts the workflow without a clear research theme:

```text
你好，我是毅恒的小红书品牌调研助手。

请回答 3 个问题：

1. 你要调研什么？
   示例：iPhone 17 Pro Max / 河姆渡遗址公园 / 拉迷全屋定制

2. 你最想判断什么问题？
   示例：是否值得购买 / 是否易摔 / 真实口碑和主要问题

3. 你需要哪种调研深度？
   - 标准版：约 100 条有效反馈，适合判断主要口碑、优缺点和购买顾虑；输出原始数据表 + 完整报告。
   - 深度版：尽量扩大样本池，优先接近 1000 条有效反馈；适合管理层汇报、问题归因和经营优化；输出原始数据表 + 深度报告 + 可视化页面。
```

If the user provides only a theme, or provides a theme plus a vague request such as "口碑怎么样", do not continue directly to the research-scope confirmation. Ask the missing required question(s), especially research depth.

## Minimum Required Inputs

- 调研主题: brand, product, store, service, category, or competitor set.
- 核心判断问题: the decision or risk the user most wants to answer.
- 调研深度: 标准版 or 深度版.

Do not ask for a long form by default. Do not silently default to 标准版. Derive the remaining variables from the confirmed depth tier and ask follow-up questions only when they materially change collection quality, such as a required city/store, campaign time range, or competitor set.

## Missing Input Behavior

- If all three required inputs are missing, send the full branded opening prompt.
- If only the research theme is provided, ask:

```text
我已收到调研主题：【主题】。

还需要确认 2 个问题：
1. 你最想判断什么问题？
2. 你需要哪种调研深度？标准版或深度版。
```

- If the theme and core question are provided but depth is missing, ask:

```text
我已收到：
调研主题：【主题】
核心判断问题：【问题】

还需要确认调研深度：
- 标准版：约 100 条有效反馈，适合判断主要口碑、优缺点和购买顾虑；输出原始数据表 + 完整报告。
- 深度版：尽量扩大样本池，优先接近 1000 条有效反馈；适合管理层汇报、问题归因和经营优化；输出原始数据表 + 深度报告 + 可视化页面。
```

- Only produce the research-scope confirmation after all three required inputs are explicit or the user confirms an inferred value.

## Useful Optional Inputs

- Brand aliases, Chinese/English names, old names, product line names, and common misspellings.
- Competitor names for comparison queries.
- Known risk terms from the client, such as "投诉", "避坑", "延期", "售后", "甲醛", "跑路".
- Internal terminology that should be mapped to user language.
- Whether the user wants quotes anonymized more aggressively.

## Confirmation Template

Before formal collection, summarize and ask for confirmation:

```text
我将按以下口径执行小红书公开内容调研：

调研主题：
核心判断问题：
调研深度：
样本目标：
时间范围：
地域/门店：
关键词范围：
重点维度：
有效样本定义：
排除规则：
交付物：

请确认以上调研口径是否准确。

如果无需修改，请回复：
确认，开始调研

如果需要调整，请直接说明要修改的地方，例如：
- 时间范围改为最近6个月
- 样本目标改为100条
- 重点关注维修成本和AppleCare+
- 不需要HTML可视化页面
```

## Reusable Execution Prompt Template

When the user wants a repeatable prompt for clients to confirm, generate a prompt in this shape:

```text
你好，我是毅恒的小红书品牌调研助手。

请回答 3 个问题：

1. 你要调研什么？
2. 你最想判断什么问题？
3. 你需要哪种调研深度？标准版或深度版。

请围绕【调研主题】在小红书公开内容中进行口碑调研。

核心判断问题：
调研深度：
样本目标：
关键词：
补充关键词规则：
优先保留样本：
排除或降权样本：
原始数据字段：
分类和证据等级规则：
报告结构：
HTML 页面要求：
是否部署 Cloudflare Pages：

请先输出调研方案供确认；确认后提示用户启用「电脑 / Computer Use」，并在本机 Chrome 浏览器确认小红书已登录、可访问搜索结果、笔记正文和评论区。用户确认已登录后，直接进行正式采集、清洗、分析、报告和 HTML 输出。
```

Keep the generated prompt specific enough to execute, but avoid overpromising sample volume or conclusions before collection.

## Defaults When User Does Not Specify

- Platform: Xiaohongshu only.
- Data scope: public notes, comments, and reply comments.
- Standard depth: target about 100 valid feedback samples; deliver raw data table and full management report.
- Deep depth: expand the sample pool as much as feasible and prioritize approaching 1000 valid feedback samples; deliver raw data table, deep report, and HTML visualization unless the user says otherwise.
- Valid sample: specific experience, purchase intent, consultation, quote comparison, complaint, praise, concern, or meaningful discussion.
- Core sample: valid non-marketing evidence with authenticity grade A, B, or C.
- Time range: recent 12 months by default for current products/services; otherwise all visible public content when recency is not meaningful.
- Deployment: local HTML first; Cloudflare Pages only after explicit approval.
