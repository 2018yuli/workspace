# 第72章 开源

> 原始页面：[Open Source – Codex | OpenAI Developers](https://developers.openai.com/codex/open-source)

## 本章目标
这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。

## 先用一个高中数学类比
安全像不等式约束。你不是只关心最优解，还要保证所有可行解都落在安全区域内。

## 严谨定义
严格地说，安全机制是对代理行为加入的一组风险边界与审计条件。

## 你读完应该抓住什么
- OpenAI 在开放环境中开发 Codex 的关键部分。该项目在 GitHub 上进行，您可以跟踪进展、报告问题并贡献改进。
- `开源组件`：| 组件 | 查找位置 | 备注 | | --- | --- | --- | | Codex CLI | openai/codex。
- `报告问题和请求功能`：使用 Codex GitHub 仓库提交有关 Codex 组件的错误报告和功能请求：

## 分步理解
### 正文
先说直白版：
OpenAI 在开放环境中开发 Codex 的关键部分。该项目在 GitHub 上进行，您可以跟踪进展、报告问题并贡献改进。
如果您维护一个广泛使用的开源项目，或者想提名管理重要项目的维护者，您也可以申请 Codex for OSS 计划以获取 API 额度、Codex 的 ChatGPT Pro 以及对 Codex 安全的选择性访问。

把它理解成一个更严谨的过程：
1. OpenAI 在开放环境中开发 Codex 的关键部分。该项目在 GitHub 上进行，您可以跟踪进展、报告问题并贡献改进。
2. 如果您维护一个广泛使用的开源项目，或者想提名管理重要项目的维护者，您也可以申请 Codex for OSS 计划以获取 API 额度、Codex 的 ChatGPT Pro 以及对 Codex 安全的选择性访问。

### 开源组件
先说直白版：
| 组件 | 查找位置 | 备注 | | --- | --- | --- | | Codex CLI | openai/codex | Codex 开源开发的主要家园 | | Codex SDK | openai/codex/sdk | SDK 源代码位于 Codex 仓库 | | Codex 应用服务器 | openai/codex/codex-rs/app-server | 应用服务器源代码位于 Codex 仓库 | | 技能 | openai/skills | 可重用的技能，扩展 Codex | | IDE 扩展 | - | 不开源 | | Codex 网络 | - | 不开源 | | 通用云环境 | openai/codex-universal | Codex 云使用的基础环境 |

把它理解成一个更严谨的过程：
1. | 组件 | 查找位置 | 备注 | | --- | --- | --- | | Codex CLI | openai/codex | Codex 开源开发的主要家园 | | Codex SDK | openai/codex/sdk | SDK 源代码位于 Codex 仓库 | | Codex 应用服务器 | openai/codex/codex-rs/app-server | 应用服务器源代码位于 Codex 仓库 | | 技能 | openai/skills | 可重用的技能，扩展 Codex | | IDE 扩展 | - | 不开源 | | Codex 网络 | - | 不开源 | | 通用云环境 | openai/codex-universal | Codex 云使用的基础环境 |

### 报告问题和请求功能
先说直白版：
使用 Codex GitHub 仓库提交有关 Codex 组件的错误报告和功能请求：
- 错误报告和功能请求：openai/codex/issues
- 讨论论坛：openai/codex/discussions
提交问题时，请注明您使用的组件（CLI、SDK、IDE 扩展、Codex 网络），并尽可能提供版本信息。

把它理解成一个更严谨的过程：
1. 使用 Codex GitHub 仓库提交有关 Codex 组件的错误报告和功能请求：
2. 错误报告和功能请求：openai/codex/issues
3. 讨论论坛：openai/codex/discussions
4. 提交问题时，请注明您使用的组件（CLI、SDK、IDE 扩展、Codex 网络），并尽可能提供版本信息。

## 实战视角
如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。

## 给高中水平读者的最后一句话
不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。
