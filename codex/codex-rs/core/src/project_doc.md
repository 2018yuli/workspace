# `project_doc.rs` 源码说明

这份文件负责一件很具体的事：**把项目里的“项目级说明文档”找出来，读进来，拼成最终给模型使用的用户说明文本**。

在这个项目里，这类文档默认叫 `AGENTS.md`。如果配置里额外声明了备用文件名，也可以退而求其次去找别的文件。最终它不仅会读取文档内容，还会和已有的 `user_instructions`、技能说明、某些 feature 对应的附加提示一起合并，生成完整的 instructions。

如果你把这个模块想成一个流程，可以理解为：

1. 先确定“从哪里开始找项目文档”。
2. 再决定“哪些文件名算项目文档”。
3. 从项目根目录一路找到当前工作目录，把沿途命中的文档按顺序收集起来。
4. 按字节上限读取并拼接内容。
5. 最后再把这些内容和配置里的其他说明项合并成一份总说明。

---

## 这个文件的主要职责

`project_doc.rs` 主要负责三类事情：

1. **定义项目文档的规则**
   比如默认文件名是什么、优先级是什么、分隔符是什么。

2. **发现并读取项目文档**
   也就是从 `cwd` 出发，找到项目根目录，然后收集 `AGENTS.md`、`AGENTS.override.md` 或配置中的 fallback 文件。

3. **构造最终 instructions**
   把项目文档内容与 `Config` 中已有的用户说明、技能说明、JS REPL 说明、子 agent 说明等拼接起来。

---

## 主要结构

### 1. 常量

文件开头定义了几个关键常量：

- `HIERARCHICAL_AGENTS_MESSAGE`
  通过 `include_str!` 把 `hierarchical_agents_message.md` 编译进来。开启 `Feature::ChildAgentsMd` 时会追加到最终说明里。

- `DEFAULT_PROJECT_DOC_FILENAME`
  默认项目文档名：`AGENTS.md`。

- `LOCAL_PROJECT_DOC_FILENAME`
  本地覆盖文档名：`AGENTS.override.md`。
  它比 `AGENTS.md` 优先级更高，适合本地个性化说明。

- `PROJECT_DOC_SEPARATOR`
  当 `Config::user_instructions` 和项目文档同时存在时，两者中间插入：

```text
\n\n--- project-doc ---\n\n
```

这个分隔符的意义很直接：让上层的系统说明和项目文档边界清晰。

### 2. 生成附加说明的函数

- `render_js_repl_instructions(config: &Config) -> Option<String>`

这个函数专门负责在启用 `Feature::JsRepl` 时生成一段 JS REPL 使用说明。它不是查找项目文档的核心逻辑，但属于最终 instructions 的组成部分。

它会根据 feature 开关决定是否输出：

- 没启用 `JsRepl`：返回 `None`
- 启用 `JsRepl`：返回一段 Markdown 文本
- 额外启用 `JsReplToolsOnly`：再追加“不要直接调工具，要通过 `codex.tool(...)`”之类的规则

### 3. 最重要的三个函数

这个模块最核心的是下面三个函数：

- `get_user_instructions`
- `read_project_docs`
- `discover_project_doc_paths`

可以把它们理解成三层：

- `discover_project_doc_paths`：只负责“找路径”
- `read_project_docs`：负责“读内容”
- `get_user_instructions`：负责“和其他说明一起组装成最终结果”

---

## 核心函数说明

## `get_user_instructions`

签名：

```rust
pub(crate) async fn get_user_instructions(
    config: &Config,
    skills: Option<&[SkillMetadata]>,
) -> Option<String>
```

这是这个模块对外最像“总入口”的函数。

它做的事情是：

1. 调用 `read_project_docs(config).await` 读取项目文档。
2. 如果 `config.user_instructions` 已经存在，先放进输出字符串。
3. 如果项目文档读取成功且非空，就把它拼到后面。
4. 如果启用了 `JsRepl`，追加 JS REPL 说明。
5. 如果传入了技能列表，就调用 `render_skills_section` 追加技能说明。
6. 如果启用了 `Feature::ChildAgentsMd`，追加层级 agent 说明。
7. 如果最终字符串还是空的，就返回 `None`；否则返回 `Some(output)`。

