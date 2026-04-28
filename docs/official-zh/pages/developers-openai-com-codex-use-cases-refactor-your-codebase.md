---
source: https://developers.openai.com/codex/use-cases/refactor-your-codebase
title: "Refactor your codebase | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:17:04.030Z
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
- [合集](https://developers.openai.com/codex/use-cases/collections)

[API 控制面板](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 重构你的代码库

去除无用代码，现代化遗留模式，同时不改变行为。

难度 **高级**

时间预估 **1小时**

使用 Codex 移除无用代码，解开大型文件的纠缠，合并重复逻辑，并在小的可审查的回合中现代化陈旧模式。

## 最适合

- 拥有无用代码、过大模块、重复逻辑或使常规编辑成本高昂的陈旧抽象的代码库。
- 需要在不将工作变成框架或堆栈迁移的情况下现代化代码的团队。

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 移除无用代码，解开大型文件的纠缠，合并重复逻辑，并在小的可审查的回合中现代化陈旧模式。

高级

1小时

相关链接

[使用 Codex 现代化你的代码库](https://developers.openai.com/cookbook/examples/codex/code_modernization)

## 最适合

- 拥有无用代码、过大模块、重复逻辑或使常规编辑成本高昂的陈旧抽象的代码库。
- 需要在不将工作变成框架或堆栈迁移的情况下现代化代码的团队。

## 技能与插件

- [安全最佳实践](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices)

在合并现代化回合之前，检查安全敏感的清理、依赖关系更改、认证流程和暴露的表面。

- [技能创建者](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)

将经过验证的现代化模式、审查清单或对等工作流转化为可重用的仓库或团队技能。


| 技能 | 使用理由 |
| --- | --- |
| [安全最佳实践](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | 在合并现代化回合之前，检查安全敏感的清理、依赖关系更改、认证流程和暴露的表面。 |
| [技能创建者](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) | 将经过验证的现代化模式、审查清单或对等工作流转化为可重用的仓库或团队技能。 |

## 启动提示

现代化并重构此代码库。

要求：
\- 除非我明确要求功能更改，否则保留行为不变。
\- 首先识别无用代码、重复路径、过大模块、陈旧抽象和减缓变更的遗留模式。
\- 对于每个提议的回合，命名当前行为、结构改进，以及应证明行为保持稳定的验证检查。
\- 将工作拆分为小的可审查的重构回合，例如删除无用代码、简化控制流程、提取助手或用仓库当前约定替换过时模式。
\- 保持公共 API 稳定，除非重构需要更改。
\- 指出任何框架迁移、依赖升级、API 更改或架构变动，这些应拆分为单独的迁移任务。
\- 如果工作范围广泛，提出我们在实施前应创建的文档、规格和对比检查。

提出一个计划来执行此操作。

[在 Codex 应用中打开](codex://new?prompt=Modernize+and+refactor+this+codebase.%0A%0ARequirements%3A%0A-+Preserve+behavior+unless+I+explicitly+ask+for+a+functional+change.%0A-+Start+by+identifying+dead+code%2C+duplicated+paths%2C+oversized+modules%2C+stale+abstractions%2C+and+legacy+patterns+that+are+slowing+changes+down.%0A-+For+each+proposed+pass%2C+name+the+current+behavior%2C+the+structural+improvement%2C+and+the+validation+check+that+should+prove+behavior+stayed+stable.%0A-+Break+the+work+into+small+reviewable+refactor+passes+such+as+deleting+dead+code%2C+simplifying+control+flow%2C+extracting+helpers%2C+or+replacing+outdated+patterns+with+the+repo%27s+current+conventions.%0A-+Keep+public+APIs+stable+unless+a+change+is+required+by+the+refactor.%0A-+Call+out+any+framework+migration%2C+dependency+upgrade%2C+API+change%2C+or+architecture+move+that+should+be+split+into+a+separate+migration+task.%0A-+If+the+work+is+broad%2C+propose+the+docs%2C+specs%2C+and+parity+checks+we+should+create+before+implementation.%0A%0APropose+a+plan+to+do+this. "在 Codex 应用中打开")

现代化并重构此代码库。

要求：
\- 除非我明确要求功能更改，否则保留行为不变。
\- 首先识别无用代码、重复路径、过大模块、陈旧抽象和减缓变更的遗留模式。
\- 对于每个提议的回合，命名当前行为、结构改进，以及应证明行为保持稳定的验证检查。
\- 将工作拆分为小的可审查的重构回合，例如删除无用代码、简化控制流程、提取助手或用仓库当前约定替换过时模式。
\- 保持公共 API 稳定，除非重构需要更改。
\- 指出任何框架迁移、依赖升级、API 更改或架构变动，这些应拆分为单独的迁移任务。
\- 如果工作范围广泛，提出我们在实施前应创建的文档、规格和对比检查。

提出一个计划来执行此操作。

## 引言

当你的代码库积累了未使用的代码、重复的逻辑、陈旧的抽象、大型文件或使每次更改比应该昂贵的遗留模式时，你应该考虑通过重构来减少工程债务。重构旨在改善现有系统的形状，而不是将其转变为堆栈迁移。

Codex 在这里非常有用，因为它可以首先映射混乱区域，然后以小的可审查回合进行清理：删除未使用的路径、解开大型模块、合并重复路径、现代化旧框架模式，并在每个回合周围收紧验证。

目标是在原地改善当前的代码库：

1. 移除未使用的代码、陈旧的助手、旧标志和不再需要的兼容性适配器。
2. 通过提取助手、拆分组件或将副作用移动到更清晰的边界来缩小嘈杂的模块。
3. 用仓库的当前约定替换遗留模式：更新的框架原语、更清晰的类型、更简单的状态流或标准库工具。
4. 在进行下一个更改变得更便宜的同时保持公共行为稳定。

## 如何使用

1. 请求 Codex 在编辑之前映射区域：嘈杂的模块、重复逻辑、未使用的代码、测试、公共契约和仓库已经过时的任何旧模式。
2. 每次选择一个清理主题：移除未使用的代码、简化控制流程、现代化过时的模式，或将大文件拆分为较小的独立文件。
3. 在 Codex 修补文件之前，让它说明当前行为、希望进行的结构改进，以及应证明行为保持稳定的最小检查。
4. 在每个回合后审查并运行最小的有用检查，而不是将整个清理批量成一个差异。
5. 将堆栈更改、依赖迁移和架构变动作为单独的任务，除非它们是完成清理所必需的。

你可以使用计划模式在开始工作之前为重构创建一个计划。

## 利用 ExecPlans

[代码现代化食谱](https://developers.openai.com/cookbook/examples/codex/code_modernization) 介绍了 ExecPlans：让 Codex 保持清理概览的文档，阐明预期的最终状态，记录每个回合后的验证。   
当重构跨越多个模块或需要超过一个会话时，它们非常有用。使用它们记录删除、模式更新、需要保持稳定的契约，以及仍需推迟的内容。

## 使用技能处理可重复模式

[技能](https://developers.openai.com/codex/guides/skills) 在相同清理规则在多个仓库、服务或团队中重复时非常有用。使用特定框架的技能（如有）时，请在风险清理周围添加安全和 CI 技能，并在拥有经过验证的未用代码移除、模块提取或遗留模式现代化清单时创建团队技能。  
如果你在多个代码库中进行相同的现代化操作，Codex 可以帮助将第一次成功的处理转变为可重用的技能。

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**创建 Codex 可以使用的 CLI**\\
\\
请求 Codex 创建一个可组合的 CLI，以便它可以从任何文件夹运行，与仓库脚本结合... \\
\\
工程 代码](https://developers.openai.com/codex/use-cases/agent-friendly-clis) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**创建基于浏览器的游戏**\\
\\
使用 Codex 将游戏简介首先转化为良好定义的计划，然后变成真实基于浏览器的... \\
\\
工程 代码](https://developers.openai.com/codex/use-cases/browser-games) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**运行代码迁移**\\
\\
使用 Codex 将遗留系统映射到新的堆栈，将迁移分阶段进行，并进行验证... \\
\\
工程 代码](https://developers.openai.com/codex/use-cases/code-migrations)
