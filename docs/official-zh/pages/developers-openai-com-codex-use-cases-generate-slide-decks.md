---
source: https://developers.openai.com/codex/use-cases/generate-slide-decks
title: "Generate slide decks | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:13:02.623Z
model: gpt-4o-mini
---
## 搜索 Codex 文档

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

主导航

搜索文档

### 推荐

worktreesmcpnoninteractivesandbox

文档 用例

- [首页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 仪表盘](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 生成幻灯片

处理 pptx 文件，使用图像生成自动化幻灯片创建。

难度 **简单**

时间预估 **30 分钟**

使用 Codex 更新现有演示文稿或通过直接编辑幻灯片、生成视觉效果并逐张应用可重复的布局规则来构建新的幻灯片。

## 最适合

- 将笔记或结构化输入转换为可重复使用的幻灯片组的团队
- 从头开始创建新的视觉演示
- 从截图、PDF 或参考演示文稿重建或扩展幻灯片

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 更新现有演示文稿或通过直接编辑幻灯片、生成视觉效果并逐张应用可重复的布局规则来构建新的幻灯片。

简单

30 分钟

相关链接

[图像生成指南](https://developers.openai.com/api/docs/guides/image-generation)

## 最适合

- 将笔记或结构化输入转换为可重复使用的幻灯片组的团队
- 从头开始创建新的视觉演示
- 从截图、PDF 或参考演示文稿重建或扩展幻灯片

## 技能与插件

- [幻灯片](https://github.com/openai/skills/tree/main/skills/.curated/slides)

在 JavaScript 中使用 PptxGenJS 创建和编辑 `.pptx` 幻灯片，配有帮助程序、渲染和验证脚本，以检查溢出、重叠和字体。

- [图像生成](https://github.com/openai/skills/tree/main/skills/.curated/imagegen)

生成符合一种可重用视觉方向的插图、封面艺术、图表和幻灯片视觉效果。

| 技能 | 使用理由 |
| --- | --- |
| [幻灯片](https://github.com/openai/skills/tree/main/skills/.curated/slides) | 在 JavaScript 中使用 PptxGenJS 创建和编辑 `.pptx` 幻灯片，配有帮助程序、渲染和验证脚本，以检查溢出、重叠和字体。 |
| [图像生成](https://github.com/openai/skills/tree/main/skills/.curated/imagegen) | 生成符合一种可重用视觉方向的插图、封面艺术、图表和幻灯片视觉效果。 |

## 启动提示

使用 $slides 和 $imagegen 以以下方式编辑此幻灯片组：
\- 如果存在，在每张幻灯片的右下角添加 logo.png
\- 在幻灯片 X、Y 和 Z 上，将文本移动到左侧，并使用图像生成在右侧生成插图（风格：抽象，数字艺术）
\- 在可行的情况下，保留文本为文本，简单图表为原生 PowerPoint 图表。
\- 添加这些幻灯片：\[在此处描述新的幻灯片\]
\- 在新幻灯片和新文本上使用现有品牌（颜色、字体、布局等）
\- 渲染更新后的幻灯片组为幻灯片图像，审查输出，并在交付前修复布局问题。
\- 在交付前运行溢出和字体替换检查，特别是在幻灯片内容密集的情况下。
\- 在创建一批相关图像时保存可重用的提示或生成注释。

输出：
\- 应用更改的幻灯片副本
\- 关于哪些幻灯片被生成、重写或保持不变的注释

[在 Codex 应用中打开](codex://new?prompt=Use+%24slides+with+%24imagegen+to+edit+this+slide+deck+in+the+following+way%3A+%0A-+If+present%2C+add+logo.png+in+the+bottom+right+corner+on+every+slide%0A-+On+slides+X%2C+Y+and+Z%2C+move+the+text+to+the+left+and+use+image+generation+to+generate+an+illustration+%28style%3A+abstract%2C+digital+art%29+on+the+right%0A-+Preserve+text+as+text+and+simple+charts+as+native+PowerPoint+charts+where+practical.%0A-+Add+these+slides%3A+%5Bdescribe+new+slides+here%5D%0A-+Use+the+existing+branding+on+new+slides+and+new+text+%28colors%2C+fonts%2C+layout%2C+etc.%29+%0A-+Render+the+updated+deck+to+slide+images%2C+review+the+output%2C+and+fix+layout+issues+before+delivery.%0A-+Run+overflow+and+font-substitution+checks+before+delivery%2C+especially+if+the+deck+is+dense.%0A-+Save+reusable+prompts+or+generation+notes+when+you+create+a+batch+of+related+images.%0A%0AOutput%3A%0A-+A+copy+of+the+slide+deck+with+the+changes+applied%0A-+notes+on+which+slides+were+generated%2C+rewritten%2C+or+left+unchanged "在 Codex 应用中打开")

使用 $slides 和 $imagegen 以以下方式编辑此幻灯片组：
\- 如果存在，在每张幻灯片的右下角添加 logo.png
\- 在幻灯片 X、Y 和 Z 上，将文本移动到左侧，并使用图像生成在右侧生成插图（风格：抽象，数字艺术）
\- 在可行的情况下，保留文本为文本，简单图表为原生 PowerPoint 图表。
\- 添加这些幻灯片：\[在此处描述新的幻灯片\]
\- 在新幻灯片和新文本上使用现有品牌（颜色、字体、布局等）
\- 渲染更新后的幻灯片组为幻灯片图像，审查输出，并在交付前修复布局问题。
\- 在交付前运行溢出和字体替换检查，特别是在幻灯片内容密集的情况下。
\- 在创建一批相关图像时保存可重用的提示或生成注释。

输出：
\- 应用更改的幻灯片副本
\- 关于哪些幻灯片被生成、重写或保持不变的注释

## 介绍

您可以使用 Codex 以系统化的方式处理 PowerPoint 幻灯片，使用幻灯片技能通过 PptxGenJS 创建和编辑幻灯片，并利用图像生成为幻灯片生成视觉效果。

可以直接从 Codex 应用中安装技能-请参阅我们的 [技能文档](https://developers.openai.com/codex/skills) 以获取更多详细信息。

您可以从头开始创建新的幻灯片，描述您想要的内容，但理想的工作流程是从现有幻灯片开始-这些幻灯片已经设定了您的品牌指导原则-然后请求 Codex 进行编辑。

## 从源幻灯片和参考开始

如果已有幻灯片，请在进行更改前请 Codex 检查它。

幻灯片技能在此方面有特定要求：在重建布局之前匹配源的宽高比，只有在源材料没有明确定义幻灯片大小时才默认为 16:9。如果参考是截图或 PDF，请先让 Codex 渲染或检查它们，以便视觉上比较幻灯片几何形状，而不是猜测。

## 保持幻灯片可编辑

在构建新幻灯片时，请求 Codex 保持幻灯片可编辑：当幻灯片包含文本、图表或简单布局元素时，它们在可行时应保持为 PowerPoint 原生格式。文本应保持为文本。简单的条形、折线、饼图和直方图可视化应保持为原生图表。对于过于自定义而无法用原生幻灯片对象表示的图表或视觉效果，Codex 可以生成或适当地放置 SVG 和图像资产，而不是将整个幻灯片栅格化。

例如，如果您想构建一个复杂的时间线与插图，而不是生成整个图像，请让 Codex 单独生成每个插图（使用一组风格提示作为参考），将它们放置在幻灯片上，然后用原生线条连接它们。文本和日期也应作为文本对象，而不包括在插图中。

## 有意生成视觉效果

当幻灯片需要封面图像、概念插图或轻量级图表，手动设计工作会比较耗时时，图像生成最有用。先请求 Codex 定义视觉方向，然后在整个幻灯片组中一致使用该方向。

当几张幻灯片需要相关的视觉效果时，要求 Codex 保存它使用的提示或生成注释。这样，幻灯片组在后期扩展时，风格上更易于保持一致。

## 保持幻灯片逻辑明确

幻灯片自动化在 Codex 将每张幻灯片视为自己的决策时效果更好。一些幻灯片应保留准确的副本，一些需要更强的标题和更清晰的结构，而其他幻灯片除了资产清理或格式修正外，应该保持尽量不变。

幻灯片技能还配有捆绑的布局助手。请请求 Codex 将这些助手复制到工作目录并在每个幻灯片组中重用，而不是在每个幻灯片组上重复实现间距、文本大小和图像放置逻辑。

## 交付前验证

幻灯片容易接近正确，但仍可能因文本被截断、字体被替换或布局偏移而在导出后出现问题。幻灯片技能包括将幻灯片渲染为每张 PNG、构建快速的评审蒙太奇、检测超出幻灯片画布的溢出，并报告缺失或替换字体的脚本。

在 Codex 交回最终幻灯片组之前，请求使用这些检查，特别是在幻灯片内容密集或边距紧凑的情况下。

## 示例想法

以下是一些您可以尝试此用例的想法：

### 从头开始的新幻灯片组

您可以从头开始创建新的幻灯片组，逐张描述您希望的内容和整体氛围。
如果您有如徽标或图像等资产，可以将其复制到同一文件夹中，以便 Codex 可以轻松访问它们。

创建一个新的幻灯片组，包含以下幻灯片：
\- 幻灯片 1：带有公司徽标 (logo.png) 和演示标题的标题幻灯片
\- 幻灯片 2：包含演示重点的议程幻灯片
\- 幻灯片 3：\[标题\] \[标语\] \[描述\]
\- ...
\- 幻灯片 N：带有关键要点的结论幻灯片
\- 幻灯片 N+1：带有我照片 (my-picture.png) 的问答幻灯片

### 幻灯片模板更新

您可以定期（每周、每月、每季度等）更新幻灯片模板，增加新内容。
如果您经常这样做，可以创建一个类似 `guidelines.md` 的文件，定义幻灯片的内容和结构以及如何更新。

将其与其他技能结合，以从您首选的数据源提取信息。

例如，如果您需要向利益相关者提供季度更新，可以用新数字和见解更新幻灯片模板。

更新幻灯片模板，从 \[整合 1\] 和 \[整合 2\] 中提取内容。
确保遵循 guidelines.md 中定义的指南。

### 调整现有幻灯片组

如果您构建了一个幻灯片组，但希望调整以修复间距、文字对齐或其他布局问题，可以请 Codex 进行修复。

调整幻灯片组以确保遵循以下布局规则：
\- 当同一幻灯片上有多个项目按行或网格显示时，间距应保持一致。
\- 当同一幻灯片上有多个项目按行或网格显示时，项目应根据内容水平或垂直对齐。
\- 所有文本框应左对齐，除非它们位于插图下方
\- 所有标题应使用字体 \[字体名称\] 和大小 \[大小\]
\- 所有说明应为 \[颜色\]
\- ....

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**协调新员工入职**\\
\\
使用 Codex 收集批准的新员工背景、阶段跟踪更新、团队之间的草稿... \\
\\
整合 数据](https://developers.openai.com/codex/use-cases/new-hire-onboarding) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**将反馈转化为行动**\\
\\
将 Codex 连接到多个数据源，例如 Slack、GitHub、Linear 或 Google Drive... \\
\\
数据 整合](https://developers.openai.com/codex/use-cases/feedback-synthesis) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**完成消息中的任务**\\
\\
使用计算机使用读取某个消息线程，完成任务并起草回复。 \\
\\
知识工作 整合](https://developers.openai.com/codex/use-cases/complete-tasks-from-messages)
