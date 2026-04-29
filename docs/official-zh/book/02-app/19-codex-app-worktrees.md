# 第19章 工作树

> 原始页面：[Worktrees – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/worktrees)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把自动化看成数列中的递推过程。你先给出初值和递推规则，之后系统会在每个时刻自动算出下一项。

## 严谨定义
严格地说，自动化就是一个由“触发条件 + 指令 + 执行环境 + 输出汇总”组成的重复映射。

## 本章先抓重点
- 在 Codex 应用中，工作树使 Codex 能够在同一个项目中运行多个独立任务，而不会相互干扰。对于 Git 仓库，自动化 在专用后台工作树上运行，以免与您正在进行的工作发生冲突。在非版本控制的项目…
- `什么是工作树`：工作树仅在 Git 仓库中的项目中有效，因为它们在底层使用 Git 工作树。工作树允许您创建仓库的第二个副本（“检出”）。每个工作树都有您仓库中每个文件的独立副本，但它们都共享有关提…
- `术语`：- **本地检出**：您创建的仓库。在 Codex 应用中有时仅称为 **本地**。

## 正文整理
### 正文
在 Codex 应用中，工作树使 Codex 能够在同一个项目中运行多个独立任务，而不会相互干扰。对于 Git 仓库，自动化 在专用后台工作树上运行，以免与您正在进行的工作发生冲突。在非版本控制的项目中，自动化直接在项目目录中运行。您还可以手动在工作树上启动线程，并使用 Handoff 将线程在本地和工作树之间移动。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 什么是工作树
工作树仅在 Git 仓库中的项目中有效，因为它们在底层使用 Git 工作树。工作树允许您创建仓库的第二个副本（“检出”）。每个工作树都有您仓库中每个文件的独立副本，但它们都共享有关提交、分支等相同的元数据（`.git` 文件夹）。这使您能够并行检出并在多个分支上工作。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

### 术语
**本地检出**：您创建的仓库。在 Codex 应用中有时仅称为 **本地**。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- **工作树**：从您在 Codex 应用中本地检出创建的 Git 工作树。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）
- **Handoff**：将线程在本地和工作树之间移动的流程。Codex 处理所需的 Git 操作，以安全地在它们之间移动您的工作。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 为什么使用工作树
1. 与 Codex 并行工作，而不会干扰您当前的本地设置。 2. 在您专注于前台的同时排队后台工作。 3. 当您准备好检查、测试或更直接地协作时，将线程移动到本地。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 入门
工作树需要一个 Git 仓库。确保您选择的项目位于其中。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- 1. 选择“工作树”（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）
- 在新线程视图中，在撰写器下选择 **工作树**。 可选地，选择一个 本地环境 来运行工作树的设置脚本。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 2. 选择起始分支

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
