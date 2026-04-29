# 第40章 Linear

> 原始页面：[Use Codex in Linear | OpenAI Developers](https://developers.openai.com/codex/integrations/linear)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 在 Linear 中使用 Codex 将工作委派给问题。将一项问题分配给 Codex 或在评论中提到 `@Codex`，Codex 创建一个云任务并回复进展和结果。
- `设置 Linear 集成`：1. 通过在 Codex 中连接 GitHub 并为您希望 Codex 工作的仓库创建一个 环境，设置 Codex 云任务。 2. 前往 Codex 设置，为您的工作区安…
- `将工作委派给 Codex`：您可以通过两种方式进行委派：

## 正文整理
### 正文
在 Linear 中使用 Codex 将工作委派给问题。将一项问题分配给 Codex 或在评论中提到 `@Codex`，Codex 创建一个云任务并回复进展和结果。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- Linear 中的 Codex 可在付费套餐中使用（请参见 定价）。
- 如果您是企业计划的用户，请请求您的 ChatGPT 工作区管理员在 工作区设置 中开启 Codex 云任务，并在 连接设置 中启用 **Codex for Linear**。（实现：[StateRuntime::create_agent_job](/codex/codex-rs/state/src/runtime.rs#L917)、[StateRuntime::report_agent_job_item_result](/codex/codex-rs/state/src/runtime.rs#L1337)、[cloud-tasks App](/codex/codex-rs/cloud-tasks/src/app.rs#L47)、[cloud-tasks CLI](/codex/codex-rs/cloud-tasks/src/cli.rs#L7)）

### 设置 Linear 集成
1. 通过在 Codex 中连接 GitHub 并为您希望 Codex 工作的仓库创建一个 环境，设置 Codex 云任务。 2. 前往 Codex 设置，为您的工作区安装 **Codex for Linear**。 3. 通过在 Linear 问题的评论线程中提到 `@Codex` 来链接您的 Linear 帐户。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 将工作委派给 Codex
您可以通过两种方式进行委派：（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

### 将问题分配给 Codex
在安装集成后，您可以像将问题分配给队友一样将问题分配给 Codex。Codex 开始工作并向问题发布更新。

### 在评论中提到 `@Codex`
您还可以在评论线程中提到 `@Codex` 来委派工作或提出问题。在 Codex 回复后，请在线程中继续跟进，以保持同一会话。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 当 Codex 开始处理一个问题时，它会选择一个 环境和仓库 进行工作。 要固定特定的仓库，请在评论中包括它，例如：`@Codex fix this in openai/codex`。
- 要跟踪进展：
- 打开问题上的 **活动** 查看进度更新。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
