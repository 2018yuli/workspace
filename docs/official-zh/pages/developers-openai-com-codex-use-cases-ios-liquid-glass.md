---
source: https://developers.openai.com/codex/use-cases/ios-liquid-glass
title: "Adopt liquid glass | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:13:44.795Z
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

- [主页](https://developers.openai.com/codex/use-cases)
- [收藏](https://developers.openai.com/codex/use-cases/collections)

[API 控制台](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 采用液态玻璃

使用 Codex 将现有的 SwiftUI 应用迁移到带有 iOS 26 API 和 Xcode 26 的液态玻璃。

难度 **高级**

时间范围 **1 小时**

使用 Codex 和 Build iOS Apps 插件审核现有的 iPhone 和 iPad UI，将自定义模糊或材料堆栈替换为本地液态玻璃，并通过 iOS 26 可用性检查和模拟器驱动的验证来确保迁移安全。

## 最适合

- 需要实际 iOS 26 液态玻璃迁移计划的现有 SwiftUI 应用，而不是模糊的重设计简报
- 希望 Codex 审核自定义卡片、表单、选项卡栏、工具栏和操作按钮的团队，然后逐步实施迁移
- 仍然支持较旧 iOS 版本的应用，需要 \`#available(iOS 26, \*)\` 回退，而不是单向视觉重写

# 内容

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 和 Build iOS Apps 插件审核现有的 iPhone 和 iPad UI，将自定义模糊或材料堆栈替换为本地液态玻璃，并通过 iOS 26 可用性检查和模拟器驱动的验证来确保迁移安全。

高级

1 小时

相关链接

[Codex 插件](https://developers.openai.com/codex/plugins) [代理技能](https://developers.openai.com/codex/skills)

## 最适合

- 需要实际 iOS 26 液态玻璃迁移计划的现有 SwiftUI 应用，而不是模糊的重设计简报
- 希望 Codex 审核自定义卡片、表单、选项卡栏、工具栏和操作按钮的团队，然后逐步实施迁移
- 仍然支持较旧 iOS 版本的应用，需要 \`#available(iOS 26, \*)\` 回退，而不是单向视觉重写

## 技能与插件

- [Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)

利用 SwiftUI 液态玻璃、SwiftUI UI 模式和模拟器调试技能来现代化 iOS 屏幕，采用本地玻璃效果，并在 iOS 26 模拟器上验证结果。

| 技能 | 使用原因 |
| --- | --- |
| [Build iOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) | 利用 SwiftUI 液态玻璃、SwiftUI UI 模式和模拟器调试技能来现代化 iOS 屏幕，采用本地玻璃效果，并在 iOS 26 模拟器上验证结果。 |

## 启动提示

使用 Build iOS Apps 插件及其 SwiftUI 液态玻璃技能，将该应用中一个高流量流程迁移到液态玻璃。

约束：
\- 将其视为 iOS 26 + Xcode 26 的迁移，但为较早的 deployment targets 保留非玻璃回退，使用 \`#available(iOS 26, \*)\`。
\- 首先审核流程。指出应该成为本地液态玻璃的自定义背景、模糊堆栈、芯片、按钮、表单和工具栏，并指出应该保持简单内容的表面。
\- 优先使用系统控件和本地 API，如 \`glassEffect\`、\`GlassEffectContainer\`、\`glassEffectID\`、\`.buttonStyle(.glass)\` 和 \`.buttonStyle(.glassProminent)\`，而不是自定义模糊。仅在真正的变形过渡改善流程时，使用 \`glassEffectID\` 和 \`@Namespace\`。
\- 在布局和视觉修饰符之后应用 \`glassEffect\`，保持形状一致，仅在实际响应触摸的控件上使用 \`.interactive()\`。
\- 使用 XcodeBuildMCP 在 iOS 26 模拟器上构建和运行，捕获迁移流程的屏幕截图，并明确提及使用的确切方案、模拟器和检查。

交付：
\- 流程的简要迁移计划
\- 实施的液态玻璃切片
\- iOS 26 设备的回退行为
\- 模拟器验证步骤和您使用的屏幕截图

[在 Codex 应用中打开](codex://new?prompt=Use+the+Build+iOS+Apps+plugin+and+its+SwiftUI+Liquid+Glass+skill+to+migrate+one+high-traffic+flow+in+this+app+to+Liquid+Glass.%0A%0AConstraints%3A%0A-+Treat+this+as+an+iOS+26+%2B+Xcode+26+migration%2C+but+preserve+a+non-glass+fallback+for+earlier+deployment+targets+with+%60%23available%28iOS+26%2C+*%29%60.%0A-+Audit+the+flow+first.+Call+out+custom+backgrounds%2C+blur+stacks%2C+chips%2C+buttons%2C+sheets%2C+and+toolbars+that+should+become+native+Liquid+Glass+and+call+out+surfaces+that+should+stay+plain+content.%0A-+Prefer+system+controls+and+native+APIs+like+%60glassEffect%60%2C+%60GlassEffectContainer%60%2C+%60glassEffectID%60%2C+%60.buttonStyle%28.glass%29%60%2C+and+%60.buttonStyle%28.glassProminent%29%60+over+custom+blurs.+Use+%60glassEffectID%60+with+%60%40Namespace%60+only+when+a+real+morphing+transition+improves+the+flow.%0A-+Apply+%60glassEffect%60+after+layout+and+visual+modifiers%2C+keep+shapes+consistent%2C+and+use+%60.interactive%28%29%60+only+on+controls+that+actually+respond+to+touch.%0A-+Use+XcodeBuildMCP+to+build+and+run+on+an+iOS+26+simulator%2C+capture+screenshots+for+the+migrated+flow%2C+and+mention+exactly+which+scheme%2C+simulator%2C+and+checks+you+used.%0A%0ADeliver%3A%0A-+a+concise+migration+plan+for+the+flow%0A-+the+implemented+Liquid+Glass+slice%0A-+the+fallback+behavior+for+pre-iOS+26+devices%0A-+the+simulator+validation+steps+and+screenshots+you+used "在 Codex 应用中打开")

使用 Build iOS Apps 插件及其 SwiftUI 液态玻璃技能，将该应用中一个高流量流程迁移到液态玻璃。

约束：
\- 将其视为 iOS 26 + Xcode 26 的迁移，但为较早的 deployment targets 保留非玻璃回退，使用 \`#available(iOS 26, \*)\`。
\- 首先审核流程。指出应该成为本地液态玻璃的自定义背景、模糊堆栈、芯片、按钮、表单和工具栏，并指出应该保持简单内容的表面。
\- 优先使用系统控件和本地 API，如 \`glassEffect\`、\`GlassEffectContainer\`、\`glassEffectID\`、\`.buttonStyle(.glass)\` 和 \`.buttonStyle(.glassProminent)\`，而不是自定义模糊。仅在真正的变形过渡改善流程时，使用 \`glassEffectID\` 和 \`@Namespace\`。
\- 在布局和视觉修饰符之后应用 \`glassEffect\`，保持形状一致，仅在实际响应触摸的控件上使用 \`.interactive()\`。
\- 使用 XcodeBuildMCP 在 iOS 26 模拟器上构建和运行，捕获迁移流程的屏幕截图，并明确提及使用的确切方案、模拟器和检查。

交付：
\- 流程的简要迁移计划
\- 实施的液态玻璃切片
\- iOS 26 设备的回退行为
\- 模拟器验证步骤和您使用的屏幕截图

## 从 iOS 26 基线开始

首先将液态玻璃视为 iOS 26 与 Xcode 26 的迁移项目。使用 iOS 26 SDK 重建应用，检查从标准 SwiftUI 控件自动获得的内容，然后再让 Codex 重新设计仍然看起来平坦、沉重或与系统界面不协调的自定义部分。

如果应用仍然支持较早的 iOS 版本，请明确说明该约束。Build iOS Apps 插件中的 SwiftUI 液态玻璃技能应使用 \`#available(iOS 26, *)\` 对新的仅玻璃 API 进行限制，并保持一个仍符合旧设备阅读的回退路径。

## 利用 iOS 插件

在希望 Codex 将 SwiftUI UI 更改与模拟器支持的验证相结合时，使用 [Build iOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)。对于液态玻璃工作，合理的步骤是请 Codex 审核一个流程，迁移一小组表面，在 iOS 26 模拟器上启动结果，并在扩大范围之前捕获屏幕截图。

该插件包含一个带有简单默认设置的 SwiftUI 液态玻璃技能，值得加入您的提示：

- 优先使用本地 \`glassEffect\`、\`GlassEffectContainer\`、玻璃按钮样式和 \`glassEffectID\` 过渡，而不是自定义模糊视图。
- 在布局和视觉修饰符之后应用 \`.glassEffect(...)`，以便材料包裹您真正想要的最终形状。
- 当多个表面一起出现时，将相关玻璃元素包裹在 \`GlassEffectContainer\` 中。
- 仅在按钮、芯片和实际上响应触摸的控件上使用 \`.interactive()`。
- 在整个功能中保持角形、着色和间距一致，而不是混合单个玻璃处理。
- 为预 iOS 26 目标保留非玻璃回退。

要了解有关安装插件和技能的更多信息，请参阅我们的 [插件](https://developers.openai.com/codex/plugins) 和 [技能](https://developers.openai.com/codex/skills) 文档。

## 观看 WWDC 会议

这些 WWDC25 会话是您在要求 Codex 重新构建真实生产流程之前的良好参考集：

- [认识液态玻璃](https://developer.apple.com/videos/play/wwdc2025/219/)
- [了解新设计系统](https://developer.apple.com/videos/play/wwdc2025/356/)
- [用新设计构建 SwiftUI 应用](https://developer.apple.com/videos/play/wwdc2025/323/)
- [用新设计构建 UIKit 应用](https://developer.apple.com/videos/play/wwdc2025/284/)
- [SwiftUI 有哪些新变化](https://developer.apple.com/videos/play/wwdc2025/256/)

## 提示迁移计划，然后一个切片

液态玻璃迁移时，当 Codex 将“玻璃应该出现在哪里？”与“现在编写所有代码”分开时，效果更好。先请求快速审核，然后让代理实现一个自包含的切片，并进行模拟器验证。

## 实用技巧

### 不要让所有内容都成为玻璃

液态玻璃应该在内容上方创建清晰的控制层，而不是将每个卡片都变成发光面板。请 Codex 删除与系统材料冲突的装饰背景，在可读性最重要的地方保留简单内容，并将着色保留用于语义强调或主要操作。

### 从一个高流量流程开始

选项卡根、详细屏幕、表单、搜索表面或入职流程通常是比全应用程序范围更好的第一个迁移目标。这使得审查更简单，并明确哪些液态玻璃决策应该成为可重用组件模式。

### 有意识地审查回退行为

如果您的部署目标低于 iOS 26，请要求 Codex 显示与液态玻璃版本的回退实现。该审查步骤可以捕捉意外的 API 可用性回归，避免发货仅在最新模拟器上有效的迁移。

## 技术栈

需求

默认选项

使用原因

需求

液态玻璃 UI API

默认选项

[SwiftUI](https://developer.apple.com/xcode/swiftui/) 与 \`glassEffect\`、\`GlassEffectContainer\` 和玻璃按钮样式

使用原因

这些是技能首先应利用的本地 API，因此 Codex 删除自定义模糊层，而不是重新发明材料系统。

需求

平台基线

默认选项

iOS 26 和 Xcode 26

使用原因

液态玻璃随 iOS 26 SDK 到来。Codex 应该使用 Xcode 26 进行编译，并为早期 OS 支持添加明确的回退。

需求

模拟器验证

默认选项

[XcodeBuildMCP](https://www.xcodebuildmcp.com/)

使用原因

在视觉迁移中，构建、启动、屏幕截图和日志检查非常重要，特别是在审查多个状态和设备大小时。

| 需求 | 默认选项 | 使用原因 |
| --- | --- | --- |
| 液态玻璃 UI API | [SwiftUI](https://developer.apple.com/xcode/swiftui/) 与 \`glassEffect\`、\`GlassEffectContainer\` 和玻璃按钮样式 | 这些是技能首先应利用的本地 API，因此 Codex 删除自定义模糊层，而不是重新发明材料系统。 |
| 平台基线 | iOS 26 和 Xcode 26 | 液态玻璃随 iOS 26 SDK 到来。Codex 应该使用 Xcode 26 进行编译，并为早期 OS 支持添加明确的回退。 |
| 模拟器验证 | [XcodeBuildMCP](https://www.xcodebuildmcp.com/) | 在视觉迁移中，构建、启动、屏幕截图和日志检查非常重要，特别是在审查多个状态和设备大小时。 |

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**添加 iOS 应用意图**\\
\\
使用 Codex 和 Build iOS Apps 插件识别您的应用应有的操作和实体... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-app-intents) [![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**构建 Mac 应用外壳**\\
\\
使用 Codex 和 Build macOS Apps 插件将应用创意转变为桌面本地... \\
\\
macOS 代码](https://developers.openai.com/codex/use-cases/macos-sidebar-detail-inspector) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**为 iOS 构建**\\
\\
使用 Codex 骨架 iOS SwiftUI 项目，通过 \`xcodebuild\` 保持构建循环 CLI 优先... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/native-ios-apps)
