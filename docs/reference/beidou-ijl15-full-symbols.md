# BeiDou-ijl15 全量符号索引

> 自动生成：`scripts/generate-full-symbol-docs.py`
> 源码路径：`/tmp/BeiDou-ijl15`
> C/C++ 文件数：48

---

## `AddyLocations.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `AutoTypes.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 13
```text
void(...)
void(...)
void(...)
void(...)
void(...)
void(...)
void(...)
void(...)
_bstr_ctor(...)
HRESULT(...)
_IWzFileSystem__Init(...)
HRESULT(...)
_IWzNameSpace__Mount(...)
```

## `BossHP.cpp`
- class 数: 0
- 类方法定义数: 20
- 顶层函数候选数: 19
```text
BossHP::Hook(...)
BossHP::HookInternal(...)
BossHP::HookUpdate(...)
Memory::SetHook(...)
BossHP::HookShowMobHPTag(...)
BossHP::HookInitField(...)
BossHP::DisposeBossHpNumber(...)
BossHP::DisposeToolTip(...)
BossHP::CreateToolTip(...)
BossHP::HookDisposeField(...)
BossHP::DrawBossHpNumberIfNeed(...)
BossHP::SetToolTip_String(...)
BossHP::DrawBossHpNumber(...)
BossHP::ClearToolTip(...)
BossHP::DisposeBossHpNumber(...)
BossHP::SetToolTip_String(...)
BossHP::ClearToolTip(...)
BossHP::DisposeToolTip(...)
BossHP::CreateToolTip(...)
BossHP::GetMiniMapWidth(...)
void(...)
_UserLocal__Update(...)
DrawBossHpNumberIfNeed(...)
void(...)
_Field__ShowMobHPTag(...)
DrawBossHpNumber(...)
void(...)
if(...)
_Field__Init(...)
void(...)
DisposeBossHpNumber(...)
_Field__Dispose(...)
sprintf_s(...)
void(...)
void(...)
void(...)
void(...)
ReadInt(...)
ReadInt(...)
```

## `BossHP.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 14
```text
class BossHP
Hook(...)
HookInternal(...)
HookUpdate(...)
HookShowMobHPTag(...)
HookDisposeField(...)
HookInitField(...)
SetToolTip_String(...)
ClearToolTip(...)
DisposeToolTip(...)
CreateToolTip(...)
DrawBossHpNumberIfNeed(...)
DrawBossHpNumber(...)
DisposeBossHpNumber(...)
GetMiniMapWidth(...)
```

## `Client.cpp`
- class 数: 0
- 类方法定义数: 100
- 顶层函数候选数: 6
```text
Client::UpdateGameStartup(...)
Memory::FillBytes(...)
Memory::FillBytes(...)
Memory::WriteInt(...)
Memory::WriteDouble(...)
Memory::WriteInt(...)
Client::UpdateResolution(...)
Memory::CodeCave(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteByteArray(...)
Memory::FillBytes(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteByte(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::WriteInt(...)
Memory::CodeCave(...)
Client::EnableNewIGCipher(...)
Client::UpdateLogin(...)
Client::FixMouseWheel(...)
Client::Chinese(...)
FixIme::HookOld(...)
FixIme::HookNew(...)
FixBuddy::Hook(...)
Memory::WriteString(...)
Memory::WriteByte(...)
Memory::WriteByte(...)
Memory::WriteByte(...)
Memory::WriteByte(...)
Memory::WriteByte(...)
Client::LongQuickSlot(...)
Client::FixDateFormat(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Client::FixItemType(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Client::JumpCap(...)
Memory::WriteInt(...)
Memory::CodeCave(...)
Memory::WriteDouble(...)
Client::FixChatPosHook(...)
Client::NoPassword(...)
Memory::WriteInt(...)
Client::MoreHook(...)
Memory::WriteByte(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::CodeCave(...)
Client::WorldMap(...)
if(...)
if(...)
if(...)
if(...)
if(...)
if(...)
```

## `Client.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 14
```text
class Client
UpdateGameStartup(...)
EnableNewIGCipher(...)
UpdateResolution(...)
UpdateLogin(...)
FixMouseWheel(...)
Chinese(...)
LongQuickSlot(...)
FixDateFormat(...)
FixItemType(...)
JumpCap(...)
FixChatPosHook(...)
NoPassword(...)
MoreHook(...)
WorldMap(...)
```

