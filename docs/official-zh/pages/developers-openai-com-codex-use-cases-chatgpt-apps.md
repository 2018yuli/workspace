---
source: https://developers.openai.com/codex/use-cases/chatgpt-apps
title: "Bring your app to ChatGPT | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:07:22.237Z
model: gpt-4o-mini
---
## 搜索 Codex 文档

搜索文档

### 建议

worktreesmcpnoninteractivesandbox

主导航

搜索文档

### 建议

worktreesmcpnoninteractivesandbox

文档 用例

- [主页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 仪表盘](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 将您的应用程序带到 ChatGPT

将您的用例转化为专注的 ChatGPT 应用程序。

难度 **高级**

时间范围 **1小时**

从头到尾构建一个独特的 ChatGPT 应用程序成果：定义工具，搭建 MCP 服务器和可选小部件，连接 ChatGPT，并迭代直到核心流程正常工作。

## 最适合

- 规划围绕用户成果的第一个 ChatGPT 应用程序
- 在不过度构建的情况下，搭建 MCP 服务器、工具元数据和可选小部件
- 从本地 HTTPS 测试到 ChatGPT 开发者模式验证之间运行紧密循环

# 内容

[← 所有用例](https://developers.openai.com/codex/use-cases)

从头到尾构建一个独特的 ChatGPT 应用程序成果：定义工具，搭建 MCP 服务器和可选小部件，连接 ChatGPT，并迭代直到核心流程正常工作。

高级

1小时

相关链接

[应用程序 SDK 快速入门](https://developers.openai.com/apps-sdk/quickstart) [构建 MCP 服务器](https://developers.openai.com/apps-sdk/build/mcp-server) [测试](https://developers.openai.com/apps-sdk/deploy/testing)

## 最适合

- 规划围绕用户成果的第一个 ChatGPT 应用程序
- 在不过度构建的情况下，搭建 MCP 服务器、工具元数据和可选小部件
- 从本地 HTTPS 测试到 ChatGPT 开发者模式验证之间运行紧密循环

## 技能与插件

- [ChatGPT 应用程序](https://github.com/openai/skills/tree/main/skills/.curated/chatgpt-apps)

规划工具，连接 MCP 资源，并遵循当前 ChatGPT 应用程序构建流程。

- [OpenAI 文档](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs)

在 Codex 编写代码或建议架构之前，拉取当前官方的应用程序 SDK 指导。

- [Vercel](https://github.com/openai/plugins/tree/main/plugins/vercel)

通过精选技能和官方 Vercel MCP 服务器，将 Vercel 生态系统指导引入 Codex。


| 技能 | 使用它的原因 |
| --- | --- |
| [ChatGPT 应用程序](https://github.com/openai/skills/tree/main/skills/.curated/chatgpt-apps) | 规划工具，连接 MCP 资源，并遵循当前 ChatGPT 应用程序构建流程。 |
| [OpenAI 文档](https://github.com/openai/skills/tree/main/skills/.curated/openai-docs) | 在 Codex 编写代码或建议架构之前，拉取当前官方的应用程序 SDK 指导。 |
| [Vercel](https://github.com/openai/plugins/tree/main/plugins/vercel) | 通过精选技能和官方 Vercel MCP 服务器，将 Vercel 生态系统指导引入 Codex。 |

## 启动提示

使用 $chatgpt-apps 和 $openai-docs 为此库中的 \[用例\] 规划一个 ChatGPT 应用程序。

要求：
\- 从一个核心用户成果开始。
\- 提议 3-5 个工具，清晰的名称、描述、输入和输出。
\- 推荐 v1 是否需要小部件或可以仅开始数据。
\- 优选 TypeScript 用于 MCP 服务器，React 用于小部件。
\- 指出身份验证、部署和测试要求。

输出：
\- 工具计划
\- 提议的文件树
\- 黄金提示集
\- 风险和开放性问题

[在 Codex 应用中打开](codex://new?prompt=Use+%24chatgpt-apps+with+%24openai-docs+to+plan+a+ChatGPT+app+for+%5Buse+case%5D+in+this+repo.%0A%0ARequirements%3A%0A-+Start+with+one+core+user+outcome.%0A-+Propose+3-5+tools+with+clear+names%2C+descriptions%2C+inputs%2C+and+outputs.%0A-+Recommend+whether+v1+needs+a+widget+or+can+start+data-only.%0A-+Prefer+TypeScript+for+the+MCP+server+and+React+for+the+widget.%0A-+Call+out+auth%2C+deployment%2C+and+test+requirements.%0A%0AOutput%3A%0A-+Tool+plan%0A-+Proposed+file+tree%0A-+Golden+prompt+set%0A-+Risks+and+open+questions "在 Codex 应用中打开")

使用 $chatgpt-apps 和 $openai-docs 为此库中的 \[用例\] 规划一个 ChatGPT 应用程序。

要求：
\- 从一个核心用户成果开始。
\- 提议 3-5 个工具，清晰的名称、描述、输入和输出。
\- 推荐 v1 是否需要小部件或可以仅开始数据。
\- 优选 TypeScript 用于 MCP 服务器，React 用于小部件。
\- 指出身份验证、部署和测试要求。

输出：
\- 工具计划
\- 提议的文件树
\- 黄金提示集
\- 风险和开放性问题

## 您构建的内容

每个 ChatGPT 应用程序有三个部分：

- 一个 MCP 服务器，定义工具，返回数据，强制执行身份验证，并指向任何 UI 资源。
- 一个可选的网页组件，可在 ChatGPT iframe 中呈现。您可以使用 React 或普通的 HTML、CSS 和 JavaScript 构建它。
- 一个模型，根据您提供的元数据决定何时调用应用程序的工具。

当 Codex 负责那些部分的重复工程工作时，它的使用价值最大：

- 规划工具表面和元数据。
- 搭建服务器和小部件。
- 连接本地运行脚本。
- 在专注的过程中添加身份验证和部署更改。
- 编写验证循环，证明应用程序在 ChatGPT 中可用。

## 为什么 Codex 适合

- ChatGPT 应用程序已经清晰地分裂为服务器、可选小部件和基于模型的工具调用。
- Codex 提示在任务明确、范围定义和容易验证时效果最佳，这与应用程序构建工作相匹配。
- 技能和 `AGENTS.md` 给予 Codex 所需的可重用指令和项目规则，使其保持稳定。

要了解有关如何安装和使用技能的更多信息，请参见我们的 [技能文档](https://developers.openai.com/codex/skills)。

## 如何使用

## 先决条件

- 从一个核心用户成果开始，而不是尝试将整个产品移植到聊天中。
- 事先选择技术栈：TypeScript 或 Python 用于服务器，React 或普通 HTML、CSS 和 JavaScript 用于小部件。
- 决定在开发期间使用哪个 HTTPS 路径，例如 `ngrok` 或 Cloudflare Tunnel。
- 当前文档通常称为应用程序，但某些旧页面和设置仍然称为连接器。在本地测试期间，将其视为相同的设置对象。

1. 从一个独特的应用程序成果开始，并请求 Codex 提议三个到五个工具，带有清晰的名称、描述、输入和输出。
2. 决定 v1 是否可以只依赖数据，或需要小部件，然后在添加依赖项之前使用现有库模式搭建 MCP 服务器和可选的小部件。
3. 在 HTTPS 后额外运行本地应用程序，在 ChatGPT 开发者模式中连接，并使用少量直接、间接和负面提示集进行测试。
4. 针对元数据、状态处理、`structuredContent` 和 `_meta` 有效负载进行迭代，直到核心读取流程在 ChatGPT 中表现可靠。
5. 仅在用户特定的数据或写入操作需要时添加 OAuth 2.1，尽可能保持匿名或只读流程简单。
6. 准备一个托管预览，拥有一个稳定的 `/mcp` 端点，验证流媒体和小部件资产托管，并在共享或提交应用程序之前查看发布清单。

## 建议的提示

针对该工作流程的强提示共享相同的成分：

- 一项明确的成果：说明应用程序应该帮助用户在 ChatGPT 中做什么。
- 一个具体的技术栈：说明您希望服务器使用 TypeScript 还是 Python，且小部件应该使用 React 还是保持轻量。
- 明确的工具边界：请求 Codex 提议或构建一小组工具，每个工具负责一项任务。
- 身份验证期望：说明第一个版本是否可以保持匿名，或者是否需要链接的帐户和写入操作。
- 本地开发路径：提及您在 ChatGPT 中进行 HTTPS 测试时预期的隧道或托管路径。
- 验证步骤：告诉 Codex 需要运行的命令、要测试的提示以及要报告的证据。

避免一个庞大的提示，要求在一次通过中进行规划、实施、身份验证、部署、提交和润色。将工作拆分为较小的里程碑。

**在搭建之前先规划应用程序**

使用 $chatgpt-apps 和 $openai-docs 为此库中的 \[用例\] 规划一个 ChatGPT 应用程序。

要求：

\- 从一个核心用户成果开始。
\- 提议 3-5 个工具，清晰的名称、描述、输入和输出。
\- 推荐 v1 是否需要小部件或可以仅开始数据。
\- 优选 TypeScript 用于 MCP 服务器，React 用于小部件。
\- 指出身份验证、部署和测试要求。

输出：

\- 工具计划
\- 提议的文件树
\- 黄金提示集
\- 风险和开放性问题

**搭建第一个工作版本**

使用 $chatgpt-apps 和 $openai-docs 搭建第一个版本的 ChatGPT 应用程序。

技术栈：

\- TypeScript MCP 服务器
\- React 小部件
\- Vite 构建
\- 通过 ngrok 本地 HTTPS

约束：

\- 保持应用程序的独特性：一个读取流程和最多一个写入流程。
\- 为模型返回简明的 `structuredContent`，并为 `_meta` 保留仅小部件的数据。
\- 使工具处理程序具备幂等性。
\- 在添加依赖项之前重用现有库模式。

验证：

\- 启动本地服务器
\- 解释如何在 ChatGPT 开发者模式中连接应用
\- 列出要测试的确切提示

**在核心流程工作后才添加身份验证**

使用 $chatgpt-apps 和 $openai-docs 为此 ChatGPT 应用程序添加身份验证。

要求：

\- 如果可能，保持只读工具匿名。
\- 仅针对用户特定的数据或写入操作添加 OAuth 2.1。
\- 使用现有身份提供者，如 Auth0 或 Stytch。
\- 文档中记录范围、令牌检查和开发者模式测试流程。

输出：

\- 身份验证流程摘要
\- 服务器变更
\- 所需环境变量
\- 端到端测试计划

**准备应用程序以进行部署和审核**

使用 $chatgpt-apps 和 $openai-docs 及 @vercel 准备此 ChatGPT 应用程序进行托管预览。

要求：

\- 显示一个稳定的 HTTPS /mcp 端点。
\- 确保持流媒体响应在 /mcp 上正常工作。
\- 正确托管小部件资产。
\- 添加一个覆盖元数据、工具提示、隐私和测试提示的发布准备清单。

输出：

\- 部署计划
\- 预览 URL 或托管步骤
\- 审核清单
\- 剩余风险

## 发布准备

- 应用程序有一个对用户显而易见的独特成果。
- 工具集保持小并具有明确的元数据、输入和输出。
- MCP 服务器端到端工作，并返回简明的 `structuredContent`，为 `_meta` 保留仅小部件的数据。
- 如果需要，小部件在 ChatGPT 中正确呈现。
- 通过 ChatGPT 开发者模式本地 HTTPS 测试循环正常工作。
- 一组小型的直接、间接和负面提示在预期的对话流程和工具负载中通过。
- 仅在用户特定的数据或写入操作需要时添加身份验证。
- 部署计划和发布准备审查在应用共享或提交之前覆盖元数据、工具提示、隐私和测试提示。

## 常见陷阱

- 请 Codex 将整个产品移植到 ChatGPT。更好的做法：请求一个核心用户成果、三个到五个工具和一个独特的小部件。
- 从一个庞大的实施提示开始。更好的做法：将工作分拆为规划、搭建、身份验证、部署和审核的多个阶段。
- 在工具协议明确之前编写用户界面。更好的做法：先规划工具表面和响应模式，然后构建小部件。
- 跳过官方文档的参考。更好的做法：将 `$chatgpt-apps` 与 `$openai-docs` 配对，以便搭建遵循当前的应用程序 SDK 指导。
- 将元数据视为附加事项。更好的做法：提前编写工具描述和参数文档，然后针对它们重放提示集。
- 在证明匿名或只读路径之前添加身份验证。更好的做法：先使核心工具流程正常工作，然后为确实需要的工具添加 OAuth。
- 在未在 ChatGPT 中进行测试之前声明应用完成。更好的做法：以开发者模式连接应用，检查工具负载，并验证真实的对话流程。

## 技术栈

需要

默认选项

为什么需要

需要

小部件框架

默认选项

[React](https://react.dev/)

为什么需要

对于需要过滤器、表格或多步骤交互的有状态小部件来说是一个强大的默认选择。

需要

托管

默认选项

[Vercel](https://vercel.com/docs)

为什么需要

快速部署、预览环境、自动 HTTPS 和明确的托管 MCP 端点路径。

| 需求 | 默认选项 | 为什么需要 |
| --- | --- | --- |
| 小部件框架 | [React](https://react.dev/) | 对于需要过滤器、表格或多步骤交互的有状态小部件来说是一个强大的默认选择。 |
| 托管 | [Vercel](https://vercel.com/docs) | 快速部署、预览环境、自动 HTTPS 和明确的托管 MCP 端点路径。 |

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**部署应用程序或网站**\\
\\
使用 Codex 与 Build Web Apps 和 Vercel 将库、屏幕截图、设计或粗略应用程序转变为 ... \\
\\
前端 集成](https://developers.openai.com/codex/use-cases/deploy-app-or-website) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**添加 iOS 应用意图**\\
\\
使用 Codex 和 Build iOS Apps 插件，识别您的应用应具有的操作和实体 ... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-app-intents) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**采用液态玻璃**\\
\\
使用 Codex 和 Build iOS Apps 插件审核现有的 iPhone 和 iPad 用户界面，更换自定义 ... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-liquid-glass)
