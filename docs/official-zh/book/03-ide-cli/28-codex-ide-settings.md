# 第28章 设置

> 原始页面：[Settings – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/settings)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用这些设置来自定义 Codex IDE 扩展。
- `更改设置`：要更改设置，请按照以下步骤操作：
- `设置参考`：| 设置 | 描述 | | --- | --- | | `chat.fontSize` | 控制 Codex 边栏中的聊天文本，包括对话内容和撰写器。 | | `chat.editor.…

## 正文整理
### 正文
使用这些设置来自定义 Codex IDE 扩展。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

### 更改设置
要更改设置，请按照以下步骤操作：

继续往下看，这一节还强调了两件事：
- 1. 打开您的编辑器设置。 2. 搜索 `Codex` 或设置名称。 3. 更新值。（实现：[web_search](/config/workspace/codex/codex-rs/core/src/web_search.rs:18)、[network_policy_decision](/config/workspace/codex/codex-rs/core/src/network_policy_decision.rs:1)、[network-proxy](/config/workspace/codex/codex-rs/network-proxy/src/lib.rs:1)）
- Codex IDE 扩展使用 Codex CLI。在共享的 `~/.codex/config.toml` 文件中配置某些行为，例如默认模型、审批和沙箱设置，而不是在编辑器设置中。有关更多信息，请参见 配置基础。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- 该扩展还尊重 VS Code 内置的聊天字体设置，用于 Codex 对话界面。

### 设置参考
| 设置 | 描述 | | --- | --- | | `chat.fontSize` | 控制 Codex 边栏中的聊天文本，包括对话内容和撰写器。 | | `chat.editor.fontSize` | 控制 Codex 对话中的代码渲染内容，包括代码片段和差异。 | | `chatgpt.cliExecutable` | 开发专用：Codex CLI 可执行文件的路径。除非您正在积极开发 Codex CLI，否则无需设置此项。如…（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
