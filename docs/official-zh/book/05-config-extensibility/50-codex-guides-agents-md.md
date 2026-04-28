# 第50章 AGENTS.md

> 原始页面：[Custom instructions with AGENTS.md – Codex | OpenAI Developers](https://developers.openai.com/codex/guides/agents-md)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。

## 严谨定义
严格地说，提示是对目标函数、约束条件和验证标准的联合描述。

## 本章先抓重点
- Codex 在执行任何工作之前会读取 `AGENTS.md` 文件。通过将全局指导与特定项目的覆盖层叠，您可以从每个任务开始时保持一致的期望，无论您打开哪个代码库。
- `Codex 如何发现指导`：Codex 在启动时（每次运行一次；在 TUI 中，这通常意味着每次启动会话时）构建一个指令链。发现遵循以下优先顺序：
- `创建全局指导`：在您的 Codex 主目录中创建持久性默认值，以便每个代码库都可以继承您的工作协议。

## 正文整理
### 正文
Codex 在执行任何工作之前会读取 `AGENTS.md` 文件。通过将全局指导与特定项目的覆盖层叠，您可以从每个任务开始时保持一致的期望，无论您打开哪个代码库。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### Codex 如何发现指导
Codex 在启动时（每次运行一次；在 TUI 中，这通常意味着每次启动会话时）构建一个指令链。发现遵循以下优先顺序：（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 1. **全局范围：** 在您的 Codex 主目录中（默认是 `~/.codex`，除非您设置了 `CODEX_HOME`），Codex 会读取 `AGENTS.override.md`（如果存在）。否则，Codex 会读取 `AGENTS.md`。Codex 只使用该层级中的第一个非空文件。 2. **项目范围：** 从项目根目录开始（通常是 Git 根…（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）
- Codex 会跳过空文件，并且在合并大小达到 `project_doc_max_bytes` 定义的限制后停止添加文件（默认为 32 KiB）。有关这些设置的详细信息，请参见 项目指令发现。当您达到上限时，请提高限制或在嵌套目录中分割指令。

### 创建全局指导
在您的 Codex 主目录中创建持久性默认值，以便每个代码库都可以继承您的工作协议。

继续往下看，这一节还强调了两件事：
- 1. 确保目录存在：
- 2. 创建 `~/.codex/AGENTS.md` 并使用可重用的偏好设置：（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）

### 工作协议
修改 JavaScript 文件后始终运行 `npm test`。

继续往下看，这一节还强调了两件事：
- 安装依赖时首选使用 `pnpm`。
- 添加新的生产依赖前需征求确认。
- 3. 在任何地方运行 Codex 来确认它加载了该文件：

### 层叠项目指令
存储库级文件保持 Codex 了解项目规范，同时仍然继承您的全局默认值。

继续往下看，这一节还强调了两件事：
- 1. 在您的存储库根目录中，添加一个涵盖基本设置的 `AGENTS.md`：（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
