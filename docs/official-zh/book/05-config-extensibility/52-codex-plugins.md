# 第52章 概述

> 原始页面：[Plugins – Codex | OpenAI Developers](https://developers.openai.com/codex/plugins)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- `概述`：插件将技能、应用集成和 MCP 服务器捆绑成可重用的工作流，以供 Codex 使用。
- `Codex 应用中的插件目录`：在 Codex 应用中打开 **插件** 以浏览和安装经过策划的插件。
- `CLI 中的插件目录`：在 Codex CLI 中，运行以下命令以打开插件列表：

## 正文整理
### 概述
插件将技能、应用集成和 MCP 服务器捆绑成可重用的工作流，以供 Codex 使用。（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）

继续往下看，这一节还强调了两件事：
- 扩展 Codex 的功能，例如：
- 安装 Gmail 插件使 Codex 能够读取和管理 Gmail。
- 安装 Google Drive 插件以在 Drive、Docs、Sheets 和 Slides 之间工作。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### Codex 应用中的插件目录
在 Codex 应用中打开 **插件** 以浏览和安装经过策划的插件。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### CLI 中的插件目录
在 Codex CLI 中，运行以下命令以打开插件列表：（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- CLI 插件浏览器按市场对插件进行分组。使用市场选项卡切换源，打开插件以检查详细信息，并按 `Space` 切换已安装插件的启用状态。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 安装和使用插件
打开插件目录后：

继续往下看，这一节还强调了两件事：
- 1. 搜索或浏览插件，然后打开其详细信息。 2. 选择安装按钮。在应用中，选择加号按钮或 **添加到 Codex**。在 CLI 中，选择 `安装插件`。 3. 如果插件需要外部应用，请在提示时连接。如果一些插件在安装过程中要求您进行身份验证，其他插件会等待您第一次使用它们时再进行。 4. 安装后，启动新线程并要求 Codex 使用该插件。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 安装插件后，您可以直接在提示窗口中使用它：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）
- 直接描述任务

### 权限和数据共享工作的方式
安装插件使其工作流可用于 Codex，但您现有的 批准设置 仍然适用。任何连接的外部服务仍受其自身身份验证、隐私和数据共享政策的约束。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 捆绑的技能在您安装插件后立即可用。（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）
- 如果插件包含应用，Codex 可能会在设置期间或第一次使用时提示您在 ChatGPT 中安装或登录这些应用。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 如果插件包含 MCP 服务器，它们可能需要额外的设置或身份验证才能使用。（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
