---
source: https://developers.openai.com/codex/use-cases/proactive-teammate
title: "Set up a teammate | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:16:16.851Z
model: gpt-4o-mini
---
## 搜索 Codex 文档

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

主要导航

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

文档 用例

- [首页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 仪表板](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 设置一个团队成员

给 Codex 提供您工作的持久视图，以便它能够注意到发生了什么变化。

难度 **简单**

时间跨度 **长期**

连接工作发生的工具，教一个线程什么是重要的，然后添加一个自动化，以便 Codex 能够注意到更改的文档、被埋藏的请求、被阻塞的交接以及需要您判断的决定。

## 最适合

- 在 Slack、Gmail、日历、文档、追踪器、代码和笔记等上下文中工作的角色
- 理解主动工作、重复决策、协作者，并穿透噪音
- 需要升级值得关注的事物的团队

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

连接工作发生的工具，教一个线程什么是重要的，然后添加一个自动化，以便 Codex 能够注意到更改的文档、被埋藏的请求、被阻塞的交接以及需要您判断的决定。

简单

长期

相关链接

[Codex 自动化](https://developers.openai.com/codex/app/automations) [Codex 插件](https://developers.openai.com/codex/plugins)

## 最适合

- 在 Slack、Gmail、日历、文档、追踪器、代码和笔记等上下文中工作的角色
- 理解主动工作、重复决策、协作者，并穿透噪音
- 需要升级值得关注的事物的团队

## 技能与插件

- [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

查找与请求、所有者更改、阻塞和决策相关的 Slack 上下文。

- [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

查找值得回复的线程，并与工作流中的其余部分进行交叉检查。

- [Google 日历](https://github.com/openai/plugins/tree/main/plugins/google-calendar)

利用当天的会议来决定哪些更新现在重要，哪些可以等待。

- [Notion](https://developers.openai.com/codex/plugins)

阅读定义工作流的项目笔记、追踪器或决策日志。


| 技能 | 使用原因 |
| --- | --- |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | 查找与请求、所有者更改、阻塞和决策相关的 Slack 上下文。 |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | 查找值得回复的线程，并与工作流中的其余部分进行交叉检查。 |
| [Google 日历](https://github.com/openai/plugins/tree/main/plugins/google-calendar) | 利用当天的会议来决定哪些更新现在重要，哪些可以等待。 |
| [Notion](https://developers.openai.com/codex/plugins) | 阅读定义工作流的项目笔记、追踪器或决策日志。 |

## 启动提示

您能检查 @slack、@gmail、@google-calendar 和 @notion 吗，并告诉我有什么需要我注意的？

寻找任何重要或令人惊讶的事情，我可能会错过。

[在 Codex 应用中打开](codex://new?prompt=Can+you+check+%40slack%2C+%40gmail%2C+%40google-calendar%2C+and+%40notion+and+tell+me+what+needs+my+attention%3F%0A%0ALook+for+anything+important+or+surprising+that+I+might+miss. "在 Codex 应用中打开")

您能检查 @slack、@gmail、@google-calendar 和 @notion 吗，并告诉我有什么需要我注意的？

寻找任何重要或令人惊讶的事情，我可能会错过。

## 将 Codex 作为团队成员

Codex 变得更加有用，当它可以看到您的工作发生的位置：Slack、Gmail、日历、项目追踪器、文档、代码和本地笔记。结合这些来源可以呈现您在做什么，您与谁合作，以及哪些请求或决定可能在一天中被埋没。

拥有这样的视图，一个 Codex 线程可以成为一个主动的团队成员。它在您使用时学习您所关心的内容，然后一个自动化将 Codex 重新引导到相同的来源，并返回值得打断您的信号。

您的浏览器不支持视频标签。

## 启动一个团队成员线程

1. 连接工作发生的工具的插件或 MCP。
2. 启动一个新的 Codex 线程，并要求它检查这些来源。
3. 告诉 Codex 哪些项目是有用的，哪些是噪音。
4. 为线程添加一个自动化，然后固定线程并注意通知。
5. 从同一线程操作：提问、获取草稿，并告诉 Codex 接下来采取什么行动。

## 进行一次有用的检查

从已经包含您工作上下文的工具开始。对一个人来说，可能是 Gmail、Slack、日历、Notion、GitHub、Linear 和本地笔记文件夹。要求 Codex 检查这些来源，并告诉您需要关注的内容。

使用本页上的起始提示进行第一次检查。您可以保持其一般性或使其特定于某个工作流、帐户、发布、团队或项目。

有用的 Codex 响应可能如下所示：

![](https://developers.openai.com/assets/OAI_Codex-Blossom_Fallback_Black.svg)
Codex

**一个变化。**

续订准备现在表示客户需要在合作伙伴笔记发送之前添加安全导出措辞。合作伙伴更新仍将工作框架为广泛的报告自动化。

有用的举措是将 Lina 的注释保持在狭窄的范围内：说出导出有助于审计准备，链接续订准备，并在 Owen 签署之前将更广泛的自动化声明排除在外。

**优先级：** 在发送审核包之前更新合作伙伴行。

有用的输出命名触发因素，显示来源，解释含义，并推荐下一步。通过您修正线程时，Codex 了解您如何操作：哪些来源重要，哪些所有者已经拥有工作，直接草稿应该是什么样的，以及什么值得重新提及。

## 将线程转变为自动化

一旦线程变得有用，要求 Codex 在同一线程中继续观察。一个自动化是一个定期检查，当它找到了值得您关注的信号时，会通过您命名的来源再次将 Codex 发送回来，然后发布新消息。它可以每小时运行，每个工作日早晨，或在其他特定时间。

您能监督这些来源并让我知道是否出现任何有用的内容吗？

检查 \[每小时，每个工作日早晨，或在上午九点\]。

这是 Codex [自动化](https://developers.openai.com/codex/app/automations) 的正确形状：先在正常线程中测试提示，然后再向该线程添加自动化。由于 Codex 可以压缩较长的对话，相同的线程可以随着您的修正不断改善，而不是每天早上重新开始。

## 从同一线程操作

警报后，团队成员变得更加有价值。将 Codex 当作您的同事进行操作：在同一线程中提问，然后让它将信号转换为回复、交接说明或决定简报。

这里有什么值得让我惊讶的？

自上次运行以来发生了什么变化？
哪个来源改变了您的推荐？
我接下来该做什么？

根据这个信号起草下一步。

使用来自这个线程的上下文，保持草稿简短，并显示支持它的来源。

不要发送或发布它。

Codex 可以观察、解释和起草。您仍然需要批准外部操作。

## 技术栈

需求

默认选项

为什么需要

需求

检查的来源

默认选项

Slack 用于主动请求，Gmail 用于待处理回复，Google 日历用于时间安排，Notion 或文档用于项目状态。当 GitHub、Linear、MCP 或本地笔记在工作发生的地方时，可以添加它们。

为什么需要

视图越强大，Codex 就越容易理解全局视图，并在不同来源中找到信号。

| 需求 | 默认选项 | 为什么需要 |
| --- | --- | --- |
| 检查的来源 | Slack 用于主动请求，Gmail 用于待处理回复，Google 日历用于时间安排，Notion 或文档用于项目状态。当 GitHub、Linear、MCP 或本地笔记在工作发生的地方时，可以添加它们。 | 视图越强大，Codex 就越容易理解全局视图，并在不同来源中找到信号。 |

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**协调新员工入职**\\
\\
使用 Codex 收集已批准的新员工上下文、阶段追踪更新、团队间的草稿... \\
\\
整合 数据](https://developers.openai.com/codex/use-cases/new-hire-onboarding) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**管理您的收件箱**\\
\\
使用 Codex 和 Gmail 查找需要关注的电子邮件，以您的语气草拟回应，拉... \\
\\
自动化 整合](https://developers.openai.com/codex/use-cases/manage-your-inbox) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**将反馈转化为行动**\\
\\
将 Codex 连接到多个数据源，如 Slack、GitHub、Linear 或 Google Drive，以... \\
\\
数据 整合](https://developers.openai.com/codex/use-cases/feedback-synthesis)
