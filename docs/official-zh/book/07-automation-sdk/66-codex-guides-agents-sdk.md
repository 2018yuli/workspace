# 第66章 MCP 服务器

> 原始页面：[Use Codex with the Agents SDK | OpenAI Developers](https://developers.openai.com/codex/guides/agents-sdk)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 本章先抓重点
- # 作为 MCP 服务器运行 Codex
- `安装依赖项`：Agents SDK 处理 Codex 之间的编排、交接和跟踪。安装最新的 SDK 包：
- `将 Codex CLI 初始化为 MCP 服务器`：首先将 Codex CLI 转换为 Agents SDK 可以调用的 MCP 服务器。服务器公开两个工具（`codex()` 开始对话，`code…

## 正文整理
### 正文
# 作为 MCP 服务器运行 Codex（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）

继续往下看，这一节还强调了两件事：
- 您可以将 Codex 作为 MCP 服务器运行，并从其他 MCP 客户端连接它（例如，用 OpenAI Agents SDK MCP 集成 构建的代理）。（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- 要将 Codex 启动为 MCP 服务器，您可以使用以下命令：（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- 您可以使用 模型上下文协议检查器 启动 Codex MCP 服务器：（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 安装依赖项
Agents SDK 处理 Codex 之间的编排、交接和跟踪。安装最新的 SDK 包：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）

继续往下看，这一节还强调了两件事：
- 激活虚拟环境可以将 SDK 依赖项与系统的其余部分隔离。

### 将 Codex CLI 初始化为 MCP 服务器
首先将 Codex CLI 转换为 Agents SDK 可以调用的 MCP 服务器。服务器公开两个工具（`codex()` 开始对话，`codex-reply()` 继续对话），并保持 Codex 在多个代理轮次之间处于活动状态。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

继续往下看，这一节还强调了两件事：
- 创建一个名为 `codex_mcp.py` 的文件，并添加以下内容：（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- from agents import Agent, Runner from agents.mcp import MCPServerStdio（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- async def main() -> None: async with MCPServerStdio( name="Codex CLI", params={ "command": "npx", "args": ["-y", "codex", "mcp-server"], }, client_ses…（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）

### 构建单代理工作流
让我们从一个使用 Codex MCP 发货的小浏览器游戏的示例开始。该工作流依赖于两个代理：（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）

继续往下看，这一节还强调了两件事：
- 1. **游戏设计师**：编写游戏简要说明。 2. **游戏开发者**：通过调用 Codex MCP 实现游戏。（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- 使用以下代码更新 `codex_mcp.py`。它保留了上述 MCP 服务器的设置，并添加了两个代理。（实现：[mcp_connection_manager](/codex/codex-rs/core/src/mcp_connection_manager.rs#L546)、[mcp_tool_call](/codex/codex-rs/core/src/mcp_tool_call.rs#L1)、[core/mcp/mod](/codex/codex-rs/core/src/mcp/mod.rs#L1)、[mcp-server/lib](/codex/codex-rs/mcp-server/src/lib.rs#L51)）
- from dotenv import load_dotenv

### 扩展到多代理工作流
现在将单代理设置转变为一个协调的、可追踪的工作流。系统增加：

继续往下看，这一节还强调了两件事：
- **项目经理**：创建共享需求，协调交接，并执行护栏。
- **设计师**、**前端开发者**、**服务器开发者** 和 **测试者**：每个角色都有特定的指令和输出文件夹。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 创建一个名为 `multi_agent_workflow.py` 的新文件：

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
