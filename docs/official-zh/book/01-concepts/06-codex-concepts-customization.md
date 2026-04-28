# 第06章 自定义

> 原始页面：[Customization – Codex | OpenAI Developers](https://developers.openai.com/codex/concepts/customization)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 本章先抓重点
- 定制化是指如何让 Codex 按照你的团队的工作方式运行。
- `AGENTS 指导`：`AGENTS.md` 为 Codex 提供持久的项目指导，这些指导与您的代码库一起移动并在代理开始工作之前应用。保持简短。
- `何时更新 `AGENTS.md``：- **重复错误**：如果代理反复犯同样的错误，请添加一条规则。

## 正文整理
### 正文
定制化是指如何让 Codex 按照你的团队的工作方式运行。

继续往下看，这一节还强调了两件事：
- 在 Codex 中，定制化来自几个相互协作的层次：
- **项目指导（`AGENTS.md`）** 用于持久性指令（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）
- **记忆** 用于从过去工作中学习的有用上下文（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

### AGENTS 指导
`AGENTS.md` 为 Codex 提供持久的项目指导，这些指导与您的代码库一起移动并在代理开始工作之前应用。保持简短。（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 将其用于您希望 Codex 每次在代码库中遵循的规则，例如：
- 构建和测试命令
- 评审期望

### 何时更新 `AGENTS.md`
**重复错误**：如果代理反复犯同样的错误，请添加一条规则。

继续往下看，这一节还强调了两件事：
- **阅读过多**：如果它找到正确的文件但阅读了太多文档，请添加路由指导（优先考虑哪些目录/文件）。
- **重复的 PR 反馈**：如果您多次留下相同的反馈，请将其编纂。
- **在 GitHub 中**：在拉取请求评论中，标记 `@codex` 并请求（例如，`@codex add this to AGENTS.md`）将更新委派到云任务。（实现：[Codex](/config/workspace/codex/codex-rs/core/src/codex.rs:285)、[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager::fork_thread](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375)、[agent/control](/config/workspace/codex/codex-rs/core/src/agent/control.rs:1)）

### 技能
技能为 Codex 提供可重用的能力以实现可重复的工作流程。技能通常是可重用工作流程的最佳选择，因为它们支持更丰富的指令、脚本和引用，同时保持跨任务的可重用性。技能被加载并对代理可见（至少它们的元数据），因此 Codex 可以隐式发现和选择它们。这使得丰富的工作流程可用，而不会提前膨胀上下文。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 使用技能文件夹在本地撰写和迭代工作流程。如果该工作流程已经存在插件，则先安装它以重用经过验证的设置。当您希望跨团队分发自己的工作流程或将其与应用程序集成捆绑时，将其打包为 插件。技能仍然是创作格式；插件是可安装的分发单元。（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）
- 技能通常是一个 `SKILL.md` 文件以及可选的脚本、引用和资产。（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）
- my-skill/（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）

### MCP
MCP（模型上下文协议）是将 Codex 连接到外部工具和上下文提供者的标准方法。它对于远程托管的系统尤为有用，例如 Figma、Linear、GitHub 或您的团队所依赖的内部知识服务。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 当 Codex 需要本地代码库之外的功能时（例如问题跟踪器、设计工具、浏览器或共享文档系统），请使用 MCP。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- 可以这样思考：
- **主机**：Codex

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
