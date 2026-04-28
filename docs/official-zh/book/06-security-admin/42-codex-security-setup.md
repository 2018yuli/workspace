# 第42章 设置

> 原始页面：[Setup – Codex Security | OpenAI Developers](https://developers.openai.com/codex/security/setup)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 本页面指导您从初始访问到审查发现和 Codex 安全中的修复请求。
- `1\. 访问和环境`：Codex 安全扫描通过 Codex Cloud 连接的 GitHub 仓库。
- `2\. 新的安全扫描`：环境存在后，访问 创建安全扫描 并选择您刚刚连接的仓库。

## 正文整理
### 正文
本页面指导您从初始访问到审查发现和 Codex 安全中的修复请求。

继续往下看，这一节还强调了两件事：
- 首先确认您已设置 Codex Cloud。如果没有，请参阅 Codex\\ Cloud 开始。

### 1\. 访问和环境
Codex 安全扫描通过 Codex Cloud 连接的 GitHub 仓库。（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）

继续往下看，这一节还强调了两件事：
- 确认您的工作区可以访问 Codex 安全。
- 确认您要扫描的仓库在 Codex Cloud 中可用。
- 访问 Codex 环境 并检查仓库是否已有环境。如果没有，请在继续之前创建一个。

### 2\. 新的安全扫描
环境存在后，访问 创建安全扫描 并选择您刚刚连接的仓库。

继续往下看，这一节还强调了两件事：
- Codex 安全首先从最新提交向后扫描仓库。它利用这些信息在新的提交到达时构建和刷新扫描上下文。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- 要配置一个仓库：（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）
- 1. 选择 GitHub 组织。 2. 选择仓库。 3. 选择您要扫描的分支。 4. 选择环境。 5. 选择一个 **历史时间窗口**。较长的窗口提供更多上下文，但回填所需时间较长。 6. 点击 **创建**。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

### 3\. 初始扫描可能需要一些时间
当您创建扫描时，Codex 安全首先在所选的历史时间窗口内进行提交级别的安全检查。 初始回填可能需要几个小时，尤其是对于较大的仓库或较长的时间窗口。 如果发现内容没有立即显示，这是正常现象。在打开工单或故障排除之前，请等待初始扫描完成。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 初始扫描设置自动且全面。这可能需要几个小时。如果第一次发现的结果延迟出现，请不要惊慌。

### 4\. 审查扫描并改善威胁模型
当初始扫描结束后，打开扫描并审查生成的威胁模型。 在初始发现出现后，更新威胁模型以匹配您的架构、信任边界和业务上下文。 这有助于 Codex 安全为您的团队排名问题。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- 如果您希望扫描结果发生变化，您可以使用更新后的范围、优先事项和假设编辑威胁模型。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）
- 在初始发现出现后，重新查看模型，以确保扫描指导与当前优先事项保持一致。 保持最新有助于 Codex 安全提出更好的建议。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）
- 有关威胁模型及其如何影响重要性和分类的更深层次解释，请参阅 改进威胁模型。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
