# 第23章 命令

> 原始页面：[Commands – Codex app | OpenAI Developers](https://developers.openai.com/codex/app/commands)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用这些命令和键盘快捷键来导航 Codex 应用。
- `键盘快捷键`：| | 操作 | macOS 快捷键 | | --- | --- | --- | | **通用** | | | | | 命令菜单 | `Cmd` \+ `Shift` \+ `P` 或…
- `斜杠命令`：斜杠命令让您在不离开线程编辑器的情况下控制 Codex。可用的命令根据您的环境和访问权限而异。

## 正文整理
### 正文
使用这些命令和键盘快捷键来导航 Codex 应用。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）

### 键盘快捷键
| | 操作 | macOS 快捷键 | | --- | --- | --- | | **通用** | | | | | 命令菜单 | `Cmd` \+ `Shift` \+ `P` 或 `Cmd` \+ `K` | | | 设置 | `Cmd` \+ `,` | | | 打开文件夹 | `Cmd` \+ `O` | | | 向后导航 | `Cmd` \+ `[` |\ | | 向前导航 | `Cmd` \+ `]` | | | 增加字体…

### 斜杠命令
斜杠命令让您在不离开线程编辑器的情况下控制 Codex。可用的命令根据您的环境和访问权限而异。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 使用斜杠命令
1. 在线程编辑器中输入 `/`。 2. 从列表中选择一个命令，或继续输入进行过滤（例如，`/status`）。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

继续往下看，这一节还强调了两件事：
- 您还可以通过在线程编辑器中输入 `$` 明确调用技能。请参见 技能。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 启用的技能也会出现在斜杠命令列表中。（实现：[SkillsManager](/codex/codex-rs/core/src/skills/manager.rs#L26)、[skills/loader](/codex/codex-rs/core/src/skills/loader.rs#L1)、[skills/injection](/codex/codex-rs/core/src/skills/injection.rs#L1)、[skills/permissions](/codex/codex-rs/core/src/skills/permissions.rs#L1)）

### 可用的斜杠命令
| 斜杠命令 | 描述 | | --- | --- | | `/feedback` | 打开反馈对话框提交反馈，并可选择性地包括日志。 | | `/mcp` | 打开 MCP 状态以查看连接的服务器。 | | `/plan-mode` | 切换多步计划的计划模式。 | | `/review` | 开始代码审查模式，审查未提交的更改或与基础分支比较。 | | `/status` | 显示线程 ID、上下文使用情况和速率限制。 |（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
