---
source: https://developers.openai.com/codex/use-cases/macos-telemetry-logs
title: "Add Mac telemetry | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:14:43.848Z
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
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 控制台](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 添加 Mac 遥测

使用 Codex 对一个 Mac 功能进行 Logger 工具的分析，运行应用程序，并从统一日志中验证操作。

难度 **高级**

时间估计 **30 分钟**

使用 Codex 和 Build macOS Apps 插件，在窗口、侧边栏、命令或同步流程周围添加一些高信号 `Logger` 事件，然后运行应用程序，并证明从控制台或 `log stream` 中触发了正确的动作。

## 最适合

- 需要稳定窗口打开、侧边栏选择、菜单命令、菜单栏操作、同步里程碑或回退路径跟踪的 Mac 应用功能
- Codex 应该修补代码、重新运行应用程序、检查日志，并根据证据决定下一个修复而不是猜测的代理调试循环
- 想要一个紧凑的用户操作序列和应用程序生命周期事件，可以在多次运行中进行比较的本地应用会话收集循环

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

使用 Codex 和 Build macOS Apps 插件，在窗口、侧边栏、命令或同步流程周围添加一些高信号 `Logger` 事件，然后运行应用程序，并证明从控制台或 `log stream` 中触发了正确的动作。

高级

30 分钟

相关链接

[Build macOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) [代理技能](https://developers.openai.com/codex/skills)

## 最适合

- 需要稳定窗口打开、侧边栏选择、菜单命令、菜单栏操作、同步里程碑或回退路径跟踪的 Mac 应用功能
- Codex 应该修补代码、重新运行应用程序、检查日志，并根据证据决定下一个修复而不是猜测的代理调试循环
- 想要一个紧凑的用户操作序列和应用程序生命周期事件，可以在多次运行中进行比较的本地应用会话收集循环

## 技能与插件

- [Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)

使用 macOS 遥测和构建/运行技能添加结构化 `OSLog` 仪器，启动应用程序，执行用户界面路径，并验证从控制台或 `log stream` 输出的事件。

| 技能 | 理由 |
| --- | --- |
| [Build macOS Apps](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) | 使用 macOS 遥测和构建/运行技能添加结构化 `OSLog` 仪器，启动应用程序，执行用户界面路径，并验证从控制台或 `log stream` 输出的事件。 |

## 启动提示

使用 Build macOS Apps 插件，在 \[名称一个 Mac 功能或操作流程\] 周围添加轻量级统一日志，然后运行应用程序并从日志中验证这些事件按预期顺序触发。

约束：
\- 优先使用 `OSLog` 中的 `Logger`，而不是 `print`，为该特性创建清晰的子系统/类别对，以便于日志过滤。
\- 为每个重要的操作边界或状态转换记录简洁的一行：例如窗口打开、侧边栏选择更改、菜单命令调用、同步开始、同步结束或回退路径触发。
\- 保持永久的 `info` 日志稳定且高信号。仅在噪音较大的本地细节中使用 `debug`，并在完成之前移除或降级临时仪器。
\- 不要记录机密、身份验证令牌、个人数据或原始文档内容。如果必须记录标识符，请选择最安全的隐私注释并解释原因。
\- 构建并运行应用，自己执行功能路径，并使用控制台或聚焦的 `log stream` 谓词验证事件。
\- 如果流程较长、中断或手动重现更方便，请将过滤后的日志流保存到一个小的本地会话跟踪文件，让我在需要时手动执行应用程序，然后读取该文件并总结事件时间线。
\- 如果预期事件未出现，请将日志移近疑似控制路径，重新运行流程，并继续直到日志解释发生的事情。

交付：
\- 新的日志记录设置和您添加的确切事件
\- 您使用的控制台过滤器或 `log stream` 谓词
\- 关于日志现在可观察内容的简短前/后总结
\- 如果这是一个较长的捕获会话，则保存的跟踪文件和时间线摘要
\- 一到两个代表性的日志行，证明流程正确地被仪器化

[在 Codex 应用中打开](codex://new?prompt=Use+the+Build+macOS+Apps+plugin+to+add+lightweight+unified+logging+around+%5Bname+one+Mac+feature+or+action+flow%5D%2C+then+run+the+app+and+verify+from+logs+that+those+events+fire+in+the+expected+order.%0A%0AConstraints%3A%0A-+Prefer+%60Logger%60+from+%60OSLog%60%2C+not+%60print%60%2C+and+create+a+clear+subsystem%2Fcategory+pair+for+this+feature+so+the+logs+are+easy+to+filter.%0A-+Log+one+concise+line+for+each+important+action+boundary+or+state+transition%3A+for+example+window+opened%2C+sidebar+selection+changed%2C+menu+command+invoked%2C+sync+started%2C+sync+finished%2C+or+fallback+path+taken.%0A-+Keep+permanent+%60info%60+logs+stable+and+high+signal.+Use+%60debug%60+only+for+noisy+local+details%2C+and+remove+or+demote+temporary+instrumentation+before+finishing.%0A-+Do+not+log+secrets%2C+auth+tokens%2C+personal+data%2C+or+raw+document+contents.+If+an+identifier+must+be+logged%2C+choose+the+safest+privacy+annotation+and+explain+why.%0A-+Build+and+run+the+app%2C+exercise+the+feature+path+yourself%2C+and+verify+the+events+with+Console+or+a+focused+%60log+stream%60+predicate.%0A-+If+the+flow+is+long%2C+intermittent%2C+or+easier+to+reproduce+by+hand%2C+save+the+filtered+log+stream+to+a+small+local+session+trace+file%2C+let+me+manually+exercise+the+app+if+needed%2C+then+read+that+file+back+and+summarize+the+event+timeline.%0A-+If+an+expected+event+does+not+appear%2C+move+the+log+closer+to+the+suspected+control+path%2C+rerun+the+flow%2C+and+continue+until+the+logs+explain+what+happened.%0A%0ADeliver%3A%0A-+the+new+logger+setup+and+the+exact+events+you+added%0A-+the+Console+filter+or+%60log+stream%60+predicate+you+used%0A-+a+short+before%2Fafter+summary+of+what+the+logs+now+make+observable%0A-+the+saved+trace+file+and+timeline+summary+if+this+became+a+longer+capture+session%0A-+one+or+two+representative+log+lines+that+prove+the+flow+is+instrumented+correctly)

使用 Build macOS Apps 插件，在 \[名称一个 Mac 功能或操作流程\] 周围添加轻量级统一日志，然后运行应用程序并从日志中验证这些事件按预期顺序触发。

约束：
\- 优先使用 `OSLog` 中的 `Logger`，而不是 `print`，为该特性创建清晰的子系统/类别对，以便于日志过滤。
\- 为每个重要的操作边界或状态转换记录简洁的一行：例如窗口打开、侧边栏选择更改、菜单命令调用、同步开始、同步结束或回退路径触发。
\- 保持永久的 `info` 日志稳定且高信号。仅在噪音较大的本地细节中使用 `debug`，并在完成之前移除或降级临时仪器。
\- 不要记录机密、身份验证令牌、个人数据或原始文档内容。如果必须记录标识符，请选择最安全的隐私注释并解释原因。
\- 构建并运行应用，自己执行功能路径，并使用控制台或聚焦的 `log stream` 谓词验证事件。
\- 如果流程较长、中断或手动重现更方便，请将过滤后的日志流保存到一个小的本地会话跟踪文件，让我在需要时手动执行应用程序，然后读取该文件并总结事件时间线。
\- 如果预期事件未出现，请将日志移近疑似控制路径，重新运行流程，并继续直到日志解释发生的事情。

交付：
\- 新的日志记录设置和您添加的确切事件
\- 您使用的控制台过滤器或 `log stream` 谓词
\- 关于日志现在可观察内容的简短前/后总结
\- 如果这是一个较长的捕获会话，则保存的跟踪文件和时间线摘要
\- 一到两个代表性的日志行，证明流程正确地被仪器化

## 在调试模糊时添加一个 Logger

此用例适用于 Mac 应用流程，其中“发生了某事”在代码审查中过于模糊。请 Codex 在一个行为周围添加几个高信号的统一日志，运行应用程序，触发该行为，然后从控制台或 `log stream` 验证预期事件是否触发。

使用 [Build macOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) 实现该循环。它的 macOS 遥测技能是故意轻量级：使用 Apple 的 `Logger`，选择清晰的子系统/类别对，记录操作边界和状态转换，避免敏感有效载荷，并在本地构建/运行后验证事件，而不是假设仪器正确连接。

## 为什么遥测对代理工程至关重要

良好的日志为 Codex 提供了每次修补后的可重复反馈循环。代理可以运行应用程序，执行流程，检查过滤后的日志，并根据证据决定下一个代码更改，而不是要求您手动检查每个窗口、菜单操作或同步过渡。

这对三个代理循环尤为重要：

- **免提调试循环：** Codex 在可疑流中进行仪器，启动应用程序，点击侧边栏或触发命令，读取发出的日志序列，修补状态更新路径，并重新运行相同的流程，直到日志和用户界面行为一致。
- **应用会话收集循环：** Codex 为应用启动、窗口打开、侧边栏选择、导入开始、导入完成和导入失败添加一个事件，然后运行本地会话并总结结果时间线，以便缺失或顺序错误的过渡变得显而易见。
- **人驱动捕获循环：** Codex 启动启用了日志的应用程序，在您手动执行复杂流程时保持聚焦的日志流运行，然后在捕获的会话之后检查并根据该跟踪提出下一个补丁。

## 保持仪器小且易于过滤

请 Codex 为每个功能区域请求一个日志记录器，而不是每个状态变化都记录一个永久日志行。`Windowing`、`Commands`、`MenuBar`、`Sidebar`、`Sync` 或 `Import` 等功能类别使得在下一次调试过程中更容易过滤日志。

```
import OSLog

private let logger = Logger(
  subsystem: Bundle.main.bundleIdentifier ?? "SampleApp",
  category: "Sidebar"
)

@MainActor
func selectItem(_ item: SidebarItem) {
  logger.info("Selected sidebar item: \(item.id, privacy: .public)")
  selection = item.id
}
```

使用 `info` 来记录应长期保留的简洁操作和生命周期事件，使用 `debug` 来记录本地状态的噪声细节，这些可能在任务完成之前被删除或降级。仅在您测量时间跨度时添加标识，而不是默认添加。

## 请 Codex 证明日志中的事件

有用的部分不仅在于添加 `Logger` 调用。请 Codex 运行应用程序，触发仪器流，并提供确切的控制台过滤器或 `log stream` 谓词及一到两个代表性日志行。

```
log stream --style compact --predicate 'subsystem == "com.example.app" && category == "Sidebar"'
```

如果预期事件未出现，请要求 Codex 将日志移近疑似控制路径，重新运行相同的流程，并继续迭代，直到日志解释发生的事情。如果任务变成崩溃或回溯分析，请转向插件的构建/运行调试工作流程，并保持遥测集中在操作边界上。

## 为后续 Codex 运行保存会话跟踪

对于较长或间歇的 bug，请要求 Codex 将聚焦的日志流保存到一个小的本地跟踪文件，总结时间线，并将该文档留在工作空间中，以便后续 Codex 运行能够检查相同的证据，而不必从内存中重放整个会话。这使得在希望执行一个代理运行来收集跟踪，另一个运行则在补丁前后比较行为的情况下，使多次调试变得更容易。

这在人工需要驱动部分会话时也很有效。请 Codex 启动一个友好的调试循环，进行类记录，开始过滤捕获，让您手动重现问题，完成后再读取已保存的跟踪文件。

## 实用技巧

### 一次对一个功能进行仪器化

从一个侧边栏、窗口、命令或同步路径开始，以便日志序列保持易于检查。如果该路径变得可靠，Codex 可以将相同的模式扩展到相邻的流程。

### 让隐私成为提示的一部分

请 Codex 解释每个记录的标识符，并避免将机密、个人数据或原始内容写入统一日志。通常，一个小的事件词汇就足够用于本地调试。

### 在最终总结中保留示例输出

代表性的日志行使更改比“添加了遥测”更容易被信任。请 Codex 包含过滤谓词和简短的操作时间线，以便下一次代理运行可以重用相同的验证循环。

## 技术栈

需求

默认选项

必要性

需求

应用日志记录

默认选项

[OSLog Logger](https://developer.apple.com/documentation/os/logger)

必要性

结构化统一日志记录为 Codex 提供了一个狭窄、可过滤的反馈循环，而不将代码库变成一堵 `print` 语句的墙。

需求

代理工作流程

默认选项

[Build macOS Apps plugin](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)

必要性

该插件的遥测和构建/运行技能旨在协同工作：对一个流程进行仪器，启动应用程序，检查日志，并缩小事件集。

需求

运行时验证

默认选项

Console.app 和 `log stream --predicate ...`

必要性

具体的日志过滤器加上示例输出为代理提供了重复的移交，使新的仪器在多个运行之间易于验证。

| 需求 | 默认选项 | 需要的原因 |
| --- | --- | --- |
| 应用日志记录 | [OSLog Logger](https://developer.apple.com/documentation/os/logger) | 结构化统一日志记录为 Codex 提供了一个狭窄、可过滤的反馈循环，而不将代码库变成一堵 `print` 语句的墙。 |
| 代理工作流程 | [Build macOS Apps plugin](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps) | 该插件的遥测和构建/运行技能旨在协同工作：对一个流程进行仪器，启动应用程序，检查日志，并缩小事件集。 |
| 运行时验证 | Console.app 和 `log stream --predicate ...` | 具体的日志过滤器加上示例输出为代理提供了重复的移交，使新的仪器在多个运行之间易于验证。 |

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**构建 Mac 应用程序外壳**\\
\\
使用 Codex 和 Build macOS Apps 插件将一个应用创意变为桌面本地... \\
\\
macOS 代码](https://developers.openai.com/codex/use-cases/macos-sidebar-detail-inspector) [![](https://developers.openai.com/images/codex/codex-wallpaper-3.webp)\\
\\
**为 macOS 构建**\\
\\
使用 Codex 构建 macOS SwiftUI 应用程序，连接外壳优先的构建和运行循环，并添加... \\
\\
macOS 代码](https://developers.openai.com/codex/use-cases/native-macos-apps) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**在 iOS 模拟器中调试**\\
\\
使用 Codex 发现正确的 Xcode 方案和模拟器，启动应用程序，检查界面... \\
\\
iOS 代码](https://developers.openai.com/codex/use-cases/ios-simulator-bug-debugging)
