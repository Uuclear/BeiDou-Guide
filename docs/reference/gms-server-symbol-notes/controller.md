# gms-server 逐符号中文职责 · 分卷 `controller`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：15

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `controller/AccountController.java`

- `class AccountController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public AccountController(AccountService accountService)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<AccountsDO> info()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Page<AccountsDO>> getAccountList(@RequestParam(name = "page", required = false) Integer page, @RequestParam(name = "size", required = false) Integer size, @RequestParam(name = "id", required = false) Integer id, @RequestParam(name = "name", required = false) String name, @RequestParam(name = "lastLoginStart", required = false) String lastLoginStart, @RequestParam(name = "lastLoginEnd", required = false) String lastLoginEnd, @RequestParam(name = "createdAtStart", required = false) String createdAtStart, @RequestParam(name = "createdAtEnd", required = false) String createdAtEnd)`：读取并返回状态/数据。

## `controller/AuthController.java`

- `class AuthController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public AuthController(AuthService authService)`：处理认证/会话生命周期。
  - `public ResultBody<Object> logout()`：处理认证/会话生命周期。

## `controller/AutobanConfigController.java`

- `class AutobanConfigController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<List<AutobanConfigDTO>> getConfigList()`：读取并返回状态/数据。
  - `public ResultBody<Object> updateConfig(@RequestBody SubmitBody<AutobanConfigDTO> request)`：更新已有对象/配置/缓存。

## `controller/CashShopController.java`

- `class CashShopController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<List<CashCategory>> getAllCategoryList()`：读取并返回状态/数据。
  - `public ResultBody<Page<CashShopSearchRtnDTO>> getCommodityByCategory(@RequestBody SubmitBody<CashCategory> request)`：读取并返回状态/数据。
  - `public ResultBody<CashShopSearchRtnDTO> getCommodityBySn(@PathVariable("sn") Integer sn)`：读取并返回状态/数据。
  - `public ResultBody<Object> onSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> offSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> batchOnSale(@RequestBody SubmitBody<CashShopBatchOnSaleReqDTO> request)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/CharacterController.java`

- `class CharacterController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Object> updateRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> resetRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> resetRates(@RequestBody SubmitBody<ExtendValueDO> submitBody)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Page<ChrOnlineListRtnDTO>> onlineList(@RequestBody SubmitBody<ChrOnlineListReqDTO> submitBody)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/CommandController.java`

- `class CommandController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Page<CommandReqDTO>> getCommandListFromDB(@RequestBody SubmitBody<CommandReqDTO> submitBody)`：读取并返回状态/数据。
  - `public ResultBody<CommandInfoDO> updateCommand(@RequestBody SubmitBody<CommandReqDTO> submitBody)`：更新已有对象/配置/缓存。
  - `public ResultBody reloadEventsByGMCommand()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody reloadPortalsByGMCommand()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody reloadMapsByGMCommand()`：通用业务逻辑入口，需结合实现查看细节。

## `controller/CommonController.java`

- `class CommonController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Object> getEquipmentInfoByItemId(@RequestBody SubmitBody<EquipmentInfoReqDTO> submitBody)`：读取并返回状态/数据。
  - `public ResultBody<Integer> getAllWorldsOnlinePlayersCount(@RequestBody SubmitBody<ServerInfoReqDto> submitBody)`：读取并返回状态/数据。
  - `public ResultBody<List<InformationResult>> informationSearch(@RequestBody SubmitBody<InformationSearch> submitBody)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/ConfigController.java`

- `class ConfigController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<ConfigTypeDTO> getConfigTypeList()`：读取并返回状态/数据。
  - `public ResultBody<Page<GameConfigDO>> getConfigList(@RequestBody SubmitBody<GameConfigReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Object> addConfig(@RequestBody SubmitBody<GameConfigDO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> updateConfig(@RequestBody SubmitBody<GameConfigDO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deleteConfig(@PathVariable("id") Long id)`：删除对象、关系或临时状态。
  - `public ResultBody<Object> deleteConfigList(@RequestBody SubmitBody<List<Long>> request)`：删除对象、关系或临时状态。
  - `public ResultBody<Object> importYml(@RequestParam("file") MultipartFile file)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResponseEntity<Resource> exportYml()`：通用业务逻辑入口，需结合实现查看细节。

## `controller/DropController.java`

- `class DropController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Page<DropSearchRtnDTO>> getDropList(@RequestBody SubmitBody<DropSearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Page<DropSearchRtnDTO>> getGlobalDropList(@RequestBody SubmitBody<DropSearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Long> addDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Long> addGlobalDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> updateDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> updateGlobalDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deleteDropData(@PathVariable("id") Long id)`：删除对象、关系或临时状态。
  - `public ResultBody<Object> deleteGlobalDropData(@PathVariable("id") Long id)`：删除对象、关系或临时状态。

## `controller/FileController.java`

- `class FileController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<String> treeRead(@RequestBody SubmitBody<FileReadDTO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<String> treeWrite(@RequestBody SubmitBody<FileWriteDTO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<List<FileTreeNodeDTO>> tree(@RequestBody SubmitBody<FileTreeDTO> request)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/GachaponController.java`

- `class GachaponController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Page<GachaponPoolSearchRtnDTO>> getPools(@RequestBody SubmitBody<GachaponPoolSearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Object> updatePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deletePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)`：删除对象、关系或临时状态。
  - `public ResultBody<List<GachaponRewardDO>> getRewards(@RequestBody SubmitBody<GachaponRewardPoolDO> request)`：读取并返回状态/数据。
  - `public ResultBody<Object> updateReward(@RequestBody SubmitBody<GachaponRewardDO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deleteReward(@RequestBody SubmitBody<GachaponRewardDO> request)`：删除对象、关系或临时状态。

## `controller/GiveController.java`

- `class GiveController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Object> giveResource(@RequestBody SubmitBody<GiveResourceReqDTO> submitBody)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/InventoryController.java`

- `class InventoryController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<List<InventoryTypeRtnDTO>> getInventoryTypeList()`：读取并返回状态/数据。
  - `public ResultBody<Page<InventorySearchReqDTO>> getCharacterList(@RequestBody SubmitBody<InventorySearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<List<InventorySearchRtnDTO>> getInventoryList(@RequestBody SubmitBody<InventorySearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Object> updateInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deleteInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)`：删除对象、关系或临时状态。

## `controller/ServerController.java`

- `class ServerController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public void shutdown()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> stopServer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> stopServerWithMsgAndInternal( @Parameter( name = "stopConfigData", in = ParameterIn.DEFAULT, required = true, description = "停服请求参数：包含停服自定义消息，停服倒计时(单位：分钟)" ) @RequestBody SubmitBody<ServerShutdownDTO> request)`：通用业务逻辑入口，需结合实现查看细节。

## `controller/ShopController.java`

- `class ShopController`：HTTP 接口层，负责参数接收、鉴权边界与调用 service。
  - `public ResultBody<Page<ShopSearchRtnDTO>> getShopList(@RequestBody SubmitBody<ShopSearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<Page<ShopItemSearchRtnDTO>> getShopItemList(@RequestBody SubmitBody<ShopSearchReqDTO> request)`：读取并返回状态/数据。
  - `public ResultBody<ShopItemSearchRtnDTO> getShopItem(@PathVariable("id") Long id)`：读取并返回状态/数据。
  - `public ResultBody<Long> addShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResultBody<Object> updateShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)`：更新已有对象/配置/缓存。
  - `public ResultBody<Object> deleteShopItem(@PathVariable("id") Long id)`：删除对象、关系或临时状态。
