# 第36章 环境

> 原始页面：[Cloud environments – Codex web | OpenAI Developers](https://developers.openai.com/codex/cloud/environments)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用环境来控制 Codex 在云任务中安装和运行的内容。例如，您可以添加依赖项，安装像 linter 和格式化工具等工具，并设置环境变量。
- `Codex 云任务的运行方式`：提交任务时发生以下情况：
- `默认通用镜像`：Codex 代理在一个名为 `universal` 的默认容器镜像中运行，该镜像预装了常见的语言、包和工具。

## 正文整理
### 正文
使用环境来控制 Codex 在云任务中安装和运行的内容。例如，您可以添加依赖项，安装像 linter 和格式化工具等工具，并设置环境变量。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

继续往下看，这一节还强调了两件事：
- 在Cedex 设置中配置环境。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### Codex 云任务的运行方式
提交任务时发生以下情况：

继续往下看，这一节还强调了两件事：
- 1. Codex 创建一个容器并在选择的分支或提交 SHA 上检出您的 repo。 2. Codex 运行您的设置脚本，缓存容器恢复时还会运行可选的维护脚本。 3. Codex 应用您的互联网访问设置。设置脚本在有互联网访问的情况下运行。代理的互联网访问默认关闭，但您可以在需要时启用有限或不受限制的访问。请参见代理互联网访问。 4. 代理在循环中运行终端命令…（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

### 默认通用镜像
Codex 代理在一个名为 `universal` 的默认容器镜像中运行，该镜像预装了常见的语言、包和工具。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

继续往下看，这一节还强调了两件事：
- 在环境设置中，选择 **设置包版本** 以固定 Python、Node.js 和其他运行时的版本。
- 有关安装内容的详细信息，请参见 参考 Dockerfile 和可拉取和本地测试的镜像。
- 虽然 `codex-universal` 为速度和便利性预装了语言，但您也可以使用设置脚本向容器安装额外包。

### 环境变量和秘密
**环境变量** 在任务的整个持续时间内设置（包括设置脚本和代理阶段）。

继续往下看，这一节还强调了两件事：
- **秘密** 与环境变量类似，但：
- 它们以额外的加密层存储，仅在任务执行时被解密。
- 它们仅对设置脚本可用。出于安全原因，秘密在代理阶段开始前被移除。

### 自动设置
对于使用常见包管理器（`npm`、`yarn`、`pnpm`、`pip`、`pipenv` 和 `poetry`）的项目，Codex 可以自动安装依赖项和工具。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
