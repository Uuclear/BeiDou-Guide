# gms-server 逐符号中文职责 · 分卷 `service`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：31

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `service/AccountService.java`

- `class AccountService`：业务编排层，组织领域逻辑与持久化调用。
  - `public AccountsDO findByName(String name)`：查询并返回匹配集合或单项结果。
  - `public AccountsDO findById(int id)`：查询并返回匹配集合或单项结果。
  - `public AccountsDO getCurrentUser()`：读取并返回状态/数据。
  - `public Page<AccountsDO> getAccountList(Integer page, Integer size, Integer id, String name, String lastLoginStart, String lastLoginEnd, String createdAtStart, String createdAtEnd)`：读取并返回状态/数据。

## `service/AuthService.java`

- `class AuthService`：业务编排层，组织领域逻辑与持久化调用。

## `service/AutobanConfigService.java`

- `class AutobanConfigService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void loadConfigs()`：从外部来源加载数据（数据库/文件/配置）。
  - `public List<AutobanConfigDTO> getConfigList()`：读取并返回状态/数据。
  - `public void updateConfig(AutobanConfigDTO dto)`：更新已有对象/配置/缓存。

## `service/CashShopService.java`

- `class CashShopService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<ModifiedCashItemDO> loadAllModifiedCashItems()`：从外部来源加载数据（数据库/文件/配置）。
  - `public List<CashCategory> getAllCategoryList()`：读取并返回状态/数据。
  - `public Page<CashShopSearchRtnDTO> getCommodityByCategory(CashCategory data)`：读取并返回状态/数据。
  - `public CashShopSearchRtnDTO getCommodityBySn(Integer sn)`：读取并返回状态/数据。
  - `public void changeOnSale(ModifiedCashItemDO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private CashCategory getCategory(Integer id, Integer subId)`：读取并返回状态/数据。
  - `private CashShopSearchRtnDTO fromCashItem(CashCategory cashCategory, ModifiedCashItemDO cashItem)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void setDbItemValue(CashShopSearchRtnDTO rtnDTO, ModifiedCashItemDO dbCashItem)`：写入或更新状态字段。
  - `public void batchChangeOnSale(CashShopBatchOnSaleReqDTO submit)`：通用业务逻辑入口，需结合实现查看细节。

## `service/CharacterService.java`

- `class CharacterService`：业务编排层，组织领域逻辑与持久化调用。
  - `public CharactersDO findById(int id)`：查询并返回匹配集合或单项结果。
  - `public void update(CharactersDO condition)`：更新已有对象/配置/缓存。
  - `public Page<ChrOnlineListRtnDTO> getChrOnlineList(ChrOnlineListReqDTO request)`：读取并返回状态/数据。
  - `public void updateRate(ExtendValueDO data)`：更新已有对象/配置/缓存。
  - `public void resetRate(ExtendValueDO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetRates(ExtendValueDO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMerchant()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<List<CharactersDO>> getWorldsRankPlayers(int worldSize)`：读取并返回状态/数据。
  - `public List<CharactersDO> getWorldRankPlayers(int worldId)`：读取并返回状态/数据。
  - `public CharactersDO findByName(String name)`：查询并返回匹配集合或单项结果。
  - `public void removeSkill(SkillsDO skillsDO)`：删除对象、关系或临时状态。
  - `public void deleteGuild(GuildsDO guildsDO)`：删除对象、关系或临时状态。
  - `public void deleteCharFromDB(Character player, int senderAccId)`：删除对象、关系或临时状态。
  - `public void saveCharToDB(Character player, boolean notAutosave)`：持久化当前状态到存储层。
  - `public Character loadCharFromDB(int cid, Client client, boolean channelServer)`：从外部来源加载数据（数据库/文件/配置）。
  - `public List<TrocklocationsDO> getTrockLocationByCharacter(Integer cid)`：读取并返回状态/数据。
  - `public List<AreaInfoDO> getAreaInfoByCharacter(Integer cid)`：读取并返回状态/数据。
  - `public List<EventstatsDO> getEventStatsByCharacter(Integer cid)`：读取并返回状态/数据。
  - `public List<WishlistsDO> getWishlistsByCharacter(Integer cid)`：读取并返回状态/数据。
  - `public List<CharactersDO> getCharacterByAccountId(int accountId)`：读取并返回状态/数据。
  - `private void checkName(ExtendValueDO data)`：校验输入参数或业务约束。
  - `private void check(ExtendValueDO data)`：校验输入参数或业务约束。
  - `private Character getCharacter(ExtendValueDO data)`：读取并返回状态/数据。

