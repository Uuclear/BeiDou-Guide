#!/usr/bin/env python3
"""
从本地 BeiDou-Server/gms-server 源码生成「公开类型 + 方法签名」索引 Markdown。
默认读取环境变量 BEIDOU_SERVER_ROOT；若未设置，尝试相对仓库根目录的上级 ../BeiDou-Server。
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

TYPE_DECL_RE = re.compile(
    r"^\s*public\s+(?:abstract\s+|final\s+|sealed\s+|non-sealed\s+)*"
    r"(?:class|interface|enum|@interface)\s+(\w+)",
    re.M,
)

def find_server_root() -> Path:
    env = os.environ.get("BEIDOU_SERVER_ROOT")
    if env:
        p = Path(env).expanduser().resolve()
        if p.is_dir():
            return p
    here = Path(__file__).resolve().parent.parent
    candidates = [
        here.parent / "BeiDou-Server" / "gms-server",
        here / "BeiDou-Server" / "gms-server",
        Path("/tmp/BeiDou-Server/gms-server"),
    ]
    for c in candidates:
        java_root = c / "src" / "main" / "java" / "org" / "gms"
        if java_root.is_dir():
            return c
    print(
        "错误：未找到 gms-server 源码目录。请克隆 BeiDou-Server 并设置：\n"
        "  export BEIDOU_SERVER_ROOT=/path/to/BeiDou-Server/gms-server",
        file=sys.stderr,
    )
    sys.exit(1)


def package_of(content: str) -> str:
    m = re.search(r"^\s*package\s+([\w.]+)\s*;", content, re.M)
    return m.group(1) if m else ""


def public_type_line(content: str) -> str | None:
    m = TYPE_DECL_RE.search(content)
    if not m:
        return None
    for line in content.splitlines():
        if re.search(
            r"public\s+(?:abstract\s+|final\s+)*\s*(?:class|interface|enum|@interface)\s+"
            + re.escape(m.group(1))
            + r"\b",
            line,
        ):
            return line.strip()
    return None


def _paren_depth_delta(s: str) -> int:
    return s.count("(") - s.count(")")


def extract_methods(content: str) -> list[str]:
    """提取 public 方法签名（含多行参数列表）；构造器与接口方法均计入。"""
    lines = content.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line
        s = line.strip()
        if s.startswith("//") or s.startswith("*") or s.startswith("/*"):
            i += 1
            continue
        if "public" not in line or "(" not in line:
            i += 1
            continue
        pre_paren = s.split("(", 1)[0]
        if re.search(r"\b(class|interface|enum|@interface)\b", pre_paren):
            i += 1
            continue
        if not re.search(r"\bpublic\b", s):
            i += 1
            continue
        block_lines = [line.rstrip()]
        paren_from = raw.find("(")
        if paren_from < 0:
            i += 1
            continue
        depth = _paren_depth_delta(raw[paren_from:])
        j = i
        while depth > 0 and j + 1 < len(lines):
            j += 1
            nxt = lines[j]
            block_lines.append(nxt.rstrip())
            depth += _paren_depth_delta(nxt)
        merged = " ".join(x.strip() for x in block_lines if x.strip())
        merged = merged.split("{", 1)[0].strip().rstrip(";").strip()
        if len(merged) > 400:
            merged = merged[:397] + "..."
        if merged.startswith("public ") and "(" in merged:
            out.append(merged)
        i = j + 1
    return out


def main() -> None:
    root = find_server_root()
    workspace = Path(__file__).resolve().parent.parent
    try:
        root_display = str(root.resolve().relative_to(workspace))
    except ValueError:
        root_display = str(root.resolve())
    java_root = root / "src" / "main" / "java" / "org" / "gms"
    files = sorted(java_root.rglob("*.java"))
    out_lines: list[str] = [
        "# gms-server 源码索引（公开类型与方法签名）",
        "",
        "> 本文件由 `scripts/generate-gms-server-api-index.py` **自动生成**，用于在约 1100+ 个 Java 源文件中快速定位类与公开方法。",
        "> 叙述性说明见 [09-源码深度导读.md](../09-源码深度导读.md)。",
        "",
        "> 生成所用源码根目录：环境变量 `BEIDOU_SERVER_ROOT` 指向的 `gms-server`，或脚本自动探测到的本地 clone。",
        f"> 本次生成使用的 `gms-server` 路径（相对本仓库根目录，若无法相对则给绝对路径）：`{root_display}`",
        f"> 源文件数：{len(files)}",
        "",
        "---",
        "",
    ]

    by_pkg: dict[str, list[tuple[str, str, list[str]]]] = {}
    for fp in files:
        rel = fp.relative_to(java_root)
        try:
            text = fp.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            out_lines.append(f"<!-- 跳过读取失败: {fp} {e} -->")
            continue
        pkg = package_of(text)
        if not pkg:
            continue
        type_line = public_type_line(text)
        simple = fp.stem
        fq = f"{pkg}.{simple}"
        methods = extract_methods(text)
        key = pkg
        by_pkg.setdefault(key, []).append((fq, type_line or f"(未解析) {simple}", methods))

    for pkg in sorted(by_pkg.keys()):
        out_lines.append(f"## `{pkg}`")
        out_lines.append("")
        for fq, type_line, methods in sorted(by_pkg[pkg], key=lambda x: x[0]):
            out_lines.append(f"### `{fq}`")
            if type_line:
                out_lines.append(f"- 声明: `{type_line}`")
            out_lines.append(f"- 方法数（启发式提取）: {len(methods)}")
            if methods:
                out_lines.append("")
                out_lines.append("```text")
                for m in methods:
                    out_lines.append(m)
                out_lines.append("```")
            out_lines.append("")

    target = Path(__file__).resolve().parent.parent / "docs" / "reference" / "gms-server-api-index.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"已写入: {target}")


if __name__ == "__main__":
    main()
