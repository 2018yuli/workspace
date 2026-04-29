# 第39章 Slack

> 原始页面：[Use Codex in Slack | OpenAI Developers](https://developers.openai.com/codex/integrations/slack)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 在 Slack 中使用 Codex 从频道和线程启动编码任务。提到 `@Codex` 并提供一个提示，Codex 将创建一个云任务并回复结果。
- `设置 Slack 应用`：1. 设置 Codex 云任务。您需要一个 Plus、Pro、Business、Enterprise 或 Edu 计划（请参见 ChatGPT 定价）、一个连接的 GitH…
- `开始任务`：1. 在一个频道或线程中，提到 `@Codex` 并包含您的提示。Codex 可以引用线程中早期的消息，因此您通常不需要重申上下文。 2. （可选）在您的提示中指定一个环境或存储库，例如…

## 正文整理
### 正文
在 Slack 中使用 Codex 从频道和线程启动编码任务。提到 `@Codex` 并提供一个提示，Codex 将创建一个云任务并回复结果。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 设置 Slack 应用
1. 设置 Codex 云任务。您需要一个 Plus、Pro、Business、Enterprise 或 Edu 计划（请参见 ChatGPT 定价）、一个连接的 GitHub 账户，以及至少一个 环境。 2. 转到 Codex 设置 并为您的工作区安装 Slack 应用。根据您的 Slack 工作区政策，可能需要管理员批准安装。 3. 在一个频道中添加 `@Codex`。如果您尚未添加，Slack 会在您提到它时提示您。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 开始任务
1. 在一个频道或线程中，提到 `@Codex` 并包含您的提示。Codex 可以引用线程中早期的消息，因此您通常不需要重申上下文。 2. （可选）在您的提示中指定一个环境或存储库，例如：`@Codex 修复上述内容在 openai/codex`。 3. 等待 Codex 反应 (👀) 并回复任务链接。当它完成时，Codex 会发布结果，并根据您的设置在线程中给出答案。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### Codex 如何选择环境和仓库
Codex 会审查您可以访问的环境，并选择最匹配您请求的环境。如果请求模糊，它会回退到您最近使用的环境。

继续往下看，这一节还强调了两件事：
- 任务在该环境的仓库映射中列出的第一个仓库的默认分支上运行。如果您需要不同的默认分支或更多仓库，请在 Codex 中更新仓库映射。
- 如果没有合适的环境或仓库可用，Codex 将在 Slack 中回复说明如何解决问题，然后重试。

### 企业数据控制
默认情况下，Codex 会在线程中回复答案，其中可能包含它运行的环境中的信息。 为了防止这种情况，企业管理员可以在 ChatGPT 工作区设置 中清除 **允许 Codex Slack 应用在任务完成时发布答案** 的选项。当管理员关闭答案时，Codex 只会回复任务链接。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
