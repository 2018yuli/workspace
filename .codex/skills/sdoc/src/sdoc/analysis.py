from __future__ import annotations

import importlib
import json
import logging
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, Optional, Sequence

from .config import SdocConfig
from .errors import ParserDependencyError
from .models import DifficultyNote, FileAnalysis, FlowStep, ParseTask, Symbol

logger = logging.getLogger(__name__)


COMMENT_PREFIXES = {
    "rust": ["///", "//!", "//"],
    "python": ["#"],
    "javascript": ["///", "//"],
    "typescript": ["///", "//"],
    "java": ["///", "//"],
    "go": ["///", "//"],
}


@dataclass(slots=True)
class Rule:
    node_type: str
    kind: str
    name_fields: tuple[str, ...] = ("name",)
    body_fields: tuple[str, ...] = ("body",)


@dataclass(slots=True)
class LanguageSpec:
    name: str
    module_name: str
    language_attr: str
    rules: tuple[Rule, ...]
    import_patterns: tuple[str, ...]
    public_markers: tuple[str, ...] = ("pub ", "public ", "export ")
    method_kinds: tuple[str, ...] = ("function", "method", "constructor")
    jsx_like: bool = False

    def load_language(self) -> Any:
        try:
            tree_sitter = importlib.import_module("tree_sitter")
            module = importlib.import_module(self.module_name)
        except ModuleNotFoundError as exc:  # pragma: no cover - 集成环境路径
            raise ParserDependencyError(
                f"缺少解析依赖: {exc.name}。请先安装 tree-sitter 及 {self.module_name}。"
            ) from exc
        language_factory = getattr(module, self.language_attr)
        return tree_sitter.Language(language_factory())

    def create_parser(self) -> Any:
        try:
            tree_sitter = importlib.import_module("tree_sitter")
        except ModuleNotFoundError as exc:  # pragma: no cover
            raise ParserDependencyError("缺少 tree-sitter 依赖。") from exc
        language = self.load_language()
        return tree_sitter.Parser(language)


LANGUAGE_SPECS: Dict[str, LanguageSpec] = {
    "rust": LanguageSpec(
        name="rust",
        module_name="tree_sitter_rust",
        language_attr="language",
        rules=(
            Rule("struct_item", "struct"),
            Rule("enum_item", "enum"),
            Rule("trait_item", "trait"),
            Rule("impl_item", "impl", name_fields=("trait", "type"), body_fields=("body",)),
            Rule("function_item", "function"),
            Rule("const_item", "const"),
            Rule("type_item", "type_alias"),
            Rule("mod_item", "module"),
        ),
        import_patterns=(
            r"\buse\s+([^;]+);",
            r"\bmod\s+([A-Za-z_][A-Za-z0-9_]*)\s*;",
        ),
        public_markers=("pub ", "pub(",),
    ),
    "python": LanguageSpec(
        name="python",
        module_name="tree_sitter_python",
        language_attr="language",
        rules=(
            Rule("class_definition", "class"),
            Rule("function_definition", "function"),
        ),
        import_patterns=(
            r"\bfrom\s+([A-Za-z0-9_\.]+)\s+import\b",
            r"\bimport\s+([A-Za-z0-9_\.,\s]+)",
        ),
        public_markers=("def ", "class "),
    ),
    "javascript": LanguageSpec(
        name="javascript",
        module_name="tree_sitter_javascript",
        language_attr="language",
        rules=(
            Rule("class_declaration", "class"),
            Rule("function_declaration", "function"),
            Rule("method_definition", "method"),
        ),
        import_patterns=(
            r"\bimport\s+(?:[^\n]*?from\s+)?['\"]([^'\"]+)['\"]",
            r"\brequire\(['\"]([^'\"]+)['\"]\)",
            r"\bexport\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]",
        ),
        public_markers=("export ",),
        jsx_like=True,
    ),
    "typescript": LanguageSpec(
        name="typescript",
        module_name="tree_sitter_typescript",
        language_attr="language_typescript",
        rules=(
            Rule("class_declaration", "class"),
            Rule("interface_declaration", "interface"),
            Rule("enum_declaration", "enum"),
            Rule("type_alias_declaration", "type_alias"),
            Rule("function_declaration", "function"),
            Rule("method_definition", "method"),
        ),
        import_patterns=(
            r"\bimport\s+(?:[^\n]*?from\s+)?['\"]([^'\"]+)['\"]",
            r"\brequire\(['\"]([^'\"]+)['\"]\)",
            r"\bexport\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]",
        ),
        public_markers=("export ", "public "),
        jsx_like=True,
    ),
    "java": LanguageSpec(
        name="java",
        module_name="tree_sitter_java",
        language_attr="language",
        rules=(
            Rule("class_declaration", "class"),
            Rule("interface_declaration", "interface"),
            Rule("enum_declaration", "enum"),
            Rule("record_declaration", "record"),
            Rule("constructor_declaration", "constructor"),
            Rule("method_declaration", "method"),
        ),
        import_patterns=(r"\bimport\s+([A-Za-z0-9_\.\*]+);",),
        public_markers=("public ", "protected "),
    ),
    "go": LanguageSpec(
        name="go",
        module_name="tree_sitter_go",
        language_attr="language",
        rules=(
            Rule("type_spec", "type"),
            Rule("function_declaration", "function"),
            Rule("method_declaration", "method"),
        ),
        import_patterns=(
            r'"([A-Za-z0-9_\-/\.]+)"',
        ),
        public_markers=tuple(),
    ),
}


