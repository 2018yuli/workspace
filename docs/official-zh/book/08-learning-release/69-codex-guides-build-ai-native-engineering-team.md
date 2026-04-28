# 第69章 构建 AI 团队

> 原始页面：[Building an AI-Native Engineering Team – Codex | OpenAI Developers](https://developers.openai.com/codex/guides/build-ai-native-engineering-team)

这一章主要把官方页面里的内容重新整理成顺着读也能理解的讲解。

阅读时可以先抓住它解决的问题，再看它的操作方式和限制条件。

## 本章先抓重点
- `介绍`：AI 模型正在迅速扩展它们能够执行的任务范围，这对工程有重大影响。前沿系统现在支持数小时的推理：截至 2025 年 8 月，METR 发现领先模型可以在大约 **50% 的信心** 下完成 …
- `AI 编码：从自动补全到代理`：AI 编码工具的进步远远超出了它们作为自动补全助手的起点。早期工具处理诸如建议下一行代码或填充函数模板等快速任务。随着模型获得更强的推理能力，开发人员开始通过聊天界面…
- `1\. 计划`：组织内的团队通常依赖工程师来确定某个功能是否可行、构建所需的时间以及涉及哪些系统或团队。虽然任何人都可以起草规格，但形成准确的计划通常需要深厚的代码库意识以及与工程团队多轮迭代以揭示…

## 正文整理
### 介绍
AI 模型正在迅速扩展它们能够执行的任务范围，这对工程有重大影响。前沿系统现在支持数小时的推理：截至 2025 年 8 月，METR 发现领先模型可以在大约 **50% 的信心** 下完成 **2 小时和 17 分钟** 的连续工作，输出正确答案。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）

继续往下看，这一节还强调了两件事：
- 这一能力正在迅速提高，任务长度大约每七个月翻一番。几年前，模型只能管理大约 30 秒的推理——足以进行小的代码建议。如今，随着模型支持更长的推理链，整个软件开发生命周期可能都在 AI 助手的考虑范围内，使编码代理能够有效地参与规划、设计、开发、测试、代码审查和部署。（实现：[ModelsManager](/config/workspace/codex/codex-rs/core/src/models_manager/manager.rs:55)、[model_info](/config/workspace/codex/codex-rs/core/src/models_manager/model_info.rs:1)、[model_presets](/config/workspace/codex/codex-rs/core/src/models_manager/model_presets.rs:1)、[supported_models](/config/workspace/codex/codex-rs/app-server/src/models.rs:10)）

### AI 编码：从自动补全到代理
AI 编码工具的进步远远超出了它们作为自动补全助手的起点。早期工具处理诸如建议下一行代码或填充函数模板等快速任务。随着模型获得更强的推理能力，开发人员开始通过聊天界面与代理进行交互，以进行配对编程和代码探索。（实现：[tools/orchestrator](/config/workspace/codex/codex-rs/core/src/tools/orchestrator.rs:43)、[tools/router](/config/workspace/codex/codex-rs/core/src/tools/router.rs:1)、[tools/registry](/config/workspace/codex/codex-rs/core/src/tools/registry.rs:1)、[unified_exec/mod](/config/workspace/codex/codex-rs/core/src/unified_exec/mod.rs:74)）

继续往下看，这一节还强调了两件事：
- 如今的编码代理能够生成整个文件，搭建新项目，并将设计转换为代码。它们能够推理多步骤的问题，例如调试或重构，代理执行也正在从个人开发者的机器转向基于云的多代理环境。这改变了开发者的工作方式，使他们能够减少在 IDE 内生成代码的时间，更多地关注于委派整个工作流程。（实现：[Codex](/config/workspace/codex/codex-rs/core/src/codex.rs:285)、[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager::fork_thread](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375)、[agent/control](/config/workspace/codex/codex-rs/core/src/agent/control.rs:1)）
- | 能力 | 使其成为可能 | | --- | --- | | **跨系统的统一上下文** | 单一模型能够读取代码、配置和遥测，在之前需要单独工具的各层之间提供一致的推理。 | | **结构化工具执行** | 模型现在可以直接调用编译器、测试运行器和扫描器，产生可验证的结果而不是静态建议。 | |…（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）
- 在 OpenAI，我们亲眼目睹了这一点。开发周期加速，过去需要数周的工作现在在数天内交付。团队在跨域移动中更加顺畅，更快地适应不熟悉的项目，并在整个组织内更灵活、更自主地运作。许多例行且耗时的任务，如记录新代码、提供相关测试、维护依赖关系和清理功能标志，现在完全委派给 Codex。（实现：[Codex](/config/workspace/codex/codex-rs/core/src/codex.rs:285)、[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager::fork_thread](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:375)、[agent/control](/config/workspace/codex/codex-rs/core/src/agent/control.rs:1)）

### 1\. 计划
组织内的团队通常依赖工程师来确定某个功能是否可行、构建所需的时间以及涉及哪些系统或团队。虽然任何人都可以起草规格，但形成准确的计划通常需要深厚的代码库意识以及与工程团队多轮迭代以揭示需求、澄清边缘案例，以及在技术上达成一致的现实。

### 编码代理如何帮助
AI 编码代理在规划和范围界定期间为团队提供即时的、代码感知的见解。举例来说，团队可能会建立将编码代理与其问题跟踪系统连接的工作流，以读取功能规格，交叉引用代码库，然后标记歧义，将工作拆分为子组件，或估算难度。

继续往下看，这一节还强调了两件事：
- 编码代理还可以即时追踪代码路径，以显示参与某个功能的服务——这一工作以前需要数小时或数天的手动挖掘大型代码库。

### 工程师代替做什么
由于代理提取了以前需要为产品对齐和范围界定会议提供的上下文，团队可以将更多时间花费在核心功能工作上。关键的实施细节、依赖关系和边缘案例在前期便被识别出来，从而加快决策速度，减少会议。（实现：[CodexThread](/config/workspace/codex/codex-rs/core/src/codex_thread.rs:37)、[ThreadManager](/config/workspace/codex/codex-rs/core/src/thread_manager.rs:120)、[context_manager](/config/workspace/codex/codex-rs/core/src/context_manager/mod.rs:1)、[message_history](/config/workspace/codex/codex-rs/core/src/message_history.rs:1)）

继续往下看，这一节还强调了两件事：
- | 委托 | 审查 | 拥有 | | --- | --- | --- | | AI 代理可以对可行性和架构分析进行初步处理。它们读取规格，将其映射到代码库，识别依赖关系，并提取需要澄清的歧义或边缘案例。 | 团队审查代理的发现，以验证准确性、评估完整性，并确保估算反映实际的技术约束。故事点分配、工作量估算和识别不明显的风险仍然需要人工判断。 | 战略决策——…（实现：[config/state](/config/workspace/codex/codex-rs/config/src/state.rs:118)、[config/constraint](/config/workspace/codex/codex-rs/config/src/constraint.rs:51)、[config/config_requirements](/config/workspace/codex/codex-rs/config/src/config_requirements.rs:78)、[config/overrides](/config/workspace/codex/codex-rs/config/src/overrides.rs:7)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
