# 第13章 网络安全

> 原始页面：[Cyber Safety – Codex | OpenAI Developers](https://developers.openai.com/codex/concepts/cyber-safety)

这一章讲的是边界。Codex 不是纯聊天工具，它会读文件、改文件、跑命令，所以必须先讲清楚它能做到哪里。

只要把“能力”和“权限”分开理解，这类章节就不会难。

## 数学类比
安全像不等式约束。你不是只关心最优解，还要保证所有可行解都落在安全区域内。

## 严谨定义
严格地说，安全机制是对代理行为加入的一组风险边界与审计条件。

## 本章先抓重点
- 除了安全培训之外，基于自动分类器的监控器还会检测可疑网络活动的信号，并将高风险流量路由到能力较低的模型（GPT-5.2）。我们预期受这些缓解措施影响的流量非常少，并且正在努力完善我们的政策、分类器和产…
- `我们为什么要这样做`：在最近几个月中，我们在网络安全任务上的模型性能取得了重要进展，这对开发者和安全专业人士都有好处。随着我们的模型在网络安全相关任务（如漏洞发现）上的改进，我们采取了预防性措施：扩…
- `它是如何工作的`：从事网络安全相关工作或类似活动的开发者和安全专业人员，可能会因为 自动检测系统的误判 而导致请求被转发到 GPT-5.2 作为后备。我们预期受这些缓解措施影响的流量非常少，并且正在…

## 正文整理
### 正文
除了安全培训之外，基于自动分类器的监控器还会检测可疑网络活动的信号，并将高风险流量路由到能力较低的模型（GPT-5.2）。我们预期受这些缓解措施影响的流量非常少，并且正在努力完善我们的政策、分类器和产品内通知。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

### 我们为什么要这样做
在最近几个月中，我们在网络安全任务上的模型性能取得了重要进展，这对开发者和安全专业人士都有好处。随着我们的模型在网络安全相关任务（如漏洞发现）上的改进，我们采取了预防性措施：扩大保护和执行，以支持合法研究，同时减缓滥用。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

继续往下看，这一节还强调了两件事：
- 网络能力本质上是双重用途的。支撑重要防御工作的相同知识和技术——渗透测试、漏洞研究、大规模扫描、恶意软件分析和威胁情报——也可能造成现实世界的伤害。
- 这些能力和技术需要在可以用于提高安全性的上下文中更容易获得和使用。我们的 网络信任访问 试点项目使个人和组织能够在不中断的情况下继续使用模型进行潜在的高风险网络安全活动。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）

### 它是如何工作的
从事网络安全相关工作或类似活动的开发者和安全专业人员，可能会因为 自动检测系统的误判 而导致请求被转发到 GPT-5.2 作为后备。我们预期受这些缓解措施影响的流量非常少，并且正在积极调校我们的政策和分类器。

继续往下看，这一节还强调了两件事：
- Codex CLI 最新的 alpha 版本包含针对请求被转发时的产品内消息。这些消息将在接下来的几天内在所有客户端中得到支持。（实现：[app-server run_main](/codex/codex-rs/app-server/src/lib.rs#L295)、[CodexMessageProcessor](/codex/codex-rs/app-server/src/codex_message_processor.rs#L399)、[transport](/codex/codex-rs/app-server/src/transport.rs#L73)、[thread_state](/codex/codex-rs/app-server/src/thread_state.rs#L1)）
- 受到缓解措施影响的账户可以通过加入下面的 网络信任访问 项目来恢复对 GPT-5.3-Codex 的访问。（实现：[CodexThread](/codex/codex-rs/core/src/codex_thread.rs#L37)、[ThreadManager](/codex/codex-rs/core/src/thread_manager.rs#L120)、[context_manager](/codex/codex-rs/core/src/context_manager/mod.rs#L1)、[message_history](/codex/codex-rs/core/src/message_history.rs#L1)）
- 我们认识到，加入网络信任访问可能并不适合每个人，因此我们计划在大多数情况下从账户级安全检查转向请求级检查，以便在我们扩大这些缓解措施和 增强 网络弹性时进行。

### 网络信任访问
我们正在试点“网络信任访问”，允许开发者在继续调校政策和分类器以供一般使用的同时，保留高级功能。我们的目标是很少有用户需要加入 网络信任访问。

继续往下看，这一节还强调了两件事：
- 要将模型用于潜在的高风险网络安全工作：（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）
- 用户可以在 chatgpt.com/cyber 验证身份
- 企业可以通过他们的 OpenAI 代表请求 网络信任访问 ，默认针对整个团队

### 误报
合法或非网络安全活动有时可能会被标记。当发生重新路由时，响应的模型将在 API 请求日志中可见，并在 CLI 中出示产品内通知，随后在所有表面展示。如果您经历了您认为不正确的重新路由，请通过 `/feedback` 举报误报。（实现：[ModelsManager](/codex/codex-rs/core/src/models_manager/manager.rs#L55)、[model_info](/codex/codex-rs/core/src/models_manager/model_info.rs#L1)、[model_presets](/codex/codex-rs/core/src/models_manager/model_presets.rs#L1)、[supported_models](/codex/codex-rs/app-server/src/models.rs#L10)）

## 小结
读完这一章后，最重要的不是记住页面上的每个术语，而是知道它在整个 Codex 体系里负责解决什么问题。
