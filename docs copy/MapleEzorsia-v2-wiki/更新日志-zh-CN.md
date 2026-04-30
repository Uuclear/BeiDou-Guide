# MapleEzorsia-v2 更新日志

## 2023年10月

### 2023/10/11
- 修复了 Cash Shop UI 在某些元素上需要过多点击才能工作的问题

### 2023/10/12
- 添加可选的 tubi 和用户自定义伤害上限/属性面板伤害上限
- 添加了登录 UI 元素可移动到屏幕边缘的选项，适用于扩展到全屏的登录框架

### 2023/10/14
- 添加可选的用户自定义最大移动速度/上限，可在属性显示中查看

### 2023/10/17
- **重大更新**：修改了 patch 加载 wz 数据的方式（现在根据选择的分辨率自动选择登录框架）
- **需要新的 WZ 文件**：[下载 EzorsiaV2_UI.wz](https://www.mediafire.com/file/6bimll8wtpbclmx/EzorsiaV2_UI.wz/file)，替换旧文件（适用于所有分辨率）
- 添加了 1024x768 的登录框架
- 修复了快捷栏交互不工作的问题

### 2023/10/23
- **重大更新**：patch 现在使用 ijl15.dll 替代 nmconew.dll
- **使用说明**：
  - 如果之前使用过 patch，删除 nmconew.dll
  - 将 nmconew2.dll 重命名为原始名称
  - 将 ijl15.dll 重命名为 2ijl15.dll
  - 将新的 ijl15.dll 放入文件夹
- 服务器 IP 地址现在在 patch 的 config.ini 中设置，无需 hex 编辑
- 修复了 mu lung dojo 崩溃问题
- 现在支持没有内置多客户端功能的客户端进行多开

### 2023/10/24
- 添加客户端自定义经验表支持（无配置选项，可在 ReplacementFuncs.h 中修改 v83 的 `_lpfn_NextLevel_Hook` 预定义数组，或创建自己的公式）
- **注意**：客户端数据必须与服务端数据匹配，32位 int 最大值仍然适用

---

## 2023年11月

### 2023/11/17
- **重大更新**：现在可作为独立的 DLL 客户端/localhost 使用
- **使用说明**：
  - patch 现在使用 dinput8.dll，不再需要替换文件夹中的任何 dll
  - 如果之前使用过 patch，删除 ijl15.dll，将 2ijl15.dll.dll 重命名为原始名称
- 修复了请求弹出窗口（如交易、组队等）出现在错误位置的问题

**配置变更**：
- VirtualProtect 不再是配置选项，而是永久开启（因为即使 CRC bypass 后，某些部分仍然是只读的）
- 可选：添加了使用 v62 经验表的选项（如果服务器使用 v62 经验率）
- 可选：添加了加载 3 个自定义 dll 的能力，这些必须在游戏文件夹中；Ezorsia V2 的修改在冲突时优先
- 添加 debug 部分：添加了初始化 sleepTime 选项，因为加载是时间敏感的

### 2023/11/18
- 紧急修复 Themida 相关的启动失败和 error 0 启动失败
- sleepTime 选项可能仍需要用于加载自定义 dll，但其他情况应保持为 0

### 2023/11/21
- **相对重大的更新**：
- DLL 现在包含 Ezorsia V2 所需的所有资源，无需其他文件或可能与服务器特定 WZ/IMG 文件冲突
  - Ezorsia V2 现在会为用户生成其他自定义：config、wz 和 img 文件（如果需要）
  - Ezorsia V2 现在从生成的文件加载，无需覆盖默认文件
  - Ezorsia V2 wz 和 img 文件正式添加到 repo
- 终止了 CsecurityClient::OnPacket
- 重写了 CRC 检查器以在匿名函数调用时不执行任何操作
- 修复启动时的前台焦点问题

**配置变更**：
- Ezorsia V2 现被认为总是包含的，因为它会生成自己的文件
- 大登录框架默认开启（用于使用自己框架的人）
- customloginframe 替代 ownloginframe 以减少冗余，现在在 optional 部分

---

**翻译说明**：本文档翻译自 MapleEzorsia-v2 Wiki Change-Log，用于 BeiDou 客户端开发参考。