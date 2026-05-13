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


def render_symbol_table(symbols: Sequence[Symbol]) -> str:
    if not symbols:
        return "暂无可展示的关键结构。"
    lines = [
        "| 名称 | 类型 | 所在文件 | 角色说明 | 初学者阅读提示 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for symbol in symbols:
        lines.append(
            "| {name} | {kind} | {file}:{line} | {role} | {difficulty} |".format(
                name=symbol.name.replace("|", "\\|"),
                kind=symbol_kind_name(symbol.kind),
                file=Path(symbol.file_path).name.replace("|", "\\|"),
                line=symbol.line_start,
                role=(symbol.role_hint or "-").replace("|", "\\|"),
                difficulty=(symbol.difficulty_hint or "-").replace("|", "\\|"),
            )
        )
    return "\n".join(lines)


def render_module_edges(edges: Sequence[tuple[str, str]]) -> str:
    if not edges:
        return "当前目录中没有识别出明显的本地模块依赖边。"
    lines = []
    for left, right in edges[:20]:
        lines.append(f"- `{left}` → `{right}`")
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


def render_snippets(symbols: Sequence[Symbol]) -> str:
    blocks = []
    for symbol in symbols:
        blocks.append(
            f"### `{symbol.name}`\n\n"
            f"位置：`{Path(symbol.file_path).name}:{symbol.line_start}`\n\n"
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
        f"入口文件：`{Path(context.entry_file).as_posix()}`  ",
        f"目标目录：`{Path(context.target_directory).as_posix()}`  ",
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
            render_symbol_table(context.key_symbols),
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
            render_module_edges(context.module_edges),
            "",
            "## 难点类比解释",
            "",
            render_difficulty_notes(context.difficulty_notes),
            "",
            "## 示例代码片段",
            "",
            render_snippets(context.snippets),
            "",
            "## 生成信息",
            "",
            f"- 生成时间：{context.generated_at}",
            f"- 分析文件数：{len(context.analyzed_files)}",
            f"- 文件清单：{'、'.join(Path(item).name for item in context.analyzed_files)}",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def build_template_context(
    *,
    title: str,
    entry_file: str,
    target_directory: str,
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
