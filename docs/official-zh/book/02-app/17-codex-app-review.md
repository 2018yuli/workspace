# 第17章 审阅

> 原始页面：[Review – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/review)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 审阅窗格帮助您了解 Codex 更改了什么，提供针对性反馈，并决定保留哪些内容。
- `显示的更改`：审阅窗格反映您的 Git 仓库的状态，而不仅仅是 Codex 编辑的内容。这意味着它将显示：
- `导航审阅窗格`：- 单击文件名通常会在您选择的编辑器中打开该文件。您可以在 设置 中选择默认编辑器。

## 正文整理
### 正文
审阅窗格帮助您了解 Codex 更改了什么，提供针对性反馈，并决定保留哪些内容。（实现：[review_prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[tasks/review](/codex/codex-rs/core/src/tasks/review.rs#L1)、[app-server review tests](/codex/codex-rs/app-server/tests/suite/v2/review.rs#L1)）

继续往下看，这一节还强调了两件事：
- 它仅适用于存放在 Git 仓库中的项目。如果您的项目还不是 Git 仓库，审阅窗格会提示您创建一个。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

### 显示的更改
审阅窗格反映您的 Git 仓库的状态，而不仅仅是 Codex 编辑的内容。这意味着它将显示：（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- Codex 进行的更改
- 您自己所做的更改
- 仓库中任何其他未提交的更改

### 导航审阅窗格
单击文件名通常会在您选择的编辑器中打开该文件。您可以在 设置 中选择默认编辑器。

继续往下看，这一节还强调了两件事：
- 单击文件名背景可展开或收起差异。
- 按住 `Cmd` 的同时单击单行将打开该行在您选择的编辑器中。
- 如果您对更改感到满意，可以 暂存更改或还原不喜欢的更改。

### 反馈的行内评论
行内评论允许您将反馈直接附加到差异中的特定行。这通常是引导 Codex 进行正确修复的最快方法。

继续往下看，这一节还强调了两件事：
- 要留下行内评论：
- 1. 打开审阅窗格。 2. 将光标悬停在您想要评论的行上。 3. 单击出现的 **+** 按钮。 4. 写下您的反馈并提交。 5. 结束反馈后，回复该线程。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 由于评论是针对特定行的，Codex 可以比一般指令更精确地作出响应。

### 代码审阅结果
如果您使用 `/review` 进行代码审阅，评论将直接在审阅窗格中显示。（实现：[review_prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[tasks/review](/codex/codex-rs/core/src/tasks/review.rs#L1)、[app-server review tests](/codex/codex-rs/app-server/tests/suite/v2/review.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
