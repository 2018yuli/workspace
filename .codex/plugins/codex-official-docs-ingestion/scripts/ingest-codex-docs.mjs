import { mkdir, readdir, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import FirecrawlApp from "@mendable/firecrawl-js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "../../../..");
const outputDir = path.resolve(
  repoRoot,
  process.env.CODEX_DOCS_OUTPUT_DIR || "docs/official",
);
const pagesDir = path.join(outputDir, "pages");
const translateToZh = process.env.CODEX_TRANSLATE_TO_ZH === "1";
const translationModel = process.env.CODEX_TRANSLATION_MODEL || "gpt-5-mini";
const translationBaseUrl =
  (process.env.OPENAI_BASE_URL || "https://api.openai.com/v1").replace(/\/+$/, "");
const translationApiStyle = process.env.OPENAI_API_STYLE || "responses";
const zhOutputDir = path.resolve(
  repoRoot,
  process.env.CODEX_DOCS_ZH_OUTPUT_DIR || "docs/official-zh",
);
const zhPagesDir = path.join(zhOutputDir, "pages");

const discoveryRoot =
  process.env.CODEX_DOC_DISCOVERY_ROOT || "https://developers.openai.com/codex/";
const allowedPrefix =
  process.env.CODEX_DOC_ALLOWED_PREFIX || "https://developers.openai.com/codex/";
const defaultSeedUrls = [
  "https://developers.openai.com/codex/",
  "https://developers.openai.com/codex/quickstart",
  "https://developers.openai.com/codex/plugins",
  "https://developers.openai.com/codex/skills",
  "https://developers.openai.com/codex/sdk",
  "https://developers.openai.com/codex/llms-full.txt"
];
const defaultMapLimit = Number.parseInt(process.env.CODEX_DOC_MAP_LIMIT || "200", 10);
const defaultBatchSize = Number.parseInt(process.env.CODEX_DOC_BATCH_SIZE || "10", 10);

function getSeedUrls() {
  const configuredTargets = process.env.CODEX_DOC_TARGETS
    ?.split(",")
    .map((value) => value.trim())
    .filter(Boolean);

  return configuredTargets?.length ? configuredTargets : defaultSeedUrls;
}

function slugifyUrl(url) {
  const parsed = new URL(url);
  const pathname = parsed.pathname.replace(/\/+$/, "") || "/";
  const base = `${parsed.hostname}${pathname === "/" ? "/index" : pathname}`;
  return base
    .replace(/[^a-zA-Z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase();
}

function uniqueUrls(urls) {
  return [...new Set(urls)];
}

function isAllowedDocUrl(url) {
  return url.startsWith(allowedPrefix);
}

function chunk(items, size) {
  const chunks = [];
  for (let index = 0; index < items.length; index += size) {
    chunks.push(items.slice(index, index + size));
  }
  return chunks;
}

function normalizeTranslatedMarkdown(markdown) {
  return markdown
    .replace(/^```markdown\s*/i, "")
    .replace(/^```\s*/i, "")
    .replace(/\s*```$/i, "")
    .trim();
}

async function ensureOutputDirs() {
  await mkdir(outputDir, { recursive: true });
  await mkdir(pagesDir, { recursive: true });
  if (translateToZh) {
    await mkdir(zhOutputDir, { recursive: true });
    await mkdir(zhPagesDir, { recursive: true });
  }
}

async function clearDir(targetDir) {
  let entries = [];
  try {
    entries = await readdir(targetDir);
  } catch {
    return;
  }

  await Promise.all(
    entries.map((entry) => rm(path.join(targetDir, entry), { force: true })),
  );
}

async function discoverUrls(app) {
  const discovered = uniqueUrls(getSeedUrls());
  const mapResponse = await app.mapUrl(discoveryRoot, {
    limit: defaultMapLimit,
    ignoreSitemap: false,
    includeSubdomains: false,
    search: "codex"
  });

  if (!mapResponse?.success) {
    const message = mapResponse?.error || "Unknown Firecrawl map error";
    throw new Error(message);
  }

  const mappedLinks = (mapResponse.links || []).filter(isAllowedDocUrl);
  return uniqueUrls([...discovered, ...mappedLinks]).sort();
}

async function writePage(document) {
  const url =
    document.url ||
    document.metadata?.sourceURL ||
    document.metadata?.url;
  if (!url) {
    return null;
  }

  const slug = slugifyUrl(url);
  const markdownPath = path.join(pagesDir, `${slug}.md`);
  const jsonPath = path.join(pagesDir, `${slug}.json`);
  const frontmatter = [
    "---",
    `source: ${url}`,
    `title: ${JSON.stringify(document.metadata?.title || document.metadata?.ogTitle || "")}`,
    `crawledAt: ${new Date().toISOString()}`,
    "---",
    ""
  ].join("\n");
  const markdown = typeof document.markdown === "string" ? document.markdown : "";

  await writeFile(markdownPath, `${frontmatter}${markdown}\n`, "utf8");
  await writeFile(
    jsonPath,
    `${JSON.stringify(document, null, 2)}\n`,
    "utf8",
  );

  return {
    url,
    slug,
    title: document.metadata?.title || document.metadata?.ogTitle || null,
    markdownPath: path.relative(repoRoot, markdownPath),
    metadataPath: path.relative(repoRoot, jsonPath),
    markdownBytes: Buffer.byteLength(markdown, "utf8")
  };
}

async function translateMarkdownToChinese(markdown, url, title) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    throw new Error("OPENAI_API_KEY is required when CODEX_TRANSLATE_TO_ZH=1.");
  }

  const requestBody = translationApiStyle === "chat_completions"
    ? {
        model: translationModel,
        stream: false,
        messages: [
          {
            role: "system",
            content:
              "Translate English technical markdown into Simplified Chinese. Preserve markdown structure, code blocks, inline code, URLs, headings, bullet structure, and literals. Do not summarize. Do not add commentary."
          },
          {
            role: "user",
            content: `URL: ${url}\nTitle: ${title || ""}\n\nMarkdown to translate:\n\n${markdown}`
          }
        ]
      }
    : {
        model: translationModel,
        input: [
          {
            role: "system",
            content: [
              {
                type: "input_text",
                text: "Translate English technical markdown into Simplified Chinese. Preserve markdown structure, code blocks, inline code, URLs, headings, bullet structure, and literals. Do not summarize. Do not add commentary."
              }
            ]
          },
          {
            role: "user",
            content: [
              {
                type: "input_text",
                text: `URL: ${url}\nTitle: ${title || ""}\n\nMarkdown to translate:\n\n${markdown}`
              }
            ]
          }
        ]
      };
  const endpoint = translationApiStyle === "chat_completions"
    ? `${translationBaseUrl}/chat/completions`
    : `${translationBaseUrl}/responses`;

  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`
    },
    body: JSON.stringify(requestBody)
  });

  if (!response.ok) {
    throw new Error(`OpenAI translation failed with status ${response.status}.`);
  }

  const payload = await response.json();
  const translated =
    payload.choices?.[0]?.message?.content?.trim() ||
    payload.output_text ||
    payload.output?.flatMap((item) => item.content || [])
      ?.filter((item) => item.type === "output_text")
      ?.map((item) => item.text)
      ?.join("\n")
      ?.trim();

  if (!translated) {
    throw new Error("OpenAI translation returned no text.");
  }

  return normalizeTranslatedMarkdown(translated);
}

async function writeChinesePage(page, document) {
  const zhMarkdownPath = path.join(zhPagesDir, `${page.slug}.md`);
  const zhJsonPath = path.join(zhPagesDir, `${page.slug}.json`);
  const translatedMarkdown = await translateMarkdownToChinese(
    typeof document.markdown === "string" ? document.markdown : "",
    page.url,
    page.title,
  );
  const frontmatter = [
    "---",
    `source: ${page.url}`,
    `title: ${JSON.stringify(page.title || "")}`,
    `translatedTo: zh-CN`,
    `translatedAt: ${new Date().toISOString()}`,
    `model: ${translationModel}`,
    "---",
    ""
  ].join("\n");

  await writeFile(zhMarkdownPath, `${frontmatter}${translatedMarkdown}\n`, "utf8");
  await writeFile(
    zhJsonPath,
    `${JSON.stringify({
      url: page.url,
      title: page.title,
      translatedTo: "zh-CN",
      model: translationModel,
      markdownPath: path.relative(repoRoot, zhMarkdownPath)
    }, null, 2)}\n`,
    "utf8",
  );

  return {
    ...page,
    markdownPath: path.relative(repoRoot, zhMarkdownPath),
    metadataPath: path.relative(repoRoot, zhJsonPath),
    language: "zh-CN"
  };
}

async function scrapeBatch(app, urls) {
  const response = await app.batchScrapeUrls(urls, {
    formats: ["markdown"],
    onlyMainContent: true
  });

  if (!response?.success) {
    const message = response?.error || "Unknown Firecrawl batch scrape error";
    throw new Error(message);
  }

  return response.data || [];
}

async function main() {
  const apiKey = process.env.FIRECRAWL_API_KEY;
  if (!apiKey) {
    throw new Error("FIRECRAWL_API_KEY is required.");
  }

  await ensureOutputDirs();
  await clearDir(pagesDir);
  if (translateToZh) {
    await clearDir(zhPagesDir);
  }

  const app = new FirecrawlApp({ apiKey });
  const discoveredUrls = await discoverUrls(app);
  const batches = chunk(discoveredUrls, defaultBatchSize);
  const pages = [];
  const zhPages = [];
  const errors = [];

  for (const [index, urls] of batches.entries()) {
    try {
      const documents = await scrapeBatch(app, urls);
      for (const document of documents) {
        const saved = await writePage(document);
        if (saved) {
          pages.push(saved);
          console.log(`Saved ${saved.url}`);
          if (translateToZh) {
            try {
              const zhSaved = await writeChinesePage(saved, document);
              zhPages.push(zhSaved);
              console.log(`Translated ${saved.url} to zh-CN`);
            } catch (error) {
              const message = error instanceof Error ? error.message : String(error);
              errors.push({ url: saved.url, error: `Translation failed: ${message}` });
              console.error(`Translation failed for ${saved.url}: ${message}`);
            }
          }
        }
      }
      console.log(`Completed batch ${index + 1}/${batches.length}`);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      for (const url of urls) {
        errors.push({ url, error: message });
      }
      console.error(`Batch ${index + 1} failed: ${message}`);
    }
  }

  const manifest = {
    generatedAt: new Date().toISOString(),
    outputDir: path.relative(repoRoot, outputDir),
    discoveryRoot,
    allowedPrefix,
    discoveredUrlCount: discoveredUrls.length,
    batchSize: defaultBatchSize,
    urls: discoveredUrls,
    pages,
    zhOutputDir: translateToZh ? path.relative(repoRoot, zhOutputDir) : null,
    zhPages,
    errors
  };

  await writeFile(
    path.join(outputDir, "manifest.json"),
    `${JSON.stringify(manifest, null, 2)}\n`,
    "utf8",
  );

  if (errors.length > 0) {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exitCode = 1;
});
