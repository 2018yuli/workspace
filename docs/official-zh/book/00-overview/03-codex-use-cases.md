# 第03章 探索用例

> 原始页面：[Codex use cases](https://developers.openai.com/codex/use-cases)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `建议`：- 首页
- `分类`：- 全部
- `原生`：- iOS

## 正文整理
### 建议
首页

继续往下看，这一节还强调了两件事：
- 集合

### 分类
全部

继续往下看，这一节还强调了两件事：
- 工程
- 评估
- 前端（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 原生
iOS

继续往下看，这一节还强调了两件事：
- macOS

### 工作流程
自动化（实现：[StateRuntime::create_agent_job](/codex/codex-rs/state/src/runtime.rs#L917)、[StateRuntime::report_agent_job_item_result](/codex/codex-rs/state/src/runtime.rs#L1337)、[cloud-tasks App](/codex/codex-rs/cloud-tasks/src/app.rs#L47)、[cloud-tasks CLI](/codex/codex-rs/cloud-tasks/src/cli.rs#L7)）

继续往下看，这一节还强调了两件事：
- 数据
- 集成
- 知识工作

### 团队
全部

继续往下看，这一节还强调了两件事：
- 设计
- 工程
- 运营

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
