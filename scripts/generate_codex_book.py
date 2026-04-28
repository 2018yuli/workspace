#!/usr/bin/env python3
from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("/config/workspace")
PAGES_DIR = ROOT / "docs/official-zh/pages"
BOOK_DIR = ROOT / "docs/official-zh/book"
NAV_FILE = PAGES_DIR / "developers-openai-com-codex.md"


@dataclass
class NavItem:
    level: int
    title: str
    url: str | None
    section: str


def slug_from_url(url: str) -> str:
    path = re.sub(r"^https?://developers\.openai\.com/", "", url).strip("/")
    if not path:
        path = "codex"
    return path.replace("/", "-")


def page_path_from_url(url: str) -> Path:
    slug = slug_from_url(url)
    return PAGES_DIR / f"developers-openai-com-{slug}.md"


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_nav() -> list[NavItem]:
    raw = NAV_FILE.read_text(encoding="utf-8")
    lines = raw.splitlines()
    items: list[NavItem] = []
    current_section = ""
    in_nav = False
    for line in lines:
        if line.startswith("### 开始使用") or line.startswith("### 入门"):
            in_nav = True
        if not in_nav:
            continue
        if line.startswith("[API"):
            break
        if line.startswith("### "):
            current_section = line[4:].strip()
            continue
        m = re.match(r"^(\s*)- \[([^\]]+)\]\((https://developers\.openai\.com/[^)]+)\)", line)
        if m:
            spaces, title, url = m.groups()
            level = len(spaces) // 2
            if "/blog/" in url or "/cookbook/" in url or "community" in url or "platform.openai.com" in url:
                continue
            items.append(NavItem(level=level, title=title.strip(), url=url.strip(), section=current_section))
            continue
        m2 = re.match(r"^(\s*)- ([^\[][^ ].+)$", line)
        if m2:
            spaces, title = m2.groups()
            level = len(spaces) // 2
            items.append(NavItem(level=level, title=title.strip(), url=None, section=current_section))
    return items


def extract_body(page: Path) -> tuple[str, list[tuple[str, list[str]]]]:
    raw = page.read_text(encoding="utf-8")
    title_match = re.search(r'^title:\s*"(.*)"\s*$', raw, re.M)
    title = title_match.group(1) if title_match else page.stem
    if "复制页面" in raw:
        body = raw.split("复制页面", 1)[1]
    else:
        body = raw
    lines = body.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_heading = "正文"
    current_paras: list[str] = []

    def flush():
        nonlocal current_heading, current_paras
        cleaned = [clean_inline(p) for p in current_paras if clean_inline(p)]
        if cleaned:
            sections.append((current_heading, cleaned))
        current_paras = []

    buffer: list[str] = []
    for line in lines:
        if re.match(r"^##+ ", line):
            if buffer:
                current_paras.extend([" ".join(buffer)])
                buffer = []
            flush()
            current_heading = re.sub(r"^##+ ", "", line).strip()
            continue
        if line.strip().startswith("![") or line.strip().startswith("[!") or line.strip().startswith("![]("):
            continue
        if line.strip().startswith("```"):
            if buffer:
                current_paras.extend([" ".join(buffer)])
                buffer = []
            current_paras.append(line.strip())
            continue
        if not line.strip():
            if buffer:
                current_paras.extend([" ".join(buffer)])
                buffer = []
            continue
        if line.strip().startswith("- "):
            if buffer:
                current_paras.extend([" ".join(buffer)])
                buffer = []
            current_paras.append(line.strip())
            continue
        if line.strip().startswith("[") and "http" in line:
            continue
        buffer.append(line.strip())
    if buffer:
        current_paras.extend([" ".join(buffer)])
    flush()
    return title, sections


