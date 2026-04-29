# 第61章 托管配置

> 原始页面：[Managed configuration – Codex | OpenAI Developers](https://developers.openai.com/codex/enterprise/managed-configuration)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 企业管理员可以通过两种方式控制本地 Codex 行为：
- `管理员强制要求 (requirements.toml)`：要求限制安全敏感设置（批准政策、批准审阅者、自动审阅政策、沙盒模式、Web 搜索模式、管理钩子，以及可选用户可以启用的 MCP 服务器）。在…
- `位置和优先级`：Codex 按以下顺序应用要求层（早期 wins 每个字段）：

## 正文整理
### 正文
企业管理员可以通过两种方式控制本地 Codex 行为：

继续往下看，这一节还强调了两件事：
- **要求**：管理员强制施加的限制，用户无法覆盖。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- **管理默认值**：Codex 启动时应用的初始值。用户仍可以在会话期间更改设置；Codex 在下次启动时重新应用管理默认值。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 管理员强制要求 (requirements.toml)
要求限制安全敏感设置（批准政策、批准审阅者、自动审阅政策、沙盒模式、Web 搜索模式、管理钩子，以及可选用户可以启用的 MCP 服务器）。在解析配置时（例如，从 `config.toml`、配置文件或 CLI 配置覆盖），如果值与强制规则冲突，Codex 将还原到兼容值并通知用户。如果你配置了 `mcp_servers` 允许列表，Codex 仅当其名称和身…（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 要求还可以通过 `requirements.toml` 中的 `[features]` 表限制 功能标志。请注意，功能不总是安全敏感，但企业可以根据需要固定值。省略的键将保持不受限制。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 关于确切的键列表，请参见 配置参考中的 `requirements.toml` 部分。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 位置和优先级
Codex 按以下顺序应用要求层（早期 wins 每个字段）：（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 1. 云管理要求（ChatGPT 商务版或企业版） 2. macOS 管理偏好（MDM）通过 `com.openai.codex:requirements_toml_base64` 3. 系统 `requirements.toml`（Unix 系统上的 `/etc/codex/requirements.toml`，包括 Linux/macOS，或 Windo…（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 在各层之间，Codex 按字段合并要求：如果较早的层设置了某字段（包括空列表），后来的层不会覆盖该字段，但较低的层仍可以填充未设置的字段。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 为了向后兼容，Codex 还解释遗留的 `managed_config.toml` 字段 `approval_policy` 和 `sandbox_mode` 作为要求（仅允许该单一值）。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 云管理要求
当您使用 ChatGPT 登录商务或企业计划时，Codex 还可以从 Codex 服务中获取管理员强制要求。这是另一个与 `requirements.toml` 兼容的要求来源。这适用于 Codex 的所有表面，包括 CLI、应用和 IDE 扩展。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 配置云管理要求
请访问 Codex 管理配置页面。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 使用与 `requirements.toml` 相同的格式和键创建一个新的管理要求文件。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- [rules] prefix_rules = [\ { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell …（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）
- 保存配置。保存后，更新的管理要求立即适用于匹配的用户。 有关更多示例，请参见 示例 requirements.toml。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
