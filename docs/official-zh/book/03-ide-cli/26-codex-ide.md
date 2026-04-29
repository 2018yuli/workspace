# 第26章 概述

> 原始页面：[IDE extension – Codex | OpenAI Developers](https://developers.openai.com/codex/ide)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它帮助您更快地构建，消除错误，并理解不熟悉的代码。通过 Codex VS Code 扩展，您可以在 IDE 中并行使用 Codex …
- `扩展设置`：Codex IDE 扩展与 VS Code 分支（如 Cursor 和 Windsurf）兼容。
- `JetBrains IDE 集成`：如果您希望在 JetBrains IDE（例如 Rider、IntelliJ、PyCharm 或 WebStorm）中使用 Codex，请安装 JetBrains…

## 正文整理
### 正文
Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它帮助您更快地构建，消除错误，并理解不熟悉的代码。通过 Codex VS Code 扩展，您可以在 IDE 中并行使用 Codex 或将任务委派给 Codex Cloud。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
- OpenAI Codex 在您的代码编辑器中 - YouTube
- 点击取消静音

### 扩展设置
Codex IDE 扩展与 VS Code 分支（如 Cursor 和 Windsurf）兼容。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 您可以从 Visual Studio Code 市场 获取 Codex 扩展，或下载适用于您的 IDE：（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 下载 Visual Studio Code 版
- 下载 Cursor 版

### JetBrains IDE 集成
如果您希望在 JetBrains IDE（例如 Rider、IntelliJ、PyCharm 或 WebStorm）中使用 Codex，请安装 JetBrains IDE 集成。它支持使用 ChatGPT、API 密钥或 JetBrains AI 订阅进行登录。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 将 Codex 移动到右侧边栏
在 VS Code 中，Codex 会自动出现在右侧边栏。如果您希望它在主（左）边栏中，请将 Codex 图标拖回左侧活动栏。

继续往下看，这一节还强调了两件事：
- 在 Cursor 等 VS Code 分支中，您可能需要手动将 Codex 移动到右侧边栏。为此，您可能需要首先暂时更改活动栏方向：
- 1. 打开您的编辑器设置，搜索 `activity bar`（在工作台设置中）。 2. 将方向更改为 `vertical`。 3. 重启您的编辑器。（实现：[web_search](/codex/codex-rs/core/src/web_search.rs#L18)、[network_policy_decision](/codex/codex-rs/core/src/network_policy_decision.rs#L1)、[network-proxy](/codex/codex-rs/network-proxy/src/lib.rs#L1)）
- 现在将 Codex 图标拖到右侧边栏（例如，紧挨着您的 Cursor 聊天）。Codex 显示为侧边栏中的另一个选项卡。

### 登录
安装扩展后，它会提示您使用 ChatGPT 帐户或 API 密钥登录。您的 ChatGPT 计划包括使用额度，因此您可以无需额外设置就使用 Codex。有关更多信息，请访问 定价页面。（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)、[auth](/codex/codex-rs/core/src/auth.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
