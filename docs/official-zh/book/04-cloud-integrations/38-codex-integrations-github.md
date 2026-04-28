# 第38章 GitHub

> 原始页面：[Use Codex in GitHub | OpenAI Developers](https://developers.openai.com/codex/integrations/github)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用 Codex 审查拉取请求，而无需离开 GitHub。添加一个拉取请求评论，输入 `@codex review`，Codex 会回复一个标准的 GitHub 代码审查。
- `设置代码审查`：1. 设置 Codex 云。 2. 转到 Codex 设置，为您的存储库启用 **代码审查**。
- `请求审查`：1. 在拉取请求评论中，提及 `@codex review`。 2. 等待 Codex 响应（👀）并发布审查。

## 正文整理
### 正文
使用 Codex 审查拉取请求，而无需离开 GitHub。添加一个拉取请求评论，输入 `@codex review`，Codex 会回复一个标准的 GitHub 代码审查。（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）

### 设置代码审查
1. 设置 Codex 云。 2. 转到 Codex 设置，为您的存储库启用 **代码审查**。（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）

### 请求审查
1. 在拉取请求评论中，提及 `@codex review`。 2. 等待 Codex 响应（👀）并发布审查。（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）

继续往下看，这一节还强调了两件事：
- Codex 在拉取请求上发布审查，就像队友一样。

### 启用自动审查
如果您希望 Codex 自动审查每个拉取请求，请在 Codex 设置中启用 **自动审查**。Codex 每当有新的 PR 提交审查时，都会发布一个审查，而不需要 `@codex review` 评论。（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）

### 自定义 Codex 审查内容
Codex 在您的存储库中搜索 `AGENTS.md` 文件，并遵循您包含的任何 **审查指南**。（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)、[web_search](/config/workspace/codex/codex-rs/core/src/web_search.rs:18)）

继续往下看，这一节还强调了两件事：
- 要为存储库设置指南，请添加或更新一个顶层的 `AGENTS.md`，包括如下部分：（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
