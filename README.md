# BeiDou-Guide

BeiDou 游戏系统完整开发文档套件。

## 项目概述

本项目为 BeiDou 游戏系统的纯文档项目，记录了客户端和服务端的完整开发文档，涵盖环境搭建、架构设计、API接口、数据库设计、配置说明、运维部署、用户手册和技术规范等各个方面。

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