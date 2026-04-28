# 第37章 互联网访问

> 原始页面：[Agent internet access – Codex web | OpenAI Developers](https://developers.openai.com/codex/cloud/internet-access)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- 默认情况下，Codex 在代理阶段会阻止互联网访问。设置脚本仍然可以在有互联网访问的情况下运行，这样您可以安装依赖项。当您需要时，您可以根据环境为代理启用互联网访问。
- `代理互联网访问的风险`：启用代理互联网访问会增加安全风险，包括：
- `配置代理互联网访问`：代理互联网访问是按环境进行配置的。

## 正文整理
### 正文
默认情况下，Codex 在代理阶段会阻止互联网访问。设置脚本仍然可以在有互联网访问的情况下运行，这样您可以安装依赖项。当您需要时，您可以根据环境为代理启用互联网访问。

### 代理互联网访问的风险
启用代理互联网访问会增加安全风险，包括：

继续往下看，这一节还强调了两件事：
- 来自不可信网站内容的提示注入（实现：[custom_prompts](/config/workspace/codex/codex-rs/core/src/custom_prompts.rs:9)、[project_doc](/config/workspace/codex/codex-rs/core/src/project_doc.rs:134)、[instructions/user_instructions](/config/workspace/codex/codex-rs/core/src/instructions/user_instructions.rs:1)）
- 代码或秘密的外泄
- 下载恶意软件或易受攻击的依赖项

### 配置代理互联网访问
代理互联网访问是按环境进行配置的。（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

继续往下看，这一节还强调了两件事：
- **关闭**: 完全阻止互联网访问。
- **打开**: 允许互联网访问，您可以通过域名白名单和允许的 HTTP 方法进行限制。

### 域名白名单
您可以选择预设的白名单：

继续往下看，这一节还强调了两件事：
- **无**: 使用空白名单并从头开始指定域名。
- **常见依赖项**: 使用预设的域名白名单，这些域名通常用于下载和构建依赖项。请参阅 常见依赖项 中的列表。
- **全部（无限制）**: 允许所有域名。

### 允许的 HTTP 方法
为了额外保护，将网络请求限制为 `GET`，`HEAD` 和 `OPTIONS`。使用其他方法（`POST`、`PUT`、`PATCH`、`DELETE` 等）的请求将被阻止。

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
