# 第63章 非交互模式

> 原始页面：[Non-interactive mode – Codex | OpenAI Developers](https://developers.openai.com/codex/noninteractive)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。

## 严谨定义
严格地说，提示是对目标函数、约束条件和验证标准的联合描述。

## 你读完应该抓住什么
- 非交互模式允许您从脚本（例如，持续集成（CI）作业）运行 Codex，而无需打开交互式 TUI。 您可以通过 `codex exec` 进行调用。
- `何时使用 `codex exec``：当您希望 Codex：
- `基本用法`：将任务提示作为单个参数传递：

## 分步理解
### 正文
先说直白版：
非交互模式允许您从脚本（例如，持续集成（CI）作业）运行 Codex，而无需打开交互式 TUI。 您可以通过 `codex exec` 进行调用。
有关标志级详细信息，请参见 `codex exec`。

把它理解成一个更严谨的过程：
1. 非交互模式允许您从脚本（例如，持续集成（CI）作业）运行 Codex，而无需打开交互式 TUI。 您可以通过 `codex exec` 进行调用。
2. 有关标志级详细信息，请参见 `codex exec`。

### 何时使用 `codex exec`
先说直白版：
当您希望 Codex：
- 作为管道的一部分运行（CI、预合并检查、定时作业）。
- 生成可以传递给其他工具的输出（例如，生成发布说明或总结）。
- 自然地适应将命令输出链入 Codex 并将 Codex 输出传递给其他工具的 CLI 工作流。

把它理解成一个更严谨的过程：
1. 当您希望 Codex：
2. 作为管道的一部分运行（CI、预合并检查、定时作业）。
3. 生成可以传递给其他工具的输出（例如，生成发布说明或总结）。
4. 自然地适应将命令输出链入 Codex 并将 Codex 输出传递给其他工具的 CLI 工作流。

### 基本用法
先说直白版：
将任务提示作为单个参数传递：
在 `codex exec` 运行时，Codex 将进度流式传输到 `stderr`，并仅将最终代理消息打印到 `stdout`。这使得重定向或管道最后的结果变得简单：
当您不希望会话回滚文件持久化到磁盘时，使用 `--ephemeral`：
如果 `stdin` 通过管道传输，并且您还提供了提示参数，Codex 会将提示视为指令，并将管道内容作为附加上下文。

把它理解成一个更严谨的过程：
1. 将任务提示作为单个参数传递：
2. 在 `codex exec` 运行时，Codex 将进度流式传输到 `stderr`，并仅将最终代理消息打印到 `stdout`。这使得重定向或管道最后的结果变得简单：
3. 当您不希望会话回滚文件持久化到磁盘时，使用 `--ephemeral`：
4. 如果 `stdin` 通过管道传输，并且您还提供了提示参数，Codex 会将提示视为指令，并将管道内容作为附加上下文。

### 权限和安全
先说直白版：
默认情况下，`codex exec` 在只读沙箱中运行。在自动化中，为工作流设置最低所需权限：
- 允许编辑：`codex exec --full-auto "<task>"`
- 允许更广泛的访问：`codex exec --sandbox danger-full-access "<task>"`
仅在受控环境中使用 `danger-full-access`（例如，隔离的 CI 运行器或容器）。

把它理解成一个更严谨的过程：
1. 默认情况下，`codex exec` 在只读沙箱中运行。在自动化中，为工作流设置最低所需权限：
2. 允许编辑：`codex exec --full-auto "<task>"`
3. 允许更广泛的访问：`codex exec --sandbox danger-full-access "<task>"`
4. 仅在受控环境中使用 `danger-full-access`（例如，隔离的 CI 运行器或容器）。

### 使输出机器可读
先说直白版：
要在脚本中使用 Codex 输出，使用 JSON Lines 输出：
启用 `--json` 时，`stdout` 变为 JSON Lines（JSONL）流，因此您可以捕获 Codex 在运行时发出的每个事件。事件类型包括 `thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*` 和 `error`。
项目类型包括代理消息、推理、命令执行、文件更改、MCP 工具调用、网络搜索和计划更新。
示例 JSON 流（每一行都是一个 JSON 对象）：

把它理解成一个更严谨的过程：
1. 要在脚本中使用 Codex 输出，使用 JSON Lines 输出：
2. 启用 `--json` 时，`stdout` 变为 JSON Lines（JSONL）流，因此您可以捕获 Codex 在运行时发出的每个事件。事件类型包括 `thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*` 和 `error`。
3. 项目类型包括代理消息、推理、命令执行、文件更改、MCP 工具调用、网络搜索和计划更新。
4. 示例 JSON 流（每一行都是一个 JSON 对象）：

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
