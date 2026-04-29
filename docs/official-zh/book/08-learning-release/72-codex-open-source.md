# 第72章 开源

> 原始页面：[Open Source – Codex | OpenAI Developers](https://developers.openai.com/codex/open-source)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- OpenAI 在开放环境中开发 Codex 的关键部分。该项目在 GitHub 上进行，您可以跟踪进展、报告问题并贡献改进。
- `开源组件`：| 组件 | 查找位置 | 备注 | | --- | --- | --- | | Codex CLI | openai/codex | Codex 开源开发的主要家园 | | Codex…
- `报告问题和请求功能`：使用 Codex GitHub 仓库提交有关 Codex 组件的错误报告和功能请求：

## 正文整理
### 正文
OpenAI 在开放环境中开发 Codex 的关键部分。该项目在 GitHub 上进行，您可以跟踪进展、报告问题并贡献改进。（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- 如果您维护一个广泛使用的开源项目，或者想提名管理重要项目的维护者，您也可以申请 Codex for OSS 计划以获取 API 额度、Codex 的 ChatGPT Pro 以及对 Codex 安全的选择性访问。

### 开源组件
| 组件 | 查找位置 | 备注 | | --- | --- | --- | | Codex CLI | openai/codex | Codex 开源开发的主要家园 | | Codex SDK | openai/codex/sdk | SDK 源代码位于 Codex 仓库 | | Codex 应用服务器 | openai/codex/codex-rs/app-server | 应用服务器源代码位于 Codex 仓库 | | 技能 | …（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）

### 报告问题和请求功能
使用 Codex GitHub 仓库提交有关 Codex 组件的错误报告和功能请求：（实现：[git_info](/codex/codex-rs/core/src/git_info.rs#L1)、[undo task](/codex/codex-rs/core/src/tasks/undo.rs#L1)、[review prompts](/codex/codex-rs/core/src/review_prompts.rs#L22)、[commit_attribution](/codex/codex-rs/core/src/commit_attribution.rs#L1)）

继续往下看，这一节还强调了两件事：
- 错误报告和功能请求：openai/codex/issues
- 讨论论坛：openai/codex/discussions
- 提交问题时，请注明您使用的组件（CLI、SDK、IDE 扩展、Codex 网络），并尽可能提供版本信息。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
