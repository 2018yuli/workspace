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
- 前端（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）

### 原生
iOS

继续往下看，这一节还强调了两件事：
- macOS

### 工作流程
自动化（实现：[StateRuntime::create_agent_job](/config/workspace/codex/codex-rs/state/src/runtime.rs:917)、[StateRuntime::report_agent_job_item_result](/config/workspace/codex/codex-rs/state/src/runtime.rs:1337)、[cloud-tasks App](/config/workspace/codex/codex-rs/cloud-tasks/src/app.rs:47)、[cloud-tasks CLI](/config/workspace/codex/codex-rs/cloud-tasks/src/cli.rs:7)）

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
