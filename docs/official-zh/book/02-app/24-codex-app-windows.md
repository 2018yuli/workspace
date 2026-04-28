# 第24章 Windows

> 原始页面：[Windows – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/windows)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- Windows 应用支持核心工作流，如工作树、自动化、Git 功能、应用内浏览器、工件预览、插件和技能。 它在 Windows 上本地运行，使用 PowerShell 和Windows 沙盒，或者您可…
- `下载并更新 Codex 应用`：从Microsoft Store下载 Codex 应用。
- `原生沙盒`：Windows 上的 Codex 应用支持当代理在 PowerShell 中运行时的原生 Windows 沙盒，并且在您运行代理时使用 Windows 子系统 Linux 2 (WSL2…

## 正文整理
### 正文
Windows 应用支持核心工作流，如工作树、自动化、Git 功能、应用内浏览器、工件预览、插件和技能。 它在 Windows 上本地运行，使用 PowerShell 和Windows 沙盒，或者您可以配置它在Windows 子系统 Linux 2 (WSL2)中运行。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 下载并更新 Codex 应用
从Microsoft Store下载 Codex 应用。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 然后按照快速开始进行操作。
- 要更新应用，请打开 Microsoft Store，转到 **下载**，然后点击 **检查更新**。之后，Store 会安装最新版本。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- 对于企业，管理员可以通过企业管理工具使用 Microsoft Store 应用分发来部署应用。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

### 原生沙盒
Windows 上的 Codex 应用支持当代理在 PowerShell 中运行时的原生 Windows 沙盒，并且在您运行代理时使用 Windows 子系统 Linux 2 (WSL2) 时使用 Linux 沙盒。当您在任何模式下应用沙盒保护时，请在 Composer 中将沙盒权限设置为 **默认权限**，然后再向 Codex 发送消息。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 以完全访问模式运行 Codex 意味着 Codex 不受限于您的项目目录，并且可能会执行导致数据丢失的意外破坏性操作。保持沙盒边界，并使用 规则 进行有针对性的例外情况，或将您的 批准策略设置为\\ 从不，以使 Codex 尝试解决问题而不请求更高权限，基于您的 批准和安全设置。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 首选编辑器
选择一个默认应用程序用于 **打开**，例如 Visual Studio、VS Code 或其他编辑器。您可以针对每个项目覆盖该选择。如果您已经为项目从 **打开** 菜单中选择了不同的应用程序，则该项目特定的选择优先。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### 集成终端
您还可以选择默认的集成终端。根据您安装的内容，选项包括：

继续往下看，这一节还强调了两件事：
- PowerShell（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 命令提示符（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）
- Git Bash（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
