# gms-server 全量符号索引（含非 public）

> 自动生成：`scripts/generate-full-symbol-docs.py`
> 源码路径：`BeiDou-Server`
> Java 文件数：1116

---

## `org.gms` / `ServerApplication.java`

### 类型声明
```text
class ServerApplication
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static void main(String[] args)
private static void initDb(String[] args) throws Exception
private static Connection getConnection(String driver, String url, String username, String password) throws Exception
private static String getStartParam(String[] args, String paramName)
```

---

## `org.gms.aop` / `aop/AuthEntryPointJwt.java`

### 类型声明
```text
class AuthEntryPointJwt
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException
```

---

## `org.gms.aop` / `aop/AuthTokenFilter.java`

### 类型声明
```text
class AuthTokenFilter
```

- 字段候选数: 4
```text
private JwtUtils jwtUtils
private UserDetailsServiceImpl userDetailsService
private SpringDocConfigProperties springDocConfigProperties
private SwaggerUiConfigProperties swaggerUiConfigProperties
```

- 方法/构造器候选数: 2
```text
protected void doFilterInternal(@NonNull HttpServletRequest request, @NonNull HttpServletResponse response, @NonNull FilterChain filterChain)
private String parseJwt(HttpServletRequest request)
```

---

## `org.gms.aop` / `aop/ServerFilter.java`

### 类型声明
```text
class ServerFilter
```

- 字段候选数: 1
```text
private final AccountService accountService
```

- 方法/构造器候选数: 2
```text
protected boolean shouldNotFilter(final HttpServletRequest request)
protected void doFilter(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws IOException, ServletException
```

---

## `org.gms.client` / `client/AbstractCharacterListener.java`

### 类型声明
```text
interface AbstractCharacterListener
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.client` / `client/AbstractCharacterObject.java`

### 类型声明
```text
class AbstractCharacterObject
```

- 字段候选数: 21
```text
protected MapleMap map
protected int attrStr
protected int attrDex
protected int attrLuk
protected int attrInt
protected int hp
protected int maxHp
protected int mp
protected int maxMp
protected int hpMpApUsed
protected int remainingAp
protected int[] remainingSp = new int[10]
protected transient int clientMaxHp
protected transient int clientMaxMp
protected transient int localMaxHp = 50
protected transient int localMaxMp = 5
protected float transientHp = Float.NEGATIVE_INFINITY
protected float transientMp = Float.NEGATIVE_INFINITY
private AbstractCharacterListener listener = null
protected final Lock statRlock
protected final Lock statWlock
```

- 方法/构造器候选数: 76
```text
protected AbstractCharacterObject()
protected void setListener(AbstractCharacterListener listener)
public int getStr()
public int getDex()
public int getInt()
public int getLuk()
public int getRemainingAp()
protected int getRemainingSp(int jobid)
public int[] getRemainingSps()
public int getHpMpApUsed()
public boolean isAlive()
public int getHp()
public int getMp()
public int getMaxHp()
public int getMaxMp()
public int getCurrentMaxHp()
public int getCurrentMaxMp()
private void dispatchHpChanged(final int oldHp)
private void dispatchHpMpPoolUpdated()
private void dispatchStatUpdated()
private void dispatchStatPoolUpdateAnnounced()
protected void setHp(int newHp)
protected void setMp(int newMp)
public void setRemainingSp(int remainingSp, int skillbook)
protected void setMaxHp(int hp_)
protected void setMaxMp(int mp_)
private static long clampStat(int v, int min, int max)
private static long calcStatPoolNode(Integer v, int displacement)
private static long calcStatPoolLong(Integer v1, Integer v2, Integer v3, Integer v4)
private void changeStatPool(Long hpMpPool, Long strDexIntLuk, Long newSp, int newAp, boolean silent)
public void healHpMp()
public void updateHpMp(int x)
public void updateHpMp(int newhp, int newmp)
public void changeHpMp(int newhp, int newmp, boolean silent)
private void changeHpMpPool(Integer hp, Integer mp, Integer maxhp, Integer maxmp, boolean silent)
public void updateHp(int hp)
public void updateMaxHp(int maxhp)
public void updateHpMaxHp(int hp, int maxhp)
private void updateHpMaxHp(Integer hp, Integer maxhp)
public void updateMp(int mp)
public void updateMaxMp(int maxmp)
public void updateMpMaxMp(int mp, int maxmp)
private void updateMpMaxMp(Integer mp, Integer maxmp)
public void updateMaxHpMaxMp(int maxhp, int maxmp)
protected void enforceMaxHpMp()
public int safeAddHP(int delta)
public void addHP(int delta)
public void addMP(int delta)
public void addMPHP(int hpDelta, int mpDelta)
protected void addMaxMPMaxHP(int hpdelta, int mpdelta, boolean silent)
public void addMaxHP(int delta)
public void addMaxMP(int delta)
public void setStr(int str)
public void setDex(int dex)
public void setInt(int int_)
public void setLuk(int luk)
public boolean assignStr(int x)
public boolean assignDex(int x)
public boolean assignInt(int x)
public boolean assignLuk(int x)
public boolean assignHP(int deltaHP, int deltaAp)
public boolean assignMP(int deltaMP, int deltaAp)
private static int apAssigned(Integer x)
public boolean assignStrDexIntLuk(int deltaStr, int deltaDex, int deltaInt, int deltaLuk)
private boolean assignStrDexIntLuk(Integer deltaStr, Integer deltaDex, Integer deltaInt, Integer deltaLuk)
public void updateStrDexIntLuk(int x)
public void changeRemainingAp(int x, boolean silent)
public void gainAp(int deltaAp, boolean silent)
protected void updateStrDexIntLuk(int str, int dex, int int_, int luk, int remainingAp)
private void changeStrDexIntLuk(Integer str, Integer dex, Integer int_, Integer luk, int remainingAp, boolean silent)
private void changeStrDexIntLukSp(Integer str, Integer dex, Integer int_, Integer luk, int remainingAp, int remainingSp, int skillbook, boolean silent)
protected void updateStrDexIntLukSp(int str, int dex, int int_, int luk, int remainingAp, int remainingSp, int skillbook)
protected void setRemainingSp(int[] sps)
protected void updateRemainingSp(int remainingSp, int skillbook)
protected void changeRemainingSp(int remainingSp, int skillbook, boolean silent)
public void gainSp(int deltaSp, int skillbook, boolean silent)
```

---

## `org.gms.client` / `client/BuddyList.java`

### 类型声明
```text
class BuddyList
enum BuddyOperation
enum BuddyAddResult
```

- 字段候选数: 1
```text
private int capacity
```

- 方法/构造器候选数: 16
```text
public BuddyList(int capacity)
public boolean contains(int characterId)
public boolean containsVisible(int characterId)
public int getCapacity()
public void setCapacity(int capacity)
public BuddylistEntry get(int characterId)
public BuddylistEntry get(String characterName)
public void put(BuddylistEntry entry)
public void remove(int characterId)
public Collection<BuddylistEntry> getBuddies()
public boolean isFull()
public int[] getBuddyIds()
public void broadcast(Packet packet, PlayerStorage pstorage)
public void loadFromDb(int characterId)
public CharacterNameAndId pollPendingRequest()
public void addBuddyRequest(Client c, int cidFrom, String nameFrom, int channelFrom)
```

---

## `org.gms.client` / `client/BuddylistEntry.java`

### 类型声明
```text
class BuddylistEntry
```

- 字段候选数: 5
```text
private final String name
private String group
private final int cid
private int channel
private boolean visible
```

- 方法/构造器候选数: 12
```text
public BuddylistEntry(String name, String group, int characterId, int channel, boolean visible)
public int getChannel()
public void setChannel(int channel)
public boolean isOnline()
public String getName()
public String getGroup()
public int getCharacterId()
public void setVisible(boolean visible)
public boolean isVisible()
public void changeGroup(String group)
public int hashCode()
public boolean equals(Object obj)
```

---

## `org.gms.client` / `client/BuffStat.java`

### 类型声明
```text
enum BuffStat
```

- 字段候选数: 2
```text
private final long i
private final boolean isFirst
```

- 方法/构造器候选数: 90
```text
MORPH(0x2L),
RECOVERY(0x4L),
MAPLE_WARRIOR(0x8L),
STANCE(0x10L),
SHARP_EYES(0x20L),
MANA_REFLECTION(0x40L),
SHADOW_CLAW(0x100L),
INFINITY(0x200L),
HOLY_SHIELD(0x400L),
HAMSTRING(0x800L),
BLIND(0x1000L),
CONCENTRATE(0x2000L),
PUPPET(0x4000L),
ECHO_OF_HERO(0x8000L),
MESO_UP_BY_ITEM(0x10000L),
GHOST_MORPH(0x20000L),
AURA(0x40000L),
CONFUSE(0x80000L),
COUPON_EXP1(0x100000L),
EXP_BUFF(0x40000000L),
COUPON_EXP2(0x200000L),
COUPON_EXP3(0x400000L), COUPON_EXP4(0x400000L),
COUPON_DRP1(0x800000L),
COUPON_DRP2(0x1000000L), COUPON_DRP3(0x1000000L),
ITEM_UP_BY_ITEM(0x100000L),
RESPECT_PIMMUNE(0x200000L),
RESPECT_MIMMUNE(0x400000L),
DEFENSE_ATT(0x800000L),
DEFENSE_STATE(0x1000000L),
HPREC(0x2000000L),
MPREC(0x4000000L),
BERSERK_FURY(0x8000000L),
DIVINE_BODY(0x10000000L),
SPARK(0x20000000L),
MAP_CHAIR(0x40000000L),
FINALATTACK(0x80000000L),
WATK(0x100000000L),
WDEF(0x200000000L),
MATK(0x400000000L),
MDEF(0x800000000L),
ACC(0x1000000000L),
AVOID(0x2000000000L),
HANDS(0x4000000000L),
SPEED(0x8000000000L),
JUMP(0x10000000000L),
MAGIC_GUARD(0x20000000000L),
DARKSIGHT(0x40000000000L),
BOOSTER(0x80000000000L),
POWERGUARD(0x100000000000L),
HYPERBODYHP(0x200000000000L),
HYPERBODYMP(0x400000000000L),
INVINCIBLE(0x800000000000L),
SOULARROW(0x1000000000000L),
STUN(0x2000000000000L),
POISON(0x4000000000000L),
SEAL(0x8000000000000L),
DARKNESS(0x10000000000000L),
COMBO(0x20000000000000L),
SUMMON(0x20000000000000L),
WK_CHARGE(0x40000000000000L),
DRAGONBLOOD(0x80000000000000L),
HOLY_SYMBOL(0x100000000000000L),
MESOUP(0x200000000000000L),
SHADOWPARTNER(0x400000000000000L),
PICKPOCKET(0x800000000000000L),
MESOGUARD(0x1000000000000000L),
EXP_INCREASE(0x2000000000000000L),
WEAKEN(0x4000000000000000L),
MAP_PROTECTION(0x8000000000000000L),
SLOW(0x200000000L, true),
ELEMENTAL_RESET(0x200000000L, true),
MAGIC_SHIELD(0x400000000L, true),
MAGIC_RESISTANCE(0x800000000L, true),
WIND_WALK(0x400000000L, true),
ARAN_COMBO(0x1000000000L, true),
COMBO_DRAIN(0x2000000000L, true),
COMBO_BARRIER(0x4000000000L, true),
BODY_PRESSURE(0x8000000000L, true),
SMART_KNOCKBACK(0x10000000000L, true),
BERSERK(0x20000000000L, true),
ENERGY_CHARGE(0x4000000000000L, true),
DASH2(0x8000000000000L, true), // correct (speed)
DASH(0x10000000000000L, true), // correct (jump)
MONSTER_RIDING(0x20000000000000L, true),
SPEED_INFUSION(0x40000000000000L, true),
BuffStat(long i, boolean isFirst)
BuffStat(long i)
public long getValue()
public boolean isFirst()
public String toString()
```

---

## `org.gms.client` / `client/Character.java`

### 类型声明
```text
class Character
```

- 字段候选数: 163
```text
private int world
private int id
private int accountId
private int level
private int rank
private int rankMove
private int jobRank
private int jobRankMove
private int gender
private int hair
private int face
private int fame
private int questFame
private int initialSpawnPoint
private int mapId
private int currentPage
private int currentType = 0
private int currentTab = 1
private int itemEffect
private int guildId
private int guildRank
private int allianceRank
private int messengerPosition = 4
private int slots = 0
private int energyBar
private int gmLevel
private int ci = 0
private FamilyEntry familyEntry
private int familyId
private int bookCover
private int battleshipHp = 0
private int mesosTraded = 0
private int possibleReports = 10
private int ariantPoints
private int dojoPoints
private int vanquisherStage
private int dojoStage
private int dojoEnergy
private int vanquisherKills
private float expRate = 1
private float mesoRate = 1
private float dropRate = 1
private int expCoupon = 1, mesoCoupon = 1, dropCoupon = 1
private int omokwins
private int omokties
private int omoklosses
private int matchcardwins
private int matchcardties
private int matchcardlosses
private int owlSearch
private long lastfametime
private long lastUsedCashItem
private long lastExpression = 0
private long jailExpiration = -1
private int localchairrate
private boolean hidden
private boolean equipchanged = true, berserk, hasMerchant, hasSandboxItem = false, whiteChat = false
private boolean canRecvPartySearchInvite = true
private boolean equippedMesoMagnet = false
private boolean equippedItemPouch = false
private boolean equippedPetItemIgnore = false
private boolean usedSafetyCharm = false
private int linkedLevel = 0
private String linkedName = null
private boolean finishedDojoTutorial
private boolean usedStorage = false
private String name
private String chalktext
private String commandtext
private String dataString
private String search = null
private long totalExpGained = 0
private int merchantmeso
private BuddyList buddylist
private EventInstanceManager eventInstance = null
private HiredMerchant hiredMerchant = null
private Client client
private GuildCharacter mgc = null
private PartyCharacter mpc = null
private Inventory[] inventory
private Job job = Job.BEGINNER
private Messenger messenger = null
private MiniGame miniGame
private RockPaperScissor rps
private Mount mapleMount
private Party party
private final Pet[] pets = new Pet[3]
private PlayerShop playerShop = null
private Shop shop = null
private SkinColor skinColor = SkinColor.NORMAL
private Storage storage = null
private Trade trade = null
private MonsterBook monsterBook
private CashShop cashShop
private final SavedLocation[] savedLocations
private final SkillMacro[] skillMacros = new SkillMacro[5]
private List<Integer> lastmonthfameids
private byte[] quickSlotLoaded
private QuickslotBinding quickSlotKeyMapped
private Door pdoor = null
private ScheduledFuture<?> dragonBloodSchedule
private ScheduledFuture<?> hpDecreaseTask
private ScheduledFuture<?> skillCooldownTask = null
private ScheduledFuture<?> buffExpireTask = null
private ScheduledFuture<?> itemExpireTask = null
private ScheduledFuture<?> diseaseExpireTask = null
private ScheduledFuture<?> questExpireTask = null
private ScheduledFuture<?> recoveryTask = null
private ScheduledFuture<?> extraRecoveryTask = null
private ScheduledFuture<?> chairRecoveryTask = null
private ScheduledFuture<?> cpqSchedule = null
private ScheduledFuture<?> FamilyBuffTimer = null
private long portaldelay = 0
private volatile long lastTeleportLikeMoveTime = 0
private static final byte MOVEMENT_DISTANCE_CONTEXT_MAX_ATTACK_CHECKS = 1
private Point movementBeforePos = null
private Point movementAfterPos = null
private int movementContextMapId = MapId.NONE
private long movementContextExpireTime = 0L
private byte movementContextRemainingChecks = 0
private long lastCombo = 0
private short combocounter = 0
private AutobanManager autoBan
private boolean banned = false
private boolean blockCashShop = false
private boolean allowExpGain = true
private byte pendantExp = 0, doorSlot = -1
private PartyQuest partyQuest = null
private Dragon dragon = null
private Ring marriageRing
private int marriageItemId = -1
private int partnerId = -1
private boolean loggedIn = false
private long npcCd
private int newWarpMap = -1
private byte extraHpRec = 0, extraMpRec = 0
private short extraRecInterval
private int targetHpBarHash = 0
private long targetHpBarTime = 0
private long nextWarningTime = 0
private int banishMap = -1
private int banishSp = -1
private long banishTime = 0
private long lastExpGainTime
private long loginTime
private boolean chasing = false
private float mobExpRate = -1
private boolean familyBuff = false
private boolean familyParty = false
private float familyExp = 1
private float familyDrop = 1
private long lastAttackTime = 0
private byte team = 0
private Fitness fitness
private Ola ola
private long snowballattack
public AriantColiseum ariantColiseum
private MonsterCarnival monsterCarnival
private MonsterCarnivalParty monsterCarnivalParty = null
private int cp = 0
private int totCP = 0
private int FestivalPoints
private boolean challenged = false
```

- 方法/构造器候选数: 620
```text
private Character()
public Job getJobStyle(byte opt)
public Job getJobStyle()
public static Character getDefault(Client c)
public boolean isLoggedInWorld()
public boolean isAwayFromWorld()
public void setEnteredChannelWorld()
public void setAwayFromChannelWorld()
public void setDisconnectedFromChannelWorld()
private void setAwayFromChannelWorld(boolean disconnect)
public void updatePartySearchAvailability(boolean pSearchAvailable)
public boolean toggleRecvPartySearchInvite()
public boolean isRecvPartySearchInviteEnabled()
public void setSessionTransitionState()
public void setCS(boolean cs)
public long getNpcCooldown()
public void setNpcCooldown(long d)
public void addCooldown(int skillId, long startTime, long length)
public Ring getRingById(int id)
public int getRelationshipId()
public boolean isMarried()
public boolean hasJustMarried()
public int addDojoPointsByMap(int mapId)
public void addMesosTraded(int gain)
public void addPet(Pet pet)
public void addSummon(int id, Summon summon)
public void addVisibleMapObject(MapObject mo)
public void ban(String reason)
public static boolean ban(String id, String reason, boolean accountId)
public int calculateMaxBaseDamage(int watk, WeaponType weapon)
public int calculateMaxBaseDamage(int watk)
public int calculateMaxBaseMagicDamage(int matk)
public void setCombo(short count)
public short getCombo()
public boolean cannotEnterCashShop()
public void toggleBlockCashShop()
public void toggleExpGain()
public void newClient(Client c)
public String getMedalText()
public void hide(boolean hide, boolean login)
public void hide(boolean hide)
public void toggleHide(boolean login)
public void cancelMagicDoor()
private void cancelPlayerBuffs(List<BuffStat> buffstats)
public static boolean canCreateChar(String name)
public static boolean existName(String name)
public boolean canDoor()
public void setHasSandboxItem()
public void removeSandboxItems()
public void changeCI(int type)
public void setMasteries(int jobId)
private void broadcastChangeJob()
public synchronized void changeJob(Job newJob)
public void broadcastAcquaintances(int type, String message)
public void broadcastAcquaintances(Packet packet)
public void changeKeybinding(int key, KeyBinding keybinding)
public void changeQuickslotKeybinding(byte[] aQuickslotKeyMapped)
public void broadcastStance(int newStance)
public void broadcastStance()
public MapleMap getWarpMap(int map)
public void warpAhead(int map)
private void eventChangedMap(int map)
private void eventAfterChangedMap(int map)
public boolean canRecoverLastBanish()
public void clearBanishPlayerData()
public void setBanishPlayerData(int banishMap, int banishSp, long banishTime)
public void changeMapBanish(int mapid, String portal, String msg)
public void changeMap(int map)
public void changeMap(int map, Object pt)
public void changeMap(MapleMap to)
public void changeMap(MapleMap to, int portal)
public void changeMap(final MapleMap target, Portal pto)
public void changeMap(final MapleMap target, final Point pos)
public void forceChangeMap(final MapleMap target, Portal pto)
private boolean buffMapProtection()
public List<Integer> getLastVisitedMapIds()
public void partyOperationUpdate(Party party, List<Character> exPartyMembers)
private static void addPartyPlayerDoor(Character target)
private static void removePartyPlayerDoor(Party party, Character target)
private static void updatePartyTownDoors(Party party, Character target, Character partyLeaver, List<Character> partyMembers)
private Integer getVisitedMapIndex(MapleMap map)
public void visitMap(MapleMap map)
public void setOwnedMap(MapleMap map)
public MapleMap getOwnedMap()
public void notifyMapTransferToPartner(int mapid)
public void removeIncomingInvites()
private void changeMapInternal(final MapleMap to, final Point pos, Packet warpPacket)
public boolean isChangingMaps()
public void setMapTransitionComplete()
public void changePage(int page)
public void changeSkillLevel(Skill skill, byte newLevel, int newMasterlevel, long expiration)
public void changeTab(int tab)
public void changeType(int type)
public void checkBerserk(final boolean isHidden)
public void checkMessenger()
public void controlMonster(Monster monster)
public void stopControllingMonster(Monster monster)
public int getNumControlledMonsters()
public Collection<Monster> getControlledMonsters()
public void releaseControlledMonsters()
public boolean applyConsumeOnPickup(final int itemId)
public final void pickupItem(MapObject ob)
public final void pickupItem(MapObject ob, int petIndex)
public int countItem(int itemid)
public boolean canHold(int itemid)
public boolean canHold(int itemid, int quantity)
public boolean canHoldUniques(List<Integer> itemids)
public boolean isRidingBattleship()
public void announceBattleshipHp()
public void decreaseBattleshipHp(int decrease)
public void decreaseReports()
public void deleteGuild(int guildId)
private void nextPendingRequest(Client c)
private void notifyRemoteChannel(Client c, int remoteChannel, int otherCid, BuddyList.BuddyOperation operation)
public void deleteBuddy(int otherCid)
public static boolean deleteCharFromDB(Character player, int senderAccId)
private static void deleteQuestProgressWhereCharacterId(Connection con, int cid) throws SQLException
private void deleteWhereCharacterId(Connection con, String sql) throws SQLException
private void stopChairTask()
private void updateChairHealStats()
private void startChairTask()
private void stopExtraTask()
private void startExtraTask(final byte healHP, final byte healMP, final short healInterval)
private void startExtraTaskInternal(final byte healHP, final byte healMP, final short healInterval)
public void disbandGuild()
public void dispel()
public final boolean hasDisease(final Disease dis)
public final int getDiseasesSize()
public void silentApplyDiseases(Map<Disease, Pair<Long, MobSkill>> diseaseMap)
public void announceDiseases()
public void collectDiseases()
public void giveDebuff(final Disease disease, MobSkill skill)
public void dispelDebuff(Disease debuff)
public void dispelDebuffs()
public void purgeDebuffs()
public void cancelAllDebuffs()
public void dispelSkill(int skillid)
private static boolean dispelSkills(int skillid)
public void changeFaceExpression(int emote)
public void doHurtHp()
public void dropMessage(String message)
public void dropMessage(int type, String message)
public void enteredScript(String script, int mapid)
public void equipChanged()
public void cancelDiseaseExpireTask()
public void diseaseExpireTask()
public void cancelBuffExpireTask()
public void buffExpireTask()
public void cancelSkillCooldownTask()
public void skillCooldownTask()
public void cancelExpirationTask()
public void expirationTask()
public void forceUpdateItem(Item item)
public void gainGachaExp()
public void addGachaExp(int gain)
public void gainExp(int gain)
public void gainExp(int gain, boolean show, boolean inChat)
public void gainExp(int gain, boolean show, boolean inChat, boolean white)
public void gainExp(int gain, int party, boolean show, boolean inChat, boolean white)
public void loseExp(int loss, boolean show, boolean inChat)
public void loseExp(int loss, boolean show, boolean inChat, boolean white)
private void announceExpGain(long gain, int equip, int party, boolean inChat, boolean white)
private synchronized void gainExpInternal(long gain, int equip, int party, boolean show, boolean inChat, boolean white)
public void gainFame(int delta)
public boolean gainFame(int delta, Character fromPlayer, int mode)
public boolean canHoldMeso(int gain)
public void gainMeso(int gain)
public void gainMeso(int gain, boolean show)
public void gainMeso(int gain, boolean show, boolean enableActions, boolean inChat)
public void genericGuildMessage(int code)
public List<PlayerCoolDownValueHolder> getAllCooldowns()
public void updateAriantScore()
public void updateAriantScore(int dropQty)
public Long getBuffedStarttime(BuffStat effect)
public Integer getBuffedValue(BuffStat effect)
public int getBuffSource(BuffStat stat)
public StatEffect getBuffEffect(BuffStat stat)
private List<BuffStatValueHolder> getAllStatups()
public List<PlayerBuffValueHolder> getAllBuffs()
public boolean hasBuffFromSourceid(int sourceid)
public boolean hasActiveBuff(int sourceid)
private void addItemEffectHolder(Integer sourceid, long expirationtime, Map<BuffStat, BuffStatValueHolder> statups)
private boolean removeEffectFromItemEffectHolder(Integer sourceid, BuffStat buffStat)
private void removeItemEffectHolder(Integer sourceid)
private BuffStatValueHolder fetchBestEffectFromItemEffectHolder(BuffStat mbs)
private void extractBuffValue(int sourceid, BuffStat stat)
public void debugListAllBuffs()
public void cancelAllBuffs(boolean softcancel)
private void dropBuffStats(List<Pair<BuffStat, BuffStatValueHolder>> effectsToCancel)
public void cancelEffect(int itemId)
public boolean cancelEffect(StatEffect effect, boolean overwrite, long startTime)
private static StatEffect getEffectFromBuffSource(Map<BuffStat, BuffStatValueHolder> buffSource)
private boolean isUpdatingEffect(Set<StatEffect> activeEffects, StatEffect mse)
public void updateActiveEffects()
private void updateEffects(Set<BuffStat> removedStats)
private boolean cancelEffect(StatEffect effect, boolean overwrite, long startTime, boolean firstCancel)
public void cancelEffectFromBuffStat(BuffStat stat)
public void cancelBuffStats(BuffStat stat)
private void cancelInactiveBuffStats(Set<BuffStat> retrievedStats, Set<BuffStat> removedStats)
private static List<StatEffect> topologicalSortRemoveLeafStats(Map<StatEffect, Set<BuffStat>> stackedBuffStats, Map<BuffStat, Stack<StatEffect>> buffStack, Map<StatEffect, Integer> leafStatCount)
private static void topologicalSortRebaseLeafStats(Map<StatEffect, Set<BuffStat>> stackedBuffStats, Map<BuffStat, Stack<StatEffect>> buffStack)
private static List<StatEffect> topologicalSortEffects(Map<BuffStat, List<Pair<StatEffect, Integer>>> buffEffects)
private static List<StatEffect> sortEffectsList(Map<StatEffect, Integer> updateEffectsList)
private void propagateBuffEffectUpdates(Map<Integer, Pair<StatEffect, Long>> retrievedEffects, Set<BuffStat> retrievedStats, Set<BuffStat> removedStats)
private static BuffStat getSingletonStatupFromEffect(StatEffect mse)
private static boolean isSingletonStatup(BuffStat mbs)
private static boolean isPriorityBuffSourceId(int sourceId)
private void addItemEffectHolderCount(BuffStat stat)
public void registerEffect(StatEffect effect, long starttime, long expirationtime, boolean isSilent)
private static int getJobMapChair(Job job)
public boolean unregisterChairBuff()
public boolean registerChairBuff()
public int getChair()
public String getChalkboard()
public AbstractPlayerInteraction getAbstractPlayerInteraction()
private List<QuestStatus> getQuestValues()
public final List<QuestStatus> getCompletedQuests()
public List<Ring> getCrushRings()
public Collection<Door> getDoors()
public Door getPlayerDoor()
public Door getMainTownDoor()
public void applyPartyDoor(Door door, boolean partyUpdate)
public Door removePartyDoor(boolean partyUpdate)
private void removePartyDoor(Party formerParty)
public EventInstanceManager getEventInstance()
public Marriage getMarriageInstance()
public void resetExcluded(int petId)
public void addExcluded(int petId, int x)
public void commitExcludedItems()
public void exportExcludedItems(Client c)
public Set<Integer> getExcludedItems()
public int getExp()
public int getGachaExp()
public boolean hasNoviceExpRate()
public float getExpRate()
public float getLevelExpRate()
public float getQuickLevelExpRate()
public void updateMobExpRate()
public float getMobExpRate()
public int getCouponExpRate()
public float getRawExpRate()
public int getCouponDropRate()
public float getRawDropRate()
public float getBossDropRate()
public int getCouponMesoRate()
public float getRawMesoRate()
public float getQuestExpRate()
public float getQuestMesoRate()
public float getCardRate(int itemid)
public Family getFamily()
public void setFamilyEntry(FamilyEntry entry)
public void setUsedStorage()
public List<Ring> getFriendshipRings()
public boolean isMale()
public Guild getGuild()
public Alliance getAlliance()
public static int getAccountIdByName(String name)
public static int getIdByName(String name)
public static String getNameById(int id)
public Inventory getInventory(InventoryType type)
public boolean haveItemWithId(int itemid, boolean checkEquipped)
public boolean haveItemEquipped(int itemid)
public boolean haveWeddingRing()
public int getItemQuantity(int itemid, boolean checkEquipped)
public int getCleanItemQuantity(int itemid, boolean checkEquipped)
public int getJobType()
public int getFh()
public int getMapId()
public Ring getMarriageRing()
public int getMasterLevel(int skill)
public int getMasterLevel(Skill skill)
public int getTotalStr()
public int getTotalDex()
public int getTotalInt()
public int getTotalLuk()
public int getTotalMagic()
public int getTotalWatk()
public int getMaxClassLevel()
public int getMaxLevel()
public int getMeso()
public void setMeso(int meso)
public int getMerchantMeso()
public int getMerchantNetMeso()
public GuildCharacter getMGC()
public void setMGC(GuildCharacter mgc)
public PartyCharacter getMPC()
public void setMPC(PartyCharacter mpc)
public void setPlayerAggro(int mobHash)
public void resetPlayerAggro()
public int getMiniGamePoints(MiniGameResult type, boolean omok)
public int getMonsterBookCover()
public int getNoPets()
public Party getParty()
public int getPartyId()
public List<Character> getPartyMembersOnline()
public List<Character> getPartyMembersOnSameMap()
public boolean isPartyMember(Character chr)
public boolean isPartyMember(int cid)
public void setGMLevel(int level)
public void closePartySearchInteractions()
public void closePlayerInteractions()
public void closeNpcShop()
public void closeTrade()
public void closePlayerShop()
public void closeMiniGame(boolean forceClose)
public void closeHiredMerchant(boolean closeMerchant)
public void closePlayerMessenger()
public Pet[] getPets()
public Pet getPet(int index)
public byte getPetIndex(int petId)
public byte getPetIndex(Pet pet)
public final byte getQuestStatus(final int quest)
public QuestStatus getQuest(final int quest)
public QuestStatus getQuest(Quest quest)
public final QuestStatus getQuestNAdd(final Quest quest)
public final QuestStatus getQuestNoAdd(final Quest quest)
public boolean needQuestItem(int questid, int itemid)
public void clearSavedLocation(SavedLocationType type)
public int peekSavedLocation(String type)
public int getSavedLocation(String type)
public int getSkillLevel(int skill)
public byte getSkillLevel(Skill skill)
public long getSkillExpiration(int skill)
public long getSkillExpiration(Skill skill)
public int getSlot()
public final List<QuestStatus> getStartedQuests()
public StatEffect getStatForBuff(BuffStat effect)
public Collection<Summon> getSummonsValues()
public void clearSummons()
public Summon getSummonByKey(int id)
public boolean isSummonsEmpty()
public boolean containsSummon(Summon summon)
public MapObject[] getVisibleMapObjects()
public World getWorldServer()
public void giveCoolDowns(final int skillid, long starttime, long length)
public int gmLevel()
private void guildUpdate()
public void handleEnergyChargeGain()
public void handleOrbconsume()
public boolean hasEntered(String script)
public boolean hasEntered(String script, int mapId)
public void hasGivenFame(Character to)
public boolean hasMerchant()
public boolean haveItem(int itemid)
public boolean haveCleanItem(int itemid)
public boolean hasEmptySlot(int itemId)
public boolean hasEmptySlot(byte invType)
public void increaseGuildCapacity()
private static String getTimeRemaining(long timeLeft)
public boolean isBuffFrom(BuffStat stat, Skill skill)
public boolean isGmJob()
public boolean isCygnus()
public boolean isAran()
public boolean isBeginnerJob()
public boolean isGM()
public boolean isMapObjectVisible(MapObject mo)
public boolean isPartyLeader()
public boolean isGuildLeader()
public boolean attemptCatchFish(int baitLevel)
public void leaveMap()
private int getChangedJobSp(Job newJob)
private int getUsedSp(Job job)
private int getJobLevelSp(int level, Job job, int jobBranch)
private int getJobMaxSp(Job job)
private int getJobRemainingSp(Job job)
private int getSpGain(int spGain, Job job)
private int getSpGain(int spGain, int curSp, Job job)
private void levelUpGainSp()
public synchronized void levelUp(boolean takeexp)
public boolean leaveParty()
public void setPlayerRates()
public void revertLastPlayerRates()
public void revertPlayerRates()
public void setWorldRates()
public void revertWorldRates()
private void applySavedRateOrElse(String type, Runnable runnable)
public void setCouponRates()
private void revertCouponRates()
public void updateCouponRates()
public void resetPlayerRates()
private int getCouponMultiplier(int couponId)
private void setExpCouponRate(int couponId, int couponQty)
private void setDropCouponRate(int couponId, int couponQty)
private void revertCouponsEffects()
private List<Integer> activateCouponsEffects()
private void setActiveCoupons(Collection<Item> cashItems)
private void commitBuffCoupon(int couponid)
public void dispelBuffCoupons()
public Set<Integer> getActiveCoupons()
public void addPlayerRing(Ring ring)
public static Character loadCharacterEntryFromDB(ResultSet rs, List<Item> equipped)
public Character generateCharacterEntry()
private void loadCharSkillPoints(String[] skillPoints)
public int getRemainingSp()
public void updateRemainingSp(int remainingSp)
public static Character fromCharactersDO(CharactersDO charactersDO, Client client)
public static CharactersDO toCharactersDO(Character chr)
public static Character loadCharFromDB(final int cid, Client client, boolean channelServer)
public void reloadQuestExpirations()
public static String makeMapleReadable(String in)
public void message(String m)
public void yellowMessage(String m)
public void raiseQuestMobCount(int id)
public Mount mount(int id, int skillid)
private void playerDead()
private void unsitChairInternal()
public void sitChair(int itemId)
private void setChair(int chair)
public void respawn(int returnMap)
public void respawn(EventInstanceManager eim, int returnMap)
private void prepareDragonBlood(final StatEffect bloodEffect)
private void recalcEquipStats()
public void reapplyLocalStats()
private void updateLocalStats()
public void receivePartyMemberHP()
public void removeAllCooldownsExcept(int id, boolean packet)
public void removeCooldown(int skillId)
public void removePet(Pet pet, boolean shift_left)
public void removeVisibleMapObject(MapObject mo)
public synchronized void resetStats()
public void resetBattleshipHp()
public void resetEnteredScript()
public void resetEnteredScript(int mapId)
public void resetEnteredScript(String script)
public synchronized void saveCooldowns()
public void saveGuildStatus()
public void saveLocationOnWarp()
public void saveLocation(String type)
public final boolean insertNewChar(CharacterFactoryRecipe recipe)
public void saveCharToDB()
public synchronized void saveCharToDB(boolean notAutosave)
public void sendPolice(int greason, String reason, int duration)
public void sendPolice(String text)
public void sendKeymap()
public void sendQuickmap()
public void sendMacros()
public void setBuddyCapacity(int capacity)
public void setBuffedValue(BuffStat effect, int value)
public void setChalkboard(String text)
public void setDojoEnergy(int x)
public void setEventInstance(EventInstanceManager eventInstance)
public void setExp(int amount)
public void setGachaExp(int exp)
public void finishDojoTutorial()
public void setGM(int level)
public void setHasMerchant(boolean set)
public void addMerchantMesos(int add)
public void setMerchantMeso(int set)
public synchronized void withdrawMerchantMesos()
public void hpChangeAction(int oldHp)
private static int calcTransientRatio(float transientpoint)
private int calcHpRatioUpdate(int curpoint, int maxpoint, int diffpoint)
private int calcMpRatioUpdate(int curpoint, int maxpoint, int diffpoint)
public boolean applyHpMpChange(int hpCon, int hpchange, int mpchange)
public void setMap(int PmapId)
public void setMiniGamePoints(Character visitor, int winnerslot, boolean omok)
public void setRPS(RockPaperScissor rps)
public void closeRPS()
public int getDoorSlot()
public int fetchDoorSlot()
public void setParty(Party p)
public byte getSlots(int type)
public boolean canGainSlots(int type, int slots)
public boolean gainSlots(int type, int slots)
public boolean gainSlots(int type, int slots, boolean update)
private int gainSlotsInternal(int type, int slots)
public int sellAllItemsFromName(byte invTypeId, String name)
public int sellAllItemsFromPosition(ItemInformationProvider ii, InventoryType type, short pos)
private int standaloneSell(Client c, ItemInformationProvider ii, InventoryType type, short slot, short quantity)
private static boolean hasMergeFlag(Item item)
private static void setMergeFlag(Item item)
private List<Equip> getUpgradeableEquipped()
private static List<Equip> getEquipsWithStat(List<Pair<Equip, Map<StatUpgrade, Short>>> equipped, StatUpgrade stat)
public boolean mergeAllItemsFromName(String name)
public void mergeAllItemsFromPosition(Map<StatUpgrade, Float> statUps, short pos)
private void standaloneMerge(Map<StatUpgrade, Float> statUps, Client c, InventoryType type, short slot, Item item)
public void setSlot(int slotid)
public void shiftPetsRight()
private long getDojoTimeLeft()
public void showDojoClock()
public void showUnderLeveledInfo(Monster mob)
public void showMapOwnershipInfo(Character mapOwner)
public void showHint(String msg)
public void showHint(String msg, int length)
public void silentGiveBuffs(List<Pair<Long, PlayerBuffValueHolder>> buffs)
public void silentPartyUpdate()
private void silentPartyUpdateInternal(Party chrParty)
public boolean skillIsCooling(int skillId)
public void runFullnessSchedule(int petSlot)
public boolean runTirednessSchedule()
public void startMapEffect(String msg, int itemId)
public void startMapEffect(String msg, int itemId, int duration)
public void unEquipAllPets()
public void unEquipPet(Pet pet, boolean shift_left)
public void unEquipPet(Pet pet, boolean shift_left, boolean hunger)
public void updateMacros(int position, SkillMacro updateMacro)
public void updatePartyMemberHP()
private void updatePartyMemberHPInternal()
public void setQuestProgress(int id, int infoNumber, String progress)
public void awardQuestPoint(int awardedPoints)
private void announceUpdateQuestInternal(Character chr, Pair<DelayedQuestUpdate, Object[]> questUpdate)
public void announceUpdateQuest(DelayedQuestUpdate questUpdateType, Object... params)
public void flushDelayedUpdateQuests()
public void updateQuestStatus(QuestStatus qs)
public void cancelQuestExpirationTask()
public void forfeitExpirableQuests()
public void questExpirationTask()
private void runQuestExpireTask()
private void registerQuestExpire(Quest quest, long time)
public void questTimeLimit(final Quest quest, int seconds)
public void questTimeLimit2(final Quest quest, long expires)
public void updateSingleStat(Stat stat, int newval)
private void updateSingleStat(Stat stat, int newval, boolean itemReaction)
public void sendPacket(Packet packet)
public int getObjectId()
public MapObjectType getType()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public void setObjectId(int id)
public String toString()
public Set<NewYearCardRecord> getNewYearRecords()
public Set<NewYearCardRecord> getReceivedNewYearRecords()
public NewYearCardRecord getNewYearRecord(int cardid)
public void addNewYearRecord(NewYearCardRecord newyear)
public void removeNewYearRecord(NewYearCardRecord newyear)
public void portalDelay(long delay)
public long portalDelay()
public void markTeleportLikeMove()
public synchronized void markTeleportLikeMove(Point beforePos, Point afterPos)
public synchronized void markRegularMove(Point beforePos, Point afterPos)
public long getLastTeleportLikeMoveTime()
public synchronized Point getTeleportBeforePositionForDistanceCheck()
public synchronized Point getMovementBeforePositionForDistanceCheck()
public synchronized void consumeTeleportDistanceCheckContext()
public synchronized void consumeMovementDistanceCheckContext()
public synchronized void clearTeleportDistanceContext()
private boolean isTeleportDistanceContextActiveLocked(long now)
private boolean isMovementDistanceContextActiveLocked(long now)
private void clearTeleportDistanceContextLocked()
private void clearMovementDistanceContextLocked()
private static boolean shouldBuildTeleportDistanceContext(Point beforePos, Point afterPos)
private static boolean shouldBuildMovementDistanceContext(Point beforePos, Point afterPos)
private static Point copyPoint(Point pos)
private static long monotonicNow()
public void blockPortal(String scriptName)
public void unblockPortal(String scriptName)
public boolean containsAreaInfo(int area, String info)
public void updateAreaInfo(int area, String info)
public void autoBan(String reason)
public void block(int reason, int days, String desc)
public List<Integer> getTrockMaps()
public List<Integer> getVipTrockMaps()
public int getTrockSize()
public void deleteFromTrocks(int map)
public void addTrockMap()
public boolean isTrockMap(int id)
public int getVipTrockSize()
public void deleteFromVipTrocks(int map)
public void addVipTrockMap()
public boolean isVipTrockMap(int id)
public AutobanManager getAutoBanManager()
public void setAutoBanManager(AutobanManager autoBan)
public void equippedItem(Equip equip)
public void unequippedItem(Equip equip)
private void equipPendantOfSpirit()
private void unequipPendantOfSpirit()
private Collection<Item> getUpgradeableEquipList()
public void increaseEquipExp(int expGain)
public void showAllEquipFeatures()
public void broadcastMarriageMessage()
public void setCpqTimer(ScheduledFuture<?> timer)
public void clearCpqTimer()
public final void empty(final boolean remove)
public void logOff()
public long getLoggedInTime()
public boolean getWhiteChat()
public void toggleWhiteChat()
public boolean gotPartyQuestItem(String partyquestchar)
public void removePartyQuestItem(String letter)
public void setPartyQuestItemObtained(String partyquestchar)
public void createDragon()
public long getJailExpirationTimeLeft()
private void setFutureJailExpiration(long time)
public void addJailExpirationTime(long time)
public void removeJailExpirationTime()
public boolean registerNameChange(String newName)
public boolean cancelPendingNameChange()
public void doPendingNameChange()
public int checkWorldTransferEligibility()
public boolean registerWorldTransfer(int newWorld)
public boolean cancelPendingWorldTransfer()
public String getLastCommandMessage()
public void setLastCommandMessage(String text)
public int getRewardPoints()
public void setRewardPoints(int value)
public void setReborns(int value)
public void addReborns()
public int getReborns()
public void executeRebornAsId(int jobId)
public void executeRebornAs(Job job)
public void setTeam(int team)
public long getLastSnowballAttack()
public void setLastSnowballAttack(long time)
public void gainFestivalPoints(int gain)
public int getCP()
public void gainCP(int gain)
public void setTotalCP(int a)
public void setCP(int a)
public int getTotalCP()
public void resetCP()
public void gainAriantPoints(int points)
public void gainEquip(int itemId, Short attStr, Short attDex, Short attInt, Short attLuk, Short attHp, Short attMp, Short pAtk, Short mAtk, Short pDef, Short mDef, Short acc, Short avoid, Short hands, Short speed, Short jump, Byte upgradeSlot, Long expireTime)
public void setFamilyBuff(boolean type, float exp, float drop)
public void startFamilyBuffTimer(int delay)
public void cancelFamilyBuffTimer()
public int getCurrentOnlineTime()
public void setCurrentOnlineTime(final int iTime)
public void updateOnlineTime()
public MapleMap getMap(int mapid, boolean showMsg)
public void enableActions()
```

---

## `org.gms.client` / `client/CharacterListener.java`

### 类型声明
```text
class CharacterListener
```

- 字段候选数: 1
```text
private final Character character
```

- 方法/构造器候选数: 5
```text
public CharacterListener(Character character)
public void onHpChanged(int oldHp)
public void onHpMpPoolUpdate()
public void onStatUpdate()
public void onAnnounceStatPoolUpdate()
```

---

## `org.gms.client` / `client/CharacterNameAndId.java`

### 类型声明
```text
class CharacterNameAndId
```

- 字段候选数: 2
```text
private final int id
private final String name
```

- 方法/构造器候选数: 3
```text
public CharacterNameAndId(int id, String name)
public int getId()
public String getName()
```

---

## `org.gms.client` / `client/Client.java`

### 类型声明
```text
class Client
enum Type
```

- 字段候选数: 36
```text
public static final int LOGIN_NOTLOGGEDIN = 0
public static final int LOGIN_SERVER_TRANSITION = 1
public static final int LOGIN_LOGGEDIN = 2
private final Type type
private final long sessionId
private final PacketProcessor packetProcessor
private Hwid hwid
private String remoteAddress
private volatile boolean inTransition
private io.netty.channel.Channel ioChannel
private Character player
private int channel = 1
private int accId = -4
private boolean loggedIn = false
private boolean serverTransition = false
private Calendar birthday = null
private String accountName = null
private int world
private volatile long lastPong
private int gmlevel
private byte characterSlots = 3
private byte loginattempt = 0
private String pin = ""
private int pinattempt = 0
private String pic = ""
private int picattempt = 0
private byte csattempt = 0
private byte gender = -1
private boolean disconnecting = false
private Calendar tempBanCalendar
private int votePoints
private int voteTime = -1
private int visibleWorlds
private long lastNpcClick
private int lang = 0
private static SystemRescue sysRescue
```

- 方法/构造器候选数: 131
```text
public Client(Type type, long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createLoginClient(long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createChannelClient(long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createMock()
public void channelActive(ChannelHandlerContext ctx)
private static String getRemoteAddress(io.netty.channel.Channel channel)
public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception
public void userEventTriggered(ChannelHandlerContext ctx, Object event)
public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception
public void channelInactive(ChannelHandlerContext ctx)
private void closeMapleSession()
public void updateLastPacket()
public long getLastPacket()
public void closeSession()
public void disconnectSession()
public Hwid getHwid()
public void setHwid(Hwid hwid)
public String getRemoteAddress()
public boolean isInTransition()
public EventManager getEventManager(String event)
public Character getPlayer()
public void setPlayer(Character player)
public AbstractPlayerInteraction getAbstractPlayerInteraction()
public void sendCharList(int server)
public List<Character> loadCharacters(int serverId)
public List<String> loadCharacterNames(int worldId)
private List<CharNameAndId> loadCharactersInternal(int worldId)
public boolean isLoggedIn()
public boolean hasBannedIP()
public int getVoteTime()
public void resetVoteTime()
public boolean hasVotedAlready()
public boolean hasBannedHWID()
public boolean hasBannedMac()
private void loadHWIDIfNescessary() throws SQLException
private void loadMacsIfNescessary() throws SQLException
public void banHWID()
public void banMacs()
public int finishLogin()
public void setPin(String pin)
public String getPin()
public boolean checkPin(String other)
public void setPic(String pic)
public String getPic()
public boolean checkPic(String other)
public int login(String login, String pwd, Hwid hwid)
public Calendar getTempBanCalendarFromDB()
public Calendar getTempBanCalendar()
public boolean hasBeenBanned()
public static long dottedQuadToLong(String dottedQuad) throws RuntimeException
public void updateHwid(Hwid hwid)
public void updateMacs(String macData)
public void setAccID(int id)
public int getAccID()
public void updateLoginState(int newState)
public int getLoginState()
public boolean checkBirthDate(Calendar date)
private void removePartyPlayer(World wserv)
private void removePlayer(World wserv, boolean serverTransition)
public final void disconnect(final boolean shutdown, final boolean cashshop)
public final void forceDisconnect()
public void timeoutDisconnect()
private synchronized boolean canDisconnect()
private void disconnectInternal(boolean shutdown, boolean cashshop)
private void clear()
public void setCharacterOnSessionTransitionState(int cid)
public int getChannel()
public Channel getChannelServer()
public World getWorldServer()
public Channel getChannelServer(byte channel)
public boolean deleteCharacter(int cid, int senderAccId)
public String getAccountName()
public void setAccountName(String a)
public void setChannel(int channel)
public int getWorld()
public void setWorld(int world)
public void pongReceived()
public void checkIfIdle(final IdleStateEvent event)
public Set<String> getMacs()
public int getGMLevel()
public void setGMLevel(int level)
public void setScriptEngine(String name, ScriptEngine e)
public ScriptEngine getScriptEngine(String name)
public void removeScriptEngine(String name)
public NPCConversationManager getCM()
public QuestActionManager getQM()
public boolean acceptToS()
public void checkChar(int accid)
public int getVotePoints()
public void addVotePoints(int points)
public void useVotePoints(int points)
private void saveVotePoints()
public void lockClient()
public void unlockClient()
public boolean tryacquireClient()
public void releaseClient()
public boolean tryacquireEncoder()
public void unlockEncoder()
private static boolean checkHash(String hash, String type, String password)
public short getAvailableCharacterSlots()
public short getAvailableCharacterWorldSlots()
public short getAvailableCharacterWorldSlots(int world)
public short getCharacterSlots()
public void setCharacterSlots(byte slots)
public boolean canGainCharacterSlot()
public synchronized boolean gainCharacterSlot()
public final byte getGReason()
public byte getGender()
public void setGender(byte m)
private void announceDisableServerMessage()
public void announceServerMessage()
public synchronized void announceBossHpBar(Monster mm, final int mobHash, Packet packet)
public void sendPacket(Packet packet)
public void announceHint(String msg, int length)
public void changeChannel(int channel)
public long getSessionId()
public boolean canRequestCharlist()
public boolean canClickNPC()
public void setClickedNPC()
public void removeClickedNPC()
public int getVisibleWorlds()
public void requestedServerlist(int worlds)
public void closePlayerScriptInteractions()
public boolean attemptCsCoupon()
public void resetCsCoupon()
public void enableCSActions()
public boolean canBypassPin()
public boolean canBypassPic()
public int getLanguage()
public void setLanguage(int lingua)
public void enableActions()
```

---

## `org.gms.client` / `client/DefaultDates.java`

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private DefaultDates()
public static LocalDate getBirthday()
public static LocalDateTime getTempban()
```

---

## `org.gms.client` / `client/Disease.java`

### 类型声明
```text
enum Disease
```

- 字段候选数: 2
```text
private final long i
private final MobSkillType mobSkillType
```

- 方法/构造器候选数: 19
```text
NULL(0x0),
SLOW(0x1, MobSkillType.SLOW),
SEDUCE(0x80, MobSkillType.SEDUCE),
FISHABLE(0x100),
ZOMBIFY(0x4000),
CONFUSE(0x80000, MobSkillType.REVERSE_INPUT),
STUN(0x2000000000000L, MobSkillType.STUN),
POISON(0x4000000000000L, MobSkillType.POISON),
SEAL(0x8000000000000L, MobSkillType.SEAL),
DARKNESS(0x10000000000000L, MobSkillType.DARKNESS),
WEAKEN(0x4000000000000000L, MobSkillType.WEAKNESS),
Disease(long i)
Disease(long i, MobSkillType skill)
public long getValue()
public boolean isFirst()
public MobSkillType getMobSkillType()
public static Disease ordinal(int ord)
public static final Disease getRandom()
public static final Disease getBySkill(MobSkillType skill)
```

---

## `org.gms.client` / `client/DiseaseValueHolder.java`

### 类型声明
```text
class DiseaseValueHolder
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public DiseaseValueHolder(long start, long length)
```

---

## `org.gms.client` / `client/Family.java`

### 类型声明
```text
class Family
```

- 字段候选数: 4
```text
private FamilyEntry leader
private String name
private String preceptsMessage = ""
private int totalGenerations
```

- 方法/构造器候选数: 23
```text
public Family(int id, int world)
private static boolean idInUse(int id)
public int getID()
public int getWorld()
public void setLeader(FamilyEntry leader)
public FamilyEntry getLeader()
private void setName(String name)
public int getTotalMembers()
public int getTotalGenerations()
public void setTotalGenerations(int generations)
public String getName()
public void setMessage(String message, boolean save)
public String getMessage()
public void addEntry(FamilyEntry entry)
public void removeEntryBranch(FamilyEntry root)
public void addEntryTree(FamilyEntry root)
public FamilyEntry getEntryByID(int cid)
public void broadcast(Packet packet)
public void broadcast(Packet packet, int ignoreID)
public void Familybuff(int duration)
public void broadcastFamilyInfoUpdate()
public void resetDailyReps()
public void saveAllMembersRep()
```

---

## `org.gms.client` / `client/FamilyEntitlement.java`

### 类型声明
```text
enum FamilyEntitlement
```

- 字段候选数: 0

- 方法/构造器候选数: 15
```text
FAMILY_REUINION(1, 300, I18nUtil.getMessage("FamilyEntitlement.message1"), I18nUtil.getMessage("FamilyEntitlement.message2")),
SUMMON_FAMILY(1, 500, I18nUtil.getMessage("FamilyEntitlement.message3"), I18nUtil.getMessage("FamilyEntitlement.message4")),
SELF_DROP_1_5(1, 700, I18nUtil.getMessage("FamilyEntitlement.message5"), I18nUtil.getMessage("FamilyEntitlement.message6")),
SELF_EXP_1_5(1, 800, I18nUtil.getMessage("FamilyEntitlement.message7"), I18nUtil.getMessage("FamilyEntitlement.message8")),
FAMILY_BONDING(1, 1000, I18nUtil.getMessage("FamilyEntitlement.message9"), I18nUtil.getMessage("FamilyEntitlement.message10")),
SELF_DROP_2(1, 1200, I18nUtil.getMessage("FamilyEntitlement.message11"), I18nUtil.getMessage("FamilyEntitlement.message12")),
SELF_EXP_2(1, 1500, I18nUtil.getMessage("FamilyEntitlement.message13"), I18nUtil.getMessage("FamilyEntitlement.message14")),
SELF_DROP_2_30MIN(1, 2000, I18nUtil.getMessage("FamilyEntitlement.message15"), I18nUtil.getMessage("FamilyEntitlement.message16")),
SELF_EXP_2_30MIN(1, 2500, I18nUtil.getMessage("FamilyEntitlement.message17"), I18nUtil.getMessage("FamilyEntitlement.message18")),
PARTY_DROP_2_30MIN(1, 4000, I18nUtil.getMessage("FamilyEntitlement.message19"), I18nUtil.getMessage("FamilyEntitlement.message20")),
FamilyEntitlement(int usageLimit, int repCost, String name, String description)
public int getUsageLimit()
public int getRepCost()
public String getName()
public String getDescription()
```

---

## `org.gms.client` / `client/FamilyEntry.java`

### 类型声明
```text
class FamilyEntry
```

- 字段候选数: 10
```text
private final int characterID
private volatile Family family
private volatile Character character
private volatile FamilyEntry senior
private final FamilyEntry[] juniors = new FamilyEntry[2]
private final int[] entitlements = new int[11]
private volatile int generation
private String charName
private int level
private Job job
```

- 方法/构造器候选数: 53
```text
public FamilyEntry(Family family, int characterID, String charName, int level, Job job)
public Character getChr()
public void setCharacter(Character newCharacter)
private void cacheOffline(Character chr)
public synchronized void join(FamilyEntry senior)
public synchronized void fork()
private synchronized boolean updateNewFamilyDB(Connection con)
private static boolean updateFamilyEntryDB(Connection con, int cid, int familyid)
private synchronized void addSeniorCount(int seniorCount, Family newFamily)
private synchronized void addJuniorCount(int juniorCount)
public Family getFamily()
public int getChrId()
public String getName()
public int getLevel()
public Job getJob()
public int getReputation()
public int getTodaysRep()
public void setReputation(int reputation)
public void setTodaysRep(int today)
public int getRepsToSenior()
public void setRepsToSenior(int reputation)
public void gainReputation(int gain, boolean countTowardsTotal)
private void gainReputation(int gain, boolean countTowardsTotal, FamilyEntry from)
public void giveReputationToSenior(int gain, boolean includeSuperSenior)
public int getTotalReputation()
public void setTotalReputation(int totalReputation)
public FamilyEntry getSenior()
public synchronized boolean setSenior(FamilyEntry senior, boolean save)
private static boolean updateDBChangeFamily(int cid, int familyid, int seniorid)
private static boolean updateDBChangeFamily(Connection con, int cid, int familyid, int seniorid)
private static boolean updateCharacterFamilyDB(Connection con, int charid, int familyid, boolean fork)
public List<FamilyEntry> getJuniors()
public FamilyEntry getOtherJunior(FamilyEntry junior)
public int getJuniorCount()
public synchronized boolean addJunior(FamilyEntry newJunior)
public synchronized boolean isJunior(FamilyEntry entry)
public synchronized boolean removeJunior(FamilyEntry junior)
public int getTotalSeniors()
public void setTotalSeniors(int totalSeniors)
public int getTotalJuniors()
public void setTotalJuniors(int totalJuniors)
public void announceToSenior(Packet packet, boolean includeSuperSenior)
public void updateSeniorFamilyInfo(boolean includeSuperSenior)
public synchronized void doFullCount()
public boolean useEntitlement(FamilyEntitlement entitlement)
public boolean refundEntitlement(FamilyEntitlement entitlement)
public boolean isEntitlementUsed(FamilyEntitlement entitlement)
public int getEntitlementUsageCount(FamilyEntitlement entitlement)
public void setEntitlementUsed(int id)
public void resetEntitlementUsages()
public boolean saveReputation()
public boolean saveReputation(Connection con)
public void savedSuccessfully()
```

---

## `org.gms.client` / `client/Job.java`

### 类型声明
```text
enum Job
```

- 字段候选数: 2
```text
private final int id
private final String name
```

- 方法/构造器候选数: 36
```text
BEGINNER(0, I18nUtil.getMessage("job.name.0")),
WARRIOR(100, I18nUtil.getMessage("job.name.100")),
FIGHTER(110, I18nUtil.getMessage("job.name.110")), CRUSADER(111, I18nUtil.getMessage("job.name.111")), HERO(112, I18nUtil.getMessage("job.name.112")),
PAGE(120, I18nUtil.getMessage("job.name.120")), WHITEKNIGHT(121, I18nUtil.getMessage("job.name.121")), PALADIN(122,  I18nUtil.getMessage("job.name.122")),
SPEARMAN(130,  I18nUtil.getMessage("job.name.130")), DRAGONKNIGHT(131,  I18nUtil.getMessage("job.name.131")), DARKKNIGHT(132, I18nUtil.getMessage("job.name.132")),
MAGICIAN(200, I18nUtil.getMessage("job.name.200")),
FP_WIZARD(210, I18nUtil.getMessage("job.name.210")), FP_MAGE(211, I18nUtil.getMessage("job.name.211")), FP_ARCHMAGE(212, I18nUtil.getMessage("job.name.212")),
IL_WIZARD(220, I18nUtil.getMessage("job.name.220")), IL_MAGE(221, I18nUtil.getMessage("job.name.221")), IL_ARCHMAGE(222, I18nUtil.getMessage("job.name.222")),
CLERIC(230, I18nUtil.getMessage("job.name.230")), PRIEST(231, I18nUtil.getMessage("job.name.231")), BISHOP(232, I18nUtil.getMessage("job.name.232")),
BOWMAN(300, I18nUtil.getMessage("job.name.300")),
HUNTER(310, I18nUtil.getMessage("job.name.310")), RANGER(311, I18nUtil.getMessage("job.name.311")), BOWMASTER(312, I18nUtil.getMessage("job.name.312")),
CROSSBOWMAN(320, I18nUtil.getMessage("job.name.320")), SNIPER(321, I18nUtil.getMessage("job.name.321")), MARKSMAN(322, I18nUtil.getMessage("job.name.322")),
THIEF(400, I18nUtil.getMessage("job.name.400")),
ASSASSIN(410,I18nUtil.getMessage("job.name.410")), HERMIT(411, I18nUtil.getMessage("job.name.411")), NIGHTLORD(412, I18nUtil.getMessage("job.name.412")),
BANDIT(420, I18nUtil.getMessage("job.name.420")), CHIEFBANDIT(421, I18nUtil.getMessage("job.name.421")), SHADOWER(422, I18nUtil.getMessage("job.name.422")),
PIRATE(500, I18nUtil.getMessage("job.name.500")),
BRAWLER(510, I18nUtil.getMessage("job.name.510")), MARAUDER(511, I18nUtil.getMessage("job.name.511")), BUCCANEER(512, I18nUtil.getMessage("job.name.512")),
GUNSLINGER(520, I18nUtil.getMessage("job.name.520")), OUTLAW(521, I18nUtil.getMessage("job.name.521")), CORSAIR(522, I18nUtil.getMessage("job.name.522")),
MAPLELEAF_BRIGADIER(800, I18nUtil.getMessage("job.name.800")),
GM(900, I18nUtil.getMessage("job.name.900")), SUPERGM(910, I18nUtil.getMessage("job.name.910")),
NOBLESSE(1000, I18nUtil.getMessage("job.name.1000")),
DAWNWARRIOR1(1100, I18nUtil.getMessage("job.name.1100")), DAWNWARRIOR2(1110, I18nUtil.getMessage("job.name.1110")), DAWNWARRIOR3(1111, I18nUtil.getMessage("job.name.1111")), DAWNWARRIOR4(1112, I18nUtil.getMessage("job.name.1112")),
BLAZEWIZARD1(1200, I18nUtil.getMessage("job.name.1200")), BLAZEWIZARD2(1210, I18nUtil.getMessage("job.name.1210")), BLAZEWIZARD3(1211,I18nUtil.getMessage("job.name.1211")), BLAZEWIZARD4(1212,I18nUtil.getMessage("job.name.1212")),
WINDARCHER1(1300,I18nUtil.getMessage("job.name.1300")), WINDARCHER2(1310, I18nUtil.getMessage("job.name.1310")), WINDARCHER3(1311, I18nUtil.getMessage("job.name.1311")), WINDARCHER4(1312, I18nUtil.getMessage("job.name.1312")),
NIGHTWALKER1(1400,I18nUtil.getMessage("job.name.1400")), NIGHTWALKER2(1410,I18nUtil.getMessage("job.name.1410")), NIGHTWALKER3(1411,I18nUtil.getMessage("job.name.1411")), NIGHTWALKER4(1412,I18nUtil.getMessage("job.name.1412")),
THUNDERBREAKER1(1500,I18nUtil.getMessage("job.name.1500")), THUNDERBREAKER2(1510,I18nUtil.getMessage("job.name.1510")), THUNDERBREAKER3(1511,I18nUtil.getMessage("job.name.1511")), THUNDERBREAKER4(1512,I18nUtil.getMessage("job.name.1512")),
LEGEND(2000, I18nUtil.getMessage("job.name.2000")), EVAN(2001, I18nUtil.getMessage("job.name.2001")),
ARAN1(2100, I18nUtil.getMessage("job.name.2100")), ARAN2(2110, I18nUtil.getMessage("job.name.2110")), ARAN3(2111, I18nUtil.getMessage("job.name.2111")), ARAN4(2112, I18nUtil.getMessage("job.name.2112")),
EVAN1(2200,I18nUtil.getMessage("job.name.2200")), EVAN2(2210, I18nUtil.getMessage("job.name.2210")), EVAN3(2211, I18nUtil.getMessage("job.name.2211")), EVAN4(2212, I18nUtil.getMessage("job.name.2212")), EVAN5(2213, I18nUtil.getMessage("job.name.2213")), EVAN6(2214, I18nUtil.getMessage("job.name.2214")),
Job(int id, String name)
public static int getMax()
public static Job getById(int id)
public static Job getBy5ByteEncoding(int encoded)
public boolean isA(Job basejob)
public int getJobNiche()
public static Job getJobStyleInternal(int jobid, byte opt)
```

---

## `org.gms.client` / `client/MonsterBook.java`

### 类型声明
```text
class MonsterBook
```

- 字段候选数: 3
```text
private int specialCard = 0
private int normalCard = 0
private int bookLevel = 1
```

- 方法/构造器候选数: 10
```text
public MonsterBook(int cid)
public void addCard(final Client c, final int cardid)
private void calculateLevel()
public int getBookLevel()
public int getTotalCards()
public int getNormalCard()
public int getSpecialCard()
public void loadCards(final int chrId)
public void saveCards(Connection con, int chrId) throws SQLException
public static int[] getCardTierSize()
```

---

## `org.gms.client` / `client/Mount.java`

### 类型声明
```text
class Mount
```

- 字段候选数: 7
```text
private int itemid
private int skillid
private int tiredness
private int exp
private int level
private Character owner
private boolean active
```

- 方法/构造器候选数: 16
```text
public Mount(Character owner, int id, int skillid)
public int getItemId()
public int getSkillId()
public int getId()
public int getTiredness()
public int getExp()
public int getLevel()
public void setTiredness(int newtiredness)
public int incrementAndGetTiredness()
public void setExp(int newexp)
public void setLevel(int newlevel)
public void setItemId(int newitemid)
public void setSkillId(int newskillid)
public void setActive(boolean set)
public boolean isActive()
public void empty()
```

---

## `org.gms.client` / `client/QuestStatus.java`

### 类型声明
```text
class QuestStatus
enum Status
```

- 字段候选数: 5
```text
private final short questID
private Status status
private int npc
private int forfeited = 0, completed = 0
private String customData
```

- 方法/构造器候选数: 32
```text
public QuestStatus(Quest quest, Status status)
public QuestStatus(Quest quest, Status status, int npc)
public Quest getQuest()
public short getQuestID()
public Status getStatus()
public final void setStatus(Status status)
public int getNpc()
public final void setNpc(int npc)
private void registerMobs()
public boolean addMedalMap(int mapid)
public int getMedalProgress()
public List<Integer> getMedalMaps()
public boolean progress(int id)
public void setProgress(int id, String pr)
public boolean madeProgress()
public String getProgress(int id)
public void resetProgress(int id)
public void resetAllProgress()
public short getInfoNumber()
public String getInfoEx(int index)
public List<String> getInfoEx()
public long getCompletionTime()
public void setCompletionTime(long completionTime)
public long getExpirationTime()
public void setExpirationTime(long expirationTime)
public int getForfeited()
public int getCompleted()
public void setForfeited(int forfeited)
public void setCompleted(int completed)
public final void setCustomData(final String customData)
public final String getCustomData()
public String getProgressData()
```

---

## `org.gms.client` / `client/Ring.java`

### 类型声明
```text
class Ring
```

- 字段候选数: 6
```text
private final int ringId
private final int ringId2
private final int partnerId
private final int itemId
private final String partnerName
private boolean equipped = false
```

- 方法/构造器候选数: 14
```text
public Ring(int id, int id2, int partnerId, int itemid, String partnername)
public static Ring loadFromDb(int ringId)
public static void removeRing(final Ring ring)
public int getRingId()
public int getPartnerRingId()
public int getPartnerChrId()
public int getItemId()
public String getPartnerName()
public boolean equipped()
public void equip()
public void unequip()
public boolean equals(Object o)
public int hashCode()
public int compareTo(Ring other)
```

---

## `org.gms.client` / `client/Skill.java`

### 类型声明
```text
class Skill
```

- 字段候选数: 5
```text
private final int id
private Element element
private int animationTime
private final int job
private boolean action
```

- 方法/构造器候选数: 14
```text
public Skill(int id)
public int getId()
public StatEffect getEffect(int level)
public int getMaxLevel()
public boolean isFourthJob()
public void setElement(Element elem)
public Element getElement()
public int getAnimationTime()
public void setAnimationTime(int time)
public void incAnimationTime(int time)
public boolean isBeginnerSkill()
public void setAction(boolean act)
public boolean getAction()
public void addLevelEffect(StatEffect effect)
```

---

## `org.gms.client` / `client/SkillFactory.java`

### 类型声明
```text
class SkillFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static Skill getSkill(int id)
public static void loadAllSkills()
private static Skill loadFromData(int id, Data data)
public static String getSkillName(int skillid)
```

---

## `org.gms.client` / `client/SkillMacro.java`

### 类型声明
```text
class SkillMacro
```

- 字段候选数: 6
```text
private int skill1
private int skill2
private int skill3
private final String name
private final int shout
private final int position
```

- 方法/构造器候选数: 10
```text
public SkillMacro(int skill1, int skill2, int skill3, String name, int shout, int position)
public int getSkill1()
public int getSkill2()
public int getSkill3()
public void setSkill1(int skill)
public void setSkill2(int skill)
public void setSkill3(int skill)
public String getName()
public int getShout()
public int getPosition()
```

---

## `org.gms.client` / `client/SkinColor.java`

### 类型声明
```text
enum SkinColor
```

- 字段候选数: 1
```text
final int id
```

- 方法/构造器候选数: 10
```text
NORMAL(0),
DARK(1),
BLACK(2),
PALE(3),
BLUE(4),
GREEN(5),
WHITE(9),
SkinColor(int id)
public int getId()
public static SkinColor getById(int id)
```

---

## `org.gms.client` / `client/Stat.java`

### 类型声明
```text
enum Stat
```

- 字段候选数: 1
```text
private final int i
```

- 方法/构造器候选数: 24
```text
SKIN(0x1),
FACE(0x2),
HAIR(0x4),
LEVEL(0x10),
JOB(0x20),
STR(0x40),
DEX(0x80),
INT(0x100),
LUK(0x200),
HP(0x400),
MAXHP(0x800),
MP(0x1000),
MAXMP(0x2000),
AVAILABLEAP(0x4000),
AVAILABLESP(0x8000),
EXP(0x10000),
FAME(0x20000),
MESO(0x40000),
PET(0x180008),
Stat(int i)
public int getValue()
public static Stat getByValue(int value)
public static Stat getBy5ByteEncoding(int encoded)
public static Stat getByString(String type)
```

---

## `org.gms.client.autoban` / `client/autoban/AutobanFactory.java`

### 类型声明
```text
enum AutobanFactory
```

- 字段候选数: 3
```text
private final String name
private final int points
private final long expiretime
```

- 方法/构造器候选数: 36
```text
MOB_COUNT(I18nUtil.getMessage("autoban.name.MOB_COUNT")),
GENERAL(I18nUtil.getMessage("autoban.name.GENERAL")),
FIX_DAMAGE(I18nUtil.getMessage("autoban.name.FIX_DAMAGE")),
DAMAGE_HACK(I18nUtil.getMessage("autoban.name.DAMAGE_HACK"), 15, MINUTES.toMillis(1)),
DISTANCE_HACK(I18nUtil.getMessage("autoban.name.DISTANCE_HACK"), 10, MINUTES.toMillis(2)),
PORTAL_DISTANCE(I18nUtil.getMessage("autoban.name.PORTAL_DISTANCE"), 5, SECONDS.toMillis(30)),
PACKET_EDIT(I18nUtil.getMessage("autoban.name.PACKET_EDIT")),
ACC_HACK(I18nUtil.getMessage("autoban.name.ACC_HACK")),
CREATION_GENERATOR(I18nUtil.getMessage("autoban.name.CREATION_GENERATOR")),
HIGH_HP_HEALING(I18nUtil.getMessage("autoban.name.HIGH_HP_HEALING")),
FAST_HP_HEALING(I18nUtil.getMessage("autoban.name.FAST_HP_HEALING"), 15),
FAST_MP_HEALING(I18nUtil.getMessage("autoban.name.FAST_MP_HEALING"), 20, SECONDS.toMillis(30)),
GACHA_EXP(I18nUtil.getMessage("autoban.name.GACHA_EXP")),
TUBI(I18nUtil.getMessage("autoban.name.TUBI"), 20, SECONDS.toMillis(15)),
SHORT_ITEM_VAC(I18nUtil.getMessage("autoban.name.SHORT_ITEM_VAC")),
ITEM_VAC(I18nUtil.getMessage("autoban.name.ITEM_VAC")),
FAST_ITEM_PICKUP(I18nUtil.getMessage("autoban.name.FAST_ITEM_PICKUP"), 5, SECONDS.toMillis(30)),
FAST_ATTACK(I18nUtil.getMessage("autoban.name.FAST_ATTACK"), 10, SECONDS.toMillis(30)),
MPCON(I18nUtil.getMessage("autoban.name.MPCON"), 25, SECONDS.toMillis(30)),
AutobanFactory(String name)
AutobanFactory(String name, int points)
AutobanFactory(String name, int points, long expire)
public int getMaximum()
public long getExpire()
public static void initConfig(Map<String, AutobanConfigDO> configs)
public static void updateConfig(String type, AutobanConfigDO config)
public static AutobanConfigDO getConfig(String type)
public int getEffectivePoints()
public long getEffectiveExpiretime()
public boolean isDisabled()
public void addPoint(AutobanManager ban, String reason)
public void alert(Character chr, String reason)
public void autoban(Character chr, String value)
public static boolean toggleIgnored(int chrId)
private static boolean isIgnored(int chrId)
public static Collection<Integer> getIgnoredChrIds()
```

---

## `org.gms.client.autoban` / `client/autoban/AutobanManager.java`

### 类型声明
```text
class AutobanManager
```

- 字段候选数: 7
```text
private final Character chr
private int misses = 0
private int lastmisses = 0
private int samemisscount = 0
private final long[] spam = new long[20]
private final int[] timestamp = new int[20]
private final byte[] timestampcounter = new byte[20]
```

- 方法/构造器候选数: 8
```text
public AutobanManager(Character chr)
public void addPoint(AutobanFactory fac, String reason)
public void addMiss()
public void resetMisses()
public void spam(int type)
public void spam(int type, int timestamp)
public long getLastSpam(int type)
public void setTimestamp(int type, int time, int times)
```

---

## `org.gms.client.command` / `client/command/Command.java`

### 类型声明
```text
class Command
```

- 字段候选数: 2
```text
protected int rank
protected String description
```

- 方法/构造器候选数: 1
```text
protected String joinStringFrom(String[] arr, int start)
```

---

## `org.gms.client.command` / `client/command/CommandsExecutor.java`

### 类型声明
```text
class CommandsExecutor
```

- 字段候选数: 2
```text
private static final char USER_HEADING = '@'
private static final char GM_HEADING = '!'
```

- 方法/构造器候选数: 16
```text
public static boolean isCommand(Client client, String content)
public void loadCommandsExecutor()
public void handle(Client client, String message)
private void handleInternal(Client client, String message)
private void addCommandInfo(String name, Class<? extends Command> commandClass)
private void addCommand(String[] syntaxs, Class<? extends Command> commandClass)
private void addCommand(String syntax, Class<? extends Command> commandClass)
private void addCommand(String[] surtaxes, int rank, Class<? extends Command> commandClass)
private void addCommand(String syntax, int rank, Class<? extends Command> commandClass)
private void registerLv0Commands()
private void registerLv1Commands()
private void registerLv2Commands()
private void registerLv3Commands()
private void registerLv4Commands()
private void registerLv5Commands()
private void registerLv6Commands()
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/ChangeLanguageCommand.java`

### 类型声明
```text
class ChangeLanguageCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/DisposeCommand.java`

### 类型声明
```text
class DisposeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/DropLimitCommand.java`

### 类型声明
```text
class DropLimitCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/EnableAuthCommand.java`

### 类型声明
```text
class EnableAuthCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/EquipLvCommand.java`

### 类型声明
```text
class EquipLvCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/GachaCommand.java`

### 类型声明
```text
class GachaCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/GmCommand.java`

### 类型声明
```text
class GmCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/HelpCommand.java`

### 类型声明
```text
class HelpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/JoinEventCommand.java`

### 类型声明
```text
class JoinEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/LeaveEventCommand.java`

### 类型声明
```text
class LeaveEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/MapOwnerClaimCommand.java`

### 类型声明
```text
class MapOwnerClaimCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/OnlineCommand.java`

### 类型声明
```text
class OnlineCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/RanksCommand.java`

### 类型声明
```text
class RanksCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/RatesCommand.java`

### 类型声明
```text
class RatesCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/ReadPointsCommand.java`

### 类型声明
```text
class ReadPointsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/ReportBugCommand.java`

### 类型声明
```text
class ReportBugCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/ShowRatesCommand.java`

### 类型声明
```text
class ShowRatesCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/StaffCommand.java`

### 类型声明
```text
class StaffCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/StatDexCommand.java`

### 类型声明
```text
class StatDexCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/StatIntCommand.java`

### 类型声明
```text
class StatIntCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/StatLukCommand.java`

### 类型声明
```text
class StatLukCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/StatStrCommand.java`

### 类型声明
```text
class StatStrCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/TimeCommand.java`

### 类型声明
```text
class TimeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/ToggleExpCommand.java`

### 类型声明
```text
class ToggleExpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm0` / `client/command/commands/gm0/UptimeCommand.java`

### 类型声明
```text
class UptimeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/BossHpCommand.java`

### 类型声明
```text
class BossHpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/BuffMeCommand.java`

### 类型声明
```text
class BuffMeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/GotoCommand.java`

### 类型声明
```text
class GotoCommand
```

- 字段候选数: 2
```text
public static String GOTO_TOWNS_INFO = ""
public static String GOTO_AREAS_INFO = ""
```

- 方法/构造器候选数: 2
```text
private static void sortGotoEntries(List<Entry<String, Integer>> listEntries)
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/MobHpCommand.java`

### 类型声明
```text
class MobHpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/WhatDropsFromCommand.java`

### 类型声明
```text
class WhatDropsFromCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm1` / `client/command/commands/gm1/WhoDropsCommand.java`

### 类型声明
```text
class WhoDropsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ApCommand.java`

### 类型声明
```text
class ApCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/BombCommand.java`

### 类型声明
```text
class BombCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/BuffCommand.java`

### 类型声明
```text
class BuffCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/BuffMapCommand.java`

### 类型声明
```text
class BuffMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ClearDropsCommand.java`

### 类型声明
```text
class ClearDropsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ClearSavedLocationsCommand.java`

### 类型声明
```text
class ClearSavedLocationsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ClearSlotCommand.java`

### 类型声明
```text
class ClearSlotCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void execute(Client c, String[] params)
private void removeSlot(Client c, InventoryType type, int slot)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/DcCommand.java`

### 类型声明
```text
class DcCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/EmpowerMeCommand.java`

### 类型声明
```text
class EmpowerMeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/GachaListCommand.java`

### 类型声明
```text
class GachaListCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/GmShopCommand.java`

### 类型声明
```text
class GmShopCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/HealCommand.java`

### 类型声明
```text
class HealCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/HideCommand.java`

### 类型声明
```text
class HideCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/IdCommand.java`

### 类型声明
```text
class IdCommand
```

- 字段候选数: 1
```text
private final static int MAX_SEARCH_HITS = 100
```

- 方法/构造器候选数: 3
```text
private record HandbookItem(String id, String name)
public void execute(Client client, final String[] params)
private void populateIdMap(String type) throws IdTypeNotSupportedException, IOException
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ItemCommand.java`

### 类型声明
```text
class ItemCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ItemDropCommand.java`

### 类型声明
```text
class ItemDropCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/JailCommand.java`

### 类型声明
```text
class JailCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/JobCommand.java`

### 类型声明
```text
class JobCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/LevelCommand.java`

### 类型声明
```text
class LevelCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/LevelProCommand.java`

### 类型声明
```text
class LevelProCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/LootCommand.java`

### 类型声明
```text
class LootCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/MaxSkillCommand.java`

### 类型声明
```text
class MaxSkillCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/MaxStatCommand.java`

### 类型声明
```text
class MaxStatCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/MobSkillCommand.java`

### 类型声明
```text
class MobSkillCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ReachCommand.java`

### 类型声明
```text
class ReachCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/RechargeCommand.java`

### 类型声明
```text
class RechargeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/ResetSkillCommand.java`

### 类型声明
```text
class ResetSkillCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/SearchCommand.java`

### 类型声明
```text
class SearchCommand
```

- 字段候选数: 4
```text
private static Data npcStringData
private static Data mobStringData
private static Data skillStringData
private static Data mapStringData
```

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/SetSlotCommand.java`

### 类型声明
```text
class SetSlotCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/SetStatCommand.java`

### 类型声明
```text
class SetStatCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/SpCommand.java`

### 类型声明
```text
class SpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/SummonCommand.java`

### 类型声明
```text
class SummonCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/UnBugCommand.java`

### 类型声明
```text
class UnBugCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/UnHideCommand.java`

### 类型声明
```text
class UnHideCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/UnJailCommand.java`

### 类型声明
```text
class UnJailCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/WarpAreaCommand.java`

### 类型声明
```text
class WarpAreaCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/WarpCommand.java`

### 类型声明
```text
class WarpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/WarpMapCommand.java`

### 类型声明
```text
class WarpMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm2` / `client/command/commands/gm2/WhereaMiCommand.java`

### 类型声明
```text
class WhereaMiCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/BanCommand.java`

### 类型声明
```text
class BanCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ChatCommand.java`

### 类型声明
```text
class ChatCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/CheckDmgCommand.java`

### 类型声明
```text
class CheckDmgCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ClosePortalCommand.java`

### 类型声明
```text
class ClosePortalCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/DebuffCommand.java`

### 类型声明
```text
class DebuffCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/EndEventCommand.java`

### 类型声明
```text
class EndEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ExpedsCommand.java`

### 类型声明
```text
class ExpedsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/FaceCommand.java`

### 类型声明
```text
class FaceCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/FameCommand.java`

### 类型声明
```text
class FameCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/FlyCommand.java`

### 类型声明
```text
class FlyCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/GiveMesosCommand.java`

### 类型声明
```text
class GiveMesosCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/GiveNxCommand.java`

### 类型声明
```text
class GiveNxCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/GiveRpCommand.java`

### 类型声明
```text
class GiveRpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/GiveVpCommand.java`

### 类型声明
```text
class GiveVpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/HairCommand.java`

### 类型声明
```text
class HairCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/HealMapCommand.java`

### 类型声明
```text
class HealMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/HealPersonCommand.java`

### 类型声明
```text
class HealPersonCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/HpMpCommand.java`

### 类型声明
```text
class HpMpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/HurtCommand.java`

### 类型声明
```text
class HurtCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/IgnoreCommand.java`

### 类型声明
```text
class IgnoreCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/IgnoredCommand.java`

### 类型声明
```text
class IgnoredCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/InMapCommand.java`

### 类型声明
```text
class InMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/KillAllCommand.java`

### 类型声明
```text
class KillAllCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/KillCommand.java`

### 类型声明
```text
class KillCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/KillMapCommand.java`

### 类型声明
```text
class KillMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MaxEnergyCommand.java`

### 类型声明
```text
class MaxEnergyCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MaxHpMpCommand.java`

### 类型声明
```text
class MaxHpMpCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MonitorCommand.java`

### 类型声明
```text
class MonitorCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MonitorsCommand.java`

### 类型声明
```text
class MonitorsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MusicCommand.java`

### 类型声明
```text
class MusicCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static String getSongList()
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/MuteMapCommand.java`

### 类型声明
```text
class MuteMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/NightCommand.java`

### 类型声明
```text
class NightCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/NoticeCommand.java`

### 类型声明
```text
class NoticeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/NpcCommand.java`

### 类型声明
```text
class NpcCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/OnlineTwoCommand.java`

### 类型声明
```text
class OnlineTwoCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/OpenPortalCommand.java`

### 类型声明
```text
class OpenPortalCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/PeCommand.java`

### 类型声明
```text
class PeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/PosCommand.java`

### 类型声明
```text
class PosCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/QuestCompleteCommand.java`

### 类型声明
```text
class QuestCompleteCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/QuestResetCommand.java`

### 类型声明
```text
class QuestResetCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/QuestStartCommand.java`

### 类型声明
```text
class QuestStartCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ReloadDropsCommand.java`

### 类型声明
```text
class ReloadDropsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ReloadEventsCommand.java`

### 类型声明
```text
class ReloadEventsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ReloadMapCommand.java`

### 类型声明
```text
class ReloadMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ReloadPortalsCommand.java`

### 类型声明
```text
class ReloadPortalsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ReloadShopsCommand.java`

### 类型声明
```text
class ReloadShopsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/RipCommand.java`

### 类型声明
```text
class RipCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/SeedCommand.java`

### 类型声明
```text
class SeedCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/SpawnCommand.java`

### 类型声明
```text
class SpawnCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/StartEventCommand.java`

### 类型声明
```text
class StartEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/StartMapEventCommand.java`

### 类型声明
```text
class StartMapEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/StopMapEventCommand.java`

### 类型声明
```text
class StopMapEventCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/TimerAllCommand.java`

### 类型声明
```text
class TimerAllCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/TimerCommand.java`

### 类型声明
```text
class TimerCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/TimerMapCommand.java`

### 类型声明
```text
class TimerMapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/ToggleCouponCommand.java`

### 类型声明
```text
class ToggleCouponCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm3` / `client/command/commands/gm3/UnBanCommand.java`

### 类型声明
```text
class UnBanCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/BossDropRateCommand.java`

### 类型声明
```text
class BossDropRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/CakeCommand.java`

### 类型声明
```text
class CakeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/DropRateCommand.java`

### 类型声明
```text
class DropRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ExpRateCommand.java`

### 类型声明
```text
class ExpRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/FishingRateCommand.java`

### 类型声明
```text
class FishingRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ForceVacCommand.java`

### 类型声明
```text
class ForceVacCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/HorntailCommand.java`

### 类型声明
```text
class HorntailCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ItemVacCommand.java`

### 类型声明
```text
class ItemVacCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/MesoRateCommand.java`

### 类型声明
```text
class MesoRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PapCommand.java`

### 类型声明
```text
class PapCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PianusCommand.java`

### 类型声明
```text
class PianusCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PinkbeanCommand.java`

### 类型声明
```text
class PinkbeanCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PlayerNpcCommand.java`

### 类型声明
```text
class PlayerNpcCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PlayerNpcRemoveCommand.java`

### 类型声明
```text
class PlayerNpcRemoveCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PmobCommand.java`

### 类型声明
```text
class PmobCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PmobRemoveCommand.java`

### 类型声明
```text
class PmobRemoveCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PnpcCommand.java`

### 类型声明
```text
class PnpcCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/PnpcRemoveCommand.java`

### 类型声明
```text
class PnpcRemoveCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ProItemCommand.java`

### 类型声明
```text
class ProItemCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void execute(Client c, String[] params)
private static void hardsetItemStats(Equip equip, short stat, short spdjmp)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/QuestRateCommand.java`

### 类型声明
```text
class QuestRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ServerMessageCommand.java`

### 类型声明
```text
class ServerMessageCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/SetEqStatCommand.java`

### 类型声明
```text
class SetEqStatCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/TravelRateCommand.java`

### 类型声明
```text
class TravelRateCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/WarpToLifeCommand.java`

### 类型声明
```text
class WarpToLifeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm4` / `client/command/commands/gm4/ZakumCommand.java`

### 类型声明
```text
class ZakumCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/DebugCommand.java`

### 类型声明
```text
class DebugCommand
```

- 字段候选数: 1
```text
private final static String[] debugTypes = {"monster", "packet", "portal", "spawnpoint", "pos", "map", "mobsp", "event", "areas", "reactors", "servercoupons", "playercoupons", "timer", "marriage", "buff", ""}
```

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/IpListCommand.java`

### 类型声明
```text
class IpListCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/SetCommand.java`

### 类型声明
```text
class SetCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/ShowMoveLifeCommand.java`

### 类型声明
```text
class ShowMoveLifeCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/ShowPacketsCommand.java`

### 类型声明
```text
class ShowPacketsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm5` / `client/command/commands/gm5/ShowSessionsCommand.java`

### 类型声明
```text
class ShowSessionsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ClearQuestCacheCommand.java`

### 类型声明
```text
class ClearQuestCacheCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ClearQuestCommand.java`

### 类型声明
```text
class ClearQuestCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/DCAllCommand.java`

### 类型声明
```text
class DCAllCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/DevtestCommand.java`

### 类型声明
```text
class DevtestCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client client, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/EraseAllPNpcsCommand.java`

### 类型声明
```text
class EraseAllPNpcsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/GetAccCommand.java`

### 类型声明
```text
class GetAccCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/MapPlayersCommand.java`

### 类型声明
```text
class MapPlayersCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/SaveAllCommand.java`

### 类型声明
```text
class SaveAllCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ServerAddChannelCommand.java`

### 类型声明
```text
class ServerAddChannelCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ServerAddWorldCommand.java`

### 类型声明
```text
class ServerAddWorldCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ServerRemoveChannelCommand.java`

### 类型声明
```text
class ServerRemoveChannelCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ServerRemoveWorldCommand.java`

### 类型声明
```text
class ServerRemoveWorldCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/SetGmLevelCommand.java`

### 类型声明
```text
class SetGmLevelCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/ShutdownCommand.java`

### 类型声明
```text
class ShutdownCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/SpawnAllPNpcsCommand.java`

### 类型声明
```text
class SpawnAllPNpcsCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/SupplyRateCouponCommand.java`

### 类型声明
```text
class SupplyRateCouponCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.command.commands.gm6` / `client/command/commands/gm6/WarpWorldCommand.java`

### 类型声明
```text
class WarpWorldCommand
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void execute(Client c, String[] params)
```

---

## `org.gms.client.creator` / `client/creator/CharacterFactory.java`

### 类型声明
```text
class CharacterFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
protected synchronized static int createNewCharacter(Client c, String name, int face, int hair, int skin, int gender, CharacterFactoryRecipe recipe)
```

---

## `org.gms.client.creator` / `client/creator/CharacterFactoryRecipe.java`

### 类型声明
```text
class CharacterFactoryRecipe
```

- 字段候选数: 11
```text
private final Job job
private final int level
private final int map
private final int top
private final int bottom
private final int shoes
private final int weapon
private int str = 4, dex = 4, int_ = 4, luk = 4
private int maxHp = 50, maxMp = 5
private int ap = 0, sp = 0
private int meso = 0
```

- 方法/构造器候选数: 29
```text
public CharacterFactoryRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
public void setStr(int v)
public void setDex(int v)
public void setInt(int v)
public void setLuk(int v)
public void setMaxHp(int v)
public void setMaxMp(int v)
public void setRemainingAp(int v)
public void setRemainingSp(int v)
public void setMeso(int v)
public void addStartingSkillLevel(Skill skill, int level)
public void addStartingEquipment(Item eqpItem)
public void addStartingItem(int itemid, int quantity, InventoryType itemType)
public Job getJob()
public int getLevel()
public int getMap()
public int getTop()
public int getBottom()
public int getShoes()
public int getWeapon()
public int getStr()
public int getDex()
public int getInt()
public int getLuk()
public int getMaxHp()
public int getMaxMp()
public int getRemainingAp()
public int getRemainingSp()
public int getMeso()
```

---

## `org.gms.client.creator` / `client/creator/MakeCharInfo.java`

### 类型声明
```text
class MakeCharInfo
```

- 字段候选数: 8
```text
private static final String FACE_ID = "0"
private static final String HAIR_ID = "1"
private static final String HAIR_COLOR_ID = "2"
private static final String SKIN_ID = "3"
private static final String TOP_ID = "4"
private static final String BOTTOM_ID = "5"
private static final String SHOE_ID = "6"
private static final String WEAPON_ID = "7"
```

- 方法/构造器候选数: 10
```text
public MakeCharInfo(Data charInfoData)
public boolean verifyFaceId(int id)
public boolean verifyHairId(int id)
public boolean verifyHairColorId(int id)
public boolean verifySkinId(int id)
public boolean verifyTopId(int id)
public boolean verifyBottomId(int id)
public boolean verifyShoeId(int id)
public boolean verifyWeaponId(int id)
public boolean verifyCharacter(Character character)
```

---

## `org.gms.client.creator` / `client/creator/MakeCharInfoValidator.java`

### 类型声明
```text
class MakeCharInfoValidator
```

- 字段候选数: 6
```text
private static final MakeCharInfo charFemale
private static final MakeCharInfo charMale
private static final MakeCharInfo orientCharFemale
private static final MakeCharInfo orientCharMale
private static final MakeCharInfo premiumCharFemale
private static final MakeCharInfo premiumCharMale
```

- 方法/构造器候选数: 2
```text
private static MakeCharInfo getMakeCharInfo(Character character)
public static boolean isNewCharacterValid(Character character)
```

---

## `org.gms.client.creator.novice` / `client/creator/novice/BeginnerCreator.java`

### 类型声明
```text
class BeginnerCreator
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

---

## `org.gms.client.creator.novice` / `client/creator/novice/LegendCreator.java`

### 类型声明
```text
class LegendCreator
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

---

## `org.gms.client.creator.novice` / `client/creator/novice/NoblesseCreator.java`

### 类型声明
```text
class NoblesseCreator
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

---

## `org.gms.client.creator.veteran` / `client/creator/veteran/BowmanCreator.java`

### 类型声明
```text
class BowmanCreator
```

- 字段候选数: 2
```text
private static final int[] weapons = {ItemId.RYDEN, ItemId.MOUNTAIN_CROSSBOW}
private static final int[] startingHpMp = {797, 404}
```

- 方法/构造器候选数: 4
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

---

## `org.gms.client.creator.veteran` / `client/creator/veteran/MagicianCreator.java`

### 类型声明
```text
class MagicianCreator
```

- 字段候选数: 4
```text
private static final int[] equips = {0, ItemId.PURPLE_FAIRY_TOP, 0, ItemId.PURPLE_FAIRY_SKIRT, ItemId.RED_MAGICSHOES}
private static final int[] weapons = {ItemId.MITHRIL_WAND, ItemId.CIRCLE_WINDED_STAFF}
private static final int[] startingHpMp = {405, 729}
private static final int[] mpGain = {0, 40, 80, 118, 156, 194, 230, 266, 302, 336, 370}
```

- 方法/构造器候选数: 4
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon, int gender, int improveSp)
private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

---

## `org.gms.client.creator.veteran` / `client/creator/veteran/PirateCreator.java`

### 类型声明
```text
class PirateCreator
```

- 字段候选数: 3
```text
private static final int[] equips = {0, 0, 0, 0, ItemId.BROWN_PAULIE_BOOTS}
private static final int[] weapons = {ItemId.PRIME_HANDS, ItemId.COLD_MIND}
private static final int[] startingHpMp = {846, 503}
```

- 方法/构造器候选数: 4
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

---

## `org.gms.client.creator.veteran` / `client/creator/veteran/ThiefCreator.java`

### 类型声明
```text
class ThiefCreator
```

- 字段候选数: 2
```text
private static final int[] weapons = {ItemId.STEEL_GUARDS, ItemId.REEF_CLAW}
private static final int[] startingHpMp = {794, 407}
```

- 方法/构造器候选数: 4
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon)
private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

---

## `org.gms.client.creator.veteran` / `client/creator/veteran/WarriorCreator.java`

### 类型声明
```text
class WarriorCreator
```

- 字段候选数: 4
```text
private static final int[] equips = {ItemId.RED_HWARANG_SHIRT, 0, ItemId.BLACK_MARTIAL_ARTS_PANTS, 0, ItemId.MITHRIL_BATTLE_GRIEVES}
private static final int[] weapons = {ItemId.GLADIUS, ItemId.MITHRIL_POLE_ARM, ItemId.MITHRIL_MAUL, ItemId.FIREMANS_AXE}
private static final int[] startingHpMp = {905, 208}
private static final int[] hpGain = {0, 72, 144, 212, 280, 348, 412, 476, 540, 600, 660}
```

- 方法/构造器候选数: 4
```text
private static CharacterFactoryRecipe createRecipe(Job job, int level, int map, int top, int bottom, int shoes, int weapon, int gender, int improveSp)
private static void giveEquipment(CharacterFactoryRecipe recipe, ItemInformationProvider ii, int equipid)
private static void giveItem(CharacterFactoryRecipe recipe, int itemid, int quantity, InventoryType itemType)
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

---

## `org.gms.client.inventory` / `client/inventory/Equip.java`

### 类型声明
```text
class Equip
enum ScrollResult
enum StatUpgrade
```

- 字段候选数: 5
```text
private byte upgradeSlots
private short flag
private float itemExp
private int ringid = -1
private boolean wear = false
```

- 方法/构造器候选数: 70
```text
public Equip(int id, short position)
public Equip(int id, short position, int slots)
public Item copy()
public short getFlag()
public byte getItemType()
public byte getUpgradeSlots()
public short getStr()
public short getDex()
public short getInt()
public short getLuk()
public short getHp()
public short getMp()
public short getWatk()
public short getMatk()
public short getWdef()
public short getMdef()
public short getAcc()
public short getAvoid()
public short getHands()
public short getSpeed()
public short getJump()
public short getVicious()
public void setFlag(short flag)
public void setStr(short str)
public void setDex(short dex)
public void setInt(short _int)
public void setLuk(short luk)
public void setHp(short hp)
public void setMp(short mp)
public void setWatk(short watk)
public void setMatk(short matk)
public void setWdef(short wdef)
public void setMdef(short mdef)
public void setAcc(short acc)
public void setAvoid(short avoid)
public void setHands(short hands)
public void setSpeed(short speed)
public void setJump(short jump)
public void setVicious(short vicious)
public void setUpgradeSlots(byte upgradeSlots)
public byte getLevel()
public void setLevel(byte level)
private static int getStatModifier(boolean isAttribute)
private static int randomizeStatUpgrade(int top)
private static boolean isPhysicalWeapon(int itemid)
private boolean isNotWeaponAffinity(StatUpgrade name)
private void getUnitStatUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name, int curStat, boolean isAttribute)
private static void getUnitSlotUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name)
private static void getUnitSlotUpgrade(List<Pair<StatUpgrade, Integer>> stats, StatUpgrade name, double chance)
private void UpgradeSlotProcessing(List<Pair<StatUpgrade, Integer>> stats,int equipLevel)
private void improveDefaultStats(List<Pair<StatUpgrade, Integer>> stats)
private int handleStatUpgrade(StatUpgrade type, int value, int maxStat)
private int getCurrentStat(StatUpgrade type)
private void setCurrentStat(StatUpgrade type, int value)
private String getStatMessage(StatUpgrade type, int value)
private void gainLevel(Client c)
public int getItemExp()
private static double normalizedMasteryExp(int reqLevel)
public synchronized void gainItemExp(Client c, int gain)
private boolean reachedMaxLevel()
public String showEquipFeatures(Client c)
public void setItemExp(int exp)
public void setItemLevel(byte level)
public void setQuantity(short quantity)
public void setUpgradeSlots(int i)
public void setVicious(int i)
public int getRingId()
public void setRingId(int id)
public boolean isWearing()
public void wear(boolean yes)
```

---

## `org.gms.client.inventory` / `client/inventory/Inventory.java`

### 类型声明
```text
class Inventory
```

- 字段候选数: 4
```text
protected final InventoryType type
protected Character owner
protected byte slotLimit
protected boolean checked = false
```

- 方法/构造器候选数: 48
```text
public Inventory(Character mc, InventoryType type, byte slotLimit)
public boolean isExtendableInventory()
public boolean isEquipInventory()
public byte getSlotLimit()
public void setSlotLimit(int newLimit)
public Collection<Item> list()
public Item findById(int itemId)
public Item findByName(String name)
public int countById(int itemId)
public int countNotOwnedById(int itemId)
public int freeSlotCountById(int itemId, int required)
public List<Item> listById(int itemId)
public List<Item> linkedListById(int itemId)
public short addItem(Item item)
public void addItemFromDB(Item item)
private static boolean isSameOwner(Item source, Item target)
public void move(short sSlot, short dSlot, short slotMax)
private void swap(Item source, Item target)
public Item getItem(short slot)
public void removeItem(short slot)
public void removeItem(short slot, short quantity, boolean allowZero)
protected short addSlot(Item item)
protected void addSlotFromDB(short slot, Item item)
public void removeSlot(short slot)
public boolean isFull()
public boolean isFull(int margin)
public boolean isFullAfterSomeItems(int margin, int used)
public short getNextFreeSlot()
public short getNumFreeSlot()
private static boolean checkItemRestricted(List<Pair<Item, InventoryType>> items)
public static boolean checkSpot(Character chr, Item item)
public static boolean checkSpot(Character chr, List<Item> items)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, boolean useProofInv)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, List<Integer> typesSlotsUsed, boolean useProofInv)
private static long fnvHash32(final String k)
private static Long hashKey(Integer itemId, String owner)
public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items)
public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items, boolean useProofInv)
public static boolean checkSpotsAndOwnership(Character chr, List<Pair<Item, InventoryType>> items, List<Integer> typesSlotsUsed, boolean useProofInv)
public InventoryType getType()
public Iterator<Item> iterator()
public Item findByCashId(int cashId)
public boolean checked()
public void checked(boolean yes)
public void lockInventory()
public void unlockInventory()
public void dispose()
```

---

## `org.gms.client.inventory` / `client/inventory/InventoryProof.java`

### 类型声明
```text
class InventoryProof
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public InventoryProof(Character mc)
public void cloneContents(Inventory inv)
public void flushContents()
protected short addSlot(Item item)
protected void addSlotFromDB(short slot, Item item)
public void removeSlot(short slot)
```

---

## `org.gms.client.inventory` / `client/inventory/InventoryType.java`

### 类型声明
```text
enum InventoryType
```

- 字段候选数: 2
```text
private final byte type
private final String name
```

- 方法/构造器候选数: 14
```text
UNDEFINED(0, I18nUtil.getMessage("InventoryType.UNDEFINED")),
EQUIP(1, I18nUtil.getMessage("InventoryType.EQUIP")),
USE(2, I18nUtil.getMessage("InventoryType.USE")),
SETUP(3, I18nUtil.getMessage("InventoryType.SETUP")),
ETC(4, I18nUtil.getMessage("InventoryType.ETC")),
CASH(5, I18nUtil.getMessage("InventoryType.CASH")),
CANHOLD(6, I18nUtil.getMessage("InventoryType.CANHOLD")),   //Proof-guard for inserting after removal checks
EQUIPPED(-1, I18nUtil.getMessage("InventoryType.EQUIPPED")); //Seems nexon screwed something when removing an item T_T
InventoryType(int type, String name)
public short getBitfieldEncoding()
public static InventoryType getByType(byte type)
public static InventoryType getByWZName(String name)
public boolean canChangeSlotMax()
public boolean isEquip()
```

---

## `org.gms.client.inventory` / `client/inventory/Item.java`

### 类型声明
```text
class Item
```

- 字段候选数: 12
```text
private final int id
private int cashId
private int sn
private short position
private short quantity
private int petid = -1
private Pet pet = null
private String owner = ""
protected List<String> itemLog
private short flag
private long expiration = -1
private String giftFrom = ""
```

- 方法/构造器候选数: 27
```text
public Item(int id, short position, short quantity)
public Item(int id, short position, short quantity, int petid)
public Item copy()
public void setPosition(short position)
public void setQuantity(short quantity)
public int getItemId()
public int getCashId()
public short getPosition()
public short getQuantity()
public InventoryType getInventoryType()
public byte getItemType()
public String getOwner()
public void setOwner(String owner)
public int getPetId()
public int compareTo(Item other)
public String toString()
public List<String> getItemLog()
public short getFlag()
public void setFlag(short b)
public long getExpiration()
public void setExpiration(long expire)
public int getSN()
public void setSN(int sn)
public String getGiftFrom()
public void setGiftFrom(String giftFrom)
public Pet getPet()
public boolean isUntradeable()
```

---

## `org.gms.client.inventory` / `client/inventory/ItemFactory.java`

### 类型声明
```text
enum ItemFactory
```

- 字段候选数: 3
```text
private final int value
private final boolean account
private static final int lockCount = 400
```

- 方法/构造器候选数: 15
```text
INVENTORY(1, false),
STORAGE(2, true),
CASH_EXPLORER(3, true),
CASH_CYGNUS(4, true),
CASH_ARAN(5, true),
MERCHANT(6, false),
CASH_OVERALL(7, true),
MARRIAGE_GIFTS(8, false),
ItemFactory(int value, boolean account)
public int getValue()
public void saveItems(List<Pair<Item, InventoryType>> items, int id, Connection con) throws SQLException
public void saveItems(List<Pair<Item, InventoryType>> items, List<Short> bundlesList, int id, Connection con) throws SQLException
private static Equip loadEquipFromResultSet(ResultSet rs) throws SQLException
private void saveItemsCommon(List<Pair<Item, InventoryType>> items, int id, Connection con) throws SQLException
private void saveItemsMerchant(List<Pair<Item, InventoryType>> items, List<Short> bundlesList, int id, Connection con) throws SQLException
```

---

## `org.gms.client.inventory` / `client/inventory/ModifyInventory.java`

### 类型声明
```text
class ModifyInventory
```

- 字段候选数: 3
```text
private final int mode
private Item item
private short oldPos
```

- 方法/构造器候选数: 9
```text
public ModifyInventory(final int mode, final Item item)
public ModifyInventory(final int mode, final Item item, final short oldPos)
public final int getMode()
public final int getInventoryType()
public final short getPosition()
public final short getOldPosition()
public final short getQuantity()
public final Item getItem()
public final void clear()
```

---

## `org.gms.client.inventory` / `client/inventory/Pet.java`

### 类型声明
```text
class Pet
enum PetAttribute
```

- 字段候选数: 10
```text
private String name
private int uniqueid
private int tameness = 0
private byte level = 1
private int fullness = 100
private int Fh
private Point pos
private int stance
private boolean summoned
private int petAttribute = 0
```

- 方法/构造器候选数: 31
```text
private Pet(int id, short position, int uniqueid)
public static Pet loadFromDb(int itemid, short position, int petid)
public static void deleteFromDb(Character owner, int petid)
public void saveToDb()
public static int createPet(int itemid)
public static int createPet(int itemid, byte level, int tameness, int fullness)
public String getName()
public void setName(String name)
public int getUniqueId()
public void setUniqueId(int id)
public int getTameness()
public void setTameness(int tameness)
public byte getLevel()
public void gainTamenessFullness(Character owner, int incTameness, int incFullness, int type)
public void gainTamenessFullness(Character owner, int incTameness, int incFullness, int type, boolean forceEnjoy)
public void setLevel(byte level)
public int getFullness()
public void setFullness(int fullness)
public int getFh()
public void setFh(int Fh)
public Point getPos()
public void setPos(Point pos)
public int getStance()
public void setStance(int stance)
public boolean isSummoned()
public void setSummoned(boolean yes)
public int getPetAttribute()
private void setPetAttribute(int flag)
public void addPetAttribute(Character owner, PetAttribute flag)
public void removePetAttribute(Character owner, PetAttribute flag)
public void updatePosition(List<LifeMovementFragment> movement)
```

---

## `org.gms.client.inventory` / `client/inventory/PetCommand.java`

### 类型声明
```text
class PetCommand
```

- 字段候选数: 4
```text
private final int petId
private final int skillId
private final int prob
private final int inc
```

- 方法/构造器候选数: 5
```text
public PetCommand(int petId, int skillId, int prob, int inc)
public int getPetId()
public int getSkillId()
public int getProbability()
public int getIncrease()
```

---

## `org.gms.client.inventory` / `client/inventory/PetDataFactory.java`

### 类型声明
```text
class PetDataFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static PetCommand getPetCommand(int petId, int skillId)
public static int getHunger(int petId)
```

---

## `org.gms.client.inventory` / `client/inventory/WeaponType.java`

### 类型声明
```text
enum WeaponType
```

- 字段候选数: 1
```text
private final double damageMultiplier
```

- 方法/构造器候选数: 21
```text
NOT_A_WEAPON(0),
GENERAL1H_SWING(4.4),
GENERAL1H_STAB(3.2),
GENERAL2H_SWING(4.8),
GENERAL2H_STAB(3.4),
BOW(3.4),
CLAW(3.6),
CROSSBOW(3.6),
DAGGER_THIEVES(3.6),
DAGGER_OTHER(4),
GUN(3.6),
KNUCKLE(4.8),
POLE_ARM_SWING(5.0),
POLE_ARM_STAB(3.0),
SPEAR_STAB(5.0),
SPEAR_SWING(3.0),
STAFF(3.6),
SWORD1H(4.0),
SWORD2H(4.6),
WeaponType(double maxDamageMultiplier)
public double getMaxDamageMultiplier()
```

---

## `org.gms.client.inventory.manipulator` / `client/inventory/manipulator/InventoryManipulator.java`

### 类型声明
```text
class InventoryManipulator
```

- 字段候选数: 0

- 方法/构造器候选数: 25
```text
public static boolean addById(Client c, int itemId, short quantity)
public static boolean addById(Client c, int itemId, short quantity, long expiration)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, long expiration)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, short flag, long expiration)
private static boolean addByIdInternal(Client c, Character chr, InventoryType type, Inventory inv, int itemId, short quantity, String owner, int petid, short flag, long expiration)
public static boolean addFromDrop(Client c, Item item)
public static boolean addFromDrop(Client c, Item item, boolean show)
public static boolean addFromDrop(Client c, Item item, boolean show, int petId)
private static boolean addFromDropInternal(Client c, Character chr, InventoryType type, Inventory inv, Item item, boolean show, int petId)
private static boolean haveItemWithId(Inventory inv, int itemid)
public static boolean checkSpace(Client c, int itemid, int quantity, String owner)
public static int checkSpaceProgressively(Client c, int itemid, int quantity, String owner, int usedSlots, boolean useProofInv)
public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop)
public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop, boolean consume)
private static void announceModifyInventory(Client c, Item item, boolean fromDrop, boolean allowZero)
public static void removeById(Client c, InventoryType type, int itemId, int quantity, boolean fromDrop, boolean consume)
private static boolean isSameOwner(Item source, Item target)
public static void move(Client c, InventoryType type, short src, short dst)
public static void equip(Client c, short src, short dst)
public static void unequip(Client c, short src, short dst)
private static boolean isDisappearingItemDrop(Item it)
public static void drop(Client c, InventoryType type, short src, short quantity)
private static boolean isDroppedItemRestricted(Item it)
public static boolean isSandboxItem(Item it)
```

---

## `org.gms.client.inventory.manipulator` / `client/inventory/manipulator/KarmaManipulator.java`

### 类型声明
```text
class KarmaManipulator
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
private static short getKarmaFlag(Item item)
public static boolean hasKarmaFlag(Item item)
public static void toggleKarmaFlagToUntradeable(Item item)
public static void setKarmaFlag(Item item)
```

---

## `org.gms.client.keybind` / `client/keybind/KeyBinding.java`

### 类型声明
```text
class KeyBinding
```

- 字段候选数: 2
```text
private final int type
private final int action
```

- 方法/构造器候选数: 3
```text
public KeyBinding(int type, int action)
public int getType()
public int getAction()
```

---

## `org.gms.client.keybind` / `client/keybind/QuickslotBinding.java`

### 类型声明
```text
class QuickslotBinding
```

- 字段候选数: 3
```text
public static final int QUICKSLOT_SIZE = 8
public static final byte[] DEFAULT_QUICKSLOTS = {0x2A, 0x52, 0x47, 0x49, 0x1D, 0x53, 0x4F, 0x51}
private final byte[] m_aQuickslotKeyMapped
```

- 方法/构造器候选数: 3
```text
public QuickslotBinding(byte[] aKeys)
public void encode(OutPacket p)
public byte[] GetKeybindings()
```

---

## `org.gms.client.processor.action` / `client/processor/action/MakerProcessor.java`

### 类型声明
```text
class MakerProcessor
```

- 字段候选数: 0

- 方法/构造器候选数: 7
```text
public static void makerAction(InPacket p, Client c)
private static boolean removeOddMakerReagents(int toCreate, Map<Integer, Short> reagentids)
private static int getMakerReagentSlots(int itemId)
public static int getMakerSkillLevel(Character chr)
private static short getCreateStatus(Client c, MakerItemCreateEntry recipe)
private static boolean hasItems(Client c, MakerItemCreateEntry recipe)
private static boolean addBoostedMakerItem(Client c, int itemid, int stimulantid, Map<Integer, Short> reagentids)
```

---

## `org.gms.client.processor.action` / `client/processor/action/PetAutopotProcessor.java`

### 类型声明
```text
class PetAutopotProcessor
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static void runAutopotAction(Client c, short slot, int itemid)
```

---

## `org.gms.client.processor.action` / `client/processor/action/SpawnPetProcessor.java`

### 类型声明
```text
class SpawnPetProcessor
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static void processSpawnPet(Client c, byte slot, boolean lead)
```

---

## `org.gms.client.processor.npc` / `client/processor/npc/DueyProcessor.java`

### 类型声明
```text
class DueyProcessor
enum Actions
```

- 字段候选数: 0

- 方法/构造器候选数: 14
```text
private static void showDueyNotification(Client c, Character player)
private static void deletePackageFromInventoryDB(Connection con, int packageId) throws SQLException
private static void removePackageFromDB(int packageId)
private static DueyPackage getPackageFromDB(ResultSet rs)
private static List<DueyPackage> loadPackages(Character chr)
private static int createPackage(int mesos, String message, String sender, int toCid, boolean quick)
private static boolean insertPackageItem(int packageId, Item item)
private static int addPackageItemFromInventory(int packageId, Client c, byte invTypeId, short itemPos, short amount)
public static void dueySendItem(Client c, byte invTypeId, short itemPos, short amount, int sendMesos, String sendMessage, String recipient, boolean quick)
public static void dueyRemovePackage(Client c, int packageid, boolean playerRemove)
public static synchronized void dueyClaimPackage(Client c, int packageId)
public static void dueySendTalk(Client c, boolean quickDelivery)
public static void dueyCreatePackage(Item item, int mesos, String sender, int recipientCid)
public static void runDueyExpireSchedule()
```

---

## `org.gms.client.processor.npc` / `client/processor/npc/FredrickProcessor.java`

### 类型声明
```text
class FredrickProcessor
```

- 字段候选数: 2
```text
private static final int[] dailyReminders = new int[]{2, 5, 10, 15, 30, 60, 90, Integer.MAX_VALUE}
private final NoteService noteService
```

- 方法/构造器候选数: 11
```text
public FredrickProcessor(NoteService noteService)
private static byte canRetrieveFromFredrick(Character chr, List<Pair<Item, InventoryType>> items)
public static int timestampElapsedDays(Timestamp then, long timeNow)
private static String fredrickReminderMessage(int daynotes)
public static void removeFredrickLog(int cid)
private static void removeFredrickLog(Connection con, int cid) throws SQLException
public static void insertFredrickLog(int cid)
private static void removeFredrickReminders(List<Pair<Integer, Integer>> expiredCids)
public void runFredrickSchedule()
private static boolean deleteFredrickItems(int cid)
public void fredrickRetrieveItems(Client c)
```

---

## `org.gms.client.processor.npc` / `client/processor/npc/StorageProcessor.java`

### 类型声明
```text
class StorageProcessor
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static void storageAction(InPacket p, Client c)
private static boolean hasGMRestrictions(Character character)
```

---

## `org.gms.client.processor.stat` / `client/processor/stat/AssignAPProcessor.java`

### 类型声明
```text
class AssignAPProcessor
```

- 字段候选数: 6
```text
private static boolean useServerAutoAssigner
private static boolean useAutoAssignSecondaryCap
private static boolean useEnforceHpmpSwap
private static boolean useFixedRatioHpmpUpdate
private static boolean useRandomizeHpmpGain
private static int maxAp
```

- 方法/构造器候选数: 12
```text
public static void reloadConfig()
public static void APAutoAssignAction(InPacket inPacket, Client c)
private static int getNthHighestStat(List<Short> statList, short rank)
private static int gainStatByType(Stat type, int[] statGain, int gain, int[] statUpdate)
private static Stat getQuaternaryStat(Job stance)
public static boolean APResetAction(Client c, int APFrom, int APTo)
public static void APAssignAction(Client c, int num)
private static boolean addStat(Character chr, int apTo, boolean usedAPReset)
private static int calcHpChange(Character player, boolean usedAPReset)
private static int calcMpChange(Character player, boolean usedAPReset)
private static int takeHp(Job job)
private static int takeMp(Job job)
```

---

## `org.gms.client.processor.stat` / `client/processor/stat/AssignSPProcessor.java`

### 类型声明
```text
class AssignSPProcessor
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static boolean canSPAssign(Client c, int skillid)
public static void SPAssignAction(Client c, int skillid)
```

---

## `org.gms.client.status` / `client/status/MonsterStatus.java`

### 类型声明
```text
enum MonsterStatus
```

- 字段候选数: 2
```text
private final int i
private final boolean first
```

- 方法/构造器候选数: 34
```text
WATK(0x1),
WDEF(0x2),
NEUTRALISE(0x2, true),
PHANTOM_IMPRINT(0x4, true), // needs testing
MATK(0x4),
MDEF(0x8),
ACC(0x10),
AVOID(0x20),
SPEED(0x40),
STUN(0x80),
FREEZE(0x100),
POISON(0x200),
SEAL(0x400),
SHOWDOWN(0x800),
WEAPON_ATTACK_UP(0x1000),
WEAPON_DEFENSE_UP(0x2000),
MAGIC_ATTACK_UP(0x4000),
MAGIC_DEFENSE_UP(0x8000),
DOOM(0x10000),
SHADOW_WEB(0x20000),
WEAPON_IMMUNITY(0x40000),
MAGIC_IMMUNITY(0x80000),
HARD_SKIN(0x200000), // just added
NINJA_AMBUSH(0x400000),
ELEMENTAL_ATTRIBUTE(0x800000), // just added
VENOMOUS_WEAPON(0x1000000),
BLIND(0x2000000), // just added
SEAL_SKILL(0x4000000),
INERTMOB(0x10000000),
WEAPON_REFLECT(0x20000000, true),
MonsterStatus(int i)
MonsterStatus(int i, boolean first)
public boolean isFirst()
public int getValue()
```

---

## `org.gms.client.status` / `client/status/MonsterStatusEffect.java`

### 类型声明
```text
class MonsterStatusEffect
```

- 字段候选数: 3
```text
private final Skill skill
private final MobSkill mobskill
private final boolean monsterSkill
```

- 方法/构造器候选数: 6
```text
public MonsterStatusEffect(Map<MonsterStatus, Integer> stati, Skill skillId, MobSkill mobskill, boolean monsterSkill)
public Integer setValue(MonsterStatus status, Integer newVal)
public Skill getSkill()
public boolean isMonsterSkill()
public void removeActiveStatus(MonsterStatus stat)
public MobSkill getMobSkill()
```

---

## `org.gms.config` / `config/CorsConfig.java`

### 类型声明
```text
class CorsConfig
```

- 字段候选数: 1
```text
private String vue
```

- 方法/构造器候选数: 1
```text
public void addCorsMappings(CorsRegistry registry)
```

---

## `org.gms.config` / `config/GameConfig.java`

### 类型声明
```text
class GameConfig
```

- 字段候选数: 0

- 方法/构造器候选数: 59
```text
private GameConfig()
public static void add(GameConfigDO gameConfigDO)
private static void add(GameConfig config, GameConfigDO gameConfigDO)
public static void remove(GameConfigDO gameConfigDO)
public static void update(GameConfigDO gameConfigDO)
public static Object getObject(String key)
public static <T> T get(String key)
public static <T> T get(String key, T defaultValue)
public static <T> T get(String type, String key)
public static <T> T get(String type, String key, T defaultVal)
public static <T> T get(String type, String subType, String key)
public static <T> T get(String type, String subType, String key, T defaultVal)
private static <T> T getValue(JSONObject valueProp)
public static JSONObject getValueProp(String type, String subType, String key)
public static JSONObject getValueProp(String type, String key)
public static Integer getInteger(String key)
public static int getIntValue(String key)
public static Long getLong(String key)
public static long getLongValue(String key)
public static Short getShort(String key)
public static short getShortValue(String key)
public static Byte getByte(String key)
public static byte getByteValue(String key)
public static float getFloat(String key)
public static float getFloatValue(String key)
public static Double getDouble(String key)
public static double getDoubleValue(String key)
public static Boolean getBoolean(String key)
public static boolean getBooleanValue(String key)
public static String getString(String key)
public static String getStringValue(String key)
public static <T> T getObject(String key, Class<T> clz)
private static <T> T getValue(String key, T defaultVal, Function<JSONObject, T> mapper)
public static <T> T getWorld(int worldId, String key)
public static <T> T getServer(String key)
public static int getWorldInt(int worldId, String key)
public static int getServerInt(String key)
public static byte getWorldByte(int worldId, String key)
public static byte getServerByte(String key)
public static long getWorldLong(int worldId, String key)
public static long getServerLong(String key)
public static short getWorldShort(int worldId, String key)
public static short getServerShort(String key)
public static float getWorldFloat(int worldId, String key)
public static float getServerFloat(String key)
public static double getWorldDouble(int worldId, String key)
public static double getServerDouble(String key)
public static String getWorldString(int worldId, String key)
public static String getServerString(String key)
public static boolean getWorldBoolean(int worldId, String key)
public static boolean getServerBoolean(String key)
public static <T> T getWorldObject(int worldId, String key, Class<T> clz)
public static <T> T getWorldObject(int worldId, String key, T defaultVal)
public static <T> T getServerObject(String key, Class<T> clz)
public static <T> T getServerObject(String key, T defaultVal)
private static <T> T getValue(boolean isServer, String subType, String key, Class<?> clz)
public static <T> T getWorldObject(int worldId, String key, TypeReference<T> type)
public static <T> T getServerObject(String key, TypeReference<T> type)
public static JSONObject getConfig()
```

---

## `org.gms.config` / `config/I18nConfig.java`

### 类型声明
```text
class I18nConfig
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public MessageSource messageSource()
public MessageSource logSource()
public MessageSource exceptionSource()
```

---

## `org.gms.config` / `config/ServerConfig.java`

### 类型声明
```text
class ServerConfig
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public FilterRegistrationBean<ServerFilter> filterRegistrationBean(ServerFilter serverFilter)
public OpenAPI openAPI()
```

---

## `org.gms.config` / `config/SpringSecurityConfig.java`

### 类型声明
```text
class SpringSecurityConfig
```

- 字段候选数: 2
```text
private final UserDetailsServiceImpl userDetailsService
private final AuthEntryPointJwt unauthorizedHandler
```

- 方法/构造器候选数: 6
```text
public SpringSecurityConfig(UserDetailsServiceImpl userDetailsService, AuthEntryPointJwt unauthorizedHandler)
public AuthTokenFilter authenticationJwtTokenFilter()
public DaoAuthenticationProvider authenticationProvider()
public AuthenticationManager authenticationManager(AuthenticationConfiguration authConfig) throws Exception
public PasswordEncoder passwordEncoder()
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception
```

---

## `org.gms.constants.api` / `constants/api/ApiConstant.java`

### 类型声明
```text
class ApiConstant
```

- 字段候选数: 2
```text
public static final String V1 = "v1"
public static final String LATEST = V1
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.api` / `constants/api/InformationType.java`

### 类型声明
```text
enum InformationType
```

- 字段候选数: 1
```text
private final String type
```

- 方法/构造器候选数: 12
```text
CASH("cash"),
CONSUME("consume"),
EQP("eqp"),
ETC("etc"),
INS("ins"),
MAP("map"),
MOB("mob"),
NPC("npc"),
PET("pet"),
SKILL("skill"),
InformationType(final String type)
public static InformationType ofType(final String type)
```

---

## `org.gms.constants.game` / `constants/game/CommodityFlag.java`

### 类型声明
```text
enum CommodityFlag
```

- 字段候选数: 3
```text
private final long flag
private final int sort
private final String desc
```

- 方法/构造器候选数: 36
```text
SN(0, 0, "SN", (p, n)-> p.writeInt(n.intValue())),
FLAG(0, 1, "FLAG", (p, n)-> p.writeInt(n.intValue())),
ITEM_ID(1, 2, "物品ID", (p, n)-> p.writeInt(n.intValue())),
COUNT(1 << 1, 3, "数量", (p, n)-> p.writeShort(n.intValue())),
PRICE(1 << 2, 5, "价格", (p, n)-> p.writeInt(n.intValue())),
BONUS(1 << 3, 6, "属性奖励", (p, n)-> p.writeByte(n.intValue())),
PRIORITY(1 << 4, 4, "优先级", (p, n)-> p.writeByte(n.intValue())),
PERIOD(1 << 5, 7, "有效期", (p, n)-> p.writeShort(n.intValue())),
MAPLE_POINT(1 << 6, 8, "抵用券", (p, n)-> p.writeInt(n.intValue())),
MESO(1 << 7, 9, "金币", (p, n)-> p.writeInt(n.intValue())),
FOR_PREMIUM_USER(1 << 8, 10, "高级用户", (p, n)-> p.writeByte(n.intValue())),
COMMODITY_GENDER(1 << 9, 11, "性别", (p, n)-> p.writeByte(n.intValue())),
ON_SALE(1 << 10, 12, "是否销售", (p, n)-> p.writeByte(n.intValue())),
CLASS(1 << 11, 13, "标签", (p, n)-> p.writeByte(n.intValue())),
LIMIT(1 << 12, 14, "限时特卖", (p, n)-> p.writeByte(n.intValue())),
PB_CASH(1 << 13, 15, "Unknown", (p, n)-> p.writeShort(n.intValue())),
PB_POINT(1 << 14, 16, "Unknown", (p, n)-> p.writeShort(n.intValue())),
PB_GIFT(1 << 15, 17, "Unknown", (p, n)-> p.writeShort(n.intValue())),
PACKAGE_SN(1 << 16, 18, "礼包SN", (p, n)->
REQ_POP(1 << 17, -1, "Unknown83", (p, n)-> p.writeByte(0)),
REQ_LEVEL(1 << 18, -1, "Unknown83", (p, n)-> p.writeByte(0)),
TERM_START(1 << 19, -1, "Unknown83", (p, n)-> p.writeByte(0)),
TERM_END(1 << 20, -1, "Unknown83", (p, n)-> p.writeByte(0)),
REFUNDABLE(1 << 21, -1, "Unknown83", (p, n)-> p.writeByte(0)),
BOMB_SALE(1 << 22, -1, "Unknown83", (p, n)-> p.writeByte(0)),
FORCED_CATEGORY(1 << 23, -1, "Unknown83", (p, n)-> p.writeByte(0)),
GAME_WORLD(1 << 24, -1, "Unknown83", (p, n)-> p.writeByte(0)),
TOKEN(1 << 25, -1, "Unknown83", (p, n)-> p.writeByte(0)),
LIMIT_MAX(1 << 26, -1, "Unknown83", (p, n)-> p.writeByte(0)),
LIMIT_QUEST_ID(1 << 27, -1, "Unknown83", (p, n)-> p.writeByte(0)),
ORIGINAL_PRICE(1 << 28, -1, "Unknown83", (p, n)-> p.writeByte(0)),
DISCOUNT(1 << 29, -1, "Unknown83", (p, n)-> p.writeByte(0)),
DISCOUNT_RATE(1 << 30, -1, "Unknown83", (p, n)-> p.writeByte(0)),
MILEAGE_RATE(1 << 31, -1, "Unknown83", (p, n)-> p.writeByte(0)),
CommodityFlag(int flag, int sort, String desc, BiConsumer<OutPacket, Number> writeMapper)
public static List<CommodityFlag> getAvailableSortedValues()
```

---

## `org.gms.constants.game` / `constants/game/DelayedQuestUpdate.java`

### 类型声明
```text
enum DelayedQuestUpdate
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.constants.game` / `constants/game/ExpTable.java`

### 类型声明
```text
class ExpTable
```

- 字段候选数: 4
```text
private static final int[] exp = {15, 15, 34, 57, 92, 135, 372, 560, 840, 1144, 1242, 1573, 2144, 2800, 3640, 4700, 5893, 7360, 9144, 11120, 13477, 16268, 19320, 22880, 27008, 31477, 36600, 42444, 48720, 55813, 63800, 86784, 98208, 110932, 124432, 139372, 155865, 173280, 192400, 213345, 235372, 259392, 285532, 312928, 342624, 374760, 408336, 445544, 483532, 524160, 567772, 598886, 631704, 666321, 702836, 741351, 781976, 824828, 870028, 917625, 967995, 1021041, 1076994, 1136013, 1198266, 1263930, 1333194, 1406252, 1483314, 1564600, 1650340, 1740778, 1836173, 1936794, 2042930, 2154882, 2272970, 2397528, 2528912, 2667496, 2813674, 2967863, 3130502, 3302053, 3483005, 3673873, 3875201, 4087562, 4311559, 4547832, 4797053, 5059931, 5337215, 5629694, 5938202, 6263614, 6606860, 6968915, 7350811, 7753635, 8178534, 8626718, 9099462, 9598112, 10124088, 10678888, 11264090, 11881362, 12532461, 13219239, 13943653, 14707765, 15513750, 16363902, 17260644, 18206527, 19204245, 20256637, 21366700, 22537594, 23772654, 25075395, 26449526, 27898960, 29427822, 31040466, 32741483, 34535716, 36428273, 38424542, 40530206, 42751262, 45094030, 47565183, 50171755, 52921167, 55821246, 58880250, 62106888, 65510344, 69100311, 72887008, 76881216, 81094306, 85594273, 90225770, 95170142, 100385466, 105886589, 111689174, 117809740, 124265714, 131075474, 138258410, 145834970, 153826726, 162256430, 171148082, 180526997, 190419876, 200854885, 211861732, 223471711, 223471711, 248635353, 262260570, 276632449, 291791906, 307782102, 324648562, 342439302, 361204976, 380999008, 401877754, 423900654, 447130410, 471633156, 497478653, 524740482, 553496261, 583827855, 615821622, 649568646, 685165008, 722712050, 762316670, 804091623, 848155844, 894634784, 943660770, 995373379, 1049919840, 1107455447, 1168144006, 1232158297, 1299680571, 1370903066, 1446028554, 1525246918, 1608855764, 1697021059}
private static final int[] equip = {1, 15, 19, 23, 35, 43, 98, 188, 237, 280, 304, 331, 571, 656, 840, 1060, 1193, 1467, 1784, 1976, 2357, 2791, 3052, 3560, 4128, 4469, 5123, 5844, 6276, 7093, 10000}
private static final int[] pet = {1, 1, 3, 6, 14, 31, 60, 108, 181, 287, 434, 632, 891, 1224, 1642, 2161, 2793, 3557, 4467, 5542, 6801, 8263, 9950, 11882, 14084, 16578, 19391, 22547, 26074, 30000, 2147483647}
private static final int[] mount = {1, 24, 50, 105, 134, 196, 254, 263, 315, 367, 430, 543, 587, 679, 725, 897, 1146, 1394, 1701, 2247, 2543, 2898, 3156, 3313, 3584, 3923, 4150, 4305, 4550, 5600}
```

- 方法/构造器候选数: 5
```text
public static int getExpNeededForLevel(int level)
public static int getTamenessNeededForLevel(int level)
public static int getMountExpNeededForLevel(int level)
public static int getEquipExpNeededForLevel(int level)
public static int getMountMaxLevel()
```

---

## `org.gms.constants.game` / `constants/game/GameConstants.java`

### 类型声明
```text
class GameConstants
```

- 字段候选数: 14
```text
public static String[] WORLD_NAMES = {"Scania", "Bera", "Broa", "Windia", "Khaini", "Bellocan", "Mardia", "Kradia", "Yellonde", "Demethos", "Galicia", "El Nido", "Zenith", "Arcenia", "Kastia", "Judis", "Plana", "Kalluna", "Stius", "Croa", "Medere"}
public static final String[] stats = {"tuc", "reqLevel", "reqJob", "reqSTR", "reqDEX", "reqINT", "reqLUK", "reqPOP", "cash", "cursed", "success", "setItemID", "equipTradeBlock", "durability", "randOption", "randStat", "masterLevel", "reqSkillLevel", "elemDefault", "incRMAS", "incRMAF", "incRMAI", "incRMAL", "canLevel", "skill", "charmEXP"}
public static final int[] CASH_DATA = new int[]{50200004, 50200069, 50200117, 50100008, 50000047}
private static final int[] DROP_RATE_GAIN = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
private static final int[] MESO_RATE_GAIN = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105}
private static final int[] jobUpgradeBlob = {1, 20, 60, 110, 190}
private static final int[] jobUpgradeSpUp = {0, 1, 2, 3, 6}
private static final int[] DEFAULT_KEY = {18, 65, 2, 23, 3, 4, 5, 6, 16, 17, 19, 25, 26, 27, 31, 34, 35, 37, 38, 40, 43, 44, 45, 46, 50, 56, 59, 60, 61, 62, 63, 64, 57, 48, 29, 7, 24, 33, 41, 39}
private static final int[] DEFAULT_TYPE = {4, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 5, 6, 6, 6, 6, 6, 6, 5, 4, 5, 4, 4, 4, 4, 4}
private static final int[] DEFAULT_ACTION = {0, 106, 10, 1, 12, 13, 18, 24, 8, 5, 4, 19, 14, 15, 2, 17, 11, 3, 20, 16, 9, 50, 51, 6, 7, 53, 100, 101, 102, 103, 104, 105, 54, 22, 52, 21, 25, 26, 23, 27}
private static final int[] CUSTOM_KEY = {2, 3, 4, 5, 31, 56, 59, 32, 42, 6, 17, 29, 30, 41, 50, 60, 61, 62, 63, 64, 65, 16, 7, 9, 13, 8}
private static final int[] CUSTOM_TYPE = {4, 4, 4, 4, 5, 5, 6, 5, 5, 4, 4, 4, 5, 4, 4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4}
private static final int[] CUSTOM_ACTION = {1, 0, 3, 2, 53, 54, 100, 52, 51, 19, 5, 9, 50, 7, 22, 101, 102, 103, 104, 105, 106, 8, 17, 26, 20, 4}
public static final int MAX_CLEAN_PACK_SIZE = 101
```

- 方法/构造器候选数: 43
```text
public static int getPlayerBonusDropRate(int slot)
public static int getPlayerBonusMesoRate(int slot)
public static int getPlayerBonusExpRate(int slot)
public static int[] getCustomKey(boolean customKeyset)
public static int[] getCustomType(boolean customKeyset)
public static int[] getCustomAction(boolean customKeyset)
public static String getJobName(int jobid)
public static int getJobUpgradeLevelRange(int jobbranch)
public static int getChangeJobSpUpgrade(int jobbranch)
public static boolean isHallOfFameMap(int mapid)
public static boolean isPodiumHallOfFameMap(int mapid)
public static byte getHallOfFameBranch(Job job, int mapid)
public static int getOverallJobRankByScriptId(int scriptId)
public static boolean canPnpcBranchUseScriptId(byte branch, int scriptId)
public static int getHallOfFameMapid(Job job)
public static int getJobBranch(Job job)
public static int getJobMaxLevel(Job job)
public static int getSkillBook(final int job)
public static boolean isAranSkills(final int skill)
public static boolean isHiddenSkills(final int skill)
public static boolean isCygnus(final int job)
public static boolean isAran(final int job)
private static boolean isInBranchJobTree(int skillJobId, int jobId, int branchType)
private static boolean hasDivergedBranchJobTree(int skillJobId, int jobId, int branchType)
public static boolean isInJobTree(int skillId, int jobId)
public static boolean isPqSkill(final int skill)
public static boolean bannedBindSkills(final int skill)
public static boolean isGMSkills(final int skill)
public static boolean isFreeMarketRoom(int mapid)
public static boolean isMerchantLocked(MapleMap map)
public static boolean isDojoBossArea(int mapid)
public static boolean isAriantColiseumLobby(int mapid)
public static boolean isAriantColiseumArena(int mapid)
public static boolean isPqSkillMap(int mapid)
public static boolean isFinisherSkill(int skillId)
public static boolean isMedalQuest(short questid)
public static boolean hasSPTable(Job job)
public static int getMonsterHP(final int level)
public static String ordinal(int i)
public synchronized static String numberWithCommas(int i)
public synchronized static Number parseNumber(String value)
private static int getMaxObstacleMobDamageFromWz()
public static int selectRandomReward(int[] rewards)
```

---

## `org.gms.constants.game` / `constants/game/NextLevelType.java`

### 类型声明
```text
enum NextLevelType
```

- 字段候选数: 1
```text
private final String type
```

- 方法/构造器候选数: 11
```text
SEND_NEXT("sendNextLevel"),
SEND_LAST("sendLastLevel"),
SEND_LAST_NEXT("sendLastNextLevel"),
SEND_OK("sendOkLevel"),
SEND_SELECT("sendSelectLevel"),
SEND_NEXT_SELECT("sendNextSelectLevel"),
GET_INPUT_NUMBER("getInputNumberLevel"),
GET_INPUT_TEXT("getInputTextLevel"),
SEND_ACCEPT_DECLINE("sendAcceptDeclineLevel"),
SEND_YES_NO("sendYesNoLevel"),
NextLevelType(String type)
```

---

## `org.gms.constants.game` / `constants/game/NpcChat.java`

### 类型声明
```text
class NpcChat
```

- 字段候选数: 1
```text
public static final String NEW_LINE = "\r\n"
```

- 方法/构造器候选数: 1
```text
private NpcChat()
```

---

## `org.gms.constants.id` / `constants/id/ItemId.java`

### 类型声明
```text
class ItemId
```

- 字段候选数: 232
```text
public static final int PENDANT_OF_THE_SPIRIT = 1122017
public static final int HEART_SHAPED_CHOCOLATE = 5110000
public static final int HAPPY_BIRTHDAY = 2022153
public static final int FISHING_CHAIR = 3011000
public static final int MINI_GAME_BASE = 4080000
public static final int MATCH_CARDS = 4080100
public static final int MAGICAL_MITTEN = 1472063
public static final int RPS_CERTIFICATE_BASE = 4031332
public static final int GOLDEN_MAPLE_LEAF = 4000313
public static final int PERFECT_PITCH = 4310000
public static final int MAGIC_ROCK = 4006000
public static final int GOLDEN_CHICKEN_EFFECT = 4290000
public static final int BUMMER_EFFECT = 4290001
public static final int ARPQ_SHIELD = 2022269
public static final int ROARING_TIGER_MESSENGER = 5390006
public static final int WHITE_POTION = 2000002
public static final int BLUE_POTION = 2000003
public static final int ORANGE_POTION = 2000001
public static final int MANA_ELIXIR = 2000006
public static final int SORCERERS_POTION = 2022337
public static final int RUSSELLONS_PILLS = 2022198
public static final int RED_BEAN_PORRIDGE = 2022001
public static final int SOFT_WHITE_BUN = 2022186
public static final int AIR_BUBBLE = 2022040
public static final int RELAXER = 3010000
private static final int CHAIR_MIN = RELAXER
private static final int CHAIR_MAX = FISHING_CHAIR
public static final int SUBI_THROWING_STARS = 2070000
public static final int HWABI_THROWING_STARS = 2070007
public static final int BALANCED_FURY = 2070018
public static final int CRYSTAL_ILBI_THROWING_STARS = 2070016
private static final int THROWING_STAR_MIN = SUBI_THROWING_STARS
private static final int THROWING_STAR_MAX = 2070016
public static final int DEVIL_RAIN_THROWING_STAR = 2070014
public static final int BULLET = 2330000
private static final int BULLET_MIN = BULLET
private static final int BULLET_MAX = 2330005
public static final int BLAZE_CAPSULE = 2331000
public static final int GLAZE_CAPSULE = 2332000
public static final int BEGINNERS_GUIDE = 4161001
public static final int LEGENDS_GUIDE = 4161048
public static final int NOBLESSE_GUIDE = 4161047
public static final int RED_HWARANG_SHIRT = 1040021
public static final int BLACK_MARTIAL_ARTS_PANTS = 1060016
public static final int MITHRIL_BATTLE_GRIEVES = 1072039
public static final int GLADIUS = 1302008
public static final int MITHRIL_POLE_ARM = 1442001
public static final int MITHRIL_MAUL = 1422001
public static final int FIREMANS_AXE = 1312005
public static final int DARK_ENGRIT = 1051010
public static final int GREEN_HUNTERS_ARMOR = 1040067
public static final int GREEN_HUNTRESS_ARMOR = 1041054
public static final int GREEN_HUNTERS_PANTS = 1060056
public static final int GREEN_HUNTRESS_PANTS = 1061050
public static final int GREEN_HUNTER_BOOTS = 1072081
public static final int RYDEN = 1452005
public static final int MOUNTAIN_CROSSBOW = 1462000
public static final int BLUE_WIZARD_ROBE = 1050003
public static final int PURPLE_FAIRY_TOP = 1041041
public static final int PURPLE_FAIRY_SKIRT = 1061034
public static final int RED_MAGICSHOES = 1072075
public static final int MITHRIL_WAND = 1372003
public static final int CIRCLE_WINDED_STAFF = 1382017
public static final int DARK_BROWN_STEALER = 1040057
public static final int RED_STEAL = 1041047
public static final int DARK_BROWN_STEALER_PANTS = 1060043
public static final int RED_STEAL_PANTS = 1061043
public static final int BRONZE_CHAIN_BOOTS = 1072032
public static final int STEEL_GUARDS = 1472008
public static final int REEF_CLAW = 1332012
public static final int BROWN_PAULIE_BOOTS = 1072294
public static final int PRIME_HANDS = 1482004
public static final int COLD_MIND = 1492004
public static final int BROWN_POLLARD = 1052107
public static final int SNAIL_SHELL = 4000019
public static final int BLUE_SNAIL_SHELL = 4000000
public static final int RED_SNAIL_SHELL = 4000016
public static final int COLD_PROTECTION_SCROLl = 2041058
public static final int SPIKES_SCROLL = 2040727
public static final int VEGAS_SPELL_10 = 5610000
public static final int VEGAS_SPELL_60 = 5610001
public static final int CHAOS_SCROll_60 = 2049100
public static final int LIAR_TREE_SAP = 2049101
public static final int MAPLE_SYRUP = 2049102
public static final int WHITE_SCROLL = 2340000
public static final int CLEAN_SLATE_1 = 2049000
public static final int CLEAN_SLATE_3 = 2049001
public static final int CLEAN_SLATE_5 = 2049002
public static final int CLEAN_SLATE_20 = 2049003
public static final int RING_STR_100_SCROLL = 2041100
public static final int DRAGON_STONE_SCROLL = 2041200
public static final int BELT_STR_100_SCROLL = 2041300
public static final int ALL_CURE_POTION = 2050004
public static final int EYEDROP = 2050001
public static final int TONIC = 2050002
public static final int HOLY_WATER = 2050003
public static final int ANTI_BANISH_SCROLL = 2030100
private static final int DOJO_PARTY_ALL_CURE = 2022433
private static final int CARNIVAL_PARTY_ALL_CURE = 2022163
public static final int WHITE_ELIXIR = 2022544
public static final int PHARAOHS_BLESSING_1 = 2022585
public static final int PHARAOHS_BLESSING_2 = 2022586
public static final int PHARAOHS_BLESSING_3 = 2022587
public static final int PHARAOHS_BLESSING_4 = 2022588
public static final int DRAGON_PET = 5000028
public static final int ROBO_PET = 5000047
public static final int MESO_MAGNET = 1812000
public static final int ITEM_POUCH = 1812001
public static final int ITEM_IGNORE = 1812007
public static final int PET_SNAIL = 5000054
private static final int PERMA_PINK_BEAN = 5000060
private static final int PERMA_KINO = 5000100
private static final int PERMA_WHITE_TIGER = 5000101
private static final int PERMA_MINI_YETI = 5000102
public static final int BASIC_MONSTER_CRYSTAL_1 = 4260000
public static final int BASIC_MONSTER_CRYSTAL_2 = 4260001
public static final int BASIC_MONSTER_CRYSTAL_3 = 4260002
public static final int INTERMEDIATE_MONSTER_CRYSTAL_1 = 4260003
public static final int INTERMEDIATE_MONSTER_CRYSTAL_2 = 4260004
public static final int INTERMEDIATE_MONSTER_CRYSTAL_3 = 4260005
public static final int ADVANCED_MONSTER_CRYSTAL_1 = 4260006
public static final int ADVANCED_MONSTER_CRYSTAL_2 = 4260007
public static final int ADVANCED_MONSTER_CRYSTAL_3 = 4260008
public static final int SAFETY_CHARM = 5130000
public static final int EASTER_BASKET = 4031283
public static final int EASTER_CHARM = 4140903
public static final int ENGAGEMENT_BOX_MOONSTONE = 2240000
public static final int ENGAGEMENT_BOX_STAR = 2240001
public static final int ENGAGEMENT_BOX_GOLDEN = 2240002
public static final int ENGAGEMENT_BOX_SILVER = 2240003
public static final int EMPTY_ENGAGEMENT_BOX_MOONSTONE = 4031357
public static final int ENGAGEMENT_RING_MOONSTONE = 4031358
public static final int EMPTY_ENGAGEMENT_BOX_STAR = 4031359
public static final int ENGAGEMENT_RING_STAR = 4031360
public static final int EMPTY_ENGAGEMENT_BOX_GOLDEN = 4031361
public static final int ENGAGEMENT_RING_GOLDEN = 4031362
public static final int EMPTY_ENGAGEMENT_BOX_SILVER = 4031363
public static final int ENGAGEMENT_RING_SILVER = 4031364
public static final int PARENTS_BLESSING = 4031373
public static final int OFFICIATORS_PERMISSION = 4031374
public static final int ONYX_CHEST_FOR_COUPLE = 4031424
public static final int NORMAL_WEDDING_TICKET_CATHEDRAL = 5251000
public static final int NORMAL_WEDDING_TICKET_CHAPEL = 5251001
public static final int PREMIUM_WEDDING_TICKET_CHAPEL = 5251002
public static final int PREMIUM_WEDDING_TICKET_CATHEDRAL = 5251003
public static final int PREMIUM_CATHEDRAL_RESERVATION_RECEIPT = 4031375
public static final int PREMIUM_CHAPEL_RESERVATION_RECEIPT = 4031376
public static final int NORMAL_CATHEDRAL_RESERVATION_RECEIPT = 4031480
public static final int NORMAL_CHAPEL_RESERVATION_RECEIPT = 4031481
public static final int INVITATION_CHAPEL = 4031377
public static final int INVITATION_CATHEDRAL = 4031395
public static final int RECEIVED_INVITATION_CHAPEL = 4031406
public static final int RECEIVED_INVITATION_CATHEDRAL = 4031407
public static final int CARAT_RING_BOX_BASE = 2240004
private static final int CARAT_RING_BOX_MAX = 2240015
public static final int ENGAGEMENT_BOX_MIN = ENGAGEMENT_BOX_MOONSTONE
public static final int ENGAGEMENT_BOX_MAX = CARAT_RING_BOX_MAX
public static final int WEDDING_RING_MOONSTONE = 1112803
public static final int WEDDING_RING_STAR = 1112806
public static final int WEDDING_RING_GOLDEN = 1112807
public static final int WEDDING_RING_SILVER = 1112809
public static final int ROSE_SCENT = 2022631
public static final int FREESIA_SCENT = 2022632
public static final int LAVENDER_SCENT = 2022633
public static final int WHEEL_OF_FORTUNE = 5510000
public static final int CASH_SHOP_SURPRISE = 5222000
public static final int EXP_COUPON_2X_4H = 5211048
public static final int DROP_COUPON_2X_4H = 5360042
public static final int EXP_COUPON_3X_2H = 5211060
public static final int QUICK_DELIVERY_TICKET = 5330000
public static final int CHALKBOARD_1 = 5370000
public static final int CHALKBOARD_2 = 5370001
public static final int REMOTE_GACHAPON_TICKET = 5451000
public static final int AP_RESET = 5050000
public static final int NAME_CHANGE = 5400000
public static final int WORLD_TRANSFER = 5401000
public static final int MAPLE_LIFE_B = 5432000
public static final int VICIOUS_HAMMER = 5570000
public static final int NX_CARD_100 = 4031865
public static final int NX_CARD_250 = 4031866
private static final int FACE_EXPRESSION_MIN = 5160000
private static final int FACE_EXPRESSION_MAX = 5160014
public static final int NEW_YEARS_CARD = 2160101
public static final int NEW_YEARS_CARD_SEND = 4300000
public static final int NEW_YEARS_CARD_RECEIVED = 4301000
private static final int WORK_GLOVES = 1082002
private static final int STEELY_THROWING_KNIVES = 2070005
private static final int ILBI_THROWING_STARS = 2070006
private static final int OWL_BALL_MASK = 1022047
private static final int PINK_ADVENTURER_CAPE = 1102041
private static final int CLAW_30_SCROLL = 2044705
private static final int HELMET_60_ACC_SCROLL = 2040017
private static final int MAPLE_SHIELD = 1092030
private static final int GLOVES_ATT_60_SCROLL = 2040804
public static final int GREEN_PRIMROSE_SEED = 4001095
public static final int PURPLE_PRIMROSE_SEED = 4001096
public static final int PINK_PRIMROSE_SEED = 4001097
public static final int BROWN_PRIMROSE_SEED = 4001098
public static final int YELLOW_PRIMROSE_SEED = 4001099
public static final int BLUE_PRIMROSE_SEED = 4001100
public static final int PHEROMONE_PERFUME = 2270000
public static final int POUCH = 2270001
public static final int GHOST_SACK = 4031830
public static final int ARPQ_ELEMENT_ROCK = 2270002
public static final int ARPQ_SPIRIT_JEWEL = 4031868
public static final int MAGIC_CANE = 2270003
public static final int TAMED_RUDOLPH = 4031887
public static final int TRANSPARENT_MARBLE_1 = 2270005
public static final int MONSTER_MARBLE_1 = 2109001
public static final int TRANSPARENT_MARBLE_2 = 2270006
public static final int MONSTER_MARBLE_2 = 2109002
public static final int TRANSPARENT_MARBLE_3 = 2270007
public static final int MONSTER_MARBLE_3 = 2109003
public static final int EPQ_PURIFICATION_MARBLE = 2270004
public static final int EPQ_MONSTER_MARBLE = 4001169
public static final int FISH_NET = 2270008
public static final int FISH_NET_WITH_A_CATCH = 2022323
public static final int BATTLESHIP = 1932000
public static final int HOG = 1902000
private static final int SILVER_MANE = 1902001
private static final int RED_DRACO = 1902002
private static final int EXPLORER_SADDLE = 1912000
private static final int MIMIANA = 1902005
private static final int MIMIO = 1902006
private static final int SHINJOU = 1902007
private static final int CYGNUS_SADDLE = 1912005
public static final int GREEN_HEADBAND = 1002067
public static final int TIMELESS_NIBLEHEIM = 1402046
public static final int BLUE_KORBEN = 1082140
public static final int MITHRIL_PLATINE_PANTS = 1060091
public static final int BLUE_CARZEN_BOOTS = 1072154
public static final int MITHRIL_PLATINE = 1040103
```

- 方法/构造器候选数: 20
```text
public static boolean isExpIncrease(int itemId)
public static boolean isRateCoupon(int itemId)
public static boolean isMonsterCard(int itemId)
public static boolean isPyramidBuff(int itemId)
public static boolean isDojoBuff(int itemId)
public static boolean isChair(int itemId)
public static int[] allThrowingStarIds()
public static int[] allBulletIds()
public static boolean isPartyAllCure(int itemId)
public static boolean isPet(int itemId)
public static int[] getPermaPets()
public static boolean isWeddingToken(int itemId)
public static boolean isWeddingRing(int itemId)
public static boolean isNxCard(int itemId)
public static boolean isCashPackage(int itemId)
public static boolean isFaceExpression(int itemId)
public static int[] getOwlItems()
public static boolean isExplorerMount(int itemId)
public static boolean isCygnusMount(int itemId)
public static int getGender(int itemId)
```

---

## `org.gms.constants.id` / `constants/id/MapId.java`

### 类型声明
```text
class MapId
```

- 字段候选数: 177
```text
public static final int NONE = 999999999
public static final int GM_MAP = 180000000
public static final int DEVELOPERS_HQ = 777777777
public static final int ORBIS_TOWER_BOTTOM = 200082300
public static final int INTERNET_CAFE = 193000000
public static final int CRIMSONWOOD_VALLEY_1 = 610020000
public static final int CRIMSONWOOD_VALLEY_2 = 610020001
public static final int HENESYS_PQ = 910010000
public static final int ORIGIN_OF_CLOCKTOWER = 220080001
public static final int CAVE_OF_PIANUS = 230040420
public static final int GUILD_HQ = 200000301
public static final int FM_ENTRANCE = 910000000
public static final int BEIDOU_BEGINNER = 4
public static final int MUSHROOM_TOWN = 10000
public static final int SOUTHPERRY = 2000000
public static final int AMHERST = 1000000
public static final int HENESYS = 100000000
public static final int ELLINIA = 101000000
public static final int PERION = 102000000
public static final int KERNING_CITY = 103000000
public static final int LITH_HARBOUR = 104000000
public static final int SLEEPYWOOD = 105040300
public static final int MUSHROOM_KINGDOM = 106020000
public static final int FLORINA_BEACH = 110000000
public static final int EREVE = 130000000
public static final int KERNING_SQUARE = 103040000
public static final int RIEN = 140000000
public static final int ORBIS = 200000000
public static final int EL_NATH = 211000000
public static final int LUDIBRIUM = 220000000
public static final int AQUARIUM = 230000000
public static final int LEAFRE = 240000000
public static final int NEO_CITY = 240070000
public static final int MU_LUNG = 250000000
public static final int HERB_TOWN = 251000000
public static final int OMEGA_SECTOR = 221000000
public static final int KOREAN_FOLK_TOWN = 222000000
public static final int ARIANT = 260000000
public static final int MAGATIA = 261000000
public static final int TEMPLE_OF_TIME = 270000100
public static final int ELLIN_FOREST = 300000000
public static final int SINGAPORE = 540000000
public static final int BOAT_QUAY_TOWN = 541000000
public static final int KAMPUNG_VILLAGE = 551000000
public static final int NEW_LEAF_CITY = 600000000
public static final int MUSHROOM_SHRINE = 800000000
public static final int SHOWA_TOWN = 801000000
public static final int NAUTILUS_HARBOR = 120000000
public static final int HAPPYVILLE = 209000000
public static final int SHOWA_SPA_M = 809000101
public static final int SHOWA_SPA_F = 809000201
private static final int MAPLE_ISLAND_MIN = 0
private static final int MAPLE_ISLAND_MAX = 2000001
public static final int FROM_LITH_TO_RIEN = 200090060
public static final int FROM_RIEN_TO_LITH = 200090070
public static final int FROM_ELLINIA_TO_EREVE = 200090030
public static final int FROM_EREVE_TO_ELLINIA = 200090031
public static final int ELLINIA_SKY_FERRY = 101000400
public static final int FROM_EREVE_TO_ORBIS = 200090021
public static final int ORBIS_STATION = 200000161
public static final int FROM_ORBIS_TO_EREVE = 200090020
public static final int ARAN_TUTORIAL_START = 914000000
public static final int ARAN_TUTORIAL_MAX = 914000500
public static final int ARAN_INTRO = 140090000
private static final int BURNING_FOREST_1 = 914000200
private static final int BURNING_FOREST_2 = 914000210
private static final int BURNING_FOREST_3 = 914000220
public static final int ARAN_TUTO_1 = 914090010
public static final int ARAN_TUTO_2 = 914090011
public static final int ARAN_TUTO_3 = 914090012
public static final int ARAN_TUTO_4 = 914090013
public static final int ARAN_POLEARM = 914090100
public static final int STARTING_MAP_NOBLESSE = 130030000
private static final int CYGNUS_INTRO_LOCATION_MIN = 913040000
private static final int CYGNUS_INTRO_LOCATION_MAX = 913040006
public static final int CYGNUS_INTRO_LEAD = 913040100
public static final int CYGNUS_INTRO_WARRIOR = 913040101
public static final int CYGNUS_INTRO_BOWMAN = 913040102
public static final int CYGNUS_INTRO_MAGE = 913040103
public static final int CYGNUS_INTRO_PIRATE = 913040104
public static final int CYGNUS_INTRO_THIEF = 913040105
public static final int CYGNUS_INTRO_CONCLUSION = 913040106
public static final int EVENT_COCONUT_HARVEST = 109080000
public static final int EVENT_OX_QUIZ = 109020001
public static final int EVENT_PHYSICAL_FITNESS = 109040000
public static final int EVENT_OLA_OLA_0 = 109030001
public static final int EVENT_OLA_OLA_1 = 109030101
public static final int EVENT_OLA_OLA_2 = 109030201
public static final int EVENT_OLA_OLA_3 = 109030301
public static final int EVENT_OLA_OLA_4 = 109030401
public static final int EVENT_SNOWBALL = 109060000
public static final int EVENT_FIND_THE_JEWEL = 109010000
public static final int FITNESS_EVENT_LAST = 109040004
public static final int OLA_EVENT_LAST_1 = 109030003
public static final int OLA_EVENT_LAST_2 = 109030103
public static final int WITCH_TOWER_ENTRANCE = 980040000
public static final int EVENT_WINNER = 109050000
public static final int EVENT_EXIT = 109050001
public static final int EVENT_SNOWBALL_ENTRANCE = 109060001
private static final int PHYSICAL_FITNESS_MIN = EVENT_PHYSICAL_FITNESS
private static final int PHYSICAL_FITNESS_MAX = FITNESS_EVENT_LAST
private static final int OLA_OLA_MIN = EVENT_OLA_OLA_0
private static final int HAPPYVILLE_TREE_MIN = 209000001
private static final int HAPPYVILLE_TREE_MAX = 209000015
private static final int GPQ_FOUNTAIN_MIN = 990000500
private static final int GPQ_FOUNTAIN_MAX = 990000502
public static final int DOJO_SOLO_BASE = 925020000
public static final int DOJO_PARTY_BASE = 925030000
public static final int DOJO_EXIT = 925020002
private static final int DOJO_MIN = DOJO_SOLO_BASE
private static final int DOJO_MAX = 925033804
private static final int DOJO_PARTY_MIN = 925030100
public static final int DOJO_PARTY_MAX = DOJO_MAX
public static final int ANT_TUNNEL_2 = 105050100
public static final int CAVE_OF_MUSHROOMS_BASE = 105050101
public static final int SLEEPY_DUNGEON_4 = 105040304
public static final int GOLEMS_CASTLE_RUINS_BASE = 105040320
public static final int SAHEL_2 = 260020600
public static final int HILL_OF_SANDSTORMS_BASE = 260020630
public static final int RAIN_FOREST_EAST_OF_HENESYS = 100020000
public static final int HENESYS_PIG_FARM_BASE = 100020100
public static final int COLD_CRADLE = 105090311
public static final int DRAKES_BLUE_CAVE_BASE = 105090320
public static final int EOS_TOWER_76TH_TO_90TH_FLOOR = 221023400
public static final int DRUMMER_BUNNYS_LAIR_BASE = 221023401
public static final int BATTLEFIELD_OF_FIRE_AND_WATER = 240020500
public static final int ROUND_TABLE_OF_KENTAURUS_BASE = 240020512
public static final int RESTORING_MEMORY_BASE = 240040800
public static final int DESTROYED_DRAGON_NEST = 240040520
public static final int NEWT_SECURED_ZONE_BASE = 240040900
public static final int RED_NOSE_PIRATE_DEN_2 = 251010402
public static final int PILLAGE_OF_TREASURE_ISLAND_BASE = 251010410
public static final int LAB_AREA_C1 = 261020300
public static final int CRITICAL_ERROR_BASE = 261020301
public static final int FANTASY_THEME_PARK_3 = 551030000
public static final int LONGEST_RIDE_ON_BYEBYE_STATION = 551030001
private static final int BOSS_RUSH_MIN = 970030100
private static final int BOSS_RUSH_MAX = 970042711
public static final int ARPQ_LOBBY = 980010000
public static final int ARPQ_ARENA_1 = 980010101
public static final int ARPQ_ARENA_2 = 980010201
public static final int ARPQ_ARENA_3 = 980010301
public static final int ARPQ_KINGS_ROOM = 980010010
public static final int NETTS_PYRAMID = 926010001
public static final int NETTS_PYRAMID_SOLO_BASE = 926010100
public static final int NETTS_PYRAMID_PARTY_BASE = 926020100
private static final int NETTS_PYRAMID_MIN = NETTS_PYRAMID_SOLO_BASE
private static final int NETTS_PYRAMID_MAX = 926023500
private static final int ON_THE_WAY_TO_THE_HARBOR = 120010000
private static final int PIER_ON_THE_BEACH = 251000100
private static final int PEACEFUL_SHIP = 541010110
public static final int AMORIA = 680000000
public static final int CHAPEL_WEDDING_ALTAR = 680000110
public static final int CATHEDRAL_WEDDING_ALTAR = 680000210
public static final int WEDDING_PHOTO = 680000300
public static final int WEDDING_EXIT = 680000500
public static final int HALL_OF_MAGICIANS = 101000004
public static final int HALL_OF_BOWMEN = 100000204
public static final int HALL_OF_THIEVES = 103000008
public static final int NAUTILUS_TRAINING_ROOM = 120000105
public static final int KNIGHTS_CHAMBER_2 = 130000110
public static final int KNIGHTS_CHAMBER_3 = 130000120
public static final int KNIGHTS_CHAMBER_LARGE = 130000101
public static final int EXCAVATION_SITE = 990000000
public static final int SOMEONE_ELSES_HOUSE = 100000005
public static final int GRIFFEY_FOREST = 240020101
public static final int MANONS_FOREST = 240020401
public static final int HOLLOWED_GROUND = 682000001
public static final int CURSED_SANCTUARY = 105090900
public static final int DOOR_TO_ZAKUM = 211042300
public static final int DRAGON_NEST_LEFT_BEHIND = 240040511
public static final int HENESYS_PARK = 100000200
public static final int ENTRANCE_TO_HORNTAILS_CAVE = 240050400
public static final int FORGOTTEN_TWILIGHT = 270050000
public static final int CRIMSONWOOD_KEEP = 610020006
public static final int MU_LUNG_DOJO_HALL = 925020001
public static final int EXCLUSIVE_TRAINING_CENTER = 970030000
```

- 方法/构造器候选数: 11
```text
public static boolean isMapleIsland(int mapId)
public static boolean isGodlyStatMap(int mapId)
public static boolean isCygnusIntro(int mapId)
public static boolean isPhysicalFitness(int mapId)
public static boolean isOlaOla(int mapId)
public static boolean isSelfLootableOnly(int mapId)
public static boolean isDojo(int mapId)
public static boolean isPartyDojo(int mapId)
public static boolean isBossRush(int mapId)
public static boolean isNettsPyramid(int mapId)
public static boolean isFishingArea(int mapId)
```

---

## `org.gms.constants.id` / `constants/id/MobId.java`

### 类型声明
```text
class MobId
```

- 字段候选数: 74
```text
public static final int ARPQ_BOMB = 9300166
public static final int GIANT_CAKE = 9400606
public static final int TRANSPARENT_ITEM = 9300216
public static final int GREEN_MUSHROOM = 1110100
public static final int DEJECTED_GREEN_MUSHROOM = 1110130
public static final int GREEN_MUSHROOM_QUEST = 9101000
public static final int ZOMBIE_MUSHROOM = 2230101
public static final int ANNOYED_ZOMBIE_MUSHROOM = 2230131
public static final int ZOMBIE_MUSHROOM_QUEST = 9101001
public static final int GHOST_STUMP = 1140100
public static final int SMIRKING_GHOST_STUMP = 1140130
public static final int GHOST_STUMP_QUEST = 9101002
public static final int PAPULATUS_CLOCK = 8500001
public static final int HIGH_DARKSTAR = 8500003
public static final int LOW_DARKSTAR = 8500004
public static final int PIANUS_R = 8510000
public static final int BLOODY_BOOM = 8510100
public static final int PINK_BEAN = 8820001
public static final int ZAKUM_1 = 8800000
public static final int ZAKUM_2 = 8800001
public static final int ZAKUM_3 = 8800002
public static final int ZAKUM_ARM_1 = 8800003
public static final int ZAKUM_ARM_2 = 8800004
public static final int ZAKUM_ARM_3 = 8800005
public static final int ZAKUM_ARM_4 = 8800006
public static final int ZAKUM_ARM_5 = 8800007
public static final int ZAKUM_ARM_6 = 8800008
public static final int ZAKUM_ARM_7 = 8800009
public static final int ZAKUM_ARM_8 = 8800010
public static final int HORNTAIL_PREHEAD_LEFT = 8810000
public static final int HORNTAIL_PREHEAD_RIGHT = 8810001
public static final int HORNTAIL_HEAD_A = 8810002
public static final int HORNTAIL_HEAD_B = 8810003
public static final int HORNTAIL_HEAD_C = 8810004
public static final int HORNTAIL_HAND_LEFT = 8810005
public static final int HORNTAIL_HAND_RIGHT = 8810006
public static final int HORNTAIL_WINGS = 8810007
public static final int HORNTAIL_LEGS = 8810008
public static final int HORNTAIL_TAIL = 8810009
public static final int DEAD_HORNTAIL_MIN = 8810010
public static final int DEAD_HORNTAIL_MAX = 8810017
public static final int HORNTAIL = 8810018
public static final int SUMMON_HORNTAIL = 8810026
public static final int SCARLION_STATUE = 9420546
public static final int SCARLION = 9420547
public static final int ANGRY_SCARLION = 9420548
public static final int FURIOUS_SCARLION = 9420549
public static final int TARGA_STATUE = 9420541
public static final int TARGA = 9420542
public static final int ANGRY_TARGA = 9420543
public static final int FURIOUS_TARGA = 9420544
public static final int TAMABLE_HOG = 9300101
public static final int GHOST = 9500197
public static final int ARPQ_SCORPION = 9300157
public static final int LOST_RUDOLPH = 9500320
public static final int KING_SLIME_DOJO = 9300187
public static final int FAUST_DOJO = 9300189
public static final int MUSHMOM_DOJO = 9300191
public static final int POISON_FLOWER = 9300175
public static final int P_JUNIOR = 9500336
public static final int WATCH_HOG = 9300102
public static final int MOON_BUNNY = 9300061
public static final int TYLUS = 9300093
public static final int JULIET = 9300137
public static final int ROMEO = 9300138
public static final int DELLI = 9300162
public static final int GIANT_SNOWMAN_LV1_EASY = 9400322
public static final int GIANT_SNOWMAN_LV1_MEDIUM = 9400327
public static final int GIANT_SNOWMAN_LV1_HARD = 9400332
public static final int GIANT_SNOWMAN_LV5_EASY = 9400326
public static final int GIANT_SNOWMAN_LV5_MEDIUM = 9400331
public static final int GIANT_SNOWMAN_LV5_HARD = 9400336
private static final int DOJO_BOSS_MIN = 9300184
private static final int DOJO_BOSS_MAX = 9300215
```

- 方法/构造器候选数: 3
```text
public static boolean isZakumArm(int mobId)
public static boolean isDeadHorntailPart(int mobId)
public static boolean isDojoBoss(int mobId)
```

---

## `org.gms.constants.id` / `constants/id/NpcId.java`

### 类型声明
```text
class NpcId
```

- 字段候选数: 31
```text
public static final int CUSTOM_DEV = 9977777
public static final int MAPLE_ADMINISTRATOR = 9010000
public static final int STEWARD = 9201143
public static final int DIMENSIONAL_MIRROR = 9010022
public static final int SPINEL = 9000020
public static final int DUEY = 9010009
public static final int RPS_ADMIN = 9000019
public static final int GRANDPA_MOON_BUNNY = 9001105
public static final int FREDRICK = 9030000
public static final int MAR_THE_FAIRY = 1032102
public static final int HERACLE = 2010007
public static final int MIMO = 1101008
public static final int LILIN = 1202000
public static final int BILLY = 1052015
public static final int TEMPLE_KEEPER = 2140000
public static final int GACHAPON_HENESYS = 9100100
public static final int GACHAPON_ELLINIA = 9100101
public static final int GACHAPON_PERION = 9100102
public static final int GACHAPON_KERNING = 9100103
public static final int GACHAPON_SLEEPYWOOD = 9100104
public static final int GACHAPON_MUSHROOM_SHRINE = 9100105
public static final int GACHAPON_SHOWA_MALE = 9100106
public static final int GACHAPON_SHOWA_FEMALE = 9100107
public static final int GACHAPON_LUDIBRIUM = 9100108
public static final int GACHAPON_NLC = 9100109
public static final int GACHAPON_EL_NATH = 9100110
public static final int GACHAPON_NAUTILUS = 9100117
public static final int GACHAPON_MIN = GACHAPON_HENESYS
public static final int GACHAPON_MAX = GACHAPON_NAUTILUS
public static final int PLAYER_NPC_BASE = 9900000
public static final int BEI_DOU_NPC_BASE = 9900001
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.inventory` / `constants/inventory/EquipSlot.java`

### 类型声明
```text
enum EquipSlot
```

- 字段候选数: 2
```text
private String name
private int[] allowed
```

- 方法/构造器候选数: 27
```text
HAT("Cp", -1),
SPECIAL_HAT("HrCp", -1),
FACE_ACCESSORY("Af", -2),
EYE_ACCESSORY("Ay", -3),
EARRINGS("Ae", -4),
TOP("Ma", -5),
OVERALL("MaPn", -5),
PANTS("Pn", -6),
SHOES("So", -7),
GLOVES("GlGw", -8),
CASH_GLOVES("Gv", -8),
CAPE("Sr", -9),
SHIELD("Si", -10),
WEAPON("Wp", -11),
WEAPON_2("WpSi", -11),
LOW_WEAPON("WpSp", -11),
RING("Ri", -12, -13, -15, -16),
PENDANT("Pe", -17),
TAMED_MOB("Tm", -18),
SADDLE("Sd", -19),
MEDAL("Me", -49),
BELT("Be", -50),
EquipSlot()
EquipSlot(String wz, int... in)
public String getName()
public boolean isAllowed(int slot, boolean cash)
public static EquipSlot getFromTextSlot(String slot)
```

---

## `org.gms.constants.inventory` / `constants/inventory/EquipType.java`

### 类型声明
```text
enum EquipType
```

- 字段候选数: 1
```text
private final int i
```

- 方法/构造器候选数: 37
```text
UNDEFINED(-1),
ACCESSORY(0),
CAP(100),
CAPE(110),
COAT(104),
FACE(2),
GLOVES(108),
HAIR(3),
LONGCOAT(105),
PANTS(106),
PET_EQUIP(180),
PET_EQUIP_FIELD(181),
PET_EQUIP_LABEL(182),
PET_EQUIP_QUOTE(183),
RING(111),
SHIELD(109),
SHOES(107),
TAMING(190),
TAMING_SADDLE(191),
SWORD(1302),
AXE(1312),
MACE(1322),
DAGGER(1332),
WAND(1372),
STAFF(1382),
SWORD_2H(1402),
AXE_2H(1412),
MACE_2H(1422),
SPEAR(1432),
POLEARM(1442),
BOW(1452),
CROSSBOW(1462),
CLAW(1472),
KNUCKLER(1482),
EquipType(int val)
public int getValue()
public static EquipType getEquipTypeById(int itemid)
```

---

## `org.gms.constants.inventory` / `constants/inventory/ItemConstants.java`

### 类型声明
```text
class ItemConstants
```

- 字段候选数: 9
```text
public final static short LOCK = 0x01
public final static short SPIKES = 0x02
public final static short KARMA_USE = 0x02
public final static short COLD = 0x04
public final static short UNTRADEABLE = 0x08
public final static short KARMA_EQP = 0x10
public final static short PET_COME = 0x80
public final static short ACCOUNT_SHARING = 0x100
public final static short MERGE_UNTRADEABLE = 0x200
```

- 方法/构造器候选数: 48
```text
public static int getFlagByInt(int type)
public static boolean isThrowingStar(int itemId)
public static boolean isBullet(int itemId)
public static boolean isPotion(int itemId)
public static boolean isFood(int itemId)
public static boolean isConsumable(int itemId)
public static boolean isRechargeable(int itemId)
public static boolean isArrowForCrossBow(int itemId)
public static boolean isArrowForBow(int itemId)
public static boolean isArrow(int itemId)
public static boolean isPet(int itemId)
public static boolean isExpirablePet(int itemId)
public static boolean isPermanentItem(int itemId)
public static boolean isNewYearCardEtc(int itemId)
public static boolean isNewYearCardUse(int itemId)
public static boolean isAccessory(int itemId)
public static boolean isTaming(int itemId)
public static boolean isTownScroll(int itemId)
public static boolean isAntibanishScroll(int itemId)
public static boolean isCleanSlate(int scrollId)
public static boolean isModifierScroll(int scrollId)
public static boolean isFlagModifier(int scrollId, short flag)
public static boolean isChaosScroll(int scrollId)
public static boolean isRateCoupon(int itemId)
public static boolean isExpCoupon(int couponId)
public static boolean isPartyItem(int itemId)
public static boolean isHiredMerchant(int itemId)
public static boolean isPlayerShop(int itemId)
public static InventoryType getInventoryType(final int itemId)
public static boolean isMakerReagent(int itemId)
public static boolean isOverall(int itemId)
public static boolean isCashStore(int itemId)
public static boolean isMapleLife(int itemId)
public static boolean isWeapon(int itemId)
public static boolean isEquipment(int itemId)
public static boolean isFishingChair(int itemId)
public static boolean isMedal(int itemId)
public static boolean isFace(int itemId)
public static boolean isHair(int itemId)
public static boolean isNewCharDefaultFace(int job, int gender, int faceId)
public static boolean isNewCharDefaultHair(int gender, int hairId)
public static boolean isNewCharDefaultHairColor(int hairColor)
public static boolean isNewCharDefaultSkinColor(int skinColor)
public static boolean isNewCharDefaultTop(int job, int gender, int topId)
public static boolean isNewCharDefaultBottom(int job, int gender, int bottomId)
public static boolean isNewCharDefaultShoes(int job, int shoesId)
public static boolean isNewCharDefaultWeapon(int job, int weaponId)
public static boolean notValidHairColor(int hairColor)
```

---

## `org.gms.constants.net` / `constants/net/OpcodeConstants.java`

### 类型声明
```text
class OpcodeConstants
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static void generateOpcodeNames()
public static void init(Opcode[] sendValues, Opcode[] recvValues)
```

---

## `org.gms.constants.net` / `constants/net/ServerConstants.java`

### 类型声明
```text
class ServerConstants
```

- 字段候选数: 4
```text
public static final short VERSION = 83
public static final String LEVEL_200 = "[Congrats] %s has reached Level %d! Congratulate %s on such an amazing achievement!"
public static final String BEI_DOU_VERSION = "1.10"
public static final String BEI_DOU_BUILD_TIME = "2025-06-22 12:45:59"
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Aran.java`

### 类型声明
```text
class Aran
```

- 字段候选数: 29
```text
public static final int COMBO_ABILITY = 21000000
public static final int DOUBLE_SWING = 21000002
public static final int COMBAT_STEP = 21001001
public static final int POLEARM_BOOSTER = 21001003
public static final int POLEARM_MASTERY = 21100000
public static final int TRIPLE_SWING = 21100001
public static final int FINAL_CHARGE = 21100002
public static final int COMBO_DRAIN = 21100005
public static final int COMBO_SMASH = 21100004
public static final int BODY_PRESSURE = 21101003
public static final int FULL_SWING = 21110002
public static final int COMBO_CRITICAL = 21110000
public static final int COMBO_FENRIR = 21110004
public static final int SNOW_CHARGE = 21111005
public static final int SMART_KNOCKBACK = 21111001
public static final int ROLLING_SPIN = 21110006
public static final int HIDDEN_FULL_DOUBLE = 21110007
public static final int HIDDEN_FULL_TRIPLE = 21110008
public static final int MAPLE_WARRIOR = 21121000
public static final int HIGH_MASTERY = 21120001
public static final int OVER_SWING = 21120002
public static final int HIGH_DEFENSE = 21120004
public static final int FINAL_BLOW = 21120005
public static final int COMBO_TEMPEST = 21120006
public static final int COMBO_BARRIER = 21120007
public static final int FREEZE_STANDING = 21121003
public static final int HEROS_WILL = 21121008
public static final int HIDDEN_OVER_DOUBLE = 21120009
public static final int HIDDEN_OVER_TRIPLE = 21120010
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Archer.java`

### 类型声明
```text
class Archer
```

- 字段候选数: 6
```text
public static final int BLESSING_OF_AMAZON = 3000000
public static final int EYE_OF_AMAZON = 3000002
public static final int CRITICAL_SHOT = 3000001
public static final int FOCUS = 3001003
public static final int DOUBLE_SHOT = 3001005
public static final int ARROW_BLOW = 3001004
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Assassin.java`

### 类型声明
```text
class Assassin
```

- 字段候选数: 6
```text
public static final int CLAW_MASTERY = 4100000
public static final int CRITICAL_THROW = 4100001
public static final int ENDURE = 4100002
public static final int CLAW_BOOSTER = 4101003
public static final int HASTE = 4101004
public static final int DRAIN = 4101005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Bandit.java`

### 类型声明
```text
class Bandit
```

- 字段候选数: 6
```text
public static final int DAGGER_MASTERY = 4200000
public static final int ENDURE = 4200001
public static final int DAGGER_BOOSTER = 4201002
public static final int HASTE = 4201003
public static final int STEAL = 4201004
public static final int SAVAGE_BLOW = 4201005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Beginner.java`

### 类型声明
```text
class Beginner
```

- 字段候选数: 17
```text
public static final int BLESSING_OF_THE_FAIRY = 12
public static final int FOLLOW_THE_LEADER = 8
public static final int MAP_CHAIR = 100
public static final int THREE_SNAILS = 1001
public static final int RECOVERY = 1001
public static final int NIMBLE_FEET = 1002
public static final int MONSTER_RIDER = 1004
public static final int ECHO_OF_HERO = 1005
public static final int BAMBOO_RAIN = 1009
public static final int INVINCIBLE_BARRIER = 1010
public static final int POWER_EXPLOSION = 1011
public static final int SPACESHIP = 1013
public static final int SPACE_DASH = 1014
public static final int YETI_MOUNT1 = 1017
public static final int YETI_MOUNT2 = 1018
public static final int WITCH_BROOMSTICK = 1019
public static final int BALROG_MOUNT = 1031
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Bishop.java`

### 类型声明
```text
class Bishop
```

- 字段候选数: 10
```text
public static final int MAPLE_WARRIOR = 2321000
public static final int BIG_BANG = 2321001
public static final int MANA_REFLECTION = 2321002
public static final int BAHAMUT = 2321003
public static final int INFINITY = 2321004
public static final int HOLY_SHIELD = 2321005
public static final int RESURRECTION = 2321006
public static final int ANGEL_RAY = 2321007
public static final int GENESIS = 2321008
public static final int HEROS_WILL = 2321009
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/BlazeWizard.java`

### 类型声明
```text
class BlazeWizard
```

- 字段候选数: 19
```text
public static final int INCREASING_MAX_MP = 12000000
public static final int MAGIC_GUARD = 12001001
public static final int MAGIC_ARMOR = 12001002
public static final int MAGIC_CLAW = 12001003
public static final int FLAME = 12001004
public static final int MEDITATION = 12101000
public static final int SLOW = 12101001
public static final int FIRE_ARROW = 12101002
public static final int TELEPORT = 12101003
public static final int SPELL_BOOSTER = 12101004
public static final int ELEMENTAL_RESET = 12101005
public static final int FIRE_PILLAR = 12101006
public static final int ELEMENTAL_RESISTANCE = 12110000
public static final int ELEMENT_AMPLIFICATION = 12110001
public static final int SEAL = 12111002
public static final int METEOR_SHOWER = 12111003
public static final int IFRIT = 12111004
public static final int FLAME_GEAR = 12111005
public static final int FIRE_STRIKE = 12111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Bowmaster.java`

### 类型声明
```text
class Bowmaster
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 3121000
public static final int SHARP_EYES = 3121002
public static final int DRAGONS_BREATH = 3121003
public static final int HURRICANE = 3121004
public static final int BOW_EXPERT = 3120005
public static final int PHOENIX = 3121006
public static final int HAMSTRING = 3121007
public static final int CONCENTRATE = 3121008
public static final int HEROS_WILL = 3121009
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Brawler.java`

### 类型声明
```text
class Brawler
```

- 字段候选数: 8
```text
public static final int IMPROVE_MAX_HP = 5100000
public static final int KNUCKLER_MASTERY = 5100001
public static final int BACK_SPIN_BLOW = 5101002
public static final int DOUBLE_UPPERCUT = 5101003
public static final int CORKSCREW_BLOW = 5101004
public static final int MP_RECOVERY = 5101005
public static final int KNUCKLER_BOOSTER = 5101006
public static final int OAK_BARREL = 5101007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Buccaneer.java`

### 类型声明
```text
class Buccaneer
```

- 字段候选数: 10
```text
public static final int MAPLE_WARRIOR = 5121000
public static final int ENERGY_ORB = 5121002
public static final int SUPER_TRANSFORMATION = 5121003
public static final int DEMOLITION = 5121004
public static final int SNATCH = 5121005
public static final int BARRAGE = 5121007
public static final int PIRATES_RAGE = 5121008
public static final int SPEED_INFUSION = 5121009
public static final int TIME_LEAP = 5121010
public static final int DRAGON_STRIKE = 5121001
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/ChiefBandit.java`

### 类型声明
```text
class ChiefBandit
```

- 字段候选数: 7
```text
public static final int SHIELD_MASTERY = 4210000
public static final int CHAKRA = 4211001
public static final int ASSAULTER = 4211002
public static final int PICKPOCKET = 4211003
public static final int BAND_OF_THIEVES = 4211004
public static final int MESO_GUARD = 4211005
public static final int MESO_EXPLOSION = 4211006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Cleric.java`

### 类型声明
```text
class Cleric
```

- 字段候选数: 6
```text
public static final int MP_EATER = 2300000
public static final int HEAL = 2301002
public static final int INVINCIBLE = 2301003
public static final int TELEPORT = 2301001
public static final int BLESS = 2301004
public static final int HOLY_ARROW = 2301005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Corsair.java`

### 类型声明
```text
class Corsair
```

- 字段候选数: 11
```text
public static final int MAPLE_WARRIOR = 5221000
public static final int ELEMENTAL_BOOST = 5220001
public static final int WRATH_OF_THE_OCTOPI = 5220002
public static final int AERIAL_STRIKE = 5221003
public static final int RAPID_FIRE = 5221004
public static final int BATTLE_SHIP = 5221006
public static final int BATTLESHIP_CANNON = 5221007
public static final int BATTLESHIP_TORPEDO = 5221008
public static final int HYPNOTIZE = 5221009
public static final int SPEED_INFUSION = 5221010
public static final int BULLSEYE = 5220011
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Crossbowman.java`

### 类型声明
```text
class Crossbowman
```

- 字段候选数: 6
```text
public static final int CROSSBOW_MASTERY = 3200000
public static final int FINAL_ATTACK = 3200001
public static final int CROSSBOW_BOOSTER = 3201002
public static final int POWER_KNOCKBACK = 3201003
public static final int SOUL_ARROW = 3201004
public static final int IRON_ARROW = 3201005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Crusader.java`

### 类型声明
```text
class Crusader
```

- 字段候选数: 9
```text
public static final int IMPROVING_MPREC = 1110000
public static final int SHIELD_MASTERY = 1110001
public static final int COMBO = 1111002
public static final int SWORD_PANIC = 1111003
public static final int AXE_PANIC = 1111004
public static final int SWORD_COMA = 1111005
public static final int AXE_COMA = 1111006
public static final int ARMOR_CRASH = 1111007
public static final int SHOUT = 1111008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/DarkKnight.java`

### 类型声明
```text
class DarkKnight
```

- 字段候选数: 10
```text
public static final int MAPLE_WARRIOR = 1321000
public static final int MONSTER_MAGNET = 1321001
public static final int STANCE = 1321002
public static final int RUSH = 1321003
public static final int ACHILLES = 1320005
public static final int BERSERK = 1320006
public static final int BEHOLDER = 1321007
public static final int AURA_OF_BEHOLDER = 1320008
public static final int HEX_OF_BEHOLDER = 1320009
public static final int HEROS_WILL = 1321010
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/DawnWarrior.java`

### 类型声明
```text
class DawnWarrior
```

- 字段候选数: 19
```text
public static final int MAX_HP_INCREASE = 11000000
public static final int IRON_BODY = 11001001
public static final int POWER_STRIKE = 11001002
public static final int SLASH_BLAST = 11001003
public static final int SOUL = 11001004
public static final int SWORD_MASTERY = 11100000
public static final int SWORD_BOOSTER = 11101001
public static final int FINAL_ATTACK = 11101002
public static final int RAGE = 11101003
public static final int SOUL_BLADE = 11101004
public static final int SOUL_RUSH = 11101005
public static final int INCREASED_MP_RECOVERY = 11110000
public static final int COMBO = 11111001
public static final int PANIC = 11111002
public static final int COMA = 11111003
public static final int BRANDISH = 11111004
public static final int ADVANCED_COMBO = 11110005
public static final int SOUL_DRIVER = 11111006
public static final int SOUL_CHARGE = 11111007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/DragonKnight.java`

### 类型声明
```text
class DragonKnight
```

- 字段候选数: 9
```text
public static final int ELEMENTAL_RESISTANCE = 1310000
public static final int SPEAR_CRUSHER = 1311001
public static final int POLE_ARM_CRUSHER = 1311002
public static final int SPEAR_DRAGON_FURY = 1311003
public static final int POLE_ARM_DRAGON_FURY = 1311004
public static final int SACRIFICE = 1311005
public static final int DRAGON_ROAR = 1311006
public static final int POWER_CRASH = 1311007
public static final int DRAGON_BLOOD = 1311008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Evan.java`

### 类型声明
```text
class Evan
```

- 字段候选数: 43
```text
public static final int BLESSING_OF_THE_FAIRY = 20010012
public static final int THREE_SNAILS = 20011000
public static final int RECOVERY = 20011001
public static final int NIMBLE_FEET = 20011002
public static final int LEGENDARY_SPIRIT = 20011003
public static final int MONSTER_RIDER = 20011004
public static final int JUMP_DOWN = 20011006
public static final int ECHO_OF_HERO = 20011005
public static final int MAKER = 20011007
public static final int BAMBOO_THRUST = 20011009
public static final int INVINCIBLE_BARRIER = 20011010
public static final int POWER_EXPLOSION = 20011011
public static final int DRAGON_SOUL = 22000000
public static final int MAGIC_MISSILE = 22001001
public static final int FIRE_CIRCLE = 22101000
public static final int TELEPORT = 22101001
public static final int LIGHTNING_BOLT = 22111000
public static final int MAGIC_GUARD = 22111001
public static final int ICE_BREATH = 22121000
public static final int ELEMENTAL_RESET = 22121001
public static final int MAGIC_FLARE = 22131000
public static final int MAGIC_SHIELD = 22131001
public static final int CRITICAL_MAGIC = 22140000
public static final int DRAGON_THRUST = 22141001
public static final int MAGIC_BOOSTER = 22141002
public static final int SLOW = 22141003
public static final int MAGIC_AMPLIFICATION = 22150000
public static final int FIRE_BREATH = 22151001
public static final int KILLER_WINGS = 22151002
public static final int MAGIC_RESISTANCE = 22151003
public static final int DRAGON_FURY = 22160000
public static final int EARTHQUAKE = 22161001
public static final int PHANTOM_IMPRINT = 22161002
public static final int RECOVERY_AURA = 22161003
public static final int MAGIC_MASTERY = 22170001
public static final int MAPLE_WARRIOR = 22171000
public static final int ILLUSION = 22171002
public static final int FLAME_WHEEL = 22171003
public static final int HEROS_WILL = 22171004
public static final int BLESSING_OF_THE_ONYX = 22181000
public static final int BLAZE = 22181001
public static final int DARK_FOG = 22181002
public static final int SOUL_STONE = 22181003
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/FPArchMage.java`

### 类型声明
```text
class FPArchMage
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 2121000
public static final int BIG_BANG = 2121001
public static final int MANA_REFLECTION = 2121002
public static final int FIRE_DEMON = 2121003
public static final int INFINITY = 2121004
public static final int ELQUINES = 2121005
public static final int PARALYZE = 2121006
public static final int METEOR_SHOWER = 2121007
public static final int HEROS_WILL = 2121008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/FPMage.java`

### 类型声明
```text
class FPMage
```

- 字段候选数: 7
```text
public static final int PARTIAL_RESISTANCE = 2110000
public static final int ELEMENT_AMPLIFICATION = 2110001
public static final int EXPLOSION = 2111002
public static final int POISON_MIST = 2111003
public static final int SEAL = 2111004
public static final int SPELL_BOOSTER = 2111005
public static final int ELEMENT_COMPOSITION = 2111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/FPWizard.java`

### 类型声明
```text
class FPWizard
```

- 字段候选数: 6
```text
public static final int MP_EATER = 2100000
public static final int MEDITATION = 2101001
public static final int TELEPORT = 2101002
public static final int SLOW = 2101003
public static final int FIRE_ARROW = 2101004
public static final int POISON_BREATH = 2101005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Fighter.java`

### 类型声明
```text
class Fighter
```

- 字段候选数: 8
```text
public static final int SWORD_MASTERY = 1100000
public static final int AXE_MASTERY = 1100001
public static final int FINAL_ATTACK_SWORD = 1100002
public static final int FINAL_ATTACK_AXE = 1100003
public static final int SWORD_BOOSTER = 1101004
public static final int AXE_BOOSTER = 1101005
public static final int RAGE = 1101006
public static final int POWER_GUARD = 1101007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/GM.java`

### 类型声明
```text
class GM
```

- 字段候选数: 10
```text
public static final int GM_ROAR1 = 9001001
public static final int GM_TELEPORT = 9001002
public static final int HIDE = 9001004
public static final int RESURRECTION = 9001005
public static final int GM_ROAR2 = 9001006
public static final int GM_TELEPORT2 = 9001007
public static final int HYPER_BODY = 9001008
public static final int ANTI_MACRO = 9001009
public static final int HASTE = 9101000
public static final int BLESS = 9101003
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Gunslinger.java`

### 类型声明
```text
class Gunslinger
```

- 字段候选数: 7
```text
public static final int GUN_MASTERY = 5200000
public static final int INVISIBLE_SHOT = 5201001
public static final int GRENADE = 5201002
public static final int GUN_BOOSTER = 5201003
public static final int BLANK_SHOT = 5201004
public static final int WINGS = 5201005
public static final int RECOIL_SHOT = 5201006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Hermit.java`

### 类型声明
```text
class Hermit
```

- 字段候选数: 7
```text
public static final int ALCHEMIST = 4110000
public static final int MESO_UP = 4111001
public static final int SHADOW_PARTNER = 4111002
public static final int SHADOW_WEB = 4111003
public static final int SHADOW_MESO = 4111004
public static final int AVENGER = 4111005
public static final int FLASH_JUMP = 4111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Hero.java`

### 类型声明
```text
class Hero
```

- 字段候选数: 10
```text
public static final int MAPLE_WARRIOR = 1121000
public static final int MONSTER_MAGNET = 1121001
public static final int STANCE = 1121002
public static final int ADVANCED_COMBO = 1120003
public static final int ACHILLES = 1120004
public static final int GUARDIAN = 1120005
public static final int RUSH = 1121006
public static final int ENRAGE = 1121010
public static final int HEROS_WILL = 1121011
public static final int BRANDISH = 1121008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Hunter.java`

### 类型声明
```text
class Hunter
```

- 字段候选数: 6
```text
public static final int BOW_MASTERY = 3100000
public static final int FINAL_ATTACK = 3100001
public static final int BOW_BOOSTER = 3101002
public static final int POWER_KNOCKBACK = 3101003
public static final int SOUL_ARROW = 3101004
public static final int ARROW_BOMB = 3101005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/ILArchMage.java`

### 类型声明
```text
class ILArchMage
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 2221000
public static final int BIG_BANG = 2221001
public static final int MANA_REFLECTION = 2221002
public static final int ICE_DEMON = 2221003
public static final int INFINITY = 2221004
public static final int IFRIT = 2221005
public static final int BLIZZARD = 2221007
public static final int HEROS_WILL = 2221008
public static final int CHAIN_LIGHTNING = 2221006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/ILMage.java`

### 类型声明
```text
class ILMage
```

- 字段候选数: 7
```text
public static final int PARTIAL_RESISTANCE = 2210000
public static final int ELEMENT_AMPLIFICATION = 2210001
public static final int ICE_STRIKE = 2211002
public static final int THUNDER_SPEAR = 2211003
public static final int SEAL = 2211004
public static final int SPELL_BOOSTER = 2211005
public static final int ELEMENT_COMPOSITION = 2211006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/ILWizard.java`

### 类型声明
```text
class ILWizard
```

- 字段候选数: 6
```text
public static final int MP_EATER = 2200000
public static final int MEDITATION = 2201001
public static final int TELEPORT = 2201002
public static final int SLOW = 2201003
public static final int COLD_BEAM = 2201004
public static final int THUNDERBOLT = 2201005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Legend.java`

### 类型声明
```text
class Legend
```

- 字段候选数: 21
```text
public static final int THREE_SNAILS = 20001000
public static final int RECOVERY = 20001001
public static final int AGILE_BODY = 20001002
public static final int LEGENDARY_SPIRIT = 20001003
public static final int MONSTER_RIDER = 20001004
public static final int ECHO_OF_HERO = 20001005
public static final int JUMP_DOWN = 20001006
public static final int MAKER = 20001007
public static final int BAMBOO_THRUST = 20001009
public static final int INVICIBLE_BARRIER = 20001010
public static final int POWER_EXPLOSION = 20001011
public static final int METEO_SHOWER = 20001011
public static final int BLESSING_OF_THE_FAIRY = 20000012
public static final int TUTORIAL_SKILL1 = 20000014
public static final int TUTORIAL_SKILL2 = 20000015
public static final int TUTORIAL_SKILL3 = 20000016
public static final int MAP_CHAIR = 20000100
public static final int YETI_MOUNT1 = 20001019
public static final int YETI_MOUNT2 = 20001022
public static final int WITCH_BROOMSTICK = 20001023
public static final int BALROG_MOUNT = 20001031
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Magician.java`

### 类型声明
```text
class Magician
```

- 字段候选数: 6
```text
public static final int IMPROVED_MP_RECOVERY = 2000000
public static final int IMPROVED_MAX_MP_INCREASE = 2000001
public static final int MAGIC_GUARD = 2001002
public static final int MAGIC_ARMOR = 2001003
public static final int ENERGY_BOLT = 2001004
public static final int MAGIC_CLAW = 2001005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Marauder.java`

### 类型声明
```text
class Marauder
```

- 字段候选数: 6
```text
public static final int STUN_MASTERY = 5110000
public static final int ENERGY_CHARGE = 5110001
public static final int ENERGY_BLAST = 5111002
public static final int ENERGY_DRAIN = 5111004
public static final int TRANSFORMATION = 5111005
public static final int SHOCKWAVE = 5111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Marksman.java`

### 类型声明
```text
class Marksman
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 3221000
public static final int PIERCING_ARROW = 3221001
public static final int SHARP_EYES = 3221002
public static final int DRAGONS_BREATH = 3221003
public static final int MARKSMAN_BOOST = 3220004
public static final int FROST_PREY = 3221005
public static final int BLIND = 3221006
public static final int SNIPE = 3221007
public static final int HEROS_WILL = 3221008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/NightLord.java`

### 类型声明
```text
class NightLord
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 4121000
public static final int SHADOW_SHIFTER = 4120002
public static final int TAUNT = 4121003
public static final int NINJA_AMBUSH = 4121004
public static final int VENOMOUS_STAR = 4120005
public static final int SHADOW_STARS = 4121006
public static final int TRIPLE_THROW = 4121007
public static final int NINJA_STORM = 4121008
public static final int HEROS_WILL = 4121009
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/NightWalker.java`

### 类型声明
```text
class NightWalker
```

- 字段候选数: 20
```text
public static final int NIMBLE_BODY = 14000000
public static final int KEEN_EYES = 14000001
public static final int DISORDER = 14000002
public static final int DARK_SIGHT = 14001003
public static final int LUCKY_SEVEN = 14001004
public static final int DARKNESS = 14001005
public static final int CLAW_MASTERY = 14100000
public static final int CRITICAL_THROW = 14100001
public static final int CLAW_BOOSTER = 14101002
public static final int HASTE = 14101003
public static final int FLASH_JUMP = 14101004
public static final int VANISH = 14100005
public static final int VAMPIRE = 14101006
public static final int SHADOW_PARTNER = 14111000
public static final int SHADOW_WEB = 14111001
public static final int AVENGER = 14111002
public static final int ALCHEMIST = 14110003
public static final int VENOM = 14110004
public static final int TRIPLE_THROW = 14110005
public static final int POISON_BOMB = 14111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Noblesse.java`

### 类型声明
```text
class Noblesse
```

- 字段候选数: 17
```text
public static final int BLESSING_OF_THE_FAIRY = 10000012
public static final int MAP_CHAIR = 10000100
public static final int THREE_SNAILS = 10001000
public static final int RECOVERY = 10001001
public static final int NIMBLE_FEET = 10001002
public static final int MONSTER_RIDER = 10001004
public static final int ECHO_OF_HERO = 10001005
public static final int MAKER = 10001007
public static final int BAMBOO_RAIN = 10001009
public static final int INVINCIBLE_BARRIER = 10001010
public static final int POWER_EXPLOSION = 10001011
public static final int SPACESHIP = 1001014
public static final int SPACE_DASH = 1001015
public static final int YETI_MOUNT1 = 10001019
public static final int YETI_MOUNT2 = 10001022
public static final int WITCH_BROOMSTICK = 10001023
public static final int BALROG_MOUNT = 10001031
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Outlaw.java`

### 类型声明
```text
class Outlaw
```

- 字段候选数: 6
```text
public static final int BURST_FIRE = 5210000
public static final int OCTOPUS = 5211001
public static final int GAVIOTA = 5211002
public static final int FLAME_THROWER = 5211004
public static final int HOMING_BEACON = 5211006
public static final int ICE_SPLITTER = 5211005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Page.java`

### 类型声明
```text
class Page
```

- 字段候选数: 8
```text
public static final int SWORD_MASTERY = 1200000
public static final int BW_MASTERY = 1200001
public static final int FINAL_ATTACK_SWORD = 1200002
public static final int FINAL_ATTACK_BW = 1200003
public static final int SWORD_BOOSTER = 1201004
public static final int BW_BOOSTER = 1201005
public static final int THREATEN = 1201006
public static final int POWER_GUARD = 1201007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Paladin.java`

### 类型声明
```text
class Paladin
```

- 字段候选数: 12
```text
public static final int MAPLE_WARRIOR = 1221000
public static final int MONSTER_MAGNET = 1221001
public static final int STANCE = 1221002
public static final int SWORD_HOLY_CHARGE = 1221003
public static final int BW_HOLY_CHARGE = 1221004
public static final int ACHILLES = 1220005
public static final int GUARDIAN = 1220006
public static final int RUSH = 1221007
public static final int ADVANCED_CHARGE = 1220010
public static final int HEAVENS_HAMMER = 1221011
public static final int HEROS_WILL = 1221012
public static final int BLAST = 1221009
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Pirate.java`

### 类型声明
```text
class Pirate
```

- 字段候选数: 5
```text
public static final int BULLET_TIME = 5000000
public static final int FLASH_FIST = 5001001
public static final int SOMERSAULT_KICK = 5001002
public static final int DOUBLE_SHOT = 5001003
public static final int DASH = 5001005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Priest.java`

### 类型声明
```text
class Priest
```

- 字段候选数: 7
```text
public static final int ELEMENTAL_RESISTANCE = 2310000
public static final int DISPEL = 2311001
public static final int MYSTIC_DOOR = 2311002
public static final int HOLY_SYMBOL = 2311003
public static final int SHINING_RAY = 2311004
public static final int DOOM = 2311005
public static final int SUMMON_DRAGON = 2311006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Ranger.java`

### 类型声明
```text
class Ranger
```

- 字段候选数: 7
```text
public static final int THRUST = 3110000
public static final int MORTAL_BLOW = 3110001
public static final int PUPPET = 3111002
public static final int INFERNO = 3111003
public static final int ARROW_RAIN = 3111004
public static final int SILVER_HAWK = 3111005
public static final int STRAFE = 3111006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Rogue.java`

### 类型声明
```text
class Rogue
```

- 字段候选数: 6
```text
public static final int NIMBLE_BODY = 4001000
public static final int KEEN_EYES = 4001001
public static final int DARK_SIGHT = 4001003
public static final int DISORDER = 4001002
public static final int DOUBLE_STAB = 4001334
public static final int LUCKY_SEVEN = 4001344
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Shadower.java`

### 类型声明
```text
class Shadower
```

- 字段候选数: 9
```text
public static final int MAPLE_WARRIOR = 4221000
public static final int ASSASSINATE = 4221001
public static final int SHADOW_SHIFTER = 4220002
public static final int TAUNT = 4221003
public static final int NINJA_AMBUSH = 4221004
public static final int VENOMOUS_STAB = 4220005
public static final int SMOKE_SCREEN = 4221006
public static final int BOOMERANG_STEP = 4221007
public static final int HEROS_WILL = 4221008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Sniper.java`

### 类型声明
```text
class Sniper
```

- 字段候选数: 7
```text
public static final int THRUST = 3210000
public static final int MORTAL_BLOW = 3210001
public static final int PUPPET = 3211002
public static final int BLIZZARD = 3211003
public static final int ARROW_ERUPTION = 3211004
public static final int GOLDEN_EAGLE = 3211005
public static final int STRAFE = 3211006
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Spearman.java`

### 类型声明
```text
class Spearman
```

- 字段候选数: 8
```text
public static final int SPEAR_MASTERY = 1300000
public static final int POLEARM_MASTERY = 1300001
public static final int FINAL_ATTACK_SPEAR = 1300002
public static final int FINAL_ATTACK_POLEARM = 1300003
public static final int SPEAR_BOOSTER = 1301004
public static final int POLEARM_BOOSTER = 1301005
public static final int IRON_WILL = 1301006
public static final int HYPER_BODY = 1301007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/SuperGM.java`

### 类型声明
```text
class SuperGM
```

- 字段候选数: 8
```text
public static final int HEAL_PLUS_DISPEL = 9101000
public static final int HASTE = 9101001
public static final int HOLY_SYMBOL = 9101002
public static final int BLESS = 9101003
public static final int HIDE = 9101004
public static final int RESURRECTION = 9101005
public static final int SUPER_DRAGON_ROAR = 9001001
public static final int HYPER_BODY = 9101008
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/ThunderBreaker.java`

### 类型声明
```text
class ThunderBreaker
```

- 字段候选数: 20
```text
public static final int QUICK_MOTION = 15000000
public static final int FIRST_STRIKE = 15001001
public static final int SOMERSAULT_KICK = 15001002
public static final int DASH = 15001003
public static final int LIGHTNING = 15001004
public static final int IMPROVE_MAX_HP = 15100000
public static final int KNUCKLER_MASTERY = 15100001
public static final int KNUCKLER_BOOSTER = 15101002
public static final int CORKSCREW_BLOW = 15101003
public static final int ENERGY_CHARGE = 15100004
public static final int ENERGY_BLAST = 15101005
public static final int LIGHTNING_CHARGE = 15101006
public static final int CRITICAL_PUNCH = 15110000
public static final int TRANSFORMATION = 15111002
public static final int BARRAGE = 15111004
public static final int SPEED_INFUSION = 15111005
public static final int SHOCK_WAVE = 15111003
public static final int ENERGY_DRAIN = 15111001
public static final int SPARK = 15111006
public static final int SHARK_WAVE = 15111007
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/Warrior.java`

### 类型声明
```text
class Warrior
```

- 字段候选数: 6
```text
public static final int IMPROVED_HPREC = 1000000
public static final int IMPROVED_MAXHP = 1000001
public static final int ENDURE = 1000002
public static final int IRON_BODY = 1000003
public static final int POWER_STRIKE = 1000004
public static final int SLASH_BLAST = 1000005
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/WhiteKnight.java`

### 类型声明
```text
class WhiteKnight
```

- 字段候选数: 10
```text
public static final int IMPROVING_MP_RECOVERY = 1210000
public static final int SHIELD_MASTERY = 1210001
public static final int CHARGE_BLOW = 1211002
public static final int SWORD_FIRE_CHARGE = 1211003
public static final int BW_FIRE_CHARGE = 1211004
public static final int SWORD_ICE_CHARGE = 1211005
public static final int BW_ICE_CHARGE = 1211006
public static final int SWORD_LIT_CHARGE = 1211007
public static final int BW_LIT_CHARGE = 1211008
public static final int MAGIC_CRASH = 1211009
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.skills` / `constants/skills/WindArcher.java`

### 类型声明
```text
class WindArcher
```

- 字段候选数: 20
```text
public static final int CRITICAL_SHOT = 13000000
public static final int EYE_OF_AMAZON = 13000001
public static final int FOCUS = 13001002
public static final int DOUBLE_SHOT = 13001003
public static final int STORM = 13001004
public static final int BOW_MASTERY = 13100000
public static final int BOW_BOOSTER = 13101001
public static final int FINAL_ATTACK = 13101002
public static final int SOUL_ARROW = 13101003
public static final int THRUST = 13100004
public static final int STORM_BREAK = 13101005
public static final int WIND_WALK = 13101006
public static final int ARROW_RAIN = 13111000
public static final int HURRICANE = 13111002
public static final int BOW_EXPERT = 13110003
public static final int PUPPET = 13111004
public static final int EAGLE_EYE = 13111005
public static final int WIND_PIERCING = 13111006
public static final int WIND_SHOT = 13111007
public static final int STRAFE = 13111001
```

- 方法/构造器候选数: 0

---

## `org.gms.constants.string` / `constants/string/CategoryType.java`

### 类型声明
```text
enum CategoryType
```

- 字段候选数: 2
```text
private final int id
private final String name
```

- 方法/构造器候选数: 11
```text
MAIN(8, I18nUtil.getMessage("CategoryType.MAIN")),
EVENT(1, I18nUtil.getMessage("CategoryType.EVENT")),
EQUIP(2, I18nUtil.getMessage("CategoryType.EQUIP")),
USE(3, I18nUtil.getMessage("CategoryType.USE")),
SET(4, I18nUtil.getMessage("CategoryType.SET")),
ETC(5, I18nUtil.getMessage("CategoryType.ETC")),
PET(6, I18nUtil.getMessage("CategoryType.PET")),
PACKAGE(7, I18nUtil.getMessage("CategoryType.PACKAGE")),
CategoryType(final int id, final String name)
public static CategoryType ofId(int id)
public static String toName(int id)
```

---

## `org.gms.constants.string` / `constants/string/CharsetConstants.java`

### 类型声明
```text
class CharsetConstants
enum Language
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static Charset getCharset(int language)
public static Locale getLanguageLocale(int language)
public static boolean isZhCN()
private static Language loadServiceLanguage()
```

---

## `org.gms.constants.string` / `constants/string/ExtendType.java`

### 类型声明
```text
enum ExtendType
```

- 字段候选数: 1
```text
private final String type
```

- 方法/构造器候选数: 10
```text
ACCOUNT_EXTEND("11"),
ACCOUNT_EXTEND_DAILY("12"),
ACCOUNT_EXTEND_WEEKLY("13"),
CHARACTER_EXTEND("21"),
CHARACTER_EXTEND_DAILY("22"),
CHARACTER_EXTEND_WEEKLY("23"),
ExtendType(String type)
public static ExtendType getExtendType(String type)
public static boolean isAccount(String type)
public static boolean isCharacter(String type)
```

---

## `org.gms.constants.string` / `constants/string/LanguageConstants.java`

### 类型声明
```text
class LanguageConstants
enum Language
```

- 字段候选数: 13
```text
public static String[] CPQBlue = new String[4]
public static String[] CPQError = new String[4]
public static String[] CPQEntry = new String[4]
public static String[] CPQFindError = new String[4]
public static String[] CPQRed = new String[4]
public static String[] CPQPlayerExit = new String[4]
public static String[] CPQEntryLobby = new String[4]
public static String[] CPQPickRoom = new String[4]
public static String[] CPQExtendTime = new String[4]
public static String[] CPQLeaderNotFound = new String[4]
public static String[] CPQChallengeRoomAnswer = new String[4]
public static String[] CPQChallengeRoomSent = new String[4]
public static String[] CPQChallengeRoomDenied = new String[4]
```

- 方法/构造器候选数: 1
```text
public static String getMessage(Character chr, String[] message)
```

---

## `org.gms.controller` / `controller/AccountController.java`

### 类型声明
```text
class AccountController
```

- 字段候选数: 1
```text
private final AccountService accountService
```

- 方法/构造器候选数: 10
```text
public AccountController(AccountService accountService)
public ResultBody<AccountsDO> info()
public ResultBody<Page<AccountsDO>> getAccountList(@RequestParam(name = "page", required = false) Integer page,
public ResultBody<Object> register(@RequestBody SubmitBody<AddAccountDTO> submitBody) throws NoSuchAlgorithmException
public ResultBody<Object> updateByUser(@RequestBody SubmitBody<UpdateAccountByUserDTO> submitBody) throws NoSuchAlgorithmException
public ResultBody<Object> updateByGm(@PathVariable("id") int id,
public ResultBody<Object> delete(@PathVariable("id") int id)
public ResultBody<Object> resetLoggedIn(@PathVariable("id") int id)
public ResultBody<Object> banAccount(@PathVariable("id") int id,
public ResultBody<Object> unbanAccount(@PathVariable("id") int id)
```

---

## `org.gms.controller` / `controller/AuthController.java`

### 类型声明
```text
class AuthController
```

- 字段候选数: 1
```text
private final AuthService authService
```

- 方法/构造器候选数: 2
```text
public AuthController(AuthService authService)
public ResultBody<Object> logout()
```

---

## `org.gms.controller` / `controller/AutobanConfigController.java`

### 类型声明
```text
class AutobanConfigController
```

- 字段候选数: 1
```text
private final AutobanConfigService autobanConfigService
```

- 方法/构造器候选数: 2
```text
public ResultBody<List<AutobanConfigDTO>> getConfigList()
public ResultBody<Object> updateConfig(@RequestBody SubmitBody<AutobanConfigDTO> request)
```

---

## `org.gms.controller` / `controller/CashShopController.java`

### 类型声明
```text
class CashShopController
```

- 字段候选数: 1
```text
private final CashShopService cashShopService
```

- 方法/构造器候选数: 6
```text
public ResultBody<List<CashCategory>> getAllCategoryList()
public ResultBody<Page<CashShopSearchRtnDTO>> getCommodityByCategory(@RequestBody SubmitBody<CashCategory> request)
public ResultBody<CashShopSearchRtnDTO> getCommodityBySn(@PathVariable("sn") Integer sn)
public ResultBody<Object> onSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)
public ResultBody<Object> offSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)
public ResultBody<Object> batchOnSale(@RequestBody SubmitBody<CashShopBatchOnSaleReqDTO> request)
```

---

## `org.gms.controller` / `controller/CharacterController.java`

### 类型声明
```text
class CharacterController
```

- 字段候选数: 1
```text
private final CharacterService characterService
```

- 方法/构造器候选数: 4
```text
public ResultBody<Object> updateRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Object> resetRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Object> resetRates(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Page<ChrOnlineListRtnDTO>> onlineList(@RequestBody SubmitBody<ChrOnlineListReqDTO> submitBody)
```

---

## `org.gms.controller` / `controller/CommandController.java`

### 类型声明
```text
class CommandController
```

- 字段候选数: 1
```text
private final CommandService commandService
```

- 方法/构造器候选数: 5
```text
public ResultBody<Page<CommandReqDTO>> getCommandListFromDB(@RequestBody SubmitBody<CommandReqDTO> submitBody)
public ResultBody<CommandInfoDO> updateCommand(@RequestBody SubmitBody<CommandReqDTO> submitBody)
public ResultBody reloadEventsByGMCommand()
public ResultBody reloadPortalsByGMCommand()
public ResultBody reloadMapsByGMCommand()
```

---

## `org.gms.controller` / `controller/CommonController.java`

### 类型声明
```text
class CommonController
```

- 字段候选数: 1
```text
private final CommonService commonService
```

- 方法/构造器候选数: 3
```text
public ResultBody<Object> getEquipmentInfoByItemId(@RequestBody SubmitBody<EquipmentInfoReqDTO> submitBody)
public ResultBody<Integer> getAllWorldsOnlinePlayersCount(@RequestBody SubmitBody<ServerInfoReqDto> submitBody)
public ResultBody<List<InformationResult>> informationSearch(@RequestBody SubmitBody<InformationSearch> submitBody)
```

---

## `org.gms.controller` / `controller/ConfigController.java`

### 类型声明
```text
class ConfigController
```

- 字段候选数: 1
```text
private final ConfigService configService
```

- 方法/构造器候选数: 8
```text
public ResultBody<ConfigTypeDTO> getConfigTypeList()
public ResultBody<Page<GameConfigDO>> getConfigList(@RequestBody SubmitBody<GameConfigReqDTO> request)
public ResultBody<Object> addConfig(@RequestBody SubmitBody<GameConfigDO> request)
public ResultBody<Object> updateConfig(@RequestBody SubmitBody<GameConfigDO> request)
public ResultBody<Object> deleteConfig(@PathVariable("id") Long id)
public ResultBody<Object> deleteConfigList(@RequestBody SubmitBody<List<Long>> request)
public ResultBody<Object> importYml(@RequestParam("file") MultipartFile file)
public ResponseEntity<Resource> exportYml()
```

---

## `org.gms.controller` / `controller/DropController.java`

### 类型声明
```text
class DropController
```

- 字段候选数: 1
```text
private final DropService dropService
```

- 方法/构造器候选数: 8
```text
public ResultBody<Page<DropSearchRtnDTO>> getDropList(@RequestBody SubmitBody<DropSearchReqDTO> request)
public ResultBody<Page<DropSearchRtnDTO>> getGlobalDropList(@RequestBody SubmitBody<DropSearchReqDTO> request)
public ResultBody<Long> addDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)
public ResultBody<Long> addGlobalDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)
public ResultBody<Object> updateDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)
public ResultBody<Object> updateGlobalDropData(@RequestBody SubmitBody<DropSearchRtnDTO> request)
public ResultBody<Object> deleteDropData(@PathVariable("id") Long id)
public ResultBody<Object> deleteGlobalDropData(@PathVariable("id") Long id)
```

---

## `org.gms.controller` / `controller/FileController.java`

### 类型声明
```text
class FileController
```

- 字段候选数: 1
```text
private final FileTreeService fileTreeService
```

- 方法/构造器候选数: 3
```text
public ResultBody<String> treeRead(@RequestBody SubmitBody<FileReadDTO> request)
public ResultBody<String> treeWrite(@RequestBody SubmitBody<FileWriteDTO> request)
public ResultBody<List<FileTreeNodeDTO>> tree(@RequestBody SubmitBody<FileTreeDTO> request)
```

---

## `org.gms.controller` / `controller/GachaponController.java`

### 类型声明
```text
class GachaponController
```

- 字段候选数: 1
```text
private GachaponService gachaponService
```

- 方法/构造器候选数: 6
```text
public ResultBody<Page<GachaponPoolSearchRtnDTO>> getPools(@RequestBody SubmitBody<GachaponPoolSearchReqDTO> request)
public ResultBody<Object> updatePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<Object> deletePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<List<GachaponRewardDO>> getRewards(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<Object> updateReward(@RequestBody SubmitBody<GachaponRewardDO> request)
public ResultBody<Object> deleteReward(@RequestBody SubmitBody<GachaponRewardDO> request)
```

---

## `org.gms.controller` / `controller/GiveController.java`

### 类型声明
```text
class GiveController
```

- 字段候选数: 1
```text
private final GiveService giveService
```

- 方法/构造器候选数: 1
```text
public ResultBody<Object> giveResource(@RequestBody SubmitBody<GiveResourceReqDTO> submitBody)
```

---

## `org.gms.controller` / `controller/InventoryController.java`

### 类型声明
```text
class InventoryController
```

- 字段候选数: 1
```text
private final InventoryService inventoryService
```

- 方法/构造器候选数: 5
```text
public ResultBody<List<InventoryTypeRtnDTO>> getInventoryTypeList()
public ResultBody<Page<InventorySearchReqDTO>> getCharacterList(@RequestBody SubmitBody<InventorySearchReqDTO> request)
public ResultBody<List<InventorySearchRtnDTO>> getInventoryList(@RequestBody SubmitBody<InventorySearchReqDTO> request)
public ResultBody<Object> updateInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)
public ResultBody<Object> deleteInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)
```

---

## `org.gms.controller` / `controller/ServerController.java`

### 类型声明
```text
class ServerController
```

- 字段候选数: 2
```text
private final ApplicationContext applicationContext
private final ServerService serverService
```

- 方法/构造器候选数: 9
```text
public void shutdown()
public ResultBody<Object> stopServer()
public ResultBody<Object> stopServerWithMsgAndInternal( @Parameter( name = "stopConfigData", in = ParameterIn.DEFAULT, required = true, description = "停服请求参数：包含停服自定义消息，停服倒计时(单位：分钟)"
public ResultBody<Object> startServer()
public ResultBody<Object> restartServer()
public ResultBody<Boolean> online()
public ResultBody<Object> worldList()
public ResultBody<List<ChannelListRtnDTO>> channelList(@RequestParam int worldId)
public ResultBody<String> version()
```

---

## `org.gms.controller` / `controller/ShopController.java`

### 类型声明
```text
class ShopController
```

- 字段候选数: 1
```text
private final ShopService shopService
```

- 方法/构造器候选数: 6
```text
public ResultBody<Page<ShopSearchRtnDTO>> getShopList(@RequestBody SubmitBody<ShopSearchReqDTO> request)
public ResultBody<Page<ShopItemSearchRtnDTO>> getShopItemList(@RequestBody SubmitBody<ShopSearchReqDTO> request)
public ResultBody<ShopItemSearchRtnDTO> getShopItem(@PathVariable("id") Long id)
public ResultBody<Long> addShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)
public ResultBody<Object> updateShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)
public ResultBody<Object> deleteShopItem(@PathVariable("id") Long id)
```

---

## `org.gms.dao.entity` / `dao/entity/AccountsDO.java`

### 类型声明
```text
class AccountsDO
```

- 字段候选数: 31
```text
private static final long serialVersionUID = 1L
private Integer id
private String name
private String password
private String pin
private String pic
private Integer loggedin
private Timestamp lastlogin
private Timestamp createdat
private Date birthday
private Boolean banned
private String banreason
private String macs
private Integer nxCredit
private Integer maplePoint
private Integer nxPrepaid
private Integer characterslots
private Integer gender
private Timestamp tempban
private Integer greason
private Boolean tos
private String sitelogged
private Integer webadmin
private String nick
private Integer mute
private String email
private String ip
private Integer rewardpoints
private Integer votepoints
private String hwid
private Integer language
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/AllianceDO.java`

### 类型声明
```text
class AllianceDO
```

- 字段候选数: 10
```text
private static final long serialVersionUID = 1L
private Long id
private String name
private Long capacity
private String notice
private String rank1
private String rank2
private String rank3
private String rank4
private String rank5
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/AllianceguildsDO.java`

### 类型声明
```text
class AllianceguildsDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long id
private Integer allianceid
private Integer guildid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/AreaInfoDO.java`

### 类型声明
```text
class AreaInfoDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer charid
private Integer area
private String info
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/AutobanConfigDO.java`

### 类型声明
```text
class AutobanConfigDO
```

- 字段候选数: 9
```text
private static final long serialVersionUID = 1L
private Integer id
private String type
private Boolean disabled
private Integer points
private Long expireTime
private String description
private Date createTime
private Date updateTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/BbsRepliesDO.java`

### 类型声明
```text
class BbsRepliesDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Long replyid
private Long threadid
private Long postercid
private BigInteger timestamp
private String content
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/BbsThreadsDO.java`

### 类型声明
```text
class BbsThreadsDO
```

- 字段候选数: 10
```text
private static final long serialVersionUID = 1L
private Long threadid
private Long postercid
private String name
private BigInteger timestamp
private Integer icon
private Integer replycount
private String startpost
private Long guildid
private Long localthreadid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/BosslogDailyDO.java`

### 类型声明
```text
class BosslogDailyDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private String bosstype
private Timestamp attempttime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/BosslogWeeklyDO.java`

### 类型声明
```text
class BosslogWeeklyDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private String bosstype
private Timestamp attempttime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/BuddiesDO.java`

### 类型声明
```text
class BuddiesDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private Integer buddyid
private Integer pending
private String group
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/CharactersDO.java`

### 类型声明
```text
class CharactersDO
```

- 字段候选数: 75
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer accountid
private Integer world
private String name
private Integer level
private Integer exp
private Integer gachaexp
private Integer attrStr
private Integer attrDex
private Integer attrLuk
private Integer attrInt
private Integer hp
private Integer mp
private Integer maxhp
private Integer maxmp
private Integer meso
private Integer hpMpUsed
private Integer job
private Integer skincolor
private Integer gender
private Integer fame
private Integer fquest
private Integer hair
private Integer face
private Integer ap
private String sp
private Integer map
private Integer spawnpoint
private Integer gm
private Integer party
private Integer buddyCapacity
private Timestamp createdate
private Integer rank
private Integer rankMove
private Integer jobRank
private Integer jobRankMove
private Integer guildid
private Integer guildrank
private Integer messengerid
private Integer messengerposition
private Integer mountlevel
private Integer mountexp
private Integer mounttiredness
private Integer omokwins
private Integer omoklosses
private Integer omokties
private Integer matchcardwins
private Integer matchcardlosses
private Integer matchcardties
private Integer merchantmesos
private Boolean hasmerchant
private Integer equipslots
private Integer useslots
private Integer setupslots
private Integer etcslots
private Integer familyId
private Integer monsterbookcover
private Integer allianceRank
private Integer vanquisherStage
private Integer ariantPoints
private Integer dojoPoints
private Integer lastDojoStage
private Integer finishedDojoTutorial
private Integer vanquisherKills
private Long summonValue
private Integer partnerId
private Integer marriageItemId
private Integer reborns
private Integer pqpoints
private String dataString
private Timestamp lastLogoutTime
private Timestamp lastExpGainTime
private Boolean partySearch
private Long jailexpire
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/CommandInfoDO.java`

### 类型声明
```text
class CommandInfoDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer level
private String syntax
private Integer defaultLevel
private String clazz
private boolean enabled
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/CooldownsDO.java`

### 类型声明
```text
class CooldownsDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer charid
private Integer skillid
private Long length
private Long starttime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/DropDataDO.java`

### 类型声明
```text
class DropDataDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Long id
private Integer dropperid
private Integer itemid
private Integer minimumQuantity
private Integer maximumQuantity
private Integer questid
private Integer chance
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/DropDataGlobalDO.java`

### 类型声明
```text
class DropDataGlobalDO
```

- 字段候选数: 9
```text
private static final long serialVersionUID = 1L
private Long id
private Integer continent
private Integer itemid
private Integer minimumQuantity
private Integer maximumQuantity
private Integer questid
private Integer chance
private String comments
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/DueyitemsDO.java`

### 类型声明
```text
class DueyitemsDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long id
private Long packageid
private Long inventoryitemid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/DueypackagesDO.java`

### 类型声明
```text
class DueypackagesDO
```

- 字段候选数: 9
```text
private static final long serialVersionUID = 1L
private Long packageid
private Long receiverid
private String sendername
private Long mesos
private Timestamp timestamp
private String message
private Integer checked
private Integer type
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/EventstatsDO.java`

### 类型声明
```text
class EventstatsDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long characterid
private String name
private Integer info
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ExtendValueDO.java`

### 类型声明
```text
class ExtendValueDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private String extendId
private String extendType
private String extendName
private String extendValue
private Date createTime
private Date updateTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/FamelogDO.java`

### 类型声明
```text
class FamelogDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer famelogid
private Integer characterid
private Integer characteridTo
private Timestamp when
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/FamilyCharacterDO.java`

### 类型声明
```text
class FamilyCharacterDO
```

- 字段候选数: 10
```text
private static final long serialVersionUID = 1L
private Integer cid
private Integer familyid
private Integer seniorid
private Integer reputation
private Integer todaysrep
private Integer totalreputation
private Integer reptosenior
private String precepts
private Long lastresettime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/FamilyEntitlementDO.java`

### 类型声明
```text
class FamilyEntitlementDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer charid
private Integer entitlementid
private Long timestamp
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/FlywaySchemaHistoryDO.java`

### 类型声明
```text
class FlywaySchemaHistoryDO
```

- 字段候选数: 11
```text
private static final long serialVersionUID = 1L
private Integer installedRank
private String version
private String description
private String type
private String script
private Integer checksum
private String installedBy
private Timestamp installedOn
private Integer executionTime
private Boolean success
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/FredstorageDO.java`

### 类型声明
```text
class FredstorageDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Long id
private Long cid
private Long daynotes
private Timestamp timestamp
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/GachaponRewardDO.java`

### 类型声明
```text
class GachaponRewardDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer poolId
private Integer itemId
private String itemName
private Short quantity
private LocalDateTime createTime
private String comment
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/GachaponRewardPoolDO.java`

### 类型声明
```text
class GachaponRewardPoolDO
```

- 字段候选数: 12
```text
private static final long serialVersionUID = 1L
private Integer id
private String name
private Integer gachaponId
private String gachaponName
private Integer weight
private Boolean isPublic
private Integer prob
private LocalDateTime startTime
private LocalDateTime endTime
private Boolean notification
private String comment
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/GameConfigDO.java`

### 类型声明
```text
class GameConfigDO
```

- 字段候选数: 9
```text
private static final long serialVersionUID = 1L
private Long id
private String configType
private String configSubType
private String configClazz
private String configCode
private String configValue
private String configDesc
private Date updateTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/GiftsDO.java`

### 类型声明
```text
class GiftsDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Long id
private Integer to
private String from
private String message
private Long sn
private Integer ringid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/GuildsDO.java`

### 类型声明
```text
class GuildsDO
```

- 字段候选数: 18
```text
private static final long serialVersionUID = 1L
private Long guildid
private Long leader
private Long gp
private Long logo
private Integer logoColor
private String name
private String rank1title
private String rank2title
private String rank3title
private String rank4title
private String rank5title
private Long capacity
private Long logoBG
private Integer logoBGColor
private String notice
private Integer signature
private Long allianceId
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/HpMpAlertDO.java`

### 类型声明
```text
class HpMpAlertDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer cId
private Byte hp
private Byte mp
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/HwidaccountsDO.java`

### 类型声明
```text
class HwidaccountsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer accountid
private String hwid
private Integer relevance
private Timestamp expiresat
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/HwidbansDO.java`

### 类型声明
```text
class HwidbansDO
```

- 字段候选数: 3
```text
private static final long serialVersionUID = 1L
private Long hwidbanid
private String hwid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/InventoryequipmentDO.java`

### 类型声明
```text
class InventoryequipmentDO
```

- 字段候选数: 25
```text
private static final long serialVersionUID = 1L
private Long inventoryequipmentid
private Long inventoryitemid
private Integer upgradeslots
private Integer level
private Integer str
private Integer dex
private Integer inte
private Integer luk
private Integer hp
private Integer mp
private Integer watk
private Integer matk
private Integer wdef
private Integer mdef
private Integer acc
private Integer avoid
private Integer hands
private Integer speed
private Integer jump
private Integer locked
private Integer vicious
private Integer itemlevel
private Integer itemexp
private Integer ringid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/InventoryitemsDO.java`

### 类型声明
```text
class InventoryitemsDO
```

- 字段候选数: 14
```text
private static final long serialVersionUID = 1L
private Long inventoryitemid
private Integer type
private Integer characterid
private Integer accountid
private Integer itemid
private Integer inventorytype
private Integer position
private Integer quantity
private String owner
private Integer petid
private Integer flag
private Long expiration
private String giftFrom
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/InventorymerchantDO.java`

### 类型声明
```text
class InventorymerchantDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Long inventorymerchantid
private Long inventoryitemid
private Integer characterid
private Integer bundles
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/IpbansDO.java`

### 类型声明
```text
class IpbansDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long ipbanid
private String ip
private String aid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/KeymapDO.java`

### 类型声明
```text
class KeymapDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private Integer key
private Integer type
private Integer action
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/LangResourcesDO.java`

### 类型声明
```text
class LangResourcesDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Long id
private String langType
private String langBase
private String langCode
private String langValue
private String langExtend
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MacbansDO.java`

### 类型声明
```text
class MacbansDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long macbanid
private String mac
private String aid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MacfiltersDO.java`

### 类型声明
```text
class MacfiltersDO
```

- 字段候选数: 3
```text
private static final long serialVersionUID = 1L
private Long macfilterid
private String filter
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MakercreatedataDO.java`

### 类型声明
```text
class MakercreatedataDO
```

- 字段候选数: 11
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer itemid
private Integer reqLevel
private Integer reqMakerLevel
private Integer reqMeso
private Integer reqItem
private Integer reqEquip
private Integer catalyst
private Integer quantity
private Integer tuc
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MakerreagentdataDO.java`

### 类型声明
```text
class MakerreagentdataDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer itemid
private String stat
private Integer value
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MakerrecipedataDO.java`

### 类型声明
```text
class MakerrecipedataDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer itemid
private Integer reqItem
private Integer count
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MakerrewarddataDO.java`

### 类型声明
```text
class MakerrewarddataDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer itemid
private Integer rewardid
private Integer quantity
private Integer prob
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MarriagesDO.java`

### 类型声明
```text
class MarriagesDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long marriageid
private Long husbandid
private Long wifeid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MedalmapsDO.java`

### 类型声明
```text
class MedalmapsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private Long queststatusid
private Integer mapid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ModifiedCashItemDO.java`

### 类型声明
```text
class ModifiedCashItemDO
```

- 字段候选数: 19
```text
private static final long serialVersionUID = 1L
private Integer sn
private Integer itemId
private Short count
private Integer price
private Integer bonus
private Integer priority
private Long period
private Integer maplePoint
private Integer meso
private Integer forPremiumUser
private Integer commodityGender
private Integer onSale
private Integer clz
private Integer limit
private Integer pbCash
private Integer pbPoint
private Integer pbGift
private Integer packageSn
```

- 方法/构造器候选数: 3
```text
public boolean isSelling()
public Item toItem()
public ModifiedCashItemDO clone()
```

---

## `org.gms.dao.entity` / `dao/entity/MonsterbookDO.java`

### 类型声明
```text
class MonsterbookDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer charid
private Integer cardid
private Integer level
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MonstercarddataDO.java`

### 类型声明
```text
class MonstercarddataDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer cardid
private Integer mobid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MtsCartDO.java`

### 类型声明
```text
class MtsCartDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer cid
private Integer itemid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/MtsItemsDO.java`

### 类型声明
```text
class MtsItemsDO
```

- 字段候选数: 41
```text
private static final long serialVersionUID = 1L
private Long id
private Integer tab
private Integer type
private Long itemid
private Integer quantity
private Integer seller
private Integer price
private Integer bidIncre
private Integer buyNow
private Integer position
private Integer upgradeslots
private Integer level
private Integer itemlevel
private Long itemexp
private Integer ringid
private Integer str
private Integer dex
private Integer inte
private Integer luk
private Integer hp
private Integer mp
private Integer watk
private Integer matk
private Integer wdef
private Integer mdef
private Integer acc
private Integer avoid
private Integer hands
private Integer speed
private Integer jump
private Integer locked
private Integer isequip
private String owner
private String sellername
private String sellEnds
private Integer transfer
private Long vicious
private Long flag
private Long expiration
private String giftFrom
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NamechangesDO.java`

### 类型声明
```text
class NamechangesDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private String older
private String newer
private Timestamp requestTime
private Timestamp completionTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NewyearDO.java`

### 类型声明
```text
class NewyearDO
```

- 字段候选数: 12
```text
private static final long serialVersionUID = 1L
private Long id
private Integer senderid
private String sendername
private Integer receiverid
private String receivername
private String message
private Boolean senderdiscard
private Boolean receiverdiscard
private Boolean received
private Long timesent
private Long timereceived
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NotesDO.java`

### 类型声明
```text
class NotesDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Integer id
private String to
private String from
private String message
private Long timestamp
private Integer fame
private Integer deleted
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NxcodeDO.java`

### 类型声明
```text
class NxcodeDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private String code
private String retriever
private BigInteger expiration
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NxcodeItemsDO.java`

### 类型声明
```text
class NxcodeItemsDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer codeid
private Integer type
private Integer item
private Integer quantity
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/NxcouponsDO.java`

### 类型声明
```text
class NxcouponsDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer couponid
private Integer rate
private Integer activeday
private Integer starthour
private Integer endhour
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PetignoresDO.java`

### 类型声明
```text
class PetignoresDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Long id
private Integer petid
private Integer itemid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PetsDO.java`

### 类型声明
```text
class PetsDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Long petid
private String name
private Long level
private Long closeness
private Long fullness
private Boolean summoned
private Long flag
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PlayerdiseasesDO.java`

### 类型声明
```text
class PlayerdiseasesDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer charid
private Integer disease
private Integer mobskillid
private Integer mobskilllv
private Long length
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PlayernpcsDO.java`

### 类型声明
```text
class PlayernpcsDO
```

- 字段候选数: 20
```text
private static final long serialVersionUID = 1L
private Integer id
private String name
private Integer hair
private Integer face
private Integer skin
private Integer gender
private Integer x
private Integer cy
private Integer world
private Integer map
private Integer dir
private Integer scriptid
private Integer fh
private Integer rx0
private Integer rx1
private Integer worldrank
private Integer overallrank
private Integer worldjobrank
private Integer job
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PlayernpcsEquipDO.java`

### 类型声明
```text
class PlayernpcsEquipDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer npcid
private Integer equipid
private Integer type
private Short equippos
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PlayernpcsFieldDO.java`

### 类型声明
```text
class PlayernpcsFieldDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer world
private Integer map
private Integer step
private Integer podium
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/PlifeDO.java`

### 类型声明
```text
class PlifeDO
```

- 字段候选数: 16
```text
private static final long serialVersionUID = 1L
private Long id
private Integer world
private Integer map
private Integer life
private String type
private Integer cy
private Integer f
private Integer fh
private Integer rx0
private Integer rx1
private Integer x
private Integer y
private Integer hide
private Integer mobtime
private Integer team
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/QuestactionsDO.java`

### 类型声明
```text
class QuestactionsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Long questactionid
private Integer questid
private Integer status
private byte[] data
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/QuestprogressDO.java`

### 类型声明
```text
class QuestprogressDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Long id
private Integer characterid
private Long queststatusid
private Integer progressid
private String progress
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/QuestrequirementsDO.java`

### 类型声明
```text
class QuestrequirementsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Long questrequirementid
private Integer questid
private Integer status
private byte[] data
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/QueststatusDO.java`

### 类型声明
```text
class QueststatusDO
```

- 字段候选数: 10
```text
private static final long serialVersionUID = 1L
private Long queststatusid
private Integer characterid
private Integer quest
private Integer status
private Integer time
private Long expires
private Integer forfeited
private Integer completed
private Integer info
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/QuickslotkeymappedDO.java`

### 类型声明
```text
class QuickslotkeymappedDO
```

- 字段候选数: 3
```text
private static final long serialVersionUID = 1L
private Integer accountid
private Long keymap
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ReactordropsDO.java`

### 类型声明
```text
class ReactordropsDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Long reactordropid
private Integer reactorid
private Integer itemid
private Integer chance
private Integer questid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ReportsDO.java`

### 类型声明
```text
class ReportsDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Long id
private Timestamp reporttime
private Integer reporterid
private Integer victimid
private Integer reason
private String chatlog
private String description
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ResponsesDO.java`

### 类型声明
```text
class ResponsesDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private String chat
private String response
private Long id
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/RingsDO.java`

### 类型声明
```text
class RingsDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer partnerRingId
private Integer partnerChrId
private Integer itemid
private String partnername
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/SavedlocationsDO.java`

### 类型声明
```text
class SavedlocationsDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private String locationtype
private Integer map
private Integer portal
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ServerQueueDO.java`

### 类型声明
```text
class ServerQueueDO
```

- 字段候选数: 8
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer accountid
private Integer characterid
private Integer type
private Integer value
private String message
private Timestamp createTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ShopitemsDO.java`

### 类型声明
```text
class ShopitemsDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Long shopitemid
private Long shopid
private Integer itemid
private Integer price
private Integer pitch
private Integer position
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/ShopsDO.java`

### 类型声明
```text
class ShopsDO
```

- 字段候选数: 3
```text
private static final long serialVersionUID = 1L
private Long shopid
private Integer npcid
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/SkillmacrosDO.java`

### 类型声明
```text
class SkillmacrosDO
```

- 字段候选数: 9
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private Integer position
private Integer skill1
private Integer skill2
private Integer skill3
private String name
private Integer shout
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/SkillsDO.java`

### 类型声明
```text
class SkillsDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer skillid
private Integer characterid
private Integer skilllevel
private Integer masterlevel
private Long expiration
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/SpecialcashitemsDO.java`

### 类型声明
```text
class SpecialcashitemsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer sn
private Integer modifier
private Integer info
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/StoragesDO.java`

### 类型声明
```text
class StoragesDO
```

- 字段候选数: 6
```text
private static final long serialVersionUID = 1L
private Long storageid
private Integer accountid
private Integer world
private Integer slots
private Integer meso
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/TrocklocationsDO.java`

### 类型声明
```text
class TrocklocationsDO
```

- 字段候选数: 5
```text
private static final long serialVersionUID = 1L
private Integer trockid
private Integer characterid
private Integer mapid
private Integer vip
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/WishlistsDO.java`

### 类型声明
```text
class WishlistsDO
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer charid
private Integer sn
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.entity` / `dao/entity/WorldtransfersDO.java`

### 类型声明
```text
class WorldtransfersDO
```

- 字段候选数: 7
```text
private static final long serialVersionUID = 1L
private Integer id
private Integer characterid
private Integer from
private Integer to
private Timestamp requestTime
private Timestamp completionTime
```

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/AccountsMapper.java`

### 类型声明
```text
interface AccountsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/AllianceMapper.java`

### 类型声明
```text
interface AllianceMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/AllianceguildsMapper.java`

### 类型声明
```text
interface AllianceguildsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/AreaInfoMapper.java`

### 类型声明
```text
interface AreaInfoMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/AutobanConfigMapper.java`

### 类型声明
```text
interface AutobanConfigMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/BbsRepliesMapper.java`

### 类型声明
```text
interface BbsRepliesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/BbsThreadsMapper.java`

### 类型声明
```text
interface BbsThreadsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/BosslogDailyMapper.java`

### 类型声明
```text
interface BosslogDailyMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/BosslogWeeklyMapper.java`

### 类型声明
```text
interface BosslogWeeklyMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/BuddiesMapper.java`

### 类型声明
```text
interface BuddiesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/CharactersMapper.java`

### 类型声明
```text
interface CharactersMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/CommandInfoMapper.java`

### 类型声明
```text
interface CommandInfoMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/CooldownsMapper.java`

### 类型声明
```text
interface CooldownsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/DropDataGlobalMapper.java`

### 类型声明
```text
interface DropDataGlobalMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/DropDataMapper.java`

### 类型声明
```text
interface DropDataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/DueyitemsMapper.java`

### 类型声明
```text
interface DueyitemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/DueypackagesMapper.java`

### 类型声明
```text
interface DueypackagesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/EventstatsMapper.java`

### 类型声明
```text
interface EventstatsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ExtendValueMapper.java`

### 类型声明
```text
interface ExtendValueMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/FamelogMapper.java`

### 类型声明
```text
interface FamelogMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/FamilyCharacterMapper.java`

### 类型声明
```text
interface FamilyCharacterMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/FamilyEntitlementMapper.java`

### 类型声明
```text
interface FamilyEntitlementMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/FlywaySchemaHistoryMapper.java`

### 类型声明
```text
interface FlywaySchemaHistoryMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/FredstorageMapper.java`

### 类型声明
```text
interface FredstorageMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/GachaponRewardMapper.java`

### 类型声明
```text
interface GachaponRewardMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/GachaponRewardPoolMapper.java`

### 类型声明
```text
interface GachaponRewardPoolMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/GameConfigMapper.java`

### 类型声明
```text
interface GameConfigMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/GiftsMapper.java`

### 类型声明
```text
interface GiftsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/GuildsMapper.java`

### 类型声明
```text
interface GuildsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/HpMpAlertMapper.java`

### 类型声明
```text
interface HpMpAlertMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/HwidaccountsMapper.java`

### 类型声明
```text
interface HwidaccountsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/HwidbansMapper.java`

### 类型声明
```text
interface HwidbansMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/InventoryequipmentMapper.java`

### 类型声明
```text
interface InventoryequipmentMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/InventoryitemsMapper.java`

### 类型声明
```text
interface InventoryitemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/InventorymerchantMapper.java`

### 类型声明
```text
interface InventorymerchantMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/IpbansMapper.java`

### 类型声明
```text
interface IpbansMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/KeymapMapper.java`

### 类型声明
```text
interface KeymapMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/LangResourcesMapper.java`

### 类型声明
```text
interface LangResourcesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MacbansMapper.java`

### 类型声明
```text
interface MacbansMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MacfiltersMapper.java`

### 类型声明
```text
interface MacfiltersMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MakercreatedataMapper.java`

### 类型声明
```text
interface MakercreatedataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MakerreagentdataMapper.java`

### 类型声明
```text
interface MakerreagentdataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MakerrecipedataMapper.java`

### 类型声明
```text
interface MakerrecipedataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MakerrewarddataMapper.java`

### 类型声明
```text
interface MakerrewarddataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MarriagesMapper.java`

### 类型声明
```text
interface MarriagesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MedalmapsMapper.java`

### 类型声明
```text
interface MedalmapsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ModifiedCashItemMapper.java`

### 类型声明
```text
interface ModifiedCashItemMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MonsterbookMapper.java`

### 类型声明
```text
interface MonsterbookMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MonstercarddataMapper.java`

### 类型声明
```text
interface MonstercarddataMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MtsCartMapper.java`

### 类型声明
```text
interface MtsCartMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/MtsItemsMapper.java`

### 类型声明
```text
interface MtsItemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NamechangesMapper.java`

### 类型声明
```text
interface NamechangesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NewyearMapper.java`

### 类型声明
```text
interface NewyearMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NotesMapper.java`

### 类型声明
```text
interface NotesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NxcodeItemsMapper.java`

### 类型声明
```text
interface NxcodeItemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NxcodeMapper.java`

### 类型声明
```text
interface NxcodeMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/NxcouponsMapper.java`

### 类型声明
```text
interface NxcouponsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PetignoresMapper.java`

### 类型声明
```text
interface PetignoresMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PetsMapper.java`

### 类型声明
```text
interface PetsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PlayerdiseasesMapper.java`

### 类型声明
```text
interface PlayerdiseasesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PlayernpcsEquipMapper.java`

### 类型声明
```text
interface PlayernpcsEquipMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PlayernpcsFieldMapper.java`

### 类型声明
```text
interface PlayernpcsFieldMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PlayernpcsMapper.java`

### 类型声明
```text
interface PlayernpcsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/PlifeMapper.java`

### 类型声明
```text
interface PlifeMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/QuestactionsMapper.java`

### 类型声明
```text
interface QuestactionsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/QuestprogressMapper.java`

### 类型声明
```text
interface QuestprogressMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/QuestrequirementsMapper.java`

### 类型声明
```text
interface QuestrequirementsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/QueststatusMapper.java`

### 类型声明
```text
interface QueststatusMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/QuickslotkeymappedMapper.java`

### 类型声明
```text
interface QuickslotkeymappedMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ReactordropsMapper.java`

### 类型声明
```text
interface ReactordropsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ReportsMapper.java`

### 类型声明
```text
interface ReportsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ResponsesMapper.java`

### 类型声明
```text
interface ResponsesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/RingsMapper.java`

### 类型声明
```text
interface RingsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/SavedlocationsMapper.java`

### 类型声明
```text
interface SavedlocationsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ServerQueueMapper.java`

### 类型声明
```text
interface ServerQueueMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ShopitemsMapper.java`

### 类型声明
```text
interface ShopitemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/ShopsMapper.java`

### 类型声明
```text
interface ShopsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/SkillmacrosMapper.java`

### 类型声明
```text
interface SkillmacrosMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/SkillsMapper.java`

### 类型声明
```text
interface SkillsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/SpecialcashitemsMapper.java`

### 类型声明
```text
interface SpecialcashitemsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/StoragesMapper.java`

### 类型声明
```text
interface StoragesMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/TrocklocationsMapper.java`

### 类型声明
```text
interface TrocklocationsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/WishlistsMapper.java`

### 类型声明
```text
interface WishlistsMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.dao.mapper` / `dao/mapper/WorldtransfersMapper.java`

### 类型声明
```text
interface WorldtransfersMapper
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.exception` / `exception/BaseErrorInfoInterface.java`

### 类型声明
```text
interface BaseErrorInfoInterface
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.exception` / `exception/BizException.java`

### 类型声明
```text
class BizException
```

- 字段候选数: 3
```text
private static final long serialVersionUID = 1L
protected Integer errorCode
protected String errorMsg
```

- 方法/构造器候选数: 12
```text
public BizException()
public BizException(BaseErrorInfoInterface errorInfoInterface)
public BizException(BaseErrorInfoInterface errorInfoInterface, Throwable cause)
public BizException(String errorMsg)
public BizException(Integer errorCode, String errorMsg)
public BizException(Integer errorCode, String errorMsg, Throwable cause)
public static BizException illegalArgument()
public static BizException illegalArgument(String errorMsg)
public static void throwIllegalArgument()
public static void throwIllegalArgument(String errorMsg)
public String getMessage()
public Throwable fillInStackTrace()
```

---

## `org.gms.exception` / `exception/BizExceptionEnum.java`

### 类型声明
```text
enum BizExceptionEnum
```

- 字段候选数: 2
```text
private final Integer resultCode
private final String resultMsg
```

- 方法/构造器候选数: 9
```text
SUCCESS(20000, I18nUtil.getExceptionMessage("SUCCESS")),
BODY_NOT_MATCH(40000, I18nUtil.getExceptionMessage("BODY_NOT_MATCH")),
REQUEST_METHOD_SUPPORT(40001, I18nUtil.getExceptionMessage("REQUEST_METHOD_SUPPORT")),
ILLEGAL_PARAMETERS(40002, I18nUtil.getExceptionMessage("ILLEGAL_PARAMETERS")),
NOT_FOUND(40004, I18nUtil.getExceptionMessage("NOT_FOUND")),
INTERNAL_SERVER_ERROR(50000, I18nUtil.getExceptionMessage("INTERNAL_SERVER_ERROR")),
BizExceptionEnum(Integer resultCode, String resultMsg)
public Integer getResultCode()
public String getResultMsg()
```

---

## `org.gms.exception` / `exception/EmptyMovementException.java`

### 类型声明
```text
class EmptyMovementException
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public EmptyMovementException(InPacket inPacket)
```

---

## `org.gms.exception` / `exception/EventInstanceInProgressException.java`

### 类型声明
```text
class EventInstanceInProgressException
```

- 字段候选数: 1
```text
public static String EIIP_KEY = "Event instance "
```

- 方法/构造器候选数: 1
```text
public EventInstanceInProgressException(String eventName, String eventInstance)
```

---

## `org.gms.exception` / `exception/GlobalExceptionHandler.java`

### 类型声明
```text
class GlobalExceptionHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public ResultBody<Object> bizExceptionHandler(HttpServletRequest req, BizException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, RuntimeException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, ServletException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, Exception e)
```

---

## `org.gms.exception` / `exception/IdTypeNotSupportedException.java`

### 类型声明
```text
class IdTypeNotSupportedException
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public IdTypeNotSupportedException()
public IdTypeNotSupportedException(String message)
```

---

## `org.gms.exception` / `exception/NotEnabledException.java`

### 类型声明
```text
class NotEnabledException
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public NotEnabledException()
public NotEnabledException(String message)
```

---

## `org.gms.manager` / `manager/ServerManager.java`

### 类型声明
```text
class ServerManager
```

- 字段候选数: 1
```text
private static ApplicationContext applicationContext
```

- 方法/构造器候选数: 3
```text
public void setApplicationContext(@NonNull ApplicationContext applicationContext) throws BeansException
public void run(ApplicationArguments args) throws Exception
public void destroy() throws Exception
```

---

## `org.gms.model.dto` / `model/dto/AddAccountDTO.java`

### 类型声明
```text
class AddAccountDTO
```

- 字段候选数: 4
```text
private String name
private String password
private Date birthday
private Integer language
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/AutobanConfigDTO.java`

### 类型声明
```text
class AutobanConfigDTO
```

- 字段候选数: 11
```text
private Integer id
private String type
private String name
private Boolean disabled
private Integer points
private Long expireTimeSeconds
private String description
private Integer defaultPoints
private Long defaultExpireTimeSeconds
private boolean changePoints
private boolean changeExpireTime
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/BasePageDTO.java`

### 类型声明
```text
class BasePageDTO
```

- 字段候选数: 4
```text
private Integer pageNo
private Integer pageSize
private boolean onlyTotal
private boolean notPage
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/CashShopBatchOnSaleReqDTO.java`

### 类型声明
```text
class CashShopBatchOnSaleReqDTO
```

- 字段候选数: 3
```text
private ModifiedCashItemDO[] data
private String type
private Integer value
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/CashShopSearchRtnDTO.java`

### 类型声明
```text
class CashShopSearchRtnDTO
```

- 字段候选数: 39
```text
private Integer categoryId
private String categoryName
private Integer subcategoryId
private String subcategoryName
private Integer sn
private Integer itemId
private String itemName
private Integer price
private Integer defaultPrice
private Long period
private Long defaultPeriod
private Integer priority
private Integer defaultPriority
private Short count
private Short defaultCount
private Integer onSale
private Integer defaultOnSale
private Integer bonus
private Integer defaultBonus
private Integer maplePoint
private Integer defaultMaplePoint
private Integer meso
private Integer defaultMeso
private Integer forPremiumUser
private Integer defaultForPremiumUser
private Integer gender
private Integer defaultGender
private Integer clz
private Integer defaultClz
private Integer limit
private Integer defaultLimit
private Integer pbCash
private Integer defaultPBCash
private Integer pbPoint
private Integer defaultPBPoint
private Integer pbGift
private Integer defaultPBGift
private Integer packageSn
private Integer defaultPackageSn
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ChannelListRtnDTO.java`

### 类型声明
```text
class ChannelListRtnDTO
```

- 字段候选数: 2
```text
private Integer id
private Integer worldId
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ChrOnlineListReqDTO.java`

### 类型声明
```text
class ChrOnlineListReqDTO
```

- 字段候选数: 4
```text
private Integer id
private String name
private Integer map
private int world
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ChrOnlineListRtnDTO.java`

### 类型声明
```text
class ChrOnlineListRtnDTO
```

- 字段候选数: 8
```text
private int world
private int id
private String name
private int map
private int job
private String jobName
private int level
private int gm
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/CommandReqDTO.java`

### 类型声明
```text
class CommandReqDTO
```

- 字段候选数: 2
```text
private Integer id
private String clazz
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ConfigTypeDTO.java`

### 类型声明
```text
class ConfigTypeDTO
```

- 字段候选数: 2
```text
private List<String> types
private List<String> subTypes
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/DropSearchReqDTO.java`

### 类型声明
```text
class DropSearchReqDTO
```

- 字段候选数: 6
```text
private Integer dropperId
private String dropperName
private Integer continent
private Integer itemId
private String itemName
private Integer questId
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/DropSearchRtnDTO.java`

### 类型声明
```text
class DropSearchRtnDTO
```

- 字段候选数: 12
```text
private Long id
private Integer dropperId
private String dropperName
private Integer continent
private Integer itemId
private String itemName
private Integer minimumQuantity
private Integer maximumQuantity
private Integer questId
private String questName
private Integer chance
private String comments
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/EquipmentInfoReqDTO.java`

### 类型声明
```text
class EquipmentInfoReqDTO
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/EquipmentInfoRtnDTO.java`

### 类型声明
```text
class EquipmentInfoRtnDTO
```

- 字段候选数: 17
```text
private Short str
private Short dex
private Short _int
private Short luk
private Short hp
private Short mp
private Short pAtk
private Short mAtk
private Short pDef
private Short mDef
private Short acc
private Short avoid
private Short hands
private Short speed
private Short jump
private Byte upgradeSlot
private Long expire
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/FileReadDTO.java`

### 类型声明
```text
class FileReadDTO
```

- 字段候选数: 2
```text
private String title
private String currentKey
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/FileTreeDTO.java`

### 类型声明
```text
class FileTreeDTO
```

- 字段候选数: 2
```text
private String title
private String currentKey
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/FileTreeNodeDTO.java`

### 类型声明
```text
class FileTreeNodeDTO
```

- 字段候选数: 4
```text
private String title
private String key
private List<FileTreeNodeDTO> children
private boolean leaf
```

- 方法/构造器候选数: 1
```text
public FileTreeNodeDTO(File file, String key)
```

---

## `org.gms.model.dto` / `model/dto/FileWriteDTO.java`

### 类型声明
```text
class FileWriteDTO
```

- 字段候选数: 3
```text
private String title
private String currentKey
private String content
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/GachaponPoolSearchReqDTO.java`

### 类型声明
```text
class GachaponPoolSearchReqDTO
```

- 字段候选数: 1
```text
private Integer gachaponId
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/GachaponPoolSearchRtnDTO.java`

### 类型声明
```text
class GachaponPoolSearchRtnDTO
```

- 字段候选数: 1
```text
private Integer realProb
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/GameConfigReqDTO.java`

### 类型声明
```text
class GameConfigReqDTO
```

- 字段候选数: 3
```text
private String type
private String subType
private String filter
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/GiveResourceReqDTO.java`

### 类型声明
```text
class GiveResourceReqDTO
```

- 字段候选数: 24
```text
private Integer worldId
private Integer playerId
private String player
private Byte type
private Integer id
private Integer quantity
private Float rate
private Short str
private Short dex
private Short _int
private Short luk
private Short hp
private Short mp
private Short pAtk
private Short mAtk
private Short pDef
private Short mDef
private Short acc
private Short avoid
private Short hands
private Short speed
private Short jump
private Byte upgradeSlot
private Long expire
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/InventoryEquipRtnDTO.java`

### 类型声明
```text
class InventoryEquipRtnDTO
```

- 字段候选数: 24
```text
private Long id
private Long inventoryItemId
private Byte upgradeSlots
private Byte level
private Short attStr
private Short attDex
private Short attInt
private Short attLuk
private Short hp
private Short mp
private Short pAtk
private Short mAtk
private Short pDef
private Short mDef
private Short acc
private Short avoid
private Short hands
private Short speed
private Short jump
private Integer locked
private Short vicious
private Byte itemLevel
private Integer itemExp
private Integer ringId
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/InventorySearchReqDTO.java`

### 类型声明
```text
class InventorySearchReqDTO
```

- 字段候选数: 4
```text
private Byte inventoryType
private Integer characterId
private String characterName
private boolean onlineStatus
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/InventorySearchRtnDTO.java`

### 类型声明
```text
class InventorySearchRtnDTO
```

- 字段候选数: 16
```text
private Long id
private Integer characterId
private Integer itemId
private Integer itemType
private Byte inventoryType
private Short position
private Short quantity
private String owner
private Integer petId
private Short flag
private Long expiration
private String giftFrom
private boolean online
private boolean equipment
private InventoryEquipRtnDTO inventoryEquipment
private String itemName
```

- 方法/构造器候选数: 1
```text
public Item toItem()
```

---

## `org.gms.model.dto` / `model/dto/InventoryTypeRtnDTO.java`

### 类型声明
```text
class InventoryTypeRtnDTO
```

- 字段候选数: 2
```text
private Byte inventoryType
private String name
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/InventoryequipmentReqDTO.java`

### 类型声明
```text
class InventoryequipmentReqDTO
```

- 字段候选数: 2
```text
private Long inventoryequipmentid
private Long inventoryitemid
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/InventoryequipmentRtnDTO.java`

### 类型声明
```text
class InventoryequipmentRtnDTO
```

- 字段候选数: 23
```text
private Long inventoryequipmentid
private Long inventoryitemid
private Integer upgradeslots
private Integer level
private Integer str
private Integer dex
private Integer inte
private Integer luk
private Integer hp
private Integer mp
private Integer watk
private Integer matk
private Integer wdef
private Integer mdef
private Integer acc
private Integer avoid
private Integer hands
private Integer speed
private Integer jump
private Integer locked
private Long vicious
private Integer itemlevel
private Long itemexp
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ResultBody.java`

### 类型声明
```text
class ResultBody
```

- 字段候选数: 4
```text
private Integer code
private String message
private String responseId
private T data
```

- 方法/构造器候选数: 9
```text
public ResultBody()
public ResultBody(BaseErrorInfoInterface errorInfo)
public static <T> ResultBody<T> success()
public static <T> ResultBody<T> success(T data)
public static <T> ResultBody<T> success(SubmitBody<?> request, T data)
public static <T> ResultBody<T> error(HttpServletRequest req, BaseErrorInfoInterface errorInfo)
public static <T> ResultBody<T> error(HttpServletRequest req, String message)
public static <T> ResultBody<T> error(HttpServletRequest req, Integer code, String message)
public String toString()
```

---

## `org.gms.model.dto` / `model/dto/ServerInfoReqDto.java`

### 类型声明
```text
class ServerInfoReqDto
```

- 字段候选数: 1
```text
private List<Integer> worldIdList
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ServerShutdownDTO.java`

### 类型声明
```text
class ServerShutdownDTO
```

- 字段候选数: 5
```text
private int minutes
private String shutdownMsg
private Boolean showServerMsg = false
private Boolean showCenterMsg = false
private Boolean showChatMsg = false
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ShopItemSearchRtnDTO.java`

### 类型声明
```text
class ShopItemSearchRtnDTO
```

- 字段候选数: 8
```text
private Long id
private Long shopId
private Integer itemId
private Integer price
private Integer pitch
private Integer position
private String itemName
private String itemDesc
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ShopSearchReqDTO.java`

### 类型声明
```text
class ShopSearchReqDTO
```

- 字段候选数: 5
```text
private Long shopId
private Integer npcId
private String npcName
private Integer itemId
private String itemName
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/ShopSearchRtnDTO.java`

### 类型声明
```text
class ShopSearchRtnDTO
```

- 字段候选数: 3
```text
private Long shopId
private Integer npcId
private String npcName
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/SubmitBody.java`

### 类型声明
```text
class SubmitBody
```

- 字段候选数: 2
```text
private String requestId
private T data
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/UpdateAccountByGmDTO.java`

### 类型声明
```text
class UpdateAccountByGmDTO
```

- 字段候选数: 16
```text
private String newPwd
private String pin
private String pic
private Date birthday
private Integer nxCredit
private Integer maplePoint
private Integer nxPrepaid
private Integer characterslots
private Integer gender
private Integer webadmin
private String nick
private Integer mute
private String email
private Integer rewardpoints
private Integer votepoints
private Integer language
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/UpdateAccountByUserDTO.java`

### 类型声明
```text
class UpdateAccountByUserDTO
```

- 字段候选数: 8
```text
private String oldPwd
private String newPwd
private String pin
private String pic
private Date birthday
private String nick
private String email
private Integer language
```

- 方法/构造器候选数: 0

---

## `org.gms.model.dto` / `model/dto/WorldListRtnDTO.java`

### 类型声明
```text
class WorldListRtnDTO
```

- 字段候选数: 8
```text
private Integer id
private Float expRate
private Float dropRate
private Float mesoRate
private Float bossDropRate
private Float questRate
private Float travelRate
private Float fishingRate
```

- 方法/构造器候选数: 0

---

## `org.gms.model.pojo` / `model/pojo/CashCategory.java`

### 类型声明
```text
class CashCategory
```

- 字段候选数: 6
```text
private Integer id
private String name
private Integer subId
private String subName
private Boolean onSale
private Integer itemId
```

- 方法/构造器候选数: 0

---

## `org.gms.model.pojo` / `model/pojo/InformationResult.java`

### 类型声明
```text
class InformationResult
```

- 字段候选数: 4
```text
private String type
private Integer id
private String name
private String desc
```

- 方法/构造器候选数: 0

---

## `org.gms.model.pojo` / `model/pojo/InformationSearch.java`

### 类型声明
```text
class InformationSearch
```

- 字段候选数: 4
```text
private List<String> types
private String filter
private int filterType
private boolean fullMatch
```

- 方法/构造器候选数: 0

---

## `org.gms.model.pojo` / `model/pojo/NewYearCardRecord.java`

### 类型声明
```text
class NewYearCardRecord
```

- 字段候选数: 12
```text
private int id
private int senderId
private String senderName
private boolean senderDiscardCard
private int receiverId
private String receiverName
private boolean receiverDiscardCard
private boolean receiverReceivedCard
private String message
private long dateSent
private long dateReceived
private ScheduledFuture<?> sendTask
```

- 方法/构造器候选数: 11
```text
public NewYearCardRecord(int senderId, String senderName, int receiverId, String receiverName, String message)
public void setExtraNewYearCardRecord(int id, boolean senderDiscardCard, boolean receiverDiscardCard, boolean receiverReceivedCard, long dateSent, long dateReceived)
public static void saveNewYearCard(NewYearCardRecord newyear)
public static void updateNewYearCard(NewYearCardRecord newyear)
public static NewYearCardRecord loadNewYearCard(int cardid)
public static void loadPlayerNewYearCards(Character chr)
public static void printNewYearRecords(Character chr)
public void startNewYearCardTask()
public void stopNewYearCardTask()
private static void deleteNewYearCard(int id)
public static void removeAllNewYearCard(boolean send, Character chr)
```

---

## `org.gms.model.pojo` / `model/pojo/NextLevelContext.java`

### 类型声明
```text
class NextLevelContext
```

- 字段候选数: 4
```text
private NextLevelType levelType
private String lastLevel
private String nextLevel
private String prefix
```

- 方法/构造器候选数: 1
```text
public void clear()
```

---

## `org.gms.model.pojo` / `model/pojo/RateLimitContext.java`

### 类型声明
```text
class RateLimitContext
```

- 字段候选数: 2
```text
private AtomicInteger curr
private Long expire
```

- 方法/构造器候选数: 0

---

## `org.gms.model.pojo` / `model/pojo/SkillEntry.java`

### 类型声明
```text
class SkillEntry
```

- 字段候选数: 3
```text
public int masterLevel
public byte skillLevel
public long expiration
```

- 方法/构造器候选数: 2
```text
public SkillEntry(byte skillLevel, int masterLevel, long expiration)
public String toString()
```

---

## `org.gms.net` / `net/AbstractPacketHandler.java`

### 类型声明
```text
class AbstractPacketHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public boolean validateState(Client c)
protected static long currentServerTime()
```

---

## `org.gms.net` / `net/ChannelDependencies.java`

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net` / `net/PacketHandler.java`

### 类型声明
```text
interface PacketHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net` / `net/PacketProcessor.java`

### 类型声明
```text
class PacketProcessor
```

- 字段候选数: 2
```text
private static ChannelDependencies channelDeps
private PacketHandler[] handlers
```

- 方法/构造器候选数: 11
```text
private PacketProcessor()
public static void registerGameHandlerDependencies(ChannelDependencies channelDependencies)
public static PacketProcessor getLoginServerProcessor()
public static PacketProcessor getChannelServerProcessor(int world, int channel)
public PacketHandler getHandler(short packetId)
public void registerHandler(Opcode code, PacketHandler handler)
public synchronized static PacketProcessor getProcessor(int world, int channel)
public void reset(int channel)
private void registerCommonHandlers()
private void registerLoginHandlers()
private void registerChannelHandlers()
```

---

## `org.gms.net.encryption` / `net/encryption/ClientCyphers.java`

### 类型声明
```text
class ClientCyphers
```

- 字段候选数: 2
```text
private final MapleAESOFB send
private final MapleAESOFB receive
```

- 方法/构造器候选数: 4
```text
private ClientCyphers(MapleAESOFB send, MapleAESOFB receive)
public static ClientCyphers of(InitializationVector sendIv, InitializationVector receiveIv)
public MapleAESOFB getSendCypher()
public MapleAESOFB getReceiveCypher()
```

---

## `org.gms.net.encryption` / `net/encryption/InitializationVector.java`

### 类型声明
```text
class InitializationVector
```

- 字段候选数: 1
```text
private final byte[] bytes
```

- 方法/构造器候选数: 5
```text
private InitializationVector(byte[] bytes)
public byte[] getBytes()
public static InitializationVector generateSend()
public static InitializationVector generateReceive()
private static byte getRandomByte()
```

---

## `org.gms.net.encryption` / `net/encryption/MapleAESOFB.java`

### 类型声明
```text
class MapleAESOFB
```

- 字段候选数: 3
```text
private final short mapleVersion
private final Cipher cipher
private byte[] iv
```

- 方法/构造器候选数: 11
```text
public MapleAESOFB(InitializationVector iv, short mapleVersion)
private static byte[] multiplyBytes(byte[] in, int count, int mul)
public synchronized byte[] crypt(byte[] data)
private synchronized void updateIv()
public byte[] getPacketHeader(int length)
public static int getPacketLength(int packetHeader)
private boolean checkPacket(byte[] packet)
public boolean isValidHeader(int packetHeader)
public static byte[] getNewIv(byte[] oldIv)
public String toString()
private static byte[] funnyShit(byte inputByte, byte[] in)
```

---

## `org.gms.net.encryption` / `net/encryption/MapleCustomEncryption.java`

### 类型声明
```text
class MapleCustomEncryption
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
private static byte rollLeft(byte in, int count)
private static byte rollRight(byte in, int count)
public static byte[] encryptData(byte[] data)
public static byte[] decryptData(byte[] data)
```

---

## `org.gms.net.encryption` / `net/encryption/PacketCodec.java`

### 类型声明
```text
class PacketCodec
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public PacketCodec(ProtocolFactory protocolFactory)
```

---

## `org.gms.net.encryption` / `net/encryption/PacketDecoder.java`

### 类型声明
```text
class PacketDecoder
```

- 字段候选数: 1
```text
private final ProtocolFactory protocolFactory
```

- 方法/构造器候选数: 2
```text
public PacketDecoder(ProtocolFactory protocolFactory)
protected void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)
```

---

## `org.gms.net.encryption` / `net/encryption/PacketEncoder.java`

### 类型声明
```text
class PacketEncoder
```

- 字段候选数: 1
```text
private final ProtocolFactory protocolFactory
```

- 方法/构造器候选数: 2
```text
public PacketEncoder(ProtocolFactory protocolFactory)
protected void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)
```

---

## `org.gms.net.encryption.protocol` / `net/encryption/protocol/GMSV83PacketProtocol.java`

### 类型声明
```text
class GMSV83PacketProtocol
```

- 字段候选数: 2
```text
private final MapleAESOFB receiveCypher
private final MapleAESOFB sendCypher
```

- 方法/构造器候选数: 7
```text
public GMSV83PacketProtocol(ClientCyphers clientCyphers)
public void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)
private static int decodePacketLength(byte[] header)
private int decodePacketLength(int header)
public void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)
private byte[] getEncodedHeader(int length)
public void writeInitialUnencryptedHelloPacket(SocketChannel socketChannel, InitializationVector sendIv, InitializationVector recvIv, Client client)
```

---

## `org.gms.net.encryption.protocol` / `net/encryption/protocol/PacketProtocol.java`

### 类型声明
```text
interface PacketProtocol
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.encryption.protocol` / `net/encryption/protocol/ProtocolConstants.java`

### 类型声明
```text
class ProtocolConstants
```

- 字段候选数: 1
```text
public static final short GMS_V83 = 83
```

- 方法/构造器候选数: 0

---

## `org.gms.net.encryption.protocol` / `net/encryption/protocol/ProtocolFactory.java`

### 类型声明
```text
class ProtocolFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public ProtocolFactory(ClientCyphers clientCyphers)
public PacketProtocol getProtocol(short version)
```

---

## `org.gms.net.netty` / `net/netty/AbstractServer.java`

### 类型声明
```text
class AbstractServer
```

- 字段候选数: 1
```text
final int port
```

- 方法/构造器候选数: 1
```text
AbstractServer(int port)
```

---

## `org.gms.net.netty` / `net/netty/ChannelServer.java`

### 类型声明
```text
class ChannelServer
```

- 字段候选数: 3
```text
private final int world
private final int channel
private Channel nettyChannel
```

- 方法/构造器候选数: 3
```text
public ChannelServer(int port, int world, int channel)
public void start()
public void stop()
```

---

## `org.gms.net.netty` / `net/netty/ChannelServerInitializer.java`

### 类型声明
```text
class ChannelServerInitializer
```

- 字段候选数: 2
```text
private final int world
private final int channel
```

- 方法/构造器候选数: 2
```text
public ChannelServerInitializer(int world, int channel)
public void initChannel(SocketChannel socketChannel)
```

---

## `org.gms.net.netty` / `net/netty/InvalidPacketHeaderException.java`

### 类型声明
```text
class InvalidPacketHeaderException
```

- 字段候选数: 1
```text
private final int header
```

- 方法/构造器候选数: 2
```text
public InvalidPacketHeaderException(String message, int header)
public int getHeader()
```

---

## `org.gms.net.netty` / `net/netty/LoginServer.java`

### 类型声明
```text
class LoginServer
```

- 字段候选数: 3
```text
public static final int WORLD_ID = -1
public static final int CHANNEL_ID = -1
private Channel channel
```

- 方法/构造器候选数: 3
```text
public LoginServer(int port)
public void start()
public void stop()
```

---

## `org.gms.net.netty` / `net/netty/LoginServerInitializer.java`

### 类型声明
```text
class LoginServerInitializer
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void initChannel(SocketChannel socketChannel)
```

---

## `org.gms.net.netty` / `net/netty/ServerChannelInitializer.java`

### 类型声明
```text
class ServerChannelInitializer
```

- 字段候选数: 1
```text
private static final int IDLE_TIME_SECONDS = 30
```

- 方法/构造器候选数: 3
```text
String getRemoteAddress(Channel channel)
void initPipeline(SocketChannel socketChannel, Client client)
private void setUpHandlers(ChannelPipeline pipeline, ProtocolFactory protocolFactory, Client client)
```

---

## `org.gms.net.opcodes` / `net/opcodes/Opcode.java`

### 类型声明
```text
interface Opcode
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.opcodes` / `net/opcodes/RecvOpcode.java`

### 类型声明
```text
enum RecvOpcode
```

- 字段候选数: 1
```text
private int code = -2
```

- 方法/构造器候选数: 183
```text
CUSTOM_PACKET(0x3713),//13 37 lol // 自定义封包
LOGIN_PASSWORD(0x01), // 登录密码
GUEST_LOGIN(0x02), // 游客登录
SERVERLIST_REREQUEST(0x04), // 重新请求服务器列表
CHARLIST_REQUEST(0x05), // 请求角色列表
SERVERSTATUS_REQUEST(0x06), // 请求服务器状态
ACCEPT_TOS(0x07), // 接受服务条款
SET_GENDER(0x08), // 设置性别
AFTER_LOGIN(0x09), // 登录后操作
REGISTER_PIN(0x0A), // 注册PIN码
SERVERLIST_REQUEST(0x0B), // 请求服务器列表
PLAYER_DC(0x0C), // 玩家断开连接
VIEW_ALL_CHAR(0x0D), // 查看所有角色
PICK_ALL_CHAR(0x0E), // 选择所有角色
NAME_TRANSFER(0x10), // 名称转移
WORLD_TRANSFER(0x12), // 世界转移
CHAR_SELECT(0x13), // 角色选择
PLAYER_LOGGEDIN(0x14), // 玩家已登录
CHECK_CHAR_NAME(0x15), // 检查角色名称
CREATE_CHAR(0x16), // 创建角色
DELETE_CHAR(0x17), // 删除角色
PONG(0x18), // 心跳响应
CLIENT_START_ERROR(0x19), // 客户端启动错误
CLIENT_ERROR(0x1A), // 客户端错误
STRANGE_DATA(0x1B), // 奇怪的数据
RELOG(0x1C), // 重新登录
REGISTER_PIC(0x1D), // 注册图片
CHAR_SELECT_WITH_PIC(0x1E), // 带图片的角色选择
VIEW_ALL_PIC_REGISTER(0x1F), // 查看所有注册图片
VIEW_ALL_WITH_PIC(0x20), // 查看所有带图片
CHANGE_MAP(0x26), // 更改地图
CHANGE_CHANNEL(0x27), // 更改频道
ENTER_CASHSHOP(0x28), // 进入现金商店
MOVE_PLAYER(0x29), // 移动玩家
CANCEL_CHAIR(0x2A), // 取消椅子
USE_CHAIR(0x2B), // 使用椅子
CLOSE_RANGE_ATTACK(0x2C), // 近战攻击
RANGED_ATTACK(0x2D), // 远程攻击
MAGIC_ATTACK(0x2E), // 魔法攻击
TOUCH_MONSTER_ATTACK(0x2F), // 触碰怪物攻击
TAKE_DAMAGE(0x30), // 受到伤害
GENERAL_CHAT(0x31), // 通用聊天
CLOSE_CHALKBOARD(0x32), // 关闭黑板
FACE_EXPRESSION(0x33), // 表情符号
USE_ITEMEFFECT(0x34), // 使用物品效果
USE_DEATHITEM(0x35), // 使用死亡物品
MOB_BANISH_PLAYER(0x38), // 怪物驱逐玩家
MONSTER_BOOK_COVER(0x39), // 怪物图鉴封面
NPC_TALK(0x3A), // NPC对话
REMOTE_STORE(0x3B), // 远程商店
NPC_TALK_MORE(0x3C), // 继续NPC对话
NPC_SHOP(0x3D), // NPC商店
STORAGE(0x3E), // 仓库
HIRED_MERCHANT_REQUEST(0x3F), // 请求雇佣商人
FREDRICK_ACTION(0x40), // Fredrick操作
DUEY_ACTION(0x41), // Duey操作
OWL_ACTION(0x42),   // 发送最常用的信息给客户端     sends most searched info to client
OWL_WARP(0x43),     // 处理玩家传送到商店        handles player warp to store
ADMIN_SHOP(0x44), // 管理员商店
ITEM_SORT(0x45), // 整理物品
ITEM_SORT2(0x46), // 整理物品2
ITEM_MOVE(0x47), // 移动物品
USE_ITEM(0x48), // 使用物品
CANCEL_ITEM_EFFECT(0x49), // 取消物品效果
USE_SUMMON_BAG(0x4B), // 使用召唤袋
PET_FOOD(0x4C), // 宠物食物
USE_MOUNT_FOOD(0x4D), // 使用坐骑食物
SCRIPTED_ITEM(0x4E), // 脚本物品
USE_CASH_ITEM(0x4F), // 使用现金物品
USE_CATCH_ITEM(0x51), // 使用捕捉物品
USE_SKILL_BOOK(0x52), // 使用技能书
USE_TELEPORT_ROCK(0x54), // 使用传送石
USE_RETURN_SCROLL(0x55), // 使用返回卷轴
USE_UPGRADE_SCROLL(0x56), // 使用升级卷轴
DISTRIBUTE_AP(0x57), // 分配能力点
AUTO_DISTRIBUTE_AP(0x58), // 自动分配能力点
HEAL_OVER_TIME(0x59), // 持续治疗
DISTRIBUTE_SP(0x5A), // 分配技能点
SPECIAL_MOVE(0x5B), // 特殊移动
CANCEL_BUFF(0x5C), // 取消增益效果
SKILL_EFFECT(0x5D), // 技能效果
MESO_DROP(0x5E), // 金币掉落
GIVE_FAME(0x5F), // 赠送声望
CHAR_INFO_REQUEST(0x61), // 请求角色信息
SPAWN_PET(0x62), // 生成宠物
CANCEL_DEBUFF(0x63), // 取消减益效果
CHANGE_MAP_SPECIAL(0x64), // 特殊更改地图
USE_INNER_PORTAL(0x65), // 使用内部传送门
TROCK_ADD_MAP(0x66), // 添加传送岩地图
REPORT(0x6A), // 报告
QUEST_ACTION(0x6B), // 任务操作
GRENADE_EFFECT(0x6D), // 手榴弹效果
SKILL_MACRO(0x6E), // 技能宏
USE_ITEM_REWARD(0x70), // 使用物品奖励
MAKER_SKILL(0x71), // 制作器技能
USE_TREASUER_CHEST(0x73), // 使用宝箱
USE_REMOTE(0x74), // 使用遥控器
WATER_OF_LIFE(0x75), // 生命之水
ADMIN_CHAT(0x76), // 管理员聊天
MULTI_CHAT(0x77), // 多人聊天
WHISPER(0x78), // 密语
SPOUSE_CHAT(0x79), // 配偶聊天
MESSENGER(0x7A), // 消息传递
PLAYER_INTERACTION(0x7B), // 玩家互动
PARTY_OPERATION(0x7C), // 组队操作
DENY_PARTY_REQUEST(0x7D), // 拒绝组队请求
GUILD_OPERATION(0x7E), // 公会操作
DENY_GUILD_REQUEST(0x7F), // 拒绝公会请求
ADMIN_COMMAND(0x80), // 管理员命令
ADMIN_LOG(0x81), // 管理员日志
BUDDYLIST_MODIFY(0x82), // 修改好友列表
NOTE_ACTION(0x83), // 笔记操作
USE_DOOR(0x85), // 使用门
CHANGE_KEYMAP(0x87), // 更改键盘映射
RPS_ACTION(0x88), // 石头剪刀布操作
RING_ACTION(0x89), // 戒指操作
WEDDING_ACTION(0x8A), // 结婚操作
WEDDING_TALK(0x8B), // 结婚对话
WEDDING_TALK_MORE(0x8B), // 继续结婚对话
ALLIANCE_OPERATION(0x8F), // 联盟操作
DENY_ALLIANCE_REQUEST(0x90), // 拒绝联盟请求
OPEN_FAMILY_PEDIGREE(0x91), // 打开家族谱系
OPEN_FAMILY(0x92), // 打开家族
ADD_FAMILY(0x93), // 添加家族
SEPARATE_FAMILY_BY_SENIOR(0x94), // 通过长辈分离家族
SEPARATE_FAMILY_BY_JUNIOR(0x95), // 通过晚辈分离家族
ACCEPT_FAMILY(0x96), // 接受家族邀请
USE_FAMILY(0x97), // 使用家族功能
CHANGE_FAMILY_MESSAGE(0x98), // 更改家族消息
FAMILY_SUMMON_RESPONSE(0x99), // 家族召唤响应
BBS_OPERATION(0x9B), // 论坛操作
ENTER_MTS(0x9C), // 进入MTS
USE_SOLOMON_ITEM(0x9D), // 使用所罗门物品
USE_GACHA_EXP(0x9E), // 使用扭蛋经验
NEW_YEAR_CARD_REQUEST(0x9F), // 新年贺卡请求
CASHSHOP_SURPRISE(0xA1), // 现金商店惊喜
CLICK_GUIDE(0xA2), // 点击引导
ARAN_COMBO_COUNTER(0xA3), // Aran连击计数器
MOVE_PET(0xA7), // 移动宠物
PET_CHAT(0xA8), // 宠物对话
PET_COMMAND(0xA9), // 宠物命令
PET_LOOT(0xAA), // 宠物拾取
PET_AUTO_POT(0xAB), // 宠物自动使用药水
PET_EXCLUDE_ITEMS(0xAC), // 宠物排除物品
MOVE_SUMMON(0xAF), // 移动召唤兽
SUMMON_ATTACK(0xB0), // 召唤兽攻击
DAMAGE_SUMMON(0xB1), // 召唤兽受到伤害
BEHOLDER(0xB2), // Beholder（不明用途）
MOVE_DRAGON(0xB5), // 移动龙
CHANGE_QUICKSLOT(0xB7),//CP_QuickslotKeyMappedModified // 更改快捷栏
MOVE_LIFE(0xBC), // 移动生命体
AUTO_AGGRO(0xBD), // 自动仇恨
FIELD_DAMAGE_MOB(0xBF), // 场景中怪物受到伤害
MOB_DAMAGE_MOB_FRIENDLY(0xC0), // 怪物对友好怪物造成伤害
MONSTER_BOMB(0xC1), // 怪物炸弹
MOB_DAMAGE_MOB(0xC2), // 怪物对怪物造成伤害
NPC_ACTION(0xC5), // NPC动作
ITEM_PICKUP(0xCA), // 捡起物品
DAMAGE_REACTOR(0xCD), // 反应堆受到伤害
TOUCHING_REACTOR(0xCE), // 触碰反应堆
PLAYER_MAP_TRANSFER(0xCF), // 玩家地图转换
MAPLETV(0xFFFE),//Don't know // MapleTV（不知道）
SNOWBALL(0xD3), // 雪球
LEFT_KNOCKBACK(0xD4), // 左侧击退
COCONUT(0xD5), // 椰子
MATCH_TABLE(0xD6),//Would be cool if I ever get it to work :) // 匹配表（如果我能让它工作就好了 :））
MONSTER_CARNIVAL(0xDA), // 怪物嘉年华
PARTY_SEARCH_REGISTER(0xDC), // 注册组队搜索
PARTY_SEARCH_START(0xDE), // 开始组队搜索
PARTY_SEARCH_UPDATE(0xDF), // 更新组队搜索
CHECK_CASH(0xE4), // 检查现金
CASHSHOP_OPERATION(0xE5), // 现金商店操作
COUPON_CODE(0xE6), // 优惠券代码
OPEN_ITEMUI(0xEC), // 打开物品界面
CLOSE_ITEMUI(0xED), // 关闭物品界面
USE_ITEMUI(0xEE), // 使用物品界面
MTS_OPERATION(0xFD), // MTS操作
USE_MAPLELIFE(0x100), // 使用MapleLife
USE_HAMMER(0x104), // 使用锤子
SET_HPMPALERT(0x1000), // 设置HP/MP警报
RecvOpcode(int code)
public int getValue()
public String getName()
```

---

## `org.gms.net.opcodes` / `net/opcodes/SendOpcode.java`

### 类型声明
```text
enum SendOpcode
```

- 字段候选数: 1
```text
private int code = -2
```

- 方法/构造器候选数: 312
```text
LOGIN_STATUS(0x00), // 登录状态
GUEST_ID_LOGIN(0x01), // 游客ID登录
ACCOUNT_INFO(0x02), // 账户信息
SERVERSTATUS(0x03), // 服务器状态（CHECK_USER_LIMIT_RESULT）
GENDER_DONE(0x04), // 性别设置结果（SET_ACCOUNT_RESULT）
CONFIRM_EULA_RESULT(0x05), // EULA确认结果
CHECK_PINCODE(0x06), // 检查PIN码
UPDATE_PINCODE(0x07), // 更新PIN码
VIEW_ALL_CHAR(0x08), // 查看所有角色
SELECT_CHARACTER_BY_VAC(0x09), // 通过VAC选择角色
SERVERLIST(0x0A), // 服务器列表
CHARLIST(0x0B), // 角色列表
SERVER_IP(0x0C), // 服务器IP
CHAR_NAME_RESPONSE(0x0D), // 角色名称响应
ADD_NEW_CHAR_ENTRY(0x0E), // 添加新角色条目
DELETE_CHAR_RESPONSE(0x0F), // 删除角色响应
CHANGE_CHANNEL(0x10), // 更改频道
PING(0x11), // 心跳检测
KOREAN_INTERNET_CAFE_SHIT(0x12), // 韩国互联网咖啡无关紧要的内容，忽略
CHANNEL_SELECTED(0x14), // 频道已选择
HACKSHIELD_REQUEST(0x15), // 可能是RELOG_RESPONSE，无所谓
RELOG_RESPONSE(0x16), // 重新登录响应
CHECK_CRC_RESULT(0x19), // CRC检查结果
LAST_CONNECTED_WORLD(0x1A), // 上次连接的世界
RECOMMENDED_WORLD_MESSAGE(0x1B), // 推荐世界消息
CHECK_SPW_RESULT(0x1C), // SPW检查结果
INVENTORY_OPERATION(0x1D), // 物品栏操作
INVENTORY_GROW(0x1E), // 扩展物品栏
STAT_CHANGED(0x1F), // 状态改变
GIVE_BUFF(0x20), // 施加增益效果
CANCEL_BUFF(0x21), // 移除增益效果
FORCED_STAT_SET(0x22), // 强制设置状态
FORCED_STAT_RESET(0x23), // 强制重置状态
UPDATE_SKILLS(0x24), // 更新技能
SKILL_USE_RESULT(0x25), // 技能使用结果
FAME_RESPONSE(0x26), // 声望响应
SHOW_STATUS_INFO(0x27), // 显示状态信息
OPEN_FULL_CLIENT_DOWNLOAD_LINK(0x28), // 打开完整客户端下载链接
MEMO_RESULT(0x29), // 备忘录结果
MAP_TRANSFER_RESULT(0x2A), // 地图转移结果
WEDDING_PHOTO(0x2B), // 结婚照片（ANTI_MACRO_RESULT在某些版本可能是这个）
CLAIM_RESULT(0x2D), // 领取结果
CLAIM_AVAILABLE_TIME(0x2E), // 领取可用时间
CLAIM_STATUS_CHANGED(0x2F), // 领取状态改变
SET_TAMING_MOB_INFO(0x30), // 设置驯服怪物信息
QUEST_CLEAR(0x31), // 任务完成
ENTRUSTED_SHOP_CHECK_RESULT(0x32), // 委托商店检查结果
SKILL_LEARN_ITEM_RESULT(0x33), // 学习技能物品结果
GATHER_ITEM_RESULT(0x34), // 收集物品结果
SORT_ITEM_RESULT(0x35), // 整理物品结果
SUE_CHARACTER_RESULT(0x37), // 控诉角色结果
TRADE_MONEY_LIMIT(0x39), // 交易金钱限制
SET_GENDER(0x3A), // 设置性别
GUILD_BBS_PACKET(0x3B), // 公会公告板数据包
CHAR_INFO(0x3D), // 角色信息
PARTY_OPERATION(0x3E), // 组队操作
BUDDYLIST(0x3F), // 好友列表
GUILD_OPERATION(0x41), // 公会操作
ALLIANCE_OPERATION(0x42), // 联盟操作
SPAWN_PORTAL(0x43), // 生成传送门
SERVERMESSAGE(0x44), // 服务器消息
INCUBATOR_RESULT(0x45), // 孵化器结果
SHOP_SCANNER_RESULT(0x46), // 商店扫描结果
SHOP_LINK_RESULT(0x47), // 商店链接结果
MARRIAGE_REQUEST(0x48), // 结婚请求
MARRIAGE_RESULT(0x49), // 结婚结果
WEDDING_GIFT_RESULT(0x4A), // 结婚礼物结果
NOTIFY_MARRIED_PARTNER_MAP_TRANSFER(0x4B), // 通知结婚伴侣地图转移
CASH_PET_FOOD_RESULT(0x4C), // 宠物食物结果
SET_WEEK_EVENT_MESSAGE(0x4D), // 设置周活动消息
SET_POTION_DISCOUNT_RATE(0x4E), // 设置药水折扣率
BRIDLE_MOB_CATCH_FAIL(0x4F), // 鞍具捕捉怪物失败
IMITATED_NPC_RESULT(0x50), // 仿冒NPC结果
IMITATED_NPC_DATA(0x51), // 仿冒NPC数据
LIMITED_NPC_DISABLE_INFO(0x52), // 限时NPC禁用信息
MONSTER_BOOK_SET_CARD(0x53), // 怪物图鉴设置卡片
MONSTER_BOOK_SET_COVER(0x54), // 怪物图鉴设置封面
HOUR_CHANGED(0x55), // 时间变化
MINIMAP_ON_OFF(0x56), // 小地图开关
CONSULT_AUTHKEY_UPDATE(0x57), // 咨询认证密钥更新
CLASS_COMPETITION_AUTHKEY_UPDATE(0x58), // 竞技场认证密钥更新
WEB_BOARD_AUTHKEY_UPDATE(0x59), // 网络论坛认证密钥更新
SESSION_VALUE(0x5A), // 会话值
PARTY_VALUE(0x5B), // 组队值
FIELD_SET_VARIABLE(0x5C), // 字段设置变量
BONUS_EXP_CHANGED(0x5D), // 奖励经验值变化（猜测，不确定v83中的opcode）
FAMILY_CHART_RESULT(0x5E), // 家族图表结果
FAMILY_INFO_RESULT(0x5F), // 家族信息结果
FAMILY_RESULT(0x60), // 家族结果
FAMILY_JOIN_REQUEST(0x61), // 家族加入请求
FAMILY_JOIN_REQUEST_RESULT(0x62), // 家族加入请求结果
FAMILY_JOIN_ACCEPTED(0x63), // 家族加入接受
FAMILY_PRIVILEGE_LIST(0x64), // 家族权限列表
FAMILY_REP_GAIN(0x65), // 家族声望获得
FAMILY_NOTIFY_LOGIN_OR_LOGOUT(0x66), // 通知家族成员登录或登出
FAMILY_SET_PRIVILEGE(0x67), // 设置家族权限
FAMILY_SUMMON_REQUEST(0x68), // 家族召唤请求
NOTIFY_LEVELUP(0x69), // 通知等级提升
NOTIFY_MARRIAGE(0x6A), // 通知结婚
NOTIFY_JOB_CHANGE(0x6B), // 通知职业变更
MAPLE_TV_USE_RES(0x6D), // Maple TV使用结果（不是空白，是一个弹窗）
AVATAR_MEGAPHONE_RESULT(0x6E), // 头像喇叭结果（机器人无用）
SET_AVATAR_MEGAPHONE(0x6F), // 设置头像喇叭
CLEAR_AVATAR_MEGAPHONE(0x70), // 清除头像喇叭
CANCEL_NAME_CHANGE_RESULT(0x71), // 取消更改名字结果
CANCEL_TRANSFER_WORLD_RESULT(0x72), // 取消转移世界结果
DESTROY_SHOP_RESULT(0x73), // 销毁商店结果
FAKE_GM_NOTICE(0x74), // 假GM通知（坏家伙）
SUCCESS_IN_USE_GACHAPON_BOX(0x75), // 成功使用扭蛋机箱
NEW_YEAR_CARD_RES(0x76), // 新年贺卡结果
RANDOM_MORPH_RES(0x77), // 随机变身结果
CANCEL_NAME_CHANGE_BY_OTHER(0x78), // 由他人取消更改名字
SET_EXTRA_PENDANT_SLOT(0x79), // 设置额外饰品插槽
SCRIPT_PROGRESS_MESSAGE(0x7A), // 脚本进度消息
DATA_CRC_CHECK_FAILED(0x7B), // 数据CRC检查失败
MACRO_SYS_DATA_INIT(0x7C), // 宏系统数据初始化
SET_FIELD(0x7D), // 设置字段
SET_ITC(0x7E), // 设置ITC
SET_CASH_SHOP(0x7F), // 设置现金商店
SET_BACK_EFFECT(0x80), // 设置背景特效
SET_MAP_OBJECT_VISIBLE(0x81), // 设置地图对象可见性
CLEAR_BACK_EFFECT(0x82), // 清除背景特效
BLOCKED_MAP(0x83), // 被阻止的地图
BLOCKED_SERVER(0x84), // 被阻止的服务器
FORCED_MAP_EQUIP(0x85), // 强制地图装备
MULTICHAT(0x86), // 多人聊天
WHISPER(0x87), // 密语
SPOUSE_CHAT(0x88), // 配偶聊天
SUMMON_ITEM_INAVAILABLE(0x89), // 在此地图无法使用召唤物品
FIELD_EFFECT(0x8A), // 场景效果
FIELD_OBSTACLE_ONOFF(0x8B), // 场景障碍物开关
FIELD_OBSTACLE_ONOFF_LIST(0x8C), // 场景障碍物开关列表
FIELD_OBSTACLE_ALL_RESET(0x8D), // 重置所有场景障碍物
BLOW_WEATHER(0x8E), // 吹风天气效果
PLAY_JUKEBOX(0x8F), // 播放点唱机
ADMIN_RESULT(0x90), // 管理员结果
OX_QUIZ(0x91), // QUIZ（OX问答）
GMEVENT_INSTRUCTIONS(0x92), // DESC（游戏事件说明）
CLOCK(0x93), // 时钟
CONTI_MOVE(0x94), // 连续移动
CONTI_STATE(0x95), // 连续状态
SET_QUEST_CLEAR(0x96), // 设置任务完成
SET_QUEST_TIME(0x97), // 设置任务时间
ARIANT_RESULT(0x98),    // thanks lrenex // ARIANT结果
SET_OBJECT_STATE(0x99), // 设置物体状态
STOP_CLOCK(0x9A), // 停止时钟
ARIANT_ARENA_SHOW_RESULT(0x9B), // ARIANT竞技场显示结果
PYRAMID_GAUGE(0x9D), // 金字塔计数器
PYRAMID_SCORE(0x9E), // 金字塔分数
QUICKSLOT_INIT(0x9F),//LP_QuickslotMappedInit // 快捷栏初始化
SPAWN_PLAYER(0xA0), // 生成玩家
REMOVE_PLAYER_FROM_MAP(0xA1), // 从地图移除玩家
CHATTEXT(0xA2), // 聊天文本（类型0）
CHATTEXT1(0xA3), // 聊天文本（类型1）
CHALKBOARD(0xA4), // 黑板
UPDATE_CHAR_BOX(0xA5), // 更新角色盒子
SHOW_CONSUME_EFFECT(0xA6), // 显示消耗效果
SHOW_SCROLL_EFFECT(0xA7), // 显示卷轴效果
SPAWN_PET(0xA8), // 生成宠物
MOVE_PET(0xAA), // 移动宠物
PET_CHAT(0xAB), // 宠物对话
PET_NAMECHANGE(0xAC), // 更改宠物名字
PET_EXCEPTION_LIST(0xAD), // 宠物异常列表
PET_COMMAND(0xAE), // 宠物命令
SPAWN_SPECIAL_MAPOBJECT(0xAF), // 生成特殊地图对象
REMOVE_SPECIAL_MAPOBJECT(0xB0), // 移除特殊地图对象
MOVE_SUMMON(0xB1), // 移动召唤兽
SUMMON_ATTACK(0xB2), // 召唤兽攻击
DAMAGE_SUMMON(0xB3), // 召唤兽受到伤害
SUMMON_SKILL(0xB4), // 召唤兽技能
SPAWN_DRAGON(0xB5), // 生成龙
MOVE_DRAGON(0xB6), // 移动龙
REMOVE_DRAGON(0xB7), // 移除龙
MOVE_PLAYER(0xB9), // 移动玩家
CLOSE_RANGE_ATTACK(0xBA), // 近战攻击
RANGED_ATTACK(0xBB), // 远程攻击
MAGIC_ATTACK(0xBC), // 魔法攻击
ENERGY_ATTACK(0xBD), // 能量攻击
SKILL_EFFECT(0xBE), // 技能效果
CANCEL_SKILL_EFFECT(0xBF), // 取消技能效果
DAMAGE_PLAYER(0xC0), // 玩家受到伤害
FACIAL_EXPRESSION(0xC1), // 表情符号
SHOW_ITEM_EFFECT(0xC2), // 显示物品效果
SHOW_CHAIR(0xC4), // 显示椅子
UPDATE_CHAR_LOOK(0xC5), // 更新角色外观
SHOW_FOREIGN_EFFECT(0xC6), // 显示远程效果
GIVE_FOREIGN_BUFF(0xC7), // 给予远程增益效果
CANCEL_FOREIGN_BUFF(0xC8), // 取消远程增益效果
UPDATE_PARTYMEMBER_HP(0xC9), // 更新组队成员HP
GUILD_NAME_CHANGED(0xCA), // 公会名称改变
GUILD_MARK_CHANGED(0xCB), // 公会标志改变
THROW_GRENADE(0xCC), // 抛掷手榴弹
CANCEL_CHAIR(0xCD), // 取消椅子
SHOW_ITEM_GAIN_INCHAT(0xCE), // 在聊天中显示获得物品
DOJO_WARP_UP(0xCF), // 武道馆传送准备
LUCKSACK_PASS(0xD0), // 幸运袋成功
LUCKSACK_FAIL(0xD1), // 幸运袋失败
MESO_BAG_MESSAGE(0xD2), // 金币背包消息
UPDATE_QUEST_INFO(0xD3), // 更新任务信息
ON_NOTIFY_HP_DEC_BY_FIELD(0xD4), // 通知字段减少HP
PLAYER_HINT(0xD6), // 玩家提示
MAKER_RESULT(0xD9), // 制作器结果
KOREAN_EVENT(0xDB), // 韩国活动
OPEN_UI(0xDC), // 打开UI
LOCK_UI(0xDD), // 锁定UI
DISABLE_UI(0xDE), // 禁用UI
SPAWN_GUIDE(0xDF), // 生成引导者
TALK_GUIDE(0xE0), // 引导者对话
SHOW_COMBO(0xE1), // 显示连击
COOLDOWN(0xEA), // 冷却时间
SPAWN_MONSTER(0xEC), // 生成怪物
KILL_MONSTER(0xED), // 击杀怪物
SPAWN_MONSTER_CONTROL(0xEE), // 控制生成怪物
MOVE_MONSTER(0xEF), // 移动怪物
MOVE_MONSTER_RESPONSE(0xF0), // 移动怪物响应
APPLY_MONSTER_STATUS(0xF2), // 应用怪物状态
CANCEL_MONSTER_STATUS(0xF3), // 取消怪物状态
RESET_MONSTER_ANIMATION(0xF4),//LOL? o.o // 重置怪物动画
DAMAGE_MONSTER(0xF6), // 怪物受到伤害
ARIANT_THING(0xF9), // ARIANT相关操作
SHOW_MONSTER_HP(0xFA), // 显示怪物HP
CATCH_MONSTER(0xFB), // 捕捉怪物
CATCH_MONSTER_WITH_ITEM(0xFC), // 使用物品捕捉怪物
SHOW_MAGNET(0xFD), // 显示磁铁效果
SPAWN_NPC(0x101), // 生成NPC
REMOVE_NPC(0x102), // 移除NPC
SPAWN_NPC_REQUEST_CONTROLLER(0x103), // 请求控制NPC生成
NPC_ACTION(0x104), // NPC动作
SET_NPC_SCRIPTABLE(0x107), // 设置NPC可脚本化
SPAWN_HIRED_MERCHANT(0x109), // 生成雇佣商人
DESTROY_HIRED_MERCHANT(0x10A), // 销毁雇佣商人
UPDATE_HIRED_MERCHANT(0x10B), // 更新雇佣商人
DROP_ITEM_FROM_MAPOBJECT(0x10C), // 从地图对象掉落物品
REMOVE_ITEM_FROM_MAP(0x10D), // 从地图移除物品
CANNOT_SPAWN_KITE(0x10E), // 无法生成风筝
SPAWN_KITE(0x10F), // 生成风筝
REMOVE_KITE(0x110), // 移除风筝
SPAWN_MIST(0x111), // 生成迷雾
REMOVE_MIST(0x112), // 移除迷雾
SPAWN_DOOR(0x113), // 生成门
REMOVE_DOOR(0x114), // 移除门
REACTOR_HIT(0x115), // 反应堆被击中
REACTOR_SPAWN(0x117), // 生成反应堆
REACTOR_DESTROY(0x118), // 销毁反应堆
SNOWBALL_STATE(0x119), // 雪球状态
HIT_SNOWBALL(0x11A), // 击中雪球
SNOWBALL_MESSAGE(0x11B), // 雪球消息
LEFT_KNOCK_BACK(0x11C), // 左侧击退
COCONUT_HIT(0x11D), // 击中椰子
COCONUT_SCORE(0x11E), // 椰子得分
GUILD_BOSS_HEALER_MOVE(0x11F), // 公会长老移动
GUILD_BOSS_PULLEY_STATE_CHANGE(0x120), // 公会长老滑轮状态改变
MONSTER_CARNIVAL_START(0x121), // 怪物嘉年华开始
MONSTER_CARNIVAL_OBTAINED_CP(0x122), // 获得怪物嘉年华CP
MONSTER_CARNIVAL_PARTY_CP(0x123), // 怪物嘉年华队伍CP
MONSTER_CARNIVAL_SUMMON(0x124), // 怪物嘉年华召唤
MONSTER_CARNIVAL_MESSAGE(0x125), // 怪物嘉年华消息
MONSTER_CARNIVAL_DIED(0x126), // 怪物嘉年华死亡
MONSTER_CARNIVAL_LEAVE(0x127), // 离开怪物嘉年华
ARIANT_ARENA_USER_SCORE(0x129), // ARIANT竞技场用户得分
SHEEP_RANCH_INFO(0x12B), // 羊牧场信息
SHEEP_RANCH_CLOTHES(0x12C), // 羊牧场服装
WITCH_TOWER_SCORE_UPDATE(0x12D),    // thanks lrenex // 巫师塔得分更新
HORNTAIL_CAVE(0x12E), // 角龙头洞
ZAKUM_SHRINE(0x12F), // 泽库姆神殿
NPC_TALK(0x130), // NPC对话
OPEN_NPC_SHOP(0x131), // 打开NPC商店
CONFIRM_SHOP_TRANSACTION(0x132), // 确认商店交易
ADMIN_SHOP_MESSAGE(0x133),//lame :P // 管理员商店消息
ADMIN_SHOP(0x134), // 管理员商店
STORAGE(0x135), // 仓库
FREDRICK_MESSAGE(0x136), // Fredrick消息
FREDRICK(0x137), // Fredrick操作
RPS_GAME(0x138), // 石头剪刀布游戏
MESSENGER(0x139), // 消息传递
PLAYER_INTERACTION(0x13A), // 玩家互动
TOURNAMENT(0x13B), // 锦标赛
TOURNAMENT_MATCH_TABLE(0x13C), // 锦标赛匹配表
TOURNAMENT_SET_PRIZE(0x13D), // 设置锦标赛奖品
TOURNAMENT_UEW(0x13E), // 锦标赛未知功能
TOURNAMENT_CHARACTERS(0x13F),//they never coded this :| // 锦标赛角色（他们从未实现这个功能）
WEDDING_PROGRESS(0x140),//byte step, int groomid, int brideid // 结婚进度
WEDDING_CEREMONY_END(0x141), // 结婚仪式结束
PARCEL(0x142), // 礼包
CHARGE_PARAM_RESULT(0x143), // 充值参数结果
QUERY_CASH_RESULT(0x144), // 查询现金结果
CASHSHOP_OPERATION(0x145), // 现金商店操作
CASHSHOP_PURCHASE_EXP_CHANGED(0x146),   // found thanks to Arnah (Vertisy) // 现金商店购买经验变化
CASHSHOP_GIFT_INFO_RESULT(0x147), // 现金商店礼物信息结果
CASHSHOP_CHECK_NAME_CHANGE(0x148), // 检查现金商店姓名更改
CASHSHOP_CHECK_NAME_CHANGE_POSSIBLE_RESULT(0x149), // 检查现金商店姓名更改可能性结果
CASHSHOP_REGISTER_NEW_CHARACTER_RESULT(0x14A), // 注册新角色结果
CASHSHOP_CHECK_TRANSFER_WORLD_POSSIBLE_RESULT(0x14B), // 检查转移世界可能性结果
CASHSHOP_GACHAPON_STAMP_RESULT(0x14C), // 现金商店扭蛋印章结果
CASHSHOP_CASH_ITEM_GACHAPON_RESULT(0x14D), // 现金商店现金物品扭蛋结果
CASHSHOP_CASH_GACHAPON_OPEN_RESULT(0x14E), // 现金商店现金扭蛋打开结果
KEYMAP(0x14F), // 键盘映射
AUTO_HP_POT(0x150), // 自动使用HP药水
AUTO_MP_POT(0x151), // 自动使用MP药水
SEND_TV(0x155), // 发送电视
REMOVE_TV(0x156), // 移除电视
ENABLE_TV(0x157), // 启用电视
MTS_OPERATION2(0x15B), // MTS操作2
MTS_OPERATION(0x15C), // MTS操作
MAPLELIFE_RESULT(0x15D), // MapleLife结果
MAPLELIFE_ERROR(0x15E), // MapleLife错误
VICIOUS_HAMMER(0x162), // 恶毒锤子
VEGA_SCROLL(0x166), // VEGA卷轴
UPDATE_HPMPAALERT(0x1000), // 更新HP/MP/EXP警报
SendOpcode(int code)
public int getValue()
public String getName()
```

---

## `org.gms.net.packet` / `net/packet/ByteBufInPacket.java`

### 类型声明
```text
class ByteBufInPacket
```

- 字段候选数: 1
```text
private final ByteBuf byteBuf
```

- 方法/构造器候选数: 17
```text
public ByteBufInPacket(ByteBuf byteBuf)
public byte[] getBytes()
public byte readByte()
public short readUnsignedByte()
public short readShort()
public int readInt()
public long readLong()
public Point readPos()
public String readString()
public byte[] readBytes(int numberOfBytes)
public void skip(int numberOfBytes)
public int available()
public void seek(int byteOffset)
public int getPosition()
public boolean equals(Object o)
public String toString()
private static String insertReaderPosition(String hexDump, int index)
```

---

## `org.gms.net.packet` / `net/packet/ByteBufOutPacket.java`

### 类型声明
```text
class ByteBufOutPacket
```

- 字段候选数: 1
```text
private final ByteBuf byteBuf
```

- 方法/构造器候选数: 17
```text
public ByteBufOutPacket()
public ByteBufOutPacket(Opcode op)
public ByteBufOutPacket(SendOpcode op, int initialCapacity)
public byte[] getBytes()
public void writeByte(byte value)
public void writeByte(int value)
public void writeBytes(byte[] value)
public void writeShort(int value)
public void writeInt(int value)
public void writeLong(long value)
public void writeBool(boolean value)
public void writeString(String value)
public void writeFixedString(String value)
public void writeFixedString(String value, int fixed)
public void writePos(Point value)
public void skip(int numberOfBytes)
public boolean equals(Object o)
```

---

## `org.gms.net.packet` / `net/packet/InPacket.java`

### 类型声明
```text
interface InPacket
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.packet` / `net/packet/OutPacket.java`

### 类型声明
```text
interface OutPacket
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
static OutPacket create(Opcode opcode)
```

---

## `org.gms.net.packet` / `net/packet/Packet.java`

### 类型声明
```text
interface Packet
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.packet.logging` / `net/packet/logging/InPacketLogger.java`

### 类型声明
```text
class InPacketLogger
```

- 字段候选数: 1
```text
private static final int LOG_CONTENT_THRESHOLD = 3_000
```

- 方法/构造器候选数: 3
```text
public void channelRead(ChannelHandlerContext ctx, Object msg)
public void log(Packet packet)
private String getRecvOpcodeName(short opcode)
```

---

## `org.gms.net.packet.logging` / `net/packet/logging/LoggingUtil.java`

### 类型声明
```text
class LoggingUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static short readFirstShort(byte[] bytes)
public static boolean isIgnoredRecvPacket(short opcode)
```

---

## `org.gms.net.packet.logging` / `net/packet/logging/MonitoredChrLogger.java`

### 类型声明
```text
class MonitoredChrLogger
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static boolean toggleMonitored(int chrId)
public static Collection<Integer> getMonitoredChrIds()
public static void logPacketIfMonitored(Client c, short packetId, byte[] packetContent)
private static boolean isRecvBlocked(RecvOpcode op)
private static RecvOpcode getOpcodeFromValue(int value)
```

---

## `org.gms.net.packet.logging` / `net/packet/logging/OutPacketLogger.java`

### 类型声明
```text
class OutPacketLogger
```

- 字段候选数: 1
```text
private static final int LOG_CONTENT_THRESHOLD = 50_000
```

- 方法/构造器候选数: 3
```text
public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise)
public void log(Packet packet)
private String getSendOpcodeName(short opcode)
```

---

## `org.gms.net.packet.logging` / `net/packet/logging/PacketLogger.java`

### 类型声明
```text
interface PacketLogger
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.packet.out` / `net/packet/out/SendNoteSuccessPacket.java`

### 类型声明
```text
class SendNoteSuccessPacket
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public SendNoteSuccessPacket()
```

---

## `org.gms.net.packet.out` / `net/packet/out/ShowNotesPacket.java`

### 类型声明
```text
class ShowNotesPacket
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public ShowNotesPacket(List<NotesDO> notes)
private void writeNote(NotesDO note)
```

---

## `org.gms.net.server` / `net/server/PlayerBuffStorage.java`

### 类型声明
```text
class PlayerBuffStorage
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public void addBuffsToStorage(int chrid, List<PlayerBuffValueHolder> toStore)
public List<PlayerBuffValueHolder> getBuffsFromStorage(int chrid)
public void addDiseasesToStorage(int chrid, Map<Disease, Pair<Long, MobSkill>> toStore)
public int hashCode()
public boolean equals(Object obj)
```

---

## `org.gms.net.server` / `net/server/PlayerBuffValueHolder.java`

### 类型声明
```text
class PlayerBuffValueHolder
```

- 字段候选数: 2
```text
public int usedTime
public StatEffect effect
```

- 方法/构造器候选数: 1
```text
public PlayerBuffValueHolder(int usedTime, StatEffect effect)
```

---

## `org.gms.net.server` / `net/server/PlayerCoolDownValueHolder.java`

### 类型声明
```text
class PlayerCoolDownValueHolder
```

- 字段候选数: 3
```text
public int skillId
public long startTime
public long length
```

- 方法/构造器候选数: 1
```text
public PlayerCoolDownValueHolder(int skillId, long startTime, long length)
```

---

## `org.gms.net.server` / `net/server/PlayerDiseaseValueHolder.java`

### 类型声明
```text
class PlayerDiseaseValueHolder
```

- 字段候选数: 3
```text
public long startTime
public long length
public Disease disease
```

- 方法/构造器候选数: 1
```text
public PlayerDiseaseValueHolder(final Disease disease, final long startTime, final long length)
```

---

## `org.gms.net.server` / `net/server/PlayerStorage.java`

### 类型声明
```text
class PlayerStorage
```

- 字段候选数: 2
```text
private final Lock rlock
private final Lock wlock
```

- 方法/构造器候选数: 8
```text
public PlayerStorage()
public void addPlayer(Character chr)
public Character removePlayer(int chr)
public Character getCharacterByName(String name)
public Character getCharacterById(int id)
public Collection<Character> getAllCharacters()
public final void disconnectAll()
public int getSize()
```

---

## `org.gms.net.server` / `net/server/Server.java`

### 类型声明
```text
class Server
```

- 字段候选数: 11
```text
private static Server instance = null
private ChannelDependencies channelDependencies
private LoginServer loginServer
private final Lock wldRLock
private final Lock wldWLock
private final Lock lgnRLock
private final Lock lgnWLock
private long serverCurrentTime = 0
private volatile boolean availableDeveloperRoom = false
private boolean online = false
private long nextTime
```

- 方法/构造器候选数: 107
```text
public static Server getInstance()
private Server()
public int getCurrentTimestamp()
public long getCurrentTime()
public void updateCurrentTime()
public long forceUpdateCurrentTime()
public void setNewYearCard(NewYearCardRecord nyc)
public NewYearCardRecord getNewYearCard(int cardid)
public NewYearCardRecord removeNewYearCard(int cardid)
public void setAvailableDeveloperRoom()
public boolean canEnterDeveloperRoom()
private void loadPlayerNpcMapStepFromDb()
public World getWorld(int id)
public List<World> getWorlds()
public int getWorldsSize()
public Channel getChannel(int world, int channel)
public List<Channel> getChannelsFromWorld(int world)
public List<Channel> getAllChannels()
public Set<Integer> getOpenChannels(int world)
private String getIP(int world, int channel)
public String[] getInetSocket(Client client, int world, int channel)
public int addChannel(int worldid)
public int addWorld()
private int initWorld()
public boolean removeChannel(int worldid)
public boolean removeWorld()
private void resetServerWorlds()
private static long getTimeLeftForNextHour()
public static long getTimeLeftForNextDay()
public List<Integer> getActiveCoupons()
public void commitActiveCoupons()
public void toggleCoupon(Integer couponId)
public void updateActiveCoupons()
public void runAnnouncePlayerDiseasesSchedule()
public void registerAnnouncePlayerDiseases(Client c)
public void reloadWorldsPlayerRanking()
public void init()
private void registerChannelDependencies()
private LoginServer initLoginServer(int port)
private void initializeTimelyTasks()
public Alliance getAlliance(int id)
public void addAlliance(int id, Alliance alliance)
public void disbandAlliance(int id)
public void allianceMessage(int id, Packet packet, int exception, int guildex)
public boolean addGuildtoAlliance(int aId, int guildId)
public boolean removeGuildFromAlliance(int aId, int guildId)
public boolean setAllianceRanks(int aId, String[] ranks)
public boolean setAllianceNotice(int aId, String notice)
public boolean increaseAllianceCapacity(int aId, int inc)
public int createGuild(int leaderId, String name)
public Guild getGuildByName(String name)
public Guild getGuild(int id)
public Guild getGuild(int id, int world)
public Guild getGuild(int id, int world, Character mc)
public void setGuildMemberOnline(Character mc, boolean bOnline, int channel)
public int addGuildMember(GuildCharacter mgc, Character chr)
public boolean setGuildAllianceId(int gId, int aId)
public void resetAllianceGuildPlayersRank(int gId)
public void leaveGuild(GuildCharacter mgc)
public void guildChat(int gid, String name, int cid, String msg)
public void changeRank(int gid, int cid, int newRank)
public void expelMember(GuildCharacter initiator, String name, int cid)
public void setGuildNotice(int gid, String notice)
public void memberLevelJobUpdate(GuildCharacter mgc)
public void changeRankTitle(int gid, String[] ranks)
public void setGuildEmblem(int gid, short bg, byte bgcolor, short logo, byte logocolor)
public void disbandGuild(int gid)
public boolean increaseGuildCapacity(int gid)
public void gainGP(int gid, int amount)
public void guildMessage(int gid, Packet packet)
public void guildMessage(int gid, Packet packet, int exception)
public PlayerBuffStorage getPlayerBuffStorage()
public void deleteGuildCharacter(Character mc)
public void deleteGuildCharacter(GuildCharacter mgc)
public void reloadGuildCharacters(int world)
public void broadcastMessage(int world, Packet packet)
public void broadcastGMMessage(int world, Packet packet)
public boolean isGmOnline(int world)
public void changeFly(Integer accountid, boolean canFly)
public boolean canFly(Integer accountid)
public int getCharacterWorld(Integer chrid)
public boolean haveCharacterEntry(Integer accountid, Integer chrid)
public short getAccountCharacterCount(Integer accountid)
public short getAccountWorldCharacterCount(Integer accountid, Integer worldid)
private Set<Integer> getAccountCharacterEntries(Integer accountid)
public void updateCharacterEntry(Character chr)
public void createCharacterEntry(Character chr)
public void deleteCharacterEntry(Integer accountid, Integer chrid)
public void transferWorldCharacterEntry(Character chr, Integer toWorld)
public void loadAllAccountsCharactersView()
private boolean isFirstAccountLogin(Integer accId)
public void loadAccountCharacters(Client c)
private int loadAccountCharactersView(Integer accId, int gmLevel, int fromWorldid)
public void loadAccountStorages(Client c)
private static String getRemoteHost(Client client)
public void setCharacteridInTransition(Client client, int charId)
public boolean validateCharacteridInTransition(Client client, int charId)
public Integer freeCharacteridInTransition(Client client)
public boolean hasCharacteridInTransition(Client client)
public void registerLoginState(Client c)
public void unregisterLoginState(Client c)
private void disconnectIdlesOnLoginState()
private void disconnectIdlesOnLoginTask()
public final Runnable shutdown(final boolean restart)
public synchronized void shutdownInternal(boolean restart)
public boolean isNextTime()
public synchronized void shutdownWithMsgAndInternal(ServerShutdownDTO serverShutdownDTO)
```

---

## `org.gms.net.server.channel` / `net/server/channel/Channel.java`

### 类型声明
```text
class Channel
```

- 字段候选数: 27
```text
private static final int BASE_PORT = 7575
private final int port
private final String ip
private final int world
private final int channel
private ChannelServer channelServer
private String serverMessage
private MapManager mapManager
private EventScriptManager eventSM
private ServicesManager services
private Event event
private boolean finishedShutdown = false
private int usedDojo = 0
private int[] dojoStage
private long[] dojoFinishTime
private ScheduledFuture<?>[] dojoTask
private ScheduledFuture<?> chapelReservationTask
private ScheduledFuture<?> cathedralReservationTask
private Integer ongoingChapel = null
private Boolean ongoingChapelType = null
private Set<Integer> ongoingChapelGuests = null
private Integer ongoingCathedral = null
private Boolean ongoingCathedralType = null
private Set<Integer> ongoingCathedralGuests = null
private long ongoingStartTime
private final Lock merchRlock
private final Lock merchWlock
```

- 方法/构造器候选数: 80
```text
public Channel(final int world, final int channel, long startTime)
private ChannelServer initServer(int port, int world, int channel)
public synchronized void reloadEventScriptManager()
public synchronized void shutdown()
private void closeChannelServices()
private void closeChannelSchedules()
private void closeAllMerchants()
public MapManager getMapFactory()
public BaseService getServiceAccess(ChannelServices sv)
public int getWorld()
public World getWorldServer()
public void addPlayer(Character chr)
public String getServerMessage()
public PlayerStorage getPlayerStorage()
public boolean removePlayer(Character chr)
public int getChannelCapacity()
public void broadcastPacket(Packet packet)
public final int getId()
public String getIP()
public Event getEvent()
public void setEvent(Event event)
public EventScriptManager getEventSM()
public void broadcastGMPacket(Packet packet)
public List<Character> getPartyMembers(Party party)
public void insertPlayerAway(int chrId)
public void removePlayerAway(int chrId)
public boolean canUninstall()
private void disconnectAwayPlayers()
public void addHiredMerchant(int chrid, HiredMerchant hm)
public void removeHiredMerchant(int chrid)
public int[] multiBuddyFind(int charIdFrom, int[] characterIds)
public boolean addExpedition(Expedition exped)
public void removeExpedition(Expedition exped)
public Expedition getExpedition(ExpeditionType type)
public List<Expedition> getExpeditions()
public boolean isConnected(String name)
public boolean isActive()
public boolean finishedShutdown()
public void setServerMessage(String message)
private static String[] getEvents()
public int getStoredVar(int key)
public void setStoredVar(int key, int val)
public int lookupPartyDojo(Party party)
public int ingressDojo(boolean isPartyDojo, int fromStage)
public int ingressDojo(boolean isPartyDojo, Party party, int fromStage)
private void freeDojoSlot(int slot, Party party)
private static int getDojoSlot(int dojoMapId)
public void resetDojoMap(int fromMapId)
public void resetDojo(int dojoMapId)
private void resetDojo(int dojoMapId, int thisStg)
public void freeDojoSectionIfEmpty(int dojoMapId)
private void startDojoSchedule(final int dojoMapId)
public void dismissDojoSchedule(int dojoMapId, Party party)
public boolean setDojoProgress(int dojoMapId)
public long getDojoFinishTime(int dojoMapId)
public boolean addMiniDungeon(int dungeonid)
public MiniDungeon getMiniDungeon(int dungeonid)
public void removeMiniDungeon(int dungeonid)
public boolean isWeddingReserved(Integer weddingId)
public int getWeddingReservationStatus(Integer weddingId, boolean cathedral)
public int pushWeddingReservation(Integer weddingId, boolean cathedral, boolean premium, Integer groomId, Integer brideId)
public boolean isOngoingWeddingGuest(boolean cathedral, int playerId)
public Integer getOngoingWedding(boolean cathedral)
public boolean getOngoingWeddingType(boolean cathedral)
public void closeOngoingWedding(boolean cathedral)
public void setOngoingWedding(final boolean cathedral, Boolean premium, Integer weddingId, Set<Integer> guests)
public synchronized boolean acceptOngoingWedding(final boolean cathedral)
private static String getTimeLeft(long futureTime)
public long getWeddingTicketExpireTime(int resSlot)
public static long getRelativeWeddingTicketExpireTime(int resSlot)
public String getWeddingReservationTimeLeft(Integer weddingId)
public void dropMessage(int type, String message)
public void registerOwnedMap(MapleMap map)
public void unregisterOwnedMap(MapleMap map)
public void runCheckOwnedMapsSchedule()
private static int getMonsterCarnivalRoom(boolean cpq1, int field)
public void initMonsterCarnival(boolean cpq1, int field)
public void finishMonsterCarnival(boolean cpq1, int field)
public boolean canInitMonsterCarnival(boolean cpq1, int field)
public void debugMarriageStatus()
```

---

## `org.gms.net.server.channel` / `net/server/channel/CharacterIdChannelPair.java`

### 类型声明
```text
class CharacterIdChannelPair
```

- 字段候选数: 2
```text
private int charid
private int channel
```

- 方法/构造器候选数: 4
```text
public CharacterIdChannelPair()
public CharacterIdChannelPair(int charid, int channel)
public int getCharacterId()
public int getChannel()
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AbstractDealDamageHandler.java`

### 类型声明
```text
class AbstractDealDamageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 22
```text
protected void applyAttack(AttackInfo attack, final Character player, int attackCount)
private static void damageMonsterWithSkill(final Character attacker, final MapleMap map, final Monster monster, final int damage, int skillid, int fixedTime)
protected AttackInfo parseDamage(InPacket p, Character chr, boolean ranged, boolean magic)
private static boolean isWithinAttackBox(Character player, Monster monster, StatEffect attackEffect, AttackInfo attack, Point alternatePlayerPos, Point secondaryAlternatePlayerPos)
private static boolean isWithinAttackBox(Point playerPos, Rectangle monsterBounds, Point monsterPos, StatEffect attackEffect, boolean facingLeft)
private static boolean intersectsAnyAttackBox(Rectangle monsterBounds, Point monsterPos, StatEffect attackEffect, boolean facingLeft, Point... playerPositions)
private static boolean isFacingLeftByDirection(int direction)
private static boolean isFacingLeftByStance(int stance)
private static Rectangle getMonsterBounds(Monster monster)
private static boolean isFullScreenDistanceExempt(int skillId)
private static boolean shouldSkipDistanceHackCheck(int skillId, StatEffect attackEffect)
private static boolean isNonSpatialAttackSkill(int skillId, StatEffect attackEffect)
private static boolean hasReliableDistanceGeometry(StatEffect attackEffect, boolean useBbox)
private static boolean hasSkillAttackBox(StatEffect attackEffect)
private static DistanceCheckSample chooseBestDistanceCheckSample(Point currentPlayerPos, Monster monster, boolean useBbox, Point teleportBeforePos, Point movementBeforePos)
private static DistanceCheckSample chooseCloserDistanceSample(DistanceCheckSample currentBest, Point candidatePos, Monster monster, boolean useBbox, Point currentPlayerPos, boolean usedTeleportContext, boolean usedMovementContext)
private static boolean shouldUseBoundingBox(Monster monster)
private static double calculateDistanceSq(Point playerPos, Monster monster, boolean useBbox)
private static String buildBboxInfo(Character player, Monster monster, boolean useBbox, Point checkPos, Point teleportBeforePos, Point movementBeforePos, boolean usedTeleportContext, boolean usedMovementContext)
private static int[] getWorldBbox(Monster monster, MonsterStats stats)
private static void detectionAttackInterval(Character chr, AttackInfo ret)
private static int rand(int l, int u)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AbstractMovementPacketHandler.java`

### 类型声明
```text
class AbstractMovementPacketHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
protected List<LifeMovementFragment> parseMovement(InPacket p) throws EmptyMovementException
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AcceptFamilyHandler.java`

### 类型声明
```text
class AcceptFamilyHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private static void insertNewFamilyRecord(int characterID, int familyID, int seniorID, boolean updateChar)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AdminChatHandler.java`

### 类型声明
```text
class AdminChatHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AdminCommandHandler.java`

### 类型声明
```text
class AdminCommandHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AdminLogHandler.java`

### 类型声明
```text
class AdminLogHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AllianceOperationHandler.java`

### 类型声明
```text
class AllianceOperationHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public final void handlePacket(InPacket p, Client c)
private void changeLeaderAllianceRank(Alliance alliance, Character newLeader)
private void changePlayerAllianceRank(Alliance alliance, Character chr, boolean raise)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AranComboHandler.java`

### 类型声明
```text
class AranComboHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AutoAggroHandler.java`

### 类型声明
```text
class AutoAggroHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/AutoAssignHandler.java`

### 类型声明
```text
class AutoAssignHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/BBSOperationHandler.java`

### 类型声明
```text
class BBSOperationHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 10
```text
private String correctLength(String in, int maxSize)
public void handlePacket(InPacket p, Client c)
private static void listBBSThreads(Client c, int start)
private static void newBBSReply(Client c, int localthreadid, String text)
private static void editBBSThread(Client client, String title, String text, int icon, int localthreadid)
private static void newBBSThread(Client client, String title, String text, int icon, boolean bNotice)
public static void deleteBBSThread(Client client, int localthreadid)
public static void deleteBBSReply(Client client, int replyid)
public static void displayThread(Client client, int threadid)
public static void displayThread(Client client, int threadid, boolean bIsThreadIdLocal)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/BeholderHandler.java`

### 类型声明
```text
class BeholderHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/BuddylistModifyHandler.java`

### 类型声明
```text
class BuddylistModifyHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
private void nextPendingRequest(Client c)
private CharacterIdNameBuddyCapacity getCharacterIdAndNameFromDatabase(String name) throws SQLException
public void handlePacket(InPacket p, Client c)
private void notifyRemoteChannel(Client c, int remoteChannel, int otherCid, BuddyOperation operation)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CancelBuffHandler.java`

### 类型声明
```text
class CancelBuffHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CancelChairHandler.java`

### 类型声明
```text
class CancelChairHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CancelDebuffHandler.java`

### 类型声明
```text
class CancelDebuffHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CancelItemEffectHandler.java`

### 类型声明
```text
class CancelItemEffectHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CashOperationHandler.java`

### 类型声明
```text
class CashOperationHandler
```

- 字段候选数: 1
```text
private final NoteService noteService
```

- 方法/构造器候选数: 5
```text
public CashOperationHandler(NoteService noteService)
private static boolean ensureCashInventoryCapacity(Client c, CashShop cs, int itemsToAdd)
public void handlePacket(InPacket p, Client c)
public static boolean checkBirthday(Client c, int idate)
private static boolean canBuy(Character chr, ModifiedCashItemDO item, int cash)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CashShopSurpriseHandler.java`

### 类型声明
```text
class CashShopSurpriseHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ChangeChannelHandler.java`

### 类型声明
```text
class ChangeChannelHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ChangeMapHandler.java`

### 类型声明
```text
class ChangeMapHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public void handlePacket(InPacket p, Client c)
private void enterFromCashShop(Client c)
private static String getFormattedMapListLogMessage(List<Integer> MapIds,Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ChangeMapSpecialHandler.java`

### 类型声明
```text
class ChangeMapSpecialHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CharInfoRequestHandler.java`

### 类型声明
```text
class CharInfoRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ClickGuideHandler.java`

### 类型声明
```text
class ClickGuideHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CloseChalkboardHandler.java`

### 类型声明
```text
class CloseChalkboardHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CloseRangeDamageHandler.java`

### 类型声明
```text
class CloseRangeDamageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CoconutHandler.java`

### 类型声明
```text
class CoconutHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/CouponCodeHandler.java`

### 类型声明
```text
class CouponCodeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseCouponResult(int res)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DamageSummonHandler.java`

### 类型声明
```text
class DamageSummonHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DenyAllianceRequestHandler.java`

### 类型声明
```text
class DenyAllianceRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DenyGuildRequestHandler.java`

### 类型声明
```text
class DenyGuildRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DenyPartyRequestHandler.java`

### 类型声明
```text
class DenyPartyRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DistributeAPHandler.java`

### 类型声明
```text
class DistributeAPHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DistributeSPHandler.java`

### 类型声明
```text
class DistributeSPHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DoorHandler.java`

### 类型声明
```text
class DoorHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/DueyHandler.java`

### 类型声明
```text
class DueyHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/EnterCashShopHandler.java`

### 类型声明
```text
class EnterCashShopHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/EnterMTSHandler.java`

### 类型声明
```text
class EnterMTSHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public void handlePacket(InPacket p, Client c)
private List<MTSItemInfo> getNotYetSold(int cid)
private List<MTSItemInfo> getTransfer(int cid)
private void openCenterScript(Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FaceExpressionHandler.java`

### 类型声明
```text
class FaceExpressionHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FamilyAddHandler.java`

### 类型声明
```text
class FamilyAddHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FamilyPreceptsHandler.java`

### 类型声明
```text
class FamilyPreceptsHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FamilySeparateHandler.java`

### 类型声明
```text
class FamilySeparateHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private static int separateRepCost(FamilyEntry junior)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FamilySummonResponseHandler.java`

### 类型声明
```text
class FamilySummonResponseHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FamilyUseHandler.java`

### 类型声明
```text
class FamilyUseHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public final void handlePacket(InPacket p, Client c)
private boolean useEntitlement(FamilyEntry entry, FamilyEntitlement entitlement)
private void applyPartyBuff(Client c, int type, int effect, int duration, FamilyEntitlement entitlement)
private void applySelfBuff(Client c, int type, int effect, int duration, float rate, FamilyEntitlement entitlement)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FieldDamageMobHandler.java`

### 类型声明
```text
class FieldDamageMobHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/FredrickHandler.java`

### 类型声明
```text
class FredrickHandler
```

- 字段候选数: 1
```text
private final FredrickProcessor fredrickProcessor
```

- 方法/构造器候选数: 2
```text
public FredrickHandler(FredrickProcessor fredrickProcessor)
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/GeneralChatHandler.java`

### 类型声明
```text
class GeneralChatHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/GiveFameHandler.java`

### 类型声明
```text
class GiveFameHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/GrenadeEffectHandler.java`

### 类型声明
```text
class GrenadeEffectHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/GuildOperationHandler.java`

### 类型声明
```text
class GuildOperationHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private boolean isGuildNameAcceptable(String name)
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/HealOvertimeHandler.java`

### 类型声明
```text
class HealOvertimeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/HiredMerchantRequest.java`

### 类型声明
```text
class HiredMerchantRequest
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/InnerPortalHandler.java`

### 类型声明
```text
class InnerPortalHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
public final void handlePacket(InPacket p, Client c)
private static boolean isPlayerReady(Character player)
private static String readPortalNameSafely(InPacket p)
private static Portal resolveValidSourcePortal(Character player, String portalName)
private static boolean isPlayerNearPortal(Point playerPos, Portal portal)
private static boolean isSameMapInnerTeleport(Character player, Portal sourcePortal)
private static Portal resolveValidTargetPortal(Character player, Portal sourcePortal)
private static void movePlayerInMap(Character player, Point afterPos)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/InventoryMergeHandler.java`

### 类型声明
```text
class InventoryMergeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/InventorySortHandler.java`

### 类型声明
```text
class PairedQuicksort
class InventorySortHandler
```

- 字段候选数: 3
```text
private int i = 0
private int j = 0
private final ArrayList<Integer> intersect
```

- 方法/构造器候选数: 12
```text
private void PartitionByItemId(int Esq, int Dir, ArrayList<Item> A)
private int getWatkForProjectile(Item item)
private void PartitionByProjectileAtk(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByName(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByQuantity(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByLevel(int Esq, int Dir, ArrayList<Item> A)
void MapleQuicksort(int Esq, int Dir, ArrayList<Item> A, int sort)
private static int getItemSubtype(Item it)
private int[] BinarySearchElement(ArrayList<Item> A, int rangeId)
public void reverseSortSublist(ArrayList<Item> A, int[] range)
public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ItemMoveHandler.java`

### 类型声明
```text
class ItemMoveHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ItemPickupHandler.java`

### 类型声明
```text
class ItemPickupHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(final InPacket p, final Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ItemRewardHandler.java`

### 类型声明
```text
class ItemRewardHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/KeymapChangeHandler.java`

### 类型声明
```text
class KeymapChangeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/LeftKnockbackHandler.java`

### 类型声明
```text
class LeftKnockbackHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, final Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MTSHandler.java`

### 类型声明
```text
class MTSHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public void handlePacket(InPacket p, Client c)
public List<MTSItemInfo> getNotYetSold(int cid)
public Packet getCart(int cid)
public List<MTSItemInfo> getTransfer(int cid)
private static Packet getMTS(int tab, int type, int page)
public Packet getMTSSearch(int tab, int type, int cOi, String search, int page)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MagicDamageHandler.java`

### 类型声明
```text
class MagicDamageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MakerSkillHandler.java`

### 类型声明
```text
class MakerSkillHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MesoDropHandler.java`

### 类型声明
```text
class MesoDropHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MessengerHandler.java`

### 类型声明
```text
class MessengerHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MobBanishPlayerHandler.java`

### 类型声明
```text
class MobBanishPlayerHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MobDamageMobFriendlyHandler.java`

### 类型声明
```text
class MobDamageMobFriendlyHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MobDamageMobHandler.java`

### 类型声明
```text
class MobDamageMobHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public void handlePacket(InPacket p, Client c)
private static int calcMaxDamage(Monster attacker, Monster damaged, boolean magic)
private static int calcModifier(Monster monster, MonsterStatus buff, MonsterStatus nerf)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MonsterBombHandler.java`

### 类型声明
```text
class MonsterBombHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MonsterBookCoverHandler.java`

### 类型声明
```text
class MonsterBookCoverHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MonsterCarnivalHandler.java`

### 类型声明
```text
class MonsterCarnivalHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private int rollHitChance(MobSkillType type)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MoveDragonHandler.java`

### 类型声明
```text
class MoveDragonHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MoveLifeHandler.java`

### 类型声明
```text
class MoveLifeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private static boolean inRangeInclusive(Byte pVal, Integer pMin, Integer pMax)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MovePetHandler.java`

### 类型声明
```text
class MovePetHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MovePlayerHandler.java`

### 类型声明
```text
class MovePlayerHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MoveSummonHandler.java`

### 类型声明
```text
class MoveSummonHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/MultiChatHandler.java`

### 类型声明
```text
class MultiChatHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NPCAnimationHandler.java`

### 类型声明
```text
class NPCAnimationHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NPCMoreTalkHandler.java`

### 类型声明
```text
class NPCMoreTalkHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public final void handlePacket(InPacket p, Client c)
private void cmRouting(Client c, byte action, byte lastMsg, int selection)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NPCShopHandler.java`

### 类型声明
```text
class NPCShopHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NPCTalkHandler.java`

### 类型声明
```text
class NPCTalkHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NewYearCardHandler.java`

### 类型声明
```text
class NewYearCardHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public final void handlePacket(InPacket p, Client c)
private static int getReceiverId(String receiver, int world)
private static int getValidNewYearCardStatus(int itemid, Character player, short slot)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/NoteActionHandler.java`

### 类型声明
```text
class NoteActionHandler
```

- 字段候选数: 1
```text
private final NoteService noteService
```

- 方法/构造器候选数: 2
```text
public NoteActionHandler(NoteService noteService)
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/OpenFamilyHandler.java`

### 类型声明
```text
class OpenFamilyHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/OpenFamilyPedigreeHandler.java`

### 类型声明
```text
class OpenFamilyPedigreeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/OwlWarpHandler.java`

### 类型声明
```text
class OwlWarpHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PartyOperationHandler.java`

### 类型声明
```text
class PartyOperationHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PartySearchRegisterHandler.java`

### 类型声明
```text
class PartySearchRegisterHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PartySearchStartHandler.java`

### 类型声明
```text
class PartySearchStartHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PartySearchUpdateHandler.java`

### 类型声明
```text
class PartySearchUpdateHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetAutoPotHandler.java`

### 类型声明
```text
class PetAutoPotHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetChatHandler.java`

### 类型声明
```text
class PetChatHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetCommandHandler.java`

### 类型声明
```text
class PetCommandHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetExcludeItemsHandler.java`

### 类型声明
```text
class PetExcludeItemsHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetFoodHandler.java`

### 类型声明
```text
class PetFoodHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PetLootHandler.java`

### 类型声明
```text
class PetLootHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PlayerInteractionHandler.java`

### 类型声明
```text
class PlayerInteractionHandler
enum Action
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
private static int establishMiniroomStatus(Character chr, boolean isMinigame)
public final void handlePacket(InPacket p, Client c)
private static boolean isTradeOpen(Character chr)
private static boolean canPlaceStore(Character chr)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PlayerLoggedinHandler.java`

### 类型声明
```text
class PlayerLoggedinHandler
```

- 字段候选数: 1
```text
private final NoteService noteService
```

- 方法/构造器候选数: 6
```text
public PlayerLoggedinHandler(NoteService noteService)
private boolean tryAcquireAccount(int accId)
private void releaseAccount(int accId)
public final boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
private static void showDueyNotification(Client c, Character player)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/PlayerMapTransitionHandler.java`

### 类型声明
```text
class PlayerMapTransitionHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/QuestActionHandler.java`

### 类型声明
```text
class QuestActionHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static boolean isNpcNearby(InPacket p, Character player, Quest quest, int npcId)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/QuickslotKeyMappedModifiedHandler.java`

### 类型声明
```text
class QuickslotKeyMappedModifiedHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RPSActionHandler.java`

### 类型声明
```text
class RPSActionHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RaiseIncExpHandler.java`

### 类型声明
```text
class RaiseIncExpHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RaiseUIStateHandler.java`

### 类型声明
```text
class RaiseUIStateHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RangedAttackHandler.java`

### 类型声明
```text
class RangedAttackHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ReactorHitHandler.java`

### 类型声明
```text
class ReactorHitHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RemoteGachaponHandler.java`

### 类型声明
```text
class RemoteGachaponHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RemoteStoreHandler.java`

### 类型声明
```text
class RemoteStoreHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private static HiredMerchant getMerchant(Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ReportHandler.java`

### 类型声明
```text
class ReportHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public final void handlePacket(InPacket p, Client c)
private void addReport(int reporterid, int victimid, int reason, String description, String chatlog)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/RingActionHandler.java`

### 类型声明
```text
class RingActionHandler
```

- 字段候选数: 1
```text
private final NoteService noteService
```

- 方法/构造器候选数: 12
```text
public RingActionHandler(NoteService noteService)
private static int getEngagementBoxId(int useItemId)
public static void sendEngageProposal(final Client c, final String name, final int itemid)
private static void eraseEngagementOffline(int characterId)
private static void eraseEngagementOffline(int characterId, Connection con) throws SQLException
private static void breakEngagementOffline(int characterId)
private synchronized static void breakMarriage(Character chr)
private static void resetRingId(Character player)
private synchronized static void breakEngagement(Character chr)
public static void breakMarriageRing(Character chr, final int wItemId)
public static void giveMarriageRings(Character player, Character partner, int marriageRingId)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ScriptedItemHandler.java`

### 类型声明
```text
class ScriptedItemHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/ScrollHandler.java`

### 类型声明
```text
class ScrollHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public final void handlePacket(InPacket p, Client c)
private static void announceCannotScroll(Client c, boolean legendarySpirit)
private static boolean canScroll(int scrollid, int itemid)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SetHpMpAlertHandler.java`

### 类型声明
```text
class SetHpMpAlertHandler
```

- 字段候选数: 1
```text
private static final int MAX_ALERT_STEP = 19
```

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SkillBookHandler.java`

### 类型声明
```text
class SkillBookHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SkillEffectHandler.java`

### 类型声明
```text
class SkillEffectHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SkillMacroHandler.java`

### 类型声明
```text
class SkillMacroHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SnowballHandler.java`

### 类型声明
```text
class SnowballHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SpawnPetHandler.java`

### 类型声明
```text
class SpawnPetHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SpecialMoveHandler.java`

### 类型声明
```text
class SpecialMoveHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SpouseChatHandler.java`

### 类型声明
```text
class SpouseChatHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/StorageHandler.java`

### 类型声明
```text
class StorageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/SummonDamageHandler.java`

### 类型声明
```text
class SummonDamageHandler
class SummonAttackEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
private static int calcMaxDamage(StatEffect summonEffect, Character player, boolean magic)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TakeDamageHandler.java`

### 类型声明
```text
class TakeDamageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TouchMonsterDamageHandler.java`

### 类型声明
```text
class TouchMonsterDamageHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TouchReactorHandler.java`

### 类型声明
```text
class TouchReactorHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TouchingCashShopHandler.java`

### 类型声明
```text
class TouchingCashShopHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TransferNameHandler.java`

### 类型声明
```text
class TransferNameHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TransferNameResultHandler.java`

### 类型声明
```text
class TransferNameResultHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TransferWorldHandler.java`

### 类型声明
```text
class TransferWorldHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/TrockAddMapHandler.java`

### 类型声明
```text
class TrockAddMapHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseCashItemHandler.java`

### 类型声明
```text
class UseCashItemHandler
```

- 字段候选数: 1
```text
private final NoteService noteService
```

- 方法/构造器候选数: 5
```text
public UseCashItemHandler(NoteService noteService)
public void handlePacket(InPacket p, Client c)
private static void remove(Client c, short position, int itemid)
private static boolean getIncubatedItem(Client c, int id)
private static void notEnabled(Character player)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseCatchItemHandler.java`

### 类型声明
```text
class UseCatchItemHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseChairHandler.java`

### 类型声明
```text
class UseChairHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseDeathItemHandler.java`

### 类型声明
```text
class UseDeathItemHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseGachaExpHandler.java`

### 类型声明
```text
class UseGachaExpHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseHammerHandler.java`

### 类型声明
```text
class UseHammerHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseItemEffectHandler.java`

### 类型声明
```text
class UseItemEffectHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseItemHandler.java`

### 类型声明
```text
class UseItemHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public final void handlePacket(InPacket p, Client c)
private void remove(Client c, short slot)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseMapleLifeHandler.java`

### 类型声明
```text
class UseMapleLifeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseMountFoodHandler.java`

### 类型声明
```text
class UseMountFoodHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseOwlOfMinervaHandler.java`

### 类型声明
```text
class UseOwlOfMinervaHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseSolomonHandler.java`

### 类型声明
```text
class UseSolomonHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseSummonBagHandler.java`

### 类型声明
```text
class UseSummonBagHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseTreasureChestHandler.java`

### 类型声明
```text
class UseTreasureChestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/UseWaterOfLifeHandler.java`

### 类型声明
```text
class UseWaterOfLifeHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/WeddingHandler.java`

### 类型声明
```text
class WeddingHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/WeddingTalkHandler.java`

### 类型声明
```text
class WeddingTalkHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/WeddingTalkMoreHandler.java`

### 类型声明
```text
class WeddingTalkMoreHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.channel.handlers` / `net/server/channel/handlers/WhisperHandler.java`

### 类型声明
```text
class WhisperHandler
```

- 字段候选数: 4
```text
public static final byte RT_ITC = 0x00
public static final byte RT_SAME_CHANNEL = 0x01
public static final byte RT_CASH_SHOP = 0x02
public static final byte RT_DIFFERENT_CHANNEL = 0x03
```

- 方法/构造器候选数: 3
```text
public void handlePacket(InPacket p, Client c)
private void handleFind(Character user, Character target, byte flag)
private void handleWhisper(String message, Character user, Character target)
```

---

## `org.gms.net.server.coordinator.login` / `net/server/coordinator/login/LoginBypassCoordinator.java`

### 类型声明
```text
class LoginBypassCoordinator
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static LoginBypassCoordinator getInstance()
public boolean canLoginBypass(Hwid hwid, int accId, boolean pic)
public void registerLoginBypassEntry(Hwid hwid, int accId, boolean pic)
public void unregisterLoginBypassEntry(Hwid hwid, int accId)
public void runUpdateLoginBypass()
```

---

## `org.gms.net.server.coordinator.login` / `net/server/coordinator/login/LoginStorage.java`

### 类型声明
```text
class LoginStorage
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public boolean registerLogin(int accountId)
public void clearExpiredAttempts()
```

---

## `org.gms.net.server.coordinator.matchchecker` / `net/server/coordinator/matchchecker/AbstractMatchCheckerListener.java`

### 类型声明
```text
interface AbstractMatchCheckerListener
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.coordinator.matchchecker` / `net/server/coordinator/matchchecker/MatchCheckerCoordinator.java`

### 类型声明
```text
class MatchCheckerCoordinator
class MatchCheckingEntry
class MatchCheckingElement
```

- 字段候选数: 0

- 方法/构造器候选数: 17
```text
private void unpoolMatchPlayer(Integer cid)
private void unpoolMatchPlayers(Set<Integer> matchPlayers)
private boolean poolMatchPlayer(Integer cid)
private boolean poolMatchPlayers(Set<Integer> matchPlayers)
private boolean isMatchingAvailable(Set<Integer> matchPlayers)
private void reenablePlayerMatching(Set<Integer> matchPlayers)
public int getMatchConfirmationLeaderid(int cid)
public MatchCheckerType getMatchConfirmationType(int cid)
public boolean isMatchConfirmationActive(int cid)
private MatchCheckingElement createMatchConfirmationInternal(MatchCheckerType matchType, int world, int leaderCid, AbstractMatchCheckerListener leaderListener, Set<Integer> players, String message)
public boolean createMatchConfirmation(MatchCheckerType matchType, int world, int leaderCid, Set<Integer> players, String message)
private void disposeMatchElement(MatchCheckingElement mmce)
private boolean acceptMatchElement(MatchCheckingElement mmce, int cid)
private void denyMatchElement(MatchCheckingElement mmce, int cid)
private void dismissMatchElement(MatchCheckingElement mmce, int cid)
public boolean answerMatchConfirmation(int cid, boolean accept)
public boolean dismissMatchConfirmation(int cid)
```

---

## `org.gms.net.server.coordinator.matchchecker` / `net/server/coordinator/matchchecker/MatchCheckerListenerFactory.java`

### 类型声明
```text
class MatchCheckerListenerFactory
enum MatchCheckerType
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.coordinator.matchchecker` / `net/server/coordinator/matchchecker/MatchCheckerListenerRecipe.java`

### 类型声明
```text
interface MatchCheckerListenerRecipe
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.coordinator.matchchecker.listener` / `net/server/coordinator/matchchecker/listener/MatchCheckerCPQChallenge.java`

### 类型声明
```text
class MatchCheckerCPQChallenge
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public static AbstractMatchCheckerListener loadListener()
private static Character getChallenger(int leaderid, Set<Character> matchPlayers)
public AbstractMatchCheckerListener getListener()
```

---

## `org.gms.net.server.coordinator.matchchecker.listener` / `net/server/coordinator/matchchecker/listener/MatchCheckerGuildCreation.java`

### 类型声明
```text
class MatchCheckerGuildCreation
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private static void broadcastGuildCreationDismiss(Set<Character> nonLeaderMatchPlayers)
public static AbstractMatchCheckerListener loadListener()
public AbstractMatchCheckerListener getListener()
```

---

## `org.gms.net.server.coordinator.partysearch` / `net/server/coordinator/partysearch/PartySearchCharacter.java`

### 类型声明
```text
class PartySearchCharacter
```

- 字段候选数: 3
```text
private final WeakReference<Character> player
private final int level
private boolean queued
```

- 方法/构造器候选数: 6
```text
public PartySearchCharacter(Character chr)
public String toString()
public Character callPlayer(int leaderid, int callerMapid)
public Character getPlayer()
public int getLevel()
public boolean isQueued()
```

---

## `org.gms.net.server.coordinator.partysearch` / `net/server/coordinator/partysearch/PartySearchCoordinator.java`

### 类型声明
```text
class PartySearchCoordinator
class LeaderSearchMetadata
```

- 字段候选数: 3
```text
private final Lock leaderQueueRLock
private final Lock leaderQueueWLock
private int updateCount = 0
```

- 方法/构造器候选数: 18
```text
public PartySearchCoordinator()
public static boolean isInVicinity(int callerMapid, int calleeMapid)
public void attachPlayer(Character chr)
public void detachPlayer(Character chr)
public void updatePartySearchStorage()
private static Job getPartySearchJob(Job job)
private Character fetchPlayer(int callerCid, int callerMapid, Job job, int minLevel, int maxLevel)
private void addQueueLeader(Character leader)
private void removeQueueLeader(Character leader)
public void registerPartyLeader(Character leader, int minLevel, int maxLevel, int jobs)
private void registerPartyLeader(Character leader, LeaderSearchMetadata settings)
public void unregisterPartyLeader(Character leader)
private Character searchPlayer(Character leader)
private boolean sendPartyInviteFromSearch(Character chr, Character leader)
private void registerLongTermPartyLeaders(List<Pair<Character, LeaderSearchMetadata>> recycledLeaders)
private void unregisterLongTermPartyLeader(Character leader)
private void reinstateLongTermPartyLeaders()
public void runPartySearch()
```

---

## `org.gms.net.server.coordinator.partysearch` / `net/server/coordinator/partysearch/PartySearchEchelon.java`

### 类型声明
```text
class PartySearchEchelon
```

- 字段候选数: 2
```text
private final Lock psRLock
private final Lock psWLock
```

- 方法/构造器候选数: 4
```text
public PartySearchEchelon()
public List<Character> exportEchelon()
public void attachPlayer(Character chr)
public boolean detachPlayer(Character chr)
```

---

## `org.gms.net.server.coordinator.partysearch` / `net/server/coordinator/partysearch/PartySearchStorage.java`

### 类型声明
```text
class PartySearchStorage
```

- 字段候选数: 2
```text
private final Lock psRLock
private final Lock psWLock
```

- 方法/构造器候选数: 6
```text
public PartySearchStorage()
public List<PartySearchCharacter> getStorageList()
public void updateStorage(Collection<Character> echelon)
private static int bsearchStorage(List<PartySearchCharacter> storage, int level)
public Character callPlayer(int callerCid, int callerMapid, int minLevel, int maxLevel)
public void detachPlayer(Character chr)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/HostHwid.java`

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
static HostHwid createWithDefaultExpiry(Hwid hwid)
private static Instant getDefaultExpiry()
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/HostHwidCache.java`

### 类型声明
```text
class HostHwidCache
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
void clearExpired()
void addEntry(String remoteHost, Hwid hwid)
HostHwid getEntry(String remoteHost)
Hwid removeEntryAndGetItsHwid(String remoteHost)
Hwid getEntryHwid(String remoteHost)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/Hwid.java`

- 字段候选数: 1
```text
private static final int HWID_LENGTH = 8
```

- 方法/构造器候选数: 2
```text
private static boolean isValidHostString(String hostString)
public static Hwid fromHostString(String hostString) throws IllegalArgumentException
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/HwidAssociationExpiry.java`

### 类型声明
```text
class HwidAssociationExpiry
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public static Instant getHwidAccountExpiry(int relevance)
private static long hwidExpirationUpdate(int relevance)
private static int getHwidExpirationDegree(int relevance)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/HwidRelevance.java`

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public int getIncrementedRelevance()
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/InitializationResult.java`

### 类型声明
```text
enum InitializationResult
```

- 字段候选数: 1
```text
private final AntiMulticlientResult antiMulticlientResult
```

- 方法/构造器候选数: 5
```text
SUCCESS(AntiMulticlientResult.SUCCESS),
ALREADY_INITIALIZED(AntiMulticlientResult.REMOTE_PROCESSING),
TIMED_OUT(AntiMulticlientResult.COORDINATOR_ERROR),
InitializationResult(AntiMulticlientResult antiMulticlientResult)
public AntiMulticlientResult getAntiMulticlientResult()
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/IpAddresses.java`

### 类型声明
```text
class IpAddresses
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
private static List<Pattern> loadLocalAddressPatterns()
public static boolean isLocalAddress(String inetAddress)
public static boolean isLanAddress(String inetAddress)
private static boolean matchesPattern(Pattern pattern, String searchTerm)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/SessionCoordinator.java`

### 类型声明
```text
class SessionCoordinator
enum AntiMulticlientResult
```

- 字段候选数: 0

- 方法/构造器候选数: 20
```text
public static SessionCoordinator getInstance()
private SessionCoordinator()
private static boolean attemptAccountAccess(int accountId, Hwid hwid, boolean routineCheck)
public static String getSessionRemoteHost(Client client)
public void updateOnlineClient(Client client)
private void disconnectClientIfOnline(int accountId)
public boolean canStartLoginSession(Client client)
public void closeLoginSession(Client client)
private void clearLoginRemoteHost(Client client)
public AntiMulticlientResult attemptLoginSession(Client client, Hwid hwid, int accountId, boolean routineCheck)
public AntiMulticlientResult attemptGameSession(Client client, int accountId, Hwid hwid)
private static void associateHwidAccountIfAbsent(Hwid hwid, int accountId)
private static Client fetchInTransitionSessionClient(Client client)
public void closeSession(Client client, Boolean immediately)
public Hwid pickLoginSessionHwid(Client client)
public Hwid getGameSessionHwid(Client client)
public void clearExpiredHwidHistory()
public void runUpdateLoginHistory()
public void printSessionTrace()
public void printSessionTrace(Client c)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/SessionDAO.java`

### 类型声明
```text
class SessionDAO
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static void deleteExpiredHwidAccounts()
public static List<Hwid> getHwidsForAccount(Connection con, int accountId) throws SQLException
public static void registerAccountAccess(Connection con, int accountId, Hwid hwid, Instant expiry)
public static List<HwidRelevance> getHwidRelevance(Connection con, int accountId) throws SQLException
public static void updateAccountAccess(Connection con, Hwid hwid, int accountId, Instant expiry, int loginRelevance)
```

---

## `org.gms.net.server.coordinator.session` / `net/server/coordinator/session/SessionInitialization.java`

### 类型声明
```text
class SessionInitialization
```

- 字段候选数: 2
```text
private static final int MAX_INIT_TRIES = 2
private static final long RETRY_DELAY_MILLIS = 1777
```

- 方法/构造器候选数: 4
```text
SessionInitialization()
private Lock getLock(String remoteHost)
public InitializationResult initialize(String remoteHost)
public void finalize(String remoteHost)
```

---

## `org.gms.net.server.coordinator.world` / `net/server/coordinator/world/EventRecallCoordinator.java`

### 类型声明
```text
class EventRecallCoordinator
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static EventRecallCoordinator getInstance()
private static boolean isRecallableEvent(EventInstanceManager eim)
public EventInstanceManager recallEventInstance(int characterId)
public void storeEventInstance(int characterId, EventInstanceManager eim)
public void manageEventInstances()
```

---

## `org.gms.net.server.coordinator.world` / `net/server/coordinator/world/InviteCoordinator.java`

### 类型声明
```text
class InviteCoordinator
enum InviteResultType
enum InviteType
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public static boolean createInvite(InviteType type, Character from, Object referenceFrom, int targetCid, Object... params)
public static boolean hasInvite(InviteType type, int targetCid)
public static InviteResult answerInvite(InviteType type, int targetCid, Object referenceFrom, boolean answer)
public static void removeInvite(InviteType type, int targetCid)
public static void removePlayerIncomingInvites(int cid)
public static void runTimeoutSchedule()
```

---

## `org.gms.net.server.coordinator.world` / `net/server/coordinator/world/MonsterAggroCoordinator.java`

### 类型声明
```text
class MonsterAggroCoordinator
class PlayerAggroEntry
```

- 字段候选数: 1
```text
private ScheduledFuture<?> aggroMonitor = null
```

- 方法/构造器候选数: 15
```text
public void stopAggroCoordinator()
public void startAggroCoordinator()
private static void updateEntryExpiration(PlayerAggroEntry pae)
private static void insertEntryDamage(PlayerAggroEntry pae, int damage)
private static boolean expiredAfterUpdateEntryDamage(PlayerAggroEntry pae, int deltaTime)
public void addAggroDamage(Monster mob, int cid, int damage)
private void runAggroUpdate(int deltaTime)
private static void insertionSortAggroList(List<PlayerAggroEntry> paeList)
public boolean isLeadingCharacterAggro(Monster mob, Character player)
public void runSortLeadingCharactersAggro()
public void removeAggroEntries(Monster mob)
public void addPuppetAggro(Character player)
public void removePuppetAggro(Integer cid)
public List<Integer> getPuppetAggroList()
public void dispose()
```

---

## `org.gms.net.server.guild` / `net/server/guild/Alliance.java`

### 类型声明
```text
class Alliance
```

- 字段候选数: 5
```text
private int allianceId = -1
private int capacity
private String name
private String notice = ""
private String[] rankTitles = new String[5]
```

- 方法/构造器候选数: 31
```text
public Alliance(String name, int id)
public static boolean canBeUsedAllianceName(String name)
private static List<Character> getPartyGuildMasters(Party party)
public static Alliance createAlliance(Party party, String name)
public static Alliance createAllianceOnDb(List<Integer> guilds, String name)
public static Alliance loadAlliance(int id)
public void saveToDB()
public static void disbandAlliance(int allianceId)
private static void removeGuildFromAllianceOnDb(int guildId)
public static boolean removeGuildFromAlliance(int allianceId, int guildId, int worldId)
public void updateAlliancePackets(Character chr)
public boolean removeGuild(int gid)
public boolean addGuild(int gid)
private int getGuildIndex(int gid)
public void setRankTitle(String[] ranks)
public String getRankTitle(int rank)
public List<Integer> getGuilds()
public String getAllianceNotice()
public String getNotice()
public void setNotice(String notice)
public void increaseCapacity(int inc)
public void setCapacity(int newCapacity)
public int getCapacity()
public int getId()
public String getName()
public GuildCharacter getLeader()
public void dropMessage(String message)
public void dropMessage(int type, String message)
public void broadcastMessage(Packet packet)
public static void sendInvitation(Client c, String targetGuildName, int allianceId)
public static boolean answerInvitation(int targetId, String targetGuildName, int allianceId, boolean answer)
```

---

## `org.gms.net.server.guild` / `net/server/guild/Guild.java`

### 类型声明
```text
class Guild
enum BCOp
```

- 字段候选数: 3
```text
private final List<GuildCharacter> members
private final int world
private boolean bDirty = true
```

- 方法/构造器候选数: 58
```text
public Guild(int guildid, int world)
private void buildNotifications()
public void writeToDB(boolean bDisband)
public int getId()
public int getLeaderId()
public int setLeaderId(int charId)
public int getGP()
public int getLogo()
public void setLogo(int l)
public int getLogoColor()
public void setLogoColor(int c)
public int getLogoBG()
public void setLogoBG(int bg)
public int getLogoBGColor()
public void setLogoBGColor(int c)
public String getNotice()
public String getName()
public List<GuildCharacter> getMembers()
public int getCapacity()
public int getSignature()
public void broadcastNameChanged()
public void broadcastEmblemChanged()
public void broadcastInfoChanged()
public void broadcast(Packet packet)
public void broadcast(Packet packet, int exception)
public void broadcast(Packet packet, int exceptionId, BCOp bcop)
public void guildMessage(Packet serverNotice)
public void dropMessage(String message)
public void dropMessage(int type, String message)
public void broadcastMessage(Packet packet)
public final void setOnline(int cid, boolean online, int channel)
public void guildChat(String name, int cid, String message)
public String getRankTitle(int rank)
public static int createGuild(int leaderId, String name)
public int addGuildMember(GuildCharacter mgc, Character chr)
public void leaveGuild(GuildCharacter mgc)
public void expelMember(GuildCharacter initiator, String name, int cid, NoteService noteService)
public void changeRank(int cid, int newRank)
public void changeRank(GuildCharacter mgc, int newRank)
public void setGuildNotice(String notice)
public void memberLevelJobUpdate(GuildCharacter mgc)
public boolean equals(Object other)
public int hashCode()
public void changeRankTitle(String[] ranks)
public void disbandGuild()
public void setGuildEmblem(short bg, byte bgcolor, short logo, byte logocolor)
public GuildCharacter getMGC(int cid)
public boolean increaseCapacity()
public void gainGP(int amount)
public void removeGP(int amount)
public static GuildResponse sendInvitation(Client c, String targetName)
public static boolean answerInvitation(int targetId, String targetName, int guildId, boolean answer)
public static Set<Character> getEligiblePlayersForGuild(Character guildLeader)
public static void displayGuildRanks(Client c, int npcid)
public int getAllianceId()
public void setAllianceId(int aid)
public void resetAllianceGuildPlayersRank()
public static int getIncreaseGuildCost(int size)
```

---

## `org.gms.net.server.guild` / `net/server/guild/GuildCharacter.java`

### 类型声明
```text
class GuildCharacter
```

- 字段候选数: 9
```text
private Character character
private int level
private final int id
private int jobid
private int guildrank
private int guildid
private int allianceRank
private boolean online
private final String name
```

- 方法/构造器候选数: 24
```text
public GuildCharacter(Character chr)
public GuildCharacter(Character chr, int _id, int _lv, String _name, int _channel, int _world, int _job, int _rank, int _gid, boolean _on, int _allianceRank)
public void setCharacter(Character ch)
public Character getCharacter()
public int getLevel()
public void setLevel(int l)
public int getId()
public void setChannel(int ch)
public int getChannel()
public int getWorld()
public int getJobId()
public void setJobId(int job)
public int getGuildId()
public void setGuildId(int gid)
public int getGuildRank()
public void setOfflineGuildRank(int rank)
public void setGuildRank(int rank)
public int getAllianceRank()
public void setAllianceRank(int rank)
public boolean isOnline()
public void setOnline(boolean f)
public String getName()
public boolean equals(Object other)
public int hashCode()
```

---

## `org.gms.net.server.guild` / `net/server/guild/GuildPackets.java`

### 类型声明
```text
class GuildPackets
```

- 字段候选数: 0

- 方法/构造器候选数: 43
```text
public static Packet showGuildInfo(Character chr)
public static Packet guildMemberOnline(int guildId, int chrId, boolean bOnline)
public static Packet guildInvite(int guildId, String charName)
public static Packet createGuildMessage(String masterName, String guildName)
public static Packet genericGuildMessage(byte code)
public static Packet responseGuildMessage(byte code, String targetName)
public static Packet newGuildMember(GuildCharacter mgc)
public static Packet memberLeft(GuildCharacter mgc, boolean bExpelled)
public static Packet changeRank(GuildCharacter mgc)
public static Packet guildNotice(int guildId, String notice)
public static Packet guildMemberLevelJobUpdate(GuildCharacter mgc)
public static Packet rankTitleChange(int guildId, String[] ranks)
public static Packet guildDisband(int guildId)
public static Packet guildQuestWaitingNotice(byte channel, int waitingPos)
public static Packet guildEmblemChange(int guildId, short bg, byte bgcolor, short logo, byte logoColor)
public static Packet guildCapacityChange(int guildId, int capacity)
public static void addThread(final OutPacket p, ResultSet rs) throws SQLException
public static Packet BBSThreadList(ResultSet rs, int start) throws SQLException
public static Packet showThread(int localthreadid, ResultSet threadRS, ResultSet repliesRS) throws SQLException, RuntimeException
public static Packet showGuildRanks(int npcid, ResultSet rs) throws SQLException
public static Packet showPlayerRanks(int npcid, List<Pair<String, Integer>> worldRanking)
public static Packet updateGP(int guildId, int GP)
public static void getGuildInfo(OutPacket p, Guild guild)
public static Packet getAllianceInfo(Alliance alliance)
public static Packet updateAllianceInfo(Alliance alliance, int world)
public static Packet getGuildAlliances(Alliance alliance, int worldId)
public static Packet addGuildToAlliance(Alliance alliance, int newGuild, Client c)
public static Packet allianceMemberOnline(Character mc, boolean online)
public static Packet allianceNotice(int id, String notice)
public static Packet changeAllianceRankTitle(int alliance, String[] ranks)
public static Packet updateAllianceJobLevel(Character mc)
public static Packet removeGuildFromAlliance(Alliance alliance, int expelledGuild, int worldId)
public static Packet disbandAlliance(int alliance)
public static Packet allianceInvite(int allianceid, Character chr)
public static Packet GuildBoss_HealerMove(short nY)
public static Packet GuildBoss_PulleyStateChange(byte nState)
public static Packet guildNameChanged(int chrid, String guildName)
public static Packet guildMarkChanged(int chrId, Guild guild)
public static Packet sendShowInfo(int allianceid, int playerid)
public static Packet sendInvitation(int allianceid, int playerid, final String guildname)
public static Packet sendChangeGuild(int allianceid, int playerid, int guildid, int option)
public static Packet sendChangeLeader(int allianceid, int playerid, int victim)
public static Packet sendChangeRank(int allianceid, int playerid, int int1, byte byte1)
```

---

## `org.gms.net.server.guild` / `net/server/guild/GuildResponse.java`

### 类型声明
```text
enum GuildResponse
```

- 字段候选数: 1
```text
private final int value
```

- 方法/构造器候选数: 7
```text
NOT_IN_CHANNEL(0x2a),
ALREADY_IN_GUILD(0x28),
NOT_IN_GUILD(0x2d),
NOT_FOUND_INVITE(0x2e),
MANAGING_INVITE(0x36),
GuildResponse(int val)
public final Packet getPacket(String targetName)
```

---

## `org.gms.net.server.guild` / `net/server/guild/GuildSummary.java`

### 类型声明
```text
class GuildSummary
```

- 字段候选数: 6
```text
private final String name
private final short logoBG
private final byte logoBGColor
private final short logo
private final byte logoColor
private final int allianceId
```

- 方法/构造器候选数: 7
```text
public GuildSummary(Guild g)
public String getName()
public short getLogoBG()
public byte getLogoBGColor()
public short getLogo()
public byte getLogoColor()
public int getAllianceId()
```

---

## `org.gms.net.server.handlers` / `net/server/handlers/CustomPacketHandler.java`

### 类型声明
```text
class CustomPacketHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

---

## `org.gms.net.server.handlers` / `net/server/handlers/KeepAliveHandler.java`

### 类型声明
```text
class KeepAliveHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

---

## `org.gms.net.server.handlers` / `net/server/handlers/LoginRequiringNoOpHandler.java`

### 类型声明
```text
class LoginRequiringNoOpHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public static LoginRequiringNoOpHandler getInstance()
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/AcceptToSHandler.java`

### 类型声明
```text
class AcceptToSHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/AfterLoginHandler.java`

### 类型声明
```text
class AfterLoginHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/CharSelectedHandler.java`

### 类型声明
```text
class CharSelectedHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/CharSelectedWithPicHandler.java`

### 类型声明
```text
class CharSelectedWithPicHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/CharlistRequestHandler.java`

### 类型声明
```text
class CharlistRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/CheckCharNameHandler.java`

### 类型声明
```text
class CheckCharNameHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/CreateCharHandler.java`

### 类型声明
```text
class CreateCharHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/DeleteCharHandler.java`

### 类型声明
```text
class DeleteCharHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/GuestLoginHandler.java`

### 类型声明
```text
class GuestLoginHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/LoginPasswordHandler.java`

### 类型声明
```text
class LoginPasswordHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
private static void login(Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/RegisterPicHandler.java`

### 类型声明
```text
class RegisterPicHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/RegisterPinHandler.java`

### 类型声明
```text
class RegisterPinHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/RelogRequestHandler.java`

### 类型声明
```text
class RelogRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ServerStatusRequestHandler.java`

### 类型声明
```text
class ServerStatusRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ServerlistRequestHandler.java`

### 类型声明
```text
class ServerlistRequestHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/SetGenderHandler.java`

### 类型声明
```text
class SetGenderHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ViewAllCharHandler.java`

### 类型声明
```text
class ViewAllCharHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public final void handlePacket(InPacket p, Client c)
private static int countTotalChrs(Map<Integer, List<Character>> worldChrs)
private static void padChrsIfNeeded(SortedMap<Integer, List<Character>> worldChrs)
private static boolean shouldPadLastRow(int totalChrs)
private static List<Character> getLastWorldChrs(SortedMap<Integer, List<Character>> worldChrs)
private static <T> T getLastItem(List<T> list)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ViewAllCharRegisterPicHandler.java`

### 类型声明
```text
class ViewAllCharRegisterPicHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ViewAllCharSelectedHandler.java`

### 类型声明
```text
class ViewAllCharSelectedHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public final void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.handlers.login` / `net/server/handlers/login/ViewAllCharSelectedWithPicHandler.java`

### 类型声明
```text
class ViewAllCharSelectedWithPicHandler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static int parseAntiMulticlientError(AntiMulticlientResult res)
public void handlePacket(InPacket p, Client c)
```

---

## `org.gms.net.server.services` / `net/server/services/BaseScheduler.java`

### 类型声明
```text
class BaseScheduler
```

- 字段候选数: 2
```text
private int idleProcs = 0
private ScheduledFuture<?> schedulerTask = null
```

- 方法/构造器候选数: 10
```text
protected BaseScheduler()
protected BaseScheduler(List<Lock> extLocks)
protected void addListener(SchedulerListener listener)
private void lockScheduler()
private void unlockScheduler()
private void runBaseSchedule()
protected void registerEntry(Object key, Runnable removalAction, long duration)
protected void interruptEntry(Object key)
private void dispatchRemovedEntries(List<Object> toRemove, boolean fromUpdate)
public void dispose()
```

---

## `org.gms.net.server.services` / `net/server/services/BaseService.java`

### 类型声明
```text
class BaseService
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
protected static int getChannelSchedulerIndex(int mapid)
```

---

## `org.gms.net.server.services` / `net/server/services/SchedulerListener.java`

### 类型声明
```text
interface SchedulerListener
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.services` / `net/server/services/Service.java`

### 类型声明
```text
class Service
```

- 字段候选数: 2
```text
private Class<T> cls
private BaseService service
```

- 方法/构造器候选数: 3
```text
public Service(Class<T> s)
public T getService()
public void dispose()
```

---

## `org.gms.net.server.services` / `net/server/services/ServiceType.java`

### 类型声明
```text
interface ServiceType
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.services` / `net/server/services/ServicesManager.java`

### 类型声明
```text
class ServicesManager
```

- 字段候选数: 1
```text
private Service[] services
```

- 方法/构造器候选数: 3
```text
public ServicesManager(ServiceType serviceBundle)
public Service getAccess(ServiceType s)
public void shutdown()
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/EventService.java`

### 类型声明
```text
class EventService
class EventScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public EventService()
public void dispose()
public void registerEventAction(int mapid, Runnable runAction, long delay)
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/MobAnimationService.java`

### 类型声明
```text
class MobAnimationService
class MobAnimationScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public MobAnimationService()
public void dispose()
public boolean registerMobOnAnimationEffect(int mapid, int mobHash, long delay)
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/MobClearSkillService.java`

### 类型声明
```text
class MobClearSkillService
class MobClearSkillScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public MobClearSkillService()
public void dispose()
public void registerMobClearSkillAction(int mapid, Runnable runAction, long delay)
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/MobMistService.java`

### 类型声明
```text
class MobMistService
class MobMistScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public MobMistService()
public void dispose()
public void registerMobMistCancelAction(int mapid, Runnable runAction, long delay)
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/MobStatusService.java`

### 类型声明
```text
class MobStatusService
class MobStatusScheduler
class MobStatusOvertimeEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public MobStatusService()
public void dispose()
public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration)
public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration, Runnable overtimeAction, int overtimeDelay)
public void interruptMobStatus(int mapid, MonsterStatusEffect mse)
```

---

## `org.gms.net.server.services.task.channel` / `net/server/services/task/channel/OverallService.java`

### 类型声明
```text
class OverallService
class OverallScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public OverallService()
public void dispose()
public void registerOverallAction(int mapid, Runnable runAction, long delay)
public void forceRunOverallAction(int mapid, Runnable runAction)
```

---

## `org.gms.net.server.services.task.world` / `net/server/services/task/world/CharacterSaveService.java`

### 类型声明
```text
class CharacterSaveService
class CharacterSaveScheduler
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void dispose()
public void registerSaveCharacter(int characterId, Runnable runAction)
```

---

## `org.gms.net.server.services.type` / `net/server/services/type/ChannelServices.java`

### 类型声明
```text
enum ChannelServices
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
MOB_STATUS(MobStatusService.class),
MOB_ANIMATION(MobAnimationService.class),
MOB_CLEAR_SKILL(MobClearSkillService.class),
MOB_MIST(MobMistService.class),
EVENT(EventService.class),
ChannelServices(Class<? extends BaseService> service)
public Service createService()
public ChannelServices[] enumValues()
```

---

## `org.gms.net.server.services.type` / `net/server/services/type/WorldServices.java`

### 类型声明
```text
enum WorldServices
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
WorldServices(Class<? extends BaseService> service)
public Service createService()
public WorldServices[] enumValues()
```

---

## `org.gms.net.server.task` / `net/server/task/BaseTask.java`

### 类型声明
```text
class BaseTask
```

- 字段候选数: 1
```text
protected World wserv
```

- 方法/构造器候选数: 2
```text
public void run()
public BaseTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/BossLogTask.java`

### 类型声明
```text
class BossLogTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/CharacterAutosaverTask.java`

### 类型声明
```text
class CharacterAutosaverTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public CharacterAutosaverTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/CharacterDiseaseTask.java`

### 类型声明
```text
class CharacterDiseaseTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/CharacterHpDecreaseTask.java`

### 类型声明
```text
class CharacterHpDecreaseTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public CharacterHpDecreaseTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/CouponTask.java`

### 类型声明
```text
class CouponTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/DueyFredrickTask.java`

### 类型声明
```text
class DueyFredrickTask
```

- 字段候选数: 1
```text
private final FredrickProcessor fredrickProcessor
```

- 方法/构造器候选数: 2
```text
public DueyFredrickTask(FredrickProcessor fredrickProcessor)
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/EventRecallCoordinatorTask.java`

### 类型声明
```text
class EventRecallCoordinatorTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/ExtendValueTask.java`

### 类型声明
```text
class ExtendValueTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/FamilyDailyResetTask.java`

### 类型声明
```text
class FamilyDailyResetTask
```

- 字段候选数: 1
```text
private final World world
```

- 方法/构造器候选数: 3
```text
public FamilyDailyResetTask(World world)
public void run()
public static void resetEntitlementUsage(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/FishingTask.java`

### 类型声明
```text
class FishingTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public FishingTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/HiredMerchantTask.java`

### 类型声明
```text
class HiredMerchantTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public HiredMerchantTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/InvitationTask.java`

### 类型声明
```text
class InvitationTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/LoginCoordinatorTask.java`

### 类型声明
```text
class LoginCoordinatorTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/LoginStorageTask.java`

### 类型声明
```text
class LoginStorageTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/MapOwnershipTask.java`

### 类型声明
```text
class MapOwnershipTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public MapOwnershipTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/MountTirednessTask.java`

### 类型声明
```text
class MountTirednessTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public MountTirednessTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/OnlineTimeTask.java`

### 类型声明
```text
class OnlineTimeTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/PartySearchTask.java`

### 类型声明
```text
class PartySearchTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public PartySearchTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/PetFullnessTask.java`

### 类型声明
```text
class PetFullnessTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public PetFullnessTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/RankingCommandTask.java`

### 类型声明
```text
class RankingCommandTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/RankingLoginTask.java`

### 类型声明
```text
class RankingLoginTask
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
private void resetMoveRank(boolean job) throws SQLException
private void updateRanking(int job, int world) throws SQLException
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/RespawnTask.java`

### 类型声明
```text
class RespawnTask
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public void run()
```

---

## `org.gms.net.server.task` / `net/server/task/ServerMessageTask.java`

### 类型声明
```text
class ServerMessageTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public ServerMessageTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/TimedMapObjectTask.java`

### 类型声明
```text
class TimedMapObjectTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public TimedMapObjectTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/TimeoutTask.java`

### 类型声明
```text
class TimeoutTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public TimeoutTask(World world)
```

---

## `org.gms.net.server.task` / `net/server/task/WeddingReservationTask.java`

### 类型声明
```text
class WeddingReservationTask
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public void run()
public WeddingReservationTask(World world)
```

---

## `org.gms.net.server.world` / `net/server/world/Messenger.java`

### 类型声明
```text
class Messenger
```

- 字段候选数: 2
```text
private final int id
private final boolean[] pos = new boolean[3]
```

- 方法/构造器候选数: 7
```text
public Messenger(int id, MessengerCharacter chrfor)
public int getId()
public Collection<MessengerCharacter> getMembers()
public void addMember(MessengerCharacter member, int position)
public void removeMember(MessengerCharacter member)
public int getLowestPosition()
public int getPositionByName(String name)
```

---

## `org.gms.net.server.world` / `net/server/world/MessengerCharacter.java`

### 类型声明
```text
class MessengerCharacter
```

- 字段候选数: 5
```text
private final String name
private final int id
private int position
private final int channel
private final boolean online
```

- 方法/构造器候选数: 9
```text
public MessengerCharacter(Character maplechar, int position)
public int getId()
public int getChannel()
public String getName()
public boolean isOnline()
public int getPosition()
public void setPosition(int position)
public int hashCode()
public boolean equals(Object obj)
```

---

## `org.gms.net.server.world` / `net/server/world/Party.java`

### 类型声明
```text
class Party
```

- 字段候选数: 5
```text
private int id
private Party enemy = null
private int leaderId
private List<PartyCharacter> pqMembers = null
private int nextEntry = 0
```

- 方法/构造器候选数: 25
```text
public Party(int id, PartyCharacter chrfor)
public boolean containsMembers(PartyCharacter member)
public void addMember(PartyCharacter member)
public void removeMember(PartyCharacter member)
public void setLeader(PartyCharacter victim)
public void updateMember(PartyCharacter member)
public PartyCharacter getMemberById(int id)
public Collection<PartyCharacter> getMembers()
public List<PartyCharacter> getPartyMembers()
public List<PartyCharacter> getPartyMembersOnline()
public Collection<PartyCharacter> getEligibleMembers()
public void setEligibleMembers(List<PartyCharacter> eliParty)
public PartyCharacter getLeader()
public List<Integer> getMembersSortedByHistory()
public byte getPartyDoor(int cid)
public void addDoor(Integer owner, Door door)
public void removeDoor(Integer owner)
public void assignNewLeader(Client c)
public int hashCode()
public PartyCharacter getMemberByPos(int pos)
public boolean equals(Object obj)
public static boolean createParty(Character player, boolean silentCheck)
public static boolean joinParty(Character player, int partyid, boolean silentCheck)
public static void leaveParty(Party party, Client c)
public static void expelFromParty(Party party, Client c, int expelCid)
```

---

## `org.gms.net.server.world` / `net/server/world/PartyCharacter.java`

### 类型声明
```text
class PartyCharacter
```

- 字段候选数: 8
```text
private final String name
private int id
private int level
private int jobid
private int mapid
private boolean online
private Job job
private Character character
```

- 方法/构造器候选数: 19
```text
public PartyCharacter(Character maplechar)
public PartyCharacter()
public Character getPlayer()
public Job getJob()
public int getLevel()
public int getChannel()
public void setChannel(int channel)
public boolean isLeader()
public boolean isOnline()
public void setOnline(boolean online)
public int getMapId()
public void setMapId(int mapid)
public String getName()
public int getId()
public int getJobId()
public int getGuildId()
public int hashCode()
public boolean equals(Object obj)
public int getWorld()
```

---

## `org.gms.net.server.world` / `net/server/world/PartyOperation.java`

### 类型声明
```text
enum PartyOperation
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.net.server.world` / `net/server/world/World.java`

### 类型声明
```text
class World
```

- 字段候选数: 29
```text
private final int id
private int flag
private float expRate
private float dropRate
private float bossDropRate
private float mesoRate
private float questRate
private float travelRate
private float fishingRate
private String eventmsg
private final Lock chnRLock
private final Lock chnWLock
private final Lock suggestRLock
private final Lock suggestWLock
private ScheduledFuture<?> srvMessagesSchedule
private ScheduledFuture<?> petsSchedule
private long petUpdate
private ScheduledFuture<?> mountsSchedule
private long mountUpdate
private ScheduledFuture<?> merchantSchedule
private long merchantUpdate
private ScheduledFuture<?> timedMapObjectsSchedule
private ScheduledFuture<?> charactersSchedule
private ScheduledFuture<?> marriagesSchedule
private ScheduledFuture<?> mapOwnershipSchedule
private ScheduledFuture<?> fishingSchedule
private ScheduledFuture<?> partySearchSchedule
private ScheduledFuture<?> timeoutSchedule
private ScheduledFuture<?> hpDecSchedule
```

- 方法/构造器候选数: 141
```text
public World(int world, int flag, String eventmsg, float expRate, float dropRate, float bossDropRate, float mesoRate, float questRate, float travelRate, float fishingRate)
public int getChannelsSize()
public List<Channel> getChannels()
public Channel getChannel(int channel)
public boolean addChannel(Channel channel)
public int removeChannel()
public boolean canUninstall()
public void setFlag(byte b)
public String getEventMessage()
public void setEventMessage(String eventMessage)
public void setExpRate(float exp)
public void setDropRate(float drop)
public void setMesoRate(float meso)
public int getTransportationTime(int travelTime)
public void loadAccountCharactersView(Integer accountId, List<Character> chars)
public void registerAccountCharacterView(Integer accountId, Character chr)
public void unregisterAccountCharacterView(Integer accountId, Integer chrId)
public void clearAccountCharacterView(Integer accountId)
public void loadAccountStorage(Integer accountId)
private void registerAccountStorage(Integer accountId)
public void unregisterAccountStorage(Integer accountId)
public Storage getAccountStorage(Integer accountId)
public List<Character> loadAndGetAllCharactersView()
public List<Character> getAllCharactersView()
public List<Character> getAccountCharactersView(int accountId)
public PlayerStorage getPlayerStorage()
public MatchCheckerCoordinator getMatchCheckerCoordinator()
public PartySearchCoordinator getPartySearchCoordinator()
public void addPlayer(Character chr)
public void removePlayer(Character chr)
public void addFamily(int id, Family f)
public void removeFamily(int id)
public Family getFamily(int id)
public Collection<Family> getFamilies()
public Guild getGuild(GuildCharacter mgc)
public boolean isWorldCapacityFull()
public int getWorldCapacityStatus()
public GuildSummary getGuildSummary(int gid, int wid)
public void updateGuildSummary(int gid, GuildSummary mgs)
public void reloadGuildSummary()
public void setGuildAndRank(List<Integer> cids, int guildid, int rank, int exception)
public void setOfflineGuildStatus(int guildid, int guildrank, int cid)
public void setGuildAndRank(int cid, int guildid, int rank)
public void changeEmblem(int gid, List<Integer> affectedPlayers, GuildSummary mgs)
public void sendPacket(List<Integer> targetIds, Packet packet, int exception)
public boolean isGuildQueued(int guildId)
public void putGuildQueued(int guildId)
public void removeGuildQueued(int guildId)
public boolean isMarriageQueued(int marriageId)
public void putMarriageQueued(int marriageId, boolean cathedral, boolean premium, int groomId, int brideId)
public boolean addMarriageGuest(int marriageId, int playerId)
public void debugMarriageStatus()
private void registerCharacterParty(Integer chrid, Integer partyid)
private void unregisterCharacterPartyInternal(Integer chrid)
private void unregisterCharacterParty(Integer chrid)
public Integer getCharacterPartyid(Integer chrid)
public Party createParty(PartyCharacter chrfor)
public Party getParty(int partyid)
private Party disbandParty(int partyid)
private void updateCharacterParty(Party party, PartyOperation operation, PartyCharacter target, Collection<PartyCharacter> partyMembers)
private void updateParty(Party party, PartyOperation operation, PartyCharacter target)
public void updateParty(int partyid, PartyOperation operation, PartyCharacter target)
public void removeMapPartyMembers(int partyid)
public int find(String name)
public int find(int id)
public void partyChat(Party party, String chattext, String namefrom)
public void buddyChat(int[] recipientCharacterIds, int cidFrom, String nameFrom, String chattext)
public CharacterIdChannelPair[] multiBuddyFind(int charIdFrom, int[] characterIds)
public Messenger getMessenger(int messengerid)
public void leaveMessenger(int messengerid, MessengerCharacter target)
public void messengerInvite(String sender, int messengerid, String target, int fromchannel)
public void addMessengerPlayer(Messenger messenger, String namefrom, int fromchannel, int position)
public void removeMessengerPlayer(Messenger messenger, int position)
public void messengerChat(Messenger messenger, String chattext, String namefrom)
public void declineChat(String sender, Character player)
public void updateMessenger(int messengerid, String namefrom, int fromchannel)
public void updateMessenger(Messenger messenger, String namefrom, int position, int fromchannel)
public void silentLeaveMessenger(int messengerid, MessengerCharacter target)
public void joinMessenger(int messengerid, MessengerCharacter target, String from, int fromchannel)
public void silentJoinMessenger(int messengerid, MessengerCharacter target, int position)
public Messenger createMessenger(MessengerCharacter chrfor)
public boolean isConnected(String charName)
public BuddyAddResult requestBuddyAdd(String addName, int channelFrom, int cidFrom, String nameFrom)
public void buddyChanged(int cid, int cidFrom, String name, int channel, BuddyOperation operation)
public void loggedOff(String name, int characterId, int channel, int[] buddies)
public void loggedOn(String name, int characterId, int channel, int[] buddies)
private void updateBuddies(int characterId, int channel, int[] buddies, boolean offline)
private static Integer getPetKey(Character chr, byte petSlot)
public void addOwlItemSearch(Integer itemid)
public void addCashItemBought(Integer snid)
private List<Integer> getMostSellerOnTab(List<Pair<Integer, Integer>> tabSellers)
public List<List<Integer>> getMostSellerCashItems()
public void registerPetHunger(Character chr, byte petSlot)
public void unregisterPetHunger(Character chr, byte petSlot)
public void runPetSchedule()
public void registerMountHunger(Character chr)
public void unregisterMountHunger(Character chr)
public void runMountSchedule()
public void registerPlayerShop(PlayerShop ps)
public void unregisterPlayerShop(PlayerShop ps)
public List<PlayerShop> getActivePlayerShops()
public PlayerShop getPlayerShop(int ownerid)
public void registerHiredMerchant(HiredMerchant hm)
public void unregisterHiredMerchant(HiredMerchant hm)
public void runHiredMerchantSchedule()
public List<HiredMerchant> getActiveMerchants()
public HiredMerchant getHiredMerchant(int ownerid)
public void registerTimedMapObject(Runnable r, long duration)
public void runTimedMapObjectSchedule()
public void addPlayerHpDecrease(Character chr)
public void removePlayerHpDecrease(Character chr)
public void runPlayerHpDecreaseSchedule()
public void resetDisabledServerMessages()
public boolean registerDisabledServerMessage(int chrid)
public boolean unregisterDisabledServerMessage(int chrid)
public void runDisabledServerMessagesSchedule()
public void setPlayerNpcMapStep(int mapid, int step)
public void setPlayerNpcMapPodiumData(int mapid, int podium)
public void setPlayerNpcMapData(int mapid, int step, int podium)
private static void executePlayerNpcMapDataUpdate(boolean isPodium, Map<Integer, ?> pnpcData, int value, int worldId, int mapId)
private void setPlayerNpcMapData(int mapId, int step, int podium, boolean silent)
public int getPlayerNpcMapStep(int mapid)
public int getPlayerNpcMapPodiumData(int mapid)
public void resetPlayerNpcMapData()
public void setServerMessage(String msg)
public void broadcastPacket(Packet packet)
private void pushRelationshipCouple(Pair<Integer, Pair<Integer, Integer>> couple)
public int getRelationshipId(int playerId)
public int createRelationship(int groomId, int brideId)
private static int addRelationshipToDb(int groomId, int brideId)
public void deleteRelationship(int playerId, int partnerId)
private static void deleteRelationshipFromDb(int playerId)
public void dropMessage(int type, String message)
public boolean registerFisherPlayer(Character chr, int baitLevel)
public int unregisterFisherPlayer(Character chr)
public void runCheckFishingSchedule()
public void runPartySearchUpdateSchedule()
public BaseService getServiceAccess(WorldServices sv)
private void closeWorldServices()
private void clearWorldData()
public final void shutdown()
```

---

## `org.gms.property` / `property/ServiceProperty.java`

### 类型声明
```text
class ServiceProperty
```

- 字段候选数: 6
```text
private String language
private RateLimitProperty rateLimit
private String wanHost
private String lanHost
private String localhost
private int loginPort
```

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/Data.java`

### 类型声明
```text
interface Data
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataDirectoryEntry.java`

### 类型声明
```text
interface DataDirectoryEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataEntity.java`

### 类型声明
```text
interface DataEntity
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataEntry.java`

### 类型声明
```text
interface DataEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataFileEntry.java`

### 类型声明
```text
interface DataFileEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataProvider.java`

### 类型声明
```text
interface DataProvider
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider` / `provider/DataProviderFactory.java`

### 类型声明
```text
class DataProviderFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static DataProvider getWZ(Path in)
public static DataProvider getDataProvider(WZFiles in)
```

---

## `org.gms.provider` / `provider/DataTool.java`

### 类型声明
```text
class DataTool
```

- 字段候选数: 0

- 方法/构造器候选数: 27
```text
public static String getString(Data data)
public static String getString(Data data, String def)
public static String getString(String path, Data data)
public static String getString(String path, Data data, String def)
public static double getDouble(Data data)
public static float getFloat(Data data)
public static int getInt(Data data)
public static int getInt(String path, Data data)
public static int getIntConvert(Data data)
public static int getIntConvert(Data data, int def)
public static int getIntConvert(String path, Data data)
public static int getInt(Data data, int def)
public static int getInt(String path, Data data, int def)
public static int getIntConvert(String path, Data data, int def)
public static Integer getInteger(String path, Data data)
public static int getInteger(String path, Data data, int def)
public static Short getShort(String path, Data data)
public static short getShort(String path, Data data, short def)
public static Long getLong(String path, Data data)
public static long getLong(String path, Data data, long def)
public static Point getPoint(Data data)
public static Point getPoint(String path, Data data)
public static Point getPoint(String path, Data data, Point def)
public static String getFullDataPath(Data data)
public static String getAttributeValue(Data data,String name)
public static String getAttributeValue(Data data,String name,String def)
public static int getAttributeValueInt(Data data,String name,int def)
```

---

## `org.gms.provider.wz` / `provider/wz/DataType.java`

### 类型声明
```text
enum DataType
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.provider.wz` / `provider/wz/WZDirectoryEntry.java`

### 类型声明
```text
class WZDirectoryEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 7
```text
public WZDirectoryEntry(String name, int size, int checksum, DataEntity parent)
public WZDirectoryEntry()
public void addDirectory(DataDirectoryEntry dir)
public void addFile(DataFileEntry fileEntry)
public List<DataDirectoryEntry> getSubdirectories()
public List<DataFileEntry> getFiles()
public DataEntry getEntry(String name)
```

---

## `org.gms.provider.wz` / `provider/wz/WZEntry.java`

### 类型声明
```text
class WZEntry
```

- 字段候选数: 5
```text
private final String name
private final int size
private final int checksum
private int offset
private final DataEntity parent
```

- 方法/构造器候选数: 6
```text
public WZEntry(String name, int size, int checksum, DataEntity parent)
public String getName()
public int getSize()
public int getChecksum()
public int getOffset()
public DataEntity getParent()
```

---

## `org.gms.provider.wz` / `provider/wz/WZFileEntry.java`

### 类型声明
```text
class WZFileEntry
```

- 字段候选数: 1
```text
private int offset
```

- 方法/构造器候选数: 3
```text
public WZFileEntry(String name, int size, int checksum, DataEntity parent)
public int getOffset()
public void setOffset(int offset)
```

---

## `org.gms.provider.wz` / `provider/wz/WZFiles.java`

### 类型声明
```text
enum WZFiles
```

- 字段候选数: 2
```text
private final String fileName
public static final String DIRECTORY = "wz"
```

- 方法/构造器候选数: 15
```text
QUEST("Quest"),
ETC("Etc"),
ITEM("Item"),
CHARACTER("Character"),
STRING("String"),
LIST("List"),
MOB("Mob"),
MAP("Map"),
NPC("Npc"),
REACTOR("Reactor"),
SKILL("Skill"),
SOUND("Sound"),
WZFiles(String name)
public Path getFile()
public String getFilePath()
```

---

## `org.gms.provider.wz` / `provider/wz/XMLDomMapleData.java`

### 类型声明
```text
class XMLDomMapleData
```

- 字段候选数: 2
```text
private final Node node
private Path imageDataDir
```

- 方法/构造器候选数: 10
```text
public XMLDomMapleData(FileInputStream fis, Path imageDataDir)
private XMLDomMapleData(Node node)
public synchronized Data getChildByPath(String path)
public synchronized List<Data> getChildren()
public synchronized Object getData()
public synchronized DataType getType()
public synchronized DataEntity getParent()
public synchronized String getName()
public synchronized Iterator<Data> iterator()
public synchronized String getAttributeValue(String name)
```

---

## `org.gms.provider.wz` / `provider/wz/XMLWZFile.java`

### 类型声明
```text
class XMLWZFile
```

- 字段候选数: 2
```text
private final Path root
private final WZDirectoryEntry rootForNavigation
```

- 方法/构造器候选数: 4
```text
public XMLWZFile(Path fileIn)
private void fillMapleDataEntitys(Path lroot, WZDirectoryEntry wzdir)
public synchronized Data getData(String path)
public DataDirectoryEntry getRoot()
```

---

## `org.gms.scripting` / `scripting/AbstractPlayerInteraction.java`

### 类型声明
```text
class AbstractPlayerInteraction
```

- 字段候选数: 1
```text
public Client c
```

- 方法/构造器候选数: 178
```text
public AbstractPlayerInteraction(Client c)
public Client getClient()
public Character getPlayer()
public Character getChar()
public int getJobId()
public Job getJob()
public int getLevel()
public MapleMap getMap()
public int getHourOfDay()
public int getMarketPortalId(int mapId)
private int getMarketPortalId(MapleMap map)
public void warp(int mapid)
public void warp(int map, int portal)
public void warp(int map, String portal)
public void warpMap(int map)
public void warpParty(int id)
public void warpParty(int id, int portalId)
public void warpParty(int map, String portalName)
public void warpParty(int id, int fromMinId, int fromMaxId)
public void warpParty(int id, int portalId, int fromMinId, int fromMaxId)
public MapleMap getWarpMap(int map)
public MapleMap getMap(int map)
public int countAllMonstersOnMap(int map)
public int countMonster()
public void resetMapObjects(int mapid)
public EventManager getEventManager(String event)
public EventInstanceManager getEventInstance()
public Inventory getInventory(int type)
public Inventory getInventory(InventoryType type)
public boolean hasItem(int itemid)
public boolean hasItem(int itemid, int quantity)
public boolean haveItem(int itemid)
public boolean haveItem(int itemid, int quantity)
public int getItemQuantity(int itemid)
public boolean haveItemWithId(int itemid)
public boolean haveItemWithId(int itemid, boolean checkEquipped)
public boolean canHold(int itemid)
public boolean canHold(int itemid, int quantity)
public boolean canHold(int itemid, int quantity, int removeItemid, int removeQuantity)
private List<Integer> convertToIntegerList(List<Object> objects)
public boolean canHoldAll(List<Object> itemids)
public boolean canHoldAll(List<Object> itemids, List<Object> quantity)
private boolean canHoldAll(List<Integer> itemids, List<Integer> quantity, boolean isInteger)
public boolean canHoldAllAfterRemoving(List<Integer> toAddItemids, List<Integer> toAddQuantity, List<Integer> toRemoveItemids, List<Integer> toRemoveQuantity)
public final QuestStatus getQuestRecord(final int id)
public final QuestStatus getQuestNoRecord(final int id)
public void openNpc(int npcid)
public void openNpc(int npcid, String script)
public int getQuestStatus(int id)
private QuestStatus.Status getQuestStat(int id)
public boolean isQuestCompleted(int id)
public boolean isQuestActive(int id)
public boolean isQuestStarted(int id)
public void setQuestProgress(int id, String progress)
public void setQuestProgress(int id, int progress)
public void setQuestProgress(int id, int infoNumber, int progress)
public void setQuestProgress(int id, int infoNumber, String progress)
public String getQuestProgress(int id)
public String getQuestProgress(int id, int infoNumber)
public int getQuestProgressInt(int id)
public int getQuestProgressInt(int id, int infoNumber)
public void resetAllQuestProgress(int id)
public void resetQuestProgress(int id, int infoNumber)
public boolean forceStartQuest(int id)
public boolean forceStartQuest(int id, int npc)
public boolean forceCompleteQuest(int id)
public boolean forceCompleteQuest(int id, int npc)
public boolean startQuest(short id)
public boolean completeQuest(short id)
public boolean startQuest(int id)
public boolean completeQuest(int id)
public boolean startQuest(short id, int npc)
public boolean completeQuest(short id, int npc)
public boolean startQuest(int id, int npc)
public boolean completeQuest(int id, int npc)
public Item evolvePet(byte slot, int afterId)
public void gainItem(int id, short quantity)
public void gainItem(int id, short quantity, boolean show)
public void gainItem(int id, boolean show)
public void gainItem(int id)
public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage)
public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage, long expires)
public Item gainItem(int id, short quantity, boolean randomStats, boolean showMessage, long expires, Pet from)
public void gainFame(int delta)
public void changeMusic(String songName)
public void playerMessage(int type, String message)
public void message(String message)
public void dropMessage(int type, String message)
public void mapMessage(int type, String message)
public void mapEffect(String path)
public void mapSound(String path)
public void displayAranIntro()
public void showIntro(String path)
public void showInfo(String path)
public void guildMessage(int type, String message)
public Guild getGuild()
public Party getParty()
public boolean isLeader()
public boolean isGuildLeader()
public boolean isPartyLeader()
public boolean isEventLeader()
public void givePartyItems(int id, short quantity, List<Character> party)
public void removeHPQItems()
public void removePartyItems(int id)
public void giveCharacterExp(int amount, Character chr)
public void givePartyExp(int amount, List<Character> party)
public void givePartyExp(String PQ)
public void givePartyExp(String PQ, boolean instance)
public void removeFromParty(int id, List<Character> party)
public void removeAll(int id)
public void removeAll(int id, Client cl)
public void removeAllByInventory(int invType)
public void removeAllByInventorySlot(int invType, short slot)
public int getMapId()
public int getPlayerCount(int mapid)
public void showInstruction(String msg, int width, int height)
public void disableMinimap()
public boolean isAllReactorState(final int reactorId, final int state)
public void resetMap(int mapid)
public void useItem(int id)
public void cancelItem(final int id)
public void teachSkill(int skillid, byte level, byte masterLevel, long expiration)
public void teachSkill(int skillid, byte level, byte masterLevel, long expiration, boolean force)
public void removeEquipFromSlot(short slot)
public void gainAndEquip(int itemid, short slot)
public void spawnNpc(int npcId, Point pos, MapleMap map)
public void spawnMonster(int id, int x, int y)
public Monster getMonsterLifeFactory(int mid)
public void spawnGuide()
public void removeGuide()
public void displayGuide(int num)
public void goDojoUp()
public void resetDojoEnergy()
public void resetPartyDojoEnergy()
public void enableActions()
public void showEffect(String effect)
public void dojoEnergy()
public void talkGuide(String message)
public void guideHint(int hint)
public void updateAreaInfo(Short area, String info)
public boolean containsAreaInfo(short area, String info)
public void earnTitle(String msg)
public void showInfoText(String msg)
public void openUI(byte ui)
public void lockUI()
public void unlockUI()
public void playSound(String sound)
public void environmentChange(String env, int mode)
public String numberWithCommas(int number)
public Pyramid getPyramid()
public int createExpedition(ExpeditionType type)
public int createExpedition(ExpeditionType type, boolean silent, int minPlayers, int maxPlayers)
public void endExpedition(Expedition exped)
public Expedition getExpedition(ExpeditionType type)
public String getExpeditionMemberNames(ExpeditionType type)
public boolean isLeaderExpedition(ExpeditionType type)
public long getJailTimeLeft()
public List<Pet> getDriedPets()
public List<Item> getUnclaimedMarriageGifts()
public boolean startDungeonInstance(int dungeonid)
public boolean canGetFirstJob(int jobType)
public String getFirstJobStatRequirement(int jobType)
public void npcTalk(int npcid, String message)
public long getCurrentTime()
public void weakenAreaBoss(int monsterId, String message)
private void applySealSkill(Monster monster)
private void applyReduceAvoid(Monster monster)
private void sendBlueNotice(MapleMap map, String message)
public String getCharacterExtendValue(String extendName)
public String getCharacterExtendValue(String extendName, boolean isDaily)
public String getAccountExtendValue(String extendName)
public String getAccountExtendValue(String extendName, boolean isDaily)
public void saveOrUpdateCharacterExtendValue(String extendName, String extendValue)
public void saveOrUpdateCharacterExtendValue(String extendName, String extendValue, boolean isDaily)
public void saveOrUpdateAccountExtendValue(String extendName, String extendValue)
public void saveOrUpdateAccountExtendValue(String extendName, String extendValue, boolean isDaily)
public void gainEquip(Equip equip)
public int getOnlineTime()
```

---

## `org.gms.scripting` / `scripting/AbstractScriptManager.java`

### 类型声明
```text
class AbstractScriptManager
```

- 字段候选数: 1
```text
private final ScriptEngineFactory sef
```

- 方法/构造器候选数: 5
```text
protected AbstractScriptManager()
protected ScriptEngine getInvocableScriptEngine(String path)
protected ScriptEngine getInvocableScriptEngine(String path, Client c)
private void enableScriptHostAccess(GraalJSScriptEngine engine)
protected void resetContext(String path, Client c)
```

---

## `org.gms.scripting` / `scripting/SynchronizedInvocable.java`

### 类型声明
```text
class SynchronizedInvocable
```

- 字段候选数: 1
```text
private final Invocable invocable
```

- 方法/构造器候选数: 6
```text
private SynchronizedInvocable(Invocable invocable)
public static Invocable of(Invocable invocable)
public synchronized Object invokeMethod(Object thiz, String name, Object... args) throws ScriptException, NoSuchMethodException
public synchronized Object invokeFunction(String name, Object... args) throws ScriptException, NoSuchMethodException
public synchronized <T> T getInterface(Class<T> clasz)
public synchronized <T> T getInterface(Object thiz, Class<T> clasz)
```

---

## `org.gms.scripting.event` / `scripting/event/EventInstanceManager.java`

### 类型声明
```text
class EventInstanceManager
```

- 字段候选数: 3
```text
private Expedition expedition = null
private final Lock readLock
private final Lock writeLock
```

- 方法/构造器候选数: 125
```text
public EventInstanceManager(EventManager em, String name)
public void setName(String name)
public EventManager getEm()
public int getEventPlayersJobs()
public void applyEventPlayersItemBuff(int itemId)
public void applyEventPlayersSkillBuff(int skillId)
public void applyEventPlayersSkillBuff(int skillId, int skillLv)
public void giveEventPlayersExp(int gain)
public void giveEventPlayersExp(int gain, int mapId)
public void giveEventPlayersMeso(int gain)
public void giveEventPlayersMeso(int gain, int mapId)
public Object invokeScriptFunction(String name, Object... args) throws ScriptException, NoSuchMethodException
public synchronized void registerPlayer(final Character chr)
public synchronized void registerPlayer(final Character chr, boolean runEntryScript)
public void exitPlayer(final Character chr)
public void dropMessage(int type, String message)
public void restartEventTimer(long time)
public void startEventTimer(long time)
public void addEventTimer(long time)
private void dismissEventTimer()
public void stopEventTimer()
public boolean isTimerStarted()
public long getTimeLeft()
public void registerParty(Character chr)
public void registerParty(Party party, MapleMap map)
public void registerExpedition(Expedition exped)
private void registerExpeditionTeam(Expedition exped, int recruitMap)
public void unregisterPlayer(final Character chr)
public int getPlayerCount()
public Character getPlayerById(int id)
public List<Character> getPlayers()
private List<Character> getPlayerList()
public void registerMonster(Monster mob)
public void movePlayer(final Character chr)
public void changedMap(final Character chr, final int mapId)
public void afterChangedMap(final Character chr, final int mapId)
public synchronized void changedLeader(final PartyCharacter ldr)
public void monsterKilled(final Monster mob, final boolean hasKiller)
public void friendlyKilled(final Monster mob, final boolean hasKiller)
public void friendlyDamaged(final Monster mob)
public void friendlyItemDrop(final Monster mob)
public void playerKilled(final Character chr)
public void reviveMonster(final Monster mob)
public boolean revivePlayer(final Character chr)
public void playerDisconnected(final Character chr)
public void monsterKilled(Character chr, final Monster mob)
public int getKillCount(Character chr)
public void dispose()
public synchronized void dispose(boolean shutdown)
public MapManager getMapFactory()
public void schedule(final String methodName, long delay)
public String getName()
public MapleMap getMapInstance(int mapId)
public void setIntProperty(String key, Integer value)
public void setProperty(String key, Integer value)
public void setProperty(String key, String value)
public Object setProperty(String key, String value, boolean prev)
public void setObjectProperty(String key, Object obj)
public String getProperty(String key)
public int getIntProperty(String key)
public Object getObjectProperty(String key)
public void leftParty(final Character chr)
public void disbandParty()
public void clearPQ()
public void removePlayer(final Character chr)
public boolean isLeader(Character chr)
public boolean isEventLeader(Character chr)
public final MapleMap getInstanceMap(final int mapid)
public final boolean disposeIfPlayerBelow(final byte size, final int towarp)
public void spawnNpc(int npcId, Point pos, MapleMap map)
public void dispatchRaiseQuestMobCount(int mobid, int mapid)
public Monster getMonster(int mid)
private List<Integer> convertToIntegerList(List<Object> objects)
public void setEventClearStageExp(List<Object> gain)
public void setEventClearStageMeso(List<Object> gain)
public Integer getClearStageExp(int stage)
public Integer getClearStageMeso(int stage)
public List<Integer> getClearStageBonus(int stage)
private void dropExclusiveItems(Character chr)
public void dropAllExclusiveItems()
public final void setExclusiveItems(List<Object> items)
public final void setEventRewards(List<Object> rwds, List<Object> qtys, int expGiven)
public final void setEventRewards(List<Object> rwds, List<Object> qtys)
public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys)
public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys, int expGiven)
private byte getRewardListRequirements(int level)
private boolean hasRewardSlot(Character player, int eventLevel)
public final boolean giveEventReward(Character player)
public final boolean giveEventReward(Character player, int eventLevel)
private void disposeExpedition()
public final synchronized void startEvent()
public final void setEventCleared()
public final boolean isEventCleared()
public final boolean isEventDisposed()
private boolean isEventTeamLeaderOn()
public final boolean checkEventTeamLacking(boolean leavingEventMap, int minPlayers)
public final boolean isExpeditionTeamLackingNow(boolean leavingEventMap, int minPlayers, Character quitter)
public final boolean isEventTeamLackingNow(boolean leavingEventMap, int minPlayers, Character quitter)
public final boolean isEventTeamTogether()
public final void warpEventTeam(int warpFrom, int warpTo)
public final void warpEventTeam(int warpTo)
public final void warpEventTeamToMapSpawnPoint(int warpFrom, int warpTo, int toSp)
public final void warpEventTeamToMapSpawnPoint(int warpTo, int toSp)
public final int getLeaderId()
public Character getLeader()
public final void setLeader(Character chr)
public final void showWrongEffect()
public final void showWrongEffect(int mapId)
public final void showClearEffect()
public final void showClearEffect(boolean hasGate)
public final void showClearEffect(int mapId)
public final void showClearEffect(boolean hasGate, int mapId)
public final void showClearEffect(int mapId, String mapObj, int newState)
public final void showClearEffect(boolean hasGate, int mapId, String mapObj, int newState)
public final void recoverOpenedGate(Character chr, int thisMapId)
public final void giveEventPlayersStageReward(int thisStage)
public final void linkToNextStage(int thisStage, String eventFamily, int thisMapId)
public final void linkPortalToScript(int thisStage, String portalName, String scriptName, int thisMapId)
public final void gridInsert(Character chr, int newStatus)
public final void gridRemove(Character chr)
public final int gridCheck(Character chr)
public final int gridSize()
public final void gridClear()
public boolean activatedAllReactorsOnMap(int mapId, int minReactorId, int maxReactorId)
public boolean activatedAllReactorsOnMap(MapleMap map, int minReactorId, int maxReactorId)
```

---

## `org.gms.scripting.event` / `scripting/event/EventManager.java`

### 类型声明
```text
class EventManager
class EventManagerTask
```

- 字段候选数: 0

- 方法/构造器候选数: 66
```text
public EventManager(Channel cserv, Invocable iv, String name)
private boolean isDisposed()
public void cancel()
private List<Integer> convertToIntegerList(List<Object> objects)
public long getLobbyDelay()
private int getMaxLobbies()
public EventScheduledFuture schedule(String methodName, long delay)
public EventScheduledFuture schedule(final String methodName, final EventInstanceManager eim, long delay)
public EventScheduledFuture scheduleAtTimestamp(final String methodName, long timestamp)
public World getWorldServer()
public Channel getChannelServer()
public Invocable getIv()
public EventInstanceManager getInstance(String name)
public Collection<EventInstanceManager> getInstances()
public EventInstanceManager newInstance(String name) throws EventInstanceInProgressException
public Marriage newMarriage(String name) throws EventInstanceInProgressException
public void disposeInstance(final String name)
public void setProperty(String key, String value)
public void setIntProperty(String key, int value)
public void setProperty(String key, int value)
public String getProperty(String key)
public int getIntProperty(String key)
private void setLockLobby(int lobbyId, boolean lock)
private boolean startLobbyInstance(int lobbyId)
private void freeLobbyInstance(String lobbyName)
public String getName()
private int availableLobbyInstance()
private String getInternalScriptExceptionMessage(Throwable a)
private EventInstanceManager createInstance(String name, Object... args) throws ScriptException, NoSuchMethodException
private void registerEventInstance(String eventName, int lobbyId)
public boolean startInstance(Expedition exped)
public boolean startInstance(int lobbyId, Expedition exped)
public boolean startInstance(int lobbyId, Expedition exped, Character leader)
public boolean startInstance(Character chr)
public boolean startInstance(int lobbyId, Character leader)
public boolean startInstance(int lobbyId, Character chr, Character leader, int difficulty)
public boolean startInstance(Party party, MapleMap map)
public boolean startInstance(int lobbyId, Party party, MapleMap map)
public boolean startInstance(int lobbyId, Party party, MapleMap map, Character leader)
public boolean startInstance(Party party, MapleMap map, int difficulty)
public boolean startInstance(int lobbyId, Party party, MapleMap map, int difficulty)
public boolean startInstance(int lobbyId, Party party, MapleMap map, int difficulty, Character leader)
public boolean startInstance(EventInstanceManager eim, String ldr)
public boolean startInstance(EventInstanceManager eim, Character ldr)
public boolean startInstance(int lobbyId, EventInstanceManager eim, String ldr)
public boolean startInstance(int lobbyId, EventInstanceManager eim, String ldr, Character leader)
public List<PartyCharacter> getEligibleParty(Party party)
public void clearPQ(EventInstanceManager eim)
public void clearPQ(EventInstanceManager eim, MapleMap toMap)
public long getEventTimeout()
public boolean isNobodyInPQ()
public Monster getMonster(int mid)
private void exportReadyGuild(Integer guildId)
private void exportMovedQueueToGuild(Integer guildId, int place)
private List<Integer> getNextGuildQueue()
public boolean isQueueFull()
public int getQueueSize()
public byte addGuildToQueue(Integer guildId, Integer leaderId)
public boolean attemptStartGuildInstance()
public void startQuest(Character chr, int id, int npcid)
public void completeQuest(Character chr, int id, int npcid)
public int getTransportationTime(int travelTime)
public int getBossTime(int BossTime)
private void fillEimQueue()
private EventInstanceManager getReadyInstance()
private void instantiateQueuedInstance()
```

---

## `org.gms.scripting.event` / `scripting/event/EventScheduledFuture.java`

### 类型声明
```text
class EventScheduledFuture
```

- 字段候选数: 2
```text
Runnable r
EventScriptScheduler ess
```

- 方法/构造器候选数: 2
```text
public EventScheduledFuture(Runnable r, EventScriptScheduler ess)
public void cancel(boolean dummy)
```

---

## `org.gms.scripting.event` / `scripting/event/EventScriptManager.java`

### 类型声明
```text
class EventScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 9
```text
public EventScriptManager(final Channel channel, String[] scripts)
public EventManager getEventManager(String event)
public boolean isActive()
public final void init()
private void reloadScripts()
private EventEntry initializeEventEntry(String script, Channel channel)
public void reload()
public void cancel()
public void dispose()
```

---

## `org.gms.scripting.event.scheduler` / `scripting/event/scheduler/EventScriptScheduler.java`

### 类型声明
```text
class EventScriptScheduler
```

- 字段候选数: 3
```text
private boolean disposed = false
private int idleProcs = 0
private ScheduledFuture<?> schedulerTask = null
```

- 方法/构造器候选数: 4
```text
private void runBaseSchedule()
public void registerEntry(final Runnable scheduledAction, final long duration)
public void cancelEntry(final Runnable scheduledAction)
public void dispose()
```

---

## `org.gms.scripting.item` / `scripting/item/ItemScriptManager.java`

### 类型声明
```text
class ItemScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static ItemScriptManager getInstance()
public void runItemScript(Client c, ScriptedItem scriptItem)
```

---

## `org.gms.scripting.item` / `scripting/item/ItemScriptMethods.java`

### 类型声明
```text
class ItemScriptMethods
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public ItemScriptMethods(Client c)
```

---

## `org.gms.scripting.map` / `scripting/map/MapScriptManager.java`

### 类型声明
```text
class MapScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public static MapScriptManager getInstance()
public void reloadScripts()
public boolean runMapScript(Client c, String mapScriptPath, boolean firstUser)
```

---

## `org.gms.scripting.map` / `scripting/map/MapScriptMethods.java`

### 类型声明
```text
class MapScriptMethods
```

- 字段候选数: 1
```text
private final String rewardstring = " 勋章挑战已完成！请找勋章老人领取你的勋章。"
```

- 方法/构造器候选数: 8
```text
public MapScriptMethods(Client c)
public void displayCygnusIntro()
public void displayAranIntro()
public void startExplorerExperience()
public void goAdventure()
public void goLith()
public void explorerQuest(short questid, String questName)
public void touchTheSky()
```

---

## `org.gms.scripting.npc` / `scripting/npc/NPCConversationManager.java`

### 类型声明
```text
class NPCConversationManager
```

- 字段候选数: 6
```text
private final int npc
private int npcOid
private String scriptName
private String getText
private boolean itemScript
private List<PartyCharacter> otherParty
```

- 方法/构造器候选数: 135
```text
private String getDefaultTalk(int npcid)
public NPCConversationManager(Client c, int npc, String scriptName)
public NPCConversationManager(Client c, int npc, List<PartyCharacter> otherParty, boolean test)
public NPCConversationManager(Client c, int npc, int oid, String scriptName, boolean itemScript)
public int getNpc()
public int getNpcObjectId()
public String getScriptName()
public boolean isItemScript()
public void resetItemScript()
public void dispose()
public void sendNext(String text)
public void sendPrev(String text)
public void sendNextPrev(String text)
public void sendOk(String text)
public void sendDefault()
public void sendYesNo(String text)
public void sendAcceptDecline(String text)
public void sendSimple(String text)
public void sendNext(String text, byte speaker)
public void sendPrev(String text, byte speaker)
public void sendNextPrev(String text, byte speaker)
public void sendOk(String text, byte speaker)
public void sendYesNo(String text, byte speaker)
public void sendAcceptDecline(String text, byte speaker)
public void sendSimple(String text, byte speaker)
public void sendStyle(String text, int[] styles)
public void sendGetNumber(String text, int def, int min, int max)
public void sendGetText(String text)
public void sendGetNumber(String text, int def, int min, int max,byte speaker)
public void sendGetText(String text,byte speaker)
public void sendDimensionalMirror(String text)
public void setGetText(String text)
public String getText()
public boolean forceStartQuest(int id)
public boolean forceCompleteQuest(int id)
public boolean startQuest(short id)
public boolean completeQuest(short id)
public boolean startQuest(int id)
public boolean completeQuest(int id)
public int getMeso()
public void gainMeso(int gain)
public void gainMeso(Double gain)
public void gainExp(int gain)
public void showEffect(String effect)
public void setHair(int hair)
public void setFace(int face)
public void setSkin(int color)
public int itemQuantity(int itemid)
public void displayGuildRanks()
public boolean canSpawnPlayerNpc(int mapid)
public PlayerNPC getPlayerNPCByScriptid(int scriptId)
public Party getParty()
public void resetMap(int mapid)
public void gainTameness(int tameness)
public String getName()
public int getGender()
public void changeJobById(int a)
public void changeJob(Job job)
public String getJobName(int id)
public StatEffect getItemEffect(int itemId)
public void resetStats()
public void openShopNPC(int id)
public void maxMastery()
public void doGachapon()
public void upgradeAlliance()
public void disbandAlliance(Client c, int allianceId)
public boolean canBeUsedAllianceName(String name)
public Alliance createAlliance(String name)
public int getAllianceCapacity()
public boolean hasMerchant()
public boolean hasMerchantItems()
public void showFredrick()
public int partyMembersInMap()
public Event getEvent()
public void divideTeams()
public Character getMapleCharacter(String player)
public void logLeaf(String prize)
public boolean createPyramid(String mode, boolean party)
public boolean itemExists(int itemid)
public int getCosmeticItem(int itemid)
private int getEquippedCosmeticid(int itemid)
public boolean isCosmeticEquipped(int itemid)
public boolean isUsingOldPqNpcStyle()
public Object[] getAvailableMasteryBooks()
public Object[] getAvailableSkillBooks()
public Object[] getNamesWhoDropsItem(Integer itemId)
public String getSkillBookInfo(int itemid)
public int cpqCalcAvgLvl(int map)
public boolean sendCPQMapLists()
public boolean fieldTaken(int field)
public boolean fieldLobbied(int field)
public void cpqLobby(int field)
public Character getChrById(int id)
public void cancelCPQLobby()
private void warpoutCPQLobby(MapleMap lobbyMap)
private int isCPQParty(MapleMap lobby, Party party)
private int canStartCPQ(MapleMap lobby, Party party, Party challenger)
public void startCPQ(final Character challenger, final int field)
public void startCPQ2(final Character challenger, final int field)
public boolean sendCPQMapLists2()
public boolean fieldTaken2(int field)
public boolean fieldLobbied2(int field)
public void cpqLobby2(int field)
public void mapClock(int time)
private boolean sendCPQChallenge(String cpqType, int leaderid)
public void answerCPQChallenge(boolean accept)
public void challengeParty2(int field)
public void challengeParty(int field)
private synchronized boolean setupAriantBattle(Expedition exped, int mapid)
public String startAriantBattle(ExpeditionType expedType, int mapid)
public void sendMarriageWishlist(boolean groom)
public void sendMarriageGifts(List<Item> gifts)
public boolean createMarriageWishlist()
public void sendNextLevel(String nextLevel, String text)
public void sendLastLevel(String lastLevel, String text)
public void sendLastNextLevel(String lastLevel, String nextLevel, String text)
public void sendOkLevel(String nextLevel, String text)
public void sendSelectLevel(String text)
public void sendSelectLevel(String prefix, String text)
public void sendNextSelectLevel(String nextLevel, String text)
public void getInputNumberLevel(String nextLevel, String text, int def, int min, int max)
public void getInputTextLevel(String nextLevel, String text)
public void sendAcceptDeclineLevel(String decLineLevel, String acceptLevel, String text)
public void sendYesNoLevel(String noLevel, String yesLevel, String text)
public void sendNextLevel(String nextLevel, String text, byte speaker)
public void sendLastLevel(String lastLevel, String text, byte speaker)
public void sendLastNextLevel(String lastLevel, String nextLevel, String text, byte speaker)
public void sendOkLevel(String nextLevel, String text, byte speaker)
public void sendSelectLevel(String text, byte speaker)
public void sendSelectLevel(String prefix, String text, byte speaker)
public void sendNextSelectLevel(String nextLevel, String text, byte speaker)
public void getPnpcInputNumberLevel(String nextLevel, String text, int def, int min, int max, byte speaker)
public void getPnpcInputTextLevel(String nextLevel, String text, byte speaker)
public void sendAcceptDeclineLevel(String decLineLevel, String acceptLevel, String text, byte speaker)
public void sendYesNoLevel(String noLevel, String yesLevel, String text, byte speaker)
```

---

## `org.gms.scripting.npc` / `scripting/npc/NPCScriptManager.java`

### 类型声明
```text
class NPCScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 15
```text
public static NPCScriptManager getInstance()
public boolean isNpcScriptAvailable(Client c, String fileName)
public boolean start(Client c, int npc, Character chr)
public boolean start(Client c, int npc, int oid, Character chr)
public boolean start(Client c, int npc, String fileName, Character chr)
public boolean start(Client c, int npc, int oid, String fileName, Character chr)
public boolean start(Client c, ScriptedItem scriptItem, Character chr)
public void start(String filename, Client c, int npc, List<PartyCharacter> chrs)
private boolean start(Client c, int npc, int oid, String fileName, Character chr, boolean itemScript, String engineName)
public void action(Client c, byte mode, byte type, int selection)
public void nextLevel(Client c, byte mode, byte type, int selection)
public void dispose(NPCConversationManager cm)
public void dispose(Client c)
public void dispose(Client c, boolean action)
public NPCConversationManager getCM(Client c)
```

---

## `org.gms.scripting.portal` / `scripting/portal/PortalPlayerInteraction.java`

### 类型声明
```text
class PortalPlayerInteraction
```

- 字段候选数: 1
```text
private final Portal portal
```

- 方法/构造器候选数: 7
```text
public PortalPlayerInteraction(Client c, Portal portal)
public Portal getPortal()
public void runMapScript()
public boolean hasLevel30Character()
public void blockPortal()
public void unblockPortal()
public void playPortalSound()
```

---

## `org.gms.scripting.portal` / `scripting/portal/PortalScript.java`

### 类型声明
```text
interface PortalScript
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.scripting.portal` / `scripting/portal/PortalScriptManager.java`

### 类型声明
```text
class PortalScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static PortalScriptManager getInstance()
private PortalScript getPortalScript(String scriptName) throws ScriptException
public boolean executePortalScript(Portal portal, Client c)
public void reloadPortalScripts()
```

---

## `org.gms.scripting.quest` / `scripting/quest/QuestActionManager.java`

### 类型声明
```text
class QuestActionManager
```

- 字段候选数: 1
```text
private final int quest
```

- 方法/构造器候选数: 11
```text
public QuestActionManager(Client c, int quest, int npc, boolean start)
public int getQuest()
public boolean isStart()
public void dispose()
public boolean forceStartQuest()
public boolean forceCompleteQuest()
public void startQuest()
public void completeQuest()
public void gainExp(int gain)
public void gainMeso(int gain)
public String getMedalName()
```

---

## `org.gms.scripting.quest` / `scripting/quest/QuestScriptManager.java`

### 类型声明
```text
class QuestScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 12
```text
public static QuestScriptManager getInstance()
private ScriptEngine getQuestScriptEngine(Client c, short questid)
public void start(Client c, short questid, int npc)
public void start(Client c, byte mode, byte type, int selection)
public void end(Client c, short questid, int npc)
public void end(Client c, byte mode, byte type, int selection)
public void raiseOpen(Client c, short questid, int npc)
public void dispose(QuestActionManager qm, Client c)
public void dispose(Client c)
public QuestActionManager getQM(Client c)
public void reloadQuestScripts()
public boolean checkFunctionExists(Client c, short questid, int npc, String functionName)
```

---

## `org.gms.scripting.reactor` / `scripting/reactor/ReactorActionManager.java`

### 类型声明
```text
class ReactorActionManager
```

- 字段候选数: 3
```text
private final Reactor reactor
private final Invocable iv
private ScheduledFuture<?> sprayTask = null
```

- 方法/构造器候选数: 31
```text
public ReactorActionManager(Client c, Reactor reactor, Invocable iv)
public void hitReactor()
public void destroyNpc(int npcId)
private static void sortDropEntries(List<ReactorDropEntry> from, List<ReactorDropEntry> item, List<ReactorDropEntry> visibleQuest, List<ReactorDropEntry> otherQuest, Character chr)
private static List<ReactorDropEntry> assembleReactorDropEntries(Character chr, List<ReactorDropEntry> items)
public void sprayItems()
public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso)
public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void sprayItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems()
public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso)
public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems(boolean delayed, int posX, int posY, boolean meso, int mesoChance, final int minMeso, final int maxMeso, int minItems)
private List<ReactorDropEntry> getDropChances()
private List<ReactorDropEntry> generateDropList(List<ReactorDropEntry> drops, float dropRate, boolean meso, int mesoChance, int minItems)
public void spawnMonster(int id)
public void createMapMonitor(int mapId, String portal)
public void spawnMonster(int id, int qty)
public void spawnMonster(int id, int qty, int x, int y)
public void spawnMonster(int id, int qty, Point pos)
public void killMonster(int id)
public void killMonster(int id, boolean withDrops)
public Point getPosition()
public void spawnNpc(int npcId)
public void spawnNpc(int npcId, Point pos)
public Reactor getReactor()
public void spawnFakeMonster(int id)
public void summonBossDelayed(final int mobId, final int delayMs, final int x, final int y, final String bgm, final String summonMessage)
private void summonBoss(int mobId, int x, int y, String bgmName, String summonMessage)
public void dispelAllMonsters(int num, int team)
```

---

## `org.gms.scripting.reactor` / `scripting/reactor/ReactorScriptManager.java`

### 类型声明
```text
class ReactorScriptManager
```

- 字段候选数: 0

- 方法/构造器候选数: 9
```text
public static ReactorScriptManager getInstance()
public void onHit(Client c, Reactor reactor)
public void act(Client c, Reactor reactor)
public List<ReactorDropEntry> getDrops(int reactorId)
public void clearDrops()
public void touch(Client c, Reactor reactor)
public void untouch(Client c, Reactor reactor)
private void touching(Client c, Reactor reactor, boolean touching)
private Invocable initializeInvocable(Client c, Reactor reactor)
```

---

## `org.gms.server` / `server/CashShop.java`

### 类型声明
```text
class CashShop
```

- 字段候选数: 12
```text
public static final int NX_CREDIT = 1
public static final int MAPLE_POINT = 2
public static final int NX_PREPAID = 4
public static final int MAX_CASH_INVENTORY_SAFE = 1000
private final int accountId
private final int characterId
private int nxCredit
private int maplePoint
private int nxPrepaid
private boolean opened
private ItemFactory factory
private int notes = 0
```

- 方法/构造器候选数: 27
```text
public CashShop(int accountId, int characterId, int jobType)
public record CashShopSurpriseResult(Item usedCashShopSurprise, Item reward)
public int getCash(int type)
public void gainCash(int type, int cash)
public void gainCash(int type, ModifiedCashItemDO buyItem, int world)
public boolean isOpened()
public void open(boolean b)
public List<Item> getInventory()
public Item findByCashId(int cashId)
public boolean addToInventory(Item item)
public boolean canAddToInventory(int itemCount)
public int getInventoryLimit()
public int getInventorySize()
public void removeFromInventory(Item item)
public List<Integer> getWishList()
public void clearWishList()
public void addToWishList(int sn)
public void gift(int recipient, String from, String message, int sn)
public void gift(int recipient, String from, String message, int sn, int ringid)
public int getAvailableNotes()
public void decreaseNotes()
public void save(Connection con) throws SQLException
public Optional<CashShopSurpriseResult> openCashShopSurprise(long cashId)
private Optional<Item> getItemByCashId(long cashId)
public int getItemsSize()
private void trimToSafeInventoryLimit()
public static Item generateCouponItem(int itemId, short quantity)
```

---

## `org.gms.server` / `server/ChatLogger.java`

### 类型声明
```text
class ChatLogger
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static void log(Client c, String chatType, String message)
```

---

## `org.gms.server` / `server/CommonInformation.java`

### 类型声明
```text
class CommonInformation
```

- 字段候选数: 2
```text
private static CommonInformation instance
private final DataProvider stringData
```

- 方法/构造器候选数: 7
```text
private CommonInformation()
public static CommonInformation getInstance()
public List<InformationResult> getStringInformation(InformationSearch condition)
private void searchXML(List<InformationResult> results, InformationType infType, String filter, int filterType, boolean fullMatch)
private void addResult(List<InformationResult> results, InformationType infType, Data data, String filter, int filterType, boolean fullMatch)
private void addMapResult(List<InformationResult> results, InformationType infType, Data data, String filter, int filterType, boolean fullMatch)
private boolean isMatch(String id, String name, String filter, int filterType, boolean fullMatch)
```

---

## `org.gms.server` / `server/DueyPackage.java`

### 类型声明
```text
class DueyPackage
```

- 字段候选数: 7
```text
private String sender = null
private Item item = null
private int mesos = 0
private String message = null
private Calendar timestamp
private int packageId = 0
private Integer receiverId
```

- 方法/构造器候选数: 15
```text
public DueyPackage(int pId, Item item)
public DueyPackage(int pId)
public String getSender()
public void setSender(String name)
public Item getItem()
public int getMesos()
public void setMesos(int set)
public String getMessage()
public void setMessage(String m)
public int getPackageId()
public Integer getReceiverId()
public void setReceiverId(Integer receiverId)
public long sentTimeInMilliseconds()
public boolean isDeliveringTime()
public void setSentTime(Timestamp ts, boolean quick)
```

---

## `org.gms.server` / `server/ExpLogger.java`

### 类型声明
```text
class ExpLogger
```

- 字段候选数: 2
```text
private static final short EXP_LOGGER_THREAD_SLEEP_DURATION_SECONDS = 60
private static final short EXP_LOGGER_THREAD_SHUTDOWN_WAIT_DURATION_MINUTES = 5
```

- 方法/构造器候选数: 4
```text
public record ExpLogRecord(float worldExpRate, int expCoupon, long gainedExp, int currentExp,Timestamp expGainTime, int charid)
public static void putExpLogRecord(ExpLogRecord expLogRecord)
private static void startExpLogger()
private static boolean stopExpLogger()
```

---

## `org.gms.server` / `server/ItemInformationProvider.java`

### 类型声明
```text
class ItemInformationProvider
class ScriptedItem
```

- 字段候选数: 10
```text
protected DataProvider itemData
protected DataProvider equipData
protected DataProvider stringData
protected DataProvider etcData
protected Data cashStringData
protected Data consumeStringData
protected Data eqpStringData
protected Data etcStringData
protected Data insStringData
protected Data petStringData
```

- 方法/构造器候选数: 79
```text
public static ItemInformationProvider getInstance()
private ItemInformationProvider()
private Data getStringData(int itemId)
public boolean noCancelMouse(int itemId)
private Data getItemData(int itemId)
public List<Integer> getItemIdsInRange(int minId, int maxId, boolean ignoreCashItem)
private static short getExtraSlotMaxFromPlayer(Client c, int itemId)
public short getSlotMax(Client c, int itemId)
public int getMeso(int itemId)
private static double getRoundedUnitPrice(double unitPrice, int max)
public int getWholePrice(int itemId)
public double getUnitPrice(int itemId)
public int getPrice(int itemId, int quantity)
protected String getEquipmentSlot(int itemId)
public Integer getEquipLevelReq(int itemId)
public List<Integer> getScrollReqs(int itemId)
public WeaponType getWeaponType(int itemId)
private static double testYourLuck(double prop, int dices)
public static boolean rollSuccessChance(double propPercent)
private static short getMaximumShortMaxIfOverflow(int value1, int value2)
private static short getShortMaxIfOverflow(int value)
private static short chscrollRandomizedStat(int range)
public void scrollOptionEquipWithChaos(Equip nEquip, int range, boolean option)
private void scrollEquipWithChaos(Equip nEquip, int range)
public boolean canUseCleanSlate(Equip equip)
public Item scrollEquipWithId(Item equip, int scrollId, boolean usingWhiteScroll, int vegaItemId, boolean isGM)
public static void improveEquipStats(Equip nEquip, Map<String, Integer> stats)
public Item getEquipById(int equipId)
private Item getEquipById(int equipId, int ringId)
private static short getRandStat(short defaultValue, int maxRange)
public Equip randomizeStats(Equip equip)
private static short getRandUpgradedStat(short defaultValue, int maxRange)
public Equip randomizeUpgradeStats(Equip equip)
public StatEffect getItemEffect(int itemId)
public int[][] getSummonMobs(int itemId)
public int getWatkForProjectile(int itemId)
public String getName(int itemId)
public String getMsg(int itemId)
public boolean isUntradeableRestricted(int itemId)
public boolean isAccountRestricted(int itemId)
public boolean isLootRestricted(int itemId)
public boolean isDropRestricted(int itemId)
public boolean isPickupRestricted(int itemId)
public boolean isQuestItem(int itemId)
public boolean isPartyQuestItem(int itemId)
private void loadCardIdData()
public int getCardMobId(int id)
public boolean isUntradeableOnEquip(int itemId)
public ScriptedItem getScriptedItemInfo(int itemId)
public boolean isKarmaAble(int itemId)
public int getStateChangeItem(int itemId)
public int getCreateItem(int itemId)
public int getMobItem(int itemId)
public int getUseDelay(int itemId)
public int getMobHP(int itemId)
public int getExpById(int itemId)
public int getMaxLevelById(int itemId)
public boolean isConsumeOnPickup(int itemId)
public final boolean isTwoHanded(int itemId)
public boolean isCash(int itemId)
public boolean isUpgradeable(int itemId)
public boolean isUnmerchable(int itemId)
public Collection<Item> canWearEquipment(Character chr, Collection<Item> items)
public boolean canWearEquipment(Character chr, Equip equip, int dst)
private Data getEquipLevelInfo(int itemId)
public int getEquipLevel(int itemId, boolean getMaxLevel)
private static int getCrystalForLevel(int level)
public int getMakerCrystalFromLeftover(Integer leftoverId)
public MakerItemCreateEntry getMakerItemEntry(int toCreate)
public int getMakerCrystalFromEquip(Integer equipId)
public int getMakerStimulantFromEquip(Integer equipId)
public int getMakerDisassembledFee(Integer itemId)
public int getMakerStimulant(int itemId)
public Set<String> getWhoDrops(Integer itemId)
private boolean canUseSkillBook(Character player, Integer skillBookId)
public List<Integer> usableMasteryBooks(Character player)
public List<Integer> usableSkillBooks(Character player)
public final QuestConsItem getQuestConsumablesInfo(final int itemId)
public final ItemCashInfo getItemCashInfo(int itemId)
```

---

## `org.gms.server` / `server/MTSItemInfo.java`

### 类型声明
```text
class MTSItemInfo
```

- 字段候选数: 7
```text
private final int price
private final Item item
private final String seller
private final int id
private final int year
private final int month
private int day = 1
```

- 方法/构造器候选数: 7
```text
public MTSItemInfo(Item item, int price, int id, int cid, String seller, String date)
public Item getItem()
public int getPrice()
public int getTaxes()
public int getID()
public long getEndingDate()
public String getSeller()
```

---

## `org.gms.server` / `server/MakerItemFactory.java`

### 类型声明
```text
class MakerItemFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static MakerItemCreateEntry getItemCreateEntry(int toCreate, int stimulantid, Map<Integer, Short> reagentids)
public static MakerItemCreateEntry generateLeftoverCrystalEntry(int fromLeftoverid, int crystalId)
public static MakerItemCreateEntry generateDisassemblyCrystalEntry(int fromEquipid, int cost, List<Pair<Integer, Integer>> gains)
private static double getMakerStimulantFee(int itemid)
private static double getMakerReagentFee(int itemid, int reagentLevel)
```

---

## `org.gms.server` / `server/MapleLeafLogger.java`

### 类型声明
```text
class MapleLeafLogger
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static void log(Character player, boolean gotPrize, String operation)
```

---

## `org.gms.server` / `server/Marriage.java`

### 类型声明
```text
class Marriage
```

- 字段候选数: 0

- 方法/构造器候选数: 14
```text
public Marriage(EventManager em, String name)
public boolean giftItemToSpouse(int cid)
public List<String> getWishlistItems(boolean groom)
public void initializeGiftItems()
public List<Item> getGiftItems(Client c, boolean groom)
private List<Item> getGiftItemsList(boolean groom)
public Item getGiftItem(Client c, boolean groom, int idx)
public void addGiftItem(boolean groom, Item item)
public void removeGiftItem(boolean groom, Item item)
public Boolean isMarriageGroom(Character chr)
public static boolean claimGiftItems(Client c, Character chr)
public static List<Item> loadGiftItemsFromDb(Client c, int cid)
public void saveGiftItemsToDb(Client c, boolean groom, int cid)
public static void saveGiftItemsToDb(Client c, List<Item> giftItems, int cid)
```

---

## `org.gms.server` / `server/Shop.java`

### 类型声明
```text
class Shop
```

- 字段候选数: 5
```text
private final int id
private final int npcId
private final List<ShopItem> items
private final int tokenvalue = 1000000000
private final int token = ItemId.GOLDEN_MAPLE_LEAF
```

- 方法/构造器候选数: 12
```text
private Shop(int id, int npcId)
private void addItem(ShopItem item)
public void sendShop(Client c)
public void buy(Client c, short slot, int itemId, short quantity)
private static boolean canSell(Item item, short quantity)
private static short getSellingQuantity(Item item, short quantity)
public void sell(Client c, InventoryType type, short slot, short quantity)
public void recharge(Client c, short slot)
private ShopItem findBySlot(short slot)
public static Shop createFromDB(int id, boolean isShopId)
public int getNpcId()
public int getId()
```

---

## `org.gms.server` / `server/ShopFactory.java`

### 类型声明
```text
class ShopFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 5
```text
public static ShopFactory getInstance()
private Shop loadShop(int id, boolean isShopId)
public Shop getShop(int shopId)
public Shop getShopForNPC(int npcId)
public void reloadShops()
```

---

## `org.gms.server` / `server/ShopItem.java`

### 类型声明
```text
class ShopItem
```

- 字段候选数: 4
```text
private final short buyable
private final int itemId
private final int price
private final int pitch
```

- 方法/构造器候选数: 5
```text
public ShopItem(short buyable, int itemId, int price, int pitch)
public short getBuyable()
public int getItemId()
public int getPrice()
public int getPitch()
```

---

## `org.gms.server` / `server/SkillbookInformationProvider.java`

### 类型声明
```text
class SkillbookInformationProvider
enum SkillBookEntry
```

- 字段候选数: 1
```text
private static final int SKILLBOOK_MIN_ITEMID = 2280000
```

- 方法/构造器候选数: 11
```text
public static void loadAllSkillbookInformation()
private static boolean is4thJobSkill(int itemid)
private static boolean isSkillBook(int itemid)
private static boolean isQuestBook(int itemid)
private static int fetchQuestbook(Data checkData, String quest)
private static void listFiles(String directoryName, ArrayList<Path> files)
private static List<Path> listFilesFromDirectoryRecursively(String directory)
private static Set<Integer> findMatchingSkillbookIdsOnFile(String fileContent)
private static String readFileToString(Path file, String encoding) throws IOException
public static SkillBookEntry getSkillbookAvailability(int itemId)
public static List<Integer> getTeachableSkills(Character chr)
```

---

## `org.gms.server` / `server/StatEffect.java`

### 类型声明
```text
class StatEffect
```

- 字段候选数: 6
```text
private int moveTo
private List<Disease> cureDebuffs
private boolean skill
private double prop
private byte mapProtection
private CardItemupStats cardStats
```

- 方法/构造器候选数: 105
```text
private boolean isEffectActive(int mapid, boolean partyHunting)
public boolean isActive(Character applyto)
public int getCardRate(int mapid, int itemid)
public static StatEffect loadSkillEffectFromData(Data source, int skillid, boolean overtime)
public static StatEffect loadItemEffectFromData(Data source, int itemid)
private static void addBuffStatPairToListIfNotZero(List<Pair<BuffStat, Integer>> list, BuffStat buffstat, Integer val)
private static byte mapProtection(int sourceid)
private static StatEffect loadFromData(Data source, int sourceid, boolean skill, boolean overTime)
public void applyPassive(Character applyto, MapObject obj, int attack)
public boolean applyEchoOfHero(Character applyfrom)
public boolean applyTo(Character chr)
public boolean applyTo(Character chr, boolean useMaxRange)
public boolean applyTo(Character chr, Point pos)
private boolean applyTo(Character applyfrom, Character applyto, boolean primary, Point pos, boolean useMaxRange, int affectedPlayers)
private int applyBuff(Character applyfrom, boolean useMaxRange)
private void applyMonsterBuff(Character applyfrom)
public boolean hasBoundingBox()
public Rectangle calculateBoundingBox(Point posFrom, boolean facingLeft)
public int getBuffLocalDuration()
public void silentApplyBuff(Character chr, long localStartTime)
public final void applyComboBuff(final Character applyto, int combo)
public final void applyBeaconBuff(final Character applyto, int objectid)
public void updateBuffEffect(Character target, List<Pair<BuffStat, Integer>> activeStats, long starttime)
private void applyBuffEffect(Character applyfrom, Character applyto, boolean primary)
private int calcHPChange(Character applyfrom, boolean primary, int affectedPlayers)
private int makeHealHP(double rate, double stat, double lowerfactor, double upperfactor)
private int calcMPChange(Character applyfrom, boolean primary)
private int alchemistModifyVal(Character chr, int val, boolean withX)
private StatEffect getAlchemistEffect(Character chr)
private boolean isGmBuff()
private boolean isMonsterBuff()
private boolean isPartyBuff()
private boolean isHeal()
private boolean isResurrection()
private boolean isTimeLeap()
public boolean isDragonBlood()
public boolean isBerserk()
public boolean isRecovery()
public boolean isMapChair()
public static boolean isMapChair(int sourceid)
public static boolean isHpMpRecovery(int sourceid)
public static boolean isAriantShield(int sourceid)
private boolean isDs()
private boolean isWw()
private boolean isCombo()
private boolean isEnrage()
public boolean isBeholder()
private boolean isShadowPartner()
private boolean isChakra()
private boolean isCouponBuff()
private boolean isAriantShield()
private boolean isMysticDoor()
public boolean isMonsterRiding()
public boolean isMagicDoor()
public boolean isPoison()
public boolean isMorph()
public boolean isMorphWithoutAttack()
private boolean isMist()
private boolean isSoulArrow()
private boolean isShadowClaw()
private boolean isCrash()
private boolean isSeal()
private boolean isDispel()
private boolean isCureAllAbnormalStatus()
public static boolean isHerosWill(int skillid)
private boolean isWkCharge()
private boolean isDash()
private boolean isSkillMorph()
private boolean isInfusion()
private boolean isCygnusFA()
private boolean isHyperBody()
private boolean isComboReset()
private int getFatigue()
private int getMorph()
private int getMorph(Character chr)
private SummonMovementType getSummonMovementType()
public boolean isSkill()
public int getSourceId()
public void setSourceId(int id)
public int getBuffSourceId()
public boolean makeChanceResult()
public short getHp()
public short getMp()
public double getHpRate()
public double getMpRate()
public byte getHpR()
public byte getMpR()
public short getHpRRate()
public short getMpRRate()
public short getHpCon()
public short getMpCon()
public short getMatk()
public short getWatk()
public int getDuration()
public boolean sameSource(StatEffect effect)
public int getX()
public int getY()
public int getDamage()
public int getAttackCount()
public int getMobCount()
public int getFixDamage()
public short getBulletCount()
public short getBulletConsume()
public int getMoneyCon()
public int getCooldown()
```

---

## `org.gms.server` / `server/Storage.java`

### 类型声明
```text
class Storage
```

- 字段候选数: 4
```text
private final int id
private int currentNpcid
private int meso
private byte slots
```

- 方法/构造器候选数: 24
```text
private Storage(int id, byte slots, int meso)
private static Storage create(int id, int world) throws SQLException
public static Storage loadOrCreateFromDB(int id, int world)
public byte getSlots()
public boolean canGainSlots(int slots)
public boolean gainSlots(int slots)
public void saveToDB(Connection con)
public Item getItem(byte slot)
public boolean takeOut(Item item)
public boolean store(Item item)
public List<Item> getItems()
private List<Item> filterItems(InventoryType type)
public byte getSlot(InventoryType type, byte slot)
public void sendStorage(Client c, int npcId)
public void sendStored(Client c, InventoryType type)
public void sendTakenOut(Client c, InventoryType type)
public void arrangeItems(Client c)
public int getMeso()
public void setMeso(int meso)
public void sendMeso(Client c)
public int getStoreFee()
public int getTakeOutFee()
public boolean isFull()
public void close()
```

---

## `org.gms.server` / `server/StorageInventory.java`

### 类型声明
```text
class StorageInventory
class PairedQuicksort
```

- 字段候选数: 5
```text
private final Client c
private final byte slotLimit
private int i = 0
private int j = 0
private final ArrayList<Integer> intersect
```

- 方法/构造器候选数: 22
```text
public StorageInventory(Client c, List<Item> toSort)
private byte getSlotLimit()
private Collection<Item> list()
private short addItem(Item item)
private static boolean isEquipOrCash(Item item)
private static boolean isSameOwner(Item source, Item target)
private void move(short sSlot, short dSlot, short slotMax)
private void moveItem(short src, short dst)
private void swap(Item source, Item target)
private Item getItem(short slot)
private void addSlot(short slot, Item item)
private void removeSlot(short slot)
private boolean isFull()
private short getNextFreeSlot()
public void mergeItems()
public List<Item> sortItems()
private void PartitionByItemId(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByName(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByQuantity(int Esq, int Dir, ArrayList<Item> A)
private void PartitionByLevel(int Esq, int Dir, ArrayList<Item> A)
void MapleQuicksort(int Esq, int Dir, ArrayList<Item> A, int sort)
public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)
```

---

## `org.gms.server` / `server/SystemRescue.java`

### 类型声明
```text
class SystemRescue
```

- 字段候选数: 1
```text
private static final String key_mapError_sysmsg = "系统救援_卡地图_系统通知"
```

- 方法/构造器候选数: 3
```text
public void setMapChange(Character player)
public void showMapChangeMessage(Character player)
private boolean dropMessage(Character player, String keyname, int type)
```

---

## `org.gms.server` / `server/ThreadManager.java`

### 类型声明
```text
class ThreadManager
```

- 字段候选数: 1
```text
private ExecutorService executorService
```

- 方法/构造器候选数: 4
```text
private ThreadManager()
public void newTask(Runnable r)
public void start()
public void stop()
```

---

## `org.gms.server` / `server/TimerManager.java`

### 类型声明
```text
class TimerManager
```

- 字段候选数: 1
```text
private ScheduledThreadPoolExecutor ses
```

- 方法/构造器候选数: 16
```text
private TimerManager()
public void start()
public void stop()
public Runnable purge()
public ScheduledFuture<?> register(Runnable r, long repeatTime, long delay)
public ScheduledFuture<?> register(Runnable r, long repeatTime)
public ScheduledFuture<?> update(ScheduledFuture<?> sf, Runnable r, long repeatTime)
public void stop(ScheduledFuture<?> sf)
public ScheduledFuture<?> schedule(Runnable r, long delay)
public ScheduledFuture<?> scheduleAtTimestamp(Runnable r, long timestamp)
public long getActiveCount()
public long getCompletedTaskCount()
public int getQueuedTasks()
public long getTaskCount()
public boolean isShutdown()
public boolean isTerminated()
```

---

## `org.gms.server` / `server/TimerManagerMBean.java`

### 类型声明
```text
interface TimerManagerMBean
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server` / `server/Trade.java`

### 类型声明
```text
class Trade
enum TradeResult
```

- 字段候选数: 7
```text
private Trade partner = null
private List<Item> exchangeItems
private int meso = 0
private int exchangeMeso
private final Character chr
private final byte number
private boolean fullTrade = false
```

- 方法/构造器候选数: 36
```text
public Trade(byte number, Character chr)
public static int getFee(long meso)
private void lockTrade()
private void fetchExchangedItems()
private void completeTrade()
private void cancel(byte result)
private boolean isLocked()
private int getMeso()
public void setMeso(int meso)
public boolean addItem(Item item)
public void chat(String message)
public Trade getPartner()
public void setPartner(Trade partner)
public Character getChr()
public List<Item> getItems()
public int getExchangeMesos()
private boolean fitsMeso()
private boolean fitsInInventory()
private boolean fitsUniquesInInventory()
private synchronized boolean checkTradeCompleteHandshake(boolean updateSelf)
private boolean checkCompleteHandshake()
public static void completeTrade(Character chr)
private static void cancelTradeInternal(Character chr, byte selfResult, byte partnerResult)
private static byte[] tradeResultsPair(byte result)
private synchronized void tradeCancelHandshake(boolean updateSelf, byte result)
private void cancelHandshake(byte result)
public static void cancelTrade(Character chr, TradeResult result)
public static void startTrade(Character chr)
private static boolean hasTradeInviteBack(Character c1, Character c2)
public static void inviteTrade(Character c1, Character c2)
public static void visitTrade(Character c1, Character c2)
public static void declineTrade(Character chr)
public boolean isFullTrade()
public void setFullTrade(boolean fullTrade)
private static void logTrade(Trade trade1, Trade trade2)
private static String getFormattedItemLogMessage(List<Item> items)
```

---

## `org.gms.server.events` / `server/events/Events.java`

### 类型声明
```text
class Events
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public Events()
```

---

## `org.gms.server.events` / `server/events/RescueGaga.java`

### 类型声明
```text
class RescueGaga
```

- 字段候选数: 1
```text
private int completed
```

- 方法/构造器候选数: 5
```text
public RescueGaga(int completed)
public int getCompleted()
public void complete()
public int getInfo()
public void giveSkill(Character chr)
```

---

## `org.gms.server.events.gm` / `server/events/gm/Coconut.java`

### 类型声明
```text
class Coconut
```

- 字段候选数: 6
```text
private MapleMap map = null
private int MapleScore = 0
private int StoryScore = 0
private int countBombing = 80
private int countFalling = 401
private int countStopped = 20
```

- 方法/构造器候选数: 17
```text
public Coconut(MapleMap map)
public void startEvent()
public void bonusTime()
public void warpOut()
public int getMapleScore()
public int getStoryScore()
public void addMapleScore()
public void addStoryScore()
public int getBombings()
public void bombCoconut()
public int getFalling()
public void fallCoconut()
public int getStopped()
public void stopCoconut()
public Coconuts getCoconut(int id)
public List<Coconuts> getAllCoconuts()
public void setCoconutsHittable(boolean hittable)
```

---

## `org.gms.server.events.gm` / `server/events/gm/Coconuts.java`

### 类型声明
```text
class Coconuts
```

- 字段候选数: 3
```text
private final int id
private int hits = 0
private boolean hittable = false
```

- 方法/构造器候选数: 7
```text
public Coconuts(int id)
public void hit()
public int getHits()
public void resetHits()
public boolean isHittable()
public void setHittable(boolean hittable)
public long getHitTime()
```

---

## `org.gms.server.events.gm` / `server/events/gm/Event.java`

### 类型声明
```text
class Event
```

- 字段候选数: 2
```text
private final int mapid
private int limit
```

- 方法/构造器候选数: 5
```text
public Event(int mapid, int limit)
public int getMapId()
public int getLimit()
public void minusLimit()
public void addLimit()
```

---

## `org.gms.server.events.gm` / `server/events/gm/Fitness.java`

### 类型声明
```text
class Fitness
```

- 字段候选数: 5
```text
private final Character chr
private long time = 0
private long timeStarted = 0
private ScheduledFuture<?> schedule = null
private ScheduledFuture<?> schedulemsg = null
```

- 方法/构造器候选数: 7
```text
public Fitness(final Character chr)
public void startFitness()
public boolean isTimerStarted()
public long getTime()
public void resetTimes()
public long getTimeLeft()
public void checkAndMessage()
```

---

## `org.gms.server.events.gm` / `server/events/gm/Ola.java`

### 类型声明
```text
class Ola
```

- 字段候选数: 4
```text
private final Character chr
private long time = 0
private long timeStarted = 0
private ScheduledFuture<?> schedule = null
```

- 方法/构造器候选数: 6
```text
public Ola(final Character chr)
public void startOla()
public boolean isTimerStarted()
public long getTime()
public void resetTimes()
public long getTimeLeft()
```

---

## `org.gms.server.events.gm` / `server/events/gm/OxQuiz.java`

### 类型声明
```text
class OxQuiz
```

- 字段候选数: 4
```text
private int round = 1
private int question = 1
private MapleMap map = null
private final int expGain = 200
```

- 方法/构造器候选数: 4
```text
public OxQuiz(MapleMap map)
private boolean isCorrectAnswer(Character chr, int answer)
public void sendQuestion()
private static int getOXAnswer(int imgdir, int id)
```

---

## `org.gms.server.events.gm` / `server/events/gm/Snowball.java`

### 类型声明
```text
class Snowball
```

- 字段候选数: 7
```text
private final MapleMap map
private int position = 0
private int hits = 3
private int snowmanhp = 1000
private boolean hittable = false
private final int team
private boolean winner = false
```

- 方法/构造器候选数: 10
```text
public Snowball(int team, MapleMap map)
public void startEvent()
public boolean isHittable()
public void setHittable(boolean hit)
public int getPosition()
public int getSnowmanHP()
public void setSnowmanHP(int hp)
public void hit(int what, int damage)
public void message(int message)
public void warpOut()
```

---

## `org.gms.server.expeditions` / `server/expeditions/Expedition.java`

### 类型声明
```text
class Expedition
```

- 字段候选数: 10
```text
private final Character leader
private final ExpeditionType type
private boolean registering
private final MapleMap startMap
private final List<String> bossLogs
private ScheduledFuture<?> schedule
private long startTime
private final boolean silent
private final int minSize
private final int maxSize
```

- 方法/构造器候选数: 37
```text
public Expedition(Character player, ExpeditionType met, boolean sil, int minPlayers, int maxPlayers)
public int getMinSize()
public int getMaxSize()
public void beginRegistration()
private void scheduleRegistrationEnd()
public void dispose(boolean log)
private void log()
private static String getTimeString(long then)
public void finishRegistration()
public void start()
public String addMember(Character player)
public int addMemberInt(Character player)
private void registerExpeditionAttempt()
private void broadcastExped(Packet packet)
public boolean removeMember(Character chr)
public void ban(Entry<Integer, String> chr)
public void monsterKilled(Character chr, Monster mob)
public void setProperty(String key, String value)
public String getProperty(String key)
public ExpeditionType getType()
public List<Character> getActiveMembers()
public final boolean isExpeditionTeamTogether()
public final void warpExpeditionTeam(int warpFrom, int warpTo)
public final void warpExpeditionTeam(int warpTo)
public final void warpExpeditionTeamToMapSpawnPoint(int warpFrom, int warpTo, int toSp)
public final void warpExpeditionTeamToMapSpawnPoint(int warpTo, int toSp)
public final boolean addChannelExpedition(Channel ch)
public final void removeChannelExpedition(Channel ch)
public Character getLeader()
public MapleMap getRecruitingMap()
public boolean contains(Character player)
public boolean isLeader(Character player)
public boolean isLeader(int playerid)
public boolean isRegistering()
public boolean isInProgress()
public long getStartTime()
public List<String> getBossLogs()
```

---

## `org.gms.server.expeditions` / `server/expeditions/ExpeditionBossLog.java`

### 类型声明
```text
class ExpeditionBossLog
enum BossLogEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public static void resetBossLogTable()
private static void resetBossLogTable(boolean week, Calendar c)
private static String getBossLogTable(boolean week)
private static int countPlayerEntries(int cid, BossLogEntry boss)
private static void insertPlayerEntry(int cid, BossLogEntry boss)
public static boolean attemptBoss(int cid, int channel, Expedition exped, boolean log)
```

---

## `org.gms.server.expeditions` / `server/expeditions/ExpeditionType.java`

### 类型声明
```text
enum ExpeditionType
```

- 字段候选数: 5
```text
private final int minSize
private final int maxSize
private final int minLevel
private final int maxLevel
private final int registrationMinutes
```

- 方法/构造器候选数: 19
```text
BALROG_EASY(3, 30, 50, 255, 5),
BALROG_NORMAL(6, 30, 50, 255, 5),
SCARGA(6, 30, 100, 255, 5),
SHOWA(3, 30, 100, 255, 5),
ZAKUM(6, 30, 50, 255, 5),
HORNTAIL(6, 30, 100, 255, 5),
CHAOS_ZAKUM(6, 30, 120, 255, 5),
CHAOS_HORNTAIL(6, 30, 120, 255, 5),
ARIANT(2, 7, 20, 30, 5),
ARIANT1(2, 7, 20, 30, 5),
ARIANT2(2, 7, 20, 30, 5),
PINKBEAN(6, 30, 120, 255, 5),
CWKPQ(6, 30, 90, 255, 5);   // CWKPQ min-level 90, found thanks to Cato
ExpeditionType(int minSize, int maxSize, int minLevel, int maxLevel, int minutes)
public int getMinSize()
public int getMaxSize()
public int getMinLevel()
public int getMaxLevel()
public int getRegistrationMinutes()
```

---

## `org.gms.server.gachapon` / `server/gachapon/ElNath.java`

### 类型声明
```text
class ElNath
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Ellinia.java`

### 类型声明
```text
class Ellinia
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Gachapon.java`

### 类型声明
```text
class Gachapon
enum GachaponType
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public static Gachapon getInstance()
public GachaponItem process(int npcId)
public static void log(Character player, int itemId, String map)
```

---

## `org.gms.server.gachapon` / `server/gachapon/GachaponItems.java`

### 类型声明
```text
class GachaponItems
```

- 字段候选数: 3
```text
private final int[] commonItems
private final int[] uncommonItems
private final int[] rareItems
```

- 方法/构造器候选数: 2
```text
public GachaponItems()
public final int[] getItems(int tier)
```

---

## `org.gms.server.gachapon` / `server/gachapon/Global.java`

### 类型声明
```text
class Global
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Henesys.java`

### 类型声明
```text
class Henesys
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/KerningCity.java`

### 类型声明
```text
class KerningCity
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Ludibrium.java`

### 类型声明
```text
class Ludibrium
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/MushroomShrine.java`

### 类型声明
```text
class MushroomShrine
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/NautilusHarbor.java`

### 类型声明
```text
class NautilusHarbor
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/NewLeafCity.java`

### 类型声明
```text
class NewLeafCity
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Perion.java`

### 类型声明
```text
class Perion
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/ShowaSpaFemale.java`

### 类型声明
```text
class ShowaSpaFemale
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/ShowaSpaMale.java`

### 类型声明
```text
class ShowaSpaMale
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.gachapon` / `server/gachapon/Sleepywood.java`

### 类型声明
```text
class Sleepywood
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

---

## `org.gms.server.life` / `server/life/AbstractLoadedLife.java`

### 类型声明
```text
class AbstractLoadedLife
```

- 字段候选数: 8
```text
private final int id
private int f
private boolean hide
private int fh
private int start_fh
private int cy
private int rx0
private int rx1
```

- 方法/构造器候选数: 16
```text
public AbstractLoadedLife(int id)
public AbstractLoadedLife(AbstractLoadedLife life)
public int getF()
public void setF(int f)
public boolean isHidden()
public void setHide(boolean hide)
public int getFh()
public void setFh(int fh)
public int getStartFh()
public int getCy()
public void setCy(int cy)
public int getRx0()
public void setRx0(int rx0)
public int getRx1()
public void setRx1(int rx1)
public int getId()
```

---

## `org.gms.server.life` / `server/life/ChangeableStats.java`

### 类型声明
```text
class ChangeableStats
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public ChangeableStats(MonsterStats stats, OverrideMonsterStats ostats)
public ChangeableStats(MonsterStats stats, int newLevel, boolean pqMob)
public ChangeableStats(MonsterStats stats, float statModifier, boolean pqMob)
```

---

## `org.gms.server.life` / `server/life/Element.java`

### 类型声明
```text
enum Element
```

- 字段候选数: 2
```text
private final int value
private boolean special = false
```

- 方法/构造器候选数: 5
```text
Element(int v)
Element(int v, boolean special)
public boolean isSpecial()
public static Element getFromChar(char c)
public int getValue()
```

---

## `org.gms.server.life` / `server/life/ElementalEffectiveness.java`

### 类型声明
```text
enum ElementalEffectiveness
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static ElementalEffectiveness getByNumber(int num)
```

---

## `org.gms.server.life` / `server/life/LifeFactory.java`

### 类型声明
```text
class LifeFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 18
```text
private static Set<Integer> getHpBarBosses()
public static AbstractLoadedLife getLife(int id, String type)
private static Data resolveUol(Data data)
private static boolean isBboxAction(String name)
private static BoundingBox buildMonsterBoundingBox(int mid, String mobName, Data monsterData)
private static Data getMonsterData(int mid)
private static Data resolveMonsterVisualData(int mid, Data monsterData)
private static boolean hasVisualBoundingBoxSource(Data monsterData)
private static Data resolvePrimaryVisualFrame(Data monsterData)
private static Data resolveVisualFrame(Data frameData)
private static void applyMonsterVisualStats(int mid, MonsterStats stats, Data visualMonsterData)
private static void setMonsterAttackInfo(int mid, List<MobAttackInfoHolder> attackInfos)
public static Monster getMonster(int mid)
public static int getMonsterLevel(int mid)
private static void decodeElementalString(MonsterStats stats, String elemAttr)
public static NPC getNPC(int nid)
public static String getNPCName(int nid)
public static String getNPCDefaultTalk(int nid)
```

---

## `org.gms.server.life` / `server/life/MobAttackInfo.java`

### 类型声明
```text
class MobAttackInfo
```

- 字段候选数: 5
```text
private boolean isDeadlyAttack
private int mpBurn
private int diseaseSkill
private int diseaseLevel
private int mpCon
```

- 方法/构造器候选数: 11
```text
public MobAttackInfo(int mobId, int attackId)
public void setDeadlyAttack(boolean isDeadlyAttack)
public boolean isDeadlyAttack()
public void setMpBurn(int mpBurn)
public int getMpBurn()
public void setDiseaseSkill(int diseaseSkill)
public int getDiseaseSkill()
public void setDiseaseLevel(int diseaseLevel)
public int getDiseaseLevel()
public void setMpCon(int mpCon)
public int getMpCon()
```

---

## `org.gms.server.life` / `server/life/MobAttackInfoFactory.java`

### 类型声明
```text
class MobAttackInfoFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static MobAttackInfo getMobAttackInfo(Monster mob, int attack)
```

---

## `org.gms.server.life` / `server/life/MobSkill.java`

### 类型声明
```text
class MobSkill
```

- 字段候选数: 14
```text
private final MobSkillId id
private final int mpCon
private final int spawnEffect
private final int hp
private final int x
private final int y
private final int count
private final long duration
private final long cooltime
private final float prop
private final Point lt
private final Point rb
private final int limit
private final List<Integer> toSummon
```

- 方法/构造器候选数: 23
```text
private MobSkill(MobSkillType type, int level, int mpCon, int spawnEffect, int hp, int x, int y, int count, long duration, long cooltime, float prop, Point lt, Point rb, int limit, List<Integer> toSummon)
public void applyDelayedEffect(final Character player, final Monster monster, final boolean skill, int animationTime)
public void applyEffect(Monster monster)
public void applyEffect(Character player, Monster monster, boolean skill, List<Character> banishPlayersOutput)
private void applyHealEffect(boolean skill, Monster monster)
private void applyDispelEffect(boolean skill, Monster monster, Character player)
private void applyBanishEffect(boolean skill, Monster monster, Character player, List<Character> banishPlayersOutput)
private void spawnMonsterMist(Monster monster)
private void summonMonsters(Monster monster)
private void applyMonsterBuffs(Map<MonsterStatus, Integer> stats, boolean skill, Monster monster, List<Integer> reflection)
private void applyDisease(Disease disease, boolean skill, Monster monster, Character player)
private List<Character> getPlayersInRange(Monster monster)
public MobSkillId getId()
public MobSkillType getType()
public int getMpCon()
public int getHP()
public int getX()
public int getY()
public long getDuration()
public long getCoolTime()
public boolean makeChanceResult()
private Rectangle calculateBoundingBox(Point posFrom)
private List<MapObject> getObjectsInRange(Monster monster, MapObjectType objectType)
```

---

## `org.gms.server.life` / `server/life/MobSkillFactory.java`

### 类型声明
```text
class MobSkillFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static MobSkill getMobSkillOrThrow(MobSkillType type, int level)
public static Optional<MobSkill> getMobSkill(final MobSkillType type, final int level)
private static Optional<MobSkill> loadMobSkill(final MobSkillType type, final int level)
private static String createKey(MobSkillType type, int skillLevel)
```

---

## `org.gms.server.life` / `server/life/MobSkillId.java`

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.life` / `server/life/MobSkillType.java`

### 类型声明
```text
enum MobSkillType
```

- 字段候选数: 1
```text
private final int id
```

- 方法/构造器候选数: 44
```text
ATTACK_UP(100),
MAGIC_ATTACK_UP(101),
DEFENSE_UP(102),
MAGIC_DEFENSE_UP(103),
ATTACK_UP_M(110),
MAGIC_ATTACK_UP_M(111),
DEFENSE_UP_M(112),
MAGIC_DEFENSE_UP_M(113),
HEAL_M(114),
HASTE_M(115),
SEAL(120),
DARKNESS(121),
WEAKNESS(122),
STUN(123),
CURSE(124),
POISON(125),
SLOW(126),
DISPEL(127),
SEDUCE(128),
BANISH(129),
AREA_POISON(131),
REVERSE_INPUT(132),
UNDEAD(133),
STOP_POTION(134),
STOP_MOTION(135),
FEAR(136),
PHYSICAL_IMMUNE(140),
MAGIC_IMMUNE(141),
HARD_SKIN(142),
PHYSICAL_COUNTER(143),
MAGIC_COUNTER(144),
PHYSICAL_AND_MAGIC_COUNTER(145),
PAD(150),
MAD(151),
PDR(152),
MDR(153),
ACC(154),
EVA(155),
SPEED(156),
SEAL_SKILL(157),
MobSkillType(int id)
public static Optional<MobSkillType> from(int id)
private static boolean isOutOfIdRange(int id)
public int getId()
```

---

## `org.gms.server.life` / `server/life/Monster.java`

### 类型声明
```text
class Monster
class DamageTask
```

- 字段候选数: 13
```text
private MonsterStats stats
private int mp
private MapleMap map
private int VenomMultiplier = 0
private boolean fake = false
private boolean dropsDisabled = false
private Set<Integer> calledMobOids = null
private int team
private int parentMobOid = 0
private int spawnEffect = 0
private ScheduledFuture<?> monsterItemDrop = null
private Runnable removeAfterAction = null
private boolean availablePuppetUpdate = true
```

- 方法/构造器候选数: 154
```text
public Monster(int id, MonsterStats stats)
public Monster(Monster monster)
public void lockMonster()
public void unlockMonster()
private void initWithStats(MonsterStats baseStats)
public void setSpawnEffect(int effect)
public int getSpawnEffect()
public void disableDrops()
public void enableDrops()
public boolean dropsDisabled()
public void setMap(MapleMap map)
public int getParentMobOid()
public void setParentMobOid(int parentMobId)
public int countAvailableMobSummons(int summonsSize, int skillLimit)
public void addSummonedMob(Monster mob)
private void removeSummonedMob(int mobOid)
private void setSummonerMob(Monster mob)
private void dispatchClearSummons()
public void pushRemoveAfterAction(Runnable run)
public Runnable popRemoveAfterAction()
public int getHp()
public synchronized void addHp(int hp)
public synchronized void setStartingHp(int hp)
public int getMaxHp()
public int getMp()
public void setMp(int mp)
public int getMaxMp()
public int getExp()
public int getLevel()
public int getCP()
public int getTeam()
public void setTeam(int team)
public int getVenomMulti()
public void setVenomMulti(int multiplier)
public MonsterStats getStats()
public void setStats(MonsterStats stats)
public boolean isBoss()
public int getAnimationTime(String name)
private List<Integer> getRevives()
private byte getTagColor()
private byte getTagBgColor()
public void setHpZero()
private boolean applyAnimationIfRoaming(int attackPos, MobSkill skill)
public synchronized Integer applyAndGetHpDamage(int delta, boolean stayAlive)
public synchronized void disposeMapObject()
public void broadcastMobHpBar(Character from)
public boolean damage(Character attacker, int damage, boolean stayAlive)
private void applyDamage(Character from, int damage, boolean stayAlive, boolean fake)
public void applyFakeDamage(Character from, int damage, boolean stayAlive)
public void heal(int hp, int mp)
public boolean isAttackedBy(Character chr)
private static boolean isWhiteExpGain(Character chr, Map<Integer, Float> personalRatio, double sdevRatio)
private static double calcExperienceStandDevThreshold(List<Float> entryExpRatio, int totalEntries)
private void distributePlayerExperience(Character chr, float exp, float partyBonusMod, int totalPartyLevel, boolean highestPartyDamager, boolean whiteExpGain, boolean hasPartySharers)
private void distributePartyExperience(Map<Character, Long> partyParticipation, float expPerDmg, Set<Character> underleveled, Map<Integer, Float> personalRatio, double sdevRatio)
private void distributeExperience(int killerId)
private float getStatusExpMultiplier(Character attacker, boolean hasPartySharers)
private static int expValueToInteger(double exp)
private void giveExpToCharacter(Character attacker, Float personalExp, Float partyExp, boolean white, boolean hasPartySharers)
public List<MonsterDropEntry> retrieveRelevantDrops()
public Character killBy(final Character killer)
public void dropFromFriendlyMonster(long delay)
private void dispatchRaiseQuestMobCount()
public void dispatchMonsterKilled(boolean hasKiller)
private synchronized void processMonsterKilled(boolean hasKiller)
private void dispatchMonsterDamaged(Character from, int trueDmg)
private void dispatchMonsterHealed(int trueHeal)
private void giveFamilyRep(FamilyEntry entry)
public int getHighestDamagerId()
public boolean isAlive()
public void addListener(MonsterListener listener)
public Character getController()
private void setController(Character controller)
public boolean isControllerHasAggro()
private void setControllerHasAggro(boolean controllerHasAggro)
public boolean isControllerKnowsAboutAggro()
private void setControllerKnowsAboutAggro(boolean controllerKnowsAboutAggro)
private void setControllerHasPuppet(boolean controllerHasPuppet)
public Packet makeBossHPBarPacket()
public boolean hasBossHPBar()
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public MapObjectType getType()
public boolean isMobile()
public boolean isFacingLeft()
public ElementalEffectiveness getElementalEffectiveness(Element e)
private ElementalEffectiveness getMonsterEffectiveness(Element e)
private Character getActiveController()
private void broadcastMonsterStatusMessage(Packet packet)
private int broadcastStatusEffect(final MonsterStatusEffect status)
public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration)
public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration, boolean venom)
public final void dispelSkill(final MobSkill skill)
public void applyMonsterBuff(final Map<MonsterStatus, Integer> stats, final int x, long duration, MobSkill skill, final List<Integer> reflection)
public void refreshMobPosition()
public void resetMobPosition(Point newPoint)
private void debuffMobStat(MonsterStatus stat)
public void debuffMob(int skillid)
public boolean isBuffed(MonsterStatus status)
public void setFake(boolean fake)
public boolean isFake()
public MapleMap getMap()
public MonsterAggroCoordinator getMapAggroCoordinator()
public Set<MobSkillId> getSkills()
public boolean hasSkill(int skillId, int level)
public boolean canUseSkill(MobSkill toUse, boolean apply)
private boolean isReflectSkill(MobSkill mobSkill)
private void usedSkill(MobSkill skill)
private void clearSkill(MobSkillId msId)
public int canUseAttack(int attackPos, boolean isSkill)
private void usedAttack(final int attackPos, int mpCon, int cooltime)
private void clearAttack(int attackPos)
public boolean hasAnySkill()
public MobSkillId getRandomSkill()
public boolean isFirstAttack()
public int getBuffToGive()
public String getName()
public void addStolen(int itemId)
public List<Integer> getStolen()
public void setTempEffectiveness(Element e, ElementalEffectiveness ee, long milli)
public Collection<MonsterStatus> alreadyBuffedStats()
public BanishInfo getBanish()
public void setBoss(boolean boss)
public int getDropPeriodTime()
public int getPADamage()
public MonsterStatusEffect getStati(MonsterStatus ms)
public final ChangeableStats getChangedStats()
public final int getMobMaxHp()
public final void setOverrideStats(final OverrideMonsterStats ostats)
public final void changeLevel(final int newLevel)
public final void changeLevel(final int newLevel, boolean pqMob)
private float getDifficultyRate(final int difficulty)
private void changeLevelByDifficulty(final int difficulty, boolean pqMob)
public final void changeDifficulty(final int difficulty, boolean pqMob)
private boolean isPuppetInVicinity(Summon summon)
public boolean isCharacterPuppetInVicinity(Character chr)
public boolean isLeadingPuppetInVicinity()
private Character getNextControllerCandidate()
public void aggroSwitchController(Character newController, boolean immediateAggro)
public void aggroAddPuppet(Character player)
public void aggroRemovePuppet(Character player)
public void aggroUpdateController()
private void aggroUpdatePuppetController(Character newController)
public void aggroRedirectController()
public Boolean aggroMoveLifeUpdate(Character player)
public void aggroAutoAggroUpdate(Character player)
public void aggroMonsterDamage(Character attacker, int damage)
private static void aggroMonsterControl(Client c, Monster mob, boolean immediateAggro)
private void aggroRefreshPuppetVisibility(Character chrController, Summon puppet)
public void aggroUpdatePuppetVisibility()
public void aggroClearDamages()
public void aggroResetAggro()
public final int getRemoveAfter()
public void dispose()
```

---

## `org.gms.server.life` / `server/life/MonsterDropEntry.java`

### 类型声明
```text
class MonsterDropEntry
```

- 字段候选数: 1
```text
public short questid
```

- 方法/构造器候选数: 1
```text
public MonsterDropEntry(int itemId, int chance, int Minimum, int Maximum, short questid)
```

---

## `org.gms.server.life` / `server/life/MonsterGlobalDropEntry.java`

### 类型声明
```text
class MonsterGlobalDropEntry
```

- 字段候选数: 1
```text
public short questid
```

- 方法/构造器候选数: 1
```text
public MonsterGlobalDropEntry(int itemId, int chance, int continent, int Minimum, int Maximum, short questid)
```

---

## `org.gms.server.life` / `server/life/MonsterInformationProvider.java`

### 类型声明
```text
class MonsterInformationProvider
```

- 字段候选数: 0

- 方法/构造器候选数: 15
```text
public static MonsterInformationProvider getInstance()
protected MonsterInformationProvider()
public final List<MonsterGlobalDropEntry> getRelevantGlobalDrops(int mapid)
private void retrieveGlobal()
public List<MonsterDropEntry> retrieveEffectiveDrop(final int monsterId)
public final List<MonsterDropEntry> retrieveDrop(final int monsterId)
public final List<Integer> retrieveDropPool(final int monsterId)
public final void setMobAttackAnimationTime(int monsterId, int attackPos, int animationTime)
public final Integer getMobAttackAnimationTime(int monsterId, int attackPos)
public final void setMobSkillAnimationTime(MobSkill skill, int animationTime)
public final Integer getMobSkillAnimationTime(MobSkill skill)
public final void setMobAttackInfo(int monsterId, int attackPos, int mpCon, int coolTime)
public boolean isBoss(int id)
public String getMobNameFromId(int id)
public final void clearDrops()
```

---

## `org.gms.server.life` / `server/life/MonsterListener.java`

### 类型声明
```text
interface MonsterListener
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.life` / `server/life/MonsterStats.java`

### 类型声明
```text
class MonsterStats
```

- 字段候选数: 12
```text
public boolean changeable
public String name
public BanishInfo banish = null
public List<loseItem> loseItem = null
public selfDestruction selfDestruction = null
public int fixedStance = 0
public boolean friendly
public int bboxMinX = 0
public int bboxMinY = 0
public int bboxMaxX = 0
public int bboxMaxY = 0
public boolean bboxValid = false
```

- 方法/构造器候选数: 83
```text
public void setChange(boolean change)
public boolean isChangeable()
public int getExp()
public void setExp(int exp)
public int getHp()
public void setHp(int hp)
public int getMp()
public void setMp(int mp)
public int getLevel()
public void setLevel(int level)
public int removeAfter()
public void setRemoveAfter(int removeAfter)
public int getDropPeriod()
public void setDropPeriod(int dropPeriod)
public void setBoss(boolean boss)
public boolean isBoss()
public void setFfaLoot(boolean ffaLoot)
public boolean isFfaLoot()
public void setAnimationTime(String name, int delay)
public int getAnimationTime(String name)
public boolean isMobile()
public List<Integer> getRevives()
public void setRevives(List<Integer> revives)
public void setUndead(boolean undead)
public boolean isUndead()
public void setEffectiveness(Element e, ElementalEffectiveness ee)
public ElementalEffectiveness getEffectiveness(Element e)
public String getName()
public void setName(String name)
public byte getTagColor()
public void setTagColor(int tagColor)
public byte getTagBgColor()
public void setTagBgColor(int tagBgColor)
public void setSkills(Set<MobSkillId> skills)
public Set<MobSkillId> getSkills()
public int getNoSkills()
public boolean hasSkill(int skillId, int level)
public void setFirstAttack(boolean firstAttack)
public boolean isFirstAttack()
public void setBuffToGive(int buff)
public int getBuffToGive()
void removeEffectiveness(Element e)
public BanishInfo getBanishInfo()
public void setBanishInfo(BanishInfo banish)
public int getPADamage()
public void setPADamage(int PADamage)
public int getCP()
public void setCP(int cp)
public List<loseItem> loseItem()
public void addLoseItem(loseItem li)
public selfDestruction selfDestruction()
public void setSelfDestruction(selfDestruction sd)
public void setExplosiveReward(boolean isExplosiveReward)
public boolean isExplosiveReward()
public void setRemoveOnMiss(boolean removeOnMiss)
public boolean removeOnMiss()
public void setCool(Pair<Integer, Integer> cool)
public int getPDDamage()
public int getMADamage()
public int getMDDamage()
public boolean isFriendly()
public void setFriendly(boolean value)
public void setPDDamage(int PDDamage)
public void setMADamage(int MADamage)
public void setMDDamage(int MDDamage)
public int getFixedStance()
public void setFixedStance(int stance)
public int getMovetype()
public void setMovetype(int movetype)
public void setImgwidth(int imgwidth)
public void setImgheight(int imgheight)
public int getImgwidth()
public int getImgheight()
public void setBbox(int minX, int minY, int maxX, int maxY)
public boolean hasBbox()
public int getBboxMinX()
public int getBboxMinY()
public int getBboxMaxX()
public int getBboxMaxY()
public int getBboxWidth()
public int getBboxHeight()
public boolean isLargeSize()
public MonsterStats copy()
```

---

## `org.gms.server.life` / `server/life/NPC.java`

### 类型声明
```text
class NPC
```

- 字段候选数: 1
```text
private final NPCStats stats
```

- 方法/构造器候选数: 7
```text
public NPC(int id, NPCStats stats)
public boolean hasShop()
public void sendShop(Client c)
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public MapObjectType getType()
public String getName()
```

---

## `org.gms.server.life` / `server/life/NPCStats.java`

### 类型声明
```text
class NPCStats
```

- 字段候选数: 1
```text
private String name
```

- 方法/构造器候选数: 3
```text
public NPCStats(String name)
public String getName()
public void setName(String name)
```

---

## `org.gms.server.life` / `server/life/OverrideMonsterStats.java`

### 类型声明
```text
class OverrideMonsterStats
```

- 字段候选数: 1
```text
public int hp
```

- 方法/构造器候选数: 9
```text
public OverrideMonsterStats()
public OverrideMonsterStats(int hp, int mp, int exp, boolean change)
public OverrideMonsterStats(int hp, int mp, int exp)
public int getExp()
public void setOExp(int exp)
public int getHp()
public void setOHp(int hp)
public int getMp()
public void setOMp(int mp)
```

---

## `org.gms.server.life` / `server/life/PlayerNPC.java`

### 类型声明
```text
class PlayerNPC
```

- 字段候选数: 12
```text
private int scriptId
private int face
private int hair
private int gender
private int job
private byte skin
private String name = ""
private int dir
private int FH
private int RX0
private int RX1
private int CY
```

- 方法/构造器候选数: 24
```text
public PlayerNPC(String name, int scriptId, int face, int hair, int gender, byte skin, Map<Short, Integer> equips, int dir, int FH, int RX0, int RX1, int CX, int CY, int oid)
public PlayerNPC(PlayernpcsDO npcDO, List<PlayernpcsEquipDO> equipDOList)
public static void loadRunningRankData(int worlds)
public int getWorldRank()
public int getOverallRank()
public int getWorldJobRank()
public int getOverallJobRank()
public MapObjectType getType()
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
private static int getAndIncrementRunningWorldJobRanks(int world, int job)
public static boolean canSpawnPlayerNpc(String name, int mapid)
public void updatePlayerNPCPosition(MapleMap map, Point newPos)
private static void fetchAvailableScriptIdsFromDb(byte branch, List<Integer> list)
private static int getNextScriptId(byte branch)
private static PlayerNPC createPlayerNPCInternal(MapleMap map, Point pos, Character chr)
private static List<Integer> removePlayerNPCInternal(MapleMap map, Character chr)
public static boolean spawnPlayerNPC(int mapid, Character chr)
public static boolean spawnPlayerNPC(int mapid, Point pos, Character chr)
private static PlayerNPC getPlayerNPCFromWorldMap(String name, int world, int map)
public static void removePlayerNPC(Character chr)
public static void multicastSpawnPlayerNPC(int mapid, int world)
public static void removeAllPlayerNPC()
public static void addPlayerNPCMapObject(MapleMap map)
```

---

## `org.gms.server.life` / `server/life/PlayerNPCFactory.java`

### 类型声明
```text
class PlayerNPCFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public synchronized static boolean isExistentScriptid(int scriptid)
```

---

## `org.gms.server.life` / `server/life/SpawnPoint.java`

### 类型声明
```text
class SpawnPoint
```

- 字段候选数: 10
```text
private final int monster
private final int mobTime
private final int team
private final int fh
private final int f
private final Point pos
private long nextPossibleSpawn
private int mobInterval = 5000
private final boolean immobile
private boolean denySpawn = false
```

- 方法/构造器候选数: 13
```text
public SpawnPoint(final Monster monster, Point pos, boolean immobile, int mobTime, int mobInterval, int team)
public int getSpawned()
public void setDenySpawn(boolean val)
public boolean getDenySpawn()
public boolean shouldSpawn()
public boolean shouldForceSpawn()
public Monster getMonster()
public int getMonsterId()
public Point getPosition()
public final int getF()
public final int getFh()
public int getMobTime()
public int getTeam()
```

---

## `org.gms.server.life.positioner` / `server/life/positioner/PlayerNPCPodium.java`

### 类型声明
```text
class PlayerNPCPodium
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
private static int getPlatformPosX(int platform)
private static int getPlatformPosY(int platform)
private static Point calcNextPos(int rank, int step)
private static Point rearrangePlayerNpcs(MapleMap map, int newStep, List<PlayerNPC> pnpcs)
private static Point reorganizePlayerNpcs(MapleMap map, int newStep, List<MapObject> mmoList)
private static int encodePodiumData(int podiumStep, int podiumCount)
private static Point getNextPlayerNpcPosition(MapleMap map, int podiumData)
public static Point getNextPlayerNpcPosition(MapleMap map)
```

---

## `org.gms.server.life.positioner` / `server/life/positioner/PlayerNPCPositioner.java`

### 类型声明
```text
class PlayerNPCPositioner
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
private static boolean isPlayerNpcNearby(List<Point> otherPos, Point searchPos, int xLimit, int yLimit)
private static int calcDx(int newStep)
private static int calcDy(int newStep)
private static List<Point> rearrangePlayerNpcPositions(MapleMap map, int newStep, int pnpcsSize)
private static Point rearrangePlayerNpcs(MapleMap map, int newStep, List<PlayerNPC> pnpcs)
private static Point reorganizePlayerNpcs(MapleMap map, int newStep, List<MapObject> mmoList)
private static Point getNextPlayerNpcPosition(MapleMap map, int initStep)
public static Point getNextPlayerNpcPosition(MapleMap map)
```

---

## `org.gms.server.loot` / `server/loot/LootInventory.java`

### 类型声明
```text
class LootInventory
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public LootInventory(Character from)
public int hasItem(int itemid, int quantity)
```

---

## `org.gms.server.loot` / `server/loot/LootManager.java`

### 类型声明
```text
class LootManager
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
private static boolean isRelevantDrop(MonsterDropEntry dropEntry, List<Character> players, List<LootInventory> playersInv)
public static List<MonsterDropEntry> retrieveRelevantDrops(int monsterId, List<Character> players)
```

---

## `org.gms.server.maps` / `server/maps/AbstractAnimatedMapObject.java`

### 类型声明
```text
class AbstractAnimatedMapObject
```

- 字段候选数: 2
```text
public static final int IDLE_MOVEMENT_PACKET_LENGTH = 15
private int stance
```

- 方法/构造器候选数: 5
```text
public int getStance()
public void setStance(int stance)
public boolean isFacingLeft()
public InPacket getIdleMovement()
private static Packet createIdleMovementPacket()
```

---

## `org.gms.server.maps` / `server/maps/AbstractMapObject.java`

### 类型声明
```text
class AbstractMapObject
```

- 字段候选数: 1
```text
private int objectId
```

- 方法/构造器候选数: 5
```text
public Point getPosition()
public void setPosition(Point position)
public int getObjectId()
public void setObjectId(int id)
public void nullifyPosition()
```

---

## `org.gms.server.maps` / `server/maps/AnimatedMapObject.java`

### 类型声明
```text
interface AnimatedMapObject
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.maps` / `server/maps/Door.java`

### 类型声明
```text
class Door
```

- 字段候选数: 8
```text
private int ownerId
private MapleMap town
private Portal townPortal
private final MapleMap target
private long deployTime
private boolean active
private DoorObject townDoor
private DoorObject areaDoor
```

- 方法/构造器候选数: 14
```text
public Door(Character owner, Point targetPosition)
public void updateDoorPortal(Character owner)
private void broadcastRemoveDoor(Character owner)
public static void attemptRemoveDoor(final Character owner)
private Portal getTownDoorPortal(int doorid)
public int getOwnerId()
public DoorObject getTownDoor()
public DoorObject getAreaDoor()
public MapleMap getTown()
public Portal getTownPortal()
public MapleMap getTarget()
public long getElapsedDeployTime()
private boolean dispose()
public boolean isActive()
```

---

## `org.gms.server.maps` / `server/maps/DoorObject.java`

### 类型声明
```text
class DoorObject
```

- 字段候选数: 8
```text
private final int ownerId
private int pairOid
private final MapleMap from
private final MapleMap to
private int linkedPortalId
private Point linkedPos
private final Lock rlock
private final Lock wlock
```

- 方法/构造器候选数: 20
```text
public DoorObject(int owner, MapleMap destination, MapleMap origin, int townPortalId, Point targetPosition, Point toPosition)
public void update(int townPortalId, Point toPosition)
private int getLinkedPortalId()
private Point getLinkedPortalPosition()
public void warp(final Character chr)
public void sendSpawnData(Client client)
public void sendSpawnData(Client client, boolean launched)
public void sendDestroyData(Client client)
public void sendDestroyData(Client client, boolean partyUpdate)
public int getOwnerId()
public void setPairOid(int oid)
public int getPairOid()
public boolean inTown()
public MapleMap getFrom()
public MapleMap getTo()
public MapleMap getTown()
public MapleMap getArea()
public Point getAreaPosition()
public Point toPosition()
public MapObjectType getType()
```

---

## `org.gms.server.maps` / `server/maps/Dragon.java`

### 类型声明
```text
class Dragon
```

- 字段候选数: 1
```text
private final Character owner
```

- 方法/构造器候选数: 6
```text
public Dragon(Character chr)
public MapObjectType getType()
public void sendSpawnData(Client client)
public int getObjectId()
public void sendDestroyData(Client c)
public Character getOwner()
```

---

## `org.gms.server.maps` / `server/maps/FieldLimit.java`

### 类型声明
```text
enum FieldLimit
```

- 字段候选数: 1
```text
private final long i
```

- 方法/构造器候选数: 14
```text
JUMP(0x01),
MOVEMENTSKILLS(0x02),
SUMMON(0x04),
DOOR(0x08),
CANNOTMIGRATE(0x10),    //change channel, town portal scroll, access cash shop, etc etc
CANNOTVIPROCK(0x40),
CANNOTMINIGAME(0x80),
CANNOTUSEMOUNTS(0x200),
CANNOTUSEPOTION(0x1000),
CANNOTJUMPDOWN(0x20000),
NO_EXP_DECREASE(0x80000),
FieldLimit(long i)
public long getValue()
public boolean check(int fieldlimit)
```

---

## `org.gms.server.maps` / `server/maps/Foothold.java`

### 类型声明
```text
class Foothold
```

- 字段候选数: 3
```text
private final Point p1
private final Point p2
private final int id
```

- 方法/构造器候选数: 13
```text
public Foothold(Point p1, Point p2, int id)
public boolean isWall()
public int getX1()
public int getX2()
public int getY1()
public int getY2()
public int calculateFooting(int x)
public int compareTo(Foothold o)
public int getId()
public int getNext()
public void setNext(int next)
public int getPrev()
public void setPrev(int prev)
```

---

## `org.gms.server.maps` / `server/maps/FootholdTree.java`

### 类型声明
```text
class FootholdTree
```

- 字段候选数: 11
```text
private FootholdTree nw = null
private FootholdTree ne = null
private FootholdTree sw = null
private FootholdTree se = null
private final Point p1
private final Point p2
private final Point center
private int depth = 0
private static final int maxDepth = 8
private int maxDropX
private int minDropX
```

- 方法/构造器候选数: 14
```text
public FootholdTree(Point p1, Point p2)
public FootholdTree(Point p1, Point p2, int depth)
public void insert(Foothold f)
private List<Foothold> getRelevants(Point p)
private List<Foothold> getRelevants(Point p, List<Foothold> list)
private Foothold findWallR(Point p1, Point p2)
public Foothold findWall(Point p1, Point p2)
public Foothold findBelow(Point p)
public int getX1()
public int getX2()
public int getY1()
public int getY2()
public int getMaxDropX()
public int getMinDropX()
```

---

## `org.gms.server.maps` / `server/maps/GenericPortal.java`

### 类型声明
```text
class GenericPortal
```

- 字段候选数: 10
```text
private String name
private String target
private Point position
private int targetmap
private final int type
private boolean status = true
private int id
private String scriptName
private boolean portalState
private Lock scriptLock = null
```

- 方法/构造器候选数: 19
```text
public GenericPortal(int type)
public int getId()
public void setId(int id)
public String getName()
public Point getPosition()
public String getTarget()
public void setPortalStatus(boolean newStatus)
public boolean getPortalStatus()
public int getTargetMapId()
public int getType()
public String getScriptName()
public void setName(String name)
public void setPosition(Point position)
public void setTarget(String target)
public void setTargetMapId(int targetmapid)
public void setScriptName(String scriptName)
public void enterPortal(Client c)
public void setPortalState(boolean state)
public boolean getPortalState()
```

---

## `org.gms.server.maps` / `server/maps/HiredMerchant.java`

### 类型声明
```text
class HiredMerchant
class SoldItem
```

- 字段候选数: 13
```text
private static final int VISITOR_HISTORY_LIMIT = 10
private static final int BLACKLIST_LIMIT = 20
private final int ownerId
private final int itemId
private final int mesos = 0
private final int channel
private final int world
private final long start
private String ownerName = ""
private String description = ""
private boolean published = false
private MapleMap map
private final Visitor[] visitors = new Visitor[3]
```

- 方法/构造器候选数: 59
```text
private record Visitor(Character chr, Instant enteredAt)
public record PastVisitor(String chrName, Duration visitDuration)
public HiredMerchant(final Character owner, String desc, int itemId)
public void broadcastToVisitorsThreadsafe(Packet packet)
private void broadcastToVisitors(Packet packet)
public byte[] getShopRoomInfo()
public boolean addVisitor(Character visitor)
public void removeVisitor(Character chr)
private void addVisitorToHistory(Visitor visitor)
public int getVisitorSlotThreadsafe(Character visitor)
private int getVisitorSlot(Character visitor)
private void removeAllVisitors()
private void removeOwner(Character owner)
public void withdrawMesos(Character chr)
public void takeItemBack(int slot, Character chr)
private static boolean canBuy(Client c, Item newItem)
private int getQuantityLeft(int itemid)
public void buy(Client c, int item, short quantity)
private void announceItemSold(Item item, int mesos, int inStore)
public void forceClose()
public void closeOwnerMerchant(Character chr)
private void closeShop(Client c, boolean timeout)
public synchronized void visitShop(Character chr)
public String getOwner()
public void clearItems()
public int getOwnerId()
public String getDescription()
public Character[] getVisitorCharacters()
public List<PlayerShopItem> getItems()
public boolean hasItem(int itemid)
public boolean addItem(PlayerShopItem item)
public void clearInexistentItems()
private void removeFromSlot(int slot)
private int getFreeSlot()
public void setDescription(String description)
public boolean isPublished()
public boolean isOpen()
public void setOpen(boolean set)
public int getItemId()
public boolean isOwner(Character chr)
public void sendMessage(Character chr, String msg)
public List<PlayerShopItem> sendAvailableBundles(int itemid)
public void saveItems(boolean shutdown) throws SQLException
private static boolean check(Character chr, List<PlayerShopItem> items)
public int getChannel()
public int getTimeOpen()
public void clearMessages()
public List<PastVisitor> getVisitorHistory()
public void addToBlacklist(String chrName)
public void removeFromBlacklist(String chrName)
public Set<String> getBlacklist()
private boolean isBlacklisted(String chrName)
public int getMapId()
public MapleMap getMap()
public List<SoldItem> getSold()
public int getMesos()
public MapObjectType getType()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
```

---

## `org.gms.server.maps` / `server/maps/Kite.java`

### 类型声明
```text
class Kite
```

- 字段候选数: 5
```text
private final Point pos
private final Character owner
private final String text
private final int ft
private final int itemid
```

- 方法/构造器候选数: 9
```text
public Kite(Character owner, String text, int itemId)
public MapObjectType getType()
public Point getPosition()
public Character getOwner()
public void setPosition(Point position)
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public final Packet makeSpawnData()
public final Packet makeDestroyData()
```

---

## `org.gms.server.maps` / `server/maps/MapEffect.java`

### 类型声明
```text
class MapEffect
```

- 字段候选数: 3
```text
private final String msg
private final int itemId
private final boolean active = true
```

- 方法/构造器候选数: 4
```text
public MapEffect(String msg, int itemId)
public final Packet makeDestroyData()
public final Packet makeStartData()
public void sendStartData(Client client)
```

---

## `org.gms.server.maps` / `server/maps/MapFactory.java`

### 类型声明
```text
class MapFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 14
```text
private static void loadLifeFromWz(MapleMap map, Data mapData)
private static void loadLifeFromDb(MapleMap map)
private static void loadLifeRaw(MapleMap map, int id, String type, int cy, int f, int fh, int rx0, int rx1, int x, int y, int hide, int mobTime, int team)
public static MapleMap loadMapFromWz(int mapid, int world, int channel, EventInstanceManager event)
private static AbstractLoadedLife loadLife(int id, String type, int cy, int f, int fh, int rx0, int rx1, int x, int y, int hide)
private static Reactor loadReactor(Data reactor, String id, final byte FacingDirection)
private static String getMapName(int mapid)
private static String getMapStringName(int mapid)
public static String loadPlaceName(int mapid)
public static String loadStreetName(int mapid)
public static String getMapIdByLifeId(int lifeId)
private static String resolveDir(DataEntry dataEntry, int lifeId)
private static String resolveFile(DataEntity dataEntry, int lifeId)
private static void resolvePath(DataEntity dataEntry, StringBuilder pathBuilder)
```

---

## `org.gms.server.maps` / `server/maps/MapItem.java`

### 类型声明
```text
class MapItem
```

- 字段候选数: 6
```text
protected Client ownerClient
protected Item item
protected MapObject dropper
protected byte type
protected boolean pickedUp = false, playerDrop, partyDrop
protected long dropTime
```

- 方法/构造器候选数: 28
```text
public MapItem(Item item, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop)
public MapItem(Item item, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop, int questid)
public MapItem(int meso, Point position, MapObject dropper, Character owner, Client ownerClient, byte type, boolean playerDrop)
public final Item getItem()
public final int getQuest()
public final int getItemId()
public final MapObject getDropper()
public final int getOwnerId()
public final int getPartyOwnerId()
public final void setPartyOwnerId(int partyid)
public final int getClientsideOwnerId()
public final boolean hasClientsideOwnership(Character player)
public final boolean isFFADrop()
public final boolean hasExpiredOwnershipTime()
public final boolean canBePickedBy(Character chr)
public final Client getOwnerClient()
public final int getMeso()
public final boolean isPlayerDrop()
public final boolean isPickedUp()
public void setPickedUp(final boolean pickedUp)
public long getDropTime()
public void setDropTime(long time)
public byte getDropType()
public void lockItem()
public void unlockItem()
public final MapObjectType getType()
public void sendSpawnData(final Client client)
public void sendDestroyData(final Client client)
```

---

## `org.gms.server.maps` / `server/maps/MapManager.java`

### 类型声明
```text
class MapManager
```

- 字段候选数: 5
```text
private final int channel
private final int world
private EventInstanceManager event
private final Lock mapsRLock
private final Lock mapsWLock
```

- 方法/构造器候选数: 9
```text
public MapManager(EventInstanceManager eim, int world, int channel)
public MapleMap resetMap(int mapid)
private synchronized MapleMap loadMapFromWz(int mapid, boolean cache)
public MapleMap getMap(int mapid)
public MapleMap getMapByLifeId(int lifeId)
public MapleMap getDisposableMap(int mapid)
public boolean isMapLoaded(int mapId)
public void updateMaps()
public void dispose()
```

---

## `org.gms.server.maps` / `server/maps/MapMonitor.java`

### 类型声明
```text
class MapMonitor
```

- 字段候选数: 3
```text
private ScheduledFuture<?> monitorSchedule
private MapleMap map
private Portal portal
```

- 方法/构造器候选数: 2
```text
public MapMonitor(final MapleMap map, String portal)
private void cancelAction()
```

---

## `org.gms.server.maps` / `server/maps/MapObject.java`

### 类型声明
```text
interface MapObject
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.maps` / `server/maps/MapObjectType.java`

### 类型声明
```text
enum MapObjectType
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.maps` / `server/maps/MapPortal.java`

### 类型声明
```text
class MapPortal
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public MapPortal()
```

---

## `org.gms.server.maps` / `server/maps/MapleMap.java`

### 类型声明
```text
class MapleMap
class MobLootEntry
class ActivateItemReactor
interface DelayedPacketCreation
interface SpawnCondition
```

- 字段候选数: 51
```text
private FootholdTree footholds = null
private final int mapid
private final int returnMapId
private final int channel
private final int world
private int seats
private byte monsterRate
private boolean clock
private boolean boat
private boolean docked = false
private EventInstanceManager event = null
private String mapName
private String streetName
private MapEffect mapEffect = null
private boolean everlast = false
private int forcedReturnMap = MapId.NONE
private int timeLimit
private long mapTimer
private int decHP = 0
private float recovery = 1.0f
private int protectItem = 0
private boolean town
private OxQuiz ox
private boolean isOxQuiz = false
private boolean dropsOn = true
private String onFirstUserEnter
private String onUserEnter
private int fieldType
private int fieldLimit = 0
private int mobCapacity = -1
private ScheduledFuture<?> itemMonitor = null
private ScheduledFuture<?> expireItemsTask = null
private ScheduledFuture<?> mobSpawnLootTask = null
private ScheduledFuture<?> characterStatUpdateTask = null
private short itemMonitorTimeout
private short mobInterval = 5000
private Character mapOwner = null
private long mapOwnerLastActivityTime = Long.MAX_VALUE
private boolean eventstarted = false, isMuted = false
private Snowball snowball0 = null
private Snowball snowball1 = null
private Coconut coconut
private int maxMobs
private int maxReactors
private int deathCP
private int timeDefault
private int timeExpand
private final Lock chrRLock
private final Lock chrWLock
private final Lock objectRLock
private final Lock objectWLock
```

- 方法/构造器候选数: 356
```text
public MapleMap(int mapid, int world, int channel, int returnMapId, float monsterRate)
public void setEventInstance(EventInstanceManager eim)
public EventInstanceManager getEventInstance()
public Rectangle getMapArea()
public int getWorld()
public void broadcastPacket(Character source, Packet packet)
public void broadcastGMPacket(Character source, Packet packet)
private void broadcastPacket(Packet packet, Predicate<Character> chrFilter)
public void toggleDrops()
private static double getRangedDistance()
public List<MapObject> getMapObjectsInRect(Rectangle box, List<MapObjectType> types)
public int getId()
public Channel getChannelServer()
public World getWorldServer()
public MapleMap getReturnMap()
public int getReturnMapId()
public MapleMap getForcedReturnMap()
public int getForcedReturnId()
public void setForcedReturnMap(int map)
public int getTimeLimit()
public void setTimeLimit(int timeLimit)
public int getTimeLeft()
public void setReactorState()
public final void limitReactor(final int rid, final int num)
public boolean isAllReactorState(final int reactorId, final int state)
public int getCurrentPartyId()
public void addPlayerNPCMapObject(PlayerNPC pnpcobject)
public void addMapObject(MapObject mapobject)
public void addSelfDestructive(Monster mob)
public boolean removeSelfDestructive(int mapobjectid)
private void spawnAndAddRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery)
private void spawnAndAddRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery, SpawnCondition condition)
private void spawnRangedMapObject(MapObject mapobject, DelayedPacketCreation packetbakery, SpawnCondition condition)
private int getUsableOID()
public void removeMapObject(int num)
public void removeMapObject(final MapObject obj)
private Point calcPointBelow(Point initial)
public void generateMapDropRangeCache()
private Point bsearchDropPos(Point initial, Point fallback)
public Point calcDropPos(Point initial, Point fallback)
public boolean canDeployDoor(Point pos)
private static double getAngle(Point doorPoint, Point spawnPoint)
public static String getRoundedCoordinate(double angle)
private static void sortDropEntries(List<MonsterDropEntry> from, List<MonsterDropEntry> item, List<MonsterDropEntry> visibleQuest, List<MonsterDropEntry> otherQuest, Character chr)
private byte dropItemsFromMonsterOnMap(List<MonsterDropEntry> dropEntry, Point pos, byte d, float chRate, byte droptype, int mobpos, Character chr, Monster mob)
private byte dropGlobalItemsFromMonsterOnMap(List<MonsterGlobalDropEntry> globalEntry, Point pos, byte d, byte droptype, int mobpos, Character chr, Monster mob)
private void dropFromMonster(final Character chr, final Monster mob, final boolean useBaseRate)
public void dropItemsFromMonster(List<MonsterDropEntry> list, final Character chr, final Monster mob)
public void dropFromFriendlyMonster(final Character chr, final Monster mob)
public void dropFromReactor(final Character chr, final Reactor reactor, Item drop, Point dropPos, short questid)
private void stopItemMonitor()
private void cleanItemMonitor()
private void startItemMonitor()
private boolean hasItemMonitor()
public int getDroppedItemCount()
private void instantiateItemDrop(MapItem mdrop)
private void registerItemDrop(MapItem mdrop)
private void unregisterItemDrop(MapItem mdrop)
private void makeDisappearExpiredItemDrops()
private void registerMobItemDrops(byte droptype, int mobpos, float chRate, Point pos, List<MonsterDropEntry> dropEntry, List<MonsterDropEntry> visibleQuestEntry, List<MonsterDropEntry> otherQuestEntry, List<MonsterGlobalDropEntry> globalEntry, Character chr, Monster mob)
private void spawnMobItemDrops()
private List<MapItem> getDroppedItems()
public int getDroppedItemsCountById(int itemid)
public void pickItemDrop(Packet pickupPacket, MapItem mdrop)
public List<MapItem> updatePlayerItemDropsToParty(int partyid, int charid, List<Character> partyMembers, Character partyLeaver)
public void updatePartyItemDropsToNewcomer(Character newcomer, List<MapItem> partyItems)
private void spawnDrop(final Item idrop, final Point dropPos, final MapObject dropper, final Character chr, final byte droptype, final short questid)
public final void spawnMesoDrop(final int meso, final Point position, final MapObject dropper, final Character owner, final boolean playerDrop, final byte droptype)
public final void disappearingItemDrop(final MapObject dropper, final Character owner, final Item item, final Point pos)
public final void disappearingMesoDrop(final int meso, final MapObject dropper, final Character owner, final Point pos)
public Monster getMonsterById(int id)
public int countMonster(int id)
public int countMonster(int minid, int maxid)
public int countMonsters()
public int countReactors()
public final List<MapObject> getReactors()
public final List<MapObject> getMonsters()
public final List<Reactor> getAllReactors()
public final List<Monster> getAllMonsters()
public int countItems()
public final List<MapObject> getItems()
public int countPlayers()
public List<MapObject> getPlayers()
public List<Character> getAllPlayers()
public List<Character> getPlayersInRange(Rectangle box)
public int countAlivePlayers()
public int countBosses()
public boolean damageMonster(final Character chr, final Monster monster, final int damage)
public void broadcastBalrogVictory(String leaderName)
public void broadcastHorntailVictory()
public void broadcastZakumVictory()
public void broadcastPinkBeanVictory(int channel)
private boolean removeKilledMonsterObject(Monster monster)
public void killMonster(final Monster monster, final Character chr, final boolean withDrops)
public void killMonster(final Monster monster, final Character chr, final boolean withDrops, int animation)
public void killFriendlies(Monster mob)
public void killMonster(int mobId)
public void killMonsterWithDrops(int mobId)
public void softKillAllMonsters()
public void killAllMonstersNotFriendly()
public void killAllMonsters()
public final void destroyReactors(final int first, final int last)
public void destroyReactor(int oid)
public void resetReactors()
public final void resetReactors(List<Reactor> list)
public void shuffleReactors()
public final void shuffleReactors(int first, int last)
public final void shuffleReactors(List<Object> list)
public List<MapObject> getMapObjects()
public NPC getNPCById(int id)
public boolean containsNPC(int npcid)
public void destroyNPC(int npcid)
public MapObject getMapObject(int oid)
public Monster getMonsterByOid(int oid)
public Reactor getReactorByOid(int oid)
public Reactor getReactorById(int Id)
public List<Reactor> getReactorsByIdRange(final int first, final int last)
public Reactor getReactorByName(String name)
public void spawnMonsterOnGroundBelow(int id, int x, int y)
public void spawnMonsterOnGroundBelow(Monster mob, Point pos)
public void spawnCPQMonster(Monster mob, Point pos, int team)
private void monsterItemDrop(final Monster m, long delay)
public void spawnFakeMonsterOnGroundBelow(Monster mob, Point pos)
public Point getGroundBelow(Point pos)
public Point getPointBelow(Point pos)
public void spawnRevives(final Monster monster)
private void applyRemoveAfter(final Monster monster)
public void dismissRemoveAfter(final Monster monster)
private List<SpawnPoint> getMonsterSpawn()
private List<SpawnPoint> getAllMonsterSpawn()
public void spawnAllMonsterIdFromMapSpawnList(int id)
public void spawnAllMonsterIdFromMapSpawnList(int id, int difficulty, boolean isPq)
public void spawnAllMonstersFromMapSpawnList()
public void spawnAllMonstersFromMapSpawnList(int difficulty, boolean isPq)
public void spawnMonster(final Monster monster)
public void spawnMonster(final Monster monster, int difficulty, boolean isPq)
public void spawnDojoMonster(final Monster monster)
public void spawnMonsterWithEffect(final Monster monster, final int effect, Point pos)
public void spawnFakeMonster(final Monster monster)
public void makeMonsterReal(final Monster monster)
public void spawnReactor(final Reactor reactor)
public void spawnDoor(final DoorObject door)
public Portal getDoorPortal(int doorid)
public void spawnSummon(final Summon summon)
public void spawnMist(final Mist mist, final int duration, boolean poison, boolean fake, boolean recovery)
public void spawnKite(final Kite kite)
public final void spawnItemDrop(final MapObject dropper, final Character owner, final Item item, Point pos, final boolean ffaDrop, final boolean playerDrop)
public final void spawnItemDrop(final MapObject dropper, final Character owner, final Item item, Point pos, final byte dropType, final boolean playerDrop)
public final void spawnItemDropList(List<Integer> list, final MapObject dropper, final Character owner, Point pos)
public final void spawnItemDropList(List<Integer> list, int minCopies, int maxCopies, final MapObject dropper, final Character owner, Point pos)
public final void spawnItemDropList(List<Integer> list, int minCopies, int maxCopies, final MapObject dropper, final Character owner, Point pos, final boolean ffaDrop, final boolean playerDrop)
private void registerMapSchedule(Runnable r, long delay)
private void activateItemReactors(final MapItem drop, final Client c)
public void searchItemReactors(final Reactor react)
public void changeEnvironment(String mapObj, int newState)
public void startMapEffect(String msg, int itemId)
public void startMapEffect(String msg, int itemId, long time)
public Character getAnyCharacterFromParty(int partyid)
private void addPartyMemberInternal(Character chr, int partyid)
private void removePartyMemberInternal(Character chr, int partyid)
public void addPartyMember(Character chr, int partyid)
public void removePartyMember(Character chr, int partyid)
public void removeParty(int partyid)
public void addPlayer(final Character chr)
private static void announcePlayerDiseases(final Client c)
public Portal getRandomPlayerSpawnpoint()
public Portal findClosestTeleportPortal(Point from)
public Portal findClosestPlayerSpawnpoint(Point from)
public Portal findClosestPortal(Point from)
public Portal findMarketPortal()
public void addPlayerPuppet(Character player)
public void removePlayerPuppet(Character player)
public void removePlayer(Character chr)
public void broadcastMessage(Packet packet)
public void broadcastGMMessage(Packet packet)
public void broadcastMessage(Character source, Packet packet, boolean repeatToSource)
public void broadcastMessage(Character source, Packet packet, boolean repeatToSource, boolean ranged)
public void broadcastMessage(Packet packet, Point rangedFrom)
public void broadcastMessage(Character source, Packet packet, Point rangedFrom)
private void broadcastMessage(Character source, Packet packet, double rangeSq, Point rangedFrom)
private boolean chrDisconnected(Iterator<Character> iterator, Character chr)
private void updateBossSpawn(Monster monster)
public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet)
public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet, Point rangedFrom)
private void broadcastBossHpMessage(Monster mm, int bossHash, Character source, Packet packet, double rangeSq, Point rangedFrom)
private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod, Point rangedFrom)
private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod)
private void broadcastItemDropMessage(MapItem mdrop, Point dropperPos, Point dropPos, byte mod, double rangeSq, Point rangedFrom)
public void broadcastSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)
public void broadcastGMSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)
private void broadcastSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField, boolean gmBroadcast)
public void broadcastUpdateCharLookMessage(Character source, Character player)
public void dropMessage(int type, String message)
public void broadcastStringMessage(int type, String message)
private static boolean isNonRangedType(MapObjectType type)
private void sendObjectPlacement(Client c)
public List<MapObject> getMapObjectsInRange(Point from, double rangeSq, List<MapObjectType> types)
public List<MapObject> getMapObjectsInBox(Rectangle box, List<MapObjectType> types)
public void addPortal(Portal myPortal)
public Portal getPortal(String portalname)
public Portal getPortal(int portalid)
public void addMapleArea(Rectangle rec)
public List<Rectangle> getAreas()
public Rectangle getArea(int index)
public void setFootholds(FootholdTree footholds)
public FootholdTree getFootholds()
public void setMapPointBoundings(int px, int py, int h, int w)
public void setMapLineBoundings(int vrTop, int vrBottom, int vrLeft, int vrRight)
public MonsterAggroCoordinator getAggroCoordinator()
public void addMonsterSpawn(Monster monster, int mobTime, int team)
public void addAllMonsterSpawn(Monster monster, int mobTime, int team)
public void removeMonsterSpawn(int mobId, int x, int y)
public void removeAllMonsterSpawn(int mobId, int x, int y)
public void reportMonsterSpawnPoints(Character chr)
public Collection<Character> getCharacters()
public Character getCharacterById(int id)
private static void updateMapObjectVisibility(Character chr, MapObject mo)
public void moveMonster(Monster monster, Point reportedPos)
public void movePlayer(Character player, Point newPosition)
public final void toggleEnvironment(final String ms)
public final void moveEnvironment(final String ms, final int type)
public String getMapName()
public void setMapName(String mapName)
public String getStreetName()
public void setClock(boolean hasClock)
public boolean hasClock()
public void setTown(boolean isTown)
public boolean isTown()
public boolean isMuted()
public void setMuted(boolean mute)
public void setStreetName(String streetName)
public void setEverlast(boolean everlast)
public boolean getEverlast()
public int getSpawnedMonstersOnMap()
public void setMobCapacity(int capacity)
public void setBackgroundTypes(HashMap<Integer, Integer> backTypes)
public void sendNightEffect(Character chr)
public void broadcastNightEffect()
public Character getCharacterByName(String name)
public boolean makeDisappearItemFromMap(MapObject mapobj)
public boolean makeDisappearItemFromMap(MapItem mapitem)
public void instanceMapFirstSpawn(int difficulty, boolean isPq)
public void instanceMapRespawn()
public void instanceMapForceRespawn()
public void closeMapSpawnPoints()
public void restoreMapSpawnPoints()
public void setAllowSpawnPointInBox(boolean allow, Rectangle box)
public void setAllowSpawnPointInRange(boolean allow, Point from, double rangeSq)
public SpawnPoint findClosestSpawnpoint(Point from)
private static double getCurrentSpawnRate(int numPlayers)
private int getNumShouldSpawn(int numPlayers)
public void respawn()
public void mobMpRecovery()
public final int getNumPlayersInArea(final int index)
public final int getNumPlayersInRect(final Rectangle rect)
public final int getNumPlayersItemsInArea(final int index)
public final int getNumPlayersItemsInRect(final Rectangle rect)
public int getHPDec()
public void setHPDec(int delta)
public int getHPDecProtect()
public void setHPDecProtect(int delta)
public float getRecovery()
public void setRecovery(float recRate)
private int hasBoat()
public void setBoat(boolean hasBoat)
public void setDocked(boolean isDocked)
public boolean getDocked()
public void setSeats(int seats)
public int getSeats()
public void broadcastGMMessage(Character source, Packet packet, boolean repeatToSource)
private void broadcastGMMessage(Character source, Packet packet, double rangeSq, Point rangedFrom)
public void broadcastNONGMMessage(Character source, Packet packet, boolean repeatToSource)
public OxQuiz getOx()
public void setOx(OxQuiz set)
public void setOxQuiz(boolean b)
public boolean isOxQuiz()
public void setOnUserEnter(String onUserEnter)
public String getOnUserEnter()
public void setOnFirstUserEnter(String onFirstUserEnter)
public String getOnFirstUserEnter()
private boolean hasForcedEquip()
public void setFieldType(int fieldType)
public void clearDrops(Character player)
public void clearDrops()
public void setFieldLimit(int fieldLimit)
public int getFieldLimit()
public void allowSummonState(boolean b)
public boolean getSummonState()
public void warpEveryone(int to)
public void warpEveryone(int to, int pto)
public void setSnowball(int team, Snowball ball)
public Snowball getSnowball(int team)
private boolean specialEquip()
public void setCoconut(Coconut nut)
public Coconut getCoconut()
public void warpOutByTeam(int team, int mapid)
public void startEvent(final Character chr)
public boolean eventStarted()
public void startEvent()
public void setEventStarted(boolean event)
public String getEventNPC()
public boolean hasEventNPC()
public boolean isStartingEventMap()
public boolean isEventMap()
public void setTimeMob(int id, String msg)
public void toggleHiddenNPC(int id)
public void setMobInterval(short interval)
public short getMobInterval()
public void clearMapObjects()
public final void resetFully()
public void resetMapObjects()
public void resetPQ()
public void resetPQ(int difficulty)
public void resetMapObjects(int difficulty, boolean isPq)
public void broadcastShip(final boolean state)
public void broadcastEnemyShip(final boolean state)
public boolean isHorntailDefeated()
public void spawnHorntailOnGroundBelow(final Point targetPoint)
public boolean claimOwnership(Character chr)
public Character unclaimOwnership()
public boolean unclaimOwnership(Character chr)
private void refreshOwnership()
public boolean isOwnershipRestricted(Character chr)
public void checkMapOwnerActivity()
public List<MCSkill> getBlueTeamBuffs()
public List<MCSkill> getRedTeamBuffs()
public void clearBuffList()
public List<MapObject> getAllPlayer()
public boolean isCPQMap()
public boolean isCPQMap2()
public boolean isCPQLobby()
public boolean isBlueCPQMap()
public boolean isPurpleCPQMap()
public Point getRandomSP(int team)
public GuardianSpawnPoint getRandomGuardianSpawn(int team)
public void addGuardianSpawnPoint(GuardianSpawnPoint a)
public int spawnGuardian(int team, int num)
public void buffMonsters(int team, MCSkill skill)
public final List<Integer> getSkillIds()
public final void addSkillId(int z)
public final void addMobSpawn(int mobId, int spendCP)
public boolean isCPQWinnerMap()
public boolean isCPQLoserMap()
public void runCharacterStatUpdate()
public void registerCharacterStatUpdate(Runnable r)
public void dispose()
public int getMaxMobs()
public void setMaxMobs(int maxMobs)
public int getMaxReactors()
public void setMaxReactors(int maxReactors)
public int getDeathCP()
public void setDeathCP(int deathCP)
public int getTimeDefault()
public void setTimeDefault(int timeDefault)
public int getTimeExpand()
public void setTimeExpand(int timeExpand)
```

---

## `org.gms.server.maps` / `server/maps/MapleTVEffect.java`

### 类型声明
```text
class MapleTVEffect
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static synchronized boolean broadcastMapleTVIfNotActive(Character player, Character victim, List<String> messages, int tvType)
private static synchronized void broadcastTV(boolean activity, final int userWorld, List<String> message, Character user, int type, Character partner)
```

---

## `org.gms.server.maps` / `server/maps/MiniDungeon.java`

### 类型声明
```text
class MiniDungeon
```

- 字段候选数: 3
```text
ScheduledFuture<?> timeoutTask = null
int baseMap
long expireTime
```

- 方法/构造器候选数: 5
```text
public MiniDungeon(int base, long timeLimit)
public boolean registerPlayer(Character chr)
public boolean unregisterPlayer(Character chr)
public void close()
public void dispose()
```

---

## `org.gms.server.maps` / `server/maps/MiniDungeonInfo.java`

### 类型声明
```text
enum MiniDungeonInfo
```

- 字段候选数: 3
```text
private final int baseId
private final int dungeonId
private final int dungeons
```

- 方法/构造器候选数: 18
```text
CAVE_OF_MUSHROOMS(MapId.ANT_TUNNEL_2, MapId.CAVE_OF_MUSHROOMS_BASE, 30), // Horny Mushroom, Zombie Mushroom
GOLEM_CASTLE_RUINS(MapId.SLEEPY_DUNGEON_4, MapId.GOLEMS_CASTLE_RUINS_BASE, 34), // Stone Golem, Mixed Golem
HILL_OF_SANDSTORMS(MapId.SAHEL_2, MapId.HILL_OF_SANDSTORMS_BASE, 30), // Sand Rat
HENESYS_PIG_FARM(MapId.RAIN_FOREST_EAST_OF_HENESYS, MapId.HENESYS_PIG_FARM_BASE, 30), // Pig, Ribbon Pig
DRAKES_BLUE_CAVE(MapId.COLD_CRADLE, MapId.DRAKES_BLUE_CAVE_BASE, 30), // Dark Drake
DRUMMER_BUNNYS_LAIR(MapId.EOS_TOWER_76TH_TO_90TH_FLOOR, MapId.DRUMMER_BUNNYS_LAIR_BASE, 30), // Drumming Bunny
THE_ROUND_TABLE_OF_KENTARUS(MapId.BATTLEFIELD_OF_FIRE_AND_WATER, MapId.ROUND_TABLE_OF_KENTAURUS_BASE, 30), // Blue/Red/Black Kentaurus
THE_RESTORING_MEMORY(MapId.DRAGON_NEST_LEFT_BEHIND, MapId.RESTORING_MEMORY_BASE, 19), // Skelegon, Skelosaurus
NEWT_SECURED_ZONE(MapId.DESTROYED_DRAGON_NEST, MapId.NEWT_SECURED_ZONE_BASE, 19), // Jr. Newtie, Transforming Jr. Newtie
PILLAGE_OF_TREASURE_ISLAND(MapId.RED_NOSE_PIRATE_DEN_2, MapId.PILLAGE_OF_TREASURE_ISLAND_BASE, 30), // Captain
CRITICAL_ERROR(MapId.LAB_AREA_C1, MapId.CRITICAL_ERROR_BASE, 30), // Roid
LONGEST_RIDE_ON_BYEBYE_STATION(MapId.FANTASY_THEME_PARK_3, MapId.LONGEST_RIDE_ON_BYEBYE_STATION, 19); // Froscola, Jester Scarlion
MiniDungeonInfo(int baseId, int dungeonId, int dungeons)
public int getBase()
public int getDungeonId()
public int getDungeons()
public static boolean isDungeonMap(int map)
public static MiniDungeonInfo getDungeon(int map)
```

---

## `org.gms.server.maps` / `server/maps/MiniGame.java`

### 类型声明
```text
class MiniGame
enum MiniGameType
enum MiniGameResult
```

- 字段候选数: 14
```text
private Character owner
private Character visitor
private final String password
private MiniGameType GameType = MiniGameType.UNDEFINED
private int piecetype
private int inprogress = 0
private final int[] piece = new int[250]
private final String description
private int loser = 1
private int firstslot = 0
private int visitorpoints = 0, visitorscore = 0, visitorforfeits = 0, lastvisitor = -1
private int ownerpoints = 0, ownerscore = 0, ownerforfeits = 0
private long nextavailabletie = 0
private int matchestowin = 0
```

- 方法/构造器候选数: 52
```text
public MiniGame(Character owner, String description, String password)
public String getPassword()
public boolean checkPassword(String sentPw)
public boolean hasFreeSlot()
public boolean isOwner(Character chr)
public void addVisitor(Character challenger)
public void closeRoom(boolean forceClose)
public void removeVisitor(boolean forceClose, Character challenger)
public boolean isVisitor(Character challenger)
public void broadcastToOwner(Packet packet)
public void broadcastToVisitor(Packet packet)
public void setFirstSlot(int type)
public int getFirstSlot()
private void updateMiniGameBox()
private synchronized boolean minigameMatchFinish()
private void minigameMatchFinished()
public void minigameMatchStarted()
public void setQuitAfterGame(Character player, boolean quit)
public boolean isMatchInProgress()
public void denyTie(Character chr)
public boolean isTieDenied(Character chr)
public void minigameMatchOwnerWins(boolean forfeit)
public void minigameMatchVisitorWins(boolean forfeit)
public void minigameMatchDraw()
public void setOwnerPoints()
public void setVisitorPoints()
public void setMatchesToWin(int type)
public void setPieceType(int type)
public int getPieceType()
public void setGameType(MiniGameType game)
public MiniGameType getGameType()
public boolean isOmok()
public void shuffleList()
public int getCardId(int slot)
public int getMatchesToWin()
public void setLoser(int type)
public int getLoser()
public void broadcast(Packet packet)
public void chat(Client c, String chat)
public void sendOmok(Client c, int type)
public void sendMatchCard(Client c, int type)
public Character getOwner()
public Character getVisitor()
public void setPiece(int move1, int move2, int type, Character chr)
private boolean searchCombo(int x, int y, int type)
private boolean searchCombo2(int x, int y, int type)
public String getDescription()
public int getOwnerScore()
public int getVisitorScore()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public MapObjectType getType()
```

---

## `org.gms.server.maps` / `server/maps/Mist.java`

### 类型声明
```text
class Mist
```

- 字段候选数: 9
```text
private final Rectangle mistPosition
private Character owner = null
private Monster mob = null
private StatEffect source
private MobSkill skill
private final boolean isMobMist
private boolean isPoisonMist
private boolean isRecoveryMist
private final int skillDelay
```

- 方法/构造器候选数: 19
```text
public Mist(Rectangle mistPosition, Monster mob, MobSkill skill)
public Mist(Rectangle mistPosition, Character owner, StatEffect source)
public MapObjectType getType()
public Point getPosition()
public Skill getSourceSkill()
public boolean isMobMist()
public boolean isPoisonMist()
public boolean isRecoveryMist()
public int getSkillDelay()
public Monster getMobOwner()
public Character getOwner()
public Rectangle getBox()
public void setPosition(Point position)
public final Packet makeDestroyData()
public final Packet makeSpawnData()
public final Packet makeFakeSpawnData(int level)
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public boolean makeChanceResult()
```

---

## `org.gms.server.maps` / `server/maps/PlayerShop.java`

### 类型声明
```text
class PlayerShop
class SoldItem
```

- 字段候选数: 5
```text
private final Character owner
private final int itemid
private final Character[] visitors = new Character[3]
private String description
private int boughtnumber = 0
```

- 方法/构造器候选数: 42
```text
public PlayerShop(Character owner, String description, int itemid)
public int getChannel()
public int getMapId()
public int getItemId()
public boolean isOpen()
public void setOpen(boolean openShop)
public boolean hasFreeSlot()
public byte[] getShopRoomInfo()
public boolean isOwner(Character chr)
private void addVisitor(Character visitor)
public void forceRemoveVisitor(Character visitor)
public void removeVisitor(Character visitor)
public boolean isVisitor(Character visitor)
public boolean addItem(PlayerShopItem item)
private void removeFromSlot(int slot)
private static boolean canBuy(Client c, Item newItem)
public void takeItemBack(int slot, Character chr)
public boolean buy(Client c, int item, short quantity)
public void broadcastToVisitors(Packet packet)
public void broadcastRestoreToVisitors()
public void removeVisitors()
public void broadcast(Packet packet)
private byte getVisitorSlot(Character chr)
public void chat(Client c, String chat)
private void recoverChatLog()
private void clearChatLog()
public void closeShop()
public void sendShop(Client c)
public Character getOwner()
public Character[] getVisitors()
public List<PlayerShopItem> getItems()
public boolean hasItem(int itemid)
public String getDescription()
public void setDescription(String description)
public void banPlayer(String name)
public boolean isBanned(String name)
public synchronized boolean visitShop(Character chr)
public List<PlayerShopItem> sendAvailableBundles(int itemid)
public List<SoldItem> getSold()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public MapObjectType getType()
```

---

## `org.gms.server.maps` / `server/maps/PlayerShopItem.java`

### 类型声明
```text
class PlayerShopItem
```

- 字段候选数: 4
```text
private final Item item
private short bundles
private final int price
private boolean doesExist
```

- 方法/构造器候选数: 7
```text
public PlayerShopItem(Item item, short bundles, int price)
public void setDoesExist(boolean tf)
public boolean isExist()
public Item getItem()
public short getBundles()
public int getPrice()
public void setBundles(short bundles)
```

---

## `org.gms.server.maps` / `server/maps/Portal.java`

### 类型声明
```text
interface Portal
```

- 字段候选数: 5
```text
int TELEPORT_PORTAL = 1
int MAP_PORTAL = 2
int DOOR_PORTAL = 6
boolean OPEN = true
boolean CLOSED = false
```

- 方法/构造器候选数: 0

---

## `org.gms.server.maps` / `server/maps/PortalFactory.java`

### 类型声明
```text
class PortalFactory
```

- 字段候选数: 1
```text
private int nextDoorPortal
```

- 方法/构造器候选数: 3
```text
public PortalFactory()
public Portal makePortal(int type, Data portal)
private void loadPortal(GenericPortal myPortal, Data portal)
```

---

## `org.gms.server.maps` / `server/maps/Reactor.java`

### 类型声明
```text
class Reactor
```

- 字段候选数: 0

- 方法/构造器候选数: 47
```text
public Reactor(ReactorStats stats, int rid)
public void setShouldCollect(boolean collect)
public boolean getShouldCollect()
public void lockReactor()
public void unlockReactor()
public void hitLockReactor()
public void hitUnlockReactor()
public void setState(byte state)
public byte getState()
public void setEventState(byte substate)
public byte getEventState()
public ReactorStats getStats()
public int getId()
public void setDelay(int delay)
public int getDelay()
public MapObjectType getType()
public int getReactorType()
public boolean isRecentHitFromAttack()
public void setMap(MapleMap map)
public MapleMap getMap()
public boolean isAlive()
public boolean isActive()
public void setAlive(boolean alive)
public void sendDestroyData(Client client)
public final Packet makeDestroyData()
public void sendSpawnData(Client client)
public final Packet makeSpawnData()
public void resetReactorActions(int newState)
public void forceHitReactor(final byte newState)
private void tryForceHitReactor(final byte newState)
public void cancelReactorTimeout()
private void refreshReactorTimeout()
public void delayedHitReactor(final Client c, long delay)
public void hitReactor(Client c)
public void hitReactor(boolean wHit, int charPos, short stance, int skillid, Client c)
public boolean destroy()
private void respawn()
public void delayedRespawn()
public boolean forceDelayedRespawn()
public boolean inDelayedRespawn()
public Rectangle getArea()
public String getName()
public void setName(String name)
public GuardianSpawnPoint getGuardian()
public void setGuardian(GuardianSpawnPoint guardian)
public final void setFacingDirection(final byte facingDirection)
public final byte getFacingDirection()
```

---

## `org.gms.server.maps` / `server/maps/ReactorDropEntry.java`

### 类型声明
```text
class ReactorDropEntry
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public ReactorDropEntry(int itemId, int chance, int questId)
```

---

## `org.gms.server.maps` / `server/maps/ReactorFactory.java`

### 类型声明
```text
class ReactorFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static final ReactorStats getReactorS(int rid)
public static ReactorStats getReactor(int rid)
```

---

## `org.gms.server.maps` / `server/maps/ReactorStats.java`

### 类型声明
```text
class ReactorStats
```

- 字段候选数: 2
```text
private Point tl
private Point br
```

- 方法/构造器候选数: 12
```text
public void setTL(Point tl)
public void setBR(Point br)
public Point getTL()
public Point getBR()
public void addState(byte state, List<StateData> data, int timeOut)
public void addState(byte state, int type, Pair<Integer, Integer> reactItem, byte nextState, int timeOut, byte canTouch)
public int getTimeout(byte state)
public byte getTimeoutState(byte state)
public byte getStateSize(byte state)
public byte getNextState(byte state, byte index)
public List<Integer> getActiveSkills(byte state, byte index)
public int getType(byte state)
```

---

## `org.gms.server.maps` / `server/maps/SavedLocation.java`

### 类型声明
```text
class SavedLocation
```

- 字段候选数: 2
```text
private final int mapId
private final int portal
```

- 方法/构造器候选数: 3
```text
public SavedLocation(int mapId, int portal)
public int getMapId()
public int getPortal()
```

---

## `org.gms.server.maps` / `server/maps/SavedLocationType.java`

### 类型声明
```text
enum SavedLocationType
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static SavedLocationType fromString(String Str)
```

---

## `org.gms.server.maps` / `server/maps/Summon.java`

### 类型声明
```text
class Summon
```

- 字段候选数: 5
```text
private final Character owner
private final byte skillLevel
private final int skill
private int hp
private final SummonMovementType movementType
```

- 方法/构造器候选数: 12
```text
public Summon(Character owner, int skill, Point pos, SummonMovementType movementType)
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public Character getOwner()
public int getSkill()
public int getHP()
public void addHP(int delta)
public SummonMovementType getMovementType()
public boolean isStationary()
public byte getSkillLevel()
public MapObjectType getType()
public final boolean isPuppet()
```

---

## `org.gms.server.maps` / `server/maps/SummonMovementType.java`

### 类型声明
```text
enum SummonMovementType
```

- 字段候选数: 1
```text
private final int val
```

- 方法/构造器候选数: 2
```text
SummonMovementType(int val)
public int getValue()
```

---

## `org.gms.server.minigame` / `server/minigame/RockPaperScissor.java`

### 类型声明
```text
class RockPaperScissor
```

- 字段候选数: 3
```text
private int round = 0
private boolean ableAnswer = true
private boolean win = false
```

- 方法/构造器候选数: 6
```text
public RockPaperScissor(final Client c, final byte mode)
public final boolean answer(final Client c, final int answer)
public final boolean timeOut(final Client c)
public final boolean nextRound(final Client c)
public final void reward(final Client c)
public final void dispose(final Client c)
```

---

## `org.gms.server.movement` / `server/movement/AbsoluteLifeMovement.java`

### 类型声明
```text
class AbsoluteLifeMovement
```

- 字段候选数: 2
```text
private Point pixelsPerSecond
private int fh
```

- 方法/构造器候选数: 6
```text
public AbsoluteLifeMovement(int type, Point position, int duration, int newstate)
public Point getPixelsPerSecond()
public void setPixelsPerSecond(Point wobble)
public int getFh()
public void setFh(int fh)
public void serialize(OutPacket p)
```

---

## `org.gms.server.movement` / `server/movement/AbstractLifeMovement.java`

### 类型声明
```text
class AbstractLifeMovement
```

- 字段候选数: 4
```text
private final Point position
private final int duration
private final int newstate
private final int type
```

- 方法/构造器候选数: 5
```text
public AbstractLifeMovement(int type, Point position, int duration, int newstate)
public int getType()
public int getDuration()
public int getNewstate()
public Point getPosition()
```

---

## `org.gms.server.movement` / `server/movement/ChairMovement.java`

### 类型声明
```text
class ChairMovement
```

- 字段候选数: 1
```text
private int fh
```

- 方法/构造器候选数: 4
```text
public ChairMovement(int type, Point position, int duration, int newstate)
public int getFh()
public void setFh(int fh)
public void serialize(OutPacket p)
```

---

## `org.gms.server.movement` / `server/movement/ChangeEquip.java`

### 类型声明
```text
class ChangeEquip
```

- 字段候选数: 1
```text
private final int wui
```

- 方法/构造器候选数: 3
```text
public ChangeEquip(int wui)
public void serialize(OutPacket p)
public Point getPosition()
```

---

## `org.gms.server.movement` / `server/movement/JumpDownMovement.java`

### 类型声明
```text
class JumpDownMovement
```

- 字段候选数: 3
```text
private Point pixelsPerSecond
private int fh
private int originFh
```

- 方法/构造器候选数: 8
```text
public JumpDownMovement(int type, Point position, int duration, int newstate)
public Point getPixelsPerSecond()
public void setPixelsPerSecond(Point wobble)
public int getFh()
public void setFh(int fh)
public int getOriginFh()
public void setOriginFh(int fh)
public void serialize(OutPacket p)
```

---

## `org.gms.server.movement` / `server/movement/LifeMovement.java`

### 类型声明
```text
interface LifeMovement
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.movement` / `server/movement/LifeMovementFragment.java`

### 类型声明
```text
interface LifeMovementFragment
```

- 字段候选数: 0

- 方法/构造器候选数: 0

---

## `org.gms.server.movement` / `server/movement/RelativeLifeMovement.java`

### 类型声明
```text
class RelativeLifeMovement
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public RelativeLifeMovement(int type, Point position, int duration, int newstate)
public void serialize(OutPacket p)
```

---

## `org.gms.server.movement` / `server/movement/TeleportMovement.java`

### 类型声明
```text
class TeleportMovement
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public TeleportMovement(int type, Point position, int newstate)
public void serialize(OutPacket p)
```

---

## `org.gms.server.partyquest` / `server/partyquest/AriantColiseum.java`

### 类型声明
```text
class AriantColiseum
```

- 字段候选数: 8
```text
private Expedition exped
private MapleMap map
private boolean scoreDirty = false
private ScheduledFuture<?> ariantUpdate
private ScheduledFuture<?> ariantFinish
private ScheduledFuture<?> ariantScoreboard
private int lostShards = 0
private boolean eventClear = false
```

- 方法/构造器候选数: 24
```text
public AriantColiseum(MapleMap eventMap, Expedition expedition)
private void setArenaUpdate(ScheduledFuture<?> ariantUpdate)
private void setArenaFinish(ScheduledFuture<?> arenaFinish)
private void setAriantScoreBoard(ScheduledFuture<?> ariantScore)
private void cancelArenaUpdate()
private void cancelArenaFinish()
private void cancelAriantScoreBoard()
private void cancelAriantSchedules()
public int getAriantScore(Character chr)
public void clearAriantScore(Character chr)
public void updateAriantScore(Character chr, int points)
private void broadcastAriantScoreUpdate()
public int getAriantRewardTier(Character chr)
public void clearAriantRewardTier(Character chr)
public void addLostShards(int quantity)
public void leaveArena(Character chr)
private synchronized void leaveArenaInternal(Character chr)
public void playerDisconnected(Character chr)
private void showArenaResults()
private static boolean isUnfairMatch(Integer winnerScore, Integer secondScore, Integer lostShardsScore, List<Integer> runnerupsScore)
public void distributeAriantPoints()
private ExpeditionType getExpeditionType()
private void enterKingsRoom()
private synchronized void dispose()
```

---

## `org.gms.server.partyquest` / `server/partyquest/CarnivalFactory.java`

### 类型声明
```text
class CarnivalFactory
```

- 字段候选数: 0

- 方法/构造器候选数: 7
```text
public CarnivalFactory()
public static final CarnivalFactory getInstance()
private void initialize()
private MCSkill randomizeSkill(boolean multi)
public MCSkill getSkill(final int id)
public MCSkill getGuardian(final int id)
public record MCSkill(int cpLoss, MobSkillType mobSkillType, int level, boolean targetsAll)
```

---

## `org.gms.server.partyquest` / `server/partyquest/GuardianSpawnPoint.java`

### 类型声明
```text
class GuardianSpawnPoint
```

- 字段候选数: 3
```text
private Point position
private boolean taken
private int team = -1
```

- 方法/构造器候选数: 7
```text
public GuardianSpawnPoint(Point a)
public Point getPosition()
public void setPosition(Point position)
public boolean isTaken()
public void setTaken(boolean taken)
public int getTeam()
public void setTeam(int team)
```

---

## `org.gms.server.partyquest` / `server/partyquest/MonsterCarnival.java`

### 类型声明
```text
class MonsterCarnival
```

- 字段候选数: 8
```text
public static int D = 3
public static int C = 2
public static int B = 1
public static int A = 0
private MapleMap map
private long startTime = 0
private int summonsR = 0, summonsB = 0, room = 0
private boolean cpq1
```

- 方法/构造器候选数: 44
```text
public MonsterCarnival(Party p1, Party p2, int mapid, boolean cpq1, int room)
private void respawn()
public void playerDisconnected(int charid)
private void earlyFinish()
public void leftParty(int charid)
protected void dispose()
public boolean canSummonR()
public void summonR()
public boolean canSummonB()
public void summonB()
public boolean canGuardianR()
public boolean canGuardianB()
protected void dispose(boolean warpout)
public void exit()
public ScheduledFuture<?> getTimer()
private void finish(int winningTeam)
private void timeUp()
public long getTimeLeft()
public int getTimeLeftSeconds()
private void extendTime()
public void complete()
public Party getRed()
public void setRed(Party p1)
public Party getBlue()
public void setBlue(Party p2)
public Character getLeader1()
public void setLeader1(Character leader1)
public Character getLeader2()
public void setLeader2(Character leader2)
public Character getEnemyLeader(int team)
public int getBlueCP()
public void setBlueCP(int blueCP)
public int getBlueTotalCP()
public void setBlueTotalCP(int blueTotalCP)
public int getRedCP()
public void setRedCP(int redCP)
public int getRedTotalCP()
public void setRedTotalCP(int redTotalCP)
public int getTotalCP(int team)
public void setTotalCP(int totalCP, int team)
public int getCP(int team)
public void setCP(int CP, int team)
public int getRoom()
public MapleMap getEventMap()
```

---

## `org.gms.server.partyquest` / `server/partyquest/MonsterCarnivalParty.java`

### 类型声明
```text
class MonsterCarnivalParty
```

- 字段候选数: 4
```text
private final Character leader
private final byte team
private int summons = 8
private boolean winner = false
```

- 方法/构造器候选数: 14
```text
public MonsterCarnivalParty(final Character owner, final List<Character> members1, final byte team1)
public final Character getLeader()
public List<Character> getMembers()
public int getTeam()
public void warpOut(final int map)
public void warp(final MapleMap map, final int portalid)
public void warpOut()
public boolean allInMap(MapleMap map)
public void removeMember(Character chr)
public boolean isWinner()
public void setWinner(boolean status)
public void displayMatchResult()
public void summon()
public boolean canSummon()
```

---

## `org.gms.server.partyquest` / `server/partyquest/PartyQuest.java`

### 类型声明
```text
class PartyQuest
```

- 字段候选数: 1
```text
Party party
```

- 方法/构造器候选数: 5
```text
public PartyQuest(Party party)
public Party getParty()
public List<Character> getParticipants()
public void removeParticipant(Character chr) throws Throwable
public static int getExp(String PQ, int level)
```

---

## `org.gms.server.partyquest` / `server/partyquest/Pyramid.java`

### 类型声明
```text
class Pyramid
enum PyramidMode
```

- 字段候选数: 5
```text
int kill = 0, miss = 0, cool = 0, exp = 0, map, count
short gauge
PyramidMode mode
ScheduledFuture<?> timer = null
ScheduledFuture<?> gaugeSchedule = null
```

- 方法/构造器候选数: 11
```text
public Pyramid(Party party, PyramidMode mode, int mapid)
public void startGaugeSchedule()
public void kill()
public void cool()
public void miss()
public int timer()
public void warp(int mapid)
public void broadcastInfo(String info, int amount)
public boolean useSkill()
public void checkBuffs()
public void sendScore(Character chr)
```

---

## `org.gms.server.quest` / `server/quest/Quest.java`

### 类型声明
```text
class Quest
```

- 字段候选数: 4
```text
protected short id
private boolean autoStart
private boolean repeatable = false
private String name = "", parent = ""
```

- 方法/构造器候选数: 41
```text
private Quest(int id)
public boolean isAutoComplete()
public boolean isAutoStart()
public static Quest getInstance(int id)
public static Quest getInstanceFromInfoNumber(int infoNumber)
public boolean isSameDayRepeatable()
public boolean canStartQuestByStatus(Character chr)
public boolean canQuestByInfoProgress(Character chr)
public boolean canStart(Character chr, int npcid)
public boolean canComplete(Character chr, Integer npcid)
public void start(Character chr, int npc)
public void complete(Character chr, int npc)
public void complete(Character chr, int npc, Integer selection)
public void reset(Character chr)
public boolean forfeit(Character chr)
public boolean forceStart(Character chr, int npc)
public boolean forceComplete(Character chr, int npc)
public short getId()
public List<Integer> getRelevantMobs()
public int getStartItemAmountNeeded(int itemid)
public int getCompleteItemAmountNeeded(int itemid)
public int getMobAmountNeeded(int mid)
public short getInfoNumber(Status qs)
public String getInfoEx(Status qs, int index)
public List<String> getInfoEx(Status qs)
public int getTimeLimit()
public static void clearCache(int quest)
public static void clearCache()
private AbstractQuestRequirement getRequirement(QuestRequirementType type, Data data)
private AbstractQuestAction getAction(QuestActionType type, Data data)
public boolean restoreLostItem(Character chr, int itemid)
public int getMedalRequirement()
public int getNpcRequirement(boolean checkEnd)
public boolean hasScriptRequirement(boolean checkEnd)
public boolean hasNextQuestAction()
public String getName()
public String getParentName()
public static boolean isExploitableQuest(short questid)
public static List<Quest> getMatchedQuests(String search)
public static void loadAllQuests()
public void expireQuest(Character chr)
```

---

## `org.gms.server.quest` / `server/quest/QuestActionType.java`

### 类型声明
```text
enum QuestActionType
```

- 字段候选数: 1
```text
final byte type
```

- 方法/构造器候选数: 20
```text
UNDEFINED(-1),
EXP(0),
ITEM(1),
NEXTQUEST(2),
MESO(3),
QUEST(4),
SKILL(5),
FAME(6),
BUFF(7),
PETSKILL(8),
YES(9),
NO(10),
NPC(11),
MIN_LEVEL(12),
NORMAL_AUTO_START(13),
PETTAMENESS(14),
PETSPEED(15),
INFO(16),
QuestActionType(int type)
public static QuestActionType getByWZName(String name)
```

---

## `org.gms.server.quest` / `server/quest/QuestRequirementType.java`

### 类型声明
```text
enum QuestRequirementType
```

- 字段候选数: 1
```text
final byte type
```

- 方法/构造器候选数: 27
```text
UNDEFINED(-1),
JOB(0),
ITEM(1),
QUEST(2),
MIN_LEVEL(3),
MAX_LEVEL(4),
END_DATE(5),
MOB(6),
NPC(7),
FIELD_ENTER(8),
INTERVAL(9),
SCRIPT(10),
PET(11),
MIN_PET_TAMENESS(12),
MONSTER_BOOK(13),
NORMAL_AUTO_START(14),
INFO_NUMBER(15),
INFO_EX(16),
COMPLETED_QUEST(17),
START(18),
END(19),
DAY_BY_DAY(20),
MESO(21),
BUFF(22),
QuestRequirementType(int type)
public byte getType()
public static QuestRequirementType getByWZName(String name)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/AbstractQuestAction.java`

### 类型声明
```text
class AbstractQuestAction
```

- 字段候选数: 2
```text
private final QuestActionType type
protected int questID
```

- 方法/构造器候选数: 5
```text
public AbstractQuestAction(QuestActionType action, Quest quest)
public boolean check(Character chr, Integer extSelection)
public QuestActionType getType()
public static List<Integer> getJobBy5ByteEncoding(int encoded)
public static List<Integer> getJobBySimpleEncoding(int encoded)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/BuffAction.java`

### 类型声明
```text
class BuffAction
```

- 字段候选数: 1
```text
int itemEffect
```

- 方法/构造器候选数: 4
```text
public BuffAction(Quest quest, Data data)
public boolean check(Character chr, Integer extSelection)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/ExpAction.java`

### 类型声明
```text
class ExpAction
```

- 字段候选数: 1
```text
int exp
```

- 方法/构造器候选数: 4
```text
public ExpAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public static void runAction(Character chr, int gain)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/FameAction.java`

### 类型声明
```text
class FameAction
```

- 字段候选数: 1
```text
int fame
```

- 方法/构造器候选数: 3
```text
public FameAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/InfoAction.java`

### 类型声明
```text
class InfoAction
```

- 字段候选数: 2
```text
private String info
private final int questID
```

- 方法/构造器候选数: 3
```text
public InfoAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/ItemAction.java`

### 类型声明
```text
class ItemAction
class ItemData
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
public ItemAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public boolean check(Character chr, Integer extSelection)
private void announceInventoryLimit(List<Integer> itemids, Character chr)
private boolean canHold(Character chr, List<Pair<Item, InventoryType>> gainList)
private boolean canGetItem(ItemData item, Character chr)
public boolean restoreLostItem(Character chr, int itemid)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/MesoAction.java`

### 类型声明
```text
class MesoAction
```

- 字段候选数: 1
```text
int mesos
```

- 方法/构造器候选数: 4
```text
public MesoAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public static void runAction(Character chr, int gain)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/NextQuestAction.java`

### 类型声明
```text
class NextQuestAction
```

- 字段候选数: 1
```text
int nextQuest
```

- 方法/构造器候选数: 3
```text
public NextQuestAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/PetSkillAction.java`

### 类型声明
```text
class PetSkillAction
```

- 字段候选数: 1
```text
int flag
```

- 方法/构造器候选数: 4
```text
public PetSkillAction(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer extSelection)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/PetSpeedAction.java`

### 类型声明
```text
class PetSpeedAction
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public PetSpeedAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/PetTamenessAction.java`

### 类型声明
```text
class PetTamenessAction
```

- 字段候选数: 1
```text
int tameness
```

- 方法/构造器候选数: 3
```text
public PetTamenessAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/QuestAction.java`

### 类型声明
```text
class QuestAction
```

- 字段候选数: 1
```text
int mesos
```

- 方法/构造器候选数: 3
```text
public QuestAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.actions` / `server/quest/actions/SkillAction.java`

### 类型声明
```text
class SkillAction
class SkillData
```

- 字段候选数: 1
```text
int itemEffect
```

- 方法/构造器候选数: 3
```text
public SkillAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/AbstractQuestRequirement.java`

### 类型声明
```text
class AbstractQuestRequirement
```

- 字段候选数: 1
```text
private final QuestRequirementType type
```

- 方法/构造器候选数: 2
```text
public AbstractQuestRequirement(QuestRequirementType type)
public QuestRequirementType getType()
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/BuffExceptRequirement.java`

### 类型声明
```text
class BuffExceptRequirement
```

- 字段候选数: 1
```text
private int buffId = -1
```

- 方法/构造器候选数: 3
```text
public BuffExceptRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/BuffRequirement.java`

### 类型声明
```text
class BuffRequirement
```

- 字段候选数: 1
```text
private int buffId = 1
```

- 方法/构造器候选数: 3
```text
public BuffRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/CompletedQuestRequirement.java`

### 类型声明
```text
class CompletedQuestRequirement
```

- 字段候选数: 1
```text
private int reqQuest
```

- 方法/构造器候选数: 3
```text
public CompletedQuestRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/EndDateRequirement.java`

### 类型声明
```text
class EndDateRequirement
```

- 字段候选数: 1
```text
private String timeStr
```

- 方法/构造器候选数: 3
```text
public EndDateRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/FieldEnterRequirement.java`

### 类型声明
```text
class FieldEnterRequirement
```

- 字段候选数: 1
```text
private int mapId = -1
```

- 方法/构造器候选数: 3
```text
public FieldEnterRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/InfoExRequirement.java`

### 类型声明
```text
class InfoExRequirement
```

- 字段候选数: 1
```text
private final int questID
```

- 方法/构造器候选数: 4
```text
public InfoExRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public List<String> getInfo()
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/InfoNumberRequirement.java`

### 类型声明
```text
class InfoNumberRequirement
```

- 字段候选数: 2
```text
private short infoNumber
private final int questID
```

- 方法/构造器候选数: 4
```text
public InfoNumberRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public short getInfoNumber()
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/IntervalRequirement.java`

### 类型声明
```text
class IntervalRequirement
```

- 字段候选数: 2
```text
private long interval = -1
private final int questID
```

- 方法/构造器候选数: 5
```text
public IntervalRequirement(Quest quest, Data data)
public long getInterval()
public void processData(Data data)
private static String getIntervalTimeLeft(Character chr, IntervalRequirement r)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/ItemRequirement.java`

### 类型声明
```text
class ItemRequirement
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public ItemRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int getItemAmountNeeded(int itemid, boolean complete)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/JobRequirement.java`

### 类型声明
```text
class JobRequirement
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public JobRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MaxLevelRequirement.java`

### 类型声明
```text
class MaxLevelRequirement
```

- 字段候选数: 1
```text
private int maxLevel
```

- 方法/构造器候选数: 3
```text
public MaxLevelRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MesoRequirement.java`

### 类型声明
```text
class MesoRequirement
```

- 字段候选数: 1
```text
private int meso = 0
```

- 方法/构造器候选数: 3
```text
public MesoRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MinLevelRequirement.java`

### 类型声明
```text
class MinLevelRequirement
```

- 字段候选数: 1
```text
private int minLevel
```

- 方法/构造器候选数: 3
```text
public MinLevelRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MinTamenessRequirement.java`

### 类型声明
```text
class MinTamenessRequirement
```

- 字段候选数: 1
```text
private int minTameness
```

- 方法/构造器候选数: 3
```text
public MinTamenessRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MobRequirement.java`

### 类型声明
```text
class MobRequirement
```

- 字段候选数: 1
```text
private final int questID
```

- 方法/构造器候选数: 4
```text
public MobRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int getRequiredMobCount(int mobid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/MonsterBookCountRequirement.java`

### 类型声明
```text
class MonsterBookCountRequirement
```

- 字段候选数: 1
```text
private int reqCards
```

- 方法/构造器候选数: 3
```text
public MonsterBookCountRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/NpcRequirement.java`

### 类型声明
```text
class NpcRequirement
```

- 字段候选数: 1
```text
private int reqNPC
```

- 方法/构造器候选数: 4
```text
public NpcRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int get()
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/PetRequirement.java`

### 类型声明
```text
class PetRequirement
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public PetRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/QuestRequirement.java`

### 类型声明
```text
class QuestRequirement
```

- 字段候选数: 0

- 方法/构造器候选数: 3
```text
public QuestRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

---

## `org.gms.server.quest.requirements` / `server/quest/requirements/ScriptRequirement.java`

### 类型声明
```text
class ScriptRequirement
```

- 字段候选数: 1
```text
private boolean reqScript
```

- 方法/构造器候选数: 4
```text
public ScriptRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public boolean get()
```

---

## `org.gms.service` / `service/AccountService.java`

### 类型声明
```text
class AccountService
```

- 字段候选数: 5
```text
private final AccountsMapper accountsMapper
private final CharactersMapper charactersMapper
private final IpbansMapper ipbansMapper
private final MacbansMapper macbansMapper
private final QuickslotkeymappedMapper quickslotkeymappedMapper
```

- 方法/构造器候选数: 20
```text
public AccountsDO findByName(String name)
public AccountsDO findById(int id)
public AccountsDO getCurrentUser()
public Page<AccountsDO> getAccountList(Integer page, Integer size, Integer id, String name, String lastLoginStart, String lastLoginEnd, String createdAtStart, String createdAtEnd)
public void update(AccountsDO condition)
public void addAccount(AddAccountDTO submitData) throws NoSuchAlgorithmException
public void updateAccountByUser(UpdateAccountByUserDTO submitData) throws NoSuchAlgorithmException
public void updateAccountByGM(int id, UpdateAccountByGmDTO submitData) throws NoSuchAlgorithmException
public void deleteAccountByGM(int id)
public String encryptPassword(String password) throws NoSuchAlgorithmException
public boolean checkPassword(String pwd, AccountsDO accountsDO)
private static boolean checkHash(String hash, String type, String password)
public void resetAllLoggedIn(int id)
public void banAccount(int accountId, String reason)
public void unbanAccount(int accountId)
public void resetAllLoggedIn()
public void ban(Character chr, String reason)
public void ban(String str, String reason, boolean isAccount)
public boolean isBanned(String ip)
public QuickslotkeymappedDO getQuickSlotKeyMap(int accountId)
```

---

## `org.gms.service` / `service/AuthService.java`

### 类型声明
```text
class AuthService
```

- 字段候选数: 2
```text
private final AccountService accountService
private final JwtUtils jwtUtils
```

- 方法/构造器候选数: 0

---

## `org.gms.service` / `service/AutobanConfigService.java`

### 类型声明
```text
class AutobanConfigService
```

- 字段候选数: 1
```text
private final AutobanConfigMapper autobanConfigMapper
```

- 方法/构造器候选数: 3
```text
public void loadConfigs()
public List<AutobanConfigDTO> getConfigList()
public void updateConfig(AutobanConfigDTO dto)
```

---

## `org.gms.service` / `service/CashShopService.java`

### 类型声明
```text
class CashShopService
```

- 字段候选数: 1
```text
private final ModifiedCashItemMapper modifiedCashItemMapper
```

- 方法/构造器候选数: 9
```text
public List<ModifiedCashItemDO> loadAllModifiedCashItems()
public List<CashCategory> getAllCategoryList()
public Page<CashShopSearchRtnDTO> getCommodityByCategory(CashCategory data)
public CashShopSearchRtnDTO getCommodityBySn(Integer sn)
public void changeOnSale(ModifiedCashItemDO data)
private CashCategory getCategory(Integer id, Integer subId)
private CashShopSearchRtnDTO fromCashItem(CashCategory cashCategory, ModifiedCashItemDO cashItem)
private void setDbItemValue(CashShopSearchRtnDTO rtnDTO, ModifiedCashItemDO dbCashItem)
public void batchChangeOnSale(CashShopBatchOnSaleReqDTO submit)
```

---

## `org.gms.service` / `service/CharacterService.java`

### 类型声明
```text
class CharacterService
```

- 字段候选数: 26
```text
private final ExtendValueMapper extendValueMapper
private final CharactersMapper charactersMapper
private final SkillsMapper skillsMapper
private final SkillmacrosMapper skillmacrosMapper
private final GuildsMapper guildsMapper
private final BuddiesMapper buddiesMapper
private final BbsThreadsMapper bbsThreadsMapper
private final BbsRepliesMapper bbsRepliesMapper
private final WishlistsMapper wishlistsMapper
private final CooldownsMapper cooldownsMapper
private final PlayerdiseasesMapper playerdiseasesMapper
private final AreaInfoMapper areaInfoMapper
private final MonsterbookMapper monsterbookMapper
private final FamilyCharacterMapper familyCharacterMapper
private final FamelogMapper famelogMapper
private final InventoryService inventoryService
private final QuestService questService
private final FredstorageMapper fredstorageMapper
private final MtsService mtsService
private final KeymapMapper keymapMapper
private final SavedlocationsMapper savedlocationsMapper
private final TrocklocationsMapper trocklocationsMapper
private final EventstatsMapper eventstatsMapper
private final ServerQueueMapper serverQueueMapper
private final NameChangeService nameChangeService
private final WorldTransferService worldTransferService
```

- 方法/构造器候选数: 23
```text
public CharactersDO findById(int id)
public void update(CharactersDO condition)
public Page<ChrOnlineListRtnDTO> getChrOnlineList(ChrOnlineListReqDTO request)
public void updateRate(ExtendValueDO data)
public void resetRate(ExtendValueDO data)
public void resetRates(ExtendValueDO data)
public void resetMerchant()
public List<List<CharactersDO>> getWorldsRankPlayers(int worldSize)
public List<CharactersDO> getWorldRankPlayers(int worldId)
public CharactersDO findByName(String name)
public void removeSkill(SkillsDO skillsDO)
public void deleteGuild(GuildsDO guildsDO)
public void deleteCharFromDB(Character player, int senderAccId)
public void saveCharToDB(Character player, boolean notAutosave)
public Character loadCharFromDB(int cid, Client client, boolean channelServer)
public List<TrocklocationsDO> getTrockLocationByCharacter(Integer cid)
public List<AreaInfoDO> getAreaInfoByCharacter(Integer cid)
public List<EventstatsDO> getEventStatsByCharacter(Integer cid)
public List<WishlistsDO> getWishlistsByCharacter(Integer cid)
public List<CharactersDO> getCharacterByAccountId(int accountId)
private void checkName(ExtendValueDO data)
private void check(ExtendValueDO data)
private Character getCharacter(ExtendValueDO data)
```

---

## `org.gms.service` / `service/CommandService.java`

### 类型声明
```text
class CommandService
```

- 字段候选数: 1
```text
private final CommandInfoMapper commandInfoMapper
```

- 方法/构造器候选数: 10
```text
public void loadCommands(final HashMap<String, Command> registeredCommands, final List<Pair<List<String>, List<String>>> commandsNameDesc)
private void updateRegisteredCommands(CommandInfoDO commandInfoDO)
private void registerCommands(final HashMap<String, Command> registeredCommands, final List<Pair<List<String>, List<String>>> commandsNameDesc, int level, List<CommandInfoDO> commandInfoList)
private Command getCommandInstance(CommandInfoDO commandInfoDO)
public Page<CommandReqDTO> getCommandListFromDB(CommandReqDTO request)
public String getDescriptionByCommandInfoDO(CommandInfoDO CommandDO)
public CommandInfoDO updateCommand(CommandReqDTO request)
public void reloadEventsByGMCommand()
public void reloadPortalsByGMCommand()
public void reloadMapsByGMCommand()
```

---

## `org.gms.service` / `service/CommonService.java`

### 类型声明
```text
class CommonService
```

- 字段候选数: 1
```text
private ItemService itemService
```

- 方法/构造器候选数: 4
```text
public EquipmentInfoRtnDTO getEquipmentInfoByItemId(EquipmentInfoReqDTO submitData)
public Integer getOnlinePlayerCountByWorldId(Integer worldId)
public Integer getAllWorldsOnlinePlayersCount(List<Integer> worldIdList)
public List<InformationResult> getInformation(InformationSearch condition)
```

---

## `org.gms.service` / `service/ConfigService.java`

### 类型声明
```text
class ConfigService
```

- 字段候选数: 3
```text
private final GameConfigMapper gameConfigMapper
private final ServiceProperty serviceProperty
private final LangResourceService langResourceService
```

- 方法/构造器候选数: 12
```text
public List<GameConfigDO> loadGameConfigs()
public ConfigTypeDTO getConfigTypeList()
public Page<GameConfigDO> getConfigList(GameConfigReqDTO condition)
public void addConfig(GameConfigDO condition)
public void updateConfig(GameConfigDO condition)
public void deleteConfig(Long id)
public void deleteConfigList(List<Long> ids)
public int importYml(MultipartFile file)
private Object parseObject(Object obj)
private String replaceWithEquals(String src, String[]... fts)
private String replaceWithContains(String src, String[]... fts)
public ResponseEntity<Resource> exportYml()
```

---

## `org.gms.service` / `service/DropService.java`

### 类型声明
```text
class DropService
```

- 字段候选数: 2
```text
private final DropDataMapper dropDataMapper
private final DropDataGlobalMapper dropDataGlobalMapper
```

- 方法/构造器候选数: 5
```text
public Page<DropSearchRtnDTO> getDropList(DropSearchReqDTO data, boolean isGlobal)
public Long modifyDropData(DropSearchRtnDTO data, boolean isGlobal, boolean isDelete)
private String getItemName(Integer itemId)
private String getMobName(Integer mobId)
private String getQuestName(Integer questId)
```

---

## `org.gms.service` / `service/FamilyService.java`

### 类型声明
```text
class FamilyService
```

- 字段候选数: 3
```text
private final FamilyCharacterMapper familyCharacterMapper
private final FamilyEntitlementMapper familyEntitlementMapper
private final CharacterService characterService
```

- 方法/构造器候选数: 1
```text
public void loadAllFamilies()
```

---

## `org.gms.service` / `service/FileTreeService.java`

### 类型声明
```text
class FileTreeService
```

- 字段候选数: 2
```text
private static final String FILE_TREE_KEY_DELIMITER = "-"
private static final boolean FILE_TREE_PATH_STRICT_MODE = true
```

- 方法/构造器候选数: 5
```text
public String readFile(String currentKey, String filename)
public void writeFile(String currentKey, String filename, String content)
public List<FileTreeNodeDTO> tree(String currentKey)
public File resolveByTreeKey(String currentKey)
private boolean matchAnyLimitPattern(Path path)
```

---

## `org.gms.service` / `service/GachaponService.java`

### 类型声明
```text
class GachaponService
```

- 字段候选数: 2
```text
private GachaponRewardPoolMapper gachaponRewardPoolMapper
private GachaponRewardMapper gachaponRewardMapper
```

- 方法/构造器候选数: 12
```text
public void updatePool(GachaponRewardPoolDO submit)
public void deletePool(Integer id)
public Page<GachaponPoolSearchRtnDTO> getPools(GachaponPoolSearchReqDTO condition)
public List<GachaponRewardDO> getRewards(Integer poolId)
public void updateReward(GachaponRewardDO reward)
public void deleteReward(Integer id)
private void setRealProb(List<GachaponPoolSearchRtnDTO> pools)
private List<GachaponRewardPoolDO> getActivePools(Integer gachaponId)
public void doGachapon(Character player, int gachaponId)
public List<GachaponRewardDO> getRewardsByNpcId(Integer npcId)
private void doReward(Character player, GachaponRewardPoolDO pool)
private List<GachaponRewardDO> getPoolRewards(Integer poolId)
```

---

## `org.gms.service` / `service/GiveService.java`

### 类型声明
```text
class GiveService
```

- 字段候选数: 1
```text
CharacterService characterService
```

- 方法/构造器候选数: 21
```text
public void give(GiveResourceReqDTO submitData)
private void giveAllOnlineChr(GiveResourceReqDTO submitData)
private void giveChr(GiveResourceReqDTO submitData)
private void giveNxAllOnlineChr(int quantity, int type)
private void giveNxChr(Character chr, int quantity, int type)
private String getCashTypeName(int type)
private void giveMesosAllOnlineChr(int quantity)
private void giveMesosChr(Character chr, int quantity)
private void giveExpAllOnlineChr(int quantity)
private void giveExpChr(Character chr, int quantity)
private void giveItemAllOnlineChr(int itemId, short quantity)
private void giveItemChr(Character chr, int itemId, short quantity)
private void giveEquipAllOnlineChr(GiveResourceReqDTO submitData)
private void giveEquipChr(Character chr, GiveResourceReqDTO submitData)
private void giveRateChr(Character chr, String type, float rate)
private void giveGMChr(Character chr, Integer level)
private void giveFameChr(Character chr, Integer fame)
private void changeMap(Character chr, Integer mapId)
private void doGainCash(Character chr, int type, int quantity)
private void doGainExp(Character chr, int quantity)
private void doGainMeso(Character chr, int quantity)
```

---

## `org.gms.service` / `service/HpMpAlertService.java`

### 类型声明
```text
class HpMpAlertService
```

- 字段候选数: 3
```text
private static final int MAX_ALERT_STEP = 19
private static final int ALERT_STEP_DIVISOR = 20
private HpMpAlertMapper hpMpAlertMapper
```

- 方法/构造器候选数: 9
```text
private static byte normalizeAlertStep(byte step)
public byte getHpAlert(int characterId)
public void setHpAlert(int characterId, byte alert)
public float getHpAlertPer(int characterId)
public byte getMpAlert(int characterId)
public void setMpAlert(int characterId, byte alert)
public float getMpAlertPer(int characterId)
public void saveAll()
public void clear()
```

---

## `org.gms.service` / `service/InventoryService.java`

### 类型声明
```text
class InventoryService
```

- 字段候选数: 5
```text
private final InventoryitemsMapper inventoryitemsMapper
private final InventoryequipmentMapper inventoryequipmentMapper
private final RingsMapper ringsMapper
private final PetsMapper petsMapper
private final PetignoresMapper petignoresMapper
```

- 方法/构造器候选数: 15
```text
public List<InventoryTypeRtnDTO> getInventoryTypeList()
public Page<InventorySearchReqDTO> getCharacterList(InventorySearchReqDTO data)
public List<InventorySearchRtnDTO> getInventoryList(InventorySearchReqDTO data)
public void deleteInventoryByCharacterId(int cid)
private Character getCharacterById(int characterId)
private InventorySearchRtnDTO buildByDb(Row obj)
private List<InventorySearchRtnDTO> buildByOnline(Character character, InventoryType type)
public void updateInventory(InventorySearchRtnDTO data)
private void updateOnline(InventorySearchRtnDTO data, Character character)
private void updateDb(InventorySearchRtnDTO data)
public void deleteInventory(InventorySearchRtnDTO data)
public List<PetignoresDO> getPetIgnoreByPetId(Integer petId)
private void modifyInventoryCheck(InventorySearchRtnDTO data)
private Item getModifyItemOnline(InventorySearchRtnDTO data, Inventory inventory)
private InventoryitemsDO getModifyItemOffline(InventorySearchRtnDTO data)
```

---

## `org.gms.service` / `service/ItemService.java`

### 类型声明
```text
class ItemService
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public Equip getEquipmentInfoByItemId(Integer itemId)
```

---

## `org.gms.service` / `service/LangResourceService.java`

### 类型声明
```text
class LangResourceService
```

- 字段候选数: 2
```text
private final ServiceProperty serviceProperty
private final LangResourcesMapper langResourcesMapper
```

- 方法/构造器候选数: 3
```text
public String getI18n(LangResourcesDO langResourcesDO)
public void insertOrUpdateI18n(LangResourcesDO langResourcesDO)
public void deleteI18n(LangResourcesDO langResourcesDO)
```

---

## `org.gms.service` / `service/MonsterBookService.java`

### 类型声明
```text
class MonsterBookService
```

- 字段候选数: 1
```text
private final MonsterbookMapper monsterbookMapper
```

- 方法/构造器候选数: 1
```text
public List<MonsterbookDO> getByCharacterId(int cid)
```

---

## `org.gms.service` / `service/MtsService.java`

### 类型声明
```text
class MtsService
```

- 字段候选数: 2
```text
private final MtsCartMapper mtsCartMapper
private final MtsItemsMapper mtsItemsMapper
```

- 方法/构造器候选数: 1
```text
public void deleteMtsByCharacterId(int cid)
```

---

## `org.gms.service` / `service/NameChangeService.java`

### 类型声明
```text
class NameChangeService
```

- 字段候选数: 4
```text
private final NamechangesMapper namechangesMapper
private final CharactersMapper charactersMapper
private final RingsMapper ringsMapper
private final InventoryitemsMapper inventoryitemsmapper
```

- 方法/构造器候选数: 6
```text
public void applyAllNameChange()
public void applyNameChange(int characterId, String characterName)
public List<NamechangesDO> getAllNameChanges()
public void doNameChange(NamechangesDO data)
public boolean registerNameChange(Character chr, String newName)
public void cancelPendingNameChange(Character chr, boolean needFinish)
```

---

## `org.gms.service` / `service/NewYearCardService.java`

### 类型声明
```text
class NewYearCardService
```

- 字段候选数: 1
```text
private final NewyearMapper newyearMapper
```

- 方法/构造器候选数: 2
```text
public void startPendingNewYearCardRequests()
public List<NewyearDO> loadPlayerNewYearCards(Character chr)
```

---

## `org.gms.service` / `service/NoteService.java`

### 类型声明
```text
class NoteService
```

- 字段候选数: 1
```text
private final NotesMapper notesMapper
```

- 方法/构造器候选数: 4
```text
public void sendNormal(String message, String senderName, String receiverName)
public void sendWithFame(String message, String senderName, String receiverName)
public void show(Character chr)
public Optional<NotesDO> delete(int noteId)
```

---

## `org.gms.service` / `service/NpcService.java`

### 类型声明
```text
class NpcService
```

- 字段候选数: 3
```text
private final PlayernpcsMapper playernpcsMapper
private final PlayernpcsEquipMapper playernpcsEquipMapper
private final PlayernpcsFieldMapper playernpcsFieldMapper
```

- 方法/构造器候选数: 5
```text
public List<PlayernpcsFieldDO> getPlayerNpcFields(PlayernpcsFieldDO condition)
public List<PlayernpcsDO> getPlayerNpcDOs(PlayernpcsDO condition)
public List<PlayernpcsEquipDO> getPlayerNpcEquipDOs(PlayernpcsEquipDO condition)
public List<PlayerNPC> getPlayerNPC(PlayernpcsDO condition)
public PlayerNPC createPlayerNPC(PlayernpcsDO playerNpcDO, List<PlayernpcsEquipDO> playerNpcEquipDOS)
```

---

## `org.gms.service` / `service/NxCodeService.java`

### 类型声明
```text
class NxCodeService
```

- 字段候选数: 2
```text
private final NxcodeMapper nxcodeMapper
private final NxcodeItemsMapper nxcodeItemsMapper
```

- 方法/构造器候选数: 1
```text
public void clearExpirations()
```

---

## `org.gms.service` / `service/NxCouponService.java`

### 类型声明
```text
class NxCouponService
```

- 字段候选数: 1
```text
private final NxcouponsMapper nxcouponsMapper
```

- 方法/构造器候选数: 2
```text
public List<Integer> selectActiveCouponIds(int weekDay, int hourDay)
public List<NxcouponsDO> getNxCoupons(NxcouponsDO condition)
```

---

## `org.gms.service` / `service/QuestService.java`

### 类型声明
```text
class QuestService
```

- 字段候选数: 3
```text
private final MedalmapsMapper medalmapsMapper
private final QuestprogressMapper questprogressMapper
private final QueststatusMapper queststatusMapper
```

- 方法/构造器候选数: 2
```text
public void deleteQuestProgressByCharacter(int cid)
public List<QuestStatus> getQuestStatusByCharacter(int cid)
```

---

## `org.gms.service` / `service/ServerService.java`

### 类型声明
```text
class ServerService
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public List<WorldListRtnDTO> worldList()
public List<ChannelListRtnDTO> channelList(int worldId)
```

---

## `org.gms.service` / `service/ShopService.java`

### 类型声明
```text
class ShopService
```

- 字段候选数: 2
```text
private final ShopsMapper shopsMapper
private final ShopitemsMapper shopitemsMapper
```

- 方法/构造器候选数: 5
```text
public Page<ShopSearchRtnDTO> getShopList(ShopSearchReqDTO data)
public Page<ShopItemSearchRtnDTO> getShopItemList(ShopSearchReqDTO data)
public ShopItemSearchRtnDTO getShopItem(Long id)
public Long modifyShopItem(ShopItemSearchRtnDTO data, boolean isDelete)
private ShopItemSearchRtnDTO fromShopItemDO(ShopitemsDO shopitemsDO)
```

---

## `org.gms.service` / `service/UserDetailsImpl.java`

### 类型声明
```text
class UserDetailsImpl
```

- 字段候选数: 4
```text
private static final long serialVersionUID = 1L
private final Integer id
private final String username
private final String password
```

- 方法/构造器候选数: 10
```text
public UserDetailsImpl(Integer id, String name, String password, Collection<? extends GrantedAuthority> authorities)
public static UserDetailsImpl build(AccountsDO user, Collection<? extends GrantedAuthority> authorities)
public Integer getId()
public String getPassword()
public String getUsername()
public boolean isAccountNonExpired()
public boolean isAccountNonLocked()
public boolean isCredentialsNonExpired()
public boolean isEnabled()
public boolean equals(Object o)
```

---

## `org.gms.service` / `service/UserDetailsServiceImpl.java`

### 类型声明
```text
class UserDetailsServiceImpl
```

- 字段候选数: 1
```text
private final AccountsMapper userDao
```

- 方法/构造器候选数: 2
```text
public UserDetailsServiceImpl(AccountsMapper userRepository)
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException
```

---

## `org.gms.service` / `service/WorldTransferService.java`

### 类型声明
```text
class WorldTransferService
```

- 字段候选数: 4
```text
private final WorldtransfersMapper worldtransfersMapper
private final CharactersMapper charactersMapper
private final AccountService accountService
private final BuddiesMapper buddiesMapper
```

- 方法/构造器候选数: 5
```text
public void applyAllWorldTransfer()
public boolean checkWorldTransferEligibility(WorldtransfersDO data)
public void doWorldTransfer(WorldtransfersDO data)
public boolean registerWorldTransfer(Character chr, int newWorld)
public void cancelPendingWorldTransfer(Character chr, boolean needFinish)
```

---

## `org.gms.util` / `util/BCrypt.java`

### 类型声明
```text
class BCrypt
```

- 字段候选数: 5
```text
private static final int GENSALT_DEFAULT_LOG2_ROUNDS = 10
private static final int BCRYPT_SALT_LEN = 16
private static final int BLOWFISH_NUM_ROUNDS = 16
private int[] P
private int[] S
```

- 方法/构造器候选数: 22
```text
private static String encode_base64(byte[] d, int len)
private static byte char64(char x)
private static byte[] decode_base64(String s, int maxolen)
private final void encipher(int[] lr, int off)
private static int[] streamtowords(byte[] data, int[] offp, int[] signp)
private static int streamtoword(byte[] data, int[] offp)
private static int streamtoword_bug(byte[] data, int[] offp)
private void init_key()
private void key(byte[] key, boolean sign_ext_bug)
private void ekskey(byte[] data, byte[] key, boolean sign_ext_bug, int safety)
private byte[] crypt_raw(byte[] password, byte[] salt, int log_rounds, boolean sign_ext_bug, int safety, int[] cdata)
private static byte[] stringToBytes(String plaintext)
public static String hashpw(String password, String salt)
public static String hashpw(byte[] passwordb, String salt)
public static String gensalt(String prefix, int log_rounds, SecureRandom random)
public static String gensalt(String prefix, int log_rounds)
public static String gensalt(int log_rounds, SecureRandom random)
public static String gensalt(int log_rounds)
public static String gensalt()
public static boolean checkpw(String plaintext, String hashed)
public static boolean checkpw(byte[] plaintext, String hashed)
public static String hashpwSHA512(String pwd) throws NoSuchAlgorithmException
```

---

## `org.gms.util` / `util/BasePageUtil.java`

### 类型声明
```text
class BasePageUtil
```

- 字段候选数: 2
```text
private Stream<T> data
private final BasePageDTO basePageDTO
```

- 方法/构造器候选数: 10
```text
private BasePageUtil(Collection<T> data)
private BasePageUtil(Collection<T> data, BasePageDTO basePageDTO)
public static <T> BasePageUtil<T> create(Collection<T> data)
public static <T> BasePageUtil<T> create(Collection<T> data, BasePageDTO basePageDTO)
public static <T> BasePageUtil<T> create(Collection<T> data, Integer pageNo, Integer pageSize)
public static <T> BasePageUtil<T> create(Collection<T> data, boolean onlyTotal, boolean notPage)
public BasePageUtil<T> filter(Predicate<T> predicate)
public BasePageUtil<T> sorted(Comparator<? super T> comparator)
public Page<T> page()
public <R> Page<R> page(Function<T, R> mapper)
```

---

## `org.gms.util` / `util/CashIdGenerator.java`

### 类型声明
```text
class CashIdGenerator
```

- 字段候选数: 1
```text
private static Integer runningCashId = 0
```

- 方法/构造器候选数: 4
```text
public static synchronized void loadExistentCashIdsFromDb()
private static void getNextAvailableCashId()
public static synchronized int generateCashId()
public static synchronized void freeCashId(int cashId)
```

---

## `org.gms.util` / `util/CustomSpringBeanConfig.java`

### 类型声明
```text
class CustomSpringBeanConfig
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public SpringDocConfigProperties springDocConfigProperties()
public SwaggerUiConfigProperties swaggerUiConfigProperties()
```

---

## `org.gms.util` / `util/DatabaseConnection.java`

### 类型声明
```text
class DatabaseConnection
```

- 字段候选数: 0

- 方法/构造器候选数: 1
```text
public static Connection getConnection() throws SQLException
```

---

## `org.gms.util` / `util/ExtendUtil.java`

### 类型声明
```text
class ExtendUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static ExtendValueDO getExtendValue(String extendId, String extendType, String extendName)
public static void saveOrUpdateExtendValue(String extendId, String extendType, String extendName, String extendValue)
```

---

## `org.gms.util` / `util/HexTool.java`

### 类型声明
```text
class HexTool
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public static String toHexString(byte[] bytes)
public static String toCompactHexString(byte[] bytes)
public static byte[] toBytes(String hexString)
private static String removeAllSpaces(String input)
public static String toStringFromCharset(final byte[] bytes)
private static boolean isSpecialCharacter(byte asciiCode)
```

---

## `org.gms.util` / `util/I18nUtil.java`

### 类型声明
```text
class I18nUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
public static String getMessage(String code, Object... args)
public static String getMessage(Locale locale, String code, Object... args)
public static String getLogMessage(String code, Object... args)
public static String getLogMessage(Locale locale, String code, Object... args)
public static String getExceptionMessage(String code, Object... args)
public static String getExceptionMessage(Locale locale, String code, Object... args)
```

---

## `org.gms.util` / `util/IntervalBuilder.java`

### 类型声明
```text
class IntervalBuilder
```

- 字段候选数: 2
```text
private final Lock intervalRlock
private final Lock intervalWlock
```

- 方法/构造器候选数: 7
```text
public IntervalBuilder()
private void refitOverlappedIntervals(int st, int en, int newFrom, int newTo)
private int bsearchInterval(int point)
public void addInterval(int from, int to)
public boolean inInterval(int point)
public boolean inInterval(int from, int to)
public void clear()
```

---

## `org.gms.util` / `util/JwtUtils.java`

### 类型声明
```text
class JwtUtils
```

- 字段候选数: 2
```text
private String jwtSecret
private int jwtDuration
```

- 方法/构造器候选数: 3
```text
public String generateJwtToken(String username)
public String getUserNameFromJwtToken(String token)
public boolean validateJwtToken(String authToken)
```

---

## `org.gms.util` / `util/LRUCache.java`

### 类型声明
```text
class LRUCache
```

- 字段候选数: 1
```text
private final int capacity
```

- 方法/构造器候选数: 3
```text
public LRUCache()
public LRUCache(int capacity)
public boolean removeEldestEntry(Map.Entry<K, V> eldest)
```

---

## `org.gms.util` / `util/NumberTool.java`

### 类型声明
```text
class NumberTool
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static long BytesToLong(byte[] aToConvert)
public static byte[] LongToBytes(long nToConvert)
public static int floatToInt(float f)
public static int doubleToInt(double d)
```

---

## `org.gms.util` / `util/PacketCreator.java`

### 类型声明
```text
class PacketCreator
```

- 字段候选数: 0

- 方法/构造器候选数: 278
```text
public static long getTime(long utcTimestamp)
private static void writeMobSkillId(OutPacket packet, MobSkillId msId)
public static Packet showHpHealed(int cid, int amount)
private static void addRemainingSkillInfo(final OutPacket p, Character chr)
private static void addCharStats(OutPacket p, Character chr)
protected static void addCharLook(final OutPacket p, Character chr, boolean mega)
private static void addCharacterInfo(OutPacket p, Character chr)
private static void addNewYearInfo(OutPacket p, Character chr)
private static void addTeleportInfo(OutPacket p, Character chr)
private static void addMiniGameInfo(OutPacket p, Character chr)
private static void addAreaInfo(OutPacket p, Character chr)
private static void addCharEquips(final OutPacket p, Character chr)
public static Packet setExtraPendantSlot(boolean toggleExtraSlot)
private static void addCharEntry(OutPacket p, Character chr, boolean viewall)
private static void addQuestInfo(OutPacket p, Character chr)
private static void addExpirationTime(final OutPacket p, long time)
private static void addItemInfo(OutPacket p, Item item)
protected static void addItemInfo(final OutPacket p, Item item, boolean zeroPosition)
private static void addInventoryInfo(OutPacket p, Character chr)
private static void addSkillInfo(OutPacket p, Character chr)
private static void addMonsterBookInfo(OutPacket p, Character chr)
public static Packet sendGuestTOS()
public static Packet getHello(short mapleVersion, InitializationVector sendIv, InitializationVector recvIv)
public static Packet getPing()
public static Packet getLoginFailed(int reason)
public static Packet getAfterLoginError(int reason)
public static Packet sendPolice()
public static Packet sendPolice(String text)
public static Packet getPermBan(byte reason)
public static Packet getTempBan(long timestampTill, byte reason)
public static Packet getAuthSuccess(Client c)
private static Packet pinOperation(byte mode)
public static Packet pinRegistered()
public static Packet requestPin()
public static Packet requestPinAfterFailure()
public static Packet registerPin()
public static Packet pinAccepted()
public static Packet wrongPic()
public static Packet getServerList(int serverId, String serverName, int flag, String eventmsg, List<Channel> channelLoad)
public static Packet getEndOfServerList()
public static Packet getServerStatus(int status)
public static Packet getServerIP(InetAddress inetAddr, int port, int clientId)
public static Packet getChannelChange(InetAddress inetAddr, int port)
public static Packet getCharList(Client c, int serverId, int status)
public static Packet enableTV()
public static Packet removeTV()
public static Packet sendTV(Character chr, List<String> messages, int type, Character partner)
public static Packet getCharInfo(Character chr)
public static Packet enableActions()
public static Packet updatePlayerStats(List<Pair<Stat, Integer>> stats, boolean enableActions, Character chr)
public static Packet getWarpToMap(MapleMap to, int spawnPoint, Character chr)
public static Packet getWarpToMap(MapleMap to, int spawnPoint, Point spawnPosition, Character chr)
public static Packet spawnPortal(int townId, int targetId, Point pos)
public static Packet spawnDoor(int ownerid, Point pos, boolean launched)
public static Packet removeDoor(int ownerId, boolean town)
public static Packet spawnSummon(Summon summon, boolean animated)
public static Packet removeSummon(Summon summon, boolean animated)
public static Packet spawnKite(int objId, int itemId, String name, String msg, Point pos, int ft)
public static Packet removeKite(int objId, int animationType)
public static Packet sendCannotSpawnKite()
public static Packet getRelogResponse()
public static Packet serverMessage(String message)
public static Packet serverNotice(int type, String message)
public static Packet serverNotice(int type, String message, int npc)
public static Packet serverNotice(int type, int channel, String message)
public static Packet serverNotice(int type, int channel, String message, boolean smegaEar)
private static Packet serverMessage(int type, int channel, String message, boolean servermessage, boolean megaEar, int npc)
public static Packet getAvatarMega(Character chr, String medal, int channel, int itemId, List<String> message, boolean ear)
public static Packet byeAvatarMega()
public static Packet gachaponMessage(Item item, String town, Character player)
public static Packet spawnNPC(NPC life)
public static Packet spawnNPCRequestController(NPC life, boolean miniMap)
public static Packet spawnMonster(Monster life, boolean newSpawn)
public static Packet spawnMonster(Monster life, boolean newSpawn, int effect)
public static Packet controlMonster(Monster life, boolean newSpawn, boolean aggro)
public static Packet removeMonsterInvisibility(Monster life)
public static Packet makeMonsterInvisible(Monster life)
private static void encodeParentlessMobSpawnEffect(OutPacket p, boolean newSpawn, int effect)
private static void encodeTemporary(OutPacket p, Map<MonsterStatus, MonsterStatusEffect> stati)
private static Packet spawnMonsterInternal(Monster life, boolean requestController, boolean newSpawn, boolean aggro, int effect, boolean makeInvis)
public static Packet spawnFakeMonster(Monster life, int effect)
public static Packet makeMonsterReal(Monster life)
public static Packet stopControllingMonster(int oid)
public static Packet moveMonsterResponse(int objectid, short moveid, int currentMp, boolean useSkills)
public static Packet moveMonsterResponse(int objectid, short moveid, int currentMp, boolean useSkills, int skillId, int skillLevel)
public static Packet getChatText(int cidfrom, String text, boolean gm, int show)
public static Packet getShowExpGain(int gain, int equip, int party, boolean inChat, boolean white)
public static Packet getShowFameGain(int gain)
public static Packet getShowMesoGain(int gain)
public static Packet getShowMesoGain(int gain, boolean inChat)
public static Packet getShowItemGain(int itemId, short quantity)
public static Packet getShowItemGain(int itemId, short quantity, boolean inChat)
public static Packet killMonster(int objId, boolean animation)
public static Packet killMonster(int objId, int animation)
public static Packet updateMapItemObject(MapItem drop, boolean giveOwnership)
public static Packet dropItemFromMapObject(Character player, MapItem drop, Point dropfrom, Point dropto, byte mod)
private static void writeForeignBuffs(OutPacket p, Character chr)
public static Packet spawnPlayerMapObject(Client target, Character chr, boolean enteringField)
private static void encodeNewYearCardInfo(OutPacket p, Character chr)
public static Packet onNewYearCardRes(Character user, int cardId, int mode, int msg)
public static Packet onNewYearCardRes(Character user, NewYearCardRecord newyear, int mode, int msg)
private static void encodeNewYearCard(NewYearCardRecord newyear, OutPacket p)
private static void addRingLook(final OutPacket p, Character chr, boolean crush)
private static void addMarriageRingLook(Client target, final OutPacket p, Character chr)
private static void addAnnounceBox(final OutPacket p, PlayerShop shop, int availability)
private static void addAnnounceBox(final OutPacket p, MiniGame game, int ammount, int joinable)
private static void updateHiredMerchantBoxInfo(OutPacket p, HiredMerchant hm)
public static Packet updateHiredMerchantBox(HiredMerchant hm)
private static void updatePlayerShopBoxInfo(OutPacket p, PlayerShop shop)
public static Packet updatePlayerShopBox(PlayerShop shop)
public static Packet removePlayerShopBox(PlayerShop shop)
public static Packet facialExpression(Character from, int expression)
private static void rebroadcastMovementList(OutPacket op, InPacket ip, long movementDataLength)
private static void serializeMovementList(OutPacket p, List<LifeMovementFragment> moves)
public static Packet movePlayer(int chrId, InPacket movementPacket, long movementDataLength)
public static Packet moveSummon(int cid, int oid, Point startPos, InPacket movementPacket, long movementDataLength)
public static Packet moveMonster(int oid, boolean skillPossible, int skill, int skillId, int skillLevel, int pOption, Point startPos, InPacket movementPacket, long movementDataLength)
public static Packet summonAttack(int cid, int summonOid, byte direction, List<SummonAttackEntry> allDamage)
public static Packet closeRangeAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, Map<Integer, List<Integer>> damage, int speed, int direction, int display)
public static Packet rangedAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, int projectile, Map<Integer, List<Integer>> damage, int speed, int direction, int display)
public static Packet magicAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, Map<Integer, List<Integer>> damage, int charge, int speed, int direction, int display)
private static void addAttackBody(OutPacket p, Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, int projectile, Map<Integer, List<Integer>> damage, int speed, int direction, int display)
public static Packet throwGrenade(int cid, Point pos, int keyDown, int skillId, int skillLevel)
private static int doubleToShortBits(double d)
public static Packet getNPCShop(Client c, int sid, List<ShopItem> items)
public static Packet shopTransaction(byte code)
public static Packet updateInventorySlotLimit(int type, int newLimit)
public static Packet modifyInventory(boolean updateTick, final List<ModifyInventory> mods)
public static Packet getScrollEffect(int chr, ScrollResult scrollSuccess, boolean legendarySpirit, boolean whiteScroll)
public static Packet removePlayerFromMap(int chrId)
public static Packet catchMessage(int message)
public static Packet showAllCharacter(int totalWorlds, int totalChrs)
public static Packet showAriantScoreBoard()
public static Packet updateAriantPQRanking(final Character chr, final int score)
public static Packet updateAriantPQRanking(Map<Character, Integer> playerScore)
public static Packet updateWitchTowerScore(int score)
public static Packet silentRemoveItemFromMap(int objId)
public static Packet removeItemFromMap(int objId, int animation, int chrId)
public static Packet removeItemFromMap(int objId, int animation, int chrId, boolean pet, int slot)
public static Packet updateCharLook(Client target, Character chr)
public static Packet damagePlayer(int skill, int monsteridfrom, int cid, int damage, int fake, int direction, boolean pgmr, int pgmr_1, boolean is_pg, int oid, int pos_x, int pos_y)
public static Packet sendMapleLifeCharacterInfo()
public static Packet sendMapleLifeNameError()
public static Packet sendMapleLifeError(int code)
public static Packet charNameResponse(String charname, boolean nameUsed)
public static Packet addNewCharEntry(Character chr)
public static Packet deleteCharResponse(int cid, int state)
public static Packet selectWorld(int world)
public static Packet sendRecommended(List<Pair<Integer, String>> worlds)
public static Packet charInfo(Character chr)
public static Packet giveBuff(int buffid, int bufflength, List<Pair<BuffStat, Integer>> statups)
public static Packet showMonsterRiding(int cid, Mount mount)
public static Packet forfeitQuest(short quest)
public static Packet completeQuest(short quest, long time)
public static Packet updateQuestInfo(short quest, int npc)
public static Packet onNotifyHPDecByField(int change)
public static Packet addQuestTimeLimit(final short quest, final int time)
public static Packet removeQuestTimeLimit(final short quest)
public static Packet updateQuest(Character chr, QuestStatus qs, boolean infoUpdate)
private static void writeLongMaskD(final OutPacket p, List<Pair<Disease, Integer>> statups)
public static Packet giveDebuff(List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet giveForeignDebuff(int chrId, List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet cancelForeignFirstDebuff(int cid, long mask)
public static Packet cancelForeignDebuff(int cid, long mask)
public static Packet giveForeignBuff(int chrId, List<Pair<BuffStat, Integer>> statups)
public static Packet cancelForeignBuff(int chrId, List<BuffStat> statups)
public static Packet cancelBuff(List<BuffStat> statups)
private static void writeLongMask(final OutPacket p, List<Pair<BuffStat, Integer>> statups)
private static void writeLongMaskFromList(OutPacket p, List<BuffStat> statups)
private static void writeLongEncodeTemporaryMask(final OutPacket p, Collection<MonsterStatus> stati)
public static Packet cancelDebuff(long mask)
private static void writeLongMaskSlowD(final OutPacket p)
public static Packet giveForeignSlowDebuff(int chrId, List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet cancelForeignSlowDebuff(int chrId)
private static void writeLongMaskChair(OutPacket p)
public static Packet giveForeignChairSkillEffect(int cid)
public static Packet giveForeignWKChargeEffect(int cid, int buffid, List<Pair<BuffStat, Integer>> statups)
public static Packet cancelForeignChairSkillEffect(int chrId)
public static Packet getPlayerShopChat(Character chr, String chat, boolean owner)
public static Packet getPlayerShopNewVisitor(Character chr, int slot)
public static Packet getPlayerShopRemoveVisitor(int slot)
public static Packet getTradePartnerAdd(Character chr)
public static Packet tradeInvite(Character chr)
public static Packet getTradeMesoSet(byte number, int meso)
public static Packet getTradeItemAdd(byte number, Item item)
public static Packet getPlayerShopItemUpdate(PlayerShop shop)
public static Packet getPlayerShopOwnerUpdate(PlayerShop.SoldItem item, int position)
public static Packet getPlayerShop(PlayerShop shop, boolean owner)
public static Packet getTradeStart(Client c, Trade trade, byte number)
public static Packet getTradeConfirmation()
public static Packet getTradeResult(byte number, byte operation)
public static Packet getNPCTalk(int npc, byte msgType, String talk, String endBytes, byte speaker)
public static Packet getDimensionalMirror(String talk)
public static Packet getNPCTalkStyle(int npc, String talk, int[] styles)
public static Packet getNPCTalkNum(int npc, String talk, int def, int min, int max)
public static Packet getNPCTalkText(int npc, String talk, String def)
public static Packet getNPCTalkNum(int npc, String talk, int def, int min, int max,byte speaker)
public static Packet getNPCTalkText(int npc, String talk, String def,byte speaker)
public static Packet OnAskQuiz(int nSpeakerTypeID, int nSpeakerTemplateID, int nResCode, String sTitle, String sProblemText, String sHintText, int nMinInput, int nMaxInput, int tRemainInitialQuiz)
public static Packet OnAskSpeedQuiz(int nSpeakerTypeID, int nSpeakerTemplateID, int nResCode, int nType, int dwAnswer, int nCorrect, int nRemain, int tRemainInitialQuiz)
public static Packet showBuffEffect(int chrId, int skillId, int effectId)
public static Packet showBuffEffect(int chrId, int skillId, int effectId, byte direction)
public static Packet showBuffEffect(int chrId, int skillId, int skillLv, int effectId, byte direction)
public static Packet showOwnBuffEffect(int skillId, int effectId)
public static Packet showOwnBerserk(int skilllevel, boolean Berserk)
public static Packet showBerserk(int chrId, int skillLv, boolean berserk)
public static Packet updateSkill(int skillId, int level, int masterlevel, long expiration)
public static Packet getShowQuestCompletion(int id)
public static Packet getKeymap(Map<Integer, KeyBinding> keybindings)
public static Packet QuickslotMappedInit(QuickslotBinding pQuickslot)
public static Packet getInventoryFull()
public static Packet getShowInventoryFull()
public static Packet showItemUnavailable()
public static Packet getShowInventoryStatus(int mode)
public static Packet getStorage(int npcId, byte slots, Collection<Item> items, int meso)
public static Packet getStorageError(byte i)
public static Packet mesoStorage(byte slots, int meso)
public static Packet storeStorage(byte slots, InventoryType type, Collection<Item> items)
public static Packet takeOutStorage(byte slots, InventoryType type, Collection<Item> items)
public static Packet arrangeStorage(byte slots, Collection<Item> items)
public static Packet showMonsterHP(int oid, int remhppercentage)
public static Packet showBossHP(int oid, int currHP, int maxHP, byte tagColor, byte tagBgColor)
public static Packet customShowBossHP(byte call, int oid, long currHP, long maxHP, byte tagColor, byte tagBgColor)
public static Packet giveFameResponse(int mode, String charname, int newfame)
public static Packet giveFameErrorResponse(int status)
public static Packet receiveFame(int mode, String charnameFrom)
public static Packet partyCreated(Party party, int partycharid)
public static Packet partyInvite(Character from)
public static Packet partySearchInvite(Character from)
public static Packet partyStatusMessage(int message)
public static Packet partyStatusMessage(int message, String charname)
private static void addPartyStatus(int forchannel, Party party, OutPacket p, boolean leaving)
public static Packet updateParty(int forChannel, Party party, PartyOperation op, PartyCharacter target)
public static Packet partyPortal(int townId, int targetId, Point position)
public static Packet updatePartyMemberHP(int cid, int curhp, int maxhp)
public static Packet multiChat(String name, String chattext, int mode)
private static void writeIntMask(OutPacket p, Map<MonsterStatus, Integer> stats)
public static Packet applyMonsterStatus(final int oid, final MonsterStatusEffect mse, final List<Integer> reflection)
public static Packet cancelMonsterStatus(int oid, Map<MonsterStatus, Integer> stats)
public static Packet getClock(Number time)
public static Packet getClockTime(int hour, int min, int sec)
public static Packet removeClock()
public static Packet spawnMobMist(int objId, int ownerMobId, MobSkillId msId, Mist mist)
public static Packet spawnMist(int objId, int ownerId, int skill, int level, Mist mist)
public static Packet removeMist(int objId)
public static Packet damageSummon(int cid, int oid, int damage, int monsterIdFrom)
public static Packet damageMonster(int oid, int damage)
public static Packet healMonster(int oid, int heal, int curhp, int maxhp)
private static Packet damageMonster(int oid, int damage, int curhp, int maxhp)
public static Packet updateBuddylist(Collection<BuddylistEntry> buddylist)
public static Packet buddylistMessage(byte message)
public static Packet requestBuddylistAdd(int chrIdFrom, int chrId, String nameFrom)
public static Packet updateBuddyChannel(int characterid, int channel)
public static Packet itemEffect(int characterid, int itemid)
public static Packet updateBuddyCapacity(int capacity)
public static Packet showChair(int characterid, int itemid)
public static Packet cancelChair(int id)
public static Packet spawnReactor(Reactor reactor)
public static Packet triggerReactor(Reactor reactor, int stance)
public static Packet destroyReactor(Reactor reactor)
public static Packet musicChange(String song)
public static Packet showEffect(String effect)
public static Packet playSound(String sound)
public static Packet environmentChange(String env, int mode)
public static Packet environmentMove(String env, int mode)
public static Packet environmentMoveList(Set<Entry<String, Integer>> envList)
public static Packet environmentMoveReset()
public static Packet startMapEffect(String msg, int itemId, boolean active)
public static Packet removeMapEffect()
public static Packet mapEffect(String path)
public static Packet mapSound(String path)
public static Packet skillEffect(Character from, int skillId, int level, byte flags, int speed, byte direction)
public static Packet skillCancel(Character from, int skillId)
public static Packet catchMonster(int mobOid, byte success)
public static Packet catchMonster(int mobOid, int itemid, byte success)
public static Packet sendHint(String hint, int width, int height)
public static Packet messengerInvite(String from, int messengerid)
public static Packet OnCoupleMessage(String fiance, String text, boolean spouse)
```

---

## `org.gms.util` / `util/Pair.java`

### 类型声明
```text
class Pair
```

- 字段候选数: 2
```text
public E left
public F right
```

- 方法/构造器候选数: 6
```text
public Pair(E left, F right)
public E getLeft()
public F getRight()
public String toString()
public int hashCode()
public boolean equals(Object obj)
```

---

## `org.gms.util` / `util/Quartet.java`

### 类型声明
```text
class Quartet
```

- 字段候选数: 4
```text
private A first
private B second
private C third
private D fourth
```

- 方法/构造器候选数: 0

---

## `org.gms.util` / `util/Randomizer.java`

### 类型声明
```text
class Randomizer
```

- 字段候选数: 0

- 方法/构造器候选数: 8
```text
public static int nextInt()
public static int nextInt(final int arg0)
public static void nextBytes(final byte[] bytes)
public static boolean nextBoolean()
public static double nextDouble()
public static float nextFloat()
public static long nextLong()
public static int rand(final int lbound, final int ubound)
```

---

## `org.gms.util` / `util/RateLimitUtil.java`

### 类型声明
```text
class RateLimitUtil
```

- 字段候选数: 2
```text
private static RateLimitUtil instance
private final ServiceProperty.RateLimitProperty rateLimitProperty
```

- 方法/构造器候选数: 3
```text
private RateLimitUtil()
public static RateLimitUtil getInstance()
public boolean check(String ip)
```

---

## `org.gms.util` / `util/RequireUtil.java`

### 类型声明
```text
class RequireUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 13
```text
public static void requireNull(Object obj)
public static void requireNull(Object obj, String msg)
public static void requireNotNull(Object obj)
public static void requireNotNull(Object obj, String msg)
public static void requireNotEmpty(Object obj)
public static void requireNotEmpty(Object obj, String msg)
public static void requireTrue(boolean b, String msg)
public static void requireFalse(boolean b, String msg)
public static boolean isEmpty(Object obj)
public static boolean isZero(Number obj)
public static void requireNotEmptyOrElse(Object obj, Runnable runnable)
public static void requireNotEmptyAndThen(Object obj, Runnable runnable)
public static <T, R> void requireNotEmptyAndThen(T t, R r, BiConsumer<T, R> consumer)
```

---

## `org.gms.util` / `util/StringUtil.java`

### 类型声明
```text
class StringUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 7
```text
public static String getLeftPaddedStr(String in, char padchar, int length)
public static String getRightPaddedStr(String in, char padchar, int length)
public static String joinStringFrom(String[] arr, int start)
public static String joinStringFrom(String[] arr, int start, String sep)
public static String makeEnumHumanReadable(String enumName)
public static int countCharacters(String str, char chr)
public static boolean isNumeric(String str)
```

---

## `org.gms.util` / `util/ThreadLocalUtil.java`

### 类型声明
```text
class ThreadLocalUtil
```

- 字段候选数: 0

- 方法/构造器候选数: 4
```text
public static void setCurrentClient(Client c)
public static Client getCurrentClient()
public static void removeCurrentClient()
public static int getClientLang()
```

---

## `org.gms.util` / `util/Trio.java`

### 类型声明
```text
class Trio
```

- 字段候选数: 3
```text
private A first
private B second
private C third
```

- 方法/构造器候选数: 0

---

## `org.gms.util.packets` / `util/packets/Fishing.java`

### 类型声明
```text
class Fishing
```

- 字段候选数: 0

- 方法/构造器候选数: 6
```text
private static double getFishingLikelihood(int x)
public static double[] fetchFishingLikelihood()
private static boolean hitFishingTime(Character chr, int baitLevel, double yearLikelihood, double timeLikelihood)
public static void doFishing(Character chr, int baitLevel, double yearLikelihood, double timeLikelihood)
public static int getRandomItem()
private static void debugFishingLikelihood()
```

---

## `org.gms.util.packets` / `util/packets/WeddingPackets.java`

### 类型声明
```text
class WeddingPackets
class Field_Wedding
class Field_WeddingPhoto
class GW_WeddingReservation
class WeddingWishList
class GW_WeddingWishList
enum MarriageStatus
enum MarriageRequest
enum WeddingType
enum WeddingMap
enum WeddingItem
```

- 字段候选数: 0

- 方法/构造器候选数: 2
```text
public static Packet onMarriageRequest(String name, int playerid)
public static Packet onTakePhoto(String ReservedGroomName, String ReservedBrideName, int m_dwField, List<Character> m_dwUsers)
```

---