## `FixBuddy.h`
- class 数: 1
- 类方法定义数: 1
- 顶层函数候选数: 2
```text
class FixBuddy
Memory::CodeCave(...)
fixBuddyAccept(...)
Hook(...)
```

## `FixIme.h`
- class 数: 1
- 类方法定义数: 14
- 顶层函数候选数: 19
```text
class FixIme
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::FillBytes(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::CodeCave(...)
Memory::FillBytes(...)
Memory::FillBytes(...)
Memory::FillBytes(...)
Memory::FillBytes(...)
Memory::WriteByte(...)
Memory::FillBytes(...)
EnableIme(...)
if(...)
ImmAssociateContext(...)
ImmReleaseContext(...)
DisableIme(...)
if(...)
ImmAssociateContext(...)
ImmReleaseContext(...)
setOnFocusFirstJudgement(...)
switchIme(...)
switchMLIme(...)
newSwitchIme(...)
destroyWindow(...)
newSwitchMLIme(...)
HookOld(...)
GeneralHook(...)
HookNew(...)
GeneralHook(...)
GeneralHook(...)
```

## `HpMpAlert.cpp`
- class 数: 0
- 类方法定义数: 4
- 顶层函数候选数: 25
```text
Memory::WriteInt(...)
Memory::WriteInt(...)
Memory::SetHook(...)
Memory::SetHook(...)
TryReadDword(...)
ClampAlert(...)
if(...)
if(...)
SendHpMpAlertFromStatusBar(...)
if(...)
if(...)
if(...)
if(...)
g_SendPacket(...)
ApplyHpMpAlertToStatusBar(...)
if(...)
HandleHpMpAlertPacket(...)
if(...)
if(...)
if(...)
ApplyHpMpAlertToStatusBar(...)
SaveGlobal_Hook(...)
s_SaveGlobal(...)
SendHpMpAlertFromStatusBar(...)
ProcessPacket_Hook(...)
HandleHpMpAlertPacket(...)
s_ProcessPacket(...)
HookSaveGlobal(...)
HookHpMpAlertRecv(...)
```

## `HpMpAlert.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
HookSaveGlobal(...)
HookHpMpAlertRecv(...)
```

## `INIReader.h`
- class 数: 1
- 类方法定义数: 13
- 顶层函数候选数: 62
```text
class INIReader
INIReader::INIReader(...)
INIReader::INIReader(...)
INIReader::ParseError(...)
INIReader::Sections(...)
INIReader::Get(...)
INIReader::GetInteger(...)
INIReader::GetReal(...)
INIReader::GetFloat(...)
INIReader::GetBoolean(...)
std::transform(...)
INIReader::MakeKey(...)
std::transform(...)
INIReader::ValueHandler(...)
license(...)
int(...)
value(...)
error(...)
error(...)
ini_parse(...)
ini_parse_file(...)
ini_parse_stream(...)
license(...)
rstrip(...)
while(...)
lskip(...)
while(...)
return(...)
find_chars_or_comment(...)
while(...)
while(...)
return(...)
strncpy0(...)
strncpy_s(...)
ini_parse_stream(...)
if(...)
while(...)
if(...)
if(...)
if(...)
if(...)
rstrip(...)
if(...)
if(...)
if(...)
strncpy0(...)
if(...)
if(...)
if(...)
if(...)
rstrip(...)
strncpy0(...)
if(...)
if(...)
if(...)
free(...)
ini_parse_file(...)
ini_parse_stream(...)
ini_parse(...)
if(...)
fclose(...)
INIReader(...)
INIReader(...)
INIReader(...)
ParseError(...)
Sections(...)
Get(...)
GetInteger(...)
GetReal(...)
GetFloat(...)
GetBoolean(...)
MakeKey(...)
ValueHandler(...)
if(...)
if(...)
if(...)
```

## `MapleClientCollectionTypes/TSecType.h`
- class 数: 3
- 类方法定义数: 0
- 顶层函数候选数: 20
```text
class TSecData
class TSecType
class SECPOINT
TSecType(...)
TSecType(...)
if(...)
T(...)
GetData(...)
for(...)
if(...)
if(...)
if(...)
if(...)
SetData(...)
for(...)
if(...)
if(...)
if(...)
SECPOINT(...)
SECPOINT(...)
SECPOINT(...)
SECPOINT(...)
tagPOINT(...)
```

## `MapleClientCollectionTypes/ZAllocAnonSelector.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
GetBlockSize(...)
switch(...)
```

## `MapleClientCollectionTypes/ZAllocBase.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
class ZAllocBase
AllocRawBlocks(...)
for(...)
```

## `MapleClientCollectionTypes/ZAllocEx.cpp`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
new(...)
delete(...)
```

