# Cloudflare Pages Delivery

Use this only after the user has approved the final local HTML page and agreed to publish it.

## Gate

Before deployment, ask for explicit confirmation:

```text
本地 HTML 已确认。是否现在部署到 Cloudflare Pages 并生成公开链接？
```

Do not deploy drafts, raw evidence, or files containing sensitive details without confirmation.

## Current-Docs Requirement

Cloudflare deployment options and commands can change. Before executing deployment, verify current official docs:

- Cloudflare Pages Direct Upload
- Cloudflare Pages Git integration
- Cloudflare Workers Static Assets, if Pages guidance has changed

Use official Cloudflare documentation as the source of truth.

## Recommended Deployment Choices

- For one-off static HTML reports, prefer direct upload if available and authenticated.
- For repeatable client work, prefer a Git-backed Cloudflare Pages project.
- For automated workflows, use a dedicated project name and avoid overwriting unrelated deployments.

## Pre-Deploy Checklist

- HTML opens locally and charts render.
- Source links are intended to be public.
- Raw data files are excluded unless the user explicitly wants them public.
- No credentials, cookies, local filesystem paths, or private user data are embedded.
- The report clearly states research limitations.

## Delivery Notes

Final response should include:

- Cloudflare URL.
- Local HTML path.
- Raw data file path.
- Methodology file path.
- Any deployment caveats, such as authentication, project name, or unpublished raw data.
