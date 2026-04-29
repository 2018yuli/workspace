# 第48章 规则

> 原始页面：[Rules – Codex | OpenAI Developers](https://developers.openai.com/codex/rules)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。

## 严谨定义
严格地说，提示是对目标函数、约束条件和验证标准的联合描述。

## 本章先抓重点
- 使用规则控制 Codex 可以在沙盒外运行的命令。
- `创建规则文件`：1. 在活动配置层旁的 `rules/` 文件夹下创建一个 `.rules` 文件（例如，`~/.codex/rules/default.rules`）。
- `理解规则字段`：`prefix_rule()`支持以下字段：

## 正文整理
### 正文
使用规则控制 Codex 可以在沙盒外运行的命令。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

继续往下看，这一节还强调了两件事：
- 规则是实验性的，可能会发生变化。

### 创建规则文件
1. 在活动配置层旁的 `rules/` 文件夹下创建一个 `.rules` 文件（例如，`~/.codex/rules/default.rules`）。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 2. 添加规则。该示例在允许 `gh pr view` 在沙盒外运行之前进行提示。（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）
- # 当 Codex 请求运行匹配的命令时采取的行动。 decision = "prompt",
- # 此规则存在的可选理由。 justification = "允许查看 PR 经过批准",（实现：[sandboxing/mod](/codex/codex-rs/core/src/sandboxing/mod.rs#L38)、[SandboxManager](/codex/codex-rs/core/src/sandboxing/mod.rs#L291)、[config/permissions](/codex/codex-rs/core/src/config/permissions.rs#L9)、[linux-sandbox](/codex/codex-rs/linux-sandbox/src/lib.rs#L18)）

### 理解规则字段
`prefix_rule()`支持以下字段：

继续往下看，这一节还强调了两件事：
- `pattern` **（必需）**：一个非空列表，定义要匹配的命令前缀。每个元素可以是：
- 一个字面字符串（例如，`"pr"`）。
- 字面量的联合（例如，`["view", "list"]`），以匹配该参数位置的替代项。

### Shell 包装器和复合命令
一些工具将多个 shell 命令包装成一个单一的调用，例如：（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

继续往下看，这一节还强调了两件事：
- 由于这种命令可以在一个字符串内隐藏多个操作，Codex 特别处理 `bash -lc`、`bash -c` 及其 `zsh` / `sh` 等效项。

### 当 Codex 可以安全地拆分脚本
如果 shell 脚本是由以下构成的线性命令链：（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）

继续往下看，这一节还强调了两件事：
- 普通单词（没有变量扩展，没有 `VAR=...`、`$FOO`、`*` 等）
- 通过安全操作符连接（`&&`、`||`、`;` 或 `|`）
- 那么 Codex 会解析它（使用 tree-sitter）并在应用规则之前将其拆分为单独的命令。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