## `MapleClientCollectionTypes/ZAllocEx.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 52
```text
GetMutex(...)
ZAllocEx(...)
for(...)
new(...)
malloc(...)
delete(...)
free(...)
GetInstance(...)
Alloc(...)
if(...)
if(...)
if(...)
if(...)
GetMutex(...)
if(...)
GetMutex(...)
Free(...)
if(...)
if(...)
if(...)
if(...)
if(...)
if(...)
GetMutex(...)
GetMutex(...)
GetMutex(...)
ZAllocEx(...)
for(...)
new(...)
malloc(...)
delete(...)
free(...)
GetInstance(...)
Alloc(...)
if(...)
if(...)
if(...)
if(...)
GetMutex(...)
if(...)
GetMutex(...)
Free(...)
if(...)
if(...)
if(...)
if(...)
if(...)
if(...)
GetMutex(...)
GetMutex(...)
new(...)
delete(...)
```

## `MapleClientCollectionTypes/ZAllocStrSelector.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 6
```text
GetBlockSize(...)
switch(...)
return(...)
return(...)
return(...)
return(...)
```

## `MapleClientCollectionTypes/ZArray.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 54
```text
class ZArray
ZArray(...)
if(...)
if(...)
if(...)
for(...)
GetAt(...)
IsEmpty(...)
Insert(...)
InsertBefore(...)
if(...)
if(...)
if(...)
if(...)
if(...)
memmove(...)
MakeSpace(...)
if(...)
if(...)
while(...)
RemoveAt(...)
RemoveAt(...)
memmove(...)
GetCount(...)
if(...)
IndexOf(...)
GetNext(...)
GetPrev(...)
if(...)
GetHeadPosition(...)
if(...)
GetTailPosition(...)
RemoveAll(...)
if(...)
Construct(...)
for(...)
Destroy(...)
for(...)
Alloc(...)
if(...)
Realloc(...)
if(...)
if(...)
if(...)
if(...)
if(...)
if(...)
memcpy(...)
if(...)
Reserve(...)
if(...)
if(...)
if(...)
if(...)
memcpy(...)
```

## `MapleClientCollectionTypes/ZFatalSection.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `MapleClientCollectionTypes/ZList.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 48
```text
class ZList
ZList(...)
ZList(...)
GetHeadPosition(...)
GetTailPosition(...)
GetCount(...)
AddTail(...)
if(...)
AddTail(...)
AddTail(...)
while(...)
RemoveAll(...)
while(...)
RemoveAt(...)
if(...)
if(...)
if(...)
FindIndex(...)
if(...)
if(...)
for(...)
if(...)
if(...)
for(...)
if(...)
if(...)
IndexOf(...)
if(...)
while(...)
if(...)
if(...)
if(...)
Find(...)
if(...)
if(...)
if(...)
while(...)
if(...)
if(...)
Insert(...)
InsertBefore(...)
GetNext(...)
if(...)
if(...)
GetPrev(...)
if(...)
if(...)
CastNode(...)
New(...)
```

## `MapleClientCollectionTypes/ZMap.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 22
```text
class ZMap
_PAIR(...)
ZMap(...)
ZMap(...)
GetHeadPosition(...)
if(...)
if(...)
while(...)
if(...)
GetPos(...)
GetAt(...)
if(...)
if(...)
while(...)
if(...)
GetNext(...)
Insert(...)
RemoveAll(...)
RemoveKey(...)
ResizeHashTable(...)
CalcAutoGrow(...)
if(...)
if(...)
```

## `MapleClientCollectionTypes/ZRecyclable.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
class ZRecyclable
new(...)
delete(...)
```

## `MapleClientCollectionTypes/ZRecyclableAvBuffer.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 7
```text
class ZRecyclableAvBuffer
ZRecyclableAvBuffer(...)
ZeroMemory(...)
GetMutex(...)
GetInstance(...)
raw_new(...)
if(...)
raw_delete(...)
```

## `MapleClientCollectionTypes/ZRecyclableStatic.h`
- class 数: 2
- 类方法定义数: 0
- 顶层函数候选数: 1
```text
class ZFakeStatAvBuff
class ZRecyclableStatic
CallBack(...)
```