### 这个函数的拼接顺序

顺序非常重要，最终内容是按下面的先后关系生成的：

1. `config.user_instructions`
2. 项目文档内容
3. JS REPL 说明
4. 技能说明
5. `HIERARCHICAL_AGENTS_MESSAGE`

也就是说，**项目文档不是唯一来源，它只是最终 instructions 的一个组成部分**。

### 异常处理方式

这里有一个值得注意的设计：

- `read_project_docs` 如果报错，`get_user_instructions` 不会直接把错误向上抛。
- 它会用 `tracing::error!` 记录日志，然后继续拼其他内容。

这说明作者的意图是：**项目文档读取失败不应该让整个 instructions 构造过程崩掉**，最多只是少了一部分上下文。

---

## `read_project_docs`

签名：

```rust
pub async fn read_project_docs(config: &Config) -> std::io::Result<Option<String>>
```

这个函数负责把项目文档“真正读出来”。

### 它的工作流程

#### 第一步：检查总字节限制

它先取出：

```rust
let max_total = config.project_doc_max_bytes;
```

如果这个值是 `0`，直接返回 `Ok(None)`。

这表示：

- 配置层明确允许“完全禁用项目文档”
- 而不是“没找到文档”

这是一个行为开关，不是异常场景。

#### 第二步：发现文档路径

它调用：

```rust
let paths = discover_project_doc_paths(config)?;
```

如果返回空列表，也直接 `Ok(None)`。

#### 第三步：按剩余预算逐个读取

它维护一个：

```rust
let mut remaining: u64 = max_total as u64;
```

然后按路径顺序依次处理文件：

- 如果剩余预算已经是 0，就停止
- 用 `tokio::fs::File::open` 异步打开文件
- 如果文件刚好在这一步不存在了：
  - `NotFound` 会被忽略，继续下一个
- 其他 I/O 错误：
  - 直接返回 `Err`

#### 第四步：按预算截断读取

这里用了一个很实用的写法：

```rust
let mut reader = tokio::io::BufReader::new(file).take(remaining);
```

意思是：**哪怕文件很大，也最多只读取剩余预算这么多字节**。

随后：

- 先通过 `metadata().len()` 获取原始文件大小
- 再 `read_to_end` 读取被 `take(remaining)` 限制过的内容
- 如果原始文件大小超过预算，就打一个 warning，说明发生了截断

#### 第五步：只保留非空文本

读出的字节会被转成：

```rust
String::from_utf8_lossy(&data).to_string()
```

这表示即使文件不是完全合法的 UTF-8，也尽量容错转换，不轻易失败。

然后它会检查：

```rust
if !text.trim().is_empty()
```

只有非空白内容才会加入结果列表，并消耗预算。

#### 第六步：最终拼接

如果最后 `parts` 为空，返回 `Ok(None)`。

否则：

```rust
Ok(Some(parts.join("\n\n")))
```

也就是多个项目文档之间用两个换行拼接。

### 这个函数的几个关键特点

#### 1. 总预算是“跨文件共享”的

不是每个文件都能读 `max_total`，而是所有文件一共只能读这么多字节。

#### 2. 按路径顺序读取，越靠前的文档优先级越高

因为预算是递减的，所以前面的文档可能会挤占后面文档的可读空间。

在本模块里，路径顺序是“从项目根到当前目录”，所以更高层的文档会先被读到。

#### 3. 文件丢失是可容忍的

发现路径和真正读取之间存在时间差，所以某个文件临时被删掉不会导致整体失败。

---

## `discover_project_doc_paths`

签名：

```rust
pub fn discover_project_doc_paths(config: &Config) -> std::io::Result<Vec<PathBuf>>
```

这个函数不读文件内容，只返回“应该去读哪些文件”的路径列表。

它是整个模块里规则最集中的地方。

### 工作流程拆解

#### 1. 先规范化 `cwd`

代码会先从：

```rust
let mut dir = config.cwd.clone();
```

开始，然后尝试：

