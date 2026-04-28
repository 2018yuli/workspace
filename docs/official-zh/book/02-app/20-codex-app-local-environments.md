# 第20章 本地环境

> 原始页面：[Local environments – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/local-environments)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 本地环境让你为工作树配置设置步骤以及项目的常见操作。
- `设置脚本`：由于工作树在不同的目录中运行，你的项目可能没有完全设置，可能缺少未检查到你仓库中的依赖项或文件。设置脚本会在 Codex 在新线程开始时创建新工作树时自动运行。
- `操作`：使用操作定义常见任务，如启动应用的开发服务器或运行测试套件。这些操作出现在 Codex 应用顶栏中，以便快速访问。这些操作将在应用的 集成终端 中运行。

## 正文整理
### 正文
本地环境让你为工作树配置设置步骤以及项目的常见操作。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

继续往下看，这一节还强调了两件事：
- 你可以通过 Codex 应用设置 面板配置本地环境。你可以将生成的文件检查到你项目的 Git 仓库中，以便与他人共享。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）
- Codex 将此配置存储在你项目根目录的 `.codex` 文件夹中。如果你的仓库包含多个项目，请打开包含共享 `.codex` 文件夹的项目目录。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### 设置脚本
由于工作树在不同的目录中运行，你的项目可能没有完全设置，可能缺少未检查到你仓库中的依赖项或文件。设置脚本会在 Codex 在新线程开始时创建新工作树时自动运行。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 使用此脚本运行配置环境所需的任何命令，例如安装依赖项或运行构建过程。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）
- 例如，对于 TypeScript 项目，你可能希望使用设置脚本安装依赖项并进行初始构建：
- 如果你的设置是特定于平台的，请为 macOS、Windows 或 Linux 定义设置脚本以覆盖默认设置。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### 操作
使用操作定义常见任务，如启动应用的开发服务器或运行测试套件。这些操作出现在 Codex 应用顶栏中，以便快速访问。这些操作将在应用的 集成终端 中运行。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 操作有助于避免你输入诸如触发项目构建或启动开发服务器等常见操作。对于一次性的快速调试，你可以直接使用集成终端。
- 例如，对于 Node.js 项目，你可能创建一个包含以下脚本的“运行”操作：
- 如果操作的命令是特定于平台的，请为 macOS、Windows 和 Linux 定义特定的平台脚本。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
