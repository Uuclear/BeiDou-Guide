#!/usr/bin/env python3
"""
生成“逐符号中文职责注释”文档：
- gms-server(Java)
- gms-ui(TS/Vue)
- BeiDou-ijl15(C/C++)
"""
from __future__ import annotations

import os
import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel_display(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path.resolve())


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


def zh_for_symbol(name: str) -> str:
    n = name.lower()
    if n.startswith("get"):
        return "读取并返回状态/数据。"
    if n.startswith("set"):
        return "写入或更新状态字段。"
    if n.startswith("is") or n.startswith("has") or n.startswith("can"):
        return "进行条件判定并返回布尔结果。"
    if n.startswith("init"):
        return "初始化模块、资源或运行时状态。"
    if n.startswith("create") or n.startswith("new"):
        return "创建对象、会话或业务记录。"
    if n.startswith("update"):
        return "更新已有对象/配置/缓存。"
    if n.startswith("delete") or n.startswith("remove"):
        return "删除对象、关系或临时状态。"
    if n.startswith("load"):
        return "从外部来源加载数据（数据库/文件/配置）。"
    if n.startswith("save"):
        return "持久化当前状态到存储层。"
    if n.startswith("parse"):
        return "解析输入文本或二进制内容。"
    if n.startswith("validate") or n.startswith("check"):
        return "校验输入参数或业务约束。"
    if n.startswith("handle") or n.endswith("handler"):
        return "处理事件/请求/消息分发。"
    if n.startswith("send"):
        return "向外发送响应、消息或网络包。"
    if n.startswith("recv") or n.startswith("receive"):
        return "接收并解码输入数据。"
    if n.startswith("build"):
        return "构建输出对象、包体或配置。"
    if n.startswith("find") or n.startswith("list") or n.startswith("query"):
        return "查询并返回匹配集合或单项结果。"
    if n.startswith("login") or n.startswith("logout") or n.startswith("auth"):
        return "处理认证/会话生命周期。"
    return "通用业务逻辑入口，需结合实现查看细节。"


def zh_for_class(name: str) -> str:
    if name.endswith("Controller"):
        return "HTTP 接口层，负责参数接收、鉴权边界与调用 service。"
    if name.endswith("Service"):
        return "业务编排层，组织领域逻辑与持久化调用。"
    if name.endswith("Handler"):
        return "网络包/事件处理器，按 opcode 或事件类型分发处理。"
    if name.endswith("Mapper") or name.endswith("Dao"):
        return "数据访问层，负责 SQL 映射与实体读写。"
    if name.endswith("Config") or name.endswith("Properties"):
        return "配置绑定/初始化相关类型。"
    if name.endswith("Util"):
        return "工具类，封装无状态通用能力。"
    return "领域类型或功能模块，职责由同名文件实现定义。"


JAVA_TYPE_RE = re.compile(
    r"^\s*(?:public|protected|private)?\s*(?:abstract\s+|final\s+|sealed\s+|non-sealed\s+)*"
    r"(class|interface|enum|@interface)\s+(\w+)",
    re.M,
)
JAVA_METHOD_RE = re.compile(
    r"^\s*(?:@\w+(?:\([^)]*\))?\s*)*"
    r"(?:(?:public|protected|private)\s+)?"
    r"(?:(?:static|final|abstract|synchronized|native|strictfp|default)\s+)*"
    r"(?:<[^>{};]+>\s+)?"
    r"(?:[\w\[\].<>?,]+\s+)?"
    r"(?P<name>\w+)\s*\(",
)
JAVA_SKIP = {"if", "for", "while", "switch", "catch", "return", "throw", "new"}


def _java_file_symbol_section(fp: Path, root: Path) -> list[str]:
    """单文件逐符号块（不含文件级标题）。"""
    text = read_text(fp)
    rel = fp.relative_to(root)
    lines_out: list[str] = [
        f"## `{rel}`",
        "",
    ]
    for kind, cname in JAVA_TYPE_RE.findall(text):
        lines_out.append(f"- `{kind} {cname}`：{zh_for_class(cname)}")
    lines = text.splitlines()
    depth = 0
    in_comment = False
    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if in_comment:
            if "*/" in s:
                in_comment = False
            depth += raw.count("{") - raw.count("}")
            i += 1
            continue
        if s.startswith("/*"):
            if "*/" not in s:
                in_comment = True
            depth += raw.count("{") - raw.count("}")
            i += 1
            continue
        if s.startswith("//"):
            depth += raw.count("{") - raw.count("}")
            i += 1
            continue
        if depth == 1 and "(" in s and not s.startswith("@"):
            merged = s
            paren = s.count("(") - s.count(")")
            j = i
            while paren > 0 and j + 1 < len(lines):
                j += 1
                nxt = lines[j].strip()
                merged = f"{merged} {nxt}"
                paren += nxt.count("(") - nxt.count(")")
            m = JAVA_METHOD_RE.match(merged)
            if m:
                name = m.group("name")
                if name not in JAVA_SKIP:
                    sig = merged.split("{", 1)[0].rstrip(";").strip()
                    if " class " in sig or " interface " in sig or " enum " in sig:
                        depth += raw.count("{") - raw.count("}")
                        i += 1
                        continue
                    lines_out.append(f"  - `{sig}`：{zh_for_symbol(name)}")
            i = j
        depth += raw.count("{") - raw.count("}")
        i += 1
    lines_out.append("")
    return lines_out


