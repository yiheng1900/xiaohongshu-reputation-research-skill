# Research Plan

Use this to turn a theme into a concrete Xiaohongshu research plan.

## Plan Sections

1. Research objective and decision questions.
2. Keyword matrix.
3. Sample inclusion and exclusion rules.
4. Data fields and evidence chain.
5. Classification rules.
6. Access gate and login check.
7. Formal collection plan.
8. Quality control and limitations.
9. Deliverables.

## Keyword Matrix

Build keywords from multiple layers. Record both user-provided and discovered keywords.

### Core Terms

- Brand name.
- Product/service name.
- Common abbreviations, old names, aliases, misspellings.
- City/store combinations if applicable.

### Purchase Decision Terms

- 怎么样
- 值不值得
- 价格
- 报价
- 套餐
- 性价比
- 对比
- 推荐
- 真实体验
- 已下单
- 已安装
- 已入住

### Risk Terms

- 避坑
- 投诉
- 翻车
- 后悔
- 维权
- 售后
- 延期
- 安装
- 质量
- 环保
- 甲醛
- 增项
- 合同
- 退款

### Stage Terms

- 到店
- 咨询
- 量尺
- 设计
- 报价
- 下单
- 交付
- 安装
- 入住
- 返修
- 售后

### Competitor Terms

For competitor comparison, combine:

```text
<theme> <competitor>
<theme> 对比 <competitor>
<theme> 和 <competitor>
<theme> vs <competitor>
```

### Industry-Specific Terms

Add terms from the user's industry. Examples:

- Home customization: 板材, 五金, 柜体, 门板, 封边, 设计师, 工期, 全屋定制.
- Beauty/medical aesthetics: 项目, 医生, 恢复期, 效果, 价格, 隐形消费.
- Education: 课程, 老师, 退费, 试听, 续费, 服务群.
- SaaS/software: 功能, 续费, 客服, 数据迁移, 稳定性, 培训.

## Sample Definitions

- Raw sample: every captured note, comment, or reply row.
- Valid sample: a row containing meaningful user experience, consultation, concern, question, comparison, complaint, praise, or decision signal.
- Core sample: a valid sample suitable for口碑 conclusions, usually authenticity A/B/C and not obvious marketing.
- Marketing/context sample: brand, store, influencer, designer, affiliate, or weak seed content. Keep it in raw data but avoid using it as core口碑 evidence.

## Prioritization

Prioritize these sample types:

1. Users who mention purchase, contract, quote, installation, usage, after-sales, refund, or store/city.
2. Users asking specific questions about price, material, safety, delivery, comparison, or service.
3. Comment threads where multiple users exchange concrete experiences.
4. Negative or controversial content with clear facts, dates, stores, or process nodes.
5. Neutral consultation and comparison content that reveals purchase barriers.

Do not over-prioritize high-like seed posts if their comments are shallow or commercial.

## Access Gate

Before collection, confirm Xiaohongshu access through `@电脑 / Computer Use` and the user's local Chrome browser:

- Xiaohongshu is logged in.
- Search results are visible.
- A note page can be opened.
- Note comments are visible.

After access is confirmed, proceed directly to formal collection. Do not insert a preliminary sample review phase. If the requested sample target later proves unrealistic, report the actual raw, valid, and core sample counts transparently.

## Collection Rules

- Capture source URL for every note-derived sample.
- Preserve publish time when visible; otherwise write `无法判断`.
- Record collection timestamp in local timezone.
- Keep original user wording in evidence fields. Do not rewrite raw evidence into official language.
- For long comment threads, keep meaningful comments and replies separately with parent note title/link.
- Deduplicate exact duplicate text by URL + source type + evidence text. Keep near-duplicates only when they are from distinct users or distinct notes.

## Quality Control

- Check whether many samples come from the same note. If so, disclose concentration risk.
- Separate "frequency in sample" from "platform-wide prevalence".
- Use multi-label denominator carefully: dimensions can exceed 100% when summed.
- Do not convert anecdotal complaints into universal claims unless repeated across independent samples.
