# 第62章 Windows

> 原始页面：[Windows – Codex | OpenAI Developers](https://developers.openai.com/codex/windows)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 在 Windows 上使用 Codex，使用本地 Codex 应用、CLI 或 IDE 扩展。
- `Windows 沙盒`：当您在 Windows 上本地运行 Codex 时，代理模式使用 Windows 沙盒来阻止工作文件夹之外的文件系统写入，并在没有您明确批准的情况下防止网络访问。
- `沙盒权限`：以完全访问模式运行 Codex 意味着 Codex 不受限于您的项目目录，并且可能会执行意外的破坏性操作，从而导致数据丢失。为了更安全的自动化，请保持沙盒边界，并使用 规则 进行特定例外…

## 正文整理
### 正文
在 Windows 上使用 Codex，使用本地 Codex 应用、CLI 或 IDE 扩展。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- Windows 上的 Codex 应用支持核心工作流，例如并行代理线程、工作树、自动化、Git 功能、应用内浏览器、工件预览、插件和技能。（实现：[Codex](/config/workspace/codex/codex-rs/core/src/codex.rs:285)、[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager::fork_thread](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375)、[agent/control](/config/workspace/codex/codex-rs/core/src/agent/control.rs:1)）
- \\ 在 Windows 上使用 Codex 应用\\ \\ 在一个地方跨项目工作，运行并行代理线程，并审查结果。](https://developers.openai.com/codex/app/windows)（实现：[Codex](/config/workspace/codex/codex-rs/core/src/codex.rs:285)、[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager::fork_thread](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375)、[agent/control](/config/workspace/codex/codex-rs/core/src/agent/control.rs:1)）
- 根据系统和您的设置，Codex 可以通过三种实际方式在 Windows 上运行：

### Windows 沙盒
当您在 Windows 上本地运行 Codex 时，代理模式使用 Windows 沙盒来阻止工作文件夹之外的文件系统写入，并在没有您明确批准的情况下防止网络访问。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 本地 Windows 沙盒支持包括两种模式，您可以在 `config.toml` 中配置：（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- `elevated` 是首选的本地 Windows 沙盒。它使用专用的低权限沙盒用户、文件系统权限边界、防火墙规则和本地策略更改，以便为在沙盒中运行的命令提供支持。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- `unelevated` 是回退的本地 Windows 沙盒。它使用源自您当前用户的受限 Windows 令牌运行命令，应用基于 ACL 的文件系统边界，并使用环境级离线控制，而不是专用的离线用户防火墙规则。它比 `elevated` 弱，但在管理员批准的设置因本地或企业政策被阻止时仍然有用。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 沙盒权限
以完全访问模式运行 Codex 意味着 Codex 不受限于您的项目目录，并且可能会执行意外的破坏性操作，从而导致数据丢失。为了更安全的自动化，请保持沙盒边界，并使用 规则 进行特定例外，或者将您的 批准政策设置为\\ never，以便 Codex 尝试在不请求升级权限的情况下解决问题，这取决于您的 批准和安全设置。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### Windows 版本矩阵
| Windows 版本 | 支持级别 | 备注 | | --- | --- | --- | | Windows 11 | 推荐 | Windows 上 Codex 的最佳基础线。如果您要标准化企业部署，请使用此版本。 | | 最近的、完全更新的 Windows 10 | 尽力而为 | 可以工作，但比 Windows 11 不太可靠。对于 Windows 1…

继续往下看，这一节还强调了两件事：
- 其他环境假设：
- `winget` 应该可用。如果它缺失，请在设置 Codex 之前更新 Windows 或安装 Windows 安装程序。
- 推荐的本地沙盒取决于管理员批准的设置。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 授予沙盒读取访问
当命令因为 Windows 沙盒无法读取目录而失败时，请使用：（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 路径必须是现有的绝对目录。命令成功后，后续在沙盒中运行的命令可以在当前会话期间读取该目录。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- 默认情况下，使用本地 Windows 沙盒。本地 Windows 沙盒提供最佳性能和最高速度，同时保持相同的安全性。当您需要 Windows 上的 Linux 本地环境时，选择 WSL2，或者当工作流已经存在于 WSL2 中时，或当没有哪种本地 Windows 沙盒模式满足您的需求时。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
