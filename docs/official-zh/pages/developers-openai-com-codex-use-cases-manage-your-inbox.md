---
source: https://developers.openai.com/codex/use-cases/manage-your-inbox
title: "Manage your inbox | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:16:36.437Z
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

文档  用例

- [首页](https://developers.openai.com/codex/use-cases)
- [合集](https://developers.openai.com/codex/use-cases/collections)

[API 仪表板](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 管理您的收件箱

让 Codex 找到重要的邮件，并以您的声音写回复。

难度 **简单**

时间估计 **5分钟**

使用 Codex 与 Gmail 配合，查找需要关注的邮件，以您的语气起草回复，从您工作的工具中提取上下文，并按照计划持续监测新回复。

## 最适合

- 希望 Codex 查找需要关注的邮件，而不是手动排序的人。
- 定期检查收件箱，Codex 可以在后台创建可审阅的草稿。

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 与 Gmail 配合，查找需要关注的邮件，以您的语气起草回复，从您工作的工具中提取上下文，并按照计划持续监测新回复。

简单

5分钟

相关链接

[Codex 插件](https://developers.openai.com/codex/plugins) [Codex 自动化](https://developers.openai.com/codex/app/automations)

## 最适合

- 希望 Codex 查找需要关注的邮件，而不是手动排序的人。
- 定期检查收件箱，Codex 可以在后台创建可审阅的草稿。

## 技能与插件

- [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail)

搜索和审核 Gmail 线程，阅读周围的对话，创建回复草稿，并在您明确请求时组织消息。

- [Slack](https://github.com/openai/plugins/tree/main/plugins/slack)

在邮箱需要最新决策、拥有者、资产或障碍时检查团队消息上下文。

- [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive)

阅读源文档、常见问题、笔记或应当形塑草稿的批准写作示例。

| 技能 | 为什么使用它 |
| --- | --- |
| [Gmail](https://github.com/openai/plugins/tree/main/plugins/gmail) | 搜索和审核 Gmail 线程，阅读周围的对话，创建回复草稿，并在您明确请求时组织消息。 |
| [Slack](https://github.com/openai/plugins/tree/main/plugins/slack) | 在邮箱需要最新决策、拥有者、资产或障碍时检查团队消息上下文。 |
| [Google Drive](https://github.com/openai/plugins/tree/main/plugins/google-drive) | 阅读源文档、常见问题、笔记或应当形塑草稿的批准写作示例。 |

## 开始提示

您能检查我的 @gmail，找出我需要回复的内容，并以我的语气撰写草稿吗。

使用我最近的已发送回复或 @google-drive \[写作示例\] 进行语气调整。

在邮件缺少最新决策、拥有者、文件或障碍时，使用 @slack、@google-drive 或我工作的其他来源。

[在 Codex 应用中打开](codex://new?prompt=Can+you+check+my+%40gmail%2C+figure+out+what+I+need+to+respond+to%2C+and+write+drafts+in+my+voice.%0A%0AUse+my+recent+sent+replies+or+%40google-drive+%5Bwriting+examples%5D+for+tone.%0A%0AUse+%40slack%2C+%40google-drive%2C+or+other+sources+where+my+work+happens+when+the+email+is+missing+the+latest+decision%2C+owner%2C+file%2C+or+blocker. "在 Codex 应用中打开")

您能检查我的 @gmail，找出我需要回复的内容，并以我的语气撰写草稿吗。

使用我最近的已发送回复或 @google-drive \[写作示例\] 进行语气调整。

在邮件缺少最新决策、拥有者、文件或障碍时，使用 @slack、@google-drive 或我工作的其他来源。

## 审查您的收件箱

要求 Codex 检查 Gmail，找到值得回复的消息，並以您的语气写草稿。它可以使用最近发出的邮件或批准的写作示例来调整风格，然后在电子邮件缺乏上下文时搜索 Slack、文档、项目笔记或其他工具。

使用 Codex 对您的收件箱进行第一次检查：找到需要您关注的电子邮件，草拟回复，并引入解释大局的工作上下文。

1. 请 Codex 审查 Gmail 中需要您关注的电子邮件。
2. 请它使用 Slack、文档或项目笔记来获取解释大局的上下文。
3. 告诉 Codex 哪些草稿是有用的，哪些邮件下次应该忽略。
4. 当邮件线索有用时，添加自动化，并将其固定以便以后快速访问。

直接使用 Gmail 插件。您可以给 Codex 一个广泛的收件箱请求、时间窗口或标签，如果您已经知道范围。如果语气很重要，请请求 Codex 查看最近的已发送回复或包含示例的文档，然后再草拟。

使用此页面上的入门提示进行第一次收件箱检查。Codex 应返回一个简短队列：需要关注的电子邮件草稿、可以等待的消息，以及在答案依赖于超过电子邮件线程的更多上下文时使用的上下文。

## 让线程学习您的喜好

将第一次检查视为校准。如果 Codex 起草了太多回复，请告知它哪些邮件是噪音。如果它遗漏了重要内容，请解释该线程为何重要。如果语气不对，请直接修正草稿。

好的开始。对于未来的检查：

\- 为 \[重要的电子邮件类型\] 草拟回复  
\- 忽略 \[时事通讯、资讯、日历重复或其他噪音\]  
\- 听起来更像 \[更简短、更温暖、更直接或不那么正式\]  
\- 当线程提到 \[项目、账目或团队\] 时，使用 @slack 获取上下文

随着时间推移，线程应该在决定需要草拟什么和什么可以暂时搁置方面变得更好。

## 按计划自动化邮件分类

您可以创建自动化任务，定期检查同一线程。Codex 会唤醒，检查 Gmail 和您指定的上下文来源，只有在需要您关注的电子邮件或值得审阅的草稿时才发布。

一旦草稿看起来有用，请请求 Codex 关注 Gmail。邮件分类是一个很好的自动化工作：草稿是可审核的，您仍然决定发送什么。

您能关注我的 @gmail 并为需要我关注的电子邮件创建草稿吗？

检查 \[每小时、每个工作日早晨或下午 4 点\]。

在需要时使用 @slack 或 @google-drive 获取上下文。跳过明显的噪音。不要发送任何内容。

在该线程对您的回复模式有良好理解后，将此与 Codex [自动化](https://developers.openai.com/codex/app/automations) 一起使用。如果 Codex 找到需要决策的电子邮件，它无法做出响应，应该标记问题而不是猜测。

## 组织您的收件箱

Gmail 插件还可以帮助您组织收件箱。在您信任分类后，请将其作为单独的命令保留。

存档或标记此次检查中低优先级的邮件。

仅处理您列出的 \[可以等待、通讯或已处理\] 的消息。

不要删除或发送任何内容。

对于删除，明确且狭窄地制定指令。草拟回复是安全的以供审核；破坏性清理应保持谨慎。

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**设置团队成员**\\
\\
连接工作发生的工具，教一个线程什么是重要的，然后添加自动化... \\
\\
自动化  集成](https://developers.openai.com/codex/use-cases/proactive-teammate) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**完成来自消息的任务**\\
\\
使用计算机阅读一个消息线程、完成任务并撰写回复。 \\
\\
知识工作  集成](https://developers.openai.com/codex/use-cases/complete-tasks-from-messages) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**协调新员工入职**\\
\\
使用 Codex 收集批准的新员工上下文、阶段跟踪更新、撰写团队逐步的... \\
\\
集成  数据](https://developers.openai.com/codex/use-cases/new-hire-onboarding)
