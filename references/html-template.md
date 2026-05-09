# HTML Visualization

Use this when turning the management report into a polished standalone HTML visualization report. Standard and deep research both require a clear, high-aesthetic visualization deliverable unless the user explicitly removes it.

## Page Structure

1. Title area: theme, platform, collection date range, sample counts.
2. Executive summary: 3-5 key conclusions.
3. KPI cards: raw, valid, core, notes, comments, replies.
4. Sentiment chart: core sample sentiment distribution.
5. Evidence level chart: A/B/C/D distribution, clearly stating denominator.
6. Dimension chart: multi-label frequencies with denominator noted.
7. Positive Top 5: concise cards/table with frequency, representative quotes, sample IDs, and clickable Xiaohongshu source links.
8. Negative Top 5: issue severity, frequency, systemic judgment, suggested fixes, sample IDs, and clickable Xiaohongshu source links.
9. Purchase concerns and journey map.
10. Quote wall: positive, neutral, negative, high-value comments.
11. Recommendations.
12. Methodology and limitations.

## Denominator Rules

- Sentiment percentages: use core samples unless explicitly stated otherwise.
- Dimension percentages: use core samples as denominator by default. Dimensions are multi-label and do not sum to 100%.
- Never use the largest dimension as the implicit denominator unless labeling it as "relative index".
- If a bar chart uses relative-to-max values for visual width, show actual sample count and actual denominator percentage next to it.
- If source rows include many comments from one note, show concentration risk in methodology.

## Visual Style

- Use the best available visual judgment: a high-aesthetic management dashboard style with restrained colors, high contrast, readable typography, and consistent spacing.
- Prioritize clarity over decoration. Every chart must be immediately legible, with visible labels, counts, denominators, and source-link affordances.
- Avoid making the whole page one hue. Use neutral background, dark text, and limited accent colors.
- Keep cards flat and purposeful. Do not nest cards inside cards.
- Use tables for dense evidence and cards only for repeated insight blocks.
- Make source links visible as "查看样本" or "来源链接".
- Use responsive layout for desktop and mobile.
- Verify that text, charts, tables, and cards remain clear and non-overlapping on desktop and mobile.

## Evidence Display

- Every Top 5 item should include 1-3 representative source links when links exist. Prefer A/B authenticity samples and avoid using rows without URLs as lead examples.
- Quotes should show sample ID, source type, sentiment, authenticity level, and link.
- Long quotes should be shortened with ellipses in HTML, while raw table preserves fuller evidence.
- Do not expose sensitive personal information.

## QA Checklist

Before final delivery:

- Open the HTML locally in the browser.
- Confirm all charts match `summary_stats.json` or the validated CSV counts.
- Confirm source links are clickable.
- Confirm no chart says "100%" merely because it is the longest bar.
- Confirm mobile layout does not overlap.
- Confirm methodology and limitations are visible.
- Confirm the HTML does not imply stronger certainty than the report.
