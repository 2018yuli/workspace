from __future__ import annotations

import unittest

from sdoc.analysis import summarize_symbol_difficulty, summarize_symbol_role
from sdoc.models import Symbol


class AnalysisSummaryTest(unittest.TestCase):
    def test_role_includes_state_and_call_chain(self) -> None:
        symbol = Symbol(
            name="append_history",
            kind="method",
            language="rust",
            file_path="/repo/src/history.rs",
            line_start=10,
            line_end=18,
            container="ContextManager",
            body_text="self.items.push(item);\nself.process_item(item);\nself.normalize_history();",
            calls=["normalize_history", "process_item"],
        )

        role = summarize_symbol_role(symbol)

        self.assertIn("`items`", role)
        self.assertIn("`normalize_history`", role)

    def test_state_fields_ignore_method_calls(self) -> None:
        symbol = Symbol(
            name="for_prompt",
            kind="method",
            language="rust",
            file_path="/repo/src/history.rs",
            line_start=30,
            line_end=36,
            container="ContextManager",
            body_text="self.normalize_history(input_modalities);\nself.items.retain(|item| true);",
            calls=["normalize_history"],
        )

        hint = summarize_symbol_difficulty(symbol)

        self.assertIn("`items`", hint)
        self.assertIn("`normalize_history`", hint)
        self.assertNotIn("`normalize_history`、`items`", hint)

    def test_difficulty_for_accessor_mentions_field_usage(self) -> None:
        symbol = Symbol(
            name="reference_context_item",
            kind="method",
            language="rust",
            file_path="/repo/src/history.rs",
            line_start=20,
            line_end=22,
            container="ContextManager",
            body_text="&self.reference_context_item",
        )

        hint = summarize_symbol_difficulty(symbol)

        self.assertIn("轻量访问器", hint)
        self.assertIn("`reference_context_item`", hint)


if __name__ == "__main__":
    unittest.main()
