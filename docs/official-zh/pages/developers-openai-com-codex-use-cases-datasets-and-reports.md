---
source: https://developers.openai.com/codex/use-cases/datasets-and-reports
title: "Analyze datasets and ship reports | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:11:53.933Z
model: gpt-4o-mini
---
## 搜索 Codex 文档

搜索文档

### 建议

worktreesmcpnoninteractivesandbox

主要导航

搜索文档

### 建议

worktreesmcpnoninteractivesandbox

文档 使用案例

- [首页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 控制面板](https://platform.openai.com/login)

Codex 使用案例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 使用案例

# 分析数据集并发布报告

将混乱的数据转化为清晰的分析和可视化。

难度 **中级**

时间范围 **1小时**

使用 Codex 清理数据、合并数据源、探索假设、建模结果，并将输出打包为可重用的 artifact。

## 最适合

- 从混乱文件开始的数据分析，最终应生成图表、备忘录、仪表板或报告
- 希望 Codex 帮助清理、合并、探索性分析和可重现脚本的分析师
- 需要可审查的 artifact 而非一次性笔记本状态的团队

# 内容

[← 所有使用案例](https://developers.openai.com/codex/use-cases)

使用 Codex 清理数据、合并数据源、探索假设、建模结果，并将输出打包为可重用的 artifact。

中级

1小时

相关链接

[代理技能](https://developers.openai.com/codex/skills) [Codex 应用中的工作树](https://developers.openai.com/codex/app/worktrees)

## 最适合

- 从混乱文件开始的数据分析，最终应生成图表、备忘录、仪表板或报告
- 希望 Codex 帮助清理、合并、探索性分析和可重现脚本的分析师
- 需要可审查的 artifact 而非一次性笔记本状态的团队

## 技能与插件

- [Spreadsheet](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet)

在公式、导出或快速电子表格检查重要时，检查 CSV、TSV 和 Excel 文件。

- [Jupyter Notebook](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook)

创建或重构笔记本以进行探索性分析、实验和可重用的演练。

- [Doc](https://github.com/openai/skills/tree/main/skills/.curated/doc)

在布局、表格或评论重要时，生成可供利益相关者使用的 \`.docx\` 报告。

- [Pdf](https://github.com/openai/skills/tree/main/skills/.curated/pdf)

渲染 PDF 输出并在共享之前检查最终分析 artifact。

| 技能 | 为什么使用它 |
| --- | --- |
| [Spreadsheet](https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet) | 在公式、导出或快速电子表格检查重要时，检查 CSV、TSV 和 Excel 文件。 |
| [Jupyter Notebook](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) | 创建或重构笔记本以进行探索性分析、实验和可重用的演练。 |
| [Doc](https://github.com/openai/skills/tree/main/skills/.curated/doc) | 在布局、表格或评论重要时，生成可供利益相关者使用的 \`.docx\` 报告。 |
| [Pdf](https://github.com/openai/skills/tree/main/skills/.curated/pdf) | 渲染 PDF 输出并在共享之前检查最终分析 artifact。 |

## 启动提示

我正在这个工作区进行数据分析项目。

目标：
\- 确定靠近高速公路的房屋是否具有较低的房地产估值。

开始：
\- 阅读 \`AGENTS.md\` 并解释推荐的 Python 环境
\- 加载 \[数据集路径\] 的数据集
\- 描述每个文件的内容、可能的合并键和明显的数据质量问题
\- 提出一个可重现的工作流程，从导入和整理到可视化、建模和报告输出

限制：
\- 更倾向于脚本和保存的 artifact 而不是一次性笔记本状态
\- 不要编造缺失值或合并键
\- 提出任何可以使工作流程更可重现的技能或工作树拆分

输出：
\- 设置计划
\- 数据清单
\- 分析计划
\- 首个命令或创建的文件

[在 Codex 应用中打开](codex://new?prompt=I%27m+doing+a+data+analysis+project+in+this+workspace.%0A%0AGoal%3A%0A-+Figure+out+whether+houses+near+the+highway+have+lower+property+valuations.%0A%0AStart+by%3A%0A-+reading+%60AGENTS.md%60+and+explaining+the+recommended+Python+environment%0A-+loading+the+dataset%28s%29+at+%5Bdataset+path%5D%0A-+describing+what+each+file+contains%2C+likely+join+keys%2C+and+obvious+data+quality+issues%0A-+proposing+a+reproducible+workflow+from+import+and+tidy+through+visualization%2C+modeling%2C+and+report+output%0A%0AConstraints%3A%0A-+prefer+scripts+and+saved+artifacts+over+one-off+notebook+state%0A-+do+not+invent+missing+values+or+merge+keys%0A-+suggest+any+skills+or+worktree+splits+that+would+make+the+workflow+more+reproducible%0A%0AOutput%3A%0A-+setup+plan%0A-+data+inventory%0A-+analysis+plan%0A-+first+commands+or+files+to+create "在 Codex 应用中打开")

我正在这个工作区进行数据分析项目。

目标：
\- 确定靠近高速公路的房屋是否具有较低的房地产估值。

开始：
\- 阅读 \`AGENTS.md\` 并解释推荐的 Python 环境
\- 加载 \[数据集路径\] 的数据集
\- 描述每个文件的内容、可能的合并键和明显的数据质量问题
\- 提出一个可重现的工作流程，从导入和整理到可视化、建模和报告输出

限制：
\- 更倾向于脚本和保存的 artifact 而不是一次性笔记本状态
\- 不要编造缺失值或合并键
\- 提出任何可以使工作流程更可重现的技能或工作树拆分

输出：
\- 设置计划
\- 数据清单
\- 分析计划
\- 首个命令或创建的文件

## 介绍

数据分析的核心在于利用数据来指导决策。目标不是为了分析而分析，而是为了产生一个帮助某人采取行动的 artifact：为领导层准备的图表、为产品团队提供的实验结果、为研究人员准备的模型评估，或指导日常操作的仪表板。

一个有用的框架，源于 _R for Data Science_，是一个循环：导入和整理数据，然后在转换、可视化和建模之间迭代，以便建立理解后再传达结果。编程围绕整个循环。

Codex 很好地适应这个工作流程。它帮助你更快地在循环中移动，通过清理数据、探索假设、生成分析和制作可重现的 artifact。目标不是一次性笔记本，而是其他人可以审查、信任和重新运行的工作流程。

## 确定你的使用案例

选择一个你希望通过数据回答的具体问题。

问题越具体越好。这将有助于 Codex 理解你想要实现什么以及如何帮助你实现。

### 运行示例：高速公路附近的房产价值

作为示例，我们将探讨以下问题：

> 靠近高速公路的房屋在物业估值上到底低了多少？

假设一个数据集中包含物业价值或销售价格，而另一个数据集包含位置信息、地块或距离高速公路的信息。工作的不仅仅是运行模型，而是使输入变得可信，记录合并，压力测试结果，并以其他人可以使用的 artifact 结束。

## 设置环境

当你开始一个新的数据分析项目时，需要设置环境并定义项目的规则。

- **环境：** Codex 应该知道该项目的标准 Python 环境、包管理器、文件夹和输出约定。
- **技能：** 重复的工作流程，例如笔记本清理、电子表格导出或最终报告打包，应该转移到可重用的技能中，而不是在每个提示中重新解释。
- **工作树：** 将不同的探索分为不同的工作树，以避免一个假设、合并策略或可视化分支渗透到另一个中。

要了解有关如何安装和使用技能的更多信息，请参阅我们的 [技能文档](https://developers.openai.com/codex/skills)。

### 指导 Codex 的行为

在处理数据之前，告诉 Codex 在该存储库中的行为。将个人默认设置放入 `~/.codex/AGENTS.md`，并在存储库 `AGENTS.md` 中放入项目规则。

一个小的 `AGENTS.md` 通常就足够了：

```
## 数据分析默认设置

- 使用 `uv run` 或项目的现有 Python 环境。
- 将原始数据保存在 `data/raw/` 中，将清理后的数据写入 `data/processed/`。
- 将探索性笔记本放在 `analysis/` 中，并将最终 artifact 放在 `output/` 中。
- 永远不要覆盖原始文件。
- 更倾向于脚本或已检查的笔记本，而不是未命名的临时单元格。
- 在合并数据集之前，报告候选键、空值率和连接覆盖率。
```

如果存储库尚未定义 Python 环境，请要求 Codex 创建一个可重现的设置并解释如何运行它。对于数据分析工作，这一步比直接跳入图表更重要。

## 导入数据

通常，开始的最快方法是粘贴文件路径并请求 Codex 进行检查。此时 Codex 帮助你回答基本但重要的问题：

- 这里有哪些文件格式？
- 每个数据集似乎表示什么？
- 哪些列可能是目标、标识符、日期、位置或度量？
- 清晰的质量问题在哪里？

现在不要要求结论。先请求清单和解释。

## 整理并合并输入

大多数实际工作从这里开始。你有两个或更多数据集，主键不明确，简单合并可能会丢失数据或创建重复。

在执行合并之前，请要求 Codex 对合并进行分析：

- 检查候选键的唯一性。
- 测量空值率和格式差异。
- 标准化明显的格式问题，如大小写、空格或地址格式。
- 运行小规模的试验合并并报告匹配率。
- 在写入最终合并文件之前，建议最安全的合并策略。

如果你需要导出最佳键，例如规范化地址、从几个列构建的地块标识符或位置连接，请让 Codex 解释权衡和边界情况，然后再接受合并。

## 使用图表和单独工作树进行探索

探索性数据分析是 Codex 受益于清晰隔离的地方。一个工作树可以测试地址清理或特征工程，而另一个则专注于图表或替代模型方向。这样可以保持每个差异可审查，并防止长线程混合不兼容的想法。

Codex 应用程序包括内置工作树支持。如果你在终端中使用，普通的 Git 工作树也很好用：

```
git worktree add ../analysis-highway-eda -b analysis/highway-eda
git worktree add ../analysis-model-comparison -b analysis/highway-modeling
```

在运行示例中，这一步是对比靠近高速公路的房屋与远离它的房屋，检查异常值，检查缺失值模式，决定观察到的效果是否真实，或者反映了社区构成、房屋大小或其他因素。

## 建模问题

并非所有分析都需要复杂的模型。先从一个可解释的基线开始。

对于高速公路问题，合理的第一步是回归或其他透明模型，该模型估计高速公路临近性与物业价值之间的关系，同时控制相关因素，例如大小、年龄和位置。

请要求 Codex 明确以下内容：

- 目标变量和特征定义。
- 包括哪些控制及原因。
- 泄漏风险和排除。
- 它如何选择切分、评估或不确定性估计。
- 结果在普通语言中的含义。

如果第一个模型较弱，这仍然是有用的。它告诉你问题是模型、特征、合并质量还是本身的问题。

## 传达结果

分析只能在其他人能够消费时才有用。请求 Codex 生成听众所需的 artifact：

- 面向技术合作伙伴的 Markdown 备忘录。
- 为后续操作工作准备的电子表格或 CSV。
- 使用 `$doc` 生成的布局和表格重要的 \`.docx\` 简报。
- 使用 `$pdf` 渲染的附录或最终交付物。
- 使用 `$vercel-deploy` 部署的轻量级仪表板或静态报告网站。

这也是你请求警告的地方。如果合并质量不完美、存在抽样偏差或模型假设不稳健，Codex 应该在交付物中明确指出。

## 需要考虑的技能

最适合这个工作流程的策划技能包括：

- `$spreadsheet` 用于 CSV、TSV 和 Excel 编辑或导出。
- `$jupyter-notebook` 当交付物应保持为 Notebook 原生时。
- `$doc` 和 `$pdf` 用于面向利益相关者的输出。
- `$vercel-deploy` 当你想通过 URL 分享结果时。

一旦工作流程稳定，为重复部分创建本地技能，例如 `refresh-data`、`merge-and-qa` 或 `publish-weekly-report`。这比在每个线程中粘贴相同的过程提示更具长期价值。

## 建议的提示

**设置分析环境**

我是一名在这个存储库中工作的数据分析师。
阅读 \`AGENTS.md\`，检查是否已经存在 Python 环境，并为此项目设置最小的可重现分析工作流程。

要求：

\- 更倾向于 \`uv\` 和本地 \`.venv\`，除非存储库已经标准化其他内容。
\- 为原始数据、处理过的数据、笔记本和输出创建清晰的文件夹。
\- 解释你将如何运行 Python、安装包和保存 artifact。
\- 不要触及原始数据文件。

**加载数据集并解释**

请加载 \[路径\] 的数据集并解释它。

包括：

\- 每个文件似乎包含什么
\- 可能的标识符、目标列和日期列
\- 文件格式和编码
\- 明显的数据质量问题或缺失的元数据

不要立即得出结论。先从清单和解释开始。

**在合并之前分析合并**

我们需要合并这两个数据集，但主键不明显。

任务：

\- 对候选合并键进行分析
- 显示每个候选的唯一性和空值率
- 标准化明显的格式问题
- 运行小规模的试验合并并报告匹配率
- 在更改任何文件之前，建议最安全的合并策略

**打开一个新的探索工作树**

为高速公路临近性和房产估值的探索性分析创建一个单独的工作树。

在这个工作树中：

\- 生成汇总表和图表
\- 比较靠近高速公路的房屋与远离的房屋
\- 保存图表和简短的 Markdown 读出
\- 仅专注于探索的差异

**构建可解释的第一模型**

建模高速公路临近性是否与较低的房产估值相关联。

要求：

\- 从可解释的基线开始
\- 明确地定义目标、特征和控制
\- 解释泄漏风险和排除
\- 报告效应大小、不确定性和主要局限性
\- 保存建模代码和简短的结果说明

**为利益相关者打包结果**

将这项分析转化为可供利益相关者使用的 artifact。

听众：

\- 决定靠近高速公路的房产是否需要单独定价假设的产品和运营领导者

输出：

\- 一份简短的执行摘要
\- 两到四个支持性图表
\- 一节警告
\- 生成 \`.docx\`、\`.pdf\` 或静态报告网站，具体哪个最合适

同时告诉我，哪个技能最有助于选择的输出。

## 技术栈

需要

默认选项

为什么需要

需要

分析栈

默认选项

[pandas](https://pandas.pydata.org/) 与 [matplotlib](https://matplotlib.org/) 或 [seaborn](https://seaborn.pydata.org/)

为什么需要

作为导入、分析、合并、清理和第一轮图表的良好默认设置。

需要

建模

默认选项

[statsmodels](https://www.statsmodels.org/) 或 [scikit-learn](https://scikit-learn.org/stable/)

为什么需要

从可解释基线开始，然后再转向更复杂的预测模型。

| 需要 | 默认选项 | 为什么需要 |
| --- | --- | --- |
| 分析栈 | [pandas](https://pandas.pydata.org/) 与 [matplotlib](https://matplotlib.org/) 或 [seaborn](https://seaborn.pydata.org/) | 作为导入、分析、合并、清理和第一轮图表的良好默认设置。 |
| 建模 | [statsmodels](https://www.statsmodels.org/) 或 [scikit-learn](https://scikit-learn.org/stable/) | 从可解释基线开始，然后再转向更复杂的预测模型。 |

## 相关使用案例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**协调新员工入职**\\
\\
使用 Codex 收集批准的新员工背景、阶段跟踪更新、草稿团队... \\
\\
集成 数据](https://developers.openai.com/codex/use-cases/new-hire-onboarding) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**查询表格数据**\\
\\
使用 Codex 与 CSV、电子表格、仪表板导出、Google 表格或本地数据文件相结合... \\
\\
数据 知识工作](https://developers.openai.com/codex/use-cases/analyze-data-export) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**将反馈转化为行动**\\
\\
将 Codex 连接到多个数据源，例如 Slack、GitHub、Linear 或 Google Drive... \\
\\
数据 集成](https://developers.openai.com/codex/use-cases/feedback-synthesis)
