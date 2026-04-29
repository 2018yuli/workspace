# 第21章 应用内浏览器

> 原始页面：[In-app browser – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/browser)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 应用内浏览器为您和 Codex 提供了一个共享视图，可以在线程内查看渲染的网页。当您构建或调试网页应用程序时，可以使用它来预览页面并附加视觉评论。
- `浏览器使用`：浏览器使用让 Codex 直接操作应用内浏览器。请在 Codex 需要点击、输入、检查渲染状态、截图或验证页面中的修复时，使用它用于本地开发服务器和文件支持的预览。
- `预览页面`：1. 在 集成终端 中或通过 本地环境操作 启动您应用的开发服务器。 2. 点击一个网址或手动在浏览器中导航，打开一个未认证的本地路由、文件支持的页面或公共页面。 3. 结合代码差异查看…

## 正文整理
### 正文
应用内浏览器为您和 Codex 提供了一个共享视图，可以在线程内查看渲染的网页。当您构建或调试网页应用程序时，可以使用它来预览页面并附加视觉评论。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 它适用于本地开发服务器、文件支持的预览和不需要登录的公共页面。对于任何依赖于登录状态或浏览器扩展的内容，请使用您常规的浏览器。（实现：[StateRuntime](/codex/codex-rs/state/src/runtime.rs#L63)、[log_db](/codex/codex-rs/state/src/log_db.rs#L47)、[extract/apply_rollout_item](/codex/codex-rs/state/src/extract.rs#L15)、[state_db](/codex/codex-rs/core/src/state_db.rs#L1)）
- 您可以通过工具栏打开应用内浏览器，通过单击网址、手动导航或按 `Cmd` + `Shift` + `B`（在 Windows 上为 `Ctrl` + `Shift` + `B`）。（实现：[tools/orchestrator](/codex/codex-rs/core/src/tools/orchestrator.rs#L43)、[tools/router](/codex/codex-rs/core/src/tools/router.rs#L1)、[tools/registry](/codex/codex-rs/core/src/tools/registry.rs#L1)、[unified_exec/mod](/codex/codex-rs/core/src/unified_exec/mod.rs#L74)）
- 应用内浏览器不支持身份验证流程、已登录的页面、您常规的浏览器配置文件、cookie、扩展或现有选项卡。仅可用于 Codex 可以在不登录的情况下打开的页面。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### 浏览器使用
浏览器使用让 Codex 直接操作应用内浏览器。请在 Codex 需要点击、输入、检查渲染状态、截图或验证页面中的修复时，使用它用于本地开发服务器和文件支持的预览。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 要使用它，请安装并启用浏览器插件。然后，请求 Codex 在您的任务中使用浏览器，或直接用 `@Browser` 引用它。该应用将浏览器使用限制在应用内浏览器中，并允许您从设置中管理允许和阻止的网站。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 示例：
- Codex 在使用网站之前会询问您，除非您已允许它。从允许列表中删除网站意味着 Codex 会再次询问您在使用它之前；从阻止列表中删除网站意味着 Codex 可以再次询问，而不是将其视为被阻止。

### 预览页面
1. 在 集成终端 中或通过 本地环境操作 启动您应用的开发服务器。 2. 点击一个网址或手动在浏览器中导航，打开一个未认证的本地路由、文件支持的页面或公共页面。 3. 结合代码差异查看渲染状态。 4. 在需要更改的元素或区域上留下浏览器评论。 5. 请 Codex 解决这些评论，并保持范围狭窄。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 示例反馈：

### 对页面进行评论
当错误仅在渲染的页面上可见时，请使用浏览器评论为 Codex 提供对页面的精确反馈。

继续往下看，这一节还强调了两件事：
- 打开评论模式，选择一个元素或区域，并提交评论。
- 在评论模式下，按住 `Shift` 并单击以选择一个区域。
- 按住 `Cmd` 同时单击以立即发送评论。

### 保持浏览器任务范围
应用内浏览器用于审核和迭代。保持每个浏览器任务足够小，以便在一次传递中进行审核。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

继续往下看，这一节还强调了两件事：
- 命名页面、路由或本地 URL。
- 命名您关心的视觉状态，例如加载、空、错误或成功。（实现：[StateRuntime](/codex/codex-rs/state/src/runtime.rs#L63)、[log_db](/codex/codex-rs/state/src/log_db.rs#L47)、[extract/apply_rollout_item](/codex/codex-rs/state/src/extract.rs#L15)、[state_db](/codex/codex-rs/core/src/state_db.rs#L1)）
- 在需要更改的确切元素或区域上留下评论。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
