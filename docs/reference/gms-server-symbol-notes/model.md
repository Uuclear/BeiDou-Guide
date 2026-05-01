# gms-server 逐符号中文职责 · 分卷 `model`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：45

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `model/dto/AddAccountDTO.java`

- `class AddAccountDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/AutobanConfigDTO.java`

- `class AutobanConfigDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/BasePageDTO.java`

- `class BasePageDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/CashShopBatchOnSaleReqDTO.java`

- `class CashShopBatchOnSaleReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/CashShopSearchRtnDTO.java`

- `class CashShopSearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ChannelListRtnDTO.java`

- `class ChannelListRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ChrOnlineListReqDTO.java`

- `class ChrOnlineListReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ChrOnlineListRtnDTO.java`

- `class ChrOnlineListRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/CommandReqDTO.java`

- `class CommandReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ConfigTypeDTO.java`

- `class ConfigTypeDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/DropSearchReqDTO.java`

- `class DropSearchReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/DropSearchRtnDTO.java`

- `class DropSearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/EquipmentInfoReqDTO.java`

- `class EquipmentInfoReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/EquipmentInfoRtnDTO.java`

- `class EquipmentInfoRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/FileReadDTO.java`

- `class FileReadDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/FileTreeDTO.java`

- `class FileTreeDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/FileTreeNodeDTO.java`

- `class FileTreeNodeDTO`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FileTreeNodeDTO(File file, String key)`：通用业务逻辑入口，需结合实现查看细节。

## `model/dto/FileWriteDTO.java`

- `class FileWriteDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/GachaponPoolSearchReqDTO.java`

- `class GachaponPoolSearchReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/GachaponPoolSearchRtnDTO.java`

- `class GachaponPoolSearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/GameConfigReqDTO.java`

- `class GameConfigReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/GiveResourceReqDTO.java`

- `class GiveResourceReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/InventoryEquipRtnDTO.java`

- `class InventoryEquipRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/InventorySearchReqDTO.java`

- `class InventorySearchReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/InventorySearchRtnDTO.java`

- `class InventorySearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Item toItem()`：通用业务逻辑入口，需结合实现查看细节。

## `model/dto/InventoryTypeRtnDTO.java`

- `class InventoryTypeRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/InventoryequipmentReqDTO.java`

- `class InventoryequipmentReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/InventoryequipmentRtnDTO.java`

- `class InventoryequipmentRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ResultBody.java`

- `class ResultBody`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ResultBody()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody(BaseErrorInfoInterface errorInfo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> success()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> success(T data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> success(SubmitBody<?> request, T data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> error(HttpServletRequest req, BaseErrorInfoInterface errorInfo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> error(HttpServletRequest req, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> ResultBody<T> error(HttpServletRequest req, Integer code, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。

## `model/dto/ServerInfoReqDto.java`

- `class ServerInfoReqDto`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ServerShutdownDTO.java`

- `class ServerShutdownDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ShopItemSearchRtnDTO.java`

- `class ShopItemSearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ShopSearchReqDTO.java`

- `class ShopSearchReqDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/ShopSearchRtnDTO.java`

- `class ShopSearchRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/SubmitBody.java`

- `class SubmitBody`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/UpdateAccountByGmDTO.java`

- `class UpdateAccountByGmDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/UpdateAccountByUserDTO.java`

- `class UpdateAccountByUserDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/dto/WorldListRtnDTO.java`

- `class WorldListRtnDTO`：领域类型或功能模块，职责由同名文件实现定义。

## `model/pojo/CashCategory.java`

- `class CashCategory`：领域类型或功能模块，职责由同名文件实现定义。

## `model/pojo/InformationResult.java`

- `class InformationResult`：领域类型或功能模块，职责由同名文件实现定义。

## `model/pojo/InformationSearch.java`

- `class InformationSearch`：领域类型或功能模块，职责由同名文件实现定义。

## `model/pojo/NewYearCardRecord.java`

- `class NewYearCardRecord`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NewYearCardRecord(int senderId, String senderName, int receiverId, String receiverName, String message)`：创建对象、会话或业务记录。
  - `public void setExtraNewYearCardRecord(int id, boolean senderDiscardCard, boolean receiverDiscardCard, boolean receiverReceivedCard, long dateSent, long dateReceived)`：写入或更新状态字段。
  - `public static void saveNewYearCard(NewYearCardRecord newyear)`：持久化当前状态到存储层。
  - `public static void updateNewYearCard(NewYearCardRecord newyear)`：更新已有对象/配置/缓存。
  - `public static NewYearCardRecord loadNewYearCard(int cardid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static void loadPlayerNewYearCards(Character chr)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static void printNewYearRecords(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startNewYearCardTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stopNewYearCardTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void deleteNewYearCard(int id)`：删除对象、关系或临时状态。
  - `public static void removeAllNewYearCard(boolean send, Character chr)`：删除对象、关系或临时状态。

## `model/pojo/NextLevelContext.java`

- `class NextLevelContext`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void clear()`：通用业务逻辑入口，需结合实现查看细节。

## `model/pojo/RateLimitContext.java`

- `class RateLimitContext`：领域类型或功能模块，职责由同名文件实现定义。

## `model/pojo/SkillEntry.java`

- `class SkillEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SkillEntry(byte skillLevel, int masterLevel, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
