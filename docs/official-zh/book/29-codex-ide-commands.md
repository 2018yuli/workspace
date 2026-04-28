# 第29章 IDE 命令

> 原始页面：[Commands – Codex IDE | OpenAI Developers](https://developers.openai.com/codex/ide/commands)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
线程像解一道多步函数题时保留下来的草稿纸。后一步是否顺利，依赖前面保留下来的中间结果。

## 严谨定义
严格地说，线程是一个按时间顺序累积状态的信息序列。

## 你读完应该抓住什么
- 使用这些命令从 VS Code 命令面板控制 Codex。您还可以将它们绑定到键盘快捷键。
- `分配一个键绑定`：要为 Codex 命令分配或更改键绑定：
- `扩展命令`：| 命令 | 默认键绑定 | 描述 | | --- | --- | --- | | `chatgpt.addToThread` |。

## 分步理解
### 正文
先说直白版：
使用这些命令从 VS Code 命令面板控制 Codex。您还可以将它们绑定到键盘快捷键。

把它理解成一个更严谨的过程：
1. 使用这些命令从 VS Code 命令面板控制 Codex。您还可以将它们绑定到键盘快捷键。

### 分配一个键绑定
先说直白版：
要为 Codex 命令分配或更改键绑定：
1. 打开命令面板（ **Cmd+Shift+P** 在 macOS 上或 **Ctrl+Shift+P** 在 Windows/Linux 上）。 2. 运行 **首选项：打开键盘快捷键**。 3. 搜索 `Codex` 或命令 ID（例如 `chatgpt.newChat`）。 4. 选择铅笔图标，然后输入您想要的快捷键。

把它理解成一个更严谨的过程：
1. 要为 Codex 命令分配或更改键绑定：
2. 1. 打开命令面板（ **Cmd+Shift+P** 在 macOS 上或 **Ctrl+Shift+P** 在 Windows/Linux 上）。 2. 运行 **首选项：打开键盘快捷键**。 3. 搜索 `Codex` 或命令 ID（例如 `chatgpt.newChat`）。 4. 选择铅笔图标，然后输入您想要的快捷键。

### 扩展命令
先说直白版：
| 命令 | 默认键绑定 | 描述 | | --- | --- | --- | | `chatgpt.addToThread` | - | 将选定文本范围添加为当前线程的上下文 | | `chatgpt.addFileToThread` | - | 将整个文件添加为当前线程的上下文 | | `chatgpt.newChat` | macOS: `Cmd+N`<br>Windows/Linux: `Ctrl+N` | 创建一个新线程 | | `chatgpt.implementTodo` | - | 请求 Codex 解决选定的 TODO 注释 | | `chatgpt.newCodexPanel` | - | 创建一个新的 Codex 面板 | | `chatgpt.openSidebar` | - | 打开 Codex 侧边栏面板 |

把它理解成一个更严谨的过程：
1. | 命令 | 默认键绑定 | 描述 | | --- | --- | --- | | `chatgpt.addToThread` | - | 将选定文本范围添加为当前线程的上下文 | | `chatgpt.addFileToThread` | - | 将整个文件添加为当前线程的上下文 | | `chatgpt.newChat` | macOS: `Cmd+N`<br>Windows/Linux: `Ctrl+N` | 创建一个新线程 | | `chatgpt.implementTodo` | - | 请求 Codex 解决选定的 TODO 注释 | | `chatgpt.newCodexPanel` | - | 创建一个新的 Codex 面板 | | `chatgpt.openSidebar` | - | 打开 Codex 侧边栏面板 |

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
