# 第26章 概述

> 原始页面：[IDE extension – Codex | OpenAI Developers](https://developers.openai.com/codex/ide)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 你读完应该抓住什么
- Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它帮助您更快地构建，消除错误，并理解不熟悉的代码。通过 Codex VS C。
- `扩展设置`：Codex IDE 扩展与 VS Code 分支（如 Cursor 和 Windsurf）兼容。
- `JetBrains IDE 集成`：如果您希望在 JetBrains IDE（例如 Rider、IntelliJ、PyCharm 或 WebS。

## 分步理解
### 正文
先说直白版：
Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它帮助您更快地构建，消除错误，并理解不熟悉的代码。通过 Codex VS Code 扩展，您可以在 IDE 中并行使用 Codex 或将任务委派给 Codex Cloud。
ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
OpenAI Codex 在您的代码编辑器中 - YouTube
点击取消静音

把它理解成一个更严谨的过程：
1. Codex 是 OpenAI 的编码代理，可以读取、编辑和运行代码。它帮助您更快地构建，消除错误，并理解不熟悉的代码。通过 Codex VS Code 扩展，您可以在 IDE 中并行使用 Codex 或将任务委派给 Codex Cloud。
2. ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
3. OpenAI Codex 在您的代码编辑器中 - YouTube
4. 点击取消静音

### 扩展设置
先说直白版：
Codex IDE 扩展与 VS Code 分支（如 Cursor 和 Windsurf）兼容。
您可以从 Visual Studio Code 市场 获取 Codex 扩展，或下载适用于您的 IDE：
- 下载 Visual Studio Code 版
- 下载 Cursor 版

把它理解成一个更严谨的过程：
1. Codex IDE 扩展与 VS Code 分支（如 Cursor 和 Windsurf）兼容。
2. 您可以从 Visual Studio Code 市场 获取 Codex 扩展，或下载适用于您的 IDE：
3. 下载 Visual Studio Code 版
4. 下载 Cursor 版

### JetBrains IDE 集成
先说直白版：
如果您希望在 JetBrains IDE（例如 Rider、IntelliJ、PyCharm 或 WebStorm）中使用 Codex，请安装 JetBrains IDE 集成。它支持使用 ChatGPT、API 密钥或 JetBrains AI 订阅进行登录。

把它理解成一个更严谨的过程：
1. 如果您希望在 JetBrains IDE（例如 Rider、IntelliJ、PyCharm 或 WebStorm）中使用 Codex，请安装 JetBrains IDE 集成。它支持使用 ChatGPT、API 密钥或 JetBrains AI 订阅进行登录。

### 将 Codex 移动到右侧边栏
先说直白版：
在 VS Code 中，Codex 会自动出现在右侧边栏。如果您希望它在主（左）边栏中，请将 Codex 图标拖回左侧活动栏。
在 Cursor 等 VS Code 分支中，您可能需要手动将 Codex 移动到右侧边栏。为此，您可能需要首先暂时更改活动栏方向：
1. 打开您的编辑器设置，搜索 `activity bar`（在工作台设置中）。 2. 将方向更改为 `vertical`。 3. 重启您的编辑器。
现在将 Codex 图标拖到右侧边栏（例如，紧挨着您的 Cursor 聊天）。Codex 显示为侧边栏中的另一个选项卡。

把它理解成一个更严谨的过程：
1. 在 VS Code 中，Codex 会自动出现在右侧边栏。如果您希望它在主（左）边栏中，请将 Codex 图标拖回左侧活动栏。
2. 在 Cursor 等 VS Code 分支中，您可能需要手动将 Codex 移动到右侧边栏。为此，您可能需要首先暂时更改活动栏方向：
3. 1. 打开您的编辑器设置，搜索 `activity bar`（在工作台设置中）。 2. 将方向更改为 `vertical`。 3. 重启您的编辑器。
4. 现在将 Codex 图标拖到右侧边栏（例如，紧挨着您的 Cursor 聊天）。Codex 显示为侧边栏中的另一个选项卡。

### 登录
先说直白版：
安装扩展后，它会提示您使用 ChatGPT 帐户或 API 密钥登录。您的 ChatGPT 计划包括使用额度，因此您可以无需额外设置就使用 Codex。有关更多信息，请访问 定价页面。

把它理解成一个更严谨的过程：
1. 安装扩展后，它会提示您使用 ChatGPT 帐户或 API 密钥登录。您的 ChatGPT 计划包括使用额度，因此您可以无需额外设置就使用 Codex。有关更多信息，请访问 定价页面。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
