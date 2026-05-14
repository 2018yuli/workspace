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
    (re.compile(r"manager$", re.I), "协调该模块的核心状态与操作边界，通常是上游调用方直接依赖的门面对象。"),
    (re.compile(r"service$", re.I), "封装一组可复用业务能力，对上提供稳定接口，对下隐藏实现细节。"),
    (re.compile(r"controller$", re.I), "负责接收外部输入、选择处理路径，并把请求分发给下游组件。"),
    (re.compile(r"builder$", re.I), "按步骤组装复杂结果，重点关注输入来源、默认值和最终产物。"),
    (re.compile(r"factory$", re.I), "统一创建对象或实现实例，让调用方不必关心具体构造细节。"),
    (re.compile(r"registry$", re.I), "维护名称、类型或条件到实现的映射，是运行时查找和扩展的入口。"),
    (re.compile(r"cache", re.I), "负责缓存可复用结果，核心问题是命中条件、失效时机和一致性。"),
    (re.compile(r"parser|lexer", re.I), "把原始输入转换为结构化表示，后续逻辑基于解析结果工作。"),
    (re.compile(r"resolver", re.I), "把名称、路径或引用解析为可操作的具体目标。"),
    (re.compile(r"scheduler|queue", re.I), "维护任务排队、选择和推进策略，影响执行顺序与吞吐。"),
]


