# `thread_state.rs` 是干嘛的

[thread_state.rs](/codex/codex-rs/app-server/src/thread_state.rs#L1) 是 `app-server` 里负责“线程运行时状态管理”的模块。

这里的 “thread” 指的是 Codex 会话线程，不是操作系统线程。

它的职责不是保存线程历史到磁盘，也不是直接执行 agent，而是维护 app-server 运行过程中，每个会话线程当前附带的一些临时状态，比如：

- 这个线程现在有哪些连接在订阅
- 当前是否有 listener 任务在监听 `CodexThread` 事件流
- 当前 turn 的临时摘要是什么
- 有没有待处理的 interrupt / rollback 请求
- 这个线程的活动 turn 快照是什么

一句话说，它是 `app-server` 的线程级 runtime state 容器。

## 为什么需要这个模块

`codex-core` 负责线程本身的业务逻辑和持久化历史，`app-server` 则负责把这些线程暴露给多个客户端连接。

在这个过程中，app-server 需要额外维护一些“仅在服务器运行期间才有意义”的状态：

- 某个 thread 当前被哪些 connection 订阅
- 某个 thread 的事件监听任务是否已经启动
- 当前 turn 还没结束时，已经收到了哪些中间事件
- 某个客户端刚发过 `turn/interrupt`，但真正的中断结果还没回来

这些状态不属于 `codex-core`，也不应该写进持久化 rollout 文件，所以集中放在 `thread_state.rs`。

## 这个文件里的两个核心结构

这个模块主要围绕两个类型：

- `ThreadState`
  - 单个 `thread_id` 对应的一份运行时状态
- `ThreadStateManager`
  - 管理所有线程的 `ThreadState`

可以把它理解成：

- `ThreadState` 是单线程上下文
- `ThreadStateManager` 是全局索引和生命周期管理器

## `ThreadState` 管什么

`ThreadState` 是每个会话线程的一份可变状态，当前主要包含这些字段。

### `pending_interrupts`

类型是一个队列：

- 保存已经收到、但还没完全处理完的 interrupt 请求
- 里面记录了请求 id 和 API version

这个状态的意义是：客户端发起 `turn/interrupt` 后，系统需要知道稍后该把结果回给谁。

### `pending_rollbacks`

- 保存当前挂起的 rollback 请求 id

如果同一个线程已经有 rollback 正在处理中，系统就可以基于这个状态避免重复发起或正确完成后续处理。

### `turn_summary`

`TurnSummary` 是一个简化的当前 turn 运行摘要，包含：

- `file_change_started`
  - 已经开始但可能还没完成的文件变更项
- `command_execution_started`
  - 已经开始但可能还没完成的命令执行项
- `last_error`
  - turn 过程中最近一次错误

这块状态主要给 [bespoke_event_handling.rs](/codex/codex-rs/app-server/src/bespoke_event_handling.rs#L1) 用，用来拼装 turn 完成、中断、失败时的最终通知。

### `cancel_tx`

- 当前 listener 任务的取消句柄

如果同一个 thread 需要替换 listener，旧 listener 可以通过这个 `oneshot::Sender<()>` 被停止。

### `experimental_raw_events`

- 当前这个线程是否启用了 experimental raw event 输出

这个开关会影响事件流对外怎么发。

### `listener_generation`

- listener 的代际编号

它的作用是避免旧 listener 在异步退出时误清理新 listener 的状态。也就是一个典型的“防止 stale task 清场”的代数标记。

### `listener_command_tx`

- 发给 listener 任务的内部命令通道

目前这里的命令类型是 `ThreadListenerCommand`，里面定义了：

- `SendThreadResumeResponse`

也就是说，外部逻辑可以通过这个通道，把一些和线程监听协同相关的命令发给已经运行的 listener。

### `current_turn_history`

- 当前 turn 的事件累积器

它使用 `ThreadHistoryBuilder` 持续吃进 `EventMsg`，生成当前活动 turn 的快照。

这让 app-server 在 turn 进行中也能拿到一个“截至目前的活动 turn 视图”。

### `listener_thread`

- 当前 listener 绑定的是哪一个 `CodexThread`

它是 `Weak<CodexThread>`，用于判断当前 listener 是否仍然匹配目标线程对象。

### `subscribed_connections`

- 当前订阅这个 thread 的所有连接 id

这是 app-server 广播事件时非常关键的一层索引。

## `ThreadState` 提供了什么行为

### `set_listener(...)`

给当前线程设置新的 listener：

- 如果之前已有 listener，会先取消旧的
- 增加 `listener_generation`
- 创建新的 command channel
- 记录当前绑定的 `CodexThread`

这基本就是“切换到新的事件监听任务”。

### `clear_listener()`

清理 listener 相关状态：

- 取消任务
- 清空命令通道
- 重置当前 turn 历史
- 清除绑定线程引用

注意它会把 `current_turn_history` 一起 reset，所以不仅是停监听，也是在做一次完整 listener 上下文清理。

### `listener_matches(...)`

判断当前 state 里的 listener 是否仍然对应某个 `CodexThread` 实例。

这在 `codex_message_processor.rs` 里可以避免重复启动 listener。

### `track_current_turn_event(...)`

把内部事件 `EventMsg` 喂给 `ThreadHistoryBuilder`。

如果 builder 判断当前已经没有 active turn，就会自动 reset。

这说明这个模块既管理“订阅关系”，也管理“当前 turn 过程态”。

### 订阅相关方法

- `add_connection(...)`
- `remove_connection(...)`
- `subscribed_connection_ids()`

这些方法负责维护线程和连接之间的关联关系。

## `ThreadStateManager` 是干嘛的

`ThreadStateManager` 是线程状态总表。

它内部维护三套映射：

- `thread_states`
  - `thread_id -> ThreadState`
- `subscription_state_by_id`
  - `subscription_id -> { thread_id, connection_id }`
- `thread_ids_by_connection`
  - `connection_id -> set<thread_id>`

这三套索引一起解决三个方向的问题：

- 已知 `thread_id`，找到它的状态
- 已知 `subscription_id`，找到它属于哪个 thread / connection
- 已知 `connection_id`，找到它订阅了哪些 threads

## `ThreadStateManager` 的主要职责

### 1. 按需创建线程状态

`thread_state(thread_id)` 会懒创建对应的 `ThreadState`。

也就是说，只有真的访问到某个 thread 时，这份状态才会存在。

### 2. 建立订阅关系

`set_listener(...)` 和 `ensure_connection_subscribed(...)` 会：

- 建立 `connection -> thread` 关系
- 把 connection 加入该 thread 的订阅集合
- 根据需要启用 experimental raw events

区别大致是：

- `set_listener(...)`
  - 用于显式建立 subscription 记录
- `ensure_connection_subscribed(...)`
  - 用于确保关联存在，但不一定新增一个新的 subscription id

### 3. 移除订阅

`remove_listener(subscription_id)` 会：

- 删除这条 subscription
- 检查该连接是否仍订阅同一个 thread
- 必要时从 thread 的连接集合中移除 connection
- 必要时更新 `thread_ids_by_connection`

值得注意的是：

- 即使最后一个订阅者离开了，也不会自动销毁 listener
- 日志里明确写的是 `retaining thread listener after last subscription removed`

这说明当前设计是“listener 生命周期不完全等同于订阅生命周期”。

### 4. 连接断开清理

`remove_connection(connection_id)` 负责处理连接整体断开时的清理：

- 删除这个连接对应的 thread 集合索引
- 删除所有 subscription 记录
- 从相关线程的 `subscribed_connections` 中把它移除

如果这个连接之前没有 thread 索引，代码还会保守地扫描全部 `thread_states` 做一次移除，避免状态残留。

### 5. 线程状态整体销毁

`remove_thread_state(thread_id)` 负责彻底 teardown 某个线程的运行时状态：

- 从 manager 中移除 `ThreadState`
- 调用 `clear_listener()`
- 清理所有 subscription 和 connection 反向索引

这是真正的“线程状态销毁入口”。

## 它和其他模块的关系

### 和 `codex_message_processor.rs`

[codex_message_processor.rs](/codex/codex-rs/app-server/src/codex_message_processor.rs#L1) 是这个模块的主要使用者。

它会用 `ThreadStateManager` 来：

- 获取某个线程的 state
- 启动或复用 listener
- 记录 pending interrupt / rollback
- 读取订阅连接列表并把事件发给它们
- 在线程销毁时清理状态

可以说，`thread_state.rs` 是 `codex_message_processor.rs` 的状态后端。

### 和 `bespoke_event_handling.rs`

[bespoke_event_handling.rs](/codex/codex-rs/app-server/src/bespoke_event_handling.rs#L1) 主要消费 `ThreadState` 里的 turn 过程态，例如：

- `turn_summary`
- `pending_rollbacks`
- 当前 turn 的完成/中断状态

它更像状态消费者，而不是状态拥有者。

### 和 `codex-core::CodexThread`

`ThreadState` 会保存一个 `Weak<CodexThread>`，但并不拥有业务线程本身。

这意味着：

- 真正的对话线程对象仍属于 `codex-core`
- `app-server` 这里只是附着一层运行时控制和广播状态

## 这个模块不做什么

为了避免误读，也可以明确一下边界。

这个模块不负责：

- 持久化 thread 历史
- 具体执行 turn
- 认证
- 配置加载
- 把所有事件转换成协议通知

它的职责非常聚焦：管理每个 thread 在 app-server 侧的运行时附加状态。

## 适合怎么理解

最容易理解它的方式是：

- `codex-core::CodexThread`
  - 真正的业务线程
- `ThreadState`
  - app-server 给这个业务线程挂上的 runtime sidecar
- `ThreadStateManager`
  - 管理所有这些 sidecar 的注册表

这个比把它理解成“线程模型本身”更准确。

## 建议怎么读

如果你要继续往下读源码，建议顺序是：

1. [thread_state.rs](/codex/codex-rs/app-server/src/thread_state.rs#L1)
2. [codex_message_processor.rs](/codex/codex-rs/app-server/src/codex_message_processor.rs#L5814)
3. [bespoke_event_handling.rs](/codex/codex-rs/app-server/src/bespoke_event_handling.rs#L1)

重点关注：

- `set_listener(...)`
- `clear_listener()`
- `track_current_turn_event(...)`
- `ThreadStateManager::remove_listener(...)`
- `ThreadStateManager::remove_connection(...)`
- `ThreadStateManager::remove_thread_state(...)`

## 一句话总结

`thread_state.rs` 是 app-server 的线程运行时状态注册表。

它不实现线程业务本身，而是负责管理每个会话线程在服务器侧的监听器、订阅连接、活动 turn 快照，以及 interrupt / rollback / turn summary 这类临时控制状态。
