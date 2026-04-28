# 第61章 托管配置

> 原始页面：[Managed configuration – Codex | OpenAI Developers](https://developers.openai.com/codex/enterprise/managed-configuration)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
沙盒像在平面直角坐标系里画出的一个有边界的定义域。函数只能在定义域内取值，超出范围就不允许。

## 严谨定义
严格地说，沙盒是执行权限、文件范围和外部访问能力的约束集合。

## 你读完应该抓住什么
- 企业管理员可以通过两种方式控制本地 Codex 行为：
- `管理员强制要求 (requirements.toml)`：要求限制安全敏感设置（批准政策、批准审阅者、自动审阅政策、沙盒模式、Web 搜索模式。
- `位置和优先级`：Codex 按以下顺序应用要求层（早期 wins 每个字段）：

## 分步理解
### 正文
先说直白版：
企业管理员可以通过两种方式控制本地 Codex 行为：
- **要求**：管理员强制施加的限制，用户无法覆盖。
- **管理默认值**：Codex 启动时应用的初始值。用户仍可以在会话期间更改设置；Codex 在下次启动时重新应用管理默认值。

把它理解成一个更严谨的过程：
1. 企业管理员可以通过两种方式控制本地 Codex 行为：
2. **要求**：管理员强制施加的限制，用户无法覆盖。
3. **管理默认值**：Codex 启动时应用的初始值。用户仍可以在会话期间更改设置；Codex 在下次启动时重新应用管理默认值。

### 管理员强制要求 (requirements.toml)
先说直白版：
要求限制安全敏感设置（批准政策、批准审阅者、自动审阅政策、沙盒模式、Web 搜索模式、管理钩子，以及可选用户可以启用的 MCP 服务器）。在解析配置时（例如，从 `config.toml`、配置文件或 CLI 配置覆盖），如果值与强制规则冲突，Codex 将还原到兼容值并通知用户。如果你配置了 `mcp_servers` 允许列表，Codex 仅当其名称和身份与批准的条目匹配时才启用 MCP 服务器；否则，Codex 将其禁用。
要求还可以通过 `requirements.toml` 中的 `[features]` 表限制 功能标志。请注意，功能不总是安全敏感，但企业可以根据需要固定值。省略的键将保持不受限制。
关于确切的键列表，请参见 配置参考中的 `requirements.toml` 部分。

把它理解成一个更严谨的过程：
1. 要求限制安全敏感设置（批准政策、批准审阅者、自动审阅政策、沙盒模式、Web 搜索模式、管理钩子，以及可选用户可以启用的 MCP 服务器）。在解析配置时（例如，从 `config.toml`、配置文件或 CLI 配置覆盖），如果值与强制规则冲突，Codex 将还原到兼容值并通知用户。如果你配置了 `mcp_servers` 允许列表，Codex 仅当其名称和身份与批准的条目匹配时才启用 MCP 服务器；否则，Codex 将其禁用。
2. 要求还可以通过 `requirements.toml` 中的 `[features]` 表限制 功能标志。请注意，功能不总是安全敏感，但企业可以根据需要固定值。省略的键将保持不受限制。
3. 关于确切的键列表，请参见 配置参考中的 `requirements.toml` 部分。

### 位置和优先级
先说直白版：
Codex 按以下顺序应用要求层（早期 wins 每个字段）：
1. 云管理要求（ChatGPT 商务版或企业版） 2. macOS 管理偏好（MDM）通过 `com.openai.codex:requirements_toml_base64` 3. 系统 `requirements.toml`（Unix 系统上的 `/etc/codex/requirements.toml`，包括 Linux/macOS，或 Windows 上的 `%ProgramData%\OpenAI\Codex\requirements.toml`）
在各层之间，Codex 按字段合并要求：如果较早的层设置了某字段（包括空列表），后来的层不会覆盖该字段，但较低的层仍可以填充未设置的字段。
为了向后兼容，Codex 还解释遗留的 `managed_config.toml` 字段 `approval_policy` 和 `sandbox_mode` 作为要求（仅允许该单一值）。

把它理解成一个更严谨的过程：
1. Codex 按以下顺序应用要求层（早期 wins 每个字段）：
2. 1. 云管理要求（ChatGPT 商务版或企业版） 2. macOS 管理偏好（MDM）通过 `com.openai.codex:requirements_toml_base64` 3. 系统 `requirements.toml`（Unix 系统上的 `/etc/codex/requirements.toml`，包括 Linux/macOS，或 Windows 上的 `%ProgramData%\OpenAI\Codex\requirements.toml`）
3. 在各层之间，Codex 按字段合并要求：如果较早的层设置了某字段（包括空列表），后来的层不会覆盖该字段，但较低的层仍可以填充未设置的字段。
4. 为了向后兼容，Codex 还解释遗留的 `managed_config.toml` 字段 `approval_policy` 和 `sandbox_mode` 作为要求（仅允许该单一值）。

### 云管理要求
先说直白版：
当您使用 ChatGPT 登录商务或企业计划时，Codex 还可以从 Codex 服务中获取管理员强制要求。这是另一个与 `requirements.toml` 兼容的要求来源。这适用于 Codex 的所有表面，包括 CLI、应用和 IDE 扩展。

把它理解成一个更严谨的过程：
1. 当您使用 ChatGPT 登录商务或企业计划时，Codex 还可以从 Codex 服务中获取管理员强制要求。这是另一个与 `requirements.toml` 兼容的要求来源。这适用于 Codex 的所有表面，包括 CLI、应用和 IDE 扩展。

### 配置云管理要求
先说直白版：
请访问 Codex 管理配置页面。
使用与 `requirements.toml` 相同的格式和键创建一个新的管理要求文件。
[rules] prefix_rules = [\ { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entrypoints" },\ ] ```
保存配置。保存后，更新的管理要求立即适用于匹配的用户。 有关更多示例，请参见 示例 requirements.toml。

把它理解成一个更严谨的过程：
1. 请访问 Codex 管理配置页面。
2. 使用与 `requirements.toml` 相同的格式和键创建一个新的管理要求文件。
3. [rules] prefix_rules = [\ { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entrypoints" },\ ] ```
4. 保存配置。保存后，更新的管理要求立即适用于匹配的用户。 有关更多示例，请参见 示例 requirements.toml。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
