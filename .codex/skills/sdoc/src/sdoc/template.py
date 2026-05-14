from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .models import DifficultyNote, FlowStep, Symbol, TemplateContext


SPECIAL_KIND_NAMES = {
    "struct": "结构体",
    "class": "类",
    "enum": "枚举",
    "trait": "Trait",
    "interface": "接口",
    "record": "Record",
    "type_alias": "类型别名",
    "function": "函数",
    "method": "方法",
    "constructor": "构造函数",
    "module": "模块",
    "impl": "实现块",
    "trait_impl": "Trait 实现",
    "const": "常量",
}


def symbol_kind_name(kind: str) -> str:
    return SPECIAL_KIND_NAMES.get(kind, kind)


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def repo_relative_path(path: str, project_root: str) -> str:
    item = Path(path).resolve()
    root = Path(project_root).resolve()
    try:
        relative = item.relative_to(root)
    except ValueError:
        relative = Path(path)
    return relative.as_posix()


def source_link(path: str, line: int, project_root: str, label: str | None = None) -> str:
    relative = repo_relative_path(path, project_root)
    href = f"/{relative}#L{line}"
    text = label or f"{relative}:{line}"
    return f"[{markdown_escape(text)}]({href})"


def symbol_display_name(symbol: Symbol) -> str:
    if symbol.container and symbol.kind in {"method", "constructor"}:
        return f"{symbol.container}::{symbol.name}"
    return symbol.name


def render_symbol_table(symbols: Sequence[Symbol], project_root: str) -> str:
    if not symbols:
        return "暂无可展示的关键结构。"
    lines = [
        "| 名称 | 类型 | 源码位置 | 职责说明 | 阅读要点 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for symbol in symbols:
        location_label = f"{Path(symbol.file_path).name}:{symbol.line_start}"
        lines.append(
            "| {name} | {kind} | {location} | {role} | {difficulty} |".format(
                name=f"`{markdown_escape(symbol_display_name(symbol))}`",
                kind=symbol_kind_name(symbol.kind),
                location=source_link(symbol.file_path, symbol.line_start, project_root, location_label),
                role=markdown_escape(symbol.role_hint or "-"),
                difficulty=markdown_escape(symbol.difficulty_hint or "-"),
            )
        )
    return "\n".join(lines)


def render_module_edges(edges: Sequence[tuple[str, str]], analyzed_files: Sequence[str], project_root: str) -> str:
    if not edges:
        return "当前目录中没有识别出明显的本地模块依赖边。"
    file_by_name = {Path(path).name: path for path in analyzed_files}
    lines = []
    for left, right in edges[:20]:
        left_label = source_link(file_by_name.get(left, left), 1, project_root, left) if left in file_by_name else f"`{left}`"
        right_label = source_link(file_by_name.get(right, right), 1, project_root, right) if right in file_by_name else f"`{right}`"
        lines.append(f"- {left_label} → {right_label}")
    return "\n".join(lines)


def render_flow_steps(flow_steps: Sequence[FlowStep]) -> str:
    lines = []
    for index, step in enumerate(flow_steps, start=1):
        lines.append(f"{index}. **{step.title}**：{step.detail}")
    return "\n".join(lines)


def render_difficulty_notes(notes: Sequence[DifficultyNote]) -> str:
    paras = []
    for note in notes:
        paras.append(f"**{note.title}**\n\n{note.explanation}\n\n类比理解：{note.analogy}")
    return "\n\n".join(paras)


def render_snippets(symbols: Sequence[Symbol], project_root: str) -> str:
    blocks = []
    for symbol in symbols:
        location = source_link(
            symbol.file_path,
            symbol.line_start,
            project_root,
            f"{repo_relative_path(symbol.file_path, project_root)}:{symbol.line_start}",
        )
        blocks.append(
            f"### `{symbol_display_name(symbol)}`\n\n"
            f"位置：{location}\n\n"
            f"```{snippet_language(symbol.language)}\n{symbol.snippet}\n```"
        )
    return "\n\n".join(blocks) if blocks else "暂无代表性代码片段。"


def snippet_language(language: str) -> str:
    mapping = {
        "rust": "rust",
        "python": "python",
        "javascript": "javascript",
        "typescript": "typescript",
        "java": "java",
        "go": "go",
    }
    return mapping.get(language, "text")


def render_markdown(context: TemplateContext) -> str:
    lines = [
        f"# {context.title}",
        "",
        "## 执行摘要",
        "",
        context.executive_summary,
        "",
        f"入口文件：{source_link(context.entry_file, 1, context.project_root, repo_relative_path(context.entry_file, context.project_root))}  ",
        f"目标目录：`/{repo_relative_path(context.target_directory, context.project_root)}`  ",
        f"涉及语言：{'、'.join(context.languages)}",
        "",
        "## 功能定位与业务说明",
        "",
    ]
    for paragraph in context.functional_description:
        lines.append(paragraph)
        lines.append("")
    if context.business_concepts:
        lines.append("### 关键业务概念")
        lines.append("")
        for concept in context.business_concepts:
            lines.append(f"- {concept}")
        lines.append("")
    lines.extend(
        [
            "## 关键结构与职责表",
            "",
            render_symbol_table(context.key_symbols, context.project_root),
            "",
            "## 主流程",
            "",
            render_flow_steps(context.flow_steps),
            "",
            "```mermaid",
            context.flow_mermaid,
            "```",
            "",
            "### 模块关系",
            "",
            render_module_edges(context.module_edges, context.analyzed_files, context.project_root),
            "",
            "## 难点类比解释",
            "",
            render_difficulty_notes(context.difficulty_notes),
            "",
            "## 示例代码片段",
            "",
            render_snippets(context.snippets, context.project_root),
            "",
            "## 生成信息",
            "",
            f"- 生成时间：{context.generated_at}",
            f"- 分析文件数：{len(context.analyzed_files)}",
            f"- 文件清单：{'、'.join(source_link(item, 1, context.project_root, Path(item).name) for item in context.analyzed_files)}",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def build_template_context(
    *,
    title: str,
    entry_file: str,
    target_directory: str,
    project_root: str,
    languages: Sequence[str],
    executive_summary: str,
    functional_description: Sequence[str],
    business_concepts: Sequence[str],
    key_symbols: Sequence[Symbol],
    flow_steps: Sequence[FlowStep],
    flow_mermaid: str,
    difficulty_notes: Sequence[DifficultyNote],
    module_edges: Sequence[tuple[str, str]],
    snippets: Sequence[Symbol],
    analyzed_files: Sequence[str],
) -> TemplateContext:
    return TemplateContext(
        title=title,
        entry_file=entry_file,
        target_directory=target_directory,
        project_root=project_root,
        languages=list(languages),
        executive_summary=executive_summary,
        functional_description=list(functional_description),
        business_concepts=list(business_concepts),
        key_symbols=list(key_symbols),
        flow_steps=list(flow_steps),
        flow_mermaid=flow_mermaid,
        difficulty_notes=list(difficulty_notes),
        module_edges=list(module_edges),
        snippets=list(snippets),
        generated_at=datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        analyzed_files=list(analyzed_files),
    )
