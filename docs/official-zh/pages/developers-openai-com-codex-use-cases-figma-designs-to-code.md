---
source: https://developers.openai.com/codex/use-cases/figma-designs-to-code
title: "Turn Figma designs into code | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:11:04.449Z
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

文档 使用案例

- [首页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 控制面板](https://platform.openai.com/login)

Codex 使用案例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 使用案例

# 将 Figma 设计转化为代码

将 Figma 选择项转化为具有结构化设计上下文和视觉检查的精致用户界面。

难度 **中级**

时间范围 **1小时**

利用 Codex 从 Figma 获取设计上下文、资产和变体，将其翻译为与代码库的设计系统匹配的代码，然后使用 Playwright 将实现与 Figma 参考进行比较，并迭代直到看起来正确。

## 最适合

- 在现有代码库中实现已经设计好的屏幕或流程
- 希望 Codex 从结构化设计上下文中工作的团队

# 目录

[← 所有使用案例](https://developers.openai.com/codex/use-cases)

利用 Codex 从 Figma 获取设计上下文、资产和变体，将其翻译为与代码库的设计系统匹配的代码，然后使用 Playwright 将实现与 Figma 参考进行比较，并迭代直到看起来正确。

中级

1小时

相关链接

[Codex 技能](https://developers.openai.com/codex/skills) [模型上下文协议](https://developers.openai.com/codex/mcp)

## 最适合

- 在现有代码库中实现已经设计好的屏幕或流程
- 希望 Codex 从结构化设计上下文中工作的团队

## 技能与插件

- [Figma](https://github.com/openai/plugins/tree/main/plugins/figma)

在代码中实现设计，创建已发布组件与源文件之间的代码连接映射，并生成项目特定的设计系统规则，以便于重复的 Figma 到代码工作。

- [Playwright](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive)

检查响应行为并在真实浏览器中验证已实现的用户界面。

| 技能 | 使用原因 |
| --- | --- |
| [Figma](https://github.com/openai/plugins/tree/main/plugins/figma) | 在代码中实现设计，创建已发布组件与源文件之间的代码连接映射，并生成项目特定的设计系统规则，以便于重复的 Figma 到代码工作。 |
| [Playwright](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive) | 检查响应行为并在真实浏览器中验证已实现的用户界面。 |

## 入门提示

使用 Figma 技能在当前项目中实现此 Figma 设计。

要求：
\- 首先使用 \`get\_design\_context\` 获取确切的节点或框架。
\- 如果响应被截断，使用 \`get\_metadata\` 映射文件，然后仅使用 \`get\_design\_context\` 重新获取所需的节点。
\- 在开始编码之前，运行 \`get\_screenshot\` 获取确切的变体。
\- 复用现有的设计系统组件和令牌。
\- 将 Figma 输出翻译为此代码库的实用工具和组件模式，而不是创造一个平行系统。
\- 精确匹配间距、布局、层次结构和响应行为。
\- 尊重代码库的路由、状态和数据获取模式。
\- 使页面在桌面和移动设备上具有响应性。
\- 如果 Figma 返回 localhost 图像或 SVG 源，则直接使用，而不要创建占位符或添加新的图标包。

验证：
\- 在外观和行为上将最终用户界面与 Figma 参考进行比较。
\- 使用 Playwright 检查用户界面是否与参考相匹配，并根据需要迭代，直到它匹配。

[在 Codex 应用中打开](codex://new?prompt=Implement+this+Figma+design+in+the+current+project+using+the+Figma+skill.%0A%0ARequirements%3A%0A-+Start+with+%60get_design_context%60+for+the+exact+node+or+frame.%0A-+If+the+response+is+truncated%2C+use+%60get_metadata%60+to+map+the+file+and+then+re-fetch+only+the+needed+nodes+with+%60get_design_context%60.%0A-+Run+%60get_screenshot%60+for+the+exact+variant+before+you+start+coding.%0A-+Reuse+the+existing+design+system+components+and+tokens.%0A-+Translate+the+Figma+output+into+this+repo%27s+utilities+and+component+patterns+instead+of+inventing+a+parallel+system.%0A-+Match+spacing%2C+layout%2C+hierarchy%2C+and+responsive+behavior+closely.%0A-+Respect+the+repo%27s+routing%2C+state%2C+and+data-fetch+patterns.%0A-+Make+the+page+responsive+on+desktop+and+mobile.%0A-+If+Figma+returns+localhost+image+or+SVG+sources%2C+use+them+directly+and+do+not+create+placeholders+or+add+new+icon+packages.%0A%0AValidation%3A%0A-+Compare+the+finished+UI+against+the+Figma+reference+for+both+look+and+behavior.%0A-+Use+Playwright+to+check+that+the+UI+matches+the+reference+and+iterate+as+needed+until+it+does. "在 Codex 应用中打开")

使用 Figma 技能在当前项目中实现此 Figma 设计。

要求：
\- 首先使用 \`get\_design\_context\` 获取确切的节点或框架。
\- 如果响应被截断，使用 \`get\_metadata\` 映射文件，然后仅使用 \`get\_design\_context\` 重新获取所需的节点。
\- 在开始编码之前，运行 \`get\_screenshot\` 获取确切的变体。
\- 复用现有的设计系统组件和令牌。
\- 将 Figma 输出翻译为此代码库的实用工具和组件模式，而不是创造一个平行系统。
\- 精确匹配间距、布局、层次结构和响应行为。
\- 尊重代码库的路由、状态和数据获取模式。
\- 使页面在桌面和移动设备上具有响应性。
\- 如果 Figma 返回 localhost 图像或 SVG 源，则直接使用，而不要创建占位符或添加新的图标包。

验证：
\- 在外观和行为上将最终用户界面与 Figma 参考进行比较。
\- 使用 Playwright 检查用户界面是否与参考相匹配，并根据需要迭代，直到它匹配。

## 介绍

当你有确切的 Figma 选择时，Codex 可以在不忽略你项目中已建立的模式的情况下将其转化为精致的用户界面。

通过 Figma 技能，Codex 可以使用 Figma MCP 服务器获取结构化设计上下文、变量、资产和应实现的确切变体。

通过 Playwright 互动技能，Codex 可以在真实浏览器中打开应用，将实现与 Figma 参考进行比较，并迭代布局或行为，直到结果更接近目标。

## 设置你的 Figma 项目

你的 Figma 文件越干净，第一次实现的效果就越好。为了改善交接：

- 尽可能使用变量或设计令牌，特别是对于颜色、排版和间距
- 为可重用的用户界面元素创建组件，而不是重复分离图层
- 尽量使用自动布局，而不是手动定位
- 保持框架和图层名称清晰，以便主要屏幕、状态和变体显而易见
- 尽可能在文件中保留真实的图标和图像，以减少 Codex 的猜测

这为 Codex 提供了更好的结构，使其能够翻译成稳健的、生产级的用户界面。

## 具体明确

你越具体地说明预期的交互模式和想要的样式，结果就会越好。

如果状态、断点或交互很重要，请明确指出。如果文件中包含多个相近的变体，请指明哪一个应被视为真实来源。

你越明确地说明需要精确匹配的内容以及代码库约定应胜出的位置，Codex 做出正确取舍的难度就越小。

## 准备设计系统

Codex 在目标代码库已具有明确组件层时效果最好。Codex 可以自动使用你现有的组件和设计系统，而不必从头开始重建它们。

如果你认为有必要，请向 Codex 指明哪些原始组件可以复用，令牌所在的位置，以及代码库认为的按钮、输入、卡片、排版和图标的规范。

将 Figma MCP 输出视为结构性参考，而不是最终的代码风格。请求 Codex 将该输出翻译为项目的实际实用程序、组件包装器、颜色系统、排版比例、间距令牌、路由、状态管理和数据获取模式。

## 工作流程

### 从 Figma 选择开始

复制指向你想要实现的确切 Figma 框架、组件或变体的链接。Figma MCP 流程是基于链接的，因此链接需要指向你想要的确切节点，而不是附近的父框架。

### 提示 Codex 使用 Figma

Figma 应驱动第一次实现。让 Codex 在开始实现之前遵循 Figma MCP 流程。

在你的提示中应包含的内容：

1\. 首先运行 \`get\_design\_context\` 获取确切节点或框架。
2\. 如果响应太大或被截断，运行 \`get\_metadata\` 映射文件，然后仅对所需的节点重新运行 \`get\_design\_context\`。
3\. 对于正在实现的确切变体，运行 \`get\_screenshot\`。
4\. 只有在设计上下文和确切变体都可用后，下载所需的资产并开始实现。
5\. 将结果转化为代码库的约定：复用现有组件，尽可能用项目的系统替换原始实用类，并保持间距、层次结构和响应行为与设计一致。
6\. 如果 Figma 返回 localhost 图像或 SVG 源，则直接使用它。 当资产已在有效负载中时，不要创建占位符或添加新的图标包。

一旦第一次实现到位，Codex 将利用 Playwright 在真实浏览器中验证用户界面并调整任何剩余的视觉或交互不匹配。

## 技术栈

需要

默认选项

必要原因

需要

设计来源

默认选项

[Figma](https://www.figma.com/)

必要原因

一个具体的框架或组件选择使实现更切合实际。

| 需要 | 默认选项 | 必要原因 |
| --- | --- | --- |
| 设计来源 | [Figma](https://www.figma.com/) | 一个具体的框架或组件选择使实现更切合实际。 |

## 相关使用案例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**构建响应式前端设计**\\
\\
使用 Codex 将屏幕截图和设计简报转换为与代码库匹配的代码...\\
\\
前端 设计](https://developers.openai.com/codex/use-cases/frontend-designs) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**生成幻灯片演示**\\
\\
使用 Codex 更新现有演示或通过直接编辑幻灯片构建新演示...\\
\\
数据 集成](https://developers.openai.com/codex/use-cases/generate-slide-decks) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**进行细致的 UI 更改**\\
\\
使用 Codex 在现有应用中一次进行一小部分 UI 调整，在...\\
\\
前端 设计](https://developers.openai.com/codex/use-cases/make-granular-ui-changes)
