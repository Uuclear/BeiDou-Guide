# BeiDou 开发文档

本站由 [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 生成，用于在 **GitHub Pages** 上集中阅读本仓库全部 Markdown 文档（含自动生成的源码索引）。

---

## 快速导航

| 分类 | 说明 |
|------|------|
| **环境与架构** | 环境搭建、架构、API、数据库、配置、运维、用户手册、技术规范 |
| **源码与索引** | 深度导读、ijl15 详解、全量符号说明与脚本用法 |
| **源码模块精读（人机）** | [12-源码模块精读-人机撰写.md](12-源码模块精读-人机撰写.md)：按阅读源码写的模块说明，**不是**脚本批量释义 |
| **gms-server 逐符号职责** | 脚本按命名生成的附注，**仅作检索辅助**；计数为 0 的条目无含义 |
| **全量符号与 API 索引** | 大体积自动生成文档，适合搜索定位 |

左上角 **搜索框** 可全文检索整站内容。

---

## 与 GitHub 仓库的关系

- 文档与脚本以仓库 [`BeiDou-Guide`](https://github.com/Uuclear/BeiDou-Guide) 为准。
- 重新生成本地索引请参考仓库根目录 **README**（与 `mkdocs.yml` 中 `repo_url` 指向的仓库一致）中的脚本说明。

---

## 离线阅读

克隆仓库后执行：

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

浏览器打开提示的本地地址即可。
