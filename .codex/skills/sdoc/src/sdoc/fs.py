from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable, List

from .config import SdocConfig
from .errors import PathResolutionError, UnsupportedLanguageError
from .models import ParseTask


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


SUPPORTED_BY_EXTENSION = {
    ".rs": "rust",
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".java": "java",
    ".go": "go",
}


def resolve_target(relative_path: str, project_root: Path) -> Path:
    base = project_root.resolve()
    candidate = (base / relative_path).resolve()
    if not candidate.exists():
        raise PathResolutionError(f"目标路径不存在: {relative_path}")
    if base not in candidate.parents and candidate != base:
        raise PathResolutionError(f"目标路径不在项目根目录下: {relative_path}")
    if candidate.is_dir():
        raise PathResolutionError("当前实现要求输入文件相对路径，而不是目录路径。")
    return candidate


def detect_language(path: Path) -> str:
    language = SUPPORTED_BY_EXTENSION.get(path.suffix.lower())
    if not language:
        raise UnsupportedLanguageError(f"暂不支持该语言或扩展名: {path.suffix}")
    return language


def _should_skip(path: Path, cfg: SdocConfig, root: Path) -> bool:
    parts = path.relative_to(root).parts
    if not cfg.include_hidden and any(part.startswith(".") for part in parts):
        return True
    lower_parts = [part.lower() for part in parts]
    if not cfg.include_tests and any(part in {"test", "tests", "__tests__"} for part in lower_parts):
        return True
    if path.stat().st_size > cfg.max_file_size_kb * 1024:
        return True
    return False


def _walk_with_depth(root: Path, depth: int) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        relative_depth = len(path.relative_to(root).parts) - 1
        if relative_depth <= depth:
            yield path


def collect_parse_tasks(entry_file: Path, cfg: SdocConfig) -> List[ParseTask]:
    target_dir = entry_file.parent
    tasks: List[ParseTask] = []
    for path in _walk_with_depth(target_dir, cfg.recursive_depth):
        if _should_skip(path, cfg, target_dir):
            continue
        if path.suffix.lower() not in set(cfg.supported_extensions):
            continue
        try:
            language = detect_language(path)
        except UnsupportedLanguageError:
            continue
        source = path.read_bytes()
        tasks.append(
            ParseTask(
                path=path,
                language=language,
                source=source,
                source_hash=sha256_bytes(path.as_posix().encode("utf-8") + b"::" + source),
            )
        )
    tasks.sort(key=lambda t: (0 if t.path == entry_file else 1, t.path.as_posix()))
    return tasks[: cfg.max_files]


def output_markdown_path(entry_file: Path) -> Path:
    return entry_file.with_suffix(".md")
