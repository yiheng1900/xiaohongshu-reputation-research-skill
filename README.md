# Xiaohongshu Reputation Research Skill

## 开始前先做这几步

在使用这个 Skill 前，建议先完成以下准备：

1. 在 Codex 中安装本 Skill：

```text
Use $skill-installer to install https://github.com/yiheng1900/xiaohongshu-reputation-research-skill
```

2. 安装完成后，重启 Codex，让新 Skill 生效。

3. 建议提前在 Codex 插件中启用或安装 **Chrome 插件**。小红书调研通常还需要使用 **Computer Use / 电脑** 能力来操作本机浏览器。

4. 在本机 Chrome 浏览器中登录小红书，并确认可以正常查看搜索结果、笔记正文和评论区。

完成后，在 Codex 中调用：

```text
Use $xiaohongshu-reputation-research
```

## 中文说明

这是一个用于 **小红书公开内容口碑调研** 的 Codex Skill。它不是独立爬虫，也不是小红书官方 API 工具，而是一套可复用的 AI 调研工作流，用于指导 Codex 在用户授权的浏览器环境中，围绕品牌、产品、服务、门店、景区或其他话题进行公开样本采集、清洗、分类、分析和报告生成。

## 这个 Skill 是做什么的

它帮助用户完成小红书口碑调研的完整流程：

- 引导用户输入调研主题、核心判断问题和调研深度
- 生成调研口径并请用户确认
- 提醒用户启用 Computer Use，并在本机 Chrome 中登录小红书
- 采集公开笔记、评论和回复评论中的有效用户反馈
- 保存原始数据和证据链
- 对样本进行去重、分类、情绪判断和证据等级标注
- 生成管理层可读的口碑分析报告
- 生成 HTML 可视化报告或页面
- 可选部署到 Cloudflare Pages

## 适用于什么场景

适合用于：

- 品牌小红书真实口碑调研
- 新品上市后的用户反馈分析
- 产品是否值得购买、是否有明显问题的判断
- 投诉、避坑、售后、交付、价格、环保等风险问题梳理
- 门店、景区、本地服务的公开评价分析
- 管理层汇报、经营复盘、产品和服务优化

## 不适用于什么场景

不适合用于：

- 绕过登录、验证码、权限或平台限制
- 抓取非公开内容、私信或个人隐私信息
- 高频自动化采集或违反平台规则的用途
- 将小红书样本直接等同于全量用户满意度调查
- 用少量个案直接推断整体市场结论

## 如何使用

推荐在 Codex 中通过 `skill-installer` 安装：

```text
Use $skill-installer to install https://github.com/yiheng1900/xiaohongshu-reputation-research-skill
```

安装后重启 Codex，然后调用：

```text
Use $xiaohongshu-reputation-research
```

如果需要手动安装，也可以将本仓库放入 Codex Skill 目录，例如：

```bash
~/.codex/skills/xiaohongshu-reputation-research
```

默认会引导用户回答 3 个问题：

```text
你好，我是毅恒小红书品牌调研小助手。

请回答 3 个问题：

1. 你要调研什么？
2. 你最想判断什么问题？
3. 你需要哪种调研深度？

- 标准版：必须达到 100 条有效反馈，适合判断主要口碑、优缺点和购买顾虑；输出原始数据表 + 完整报告 + 可视化报告。可视化报告必须使用最好的审美，清晰可见。
- 深度版：尽量扩大样本池，优先接近 1000 条有效反馈；适合管理层汇报、问题归因和经营优化；输出原始数据表 + 深度报告 + 可视化页面。可视化页面必须使用最好的审美，清晰可见。
```

这段开场是固定流程：三项没有填完整前，不会进入关键词计划、调研口径或采集方案；也不会默认标准版。

调研口径确认后，需要用户启用「电脑 / Computer Use」。建议提前安装或启用 Codex 的 Chrome 插件，并在本机 Chrome 浏览器中确认小红书已登录，且可以正常查看搜索结果、笔记正文和评论区。

## 主要产出

通常会生成：

- 原始数据表：CSV / XLSX
- 原始采集记录：JSONL / collection log
- 管理层调研报告：Markdown
- 方法说明：methodology
- HTML 可视化报告或页面
- 可选 Cloudflare Pages 公开链接

## 注意事项

- 仅使用公开可访问的小红书内容。
- 不绕过登录墙、验证码、付费墙、隐私设置或平台限制。
- 采样结果会受到小红书搜索排序、算法推荐、关键词设计和可见内容的影响。
- 正面内容可能包含商业种草，负面内容也可能存在情绪放大。
- 用户身份无法完全验证，报告中需要保留证据等级和真实性判断。
- 不同城市、门店和服务人员可能导致体验差异，不能简单合并为全国结论。
- 关键结论必须能回溯到原始样本 ID 和小红书来源链接。
- Cloudflare Pages 部署需要用户明确确认后再执行。

