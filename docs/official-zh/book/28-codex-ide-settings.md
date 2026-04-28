# 第28章 设置

> 原始页面：[Settings – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/settings)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。

## 严谨定义
严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。

## 你读完应该抓住什么
- 使用这些设置来自定义 Codex IDE 扩展。
- `更改设置`：要更改设置，请按照以下步骤操作：
- `设置参考`：| 设置 | 描述 | | --- | --- | | `chat.fontSize` | 控制 Codex 边栏中的聊天文本，包。

## 分步理解
### 正文
先说直白版：
使用这些设置来自定义 Codex IDE 扩展。

把它理解成一个更严谨的过程：
1. 使用这些设置来自定义 Codex IDE 扩展。

### 更改设置
先说直白版：
要更改设置，请按照以下步骤操作：
1. 打开您的编辑器设置。 2. 搜索 `Codex` 或设置名称。 3. 更新值。
Codex IDE 扩展使用 Codex CLI。在共享的 `~/.codex/config.toml` 文件中配置某些行为，例如默认模型、审批和沙箱设置，而不是在编辑器设置中。有关更多信息，请参见 配置基础。
该扩展还尊重 VS Code 内置的聊天字体设置，用于 Codex 对话界面。

把它理解成一个更严谨的过程：
1. 要更改设置，请按照以下步骤操作：
2. 1. 打开您的编辑器设置。 2. 搜索 `Codex` 或设置名称。 3. 更新值。
3. Codex IDE 扩展使用 Codex CLI。在共享的 `~/.codex/config.toml` 文件中配置某些行为，例如默认模型、审批和沙箱设置，而不是在编辑器设置中。有关更多信息，请参见 配置基础。
4. 该扩展还尊重 VS Code 内置的聊天字体设置，用于 Codex 对话界面。

### 设置参考
先说直白版：
| 设置 | 描述 | | --- | --- | | `chat.fontSize` | 控制 Codex 边栏中的聊天文本，包括对话内容和撰写器。 | | `chat.editor.fontSize` | 控制 Codex 对话中的代码渲染内容，包括代码片段和差异。 | | `chatgpt.cliExecutable` | 开发专用：Codex CLI 可执行文件的路径。除非您正在积极开发 Codex CLI，否则无需设置此项。如果手动设置此项，则扩展的某些部分可能无法按预期工作。 | | `chatgpt.commentCodeLensEnabled` | 在待办事项评论上方显示 CodeLens，以便您可以使用 Codex 完成它们。 | | `chatgpt.localeOverride` | Codex UI 的首选语言。留空以自动检测。 | | `chatgpt.openOnStartup` | 在扩展启动完成后聚焦 Codex 边栏。 | | `chatgpt.runCodexInWindowsSubsystemForLinux` | 仅适用于 Windows：在可用的情况下，在 WSL 中运行 Codex。在您的代码库和工具位于 WSL2 中或需要 Linux 原生工具时使用此项。否则，Codex 可以在 Windows 上使用 Windows 沙箱原生运行。更改此设置将重新加载 VS Code 以应用更改。 |

把它理解成一个更严谨的过程：
1. | 设置 | 描述 | | --- | --- | | `chat.fontSize` | 控制 Codex 边栏中的聊天文本，包括对话内容和撰写器。 | | `chat.editor.fontSize` | 控制 Codex 对话中的代码渲染内容，包括代码片段和差异。 | | `chatgpt.cliExecutable` | 开发专用：Codex CLI 可执行文件的路径。除非您正在积极开发 Codex CLI，否则无需设置此项。如果手动设置此项，则扩展的某些部分可能无法按预期工作。 | | `chatgpt.commentCodeLensEnabled` | 在待办事项评论上方显示 CodeLens，以便您可以使用 Codex 完成它们。 | | `chatgpt.localeOverride` | Codex UI 的首选语言。留空以自动检测。 | | `chatgpt.openOnStartup` | 在扩展启动完成后聚焦 Codex 边栏。 | | `chatgpt.runCodexInWindowsSubsystemForLinux` | 仅适用于 Windows：在可用的情况下，在 WSL 中运行 Codex。在您的代码库和工具位于 WSL2 中或需要 Linux 原生工具时使用此项。否则，Codex 可以在 Windows 上使用 Windows 沙箱原生运行。更改此设置将重新加载 VS Code 以应用更改。 |

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
