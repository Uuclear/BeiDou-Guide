# BeiDou-ijl15 逐符号中文职责索引

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`/tmp/BeiDou-ijl15`
> 文件数：48

## `AddyLocations.h`

## `AutoTypes.h`
- `_IWzFileSystem__Init(...)`：通用业务逻辑入口，需结合实现查看细节。
- `_IWzNameSpace__Mount(...)`：通用业务逻辑入口，需结合实现查看细节。

## `BossHP.cpp`
- `BossHP::Hook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::HookInternal(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::HookUpdate(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::SetHook(...)`：写入或更新状态字段。
- `BossHP::HookShowMobHPTag(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::HookInitField(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::DisposeBossHpNumber(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::DisposeToolTip(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::CreateToolTip(...)`：创建对象、会话或业务记录。
- `BossHP::HookDisposeField(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::DrawBossHpNumberIfNeed(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::SetToolTip_String(...)`：写入或更新状态字段。
- `BossHP::DrawBossHpNumber(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::ClearToolTip(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::GetMiniMapWidth(...)`：读取并返回状态/数据。
- `ReadInt(...)`：通用业务逻辑入口，需结合实现查看细节。

## `BossHP.h`
- `class BossHP`：领域类型或功能模块，职责由同名文件实现定义。
- `Hook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookInternal(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookUpdate(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookShowMobHPTag(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookDisposeField(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookInitField(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SetToolTip_String(...)`：写入或更新状态字段。
- `ClearToolTip(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DisposeToolTip(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CreateToolTip(...)`：创建对象、会话或业务记录。
- `DrawBossHpNumberIfNeed(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DrawBossHpNumber(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DisposeBossHpNumber(...)`：通用业务逻辑入口，需结合实现查看细节。
- `GetMiniMapWidth(...)`：读取并返回状态/数据。

## `Client.cpp`
- `Client::UpdateGameStartup(...)`：更新已有对象/配置/缓存。
- `Memory::FillBytes(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteInt(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteDouble(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::UpdateResolution(...)`：更新已有对象/配置/缓存。
- `Memory::CodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteByteArray(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteByte(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::EnableNewIGCipher(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::UpdateLogin(...)`：更新已有对象/配置/缓存。
- `Client::FixMouseWheel(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::Chinese(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixIme::HookOld(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixIme::HookNew(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixBuddy::Hook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::LongQuickSlot(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixDateFormat(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixItemType(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::JumpCap(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixChatPosHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::NoPassword(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::MoreHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::WorldMap(...)`：通用业务逻辑入口，需结合实现查看细节。

