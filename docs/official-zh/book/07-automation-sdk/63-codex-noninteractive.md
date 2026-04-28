# 第63章 非交互模式

> 原始页面：[Non-interactive mode – Codex | OpenAI Developers](https://developers.openai.com/codex/noninteractive)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 非交互模式允许您从脚本（例如，持续集成（CI）作业）运行 Codex，而无需打开交互式 TUI。 您可以通过 `codex exec` 进行调用。
- `何时使用 `codex exec``：当您希望 Codex：
- `基本用法`：将任务提示作为单个参数传递：

## 正文整理
### 正文
非交互模式允许您从脚本（例如，持续集成（CI）作业）运行 Codex，而无需打开交互式 TUI。 您可以通过 `codex exec` 进行调用。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

继续往下看，这一节还强调了两件事：
- 有关标志级详细信息，请参见 `codex exec`。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

### 何时使用 `codex exec`
当您希望 Codex：

继续往下看，这一节还强调了两件事：
- 作为管道的一部分运行（CI、预合并检查、定时作业）。（实现：[StateRuntime::create_agent_job](/config/workspace/codex/codex-rs/state/src/runtime.rs:917)、[StateRuntime::report_agent_job_item_result](/config/workspace/codex/codex-rs/state/src/runtime.rs:1337)、[cloud-tasks App](/config/workspace/codex/codex-rs/cloud-tasks/src/app.rs:47)、[cloud-tasks CLI](/config/workspace/codex/codex-rs/cloud-tasks/src/cli.rs:7)）
- 生成可以传递给其他工具的输出（例如，生成发布说明或总结）。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 自然地适应将命令输出链入 Codex 并将 Codex 输出传递给其他工具的 CLI 工作流。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

### 基本用法
将任务提示作为单个参数传递：（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）

继续往下看，这一节还强调了两件事：
- 在 `codex exec` 运行时，Codex 将进度流式传输到 `stderr`，并仅将最终代理消息打印到 `stdout`。这使得重定向或管道最后的结果变得简单：（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 当您不希望会话回滚文件持久化到磁盘时，使用 `--ephemeral`：（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- 如果 `stdin` 通过管道传输，并且您还提供了提示参数，Codex 会将提示视为指令，并将管道内容作为附加上下文。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

### 权限和安全
默认情况下，`codex exec` 在只读沙箱中运行。在自动化中，为工作流设置最低所需权限：（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

继续往下看，这一节还强调了两件事：
- 允许编辑：`codex exec --full-auto "<task>"`（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 允许更广泛的访问：`codex exec --sandbox danger-full-access "<task>"`（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- 仅在受控环境中使用 `danger-full-access`（例如，隔离的 CI 运行器或容器）。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

### 使输出机器可读
要在脚本中使用 Codex 输出，使用 JSON Lines 输出：

继续往下看，这一节还强调了两件事：
- 启用 `--json` 时，`stdout` 变为 JSON Lines（JSONL）流，因此您可以捕获 Codex 在运行时发出的每个事件。事件类型包括 `thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*` 和 `error`。
- 项目类型包括代理消息、推理、命令执行、文件更改、MCP 工具调用、网络搜索和计划更新。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 示例 JSON 流（每一行都是一个 JSON 对象）：

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