_ROLE_RULES = [
    (re.compile(r"manager$", re.I), "承担总控与协调职责，像一个总调度台。"),
    (re.compile(r"service$", re.I), "更像对外提供能力的业务服务层。"),
    (re.compile(r"controller$", re.I), "更像接收输入并分发动作的入口层。"),
    (re.compile(r"context", re.I), "负责维护上下文或运行现场，像工作台上的共享白板。"),
    (re.compile(r"builder$", re.I), "负责按步骤组装结果，像流水线装配工位。"),
    (re.compile(r"factory$", re.I), "负责统一创建对象，像生产线出厂口。"),
    (re.compile(r"registry$", re.I), "负责登记与查找映射，像通讯录或索引表。"),
    (re.compile(r"cache", re.I), "承担缓存与复用职责，目的是减少重复计算。"),
    (re.compile(r"parser|lexer", re.I), "承担语法拆解或输入解析职责，像把原材料先分门别类。"),
    (re.compile(r"resolver", re.I), "负责把名字、引用或依赖解析到具体目标。"),
    (re.compile(r"scheduler|queue", re.I), "负责排队、择时或调度，像任务分发中心。"),
]


_DIFFICULTY_RULES = [
    (
        re.compile(r"async|await|tokio|futures|goroutine|channel|thread", re.I),
        DifficultyNote(
            title="并发/异步流程",
            explanation="代码可能不是按单线程直线往下跑，而是把等待 I/O 或耗时操作拆出去并行推进。",
            analogy="可以把它想成餐厅里同时处理点单、后厨出餐、叫号取餐，顾客看到的是一个流程，内部其实是多个环节协同。",
        ),
    ),
    (
        re.compile(r"cache|memo|lru|store", re.I),
        DifficultyNote(
            title="缓存与复用",
            explanation="这类代码会优先复用已算过的数据，以减少重复昂贵操作。",
            analogy="就像图书馆先查索引卡片，找到馆藏位置再取书，而不是每次都从头翻遍整馆。",
        ),
    ),
    (
        re.compile(r"trait|interface|abstract|generic|where\s|impl<|<T|<K|<V", re.I),
        DifficultyNote(
            title="抽象层与泛型",
            explanation="代码强调“约定优先”，先定义一套接口或能力，再让不同实现去接入。",
            analogy="可以把它理解成插座标准：先规定插头接口，具体接电风扇还是电饭煲并不重要。",
        ),
    ),
    (
        re.compile(r"state|status|phase|stage|transition", re.I),
        DifficultyNote(
            title="状态流转",
            explanation="逻辑不是一次完成，而是在多个状态之间逐步推进，每一步可走的分支不同。",
            analogy="像订单从“待支付、待发货、运输中、已签收”逐步流转，每个阶段允许的动作都不同。",
        ),
    ),
    (
        re.compile(r"context|scope|session|env", re.I),
        DifficultyNote(
            title="上下文传递",
            explanation="部分信息不会直接写死在函数里，而是通过上下文对象逐层传递。",
            analogy="像会议中共享的白板，后续所有参与者都从这块白板读取当前背景信息。",
        ),
    ),
    (
        re.compile(r"parse|syntax|ast|tree-sitter|token", re.I),
        DifficultyNote(
            title="语法树与解析过程",
            explanation="代码在处理文本时，通常会先把文本拆成结构化节点，再基于这些节点做判断。",
            analogy="像先把一段文章拆成标题、段落、句子和词，再去理解整篇文章，而不是直接在原文上乱抓关键字。",
        ),
    ),
]


_IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def walk_tree(root: Any) -> Iterator[Any]:
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        children = getattr(node, "children", [])
        stack.extend(reversed(children))


def node_text(source_text: str, node: Any) -> str:
    return source_text[node.start_byte : node.end_byte]


def first_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line
    return ""


def compact(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text


def extract_name(node: Any, rule: Rule, text: str, language: str) -> str:
    for field_name in rule.name_fields:
        child = node.child_by_field_name(field_name)
        if child is not None:
            value = compact(node_text(text, child))
            if value:
                return value

    if language == "python" and node.type in {"class_definition", "function_definition"}:
        children = [child for child in getattr(node, "children", []) if child.is_named]
        if len(children) >= 2:
            return compact(node_text(text, children[1]))

    if language in {"javascript", "typescript"} and node.type == "method_definition":
        for child in getattr(node, "children", []):
            if child.type in {"property_identifier", "identifier", "private_property_identifier"}:
                return compact(node_text(text, child))

    if language == "java" and node.type in {"method_declaration", "constructor_declaration"}:
        for child in getattr(node, "children", []):
            if child.type in {"identifier"}:
                return compact(node_text(text, child))

    if language == "go" and node.type == "type_spec":
        children = [child for child in getattr(node, "children", []) if child.is_named]
        if children:
            return compact(node_text(text, children[0]))

    candidates = []
    for child in getattr(node, "children", []):
        if child.type in {"identifier", "type_identifier", "field_identifier", "property_identifier"}:
            candidates.append(compact(node_text(text, child)))
    return candidates[0] if candidates else f"<{node.type}>"


def normalize_kind(node: Any, rule: Rule, text: str, language: str) -> str:
    kind = rule.kind
    if language == "go" and node.type == "type_spec":
        body = compact(node_text(text, node))
        if "interface" in body:
            return "interface"
        if "struct" in body:
            return "struct"
        if body.startswith("type "):
            return "type_alias"
    if language == "rust" and node.type == "impl_item":
        name = extract_name(node, rule, text, language)
        return "impl" if " for " not in name else "trait_impl"
    return kind


def extract_body_text(node: Any, rule: Rule, text: str) -> str:
    for field_name in rule.body_fields:
        child = node.child_by_field_name(field_name)
        if child is not None:
            return node_text(text, child)
    return node_text(text, node)


def is_public_symbol(source_text: str, symbol_text: str, language: str, kind: str) -> bool:
    header = first_line(symbol_text)
    if language == "python":
        return not header.startswith("_")
    if language == "go":
        name_match = _IDENTIFIER_RE.search(header.replace("func ", ""))
        if name_match:
            return name_match.group(0)[:1].isupper()
    if language in {"javascript", "typescript"} and kind in {"class", "function"}:
        return header.startswith("export ") or " export " in header
    if language == "rust":
        return header.startswith("pub ") or header.startswith("pub(")
    if language == "java":
        return header.startswith("public ") or header.startswith("protected ")
    return False


def extract_header_comments(lines: Sequence[str], language: str, limit: int = 8) -> list[str]:
    prefixes = COMMENT_PREFIXES[language]
    items: list[str] = []
    for raw_line in lines[:limit * 2]:
        line = raw_line.strip()
        if not line and not items:
            continue
        if any(line.startswith(prefix) for prefix in prefixes):
            cleaned = strip_comment_prefix(line, prefixes)
            if cleaned:
                items.append(cleaned)
            continue
        if language == "python" and (line.startswith('"""') or line.startswith("'''") ):
            items.append(line.strip('"\''))
            break
        if items:
            break
        if line:
            break
    return items[:limit]


def strip_comment_prefix(line: str, prefixes: Sequence[str]) -> str:
    for prefix in sorted(prefixes, key=len, reverse=True):
        if line.startswith(prefix):
            return line[len(prefix) :].strip(" */\t")
    return line.strip()


def extract_preceding_doc(lines: Sequence[str], line_no: int, language: str) -> str:
    prefixes = COMMENT_PREFIXES[language]
    idx = max(0, line_no - 2)
    collected: list[str] = []
    while idx >= 0:
        raw = lines[idx].rstrip()
        stripped = raw.strip()
        if not stripped:
            if collected:
                break
            idx -= 1
            continue
        if any(stripped.startswith(prefix) for prefix in prefixes):
            collected.append(strip_comment_prefix(stripped, prefixes))
            idx -= 1
            continue
        if language == "python" and stripped.endswith(('"""', "'''")):
            collected.append(stripped.strip('"\''))
            idx -= 1
            continue
        break
    collected.reverse()
    return " ".join(item for item in collected if item)


def extract_python_docstring(node: Any, text: str) -> str:
    body = node.child_by_field_name("body")
    if body is None:
        return ""
    named_children = [child for child in getattr(body, "children", []) if child.is_named]
    if not named_children:
        return ""
    first = named_children[0]
    if first.type != "expression_statement":
        return ""
    if not getattr(first, "children", None):
        return ""
    if first.children[0].type == "string":
        return compact(node_text(text, first.children[0]).strip('"\''))
    return ""


def summarize_symbol_role(symbol: Symbol) -> str:
    lowered = symbol.name.lower()
    for pattern, message in _ROLE_RULES:
        if pattern.search(lowered):
            return message
    if symbol.kind in {"class", "struct", "interface", "trait", "record"}:
        return "更像承载核心状态与行为边界的主体对象。"
    if symbol.kind in {"function", "method", "constructor"}:
        return "更像流程中的一个动作节点，负责完成某一步操作。"
    if symbol.kind in {"enum", "type_alias"}:
        return "主要用于约束取值范围或统一表达语义。"
    return "承担局部职责，建议结合调用关系一起理解。"


def summarize_symbol_difficulty(symbol: Symbol) -> str:
    body = f"{symbol.signature} {symbol.body_text}"
    if re.search(r"async|await|tokio|goroutine|channel|thread", body, re.I):
        return "涉及异步或并发，阅读时要分清谁负责发起、等待、汇总。"
    if re.search(r"cache|memo|lru", body, re.I):
        return "涉及缓存，容易把“何时命中/何时失效”看混。"
    if re.search(r"trait|interface|impl|generic|<T|where ", body, re.I):
        return "抽象层较多，建议先看接口，再看具体实现。"
    if re.search(r"unsafe|unwrap\(|panic\(|expect\(|Result<|Option<", body, re.I):
        return "包含错误边界或风险点，建议先看出错路径。"
    return "整体不算绕，但第一次读时最好先抓输入、输出和状态变化。"


def import_targets_from_text(source_text: str, spec: LanguageSpec) -> list[str]:
    items: list[str] = []
    if spec.name == "go":
        for block in re.findall(r"\bimport\s*\((.*?)\)", source_text, flags=re.S):
            items.extend(re.findall(spec.import_patterns[0], block))
        for single in re.findall(r"\bimport\s+\"([^\"]+)\"", source_text):
            items.append(single)
    else:
        for pattern in spec.import_patterns:
            for match in re.findall(pattern, source_text, flags=re.MULTILINE):
                if isinstance(match, tuple):
                    for element in match:
                        if element:
                            items.append(element.strip())
                else:
                    items.append(match.strip())
    cleaned = []
    for item in items:
        item = item.strip().strip(";,")
        if item:
            cleaned.append(item)
    return cleaned


def analyze_parse_task(task: ParseTask) -> FileAnalysis:
    spec = LANGUAGE_SPECS[task.language]
    parser = spec.create_parser()
    source_text = task.source.decode("utf-8", errors="replace")
    tree = parser.parse(task.source)
    lines = source_text.splitlines()
    comments = extract_header_comments(lines, task.language)
    imports = import_targets_from_text(source_text, spec)
    symbols: list[Symbol] = []
    for node in walk_tree(tree.root_node):
        for rule in spec.rules:
            if node.type != rule.node_type:
                continue
            raw_text = node_text(source_text, node)
            name = extract_name(node, rule, source_text, task.language)
            body_text = extract_body_text(node, rule, source_text)
            doc = extract_preceding_doc(lines, node.start_point[0] + 1, task.language)
            if task.language == "python" and not doc:
                doc = extract_python_docstring(node, source_text)
            symbol = Symbol(
                name=name,
                kind=normalize_kind(node, rule, source_text, task.language),
                language=task.language,
                file_path=task.path.as_posix(),
                line_start=node.start_point[0] + 1,
                line_end=node.end_point[0] + 1,
                signature=first_line(raw_text),
                is_public=is_public_symbol(source_text, raw_text, task.language, rule.kind),
                doc=doc,
                body_text=body_text,
            )
            symbol.role_hint = summarize_symbol_role(symbol)
            symbol.difficulty_hint = summarize_symbol_difficulty(symbol)
            symbol.score = score_symbol(symbol, task.path.name)
            symbols.append(symbol)
            break
    local_function_names = {s.name for s in symbols if s.kind in {"function", "method", "constructor"}}
    for symbol in symbols:
        if symbol.kind not in {"function", "method", "constructor"}:
            continue
        symbol.calls = sorted(find_local_calls(symbol.body_text, local_function_names, symbol.name))
    return FileAnalysis(
        file_path=task.path.as_posix(),
        language=task.language,
        source_hash=task.source_hash,
        imports=imports,
        comments=comments,
        file_summary_hints=derive_file_hints(task.path, comments, symbols),
        symbols=symbols,
        diagnostics=[],
    )


def derive_file_hints(path: Path, comments: Sequence[str], symbols: Sequence[Symbol]) -> list[str]:
    hints: list[str] = []
    if comments:
        hints.extend(comments[:3])
    important_kinds = [s.kind for s in symbols if s.is_public][:5]
    if important_kinds:
        kind_counter = Counter(important_kinds)
        kinds = "、".join(kind for kind, _ in kind_counter.most_common(3))
        hints.append(f"该文件公开暴露的核心对象主要集中在：{kinds}。")
    if path.name == "mod.rs":
        hints.append("这是 Rust 模块入口文件，通常承担“对外组织模块、对内协调实现”的角色。")
    return dedupe_preserve_order(hints)


def score_symbol(symbol: Symbol, file_name: str) -> float:
    score = 0.0
    if symbol.is_public:
        score += 6.0
    if symbol.doc:
        score += 4.0
    if symbol.kind in {"class", "struct", "trait", "interface", "record", "enum"}:
        score += 5.0
    if symbol.kind in {"function", "method", "constructor"}:
        score += 3.0
    if Path(symbol.file_path).name == file_name:
        score += 2.0
    name_bonus_tokens = ["manager", "context", "service", "parser", "resolver", "builder", "registry"]
    lowered = symbol.name.lower()
    score += sum(1.0 for token in name_bonus_tokens if token in lowered)
    return score


def find_local_calls(body_text: str, local_names: Iterable[str], self_name: str) -> set[str]:
    found: set[str] = set()
    for name in local_names:
        if name == self_name:
            continue
        pattern = rf"\b{re.escape(name)}\s*\("
        if re.search(pattern, body_text):
            found.add(name)
    return found


def dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if not item or item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def select_top_symbols(analyses: Sequence[FileAnalysis], limit: int, prefer_entry_file: Optional[str] = None) -> list[Symbol]:
    symbols = [symbol for analysis in analyses for symbol in analysis.symbols]
    ranked = sorted(
        symbols,
        key=lambda s: (
            -(s.score + (0.5 if prefer_entry_file and s.file_path == prefer_entry_file else 0.0)),
            s.line_start,
            s.name,
        ),
    )
    return ranked[:limit]


def build_module_edges(analyses: Sequence[FileAnalysis]) -> list[tuple[str, str]]:
    stems = {Path(item.file_path).stem: item.file_path for item in analyses}
    edges: list[tuple[str, str]] = []
    for analysis in analyses:
        current = Path(analysis.file_path).name
        for imported in analysis.imports:
            tokens = re.split(r"[\s:/\\\.]+", imported)
            for token in tokens:
                if token in stems:
                    edges.append((current, Path(stems[token]).name))
        if Path(analysis.file_path).name == "mod.rs":
            for sibling in analyses:
                if sibling.file_path == analysis.file_path:
                    continue
                if Path(sibling.file_path).parent == Path(analysis.file_path).parent:
                    edges.append((current, Path(sibling.file_path).name))
    serialized = dedupe_preserve_order([f"{left}->{right}" for left, right in edges])
    return [tuple(item.split("->", 1)) for item in serialized]


def infer_executive_summary(entry_file: Path, analyses: Sequence[FileAnalysis], supplemental_texts: Sequence[str], cfg: SdocConfig) -> tuple[str, list[str], list[str]]:
    core_symbols = select_top_symbols(analyses, limit=8, prefer_entry_file=entry_file.as_posix())
    all_text = "\n".join(
        list(supplemental_texts)
        + [hint for analysis in analyses for hint in analysis.file_summary_hints]
        + [symbol.doc for symbol in core_symbols if symbol.doc]
        + [symbol.name for symbol in core_symbols]
    )
    keywords = infer_keywords(all_text)
    business_concepts = infer_business_concepts(all_text, core_symbols)

    language_names = "、".join(dedupe_preserve_order([analysis.language for analysis in analyses]))
    symbol_names = "、".join(symbol.name for symbol in core_symbols[:4])
    summary = (
        f"该实现会以 {entry_file.name} 为入口，递归分析其所在目录内的源码文件，优先通过抽象语法树提取核心结构，再结合注释、命名、导入关系和局部调用链生成面向初学者的 Markdown 架构说明。"
        f" 本次分析覆盖的源码语言包括 {language_names}，输出会自动落在目标目录，并附带执行摘要、关键结构表、主流程 mermaid 图、难点类比说明和代表性代码片段。"
    )
    details = [
        f"从当前代码特征看，这个目录的关注点主要围绕：{'、'.join(keywords[:6]) or '模块组织、核心结构、关键流程'}。",
        f"最值得先读的对象通常是：{symbol_names or '入口文件中的公开结构与主函数'}。",
        "生成策略会优先相信显式注释和类型声明，其次才根据命名和调用关系做推断，以降低“看名字猜功能”带来的误判。",
        "如果遇到当前未支持的语言扩展名，工具会立即给出明确报错，不会静默跳过入口文件。",
    ][: cfg.summary_sentence_limit]
    return summary, details, business_concepts


def infer_keywords(text: str) -> list[str]:
    lowered = text.lower()
    token_candidates = re.findall(r"[A-Za-z][A-Za-z0-9_\-]{2,}", lowered)
    stopwords = {
        "this",
        "that",
        "with",
        "from",
        "into",
        "impl",
        "self",
        "true",
        "false",
        "none",
        "some",
        "module",
        "mod",
        "class",
        "struct",
        "enum",
        "type",
        "function",
        "method",
        "return",
        "result",
        "string",
        "value",
        "data",
        "core",
        "src",
        "main",
        "test",
        "public",
        "private",
        "async",
    }
    counter = Counter(token for token in token_candidates if token not in stopwords and len(token) <= 24)
    return [word for word, _ in counter.most_common(12)]


def infer_business_concepts(text: str, symbols: Sequence[Symbol]) -> list[str]:
    results: list[str] = []
    body = text.lower() + " " + " ".join(symbol.name.lower() for symbol in symbols)
    if re.search(r"context", body):
        results.append("**上下文**：可以理解为流程运行时共享的一组背景信息，例如当前配置、会话状态、依赖对象或已收集的数据。")
    if re.search(r"resolver|resolve", body):
        results.append("**解析/解析器**：把“名字、路径、引用”映射到真正可使用对象的过程，类似先查索引再定位实体。")
    if re.search(r"registry|map|index", body):
        results.append("**注册表**：统一登记“名字 -> 实现”或“条件 -> 处理器”的映射，方便后续按条件快速查找。")
    if re.search(r"cache|memo|lru", body):
        results.append("**缓存**：把重复成本高的结果临时保存下来，下次直接复用，以换取速度。")
    if re.search(r"pipeline|stage|phase|workflow", body):
        results.append("**流水线/阶段**：把复杂任务拆为多个阶段，前一步的输出成为后一步的输入。")
    if re.search(r"parser|ast|syntax|token", body):
        results.append("**语法树**：先把源代码解析成树状结构，再去理解“谁定义了什么、谁调用了谁”。")
    return results[:5]


def collect_difficulty_notes(analyses: Sequence[FileAnalysis], limit: int) -> list[DifficultyNote]:
    haystack = "\n".join(
        [analysis.file_path for analysis in analyses]
        + [symbol.signature + "\n" + symbol.body_text + "\n" + symbol.doc for analysis in analyses for symbol in analysis.symbols]
    )
    notes: list[DifficultyNote] = []
    seen_titles: set[str] = set()
    for pattern, note in _DIFFICULTY_RULES:
        if pattern.search(haystack) and note.title not in seen_titles:
            notes.append(note)
            seen_titles.add(note.title)
        if len(notes) >= limit:
            break
    if not notes:
        notes.append(
            DifficultyNote(
                title="没有明显的“黑魔法”",
                explanation="当前代码主要复杂度来自模块拆分和职责分散，而不是语法技巧本身。",
                analogy="更像一套分工明确的办公室：不是某个人做事很玄，而是文件散落在多个部门，需要先找到主责人。",
            )
        )
    return notes


def build_flow_steps(entry_file: Path, analyses: Sequence[FileAnalysis]) -> list[FlowStep]:
    symbols = [symbol for analysis in analyses for symbol in analysis.symbols]
    call_map = {symbol.name: symbol.calls for symbol in symbols if symbol.kind in {"function", "method", "constructor"}}
    entry_candidates = sorted(
        [
            symbol
            for symbol in symbols
            if symbol.kind in {"function", "method", "constructor"}
        ],
        key=lambda s: (
            -(
                s.score
                + (4 if s.file_path == entry_file.as_posix() else 0)
                + (3 if re.search(r"new|create|build|load|run|execute|handle|process|resolve|init", s.name, re.I) else 0)
            ),
            s.line_start,
        ),
    )
    if not entry_candidates:
        top_objects = select_top_symbols(analyses, 3, prefer_entry_file=entry_file.as_posix())
        return [
            FlowStep("识别入口文件", f"从 {entry_file.name} 开始收拢该目录的核心定义与对外接口。"),
            FlowStep("定位核心对象", f"优先阅读 {'、'.join(symbol.name for symbol in top_objects) or '关键结构体'} 的职责。"),
            FlowStep("补全模块关系", "再结合导入关系和相邻文件，理解这个目录如何被组织起来。"),
        ]
    entry = entry_candidates[0]
    steps = [FlowStep("接收输入或建立上下文", f"流程通常会先进入 `{entry.name}`，它像这个目录的前台入口。")]
    current_name = entry.name
    visited = {current_name}
    for _ in range(4):
        next_calls = call_map.get(current_name, [])
        next_name = next((name for name in next_calls if name not in visited), None)
        if not next_name:
            break
        visited.add(next_name)
        target = next((symbol for symbol in symbols if symbol.name == next_name), None)
        if target:
            steps.append(
                FlowStep(
                    f"进入 {target.name}",
                    f"这一层更像把上一层准备好的输入继续加工，职责偏向：{target.role_hint}",
                )
            )
        current_name = next_name
    steps.append(FlowStep("汇总结果或向外输出", "最后由入口层或其上游调用方拿到已整理好的结构化结果，并写出 Markdown 文档。"))
    return steps[:6]


def build_mermaid(flow_steps: Sequence[FlowStep]) -> str:
    lines = ["flowchart TD"]
    for index, step in enumerate(flow_steps):
        node_id = f"S{index + 1}"
        label = f"{step.title}\n{step.detail}"
        label = label.replace('"', "'")
        lines.append(f'    {node_id}["{label}"]')
        if index > 0:
            prev_id = f"S{index}"
            lines.append(f"    {prev_id} --> {node_id}")
    return "\n".join(lines)


def build_snippet_text(file_path: Path, line_start: int, line_end: int, max_lines: int) -> str:
    lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    start = max(0, line_start - 1)
    end = min(len(lines), start + max_lines, max(line_end, line_start + max_lines // 2))
    chosen = lines[start:end]
    while len(chosen) > max_lines:
        chosen = chosen[:-1]
    return "\n".join(chosen).rstrip()


def enrich_snippets(symbols: Sequence[Symbol], max_lines: int) -> list[Symbol]:
    enriched: list[Symbol] = []
    for symbol in symbols:
        path = Path(symbol.file_path)
        copied = Symbol.from_dict(symbol.to_dict())
        copied.snippet = build_snippet_text(path, symbol.line_start, symbol.line_end, max_lines)
        enriched.append(copied)
    return enriched


def collect_supplemental_texts(entry_file: Path, cfg: SdocConfig) -> list[str]:
    results: list[str] = []
    current = entry_file.parent
    stop_root = Path(cfg.project_root).resolve()
    for folder in [current, *current.parents]:
        if stop_root not in [folder, *folder.parents] and folder != stop_root:
            continue
        if cfg.include_readme_context:
            for name in ("README.md", "readme.md", "README", "readme"):
                file_path = folder / name
                if file_path.exists():
                    text = file_path.read_text(encoding="utf-8", errors="replace")
                    results.extend(extract_context_lines(text, max_lines=6))
                    break
        if cfg.include_manifest_context:
            for name in ("Cargo.toml", "pyproject.toml", "package.json", "go.mod", "pom.xml", "build.gradle"):
                file_path = folder / name
                if file_path.exists():
                    text = file_path.read_text(encoding="utf-8", errors="replace")
                    results.extend(extract_manifest_hints(file_path, text))
        if folder == stop_root:
            break
    return dedupe_preserve_order(results)


def extract_context_lines(text: str, max_lines: int) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        stripped = raw.strip().lstrip("#-*")
        stripped = compact(stripped)
        if not stripped:
            continue
        if len(stripped) < 8:
            continue
        lines.append(stripped)
        if len(lines) >= max_lines:
            break
    return lines


def extract_manifest_hints(path: Path, text: str) -> list[str]:
    results: list[str] = []
    if path.name == "Cargo.toml":
        match = re.search(r"^description\s*=\s*['\"](.+?)['\"]", text, re.M)
        if match:
            results.append(match.group(1))
    elif path.name == "pyproject.toml":
        match = re.search(r"^description\s*=\s*['\"](.+?)['\"]", text, re.M)
        if match:
            results.append(match.group(1))
    elif path.name == "package.json":
        try:
            json_obj = json.loads(text)
            if isinstance(json_obj, dict) and json_obj.get("description"):
                results.append(str(json_obj["description"]))
        except json.JSONDecodeError:
            pass
    elif path.name == "go.mod":
        match = re.search(r"^module\s+(.+)$", text, re.M)
        if match:
            results.append(f"Go 模块名：{match.group(1).strip()}")
    elif path.name == "pom.xml":
        match = re.search(r"<description>(.+?)</description>", text, re.S)
        if match:
            results.append(compact(match.group(1)))
    elif path.name == "build.gradle":
        match = re.search(r"description\s*=\s*['\"](.+?)['\"]", text)
        if match:
            results.append(match.group(1))
    return results


def analyze_tasks(tasks: Sequence[ParseTask], cfg: SdocConfig) -> list[FileAnalysis]:
    analyses: list[FileAnalysis] = []
    with ThreadPoolExecutor(max_workers=max(1, cfg.concurrency)) as executor:
        future_map = {executor.submit(analyze_parse_task, task): task for task in tasks}
        for future in as_completed(future_map):
            task = future_map[future]
            try:
                analyses.append(future.result())
            except Exception as exc:
                logger.exception("解析文件失败: %s", task.path)
                raise exc
    analyses.sort(key=lambda item: item.file_path)
    return analyses
