from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, Optional

from .analysis import (
    LANGUAGE_SPECS,
    analyze_tasks,
    build_flow_steps,
    build_mermaid,
    build_module_edges,
    collect_difficulty_notes,
    collect_supplemental_texts,
    enrich_snippets,
    infer_executive_summary,
    select_top_symbols,
)
from .cache import CacheStore
from .config import SdocConfig, find_config, load_config, update_config
from .errors import DocumentGenerationError
from .fs import collect_parse_tasks, detect_language, output_markdown_path, resolve_target
from .models import GenerationArtifacts
from .template import build_template_context, render_markdown

logger = logging.getLogger(__name__)


def load_runtime_config(
    *,
    relative_path: str,
    config_path: Optional[str] = None,
    overrides: Optional[Dict[str, Any]] = None,
) -> SdocConfig:
    probe = Path.cwd() / relative_path
    discovered = find_config(probe) if config_path is None else Path(config_path)
    cfg = load_config(str(discovered) if discovered else None)
    if discovered is not None and not Path(cfg.project_root).is_absolute():
        cfg = update_config(cfg, {"project_root": str((Path(discovered).parent / cfg.project_root).resolve())})
    if overrides:
        cfg = update_config(cfg, overrides)
    return cfg


def generate_document(
    relative_path: str,
    *,
    config_path: Optional[str] = None,
    overrides: Optional[Dict[str, Any]] = None,
) -> GenerationArtifacts:
    cfg = load_runtime_config(relative_path=relative_path, config_path=config_path, overrides=overrides)
    root = cfg.root_path()
    entry_file = resolve_target(relative_path, root)
    language = detect_language(entry_file)
    if language not in LANGUAGE_SPECS:
        raise DocumentGenerationError(f"入口语种未实现解析器: {language}")

    tasks = collect_parse_tasks(entry_file, cfg)
    if not tasks:
        raise DocumentGenerationError("在目标目录内没有找到可分析的源码文件。")

    cache = CacheStore(root / cfg.cache_file, version=cfg.cache_version, enabled=cfg.enable_cache)
    cache_hits = 0
    analyses = []
    pending_tasks = []
    for task in tasks:
        hit = cache.get(task.source_hash)
        if hit is not None:
            analyses.append(hit)
            cache_hits += 1
        else:
            pending_tasks.append(task)

    if pending_tasks:
        parsed = analyze_tasks(pending_tasks, cfg)
        for item in parsed:
            cache.put(item)
        analyses.extend(parsed)
    analyses.sort(key=lambda item: item.file_path)
    cache.save()

    supplemental_texts = collect_supplemental_texts(entry_file, cfg)
    executive_summary, functional_description, business_concepts = infer_executive_summary(
        entry_file,
        analyses,
        supplemental_texts,
        cfg,
    )
    key_symbols = select_top_symbols(
        analyses,
        limit=cfg.max_definition_table_rows,
        prefer_entry_file=entry_file.as_posix(),
    )
    flow_steps = build_flow_steps(entry_file, analyses)
    flow_mermaid = build_mermaid(flow_steps)
    difficulties = collect_difficulty_notes(analyses, cfg.max_difficulty_notes)
    module_edges = build_module_edges(analyses)
    snippet_symbols = enrich_snippets(
        select_top_symbols(analyses, limit=cfg.max_snippets, prefer_entry_file=entry_file.as_posix()),
        cfg.snippet_max_lines,
    )
    languages = sorted({analysis.language for analysis in analyses})
    title = f"{entry_file.stem} {cfg.template_title_suffix}" if cfg.template_title_suffix else entry_file.stem
    template_context = build_template_context(
        title=title,
        entry_file=entry_file.as_posix(),
        target_directory=entry_file.parent.as_posix(),
        languages=languages,
        executive_summary=executive_summary,
        functional_description=functional_description,
        business_concepts=business_concepts,
        key_symbols=key_symbols,
        flow_steps=flow_steps,
        flow_mermaid=flow_mermaid,
        difficulty_notes=difficulties,
        module_edges=module_edges,
        snippets=snippet_symbols,
        analyzed_files=[analysis.file_path for analysis in analyses],
    )
    markdown = render_markdown(template_context)
    output_file = output_markdown_path(entry_file)
    output_file.write_text(markdown, encoding=cfg.output_encoding)
    logger.info("已写出文档: %s", output_file)

    return GenerationArtifacts(
        entry_file=entry_file.as_posix(),
        target_directory=entry_file.parent.as_posix(),
        output_file=output_file.as_posix(),
        markdown=markdown,
        languages=languages,
        analyzed_files=[analysis.file_path for analysis in analyses],
        symbols=key_symbols,
        summaries=functional_description,
        business_concepts=business_concepts,
        flow_steps=flow_steps,
        difficulties=difficulties,
        module_edges=module_edges,
        cache_hits=cache_hits,
    )
