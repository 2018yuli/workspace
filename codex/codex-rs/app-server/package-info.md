# `codex-rs/app-server` 这个包是干嘛的

`codex/codex-rs/app-server` 是 Codex 的“应用服务器”包。

它的作用不是直接实现模型推理本身，而是把 `codex-core` 里的能力包装成一个可连接、可编程、可流式消费的服务接口，供外部客户端使用，比如：

- Codex VS Code 扩展
- 其他 IDE 集成
- 本地桌面应用
- 需要通过 JSON-RPC 驱动 Codex 的自动化工具

一句话说，这个包是 Codex 的“服务端接入层”。

## 它解决什么问题

`codex-core` 提供了线程、回合、认证、配置、工具执行等核心能力，但这些能力本身更偏内部运行逻辑。

`app-server` 负责把这些内部能力变成一个稳定的对外接口：

- 接收客户端请求
- 校验连接初始化状态
- 把请求路由到对应的处理逻辑
- 把执行过程中的事件流式发回客户端
- 管理连接、线程状态和通知订阅

所以它的定位类似：

- “Codex 的本地 RPC 服务器”
- 或者“Codex rich client 的后端桥接层”

## 它提供什么能力

从包内结构和测试覆盖看，这个包主要对外暴露这些能力：

- 线程管理
  - 新建、恢复、分叉、归档、反归档、读取、列出线程
- 回合驱动
  - 启动一个 turn、插入 steer 输入、中断 turn、review
- 事件流
  - 把 agent message、工具调用、命令执行、文件修改、plan 更新等过程事件实时发给客户端
- 认证桥接
  - 接入 `AuthManager`
  - 支持外部 ChatGPT token 刷新回调
- 配置接口
  - 读取配置
  - 写入单个配置项或批量配置
  - 重新加载 MCP 配置
- 模型与功能发现
  - 列出模型、实验功能、协作模式、技能、应用
- 独立命令执行
  - 不开启完整线程/turn，直接跑 `command/exec`
- 平台辅助能力
  - fuzzy file search
  - Windows sandbox setup
  - external agent config 检测与导入
  - feedback 上传

## 它在整体架构里的位置

可以把这个包理解成下面这一层：

1. 底层是 `codex-core`
   - 真正的线程、认证、配置、agent 执行逻辑都在这里
2. 中间是 `app-server`
   - 把这些能力封装成 JSON-RPC API
   - 处理连接、请求分发、事件转发、会话状态
3. 最上层是客户端
   - VS Code 扩展、桌面端、其他集成

所以 `app-server` 本身不是业务核心的唯一来源，它更像一个“对外暴露内核能力的壳”。

## 这个包里的关键模块

### `src/lib.rs`

入口和运行时装配层。

它负责：

- 初始化日志
- 加载配置
- 选择传输方式
- 启动 processor loop 和 outbound loop
- 管理连接打开/关闭
- 处理优雅重启和 Ctrl-C drain

如果你想知道“这个服务怎么启动起来”，先看这里。

### `src/transport.rs`

传输层。

它负责：

- 支持 `stdio` 和 `websocket` 两种连接方式
- 把入站 JSON-RPC 消息转换成内部 `TransportEvent`
- 管理每个连接的 writer 和断开逻辑
- 控制有界队列和背压行为

这个文件解决的是“消息怎么进来、怎么出去”。

### `src/message_processor.rs`

应用层请求分发入口。

它负责：

- 接收 JSON-RPC request / notification
- 校验连接是否已 `initialize`
- 处理一部分通用 API
- 创建并持有 `CodexMessageProcessor`
- 接入 `AuthManager`、`ThreadManager`、`ConfigApi`

这个模块更像总调度器。

### `src/codex_message_processor.rs`

核心业务请求处理器。

这是包里最重的模块之一，主要负责：

- `thread/*`
- `turn/*`
- `review/start`
- `model/list`
- `skills/*`
- `app/list`
- 以及大量和 Codex agent 生命周期有关的请求

如果你关心“具体某个 app-server API 是怎么实现的”，大概率要读这个文件。

### `src/bespoke_event_handling.rs`

事件整形与协议适配层。

`codex-core` 内部事件和 app-server 对外通知并不是一一直接对应的，这个模块负责：

