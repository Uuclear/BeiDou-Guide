# BeiDou-ijl15 源码详解

本文档对应上游仓库 [BeiDouMS/BeiDou-ijl15](https://github.com/BeiDouMS/BeiDou-ijl15) 中 `ezorsia/` 目录下的主要源文件。ijl15 工程体量小（数十个 C/C++ 单元），适合在文档中**按文件**说明职责；地址偏移（如 `0x004CA061`）与客户端版本强相关，升级客户端后必须重新校验。

---

## 总览：DLL 在何时做了什么

1. **进程加载 DLL**（`DllMain` → `DLL_PROCESS_ATTACH`）  
2. 读取同目录 **`config.ini`**（`INIReader`），填充 `Client::` 静态配置（分辨率、端口、伤害上限、IME 等）。  
3. 将 **主机名解析为 IPv4 字符串**（`ResolveToIpv4String`），供后续补丁写入连接信息时使用。  
4. 按固定顺序安装 **Detours 钩子**（`ReplacementFuncs.h` 中大量 `Hook*`）：多开、窗口、资源加载路径、字符串池等。  
5. 调用 `Client::UpdateGameStartup()` 及一系列 `Client::` 补丁方法，应用分辨率、中文、数值上限等逻辑。  
6. `BossHP::Hook()` 钩住与 Boss 血条 UI 相关的客户端例程。  
7. **`ijl15::CreateHook()`**：从 **`2ijl15.dll`** 取真实 JPEG 库导出并 **转发**（见下文），使本 DLL 可顶替游戏加载的 `ijl15.dll` 名称而不破坏图像解码。  
8. `DLL_PROCESS_DETACH` 中当前实现为 **`ExitProcess(0)`**（会终结进程；若需热卸载需自行调整）。

> 说明：`dllmain.cpp` 内注释仍写「NMCO hook」，但实际加载的是 `ijl15::CreateHook()`。**NMCO** 相关转发实现在 `NMCO.cpp`，依赖 **`nmconew2.dll`**，与 **ijl15 转发** 是两套可选机制，是否启用取决于你的打包与引导方式。

---

## 入口与配置

### `dllmain.cpp`

| 符号 | 作用 |
|------|------|
| `ResolveToIpv4String` | 若 `config.ini` 里是域名，用 WinSock `getaddrinfo` 解析为 IPv4 点分字符串；解析失败则退回原文本。 |
| `CreateConsole` | 分配控制台（开发调试用，默认注释）。 |
| `DllMain` | 读配置、安装钩子、调用 `Client` / `BossHP` / `ijl15` 初始化；`DLL_PROCESS_DETACH` 调 `ExitProcess(0)`。 |

### `dllmain.h`

通常为空或仅声明；以仓库实际内容为准。

### `INIReader.h` / `INIReader` 实现段

基于 **inih** 的 INI 解析（参见文件头许可证说明）。`dllmain` 使用 `INIReader reader("config.ini")`，各 section（如 `general`、`optional`、`debug`）键值映射到 `Client::` 静态成员。

---

## 名称劫持：`ijl15` 与 `NMCO`

### `ijl15.h` / `ijl15.cpp` —— 类 `ijl15`

| 成员 | 说明 |
|------|------|
| `CreateHook()` | `LoadLibraryA("2ijl15.dll")`，`GetProcAddress` 取得 `ijlErrorStr`、`ijlFree`、`ijlGetLibVersion`、`ijlInit`、`ijlRead`、`ijlWrite` 地址。 |
| 导出函数 `ijlGetLibVersion` 等 | `extern "C"` + `naked`，内联汇编 `jmp` 到真实实现（**x86**）。 |

设计意图：游戏进程仍按名称加载 **ijl15.dll**，本模块导出同名入口，把调用转发到真正的 **`2ijl15.dll`**（需与游戏一并分发）。

### `NMCO.h` / `NMCO.cpp` —— 类 `NMCO`

| 成员 | 说明 |
|------|------|
| `CreateHook()` | `LoadLibraryA("nmconew2.dll")`，解析 `NMCO_CallNMFunc`、`NMCO_CallNMFunc2`、`NMCO_MemoryFree`。 |
| 导出 `NMCO_*` | 同样为 `naked` + `jmp` 转发。 |

用于 Nexon/登录组件一类 DLL 的导出兼容（具体取决于你的客户端补丁策略）。

---

## 内存与钩子基础设施

### `Memory.h` / `Memory.cpp` —— 类 `Memory`

| 方法 | 说明 |
|------|------|
| `UseVirtuProtect` | 静态开关：是否在改写内存前使用 `VirtualProtect`（默认可通过 `config.ini` 的 `UseVirtuProtect` 控制）。 |
| `SetHook` | 封装 Detours：`DetourTransactionBegin` → `DetourAttach`/`Detach` → `Commit`。 |
| `FillBytes` | 按字节填充指定地址区域。 |
| `ReplaceString` / `WriteString` | 在客户端内存中改写字符串；注释中强调 **新串长度 ≤ 原串** 等约束。 |
| `WriteByte` / `WriteShort` / `WriteInt` / `WriteDouble` | 写入标量。 |
| `WriteByteArray` | 写入字节数组补丁。 |
| `CodeCave` | 在指定地址写入跳转/补丁（与 `codecaves` 配合）。 |
| `PatchNop` | 用 NOP（`0x90`）填充指定长度，可选 `VirtualProtect`。 |

---

## 客户端逻辑补丁：类 `Client`

### `Client.h` / `Client.cpp`

**静态配置成员**（节选，完整以头文件为准）：分辨率 `m_nGameWidth`/`m_nGameHeight`、`MsgAmount`、窗口与 Logo 选项、`setDamageCap` 等数值上限、`ServerIP_AddressFromINI`、`serverIP_Port`、IME 与调试开关等。

**静态方法**（职责摘要）：

| 方法 | 职责摘要 |
|------|----------|
| `UpdateGameStartup` | 大量 **可选** 的 `Memory::CodeCave` / `WriteByte` 补丁（多数以注释形式保留），用于版本特定的启动与网络绕过；按客户端构建切换。 |
| `EnableNewIGCipher` | 与 `m_nIGCipherHash` 相关的密码学/包处理补丁。 |
| `UpdateResolution` | 按配置分辨率改写客户端渲染/窗口相关常量与调用。 |
| `UpdateLogin` | 登录流程相关内存补丁（与 `AddyLocations` 地址绑定）。 |
| `FixMouseWheel` | 鼠标滚轮行为修正。 |
| `Chinese` | 中文显示/编码相关补丁。 |
| `LongQuickSlot` | 快捷栏扩展相关。 |
| `FixDateFormat` | 日期格式。 |
| `FixItemType` | 物品类型显示或判定。 |
| `JumpCap` | 跳跃上限相关。 |
| `FixChatPosHook` | 聊天窗口位置。 |
| `NoPassword` | 配合调试的无密码逻辑（受 `noPassword` 等标志控制）。 |
| `MoreHook` | 其它杂项钩子集合。 |
| `WorldMap` | 世界地图相关 UI 或数据补丁。 |

具体汇编级行为需对照 **`AddyLocations.h`**、**`codecaves.h`** 中地址与 `Client.cpp` 实现。

---

## 函数替换与 Win32 / Wz 钩子：`ReplacementFuncs.h`

该头文件体积大，主要包含：

- `HookGetModuleFileName`、`HookCreateWindowExA`、`Hook_CreateMutexA` 等 **Win32 API** 级别的 Detour（多开、窗口居中、最小化按钮等）。  
- `HookPcCreateObject_IWzResMan` 等与 **Wz 资源系统** 相关的钩子，用于路径、挂载与加载行为修正。  
- 大量内联 **lambda** 作为 Detour 目标，调用 `Memory::SetHook`。

阅读方式：搜索 `bool Hook` 或 `Hook` 前缀函数名，从 `DllMain` 里实际启用的一组开始跟踪。

---

## 地址与代码洞

### `AddyLocations.h`

客户端 **VA（虚拟地址）** 常量，供 `Memory::Write*`、`CodeCave` 使用。版本变化时此处最先失效。

### `codecaves.h`

预定义的 **code cave** 机器码块与目标地址、NOP 计数等，与 `Memory::CodeCave` 配合。

---

## 输入法与好友：`FixIme` / `FixBuddy`

### `FixIme.h`

- `EnableIme` / `DisableIme`：通过 `ImmGetContext` / `ImmAssociateContext` 调整 IME（注释标明部分方法未充分测试）。  
- 若干 **`__declspec(naked)`** 与全局 **`DWORD` 返回地址**：在内联汇编里跳转到客户端原有 IME 分支，修复中文输入路径；地址与客户端构建绑定。

### `FixBuddy.h`

好友列表/社交相关补丁声明（具体以文件内容为准）。

---

## Boss 血条 UI：`BossHP.h` / `BossHP.cpp`

| 成员 | 说明 |
|------|------|
| `Hook` | 对外入口，内部调用 `HookInternal` 等安装一系列与怪物 HP 标签、字段初始化/销毁相关的钩子。 |
| `DrawBossHpNumberIfNeed` 等 | 在适当时机绘制自定义 Boss HP 数值或覆盖默认显示。 |
| `GetMiniMapWidth` | 布局计算辅助。 |

---

## HP/MP 预警：`HpMpAlert.h` / `HpMpAlert.cpp`

声明 `HookSaveGlobal`、`HookHpMpAlertRecv`：与全局状态保存及 HP/MP 包处理挂钩，实现低血量提示等（细节见 `.cpp`）。

---

## 客户端集合类型模板：`MapleClientCollectionTypes/*`

`ZArray`、`ZList`、`ZXString`、`ZRef` 等模板/工具类，多为 **从客户端逆向风格** 迁移的容器与字符串封装，供补丁代码安全访问游戏内结构；阅读时关注 **`ZXString`**、**`ZArray`** 等与游戏内类型布局一致性。

---

## 其它头文件

| 文件 | 作用 |
|------|------|
| `stdafx.h` / `stdafx.cpp` | 预编译头与通用 Windows / CRT 包含。 |
| `AutoTypes.h` | 自动类型/typedef 聚合，服务钩子签名。 |
| `resource.h` | 资源 ID。 |
| `detours.h` / `detver.h` | Microsoft Detours 库头文件。 |
| `syelog.h`、`targetver.h` | 日志与目标平台版本（按项目配置）。 |

---

## 阅读顺序建议

1. `dllmain.cpp` → 弄清配置键与钩子启用顺序。  
2. `Memory.cpp` → 理解所有补丁的底层能力边界。  
3. `ijl15.cpp` / `NMCO.cpp` → 理解 DLL 名称劫持模式。  
4. `Client.cpp` 中**未被注释**的活跃补丁 → 当前版本实际生效逻辑。  
5. `ReplacementFuncs.h` 中与 `DllMain` 调用名一致的 `Hook*` → Win32 与 Wz 层行为。  
6. `FixIme.h`、`BossHP`、`HpMpAlert` → 专项功能。

修改补丁时务必在 **与目标客户端完全一致** 的二进制上验证地址与调用约定（**stdcall/cdecl/thiscall** 等）。
