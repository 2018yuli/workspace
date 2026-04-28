---
source: https://developers.openai.com/codex/use-cases/agent-friendly-clis
title: "Create a CLI Codex can use | Codex use cases"
translatedTo: zh-CN
translatedAt: 2026-04-27T14:08:10.645Z
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

- [首页](https://developers.openai.com/codex/use-cases)
- [集合](https://developers.openai.com/codex/use-cases/collections)

[API 仪表盘](https://platform.openai.com/login)

Codex 用例

![](https://developers.openai.com/assets/OpenAI-black-wordmark.svg)

![Codex](https://developers.openai.com/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex 用例

# 创建 Codex 可用的 CLI

提供给 Codex 一个可组合的命令，用于 API、日志源、导出或团队脚本。

难度 **中等**

时间预期 **1 小时**

要求 Codex 创建一个可组合的 CLI，使其能够从任何文件夹运行，结合仓库脚本，使用来下载文件，并通过伴随技能进行记忆。

## 最佳适用场景

- 重复工作，Codex 需要搜索、读取、从相同服务安全地下载或写入，导出、地方档案或仓库脚本。
- 代理工具需要分页搜索、精准按 ID 读取、可预期的 JSON、已下载文件、本地索引或写入前草稿命令。

# 目录

[← 所有用例](https://developers.openai.com/codex/use-cases)

要求 Codex 创建一个可组合的 CLI，使其能够从任何文件夹运行，结合仓库脚本，使用来下载文件，并通过伴随技能进行记忆。

中等

1 小时

相关链接

[Codex 技能](https://developers.openai.com/codex/skills) [创建自定义技能](https://developers.openai.com/codex/skills/create-skill)

## 最佳适用场景

- 重复工作，Codex 需要搜索、读取、从相同服务安全地下载或写入，导出、地方档案或仓库脚本。
- 代理工具需要分页搜索、精准按 ID 读取、可预期的 JSON、已下载文件、本地索引或写入前草稿命令。

## 技能与插件

- [Cli Creator](https://github.com/openai/skills/tree/main/skills/.curated/cli-creator)

设计命令表面，构建 CLI，添加设置和身份验证检查，将命令安装到 PATH，并从另一个文件夹进行验证。

- [Skill Creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)

创建伴随技能，以教导后续 Codex 任务哪些 CLI 命令应该优先运行，哪些写操作需要批准。

| 技能 | 使用原因 |
| --- | --- |
| [Cli Creator](https://github.com/openai/skills/tree/main/skills/.curated/cli-creator) | 设计命令表面，构建 CLI，添加设置和身份验证检查，将命令安装到 PATH，并从另一个文件夹进行验证。 |
| [Skill Creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) | 创建伴随技能，以教导后续 Codex 任务哪些 CLI 命令应该优先运行，哪些写操作需要批准。 |

## 启动提示

使用 $cli-creator 创建一个可以使用的 CLI，并使用 $skill-creator 创建同一线程中的伴随技能。

要学习的来源：\[文档 URL、OpenAPI 规范、已编辑的 curl 命令、现有脚本路径、日志文件夹、CSV 或 JSON 导出、SQLite 数据库路径或粘贴的 --help 输出\]。

CLI 应支持的第一个任务：\[从构建 URL 下载失败的 CI 日志，搜索支持票并按 ID 读取一张，查询管理员 API，读取本地数据库，或从现有脚本运行一个步骤\]。

可选的写入任务：\[创建草稿评论，上传媒体，重试失败的任务，或者目前仅限只读\]。

命令名称：\[cli-name，或推荐一个\]。

在编码之前，向我展示建议的命令表面，只询问仅会阻碍构建的缺失细节。

[在 Codex 应用中打开](codex://new?prompt=Use+%24cli-creator+to+create+a+CLI+you+can+use%2C+and+use+%24skill-creator+to+create+the+companion+skill+in+this+same+thread.%0A%0ASource+to+learn+from%3A+%5Bdocs+URL%2C+OpenAPI+spec%2C+redacted+curl+command%2C+existing+script+path%2C+log+folder%2C+CSV+or+JSON+export%2C+SQLite+database+path%2C+or+pasted+--help+output%5D.%0A%0AFirst+job+the+CLI+should+support%3A+%5Bdownload+failed+CI+logs+from+a+build+URL%2C+search+support+tickets+and+read+one+by+ID%2C+query+an+admin+API%2C+read+a+local+database%2C+or+run+one+step+from+an+existing+script%5D.%0A%0AOptional+write+job%3A+%5Bcreate+a+draft+comment%2C+upload+media%2C+retry+a+failed+job%2C+or+read-only+for+now%5D.%0A%0ACommand+name%3A+%5Bcli-name%2C+or+recommend+one%5D.%0A%0ABefore+coding%2C+show+me+the+proposed+command+surface+and+ask+only+for+missing+details+that+would+block+the+build. "在 Codex 应用中打开")

使用 $cli-creator 创建一个可以使用的 CLI，并使用 $skill-creator 创建同一线程中的伴随技能。

要学习的来源：\[文档 URL、OpenAPI 规范、已编辑的 curl 命令、现有脚本路径、日志文件夹、CSV 或 JSON 导出、SQLite 数据库路径或粘贴的 --help 输出\]。

CLI 应支持的第一个任务：\[从构建 URL 下载失败的 CI 日志，搜索支持票并按 ID 读取一张，查询管理员 API，读取本地数据库，或从现有脚本运行一个步骤\]。

可选的写入任务：\[创建草稿评论，上传媒体，重试失败的任务，或者目前仅限只读\]。

命令名称：\[cli-name，或推荐一个\]。

在编码之前，向我展示建议的命令表面，只询问仅会阻碍构建的缺失细节。

## 引言

当 Codex 不断使用相同的 API、日志源、导出收件箱、本地数据库或团队脚本时，给这项工作一个可组合的接口：一个可以从任何文件夹运行的命令，检查、缩小，并与 `git`、`gh`、`rg`、测试和仓库脚本相结合。

添加一个伴随技能，记录 Codex 何时应使用 CLI、首先运行什么、如何保持输出简洁、下载的文件存放在哪里，以及哪些写命令需要批准。

在此工作流程中，`$cli-creator` 帮助 Codex 构建命令。`$skill-creator` 帮助 Codex 保存可重用技能，例如 `$ci-logs`，将来任务可以通过名称调用。

## 如何使用

1. [决定该任务是否需要 CLI](https://developers.openai.com/codex/use-cases/agent-friendly-clis#choose-what-the-cli-should-do)
2. [共享 Codex 应学习的来源](https://developers.openai.com/codex/use-cases/agent-friendly-clis#share-the-docs-files-or-commands)
3. [运行 `$cli-creator`](https://developers.openai.com/codex/use-cases/agent-friendly-clis#ask-codex-to-build-the-cli-and-skill)
4. [测试已安装的命令](https://developers.openai.com/codex/use-cases/agent-friendly-clis#verify-the-command-works-from-any-folder)
5. [稍后调用保存的技能](https://developers.openai.com/codex/use-cases/agent-friendly-clis#use-the-skill-later)

## 选择 CLI 应该做什么

从你希望 Codex 做的事情开始，而不是你希望它编写的技术。一个好的 CLI 将重复的读取、搜索、下载、导出、草稿、上传、轮询或安全写入转换为 Codex 可以从任何仓库运行的命令。

| 情况 | Codex 可以通过 CLI 做什么 |
| --- | --- |
| **CI 日志位于构建页面后面。** | 取一个构建 URL，将失败的作业日志下载到 `./logs`，并返回文件路径及简短片段。 |
| **支持票作为每周导出到达。** | 索引最新的 CSV 或 JSON 导出，按客户或短语搜索，并通过稳定 ID 读取一张票。 |
| **API 响应对上下文太大。** | 仅列出所需字段，通过 ID 读取完整对象，并将完整响应导出到文件。 |
| **Slack 导出有长线程。** | 使用 `--limit` 搜索，读取一条线程，并返回附近的上下文，而不是整个档案。 |
| **团队脚本运行四个不同的步骤。** | 将设置、发现、下载、草稿、上传、轮询和实时写入拆分为单独的命令。 |
| **插件找到记录，但 Codex 需要文件。** | 保留插件在线程中；使用 CLI 下载附件、追踪、报告、视频或日志包，并返回路径。 |

## 共享文档、文件或命令

Codex 需要一些具体的学习材料：文档或 OpenAPI、已编辑的 curl 命令、导出或数据库路径、日志文件夹或现有脚本。如果你希望 CLI 遵循熟悉的风格，请粘贴来自 `gh`、`kubectl` 或你团队自身工具的短 `--help` 输出。

如果命令需要身份验证，请告诉 Codex 环境变量名称、配置文件路径或它应该支持的登录流程。请自己在 shell 或配置文件中设置密钥。切勿在线程中粘贴密钥。请要求 Codex 在身份验证缺失时清晰地使 CLI 的设置检查失败。

## 要求 Codex 构建 CLI 和技能

使用此页面上的启动提示。填写 Codex 应学习的来源和 CLI 应支持的第一个任务。

在 Codex 编写代码之前，它应该展示建议的命令表面，只询问仅会阻碍构建的缺失细节。

## 验证命令在任何文件夹中均可工作

Codex 不应在 `cargo run`、`python path/to/script.py` 或未安装的包命令后停止。要求它从另一个仓库或临时文件夹测试已安装的命令，以后任务将以这种方式使用它。

**像未来的代理那样测试 CLI**

按照你将在未来任务中使用的方式测试 \[cli-name\]。

请提供证据表明：

\- command -v \[cli-name\] 在 CLI 源文件夹外成功运行
\- \[cli-name\] --help 解释主要命令
\- 设置/身份验证检查运行
\- 一个安全的发现、列表或搜索命令正常工作
\- 一个使用发现结果中的 ID 的精准读取命令正常工作
\- 任何大型日志、导出、追踪或负载写入文件并返回路径
\- 实时写入命令在我明确批准之前不会运行

然后读取伴随技能并告诉我在需要此 CLI 时应使用的最简短提示。

如果 Codex 返回一个巨大的 JSON 对象，请要求它缩小默认响应，并为完整的有效负载添加文件导出。如果它忘记了批准边界，请在我在另一个线程中使用它之前要求它更新伴随技能。

## 稍后使用技能

当你再次需要 CLI 时，调用技能而不是重复粘贴文档：

使用 $ci-logs 下载此构建 URL 的失败日志，并告诉我第一个失败的步骤。

使用 $support-export 搜索本周的退款投诉并读取三个最高价值的票。

使用 $admin-api 查找该用户的工作区，读取账单记录，并草拟一条安全的账户备注。

对于重复工作，先在正常线程中测试一次技能，然后要求 Codex 将该调用转变为自动化。

## 相关用例

[![](https://developers.openai.com/images/codex/codex-wallpaper-1.webp)\\
\\
**创建基于浏览器的游戏**\\
\\
使用 Codex 将游戏简报首先变为一个良好定义的计划，然后是一个真正的浏览器... \\
\\
工程 代码](https://developers.openai.com/codex/use-cases/browser-games) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**部署应用或网站**\\
\\
使用 Codex 与 Build Web Apps 和 Vercel 将一个仓库、屏幕截图、设计或粗糙应用... \\
\\
前端  集成](https://developers.openai.com/codex/use-cases/deploy-app-or-website) [![](https://developers.openai.com/images/codex/codex-wallpaper-2.webp)\\
\\
**重构你的代码库**\\
\\
使用 Codex 删除无效代码、解开大型文件、合并重复逻辑，并... \\
\\
工程 代码](https://developers.openai.com/codex/use-cases/refactor-your-codebase)
