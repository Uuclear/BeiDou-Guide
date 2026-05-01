# gms-server 逐符号中文职责 · 分卷 `client`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：241

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

## `client/AbstractCharacterListener.java`

- `interface AbstractCharacterListener`：领域类型或功能模块，职责由同名文件实现定义。
  - `void onHpChanged(int oldHp)`：通用业务逻辑入口，需结合实现查看细节。
  - `void onHpMpPoolUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `void onStatUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `void onAnnounceStatPoolUpdate()`：通用业务逻辑入口，需结合实现查看细节。

## `client/AbstractCharacterObject.java`

- `class AbstractCharacterObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected AbstractCharacterObject()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void setListener(AbstractCharacterListener listener)`：写入或更新状态字段。
  - `public int getStr()`：读取并返回状态/数据。
  - `public int getDex()`：读取并返回状态/数据。
  - `public int getInt()`：读取并返回状态/数据。
  - `public int getLuk()`：读取并返回状态/数据。
  - `public int getRemainingAp()`：读取并返回状态/数据。
  - `protected int getRemainingSp(int jobid)`：读取并返回状态/数据。
  - `public int[] getRemainingSps()`：读取并返回状态/数据。
  - `public int getHpMpApUsed()`：读取并返回状态/数据。
  - `public boolean isAlive()`：进行条件判定并返回布尔结果。
  - `public int getHp()`：读取并返回状态/数据。
  - `public int getMp()`：读取并返回状态/数据。
  - `public int getMaxHp()`：读取并返回状态/数据。
  - `public int getMaxMp()`：读取并返回状态/数据。
  - `public int getCurrentMaxHp()`：读取并返回状态/数据。
  - `public int getCurrentMaxMp()`：读取并返回状态/数据。
  - `private void dispatchHpChanged(final int oldHp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchHpMpPoolUpdated()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchStatUpdated()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchStatPoolUpdateAnnounced()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void setHp(int newHp)`：写入或更新状态字段。
  - `protected void setMp(int newMp)`：写入或更新状态字段。
  - `public void setRemainingSp(int remainingSp, int skillbook)`：写入或更新状态字段。
  - `protected void setMaxHp(int hp_)`：写入或更新状态字段。
  - `protected void setMaxMp(int mp_)`：写入或更新状态字段。
  - `private static long clampStat(int v, int min, int max)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static long calcStatPoolNode(Integer v, int displacement)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static long calcStatPoolLong(Integer v1, Integer v2, Integer v3, Integer v4)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void changeStatPool(Long hpMpPool, Long strDexIntLuk, Long newSp, int newAp, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void healHpMp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateHpMp(int x)`：更新已有对象/配置/缓存。
  - `public void updateHpMp(int newhp, int newmp)`：更新已有对象/配置/缓存。
  - `public void changeHpMp(int newhp, int newmp, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void changeHpMpPool(Integer hp, Integer mp, Integer maxhp, Integer maxmp, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateHp(int hp)`：更新已有对象/配置/缓存。
  - `public void updateMaxHp(int maxhp)`：更新已有对象/配置/缓存。
  - `public void updateHpMaxHp(int hp, int maxhp)`：更新已有对象/配置/缓存。
  - `private void updateHpMaxHp(Integer hp, Integer maxhp)`：更新已有对象/配置/缓存。
  - `public void updateMp(int mp)`：更新已有对象/配置/缓存。
  - `public void updateMaxMp(int maxmp)`：更新已有对象/配置/缓存。
  - `public void updateMpMaxMp(int mp, int maxmp)`：更新已有对象/配置/缓存。
  - `private void updateMpMaxMp(Integer mp, Integer maxmp)`：更新已有对象/配置/缓存。
  - `public void updateMaxHpMaxMp(int maxhp, int maxmp)`：更新已有对象/配置/缓存。
  - `protected void enforceMaxHpMp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int safeAddHP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addHP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMPHP(int hpDelta, int mpDelta)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void addMaxMPMaxHP(int hpdelta, int mpdelta, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMaxHP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMaxMP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setStr(int str)`：写入或更新状态字段。
  - `public void setDex(int dex)`：写入或更新状态字段。
  - `public void setInt(int int_)`：写入或更新状态字段。
  - `public void setLuk(int luk)`：写入或更新状态字段。
  - `public boolean assignStr(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignDex(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignInt(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignLuk(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignHP(int deltaHP, int deltaAp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignMP(int deltaMP, int deltaAp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int apAssigned(Integer x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean assignStrDexIntLuk(int deltaStr, int deltaDex, int deltaInt, int deltaLuk)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean assignStrDexIntLuk(Integer deltaStr, Integer deltaDex, Integer deltaInt, Integer deltaLuk)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateStrDexIntLuk(int x)`：更新已有对象/配置/缓存。
  - `public void changeRemainingAp(int x, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainAp(int deltaAp, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void updateStrDexIntLuk(int str, int dex, int int_, int luk, int remainingAp)`：更新已有对象/配置/缓存。
  - `private void changeStrDexIntLuk(Integer str, Integer dex, Integer int_, Integer luk, int remainingAp, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void changeStrDexIntLukSp(Integer str, Integer dex, Integer int_, Integer luk, int remainingAp, int remainingSp, int skillbook, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void updateStrDexIntLukSp(int str, int dex, int int_, int luk, int remainingAp, int remainingSp, int skillbook)`：更新已有对象/配置/缓存。
  - `protected void setRemainingSp(int[] sps)`：写入或更新状态字段。
  - `protected void updateRemainingSp(int remainingSp, int skillbook)`：更新已有对象/配置/缓存。
  - `protected void changeRemainingSp(int remainingSp, int skillbook, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainSp(int deltaSp, int skillbook, boolean silent)`：通用业务逻辑入口，需结合实现查看细节。

## `client/BuddyList.java`

