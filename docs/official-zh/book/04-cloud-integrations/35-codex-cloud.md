# 第35章 概述

> 原始页面：[Web – Codex | OpenAI Developers](https://developers.openai.com/codex/cloud)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它可以帮助您更快地构建、修复错误和理解不熟悉的代码。使用 Codex 云，Codex 可以在后台（包括并行）处理任务，利用其自己的云…
- `Codex Web 设置`：访问 Codex 并连接您的 GitHub 帐户。这使 Codex 可以处理您存储库中的代码并从其工作创建拉取请求。
- `使用 Codex Web`：**了解提示** \\ \\ 编写更清晰的提示，添加约束，并选择正确的细节级别以获得更好的结果。 **常见工作流** \\ \\ 从经过验证的模式开始，委托任务、审查更改…

## 正文整理
### 正文
Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它可以帮助您更快地构建、修复错误和理解不熟悉的代码。使用 Codex 云，Codex 可以在后台（包括并行）处理任务，利用其自己的云环境。

### Codex Web 设置
访问 Codex 并连接您的 GitHub 帐户。这使 Codex 可以处理您存储库中的代码并从其工作创建拉取请求。（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）

继续往下看，这一节还强调了两件事：
- 您的 Plus、Pro、Business、Edu 或 Enterprise 计划包括 Codex。了解更多关于 包含内容。某些企业工作区可能需要 管理员设置，才能访问 Codex。
- * * *

### 使用 Codex Web
**了解提示** \\ \\ 编写更清晰的提示，添加约束，并选择正确的细节级别以获得更好的结果。 **常见工作流** \\ \\ 从经过验证的模式开始，委托任务、审查更改，并将结果转换为拉取请求。 **配置环境** \\ \\ 选择存储库、设置步骤和 Codex 在云中运行任务时应使用的工具。 **从 IDE 扩展委托工作** \\ \\ 从您的编辑器启动云任务，然后监视进度并在本地应用生成的差异。 **从 GitHub 委托** \\…（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
