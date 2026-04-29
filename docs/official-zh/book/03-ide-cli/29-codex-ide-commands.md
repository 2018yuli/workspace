# 第29章 IDE 命令

> 原始页面：[Commands – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/commands)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 使用这些命令从 VS Code 命令面板控制 Codex。您还可以将它们绑定到键盘快捷键。
- `分配一个键绑定`：要为 Codex 命令分配或更改键绑定：
- `扩展命令`：| 命令 | 默认键绑定 | 描述 | | --- | --- | --- | | `chatgpt.addToThread` | - | 将选定文本范围添加为当前线程的上下文 | | …

## 正文整理
### 正文
使用这些命令从 VS Code 命令面板控制 Codex。您还可以将它们绑定到键盘快捷键。

### 分配一个键绑定
要为 Codex 命令分配或更改键绑定：

继续往下看，这一节还强调了两件事：
- 1. 打开命令面板（ **Cmd+Shift+P** 在 macOS 上或 **Ctrl+Shift+P** 在 Windows/Linux 上）。 2. 运行 **首选项：打开键盘快捷键**。 3. 搜索 `Codex` 或命令 ID（例如 `chatgpt.newChat`）。 4. 选择铅笔图标，然后输入您想要的快捷键。（实现：[web_search](/codex/codex-rs/core/src/web_search.rs#L18)、[network_policy_decision](/codex/codex-rs/core/src/network_policy_decision.rs#L1)、[network-proxy](/codex/codex-rs/network-proxy/src/lib.rs#L1)）

### 扩展命令
| 命令 | 默认键绑定 | 描述 | | --- | --- | --- | | `chatgpt.addToThread` | - | 将选定文本范围添加为当前线程的上下文 | | `chatgpt.addFileToThread` | - | 将整个文件添加为当前线程的上下文 | | `chatgpt.newChat` | macOS: `Cmd+N`<br>Windows/Linux: `Ctrl+N` | 创建一个新线程 | …（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
