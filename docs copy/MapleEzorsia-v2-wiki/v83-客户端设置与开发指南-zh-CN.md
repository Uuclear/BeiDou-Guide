# v83 客户端设置与 DLL 客户端开发指南（适用于现代高清显示器）

**目录**

- [核心设置](#核心设置)
- [终端用户安全](#终端用户安全)
- [故障排除](#故障排除)
- [服务器相关事项](#服务器相关事项)
- [开发前的说明](#开发前的说明)
- [DLL客户端开发所需工具](#dll客户端开发所需工具)
- [DLL客户端开发流程](#dll客户端开发流程)
- [DLL客户端开发教程](#dll客户端开发教程)
- [实用资源](#实用资源)

---

## 核心设置

本设置指南是为开源 v83 DLL 客户端设计的，该客户端旨在与最完善的开源 v83 服务器（目前是 Cosmic）配合使用。

本指南假设你已经按照各自 v83 服务器源码的服务器设置指南操作到了安装游戏的步骤。不要使用提供的 localhost，也不要删除默认安装中的任何内容，请下载以下内容：

- 从 [releases](https://github.com/444Ro666/MapleEzorsia-v2/releases) 下载编译好的 Ezorsia V2 DLL；按照 [readme 中的说明](https://github.com/444Ro666/MapleEzorsia-v2#default-configini) 安装（源码也已发布，用于透明度和开发）
- [已移除管理员权限请求并启用 4G 标志的默认 v83 客户端](https://mega.nz/file/9uNmHIAZ#zzE7t7T6wQyDbJrHJxgw-AOlmzzwCpLrOKmoUlec_5E) 这是直接对二进制文件进行的仅两项修改，因为我无法通过 DLL 实现
  - 4G 标志激活 PE 头中的"大地址空间感知"（LAA）标志。这将允许客户端使用最多 4GB 内存，而不仅仅是 2GB。
    - 如果你想自己进行修改以验证，需要安装时附带的客户端（如果删除了请重新安装，或直接使用这里提供的），还需要使用 Cosmic 文件中的十六进制编辑器 [这里](https://drive.google.com/drive/folders/1hgnb92MGL6xqEp9szEMBh0K9pSJcJ6IT)，并进行以下修改：
      - [如图所示](https://www.mediafire.com/view/2jdmfszadkzpn49/2023-09-12-100911_1295x227_scrot.png/file#)（只做第一个"asInvoker"部分，我的 DLL 会处理其余部分，因为你无法在打包客户端中编辑这些实际偏移量）
        - 编辑管理员部分后，可能需要将可执行文件重命名为"MapleStory2"或其他名称，有报告称如果使用默认名称可能无法真正移除权限提升
      - 以及 [如图所示](https://mega.nz/file/5jdjiTTJ#0WA-FczBGEGyrnVWET49Rh6IvDM4DWuIcyGdl7HkQ2g) 注意对于 PE 头中的 4G 标志，默认值是"0f"，需要改为"2f"。地址是 0000013E
- 为了最佳体验，我推荐 1280x720 分辨率，并配合后面提供的无边框全屏工具。这是我开发和游戏时使用的分辨率
- 从 https://github.com/Blinue/Magpie 下载 Magpie；游戏运行时打开 Magpie，点击新建配置文件并选择你的客户端窗口，然后进入创建的配置文件并启用"前台时自动缩放"。确保 Ezorsia 配置中窗口模式已开启。
  - Magpie 是一个无边框全屏工具，通过与 DirectX 交互将像素重新绘制为高分辨率以匹配你的显示器分辨率。这样你可以在不拉伸的情况下匹配屏幕比例，保持经典的冒险岛 1280x720 外观，并避免在 Ezorsia 配置中选择更高分辨率时出现的 UI 元素缩小问题

---

## 终端用户安全

本指南也旨在为终端用户提供尽可能安全的设置，所以我们需要谈谈这个。

### 使用旧版可执行应用程序 localhost

- 我建议直接使用默认游戏安装附带的客户端配合这个 DLL，但如果你真的想使用旧版可执行应用程序 localhost，请参阅下面的"终端用户安全（已过时）"部分
  - 如果必须使用，我不推荐使用除 Hendi 以外的任何可执行应用程序 localhost

### 使用第三方未公开源码的 Ezorsia V2 或类似版本

（最好只从我的 Ezorsia V2 releases 下载，或自己从源码编译）

- 这是有风险的，因为作为 Ezorsia V2 的创建者，我必须告诉你该项目使用了 Windows API 的一些强大功能，第三方可能利用这些功能将其变成恶意软件。即使他们不是故意将其变成恶意软件，如果误用（无论是意外还是故意），它仍然可能做一些令人讨厌的事情（要查看完整的功能列表，可以尝试将发布的 DLL 通过 VirusTotal 运行并查看"behaviors"标签页）
  - 基础 DLL 通过 Hook 多个 Windows API 函数与之交互，并原生使用多个潜在危险的功能，包括：
    - **文件释放能力**：我添加这个是因为注意到很多人觉得遵循完整说明很麻烦，只想下载后直接玩，所以我把所有东西都放进 DLL 并允许在运行时生成
    - **进程创建能力**：原生情况下，Ezorsia V2 只应在 WINAPI 创建窗口因不确定原因失败时创建进程来硬重启自身（这是默认打包客户端在 WINAPI 方面的失败，我没有找到其他修复方法）。但我无法保证第三方不会用这个来执行恶意进程，可能在释放一个 .exe 之后（即前面提到的功能）
  - **Hook dinput8.dll**：Ezorsia V2 Hook dinput8.dll 因为它是游戏使用的第二个最早的 DLL，这通常用于游戏模组，但需要注意的是，DirectInput 对象的创建可能被用于记录按键
    - 原生情况下，Ezorsia V2 只是将 Hook 的 dinput8.dll 函数导出以模拟真正的 DLL，没有进一步修改。但如果你注意到这些导出函数有修改并变成真正的 Hook/覆盖/重写，那就值得警惕，因为它可能被用于拦截按键。有时模组制作者会这样做来重新映射按键，但要极度警惕
- 如果你对 releases 部分的二进制文件本身有任何疑虑，可以下载源码并按照编译说明生成自己的二进制文件，你可以验证它与 releases 中的相同
  - 如果你对代码本身有疑虑，可以下载源码并检查，即使没有太多编程知识，你也可以将代码输入 GPT 并询问代码在做什么
    - 我努力确保我的发布对终端用户尽可能安全，但我理解信任很难获得，言语毫无价值，行动比言语更有说服力，所以我发布了源码以给你这些选择
- 总之，除非你完全信任他们（包括你的电脑生命），不要从第三方下载 Ezorsia V2 或类似版本
  - 或者如果你确实下载了第三方提供的 Ezorsia V2 或类似版本，如果有任何疑虑，请礼貌地要求他们提供源代码。Ezorsia V2 采用 AGPL 许可证的一个主要原因是终端用户透明度，他们有义务使用原始许可证

---

## 故障排除

### 如何在 config.ini 中禁用特定 Ezorsia V2 WZ 修改

如果 Ezorsia V2 的特定 WZ 修改与你的服务器自定义 WZ 冲突，你可以通过在 config.ini 中将其设置为 false 来禁用：

- `EzorsiaV2WzIncluded=false` - 完全禁用所有 Ezorsia V2 WZ 修改
- 其他具体修改选项可在 config.ini 中找到

### 其他常见问题

| 问题 | 解决方案 |
|------|----------|
| 游戏启动崩溃 | 检查 config.ini 中的 sleepTime 设置，确保等待 Themida 完全解包 |
| 登录界面崩溃 | 检查分辨率设置是否与 WZ 文件匹配 |
| 多客户端无法使用 | 确保 Hook_CreateMutexA 正常工作 |
| 中文输入卡门 | 尝试切换 imeType（0 或 1） |

---

## 服务器相关事项

### MySQL Workbench 配置

- 设置 MySQL Workbench 连接数据库服务器时，确保 [按如图所示输入参数](https://www.mediafire.com/view/iagchkgjqqvnaoe/connectguideUntitled.png/file)（假设使用 Cosmic）
- 我在这部分遇到过问题，所以记录下来希望能帮助其他人

### Docker 配置

- 如果你像我一样使用 Docker，[这个指南](https://dingyunxing.github.io/tutorial/2021/10/07/mysql-docker/) 也可能对你有帮助（包含所需的命令）

### 服务端配合

以下服务端修改可能有助于你：

- **免密登录**：服务端需要修改密码验证逻辑，客户端只需设置 `noPassword=true`
- **自定义经验表**：服务端和客户端的经验表数据必须匹配
- **上限突破**：服务端需要修改数据库/计算逻辑以匹配客户端上限

---

## 开发前的说明

### 作者说明

以下关于如何使用工具和编辑客户端的建议，只是我在加入这个圈子一个月内学到的内容。我有一些编程经验，但之前没有 C++ 经验，也没有汇编或逆向工程经验。很可能有更好的方法来做事情，甚至我自己的流程也在不断变化。到目前为止，这只是我设法收集到的内容、偶尔有人慷慨教导我的内容，以及在撰写时发现成功工作的内容。希望这能帮助你，但随时准备好学习更多！

### 关于打包客户端的说明

- 默认的 v83 客户端是 Themida 打包的，这意味着有些地址在运行时会被解包到不同的位置
- 对于这些情况，你需要找到模式并动态定位地址
- 一些地址是静态的，可以直接修改

### 关于地址冲突的说明

- 确保你找到的地址不存在于现有修改中
- 在 Visual Studio 中按 Ctrl+F，搜索范围设为"当前项目"
- 搜索相关地址，如 00849E39，也应搜索 00849E3、00849E、00849 等
- 地址相近时通常与同一功能区域相关，但不总是如此

---

## DLL 客户端开发所需工具

### 编译工具

| 工具 | 用途 | 说明 |
|------|------|------|
| **IDA Pro 7.0** | 反汇编器 | 用于查看和分析汇编代码，查看内存转储 |
| **v83/v95 IDB** | IDA 数据库 | 包含已识别的函数和枚举 |
| **Visual Studio 2019** | C++ 编译器 | 必须使用 Release x86 模式 |
| **x32dbg** | 调试器 | 查看正在运行的客户端内存，用于测试 |
| **十六进制编辑器** | 内存编辑 | 直接修改内存地址 |
| **Harepacker** | WZ 编辑器 | 编辑游戏资源文件 |

### IDB（IDA 数据库）资源

| 资源 | 说明 |
|------|------|
| [Angel 的 v83 IDB 发布](https://forum.ragezone.com/threads/v83-idb-client-edit-dump.1193418/) | v83 客户端转储，包含完整命名的函数 |
| [Angel 的 v95 IDB 发布](https://discord.com/channels/350831332609359875/1051899319491506298/1125628734347690065) | v95 IDB，可用于交叉参考 |
| [原始 v95 泄露](https://forum.ragezone.com/threads/getting-packet-structures-and-opcodes-with-ida-after-gms-new-update.872876/) | 如果上述链接失效，需要自己制作 v95 IDB |

**IDA 注意事项：**
- 使用破解版 IDA 7.0：https://rutracker.org/forum/viewtopic.php?t=5459068
- 我无法保证破解软件的安全性，建议考虑虚拟化（如 Sandboxie）
- 更新版本的 IDA 可能无法读取旧版 IDB 文件

### Ezorsia V2 源码

- [MapleEzorsia-v2 源码](https://github.com/444Ro666/MapleEzorsia-v2)

### 数据转换工具（在线工具，建议收藏）

| 工具 | 用途 | 链接 |
|------|------|------|
| **十进制/十六进制转换器** | 验证十六进制值 | https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html |
| **x86 汇编/反汇编器** | 将内存转储中的十六进制组转换为准确的 ASM 指令 | https://defuse.ca/online-x86-assembler.htm#disassembly |
| **IEEE 754 浮点转换器** | 转换 64 位值（如伤害上限） | https://baseconvert.com/ieee-754-floating-point |

### IDA 设置

1. 在 IDA 中打开 v83 客户端
2. 加载 v83 IDB（或 v95 IDB 配合使用）
3. 使用字符串搜索找到相关函数
4. 按 F5 生成伪代码进行分析

### Visual Studio 编译设置

- 使用 **Release x86** 模式
- 工具集：**VS2019 (v142)**
- SDK：**Windows 10 SDK**
- 编译后的 DLL 位于 `out/Release` 目录

---

## DLL 客户端开发流程

### 步骤 1：在 IDA 中定位地址

找到与你需要修改的二进制内存区域相关的线索，可以通过以下方式：

1. **使用 v95 IDB 的函数区域**
   - 在完整命名的 v95 IDB 中查找相关函数
   - 后续需要在 v83 转储中查找类似功能的区域，但可以验证很多东西
   - v95 IDB 生成的伪代码通常更容易阅读

2. **使用 StringPool（枚举）**
   - 通过 StringPool 查找内存转储中的相关区域
   - 需要通过 WZ 文件查找相关字符串

3. **使用现有地址**
   - 使用影响你想要修改内容的现有地址，在同一区域查找

### 步骤 2：分析汇编和伪代码

1. 查看步骤 1 中识别区域的汇编代码
2. 按 F5 将其转换为伪代码
3. 可以右键在 IDA 视图和伪代码之间同步，或查看左下角显示伪代码光标所在的地址

**分析要点：**
- 过程式编程的知识和经验非常有帮助，这决定了你的效率
- 追踪变量何时初始化和清除，值如何传递，机制如何协同工作
- 右键子程序的函数名，点击"列出交叉引用到/从"查看其他相关子程序
- 尝试找到函数的构造函数（如 `CUIScreenMsg::CUIScreenMsg`），很多东西在那里初始化
- 大多数情况下，一个特定的子程序不会包含所有你需要的内容
  - 例如：初始线索可能指向 `CUIScreenMsg::CUIScreenMsg`，但你需要在 `CUIScreenMsg::LayoutScrMsg` 中进行修改，因为前者调用后者
- IDA 的流程图视图可能有帮助

**输出结果：**
- 你应该得到要修改的 ASM 指令起始地址，以及要修改成的内容
- 如果使用 Code Cave 修改整段内存，还需要返回地址和初始地址与返回地址之间的字节数量（用于 NOP 计数，最少 5）

**地址验证：**
- 确保找到的地址不存在于现有修改中：在 Visual Studio 中按 Ctrl+F，搜索范围设为"当前项目"
- 同时搜索相关地址，如对于 00849E39，也应搜索 00849E3、00849E、00849、0084 等
- 地址相近时通常与同一功能区域相关，但不总是如此
- 确保不会做出冗余或冲突的修改
- 确保修改顺序正确：如果一个修改依赖另一个，确保依赖的修改在它依赖的修改之后执行

### 步骤 3：测试修改

使用 `client.cpp` 底部的"测试"内存编辑函数：

```cpp
// 内存直接编辑测试
Memory::WriteAddress(0xXXXXXX, newValue);

// Code Cave 测试（在 codecaves.h 中填写相关信息）
```

**注意事项：**

**直接编辑内存时：**
- 确保输入的值适合该内存区域，否则游戏会在执行时崩溃
- 注意 ASM 指令起始偏移后有多少字节空间可用
- 单字节最大值只能是 255

**Code Cave 时：**
- 尝试添加或修改指令，而不影响从 Code Cave 原始位置取出的现有指令
- 不要干扰栈上的变量，否则应用程序会崩溃
- 如果崩溃，尝试渐进式修改：
  - 先完全复制 Code Cave 中的原指令，不做任何修改，让它工作
  - 然后逐步修改，让它工作

**函数替换：**
- 也可以使用函数替换来以自己的方式使用客户端的函数
- 或修改原函数的工作方式（如果不需要在函数中间进行修改）
- 见源码中的注释（作者在实践中没有太多经验）

### 步骤 4：编译和验证

1. 编译 DLL，替换旧的，运行游戏，测试修改
2. 如果修改正确，将测试用的代码行迁移到自己命名的代码行中

**编译设置：**
- 使用这些构建设置：https://www.mediafire.com/view/9ssrqg8eiwbh0k1/buildsettings2.png/file
- 如果生成的 DLL 不工作，尝试这个设置：https://www.mediafire.com/view/6xk7b9bf8qv3gda/buildsettingsEzorsia.png/file

**注意：** 这些指令一开始可能不容易理解，这很正常。你需要一定程度的理解才能执行。以下是一些帮助我的教程：

---

## DLL 客户端开发教程

以下教程没有特定顺序，但我尝试将更高级的放在底部。你可能需要来回跳转教程并偶尔重新学习以掌握正在发生的事情。

### IDA/IDB 相关

- [使用 v95 IDB 与 v83 IDB 进行修改](https://forum.ragezone.com/threads/getting-packet-structures-and-opcodes-with-ida-after-gms-new-update.872876/)（如果使用已有枚举 ID 的 IDB，可以跳过字符串部分）
- [IDA 和 IDB 使用指南](https://forum.ragezone.com/threads/how-to-use-ida-in-v83.1107216/)
- [移除客户端检查示例](https://forum.ragezone.com/threads/removing-a-check-in-the-maplestory-client-v83.1147791/)

### C++ 基础

- [C++ 条件语句教程](https://www.kindsonthegenius.com/cplusplus/c-conditional-statements/) - 更新 DLL 代码
- [C++ 变量和基本类型](https://cplusplus.com/doc/tutorial/variables/) - 处理值时很有用

### Code Cave

- [Code Cave 入门指南](https://www.codeproject.com/Articles/20240/The-Beginners-Guide-to-Codecaves) - 了解什么是 Code Cave

### 汇编语言

- [x86 汇编基础](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html) - 教授栈如何工作、各种寄存器以及指令
- [汇编指令示例教程](https://www.tutorialspoint.com/assembly_programming/assembly_logical_instructions.htm) - 通过示例教授指令
- [MOVS 指令说明](https://www.scs.stanford.edu/05au-cs240c/lab/i386/MOVS.htm) - 关于 movsd 指令
- [x86-64 汇编教程](https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+Arch1001_x86-64_Asm+2021_v1/course/) - 另一个汇编教程（尚未注册但被推荐）

### 调用约定

- [x86 调用约定](https://en.m.wikibooks.org/wiki/X86_Disassembly/Calling_Conventions) - 对函数替换和理解子程序如何读取栈值非常有用（也解释了如名称修饰和子程序如何返回值等内容）

### 函数替换示例

- [自定义字符串池](https://forum.ragezone.com/threads/custom-string-pool.1148502/)
- [AuthHook 示例代码](https://github.com/pokiuwu/AuthHook-v176-StringPool/blob/master/Client176/MapleHook.cpp)

### Eric 的教程视频

- [视频 1](https://discord.com/channels/350831332609359875/939516633096015932/939517377136185374)
- [视频 2](https://discord.com/channels/350831332609359875/939516633096015932/939525229359816786)

**注意：** 如果你完全没有编程经验，并且在解释伪代码和 C++ 源码时遇到极大困难以至于无法工作，你应该查找更多关于过程式编程的初学者教程。如果你有有限的编程经验，通常可以像我一样边学边做。

---

## 实用资源

### 服务器源码

- **Cosmic**（频繁更新的 v83 开源服务器）：https://github.com/P0nk/Cosmic
- **BeiDou**（Cosmic 的中文优化版）：https://github.com/BeiDouMS/BeiDou-Server

### 原版 Ezorsia

- **MapleEzorsia**：https://github.com/izarooni/MapleEzorsia

### WZ 工具

| 工具 | 说明 |
|------|------|
| [WzComparerR2](https://github.com/Kagamia/WzComparerR2) | WZ 文件差异对比工具 |
| [Harepacker-resurrected](https://github.com/lastbattle/Harepacker-resurrected) | WZ 编辑器 |
| [更好的 WZ 编辑器](https://discord.com/channels/350831332609359875/939516633096015932/1158733731411001375) | 推荐使用 |

### 其他工具

| 工具 | 说明 |
|------|------|
| [MapEditor](https://www.mediafire.com/file/ez85hdtpvy601ym/MapEditor.rar/file) | 地图编辑器 |
| [STREDIT](https://github.com/diamondo25/STREDIT) | 客户端字符串提取器 |
| [Magicmida](https://github.com/Hendi48/Magicmida) | Themida 解包器 |
| [干净客户端镜像](https://mega.nz/file/grdRnR5I#tU624QukdO0mrc4m-7Exp1i1_3oeyB8HpowrRFl9-q8) | Hendi 4G 客户端备份 |
| [MapleClientEditTemplate](https://github.com/MapleStory-Archive/MapleClientEditTemplate) | C# 启动器模板 |
| [mushroom_redirector](https://github.com/necronomicon/mushroom_redirector) | C 语言启动器 |

### 其他指南

- [v83 分辨率修改地址大全](https://forum.ragezone.com/threads/all-addresses-for-v83-resolution-change.1161938/)
- [WZ 编辑修复指南](https://forum.ragezone.com/threads/v62-v83-for-wz-edits-hair-item-cap-client-fix.1125064/)

---

## 常用修改地址参考

以下是开发中常用的一些地址类型：

| 功能类型 | 示例地址范围 | 说明 |
|----------|--------------|------|
| 分辨率修改 | 0x00XXXXXX | 游戏窗口大小、UI 元素位置 |
| 上限突破 | 0x00XXXXXX | 攻击力、魔攻、移速等上限 |
| UI 显示 | 0x00XXXXXX | Boss 血条、消息数量等 |
| 输入处理 | 0x00XXXXXX | 中文输入、IME 修复 |
| 网络连接 | 0x00XXXXXX | 服务器 IP、端口 |

---

**翻译说明**：本文档翻译自 MapleEzorsia-v2 Wiki，用于 BeiDou 客户端开发参考。原始文档位于 https://github.com/444Ro666/MapleEzorsia-v2/wiki