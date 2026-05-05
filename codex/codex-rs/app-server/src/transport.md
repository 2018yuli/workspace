# `transport.rs` 是干嘛的

[transport.rs](/codex/codex-rs/app-server/src/transport.rs#L1) 是 `app-server` 的传输层模块。

它负责解决的不是“业务请求该怎么处理”，而是更靠外层的问题：

- app-server 通过什么方式和客户端连通
- 客户端发来的 JSON-RPC 消息怎么进入内部处理循环
- 服务端生成的消息怎么发回对应连接
- 队列满了怎么办
- WebSocket 慢连接、断连、Ping/Pong 怎么处理

一句话说，它是 app-server 的“连接与消息收发基础设施”。

## 这个模块的定位

如果把 `app-server` 拆成几层，大致可以这样看：

1. `transport.rs`
   - 负责连线、读写、连接生命周期、消息收发
2. `message_processor.rs`
   - 负责 JSON-RPC 请求分发和 session 级校验
3. `codex_message_processor.rs`
   - 负责 thread / turn / review / config 等具体业务

所以 `transport.rs` 的边界很清晰：

- 它不决定 `thread/start` 是怎么实现的
- 它只负责把请求可靠地送进去，再把结果发回来

## 它支持哪些传输方式

`AppServerTransport` 定义了两种模式：

- `Stdio`
- `WebSocket { bind_address }`

对应的 listen URL 规则是：

- `stdio://`
  - 默认方式
- `ws://IP:PORT`
  - WebSocket 方式

这个解析逻辑在 `AppServerTransport::from_listen_url(...)` 里。

注意这里的 WebSocket 只接受 `IP:PORT`，不接受 `localhost:1234` 这种 hostname。

## 这个模块里最重要的抽象

### `TransportEvent`

这是传输层发给 processor loop 的内部事件类型，包含三种：

- `ConnectionOpened`
- `ConnectionClosed`
- `IncomingMessage`

也就是说，传输层不会直接处理业务请求，它只是把外界变化翻译成内部事件丢给上层。

这是整个模块最核心的解耦点。

### `ConnectionState`

这是 processor loop 持有的“连接入站状态”。

它包含：

- `outbound_initialized`
- `outbound_experimental_api_enabled`
- `outbound_opted_out_notification_methods`
- `session`

这里的关键点是：

- processor 负责更新 session 状态
- outbound loop 需要知道一部分状态来决定要不要发消息
- 两边通过共享的 `Arc<AtomicBool>` / `Arc<RwLock<_>>` 协调

所以 `ConnectionState` 本质上是“processor 侧持有、并向 outbound 暴露部分状态”的连接上下文。

### `OutboundConnectionState`

这是 outbound loop 持有的“连接出站状态”。

它包含：

- 当前连接的 writer channel
- initialized 标记
- experimental API 标记
- opted-out notification methods
- 可选的 disconnect token

它的职责是：让 outbound router 在发消息时，知道某个连接现在是否还能发、该发什么、是否应该被断开。

## stdio 模式怎么工作

`start_stdio_connection(...)` 会创建一个固定的单连接：

- `connection_id = 0`

然后启动两个任务：

1. stdin reader
2. stdout writer

### stdin reader 做什么

它逐行读取 stdin，把每一行都当作一条 JSON-RPC 消息：

- 调用 `forward_incoming_message(...)`
- 解析成 `JSONRPCMessage`
- 再封装成 `TransportEvent::IncomingMessage`

如果 stdin EOF 或读取失败：

- 发 `ConnectionClosed`
- reader 退出

### stdout writer 做什么

它从 `writer_rx` 收取 `OutgoingMessage`：

- 序列化成 JSON
- 追加换行
- 写到 stdout

因为 stdio 是单客户端、单连接模型，所以这里不用考虑慢连接断开策略，写失败基本就意味着连接结束。

## WebSocket 模式怎么工作

WebSocket 逻辑比 stdio 更复杂，因为它要支持多连接和显式断开控制。

### `start_websocket_acceptor(...)`

这个函数负责：

- 绑定监听地址
- 打印启动 banner
- 接收新 TCP 连接
- 为每个连接分配新的 `ConnectionId`
- 启动 `run_websocket_connection(...)`

这里使用 `AtomicU64` 给 websocket 连接分配递增 id。

### `run_websocket_connection(...)`

这是单个 websocket 连接的生命周期控制器。

它会：

1. 完成 websocket handshake
2. 创建该连接的 writer channel
3. 向 processor 发送 `ConnectionOpened`
4. 把 websocket split 成 reader / writer
5. 启动两个任务：
   - `run_websocket_outbound_loop(...)`
   - `run_websocket_inbound_loop(...)`
6. 任一任务退出时，取消另一个
7. 最后发送 `ConnectionClosed`

这就是典型的“双向异步连接拆分模型”。

### `run_websocket_inbound_loop(...)`

入站 loop 负责：

- 读取文本帧
- 解析 JSON-RPC
- 转发成 `IncomingMessage`
- 处理 `Ping` / `Pong`
- 忽略或拒绝不支持的帧类型

具体行为：

- `Text`
  - 作为 JSON-RPC 消息处理
- `Ping`
  - 尝试通过 control queue 回 `Pong`
- `Pong`
  - 忽略
- `Close`
  - 结束连接
- `Binary`
  - 记录 warning，不支持

这里专门用了一个 `writer_control_tx` 来发送 `Pong` 等控制帧，而不是和普通业务消息混在一起。

### `run_websocket_outbound_loop(...)`

出站 loop 负责两类输出：

- `writer_control_rx`
  - WebSocket 控制帧，例如 `Pong`
- `writer_rx`
  - 普通 `OutgoingMessage`

两者通过 `tokio::select!` 合并处理。

如果连接被取消、writer 关闭或发送失败，就退出。

## 入站消息怎么进入 processor

### `forward_incoming_message(...)`

这个函数做的事情很简单：

- 把原始字符串反序列化为 `JSONRPCMessage`
- 成功则进入 `enqueue_incoming_message(...)`
- 失败则记录日志

注意：反序列化失败不会主动断开连接，只是丢弃该消息。

### `enqueue_incoming_message(...)`

这是传输层里很重要的一块，因为它实现了入站背压策略。

它会先尝试：

- `transport_event_tx.try_send(event)`

然后根据结果分情况处理。

#### 情况 1：成功

- 消息直接进入 processor 队列

#### 情况 2：channel 已关闭

- 返回 `false`
- 调用方通常会结束对应连接处理

#### 情况 3：队列满，且消息是 request

这是最关键的 overload 分支。

如果当前入站消息是 JSON-RPC request，且 processor 队列已满：

- 不阻塞等待
- 直接给客户端回一个 JSON-RPC error
- 错误码是 `OVERLOADED_ERROR_CODE`
- 消息是 `"Server overloaded; retry later."`

这是一种明确的“可重试”背压反馈机制。

#### 情况 4：队列满，但不是 request

比如 notification 等情况：

- 会退化成异步 `send(event).await`

也就是必要时等待容量释放。

这说明模块对“可回应的请求”和“其他消息”做了不同优先级策略。

## 出站消息怎么发回客户端

### `route_outgoing_envelope(...)`

这是传输层的总出站路由入口。

它处理两类 envelope：

- `ToConnection`
  - 定向发给某个连接
- `Broadcast`
  - 广播给所有已初始化连接

广播时还会额外检查：

- 连接是否 initialized
- 连接是否 opt-out 了该通知方法

### `send_message_to_connection(...)`

这是单连接发送逻辑的核心。

发送前会做三件事：

1. 找到连接
2. 用 `filter_outgoing_message_for_connection(...)` 做协议裁剪
3. 用 `should_skip_notification_for_connection(...)` 判断是否应跳过

然后根据连接类型决定发送策略。

#### 对可断开的连接

主要是 websocket 连接。

这里优先用：

- `writer.try_send(message)`

如果队列满了：

- 认为这是 slow connection
- 记录 warning
- 主动断开该连接

这是一种很明确的策略：

- 不让单个慢 websocket 连接拖垮整个服务

#### 对不可断开的连接

主要是 stdio 连接。

这里用：

- `writer.send(message).await`

因为 stdio 是主连接，不适合用“队列满就踢掉”的策略。

## 通知过滤和能力裁剪

### `should_skip_notification_for_connection(...)`

客户端在 `initialize` 时可以声明 `optOutNotificationMethods`。

这个函数会检查：

- 当前出站消息是不是某种 notification
- 它的方法名是否在该连接的 opt-out 集合里

如果在，就跳过发送。

这让每个连接可以按自己能力或需求抑制部分事件流。

### `filter_outgoing_message_for_connection(...)`

这个函数用来做“按连接能力降级”。

当前代码里比较典型的是：

- 如果连接没有启用 experimental API
- 那么 `CommandExecutionRequestApproval` 里的实验字段会被 strip 掉

这说明 transport 层不只是“搬运消息”，也负责最后一层按连接能力裁剪协议形态。

## 连接断开是怎么处理的

### `disconnect_connection(...)`

这个函数做的事情很直接：

- 从连接表里移除连接
- 调用其 `disconnect_token.cancel()`

只要有慢连接、writer 关闭、显式断开等情况，最终都会走到这里或等价逻辑。

### `OutboundConnectionState::request_disconnect()`

这是对具体连接发起断开的封装，主要用于 websocket。

stdio 没有 `disconnect_sender`，所以不能像 websocket 那样被显式 cancel。

## 它和 `lib.rs` 是怎么配合的

理解这个模块最关键的一点，是它本身不是一个完整 server，它只是 `lib.rs` 的传输子系统。

在 [lib.rs](/codex/codex-rs/app-server/src/lib.rs#L300) 里，整体运行时被拆成两个主要循环：

### processor loop

职责：

- 接收 `TransportEvent`
- 维护 `ConnectionState`
- 调用 `MessageProcessor`
- 更新 initialized / experimental API / opt-out 状态

### outbound loop

职责：

- 接收 `OutgoingEnvelope`
- 维护 `OutboundConnectionState`
- 调用 `route_outgoing_envelope(...)`

两者之间通过 channel 解耦。

这意味着：

- 入站处理不会直接阻塞出站写入
- 慢连接问题主要被局部隔离在 outbound loop
- 连接状态可以分成“处理请求用的状态”和“发消息用的状态”

这个设计是 `transport.rs` 的核心价值之一。

## 它的背压策略很重要

这个模块最有工程味道的部分，其实是背压策略：

- 入站 processor 队列有上限：`CHANNEL_CAPACITY = 128`
- request 队列满时直接回 overload 错误
- websocket 出站队列满时直接断开慢连接
- stdio 不用这个策略，而是等待写出

这几条组合起来，目标非常明确：

- 优先保护服务整体可用性
- 不让局部阻塞扩散
- 对客户端给出明确的重试语义

## 它不做什么

这个模块不负责：

- JSON-RPC 方法语义
- thread / turn 业务逻辑
- 认证逻辑
- 配置逻辑
- 历史持久化

它的职责很收敛：

- 接住连接
- 搬运消息
- 控制队列
- 处理慢客户端和断连

## 建议怎么读

如果你要继续读源码，建议顺序是：

1. [transport.rs](/codex/codex-rs/app-server/src/transport.rs#L1)
2. [lib.rs](/codex/codex-rs/app-server/src/lib.rs#L319)
3. [message_processor.rs](/codex/codex-rs/app-server/src/message_processor.rs#L1)

优先关注这些函数：

- `start_stdio_connection(...)`
- `start_websocket_acceptor(...)`
- `run_websocket_connection(...)`
- `enqueue_incoming_message(...)`
- `send_message_to_connection(...)`
- `route_outgoing_envelope(...)`

## 一句话总结

`transport.rs` 是 app-server 的消息收发层。

它把 `stdio` 和 `websocket` 统一成同一套 `TransportEvent` / `OutgoingEnvelope` 模型，负责连接生命周期、入站背压、出站路由、慢连接处理以及按连接能力过滤消息。