## `MapleClientCollectionTypes/ZRef.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 21
```text
class ZRef
ZRef(...)
ZRef(...)
if(...)
if(...)
InterlockedIncrement(...)
ZRef(...)
if(...)
InterlockedIncrement(...)
Alloc(...)
if(...)
if(...)
InterlockedIncrement(...)
if(...)
InterlockedIncrement(...)
ReleaseRaw(...)
if(...)
if(...)
InterlockedIncrement(...)
GetBase(...)
if(...)
static_assert(...)
```

## `MapleClientCollectionTypes/ZRefCounted.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
class ZRefCounted
ZRefCounted(...)
ZRefCounted_Alloc(...)
```

## `MapleClientCollectionTypes/ZRefCountedAccessor.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 0
```text
class ZRefCountedAccessor
```

## `MapleClientCollectionTypes/ZRefCountedDummy.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
class ZRefCountedDummy
new(...)
delete(...)
```

## `MapleClientCollectionTypes/ZXString.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 64
```text
class ZXString
if(...)
Length(...)
Empty(...)
if(...)
IsEmpty(...)
Assign(...)
if(...)
if(...)
if(...)
InterlockedIncrement(...)
if(...)
if(...)
Assign(...)
if(...)
if(...)
memcpy(...)
if(...)
Compare(...)
if(...)
if(...)
for(...)
if(...)
Compare(...)
if(...)
Compare(...)
if(...)
CompareNoCase(...)
if(...)
CompareNoCase(...)
if(...)
Concat(...)
if(...)
if(...)
if(...)
memcpy(...)
while(...)
memcpy(...)
Format(...)
va_start(...)
for(...)
if(...)
if(...)
if(...)
va_end(...)
GetData(...)
if(...)
GetBuffer(...)
if(...)
if(...)
if(...)
if(...)
if(...)
memcpy(...)
if(...)
if(...)
ReleaseBuffer(...)
if(...)
Alloc(...)
Release(...)
if(...)
TStrLen(...)
strlen(...)
TStrLen(...)
wcslen(...)
```

## `MapleClientCollectionTypes/ZtlSecure.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 22
```text
class SECRECT
ZtlSecureTear(...)
for(...)
ZtlSecureFuse(...)
for(...)
if(...)
CxxThrowException(...)
SECRECT(...)
SetRect(...)
SECRECT(...)
SetRect(...)
SetRect(...)
SetRectEmpty(...)
IsRectEmpty(...)
if(...)
GetRight(...)
GetLeft(...)
GetTop(...)
GetBottom(...)
PutRight(...)
PutLeft(...)
PutTop(...)
PutBottom(...)
```

## `Memory.cpp`
- class 数: 0
- 类方法定义数: 11
- 顶层函数候选数: 37
```text
Memory::SetHook(...)
Memory::FillBytes(...)
Memory::ReplaceString(...)
Memory::WriteString(...)
Memory::WriteString(...)
Memory::WriteByte(...)
Memory::WriteShort(...)
Memory::WriteInt(...)
Memory::WriteDouble(...)
Memory::WriteByteArray(...)
Memory::CodeCave(...)
if(...)
if(...)
if(...)
if(...)
DetourTransactionAbort(...)
if(...)
VirtualProtect(...)
memset(...)
VirtualProtect(...)
WriteString(...)
FillBytes(...)
WriteString(...)
FillBytes(...)
if(...)
VirtualProtect(...)
memcpy(...)
VirtualProtect(...)
if(...)
VirtualProtect(...)
VirtualProtect(...)
if(...)
VirtualProtect(...)
VirtualProtect(...)
if(...)
VirtualProtect(...)
VirtualProtect(...)
if(...)
VirtualProtect(...)
VirtualProtect(...)
if(...)
for(...)
VirtualProtect(...)
VirtualProtect(...)
for(...)
if(...)
WriteByte(...)
WriteInt(...)
```

## `Memory.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 18
```text
class Memory
SetHook(...)
FillBytes(...)
ReplaceString(...)
WriteString(...)
WriteString(...)
WriteByte(...)
WriteShort(...)
WriteInt(...)
WriteDouble(...)
CodeCave(...)
WriteByteArray(...)
PatchNop(...)
if(...)
if(...)
VirtualProtect(...)
memset(...)
if(...)
VirtualProtect(...)
```