def choose_analogy(title: str, text: str) -> tuple[str, str]:
    t = f"{title} {text}"
    rules = [
        ("自动化", "把自动化看成数列中的递推过程。你先给出初值和递推规则，之后系统会在每个时刻自动算出下一项。", "严格地说，自动化就是一个由“触发条件 + 指令 + 执行环境 + 输出汇总”组成的重复映射。"),
        ("提示", "把提示词想成做几何证明时的题目条件。条件越完整，证明路径越短；条件越含糊，辅助线就会乱加。", "严格地说，提示是对目标函数、约束条件和验证标准的联合描述。"),
        ("线程", "线程像解一道多步函数题时保留下来的草稿纸。后一步是否顺利，依赖前面保留下来的中间结果。", "严格地说，线程是一个按时间顺序累积状态的信息序列。"),
        ("子代理", "子代理像把一道大题拆成几道小问：主问题不变，但每个小问由更专门的人分别处理。", "严格地说，子代理是主代理派生出的局部求解器，拥有较小的任务域和更清晰的边界。"),
        ("沙盒", "沙盒像在平面直角坐标系里画出的一个有边界的定义域。函数只能在定义域内取值，超出范围就不允许。", "严格地说，沙盒是执行权限、文件范围和外部访问能力的约束集合。"),
        ("配置", "配置像给函数预先设定参数。公式不变，但参数不同，图像和输出会明显不同。", "严格地说，配置是运行时行为的参数化描述。"),
        ("安全", "安全像不等式约束。你不是只关心最优解，还要保证所有可行解都落在安全区域内。", "严格地说，安全机制是对代理行为加入的一组风险边界与审计条件。"),
        ("模型", "模型选择像选解题工具：心算快但不适合难题，复杂题可能要用更强的公式和更长的推导。", "严格地说，模型是具有特定上下文窗口、推理能力和工具调用风格的求解器。"),
        ("工作流", "工作流像标准解题模板。先审题，再列式，再求解，再验算。", "严格地说，工作流是多个步骤之间按依赖关系构成的执行图。"),
        ("记忆", "记忆像你在数学习题本上积累的错题本。新题并不直接等于旧题，但旧经验会影响下一次求解。", "严格地说，记忆是跨线程保留、可被后续任务调用的持久化上下文。"),
        ("插件", "插件像给函数增加外部变量来源。原来只能用题目内数据，现在可以调用外部表格和工具。", "严格地说，插件是把外部能力封装为标准接口，供代理在推理过程中调用。"),
    ]
    for key, analogy, definition in rules:
        if key in t:
            return analogy, definition
    return (
        "把这一章看成在学习一个新的数学对象。先认识它的定义，再看它的性质，最后看它怎么解题。",
        "严格地说，这一章讨论的是 Codex 体系中的一个功能模块，以及它与输入、状态、输出之间的关系。",
    )


def explain_section(heading: str, paragraphs: list[str]) -> str:
    chunks = []
    intro = f"### {heading}\n"
    chunks.append(intro)
    chunks.append("先说直白版：")
    for para in paragraphs[:4]:
        if para.startswith("- "):
            chunks.append(f"- {clean_inline(para[2:])}")
        elif para.startswith("```"):
            continue
        else:
            chunks.append(textwrap.fill(para, width=88))
    chunks.append("")
    chunks.append("把它理解成一个更严谨的过程：")
    numbered: list[str] = []
    for para in paragraphs[:4]:
        if para.startswith("```"):
            continue
        sentence = clean_inline(para)
        if sentence.startswith("- "):
            sentence = sentence[2:]
        numbered.append(sentence)
    if numbered:
        for idx, item in enumerate(numbered, start=1):
            chunks.append(f"{idx}. {item}")
    return "\n".join(chunks).strip()


