# 第68章 视频

> 原始页面：[Videos – Codex | OpenAI Developers](https://developers.openai.com/codex/videos)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `开始使用`：- 概述
- `使用 Codex`：- 应用
- `配置`：- 配置文件

## 正文整理
### 开始使用
概述

继续往下看，这一节还强调了两件事：
- 快速入门
- 探索用例
- 定价

### 使用 Codex
应用（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

继续往下看，这一节还强调了两件事：
- 概述
- 功能
- 设置

### 配置
配置文件（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

继续往下看，这一节还强调了两件事：
- 配置基础（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）
- 高级配置（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）
- 配置参考（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### 管理
认证（实现：[auth](/config/workspace/codex/codex-rs/core/src/auth.rs:1)、[auth/storage](/config/workspace/codex/codex-rs/core/src/auth/storage.rs:1)、[login crate](/config/workspace/codex/codex-rs/login/src/lib.rs:1)、[cloud-tasks auth helper](/config/workspace/codex/codex-rs/cloud-tasks/src/util.rs:62)）

继续往下看，这一节还强调了两件事：
- 代理审批与安全（实现：[sandboxing/mod](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:38)、[SandboxManager](/config/workspace/codex/codex-rs/core/src/sandboxing/mod.rs:291)、[config/permissions](/config/workspace/codex/codex-rs/core/src/config/permissions.rs:9)、[linux-sandbox](/config/workspace/codex/codex-rs/linux-sandbox/src/lib.rs:18)）
- 远程连接
- 企业

### 自动化
非交互模式

继续往下看，这一节还强调了两件事：
- Codex SDK
- 应用服务器（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- MCP 服务器（实现：[mcp_connection_manager](/config/workspace/codex/codex-rs/core/src/mcp_connection_manager.rs:546)、[mcp_tool_call](/config/workspace/codex/codex-rs/core/src/mcp_tool_call.rs:1)、[core/mcp/mod](/config/workspace/codex/codex-rs/core/src/mcp/mod.rs:1)、[mcp-server/lib](/config/workspace/codex/codex-rs/mcp-server/src/lib.rs:51)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
