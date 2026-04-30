# `auth/` 目录说明

这个目录目前主要放的是 Codex 认证模块的“存储层”实现，核心文件是 [storage.rs](/codex/codex-rs/core/src/auth/storage.rs#L1)。

上层入口在 [auth.rs](/codex/codex-rs/core/src/auth.rs#L1)：

- `auth.rs` 负责认证流程本身，例如加载当前登录状态、区分 `ApiKey` / `Chatgpt` 模式、读取 token、刷新 token、登出，以及把这些能力暴露给其他模块使用。
- `auth/storage.rs` 负责“认证信息存到哪里、怎么读写、怎么删除”。它不决定认证策略，而是给 `auth.rs` 提供统一的持久化接口。

## `storage.rs` 是干嘛的

`storage.rs` 的职责可以概括成三件事：

- 定义认证数据的结构，也就是 `AuthDotJson`，对应 `$CODEX_HOME/auth.json` 的内容。
- 定义统一存储抽象 `AuthStorageBackend`，约定 `load`、`save`、`delete` 三个操作。
- 提供多种具体存储后端，并根据配置创建合适的实现。

换句话说，它是认证系统的 repository / persistence 层。

## 里面有哪些存储模式

`AuthCredentialsStoreMode` 定义了 4 种模式：

- `File`
  - 直接把认证信息保存到 `$CODEX_HOME/auth.json`。
- `Keyring`
  - 使用系统 keyring 保存认证信息；如果 keyring 不可用，则报错。
- `Auto`
  - 优先使用 keyring；失败时回退到文件存储。
- `Ephemeral`
  - 只放在当前进程内存里，不写磁盘，也不进 keyring。

这些模式最终都会通过 `create_auth_storage(...)` 生成对应的后端对象，供 `auth.rs` 使用。

## 主要类型

- `AuthDotJson`
  - 认证信息的数据模型。
  - 包含 `auth_mode`、`OPENAI_API_KEY`、`tokens`、`last_refresh` 等字段。
- `AuthStorageBackend`
  - 存储抽象 trait。
  - 统一了 `load()` / `save()` / `delete()`。
- `FileAuthStorage`
  - 基于 `$CODEX_HOME/auth.json` 的文件存储实现。
- `KeyringAuthStorage`
  - 基于系统 keyring 的安全存储实现。
- `AutoAuthStorage`
  - keyring 优先，失败时回退到文件。
- `EphemeralAuthStorage`
  - 基于进程内全局内存 map 的临时存储实现。

## 设计意图

这样拆分有几个实际好处：

- `auth.rs` 可以只关心认证行为，不需要关心底层保存方式。
- 可以在不同运行环境下切换存储策略，比如桌面环境用 keyring，测试或临时会话用 ephemeral。
- 便于测试。`storage.rs` 里已经为不同后端提供了比较完整的单元测试。

## 一个典型调用链

1. `auth.rs` 判断当前应该使用哪种认证模式和存储模式。
2. `auth.rs` 调用 `create_auth_storage(...)` 创建后端。
3. 后端从文件、keyring 或内存中读取 `AuthDotJson`。
4. `auth.rs` 再把这些数据包装成更高层的 `CodexAuth`、`ChatgptAuth` 等运行时对象。

## 一句话总结

如果你想知道“Codex 怎么登录”，主要看 [auth.rs](/codex/codex-rs/core/src/auth.rs#L1)。

如果你想知道“登录后的 token / API key 被存在哪里、怎么落盘、怎么删除、怎么回退”，主要看 [storage.rs](/codex/codex-rs/core/src/auth/storage.rs#L1)。
