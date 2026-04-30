# MapleEzorsia-v2 待办事项列表

这是开发者的临时待办列表，记录了正在开发和计划开发的功能。

---

## 高优先级任务

### 异常处理重写
- 为重写功能实现异常处理（当前 Hook 的 throw error 似乎没有效果）
- 附加：寻找不包含"code of conduct"的异常处理模板
- 推荐：使用 stackwalker 来处理这个问题

### Themida 打包部分重写
- 重写其他 Themida 打包的部分

### 分辨率崩溃修复
- 修复 x1024、x1366 和 x1600 分辨率崩溃问题（某些用户遇到）

---

## 中优先级任务

### 硬件断点
- DR-check 检查的硬件断点
- TryDoAttack 调用 GetThreadContext 的处理

### 弹窗位置问题
- SMega 和其他弹窗框显示在窗口外或向下偏移的问题

### 自定义 HWID
- 实现自定义硬件 ID：参考讨论链接

### Tubi Hook
- 实现 Tubi Hook：参考讨论链接

### 快捷栏优化
- 快捷栏缩小功能

### 内部窗口保存位置
- 修复装备栏和物品栏等内部窗口在默认 800x600 区域外放置时不保存位置的问题

### 换线弹窗居中
- 换线弹窗居中显示

---

## 图形修复相关

### GFX 内存问题（heap fragmentation）

**问题分析：**
- 由堆内存碎片化引起
- 主要来自 Boss 战或大量使用 GFX 的内容
- 自定义 WZ 文件（由 Harepacker 压缩）会增加问题，因为 Harepacker 不能正确处理 PNG 文件的压缩

**解决方案：**
- 清除缓存
- 修改 GFX 函数（临时修复，因为会重置某些缓存状态）
- 预分配内存并在失败时调用预分配部分
- Boss 战脚本创建和销毁怪物时的分配大小优化
- 直接从 .img 加载（可能绕过 Harepacker 问题）
- 懒加载以节省内存
- Hook RtlAllocate（太复杂，涉及所有资源分配）

**十六进制编辑修复（如果直接 hex edit）：**
- resman.dll 需要应用 2 个补丁
- MapleStory.exe 需要 2 个补丁（实际上 prebb 客户端需要 9 个）

**参考链接：**
- https://forum.ragezone.com/threads/client-unresponsive.1146934/

---

## 其他待办

### 魔法数字注释
- 在注释中定义所有魔法数字

### CashShop 焦点恢复
- 使用函数替换正确调用 CashShop 焦点恢复

### 属性窗口背景
- 状态窗口背景实现
- 研究：main stat window 如何加载背景（偏移量 212/218）

### VR（视野范围）修改
- 地图的 VR 修改（地址在 client.cpp 中标注）
- 测试新的 VR 地址

### IDA 工具
- 尝试让 diaphora/bindiff/sigmaker 在 IDA 7 中工作

### v95 函数查找
- 在 v95 中搜索 get_screen_height
- 查找以下在 v83 中可能需要检查的函数：

```cpp
// 这些函数在 v95 中使用 get_screen_height，与分辨率相关
CWndMan::ResetOrgWindow(CWndMan *this)
CWnd::OnMoveWnd(CWnd *this, int l, int t)
CUIArtSpeakerSample::CUIArtSpeakerSample(CUIArtSpeakerSample *this, int nItemID, tagPOINT pt)
CUIContextMenu::CUIContextMenu(CUIContextMenu *this, ZXString<char> sCharacterName, tagPOINT pt, int bCantFollow)
get_screen_height()  // 原始函数，可能不存在于 v83

CUIToolTip::SetToolTip_Equip2(CUIToolTip *this, int x, int y, GW_ItemSlotEquip *pe1, GW_ItemSlotEquip *pe2, int bVertical, int nNpcShopTimeLimitedItemPeriod, int bSetItemView)
CUIToolTip::AddToolTip_SetItem(CUIToolTip *this, int x, int y, GW_ItemSlotEquip *pe, IWzGr2DLayer* pLayerEquip)
CUIToolTip::MakeLayer(CUIToolTip *this, IWzCanvas* result, int nLeft, int nTop, int bDoubleOutline, int bLogin, int bCharToolTip, unsigned int uColor, int bAdditional)

CSummoned::ProcessAttack(CSummoned *this, int tCur)
CScreenShot::SaveFullScreenToJpg(ZXString<char> *sFileName)
CMapLoadable::RestoreViewRange(CMapLoadable *this)
CMapLoadable::TransientLayer_Weather(CMapLoadable *this, ZXString<unsigned short> *sPath, int nType, int nDirection, int nSpeed)
CMapLoadable::MakeGrid(CMapLoadable *this, IWzGr2DLayer* pLayer, int type, int cx, int cy, int alpha, int nAnimate, int bObj, ZRef<ZList<IWzGr2DLayer>> pList, unsigned int ulColor)

CInputSystem::Init(CInputSystem *this, HWND__ *hWnd, void **ahEvent)
CInputSystem::SetCursorPos(CInputSystem *this, int x, int y)
```

---

## 高难度任务

### 消息消失机制（困难）
- 找到方法让 CUIScreenMsg 消息在达到最大消息数时消失，而不是循环回到底部
- 当前问题：重用的层会以更快的时间淡出，但出现在旧消息下方，导致新消息淡出更快，并在屏幕中间留下空白区域
- 注意：这在原版客户端中也存在，但由于只有 6 条最大消息，不太明显

### 右键输入灵敏度
- 改变右键点击输入灵敏度，使其与左键相同（为左手用户和喜欢使用右键的用户）

### Boss 血条位置检测
- 检测服务器消息是否存在，如果存在，将 Boss 血条移动到服务器消息下方（低优先级）

### VR Top/Bottom 全地图支持
- VR top 和 bottom 在所有地图上正常工作
- 需要让自定义 VR top 和 bot 工作（基于选择的分辨率或某种地图数据）
- 许多旧地图缺少 VR top 和 bottom 数据，新地图有这些数据

### 地图背景缩放
- 找到方法让地图背景更好地适应分辨率，而不需要在每个地图上单独编辑
- 困难：地图背景的元素排列方式高度可变

### 物品名称显示长度
- 移除显示获得长名称物品时的 15 字符限制
- 考虑：1280x720 已经有较长名称的显示长度问题

---

## 原版 Bug 修复

### 联盟信息
- 修复角色联盟信息？（角色视图中的联盟信息是否损坏？）

### EXP 提示
- 修复 UI stat exp tool tip？（悬浮在某些 UI 上时，exp 数量弹窗（透明的黑色 ###/### 弹窗）是否不工作？）

---

**翻译说明**：本文档翻译自 MapleEzorsia-v2 Wiki my-to-do-list，用于 BeiDou 客户端开发参考。这些待办事项可以帮助开发者了解项目的发展方向和潜在改进点。