```rust
if let Ok(canon) = normalize_path(&dir) {
    dir = canon;
}
```

这里用的是 `dunce::canonicalize` 的别名 `normalize_path`。

目的很简单：

- 尽量消除路径里的符号链接、相对段等差异
- 让后面的祖先遍历和路径比较更稳定

如果规范化失败，也不会报错退出，而是继续使用原始 `cwd`。

#### 2. 合并配置层，计算项目根标记

这一段稍微绕一点，但很关键。

它先创建一个空的 TOML：

```rust
let mut merged = TomlValue::Table(toml::map::Map::new());
```

然后遍历 `config.config_layer_stack`，按 **低优先级到高优先级** 合并配置层。

但它故意跳过：

```rust
ConfigLayerSource::Project { .. }
```

也就是说：**决定“项目根在哪里”的配置，不允许从项目配置文件本身读取**。

这是一个很有意图的设计，原因通常是：

- 你得先知道项目根，才能知道要不要读取项目配置
- 如果反过来依赖项目配置来定义项目根，会形成循环依赖

随后它调用：

- `project_root_markers_from_config(&merged)`
- 如果没有配置，使用 `default_project_root_markers()`
- 如果配置非法，打 warning，并回退到默认值

#### 3. 向上查找项目根目录

有了 marker 列表后，函数会从当前目录开始，沿祖先目录一路往上找。

对每个祖先目录，会检查每个 marker 是否存在：

```rust
ancestor.join(marker)
```

只要某个 marker 存在，这个祖先目录就被认定为 `project_root`。

默认 marker 通常是 `.git`，所以最常见的行为是：

- 在 Git 仓库中工作时，以仓库根目录作为项目根

几个边界行为也很明确：

- 如果 marker 列表为空：
  - 直接禁用向上遍历
  - 只把当前目录当作搜索范围
- 如果一路都没找到 marker：
  - 也只搜索当前目录

#### 4. 生成搜索目录列表

如果找到了项目根，就会构造：

- 从项目根
- 到当前工作目录
- 每一级目录都包含在内

比如：

```text
/repo
/repo/services
/repo/services/api
```

如果没找到项目根，则搜索目录列表只有一个：`cwd`。

#### 5. 为每个目录挑选文档文件

函数接着调用：

```rust
let candidate_filenames = candidate_filenames(config);
```

然后对每个目录按候选文件名顺序逐个检查。

一旦某个目录命中了一个候选文件，就：

- 把该路径加入结果
- `break`

这意味着：

- **每个目录最多只会选择一个项目文档文件**
- 同一目录下如果 `AGENTS.override.md` 存在，就不会再加入 `AGENTS.md`

#### 6. 允许符号链接

检查文件存在时，代码使用的是：

```rust
std::fs::symlink_metadata(&candidate)
```

并且接受：

- 普通文件
- 符号链接

注释里也写明了：悬空链接不在这里处理，后面真正打开文件时才会失败。

---

## `candidate_filenames`

签名：

```rust
fn candidate_filenames<'a>(config: &'a Config) -> Vec<&'a str>
```

这是一个小函数，但把“文件名优先级”定义得很清楚。

返回顺序是：

1. `AGENTS.override.md`
2. `AGENTS.md`
3. `config.project_doc_fallback_filenames` 里的自定义文件名

它还做了两件小事：

- 跳过空字符串
- 去重，避免重复候选名

所以可以得出明确结论：

- 本地覆盖文件永远优先
- 默认文件次之
- fallback 只在前两者都没命中时才有机会生效

---

## 主要工作流程

如果把整个模块串起来，完整流程如下。

### 场景一：系统要生成最终用户说明

入口一般是 `get_user_instructions(config, skills)`。

### 场景二：内部开始查找项目文档

`get_user_instructions` 会调用 `read_project_docs(config)`。

### 场景三：先找路径，再读内容

`read_project_docs` 会调用 `discover_project_doc_paths(config)`。

此时会发生：

1. 规范化 `cwd`
2. 根据非项目层配置得到 `project_root_markers`
3. 向上查找项目根
4. 构造从项目根到当前目录的搜索链
5. 每一级目录按优先级检查：
   - `AGENTS.override.md`
   - `AGENTS.md`
   - fallback 文件
