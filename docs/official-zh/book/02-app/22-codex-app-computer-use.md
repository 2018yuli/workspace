# 第22章 计算机使用

> 原始页面：[Computer Use – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/computer-use)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 在 Codex 应用中，计算机使用当前适用于 macOS，但在启动时不在欧洲经济区、英国和瑞士。安装计算机使用插件，然后在 macOS 提示时授予屏幕录制和辅助功能权限。
- `设置计算机使用`：在 Codex 设置中，打开 **计算机使用** 并点击 **安装** 以在请求 Codex 操作桌面应用之前安装计算机使用插件。当 macOS 提示访问时，如果希望 Codex …
- `何时使用计算机使用`：当任务依赖于难以仅通过文件或命令输出验证的图形用户界面时，选择计算机使用。

## 正文整理
### 正文
在 Codex 应用中，计算机使用当前适用于 macOS，但在启动时不在欧洲经济区、英国和瑞士。安装计算机使用插件，然后在 macOS 提示时授予屏幕录制和辅助功能权限。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 通过计算机使用，Codex 可以查看和操作 macOS 上的图形用户界面。可以将其用于命令行工具或结构化集成不够的任务，例如检查桌面应用、使用浏览器、更改应用设置、处理未作为插件提供的数据源，或重现仅在图形用户界面中发生的错误。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 由于计算机使用可能会影响您的项目工作区之外的应用和系统状态，请将其用于有范围的任务，并在继续之前检查权限提示。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 设置计算机使用
在 Codex 设置中，打开 **计算机使用** 并点击 **安装** 以在请求 Codex 操作桌面应用之前安装计算机使用插件。当 macOS 提示访问时，如果希望 Codex 查看和与目标应用交互，请授予屏幕录制和辅助功能权限。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 要使用计算机使用，请授予：
- **屏幕录制** 权限，以便 Codex 可以看到目标应用。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- **辅助功能** 权限，以便 Codex 可以点击、输入和导航。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 何时使用计算机使用
当任务依赖于难以仅通过文件或命令输出验证的图形用户界面时，选择计算机使用。

继续往下看，这一节还强调了两件事：
- 适合的例子包括：
- 测试 macOS 应用、iOS 模拟器流或 Codex 正在构建的其他桌面应用。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- 执行需要您的网页浏览器的任务。（实现：[web_search](/config/workspace/codex/codex-rs/core/src/web_search.rs:18)、[network_policy_decision](/config/workspace/codex/codex-rs/core/src/network_policy_decision.rs:1)、[network-proxy](/config/workspace/codex/codex-rs/network-proxy/src/lib.rs:1)）

### 开始计算机使用任务
在提示中提及 `@Computer Use` 或 `@AppName`，或要求 Codex 使用计算机使用。描述 Codex 应该操作的确切应用、窗口或流程。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 如果目标应用暴露了一个专用插件或 MCP 服务器，更喜欢使用该结构化集成来访问数据和进行可重复的操作。当 Codex 需要检查或在视觉上操作应用时，选择计算机使用。（实现：[mcp_connection_manager](/config/workspace/codex/codex-rs/core/src/mcp_connection_manager.rs:546)、[mcp_tool_call](/config/workspace/codex/codex-rs/core/src/mcp_tool_call.rs:1)、[core/mcp/mod](/config/workspace/codex/codex-rs/core/src/mcp/mod.rs:1)、[mcp-server/lib](/config/workspace/codex/codex-rs/mcp-server/src/lib.rs:51)）

### 权限和批准
macOS 系统权限与 Codex 中的应用批准是分开的。macOS 权限允许 Codex 查看和操作应用。应用批准决定您允许 Codex 使用哪些应用。文件读取、文件编辑和 shell 命令仍然遵循线程的沙箱和批准设置。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 通过计算机使用，Codex 只能在您允许的应用中查看和采取行动。在任务期间，Codex 会请求您的权限才能使用您计算机上的应用。您可以选择 **始终允许**，以便 Codex 将来可以无须再次询问地使用该应用。您可以在 Codex 设置的 **计算机使用** 部分中将应用从 **始终允许** 列表中删除。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- Codex 也可能在进行敏感或具有破坏性操作之前请求权限。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- 如果 Codex 无法看到或控制应用，请打开 **系统设置 > 隐私与安全** 并检查 Codex 应用的 **屏幕录制** 和 **辅助功能**。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
