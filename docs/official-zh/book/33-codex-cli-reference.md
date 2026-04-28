# 第33章 命令行选项

> 原始页面：[Command line options – Codex CLI | OpenAI Developers](https://developers.openai.com/codex/cli/reference)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。

## 严谨定义
严格地说，提示是对目标函数、约束条件和验证标准的联合描述。

## 你读完应该抓住什么
- `如何阅读此参考`：此页面记录了每个文档化的 Codex CLI 命令和标志。使用互动表格按关键字或描述进行搜索。每个部分指示该选项是否稳定或实。
- `全局标志`：| 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--add-dir` | `path` 。
- `命令概述`：成熟度列使用功能成熟度标签，例如实验性、Beta 和稳定。有关如何解释这些标签的信息，请参见 功能成熟度。

## 分步理解
### 如何阅读此参考
先说直白版：
此页面记录了每个文档化的 Codex CLI 命令和标志。使用互动表格按关键字或描述进行搜索。每个部分指示该选项是否稳定或实验性，并指出有风险的组合。
CLI 从 `~/.codex/config.toml` 继承大多数默认值。任何您在命令行中传递的 `-c key=value` 重写在该调用中优先使用。有关更多信息，请参见 配置基础。

把它理解成一个更严谨的过程：
1. 此页面记录了每个文档化的 Codex CLI 命令和标志。使用互动表格按关键字或描述进行搜索。每个部分指示该选项是否稳定或实验性，并指出有风险的组合。
2. CLI 从 `~/.codex/config.toml` 继承大多数默认值。任何您在命令行中传递的 `-c key=value` 重写在该调用中优先使用。有关更多信息，请参见 配置基础。

### 全局标志
先说直白版：
| 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--add-dir` | `path` | 授予其他目录与主工作区相同的写入访问权限。重复以获取多个路径。 | | `--ask-for-approval, -a` | `untrusted | on-request | never` | 控制 Codex 在运行命令之前何时暂停等待人工批准。 `on-failure` 已弃用；对于交互式运行，优先使用 `on-request`，对于非交互式运行则使用 `never`。 | | `--cd, -C` | `path` | 在代理开始处理请求之前设置工作目录。 | | `--config, -c` | `key=value` | 重写配置值。值在可能的情况下解析为 JSON；否则使用字面字符串。 | | `--dangerously-bypass-approvals-and-sandbox, --yolo` | `boolean` | 在没有批准或沙盒的情况下运行每个命令。仅在外部强化的环境中使用。 | | `--disable` | `feature` | 强制禁用一个功能标志（对应于 `-c features.<name>=false`）。可重复。 | | `--enable` | `feature` | 强制启用一个功能标志（对应于 `-c features.<name>=true`）。可重复。 | | `--full-auto` | `boolean` | 低摩擦本地工作的快捷方式：设置 `--ask-for-approval on-request` 和 `--sandbox workspace-write`。 | | `--image, -i` | `path[,path...]` | 将一个或多个图像文件附加到初始提示。使用逗号分隔多个路径或重复该标志。 | | `--model, -m` | `string` | 重写在配置中设置的模型（例如 `gpt-5.4`）。 | | `--no-alt-screen` | `boolean` | 禁用 TUI 的替代屏幕模式（覆盖 `tui.alternate_screen` 在此运行）。 | | `--oss` | `boolean` | 使用本地开源模型提供者（相当于 `-c model_provider="oss"`）。验证 Ollama 是否正在运行。 | | `--profile, -p` | `string` | 要从 `~/.codex/config.toml` 加载的配置配置文件名。 | | `--remote` | `ws://host:port | wss://host:port` | 将交互式 TUI 连接到远程应用服务器 WebSocket 端点。支持 `codex`、`codex resume` 和 `codex fork`；其他子命令拒绝远程模式。 | | `--remote-auth-token-env` | `ENV_VAR` | 从此环境变量读取承载令牌，并在使用 `--remote` 连接时发送。需要 `--remote`；仅在 `wss://` URL 或其主机为 `localhost`、`127.0.0.1` 或 `::1` 的 `ws://` URL 上发送令牌。 | | `--sandbox, -s` | `read-only | workspace-write | danger-full-access` | 选择模型生成的 shell 命令的沙盒策略。 | | `--search` | `boolean` | 启用实时网络搜索（将 `web_search` 设置为 `"live"`，而不是默认的 `"cached"`）。 | | `PROMPT` | `string` | 启动会话的可选文本指令。省略以在没有预填消息的情况下启动 TUI。 |
键
`--add-dir`
类型 / 值

把它理解成一个更严谨的过程：
1. | 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--add-dir` | `path` | 授予其他目录与主工作区相同的写入访问权限。重复以获取多个路径。 | | `--ask-for-approval, -a` | `untrusted | on-request | never` | 控制 Codex 在运行命令之前何时暂停等待人工批准。 `on-failure` 已弃用；对于交互式运行，优先使用 `on-request`，对于非交互式运行则使用 `never`。 | | `--cd, -C` | `path` | 在代理开始处理请求之前设置工作目录。 | | `--config, -c` | `key=value` | 重写配置值。值在可能的情况下解析为 JSON；否则使用字面字符串。 | | `--dangerously-bypass-approvals-and-sandbox, --yolo` | `boolean` | 在没有批准或沙盒的情况下运行每个命令。仅在外部强化的环境中使用。 | | `--disable` | `feature` | 强制禁用一个功能标志（对应于 `-c features.<name>=false`）。可重复。 | | `--enable` | `feature` | 强制启用一个功能标志（对应于 `-c features.<name>=true`）。可重复。 | | `--full-auto` | `boolean` | 低摩擦本地工作的快捷方式：设置 `--ask-for-approval on-request` 和 `--sandbox workspace-write`。 | | `--image, -i` | `path[,path...]` | 将一个或多个图像文件附加到初始提示。使用逗号分隔多个路径或重复该标志。 | | `--model, -m` | `string` | 重写在配置中设置的模型（例如 `gpt-5.4`）。 | | `--no-alt-screen` | `boolean` | 禁用 TUI 的替代屏幕模式（覆盖 `tui.alternate_screen` 在此运行）。 | | `--oss` | `boolean` | 使用本地开源模型提供者（相当于 `-c model_provider="oss"`）。验证 Ollama 是否正在运行。 | | `--profile, -p` | `string` | 要从 `~/.codex/config.toml` 加载的配置配置文件名。 | | `--remote` | `ws://host:port | wss://host:port` | 将交互式 TUI 连接到远程应用服务器 WebSocket 端点。支持 `codex`、`codex resume` 和 `codex fork`；其他子命令拒绝远程模式。 | | `--remote-auth-token-env` | `ENV_VAR` | 从此环境变量读取承载令牌，并在使用 `--remote` 连接时发送。需要 `--remote`；仅在 `wss://` URL 或其主机为 `localhost`、`127.0.0.1` 或 `::1` 的 `ws://` URL 上发送令牌。 | | `--sandbox, -s` | `read-only | workspace-write | danger-full-access` | 选择模型生成的 shell 命令的沙盒策略。 | | `--search` | `boolean` | 启用实时网络搜索（将 `web_search` 设置为 `"live"`，而不是默认的 `"cached"`）。 | | `PROMPT` | `string` | 启动会话的可选文本指令。省略以在没有预填消息的情况下启动 TUI。 |
2. 键
3. `--add-dir`
4. 类型 / 值

### 命令概述
先说直白版：
成熟度列使用功能成熟度标签，例如实验性、Beta 和稳定。有关如何解释这些标签的信息，请参见 功能成熟度。
| 键 | 成熟度 | 详细信息 | | --- | --- | --- | | `codex` | 稳定 | 启动终端用户界面。接受上述全局标志以及可选提示或图像附加。 | | `codex app` | 稳定 | 在 macOS 或 Windows 上启动 Codex 桌面应用。 在 macOS 上，Codex 可以打开工作区路径；在 Windows 上，Codex 打印要打开的路径。 | | `codex app-server` | 实验性 | 启动用于本地开发或调试的 Codex 应用服务器。 | | `codex apply` | 稳定 | 将 Codex Cloud 任务生成的最新差异应用到您的本地工作树。别名：`codex a`。 | | `codex cloud` | 实验性 | 从终端浏览或执行 Codex Cloud 任务，而不打开 TUI。别名：`codex cloud-tasks`。 | | `codex completion` | 稳定 | 为 Bash、Zsh、Fish 或 PowerShell 生成 shell 完成脚本。 | | `codex debug app-server send-message-v2` | 实验性 | 通过内置测试客户端发送单个 V2 消息以调试应用服务器。 | | `codex exec` | 稳定 | 以非交互方式运行 Codex。别名：`codex e`。将结果流式传输到 stdout 或 JSONL，并可选择恢复先前的会话。 | | `codex execpolicy` | 实验性 | 评估 execpolicy 规则文件，并查看命令是否被允许、提示或阻止。 | | `codex features` | 稳定 | 列出功能标志，并在 `config.toml` 中持久化启用或禁用它们。 | | `codex fork` | 稳定 | 将先前的交互会话分叉到新线程，保留原始记录。 | | `codex login` | 稳定 | 使用 ChatGPT OAuth、设备认证或通过 stdin 管道传递的 API 密钥认证 Codex。 | | `codex logout` | 稳定 | 移除存储的认证凭据。 | | `codex mcp` | 实验性 | 管理模型上下文协议服务器（列表、添加、删除、认证）。 | | `codex mcp-server` | 实验性 | 通过 stdio 运行 Codex 本身作为 MCP 服务器。当另一个代理使用 Codex 时非常有用。 | | `codex plugin marketplace` | 实验性 | 从 Git 或本地源添加、升级或删除插件市场。 | | `codex resume` | 稳定 | 通过 ID 继续先前的交互会话，或恢复最近的对话。 | | `codex sandbox` | 实验性 | 在 Codex 提供的 macOS seatbelt 或 Linux bubblewrap 沙盒中运行任意命令。 |
键
成熟度

把它理解成一个更严谨的过程：
1. 成熟度列使用功能成熟度标签，例如实验性、Beta 和稳定。有关如何解释这些标签的信息，请参见 功能成熟度。
2. | 键 | 成熟度 | 详细信息 | | --- | --- | --- | | `codex` | 稳定 | 启动终端用户界面。接受上述全局标志以及可选提示或图像附加。 | | `codex app` | 稳定 | 在 macOS 或 Windows 上启动 Codex 桌面应用。 在 macOS 上，Codex 可以打开工作区路径；在 Windows 上，Codex 打印要打开的路径。 | | `codex app-server` | 实验性 | 启动用于本地开发或调试的 Codex 应用服务器。 | | `codex apply` | 稳定 | 将 Codex Cloud 任务生成的最新差异应用到您的本地工作树。别名：`codex a`。 | | `codex cloud` | 实验性 | 从终端浏览或执行 Codex Cloud 任务，而不打开 TUI。别名：`codex cloud-tasks`。 | | `codex completion` | 稳定 | 为 Bash、Zsh、Fish 或 PowerShell 生成 shell 完成脚本。 | | `codex debug app-server send-message-v2` | 实验性 | 通过内置测试客户端发送单个 V2 消息以调试应用服务器。 | | `codex exec` | 稳定 | 以非交互方式运行 Codex。别名：`codex e`。将结果流式传输到 stdout 或 JSONL，并可选择恢复先前的会话。 | | `codex execpolicy` | 实验性 | 评估 execpolicy 规则文件，并查看命令是否被允许、提示或阻止。 | | `codex features` | 稳定 | 列出功能标志，并在 `config.toml` 中持久化启用或禁用它们。 | | `codex fork` | 稳定 | 将先前的交互会话分叉到新线程，保留原始记录。 | | `codex login` | 稳定 | 使用 ChatGPT OAuth、设备认证或通过 stdin 管道传递的 API 密钥认证 Codex。 | | `codex logout` | 稳定 | 移除存储的认证凭据。 | | `codex mcp` | 实验性 | 管理模型上下文协议服务器（列表、添加、删除、认证）。 | | `codex mcp-server` | 实验性 | 通过 stdio 运行 Codex 本身作为 MCP 服务器。当另一个代理使用 Codex 时非常有用。 | | `codex plugin marketplace` | 实验性 | 从 Git 或本地源添加、升级或删除插件市场。 | | `codex resume` | 稳定 | 通过 ID 继续先前的交互会话，或恢复最近的对话。 | | `codex sandbox` | 实验性 | 在 Codex 提供的 macOS seatbelt 或 Linux bubblewrap 沙盒中运行任意命令。 |
3. 键
4. 成熟度

### `codex`（交互式）
先说直白版：
运行 `codex` 而不带子命令启动交互式终端用户界面（TUI）。代理接受上述全局标志以及图像附件。网络搜索默认为缓存模式；使用 `--search` 切换到实时浏览，并使用 `--full-auto` 让 Codex 在没有提示的情况下运行大部分命令。
使用 `--remote ws://host:port` 或 `--remote wss://host:port` 将 TUI 连接到使用 `codex app-server --listen ws://IP:PORT` 启动的应用服务器。当前服务器需要承载令牌进行 WebSocket 身份验证时，请添加 `--remote-auth-token-env <ENV_VAR>`。有关设置示例和身份验证指导，请参见 Codex CLI 功能。

把它理解成一个更严谨的过程：
1. 运行 `codex` 而不带子命令启动交互式终端用户界面（TUI）。代理接受上述全局标志以及图像附件。网络搜索默认为缓存模式；使用 `--search` 切换到实时浏览，并使用 `--full-auto` 让 Codex 在没有提示的情况下运行大部分命令。
2. 使用 `--remote ws://host:port` 或 `--remote wss://host:port` 将 TUI 连接到使用 `codex app-server --listen ws://IP:PORT` 启动的应用服务器。当前服务器需要承载令牌进行 WebSocket 身份验证时，请添加 `--remote-auth-token-env <ENV_VAR>`。有关设置示例和身份验证指导，请参见 Codex CLI 功能。

### `codex app-server`
先说直白版：
在本地启动 Codex 应用服务器。这主要用于开发和调试，可能会更改而不另行通知。
| 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--listen` | `stdio:// | ws://IP:PORT` | 传输监听器 URL。使用 `ws://IP:PORT` 为远程客户端公开 WebSocket 端点。 | | `--ws-audience` | `string` | 签名的承载令牌预期的 `aud` 声明。需要 `--ws-auth signed-bearer-token`。 | | `--ws-auth` | `capability-token | signed-bearer-token` | 应用服务器 WebSocket 客户端的身份验证模式。如果省略，则禁用 WebSocket 身份验证；本地外部监听器在启动时发出警告。 | | `--ws-issuer` | `string` | 签名的承载令牌预期的 `iss` 声明。需要 `--ws-auth signed-bearer-token`。 | | `--ws-max-clock-skew-seconds` | `number` | 在验证签名的承载令牌 `exp` 和 `nbf` 声明时的时钟偏差容忍度。需要 `--ws-auth signed-bearer-token`。 | | `--ws-shared-secret-file` | `absolute path` | 包含用于验证签名 JWT 承载令牌的 HMAC 共享秘密的文件。与 `--ws-auth signed-bearer-token` 一起使用。 | | `--ws-token-file` | `absolute path` | 包含共享能力令牌的文件。与 `--ws-auth capability-token` 一起使用。 |
键
`--listen`

把它理解成一个更严谨的过程：
1. 在本地启动 Codex 应用服务器。这主要用于开发和调试，可能会更改而不另行通知。
2. | 键 | 类型 / 值 | 详细信息 | | --- | --- | --- | | `--listen` | `stdio:// | ws://IP:PORT` | 传输监听器 URL。使用 `ws://IP:PORT` 为远程客户端公开 WebSocket 端点。 | | `--ws-audience` | `string` | 签名的承载令牌预期的 `aud` 声明。需要 `--ws-auth signed-bearer-token`。 | | `--ws-auth` | `capability-token | signed-bearer-token` | 应用服务器 WebSocket 客户端的身份验证模式。如果省略，则禁用 WebSocket 身份验证；本地外部监听器在启动时发出警告。 | | `--ws-issuer` | `string` | 签名的承载令牌预期的 `iss` 声明。需要 `--ws-auth signed-bearer-token`。 | | `--ws-max-clock-skew-seconds` | `number` | 在验证签名的承载令牌 `exp` 和 `nbf` 声明时的时钟偏差容忍度。需要 `--ws-auth signed-bearer-token`。 | | `--ws-shared-secret-file` | `absolute path` | 包含用于验证签名 JWT 承载令牌的 HMAC 共享秘密的文件。与 `--ws-auth signed-bearer-token` 一起使用。 | | `--ws-token-file` | `absolute path` | 包含共享能力令牌的文件。与 `--ws-auth capability-token` 一起使用。 |
3. 键
4. `--listen`

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
