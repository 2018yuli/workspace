---
name: ingestion
description: Use this skill when you need to crawl the official Codex documentation with the Firecrawl client and export the resulting markdown and metadata to docs/official in the current repository.
---

# Codex Docs Ingestion

Use this skill to refresh the local mirror of official Codex documentation.
It can also generate a Simplified Chinese mirror.

## Workflow

1. Ensure `FIRECRAWL_API_KEY` is set in the environment before running the script.
2. From the repository root, install the plugin dependency if needed:
   `pnpm --dir .codex/plugins/codex-official-docs-ingestion install`
3. Run:
   `pnpm --dir .codex/plugins/codex-official-docs-ingestion ingest`
4. Review the generated files under `docs/official/`:
   - `manifest.json` contains the crawl summary.
   - `pages/*.md` contains page markdown.
   - `pages/*.json` contains raw metadata per page.

## Chinese Output

To generate Simplified Chinese pages as well:

1. Set `OPENAI_API_KEY`.
2. Run with `CODEX_TRANSLATE_TO_ZH=1`.
3. Review the translated output under `docs/official-zh/`.

Example:

`CODEX_TRANSLATE_TO_ZH=1 OPENAI_API_KEY=... pnpm --dir .codex/plugins/codex-official-docs-ingestion ingest`

## Notes

- The script is intentionally conservative about crawl scope. It targets known Codex documentation entry points under `https://developers.openai.com/codex` rather than the entire OpenAI domain.
- Override targets by setting `CODEX_DOC_TARGETS` to a comma-separated URL list.
- Override output by setting `CODEX_DOCS_OUTPUT_DIR`.
- Override Chinese output by setting `CODEX_DOCS_ZH_OUTPUT_DIR`.
- Override the translation model by setting `CODEX_TRANSLATION_MODEL`.
