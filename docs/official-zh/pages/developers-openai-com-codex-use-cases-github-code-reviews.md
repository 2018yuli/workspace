---
source: https://developers.openai.com/codex/use-cases/github-code-reviews
title: "Review pull requests faster | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:13:57.664Z
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

[API 仪表板](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 更快地审核拉取请求

在人工审核之前捕获回归和潜在问题。

难度 **简单**

时间限制 **5秒**

在 GitHub 中使用 Codex 自动检测拉取请求中的回归、缺少的测试和文档问题。

## 最适合

- 希望在人工合并审批之前获得另一种审核信号的团队
- 用于生产中的大型代码库

# 内容

[← 所有用例](https://developers.openai.com/codex/use-cases)

在 GitHub 中使用 Codex 自动检测拉取请求中的回归、缺少的测试和文档问题。

简单

5秒

相关链接

[在 GitHub 中使用 Codex](https://developers.openai.com/codex/integrations/github) [与 AGENTS.md 的自定义指令](https://developers.openai.com/codex/guides/agents-md)

## 最适合

- 希望在人工合并审批之前获得另一种审核信号的团队
- 用于生产中的大型代码库

## 技能与插件

- [安全最佳实践](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices)

将审核重点放在风险高的表面，如机密、认证和依赖关系更改。


| 技能 | 使用原因 |
| --- | --- |
| [安全最佳实践](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | 将审核重点放在风险高的表面，如机密、认证和依赖关系更改。 |

## 启动提示

@codex 审核安全回归、缺少的测试和风险行为变化。

@codex 审核安全回归、缺少的测试和风险行为变化。

## 如何使用

首先将 Codex 代码审查添加到您的 GitHub 组织或仓库中。请参阅 [在 GitHub 中使用 Codex](https://developers.openai.com/codex/integrations/github) 获取详细信息。

您可以设置 Codex 自动审核每个拉取请求，或者您可以在拉取请求评论中使用 `@codex review` 请求审查。

如果 Codex 标记了回归或潜在问题，您可以通过在拉取请求中评论后续提示，例如 `@codex fix it` 来请求它修复问题。

这将启动一个新的云任务，修复该问题并更新拉取请求。

## 定义附加指导

要自定义 Codex 的审核内容，可以添加或更新一个顶级 `AGENTS.md`，其中包含如下部分：

```
## 审核指南

- 将错别字和语法问题标记为 P0 问题。
- 将潜在缺少的文档标记为 P1 问题。
- 将缺少的测试标记为 P1 问题。
  ...


```

Codex 会将指导应用于每个更改文件中最近的 `AGENTS.md`。您可以在树中更深处放置更具体的指令，以便对特定包进行额外的审查。

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**部署应用或网站**\\
\\
使用 Codex 和 Build Web Apps 及 Vercel 将一个仓库、截图、设计或粗略应用...... \\
\\
前端  集成](https://developers.openai.com/codex/use-cases/deploy-app-or-website) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**将您的应用带入 ChatGPT**\\
\\
构建一个狭窄的 ChatGPT 应用结果：定义工具、搭建 MCP 服务器...... \\
\\
集成  代码](https://developers.openai.com/codex/use-cases/chatgpt-apps) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**从消息中完成任务**\\
\\
使用计算机使用读取一条消息线程，完成任务，并草拟回复。 \\
\\
知识工作  集成](https://developers.openai.com/codex/use-cases/complete-tasks-from-messages)