6. 每个目录最多选一个文件

### 场景四：按预算读取文档

找到路径后，`read_project_docs` 会：

1. 依次打开文件
2. 按剩余字节预算读取
3. 自动截断超大文件
4. 跳过空白文档
5. 用空行拼接多个文档

### 场景五：合并其他说明来源

最后 `get_user_instructions` 再把这些文档内容和其他来源拼起来：

1. `config.user_instructions`
2. 项目文档
3. JS REPL 说明
4. Skills 说明
5. Child Agents 说明

如果最后什么都没有，就返回 `None`。

---

## 这个模块的设计重点

## 1. 查找规则是“分层继承”的

从项目根一路找到当前目录，而不是只看当前目录。这使得项目可以：

- 在仓库根目录放全局规则
- 在子目录放局部补充说明

最终形成类似“继承 + 局部覆盖”的效果，不过这里不是覆盖文本，而是**按路径顺序拼接**。

## 2. 同一层目录只取一个文件

虽然支持多个候选文件名，但每个目录一旦找到第一个匹配项就停止。这避免了：

- 同一个目录下的多份文档重复叠加
- 本地 override 和默认文档同时生效造成冲突

## 3. 项目根识别与项目配置解耦

查找项目根时忽略 `ConfigLayerSource::Project`，避免“要先找到项目根，才能读取项目配置；又要先读取项目配置，才能知道项目根”的循环问题。

## 4. 对运行时变化比较宽容

它允许以下情况尽量不中断：

- canonicalize 失败
- 某个候选文件在发现后被删掉
- 文件内容不是严格 UTF-8
- `project_root_markers` 配置非法

整体策略偏向“尽量产出结果”，而不是“一出问题就失败”。

---

## 测试覆盖了什么

文件底部的测试很多，基本把关键行为都锁住了。重点包括：

- 没有文档时返回 `None`
- 文档小于上限时原样返回
- 文档超过上限时会截断
- 嵌套目录下能找到仓库根目录的 `AGENTS.md`
- `project_doc_max_bytes = 0` 时彻底禁用项目文档
- `user_instructions` 和项目文档会通过固定分隔符拼接
- 根目录和当前目录的文档会按“从上到下”顺序拼接
- `project_root_markers` 配置会影响项目根识别
- `AGENTS.override.md` 优先于 `AGENTS.md`
- fallback 文件名会在默认文件缺失时生效
- 默认文件仍优先于 fallback
- skills 说明可以单独输出，也可以追加到项目文档后
- `Feature::Apps` 不会平白生成额外说明
- `Feature::JsRepl` / `Feature::JsReplToolsOnly` 会追加对应规则

从测试数量和粒度看，这个模块虽然逻辑不大，但行为约束其实写得很细。

---

## 和其他模块的关系

这个文件不是孤立存在的，它和几个模块关系很紧：

- `config`
  提供 `Config`、`project_doc_max_bytes`、`project_doc_fallback_filenames` 等配置项。

- `config_loader`
  提供配置层合并逻辑，以及项目根 marker 的默认值和解析函数。

- `skills`
  提供 `render_skills_section`，用于把技能信息追加到最终 instructions。

- `features`
  提供 feature 开关，控制是否注入 JS REPL 说明和 Child Agents 说明。

- `tui/src/status/helpers.rs`
  会调用 `discover_project_doc_paths` 来展示当前命中的文档路径列表，说明这个“发现路径”的逻辑不仅服务于 prompt 构造，也服务于 UI 状态展示。

---

## 一句话总结

`project_doc.rs` 的本质就是一个“项目说明文档装配器”：

- 它先确定项目根
- 再按目录层级发现项目说明文件
- 按优先级和字节预算读取内容
- 最后把项目文档和其他说明源拼成统一的 instructions

如果你要修改这个模块，最值得先搞清楚的是三件事：

1. 路径发现顺序会不会变。
2. 同目录候选文件的优先级会不会变。
3. 最终 instructions 的拼接顺序会不会变。

这三点基本决定了它的外部行为。
