# 第65章 应用服务器

> 原始页面：[App Server – Codex | OpenAI Developers](https://developers.openai.com/codex/app-server)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把自动化看成数列中的递推过程。你先给出初值和递推规则，之后系统会在每个时刻自动算出下一项。

## 严谨定义
严格地说，自动化就是一个由“触发条件 + 指令 + 执行环境 + 输出汇总”组成的重复映射。

## 你读完应该抓住什么
- Codex 应用服务器是 Codex 用于支持丰富客户端的接口（例如，Codex VS Code 扩展）。当您希望将 Codex 深入集成到自己。
- `协议`：如同 MCP，`codex app-server` 支持使用 JSON-RPC 2.0 消息进行双向通信（在传输中省略了 `"json。
- `消息模式`：请求包括 `method`，`params` 和 `id`：

## 分步理解
### 正文
先说直白版：
Codex 应用服务器是 Codex 用于支持丰富客户端的接口（例如，Codex VS Code 扩展）。当您希望将 Codex 深入集成到自己的产品中时，请使用它：身份验证、对话历史、审批和流式代理事件。应用服务器实现是开源的，可以在 Codex GitHub 仓库中找到（ openai/codex/codex-rs/app-server）。有关开源 Codex 组件的完整列表，请参见 开源 页面。
如果您正在自动化工作或在 CI 中运行 Codex，请使用

把它理解成一个更严谨的过程：
1. Codex 应用服务器是 Codex 用于支持丰富客户端的接口（例如，Codex VS Code 扩展）。当您希望将 Codex 深入集成到自己的产品中时，请使用它：身份验证、对话历史、审批和流式代理事件。应用服务器实现是开源的，可以在 Codex GitHub 仓库中找到（ openai/codex/codex-rs/app-server）。有关开源 Codex 组件的完整列表，请参见 开源 页面。
2. 如果您正在自动化工作或在 CI 中运行 Codex，请使用

### 协议
先说直白版：
如同 MCP，`codex app-server` 支持使用 JSON-RPC 2.0 消息进行双向通信（在传输中省略了 `"jsonrpc":"2.0"` 头）。
支持的传输：
- `stdio` (`--listen stdio://`, 默认)：以换行分隔的 JSON（JSONL）。
- `websocket` (`--listen ws://IP:PORT`, 实验性且不支持)：每个 WebSocket 文本帧一个 JSON-RPC 消息。

把它理解成一个更严谨的过程：
1. 如同 MCP，`codex app-server` 支持使用 JSON-RPC 2.0 消息进行双向通信（在传输中省略了 `"jsonrpc":"2.0"` 头）。
2. 支持的传输：
3. `stdio` (`--listen stdio://`, 默认)：以换行分隔的 JSON（JSONL）。
4. `websocket` (`--listen ws://IP:PORT`, 实验性且不支持)：每个 WebSocket 文本帧一个 JSON-RPC 消息。

### 消息模式
先说直白版：
请求包括 `method`，`params` 和 `id`：
响应会以 `id` 附 Echo，带有 `result` 或 `error`：
通知省略 `id`，仅使用 `method` 和 `params`：
您可以从 CLI 生成 TypeScript 模式或 JSON 模式包。每个输出特定于您运行的 Codex 版本，因此生成的工件与该版本完全匹配：

把它理解成一个更严谨的过程：
1. 请求包括 `method`，`params` 和 `id`：
2. 响应会以 `id` 附 Echo，带有 `result` 或 `error`：
3. 通知省略 `id`，仅使用 `method` 和 `params`：
4. 您可以从 CLI 生成 TypeScript 模式或 JSON 模式包。每个输出特定于您运行的 Codex 版本，因此生成的工件与该版本完全匹配：

### 入门
先说直白版：
1. 使用 `codex app-server` 启动服务器（默认 stdio 传输）或使用 `codex app-server --listen ws://127.0.0.1:4500`（实验性 WebSocket 传输）。 2. 通过所选传输连接客户端，然后发送 `initialize`，接着是 `initialized` 通知。 3. 启动线程和回合，然后持续读取活动传输流中的通知。
示例（Node.js / TypeScript）：
const proc = spawn("codex", ["app-server"], { stdio: ["pipe", "pipe", "inherit"], }); const rl = readline.createInterface({ input: proc.stdout });
const send = (message: unknown) => { proc.stdin.write(`${JSON.stringify(message)}\n`); };

把它理解成一个更严谨的过程：
1. 1. 使用 `codex app-server` 启动服务器（默认 stdio 传输）或使用 `codex app-server --listen ws://127.0.0.1:4500`（实验性 WebSocket 传输）。 2. 通过所选传输连接客户端，然后发送 `initialize`，接着是 `initialized` 通知。 3. 启动线程和回合，然后持续读取活动传输流中的通知。
2. 示例（Node.js / TypeScript）：
3. const proc = spawn("codex", ["app-server"], { stdio: ["pipe", "pipe", "inherit"], }); const rl = readline.createInterface({ input: proc.stdout });
4. const send = (message: unknown) => { proc.stdin.write(`${JSON.stringify(message)}\n`); };

### 核心原语
先说直白版：
- **线程**：用户和 Codex 代理之间的对话。线程包含回合。
- **回合**：单个用户请求及随之而来的代理工作。回合包含项目并流式更新。
- **项目**：输入或输出的单位（用户消息、代理消息、命令运行、文件更改、工具调用等）。
使用线程 API 创建、列出或归档对话。使用回合 API 驱动对话，并通过回合通知流进度。

把它理解成一个更严谨的过程：
1. **线程**：用户和 Codex 代理之间的对话。线程包含回合。
2. **回合**：单个用户请求及随之而来的代理工作。回合包含项目并流式更新。
3. **项目**：输入或输出的单位（用户消息、代理消息、命令运行、文件更改、工具调用等）。
4. 使用线程 API 创建、列出或归档对话。使用回合 API 驱动对话，并通过回合通知流进度。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
