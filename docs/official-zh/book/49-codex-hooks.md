# 第49章 钩子

> 原始页面：[Hooks – Codex | OpenAI Developers](https://developers.openai.com/codex/hooks)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。

## 严谨定义
严格地说，配置是运行时行为的参数化描述。

## 你读完应该抓住什么
- 钩子是 Codex 的扩展框架。它们允许您将自己的脚本注入到代理循环中，实现以下功能：
- `Codex 查找钩子的地方`：Codex 在以下两种形式的活动配置层旁发现钩子：
- `配置形状`：钩子分为三个层次：

## 分步理解
### 正文
先说直白版：
钩子是 Codex 的扩展框架。它们允许您将自己的脚本注入到代理循环中，实现以下功能：
- 将对话发送到自定义日志/分析引擎
- 扫描团队的提示，以阻止意外粘贴 API 密钥
- 自动总结对话以创建持久记忆

把它理解成一个更严谨的过程：
1. 钩子是 Codex 的扩展框架。它们允许您将自己的脚本注入到代理循环中，实现以下功能：
2. 将对话发送到自定义日志/分析引擎
3. 扫描团队的提示，以阻止意外粘贴 API 密钥
4. 自动总结对话以创建持久记忆

### Codex 查找钩子的地方
先说直白版：
Codex 在以下两种形式的活动配置层旁发现钩子：
- `hooks.json`
- `config.toml` 中的内联 `[hooks]` 表
在实践中，最有用的四个位置是：

把它理解成一个更严谨的过程：
1. Codex 在以下两种形式的活动配置层旁发现钩子：
2. `hooks.json`
3. `config.toml` 中的内联 `[hooks]` 表
4. 在实践中，最有用的四个位置是：

### 配置形状
先说直白版：
钩子分为三个层次：
- 钩子事件，例如 `PreToolUse`、`PostToolUse` 或 `Stop`
- 匹配器组，用于决定何时匹配该事件
- 一个或多个钩子处理程序，在匹配器组匹配时运行

把它理解成一个更严谨的过程：
1. 钩子分为三个层次：
2. 钩子事件，例如 `PreToolUse`、`PostToolUse` 或 `Stop`
3. 匹配器组，用于决定何时匹配该事件
4. 一个或多个钩子处理程序，在匹配器组匹配时运行

### 从 `requirements.toml` 管理的钩子
先说直白版：
企业管理的需求也可以在 `[hooks]` 下定义钩子。这在管理员希望强制执行钩子配置的情况下非常有用，同时通过 MDM 或其他设备管理系统提供实际脚本。
[hooks] managed_dir = "/enterprise/hooks" windows_managed_dir = 'C:\enterprise\hooks'
[[hooks.PreToolUse]] matcher = "^Bash$"
[[hooks.PreToolUse.hooks]] type = "command" command = "python3 /enterprise/hooks/pre_tool_use_policy.py" timeout = 30 statusMessage = "检查管理的 Bash 命令"

把它理解成一个更严谨的过程：
1. 企业管理的需求也可以在 `[hooks]` 下定义钩子。这在管理员希望强制执行钩子配置的情况下非常有用，同时通过 MDM 或其他设备管理系统提供实际脚本。
2. [hooks] managed_dir = "/enterprise/hooks" windows_managed_dir = 'C:\enterprise\hooks'
3. [[hooks.PreToolUse]] matcher = "^Bash$"
4. [[hooks.PreToolUse.hooks]] type = "command" command = "python3 /enterprise/hooks/pre_tool_use_policy.py" timeout = 30 statusMessage = "检查管理的 Bash 命令"

### 匹配器模式
先说直白版：
`matcher` 字段是过滤钩子触发的正则表达式字符串。使用 `"*"`, `""`，或完全省略 `matcher` 以匹配每个支持事件的出现。
当前，只有某些 Codex 事件认可 `matcher`：
| 事件 | `matcher` 过滤内容 | 备注 | | --- | --- | --- | | `PermissionRequest` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `PostToolUse` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `PreToolUse` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `SessionStart` | 启动源 | 当前运行时值包括 `startup`、`resume` 和 `clear` | | `UserPromptSubmit` | 不支持 | 此事件将忽略任何配置的 `matcher` | | `Stop` | 不支持 | 此事件将忽略任何配置的 `matcher` |
\*对于 `apply_patch`，匹配器也可以使用 `Edit` 或 `Write`。

把它理解成一个更严谨的过程：
1. `matcher` 字段是过滤钩子触发的正则表达式字符串。使用 `"*"`, `""`，或完全省略 `matcher` 以匹配每个支持事件的出现。
2. 当前，只有某些 Codex 事件认可 `matcher`：
3. | 事件 | `matcher` 过滤内容 | 备注 | | --- | --- | --- | | `PermissionRequest` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `PostToolUse` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `PreToolUse` | 工具名称 | 支持包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 | | `SessionStart` | 启动源 | 当前运行时值包括 `startup`、`resume` 和 `clear` | | `UserPromptSubmit` | 不支持 | 此事件将忽略任何配置的 `matcher` | | `Stop` | 不支持 | 此事件将忽略任何配置的 `matcher` |
4. \*对于 `apply_patch`，匹配器也可以使用 `Edit` 或 `Write`。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
