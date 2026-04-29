# 第04章 定价

> 原始页面：[Pricing – Codex | OpenAI Developers](https://developers.openai.com/codex/pricing)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 团队现在可以在没有固定月费的情况下开始使用 Codex。有限时间内，符合条件的 ChatGPT Business 工作区其团队成员开始使用 Codex 后可以获得高达 $500 的积分。 查看\\ 条…
- `定价选项`：个人版 商业 / 企业版
- `免费`：探索 Codex 在快速编码任务上的能力。

## 正文整理
### 正文
团队现在可以在没有固定月费的情况下开始使用 Codex。有限时间内，符合条件的 ChatGPT Business 工作区其团队成员开始使用 Codex 后可以获得高达 $500 的积分。 查看\\ 条款 或 开始。

### 定价选项
个人版 商业 / 企业版

### 免费
探索 Codex 在快速编码任务上的能力。

继续往下看，这一节还强调了两件事：
- $0/月

### Go
在轻量级编码任务中使用 Codex。

继续往下看，这一节还强调了两件事：
- $8/月

### Plus
每周进行几次集中的编码会话。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- $20/月
- Codex 在 Web、CLI、IDE 扩展和 iOS 上（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 云集成，如自动代码审查和 Slack 集成（实现：[review_prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[tasks/review](/codex/codex-rs/core/src/tasks/review.rs#L1)、[app-server review tests](/codex/codex-rs/app-server/tests/suite/v2/review.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
