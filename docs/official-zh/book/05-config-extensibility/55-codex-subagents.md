# 第55章 子代理

> 原始页面：[Subagents – Codex | OpenAI Developers](https://developers.openai.com/codex/subagents)

这一章讲子代理，也就是把一个大任务拆给多个代理分别处理，再把结果汇总回来。

如果你已经能理解“主线程”和“上下文”这两个词，这一章就会非常自然。

## 数学类比
线程像解一道多步函数题时保留下来的草稿纸。后一步是否顺利，依赖前面保留下来的中间结果。

## 严谨定义
严格地说，线程是一个按时间顺序累积状态的信息序列。

## 本章先抓重点
- Codex 可以通过并行生成专业代理来运行子代理工作流，然后将它们的结果整合为一个响应。这在处理复杂且高度并行的任务时尤其有用，例如代码库探索或实现多步骤特性计划。
- `可用性`：当前 Codex 版本默认启用子代理工作流。
- `典型工作流`：Codex 处理代理间的编排，包括生成新的子代理、路由后续指令、等待结果以及关闭代理线程。

## 正文整理
### 正文
Codex 可以通过并行生成专业代理来运行子代理工作流，然后将它们的结果整合为一个响应。这在处理复杂且高度并行的任务时尤其有用，例如代码库探索或实现多步骤特性计划。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 通过子代理工作流，您还可以根据任务定义自己的自定义代理，具有不同的模型配置和指令。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）
- 有关子代理工作流背后的概念和权衡，包括上下文污染、上下文衰退和模型选择指导，请参见 子代理概念。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

### 可用性
当前 Codex 版本默认启用子代理工作流。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 子代理活动目前在 Codex 应用和 CLI 中显示。IDE 扩展的可见性即将推出。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）
- Codex 仅在您明确要求时才生成子代理。由于每个子代理都进行自己的模型和工具工作，子代理工作流消耗的令牌比可比的单代理运行更多。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

### 典型工作流
Codex 处理代理间的编排，包括生成新的子代理、路由后续指令、等待结果以及关闭代理线程。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 当许多代理正在运行时，Codex 会等待所有请求的结果可用，然后返回一个合并的响应。
- Codex 仅在您明确要求时才生成新的代理。
- 要查看其实际运作，请在您的项目中尝试以下提示：（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）

### 管理子代理
在 CLI 中使用 `/agent` 在活动代理线程之间切换并检查正在进行的线程。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 直接询问 Codex 以引导正在运行的子代理、停止它，或关闭已完成的代理线程。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

### 审批和沙盒控制
子代理继承您当前的沙盒策略。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

继续往下看，这一节还强调了两件事：
- 在交互式 CLI 会话中，即使您正在查看主线程，来自非活跃代理线程的审批请求也可以浮出水面。审批覆盖显示源线程标签，您可以按 `o` 打开该线程，然后再批准、拒绝或回答请求。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）
- 在非交互流程中，或者每当运行无法浮出新的审批时，需要新审批的操作将失败，并且 Codex 会将错误信息返回给父工作流。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- Codex 还会在生成子代理时重新应用父级轮次的实时运行时覆盖。这包括您在会话期间交互设置的沙盒和审批选择，例如 `/approvals` 变更或 `--yolo`，即使所选自定义代理文件设置了不同的默认值。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