def _gms_server_volume_key(rel: Path) -> str:
    """按 org/gms 下一级目录分卷；包根下直接放的 Java 归入 _root。"""
    if len(rel.parts) == 1:
        return "_root"
    return rel.parts[0]


def gen_server_notes(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_SERVER_REPO",
        [workspace / "BeiDou-Server", Path("/tmp/BeiDou-Server")],
        Path("gms-server/src/main/java/org/gms"),
    )
    if not repo:
        raise SystemExit("未找到 BeiDou-Server。")

    root = repo / "gms-server" / "src" / "main" / "java" / "org" / "gms"
    files = sorted(root.rglob("*.java"))
    vol_dir = out_dir / "gms-server-symbol-notes"
    vol_dir.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list[Path]] = {}
    for fp in files:
        rel = fp.relative_to(root)
        key = _gms_server_volume_key(rel)
        buckets.setdefault(key, []).append(fp)

    # 分卷正文
    for vol, fps in sorted(buckets.items(), key=lambda x: (x[0] != "_root", x[0])):
        body: list[str] = [
            f"# gms-server 逐符号中文职责 · 分卷 `{vol}`",
            "",
            "> 自动生成：`scripts/generate-symbol-notes.py`",
            f"> 源码路径：`{rel_display(repo, workspace)}`",
            f"> 本分卷 Java 文件数：{len(fps)}",
            "",
            f"[← 返回分卷索引](../gms-server-symbol-notes-README.md)",
            "",
            "---",
            "",
        ]
        for fp in sorted(fps):
            body.extend(_java_file_symbol_section(fp, root))
        safe = vol.replace("/", "_").replace("\\", "_")
        (vol_dir / f"{safe}.md").write_text("\n".join(body), encoding="utf-8")

    # 分卷索引表
    index_lines: list[str] = [
        "# gms-server 逐符号中文职责 · 分卷索引",
        "",
        "> 自动生成：`scripts/generate-symbol-notes.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> Java 文件总数：{len(files)}",
        "",
        "按 `org/gms` 下**一级目录**拆分（与源码目录一致），便于按模块打开与搜索。",
        "",
        "| 分卷 | Java 文件数 | 链接 |",
        "|------|---------------|------|",
    ]
    for vol, fps in sorted(buckets.items(), key=lambda x: (x[0] != "_root", x[0])):
        safe = vol.replace("/", "_").replace("\\", "_")
        index_lines.append(f"| `{vol}` | {len(fps)} | [打开](gms-server-symbol-notes/{safe}.md) |")
    index_lines.extend(
        [
            "",
            "---",
            "",
            "根目录 `gms-server-symbol-notes.md` 仅作跳转，避免单文件过大。",
        ]
    )
    (out_dir / "gms-server-symbol-notes-README.md").write_text("\n".join(index_lines), encoding="utf-8")

    stub = "\n".join(
        [
            "# gms-server 逐符号中文职责索引（已分卷）",
            "",
            "单文件体量过大，已按 `org/gms` 下一级目录拆成多卷。",
            "",
            "**请打开：[分卷索引](gms-server-symbol-notes-README.md)**，再选择对应模块。",
            "",
            "> 重新生成：`python3 scripts/generate-symbol-notes.py`",
            "",
        ]
    )
    (out_dir / "gms-server-symbol-notes.md").write_text(stub, encoding="utf-8")


