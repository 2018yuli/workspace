# 第45章 配置参考

> 原始页面：[Configuration Reference – Codex | OpenAI Developers](https://developers.openai.com/codex/config-reference)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用此页面作为 Codex 配置文件的可搜索参考。有关概念指导和示例，请从 配置基础 和 高级配置 开始。
- ``config.toml``：用户级配置保存在 `~/.codex/config.toml` 中。您还可以在 `.codex/config.toml` 文件中添加项目范围的覆盖。Codex 仅在您信…

## 正文整理
### 正文
使用此页面作为 Codex 配置文件的可搜索参考。有关概念指导和示例，请从 配置基础 和 高级配置 开始。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### `config.toml`
用户级配置保存在 `~/.codex/config.toml` 中。您还可以在 `.codex/config.toml` 文件中添加项目范围的覆盖。Codex 仅在您信任该项目时加载项目范围的配置文件。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 对于沙盒和批准密钥 (`approval_policy`、`sandbox_mode` 和 `sandbox_workspace_write.*`)，请将此参考与 沙盒和批准、可写根中的受保护路径 和 网络访问 一起使用。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- | 键 | 类型 / 值 | 详情 | | --- | --- | --- | | `agents.<name>.config_file` | `string (path)` | 此角色的 TOML 配置层的路径；相对路径以声明角色的配置文件为基准解析。 | | `agents.<name>.des…（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 键

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