## `NMCO.cpp`
- class 数: 0
- 类方法定义数: 1
- 顶层函数候选数: 4
```text
NMCO::CreateHook(...)
MessageBoxW(...)
NMCO_CallNMFunc(...)
NMCO_CallNMFunc2(...)
NMCO_MemoryFree(...)
```

## `NMCO.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 1
```text
class NMCO
CreateHook(...)
```

## `ReplacementFuncs.h`
- class 数: 0
- 类方法定义数: 13
- 顶层函数候选数: 40
```text
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
Memory::SetHook(...)
HookGetModuleFileName(...)
decltype(...)
decltype(...)
if(...)
HookCreateWindowExA(...)
decltype(...)
create_window_ex_a(...)
GetFuncAddress(...)
if(...)
if(...)
Hook_CreateMutexA(...)
decltype(...)
if(...)
return(...)
_CreateMutexA(...)
HookPcCreateObject_IWzResMan(...)
HookPcCreateObject_IWzNameSpace(...)
HookPcCreateObject_IWzFileSystem(...)
HookCWvsApp__Dir_BackSlashToSlash(...)
HookCWvsApp__Dir_upDir(...)
Hookbstr_ctor(...)
HookIWzFileSystem__Init(...)
HookIWzNameSpace__Mount(...)
HookCWvsApp__InitializeResMan(...)
_CWvsApp__InitializeResMan(...)
Hook_StringPool__GetString(...)
if(...)
switch(...)
if(...)
switch(...)
if(...)
if(...)
if(...)
if(...)
for(...)
if(...)
HookMyTestHook(...)
HookDetectLogin(...)
_lpfn_NextLevel_Hook(...)
Hook_lpfn_NextLevel(...)
```

## `ZAllocEx.cpp`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
new(...)
delete(...)
```

## `codecaves.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 133
```text
AdjustStatusBar(...)
AdjustStatusBarBG(...)
AdjustStatusBarInput(...)
PositionLoginDlg(...)
PositionLoginUsername(...)
PositionLoginPassword(...)
PositionBossBarY(...)
PositionBossBarY1(...)
PositionBossBarY2(...)
CashShopFix(...)
CashShopFix1(...)
CashShopFix2(...)
CashShopFix3(...)
CashShopFix4(...)
CashShopFix5(...)
CashShopFix6(...)
CashShopFix7(...)
CashShopFix8(...)
CashShopFixOnOff(...)
CashShopFixPrev(...)
ITCFix1(...)
ITCFix2(...)
ITCFix3(...)
ITCFix4(...)
ITCFix5(...)
ITCFix6(...)
ITCFix7(...)
ITCFix8(...)
VersionNumberFix(...)
AlwaysViewRestoreFix(...)
ccLoginBackCanvasFix(...)
ccLoginViewRecFix(...)
ccLoginBackBtnFix(...)
ccLoginDescriptorFix(...)
ccMoreGainMsgs(...)
ccMoreGainMsgsFade(...)
ccMoreGainMsgsFade1(...)
ccMuruengraidPlayer(...)
ccMuruengraidClock(...)
ccMuruengraidMonster(...)
ccMuruengraidMonster1(...)
ccMuruengraidMonster2(...)
ccMuruengraidEngBar(...)
ccMuruengraidEngBar1(...)
ccMuruengraidEngBar2(...)
ccMuruengraidClearRoundUI(...)
ccMuruengraidTimerCanvas(...)
ccMuruengraidTimerMinutes(...)
ccMuruengraidTimerSeconds(...)
ccMuruengraidTimerBar(...)
ccMuruengraidMonster1_2(...)
ccStatsSubMov(...)
ccCLoginSendCheckPasswordPacket(...)
cc0x0044E550(...)
cc0x0044E5BE(...)
cc0x0044E5DB(...)
cc0x0044E6AC(...)
cc0x0044E71D(...)
cc0x0044E80C(...)
cc0x0044E8B4(...)
cc0x0044EA22(...)
cc0x0044EA6F(...)
cc0x0044EBD6(...)
cc0x0044ECA1(...)
cc0x0044ED32(...)
cc0x0044ED52(...)
cc0x0044EED3(...)
cc0x00494943(...)
cc0x00494BB6(...)
cc0x00494CA9(...)
cc0x00494CF0(...)
cc0x00494D3B(...)
cc0x00494EAF(...)
cc0x00494EEC(...)
cc0x00494F87(...)
cc0x009F4E84(...)
cc0x009F4EC3(...)
cc0x009F4F12(...)
cc0x009F4FC6(...)
cc0x009F503C(...)
cc0x009F51A7(...)
cc0x009F526F(...)
cc0x009F5653(...)
cc0x009F5833(...)
cc0x009F5C2C(...)
cc0x009F5CA3(...)
cc0x009F5FBD(...)
cc0x009F631C(...)
cc0x009F691F(...)
cc0x009F6F36(...)
cc0x009F6F5C(...)
cc0x009F7CFA(...)
cc0x009F7D83(...)
cc0x009F81FB(...)
cc0x009F84E9(...)
cc0x009F8AD4(...)
cc0x00A4BB39(...)
cc0x00A4BC79(...)
cc0x00A4BD05(...)
cc0x00A4BD4E(...)
cc0x00A4BD99(...)
cc0x00A4BDE3(...)
cc0x00A4BDFE(...)
cc0x00A4BE47(...)
testingCodeCave(...)
testingCodeCave2(...)
testingCodeCave3(...)
testingCodeCave4(...)
fixMouseWheelHook(...)
fixDateFormat(...)
fixDateFormat2(...)
fixDateFormat3(...)
fixDateFormat4(...)
getItemType1(...)
getItemType2(...)
customJumpCapHook1(...)
customJumpCapHook2(...)
customJumpCapHook3(...)
chatTextPos(...)
calcClimbSpeed(...)
calcSpeedHook(...)
faceHairCave(...)
canSendPkgTimeCave(...)
apDetailBtn(...)
darkMap1cc(...)
darkMap2cc(...)
darkMap3cc(...)
wordMapUIcc(...)
calcCharLen(...)
if(...)
if(...)
if(...)
skillToolTipNew(...)
```

