# sdoc

`sdoc` 是一个离线、可扩展的源码架构文档生成器。

给定任意**源码相对路径**，例如：

```bash
sdoc generate codex/codex-rs/core/src/context_manager/mod.rs --project-root /path/to/repo
```

工具会自动扫描该文件所在目录下的源码，并将文档写到相同目录下的 `mod.md`。

## 功能

- 接受源码相对路径并自动生成同目录 Markdown 文档
- 优先支持 Rust，同时内置 Python / JavaScript / TypeScript / Java / Go
- 若入口文件扩展名不支持，会**明确报错**
- 自动提取关键结构体/类、主要函数、导入关系、局部调用链
- 结合注释、命名、README、manifest 推断业务意图
- 自动输出：执行摘要、关键结构表、主流程步骤、Mermaid 流程图、难点类比解释、示例代码片段
- 支持 CLI + Python 库接口
- 支持缓存、并发解析、可配置模板参数、单元测试

## 安装

建议在 Python 3.11+ 环境中安装：

```bash
pip install -e .
```

## CLI 用法

```bash
sdoc generate codex/codex-rs/core/src/context_manager/mod.rs \
  --project-root /path/to/repo \
  --depth 1 \
  --max-files 100 \
  --max-snippets 3
```

输出示例：

```text
已生成: /path/to/repo/codex/codex-rs/core/src/context_manager/mod.md
分析文件数: 4
缓存命中: 2
```

查看当前生效配置：

```bash
sdoc print-config codex/codex-rs/core/src/context_manager/mod.rs
```

输出 JSON 摘要：

```bash
sdoc generate codex/codex-rs/core/src/context_manager/mod.rs --json
```

## 作为库调用

```python
from sdoc import generate_document

result = generate_document(
    "codex/codex-rs/core/src/context_manager/mod.rs",
    overrides={
        "project_root": "/path/to/repo",
        "recursive_depth": 1,
        "enable_cache": True,
    },
)

print(result.output_file)
print(result.markdown[:200])
```

## 默认配置

可在项目根目录提供 `sdoc.toml`：

```toml
[sdoc]
project_root = "."
recursive_depth = 1
enable_cache = true
cache_file = ".sdoc-cache.json"
template_title_suffix = "代码架构文档"
```

## 输出文档结构

生成的 Markdown 默认包含：

- 执行摘要
- 功能定位与业务说明
- 关键业务概念
- 关键结构与职责表
- 主流程步骤
- Mermaid 流程图
- 模块关系
- 难点类比解释
- 示例代码片段
- 生成信息

## 质量优化策略

`sdoc` 默认实现了以下提质策略：

1. **AST 优先**：核心符号提取尽量基于 Tree-sitter 语法树，而不是纯正则。
2. **注释优先**：若代码已有注释或 docstring，优先把这些注释作为业务描述基础。
3. **上下文聚合**：会补充读取邻近 `README`、`Cargo.toml`、`pyproject.toml`、`package.json` 等文件中的说明。
4. **局部调用链**：对本目录内已识别函数做局部调用匹配，帮助组织主流程。
5. **命名约定推断**：对 `Manager / Service / Builder / Registry / Context` 等名称做职责提示。
6. **难点类比库**：对异步、缓存、抽象层、状态流转、上下文传递、语法树等模式生成通俗类比。
7. **并发解析**：多文件目录使用线程池并发解析。
8. **缓存复用**：按文件内容哈希缓存分析结果，避免重复解析未变更文件。
9. **可扩展语言解析器**：通过 `LANGUAGE_SPECS` 注册新语言。
10. **可配置输出规模**：可控制扫描深度、最大文件数、片段数量等，避免文档失控膨胀。

## 运行测试

```bash
python -m unittest discover -s tests -v
```

## 扩展新语言

在 `src/sdoc/analysis.py` 中：

1. 增加新的 `LanguageSpec`
2. 配置对应 Tree-sitter Python 绑定包
3. 定义语法节点规则 `Rule`
4. 补充导入语句匹配模式
5. 如有需要，补充 `extract_name` 与 `normalize_kind` 中的特例逻辑

## 限制

- 当前调用链分析是“目录内局部静态近似”，不是全项目精确调用图
- 对宏、反射、动态派发、运行时注入做的是保守推断
- 默认更适合生成“面向初学者的架构阅读文档”，而不是形式化 API 参考手册
