# 第60章 治理

> 原始页面：[Governance – Codex | OpenAI Developers](https://developers.openai.com/codex/enterprise/governance)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- # 治理和可观察性
- `跟踪 Codex 使用情况的方法`：有三种方法可以监控 Codex 使用情况，具体取决于你的需求：
- `仪表板`：Codex 提供以下仪表板：

## 正文整理
### 正文
# 治理和可观察性

继续往下看，这一节还强调了两件事：
- Codex 为企业团队提供了对采用情况和影响的可见性，以及安全和合规程序所需的可审核性。使用自助仪表板进行日常跟踪，使用分析 API 进行程序化报告，使用合规 API 将详细日志导出到你的治理堆栈中。（实现：[StateRuntime](/config/workspace/codex/codex-rs/state/src/runtime.rs:63)、[log_db](/config/workspace/codex/codex-rs/state/src/log_db.rs:47)、[extract/apply_rollout_item](/config/workspace/codex/codex-rs/state/src/extract.rs:15)、[state_db](/config/workspace/codex/codex-rs/core/src/state_db.rs:1)）

### 跟踪 Codex 使用情况的方法
有三种方法可以监控 Codex 使用情况，具体取决于你的需求：

继续往下看，这一节还强调了两件事：
- **分析仪表板**：快速查看采用情况和代码审查影响。（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）
- **分析 API**：将结构化的日常指标导入到你的数据仓库或 BI 工具中。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）
- **合规 API**：导出详细的活动日志以进行审核、监控和调查。（实现：[StateRuntime](/config/workspace/codex/codex-rs/state/src/runtime.rs:63)、[log_db](/config/workspace/codex/codex-rs/state/src/log_db.rs:47)、[extract/apply_rollout_item](/config/workspace/codex/codex-rs/state/src/extract.rs:15)、[state_db](/config/workspace/codex/codex-rs/core/src/state_db.rs:1)）

### 仪表板
Codex 提供以下仪表板：

继续往下看，这一节还强调了两件事：
- 按产品（CLI，IDE，云，代码审查）每日用户（实现：[app-server run_main](/config/workspace/codex/codex-rs/app-server/src/lib.rs:295)、[CodexMessageProcessor](/config/workspace/codex/codex-rs/app-server/src/codex_message_processor.rs:399)、[transport](/config/workspace/codex/codex-rs/app-server/src/transport.rs:73)、[thread_state](/config/workspace/codex/codex-rs/app-server/src/thread_state.rs:1)）
- 每日代码审查用户（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）
- 每日代码审查（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）

### 数据导出
管理员还可以将 Codex 分析数据导出为 CSV 或 JSON 格式。Codex 提供以下导出选项：

继续往下看，这一节还强调了两件事：
- 代码审查用户和审查（每日独特用户和已完成的总审查）（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）
- 代码审查发现和反馈（每日评论、反应、回复和优先级发现的数量）（实现：[review_prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[tasks/review](/config/workspace/codex/codex-rs/core/src/tasks/review.rs:1)、[app-server review tests](/config/workspace/codex/codex-rs/app-server/tests/suite/v2/review.rs:1)）
- 云用户和任务（每日独特云用户和已完成的任务）

### 分析 API
当你需要自动化报告、构建内部仪表板或将 Codex 指标与现有工程数据结合使用时，请使用 分析 API。（实现：[StateRuntime::create_agent_job](/config/workspace/codex/codex-rs/state/src/runtime.rs:917)、[StateRuntime::report_agent_job_item_result](/config/workspace/codex/codex-rs/state/src/runtime.rs:1337)、[cloud-tasks App](/config/workspace/codex/codex-rs/cloud-tasks/src/app.rs:47)、[cloud-tasks CLI](/config/workspace/codex/codex-rs/cloud-tasks/src/cli.rs:7)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
