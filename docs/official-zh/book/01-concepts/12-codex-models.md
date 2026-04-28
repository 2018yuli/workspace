# 第12章 模型

> 原始页面：[Models – Codex | OpenAI Developers](https://developers.openai.com/codex/models)

这一章讲如何选择模型与推理强度，本质上是在做效果、速度和成本之间的平衡。

它不是只给你型号清单，而是在解释不同任务为什么要用不同求解器。

## 数学类比
模型选择像选解题工具：心算快但不适合难题，复杂题可能要用更强的公式和更长的推导。

## 严谨定义
严格地说，模型是具有特定上下文窗口、推理能力和工具调用风格的求解器。

## 本章先抓重点
- `推荐模型`：gpt-5.5
- `替代模型`：gpt-5.2
- `其他模型`：当你通过 ChatGPT 登录时，Codex 最适合使用上述模型。

## 正文整理
### 推荐模型
gpt-5.5

继续往下看，这一节还强调了两件事：
- OpenAI 最新的前沿模型，用于复杂编码、计算机使用、知识工作和 Codex 中的研究工作流。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）
- codex -m gpt-5.5
- 复制命令

### 替代模型
gpt-5.2

继续往下看，这一节还强调了两件事：
- 之前的通用模型，适用于编码和代理任务，包括需深入思考的困难调试任务。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）
- codex -m gpt-5.2
- 复制命令

### 其他模型
当你通过 ChatGPT 登录时，Codex 最适合使用上述模型。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）

继续往下看，这一节还强调了两件事：
- 你还可以将 Codex 指向任何支持 聊天完成 或 响应 API 的模型和提供者，以适应你的特定用例。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）
- 聊天完成 API 的支持已被弃用，将在 Codex 的未来版本中删除。

### 配置你的默认本地模型
Codex CLI 和 IDE 扩展使用相同的 `config.toml` 配置文件。要指定模型，请在配置文件中添加 `model` 条目。如果你不指定模型，Codex 应用、CLI 或 IDE 扩展将默认使用推荐模型。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）

继续往下看，这一节还强调了两件事：
- 如果 `gpt-5.5` 尚未在你的账户中可用，请使用 `gpt-5.4`。

### 临时选择不同的本地模型
在 Codex CLI 中，你可以在活动线程中使用 `/model` 命令更改模型。在 IDE 扩展中，你可以使用输入框下方的模型选择器选择模型。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 要以特定模型启动新的 Codex CLI 线程或为 `codex exec` 指定模型，你可以使用 `--model`/`-m` 标志：（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
