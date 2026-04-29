# 第49章 钩子

> 原始页面：[Hooks – Codex | OpenAI Developers](https://developers.openai.com/codex/hooks)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。

## 严谨定义
严格地说，配置是运行时行为的参数化描述。

## 本章先抓重点
- 钩子是 Codex 的扩展框架。它们允许您将自己的脚本注入到代理循环中，实现以下功能：
- `Codex 查找钩子的地方`：Codex 在以下两种形式的活动配置层旁发现钩子：
- `配置形状`：钩子分为三个层次：

## 正文整理
### 正文
钩子是 Codex 的扩展框架。它们允许您将自己的脚本注入到代理循环中，实现以下功能：（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）

继续往下看，这一节还强调了两件事：
- 将对话发送到自定义日志/分析引擎（实现：[StateRuntime](/codex/codex-rs/state/src/runtime.rs#L63)、[log_db](/codex/codex-rs/state/src/log_db.rs#L47)、[extract/apply_rollout_item](/codex/codex-rs/state/src/extract.rs#L15)、[state_db](/codex/codex-rs/core/src/state_db.rs#L1)）
- 扫描团队的提示，以阻止意外粘贴 API 密钥（实现：[custom_prompts](/codex/codex-rs/core/src/custom_prompts.rs#L9)、[project_doc](/codex/codex-rs/core/src/project_doc.rs#L134)、[instructions/user_instructions](/codex/codex-rs/core/src/instructions/user_instructions.rs#L1)）
- 自动总结对话以创建持久记忆（实现：[memories/mod](/codex/codex-rs/core/src/memories/mod.rs#L1)、[memories/storage](/codex/codex-rs/core/src/memories/storage.rs#L1)、[memories/phase1](/codex/codex-rs/core/src/memories/phase1.rs#L1)、[memories/phase2](/codex/codex-rs/core/src/memories/phase2.rs#L1)）

### Codex 查找钩子的地方
Codex 在以下两种形式的活动配置层旁发现钩子：（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- `hooks.json`（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）
- `config.toml` 中的内联 `[hooks]` 表（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 在实践中，最有用的四个位置是：

### 配置形状
钩子分为三个层次：（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）

继续往下看，这一节还强调了两件事：
- 钩子事件，例如 `PreToolUse`、`PostToolUse` 或 `Stop`（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）
- 匹配器组，用于决定何时匹配该事件
- 一个或多个钩子处理程序，在匹配器组匹配时运行（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）

### 从 `requirements.toml` 管理的钩子
企业管理的需求也可以在 `[hooks]` 下定义钩子。这在管理员希望强制执行钩子配置的情况下非常有用，同时通过 MDM 或其他设备管理系统提供实际脚本。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- [hooks] managed_dir = "/enterprise/hooks" windows_managed_dir = 'C:\enterprise\hooks'（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）
- [[hooks.PreToolUse]] matcher = "^Bash$"（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）
- [[hooks.PreToolUse.hooks]] type = "command" command = "python3 /enterprise/hooks/pre_tool_use_policy.py" timeout = 30 statusMessage = "检查管理的 Bash 命令"（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

### 匹配器模式
`matcher` 字段是过滤钩子触发的正则表达式字符串。使用 `"*"`, `""`，或完全省略 `matcher` 以匹配每个支持事件的出现。（实现：[Hooks](/codex/codex-rs/hooks/src/registry.rs#L14)、[Hook types](/codex/codex-rs/hooks/src/types.rs#L34)、[user_notification](/codex/codex-rs/hooks/src/user_notification.rs#L31)）

继续往下看，这一节还强调了两件事：
- 当前，只有某些 Codex 事件认可 `matcher`：
- | 事件 | `matcher` 过滤内容 | 备注 | | --- | --- | --- | | `PermissionRequest` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `PostToolUse` | 工具名称 | 支持包括…（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）
- \*对于 `apply_patch`，匹配器也可以使用 `Edit` 或 `Write`。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
