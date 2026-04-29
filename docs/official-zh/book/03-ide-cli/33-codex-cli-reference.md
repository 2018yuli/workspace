# 第33章 命令行选项

> 原始页面：[Command line options – Codex CLI | OpenAI Developers](https://developers.openai.com/codex/cli/reference)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `如何阅读此参考`：此页面记录了每个文档化的 Codex CLI 命令和标志。使用互动表格按关键字或描述进行搜索。每个部分指示该选项是否稳定或实验性，并指出有风险的组合。
- `全局标志`：| 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--add-dir` | `path` | 授予其他目录与主工作区相同的写入访问权限。重复以获取…
- `命令概述`：成熟度列使用功能成熟度标签，例如实验性、Beta 和稳定。有关如何解释这些标签的信息，请参见 功能成熟度。

## 正文整理
### 如何阅读此参考
此页面记录了每个文档化的 Codex CLI 命令和标志。使用互动表格按关键字或描述进行搜索。每个部分指示该选项是否稳定或实验性，并指出有风险的组合。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- CLI 从 `~/.codex/config.toml` 继承大多数默认值。任何您在命令行中传递的 `-c key=value` 重写在该调用中优先使用。有关更多信息，请参见 配置基础。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 全局标志
| 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--add-dir` | `path` | 授予其他目录与主工作区相同的写入访问权限。重复以获取多个路径。 | | `--ask-for-approval, -a` | `untrusted | on-request | never` | 控制 Codex 在运行命令之…（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 键
- `--add-dir`
- 类型 / 值

### 命令概述
成熟度列使用功能成熟度标签，例如实验性、Beta 和稳定。有关如何解释这些标签的信息，请参见 功能成熟度。

继续往下看，这一节还强调了两件事：
- | 键 | 成熟度 | 详细信息 | | --- | --- | --- | | `codex` | 稳定 | 启动终端用户界面。接受上述全局标志以及可选提示或图像附加。 | | `codex app` | 稳定 | 在 macOS 或 Windows 上启动 Codex 桌面应用。 在 macOS 上，Codex 可以打开工作区路径；在 Windows 上…（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 键
- 成熟度

### `codex`（交互式）
运行 `codex` 而不带子命令启动交互式终端用户界面（TUI）。代理接受上述全局标志以及图像附件。网络搜索默认为缓存模式；使用 `--search` 切换到实时浏览，并使用 `--full-auto` 让 Codex 在没有提示的情况下运行大部分命令。（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)、[web_search](/codex/codex-rs/core/src/web_search.rs#L18)）

继续往下看，这一节还强调了两件事：
- 使用 `--remote ws://host:port` 或 `--remote wss://host:port` 将 TUI 连接到使用 `codex app-server --listen ws://IP:PORT` 启动的应用服务器。当前服务器需要承载令牌进行 WebSocket 身份验证时，请添加 `--remote-auth-token-env <…（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）

### `codex app-server`
在本地启动 Codex 应用服务器。这主要用于开发和调试，可能会更改而不另行通知。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- | 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--listen` | `stdio:// | ws://IP:PORT` | 传输监听器 URL。使用 `ws://IP:PORT` 为远程客户端公开 WebSocket 端点。 | | `--ws-audience` | `string` | 签名的承载令牌预期的 …（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 键
- `--listen`

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