## `service/CommandService.java`

- `class CommandService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void loadCommands(final HashMap<String, Command> registeredCommands, final List<Pair<List<String>, List<String>>> commandsNameDesc)`：从外部来源加载数据（数据库/文件/配置）。
  - `updateRegisteredCommands(commandInfoDO)`：更新已有对象/配置/缓存。

## `service/CommonService.java`

- `class CommonService`：业务编排层，组织领域逻辑与持久化调用。
  - `public EquipmentInfoRtnDTO getEquipmentInfoByItemId(EquipmentInfoReqDTO submitData)`：读取并返回状态/数据。
  - `public Integer getOnlinePlayerCountByWorldId(Integer worldId)`：读取并返回状态/数据。
  - `public Integer getAllWorldsOnlinePlayersCount(List<Integer> worldIdList)`：读取并返回状态/数据。
  - `public List<InformationResult> getInformation(InformationSearch condition)`：读取并返回状态/数据。

## `service/ConfigService.java`

- `class ConfigService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<GameConfigDO> loadGameConfigs()`：从外部来源加载数据（数据库/文件/配置）。
  - `public ConfigTypeDTO getConfigTypeList()`：读取并返回状态/数据。
  - `public Page<GameConfigDO> getConfigList(GameConfigReqDTO condition)`：读取并返回状态/数据。
  - `public void addConfig(GameConfigDO condition)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateConfig(GameConfigDO condition)`：更新已有对象/配置/缓存。
  - `public void deleteConfig(Long id)`：删除对象、关系或临时状态。
  - `public void deleteConfigList(List<Long> ids)`：删除对象、关系或临时状态。
  - `public int importYml(MultipartFile file)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Object parseObject(Object obj)`：解析输入文本或二进制内容。
  - `private String replaceWithEquals(String src, String[]... fts)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String replaceWithContains(String src, String[]... fts)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ResponseEntity<Resource> exportYml()`：通用业务逻辑入口，需结合实现查看细节。

## `service/DropService.java`

- `class DropService`：业务编排层，组织领域逻辑与持久化调用。
  - `public Page<DropSearchRtnDTO> getDropList(DropSearchReqDTO data, boolean isGlobal)`：读取并返回状态/数据。
  - `public Long modifyDropData(DropSearchRtnDTO data, boolean isGlobal, boolean isDelete)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String getItemName(Integer itemId)`：读取并返回状态/数据。
  - `private String getMobName(Integer mobId)`：读取并返回状态/数据。
  - `private String getQuestName(Integer questId)`：读取并返回状态/数据。

## `service/FamilyService.java`

- `class FamilyService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void loadAllFamilies()`：从外部来源加载数据（数据库/文件/配置）。

## `service/FileTreeService.java`

- `class FileTreeService`：业务编排层，组织领域逻辑与持久化调用。
  - `public String readFile(String currentKey, String filename)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeFile(String currentKey, String filename, String content)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<FileTreeNodeDTO> tree(String currentKey)`：通用业务逻辑入口，需结合实现查看细节。
  - `public File resolveByTreeKey(String currentKey)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean matchAnyLimitPattern(Path path)`：通用业务逻辑入口，需结合实现查看细节。

## `service/GachaponService.java`

