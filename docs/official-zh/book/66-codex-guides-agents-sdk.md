# 第66章 MCP 服务器

> 原始页面：[Use Codex with the Agents SDK | OpenAI Developers](https://developers.openai.com/codex/guides/agents-sdk)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 你读完应该抓住什么
- # 作为 MCP 服务器运行 Codex
- `安装依赖项`：Agents SDK 处理 Codex 之间的编排、交接和跟踪。安装最新的 SDK 包：
- `将 Codex CLI 初始化为 MCP 服务器`：首先将 Codex CLI 转换为 Agents SDK 可以调用的 MCP 服务器。服务。

## 分步理解
### 正文
先说直白版：
# 作为 MCP 服务器运行 Codex
您可以将 Codex 作为 MCP 服务器运行，并从其他 MCP 客户端连接它（例如，用 OpenAI Agents SDK MCP 集成 构建的代理）。
要将 Codex 启动为 MCP 服务器，您可以使用以下命令：
您可以使用 模型上下文协议检查器 启动 Codex MCP 服务器：

把它理解成一个更严谨的过程：
1. # 作为 MCP 服务器运行 Codex
2. 您可以将 Codex 作为 MCP 服务器运行，并从其他 MCP 客户端连接它（例如，用 OpenAI Agents SDK MCP 集成 构建的代理）。
3. 要将 Codex 启动为 MCP 服务器，您可以使用以下命令：
4. 您可以使用 模型上下文协议检查器 启动 Codex MCP 服务器：

### 安装依赖项
先说直白版：
Agents SDK 处理 Codex 之间的编排、交接和跟踪。安装最新的 SDK 包：
激活虚拟环境可以将 SDK 依赖项与系统的其余部分隔离。

把它理解成一个更严谨的过程：
1. Agents SDK 处理 Codex 之间的编排、交接和跟踪。安装最新的 SDK 包：
2. 激活虚拟环境可以将 SDK 依赖项与系统的其余部分隔离。

### 将 Codex CLI 初始化为 MCP 服务器
先说直白版：
首先将 Codex CLI 转换为 Agents SDK 可以调用的 MCP 服务器。服务器公开两个工具（`codex()` 开始对话，`codex-reply()` 继续对话），并保持 Codex 在多个代理轮次之间处于活动状态。
创建一个名为 `codex_mcp.py` 的文件，并添加以下内容：
from agents import Agent, Runner from agents.mcp import MCPServerStdio
async def main() -> None: async with MCPServerStdio( name="Codex CLI", params={ "command": "npx", "args": ["-y", "codex", "mcp-server"], }, client_session_timeout_seconds=360000, ) as codex_mcp_server: print("Codex MCP server started.") # 更多逻辑将在后面的部分中到来。 return

把它理解成一个更严谨的过程：
1. 首先将 Codex CLI 转换为 Agents SDK 可以调用的 MCP 服务器。服务器公开两个工具（`codex()` 开始对话，`codex-reply()` 继续对话），并保持 Codex 在多个代理轮次之间处于活动状态。
2. 创建一个名为 `codex_mcp.py` 的文件，并添加以下内容：
3. from agents import Agent, Runner from agents.mcp import MCPServerStdio
4. async def main() -> None: async with MCPServerStdio( name="Codex CLI", params={ "command": "npx", "args": ["-y", "codex", "mcp-server"], }, client_session_timeout_seconds=360000, ) as codex_mcp_server: print("Codex MCP server started.") # 更多逻辑将在后面的部分中到来。 return

### 构建单代理工作流
先说直白版：
让我们从一个使用 Codex MCP 发货的小浏览器游戏的示例开始。该工作流依赖于两个代理：
1. **游戏设计师**：编写游戏简要说明。 2. **游戏开发者**：通过调用 Codex MCP 实现游戏。
使用以下代码更新 `codex_mcp.py`。它保留了上述 MCP 服务器的设置，并添加了两个代理。
from dotenv import load_dotenv

把它理解成一个更严谨的过程：
1. 让我们从一个使用 Codex MCP 发货的小浏览器游戏的示例开始。该工作流依赖于两个代理：
2. 1. **游戏设计师**：编写游戏简要说明。 2. **游戏开发者**：通过调用 Codex MCP 实现游戏。
3. 使用以下代码更新 `codex_mcp.py`。它保留了上述 MCP 服务器的设置，并添加了两个代理。
4. from dotenv import load_dotenv

### 扩展到多代理工作流
先说直白版：
现在将单代理设置转变为一个协调的、可追踪的工作流。系统增加：
- **项目经理**：创建共享需求，协调交接，并执行护栏。
- **设计师**、**前端开发者**、**服务器开发者** 和 **测试者**：每个角色都有特定的指令和输出文件夹。
创建一个名为 `multi_agent_workflow.py` 的新文件：

把它理解成一个更严谨的过程：
1. 现在将单代理设置转变为一个协调的、可追踪的工作流。系统增加：
2. **项目经理**：创建共享需求，协调交接，并执行护栏。
3. **设计师**、**前端开发者**、**服务器开发者** 和 **测试者**：每个角色都有特定的指令和输出文件夹。
4. 创建一个名为 `multi_agent_workflow.py` 的新文件：

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
