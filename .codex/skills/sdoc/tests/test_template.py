from __future__ import annotations

import unittest

from sdoc.models import DifficultyNote, FlowStep, Symbol
from sdoc.template import build_template_context, render_markdown


class TemplateTest(unittest.TestCase):
    def test_render_markdown_contains_sections(self) -> None:
        context = build_template_context(
            title="mod 代码架构文档",
            entry_file="/repo/src/mod.rs",
            target_directory="/repo/src",
            project_root="/repo",
            languages=["rust"],
            executive_summary="这是摘要。",
            functional_description=["说明一。", "说明二。"],
            business_concepts=["**上下文**：共享背景信息。"],
            key_symbols=[
                Symbol(
                    name="ContextManager",
                    kind="struct",
                    language="rust",
                    file_path="/repo/src/mod.rs",
                    line_start=1,
                    line_end=20,
                    role_hint="核心上下文对象。",
                    difficulty_hint="建议先看输入输出。",
                )
            ],
            flow_steps=[FlowStep("进入入口", "从入口函数开始。")],
            flow_mermaid="flowchart TD\nA-->B",
            difficulty_notes=[
                DifficultyNote(
                    title="上下文传递",
                    explanation="存在上下文对象。",
                    analogy="像共享白板。",
                )
            ],
            module_edges=[("mod.rs", "loader.rs")],
            snippets=[
                Symbol(
                    name="ContextManager",
                    kind="struct",
                    language="rust",
                    file_path="/repo/src/mod.rs",
                    line_start=1,
                    line_end=6,
                    snippet="pub struct ContextManager {}",
                )
            ],
            analyzed_files=["/repo/src/mod.rs"],
        )
        markdown = render_markdown(context)
        self.assertIn("## 执行摘要", markdown)
        self.assertIn("```mermaid", markdown)
        self.assertIn("关键结构与职责表", markdown)
        self.assertIn("ContextManager", markdown)
        self.assertIn("/src/mod.rs#L1", markdown)


if __name__ == "__main__":
    unittest.main()
