#!/usr/bin/env python3
"""
生成“全量级”源码符号文档：
1) gms-server(Java): 包、类型、字段、构造器、方法（public/protected/private/default）
2) gms-ui(TS/Vue): export 符号、setup 中函数、script block 中函数
3) BeiDou-ijl15(C/C++): 顶层函数、类方法、静态成员声明
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


def rel_display(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path.resolve())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_repo(root_env: str, guesses: list[Path], must_have: Path) -> Path:
    env = os.environ.get(root_env)
    if env:
        p = Path(env).expanduser().resolve()
        if (p / must_have).exists():
            return p
    for g in guesses:
        if (g / must_have).exists():
            return g
    return Path()


JAVA_TYPE_RE = re.compile(
    r"^\s*(?:public|protected|private)?\s*(?:abstract\s+|final\s+|sealed\s+|non-sealed\s+)*"
    r"(class|interface|enum|@interface)\s+(\w+)",
    re.M,
)
JAVA_MEMBER_METHOD_RE = re.compile(
    r"^\s*(?:@\w+(?:\([^)]*\))?\s*)*"
    r"(?:(?:public|protected|private)\s+)?"
    r"(?:(?:static|final|abstract|synchronized|native|strictfp|default)\s+)*"
    r"(?:<[^>{};]+>\s+)?"
    r"(?:[\w\[\].<>?,]+\s+)?"
    r"(?P<name>\w+)\s*\(",
)
JAVA_MEMBER_FIELD_RE = re.compile(
    r"^\s*(?:@\w+(?:\([^)]*\))?\s*)*"
    r"(?:(?:public|protected|private)\s+)?"
    r"(?:(?:static|final|transient|volatile)\s+)*"
    r"[\w\[\].<>?,]+\s+(?P<name>\w+)\s*(?:=\s*[^;]+)?;",
)
JAVA_SKIP_METHOD = {"if", "for", "while", "switch", "catch", "return", "throw", "new"}
JAVA_SKIP_FIELD = {"return", "new"}


def gen_gms_server_symbols(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_SERVER_REPO",
        [workspace / "BeiDou-Server", Path("/tmp/BeiDou-Server")],
        Path("gms-server/src/main/java/org/gms"),
    )
    if not repo:
        raise SystemExit("未找到 BeiDou-Server 仓库，请设置 BEIDOU_SERVER_REPO。")

    java_root = repo / "gms-server" / "src" / "main" / "java" / "org" / "gms"
    files = sorted(java_root.rglob("*.java"))
    out: list[str] = [
        "# gms-server 全量符号索引（含非 public）",
        "",
        "> 自动生成：`scripts/generate-full-symbol-docs.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> Java 文件数：{len(files)}",
        "",
        "---",
        "",
    ]

    for fp in files:
        text = read_text(fp)
        pkg_m = re.search(r"^\s*package\s+([\w.]+)\s*;", text, re.M)
        pkg = pkg_m.group(1) if pkg_m else "(no package)"
        rel = fp.relative_to(java_root)
        out.append(f"## `{pkg}` / `{rel}`")
        out.append("")

        types = JAVA_TYPE_RE.findall(text)
        if types:
            out.append("### 类型声明")
            out.append("```text")
            for t_kind, t_name in types:
                out.append(f"{t_kind} {t_name}")
            out.append("```")
            out.append("")

        lines = text.splitlines()
        fields: list[str] = []
        methods: list[str] = []
        depth = 0
        in_block_comment = False
        for raw in lines:
            line = raw.strip()
            if not line:
                depth += raw.count("{") - raw.count("}")
                continue
            if in_block_comment:
                if "*/" in line:
                    in_block_comment = False
                depth += raw.count("{") - raw.count("}")
                continue
            if line.startswith("/*"):
                if "*/" not in line:
                    in_block_comment = True
                depth += raw.count("{") - raw.count("}")
                continue
            if line.startswith("//"):
                depth += raw.count("{") - raw.count("}")
                continue

            # 仅在类体第一层抓成员，尽量排除方法体内局部变量
            if depth == 1:
                if "(" in line and not line.endswith(";"):
                    if line.startswith("@"):
                        depth += raw.count("{") - raw.count("}")
                        continue
                    merged = line
                    if ")" not in line:
                        # 合并多行参数列表
                        for nxt in lines[lines.index(raw) + 1:]:
                            merged = f"{merged} {nxt.strip()}"
                            if ")" in nxt:
                                break
                    mm = JAVA_MEMBER_METHOD_RE.match(merged)
                    if mm:
                        name = mm.group("name")
                        if name not in JAVA_SKIP_METHOD and " class " not in merged and " interface " not in merged and " enum " not in merged:
                            methods.append(merged.split("{", 1)[0].strip())
                elif line.endswith(";") and "(" not in line:
                    fm = JAVA_MEMBER_FIELD_RE.match(line)
                    if fm:
                        fname = fm.group("name")
                        if fname not in JAVA_SKIP_FIELD and " class " not in line and " interface " not in line and " enum " not in line:
                            fields.append(line.rstrip(";"))

            depth += raw.count("{") - raw.count("}")

        out.append(f"- 字段候选数: {len(fields)}")
        if fields:
            out.append("```text")
            out.extend(fields[:400])
            if len(fields) > 400:
                out.append(f"... ({len(fields) - 400} more)")
            out.append("```")
        out.append("")

        out.append(f"- 方法/构造器候选数: {len(methods)}")
        if methods:
            out.append("```text")
            out.extend(methods[:1200])
            if len(methods) > 1200:
                out.append(f"... ({len(methods) - 1200} more)")
            out.append("```")
        out.append("")
        out.append("---")
        out.append("")

    target = out_dir / "gms-server-full-symbols.md"
    target.write_text("\n".join(out), encoding="utf-8")


TS_EXPORT_RE = re.compile(r"^\s*export\s+(?:default\s+)?(?:const|let|var|function|class|interface|type|enum)\s+(\w+)", re.M)
TS_FUNC_RE = re.compile(r"^\s*(?:async\s+)?function\s+(\w+)\s*\(", re.M)
TS_CONST_FN_RE = re.compile(r"^\s*const\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>", re.M)


def extract_vue_script_blocks(content: str) -> list[str]:
    blocks = []
    for m in re.finditer(r"<script[^>]*>(.*?)</script>", content, re.S | re.I):
        blocks.append(m.group(1))
    return blocks


def gen_gms_ui_symbols(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_SERVER_REPO",
        [workspace / "BeiDou-Server", Path("/tmp/BeiDou-Server")],
        Path("gms-ui/src"),
    )
    if not repo:
        raise SystemExit("未找到 BeiDou-Server 仓库中的 gms-ui。")
    src = repo / "gms-ui" / "src"
    files = sorted(list(src.rglob("*.ts")) + list(src.rglob("*.vue")))

    out = [
        "# gms-ui 全量符号索引",
        "",
        "> 自动生成：`scripts/generate-full-symbol-docs.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> TS/Vue 文件数：{len(files)}",
        "",
        "---",
        "",
    ]
    for fp in files:
        rel = fp.relative_to(src)
        text = read_text(fp)
        analy_text = text
        if fp.suffix == ".vue":
            analy_text = "\n\n".join(extract_vue_script_blocks(text))
        exports = TS_EXPORT_RE.findall(analy_text)
        funcs = TS_FUNC_RE.findall(analy_text)
        lambdas = TS_CONST_FN_RE.findall(analy_text)
        out.append(f"## `{rel}`")
        out.append(f"- export 符号数: {len(exports)}")
        out.append(f"- function 声明数: {len(funcs)}")
        out.append(f"- const 箭头函数数: {len(lambdas)}")
        if exports or funcs or lambdas:
            out.append("```text")
            for x in exports:
                out.append(f"export {x}")
            for x in funcs:
                out.append(f"function {x}(")
            for x in lambdas:
                out.append(f"const {x} = (...) =>")
            out.append("```")
        out.append("")
    (out_dir / "gms-ui-full-symbols.md").write_text("\n".join(out), encoding="utf-8")


CPP_CLASS_RE = re.compile(r"^\s*class\s+(\w+)", re.M)
CPP_METHOD_RE = re.compile(r"^\s*(?:[\w:<>,~*&\s]+)\s+(\w+)::(\w+)\s*\(", re.M)
CPP_FUNC_RE = re.compile(r"^\s*(?:extern\s+\"C\"\s+)?(?:__declspec\([^)]+\)\s*)*(?:[\w:<>,~*&\s]+)\s+(\w+)\s*\(", re.M)


def gen_ijl15_symbols(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_IJL15_REPO",
        [workspace / "BeiDou-ijl15", Path("/tmp/BeiDou-ijl15")],
        Path("ezorsia"),
    )
    if not repo:
        raise SystemExit("未找到 BeiDou-ijl15 仓库，请设置 BEIDOU_IJL15_REPO。")

    src = repo / "ezorsia"
    files = sorted(list(src.rglob("*.h")) + list(src.rglob("*.hpp")) + list(src.rglob("*.cpp")) + list(src.rglob("*.c")))
    out = [
        "# BeiDou-ijl15 全量符号索引",
        "",
        "> 自动生成：`scripts/generate-full-symbol-docs.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> C/C++ 文件数：{len(files)}",
        "",
        "---",
        "",
    ]
    for fp in files:
        rel = fp.relative_to(src)
        text = read_text(fp)
        classes = CPP_CLASS_RE.findall(text)
        methods = [f"{c}::{m}" for c, m in CPP_METHOD_RE.findall(text)]
        funcs = CPP_FUNC_RE.findall(text)
        out.append(f"## `{rel}`")
        out.append(f"- class 数: {len(classes)}")
        out.append(f"- 类方法定义数: {len(methods)}")
        out.append(f"- 顶层函数候选数: {len(funcs)}")
        if classes or methods or funcs:
            out.append("```text")
            for x in classes:
                out.append(f"class {x}")
            for x in methods:
                out.append(f"{x}(...)")
            for x in funcs[:800]:
                out.append(f"{x}(...)")
            if len(funcs) > 800:
                out.append(f"... ({len(funcs) - 800} more)")
            out.append("```")
        out.append("")
    (out_dir / "beidou-ijl15-full-symbols.md").write_text("\n".join(out), encoding="utf-8")


def write_summary(workspace: Path, out_dir: Path) -> None:
    content = """# 全量源码符号文档说明

