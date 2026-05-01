# gms-server 逐符号中文职责 · 分卷 `constants`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：74

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `constants/api/ApiConstant.java`

- `class ApiConstant`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/api/InformationType.java`

- `enum InformationType`：领域类型或功能模块，职责由同名文件实现定义。
  - `CASH("cash"),`：通用业务逻辑入口，需结合实现查看细节。
  - `CONSUME("consume"),`：通用业务逻辑入口，需结合实现查看细节。
  - `EQP("eqp"),`：通用业务逻辑入口，需结合实现查看细节。
  - `ETC("etc"),`：通用业务逻辑入口，需结合实现查看细节。
  - `INS("ins"),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAP("map"),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB("mob"),`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC("npc"),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET("pet"),`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL("skill"),`：通用业务逻辑入口，需结合实现查看细节。
  - `InformationType(final String type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static InformationType ofType(final String type)`：通用业务逻辑入口，需结合实现查看细节。

## `constants/game/CommodityFlag.java`

- `enum CommodityFlag`：领域类型或功能模块，职责由同名文件实现定义。
  - `SN(0, 0, "SN", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `FLAG(0, 1, "FLAG", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_ID(1, 2, "物品ID", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUNT(1 << 1, 3, "数量", (p, n)-> p.writeShort(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PRICE(1 << 2, 5, "价格", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `BONUS(1 << 3, 6, "属性奖励", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PRIORITY(1 << 4, 4, "优先级", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PERIOD(1 << 5, 7, "有效期", (p, n)-> p.writeShort(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLE_POINT(1 << 6, 8, "抵用券", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO(1 << 7, 9, "金币", (p, n)-> p.writeInt(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `FOR_PREMIUM_USER(1 << 8, 10, "高级用户", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `COMMODITY_GENDER(1 << 9, 11, "性别", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `ON_SALE(1 << 10, 12, "是否销售", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `CLASS(1 << 11, 13, "标签", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `LIMIT(1 << 12, 14, "限时特卖", (p, n)-> p.writeByte(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PB_CASH(1 << 13, 15, "Unknown", (p, n)-> p.writeShort(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PB_POINT(1 << 14, 16, "Unknown", (p, n)-> p.writeShort(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PB_GIFT(1 << 15, 17, "Unknown", (p, n)-> p.writeShort(n.intValue())),`：通用业务逻辑入口，需结合实现查看细节。
  - `PACKAGE_SN(1 << 16, 18, "礼包SN", (p, n)->`：通用业务逻辑入口，需结合实现查看细节。

## `constants/game/DelayedQuestUpdate.java`

- `enum DelayedQuestUpdate`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/game/ExpTable.java`

- `class ExpTable`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static int getExpNeededForLevel(int level)`：读取并返回状态/数据。
  - `public static int getTamenessNeededForLevel(int level)`：读取并返回状态/数据。
  - `public static int getMountExpNeededForLevel(int level)`：读取并返回状态/数据。
  - `public static int getEquipExpNeededForLevel(int level)`：读取并返回状态/数据。
  - `public static int getMountMaxLevel()`：读取并返回状态/数据。

## `constants/game/GameConstants.java`

- `class GameConstants`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static int getPlayerBonusDropRate(int slot)`：读取并返回状态/数据。
  - `public static int getPlayerBonusMesoRate(int slot)`：读取并返回状态/数据。
  - `public static int getPlayerBonusExpRate(int slot)`：读取并返回状态/数据。
  - `public static int[] getCustomKey(boolean customKeyset)`：读取并返回状态/数据。
  - `public static int[] getCustomType(boolean customKeyset)`：读取并返回状态/数据。
  - `public static int[] getCustomAction(boolean customKeyset)`：读取并返回状态/数据。
  - `public static String getJobName(int jobid)`：读取并返回状态/数据。
  - `public static int getJobUpgradeLevelRange(int jobbranch)`：读取并返回状态/数据。
  - `public static int getChangeJobSpUpgrade(int jobbranch)`：读取并返回状态/数据。
  - `public static boolean isHallOfFameMap(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isPodiumHallOfFameMap(int mapid)`：进行条件判定并返回布尔结果。
  - `public static byte getHallOfFameBranch(Job job, int mapid)`：读取并返回状态/数据。
  - `public static int getOverallJobRankByScriptId(int scriptId)`：读取并返回状态/数据。
  - `public static boolean canPnpcBranchUseScriptId(byte branch, int scriptId)`：进行条件判定并返回布尔结果。
  - `public static int getHallOfFameMapid(Job job)`：读取并返回状态/数据。
  - `public static int getJobBranch(Job job)`：读取并返回状态/数据。
  - `public static int getJobMaxLevel(Job job)`：读取并返回状态/数据。
  - `public static int getSkillBook(final int job)`：读取并返回状态/数据。
  - `public static boolean isAranSkills(final int skill)`：进行条件判定并返回布尔结果。
  - `public static boolean isHiddenSkills(final int skill)`：进行条件判定并返回布尔结果。
  - `public static boolean isCygnus(final int job)`：进行条件判定并返回布尔结果。
  - `public static boolean isAran(final int job)`：进行条件判定并返回布尔结果。
  - `private static boolean isInBranchJobTree(int skillJobId, int jobId, int branchType)`：进行条件判定并返回布尔结果。
  - `private static boolean hasDivergedBranchJobTree(int skillJobId, int jobId, int branchType)`：进行条件判定并返回布尔结果。
  - `public static boolean isInJobTree(int skillId, int jobId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPqSkill(final int skill)`：进行条件判定并返回布尔结果。
  - `public static boolean bannedBindSkills(final int skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isGMSkills(final int skill)`：进行条件判定并返回布尔结果。
  - `public static boolean isFreeMarketRoom(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isMerchantLocked(MapleMap map)`：进行条件判定并返回布尔结果。
  - `public static boolean isDojoBossArea(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isAriantColiseumLobby(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isAriantColiseumArena(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isPqSkillMap(int mapid)`：进行条件判定并返回布尔结果。
  - `public static boolean isFinisherSkill(int skillId)`：进行条件判定并返回布尔结果。
  - `public static boolean isMedalQuest(short questid)`：进行条件判定并返回布尔结果。
  - `public static boolean hasSPTable(Job job)`：进行条件判定并返回布尔结果。
  - `public static int getMonsterHP(final int level)`：读取并返回状态/数据。
  - `public static String ordinal(int i)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized static String numberWithCommas(int i)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized static Number parseNumber(String value)`：解析输入文本或二进制内容。
  - `private static int getMaxObstacleMobDamageFromWz()`：读取并返回状态/数据。
  - `public static int selectRandomReward(int[] rewards)`：通用业务逻辑入口，需结合实现查看细节。

## `constants/game/NextLevelType.java`

- `enum NextLevelType`：领域类型或功能模块，职责由同名文件实现定义。
  - `SEND_NEXT("sendNextLevel"),`：向外发送响应、消息或网络包。
  - `SEND_LAST("sendLastLevel"),`：向外发送响应、消息或网络包。
  - `SEND_LAST_NEXT("sendLastNextLevel"),`：向外发送响应、消息或网络包。
  - `SEND_OK("sendOkLevel"),`：向外发送响应、消息或网络包。
  - `SEND_SELECT("sendSelectLevel"),`：向外发送响应、消息或网络包。
  - `SEND_NEXT_SELECT("sendNextSelectLevel"),`：向外发送响应、消息或网络包。
  - `GET_INPUT_NUMBER("getInputNumberLevel"),`：读取并返回状态/数据。
  - `GET_INPUT_TEXT("getInputTextLevel"),`：读取并返回状态/数据。
  - `SEND_ACCEPT_DECLINE("sendAcceptDeclineLevel"),`：向外发送响应、消息或网络包。
  - `SEND_YES_NO("sendYesNoLevel"),`：向外发送响应、消息或网络包。
  - `NextLevelType(String type)`：通用业务逻辑入口，需结合实现查看细节。

## `constants/game/NpcChat.java`

- `class NpcChat`：领域类型或功能模块，职责由同名文件实现定义。
  - `private NpcChat()`：通用业务逻辑入口，需结合实现查看细节。

## `constants/id/ItemId.java`

- `class ItemId`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean isExpIncrease(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isRateCoupon(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isMonsterCard(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPyramidBuff(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isDojoBuff(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isChair(int itemId)`：进行条件判定并返回布尔结果。
  - `public static int[] allThrowingStarIds()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int[] allBulletIds()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isPartyAllCure(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPet(int itemId)`：进行条件判定并返回布尔结果。
  - `public static int[] getPermaPets()`：读取并返回状态/数据。
  - `public static boolean isWeddingToken(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isWeddingRing(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNxCard(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isCashPackage(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFaceExpression(int itemId)`：进行条件判定并返回布尔结果。
  - `public static int[] getOwlItems()`：读取并返回状态/数据。
  - `public static boolean isExplorerMount(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isCygnusMount(int itemId)`：进行条件判定并返回布尔结果。
  - `public static int getGender(int itemId)`：读取并返回状态/数据。

## `constants/id/MapId.java`

- `class MapId`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean isMapleIsland(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isGodlyStatMap(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isCygnusIntro(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPhysicalFitness(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isOlaOla(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isSelfLootableOnly(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isDojo(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPartyDojo(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isBossRush(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNettsPyramid(int mapId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFishingArea(int mapId)`：进行条件判定并返回布尔结果。

## `constants/id/MobId.java`

- `class MobId`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean isZakumArm(int mobId)`：进行条件判定并返回布尔结果。
  - `public static boolean isDeadHorntailPart(int mobId)`：进行条件判定并返回布尔结果。
  - `public static boolean isDojoBoss(int mobId)`：进行条件判定并返回布尔结果。

## `constants/id/NpcId.java`

- `class NpcId`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/inventory/EquipSlot.java`

- `enum EquipSlot`：领域类型或功能模块，职责由同名文件实现定义。
  - `HAT("Cp", -1),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPECIAL_HAT("HrCp", -1),`：通用业务逻辑入口，需结合实现查看细节。
  - `FACE_ACCESSORY("Af", -2),`：通用业务逻辑入口，需结合实现查看细节。
  - `EYE_ACCESSORY("Ay", -3),`：通用业务逻辑入口，需结合实现查看细节。
  - `EARRINGS("Ae", -4),`：通用业务逻辑入口，需结合实现查看细节。
  - `TOP("Ma", -5),`：通用业务逻辑入口，需结合实现查看细节。
  - `OVERALL("MaPn", -5),`：通用业务逻辑入口，需结合实现查看细节。
  - `PANTS("Pn", -6),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOES("So", -7),`：通用业务逻辑入口，需结合实现查看细节。
  - `GLOVES("GlGw", -8),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_GLOVES("Gv", -8),`：通用业务逻辑入口，需结合实现查看细节。
  - `CAPE("Sr", -9),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHIELD("Si", -10),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON("Wp", -11),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON_2("WpSi", -11),`：通用业务逻辑入口，需结合实现查看细节。
  - `LOW_WEAPON("WpSp", -11),`：通用业务逻辑入口，需结合实现查看细节。
  - `RING("Ri", -12, -13, -15, -16),`：通用业务逻辑入口，需结合实现查看细节。
  - `PENDANT("Pe", -17),`：通用业务逻辑入口，需结合实现查看细节。
  - `TAMED_MOB("Tm", -18),`：通用业务逻辑入口，需结合实现查看细节。
  - `SADDLE("Sd", -19),`：通用业务逻辑入口，需结合实现查看细节。
  - `MEDAL("Me", -49),`：通用业务逻辑入口，需结合实现查看细节。
  - `BELT("Be", -50),`：通用业务逻辑入口，需结合实现查看细节。
  - `EquipSlot()`：通用业务逻辑入口，需结合实现查看细节。
  - `EquipSlot(String wz, int... in)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public boolean isAllowed(int slot, boolean cash)`：进行条件判定并返回布尔结果。
  - `public static EquipSlot getFromTextSlot(String slot)`：读取并返回状态/数据。

## `constants/inventory/EquipType.java`

- `enum EquipType`：领域类型或功能模块，职责由同名文件实现定义。
  - `UNDEFINED(-1),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCESSORY(0),`：通用业务逻辑入口，需结合实现查看细节。
  - `CAP(100),`：通用业务逻辑入口，需结合实现查看细节。
  - `CAPE(110),`：通用业务逻辑入口，需结合实现查看细节。
  - `COAT(104),`：通用业务逻辑入口，需结合实现查看细节。
  - `FACE(2),`：通用业务逻辑入口，需结合实现查看细节。
  - `GLOVES(108),`：通用业务逻辑入口，需结合实现查看细节。
  - `HAIR(3),`：通用业务逻辑入口，需结合实现查看细节。
  - `LONGCOAT(105),`：通用业务逻辑入口，需结合实现查看细节。
  - `PANTS(106),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EQUIP(180),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EQUIP_FIELD(181),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EQUIP_LABEL(182),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EQUIP_QUOTE(183),`：通用业务逻辑入口，需结合实现查看细节。
  - `RING(111),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHIELD(109),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOES(107),`：通用业务逻辑入口，需结合实现查看细节。
  - `TAMING(190),`：通用业务逻辑入口，需结合实现查看细节。
  - `TAMING_SADDLE(191),`：通用业务逻辑入口，需结合实现查看细节。
  - `SWORD(1302),`：通用业务逻辑入口，需结合实现查看细节。
  - `AXE(1312),`：通用业务逻辑入口，需结合实现查看细节。
  - `MACE(1322),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAGGER(1332),`：通用业务逻辑入口，需结合实现查看细节。
  - `WAND(1372),`：通用业务逻辑入口，需结合实现查看细节。
  - `STAFF(1382),`：通用业务逻辑入口，需结合实现查看细节。
  - `SWORD_2H(1402),`：通用业务逻辑入口，需结合实现查看细节。
  - `AXE_2H(1412),`：通用业务逻辑入口，需结合实现查看细节。
  - `MACE_2H(1422),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEAR(1432),`：通用业务逻辑入口，需结合实现查看细节。
  - `POLEARM(1442),`：通用业务逻辑入口，需结合实现查看细节。
  - `BOW(1452),`：通用业务逻辑入口，需结合实现查看细节。
  - `CROSSBOW(1462),`：通用业务逻辑入口，需结合实现查看细节。
  - `CLAW(1472),`：通用业务逻辑入口，需结合实现查看细节。
  - `KNUCKLER(1482),`：通用业务逻辑入口，需结合实现查看细节。
  - `PISTOL(1492)`：通用业务逻辑入口，需结合实现查看细节。
  - `EquipType(int val)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getValue()`：读取并返回状态/数据。
  - `public static EquipType getEquipTypeById(int itemid)`：读取并返回状态/数据。

## `constants/inventory/ItemConstants.java`

- `class ItemConstants`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static int getFlagByInt(int type)`：读取并返回状态/数据。
  - `public static boolean isThrowingStar(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isBullet(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPotion(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFood(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isConsumable(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isRechargeable(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isArrowForCrossBow(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isArrowForBow(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isArrow(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPet(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isExpirablePet(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPermanentItem(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewYearCardEtc(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewYearCardUse(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isAccessory(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isTaming(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isTownScroll(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isAntibanishScroll(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isCleanSlate(int scrollId)`：进行条件判定并返回布尔结果。
  - `public static boolean isModifierScroll(int scrollId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFlagModifier(int scrollId, short flag)`：进行条件判定并返回布尔结果。
  - `public static boolean isChaosScroll(int scrollId)`：进行条件判定并返回布尔结果。
  - `public static boolean isRateCoupon(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isExpCoupon(int couponId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPartyItem(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isHiredMerchant(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isPlayerShop(int itemId)`：进行条件判定并返回布尔结果。
  - `public static InventoryType getInventoryType(final int itemId)`：读取并返回状态/数据。
  - `public static boolean isMakerReagent(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isOverall(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isCashStore(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isMapleLife(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isWeapon(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isEquipment(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFishingChair(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isMedal(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isFace(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isHair(int itemId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultFace(int job, int gender, int faceId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultHair(int gender, int hairId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultHairColor(int hairColor)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultSkinColor(int skinColor)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultTop(int job, int gender, int topId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultBottom(int job, int gender, int bottomId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultShoes(int job, int shoesId)`：进行条件判定并返回布尔结果。
  - `public static boolean isNewCharDefaultWeapon(int job, int weaponId)`：进行条件判定并返回布尔结果。
  - `public static boolean notValidHairColor(int hairColor)`：通用业务逻辑入口，需结合实现查看细节。

## `constants/net/OpcodeConstants.java`

- `class OpcodeConstants`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void generateOpcodeNames()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void init(Opcode[] sendValues, Opcode[] recvValues)`：初始化模块、资源或运行时状态。

## `constants/net/ServerConstants.java`

- `class ServerConstants`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Aran.java`

- `class Aran`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Archer.java`

- `class Archer`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Assassin.java`

- `class Assassin`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Bandit.java`

- `class Bandit`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Beginner.java`

- `class Beginner`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Bishop.java`

- `class Bishop`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/BlazeWizard.java`

- `class BlazeWizard`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Bowmaster.java`

- `class Bowmaster`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Brawler.java`

- `class Brawler`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Buccaneer.java`

- `class Buccaneer`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/ChiefBandit.java`

- `class ChiefBandit`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Cleric.java`

- `class Cleric`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Corsair.java`

- `class Corsair`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Crossbowman.java`

- `class Crossbowman`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Crusader.java`

- `class Crusader`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/DarkKnight.java`

- `class DarkKnight`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/DawnWarrior.java`

- `class DawnWarrior`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/DragonKnight.java`

- `class DragonKnight`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Evan.java`

- `class Evan`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/FPArchMage.java`

- `class FPArchMage`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/FPMage.java`

- `class FPMage`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/FPWizard.java`

- `class FPWizard`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Fighter.java`

- `class Fighter`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/GM.java`

- `class GM`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Gunslinger.java`

- `class Gunslinger`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Hermit.java`

- `class Hermit`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Hero.java`

- `class Hero`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Hunter.java`

- `class Hunter`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/ILArchMage.java`

- `class ILArchMage`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/ILMage.java`

- `class ILMage`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/ILWizard.java`

- `class ILWizard`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Legend.java`

- `class Legend`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Magician.java`

- `class Magician`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Marauder.java`

- `class Marauder`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Marksman.java`

- `class Marksman`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/NightLord.java`

- `class NightLord`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/NightWalker.java`

- `class NightWalker`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Noblesse.java`

- `class Noblesse`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Outlaw.java`

- `class Outlaw`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Page.java`

- `class Page`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Paladin.java`

- `class Paladin`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Pirate.java`

- `class Pirate`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Priest.java`

- `class Priest`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Ranger.java`

- `class Ranger`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Rogue.java`

- `class Rogue`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Shadower.java`

- `class Shadower`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Sniper.java`

- `class Sniper`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Spearman.java`

- `class Spearman`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/SuperGM.java`

- `class SuperGM`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/ThunderBreaker.java`

- `class ThunderBreaker`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/Warrior.java`

- `class Warrior`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/WhiteKnight.java`

- `class WhiteKnight`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/skills/WindArcher.java`

- `class WindArcher`：领域类型或功能模块，职责由同名文件实现定义。

## `constants/string/CategoryType.java`

- `enum CategoryType`：领域类型或功能模块，职责由同名文件实现定义。
  - `MAIN(8, I18nUtil.getMessage("CategoryType.MAIN")),`：通用业务逻辑入口，需结合实现查看细节。
  - `EVENT(1, I18nUtil.getMessage("CategoryType.EVENT")),`：通用业务逻辑入口，需结合实现查看细节。
  - `EQUIP(2, I18nUtil.getMessage("CategoryType.EQUIP")),`：通用业务逻辑入口，需结合实现查看细节。
  - `USE(3, I18nUtil.getMessage("CategoryType.USE")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SET(4, I18nUtil.getMessage("CategoryType.SET")),`：写入或更新状态字段。
  - `ETC(5, I18nUtil.getMessage("CategoryType.ETC")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET(6, I18nUtil.getMessage("CategoryType.PET")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PACKAGE(7, I18nUtil.getMessage("CategoryType.PACKAGE")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CategoryType(final int id, final String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static CategoryType ofId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String toName(int id)`：通用业务逻辑入口，需结合实现查看细节。

## `constants/string/CharsetConstants.java`

- `class CharsetConstants`：领域类型或功能模块，职责由同名文件实现定义。
- `enum Language`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Charset getCharset(int language)`：读取并返回状态/数据。
  - `public static Locale getLanguageLocale(int language)`：读取并返回状态/数据。
  - `public static boolean isZhCN()`：进行条件判定并返回布尔结果。
  - `private static Language loadServiceLanguage()`：从外部来源加载数据（数据库/文件/配置）。

## `constants/string/ExtendType.java`

- `enum ExtendType`：领域类型或功能模块，职责由同名文件实现定义。
  - `ACCOUNT_EXTEND("11"),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCOUNT_EXTEND_DAILY("12"),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCOUNT_EXTEND_WEEKLY("13"),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARACTER_EXTEND("21"),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARACTER_EXTEND_DAILY("22"),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARACTER_EXTEND_WEEKLY("23"),`：通用业务逻辑入口，需结合实现查看细节。
  - `UNSUPPORTED("99")`：通用业务逻辑入口，需结合实现查看细节。
  - `ExtendType(String type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static ExtendType getExtendType(String type)`：读取并返回状态/数据。
  - `public static boolean isAccount(String type)`：进行条件判定并返回布尔结果。
  - `public static boolean isCharacter(String type)`：进行条件判定并返回布尔结果。

## `constants/string/LanguageConstants.java`

- `class LanguageConstants`：领域类型或功能模块，职责由同名文件实现定义。
- `enum Language`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static String getMessage(Character chr, String[] message)`：读取并返回状态/数据。
