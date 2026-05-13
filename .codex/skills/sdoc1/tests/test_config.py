from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sdoc.config import find_config, load_config


class ConfigTest(unittest.TestCase):
    def test_load_config_and_override(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "sdoc.toml"
            config_path.write_text(
                """
[sdoc]
project_root = "/repo"
recursive_depth = 2
max_files = 10
""".strip(),
                encoding="utf-8",
            )
            cfg = load_config(str(config_path), overrides={"max_files": 20})
            self.assertEqual(cfg.project_root, "/repo")
            self.assertEqual(cfg.recursive_depth, 2)
            self.assertEqual(cfg.max_files, 20)

    def test_find_config_walks_up(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            nested = root / "a" / "b"
            nested.mkdir(parents=True)
            (root / "sdoc.toml").write_text("[sdoc]\nrecursive_depth = 1\n", encoding="utf-8")
            found = find_config(nested)
            self.assertEqual(found, root / "sdoc.toml")


if __name__ == "__main__":
    unittest.main()
