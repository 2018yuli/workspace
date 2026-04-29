# 第41章 概述

> 原始页面：[Security – Codex | OpenAI Developers](https://developers.openai.com/codex/security)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- Codex 安全性帮助工程和安全团队查找、验证和修复连接的 GitHub 存储库中的可能漏洞。
- `工作原理`：Codex 安全性逐步扫描连接的存储库。 它根据您的仓库构建扫描上下文，将可能的漏洞与该上下文进行检查，并在隔离环境中验证高信号问题，之后再将其展示出来。
- `访问和先决条件`：Codex 安全性通过 Codex Web 与连接的 GitHub 存储库协同工作。OpenAI 管理访问。如果您需要访问权限或某个存储库不可见，请联系您的 OpenAI 账户团队…

## 正文整理
### 正文
Codex 安全性帮助工程和安全团队查找、验证和修复连接的 GitHub 存储库中的可能漏洞。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- 本页面涵盖 Codex 安全性，这款产品扫描连接的 GitHub 存储库以查找可能的安全问题。有关 Codex 沙盒、批准、网络控制和管理设置的信息，请参见 代理批准与\\ 安全。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- 它帮助团队：
- 1. **查找可能的漏洞**，通过使用特定于仓库的威胁模型和实际代码上下文。 2. **减少噪音**，通过在审核它们之前验证发现。 3. **将发现向解决方案移动**，提供排名结果、证据和建议的补丁选项。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 工作原理
Codex 安全性逐步扫描连接的存储库。 它根据您的仓库构建扫描上下文，将可能的漏洞与该上下文进行检查，并在隔离环境中验证高信号问题，之后再将其展示出来。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 您将获得专注于以下内容的工作流：
- 具体于仓库的上下文，而不是通用签名（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 帮助减少误报的验证证据

### 访问和先决条件
Codex 安全性通过 Codex Web 与连接的 GitHub 存储库协同工作。OpenAI 管理访问。如果您需要访问权限或某个存储库不可见，请联系您的 OpenAI 账户团队，并确认该存储库可以通过您的 Codex Web 工作区访问。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 相关文档
Codex 安全设置 涵盖设置、扫描和发现审核。

继续往下看，这一节还强调了两件事：
- 常见问题解答 涵盖常见产品问题。
- 改进威胁模型 解释如何调整范围、攻击面和关键假设。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
