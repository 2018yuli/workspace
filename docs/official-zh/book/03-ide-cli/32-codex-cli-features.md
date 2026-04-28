# 第32章 功能

> 原始页面：[Features – Codex CLI | OpenAI Developers](https://developers.openai.com/codex/cli/features)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- Codex 支持超越聊天的工作流。使用本指南学习每个工作流解锁的功能以及何时使用它。
- `在交互模式下运行`：Codex 启动为全屏终端 UI，可以读取您的代码库、进行编辑并在您一起迭代时运行命令。每当您想要一个可以实时查看 Codex 动作的对话式工作流时，请使用它。
- `恢复对话`：Codex 将您的记录保存在本地，因此您可以从上次停下的地方继续，而无需重复上下文。当您想使用相同的代码库状态和指令重新打开先前线程时，请使用 `resume` 子命令。

## 正文整理
### 正文
Codex 支持超越聊天的工作流。使用本指南学习每个工作流解锁的功能以及何时使用它。

### 在交互模式下运行
Codex 启动为全屏终端 UI，可以读取您的代码库、进行编辑并在您一起迭代时运行命令。每当您想要一个可以实时查看 Codex 动作的对话式工作流时，请使用它。

继续往下看，这一节还强调了两件事：
- 您还可以在命令行中指定初始提示。（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）
- 一旦会话打开，您可以：（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- 将提示、代码片段或截图（见 图像输入）直接发送到编写器。（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）

### 恢复对话
Codex 将您的记录保存在本地，因此您可以从上次停下的地方继续，而无需重复上下文。当您想使用相同的代码库状态和指令重新打开先前线程时，请使用 `resume` 子命令。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- `codex resume` 启动最近交互会话的选择器。高亮显示一轮以查看其摘要，然后按 `Enter` 重新打开它。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- `codex resume --all` 显示当前工作目录之外的会话，因此您可以重新打开任何本地运行。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- `codex resume --last` 跳过选择器，直接跳转到当前工作目录的最近会话（添加 `--all` 以忽略当前工作目录过滤）。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

### 将 TUI 连接到远程应用服务器
远程 TUI 模式允许您在一台机器上运行 Codex 应用服务器，并从另一台机器使用 Codex 终端 UI。这在代码、凭证或执行环境位于远程主机上，但您想要本地交互式 TUI 体验时非常有用。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 在应拥有工作区并运行命令的机器上启动应用服务器：（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- 然后从运行 TUI 的机器连接：
- 要从另一台机器访问，请将应用服务器绑定到可访问的接口，例如：（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

### 模型和推理
对于 Codex 中的大多数任务，当可用时推荐使用 `gpt-5.5` 模型。这是 OpenAI 用于复杂编码、计算机使用、知识工作和研究工作流的最新前沿模型，具有更强的计划、工具使用和对多步骤任务的跟进能力。如果 `gpt-5.5` 尚不可用，请继续使用 `gpt-5.4`。对于额外快速的任务，ChatGPT Pro 订阅者可以访问 GPT-5.3-Cod…（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

继续往下看，这一节还强调了两件事：
- 使用 `/model` 命令在会话期间切换模型，或在启动 CLI 时指定一个。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
