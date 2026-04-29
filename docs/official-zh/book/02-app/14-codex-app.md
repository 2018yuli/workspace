# 第14章 概述

> 原始页面：[App – Codex | OpenAI Developers](https://developers.openai.com/codex/app)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- Codex 应用程序是一个专注的桌面体验，旨在并行处理 Codex 线程，内置工作树支持、自动化和 Git 功能。
- `入门`：Codex 应用程序适用于 macOS 和 Windows。
- `使用 Codex 应用程序`：**在项目之间多任务处理** \\ \\ 并排运行项目线程，并快速切换之间。 **工作树** \\ \\ 利用内置 Git 工作树支持将并行代码更改隔离。 **计算机使…

## 正文整理
### 正文
Codex 应用程序是一个专注的桌面体验，旨在并行处理 Codex 线程，内置工作树支持、自动化和 Git 功能。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划包含 Codex。了解更多关于 包含的内容。

### 入门
Codex 应用程序适用于 macOS 和 Windows。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 大多数 Codex 应用程序功能在两个平台上均可用。平台特定的例外将在相关文档中注明。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 1. 下载并安装 Codex 应用程序（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 下载适用于 macOS 或 Windows 的 Codex 应用程序。如果您使用的是基于 Intel 的 Mac，请选择 Intel 版本。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 使用 Codex 应用程序
**在项目之间多任务处理** \\ \\ 并排运行项目线程，并快速切换之间。 **工作树** \\ \\ 利用内置 Git 工作树支持将并行代码更改隔离。 **计算机使用** \\ \\ 让 Codex 使用 macOS 应用程序进行 GUI 任务、浏览器流程和本地应用程序测试。 **审查和发布更改** \\ \\ 检查差异、处理 PR 反馈、暂存文件、提交…（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- * * *
- 需要帮助吗？访问 故障排除指南。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
