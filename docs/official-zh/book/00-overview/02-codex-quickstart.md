# 第02章 快速入门

> 原始页面：[Quickstart – Codex | OpenAI Developers](https://developers.openai.com/codex/quickstart)

这一章属于入门部分，作用是先把 Codex 是什么、能做什么、应该从哪里开始用讲清楚。

如果你还没有建立整体印象，这一章最重要；后面的很多概念都会默认你已经知道这些背景。

## 本章先抓重点
- 每个ChatGPT计划都包括Codex。
- `设置`：应用推荐IDE扩展Codex 在你的 IDE中CLI在终端中使用CodexCloud浏览器中的Codex

## 正文整理
### 正文
每个ChatGPT计划都包括Codex。

继续往下看，这一节还强调了两件事： 
- 您还可以通过使用OpenAI API密钥登录来使用Codex和API积分。（实现：[auth](/codex/codex-rs/core/src/auth.rs#L1)、[auth/storage](/codex/codex-rs/core/src/auth/storage.rs#L1)、[login crate](/codex/codex-rs/login/src/lib.rs#L1)、[cloud-tasks auth helper](/codex/codex-rs/cloud-tasks/src/util.rs#L62)）

### 设置
应用推荐IDE扩展Codex 在你的 IDE中CLI在终端中使用CodexCloud浏览器中的Codex（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- Codex应用程序可在macOS和Windows上使用。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 大多数Codex应用程序功能在两个平台上均可用。平台特定的例外在相关文档中注明。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 1. 下载并安装Codex应用程序（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
