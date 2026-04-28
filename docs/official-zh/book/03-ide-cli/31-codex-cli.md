# 第31章 概述

> 原始页面：[CLI – Codex | OpenAI Developers](https://developers.openai.com/codex/cli)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- Codex CLI 是 OpenAI 的编码代理，您可以从终端本地运行。它可以读取、修改并在您选择的目录中运行代码。 它是 开源的，并使用 Rust 构建，以实现速度和效率。
- `CLI 设置`：选择您的包管理器
- `安装`：使用 npm 安装 Codex CLI。

## 正文整理
### 正文
Codex CLI 是 OpenAI 的编码代理，您可以从终端本地运行。它可以读取、修改并在您选择的目录中运行代码。 它是 开源的，并使用 Rust 构建，以实现速度和效率。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包括 Codex。了解更多关于 包含的内容。
- 使用 OpenAI Codex CLI 与 GPT-5-Codex - YouTube（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- 点击以取消静音

### CLI 设置
选择您的包管理器

继续往下看，这一节还强调了两件事：
- npmHomebrew
- 1. 1

### 安装
使用 npm 安装 Codex CLI。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- npm install 命令
- npm i -g @openai/codex复制
- 2. 2

### 运行
在终端中运行 Codex。它可以检查您的代码库、编辑文件并运行命令。

继续往下看，这一节还强调了两件事：
- 运行 Codex 命令
- codex复制
- 第一次运行 Codex 时，系统会提示您登录。可以使用您的 ChatGPT 帐户或 API 密钥进行身份验证。（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)、[auth](/config/workspace/codex/codex-rs/core/src/auth.rs:1)）

### 升级
Codex CLI 的新版本会定期发布。请查看 更新日志 以获取发布说明。要使用 npm 升级，请运行：（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- npm upgrade 命令
- npm i -g @openai/codex@latest复制
- Codex CLI 可在 macOS、Windows 和 Linux 上使用。在 Windows 上，可以在 PowerShell 中原生运行 Codex，使用 Windows 沙盒，或在需要 Linux 原生环境时使用 WSL2。有关设置细节，请查看 Windows 设置指南。（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