你要求“全部”，本目录给出可检索的全量符号文档（自动生成）：

1. `gms-server-full-symbols.md`
   - 覆盖 gms-server 的 Java 文件
   - 包含类型声明、字段候选、方法/构造器候选（含非 public）
2. `gms-ui-full-symbols.md`
   - 覆盖 TS 与 Vue script block
   - 包含 export、function、箭头函数候选
3. `beidou-ijl15-full-symbols.md`
   - 覆盖 ezorsia 的 C/C++ 文件
   - 包含 class、类方法、顶层函数候选

> 注意：这类“全量”文档基于正则启发式提取，目标是“尽可能全 + 可搜索”；语义解释仍应结合对应源文件阅读。

## 生成方式

```bash
export BEIDOU_SERVER_REPO=/path/to/BeiDou-Server
export BEIDOU_IJL15_REPO=/path/to/BeiDou-ijl15
python3 scripts/generate-full-symbol-docs.py
```
"""
    (workspace / "docs" / "11-全量源码符号文档说明.md").write_text(content, encoding="utf-8")


def main() -> None:
    workspace = Path(__file__).resolve().parent.parent
    out_dir = workspace / "docs" / "reference"
    out_dir.mkdir(parents=True, exist_ok=True)
    gen_gms_server_symbols(workspace, out_dir)
    gen_gms_ui_symbols(workspace, out_dir)
    gen_ijl15_symbols(workspace, out_dir)
    write_summary(workspace, out_dir)
    print("已生成全量符号文档：")
    print(f"- {out_dir / 'gms-server-full-symbols.md'}")
    print(f"- {out_dir / 'gms-ui-full-symbols.md'}")
    print(f"- {out_dir / 'beidou-ijl15-full-symbols.md'}")
    print(f"- {workspace / 'docs' / '11-全量源码符号文档说明.md'}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"生成失败: {e}", file=sys.stderr)
        raise
