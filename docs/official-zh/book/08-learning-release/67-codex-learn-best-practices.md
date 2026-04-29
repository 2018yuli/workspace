# 第67章 最佳实践

> 原始页面：[Best practices – Codex | OpenAI Developers](https://developers.openai.com/codex/learn/best-practices)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 如果您是 Codex 或编码代理的新手，本指南将帮助您更快获得更好的结果。它涵盖了使 Codex 更有效的核心习惯，适用于 CLI、IDE 扩展 和 Codex 应用，从提示、规划到验证、MCP、技能…
- `强大的首次使用：上下文和提示`：即使您的提示不完美，Codex 已经足够强大，能够提供有用的结果。您通常可以在进行最少设置的情况下，将一个难题提交给它，并依然获得强结果。清晰的 提示 并不是获取价值…
- `对于困难任务先规划`：如果任务复杂、模糊或难以良好描述，请在 Codex 开始编码之前请求它进行规划。

## 正文整理
### 正文
如果您是 Codex 或编码代理的新手，本指南将帮助您更快获得更好的结果。它涵盖了使 Codex 更有效的核心习惯，适用于 CLI、IDE 扩展 和 Codex 应用，从提示、规划到验证、MCP、技能和自动化。（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）

继续往下看，这一节还强调了两件事：
- 当您将 Codex 视为一个可配置和逐步改进的团队成员时，它的效果最佳。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 一种有用的思路是：从合适的任务上下文开始，使用 `AGENTS.md` 提供持久的指导，配置 Codex 以匹配您的工作流程，通过 MCP 连接外部系统，将重复工作转变为技能，并自动化稳定的工作流程。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 强大的首次使用：上下文和提示
即使您的提示不完美，Codex 已经足够强大，能够提供有用的结果。您通常可以在进行最少设置的情况下，将一个难题提交给它，并依然获得强结果。清晰的 提示 并不是获取价值所必需的，但它确实使结果更可靠，尤其是在更大的代码库或更高风险的任务中。（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）

继续往下看，这一节还强调了两件事：
- 如果您在一个大型或复杂的代码库中工作，最大解锁是在为 Codex 提供正确的任务上下文和所需完成内容的清晰结构。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 一个好的默认做法是在您的提示中包含四个内容：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）
- **目标：** 您想要更改或构建什么？

### 对于困难任务先规划
如果任务复杂、模糊或难以良好描述，请在 Codex 开始编码之前请求它进行规划。

继续往下看，这一节还强调了两件事：
- 以下几种方法效果良好：
- **使用计划模式：** 对于大多数用户，这是最简单、最有效的选择。计划模式让 Codex 收集上下文、提问澄清问题，并在实施之前制定更强的计划。通过 `/plan` 或 `Shift` + `Tab` 切换。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- **请求 Codex 采访您：** 如果您对自己想要的内容有大概想法，但不确定如何恰当地描述，可以先让 Codex 问您。告诉它挑战您的假设，并将模糊的想法转变为具体内容，然后再编写代码。

### 通过 `AGENTS.md` 使指导可重用
一旦提示模式有效，下一步是停止手动重复它。这就是 AGENTS.md 的作用。（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）

继续往下看，这一节还强调了两件事：
- 将 `AGENTS.md` 视为代理的开放格式 README。它会自动加载到上下文中，是编码您和您的团队希望 Codex 在代码库中工作方式的最佳地方。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 一个好的 `AGENTS.md` 包含：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）
- 回购布局和重要目录

### 为一致性配置 Codex
配置是使 Codex 在会话和表面之间行为更一致的主要方式之一。例如，您可以设置模型选择、推理工作量、沙盒模式、批准政策、配置文件和 MCP 设置的默认值。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 一个好的起始模式是：
- 将个人默认设置保存在 `~/.codex/config.toml` 中（设置 → 配置 → 从 Codex 应用中打开 config.toml）（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 在 `.codex/config.toml` 中保留回购特定行为（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
