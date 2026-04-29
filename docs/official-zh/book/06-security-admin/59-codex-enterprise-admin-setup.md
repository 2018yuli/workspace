# 第59章 管理员设置

> 原始页面：[Admin Setup – Codex | OpenAI Developers](https://developers.openai.com/codex/enterprise/admin-setup)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 本指南适用于希望为其工作区设置 Codex 的 ChatGPT 企业管理员。
- `企业级安全和隐私`：Codex 支持 ChatGPT 企业安全功能，包括：
- `先决条件：确定负责人和推出策略`：在推出过程中，团队成员可能会支持将 Codex 集成到您的组织的不同方面。确保您有以下负责人：

## 正文整理
### 正文
本指南适用于希望为其工作区设置 Codex 的 ChatGPT 企业管理员。

继续往下看，这一节还强调了两件事：
- 请将此页面用作逐步推出指南。如需详细的政策、配置和监控信息，请使用链接页面：身份验证、代理批准与安全、托管配置和治理。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 企业级安全和隐私
Codex 支持 ChatGPT 企业安全功能，包括：

继续往下看，这一节还强调了两件事：
- 不对企业数据进行训练
- 应用、CLI 和 IDE 的零数据保留（代码保留在开发者环境中）（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 遵循 ChatGPT 企业政策的居住和保留

### 先决条件：确定负责人和推出策略
在推出过程中，团队成员可能会支持将 Codex 集成到您的组织的不同方面。确保您有以下负责人：

继续往下看，这一节还强调了两件事：
- **ChatGPT 企业工作区所有者：** 必须配置工作区中的 Codex 设置。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- **安全负责人：** 确定 Codex 的代理权限设置。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- **分析负责人：** 将分析和合规 API 集成到您的数据管道中。

### 第一步：在工作区中启用 Codex
您可以在 ChatGPT 企业工作区设置中配置对 Codex 的访问。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 转到 工作区设置 > 设置和权限。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### Codex 本地
Codex 本地在新的 ChatGPT 企业工作区中默认启用。如果您不是 ChatGPT 工作区的所有者，您可以通过安装 Codex并使用您的工作电子邮件登录来测试您是否有访问权限。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 开启 **允许成员使用 Codex Local**。
- 这允许允许的用户使用 Codex 应用、CLI 和 IDE 扩展。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 如果此切换关闭，尝试使用 Codex 应用、CLI 或 IDE 的用户将看到以下错误：“403 - 未授权。请联系您的 ChatGPT 管理员以获取访问权限。”（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
