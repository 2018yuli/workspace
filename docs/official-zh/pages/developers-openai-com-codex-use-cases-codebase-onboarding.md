---
source: https://developers.openai.com/codex/use-cases/codebase-onboarding
title: "Understand large codebases | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:08:55.134Z
model: gpt-4o-mini
---
## 搜索Codex文档

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

主要导航

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

文档  用例

- [主页](https://developers.openai.com/codex/use-cases)
- [分类](https://developers.openai.com/codex/use-cases/collections)

[API仪表板](https://platform.openai.com/login)

Codex用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex用例

# 理解大型代码库

追踪请求流，映射不熟悉的模块，快速找到正确的文件。

难度 **简单**

时间范围 **5分钟**

使用Codex来映射不熟悉的代码库，解释不同的模块和数据流，并指引您在编辑前阅读下一个值得关注的文件。

## 最适合

- 新工程师进行新仓库或服务的上岗培训
- 任何试图理解功能在更改之前如何工作的人员

# 内容

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用Codex来映射不熟悉的代码库，解释不同的模块和数据流，并指引您在编辑前阅读下一个值得关注的文件。

简单

5分钟

相关链接

[Codex应用](https://developers.openai.com/codex/app)

## 最适合

- 新工程师进行新仓库或服务的上岗培训
- 任何试图理解功能在更改之前如何工作的人员

## 开始提示

解释请求如何在代码库中的 <name of the system area> 流动。

包括：
\- 哪些模块拥有哪些功能
\- 数据在哪里进行验证
\- 在进行更改之前需要注意的主要陷阱

最后给出我应该阅读的下一个文件。

[在Codex应用中打开](codex://new?prompt=Explain+how+the+request+flows+through+%3Cname+of+the+system+area%3E+in+the+codebase.%0A%0AInclude%3A%0A-+which+modules+own+what%0A-+where+data+is+validated%0A-+the+top+gotchas+to+watch+for+before+making+changes%0A%0AEnd+with+the+files+I+should+read+next. "在Codex应用中打开")

解释请求如何在代码库中的 <name of the system area> 流动。

包括：
\- 哪些模块拥有哪些功能
\- 数据在哪里进行验证
\- 在进行更改之前需要注意的主要陷阱

最后给出我应该阅读的下一个文件。

## 介绍

当您对一个仓库不熟悉或进入一个不熟悉的功能时，Codex可以帮助您在开始更改代码之前进行定位。目标不仅仅是获得一个高层次的总结，而是映射请求流，理解哪些模块拥有哪些功能，并确定下一个值得阅读的文件。

## 如何使用

如果您是新项目的用户，可以简单地开始请求Codex解释整个代码库：

解释这个仓库给我

如果您需要在现有代码库中贡献新功能，可以请求Codex解释特定的系统区域。请求越具体，解释越具体：

1. 给Codex提供您正在尝试理解的相关文件、目录或功能区域。
2. 请求它追踪请求流并解释哪些模块拥有业务逻辑、传输、持久性或UI。
3. 询问数据验证、旁作用或状态转换在您编辑任何内容之前发生在哪里。
4. 最后询问我应该阅读哪些文件以及哪些地方存在风险。

有用的入职回答应该给您提供一个具体的地图，而不仅仅是文件名的列表。到最后，Codex应该已经解释了主要流，突出了风险部分，并指引您到下一个重要的文件或检查内容。

## 接下来要问的问题

一旦Codex给您一个初步的解释，继续提问直到解释具体到您会信任自己进行第一次编辑的程度。良好的后续问题通常会迫使其指出假设、隐含依赖关系及更改后需要注意的检查内容。

- 哪个模块拥有实际的业务逻辑，而不是传输或UI层？
- 验证在哪里发生，那里执行了什么假设？
- 如果我更改这个流，哪些相关文件或后台作业容易被忽视？
- 修改这个区域后我应该运行哪些测试或检查？

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**迭代困难问题**\\
\\
给Codex一个评估系统，比如脚本和可审查的工件，这样它可以继续... \\
\\
工程  分析](https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**创建基于浏览器的游戏**\\
\\
使用Codex将游戏简报转变为首先一个明确定义的计划，然后是一个真正的基于浏览器的... \\
\\
工程  代码](https://developers.openai.com/codex/use-cases/browser-games) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**学习一个新概念**\\
\\
使用Codex来研读材料，如研究论文或课程，分配阅读... \\
\\
知识工作  数据](https://developers.openai.com/codex/use-cases/learn-a-new-concept)
