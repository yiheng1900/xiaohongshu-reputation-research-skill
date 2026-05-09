# Classification Rules

Use these definitions consistently. When evidence is ambiguous, choose the weaker claim and mark uncertainty explicitly.

## Sentiment

### 正面

Clear favorable evaluation, satisfaction, recommendation, successful outcome, acceptable value, or reduced concern.

Examples:

- "装完效果不错"
- "设计师很负责"
- "价格比预期合适"
- "售后处理了"

### 中性

Information seeking, comparison, factual sharing, price/material/design questions, or no clear praise/complaint.

Examples:

- "多少钱一平"
- "这个板材环保吗"
- "和某品牌怎么选"
- "已报价，正在对比"

### 负面

Clear dissatisfaction, complaint, warning, unresolved issue, risk claim, regret, or strong purchase barrier.

Examples:

- "延期很久"
- "安装问题没人处理"
- "报价不透明"
- "售后太慢"

### 混合

Both clear positive and negative signals in the same sample.

Examples:

- "设计满意，但安装拖了很久"
- "价格可以，售后一般"

## Dimensions

Use multi-label classification. A sample can belong to several dimensions.

- 价格: quote, package, discount, expensive/cheap, budget, hidden cost.
- 设计: design plan, layout, rendering, designer, aesthetics, implementation consistency.
- 产品质量: durability, workmanship, finish, hardware, defects.
- 板材: material, board type, surface, edge banding, hardware/material authenticity.
- 环保: smell, formaldehyde, certification, safety concern.
- 安装: installer, on-site workmanship, damage, rework, measurement fit.
- 交付: production cycle, delivery delay, scheduling, promised timeline.
- 售后: repair, replacement, complaint handling, response speed, responsibility.
- 门店服务: store reception, salesperson, designer service, communication, local execution.
- 性价比: overall value judgment combining price and perceived result.
- 合同/增项: contract terms, add-ons, payment, refund, scope ambiguity.
- 竞品对比: explicit comparison with named alternatives.
- 内容营销: influencer promotion, brand/store post, commercial content pattern.
- 其他: use only when no defined label fits.

## Account Type

Classify conservatively:

- 真实用户: personal account with concrete purchase/consultation/use evidence.
- 装修博主/行业博主: content creator or guide-style account; commercial status may be unclear.
- 设计师: presents as designer or design service provider.
- 门店销售: store sales, consultant, local dealer, or account driving store leads.
- 品牌号: official brand or franchise account.
- 疑似商家: unclear account with repeated promotion, lead capture, or sales language.
- 无法判断: not enough signals.

## Suspected Ad or Soft Promotion

Mark `是` when there is obvious brand/store promotion, lead capture, affiliate language, repetitive commercial format, or comment guidance toward private consultation.

Mark `不确定` when the account could be a genuine user but content format is highly polished, commercial, or has unexplained brand emphasis.

Mark `否` only when concrete user experience or organic discussion is the dominant signal.

## Authenticity Level

- A: purchase/install/use/after-sales/contract/price/store/time evidence is concrete.
- B: consultation, quote, comparison, or purchase concern is concrete but purchase not proven.
- C: useful reference from blogger/designer/summary content; commercial status uncertain.
- D: weak, vague, promotional, duplicate, or not useful for口碑 judgment.

## Valid and Core Samples

Mark valid when the sample contains a meaningful user signal.

Mark core when all are true:

- Valid sample.
- Authenticity level A, B, or C.
- Not obvious advertising.
- Relevant to the research theme.

Keep D-level and ad samples in the raw table, but exclude them from core口碑 percentages unless explicitly analyzing marketing noise.

## Systemic vs Incident

Treat a negative issue as potentially systemic only when it appears in at least three independent sources or across multiple notes/stores/stages with a similar mechanism.

Treat it as an incident when evidence is detailed but isolated.

Use "无法判断是否系统性" when volume is too small or many comments come from one thread.

## Quote Selection

- Prefer A/B evidence for user quotes.
- Preserve original wording, but avoid exposing sensitive personal information.
- Keep quotes short and link them to sample IDs.
- Do not use D-level marketing copy as representative user口碑.
