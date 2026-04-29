# 第44章 高级配置

> 原始页面：[Advanced Configuration – Codex | OpenAI Developers](https://developers.openai.com/codex/config-advanced)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 在需要更好地控制提供者、策略和集成时使用这些选项。有关快速入门，请参见 配置基础。
- `配置文件`：配置文件允许您保存命名的配置值集，并从 CLI 切换它们。
- `CLI 的一次性覆盖`：除编辑 `~/.codex/config.toml` 外，您还可以从 CLI 覆盖单次运行的配置：

## 正文整理
### 正文
在需要更好地控制提供者、策略和集成时使用这些选项。有关快速入门，请参见 配置基础。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 有关项目指导、可重用能力、自定义斜线命令、子代理工作流和集成的背景信息，请见 定制。有关配置密钥，请参见 配置参考。（实现：[Codex](/codex/codex-rs/core/src/codex.rs#L285)、[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager::fork_thread](/codex/codex-rs/core/src/thread_manager.rs#L375)、[agent/control](/codex/codex-rs/core/src/agent/control.rs#L1)）

### 配置文件
配置文件允许您保存命名的配置值集，并从 CLI 切换它们。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 配置文件处于实验状态，可能会在未来的版本中更改或删除。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 目前不支持在 Codex IDE 扩展中使用配置文件。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 在 `config.toml` 中定义配置文件`[profiles.<name>]`，然后运行 `codex --profile <name>`：（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

### CLI 的一次性覆盖
除编辑 `~/.codex/config.toml` 外，您还可以从 CLI 覆盖单次运行的配置：（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 在存在时优先使用专用标志（例如 `--model`）。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）
- 当需要覆盖任意键时，请使用 `-c` / `--config`。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 示例：

### 配置与状态位置
Codex 将其本地状态存储在 `CODEX_HOME` 下（默认为 `~/.codex`）。（实现：[StateRuntime](/codex/codex-rs/state/src/runtime.rs#L63)、[log_db](/codex/codex-rs/state/src/log_db.rs#L47)、[extract/apply_rollout_item](/codex/codex-rs/state/src/extract.rs#L15)、[state_db](/codex/codex-rs/core/src/state_db.rs#L1)）

继续往下看，这一节还强调了两件事：
- 您可能会看到的常见文件：
- `config.toml`（您的本地配置）（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- `auth.json`（如果您使用基于文件的凭据存储）或您的操作系统密钥链/密钥环（实现：[auth](/codex/codex-rs/core/src/auth.rs#L1)、[auth/storage](/codex/codex-rs/core/src/auth/storage.rs#L1)、[login crate](/codex/codex-rs/login/src/lib.rs#L1)、[cloud-tasks auth helper](/codex/codex-rs/cloud-tasks/src/util.rs#L62)）

### 项目配置文件 (`.codex/config.toml`)
除了用户配置外，Codex 还会读取项目范围的覆盖 `.codex/config.toml` 文件，位于您的仓库中。Codex 从项目根目录向您当前的工作目录遍历，并加载它发现的每一个 `.codex/config.toml` 文件。如果多个文件定义了相同的键，则离您工作目录最近的文件获胜。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）

继续往下看，这一节还强调了两件事：
- 出于安全原因，仅当项目被信任时，Codex 才会加载项目范围的配置文件。如果项目不被信任，Codex 将忽略项目的 `.codex/` 层，包括 `.codex/config.toml`、项目本地钩子和项目本地规则。用户层和系统层仍然保持独立并继续加载。（实现：[config/state](/codex/codex-rs/config/src/state.rs#L118)、[config/constraint](/codex/codex-rs/config/src/constraint.rs#L51)、[config/config_requirements](/codex/codex-rs/config/src/config_requirements.rs#L78)、[config/overrides](/codex/codex-rs/config/src/overrides.rs#L7)）
- 项目配置中的相对路径（例如，`model_instructions_file`）相对于包含 `config.toml` 的 `.codex/` 文件夹进行解析。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
