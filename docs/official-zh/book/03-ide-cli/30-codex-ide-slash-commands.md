# 第30章 斜杠命令

> 原始页面：[Slash commands – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/slash-commands)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 斜杠命令让你在不离开聊天输入的情况下控制Codex。使用它们来检查状态、在本地和云模式之间切换或发送反馈。
- `使用斜杠命令`：1. 在Codex聊天输入中，输入`/`。 2. 从列表中选择一个命令，或继续输入以过滤（例如，`/status`）。 3. 按 **Enter**。
- `可用的斜杠命令`：| 斜杠命令 | 描述 | | --- | --- | | `/auto-context` | 开启或关闭自动上下文，以自动包含最近的文件和IDE上下文。 | | `/cloud`…

## 正文整理
### 正文
斜杠命令让你在不离开聊天输入的情况下控制Codex。使用它们来检查状态、在本地和云模式之间切换或发送反馈。（实现：[StateRuntime](/codex/codex-rs/state/src/runtime.rs#L63)、[log_db](/codex/codex-rs/state/src/log_db.rs#L47)、[extract/apply_rollout_item](/codex/codex-rs/state/src/extract.rs#L15)、[state_db](/codex/codex-rs/core/src/state_db.rs#L1)）

### 使用斜杠命令
1. 在Codex聊天输入中，输入`/`。 2. 从列表中选择一个命令，或继续输入以过滤（例如，`/status`）。 3. 按 **Enter**。

### 可用的斜杠命令
| 斜杠命令 | 描述 | | --- | --- | | `/auto-context` | 开启或关闭自动上下文，以自动包含最近的文件和IDE上下文。 | | `/cloud` | 切换到云模式以远程运行任务（需要云访问）。 | | `/cloud-environment` | 选择要使用的云环境（仅在云模式中可用）。 | | `/feedback` | 打开反馈对话框以提交反馈，并可以选择包括日志。 | | `/local` | …（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
