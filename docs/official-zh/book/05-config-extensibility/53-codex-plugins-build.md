# 第53章 构建插件

> 原始页面：[Build plugins – Codex | OpenAI Developers](https://developers.openai.com/codex/plugins/build)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 数学类比
配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。

## 严谨定义
严格地说，配置是运行时行为的参数化描述。

## 本章先抓重点
- 此页面是为插件作者准备的。如果您想浏览、安装和使用 Codex 中的插件，请参见 插件。如果您仍在一个 仓库或个人工作流中迭代，请从本地技能开始。当您想跨团队共享工作流、打包应用集成或 MCP 配置，…
- `使用 `$plugin-creator` 创建插件`：要快速设置，请使用内置的 `$plugin-creator` 技能。
- `构建您自己的精选插件列表`：市场是插件的 JSON 目录。`$plugin-creator` 可以为单个插件生成一个， 您可以继续向该市场添加条目，以为仓库、团队或个人工作流构建自己的精选列表。

## 正文整理
### 正文
此页面是为插件作者准备的。如果您想浏览、安装和使用 Codex 中的插件，请参见 插件。如果您仍在一个 仓库或个人工作流中迭代，请从本地技能开始。当您想跨团队共享工作流、打包应用集成或 MCP 配置，或发布稳定包时，请构建插件。（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）

### 使用 `$plugin-creator` 创建插件
要快速设置，请使用内置的 `$plugin-creator` 技能。（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）

继续往下看，这一节还强调了两件事：
- 它搭建了所需的 `.codex-plugin/plugin.json` 清单，并且还可以 生成本地市场条目以便测试。如果您已有插件文件夹，仍然可以使用 `$plugin-creator` 将其连接到本地 市场。

### 构建您自己的精选插件列表
市场是插件的 JSON 目录。`$plugin-creator` 可以为单个插件生成一个， 您可以继续向该市场添加条目，以为仓库、团队或个人工作流构建自己的精选列表。

继续往下看，这一节还强调了两件事：
- 在 Codex 中，每个市场显示为插件目录中的可选择来源。使用 `$REPO_ROOT/.agents/plugins/marketplace.json` 作为仓库范围的列表，或使用 `~/.agents/plugins/marketplace.json` 作为个人列表。在 `plugins[]` 下为每个插件添加一个条目，指向插件文件夹的 `source.…（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）
- 您不需要为每个插件单独创建市场。一个市场可以在您测试时公开单个插件，然后随着您添加更多插件而增长为更大的精选目录。

### 从 CLI 添加市场
当您希望 Codex 为您安装和跟踪市场来源而不是手动编辑 `config.toml` 时，使用 `codex plugin marketplace add`。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

继续往下看，这一节还强调了两件事：
- 市场来源可以是 GitHub 简码（`owner/repo` 或 `owner/repo@ref`），HTTP 或 HTTPS Git URL，SSH Git URL，或本地市场根目录。使用 `--ref` 钉住 Git 引用，重复 `--sparse PATH` 以对 Git 支持的市场仓库使用稀疏检出。`--sparse` 仅对 Git 市场来源有效。（实现：[git_info](/config/workspace/codex/codex-rs/core/src/git_info.rs:1)、[undo task](/config/workspace/codex/codex-rs/core/src/tasks/undo.rs:1)、[review prompts](/config/workspace/codex/codex-rs/core/src/review_prompts.rs:22)、[commit_attribution](/config/workspace/codex/codex-rs/core/src/commit_attribution.rs:1)）
- 要刷新或删除已配置的市场：（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

### 手动创建插件
从打包一个技能的最小插件开始。（实现：[SkillsManager](/config/workspace/codex/codex-rs/core/src/skills/manager.rs:26)、[skills/loader](/config/workspace/codex/codex-rs/core/src/skills/loader.rs:1)、[skills/injection](/config/workspace/codex/codex-rs/core/src/skills/injection.rs:1)、[skills/permissions](/config/workspace/codex/codex-rs/core/src/skills/permissions.rs:1)）

继续往下看，这一节还强调了两件事：
- 1. 创建一个插件文件夹并在 `.codex-plugin/plugin.json` 中放置清单。
- `my-first-plugin/.codex-plugin/plugin.json`
- 使用稳定插件 `name` 采用 kebab-case 格式。Codex 将其用作插件 标识符和组件命名空间。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
