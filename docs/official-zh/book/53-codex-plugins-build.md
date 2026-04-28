# 第53章 构建插件

> 原始页面：[Build plugins – Codex | OpenAI Developers](https://developers.openai.com/codex/plugins/build)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。

## 严谨定义
严格地说，配置是运行时行为的参数化描述。

## 你读完应该抓住什么
- 此页面是为插件作者准备的。如果您想浏览、安装和使用 Codex 中的插件，请参见 插件。如果您仍在一个 仓库或个人工作流中迭代，请从本地技能开始。
- `使用 `$plugin-creator` 创建插件`：要快速设置，请使用内置的 `$plugin-creator` 技能。
- `构建您自己的精选插件列表`：市场是插件的 JSON 目录。`$plugin-creator` 可以为单个插件生成一个， 您可以继续向该市场添加。

## 分步理解
### 正文
先说直白版：
此页面是为插件作者准备的。如果您想浏览、安装和使用 Codex 中的插件，请参见 插件。如果您仍在一个 仓库或个人工作流中迭代，请从本地技能开始。当您想跨团队共享工作流、打包应用集成或 MCP 配置，或发布稳定包时，请构建插件。

把它理解成一个更严谨的过程：
1. 此页面是为插件作者准备的。如果您想浏览、安装和使用 Codex 中的插件，请参见 插件。如果您仍在一个 仓库或个人工作流中迭代，请从本地技能开始。当您想跨团队共享工作流、打包应用集成或 MCP 配置，或发布稳定包时，请构建插件。

### 使用 `$plugin-creator` 创建插件
先说直白版：
要快速设置，请使用内置的 `$plugin-creator` 技能。
它搭建了所需的 `.codex-plugin/plugin.json` 清单，并且还可以 生成本地市场条目以便测试。如果您已有插件文件夹，仍然可以使用 `$plugin-creator` 将其连接到本地 市场。

把它理解成一个更严谨的过程：
1. 要快速设置，请使用内置的 `$plugin-creator` 技能。
2. 它搭建了所需的 `.codex-plugin/plugin.json` 清单，并且还可以 生成本地市场条目以便测试。如果您已有插件文件夹，仍然可以使用 `$plugin-creator` 将其连接到本地 市场。

### 构建您自己的精选插件列表
先说直白版：
市场是插件的 JSON 目录。`$plugin-creator` 可以为单个插件生成一个， 您可以继续向该市场添加条目，以为仓库、团队或个人工作流构建自己的精选列表。
在 Codex 中，每个市场显示为插件目录中的可选择来源。使用 `$REPO_ROOT/.agents/plugins/marketplace.json` 作为仓库范围的列表，或使用 `~/.agents/plugins/marketplace.json` 作为个人列表。在 `plugins[]` 下为每个插件添加一个条目，指向插件文件夹的 `source.path` 设置为带有 `./` 前缀相对路径，并将 `interface.displayName` 设置为希望 Codex 在市场选择器中显示的标签。然后重启 Codex。之后，打开插件目录，选择您的市场，并浏览或安装该精选列表中的插件。
您不需要为每个插件单独创建市场。一个市场可以在您测试时公开单个插件，然后随着您添加更多插件而增长为更大的精选目录。

把它理解成一个更严谨的过程：
1. 市场是插件的 JSON 目录。`$plugin-creator` 可以为单个插件生成一个， 您可以继续向该市场添加条目，以为仓库、团队或个人工作流构建自己的精选列表。
2. 在 Codex 中，每个市场显示为插件目录中的可选择来源。使用 `$REPO_ROOT/.agents/plugins/marketplace.json` 作为仓库范围的列表，或使用 `~/.agents/plugins/marketplace.json` 作为个人列表。在 `plugins[]` 下为每个插件添加一个条目，指向插件文件夹的 `source.path` 设置为带有 `./` 前缀相对路径，并将 `interface.displayName` 设置为希望 Codex 在市场选择器中显示的标签。然后重启 Codex。之后，打开插件目录，选择您的市场，并浏览或安装该精选列表中的插件。
3. 您不需要为每个插件单独创建市场。一个市场可以在您测试时公开单个插件，然后随着您添加更多插件而增长为更大的精选目录。

### 从 CLI 添加市场
先说直白版：
当您希望 Codex 为您安装和跟踪市场来源而不是手动编辑 `config.toml` 时，使用 `codex plugin marketplace add`。
市场来源可以是 GitHub 简码（`owner/repo` 或 `owner/repo@ref`），HTTP 或 HTTPS Git URL，SSH Git URL，或本地市场根目录。使用 `--ref` 钉住 Git 引用，重复 `--sparse PATH` 以对 Git 支持的市场仓库使用稀疏检出。`--sparse` 仅对 Git 市场来源有效。
要刷新或删除已配置的市场：

把它理解成一个更严谨的过程：
1. 当您希望 Codex 为您安装和跟踪市场来源而不是手动编辑 `config.toml` 时，使用 `codex plugin marketplace add`。
2. 市场来源可以是 GitHub 简码（`owner/repo` 或 `owner/repo@ref`），HTTP 或 HTTPS Git URL，SSH Git URL，或本地市场根目录。使用 `--ref` 钉住 Git 引用，重复 `--sparse PATH` 以对 Git 支持的市场仓库使用稀疏检出。`--sparse` 仅对 Git 市场来源有效。
3. 要刷新或删除已配置的市场：

### 手动创建插件
先说直白版：
从打包一个技能的最小插件开始。
1. 创建一个插件文件夹并在 `.codex-plugin/plugin.json` 中放置清单。
`my-first-plugin/.codex-plugin/plugin.json`
使用稳定插件 `name` 采用 kebab-case 格式。Codex 将其用作插件 标识符和组件命名空间。

把它理解成一个更严谨的过程：
1. 从打包一个技能的最小插件开始。
2. 1. 创建一个插件文件夹并在 `.codex-plugin/plugin.json` 中放置清单。
3. `my-first-plugin/.codex-plugin/plugin.json`
4. 使用稳定插件 `name` 采用 kebab-case 格式。Codex 将其用作插件 标识符和组件命名空间。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