- `class BuddyList`：领域类型或功能模块，职责由同名文件实现定义。
- `enum BuddyOperation`：领域类型或功能模块，职责由同名文件实现定义。
- `enum BuddyAddResult`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BuddyList(int capacity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean contains(int characterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean containsVisible(int characterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCapacity()`：读取并返回状态/数据。
  - `public void setCapacity(int capacity)`：写入或更新状态字段。
  - `public BuddylistEntry get(int characterId)`：读取并返回状态/数据。
  - `public BuddylistEntry get(String characterName)`：读取并返回状态/数据。
  - `public void put(BuddylistEntry entry)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void remove(int characterId)`：删除对象、关系或临时状态。
  - `public Collection<BuddylistEntry> getBuddies()`：读取并返回状态/数据。
  - `public boolean isFull()`：进行条件判定并返回布尔结果。
  - `public int[] getBuddyIds()`：读取并返回状态/数据。
  - `public void broadcast(Packet packet, PlayerStorage pstorage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void loadFromDb(int characterId)`：从外部来源加载数据（数据库/文件/配置）。
  - `public CharacterNameAndId pollPendingRequest()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addBuddyRequest(Client c, int cidFrom, String nameFrom, int channelFrom)`：通用业务逻辑入口，需结合实现查看细节。

## `client/BuddylistEntry.java`

- `class BuddylistEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BuddylistEntry(String name, String group, int characterId, int channel, boolean visible)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public void setChannel(int channel)`：写入或更新状态字段。
  - `public boolean isOnline()`：进行条件判定并返回布尔结果。
  - `public String getName()`：读取并返回状态/数据。
  - `public String getGroup()`：读取并返回状态/数据。
  - `public int getCharacterId()`：读取并返回状态/数据。
  - `public void setVisible(boolean visible)`：写入或更新状态字段。
  - `public boolean isVisible()`：进行条件判定并返回布尔结果。
  - `public void changeGroup(String group)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。

## `client/BuffStat.java`

- `enum BuffStat`：领域类型或功能模块，职责由同名文件实现定义。
  - `MORPH(0x2L),`：通用业务逻辑入口，需结合实现查看细节。
  - `RECOVERY(0x4L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLE_WARRIOR(0x8L),`：通用业务逻辑入口，需结合实现查看细节。
  - `STANCE(0x10L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHARP_EYES(0x20L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MANA_REFLECTION(0x40L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHADOW_CLAW(0x100L),`：通用业务逻辑入口，需结合实现查看细节。
  - `INFINITY(0x200L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HOLY_SHIELD(0x400L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HAMSTRING(0x800L),`：通用业务逻辑入口，需结合实现查看细节。
  - `BLIND(0x1000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `CONCENTRATE(0x2000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `PUPPET(0x4000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `ECHO_OF_HERO(0x8000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO_UP_BY_ITEM(0x10000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `GHOST_MORPH(0x20000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `AURA(0x40000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `CONFUSE(0x80000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_EXP1(0x100000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `EXP_BUFF(0x40000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_EXP2(0x200000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_EXP3(0x400000L), COUPON_EXP4(0x400000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_DRP1(0x800000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_DRP2(0x1000000L), COUPON_DRP3(0x1000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_UP_BY_ITEM(0x100000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `RESPECT_PIMMUNE(0x200000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `RESPECT_MIMMUNE(0x400000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DEFENSE_ATT(0x800000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DEFENSE_STATE(0x1000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HPREC(0x2000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MPREC(0x4000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `BERSERK_FURY(0x8000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DIVINE_BODY(0x10000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPARK(0x20000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAP_CHAIR(0x40000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `FINALATTACK(0x80000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `WATK(0x100000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `WDEF(0x200000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MATK(0x400000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MDEF(0x800000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACC(0x1000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `AVOID(0x2000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HANDS(0x4000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEED(0x8000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `JUMP(0x10000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_GUARD(0x20000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DARKSIGHT(0x40000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `BOOSTER(0x80000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `POWERGUARD(0x100000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HYPERBODYHP(0x200000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HYPERBODYMP(0x400000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `INVINCIBLE(0x800000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SOULARROW(0x1000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `STUN(0x2000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `POISON(0x4000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEAL(0x8000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DARKNESS(0x10000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `COMBO(0x20000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON(0x20000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `WK_CHARGE(0x40000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `DRAGONBLOOD(0x80000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `HOLY_SYMBOL(0x100000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESOUP(0x200000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHADOWPARTNER(0x400000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `PICKPOCKET(0x800000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESOGUARD(0x1000000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `EXP_INCREASE(0x2000000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAKEN(0x4000000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAP_PROTECTION(0x8000000000000000L),`：通用业务逻辑入口，需结合实现查看细节。
  - `SLOW(0x200000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `ELEMENTAL_RESET(0x200000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_SHIELD(0x400000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_RESISTANCE(0x800000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `WIND_WALK(0x400000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `ARAN_COMBO(0x1000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `COMBO_DRAIN(0x2000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `COMBO_BARRIER(0x4000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `BODY_PRESSURE(0x8000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `SMART_KNOCKBACK(0x10000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `BERSERK(0x20000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `ENERGY_CHARGE(0x4000000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `DASH2(0x8000000000000L, true), // correct (speed)`：通用业务逻辑入口，需结合实现查看细节。
  - `DASH(0x10000000000000L, true), // correct (jump)`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_RIDING(0x20000000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEED_INFUSION(0x40000000000000L, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `HOMING_BEACON(0x80000000000000L, true)`：通用业务逻辑入口，需结合实现查看细节。
  - `BuffStat(long i, boolean isFirst)`：通用业务逻辑入口，需结合实现查看细节。
  - `BuffStat(long i)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getValue()`：读取并返回状态/数据。
  - `public boolean isFirst()`：进行条件判定并返回布尔结果。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。

## `client/Character.java`

- `class Character`：领域类型或功能模块，职责由同名文件实现定义。
  - `private Character()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Job getJobStyle(byte opt)`：读取并返回状态/数据。
  - `public Job getJobStyle()`：读取并返回状态/数据。
  - `public static Character getDefault(Client c)`：读取并返回状态/数据。
  - `public boolean isLoggedInWorld()`：进行条件判定并返回布尔结果。
  - `public boolean isAwayFromWorld()`：进行条件判定并返回布尔结果。
  - `public void setEnteredChannelWorld()`：写入或更新状态字段。
  - `public void setAwayFromChannelWorld()`：写入或更新状态字段。
  - `public void setDisconnectedFromChannelWorld()`：写入或更新状态字段。
  - `private void setAwayFromChannelWorld(boolean disconnect)`：写入或更新状态字段。
  - `public void updatePartySearchAvailability(boolean pSearchAvailable)`：更新已有对象/配置/缓存。
  - `public boolean toggleRecvPartySearchInvite()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isRecvPartySearchInviteEnabled()`：进行条件判定并返回布尔结果。
  - `public void setSessionTransitionState()`：写入或更新状态字段。
  - `public void setCS(boolean cs)`：写入或更新状态字段。
  - `public long getNpcCooldown()`：读取并返回状态/数据。
  - `public void setNpcCooldown(long d)`：写入或更新状态字段。
  - `public void addCooldown(int skillId, long startTime, long length)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Ring getRingById(int id)`：读取并返回状态/数据。
  - `public int getRelationshipId()`：读取并返回状态/数据。
  - `public boolean isMarried()`：进行条件判定并返回布尔结果。
  - `public boolean hasJustMarried()`：进行条件判定并返回布尔结果。
  - `public int addDojoPointsByMap(int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMesosTraded(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addPet(Pet pet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addSummon(int id, Summon summon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addVisibleMapObject(MapObject mo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void ban(String reason)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean ban(String id, String reason, boolean accountId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int calculateMaxBaseDamage(int watk, WeaponType weapon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int calculateMaxBaseDamage(int watk)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int calculateMaxBaseMagicDamage(int matk)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCombo(short count)`：写入或更新状态字段。
  - `public short getCombo()`：读取并返回状态/数据。
  - `public boolean cannotEnterCashShop()`：进行条件判定并返回布尔结果。
  - `public void toggleBlockCashShop()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void toggleExpGain()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void newClient(Client c)`：创建对象、会话或业务记录。
  - `public String getMedalText()`：读取并返回状态/数据。
  - `public void hide(boolean hide, boolean login)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hide(boolean hide)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void toggleHide(boolean login)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelMagicDoor()`：进行条件判定并返回布尔结果。
  - `private void cancelPlayerBuffs(List<BuffStat> buffstats)`：进行条件判定并返回布尔结果。
  - `public static boolean canCreateChar(String name)`：进行条件判定并返回布尔结果。
  - `public static boolean existName(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canDoor()`：进行条件判定并返回布尔结果。
  - `public void setHasSandboxItem()`：写入或更新状态字段。
  - `public void removeSandboxItems()`：删除对象、关系或临时状态。
  - `public void changeCI(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setMasteries(int jobId)`：写入或更新状态字段。
  - `private void broadcastChangeJob()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void changeJob(Job newJob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastAcquaintances(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastAcquaintances(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeKeybinding(int key, KeyBinding keybinding)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeQuickslotKeybinding(byte[] aQuickslotKeyMapped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastStance(int newStance)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastStance()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapleMap getWarpMap(int map)`：读取并返回状态/数据。
  - `public void warpAhead(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void eventChangedMap(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void eventAfterChangedMap(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canRecoverLastBanish()`：进行条件判定并返回布尔结果。
  - `public void clearBanishPlayerData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setBanishPlayerData(int banishMap, int banishSp, long banishTime)`：写入或更新状态字段。
  - `public void changeMapBanish(int mapid, String portal, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(int map, Object pt)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(MapleMap to)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(MapleMap to, int portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(final MapleMap target, Portal pto)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMap(final MapleMap target, final Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceChangeMap(final MapleMap target, Portal pto)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean buffMapProtection()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Integer> getLastVisitedMapIds()`：读取并返回状态/数据。
  - `public void partyOperationUpdate(Party party, List<Character> exPartyMembers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void addPartyPlayerDoor(Character target)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void removePartyPlayerDoor(Party party, Character target)`：删除对象、关系或临时状态。
  - `private static void updatePartyTownDoors(Party party, Character target, Character partyLeaver, List<Character> partyMembers)`：更新已有对象/配置/缓存。
  - `private Integer getVisitedMapIndex(MapleMap map)`：读取并返回状态/数据。
  - `public void visitMap(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setOwnedMap(MapleMap map)`：写入或更新状态字段。
  - `public MapleMap getOwnedMap()`：读取并返回状态/数据。
  - `public void notifyMapTransferToPartner(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeIncomingInvites()`：删除对象、关系或临时状态。
  - `private void changeMapInternal(final MapleMap to, final Point pos, Packet warpPacket)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isChangingMaps()`：进行条件判定并返回布尔结果。
  - `public void setMapTransitionComplete()`：写入或更新状态字段。
  - `public void changePage(int page)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeSkillLevel(Skill skill, byte newLevel, int newMasterlevel, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeTab(int tab)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeType(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void checkBerserk(final boolean isHidden)`：校验输入参数或业务约束。
  - `public void checkMessenger()`：校验输入参数或业务约束。
  - `public void controlMonster(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stopControllingMonster(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getNumControlledMonsters()`：读取并返回状态/数据。
  - `public Collection<Monster> getControlledMonsters()`：读取并返回状态/数据。
  - `public void releaseControlledMonsters()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyConsumeOnPickup(final int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void pickupItem(MapObject ob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void pickupItem(MapObject ob, int petIndex)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countItem(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canHold(int itemid)`：进行条件判定并返回布尔结果。
  - `public boolean canHold(int itemid, int quantity)`：进行条件判定并返回布尔结果。
  - `public boolean canHoldUniques(List<Integer> itemids)`：进行条件判定并返回布尔结果。
  - `public boolean isRidingBattleship()`：进行条件判定并返回布尔结果。
  - `public void announceBattleshipHp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void decreaseBattleshipHp(int decrease)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void decreaseReports()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void deleteGuild(int guildId)`：删除对象、关系或临时状态。
  - `private void nextPendingRequest(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void notifyRemoteChannel(Client c, int remoteChannel, int otherCid, BuddyList.BuddyOperation operation)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void deleteBuddy(int otherCid)`：删除对象、关系或临时状态。
  - `public static boolean deleteCharFromDB(Character player, int senderAccId)`：删除对象、关系或临时状态。
  - `private static void deleteQuestProgressWhereCharacterId(Connection con, int cid) throws SQLException`：删除对象、关系或临时状态。
  - `private void deleteWhereCharacterId(Connection con, String sql) throws SQLException`：删除对象、关系或临时状态。
  - `private void stopChairTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void updateChairHealStats()`：更新已有对象/配置/缓存。
  - `private void startChairTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void stopExtraTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void startExtraTask(final byte healHP, final byte healMP, final short healInterval)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void startExtraTaskInternal(final byte healHP, final byte healMP, final short healInterval)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disbandGuild()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispel()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean hasDisease(final Disease dis)`：进行条件判定并返回布尔结果。
  - `public final int getDiseasesSize()`：读取并返回状态/数据。
  - `public void silentApplyDiseases(Map<Disease, Pair<Long, MobSkill>> diseaseMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void announceDiseases()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void collectDiseases()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveDebuff(final Disease disease, MobSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispelDebuff(Disease debuff)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispelDebuffs()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void purgeDebuffs()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelAllDebuffs()`：进行条件判定并返回布尔结果。
  - `public void dispelSkill(int skillid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean dispelSkills(int skillid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeFaceExpression(int emote)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void doHurtHp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void enteredScript(String script, int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void equipChanged()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelDiseaseExpireTask()`：进行条件判定并返回布尔结果。
  - `public void diseaseExpireTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelBuffExpireTask()`：进行条件判定并返回布尔结果。
  - `public void buffExpireTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelSkillCooldownTask()`：进行条件判定并返回布尔结果。
  - `public void skillCooldownTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelExpirationTask()`：进行条件判定并返回布尔结果。
  - `public void expirationTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceUpdateItem(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainGachaExp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addGachaExp(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain, boolean show, boolean inChat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain, boolean show, boolean inChat, boolean white)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain, int party, boolean show, boolean inChat, boolean white)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void loseExp(int loss, boolean show, boolean inChat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void loseExp(int loss, boolean show, boolean inChat, boolean white)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void announceExpGain(long gain, int equip, int party, boolean inChat, boolean white)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void gainExpInternal(long gain, int equip, int party, boolean show, boolean inChat, boolean white)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainFame(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean gainFame(int delta, Character fromPlayer, int mode)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canHoldMeso(int gain)`：进行条件判定并返回布尔结果。
  - `public void gainMeso(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainMeso(int gain, boolean show)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainMeso(int gain, boolean show, boolean enableActions, boolean inChat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void genericGuildMessage(int code)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PlayerCoolDownValueHolder> getAllCooldowns()`：读取并返回状态/数据。
  - `public void updateAriantScore()`：更新已有对象/配置/缓存。
  - `public void updateAriantScore(int dropQty)`：更新已有对象/配置/缓存。
  - `public Long getBuffedStarttime(BuffStat effect)`：读取并返回状态/数据。
  - `public Integer getBuffedValue(BuffStat effect)`：读取并返回状态/数据。
  - `public int getBuffSource(BuffStat stat)`：读取并返回状态/数据。
  - `public StatEffect getBuffEffect(BuffStat stat)`：读取并返回状态/数据。
  - `private List<BuffStatValueHolder> getAllStatups()`：读取并返回状态/数据。
  - `public List<PlayerBuffValueHolder> getAllBuffs()`：读取并返回状态/数据。
  - `public boolean hasBuffFromSourceid(int sourceid)`：进行条件判定并返回布尔结果。
  - `public boolean hasActiveBuff(int sourceid)`：进行条件判定并返回布尔结果。
  - `private void addItemEffectHolder(Integer sourceid, long expirationtime, Map<BuffStat, BuffStatValueHolder> statups)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean removeEffectFromItemEffectHolder(Integer sourceid, BuffStat buffStat)`：删除对象、关系或临时状态。
  - `private void removeItemEffectHolder(Integer sourceid)`：删除对象、关系或临时状态。
  - `private BuffStatValueHolder fetchBestEffectFromItemEffectHolder(BuffStat mbs)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void extractBuffValue(int sourceid, BuffStat stat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void debugListAllBuffs()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelAllBuffs(boolean softcancel)`：进行条件判定并返回布尔结果。
  - `private void dropBuffStats(List<Pair<BuffStat, BuffStatValueHolder>> effectsToCancel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelEffect(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean cancelEffect(StatEffect effect, boolean overwrite, long startTime)`：进行条件判定并返回布尔结果。
  - `private static StatEffect getEffectFromBuffSource(Map<BuffStat, BuffStatValueHolder> buffSource)`：读取并返回状态/数据。
  - `private boolean isUpdatingEffect(Set<StatEffect> activeEffects, StatEffect mse)`：进行条件判定并返回布尔结果。
  - `public void updateActiveEffects()`：更新已有对象/配置/缓存。
  - `private void updateEffects(Set<BuffStat> removedStats)`：更新已有对象/配置/缓存。
  - `private boolean cancelEffect(StatEffect effect, boolean overwrite, long startTime, boolean firstCancel)`：进行条件判定并返回布尔结果。
  - `public void cancelEffectFromBuffStat(BuffStat stat)`：进行条件判定并返回布尔结果。
  - `public void cancelBuffStats(BuffStat stat)`：进行条件判定并返回布尔结果。
  - `private void cancelInactiveBuffStats(Set<BuffStat> retrievedStats, Set<BuffStat> removedStats)`：进行条件判定并返回布尔结果。
  - `private static List<StatEffect> topologicalSortRemoveLeafStats(Map<StatEffect, Set<BuffStat>> stackedBuffStats, Map<BuffStat, Stack<StatEffect>> buffStack, Map<StatEffect, Integer> leafStatCount)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void topologicalSortRebaseLeafStats(Map<StatEffect, Set<BuffStat>> stackedBuffStats, Map<BuffStat, Stack<StatEffect>> buffStack)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static List<StatEffect> topologicalSortEffects(Map<BuffStat, List<Pair<StatEffect, Integer>>> buffEffects)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static List<StatEffect> sortEffectsList(Map<StatEffect, Integer> updateEffectsList)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void propagateBuffEffectUpdates(Map<Integer, Pair<StatEffect, Long>> retrievedEffects, Set<BuffStat> retrievedStats, Set<BuffStat> removedStats)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static BuffStat getSingletonStatupFromEffect(StatEffect mse)`：读取并返回状态/数据。
  - `private static boolean isSingletonStatup(BuffStat mbs)`：进行条件判定并返回布尔结果。
  - `private static boolean isPriorityBuffSourceId(int sourceId)`：进行条件判定并返回布尔结果。
  - `private void addItemEffectHolderCount(BuffStat stat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerEffect(StatEffect effect, long starttime, long expirationtime, boolean isSilent)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getJobMapChair(Job job)`：读取并返回状态/数据。
  - `public boolean unregisterChairBuff()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean registerChairBuff()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getChair()`：读取并返回状态/数据。
  - `public String getChalkboard()`：读取并返回状态/数据。
  - `public AbstractPlayerInteraction getAbstractPlayerInteraction()`：读取并返回状态/数据。
  - `private List<QuestStatus> getQuestValues()`：读取并返回状态/数据。
  - `public final List<QuestStatus> getCompletedQuests()`：读取并返回状态/数据。
  - `public List<Ring> getCrushRings()`：读取并返回状态/数据。
  - `public Collection<Door> getDoors()`：读取并返回状态/数据。
  - `public Door getPlayerDoor()`：读取并返回状态/数据。
  - `public Door getMainTownDoor()`：读取并返回状态/数据。
  - `public void applyPartyDoor(Door door, boolean partyUpdate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Door removePartyDoor(boolean partyUpdate)`：删除对象、关系或临时状态。
  - `private void removePartyDoor(Party formerParty)`：删除对象、关系或临时状态。
  - `public EventInstanceManager getEventInstance()`：读取并返回状态/数据。
  - `public Marriage getMarriageInstance()`：读取并返回状态/数据。
  - `public void resetExcluded(int petId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addExcluded(int petId, int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void commitExcludedItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void exportExcludedItems(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Set<Integer> getExcludedItems()`：读取并返回状态/数据。
  - `public int getExp()`：读取并返回状态/数据。
  - `public int getGachaExp()`：读取并返回状态/数据。
  - `public boolean hasNoviceExpRate()`：进行条件判定并返回布尔结果。
  - `public float getExpRate()`：读取并返回状态/数据。
  - `public float getLevelExpRate()`：读取并返回状态/数据。
  - `public float getQuickLevelExpRate()`：读取并返回状态/数据。
  - `public void updateMobExpRate()`：更新已有对象/配置/缓存。
  - `public float getMobExpRate()`：读取并返回状态/数据。
  - `public int getCouponExpRate()`：读取并返回状态/数据。
  - `public float getRawExpRate()`：读取并返回状态/数据。
  - `public int getCouponDropRate()`：读取并返回状态/数据。
  - `public float getRawDropRate()`：读取并返回状态/数据。
  - `public float getBossDropRate()`：读取并返回状态/数据。
  - `public int getCouponMesoRate()`：读取并返回状态/数据。
  - `public float getRawMesoRate()`：读取并返回状态/数据。
  - `public float getQuestExpRate()`：读取并返回状态/数据。
  - `public float getQuestMesoRate()`：读取并返回状态/数据。
  - `public float getCardRate(int itemid)`：读取并返回状态/数据。
  - `public Family getFamily()`：读取并返回状态/数据。
  - `public void setFamilyEntry(FamilyEntry entry)`：写入或更新状态字段。
  - `public void setUsedStorage()`：写入或更新状态字段。
  - `public List<Ring> getFriendshipRings()`：读取并返回状态/数据。
  - `public boolean isMale()`：进行条件判定并返回布尔结果。
  - `public Guild getGuild()`：读取并返回状态/数据。
  - `public Alliance getAlliance()`：读取并返回状态/数据。
  - `public static int getAccountIdByName(String name)`：读取并返回状态/数据。
  - `public static int getIdByName(String name)`：读取并返回状态/数据。
  - `public static String getNameById(int id)`：读取并返回状态/数据。
  - `public Inventory getInventory(InventoryType type)`：读取并返回状态/数据。
  - `public boolean haveItemWithId(int itemid, boolean checkEquipped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean haveItemEquipped(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean haveWeddingRing()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getItemQuantity(int itemid, boolean checkEquipped)`：读取并返回状态/数据。
  - `public int getCleanItemQuantity(int itemid, boolean checkEquipped)`：读取并返回状态/数据。
  - `public int getJobType()`：读取并返回状态/数据。
  - `public int getFh()`：读取并返回状态/数据。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public Ring getMarriageRing()`：读取并返回状态/数据。
  - `public int getMasterLevel(int skill)`：读取并返回状态/数据。
  - `public int getMasterLevel(Skill skill)`：读取并返回状态/数据。
  - `public int getTotalStr()`：读取并返回状态/数据。
  - `public int getTotalDex()`：读取并返回状态/数据。
  - `public int getTotalInt()`：读取并返回状态/数据。
  - `public int getTotalLuk()`：读取并返回状态/数据。
  - `public int getTotalMagic()`：读取并返回状态/数据。
  - `public int getTotalWatk()`：读取并返回状态/数据。
  - `public int getMaxClassLevel()`：读取并返回状态/数据。
  - `public int getMaxLevel()`：读取并返回状态/数据。
  - `public int getMeso()`：读取并返回状态/数据。
  - `public void setMeso(int meso)`：写入或更新状态字段。
  - `public int getMerchantMeso()`：读取并返回状态/数据。
  - `public int getMerchantNetMeso()`：读取并返回状态/数据。
  - `public GuildCharacter getMGC()`：读取并返回状态/数据。
  - `public void setMGC(GuildCharacter mgc)`：写入或更新状态字段。
  - `public PartyCharacter getMPC()`：读取并返回状态/数据。
  - `public void setMPC(PartyCharacter mpc)`：写入或更新状态字段。
  - `public void setPlayerAggro(int mobHash)`：写入或更新状态字段。
  - `public void resetPlayerAggro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMiniGamePoints(MiniGameResult type, boolean omok)`：读取并返回状态/数据。
  - `public int getMonsterBookCover()`：读取并返回状态/数据。
  - `public int getNoPets()`：读取并返回状态/数据。
  - `public Party getParty()`：读取并返回状态/数据。
  - `public int getPartyId()`：读取并返回状态/数据。
  - `public List<Character> getPartyMembersOnline()`：读取并返回状态/数据。
  - `public List<Character> getPartyMembersOnSameMap()`：读取并返回状态/数据。
  - `public boolean isPartyMember(Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean isPartyMember(int cid)`：进行条件判定并返回布尔结果。
  - `public void setGMLevel(int level)`：写入或更新状态字段。
  - `public void closePartySearchInteractions()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closePlayerInteractions()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeNpcShop()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeTrade()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closePlayerShop()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeMiniGame(boolean forceClose)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeHiredMerchant(boolean closeMerchant)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closePlayerMessenger()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Pet[] getPets()`：读取并返回状态/数据。
  - `public Pet getPet(int index)`：读取并返回状态/数据。
  - `public byte getPetIndex(int petId)`：读取并返回状态/数据。
  - `public byte getPetIndex(Pet pet)`：读取并返回状态/数据。
  - `public final byte getQuestStatus(final int quest)`：读取并返回状态/数据。
  - `public QuestStatus getQuest(final int quest)`：读取并返回状态/数据。
  - `public QuestStatus getQuest(Quest quest)`：读取并返回状态/数据。
  - `public final QuestStatus getQuestNAdd(final Quest quest)`：读取并返回状态/数据。
  - `public final QuestStatus getQuestNoAdd(final Quest quest)`：读取并返回状态/数据。
  - `public boolean needQuestItem(int questid, int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearSavedLocation(SavedLocationType type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int peekSavedLocation(String type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getSavedLocation(String type)`：读取并返回状态/数据。
  - `public int getSkillLevel(int skill)`：读取并返回状态/数据。
  - `public byte getSkillLevel(Skill skill)`：读取并返回状态/数据。
  - `public long getSkillExpiration(int skill)`：读取并返回状态/数据。
  - `public long getSkillExpiration(Skill skill)`：读取并返回状态/数据。
  - `public int getSlot()`：读取并返回状态/数据。
  - `public final List<QuestStatus> getStartedQuests()`：读取并返回状态/数据。
  - `public StatEffect getStatForBuff(BuffStat effect)`：读取并返回状态/数据。
  - `public Collection<Summon> getSummonsValues()`：读取并返回状态/数据。
  - `public void clearSummons()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Summon getSummonByKey(int id)`：读取并返回状态/数据。
  - `public boolean isSummonsEmpty()`：进行条件判定并返回布尔结果。
  - `public boolean containsSummon(Summon summon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObject[] getVisibleMapObjects()`：读取并返回状态/数据。
  - `public World getWorldServer()`：读取并返回状态/数据。
  - `public void giveCoolDowns(final int skillid, long starttime, long length)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int gmLevel()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void guildUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void handleEnergyChargeGain()`：处理事件/请求/消息分发。
  - `public void handleOrbconsume()`：处理事件/请求/消息分发。
  - `public boolean hasEntered(String script)`：进行条件判定并返回布尔结果。
  - `public boolean hasEntered(String script, int mapId)`：进行条件判定并返回布尔结果。
  - `public void hasGivenFame(Character to)`：进行条件判定并返回布尔结果。
  - `public boolean hasMerchant()`：进行条件判定并返回布尔结果。
  - `public boolean haveItem(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean haveCleanItem(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasEmptySlot(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean hasEmptySlot(byte invType)`：进行条件判定并返回布尔结果。
  - `public void increaseGuildCapacity()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getTimeRemaining(long timeLeft)`：读取并返回状态/数据。
  - `public boolean isBuffFrom(BuffStat stat, Skill skill)`：进行条件判定并返回布尔结果。
  - `public boolean isGmJob()`：进行条件判定并返回布尔结果。
  - `public boolean isCygnus()`：进行条件判定并返回布尔结果。
  - `public boolean isAran()`：进行条件判定并返回布尔结果。
  - `public boolean isBeginnerJob()`：进行条件判定并返回布尔结果。
  - `public boolean isGM()`：进行条件判定并返回布尔结果。
  - `public boolean isMapObjectVisible(MapObject mo)`：进行条件判定并返回布尔结果。
  - `public boolean isPartyLeader()`：进行条件判定并返回布尔结果。
  - `public boolean isGuildLeader()`：进行条件判定并返回布尔结果。
  - `public boolean attemptCatchFish(int baitLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void leaveMap()`：通用业务逻辑入口，需结合实现查看细节。
  - `private int getChangedJobSp(Job newJob)`：读取并返回状态/数据。
  - `private int getUsedSp(Job job)`：读取并返回状态/数据。
  - `private int getJobLevelSp(int level, Job job, int jobBranch)`：读取并返回状态/数据。
  - `private int getJobMaxSp(Job job)`：读取并返回状态/数据。
  - `private int getJobRemainingSp(Job job)`：读取并返回状态/数据。
  - `private int getSpGain(int spGain, Job job)`：读取并返回状态/数据。
  - `private int getSpGain(int spGain, int curSp, Job job)`：读取并返回状态/数据。
  - `private void levelUpGainSp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void levelUp(boolean takeexp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean leaveParty()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setPlayerRates()`：写入或更新状态字段。
  - `public void revertLastPlayerRates()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void revertPlayerRates()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setWorldRates()`：写入或更新状态字段。
  - `public void revertWorldRates()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applySavedRateOrElse(String type, Runnable runnable)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCouponRates()`：写入或更新状态字段。
  - `private void revertCouponRates()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateCouponRates()`：更新已有对象/配置/缓存。
  - `public void resetPlayerRates()`：通用业务逻辑入口，需结合实现查看细节。
  - `private int getCouponMultiplier(int couponId)`：读取并返回状态/数据。
  - `private void setExpCouponRate(int couponId, int couponQty)`：写入或更新状态字段。
  - `private void setDropCouponRate(int couponId, int couponQty)`：写入或更新状态字段。
  - `private void revertCouponsEffects()`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<Integer> activateCouponsEffects()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void setActiveCoupons(Collection<Item> cashItems)`：写入或更新状态字段。
  - `private void commitBuffCoupon(int couponid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispelBuffCoupons()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Set<Integer> getActiveCoupons()`：读取并返回状态/数据。
  - `public void addPlayerRing(Ring ring)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Character loadCharacterEntryFromDB(ResultSet rs, List<Item> equipped)`：从外部来源加载数据（数据库/文件/配置）。
  - `public Character generateCharacterEntry()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void loadCharSkillPoints(String[] skillPoints)`：从外部来源加载数据（数据库/文件/配置）。
  - `public int getRemainingSp()`：读取并返回状态/数据。
  - `public void updateRemainingSp(int remainingSp)`：更新已有对象/配置/缓存。
  - `public static Character fromCharactersDO(CharactersDO charactersDO, Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static CharactersDO toCharactersDO(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Character loadCharFromDB(final int cid, Client client, boolean channelServer)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void reloadQuestExpirations()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String makeMapleReadable(String in)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void message(String m)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void yellowMessage(String m)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void raiseQuestMobCount(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Mount mount(int id, int skillid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void playerDead()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unsitChairInternal()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sitChair(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void setChair(int chair)`：写入或更新状态字段。
  - `public void respawn(int returnMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void respawn(EventInstanceManager eim, int returnMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void prepareDragonBlood(final StatEffect bloodEffect)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void recalcEquipStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reapplyLocalStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void updateLocalStats()`：更新已有对象/配置/缓存。
  - `public void receivePartyMemberHP()`：接收并解码输入数据。
  - `public void removeAllCooldownsExcept(int id, boolean packet)`：删除对象、关系或临时状态。
  - `public void removeCooldown(int skillId)`：删除对象、关系或临时状态。
  - `public void removePet(Pet pet, boolean shift_left)`：删除对象、关系或临时状态。
  - `public void removeVisibleMapObject(MapObject mo)`：删除对象、关系或临时状态。
  - `public synchronized void resetStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetBattleshipHp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetEnteredScript()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetEnteredScript(int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetEnteredScript(String script)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void saveCooldowns()`：持久化当前状态到存储层。
  - `public void saveGuildStatus()`：持久化当前状态到存储层。
  - `public void saveLocationOnWarp()`：持久化当前状态到存储层。
  - `public void saveLocation(String type)`：持久化当前状态到存储层。
  - `public final boolean insertNewChar(CharacterFactoryRecipe recipe)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void saveCharToDB()`：持久化当前状态到存储层。
  - `public synchronized void saveCharToDB(boolean notAutosave)`：持久化当前状态到存储层。
  - `public void sendPolice(int greason, String reason, int duration)`：向外发送响应、消息或网络包。
  - `public void sendPolice(String text)`：向外发送响应、消息或网络包。
  - `public void sendKeymap()`：向外发送响应、消息或网络包。
  - `public void sendQuickmap()`：向外发送响应、消息或网络包。
  - `public void sendMacros()`：向外发送响应、消息或网络包。
  - `public void setBuddyCapacity(int capacity)`：写入或更新状态字段。
  - `public void setBuffedValue(BuffStat effect, int value)`：写入或更新状态字段。
  - `public void setChalkboard(String text)`：写入或更新状态字段。
  - `public void setDojoEnergy(int x)`：写入或更新状态字段。
  - `public void setEventInstance(EventInstanceManager eventInstance)`：写入或更新状态字段。
  - `public void setExp(int amount)`：写入或更新状态字段。
  - `public void setGachaExp(int exp)`：写入或更新状态字段。
  - `public void finishDojoTutorial()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setGM(int level)`：写入或更新状态字段。
  - `public void setHasMerchant(boolean set)`：写入或更新状态字段。
  - `public void addMerchantMesos(int add)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setMerchantMeso(int set)`：写入或更新状态字段。
  - `public synchronized void withdrawMerchantMesos()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hpChangeAction(int oldHp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int calcTransientRatio(float transientpoint)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int calcHpRatioUpdate(int curpoint, int maxpoint, int diffpoint)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int calcMpRatioUpdate(int curpoint, int maxpoint, int diffpoint)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyHpMpChange(int hpCon, int hpchange, int mpchange)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setMap(int PmapId)`：写入或更新状态字段。
  - `public void setMiniGamePoints(Character visitor, int winnerslot, boolean omok)`：写入或更新状态字段。
  - `public void setRPS(RockPaperScissor rps)`：写入或更新状态字段。
  - `public void closeRPS()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getDoorSlot()`：读取并返回状态/数据。
  - `public int fetchDoorSlot()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setParty(Party p)`：写入或更新状态字段。
  - `public byte getSlots(int type)`：读取并返回状态/数据。
  - `public boolean canGainSlots(int type, int slots)`：进行条件判定并返回布尔结果。
  - `public boolean gainSlots(int type, int slots)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean gainSlots(int type, int slots, boolean update)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int gainSlotsInternal(int type, int slots)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int sellAllItemsFromName(byte invTypeId, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int sellAllItemsFromPosition(ItemInformationProvider ii, InventoryType type, short pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int standaloneSell(Client c, ItemInformationProvider ii, InventoryType type, short slot, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean hasMergeFlag(Item item)`：进行条件判定并返回布尔结果。
  - `private static void setMergeFlag(Item item)`：写入或更新状态字段。
  - `private List<Equip> getUpgradeableEquipped()`：读取并返回状态/数据。
  - `private static List<Equip> getEquipsWithStat(List<Pair<Equip, Map<StatUpgrade, Short>>> equipped, StatUpgrade stat)`：读取并返回状态/数据。
  - `public boolean mergeAllItemsFromName(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mergeAllItemsFromPosition(Map<StatUpgrade, Float> statUps, short pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void standaloneMerge(Map<StatUpgrade, Float> statUps, Client c, InventoryType type, short slot, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setSlot(int slotid)`：写入或更新状态字段。
  - `public void shiftPetsRight()`：通用业务逻辑入口，需结合实现查看细节。
  - `private long getDojoTimeLeft()`：读取并返回状态/数据。
  - `public void showDojoClock()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showUnderLeveledInfo(Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showMapOwnershipInfo(Character mapOwner)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showHint(String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showHint(String msg, int length)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void silentGiveBuffs(List<Pair<Long, PlayerBuffValueHolder>> buffs)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void silentPartyUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void silentPartyUpdateInternal(Party chrParty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean skillIsCooling(int skillId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void runFullnessSchedule(int petSlot)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean runTirednessSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startMapEffect(String msg, int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startMapEffect(String msg, int itemId, int duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unEquipAllPets()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unEquipPet(Pet pet, boolean shift_left)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unEquipPet(Pet pet, boolean shift_left, boolean hunger)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateMacros(int position, SkillMacro updateMacro)`：更新已有对象/配置/缓存。
  - `public void updatePartyMemberHP()`：更新已有对象/配置/缓存。
  - `private void updatePartyMemberHPInternal()`：更新已有对象/配置/缓存。
  - `public void setQuestProgress(int id, int infoNumber, String progress)`：写入或更新状态字段。
  - `public void awardQuestPoint(int awardedPoints)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void announceUpdateQuestInternal(Character chr, Pair<DelayedQuestUpdate, Object[]> questUpdate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void announceUpdateQuest(DelayedQuestUpdate questUpdateType, Object... params)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void flushDelayedUpdateQuests()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateQuestStatus(QuestStatus qs)`：更新已有对象/配置/缓存。
  - `public void cancelQuestExpirationTask()`：进行条件判定并返回布尔结果。
  - `public void forfeitExpirableQuests()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void questExpirationTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void runQuestExpireTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerQuestExpire(Quest quest, long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void questTimeLimit(final Quest quest, int seconds)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void questTimeLimit2(final Quest quest, long expires)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateSingleStat(Stat stat, int newval)`：更新已有对象/配置/缓存。
  - `private void updateSingleStat(Stat stat, int newval, boolean itemReaction)`：更新已有对象/配置/缓存。
  - `public void sendPacket(Packet packet)`：向外发送响应、消息或网络包。
  - `public int getObjectId()`：读取并返回状态/数据。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void setObjectId(int id)`：写入或更新状态字段。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Set<NewYearCardRecord> getNewYearRecords()`：读取并返回状态/数据。
  - `public Set<NewYearCardRecord> getReceivedNewYearRecords()`：读取并返回状态/数据。
  - `public NewYearCardRecord getNewYearRecord(int cardid)`：读取并返回状态/数据。
  - `public void addNewYearRecord(NewYearCardRecord newyear)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeNewYearRecord(NewYearCardRecord newyear)`：删除对象、关系或临时状态。
  - `public void portalDelay(long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long portalDelay()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void markTeleportLikeMove()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void markTeleportLikeMove(Point beforePos, Point afterPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void markRegularMove(Point beforePos, Point afterPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getLastTeleportLikeMoveTime()`：读取并返回状态/数据。
  - `public synchronized Point getTeleportBeforePositionForDistanceCheck()`：读取并返回状态/数据。
  - `public synchronized Point getMovementBeforePositionForDistanceCheck()`：读取并返回状态/数据。
  - `public synchronized void consumeTeleportDistanceCheckContext()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void consumeMovementDistanceCheckContext()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void clearTeleportDistanceContext()`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isTeleportDistanceContextActiveLocked(long now)`：进行条件判定并返回布尔结果。
  - `private boolean isMovementDistanceContextActiveLocked(long now)`：进行条件判定并返回布尔结果。
  - `private void clearTeleportDistanceContextLocked()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void clearMovementDistanceContextLocked()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean shouldBuildTeleportDistanceContext(Point beforePos, Point afterPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean shouldBuildMovementDistanceContext(Point beforePos, Point afterPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point copyPoint(Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static long monotonicNow()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void blockPortal(String scriptName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unblockPortal(String scriptName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean containsAreaInfo(int area, String info)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateAreaInfo(int area, String info)`：更新已有对象/配置/缓存。
  - `public void autoBan(String reason)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void block(int reason, int days, String desc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Integer> getTrockMaps()`：读取并返回状态/数据。
  - `public List<Integer> getVipTrockMaps()`：读取并返回状态/数据。
  - `public int getTrockSize()`：读取并返回状态/数据。
  - `public void deleteFromTrocks(int map)`：删除对象、关系或临时状态。
  - `public void addTrockMap()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isTrockMap(int id)`：进行条件判定并返回布尔结果。
  - `public int getVipTrockSize()`：读取并返回状态/数据。
  - `public void deleteFromVipTrocks(int map)`：删除对象、关系或临时状态。
  - `public void addVipTrockMap()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isVipTrockMap(int id)`：进行条件判定并返回布尔结果。
  - `public AutobanManager getAutoBanManager()`：读取并返回状态/数据。
  - `public void setAutoBanManager(AutobanManager autoBan)`：写入或更新状态字段。
  - `public void equippedItem(Equip equip)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unequippedItem(Equip equip)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void equipPendantOfSpirit()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unequipPendantOfSpirit()`：通用业务逻辑入口，需结合实现查看细节。
  - `private Collection<Item> getUpgradeableEquipList()`：读取并返回状态/数据。
  - `public void increaseEquipExp(int expGain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showAllEquipFeatures()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMarriageMessage()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCpqTimer(ScheduledFuture<?> timer)`：写入或更新状态字段。
  - `public void clearCpqTimer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void empty(final boolean remove)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void logOff()`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getLoggedInTime()`：读取并返回状态/数据。
  - `public boolean getWhiteChat()`：读取并返回状态/数据。
  - `public void toggleWhiteChat()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean gotPartyQuestItem(String partyquestchar)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePartyQuestItem(String letter)`：删除对象、关系或临时状态。
  - `public void setPartyQuestItemObtained(String partyquestchar)`：写入或更新状态字段。
  - `public void createDragon()`：创建对象、会话或业务记录。
  - `public long getJailExpirationTimeLeft()`：读取并返回状态/数据。
  - `private void setFutureJailExpiration(long time)`：写入或更新状态字段。
  - `public void addJailExpirationTime(long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeJailExpirationTime()`：删除对象、关系或临时状态。
  - `public boolean registerNameChange(String newName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean cancelPendingNameChange()`：进行条件判定并返回布尔结果。
  - `public void doPendingNameChange()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int checkWorldTransferEligibility()`：校验输入参数或业务约束。
  - `public boolean registerWorldTransfer(int newWorld)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean cancelPendingWorldTransfer()`：进行条件判定并返回布尔结果。
  - `public String getLastCommandMessage()`：读取并返回状态/数据。
  - `public void setLastCommandMessage(String text)`：写入或更新状态字段。
  - `public int getRewardPoints()`：读取并返回状态/数据。
  - `public void setRewardPoints(int value)`：写入或更新状态字段。
  - `public void setReborns(int value)`：写入或更新状态字段。
  - `public void addReborns()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getReborns()`：读取并返回状态/数据。
  - `public void executeRebornAsId(int jobId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void executeRebornAs(Job job)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setTeam(int team)`：写入或更新状态字段。
  - `public long getLastSnowballAttack()`：读取并返回状态/数据。
  - `public void setLastSnowballAttack(long time)`：写入或更新状态字段。
  - `public void gainFestivalPoints(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCP()`：读取并返回状态/数据。
  - `public void gainCP(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setTotalCP(int a)`：写入或更新状态字段。
  - `public void setCP(int a)`：写入或更新状态字段。
  - `public int getTotalCP()`：读取并返回状态/数据。
  - `public void resetCP()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainAriantPoints(int points)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainEquip(int itemId, Short attStr, Short attDex, Short attInt, Short attLuk, Short attHp, Short attMp, Short pAtk, Short mAtk, Short pDef, Short mDef, Short acc, Short avoid, Short hands, Short speed, Short jump, Byte upgradeSlot, Long expireTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setFamilyBuff(boolean type, float exp, float drop)`：写入或更新状态字段。
  - `public void startFamilyBuffTimer(int delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelFamilyBuffTimer()`：进行条件判定并返回布尔结果。
  - `public int getCurrentOnlineTime()`：读取并返回状态/数据。
  - `public void setCurrentOnlineTime(final int iTime)`：写入或更新状态字段。
  - `public void updateOnlineTime()`：更新已有对象/配置/缓存。
  - `public MapleMap getMap(int mapid, boolean showMsg)`：读取并返回状态/数据。
  - `public void enableActions()`：通用业务逻辑入口，需结合实现查看细节。

## `client/CharacterListener.java`

- `class CharacterListener`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CharacterListener(Character character)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void onHpChanged(int oldHp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void onHpMpPoolUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void onStatUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void onAnnounceStatPoolUpdate()`：通用业务逻辑入口，需结合实现查看细节。

## `client/CharacterNameAndId.java`

- `class CharacterNameAndId`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CharacterNameAndId(int id, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。

## `client/Client.java`

- `class Client`：领域类型或功能模块，职责由同名文件实现定义。
- `enum Type`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Client(Type type, long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Client createLoginClient(long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)`：创建对象、会话或业务记录。
  - `updateLastPacket()`：更新已有对象/配置/缓存。
  - `closeMapleSession()`：通用业务逻辑入口，需结合实现查看细节。
  - `return getChannelServer().getEventSM().getEventManager(event)`：读取并返回状态/数据。
  - `try (Connection con = DatabaseConnection.getConnection(); PreparedStatement ps = con.prepareStatement("SELECT id, name FROM characters WHERE accountid = ? AND world = ?"))`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (Connection con = DatabaseConnection.getConnection(); PreparedStatement ps = con.prepareStatement("SELECT hwid FROM accounts WHERE id = ?"))`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (PreparedStatement ps = con.prepareStatement("SELECT filter FROM macfilters"); ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `getWorldServer().removePlayerHpDecrease(player)`：读取并返回状态/数据。
  - `clear()`：通用业务逻辑入口，需结合实现查看细节。
  - `getChannelServer().removePlayer(player)`：读取并返回状态/数据。

## `client/DefaultDates.java`

  - `private DefaultDates()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static LocalDate getBirthday()`：读取并返回状态/数据。
  - `public static LocalDateTime getTempban()`：读取并返回状态/数据。

## `client/Disease.java`

- `enum Disease`：领域类型或功能模块，职责由同名文件实现定义。
  - `NULL(0x0),`：通用业务逻辑入口，需结合实现查看细节。
  - `SLOW(0x1, MobSkillType.SLOW),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEDUCE(0x80, MobSkillType.SEDUCE),`：通用业务逻辑入口，需结合实现查看细节。
  - `FISHABLE(0x100),`：通用业务逻辑入口，需结合实现查看细节。
  - `ZOMBIFY(0x4000),`：通用业务逻辑入口，需结合实现查看细节。
  - `CONFUSE(0x80000, MobSkillType.REVERSE_INPUT),`：通用业务逻辑入口，需结合实现查看细节。
  - `STUN(0x2000000000000L, MobSkillType.STUN),`：通用业务逻辑入口，需结合实现查看细节。
  - `POISON(0x4000000000000L, MobSkillType.POISON),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEAL(0x8000000000000L, MobSkillType.SEAL),`：通用业务逻辑入口，需结合实现查看细节。
  - `DARKNESS(0x10000000000000L, MobSkillType.DARKNESS),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAKEN(0x4000000000000000L, MobSkillType.WEAKNESS),`：通用业务逻辑入口，需结合实现查看细节。
  - `CURSE(0x8000000000000000L, MobSkillType.CURSE)`：通用业务逻辑入口，需结合实现查看细节。
  - `Disease(long i)`：通用业务逻辑入口，需结合实现查看细节。
  - `Disease(long i, MobSkillType skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getValue()`：读取并返回状态/数据。
  - `public boolean isFirst()`：进行条件判定并返回布尔结果。
  - `public MobSkillType getMobSkillType()`：读取并返回状态/数据。
  - `public static Disease ordinal(int ord)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static final Disease getRandom()`：读取并返回状态/数据。
  - `public static final Disease getBySkill(MobSkillType skill)`：读取并返回状态/数据。

## `client/DiseaseValueHolder.java`

- `class DiseaseValueHolder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public DiseaseValueHolder(long start, long length)`：通用业务逻辑入口，需结合实现查看细节。

## `client/Family.java`

- `class Family`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Family(int id, int world)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean idInUse(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getID()`：读取并返回状态/数据。
  - `public int getWorld()`：读取并返回状态/数据。
  - `public void setLeader(FamilyEntry leader)`：写入或更新状态字段。
  - `public FamilyEntry getLeader()`：读取并返回状态/数据。
  - `private void setName(String name)`：写入或更新状态字段。
  - `public int getTotalMembers()`：读取并返回状态/数据。
  - `public int getTotalGenerations()`：读取并返回状态/数据。
  - `public void setTotalGenerations(int generations)`：写入或更新状态字段。
  - `public String getName()`：读取并返回状态/数据。
  - `public void setMessage(String message, boolean save)`：写入或更新状态字段。
  - `public String getMessage()`：读取并返回状态/数据。
  - `public void addEntry(FamilyEntry entry)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeEntryBranch(FamilyEntry root)`：删除对象、关系或临时状态。
  - `public void addEntryTree(FamilyEntry root)`：通用业务逻辑入口，需结合实现查看细节。
  - `public FamilyEntry getEntryByID(int cid)`：读取并返回状态/数据。
  - `public void broadcast(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcast(Packet packet, int ignoreID)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void Familybuff(int duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastFamilyInfoUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetDailyReps()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void saveAllMembersRep()`：持久化当前状态到存储层。

## `client/FamilyEntitlement.java`

- `enum FamilyEntitlement`：领域类型或功能模块，职责由同名文件实现定义。
  - `FAMILY_REUINION(1, 300, I18nUtil.getMessage("FamilyEntitlement.message1"), I18nUtil.getMessage("FamilyEntitlement.message2")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON_FAMILY(1, 500, I18nUtil.getMessage("FamilyEntitlement.message3"), I18nUtil.getMessage("FamilyEntitlement.message4")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_DROP_1_5(1, 700, I18nUtil.getMessage("FamilyEntitlement.message5"), I18nUtil.getMessage("FamilyEntitlement.message6")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_EXP_1_5(1, 800, I18nUtil.getMessage("FamilyEntitlement.message7"), I18nUtil.getMessage("FamilyEntitlement.message8")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_BONDING(1, 1000, I18nUtil.getMessage("FamilyEntitlement.message9"), I18nUtil.getMessage("FamilyEntitlement.message10")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_DROP_2(1, 1200, I18nUtil.getMessage("FamilyEntitlement.message11"), I18nUtil.getMessage("FamilyEntitlement.message12")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_EXP_2(1, 1500, I18nUtil.getMessage("FamilyEntitlement.message13"), I18nUtil.getMessage("FamilyEntitlement.message14")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_DROP_2_30MIN(1, 2000, I18nUtil.getMessage("FamilyEntitlement.message15"), I18nUtil.getMessage("FamilyEntitlement.message16")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SELF_EXP_2_30MIN(1, 2500, I18nUtil.getMessage("FamilyEntitlement.message17"), I18nUtil.getMessage("FamilyEntitlement.message18")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_DROP_2_30MIN(1, 4000, I18nUtil.getMessage("FamilyEntitlement.message19"), I18nUtil.getMessage("FamilyEntitlement.message20")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_EXP_2_30MIN(1, 5000, I18nUtil.getMessage("FamilyEntitlement.message21"), I18nUtil.getMessage("FamilyEntitlement.message22"))`：通用业务逻辑入口，需结合实现查看细节。
  - `FamilyEntitlement(int usageLimit, int repCost, String name, String description)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getUsageLimit()`：读取并返回状态/数据。
  - `public int getRepCost()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public String getDescription()`：读取并返回状态/数据。

## `client/FamilyEntry.java`

- `class FamilyEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FamilyEntry(Family family, int characterID, String charName, int level, Job job)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getChr()`：读取并返回状态/数据。
  - `public void setCharacter(Character newCharacter)`：写入或更新状态字段。
  - `private void cacheOffline(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void join(FamilyEntry senior)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void fork()`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized boolean updateNewFamilyDB(Connection con)`：更新已有对象/配置/缓存。
  - `private static boolean updateFamilyEntryDB(Connection con, int cid, int familyid)`：更新已有对象/配置/缓存。
  - `private synchronized void addSeniorCount(int seniorCount, Family newFamily)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void addJuniorCount(int juniorCount)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Family getFamily()`：读取并返回状态/数据。
  - `public int getChrId()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public Job getJob()`：读取并返回状态/数据。
  - `public int getReputation()`：读取并返回状态/数据。
  - `public int getTodaysRep()`：读取并返回状态/数据。
  - `public void setReputation(int reputation)`：写入或更新状态字段。
  - `public void setTodaysRep(int today)`：写入或更新状态字段。
  - `public int getRepsToSenior()`：读取并返回状态/数据。
  - `public void setRepsToSenior(int reputation)`：写入或更新状态字段。
  - `public void gainReputation(int gain, boolean countTowardsTotal)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void gainReputation(int gain, boolean countTowardsTotal, FamilyEntry from)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveReputationToSenior(int gain, boolean includeSuperSenior)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getTotalReputation()`：读取并返回状态/数据。
  - `public void setTotalReputation(int totalReputation)`：写入或更新状态字段。
  - `public FamilyEntry getSenior()`：读取并返回状态/数据。
  - `public synchronized boolean setSenior(FamilyEntry senior, boolean save)`：写入或更新状态字段。
  - `private static boolean updateDBChangeFamily(int cid, int familyid, int seniorid)`：更新已有对象/配置/缓存。
  - `private static boolean updateDBChangeFamily(Connection con, int cid, int familyid, int seniorid)`：更新已有对象/配置/缓存。
  - `private static boolean updateCharacterFamilyDB(Connection con, int charid, int familyid, boolean fork)`：更新已有对象/配置/缓存。
  - `public List<FamilyEntry> getJuniors()`：读取并返回状态/数据。
  - `public FamilyEntry getOtherJunior(FamilyEntry junior)`：读取并返回状态/数据。
  - `public int getJuniorCount()`：读取并返回状态/数据。
  - `public synchronized boolean addJunior(FamilyEntry newJunior)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized boolean isJunior(FamilyEntry entry)`：进行条件判定并返回布尔结果。
  - `public synchronized boolean removeJunior(FamilyEntry junior)`：删除对象、关系或临时状态。
  - `public int getTotalSeniors()`：读取并返回状态/数据。
  - `public void setTotalSeniors(int totalSeniors)`：写入或更新状态字段。
  - `public int getTotalJuniors()`：读取并返回状态/数据。
  - `public void setTotalJuniors(int totalJuniors)`：写入或更新状态字段。
  - `public void announceToSenior(Packet packet, boolean includeSuperSenior)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateSeniorFamilyInfo(boolean includeSuperSenior)`：更新已有对象/配置/缓存。
  - `public synchronized void doFullCount()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean useEntitlement(FamilyEntitlement entitlement)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean refundEntitlement(FamilyEntitlement entitlement)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isEntitlementUsed(FamilyEntitlement entitlement)`：进行条件判定并返回布尔结果。
  - `public int getEntitlementUsageCount(FamilyEntitlement entitlement)`：读取并返回状态/数据。
  - `public void setEntitlementUsed(int id)`：写入或更新状态字段。
  - `public void resetEntitlementUsages()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean saveReputation()`：持久化当前状态到存储层。
  - `public boolean saveReputation(Connection con)`：持久化当前状态到存储层。
  - `public void savedSuccessfully()`：持久化当前状态到存储层。

## `client/Job.java`

- `enum Job`：领域类型或功能模块，职责由同名文件实现定义。
  - `BEGINNER(0, I18nUtil.getMessage("job.name.0")),`：通用业务逻辑入口，需结合实现查看细节。
  - `WARRIOR(100, I18nUtil.getMessage("job.name.100")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FIGHTER(110, I18nUtil.getMessage("job.name.110")), CRUSADER(111, I18nUtil.getMessage("job.name.111")), HERO(112, I18nUtil.getMessage("job.name.112")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PAGE(120, I18nUtil.getMessage("job.name.120")), WHITEKNIGHT(121, I18nUtil.getMessage("job.name.121")), PALADIN(122,  I18nUtil.getMessage("job.name.122")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEARMAN(130,  I18nUtil.getMessage("job.name.130")), DRAGONKNIGHT(131,  I18nUtil.getMessage("job.name.131")), DARKKNIGHT(132, I18nUtil.getMessage("job.name.132")),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGICIAN(200, I18nUtil.getMessage("job.name.200")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FP_WIZARD(210, I18nUtil.getMessage("job.name.210")), FP_MAGE(211, I18nUtil.getMessage("job.name.211")), FP_ARCHMAGE(212, I18nUtil.getMessage("job.name.212")),`：通用业务逻辑入口，需结合实现查看细节。
  - `IL_WIZARD(220, I18nUtil.getMessage("job.name.220")), IL_MAGE(221, I18nUtil.getMessage("job.name.221")), IL_ARCHMAGE(222, I18nUtil.getMessage("job.name.222")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CLERIC(230, I18nUtil.getMessage("job.name.230")), PRIEST(231, I18nUtil.getMessage("job.name.231")), BISHOP(232, I18nUtil.getMessage("job.name.232")),`：通用业务逻辑入口，需结合实现查看细节。
  - `BOWMAN(300, I18nUtil.getMessage("job.name.300")),`：通用业务逻辑入口，需结合实现查看细节。
  - `HUNTER(310, I18nUtil.getMessage("job.name.310")), RANGER(311, I18nUtil.getMessage("job.name.311")), BOWMASTER(312, I18nUtil.getMessage("job.name.312")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CROSSBOWMAN(320, I18nUtil.getMessage("job.name.320")), SNIPER(321, I18nUtil.getMessage("job.name.321")), MARKSMAN(322, I18nUtil.getMessage("job.name.322")),`：通用业务逻辑入口，需结合实现查看细节。
  - `THIEF(400, I18nUtil.getMessage("job.name.400")),`：通用业务逻辑入口，需结合实现查看细节。
  - `ASSASSIN(410,I18nUtil.getMessage("job.name.410")), HERMIT(411, I18nUtil.getMessage("job.name.411")), NIGHTLORD(412, I18nUtil.getMessage("job.name.412")),`：通用业务逻辑入口，需结合实现查看细节。
  - `BANDIT(420, I18nUtil.getMessage("job.name.420")), CHIEFBANDIT(421, I18nUtil.getMessage("job.name.421")), SHADOWER(422, I18nUtil.getMessage("job.name.422")),`：通用业务逻辑入口，需结合实现查看细节。
  - `PIRATE(500, I18nUtil.getMessage("job.name.500")),`：通用业务逻辑入口，需结合实现查看细节。
  - `BRAWLER(510, I18nUtil.getMessage("job.name.510")), MARAUDER(511, I18nUtil.getMessage("job.name.511")), BUCCANEER(512, I18nUtil.getMessage("job.name.512")),`：通用业务逻辑入口，需结合实现查看细节。
  - `GUNSLINGER(520, I18nUtil.getMessage("job.name.520")), OUTLAW(521, I18nUtil.getMessage("job.name.521")), CORSAIR(522, I18nUtil.getMessage("job.name.522")),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLELEAF_BRIGADIER(800, I18nUtil.getMessage("job.name.800")),`：通用业务逻辑入口，需结合实现查看细节。
  - `GM(900, I18nUtil.getMessage("job.name.900")), SUPERGM(910, I18nUtil.getMessage("job.name.910")),`：通用业务逻辑入口，需结合实现查看细节。
  - `NOBLESSE(1000, I18nUtil.getMessage("job.name.1000")),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAWNWARRIOR1(1100, I18nUtil.getMessage("job.name.1100")), DAWNWARRIOR2(1110, I18nUtil.getMessage("job.name.1110")), DAWNWARRIOR3(1111, I18nUtil.getMessage("job.name.1111")), DAWNWARRIOR4(1112, I18nUtil.getMessage("job.name.1112")),`：通用业务逻辑入口，需结合实现查看细节。
  - `BLAZEWIZARD1(1200, I18nUtil.getMessage("job.name.1200")), BLAZEWIZARD2(1210, I18nUtil.getMessage("job.name.1210")), BLAZEWIZARD3(1211,I18nUtil.getMessage("job.name.1211")), BLAZEWIZARD4(1212,I18nUtil.getMessage("job.name.1212")),`：通用业务逻辑入口，需结合实现查看细节。
  - `WINDARCHER1(1300,I18nUtil.getMessage("job.name.1300")), WINDARCHER2(1310, I18nUtil.getMessage("job.name.1310")), WINDARCHER3(1311, I18nUtil.getMessage("job.name.1311")), WINDARCHER4(1312, I18nUtil.getMessage("job.name.1312")),`：通用业务逻辑入口，需结合实现查看细节。
  - `NIGHTWALKER1(1400,I18nUtil.getMessage("job.name.1400")), NIGHTWALKER2(1410,I18nUtil.getMessage("job.name.1410")), NIGHTWALKER3(1411,I18nUtil.getMessage("job.name.1411")), NIGHTWALKER4(1412,I18nUtil.getMessage("job.name.1412")),`：通用业务逻辑入口，需结合实现查看细节。
  - `THUNDERBREAKER1(1500,I18nUtil.getMessage("job.name.1500")), THUNDERBREAKER2(1510,I18nUtil.getMessage("job.name.1510")), THUNDERBREAKER3(1511,I18nUtil.getMessage("job.name.1511")), THUNDERBREAKER4(1512,I18nUtil.getMessage("job.name.1512")),`：通用业务逻辑入口，需结合实现查看细节。
  - `LEGEND(2000, I18nUtil.getMessage("job.name.2000")), EVAN(2001, I18nUtil.getMessage("job.name.2001")),`：通用业务逻辑入口，需结合实现查看细节。
  - `ARAN1(2100, I18nUtil.getMessage("job.name.2100")), ARAN2(2110, I18nUtil.getMessage("job.name.2110")), ARAN3(2111, I18nUtil.getMessage("job.name.2111")), ARAN4(2112, I18nUtil.getMessage("job.name.2112")),`：通用业务逻辑入口，需结合实现查看细节。
  - `EVAN1(2200,I18nUtil.getMessage("job.name.2200")), EVAN2(2210, I18nUtil.getMessage("job.name.2210")), EVAN3(2211, I18nUtil.getMessage("job.name.2211")), EVAN4(2212, I18nUtil.getMessage("job.name.2212")), EVAN5(2213, I18nUtil.getMessage("job.name.2213")), EVAN6(2214, I18nUtil.getMessage("job.name.2214")),`：通用业务逻辑入口，需结合实现查看细节。
  - `EVAN7(2215, I18nUtil.getMessage("job.name.2215")), EVAN8(2216, I18nUtil.getMessage("job.name.2216")), EVAN9(2217, I18nUtil.getMessage("job.name.2217")), EVAN10(2218, I18nUtil.getMessage("job.name.2218"))`：通用业务逻辑入口，需结合实现查看细节。
  - `Job(int id, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int getMax()`：读取并返回状态/数据。
  - `public static Job getById(int id)`：读取并返回状态/数据。
  - `public static Job getBy5ByteEncoding(int encoded)`：读取并返回状态/数据。
  - `public boolean isA(Job basejob)`：进行条件判定并返回布尔结果。
  - `public int getJobNiche()`：读取并返回状态/数据。
  - `public static Job getJobStyleInternal(int jobid, byte opt)`：读取并返回状态/数据。

## `client/MonsterBook.java`

- `class MonsterBook`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterBook(int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addCard(final Client c, final int cardid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void calculateLevel()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getBookLevel()`：读取并返回状态/数据。
  - `public int getTotalCards()`：读取并返回状态/数据。
  - `public int getNormalCard()`：读取并返回状态/数据。
  - `public int getSpecialCard()`：读取并返回状态/数据。
  - `public void loadCards(final int chrId)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void saveCards(Connection con, int chrId) throws SQLException`：持久化当前状态到存储层。
  - `public static int[] getCardTierSize()`：读取并返回状态/数据。

## `client/Mount.java`

- `class Mount`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Mount(Character owner, int id, int skillid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public int getSkillId()`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。
  - `public int getTiredness()`：读取并返回状态/数据。
  - `public int getExp()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public void setTiredness(int newtiredness)`：写入或更新状态字段。
  - `public int incrementAndGetTiredness()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setExp(int newexp)`：写入或更新状态字段。
  - `public void setLevel(int newlevel)`：写入或更新状态字段。
  - `public void setItemId(int newitemid)`：写入或更新状态字段。
  - `public void setSkillId(int newskillid)`：写入或更新状态字段。
  - `public void setActive(boolean set)`：写入或更新状态字段。
  - `public boolean isActive()`：进行条件判定并返回布尔结果。
  - `public void empty()`：通用业务逻辑入口，需结合实现查看细节。

## `client/QuestStatus.java`

- `class QuestStatus`：领域类型或功能模块，职责由同名文件实现定义。
- `enum Status`：领域类型或功能模块，职责由同名文件实现定义。
  - `public QuestStatus(Quest quest, Status status)`：通用业务逻辑入口，需结合实现查看细节。
  - `public QuestStatus(Quest quest, Status status, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Quest getQuest()`：读取并返回状态/数据。
  - `public short getQuestID()`：读取并返回状态/数据。
  - `public Status getStatus()`：读取并返回状态/数据。
  - `public final void setStatus(Status status)`：写入或更新状态字段。
  - `public int getNpc()`：读取并返回状态/数据。
  - `public final void setNpc(int npc)`：写入或更新状态字段。
  - `private void registerMobs()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean addMedalMap(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMedalProgress()`：读取并返回状态/数据。
  - `public List<Integer> getMedalMaps()`：读取并返回状态/数据。
  - `public boolean progress(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setProgress(int id, String pr)`：写入或更新状态字段。
  - `public boolean madeProgress()`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getProgress(int id)`：读取并返回状态/数据。
  - `public void resetProgress(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetAllProgress()`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getInfoNumber()`：读取并返回状态/数据。
  - `public String getInfoEx(int index)`：读取并返回状态/数据。
  - `public List<String> getInfoEx()`：读取并返回状态/数据。
  - `public long getCompletionTime()`：读取并返回状态/数据。
  - `public void setCompletionTime(long completionTime)`：写入或更新状态字段。
  - `public long getExpirationTime()`：读取并返回状态/数据。
  - `public void setExpirationTime(long expirationTime)`：写入或更新状态字段。
  - `public int getForfeited()`：读取并返回状态/数据。
  - `public int getCompleted()`：读取并返回状态/数据。
  - `public void setForfeited(int forfeited)`：写入或更新状态字段。
  - `public void setCompleted(int completed)`：写入或更新状态字段。
  - `public final void setCustomData(final String customData)`：写入或更新状态字段。
  - `public final String getCustomData()`：读取并返回状态/数据。
  - `public String getProgressData()`：读取并返回状态/数据。

## `client/Ring.java`

- `class Ring`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Ring(int id, int id2, int partnerId, int itemid, String partnername)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Ring loadFromDb(int ringId)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static void removeRing(final Ring ring)`：删除对象、关系或临时状态。
  - `public int getRingId()`：读取并返回状态/数据。
  - `public int getPartnerRingId()`：读取并返回状态/数据。
  - `public int getPartnerChrId()`：读取并返回状态/数据。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public String getPartnerName()`：读取并返回状态/数据。
  - `public boolean equipped()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void equip()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unequip()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean equals(Object o)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public int compareTo(Ring other)`：通用业务逻辑入口，需结合实现查看细节。

## `client/Skill.java`

- `class Skill`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Skill(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public StatEffect getEffect(int level)`：读取并返回状态/数据。
  - `public int getMaxLevel()`：读取并返回状态/数据。
  - `public boolean isFourthJob()`：进行条件判定并返回布尔结果。
  - `public void setElement(Element elem)`：写入或更新状态字段。
  - `public Element getElement()`：读取并返回状态/数据。
  - `public int getAnimationTime()`：读取并返回状态/数据。
  - `public void setAnimationTime(int time)`：写入或更新状态字段。
  - `public void incAnimationTime(int time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isBeginnerSkill()`：进行条件判定并返回布尔结果。
  - `public void setAction(boolean act)`：写入或更新状态字段。
  - `public boolean getAction()`：读取并返回状态/数据。
  - `public void addLevelEffect(StatEffect effect)`：通用业务逻辑入口，需结合实现查看细节。

## `client/SkillFactory.java`

- `class SkillFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Skill getSkill(int id)`：读取并返回状态/数据。
  - `public static void loadAllSkills()`：从外部来源加载数据（数据库/文件/配置）。
  - `private static Skill loadFromData(int id, Data data)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static String getSkillName(int skillid)`：读取并返回状态/数据。

## `client/SkillMacro.java`

- `class SkillMacro`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SkillMacro(int skill1, int skill2, int skill3, String name, int shout, int position)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getSkill1()`：读取并返回状态/数据。
  - `public int getSkill2()`：读取并返回状态/数据。
  - `public int getSkill3()`：读取并返回状态/数据。
  - `public void setSkill1(int skill)`：写入或更新状态字段。
  - `public void setSkill2(int skill)`：写入或更新状态字段。
  - `public void setSkill3(int skill)`：写入或更新状态字段。
  - `public String getName()`：读取并返回状态/数据。
  - `public int getShout()`：读取并返回状态/数据。
  - `public int getPosition()`：读取并返回状态/数据。

## `client/SkinColor.java`

- `enum SkinColor`：领域类型或功能模块，职责由同名文件实现定义。
  - `NORMAL(0),`：通用业务逻辑入口，需结合实现查看细节。
  - `DARK(1),`：通用业务逻辑入口，需结合实现查看细节。
  - `BLACK(2),`：通用业务逻辑入口，需结合实现查看细节。
  - `PALE(3),`：通用业务逻辑入口，需结合实现查看细节。
  - `BLUE(4),`：通用业务逻辑入口，需结合实现查看细节。
  - `GREEN(5),`：通用业务逻辑入口，需结合实现查看细节。
  - `WHITE(9),`：通用业务逻辑入口，需结合实现查看细节。
  - `PINK(10)`：通用业务逻辑入口，需结合实现查看细节。
  - `SkinColor(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public static SkinColor getById(int id)`：读取并返回状态/数据。

## `client/Stat.java`

- `enum Stat`：领域类型或功能模块，职责由同名文件实现定义。
  - `SKIN(0x1),`：通用业务逻辑入口，需结合实现查看细节。
  - `FACE(0x2),`：通用业务逻辑入口，需结合实现查看细节。
  - `HAIR(0x4),`：通用业务逻辑入口，需结合实现查看细节。
  - `LEVEL(0x10),`：通用业务逻辑入口，需结合实现查看细节。
  - `JOB(0x20),`：通用业务逻辑入口，需结合实现查看细节。
  - `STR(0x40),`：通用业务逻辑入口，需结合实现查看细节。
  - `DEX(0x80),`：通用业务逻辑入口，需结合实现查看细节。
  - `INT(0x100),`：通用业务逻辑入口，需结合实现查看细节。
  - `LUK(0x200),`：通用业务逻辑入口，需结合实现查看细节。
  - `HP(0x400),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAXHP(0x800),`：通用业务逻辑入口，需结合实现查看细节。
  - `MP(0x1000),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAXMP(0x2000),`：通用业务逻辑入口，需结合实现查看细节。
  - `AVAILABLEAP(0x4000),`：通用业务逻辑入口，需结合实现查看细节。
  - `AVAILABLESP(0x8000),`：通用业务逻辑入口，需结合实现查看细节。
  - `EXP(0x10000),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAME(0x20000),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO(0x40000),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET(0x180008),`：通用业务逻辑入口，需结合实现查看细节。
  - `GACHAEXP(0x200000)`：通用业务逻辑入口，需结合实现查看细节。
  - `Stat(int i)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getValue()`：读取并返回状态/数据。
  - `public static Stat getByValue(int value)`：读取并返回状态/数据。
  - `public static Stat getBy5ByteEncoding(int encoded)`：读取并返回状态/数据。
  - `public static Stat getByString(String type)`：读取并返回状态/数据。

## `client/autoban/AutobanFactory.java`

- `enum AutobanFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `MOB_COUNT(I18nUtil.getMessage("autoban.name.MOB_COUNT")),`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL(I18nUtil.getMessage("autoban.name.GENERAL")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FIX_DAMAGE(I18nUtil.getMessage("autoban.name.FIX_DAMAGE")),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAMAGE_HACK(I18nUtil.getMessage("autoban.name.DAMAGE_HACK"), 15, MINUTES.toMillis(1)),`：通用业务逻辑入口，需结合实现查看细节。
  - `DISTANCE_HACK(I18nUtil.getMessage("autoban.name.DISTANCE_HACK"), 10, MINUTES.toMillis(2)),`：通用业务逻辑入口，需结合实现查看细节。
  - `PORTAL_DISTANCE(I18nUtil.getMessage("autoban.name.PORTAL_DISTANCE"), 5, SECONDS.toMillis(30)),`：通用业务逻辑入口，需结合实现查看细节。
  - `PACKET_EDIT(I18nUtil.getMessage("autoban.name.PACKET_EDIT")),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACC_HACK(I18nUtil.getMessage("autoban.name.ACC_HACK")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CREATION_GENERATOR(I18nUtil.getMessage("autoban.name.CREATION_GENERATOR")),`：通用业务逻辑入口，需结合实现查看细节。
  - `HIGH_HP_HEALING(I18nUtil.getMessage("autoban.name.HIGH_HP_HEALING")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAST_HP_HEALING(I18nUtil.getMessage("autoban.name.FAST_HP_HEALING"), 15),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAST_MP_HEALING(I18nUtil.getMessage("autoban.name.FAST_MP_HEALING"), 20, SECONDS.toMillis(30)),`：通用业务逻辑入口，需结合实现查看细节。
  - `GACHA_EXP(I18nUtil.getMessage("autoban.name.GACHA_EXP")),`：通用业务逻辑入口，需结合实现查看细节。
  - `TUBI(I18nUtil.getMessage("autoban.name.TUBI"), 20, SECONDS.toMillis(15)),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHORT_ITEM_VAC(I18nUtil.getMessage("autoban.name.SHORT_ITEM_VAC")),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_VAC(I18nUtil.getMessage("autoban.name.ITEM_VAC")),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAST_ITEM_PICKUP(I18nUtil.getMessage("autoban.name.FAST_ITEM_PICKUP"), 5, SECONDS.toMillis(30)),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAST_ATTACK(I18nUtil.getMessage("autoban.name.FAST_ATTACK"), 10, SECONDS.toMillis(30)),`：通用业务逻辑入口，需结合实现查看细节。
  - `MPCON(I18nUtil.getMessage("autoban.name.MPCON"), 25, SECONDS.toMillis(30)),`：通用业务逻辑入口，需结合实现查看细节。
  - `ATTACK_INTERVAL(I18nUtil.getMessage("autoban.name.ATTACK_INTERVAL"), 60, SECONDS.toMillis(60))`：通用业务逻辑入口，需结合实现查看细节。
  - `AutobanFactory(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `AutobanFactory(String name, int points)`：通用业务逻辑入口，需结合实现查看细节。
  - `AutobanFactory(String name, int points, long expire)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMaximum()`：读取并返回状态/数据。
  - `public long getExpire()`：读取并返回状态/数据。
  - `public static void initConfig(Map<String, AutobanConfigDO> configs)`：初始化模块、资源或运行时状态。
  - `public static void updateConfig(String type, AutobanConfigDO config)`：更新已有对象/配置/缓存。
  - `public static AutobanConfigDO getConfig(String type)`：读取并返回状态/数据。
  - `public int getEffectivePoints()`：读取并返回状态/数据。
  - `public long getEffectiveExpiretime()`：读取并返回状态/数据。
  - `public boolean isDisabled()`：进行条件判定并返回布尔结果。
  - `public void addPoint(AutobanManager ban, String reason)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void alert(Character chr, String reason)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void autoban(Character chr, String value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean toggleIgnored(int chrId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isIgnored(int chrId)`：进行条件判定并返回布尔结果。
  - `public static Collection<Integer> getIgnoredChrIds()`：读取并返回状态/数据。

## `client/autoban/AutobanManager.java`

- `class AutobanManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AutobanManager(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addPoint(AutobanFactory fac, String reason)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMiss()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMisses()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spam(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spam(int type, int timestamp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getLastSpam(int type)`：读取并返回状态/数据。
  - `public void setTimestamp(int type, int time, int times)`：写入或更新状态字段。

## `client/command/Command.java`

- `class Command`：领域类型或功能模块，职责由同名文件实现定义。
  - `public abstract void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected String joinStringFrom(String[] arr, int start)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/CommandsExecutor.java`

- `class CommandsExecutor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean isCommand(Client client, String content)`：进行条件判定并返回布尔结果。
  - `public void loadCommandsExecutor()`：从外部来源加载数据（数据库/文件/配置）。
  - `public void handle(Client client, String message)`：处理事件/请求/消息分发。
  - `private void handleInternal(Client client, String message)`：处理事件/请求/消息分发。
  - `private void addCommandInfo(String name, Class<? extends Command> commandClass)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addCommand(String[] syntaxs, Class<? extends Command> commandClass)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addCommand(String syntax, Class<? extends Command> commandClass)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addCommand(String[] surtaxes, int rank, Class<? extends Command> commandClass)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addCommand(String syntax, int rank, Class<? extends Command> commandClass)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv0Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv1Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv2Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv3Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv4Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv5Commands()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLv6Commands()`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/ChangeLanguageCommand.java`

- `class ChangeLanguageCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/DisposeCommand.java`

- `class DisposeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/DropLimitCommand.java`

- `class DropLimitCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/EnableAuthCommand.java`

- `class EnableAuthCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/EquipLvCommand.java`

- `class EquipLvCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/GachaCommand.java`

- `class GachaCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/GmCommand.java`

- `class GmCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/HelpCommand.java`

- `class HelpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/JoinEventCommand.java`

- `class JoinEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/LeaveEventCommand.java`

- `class LeaveEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/MapOwnerClaimCommand.java`

- `class MapOwnerClaimCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/OnlineCommand.java`

- `class OnlineCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/RanksCommand.java`

- `class RanksCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/RatesCommand.java`

- `class RatesCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/ReadPointsCommand.java`

- `class ReadPointsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/ReportBugCommand.java`

- `class ReportBugCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/ShowRatesCommand.java`

- `class ShowRatesCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/StaffCommand.java`

- `class StaffCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/StatDexCommand.java`

- `class StatDexCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/StatIntCommand.java`

- `class StatIntCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/StatLukCommand.java`

- `class StatLukCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/StatStrCommand.java`

- `class StatStrCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/TimeCommand.java`

- `class TimeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/ToggleExpCommand.java`

- `class ToggleExpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm0/UptimeCommand.java`

- `class UptimeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/BossHpCommand.java`

- `class BossHpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/BuffMeCommand.java`

- `class BuffMeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/GotoCommand.java`

- `class GotoCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static void sortGotoEntries(List<Entry<String, Integer>> listEntries)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/MobHpCommand.java`

- `class MobHpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/WhatDropsFromCommand.java`

- `class WhatDropsFromCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm1/WhoDropsCommand.java`

- `class WhoDropsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ApCommand.java`

- `class ApCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/BombCommand.java`

- `class BombCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/BuffCommand.java`

- `class BuffCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/BuffMapCommand.java`

- `class BuffMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ClearDropsCommand.java`

- `class ClearDropsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ClearSavedLocationsCommand.java`

- `class ClearSavedLocationsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ClearSlotCommand.java`

- `class ClearSlotCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeSlot(Client c, InventoryType type, int slot)`：删除对象、关系或临时状态。

## `client/command/commands/gm2/DcCommand.java`

- `class DcCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/EmpowerMeCommand.java`

- `class EmpowerMeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/GachaListCommand.java`

- `class GachaListCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/GmShopCommand.java`

- `class GmShopCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/HealCommand.java`

- `class HealCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/HideCommand.java`

- `class HideCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/IdCommand.java`

- `class IdCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `private record HandbookItem(String id, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void execute(Client client, final String[] params)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void populateIdMap(String type) throws IdTypeNotSupportedException, IOException`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ItemCommand.java`

- `class ItemCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ItemDropCommand.java`

- `class ItemDropCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/JailCommand.java`

- `class JailCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/JobCommand.java`

- `class JobCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/LevelCommand.java`

- `class LevelCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/LevelProCommand.java`

- `class LevelProCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/LootCommand.java`

- `class LootCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/MaxSkillCommand.java`

- `class MaxSkillCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/MaxStatCommand.java`

- `class MaxStatCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/MobSkillCommand.java`

- `class MobSkillCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ReachCommand.java`

- `class ReachCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/RechargeCommand.java`

- `class RechargeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/ResetSkillCommand.java`

- `class ResetSkillCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/SearchCommand.java`

- `class SearchCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/SetSlotCommand.java`

- `class SetSlotCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/SetStatCommand.java`

- `class SetStatCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/SpCommand.java`

- `class SpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/SummonCommand.java`

- `class SummonCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/UnBugCommand.java`

- `class UnBugCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/UnHideCommand.java`

- `class UnHideCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/UnJailCommand.java`

- `class UnJailCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/WarpAreaCommand.java`

- `class WarpAreaCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/WarpCommand.java`

- `class WarpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/WarpMapCommand.java`

- `class WarpMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm2/WhereaMiCommand.java`

- `class WhereaMiCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/BanCommand.java`

- `class BanCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ChatCommand.java`

- `class ChatCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/CheckDmgCommand.java`

- `class CheckDmgCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ClosePortalCommand.java`

- `class ClosePortalCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/DebuffCommand.java`

- `class DebuffCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/EndEventCommand.java`

- `class EndEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ExpedsCommand.java`

- `class ExpedsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/FaceCommand.java`

- `class FaceCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/FameCommand.java`

- `class FameCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/FlyCommand.java`

- `class FlyCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/GiveMesosCommand.java`

- `class GiveMesosCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/GiveNxCommand.java`

- `class GiveNxCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/GiveRpCommand.java`

- `class GiveRpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/GiveVpCommand.java`

- `class GiveVpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/HairCommand.java`

- `class HairCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/HealMapCommand.java`

- `class HealMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/HealPersonCommand.java`

- `class HealPersonCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/HpMpCommand.java`

- `class HpMpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/HurtCommand.java`

- `class HurtCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/IgnoreCommand.java`

- `class IgnoreCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/IgnoredCommand.java`

- `class IgnoredCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/InMapCommand.java`

- `class InMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/KillAllCommand.java`

- `class KillAllCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/KillCommand.java`

- `class KillCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/KillMapCommand.java`

- `class KillMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MaxEnergyCommand.java`

- `class MaxEnergyCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MaxHpMpCommand.java`

- `class MaxHpMpCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MonitorCommand.java`

- `class MonitorCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MonitorsCommand.java`

- `class MonitorsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MusicCommand.java`

- `class MusicCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static String getSongList()`：读取并返回状态/数据。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/MuteMapCommand.java`

- `class MuteMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/NightCommand.java`

- `class NightCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/NoticeCommand.java`

- `class NoticeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/NpcCommand.java`

- `class NpcCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/OnlineTwoCommand.java`

- `class OnlineTwoCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/OpenPortalCommand.java`

- `class OpenPortalCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/PeCommand.java`

- `class PeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/PosCommand.java`

- `class PosCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/QuestCompleteCommand.java`

- `class QuestCompleteCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/QuestResetCommand.java`

- `class QuestResetCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/QuestStartCommand.java`

- `class QuestStartCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ReloadDropsCommand.java`

- `class ReloadDropsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ReloadEventsCommand.java`

- `class ReloadEventsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ReloadMapCommand.java`

- `class ReloadMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ReloadPortalsCommand.java`

- `class ReloadPortalsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ReloadShopsCommand.java`

- `class ReloadShopsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/RipCommand.java`

- `class RipCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/SeedCommand.java`

- `class SeedCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/SpawnCommand.java`

- `class SpawnCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/StartEventCommand.java`

- `class StartEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/StartMapEventCommand.java`

- `class StartMapEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/StopMapEventCommand.java`

- `class StopMapEventCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/TimerAllCommand.java`

- `class TimerAllCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/TimerCommand.java`

- `class TimerCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/TimerMapCommand.java`

- `class TimerMapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/ToggleCouponCommand.java`

- `class ToggleCouponCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm3/UnBanCommand.java`

- `class UnBanCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/BossDropRateCommand.java`

- `class BossDropRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/CakeCommand.java`

- `class CakeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/DropRateCommand.java`

- `class DropRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ExpRateCommand.java`

- `class ExpRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/FishingRateCommand.java`

- `class FishingRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ForceVacCommand.java`

- `class ForceVacCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/HorntailCommand.java`

- `class HorntailCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ItemVacCommand.java`

- `class ItemVacCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/MesoRateCommand.java`

- `class MesoRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PapCommand.java`

- `class PapCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PianusCommand.java`

- `class PianusCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PinkbeanCommand.java`

- `class PinkbeanCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PlayerNpcCommand.java`

- `class PlayerNpcCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PlayerNpcRemoveCommand.java`

- `class PlayerNpcRemoveCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PmobCommand.java`

- `class PmobCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PmobRemoveCommand.java`

- `class PmobRemoveCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PnpcCommand.java`

- `class PnpcCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/PnpcRemoveCommand.java`

- `class PnpcRemoveCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ProItemCommand.java`

- `class ProItemCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void hardsetItemStats(Equip equip, short stat, short spdjmp)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/QuestRateCommand.java`

- `class QuestRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ServerMessageCommand.java`

- `class ServerMessageCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/SetEqStatCommand.java`

- `class SetEqStatCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/TravelRateCommand.java`

- `class TravelRateCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/WarpToLifeCommand.java`

- `class WarpToLifeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm4/ZakumCommand.java`

- `class ZakumCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/DebugCommand.java`

- `class DebugCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/IpListCommand.java`

- `class IpListCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/SetCommand.java`

- `class SetCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/ShowMoveLifeCommand.java`

- `class ShowMoveLifeCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/ShowPacketsCommand.java`

- `class ShowPacketsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm5/ShowSessionsCommand.java`

- `class ShowSessionsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ClearQuestCacheCommand.java`

- `class ClearQuestCacheCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ClearQuestCommand.java`

- `class ClearQuestCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/DCAllCommand.java`

- `class DCAllCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/DevtestCommand.java`

- `class DevtestCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client client, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/EraseAllPNpcsCommand.java`

- `class EraseAllPNpcsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/GetAccCommand.java`

- `class GetAccCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/MapPlayersCommand.java`

- `class MapPlayersCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/SaveAllCommand.java`

- `class SaveAllCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ServerAddChannelCommand.java`

- `class ServerAddChannelCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ServerAddWorldCommand.java`

- `class ServerAddWorldCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ServerRemoveChannelCommand.java`

- `class ServerRemoveChannelCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ServerRemoveWorldCommand.java`

- `class ServerRemoveWorldCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/SetGmLevelCommand.java`

- `class SetGmLevelCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/ShutdownCommand.java`

- `class ShutdownCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/SpawnAllPNpcsCommand.java`

- `class SpawnAllPNpcsCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/SupplyRateCouponCommand.java`

- `class SupplyRateCouponCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/command/commands/gm6/WarpWorldCommand.java`

- `class WarpWorldCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void execute(Client c, String[] params)`：通用业务逻辑入口，需结合实现查看细节。

## `client/creator/CharacterFactory.java`

- `class CharacterFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected synchronized static int createNewCharacter(Client c, String name, int face, int hair, int skin, int gender, CharacterFactoryRecipe recipe)`：创建对象、会话或业务记录。

## `client/creator/CharacterFactoryRecipe.java`

- `class CharacterFactoryRecipe`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CharacterFactoryRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setStr(int v)`：写入或更新状态字段。
  - `public void setDex(int v)`：写入或更新状态字段。
  - `public void setInt(int v)`：写入或更新状态字段。
  - `public void setLuk(int v)`：写入或更新状态字段。
  - `public void setMaxHp(int v)`：写入或更新状态字段。
  - `public void setMaxMp(int v)`：写入或更新状态字段。
  - `public void setRemainingAp(int v)`：写入或更新状态字段。
  - `public void setRemainingSp(int v)`：写入或更新状态字段。
  - `public void setMeso(int v)`：写入或更新状态字段。
  - `public void addStartingSkillLevel(Skill skill, int level)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addStartingEquipment(Item eqpItem)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addStartingItem(int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Job getJob()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public int getMap()`：读取并返回状态/数据。
  - `public int getTop()`：读取并返回状态/数据。
  - `public int getBottom()`：读取并返回状态/数据。
  - `public int getShoes()`：读取并返回状态/数据。
  - `public int getWeapon()`：读取并返回状态/数据。
  - `public int getStr()`：读取并返回状态/数据。
  - `public int getDex()`：读取并返回状态/数据。
  - `public int getInt()`：读取并返回状态/数据。
  - `public int getLuk()`：读取并返回状态/数据。
  - `public int getMaxHp()`：读取并返回状态/数据。
  - `public int getMaxMp()`：读取并返回状态/数据。
  - `public int getRemainingAp()`：读取并返回状态/数据。
  - `public int getRemainingSp()`：读取并返回状态/数据。
  - `public int getMeso()`：读取并返回状态/数据。

## `client/creator/MakeCharInfo.java`

- `class MakeCharInfo`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MakeCharInfo(Data charInfoData)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyFaceId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyHairId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyHairColorId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifySkinId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyTopId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyBottomId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyShoeId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyWeaponId(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean verifyCharacter(Character character)`：通用业务逻辑入口，需结合实现查看细节。

## `client/creator/MakeCharInfoValidator.java`

- `class MakeCharInfoValidator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static MakeCharInfo getMakeCharInfo(Character character)`：读取并返回状态/数据。
  - `public static boolean isNewCharacterValid(Character character)`：进行条件判定并返回布尔结果。

## `client/creator/novice/BeginnerCreator.java`

- `class BeginnerCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)`：创建对象、会话或业务记录。

## `client/creator/novice/LegendCreator.java`

- `class LegendCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)`：创建对象、会话或业务记录。

## `client/creator/novice/NoblesseCreator.java`

- `class NoblesseCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)`：创建对象、会话或业务记录。

## `client/creator/veteran/BowmanCreator.java`

- `class BowmanCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)`：创建对象、会话或业务记录。

## `client/creator/veteran/MagicianCreator.java`

- `class MagicianCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon, int gender, int improveSp)`：创建对象、会话或业务记录。
  - `private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)`：创建对象、会话或业务记录。

## `client/creator/veteran/PirateCreator.java`

- `class PirateCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)`：创建对象、会话或业务记录。

## `client/creator/veteran/ThiefCreator.java`

- `class ThiefCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)`：创建对象、会话或业务记录。
  - `private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)`：创建对象、会话或业务记录。

## `client/creator/veteran/WarriorCreator.java`

- `class WarriorCreator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon, int gender, int improveSp)`：创建对象、会话或业务记录。
  - `private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)`：创建对象、会话或业务记录。

## `client/inventory/Equip.java`

- `class Equip`：领域类型或功能模块，职责由同名文件实现定义。
- `enum ScrollResult`：领域类型或功能模块，职责由同名文件实现定义。
- `enum StatUpgrade`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Equip(int id, short position)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Equip(int id, short position, int slots)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item copy()`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getFlag()`：读取并返回状态/数据。
  - `public byte getItemType()`：读取并返回状态/数据。
  - `public byte getUpgradeSlots()`：读取并返回状态/数据。
  - `public short getStr()`：读取并返回状态/数据。
  - `public short getDex()`：读取并返回状态/数据。
  - `public short getInt()`：读取并返回状态/数据。
  - `public short getLuk()`：读取并返回状态/数据。
  - `public short getHp()`：读取并返回状态/数据。
  - `public short getMp()`：读取并返回状态/数据。
  - `public short getWatk()`：读取并返回状态/数据。
  - `public short getMatk()`：读取并返回状态/数据。
  - `public short getWdef()`：读取并返回状态/数据。
  - `public short getMdef()`：读取并返回状态/数据。
  - `public short getAcc()`：读取并返回状态/数据。
  - `public short getAvoid()`：读取并返回状态/数据。
  - `public short getHands()`：读取并返回状态/数据。
  - `public short getSpeed()`：读取并返回状态/数据。
  - `public short getJump()`：读取并返回状态/数据。
  - `public short getVicious()`：读取并返回状态/数据。
  - `public void setFlag(short flag)`：写入或更新状态字段。
  - `public void setStr(short str)`：写入或更新状态字段。
  - `public void setDex(short dex)`：写入或更新状态字段。
  - `public void setInt(short _int)`：写入或更新状态字段。
  - `public void setLuk(short luk)`：写入或更新状态字段。
  - `public void setHp(short hp)`：写入或更新状态字段。
  - `public void setMp(short mp)`：写入或更新状态字段。
  - `public void setWatk(short watk)`：写入或更新状态字段。
  - `public void setMatk(short matk)`：写入或更新状态字段。
  - `public void setWdef(short wdef)`：写入或更新状态字段。
  - `public void setMdef(short mdef)`：写入或更新状态字段。
  - `public void setAcc(short acc)`：写入或更新状态字段。
  - `public void setAvoid(short avoid)`：写入或更新状态字段。
  - `public void setHands(short hands)`：写入或更新状态字段。
  - `public void setSpeed(short speed)`：写入或更新状态字段。
  - `public void setJump(short jump)`：写入或更新状态字段。
  - `public void setVicious(short vicious)`：写入或更新状态字段。
  - `public void setUpgradeSlots(byte upgradeSlots)`：写入或更新状态字段。
  - `public byte getLevel()`：读取并返回状态/数据。
  - `public void setLevel(byte level)`：写入或更新状态字段。
  - `private static int getStatModifier(boolean isAttribute)`：读取并返回状态/数据。
  - `private static int randomizeStatUpgrade(int top)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isPhysicalWeapon(int itemid)`：进行条件判定并返回布尔结果。
  - `private boolean isNotWeaponAffinity(StatUpgrade name)`：进行条件判定并返回布尔结果。
  - `private void getUnitStatUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name, int curStat, boolean isAttribute)`：读取并返回状态/数据。
  - `private static void getUnitSlotUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name)`：读取并返回状态/数据。
  - `private static void getUnitSlotUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name, double chance)`：读取并返回状态/数据。
  - `private void UpgradeSlotProcessing(List<Pair<StatUpgrade, Integer>> stats,int equipLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void improveDefaultStats(List<Pair<StatUpgrade, Integer>> stats)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int handleStatUpgrade(StatUpgrade type, int value, int maxStat)`：处理事件/请求/消息分发。
  - `private int getCurrentStat(StatUpgrade type)`：读取并返回状态/数据。
  - `private void setCurrentStat(StatUpgrade type, int value)`：写入或更新状态字段。
  - `private String getStatMessage(StatUpgrade type, int value)`：读取并返回状态/数据。
  - `private void gainLevel(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getItemExp()`：读取并返回状态/数据。
  - `private static double normalizedMasteryExp(int reqLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void gainItemExp(Client c, int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean reachedMaxLevel()`：通用业务逻辑入口，需结合实现查看细节。
  - `public String showEquipFeatures(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setItemExp(int exp)`：写入或更新状态字段。
  - `public void setItemLevel(byte level)`：写入或更新状态字段。
  - `public void setQuantity(short quantity)`：写入或更新状态字段。
  - `public void setUpgradeSlots(int i)`：写入或更新状态字段。
  - `public void setVicious(int i)`：写入或更新状态字段。
  - `public int getRingId()`：读取并返回状态/数据。
  - `public void setRingId(int id)`：写入或更新状态字段。
  - `public boolean isWearing()`：进行条件判定并返回布尔结果。
  - `public void wear(boolean yes)`：通用业务逻辑入口，需结合实现查看细节。

## `client/inventory/Inventory.java`

- `class Inventory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Inventory(Character mc, InventoryType type, byte slotLimit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isExtendableInventory()`：进行条件判定并返回布尔结果。
  - `public boolean isEquipInventory()`：进行条件判定并返回布尔结果。
  - `public byte getSlotLimit()`：读取并返回状态/数据。
  - `public void setSlotLimit(int newLimit)`：写入或更新状态字段。
  - `public Collection<Item> list()`：查询并返回匹配集合或单项结果。
  - `public Item findById(int itemId)`：查询并返回匹配集合或单项结果。
  - `public Item findByName(String name)`：查询并返回匹配集合或单项结果。
  - `public int countById(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countNotOwnedById(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int freeSlotCountById(int itemId, int required)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Item> listById(int itemId)`：查询并返回匹配集合或单项结果。
  - `public List<Item> linkedListById(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public short addItem(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addItemFromDB(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isSameOwner(Item source, Item target)`：进行条件判定并返回布尔结果。
  - `public void move(short sSlot, short dSlot, short slotMax)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void swap(Item source, Item target)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item getItem(short slot)`：读取并返回状态/数据。
  - `public void removeItem(short slot)`：删除对象、关系或临时状态。
  - `public void removeItem(short slot, short quantity, boolean allowZero)`：删除对象、关系或临时状态。
  - `protected short addSlot(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void addSlotFromDB(short slot, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeSlot(short slot)`：删除对象、关系或临时状态。
  - `public boolean isFull()`：进行条件判定并返回布尔结果。
  - `public boolean isFull(int margin)`：进行条件判定并返回布尔结果。
  - `public boolean isFullAfterSomeItems(int margin, int used)`：进行条件判定并返回布尔结果。
  - `public short getNextFreeSlot()`：读取并返回状态/数据。
  - `public short getNumFreeSlot()`：读取并返回状态/数据。
  - `private static boolean checkItemRestricted(List<Pair<Item, InventoryType>> items)`：校验输入参数或业务约束。
  - `public static boolean checkSpot(Character chr, Item item)`：校验输入参数或业务约束。
  - `public static boolean checkSpot(Character chr, List<Item> items)`：校验输入参数或业务约束。
  - `public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items)`：校验输入参数或业务约束。
  - `public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, boolean useProofInv)`：校验输入参数或业务约束。
  - `public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, List<Integer> typesSlotsUsed, boolean useProofInv)`：校验输入参数或业务约束。
  - `private static long fnvHash32(final String k)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Long hashKey(Integer itemId, String owner)`：进行条件判定并返回布尔结果。
  - `public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items)`：校验输入参数或业务约束。
  - `public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items, boolean useProofInv)`：校验输入参数或业务约束。
  - `public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items, List<Integer> typesSlotsUsed, boolean useProofInv)`：校验输入参数或业务约束。
  - `public InventoryType getType()`：读取并返回状态/数据。
  - `public Iterator<Item> iterator()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item findByCashId(int cashId)`：查询并返回匹配集合或单项结果。
  - `public boolean checked()`：校验输入参数或业务约束。
  - `public void checked(boolean yes)`：校验输入参数或业务约束。
  - `public void lockInventory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unlockInventory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `client/inventory/InventoryProof.java`

- `class InventoryProof`：领域类型或功能模块，职责由同名文件实现定义。
  - `public InventoryProof(Character mc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cloneContents(Inventory inv)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void flushContents()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected short addSlot(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void addSlotFromDB(short slot, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeSlot(short slot)`：删除对象、关系或临时状态。

## `client/inventory/InventoryType.java`

- `enum InventoryType`：领域类型或功能模块，职责由同名文件实现定义。
  - `UNDEFINED(0, I18nUtil.getMessage("InventoryType.UNDEFINED")),`：通用业务逻辑入口，需结合实现查看细节。
  - `EQUIP(1, I18nUtil.getMessage("InventoryType.EQUIP")),`：通用业务逻辑入口，需结合实现查看细节。
  - `USE(2, I18nUtil.getMessage("InventoryType.USE")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SETUP(3, I18nUtil.getMessage("InventoryType.SETUP")),`：写入或更新状态字段。
  - `ETC(4, I18nUtil.getMessage("InventoryType.ETC")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH(5, I18nUtil.getMessage("InventoryType.CASH")),`：通用业务逻辑入口，需结合实现查看细节。
  - `CANHOLD(6, I18nUtil.getMessage("InventoryType.CANHOLD")),   //Proof-guard for inserting after removal checks`：进行条件判定并返回布尔结果。
  - `EQUIPPED(-1, I18nUtil.getMessage("InventoryType.EQUIPPED")); //Seems nexon screwed something when removing an item T_T`：通用业务逻辑入口，需结合实现查看细节。
  - `InventoryType(int type, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getBitfieldEncoding()`：读取并返回状态/数据。
  - `public static InventoryType getByType(byte type)`：读取并返回状态/数据。
  - `public static InventoryType getByWZName(String name)`：读取并返回状态/数据。
  - `public boolean canChangeSlotMax()`：进行条件判定并返回布尔结果。
  - `public boolean isEquip()`：进行条件判定并返回布尔结果。

## `client/inventory/Item.java`

- `class Item`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Item(int id, short position, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item(int id, short position, short quantity, int petid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item copy()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setPosition(short position)`：写入或更新状态字段。
  - `public void setQuantity(short quantity)`：写入或更新状态字段。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public int getCashId()`：读取并返回状态/数据。
  - `public short getPosition()`：读取并返回状态/数据。
  - `public short getQuantity()`：读取并返回状态/数据。
  - `public InventoryType getInventoryType()`：读取并返回状态/数据。
  - `public byte getItemType()`：读取并返回状态/数据。
  - `public String getOwner()`：读取并返回状态/数据。
  - `public void setOwner(String owner)`：写入或更新状态字段。
  - `public int getPetId()`：读取并返回状态/数据。
  - `public int compareTo(Item other)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<String> getItemLog()`：读取并返回状态/数据。
  - `public short getFlag()`：读取并返回状态/数据。
  - `public void setFlag(short b)`：写入或更新状态字段。
  - `public long getExpiration()`：读取并返回状态/数据。
  - `public void setExpiration(long expire)`：写入或更新状态字段。
  - `public int getSN()`：读取并返回状态/数据。
  - `public void setSN(int sn)`：写入或更新状态字段。
  - `public String getGiftFrom()`：读取并返回状态/数据。
  - `public void setGiftFrom(String giftFrom)`：写入或更新状态字段。
  - `public Pet getPet()`：读取并返回状态/数据。
  - `public boolean isUntradeable()`：进行条件判定并返回布尔结果。

## `client/inventory/ItemFactory.java`

- `enum ItemFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `INVENTORY(1, false),`：通用业务逻辑入口，需结合实现查看细节。
  - `STORAGE(2, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_EXPLORER(3, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_CYGNUS(4, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_ARAN(5, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `MERCHANT(6, false),`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_OVERALL(7, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `MARRIAGE_GIFTS(8, false),`：通用业务逻辑入口，需结合实现查看细节。
  - `DUEY(9, false)`：通用业务逻辑入口，需结合实现查看细节。
  - `ItemFactory(int value, boolean account)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getValue()`：读取并返回状态/数据。
  - `public void saveItems(List<Pair<Item, InventoryType>> items, int id, Connection con) throws SQLException`：持久化当前状态到存储层。
  - `public void saveItems(List<Pair<Item, InventoryType>> items, List<Short> bundlesList, int id, Connection con) throws SQLException`：持久化当前状态到存储层。
  - `private static Equip loadEquipFromResultSet(ResultSet rs) throws SQLException`：从外部来源加载数据（数据库/文件/配置）。
  - `private void saveItemsCommon(List<Pair<Item, InventoryType>> items, int id, Connection con) throws SQLException`：持久化当前状态到存储层。
  - `private void saveItemsMerchant(List<Pair<Item, InventoryType>> items, List<Short> bundlesList, int id, Connection con) throws SQLException`：持久化当前状态到存储层。

## `client/inventory/ModifyInventory.java`

- `class ModifyInventory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ModifyInventory(final int mode, final Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ModifyInventory(final int mode, final Item item, final short oldPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int getMode()`：读取并返回状态/数据。
  - `public final int getInventoryType()`：读取并返回状态/数据。
  - `public final short getPosition()`：读取并返回状态/数据。
  - `public final short getOldPosition()`：读取并返回状态/数据。
  - `public final short getQuantity()`：读取并返回状态/数据。
  - `public final Item getItem()`：读取并返回状态/数据。
  - `public final void clear()`：通用业务逻辑入口，需结合实现查看细节。

## `client/inventory/Pet.java`

- `class Pet`：领域类型或功能模块，职责由同名文件实现定义。
- `enum PetAttribute`：领域类型或功能模块，职责由同名文件实现定义。
  - `private Pet(int id, short position, int uniqueid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Pet loadFromDb(int itemid, short position, int petid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static void deleteFromDb(Character owner, int petid)`：删除对象、关系或临时状态。
  - `public void saveToDb()`：持久化当前状态到存储层。
  - `public static int createPet(int itemid)`：创建对象、会话或业务记录。
  - `public static int createPet(int itemid, byte level, int tameness, int fullness)`：创建对象、会话或业务记录。
  - `public String getName()`：读取并返回状态/数据。
  - `public void setName(String name)`：写入或更新状态字段。
  - `public int getUniqueId()`：读取并返回状态/数据。
  - `public void setUniqueId(int id)`：写入或更新状态字段。
  - `public int getTameness()`：读取并返回状态/数据。
  - `public void setTameness(int tameness)`：写入或更新状态字段。
  - `public byte getLevel()`：读取并返回状态/数据。
  - `public void gainTamenessFullness(Character owner, int incTameness, int incFullness, int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainTamenessFullness(Character owner, int incTameness, int incFullness, int type, boolean forceEnjoy)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setLevel(byte level)`：写入或更新状态字段。
  - `public int getFullness()`：读取并返回状态/数据。
  - `public void setFullness(int fullness)`：写入或更新状态字段。
  - `public int getFh()`：读取并返回状态/数据。
  - `public void setFh(int Fh)`：写入或更新状态字段。
  - `public Point getPos()`：读取并返回状态/数据。
  - `public void setPos(Point pos)`：写入或更新状态字段。
  - `public int getStance()`：读取并返回状态/数据。
  - `public void setStance(int stance)`：写入或更新状态字段。
  - `public boolean isSummoned()`：进行条件判定并返回布尔结果。
  - `public void setSummoned(boolean yes)`：写入或更新状态字段。
  - `public int getPetAttribute()`：读取并返回状态/数据。
  - `private void setPetAttribute(int flag)`：写入或更新状态字段。
  - `public void addPetAttribute(Character owner, PetAttribute flag)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePetAttribute(Character owner, PetAttribute flag)`：删除对象、关系或临时状态。
  - `public void updatePosition(List<LifeMovementFragment> movement)`：更新已有对象/配置/缓存。

## `client/inventory/PetCommand.java`

- `class PetCommand`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PetCommand(int petId, int skillId, int prob, int inc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getPetId()`：读取并返回状态/数据。
  - `public int getSkillId()`：读取并返回状态/数据。
  - `public int getProbability()`：读取并返回状态/数据。
  - `public int getIncrease()`：读取并返回状态/数据。

## `client/inventory/PetDataFactory.java`

- `class PetDataFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static PetCommand getPetCommand(int petId, int skillId)`：读取并返回状态/数据。
  - `public static int getHunger(int petId)`：读取并返回状态/数据。

## `client/inventory/WeaponType.java`

- `enum WeaponType`：领域类型或功能模块，职责由同名文件实现定义。
  - `NOT_A_WEAPON(0),`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL1H_SWING(4.4),`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL1H_STAB(3.2),`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL2H_SWING(4.8),`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL2H_STAB(3.4),`：通用业务逻辑入口，需结合实现查看细节。
  - `BOW(3.4),`：通用业务逻辑入口，需结合实现查看细节。
  - `CLAW(3.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `CROSSBOW(3.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAGGER_THIEVES(3.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAGGER_OTHER(4),`：通用业务逻辑入口，需结合实现查看细节。
  - `GUN(3.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `KNUCKLE(4.8),`：通用业务逻辑入口，需结合实现查看细节。
  - `POLE_ARM_SWING(5.0),`：通用业务逻辑入口，需结合实现查看细节。
  - `POLE_ARM_STAB(3.0),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEAR_STAB(5.0),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEAR_SWING(3.0),`：通用业务逻辑入口，需结合实现查看细节。
  - `STAFF(3.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `SWORD1H(4.0),`：通用业务逻辑入口，需结合实现查看细节。
  - `SWORD2H(4.6),`：通用业务逻辑入口，需结合实现查看细节。
  - `WAND(3.6)`：通用业务逻辑入口，需结合实现查看细节。
  - `WeaponType(double maxDamageMultiplier)`：通用业务逻辑入口，需结合实现查看细节。
  - `public double getMaxDamageMultiplier()`：读取并返回状态/数据。

## `client/inventory/manipulator/InventoryManipulator.java`

- `class InventoryManipulator`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean addById(Client c, int itemId, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addById(Client c, int itemId, short quantity, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addById(Client c, int itemId, short quantity, String owner, int petid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, short flag, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean addByIdInternal(Client c, Character chr, InventoryType type, Inventory inv, int itemId, short quantity, String owner, int petid, short flag, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addFromDrop(Client c, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addFromDrop(Client c, Item item, boolean show)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean addFromDrop(Client c, Item item, boolean show, int petId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean addFromDropInternal(Client c, Character chr, InventoryType type, Inventory inv, Item item, boolean show, int petId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean haveItemWithId(Inventory inv, int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean checkSpace(Client c, int itemid, int quantity, String owner)`：校验输入参数或业务约束。
  - `public static int checkSpaceProgressively(Client c, int itemid, int quantity, String owner, int usedSlots, boolean useProofInv)`：校验输入参数或业务约束。
  - `public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop)`：删除对象、关系或临时状态。
  - `public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop, boolean consume)`：删除对象、关系或临时状态。
  - `private static void announceModifyInventory(Client c, Item item, boolean fromDrop, boolean allowZero)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void removeById(Client c, InventoryType type, int itemId, int quantity, boolean fromDrop, boolean consume)`：删除对象、关系或临时状态。
  - `private static boolean isSameOwner(Item source, Item target)`：进行条件判定并返回布尔结果。
  - `public static void move(Client c, InventoryType type, short src, short dst)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void equip(Client c, short src, short dst)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void unequip(Client c, short src, short dst)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isDisappearingItemDrop(Item it)`：进行条件判定并返回布尔结果。
  - `public static void drop(Client c, InventoryType type, short src, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isDroppedItemRestricted(Item it)`：进行条件判定并返回布尔结果。
  - `public static boolean isSandboxItem(Item it)`：进行条件判定并返回布尔结果。

## `client/inventory/manipulator/KarmaManipulator.java`

- `class KarmaManipulator`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static short getKarmaFlag(Item item)`：读取并返回状态/数据。
  - `public static boolean hasKarmaFlag(Item item)`：进行条件判定并返回布尔结果。
  - `public static void toggleKarmaFlagToUntradeable(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void setKarmaFlag(Item item)`：写入或更新状态字段。

## `client/keybind/KeyBinding.java`

- `class KeyBinding`：领域类型或功能模块，职责由同名文件实现定义。
  - `public KeyBinding(int type, int action)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getType()`：读取并返回状态/数据。
  - `public int getAction()`：读取并返回状态/数据。

## `client/keybind/QuickslotBinding.java`

- `class QuickslotBinding`：领域类型或功能模块，职责由同名文件实现定义。
  - `public QuickslotBinding(byte[] aKeys)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void encode(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte[] GetKeybindings()`：读取并返回状态/数据。

## `client/processor/action/MakerProcessor.java`

- `class MakerProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void makerAction(InPacket p, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean removeOddMakerReagents(int toCreate, Map<Integer, Short> reagentids)`：删除对象、关系或临时状态。
  - `private static int getMakerReagentSlots(int itemId)`：读取并返回状态/数据。
  - `public static int getMakerSkillLevel(Character chr)`：读取并返回状态/数据。
  - `private static short getCreateStatus(Client c, MakerItemCreateEntry recipe)`：读取并返回状态/数据。
  - `private static boolean hasItems(Client c, MakerItemCreateEntry recipe)`：进行条件判定并返回布尔结果。
  - `private static boolean addBoostedMakerItem(Client c, int itemid, int stimulantid, Map<Integer, Short> reagentids)`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/action/PetAutopotProcessor.java`

- `class PetAutopotProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void runAutopotAction(Client c, short slot, int itemid)`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/action/SpawnPetProcessor.java`

- `class SpawnPetProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void processSpawnPet(Client c, byte slot, boolean lead)`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/npc/DueyProcessor.java`

- `class DueyProcessor`：领域类型或功能模块，职责由同名文件实现定义。
- `enum Actions`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static void showDueyNotification(Client c, Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void deletePackageFromInventoryDB(Connection con, int packageId) throws SQLException`：删除对象、关系或临时状态。
  - `private static void removePackageFromDB(int packageId)`：删除对象、关系或临时状态。
  - `private static DueyPackage getPackageFromDB(ResultSet rs)`：读取并返回状态/数据。
  - `private static List<DueyPackage> loadPackages(Character chr)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static int createPackage(int mesos, String message, String sender, int toCid, boolean quick)`：创建对象、会话或业务记录。
  - `private static boolean insertPackageItem(int packageId, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int addPackageItemFromInventory(int packageId, Client c, byte invTypeId, short itemPos, short amount)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void dueySendItem(Client c, byte invTypeId, short itemPos, short amount, int sendMesos, String sendMessage, String recipient, boolean quick)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void dueyRemovePackage(Client c, int packageid, boolean playerRemove)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static synchronized void dueyClaimPackage(Client c, int packageId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void dueySendTalk(Client c, boolean quickDelivery)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void dueyCreatePackage(Item item, int mesos, String sender, int recipientCid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void runDueyExpireSchedule()`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/npc/FredrickProcessor.java`

- `class FredrickProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FredrickProcessor(NoteService noteService)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte canRetrieveFromFredrick(Character chr, List<Pair<Item, InventoryType>> items)`：进行条件判定并返回布尔结果。
  - `public static int timestampElapsedDays(Timestamp then, long timeNow)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String fredrickReminderMessage(int daynotes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void removeFredrickLog(int cid)`：删除对象、关系或临时状态。
  - `private static void removeFredrickLog(Connection con, int cid) throws SQLException`：删除对象、关系或临时状态。
  - `public static void insertFredrickLog(int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void removeFredrickReminders(List<Pair<Integer, Integer>> expiredCids)`：删除对象、关系或临时状态。
  - `public void runFredrickSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean deleteFredrickItems(int cid)`：删除对象、关系或临时状态。
  - `public void fredrickRetrieveItems(Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/npc/StorageProcessor.java`

- `class StorageProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void storageAction(InPacket p, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean hasGMRestrictions(Character character)`：进行条件判定并返回布尔结果。

## `client/processor/stat/AssignAPProcessor.java`

- `class AssignAPProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void reloadConfig()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void APAutoAssignAction(InPacket inPacket, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getNthHighestStat(List<Short> statList, short rank)`：读取并返回状态/数据。
  - `private static int gainStatByType(Stat type, int[] statGain, int gain, int[] statUpdate)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Stat getQuaternaryStat(Job stance)`：读取并返回状态/数据。
  - `public static boolean APResetAction(Client c, int APFrom, int APTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void APAssignAction(Client c, int num)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean addStat(Character chr, int apTo, boolean usedAPReset)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int calcHpChange(Character player, boolean usedAPReset)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int calcMpChange(Character player, boolean usedAPReset)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int takeHp(Job job)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int takeMp(Job job)`：通用业务逻辑入口，需结合实现查看细节。

## `client/processor/stat/AssignSPProcessor.java`

- `class AssignSPProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean canSPAssign(Client c, int skillid)`：进行条件判定并返回布尔结果。
  - `public static void SPAssignAction(Client c, int skillid)`：通用业务逻辑入口，需结合实现查看细节。

## `client/status/MonsterStatus.java`

- `enum MonsterStatus`：领域类型或功能模块，职责由同名文件实现定义。
  - `WATK(0x1),`：通用业务逻辑入口，需结合实现查看细节。
  - `WDEF(0x2),`：通用业务逻辑入口，需结合实现查看细节。
  - `NEUTRALISE(0x2, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `PHANTOM_IMPRINT(0x4, true), // needs testing`：通用业务逻辑入口，需结合实现查看细节。
  - `MATK(0x4),`：通用业务逻辑入口，需结合实现查看细节。
  - `MDEF(0x8),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACC(0x10),`：通用业务逻辑入口，需结合实现查看细节。
  - `AVOID(0x20),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEED(0x40),`：通用业务逻辑入口，需结合实现查看细节。
  - `STUN(0x80),`：通用业务逻辑入口，需结合实现查看细节。
  - `FREEZE(0x100),`：通用业务逻辑入口，需结合实现查看细节。
  - `POISON(0x200),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEAL(0x400),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOWDOWN(0x800),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON_ATTACK_UP(0x1000),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON_DEFENSE_UP(0x2000),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_ATTACK_UP(0x4000),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_DEFENSE_UP(0x8000),`：通用业务逻辑入口，需结合实现查看细节。
  - `DOOM(0x10000),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHADOW_WEB(0x20000),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON_IMMUNITY(0x40000),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_IMMUNITY(0x80000),`：通用业务逻辑入口，需结合实现查看细节。
  - `HARD_SKIN(0x200000), // just added`：通用业务逻辑入口，需结合实现查看细节。
  - `NINJA_AMBUSH(0x400000),`：通用业务逻辑入口，需结合实现查看细节。
  - `ELEMENTAL_ATTRIBUTE(0x800000), // just added`：通用业务逻辑入口，需结合实现查看细节。
  - `VENOMOUS_WEAPON(0x1000000),`：通用业务逻辑入口，需结合实现查看细节。
  - `BLIND(0x2000000), // just added`：通用业务逻辑入口，需结合实现查看细节。
  - `SEAL_SKILL(0x4000000),`：通用业务逻辑入口，需结合实现查看细节。
  - `INERTMOB(0x10000000),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAPON_REFLECT(0x20000000, true),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_REFLECT(0x40000000, true)`：通用业务逻辑入口，需结合实现查看细节。
  - `MonsterStatus(int i)`：通用业务逻辑入口，需结合实现查看细节。
  - `MonsterStatus(int i, boolean first)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isFirst()`：进行条件判定并返回布尔结果。
  - `public int getValue()`：读取并返回状态/数据。

## `client/status/MonsterStatusEffect.java`

- `class MonsterStatusEffect`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterStatusEffect(Map<MonsterStatus, Integer> stati, Skill skillId, MobSkill mobskill, boolean monsterSkill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Integer setValue(MonsterStatus status, Integer newVal)`：写入或更新状态字段。
  - `public Skill getSkill()`：读取并返回状态/数据。
  - `public boolean isMonsterSkill()`：进行条件判定并返回布尔结果。
  - `public void removeActiveStatus(MonsterStatus stat)`：删除对象、关系或临时状态。
  - `public MobSkill getMobSkill()`：读取并返回状态/数据。