TS_FN_RE = re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(", re.M)
TS_ARROW_RE = re.compile(r"^\s*(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>", re.M)
TS_EXPORT_RE = re.compile(r"^\s*export\s+(?:default\s+)?(?:const|function|class|interface|type|enum)\s+(\w+)", re.M)


def extract_vue_script(content: str) -> str:
    blocks = re.findall(r"<script[^>]*>(.*?)</script>", content, re.S | re.I)
    return "\n\n".join(blocks)


def gen_ui_notes(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_SERVER_REPO",
        [workspace / "BeiDou-Server", Path("/tmp/BeiDou-Server")],
        Path("gms-ui/src"),
    )
    if not repo:
        raise SystemExit("未找到 gms-ui。")
    src = repo / "gms-ui" / "src"
    files = sorted(list(src.rglob("*.ts")) + list(src.rglob("*.vue")))
    out = [
        "# gms-ui 逐符号中文职责索引",
        "",
        "> 自动生成：`scripts/generate-symbol-notes.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> 文件数：{len(files)}",
        "",
    ]
    for fp in files:
        txt = read_text(fp)
        if fp.suffix == ".vue":
            txt = extract_vue_script(txt)
        rel = fp.relative_to(src)
        out.append(f"## `{rel}`")
        for n in TS_EXPORT_RE.findall(txt):
            out.append(f"- `export {n}`：对外导出给其它模块/页面复用。")
        for n in TS_FN_RE.findall(txt):
            out.append(f"- `function {n}(...)`：{zh_for_symbol(n)}")
        for n in TS_ARROW_RE.findall(txt):
            out.append(f"- `const {n} = (...) =>`：{zh_for_symbol(n)}")
        out.append("")
    (out_dir / "gms-ui-symbol-notes.md").write_text("\n".join(out), encoding="utf-8")


CPP_CLASS_RE = re.compile(r"^\s*class\s+(\w+)", re.M)
CPP_METHOD_RE = re.compile(r"^\s*(?:[\w:<>,~*&\s]+)\s+(\w+)::(\w+)\s*\(", re.M)
CPP_DECL_RE = re.compile(
    r"^\s*(?:extern\s+\"C\"\s+)?"
    r"(?:(?:static|inline|constexpr|virtual)\s+)*"
    r"(?:__declspec\([^)]+\)\s*)*"
    r"(?:[\w:<>,~*&]+\s+)+"
    r"(?P<name>\w+)\s*\([^;{}]*\)\s*(?:;|\{)\s*$"
)
CPP_SKIP = {"if", "for", "while", "switch", "catch", "return", "sizeof"}
CPP_BLACKLIST = {
    "void",
    "int",
    "char",
    "short",
    "long",
    "float",
    "double",
    "bool",
    "auto",
    "class",
    "struct",
    "enum",
}


def gen_ijl15_notes(workspace: Path, out_dir: Path) -> None:
    repo = find_repo(
        "BEIDOU_IJL15_REPO",
        [workspace / "BeiDou-ijl15", Path("/tmp/BeiDou-ijl15")],
        Path("ezorsia"),
    )
    if not repo:
        raise SystemExit("未找到 BeiDou-ijl15。")
    src = repo / "ezorsia"
    files = sorted(list(src.rglob("*.h")) + list(src.rglob("*.hpp")) + list(src.rglob("*.cpp")) + list(src.rglob("*.c")))
    out = [
        "# BeiDou-ijl15 逐符号中文职责索引",
        "",
        "> 自动生成：`scripts/generate-symbol-notes.py`",
        f"> 源码路径：`{rel_display(repo, workspace)}`",
        f"> 文件数：{len(files)}",
        "",
    ]
    for fp in files:
        rel = fp.relative_to(src)
        text = read_text(fp)
        out.append(f"## `{rel}`")
        for c in CPP_CLASS_RE.findall(text):
            out.append(f"- `class {c}`：{zh_for_class(c)}")
        seen: set[str] = set()
        for c, m in CPP_METHOD_RE.findall(text):
            if m in CPP_SKIP:
                continue
            k = f"{c}::{m}"
            if k in seen:
                continue
            seen.add(k)
            out.append(f"- `{c}::{m}(...)`：{zh_for_symbol(m)}")
        for raw in text.splitlines():
            s = raw.strip()
            if not s or s.startswith("//") or s.startswith("/*") or s.startswith("*"):
                continue
            if "::" in s:
                continue
            m = CPP_DECL_RE.match(s)
            if not m:
                continue
            fn = m.group("name")
            if fn in CPP_SKIP:
                continue
            if fn in CPP_BLACKLIST:
                continue
            if f"::{fn}" in "".join(seen):
                continue
            out.append(f"- `{fn}(...)`：{zh_for_symbol(fn)}")
        out.append("")
    (out_dir / "beidou-ijl15-symbol-notes.md").write_text("\n".join(out), encoding="utf-8")


def update_overview(workspace: Path) -> None:
    p = workspace / "docs" / "11-全量源码符号文档说明.md"
    content = read_text(p)
    addon = """

## 逐符号中文职责版（新增）

- `docs/reference/gms-server-symbol-notes.md`
- `docs/reference/gms-ui-symbol-notes.md`
- `docs/reference/beidou-ijl15-symbol-notes.md`

上述文档在“符号列表”基础上，为每个类/函数补一条中文职责摘要，便于快速理解。
"""
    if "逐符号中文职责版（新增）" not in content:
        p.write_text(content.rstrip() + addon + "\n", encoding="utf-8")


def main() -> None:
    workspace = Path(__file__).resolve().parent.parent
    out = workspace / "docs" / "reference"
    out.mkdir(parents=True, exist_ok=True)
    gen_server_notes(workspace, out)
    gen_ui_notes(workspace, out)
    gen_ijl15_notes(workspace, out)
    update_overview(workspace)
    print("已生成逐符号中文职责文档。")


if __name__ == "__main__":
    main()
