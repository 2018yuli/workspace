# 第15章 功能

> 原始页面：[Features – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/features)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- Codex 应用是一个专注的桌面体验，旨在并行处理 Codex 线程，具有内置的工作树支持、自动化和 Git 功能。
- `在项目间多任务处理`：使用一个 Codex 应用窗口在项目间运行任务。为每个代码库添加一个项目，并在需要时切换它们。
- `技能支持`：Codex 应用支持与 CLI 和 IDE 扩展相同的 代理技能。您还可以通过单击侧边栏中的技能查看和探索您的团队在不同项目中创建的新技能。

## 正文整理
### 正文
Codex 应用是一个专注的桌面体验，旨在并行处理 Codex 线程，具有内置的工作树支持、自动化和 Git 功能。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 大多数 Codex 应用功能在 macOS 和 Windows 上均可用。以下部分注意平台特定的例外情况。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- * * *

### 在项目间多任务处理
使用一个 Codex 应用窗口在项目间运行任务。为每个代码库添加一个项目，并在需要时切换它们。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 如果您使用过 Codex CLI，项目就像是在特定目录中启动一个会话。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 如果您在一个单一的代码库中有两个或多个应用或软件包，请将不同的项目分成单独的应用项目，这样 沙盒 中仅包括该项目的文件。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 技能支持
Codex 应用支持与 CLI 和 IDE 扩展相同的 代理技能。您还可以通过单击侧边栏中的技能查看和探索您的团队在不同项目中创建的新技能。（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）

### 自动化
您还可以将技能与 自动化 结合，执行常规任务，例如评估您在遥测中的错误并提交修复或创建有关最近代码库更改的报告。对于应该保持在一个线程中的持续工作，使用 线程自动化。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 模式
每个线程在选择的模式下运行。开始线程时，您可以选择：（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- **本地**：直接在您当前的项目目录中工作。
- **工作树**：在 Git 工作树中隔离更改。了解更多。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）
- **云**：在配置的云环境中远程运行。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
