# gms-server 逐符号中文职责 · 分卷 `util`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：23

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `util/BCrypt.java`

- `class BCrypt`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static String encode_base64(byte[] d, int len)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte char64(char x)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte[] decode_base64(String s, int maxolen)`：通用业务逻辑入口，需结合实现查看细节。
  - `private final void encipher(int[] lr, int off)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int[] streamtowords(byte[] data, int[] offp, int[] signp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int streamtoword(byte[] data, int[] offp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int streamtoword_bug(byte[] data, int[] offp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void init_key()`：初始化模块、资源或运行时状态。
  - `private void key(byte[] key, boolean sign_ext_bug)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void ekskey(byte[] data, byte[] key, boolean sign_ext_bug, int safety)`：通用业务逻辑入口，需结合实现查看细节。
  - `init_key()`：初始化模块、资源或运行时状态。
  - `ekskey(salt, password, sign_ext_bug, safety)`：通用业务逻辑入口，需结合实现查看细节。
  - `return hashpw(passwordb, salt)`：进行条件判定并返回布尔结果。

## `util/BasePageUtil.java`

- `class BasePageUtil`：工具类，封装无状态通用能力。
  - `private BasePageUtil(Collection<T> data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private BasePageUtil(Collection<T> data, BasePageDTO basePageDTO)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T> BasePageUtil<T> create(Collection<T> data)`：创建对象、会话或业务记录。
  - `public static <T> BasePageUtil<T> create(Collection<T> data, BasePageDTO basePageDTO)`：创建对象、会话或业务记录。
  - `public static <T> BasePageUtil<T> create(Collection<T> data, Integer pageNo, Integer pageSize)`：创建对象、会话或业务记录。
  - `public static <T> BasePageUtil<T> create(Collection<T> data, boolean onlyTotal, boolean notPage)`：创建对象、会话或业务记录。
  - `public BasePageUtil<T> filter(Predicate<T> predicate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public BasePageUtil<T> sorted(Comparator<? super T> comparator)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Page<T> page()`：通用业务逻辑入口，需结合实现查看细节。
  - `public <R> Page<R> page(Function<T, R> mapper)`：通用业务逻辑入口，需结合实现查看细节。

## `util/CashIdGenerator.java`

- `class CashIdGenerator`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static synchronized void loadExistentCashIdsFromDb()`：从外部来源加载数据（数据库/文件/配置）。
  - `private static void getNextAvailableCashId()`：读取并返回状态/数据。
  - `public static synchronized int generateCashId()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static synchronized void freeCashId(int cashId)`：通用业务逻辑入口，需结合实现查看细节。

## `util/CustomSpringBeanConfig.java`

- `class CustomSpringBeanConfig`：配置绑定/初始化相关类型。
  - `public SpringDocConfigProperties springDocConfigProperties()`：通用业务逻辑入口，需结合实现查看细节。
  - `public SwaggerUiConfigProperties swaggerUiConfigProperties()`：通用业务逻辑入口，需结合实现查看细节。

## `util/DatabaseConnection.java`

- `class DatabaseConnection`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Connection getConnection() throws SQLException`：读取并返回状态/数据。

## `util/ExtendUtil.java`

- `class ExtendUtil`：工具类，封装无状态通用能力。
  - `public static ExtendValueDO getExtendValue(String extendId, String extendType, String extendName)`：读取并返回状态/数据。
  - `public static void saveOrUpdateExtendValue(String extendId, String extendType, String extendName, String extendValue)`：持久化当前状态到存储层。

## `util/HexTool.java`

- `class HexTool`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static String toHexString(byte[] bytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String toCompactHexString(byte[] bytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static byte[] toBytes(String hexString)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String removeAllSpaces(String input)`：删除对象、关系或临时状态。
  - `public static String toStringFromCharset(final byte[] bytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isSpecialCharacter(byte asciiCode)`：进行条件判定并返回布尔结果。

## `util/I18nUtil.java`

- `class I18nUtil`：工具类，封装无状态通用能力。
  - `public static String getMessage(String code, Object... args)`：读取并返回状态/数据。
  - `public static String getMessage(Locale locale, String code, Object... args)`：读取并返回状态/数据。
  - `public static String getLogMessage(String code, Object... args)`：读取并返回状态/数据。
  - `public static String getLogMessage(Locale locale, String code, Object... args)`：读取并返回状态/数据。
  - `public static String getExceptionMessage(String code, Object... args)`：读取并返回状态/数据。
  - `public static String getExceptionMessage(Locale locale, String code, Object... args)`：读取并返回状态/数据。

## `util/IntervalBuilder.java`

- `class IntervalBuilder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public IntervalBuilder()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void refitOverlappedIntervals(int st, int en, int newFrom, int newTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int bsearchInterval(int point)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addInterval(int from, int to)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean inInterval(int point)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean inInterval(int from, int to)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clear()`：通用业务逻辑入口，需结合实现查看细节。

## `util/JwtUtils.java`

- `class JwtUtils`：领域类型或功能模块，职责由同名文件实现定义。
  - `public String generateJwtToken(String username)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getUserNameFromJwtToken(String token)`：读取并返回状态/数据。
  - `public boolean validateJwtToken(String authToken)`：校验输入参数或业务约束。

## `util/LRUCache.java`

- `class LRUCache`：领域类型或功能模块，职责由同名文件实现定义。
  - `public LRUCache()`：通用业务逻辑入口，需结合实现查看细节。
  - `public LRUCache(int capacity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean removeEldestEntry(Map.Entry<K, V> eldest)`：删除对象、关系或临时状态。

## `util/NumberTool.java`

- `class NumberTool`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static long BytesToLong(byte[] aToConvert)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static byte[] LongToBytes(long nToConvert)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int floatToInt(float f)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int doubleToInt(double d)`：通用业务逻辑入口，需结合实现查看细节。

## `util/PacketCreator.java`

- `class PacketCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static long getTime(long utcTimestamp)`：读取并返回状态/数据。
  - `private static void writeMobSkillId(OutPacket packet, MobSkillId msId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet showHpHealed(int cid, int amount)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addRemainingSkillInfo(final OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addCharStats(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected static void addCharLook(final OutPacket p, Character chr, boolean mega)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addCharacterInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addNewYearInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addTeleportInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addMiniGameInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addAreaInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addCharEquips(final OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet setExtraPendantSlot(boolean toggleExtraSlot)`：写入或更新状态字段。
  - `private static void addCharEntry(OutPacket p, Character chr, boolean viewall)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addQuestInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addExpirationTime(final OutPacket p, long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addItemInfo(OutPacket p, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected static void addItemInfo(final OutPacket p, Item item, boolean zeroPosition)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addInventoryInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addSkillInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addMonsterBookInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet sendGuestTOS()`：向外发送响应、消息或网络包。
  - `public static Packet getHello(short mapleVersion, InitializationVector sendIv, InitializationVector recvIv)`：读取并返回状态/数据。
  - `public static Packet getPing()`：读取并返回状态/数据。
  - `public static Packet getLoginFailed(int reason)`：读取并返回状态/数据。
  - `public static Packet getAfterLoginError(int reason)`：读取并返回状态/数据。
  - `public static Packet sendPolice()`：向外发送响应、消息或网络包。
  - `public static Packet sendPolice(String text)`：向外发送响应、消息或网络包。
  - `public static Packet getPermBan(byte reason)`：读取并返回状态/数据。
  - `public static Packet getTempBan(long timestampTill, byte reason)`：读取并返回状态/数据。
  - `public static Packet getAuthSuccess(Client c)`：读取并返回状态/数据。
  - `private static Packet pinOperation(byte mode)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet pinRegistered()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet requestPin()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet requestPinAfterFailure()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet registerPin()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet pinAccepted()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet wrongPic()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet getServerList(int serverId, String serverName, int flag, String eventmsg, List<Channel> channelLoad)`：读取并返回状态/数据。
  - `public static Packet getEndOfServerList()`：读取并返回状态/数据。
  - `public static Packet getServerStatus(int status)`：读取并返回状态/数据。
  - `public static Packet getServerIP(InetAddress inetAddr, int port, int clientId)`：读取并返回状态/数据。
  - `public static Packet getChannelChange(InetAddress inetAddr, int port)`：读取并返回状态/数据。
  - `public static Packet getCharList(Client c, int serverId, int status)`：读取并返回状态/数据。
  - `public static Packet enableTV()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet removeTV()`：删除对象、关系或临时状态。
  - `public static Packet sendTV(Character chr, List<String> messages, int type, Character partner)`：向外发送响应、消息或网络包。
  - `public static Packet getCharInfo(Character chr)`：读取并返回状态/数据。
  - `public static Packet enableActions()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet updatePlayerStats(List<Pair<Stat, Integer>> stats, boolean enableActions, Character chr)`：更新已有对象/配置/缓存。
  - `public static Packet getWarpToMap(MapleMap to, int spawnPoint, Character chr)`：读取并返回状态/数据。
  - `public static Packet getWarpToMap(MapleMap to, int spawnPoint, Point spawnPosition, Character chr)`：读取并返回状态/数据。
  - `public static Packet spawnPortal(int townId, int targetId, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnDoor(int ownerid, Point pos, boolean launched)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet removeDoor(int ownerId, boolean town)`：删除对象、关系或临时状态。
  - `public static Packet spawnSummon(Summon summon, boolean animated)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet removeSummon(Summon summon, boolean animated)`：删除对象、关系或临时状态。
  - `public static Packet spawnKite(int objId, int itemId, String name, String msg, Point pos, int ft)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet removeKite(int objId, int animationType)`：删除对象、关系或临时状态。
  - `public static Packet sendCannotSpawnKite()`：向外发送响应、消息或网络包。
  - `public static Packet getRelogResponse()`：读取并返回状态/数据。
  - `public static Packet serverMessage(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet serverNotice(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet serverNotice(int type, String message, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet serverNotice(int type, int channel, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet serverNotice(int type, int channel, String message, boolean smegaEar)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Packet serverMessage(int type, int channel, String message, boolean servermessage, boolean megaEar, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet getAvatarMega(Character chr, String medal, int channel, int itemId, List<String> message, boolean ear)`：读取并返回状态/数据。
  - `public static Packet byeAvatarMega()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet gachaponMessage(Item item, String town, Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnNPC(NPC life)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnNPCRequestController(NPC life, boolean miniMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnMonster(Monster life, boolean newSpawn)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnMonster(Monster life, boolean newSpawn, int effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet controlMonster(Monster life, boolean newSpawn, boolean aggro)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet removeMonsterInvisibility(Monster life)`：删除对象、关系或临时状态。
  - `public static Packet makeMonsterInvisible(Monster life)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void encodeParentlessMobSpawnEffect(OutPacket p, boolean newSpawn, int effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void encodeTemporary(OutPacket p, Map<MonsterStatus, MonsterStatusEffect> stati)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Packet spawnMonsterInternal(Monster life, boolean requestController, boolean newSpawn, boolean aggro, int effect, boolean makeInvis)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnFakeMonster(Monster life, int effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet makeMonsterReal(Monster life)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet stopControllingMonster(int oid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet moveMonsterResponse(int objectid, short moveid, int currentMp, boolean useSkills)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet moveMonsterResponse(int objectid, short moveid, int currentMp, boolean useSkills, int skillId, int skillLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet getChatText(int cidfrom, String text, boolean gm, int show)`：读取并返回状态/数据。
  - `public static Packet getShowExpGain(int gain, int equip, int party, boolean inChat, boolean white)`：读取并返回状态/数据。
  - `public static Packet getShowFameGain(int gain)`：读取并返回状态/数据。
  - `public static Packet getShowMesoGain(int gain)`：读取并返回状态/数据。
  - `public static Packet getShowMesoGain(int gain, boolean inChat)`：读取并返回状态/数据。
  - `public static Packet getShowItemGain(int itemId, short quantity)`：读取并返回状态/数据。
  - `public static Packet getShowItemGain(int itemId, short quantity, boolean inChat)`：读取并返回状态/数据。
  - `public static Packet killMonster(int objId, boolean animation)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet killMonster(int objId, int animation)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet updateMapItemObject(MapItem drop, boolean giveOwnership)`：更新已有对象/配置/缓存。
  - `public static Packet dropItemFromMapObject(Character player, MapItem drop, Point dropfrom, Point dropto, byte mod)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void writeForeignBuffs(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet spawnPlayerMapObject(Client target, Character chr, boolean enteringField)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void encodeNewYearCardInfo(OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet onNewYearCardRes(Character user, int cardId, int mode, int msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet onNewYearCardRes(Character user, NewYearCardRecord newyear, int mode, int msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void encodeNewYearCard(NewYearCardRecord newyear, OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addRingLook(final OutPacket p, Character chr, boolean crush)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addMarriageRingLook(Client target, final OutPacket p, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addAnnounceBox(final OutPacket p, PlayerShop shop, int availability)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addAnnounceBox(final OutPacket p, MiniGame game, int ammount, int joinable)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void updateHiredMerchantBoxInfo(OutPacket p, HiredMerchant hm)`：更新已有对象/配置/缓存。
  - `public static Packet updateHiredMerchantBox(HiredMerchant hm)`：更新已有对象/配置/缓存。
  - `private static void updatePlayerShopBoxInfo(OutPacket p, PlayerShop shop)`：更新已有对象/配置/缓存。
  - `public static Packet updatePlayerShopBox(PlayerShop shop)`：更新已有对象/配置/缓存。
  - `public static Packet removePlayerShopBox(PlayerShop shop)`：删除对象、关系或临时状态。
  - `public static Packet facialExpression(Character from, int expression)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void rebroadcastMovementList(OutPacket op, InPacket ip, long movementDataLength)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void serializeMovementList(OutPacket p, List<LifeMovementFragment> moves)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet movePlayer(int chrId, InPacket movementPacket, long movementDataLength)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet moveSummon(int cid, int oid, Point startPos, InPacket movementPacket, long movementDataLength)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet moveMonster(int oid, boolean skillPossible, int skill, int skillId, int skillLevel, int pOption, Point startPos, InPacket movementPacket, long movementDataLength)`：通用业务逻辑入口，需结合实现查看细节。
  - `rebroadcastMovementList(p, movementPacket, movementDataLength)`：通用业务逻辑入口，需结合实现查看细节。
  - `addAttackBody(p, chr, skill, skilllevel, stance, numAttackedAndDamage, 0, damage, speed, direction, display)`：通用业务逻辑入口，需结合实现查看细节。
  - `addAttackBody(p, chr, skill, skilllevel, stance, numAttackedAndDamage, projectile, damage, speed, direction, display)`：通用业务逻辑入口，需结合实现查看细节。
  - `addAttackBody(p, chr, skill, skilllevel, stance, numAttackedAndDamage, 0, damage, speed, direction, display)`：通用业务逻辑入口，需结合实现查看细节。
  - `return updateAriantPQRanking(new LinkedHashMap<Character, Integer>()`：更新已有对象/配置/缓存。

## `util/Pair.java`

- `class Pair`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Pair(E left, F right)`：通用业务逻辑入口，需结合实现查看细节。
  - `public E getLeft()`：读取并返回状态/数据。
  - `public F getRight()`：读取并返回状态/数据。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。

## `util/Quartet.java`

- `class Quartet`：领域类型或功能模块，职责由同名文件实现定义。

## `util/Randomizer.java`

- `class Randomizer`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static int nextInt()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int nextInt(final int arg0)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void nextBytes(final byte[] bytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean nextBoolean()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static double nextDouble()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static float nextFloat()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static long nextLong()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int rand(final int lbound, final int ubound)`：通用业务逻辑入口，需结合实现查看细节。

## `util/RateLimitUtil.java`

- `class RateLimitUtil`：工具类，封装无状态通用能力。
  - `private RateLimitUtil()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static RateLimitUtil getInstance()`：读取并返回状态/数据。
  - `public boolean check(String ip)`：校验输入参数或业务约束。

## `util/RequireUtil.java`

- `class RequireUtil`：工具类，封装无状态通用能力。
  - `public static void requireNull(Object obj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNull(Object obj, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNotNull(Object obj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNotNull(Object obj, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNotEmpty(Object obj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNotEmpty(Object obj, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireTrue(boolean b, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireFalse(boolean b, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isEmpty(Object obj)`：进行条件判定并返回布尔结果。
  - `public static boolean isZero(Number obj)`：进行条件判定并返回布尔结果。
  - `public static void requireNotEmptyOrElse(Object obj, Runnable runnable)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void requireNotEmptyAndThen(Object obj, Runnable runnable)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static <T, R> void requireNotEmptyAndThen(T t, R r, BiConsumer<T, R> consumer)`：通用业务逻辑入口，需结合实现查看细节。

## `util/StringUtil.java`

- `class StringUtil`：工具类，封装无状态通用能力。
  - `public static String getLeftPaddedStr(String in, char padchar, int length)`：读取并返回状态/数据。
  - `public static String getRightPaddedStr(String in, char padchar, int length)`：读取并返回状态/数据。
  - `public static String joinStringFrom(String[] arr, int start)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String joinStringFrom(String[] arr, int start, String sep)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String makeEnumHumanReadable(String enumName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int countCharacters(String str, char chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isNumeric(String str)`：进行条件判定并返回布尔结果。

## `util/ThreadLocalUtil.java`

- `class ThreadLocalUtil`：工具类，封装无状态通用能力。
  - `public static void setCurrentClient(Client c)`：写入或更新状态字段。
  - `public static Client getCurrentClient()`：读取并返回状态/数据。
  - `public static void removeCurrentClient()`：删除对象、关系或临时状态。
  - `public static int getClientLang()`：读取并返回状态/数据。

## `util/Trio.java`

- `class Trio`：领域类型或功能模块，职责由同名文件实现定义。

## `util/packets/Fishing.java`

- `class Fishing`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static double getFishingLikelihood(int x)`：读取并返回状态/数据。
  - `public static double[] fetchFishingLikelihood()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean hitFishingTime(Character chr, int baitLevel, double yearLikelihood, double timeLikelihood)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void doFishing(Character chr, int baitLevel, double yearLikelihood, double timeLikelihood)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int getRandomItem()`：读取并返回状态/数据。
  - `private static void debugFishingLikelihood()`：通用业务逻辑入口，需结合实现查看细节。

## `util/packets/WeddingPackets.java`

- `class WeddingPackets`：领域类型或功能模块，职责由同名文件实现定义。
- `class Field_Wedding`：领域类型或功能模块，职责由同名文件实现定义。
- `class Field_WeddingPhoto`：领域类型或功能模块，职责由同名文件实现定义。
- `class GW_WeddingReservation`：领域类型或功能模块，职责由同名文件实现定义。
- `class WeddingWishList`：领域类型或功能模块，职责由同名文件实现定义。
- `class GW_WeddingWishList`：领域类型或功能模块，职责由同名文件实现定义。
- `enum MarriageStatus`：领域类型或功能模块，职责由同名文件实现定义。
- `enum MarriageRequest`：领域类型或功能模块，职责由同名文件实现定义。
- `enum WeddingType`：领域类型或功能模块，职责由同名文件实现定义。
- `enum WeddingMap`：领域类型或功能模块，职责由同名文件实现定义。
- `enum WeddingItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Packet onMarriageRequest(String name, int playerid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet onTakePhoto(String ReservedGroomName, String ReservedBrideName, int m_dwField, List<Character> m_dwUsers)`：通用业务逻辑入口，需结合实现查看细节。
