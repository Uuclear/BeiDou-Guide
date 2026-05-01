# BeiDou-Guide

BeiDou 游戏系统完整开发文档套件。

## 项目概述

本项目为 BeiDou 游戏系统的纯文档项目，记录了客户端和服务端的完整开发文档，涵盖环境搭建、架构设计、API接口、数据库设计、配置说明、运维部署、用户手册和技术规范等各个方面。

## 在线文档（GitHub Pages）

推送 `main` 后，由 [`.github/workflows/docs-pages.yml`](.github/workflows/docs-pages.yml) 自动构建并发布到 **`gh-pages`** 分支。

1. 在 GitHub 打开仓库 **Settings → Pages**
2. **Build and deployment** 选 **Deploy from a branch**
3. **Branch** 选 **`gh-pages`** / **`/ (root)`**

默认站点地址为：`https://uuclear.github.io/BeiDou-Guide/`（若仓库所有者或仓库名不同，请修改根目录 `mkdocs.yml` 中的 `site_url` 后重新部署。）

本地预览：

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## 文档目录

| 文档 | 描述 |
|------|------|
| [01-环境搭建指南](docs/01-环境搭建指南.md) | 服务端、前端、客户端DLL开发环境配置 |
| [02-架构设计文档](docs/02-架构设计文档.md) | 系统架构、技术栈、模块关系说明 |
| [03-API接口文档](docs/03-API接口文档.md) | REST API 详细说明，Swagger访问地址 |
| [04-数据库设计文档](docs/04-数据库设计文档.md) | 数据库表结构、Flyway迁移脚本说明 |
| [05-配置说明文档](docs/05-配置说明文档.md) | 服务端 application.yml 和客户端 config.ini 详细配置 |
| [06-运维部署文档](docs/06-运维部署文档.md) | 生产环境部署、安全配置、Docker部署参考 |
| [07-用户使用手册](docs/07-用户使用手册.md) | 玩家客户端使用和管理员后台操作指南 |
| [08-技术规范文档](docs/08-技术规范文档.md) | API版本控制、数据库命名、代码提交规范 |
| [09-源码深度导读](docs/09-源码深度导读.md) | gms-server / gms-ui 源码阅读路径、包职责说明 |
| [10-BeiDou-ijl15-源码详解](docs/10-BeiDou-ijl15-源码详解.md) | 客户端 DLL（ezorsia）按文件的类与函数说明 |
| [11-全量源码符号文档说明](docs/11-全量源码符号文档说明.md) | “我就要全部”场景：全量符号索引入口与生成方式 |
| [12-源码模块精读（人机撰写）](docs/12-源码模块精读-人机撰写.md) | 按阅读源码写的模块/关键入口说明（非脚本批量释义） |

### 源码索引（需本地克隆 BeiDou-Server 后生成）

从本仓库运行 `python3 scripts/generate-gms-server-api-index.py` 可生成 **gms-server 全量 public 类型与方法签名** 索引：[docs/reference/gms-server-api-index.md](docs/reference/gms-server-api-index.md)（默认约 1.2 万行，适合检索而非通读）。

若你需要“全部（含非 public）”，运行 `python3 scripts/generate-full-symbol-docs.py` 生成：

- [docs/reference/gms-server-full-symbols.md](docs/reference/gms-server-full-symbols.md)
- [docs/reference/gms-ui-full-symbols.md](docs/reference/gms-ui-full-symbols.md)
- [docs/reference/beidou-ijl15-full-symbols.md](docs/reference/beidou-ijl15-full-symbols.md)

若你需要「清单式」逐符号附注（**按命名启发式生成，不是读代码写出的设计说明**），运行 `python3 scripts/generate-symbol-notes.py`：

- **gms-server（按 `org/gms` 一级目录分卷）**：[分卷索引](docs/reference/gms-server-symbol-notes-README.md) · [各卷目录](docs/reference/gms-server-symbol-notes/)
- [docs/reference/gms-ui-symbol-notes.md](docs/reference/gms-ui-symbol-notes.md)
- [docs/reference/beidou-ijl15-symbol-notes.md](docs/reference/beidou-ijl15-symbol-notes.md)

**按理解撰写的模块说明**请以 [12-源码模块精读（人机撰写）](docs/12-源码模块精读-人机撰写.md) 为准；该文档会随指定模块逐步扩写。

## 项目结构

```
BeiDou-Guide/
├── README.md                    # 项目概述与导航
├── docs/
│   ├── 01-环境搭建指南.md       # 开发环境配置
│   ├── 02-架构设计文档.md       # 系统架构说明
│   ├── 03-API接口文档.md        # REST API 详细说明
│   ├── 04-数据库设计文档.md     # 数据库结构与迁移
│   ├── 05-配置说明文档.md       # 配置文件详解
│   ├── 06-运维部署文档.md       # 生产环境部署
│   ├── 07-用户使用手册.md       # 玩家/管理员使用指南
│   ├── 08-技术规范文档.md       # 开发规范与最佳实践
│   ├── 09-源码深度导读.md       # 服务端/前端源码阅读指南
│   ├── 10-BeiDou-ijl15-源码详解.md  # 客户端 DLL 逐文件说明
│   ├── 11-全量源码符号文档说明.md   # 全量索引入口与生成说明
│   ├── 12-源码模块精读-人机撰写.md # 按阅读源码写的模块说明（非脚本释义）
│   ├── reference/               # 自动生成的 gms-server API 索引等
│   └── images/                  # 文档配图目录
```

## 相关项目

- **BeiDou-ijl15**: 客户端DLL项目，基于 Ezorsia 开发，提供中文输入修复、属性上限突破等功能
- **BeiDou-Server**: 服务端项目，包含 gms-server (Java Spring Boot) 和 gms-ui (Vue 3 Web管理界面)
- **BeiDou-docker**: Docker 部署配置独立仓库

## 快速开始

### 服务端环境

1. 安装 OpenJDK 21
2. 安装 MySQL 8 数据库
3. 使用 IntelliJ IDEA 导入 gms-server 项目
4. 运行 Maven 构建

### 前端环境

1. 安装 Node.js v20.15.0
2. 安装 Yarn: `npm install -g yarn`
3. 进入 gms-ui 目录执行: `yarn install`
4. 启动开发服务器: `yarn dev`

### 客户端DLL环境

1. 安装 Visual Studio 2019
2. 配置 Windows SDK 10 和工具集 VS2019 (v142)
3. 使用 Release x86 模式生成解决方案
4. 输出文件位于 `out/Release/ijl15.dll`

详细步骤请参考 [环境搭建指南](docs/01-环境搭建指南.md)。

## 版本信息

| 组件 | 版本 |
|------|------|
| gms-server | Java 21, Spring Boot 3.2.3 |
| gms-ui | Vue 3, Node.js 20.15.0 |
| ijl15.dll | VS2019 (v142), Windows SDK 10 |
| MySQL | 8.x |

## 许可证

本文档项目遵循 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来完善文档内容。