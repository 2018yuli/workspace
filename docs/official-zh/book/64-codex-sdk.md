# 第64章 Codex SDK

> 原始页面：[SDK – Codex | OpenAI Developers](https://developers.openai.com/codex/sdk)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 你读完应该抓住什么
- 如果你通过 Codex CLI、IDE 扩展或 Codex Web 使用 Codex，你也可以通过编程方式控制它。
- `TypeScript 库`：TypeScript 库提供了一种在应用程序中控制 Codex 的方式，比非交互模式更全面和灵活。
- `安装`：要开始使用，使用 `npm` 安装 Codex SDK：

## 分步理解
### 正文
先说直白版：
如果你通过 Codex CLI、IDE 扩展或 Codex Web 使用 Codex，你也可以通过编程方式控制它。
当你需要时使用 SDK：
- 将 Codex 作为 CI/CD 流程的一部分进行控制
- 创建自己的代理，可以与 Codex 互动以执行复杂的工程任务

把它理解成一个更严谨的过程：
1. 如果你通过 Codex CLI、IDE 扩展或 Codex Web 使用 Codex，你也可以通过编程方式控制它。
2. 当你需要时使用 SDK：
3. 将 Codex 作为 CI/CD 流程的一部分进行控制
4. 创建自己的代理，可以与 Codex 互动以执行复杂的工程任务

### TypeScript 库
先说直白版：
TypeScript 库提供了一种在应用程序中控制 Codex 的方式，比非交互模式更全面和灵活。
在服务器端使用该库；它需要 Node.js 18 或更高版本。

把它理解成一个更严谨的过程：
1. TypeScript 库提供了一种在应用程序中控制 Codex 的方式，比非交互模式更全面和灵活。
2. 在服务器端使用该库；它需要 Node.js 18 或更高版本。

### 安装
先说直白版：
要开始使用，使用 `npm` 安装 Codex SDK：

把它理解成一个更严谨的过程：
1. 要开始使用，使用 `npm` 安装 Codex SDK：

### 使用
先说直白版：
与 Codex 开始一个线程，并使用你的提示运行它。
const codex = new Codex(); const thread = codex.startThread(); const result = await thread.run( "制定计划以诊断和修复 CI 故障" );
console.log(result); ```
再次调用 `run()` 以继续在同一线程上，或通过提供线程 ID 恢复以前的线程。

把它理解成一个更严谨的过程：
1. 与 Codex 开始一个线程，并使用你的提示运行它。
2. const codex = new Codex(); const thread = codex.startThread(); const result = await thread.run( "制定计划以诊断和修复 CI 故障" );
3. console.log(result); ```
4. 再次调用 `run()` 以继续在同一线程上，或通过提供线程 ID 恢复以前的线程。

### Python 库
先说直白版：
Python SDK 是实验性的，并通过 JSON-RPC 控制本地 Codex 应用服务器。它需要 Python 3.10 或更高版本和本地的开源 Codex 仓库的检查。

把它理解成一个更严谨的过程：
1. Python SDK 是实验性的，并通过 JSON-RPC 控制本地 Codex 应用服务器。它需要 Python 3.10 或更高版本和本地的开源 Codex 仓库的检查。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
