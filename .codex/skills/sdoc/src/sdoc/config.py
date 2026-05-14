from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


DEFAULT_EXTENSIONS = [".rs", ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".go"]


@dataclass(slots=True)
class SdocConfig:
    project_root: str = "."
    output_encoding: str = "utf-8"
    recursive_depth: int = 1
    include_tests: bool = False
    include_hidden: bool = False
    include_readme_context: bool = True
    include_manifest_context: bool = True
    max_files: int = 80
    max_file_size_kb: int = 512
    max_definition_table_rows: int = 20
    max_snippets: int = 3
    snippet_max_lines: int = 18
    summary_sentence_limit: int = 4
    max_difficulty_notes: int = 5
    concurrency: int = max(4, (os.cpu_count() or 4))
    supported_extensions: list[str] = field(default_factory=lambda: list(DEFAULT_EXTENSIONS))
    enable_cache: bool = True
    cache_file: str = ".sdoc-cache.json"
    cache_version: str = "2026-05-13-quality-v3"
    log_level: str = "INFO"
    fail_on_unsupported_language: bool = True
    template_title_suffix: str = "代码架构文档"

    def root_path(self) -> Path:
        return Path(self.project_root).resolve()


def _normalize_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    if "sdoc" in data and isinstance(data["sdoc"], dict):
        return dict(data["sdoc"])
    return dict(data)


def load_config(path: Optional[str] = None, overrides: Optional[Dict[str, Any]] = None) -> SdocConfig:
    config = SdocConfig()
    if path:
        file_path = Path(path)
        if file_path.exists():
            with file_path.open("rb") as fp:
                raw = tomllib.load(fp)
            file_data = _normalize_dict(raw)
            config = update_config(config, file_data)
    if overrides:
        config = update_config(config, overrides)
    return config


def update_config(config: SdocConfig, values: Dict[str, Any]) -> SdocConfig:
    allowed = {field.name for field in config.__dataclass_fields__.values()}  # type: ignore[attr-defined]
    cleaned: Dict[str, Any] = {}
    for key, value in values.items():
        if value is None or key not in allowed:
            continue
        cleaned[key] = value
    return replace(config, **cleaned)


def find_config(start: Path, candidates: Iterable[str] = ("sdoc.toml", ".sdoc.toml")) -> Optional[Path]:
    start = start.resolve()
    probe = start if start.is_dir() else start.parent
    for current in [probe, *probe.parents]:
        for name in candidates:
            candidate = current / name
            if candidate.exists():
                return candidate
    return None
