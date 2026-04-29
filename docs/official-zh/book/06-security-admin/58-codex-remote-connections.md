# 第58章 远程连接

> 原始页面：[Remote connections – Codex | OpenAI Developers](https://developers.openai.com/codex/remote-connections)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
线程像解一道多步函数题时保留下来的草稿纸。后一步是否顺利，依赖前面保留下来的中间结果。

## 严谨定义
严格地说，线程是一个按时间顺序累积状态的信息序列。

## 本章先抓重点
- SSH 远程连接目前处于 alpha 阶段。要今天启用它，请在 `~/.codex/config.toml` 中的 `[features]` 表中设置 `remote_connections = tr…
- `Codex 应用`：在 Codex 应用中，从 SSH 主机添加远程项目并在远程文件系统和 shell 上运行线程。
- `身份验证和网络暴露`：使用 SSH 端口转发和本地主机 WebSocket 侦听器。不要在共享或公共网络上公开未验证的应用服务器侦听器。

## 正文整理
### 正文
SSH 远程连接目前处于 alpha 阶段。要今天启用它，请在 `~/.codex/config.toml` 中的 `[features]` 表中设置 `remote_connections = true`。可用性、设置流程和支持的环境可能会随着功能的改进而变化。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 远程连接让 Codex 可以处理在另一台可以通过 SSH 访问的计算机上的项目。当您需要的代码库、凭据、服务或构建环境可在该主机上而不是您的本地计算机上时，使用它们。
- 请保持远程主机的配置与用于正常 SSH 访问的安全预期一致：信任的密钥、最小权限帐户和无身份验证的公共侦听器。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### Codex 应用
在 Codex 应用中，从 SSH 主机添加远程项目并在远程文件系统和 shell 上运行线程。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 1. 将主机添加到您的 SSH 配置中，以便 Codex 可以自动发现它。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- Codex 从 `~/.ssh/config` 中读取具体主机别名，并通过 OpenSSH 解析它们，忽略仅具有模式的主机。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 2. 确认您可以从运行 Codex 应用的计算机 SSH 到该主机。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 身份验证和网络暴露
使用 SSH 端口转发和本地主机 WebSocket 侦听器。不要在共享或公共网络上公开未验证的应用服务器侦听器。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 如果您需要访问在当前网络外的远程计算机，请使用 VPN 或网状网络工具，例如 Tailscale，而不是直接将应用服务器暴露在互联网上。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

### 另见
Codex 应用设置（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 命令行选项
- 身份验证

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
