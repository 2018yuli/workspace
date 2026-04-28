# Codex 通俗书

这套书根据 `docs/official-zh/pages` 中的官方中文页面整理而成，但现在不再只是按官网导航平铺，而是进一步按业务架构主题聚合成目录。

这样整理后，你可以从两个角度阅读：

1. 按主题读：先看某一类业务能力在系统里如何成型。
2. 按编号读：保留原章节编号，方便和之前的引用、链接、笔记保持一致。

## 主题目录

### 00 总览
- [00-overview/README.md](./00-overview/README.md)
- 适合第一次建立全局认识：Codex 是什么、怎么开始、能做什么、成本大致怎样。

### 01 核心概念
- [01-concepts/README.md](./01-concepts/README.md)
- 适合建立系统心智模型：提示、记忆、沙盒、子代理、工作流、模型、网络安全。

### 02 应用层
- [02-app/README.md](./02-app/README.md)
- 适合理解桌面 App 这一层的核心业务：线程、审阅、自动化、工作树、本地环境、浏览器、命令。

### 03 IDE 与 CLI
- [03-ide-cli/README.md](./03-ide-cli/README.md)
- 适合理解开发者一线交互入口：IDE 插件与 CLI 的功能、命令、配置入口。

### 04 云与集成
- [04-cloud-integrations/README.md](./04-cloud-integrations/README.md)
- 适合理解云线程、环境、网络访问，以及 GitHub / Slack / Linear 这类业务接入面。

### 05 配置与扩展
- [05-config-extensibility/README.md](./05-config-extensibility/README.md)
- 适合理解系统如何被定制：配置、规则、钩子、AGENTS.md、MCP、插件、技能、扩展式子代理。

### 06 安全与治理
- [06-security-admin/README.md](./06-security-admin/README.md)
- 适合理解权限边界、身份、远程连接、企业治理、托管配置等管理能力。

### 07 自动化与程序接入
- [07-automation-sdk/README.md](./07-automation-sdk/README.md)
- 适合理解非交互执行、SDK、应用服务器、Agents SDK 这类程序化接入能力。

### 08 学习与发布
- [08-learning-release/README.md](./08-learning-release/README.md)
- 适合作为附录与演进视角：最佳实践、视频、团队方法、更新日志、成熟度、开源。

## 系统架构总览

- `codex/codex-rs/core`：主业务编排层，线程、工具、记忆、模型、技能、MCP、审批都在这里汇总。
- `codex/codex-rs/app-server`：App / IDE 的通信与消息处理入口。
- `codex/codex-rs/config` 与 `codex/codex-rs/core/src/config`：配置模型、约束和加载流程。
- `codex/codex-rs/state`：线程、日志、agent job、记忆等持久化状态。
- `codex/codex-rs/linux-sandbox`、`codex/codex-rs/windows-sandbox-rs`、`codex/codex-rs/shell-escalation`：本地权限边界与沙盒执行。
- `codex/codex-rs/cloud-tasks`：云任务与后台任务的任务视图、状态和交互入口。
- `codex/codex-rs/mcp-server`、`codex/codex-rs/core/src/mcp_*`：MCP 工具接入与调用链。
- `codex/sdk/typescript`：外部程序调用 Codex 的 TypeScript SDK。

## 阅读建议

1. 如果你想先懂“它是什么”，从 `00 总览` 开始。
2. 如果你想先懂“它内部怎么运作”，从 `01 核心概念` 开始。
3. 如果你关心具体入口，按 `02 应用层`、`03 IDE 与 CLI`、`04 云与集成` 分别进入。
4. 如果你关心系统可控性和二次开发，重点看 `05 配置与扩展`、`06 安全与治理`、`07 自动化与程序接入`。
