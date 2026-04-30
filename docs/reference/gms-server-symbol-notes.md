# gms-server 逐符号中文职责索引

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 文件数：1116

## `ServerApplication.java`

- `class ServerApplication`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void main(String[] args)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void initDb(String[] args) throws Exception`：初始化模块、资源或运行时状态。
  - `private static Connection getConnection(String driver, String url, String username, String password) throws Exception`：读取并返回状态/数据。
  - `private static String getStartParam(String[] args, String paramName)`：读取并返回状态/数据。

## `aop/AuthEntryPointJwt.java`

- `class AuthEntryPointJwt`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException`：通用业务逻辑入口，需结合实现查看细节。

## `aop/AuthTokenFilter.java`

- `class AuthTokenFilter`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected void doFilterInternal(@NonNull HttpServletRequest request, @NonNull HttpServletResponse response, @NonNull FilterChain filterChain)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String parseJwt(HttpServletRequest request)`：解析输入文本或二进制内容。

## `aop/ServerFilter.java`

- `class ServerFilter`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected boolean shouldNotFilter(final HttpServletRequest request)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void doFilter(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws IOException, ServletException`：通用业务逻辑入口，需结合实现查看细节。

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

## `config/CorsConfig.java`

- `class CorsConfig`：配置绑定/初始化相关类型。
  - `public void addCorsMappings(CorsRegistry registry)`：通用业务逻辑入口，需结合实现查看细节。

## `config/GameConfig.java`

- `class GameConfig`：配置绑定/初始化相关类型。
  - `private GameConfig()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void add(GameConfigDO gameConfigDO)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void add(GameConfig config, GameConfigDO gameConfigDO)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void remove(GameConfigDO gameConfigDO)`：删除对象、关系或临时状态。
  - `public static void update(GameConfigDO gameConfigDO)`：更新已有对象/配置/缓存。
  - `public static Object getObject(String key)`：读取并返回状态/数据。
  - `public static <T> T get(String key)`：读取并返回状态/数据。
  - `public static <T> T get(String key, T defaultValue)`：读取并返回状态/数据。
  - `public static <T> T get(String type, String key)`：读取并返回状态/数据。
  - `public static <T> T get(String type, String key, T defaultVal)`：读取并返回状态/数据。
  - `public static <T> T get(String type, String subType, String key)`：读取并返回状态/数据。
  - `public static <T> T get(String type, String subType, String key, T defaultVal)`：读取并返回状态/数据。
  - `private static <T> T getValue(JSONObject valueProp)`：读取并返回状态/数据。
  - `public static JSONObject getValueProp(String type, String subType, String key)`：读取并返回状态/数据。
  - `public static JSONObject getValueProp(String type, String key)`：读取并返回状态/数据。
  - `public static Integer getInteger(String key)`：读取并返回状态/数据。
  - `public static int getIntValue(String key)`：读取并返回状态/数据。
  - `public static Long getLong(String key)`：读取并返回状态/数据。
  - `public static long getLongValue(String key)`：读取并返回状态/数据。
  - `public static Short getShort(String key)`：读取并返回状态/数据。
  - `public static short getShortValue(String key)`：读取并返回状态/数据。
  - `public static Byte getByte(String key)`：读取并返回状态/数据。
  - `public static byte getByteValue(String key)`：读取并返回状态/数据。
  - `public static float getFloat(String key)`：读取并返回状态/数据。
  - `public static float getFloatValue(String key)`：读取并返回状态/数据。
  - `public static Double getDouble(String key)`：读取并返回状态/数据。
  - `public static double getDoubleValue(String key)`：读取并返回状态/数据。
  - `public static Boolean getBoolean(String key)`：读取并返回状态/数据。
  - `public static boolean getBooleanValue(String key)`：读取并返回状态/数据。
  - `public static String getString(String key)`：读取并返回状态/数据。
  - `public static String getStringValue(String key)`：读取并返回状态/数据。
  - `public static <T> T getObject(String key, Class<T> clz)`：读取并返回状态/数据。
  - `private static <T> T getValue(String key, T defaultVal, Function<JSONObject, T> mapper)`：读取并返回状态/数据。
  - `public static <T> T getWorld(int worldId, String key)`：读取并返回状态/数据。
  - `public static <T> T getServer(String key)`：读取并返回状态/数据。
  - `public static int getWorldInt(int worldId, String key)`：读取并返回状态/数据。
  - `public static int getServerInt(String key)`：读取并返回状态/数据。
  - `public static byte getWorldByte(int worldId, String key)`：读取并返回状态/数据。
  - `public static byte getServerByte(String key)`：读取并返回状态/数据。
  - `public static long getWorldLong(int worldId, String key)`：读取并返回状态/数据。
  - `public static long getServerLong(String key)`：读取并返回状态/数据。
  - `public static short getWorldShort(int worldId, String key)`：读取并返回状态/数据。
  - `public static short getServerShort(String key)`：读取并返回状态/数据。
  - `public static float getWorldFloat(int worldId, String key)`：读取并返回状态/数据。
  - `public static float getServerFloat(String key)`：读取并返回状态/数据。
  - `public static double getWorldDouble(int worldId, String key)`：读取并返回状态/数据。
  - `public static double getServerDouble(String key)`：读取并返回状态/数据。
  - `public static String getWorldString(int worldId, String key)`：读取并返回状态/数据。
  - `public static String getServerString(String key)`：读取并返回状态/数据。
  - `public static boolean getWorldBoolean(int worldId, String key)`：读取并返回状态/数据。
  - `public static boolean getServerBoolean(String key)`：读取并返回状态/数据。
  - `public static <T> T getWorldObject(int worldId, String key, Class<T> clz)`：读取并返回状态/数据。
  - `public static <T> T getWorldObject(int worldId, String key, T defaultVal)`：读取并返回状态/数据。
  - `public static <T> T getServerObject(String key, Class<T> clz)`：读取并返回状态/数据。
  - `public static <T> T getServerObject(String key, T defaultVal)`：读取并返回状态/数据。
  - `private static <T> T getValue(boolean isServer, String subType, String key, Class<?> clz)`：读取并返回状态/数据。
  - `public static <T> T getWorldObject(int worldId, String key, TypeReference<T> type)`：读取并返回状态/数据。
  - `public static <T> T getServerObject(String key, TypeReference<T> type)`：读取并返回状态/数据。
  - `public static JSONObject getConfig()`：读取并返回状态/数据。

## `config/I18nConfig.java`

- `class I18nConfig`：配置绑定/初始化相关类型。
  - `public MessageSource messageSource()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MessageSource logSource()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MessageSource exceptionSource()`：通用业务逻辑入口，需结合实现查看细节。

## `config/ServerConfig.java`

- `class ServerConfig`：配置绑定/初始化相关类型。
  - `public FilterRegistrationBean<ServerFilter> filterRegistrationBean(ServerFilter serverFilter)`：通用业务逻辑入口，需结合实现查看细节。
  - `public OpenAPI openAPI()`：通用业务逻辑入口，需结合实现查看细节。

## `config/SpringSecurityConfig.java`

- `class SpringSecurityConfig`：配置绑定/初始化相关类型。
  - `public SpringSecurityConfig(UserDetailsServiceImpl userDetailsService, AuthEntryPointJwt unauthorizedHandler)`：通用业务逻辑入口，需结合实现查看细节。
  - `public AuthTokenFilter authenticationJwtTokenFilter()`：处理认证/会话生命周期。
  - `public DaoAuthenticationProvider authenticationProvider()`：处理认证/会话生命周期。
  - `public AuthenticationManager authenticationManager(AuthenticationConfiguration authConfig) throws Exception`：处理认证/会话生命周期。
  - `public PasswordEncoder passwordEncoder()`：通用业务逻辑入口，需结合实现查看细节。
  - `public SecurityFilterChain filterChain(HttpSecurity http) throws Exception`：通用业务逻辑入口，需结合实现查看细节。

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

## `dao/entity/AccountsDO.java`

- `class AccountsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/AllianceDO.java`

- `class AllianceDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/AllianceguildsDO.java`

- `class AllianceguildsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/AreaInfoDO.java`

- `class AreaInfoDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/AutobanConfigDO.java`

- `class AutobanConfigDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/BbsRepliesDO.java`

- `class BbsRepliesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/BbsThreadsDO.java`

- `class BbsThreadsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/BosslogDailyDO.java`

- `class BosslogDailyDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/BosslogWeeklyDO.java`

- `class BosslogWeeklyDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/BuddiesDO.java`

- `class BuddiesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/CharactersDO.java`

- `class CharactersDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/CommandInfoDO.java`

- `class CommandInfoDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/CooldownsDO.java`

- `class CooldownsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/DropDataDO.java`

- `class DropDataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/DropDataGlobalDO.java`

- `class DropDataGlobalDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/DueyitemsDO.java`

- `class DueyitemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/DueypackagesDO.java`

- `class DueypackagesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/EventstatsDO.java`

- `class EventstatsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ExtendValueDO.java`

- `class ExtendValueDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/FamelogDO.java`

- `class FamelogDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/FamilyCharacterDO.java`

- `class FamilyCharacterDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/FamilyEntitlementDO.java`

- `class FamilyEntitlementDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/FlywaySchemaHistoryDO.java`

- `class FlywaySchemaHistoryDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/FredstorageDO.java`

- `class FredstorageDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/GachaponRewardDO.java`

- `class GachaponRewardDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/GachaponRewardPoolDO.java`

- `class GachaponRewardPoolDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/GameConfigDO.java`

- `class GameConfigDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/GiftsDO.java`

- `class GiftsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/GuildsDO.java`

- `class GuildsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/HpMpAlertDO.java`

- `class HpMpAlertDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/HwidaccountsDO.java`

- `class HwidaccountsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/HwidbansDO.java`

- `class HwidbansDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/InventoryequipmentDO.java`

- `class InventoryequipmentDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/InventoryitemsDO.java`

- `class InventoryitemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/InventorymerchantDO.java`

- `class InventorymerchantDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/IpbansDO.java`

- `class IpbansDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/KeymapDO.java`

- `class KeymapDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/LangResourcesDO.java`

- `class LangResourcesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MacbansDO.java`

- `class MacbansDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MacfiltersDO.java`

- `class MacfiltersDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MakercreatedataDO.java`

- `class MakercreatedataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MakerreagentdataDO.java`

- `class MakerreagentdataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MakerrecipedataDO.java`

- `class MakerrecipedataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MakerrewarddataDO.java`

- `class MakerrewarddataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MarriagesDO.java`

- `class MarriagesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MedalmapsDO.java`

- `class MedalmapsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ModifiedCashItemDO.java`

- `class ModifiedCashItemDO`：领域类型或功能模块，职责由同名文件实现定义。
  - `public boolean isSelling()`：进行条件判定并返回布尔结果。
  - `public Item toItem()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ModifiedCashItemDO clone()`：通用业务逻辑入口，需结合实现查看细节。

## `dao/entity/MonsterbookDO.java`

- `class MonsterbookDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MonstercarddataDO.java`

- `class MonstercarddataDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MtsCartDO.java`

- `class MtsCartDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/MtsItemsDO.java`

- `class MtsItemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NamechangesDO.java`

- `class NamechangesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NewyearDO.java`

- `class NewyearDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NotesDO.java`

- `class NotesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NxcodeDO.java`

- `class NxcodeDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NxcodeItemsDO.java`

- `class NxcodeItemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/NxcouponsDO.java`

- `class NxcouponsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PetignoresDO.java`

- `class PetignoresDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PetsDO.java`

- `class PetsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PlayerdiseasesDO.java`

- `class PlayerdiseasesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PlayernpcsDO.java`

- `class PlayernpcsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PlayernpcsEquipDO.java`

- `class PlayernpcsEquipDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PlayernpcsFieldDO.java`

- `class PlayernpcsFieldDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/PlifeDO.java`

- `class PlifeDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/QuestactionsDO.java`

- `class QuestactionsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/QuestprogressDO.java`

- `class QuestprogressDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/QuestrequirementsDO.java`

- `class QuestrequirementsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/QueststatusDO.java`

- `class QueststatusDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/QuickslotkeymappedDO.java`

- `class QuickslotkeymappedDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ReactordropsDO.java`

- `class ReactordropsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ReportsDO.java`

- `class ReportsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ResponsesDO.java`

- `class ResponsesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/RingsDO.java`

- `class RingsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/SavedlocationsDO.java`

- `class SavedlocationsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ServerQueueDO.java`

- `class ServerQueueDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ShopitemsDO.java`

- `class ShopitemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/ShopsDO.java`

- `class ShopsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/SkillmacrosDO.java`

- `class SkillmacrosDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/SkillsDO.java`

- `class SkillsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/SpecialcashitemsDO.java`

- `class SpecialcashitemsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/StoragesDO.java`

- `class StoragesDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/TrocklocationsDO.java`

- `class TrocklocationsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/WishlistsDO.java`

- `class WishlistsDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/entity/WorldtransfersDO.java`

- `class WorldtransfersDO`：领域类型或功能模块，职责由同名文件实现定义。

## `dao/mapper/AccountsMapper.java`

- `interface AccountsMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `void updateAllLoggedIn(Integer value)`：更新已有对象/配置/缓存。
  - `AccountsDO selectOneByName(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `void addAccount(AccountsDO accountsDO)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/AllianceMapper.java`

- `interface AllianceMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/AllianceguildsMapper.java`

- `interface AllianceguildsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/AreaInfoMapper.java`

- `interface AreaInfoMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/AutobanConfigMapper.java`

- `interface AutobanConfigMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/BbsRepliesMapper.java`

- `interface BbsRepliesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/BbsThreadsMapper.java`

- `interface BbsThreadsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/BosslogDailyMapper.java`

- `interface BosslogDailyMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/BosslogWeeklyMapper.java`

- `interface BosslogWeeklyMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/BuddiesMapper.java`

- `interface BuddiesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/CharactersMapper.java`

- `interface CharactersMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `void updateAllHasMerchant(Integer value)`：更新已有对象/配置/缓存。
  - `List<CharactersDO> selectIdAndWorldListByAccountId(int accountId)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/CommandInfoMapper.java`

- `interface CommandInfoMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/CooldownsMapper.java`

- `interface CooldownsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/DropDataGlobalMapper.java`

- `interface DropDataGlobalMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/DropDataMapper.java`

- `interface DropDataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/DueyitemsMapper.java`

- `interface DueyitemsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/DueypackagesMapper.java`

- `interface DueypackagesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/EventstatsMapper.java`

- `interface EventstatsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ExtendValueMapper.java`

- `interface ExtendValueMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `void clean(@Param("extendType") String extendType, @Param("createTime") Date createTime)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/FamelogMapper.java`

- `interface FamelogMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/FamilyCharacterMapper.java`

- `interface FamilyCharacterMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/FamilyEntitlementMapper.java`

- `interface FamilyEntitlementMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/FlywaySchemaHistoryMapper.java`

- `interface FlywaySchemaHistoryMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/FredstorageMapper.java`

- `interface FredstorageMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/GachaponRewardMapper.java`

- `interface GachaponRewardMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/GachaponRewardPoolMapper.java`

- `interface GachaponRewardPoolMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/GameConfigMapper.java`

- `interface GameConfigMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/GiftsMapper.java`

- `interface GiftsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/GuildsMapper.java`

- `interface GuildsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/HpMpAlertMapper.java`

- `interface HpMpAlertMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/HwidaccountsMapper.java`

- `interface HwidaccountsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/HwidbansMapper.java`

- `interface HwidbansMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/InventoryequipmentMapper.java`

- `interface InventoryequipmentMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/InventoryitemsMapper.java`

- `interface InventoryitemsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/InventorymerchantMapper.java`

- `interface InventorymerchantMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/IpbansMapper.java`

- `interface IpbansMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/KeymapMapper.java`

- `interface KeymapMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/LangResourcesMapper.java`

- `interface LangResourcesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MacbansMapper.java`

- `interface MacbansMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MacfiltersMapper.java`

- `interface MacfiltersMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MakercreatedataMapper.java`

- `interface MakercreatedataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MakerreagentdataMapper.java`

- `interface MakerreagentdataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MakerrecipedataMapper.java`

- `interface MakerrecipedataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MakerrewarddataMapper.java`

- `interface MakerrewarddataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MarriagesMapper.java`

- `interface MarriagesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MedalmapsMapper.java`

- `interface MedalmapsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ModifiedCashItemMapper.java`

- `interface ModifiedCashItemMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MonsterbookMapper.java`

- `interface MonsterbookMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MonstercarddataMapper.java`

- `interface MonstercarddataMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MtsCartMapper.java`

- `interface MtsCartMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/MtsItemsMapper.java`

- `interface MtsItemsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/NamechangesMapper.java`

- `interface NamechangesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/NewyearMapper.java`

- `interface NewyearMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/NotesMapper.java`

- `interface NotesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/NxcodeItemsMapper.java`

- `interface NxcodeItemsMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `void clearExpirations(long timeClear)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/NxcodeMapper.java`

- `interface NxcodeMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `void clearExpirations(long timeClear)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/NxcouponsMapper.java`

- `interface NxcouponsMapper`：数据访问层，负责 SQL 映射与实体读写。
  - `List<Integer> selectActiveCouponIds(@Param("weekDay") int weekDay, @Param("hourDay") int hourDay)`：通用业务逻辑入口，需结合实现查看细节。

## `dao/mapper/PetignoresMapper.java`

- `interface PetignoresMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PetsMapper.java`

- `interface PetsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PlayerdiseasesMapper.java`

- `interface PlayerdiseasesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PlayernpcsEquipMapper.java`

- `interface PlayernpcsEquipMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PlayernpcsFieldMapper.java`

- `interface PlayernpcsFieldMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PlayernpcsMapper.java`

- `interface PlayernpcsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/PlifeMapper.java`

- `interface PlifeMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/QuestactionsMapper.java`

- `interface QuestactionsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/QuestprogressMapper.java`

- `interface QuestprogressMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/QuestrequirementsMapper.java`

- `interface QuestrequirementsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/QueststatusMapper.java`

- `interface QueststatusMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/QuickslotkeymappedMapper.java`

- `interface QuickslotkeymappedMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ReactordropsMapper.java`

- `interface ReactordropsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ReportsMapper.java`

- `interface ReportsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ResponsesMapper.java`

- `interface ResponsesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/RingsMapper.java`

- `interface RingsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/SavedlocationsMapper.java`

- `interface SavedlocationsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ServerQueueMapper.java`

- `interface ServerQueueMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ShopitemsMapper.java`

- `interface ShopitemsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/ShopsMapper.java`

- `interface ShopsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/SkillmacrosMapper.java`

- `interface SkillmacrosMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/SkillsMapper.java`

- `interface SkillsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/SpecialcashitemsMapper.java`

- `interface SpecialcashitemsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/StoragesMapper.java`

- `interface StoragesMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/TrocklocationsMapper.java`

- `interface TrocklocationsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/WishlistsMapper.java`

- `interface WishlistsMapper`：数据访问层，负责 SQL 映射与实体读写。

## `dao/mapper/WorldtransfersMapper.java`

- `interface WorldtransfersMapper`：数据访问层，负责 SQL 映射与实体读写。

## `exception/BaseErrorInfoInterface.java`

- `interface BaseErrorInfoInterface`：领域类型或功能模块，职责由同名文件实现定义。
  - `Integer getResultCode()`：读取并返回状态/数据。
  - `String getResultMsg()`：读取并返回状态/数据。

## `exception/BizException.java`

- `class BizException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BizException()`：通用业务逻辑入口，需结合实现查看细节。
  - `public BizException(BaseErrorInfoInterface errorInfoInterface)`：通用业务逻辑入口，需结合实现查看细节。
  - `public BizException(BaseErrorInfoInterface errorInfoInterface, Throwable cause)`：通用业务逻辑入口，需结合实现查看细节。
  - `public BizException(String errorMsg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public BizException(Integer errorCode, String errorMsg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public BizException(Integer errorCode, String errorMsg, Throwable cause)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static BizException illegalArgument()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static BizException illegalArgument(String errorMsg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void throwIllegalArgument()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void throwIllegalArgument(String errorMsg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getMessage()`：读取并返回状态/数据。
  - `public Throwable fillInStackTrace()`：通用业务逻辑入口，需结合实现查看细节。

## `exception/BizExceptionEnum.java`

- `enum BizExceptionEnum`：领域类型或功能模块，职责由同名文件实现定义。
  - `SUCCESS(20000, I18nUtil.getExceptionMessage("SUCCESS")),`：通用业务逻辑入口，需结合实现查看细节。
  - `BODY_NOT_MATCH(40000, I18nUtil.getExceptionMessage("BODY_NOT_MATCH")),`：通用业务逻辑入口，需结合实现查看细节。
  - `REQUEST_METHOD_SUPPORT(40001, I18nUtil.getExceptionMessage("REQUEST_METHOD_SUPPORT")),`：通用业务逻辑入口，需结合实现查看细节。
  - `ILLEGAL_PARAMETERS(40002, I18nUtil.getExceptionMessage("ILLEGAL_PARAMETERS")),`：通用业务逻辑入口，需结合实现查看细节。
  - `NOT_FOUND(40004, I18nUtil.getExceptionMessage("NOT_FOUND")),`：通用业务逻辑入口，需结合实现查看细节。
  - `INTERNAL_SERVER_ERROR(50000, I18nUtil.getExceptionMessage("INTERNAL_SERVER_ERROR")),`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVER_BUSY(50003, I18nUtil.getExceptionMessage("SERVER_BUSY"))`：通用业务逻辑入口，需结合实现查看细节。
  - `BizExceptionEnum(Integer resultCode, String resultMsg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Integer getResultCode()`：读取并返回状态/数据。
  - `public String getResultMsg()`：读取并返回状态/数据。

## `exception/EmptyMovementException.java`

- `class EmptyMovementException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EmptyMovementException(InPacket inPacket)`：通用业务逻辑入口，需结合实现查看细节。

## `exception/EventInstanceInProgressException.java`

- `class EventInstanceInProgressException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventInstanceInProgressException(String eventName, String eventInstance)`：通用业务逻辑入口，需结合实现查看细节。

## `exception/GlobalExceptionHandler.java`

- `class GlobalExceptionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public ResultBody<Object> bizExceptionHandler(HttpServletRequest req, BizException e)`：处理事件/请求/消息分发。
  - `public ResultBody<Object> exceptionHandler(HttpServletRequest req, RuntimeException e)`：处理事件/请求/消息分发。
  - `public ResultBody<Object> exceptionHandler(HttpServletRequest req, ServletException e)`：处理事件/请求/消息分发。
  - `public ResultBody<Object> exceptionHandler(HttpServletRequest req, Exception e)`：处理事件/请求/消息分发。

## `exception/IdTypeNotSupportedException.java`

- `class IdTypeNotSupportedException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public IdTypeNotSupportedException()`：通用业务逻辑入口，需结合实现查看细节。
  - `public IdTypeNotSupportedException(String message)`：通用业务逻辑入口，需结合实现查看细节。

## `exception/NotEnabledException.java`

- `class NotEnabledException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NotEnabledException()`：通用业务逻辑入口，需结合实现查看细节。
  - `public NotEnabledException(String message)`：通用业务逻辑入口，需结合实现查看细节。

## `manager/ServerManager.java`

- `class ServerManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void setApplicationContext(@NonNull ApplicationContext applicationContext) throws BeansException`：写入或更新状态字段。
  - `public void run(ApplicationArguments args) throws Exception`：通用业务逻辑入口，需结合实现查看细节。
  - `public void destroy() throws Exception`：通用业务逻辑入口，需结合实现查看细节。

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

## `net/AbstractPacketHandler.java`

- `class AbstractPacketHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。
  - `protected static long currentServerTime()`：通用业务逻辑入口，需结合实现查看细节。

## `net/ChannelDependencies.java`


## `net/PacketHandler.java`

- `interface PacketHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `boolean validateState(Client c)`：校验输入参数或业务约束。

## `net/PacketProcessor.java`

- `class PacketProcessor`：领域类型或功能模块，职责由同名文件实现定义。
  - `private PacketProcessor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void registerGameHandlerDependencies(ChannelDependencies channelDependencies)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static PacketProcessor getLoginServerProcessor()`：读取并返回状态/数据。
  - `public static PacketProcessor getChannelServerProcessor(int world, int channel)`：读取并返回状态/数据。
  - `public PacketHandler getHandler(short packetId)`：读取并返回状态/数据。
  - `public void registerHandler(Opcode code, PacketHandler handler)`：处理事件/请求/消息分发。
  - `public synchronized static PacketProcessor getProcessor(int world, int channel)`：读取并返回状态/数据。
  - `public void reset(int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerCommonHandlers()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerLoginHandlers()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerChannelHandlers()`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/ClientCyphers.java`

- `class ClientCyphers`：领域类型或功能模块，职责由同名文件实现定义。
  - `private ClientCyphers(MapleAESOFB send, MapleAESOFB receive)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static ClientCyphers of(InitializationVector sendIv, InitializationVector receiveIv)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapleAESOFB getSendCypher()`：读取并返回状态/数据。
  - `public MapleAESOFB getReceiveCypher()`：读取并返回状态/数据。

## `net/encryption/InitializationVector.java`

- `class InitializationVector`：领域类型或功能模块，职责由同名文件实现定义。
  - `private InitializationVector(byte[] bytes)`：初始化模块、资源或运行时状态。
  - `public byte[] getBytes()`：读取并返回状态/数据。
  - `public static InitializationVector generateSend()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static InitializationVector generateReceive()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte getRandomByte()`：读取并返回状态/数据。

## `net/encryption/MapleAESOFB.java`

- `class MapleAESOFB`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapleAESOFB(InitializationVector iv, short mapleVersion)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte[] multiplyBytes(byte[] in, int count, int mul)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized byte[] crypt(byte[] data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void updateIv()`：更新已有对象/配置/缓存。
  - `public byte[] getPacketHeader(int length)`：读取并返回状态/数据。
  - `public static int getPacketLength(int packetHeader)`：读取并返回状态/数据。
  - `private boolean checkPacket(byte[] packet)`：校验输入参数或业务约束。
  - `public boolean isValidHeader(int packetHeader)`：进行条件判定并返回布尔结果。
  - `public static byte[] getNewIv(byte[] oldIv)`：读取并返回状态/数据。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte[] funnyShit(byte inputByte, byte[] in)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/MapleCustomEncryption.java`

- `class MapleCustomEncryption`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static byte rollLeft(byte in, int count)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte rollRight(byte in, int count)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static byte[] encryptData(byte[] data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static byte[] decryptData(byte[] data)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/PacketCodec.java`

- `class PacketCodec`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PacketCodec(ProtocolFactory protocolFactory)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/PacketDecoder.java`

- `class PacketDecoder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PacketDecoder(ProtocolFactory protocolFactory)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/PacketEncoder.java`

- `class PacketEncoder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PacketEncoder(ProtocolFactory protocolFactory)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/protocol/GMSV83PacketProtocol.java`

- `class GMSV83PacketProtocol`：领域类型或功能模块，职责由同名文件实现定义。
  - `public GMSV83PacketProtocol(ClientCyphers clientCyphers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int decodePacketLength(byte[] header)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int decodePacketLength(int header)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)`：通用业务逻辑入口，需结合实现查看细节。
  - `private byte[] getEncodedHeader(int length)`：读取并返回状态/数据。
  - `public void writeInitialUnencryptedHelloPacket(SocketChannel socketChannel, InitializationVector sendIv, InitializationVector recvIv, Client client)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/protocol/PacketProtocol.java`

- `interface PacketProtocol`：领域类型或功能模块，职责由同名文件实现定义。
  - `void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)`：通用业务逻辑入口，需结合实现查看细节。
  - `void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeInitialUnencryptedHelloPacket(SocketChannel socketChannel, InitializationVector sendIv, InitializationVector recvIv, Client client)`：通用业务逻辑入口，需结合实现查看细节。

## `net/encryption/protocol/ProtocolConstants.java`

- `class ProtocolConstants`：领域类型或功能模块，职责由同名文件实现定义。

## `net/encryption/protocol/ProtocolFactory.java`

- `class ProtocolFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ProtocolFactory(ClientCyphers clientCyphers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PacketProtocol getProtocol(short version)`：读取并返回状态/数据。

## `net/netty/AbstractServer.java`

- `class AbstractServer`：领域类型或功能模块，职责由同名文件实现定义。
  - `AbstractServer(int port)`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract void stop()`：通用业务逻辑入口，需结合实现查看细节。

## `net/netty/ChannelServer.java`

- `class ChannelServer`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ChannelServer(int port, int world, int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stop()`：通用业务逻辑入口，需结合实现查看细节。

## `net/netty/ChannelServerInitializer.java`

- `class ChannelServerInitializer`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ChannelServerInitializer(int world, int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void initChannel(SocketChannel socketChannel)`：初始化模块、资源或运行时状态。

## `net/netty/InvalidPacketHeaderException.java`

- `class InvalidPacketHeaderException`：领域类型或功能模块，职责由同名文件实现定义。
  - `public InvalidPacketHeaderException(String message, int header)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getHeader()`：读取并返回状态/数据。

## `net/netty/LoginServer.java`

- `class LoginServer`：领域类型或功能模块，职责由同名文件实现定义。
  - `public LoginServer(int port)`：处理认证/会话生命周期。
  - `public void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stop()`：通用业务逻辑入口，需结合实现查看细节。

## `net/netty/LoginServerInitializer.java`

- `class LoginServerInitializer`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void initChannel(SocketChannel socketChannel)`：初始化模块、资源或运行时状态。

## `net/netty/ServerChannelInitializer.java`

- `class ServerChannelInitializer`：领域类型或功能模块，职责由同名文件实现定义。
  - `String getRemoteAddress(Channel channel)`：读取并返回状态/数据。
  - `void initPipeline(SocketChannel socketChannel, Client client)`：初始化模块、资源或运行时状态。
  - `private void setUpHandlers(ChannelPipeline pipeline, ProtocolFactory protocolFactory, Client client)`：写入或更新状态字段。

## `net/opcodes/Opcode.java`

- `interface Opcode`：领域类型或功能模块，职责由同名文件实现定义。
  - `int getValue()`：读取并返回状态/数据。
  - `String getName()`：读取并返回状态/数据。

## `net/opcodes/RecvOpcode.java`

- `enum RecvOpcode`：领域类型或功能模块，职责由同名文件实现定义。
  - `CUSTOM_PACKET(0x3713),//13 37 lol // 自定义封包`：通用业务逻辑入口，需结合实现查看细节。
  - `LOGIN_PASSWORD(0x01), // 登录密码`：处理认证/会话生命周期。
  - `GUEST_LOGIN(0x02), // 游客登录`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERLIST_REREQUEST(0x04), // 重新请求服务器列表`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARLIST_REQUEST(0x05), // 请求角色列表`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERSTATUS_REQUEST(0x06), // 请求服务器状态`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCEPT_TOS(0x07), // 接受服务条款`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_GENDER(0x08), // 设置性别`：写入或更新状态字段。
  - `AFTER_LOGIN(0x09), // 登录后操作`：通用业务逻辑入口，需结合实现查看细节。
  - `REGISTER_PIN(0x0A), // 注册PIN码`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERLIST_REQUEST(0x0B), // 请求服务器列表`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_DC(0x0C), // 玩家断开连接`：通用业务逻辑入口，需结合实现查看细节。
  - `VIEW_ALL_CHAR(0x0D), // 查看所有角色`：通用业务逻辑入口，需结合实现查看细节。
  - `PICK_ALL_CHAR(0x0E), // 选择所有角色`：通用业务逻辑入口，需结合实现查看细节。
  - `NAME_TRANSFER(0x10), // 名称转移`：通用业务逻辑入口，需结合实现查看细节。
  - `WORLD_TRANSFER(0x12), // 世界转移`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAR_SELECT(0x13), // 角色选择`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_LOGGEDIN(0x14), // 玩家已登录`：通用业务逻辑入口，需结合实现查看细节。
  - `CHECK_CHAR_NAME(0x15), // 检查角色名称`：校验输入参数或业务约束。
  - `CREATE_CHAR(0x16), // 创建角色`：创建对象、会话或业务记录。
  - `DELETE_CHAR(0x17), // 删除角色`：删除对象、关系或临时状态。
  - `PONG(0x18), // 心跳响应`：通用业务逻辑入口，需结合实现查看细节。
  - `CLIENT_START_ERROR(0x19), // 客户端启动错误`：通用业务逻辑入口，需结合实现查看细节。
  - `CLIENT_ERROR(0x1A), // 客户端错误`：通用业务逻辑入口，需结合实现查看细节。
  - `STRANGE_DATA(0x1B), // 奇怪的数据`：通用业务逻辑入口，需结合实现查看细节。
  - `RELOG(0x1C), // 重新登录`：通用业务逻辑入口，需结合实现查看细节。
  - `REGISTER_PIC(0x1D), // 注册图片`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAR_SELECT_WITH_PIC(0x1E), // 带图片的角色选择`：通用业务逻辑入口，需结合实现查看细节。
  - `VIEW_ALL_PIC_REGISTER(0x1F), // 查看所有注册图片`：通用业务逻辑入口，需结合实现查看细节。
  - `VIEW_ALL_WITH_PIC(0x20), // 查看所有带图片`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANGE_MAP(0x26), // 更改地图`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANGE_CHANNEL(0x27), // 更改频道`：通用业务逻辑入口，需结合实现查看细节。
  - `ENTER_CASHSHOP(0x28), // 进入现金商店`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_PLAYER(0x29), // 移动玩家`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_CHAIR(0x2A), // 取消椅子`：进行条件判定并返回布尔结果。
  - `USE_CHAIR(0x2B), // 使用椅子`：通用业务逻辑入口，需结合实现查看细节。
  - `CLOSE_RANGE_ATTACK(0x2C), // 近战攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `RANGED_ATTACK(0x2D), // 远程攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_ATTACK(0x2E), // 魔法攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `TOUCH_MONSTER_ATTACK(0x2F), // 触碰怪物攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `TAKE_DAMAGE(0x30), // 受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `GENERAL_CHAT(0x31), // 通用聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `CLOSE_CHALKBOARD(0x32), // 关闭黑板`：通用业务逻辑入口，需结合实现查看细节。
  - `FACE_EXPRESSION(0x33), // 表情符号`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_ITEMEFFECT(0x34), // 使用物品效果`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_DEATHITEM(0x35), // 使用死亡物品`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_BANISH_PLAYER(0x38), // 怪物驱逐玩家`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_BOOK_COVER(0x39), // 怪物图鉴封面`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_TALK(0x3A), // NPC对话`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOTE_STORE(0x3B), // 远程商店`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_TALK_MORE(0x3C), // 继续NPC对话`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_SHOP(0x3D), // NPC商店`：通用业务逻辑入口，需结合实现查看细节。
  - `STORAGE(0x3E), // 仓库`：通用业务逻辑入口，需结合实现查看细节。
  - `HIRED_MERCHANT_REQUEST(0x3F), // 请求雇佣商人`：通用业务逻辑入口，需结合实现查看细节。
  - `FREDRICK_ACTION(0x40), // Fredrick操作`：通用业务逻辑入口，需结合实现查看细节。
  - `DUEY_ACTION(0x41), // Duey操作`：通用业务逻辑入口，需结合实现查看细节。
  - `OWL_ACTION(0x42),   // 发送最常用的信息给客户端     sends most searched info to client`：通用业务逻辑入口，需结合实现查看细节。
  - `OWL_WARP(0x43),     // 处理玩家传送到商店        handles player warp to store`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_SHOP(0x44), // 管理员商店`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_SORT(0x45), // 整理物品`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_SORT2(0x46), // 整理物品2`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_MOVE(0x47), // 移动物品`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_ITEM(0x48), // 使用物品`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_ITEM_EFFECT(0x49), // 取消物品效果`：进行条件判定并返回布尔结果。
  - `USE_SUMMON_BAG(0x4B), // 使用召唤袋`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_FOOD(0x4C), // 宠物食物`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_MOUNT_FOOD(0x4D), // 使用坐骑食物`：通用业务逻辑入口，需结合实现查看细节。
  - `SCRIPTED_ITEM(0x4E), // 脚本物品`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_CASH_ITEM(0x4F), // 使用现金物品`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_CATCH_ITEM(0x51), // 使用捕捉物品`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_SKILL_BOOK(0x52), // 使用技能书`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_TELEPORT_ROCK(0x54), // 使用传送石`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_RETURN_SCROLL(0x55), // 使用返回卷轴`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_UPGRADE_SCROLL(0x56), // 使用升级卷轴`：通用业务逻辑入口，需结合实现查看细节。
  - `DISTRIBUTE_AP(0x57), // 分配能力点`：通用业务逻辑入口，需结合实现查看细节。
  - `AUTO_DISTRIBUTE_AP(0x58), // 自动分配能力点`：通用业务逻辑入口，需结合实现查看细节。
  - `HEAL_OVER_TIME(0x59), // 持续治疗`：通用业务逻辑入口，需结合实现查看细节。
  - `DISTRIBUTE_SP(0x5A), // 分配技能点`：通用业务逻辑入口，需结合实现查看细节。
  - `SPECIAL_MOVE(0x5B), // 特殊移动`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_BUFF(0x5C), // 取消增益效果`：进行条件判定并返回布尔结果。
  - `SKILL_EFFECT(0x5D), // 技能效果`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO_DROP(0x5E), // 金币掉落`：通用业务逻辑入口，需结合实现查看细节。
  - `GIVE_FAME(0x5F), // 赠送声望`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAR_INFO_REQUEST(0x61), // 请求角色信息`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_PET(0x62), // 生成宠物`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_DEBUFF(0x63), // 取消减益效果`：进行条件判定并返回布尔结果。
  - `CHANGE_MAP_SPECIAL(0x64), // 特殊更改地图`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_INNER_PORTAL(0x65), // 使用内部传送门`：通用业务逻辑入口，需结合实现查看细节。
  - `TROCK_ADD_MAP(0x66), // 添加传送岩地图`：通用业务逻辑入口，需结合实现查看细节。
  - `REPORT(0x6A), // 报告`：通用业务逻辑入口，需结合实现查看细节。
  - `QUEST_ACTION(0x6B), // 任务操作`：通用业务逻辑入口，需结合实现查看细节。
  - `GRENADE_EFFECT(0x6D), // 手榴弹效果`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL_MACRO(0x6E), // 技能宏`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_ITEM_REWARD(0x70), // 使用物品奖励`：通用业务逻辑入口，需结合实现查看细节。
  - `MAKER_SKILL(0x71), // 制作器技能`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_TREASUER_CHEST(0x73), // 使用宝箱`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_REMOTE(0x74), // 使用遥控器`：通用业务逻辑入口，需结合实现查看细节。
  - `WATER_OF_LIFE(0x75), // 生命之水`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_CHAT(0x76), // 管理员聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `MULTI_CHAT(0x77), // 多人聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `WHISPER(0x78), // 密语`：通用业务逻辑入口，需结合实现查看细节。
  - `SPOUSE_CHAT(0x79), // 配偶聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `MESSENGER(0x7A), // 消息传递`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_INTERACTION(0x7B), // 玩家互动`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_OPERATION(0x7C), // 组队操作`：通用业务逻辑入口，需结合实现查看细节。
  - `DENY_PARTY_REQUEST(0x7D), // 拒绝组队请求`：通用业务逻辑入口，需结合实现查看细节。
  - `GUILD_OPERATION(0x7E), // 公会操作`：通用业务逻辑入口，需结合实现查看细节。
  - `DENY_GUILD_REQUEST(0x7F), // 拒绝公会请求`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_COMMAND(0x80), // 管理员命令`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_LOG(0x81), // 管理员日志`：通用业务逻辑入口，需结合实现查看细节。
  - `BUDDYLIST_MODIFY(0x82), // 修改好友列表`：通用业务逻辑入口，需结合实现查看细节。
  - `NOTE_ACTION(0x83), // 笔记操作`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_DOOR(0x85), // 使用门`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANGE_KEYMAP(0x87), // 更改键盘映射`：通用业务逻辑入口，需结合实现查看细节。
  - `RPS_ACTION(0x88), // 石头剪刀布操作`：通用业务逻辑入口，需结合实现查看细节。
  - `RING_ACTION(0x89), // 戒指操作`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_ACTION(0x8A), // 结婚操作`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_TALK(0x8B), // 结婚对话`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_TALK_MORE(0x8B), // 继续结婚对话`：通用业务逻辑入口，需结合实现查看细节。
  - `ALLIANCE_OPERATION(0x8F), // 联盟操作`：通用业务逻辑入口，需结合实现查看细节。
  - `DENY_ALLIANCE_REQUEST(0x90), // 拒绝联盟请求`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_FAMILY_PEDIGREE(0x91), // 打开家族谱系`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_FAMILY(0x92), // 打开家族`：通用业务逻辑入口，需结合实现查看细节。
  - `ADD_FAMILY(0x93), // 添加家族`：通用业务逻辑入口，需结合实现查看细节。
  - `SEPARATE_FAMILY_BY_SENIOR(0x94), // 通过长辈分离家族`：通用业务逻辑入口，需结合实现查看细节。
  - `SEPARATE_FAMILY_BY_JUNIOR(0x95), // 通过晚辈分离家族`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCEPT_FAMILY(0x96), // 接受家族邀请`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_FAMILY(0x97), // 使用家族功能`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANGE_FAMILY_MESSAGE(0x98), // 更改家族消息`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_SUMMON_RESPONSE(0x99), // 家族召唤响应`：通用业务逻辑入口，需结合实现查看细节。
  - `BBS_OPERATION(0x9B), // 论坛操作`：通用业务逻辑入口，需结合实现查看细节。
  - `ENTER_MTS(0x9C), // 进入MTS`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_SOLOMON_ITEM(0x9D), // 使用所罗门物品`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_GACHA_EXP(0x9E), // 使用扭蛋经验`：通用业务逻辑入口，需结合实现查看细节。
  - `NEW_YEAR_CARD_REQUEST(0x9F), // 新年贺卡请求`：创建对象、会话或业务记录。
  - `CASHSHOP_SURPRISE(0xA1), // 现金商店惊喜`：通用业务逻辑入口，需结合实现查看细节。
  - `CLICK_GUIDE(0xA2), // 点击引导`：通用业务逻辑入口，需结合实现查看细节。
  - `ARAN_COMBO_COUNTER(0xA3), // Aran连击计数器`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_PET(0xA7), // 移动宠物`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_CHAT(0xA8), // 宠物对话`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_COMMAND(0xA9), // 宠物命令`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_LOOT(0xAA), // 宠物拾取`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_AUTO_POT(0xAB), // 宠物自动使用药水`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EXCLUDE_ITEMS(0xAC), // 宠物排除物品`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_SUMMON(0xAF), // 移动召唤兽`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON_ATTACK(0xB0), // 召唤兽攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `DAMAGE_SUMMON(0xB1), // 召唤兽受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `BEHOLDER(0xB2), // Beholder（不明用途）`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_DRAGON(0xB5), // 移动龙`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANGE_QUICKSLOT(0xB7),//CP_QuickslotKeyMappedModified // 更改快捷栏`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_LIFE(0xBC), // 移动生命体`：通用业务逻辑入口，需结合实现查看细节。
  - `AUTO_AGGRO(0xBD), // 自动仇恨`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_DAMAGE_MOB(0xBF), // 场景中怪物受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_DAMAGE_MOB_FRIENDLY(0xC0), // 怪物对友好怪物造成伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_BOMB(0xC1), // 怪物炸弹`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_DAMAGE_MOB(0xC2), // 怪物对怪物造成伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_ACTION(0xC5), // NPC动作`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM_PICKUP(0xCA), // 捡起物品`：通用业务逻辑入口，需结合实现查看细节。
  - `DAMAGE_REACTOR(0xCD), // 反应堆受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `TOUCHING_REACTOR(0xCE), // 触碰反应堆`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_MAP_TRANSFER(0xCF), // 玩家地图转换`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLETV(0xFFFE),//Don't know // MapleTV（不知道）`：通用业务逻辑入口，需结合实现查看细节。
  - `SNOWBALL(0xD3), // 雪球`：通用业务逻辑入口，需结合实现查看细节。
  - `LEFT_KNOCKBACK(0xD4), // 左侧击退`：通用业务逻辑入口，需结合实现查看细节。
  - `COCONUT(0xD5), // 椰子`：通用业务逻辑入口，需结合实现查看细节。
  - `MATCH_TABLE(0xD6),//Would be cool if I ever get it to work :) // 匹配表（如果我能让它工作就好了 :））`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL(0xDA), // 怪物嘉年华`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_SEARCH_REGISTER(0xDC), // 注册组队搜索`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_SEARCH_START(0xDE), // 开始组队搜索`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_SEARCH_UPDATE(0xDF), // 更新组队搜索`：通用业务逻辑入口，需结合实现查看细节。
  - `CHECK_CASH(0xE4), // 检查现金`：校验输入参数或业务约束。
  - `CASHSHOP_OPERATION(0xE5), // 现金商店操作`：通用业务逻辑入口，需结合实现查看细节。
  - `COUPON_CODE(0xE6), // 优惠券代码`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_ITEMUI(0xEC), // 打开物品界面`：通用业务逻辑入口，需结合实现查看细节。
  - `CLOSE_ITEMUI(0xED), // 关闭物品界面`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_ITEMUI(0xEE), // 使用物品界面`：通用业务逻辑入口，需结合实现查看细节。
  - `MTS_OPERATION(0xFD), // MTS操作`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_MAPLELIFE(0x100), // 使用MapleLife`：通用业务逻辑入口，需结合实现查看细节。
  - `USE_HAMMER(0x104), // 使用锤子`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_HPMPALERT(0x1000), // 设置HP/MP警报`：写入或更新状态字段。
  - `RecvOpcode(int code)`：接收并解码输入数据。
  - `public int getValue()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。

## `net/opcodes/SendOpcode.java`

- `enum SendOpcode`：领域类型或功能模块，职责由同名文件实现定义。
  - `LOGIN_STATUS(0x00), // 登录状态`：处理认证/会话生命周期。
  - `GUEST_ID_LOGIN(0x01), // 游客ID登录`：通用业务逻辑入口，需结合实现查看细节。
  - `ACCOUNT_INFO(0x02), // 账户信息`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERSTATUS(0x03), // 服务器状态（CHECK_USER_LIMIT_RESULT）`：通用业务逻辑入口，需结合实现查看细节。
  - `GENDER_DONE(0x04), // 性别设置结果（SET_ACCOUNT_RESULT）`：通用业务逻辑入口，需结合实现查看细节。
  - `CONFIRM_EULA_RESULT(0x05), // EULA确认结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CHECK_PINCODE(0x06), // 检查PIN码`：校验输入参数或业务约束。
  - `UPDATE_PINCODE(0x07), // 更新PIN码`：更新已有对象/配置/缓存。
  - `VIEW_ALL_CHAR(0x08), // 查看所有角色`：通用业务逻辑入口，需结合实现查看细节。
  - `SELECT_CHARACTER_BY_VAC(0x09), // 通过VAC选择角色`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERLIST(0x0A), // 服务器列表`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARLIST(0x0B), // 角色列表`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVER_IP(0x0C), // 服务器IP`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAR_NAME_RESPONSE(0x0D), // 角色名称响应`：通用业务逻辑入口，需结合实现查看细节。
  - `ADD_NEW_CHAR_ENTRY(0x0E), // 添加新角色条目`：通用业务逻辑入口，需结合实现查看细节。
  - `DELETE_CHAR_RESPONSE(0x0F), // 删除角色响应`：删除对象、关系或临时状态。
  - `CHANGE_CHANNEL(0x10), // 更改频道`：通用业务逻辑入口，需结合实现查看细节。
  - `PING(0x11), // 心跳检测`：通用业务逻辑入口，需结合实现查看细节。
  - `KOREAN_INTERNET_CAFE_SHIT(0x12), // 韩国互联网咖啡无关紧要的内容，忽略`：通用业务逻辑入口，需结合实现查看细节。
  - `CHANNEL_SELECTED(0x14), // 频道已选择`：通用业务逻辑入口，需结合实现查看细节。
  - `HACKSHIELD_REQUEST(0x15), // 可能是RELOG_RESPONSE，无所谓`：通用业务逻辑入口，需结合实现查看细节。
  - `RELOG_RESPONSE(0x16), // 重新登录响应`：通用业务逻辑入口，需结合实现查看细节。
  - `CHECK_CRC_RESULT(0x19), // CRC检查结果`：校验输入参数或业务约束。
  - `LAST_CONNECTED_WORLD(0x1A), // 上次连接的世界`：通用业务逻辑入口，需结合实现查看细节。
  - `RECOMMENDED_WORLD_MESSAGE(0x1B), // 推荐世界消息`：通用业务逻辑入口，需结合实现查看细节。
  - `CHECK_SPW_RESULT(0x1C), // SPW检查结果`：校验输入参数或业务约束。
  - `INVENTORY_OPERATION(0x1D), // 物品栏操作`：通用业务逻辑入口，需结合实现查看细节。
  - `INVENTORY_GROW(0x1E), // 扩展物品栏`：通用业务逻辑入口，需结合实现查看细节。
  - `STAT_CHANGED(0x1F), // 状态改变`：通用业务逻辑入口，需结合实现查看细节。
  - `GIVE_BUFF(0x20), // 施加增益效果`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_BUFF(0x21), // 移除增益效果`：进行条件判定并返回布尔结果。
  - `FORCED_STAT_SET(0x22), // 强制设置状态`：通用业务逻辑入口，需结合实现查看细节。
  - `FORCED_STAT_RESET(0x23), // 强制重置状态`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_SKILLS(0x24), // 更新技能`：更新已有对象/配置/缓存。
  - `SKILL_USE_RESULT(0x25), // 技能使用结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAME_RESPONSE(0x26), // 声望响应`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_STATUS_INFO(0x27), // 显示状态信息`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_FULL_CLIENT_DOWNLOAD_LINK(0x28), // 打开完整客户端下载链接`：通用业务逻辑入口，需结合实现查看细节。
  - `MEMO_RESULT(0x29), // 备忘录结果`：通用业务逻辑入口，需结合实现查看细节。
  - `MAP_TRANSFER_RESULT(0x2A), // 地图转移结果`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_PHOTO(0x2B), // 结婚照片（ANTI_MACRO_RESULT在某些版本可能是这个）`：通用业务逻辑入口，需结合实现查看细节。
  - `CLAIM_RESULT(0x2D), // 领取结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CLAIM_AVAILABLE_TIME(0x2E), // 领取可用时间`：通用业务逻辑入口，需结合实现查看细节。
  - `CLAIM_STATUS_CHANGED(0x2F), // 领取状态改变`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_TAMING_MOB_INFO(0x30), // 设置驯服怪物信息`：写入或更新状态字段。
  - `QUEST_CLEAR(0x31), // 任务完成`：通用业务逻辑入口，需结合实现查看细节。
  - `ENTRUSTED_SHOP_CHECK_RESULT(0x32), // 委托商店检查结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL_LEARN_ITEM_RESULT(0x33), // 学习技能物品结果`：通用业务逻辑入口，需结合实现查看细节。
  - `GATHER_ITEM_RESULT(0x34), // 收集物品结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SORT_ITEM_RESULT(0x35), // 整理物品结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SUE_CHARACTER_RESULT(0x37), // 控诉角色结果`：通用业务逻辑入口，需结合实现查看细节。
  - `TRADE_MONEY_LIMIT(0x39), // 交易金钱限制`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_GENDER(0x3A), // 设置性别`：写入或更新状态字段。
  - `GUILD_BBS_PACKET(0x3B), // 公会公告板数据包`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAR_INFO(0x3D), // 角色信息`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_OPERATION(0x3E), // 组队操作`：通用业务逻辑入口，需结合实现查看细节。
  - `BUDDYLIST(0x3F), // 好友列表`：通用业务逻辑入口，需结合实现查看细节。
  - `GUILD_OPERATION(0x41), // 公会操作`：通用业务逻辑入口，需结合实现查看细节。
  - `ALLIANCE_OPERATION(0x42), // 联盟操作`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_PORTAL(0x43), // 生成传送门`：通用业务逻辑入口，需结合实现查看细节。
  - `SERVERMESSAGE(0x44), // 服务器消息`：通用业务逻辑入口，需结合实现查看细节。
  - `INCUBATOR_RESULT(0x45), // 孵化器结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOP_SCANNER_RESULT(0x46), // 商店扫描结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOP_LINK_RESULT(0x47), // 商店链接结果`：通用业务逻辑入口，需结合实现查看细节。
  - `MARRIAGE_REQUEST(0x48), // 结婚请求`：通用业务逻辑入口，需结合实现查看细节。
  - `MARRIAGE_RESULT(0x49), // 结婚结果`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_GIFT_RESULT(0x4A), // 结婚礼物结果`：通用业务逻辑入口，需结合实现查看细节。
  - `NOTIFY_MARRIED_PARTNER_MAP_TRANSFER(0x4B), // 通知结婚伴侣地图转移`：通用业务逻辑入口，需结合实现查看细节。
  - `CASH_PET_FOOD_RESULT(0x4C), // 宠物食物结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_WEEK_EVENT_MESSAGE(0x4D), // 设置周活动消息`：写入或更新状态字段。
  - `SET_POTION_DISCOUNT_RATE(0x4E), // 设置药水折扣率`：写入或更新状态字段。
  - `BRIDLE_MOB_CATCH_FAIL(0x4F), // 鞍具捕捉怪物失败`：通用业务逻辑入口，需结合实现查看细节。
  - `IMITATED_NPC_RESULT(0x50), // 仿冒NPC结果`：通用业务逻辑入口，需结合实现查看细节。
  - `IMITATED_NPC_DATA(0x51), // 仿冒NPC数据`：通用业务逻辑入口，需结合实现查看细节。
  - `LIMITED_NPC_DISABLE_INFO(0x52), // 限时NPC禁用信息`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_BOOK_SET_CARD(0x53), // 怪物图鉴设置卡片`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_BOOK_SET_COVER(0x54), // 怪物图鉴设置封面`：通用业务逻辑入口，需结合实现查看细节。
  - `HOUR_CHANGED(0x55), // 时间变化`：通用业务逻辑入口，需结合实现查看细节。
  - `MINIMAP_ON_OFF(0x56), // 小地图开关`：通用业务逻辑入口，需结合实现查看细节。
  - `CONSULT_AUTHKEY_UPDATE(0x57), // 咨询认证密钥更新`：通用业务逻辑入口，需结合实现查看细节。
  - `CLASS_COMPETITION_AUTHKEY_UPDATE(0x58), // 竞技场认证密钥更新`：通用业务逻辑入口，需结合实现查看细节。
  - `WEB_BOARD_AUTHKEY_UPDATE(0x59), // 网络论坛认证密钥更新`：通用业务逻辑入口，需结合实现查看细节。
  - `SESSION_VALUE(0x5A), // 会话值`：通用业务逻辑入口，需结合实现查看细节。
  - `PARTY_VALUE(0x5B), // 组队值`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_SET_VARIABLE(0x5C), // 字段设置变量`：通用业务逻辑入口，需结合实现查看细节。
  - `BONUS_EXP_CHANGED(0x5D), // 奖励经验值变化（猜测，不确定v83中的opcode）`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_CHART_RESULT(0x5E), // 家族图表结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_INFO_RESULT(0x5F), // 家族信息结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_RESULT(0x60), // 家族结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_JOIN_REQUEST(0x61), // 家族加入请求`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_JOIN_REQUEST_RESULT(0x62), // 家族加入请求结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_JOIN_ACCEPTED(0x63), // 家族加入接受`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_PRIVILEGE_LIST(0x64), // 家族权限列表`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_REP_GAIN(0x65), // 家族声望获得`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_NOTIFY_LOGIN_OR_LOGOUT(0x66), // 通知家族成员登录或登出`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_SET_PRIVILEGE(0x67), // 设置家族权限`：通用业务逻辑入口，需结合实现查看细节。
  - `FAMILY_SUMMON_REQUEST(0x68), // 家族召唤请求`：通用业务逻辑入口，需结合实现查看细节。
  - `NOTIFY_LEVELUP(0x69), // 通知等级提升`：通用业务逻辑入口，需结合实现查看细节。
  - `NOTIFY_MARRIAGE(0x6A), // 通知结婚`：通用业务逻辑入口，需结合实现查看细节。
  - `NOTIFY_JOB_CHANGE(0x6B), // 通知职业变更`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLE_TV_USE_RES(0x6D), // Maple TV使用结果（不是空白，是一个弹窗）`：通用业务逻辑入口，需结合实现查看细节。
  - `AVATAR_MEGAPHONE_RESULT(0x6E), // 头像喇叭结果（机器人无用）`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_AVATAR_MEGAPHONE(0x6F), // 设置头像喇叭`：写入或更新状态字段。
  - `CLEAR_AVATAR_MEGAPHONE(0x70), // 清除头像喇叭`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_NAME_CHANGE_RESULT(0x71), // 取消更改名字结果`：进行条件判定并返回布尔结果。
  - `CANCEL_TRANSFER_WORLD_RESULT(0x72), // 取消转移世界结果`：进行条件判定并返回布尔结果。
  - `DESTROY_SHOP_RESULT(0x73), // 销毁商店结果`：通用业务逻辑入口，需结合实现查看细节。
  - `FAKE_GM_NOTICE(0x74), // 假GM通知（坏家伙）`：通用业务逻辑入口，需结合实现查看细节。
  - `SUCCESS_IN_USE_GACHAPON_BOX(0x75), // 成功使用扭蛋机箱`：通用业务逻辑入口，需结合实现查看细节。
  - `NEW_YEAR_CARD_RES(0x76), // 新年贺卡结果`：创建对象、会话或业务记录。
  - `RANDOM_MORPH_RES(0x77), // 随机变身结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_NAME_CHANGE_BY_OTHER(0x78), // 由他人取消更改名字`：进行条件判定并返回布尔结果。
  - `SET_EXTRA_PENDANT_SLOT(0x79), // 设置额外饰品插槽`：写入或更新状态字段。
  - `SCRIPT_PROGRESS_MESSAGE(0x7A), // 脚本进度消息`：通用业务逻辑入口，需结合实现查看细节。
  - `DATA_CRC_CHECK_FAILED(0x7B), // 数据CRC检查失败`：通用业务逻辑入口，需结合实现查看细节。
  - `MACRO_SYS_DATA_INIT(0x7C), // 宏系统数据初始化`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_FIELD(0x7D), // 设置字段`：写入或更新状态字段。
  - `SET_ITC(0x7E), // 设置ITC`：写入或更新状态字段。
  - `SET_CASH_SHOP(0x7F), // 设置现金商店`：写入或更新状态字段。
  - `SET_BACK_EFFECT(0x80), // 设置背景特效`：写入或更新状态字段。
  - `SET_MAP_OBJECT_VISIBLE(0x81), // 设置地图对象可见性`：写入或更新状态字段。
  - `CLEAR_BACK_EFFECT(0x82), // 清除背景特效`：通用业务逻辑入口，需结合实现查看细节。
  - `BLOCKED_MAP(0x83), // 被阻止的地图`：通用业务逻辑入口，需结合实现查看细节。
  - `BLOCKED_SERVER(0x84), // 被阻止的服务器`：通用业务逻辑入口，需结合实现查看细节。
  - `FORCED_MAP_EQUIP(0x85), // 强制地图装备`：通用业务逻辑入口，需结合实现查看细节。
  - `MULTICHAT(0x86), // 多人聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `WHISPER(0x87), // 密语`：通用业务逻辑入口，需结合实现查看细节。
  - `SPOUSE_CHAT(0x88), // 配偶聊天`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON_ITEM_INAVAILABLE(0x89), // 在此地图无法使用召唤物品`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_EFFECT(0x8A), // 场景效果`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_OBSTACLE_ONOFF(0x8B), // 场景障碍物开关`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_OBSTACLE_ONOFF_LIST(0x8C), // 场景障碍物开关列表`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_OBSTACLE_ALL_RESET(0x8D), // 重置所有场景障碍物`：通用业务逻辑入口，需结合实现查看细节。
  - `BLOW_WEATHER(0x8E), // 吹风天气效果`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAY_JUKEBOX(0x8F), // 播放点唱机`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_RESULT(0x90), // 管理员结果`：通用业务逻辑入口，需结合实现查看细节。
  - `OX_QUIZ(0x91), // QUIZ（OX问答）`：通用业务逻辑入口，需结合实现查看细节。
  - `GMEVENT_INSTRUCTIONS(0x92), // DESC（游戏事件说明）`：通用业务逻辑入口，需结合实现查看细节。
  - `CLOCK(0x93), // 时钟`：通用业务逻辑入口，需结合实现查看细节。
  - `CONTI_MOVE(0x94), // 连续移动`：通用业务逻辑入口，需结合实现查看细节。
  - `CONTI_STATE(0x95), // 连续状态`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_QUEST_CLEAR(0x96), // 设置任务完成`：写入或更新状态字段。
  - `SET_QUEST_TIME(0x97), // 设置任务时间`：写入或更新状态字段。
  - `ARIANT_RESULT(0x98),    // thanks lrenex // ARIANT结果`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_OBJECT_STATE(0x99), // 设置物体状态`：写入或更新状态字段。
  - `STOP_CLOCK(0x9A), // 停止时钟`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT_ARENA_SHOW_RESULT(0x9B), // ARIANT竞技场显示结果`：通用业务逻辑入口，需结合实现查看细节。
  - `PYRAMID_GAUGE(0x9D), // 金字塔计数器`：通用业务逻辑入口，需结合实现查看细节。
  - `PYRAMID_SCORE(0x9E), // 金字塔分数`：通用业务逻辑入口，需结合实现查看细节。
  - `QUICKSLOT_INIT(0x9F),//LP_QuickslotMappedInit // 快捷栏初始化`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_PLAYER(0xA0), // 生成玩家`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_PLAYER_FROM_MAP(0xA1), // 从地图移除玩家`：删除对象、关系或临时状态。
  - `CHATTEXT(0xA2), // 聊天文本（类型0）`：通用业务逻辑入口，需结合实现查看细节。
  - `CHATTEXT1(0xA3), // 聊天文本（类型1）`：通用业务逻辑入口，需结合实现查看细节。
  - `CHALKBOARD(0xA4), // 黑板`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_CHAR_BOX(0xA5), // 更新角色盒子`：更新已有对象/配置/缓存。
  - `SHOW_CONSUME_EFFECT(0xA6), // 显示消耗效果`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_SCROLL_EFFECT(0xA7), // 显示卷轴效果`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_PET(0xA8), // 生成宠物`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_PET(0xAA), // 移动宠物`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_CHAT(0xAB), // 宠物对话`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_NAMECHANGE(0xAC), // 更改宠物名字`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_EXCEPTION_LIST(0xAD), // 宠物异常列表`：通用业务逻辑入口，需结合实现查看细节。
  - `PET_COMMAND(0xAE), // 宠物命令`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_SPECIAL_MAPOBJECT(0xAF), // 生成特殊地图对象`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_SPECIAL_MAPOBJECT(0xB0), // 移除特殊地图对象`：删除对象、关系或临时状态。
  - `MOVE_SUMMON(0xB1), // 移动召唤兽`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON_ATTACK(0xB2), // 召唤兽攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `DAMAGE_SUMMON(0xB3), // 召唤兽受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON_SKILL(0xB4), // 召唤兽技能`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_DRAGON(0xB5), // 生成龙`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_DRAGON(0xB6), // 移动龙`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_DRAGON(0xB7), // 移除龙`：删除对象、关系或临时状态。
  - `MOVE_PLAYER(0xB9), // 移动玩家`：通用业务逻辑入口，需结合实现查看细节。
  - `CLOSE_RANGE_ATTACK(0xBA), // 近战攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `RANGED_ATTACK(0xBB), // 远程攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_ATTACK(0xBC), // 魔法攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `ENERGY_ATTACK(0xBD), // 能量攻击`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL_EFFECT(0xBE), // 技能效果`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_SKILL_EFFECT(0xBF), // 取消技能效果`：进行条件判定并返回布尔结果。
  - `DAMAGE_PLAYER(0xC0), // 玩家受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `FACIAL_EXPRESSION(0xC1), // 表情符号`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_ITEM_EFFECT(0xC2), // 显示物品效果`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_CHAIR(0xC4), // 显示椅子`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_CHAR_LOOK(0xC5), // 更新角色外观`：更新已有对象/配置/缓存。
  - `SHOW_FOREIGN_EFFECT(0xC6), // 显示远程效果`：通用业务逻辑入口，需结合实现查看细节。
  - `GIVE_FOREIGN_BUFF(0xC7), // 给予远程增益效果`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_FOREIGN_BUFF(0xC8), // 取消远程增益效果`：进行条件判定并返回布尔结果。
  - `UPDATE_PARTYMEMBER_HP(0xC9), // 更新组队成员HP`：更新已有对象/配置/缓存。
  - `GUILD_NAME_CHANGED(0xCA), // 公会名称改变`：通用业务逻辑入口，需结合实现查看细节。
  - `GUILD_MARK_CHANGED(0xCB), // 公会标志改变`：通用业务逻辑入口，需结合实现查看细节。
  - `THROW_GRENADE(0xCC), // 抛掷手榴弹`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_CHAIR(0xCD), // 取消椅子`：进行条件判定并返回布尔结果。
  - `SHOW_ITEM_GAIN_INCHAT(0xCE), // 在聊天中显示获得物品`：通用业务逻辑入口，需结合实现查看细节。
  - `DOJO_WARP_UP(0xCF), // 武道馆传送准备`：通用业务逻辑入口，需结合实现查看细节。
  - `LUCKSACK_PASS(0xD0), // 幸运袋成功`：通用业务逻辑入口，需结合实现查看细节。
  - `LUCKSACK_FAIL(0xD1), // 幸运袋失败`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO_BAG_MESSAGE(0xD2), // 金币背包消息`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_QUEST_INFO(0xD3), // 更新任务信息`：更新已有对象/配置/缓存。
  - `ON_NOTIFY_HP_DEC_BY_FIELD(0xD4), // 通知字段减少HP`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_HINT(0xD6), // 玩家提示`：通用业务逻辑入口，需结合实现查看细节。
  - `MAKER_RESULT(0xD9), // 制作器结果`：通用业务逻辑入口，需结合实现查看细节。
  - `KOREAN_EVENT(0xDB), // 韩国活动`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_UI(0xDC), // 打开UI`：通用业务逻辑入口，需结合实现查看细节。
  - `LOCK_UI(0xDD), // 锁定UI`：通用业务逻辑入口，需结合实现查看细节。
  - `DISABLE_UI(0xDE), // 禁用UI`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_GUIDE(0xDF), // 生成引导者`：通用业务逻辑入口，需结合实现查看细节。
  - `TALK_GUIDE(0xE0), // 引导者对话`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_COMBO(0xE1), // 显示连击`：通用业务逻辑入口，需结合实现查看细节。
  - `COOLDOWN(0xEA), // 冷却时间`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_MONSTER(0xEC), // 生成怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `KILL_MONSTER(0xED), // 击杀怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_MONSTER_CONTROL(0xEE), // 控制生成怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_MONSTER(0xEF), // 移动怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVE_MONSTER_RESPONSE(0xF0), // 移动怪物响应`：通用业务逻辑入口，需结合实现查看细节。
  - `APPLY_MONSTER_STATUS(0xF2), // 应用怪物状态`：通用业务逻辑入口，需结合实现查看细节。
  - `CANCEL_MONSTER_STATUS(0xF3), // 取消怪物状态`：进行条件判定并返回布尔结果。
  - `RESET_MONSTER_ANIMATION(0xF4),//LOL? o.o // 重置怪物动画`：通用业务逻辑入口，需结合实现查看细节。
  - `DAMAGE_MONSTER(0xF6), // 怪物受到伤害`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT_THING(0xF9), // ARIANT相关操作`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_MONSTER_HP(0xFA), // 显示怪物HP`：通用业务逻辑入口，需结合实现查看细节。
  - `CATCH_MONSTER(0xFB), // 捕捉怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `CATCH_MONSTER_WITH_ITEM(0xFC), // 使用物品捕捉怪物`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOW_MAGNET(0xFD), // 显示磁铁效果`：通用业务逻辑入口，需结合实现查看细节。
  - `SPAWN_NPC(0x101), // 生成NPC`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_NPC(0x102), // 移除NPC`：删除对象、关系或临时状态。
  - `SPAWN_NPC_REQUEST_CONTROLLER(0x103), // 请求控制NPC生成`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_ACTION(0x104), // NPC动作`：通用业务逻辑入口，需结合实现查看细节。
  - `SET_NPC_SCRIPTABLE(0x107), // 设置NPC可脚本化`：写入或更新状态字段。
  - `SPAWN_HIRED_MERCHANT(0x109), // 生成雇佣商人`：通用业务逻辑入口，需结合实现查看细节。
  - `DESTROY_HIRED_MERCHANT(0x10A), // 销毁雇佣商人`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_HIRED_MERCHANT(0x10B), // 更新雇佣商人`：更新已有对象/配置/缓存。
  - `DROP_ITEM_FROM_MAPOBJECT(0x10C), // 从地图对象掉落物品`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_ITEM_FROM_MAP(0x10D), // 从地图移除物品`：删除对象、关系或临时状态。
  - `CANNOT_SPAWN_KITE(0x10E), // 无法生成风筝`：进行条件判定并返回布尔结果。
  - `SPAWN_KITE(0x10F), // 生成风筝`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_KITE(0x110), // 移除风筝`：删除对象、关系或临时状态。
  - `SPAWN_MIST(0x111), // 生成迷雾`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_MIST(0x112), // 移除迷雾`：删除对象、关系或临时状态。
  - `SPAWN_DOOR(0x113), // 生成门`：通用业务逻辑入口，需结合实现查看细节。
  - `REMOVE_DOOR(0x114), // 移除门`：删除对象、关系或临时状态。
  - `REACTOR_HIT(0x115), // 反应堆被击中`：通用业务逻辑入口，需结合实现查看细节。
  - `REACTOR_SPAWN(0x117), // 生成反应堆`：通用业务逻辑入口，需结合实现查看细节。
  - `REACTOR_DESTROY(0x118), // 销毁反应堆`：通用业务逻辑入口，需结合实现查看细节。
  - `SNOWBALL_STATE(0x119), // 雪球状态`：通用业务逻辑入口，需结合实现查看细节。
  - `HIT_SNOWBALL(0x11A), // 击中雪球`：通用业务逻辑入口，需结合实现查看细节。
  - `SNOWBALL_MESSAGE(0x11B), // 雪球消息`：通用业务逻辑入口，需结合实现查看细节。
  - `LEFT_KNOCK_BACK(0x11C), // 左侧击退`：通用业务逻辑入口，需结合实现查看细节。
  - `COCONUT_HIT(0x11D), // 击中椰子`：通用业务逻辑入口，需结合实现查看细节。
  - `COCONUT_SCORE(0x11E), // 椰子得分`：通用业务逻辑入口，需结合实现查看细节。
  - `GUILD_BOSS_HEALER_MOVE(0x11F), // 公会长老移动`：通用业务逻辑入口，需结合实现查看细节。
  - `GUILD_BOSS_PULLEY_STATE_CHANGE(0x120), // 公会长老滑轮状态改变`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_START(0x121), // 怪物嘉年华开始`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_OBTAINED_CP(0x122), // 获得怪物嘉年华CP`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_PARTY_CP(0x123), // 怪物嘉年华队伍CP`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_SUMMON(0x124), // 怪物嘉年华召唤`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_MESSAGE(0x125), // 怪物嘉年华消息`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_DIED(0x126), // 怪物嘉年华死亡`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_CARNIVAL_LEAVE(0x127), // 离开怪物嘉年华`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT_ARENA_USER_SCORE(0x129), // ARIANT竞技场用户得分`：通用业务逻辑入口，需结合实现查看细节。
  - `SHEEP_RANCH_INFO(0x12B), // 羊牧场信息`：通用业务逻辑入口，需结合实现查看细节。
  - `SHEEP_RANCH_CLOTHES(0x12C), // 羊牧场服装`：通用业务逻辑入口，需结合实现查看细节。
  - `WITCH_TOWER_SCORE_UPDATE(0x12D),    // thanks lrenex // 巫师塔得分更新`：通用业务逻辑入口，需结合实现查看细节。
  - `HORNTAIL_CAVE(0x12E), // 角龙头洞`：通用业务逻辑入口，需结合实现查看细节。
  - `ZAKUM_SHRINE(0x12F), // 泽库姆神殿`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC_TALK(0x130), // NPC对话`：通用业务逻辑入口，需结合实现查看细节。
  - `OPEN_NPC_SHOP(0x131), // 打开NPC商店`：通用业务逻辑入口，需结合实现查看细节。
  - `CONFIRM_SHOP_TRANSACTION(0x132), // 确认商店交易`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_SHOP_MESSAGE(0x133),//lame :P // 管理员商店消息`：通用业务逻辑入口，需结合实现查看细节。
  - `ADMIN_SHOP(0x134), // 管理员商店`：通用业务逻辑入口，需结合实现查看细节。
  - `STORAGE(0x135), // 仓库`：通用业务逻辑入口，需结合实现查看细节。
  - `FREDRICK_MESSAGE(0x136), // Fredrick消息`：通用业务逻辑入口，需结合实现查看细节。
  - `FREDRICK(0x137), // Fredrick操作`：通用业务逻辑入口，需结合实现查看细节。
  - `RPS_GAME(0x138), // 石头剪刀布游戏`：通用业务逻辑入口，需结合实现查看细节。
  - `MESSENGER(0x139), // 消息传递`：通用业务逻辑入口，需结合实现查看细节。
  - `PLAYER_INTERACTION(0x13A), // 玩家互动`：通用业务逻辑入口，需结合实现查看细节。
  - `TOURNAMENT(0x13B), // 锦标赛`：通用业务逻辑入口，需结合实现查看细节。
  - `TOURNAMENT_MATCH_TABLE(0x13C), // 锦标赛匹配表`：通用业务逻辑入口，需结合实现查看细节。
  - `TOURNAMENT_SET_PRIZE(0x13D), // 设置锦标赛奖品`：通用业务逻辑入口，需结合实现查看细节。
  - `TOURNAMENT_UEW(0x13E), // 锦标赛未知功能`：通用业务逻辑入口，需结合实现查看细节。
  - `TOURNAMENT_CHARACTERS(0x13F),//they never coded this :| // 锦标赛角色（他们从未实现这个功能）`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_PROGRESS(0x140),//byte step, int groomid, int brideid // 结婚进度`：通用业务逻辑入口，需结合实现查看细节。
  - `WEDDING_CEREMONY_END(0x141), // 结婚仪式结束`：通用业务逻辑入口，需结合实现查看细节。
  - `PARCEL(0x142), // 礼包`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARGE_PARAM_RESULT(0x143), // 充值参数结果`：通用业务逻辑入口，需结合实现查看细节。
  - `QUERY_CASH_RESULT(0x144), // 查询现金结果`：查询并返回匹配集合或单项结果。
  - `CASHSHOP_OPERATION(0x145), // 现金商店操作`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_PURCHASE_EXP_CHANGED(0x146),   // found thanks to Arnah (Vertisy) // 现金商店购买经验变化`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_GIFT_INFO_RESULT(0x147), // 现金商店礼物信息结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_CHECK_NAME_CHANGE(0x148), // 检查现金商店姓名更改`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_CHECK_NAME_CHANGE_POSSIBLE_RESULT(0x149), // 检查现金商店姓名更改可能性结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_REGISTER_NEW_CHARACTER_RESULT(0x14A), // 注册新角色结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_CHECK_TRANSFER_WORLD_POSSIBLE_RESULT(0x14B), // 检查转移世界可能性结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_GACHAPON_STAMP_RESULT(0x14C), // 现金商店扭蛋印章结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_CASH_ITEM_GACHAPON_RESULT(0x14D), // 现金商店现金物品扭蛋结果`：通用业务逻辑入口，需结合实现查看细节。
  - `CASHSHOP_CASH_GACHAPON_OPEN_RESULT(0x14E), // 现金商店现金扭蛋打开结果`：通用业务逻辑入口，需结合实现查看细节。
  - `KEYMAP(0x14F), // 键盘映射`：通用业务逻辑入口，需结合实现查看细节。
  - `AUTO_HP_POT(0x150), // 自动使用HP药水`：通用业务逻辑入口，需结合实现查看细节。
  - `AUTO_MP_POT(0x151), // 自动使用MP药水`：通用业务逻辑入口，需结合实现查看细节。
  - `SEND_TV(0x155), // 发送电视`：向外发送响应、消息或网络包。
  - `REMOVE_TV(0x156), // 移除电视`：删除对象、关系或临时状态。
  - `ENABLE_TV(0x157), // 启用电视`：通用业务逻辑入口，需结合实现查看细节。
  - `MTS_OPERATION2(0x15B), // MTS操作2`：通用业务逻辑入口，需结合实现查看细节。
  - `MTS_OPERATION(0x15C), // MTS操作`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLELIFE_RESULT(0x15D), // MapleLife结果`：通用业务逻辑入口，需结合实现查看细节。
  - `MAPLELIFE_ERROR(0x15E), // MapleLife错误`：通用业务逻辑入口，需结合实现查看细节。
  - `VICIOUS_HAMMER(0x162), // 恶毒锤子`：通用业务逻辑入口，需结合实现查看细节。
  - `VEGA_SCROLL(0x166), // VEGA卷轴`：通用业务逻辑入口，需结合实现查看细节。
  - `UPDATE_HPMPAALERT(0x1000), // 更新HP/MP/EXP警报`：更新已有对象/配置/缓存。
  - `SendOpcode(int code)`：向外发送响应、消息或网络包。
  - `public int getValue()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。

## `net/packet/ByteBufInPacket.java`

- `class ByteBufInPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ByteBufInPacket(ByteBuf byteBuf)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte[] getBytes()`：读取并返回状态/数据。
  - `public byte readByte()`：通用业务逻辑入口，需结合实现查看细节。
  - `public short readUnsignedByte()`：通用业务逻辑入口，需结合实现查看细节。
  - `public short readShort()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int readInt()`：通用业务逻辑入口，需结合实现查看细节。
  - `public long readLong()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point readPos()`：通用业务逻辑入口，需结合实现查看细节。
  - `public String readString()`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte[] readBytes(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void skip(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int available()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void seek(int byteOffset)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getPosition()`：读取并返回状态/数据。
  - `public boolean equals(Object o)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String insertReaderPosition(String hexDump, int index)`：通用业务逻辑入口，需结合实现查看细节。

## `net/packet/ByteBufOutPacket.java`

- `class ByteBufOutPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ByteBufOutPacket()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ByteBufOutPacket(Opcode op)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ByteBufOutPacket(SendOpcode op, int initialCapacity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte[] getBytes()`：读取并返回状态/数据。
  - `public void writeByte(byte value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeByte(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeBytes(byte[] value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeShort(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeInt(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeLong(long value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeBool(boolean value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeString(String value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeFixedString(String value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writeFixedString(String value, int fixed)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void writePos(Point value)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void skip(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean equals(Object o)`：通用业务逻辑入口，需结合实现查看细节。

## `net/packet/InPacket.java`

- `interface InPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `byte readByte()`：通用业务逻辑入口，需结合实现查看细节。
  - `short readUnsignedByte()`：通用业务逻辑入口，需结合实现查看细节。
  - `short readShort()`：通用业务逻辑入口，需结合实现查看细节。
  - `int readInt()`：通用业务逻辑入口，需结合实现查看细节。
  - `long readLong()`：通用业务逻辑入口，需结合实现查看细节。
  - `Point readPos()`：通用业务逻辑入口，需结合实现查看细节。
  - `String readString()`：通用业务逻辑入口，需结合实现查看细节。
  - `byte[] readBytes(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `void skip(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `int available()`：通用业务逻辑入口，需结合实现查看细节。
  - `void seek(int byteOffset)`：通用业务逻辑入口，需结合实现查看细节。
  - `int getPosition()`：读取并返回状态/数据。

## `net/packet/OutPacket.java`

- `interface OutPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `void writeByte(byte value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeByte(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeBytes(byte[] value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeShort(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeInt(int value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeLong(long value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeBool(boolean value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeString(String value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeFixedString(String value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writeFixedString(String value, int fixed)`：通用业务逻辑入口，需结合实现查看细节。
  - `void writePos(Point value)`：通用业务逻辑入口，需结合实现查看细节。
  - `void skip(int numberOfBytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `static OutPacket create(Opcode opcode)`：创建对象、会话或业务记录。

## `net/packet/Packet.java`

- `interface Packet`：领域类型或功能模块，职责由同名文件实现定义。
  - `byte[] getBytes()`：读取并返回状态/数据。

## `net/packet/logging/InPacketLogger.java`

- `class InPacketLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void channelRead(ChannelHandlerContext ctx, Object msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void log(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String getRecvOpcodeName(short opcode)`：读取并返回状态/数据。

## `net/packet/logging/LoggingUtil.java`

- `class LoggingUtil`：工具类，封装无状态通用能力。
  - `public static short readFirstShort(byte[] bytes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isIgnoredRecvPacket(short opcode)`：进行条件判定并返回布尔结果。

## `net/packet/logging/MonitoredChrLogger.java`

- `class MonitoredChrLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean toggleMonitored(int chrId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Collection<Integer> getMonitoredChrIds()`：读取并返回状态/数据。
  - `public static void logPacketIfMonitored(Client c, short packetId, byte[] packetContent)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isRecvBlocked(RecvOpcode op)`：进行条件判定并返回布尔结果。
  - `private static RecvOpcode getOpcodeFromValue(int value)`：读取并返回状态/数据。

## `net/packet/logging/OutPacketLogger.java`

- `class OutPacketLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void log(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private String getSendOpcodeName(short opcode)`：读取并返回状态/数据。

## `net/packet/logging/PacketLogger.java`

- `interface PacketLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `void log(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。

## `net/packet/out/SendNoteSuccessPacket.java`

- `class SendNoteSuccessPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SendNoteSuccessPacket()`：向外发送响应、消息或网络包。

## `net/packet/out/ShowNotesPacket.java`

- `class ShowNotesPacket`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ShowNotesPacket(List<NotesDO> notes)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void writeNote(NotesDO note)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/PlayerBuffStorage.java`

- `class PlayerBuffStorage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void addBuffsToStorage(int chrid, List<PlayerBuffValueHolder> toStore)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PlayerBuffValueHolder> getBuffsFromStorage(int chrid)`：读取并返回状态/数据。
  - `public void addDiseasesToStorage(int chrid, Map<Disease, Pair<Long, MobSkill>> toStore)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/PlayerBuffValueHolder.java`

- `class PlayerBuffValueHolder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerBuffValueHolder(int usedTime, StatEffect effect)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/PlayerCoolDownValueHolder.java`

- `class PlayerCoolDownValueHolder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerCoolDownValueHolder(int skillId, long startTime, long length)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/PlayerDiseaseValueHolder.java`

- `class PlayerDiseaseValueHolder`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerDiseaseValueHolder(final Disease disease, final long startTime, final long length)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/PlayerStorage.java`

- `class PlayerStorage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerStorage()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character removePlayer(int chr)`：删除对象、关系或临时状态。
  - `public Character getCharacterByName(String name)`：读取并返回状态/数据。
  - `public Character getCharacterById(int id)`：读取并返回状态/数据。
  - `public Collection<Character> getAllCharacters()`：读取并返回状态/数据。
  - `public final void disconnectAll()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getSize()`：读取并返回状态/数据。

## `net/server/Server.java`

- `class Server`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Server getInstance()`：读取并返回状态/数据。
  - `private Server()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCurrentTimestamp()`：读取并返回状态/数据。
  - `public long getCurrentTime()`：读取并返回状态/数据。
  - `public void updateCurrentTime()`：更新已有对象/配置/缓存。
  - `public long forceUpdateCurrentTime()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setNewYearCard(NewYearCardRecord nyc)`：写入或更新状态字段。
  - `public NewYearCardRecord getNewYearCard(int cardid)`：读取并返回状态/数据。
  - `public NewYearCardRecord removeNewYearCard(int cardid)`：删除对象、关系或临时状态。
  - `public void setAvailableDeveloperRoom()`：写入或更新状态字段。
  - `public boolean canEnterDeveloperRoom()`：进行条件判定并返回布尔结果。
  - `private void loadPlayerNpcMapStepFromDb()`：从外部来源加载数据（数据库/文件/配置）。
  - `public World getWorld(int id)`：读取并返回状态/数据。
  - `public List<World> getWorlds()`：读取并返回状态/数据。
  - `public int getWorldsSize()`：读取并返回状态/数据。
  - `public Channel getChannel(int world, int channel)`：读取并返回状态/数据。
  - `public List<Channel> getChannelsFromWorld(int world)`：读取并返回状态/数据。
  - `public List<Channel> getAllChannels()`：读取并返回状态/数据。
  - `public Set<Integer> getOpenChannels(int world)`：读取并返回状态/数据。
  - `private String getIP(int world, int channel)`：读取并返回状态/数据。
  - `public String[] getInetSocket(Client client, int world, int channel)`：读取并返回状态/数据。
  - `public int addChannel(int worldid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int addWorld()`：通用业务逻辑入口，需结合实现查看细节。
  - `private int initWorld()`：初始化模块、资源或运行时状态。
  - `public boolean removeChannel(int worldid)`：删除对象、关系或临时状态。
  - `public boolean removeWorld()`：删除对象、关系或临时状态。
  - `private void resetServerWorlds()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static long getTimeLeftForNextHour()`：读取并返回状态/数据。
  - `public static long getTimeLeftForNextDay()`：读取并返回状态/数据。
  - `public List<Integer> getActiveCoupons()`：读取并返回状态/数据。
  - `public void commitActiveCoupons()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void toggleCoupon(Integer couponId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateActiveCoupons()`：更新已有对象/配置/缓存。
  - `public void runAnnouncePlayerDiseasesSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerAnnouncePlayerDiseases(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reloadWorldsPlayerRanking()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void init()`：初始化模块、资源或运行时状态。
  - `private void registerChannelDependencies()`：通用业务逻辑入口，需结合实现查看细节。
  - `private LoginServer initLoginServer(int port)`：初始化模块、资源或运行时状态。
  - `private void initializeTimelyTasks()`：初始化模块、资源或运行时状态。
  - `public Alliance getAlliance(int id)`：读取并返回状态/数据。
  - `public void addAlliance(int id, Alliance alliance)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disbandAlliance(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void allianceMessage(int id, Packet packet, int exception, int guildex)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean addGuildtoAlliance(int aId, int guildId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean removeGuildFromAlliance(int aId, int guildId)`：删除对象、关系或临时状态。
  - `public boolean setAllianceRanks(int aId, String[] ranks)`：写入或更新状态字段。
  - `public boolean setAllianceNotice(int aId, String notice)`：写入或更新状态字段。
  - `public boolean increaseAllianceCapacity(int aId, int inc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int createGuild(int leaderId, String name)`：创建对象、会话或业务记录。
  - `public Guild getGuildByName(String name)`：读取并返回状态/数据。
  - `public Guild getGuild(int id)`：读取并返回状态/数据。
  - `public Guild getGuild(int id, int world)`：读取并返回状态/数据。
  - `public Guild getGuild(int id, int world, Character mc)`：读取并返回状态/数据。
  - `public void setGuildMemberOnline(Character mc, boolean bOnline, int channel)`：写入或更新状态字段。
  - `public int addGuildMember(GuildCharacter mgc, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean setGuildAllianceId(int gId, int aId)`：写入或更新状态字段。
  - `public void resetAllianceGuildPlayersRank(int gId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void leaveGuild(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guildChat(int gid, String name, int cid, String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeRank(int gid, int cid, int newRank)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void expelMember(GuildCharacter initiator, String name, int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setGuildNotice(int gid, String notice)`：写入或更新状态字段。
  - `public void memberLevelJobUpdate(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeRankTitle(int gid, String[] ranks)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setGuildEmblem(int gid, short bg, byte bgcolor, short logo, byte logocolor)`：写入或更新状态字段。
  - `public void disbandGuild(int gid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean increaseGuildCapacity(int gid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainGP(int gid, int amount)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guildMessage(int gid, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guildMessage(int gid, Packet packet, int exception)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PlayerBuffStorage getPlayerBuffStorage()`：读取并返回状态/数据。
  - `public void deleteGuildCharacter(Character mc)`：删除对象、关系或临时状态。
  - `public void deleteGuildCharacter(GuildCharacter mgc)`：删除对象、关系或临时状态。
  - `public void reloadGuildCharacters(int world)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(int world, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastGMMessage(int world, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isGmOnline(int world)`：进行条件判定并返回布尔结果。
  - `public void changeFly(Integer accountid, boolean canFly)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canFly(Integer accountid)`：进行条件判定并返回布尔结果。
  - `public int getCharacterWorld(Integer chrid)`：读取并返回状态/数据。
  - `public boolean haveCharacterEntry(Integer accountid, Integer chrid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getAccountCharacterCount(Integer accountid)`：读取并返回状态/数据。
  - `public short getAccountWorldCharacterCount(Integer accountid, Integer worldid)`：读取并返回状态/数据。
  - `private Set<Integer> getAccountCharacterEntries(Integer accountid)`：读取并返回状态/数据。
  - `public void updateCharacterEntry(Character chr)`：更新已有对象/配置/缓存。
  - `public void createCharacterEntry(Character chr)`：创建对象、会话或业务记录。
  - `public void deleteCharacterEntry(Integer accountid, Integer chrid)`：删除对象、关系或临时状态。
  - `public void transferWorldCharacterEntry(Character chr, Integer toWorld)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void loadAllAccountsCharactersView()`：从外部来源加载数据（数据库/文件/配置）。
  - `private boolean isFirstAccountLogin(Integer accId)`：进行条件判定并返回布尔结果。
  - `public void loadAccountCharacters(Client c)`：从外部来源加载数据（数据库/文件/配置）。
  - `private int loadAccountCharactersView(Integer accId, int gmLevel, int fromWorldid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void loadAccountStorages(Client c)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static String getRemoteHost(Client client)`：读取并返回状态/数据。
  - `public void setCharacteridInTransition(Client client, int charId)`：写入或更新状态字段。
  - `public boolean validateCharacteridInTransition(Client client, int charId)`：校验输入参数或业务约束。
  - `public Integer freeCharacteridInTransition(Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasCharacteridInTransition(Client client)`：进行条件判定并返回布尔结果。
  - `public void registerLoginState(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unregisterLoginState(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void disconnectIdlesOnLoginState()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void disconnectIdlesOnLoginTask()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Runnable shutdown(final boolean restart)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void shutdownInternal(boolean restart)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isNextTime()`：进行条件判定并返回布尔结果。
  - `public synchronized void shutdownWithMsgAndInternal(ServerShutdownDTO serverShutdownDTO)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/Channel.java`

- `class Channel`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Channel(final int world, final int channel, long startTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `private ChannelServer initServer(int port, int world, int channel)`：初始化模块、资源或运行时状态。
  - `public synchronized void reloadEventScriptManager()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void shutdown()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void closeChannelServices()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void closeChannelSchedules()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void closeAllMerchants()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapManager getMapFactory()`：读取并返回状态/数据。
  - `public BaseService getServiceAccess(ChannelServices sv)`：读取并返回状态/数据。
  - `public int getWorld()`：读取并返回状态/数据。
  - `public World getWorldServer()`：读取并返回状态/数据。
  - `public void addPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getServerMessage()`：读取并返回状态/数据。
  - `public PlayerStorage getPlayerStorage()`：读取并返回状态/数据。
  - `public boolean removePlayer(Character chr)`：删除对象、关系或临时状态。
  - `public int getChannelCapacity()`：读取并返回状态/数据。
  - `public void broadcastPacket(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int getId()`：读取并返回状态/数据。
  - `public String getIP()`：读取并返回状态/数据。
  - `public Event getEvent()`：读取并返回状态/数据。
  - `public void setEvent(Event event)`：写入或更新状态字段。
  - `public EventScriptManager getEventSM()`：读取并返回状态/数据。
  - `public void broadcastGMPacket(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Character> getPartyMembers(Party party)`：读取并返回状态/数据。
  - `public void insertPlayerAway(int chrId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePlayerAway(int chrId)`：删除对象、关系或临时状态。
  - `public boolean canUninstall()`：进行条件判定并返回布尔结果。
  - `private void disconnectAwayPlayers()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addHiredMerchant(int chrid, HiredMerchant hm)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeHiredMerchant(int chrid)`：删除对象、关系或临时状态。
  - `public int[] multiBuddyFind(int charIdFrom, int[] characterIds)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean addExpedition(Expedition exped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeExpedition(Expedition exped)`：删除对象、关系或临时状态。
  - `public Expedition getExpedition(ExpeditionType type)`：读取并返回状态/数据。
  - `public List<Expedition> getExpeditions()`：读取并返回状态/数据。
  - `public boolean isConnected(String name)`：进行条件判定并返回布尔结果。
  - `public boolean isActive()`：进行条件判定并返回布尔结果。
  - `public boolean finishedShutdown()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setServerMessage(String message)`：写入或更新状态字段。
  - `private static String[] getEvents()`：读取并返回状态/数据。
  - `public int getStoredVar(int key)`：读取并返回状态/数据。
  - `public void setStoredVar(int key, int val)`：写入或更新状态字段。
  - `public int lookupPartyDojo(Party party)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int ingressDojo(boolean isPartyDojo, int fromStage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int ingressDojo(boolean isPartyDojo, Party party, int fromStage)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void freeDojoSlot(int slot, Party party)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getDojoSlot(int dojoMapId)`：读取并返回状态/数据。
  - `public void resetDojoMap(int fromMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetDojo(int dojoMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void resetDojo(int dojoMapId, int thisStg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void freeDojoSectionIfEmpty(int dojoMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void startDojoSchedule(final int dojoMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dismissDojoSchedule(int dojoMapId, Party party)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean setDojoProgress(int dojoMapId)`：写入或更新状态字段。
  - `public long getDojoFinishTime(int dojoMapId)`：读取并返回状态/数据。
  - `public boolean addMiniDungeon(int dungeonid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MiniDungeon getMiniDungeon(int dungeonid)`：读取并返回状态/数据。
  - `public void removeMiniDungeon(int dungeonid)`：删除对象、关系或临时状态。
  - `public boolean isWeddingReserved(Integer weddingId)`：进行条件判定并返回布尔结果。
  - `public int getWeddingReservationStatus(Integer weddingId, boolean cathedral)`：读取并返回状态/数据。
  - `public int pushWeddingReservation(Integer weddingId, boolean cathedral, boolean premium, Integer groomId, Integer brideId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isOngoingWeddingGuest(boolean cathedral, int playerId)`：进行条件判定并返回布尔结果。
  - `public Integer getOngoingWedding(boolean cathedral)`：读取并返回状态/数据。
  - `public boolean getOngoingWeddingType(boolean cathedral)`：读取并返回状态/数据。
  - `public void closeOngoingWedding(boolean cathedral)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setOngoingWedding(final boolean cathedral, Boolean premium, Integer weddingId, Set<Integer> guests)`：写入或更新状态字段。
  - `public synchronized boolean acceptOngoingWedding(final boolean cathedral)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getTimeLeft(long futureTime)`：读取并返回状态/数据。
  - `public long getWeddingTicketExpireTime(int resSlot)`：读取并返回状态/数据。
  - `public static long getRelativeWeddingTicketExpireTime(int resSlot)`：读取并返回状态/数据。
  - `public String getWeddingReservationTimeLeft(Integer weddingId)`：读取并返回状态/数据。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerOwnedMap(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unregisterOwnedMap(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void runCheckOwnedMapsSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getMonsterCarnivalRoom(boolean cpq1, int field)`：读取并返回状态/数据。
  - `public void initMonsterCarnival(boolean cpq1, int field)`：初始化模块、资源或运行时状态。
  - `public void finishMonsterCarnival(boolean cpq1, int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canInitMonsterCarnival(boolean cpq1, int field)`：进行条件判定并返回布尔结果。
  - `public void debugMarriageStatus()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/CharacterIdChannelPair.java`

- `class CharacterIdChannelPair`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CharacterIdChannelPair()`：通用业务逻辑入口，需结合实现查看细节。
  - `public CharacterIdChannelPair(int charid, int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCharacterId()`：读取并返回状态/数据。
  - `public int getChannel()`：读取并返回状态/数据。

## `net/server/channel/handlers/AbstractDealDamageHandler.java`

- `class AbstractDealDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `protected void applyAttack(AttackInfo attack, final Character player, int attackCount)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void damageMonsterWithSkill(final Character attacker, final MapleMap map, final Monster monster, final int damage, int skillid, int fixedTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected AttackInfo parseDamage(InPacket p, Character chr, boolean ranged, boolean magic)`：解析输入文本或二进制内容。
  - `private static boolean isWithinAttackBox(Character player, Monster monster, StatEffect attackEffect, AttackInfo attack, Point alternatePlayerPos, Point secondaryAlternatePlayerPos)`：进行条件判定并返回布尔结果。
  - `private static boolean isWithinAttackBox(Point playerPos, Rectangle monsterBounds, Point monsterPos, StatEffect attackEffect, boolean facingLeft)`：进行条件判定并返回布尔结果。
  - `private static boolean intersectsAnyAttackBox(Rectangle monsterBounds, Point monsterPos, StatEffect attackEffect, boolean facingLeft, Point... playerPositions)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isFacingLeftByDirection(int direction)`：进行条件判定并返回布尔结果。
  - `private static boolean isFacingLeftByStance(int stance)`：进行条件判定并返回布尔结果。
  - `private static Rectangle getMonsterBounds(Monster monster)`：读取并返回状态/数据。
  - `private static boolean isFullScreenDistanceExempt(int skillId)`：进行条件判定并返回布尔结果。
  - `private static boolean shouldSkipDistanceHackCheck(int skillId, StatEffect attackEffect)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isNonSpatialAttackSkill(int skillId, StatEffect attackEffect)`：进行条件判定并返回布尔结果。
  - `private static boolean hasReliableDistanceGeometry(StatEffect attackEffect, boolean useBbox)`：进行条件判定并返回布尔结果。
  - `private static boolean hasSkillAttackBox(StatEffect attackEffect)`：进行条件判定并返回布尔结果。
  - `private static DistanceCheckSample chooseBestDistanceCheckSample(Point currentPlayerPos, Monster monster, boolean useBbox, Point teleportBeforePos, Point movementBeforePos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static DistanceCheckSample chooseCloserDistanceSample(DistanceCheckSample currentBest, Point candidatePos, Monster monster, boolean useBbox, Point currentPlayerPos, boolean usedTeleportContext, boolean usedMovementContext)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean shouldUseBoundingBox(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static double calculateDistanceSq(Point playerPos, Monster monster, boolean useBbox)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String buildBboxInfo(Character player, Monster monster, boolean useBbox, Point checkPos, Point teleportBeforePos, Point movementBeforePos, boolean usedTeleportContext, boolean usedMovementContext)`：构建输出对象、包体或配置。
  - `private static int[] getWorldBbox(Monster monster, MonsterStats stats)`：读取并返回状态/数据。
  - `private static void detectionAttackInterval(Character chr, AttackInfo ret)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int rand(int l, int u)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/AbstractMovementPacketHandler.java`

- `class AbstractMovementPacketHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `protected List<LifeMovementFragment> parseMovement(InPacket p) throws EmptyMovementException`：解析输入文本或二进制内容。

## `net/server/channel/handlers/AcceptFamilyHandler.java`

- `class AcceptFamilyHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void insertNewFamilyRecord(int characterID, int familyID, int seniorID, boolean updateChar)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/AdminChatHandler.java`

- `class AdminChatHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/AdminCommandHandler.java`

- `class AdminCommandHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/AdminLogHandler.java`

- `class AdminLogHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/AllianceOperationHandler.java`

- `class AllianceOperationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void changeLeaderAllianceRank(Alliance alliance, Character newLeader)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void changePlayerAllianceRank(Alliance alliance, Character chr, boolean raise)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/AranComboHandler.java`

- `class AranComboHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/AutoAggroHandler.java`

- `class AutoAggroHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/AutoAssignHandler.java`

- `class AutoAssignHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/BBSOperationHandler.java`

- `class BBSOperationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private String correctLength(String in, int maxSize)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void listBBSThreads(Client c, int start)`：查询并返回匹配集合或单项结果。
  - `private static void newBBSReply(Client c, int localthreadid, String text)`：创建对象、会话或业务记录。
  - `private static void editBBSThread(Client client, String title, String text, int icon, int localthreadid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void newBBSThread(Client client, String title, String text, int icon, boolean bNotice)`：创建对象、会话或业务记录。
  - `public static void deleteBBSThread(Client client, int localthreadid)`：删除对象、关系或临时状态。
  - `public static void deleteBBSReply(Client client, int replyid)`：删除对象、关系或临时状态。
  - `public static void displayThread(Client client, int threadid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void displayThread(Client client, int threadid, boolean bIsThreadIdLocal)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/BeholderHandler.java`

- `class BeholderHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/BuddylistModifyHandler.java`

- `class BuddylistModifyHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private void nextPendingRequest(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private CharacterIdNameBuddyCapacity getCharacterIdAndNameFromDatabase(String name) throws SQLException`：读取并返回状态/数据。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void notifyRemoteChannel(Client c, int remoteChannel, int otherCid, BuddyOperation operation)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/CancelBuffHandler.java`

- `class CancelBuffHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CancelChairHandler.java`

- `class CancelChairHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CancelDebuffHandler.java`

- `class CancelDebuffHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CancelItemEffectHandler.java`

- `class CancelItemEffectHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CashOperationHandler.java`

- `class CashOperationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public CashOperationHandler(NoteService noteService)`：处理事件/请求/消息分发。
  - `private static boolean ensureCashInventoryCapacity(Client c, CashShop cs, int itemsToAdd)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `public static boolean checkBirthday(Client c, int idate)`：校验输入参数或业务约束。
  - `private static boolean canBuy(Character chr, ModifiedCashItemDO item, int cash)`：进行条件判定并返回布尔结果。

## `net/server/channel/handlers/CashShopSurpriseHandler.java`

- `class CashShopSurpriseHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ChangeChannelHandler.java`

- `class ChangeChannelHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ChangeMapHandler.java`

- `class ChangeMapHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void enterFromCashShop(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getFormattedMapListLogMessage(List<Integer> MapIds,Client c)`：读取并返回状态/数据。

## `net/server/channel/handlers/ChangeMapSpecialHandler.java`

- `class ChangeMapSpecialHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CharInfoRequestHandler.java`

- `class CharInfoRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ClickGuideHandler.java`

- `class ClickGuideHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CloseChalkboardHandler.java`

- `class CloseChalkboardHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CloseRangeDamageHandler.java`

- `class CloseRangeDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CoconutHandler.java`

- `class CoconutHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/CouponCodeHandler.java`

- `class CouponCodeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseCouponResult(int res)`：解析输入文本或二进制内容。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DamageSummonHandler.java`

- `class DamageSummonHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DenyAllianceRequestHandler.java`

- `class DenyAllianceRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DenyGuildRequestHandler.java`

- `class DenyGuildRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DenyPartyRequestHandler.java`

- `class DenyPartyRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DistributeAPHandler.java`

- `class DistributeAPHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DistributeSPHandler.java`

- `class DistributeSPHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DoorHandler.java`

- `class DoorHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/DueyHandler.java`

- `class DueyHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/EnterCashShopHandler.java`

- `class EnterCashShopHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/EnterMTSHandler.java`

- `class EnterMTSHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private List<MTSItemInfo> getNotYetSold(int cid)`：读取并返回状态/数据。
  - `private List<MTSItemInfo> getTransfer(int cid)`：读取并返回状态/数据。
  - `private void openCenterScript(Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/FaceExpressionHandler.java`

- `class FaceExpressionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/FamilyAddHandler.java`

- `class FamilyAddHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/FamilyPreceptsHandler.java`

- `class FamilyPreceptsHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/FamilySeparateHandler.java`

- `class FamilySeparateHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static int separateRepCost(FamilyEntry junior)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/FamilySummonResponseHandler.java`

- `class FamilySummonResponseHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/FamilyUseHandler.java`

- `class FamilyUseHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private boolean useEntitlement(FamilyEntry entry, FamilyEntitlement entitlement)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applyPartyBuff(Client c, int type, int effect, int duration, FamilyEntitlement entitlement)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applySelfBuff(Client c, int type, int effect, int duration, float rate, FamilyEntitlement entitlement)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/FieldDamageMobHandler.java`

- `class FieldDamageMobHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/FredrickHandler.java`

- `class FredrickHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public FredrickHandler(FredrickProcessor fredrickProcessor)`：处理事件/请求/消息分发。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/GeneralChatHandler.java`

- `class GeneralChatHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/GiveFameHandler.java`

- `class GiveFameHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/GrenadeEffectHandler.java`

- `class GrenadeEffectHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/GuildOperationHandler.java`

- `class GuildOperationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private boolean isGuildNameAcceptable(String name)`：进行条件判定并返回布尔结果。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/HealOvertimeHandler.java`

- `class HealOvertimeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/HiredMerchantRequest.java`

- `class HiredMerchantRequest`：领域类型或功能模块，职责由同名文件实现定义。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/InnerPortalHandler.java`

- `class InnerPortalHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static boolean isPlayerReady(Character player)`：进行条件判定并返回布尔结果。
  - `private static String readPortalNameSafely(InPacket p)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Portal resolveValidSourcePortal(Character player, String portalName)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isPlayerNearPortal(Point playerPos, Portal portal)`：进行条件判定并返回布尔结果。
  - `private static boolean isSameMapInnerTeleport(Character player, Portal sourcePortal)`：进行条件判定并返回布尔结果。
  - `private static Portal resolveValidTargetPortal(Character player, Portal sourcePortal)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void movePlayerInMap(Character player, Point afterPos)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/InventoryMergeHandler.java`

- `class InventoryMergeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/InventorySortHandler.java`

- `class PairedQuicksort`：领域类型或功能模块，职责由同名文件实现定义。
- `class InventorySortHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private void PartitionByItemId(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int getWatkForProjectile(Item item)`：读取并返回状态/数据。
  - `private void PartitionByProjectileAtk(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByName(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByQuantity(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByLevel(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `void MapleQuicksort(int Esq, int Dir, ArrayList<Item> A, int sort)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getItemSubtype(Item it)`：读取并返回状态/数据。
  - `private int[] BinarySearchElement(ArrayList<Item> A, int rangeId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reverseSortSublist(ArrayList<Item> A, int[] range)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ItemMoveHandler.java`

- `class ItemMoveHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ItemPickupHandler.java`

- `class ItemPickupHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(final InPacket p, final Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ItemRewardHandler.java`

- `class ItemRewardHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/KeymapChangeHandler.java`

- `class KeymapChangeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/LeftKnockbackHandler.java`

- `class LeftKnockbackHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, final Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MTSHandler.java`

- `class MTSHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `public List<MTSItemInfo> getNotYetSold(int cid)`：读取并返回状态/数据。
  - `public Packet getCart(int cid)`：读取并返回状态/数据。
  - `public List<MTSItemInfo> getTransfer(int cid)`：读取并返回状态/数据。
  - `private static Packet getMTS(int tab, int type, int page)`：读取并返回状态/数据。
  - `public Packet getMTSSearch(int tab, int type, int cOi, String search, int page)`：读取并返回状态/数据。

## `net/server/channel/handlers/MagicDamageHandler.java`

- `class MagicDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MakerSkillHandler.java`

- `class MakerSkillHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MesoDropHandler.java`

- `class MesoDropHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MessengerHandler.java`

- `class MessengerHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MobBanishPlayerHandler.java`

- `class MobBanishPlayerHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MobDamageMobFriendlyHandler.java`

- `class MobDamageMobFriendlyHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MobDamageMobHandler.java`

- `class MobDamageMobHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static int calcMaxDamage(Monster attacker, Monster damaged, boolean magic)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int calcModifier(Monster monster, MonsterStatus buff, MonsterStatus nerf)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/MonsterBombHandler.java`

- `class MonsterBombHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MonsterBookCoverHandler.java`

- `class MonsterBookCoverHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MonsterCarnivalHandler.java`

- `class MonsterCarnivalHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private int rollHitChance(MobSkillType type)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/MoveDragonHandler.java`

- `class MoveDragonHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MoveLifeHandler.java`

- `class MoveLifeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static boolean inRangeInclusive(Byte pVal, Integer pMin, Integer pMax)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/MovePetHandler.java`

- `class MovePetHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MovePlayerHandler.java`

- `class MovePlayerHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MoveSummonHandler.java`

- `class MoveSummonHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/MultiChatHandler.java`

- `class MultiChatHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/NPCAnimationHandler.java`

- `class NPCAnimationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/NPCMoreTalkHandler.java`

- `class NPCMoreTalkHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void cmRouting(Client c, byte action, byte lastMsg, int selection)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/NPCShopHandler.java`

- `class NPCShopHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/NPCTalkHandler.java`

- `class NPCTalkHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/NewYearCardHandler.java`

- `class NewYearCardHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static int getReceiverId(String receiver, int world)`：读取并返回状态/数据。
  - `private static int getValidNewYearCardStatus(int itemid, Character player, short slot)`：读取并返回状态/数据。

## `net/server/channel/handlers/NoteActionHandler.java`

- `class NoteActionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public NoteActionHandler(NoteService noteService)`：处理事件/请求/消息分发。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/OpenFamilyHandler.java`

- `class OpenFamilyHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/OpenFamilyPedigreeHandler.java`

- `class OpenFamilyPedigreeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/OwlWarpHandler.java`

- `class OwlWarpHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PartyOperationHandler.java`

- `class PartyOperationHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PartySearchRegisterHandler.java`

- `class PartySearchRegisterHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PartySearchStartHandler.java`

- `class PartySearchStartHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PartySearchUpdateHandler.java`

- `class PartySearchUpdateHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetAutoPotHandler.java`

- `class PetAutoPotHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetChatHandler.java`

- `class PetChatHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetCommandHandler.java`

- `class PetCommandHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetExcludeItemsHandler.java`

- `class PetExcludeItemsHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetFoodHandler.java`

- `class PetFoodHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PetLootHandler.java`

- `class PetLootHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/PlayerInteractionHandler.java`

- `class PlayerInteractionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
- `enum Action`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static int establishMiniroomStatus(Character chr, boolean isMinigame)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static boolean isTradeOpen(Character chr)`：进行条件判定并返回布尔结果。
  - `private static boolean canPlaceStore(Character chr)`：进行条件判定并返回布尔结果。

## `net/server/channel/handlers/PlayerLoggedinHandler.java`

- `class PlayerLoggedinHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public PlayerLoggedinHandler(NoteService noteService)`：处理事件/请求/消息分发。
  - `private boolean tryAcquireAccount(int accId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void releaseAccount(int accId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean validateState(Client c)`：校验输入参数或业务约束。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void showDueyNotification(Client c, Character player)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/PlayerMapTransitionHandler.java`

- `class PlayerMapTransitionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/QuestActionHandler.java`

- `class QuestActionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static boolean isNpcNearby(InPacket p, Character player, Quest quest, int npcId)`：进行条件判定并返回布尔结果。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/QuickslotKeyMappedModifiedHandler.java`

- `class QuickslotKeyMappedModifiedHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RPSActionHandler.java`

- `class RPSActionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RaiseIncExpHandler.java`

- `class RaiseIncExpHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RaiseUIStateHandler.java`

- `class RaiseUIStateHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RangedAttackHandler.java`

- `class RangedAttackHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ReactorHitHandler.java`

- `class ReactorHitHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RemoteGachaponHandler.java`

- `class RemoteGachaponHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/RemoteStoreHandler.java`

- `class RemoteStoreHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static HiredMerchant getMerchant(Client c)`：读取并返回状态/数据。

## `net/server/channel/handlers/ReportHandler.java`

- `class ReportHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void addReport(int reporterid, int victimid, int reason, String description, String chatlog)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/RingActionHandler.java`

- `class RingActionHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public RingActionHandler(NoteService noteService)`：处理事件/请求/消息分发。
  - `private static int getEngagementBoxId(int useItemId)`：读取并返回状态/数据。
  - `public static void sendEngageProposal(final Client c, final String name, final int itemid)`：向外发送响应、消息或网络包。
  - `private static void eraseEngagementOffline(int characterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void eraseEngagementOffline(int characterId, Connection con) throws SQLException`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void breakEngagementOffline(int characterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized static void breakMarriage(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void resetRingId(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized static void breakEngagement(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void breakMarriageRing(Character chr, final int wItemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void giveMarriageRings(Character player, Character partner, int marriageRingId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ScriptedItemHandler.java`

- `class ScriptedItemHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/ScrollHandler.java`

- `class ScrollHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void announceCannotScroll(Client c, boolean legendarySpirit)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean canScroll(int scrollid, int itemid)`：进行条件判定并返回布尔结果。

## `net/server/channel/handlers/SetHpMpAlertHandler.java`

- `class SetHpMpAlertHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SkillBookHandler.java`

- `class SkillBookHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SkillEffectHandler.java`

- `class SkillEffectHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SkillMacroHandler.java`

- `class SkillMacroHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SnowballHandler.java`

- `class SnowballHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SpawnPetHandler.java`

- `class SpawnPetHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SpecialMoveHandler.java`

- `class SpecialMoveHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SpouseChatHandler.java`

- `class SpouseChatHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/StorageHandler.java`

- `class StorageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/SummonDamageHandler.java`

- `class SummonDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
- `class SummonAttackEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static int calcMaxDamage(StatEffect summonEffect, Character player, boolean magic)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/TakeDamageHandler.java`

- `class TakeDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TouchMonsterDamageHandler.java`

- `class TouchMonsterDamageHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TouchReactorHandler.java`

- `class TouchReactorHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TouchingCashShopHandler.java`

- `class TouchingCashShopHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TransferNameHandler.java`

- `class TransferNameHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TransferNameResultHandler.java`

- `class TransferNameResultHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TransferWorldHandler.java`

- `class TransferWorldHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/TrockAddMapHandler.java`

- `class TrockAddMapHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseCashItemHandler.java`

- `class UseCashItemHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public UseCashItemHandler(NoteService noteService)`：处理事件/请求/消息分发。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void remove(Client c, short position, int itemid)`：删除对象、关系或临时状态。
  - `private static boolean getIncubatedItem(Client c, int id)`：读取并返回状态/数据。
  - `private static void notEnabled(Character player)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/channel/handlers/UseCatchItemHandler.java`

- `class UseCatchItemHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseChairHandler.java`

- `class UseChairHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseDeathItemHandler.java`

- `class UseDeathItemHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseGachaExpHandler.java`

- `class UseGachaExpHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseHammerHandler.java`

- `class UseHammerHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseItemEffectHandler.java`

- `class UseItemEffectHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseItemHandler.java`

- `class UseItemHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void remove(Client c, short slot)`：删除对象、关系或临时状态。

## `net/server/channel/handlers/UseMapleLifeHandler.java`

- `class UseMapleLifeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseMountFoodHandler.java`

- `class UseMountFoodHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseOwlOfMinervaHandler.java`

- `class UseOwlOfMinervaHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseSolomonHandler.java`

- `class UseSolomonHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseSummonBagHandler.java`

- `class UseSummonBagHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseTreasureChestHandler.java`

- `class UseTreasureChestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/UseWaterOfLifeHandler.java`

- `class UseWaterOfLifeHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/WeddingHandler.java`

- `class WeddingHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/WeddingTalkHandler.java`

- `class WeddingTalkHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/WeddingTalkMoreHandler.java`

- `class WeddingTalkMoreHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/channel/handlers/WhisperHandler.java`

- `class WhisperHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private void handleFind(Character user, Character target, byte flag)`：处理事件/请求/消息分发。
  - `private void handleWhisper(String message, Character user, Character target)`：处理事件/请求/消息分发。

## `net/server/coordinator/login/LoginBypassCoordinator.java`

- `class LoginBypassCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static LoginBypassCoordinator getInstance()`：读取并返回状态/数据。
  - `public boolean canLoginBypass(Hwid hwid, int accId, boolean pic)`：进行条件判定并返回布尔结果。
  - `public void registerLoginBypassEntry(Hwid hwid, int accId, boolean pic)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unregisterLoginBypassEntry(Hwid hwid, int accId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void runUpdateLoginBypass()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/login/LoginStorage.java`

- `class LoginStorage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public boolean registerLogin(int accountId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearExpiredAttempts()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/matchchecker/AbstractMatchCheckerListener.java`

- `interface AbstractMatchCheckerListener`：领域类型或功能模块，职责由同名文件实现定义。
  - `void onMatchCreated(Character leader, Set<Character> nonLeaderMatchPlayers, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `void onMatchAccepted(int leaderid, Set<Character> matchPlayers, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `void onMatchDeclined(int leaderid, Set<Character> matchPlayers, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `void onMatchDismissed(int leaderid, Set<Character> matchPlayers, String message)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/matchchecker/MatchCheckerCoordinator.java`

- `class MatchCheckerCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
- `class MatchCheckingEntry`：领域类型或功能模块，职责由同名文件实现定义。
- `class MatchCheckingElement`：领域类型或功能模块，职责由同名文件实现定义。
  - `private void unpoolMatchPlayer(Integer cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unpoolMatchPlayers(Set<Integer> matchPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean poolMatchPlayer(Integer cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean poolMatchPlayers(Set<Integer> matchPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isMatchingAvailable(Set<Integer> matchPlayers)`：进行条件判定并返回布尔结果。
  - `private void reenablePlayerMatching(Set<Integer> matchPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMatchConfirmationLeaderid(int cid)`：读取并返回状态/数据。
  - `public MatchCheckerType getMatchConfirmationType(int cid)`：读取并返回状态/数据。
  - `public boolean isMatchConfirmationActive(int cid)`：进行条件判定并返回布尔结果。
  - `private MatchCheckingElement createMatchConfirmationInternal(MatchCheckerType matchType, int world, int leaderCid, AbstractMatchCheckerListener leaderListener, Set<Integer> players, String message)`：创建对象、会话或业务记录。
  - `public boolean createMatchConfirmation(MatchCheckerType matchType, int world, int leaderCid, Set<Integer> players, String message)`：创建对象、会话或业务记录。
  - `private void disposeMatchElement(MatchCheckingElement mmce)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean acceptMatchElement(MatchCheckingElement mmce, int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void denyMatchElement(MatchCheckingElement mmce, int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dismissMatchElement(MatchCheckingElement mmce, int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean answerMatchConfirmation(int cid, boolean accept)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean dismissMatchConfirmation(int cid)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/matchchecker/MatchCheckerListenerFactory.java`

- `class MatchCheckerListenerFactory`：领域类型或功能模块，职责由同名文件实现定义。
- `enum MatchCheckerType`：领域类型或功能模块，职责由同名文件实现定义。

## `net/server/coordinator/matchchecker/MatchCheckerListenerRecipe.java`

- `interface MatchCheckerListenerRecipe`：领域类型或功能模块，职责由同名文件实现定义。
  - `AbstractMatchCheckerListener getListener()`：读取并返回状态/数据。

## `net/server/coordinator/matchchecker/listener/MatchCheckerCPQChallenge.java`

- `class MatchCheckerCPQChallenge`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static AbstractMatchCheckerListener loadListener()`：从外部来源加载数据（数据库/文件/配置）。
  - `private static Character getChallenger(int leaderid, Set<Character> matchPlayers)`：读取并返回状态/数据。
  - `public AbstractMatchCheckerListener getListener()`：读取并返回状态/数据。

## `net/server/coordinator/matchchecker/listener/MatchCheckerGuildCreation.java`

- `class MatchCheckerGuildCreation`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static void broadcastGuildCreationDismiss(Set<Character> nonLeaderMatchPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static AbstractMatchCheckerListener loadListener()`：从外部来源加载数据（数据库/文件/配置）。
  - `public AbstractMatchCheckerListener getListener()`：读取并返回状态/数据。

## `net/server/coordinator/partysearch/PartySearchCharacter.java`

- `class PartySearchCharacter`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartySearchCharacter(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String toString()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character callPlayer(int leaderid, int callerMapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getPlayer()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public boolean isQueued()`：进行条件判定并返回布尔结果。

## `net/server/coordinator/partysearch/PartySearchCoordinator.java`

- `class PartySearchCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
- `class LeaderSearchMetadata`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartySearchCoordinator()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean isInVicinity(int callerMapid, int calleeMapid)`：进行条件判定并返回布尔结果。
  - `public void attachPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void detachPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updatePartySearchStorage()`：更新已有对象/配置/缓存。
  - `private static Job getPartySearchJob(Job job)`：读取并返回状态/数据。
  - `private Character fetchPlayer(int callerCid, int callerMapid, Job job, int minLevel, int maxLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addQueueLeader(Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeQueueLeader(Character leader)`：删除对象、关系或临时状态。
  - `public void registerPartyLeader(Character leader, int minLevel, int maxLevel, int jobs)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerPartyLeader(Character leader, LeaderSearchMetadata settings)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unregisterPartyLeader(Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Character searchPlayer(Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean sendPartyInviteFromSearch(Character chr, Character leader)`：向外发送响应、消息或网络包。
  - `private void registerLongTermPartyLeaders(List<Pair<Character, LeaderSearchMetadata>> recycledLeaders)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unregisterLongTermPartyLeader(Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void reinstateLongTermPartyLeaders()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void runPartySearch()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/partysearch/PartySearchEchelon.java`

- `class PartySearchEchelon`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartySearchEchelon()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Character> exportEchelon()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void attachPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean detachPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/partysearch/PartySearchStorage.java`

- `class PartySearchStorage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartySearchStorage()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PartySearchCharacter> getStorageList()`：读取并返回状态/数据。
  - `public void updateStorage(Collection<Character> echelon)`：更新已有对象/配置/缓存。
  - `private static int bsearchStorage(List<PartySearchCharacter> storage, int level)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character callPlayer(int callerCid, int callerMapid, int minLevel, int maxLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void detachPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/session/HostHwid.java`

  - `static HostHwid createWithDefaultExpiry(Hwid hwid)`：创建对象、会话或业务记录。
  - `private static Instant getDefaultExpiry()`：读取并返回状态/数据。

## `net/server/coordinator/session/HostHwidCache.java`

- `class HostHwidCache`：领域类型或功能模块，职责由同名文件实现定义。
  - `void clearExpired()`：通用业务逻辑入口，需结合实现查看细节。
  - `void addEntry(String remoteHost, Hwid hwid)`：通用业务逻辑入口，需结合实现查看细节。
  - `HostHwid getEntry(String remoteHost)`：读取并返回状态/数据。
  - `Hwid removeEntryAndGetItsHwid(String remoteHost)`：删除对象、关系或临时状态。
  - `Hwid getEntryHwid(String remoteHost)`：读取并返回状态/数据。

## `net/server/coordinator/session/Hwid.java`

  - `private static boolean isValidHostString(String hostString)`：进行条件判定并返回布尔结果。
  - `public static Hwid fromHostString(String hostString) throws IllegalArgumentException`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/session/HwidAssociationExpiry.java`

- `class HwidAssociationExpiry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Instant getHwidAccountExpiry(int relevance)`：读取并返回状态/数据。
  - `private static long hwidExpirationUpdate(int relevance)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getHwidExpirationDegree(int relevance)`：读取并返回状态/数据。

## `net/server/coordinator/session/HwidRelevance.java`

  - `public int getIncrementedRelevance()`：读取并返回状态/数据。

## `net/server/coordinator/session/InitializationResult.java`

- `enum InitializationResult`：领域类型或功能模块，职责由同名文件实现定义。
  - `SUCCESS(AntiMulticlientResult.SUCCESS),`：通用业务逻辑入口，需结合实现查看细节。
  - `ALREADY_INITIALIZED(AntiMulticlientResult.REMOTE_PROCESSING),`：通用业务逻辑入口，需结合实现查看细节。
  - `TIMED_OUT(AntiMulticlientResult.COORDINATOR_ERROR),`：通用业务逻辑入口，需结合实现查看细节。
  - `ERROR(AntiMulticlientResult.COORDINATOR_ERROR)`：通用业务逻辑入口，需结合实现查看细节。
  - `InitializationResult(AntiMulticlientResult antiMulticlientResult)`：初始化模块、资源或运行时状态。
  - `public AntiMulticlientResult getAntiMulticlientResult()`：读取并返回状态/数据。

## `net/server/coordinator/session/IpAddresses.java`

- `class IpAddresses`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static List<Pattern> loadLocalAddressPatterns()`：从外部来源加载数据（数据库/文件/配置）。
  - `public static boolean isLocalAddress(String inetAddress)`：进行条件判定并返回布尔结果。
  - `public static boolean isLanAddress(String inetAddress)`：进行条件判定并返回布尔结果。
  - `private static boolean matchesPattern(Pattern pattern, String searchTerm)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/session/SessionCoordinator.java`

- `class SessionCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
- `enum AntiMulticlientResult`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static SessionCoordinator getInstance()`：读取并返回状态/数据。
  - `private SessionCoordinator()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean attemptAccountAccess(int accountId, Hwid hwid, boolean routineCheck)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static String getSessionRemoteHost(Client client)`：读取并返回状态/数据。
  - `public void updateOnlineClient(Client client)`：更新已有对象/配置/缓存。
  - `private void disconnectClientIfOnline(int accountId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canStartLoginSession(Client client)`：进行条件判定并返回布尔结果。
  - `public void closeLoginSession(Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void clearLoginRemoteHost(Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `public AntiMulticlientResult attemptLoginSession(Client client, Hwid hwid, int accountId, boolean routineCheck)`：通用业务逻辑入口，需结合实现查看细节。
  - `public AntiMulticlientResult attemptGameSession(Client client, int accountId, Hwid hwid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void associateHwidAccountIfAbsent(Hwid hwid, int accountId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Client fetchInTransitionSessionClient(Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeSession(Client client, Boolean immediately)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Hwid pickLoginSessionHwid(Client client)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Hwid getGameSessionHwid(Client client)`：读取并返回状态/数据。
  - `public void clearExpiredHwidHistory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void runUpdateLoginHistory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void printSessionTrace()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void printSessionTrace(Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/session/SessionDAO.java`

- `class SessionDAO`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void deleteExpiredHwidAccounts()`：删除对象、关系或临时状态。
  - `public static List<Hwid> getHwidsForAccount(Connection con, int accountId) throws SQLException`：读取并返回状态/数据。
  - `public static void registerAccountAccess(Connection con, int accountId, Hwid hwid, Instant expiry)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static List<HwidRelevance> getHwidRelevance(Connection con, int accountId) throws SQLException`：读取并返回状态/数据。
  - `public static void updateAccountAccess(Connection con, Hwid hwid, int accountId, Instant expiry, int loginRelevance)`：更新已有对象/配置/缓存。

## `net/server/coordinator/session/SessionInitialization.java`

- `class SessionInitialization`：领域类型或功能模块，职责由同名文件实现定义。
  - `SessionInitialization()`：通用业务逻辑入口，需结合实现查看细节。
  - `private Lock getLock(String remoteHost)`：读取并返回状态/数据。
  - `public InitializationResult initialize(String remoteHost)`：初始化模块、资源或运行时状态。
  - `public void finalize(String remoteHost)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/world/EventRecallCoordinator.java`

- `class EventRecallCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static EventRecallCoordinator getInstance()`：读取并返回状态/数据。
  - `private static boolean isRecallableEvent(EventInstanceManager eim)`：进行条件判定并返回布尔结果。
  - `public EventInstanceManager recallEventInstance(int characterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void storeEventInstance(int characterId, EventInstanceManager eim)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void manageEventInstances()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/world/InviteCoordinator.java`

- `class InviteCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
- `enum InviteResultType`：领域类型或功能模块，职责由同名文件实现定义。
- `enum InviteType`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static boolean createInvite(InviteType type, Character from, Object referenceFrom, int targetCid, Object... params)`：创建对象、会话或业务记录。
  - `public static boolean hasInvite(InviteType type, int targetCid)`：进行条件判定并返回布尔结果。
  - `public static InviteResult answerInvite(InviteType type, int targetCid, Object referenceFrom, boolean answer)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void removeInvite(InviteType type, int targetCid)`：删除对象、关系或临时状态。
  - `public static void removePlayerIncomingInvites(int cid)`：删除对象、关系或临时状态。
  - `public static void runTimeoutSchedule()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/coordinator/world/MonsterAggroCoordinator.java`

- `class MonsterAggroCoordinator`：领域类型或功能模块，职责由同名文件实现定义。
- `class PlayerAggroEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void stopAggroCoordinator()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startAggroCoordinator()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void updateEntryExpiration(PlayerAggroEntry pae)`：更新已有对象/配置/缓存。
  - `private static void insertEntryDamage(PlayerAggroEntry pae, int damage)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean expiredAfterUpdateEntryDamage(PlayerAggroEntry pae, int deltaTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addAggroDamage(Monster mob, int cid, int damage)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void runAggroUpdate(int deltaTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void insertionSortAggroList(List<PlayerAggroEntry> paeList)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isLeadingCharacterAggro(Monster mob, Character player)`：进行条件判定并返回布尔结果。
  - `public void runSortLeadingCharactersAggro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeAggroEntries(Monster mob)`：删除对象、关系或临时状态。
  - `public void addPuppetAggro(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePuppetAggro(Integer cid)`：删除对象、关系或临时状态。
  - `public List<Integer> getPuppetAggroList()`：读取并返回状态/数据。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/guild/Alliance.java`

- `class Alliance`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Alliance(String name, int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean canBeUsedAllianceName(String name)`：进行条件判定并返回布尔结果。
  - `private static List<Character> getPartyGuildMasters(Party party)`：读取并返回状态/数据。
  - `public static Alliance createAlliance(Party party, String name)`：创建对象、会话或业务记录。
  - `public static Alliance createAllianceOnDb(List<Integer> guilds, String name)`：创建对象、会话或业务记录。
  - `public static Alliance loadAlliance(int id)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void saveToDB()`：持久化当前状态到存储层。
  - `public static void disbandAlliance(int allianceId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void removeGuildFromAllianceOnDb(int guildId)`：删除对象、关系或临时状态。
  - `public static boolean removeGuildFromAlliance(int allianceId, int guildId, int worldId)`：删除对象、关系或临时状态。
  - `public void updateAlliancePackets(Character chr)`：更新已有对象/配置/缓存。
  - `public boolean removeGuild(int gid)`：删除对象、关系或临时状态。
  - `public boolean addGuild(int gid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int getGuildIndex(int gid)`：读取并返回状态/数据。
  - `public void setRankTitle(String[] ranks)`：写入或更新状态字段。
  - `public String getRankTitle(int rank)`：读取并返回状态/数据。
  - `public List<Integer> getGuilds()`：读取并返回状态/数据。
  - `public String getAllianceNotice()`：读取并返回状态/数据。
  - `public String getNotice()`：读取并返回状态/数据。
  - `public void setNotice(String notice)`：写入或更新状态字段。
  - `public void increaseCapacity(int inc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCapacity(int newCapacity)`：写入或更新状态字段。
  - `public int getCapacity()`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public GuildCharacter getLeader()`：读取并返回状态/数据。
  - `public void dropMessage(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void sendInvitation(Client c, String targetGuildName, int allianceId)`：向外发送响应、消息或网络包。
  - `public static boolean answerInvitation(int targetId, String targetGuildName, int allianceId, boolean answer)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/guild/Guild.java`

- `class Guild`：领域类型或功能模块，职责由同名文件实现定义。
- `enum BCOp`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Guild(int guildid, int world)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void buildNotifications()`：构建输出对象、包体或配置。
  - `public void writeToDB(boolean bDisband)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public int getLeaderId()`：读取并返回状态/数据。
  - `public int setLeaderId(int charId)`：写入或更新状态字段。
  - `public int getGP()`：读取并返回状态/数据。
  - `public int getLogo()`：读取并返回状态/数据。
  - `public void setLogo(int l)`：写入或更新状态字段。
  - `public int getLogoColor()`：读取并返回状态/数据。
  - `public void setLogoColor(int c)`：写入或更新状态字段。
  - `public int getLogoBG()`：读取并返回状态/数据。
  - `public void setLogoBG(int bg)`：写入或更新状态字段。
  - `public int getLogoBGColor()`：读取并返回状态/数据。
  - `public void setLogoBGColor(int c)`：写入或更新状态字段。
  - `public String getNotice()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public List<GuildCharacter> getMembers()`：读取并返回状态/数据。
  - `public int getCapacity()`：读取并返回状态/数据。
  - `public int getSignature()`：读取并返回状态/数据。
  - `public void broadcastNameChanged()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastEmblemChanged()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastInfoChanged()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcast(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcast(Packet packet, int exception)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcast(Packet packet, int exceptionId, BCOp bcop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guildMessage(Packet serverNotice)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void setOnline(int cid, boolean online, int channel)`：写入或更新状态字段。
  - `public void guildChat(String name, int cid, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getRankTitle(int rank)`：读取并返回状态/数据。
  - `public static int createGuild(int leaderId, String name)`：创建对象、会话或业务记录。
  - `public int addGuildMember(GuildCharacter mgc, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void leaveGuild(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void expelMember(GuildCharacter initiator, String name, int cid, NoteService noteService)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeRank(int cid, int newRank)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeRank(GuildCharacter mgc, int newRank)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setGuildNotice(String notice)`：写入或更新状态字段。
  - `public void memberLevelJobUpdate(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean equals(Object other)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public void changeRankTitle(String[] ranks)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disbandGuild()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setGuildEmblem(short bg, byte bgcolor, short logo, byte logocolor)`：写入或更新状态字段。
  - `public GuildCharacter getMGC(int cid)`：读取并返回状态/数据。
  - `public boolean increaseCapacity()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainGP(int amount)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeGP(int amount)`：删除对象、关系或临时状态。
  - `public static GuildResponse sendInvitation(Client c, String targetName)`：向外发送响应、消息或网络包。
  - `public static boolean answerInvitation(int targetId, String targetName, int guildId, boolean answer)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Set<Character> getEligiblePlayersForGuild(Character guildLeader)`：读取并返回状态/数据。
  - `public static void displayGuildRanks(Client c, int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getAllianceId()`：读取并返回状态/数据。
  - `public void setAllianceId(int aid)`：写入或更新状态字段。
  - `public void resetAllianceGuildPlayersRank()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int getIncreaseGuildCost(int size)`：读取并返回状态/数据。

## `net/server/guild/GuildCharacter.java`

- `class GuildCharacter`：领域类型或功能模块，职责由同名文件实现定义。
  - `public GuildCharacter(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public GuildCharacter(Character chr, int _id, int _lv, String _name, int _channel, int _world, int _job, int _rank, int _gid, boolean _on, int _allianceRank)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCharacter(Character ch)`：写入或更新状态字段。
  - `public Character getCharacter()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public void setLevel(int l)`：写入或更新状态字段。
  - `public int getId()`：读取并返回状态/数据。
  - `public void setChannel(int ch)`：写入或更新状态字段。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public int getWorld()`：读取并返回状态/数据。
  - `public int getJobId()`：读取并返回状态/数据。
  - `public void setJobId(int job)`：写入或更新状态字段。
  - `public int getGuildId()`：读取并返回状态/数据。
  - `public void setGuildId(int gid)`：写入或更新状态字段。
  - `public int getGuildRank()`：读取并返回状态/数据。
  - `public void setOfflineGuildRank(int rank)`：写入或更新状态字段。
  - `public void setGuildRank(int rank)`：写入或更新状态字段。
  - `public int getAllianceRank()`：读取并返回状态/数据。
  - `public void setAllianceRank(int rank)`：写入或更新状态字段。
  - `public boolean isOnline()`：进行条件判定并返回布尔结果。
  - `public void setOnline(boolean f)`：写入或更新状态字段。
  - `public String getName()`：读取并返回状态/数据。
  - `public boolean equals(Object other)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。

## `net/server/guild/GuildPackets.java`

- `class GuildPackets`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Packet showGuildInfo(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildMemberOnline(int guildId, int chrId, boolean bOnline)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildInvite(int guildId, String charName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet createGuildMessage(String masterName, String guildName)`：创建对象、会话或业务记录。
  - `public static Packet genericGuildMessage(byte code)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet responseGuildMessage(byte code, String targetName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet newGuildMember(GuildCharacter mgc)`：创建对象、会话或业务记录。
  - `public static Packet memberLeft(GuildCharacter mgc, boolean bExpelled)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet changeRank(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildNotice(int guildId, String notice)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildMemberLevelJobUpdate(GuildCharacter mgc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet rankTitleChange(int guildId, String[] ranks)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildDisband(int guildId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildQuestWaitingNotice(byte channel, int waitingPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildEmblemChange(int guildId, short bg, byte bgcolor, short logo, byte logoColor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildCapacityChange(int guildId, int capacity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void addThread(final OutPacket p, ResultSet rs) throws SQLException`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet BBSThreadList(ResultSet rs, int start) throws SQLException`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet showThread(int localthreadid, ResultSet threadRS, ResultSet repliesRS) throws SQLException, RuntimeException`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet showGuildRanks(int npcid, ResultSet rs) throws SQLException`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet showPlayerRanks(int npcid, List<Pair<String, Integer>> worldRanking)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet updateGP(int guildId, int GP)`：更新已有对象/配置/缓存。
  - `public static void getGuildInfo(OutPacket p, Guild guild)`：读取并返回状态/数据。
  - `public static Packet getAllianceInfo(Alliance alliance)`：读取并返回状态/数据。
  - `public static Packet updateAllianceInfo(Alliance alliance, int world)`：更新已有对象/配置/缓存。
  - `public static Packet getGuildAlliances(Alliance alliance, int worldId)`：读取并返回状态/数据。
  - `public static Packet addGuildToAlliance(Alliance alliance, int newGuild, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet allianceMemberOnline(Character mc, boolean online)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet allianceNotice(int id, String notice)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet changeAllianceRankTitle(int alliance, String[] ranks)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet updateAllianceJobLevel(Character mc)`：更新已有对象/配置/缓存。
  - `public static Packet removeGuildFromAlliance(Alliance alliance, int expelledGuild, int worldId)`：删除对象、关系或临时状态。
  - `public static Packet disbandAlliance(int alliance)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet allianceInvite(int allianceid, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet GuildBoss_HealerMove(short nY)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet GuildBoss_PulleyStateChange(byte nState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildNameChanged(int chrid, String guildName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet guildMarkChanged(int chrId, Guild guild)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Packet sendShowInfo(int allianceid, int playerid)`：向外发送响应、消息或网络包。
  - `public static Packet sendInvitation(int allianceid, int playerid, final String guildname)`：向外发送响应、消息或网络包。
  - `public static Packet sendChangeGuild(int allianceid, int playerid, int guildid, int option)`：向外发送响应、消息或网络包。
  - `public static Packet sendChangeLeader(int allianceid, int playerid, int victim)`：向外发送响应、消息或网络包。
  - `public static Packet sendChangeRank(int allianceid, int playerid, int int1, byte byte1)`：向外发送响应、消息或网络包。

## `net/server/guild/GuildResponse.java`

- `enum GuildResponse`：领域类型或功能模块，职责由同名文件实现定义。
  - `NOT_IN_CHANNEL(0x2a),`：通用业务逻辑入口，需结合实现查看细节。
  - `ALREADY_IN_GUILD(0x28),`：通用业务逻辑入口，需结合实现查看细节。
  - `NOT_IN_GUILD(0x2d),`：通用业务逻辑入口，需结合实现查看细节。
  - `NOT_FOUND_INVITE(0x2e),`：通用业务逻辑入口，需结合实现查看细节。
  - `MANAGING_INVITE(0x36),`：通用业务逻辑入口，需结合实现查看细节。
  - `DENIED_INVITE(0x37)`：通用业务逻辑入口，需结合实现查看细节。
  - `GuildResponse(int val)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet getPacket(String targetName)`：读取并返回状态/数据。

## `net/server/guild/GuildSummary.java`

- `class GuildSummary`：领域类型或功能模块，职责由同名文件实现定义。
  - `public GuildSummary(Guild g)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public short getLogoBG()`：读取并返回状态/数据。
  - `public byte getLogoBGColor()`：读取并返回状态/数据。
  - `public short getLogo()`：读取并返回状态/数据。
  - `public byte getLogoColor()`：读取并返回状态/数据。
  - `public int getAllianceId()`：读取并返回状态/数据。

## `net/server/handlers/CustomPacketHandler.java`

- `class CustomPacketHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。

## `net/server/handlers/KeepAliveHandler.java`

- `class KeepAliveHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。

## `net/server/handlers/LoginRequiringNoOpHandler.java`

- `class LoginRequiringNoOpHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public static LoginRequiringNoOpHandler getInstance()`：读取并返回状态/数据。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。

## `net/server/handlers/login/AcceptToSHandler.java`

- `class AcceptToSHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/AfterLoginHandler.java`

- `class AfterLoginHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/CharSelectedHandler.java`

- `class CharSelectedHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/CharSelectedWithPicHandler.java`

- `class CharSelectedWithPicHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/CharlistRequestHandler.java`

- `class CharlistRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/CheckCharNameHandler.java`

- `class CheckCharNameHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/CreateCharHandler.java`

- `class CreateCharHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/DeleteCharHandler.java`

- `class DeleteCharHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/GuestLoginHandler.java`

- `class GuestLoginHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/LoginPasswordHandler.java`

- `class LoginPasswordHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。
  - `private static void login(Client c)`：处理认证/会话生命周期。

## `net/server/handlers/login/RegisterPicHandler.java`

- `class RegisterPicHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/RegisterPinHandler.java`

- `class RegisterPinHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/RelogRequestHandler.java`

- `class RelogRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public boolean validateState(Client c)`：校验输入参数或业务约束。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ServerStatusRequestHandler.java`

- `class ServerStatusRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ServerlistRequestHandler.java`

- `class ServerlistRequestHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/SetGenderHandler.java`

- `class SetGenderHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ViewAllCharHandler.java`

- `class ViewAllCharHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ViewAllCharRegisterPicHandler.java`

- `class ViewAllCharRegisterPicHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ViewAllCharSelectedHandler.java`

- `class ViewAllCharSelectedHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public final void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/handlers/login/ViewAllCharSelectedWithPicHandler.java`

- `class ViewAllCharSelectedWithPicHandler`：网络包/事件处理器，按 opcode 或事件类型分发处理。
  - `private static int parseAntiMulticlientError(AntiMulticlientResult res)`：解析输入文本或二进制内容。
  - `public void handlePacket(InPacket p, Client c)`：处理事件/请求/消息分发。

## `net/server/services/BaseScheduler.java`

- `class BaseScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected BaseScheduler()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected BaseScheduler(List<Lock> extLocks)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void addListener(SchedulerListener listener)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void lockScheduler()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unlockScheduler()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void runBaseSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void registerEntry(Object key, Runnable removalAction, long duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void interruptEntry(Object key)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchRemovedEntries(List<Object> toRemove, boolean fromUpdate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/BaseService.java`

- `class BaseService`：业务编排层，组织领域逻辑与持久化调用。
  - `protected static int getChannelSchedulerIndex(int mapid)`：读取并返回状态/数据。
  - `public abstract void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/SchedulerListener.java`

- `interface SchedulerListener`：领域类型或功能模块，职责由同名文件实现定义。
  - `void removedScheduledEntries(List<Object> entries, boolean update)`：删除对象、关系或临时状态。

## `net/server/services/Service.java`

- `class Service`：业务编排层，组织领域逻辑与持久化调用。
  - `public Service(Class<T> s)`：通用业务逻辑入口，需结合实现查看细节。
  - `public T getService()`：读取并返回状态/数据。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/ServiceType.java`

- `interface ServiceType`：领域类型或功能模块，职责由同名文件实现定义。
  - `Service createService()`：创建对象、会话或业务记录。
  - `int ordinal()`：通用业务逻辑入口，需结合实现查看细节。
  - `T[] enumValues()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/ServicesManager.java`

- `class ServicesManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ServicesManager(ServiceType serviceBundle)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Service getAccess(ServiceType s)`：读取并返回状态/数据。
  - `public void shutdown()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/EventService.java`

- `class EventService`：业务编排层，组织领域逻辑与持久化调用。
- `class EventScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerEventAction(int mapid, Runnable runAction, long delay)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/MobAnimationService.java`

- `class MobAnimationService`：业务编排层，组织领域逻辑与持久化调用。
- `class MobAnimationScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobAnimationService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean registerMobOnAnimationEffect(int mapid, int mobHash, long delay)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/MobClearSkillService.java`

- `class MobClearSkillService`：业务编排层，组织领域逻辑与持久化调用。
- `class MobClearSkillScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobClearSkillService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerMobClearSkillAction(int mapid, Runnable runAction, long delay)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/MobMistService.java`

- `class MobMistService`：业务编排层，组织领域逻辑与持久化调用。
- `class MobMistScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobMistService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerMobMistCancelAction(int mapid, Runnable runAction, long delay)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/MobStatusService.java`

- `class MobStatusService`：业务编排层，组织领域逻辑与持久化调用。
- `class MobStatusScheduler`：领域类型或功能模块，职责由同名文件实现定义。
- `class MobStatusOvertimeEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobStatusService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration, Runnable overtimeAction, int overtimeDelay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void interruptMobStatus(int mapid, MonsterStatusEffect mse)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/channel/OverallService.java`

- `class OverallService`：业务编排层，组织领域逻辑与持久化调用。
- `class OverallScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public OverallService()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerOverallAction(int mapid, Runnable runAction, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceRunOverallAction(int mapid, Runnable runAction)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/task/world/CharacterSaveService.java`

- `class CharacterSaveService`：业务编排层，组织领域逻辑与持久化调用。
- `class CharacterSaveScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerSaveCharacter(int characterId, Runnable runAction)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/type/ChannelServices.java`

- `enum ChannelServices`：领域类型或功能模块，职责由同名文件实现定义。
  - `MOB_STATUS(MobStatusService.class),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_ANIMATION(MobAnimationService.class),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_CLEAR_SKILL(MobClearSkillService.class),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB_MIST(MobMistService.class),`：通用业务逻辑入口，需结合实现查看细节。
  - `EVENT(EventService.class),`：通用业务逻辑入口，需结合实现查看细节。
  - `OVERALL(OverallService.class)`：通用业务逻辑入口，需结合实现查看细节。
  - `ChannelServices(Class<? extends BaseService> service)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Service createService()`：创建对象、会话或业务记录。
  - `public ChannelServices[] enumValues()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/services/type/WorldServices.java`

- `enum WorldServices`：领域类型或功能模块，职责由同名文件实现定义。
  - `SAVE_CHARACTER(CharacterSaveService.class)`：持久化当前状态到存储层。
  - `WorldServices(Class<? extends BaseService> service)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Service createService()`：创建对象、会话或业务记录。
  - `public WorldServices[] enumValues()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/BaseTask.java`

- `class BaseTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public BaseTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/BossLogTask.java`

- `class BossLogTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/CharacterAutosaverTask.java`

- `class CharacterAutosaverTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public CharacterAutosaverTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/CharacterDiseaseTask.java`

- `class CharacterDiseaseTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/CharacterHpDecreaseTask.java`

- `class CharacterHpDecreaseTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public CharacterHpDecreaseTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/CouponTask.java`

- `class CouponTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/DueyFredrickTask.java`

- `class DueyFredrickTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public DueyFredrickTask(FredrickProcessor fredrickProcessor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/EventRecallCoordinatorTask.java`

- `class EventRecallCoordinatorTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/ExtendValueTask.java`

- `class ExtendValueTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/FamilyDailyResetTask.java`

- `class FamilyDailyResetTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FamilyDailyResetTask(World world)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void resetEntitlementUsage(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/FishingTask.java`

- `class FishingTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public FishingTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/HiredMerchantTask.java`

- `class HiredMerchantTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public HiredMerchantTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/InvitationTask.java`

- `class InvitationTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/LoginCoordinatorTask.java`

- `class LoginCoordinatorTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/LoginStorageTask.java`

- `class LoginStorageTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/MapOwnershipTask.java`

- `class MapOwnershipTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapOwnershipTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/MountTirednessTask.java`

- `class MountTirednessTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MountTirednessTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/OnlineTimeTask.java`

- `class OnlineTimeTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/PartySearchTask.java`

- `class PartySearchTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public PartySearchTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/PetFullnessTask.java`

- `class PetFullnessTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public PetFullnessTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/RankingCommandTask.java`

- `class RankingCommandTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/RankingLoginTask.java`

- `class RankingLoginTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `private void resetMoveRank(boolean job) throws SQLException`：通用业务逻辑入口，需结合实现查看细节。
  - `private void updateRanking(int job, int world) throws SQLException`：更新已有对象/配置/缓存。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/RespawnTask.java`

- `class RespawnTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/ServerMessageTask.java`

- `class ServerMessageTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ServerMessageTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/TimedMapObjectTask.java`

- `class TimedMapObjectTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public TimedMapObjectTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/TimeoutTask.java`

- `class TimeoutTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public TimeoutTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/task/WeddingReservationTask.java`

- `class WeddingReservationTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void run()`：通用业务逻辑入口，需结合实现查看细节。
  - `public WeddingReservationTask(World world)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/world/Messenger.java`

- `class Messenger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Messenger(int id, MessengerCharacter chrfor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public Collection<MessengerCharacter> getMembers()`：读取并返回状态/数据。
  - `public void addMember(MessengerCharacter member, int position)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeMember(MessengerCharacter member)`：删除对象、关系或临时状态。
  - `public int getLowestPosition()`：读取并返回状态/数据。
  - `public int getPositionByName(String name)`：读取并返回状态/数据。

## `net/server/world/MessengerCharacter.java`

- `class MessengerCharacter`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MessengerCharacter(Character maplechar, int position)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public boolean isOnline()`：进行条件判定并返回布尔结果。
  - `public int getPosition()`：读取并返回状态/数据。
  - `public void setPosition(int position)`：写入或更新状态字段。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/world/Party.java`

- `class Party`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Party(int id, PartyCharacter chrfor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean containsMembers(PartyCharacter member)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMember(PartyCharacter member)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeMember(PartyCharacter member)`：删除对象、关系或临时状态。
  - `public void setLeader(PartyCharacter victim)`：写入或更新状态字段。
  - `public void updateMember(PartyCharacter member)`：更新已有对象/配置/缓存。
  - `public PartyCharacter getMemberById(int id)`：读取并返回状态/数据。
  - `public Collection<PartyCharacter> getMembers()`：读取并返回状态/数据。
  - `public List<PartyCharacter> getPartyMembers()`：读取并返回状态/数据。
  - `public List<PartyCharacter> getPartyMembersOnline()`：读取并返回状态/数据。
  - `public Collection<PartyCharacter> getEligibleMembers()`：读取并返回状态/数据。
  - `public void setEligibleMembers(List<PartyCharacter> eliParty)`：写入或更新状态字段。
  - `public PartyCharacter getLeader()`：读取并返回状态/数据。
  - `public List<Integer> getMembersSortedByHistory()`：读取并返回状态/数据。
  - `public byte getPartyDoor(int cid)`：读取并返回状态/数据。
  - `public void addDoor(Integer owner, Door door)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeDoor(Integer owner)`：删除对象、关系或临时状态。
  - `public void assignNewLeader(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public PartyCharacter getMemberByPos(int pos)`：读取并返回状态/数据。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean createParty(Character player, boolean silentCheck)`：创建对象、会话或业务记录。
  - `public static boolean joinParty(Character player, int partyid, boolean silentCheck)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void leaveParty(Party party, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void expelFromParty(Party party, Client c, int expelCid)`：通用业务逻辑入口，需结合实现查看细节。

## `net/server/world/PartyCharacter.java`

- `class PartyCharacter`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartyCharacter(Character maplechar)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PartyCharacter()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getPlayer()`：读取并返回状态/数据。
  - `public Job getJob()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public void setChannel(int channel)`：写入或更新状态字段。
  - `public boolean isLeader()`：进行条件判定并返回布尔结果。
  - `public boolean isOnline()`：进行条件判定并返回布尔结果。
  - `public void setOnline(boolean online)`：写入或更新状态字段。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public void setMapId(int mapid)`：写入或更新状态字段。
  - `public String getName()`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。
  - `public int getJobId()`：读取并返回状态/数据。
  - `public int getGuildId()`：读取并返回状态/数据。
  - `public int hashCode()`：进行条件判定并返回布尔结果。
  - `public boolean equals(Object obj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getWorld()`：读取并返回状态/数据。

## `net/server/world/PartyOperation.java`

- `enum PartyOperation`：领域类型或功能模块，职责由同名文件实现定义。

## `net/server/world/World.java`

- `class World`：领域类型或功能模块，职责由同名文件实现定义。
  - `public World(int world, int flag, String eventmsg, float expRate, float dropRate, float bossDropRate, float mesoRate, float questRate, float travelRate, float fishingRate)`：通用业务逻辑入口，需结合实现查看细节。
  - `return getAllCharactersView()`：读取并返回状态/数据。
  - `synchronized (families)`：通用业务逻辑入口，需结合实现查看细节。
  - `synchronized (families)`：通用业务逻辑入口，需结合实现查看细节。
  - `synchronized (families)`：通用业务逻辑入口，需结合实现查看细节。
  - `synchronized (families)`：通用业务逻辑入口，需结合实现查看细节。
  - `return getWorldCapacityStatus() == 2`：读取并返回状态/数据。
  - `try (Connection con = DatabaseConnection.getConnection(); PreparedStatement ps = con.prepareStatement("UPDATE characters SET guildid = ?, guildrank = ? WHERE id = ?"))`：通用业务逻辑入口，需结合实现查看细节。
  - `unregisterCharacterPartyInternal(chrid)`：通用业务逻辑入口，需结合实现查看细节。
  - `registerCharacterParty(chrfor.getId(), partyid)`：通用业务逻辑入口，需结合实现查看细节。
  - `registerCharacterParty(target.getId(), party.getId())`：通用业务逻辑入口，需结合实现查看细节。
  - `unregisterCharacterParty(target.getId())`：通用业务逻辑入口，需结合实现查看细节。
  - `disbandParty(partyid)`：通用业务逻辑入口，需结合实现查看细节。
  - `pushRelationshipCouple(couple)`：通用业务逻辑入口，需结合实现查看细节。
  - `pushRelationshipCouple(couple)`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.executeQuery())`：通用业务逻辑入口，需结合实现查看细节。
  - `try (ResultSet rs = ps.getGeneratedKeys())`：通用业务逻辑入口，需结合实现查看细节。
  - `synchronized (fishingAttempters)`：通用业务逻辑入口，需结合实现查看细节。

## `property/ServiceProperty.java`

- `class ServiceProperty`：领域类型或功能模块，职责由同名文件实现定义。

## `provider/Data.java`

- `interface Data`：领域类型或功能模块，职责由同名文件实现定义。
  - `String getName()`：读取并返回状态/数据。
  - `DataType getType()`：读取并返回状态/数据。
  - `List<Data> getChildren()`：读取并返回状态/数据。
  - `Data getChildByPath(String path)`：读取并返回状态/数据。
  - `Object getData()`：读取并返回状态/数据。
  - `String getAttributeValue(String name)`：读取并返回状态/数据。

## `provider/DataDirectoryEntry.java`

- `interface DataDirectoryEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `List<DataDirectoryEntry> getSubdirectories()`：读取并返回状态/数据。
  - `List<DataFileEntry> getFiles()`：读取并返回状态/数据。
  - `DataEntry getEntry(String name)`：读取并返回状态/数据。

## `provider/DataEntity.java`

- `interface DataEntity`：领域类型或功能模块，职责由同名文件实现定义。
  - `String getName()`：读取并返回状态/数据。
  - `DataEntity getParent()`：读取并返回状态/数据。

## `provider/DataEntry.java`

- `interface DataEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `String getName()`：读取并返回状态/数据。
  - `int getSize()`：读取并返回状态/数据。
  - `int getChecksum()`：读取并返回状态/数据。
  - `int getOffset()`：读取并返回状态/数据。

## `provider/DataFileEntry.java`

- `interface DataFileEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `void setOffset(int offset)`：写入或更新状态字段。

## `provider/DataProvider.java`

- `interface DataProvider`：领域类型或功能模块，职责由同名文件实现定义。
  - `Data getData(String path)`：读取并返回状态/数据。
  - `DataDirectoryEntry getRoot()`：读取并返回状态/数据。

## `provider/DataProviderFactory.java`

- `class DataProviderFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static DataProvider getWZ(Path in)`：读取并返回状态/数据。
  - `public static DataProvider getDataProvider(WZFiles in)`：读取并返回状态/数据。

## `provider/DataTool.java`

- `class DataTool`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static String getString(Data data)`：读取并返回状态/数据。
  - `public static String getString(Data data, String def)`：读取并返回状态/数据。
  - `public static String getString(String path, Data data)`：读取并返回状态/数据。
  - `public static String getString(String path, Data data, String def)`：读取并返回状态/数据。
  - `public static double getDouble(Data data)`：读取并返回状态/数据。
  - `public static float getFloat(Data data)`：读取并返回状态/数据。
  - `public static int getInt(Data data)`：读取并返回状态/数据。
  - `public static int getInt(String path, Data data)`：读取并返回状态/数据。
  - `public static int getIntConvert(Data data)`：读取并返回状态/数据。
  - `public static int getIntConvert(Data data, int def)`：读取并返回状态/数据。
  - `public static int getIntConvert(String path, Data data)`：读取并返回状态/数据。
  - `public static int getInt(Data data, int def)`：读取并返回状态/数据。
  - `public static int getInt(String path, Data data, int def)`：读取并返回状态/数据。
  - `public static int getIntConvert(String path, Data data, int def)`：读取并返回状态/数据。
  - `public static Integer getInteger(String path, Data data)`：读取并返回状态/数据。
  - `public static int getInteger(String path, Data data, int def)`：读取并返回状态/数据。
  - `public static Short getShort(String path, Data data)`：读取并返回状态/数据。
  - `public static short getShort(String path, Data data, short def)`：读取并返回状态/数据。
  - `public static Long getLong(String path, Data data)`：读取并返回状态/数据。
  - `public static long getLong(String path, Data data, long def)`：读取并返回状态/数据。
  - `public static Point getPoint(Data data)`：读取并返回状态/数据。
  - `public static Point getPoint(String path, Data data)`：读取并返回状态/数据。
  - `public static Point getPoint(String path, Data data, Point def)`：读取并返回状态/数据。
  - `public static String getFullDataPath(Data data)`：读取并返回状态/数据。
  - `public static String getAttributeValue(Data data,String name)`：读取并返回状态/数据。
  - `public static String getAttributeValue(Data data,String name,String def)`：读取并返回状态/数据。
  - `public static int getAttributeValueInt(Data data,String name,int def)`：读取并返回状态/数据。

## `provider/wz/DataType.java`

- `enum DataType`：领域类型或功能模块，职责由同名文件实现定义。

## `provider/wz/WZDirectoryEntry.java`

- `class WZDirectoryEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public WZDirectoryEntry(String name, int size, int checksum, DataEntity parent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public WZDirectoryEntry()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addDirectory(DataDirectoryEntry dir)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addFile(DataFileEntry fileEntry)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<DataDirectoryEntry> getSubdirectories()`：读取并返回状态/数据。
  - `public List<DataFileEntry> getFiles()`：读取并返回状态/数据。
  - `public DataEntry getEntry(String name)`：读取并返回状态/数据。

## `provider/wz/WZEntry.java`

- `class WZEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public WZEntry(String name, int size, int checksum, DataEntity parent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public int getSize()`：读取并返回状态/数据。
  - `public int getChecksum()`：读取并返回状态/数据。
  - `public int getOffset()`：读取并返回状态/数据。
  - `public DataEntity getParent()`：读取并返回状态/数据。

## `provider/wz/WZFileEntry.java`

- `class WZFileEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public WZFileEntry(String name, int size, int checksum, DataEntity parent)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getOffset()`：读取并返回状态/数据。
  - `public void setOffset(int offset)`：写入或更新状态字段。

## `provider/wz/WZFiles.java`

- `enum WZFiles`：领域类型或功能模块，职责由同名文件实现定义。
  - `QUEST("Quest"),`：通用业务逻辑入口，需结合实现查看细节。
  - `ETC("Etc"),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM("Item"),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHARACTER("Character"),`：通用业务逻辑入口，需结合实现查看细节。
  - `STRING("String"),`：通用业务逻辑入口，需结合实现查看细节。
  - `LIST("List"),`：查询并返回匹配集合或单项结果。
  - `MOB("Mob"),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAP("Map"),`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC("Npc"),`：通用业务逻辑入口，需结合实现查看细节。
  - `REACTOR("Reactor"),`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL("Skill"),`：通用业务逻辑入口，需结合实现查看细节。
  - `SOUND("Sound"),`：通用业务逻辑入口，需结合实现查看细节。
  - `UI("UI")`：通用业务逻辑入口，需结合实现查看细节。
  - `WZFiles(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Path getFile()`：读取并返回状态/数据。
  - `public String getFilePath()`：读取并返回状态/数据。

## `provider/wz/XMLDomMapleData.java`

- `class XMLDomMapleData`：领域类型或功能模块，职责由同名文件实现定义。
  - `public XMLDomMapleData(FileInputStream fis, Path imageDataDir)`：通用业务逻辑入口，需结合实现查看细节。
  - `private XMLDomMapleData(Node node)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized Data getChildByPath(String path)`：读取并返回状态/数据。
  - `public synchronized List<Data> getChildren()`：读取并返回状态/数据。
  - `public synchronized Object getData()`：读取并返回状态/数据。
  - `public synchronized DataType getType()`：读取并返回状态/数据。
  - `public synchronized DataEntity getParent()`：读取并返回状态/数据。
  - `public synchronized String getName()`：读取并返回状态/数据。
  - `public synchronized Iterator<Data> iterator()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized String getAttributeValue(String name)`：读取并返回状态/数据。

## `provider/wz/XMLWZFile.java`

- `class XMLWZFile`：领域类型或功能模块，职责由同名文件实现定义。
  - `public XMLWZFile(Path fileIn)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void fillMapleDataEntitys(Path lroot, WZDirectoryEntry wzdir)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized Data getData(String path)`：读取并返回状态/数据。
  - `public DataDirectoryEntry getRoot()`：读取并返回状态/数据。

## `scripting/AbstractPlayerInteraction.java`

- `class AbstractPlayerInteraction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbstractPlayerInteraction(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Client getClient()`：读取并返回状态/数据。
  - `public Character getPlayer()`：读取并返回状态/数据。
  - `public Character getChar()`：读取并返回状态/数据。
  - `public int getJobId()`：读取并返回状态/数据。
  - `public Job getJob()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public MapleMap getMap()`：读取并返回状态/数据。
  - `public int getHourOfDay()`：读取并返回状态/数据。
  - `public int getMarketPortalId(int mapId)`：读取并返回状态/数据。
  - `private int getMarketPortalId(MapleMap map)`：读取并返回状态/数据。
  - `public void warp(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warp(int map, int portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warp(int map, String portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpMap(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpParty(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpParty(int id, int portalId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpParty(int map, String portalName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpParty(int id, int fromMinId, int fromMaxId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpParty(int id, int portalId, int fromMinId, int fromMaxId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapleMap getWarpMap(int map)`：读取并返回状态/数据。
  - `public MapleMap getMap(int map)`：读取并返回状态/数据。
  - `public int countAllMonstersOnMap(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countMonster()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMapObjects(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public EventManager getEventManager(String event)`：读取并返回状态/数据。
  - `public EventInstanceManager getEventInstance()`：读取并返回状态/数据。
  - `public Inventory getInventory(int type)`：读取并返回状态/数据。
  - `public Inventory getInventory(InventoryType type)`：读取并返回状态/数据。
  - `public boolean hasItem(int itemid)`：进行条件判定并返回布尔结果。
  - `public boolean hasItem(int itemid, int quantity)`：进行条件判定并返回布尔结果。
  - `public boolean haveItem(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean haveItem(int itemid, int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getItemQuantity(int itemid)`：读取并返回状态/数据。
  - `public boolean haveItemWithId(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean haveItemWithId(int itemid, boolean checkEquipped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canHold(int itemid)`：进行条件判定并返回布尔结果。
  - `public boolean canHold(int itemid, int quantity)`：进行条件判定并返回布尔结果。
  - `public boolean canHold(int itemid, int quantity, int removeItemid, int removeQuantity)`：进行条件判定并返回布尔结果。
  - `private List<Integer> convertToIntegerList(List<Object> objects)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canHoldAll(List<Object> itemids)`：进行条件判定并返回布尔结果。
  - `public boolean canHoldAll(List<Object> itemids, List<Object> quantity)`：进行条件判定并返回布尔结果。
  - `private boolean canHoldAll(List<Integer> itemids, List<Integer> quantity, boolean isInteger)`：进行条件判定并返回布尔结果。
  - `public boolean canHoldAllAfterRemoving(List<Integer> toAddItemids, List<Integer> toAddQuantity, List<Integer> toRemoveItemids, List<Integer> toRemoveQuantity)`：进行条件判定并返回布尔结果。
  - `public final QuestStatus getQuestRecord(final int id)`：读取并返回状态/数据。
  - `public final QuestStatus getQuestNoRecord(final int id)`：读取并返回状态/数据。
  - `public void openNpc(int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void openNpc(int npcid, String script)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getQuestStatus(int id)`：读取并返回状态/数据。
  - `private QuestStatus.Status getQuestStat(int id)`：读取并返回状态/数据。
  - `public boolean isQuestCompleted(int id)`：进行条件判定并返回布尔结果。
  - `public boolean isQuestActive(int id)`：进行条件判定并返回布尔结果。
  - `public boolean isQuestStarted(int id)`：进行条件判定并返回布尔结果。
  - `public void setQuestProgress(int id, String progress)`：写入或更新状态字段。
  - `public void setQuestProgress(int id, int progress)`：写入或更新状态字段。
  - `public void setQuestProgress(int id, int infoNumber, int progress)`：写入或更新状态字段。
  - `public void setQuestProgress(int id, int infoNumber, String progress)`：写入或更新状态字段。
  - `public String getQuestProgress(int id)`：读取并返回状态/数据。
  - `public String getQuestProgress(int id, int infoNumber)`：读取并返回状态/数据。
  - `public int getQuestProgressInt(int id)`：读取并返回状态/数据。
  - `public int getQuestProgressInt(int id, int infoNumber)`：读取并返回状态/数据。
  - `public void resetAllQuestProgress(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetQuestProgress(int id, int infoNumber)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceStartQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceStartQuest(int id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceCompleteQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceCompleteQuest(int id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(short id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(short id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(short id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(short id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(int id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(int id, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item evolvePet(byte slot, int afterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainItem(int id, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainItem(int id, short quantity, boolean show)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainItem(int id, boolean show)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainItem(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage, long expires)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage, long expires, Pet from)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainFame(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeMusic(String songName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playerMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void message(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mapMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mapEffect(String path)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mapSound(String path)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void displayAranIntro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showIntro(String path)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showInfo(String path)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guildMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Guild getGuild()`：读取并返回状态/数据。
  - `public Party getParty()`：读取并返回状态/数据。
  - `public boolean isLeader()`：进行条件判定并返回布尔结果。
  - `public boolean isGuildLeader()`：进行条件判定并返回布尔结果。
  - `public boolean isPartyLeader()`：进行条件判定并返回布尔结果。
  - `public boolean isEventLeader()`：进行条件判定并返回布尔结果。
  - `public void givePartyItems(int id, short quantity, List<Character> party)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeHPQItems()`：删除对象、关系或临时状态。
  - `public void removePartyItems(int id)`：删除对象、关系或临时状态。
  - `public void giveCharacterExp(int amount, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void givePartyExp(int amount, List<Character> party)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void givePartyExp(String PQ)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void givePartyExp(String PQ, boolean instance)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeFromParty(int id, List<Character> party)`：删除对象、关系或临时状态。
  - `public void removeAll(int id)`：删除对象、关系或临时状态。
  - `public void removeAll(int id, Client cl)`：删除对象、关系或临时状态。
  - `public void removeAllByInventory(int invType)`：删除对象、关系或临时状态。
  - `public void removeAllByInventorySlot(int invType, short slot)`：删除对象、关系或临时状态。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public int getPlayerCount(int mapid)`：读取并返回状态/数据。
  - `public void showInstruction(String msg, int width, int height)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disableMinimap()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isAllReactorState(final int reactorId, final int state)`：进行条件判定并返回布尔结果。
  - `public void resetMap(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void useItem(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelItem(final int id)`：进行条件判定并返回布尔结果。
  - `public void teachSkill(int skillid, byte level, byte masterLevel, long expiration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void teachSkill(int skillid, byte level, byte masterLevel, long expiration, boolean force)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeEquipFromSlot(short slot)`：删除对象、关系或临时状态。
  - `public void gainAndEquip(int itemid, short slot)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnNpc(int npcId, Point pos, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(int id, int x, int y)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Monster getMonsterLifeFactory(int mid)`：读取并返回状态/数据。
  - `public void spawnGuide()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeGuide()`：删除对象、关系或临时状态。
  - `public void displayGuide(int num)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void goDojoUp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetDojoEnergy()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetPartyDojoEnergy()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void enableActions()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showEffect(String effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dojoEnergy()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void talkGuide(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void guideHint(int hint)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateAreaInfo(Short area, String info)`：更新已有对象/配置/缓存。
  - `public boolean containsAreaInfo(short area, String info)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void earnTitle(String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showInfoText(String msg)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void openUI(byte ui)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void lockUI()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unlockUI()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playSound(String sound)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void environmentChange(String env, int mode)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String numberWithCommas(int number)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Pyramid getPyramid()`：读取并返回状态/数据。
  - `public int createExpedition(ExpeditionType type)`：创建对象、会话或业务记录。
  - `public int createExpedition(ExpeditionType type, boolean silent, int minPlayers, int maxPlayers)`：创建对象、会话或业务记录。
  - `public void endExpedition(Expedition exped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Expedition getExpedition(ExpeditionType type)`：读取并返回状态/数据。
  - `public String getExpeditionMemberNames(ExpeditionType type)`：读取并返回状态/数据。
  - `public boolean isLeaderExpedition(ExpeditionType type)`：进行条件判定并返回布尔结果。
  - `public long getJailTimeLeft()`：读取并返回状态/数据。
  - `public List<Pet> getDriedPets()`：读取并返回状态/数据。
  - `public List<Item> getUnclaimedMarriageGifts()`：读取并返回状态/数据。
  - `public boolean startDungeonInstance(int dungeonid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canGetFirstJob(int jobType)`：进行条件判定并返回布尔结果。
  - `public String getFirstJobStatRequirement(int jobType)`：读取并返回状态/数据。
  - `public void npcTalk(int npcid, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getCurrentTime()`：读取并返回状态/数据。
  - `public void weakenAreaBoss(int monsterId, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applySealSkill(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applyReduceAvoid(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void sendBlueNotice(MapleMap map, String message)`：向外发送响应、消息或网络包。
  - `public String getCharacterExtendValue(String extendName)`：读取并返回状态/数据。
  - `public String getCharacterExtendValue(String extendName, boolean isDaily)`：读取并返回状态/数据。
  - `public String getAccountExtendValue(String extendName)`：读取并返回状态/数据。
  - `public String getAccountExtendValue(String extendName, boolean isDaily)`：读取并返回状态/数据。
  - `public void saveOrUpdateCharacterExtendValue(String extendName, String extendValue)`：持久化当前状态到存储层。
  - `public void saveOrUpdateCharacterExtendValue(String extendName, String extendValue, boolean isDaily)`：持久化当前状态到存储层。
  - `public void saveOrUpdateAccountExtendValue(String extendName, String extendValue)`：持久化当前状态到存储层。
  - `public void saveOrUpdateAccountExtendValue(String extendName, String extendValue, boolean isDaily)`：持久化当前状态到存储层。
  - `public void gainEquip(Equip equip)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getOnlineTime()`：读取并返回状态/数据。

## `scripting/AbstractScriptManager.java`

- `class AbstractScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `protected AbstractScriptManager()`：通用业务逻辑入口，需结合实现查看细节。
  - `protected ScriptEngine getInvocableScriptEngine(String path)`：读取并返回状态/数据。
  - `protected ScriptEngine getInvocableScriptEngine(String path, Client c)`：读取并返回状态/数据。
  - `private void enableScriptHostAccess(GraalJSScriptEngine engine)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void resetContext(String path, Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/SynchronizedInvocable.java`

- `class SynchronizedInvocable`：领域类型或功能模块，职责由同名文件实现定义。
  - `private SynchronizedInvocable(Invocable invocable)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Invocable of(Invocable invocable)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized Object invokeMethod(Object thiz, String name, Object... args) throws ScriptException, NoSuchMethodException`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized Object invokeFunction(String name, Object... args) throws ScriptException, NoSuchMethodException`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized <T> T getInterface(Class<T> clasz)`：读取并返回状态/数据。
  - `public synchronized <T> T getInterface(Object thiz, Class<T> clasz)`：读取并返回状态/数据。

## `scripting/event/EventInstanceManager.java`

- `class EventInstanceManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventInstanceManager(EventManager em, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setName(String name)`：写入或更新状态字段。
  - `public EventManager getEm()`：读取并返回状态/数据。
  - `public int getEventPlayersJobs()`：读取并返回状态/数据。
  - `public void applyEventPlayersItemBuff(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void applyEventPlayersSkillBuff(int skillId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void applyEventPlayersSkillBuff(int skillId, int skillLv)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveEventPlayersExp(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveEventPlayersExp(int gain, int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveEventPlayersMeso(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void giveEventPlayersMeso(int gain, int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Object invokeScriptFunction(String name, Object... args) throws ScriptException, NoSuchMethodException`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void registerPlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void registerPlayer(final Character chr, boolean runEntryScript)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void exitPlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void restartEventTimer(long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startEventTimer(long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addEventTimer(long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dismissEventTimer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stopEventTimer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isTimerStarted()`：进行条件判定并返回布尔结果。
  - `public long getTimeLeft()`：读取并返回状态/数据。
  - `public void registerParty(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerParty(Party party, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerExpedition(Expedition exped)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerExpeditionTeam(Expedition exped, int recruitMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unregisterPlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getPlayerCount()`：读取并返回状态/数据。
  - `public Character getPlayerById(int id)`：读取并返回状态/数据。
  - `public List<Character> getPlayers()`：读取并返回状态/数据。
  - `private List<Character> getPlayerList()`：读取并返回状态/数据。
  - `public void registerMonster(Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void movePlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changedMap(final Character chr, final int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void afterChangedMap(final Character chr, final int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void changedLeader(final PartyCharacter ldr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void monsterKilled(final Monster mob, final boolean hasKiller)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void friendlyKilled(final Monster mob, final boolean hasKiller)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void friendlyDamaged(final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void friendlyItemDrop(final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playerKilled(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reviveMonster(final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean revivePlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playerDisconnected(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void monsterKilled(Character chr, final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getKillCount(Character chr)`：读取并返回状态/数据。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void dispose(boolean shutdown)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapManager getMapFactory()`：读取并返回状态/数据。
  - `public void schedule(final String methodName, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public MapleMap getMapInstance(int mapId)`：读取并返回状态/数据。
  - `public void setIntProperty(String key, Integer value)`：写入或更新状态字段。
  - `public void setProperty(String key, Integer value)`：写入或更新状态字段。
  - `public void setProperty(String key, String value)`：写入或更新状态字段。
  - `public Object setProperty(String key, String value, boolean prev)`：写入或更新状态字段。
  - `public void setObjectProperty(String key, Object obj)`：写入或更新状态字段。
  - `public String getProperty(String key)`：读取并返回状态/数据。
  - `public int getIntProperty(String key)`：读取并返回状态/数据。
  - `public Object getObjectProperty(String key)`：读取并返回状态/数据。
  - `public void leftParty(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disbandParty()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearPQ()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePlayer(final Character chr)`：删除对象、关系或临时状态。
  - `public boolean isLeader(Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean isEventLeader(Character chr)`：进行条件判定并返回布尔结果。
  - `public final MapleMap getInstanceMap(final int mapid)`：读取并返回状态/数据。
  - `public final boolean disposeIfPlayerBelow(final byte size, final int towarp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnNpc(int npcId, Point pos, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispatchRaiseQuestMobCount(int mobid, int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Monster getMonster(int mid)`：读取并返回状态/数据。
  - `private List<Integer> convertToIntegerList(List<Object> objects)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setEventClearStageExp(List<Object> gain)`：写入或更新状态字段。
  - `public void setEventClearStageMeso(List<Object> gain)`：写入或更新状态字段。
  - `public Integer getClearStageExp(int stage)`：读取并返回状态/数据。
  - `public Integer getClearStageMeso(int stage)`：读取并返回状态/数据。
  - `public List<Integer> getClearStageBonus(int stage)`：读取并返回状态/数据。
  - `private void dropExclusiveItems(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropAllExclusiveItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void setExclusiveItems(List<Object> items)`：写入或更新状态字段。
  - `public final void setEventRewards(List<Object> rwds, List<Object> qtys, int expGiven)`：写入或更新状态字段。
  - `public final void setEventRewards(List<Object> rwds, List<Object> qtys)`：写入或更新状态字段。
  - `public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys)`：写入或更新状态字段。
  - `public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys, int expGiven)`：写入或更新状态字段。
  - `private byte getRewardListRequirements(int level)`：读取并返回状态/数据。
  - `private boolean hasRewardSlot(Character player, int eventLevel)`：进行条件判定并返回布尔结果。
  - `public final boolean giveEventReward(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean giveEventReward(Character player, int eventLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void disposeExpedition()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final synchronized void startEvent()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void setEventCleared()`：写入或更新状态字段。
  - `public final boolean isEventCleared()`：进行条件判定并返回布尔结果。
  - `public final boolean isEventDisposed()`：进行条件判定并返回布尔结果。
  - `private boolean isEventTeamLeaderOn()`：进行条件判定并返回布尔结果。
  - `public final boolean checkEventTeamLacking(boolean leavingEventMap, int minPlayers)`：校验输入参数或业务约束。
  - `public final boolean isExpeditionTeamLackingNow(boolean leavingEventMap, int minPlayers, Character quitter)`：进行条件判定并返回布尔结果。
  - `public final boolean isEventTeamLackingNow(boolean leavingEventMap, int minPlayers, Character quitter)`：进行条件判定并返回布尔结果。
  - `public final boolean isEventTeamTogether()`：进行条件判定并返回布尔结果。
  - `public final void warpEventTeam(int warpFrom, int warpTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpEventTeam(int warpTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpEventTeamToMapSpawnPoint(int warpFrom, int warpTo, int toSp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpEventTeamToMapSpawnPoint(int warpTo, int toSp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int getLeaderId()`：读取并返回状态/数据。
  - `public Character getLeader()`：读取并返回状态/数据。
  - `public final void setLeader(Character chr)`：写入或更新状态字段。
  - `public final void showWrongEffect()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showWrongEffect(int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect(boolean hasGate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect(int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect(boolean hasGate, int mapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect(int mapId, String mapObj, int newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void showClearEffect(boolean hasGate, int mapId, String mapObj, int newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void recoverOpenedGate(Character chr, int thisMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void giveEventPlayersStageReward(int thisStage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void linkToNextStage(int thisStage, String eventFamily, int thisMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void linkPortalToScript(int thisStage, String portalName, String scriptName, int thisMapId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void gridInsert(Character chr, int newStatus)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void gridRemove(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int gridCheck(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int gridSize()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void gridClear()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean activatedAllReactorsOnMap(int mapId, int minReactorId, int maxReactorId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean activatedAllReactorsOnMap(MapleMap map, int minReactorId, int maxReactorId)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/event/EventManager.java`

- `class EventManager`：领域类型或功能模块，职责由同名文件实现定义。
- `class EventManagerTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventManager(Channel cserv, Invocable iv, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isDisposed()`：进行条件判定并返回布尔结果。
  - `public void cancel()`：进行条件判定并返回布尔结果。
  - `private List<Integer> convertToIntegerList(List<Object> objects)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getLobbyDelay()`：读取并返回状态/数据。
  - `private int getMaxLobbies()`：读取并返回状态/数据。
  - `public EventScheduledFuture schedule(String methodName, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public EventScheduledFuture schedule(final String methodName, final EventInstanceManager eim, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public EventScheduledFuture scheduleAtTimestamp(final String methodName, long timestamp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public World getWorldServer()`：读取并返回状态/数据。
  - `public Channel getChannelServer()`：读取并返回状态/数据。
  - `public Invocable getIv()`：读取并返回状态/数据。
  - `public EventInstanceManager getInstance(String name)`：读取并返回状态/数据。
  - `public Collection<EventInstanceManager> getInstances()`：读取并返回状态/数据。
  - `public EventInstanceManager newInstance(String name) throws EventInstanceInProgressException`：创建对象、会话或业务记录。
  - `public Marriage newMarriage(String name) throws EventInstanceInProgressException`：创建对象、会话或业务记录。
  - `public void disposeInstance(final String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setProperty(String key, String value)`：写入或更新状态字段。
  - `public void setIntProperty(String key, int value)`：写入或更新状态字段。
  - `public void setProperty(String key, int value)`：写入或更新状态字段。
  - `public String getProperty(String key)`：读取并返回状态/数据。
  - `public int getIntProperty(String key)`：读取并返回状态/数据。
  - `private void setLockLobby(int lobbyId, boolean lock)`：写入或更新状态字段。
  - `private boolean startLobbyInstance(int lobbyId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void freeLobbyInstance(String lobbyName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `private int availableLobbyInstance()`：通用业务逻辑入口，需结合实现查看细节。
  - `private String getInternalScriptExceptionMessage(Throwable a)`：读取并返回状态/数据。
  - `private EventInstanceManager createInstance(String name, Object... args) throws ScriptException, NoSuchMethodException`：创建对象、会话或业务记录。
  - `private void registerEventInstance(String eventName, int lobbyId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(Expedition exped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Expedition exped)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Expedition exped, Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Character chr, Character leader, int difficulty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(Party party, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Party party, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Party party, MapleMap map, Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(Party party, MapleMap map, int difficulty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Party party, MapleMap map, int difficulty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, Party party, MapleMap map, int difficulty, Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(EventInstanceManager eim, String ldr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(EventInstanceManager eim, Character ldr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, EventInstanceManager eim, String ldr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startInstance(int lobbyId, EventInstanceManager eim, String ldr, Character leader)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PartyCharacter> getEligibleParty(Party party)`：读取并返回状态/数据。
  - `public void clearPQ(EventInstanceManager eim)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearPQ(EventInstanceManager eim, MapleMap toMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getEventTimeout()`：读取并返回状态/数据。
  - `public boolean isNobodyInPQ()`：进行条件判定并返回布尔结果。
  - `public Monster getMonster(int mid)`：读取并返回状态/数据。
  - `private void exportReadyGuild(Integer guildId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void exportMovedQueueToGuild(Integer guildId, int place)`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<Integer> getNextGuildQueue()`：读取并返回状态/数据。
  - `public boolean isQueueFull()`：进行条件判定并返回布尔结果。
  - `public int getQueueSize()`：读取并返回状态/数据。
  - `public byte addGuildToQueue(Integer guildId, Integer leaderId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean attemptStartGuildInstance()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startQuest(Character chr, int id, int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void completeQuest(Character chr, int id, int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getTransportationTime(int travelTime)`：读取并返回状态/数据。
  - `public int getBossTime(int BossTime)`：读取并返回状态/数据。
  - `private void fillEimQueue()`：通用业务逻辑入口，需结合实现查看细节。
  - `private EventInstanceManager getReadyInstance()`：读取并返回状态/数据。
  - `private void instantiateQueuedInstance()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/event/EventScheduledFuture.java`

- `class EventScheduledFuture`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventScheduledFuture(Runnable r, EventScriptScheduler ess)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancel(boolean dummy)`：进行条件判定并返回布尔结果。

## `scripting/event/EventScriptManager.java`

- `class EventScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EventScriptManager(final Channel channel, String[] scripts)`：通用业务逻辑入口，需结合实现查看细节。
  - `public EventManager getEventManager(String event)`：读取并返回状态/数据。
  - `public boolean isActive()`：进行条件判定并返回布尔结果。
  - `public final void init()`：初始化模块、资源或运行时状态。
  - `private void reloadScripts()`：通用业务逻辑入口，需结合实现查看细节。
  - `private EventEntry initializeEventEntry(String script, Channel channel)`：初始化模块、资源或运行时状态。
  - `public void reload()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancel()`：进行条件判定并返回布尔结果。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/event/scheduler/EventScriptScheduler.java`

- `class EventScriptScheduler`：领域类型或功能模块，职责由同名文件实现定义。
  - `private void runBaseSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerEntry(final Runnable scheduledAction, final long duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelEntry(final Runnable scheduledAction)`：进行条件判定并返回布尔结果。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/item/ItemScriptManager.java`

- `class ItemScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static ItemScriptManager getInstance()`：读取并返回状态/数据。
  - `public void runItemScript(Client c, ScriptedItem scriptItem)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/item/ItemScriptMethods.java`

- `class ItemScriptMethods`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ItemScriptMethods(Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/map/MapScriptManager.java`

- `class MapScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static MapScriptManager getInstance()`：读取并返回状态/数据。
  - `public void reloadScripts()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean runMapScript(Client c, String mapScriptPath, boolean firstUser)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/map/MapScriptMethods.java`

- `class MapScriptMethods`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapScriptMethods(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void displayCygnusIntro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void displayAranIntro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startExplorerExperience()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void goAdventure()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void goLith()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void explorerQuest(short questid, String questName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void touchTheSky()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/npc/NPCConversationManager.java`

- `class NPCConversationManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `private String getDefaultTalk(int npcid)`：读取并返回状态/数据。
  - `public NPCConversationManager(Client c, int npc, String scriptName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public NPCConversationManager(Client c, int npc, List<PartyCharacter> otherParty, boolean test)`：通用业务逻辑入口，需结合实现查看细节。
  - `public NPCConversationManager(Client c, int npc, int oid, String scriptName, boolean itemScript)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getNpc()`：读取并返回状态/数据。
  - `public int getNpcObjectId()`：读取并返回状态/数据。
  - `public String getScriptName()`：读取并返回状态/数据。
  - `public boolean isItemScript()`：进行条件判定并返回布尔结果。
  - `public void resetItemScript()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendNext(String text)`：向外发送响应、消息或网络包。
  - `public void sendPrev(String text)`：向外发送响应、消息或网络包。
  - `public void sendNextPrev(String text)`：向外发送响应、消息或网络包。
  - `public void sendOk(String text)`：向外发送响应、消息或网络包。
  - `public void sendDefault()`：向外发送响应、消息或网络包。
  - `public void sendYesNo(String text)`：向外发送响应、消息或网络包。
  - `public void sendAcceptDecline(String text)`：向外发送响应、消息或网络包。
  - `public void sendSimple(String text)`：向外发送响应、消息或网络包。
  - `public void sendNext(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendPrev(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendNextPrev(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendOk(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendYesNo(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendAcceptDecline(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendSimple(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendStyle(String text, int[] styles)`：向外发送响应、消息或网络包。
  - `public void sendGetNumber(String text, int def, int min, int max)`：向外发送响应、消息或网络包。
  - `public void sendGetText(String text)`：向外发送响应、消息或网络包。
  - `public void sendGetNumber(String text, int def, int min, int max,byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendGetText(String text,byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendDimensionalMirror(String text)`：向外发送响应、消息或网络包。
  - `public void setGetText(String text)`：写入或更新状态字段。
  - `public String getText()`：读取并返回状态/数据。
  - `public boolean forceStartQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceCompleteQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(short id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(short id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean startQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean completeQuest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMeso()`：读取并返回状态/数据。
  - `public void gainMeso(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainMeso(Double gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void showEffect(String effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setHair(int hair)`：写入或更新状态字段。
  - `public void setFace(int face)`：写入或更新状态字段。
  - `public void setSkin(int color)`：写入或更新状态字段。
  - `public int itemQuantity(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void displayGuildRanks()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canSpawnPlayerNpc(int mapid)`：进行条件判定并返回布尔结果。
  - `public PlayerNPC getPlayerNPCByScriptid(int scriptId)`：读取并返回状态/数据。
  - `public Party getParty()`：读取并返回状态/数据。
  - `public void resetMap(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainTameness(int tameness)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public int getGender()`：读取并返回状态/数据。
  - `public void changeJobById(int a)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeJob(Job job)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getJobName(int id)`：读取并返回状态/数据。
  - `public StatEffect getItemEffect(int itemId)`：读取并返回状态/数据。
  - `public void resetStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void openShopNPC(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void maxMastery()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void doGachapon()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void upgradeAlliance()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void disbandAlliance(Client c, int allianceId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canBeUsedAllianceName(String name)`：进行条件判定并返回布尔结果。
  - `public Alliance createAlliance(String name)`：创建对象、会话或业务记录。
  - `public int getAllianceCapacity()`：读取并返回状态/数据。
  - `public boolean hasMerchant()`：进行条件判定并返回布尔结果。
  - `public boolean hasMerchantItems()`：进行条件判定并返回布尔结果。
  - `public void showFredrick()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int partyMembersInMap()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Event getEvent()`：读取并返回状态/数据。
  - `public void divideTeams()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getMapleCharacter(String player)`：读取并返回状态/数据。
  - `public void logLeaf(String prize)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean createPyramid(String mode, boolean party)`：创建对象、会话或业务记录。
  - `public boolean itemExists(int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCosmeticItem(int itemid)`：读取并返回状态/数据。
  - `private int getEquippedCosmeticid(int itemid)`：读取并返回状态/数据。
  - `public boolean isCosmeticEquipped(int itemid)`：进行条件判定并返回布尔结果。
  - `public boolean isUsingOldPqNpcStyle()`：进行条件判定并返回布尔结果。
  - `public Object[] getAvailableMasteryBooks()`：读取并返回状态/数据。
  - `public Object[] getAvailableSkillBooks()`：读取并返回状态/数据。
  - `public Object[] getNamesWhoDropsItem(Integer itemId)`：读取并返回状态/数据。
  - `public String getSkillBookInfo(int itemid)`：读取并返回状态/数据。
  - `public int cpqCalcAvgLvl(int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean sendCPQMapLists()`：向外发送响应、消息或网络包。
  - `public boolean fieldTaken(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean fieldLobbied(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cpqLobby(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getChrById(int id)`：读取并返回状态/数据。
  - `public void cancelCPQLobby()`：进行条件判定并返回布尔结果。
  - `private void warpoutCPQLobby(MapleMap lobbyMap)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int isCPQParty(MapleMap lobby, Party party)`：进行条件判定并返回布尔结果。
  - `private int canStartCPQ(MapleMap lobby, Party party, Party challenger)`：进行条件判定并返回布尔结果。
  - `public void startCPQ(final Character challenger, final int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startCPQ2(final Character challenger, final int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean sendCPQMapLists2()`：向外发送响应、消息或网络包。
  - `public boolean fieldTaken2(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean fieldLobbied2(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cpqLobby2(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mapClock(int time)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean sendCPQChallenge(String cpqType, int leaderid)`：向外发送响应、消息或网络包。
  - `public void answerCPQChallenge(boolean accept)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void challengeParty2(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void challengeParty(int field)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized boolean setupAriantBattle(Expedition exped, int mapid)`：写入或更新状态字段。
  - `public String startAriantBattle(ExpeditionType expedType, int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendMarriageWishlist(boolean groom)`：向外发送响应、消息或网络包。
  - `public void sendMarriageGifts(List<Item> gifts)`：向外发送响应、消息或网络包。
  - `public boolean createMarriageWishlist()`：创建对象、会话或业务记录。
  - `public void sendNextLevel(String nextLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendLastLevel(String lastLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendLastNextLevel(String lastLevel, String nextLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendOkLevel(String nextLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendSelectLevel(String text)`：向外发送响应、消息或网络包。
  - `public void sendSelectLevel(String prefix, String text)`：向外发送响应、消息或网络包。
  - `public void sendNextSelectLevel(String nextLevel, String text)`：向外发送响应、消息或网络包。
  - `public void getInputNumberLevel(String nextLevel, String text, int def, int min, int max)`：读取并返回状态/数据。
  - `public void getInputTextLevel(String nextLevel, String text)`：读取并返回状态/数据。
  - `public void sendAcceptDeclineLevel(String decLineLevel, String acceptLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendYesNoLevel(String noLevel, String yesLevel, String text)`：向外发送响应、消息或网络包。
  - `public void sendNextLevel(String nextLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendLastLevel(String lastLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendLastNextLevel(String lastLevel, String nextLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendOkLevel(String nextLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendSelectLevel(String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendSelectLevel(String prefix, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendNextSelectLevel(String nextLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void getPnpcInputNumberLevel(String nextLevel, String text, int def, int min, int max, byte speaker)`：读取并返回状态/数据。
  - `public void getPnpcInputTextLevel(String nextLevel, String text, byte speaker)`：读取并返回状态/数据。
  - `public void sendAcceptDeclineLevel(String decLineLevel, String acceptLevel, String text, byte speaker)`：向外发送响应、消息或网络包。
  - `public void sendYesNoLevel(String noLevel, String yesLevel, String text, byte speaker)`：向外发送响应、消息或网络包。

## `scripting/npc/NPCScriptManager.java`

- `class NPCScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static NPCScriptManager getInstance()`：读取并返回状态/数据。
  - `public boolean isNpcScriptAvailable(Client c, String fileName)`：进行条件判定并返回布尔结果。
  - `public boolean start(Client c, int npc, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean start(Client c, int npc, int oid, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean start(Client c, int npc, String fileName, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean start(Client c, int npc, int oid, String fileName, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean start(Client c, ScriptedItem scriptItem, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void start(String filename, Client c, int npc, List<PartyCharacter> chrs)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean start(Client c, int npc, int oid, String fileName, Character chr, boolean itemScript, String engineName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void action(Client c, byte mode, byte type, int selection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void nextLevel(Client c, byte mode, byte type, int selection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(NPCConversationManager cm)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(Client c, boolean action)`：通用业务逻辑入口，需结合实现查看细节。
  - `public NPCConversationManager getCM(Client c)`：读取并返回状态/数据。

## `scripting/portal/PortalPlayerInteraction.java`

- `class PortalPlayerInteraction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PortalPlayerInteraction(Client c, Portal portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Portal getPortal()`：读取并返回状态/数据。
  - `public void runMapScript()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasLevel30Character()`：进行条件判定并返回布尔结果。
  - `public void blockPortal()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unblockPortal()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playPortalSound()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/portal/PortalScript.java`

- `interface PortalScript`：领域类型或功能模块，职责由同名文件实现定义。
  - `boolean enter(PortalPlayerInteraction ppi)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/portal/PortalScriptManager.java`

- `class PortalScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static PortalScriptManager getInstance()`：读取并返回状态/数据。
  - `private PortalScript getPortalScript(String scriptName) throws ScriptException`：读取并返回状态/数据。
  - `public boolean executePortalScript(Portal portal, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reloadPortalScripts()`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/quest/QuestActionManager.java`

- `class QuestActionManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public QuestActionManager(Client c, int quest, int npc, boolean start)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getQuest()`：读取并返回状态/数据。
  - `public boolean isStart()`：进行条件判定并返回布尔结果。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceStartQuest()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceCompleteQuest()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startQuest()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void completeQuest()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainExp(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainMeso(int gain)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getMedalName()`：读取并返回状态/数据。

## `scripting/quest/QuestScriptManager.java`

- `class QuestScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static QuestScriptManager getInstance()`：读取并返回状态/数据。
  - `private ScriptEngine getQuestScriptEngine(Client c, short questid)`：读取并返回状态/数据。
  - `public void start(Client c, short questid, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void start(Client c, byte mode, byte type, int selection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void end(Client c, short questid, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void end(Client c, byte mode, byte type, int selection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void raiseOpen(Client c, short questid, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(QuestActionManager qm, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public QuestActionManager getQM(Client c)`：读取并返回状态/数据。
  - `public void reloadQuestScripts()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean checkFunctionExists(Client c, short questid, int npc, String functionName)`：校验输入参数或业务约束。

## `scripting/reactor/ReactorActionManager.java`

- `class ReactorActionManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ReactorActionManager(Client c, Reactor reactor, Invocable iv)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hitReactor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void destroyNpc(int npcId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void sortDropEntries(List<ReactorDropEntry> from, List<ReactorDropEntry> item, List<ReactorDropEntry> visibleQuest, List<ReactorDropEntry> otherQuest, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static List<ReactorDropEntry> assembleReactorDropEntries(Character chr, List<ReactorDropEntry> items)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sprayItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sprayItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItems(boolean delayed, int posX, int posY, boolean meso, int mesoChance, final int minMeso, final int maxMeso, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<ReactorDropEntry> getDropChances()`：读取并返回状态/数据。
  - `private List<ReactorDropEntry> generateDropList(List<ReactorDropEntry> drops, float dropRate, boolean meso, int mesoChance, int minItems)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void createMapMonitor(int mapId, String portal)`：创建对象、会话或业务记录。
  - `public void spawnMonster(int id, int qty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(int id, int qty, int x, int y)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(int id, int qty, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killMonster(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killMonster(int id, boolean withDrops)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public void spawnNpc(int npcId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnNpc(int npcId, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Reactor getReactor()`：读取并返回状态/数据。
  - `public void spawnFakeMonster(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void summonBossDelayed(final int mobId, final int delayMs, final int x, final int y, final String bgm, final String summonMessage)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void summonBoss(int mobId, int x, int y, String bgmName, String summonMessage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispelAllMonsters(int num, int team)`：通用业务逻辑入口，需结合实现查看细节。

## `scripting/reactor/ReactorScriptManager.java`

- `class ReactorScriptManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static ReactorScriptManager getInstance()`：读取并返回状态/数据。
  - `public void onHit(Client c, Reactor reactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void act(Client c, Reactor reactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<ReactorDropEntry> getDrops(int reactorId)`：读取并返回状态/数据。
  - `public void clearDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void touch(Client c, Reactor reactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void untouch(Client c, Reactor reactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void touching(Client c, Reactor reactor, boolean touching)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Invocable initializeInvocable(Client c, Reactor reactor)`：初始化模块、资源或运行时状态。

## `server/CashShop.java`

- `class CashShop`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CashShop(int accountId, int characterId, int jobType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public record CashShopSurpriseResult(Item usedCashShopSurprise, Item reward)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCash(int type)`：读取并返回状态/数据。
  - `public void gainCash(int type, int cash)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gainCash(int type, ModifiedCashItemDO buyItem, int world)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isOpened()`：进行条件判定并返回布尔结果。
  - `public void open(boolean b)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Item> getInventory()`：读取并返回状态/数据。
  - `public Item findByCashId(int cashId)`：查询并返回匹配集合或单项结果。
  - `public boolean addToInventory(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canAddToInventory(int itemCount)`：进行条件判定并返回布尔结果。
  - `public int getInventoryLimit()`：读取并返回状态/数据。
  - `public int getInventorySize()`：读取并返回状态/数据。
  - `public void removeFromInventory(Item item)`：删除对象、关系或临时状态。
  - `public List<Integer> getWishList()`：读取并返回状态/数据。
  - `public void clearWishList()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addToWishList(int sn)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gift(int recipient, String from, String message, int sn)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void gift(int recipient, String from, String message, int sn, int ringid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getAvailableNotes()`：读取并返回状态/数据。
  - `public void decreaseNotes()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void save(Connection con) throws SQLException`：持久化当前状态到存储层。
  - `public Optional<CashShopSurpriseResult> openCashShopSurprise(long cashId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Optional<Item> getItemByCashId(long cashId)`：读取并返回状态/数据。
  - `public int getItemsSize()`：读取并返回状态/数据。
  - `private void trimToSafeInventoryLimit()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Item generateCouponItem(int itemId, short quantity)`：通用业务逻辑入口，需结合实现查看细节。

## `server/ChatLogger.java`

- `class ChatLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void log(Client c, String chatType, String message)`：通用业务逻辑入口，需结合实现查看细节。

## `server/CommonInformation.java`

- `class CommonInformation`：领域类型或功能模块，职责由同名文件实现定义。
  - `private CommonInformation()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static CommonInformation getInstance()`：读取并返回状态/数据。
  - `public List<InformationResult> getStringInformation(InformationSearch condition)`：读取并返回状态/数据。
  - `private void searchXML(List<InformationResult> results, InformationType infType, String filter, int filterType, boolean fullMatch)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addResult(List<InformationResult> results, InformationType infType, Data data, String filter, int filterType, boolean fullMatch)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addMapResult(List<InformationResult> results, InformationType infType, Data data, String filter, int filterType, boolean fullMatch)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isMatch(String id, String name, String filter, int filterType, boolean fullMatch)`：进行条件判定并返回布尔结果。

## `server/DueyPackage.java`

- `class DueyPackage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public DueyPackage(int pId, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public DueyPackage(int pId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getSender()`：读取并返回状态/数据。
  - `public void setSender(String name)`：写入或更新状态字段。
  - `public Item getItem()`：读取并返回状态/数据。
  - `public int getMesos()`：读取并返回状态/数据。
  - `public void setMesos(int set)`：写入或更新状态字段。
  - `public String getMessage()`：读取并返回状态/数据。
  - `public void setMessage(String m)`：写入或更新状态字段。
  - `public int getPackageId()`：读取并返回状态/数据。
  - `public Integer getReceiverId()`：读取并返回状态/数据。
  - `public void setReceiverId(Integer receiverId)`：写入或更新状态字段。
  - `public long sentTimeInMilliseconds()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isDeliveringTime()`：进行条件判定并返回布尔结果。
  - `public void setSentTime(Timestamp ts, boolean quick)`：写入或更新状态字段。

## `server/ExpLogger.java`

- `class ExpLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public record ExpLogRecord(float worldExpRate, int expCoupon, long gainedExp, int currentExp,Timestamp expGainTime, int charid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void putExpLogRecord(ExpLogRecord expLogRecord)`：通用业务逻辑入口，需结合实现查看细节。

## `server/ItemInformationProvider.java`

- `class ItemInformationProvider`：领域类型或功能模块，职责由同名文件实现定义。
- `class ScriptedItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static ItemInformationProvider getInstance()`：读取并返回状态/数据。
  - `private ItemInformationProvider()`：通用业务逻辑入口，需结合实现查看细节。
  - `private Data getStringData(int itemId)`：读取并返回状态/数据。
  - `public boolean noCancelMouse(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Data getItemData(int itemId)`：读取并返回状态/数据。
  - `public List<Integer> getItemIdsInRange(int minId, int maxId, boolean ignoreCashItem)`：读取并返回状态/数据。
  - `private static short getExtraSlotMaxFromPlayer(Client c, int itemId)`：读取并返回状态/数据。
  - `public short getSlotMax(Client c, int itemId)`：读取并返回状态/数据。
  - `public int getMeso(int itemId)`：读取并返回状态/数据。
  - `private static double getRoundedUnitPrice(double unitPrice, int max)`：读取并返回状态/数据。
  - `public int getWholePrice(int itemId)`：读取并返回状态/数据。
  - `public double getUnitPrice(int itemId)`：读取并返回状态/数据。
  - `public int getPrice(int itemId, int quantity)`：读取并返回状态/数据。
  - `protected String getEquipmentSlot(int itemId)`：读取并返回状态/数据。
  - `public Integer getEquipLevelReq(int itemId)`：读取并返回状态/数据。
  - `public List<Integer> getScrollReqs(int itemId)`：读取并返回状态/数据。
  - `public WeaponType getWeaponType(int itemId)`：读取并返回状态/数据。
  - `private static double testYourLuck(double prop, int dices)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean rollSuccessChance(double propPercent)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static short getMaximumShortMaxIfOverflow(int value1, int value2)`：读取并返回状态/数据。
  - `private static short getShortMaxIfOverflow(int value)`：读取并返回状态/数据。
  - `private static short chscrollRandomizedStat(int range)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void scrollOptionEquipWithChaos(Equip nEquip, int range, boolean option)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void scrollEquipWithChaos(Equip nEquip, int range)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canUseCleanSlate(Equip equip)`：进行条件判定并返回布尔结果。
  - `public Item scrollEquipWithId(Item equip, int scrollId, boolean usingWhiteScroll, int vegaItemId, boolean isGM)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void improveEquipStats(Equip nEquip, Map<String, Integer> stats)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item getEquipById(int equipId)`：读取并返回状态/数据。
  - `private Item getEquipById(int equipId, int ringId)`：读取并返回状态/数据。
  - `private static short getRandStat(short defaultValue, int maxRange)`：读取并返回状态/数据。
  - `public Equip randomizeStats(Equip equip)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static short getRandUpgradedStat(short defaultValue, int maxRange)`：读取并返回状态/数据。
  - `public Equip randomizeUpgradeStats(Equip equip)`：通用业务逻辑入口，需结合实现查看细节。
  - `public StatEffect getItemEffect(int itemId)`：读取并返回状态/数据。
  - `public int[][] getSummonMobs(int itemId)`：读取并返回状态/数据。
  - `public int getWatkForProjectile(int itemId)`：读取并返回状态/数据。
  - `public String getName(int itemId)`：读取并返回状态/数据。
  - `public String getMsg(int itemId)`：读取并返回状态/数据。
  - `public boolean isUntradeableRestricted(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isAccountRestricted(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isLootRestricted(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isDropRestricted(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isPickupRestricted(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isQuestItem(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isPartyQuestItem(int itemId)`：进行条件判定并返回布尔结果。
  - `private void loadCardIdData()`：从外部来源加载数据（数据库/文件/配置）。
  - `public int getCardMobId(int id)`：读取并返回状态/数据。
  - `public boolean isUntradeableOnEquip(int itemId)`：进行条件判定并返回布尔结果。
  - `public ScriptedItem getScriptedItemInfo(int itemId)`：读取并返回状态/数据。
  - `public boolean isKarmaAble(int itemId)`：进行条件判定并返回布尔结果。
  - `public int getStateChangeItem(int itemId)`：读取并返回状态/数据。
  - `public int getCreateItem(int itemId)`：读取并返回状态/数据。
  - `public int getMobItem(int itemId)`：读取并返回状态/数据。
  - `public int getUseDelay(int itemId)`：读取并返回状态/数据。
  - `public int getMobHP(int itemId)`：读取并返回状态/数据。
  - `public int getExpById(int itemId)`：读取并返回状态/数据。
  - `public int getMaxLevelById(int itemId)`：读取并返回状态/数据。
  - `public boolean isConsumeOnPickup(int itemId)`：进行条件判定并返回布尔结果。
  - `public final boolean isTwoHanded(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isCash(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isUpgradeable(int itemId)`：进行条件判定并返回布尔结果。
  - `public boolean isUnmerchable(int itemId)`：进行条件判定并返回布尔结果。
  - `public Collection<Item> canWearEquipment(Character chr, Collection<Item> items)`：进行条件判定并返回布尔结果。
  - `public boolean canWearEquipment(Character chr, Equip equip, int dst)`：进行条件判定并返回布尔结果。
  - `private Data getEquipLevelInfo(int itemId)`：读取并返回状态/数据。
  - `public int getEquipLevel(int itemId, boolean getMaxLevel)`：读取并返回状态/数据。
  - `private static int getCrystalForLevel(int level)`：读取并返回状态/数据。
  - `public int getMakerCrystalFromLeftover(Integer leftoverId)`：读取并返回状态/数据。
  - `public MakerItemCreateEntry getMakerItemEntry(int toCreate)`：读取并返回状态/数据。
  - `public int getMakerCrystalFromEquip(Integer equipId)`：读取并返回状态/数据。
  - `public int getMakerStimulantFromEquip(Integer equipId)`：读取并返回状态/数据。
  - `public int getMakerDisassembledFee(Integer itemId)`：读取并返回状态/数据。
  - `public int getMakerStimulant(int itemId)`：读取并返回状态/数据。
  - `public Set<String> getWhoDrops(Integer itemId)`：读取并返回状态/数据。
  - `private boolean canUseSkillBook(Character player, Integer skillBookId)`：进行条件判定并返回布尔结果。
  - `public List<Integer> usableMasteryBooks(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Integer> usableSkillBooks(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final QuestConsItem getQuestConsumablesInfo(final int itemId)`：读取并返回状态/数据。
  - `public final ItemCashInfo getItemCashInfo(int itemId)`：读取并返回状态/数据。

## `server/MTSItemInfo.java`

- `class MTSItemInfo`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MTSItemInfo(Item item, int price, int id, int cid, String seller, String date)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Item getItem()`：读取并返回状态/数据。
  - `public int getPrice()`：读取并返回状态/数据。
  - `public int getTaxes()`：读取并返回状态/数据。
  - `public int getID()`：读取并返回状态/数据。
  - `public long getEndingDate()`：读取并返回状态/数据。
  - `public String getSeller()`：读取并返回状态/数据。

## `server/MakerItemFactory.java`

- `class MakerItemFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static MakerItemCreateEntry getItemCreateEntry(int toCreate, int stimulantid, Map<Integer, Short> reagentids)`：读取并返回状态/数据。
  - `public static MakerItemCreateEntry generateLeftoverCrystalEntry(int fromLeftoverid, int crystalId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static MakerItemCreateEntry generateDisassemblyCrystalEntry(int fromEquipid, int cost, List<Pair<Integer, Integer>> gains)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static double getMakerStimulantFee(int itemid)`：读取并返回状态/数据。
  - `private static double getMakerReagentFee(int itemid, int reagentLevel)`：读取并返回状态/数据。

## `server/MapleLeafLogger.java`

- `class MapleLeafLogger`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void log(Character player, boolean gotPrize, String operation)`：通用业务逻辑入口，需结合实现查看细节。

## `server/Marriage.java`

- `class Marriage`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Marriage(EventManager em, String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean giftItemToSpouse(int cid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<String> getWishlistItems(boolean groom)`：读取并返回状态/数据。
  - `public void initializeGiftItems()`：初始化模块、资源或运行时状态。
  - `public List<Item> getGiftItems(Client c, boolean groom)`：读取并返回状态/数据。
  - `private List<Item> getGiftItemsList(boolean groom)`：读取并返回状态/数据。
  - `public Item getGiftItem(Client c, boolean groom, int idx)`：读取并返回状态/数据。
  - `public void addGiftItem(boolean groom, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeGiftItem(boolean groom, Item item)`：删除对象、关系或临时状态。
  - `public Boolean isMarriageGroom(Character chr)`：进行条件判定并返回布尔结果。
  - `public static boolean claimGiftItems(Client c, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static List<Item> loadGiftItemsFromDb(Client c, int cid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void saveGiftItemsToDb(Client c, boolean groom, int cid)`：持久化当前状态到存储层。
  - `public static void saveGiftItemsToDb(Client c, List<Item> giftItems, int cid)`：持久化当前状态到存储层。

## `server/Shop.java`

- `class Shop`：领域类型或功能模块，职责由同名文件实现定义。
  - `private Shop(int id, int npcId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void addItem(ShopItem item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendShop(Client c)`：向外发送响应、消息或网络包。
  - `public void buy(Client c, short slot, int itemId, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean canSell(Item item, short quantity)`：进行条件判定并返回布尔结果。
  - `private static short getSellingQuantity(Item item, short quantity)`：读取并返回状态/数据。
  - `public void sell(Client c, InventoryType type, short slot, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void recharge(Client c, short slot)`：通用业务逻辑入口，需结合实现查看细节。
  - `private ShopItem findBySlot(short slot)`：查询并返回匹配集合或单项结果。
  - `public static Shop createFromDB(int id, boolean isShopId)`：创建对象、会话或业务记录。
  - `public int getNpcId()`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。

## `server/ShopFactory.java`

- `class ShopFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static ShopFactory getInstance()`：读取并返回状态/数据。
  - `private Shop loadShop(int id, boolean isShopId)`：从外部来源加载数据（数据库/文件/配置）。
  - `public Shop getShop(int shopId)`：读取并返回状态/数据。
  - `public Shop getShopForNPC(int npcId)`：读取并返回状态/数据。
  - `public void reloadShops()`：通用业务逻辑入口，需结合实现查看细节。

## `server/ShopItem.java`

- `class ShopItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ShopItem(short buyable, int itemId, int price, int pitch)`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getBuyable()`：读取并返回状态/数据。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public int getPrice()`：读取并返回状态/数据。
  - `public int getPitch()`：读取并返回状态/数据。

## `server/SkillbookInformationProvider.java`

- `class SkillbookInformationProvider`：领域类型或功能模块，职责由同名文件实现定义。
- `enum SkillBookEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void loadAllSkillbookInformation()`：从外部来源加载数据（数据库/文件/配置）。
  - `private static boolean is4thJobSkill(int itemid)`：进行条件判定并返回布尔结果。
  - `private static boolean isSkillBook(int itemid)`：进行条件判定并返回布尔结果。
  - `private static boolean isQuestBook(int itemid)`：进行条件判定并返回布尔结果。
  - `private static int fetchQuestbook(Data checkData, String quest)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void listFiles(String directoryName, ArrayList<Path> files)`：查询并返回匹配集合或单项结果。
  - `private static List<Path> listFilesFromDirectoryRecursively(String directory)`：查询并返回匹配集合或单项结果。
  - `private static Set<Integer> findMatchingSkillbookIdsOnFile(String fileContent)`：查询并返回匹配集合或单项结果。
  - `private static String readFileToString(Path file, String encoding) throws IOException`：通用业务逻辑入口，需结合实现查看细节。
  - `public static SkillBookEntry getSkillbookAvailability(int itemId)`：读取并返回状态/数据。
  - `public static List<Integer> getTeachableSkills(Character chr)`：读取并返回状态/数据。

## `server/StatEffect.java`

- `class StatEffect`：领域类型或功能模块，职责由同名文件实现定义。
  - `private boolean isEffectActive(int mapid, boolean partyHunting)`：进行条件判定并返回布尔结果。
  - `public boolean isActive(Character applyto)`：进行条件判定并返回布尔结果。
  - `public int getCardRate(int mapid, int itemid)`：读取并返回状态/数据。
  - `public static StatEffect loadSkillEffectFromData(Data source, int skillid, boolean overtime)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static StatEffect loadItemEffectFromData(Data source, int itemid)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static void addBuffStatPairToListIfNotZero(List<Pair<BuffStat, Integer>> list, BuffStat buffstat, Integer val)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static byte mapProtection(int sourceid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static StatEffect loadFromData(Data source, int sourceid, boolean skill, boolean overTime)`：从外部来源加载数据（数据库/文件/配置）。
  - `public void applyPassive(Character applyto, MapObject obj, int attack)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyEchoOfHero(Character applyfrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyTo(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyTo(Character chr, boolean useMaxRange)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyTo(Character chr, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean applyTo(Character applyfrom, Character applyto, boolean primary, Point pos, boolean useMaxRange, int affectedPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int applyBuff(Character applyfrom, boolean useMaxRange)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applyMonsterBuff(Character applyfrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasBoundingBox()`：进行条件判定并返回布尔结果。
  - `public Rectangle calculateBoundingBox(Point posFrom, boolean facingLeft)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getBuffLocalDuration()`：读取并返回状态/数据。
  - `public void silentApplyBuff(Character chr, long localStartTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void applyComboBuff(final Character applyto, int combo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void applyBeaconBuff(final Character applyto, int objectid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateBuffEffect(Character target, List<Pair<BuffStat, Integer>> activeStats, long starttime)`：更新已有对象/配置/缓存。
  - `private void applyBuffEffect(Character applyfrom, Character applyto, boolean primary)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int calcHPChange(Character applyfrom, boolean primary, int affectedPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int makeHealHP(double rate, double stat, double lowerfactor, double upperfactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int calcMPChange(Character applyfrom, boolean primary)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int alchemistModifyVal(Character chr, int val, boolean withX)`：通用业务逻辑入口，需结合实现查看细节。
  - `private StatEffect getAlchemistEffect(Character chr)`：读取并返回状态/数据。
  - `private boolean isGmBuff()`：进行条件判定并返回布尔结果。
  - `private boolean isMonsterBuff()`：进行条件判定并返回布尔结果。
  - `private boolean isPartyBuff()`：进行条件判定并返回布尔结果。
  - `private boolean isHeal()`：进行条件判定并返回布尔结果。
  - `private boolean isResurrection()`：进行条件判定并返回布尔结果。
  - `private boolean isTimeLeap()`：进行条件判定并返回布尔结果。
  - `public boolean isDragonBlood()`：进行条件判定并返回布尔结果。
  - `public boolean isBerserk()`：进行条件判定并返回布尔结果。
  - `public boolean isRecovery()`：进行条件判定并返回布尔结果。
  - `public boolean isMapChair()`：进行条件判定并返回布尔结果。
  - `public static boolean isMapChair(int sourceid)`：进行条件判定并返回布尔结果。
  - `public static boolean isHpMpRecovery(int sourceid)`：进行条件判定并返回布尔结果。
  - `public static boolean isAriantShield(int sourceid)`：进行条件判定并返回布尔结果。
  - `private boolean isDs()`：进行条件判定并返回布尔结果。
  - `private boolean isWw()`：进行条件判定并返回布尔结果。
  - `private boolean isCombo()`：进行条件判定并返回布尔结果。
  - `private boolean isEnrage()`：进行条件判定并返回布尔结果。
  - `public boolean isBeholder()`：进行条件判定并返回布尔结果。
  - `private boolean isShadowPartner()`：进行条件判定并返回布尔结果。
  - `private boolean isChakra()`：进行条件判定并返回布尔结果。
  - `private boolean isCouponBuff()`：进行条件判定并返回布尔结果。
  - `private boolean isAriantShield()`：进行条件判定并返回布尔结果。
  - `private boolean isMysticDoor()`：进行条件判定并返回布尔结果。
  - `public boolean isMonsterRiding()`：进行条件判定并返回布尔结果。
  - `public boolean isMagicDoor()`：进行条件判定并返回布尔结果。
  - `public boolean isPoison()`：进行条件判定并返回布尔结果。
  - `public boolean isMorph()`：进行条件判定并返回布尔结果。
  - `public boolean isMorphWithoutAttack()`：进行条件判定并返回布尔结果。
  - `private boolean isMist()`：进行条件判定并返回布尔结果。
  - `private boolean isSoulArrow()`：进行条件判定并返回布尔结果。
  - `private boolean isShadowClaw()`：进行条件判定并返回布尔结果。
  - `private boolean isCrash()`：进行条件判定并返回布尔结果。
  - `private boolean isSeal()`：进行条件判定并返回布尔结果。
  - `private boolean isDispel()`：进行条件判定并返回布尔结果。
  - `private boolean isCureAllAbnormalStatus()`：进行条件判定并返回布尔结果。
  - `public static boolean isHerosWill(int skillid)`：进行条件判定并返回布尔结果。
  - `private boolean isWkCharge()`：进行条件判定并返回布尔结果。
  - `private boolean isDash()`：进行条件判定并返回布尔结果。
  - `private boolean isSkillMorph()`：进行条件判定并返回布尔结果。
  - `private boolean isInfusion()`：进行条件判定并返回布尔结果。
  - `private boolean isCygnusFA()`：进行条件判定并返回布尔结果。
  - `private boolean isHyperBody()`：进行条件判定并返回布尔结果。
  - `private boolean isComboReset()`：进行条件判定并返回布尔结果。
  - `private int getFatigue()`：读取并返回状态/数据。
  - `private int getMorph()`：读取并返回状态/数据。
  - `private int getMorph(Character chr)`：读取并返回状态/数据。
  - `private SummonMovementType getSummonMovementType()`：读取并返回状态/数据。
  - `public boolean isSkill()`：进行条件判定并返回布尔结果。
  - `public int getSourceId()`：读取并返回状态/数据。
  - `public void setSourceId(int id)`：写入或更新状态字段。
  - `public int getBuffSourceId()`：读取并返回状态/数据。
  - `public boolean makeChanceResult()`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getHp()`：读取并返回状态/数据。
  - `public short getMp()`：读取并返回状态/数据。
  - `public double getHpRate()`：读取并返回状态/数据。
  - `public double getMpRate()`：读取并返回状态/数据。
  - `public byte getHpR()`：读取并返回状态/数据。
  - `public byte getMpR()`：读取并返回状态/数据。
  - `public short getHpRRate()`：读取并返回状态/数据。
  - `public short getMpRRate()`：读取并返回状态/数据。
  - `public short getHpCon()`：读取并返回状态/数据。
  - `public short getMpCon()`：读取并返回状态/数据。
  - `public short getMatk()`：读取并返回状态/数据。
  - `public short getWatk()`：读取并返回状态/数据。
  - `public int getDuration()`：读取并返回状态/数据。
  - `public boolean sameSource(StatEffect effect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getX()`：读取并返回状态/数据。
  - `public int getY()`：读取并返回状态/数据。
  - `public int getDamage()`：读取并返回状态/数据。
  - `public int getAttackCount()`：读取并返回状态/数据。
  - `public int getMobCount()`：读取并返回状态/数据。
  - `public int getFixDamage()`：读取并返回状态/数据。
  - `public short getBulletCount()`：读取并返回状态/数据。
  - `public short getBulletConsume()`：读取并返回状态/数据。
  - `public int getMoneyCon()`：读取并返回状态/数据。
  - `public int getCooldown()`：读取并返回状态/数据。

## `server/Storage.java`

- `class Storage`：领域类型或功能模块，职责由同名文件实现定义。
  - `private Storage(int id, byte slots, int meso)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Storage create(int id, int world) throws SQLException`：创建对象、会话或业务记录。
  - `public static Storage loadOrCreateFromDB(int id, int world)`：从外部来源加载数据（数据库/文件/配置）。
  - `public byte getSlots()`：读取并返回状态/数据。
  - `public boolean canGainSlots(int slots)`：进行条件判定并返回布尔结果。
  - `public boolean gainSlots(int slots)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void saveToDB(Connection con)`：持久化当前状态到存储层。
  - `public Item getItem(byte slot)`：读取并返回状态/数据。
  - `public boolean takeOut(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean store(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Item> getItems()`：读取并返回状态/数据。
  - `private List<Item> filterItems(InventoryType type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte getSlot(InventoryType type, byte slot)`：读取并返回状态/数据。
  - `public void sendStorage(Client c, int npcId)`：向外发送响应、消息或网络包。
  - `public void sendStored(Client c, InventoryType type)`：向外发送响应、消息或网络包。
  - `public void sendTakenOut(Client c, InventoryType type)`：向外发送响应、消息或网络包。
  - `public void arrangeItems(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMeso()`：读取并返回状态/数据。
  - `public void setMeso(int meso)`：写入或更新状态字段。
  - `public void sendMeso(Client c)`：向外发送响应、消息或网络包。
  - `public int getStoreFee()`：读取并返回状态/数据。
  - `public int getTakeOutFee()`：读取并返回状态/数据。
  - `public boolean isFull()`：进行条件判定并返回布尔结果。
  - `public void close()`：通用业务逻辑入口，需结合实现查看细节。

## `server/StorageInventory.java`

- `class StorageInventory`：领域类型或功能模块，职责由同名文件实现定义。
- `class PairedQuicksort`：领域类型或功能模块，职责由同名文件实现定义。
  - `public StorageInventory(Client c, List<Item> toSort)`：通用业务逻辑入口，需结合实现查看细节。
  - `private byte getSlotLimit()`：读取并返回状态/数据。
  - `private Collection<Item> list()`：查询并返回匹配集合或单项结果。
  - `private short addItem(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isEquipOrCash(Item item)`：进行条件判定并返回布尔结果。
  - `private static boolean isSameOwner(Item source, Item target)`：进行条件判定并返回布尔结果。
  - `private void move(short sSlot, short dSlot, short slotMax)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void moveItem(short src, short dst)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void swap(Item source, Item target)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Item getItem(short slot)`：读取并返回状态/数据。
  - `private void addSlot(short slot, Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeSlot(short slot)`：删除对象、关系或临时状态。
  - `private boolean isFull()`：进行条件判定并返回布尔结果。
  - `private short getNextFreeSlot()`：读取并返回状态/数据。
  - `public void mergeItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Item> sortItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByItemId(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByName(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByQuantity(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void PartitionByLevel(int Esq, int Dir, ArrayList<Item> A)`：通用业务逻辑入口，需结合实现查看细节。
  - `void MapleQuicksort(int Esq, int Dir, ArrayList<Item> A, int sort)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)`：通用业务逻辑入口，需结合实现查看细节。

## `server/SystemRescue.java`

- `class SystemRescue`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void setMapChange(Character player)`：写入或更新状态字段。
  - `public void showMapChangeMessage(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean dropMessage(Character player, String keyname, int type)`：通用业务逻辑入口，需结合实现查看细节。

## `server/ThreadManager.java`

- `class ThreadManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `private ThreadManager()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void newTask(Runnable r)`：创建对象、会话或业务记录。
  - `public void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stop()`：通用业务逻辑入口，需结合实现查看细节。

## `server/TimerManager.java`

- `class TimerManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `private TimerManager()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void stop()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Runnable purge()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> register(Runnable r, long repeatTime, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> register(Runnable r, long repeatTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> update(ScheduledFuture<?> sf, Runnable r, long repeatTime)`：更新已有对象/配置/缓存。
  - `public void stop(ScheduledFuture<?> sf)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> schedule(Runnable r, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> scheduleAtTimestamp(Runnable r, long timestamp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getActiveCount()`：读取并返回状态/数据。
  - `public long getCompletedTaskCount()`：读取并返回状态/数据。
  - `public int getQueuedTasks()`：读取并返回状态/数据。
  - `public long getTaskCount()`：读取并返回状态/数据。
  - `public boolean isShutdown()`：进行条件判定并返回布尔结果。
  - `public boolean isTerminated()`：进行条件判定并返回布尔结果。

## `server/TimerManagerMBean.java`

- `interface TimerManagerMBean`：领域类型或功能模块，职责由同名文件实现定义。
  - `boolean isTerminated()`：进行条件判定并返回布尔结果。
  - `boolean isShutdown()`：进行条件判定并返回布尔结果。
  - `long getCompletedTaskCount()`：读取并返回状态/数据。
  - `long getActiveCount()`：读取并返回状态/数据。
  - `long getTaskCount()`：读取并返回状态/数据。
  - `int getQueuedTasks()`：读取并返回状态/数据。

## `server/Trade.java`

- `class Trade`：领域类型或功能模块，职责由同名文件实现定义。
- `enum TradeResult`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Trade(byte number, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static int getFee(long meso)`：读取并返回状态/数据。
  - `private void lockTrade()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void fetchExchangedItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void completeTrade()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void cancel(byte result)`：进行条件判定并返回布尔结果。
  - `private boolean isLocked()`：进行条件判定并返回布尔结果。
  - `private int getMeso()`：读取并返回状态/数据。
  - `public void setMeso(int meso)`：写入或更新状态字段。
  - `public boolean addItem(Item item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void chat(String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Trade getPartner()`：读取并返回状态/数据。
  - `public void setPartner(Trade partner)`：写入或更新状态字段。
  - `public Character getChr()`：读取并返回状态/数据。
  - `public List<Item> getItems()`：读取并返回状态/数据。
  - `public int getExchangeMesos()`：读取并返回状态/数据。
  - `private boolean fitsMeso()`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean fitsInInventory()`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean fitsUniquesInInventory()`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized boolean checkTradeCompleteHandshake(boolean updateSelf)`：校验输入参数或业务约束。
  - `private boolean checkCompleteHandshake()`：校验输入参数或业务约束。
  - `public static void completeTrade(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void cancelTradeInternal(Character chr, byte selfResult, byte partnerResult)`：进行条件判定并返回布尔结果。
  - `private static byte[] tradeResultsPair(byte result)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void tradeCancelHandshake(boolean updateSelf, byte result)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void cancelHandshake(byte result)`：进行条件判定并返回布尔结果。
  - `public static void cancelTrade(Character chr, TradeResult result)`：进行条件判定并返回布尔结果。
  - `public static void startTrade(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean hasTradeInviteBack(Character c1, Character c2)`：进行条件判定并返回布尔结果。
  - `public static void inviteTrade(Character c1, Character c2)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void visitTrade(Character c1, Character c2)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void declineTrade(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isFullTrade()`：进行条件判定并返回布尔结果。
  - `public void setFullTrade(boolean fullTrade)`：写入或更新状态字段。
  - `private static void logTrade(Trade trade1, Trade trade2)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getFormattedItemLogMessage(List<Item> items)`：读取并返回状态/数据。

## `server/events/Events.java`

- `class Events`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Events()`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract int getInfo()`：读取并返回状态/数据。

## `server/events/RescueGaga.java`

- `class RescueGaga`：领域类型或功能模块，职责由同名文件实现定义。
  - `public RescueGaga(int completed)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCompleted()`：读取并返回状态/数据。
  - `public void complete()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getInfo()`：读取并返回状态/数据。
  - `public void giveSkill(Character chr)`：通用业务逻辑入口，需结合实现查看细节。

## `server/events/gm/Coconut.java`

- `class Coconut`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Coconut(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startEvent()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void bonusTime()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpOut()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMapleScore()`：读取并返回状态/数据。
  - `public int getStoryScore()`：读取并返回状态/数据。
  - `public void addMapleScore()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addStoryScore()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getBombings()`：读取并返回状态/数据。
  - `public void bombCoconut()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getFalling()`：读取并返回状态/数据。
  - `public void fallCoconut()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getStopped()`：读取并返回状态/数据。
  - `public void stopCoconut()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Coconuts getCoconut(int id)`：读取并返回状态/数据。
  - `public List<Coconuts> getAllCoconuts()`：读取并返回状态/数据。
  - `public void setCoconutsHittable(boolean hittable)`：写入或更新状态字段。

## `server/events/gm/Coconuts.java`

- `class Coconuts`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Coconuts(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hit()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getHits()`：读取并返回状态/数据。
  - `public void resetHits()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isHittable()`：进行条件判定并返回布尔结果。
  - `public void setHittable(boolean hittable)`：写入或更新状态字段。
  - `public long getHitTime()`：读取并返回状态/数据。

## `server/events/gm/Event.java`

- `class Event`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Event(int mapid, int limit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public int getLimit()`：读取并返回状态/数据。
  - `public void minusLimit()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addLimit()`：通用业务逻辑入口，需结合实现查看细节。

## `server/events/gm/Fitness.java`

- `class Fitness`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Fitness(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startFitness()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isTimerStarted()`：进行条件判定并返回布尔结果。
  - `public long getTime()`：读取并返回状态/数据。
  - `public void resetTimes()`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getTimeLeft()`：读取并返回状态/数据。
  - `public void checkAndMessage()`：校验输入参数或业务约束。

## `server/events/gm/Ola.java`

- `class Ola`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Ola(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startOla()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isTimerStarted()`：进行条件判定并返回布尔结果。
  - `public long getTime()`：读取并返回状态/数据。
  - `public void resetTimes()`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getTimeLeft()`：读取并返回状态/数据。

## `server/events/gm/OxQuiz.java`

- `class OxQuiz`：领域类型或功能模块，职责由同名文件实现定义。
  - `public OxQuiz(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isCorrectAnswer(Character chr, int answer)`：进行条件判定并返回布尔结果。
  - `public void sendQuestion()`：向外发送响应、消息或网络包。
  - `private static int getOXAnswer(int imgdir, int id)`：读取并返回状态/数据。

## `server/events/gm/Snowball.java`

- `class Snowball`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Snowball(int team, MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startEvent()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isHittable()`：进行条件判定并返回布尔结果。
  - `public void setHittable(boolean hit)`：写入或更新状态字段。
  - `public int getPosition()`：读取并返回状态/数据。
  - `public int getSnowmanHP()`：读取并返回状态/数据。
  - `public void setSnowmanHP(int hp)`：写入或更新状态字段。
  - `public void hit(int what, int damage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void message(int message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpOut()`：通用业务逻辑入口，需结合实现查看细节。

## `server/expeditions/Expedition.java`

- `class Expedition`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Expedition(Character player, ExpeditionType met, boolean sil, int minPlayers, int maxPlayers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMinSize()`：读取并返回状态/数据。
  - `public int getMaxSize()`：读取并返回状态/数据。
  - `public void beginRegistration()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void scheduleRegistrationEnd()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose(boolean log)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void log()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getTimeString(long then)`：读取并返回状态/数据。
  - `public void finishRegistration()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void start()`：通用业务逻辑入口，需结合实现查看细节。
  - `public String addMember(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int addMemberInt(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerExpeditionAttempt()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastExped(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean removeMember(Character chr)`：删除对象、关系或临时状态。
  - `public void ban(Entry<Integer, String> chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void monsterKilled(Character chr, Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setProperty(String key, String value)`：写入或更新状态字段。
  - `public String getProperty(String key)`：读取并返回状态/数据。
  - `public ExpeditionType getType()`：读取并返回状态/数据。
  - `public List<Character> getActiveMembers()`：读取并返回状态/数据。
  - `public final boolean isExpeditionTeamTogether()`：进行条件判定并返回布尔结果。
  - `public final void warpExpeditionTeam(int warpFrom, int warpTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpExpeditionTeam(int warpTo)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpExpeditionTeamToMapSpawnPoint(int warpFrom, int warpTo, int toSp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void warpExpeditionTeamToMapSpawnPoint(int warpTo, int toSp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean addChannelExpedition(Channel ch)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void removeChannelExpedition(Channel ch)`：删除对象、关系或临时状态。
  - `public Character getLeader()`：读取并返回状态/数据。
  - `public MapleMap getRecruitingMap()`：读取并返回状态/数据。
  - `public boolean contains(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isLeader(Character player)`：进行条件判定并返回布尔结果。
  - `public boolean isLeader(int playerid)`：进行条件判定并返回布尔结果。
  - `public boolean isRegistering()`：进行条件判定并返回布尔结果。
  - `public boolean isInProgress()`：进行条件判定并返回布尔结果。
  - `public long getStartTime()`：读取并返回状态/数据。
  - `public List<String> getBossLogs()`：读取并返回状态/数据。

## `server/expeditions/ExpeditionBossLog.java`

- `class ExpeditionBossLog`：领域类型或功能模块，职责由同名文件实现定义。
- `enum BossLogEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static void resetBossLogTable()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void resetBossLogTable(boolean week, Calendar c)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getBossLogTable(boolean week)`：读取并返回状态/数据。
  - `private static int countPlayerEntries(int cid, BossLogEntry boss)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void insertPlayerEntry(int cid, BossLogEntry boss)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean attemptBoss(int cid, int channel, Expedition exped, boolean log)`：通用业务逻辑入口，需结合实现查看细节。

## `server/expeditions/ExpeditionType.java`

- `enum ExpeditionType`：领域类型或功能模块，职责由同名文件实现定义。
  - `BALROG_EASY(3, 30, 50, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `BALROG_NORMAL(6, 30, 50, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `SCARGA(6, 30, 100, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `SHOWA(3, 30, 100, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `ZAKUM(6, 30, 50, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `HORNTAIL(6, 30, 100, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAOS_ZAKUM(6, 30, 120, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `CHAOS_HORNTAIL(6, 30, 120, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT(2, 7, 20, 30, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT1(2, 7, 20, 30, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `ARIANT2(2, 7, 20, 30, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `PINKBEAN(6, 30, 120, 255, 5),`：通用业务逻辑入口，需结合实现查看细节。
  - `CWKPQ(6, 30, 90, 255, 5);   // CWKPQ min-level 90, found thanks to Cato`：通用业务逻辑入口，需结合实现查看细节。
  - `ExpeditionType(int minSize, int maxSize, int minLevel, int maxLevel, int minutes)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMinSize()`：读取并返回状态/数据。
  - `public int getMaxSize()`：读取并返回状态/数据。
  - `public int getMinLevel()`：读取并返回状态/数据。
  - `public int getMaxLevel()`：读取并返回状态/数据。
  - `public int getRegistrationMinutes()`：读取并返回状态/数据。

## `server/gachapon/ElNath.java`

- `class ElNath`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Ellinia.java`

- `class Ellinia`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Gachapon.java`

- `class Gachapon`：领域类型或功能模块，职责由同名文件实现定义。
- `enum GachaponType`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static Gachapon getInstance()`：读取并返回状态/数据。
  - `public GachaponItem process(int npcId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void log(Character player, int itemId, String map)`：通用业务逻辑入口，需结合实现查看细节。

## `server/gachapon/GachaponItems.java`

- `class GachaponItems`：领域类型或功能模块，职责由同名文件实现定义。
  - `public abstract int[] getCommonItems()`：读取并返回状态/数据。
  - `public abstract int[] getUncommonItems()`：读取并返回状态/数据。
  - `public abstract int[] getRareItems()`：读取并返回状态/数据。
  - `public GachaponItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int[] getItems(int tier)`：读取并返回状态/数据。

## `server/gachapon/Global.java`

- `class Global`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Henesys.java`

- `class Henesys`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/KerningCity.java`

- `class KerningCity`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Ludibrium.java`

- `class Ludibrium`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/MushroomShrine.java`

- `class MushroomShrine`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/NautilusHarbor.java`

- `class NautilusHarbor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/NewLeafCity.java`

- `class NewLeafCity`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Perion.java`

- `class Perion`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/ShowaSpaFemale.java`

- `class ShowaSpaFemale`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/ShowaSpaMale.java`

- `class ShowaSpaMale`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/gachapon/Sleepywood.java`

- `class Sleepywood`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int[] getCommonItems()`：读取并返回状态/数据。
  - `public int[] getUncommonItems()`：读取并返回状态/数据。
  - `public int[] getRareItems()`：读取并返回状态/数据。

## `server/life/AbstractLoadedLife.java`

- `class AbstractLoadedLife`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbstractLoadedLife(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public AbstractLoadedLife(AbstractLoadedLife life)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getF()`：读取并返回状态/数据。
  - `public void setF(int f)`：写入或更新状态字段。
  - `public boolean isHidden()`：进行条件判定并返回布尔结果。
  - `public void setHide(boolean hide)`：写入或更新状态字段。
  - `public int getFh()`：读取并返回状态/数据。
  - `public void setFh(int fh)`：写入或更新状态字段。
  - `public int getStartFh()`：读取并返回状态/数据。
  - `public int getCy()`：读取并返回状态/数据。
  - `public void setCy(int cy)`：写入或更新状态字段。
  - `public int getRx0()`：读取并返回状态/数据。
  - `public void setRx0(int rx0)`：写入或更新状态字段。
  - `public int getRx1()`：读取并返回状态/数据。
  - `public void setRx1(int rx1)`：写入或更新状态字段。
  - `public int getId()`：读取并返回状态/数据。

## `server/life/ChangeableStats.java`

- `class ChangeableStats`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ChangeableStats(MonsterStats stats, OverrideMonsterStats ostats)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ChangeableStats(MonsterStats stats, int newLevel, boolean pqMob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public ChangeableStats(MonsterStats stats, float statModifier, boolean pqMob)`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/Element.java`

- `enum Element`：领域类型或功能模块，职责由同名文件实现定义。
  - `NEUTRAL(0), PHYSICAL(1), FIRE(2, true), ICE(3, true), LIGHTING(4), POISON(5), HOLY(6, true), DARKNESS(7)`：通用业务逻辑入口，需结合实现查看细节。
  - `Element(int v)`：通用业务逻辑入口，需结合实现查看细节。
  - `Element(int v, boolean special)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isSpecial()`：进行条件判定并返回布尔结果。
  - `public static Element getFromChar(char c)`：读取并返回状态/数据。
  - `public int getValue()`：读取并返回状态/数据。

## `server/life/ElementalEffectiveness.java`

- `enum ElementalEffectiveness`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static ElementalEffectiveness getByNumber(int num)`：读取并返回状态/数据。

## `server/life/LifeFactory.java`

- `class LifeFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static Set<Integer> getHpBarBosses()`：读取并返回状态/数据。
  - `public static AbstractLoadedLife getLife(int id, String type)`：读取并返回状态/数据。
  - `private static Data resolveUol(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isBboxAction(String name)`：进行条件判定并返回布尔结果。
  - `private static BoundingBox buildMonsterBoundingBox(int mid, String mobName, Data monsterData)`：构建输出对象、包体或配置。
  - `private static Data getMonsterData(int mid)`：读取并返回状态/数据。
  - `private static Data resolveMonsterVisualData(int mid, Data monsterData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean hasVisualBoundingBoxSource(Data monsterData)`：进行条件判定并返回布尔结果。
  - `private static Data resolvePrimaryVisualFrame(Data monsterData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Data resolveVisualFrame(Data frameData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void applyMonsterVisualStats(int mid, MonsterStats stats, Data visualMonsterData)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void setMonsterAttackInfo(int mid, List<MobAttackInfoHolder> attackInfos)`：写入或更新状态字段。
  - `public static Monster getMonster(int mid)`：读取并返回状态/数据。
  - `public static int getMonsterLevel(int mid)`：读取并返回状态/数据。
  - `private static void decodeElementalString(MonsterStats stats, String elemAttr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static NPC getNPC(int nid)`：读取并返回状态/数据。
  - `public static String getNPCName(int nid)`：读取并返回状态/数据。
  - `public static String getNPCDefaultTalk(int nid)`：读取并返回状态/数据。

## `server/life/MobAttackInfo.java`

- `class MobAttackInfo`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobAttackInfo(int mobId, int attackId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setDeadlyAttack(boolean isDeadlyAttack)`：写入或更新状态字段。
  - `public boolean isDeadlyAttack()`：进行条件判定并返回布尔结果。
  - `public void setMpBurn(int mpBurn)`：写入或更新状态字段。
  - `public int getMpBurn()`：读取并返回状态/数据。
  - `public void setDiseaseSkill(int diseaseSkill)`：写入或更新状态字段。
  - `public int getDiseaseSkill()`：读取并返回状态/数据。
  - `public void setDiseaseLevel(int diseaseLevel)`：写入或更新状态字段。
  - `public int getDiseaseLevel()`：读取并返回状态/数据。
  - `public void setMpCon(int mpCon)`：写入或更新状态字段。
  - `public int getMpCon()`：读取并返回状态/数据。

## `server/life/MobAttackInfoFactory.java`

- `class MobAttackInfoFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static MobAttackInfo getMobAttackInfo(Monster mob, int attack)`：读取并返回状态/数据。

## `server/life/MobSkill.java`

- `class MobSkill`：领域类型或功能模块，职责由同名文件实现定义。
  - `private MobSkill(MobSkillType type, int level, int mpCon, int spawnEffect, int hp, int x, int y, int count, long duration, long cooltime, float prop, Point lt, Point rb, int limit, List<Integer> toSummon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder(MobSkillType type, int level)`：构建输出对象、包体或配置。
  - `public Builder mpCon(int mpCon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder spawnEffect(int spawnEffect)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder hp(int hp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder x(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder y(int y)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder count(int count)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder duration(long duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder cooltime(long cooltime)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder prop(float prop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder lt(Point lt)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder rb(Point rb)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder limit(int limit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Builder toSummon(List<Integer> toSummon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MobSkill build()`：构建输出对象、包体或配置。
  - `applyEffect(null, monster, false, Collections.emptyList())`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MobSkillFactory.java`

- `class MobSkillFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static MobSkill getMobSkillOrThrow(MobSkillType type, int level)`：读取并返回状态/数据。
  - `public static Optional<MobSkill> getMobSkill(final MobSkillType type, final int level)`：读取并返回状态/数据。
  - `private static Optional<MobSkill> loadMobSkill(final MobSkillType type, final int level)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static String createKey(MobSkillType type, int skillLevel)`：创建对象、会话或业务记录。

## `server/life/MobSkillId.java`


## `server/life/MobSkillType.java`

- `enum MobSkillType`：领域类型或功能模块，职责由同名文件实现定义。
  - `ATTACK_UP(100),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_ATTACK_UP(101),`：通用业务逻辑入口，需结合实现查看细节。
  - `DEFENSE_UP(102),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_DEFENSE_UP(103),`：通用业务逻辑入口，需结合实现查看细节。
  - `ATTACK_UP_M(110),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_ATTACK_UP_M(111),`：通用业务逻辑入口，需结合实现查看细节。
  - `DEFENSE_UP_M(112),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_DEFENSE_UP_M(113),`：通用业务逻辑入口，需结合实现查看细节。
  - `HEAL_M(114),`：通用业务逻辑入口，需结合实现查看细节。
  - `HASTE_M(115),`：进行条件判定并返回布尔结果。
  - `SEAL(120),`：通用业务逻辑入口，需结合实现查看细节。
  - `DARKNESS(121),`：通用业务逻辑入口，需结合实现查看细节。
  - `WEAKNESS(122),`：通用业务逻辑入口，需结合实现查看细节。
  - `STUN(123),`：通用业务逻辑入口，需结合实现查看细节。
  - `CURSE(124),`：通用业务逻辑入口，需结合实现查看细节。
  - `POISON(125),`：通用业务逻辑入口，需结合实现查看细节。
  - `SLOW(126),`：通用业务逻辑入口，需结合实现查看细节。
  - `DISPEL(127),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEDUCE(128),`：通用业务逻辑入口，需结合实现查看细节。
  - `BANISH(129),`：通用业务逻辑入口，需结合实现查看细节。
  - `AREA_POISON(131),`：通用业务逻辑入口，需结合实现查看细节。
  - `REVERSE_INPUT(132),`：通用业务逻辑入口，需结合实现查看细节。
  - `UNDEAD(133),`：通用业务逻辑入口，需结合实现查看细节。
  - `STOP_POTION(134),`：通用业务逻辑入口，需结合实现查看细节。
  - `STOP_MOTION(135),`：通用业务逻辑入口，需结合实现查看细节。
  - `FEAR(136),`：通用业务逻辑入口，需结合实现查看细节。
  - `PHYSICAL_IMMUNE(140),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_IMMUNE(141),`：通用业务逻辑入口，需结合实现查看细节。
  - `HARD_SKIN(142),`：通用业务逻辑入口，需结合实现查看细节。
  - `PHYSICAL_COUNTER(143),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAGIC_COUNTER(144),`：通用业务逻辑入口，需结合实现查看细节。
  - `PHYSICAL_AND_MAGIC_COUNTER(145),`：通用业务逻辑入口，需结合实现查看细节。
  - `PAD(150),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAD(151),`：通用业务逻辑入口，需结合实现查看细节。
  - `PDR(152),`：通用业务逻辑入口，需结合实现查看细节。
  - `MDR(153),`：通用业务逻辑入口，需结合实现查看细节。
  - `ACC(154),`：通用业务逻辑入口，需结合实现查看细节。
  - `EVA(155),`：通用业务逻辑入口，需结合实现查看细节。
  - `SPEED(156),`：通用业务逻辑入口，需结合实现查看细节。
  - `SEAL_SKILL(157),`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON(200)`：通用业务逻辑入口，需结合实现查看细节。
  - `MobSkillType(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static Optional<MobSkillType> from(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isOutOfIdRange(int id)`：进行条件判定并返回布尔结果。
  - `public int getId()`：读取并返回状态/数据。

## `server/life/Monster.java`

- `class Monster`：领域类型或功能模块，职责由同名文件实现定义。
- `class DamageTask`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Monster(int id, MonsterStats stats)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Monster(Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void lockMonster()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unlockMonster()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void initWithStats(MonsterStats baseStats)`：初始化模块、资源或运行时状态。
  - `public void setSpawnEffect(int effect)`：写入或更新状态字段。
  - `public int getSpawnEffect()`：读取并返回状态/数据。
  - `public void disableDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void enableDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean dropsDisabled()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setMap(MapleMap map)`：写入或更新状态字段。
  - `public int getParentMobOid()`：读取并返回状态/数据。
  - `public void setParentMobOid(int parentMobId)`：写入或更新状态字段。
  - `public int countAvailableMobSummons(int summonsSize, int skillLimit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addSummonedMob(Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeSummonedMob(int mobOid)`：删除对象、关系或临时状态。
  - `private void setSummonerMob(Monster mob)`：写入或更新状态字段。
  - `private void dispatchClearSummons()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void pushRemoveAfterAction(Runnable run)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Runnable popRemoveAfterAction()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getHp()`：读取并返回状态/数据。
  - `public synchronized void addHp(int hp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void setStartingHp(int hp)`：写入或更新状态字段。
  - `public int getMaxHp()`：读取并返回状态/数据。
  - `public int getMp()`：读取并返回状态/数据。
  - `public void setMp(int mp)`：写入或更新状态字段。
  - `public int getMaxMp()`：读取并返回状态/数据。
  - `public int getExp()`：读取并返回状态/数据。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public int getCP()`：读取并返回状态/数据。
  - `public int getTeam()`：读取并返回状态/数据。
  - `public void setTeam(int team)`：写入或更新状态字段。
  - `public int getVenomMulti()`：读取并返回状态/数据。
  - `public void setVenomMulti(int multiplier)`：写入或更新状态字段。
  - `public MonsterStats getStats()`：读取并返回状态/数据。
  - `public void setStats(MonsterStats stats)`：写入或更新状态字段。
  - `public boolean isBoss()`：进行条件判定并返回布尔结果。
  - `public int getAnimationTime(String name)`：读取并返回状态/数据。
  - `private List<Integer> getRevives()`：读取并返回状态/数据。
  - `private byte getTagColor()`：读取并返回状态/数据。
  - `private byte getTagBgColor()`：读取并返回状态/数据。
  - `public void setHpZero()`：写入或更新状态字段。
  - `private boolean applyAnimationIfRoaming(int attackPos, MobSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized Integer applyAndGetHpDamage(int delta, boolean stayAlive)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void disposeMapObject()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMobHpBar(Character from)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean damage(Character attacker, int damage, boolean stayAlive)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applyDamage(Character from, int damage, boolean stayAlive, boolean fake)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void applyFakeDamage(Character from, int damage, boolean stayAlive)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void heal(int hp, int mp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isAttackedBy(Character chr)`：进行条件判定并返回布尔结果。
  - `private static boolean isWhiteExpGain(Character chr, Map<Integer, Float> personalRatio, double sdevRatio)`：进行条件判定并返回布尔结果。
  - `private static double calcExperienceStandDevThreshold(List<Float> entryExpRatio, int totalEntries)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void distributePlayerExperience(Character chr, float exp, float partyBonusMod, int totalPartyLevel, boolean highestPartyDamager, boolean whiteExpGain, boolean hasPartySharers)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void distributePartyExperience(Map<Character, Long> partyParticipation, float expPerDmg, Set<Character> underleveled, Map<Integer, Float> personalRatio, double sdevRatio)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void distributeExperience(int killerId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private float getStatusExpMultiplier(Character attacker, boolean hasPartySharers)`：读取并返回状态/数据。
  - `private static int expValueToInteger(double exp)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveExpToCharacter(Character attacker, Float personalExp, Float partyExp, boolean white, boolean hasPartySharers)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MonsterDropEntry> retrieveRelevantDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character killBy(final Character killer)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropFromFriendlyMonster(long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchRaiseQuestMobCount()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispatchMonsterKilled(boolean hasKiller)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void processMonsterKilled(boolean hasKiller)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchMonsterDamaged(Character from, int trueDmg)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dispatchMonsterHealed(int trueHeal)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void giveFamilyRep(FamilyEntry entry)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getHighestDamagerId()`：读取并返回状态/数据。
  - `public boolean isAlive()`：进行条件判定并返回布尔结果。
  - `public void addListener(MonsterListener listener)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getController()`：读取并返回状态/数据。
  - `private void setController(Character controller)`：写入或更新状态字段。
  - `public boolean isControllerHasAggro()`：进行条件判定并返回布尔结果。
  - `private void setControllerHasAggro(boolean controllerHasAggro)`：写入或更新状态字段。
  - `public boolean isControllerKnowsAboutAggro()`：进行条件判定并返回布尔结果。
  - `private void setControllerKnowsAboutAggro(boolean controllerKnowsAboutAggro)`：写入或更新状态字段。
  - `private void setControllerHasPuppet(boolean controllerHasPuppet)`：写入或更新状态字段。
  - `public Packet makeBossHPBarPacket()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasBossHPBar()`：进行条件判定并返回布尔结果。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public boolean isMobile()`：进行条件判定并返回布尔结果。
  - `public boolean isFacingLeft()`：进行条件判定并返回布尔结果。
  - `public ElementalEffectiveness getElementalEffectiveness(Element e)`：读取并返回状态/数据。
  - `private ElementalEffectiveness getMonsterEffectiveness(Element e)`：读取并返回状态/数据。
  - `private Character getActiveController()`：读取并返回状态/数据。
  - `private void broadcastMonsterStatusMessage(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int broadcastStatusEffect(final MonsterStatusEffect status)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration, boolean venom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void dispelSkill(final MobSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void applyMonsterBuff(final Map<MonsterStatus, Integer> stats, final int x, long duration, MobSkill skill, final List<Integer> reflection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void refreshMobPosition()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMobPosition(Point newPoint)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void debuffMobStat(MonsterStatus stat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void debuffMob(int skillid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isBuffed(MonsterStatus status)`：进行条件判定并返回布尔结果。
  - `public void setFake(boolean fake)`：写入或更新状态字段。
  - `public boolean isFake()`：进行条件判定并返回布尔结果。
  - `public MapleMap getMap()`：读取并返回状态/数据。
  - `public MonsterAggroCoordinator getMapAggroCoordinator()`：读取并返回状态/数据。
  - `public Set<MobSkillId> getSkills()`：读取并返回状态/数据。
  - `public boolean hasSkill(int skillId, int level)`：进行条件判定并返回布尔结果。
  - `public boolean canUseSkill(MobSkill toUse, boolean apply)`：进行条件判定并返回布尔结果。
  - `private boolean isReflectSkill(MobSkill mobSkill)`：进行条件判定并返回布尔结果。
  - `private void usedSkill(MobSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void clearSkill(MobSkillId msId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int canUseAttack(int attackPos, boolean isSkill)`：进行条件判定并返回布尔结果。
  - `private void usedAttack(final int attackPos, int mpCon, int cooltime)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void clearAttack(int attackPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasAnySkill()`：进行条件判定并返回布尔结果。
  - `public MobSkillId getRandomSkill()`：读取并返回状态/数据。
  - `public boolean isFirstAttack()`：进行条件判定并返回布尔结果。
  - `public int getBuffToGive()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public void addStolen(int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Integer> getStolen()`：读取并返回状态/数据。
  - `public void setTempEffectiveness(Element e, ElementalEffectiveness ee, long milli)`：写入或更新状态字段。
  - `public Collection<MonsterStatus> alreadyBuffedStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `public BanishInfo getBanish()`：读取并返回状态/数据。
  - `public void setBoss(boolean boss)`：写入或更新状态字段。
  - `public int getDropPeriodTime()`：读取并返回状态/数据。
  - `public int getPADamage()`：读取并返回状态/数据。
  - `public MonsterStatusEffect getStati(MonsterStatus ms)`：读取并返回状态/数据。
  - `public final ChangeableStats getChangedStats()`：读取并返回状态/数据。
  - `public final int getMobMaxHp()`：读取并返回状态/数据。
  - `public final void setOverrideStats(final OverrideMonsterStats ostats)`：写入或更新状态字段。
  - `public final void changeLevel(final int newLevel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void changeLevel(final int newLevel, boolean pqMob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private float getDifficultyRate(final int difficulty)`：读取并返回状态/数据。
  - `private void changeLevelByDifficulty(final int difficulty, boolean pqMob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void changeDifficulty(final int difficulty, boolean pqMob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean isPuppetInVicinity(Summon summon)`：进行条件判定并返回布尔结果。
  - `public boolean isCharacterPuppetInVicinity(Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean isLeadingPuppetInVicinity()`：进行条件判定并返回布尔结果。
  - `private Character getNextControllerCandidate()`：读取并返回状态/数据。
  - `public void aggroSwitchController(Character newController, boolean immediateAggro)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroAddPuppet(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroRemovePuppet(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroUpdateController()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void aggroUpdatePuppetController(Character newController)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroRedirectController()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Boolean aggroMoveLifeUpdate(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroAutoAggroUpdate(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroMonsterDamage(Character attacker, int damage)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void aggroMonsterControl(Client c, Monster mob, boolean immediateAggro)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void aggroRefreshPuppetVisibility(Character chrController, Summon puppet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroUpdatePuppetVisibility()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroClearDamages()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void aggroResetAggro()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int getRemoveAfter()`：读取并返回状态/数据。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MonsterDropEntry.java`

- `class MonsterDropEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterDropEntry(int itemId, int chance, int Minimum, int Maximum, short questid)`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MonsterGlobalDropEntry.java`

- `class MonsterGlobalDropEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterGlobalDropEntry(int itemId, int chance, int continent, int Minimum, int Maximum, short questid)`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MonsterInformationProvider.java`

- `class MonsterInformationProvider`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static MonsterInformationProvider getInstance()`：读取并返回状态/数据。
  - `protected MonsterInformationProvider()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<MonsterGlobalDropEntry> getRelevantGlobalDrops(int mapid)`：读取并返回状态/数据。
  - `private void retrieveGlobal()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MonsterDropEntry> retrieveEffectiveDrop(final int monsterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<MonsterDropEntry> retrieveDrop(final int monsterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<Integer> retrieveDropPool(final int monsterId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void setMobAttackAnimationTime(int monsterId, int attackPos, int animationTime)`：写入或更新状态字段。
  - `public final Integer getMobAttackAnimationTime(int monsterId, int attackPos)`：读取并返回状态/数据。
  - `public final void setMobSkillAnimationTime(MobSkill skill, int animationTime)`：写入或更新状态字段。
  - `public final Integer getMobSkillAnimationTime(MobSkill skill)`：读取并返回状态/数据。
  - `public final void setMobAttackInfo(int monsterId, int attackPos, int mpCon, int coolTime)`：写入或更新状态字段。
  - `public boolean isBoss(int id)`：进行条件判定并返回布尔结果。
  - `public String getMobNameFromId(int id)`：读取并返回状态/数据。
  - `public final void clearDrops()`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MonsterListener.java`

- `interface MonsterListener`：领域类型或功能模块，职责由同名文件实现定义。
  - `void monsterKilled(int aniTime)`：通用业务逻辑入口，需结合实现查看细节。
  - `void monsterDamaged(Character from, int trueDmg)`：通用业务逻辑入口，需结合实现查看细节。
  - `void monsterHealed(int trueHeal)`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/MonsterStats.java`

- `class MonsterStats`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void setChange(boolean change)`：写入或更新状态字段。
  - `public boolean isChangeable()`：进行条件判定并返回布尔结果。
  - `public int getExp()`：读取并返回状态/数据。
  - `public void setExp(int exp)`：写入或更新状态字段。
  - `public int getHp()`：读取并返回状态/数据。
  - `public void setHp(int hp)`：写入或更新状态字段。
  - `public int getMp()`：读取并返回状态/数据。
  - `public void setMp(int mp)`：写入或更新状态字段。
  - `public int getLevel()`：读取并返回状态/数据。
  - `public void setLevel(int level)`：写入或更新状态字段。
  - `public int removeAfter()`：删除对象、关系或临时状态。
  - `public void setRemoveAfter(int removeAfter)`：写入或更新状态字段。
  - `public int getDropPeriod()`：读取并返回状态/数据。
  - `public void setDropPeriod(int dropPeriod)`：写入或更新状态字段。
  - `public void setBoss(boolean boss)`：写入或更新状态字段。
  - `public boolean isBoss()`：进行条件判定并返回布尔结果。
  - `public void setFfaLoot(boolean ffaLoot)`：写入或更新状态字段。
  - `public boolean isFfaLoot()`：进行条件判定并返回布尔结果。
  - `public void setAnimationTime(String name, int delay)`：写入或更新状态字段。
  - `public int getAnimationTime(String name)`：读取并返回状态/数据。
  - `public boolean isMobile()`：进行条件判定并返回布尔结果。
  - `public List<Integer> getRevives()`：读取并返回状态/数据。
  - `public void setRevives(List<Integer> revives)`：写入或更新状态字段。
  - `public void setUndead(boolean undead)`：写入或更新状态字段。
  - `public boolean isUndead()`：进行条件判定并返回布尔结果。
  - `public void setEffectiveness(Element e, ElementalEffectiveness ee)`：写入或更新状态字段。
  - `public ElementalEffectiveness getEffectiveness(Element e)`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public void setName(String name)`：写入或更新状态字段。
  - `public byte getTagColor()`：读取并返回状态/数据。
  - `public void setTagColor(int tagColor)`：写入或更新状态字段。
  - `public byte getTagBgColor()`：读取并返回状态/数据。
  - `public void setTagBgColor(int tagBgColor)`：写入或更新状态字段。
  - `public void setSkills(Set<MobSkillId> skills)`：写入或更新状态字段。
  - `public Set<MobSkillId> getSkills()`：读取并返回状态/数据。
  - `public int getNoSkills()`：读取并返回状态/数据。
  - `public boolean hasSkill(int skillId, int level)`：进行条件判定并返回布尔结果。
  - `public void setFirstAttack(boolean firstAttack)`：写入或更新状态字段。
  - `public boolean isFirstAttack()`：进行条件判定并返回布尔结果。
  - `public void setBuffToGive(int buff)`：写入或更新状态字段。
  - `public int getBuffToGive()`：读取并返回状态/数据。
  - `void removeEffectiveness(Element e)`：删除对象、关系或临时状态。
  - `public BanishInfo getBanishInfo()`：读取并返回状态/数据。
  - `public void setBanishInfo(BanishInfo banish)`：写入或更新状态字段。
  - `public int getPADamage()`：读取并返回状态/数据。
  - `public void setPADamage(int PADamage)`：写入或更新状态字段。
  - `public int getCP()`：读取并返回状态/数据。
  - `public void setCP(int cp)`：写入或更新状态字段。
  - `public List<loseItem> loseItem()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addLoseItem(loseItem li)`：通用业务逻辑入口，需结合实现查看细节。
  - `public selfDestruction selfDestruction()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setSelfDestruction(selfDestruction sd)`：写入或更新状态字段。
  - `public void setExplosiveReward(boolean isExplosiveReward)`：写入或更新状态字段。
  - `public boolean isExplosiveReward()`：进行条件判定并返回布尔结果。
  - `public void setRemoveOnMiss(boolean removeOnMiss)`：写入或更新状态字段。
  - `public boolean removeOnMiss()`：删除对象、关系或临时状态。
  - `public void setCool(Pair<Integer, Integer> cool)`：写入或更新状态字段。
  - `public int getPDDamage()`：读取并返回状态/数据。
  - `public int getMADamage()`：读取并返回状态/数据。
  - `public int getMDDamage()`：读取并返回状态/数据。
  - `public boolean isFriendly()`：进行条件判定并返回布尔结果。
  - `public void setFriendly(boolean value)`：写入或更新状态字段。
  - `public void setPDDamage(int PDDamage)`：写入或更新状态字段。
  - `public void setMADamage(int MADamage)`：写入或更新状态字段。
  - `public void setMDDamage(int MDDamage)`：写入或更新状态字段。
  - `public int getFixedStance()`：读取并返回状态/数据。
  - `public void setFixedStance(int stance)`：写入或更新状态字段。
  - `public int getMovetype()`：读取并返回状态/数据。
  - `public void setMovetype(int movetype)`：写入或更新状态字段。
  - `public void setImgwidth(int imgwidth)`：写入或更新状态字段。
  - `public void setImgheight(int imgheight)`：写入或更新状态字段。
  - `public int getImgwidth()`：读取并返回状态/数据。
  - `public int getImgheight()`：读取并返回状态/数据。
  - `public void setBbox(int minX, int minY, int maxX, int maxY)`：写入或更新状态字段。
  - `public boolean hasBbox()`：进行条件判定并返回布尔结果。
  - `public int getBboxMinX()`：读取并返回状态/数据。
  - `public int getBboxMinY()`：读取并返回状态/数据。
  - `public int getBboxMaxX()`：读取并返回状态/数据。
  - `public int getBboxMaxY()`：读取并返回状态/数据。
  - `public int getBboxWidth()`：读取并返回状态/数据。
  - `public int getBboxHeight()`：读取并返回状态/数据。
  - `public boolean isLargeSize()`：进行条件判定并返回布尔结果。
  - `public MonsterStats copy()`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/NPC.java`

- `class NPC`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NPC(int id, NPCStats stats)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean hasShop()`：进行条件判定并返回布尔结果。
  - `public void sendShop(Client c)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。

## `server/life/NPCStats.java`

- `class NPCStats`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NPCStats(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getName()`：读取并返回状态/数据。
  - `public void setName(String name)`：写入或更新状态字段。

## `server/life/OverrideMonsterStats.java`

- `class OverrideMonsterStats`：领域类型或功能模块，职责由同名文件实现定义。
  - `public OverrideMonsterStats()`：通用业务逻辑入口，需结合实现查看细节。
  - `public OverrideMonsterStats(int hp, int mp, int exp, boolean change)`：通用业务逻辑入口，需结合实现查看细节。
  - `public OverrideMonsterStats(int hp, int mp, int exp)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getExp()`：读取并返回状态/数据。
  - `public void setOExp(int exp)`：写入或更新状态字段。
  - `public int getHp()`：读取并返回状态/数据。
  - `public void setOHp(int hp)`：写入或更新状态字段。
  - `public int getMp()`：读取并返回状态/数据。
  - `public void setOMp(int mp)`：写入或更新状态字段。

## `server/life/PlayerNPC.java`

- `class PlayerNPC`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerNPC(String name, int scriptId, int face, int hair, int gender, byte skin, Map<Short, Integer> equips, int dir, int FH, int RX0, int RX1, int CX, int CY, int oid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public PlayerNPC(PlayernpcsDO npcDO, List<PlayernpcsEquipDO> equipDOList)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void loadRunningRankData(int worlds)`：从外部来源加载数据（数据库/文件/配置）。
  - `public int getWorldRank()`：读取并返回状态/数据。
  - `public int getOverallRank()`：读取并返回状态/数据。
  - `public int getWorldJobRank()`：读取并返回状态/数据。
  - `public int getOverallJobRank()`：读取并返回状态/数据。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `private static int getAndIncrementRunningWorldJobRanks(int world, int job)`：读取并返回状态/数据。
  - `public static boolean canSpawnPlayerNpc(String name, int mapid)`：进行条件判定并返回布尔结果。
  - `public void updatePlayerNPCPosition(MapleMap map, Point newPos)`：更新已有对象/配置/缓存。
  - `private static void fetchAvailableScriptIdsFromDb(byte branch, List<Integer> list)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int getNextScriptId(byte branch)`：读取并返回状态/数据。
  - `private static PlayerNPC createPlayerNPCInternal(MapleMap map, Point pos, Character chr)`：创建对象、会话或业务记录。
  - `private static List<Integer> removePlayerNPCInternal(MapleMap map, Character chr)`：删除对象、关系或临时状态。
  - `public static boolean spawnPlayerNPC(int mapid, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static boolean spawnPlayerNPC(int mapid, Point pos, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static PlayerNPC getPlayerNPCFromWorldMap(String name, int world, int map)`：读取并返回状态/数据。
  - `public static void removePlayerNPC(Character chr)`：删除对象、关系或临时状态。
  - `public static void multicastSpawnPlayerNPC(int mapid, int world)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void removeAllPlayerNPC()`：删除对象、关系或临时状态。
  - `public static void addPlayerNPCMapObject(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。

## `server/life/PlayerNPCFactory.java`

- `class PlayerNPCFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public synchronized static boolean isExistentScriptid(int scriptid)`：进行条件判定并返回布尔结果。

## `server/life/SpawnPoint.java`

- `class SpawnPoint`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SpawnPoint(final Monster monster, Point pos, boolean immobile, int mobTime, int mobInterval, int team)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getSpawned()`：读取并返回状态/数据。
  - `public void setDenySpawn(boolean val)`：写入或更新状态字段。
  - `public boolean getDenySpawn()`：读取并返回状态/数据。
  - `public boolean shouldSpawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean shouldForceSpawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Monster getMonster()`：读取并返回状态/数据。
  - `public int getMonsterId()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public final int getF()`：读取并返回状态/数据。
  - `public final int getFh()`：读取并返回状态/数据。
  - `public int getMobTime()`：读取并返回状态/数据。
  - `public int getTeam()`：读取并返回状态/数据。

## `server/life/positioner/PlayerNPCPodium.java`

- `class PlayerNPCPodium`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static int getPlatformPosX(int platform)`：读取并返回状态/数据。
  - `private static int getPlatformPosY(int platform)`：读取并返回状态/数据。
  - `private static Point calcNextPos(int rank, int step)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point rearrangePlayerNpcs(MapleMap map, int newStep, List<PlayerNPC> pnpcs)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point reorganizePlayerNpcs(MapleMap map, int newStep, List<MapObject> mmoList)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int encodePodiumData(int podiumStep, int podiumCount)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point getNextPlayerNpcPosition(MapleMap map, int podiumData)`：读取并返回状态/数据。
  - `public static Point getNextPlayerNpcPosition(MapleMap map)`：读取并返回状态/数据。

## `server/life/positioner/PlayerNPCPositioner.java`

- `class PlayerNPCPositioner`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static boolean isPlayerNpcNearby(List<Point> otherPos, Point searchPos, int xLimit, int yLimit)`：进行条件判定并返回布尔结果。
  - `private static int calcDx(int newStep)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static int calcDy(int newStep)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static List<Point> rearrangePlayerNpcPositions(MapleMap map, int newStep, int pnpcsSize)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point rearrangePlayerNpcs(MapleMap map, int newStep, List<PlayerNPC> pnpcs)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point reorganizePlayerNpcs(MapleMap map, int newStep, List<MapObject> mmoList)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static Point getNextPlayerNpcPosition(MapleMap map, int initStep)`：读取并返回状态/数据。
  - `public static Point getNextPlayerNpcPosition(MapleMap map)`：读取并返回状态/数据。

## `server/loot/LootInventory.java`

- `class LootInventory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public LootInventory(Character from)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int hasItem(int itemid, int quantity)`：进行条件判定并返回布尔结果。

## `server/loot/LootManager.java`

- `class LootManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static boolean isRelevantDrop(MonsterDropEntry dropEntry, List<Character> players, List<LootInventory> playersInv)`：进行条件判定并返回布尔结果。
  - `public static List<MonsterDropEntry> retrieveRelevantDrops(int monsterId, List<Character> players)`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/AbstractAnimatedMapObject.java`

- `class AbstractAnimatedMapObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `public int getStance()`：读取并返回状态/数据。
  - `public void setStance(int stance)`：写入或更新状态字段。
  - `public boolean isFacingLeft()`：进行条件判定并返回布尔结果。
  - `public InPacket getIdleMovement()`：读取并返回状态/数据。
  - `private static Packet createIdleMovementPacket()`：创建对象、会话或业务记录。

## `server/maps/AbstractMapObject.java`

- `class AbstractMapObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `public abstract MapObjectType getType()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public void setPosition(Point position)`：写入或更新状态字段。
  - `public int getObjectId()`：读取并返回状态/数据。
  - `public void setObjectId(int id)`：写入或更新状态字段。
  - `public void nullifyPosition()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/AnimatedMapObject.java`

- `interface AnimatedMapObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `int getStance()`：读取并返回状态/数据。
  - `void setStance(int stance)`：写入或更新状态字段。
  - `boolean isFacingLeft()`：进行条件判定并返回布尔结果。

## `server/maps/Door.java`

- `class Door`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Door(Character owner, Point targetPosition)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateDoorPortal(Character owner)`：更新已有对象/配置/缓存。
  - `private void broadcastRemoveDoor(Character owner)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void attemptRemoveDoor(final Character owner)`：通用业务逻辑入口，需结合实现查看细节。
  - `private Portal getTownDoorPortal(int doorid)`：读取并返回状态/数据。
  - `public int getOwnerId()`：读取并返回状态/数据。
  - `public DoorObject getTownDoor()`：读取并返回状态/数据。
  - `public DoorObject getAreaDoor()`：读取并返回状态/数据。
  - `public MapleMap getTown()`：读取并返回状态/数据。
  - `public Portal getTownPortal()`：读取并返回状态/数据。
  - `public MapleMap getTarget()`：读取并返回状态/数据。
  - `public long getElapsedDeployTime()`：读取并返回状态/数据。
  - `private boolean dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isActive()`：进行条件判定并返回布尔结果。

## `server/maps/DoorObject.java`

- `class DoorObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `public DoorObject(int owner, MapleMap destination, MapleMap origin, int townPortalId, Point targetPosition, Point toPosition)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void update(int townPortalId, Point toPosition)`：更新已有对象/配置/缓存。
  - `private int getLinkedPortalId()`：读取并返回状态/数据。
  - `private Point getLinkedPortalPosition()`：读取并返回状态/数据。
  - `public void warp(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client, boolean launched)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client, boolean partyUpdate)`：向外发送响应、消息或网络包。
  - `public int getOwnerId()`：读取并返回状态/数据。
  - `public void setPairOid(int oid)`：写入或更新状态字段。
  - `public int getPairOid()`：读取并返回状态/数据。
  - `public boolean inTown()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapleMap getFrom()`：读取并返回状态/数据。
  - `public MapleMap getTo()`：读取并返回状态/数据。
  - `public MapleMap getTown()`：读取并返回状态/数据。
  - `public MapleMap getArea()`：读取并返回状态/数据。
  - `public Point getAreaPosition()`：读取并返回状态/数据。
  - `public Point toPosition()`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObjectType getType()`：读取并返回状态/数据。

## `server/maps/Dragon.java`

- `class Dragon`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Dragon(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public int getObjectId()`：读取并返回状态/数据。
  - `public void sendDestroyData(Client c)`：向外发送响应、消息或网络包。
  - `public Character getOwner()`：读取并返回状态/数据。

## `server/maps/FieldLimit.java`

- `enum FieldLimit`：领域类型或功能模块，职责由同名文件实现定义。
  - `JUMP(0x01),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOVEMENTSKILLS(0x02),`：通用业务逻辑入口，需结合实现查看细节。
  - `SUMMON(0x04),`：通用业务逻辑入口，需结合实现查看细节。
  - `DOOR(0x08),`：通用业务逻辑入口，需结合实现查看细节。
  - `CANNOTMIGRATE(0x10),    //change channel, town portal scroll, access cash shop, etc etc`：进行条件判定并返回布尔结果。
  - `CANNOTVIPROCK(0x40),`：进行条件判定并返回布尔结果。
  - `CANNOTMINIGAME(0x80),`：进行条件判定并返回布尔结果。
  - `CANNOTUSEMOUNTS(0x200),`：进行条件判定并返回布尔结果。
  - `CANNOTUSEPOTION(0x1000),`：进行条件判定并返回布尔结果。
  - `CANNOTJUMPDOWN(0x20000),`：进行条件判定并返回布尔结果。
  - `NO_EXP_DECREASE(0x80000),`：通用业务逻辑入口，需结合实现查看细节。
  - `DROP_LIMIT(0x400000)`：通用业务逻辑入口，需结合实现查看细节。
  - `FieldLimit(long i)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getValue()`：读取并返回状态/数据。
  - `public boolean check(int fieldlimit)`：校验输入参数或业务约束。

## `server/maps/Foothold.java`

- `class Foothold`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Foothold(Point p1, Point p2, int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isWall()`：进行条件判定并返回布尔结果。
  - `public int getX1()`：读取并返回状态/数据。
  - `public int getX2()`：读取并返回状态/数据。
  - `public int getY1()`：读取并返回状态/数据。
  - `public int getY2()`：读取并返回状态/数据。
  - `public int calculateFooting(int x)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int compareTo(Foothold o)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public int getNext()`：读取并返回状态/数据。
  - `public void setNext(int next)`：写入或更新状态字段。
  - `public int getPrev()`：读取并返回状态/数据。
  - `public void setPrev(int prev)`：写入或更新状态字段。

## `server/maps/FootholdTree.java`

- `class FootholdTree`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FootholdTree(Point p1, Point p2)`：通用业务逻辑入口，需结合实现查看细节。
  - `public FootholdTree(Point p1, Point p2, int depth)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void insert(Foothold f)`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<Foothold> getRelevants(Point p)`：读取并返回状态/数据。
  - `private List<Foothold> getRelevants(Point p, List<Foothold> list)`：读取并返回状态/数据。
  - `private Foothold findWallR(Point p1, Point p2)`：查询并返回匹配集合或单项结果。
  - `public Foothold findWall(Point p1, Point p2)`：查询并返回匹配集合或单项结果。
  - `public Foothold findBelow(Point p)`：查询并返回匹配集合或单项结果。
  - `public int getX1()`：读取并返回状态/数据。
  - `public int getX2()`：读取并返回状态/数据。
  - `public int getY1()`：读取并返回状态/数据。
  - `public int getY2()`：读取并返回状态/数据。
  - `public int getMaxDropX()`：读取并返回状态/数据。
  - `public int getMinDropX()`：读取并返回状态/数据。

## `server/maps/GenericPortal.java`

- `class GenericPortal`：领域类型或功能模块，职责由同名文件实现定义。
  - `public GenericPortal(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getId()`：读取并返回状态/数据。
  - `public void setId(int id)`：写入或更新状态字段。
  - `public String getName()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public String getTarget()`：读取并返回状态/数据。
  - `public void setPortalStatus(boolean newStatus)`：写入或更新状态字段。
  - `public boolean getPortalStatus()`：读取并返回状态/数据。
  - `public int getTargetMapId()`：读取并返回状态/数据。
  - `public int getType()`：读取并返回状态/数据。
  - `public String getScriptName()`：读取并返回状态/数据。
  - `public void setName(String name)`：写入或更新状态字段。
  - `public void setPosition(Point position)`：写入或更新状态字段。
  - `public void setTarget(String target)`：写入或更新状态字段。
  - `public void setTargetMapId(int targetmapid)`：写入或更新状态字段。
  - `public void setScriptName(String scriptName)`：写入或更新状态字段。
  - `public void enterPortal(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setPortalState(boolean state)`：写入或更新状态字段。
  - `public boolean getPortalState()`：读取并返回状态/数据。

## `server/maps/HiredMerchant.java`

- `class HiredMerchant`：领域类型或功能模块，职责由同名文件实现定义。
- `class SoldItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `private record Visitor(Character chr, Instant enteredAt)`：通用业务逻辑入口，需结合实现查看细节。
  - `public record PastVisitor(String chrName, Duration visitDuration)`：通用业务逻辑入口，需结合实现查看细节。
  - `public HiredMerchant(final Character owner, String desc, int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastToVisitorsThreadsafe(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastToVisitors(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte[] getShopRoomInfo()`：读取并返回状态/数据。
  - `public boolean addVisitor(Character visitor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeVisitor(Character chr)`：删除对象、关系或临时状态。
  - `private void addVisitorToHistory(Visitor visitor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getVisitorSlotThreadsafe(Character visitor)`：读取并返回状态/数据。
  - `private int getVisitorSlot(Character visitor)`：读取并返回状态/数据。
  - `private void removeAllVisitors()`：删除对象、关系或临时状态。
  - `private void removeOwner(Character owner)`：删除对象、关系或临时状态。
  - `public void withdrawMesos(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void takeItemBack(int slot, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean canBuy(Client c, Item newItem)`：进行条件判定并返回布尔结果。
  - `private int getQuantityLeft(int itemid)`：读取并返回状态/数据。
  - `public void buy(Client c, int item, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void announceItemSold(Item item, int mesos, int inStore)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceClose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeOwnerMerchant(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void closeShop(Client c, boolean timeout)`：通用业务逻辑入口，需结合实现查看细节。
  - `public synchronized void visitShop(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getOwner()`：读取并返回状态/数据。
  - `public void clearItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getOwnerId()`：读取并返回状态/数据。
  - `public String getDescription()`：读取并返回状态/数据。
  - `public Character[] getVisitorCharacters()`：读取并返回状态/数据。
  - `public List<PlayerShopItem> getItems()`：读取并返回状态/数据。
  - `public boolean hasItem(int itemid)`：进行条件判定并返回布尔结果。
  - `public boolean addItem(PlayerShopItem item)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearInexistentItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeFromSlot(int slot)`：删除对象、关系或临时状态。
  - `private int getFreeSlot()`：读取并返回状态/数据。
  - `public void setDescription(String description)`：写入或更新状态字段。
  - `public boolean isPublished()`：进行条件判定并返回布尔结果。
  - `public boolean isOpen()`：进行条件判定并返回布尔结果。
  - `public void setOpen(boolean set)`：写入或更新状态字段。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public boolean isOwner(Character chr)`：进行条件判定并返回布尔结果。
  - `public void sendMessage(Character chr, String msg)`：向外发送响应、消息或网络包。
  - `public List<PlayerShopItem> sendAvailableBundles(int itemid)`：向外发送响应、消息或网络包。
  - `public void saveItems(boolean shutdown) throws SQLException`：持久化当前状态到存储层。
  - `private static boolean check(Character chr, List<PlayerShopItem> items)`：校验输入参数或业务约束。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public int getTimeOpen()`：读取并返回状态/数据。
  - `public void clearMessages()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PastVisitor> getVisitorHistory()`：读取并返回状态/数据。
  - `public void addToBlacklist(String chrName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeFromBlacklist(String chrName)`：删除对象、关系或临时状态。
  - `public Set<String> getBlacklist()`：读取并返回状态/数据。
  - `private boolean isBlacklisted(String chrName)`：进行条件判定并返回布尔结果。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public MapleMap getMap()`：读取并返回状态/数据。
  - `public List<SoldItem> getSold()`：读取并返回状态/数据。
  - `public int getMesos()`：读取并返回状态/数据。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。

## `server/maps/Kite.java`

- `class Kite`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Kite(Character owner, String text, int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public Character getOwner()`：读取并返回状态/数据。
  - `public void setPosition(Point position)`：写入或更新状态字段。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public final Packet makeSpawnData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet makeDestroyData()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MapEffect.java`

- `class MapEffect`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapEffect(String msg, int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet makeDestroyData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet makeStartData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendStartData(Client client)`：向外发送响应、消息或网络包。

## `server/maps/MapFactory.java`

- `class MapFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `private static void loadLifeFromWz(MapleMap map, Data mapData)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static void loadLifeFromDb(MapleMap map)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static void loadLifeRaw(MapleMap map, int id, String type, int cy, int f, int fh, int rx0, int rx1, int x, int y, int hide, int mobTime, int team)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static MapleMap loadMapFromWz(int mapid, int world, int channel, EventInstanceManager event)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static AbstractLoadedLife loadLife(int id, String type, int cy, int f, int fh, int rx0, int rx1, int x, int y, int hide)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static Reactor loadReactor(Data reactor, String id, final byte FacingDirection)`：从外部来源加载数据（数据库/文件/配置）。
  - `private static String getMapName(int mapid)`：读取并返回状态/数据。
  - `private static String getMapStringName(int mapid)`：读取并返回状态/数据。
  - `public static String loadPlaceName(int mapid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static String loadStreetName(int mapid)`：从外部来源加载数据（数据库/文件/配置）。
  - `public static String getMapIdByLifeId(int lifeId)`：读取并返回状态/数据。
  - `private static String resolveDir(DataEntry dataEntry, int lifeId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String resolveFile(DataEntity dataEntry, int lifeId)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void resolvePath(DataEntity dataEntry, StringBuilder pathBuilder)`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MapItem.java`

- `class MapItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapItem(Item item, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapItem(Item item, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop, int questid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapItem(int meso, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Item getItem()`：读取并返回状态/数据。
  - `public final int getQuest()`：读取并返回状态/数据。
  - `public final int getItemId()`：读取并返回状态/数据。
  - `public final MapObject getDropper()`：读取并返回状态/数据。
  - `public final int getOwnerId()`：读取并返回状态/数据。
  - `public final int getPartyOwnerId()`：读取并返回状态/数据。
  - `public final void setPartyOwnerId(int partyid)`：写入或更新状态字段。
  - `public final int getClientsideOwnerId()`：读取并返回状态/数据。
  - `public final boolean hasClientsideOwnership(Character player)`：进行条件判定并返回布尔结果。
  - `public final boolean isFFADrop()`：进行条件判定并返回布尔结果。
  - `public final boolean hasExpiredOwnershipTime()`：进行条件判定并返回布尔结果。
  - `public final boolean canBePickedBy(Character chr)`：进行条件判定并返回布尔结果。
  - `public final Client getOwnerClient()`：读取并返回状态/数据。
  - `public final int getMeso()`：读取并返回状态/数据。
  - `public final boolean isPlayerDrop()`：进行条件判定并返回布尔结果。
  - `public final boolean isPickedUp()`：进行条件判定并返回布尔结果。
  - `public void setPickedUp(final boolean pickedUp)`：写入或更新状态字段。
  - `public long getDropTime()`：读取并返回状态/数据。
  - `public void setDropTime(long time)`：写入或更新状态字段。
  - `public byte getDropType()`：读取并返回状态/数据。
  - `public void lockItem()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unlockItem()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final MapObjectType getType()`：读取并返回状态/数据。
  - `public void sendSpawnData(final Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(final Client client)`：向外发送响应、消息或网络包。

## `server/maps/MapManager.java`

- `class MapManager`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapManager(EventInstanceManager eim, int world, int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapleMap resetMap(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized MapleMap loadMapFromWz(int mapid, boolean cache)`：从外部来源加载数据（数据库/文件/配置）。
  - `public MapleMap getMap(int mapid)`：读取并返回状态/数据。
  - `public MapleMap getMapByLifeId(int lifeId)`：读取并返回状态/数据。
  - `public MapleMap getDisposableMap(int mapid)`：读取并返回状态/数据。
  - `public boolean isMapLoaded(int mapId)`：进行条件判定并返回布尔结果。
  - `public void updateMaps()`：更新已有对象/配置/缓存。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MapMonitor.java`

- `class MapMonitor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapMonitor(final MapleMap map, String portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void cancelAction()`：进行条件判定并返回布尔结果。

## `server/maps/MapObject.java`

- `interface MapObject`：领域类型或功能模块，职责由同名文件实现定义。
  - `int getObjectId()`：读取并返回状态/数据。
  - `void setObjectId(int id)`：写入或更新状态字段。
  - `MapObjectType getType()`：读取并返回状态/数据。
  - `Point getPosition()`：读取并返回状态/数据。
  - `void setPosition(Point position)`：写入或更新状态字段。
  - `void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `void nullifyPosition()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MapObjectType.java`

- `enum MapObjectType`：领域类型或功能模块，职责由同名文件实现定义。

## `server/maps/MapPortal.java`

- `class MapPortal`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapPortal()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MapleMap.java`

- `class MapleMap`：领域类型或功能模块，职责由同名文件实现定义。
- `class MobLootEntry`：领域类型或功能模块，职责由同名文件实现定义。
- `class ActivateItemReactor`：领域类型或功能模块，职责由同名文件实现定义。
- `interface DelayedPacketCreation`：领域类型或功能模块，职责由同名文件实现定义。
- `interface SpawnCondition`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MapleMap(int mapid, int world, int channel, int returnMapId, float monsterRate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setEventInstance(EventInstanceManager eim)`：写入或更新状态字段。
  - `public EventInstanceManager getEventInstance()`：读取并返回状态/数据。
  - `public Rectangle getMapArea()`：读取并返回状态/数据。
  - `public int getWorld()`：读取并返回状态/数据。
  - `public void broadcastPacket(Character source, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastGMPacket(Character source, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastPacket(Packet packet, Predicate<Character> chrFilter)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void toggleDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static double getRangedDistance()`：读取并返回状态/数据。
  - `public List<MapObject> getMapObjectsInRect(Rectangle box, List<MapObjectType> types)`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。
  - `public Channel getChannelServer()`：读取并返回状态/数据。
  - `public World getWorldServer()`：读取并返回状态/数据。
  - `public MapleMap getReturnMap()`：读取并返回状态/数据。
  - `public int getReturnMapId()`：读取并返回状态/数据。
  - `public MapleMap getForcedReturnMap()`：读取并返回状态/数据。
  - `public int getForcedReturnId()`：读取并返回状态/数据。
  - `public void setForcedReturnMap(int map)`：写入或更新状态字段。
  - `public int getTimeLimit()`：读取并返回状态/数据。
  - `public void setTimeLimit(int timeLimit)`：写入或更新状态字段。
  - `public int getTimeLeft()`：读取并返回状态/数据。
  - `public void setReactorState()`：写入或更新状态字段。
  - `public final void limitReactor(final int rid, final int num)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isAllReactorState(final int reactorId, final int state)`：进行条件判定并返回布尔结果。
  - `public int getCurrentPartyId()`：读取并返回状态/数据。
  - `public void addPlayerNPCMapObject(PlayerNPC pnpcobject)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addMapObject(MapObject mapobject)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addSelfDestructive(Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean removeSelfDestructive(int mapobjectid)`：删除对象、关系或临时状态。
  - `private void spawnAndAddRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void spawnAndAddRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery, SpawnCondition condition)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void spawnRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery, SpawnCondition condition)`：通用业务逻辑入口，需结合实现查看细节。
  - `private int getUsableOID()`：读取并返回状态/数据。
  - `public void removeMapObject(int num)`：删除对象、关系或临时状态。
  - `public void removeMapObject(final MapObject obj)`：删除对象、关系或临时状态。
  - `private Point calcPointBelow(Point initial)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void generateMapDropRangeCache()`：通用业务逻辑入口，需结合实现查看细节。
  - `private Point bsearchDropPos(Point initial, Point fallback)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point calcDropPos(Point initial, Point fallback)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canDeployDoor(Point pos)`：进行条件判定并返回布尔结果。
  - `private static double getAngle(Point doorPoint, Point spawnPoint)`：读取并返回状态/数据。
  - `public static String getRoundedCoordinate(double angle)`：读取并返回状态/数据。
  - `private static void sortDropEntries(List<MonsterDropEntry> from, List<MonsterDropEntry> item, List<MonsterDropEntry> visibleQuest, List<MonsterDropEntry> otherQuest, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private byte dropItemsFromMonsterOnMap(List<MonsterDropEntry> dropEntry, Point pos, byte d, float chRate, byte droptype, int mobpos, Character chr, Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private byte dropGlobalItemsFromMonsterOnMap(List<MonsterGlobalDropEntry> globalEntry, Point pos, byte d, byte droptype, int mobpos, Character chr, Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void dropFromMonster(final Character chr, final Monster mob, final boolean useBaseRate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropItemsFromMonster(List<MonsterDropEntry> list, final Character chr, final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropFromFriendlyMonster(final Character chr, final Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropFromReactor(final Character chr, final Reactor reactor, Item drop, Point dropPos, short questid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void stopItemMonitor()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void cleanItemMonitor()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void startItemMonitor()`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean hasItemMonitor()`：进行条件判定并返回布尔结果。
  - `public int getDroppedItemCount()`：读取并返回状态/数据。
  - `private void instantiateItemDrop(MapItem mdrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerItemDrop(MapItem mdrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void unregisterItemDrop(MapItem mdrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void makeDisappearExpiredItemDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerMobItemDrops(byte droptype, int mobpos, float chRate, Point pos, List<MonsterDropEntry> dropEntry, List<MonsterDropEntry> visibleQuestEntry, List<MonsterDropEntry> otherQuestEntry, List<MonsterGlobalDropEntry> globalEntry, Character chr, Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void spawnMobItemDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<MapItem> getDroppedItems()`：读取并返回状态/数据。
  - `public int getDroppedItemsCountById(int itemid)`：读取并返回状态/数据。
  - `public void pickItemDrop(Packet pickupPacket, MapItem mdrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MapItem> updatePlayerItemDropsToParty(int partyid, int charid, List<Character> partyMembers, Character partyLeaver)`：更新已有对象/配置/缓存。
  - `public void updatePartyItemDropsToNewcomer(Character newcomer, List<MapItem> partyItems)`：更新已有对象/配置/缓存。
  - `private void spawnDrop(final Item idrop, final Point dropPos, final MapObject dropper, final Character chr, final byte droptype, final short questid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnMesoDrop(final int meso, final Point position, final MapObject dropper, final Character owner, final boolean playerDrop, final byte droptype)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void disappearingItemDrop(final MapObject dropper, final Character owner, final Item item, final Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void disappearingMesoDrop(final int meso, final MapObject dropper, final Character owner, final Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Monster getMonsterById(int id)`：读取并返回状态/数据。
  - `public int countMonster(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countMonster(int minid, int maxid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countMonsters()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countReactors()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<MapObject> getReactors()`：读取并返回状态/数据。
  - `public final List<MapObject> getMonsters()`：读取并返回状态/数据。
  - `public final List<Reactor> getAllReactors()`：读取并返回状态/数据。
  - `public final List<Monster> getAllMonsters()`：读取并返回状态/数据。
  - `public int countItems()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<MapObject> getItems()`：读取并返回状态/数据。
  - `public int countPlayers()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MapObject> getPlayers()`：读取并返回状态/数据。
  - `public List<Character> getAllPlayers()`：读取并返回状态/数据。
  - `public List<Character> getPlayersInRange(Rectangle box)`：读取并返回状态/数据。
  - `public int countAlivePlayers()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int countBosses()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean damageMonster(final Character chr, final Monster monster, final int damage)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastBalrogVictory(String leaderName)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastHorntailVictory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastZakumVictory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastPinkBeanVictory(int channel)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean removeKilledMonsterObject(Monster monster)`：删除对象、关系或临时状态。
  - `public void killMonster(final Monster monster, final Character chr, final boolean withDrops)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killMonster(final Monster monster, final Character chr, final boolean withDrops, int animation)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killFriendlies(Monster mob)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killMonster(int mobId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killMonsterWithDrops(int mobId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void softKillAllMonsters()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killAllMonstersNotFriendly()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void killAllMonsters()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void destroyReactors(final int first, final int last)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void destroyReactor(int oid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetReactors()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void resetReactors(List<Reactor> list)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void shuffleReactors()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void shuffleReactors(int first, int last)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void shuffleReactors(List<Object> list)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MapObject> getMapObjects()`：读取并返回状态/数据。
  - `public NPC getNPCById(int id)`：读取并返回状态/数据。
  - `public boolean containsNPC(int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void destroyNPC(int npcid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObject getMapObject(int oid)`：读取并返回状态/数据。
  - `public Monster getMonsterByOid(int oid)`：读取并返回状态/数据。
  - `public Reactor getReactorByOid(int oid)`：读取并返回状态/数据。
  - `public Reactor getReactorById(int Id)`：读取并返回状态/数据。
  - `public List<Reactor> getReactorsByIdRange(final int first, final int last)`：读取并返回状态/数据。
  - `public Reactor getReactorByName(String name)`：读取并返回状态/数据。
  - `public void spawnMonsterOnGroundBelow(int id, int x, int y)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonsterOnGroundBelow(Monster mob, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnCPQMonster(Monster mob, Point pos, int team)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void monsterItemDrop(final Monster m, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnFakeMonsterOnGroundBelow(Monster mob, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getGroundBelow(Point pos)`：读取并返回状态/数据。
  - `public Point getPointBelow(Point pos)`：读取并返回状态/数据。
  - `public void spawnRevives(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void applyRemoveAfter(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dismissRemoveAfter(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `private List<SpawnPoint> getMonsterSpawn()`：读取并返回状态/数据。
  - `private List<SpawnPoint> getAllMonsterSpawn()`：读取并返回状态/数据。
  - `public void spawnAllMonsterIdFromMapSpawnList(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnAllMonsterIdFromMapSpawnList(int id, int difficulty, boolean isPq)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnAllMonstersFromMapSpawnList()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnAllMonstersFromMapSpawnList(int difficulty, boolean isPq)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonster(final Monster monster, int difficulty, boolean isPq)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnDojoMonster(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMonsterWithEffect(final Monster monster, final int effect, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnFakeMonster(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void makeMonsterReal(final Monster monster)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnReactor(final Reactor reactor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnDoor(final DoorObject door)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Portal getDoorPortal(int doorid)`：读取并返回状态/数据。
  - `public void spawnSummon(final Summon summon)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnMist(final Mist mist, final int duration, boolean poison, boolean fake, boolean recovery)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void spawnKite(final Kite kite)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnItemDrop(final MapObject dropper, final Character owner, final Item item, Point pos, final boolean ffaDrop, final boolean playerDrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnItemDrop(final MapObject dropper, final Character owner, final Item item, Point pos, final byte dropType, final boolean playerDrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnItemDropList(List<Integer> list, final MapObject dropper, final Character owner, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnItemDropList(List<Integer> list, int minCopies, int maxCopies, final MapObject dropper, final Character owner, Point pos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void spawnItemDropList(List<Integer> list, int minCopies, int maxCopies, final MapObject dropper, final Character owner, Point pos, final boolean ffaDrop, final boolean playerDrop)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void registerMapSchedule(Runnable r, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void activateItemReactors(final MapItem drop, final Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void searchItemReactors(final Reactor react)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void changeEnvironment(String mapObj, int newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startMapEffect(String msg, int itemId)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startMapEffect(String msg, int itemId, long time)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getAnyCharacterFromParty(int partyid)`：读取并返回状态/数据。
  - `private void addPartyMemberInternal(Character chr, int partyid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removePartyMemberInternal(Character chr, int partyid)`：删除对象、关系或临时状态。
  - `public void addPartyMember(Character chr, int partyid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePartyMember(Character chr, int partyid)`：删除对象、关系或临时状态。
  - `public void removeParty(int partyid)`：删除对象、关系或临时状态。
  - `public void addPlayer(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static void announcePlayerDiseases(final Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Portal getRandomPlayerSpawnpoint()`：读取并返回状态/数据。
  - `public Portal findClosestTeleportPortal(Point from)`：查询并返回匹配集合或单项结果。
  - `public Portal findClosestPlayerSpawnpoint(Point from)`：查询并返回匹配集合或单项结果。
  - `public Portal findClosestPortal(Point from)`：查询并返回匹配集合或单项结果。
  - `public Portal findMarketPortal()`：查询并返回匹配集合或单项结果。
  - `public void addPlayerPuppet(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removePlayerPuppet(Character player)`：删除对象、关系或临时状态。
  - `public void removePlayer(Character chr)`：删除对象、关系或临时状态。
  - `public void broadcastMessage(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastGMMessage(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Character source, Packet packet, boolean repeatToSource)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Character source, Packet packet, boolean repeatToSource, boolean ranged)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Packet packet, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastMessage(Character source, Packet packet, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastMessage(Character source, Packet packet, double rangeSq, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean chrDisconnected(Iterator<Character> iterator, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void updateBossSpawn(Monster monster)`：更新已有对象/配置/缓存。
  - `public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastBossHpMessage(Monster mm, int bossHash, Character source, Packet packet, double rangeSq, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod, double rangeSq, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastGMSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField, boolean gmBroadcast)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastUpdateCharLookMessage(Character source, Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dropMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastStringMessage(int type, String message)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isNonRangedType(MapObjectType type)`：进行条件判定并返回布尔结果。
  - `private void sendObjectPlacement(Client c)`：向外发送响应、消息或网络包。
  - `public List<MapObject> getMapObjectsInRange(Point from, double rangeSq, List<MapObjectType> types)`：读取并返回状态/数据。
  - `public List<MapObject> getMapObjectsInBox(Rectangle box, List<MapObjectType> types)`：读取并返回状态/数据。
  - `public void addPortal(Portal myPortal)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Portal getPortal(String portalname)`：读取并返回状态/数据。
  - `public Portal getPortal(int portalid)`：读取并返回状态/数据。
  - `public void addMapleArea(Rectangle rec)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<Rectangle> getAreas()`：读取并返回状态/数据。
  - `public Rectangle getArea(int index)`：读取并返回状态/数据。
  - `public void setFootholds(FootholdTree footholds)`：写入或更新状态字段。
  - `public FootholdTree getFootholds()`：读取并返回状态/数据。
  - `public void setMapPointBoundings(int px, int py, int h, int w)`：写入或更新状态字段。
  - `public void setMapLineBoundings(int vrTop, int vrBottom, int vrLeft, int vrRight)`：写入或更新状态字段。
  - `public MonsterAggroCoordinator getAggroCoordinator()`：读取并返回状态/数据。
  - `public void addMonsterSpawn(Monster monster, int mobTime, int team)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addAllMonsterSpawn(Monster monster, int mobTime, int team)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeMonsterSpawn(int mobId, int x, int y)`：删除对象、关系或临时状态。
  - `public void removeAllMonsterSpawn(int mobId, int x, int y)`：删除对象、关系或临时状态。
  - `public void reportMonsterSpawnPoints(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Collection<Character> getCharacters()`：读取并返回状态/数据。
  - `public Character getCharacterById(int id)`：读取并返回状态/数据。
  - `private static void updateMapObjectVisibility(Character chr, MapObject mo)`：更新已有对象/配置/缓存。
  - `public void moveMonster(Monster monster, Point reportedPos)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void movePlayer(Character player, Point newPosition)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void toggleEnvironment(final String ms)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void moveEnvironment(final String ms, final int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getMapName()`：读取并返回状态/数据。
  - `public void setMapName(String mapName)`：写入或更新状态字段。
  - `public String getStreetName()`：读取并返回状态/数据。
  - `public void setClock(boolean hasClock)`：写入或更新状态字段。
  - `public boolean hasClock()`：进行条件判定并返回布尔结果。
  - `public void setTown(boolean isTown)`：写入或更新状态字段。
  - `public boolean isTown()`：进行条件判定并返回布尔结果。
  - `public boolean isMuted()`：进行条件判定并返回布尔结果。
  - `public void setMuted(boolean mute)`：写入或更新状态字段。
  - `public void setStreetName(String streetName)`：写入或更新状态字段。
  - `public void setEverlast(boolean everlast)`：写入或更新状态字段。
  - `public boolean getEverlast()`：读取并返回状态/数据。
  - `public int getSpawnedMonstersOnMap()`：读取并返回状态/数据。
  - `public void setMobCapacity(int capacity)`：写入或更新状态字段。
  - `public void setBackgroundTypes(HashMap<Integer, Integer> backTypes)`：写入或更新状态字段。
  - `public void sendNightEffect(Character chr)`：向外发送响应、消息或网络包。
  - `public void broadcastNightEffect()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character getCharacterByName(String name)`：读取并返回状态/数据。
  - `public boolean makeDisappearItemFromMap(MapObject mapobj)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean makeDisappearItemFromMap(MapItem mapitem)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void instanceMapFirstSpawn(int difficulty, boolean isPq)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void instanceMapRespawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void instanceMapForceRespawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeMapSpawnPoints()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void restoreMapSpawnPoints()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setAllowSpawnPointInBox(boolean allow, Rectangle box)`：写入或更新状态字段。
  - `public void setAllowSpawnPointInRange(boolean allow, Point from, double rangeSq)`：写入或更新状态字段。
  - `public SpawnPoint findClosestSpawnpoint(Point from)`：查询并返回匹配集合或单项结果。
  - `private static double getCurrentSpawnRate(int numPlayers)`：读取并返回状态/数据。
  - `private int getNumShouldSpawn(int numPlayers)`：读取并返回状态/数据。
  - `public void respawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void mobMpRecovery()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final int getNumPlayersInArea(final int index)`：读取并返回状态/数据。
  - `public final int getNumPlayersInRect(final Rectangle rect)`：读取并返回状态/数据。
  - `public final int getNumPlayersItemsInArea(final int index)`：读取并返回状态/数据。
  - `public final int getNumPlayersItemsInRect(final Rectangle rect)`：读取并返回状态/数据。
  - `public int getHPDec()`：读取并返回状态/数据。
  - `public void setHPDec(int delta)`：写入或更新状态字段。
  - `public int getHPDecProtect()`：读取并返回状态/数据。
  - `public void setHPDecProtect(int delta)`：写入或更新状态字段。
  - `public float getRecovery()`：读取并返回状态/数据。
  - `public void setRecovery(float recRate)`：写入或更新状态字段。
  - `private int hasBoat()`：进行条件判定并返回布尔结果。
  - `public void setBoat(boolean hasBoat)`：写入或更新状态字段。
  - `public void setDocked(boolean isDocked)`：写入或更新状态字段。
  - `public boolean getDocked()`：读取并返回状态/数据。
  - `public void setSeats(int seats)`：写入或更新状态字段。
  - `public int getSeats()`：读取并返回状态/数据。
  - `public void broadcastGMMessage(Character source, Packet packet, boolean repeatToSource)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void broadcastGMMessage(Character source, Packet packet, double rangeSq, Point rangedFrom)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastNONGMMessage(Character source, Packet packet, boolean repeatToSource)`：通用业务逻辑入口，需结合实现查看细节。
  - `public OxQuiz getOx()`：读取并返回状态/数据。
  - `public void setOx(OxQuiz set)`：写入或更新状态字段。
  - `public void setOxQuiz(boolean b)`：写入或更新状态字段。
  - `public boolean isOxQuiz()`：进行条件判定并返回布尔结果。
  - `public void setOnUserEnter(String onUserEnter)`：写入或更新状态字段。
  - `public String getOnUserEnter()`：读取并返回状态/数据。
  - `public void setOnFirstUserEnter(String onFirstUserEnter)`：写入或更新状态字段。
  - `public String getOnFirstUserEnter()`：读取并返回状态/数据。
  - `private boolean hasForcedEquip()`：进行条件判定并返回布尔结果。
  - `public void setFieldType(int fieldType)`：写入或更新状态字段。
  - `public void clearDrops(Character player)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void clearDrops()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setFieldLimit(int fieldLimit)`：写入或更新状态字段。
  - `public int getFieldLimit()`：读取并返回状态/数据。
  - `public void allowSummonState(boolean b)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean getSummonState()`：读取并返回状态/数据。
  - `public void warpEveryone(int to)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpEveryone(int to, int pto)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setSnowball(int team, Snowball ball)`：写入或更新状态字段。
  - `public Snowball getSnowball(int team)`：读取并返回状态/数据。
  - `private boolean specialEquip()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setCoconut(Coconut nut)`：写入或更新状态字段。
  - `public Coconut getCoconut()`：读取并返回状态/数据。
  - `public void warpOutByTeam(int team, int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startEvent(final Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean eventStarted()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startEvent()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setEventStarted(boolean event)`：写入或更新状态字段。
  - `public String getEventNPC()`：读取并返回状态/数据。
  - `public boolean hasEventNPC()`：进行条件判定并返回布尔结果。
  - `public boolean isStartingEventMap()`：进行条件判定并返回布尔结果。
  - `public boolean isEventMap()`：进行条件判定并返回布尔结果。
  - `public void setTimeMob(int id, String msg)`：写入或更新状态字段。
  - `public void toggleHiddenNPC(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setMobInterval(short interval)`：写入或更新状态字段。
  - `public short getMobInterval()`：读取并返回状态/数据。
  - `public void clearMapObjects()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void resetFully()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMapObjects()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetPQ()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetPQ(int difficulty)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetMapObjects(int difficulty, boolean isPq)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastShip(final boolean state)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastEnemyShip(final boolean state)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isHorntailDefeated()`：进行条件判定并返回布尔结果。
  - `public void spawnHorntailOnGroundBelow(final Point targetPoint)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean claimOwnership(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Character unclaimOwnership()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean unclaimOwnership(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void refreshOwnership()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isOwnershipRestricted(Character chr)`：进行条件判定并返回布尔结果。
  - `public void checkMapOwnerActivity()`：校验输入参数或业务约束。
  - `public List<MCSkill> getBlueTeamBuffs()`：读取并返回状态/数据。
  - `public List<MCSkill> getRedTeamBuffs()`：读取并返回状态/数据。
  - `public void clearBuffList()`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<MapObject> getAllPlayer()`：读取并返回状态/数据。
  - `public boolean isCPQMap()`：进行条件判定并返回布尔结果。
  - `public boolean isCPQMap2()`：进行条件判定并返回布尔结果。
  - `public boolean isCPQLobby()`：进行条件判定并返回布尔结果。
  - `public boolean isBlueCPQMap()`：进行条件判定并返回布尔结果。
  - `public boolean isPurpleCPQMap()`：进行条件判定并返回布尔结果。
  - `public Point getRandomSP(int team)`：读取并返回状态/数据。
  - `public GuardianSpawnPoint getRandomGuardianSpawn(int team)`：读取并返回状态/数据。
  - `public void addGuardianSpawnPoint(GuardianSpawnPoint a)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int spawnGuardian(int team, int num)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void buffMonsters(int team, MCSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final List<Integer> getSkillIds()`：读取并返回状态/数据。
  - `public final void addSkillId(int z)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void addMobSpawn(int mobId, int spendCP)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isCPQWinnerMap()`：进行条件判定并返回布尔结果。
  - `public boolean isCPQLoserMap()`：进行条件判定并返回布尔结果。
  - `public void runCharacterStatUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void registerCharacterStatUpdate(Runnable r)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMaxMobs()`：读取并返回状态/数据。
  - `public void setMaxMobs(int maxMobs)`：写入或更新状态字段。
  - `public int getMaxReactors()`：读取并返回状态/数据。
  - `public void setMaxReactors(int maxReactors)`：写入或更新状态字段。
  - `public int getDeathCP()`：读取并返回状态/数据。
  - `public void setDeathCP(int deathCP)`：写入或更新状态字段。
  - `public int getTimeDefault()`：读取并返回状态/数据。
  - `public void setTimeDefault(int timeDefault)`：写入或更新状态字段。
  - `public int getTimeExpand()`：读取并返回状态/数据。
  - `public void setTimeExpand(int timeExpand)`：写入或更新状态字段。

## `server/maps/MapleTVEffect.java`

- `class MapleTVEffect`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static synchronized boolean broadcastMapleTVIfNotActive(Character player, Character victim, List<String> messages, int tvType)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static synchronized void broadcastTV(boolean activity, final int userWorld, List<String> message, Character user, int type, Character partner)`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MiniDungeon.java`

- `class MiniDungeon`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MiniDungeon(int base, long timeLimit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean registerPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean unregisterPlayer(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void close()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/MiniDungeonInfo.java`

- `enum MiniDungeonInfo`：领域类型或功能模块，职责由同名文件实现定义。
  - `CAVE_OF_MUSHROOMS(MapId.ANT_TUNNEL_2, MapId.CAVE_OF_MUSHROOMS_BASE, 30), // Horny Mushroom, Zombie Mushroom`：通用业务逻辑入口，需结合实现查看细节。
  - `GOLEM_CASTLE_RUINS(MapId.SLEEPY_DUNGEON_4, MapId.GOLEMS_CASTLE_RUINS_BASE, 34), // Stone Golem, Mixed Golem`：通用业务逻辑入口，需结合实现查看细节。
  - `HILL_OF_SANDSTORMS(MapId.SAHEL_2, MapId.HILL_OF_SANDSTORMS_BASE, 30), // Sand Rat`：通用业务逻辑入口，需结合实现查看细节。
  - `HENESYS_PIG_FARM(MapId.RAIN_FOREST_EAST_OF_HENESYS, MapId.HENESYS_PIG_FARM_BASE, 30), // Pig, Ribbon Pig`：通用业务逻辑入口，需结合实现查看细节。
  - `DRAKES_BLUE_CAVE(MapId.COLD_CRADLE, MapId.DRAKES_BLUE_CAVE_BASE, 30), // Dark Drake`：通用业务逻辑入口，需结合实现查看细节。
  - `DRUMMER_BUNNYS_LAIR(MapId.EOS_TOWER_76TH_TO_90TH_FLOOR, MapId.DRUMMER_BUNNYS_LAIR_BASE, 30), // Drumming Bunny`：通用业务逻辑入口，需结合实现查看细节。
  - `THE_ROUND_TABLE_OF_KENTARUS(MapId.BATTLEFIELD_OF_FIRE_AND_WATER, MapId.ROUND_TABLE_OF_KENTAURUS_BASE, 30), // Blue/Red/Black Kentaurus`：通用业务逻辑入口，需结合实现查看细节。
  - `THE_RESTORING_MEMORY(MapId.DRAGON_NEST_LEFT_BEHIND, MapId.RESTORING_MEMORY_BASE, 19), // Skelegon, Skelosaurus`：通用业务逻辑入口，需结合实现查看细节。
  - `NEWT_SECURED_ZONE(MapId.DESTROYED_DRAGON_NEST, MapId.NEWT_SECURED_ZONE_BASE, 19), // Jr. Newtie, Transforming Jr. Newtie`：创建对象、会话或业务记录。
  - `PILLAGE_OF_TREASURE_ISLAND(MapId.RED_NOSE_PIRATE_DEN_2, MapId.PILLAGE_OF_TREASURE_ISLAND_BASE, 30), // Captain`：通用业务逻辑入口，需结合实现查看细节。
  - `CRITICAL_ERROR(MapId.LAB_AREA_C1, MapId.CRITICAL_ERROR_BASE, 30), // Roid`：通用业务逻辑入口，需结合实现查看细节。
  - `LONGEST_RIDE_ON_BYEBYE_STATION(MapId.FANTASY_THEME_PARK_3, MapId.LONGEST_RIDE_ON_BYEBYE_STATION, 19); // Froscola, Jester Scarlion`：通用业务逻辑入口，需结合实现查看细节。
  - `MiniDungeonInfo(int baseId, int dungeonId, int dungeons)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getBase()`：读取并返回状态/数据。
  - `public int getDungeonId()`：读取并返回状态/数据。
  - `public int getDungeons()`：读取并返回状态/数据。
  - `public static boolean isDungeonMap(int map)`：进行条件判定并返回布尔结果。
  - `public static MiniDungeonInfo getDungeon(int map)`：读取并返回状态/数据。

## `server/maps/MiniGame.java`

- `class MiniGame`：领域类型或功能模块，职责由同名文件实现定义。
- `enum MiniGameType`：领域类型或功能模块，职责由同名文件实现定义。
- `enum MiniGameResult`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MiniGame(Character owner, String description, String password)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getPassword()`：读取并返回状态/数据。
  - `public boolean checkPassword(String sentPw)`：校验输入参数或业务约束。
  - `public boolean hasFreeSlot()`：进行条件判定并返回布尔结果。
  - `public boolean isOwner(Character chr)`：进行条件判定并返回布尔结果。
  - `public void addVisitor(Character challenger)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeRoom(boolean forceClose)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeVisitor(boolean forceClose, Character challenger)`：删除对象、关系或临时状态。
  - `public boolean isVisitor(Character challenger)`：进行条件判定并返回布尔结果。
  - `public void broadcastToOwner(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastToVisitor(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setFirstSlot(int type)`：写入或更新状态字段。
  - `public int getFirstSlot()`：读取并返回状态/数据。
  - `private void updateMiniGameBox()`：更新已有对象/配置/缓存。
  - `private synchronized boolean minigameMatchFinish()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void minigameMatchFinished()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void minigameMatchStarted()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setQuitAfterGame(Character player, boolean quit)`：写入或更新状态字段。
  - `public boolean isMatchInProgress()`：进行条件判定并返回布尔结果。
  - `public void denyTie(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isTieDenied(Character chr)`：进行条件判定并返回布尔结果。
  - `public void minigameMatchOwnerWins(boolean forfeit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void minigameMatchVisitorWins(boolean forfeit)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void minigameMatchDraw()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setOwnerPoints()`：写入或更新状态字段。
  - `public void setVisitorPoints()`：写入或更新状态字段。
  - `public void setMatchesToWin(int type)`：写入或更新状态字段。
  - `public void setPieceType(int type)`：写入或更新状态字段。
  - `public int getPieceType()`：读取并返回状态/数据。
  - `public void setGameType(MiniGameType game)`：写入或更新状态字段。
  - `public MiniGameType getGameType()`：读取并返回状态/数据。
  - `public boolean isOmok()`：进行条件判定并返回布尔结果。
  - `public void shuffleList()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getCardId(int slot)`：读取并返回状态/数据。
  - `public int getMatchesToWin()`：读取并返回状态/数据。
  - `public void setLoser(int type)`：写入或更新状态字段。
  - `public int getLoser()`：读取并返回状态/数据。
  - `public void broadcast(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void chat(Client c, String chat)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendOmok(Client c, int type)`：向外发送响应、消息或网络包。
  - `public void sendMatchCard(Client c, int type)`：向外发送响应、消息或网络包。
  - `public Character getOwner()`：读取并返回状态/数据。
  - `public Character getVisitor()`：读取并返回状态/数据。
  - `public void setPiece(int move1, int move2, int type, Character chr)`：写入或更新状态字段。
  - `private boolean searchCombo(int x, int y, int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean searchCombo2(int x, int y, int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public String getDescription()`：读取并返回状态/数据。
  - `public int getOwnerScore()`：读取并返回状态/数据。
  - `public int getVisitorScore()`：读取并返回状态/数据。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public MapObjectType getType()`：读取并返回状态/数据。

## `server/maps/Mist.java`

- `class Mist`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Mist(Rectangle mistPosition, Monster mob, MobSkill skill)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Mist(Rectangle mistPosition, Character owner, StatEffect source)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public Skill getSourceSkill()`：读取并返回状态/数据。
  - `public boolean isMobMist()`：进行条件判定并返回布尔结果。
  - `public boolean isPoisonMist()`：进行条件判定并返回布尔结果。
  - `public boolean isRecoveryMist()`：进行条件判定并返回布尔结果。
  - `public int getSkillDelay()`：读取并返回状态/数据。
  - `public Monster getMobOwner()`：读取并返回状态/数据。
  - `public Character getOwner()`：读取并返回状态/数据。
  - `public Rectangle getBox()`：读取并返回状态/数据。
  - `public void setPosition(Point position)`：写入或更新状态字段。
  - `public final Packet makeDestroyData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet makeSpawnData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Packet makeFakeSpawnData(int level)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public boolean makeChanceResult()`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/PlayerShop.java`

- `class PlayerShop`：领域类型或功能模块，职责由同名文件实现定义。
- `class SoldItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerShop(Character owner, String description, int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getChannel()`：读取并返回状态/数据。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public int getItemId()`：读取并返回状态/数据。
  - `public boolean isOpen()`：进行条件判定并返回布尔结果。
  - `public void setOpen(boolean openShop)`：写入或更新状态字段。
  - `public boolean hasFreeSlot()`：进行条件判定并返回布尔结果。
  - `public byte[] getShopRoomInfo()`：读取并返回状态/数据。
  - `public boolean isOwner(Character chr)`：进行条件判定并返回布尔结果。
  - `private void addVisitor(Character visitor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceRemoveVisitor(Character visitor)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeVisitor(Character visitor)`：删除对象、关系或临时状态。
  - `public boolean isVisitor(Character visitor)`：进行条件判定并返回布尔结果。
  - `public boolean addItem(PlayerShopItem item)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void removeFromSlot(int slot)`：删除对象、关系或临时状态。
  - `private static boolean canBuy(Client c, Item newItem)`：进行条件判定并返回布尔结果。
  - `public void takeItemBack(int slot, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean buy(Client c, int item, short quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastToVisitors(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastRestoreToVisitors()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeVisitors()`：删除对象、关系或临时状态。
  - `public void broadcast(Packet packet)`：通用业务逻辑入口，需结合实现查看细节。
  - `private byte getVisitorSlot(Character chr)`：读取并返回状态/数据。
  - `public void chat(Client c, String chat)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void recoverChatLog()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void clearChatLog()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void closeShop()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendShop(Client c)`：向外发送响应、消息或网络包。
  - `public Character getOwner()`：读取并返回状态/数据。
  - `public Character[] getVisitors()`：读取并返回状态/数据。
  - `public List<PlayerShopItem> getItems()`：读取并返回状态/数据。
  - `public boolean hasItem(int itemid)`：进行条件判定并返回布尔结果。
  - `public String getDescription()`：读取并返回状态/数据。
  - `public void setDescription(String description)`：写入或更新状态字段。
  - `public void banPlayer(String name)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isBanned(String name)`：进行条件判定并返回布尔结果。
  - `public synchronized boolean visitShop(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public List<PlayerShopItem> sendAvailableBundles(int itemid)`：向外发送响应、消息或网络包。
  - `public List<SoldItem> getSold()`：读取并返回状态/数据。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public MapObjectType getType()`：读取并返回状态/数据。

## `server/maps/PlayerShopItem.java`

- `class PlayerShopItem`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PlayerShopItem(Item item, short bundles, int price)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setDoesExist(boolean tf)`：写入或更新状态字段。
  - `public boolean isExist()`：进行条件判定并返回布尔结果。
  - `public Item getItem()`：读取并返回状态/数据。
  - `public short getBundles()`：读取并返回状态/数据。
  - `public int getPrice()`：读取并返回状态/数据。
  - `public void setBundles(short bundles)`：写入或更新状态字段。

## `server/maps/Portal.java`

- `interface Portal`：领域类型或功能模块，职责由同名文件实现定义。
  - `int getType()`：读取并返回状态/数据。
  - `int getId()`：读取并返回状态/数据。
  - `Point getPosition()`：读取并返回状态/数据。
  - `String getName()`：读取并返回状态/数据。
  - `String getTarget()`：读取并返回状态/数据。
  - `String getScriptName()`：读取并返回状态/数据。
  - `void setScriptName(String newName)`：写入或更新状态字段。
  - `void setPortalStatus(boolean newStatus)`：写入或更新状态字段。
  - `boolean getPortalStatus()`：读取并返回状态/数据。
  - `int getTargetMapId()`：读取并返回状态/数据。
  - `void enterPortal(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `void setPortalState(boolean state)`：写入或更新状态字段。
  - `boolean getPortalState()`：读取并返回状态/数据。

## `server/maps/PortalFactory.java`

- `class PortalFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PortalFactory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Portal makePortal(int type, Data portal)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void loadPortal(GenericPortal myPortal, Data portal)`：从外部来源加载数据（数据库/文件/配置）。

## `server/maps/Reactor.java`

- `class Reactor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Reactor(ReactorStats stats, int rid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setShouldCollect(boolean collect)`：写入或更新状态字段。
  - `public boolean getShouldCollect()`：读取并返回状态/数据。
  - `public void lockReactor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void unlockReactor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hitLockReactor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hitUnlockReactor()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void setState(byte state)`：写入或更新状态字段。
  - `public byte getState()`：读取并返回状态/数据。
  - `public void setEventState(byte substate)`：写入或更新状态字段。
  - `public byte getEventState()`：读取并返回状态/数据。
  - `public ReactorStats getStats()`：读取并返回状态/数据。
  - `public int getId()`：读取并返回状态/数据。
  - `public void setDelay(int delay)`：写入或更新状态字段。
  - `public int getDelay()`：读取并返回状态/数据。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public int getReactorType()`：读取并返回状态/数据。
  - `public boolean isRecentHitFromAttack()`：进行条件判定并返回布尔结果。
  - `public void setMap(MapleMap map)`：写入或更新状态字段。
  - `public MapleMap getMap()`：读取并返回状态/数据。
  - `public boolean isAlive()`：进行条件判定并返回布尔结果。
  - `public boolean isActive()`：进行条件判定并返回布尔结果。
  - `public void setAlive(boolean alive)`：写入或更新状态字段。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public final Packet makeDestroyData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public final Packet makeSpawnData()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void resetReactorActions(int newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void forceHitReactor(final byte newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void tryForceHitReactor(final byte newState)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cancelReactorTimeout()`：进行条件判定并返回布尔结果。
  - `private void refreshReactorTimeout()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void delayedHitReactor(final Client c, long delay)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hitReactor(Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void hitReactor(boolean wHit, int charPos, short stance, int skillid, Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean destroy()`：通用业务逻辑入口，需结合实现查看细节。
  - `private void respawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void delayedRespawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceDelayedRespawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean inDelayedRespawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Rectangle getArea()`：读取并返回状态/数据。
  - `public String getName()`：读取并返回状态/数据。
  - `public void setName(String name)`：写入或更新状态字段。
  - `public GuardianSpawnPoint getGuardian()`：读取并返回状态/数据。
  - `public void setGuardian(GuardianSpawnPoint guardian)`：写入或更新状态字段。
  - `public final void setFacingDirection(final byte facingDirection)`：写入或更新状态字段。
  - `public final byte getFacingDirection()`：读取并返回状态/数据。

## `server/maps/ReactorDropEntry.java`

- `class ReactorDropEntry`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ReactorDropEntry(int itemId, int chance, int questId)`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/ReactorFactory.java`

- `class ReactorFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static final ReactorStats getReactorS(int rid)`：读取并返回状态/数据。
  - `public static ReactorStats getReactor(int rid)`：读取并返回状态/数据。

## `server/maps/ReactorStats.java`

- `class ReactorStats`：领域类型或功能模块，职责由同名文件实现定义。
  - `public void setTL(Point tl)`：写入或更新状态字段。
  - `public void setBR(Point br)`：写入或更新状态字段。
  - `public Point getTL()`：读取并返回状态/数据。
  - `public Point getBR()`：读取并返回状态/数据。
  - `public void addState(byte state, List<StateData> data, int timeOut)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addState(byte state, int type, Pair<Integer, Integer> reactItem, byte nextState, int timeOut, byte canTouch)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getTimeout(byte state)`：读取并返回状态/数据。
  - `public byte getTimeoutState(byte state)`：读取并返回状态/数据。
  - `public byte getStateSize(byte state)`：读取并返回状态/数据。
  - `public byte getNextState(byte state, byte index)`：读取并返回状态/数据。
  - `public List<Integer> getActiveSkills(byte state, byte index)`：读取并返回状态/数据。
  - `public int getType(byte state)`：读取并返回状态/数据。

## `server/maps/SavedLocation.java`

- `class SavedLocation`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SavedLocation(int mapId, int portal)`：持久化当前状态到存储层。
  - `public int getMapId()`：读取并返回状态/数据。
  - `public int getPortal()`：读取并返回状态/数据。

## `server/maps/SavedLocationType.java`

- `enum SavedLocationType`：领域类型或功能模块，职责由同名文件实现定义。
  - `public static SavedLocationType fromString(String Str)`：通用业务逻辑入口，需结合实现查看细节。

## `server/maps/Summon.java`

- `class Summon`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Summon(Character owner, int skill, Point pos, SummonMovementType movementType)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void sendSpawnData(Client client)`：向外发送响应、消息或网络包。
  - `public void sendDestroyData(Client client)`：向外发送响应、消息或网络包。
  - `public Character getOwner()`：读取并返回状态/数据。
  - `public int getSkill()`：读取并返回状态/数据。
  - `public int getHP()`：读取并返回状态/数据。
  - `public void addHP(int delta)`：通用业务逻辑入口，需结合实现查看细节。
  - `public SummonMovementType getMovementType()`：读取并返回状态/数据。
  - `public boolean isStationary()`：进行条件判定并返回布尔结果。
  - `public byte getSkillLevel()`：读取并返回状态/数据。
  - `public MapObjectType getType()`：读取并返回状态/数据。
  - `public final boolean isPuppet()`：进行条件判定并返回布尔结果。

## `server/maps/SummonMovementType.java`

- `enum SummonMovementType`：领域类型或功能模块，职责由同名文件实现定义。
  - `STATIONARY(0), FOLLOW(1), CIRCLE_FOLLOW(3)`：通用业务逻辑入口，需结合实现查看细节。
  - `SummonMovementType(int val)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getValue()`：读取并返回状态/数据。

## `server/minigame/RockPaperScissor.java`

- `class RockPaperScissor`：领域类型或功能模块，职责由同名文件实现定义。
  - `public RockPaperScissor(final Client c, final byte mode)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean answer(final Client c, final int answer)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean timeOut(final Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final boolean nextRound(final Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void reward(final Client c)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final void dispose(final Client c)`：通用业务逻辑入口，需结合实现查看细节。

## `server/movement/AbsoluteLifeMovement.java`

- `class AbsoluteLifeMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbsoluteLifeMovement(int type, Point position, int duration, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getPixelsPerSecond()`：读取并返回状态/数据。
  - `public void setPixelsPerSecond(Point wobble)`：写入或更新状态字段。
  - `public int getFh()`：读取并返回状态/数据。
  - `public void setFh(int fh)`：写入或更新状态字段。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。

## `server/movement/AbstractLifeMovement.java`

- `class AbstractLifeMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbstractLifeMovement(int type, Point position, int duration, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getType()`：读取并返回状态/数据。
  - `public int getDuration()`：读取并返回状态/数据。
  - `public int getNewstate()`：读取并返回状态/数据。
  - `public Point getPosition()`：读取并返回状态/数据。

## `server/movement/ChairMovement.java`

- `class ChairMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ChairMovement(int type, Point position, int duration, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getFh()`：读取并返回状态/数据。
  - `public void setFh(int fh)`：写入或更新状态字段。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。

## `server/movement/ChangeEquip.java`

- `class ChangeEquip`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ChangeEquip(int wui)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getPosition()`：读取并返回状态/数据。

## `server/movement/JumpDownMovement.java`

- `class JumpDownMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public JumpDownMovement(int type, Point position, int duration, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getPixelsPerSecond()`：读取并返回状态/数据。
  - `public void setPixelsPerSecond(Point wobble)`：写入或更新状态字段。
  - `public int getFh()`：读取并返回状态/数据。
  - `public void setFh(int fh)`：写入或更新状态字段。
  - `public int getOriginFh()`：读取并返回状态/数据。
  - `public void setOriginFh(int fh)`：写入或更新状态字段。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。

## `server/movement/LifeMovement.java`

- `interface LifeMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `Point getPosition()`：读取并返回状态/数据。
  - `int getNewstate()`：读取并返回状态/数据。
  - `int getDuration()`：读取并返回状态/数据。
  - `int getType()`：读取并返回状态/数据。

## `server/movement/LifeMovementFragment.java`

- `interface LifeMovementFragment`：领域类型或功能模块，职责由同名文件实现定义。
  - `void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。
  - `Point getPosition()`：读取并返回状态/数据。

## `server/movement/RelativeLifeMovement.java`

- `class RelativeLifeMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public RelativeLifeMovement(int type, Point position, int duration, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。

## `server/movement/TeleportMovement.java`

- `class TeleportMovement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public TeleportMovement(int type, Point position, int newstate)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void serialize(OutPacket p)`：通用业务逻辑入口，需结合实现查看细节。

## `server/partyquest/AriantColiseum.java`

- `class AriantColiseum`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AriantColiseum(MapleMap eventMap, Expedition expedition)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void setArenaUpdate(ScheduledFuture<?> ariantUpdate)`：写入或更新状态字段。
  - `private void setArenaFinish(ScheduledFuture<?> arenaFinish)`：写入或更新状态字段。
  - `private void setAriantScoreBoard(ScheduledFuture<?> ariantScore)`：写入或更新状态字段。
  - `private void cancelArenaUpdate()`：进行条件判定并返回布尔结果。
  - `private void cancelArenaFinish()`：进行条件判定并返回布尔结果。
  - `private void cancelAriantScoreBoard()`：进行条件判定并返回布尔结果。
  - `private void cancelAriantSchedules()`：进行条件判定并返回布尔结果。
  - `public int getAriantScore(Character chr)`：读取并返回状态/数据。
  - `public void clearAriantScore(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void updateAriantScore(Character chr, int points)`：更新已有对象/配置/缓存。
  - `private void broadcastAriantScoreUpdate()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getAriantRewardTier(Character chr)`：读取并返回状态/数据。
  - `public void clearAriantRewardTier(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void addLostShards(int quantity)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void leaveArena(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void leaveArenaInternal(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playerDisconnected(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void showArenaResults()`：通用业务逻辑入口，需结合实现查看细节。
  - `private static boolean isUnfairMatch(Integer winnerScore, Integer secondScore, Integer lostShardsScore, List<Integer> runnerupsScore)`：进行条件判定并返回布尔结果。
  - `public void distributeAriantPoints()`：通用业务逻辑入口，需结合实现查看细节。
  - `private ExpeditionType getExpeditionType()`：读取并返回状态/数据。
  - `private void enterKingsRoom()`：通用业务逻辑入口，需结合实现查看细节。
  - `private synchronized void dispose()`：通用业务逻辑入口，需结合实现查看细节。

## `server/partyquest/CarnivalFactory.java`

- `class CarnivalFactory`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CarnivalFactory()`：通用业务逻辑入口，需结合实现查看细节。
  - `public static final CarnivalFactory getInstance()`：读取并返回状态/数据。
  - `private void initialize()`：初始化模块、资源或运行时状态。
  - `private MCSkill randomizeSkill(boolean multi)`：通用业务逻辑入口，需结合实现查看细节。
  - `public MCSkill getSkill(final int id)`：读取并返回状态/数据。
  - `public MCSkill getGuardian(final int id)`：读取并返回状态/数据。
  - `public record MCSkill(int cpLoss, MobSkillType mobSkillType, int level, boolean targetsAll)`：通用业务逻辑入口，需结合实现查看细节。

## `server/partyquest/GuardianSpawnPoint.java`

- `class GuardianSpawnPoint`：领域类型或功能模块，职责由同名文件实现定义。
  - `public GuardianSpawnPoint(Point a)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Point getPosition()`：读取并返回状态/数据。
  - `public void setPosition(Point position)`：写入或更新状态字段。
  - `public boolean isTaken()`：进行条件判定并返回布尔结果。
  - `public void setTaken(boolean taken)`：写入或更新状态字段。
  - `public int getTeam()`：读取并返回状态/数据。
  - `public void setTeam(int team)`：写入或更新状态字段。

## `server/partyquest/MonsterCarnival.java`

- `class MonsterCarnival`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterCarnival(Party p1, Party p2, int mapid, boolean cpq1, int room)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void respawn()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void playerDisconnected(int charid)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void earlyFinish()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void leftParty(int charid)`：通用业务逻辑入口，需结合实现查看细节。
  - `protected void dispose()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canSummonR()`：进行条件判定并返回布尔结果。
  - `public void summonR()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canSummonB()`：进行条件判定并返回布尔结果。
  - `public void summonB()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canGuardianR()`：进行条件判定并返回布尔结果。
  - `public boolean canGuardianB()`：进行条件判定并返回布尔结果。
  - `protected void dispose(boolean warpout)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void exit()`：通用业务逻辑入口，需结合实现查看细节。
  - `public ScheduledFuture<?> getTimer()`：读取并返回状态/数据。
  - `private void finish(int winningTeam)`：通用业务逻辑入口，需结合实现查看细节。
  - `private void timeUp()`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getTimeLeft()`：读取并返回状态/数据。
  - `public int getTimeLeftSeconds()`：读取并返回状态/数据。
  - `private void extendTime()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void complete()`：通用业务逻辑入口，需结合实现查看细节。
  - `public Party getRed()`：读取并返回状态/数据。
  - `public void setRed(Party p1)`：写入或更新状态字段。
  - `public Party getBlue()`：读取并返回状态/数据。
  - `public void setBlue(Party p2)`：写入或更新状态字段。
  - `public Character getLeader1()`：读取并返回状态/数据。
  - `public void setLeader1(Character leader1)`：写入或更新状态字段。
  - `public Character getLeader2()`：读取并返回状态/数据。
  - `public void setLeader2(Character leader2)`：写入或更新状态字段。
  - `public Character getEnemyLeader(int team)`：读取并返回状态/数据。
  - `public int getBlueCP()`：读取并返回状态/数据。
  - `public void setBlueCP(int blueCP)`：写入或更新状态字段。
  - `public int getBlueTotalCP()`：读取并返回状态/数据。
  - `public void setBlueTotalCP(int blueTotalCP)`：写入或更新状态字段。
  - `public int getRedCP()`：读取并返回状态/数据。
  - `public void setRedCP(int redCP)`：写入或更新状态字段。
  - `public int getRedTotalCP()`：读取并返回状态/数据。
  - `public void setRedTotalCP(int redTotalCP)`：写入或更新状态字段。
  - `public int getTotalCP(int team)`：读取并返回状态/数据。
  - `public void setTotalCP(int totalCP, int team)`：写入或更新状态字段。
  - `public int getCP(int team)`：读取并返回状态/数据。
  - `public void setCP(int CP, int team)`：写入或更新状态字段。
  - `public int getRoom()`：读取并返回状态/数据。
  - `public MapleMap getEventMap()`：读取并返回状态/数据。

## `server/partyquest/MonsterCarnivalParty.java`

- `class MonsterCarnivalParty`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterCarnivalParty(final Character owner, final List<Character> members1, final byte team1)`：通用业务逻辑入口，需结合实现查看细节。
  - `public final Character getLeader()`：读取并返回状态/数据。
  - `public List<Character> getMembers()`：读取并返回状态/数据。
  - `public int getTeam()`：读取并返回状态/数据。
  - `public void warpOut(final int map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warp(final MapleMap map, final int portalid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warpOut()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean allInMap(MapleMap map)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void removeMember(Character chr)`：删除对象、关系或临时状态。
  - `public boolean isWinner()`：进行条件判定并返回布尔结果。
  - `public void setWinner(boolean status)`：写入或更新状态字段。
  - `public void displayMatchResult()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void summon()`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean canSummon()`：进行条件判定并返回布尔结果。

## `server/partyquest/PartyQuest.java`

- `class PartyQuest`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PartyQuest(Party party)`：通用业务逻辑入口，需结合实现查看细节。
  - `public Party getParty()`：读取并返回状态/数据。
  - `public List<Character> getParticipants()`：读取并返回状态/数据。
  - `public void removeParticipant(Character chr) throws Throwable`：删除对象、关系或临时状态。
  - `public static int getExp(String PQ, int level)`：读取并返回状态/数据。

## `server/partyquest/Pyramid.java`

- `class Pyramid`：领域类型或功能模块，职责由同名文件实现定义。
- `enum PyramidMode`：领域类型或功能模块，职责由同名文件实现定义。
  - `public Pyramid(Party party, PyramidMode mode, int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void startGaugeSchedule()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void kill()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void cool()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void miss()`：通用业务逻辑入口，需结合实现查看细节。
  - `public int timer()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void warp(int mapid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void broadcastInfo(String info, int amount)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean useSkill()`：通用业务逻辑入口，需结合实现查看细节。
  - `public void checkBuffs()`：校验输入参数或业务约束。
  - `public void sendScore(Character chr)`：向外发送响应、消息或网络包。

## `server/quest/Quest.java`

- `class Quest`：领域类型或功能模块，职责由同名文件实现定义。
  - `private Quest(int id)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean isAutoComplete()`：进行条件判定并返回布尔结果。
  - `public boolean isAutoStart()`：进行条件判定并返回布尔结果。
  - `public static Quest getInstance(int id)`：读取并返回状态/数据。
  - `public static Quest getInstanceFromInfoNumber(int infoNumber)`：读取并返回状态/数据。
  - `public boolean isSameDayRepeatable()`：进行条件判定并返回布尔结果。
  - `public boolean canStartQuestByStatus(Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean canQuestByInfoProgress(Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean canStart(Character chr, int npcid)`：进行条件判定并返回布尔结果。
  - `public boolean canComplete(Character chr, Integer npcid)`：进行条件判定并返回布尔结果。
  - `public void start(Character chr, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void complete(Character chr, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void complete(Character chr, int npc, Integer selection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void reset(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forfeit(Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceStart(Character chr, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean forceComplete(Character chr, int npc)`：通用业务逻辑入口，需结合实现查看细节。
  - `public short getId()`：读取并返回状态/数据。
  - `public List<Integer> getRelevantMobs()`：读取并返回状态/数据。
  - `public int getStartItemAmountNeeded(int itemid)`：读取并返回状态/数据。
  - `public int getCompleteItemAmountNeeded(int itemid)`：读取并返回状态/数据。
  - `public int getMobAmountNeeded(int mid)`：读取并返回状态/数据。
  - `public short getInfoNumber(Status qs)`：读取并返回状态/数据。
  - `public String getInfoEx(Status qs, int index)`：读取并返回状态/数据。
  - `public List<String> getInfoEx(Status qs)`：读取并返回状态/数据。
  - `public int getTimeLimit()`：读取并返回状态/数据。
  - `public static void clearCache(int quest)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void clearCache()`：通用业务逻辑入口，需结合实现查看细节。
  - `private AbstractQuestRequirement getRequirement(QuestRequirementType type, Data data)`：读取并返回状态/数据。
  - `private AbstractQuestAction getAction(QuestActionType type, Data data)`：读取并返回状态/数据。
  - `public boolean restoreLostItem(Character chr, int itemid)`：通用业务逻辑入口，需结合实现查看细节。
  - `public int getMedalRequirement()`：读取并返回状态/数据。
  - `public int getNpcRequirement(boolean checkEnd)`：读取并返回状态/数据。
  - `public boolean hasScriptRequirement(boolean checkEnd)`：进行条件判定并返回布尔结果。
  - `public boolean hasNextQuestAction()`：进行条件判定并返回布尔结果。
  - `public String getName()`：读取并返回状态/数据。
  - `public String getParentName()`：读取并返回状态/数据。
  - `public static boolean isExploitableQuest(short questid)`：进行条件判定并返回布尔结果。
  - `public static List<Quest> getMatchedQuests(String search)`：读取并返回状态/数据。
  - `public static void loadAllQuests()`：从外部来源加载数据（数据库/文件/配置）。
  - `public void expireQuest(Character chr)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/QuestActionType.java`

- `enum QuestActionType`：领域类型或功能模块，职责由同名文件实现定义。
  - `UNDEFINED(-1),`：通用业务逻辑入口，需结合实现查看细节。
  - `EXP(0),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM(1),`：通用业务逻辑入口，需结合实现查看细节。
  - `NEXTQUEST(2),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO(3),`：通用业务逻辑入口，需结合实现查看细节。
  - `QUEST(4),`：通用业务逻辑入口，需结合实现查看细节。
  - `SKILL(5),`：通用业务逻辑入口，需结合实现查看细节。
  - `FAME(6),`：通用业务逻辑入口，需结合实现查看细节。
  - `BUFF(7),`：通用业务逻辑入口，需结合实现查看细节。
  - `PETSKILL(8),`：通用业务逻辑入口，需结合实现查看细节。
  - `YES(9),`：通用业务逻辑入口，需结合实现查看细节。
  - `NO(10),`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC(11),`：通用业务逻辑入口，需结合实现查看细节。
  - `MIN_LEVEL(12),`：通用业务逻辑入口，需结合实现查看细节。
  - `NORMAL_AUTO_START(13),`：通用业务逻辑入口，需结合实现查看细节。
  - `PETTAMENESS(14),`：通用业务逻辑入口，需结合实现查看细节。
  - `PETSPEED(15),`：通用业务逻辑入口，需结合实现查看细节。
  - `INFO(16),`：通用业务逻辑入口，需结合实现查看细节。
  - `ZERO(16)`：通用业务逻辑入口，需结合实现查看细节。
  - `QuestActionType(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static QuestActionType getByWZName(String name)`：读取并返回状态/数据。

## `server/quest/QuestRequirementType.java`

- `enum QuestRequirementType`：领域类型或功能模块，职责由同名文件实现定义。
  - `UNDEFINED(-1),`：通用业务逻辑入口，需结合实现查看细节。
  - `JOB(0),`：通用业务逻辑入口，需结合实现查看细节。
  - `ITEM(1),`：通用业务逻辑入口，需结合实现查看细节。
  - `QUEST(2),`：通用业务逻辑入口，需结合实现查看细节。
  - `MIN_LEVEL(3),`：通用业务逻辑入口，需结合实现查看细节。
  - `MAX_LEVEL(4),`：通用业务逻辑入口，需结合实现查看细节。
  - `END_DATE(5),`：通用业务逻辑入口，需结合实现查看细节。
  - `MOB(6),`：通用业务逻辑入口，需结合实现查看细节。
  - `NPC(7),`：通用业务逻辑入口，需结合实现查看细节。
  - `FIELD_ENTER(8),`：通用业务逻辑入口，需结合实现查看细节。
  - `INTERVAL(9),`：通用业务逻辑入口，需结合实现查看细节。
  - `SCRIPT(10),`：通用业务逻辑入口，需结合实现查看细节。
  - `PET(11),`：通用业务逻辑入口，需结合实现查看细节。
  - `MIN_PET_TAMENESS(12),`：通用业务逻辑入口，需结合实现查看细节。
  - `MONSTER_BOOK(13),`：通用业务逻辑入口，需结合实现查看细节。
  - `NORMAL_AUTO_START(14),`：通用业务逻辑入口，需结合实现查看细节。
  - `INFO_NUMBER(15),`：通用业务逻辑入口，需结合实现查看细节。
  - `INFO_EX(16),`：通用业务逻辑入口，需结合实现查看细节。
  - `COMPLETED_QUEST(17),`：通用业务逻辑入口，需结合实现查看细节。
  - `START(18),`：通用业务逻辑入口，需结合实现查看细节。
  - `END(19),`：通用业务逻辑入口，需结合实现查看细节。
  - `DAY_BY_DAY(20),`：通用业务逻辑入口，需结合实现查看细节。
  - `MESO(21),`：通用业务逻辑入口，需结合实现查看细节。
  - `BUFF(22),`：通用业务逻辑入口，需结合实现查看细节。
  - `EXCEPT_BUFF(23)`：通用业务逻辑入口，需结合实现查看细节。
  - `QuestRequirementType(int type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public byte getType()`：读取并返回状态/数据。
  - `public static QuestRequirementType getByWZName(String name)`：读取并返回状态/数据。

## `server/quest/actions/AbstractQuestAction.java`

- `class AbstractQuestAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbstractQuestAction(QuestActionType action, Quest quest)`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer extSelection)`：校验输入参数或业务约束。
  - `public QuestActionType getType()`：读取并返回状态/数据。
  - `public static List<Integer> getJobBy5ByteEncoding(int encoded)`：读取并返回状态/数据。
  - `public static List<Integer> getJobBySimpleEncoding(int encoded)`：读取并返回状态/数据。

## `server/quest/actions/BuffAction.java`

- `class BuffAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BuffAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer extSelection)`：校验输入参数或业务约束。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/ExpAction.java`

- `class ExpAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ExpAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void runAction(Character chr, int gain)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/FameAction.java`

- `class FameAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FameAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/InfoAction.java`

- `class InfoAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public InfoAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/ItemAction.java`

- `class ItemAction`：领域类型或功能模块，职责由同名文件实现定义。
- `class ItemData`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ItemAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer extSelection)`：校验输入参数或业务约束。
  - `private void announceInventoryLimit(List<Integer> itemids, Character chr)`：通用业务逻辑入口，需结合实现查看细节。
  - `private boolean canHold(Character chr, List<Pair<Item, InventoryType>> gainList)`：进行条件判定并返回布尔结果。
  - `private boolean canGetItem(ItemData item, Character chr)`：进行条件判定并返回布尔结果。
  - `public boolean restoreLostItem(Character chr, int itemid)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/MesoAction.java`

- `class MesoAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MesoAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。
  - `public static void runAction(Character chr, int gain)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/NextQuestAction.java`

- `class NextQuestAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NextQuestAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/PetSkillAction.java`

- `class PetSkillAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PetSkillAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer extSelection)`：校验输入参数或业务约束。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/PetSpeedAction.java`

- `class PetSpeedAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PetSpeedAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/PetTamenessAction.java`

- `class PetTamenessAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PetTamenessAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/QuestAction.java`

- `class QuestAction`：领域类型或功能模块，职责由同名文件实现定义。
  - `public QuestAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/actions/SkillAction.java`

- `class SkillAction`：领域类型或功能模块，职责由同名文件实现定义。
- `class SkillData`：领域类型或功能模块，职责由同名文件实现定义。
  - `public SkillAction(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void run(Character chr, Integer extSelection)`：通用业务逻辑入口，需结合实现查看细节。

## `server/quest/requirements/AbstractQuestRequirement.java`

- `class AbstractQuestRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public AbstractQuestRequirement(QuestRequirementType type)`：通用业务逻辑入口，需结合实现查看细节。
  - `public abstract boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public abstract void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public QuestRequirementType getType()`：读取并返回状态/数据。

## `server/quest/requirements/BuffExceptRequirement.java`

- `class BuffExceptRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BuffExceptRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/BuffRequirement.java`

- `class BuffRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public BuffRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/CompletedQuestRequirement.java`

- `class CompletedQuestRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public CompletedQuestRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/EndDateRequirement.java`

- `class EndDateRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public EndDateRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/FieldEnterRequirement.java`

- `class FieldEnterRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public FieldEnterRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/InfoExRequirement.java`

- `class InfoExRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public InfoExRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public List<String> getInfo()`：读取并返回状态/数据。

## `server/quest/requirements/InfoNumberRequirement.java`

- `class InfoNumberRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public InfoNumberRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public short getInfoNumber()`：读取并返回状态/数据。

## `server/quest/requirements/IntervalRequirement.java`

- `class IntervalRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public IntervalRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public long getInterval()`：读取并返回状态/数据。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `private static String getIntervalTimeLeft(Character chr, IntervalRequirement r)`：读取并返回状态/数据。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/ItemRequirement.java`

- `class ItemRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ItemRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public int getItemAmountNeeded(int itemid, boolean complete)`：读取并返回状态/数据。

## `server/quest/requirements/JobRequirement.java`

- `class JobRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public JobRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/MaxLevelRequirement.java`

- `class MaxLevelRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MaxLevelRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/MesoRequirement.java`

- `class MesoRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MesoRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/MinLevelRequirement.java`

- `class MinLevelRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MinLevelRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/MinTamenessRequirement.java`

- `class MinTamenessRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MinTamenessRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/MobRequirement.java`

- `class MobRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MobRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public int getRequiredMobCount(int mobid)`：读取并返回状态/数据。

## `server/quest/requirements/MonsterBookCountRequirement.java`

- `class MonsterBookCountRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public MonsterBookCountRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/NpcRequirement.java`

- `class NpcRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public NpcRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public int get()`：读取并返回状态/数据。

## `server/quest/requirements/PetRequirement.java`

- `class PetRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public PetRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/QuestRequirement.java`

- `class QuestRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public QuestRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。

## `server/quest/requirements/ScriptRequirement.java`

- `class ScriptRequirement`：领域类型或功能模块，职责由同名文件实现定义。
  - `public ScriptRequirement(Quest quest, Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public void processData(Data data)`：通用业务逻辑入口，需结合实现查看细节。
  - `public boolean check(Character chr, Integer npcid)`：校验输入参数或业务约束。
  - `public boolean get()`：读取并返回状态/数据。

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