## English

This repository contains a **Codex Skill for Xiaohongshu public reputation research**. It is not a standalone crawler and it is not an official Xiaohongshu API client. It is a reusable AI research workflow that guides Codex through collecting, cleaning, classifying, analyzing, and reporting publicly available Xiaohongshu notes and comments in a user-authorized browser environment.

## Before You Start

Before using this Skill, prepare Codex and the browser environment:

1. Install this Skill in Codex:

```text
Use $skill-installer to install https://github.com/yiheng1900/xiaohongshu-reputation-research-skill
```

2. Restart Codex after installation so the new Skill is available.

3. Preferably enable or install the **Chrome plugin** in Codex in advance. Xiaohongshu research usually also requires **Computer Use** to operate the local browser.

4. Log into Xiaohongshu in the local Chrome browser and confirm that search results, note content, and comment sections are visible.

Then invoke the Skill in Codex:

```text
Use $xiaohongshu-reputation-research
```

## What This Skill Does

This Skill helps run an end-to-end Xiaohongshu reputation research workflow:

- Guides the user to define the research topic, core question, and research depth
- Creates a research scope for user confirmation
- Reminds the user to enable Computer Use and log into Xiaohongshu in local Chrome
- Collects valid feedback from public notes, comments, and comment replies
- Saves raw data and evidence trails
- Deduplicates, classifies, labels sentiment, and grades evidence strength
- Generates a management-ready reputation research report
- Creates an HTML visualization report/page
- Optionally deploys the HTML report to Cloudflare Pages

## Use Cases

This Skill is useful for:

- Brand reputation research on Xiaohongshu
- Product launch feedback analysis
- Purchase decision research, such as whether a product is worth buying
- Complaint, risk, after-sales, delivery, price, or quality issue analysis
- Store, attraction, local service, or category-level public feedback research
- Management reporting, business review, and product/service improvement

## Not For

This Skill should not be used for:

- Bypassing login, CAPTCHA, access control, or platform restrictions
- Collecting private messages, non-public content, or personal sensitive data
- High-frequency automation that violates platform rules
- Treating Xiaohongshu samples as a complete customer satisfaction survey
- Overgeneralizing market conclusions from a small number of anecdotes

## How To Use

Recommended installation through Codex `skill-installer`:

```text
Use $skill-installer to install https://github.com/yiheng1900/xiaohongshu-reputation-research-skill
```

Restart Codex, then invoke:

```text
Use $xiaohongshu-reputation-research
```

Manual installation is also possible by placing this repository in your Codex skills directory, for example:

```bash
~/.codex/skills/xiaohongshu-reputation-research
```

The default intake asks three questions:

```text
你好，我是毅恒小红书品牌调研小助手。

请回答 3 个问题：

1. What do you want to research?
2. What is the key question you want to answer?
3. What research depth do you need: standard or deep?

- 标准版：必须达到 100 条有效反馈，适合判断主要口碑、优缺点和购买顾虑；输出原始数据表 + 完整报告 + 可视化报告。可视化报告必须使用最好的审美，清晰可见。
- 深度版：尽量扩大样本池，优先接近 1000 条有效反馈；适合管理层汇报、问题归因和经营优化；输出原始数据表 + 深度报告 + 可视化页面。可视化页面必须使用最好的审美，清晰可见。
```

This opening flow is fixed: before all three inputs are explicit, the Skill should not move into keyword planning, research-scope confirmation, or collection planning, and it should not default to the standard tier.

After the research scope is confirmed, the user must enable **Computer Use**. It is recommended to enable or install the Codex **Chrome plugin** in advance, then confirm that Xiaohongshu is logged in through the local Chrome browser, with access to search results, note content, and comment sections.

## Outputs

Typical outputs include:

- Raw data table: CSV / XLSX
- Raw collection records: JSONL / collection log
- Management report: Markdown
- Methodology notes
- HTML visualization report/page
- Optional Cloudflare Pages public link

## Important Notes

- Use only publicly accessible Xiaohongshu content.
- Do not bypass login walls, CAPTCHAs, paywalls, privacy settings, or platform restrictions.
- Samples may be affected by Xiaohongshu search ranking, recommendation algorithms, keyword design, and visible content availability.
- Positive posts may include commercial seeding; negative posts may be emotionally amplified.
- User identity cannot always be fully verified, so evidence grading and authenticity labels are required.
- Experiences may vary by city, store, or service provider and should not be overgeneralized.
- Key conclusions must be traceable to raw sample IDs and Xiaohongshu source links.
- Cloudflare Pages deployment should only happen after explicit user confirmation.
