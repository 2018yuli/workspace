# 第08章 编年史

> 原始页面：[Chronicle – Codex | OpenAI Developers](https://developers.openai.com/codex/memories/chronicle)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。

## 严谨定义
严格地说，提示是对目标函数、约束条件和验证标准的联合描述。

## 本章先抓重点
- Chronicle 处于 **选择加入的研究预览** 中。仅对 macOS 的 ChatGPT Pro 订阅者可用，尚未在欧盟、英国和瑞士提供。请查看 隐私与安全 部分以获取详细信息，并在启用前了解当…
- `Chronicle 如何帮助`：我们设计 Chronicle 以减少您在与 Codex 工作时需要重复陈述的上下文量。通过使用最近的屏幕上下文来改善记忆构建，Chronicle 可以帮助 Codex…
- `使用屏幕上的内容`：通过 Chronicle，Codex 可以理解您当前正在查看的内容，为您节省时间和上下文切换。

## 正文整理
### 正文
Chronicle 处于 **选择加入的研究预览** 中。仅对 macOS 的 ChatGPT Pro 订阅者可用，尚未在欧盟、英国和瑞士提供。请查看 隐私与安全 部分以获取详细信息，并在启用前了解当前的风险。

继续往下看，这一节还强调了两件事：
- Chronicle 增强了 Codex 记忆，通过您的屏幕提供上下文。当您提示 Codex 时，这些记忆可以帮助它理解您正在处理的内容，减少您需要重复说明上下文的必要。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- Chronicle 作为 Codex 应用程序中选择加入的研究预览在 macOS 上可用。它需要 macOS 的屏幕录制和辅助功能权限。启用之前，请注意 Chronicle 会快速消耗速率限制，增加提示注入的风险，并以未加密的方式在您的设备上存储记忆。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### Chronicle 如何帮助
我们设计 Chronicle 以减少您在与 Codex 工作时需要重复陈述的上下文量。通过使用最近的屏幕上下文来改善记忆构建，Chronicle 可以帮助 Codex 理解您所指的内容，识别合适的资源并了解您依赖的工具和工作流程。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 使用屏幕上的内容
通过 Chronicle，Codex 可以理解您当前正在查看的内容，为您节省时间和上下文切换。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 有 Chronicle 的时候
- 没有 Chronicle 的时候
- 为什么这会失败？

### 填补缺失的上下文
无需仔细构建您的上下文并从零开始。Chronicle 让 Codex 填补您上下文中的空缺。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 有 Chronicle 的时候
- 没有 Chronicle 的时候
- 同步最新文档草稿更改并在完成后给 Romain 留言

### 记住工具和工作流程
无需向 Codex 解释要使用哪些工具来执行您的工作。Codex 在您工作时学习，以节省您长远的时间。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

继续往下看，这一节还强调了两件事：
- 有 Chronicle 的时候
- 没有 Chronicle 的时候
- 创建新的启动通讯以便在内部共享

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