_DIFFICULTY_RULES = [
    (
        re.compile(r"ResponseItem|FunctionCallOutput|CustomToolCallOutput|LocalShellCall|call_id", re.I),
        DifficultyNote(
            title="历史项配对不变量",
            explanation="这类代码通常要求“调用项”和“输出项”成对存在，否则模型侧会看到不完整的工具调用历史。",
            analogy="优先检查插入、删除和回滚路径是否同时维护两端，而不是只看单个 Vec 的增删。",
        ),
    ),
    (
        re.compile(r"TokenUsage|token|truncate|context_window|approx_token", re.I),
        DifficultyNote(
            title="Token 预算是启发式估算",
            explanation="上下文预算往往结合服务端真实 usage、客户端新增项和字节到 token 的近似换算。",
            analogy="阅读时要区分“服务端已统计的 token”和“本地为了决策临时估算的 token”。",
        ),
    ),
    (
        re.compile(r"InputModality|InputImage|image_url|supports_images", re.I),
        DifficultyNote(
            title="多模态能力降级",
            explanation="当目标模型不支持某类输入时，历史仍要保持结构完整，但对应内容需要替换或省略。",
            analogy="重点确认替换后是否仍保留用户/工具输出的语义位置，以及是否避免把不可用内容发给模型。",
        ),
    ),
    (
        re.compile(r"TurnContextItem|previous|next|diff|model_switch|personality|sandbox", re.I),
        DifficultyNote(
            title="上下文差量更新",
            explanation="上下文更新代码通常只在 previous 与 next 存在差异时生成新指令，避免重复注入相同信息。",
            analogy="阅读时要沿着每个 early return 看清楚：哪些变化会发给模型，哪些变化会被静默跳过。",
        ),
    ),
    (
        re.compile(r"async|await|tokio|futures|goroutine|channel|thread", re.I),
        DifficultyNote(
            title="并发/异步流程",
            explanation="代码可能不是按单线程直线往下跑，而是把等待 I/O 或耗时操作拆出去并行推进。",
            analogy="阅读时先区分发起者、等待点和结果汇总点，再回头看错误传播路径。",
        ),
    ),
    (
        re.compile(r"cache|memo|lru|store", re.I),
        DifficultyNote(
            title="缓存与复用",
            explanation="这类代码会优先复用已算过的数据，以减少重复昂贵操作。",
            analogy="重点确认缓存键、命中条件、失效条件，以及缓存内容是否会跨上下文污染。",
        ),
    ),
    (
        re.compile(r"trait|interface|abstract|generic|where\s|impl<|<T|<K|<V", re.I),
        DifficultyNote(
            title="抽象层与泛型",
            explanation="代码强调“约定优先”，先定义一套接口或能力，再让不同实现去接入。",
            analogy="阅读时先看 trait/interface 的契约，再看具体实现如何满足这些约束。",
        ),
    ),
    (
        re.compile(r"state|status|phase|stage|transition", re.I),
        DifficultyNote(
            title="状态流转",
            explanation="逻辑不是一次完成，而是在多个状态之间逐步推进，每一步可走的分支不同。",
            analogy="建议列出状态字段、触发条件和每条路径对状态的修改结果。",
        ),
    ),
    (
        re.compile(r"context|scope|session|env", re.I),
        DifficultyNote(
            title="上下文传递",
            explanation="部分信息不会直接写死在函数里，而是通过上下文对象逐层传递。",
            analogy="重点确认上下文的来源、生命周期，以及哪些字段会进入模型可见历史。",
        ),
    ),
    (
        re.compile(r"parse|syntax|ast|tree-sitter|token", re.I),
        DifficultyNote(
            title="语法树与解析过程",
            explanation="代码在处理文本时，通常会先把文本拆成结构化节点，再基于这些节点做判断。",
            analogy="阅读时把解析阶段、节点筛选阶段和语义转换阶段分开看。",
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


def assign_symbol_containers(symbols: Sequence[Symbol]) -> None:
    containers = [
        symbol
        for symbol in symbols
        if symbol.kind in {"class", "struct", "interface", "trait", "record", "impl", "trait_impl"}
    ]
    for symbol in symbols:
        if symbol.kind not in {"function", "method", "constructor"}:
            continue
        candidates = [
            container
            for container in containers
            if container is not symbol
            and container.line_start <= symbol.line_start
            and symbol.line_end <= container.line_end
        ]
        if not candidates:
            continue
        container = min(candidates, key=lambda item: item.line_end - item.line_start)
        symbol.container = clean_container_name(container.name)
        if container.kind in {"impl", "trait_impl", "trait", "class", "interface"}:
            symbol.kind = "method"


def clean_container_name(name: str) -> str:
    name = compact(name)
    name = re.sub(r"^impl\s+", "", name)
    name = re.sub(r"\s*\{.*$", "", name)
    if " for " in name:
        name = name.split(" for ", 1)[1]
    return name.strip() or name


def display_symbol_name(symbol: Symbol) -> str:
    if symbol.container and symbol.kind in {"method", "constructor"}:
        return f"{symbol.container}::{symbol.name}"
    return symbol.name


def extract_field_summaries(symbol: Symbol, limit: int = 5) -> list[str]:
    fields: list[str] = []
    for match in re.finditer(
        r"^\s*(?:pub(?:\([^)]*\))?\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([^,\n]+)",
        symbol.body_text,
        flags=re.M,
    ):
        name = match.group(1)
        type_name = compact(match.group(2))
        fields.append(f"`{name}: {type_name}`")
        if len(fields) >= limit:
            break
    return fields


def extract_state_fields(symbol: Symbol, limit: int = 6) -> list[str]:
    fields: list[str] = []
    for match in re.finditer(r"\bself\.([A-Za-z_][A-Za-z0-9_]*)", symbol.body_text):
        suffix = symbol.body_text[match.end():]
        if re.match(r"\s*\(", suffix):
            continue
        field = match.group(1)
        if field not in fields:
            fields.append(field)
        if len(fields) >= limit:
            break
    return fields


def extract_mutated_fields(symbol: Symbol, limit: int = 6) -> list[str]:
    mutated: list[str] = []
    mutation_patterns = (
        r"\bself\.([A-Za-z_][A-Za-z0-9_]*)\s*=",
        r"\bself\.([A-Za-z_][A-Za-z0-9_]*)\.(?:push|pop|retain|remove|insert|extend|clear|truncate|sort|drain)\s*\(",
    )
    for pattern in mutation_patterns:
        for match in re.finditer(pattern, symbol.body_text):
            field = match.group(1)
            if field not in mutated:
                mutated.append(field)
            if len(mutated) >= limit:
                return mutated
    return mutated


def format_identifier_list(items: Sequence[str], limit: int = 4) -> str:
    picked = [f"`{item}`" for item in items[:limit] if item]
    return "、".join(picked)


def infer_accessor_field(symbol: Symbol) -> str | None:
    direct_names = extract_state_fields(symbol, limit=2)
    if len(direct_names) == 1:
        return direct_names[0]
    for prefix in ("set_", "get_", "update_", "read_"):
        if symbol.name.startswith(prefix):
            return symbol.name.removeprefix(prefix)
    return None


def is_simple_accessor(symbol: Symbol) -> bool:
    body = compact(symbol.body_text)
    if not body:
        return False
    if re.search(r"\bself\.[A-Za-z_][A-Za-z0-9_]*\.clone\(\)", body):
        return True
    if re.fullmatch(r"\{?\s*&?self\.[A-Za-z_][A-Za-z0-9_]*\s*\}?", body):
        return True
    return False


def infer_method_role_from_structure(symbol: Symbol) -> str | None:
    mutated_fields = extract_mutated_fields(symbol)
    state_fields = extract_state_fields(symbol)
    called = symbol.calls[:3]
    name = symbol.name.lower()

    if symbol.kind not in {"function", "method", "constructor"}:
        return None
    if symbol.kind == "constructor" or name == "new":
        if state_fields:
            return f"初始化 {format_identifier_list(state_fields)} 等内部状态，建立 `{symbol.container or symbol.name}` 的可用初始值。"
        return "构造并返回一个可直接投入后续流程使用的初始对象。"
    accessor_field = infer_accessor_field(symbol)
    if accessor_field and symbol.name.startswith("get_"):
        return f"读取 `{accessor_field}` 状态，对外提供该字段的受控访问入口。"
    if is_simple_accessor(symbol) and accessor_field:
        return f"暴露 `{accessor_field}` 的只读访问，避免上层直接依赖内部字段布局。"
    if mutated_fields and called:
        return f"围绕 {format_identifier_list(mutated_fields)} 等状态推进当前步骤，并把具体处理下沉到 {format_identifier_list(called)}。"
    if mutated_fields:
        return f"直接修改 {format_identifier_list(mutated_fields)} 等内部状态，是当前对象状态流转中的一个写入点。"
    if called and state_fields:
        return f"基于 {format_identifier_list(state_fields)} 等上下文编排后续处理，核心动作委托给 {format_identifier_list(called)}。"
    if called:
        return f"作为局部编排节点，按顺序调用 {format_identifier_list(called)} 等辅助逻辑完成本步骤。"
    if state_fields:
        return f"围绕 {format_identifier_list(state_fields)} 等内部状态完成一次局部读写或判断。"
    return None


def infer_reading_hint_from_structure(symbol: Symbol) -> str | None:
    body = f"{symbol.signature} {symbol.body_text}"
    state_fields = extract_state_fields(symbol)
    mutated_fields = extract_mutated_fields(symbol)
    called = symbol.calls[:3]

    if re.search(r"async|await|tokio|goroutine|channel|thread", body, re.I):
        return "涉及异步或并发，阅读时要分清谁负责发起、等待、汇总。"
    if re.search(r"cache|memo|lru", body, re.I):
        return "涉及缓存，容易把“何时命中/何时失效”看混。"
    if re.search(r"trait|interface|impl|generic|<T|where ", body, re.I):
        return "抽象层较多，建议先看接口，再看具体实现。"
    if re.search(r"unsafe|unwrap\(|panic\(|expect\(|Result<|Option<", body, re.I):
        details = ["包含错误边界或风险点，建议先看出错路径"]
        if called:
            details.append(f"再顺着 {format_identifier_list(called)} 看异常如何传播")
        return "；".join(details) + "。"
    if symbol.name.startswith("set_") and mutated_fields:
        return f"这是直接状态写入点，重点看 {format_identifier_list(mutated_fields)} 在哪些回合边界被更新。"
    if is_simple_accessor(symbol) and state_fields:
        return f"这是轻量访问器，重点看 {format_identifier_list(state_fields)} 的来源以及谁依赖这个读取结果。"
    notes: list[str] = []
    if mutated_fields:
        notes.append(f"先确认它会改动哪些状态：{format_identifier_list(mutated_fields)}")
    elif state_fields:
        notes.append(f"先确认它依赖哪些状态：{format_identifier_list(state_fields)}")
    if called:
        notes.append(f"再顺着调用链继续看：{format_identifier_list(called)}")
    if notes:
        return "；".join(notes) + "。"
    return None


def normalize_technical_terms(text: str) -> str:
    replacements = {
        "ResponseItem": "模型交互历史项",
        "TokenUsageInfo": "token 使用统计",
        "TokenUsage": "token 使用量",
        "TurnContextItem": "回合上下文快照",
        "InputModality": "模型输入模态",
        "FunctionCallOutput": "函数调用输出",
        "CustomToolCallOutput": "自定义工具调用输出",
        "DeveloperInstructions": "开发者指令",
        "EnvironmentContext": "运行环境上下文",
    }
    result = text
    for raw, friendly in replacements.items():
        result = result.replace(raw, friendly)
    return result


def role_from_exact_name(symbol: Symbol) -> Optional[str]:
    body = f"{symbol.signature}\n{symbol.body_text}"
    exact_roles = {
        "ContextManager": "维护按时间排序的模型交互历史、token 使用统计和上下文基线，是发送模型前整理 prompt 历史的核心状态对象。",
        "TotalTokenUsageBreakdown": "承载 token 统计拆解结果，把服务端已报告 token、历史可见字节数和最近新增项的估算成本分开暴露，方便上层做预算判断。",
        "record_items": "接收按时间顺序到来的历史项，只保留 API 相关项和 ghost snapshot，并在入库前按截断策略压缩工具输出。",
        "for_prompt": "生成即将发送给模型的历史列表：先执行历史归一化，再移除 ghost snapshot，最终返回模型可见的 `ResponseItem` 序列。",
        "raw_items": "提供未归一化的历史只读视图，供调用方检查当前内存中的原始 `ResponseItem`。",
        "estimate_token_count": "结合当前回合的模型基础指令与历史项估算 token 总量，用于上下文窗口预算判断。",
        "estimate_token_count_with_base_instructions": "把基础指令 token 与每个历史项的估算 token 饱和相加，形成粗粒度预算结果。",
        "remove_first_item": "删除最老历史项，并同步删除与其配对的调用或输出，避免破坏工具调用配对不变量。",
        "remove_last_item": "弹出最新历史项并清理其配对项，用于回滚末尾历史同时保持调用/输出成对。",
        "replace": "整体替换内存历史列表，通常用于回滚或外部重新整理后的状态覆盖。",
        "replace_last_turn_images": "在最近一轮中把工具输出图片替换为占位文本，用于在不重新生成整段历史的情况下移除图片负载。",
        "drop_last_n_user_turns": "按用户消息边界回滚最近 N 个用户回合，并保留第一条用户消息之前的系统或初始化历史。",
        "update_token_info": "把最新 API token usage 合并进累计统计，并根据模型上下文窗口维护 token 信息。",
        "get_non_last_reasoning_items_tokens": "估算最后一个用户消息之前的加密 reasoning 项 token，避免与服务端最近 usage 统计混淆。",
        "items_after_last_model_generated_item": "定位最近一次模型生成项之后的本地新增历史片段，这些项通常尚未反映在服务端 usage 中。",
        "get_total_token_usage": "合并服务端 usage、本地新增项估算和可选 reasoning 估算，得到当前历史的总 token 成本。",
        "get_total_token_usage_breakdown": "输出 token 成本拆解，区分服务端最近响应、全历史可见字节和最近新增项的估算 token/字节。",
        "normalize_history": "集中维护 prompt 历史不变量：补齐调用输出、移除孤儿输出，并按模型输入能力替换图片内容。",
        "process_item": "入库前处理单个历史项；对工具输出应用序列化预算截断，其他模型交互项保持原样克隆。",
        "is_api_message": "判定历史项是否属于应记录的 API 消息，排除 system、ghost snapshot 和未知项。",
        "estimate_reasoning_length": "用 base64 长度近似推导 reasoning 明文长度，并扣除固定封装开销。",
        "estimate_item_token_count": "把单个历史项的模型可见字节数转换为近似 token 数。",
        "estimate_response_item_model_visible_bytes": "估算单个 `ResponseItem` 对模型可见的序列化字节成本，并对加密 reasoning 与内联图片做专门折算。",
        "base64_data_url_payload_len": "识别 `data:image/...;base64,...` 形式的内联图片，并返回可折算的 base64 payload 长度。",
        "image_data_url_estimate_adjustment": "扫描消息和工具输出中的内联图片，计算需要从原始序列化大小中扣除并替换为固定图片成本的字节数。",
        "is_model_generated_item": "识别由模型侧产生的历史项，作为 usage 断点和本地新增项切分依据。",
        "is_codex_generated_item": "判断历史项是否由 Codex/模型生成，用于区分用户边界和助手侧事件。",
        "is_user_turn_boundary": "识别用户回合边界，支撑回滚、截断和上下文整理逻辑。",
        "user_message_positions": "收集历史中所有用户消息的位置，为按用户回合回滚提供切分索引。",
        "ensure_call_outputs_present": "扫描历史中的函数、自定义工具和本地 shell 调用，确保每个调用都有对应输出占位，维持 OpenAI 输入协议不变量。",
        "remove_orphan_outputs": "删除找不到对应调用项的输出，并在发现孤儿输出时记录错误或触发测试期 panic。",
        "remove_corresponding_for": "当调用项或输出项被删除时，顺带移除另一端配对项，避免历史中留下半截工具调用。",
        "strip_images_when_unsupported": "当模型不支持图片输入时，把消息和工具输出中的图片内容替换为固定占位文本，同时保留历史结构。",
        "build_settings_update_items": "比较上一轮和下一轮上下文，按固定顺序生成模型指令、环境、权限、协作模式和人格等差量更新项。",
        "build_model_instructions_update_item": "模型发生切换时生成新的模型指令注入项，确保下一个模型收到匹配的基础行为说明。",
        "personality_message_for": "从模型消息配置中查找指定 personality 的指令文本，并过滤空消息。",
    }
    if symbol.name in exact_roles:
        return exact_roles[symbol.name]
    if re.match(r"^set_[A-Za-z0-9_]+$", symbol.name):
        field = symbol.name.removeprefix("set_")
        return f"更新 `{field}` 状态字段，是 `{symbol.container or '当前对象'}` 对外暴露的显式状态写入入口。"
    if re.match(r"^[A-Za-z0-9_]+$", symbol.name) and symbol.container and re.search(r"clone\(\)|&self\.[A-Za-z_]", body):
        return f"读取 `{symbol.name}` 相关状态，避免调用方直接访问 `{symbol.container}` 的内部字段。"
    return None


def role_from_patterns(symbol: Symbol) -> Optional[str]:
    name = symbol.name.lower()
    body = f"{symbol.signature}\n{symbol.body_text}"
    lowered_body = body.lower()
    mutated_fields = extract_mutated_fields(symbol)
    state_fields = extract_state_fields(symbol)
    called = symbol.calls[:3]
    if symbol.kind in {"class", "struct", "interface", "trait", "record"}:
        fields = extract_field_summaries(symbol)
        if fields:
            field_text = "、".join(fields)
            if "responseitem" in lowered_body or "token" in lowered_body or "context" in lowered_body:
                return f"封装 {field_text} 等关键状态，把历史记录、预算统计和上下文快照集中在一个边界内管理。"
            return f"封装 {field_text} 等字段，定义该模块内部状态和行为的主要边界。"
    if symbol.kind in {"function", "method", "constructor"}:
        if name.startswith("build_") and "update" in name:
            detail = ""
            if called:
                detail = f"，并继续调用 {format_identifier_list(called)} 组织具体更新项"
            return f"根据前后上下文差异构造可注入模型历史的更新项，只有检测到真实变化时才返回结果{detail}。"
        if "normalize" in name or "orphan" in name or "corresponding" in name:
            detail = f"；重点看 {format_identifier_list(called)} 如何修复配对关系" if called else ""
            return f"维护历史列表的不变量，重点处理调用项、输出项和模型能力不匹配造成的结构问题{detail}。"
        if "token" in name or "usage" in name:
            detail = f"；关注它读写的状态：{format_identifier_list(state_fields)}" if state_fields else ""
            return f"负责 token/字节成本估算或统计合并，是上下文窗口预算相关逻辑的一部分{detail}。"
        if "image" in name or "modality" in lowered_body:
            detail = f"；主要作用在 {format_identifier_list(mutated_fields or state_fields)}" if (mutated_fields or state_fields) else ""
            return f"处理图片内容与模型输入能力之间的兼容问题，避免不支持图片的模型收到原始图片负载{detail}。"
        if "remove" in name or "drop" in name or "rollback" in name:
            detail = f"；通常会直接改动 {format_identifier_list(mutated_fields)}" if mutated_fields else ""
            return f"负责删除或回滚历史片段，同时需要保持调用/输出配对和用户回合边界的正确性{detail}。"
        if "record" in name or "append" in name or "push" in lowered_body:
            details = []
            if mutated_fields:
                details.append(f"写入 {format_identifier_list(mutated_fields)}")
            if called:
                details.append(f"下沉到 {format_identifier_list(called)} 做具体处理")
            suffix = f"；{'，'.join(details)}" if details else ""
            return f"负责把新输入纳入内部状态，并在写入前做过滤、归一化或预算处理{suffix}。"
        if "retain" in lowered_body or "filter" in lowered_body:
            detail = f"；筛选目标集中在 {format_identifier_list(mutated_fields or state_fields)}" if (mutated_fields or state_fields) else ""
            return f"负责筛选集合内容，只保留后续流程真正需要且满足协议约束的元素{detail}。"
        if "match" in lowered_body and "responseitem" in lowered_body:
            return "按 `ResponseItem` 变体分派处理逻辑，是理解该模块行为分支的关键位置。"
    return None


def summarize_symbol_role(symbol: Symbol) -> str:
    exact = role_from_exact_name(symbol)
    if exact:
        return exact
    patterned = role_from_patterns(symbol)
    if patterned:
        return patterned
    inferred = infer_method_role_from_structure(symbol)
    if inferred:
        return inferred
    lowered = symbol.name.lower()
    for pattern, message in _ROLE_RULES:
        if pattern.search(lowered):
            return message
    if symbol.doc:
        return normalize_technical_terms(f"围绕注释所描述的能力提供实现：{symbol.doc}。")
    if symbol.kind in {"class", "struct", "interface", "trait", "record"}:
        return "定义该模块的核心数据边界，建议结合字段列表和关联方法一起理解。"
    if symbol.kind in {"function", "method", "constructor"}:
        return "承担一个明确处理步骤，建议从输入参数、返回值和对共享状态的修改三处阅读。"
    if symbol.kind in {"enum", "type_alias"}:
        return "约束一组取值或统一复杂类型表达，帮助上层逻辑减少重复类型细节。"
    if symbol.kind == "module":
        return "声明或组织子模块，是当前目录对外暴露结构的一部分。"
    return "承担局部职责，建议结合调用关系和相邻定义一起理解。"


def summarize_symbol_difficulty(symbol: Symbol) -> str:
    inferred = infer_reading_hint_from_structure(symbol)
    if inferred:
        return inferred
    return "先抓输入、输出与状态变化，再决定是否需要展开相邻调用点。"


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
            symbols.append(symbol)
            break
    assign_symbol_containers(symbols)
    local_function_names = {s.name for s in symbols if s.kind in {"function", "method", "constructor"}}
    for symbol in symbols:
        if symbol.kind not in {"function", "method", "constructor"}:
            continue
        symbol.calls = sorted(find_local_calls(symbol.body_text, local_function_names, symbol.name))
    for symbol in symbols:
        symbol.role_hint = summarize_symbol_role(symbol)
        symbol.difficulty_hint = summarize_symbol_difficulty(symbol)
        symbol.score = score_symbol(symbol, task.path.name)
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
    file_name = path.name
    symbol_names = {symbol.name for symbol in symbols}
    joined = "\n".join(symbol.signature + "\n" + symbol.body_text for symbol in symbols)
    if file_name == "history.rs" and ({"ContextManager", "ResponseItem"} & symbol_names or "ResponseItem" in joined):
        hints.append("该文件负责维护 Codex 会话历史、模型可见 prompt 项、token 预算估算和历史归一化入口。")
    elif file_name == "normalize.rs" or "ensure_call_outputs_present" in symbol_names:
        hints.append("该文件集中维护工具调用与输出的配对不变量，并处理模型不支持图片时的历史降级。")
    elif file_name == "updates.rs" or "build_settings_update_items" in symbol_names:
        hints.append("该文件根据 TurnContext 的前后差异生成模型可见的设置更新项，避免重复注入未变化上下文。")
    elif file_name == "mod.rs":
        hints.append("这是 Rust 模块入口，负责声明子模块并重新导出 context_manager 对外 API。")
    important_kinds = [s.kind for s in symbols if s.is_public][:5]
    if important_kinds:
        kind_counter = Counter(important_kinds)
        kinds = "、".join(kind for kind, _ in kind_counter.most_common(3))
        hints.append(f"该文件公开暴露的核心对象主要集中在：{kinds}。")
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
    symbol_names = "、".join(display_symbol_name(symbol) for symbol in core_symbols[:4])
    module_focus = infer_module_focus(entry_file, analyses, keywords)
    primary_files = "、".join(Path(analysis.file_path).name for analysis in analyses[:5])
    summary = (
        f"`{entry_file.name}` 所在目录主要负责{module_focus}。"
        f"本次分析覆盖 {len(analyses)} 个 {language_names} 文件（{primary_files}），核心阅读对象包括 {symbol_names or '入口文件中的公开结构与主函数'}。"
    )
    details = infer_functional_details(entry_file, analyses, core_symbols, keywords)
    details = details[: cfg.summary_sentence_limit]
    return summary, details, business_concepts


def infer_module_focus(entry_file: Path, analyses: Sequence[FileAnalysis], keywords: Sequence[str]) -> str:
    names = {Path(analysis.file_path).name for analysis in analyses}
    all_text = "\n".join(
        [analysis.file_path for analysis in analyses]
        + [hint for analysis in analyses for hint in analysis.file_summary_hints]
        + [symbol.name + "\n" + symbol.signature + "\n" + symbol.body_text[:1200] for analysis in analyses for symbol in analysis.symbols]
    )
    lowered = all_text.lower()
    if "history.rs" in names and "normalize.rs" in names and "responseitem" in lowered:
        return "Codex 对话历史的记录、裁剪、归一化、模型可见内容构造，以及 token 使用量估算"
    if "updates.rs" in names and "turncontext" in lowered:
        return "根据运行上下文变化生成模型可见设置更新，控制模型指令、环境、权限和人格差量注入"
    if entry_file.name == "mod.rs":
        return "组织当前 Rust 模块的子模块声明与对外重导出，形成上层调用方看到的 context_manager API"
    return "、".join(keywords[:4]) or "当前目录的核心数据结构、处理流程和对外接口"


def infer_functional_details(
    entry_file: Path,
    analyses: Sequence[FileAnalysis],
    core_symbols: Sequence[Symbol],
    keywords: Sequence[str],
) -> list[str]:
    all_symbols = [symbol for analysis in analyses for symbol in analysis.symbols]
    names = {symbol.name for symbol in all_symbols}
    details: list[str] = []
    if "ContextManager" in names:
        details.append("`ContextManager` 是历史状态门面：它持有按时间排序的 `ResponseItem`、token 统计和参考上下文快照，并负责把原始历史整理成可发送给模型的 prompt 历史。")
    if {"ensure_call_outputs_present", "remove_orphan_outputs", "strip_images_when_unsupported"} & names:
        details.append("`normalize` 模块维护历史协议不变量：工具调用必须有输出、输出必须能找到调用；当模型不支持图片时，图片内容会被替换为占位文本而不是破坏消息结构。")
    if {"estimate_response_item_model_visible_bytes", "get_total_token_usage", "get_total_token_usage_breakdown"} & names:
        details.append("token 预算逻辑同时处理服务端已返回 usage、本地新增历史项、加密 reasoning 和内联图片的启发式成本，适合先按“真实统计 vs 本地估算”两条线阅读。")
    if "build_settings_update_items" in names:
        details.append("`updates` 模块按固定顺序生成上下文差量更新，优先注入模型切换指令，再处理环境、权限、协作模式和 personality 变化。")
    if entry_file.name == "mod.rs":
        exported = [symbol for symbol in all_symbols if symbol.file_path == entry_file.as_posix()]
        if exported:
            details.append("模块入口的价值在于收敛 API：上层通过这里拿到 `ContextManager`、token breakdown 和历史边界判断函数，而不必关心子文件拆分。")
    if core_symbols:
        details.append(f"建议阅读顺序：先看 {'、'.join(display_symbol_name(symbol) for symbol in core_symbols[:5])}，再沿职责表中的源码链接跳到具体实现。")
    if not details:
        details.append(f"从当前代码特征看，这个目录的关注点主要围绕：{'、'.join(keywords[:6]) or '模块组织、核心结构、关键流程'}。")
    return details


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
    if re.search(r"responseitem|conversation|history|transcript|prompt", body):
        results.append("**历史项 / ResponseItem**：一次对话中模型、用户、工具调用和工具输出的结构化记录；发送给模型前必须保持顺序和协议不变量。")
    if re.search(r"call_id|functioncall|customtoolcall|orphan|corresponding", body):
        results.append("**调用 / 输出配对**：工具调用和工具输出依靠 `call_id` 成对出现；删除、回滚或归一化时必须同时维护两端。")
    if re.search(r"token|context_window|truncate|usage|visible_bytes", body):
        results.append("**Token 预算**：结合服务端 usage 与本地启发式估算，判断历史是否接近模型上下文窗口。")
    if re.search(r"modality|inputimage|image_url|image", body):
        results.append("**输入模态降级**：当模型不支持图片等输入类型时，用占位文本保留历史位置，同时避免发送不可处理内容。")
    if re.search(r"turncontext|environmentcontext|sandbox|approval|personality", body):
        results.append("**上下文差量更新**：比较上一轮和下一轮运行上下文，只把变化部分作为开发者指令重新注入模型历史。")
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
    symbol_names = {symbol.name for symbol in symbols}
    if "ContextManager" in symbol_names:
        steps = [
            FlowStep("记录历史项", "`ContextManager::record_items` 按时间顺序接收新历史，只保留 API 相关消息和 ghost snapshot，并通过 `process_item` 截断大型工具输出。"),
            FlowStep("维护历史窗口", "删除、回滚和替换路径会调用 `normalize::remove_corresponding_for`，保证函数/工具调用与输出不会只剩一端。"),
            FlowStep("准备模型输入", "`ContextManager::for_prompt` 在返回历史前执行 `normalize_history`，补齐缺失输出、移除孤儿输出，并按模型模态能力处理图片。"),
            FlowStep("估算上下文成本", "`estimate_token_count` 与 `get_total_token_usage*` 把基础指令、历史项、reasoning 和图片折算为预算信息。"),
            FlowStep("暴露边界判断", "`is_codex_generated_item`、`is_user_turn_boundary` 等辅助函数供回滚、压缩和上层线程管理逻辑识别历史边界。"),
        ]
        return steps[:6]
    if "build_settings_update_items" in symbol_names:
        return [
            FlowStep("接收上下文快照", "入口接收 previous、previous_user_turn_model 和 next `TurnContext`，同时拿到 shell、执行策略和 personality feature 开关。"),
            FlowStep("优先处理模型切换", "模型切换指令排在最前，确保新模型先读到匹配自身的基础行为说明。"),
            FlowStep("生成环境与权限差量", "环境、sandbox、approval policy 等只有发生变化时才转成新的 `DeveloperInstructions`。"),
            FlowStep("补充协作模式与人格", "协作模式和 personality 更新在后续追加，且空指令或未启用 feature 会被跳过。"),
            FlowStep("返回有序更新项", "最终返回可插入历史的 `ResponseItem` 列表，上游负责把这些差量送入模型上下文。"),
        ]
    if {"ensure_call_outputs_present", "remove_orphan_outputs", "strip_images_when_unsupported"} & symbol_names:
        return [
            FlowStep("扫描调用项", "先收集函数调用、自定义工具调用和本地 shell 调用的 `call_id`，确认哪些调用需要输出。"),
            FlowStep("补齐缺失输出", "对没有输出的调用追加失败占位输出，避免模型收到不完整工具调用链。"),
            FlowStep("移除孤儿输出", "再反向检查输出是否能找到对应调用，找不到就记录错误并从历史中移除。"),
            FlowStep("按能力降级内容", "当模型不支持图片输入时，把消息和工具输出中的图片替换为统一占位文本。"),
        ]
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
    entry_display = display_symbol_name(entry)
    steps = [FlowStep("进入核心处理", f"流程通常从 `{entry_display}` 开始；该节点的职责是：{entry.role_hint}")]
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
    steps.append(FlowStep("交还上游", "处理完成后返回结构化结果或已更新的内部状态，由上游继续发送模型、回滚历史或展示统计信息。"))
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