## `detours.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 149
```text
sizeof(...)
sizeof(...)
sizeof(...)
BOOL(...)
BOOL(...)
BOOL(...)
BOOL(...)
BOOL(...)
BOOL(...)
BOOL(...)
BOOL(...)
DetourTransactionBegin(...)
DetourTransactionAbort(...)
DetourTransactionCommit(...)
DetourTransactionCommitEx(...)
DetourUpdateThread(...)
DetourAttach(...)
DetourAttachEx(...)
DetourDetach(...)
DetourSetIgnoreTooSmall(...)
DetourSetRetainRegions(...)
DetourSetSystemRegionLowerBound(...)
DetourSetSystemRegionUpperBound(...)
DetourFindFunction(...)
DetourCodeFromPointer(...)
DetourCopyInstruction(...)
DetourSetCodeModule(...)
DetourAllocateRegionWithinJumpBounds(...)
DetourGetContainingModule(...)
DetourEnumerateModules(...)
DetourGetEntryPoint(...)
DetourGetModuleSize(...)
DetourEnumerateExports(...)
DetourEnumerateImports(...)
DetourEnumerateImportsEx(...)
DetourFindPayload(...)
DetourFindPayloadEx(...)
DetourGetSizeOfPayloads(...)
DetourBinaryOpen(...)
DetourBinaryEnumeratePayloads(...)
DetourBinaryFindPayload(...)
DetourBinarySetPayload(...)
_In_reads_opt_(...)
DetourBinaryDeletePayload(...)
DetourBinaryPurgePayloads(...)
DetourBinaryResetImports(...)
DetourBinaryEditImports(...)
DetourBinaryWrite(...)
DetourBinaryClose(...)
BOOL(...)
BOOL(...)
DetourCreateProcessWithDllA(...)
DetourCreateProcessWithDllW(...)
DetourCreateProcessWithDllExA(...)
DetourCreateProcessWithDllExW(...)
DetourCreateProcessWithDllsA(...)
_In_reads_(...)
DetourCreateProcessWithDllsW(...)
_In_reads_(...)
DetourProcessViaHelperA(...)
DetourProcessViaHelperW(...)
DetourProcessViaHelperDllsA(...)
_In_reads_(...)
DetourProcessViaHelperDllsW(...)
_In_reads_(...)
DetourUpdateProcessWithDll(...)
_In_reads_(...)
DetourUpdateProcessWithDllEx(...)
_In_reads_(...)
DetourCopyPayloadToProcess(...)
_In_reads_bytes_(...)
DetourRestoreAfterWith(...)
DetourRestoreAfterWithEx(...)
DetourIsHelperProcess(...)
DetourFinishHelperProcess(...)
InterlockedCompareExchange(...)
return(...)
LPAPI_VERSION(...)
BOOL(...)
DWORD(...)
DWORD(...)
DWORD64(...)
BOOL(...)
BOOL(...)
DetourLoadImageHlp(...)
RelocateBundle(...)
RelocateInstruction(...)
GetTemplate(...)
GetInst0(...)
GetInst1(...)
GetInst2(...)
GetUnit(...)
GetUnit0(...)
GetUnit1(...)
GetUnit2(...)
GetData0(...)
GetData1(...)
GetData2(...)
GetInstruction(...)
GetInstruction0(...)
GetInstruction1(...)
GetInstruction2(...)
SetInstruction(...)
SetInstruction0(...)
SetInstruction1(...)
SetInstruction2(...)
GetBits(...)
SetBits(...)
GetOpcode(...)
GetX(...)
GetX3(...)
GetX6(...)
GetImm7a(...)
SetImm7a(...)
GetImm13c(...)
SetImm13c(...)
GetSignBit(...)
SetSignBit(...)
GetImm20a(...)
SetImm20a(...)
GetImm20b(...)
SetImm20b(...)
SignExtend(...)
IsMovlGp(...)
SetInst(...)
SetInst0(...)
SetInst1(...)
SetInst2(...)
SetData(...)
SetData0(...)
SetData1(...)
SetData2(...)
SetNop(...)
SetNop0(...)
SetNop1(...)
SetNop2(...)
IsBrl(...)
SetBrl(...)
SetBrl(...)
GetBrlTarget(...)
SetBrlTarget(...)
SetBrlImm(...)
GetBrlImm(...)
GetMovlGp(...)
SetMovlGp(...)
SetStop(...)
Copy(...)
DetourVirtualProtectSameExecuteEx(...)
DetourVirtualProtectSameExecute(...)
```

