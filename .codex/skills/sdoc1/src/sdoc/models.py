from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List


@dataclass(slots=True)
class Symbol:
    name: str
    kind: str
    language: str
    file_path: str
    line_start: int
    line_end: int
    signature: str = ""
    is_public: bool = False
    doc: str = ""
    body_text: str = ""
    snippet: str = ""
    score: float = 0.0
    role_hint: str = ""
    difficulty_hint: str = ""
    calls: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Symbol":
        return cls(**data)


@dataclass(slots=True)
class FileAnalysis:
    file_path: str
    language: str
    source_hash: str
    imports: List[str] = field(default_factory=list)
    comments: List[str] = field(default_factory=list)
    file_summary_hints: List[str] = field(default_factory=list)
    symbols: List[Symbol] = field(default_factory=list)
    diagnostics: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["symbols"] = [symbol.to_dict() for symbol in self.symbols]
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FileAnalysis":
        symbols = [Symbol.from_dict(item) for item in data.get("symbols", [])]
        data = dict(data)
        data["symbols"] = symbols
        return cls(**data)


@dataclass(slots=True)
class FlowStep:
    title: str
    detail: str


@dataclass(slots=True)
class DifficultyNote:
    title: str
    explanation: str
    analogy: str


@dataclass(slots=True)
class GenerationArtifacts:
    entry_file: str
    target_directory: str
    output_file: str
    markdown: str
    languages: List[str]
    analyzed_files: List[str]
    symbols: List[Symbol]
    summaries: List[str]
    business_concepts: List[str]
    flow_steps: List[FlowStep]
    difficulties: List[DifficultyNote]
    module_edges: List[tuple[str, str]]
    cache_hits: int = 0


@dataclass(slots=True)
class ParseTask:
    path: Path
    language: str
    source: bytes
    source_hash: str


@dataclass(slots=True)
class TemplateContext:
    title: str
    entry_file: str
    target_directory: str
    languages: List[str]
    executive_summary: str
    functional_description: List[str]
    business_concepts: List[str]
    key_symbols: List[Symbol]
    flow_steps: List[FlowStep]
    flow_mermaid: str
    difficulty_notes: List[DifficultyNote]
    module_edges: List[tuple[str, str]]
    snippets: List[Symbol]
    generated_at: str
    analyzed_files: List[str]
