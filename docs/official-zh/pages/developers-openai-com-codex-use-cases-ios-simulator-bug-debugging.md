---
source: https://developers.openai.com/codex/use-cases/ios-simulator-bug-debugging
title: "Debug in iOS simulator | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:15:21.439Z
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

[API 仪表板](https://platform.openai.com/login)

Codex 使用案例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 使用案例

# 在 iOS 模拟器中调试

使用 Codex 和 XcodeBuildMCP 驱动您的应用程序在 iOS 模拟器中，捕获证据，并进行迭代以实现修复。

难度 **高级**

时间跨度 **1小时**

使用 Codex 发现正确的 Xcode 方案和模拟器，启动应用程序，检查 UI 树，点击、输入、滑动，捕获屏幕截图和日志，必要时附加 LLDB，并将模糊的错误报告转变为小的经过验证的修复。

## 最佳适用

- 仅在模拟器中经过特定的点击、滚动或表单输入路径后显示的 UI 错误
- 崩溃、挂起或导航失效的情况，其中 Codex 需要在编辑代码之前获取日志、屏幕截图、视图层次状态和调试器回溯
- 希望 Codex 拥有再现-修复-验证循环的团队，而不是要求人类手动点击每个状态

# 目录

[← 所有使用案例](https://developers.openai.com/codex/use-cases)

使用 Codex 发现正确的 Xcode 方案和模拟器，启动应用程序，检查 UI 树，点击、输入、滑动，捕获屏幕截图和日志，必要时附加 LLDB，并将模糊的错误报告转变为小的经过验证的修复。

高级

1小时

相关链接

[构建 iOS 应用插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) [模型上下文协议](https://developers.openai.com/codex/mcp) [代理技能](https://developers.openai.com/codex/skills)

## 最佳适用

- 仅在模拟器中经过特定的点击、滚动或表单输入路径后显示的 UI 错误
- 崩溃、挂起或导航失效的情况，其中 Codex 需要在编辑代码之前获取日志、屏幕截图、视图层次状态和调试器回溯
- 希望 Codex 拥有再现-修复-验证循环的团队，而不是要求人类手动点击每个状态

## 技能与插件

- [构建 iOS 应用](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)

使用 iOS 调试代理在模拟器上与 XcodeBuildMCP 一起构建、启动、检查并驱动应用程序，然后在 Codex 确定错误的同时捕获日志、屏幕截图和堆栈跟踪。


| 技能 | 使用原因 |
| --- | --- |
| [构建 iOS 应用](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) | 使用 iOS 调试代理在模拟器上与 XcodeBuildMCP 一起构建、启动、检查并驱动应用程序，然后在 Codex 确定错误的同时捕获日志、屏幕截图和堆栈跟踪。 |

## 开始提示

使用构建 iOS 应用插件和 XcodeBuildMCP 直接在模拟器中重现此错误，诊断根本原因，并实施小的修复。

错误报告：
\[描述预期行为、实际错误以及任何已知的屏幕或帐户设置。\]

约束：
\- 首先检查是否已选择项目、方案和模拟器。如果没有，发现正确的 Xcode 项目或工作空间，选择应用方案，选择模拟器，并将该设置用于整个会话。
\- 在模拟器中构建并启动应用程序，然后确认在您开始与它互动之前，通过 UI 快照或屏幕截图确认可见的正确屏幕。
\- 通过在模拟器中点击、输入、滚动和滑动来驱动确切的重现路径。更倾向于使用无障碍标签或 ID 而不是原始坐标，并在布局更改时在下一步之前重新查看 UI 层次结构。
\- 在调试时捕获证据：用于视觉状态的屏幕截图、失败相关的模拟器日志，以及如果错误看起来像崩溃或挂起，使用 LLDB 堆栈帧或变量。
\- 如果模拟器尚未启动，请启动一个并告诉我您选择了哪个设备和操作系统。如果需要凭据或特殊装置，请暂停并仅询问缺失的输入。
\- 进行尽可能小的代码更改以解决该错误，然后重新运行模拟器流程，并告诉我您验证修复的具体方法。

交付：
\- Codex 执行的重现步骤
\- 解释错误的关键屏幕截图、日志或堆栈详情
\- 代码修复及其工作原理
\- 最终验证所用的模拟器和方案

[在 Codex 应用中打开](codex://new?prompt=Use+the+Build+iOS+Apps+plugin+and+XcodeBuildMCP+to+reproduce+this+bug+directly+in+Simulator%2C+diagnose+the+root+cause%2C+and+implement+a+small+fix.%0A%0ABug+report%3A%0A%5BDescribe+the+expected+behavior%2C+the+actual+bug%2C+and+any+known+screen+or+account+setup.%5D%0A%0AConstraints%3A%0A-+First+check+whether+a+project%2C+scheme%2C+and+simulator+are+already+selected.+If+not%2C+discover+the+right+Xcode+project+or+workspace%2C+pick+the+app+scheme%2C+choose+a+simulator%2C+and+reuse+that+setup+for+the+rest+of+the+session.%0A-+Build+and+launch+the+app+in+Simulator%2C+then+confirm+the+right+screen+is+visible+with+a+UI+snapshot+or+screenshot+before+you+start+interacting+with+it.%0A-+Drive+the+exact+reproduction+path+yourself+by+tapping%2C+typing%2C+scrolling%2C+and+swiping+in+the+simulator.+Prefer+accessibility+labels+or+IDs+over+raw+coordinates%2C+and+re-read+the+UI+hierarchy+before+the+next+action+when+the+layout+changes.%0A-+Capture+evidence+while+you+debug%3A+screenshots+for+visual+state%2C+simulator+logs+around+the+failure%2C+and+LLDB+stack+frames+or+variables+if+the+bug+looks+like+a+crash+or+hang.%0A-+If+the+simulator+is+not+already+booted%2C+boot+one+and+tell+me+which+device+and+OS+you+chose.+If+credentials+or+a+special+fixture+are+required%2C+pause+and+ask+only+for+that+missing+input.%0A-+Make+the+smallest+code+change+that+addresses+the+bug%2C+then+rerun+the+simulator+flow+and+tell+me+exactly+how+you+verified+the+fix.%0A%0ADeliver%3A%0A-+the+reproduction+steps+Codex+executed%0A-+the+key+screenshots%2C+logs%2C+or+stack+details+that+explained+the+bug%0A-+the+code+fix+and+why+it+works%0A-+the+simulator+and+scheme+used+for+final+verification "在 Codex 应用中打开")

使用构建 iOS 应用插件和 XcodeBuildMCP 直接在模拟器中重现此错误，诊断根本原因，并实施小的修复。

错误报告：
\[描述预期行为、实际错误以及任何已知的屏幕或帐户设置。\]

约束：
\- 首先检查是否已选择项目、方案和模拟器。如果没有，发现正确的 Xcode 项目或工作空间，选择应用方案，选择模拟器，并将该设置用于整个会话。
\- 在模拟器中构建并启动应用程序，然后确认在您开始与它互动之前，通过 UI 快照或屏幕截图确认可见的正确屏幕。
\- 通过在模拟器中点击、输入、滚动和滑动来驱动确切的重现路径。更倾向于使用无障碍标签或 ID 而不是原始坐标，并在布局更改时在下一步之前重新查看 UI 层次结构。
\- 在调试时捕获证据：用于视觉状态的屏幕截图、失败相关的模拟器日志，以及如果错误看起来像崩溃或挂起，使用 LLDB 堆栈帧或变量。
\- 如果模拟器尚未启动，请启动一个并告诉我您选择了哪个设备和操作系统。如果需要凭据或特殊装置，请暂停并仅询问缺失的输入。
\- 进行尽可能小的代码更改以解决该错误，然后重新运行模拟器流程，并告诉我您验证修复的具体方法。

交付：
\- Codex 执行的重现步骤
\- 解释错误的关键屏幕截图、日志或堆栈详情
\- 代码修复及其工作原理
\- 最终验证所用的模拟器和方案

## 让 Codex 拥有整个模拟器循环

这个用例在 Codex 拥有完整循环时效果最佳：选择正确的应用目标，启动应用程序在模拟器中，检查当前屏幕，执行重现步骤，收集日志和截图，必要时检查堆栈跟踪，修补代码，并重新运行相同路径以证明错误不存在。

当您希望该循环保持自主时，请使用 [构建 iOS 应用插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)。其 iOS 调试工作流围绕着 XcodeBuildMCP 构建，这意味着 Codex 可以与已启动的模拟器交互，并收集人类通常手动收集的相同证据。

当 XcodeBuildMCP 配置了模拟器自动化、UI 自动化、调试和日志记录工作流时，Codex 可以拥有完整的再现-调试-验证循环。如果 Codex 还没有选择项目、方案和模拟器，请要求它先发现这些，然后在整个会话中重复使用该设置。

## 利用 XcodeBuildMCP 的能力

这些是提示 Codex 使用的实用能力组：

- 项目和模拟器发现：检查 Codex 是否已经知道使用哪个应用目标和模拟器，发现 Xcode 项目或工作区，枚举方案，查找或启动模拟器，并保持该设置稳定以用于将来的构建/运行步骤。
- 构建和启动控制：构建活动应用目标，安装和启动模拟器构建，当需要时重新启动以捕获日志，并在 Codex 需要检查应用特定运行时日志时解决应用包 ID。
- UI 检查和交互：读取正在屏幕上的无障碍层次结构，拍摄屏幕截图，点击控件，输入字段，滚动列表，执行边缘滑动或其他模拟器手势。
- 日志和调试器状态：流式传输模拟器日志，将 LLDB 附加到正在运行的应用程序，设置断点，检查堆栈帧和局部变量，并在崩溃或挂起需要更深入检查时运行调试器命令。

关键习惯是在 Codex 点击之前要求它检查视图树。XcodeBuildMCP 暴露了无障碍层次结构以及坐标，因此 Codex 可以优先选择稳定的标签或元素 ID 而不是猜测原始屏幕位置。

## 将模糊的错误变成可重现的脚本

当您的提示给出一个具体的错误和一个预期的结果，然后让 Codex 驱动应用程序并自主收集证据时，iOS 调试技能最为有效。如果需要登录、深度链接或测试装置，请说一次，并在缺少的输入阻止进度时要求 Codex 暂停。

## 实用提示

### 请求证据，而不仅仅是修复

请求 Codex 用于解释错误的确切模拟器、方案、屏幕截图、日志片段和堆栈详情。这使最终补丁比“我认为这应该修复它”更容易审查。

### 优先考虑无障碍标签而不是坐标

如果 Codex 不得不通过坐标点击，因为控件没有稳定的标签或无障碍标识符，请要求它指出这一点。通常，这表明错误修复应包括小的 UI 可测试性改进。

### 每次运行一个错误

由模拟器驱动的调试循环是强大的，但当一个提示针对一个失败模式时，信任起来仍然更容易。在扩展到相邻问题之前，请要求 Codex 完成一个再现-修复-验证循环。

## 技术栈

需求

默认选项

为什么需要

需求

模拟器自动化

默认选项

[XcodeBuildMCP](https://www.xcodebuildmcp.com/)

为什么需要

当前工具表面涵盖模拟器设置、构建和启动、UI 快照、点击、输入、手势、屏幕截图、日志捕获和调试器附加。

需求

代理工作流

默认选项

[构建 iOS 应用插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)

为什么需要

该插件的 iOS 调试代理为 Codex 提供了一个清晰的模拟器优先循环，用于再现错误、收集证据和在每次更改后验证修复。

需求

应用程序可观察性

默认选项

`Logger`、`OSLog`、LLDB 和模拟器屏幕截图

为什么需要

Codex 可以使用日志和调试器状态来解释什么出现了问题，然后保存屏幕截图以证明修复前后的确切 UI 状态。

| 需求 | 默认选项 | 为什么需要 |
| --- | --- | --- |
| 模拟器自动化 | [XcodeBuildMCP](https://www.xcodebuildmcp.com/) | 当前工具表面涵盖模拟器设置、构建和启动、UI 快照、点击、输入、手势、屏幕截图、日志捕获和调试器附加。 |
| 代理工作流 | [构建 iOS 应用插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) | 该插件的 iOS 调试代理为 Codex 提供了一个清晰的模拟器优先循环，用于再现错误、收集证据和在每次更改后验证修复。 |
| 应用程序可观察性 | `Logger`、`OSLog`、LLDB 和模拟器屏幕截图 | Codex 可以使用日志和调试器状态来解释什么出现了问题，然后保存屏幕截图以证明修复前后的确切 UI 状态。 |

## 相关使用案例

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**添加 iOS 应用意图**\\
\\
使用 Codex 和构建 iOS 应用插件来识别您的应用程序应有的动作和实体... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-app-intents) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**采用液态玻璃**\\
\\
使用 Codex 和构建 iOS 应用插件来审核现有的 iPhone 和 iPad UI，替换自定义... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-liquid-glass) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**为 iOS 构建**\\
\\
使用 Codex 来构建 iOS SwiftUI 项目，使构建循环以 CLI 为主，使用 \`xcodebuild\`... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/native-ios-apps)
