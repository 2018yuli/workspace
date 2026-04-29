# 第27章 功能

> 原始页面：[Features – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/features)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- Codex IDE 扩展使你可以直接在 VS Code、Cursor、Windsurf 和其他兼容 VS Code 的编辑器中访问 Codex。它使用与 Codex CLI 相同的代理，并共享相同的配…
- `提示 Codex`：在你的编辑器中使用 Codex 进行聊天、编辑和无缝预览更改。当 Codex 从打开的文件和选定的代码中获得上下文时，你可以编写更短的提示并获得更快、更相关的结果。
- `在模型之间切换`：你可以使用聊天输入下方的切换器切换模型。

## 正文整理
### 正文
Codex IDE 扩展使你可以直接在 VS Code、Cursor、Windsurf 和其他兼容 VS Code 的编辑器中访问 Codex。它使用与 Codex CLI 相同的代理，并共享相同的配置。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 提示 Codex
在你的编辑器中使用 Codex 进行聊天、编辑和无缝预览更改。当 Codex 从打开的文件和选定的代码中获得上下文时，你可以编写更短的提示并获得更快、更相关的结果。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 你可以通过在提示中标记文件来引用编辑器中的任何文件，如下所示：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）

### 在模型之间切换
你可以使用聊天输入下方的切换器切换模型。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

### 调整推理努力
你可以调整推理努力，以控制 Codex 在响应之前思考的时间。更高的努力可以帮助完成复杂任务，但响应时间更长。更高的努力也会使用更多的令牌，并可能更快消耗你的速率限制，尤其是使用更高能力的模型时。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

继续往下看，这一节还强调了两件事：
- 使用上面显示的相同模型切换器，为每个模型选择 `low`、`medium` 或 `high`。从 `medium` 开始，仅在需要更深入时切换到 `high`。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

### 选择批准模式
默认情况下，Codex 在 `Agent` 模式下运行。在此模式下，Codex 可以自动读取文件、进行编辑并在工作目录中运行命令。Codex 仍然需要你的批准，才能在工作目录外工作或访问网络。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 当你只想聊天，或者希望在做更改之前进行规划时，可以使用聊天输入下方的切换器切换到 `Chat`。
- 如果你需要 Codex 读取文件、进行编辑并在没有批准的情况下运行访问网络的命令，请使用 `Agent (Full Access)`。在这样做之前请谨慎。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