- `class GachaponService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void updatePool(GachaponRewardPoolDO submit)`：更新已有对象/配置/缓存。
  - `public void deletePool(Integer id)`：删除对象、关系或临时状态。
  - `public Page<GachaponPoolSearchRtnDTO> getPools(GachaponPoolSearchReqDTO condition)`：读取并返回状态/数据。
  - `public List<GachaponRewardDO> getRewards(Integer poolId)`：读取并返回状态/数据。
  - `public void updateReward(GachaponRewardDO reward)`：更新已有对象/配置/缓存。
  - `public void deleteReward(Integer id)`：删除对象、关系或临时状态。
  - `private void setRealProb(List<GachaponPoolSearchRtnDTO> pools)`：写入或更新状态字段。
  - `private List<GachaponRewardPoolDO> getActivePools(Integer gachaponId)`：读取并返回状态/数据。
  - `public void doGachapon(Character player, int gachaponId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<GachaponRewardDO> getRewardsByNpcId(Integer npcId)`：读取并返回状态/数据。
  - `private void doReward(Character player, GachaponRewardPoolDO pool)`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<GachaponRewardDO> getPoolRewards(Integer poolId)`：读取并返回状态/数据。

## `service/GiveService.java`

- `class GiveService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void give(GiveResourceReqDTO submitData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveAllOnlineChr(GiveResourceReqDTO submitData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveChr(GiveResourceReqDTO submitData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveNxAllOnlineChr(int quantity, int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveNxChr(Character chr, int quantity, int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String getCashTypeName(int type)`：读取并返回状态/数据。
  - `private void giveMesosAllOnlineChr(int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveMesosChr(Character chr, int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveExpAllOnlineChr(int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveExpChr(Character chr, int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveItemAllOnlineChr(int itemId, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveItemChr(Character chr, int itemId, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveEquipAllOnlineChr(GiveResourceReqDTO submitData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveEquipChr(Character chr, GiveResourceReqDTO submitData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveRateChr(Character chr, String type, float rate)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveGMChr(Character chr, Integer level)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveFameChr(Character chr, Integer fame)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void changeMap(Character chr, Integer mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void doGainCash(Character chr, int type, int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void doGainExp(Character chr, int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void doGainMeso(Character chr, int quantity)`：通用业务逻辑入口，需结合实现查看细节。

## `service/HpMpAlertService.java`

- `class HpMpAlertService`：业务编排层，组织领域逻辑与持久化调用。
  - `private static byte normalizeAlertStep(byte step)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte getHpAlert(int characterId)`：读取并返回状态/数据。
  - `public void setHpAlert(int characterId, byte alert)`：写入或更新状态字段。
  - `public float getHpAlertPer(int characterId)`：读取并返回状态/数据。
  - `public byte getMpAlert(int characterId)`：读取并返回状态/数据。
  - `public void setMpAlert(int characterId, byte alert)`：写入或更新状态字段。
  - `public float getMpAlertPer(int characterId)`：读取并返回状态/数据。
  - `public void saveAll()`：持久化当前状态到存储层。
  - `public void clear()`：通用业务逻辑入口，需结合实现查看细节。

## `service/InventoryService.java`

- `class InventoryService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<InventoryTypeRtnDTO> getInventoryTypeList()`：读取并返回状态/数据。
  - `public Page<InventorySearchReqDTO> getCharacterList(InventorySearchReqDTO data)`：读取并返回状态/数据。
  - `public List<InventorySearchRtnDTO> getInventoryList(InventorySearchReqDTO data)`：读取并返回状态/数据。
  - `public void deleteInventoryByCharacterId(int cid)`：删除对象、关系或临时状态。
  - `private Character getCharacterById(int characterId)`：读取并返回状态/数据。
  - `private InventorySearchRtnDTO buildByDb(Row obj)`：构建输出对象、包体或配置。
  - `private List<InventorySearchRtnDTO> buildByOnline(Character character, InventoryType type)`：构建输出对象、包体或配置。
  - `public void updateInventory(InventorySearchRtnDTO data)`：更新已有对象/配置/缓存。
  - `private void updateOnline(InventorySearchRtnDTO data, Character character)`：更新已有对象/配置/缓存。
  - `private void updateDb(InventorySearchRtnDTO data)`：更新已有对象/配置/缓存。
  - `public void deleteInventory(InventorySearchRtnDTO data)`：删除对象、关系或临时状态。
  - `public List<PetignoresDO> getPetIgnoreByPetId(Integer petId)`：读取并返回状态/数据。
  - `private void modifyInventoryCheck(InventorySearchRtnDTO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Item getModifyItemOnline(InventorySearchRtnDTO data, Inventory inventory)`：读取并返回状态/数据。
  - `private InventoryitemsDO getModifyItemOffline(InventorySearchRtnDTO data)`：读取并返回状态/数据。

## `service/ItemService.java`

- `class ItemService`：业务编排层，组织领域逻辑与持久化调用。
  - `public Equip getEquipmentInfoByItemId(Integer itemId)`：读取并返回状态/数据。

## `service/LangResourceService.java`

- `class LangResourceService`：业务编排层，组织领域逻辑与持久化调用。
  - `public String getI18n(LangResourcesDO langResourcesDO)`：读取并返回状态/数据。
  - `public void insertOrUpdateI18n(LangResourcesDO langResourcesDO)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void deleteI18n(LangResourcesDO langResourcesDO)`：删除对象、关系或临时状态。

## `service/MonsterBookService.java`

- `class MonsterBookService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<MonsterbookDO> getByCharacterId(int cid)`：读取并返回状态/数据。

## `service/MtsService.java`

- `class MtsService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void deleteMtsByCharacterId(int cid)`：删除对象、关系或临时状态。

## `service/NameChangeService.java`

- `class NameChangeService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void applyAllNameChange()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void applyNameChange(int characterId, String characterName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<NamechangesDO> getAllNameChanges()`：读取并返回状态/数据。
  - `public void doNameChange(NamechangesDO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean registerNameChange(Character chr, String newName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelPendingNameChange(Character chr, boolean needFinish)`：进行条件判定并返回布尔结果。

## `service/NewYearCardService.java`

- `class NewYearCardService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void startPendingNewYearCardRequests()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<NewyearDO> loadPlayerNewYearCards(Character chr)`：从外部来源加载数据（数据库/文件/配置）。

## `service/NoteService.java`

- `class NoteService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void sendNormal(String message, String senderName, String receiverName)`：向外发送响应、消息或网络包。
  - `public void sendWithFame(String message, String senderName, String receiverName)`：向外发送响应、消息或网络包。
  - `public void show(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Optional<NotesDO> delete(int noteId)`：删除对象、关系或临时状态。

## `service/NpcService.java`

- `class NpcService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<PlayernpcsFieldDO> getPlayerNpcFields(PlayernpcsFieldDO condition)`：读取并返回状态/数据。
  - `public List<PlayernpcsDO> getPlayerNpcDOs(PlayernpcsDO condition)`：读取并返回状态/数据。
  - `public List<PlayernpcsEquipDO> getPlayerNpcEquipDOs(PlayernpcsEquipDO condition)`：读取并返回状态/数据。
  - `public List<PlayerNPC> getPlayerNPC(PlayernpcsDO condition)`：读取并返回状态/数据。
  - `public PlayerNPC createPlayerNPC(PlayernpcsDO playerNpcDO, List<PlayernpcsEquipDO> playerNpcEquipDOS)`：创建对象、会话或业务记录。

## `service/NxCodeService.java`

- `class NxCodeService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void clearExpirations()`：通用业务逻辑入口，需结合实现查看细节。

## `service/NxCouponService.java`

- `class NxCouponService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<Integer> selectActiveCouponIds(int weekDay, int hourDay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<NxcouponsDO> getNxCoupons(NxcouponsDO condition)`：读取并返回状态/数据。

## `service/QuestService.java`

- `class QuestService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void deleteQuestProgressByCharacter(int cid)`：删除对象、关系或临时状态。
  - `public List<QuestStatus> getQuestStatusByCharacter(int cid)`：读取并返回状态/数据。

## `service/ServerService.java`

- `class ServerService`：业务编排层，组织领域逻辑与持久化调用。
  - `public List<WorldListRtnDTO> worldList()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<ChannelListRtnDTO> channelList(int worldId)`：通用业务逻辑入口，需结合实现查看细节。

## `service/ShopService.java`

- `class ShopService`：业务编排层，组织领域逻辑与持久化调用。
  - `public Page<ShopSearchRtnDTO> getShopList(ShopSearchReqDTO data)`：读取并返回状态/数据。
  - `public Page<ShopItemSearchRtnDTO> getShopItemList(ShopSearchReqDTO data)`：读取并返回状态/数据。
  - `public ShopItemSearchRtnDTO getShopItem(Long id)`：读取并返回状态/数据。
  - `public Long modifyShopItem(ShopItemSearchRtnDTO data, boolean isDelete)`：通用业务逻辑入口，需结合实现查看细节。
  - `private ShopItemSearchRtnDTO fromShopItemDO(ShopitemsDO shopitemsDO)`：通用业务逻辑入口，需结合实现查看细节。

## `service/UserDetailsImpl.java`

- `class UserDetailsImpl`：领域类型或功能模块，职责由同名文件实现定义。
  - `public UserDetailsImpl(Integer id, String name, String password, Collection<? extends GrantedAuthority> authorities)`：通用业务逻辑入口，需结合实现查看细节。

## `service/UserDetailsServiceImpl.java`

- `class UserDetailsServiceImpl`：领域类型或功能模块，职责由同名文件实现定义。
  - `public UserDetailsServiceImpl(AccountsMapper userRepository)`：通用业务逻辑入口，需结合实现查看细节。
  - `public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException`：从外部来源加载数据（数据库/文件/配置）。

## `service/WorldTransferService.java`

- `class WorldTransferService`：业务编排层，组织领域逻辑与持久化调用。
  - `public void applyAllWorldTransfer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean checkWorldTransferEligibility(WorldtransfersDO data)`：校验输入参数或业务约束。
  - `public void doWorldTransfer(WorldtransfersDO data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean registerWorldTransfer(Character chr, int newWorld)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelPendingWorldTransfer(Character chr, boolean needFinish)`：进行条件判定并返回布尔结果。
