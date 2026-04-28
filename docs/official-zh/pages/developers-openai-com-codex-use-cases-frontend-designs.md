---
source: https://developers.openai.com/codex/use-cases/frontend-designs
title: "Build responsive front-end designs | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:12:21.973Z
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

文档 用例

- [主页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 仪表板](https://platform.openai.com/login)

Codex 使用案例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 构建响应式前端设计

将截图和视觉参考转化为具有视觉检查的响应式 UI。

难度 **中级**

时间预期 **1小时**

使用 Codex 将截图和设计说明转换为符合代码库设计系统的代码，然后使用 Playwright 比较实现与不同屏幕尺寸的参考，直到看起来正确为止。

## 最适合

- 从头创建新的前端项目
- 从现有代码库中的截图实施已经设计好的屏幕或流程

# 内容

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 将截图和设计说明转换为符合代码库设计系统的代码，然后使用 Playwright 比较实现与不同屏幕尺寸的参考，直到看起来正确为止。

中级

1小时

相关链接

[Codex 技能](https://developers.openai.com/codex/skills)

## 最适合

- 从头创建新的前端项目
- 从现有代码库中的截图实施已经设计好的屏幕或流程

## 技能与插件

- [Playwright](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive)

在真实浏览器中打开应用以验证实现并迭代布局和行为。

| 技能 | 使用原因 |
| --- | --- |
| [Playwright](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive) | 在真实浏览器中打开应用以验证实现并迭代布局和行为。 |

## 启动提示

在当前项目中实现此 UI，使用我提供的截图和注释作为真实来源。

要求：
\- 重用现有设计系统组件和令牌。
\- 将截图转换为该代码库的实用程序和组件模式，而不是创造一个平行系统。
\- 密切匹配间距、布局、层级和响应行为。
\- 尊重代码库的路由、状态和数据获取模式。
\- 使页面在桌面和移动设备上都响应式。
\- 如果任何截图细节不明确，请选择最简单的实现，仍然符合整体方向，并简要记录假设。

验证：
\- 将完成的 UI 与提供的截图进行比较，检查外观和行为。
\- 使用 $playwright-interactive 检查 UI 是否与参考一致，并根据需要进行迭代，直到符合要求。

[在 Codex 应用中打开](codex://new?prompt=Implement+this+UI+in+the+current+project+using+the+screenshots+and+notes+I+provide+as+the+source+of+truth.%0A%0ARequirements%3A%0A-+Reuse+the+existing+design+system+components+and+tokens.%0A-+Translate+the+screenshots+into+this+repo%27s+utilities+and+component+patterns+instead+of+inventing+a+parallel+system.%0A-+Match+spacing%2C+layout%2C+hierarchy%2C+and+responsive+behavior+closely.%0A-+Respect+the+repo%27s+routing%2C+state%2C+and+data-fetch+patterns.%0A-+Make+the+page+responsive+on+desktop+and+mobile.%0A-+If+any+screenshot+detail+is+ambiguous%2C+choose+the+simplest+implementation+that+still+matches+the+overall+direction+and+note+the+assumption+briefly.%0A%0AValidation%3A%0A-+Compare+the+finished+UI+against+the+provided+screenshots+for+both+look+and+behavior.%0A-+Use+%24playwright-interactive+to+check+that+the+UI+matches+the+references+and+iterate+as+needed+until+it+does. "在 Codex 应用中打开")

在当前项目中实现此 UI，使用我提供的截图和注释作为真实来源。

要求：
\- 重用现有设计系统组件和令牌。
\- 将截图转换为该代码库的实用程序和组件模式，而不是创造一个平行系统。
\- 密切匹配间距、布局、层级和响应行为。
\- 尊重代码库的路由、状态和数据获取模式。
\- 使页面在桌面和移动设备上都响应式。
\- 如果任何截图细节不明确，请选择最简单的实现，仍然符合整体方向，并简要记录假设。

验证：
\- 将完成的 UI 与提供的截图进行比较，检查外观和行为。
\- 使用 $playwright-interactive 检查 UI 是否与参考一致，并根据需要进行迭代，直到符合要求。

## 介绍

当你有截图、简短的设计说明或一些灵感参考时，Codex 可以将这些转化为响应式 UI，而不忽视你项目中已建立的模式。

借助 Playwright 技能，Codex 可以在真实浏览器中打开应用，将实施与您提供的截图进行比较，针对不同屏幕尺寸进行布局或行为的迭代，直到结果更接近目标。

## 从参考开始

给 Codex 提供你所期望 UI 的最清晰参考。一张截图就可以足够用于某个特定任务，但当你包含多个状态（如桌面和移动布局、悬停或选中状态，以及任何重要的空或加载视图）时，交接会更好。

参考不需要是完美的设计交付物。它们只需要使预期的层级、间距和方向足够具体，以便 Codex 不会进行猜测。

## 具体说明

你越具体地描述预期的交互模式和想要的风格，最终结果就会越好。
如果从你的参考中看不出你想要什么，模型通常会默认高频模式和风格，因此 UI 可能看起来比较通用。
你提供的参考灵感越多，或是提供更具体的说明，期望得到的 UI 就会更突出。

## 准备设计系统

Codex 在目标代码库已经有清晰组件层时效果最佳。Codex 可以自动使用你现有的组件和设计系统，而不是从头开始重新创建它们。

如果你认为有必要（例如：如果你不是在使用标准栈），请明确告诉 Codex 哪些原始组件可以重用、你的令牌存放在哪里、以及代码库认为按钮、输入框、卡片、排版和图标的规范是什么。

如果你是从现有代码库开始，Codex 很可能会自行理解如何使用你的组件和设计系统，但如果从头开始，明确说明将是一个好主意。

请 Codex 将截图视为视觉目标，但将该目标转化为项目的实际实用程序、组件包装器、色彩系统、排版比例、间距令牌、路由、状态管理和数据获取模式。

## 利用 Playwright

Playwright 是一个很好的工具，可以帮助 Codex 在 UI 上进行迭代。借助该工具，Codex 可以在真实浏览器中打开应用，将实施与您提供的截图进行比较，进行布局或行为迭代。

它可以调整浏览器窗口的大小，以适应不同屏幕尺寸，并在不同断点检查布局。

确保你在 Codex 中启用了 Playwright 交互技能。有关更多详细信息，请参阅[技能文档](https://developers.openai.com/codex/skills)。

## 迭代

初次尝试应该已经接近截图的方向。对于复杂的布局、交互或动画繁重的 UI，预计会有几轮调整。

请 Codex 将实施与截图进行比较，而不仅仅是检查页面是否构建完成。当出现冲突时，Codex 应优先考虑代码库的设计系统令牌，仅进行必要的间距或大小调整，以保持设计的整体外观。

如果有额外的截图或简短的说明，可以帮助阐明从一张图像中看不出的状态，也可以使用它们。

### 建议的后续提示

\[当前实施图像\] \[参考图像\]

这看起来不对。请确保实现的内容与参考紧密匹配：

\[如有需要，请说明差异\]

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**将 Figma 设计转化为代码**\\
\\
使用 Codex 从 Figma 中提取设计上下文、资产和变体，将它们转换为代码... \\
\\
前端  设计](https://developers.openai.com/codex/use-cases/figma-designs-to-code) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**生成幻灯片**\\
\\
使用 Codex 更新现有演示文稿或通过直接编辑幻灯片构建新幻灯片... \\
\\
数据  集成](https://developers.openai.com/codex/use-cases/generate-slide-decks) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**进行细粒度 UI 更改**\\
\\
使用 Codex 在现有应用中逐一进行小的 UI 调整，在... \\
\\
前端  设计](https://developers.openai.com/codex/use-cases/make-granular-ui-changes)
