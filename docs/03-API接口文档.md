# API接口文档

本文档详细介绍 BeiDou 服务端 REST API 的接口规范、认证机制和使用方法。

---

## 目录

1. [API概述](#api概述)
2. [认证机制](#认证机制)
3. [版本控制](#版本控制)
4. [接口分类](#接口分类)
5. [通用规范](#通用规范)
6. [Swagger文档](#swagger文档)
7. [常见接口示例](#常见接口示例)
8. [错误处理](#错误处理)

---

## API概述

BeiDou 服务端提供 REST API 供 Web 管理界面调用，实现用户管理、角色管理、服务器监控等功能。

### 基本信息

| 项目 | 值 |
|------|------|
| 基础URL | `http://localhost:8686` |
| 协议 | HTTP/HTTPS |
| 数据格式 | JSON |
| 认证方式 | JWT Token |
| 文档地址 | `http://localhost:8686/swagger-ui/index.html` |

### 服务端配置

API 服务配置位于 `application.yml`：

```yaml
server:
  port: 8686

jwt:
  secret: "50da066e-6080-40f5-a173-86bd27d4f674"
  duration: 1800000  # 30分钟

springdoc:
  api-docs:
    enabled: true
  swagger-ui:
    enabled: true
```

---

## 认证机制

### JWT Token 认证

所有需要认证的接口都需要在请求头携带 JWT Token。

**获取Token：**

```http
POST /v1/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin"
}
```

**响应示例：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expireTime": 1800000
  }
}
```

**使用Token：**

在后续请求中添加 Authorization 头：

```http
GET /v1/characters
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Token 配置

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| jwt.secret | UUID字符串 | Token签名密钥，生产环境必须修改 |
| jwt.duration | 1800000ms | Token有效期，默认30分钟 |

### 安全注意事项

生产环境必须：
1. 修改 `jwt.secret` 为自定义 UUID
2. 使用 HTTPS 协议
3. 定期更换密钥

---

## 版本控制

### 版本机制

API 采用版本控制，通过 URL 路径区分版本：

- `/v1/xxx` - 版本1接口
- `/v2/xxx` - 版本2接口
- `/v3/xxx` - 版本3接口

### 版本常量定义

```java
public class ApiConstant {
    public static final String V1 = "v1";
    public static final String V2 = "v2";
    public static final String V3 = "v3";
    public static final String LATEST = "v3";  // 当前最新版本
}
```

### 版本更新策略

| 场景 | 处理方式 |
|------|----------|
| 新增接口 | 使用 LATEST 版本 |
| 接口不兼容更新 | 旧接口改为指定版本 Tag，新接口使用新版本 |
| 接口小改动兼容 | 直接更新 LATEST 版本接口 |

### 默认配置

默认的 Swagger 标签为 `ApiConstant.LATEST`，默认的 RequestMapping 格式：

```java
@RequestMapping("/" + ApiConstant.LATEST + "/xx")
@Tag(name = ApiConstant.LATEST)
```

---

## 接口分类

### 1. 认证接口 (Auth)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 登录 | POST | `/v1/auth/login` | 用户登录获取Token |
| 登出 | POST | `/v1/auth/logout` | 用户登出 |

### 2. 用户管理接口 (Account)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 用户列表 | GET | `/v1/accounts` | 查询用户列表 |
| 用户详情 | GET | `/v1/accounts/{id}` | 查询用户详情 |
| 创建用户 | POST | `/v1/accounts` | 创建新用户 |
| 更新用户 | PUT | `/v1/accounts/{id}` | 更新用户信息 |
| 删除用户 | DELETE | `/v1/accounts/{id}` | 删除用户 |
| 封禁用户 | POST | `/v1/accounts/{id}/ban` | 封禁指定用户 |
| 解封用户 | POST | `/v1/accounts/{id}/unban` | 解封指定用户 |

### 3. 角色管理接口 (Character)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 角色列表 | GET | `/v1/characters` | 查询角色列表 |
| 角色详情 | GET | `/v1/characters/{id}` | 查询角色详情 |
| 更新角色 | PUT | `/v1/characters/{id}` | 更新角色信息 |
| 删除角色 | DELETE | `/v1/characters/{id}` | 删除角色 |
| 角色装备 | GET | `/v1/characters/{id}/equipment` | 查询角色装备 |
| 角色物品 | GET | `/v1/characters/{id}/inventory` | 查询角色背包 |

### 4. 商店接口 (Shop)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 商店列表 | GET | `/v1/shops` | 查询商店列表 |
| 商店物品 | GET | `/v1/shops/{id}/items` | 查询商店物品 |

### 5. 物品接口 (Item)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 物品列表 | GET | `/v1/items` | 查询物品列表 |
| 物品详情 | GET | `/v1/items/{id}` | 查询物品详情 |

### 6. 服务器状态接口 (Server)

| 接口 | 方法 | 路径 | 描述 |
|------|------|------|------|
| 服务器状态 | GET | `/v1/server/status` | 查询服务器运行状态 |
| 在线玩家 | GET | `/v1/server/online` | 查询在线玩家列表 |
| 服务器配置 | GET | `/v1/server/config` | 查询服务器配置 |

---

## 通用规范

### 请求格式

**Content-Type:**

```http
Content-Type: application/json
```

**请求示例：**

```json
{
  "username": "test",
  "password": "123456",
  "email": "test@example.com"
}
```

### 响应格式

**标准响应结构：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    // 业务数据
  }
}
```

**错误响应：**

```json
{
  "code": 400,
  "message": "参数错误",
  "data": null
}
```

### 状态码定义

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未认证/Token失效 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

### 分页参数

列表查询支持分页：

```http
GET /v1/characters?page=1&size=20
```

**分页响应：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "list": [...],
    "total": 100,
    "page": 1,
    "size": 20
  }
}
```

---

## Swagger文档

### 访问地址

启动服务端后访问：

```
http://localhost:8686/swagger-ui/index.html
```

### Swagger配置

```yaml
springdoc:
  api-docs:
    enabled: true   # 是否开启OpenApi
  swagger-ui:
    enabled: true   # 是否开启SwaggerUI
```

**生产环境配置：**

```yaml
springdoc:
  api-docs:
    enabled: false
  swagger-ui:
    enabled: false
```

### Swagger标注

控制器示例：

```java
@RestController
@RequestMapping("/" + ApiConstant.LATEST + "/characters")
@Tag(name = ApiConstant.LATEST, description = "角色管理接口")
public class CharacterController {
    
    @Operation(summary = "查询角色列表")
    @GetMapping
    public Result list(@RequestParam int page, @RequestParam int size) {
        // ...
    }
}
```

---

## 常见接口示例

### 1. 用户登录

**请求：**

```http
POST /v1/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin"
}
```

**响应：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expireTime": 1800000,
    "user": {
      "id": 1,
      "name": "admin",
      "role": "admin"
    }
  }
}
```

### 2. 查询角色列表

**请求：**

```http
GET /v1/characters?page=1&size=10
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**响应：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "list": [
      {
        "id": 1,
        "name": "角色A",
        "level": 100,
        "job": 422,
        "accountId": 1
      },
      {
        "id": 2,
        "name": "角色B",
        "level": 50,
        "job": 310,
        "accountId": 2
      }
    ],
    "total": 100,
    "page": 1,
    "size": 10
  }
}
```

### 3. 封禁用户

**请求：**

```http
POST /v1/accounts/1/ban
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "reason": "违规操作",
  "duration": 7  // 封禁天数，-1表示永久
}
```

**响应：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "accountId": 1,
    "banned": true,
    "reason": "违规操作",
    "expireTime": "2026-05-07T00:00:00"
  }
}
```

