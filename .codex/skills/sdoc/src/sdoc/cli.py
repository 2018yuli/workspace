from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

from .errors import SdocError
from .logging_utils import configure_logging
from .service import generate_document, load_runtime_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sdoc", description="生成通俗易懂的代码架构文档")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="根据相对路径生成 Markdown 架构文档")
    generate.add_argument("relative_path", help="项目根目录下的源码相对路径")
    generate.add_argument("--config", dest="config_path", help="配置文件路径，默认自动向上查找 sdoc.toml")
    generate.add_argument("--project-root", dest="project_root", help="项目根目录，默认取配置值或当前目录")
    generate.add_argument("--depth", dest="recursive_depth", type=int, help="递归扫描深度")
    generate.add_argument("--max-files", dest="max_files", type=int, help="最多分析多少个文件")
    generate.add_argument("--max-snippets", dest="max_snippets", type=int, help="文档内最多输出多少个代码片段")
    generate.add_argument("--include-tests", action="store_true", help="分析 tests 目录")
    generate.add_argument("--no-cache", action="store_true", help="关闭缓存")
    generate.add_argument("--log-level", default=None, help="日志级别，例如 INFO 或 DEBUG")
    generate.add_argument("--json", action="store_true", help="命令完成后输出 JSON 结果摘要")

    show_config = subparsers.add_parser("print-config", help="查看 sdoc 生效配置")
    show_config.add_argument("relative_path", nargs="?", default=".", help="用于定位配置文件起点的相对路径")
    show_config.add_argument("--config", dest="config_path", help="显式配置文件路径")

    return parser


def cli(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "print-config":
        cfg = load_runtime_config(relative_path=args.relative_path, config_path=args.config_path)
        print(json.dumps(asdict(cfg), ensure_ascii=False, indent=2))
        return 0

    overrides = {
        "project_root": args.project_root,
        "recursive_depth": args.recursive_depth,
        "max_files": args.max_files,
        "max_snippets": args.max_snippets,
        "include_tests": args.include_tests or None,
        "enable_cache": False if args.no_cache else None,
        "log_level": args.log_level,
    }
    cfg = load_runtime_config(relative_path=args.relative_path, config_path=args.config_path, overrides=overrides)
    configure_logging(cfg.log_level)

    try:
        result = generate_document(args.relative_path, config_path=args.config_path, overrides=overrides)
    except SdocError as exc:
        print(f"[sdoc] 失败: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # pragma: no cover - 兜底
        print(f"[sdoc] 未预期异常: {exc}", file=sys.stderr)
        return 3

    if args.json:
        payload = {
            "entry_file": result.entry_file,
            "output_file": result.output_file,
            "languages": result.languages,
            "analyzed_files": result.analyzed_files,
            "cache_hits": result.cache_hits,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"已生成: {result.output_file}")
        print(f"分析文件数: {len(result.analyzed_files)}")
        print(f"缓存命中: {result.cache_hits}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(cli())
