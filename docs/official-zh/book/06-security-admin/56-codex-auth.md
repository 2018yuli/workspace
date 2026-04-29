# 第56章 身份验证

> 原始页面：[Authentication – Codex | OpenAI Developers](https://developers.openai.com/codex/auth)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `OpenAI 身份验证`：Codex 支持在使用 OpenAI 模型时，通过两种方式登录：
- `使用 ChatGPT 登录`：当您从 Codex 应用、CLI 或 IDE 扩展使用 ChatGPT 登录时，Codex 会为您打开一个浏览器窗口以完成登录流程。登录后，浏览器会将访问令牌返回给 C…
- `使用 API 密钥登录`：您还可以使用 API 密钥登录 Codex 应用、CLI 或 IDE 扩展。请从 OpenAI 仪表板 获取您的 API 密钥。

## 正文整理
### OpenAI 身份验证
Codex 支持在使用 OpenAI 模型时，通过两种方式登录：（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

继续往下看，这一节还强调了两件事：
- 使用 ChatGPT 登录以获得订阅访问权限（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- 使用 API 密钥登录以获得基于使用量的访问权限（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- Codex 云要求使用 ChatGPT 登录。Codex CLI 和 IDE 扩展支持两种登录方式。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 使用 ChatGPT 登录
当您从 Codex 应用、CLI 或 IDE 扩展使用 ChatGPT 登录时，Codex 会为您打开一个浏览器窗口以完成登录流程。登录后，浏览器会将访问令牌返回给 CLI 或 IDE 扩展。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 使用 API 密钥登录
您还可以使用 API 密钥登录 Codex 应用、CLI 或 IDE 扩展。请从 OpenAI 仪表板 获取您的 API 密钥。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- OpenAI 会通过您的 OpenAI 平台账户按标准 API 费率对 API 密钥的使用进行计费。请查看 API 定价页面。
- 依赖于 ChatGPT 余额的功能，例如 快速模式，仅在使用 ChatGPT 登录时可用。如果您使用 API 密钥登录，Codex 将使用标准 API 定价。（实现：[auth](/codex/codex-rs/core/src/auth.rs#L1)、[auth/storage](/codex/codex-rs/core/src/auth/storage.rs#L1)、[login crate](/codex/codex-rs/login/src/lib.rs#L1)、[cloud-tasks auth helper](/codex/codex-rs/cloud-tasks/src/util.rs#L62)）
- 推荐在程序化的 Codex CLI 工作流中使用 API 密钥身份验证（例如 CI/CD 作业）。请勿在不受信任或公共环境中暴露 Codex 执行。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 保护您的 Codex 云账户
Codex 云直接与您的代码库交互，因此需要比许多其他 ChatGPT 功能更强的安全性。启用多因素身份验证 (MFA)。

继续往下看，这一节还强调了两件事：
- 如果您使用社交登录提供商（谷歌、微软、苹果），则不需要在您的 ChatGPT 账户中启用 MFA，但您可以与您的社交登录提供商一起设置。（实现：[auth](/codex/codex-rs/core/src/auth.rs#L1)、[auth/storage](/codex/codex-rs/core/src/auth/storage.rs#L1)、[login crate](/codex/codex-rs/login/src/lib.rs#L1)、[cloud-tasks auth helper](/codex/codex-rs/cloud-tasks/src/util.rs#L62)）
- 有关设置说明，请参见：
- 谷歌

### 登录缓存
当您使用 ChatGPT 或 API 密钥登录 Codex 应用、CLI 或 IDE 扩展时，Codex 会缓存您的登录详情，并在您下次启动 CLI 或扩展时重用它们。CLI 和扩展共享相同的缓存登录详情。如果您从其中一个注销，则下次启动 CLI 或扩展时需要重新登录。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- Codex 在 `~/.codex/auth.json` 的明文文件中或在您操作系统特定的凭证存储中本地缓存登录详情。（实现：[auth](/codex/codex-rs/core/src/auth.rs#L1)、[auth/storage](/codex/codex-rs/core/src/auth/storage.rs#L1)、[login crate](/codex/codex-rs/login/src/lib.rs#L1)、[cloud-tasks auth helper](/codex/codex-rs/cloud-tasks/src/util.rs#L62)）
- 对于使用 ChatGPT 会话的登录，Codex 会在使用期间在令牌过期前自动刷新令牌，因此活跃会话通常会持续进行，而无需再次浏览器登录。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