### 4. 查询服务器状态

**请求：**

```http
GET /v1/server/status
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**响应：**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "running": true,
    "onlineCount": 50,
    "maxOnline": 1000,
    "uptime": 3600000,
    "version": "1.8.5"
  }
}
```

---

## 错误处理

### 错误码定义

| 错误码 | 描述 | 处理建议 |
|--------|------|----------|
| 40001 | 参数缺失 | 检查必填参数 |
| 40002 | 参数格式错误 | 检查参数类型 |
| 40101 | Token缺失 | 添加Authorization头 |
| 40102 | Token过期 | 重新登录获取新Token |
| 40301 | 权限不足 | 检查用户权限 |
| 40401 | 用户不存在 | 检查用户ID |
| 40402 | 角色不存在 | 检查角色ID |
| 50001 | 数据库错误 | 检查数据库连接 |

### 错误响应示例

**Token过期：**

```json
{
  "code": 40102,
  "message": "Token已过期，请重新登录",
  "data": null
}
```

**权限不足：**

```json
{
  "code": 40301,
  "message": "无权限执行此操作",
  "data": null
}
```

### 前端错误处理

建议在前端统一处理：

```typescript
// axios 拦截器示例
axios.interceptors.response.use(
  response => {
    if (response.data.code !== 200) {
      // 显示错误提示
      Message.error(response.data.message);
      return Promise.reject(response.data);
    }
    return response.data;
  },
  error => {
    if (error.response?.status === 401) {
      // Token失效，跳转登录
      router.push('/login');
    }
    return Promise.reject(error);
  }
);
```

---

## 限流配置

服务端支持API限流保护：

```yaml
gms:
  service:
    rate-limit:
      enabled: false      # 是否开启限流
      limit: 10           # 每IP最大请求数
      duration: 1000      # 重置时间(ms)
      auto-ban: false     # 是否自动封禁
```

开启后，同一IP在 `duration` 时间内请求超过 `limit` 次会被限制。

---

## 下一步

- [数据库设计文档](04-数据库设计文档.md) - 数据表结构
- [配置说明文档](05-配置说明文档.md) - 服务端配置详情
- [运维部署文档](06-运维部署文档.md) - 生产环境部署