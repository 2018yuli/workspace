# 第25章 故障排除

> 原始页面：[Troubleshooting – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/troubleshooting)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `文件出现在侧边栏中，而 Codex 并未编辑`：如果你的项目在 Git 仓库内，审查面板会自动显示基于项目的 Git 状态的更改，包括 Codex 未进行的更改。
- `从侧边栏移除项目`：要从侧边栏移除项目，将鼠标悬停在项目名称上，点击三个点并选择“移除”。要恢复它，请使用 **添加新项目** 按钮或使用 `Cmd` + `O` 重新添加项目。
- `找到归档的线程`：归档的线程可以在 设置 中找到。当你取消归档线程时，它将重新出现在侧边栏的原始位置。

## 正文整理
### 文件出现在侧边栏中，而 Codex 并未编辑
如果你的项目在 Git 仓库内，审查面板会自动显示基于项目的 Git 状态的更改，包括 Codex 未进行的更改。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- 在审查面板中，你可以在暂存的更改和未暂存的更改之间切换，并比较你的分支与主分支。
- 如果你只想查看最后一次 Codex 操作的更改，请将差异面板切换到“最后一次更改”视图。

### 从侧边栏移除项目
要从侧边栏移除项目，将鼠标悬停在项目名称上，点击三个点并选择“移除”。要恢复它，请使用 **添加新项目** 按钮或使用 `Cmd` + `O` 重新添加项目。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 找到归档的线程
归档的线程可以在 设置 中找到。当你取消归档线程时，它将重新出现在侧边栏的原始位置。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 只有一些线程出现在侧边栏
侧边栏允许根据项目的状态过滤线程。如果你缺少线程，请点击 **线程** 标签旁边的过滤图标并切换到按时间顺序排列。如果仍然没有看到线程，请打开 设置 并检查归档聊天或归档线程部分。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 代码在工作树上无法运行
工作树是在不同目录中创建的，仅继承已检查到 Git 的文件。根据你管理项目的依赖项和工具的方式，你可能需要在工作树上运行一些设置脚本，使用 本地环境。或者，你可以在常规本地项目中查看更改。查看 工作树文档 以了解更多信息。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
