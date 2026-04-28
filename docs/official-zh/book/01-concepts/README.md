# 01 核心概念

这一组文件是整本书最重要的基础层。它对应的是 Codex 的核心业务语义：输入如何组织、状态如何积累、执行如何受限、任务如何拆分。

## 章节

- [第05章 提示](./05-codex-prompting.md)
- [第06章 自定义](./06-codex-concepts-customization.md)
- [第07章 记忆](./07-codex-memories.md)
- [第08章 编年史](./08-codex-memories-chronicle.md)
- [第09章 沙盒](./09-codex-concepts-sandboxing.md)
- [第10章 子代理](./10-codex-concepts-subagents.md)
- [第11章 工作流](./11-codex-workflows.md)
- [第12章 模型](./12-codex-models.md)
- [第13章 网络安全](./13-codex-concepts-cyber-safety.md)

## 这一组在业务架构里的位置

这一组大体对应 `codex/codex-rs/core` 里的主编排逻辑，以及与之紧密相关的 `state`、`config`、`sandbox` 子系统。