def chapter_content(chapter_no: int, display_title: str, page_title: str, source_url: str, body_sections: list[tuple[str, list[str]]]) -> str:
    joined = " ".join(p for _, ps in body_sections[:3] for p in ps[:2])
    analogy, definition = choose_analogy(display_title + " " + page_title, joined)
    takeaway_points: list[str] = []
    for heading, paras in body_sections[:3]:
        if heading != "正文":
            takeaway_points.append(f"`{heading}`：{clean_inline(paras[0])[:70]}。")
        elif paras:
            takeaway_points.append(clean_inline(paras[0])[:70] + "。")
    if not takeaway_points:
        takeaway_points.append("本章主要介绍这一功能的用途、边界和典型使用方式。")

    parts = [
        f"# 第{chapter_no:02d}章 {display_title}",
        "",
        f"> 原始页面：[{page_title}]({source_url})",
        "",
        "## 本章目标",
        "这章面向会 Python、懂一点 LangChain、但还没有真正把 AI Agent 当成工程系统来使用的读者。重点不是背术语，而是把“这个功能为什么存在、什么时候该用、怎么安全地用”讲清楚。",
        "",
        "## 先用一个高中数学类比",
        analogy,
        "",
        "## 严谨定义",
        definition,
        "",
        "## 你读完应该抓住什么",
    ]
    for point in takeaway_points:
        parts.append(f"- {point}")
    parts.extend([
        "",
        "## 分步理解",
    ])
    for heading, paras in body_sections[:5]:
        if not paras:
            continue
        parts.append(explain_section(heading, paras))
        parts.append("")
    parts.extend([
        "## 实战视角",
        "如果你会 Python，可以把这一章里的能力理解成一个可以读文件、调工具、保留状态、按规则执行的程序代理。它和 LangChain 的链、工具、记忆很像，但 Codex 更强调真实工程环境：仓库、命令、审阅、权限、并行任务。",
        "",
        "## 给高中水平读者的最后一句话",
        "不要急着一次学完整个体系。把每章都当成“定义 + 例子 + 适用边界”三件事去掌握，AI Agent 就会从模糊概念变成你能实际操作的工程对象。",
        "",
    ])
    return "\n".join(parts)


def build_book() -> None:
    nav = parse_nav()
    BOOK_DIR.mkdir(parents=True, exist_ok=True)

    chapter_index = 1
    manifest: list[tuple[int, str, str, str]] = []
    written_urls: set[str] = set()

    for item in nav:
        if not item.url or item.url in written_urls:
            continue
        page = page_path_from_url(item.url)
        if not page.exists():
            continue
        written_urls.add(item.url)
        page_title, sections = extract_body(page)
        filename = f"{chapter_index:02d}-{slug_from_url(item.url)}.md"
        display_title = item.title
        content = chapter_content(chapter_index, display_title, page_title, item.url, sections)
        (BOOK_DIR / filename).write_text(content, encoding="utf-8")
        manifest.append((chapter_index, item.section, display_title, filename))
        chapter_index += 1

    lines = [
        "# Codex 通俗书",
        "",
        "这套书根据 `docs/official-zh/pages` 中的官方中文页面整理而成，保持原导航顺序，同时把表达方式改成更适合入门读者的书籍体例。",
        "",
        "目标读者：",
        "- 会 Python。",
        "- 用过 LangChain 或知道 tool / memory / agent 这些词。",
        "- 还不太会把 AI Agent 当成完整工程系统来使用。",
        "- 喜欢通过高中数学的类比来建立直觉。",
        "",
        "阅读方法：",
        "1. 先看“开始使用”和“概念”，建立整体坐标系。",
        "2. 再根据你实际使用的入口选择 `App`、`IDE`、`CLI` 或 `Cloud`。",
        "3. 配置、安全、自动化三部分建议结合自己的项目边读边试。",
        "",
        "## 目录",
        "",
    ]
    current_section = None
    for chapter_no, section, title, filename in manifest:
        if section != current_section:
            current_section = section
            lines.append(f"### {section}")
        lines.append(f"- [第{chapter_no:02d}章 {title}](./{filename})")
    (BOOK_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_book()
