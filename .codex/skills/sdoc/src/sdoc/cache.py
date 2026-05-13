from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, Optional

from .models import FileAnalysis

logger = logging.getLogger(__name__)


class CacheStore:
    def __init__(self, path: Path, version: str, enabled: bool = True) -> None:
        self.path = path
        self.version = version
        self.enabled = enabled
        self._data: Dict[str, dict] = {"version": version, "entries": {}}
        if enabled:
            self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            self._data = json.loads(self.path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover - 仅日志路径
            logger.warning("读取缓存失败: %s", exc)
            self._data = {"version": self.version, "entries": {}}
        if self._data.get("version") != self.version:
            self._data = {"version": self.version, "entries": {}}

    def get(self, source_hash: str) -> Optional[FileAnalysis]:
        if not self.enabled:
            return None
        item = self._data.get("entries", {}).get(source_hash)
        if not item:
            return None
        return FileAnalysis.from_dict(item)

    def put(self, analysis: FileAnalysis) -> None:
        if not self.enabled:
            return
        self._data.setdefault("entries", {})[analysis.source_hash] = analysis.to_dict()

    def save(self) -> None:
        if not self.enabled:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