## `Client.h`
- `class Client`：领域类型或功能模块，职责由同名文件实现定义。
- `UpdateGameStartup(...)`：更新已有对象/配置/缓存。
- `EnableNewIGCipher(...)`：通用业务逻辑入口，需结合实现查看细节。
- `UpdateResolution(...)`：更新已有对象/配置/缓存。
- `UpdateLogin(...)`：更新已有对象/配置/缓存。
- `FixMouseWheel(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Chinese(...)`：通用业务逻辑入口，需结合实现查看细节。
- `LongQuickSlot(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixDateFormat(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixItemType(...)`：通用业务逻辑入口，需结合实现查看细节。
- `JumpCap(...)`：通用业务逻辑入口，需结合实现查看细节。
- `FixChatPosHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `NoPassword(...)`：通用业务逻辑入口，需结合实现查看细节。
- `MoreHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WorldMap(...)`：通用业务逻辑入口，需结合实现查看细节。

## `FixBuddy.h`
- `class FixBuddy`：领域类型或功能模块，职责由同名文件实现定义。
- `Memory::CodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixBuddyAccept(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Hook(...)`：通用业务逻辑入口，需结合实现查看细节。

## `FixIme.h`
- `class FixIme`：领域类型或功能模块，职责由同名文件实现定义。
- `Memory::CodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::FillBytes(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteByte(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DisableIme(...)`：通用业务逻辑入口，需结合实现查看细节。
- `setOnFocusFirstJudgement(...)`：写入或更新状态字段。
- `switchIme(...)`：通用业务逻辑入口，需结合实现查看细节。
- `switchMLIme(...)`：通用业务逻辑入口，需结合实现查看细节。
- `newSwitchIme(...)`：创建对象、会话或业务记录。
- `destroyWindow(...)`：通用业务逻辑入口，需结合实现查看细节。
- `newSwitchMLIme(...)`：创建对象、会话或业务记录。
- `HookOld(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookNew(...)`：通用业务逻辑入口，需结合实现查看细节。
- `GeneralHook(...)`：通用业务逻辑入口，需结合实现查看细节。

## `HpMpAlert.cpp`
- `Memory::WriteInt(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::SetHook(...)`：写入或更新状态字段。
- `TryReadDword(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ClampAlert(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SendHpMpAlertFromStatusBar(...)`：向外发送响应、消息或网络包。
- `ApplyHpMpAlertToStatusBar(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HandleHpMpAlertPacket(...)`：处理事件/请求/消息分发。
- `SaveGlobal_Hook(...)`：持久化当前状态到存储层。
- `ProcessPacket_Hook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookSaveGlobal(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookHpMpAlertRecv(...)`：通用业务逻辑入口，需结合实现查看细节。

## `HpMpAlert.h`
- `HookSaveGlobal(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookHpMpAlertRecv(...)`：通用业务逻辑入口，需结合实现查看细节。

## `INIReader.h`
- `class INIReader`：领域类型或功能模块，职责由同名文件实现定义。
- `INIReader::INIReader(...)`：通用业务逻辑入口，需结合实现查看细节。
- `INIReader::ParseError(...)`：解析输入文本或二进制内容。
- `INIReader::Sections(...)`：通用业务逻辑入口，需结合实现查看细节。
- `INIReader::Get(...)`：读取并返回状态/数据。
- `INIReader::GetInteger(...)`：读取并返回状态/数据。
- `INIReader::GetReal(...)`：读取并返回状态/数据。
- `INIReader::GetFloat(...)`：读取并返回状态/数据。
- `INIReader::GetBoolean(...)`：读取并返回状态/数据。
- `std::transform(...)`：通用业务逻辑入口，需结合实现查看细节。
- `INIReader::MakeKey(...)`：通用业务逻辑入口，需结合实现查看细节。
- `INIReader::ValueHandler(...)`：处理事件/请求/消息分发。
- `ini_parse(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ini_parse_file(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ini_parse_stream(...)`：通用业务逻辑入口，需结合实现查看细节。

## `MapleClientCollectionTypes/TSecType.h`
- `class TSecData`：领域类型或功能模块，职责由同名文件实现定义。
- `class TSecType`：领域类型或功能模块，职责由同名文件实现定义。
- `class SECPOINT`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZAllocAnonSelector.h`

## `MapleClientCollectionTypes/ZAllocBase.h`
- `class ZAllocBase`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZAllocEx.cpp`

## `MapleClientCollectionTypes/ZAllocEx.h`
- `malloc(...)`：通用业务逻辑入口，需结合实现查看细节。
- `malloc(...)`：通用业务逻辑入口，需结合实现查看细节。
- `new(...)`：创建对象、会话或业务记录。
- `delete(...)`：删除对象、关系或临时状态。

## `MapleClientCollectionTypes/ZAllocStrSelector.h`

## `MapleClientCollectionTypes/ZArray.h`
- `class ZArray`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZFatalSection.h`

## `MapleClientCollectionTypes/ZList.h`
- `class ZList`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZMap.h`
- `class ZMap`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRecyclable.h`
- `class ZRecyclable`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRecyclableAvBuffer.h`
- `class ZRecyclableAvBuffer`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRecyclableStatic.h`
- `class ZFakeStatAvBuff`：领域类型或功能模块，职责由同名文件实现定义。
- `class ZRecyclableStatic`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRef.h`
- `class ZRef`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRefCounted.h`
- `class ZRefCounted`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRefCountedAccessor.h`
- `class ZRefCountedAccessor`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZRefCountedDummy.h`
- `class ZRefCountedDummy`：领域类型或功能模块，职责由同名文件实现定义。

## `MapleClientCollectionTypes/ZXString.h`
- `class ZXString`：领域类型或功能模块，职责由同名文件实现定义。
- `strlen(...)`：通用业务逻辑入口，需结合实现查看细节。
- `wcslen(...)`：通用业务逻辑入口，需结合实现查看细节。

## `MapleClientCollectionTypes/ZtlSecure.h`
- `class SECRECT`：领域类型或功能模块，职责由同名文件实现定义。

## `Memory.cpp`
- `Memory::SetHook(...)`：写入或更新状态字段。
- `Memory::FillBytes(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::ReplaceString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteByte(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteShort(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteInt(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteDouble(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::WriteByteArray(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Memory::CodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。

## `Memory.h`
- `class Memory`：领域类型或功能模块，职责由同名文件实现定义。
- `SetHook(...)`：写入或更新状态字段。
- `FillBytes(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ReplaceString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteString(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteByte(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteShort(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteInt(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteDouble(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。
- `WriteByteArray(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PatchNop(...)`：通用业务逻辑入口，需结合实现查看细节。

## `NMCO.cpp`
- `NMCO::CreateHook(...)`：创建对象、会话或业务记录。
- `NMCO_CallNMFunc(...)`：通用业务逻辑入口，需结合实现查看细节。
- `NMCO_CallNMFunc2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `NMCO_MemoryFree(...)`：通用业务逻辑入口，需结合实现查看细节。

## `NMCO.h`
- `class NMCO`：领域类型或功能模块，职责由同名文件实现定义。
- `CreateHook(...)`：创建对象、会话或业务记录。

## `ReplacementFuncs.h`
- `Memory::SetHook(...)`：写入或更新状态字段。
- `HookGetModuleFileName(...)`：通用业务逻辑入口，需结合实现查看细节。
- `HookCreateWindowExA(...)`：通用业务逻辑入口，需结合实现查看细节。
- `create_window_ex_a(...)`：创建对象、会话或业务记录。
- `_CreateMutexA(...)`：通用业务逻辑入口，需结合实现查看细节。

## `ZAllocEx.cpp`

## `codecaves.h`
- `AdjustStatusBar(...)`：通用业务逻辑入口，需结合实现查看细节。
- `AdjustStatusBarBG(...)`：通用业务逻辑入口，需结合实现查看细节。
- `AdjustStatusBarInput(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionLoginDlg(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionLoginUsername(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionLoginPassword(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionBossBarY(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionBossBarY1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `PositionBossBarY2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix5(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix6(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix7(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFix8(...)`：通用业务逻辑入口，需结合实现查看细节。
- `CashShopFixPrev(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix5(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix6(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix7(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ITCFix8(...)`：通用业务逻辑入口，需结合实现查看细节。
- `VersionNumberFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `AlwaysViewRestoreFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccLoginBackCanvasFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccLoginViewRecFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccLoginDescriptorFix(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMoreGainMsgs(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMoreGainMsgsFade(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMoreGainMsgsFade1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidPlayer(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidClock(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidMonster(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidMonster1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidMonster2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidEngBar(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidEngBar1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidEngBar2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidClearRoundUI(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidTimerCanvas(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidTimerMinutes(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidTimerSeconds(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidTimerBar(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccMuruengraidMonster1_2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccStatsSubMov(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ccCLoginSendCheckPasswordPacket(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E550(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E5BE(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E5DB(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E6AC(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E71D(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E80C(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044E8B4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044EA22(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044EA6F(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044EBD6(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044ECA1(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044ED32(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044ED52(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x0044EED3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494943(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494BB6(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494CA9(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494CF0(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494D3B(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494EAF(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494EEC(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00494F87(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F4E84(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F4EC3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F4F12(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F4FC6(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F503C(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F51A7(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F526F(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F5653(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F5833(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F5C2C(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F5CA3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F5FBD(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F631C(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F691F(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F6F36(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F6F5C(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F7CFA(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F7D83(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F81FB(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F84E9(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x009F8AD4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BB39(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BC79(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BD05(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BD4E(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BD99(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BDE3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BDFE(...)`：通用业务逻辑入口，需结合实现查看细节。
- `cc0x00A4BE47(...)`：通用业务逻辑入口，需结合实现查看细节。
- `testingCodeCave(...)`：通用业务逻辑入口，需结合实现查看细节。
- `testingCodeCave2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `testingCodeCave3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `testingCodeCave4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixMouseWheelHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixDateFormat(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixDateFormat2(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixDateFormat3(...)`：通用业务逻辑入口，需结合实现查看细节。
- `fixDateFormat4(...)`：通用业务逻辑入口，需结合实现查看细节。
- `getItemType1(...)`：读取并返回状态/数据。
- `getItemType2(...)`：读取并返回状态/数据。
- `calcClimbSpeed(...)`：通用业务逻辑入口，需结合实现查看细节。
- `darkMap1cc(...)`：通用业务逻辑入口，需结合实现查看细节。
- `darkMap2cc(...)`：通用业务逻辑入口，需结合实现查看细节。
- `darkMap3cc(...)`：通用业务逻辑入口，需结合实现查看细节。

## `detours.h`
- `DetourTransactionBegin(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourTransactionAbort(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourTransactionCommit(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourTransactionCommitEx(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourUpdateThread(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourSetIgnoreTooSmall(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourSetRetainRegions(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourSetSystemRegionLowerBound(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourSetSystemRegionUpperBound(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourGetContainingModule(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourEnumerateModules(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourGetEntryPoint(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourGetModuleSize(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourGetSizeOfPayloads(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryOpen(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryDeletePayload(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryPurgePayloads(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryResetImports(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryWrite(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourBinaryClose(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourRestoreAfterWith(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourIsHelperProcess(...)`：通用业务逻辑入口，需结合实现查看细节。
- `LPAPI_VERSION(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DWORD(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DWORD(...)`：通用业务逻辑入口，需结合实现查看细节。
- `DetourLoadImageHlp(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SetInstruction(...)`：写入或更新状态字段。
- `SetInstruction0(...)`：写入或更新状态字段。
- `SetInstruction1(...)`：写入或更新状态字段。
- `SetInstruction2(...)`：写入或更新状态字段。
- `GetBits(...)`：读取并返回状态/数据。
- `SetBits(...)`：写入或更新状态字段。
- `GetImm7a(...)`：读取并返回状态/数据。
- `SetImm7a(...)`：写入或更新状态字段。
- `GetImm13c(...)`：读取并返回状态/数据。
- `SetImm13c(...)`：写入或更新状态字段。
- `GetSignBit(...)`：读取并返回状态/数据。
- `SetSignBit(...)`：写入或更新状态字段。
- `GetImm20a(...)`：读取并返回状态/数据。
- `SetImm20a(...)`：写入或更新状态字段。
- `GetImm20b(...)`：读取并返回状态/数据。
- `SetImm20b(...)`：写入或更新状态字段。
- `SignExtend(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SetInst(...)`：写入或更新状态字段。
- `SetInst0(...)`：写入或更新状态字段。
- `SetInst1(...)`：写入或更新状态字段。
- `SetInst2(...)`：写入或更新状态字段。
- `SetData(...)`：写入或更新状态字段。
- `SetData0(...)`：写入或更新状态字段。
- `SetData1(...)`：写入或更新状态字段。
- `SetData2(...)`：写入或更新状态字段。
- `SetNop(...)`：写入或更新状态字段。
- `SetNop0(...)`：写入或更新状态字段。
- `SetNop1(...)`：写入或更新状态字段。
- `SetNop2(...)`：写入或更新状态字段。
- `SetBrl(...)`：写入或更新状态字段。
- `SetBrl(...)`：写入或更新状态字段。
- `SetBrlTarget(...)`：写入或更新状态字段。
- `SetBrlImm(...)`：写入或更新状态字段。
- `SetMovlGp(...)`：写入或更新状态字段。
- `SetStop(...)`：写入或更新状态字段。

## `detver.h`

## `dllmain.cpp`
- `std::string(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::UpdateGameStartup(...)`：更新已有对象/配置/缓存。
- `Client::UpdateResolution(...)`：更新已有对象/配置/缓存。
- `Client::FixMouseWheel(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::Chinese(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::LongQuickSlot(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixDateFormat(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixItemType(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::JumpCap(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::FixChatPosHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::NoPassword(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::MoreHook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `BossHP::Hook(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Client::WorldMap(...)`：通用业务逻辑入口，需结合实现查看细节。
- `ijl15::CreateHook(...)`：创建对象、会话或业务记录。
- `CreateConsole(...)`：创建对象、会话或业务记录。
- `reader(...)`：通用业务逻辑入口，需结合实现查看细节。

## `dllmain.h`
- `CreateConsole(...)`：创建对象、会话或业务记录。
- `CreateHook(...)`：创建对象、会话或业务记录。

## `ijl15.cpp`
- `ijl15::CreateHook(...)`：创建对象、会话或业务记录。

## `ijl15.h`
- `class ijl15`：领域类型或功能模块，职责由同名文件实现定义。
- `CreateHook(...)`：创建对象、会话或业务记录。

## `resource.h`

## `stdafx.cpp`

## `stdafx.h`

## `syelog.h`
- `SyelogOpen(...)`：通用业务逻辑入口，需结合实现查看细节。
- `Syelog(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SyelogV(...)`：通用业务逻辑入口，需结合实现查看细节。
- `SyelogClose(...)`：通用业务逻辑入口，需结合实现查看细节。

## `targetver.h`
