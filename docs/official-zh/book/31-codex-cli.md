# 第31章 概述

> 原始页面：[CLI – Codex | OpenAI Developers](https://developers.openai.com/codex/cli)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 你读完应该抓住什么
- Codex CLI 是 OpenAI 的编码代理，您可以从终端本地运行。它可以读取、修改并在您选择的目录中运行代码。 它是 开源的，并使用 Ru。
- `CLI 设置`：选择您的包管理器
- `安装`：使用 npm 安装 Codex CLI。

## 分步理解
### 正文
先说直白版：
Codex CLI 是 OpenAI 的编码代理，您可以从终端本地运行。它可以读取、修改并在您选择的目录中运行代码。 它是 开源的，并使用 Rust 构建，以实现速度和效率。
ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
使用 OpenAI Codex CLI 与 GPT-5-Codex - YouTube
点击以取消静音

把它理解成一个更严谨的过程：
1. Codex CLI 是 OpenAI 的编码代理，您可以从终端本地运行。它可以读取、修改并在您选择的目录中运行代码。 它是 开源的，并使用 Rust 构建，以实现速度和效率。
2. ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
3. 使用 OpenAI Codex CLI 与 GPT-5-Codex - YouTube
4. 点击以取消静音

### CLI 设置
先说直白版：
选择您的包管理器
npmHomebrew
1. 1

把它理解成一个更严谨的过程：
1. 选择您的包管理器
2. npmHomebrew
3. 1. 1

### 安装
先说直白版：
使用 npm 安装 Codex CLI。
npm install 命令
npm i -g @openai/codex复制
2. 2

把它理解成一个更严谨的过程：
1. 使用 npm 安装 Codex CLI。
2. npm install 命令
3. npm i -g @openai/codex复制
4. 2. 2

### 运行
先说直白版：
在终端中运行 Codex。它可以检查您的代码库、编辑文件并运行命令。
运行 Codex 命令
codex复制
第一次运行 Codex 时，系统会提示您登录。可以使用您的 ChatGPT 帐户或 API 密钥进行身份验证。

把它理解成一个更严谨的过程：
1. 在终端中运行 Codex。它可以检查您的代码库、编辑文件并运行命令。
2. 运行 Codex 命令
3. codex复制
4. 第一次运行 Codex 时，系统会提示您登录。可以使用您的 ChatGPT 帐户或 API 密钥进行身份验证。

### 升级
先说直白版：
Codex CLI 的新版本会定期发布。请查看 更新日志 以获取发布说明。要使用 npm 升级，请运行：
npm upgrade 命令
npm i -g @openai/codex@latest复制
Codex CLI 可在 macOS、Windows 和 Linux 上使用。在 Windows 上，可以在 PowerShell 中原生运行 Codex，使用 Windows 沙盒，或在需要 Linux 原生环境时使用 WSL2。有关设置细节，请查看 Windows 设置指南。

把它理解成一个更严谨的过程：
1. Codex CLI 的新版本会定期发布。请查看 更新日志 以获取发布说明。要使用 npm 升级，请运行：
2. npm upgrade 命令
3. npm i -g @openai/codex@latest复制
4. Codex CLI 可在 macOS、Windows 和 Linux 上使用。在 Windows 上，可以在 PowerShell 中原生运行 Codex，使用 Windows 沙盒，或在需要 Linux 原生环境时使用 WSL2。有关设置细节，请查看 Windows 设置指南。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