## `detver.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `dllmain.cpp`
- class 数: 0
- 类方法定义数: 15
- 顶层函数候选数: 25
```text
std::string(...)
Client::UpdateGameStartup(...)
Client::UpdateResolution(...)
Client::FixMouseWheel(...)
Client::Chinese(...)
Client::LongQuickSlot(...)
Client::FixDateFormat(...)
Client::FixItemType(...)
Client::JumpCap(...)
Client::FixChatPosHook(...)
Client::NoPassword(...)
Client::MoreHook(...)
BossHP::Hook(...)
Client::WorldMap(...)
ijl15::CreateHook(...)
ResolveToIpv4String(...)
WSACleanup(...)
freeaddrinfo(...)
if(...)
CreateConsole(...)
DllMain(...)
reader(...)
if(...)
Hook_CreateMutexA(...)
HookCreateWindowExA(...)
HookGetModuleFileName(...)
HookPcCreateObject_IWzResMan(...)
HookPcCreateObject_IWzNameSpace(...)
HookPcCreateObject_IWzFileSystem(...)
HookCWvsApp__Dir_BackSlashToSlash(...)
HookCWvsApp__Dir_upDir(...)
Hookbstr_ctor(...)
HookIWzFileSystem__Init(...)
HookIWzNameSpace__Mount(...)
HookCWvsApp__InitializeResMan(...)
Hook_StringPool__GetString(...)
Hook_lpfn_NextLevel(...)
HookSaveGlobal(...)
HookHpMpAlertRecv(...)
ExitProcess(...)
```

## `dllmain.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 2
```text
CreateConsole(...)
CreateHook(...)
```

## `ijl15.cpp`
- class 数: 0
- 类方法定义数: 1
- 顶层函数候选数: 7
```text
ijl15::CreateHook(...)
MessageBoxW(...)
ijlGetLibVersion(...)
ijlInit(...)
ijlFree(...)
ijlRead(...)
ijlWrite(...)
ijlErrorStr(...)
```

## `ijl15.h`
- class 数: 1
- 类方法定义数: 0
- 顶层函数候选数: 1
```text
class ijl15
CreateHook(...)
```

## `resource.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `stdafx.cpp`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `stdafx.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0

## `syelog.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 4
```text
SyelogOpen(...)
Syelog(...)
SyelogV(...)
SyelogClose(...)
```

## `targetver.h`
- class 数: 0
- 类方法定义数: 0
- 顶层函数候选数: 0
