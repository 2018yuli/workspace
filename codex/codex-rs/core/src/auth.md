# `auth.rs` 是干嘛的

[auth.rs](/codex/codex-rs/core/src/auth.rs#L1) 是 Codex CLI 的认证核心模块。

它负责回答几个关键问题：

- 当前用户是用什么方式登录的？
- 现在内存里应该使用哪份认证状态？
- ChatGPT token 过期或请求返回 `401` 时，应该如何恢复？
- 登录限制是否满足，比如是否强制要求 API key 登录，或者是否限定某个 ChatGPT workspace？

如果说 [auth/storage.rs](/codex/codex-rs/core/src/auth/storage.rs#L1) 是“认证数据存储层”，那么 `auth.rs` 就是“认证业务层”。

## 它管理哪些认证方式

`auth.rs` 统一管理两类认证：

- `ApiKey`
  - 使用 `OPENAI_API_KEY` 或 `CODEX_API_KEY`，或者保存到本地的 API key。
- `Chatgpt`
  - 使用 ChatGPT 登录拿到的 token。
- `ChatgptAuthTokens`
  - 一种特殊的 ChatGPT 模式，token 由外部应用提供，不由 CLI 自己落盘管理，通常只存在于内存中。

对应的核心类型是：

- `AuthMode`
  - 高层分类，只区分 `ApiKey` 和 `Chatgpt`。
- `CodexAuth`
  - 当前实际使用的认证对象，可能是 `ApiKey`、`Chatgpt` 或 `ChatgptAuthTokens`。
- `AuthManager`
  - 模块里最重要的管理器，对外提供统一的认证读取、刷新、登出和恢复能力。

## 它主要做什么

### 1. 加载当前认证状态

`load_auth(...)` 会按优先级决定当前应该使用哪份认证：

1. 如果允许 `CODEX_API_KEY` 环境变量，并且它存在，优先使用它。
2. 先检查 ephemeral 内存存储里的外部 ChatGPT token。
3. 如果没有，再检查持久化存储中的认证信息。

这样做的目的很实际：

- 环境变量可以临时覆盖本地登录状态。
- 外部应用注入的 token 要优先于磁盘上的旧凭据。
- 最后才回退到文件或 keyring 中保存的登录信息。

## 2. 提供登录与登出能力

这个文件里有几组直接操作认证状态的函数：

- `login_with_api_key(...)`
  - 保存 API key 登录信息。
- `login_with_chatgpt_auth_tokens(...)`
  - 保存外部提供的 ChatGPT access token，写入 ephemeral 存储。
- `save_auth(...)`
  - 把 `AuthDotJson` 保存到配置的存储后端。
- `logout(...)`
  - 删除认证信息。

这些函数本身不关心底层是文件、keyring 还是内存；它们把这部分工作委托给 [auth/storage.rs](/codex/codex-rs/core/src/auth/storage.rs#L1)。

## 3. 暴露统一的认证读取接口

`CodexAuth` 提供了一层运行时视图，方便其他模块读取认证信息，例如：

- `api_key()`
  - 取 API key。
- `get_token()`
  - 取当前用于 Bearer 认证的 token。
- `get_token_data()`
  - 取完整的 token 数据。
- `get_account_id()` / `get_account_email()`
  - 取当前 ChatGPT 账号信息。
- `account_plan_type()`
  - 取订阅计划类型，用于 UI 或产品逻辑判断。

也就是说，其他模块通常不应该自己去读 `auth.json`，而应该通过 `CodexAuth` 或 `AuthManager` 获取当前认证状态。

## 4. 刷新 ChatGPT token

`auth.rs` 负责 ChatGPT token 的刷新逻辑。

关键点有两个：

- 如果 token 长时间未刷新，`AuthManager::auth()` 会先尝试 `refresh_if_stale(...)`。
- 真正的刷新请求由 `request_chatgpt_token_refresh(...)` 发到 OAuth endpoint：
  - 默认地址是 `https://auth.openai.com/oauth/token`
  - 也支持通过 `CODEX_REFRESH_TOKEN_URL_OVERRIDE` 覆盖

刷新成功后，会：

1. 更新 `id_token` / `access_token` / `refresh_token`
2. 更新 `last_refresh`
3. 写回存储
4. 重新加载内存缓存

这保证了整个进程后续看到的是一致的新认证状态。

## 5. 处理请求返回 `401` 的恢复流程

这是 `auth.rs` 里比较重要的一块。

当接口请求返回 `401 Unauthorized` 时，模块不会立刻失败，而是通过 `UnauthorizedRecovery` 做一个小型状态机恢复。

对于 CLI 自己管理的 ChatGPT 登录：

1. 先尝试从存储重新加载认证数据。
2. 只有当 account id 与当前进程里缓存的一致时，才接受这次 reload。
3. 如果 reload 后 token 还是同一份，就尝试走 refresh token 流程。
4. 如果还是失败，再把错误抛给上层。

这样设计是为了避免：

- 多个进程同时刷新 token 时互相覆盖
- 当前进程误读到另一个账号的认证信息

对于外部注入的 `ChatgptAuthTokens`：

- 不会直接刷新本地磁盘 token
- 会调用 `ExternalAuthRefresher`
- 由父应用重新下发一份新的 token
- 然后写入 ephemeral 存储并 reload

## 6. 维护单一认证真相源

`AuthManager` 的定位是“单一认证真相源”。

它的职责包括：

- 启动时加载一次认证状态
- 在运行期缓存认证对象
- 按需刷新 stale token
- 显式 reload 存储中的认证信息
- 在登出后清空缓存
- 为 `401` 恢复流程提供统一入口

它的设计目标不是“随时自动监听磁盘变化”，而是“让整个程序在一次运行中看到一致的认证快照”。

这点很重要，因为如果不同模块在同一时刻看到不同认证状态，行为会变得不可预测。

## 7. 执行登录限制校验

`enforce_login_restrictions(...)` 用来执行配置层面的认证限制，例如：

- 强制要求只能使用 API key 登录
- 强制要求只能使用 ChatGPT 登录
- 强制要求当前登录属于指定 workspace

如果不满足限制，它会触发登出并返回错误。

这说明 `auth.rs` 不只是“读 token”，它还负责保证当前认证状态符合运行约束。

## 和 `storage.rs` 的关系

两者分工可以这样理解：

- [auth.rs](/codex/codex-rs/core/src/auth.rs#L1)
  - 认证业务逻辑
  - 认证状态加载
  - token 刷新
  - 401 恢复
  - 登录限制校验
  - 认证缓存管理
- [auth/storage.rs](/codex/codex-rs/core/src/auth/storage.rs#L1)
  - 认证信息落盘/读盘
  - keyring / file / auto / ephemeral 后端实现
  - 存储抽象

## 建议怎么读

如果你要读这个文件，建议按下面顺序看：

1. `AuthMode` 和 `CodexAuth`
2. `load_auth(...)`
3. `AuthManager`
4. `request_chatgpt_token_refresh(...)`
5. `UnauthorizedRecovery`
6. `enforce_login_restrictions(...)`

这样会比较容易先建立整体模型，再理解异常和边界处理。

## 一句话总结

`auth.rs` 是 Codex 的认证控制中心。

它负责把“凭据从哪里来、当前该用哪份凭据、什么时候刷新、401 怎么恢复、限制是否满足”这些问题统一收口起来，对外提供稳定的认证行为。
