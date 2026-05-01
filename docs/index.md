# BeiDou 开发文档

本站由 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 生成，用于在 **GitHub Pages** 上集中阅读本仓库全部 Markdown 文档（含自动生成的源码索引）。

!!! note "第一次来？"

    请先打开 **[阅读指引：文档分层与推荐路径](read-guide.md)**：里面说明了 **精读 vs 自动生成索引** 的差别，以及推荐阅读顺序，避免在大段符号表里迷路。

---

## 快速导航

| 分类 | 说明 |
|------|------|
| **[阅读指引](read-guide.md)** | 文档分层、推荐路径、站内检索技巧 |
| **环境与架构** | 环境搭建、架构、API、数据库、配置、运维、用户手册、技术规范 |
| **源码精读与导读** | 深度导读、ijl15 详解、`11` 生成说明、**`12` 人机精读（优先）** |
| **自动生成索引** | gms-server 分卷职责、全量符号与 API — **适合检索，不等于设计说明** |

左上角 **搜索框** 可全文检索整站内容；长文可使用右侧 **目录** 跟随滚动。

---

## 与 GitHub 仓库的关系

- 文档与脚本以仓库 [`BeiDou-Guide`](https://github.com/Uuclear/BeiDou-Guide) 为准。
- 页面右上角 **编辑** 链到 GitHub 上对应 Markdown（若仓库权限允许）。
- 重新生成本地索引请参考仓库根目录 **README** 中的脚本说明。

---

## 离线阅读

克隆仓库后执行：

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

浏览器打开提示的本地地址即可。