- 把内部事件转成客户端可消费的通知
- 处理 item started/completed、delta、plan update、approval response 等细节
- 组装 turn 完成和中断时的最终通知

它解决的是“内部事件怎么翻译成客户端协议事件”。

### `src/outgoing_message.rs`

出站消息基础设施。

它负责：

- 封装服务端发给客户端的消息
- 管理 connection id / request id
- 支持服务端主动发 request
- 跟踪响应回流

这是服务端主动和客户端交互的重要基础层。

### `src/thread_state.rs` 和 `src/thread_status.rs`

线程状态管理。

它们负责：

- 跟踪当前已加载线程
- 管理 thread status 变化
- 把状态变化广播给连接

### `src/config_api.rs`

配置 API 处理层。

它负责读写 `config.toml` 以及相关配置接口，不把这些逻辑塞进主 processor。

### `src/external_agent_config_api.rs`

外部 agent 配置迁移接口。

它负责检测和导入外部 agent 生态的可迁移配置。

### `src/models.rs`、`src/dynamic_tools.rs`、`src/fuzzy_file_search.rs`

这些属于辅助能力模块，分别处理：

- 模型展示/适配
- 动态工具定义
- 文件模糊搜索会话

## 它怎么和认证系统协作

这个包不自己实现认证底层逻辑，而是依赖 `codex-core::AuthManager`。

在 [src/message_processor.rs](/codex/codex-rs/app-server/src/message_processor.rs#L1) 里可以看到：

- `MessageProcessor` 启动时会创建 `AuthManager`
- 同时会注入一个 `ExternalAuthRefreshBridge`

这个 bridge 的作用是：

- 当 `codex-core` 发现外部 ChatGPT token 需要刷新时
- 不直接自己刷新
- 而是通过 app-server 向上层客户端发起一个 refresh 请求
- 等客户端返回新的 token，再继续流程

这说明 `app-server` 也是认证系统和宿主应用之间的桥梁。

## 它的协议是什么

这个包主要通过 JSON-RPC 风格协议对外通信。

支持两种传输：

- `stdio://`
  - 默认方式，适合本地子进程集成
- `ws://IP:PORT`
  - WebSocket，当前是实验性能力

但要注意，这个包的重点不只是“收发 JSON”，而是围绕 Codex 的会话模型，维护：

- connection
- thread
- turn
- item
- notification stream

所以它比一个简单 RPC server 更像“长连接会话服务器”。

## 什么不属于这个包

为了避免误解，也可以反过来看：

这个包一般不负责：

- 模型底层调用策略本身
- token 持久化实现细节
- thread/turn 的最底层业务实现
- 核心 agent 执行引擎

这些主要在 `codex-core` 或其他底层 crate 中。

`app-server` 的重点是“暴露”和“协调”，不是“承载所有底层逻辑”。

## 适合什么场景

这个包适合用于：

- 需要把 Codex 嵌入到 IDE / GUI / 桌面端
- 希望通过编程接口驱动会话、读事件流、管理线程
- 需要外部应用控制认证、配置或工具调用

如果只是终端里直接运行 Codex CLI，本身不一定会直接感知这个包；但很多 richer client experience 都依赖它。

## 建议怎么读

如果你要理解这个包，建议按这个顺序：

1. [src/lib.rs](/codex/codex-rs/app-server/src/lib.rs#L1)
2. [src/transport.rs](/codex/codex-rs/app-server/src/transport.rs#L1)
3. [src/message_processor.rs](/codex/codex-rs/app-server/src/message_processor.rs#L1)
4. [src/codex_message_processor.rs](/codex/codex-rs/app-server/src/codex_message_processor.rs#L1)
5. [src/bespoke_event_handling.rs](/codex/codex-rs/app-server/src/bespoke_event_handling.rs#L1)

这样会先看到服务是怎么跑起来的，再看到请求怎么分发，最后再看复杂的业务处理和事件翻译。

## 一句话总结

`codex-rs/app-server` 是 Codex 面向 rich client 的本地应用服务器。

它把 `codex-core` 的线程、回合、认证、配置和工具执行能力包装成可连接的 JSON-RPC 服务，并负责连接管理、事件流转发、请求分发以及和外部客户端的交互桥接。
