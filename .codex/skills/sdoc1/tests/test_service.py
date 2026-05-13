from __future__ import annotations

import importlib
import tempfile
import textwrap
import unittest
from pathlib import Path

from sdoc.service import generate_document


class ServiceIntegrationTest(unittest.TestCase):
    @unittest.skipUnless(
        importlib.util.find_spec("tree_sitter") and importlib.util.find_spec("tree_sitter_rust"),
        "需要 tree-sitter 与 tree-sitter-rust 依赖",
    )
    def test_generate_document_for_rust_module(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "codex" / "codex-rs" / "core" / "src" / "context_manager"
            src.mkdir(parents=True)
            (root / "sdoc.toml").write_text(
                textwrap.dedent(
                    """
                    [sdoc]
                    project_root = "."
                    recursive_depth = 1
                    enable_cache = false
                    """
                ).strip(),
                encoding="utf-8",
            )
            (src / "mod.rs").write_text(
                textwrap.dedent(
                    """
                    /// 管理上下文的入口模块
                    pub struct ContextManager {
                        cache: Vec<String>,
                    }

                    impl ContextManager {
                        pub fn new() -> Self {
                            Self { cache: Vec::new() }
                        }

                        pub fn load(&mut self) {
                            self.prepare();
                        }

                        fn prepare(&mut self) {}
                    }
                    """
                ).strip(),
                encoding="utf-8",
            )
            result = generate_document(
                "codex/codex-rs/core/src/context_manager/mod.rs",
                overrides={"project_root": str(root), "enable_cache": False},
            )
            output = Path(result.output_file)
            self.assertTrue(output.exists())
            content = output.read_text(encoding="utf-8")
            self.assertIn("ContextManager", content)
            self.assertIn("```mermaid", content)


if __name__ == "__main__":
    unittest.main()
