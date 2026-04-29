# 第16章 设置

> 原始页面：[Settings – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/settings)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用设置面板调整 Codex 应用的行为，文件打开方式和连接工具的方式。从应用菜单打开 **设置** 或按 `Cmd` + `,`。
- `一般`：选择文件打开的位置，以及命令输出在线程中出现的数量。你还可以要求在多行提示时需要按 `Cmd` + `Enter`，或在线程运行时防止睡眠。
- `通知`：选择完成通知何时出现，以及应用是否应提示通知权限。

## 正文整理
### 正文
使用设置面板调整 Codex 应用的行为，文件打开方式和连接工具的方式。从应用菜单打开 **设置** 或按 `Cmd` + `,`。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

### 一般
选择文件打开的位置，以及命令输出在线程中出现的数量。你还可以要求在多行提示时需要按 `Cmd` + `Enter`，或在线程运行时防止睡眠。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 通知
选择完成通知何时出现，以及应用是否应提示通知权限。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 代理配置
应用中的 Codex 代理继承 IDE 和 CLI 扩展的相同配置。使用应用内控件设置常见选项，或者编辑 `config.toml` 进行高级选项。有关更多详细信息，请参见 Codex 安全 和 配置基础。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 外观
在 **设置** 中，您可以通过选择基本主题、调整强调色、背景和前景颜色，以及更改 UI 和代码字体来改变 Codex 应用的外观。您还可以与朋友分享您的自定义主题。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
