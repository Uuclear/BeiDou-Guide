# gms-server 源码索引（公开类型与方法签名）

> 本文件由 `scripts/generate-gms-server-api-index.py` **自动生成**，用于在约 1100+ 个 Java 源文件中快速定位类与公开方法。
> 叙述性说明见 [09-源码深度导读.md](../09-源码深度导读.md)。

> 生成所用源码根目录：环境变量 `BEIDOU_SERVER_ROOT` 指向的 `gms-server`，或脚本自动探测到的本地 clone。
> 本次生成使用的 `gms-server` 路径（相对本仓库根目录，若无法相对则给绝对路径）：`BeiDou-Server/gms-server`
> 源文件数：1116

---

## `org.gms`

### `org.gms.ServerApplication`
- 声明: `public class ServerApplication {`
- 方法数（启发式提取）: 1

```text
public static void main(String[] args)
```

## `org.gms.aop`

### `org.gms.aop.AuthEntryPointJwt`
- 声明: `public class AuthEntryPointJwt implements AuthenticationEntryPoint {`
- 方法数（启发式提取）: 1

```text
public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException authException) throws IOException, ServletException
```

### `org.gms.aop.AuthTokenFilter`
- 声明: `public class AuthTokenFilter extends OncePerRequestFilter {`
- 方法数（启发式提取）: 0

### `org.gms.aop.ServerFilter`
- 声明: `public class ServerFilter extends HttpFilter {`
- 方法数（启发式提取）: 8

```text
public CachedHttpServletRequest(HttpServletRequest request) throws IOException
public BufferedReader getReader()
public ServletInputStream getInputStream()
public CachedServletInputStream(byte[] cachedBody)
public boolean isFinished()
public boolean isReady()
public void setReadListener(ReadListener listener)
public int read()
```

## `org.gms.client`

### `org.gms.client.AbstractCharacterListener`
- 声明: `public interface AbstractCharacterListener {`
- 方法数（启发式提取）: 0

### `org.gms.client.AbstractCharacterObject`
- 声明: `public abstract class AbstractCharacterObject extends AbstractAnimatedMapObject {`
- 方法数（启发式提取）: 47

```text
public int getStr()
public int getDex()
public int getInt()
public int getLuk()
public int getRemainingAp()
public int[] getRemainingSps()
public int getHpMpApUsed()
public boolean isAlive()
public int getHp()
public int getMp()
public int getMaxHp()
public int getMaxMp()
public int getCurrentMaxHp()
public int getCurrentMaxMp()
public void setRemainingSp(int remainingSp, int skillbook)
public void healHpMp()
public void updateHpMp(int x)
public void updateHpMp(int newhp, int newmp)
public void changeHpMp(int newhp, int newmp, boolean silent)
public void updateHp(int hp)
public void updateMaxHp(int maxhp)
public void updateHpMaxHp(int hp, int maxhp)
public void updateMp(int mp)
public void updateMaxMp(int maxmp)
public void updateMpMaxMp(int mp, int maxmp)
public void updateMaxHpMaxMp(int maxhp, int maxmp)
public int safeAddHP(int delta)
public void addHP(int delta)
public void addMP(int delta)
public void addMPHP(int hpDelta, int mpDelta)
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
public boolean assignStrDexIntLuk(int deltaStr, int deltaDex, int deltaInt, int deltaLuk)
public void updateStrDexIntLuk(int x)
public void changeRemainingAp(int x, boolean silent)
public void gainAp(int deltaAp, boolean silent)
public void gainSp(int deltaSp, int skillbook, boolean silent)
```

### `org.gms.client.BuddyList`
- 声明: `public class BuddyList {`
- 方法数（启发式提取）: 16

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

### `org.gms.client.BuddylistEntry`
- 声明: `public class BuddylistEntry {`
- 方法数（启发式提取）: 12

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

### `org.gms.client.BuffStat`
- 声明: `public enum BuffStat {`
- 方法数（启发式提取）: 3

```text
public long getValue()
public boolean isFirst()
public String toString()
```

### `org.gms.client.Character`
- 声明: `public class Character extends AbstractCharacterObject {`
- 方法数（启发式提取）: 525

```text
public Job getJobStyle(byte opt)
public Job getJobStyle()
public static Character getDefault(Client c)
public boolean isLoggedInWorld()
public boolean isAwayFromWorld()
public void setEnteredChannelWorld()
public void setAwayFromChannelWorld()
public void setDisconnectedFromChannelWorld()
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
public static boolean canCreateChar(String name)
public static boolean existName(String name)
public boolean canDoor()
public void setHasSandboxItem()
public void removeSandboxItems()
public void changeCI(int type)
public void setMasteries(int jobId)
public synchronized void changeJob(Job newJob)
public void broadcastAcquaintances(int type, String message)
public void broadcastAcquaintances(Packet packet)
public void changeKeybinding(int key, KeyBinding keybinding)
public void changeQuickslotKeybinding(byte[] aQuickslotKeyMapped)
public void broadcastStance(int newStance)
public void broadcastStance()
public MapleMap getWarpMap(int map)
public void warpAhead(int map)
public boolean canRecoverLastBanish()
public Pair<Integer, Integer> getLastBanishData()
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
public List<Integer> getLastVisitedMapIds()
public void partyOperationUpdate(Party party, List<Character> exPartyMembers)
public void visitMap(MapleMap map)
public void setOwnedMap(MapleMap map)
public MapleMap getOwnedMap()
public void notifyMapTransferToPartner(int mapid)
public void removeIncomingInvites()
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
public void deleteBuddy(int otherCid)
public static boolean deleteCharFromDB(Character player, int senderAccId)
public void disbandGuild()
public void dispel()
public final boolean hasDisease(final Disease dis)
public final int getDiseasesSize()
public Map<Disease, Pair<Long, MobSkill>> getAllDiseases()
public void silentApplyDiseases(Map<Disease, Pair<Long, MobSkill>> diseaseMap)
public void announceDiseases()
public void collectDiseases()
public void giveDebuff(final Disease disease, MobSkill skill)
public void dispelDebuff(Disease debuff)
public void dispelDebuffs()
public void purgeDebuffs()
public void cancelAllDebuffs()
public void dispelSkill(int skillid)
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
public List<PlayerBuffValueHolder> getAllBuffs()
public boolean hasBuffFromSourceid(int sourceid)
public boolean hasActiveBuff(int sourceid)
public void debugListAllBuffs()
public void cancelAllBuffs(boolean softcancel)
public void cancelEffect(int itemId)
public boolean cancelEffect(StatEffect effect, boolean overwrite, long startTime)
public void updateActiveEffects()
public void cancelEffectFromBuffStat(BuffStat stat)
public void cancelBuffStats(BuffStat stat)
public void registerEffect(StatEffect effect, long starttime, long expirationtime, boolean isSilent)
public boolean unregisterChairBuff()
public boolean registerChairBuff()
public int getChair()
public String getChalkboard()
public AbstractPlayerInteraction getAbstractPlayerInteraction()
public final List<QuestStatus> getCompletedQuests()
public List<Ring> getCrushRings()
public Collection<Door> getDoors()
public Door getPlayerDoor()
public Door getMainTownDoor()
public void applyPartyDoor(Door door, boolean partyUpdate)
public Door removePartyDoor(boolean partyUpdate)
public EventInstanceManager getEventInstance()
public Marriage getMarriageInstance()
public void resetExcluded(int petId)
public void addExcluded(int petId, int x)
public void commitExcludedItems()
public void exportExcludedItems(Client c)
public Map<Integer, Set<Integer>> getExcluded()
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
public Map<Skill, SkillEntry> getSkills()
public Map<Skill, SkillEntry> getEditableSkills()
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
public synchronized void levelUp(boolean takeexp)
public boolean leaveParty()
public void setPlayerRates()
public void revertLastPlayerRates()
public void revertPlayerRates()
public void setWorldRates()
public void revertWorldRates()
public void setCouponRates()
public void updateCouponRates()
public void resetPlayerRates()
public void dispelBuffCoupons()
public Set<Integer> getActiveCoupons()
public void addPlayerRing(Ring ring)
public static Character loadCharacterEntryFromDB(ResultSet rs, List<Item> equipped)
public Character generateCharacterEntry()
public int getRemainingSp()
public void updateRemainingSp(int remainingSp)
public static Character fromCharactersDO(CharactersDO charactersDO, Client client)
public static CharactersDO toCharactersDO(Character chr)
public static Character loadCharFromDB(final int cid, Client client, boolean channelServer)
public void reloadQuestExpirations()
public static String makeMapleReadable(String in)
public BuffStatValueHolder(StatEffect effect, long startTime, int value)
public CooldownValueHolder(int skillId, long startTime, long length)
public void message(String m)
public void yellowMessage(String m)
public void raiseQuestMobCount(int id)
public Mount mount(int id, int skillid)
public void sitChair(int itemId)
public void respawn(int returnMap)
public void respawn(EventInstanceManager eim, int returnMap)
public void reapplyLocalStats()
public List<Pair<Stat, Integer>> recalcLocalStats()
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
public int sellAllItemsFromName(byte invTypeId, String name)
public int sellAllItemsFromPosition(ItemInformationProvider ii, InventoryType type, short pos)
public boolean mergeAllItemsFromName(String name)
public void mergeAllItemsFromPosition(Map<StatUpgrade, Float> statUps, short pos)
public void setSlot(int slotid)
public void shiftPetsRight()
public void showDojoClock()
public void showUnderLeveledInfo(Monster mob)
public void showMapOwnershipInfo(Character mapOwner)
public void showHint(String msg)
public void showHint(String msg, int length)
public void silentGiveBuffs(List<Pair<Long, PlayerBuffValueHolder>> buffs)
public void silentPartyUpdate()
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
public void setQuestProgress(int id, int infoNumber, String progress)
public void awardQuestPoint(int awardedPoints)
public void announceUpdateQuest(DelayedQuestUpdate questUpdateType, Object... params)
public void flushDelayedUpdateQuests()
public void updateQuestStatus(QuestStatus qs)
public void cancelQuestExpirationTask()
public void forfeitExpirableQuests()
public void questExpirationTask()
public void questTimeLimit(final Quest quest, int seconds)
public void questTimeLimit2(final Quest quest, long expires)
public void updateSingleStat(Stat stat, int newval)
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
public void blockPortal(String scriptName)
public void unblockPortal(String scriptName)
public boolean containsAreaInfo(int area, String info)
public void updateAreaInfo(int area, String info)
public Map<Short, String> getAreaInfos()
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

### `org.gms.client.CharacterListener`
- 声明: `public class CharacterListener implements AbstractCharacterListener {`
- 方法数（启发式提取）: 5

```text
public CharacterListener(Character character)
public void onHpChanged(int oldHp)
public void onHpMpPoolUpdate()
public void onStatUpdate()
public void onAnnounceStatPoolUpdate()
```

### `org.gms.client.CharacterNameAndId`
- 声明: `public class CharacterNameAndId {`
- 方法数（启发式提取）: 3

```text
public CharacterNameAndId(int id, String name)
public int getId()
public String getName()
```

### `org.gms.client.Client`
- 声明: `public class Client extends ChannelInboundHandlerAdapter {`
- 方法数（启发式提取）: 119

```text
public Client(Type type, long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createLoginClient(long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createChannelClient(long sessionId, String remoteAddress, PacketProcessor packetProcessor, int world, int channel)
public static Client createMock()
public void channelActive(ChannelHandlerContext ctx)
public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception
public void userEventTriggered(ChannelHandlerContext ctx, Object event)
public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception
public void channelInactive(ChannelHandlerContext ctx)
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
public boolean isLoggedIn()
public boolean hasBannedIP()
public int getVoteTime()
public void resetVoteTime()
public boolean hasVotedAlready()
public boolean hasBannedHWID()
public boolean hasBannedMac()
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
public final void disconnect(final boolean shutdown, final boolean cashshop)
public final void forceDisconnect()
public void timeoutDisconnect()
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
public void lockClient()
public void unlockClient()
public boolean tryacquireClient()
public void releaseClient()
public boolean tryacquireEncoder()
public void unlockEncoder()
public CharNameAndId(String name, int id)
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

### `org.gms.client.DefaultDates`
- 声明: `(未解析) DefaultDates`
- 方法数（启发式提取）: 2

```text
public static LocalDate getBirthday()
public static LocalDateTime getTempban()
```

### `org.gms.client.Disease`
- 声明: `public enum Disease {`
- 方法数（启发式提取）: 6

```text
public long getValue()
public boolean isFirst()
public MobSkillType getMobSkillType()
public static Disease ordinal(int ord)
public static final Disease getRandom()
public static final Disease getBySkill(MobSkillType skill)
```

### `org.gms.client.DiseaseValueHolder`
- 声明: `public class DiseaseValueHolder {`
- 方法数（启发式提取）: 1

```text
public DiseaseValueHolder(long start, long length)
```

### `org.gms.client.Family`
- 声明: `public class Family {`
- 方法数（启发式提取）: 21

```text
public Family(int id, int world)
public int getID()
public int getWorld()
public void setLeader(FamilyEntry leader)
public FamilyEntry getLeader()
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

### `org.gms.client.FamilyEntitlement`
- 声明: `public enum FamilyEntitlement {`
- 方法数（启发式提取）: 4

```text
public int getUsageLimit()
public int getRepCost()
public String getName()
public String getDescription()
```

### `org.gms.client.FamilyEntry`
- 声明: `public class FamilyEntry {`
- 方法数（启发式提取）: 44

```text
public FamilyEntry(Family family, int characterID, String charName, int level, Job job)
public Character getChr()
public void setCharacter(Character newCharacter)
public synchronized void join(FamilyEntry senior)
public synchronized void fork()
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
public void giveReputationToSenior(int gain, boolean includeSuperSenior)
public int getTotalReputation()
public void setTotalReputation(int totalReputation)
public FamilyEntry getSenior()
public synchronized boolean setSenior(FamilyEntry senior, boolean save)
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

### `org.gms.client.Job`
- 声明: `public enum Job {`
- 方法数（启发式提取）: 6

```text
public static int getMax()
public static Job getById(int id)
public static Job getBy5ByteEncoding(int encoded)
public boolean isA(Job basejob)
public int getJobNiche()
public static Job getJobStyleInternal(int jobid, byte opt)
```

### `org.gms.client.MonsterBook`
- 声明: `public final class MonsterBook {`
- 方法数（启发式提取）: 11

```text
public MonsterBook(int cid)
public Set<Entry<Integer, Integer>> getCardSet()
public void addCard(final Client c, final int cardid)
public int getBookLevel()
public Map<Integer, Integer> getCards()
public int getTotalCards()
public int getNormalCard()
public int getSpecialCard()
public void loadCards(final int chrId)
public void saveCards(Connection con, int chrId) throws SQLException
public static int[] getCardTierSize()
```

### `org.gms.client.Mount`
- 声明: `public class Mount {`
- 方法数（启发式提取）: 16

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

### `org.gms.client.QuestStatus`
- 声明: `public class QuestStatus {`
- 方法数（启发式提取）: 36

```text
public int getId()
public static Status getById(int id)
public QuestStatus(Quest quest, Status status)
public QuestStatus(Quest quest, Status status, int npc)
public Quest getQuest()
public short getQuestID()
public Status getStatus()
public final void setStatus(Status status)
public boolean wasUpdated()
public void resetUpdated()
public int getNpc()
public final void setNpc(int npc)
public boolean addMedalMap(int mapid)
public int getMedalProgress()
public List<Integer> getMedalMaps()
public boolean progress(int id)
public void setProgress(int id, String pr)
public boolean madeProgress()
public String getProgress(int id)
public void resetProgress(int id)
public void resetAllProgress()
public Map<Integer, String> getProgress()
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

### `org.gms.client.Ring`
- 声明: `public class Ring implements Comparable<Ring> {`
- 方法数（启发式提取）: 15

```text
public Ring(int id, int id2, int partnerId, int itemid, String partnername)
public static Ring loadFromDb(int ringId)
public static void removeRing(final Ring ring)
public static Pair<Integer, Integer> createRing(int itemid, final Character partner1, final Character partner2)
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

### `org.gms.client.Skill`
- 声明: `public class Skill {`
- 方法数（启发式提取）: 14

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

### `org.gms.client.SkillFactory`
- 声明: `public class SkillFactory {`
- 方法数（启发式提取）: 3

```text
public static Skill getSkill(int id)
public static void loadAllSkills()
public static String getSkillName(int skillid)
```

### `org.gms.client.SkillMacro`
- 声明: `public class SkillMacro {`
- 方法数（启发式提取）: 10

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

### `org.gms.client.SkinColor`
- 声明: `public enum SkinColor {`
- 方法数（启发式提取）: 2

```text
public int getId()
public static SkinColor getById(int id)
```

### `org.gms.client.Stat`
- 声明: `public enum Stat {`
- 方法数（启发式提取）: 4

```text
public int getValue()
public static Stat getByValue(int value)
public static Stat getBy5ByteEncoding(int encoded)
public static Stat getByString(String type)
```

## `org.gms.client.autoban`

### `org.gms.client.autoban.AutobanFactory`
- 声明: `public enum AutobanFactory {`
- 方法数（启发式提取）: 13

```text
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
public static Collection<Integer> getIgnoredChrIds()
```

### `org.gms.client.autoban.AutobanManager`
- 声明: `public class AutobanManager {`
- 方法数（启发式提取）: 8

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

## `org.gms.client.command`

### `org.gms.client.command.Command`
- 声明: `public abstract class Command {`
- 方法数（启发式提取）: 1

```text
public abstract void execute(Client client, String[] params)
```

### `org.gms.client.command.CommandsExecutor`
- 声明: `public class CommandsExecutor {`
- 方法数（启发式提取）: 3

```text
public static boolean isCommand(Client client, String content)
public void loadCommandsExecutor()
public void handle(Client client, String message)
```

## `org.gms.client.command.commands.gm0`

### `org.gms.client.command.commands.gm0.ChangeLanguageCommand`
- 声明: `public class ChangeLanguageCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.DisposeCommand`
- 声明: `public class DisposeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.DropLimitCommand`
- 声明: `public class DropLimitCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.EnableAuthCommand`
- 声明: `public class EnableAuthCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.EquipLvCommand`
- 声明: `public class EquipLvCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.GachaCommand`
- 声明: `public class GachaCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.GmCommand`
- 声明: `public class GmCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.HelpCommand`
- 声明: `public class HelpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm0.JoinEventCommand`
- 声明: `public class JoinEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.LeaveEventCommand`
- 声明: `public class LeaveEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.MapOwnerClaimCommand`
- 声明: `public class MapOwnerClaimCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.OnlineCommand`
- 声明: `public class OnlineCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.RanksCommand`
- 声明: `public class RanksCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.RatesCommand`
- 声明: `public class RatesCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.ReadPointsCommand`
- 声明: `public class ReadPointsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm0.ReportBugCommand`
- 声明: `public class ReportBugCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.ShowRatesCommand`
- 声明: `public class ShowRatesCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.StaffCommand`
- 声明: `public class StaffCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.StatDexCommand`
- 声明: `public class StatDexCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.StatIntCommand`
- 声明: `public class StatIntCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.StatLukCommand`
- 声明: `public class StatLukCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.StatStrCommand`
- 声明: `public class StatStrCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.TimeCommand`
- 声明: `public class TimeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm0.ToggleExpCommand`
- 声明: `public class ToggleExpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm0.UptimeCommand`
- 声明: `public class UptimeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm1`

### `org.gms.client.command.commands.gm1.BossHpCommand`
- 声明: `public class BossHpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm1.BuffMeCommand`
- 声明: `public class BuffMeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm1.GotoCommand`
- 声明: `public class GotoCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm1.MobHpCommand`
- 声明: `public class MobHpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm1.WhatDropsFromCommand`
- 声明: `public class WhatDropsFromCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm1.WhoDropsCommand`
- 声明: `public class WhoDropsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm2`

### `org.gms.client.command.commands.gm2.ApCommand`
- 声明: `public class ApCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.BombCommand`
- 声明: `public class BombCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.BuffCommand`
- 声明: `public class BuffCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.BuffMapCommand`
- 声明: `public class BuffMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.ClearDropsCommand`
- 声明: `public class ClearDropsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.ClearSavedLocationsCommand`
- 声明: `public class ClearSavedLocationsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.ClearSlotCommand`
- 声明: `public class ClearSlotCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.DcCommand`
- 声明: `public class DcCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.EmpowerMeCommand`
- 声明: `public class EmpowerMeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.GachaListCommand`
- 声明: `public class GachaListCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.GmShopCommand`
- 声明: `public class GmShopCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.HealCommand`
- 声明: `public class HealCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.HideCommand`
- 声明: `public class HideCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.IdCommand`
- 声明: `public class IdCommand extends Command {`
- 方法数（启发式提取）: 4

```text
public HandbookFileItems(List<String> fileLines)
public List<HandbookItem> search(String query)
public boolean matches(String query)
public void execute(Client client, final String[] params)
```

### `org.gms.client.command.commands.gm2.ItemCommand`
- 声明: `public class ItemCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.ItemDropCommand`
- 声明: `public class ItemDropCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.JailCommand`
- 声明: `public class JailCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.JobCommand`
- 声明: `public class JobCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.LevelCommand`
- 声明: `public class LevelCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.LevelProCommand`
- 声明: `public class LevelProCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.LootCommand`
- 声明: `public class LootCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.MaxSkillCommand`
- 声明: `public class MaxSkillCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.MaxStatCommand`
- 声明: `public class MaxStatCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.MobSkillCommand`
- 声明: `public class MobSkillCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm2.ReachCommand`
- 声明: `public class ReachCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.RechargeCommand`
- 声明: `public class RechargeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.ResetSkillCommand`
- 声明: `public class ResetSkillCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.SearchCommand`
- 声明: `public class SearchCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.SetSlotCommand`
- 声明: `public class SetSlotCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.SetStatCommand`
- 声明: `public class SetStatCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.SpCommand`
- 声明: `public class SpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.SummonCommand`
- 声明: `public class SummonCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.UnBugCommand`
- 声明: `public class UnBugCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.UnHideCommand`
- 声明: `public class UnHideCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.UnJailCommand`
- 声明: `public class UnJailCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.WarpAreaCommand`
- 声明: `public class WarpAreaCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.WarpCommand`
- 声明: `public class WarpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.WarpMapCommand`
- 声明: `public class WarpMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm2.WhereaMiCommand`
- 声明: `public class WhereaMiCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm3`

### `org.gms.client.command.commands.gm3.BanCommand`
- 声明: `public class BanCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ChatCommand`
- 声明: `public class ChatCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.CheckDmgCommand`
- 声明: `public class CheckDmgCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ClosePortalCommand`
- 声明: `public class ClosePortalCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.DebuffCommand`
- 声明: `public class DebuffCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.EndEventCommand`
- 声明: `public class EndEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ExpedsCommand`
- 声明: `public class ExpedsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.FaceCommand`
- 声明: `public class FaceCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.FameCommand`
- 声明: `public class FameCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.FlyCommand`
- 声明: `public class FlyCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.GiveMesosCommand`
- 声明: `public class GiveMesosCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.GiveNxCommand`
- 声明: `public class GiveNxCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.GiveRpCommand`
- 声明: `public class GiveRpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm3.GiveVpCommand`
- 声明: `public class GiveVpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.HairCommand`
- 声明: `public class HairCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.HealMapCommand`
- 声明: `public class HealMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.HealPersonCommand`
- 声明: `public class HealPersonCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.HpMpCommand`
- 声明: `public class HpMpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.HurtCommand`
- 声明: `public class HurtCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.IgnoreCommand`
- 声明: `public class IgnoreCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.IgnoredCommand`
- 声明: `public class IgnoredCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.InMapCommand`
- 声明: `public class InMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.KillAllCommand`
- 声明: `public class KillAllCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.KillCommand`
- 声明: `public class KillCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.KillMapCommand`
- 声明: `public class KillMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MaxEnergyCommand`
- 声明: `public class MaxEnergyCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MaxHpMpCommand`
- 声明: `public class MaxHpMpCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MonitorCommand`
- 声明: `public class MonitorCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MonitorsCommand`
- 声明: `public class MonitorsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MusicCommand`
- 声明: `public class MusicCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.MuteMapCommand`
- 声明: `public class MuteMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.NightCommand`
- 声明: `public class NightCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.NoticeCommand`
- 声明: `public class NoticeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.NpcCommand`
- 声明: `public class NpcCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.OnlineTwoCommand`
- 声明: `public class OnlineTwoCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.OpenPortalCommand`
- 声明: `public class OpenPortalCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.PeCommand`
- 声明: `public class PeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.PosCommand`
- 声明: `public class PosCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.QuestCompleteCommand`
- 声明: `public class QuestCompleteCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.QuestResetCommand`
- 声明: `public class QuestResetCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.QuestStartCommand`
- 声明: `public class QuestStartCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ReloadDropsCommand`
- 声明: `public class ReloadDropsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ReloadEventsCommand`
- 声明: `public class ReloadEventsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ReloadMapCommand`
- 声明: `public class ReloadMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ReloadPortalsCommand`
- 声明: `public class ReloadPortalsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ReloadShopsCommand`
- 声明: `public class ReloadShopsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.RipCommand`
- 声明: `public class RipCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.SeedCommand`
- 声明: `public class SeedCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.SpawnCommand`
- 声明: `public class SpawnCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.StartEventCommand`
- 声明: `public class StartEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.StartMapEventCommand`
- 声明: `public class StartMapEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.StopMapEventCommand`
- 声明: `public class StopMapEventCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.TimerAllCommand`
- 声明: `public class TimerAllCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.TimerCommand`
- 声明: `public class TimerCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.TimerMapCommand`
- 声明: `public class TimerMapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.ToggleCouponCommand`
- 声明: `public class ToggleCouponCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm3.UnBanCommand`
- 声明: `public class UnBanCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm4`

### `org.gms.client.command.commands.gm4.BossDropRateCommand`
- 声明: `public class BossDropRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.CakeCommand`
- 声明: `public class CakeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.DropRateCommand`
- 声明: `public class DropRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ExpRateCommand`
- 声明: `public class ExpRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.FishingRateCommand`
- 声明: `public class FishingRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ForceVacCommand`
- 声明: `public class ForceVacCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.HorntailCommand`
- 声明: `public class HorntailCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ItemVacCommand`
- 声明: `public class ItemVacCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.MesoRateCommand`
- 声明: `public class MesoRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PapCommand`
- 声明: `public class PapCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PianusCommand`
- 声明: `public class PianusCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PinkbeanCommand`
- 声明: `public class PinkbeanCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PlayerNpcCommand`
- 声明: `public class PlayerNpcCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PlayerNpcRemoveCommand`
- 声明: `public class PlayerNpcRemoveCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PmobCommand`
- 声明: `public class PmobCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PmobRemoveCommand`
- 声明: `public class PmobRemoveCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PnpcCommand`
- 声明: `public class PnpcCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.PnpcRemoveCommand`
- 声明: `public class PnpcRemoveCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ProItemCommand`
- 声明: `public class ProItemCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.QuestRateCommand`
- 声明: `public class QuestRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ServerMessageCommand`
- 声明: `public class ServerMessageCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.SetEqStatCommand`
- 声明: `public class SetEqStatCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.TravelRateCommand`
- 声明: `public class TravelRateCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.WarpToLifeCommand`
- 声明: `public class WarpToLifeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm4.ZakumCommand`
- 声明: `public class ZakumCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm5`

### `org.gms.client.command.commands.gm5.DebugCommand`
- 声明: `public class DebugCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm5.IpListCommand`
- 声明: `public class IpListCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm5.SetCommand`
- 声明: `public class SetCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm5.ShowMoveLifeCommand`
- 声明: `public class ShowMoveLifeCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm5.ShowPacketsCommand`
- 声明: `public class ShowPacketsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm5.ShowSessionsCommand`
- 声明: `public class ShowSessionsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.command.commands.gm6`

### `org.gms.client.command.commands.gm6.ClearQuestCacheCommand`
- 声明: `public class ClearQuestCacheCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ClearQuestCommand`
- 声明: `public class ClearQuestCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.DCAllCommand`
- 声明: `public class DCAllCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.DevtestCommand`
- 声明: `public class DevtestCommand extends Command {`
- 方法数（启发式提取）: 2

```text
public ScriptEngine getInvocableScriptEngine(String path)
public void execute(Client client, String[] params)
```

### `org.gms.client.command.commands.gm6.EraseAllPNpcsCommand`
- 声明: `public class EraseAllPNpcsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.GetAccCommand`
- 声明: `public class GetAccCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.MapPlayersCommand`
- 声明: `public class MapPlayersCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.SaveAllCommand`
- 声明: `public class SaveAllCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ServerAddChannelCommand`
- 声明: `public class ServerAddChannelCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ServerAddWorldCommand`
- 声明: `public class ServerAddWorldCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ServerRemoveChannelCommand`
- 声明: `public class ServerRemoveChannelCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ServerRemoveWorldCommand`
- 声明: `public class ServerRemoveWorldCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.SetGmLevelCommand`
- 声明: `public class SetGmLevelCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.ShutdownCommand`
- 声明: `public class ShutdownCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.SpawnAllPNpcsCommand`
- 声明: `public class SpawnAllPNpcsCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.SupplyRateCouponCommand`
- 声明: `public class SupplyRateCouponCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

### `org.gms.client.command.commands.gm6.WarpWorldCommand`
- 声明: `public class WarpWorldCommand extends Command {`
- 方法数（启发式提取）: 1

```text
public void execute(Client c, String[] params)
```

## `org.gms.client.creator`

### `org.gms.client.creator.CharacterFactory`
- 声明: `public abstract class CharacterFactory {`
- 方法数（启发式提取）: 0

### `org.gms.client.creator.CharacterFactoryRecipe`
- 声明: `public class CharacterFactoryRecipe {`
- 方法数（启发式提取）: 31

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
public List<Pair<Skill, Integer>> getStartingSkillLevel()
public List<Pair<Item, InventoryType>> getStartingItems()
```

### `org.gms.client.creator.MakeCharInfo`
- 声明: `public class MakeCharInfo {`
- 方法数（启发式提取）: 10

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

### `org.gms.client.creator.MakeCharInfoValidator`
- 声明: `public class MakeCharInfoValidator {`
- 方法数（启发式提取）: 1

```text
public static boolean isNewCharacterValid(Character character)
```

## `org.gms.client.creator.novice`

### `org.gms.client.creator.novice.BeginnerCreator`
- 声明: `public class BeginnerCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

### `org.gms.client.creator.novice.LegendCreator`
- 声明: `public class LegendCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

### `org.gms.client.creator.novice.NoblesseCreator`
- 声明: `public class NoblesseCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int top, int bottom, int shoes, int weapon, int gender)
```

## `org.gms.client.creator.veteran`

### `org.gms.client.creator.veteran.BowmanCreator`
- 声明: `public class BowmanCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

### `org.gms.client.creator.veteran.MagicianCreator`
- 声明: `public class MagicianCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

### `org.gms.client.creator.veteran.PirateCreator`
- 声明: `public class PirateCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

### `org.gms.client.creator.veteran.ThiefCreator`
- 声明: `public class ThiefCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

### `org.gms.client.creator.veteran.WarriorCreator`
- 声明: `public class WarriorCreator extends CharacterFactory {`
- 方法数（启发式提取）: 1

```text
public static int createCharacter(Client c, String name, int face, int hair, int skin, int gender, int improveSp)
```

## `org.gms.client.inventory`

### `org.gms.client.inventory.Equip`
- 声明: `public class Equip extends Item {`
- 方法数（启发式提取）: 57

```text
public int getValue()
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
public Map<StatUpgrade, Short> getStats()
public Pair<String, Pair<Boolean, Boolean>> gainStats(List<Pair<StatUpgrade, Integer>> stats)
public int getItemExp()
public synchronized void gainItemExp(Client c, int gain)
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

### `org.gms.client.inventory.Inventory`
- 声明: `public class Inventory implements Iterable<Item> {`
- 方法数（启发式提取）: 41

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
public void move(short sSlot, short dSlot, short slotMax)
public Item getItem(short slot)
public void removeItem(short slot)
public void removeItem(short slot, short quantity, boolean allowZero)
public void removeSlot(short slot)
public boolean isFull()
public boolean isFull(int margin)
public boolean isFullAfterSomeItems(int margin, int used)
public short getNextFreeSlot()
public short getNumFreeSlot()
public static boolean checkSpot(Character chr, Item item)
public static boolean checkSpot(Character chr, List<Item> items)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, boolean useProofInv)
public static boolean checkSpots(Character chr, List<Pair<Item, InventoryType>> items, List<Integer> typesSlotsUsed, boolean useProofInv)
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

### `org.gms.client.inventory.InventoryProof`
- 声明: `public class InventoryProof extends Inventory {`
- 方法数（启发式提取）: 4

```text
public InventoryProof(Character mc)
public void cloneContents(Inventory inv)
public void flushContents()
public void removeSlot(short slot)
```

### `org.gms.client.inventory.InventoryType`
- 声明: `public enum InventoryType {`
- 方法数（启发式提取）: 5

```text
public short getBitfieldEncoding()
public static InventoryType getByType(byte type)
public static InventoryType getByWZName(String name)
public boolean canChangeSlotMax()
public boolean isEquip()
```

### `org.gms.client.inventory.Item`
- 声明: `public class Item implements Comparable<Item> {`
- 方法数（启发式提取）: 27

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

### `org.gms.client.inventory.ItemFactory`
- 声明: `public enum ItemFactory {`
- 方法数（启发式提取）: 5

```text
public int getValue()
public List<Pair<Item, InventoryType>> loadItems(int id, boolean login) throws SQLException
public void saveItems(List<Pair<Item, InventoryType>> items, int id, Connection con) throws SQLException
public void saveItems(List<Pair<Item, InventoryType>> items, List<Short> bundlesList, int id, Connection con) throws SQLException
public static List<Pair<Item, Integer>> loadEquippedItems(int id, boolean isAccount, boolean login) throws SQLException
```

### `org.gms.client.inventory.ModifyInventory`
- 声明: `public class ModifyInventory {`
- 方法数（启发式提取）: 9

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

### `org.gms.client.inventory.Pet`
- 声明: `public class Pet extends Item {`
- 方法数（启发式提取）: 31

```text
public int getValue()
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
public void addPetAttribute(Character owner, PetAttribute flag)
public void removePetAttribute(Character owner, PetAttribute flag)
public Pair<Integer, Boolean> canConsume(int itemId)
public void updatePosition(List<LifeMovementFragment> movement)
```

### `org.gms.client.inventory.PetCommand`
- 声明: `public class PetCommand {`
- 方法数（启发式提取）: 5

```text
public PetCommand(int petId, int skillId, int prob, int inc)
public int getPetId()
public int getSkillId()
public int getProbability()
public int getIncrease()
```

### `org.gms.client.inventory.PetDataFactory`
- 声明: `public class PetDataFactory {`
- 方法数（启发式提取）: 2

```text
public static PetCommand getPetCommand(int petId, int skillId)
public static int getHunger(int petId)
```

### `org.gms.client.inventory.WeaponType`
- 声明: `public enum WeaponType {`
- 方法数（启发式提取）: 1

```text
public double getMaxDamageMultiplier()
```

## `org.gms.client.inventory.manipulator`

### `org.gms.client.inventory.manipulator.InventoryManipulator`
- 声明: `public class InventoryManipulator {`
- 方法数（启发式提取）: 18

```text
public static boolean addById(Client c, int itemId, short quantity)
public static boolean addById(Client c, int itemId, short quantity, long expiration)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, long expiration)
public static boolean addById(Client c, int itemId, short quantity, String owner, int petid, short flag, long expiration)
public static boolean addFromDrop(Client c, Item item)
public static boolean addFromDrop(Client c, Item item, boolean show)
public static boolean addFromDrop(Client c, Item item, boolean show, int petId)
public static boolean checkSpace(Client c, int itemid, int quantity, String owner)
public static int checkSpaceProgressively(Client c, int itemid, int quantity, String owner, int usedSlots, boolean useProofInv)
public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop)
public static void removeFromSlot(Client c, InventoryType type, short slot, short quantity, boolean fromDrop, boolean consume)
public static void removeById(Client c, InventoryType type, int itemId, int quantity, boolean fromDrop, boolean consume)
public static void move(Client c, InventoryType type, short src, short dst)
public static void equip(Client c, short src, short dst)
public static void unequip(Client c, short src, short dst)
public static void drop(Client c, InventoryType type, short src, short quantity)
public static boolean isSandboxItem(Item it)
```

### `org.gms.client.inventory.manipulator.KarmaManipulator`
- 声明: `public class KarmaManipulator {`
- 方法数（启发式提取）: 3

```text
public static boolean hasKarmaFlag(Item item)
public static void toggleKarmaFlagToUntradeable(Item item)
public static void setKarmaFlag(Item item)
```

## `org.gms.client.keybind`

### `org.gms.client.keybind.KeyBinding`
- 声明: `public class KeyBinding {`
- 方法数（启发式提取）: 3

```text
public KeyBinding(int type, int action)
public int getType()
public int getAction()
```

### `org.gms.client.keybind.QuickslotBinding`
- 声明: `public class QuickslotBinding {`
- 方法数（启发式提取）: 3

```text
public QuickslotBinding(byte[] aKeys)
public void encode(OutPacket p)
public byte[] GetKeybindings()
```

## `org.gms.client.processor.action`

### `org.gms.client.processor.action.MakerProcessor`
- 声明: `public class MakerProcessor {`
- 方法数（启发式提取）: 2

```text
public static void makerAction(InPacket p, Client c)
public static int getMakerSkillLevel(Character chr)
```

### `org.gms.client.processor.action.PetAutopotProcessor`
- 声明: `public class PetAutopotProcessor {`
- 方法数（启发式提取）: 3

```text
public AutopotAction(Client c, short slot, int itemId)
public void run()
public static void runAutopotAction(Client c, short slot, int itemid)
```

### `org.gms.client.processor.action.SpawnPetProcessor`
- 声明: `public class SpawnPetProcessor {`
- 方法数（启发式提取）: 1

```text
public static void processSpawnPet(Client c, byte slot, boolean lead)
```

## `org.gms.client.processor.npc`

### `org.gms.client.processor.npc.DueyProcessor`
- 声明: `public class DueyProcessor {`
- 方法数（启发式提取）: 7

```text
public byte getCode()
public static void dueySendItem(Client c, byte invTypeId, short itemPos, short amount, int sendMesos, String sendMessage, String recipient, boolean quick)
public static void dueyRemovePackage(Client c, int packageid, boolean playerRemove)
public static synchronized void dueyClaimPackage(Client c, int packageId)
public static void dueySendTalk(Client c, boolean quickDelivery)
public static void dueyCreatePackage(Item item, int mesos, String sender, int recipientCid)
public static void runDueyExpireSchedule()
```

### `org.gms.client.processor.npc.FredrickProcessor`
- 声明: `public class FredrickProcessor {`
- 方法数（启发式提取）: 6

```text
public FredrickProcessor(NoteService noteService)
public static int timestampElapsedDays(Timestamp then, long timeNow)
public static void removeFredrickLog(int cid)
public static void insertFredrickLog(int cid)
public void runFredrickSchedule()
public void fredrickRetrieveItems(Client c)
```

### `org.gms.client.processor.npc.StorageProcessor`
- 声明: `public class StorageProcessor {`
- 方法数（启发式提取）: 1

```text
public static void storageAction(InPacket p, Client c)
```

## `org.gms.client.processor.stat`

### `org.gms.client.processor.stat.AssignAPProcessor`
- 声明: `public class AssignAPProcessor {`
- 方法数（启发式提取）: 4

```text
public static void reloadConfig()
public static void APAutoAssignAction(InPacket inPacket, Client c)
public static boolean APResetAction(Client c, int APFrom, int APTo)
public static void APAssignAction(Client c, int num)
```

### `org.gms.client.processor.stat.AssignSPProcessor`
- 声明: `public class AssignSPProcessor {`
- 方法数（启发式提取）: 2

```text
public static boolean canSPAssign(Client c, int skillid)
public static void SPAssignAction(Client c, int skillid)
```

## `org.gms.client.status`

### `org.gms.client.status.MonsterStatus`
- 声明: `public enum MonsterStatus {`
- 方法数（启发式提取）: 2

```text
public boolean isFirst()
public int getValue()
```

### `org.gms.client.status.MonsterStatusEffect`
- 声明: `public class MonsterStatusEffect {`
- 方法数（启发式提取）: 7

```text
public MonsterStatusEffect(Map<MonsterStatus, Integer> stati, Skill skillId, MobSkill mobskill, boolean monsterSkill)
public Map<MonsterStatus, Integer> getStati()
public Integer setValue(MonsterStatus status, Integer newVal)
public Skill getSkill()
public boolean isMonsterSkill()
public void removeActiveStatus(MonsterStatus stat)
public MobSkill getMobSkill()
```

## `org.gms.config`

### `org.gms.config.CorsConfig`
- 声明: `public class CorsConfig implements WebMvcConfigurer {`
- 方法数（启发式提取）: 1

```text
public void addCorsMappings(CorsRegistry registry)
```

### `org.gms.config.GameConfig`
- 声明: `public class GameConfig {`
- 方法数（启发式提取）: 54

```text
public static void add(GameConfigDO gameConfigDO)
public static void remove(GameConfigDO gameConfigDO)
public static void update(GameConfigDO gameConfigDO)
public static Object getObject(String key)
public static <T> T get(String key)
public static <T> T get(String key, T defaultValue)
public static <T> T get(String type, String key)
public static <T> T get(String type, String key, T defaultVal)
public static <T> T get(String type, String subType, String key)
public static <T> T get(String type, String subType, String key, T defaultVal)
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
public static <T> T getWorldObject(int worldId, String key, TypeReference<T> type)
public static <T> T getServerObject(String key, TypeReference<T> type)
public static JSONObject getConfig()
```

### `org.gms.config.I18nConfig`
- 声明: `public class I18nConfig {`
- 方法数（启发式提取）: 3

```text
public MessageSource messageSource()
public MessageSource logSource()
public MessageSource exceptionSource()
```

### `org.gms.config.ServerConfig`
- 声明: `public class ServerConfig {`
- 方法数（启发式提取）: 2

```text
public FilterRegistrationBean<ServerFilter> filterRegistrationBean(ServerFilter serverFilter)
public OpenAPI openAPI()
```

### `org.gms.config.SpringSecurityConfig`
- 声明: `public class SpringSecurityConfig {`
- 方法数（启发式提取）: 6

```text
public SpringSecurityConfig(UserDetailsServiceImpl userDetailsService, AuthEntryPointJwt unauthorizedHandler)
public AuthTokenFilter authenticationJwtTokenFilter()
public DaoAuthenticationProvider authenticationProvider()
public AuthenticationManager authenticationManager(AuthenticationConfiguration authConfig) throws Exception
public PasswordEncoder passwordEncoder()
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception
```

## `org.gms.constants.api`

### `org.gms.constants.api.ApiConstant`
- 声明: `public class ApiConstant {`
- 方法数（启发式提取）: 0

### `org.gms.constants.api.InformationType`
- 声明: `public enum InformationType {`
- 方法数（启发式提取）: 1

```text
public static InformationType ofType(final String type)
```

## `org.gms.constants.game`

### `org.gms.constants.game.CommodityFlag`
- 声明: `public enum CommodityFlag {`
- 方法数（启发式提取）: 1

```text
public static List<CommodityFlag> getAvailableSortedValues()
```

### `org.gms.constants.game.DelayedQuestUpdate`
- 声明: `public enum DelayedQuestUpdate {`
- 方法数（启发式提取）: 0

### `org.gms.constants.game.ExpTable`
- 声明: `public final class ExpTable {`
- 方法数（启发式提取）: 5

```text
public static int getExpNeededForLevel(int level)
public static int getTamenessNeededForLevel(int level)
public static int getMountExpNeededForLevel(int level)
public static int getEquipExpNeededForLevel(int level)
public static int getMountMaxLevel()
```

### `org.gms.constants.game.GameConstants`
- 声明: `public class GameConstants {`
- 方法数（启发式提取）: 45

```text
public static final int MAX_FIELD_MOB_DAMAGE = getMaxObstacleMobDamageFromWz() * 2
public static int getPlayerBonusDropRate(int slot)
public static int getPlayerBonusMesoRate(int slot)
public static int getPlayerBonusExpRate(int slot)
public static final Map<String, Integer> GOTO_TOWNS = new HashMap<>()
public static final Map<String, Integer> GOTO_AREAS = new HashMap<>()
public static final List<String> GAME_SONGS = new ArrayList<>(170)
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
public static Pair<byte[], byte[]> getEnc()
public static int selectRandomReward(int[] rewards)
```

### `org.gms.constants.game.NextLevelType`
- 声明: `public enum NextLevelType {`
- 方法数（启发式提取）: 0

### `org.gms.constants.game.NpcChat`
- 声明: `public final class NpcChat {`
- 方法数（启发式提取）: 0

## `org.gms.constants.id`

### `org.gms.constants.id.ItemId`
- 声明: `public class ItemId {`
- 方法数（启发式提取）: 20

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

### `org.gms.constants.id.MapId`
- 声明: `public class MapId {`
- 方法数（启发式提取）: 11

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

### `org.gms.constants.id.MobId`
- 声明: `public class MobId {`
- 方法数（启发式提取）: 3

```text
public static boolean isZakumArm(int mobId)
public static boolean isDeadHorntailPart(int mobId)
public static boolean isDojoBoss(int mobId)
```

### `org.gms.constants.id.NpcId`
- 声明: `public class NpcId {`
- 方法数（启发式提取）: 0

## `org.gms.constants.inventory`

### `org.gms.constants.inventory.EquipSlot`
- 声明: `public enum EquipSlot {`
- 方法数（启发式提取）: 3

```text
public String getName()
public boolean isAllowed(int slot, boolean cash)
public static EquipSlot getFromTextSlot(String slot)
```

### `org.gms.constants.inventory.EquipType`
- 声明: `public enum EquipType {`
- 方法数（启发式提取）: 2

```text
public int getValue()
public static EquipType getEquipTypeById(int itemid)
```

### `org.gms.constants.inventory.ItemConstants`
- 声明: `public final class ItemConstants {`
- 方法数（启发式提取）: 49

```text
public final static Set<Integer> permanentItemids = new HashSet<>()
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

## `org.gms.constants.net`

### `org.gms.constants.net.OpcodeConstants`
- 声明: `public class OpcodeConstants {`
- 方法数（启发式提取）: 4

```text
public static Map<Integer, String> sendOpcodeNames = new HashMap<>()
public static Map<Integer, String> recvOpcodeNames = new HashMap<>()
public static void generateOpcodeNames()
public static void init(Opcode[] sendValues, Opcode[] recvValues)
```

### `org.gms.constants.net.ServerConstants`
- 声明: `public class ServerConstants {`
- 方法数（启发式提取）: 0

## `org.gms.constants.skills`

### `org.gms.constants.skills.Aran`
- 声明: `public class Aran {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Archer`
- 声明: `public class Archer {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Assassin`
- 声明: `public class Assassin {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Bandit`
- 声明: `public class Bandit {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Beginner`
- 声明: `public class Beginner {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Bishop`
- 声明: `public class Bishop {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.BlazeWizard`
- 声明: `public class BlazeWizard {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Bowmaster`
- 声明: `public class Bowmaster {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Brawler`
- 声明: `public class Brawler {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Buccaneer`
- 声明: `public class Buccaneer {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.ChiefBandit`
- 声明: `public class ChiefBandit {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Cleric`
- 声明: `public class Cleric {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Corsair`
- 声明: `public class Corsair {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Crossbowman`
- 声明: `public class Crossbowman {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Crusader`
- 声明: `public class Crusader {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.DarkKnight`
- 声明: `public class DarkKnight {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.DawnWarrior`
- 声明: `public class DawnWarrior {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.DragonKnight`
- 声明: `public class DragonKnight {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Evan`
- 声明: `public class Evan {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.FPArchMage`
- 声明: `public class FPArchMage {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.FPMage`
- 声明: `public class FPMage {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.FPWizard`
- 声明: `public class FPWizard {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Fighter`
- 声明: `public class Fighter {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.GM`
- 声明: `public class GM {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Gunslinger`
- 声明: `public class Gunslinger {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Hermit`
- 声明: `public class Hermit {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Hero`
- 声明: `public class Hero {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Hunter`
- 声明: `public class Hunter {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.ILArchMage`
- 声明: `public class ILArchMage {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.ILMage`
- 声明: `public class ILMage {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.ILWizard`
- 声明: `public class ILWizard {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Legend`
- 声明: `public class Legend {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Magician`
- 声明: `public class Magician {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Marauder`
- 声明: `public class Marauder {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Marksman`
- 声明: `public class Marksman {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.NightLord`
- 声明: `public class NightLord {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.NightWalker`
- 声明: `public class NightWalker {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Noblesse`
- 声明: `public class Noblesse {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Outlaw`
- 声明: `public class Outlaw {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Page`
- 声明: `public class Page {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Paladin`
- 声明: `public class Paladin {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Pirate`
- 声明: `public class Pirate {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Priest`
- 声明: `public class Priest {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Ranger`
- 声明: `public class Ranger {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Rogue`
- 声明: `public class Rogue {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Shadower`
- 声明: `public class Shadower {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Sniper`
- 声明: `public class Sniper {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Spearman`
- 声明: `public class Spearman {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.SuperGM`
- 声明: `public class SuperGM {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.ThunderBreaker`
- 声明: `public class ThunderBreaker {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.Warrior`
- 声明: `public class Warrior {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.WhiteKnight`
- 声明: `public class WhiteKnight {`
- 方法数（启发式提取）: 0

### `org.gms.constants.skills.WindArcher`
- 声明: `public class WindArcher {`
- 方法数（启发式提取）: 0

## `org.gms.constants.string`

### `org.gms.constants.string.CategoryType`
- 声明: `public enum CategoryType {`
- 方法数（启发式提取）: 2

```text
public static CategoryType ofId(int id)
public static String toName(int id)
```

### `org.gms.constants.string.CharsetConstants`
- 声明: `public class CharsetConstants {`
- 方法数（启发式提取）: 4

```text
public static Charset getCharset(int language)
public static Locale getLanguageLocale(int language)
public static boolean isZhCN()
public static Language fromLang(int lang)
```

### `org.gms.constants.string.ExtendType`
- 声明: `public enum ExtendType {`
- 方法数（启发式提取）: 4

```text
public static ExtendType getExtendType(String type)
public static Map<String, Date> getCleanMap()
public static boolean isAccount(String type)
public static boolean isCharacter(String type)
```

### `org.gms.constants.string.LanguageConstants`
- 声明: `public class LanguageConstants {`
- 方法数（启发式提取）: 1

```text
public static String getMessage(Character chr, String[] message)
```

## `org.gms.controller`

### `org.gms.controller.AccountController`
- 声明: `public class AccountController {`
- 方法数（启发式提取）: 10

```text
public AccountController(AccountService accountService)
public ResultBody<AccountsDO> info()
public ResultBody<Page<AccountsDO>> getAccountList(@RequestParam(name = "page", required = false) Integer page, @RequestParam(name = "size", required = false) Integer size, @RequestParam(name = "id", required = false) Integer id, @RequestParam(name = "name", required = false) String name, @RequestParam(name = "lastLoginStart", required = false) String lastLoginStart, @RequestParam(name = "lastL...
public ResultBody<Object> register(@RequestBody SubmitBody<AddAccountDTO> submitBody) throws NoSuchAlgorithmException
public ResultBody<Object> updateByUser(@RequestBody SubmitBody<UpdateAccountByUserDTO> submitBody) throws NoSuchAlgorithmException
public ResultBody<Object> updateByGm(@PathVariable("id") int id, @RequestBody SubmitBody<UpdateAccountByGmDTO> submitBody) throws NoSuchAlgorithmException
public ResultBody<Object> delete(@PathVariable("id") int id)
public ResultBody<Object> resetLoggedIn(@PathVariable("id") int id)
public ResultBody<Object> banAccount(@PathVariable("id") int id, @RequestBody SubmitBody<Map<String, String>> submitBody)
public ResultBody<Object> unbanAccount(@PathVariable("id") int id)
```

### `org.gms.controller.AuthController`
- 声明: `public class AuthController {`
- 方法数（启发式提取）: 4

```text
public AuthController(AuthService authService)
public ResultBody<Map<String, String>> login(@RequestBody SubmitBody<Map<String, String>> data)
public ResultBody<Object> logout()
public ResultBody<Map<String, String>> refreshToken(@RequestHeader("Authorization") String token)
```

### `org.gms.controller.AutobanConfigController`
- 声明: `public class AutobanConfigController {`
- 方法数（启发式提取）: 2

```text
public ResultBody<List<AutobanConfigDTO>> getConfigList()
public ResultBody<Object> updateConfig(@RequestBody SubmitBody<AutobanConfigDTO> request)
```

### `org.gms.controller.CashShopController`
- 声明: `public class CashShopController {`
- 方法数（启发式提取）: 6

```text
public ResultBody<List<CashCategory>> getAllCategoryList()
public ResultBody<Page<CashShopSearchRtnDTO>> getCommodityByCategory(@RequestBody SubmitBody<CashCategory> request)
public ResultBody<CashShopSearchRtnDTO> getCommodityBySn(@PathVariable("sn") Integer sn)
public ResultBody<Object> onSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)
public ResultBody<Object> offSale(@RequestBody SubmitBody<ModifiedCashItemDO> request)
public ResultBody<Object> batchOnSale(@RequestBody SubmitBody<CashShopBatchOnSaleReqDTO> request)
```

### `org.gms.controller.CharacterController`
- 声明: `public class CharacterController {`
- 方法数（启发式提取）: 4

```text
public ResultBody<Object> updateRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Object> resetRate(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Object> resetRates(@RequestBody SubmitBody<ExtendValueDO> submitBody)
public ResultBody<Page<ChrOnlineListRtnDTO>> onlineList(@RequestBody SubmitBody<ChrOnlineListReqDTO> submitBody)
```

### `org.gms.controller.CommandController`
- 声明: `public class CommandController {`
- 方法数（启发式提取）: 5

```text
public ResultBody<Page<CommandReqDTO>> getCommandListFromDB(@RequestBody SubmitBody<CommandReqDTO> submitBody)
public ResultBody<CommandInfoDO> updateCommand(@RequestBody SubmitBody<CommandReqDTO> submitBody)
public ResultBody reloadEventsByGMCommand()
public ResultBody reloadPortalsByGMCommand()
public ResultBody reloadMapsByGMCommand()
```

### `org.gms.controller.CommonController`
- 声明: `public class CommonController {`
- 方法数（启发式提取）: 3

```text
public ResultBody<Object> getEquipmentInfoByItemId(@RequestBody SubmitBody<EquipmentInfoReqDTO> submitBody)
public ResultBody<Integer> getAllWorldsOnlinePlayersCount(@RequestBody SubmitBody<ServerInfoReqDto> submitBody)
public ResultBody<List<InformationResult>> informationSearch(@RequestBody SubmitBody<InformationSearch> submitBody)
```

### `org.gms.controller.ConfigController`
- 声明: `public class ConfigController {`
- 方法数（启发式提取）: 8

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

### `org.gms.controller.DropController`
- 声明: `public class DropController {`
- 方法数（启发式提取）: 8

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

### `org.gms.controller.FileController`
- 声明: `public class FileController {`
- 方法数（启发式提取）: 3

```text
public ResultBody<String> treeRead(@RequestBody SubmitBody<FileReadDTO> request)
public ResultBody<String> treeWrite(@RequestBody SubmitBody<FileWriteDTO> request)
public ResultBody<List<FileTreeNodeDTO>> tree(@RequestBody SubmitBody<FileTreeDTO> request)
```

### `org.gms.controller.GachaponController`
- 声明: `public class GachaponController {`
- 方法数（启发式提取）: 6

```text
public ResultBody<Page<GachaponPoolSearchRtnDTO>> getPools(@RequestBody SubmitBody<GachaponPoolSearchReqDTO> request)
public ResultBody<Object> updatePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<Object> deletePool(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<List<GachaponRewardDO>> getRewards(@RequestBody SubmitBody<GachaponRewardPoolDO> request)
public ResultBody<Object> updateReward(@RequestBody SubmitBody<GachaponRewardDO> request)
public ResultBody<Object> deleteReward(@RequestBody SubmitBody<GachaponRewardDO> request)
```

### `org.gms.controller.GiveController`
- 声明: `public class GiveController {`
- 方法数（启发式提取）: 1

```text
public ResultBody<Object> giveResource(@RequestBody SubmitBody<GiveResourceReqDTO> submitBody)
```

### `org.gms.controller.InventoryController`
- 声明: `public class InventoryController {`
- 方法数（启发式提取）: 5

```text
public ResultBody<List<InventoryTypeRtnDTO>> getInventoryTypeList()
public ResultBody<Page<InventorySearchReqDTO>> getCharacterList(@RequestBody SubmitBody<InventorySearchReqDTO> request)
public ResultBody<List<InventorySearchRtnDTO>> getInventoryList(@RequestBody SubmitBody<InventorySearchReqDTO> request)
public ResultBody<Object> updateInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)
public ResultBody<Object> deleteInventory(@RequestBody SubmitBody<InventorySearchRtnDTO> request)
```

### `org.gms.controller.ServerController`
- 声明: `public class ServerController {`
- 方法数（启发式提取）: 9

```text
public void shutdown()
public ResultBody<Object> stopServer()
public ResultBody<Object> stopServerWithMsgAndInternal( @Parameter( name = "stopConfigData", in = ParameterIn.DEFAULT, required = true, description = "停服请求参数：包含停服自定义消息，停服倒计时(单位：分钟)" ) @RequestBody SubmitBody<ServerShutdownDTO> request)
public ResultBody<Object> startServer()
public ResultBody<Object> restartServer()
public ResultBody<Boolean> online()
public ResultBody<Object> worldList()
public ResultBody<List<ChannelListRtnDTO>> channelList(@RequestParam int worldId)
public ResultBody<String> version()
```

### `org.gms.controller.ShopController`
- 声明: `public class ShopController {`
- 方法数（启发式提取）: 6

```text
public ResultBody<Page<ShopSearchRtnDTO>> getShopList(@RequestBody SubmitBody<ShopSearchReqDTO> request)
public ResultBody<Page<ShopItemSearchRtnDTO>> getShopItemList(@RequestBody SubmitBody<ShopSearchReqDTO> request)
public ResultBody<ShopItemSearchRtnDTO> getShopItem(@PathVariable("id") Long id)
public ResultBody<Long> addShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)
public ResultBody<Object> updateShopItem(@RequestBody SubmitBody<ShopItemSearchRtnDTO> request)
public ResultBody<Object> deleteShopItem(@PathVariable("id") Long id)
```

## `org.gms.dao.entity`

### `org.gms.dao.entity.AccountsDO`
- 声明: `public class AccountsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.AllianceDO`
- 声明: `public class AllianceDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.AllianceguildsDO`
- 声明: `public class AllianceguildsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.AreaInfoDO`
- 声明: `public class AreaInfoDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.AutobanConfigDO`
- 声明: `public class AutobanConfigDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.BbsRepliesDO`
- 声明: `public class BbsRepliesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.BbsThreadsDO`
- 声明: `public class BbsThreadsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.BosslogDailyDO`
- 声明: `public class BosslogDailyDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.BosslogWeeklyDO`
- 声明: `public class BosslogWeeklyDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.BuddiesDO`
- 声明: `public class BuddiesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.CharactersDO`
- 声明: `public class CharactersDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.CommandInfoDO`
- 声明: `public class CommandInfoDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.CooldownsDO`
- 声明: `public class CooldownsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.DropDataDO`
- 声明: `public class DropDataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.DropDataGlobalDO`
- 声明: `public class DropDataGlobalDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.DueyitemsDO`
- 声明: `public class DueyitemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.DueypackagesDO`
- 声明: `public class DueypackagesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.EventstatsDO`
- 声明: `public class EventstatsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ExtendValueDO`
- 声明: `public class ExtendValueDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.FamelogDO`
- 声明: `public class FamelogDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.FamilyCharacterDO`
- 声明: `public class FamilyCharacterDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.FamilyEntitlementDO`
- 声明: `public class FamilyEntitlementDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.FlywaySchemaHistoryDO`
- 声明: `public class FlywaySchemaHistoryDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.FredstorageDO`
- 声明: `public class FredstorageDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.GachaponRewardDO`
- 声明: `public class GachaponRewardDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.GachaponRewardPoolDO`
- 声明: `public class GachaponRewardPoolDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.GameConfigDO`
- 声明: `public class GameConfigDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.GiftsDO`
- 声明: `public class GiftsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.GuildsDO`
- 声明: `public class GuildsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.HpMpAlertDO`
- 声明: `public class HpMpAlertDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.HwidaccountsDO`
- 声明: `public class HwidaccountsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.HwidbansDO`
- 声明: `public class HwidbansDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.InventoryequipmentDO`
- 声明: `public class InventoryequipmentDO implements Serializable  {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.InventoryitemsDO`
- 声明: `public class InventoryitemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.InventorymerchantDO`
- 声明: `public class InventorymerchantDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.IpbansDO`
- 声明: `public class IpbansDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.KeymapDO`
- 声明: `public class KeymapDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.LangResourcesDO`
- 声明: `public class LangResourcesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MacbansDO`
- 声明: `public class MacbansDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MacfiltersDO`
- 声明: `public class MacfiltersDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MakercreatedataDO`
- 声明: `public class MakercreatedataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MakerreagentdataDO`
- 声明: `public class MakerreagentdataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MakerrecipedataDO`
- 声明: `public class MakerrecipedataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MakerrewarddataDO`
- 声明: `public class MakerrewarddataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MarriagesDO`
- 声明: `public class MarriagesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MedalmapsDO`
- 声明: `public class MedalmapsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ModifiedCashItemDO`
- 声明: `public class ModifiedCashItemDO implements Serializable, Cloneable {`
- 方法数（启发式提取）: 3

```text
public boolean isSelling()
public Item toItem()
public ModifiedCashItemDO clone()
```

### `org.gms.dao.entity.MonsterbookDO`
- 声明: `public class MonsterbookDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MonstercarddataDO`
- 声明: `public class MonstercarddataDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MtsCartDO`
- 声明: `public class MtsCartDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.MtsItemsDO`
- 声明: `public class MtsItemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NamechangesDO`
- 声明: `public class NamechangesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NewyearDO`
- 声明: `public class NewyearDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NotesDO`
- 声明: `public class NotesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NxcodeDO`
- 声明: `public class NxcodeDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NxcodeItemsDO`
- 声明: `public class NxcodeItemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.NxcouponsDO`
- 声明: `public class NxcouponsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PetignoresDO`
- 声明: `public class PetignoresDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PetsDO`
- 声明: `public class PetsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PlayerdiseasesDO`
- 声明: `public class PlayerdiseasesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PlayernpcsDO`
- 声明: `public class PlayernpcsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PlayernpcsEquipDO`
- 声明: `public class PlayernpcsEquipDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PlayernpcsFieldDO`
- 声明: `public class PlayernpcsFieldDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.PlifeDO`
- 声明: `public class PlifeDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.QuestactionsDO`
- 声明: `public class QuestactionsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.QuestprogressDO`
- 声明: `public class QuestprogressDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.QuestrequirementsDO`
- 声明: `public class QuestrequirementsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.QueststatusDO`
- 声明: `public class QueststatusDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.QuickslotkeymappedDO`
- 声明: `public class QuickslotkeymappedDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ReactordropsDO`
- 声明: `public class ReactordropsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ReportsDO`
- 声明: `public class ReportsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ResponsesDO`
- 声明: `public class ResponsesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.RingsDO`
- 声明: `public class RingsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.SavedlocationsDO`
- 声明: `public class SavedlocationsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ServerQueueDO`
- 声明: `public class ServerQueueDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ShopitemsDO`
- 声明: `public class ShopitemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.ShopsDO`
- 声明: `public class ShopsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.SkillmacrosDO`
- 声明: `public class SkillmacrosDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.SkillsDO`
- 声明: `public class SkillsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.SpecialcashitemsDO`
- 声明: `public class SpecialcashitemsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.StoragesDO`
- 声明: `public class StoragesDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.TrocklocationsDO`
- 声明: `public class TrocklocationsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.WishlistsDO`
- 声明: `public class WishlistsDO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.dao.entity.WorldtransfersDO`
- 声明: `public class WorldtransfersDO implements Serializable {`
- 方法数（启发式提取）: 0

## `org.gms.dao.mapper`

### `org.gms.dao.mapper.AccountsMapper`
- 声明: `public interface AccountsMapper extends BaseMapper<AccountsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.AllianceMapper`
- 声明: `public interface AllianceMapper extends BaseMapper<AllianceDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.AllianceguildsMapper`
- 声明: `public interface AllianceguildsMapper extends BaseMapper<AllianceguildsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.AreaInfoMapper`
- 声明: `public interface AreaInfoMapper extends BaseMapper<AreaInfoDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.AutobanConfigMapper`
- 声明: `public interface AutobanConfigMapper extends BaseMapper<AutobanConfigDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.BbsRepliesMapper`
- 声明: `public interface BbsRepliesMapper extends BaseMapper<BbsRepliesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.BbsThreadsMapper`
- 声明: `public interface BbsThreadsMapper extends BaseMapper<BbsThreadsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.BosslogDailyMapper`
- 声明: `public interface BosslogDailyMapper extends BaseMapper<BosslogDailyDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.BosslogWeeklyMapper`
- 声明: `public interface BosslogWeeklyMapper extends BaseMapper<BosslogWeeklyDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.BuddiesMapper`
- 声明: `public interface BuddiesMapper extends BaseMapper<BuddiesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.CharactersMapper`
- 声明: `public interface CharactersMapper extends BaseMapper<CharactersDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.CommandInfoMapper`
- 声明: `public interface CommandInfoMapper extends BaseMapper<CommandInfoDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.CooldownsMapper`
- 声明: `public interface CooldownsMapper extends BaseMapper<CooldownsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.DropDataGlobalMapper`
- 声明: `public interface DropDataGlobalMapper extends BaseMapper<DropDataGlobalDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.DropDataMapper`
- 声明: `public interface DropDataMapper extends BaseMapper<DropDataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.DueyitemsMapper`
- 声明: `public interface DueyitemsMapper extends BaseMapper<DueyitemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.DueypackagesMapper`
- 声明: `public interface DueypackagesMapper extends BaseMapper<DueypackagesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.EventstatsMapper`
- 声明: `public interface EventstatsMapper extends BaseMapper<EventstatsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ExtendValueMapper`
- 声明: `public interface ExtendValueMapper extends BaseMapper<ExtendValueDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.FamelogMapper`
- 声明: `public interface FamelogMapper extends BaseMapper<FamelogDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.FamilyCharacterMapper`
- 声明: `public interface FamilyCharacterMapper extends BaseMapper<FamilyCharacterDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.FamilyEntitlementMapper`
- 声明: `public interface FamilyEntitlementMapper extends BaseMapper<FamilyEntitlementDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.FlywaySchemaHistoryMapper`
- 声明: `public interface FlywaySchemaHistoryMapper extends BaseMapper<FlywaySchemaHistoryDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.FredstorageMapper`
- 声明: `public interface FredstorageMapper extends BaseMapper<FredstorageDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.GachaponRewardMapper`
- 声明: `public interface GachaponRewardMapper extends BaseMapper<GachaponRewardDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.GachaponRewardPoolMapper`
- 声明: `public interface GachaponRewardPoolMapper extends BaseMapper<GachaponRewardPoolDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.GameConfigMapper`
- 声明: `public interface GameConfigMapper extends BaseMapper<GameConfigDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.GiftsMapper`
- 声明: `public interface GiftsMapper extends BaseMapper<GiftsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.GuildsMapper`
- 声明: `public interface GuildsMapper extends BaseMapper<GuildsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.HpMpAlertMapper`
- 声明: `public interface HpMpAlertMapper extends BaseMapper<HpMpAlertDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.HwidaccountsMapper`
- 声明: `public interface HwidaccountsMapper extends BaseMapper<HwidaccountsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.HwidbansMapper`
- 声明: `public interface HwidbansMapper extends BaseMapper<HwidbansDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.InventoryequipmentMapper`
- 声明: `public interface InventoryequipmentMapper extends BaseMapper<InventoryequipmentDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.InventoryitemsMapper`
- 声明: `public interface InventoryitemsMapper extends BaseMapper<InventoryitemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.InventorymerchantMapper`
- 声明: `public interface InventorymerchantMapper extends BaseMapper<InventorymerchantDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.IpbansMapper`
- 声明: `public interface IpbansMapper extends BaseMapper<IpbansDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.KeymapMapper`
- 声明: `public interface KeymapMapper extends BaseMapper<KeymapDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.LangResourcesMapper`
- 声明: `public interface LangResourcesMapper extends BaseMapper<LangResourcesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MacbansMapper`
- 声明: `public interface MacbansMapper extends BaseMapper<MacbansDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MacfiltersMapper`
- 声明: `public interface MacfiltersMapper extends BaseMapper<MacfiltersDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MakercreatedataMapper`
- 声明: `public interface MakercreatedataMapper extends BaseMapper<MakercreatedataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MakerreagentdataMapper`
- 声明: `public interface MakerreagentdataMapper extends BaseMapper<MakerreagentdataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MakerrecipedataMapper`
- 声明: `public interface MakerrecipedataMapper extends BaseMapper<MakerrecipedataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MakerrewarddataMapper`
- 声明: `public interface MakerrewarddataMapper extends BaseMapper<MakerrewarddataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MarriagesMapper`
- 声明: `public interface MarriagesMapper extends BaseMapper<MarriagesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MedalmapsMapper`
- 声明: `public interface MedalmapsMapper extends BaseMapper<MedalmapsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ModifiedCashItemMapper`
- 声明: `public interface ModifiedCashItemMapper extends BaseMapper<ModifiedCashItemDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MonsterbookMapper`
- 声明: `public interface MonsterbookMapper extends BaseMapper<MonsterbookDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MonstercarddataMapper`
- 声明: `public interface MonstercarddataMapper extends BaseMapper<MonstercarddataDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MtsCartMapper`
- 声明: `public interface MtsCartMapper extends BaseMapper<MtsCartDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.MtsItemsMapper`
- 声明: `public interface MtsItemsMapper extends BaseMapper<MtsItemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NamechangesMapper`
- 声明: `public interface NamechangesMapper extends BaseMapper<NamechangesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NewyearMapper`
- 声明: `public interface NewyearMapper extends BaseMapper<NewyearDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NotesMapper`
- 声明: `public interface NotesMapper extends BaseMapper<NotesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NxcodeItemsMapper`
- 声明: `public interface NxcodeItemsMapper extends BaseMapper<NxcodeItemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NxcodeMapper`
- 声明: `public interface NxcodeMapper extends BaseMapper<NxcodeDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.NxcouponsMapper`
- 声明: `public interface NxcouponsMapper extends BaseMapper<NxcouponsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PetignoresMapper`
- 声明: `public interface PetignoresMapper extends BaseMapper<PetignoresDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PetsMapper`
- 声明: `public interface PetsMapper extends BaseMapper<PetsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PlayerdiseasesMapper`
- 声明: `public interface PlayerdiseasesMapper extends BaseMapper<PlayerdiseasesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PlayernpcsEquipMapper`
- 声明: `public interface PlayernpcsEquipMapper extends BaseMapper<PlayernpcsEquipDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PlayernpcsFieldMapper`
- 声明: `public interface PlayernpcsFieldMapper extends BaseMapper<PlayernpcsFieldDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PlayernpcsMapper`
- 声明: `public interface PlayernpcsMapper extends BaseMapper<PlayernpcsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.PlifeMapper`
- 声明: `public interface PlifeMapper extends BaseMapper<PlifeDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.QuestactionsMapper`
- 声明: `public interface QuestactionsMapper extends BaseMapper<QuestactionsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.QuestprogressMapper`
- 声明: `public interface QuestprogressMapper extends BaseMapper<QuestprogressDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.QuestrequirementsMapper`
- 声明: `public interface QuestrequirementsMapper extends BaseMapper<QuestrequirementsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.QueststatusMapper`
- 声明: `public interface QueststatusMapper extends BaseMapper<QueststatusDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.QuickslotkeymappedMapper`
- 声明: `public interface QuickslotkeymappedMapper extends BaseMapper<QuickslotkeymappedDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ReactordropsMapper`
- 声明: `public interface ReactordropsMapper extends BaseMapper<ReactordropsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ReportsMapper`
- 声明: `public interface ReportsMapper extends BaseMapper<ReportsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ResponsesMapper`
- 声明: `public interface ResponsesMapper extends BaseMapper<ResponsesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.RingsMapper`
- 声明: `public interface RingsMapper extends BaseMapper<RingsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.SavedlocationsMapper`
- 声明: `public interface SavedlocationsMapper extends BaseMapper<SavedlocationsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ServerQueueMapper`
- 声明: `public interface ServerQueueMapper extends BaseMapper<ServerQueueDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ShopitemsMapper`
- 声明: `public interface ShopitemsMapper extends BaseMapper<ShopitemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.ShopsMapper`
- 声明: `public interface ShopsMapper extends BaseMapper<ShopsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.SkillmacrosMapper`
- 声明: `public interface SkillmacrosMapper extends BaseMapper<SkillmacrosDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.SkillsMapper`
- 声明: `public interface SkillsMapper extends BaseMapper<SkillsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.SpecialcashitemsMapper`
- 声明: `public interface SpecialcashitemsMapper extends BaseMapper<SpecialcashitemsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.StoragesMapper`
- 声明: `public interface StoragesMapper extends BaseMapper<StoragesDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.TrocklocationsMapper`
- 声明: `public interface TrocklocationsMapper extends BaseMapper<TrocklocationsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.WishlistsMapper`
- 声明: `public interface WishlistsMapper extends BaseMapper<WishlistsDO> {`
- 方法数（启发式提取）: 0

### `org.gms.dao.mapper.WorldtransfersMapper`
- 声明: `public interface WorldtransfersMapper extends BaseMapper<WorldtransfersDO> {`
- 方法数（启发式提取）: 0

## `org.gms.exception`

### `org.gms.exception.BaseErrorInfoInterface`
- 声明: `public interface BaseErrorInfoInterface {`
- 方法数（启发式提取）: 0

### `org.gms.exception.BizException`
- 声明: `public class BizException extends RuntimeException {`
- 方法数（启发式提取）: 12

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

### `org.gms.exception.BizExceptionEnum`
- 声明: `public enum BizExceptionEnum implements BaseErrorInfoInterface {`
- 方法数（启发式提取）: 2

```text
public Integer getResultCode()
public String getResultMsg()
```

### `org.gms.exception.EmptyMovementException`
- 声明: `public class EmptyMovementException extends Exception {`
- 方法数（启发式提取）: 1

```text
public EmptyMovementException(InPacket inPacket)
```

### `org.gms.exception.EventInstanceInProgressException`
- 声明: `public class EventInstanceInProgressException extends Exception {`
- 方法数（启发式提取）: 1

```text
public EventInstanceInProgressException(String eventName, String eventInstance)
```

### `org.gms.exception.GlobalExceptionHandler`
- 声明: `public class GlobalExceptionHandler {`
- 方法数（启发式提取）: 4

```text
public ResultBody<Object> bizExceptionHandler(HttpServletRequest req, BizException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, RuntimeException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, ServletException e)
public ResultBody<Object> exceptionHandler(HttpServletRequest req, Exception e)
```

### `org.gms.exception.IdTypeNotSupportedException`
- 声明: `public class IdTypeNotSupportedException extends Exception {`
- 方法数（启发式提取）: 2

```text
public IdTypeNotSupportedException()
public IdTypeNotSupportedException(String message)
```

### `org.gms.exception.NotEnabledException`
- 声明: `public class NotEnabledException extends RuntimeException {`
- 方法数（启发式提取）: 2

```text
public NotEnabledException()
public NotEnabledException(String message)
```

## `org.gms.manager`

### `org.gms.manager.ServerManager`
- 声明: `public class ServerManager implements ApplicationContextAware, ApplicationRunner, DisposableBean {`
- 方法数（启发式提取）: 3

```text
public void setApplicationContext(@NonNull ApplicationContext applicationContext) throws BeansException
public void run(ApplicationArguments args) throws Exception
public void destroy() throws Exception
```

## `org.gms.model.dto`

### `org.gms.model.dto.AddAccountDTO`
- 声明: `public class AddAccountDTO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.AutobanConfigDTO`
- 声明: `public class AutobanConfigDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.BasePageDTO`
- 声明: `public class BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.CashShopBatchOnSaleReqDTO`
- 声明: `public class CashShopBatchOnSaleReqDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.CashShopSearchRtnDTO`
- 声明: `public class CashShopSearchRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ChannelListRtnDTO`
- 声明: `public class ChannelListRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ChrOnlineListReqDTO`
- 声明: `public class ChrOnlineListReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ChrOnlineListRtnDTO`
- 声明: `public class ChrOnlineListRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.CommandReqDTO`
- 声明: `public class CommandReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ConfigTypeDTO`
- 声明: `public class ConfigTypeDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.DropSearchReqDTO`
- 声明: `public class DropSearchReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.DropSearchRtnDTO`
- 声明: `public class DropSearchRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.EquipmentInfoReqDTO`
- 声明: `public class EquipmentInfoReqDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.EquipmentInfoRtnDTO`
- 声明: `public class EquipmentInfoRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.FileReadDTO`
- 声明: `public class FileReadDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.FileTreeDTO`
- 声明: `public class FileTreeDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.FileTreeNodeDTO`
- 声明: `public class FileTreeNodeDTO {`
- 方法数（启发式提取）: 1

```text
public FileTreeNodeDTO(File file, String key)
```

### `org.gms.model.dto.FileWriteDTO`
- 声明: `public class FileWriteDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.GachaponPoolSearchReqDTO`
- 声明: `public class GachaponPoolSearchReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.GachaponPoolSearchRtnDTO`
- 声明: `public class GachaponPoolSearchRtnDTO extends GachaponRewardPoolDO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.GameConfigReqDTO`
- 声明: `public class GameConfigReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.GiveResourceReqDTO`
- 声明: `public class GiveResourceReqDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.InventoryEquipRtnDTO`
- 声明: `public class InventoryEquipRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.InventorySearchReqDTO`
- 声明: `public class InventorySearchReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.InventorySearchRtnDTO`
- 声明: `public class InventorySearchRtnDTO {`
- 方法数（启发式提取）: 1

```text
public Item toItem()
```

### `org.gms.model.dto.InventoryTypeRtnDTO`
- 声明: `public class InventoryTypeRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.InventoryequipmentReqDTO`
- 声明: `public class InventoryequipmentReqDTO  extends BasePageDTO{`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.InventoryequipmentRtnDTO`
- 声明: `public class InventoryequipmentRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ResultBody`
- 声明: `public class ResultBody<T> {`
- 方法数（启发式提取）: 9

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

### `org.gms.model.dto.ServerInfoReqDto`
- 声明: `public class ServerInfoReqDto {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ServerShutdownDTO`
- 声明: `public class ServerShutdownDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ShopItemSearchRtnDTO`
- 声明: `public class ShopItemSearchRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ShopSearchReqDTO`
- 声明: `public class ShopSearchReqDTO extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.ShopSearchRtnDTO`
- 声明: `public class ShopSearchRtnDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.SubmitBody`
- 声明: `public class SubmitBody<T> {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.UpdateAccountByGmDTO`
- 声明: `public class UpdateAccountByGmDTO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.UpdateAccountByUserDTO`
- 声明: `public class UpdateAccountByUserDTO implements Serializable {`
- 方法数（启发式提取）: 0

### `org.gms.model.dto.WorldListRtnDTO`
- 声明: `public class WorldListRtnDTO {`
- 方法数（启发式提取）: 0

## `org.gms.model.pojo`

### `org.gms.model.pojo.CashCategory`
- 声明: `public class CashCategory extends BasePageDTO {`
- 方法数（启发式提取）: 0

### `org.gms.model.pojo.InformationResult`
- 声明: `public class InformationResult {`
- 方法数（启发式提取）: 0

### `org.gms.model.pojo.InformationSearch`
- 声明: `public class InformationSearch {`
- 方法数（启发式提取）: 0

### `org.gms.model.pojo.NewYearCardRecord`
- 声明: `public class NewYearCardRecord {`
- 方法数（启发式提取）: 10

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
public static void removeAllNewYearCard(boolean send, Character chr)
```

### `org.gms.model.pojo.NextLevelContext`
- 声明: `public class NextLevelContext {`
- 方法数（启发式提取）: 1

```text
public void clear()
```

### `org.gms.model.pojo.RateLimitContext`
- 声明: `public class RateLimitContext {`
- 方法数（启发式提取）: 0

### `org.gms.model.pojo.SkillEntry`
- 声明: `public class SkillEntry {`
- 方法数（启发式提取）: 2

```text
public SkillEntry(byte skillLevel, int masterLevel, long expiration)
public String toString()
```

## `org.gms.net`

### `org.gms.net.AbstractPacketHandler`
- 声明: `public abstract class AbstractPacketHandler implements PacketHandler {`
- 方法数（启发式提取）: 1

```text
public boolean validateState(Client c)
```

### `org.gms.net.ChannelDependencies`
- 声明: `(未解析) ChannelDependencies`
- 方法数（启发式提取）: 1

```text
public record ChannelDependencies(NoteService noteService, FredrickProcessor fredrickProcessor)
```

### `org.gms.net.PacketHandler`
- 声明: `public interface PacketHandler {`
- 方法数（启发式提取）: 0

### `org.gms.net.PacketProcessor`
- 声明: `public final class PacketProcessor {`
- 方法数（启发式提取）: 7

```text
public static void registerGameHandlerDependencies(ChannelDependencies channelDependencies)
public static PacketProcessor getLoginServerProcessor()
public static PacketProcessor getChannelServerProcessor(int world, int channel)
public PacketHandler getHandler(short packetId)
public void registerHandler(Opcode code, PacketHandler handler)
public synchronized static PacketProcessor getProcessor(int world, int channel)
public void reset(int channel)
```

## `org.gms.net.encryption`

### `org.gms.net.encryption.ClientCyphers`
- 声明: `public class ClientCyphers {`
- 方法数（启发式提取）: 3

```text
public static ClientCyphers of(InitializationVector sendIv, InitializationVector receiveIv)
public MapleAESOFB getSendCypher()
public MapleAESOFB getReceiveCypher()
```

### `org.gms.net.encryption.InitializationVector`
- 声明: `public class InitializationVector {`
- 方法数（启发式提取）: 3

```text
public byte[] getBytes()
public static InitializationVector generateSend()
public static InitializationVector generateReceive()
```

### `org.gms.net.encryption.MapleAESOFB`
- 声明: `public class MapleAESOFB {`
- 方法数（启发式提取）: 7

```text
public MapleAESOFB(InitializationVector iv, short mapleVersion)
public synchronized byte[] crypt(byte[] data)
public byte[] getPacketHeader(int length)
public static int getPacketLength(int packetHeader)
public boolean isValidHeader(int packetHeader)
public static byte[] getNewIv(byte[] oldIv)
public String toString()
```

### `org.gms.net.encryption.MapleCustomEncryption`
- 声明: `public class MapleCustomEncryption {`
- 方法数（启发式提取）: 2

```text
public static byte[] encryptData(byte[] data)
public static byte[] decryptData(byte[] data)
```

### `org.gms.net.encryption.PacketCodec`
- 声明: `public class PacketCodec extends CombinedChannelDuplexHandler<PacketDecoder, PacketEncoder> {`
- 方法数（启发式提取）: 1

```text
public PacketCodec(ProtocolFactory protocolFactory)
```

### `org.gms.net.encryption.PacketDecoder`
- 声明: `public class PacketDecoder extends ReplayingDecoder<Void> {`
- 方法数（启发式提取）: 1

```text
public PacketDecoder(ProtocolFactory protocolFactory)
```

### `org.gms.net.encryption.PacketEncoder`
- 声明: `public class PacketEncoder extends MessageToByteEncoder<Packet> {`
- 方法数（启发式提取）: 1

```text
public PacketEncoder(ProtocolFactory protocolFactory)
```

## `org.gms.net.encryption.protocol`

### `org.gms.net.encryption.protocol.GMSV83PacketProtocol`
- 声明: `public class GMSV83PacketProtocol implements PacketProtocol {`
- 方法数（启发式提取）: 4

```text
public GMSV83PacketProtocol(ClientCyphers clientCyphers)
public void decode(ChannelHandlerContext context, ByteBuf in, List<Object> out)
public void encode(ChannelHandlerContext ctx, Packet in, ByteBuf out)
public void writeInitialUnencryptedHelloPacket(SocketChannel socketChannel, InitializationVector sendIv, InitializationVector recvIv, Client client)
```

### `org.gms.net.encryption.protocol.PacketProtocol`
- 声明: `public interface PacketProtocol {`
- 方法数（启发式提取）: 0

### `org.gms.net.encryption.protocol.ProtocolConstants`
- 声明: `public class ProtocolConstants {`
- 方法数（启发式提取）: 0

### `org.gms.net.encryption.protocol.ProtocolFactory`
- 声明: `public class ProtocolFactory {`
- 方法数（启发式提取）: 2

```text
public ProtocolFactory(ClientCyphers clientCyphers)
public PacketProtocol getProtocol(short version)
```

## `org.gms.net.netty`

### `org.gms.net.netty.AbstractServer`
- 声明: `public abstract class AbstractServer {`
- 方法数（启发式提取）: 2

```text
public abstract void start()
public abstract void stop()
```

### `org.gms.net.netty.ChannelServer`
- 声明: `public class ChannelServer extends AbstractServer {`
- 方法数（启发式提取）: 3

```text
public ChannelServer(int port, int world, int channel)
public void start()
public void stop()
```

### `org.gms.net.netty.ChannelServerInitializer`
- 声明: `public class ChannelServerInitializer extends ServerChannelInitializer {`
- 方法数（启发式提取）: 2

```text
public ChannelServerInitializer(int world, int channel)
public void initChannel(SocketChannel socketChannel)
```

### `org.gms.net.netty.InvalidPacketHeaderException`
- 声明: `public class InvalidPacketHeaderException extends RuntimeException {`
- 方法数（启发式提取）: 2

```text
public InvalidPacketHeaderException(String message, int header)
public int getHeader()
```

### `org.gms.net.netty.LoginServer`
- 声明: `public class LoginServer extends AbstractServer {`
- 方法数（启发式提取）: 3

```text
public LoginServer(int port)
public void start()
public void stop()
```

### `org.gms.net.netty.LoginServerInitializer`
- 声明: `public class LoginServerInitializer extends ServerChannelInitializer {`
- 方法数（启发式提取）: 1

```text
public void initChannel(SocketChannel socketChannel)
```

### `org.gms.net.netty.ServerChannelInitializer`
- 声明: `public abstract class ServerChannelInitializer extends ChannelInitializer<SocketChannel> {`
- 方法数（启发式提取）: 0

## `org.gms.net.opcodes`

### `org.gms.net.opcodes.Opcode`
- 声明: `public interface Opcode {`
- 方法数（启发式提取）: 0

### `org.gms.net.opcodes.RecvOpcode`
- 声明: `public enum RecvOpcode implements Opcode {`
- 方法数（启发式提取）: 2

```text
public int getValue()
public String getName()
```

### `org.gms.net.opcodes.SendOpcode`
- 声明: `public enum SendOpcode implements Opcode {`
- 方法数（启发式提取）: 2

```text
public int getValue()
public String getName()
```

## `org.gms.net.packet`

### `org.gms.net.packet.ByteBufInPacket`
- 声明: `public class ByteBufInPacket implements InPacket {`
- 方法数（启发式提取）: 16

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
```

### `org.gms.net.packet.ByteBufOutPacket`
- 声明: `public class ByteBufOutPacket implements OutPacket {`
- 方法数（启发式提取）: 17

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

### `org.gms.net.packet.InPacket`
- 声明: `public interface InPacket extends Packet {`
- 方法数（启发式提取）: 0

### `org.gms.net.packet.OutPacket`
- 声明: `public interface OutPacket extends Packet {`
- 方法数（启发式提取）: 0

### `org.gms.net.packet.Packet`
- 声明: `public interface Packet {`
- 方法数（启发式提取）: 0

## `org.gms.net.packet.logging`

### `org.gms.net.packet.logging.InPacketLogger`
- 声明: `public class InPacketLogger extends ChannelInboundHandlerAdapter implements PacketLogger {`
- 方法数（启发式提取）: 2

```text
public void channelRead(ChannelHandlerContext ctx, Object msg)
public void log(Packet packet)
```

### `org.gms.net.packet.logging.LoggingUtil`
- 声明: `public class LoggingUtil {`
- 方法数（启发式提取）: 2

```text
public static short readFirstShort(byte[] bytes)
public static boolean isIgnoredRecvPacket(short opcode)
```

### `org.gms.net.packet.logging.MonitoredChrLogger`
- 声明: `public class MonitoredChrLogger {`
- 方法数（启发式提取）: 3

```text
public static boolean toggleMonitored(int chrId)
public static Collection<Integer> getMonitoredChrIds()
public static void logPacketIfMonitored(Client c, short packetId, byte[] packetContent)
```

### `org.gms.net.packet.logging.OutPacketLogger`
- 声明: `public class OutPacketLogger extends ChannelOutboundHandlerAdapter implements PacketLogger {`
- 方法数（启发式提取）: 2

```text
public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise)
public void log(Packet packet)
```

### `org.gms.net.packet.logging.PacketLogger`
- 声明: `public interface PacketLogger {`
- 方法数（启发式提取）: 0

## `org.gms.net.packet.out`

### `org.gms.net.packet.out.SendNoteSuccessPacket`
- 声明: `public final class SendNoteSuccessPacket extends ByteBufOutPacket {`
- 方法数（启发式提取）: 1

```text
public SendNoteSuccessPacket()
```

### `org.gms.net.packet.out.ShowNotesPacket`
- 声明: `public final class ShowNotesPacket extends ByteBufOutPacket {`
- 方法数（启发式提取）: 1

```text
public ShowNotesPacket(List<NotesDO> notes)
```

## `org.gms.net.server`

### `org.gms.net.server.PlayerBuffStorage`
- 声明: `public class PlayerBuffStorage {`
- 方法数（启发式提取）: 6

```text
public void addBuffsToStorage(int chrid, List<PlayerBuffValueHolder> toStore)
public List<PlayerBuffValueHolder> getBuffsFromStorage(int chrid)
public void addDiseasesToStorage(int chrid, Map<Disease, Pair<Long, MobSkill>> toStore)
public Map<Disease, Pair<Long, MobSkill>> getDiseasesFromStorage(int chrid)
public int hashCode()
public boolean equals(Object obj)
```

### `org.gms.net.server.PlayerBuffValueHolder`
- 声明: `public class PlayerBuffValueHolder {`
- 方法数（启发式提取）: 1

```text
public PlayerBuffValueHolder(int usedTime, StatEffect effect)
```

### `org.gms.net.server.PlayerCoolDownValueHolder`
- 声明: `public class PlayerCoolDownValueHolder {`
- 方法数（启发式提取）: 1

```text
public PlayerCoolDownValueHolder(int skillId, long startTime, long length)
```

### `org.gms.net.server.PlayerDiseaseValueHolder`
- 声明: `public class PlayerDiseaseValueHolder {//Thanks Celino`
- 方法数（启发式提取）: 1

```text
public PlayerDiseaseValueHolder(final Disease disease, final long startTime, final long length)
```

### `org.gms.net.server.PlayerStorage`
- 声明: `public class PlayerStorage {`
- 方法数（启发式提取）: 8

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

### `org.gms.net.server.Server`
- 声明: `public class Server {`
- 方法数（启发式提取）: 98

```text
public static Server getInstance()
public static long uptime = System.currentTimeMillis()
public int getCurrentTimestamp()
public long getCurrentTime()
public void updateCurrentTime()
public long forceUpdateCurrentTime()
public List<Pair<Integer, String>> worldRecommendedList()
public void setNewYearCard(NewYearCardRecord nyc)
public NewYearCardRecord getNewYearCard(int cardid)
public NewYearCardRecord removeNewYearCard(int cardid)
public void setAvailableDeveloperRoom()
public boolean canEnterDeveloperRoom()
public World getWorld(int id)
public List<World> getWorlds()
public int getWorldsSize()
public Channel getChannel(int world, int channel)
public List<Channel> getChannelsFromWorld(int world)
public List<Channel> getAllChannels()
public Set<Integer> getOpenChannels(int world)
public String[] getInetSocket(Client client, int world, int channel)
public int addChannel(int worldid)
public int addWorld()
public boolean removeChannel(int worldid)
public boolean removeWorld()
public static long getTimeLeftForNextDay()
public Map<Integer, Integer> getCouponRates()
public List<Integer> getActiveCoupons()
public void commitActiveCoupons()
public void toggleCoupon(Integer couponId)
public void updateActiveCoupons()
public void runAnnouncePlayerDiseasesSchedule()
public void registerAnnouncePlayerDiseases(Client c)
public List<Pair<String, Integer>> getWorldPlayerRanking(int worldid)
public void reloadWorldsPlayerRanking()
public void init()
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
public void updateCharacterEntry(Character chr)
public void createCharacterEntry(Character chr)
public void deleteCharacterEntry(Integer accountid, Integer chrid)
public void transferWorldCharacterEntry(Character chr, Integer toWorld)
public void deleteAccountEntry(Integer accountid)
public SortedMap<Integer, List<Character>> loadAccountCharlist(int accountId, int visibleWorlds)
public void loadAllAccountsCharactersView()
public void loadAccountCharacters(Client c)
public void loadAccountStorages(Client c)
public void setCharacteridInTransition(Client client, int charId)
public boolean validateCharacteridInTransition(Client client, int charId)
public Integer freeCharacteridInTransition(Client client)
public boolean hasCharacteridInTransition(Client client)
public void registerLoginState(Client c)
public void unregisterLoginState(Client c)
public final Runnable shutdown(final boolean restart)
public synchronized void shutdownInternal(boolean restart)
public boolean isNextTime()
public synchronized void shutdownWithMsgAndInternal(ServerShutdownDTO serverShutdownDTO)
```

## `org.gms.net.server.channel`

### `org.gms.net.server.channel.Channel`
- 声明: `public final class Channel {`
- 方法数（启发式提取）: 71

```text
public Channel(final int world, final int channel, long startTime)
public synchronized void reloadEventScriptManager()
public synchronized void shutdown()
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
public Map<Integer, HiredMerchant> getHiredMerchants()
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
public int getStoredVar(int key)
public void setStoredVar(int key, int val)
public int lookupPartyDojo(Party party)
public int ingressDojo(boolean isPartyDojo, int fromStage)
public int ingressDojo(boolean isPartyDojo, Party party, int fromStage)
public void resetDojoMap(int fromMapId)
public void resetDojo(int dojoMapId)
public void freeDojoSectionIfEmpty(int dojoMapId)
public void dismissDojoSchedule(int dojoMapId, Party party)
public boolean setDojoProgress(int dojoMapId)
public long getDojoFinishTime(int dojoMapId)
public boolean addMiniDungeon(int dungeonid)
public MiniDungeon getMiniDungeon(int dungeonid)
public void removeMiniDungeon(int dungeonid)
public Pair<Boolean, Pair<Integer, Set<Integer>>> getNextWeddingReservation(boolean cathedral)
public boolean isWeddingReserved(Integer weddingId)
public int getWeddingReservationStatus(Integer weddingId, boolean cathedral)
public int pushWeddingReservation(Integer weddingId, boolean cathedral, boolean premium, Integer groomId, Integer brideId)
public boolean isOngoingWeddingGuest(boolean cathedral, int playerId)
public Integer getOngoingWedding(boolean cathedral)
public boolean getOngoingWeddingType(boolean cathedral)
public void closeOngoingWedding(boolean cathedral)
public void setOngoingWedding(final boolean cathedral, Boolean premium, Integer weddingId, Set<Integer> guests)
public synchronized boolean acceptOngoingWedding(final boolean cathedral)
public long getWeddingTicketExpireTime(int resSlot)
public static long getRelativeWeddingTicketExpireTime(int resSlot)
public String getWeddingReservationTimeLeft(Integer weddingId)
public Pair<Integer, Integer> getWeddingCoupleForGuest(int guestId, boolean cathedral)
public void dropMessage(int type, String message)
public void registerOwnedMap(MapleMap map)
public void unregisterOwnedMap(MapleMap map)
public void runCheckOwnedMapsSchedule()
public void initMonsterCarnival(boolean cpq1, int field)
public void finishMonsterCarnival(boolean cpq1, int field)
public boolean canInitMonsterCarnival(boolean cpq1, int field)
public void debugMarriageStatus()
```

### `org.gms.net.server.channel.CharacterIdChannelPair`
- 声明: `public class CharacterIdChannelPair {`
- 方法数（启发式提取）: 4

```text
public CharacterIdChannelPair()
public CharacterIdChannelPair(int charid, int channel)
public int getCharacterId()
public int getChannel()
```

## `org.gms.net.server.channel.handlers`

### `org.gms.net.server.channel.handlers.AbstractDealDamageHandler`
- 声明: `public abstract class AbstractDealDamageHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public Point position = new Point()
public StatEffect getAttackEffect(Character chr, Skill theSkill)
```

### `org.gms.net.server.channel.handlers.AbstractMovementPacketHandler`
- 声明: `public abstract class AbstractMovementPacketHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 0

### `org.gms.net.server.channel.handlers.AcceptFamilyHandler`
- 声明: `public final class AcceptFamilyHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AdminChatHandler`
- 声明: `public class AdminChatHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AdminCommandHandler`
- 声明: `public final class AdminCommandHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AdminLogHandler`
- 声明: `public final class AdminLogHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AllianceOperationHandler`
- 声明: `public final class AllianceOperationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AranComboHandler`
- 声明: `public class AranComboHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AutoAggroHandler`
- 声明: `public final class AutoAggroHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.AutoAssignHandler`
- 声明: `public class AutoAssignHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.BBSOperationHandler`
- 声明: `public final class BBSOperationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 5

```text
public void handlePacket(InPacket p, Client c)
public static void deleteBBSThread(Client client, int localthreadid)
public static void deleteBBSReply(Client client, int replyid)
public static void displayThread(Client client, int threadid)
public static void displayThread(Client client, int threadid, boolean bIsThreadIdLocal)
```

### `org.gms.net.server.channel.handlers.BeholderHandler`
- 声明: `public final class BeholderHandler extends AbstractPacketHandler {//Summon Skills noobs`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.BuddylistModifyHandler`
- 声明: `public class BuddylistModifyHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 3

```text
public CharacterIdNameBuddyCapacity(int id, String name, int buddyCapacity)
public int getBuddyCapacity()
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CancelBuffHandler`
- 声明: `public final class CancelBuffHandler extends AbstractPacketHandler implements PacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CancelChairHandler`
- 声明: `public final class CancelChairHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CancelDebuffHandler`
- 声明: `public final class CancelDebuffHandler extends AbstractPacketHandler {//TIP: BAD STUFF LOL!`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CancelItemEffectHandler`
- 声明: `public final class CancelItemEffectHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CashOperationHandler`
- 声明: `public final class CashOperationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 3

```text
public CashOperationHandler(NoteService noteService)
public void handlePacket(InPacket p, Client c)
public static boolean checkBirthday(Client c, int idate)
```

### `org.gms.net.server.channel.handlers.CashShopSurpriseHandler`
- 声明: `public class CashShopSurpriseHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ChangeChannelHandler`
- 声明: `public final class ChangeChannelHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ChangeMapHandler`
- 声明: `public final class ChangeMapHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ChangeMapSpecialHandler`
- 声明: `public final class ChangeMapSpecialHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CharInfoRequestHandler`
- 声明: `public final class CharInfoRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ClickGuideHandler`
- 声明: `public class ClickGuideHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CloseChalkboardHandler`
- 声明: `public final class CloseChalkboardHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CloseRangeDamageHandler`
- 声明: `public final class CloseRangeDamageHandler extends AbstractDealDamageHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CoconutHandler`
- 声明: `public final class CoconutHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.CouponCodeHandler`
- 声明: `public final class CouponCodeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DamageSummonHandler`
- 声明: `public final class DamageSummonHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DenyAllianceRequestHandler`
- 声明: `public final class DenyAllianceRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DenyGuildRequestHandler`
- 声明: `public final class DenyGuildRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DenyPartyRequestHandler`
- 声明: `public final class DenyPartyRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DistributeAPHandler`
- 声明: `public final class DistributeAPHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DistributeSPHandler`
- 声明: `public final class DistributeSPHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DoorHandler`
- 声明: `public final class DoorHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.DueyHandler`
- 声明: `public final class DueyHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.EnterCashShopHandler`
- 声明: `public class EnterCashShopHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.EnterMTSHandler`
- 声明: `public final class EnterMTSHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FaceExpressionHandler`
- 声明: `public final class FaceExpressionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FamilyAddHandler`
- 声明: `public final class FamilyAddHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FamilyPreceptsHandler`
- 声明: `public class FamilyPreceptsHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FamilySeparateHandler`
- 声明: `public class FamilySeparateHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FamilySummonResponseHandler`
- 声明: `public class FamilySummonResponseHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FamilyUseHandler`
- 声明: `public final class FamilyUseHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FieldDamageMobHandler`
- 声明: `public class FieldDamageMobHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.FredrickHandler`
- 声明: `public class FredrickHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public FredrickHandler(FredrickProcessor fredrickProcessor)
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.GeneralChatHandler`
- 声明: `public final class GeneralChatHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.GiveFameHandler`
- 声明: `public final class GiveFameHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.GrenadeEffectHandler`
- 声明: `public class GrenadeEffectHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.GuildOperationHandler`
- 声明: `public final class GuildOperationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.HealOvertimeHandler`
- 声明: `public final class HealOvertimeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.HiredMerchantRequest`
- 声明: `public final class HiredMerchantRequest extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.InnerPortalHandler`
- 声明: `public final class InnerPortalHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.InventoryMergeHandler`
- 声明: `public final class InventoryMergeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.InventorySortHandler`
- 声明: `public final class InventorySortHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 3

```text
public void reverseSortSublist(ArrayList<Item> A, int[] range)
public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ItemMoveHandler`
- 声明: `public final class ItemMoveHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ItemPickupHandler`
- 声明: `public final class ItemPickupHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(final InPacket p, final Client c)
```

### `org.gms.net.server.channel.handlers.ItemRewardHandler`
- 声明: `public final class ItemRewardHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.KeymapChangeHandler`
- 声明: `public final class KeymapChangeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.LeftKnockbackHandler`
- 声明: `public class LeftKnockbackHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, final Client c)
```

### `org.gms.net.server.channel.handlers.MTSHandler`
- 声明: `public final class MTSHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 5

```text
public void handlePacket(InPacket p, Client c)
public List<MTSItemInfo> getNotYetSold(int cid)
public Packet getCart(int cid)
public List<MTSItemInfo> getTransfer(int cid)
public Packet getMTSSearch(int tab, int type, int cOi, String search, int page)
```

### `org.gms.net.server.channel.handlers.MagicDamageHandler`
- 声明: `public final class MagicDamageHandler extends AbstractDealDamageHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MakerSkillHandler`
- 声明: `public final class MakerSkillHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MesoDropHandler`
- 声明: `public final class MesoDropHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MessengerHandler`
- 声明: `public final class MessengerHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MobBanishPlayerHandler`
- 声明: `public final class MobBanishPlayerHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MobDamageMobFriendlyHandler`
- 声明: `public final class MobDamageMobFriendlyHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MobDamageMobHandler`
- 声明: `public final class MobDamageMobHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MonsterBombHandler`
- 声明: `public final class MonsterBombHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MonsterBookCoverHandler`
- 声明: `public final class MonsterBookCoverHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MonsterCarnivalHandler`
- 声明: `public final class MonsterCarnivalHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MoveDragonHandler`
- 声明: `public class MoveDragonHandler extends AbstractMovementPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MoveLifeHandler`
- 声明: `public final class MoveLifeHandler extends AbstractMovementPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MovePetHandler`
- 声明: `public final class MovePetHandler extends AbstractMovementPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MovePlayerHandler`
- 声明: `public final class MovePlayerHandler extends AbstractMovementPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MoveSummonHandler`
- 声明: `public final class MoveSummonHandler extends AbstractMovementPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.MultiChatHandler`
- 声明: `public final class MultiChatHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NPCAnimationHandler`
- 声明: `public final class NPCAnimationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NPCMoreTalkHandler`
- 声明: `public final class NPCMoreTalkHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NPCShopHandler`
- 声明: `public final class NPCShopHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NPCTalkHandler`
- 声明: `public final class NPCTalkHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NewYearCardHandler`
- 声明: `public final class NewYearCardHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.NoteActionHandler`
- 声明: `public final class NoteActionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public NoteActionHandler(NoteService noteService)
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.OpenFamilyHandler`
- 声明: `public final class OpenFamilyHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.OpenFamilyPedigreeHandler`
- 声明: `public final class OpenFamilyPedigreeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.OwlWarpHandler`
- 声明: `public final class OwlWarpHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PartyOperationHandler`
- 声明: `public final class PartyOperationHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PartySearchRegisterHandler`
- 声明: `public class PartySearchRegisterHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PartySearchStartHandler`
- 声明: `public class PartySearchStartHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PartySearchUpdateHandler`
- 声明: `public final class PartySearchUpdateHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetAutoPotHandler`
- 声明: `public final class PetAutoPotHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetChatHandler`
- 声明: `public final class PetChatHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetCommandHandler`
- 声明: `public final class PetCommandHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetExcludeItemsHandler`
- 声明: `public final class PetExcludeItemsHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetFoodHandler`
- 声明: `public final class PetFoodHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PetLootHandler`
- 声明: `public final class PetLootHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PlayerInteractionHandler`
- 声明: `public final class PlayerInteractionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public byte getCode()
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PlayerLoggedinHandler`
- 声明: `public final class PlayerLoggedinHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 3

```text
public PlayerLoggedinHandler(NoteService noteService)
public final boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.PlayerMapTransitionHandler`
- 声明: `public final class PlayerMapTransitionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.QuestActionHandler`
- 声明: `public final class QuestActionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.QuickslotKeyMappedModifiedHandler`
- 声明: `public class QuickslotKeyMappedModifiedHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RPSActionHandler`
- 声明: `public final class RPSActionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RaiseIncExpHandler`
- 声明: `public class RaiseIncExpHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RaiseUIStateHandler`
- 声明: `public class RaiseUIStateHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RangedAttackHandler`
- 声明: `public final class RangedAttackHandler extends AbstractDealDamageHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ReactorHitHandler`
- 声明: `public final class ReactorHitHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RemoteGachaponHandler`
- 声明: `public final class RemoteGachaponHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RemoteStoreHandler`
- 声明: `public class RemoteStoreHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ReportHandler`
- 声明: `public final class ReportHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.RingActionHandler`
- 声明: `public final class RingActionHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 5

```text
public RingActionHandler(NoteService noteService)
public static void sendEngageProposal(final Client c, final String name, final int itemid)
public static void breakMarriageRing(Character chr, final int wItemId)
public static void giveMarriageRings(Character player, Character partner, int marriageRingId)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ScriptedItemHandler`
- 声明: `public final class ScriptedItemHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.ScrollHandler`
- 声明: `public final class ScrollHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SetHpMpAlertHandler`
- 声明: `public class SetHpMpAlertHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SkillBookHandler`
- 声明: `public final class SkillBookHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SkillEffectHandler`
- 声明: `public final class SkillEffectHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SkillMacroHandler`
- 声明: `public final class SkillMacroHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SnowballHandler`
- 声明: `public final class SnowballHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SpawnPetHandler`
- 声明: `public final class SpawnPetHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SpecialMoveHandler`
- 声明: `public final class SpecialMoveHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SpouseChatHandler`
- 声明: `public final class SpouseChatHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.StorageHandler`
- 声明: `public final class StorageHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.SummonDamageHandler`
- 声明: `public final class SummonDamageHandler extends AbstractDealDamageHandler {`
- 方法数（启发式提取）: 4

```text
public SummonAttackEntry(int monsterOid, int damage)
public int getMonsterOid()
public int getDamage()
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TakeDamageHandler`
- 声明: `public final class TakeDamageHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TouchMonsterDamageHandler`
- 声明: `public final class TouchMonsterDamageHandler extends AbstractDealDamageHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TouchReactorHandler`
- 声明: `public final class TouchReactorHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TouchingCashShopHandler`
- 声明: `public final class TouchingCashShopHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TransferNameHandler`
- 声明: `public final class TransferNameHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TransferNameResultHandler`
- 声明: `public final class TransferNameResultHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TransferWorldHandler`
- 声明: `public final class TransferWorldHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.TrockAddMapHandler`
- 声明: `public final class TrockAddMapHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseCashItemHandler`
- 声明: `public final class UseCashItemHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public UseCashItemHandler(NoteService noteService)
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseCatchItemHandler`
- 声明: `public final class UseCatchItemHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseChairHandler`
- 声明: `public final class UseChairHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseDeathItemHandler`
- 声明: `public final class UseDeathItemHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseGachaExpHandler`
- 声明: `public class UseGachaExpHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseHammerHandler`
- 声明: `public final class UseHammerHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseItemEffectHandler`
- 声明: `public final class UseItemEffectHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseItemHandler`
- 声明: `public final class UseItemHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseMapleLifeHandler`
- 声明: `public class UseMapleLifeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseMountFoodHandler`
- 声明: `public final class UseMountFoodHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseOwlOfMinervaHandler`
- 声明: `public final class UseOwlOfMinervaHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseSolomonHandler`
- 声明: `public final class UseSolomonHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseSummonBagHandler`
- 声明: `public final class UseSummonBagHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseTreasureChestHandler`
- 声明: `public final class UseTreasureChestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.UseWaterOfLifeHandler`
- 声明: `public final class UseWaterOfLifeHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.WeddingHandler`
- 声明: `public final class WeddingHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.WeddingTalkHandler`
- 声明: `public final class WeddingTalkHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.WeddingTalkMoreHandler`
- 声明: `public final class WeddingTalkMoreHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.channel.handlers.WhisperHandler`
- 声明: `public final class WhisperHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

## `org.gms.net.server.coordinator.login`

### `org.gms.net.server.coordinator.login.LoginBypassCoordinator`
- 声明: `public class LoginBypassCoordinator {`
- 方法数（启发式提取）: 5

```text
public static LoginBypassCoordinator getInstance()
public boolean canLoginBypass(Hwid hwid, int accId, boolean pic)
public void registerLoginBypassEntry(Hwid hwid, int accId, boolean pic)
public void unregisterLoginBypassEntry(Hwid hwid, int accId)
public void runUpdateLoginBypass()
```

### `org.gms.net.server.coordinator.login.LoginStorage`
- 声明: `public class LoginStorage {`
- 方法数（启发式提取）: 2

```text
public boolean registerLogin(int accountId)
public void clearExpiredAttempts()
```

## `org.gms.net.server.coordinator.matchchecker`

### `org.gms.net.server.coordinator.matchchecker.AbstractMatchCheckerListener`
- 声明: `public interface AbstractMatchCheckerListener {`
- 方法数（启发式提取）: 0

### `org.gms.net.server.coordinator.matchchecker.MatchCheckerCoordinator`
- 声明: `public class MatchCheckerCoordinator {`
- 方法数（启发式提取）: 6

```text
public int getMatchConfirmationLeaderid(int cid)
public MatchCheckerType getMatchConfirmationType(int cid)
public boolean isMatchConfirmationActive(int cid)
public boolean createMatchConfirmation(MatchCheckerType matchType, int world, int leaderCid, Set<Integer> players, String message)
public boolean answerMatchConfirmation(int cid, boolean accept)
public boolean dismissMatchConfirmation(int cid)
```

### `org.gms.net.server.coordinator.matchchecker.MatchCheckerListenerFactory`
- 声明: `public class MatchCheckerListenerFactory {`
- 方法数（启发式提取）: 1

```text
public AbstractMatchCheckerListener getListener()
```

### `org.gms.net.server.coordinator.matchchecker.MatchCheckerListenerRecipe`
- 声明: `public interface MatchCheckerListenerRecipe {`
- 方法数（启发式提取）: 0

## `org.gms.net.server.coordinator.matchchecker.listener`

### `org.gms.net.server.coordinator.matchchecker.listener.MatchCheckerCPQChallenge`
- 声明: `public class MatchCheckerCPQChallenge implements MatchCheckerListenerRecipe {`
- 方法数（启发式提取）: 6

```text
public static AbstractMatchCheckerListener loadListener()
public AbstractMatchCheckerListener getListener()
public void onMatchCreated(Character leader, Set<Character> nonLeaderMatchPlayers, String message)
public void onMatchAccepted(int leaderid, Set<Character> matchPlayers, String message)
public void onMatchDeclined(int leaderid, Set<Character> matchPlayers, String message)
public void onMatchDismissed(int leaderid, Set<Character> matchPlayers, String message)
```

### `org.gms.net.server.coordinator.matchchecker.listener.MatchCheckerGuildCreation`
- 声明: `public class MatchCheckerGuildCreation implements MatchCheckerListenerRecipe {`
- 方法数（启发式提取）: 6

```text
public static AbstractMatchCheckerListener loadListener()
public AbstractMatchCheckerListener getListener()
public void onMatchCreated(Character leader, Set<Character> nonLeaderMatchPlayers, String message)
public void onMatchAccepted(int leaderid, Set<Character> matchPlayers, String message)
public void onMatchDeclined(int leaderid, Set<Character> matchPlayers, String message)
public void onMatchDismissed(int leaderid, Set<Character> matchPlayers, String message)
```

## `org.gms.net.server.coordinator.partysearch`

### `org.gms.net.server.coordinator.partysearch.PartySearchCharacter`
- 声明: `public class PartySearchCharacter {`
- 方法数（启发式提取）: 6

```text
public PartySearchCharacter(Character chr)
public String toString()
public Character callPlayer(int leaderid, int callerMapid)
public Character getPlayer()
public int getLevel()
public boolean isQueued()
```

### `org.gms.net.server.coordinator.partysearch.PartySearchCoordinator`
- 声明: `public class PartySearchCoordinator {`
- 方法数（启发式提取）: 8

```text
public PartySearchCoordinator()
public static boolean isInVicinity(int callerMapid, int calleeMapid)
public void attachPlayer(Character chr)
public void detachPlayer(Character chr)
public void updatePartySearchStorage()
public void registerPartyLeader(Character leader, int minLevel, int maxLevel, int jobs)
public void unregisterPartyLeader(Character leader)
public void runPartySearch()
```

### `org.gms.net.server.coordinator.partysearch.PartySearchEchelon`
- 声明: `public class PartySearchEchelon {`
- 方法数（启发式提取）: 4

```text
public PartySearchEchelon()
public List<Character> exportEchelon()
public void attachPlayer(Character chr)
public boolean detachPlayer(Character chr)
```

### `org.gms.net.server.coordinator.partysearch.PartySearchStorage`
- 声明: `public class PartySearchStorage {`
- 方法数（启发式提取）: 5

```text
public PartySearchStorage()
public List<PartySearchCharacter> getStorageList()
public void updateStorage(Collection<Character> echelon)
public Character callPlayer(int callerCid, int callerMapid, int minLevel, int maxLevel)
public void detachPlayer(Character chr)
```

## `org.gms.net.server.coordinator.session`

### `org.gms.net.server.coordinator.session.HostHwid`
- 声明: `(未解析) HostHwid`
- 方法数（启发式提取）: 0

### `org.gms.net.server.coordinator.session.HostHwidCache`
- 声明: `(未解析) HostHwidCache`
- 方法数（启发式提取）: 0

### `org.gms.net.server.coordinator.session.Hwid`
- 声明: `(未解析) Hwid`
- 方法数（启发式提取）: 2

```text
public record Hwid(String hwid)
public static Hwid fromHostString(String hostString) throws IllegalArgumentException
```

### `org.gms.net.server.coordinator.session.HwidAssociationExpiry`
- 声明: `public class HwidAssociationExpiry {`
- 方法数（启发式提取）: 1

```text
public static Instant getHwidAccountExpiry(int relevance)
```

### `org.gms.net.server.coordinator.session.HwidRelevance`
- 声明: `(未解析) HwidRelevance`
- 方法数（启发式提取）: 2

```text
public record HwidRelevance(String hwid, int relevance)
public int getIncrementedRelevance()
```

### `org.gms.net.server.coordinator.session.InitializationResult`
- 声明: `(未解析) InitializationResult`
- 方法数（启发式提取）: 1

```text
public AntiMulticlientResult getAntiMulticlientResult()
```

### `org.gms.net.server.coordinator.session.IpAddresses`
- 声明: `public class IpAddresses {`
- 方法数（启发式提取）: 2

```text
public static boolean isLocalAddress(String inetAddress)
public static boolean isLanAddress(String inetAddress)
```

### `org.gms.net.server.coordinator.session.SessionCoordinator`
- 声明: `public class SessionCoordinator {`
- 方法数（启发式提取）: 14

```text
public static SessionCoordinator getInstance()
public static String getSessionRemoteHost(Client client)
public void updateOnlineClient(Client client)
public boolean canStartLoginSession(Client client)
public void closeLoginSession(Client client)
public AntiMulticlientResult attemptLoginSession(Client client, Hwid hwid, int accountId, boolean routineCheck)
public AntiMulticlientResult attemptGameSession(Client client, int accountId, Hwid hwid)
public void closeSession(Client client, Boolean immediately)
public Hwid pickLoginSessionHwid(Client client)
public Hwid getGameSessionHwid(Client client)
public void clearExpiredHwidHistory()
public void runUpdateLoginHistory()
public void printSessionTrace()
public void printSessionTrace(Client c)
```

### `org.gms.net.server.coordinator.session.SessionDAO`
- 声明: `public class SessionDAO {`
- 方法数（启发式提取）: 5

```text
public static void deleteExpiredHwidAccounts()
public static List<Hwid> getHwidsForAccount(Connection con, int accountId) throws SQLException
public static void registerAccountAccess(Connection con, int accountId, Hwid hwid, Instant expiry)
public static List<HwidRelevance> getHwidRelevance(Connection con, int accountId) throws SQLException
public static void updateAccountAccess(Connection con, Hwid hwid, int accountId, Instant expiry, int loginRelevance)
```

### `org.gms.net.server.coordinator.session.SessionInitialization`
- 声明: `public class SessionInitialization {`
- 方法数（启发式提取）: 2

```text
public InitializationResult initialize(String remoteHost)
public void finalize(String remoteHost)
```

## `org.gms.net.server.coordinator.world`

### `org.gms.net.server.coordinator.world.EventRecallCoordinator`
- 声明: `public class EventRecallCoordinator {`
- 方法数（启发式提取）: 4

```text
public static EventRecallCoordinator getInstance()
public EventInstanceManager recallEventInstance(int characterId)
public void storeEventInstance(int characterId, EventInstanceManager eim)
public void manageEventInstances()
```

### `org.gms.net.server.coordinator.world.InviteCoordinator`
- 声明: `public class InviteCoordinator {`
- 方法数（启发式提取）: 6

```text
public static boolean createInvite(InviteType type, Character from, Object referenceFrom, int targetCid, Object... params)
public static boolean hasInvite(InviteType type, int targetCid)
public static InviteResult answerInvite(InviteType type, int targetCid, Object referenceFrom, boolean answer)
public static void removeInvite(InviteType type, int targetCid)
public static void removePlayerIncomingInvites(int cid)
public static void runTimeoutSchedule()
```

### `org.gms.net.server.coordinator.world.MonsterAggroCoordinator`
- 声明: `public class MonsterAggroCoordinator {`
- 方法数（启发式提取）: 10

```text
public void stopAggroCoordinator()
public void startAggroCoordinator()
public void addAggroDamage(Monster mob, int cid, int damage)
public boolean isLeadingCharacterAggro(Monster mob, Character player)
public void runSortLeadingCharactersAggro()
public void removeAggroEntries(Monster mob)
public void addPuppetAggro(Character player)
public void removePuppetAggro(Integer cid)
public List<Integer> getPuppetAggroList()
public void dispose()
```

## `org.gms.net.server.guild`

### `org.gms.net.server.guild.Alliance`
- 声明: `public class Alliance {`
- 方法数（启发式提取）: 28

```text
public Alliance(String name, int id)
public static boolean canBeUsedAllianceName(String name)
public static Alliance createAlliance(Party party, String name)
public static Alliance createAllianceOnDb(List<Integer> guilds, String name)
public static Alliance loadAlliance(int id)
public void saveToDB()
public static void disbandAlliance(int allianceId)
public static boolean removeGuildFromAlliance(int allianceId, int guildId, int worldId)
public void updateAlliancePackets(Character chr)
public boolean removeGuild(int gid)
public boolean addGuild(int gid)
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

### `org.gms.net.server.guild.Guild`
- 声明: `public class Guild {`
- 方法数（启发式提取）: 57

```text
public Guild(int guildid, int world)
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

### `org.gms.net.server.guild.GuildCharacter`
- 声明: `public class GuildCharacter {`
- 方法数（启发式提取）: 24

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

### `org.gms.net.server.guild.GuildPackets`
- 声明: `public class GuildPackets {`
- 方法数（启发式提取）: 43

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

### `org.gms.net.server.guild.GuildResponse`
- 声明: `public enum GuildResponse {`
- 方法数（启发式提取）: 1

```text
public final Packet getPacket(String targetName)
```

### `org.gms.net.server.guild.GuildSummary`
- 声明: `public class GuildSummary {`
- 方法数（启发式提取）: 7

```text
public GuildSummary(Guild g)
public String getName()
public short getLogoBG()
public byte getLogoBGColor()
public short getLogo()
public byte getLogoColor()
public int getAllianceId()
```

## `org.gms.net.server.handlers`

### `org.gms.net.server.handlers.CustomPacketHandler`
- 声明: `public class CustomPacketHandler implements PacketHandler {`
- 方法数（启发式提取）: 2

```text
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

### `org.gms.net.server.handlers.KeepAliveHandler`
- 声明: `public class KeepAliveHandler implements PacketHandler {`
- 方法数（启发式提取）: 2

```text
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

### `org.gms.net.server.handlers.LoginRequiringNoOpHandler`
- 声明: `public final class LoginRequiringNoOpHandler implements PacketHandler {`
- 方法数（启发式提取）: 3

```text
public static LoginRequiringNoOpHandler getInstance()
public void handlePacket(InPacket p, Client c)
public boolean validateState(Client c)
```

## `org.gms.net.server.handlers.login`

### `org.gms.net.server.handlers.login.AcceptToSHandler`
- 声明: `public final class AcceptToSHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.AfterLoginHandler`
- 声明: `public final class AfterLoginHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.CharSelectedHandler`
- 声明: `public final class CharSelectedHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.CharSelectedWithPicHandler`
- 声明: `public class CharSelectedWithPicHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.CharlistRequestHandler`
- 声明: `public final class CharlistRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.CheckCharNameHandler`
- 声明: `public final class CheckCharNameHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.CreateCharHandler`
- 声明: `public final class CreateCharHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.DeleteCharHandler`
- 声明: `public final class DeleteCharHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.GuestLoginHandler`
- 声明: `public final class GuestLoginHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.LoginPasswordHandler`
- 声明: `public final class LoginPasswordHandler implements PacketHandler {`
- 方法数（启发式提取）: 2

```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.RegisterPicHandler`
- 声明: `public final class RegisterPicHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.RegisterPinHandler`
- 声明: `public final class RegisterPinHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.RelogRequestHandler`
- 声明: `public final class RelogRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 2

```text
public boolean validateState(Client c)
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ServerStatusRequestHandler`
- 声明: `public final class ServerStatusRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ServerlistRequestHandler`
- 声明: `public final class ServerlistRequestHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.SetGenderHandler`
- 声明: `public class SetGenderHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ViewAllCharHandler`
- 声明: `public final class ViewAllCharHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ViewAllCharRegisterPicHandler`
- 声明: `public final class ViewAllCharRegisterPicHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ViewAllCharSelectedHandler`
- 声明: `public final class ViewAllCharSelectedHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public final void handlePacket(InPacket p, Client c)
```

### `org.gms.net.server.handlers.login.ViewAllCharSelectedWithPicHandler`
- 声明: `public class ViewAllCharSelectedWithPicHandler extends AbstractPacketHandler {`
- 方法数（启发式提取）: 1

```text
public void handlePacket(InPacket p, Client c)
```

## `org.gms.net.server.services`

### `org.gms.net.server.services.BaseScheduler`
- 声明: `public abstract class BaseScheduler {`
- 方法数（启发式提取）: 1

```text
public void dispose()
```

### `org.gms.net.server.services.BaseService`
- 声明: `public abstract class BaseService {`
- 方法数（启发式提取）: 1

```text
public abstract void dispose()
```

### `org.gms.net.server.services.SchedulerListener`
- 声明: `public interface SchedulerListener {`
- 方法数（启发式提取）: 0

### `org.gms.net.server.services.Service`
- 声明: `public class Service<T extends BaseService> {`
- 方法数（启发式提取）: 3

```text
public Service(Class<T> s)
public T getService()
public void dispose()
```

### `org.gms.net.server.services.ServiceType`
- 声明: `public interface ServiceType<T extends Enum<?>> {`
- 方法数（启发式提取）: 0

### `org.gms.net.server.services.ServicesManager`
- 声明: `public class ServicesManager {`
- 方法数（启发式提取）: 3

```text
public ServicesManager(ServiceType serviceBundle)
public Service getAccess(ServiceType s)
public void shutdown()
```

## `org.gms.net.server.services.task.channel`

### `org.gms.net.server.services.task.channel.EventService`
- 声明: `public class EventService extends BaseService {`
- 方法数（启发式提取）: 4

```text
public EventService()
public void dispose()
public void registerEventAction(int mapid, Runnable runAction, long delay)
public void registerDelayedAction(Runnable runAction, long delay)
```

### `org.gms.net.server.services.task.channel.MobAnimationService`
- 声明: `public class MobAnimationService extends BaseService {`
- 方法数（启发式提取）: 6

```text
public MobAnimationService()
public void dispose()
public boolean registerMobOnAnimationEffect(int mapid, int mobHash, long delay)
public MobAnimationScheduler()
public boolean registerAnimationMode(Integer mobHash, long animationTime)
public void dispose()
```

### `org.gms.net.server.services.task.channel.MobClearSkillService`
- 声明: `public class MobClearSkillService extends BaseService {`
- 方法数（启发式提取）: 4

```text
public MobClearSkillService()
public void dispose()
public void registerMobClearSkillAction(int mapid, Runnable runAction, long delay)
public void registerClearSkillAction(Runnable runAction, long delay)
```

### `org.gms.net.server.services.task.channel.MobMistService`
- 声明: `public class MobMistService extends BaseService {`
- 方法数（启发式提取）: 4

```text
public MobMistService()
public void dispose()
public void registerMobMistCancelAction(int mapid, Runnable runAction, long delay)
public void registerMistCancelAction(Runnable runAction, long delay)
```

### `org.gms.net.server.services.task.channel.MobStatusService`
- 声明: `public class MobStatusService extends BaseService {`
- 方法数（启发式提取）: 9

```text
public MobStatusService()
public void dispose()
public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration)
public void registerMobStatus(int mapid, MonsterStatusEffect mse, Runnable cancelAction, long duration, Runnable overtimeAction, int overtimeDelay)
public void interruptMobStatus(int mapid, MonsterStatusEffect mse)
public MobStatusScheduler()
public void registerMobStatus(MonsterStatusEffect mse, Runnable cancelStatus, long duration, Runnable overtimeStatus, int overtimeDelay)
public void interruptMobStatus(MonsterStatusEffect mse)
public void dispose()
```

### `org.gms.net.server.services.task.channel.OverallService`
- 声明: `public class OverallService extends BaseService {   // thanks Alex for suggesting a refactor over the several channel schedulers unnecessarily populating the Channel class`
- 方法数（启发式提取）: 6

```text
public OverallService()
public void dispose()
public void registerOverallAction(int mapid, Runnable runAction, long delay)
public void forceRunOverallAction(int mapid, Runnable runAction)
public void registerDelayedAction(Runnable runAction, long delay)
public void forceRunDelayedAction(Runnable runAction)
```

## `org.gms.net.server.services.task.world`

### `org.gms.net.server.services.task.world.CharacterSaveService`
- 声明: `public class CharacterSaveService extends BaseService {`
- 方法数（启发式提取）: 4

```text
public void dispose()
public void registerSaveCharacter(int characterId, Runnable runAction)
public void registerSaveCharacter(Integer characterId, Runnable runAction)
public void unregisterSaveCharacter(Integer characterId)
```

## `org.gms.net.server.services.type`

### `org.gms.net.server.services.type.ChannelServices`
- 声明: `public enum ChannelServices implements ServiceType {`
- 方法数（启发式提取）: 2

```text
public Service createService()
public ChannelServices[] enumValues()
```

### `org.gms.net.server.services.type.WorldServices`
- 声明: `public enum WorldServices implements ServiceType {`
- 方法数（启发式提取）: 2

```text
public Service createService()
public WorldServices[] enumValues()
```

## `org.gms.net.server.task`

### `org.gms.net.server.task.BaseTask`
- 声明: `public abstract class BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public BaseTask(World world)
```

### `org.gms.net.server.task.BossLogTask`
- 声明: `public class BossLogTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.CharacterAutosaverTask`
- 声明: `public class CharacterAutosaverTask extends BaseTask implements Runnable {  // thanks Alex09 (Alex-0000) for noticing these runnable classes are tasks, "workers" runs them`
- 方法数（启发式提取）: 2

```text
public void run()
public CharacterAutosaverTask(World world)
```

### `org.gms.net.server.task.CharacterDiseaseTask`
- 声明: `public class CharacterDiseaseTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.CharacterHpDecreaseTask`
- 声明: `public class CharacterHpDecreaseTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public CharacterHpDecreaseTask(World world)
```

### `org.gms.net.server.task.CouponTask`
- 声明: `public class CouponTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.DueyFredrickTask`
- 声明: `public class DueyFredrickTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public DueyFredrickTask(FredrickProcessor fredrickProcessor)
public void run()
```

### `org.gms.net.server.task.EventRecallCoordinatorTask`
- 声明: `public class EventRecallCoordinatorTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.ExtendValueTask`
- 声明: `public class ExtendValueTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.FamilyDailyResetTask`
- 声明: `public class FamilyDailyResetTask implements Runnable {`
- 方法数（启发式提取）: 3

```text
public FamilyDailyResetTask(World world)
public void run()
public static void resetEntitlementUsage(World world)
```

### `org.gms.net.server.task.FishingTask`
- 声明: `public class FishingTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public FishingTask(World world)
```

### `org.gms.net.server.task.HiredMerchantTask`
- 声明: `public class HiredMerchantTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public HiredMerchantTask(World world)
```

### `org.gms.net.server.task.InvitationTask`
- 声明: `public class InvitationTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.LoginCoordinatorTask`
- 声明: `public class LoginCoordinatorTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.LoginStorageTask`
- 声明: `public class LoginStorageTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.MapOwnershipTask`
- 声明: `public class MapOwnershipTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public MapOwnershipTask(World world)
```

### `org.gms.net.server.task.MountTirednessTask`
- 声明: `public class MountTirednessTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public MountTirednessTask(World world)
```

### `org.gms.net.server.task.OnlineTimeTask`
- 声明: `public class OnlineTimeTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.PartySearchTask`
- 声明: `public class PartySearchTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public PartySearchTask(World world)
```

### `org.gms.net.server.task.PetFullnessTask`
- 声明: `public class PetFullnessTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public PetFullnessTask(World world)
```

### `org.gms.net.server.task.RankingCommandTask`
- 声明: `public class RankingCommandTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.RankingLoginTask`
- 声明: `public class RankingLoginTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.RespawnTask`
- 声明: `public class RespawnTask implements Runnable {`
- 方法数（启发式提取）: 1

```text
public void run()
```

### `org.gms.net.server.task.ServerMessageTask`
- 声明: `public class ServerMessageTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public ServerMessageTask(World world)
```

### `org.gms.net.server.task.TimedMapObjectTask`
- 声明: `public class TimedMapObjectTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public TimedMapObjectTask(World world)
```

### `org.gms.net.server.task.TimeoutTask`
- 声明: `public class TimeoutTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public TimeoutTask(World world)
```

### `org.gms.net.server.task.WeddingReservationTask`
- 声明: `public class WeddingReservationTask extends BaseTask implements Runnable {`
- 方法数（启发式提取）: 2

```text
public void run()
public WeddingReservationTask(World world)
```

## `org.gms.net.server.world`

### `org.gms.net.server.world.Messenger`
- 声明: `public final class Messenger {`
- 方法数（启发式提取）: 7

```text
public Messenger(int id, MessengerCharacter chrfor)
public int getId()
public Collection<MessengerCharacter> getMembers()
public void addMember(MessengerCharacter member, int position)
public void removeMember(MessengerCharacter member)
public int getLowestPosition()
public int getPositionByName(String name)
```

### `org.gms.net.server.world.MessengerCharacter`
- 声明: `public class MessengerCharacter {`
- 方法数（启发式提取）: 9

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

### `org.gms.net.server.world.Party`
- 声明: `public class Party {`
- 方法数（启发式提取）: 26

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
public Map<Integer, Door> getDoors()
public void assignNewLeader(Client c)
public int hashCode()
public PartyCharacter getMemberByPos(int pos)
public boolean equals(Object obj)
public static boolean createParty(Character player, boolean silentCheck)
public static boolean joinParty(Character player, int partyid, boolean silentCheck)
public static void leaveParty(Party party, Client c)
public static void expelFromParty(Party party, Client c, int expelCid)
```

### `org.gms.net.server.world.PartyCharacter`
- 声明: `public class PartyCharacter {`
- 方法数（启发式提取）: 19

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

### `org.gms.net.server.world.PartyOperation`
- 声明: `public enum PartyOperation {`
- 方法数（启发式提取）: 0

### `org.gms.net.server.world.World`
- 声明: `public class World {`
- 方法数（启发式提取）: 131

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
public Pair<Boolean, Boolean> getMarriageQueuedLocation(int marriageId)
public Pair<Integer, Integer> getMarriageQueuedCouple(int marriageId)
public void putMarriageQueued(int marriageId, boolean cathedral, boolean premium, int groomId, int brideId)
public Pair<Boolean, Set<Integer>> removeMarriageQueued(int marriageId)
public boolean addMarriageGuest(int marriageId, int playerId)
public Pair<Integer, Integer> getWeddingCoupleForGuest(int guestId, Boolean cathedral)
public void debugMarriageStatus()
public Integer getCharacterPartyid(Integer chrid)
public Party createParty(PartyCharacter chrfor)
public Party getParty(int partyid)
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
public void addOwlItemSearch(Integer itemid)
public List<Pair<Integer, Integer>> getOwlSearchedItems()
public void addCashItemBought(Integer snid)
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
public int getPlayerNpcMapStep(int mapid)
public int getPlayerNpcMapPodiumData(int mapid)
public void resetPlayerNpcMapData()
public void setServerMessage(String msg)
public void broadcastPacket(Packet packet)
public List<Pair<PlayerShopItem, AbstractMapObject>> getAvailableItemBundles(int itemid)
public Pair<Integer, Integer> getRelationshipCouple(int relationshipId)
public int getRelationshipId(int playerId)
public int createRelationship(int groomId, int brideId)
public void deleteRelationship(int playerId, int partnerId)
public void dropMessage(int type, String message)
public boolean registerFisherPlayer(Character chr, int baitLevel)
public int unregisterFisherPlayer(Character chr)
public void runCheckFishingSchedule()
public void runPartySearchUpdateSchedule()
public BaseService getServiceAccess(WorldServices sv)
public final void shutdown()
```

## `org.gms.property`

### `org.gms.property.ServiceProperty`
- 声明: `public class ServiceProperty {`
- 方法数（启发式提取）: 0

## `org.gms.provider`

### `org.gms.provider.Data`
- 声明: `public interface Data extends DataEntity, Iterable<Data> {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataDirectoryEntry`
- 声明: `public interface DataDirectoryEntry extends DataEntry {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataEntity`
- 声明: `public interface DataEntity {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataEntry`
- 声明: `public interface DataEntry extends DataEntity {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataFileEntry`
- 声明: `public interface DataFileEntry extends DataEntry {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataProvider`
- 声明: `public interface DataProvider {`
- 方法数（启发式提取）: 0

### `org.gms.provider.DataProviderFactory`
- 声明: `public class DataProviderFactory {`
- 方法数（启发式提取）: 1

```text
public static DataProvider getDataProvider(WZFiles in)
```

### `org.gms.provider.DataTool`
- 声明: `public class DataTool {`
- 方法数（启发式提取）: 27

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

## `org.gms.provider.wz`

### `org.gms.provider.wz.DataType`
- 声明: `public enum DataType {`
- 方法数（启发式提取）: 0

### `org.gms.provider.wz.WZDirectoryEntry`
- 声明: `public class WZDirectoryEntry extends WZEntry implements DataDirectoryEntry {`
- 方法数（启发式提取）: 7

```text
public WZDirectoryEntry(String name, int size, int checksum, DataEntity parent)
public WZDirectoryEntry()
public void addDirectory(DataDirectoryEntry dir)
public void addFile(DataFileEntry fileEntry)
public List<DataDirectoryEntry> getSubdirectories()
public List<DataFileEntry> getFiles()
public DataEntry getEntry(String name)
```

### `org.gms.provider.wz.WZEntry`
- 声明: `public class WZEntry implements DataEntry {`
- 方法数（启发式提取）: 6

```text
public WZEntry(String name, int size, int checksum, DataEntity parent)
public String getName()
public int getSize()
public int getChecksum()
public int getOffset()
public DataEntity getParent()
```

### `org.gms.provider.wz.WZFileEntry`
- 声明: `public class WZFileEntry extends WZEntry implements DataFileEntry {`
- 方法数（启发式提取）: 3

```text
public WZFileEntry(String name, int size, int checksum, DataEntity parent)
public int getOffset()
public void setOffset(int offset)
```

### `org.gms.provider.wz.WZFiles`
- 声明: `public enum WZFiles {`
- 方法数（启发式提取）: 2

```text
public Path getFile()
public String getFilePath()
```

### `org.gms.provider.wz.XMLDomMapleData`
- 声明: `public class XMLDomMapleData implements Data {`
- 方法数（启发式提取）: 9

```text
public XMLDomMapleData(FileInputStream fis, Path imageDataDir)
public synchronized Data getChildByPath(String path)
public synchronized List<Data> getChildren()
public synchronized Object getData()
public synchronized DataType getType()
public synchronized DataEntity getParent()
public synchronized String getName()
public synchronized Iterator<Data> iterator()
public synchronized String getAttributeValue(String name)
```

### `org.gms.provider.wz.XMLWZFile`
- 声明: `public class XMLWZFile implements DataProvider {`
- 方法数（启发式提取）: 3

```text
public XMLWZFile(Path fileIn)
public synchronized Data getData(String path)
public DataDirectoryEntry getRoot()
```

## `org.gms.scripting`

### `org.gms.scripting.AbstractPlayerInteraction`
- 声明: `public class AbstractPlayerInteraction {`
- 方法数（启发式提取）: 171

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
public boolean canHoldAll(List<Object> itemids)
public boolean canHoldAll(List<Object> itemids, List<Object> quantity)
public boolean canHoldAllAfterRemoving(List<Integer> toAddItemids, List<Integer> toAddQuantity, List<Integer> toRemoveItemids, List<Integer> toRemoveQuantity)
public final QuestStatus getQuestRecord(final int id)
public final QuestStatus getQuestNoRecord(final int id)
public void openNpc(int npcid)
public void openNpc(int npcid, String script)
public int getQuestStatus(int id)
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

### `org.gms.scripting.AbstractScriptManager`
- 声明: `public abstract class AbstractScriptManager {`
- 方法数（启发式提取）: 0

### `org.gms.scripting.SynchronizedInvocable`
- 声明: `public class SynchronizedInvocable implements Invocable {`
- 方法数（启发式提取）: 5

```text
public static Invocable of(Invocable invocable)
public synchronized Object invokeMethod(Object thiz, String name, Object... args) throws ScriptException, NoSuchMethodException
public synchronized Object invokeFunction(String name, Object... args) throws ScriptException, NoSuchMethodException
public synchronized <T> T getInterface(Class<T> clasz)
public synchronized <T> T getInterface(Object thiz, Class<T> clasz)
```

## `org.gms.scripting.event`

### `org.gms.scripting.event.EventInstanceManager`
- 声明: `public class EventInstanceManager {`
- 方法数（启发式提取）: 116

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
public void stopEventTimer()
public boolean isTimerStarted()
public long getTimeLeft()
public void registerParty(Character chr)
public void registerParty(Party party, MapleMap map)
public void registerExpedition(Expedition exped)
public void unregisterPlayer(final Character chr)
public int getPlayerCount()
public Character getPlayerById(int id)
public List<Character> getPlayers()
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
public void setEventClearStageExp(List<Object> gain)
public void setEventClearStageMeso(List<Object> gain)
public Integer getClearStageExp(int stage)
public Integer getClearStageMeso(int stage)
public List<Integer> getClearStageBonus(int stage)
public void dropAllExclusiveItems()
public final void setExclusiveItems(List<Object> items)
public final void setEventRewards(List<Object> rwds, List<Object> qtys, int expGiven)
public final void setEventRewards(List<Object> rwds, List<Object> qtys)
public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys)
public final void setEventRewards(int eventLevel, List<Object> rwds, List<Object> qtys, int expGiven)
public final boolean giveEventReward(Character player)
public final boolean giveEventReward(Character player, int eventLevel)
public final synchronized void startEvent()
public final void setEventCleared()
public final boolean isEventCleared()
public final boolean isEventDisposed()
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

### `org.gms.scripting.event.EventManager`
- 声明: `public class EventManager {`
- 方法数（启发式提取）: 51

```text
public EventManager(Channel cserv, Invocable iv, String name)
public void cancel()
public long getLobbyDelay()
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
public String getName()
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
public boolean isQueueFull()
public int getQueueSize()
public byte addGuildToQueue(Integer guildId, Integer leaderId)
public boolean attemptStartGuildInstance()
public void startQuest(Character chr, int id, int npcid)
public void completeQuest(Character chr, int id, int npcid)
public int getTransportationTime(int travelTime)
public int getBossTime(int BossTime)
public void run()
```

### `org.gms.scripting.event.EventScheduledFuture`
- 声明: `public class EventScheduledFuture {`
- 方法数（启发式提取）: 2

```text
public EventScheduledFuture(Runnable r, EventScriptScheduler ess)
public void cancel(boolean dummy)
```

### `org.gms.scripting.event.EventScriptManager`
- 声明: `public class EventScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 8

```text
public EventEntry(Invocable iv, EventManager em)
public EventScriptManager(final Channel channel, String[] scripts)
public EventManager getEventManager(String event)
public boolean isActive()
public final void init()
public void reload()
public void cancel()
public void dispose()
```

## `org.gms.scripting.event.scheduler`

### `org.gms.scripting.event.scheduler.EventScriptScheduler`
- 声明: `public class EventScriptScheduler {`
- 方法数（启发式提取）: 3

```text
public void registerEntry(final Runnable scheduledAction, final long duration)
public void cancelEntry(final Runnable scheduledAction)
public void dispose()
```

## `org.gms.scripting.item`

### `org.gms.scripting.item.ItemScriptManager`
- 声明: `public class ItemScriptManager {`
- 方法数（启发式提取）: 2

```text
public static ItemScriptManager getInstance()
public void runItemScript(Client c, ScriptedItem scriptItem)
```

### `org.gms.scripting.item.ItemScriptMethods`
- 声明: `public class ItemScriptMethods extends AbstractPlayerInteraction {`
- 方法数（启发式提取）: 1

```text
public ItemScriptMethods(Client c)
```

## `org.gms.scripting.map`

### `org.gms.scripting.map.MapScriptManager`
- 声明: `public class MapScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 3

```text
public static MapScriptManager getInstance()
public void reloadScripts()
public boolean runMapScript(Client c, String mapScriptPath, boolean firstUser)
```

### `org.gms.scripting.map.MapScriptMethods`
- 声明: `public class MapScriptMethods extends AbstractPlayerInteraction {`
- 方法数（启发式提取）: 8

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

## `org.gms.scripting.npc`

### `org.gms.scripting.npc.NPCConversationManager`
- 声明: `public class NPCConversationManager extends AbstractPlayerInteraction {`
- 方法数（启发式提取）: 128

```text
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
public void startCPQ(final Character challenger, final int field)
public void startCPQ2(final Character challenger, final int field)
public boolean sendCPQMapLists2()
public boolean fieldTaken2(int field)
public boolean fieldLobbied2(int field)
public void cpqLobby2(int field)
public void mapClock(int time)
public void answerCPQChallenge(boolean accept)
public void challengeParty2(int field)
public void challengeParty(int field)
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

### `org.gms.scripting.npc.NPCScriptManager`
- 声明: `public class NPCScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 14

```text
public static NPCScriptManager getInstance()
public boolean isNpcScriptAvailable(Client c, String fileName)
public boolean start(Client c, int npc, Character chr)
public boolean start(Client c, int npc, int oid, Character chr)
public boolean start(Client c, int npc, String fileName, Character chr)
public boolean start(Client c, int npc, int oid, String fileName, Character chr)
public boolean start(Client c, ScriptedItem scriptItem, Character chr)
public void start(String filename, Client c, int npc, List<PartyCharacter> chrs)
public void action(Client c, byte mode, byte type, int selection)
public void nextLevel(Client c, byte mode, byte type, int selection)
public void dispose(NPCConversationManager cm)
public void dispose(Client c)
public void dispose(Client c, boolean action)
public NPCConversationManager getCM(Client c)
```

## `org.gms.scripting.portal`

### `org.gms.scripting.portal.PortalPlayerInteraction`
- 声明: `public class PortalPlayerInteraction extends AbstractPlayerInteraction {`
- 方法数（启发式提取）: 7

```text
public PortalPlayerInteraction(Client c, Portal portal)
public Portal getPortal()
public void runMapScript()
public boolean hasLevel30Character()
public void blockPortal()
public void unblockPortal()
public void playPortalSound()
```

### `org.gms.scripting.portal.PortalScript`
- 声明: `public interface PortalScript {`
- 方法数（启发式提取）: 0

### `org.gms.scripting.portal.PortalScriptManager`
- 声明: `public class PortalScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 3

```text
public static PortalScriptManager getInstance()
public boolean executePortalScript(Portal portal, Client c)
public void reloadPortalScripts()
```

## `org.gms.scripting.quest`

### `org.gms.scripting.quest.QuestActionManager`
- 声明: `public class QuestActionManager extends NPCConversationManager {`
- 方法数（启发式提取）: 11

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

### `org.gms.scripting.quest.QuestScriptManager`
- 声明: `public class QuestScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 11

```text
public static QuestScriptManager getInstance()
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

## `org.gms.scripting.reactor`

### `org.gms.scripting.reactor.ReactorActionManager`
- 声明: `public class ReactorActionManager extends AbstractPlayerInteraction {`
- 方法数（启发式提取）: 26

```text
public ReactorActionManager(Client c, Reactor reactor, Invocable iv)
public void hitReactor()
public void destroyNpc(int npcId)
public void sprayItems()
public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso)
public void sprayItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void sprayItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems()
public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso)
public void dropItems(boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems(int posX, int posY, boolean meso, int mesoChance, int minMeso, int maxMeso, int minItems)
public void dropItems(boolean delayed, int posX, int posY, boolean meso, int mesoChance, final int minMeso, final int maxMeso, int minItems)
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
public void dispelAllMonsters(int num, int team)
```

### `org.gms.scripting.reactor.ReactorScriptManager`
- 声明: `public class ReactorScriptManager extends AbstractScriptManager {`
- 方法数（启发式提取）: 7

```text
public static ReactorScriptManager getInstance()
public void onHit(Client c, Reactor reactor)
public void act(Client c, Reactor reactor)
public List<ReactorDropEntry> getDrops(int reactorId)
public void clearDrops()
public void touch(Client c, Reactor reactor)
public void untouch(Client c, Reactor reactor)
```

## `org.gms.server`

### `org.gms.server.CashShop`
- 声明: `public class CashShop {`
- 方法数（启发式提取）: 33

```text
public CashShop(int accountId, int characterId, int jobType)
public static void loadAllCashItems()
public static void loadAllModifiedCashItems()
public static Optional<ModifiedCashItemDO> getRandomCashItem()
public static ModifiedCashItemDO getItem(int sn)
public static ModifiedCashItemDO getWzItem(int sn)
public static List<Item> getPackage(int itemId)
public static boolean isPackage(int itemId)
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
public List<Pair<Item, String>> loadGifts()
public int getAvailableNotes()
public void decreaseNotes()
public void save(Connection con) throws SQLException
public Optional<CashShopSurpriseResult> openCashShopSurprise(long cashId)
public int getItemsSize()
public static Item generateCouponItem(int itemId, short quantity)
```

### `org.gms.server.ChatLogger`
- 声明: `public class ChatLogger {`
- 方法数（启发式提取）: 1

```text
public static void log(Client c, String chatType, String message)
```

### `org.gms.server.CommonInformation`
- 声明: `public class CommonInformation {`
- 方法数（启发式提取）: 2

```text
public static CommonInformation getInstance()
public List<InformationResult> getStringInformation(InformationSearch condition)
```

### `org.gms.server.DueyPackage`
- 声明: `public class DueyPackage {`
- 方法数（启发式提取）: 15

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

### `org.gms.server.ExpLogger`
- 声明: `public class ExpLogger {`
- 方法数（启发式提取）: 2

```text
public record ExpLogRecord(float worldExpRate, int expCoupon, long gainedExp, int currentExp,Timestamp expGainTime, int charid)
public static void putExpLogRecord(ExpLogRecord expLogRecord)
```

### `org.gms.server.ItemInformationProvider`
- 声明: `public class ItemInformationProvider {`
- 方法数（启发式提取）: 79

```text
public static ItemInformationProvider getInstance()
public List<Pair<Integer, String>> getAllItems()
public List<Pair<Integer, String>> getAllEtcItems()
public boolean noCancelMouse(int itemId)
public List<Integer> getItemIdsInRange(int minId, int maxId, boolean ignoreCashItem)
public short getSlotMax(Client c, int itemId)
public int getMeso(int itemId)
public int getWholePrice(int itemId)
public double getUnitPrice(int itemId)
public int getPrice(int itemId, int quantity)
public Pair<Integer, String> getReplaceOnExpire(int itemId)
public Map<String, Integer> getEquipStats(int itemId)
public Integer getEquipLevelReq(int itemId)
public List<Integer> getScrollReqs(int itemId)
public WeaponType getWeaponType(int itemId)
public static boolean rollSuccessChance(double propPercent)
public void scrollOptionEquipWithChaos(Equip nEquip, int range, boolean option)
public boolean canUseCleanSlate(Equip equip)
public Item scrollEquipWithId(Item equip, int scrollId, boolean usingWhiteScroll, int vegaItemId, boolean isGM)
public static void improveEquipStats(Equip nEquip, Map<String, Integer> stats)
public Item getEquipById(int equipId)
public Equip randomizeStats(Equip equip)
public Equip randomizeUpgradeStats(Equip equip)
public StatEffect getItemEffect(int itemId)
public int[][] getSummonMobs(int itemId)
public int getWatkForProjectile(int itemId)
public String getName(int itemId)
public Pair<String, String> getNameDesc(int itemId)
public String getMsg(int itemId)
public boolean isUntradeableRestricted(int itemId)
public boolean isAccountRestricted(int itemId)
public boolean isLootRestricted(int itemId)
public boolean isDropRestricted(int itemId)
public boolean isPickupRestricted(int itemId)
public Map<String, Integer> getSkillStats(int itemId, double playerJob)
public Pair<Integer, Boolean> canPetConsume(Integer petId, Integer itemId)
public boolean isQuestItem(int itemId)
public boolean isPartyQuestItem(int itemId)
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
public Pair<Integer, List<RewardItem>> getItemReward(int itemId)
public boolean isConsumeOnPickup(int itemId)
public final boolean isTwoHanded(int itemId)
public boolean isCash(int itemId)
public boolean isUpgradeable(int itemId)
public boolean isUnmerchable(int itemId)
public Collection<Item> canWearEquipment(Character chr, Collection<Item> items)
public boolean canWearEquipment(Character chr, Equip equip, int dst)
public ArrayList<Pair<Integer, String>> getItemDataByName(String name)
public int getEquipLevel(int itemId, boolean getMaxLevel)
public List<Pair<String, Integer>> getItemLevelupStats(int itemId, int level)
public Pair<String, Integer> getMakerReagentStatUpgrade(int itemId)
public int getMakerCrystalFromLeftover(Integer leftoverId)
public MakerItemCreateEntry getMakerItemEntry(int toCreate)
public int getMakerCrystalFromEquip(Integer equipId)
public int getMakerStimulantFromEquip(Integer equipId)
public List<Pair<Integer, Integer>> getMakerDisassembledItems(Integer itemId)
public int getMakerDisassembledFee(Integer itemId)
public int getMakerStimulant(int itemId)
public Set<String> getWhoDrops(Integer itemId)
public List<Integer> usableMasteryBooks(Character player)
public List<Integer> usableSkillBooks(Character player)
public final QuestConsItem getQuestConsumablesInfo(final int itemId)
public final ItemCashInfo getItemCashInfo(int itemId)
public ScriptedItem(int npc, String script, boolean rop)
public int getNpc()
public String getScript()
public boolean runOnPickup()
public Integer getItemRequirement(int itemid)
public static ArrayList<Pair<Integer, String>> getItemsIDsFromName(String search)
```

### `org.gms.server.MTSItemInfo`
- 声明: `public class MTSItemInfo {`
- 方法数（启发式提取）: 7

```text
public MTSItemInfo(Item item, int price, int id, int cid, String seller, String date)
public Item getItem()
public int getPrice()
public int getTaxes()
public int getID()
public long getEndingDate()
public String getSeller()
```

### `org.gms.server.MakerItemFactory`
- 声明: `public class MakerItemFactory {`
- 方法数（启发式提取）: 13

```text
public static MakerItemCreateEntry getItemCreateEntry(int toCreate, int stimulantid, Map<Integer, Short> reagentids)
public static MakerItemCreateEntry generateLeftoverCrystalEntry(int fromLeftoverid, int crystalId)
public static MakerItemCreateEntry generateDisassemblyCrystalEntry(int fromEquipid, int cost, List<Pair<Integer, Integer>> gains)
public MakerItemCreateEntry(int cost, int reqLevel, int reqMakerLevel)
public MakerItemCreateEntry(MakerItemCreateEntry mi)
public List<Pair<Integer, Integer>> getReqItems()
public List<Pair<Integer, Integer>> getGainItems()
public int getReqLevel()
public int getReqSkillLevel()
public int getCost()
public void addCost(double amount)
public void trimCost()
public boolean isInvalid()
```

### `org.gms.server.MapleLeafLogger`
- 声明: `public class MapleLeafLogger {`
- 方法数（启发式提取）: 1

```text
public static void log(Character player, boolean gotPrize, String operation)
```

### `org.gms.server.Marriage`
- 声明: `public class Marriage extends EventInstanceManager {`
- 方法数（启发式提取）: 13

```text
public Marriage(EventManager em, String name)
public boolean giftItemToSpouse(int cid)
public List<String> getWishlistItems(boolean groom)
public void initializeGiftItems()
public List<Item> getGiftItems(Client c, boolean groom)
public Item getGiftItem(Client c, boolean groom, int idx)
public void addGiftItem(boolean groom, Item item)
public void removeGiftItem(boolean groom, Item item)
public Boolean isMarriageGroom(Character chr)
public static boolean claimGiftItems(Client c, Character chr)
public static List<Item> loadGiftItemsFromDb(Client c, int cid)
public void saveGiftItemsToDb(Client c, boolean groom, int cid)
public static void saveGiftItemsToDb(Client c, List<Item> giftItems, int cid)
```

### `org.gms.server.Shop`
- 声明: `public class Shop {`
- 方法数（启发式提取）: 7

```text
public void sendShop(Client c)
public void buy(Client c, short slot, int itemId, short quantity)
public void sell(Client c, InventoryType type, short slot, short quantity)
public void recharge(Client c, short slot)
public static Shop createFromDB(int id, boolean isShopId)
public int getNpcId()
public int getId()
```

### `org.gms.server.ShopFactory`
- 声明: `public class ShopFactory {`
- 方法数（启发式提取）: 4

```text
public static ShopFactory getInstance()
public Shop getShop(int shopId)
public Shop getShopForNPC(int npcId)
public void reloadShops()
```

### `org.gms.server.ShopItem`
- 声明: `public class ShopItem {`
- 方法数（启发式提取）: 5

```text
public ShopItem(short buyable, int itemId, int price, int pitch)
public short getBuyable()
public int getItemId()
public int getPrice()
public int getPitch()
```

### `org.gms.server.SkillbookInformationProvider`
- 声明: `public class SkillbookInformationProvider {`
- 方法数（启发式提取）: 3

```text
public static void loadAllSkillbookInformation()
public static SkillBookEntry getSkillbookAvailability(int itemId)
public static List<Integer> getTeachableSkills(Character chr)
```

### `org.gms.server.StatEffect`
- 声明: `public class StatEffect {`
- 方法数（启发式提取）: 63

```text
public boolean isActive(Character applyto)
public int getCardRate(int mapid, int itemid)
public static StatEffect loadSkillEffectFromData(Data source, int skillid, boolean overtime)
public static StatEffect loadItemEffectFromData(Data source, int itemid)
public void applyPassive(Character applyto, MapObject obj, int attack)
public boolean applyEchoOfHero(Character applyfrom)
public boolean applyTo(Character chr)
public boolean applyTo(Character chr, boolean useMaxRange)
public boolean applyTo(Character chr, Point pos)
public boolean hasBoundingBox()
public Rectangle calculateBoundingBox(Point posFrom, boolean facingLeft)
public int getBuffLocalDuration()
public void silentApplyBuff(Character chr, long localStartTime)
public final void applyComboBuff(final Character applyto, int combo)
public final void applyBeaconBuff(final Character applyto, int objectid)
public void updateBuffEffect(Character target, List<Pair<BuffStat, Integer>> activeStats, long starttime)
public boolean isDragonBlood()
public boolean isBerserk()
public boolean isRecovery()
public boolean isMapChair()
public static boolean isMapChair(int sourceid)
public static boolean isHpMpRecovery(int sourceid)
public static boolean isAriantShield(int sourceid)
public boolean isBeholder()
public boolean isMonsterRiding()
public boolean isMagicDoor()
public boolean isPoison()
public boolean isMorph()
public boolean isMorphWithoutAttack()
public static boolean isHerosWill(int skillid)
public boolean isSkill()
public int getSourceId()
public void setSourceId(int id)
public int getBuffSourceId()
public boolean makeChanceResult()
public CancelEffectAction(Character target, StatEffect effect, long startTime)
public void run()
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
public List<Pair<BuffStat, Integer>> getStatups()
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
public Map<MonsterStatus, Integer> getMonsterStati()
```

### `org.gms.server.Storage`
- 声明: `public class Storage {`
- 方法数（启发式提取）: 21

```text
public static Storage loadOrCreateFromDB(int id, int world)
public byte getSlots()
public boolean canGainSlots(int slots)
public boolean gainSlots(int slots)
public void saveToDB(Connection con)
public Item getItem(byte slot)
public boolean takeOut(Item item)
public boolean store(Item item)
public List<Item> getItems()
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

### `org.gms.server.StorageInventory`
- 声明: `public class StorageInventory {`
- 方法数（启发式提取）: 4

```text
public StorageInventory(Client c, List<Item> toSort)
public void mergeItems()
public List<Item> sortItems()
public PairedQuicksort(ArrayList<Item> A, int primarySort, int secondarySort)
```

### `org.gms.server.SystemRescue`
- 声明: `public class SystemRescue {`
- 方法数（启发式提取）: 2

```text
public void setMapChange(Character player)
public void showMapChangeMessage(Character player)
```

### `org.gms.server.ThreadManager`
- 声明: `public class ThreadManager {`
- 方法数（启发式提取）: 3

```text
public void newTask(Runnable r)
public void start()
public void stop()
```

### `org.gms.server.TimerManager`
- 声明: `public class TimerManager implements TimerManagerMBean {`
- 方法数（启发式提取）: 18

```text
public void start()
public Thread newThread(Runnable r)
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
public TimerRunner(Runnable r)
public void run()
```

### `org.gms.server.TimerManagerMBean`
- 声明: `public interface TimerManagerMBean {`
- 方法数（启发式提取）: 0

### `org.gms.server.Trade`
- 声明: `public class Trade {`
- 方法数（启发式提取）: 18

```text
public Trade(byte number, Character chr)
public static int getFee(long meso)
public void setMeso(int meso)
public boolean addItem(Item item)
public void chat(String message)
public Trade getPartner()
public void setPartner(Trade partner)
public Character getChr()
public List<Item> getItems()
public int getExchangeMesos()
public static void completeTrade(Character chr)
public static void cancelTrade(Character chr, TradeResult result)
public static void startTrade(Character chr)
public static void inviteTrade(Character c1, Character c2)
public static void visitTrade(Character c1, Character c2)
public static void declineTrade(Character chr)
public boolean isFullTrade()
public void setFullTrade(boolean fullTrade)
```

## `org.gms.server.events`

### `org.gms.server.events.Events`
- 声明: `public abstract class Events {`
- 方法数（启发式提取）: 2

```text
public Events()
public abstract int getInfo()
```

### `org.gms.server.events.RescueGaga`
- 声明: `public class RescueGaga extends Events {`
- 方法数（启发式提取）: 5

```text
public RescueGaga(int completed)
public int getCompleted()
public void complete()
public int getInfo()
public void giveSkill(Character chr)
```

## `org.gms.server.events.gm`

### `org.gms.server.events.gm.Coconut`
- 声明: `public class Coconut extends Event {`
- 方法数（启发式提取）: 17

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

### `org.gms.server.events.gm.Coconuts`
- 声明: `public class Coconuts {`
- 方法数（启发式提取）: 7

```text
public Coconuts(int id)
public void hit()
public int getHits()
public void resetHits()
public boolean isHittable()
public void setHittable(boolean hittable)
public long getHitTime()
```

### `org.gms.server.events.gm.Event`
- 声明: `public class Event {`
- 方法数（启发式提取）: 5

```text
public Event(int mapid, int limit)
public int getMapId()
public int getLimit()
public void minusLimit()
public void addLimit()
```

### `org.gms.server.events.gm.Fitness`
- 声明: `public class Fitness {`
- 方法数（启发式提取）: 7

```text
public Fitness(final Character chr)
public void startFitness()
public boolean isTimerStarted()
public long getTime()
public void resetTimes()
public long getTimeLeft()
public void checkAndMessage()
```

### `org.gms.server.events.gm.Ola`
- 声明: `public class Ola {`
- 方法数（启发式提取）: 6

```text
public Ola(final Character chr)
public void startOla()
public boolean isTimerStarted()
public long getTime()
public void resetTimes()
public long getTimeLeft()
```

### `org.gms.server.events.gm.OxQuiz`
- 声明: `public final class OxQuiz {`
- 方法数（启发式提取）: 2

```text
public OxQuiz(MapleMap map)
public void sendQuestion()
```

### `org.gms.server.events.gm.Snowball`
- 声明: `public class Snowball {`
- 方法数（启发式提取）: 10

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

## `org.gms.server.expeditions`

### `org.gms.server.expeditions.Expedition`
- 声明: `public class Expedition {`
- 方法数（启发式提取）: 34

```text
public Expedition(Character player, ExpeditionType met, boolean sil, int minPlayers, int maxPlayers)
public int getMinSize()
public int getMaxSize()
public void beginRegistration()
public void dispose(boolean log)
public void finishRegistration()
public void start()
public String addMember(Character player)
public int addMemberInt(Character player)
public boolean removeMember(Character chr)
public void ban(Entry<Integer, String> chr)
public void monsterKilled(Character chr, Monster mob)
public void setProperty(String key, String value)
public String getProperty(String key)
public ExpeditionType getType()
public List<Character> getActiveMembers()
public Map<Integer, String> getMembers()
public List<Entry<Integer, String>> getMemberList()
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

### `org.gms.server.expeditions.ExpeditionBossLog`
- 声明: `public class ExpeditionBossLog {`
- 方法数（启发式提取）: 2

```text
public static void resetBossLogTable()
public static boolean attemptBoss(int cid, int channel, Expedition exped, boolean log)
```

### `org.gms.server.expeditions.ExpeditionType`
- 声明: `public enum ExpeditionType {`
- 方法数（启发式提取）: 5

```text
public int getMinSize()
public int getMaxSize()
public int getMinLevel()
public int getMaxLevel()
public int getRegistrationMinutes()
```

## `org.gms.server.gachapon`

### `org.gms.server.gachapon.ElNath`
- 声明: `public class ElNath extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Ellinia`
- 声明: `public class Ellinia extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Gachapon`
- 声明: `public class Gachapon {`
- 方法数（启发式提取）: 11

```text
public static Gachapon getInstance()
public int[] getItems(int tier)
public int getItem(int tier)
public static GachaponType getByNpcId(int npcId)
public static String[] getLootNames()
public static int[] getLootIds()
public GachaponItem process(int npcId)
public GachaponItem(int t, int i)
public int getTier()
public int getId()
public static void log(Character player, int itemId, String map)
```

### `org.gms.server.gachapon.GachaponItems`
- 声明: `public abstract class GachaponItems {`
- 方法数（启发式提取）: 5

```text
public abstract int[] getCommonItems()
public abstract int[] getUncommonItems()
public abstract int[] getRareItems()
public GachaponItems()
public final int[] getItems(int tier)
```

### `org.gms.server.gachapon.Global`
- 声明: `public class Global extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Henesys`
- 声明: `public class Henesys extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.KerningCity`
- 声明: `public class KerningCity extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Ludibrium`
- 声明: `public class Ludibrium extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.MushroomShrine`
- 声明: `public class MushroomShrine extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.NautilusHarbor`
- 声明: `public class NautilusHarbor extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.NewLeafCity`
- 声明: `public class NewLeafCity extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Perion`
- 声明: `public class Perion extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.ShowaSpaFemale`
- 声明: `public class ShowaSpaFemale extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.ShowaSpaMale`
- 声明: `public class ShowaSpaMale extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

### `org.gms.server.gachapon.Sleepywood`
- 声明: `public class Sleepywood extends GachaponItems {`
- 方法数（启发式提取）: 3

```text
public int[] getCommonItems()
public int[] getUncommonItems()
public int[] getRareItems()
```

## `org.gms.server.life`

### `org.gms.server.life.AbstractLoadedLife`
- 声明: `public abstract class AbstractLoadedLife extends AbstractAnimatedMapObject {`
- 方法数（启发式提取）: 16

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

### `org.gms.server.life.ChangeableStats`
- 声明: `public class ChangeableStats extends OverrideMonsterStats {`
- 方法数（启发式提取）: 3

```text
public ChangeableStats(MonsterStats stats, OverrideMonsterStats ostats)
public ChangeableStats(MonsterStats stats, int newLevel, boolean pqMob)
public ChangeableStats(MonsterStats stats, float statModifier, boolean pqMob)
```

### `org.gms.server.life.Element`
- 声明: `public enum Element {`
- 方法数（启发式提取）: 3

```text
public boolean isSpecial()
public static Element getFromChar(char c)
public int getValue()
```

### `org.gms.server.life.ElementalEffectiveness`
- 声明: `public enum ElementalEffectiveness {`
- 方法数（启发式提取）: 1

```text
public static ElementalEffectiveness getByNumber(int num)
```

### `org.gms.server.life.LifeFactory`
- 声明: `public class LifeFactory {`
- 方法数（启发式提取）: 24

```text
public static AbstractLoadedLife getLife(int id, String type)
public void update(Point lt, Point rb)
public boolean isValid()
public int getMinX()
public int getMinY()
public int getMaxX()
public int getMaxY()
public static Monster getMonster(int mid)
public static int getMonsterLevel(int mid)
public static NPC getNPC(int nid)
public static String getNPCName(int nid)
public static String getNPCDefaultTalk(int nid)
public BanishInfo(String msg, int map, String portal)
public int getMap()
public String getPortal()
public String getMsg()
public loseItem(int id, byte chance, byte x)
public int getId()
public byte getChance()
public byte getX()
public selfDestruction(byte action, int removeAfter, int hp)
public int getHp()
public byte getAction()
public int removeAfter()
```

### `org.gms.server.life.MobAttackInfo`
- 声明: `public class MobAttackInfo {`
- 方法数（启发式提取）: 11

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

### `org.gms.server.life.MobAttackInfoFactory`
- 声明: `public class MobAttackInfoFactory {`
- 方法数（启发式提取）: 1

```text
public static MobAttackInfo getMobAttackInfo(Monster mob, int attack)
```

### `org.gms.server.life.MobSkill`
- 声明: `public class MobSkill {`
- 方法数（启发式提取）: 27

```text
public Builder(MobSkillType type, int level)
public Builder mpCon(int mpCon)
public Builder spawnEffect(int spawnEffect)
public Builder hp(int hp)
public Builder x(int x)
public Builder y(int y)
public Builder count(int count)
public Builder duration(long duration)
public Builder cooltime(long cooltime)
public Builder prop(float prop)
public Builder lt(Point lt)
public Builder rb(Point rb)
public Builder limit(int limit)
public Builder toSummon(List<Integer> toSummon)
public MobSkill build()
public void applyDelayedEffect(final Character player, final Monster monster, final boolean skill, int animationTime)
public void applyEffect(Monster monster)
public void applyEffect(Character player, Monster monster, boolean skill, List<Character> banishPlayersOutput)
public MobSkillId getId()
public MobSkillType getType()
public int getMpCon()
public int getHP()
public int getX()
public int getY()
public long getDuration()
public long getCoolTime()
public boolean makeChanceResult()
```

### `org.gms.server.life.MobSkillFactory`
- 声明: `public class MobSkillFactory {`
- 方法数（启发式提取）: 2

```text
public static MobSkill getMobSkillOrThrow(MobSkillType type, int level)
public static Optional<MobSkill> getMobSkill(final MobSkillType type, final int level)
```

### `org.gms.server.life.MobSkillId`
- 声明: `(未解析) MobSkillId`
- 方法数（启发式提取）: 1

```text
public record MobSkillId(MobSkillType type, int level)
```

### `org.gms.server.life.MobSkillType`
- 声明: `public enum MobSkillType {`
- 方法数（启发式提取）: 2

```text
public static Optional<MobSkillType> from(int id)
public int getId()
```

### `org.gms.server.life.Monster`
- 声明: `public class Monster extends AbstractLoadedLife {`
- 方法数（启发式提取）: 114

```text
public Monster(int id, MonsterStats stats)
public Monster(Monster monster)
public void lockMonster()
public void unlockMonster()
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
public void setHpZero()
public synchronized Integer applyAndGetHpDamage(int delta, boolean stayAlive)
public synchronized void disposeMapObject()
public void broadcastMobHpBar(Character from)
public boolean damage(Character attacker, int damage, boolean stayAlive)
public void applyFakeDamage(Character from, int damage, boolean stayAlive)
public void heal(int hp, int mp)
public boolean isAttackedBy(Character chr)
public List<MonsterDropEntry> retrieveRelevantDrops()
public Character killBy(final Character killer)
public void dropFromFriendlyMonster(long delay)
public void dispatchMonsterKilled(boolean hasKiller)
public int getHighestDamagerId()
public boolean isAlive()
public void addListener(MonsterListener listener)
public Character getController()
public boolean isControllerHasAggro()
public boolean isControllerKnowsAboutAggro()
public Packet makeBossHPBarPacket()
public boolean hasBossHPBar()
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public MapObjectType getType()
public boolean isMobile()
public boolean isFacingLeft()
public ElementalEffectiveness getElementalEffectiveness(Element e)
public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration)
public boolean applyStatus(Character from, final MonsterStatusEffect status, boolean poison, long duration, boolean venom)
public final void dispelSkill(final MobSkill skill)
public void applyMonsterBuff(final Map<MonsterStatus, Integer> stats, final int x, long duration, MobSkill skill, final List<Integer> reflection)
public void refreshMobPosition()
public void resetMobPosition(Point newPoint)
public void debuffMob(int skillid)
public boolean isBuffed(MonsterStatus status)
public void setFake(boolean fake)
public boolean isFake()
public MapleMap getMap()
public MonsterAggroCoordinator getMapAggroCoordinator()
public Set<MobSkillId> getSkills()
public boolean hasSkill(int skillId, int level)
public boolean canUseSkill(MobSkill toUse, boolean apply)
public int canUseAttack(int attackPos, boolean isSkill)
public boolean hasAnySkill()
public MobSkillId getRandomSkill()
public boolean isFirstAttack()
public int getBuffToGive()
public void run()
public String getName()
public void addStolen(int itemId)
public List<Integer> getStolen()
public void setTempEffectiveness(Element e, ElementalEffectiveness ee, long milli)
public Collection<MonsterStatus> alreadyBuffedStats()
public BanishInfo getBanish()
public void setBoss(boolean boss)
public int getDropPeriodTime()
public int getPADamage()
public Map<MonsterStatus, MonsterStatusEffect> getStati()
public MonsterStatusEffect getStati(MonsterStatus ms)
public final ChangeableStats getChangedStats()
public final int getMobMaxHp()
public final void setOverrideStats(final OverrideMonsterStats ostats)
public final void changeLevel(final int newLevel)
public final void changeLevel(final int newLevel, boolean pqMob)
public final void changeDifficulty(final int difficulty, boolean pqMob)
public boolean isCharacterPuppetInVicinity(Character chr)
public boolean isLeadingPuppetInVicinity()
public Pair<Character, Boolean> aggroRemoveController()
public void aggroSwitchController(Character newController, boolean immediateAggro)
public void aggroAddPuppet(Character player)
public void aggroRemovePuppet(Character player)
public void aggroUpdateController()
public void aggroRedirectController()
public Boolean aggroMoveLifeUpdate(Character player)
public void aggroAutoAggroUpdate(Character player)
public void aggroMonsterDamage(Character attacker, int damage)
public void aggroUpdatePuppetVisibility()
public void aggroClearDamages()
public void aggroResetAggro()
public final int getRemoveAfter()
public void dispose()
```

### `org.gms.server.life.MonsterDropEntry`
- 声明: `public class MonsterDropEntry {`
- 方法数（启发式提取）: 1

```text
public MonsterDropEntry(int itemId, int chance, int Minimum, int Maximum, short questid)
```

### `org.gms.server.life.MonsterGlobalDropEntry`
- 声明: `public class MonsterGlobalDropEntry {`
- 方法数（启发式提取）: 1

```text
public MonsterGlobalDropEntry(int itemId, int chance, int continent, int Minimum, int Maximum, short questid)
```

### `org.gms.server.life.MonsterInformationProvider`
- 声明: `public class MonsterInformationProvider {`
- 方法数（启发式提取）: 15

```text
public static MonsterInformationProvider getInstance()
public final List<MonsterGlobalDropEntry> getRelevantGlobalDrops(int mapid)
public List<MonsterDropEntry> retrieveEffectiveDrop(final int monsterId)
public final List<MonsterDropEntry> retrieveDrop(final int monsterId)
public final List<Integer> retrieveDropPool(final int monsterId)
public final void setMobAttackAnimationTime(int monsterId, int attackPos, int animationTime)
public final Integer getMobAttackAnimationTime(int monsterId, int attackPos)
public final void setMobSkillAnimationTime(MobSkill skill, int animationTime)
public final Integer getMobSkillAnimationTime(MobSkill skill)
public final void setMobAttackInfo(int monsterId, int attackPos, int mpCon, int coolTime)
public final Pair<Integer, Integer> getMobAttackInfo(int monsterId, int attackPos)
public static ArrayList<Pair<Integer, String>> getMobsIDsFromName(String search)
public boolean isBoss(int id)
public String getMobNameFromId(int id)
public final void clearDrops()
```

### `org.gms.server.life.MonsterListener`
- 声明: `public interface MonsterListener {`
- 方法数（启发式提取）: 0

### `org.gms.server.life.MonsterStats`
- 声明: `public class MonsterStats {`
- 方法数（启发式提取）: 87

```text
public Map<String, Integer> animationTimes = new HashMap<>()
public Map<Element, ElementalEffectiveness> resistance = new HashMap<>()
public List<Integer> revives = Collections.emptyList()
public Set<MobSkillId> skills = new HashSet<>()
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
public Pair<Integer, Integer> getCool()
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

### `org.gms.server.life.NPC`
- 声明: `public class NPC extends AbstractLoadedLife {`
- 方法数（启发式提取）: 7

```text
public NPC(int id, NPCStats stats)
public boolean hasShop()
public void sendShop(Client c)
public void sendSpawnData(Client client)
public void sendDestroyData(Client client)
public MapObjectType getType()
public String getName()
```

### `org.gms.server.life.NPCStats`
- 声明: `public class NPCStats {`
- 方法数（启发式提取）: 3

```text
public NPCStats(String name)
public String getName()
public void setName(String name)
```

### `org.gms.server.life.OverrideMonsterStats`
- 声明: `public class OverrideMonsterStats {`
- 方法数（启发式提取）: 9

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

### `org.gms.server.life.PlayerNPC`
- 声明: `public class PlayerNPC extends AbstractMapObject {`
- 方法数（启发式提取）: 18

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
public static boolean canSpawnPlayerNpc(String name, int mapid)
public void updatePlayerNPCPosition(MapleMap map, Point newPos)
public static boolean spawnPlayerNPC(int mapid, Character chr)
public static boolean spawnPlayerNPC(int mapid, Point pos, Character chr)
public static void removePlayerNPC(Character chr)
public static void multicastSpawnPlayerNPC(int mapid, int world)
public static void removeAllPlayerNPC()
public static void addPlayerNPCMapObject(MapleMap map)
```

### `org.gms.server.life.PlayerNPCFactory`
- 声明: `public class PlayerNPCFactory {`
- 方法数（启发式提取）: 1

```text
public synchronized static boolean isExistentScriptid(int scriptid)
```

### `org.gms.server.life.SpawnPoint`
- 声明: `public class SpawnPoint {`
- 方法数（启发式提取）: 16

```text
public SpawnPoint(final Monster monster, Point pos, boolean immobile, int mobTime, int mobInterval, int team)
public int getSpawned()
public void setDenySpawn(boolean val)
public boolean getDenySpawn()
public boolean shouldSpawn()
public boolean shouldForceSpawn()
public Monster getMonster()
public void monsterKilled(int aniTime)
public void monsterDamaged(Character from, int trueDmg)
public void monsterHealed(int trueHeal)
public int getMonsterId()
public Point getPosition()
public final int getF()
public final int getFh()
public int getMobTime()
public int getTeam()
```

## `org.gms.server.life.positioner`

### `org.gms.server.life.positioner.PlayerNPCPodium`
- 声明: `public class PlayerNPCPodium {`
- 方法数（启发式提取）: 1

```text
public static Point getNextPlayerNpcPosition(MapleMap map)
```

### `org.gms.server.life.positioner.PlayerNPCPositioner`
- 声明: `public class PlayerNPCPositioner {`
- 方法数（启发式提取）: 1

```text
public static Point getNextPlayerNpcPosition(MapleMap map)
```

## `org.gms.server.loot`

### `org.gms.server.loot.LootInventory`
- 声明: `public class LootInventory {`
- 方法数（启发式提取）: 2

```text
public LootInventory(Character from)
public int hasItem(int itemid, int quantity)
```

### `org.gms.server.loot.LootManager`
- 声明: `public class LootManager {`
- 方法数（启发式提取）: 1

```text
public static List<MonsterDropEntry> retrieveRelevantDrops(int monsterId, List<Character> players)
```

## `org.gms.server.maps`

### `org.gms.server.maps.AbstractAnimatedMapObject`
- 声明: `public abstract class AbstractAnimatedMapObject extends AbstractMapObject implements AnimatedMapObject {`
- 方法数（启发式提取）: 4

```text
public int getStance()
public void setStance(int stance)
public boolean isFacingLeft()
public InPacket getIdleMovement()
```

### `org.gms.server.maps.AbstractMapObject`
- 声明: `public abstract class AbstractMapObject implements MapObject {`
- 方法数（启发式提取）: 6

```text
public abstract MapObjectType getType()
public Point getPosition()
public void setPosition(Point position)
public int getObjectId()
public void setObjectId(int id)
public void nullifyPosition()
```

### `org.gms.server.maps.AnimatedMapObject`
- 声明: `public interface AnimatedMapObject extends MapObject {`
- 方法数（启发式提取）: 0

### `org.gms.server.maps.Door`
- 声明: `public class Door {`
- 方法数（启发式提取）: 12

```text
public Door(Character owner, Point targetPosition)
public void updateDoorPortal(Character owner)
public static void attemptRemoveDoor(final Character owner)
public int getOwnerId()
public DoorObject getTownDoor()
public DoorObject getAreaDoor()
public MapleMap getTown()
public Portal getTownPortal()
public MapleMap getTarget()
public Pair<String, Integer> getDoorStatus()
public long getElapsedDeployTime()
public boolean isActive()
```

### `org.gms.server.maps.DoorObject`
- 声明: `public class DoorObject extends AbstractMapObject {`
- 方法数（启发式提取）: 18

```text
public DoorObject(int owner, MapleMap destination, MapleMap origin, int townPortalId, Point targetPosition, Point toPosition)
public void update(int townPortalId, Point toPosition)
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

### `org.gms.server.maps.Dragon`
- 声明: `public class Dragon extends AbstractAnimatedMapObject {`
- 方法数（启发式提取）: 6

```text
public Dragon(Character chr)
public MapObjectType getType()
public void sendSpawnData(Client client)
public int getObjectId()
public void sendDestroyData(Client c)
public Character getOwner()
```

### `org.gms.server.maps.FieldLimit`
- 声明: `public enum FieldLimit {`
- 方法数（启发式提取）: 2

```text
public long getValue()
public boolean check(int fieldlimit)
```

### `org.gms.server.maps.Foothold`
- 声明: `public class Foothold implements Comparable<Foothold> {`
- 方法数（启发式提取）: 13

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

### `org.gms.server.maps.FootholdTree`
- 声明: `public class FootholdTree {`
- 方法数（启发式提取）: 11

```text
public FootholdTree(Point p1, Point p2)
public FootholdTree(Point p1, Point p2, int depth)
public void insert(Foothold f)
public Foothold findWall(Point p1, Point p2)
public Foothold findBelow(Point p)
public int getX1()
public int getX2()
public int getY1()
public int getY2()
public int getMaxDropX()
public int getMinDropX()
```

### `org.gms.server.maps.GenericPortal`
- 声明: `public class GenericPortal implements Portal {`
- 方法数（启发式提取）: 19

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

### `org.gms.server.maps.HiredMerchant`
- 声明: `public class HiredMerchant extends AbstractMapObject {`
- 方法数（启发式提取）: 51

```text
public record PastVisitor(String chrName, Duration visitDuration)
public HiredMerchant(final Character owner, String desc, int itemId)
public void broadcastToVisitorsThreadsafe(Packet packet)
public byte[] getShopRoomInfo()
public boolean addVisitor(Character visitor)
public void removeVisitor(Character chr)
public int getVisitorSlotThreadsafe(Character visitor)
public void withdrawMesos(Character chr)
public void takeItemBack(int slot, Character chr)
public void buy(Client c, int item, short quantity)
public void forceClose()
public void closeOwnerMerchant(Character chr)
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
public void setDescription(String description)
public boolean isPublished()
public boolean isOpen()
public void setOpen(boolean set)
public int getItemId()
public boolean isOwner(Character chr)
public void sendMessage(Character chr, String msg)
public List<PlayerShopItem> sendAvailableBundles(int itemid)
public void saveItems(boolean shutdown) throws SQLException
public int getChannel()
public int getTimeOpen()
public void clearMessages()
public List<Pair<String, Byte>> getMessages()
public List<PastVisitor> getVisitorHistory()
public void addToBlacklist(String chrName)
public void removeFromBlacklist(String chrName)
public Set<String> getBlacklist()
public int getMapId()
public MapleMap getMap()
public List<SoldItem> getSold()
public int getMesos()
public MapObjectType getType()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public SoldItem(String buyer, int itemid, short quantity, int mesos)
public String getBuyer()
public int getItemId()
public short getQuantity()
public int getMesos()
```

### `org.gms.server.maps.Kite`
- 声明: `public class Kite extends AbstractMapObject {`
- 方法数（启发式提取）: 9

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

### `org.gms.server.maps.MapEffect`
- 声明: `public class MapEffect {`
- 方法数（启发式提取）: 4

```text
public MapEffect(String msg, int itemId)
public final Packet makeDestroyData()
public final Packet makeStartData()
public void sendStartData(Client client)
```

### `org.gms.server.maps.MapFactory`
- 声明: `public class MapFactory {`
- 方法数（启发式提取）: 4

```text
public static MapleMap loadMapFromWz(int mapid, int world, int channel, EventInstanceManager event)
public static String loadPlaceName(int mapid)
public static String loadStreetName(int mapid)
public static String getMapIdByLifeId(int lifeId)
```

### `org.gms.server.maps.MapItem`
- 声明: `public class MapItem extends AbstractMapObject {`
- 方法数（启发式提取）: 28

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

### `org.gms.server.maps.MapManager`
- 声明: `public class MapManager {`
- 方法数（启发式提取）: 9

```text
public MapManager(EventInstanceManager eim, int world, int channel)
public MapleMap resetMap(int mapid)
public MapleMap getMap(int mapid)
public MapleMap getMapByLifeId(int lifeId)
public MapleMap getDisposableMap(int mapid)
public boolean isMapLoaded(int mapId)
public Map<Integer, MapleMap> getMaps()
public void updateMaps()
public void dispose()
```

### `org.gms.server.maps.MapMonitor`
- 声明: `public class MapMonitor {`
- 方法数（启发式提取）: 1

```text
public MapMonitor(final MapleMap map, String portal)
```

### `org.gms.server.maps.MapObject`
- 声明: `public interface MapObject {`
- 方法数（启发式提取）: 0

### `org.gms.server.maps.MapObjectType`
- 声明: `public enum MapObjectType {`
- 方法数（启发式提取）: 0

### `org.gms.server.maps.MapPortal`
- 声明: `public class MapPortal extends GenericPortal {`
- 方法数（启发式提取）: 1

```text
public MapPortal()
```

### `org.gms.server.maps.MapleMap`
- 声明: `public class MapleMap {`
- 方法数（启发式提取）: 319

```text
public MapleMap(int mapid, int world, int channel, int returnMapId, float monsterRate)
public void setEventInstance(EventInstanceManager eim)
public EventInstanceManager getEventInstance()
public Rectangle getMapArea()
public int getWorld()
public void broadcastPacket(Character source, Packet packet)
public void broadcastGMPacket(Character source, Packet packet)
public void toggleDrops()
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
public void removeMapObject(int num)
public void removeMapObject(final MapObject obj)
public void generateMapDropRangeCache()
public Point calcDropPos(Point initial, Point fallback)
public boolean canDeployDoor(Point pos)
public static String getRoundedCoordinate(double angle)
public Pair<String, Integer> getDoorPositionStatus(Point pos)
public void dropItemsFromMonster(List<MonsterDropEntry> list, final Character chr, final Monster mob)
public void dropFromFriendlyMonster(final Character chr, final Monster mob)
public void dropFromReactor(final Character chr, final Reactor reactor, Item drop, Point dropPos, short questid)
public int getDroppedItemCount()
public int getDroppedItemsCountById(int itemid)
public void pickItemDrop(Packet pickupPacket, MapItem mdrop)
public List<MapItem> updatePlayerItemDropsToParty(int partyid, int charid, List<Character> partyMembers, Character partyLeaver)
public void updatePartyItemDropsToNewcomer(Character newcomer, List<MapItem> partyItems)
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
public Map<Integer, Character> getMapAllPlayers()
public List<Character> getPlayersInRange(Rectangle box)
public int countAlivePlayers()
public int countBosses()
public boolean damageMonster(final Character chr, final Monster monster, final int damage)
public void broadcastBalrogVictory(String leaderName)
public void broadcastHorntailVictory()
public void broadcastZakumVictory()
public void broadcastPinkBeanVictory(int channel)
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
public void spawnFakeMonsterOnGroundBelow(Monster mob, Point pos)
public Point getGroundBelow(Point pos)
public Point getPointBelow(Point pos)
public void spawnRevives(final Monster monster)
public void dismissRemoveAfter(final Monster monster)
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
public void searchItemReactors(final Reactor react)
public void changeEnvironment(String mapObj, int newState)
public void startMapEffect(String msg, int itemId)
public void startMapEffect(String msg, int itemId, long time)
public Character getAnyCharacterFromParty(int partyid)
public void addPartyMember(Character chr, int partyid)
public void removePartyMember(Character chr, int partyid)
public void removeParty(int partyid)
public void addPlayer(final Character chr)
public Portal getRandomPlayerSpawnpoint()
public Portal findClosestTeleportPortal(Point from)
public Portal findClosestPlayerSpawnpoint(Point from)
public Portal findClosestPortal(Point from)
public Portal findMarketPortal()
public Collection<Portal> getPortals()
public void addPlayerPuppet(Character player)
public void removePlayerPuppet(Character player)
public void removePlayer(Character chr)
public void broadcastMessage(Packet packet)
public void broadcastGMMessage(Packet packet)
public void broadcastMessage(Character source, Packet packet, boolean repeatToSource)
public void broadcastMessage(Character source, Packet packet, boolean repeatToSource, boolean ranged)
public void broadcastMessage(Packet packet, Point rangedFrom)
public void broadcastMessage(Character source, Packet packet, Point rangedFrom)
public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet)
public void broadcastBossHpMessage(Monster mm, int bossHash, Packet packet, Point rangedFrom)
public void broadcastSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)
public void broadcastGMSpawnPlayerMapObjectMessage(Character source, Character player, boolean enteringField)
public void broadcastUpdateCharLookMessage(Character source, Character player)
public void dropMessage(int type, String message)
public void broadcastStringMessage(int type, String message)
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
public Map<Integer, Character> getMapPlayers()
public Collection<Character> getCharacters()
public Character getCharacterById(int id)
public void moveMonster(Monster monster, Point reportedPos)
public void movePlayer(Character player, Point newPosition)
public final void toggleEnvironment(final String ms)
public final void moveEnvironment(final String ms, final int type)
public final Map<String, Integer> getEnvironment()
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
public void run()
public ActivateItemReactor(MapItem mapitem, Reactor reactor, Client c)
public void run()
public void instanceMapFirstSpawn(int difficulty, boolean isPq)
public void instanceMapRespawn()
public void instanceMapForceRespawn()
public void closeMapSpawnPoints()
public void restoreMapSpawnPoints()
public void setAllowSpawnPointInBox(boolean allow, Rectangle box)
public void setAllowSpawnPointInRange(boolean allow, Point from, double rangeSq)
public SpawnPoint findClosestSpawnpoint(Point from)
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
public void setBoat(boolean hasBoat)
public void setDocked(boolean isDocked)
public boolean getDocked()
public void setSeats(int seats)
public int getSeats()
public void broadcastGMMessage(Character source, Packet packet, boolean repeatToSource)
public void broadcastNONGMMessage(Character source, Packet packet, boolean repeatToSource)
public OxQuiz getOx()
public void setOx(OxQuiz set)
public void setOxQuiz(boolean b)
public boolean isOxQuiz()
public void setOnUserEnter(String onUserEnter)
public String getOnUserEnter()
public void setOnFirstUserEnter(String onFirstUserEnter)
public String getOnFirstUserEnter()
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
public Pair<Integer, String> getTimeMob()
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
public void monsterKilled(int aniTime)
public void monsterDamaged(Character from, int trueDmg)
public void monsterHealed(int trueHeal)
public void monsterKilled(int aniTime)
public void monsterDamaged(Character from, int trueDmg)
public void monsterHealed(int trueHeal)
public boolean claimOwnership(Character chr)
public Character unclaimOwnership()
public boolean unclaimOwnership(Character chr)
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
public final List<Pair<Integer, Integer>> getMobsToSpawn()
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

### `org.gms.server.maps.MapleTVEffect`
- 声明: `public class MapleTVEffect {`
- 方法数（启发式提取）: 1

```text
public static synchronized boolean broadcastMapleTVIfNotActive(Character player, Character victim, List<String> messages, int tvType)
```

### `org.gms.server.maps.MiniDungeon`
- 声明: `public class MiniDungeon {`
- 方法数（启发式提取）: 5

```text
public MiniDungeon(int base, long timeLimit)
public boolean registerPlayer(Character chr)
public boolean unregisterPlayer(Character chr)
public void close()
public void dispose()
```

### `org.gms.server.maps.MiniDungeonInfo`
- 声明: `public enum MiniDungeonInfo {`
- 方法数（启发式提取）: 5

```text
public int getBase()
public int getDungeonId()
public int getDungeons()
public static boolean isDungeonMap(int map)
public static MiniDungeonInfo getDungeon(int map)
```

### `org.gms.server.maps.MiniGame`
- 声明: `public class MiniGame extends AbstractMapObject {`
- 方法数（启发式提取）: 48

```text
public int getValue()
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
public String getDescription()
public int getOwnerScore()
public int getVisitorScore()
public void sendDestroyData(Client client)
public void sendSpawnData(Client client)
public MapObjectType getType()
```

### `org.gms.server.maps.Mist`
- 声明: `public class Mist extends AbstractMapObject {`
- 方法数（启发式提取）: 19

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

### `org.gms.server.maps.PlayerShop`
- 声明: `public class PlayerShop extends AbstractMapObject {`
- 方法数（启发式提取）: 41

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
public void forceRemoveVisitor(Character visitor)
public void removeVisitor(Character visitor)
public boolean isVisitor(Character visitor)
public boolean addItem(PlayerShopItem item)
public void takeItemBack(int slot, Character chr)
public boolean buy(Client c, int item, short quantity)
public void broadcastToVisitors(Packet packet)
public void broadcastRestoreToVisitors()
public void removeVisitors()
public void broadcast(Packet packet)
public void chat(Client c, String chat)
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
public SoldItem(String buyer, int itemid, short quantity, int mesos)
public String getBuyer()
public int getItemId()
public short getQuantity()
public int getMesos()
```

### `org.gms.server.maps.PlayerShopItem`
- 声明: `public class PlayerShopItem {`
- 方法数（启发式提取）: 7

```text
public PlayerShopItem(Item item, short bundles, int price)
public void setDoesExist(boolean tf)
public boolean isExist()
public Item getItem()
public short getBundles()
public int getPrice()
public void setBundles(short bundles)
```

### `org.gms.server.maps.Portal`
- 声明: `public interface Portal {`
- 方法数（启发式提取）: 0

### `org.gms.server.maps.PortalFactory`
- 声明: `public class PortalFactory {`
- 方法数（启发式提取）: 2

```text
public PortalFactory()
public Portal makePortal(int type, Data portal)
```

### `org.gms.server.maps.Reactor`
- 声明: `public class Reactor extends AbstractMapObject {`
- 方法数（启发式提取）: 45

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
public Pair<Integer, Integer> getReactItem(byte index)
public boolean isAlive()
public boolean isActive()
public void setAlive(boolean alive)
public void sendDestroyData(Client client)
public final Packet makeDestroyData()
public void sendSpawnData(Client client)
public final Packet makeSpawnData()
public void resetReactorActions(int newState)
public void forceHitReactor(final byte newState)
public void cancelReactorTimeout()
public void delayedHitReactor(final Client c, long delay)
public void hitReactor(Client c)
public void hitReactor(boolean wHit, int charPos, short stance, int skillid, Client c)
public boolean destroy()
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

### `org.gms.server.maps.ReactorDropEntry`
- 声明: `public class ReactorDropEntry {`
- 方法数（启发式提取）: 1

```text
public ReactorDropEntry(int itemId, int chance, int questId)
```

### `org.gms.server.maps.ReactorFactory`
- 声明: `public class ReactorFactory {`
- 方法数（启发式提取）: 2

```text
public static final ReactorStats getReactorS(int rid)
public static ReactorStats getReactor(int rid)
```

### `org.gms.server.maps.ReactorStats`
- 声明: `public class ReactorStats {`
- 方法数（启发式提取）: 14

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
public Pair<Integer, Integer> getReactItem(byte state, byte index)
public StateData(int type, Pair<Integer, Integer> reactItem, List<Integer> activeSkills, byte nextState)
```

### `org.gms.server.maps.SavedLocation`
- 声明: `public class SavedLocation {`
- 方法数（启发式提取）: 3

```text
public SavedLocation(int mapId, int portal)
public int getMapId()
public int getPortal()
```

### `org.gms.server.maps.SavedLocationType`
- 声明: `public enum SavedLocationType {`
- 方法数（启发式提取）: 1

```text
public static SavedLocationType fromString(String Str)
```

### `org.gms.server.maps.Summon`
- 声明: `public class Summon extends AbstractAnimatedMapObject {`
- 方法数（启发式提取）: 12

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

### `org.gms.server.maps.SummonMovementType`
- 声明: `public enum SummonMovementType {`
- 方法数（启发式提取）: 1

```text
public int getValue()
```

## `org.gms.server.minigame`

### `org.gms.server.minigame.RockPaperScissor`
- 声明: `public class RockPaperScissor {`
- 方法数（启发式提取）: 6

```text
public RockPaperScissor(final Client c, final byte mode)
public final boolean answer(final Client c, final int answer)
public final boolean timeOut(final Client c)
public final boolean nextRound(final Client c)
public final void reward(final Client c)
public final void dispose(final Client c)
```

## `org.gms.server.movement`

### `org.gms.server.movement.AbsoluteLifeMovement`
- 声明: `public class AbsoluteLifeMovement extends AbstractLifeMovement {`
- 方法数（启发式提取）: 6

```text
public AbsoluteLifeMovement(int type, Point position, int duration, int newstate)
public Point getPixelsPerSecond()
public void setPixelsPerSecond(Point wobble)
public int getFh()
public void setFh(int fh)
public void serialize(OutPacket p)
```

### `org.gms.server.movement.AbstractLifeMovement`
- 声明: `public abstract class AbstractLifeMovement implements LifeMovement {`
- 方法数（启发式提取）: 5

```text
public AbstractLifeMovement(int type, Point position, int duration, int newstate)
public int getType()
public int getDuration()
public int getNewstate()
public Point getPosition()
```

### `org.gms.server.movement.ChairMovement`
- 声明: `public class ChairMovement extends AbstractLifeMovement {`
- 方法数（启发式提取）: 4

```text
public ChairMovement(int type, Point position, int duration, int newstate)
public int getFh()
public void setFh(int fh)
public void serialize(OutPacket p)
```

### `org.gms.server.movement.ChangeEquip`
- 声明: `public class ChangeEquip implements LifeMovementFragment {`
- 方法数（启发式提取）: 3

```text
public ChangeEquip(int wui)
public void serialize(OutPacket p)
public Point getPosition()
```

### `org.gms.server.movement.JumpDownMovement`
- 声明: `public class JumpDownMovement extends AbstractLifeMovement {`
- 方法数（启发式提取）: 8

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

### `org.gms.server.movement.LifeMovement`
- 声明: `public interface LifeMovement extends LifeMovementFragment {`
- 方法数（启发式提取）: 0

### `org.gms.server.movement.LifeMovementFragment`
- 声明: `public interface LifeMovementFragment {`
- 方法数（启发式提取）: 0

### `org.gms.server.movement.RelativeLifeMovement`
- 声明: `public class RelativeLifeMovement extends AbstractLifeMovement {`
- 方法数（启发式提取）: 2

```text
public RelativeLifeMovement(int type, Point position, int duration, int newstate)
public void serialize(OutPacket p)
```

### `org.gms.server.movement.TeleportMovement`
- 声明: `public class TeleportMovement extends AbsoluteLifeMovement {`
- 方法数（启发式提取）: 2

```text
public TeleportMovement(int type, Point position, int newstate)
public void serialize(OutPacket p)
```

## `org.gms.server.partyquest`

### `org.gms.server.partyquest.AriantColiseum`
- 声明: `public class AriantColiseum {`
- 方法数（启发式提取）: 10

```text
public AriantColiseum(MapleMap eventMap, Expedition expedition)
public int getAriantScore(Character chr)
public void clearAriantScore(Character chr)
public void updateAriantScore(Character chr, int points)
public int getAriantRewardTier(Character chr)
public void clearAriantRewardTier(Character chr)
public void addLostShards(int quantity)
public void leaveArena(Character chr)
public void playerDisconnected(Character chr)
public void distributeAriantPoints()
```

### `org.gms.server.partyquest.CarnivalFactory`
- 声明: `public class CarnivalFactory {`
- 方法数（启发式提取）: 7

```text
public CarnivalFactory()
public static final CarnivalFactory getInstance()
public MCSkill getSkill(final int id)
public MCSkill getGuardian(final int id)
public record MCSkill(int cpLoss, MobSkillType mobSkillType, int level, boolean targetsAll)
public MobSkill getSkill()
public Disease getDisease()
```

### `org.gms.server.partyquest.GuardianSpawnPoint`
- 声明: `public class GuardianSpawnPoint {`
- 方法数（启发式提取）: 7

```text
public GuardianSpawnPoint(Point a)
public Point getPosition()
public void setPosition(Point position)
public boolean isTaken()
public void setTaken(boolean taken)
public int getTeam()
public void setTeam(int team)
```

### `org.gms.server.partyquest.MonsterCarnival`
- 声明: `public class MonsterCarnival {`
- 方法数（启发式提取）: 37

```text
public MonsterCarnival(Party p1, Party p2, int mapid, boolean cpq1, int room)
public void playerDisconnected(int charid)
public void leftParty(int charid)
public boolean canSummonR()
public void summonR()
public boolean canSummonB()
public void summonB()
public boolean canGuardianR()
public boolean canGuardianB()
public void exit()
public ScheduledFuture<?> getTimer()
public long getTimeLeft()
public int getTimeLeftSeconds()
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

### `org.gms.server.partyquest.MonsterCarnivalParty`
- 声明: `public class MonsterCarnivalParty {`
- 方法数（启发式提取）: 14

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

### `org.gms.server.partyquest.PartyQuest`
- 声明: `public class PartyQuest {`
- 方法数（启发式提取）: 5

```text
public PartyQuest(Party party)
public Party getParty()
public List<Character> getParticipants()
public void removeParticipant(Character chr) throws Throwable
public static int getExp(String PQ, int level)
```

### `org.gms.server.partyquest.Pyramid`
- 声明: `public class Pyramid extends PartyQuest {`
- 方法数（启发式提取）: 12

```text
public int getMode()
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

## `org.gms.server.quest`

### `org.gms.server.quest.Quest`
- 声明: `public class Quest {`
- 方法数（启发式提取）: 38

```text
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

### `org.gms.server.quest.QuestActionType`
- 声明: `public enum QuestActionType {`
- 方法数（启发式提取）: 1

```text
public static QuestActionType getByWZName(String name)
```

### `org.gms.server.quest.QuestRequirementType`
- 声明: `public enum QuestRequirementType {`
- 方法数（启发式提取）: 2

```text
public byte getType()
public static QuestRequirementType getByWZName(String name)
```

## `org.gms.server.quest.actions`

### `org.gms.server.quest.actions.AbstractQuestAction`
- 声明: `public abstract class AbstractQuestAction {`
- 方法数（启发式提取）: 7

```text
public AbstractQuestAction(QuestActionType action, Quest quest)
public abstract void run(Character chr, Integer extSelection)
public abstract void processData(Data data)
public boolean check(Character chr, Integer extSelection)
public QuestActionType getType()
public static List<Integer> getJobBy5ByteEncoding(int encoded)
public static List<Integer> getJobBySimpleEncoding(int encoded)
```

### `org.gms.server.quest.actions.BuffAction`
- 声明: `public class BuffAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 4

```text
public BuffAction(Quest quest, Data data)
public boolean check(Character chr, Integer extSelection)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.ExpAction`
- 声明: `public class ExpAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 4

```text
public ExpAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public static void runAction(Character chr, int gain)
```

### `org.gms.server.quest.actions.FameAction`
- 声明: `public class FameAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public FameAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.InfoAction`
- 声明: `public class InfoAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public InfoAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.ItemAction`
- 声明: `public class ItemAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 12

```text
public ItemAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public boolean check(Character chr, Integer extSelection)
public boolean restoreLostItem(Character chr, int itemid)
public ItemData(int map, int id, int count, Integer prop, int job, int gender, int period)
public int getId()
public int getCount()
public Integer getProp()
public int getJob()
public int getGender()
public int getPeriod()
```

### `org.gms.server.quest.actions.MesoAction`
- 声明: `public class MesoAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 4

```text
public MesoAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public static void runAction(Character chr, int gain)
```

### `org.gms.server.quest.actions.NextQuestAction`
- 声明: `public class NextQuestAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public NextQuestAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.PetSkillAction`
- 声明: `public class PetSkillAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 4

```text
public PetSkillAction(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer extSelection)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.PetSpeedAction`
- 声明: `public class PetSpeedAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public PetSpeedAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.PetTamenessAction`
- 声明: `public class PetTamenessAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public PetTamenessAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.QuestAction`
- 声明: `public class QuestAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 3

```text
public QuestAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
```

### `org.gms.server.quest.actions.SkillAction`
- 声明: `public class SkillAction extends AbstractQuestAction {`
- 方法数（启发式提取）: 8

```text
public SkillAction(Quest quest, Data data)
public void processData(Data data)
public void run(Character chr, Integer extSelection)
public SkillData(int id, int level, int masterLevel, List<Integer> jobs)
public int getId()
public int getLevel()
public int getMasterLevel()
public boolean jobsContains(Job job)
```

## `org.gms.server.quest.requirements`

### `org.gms.server.quest.requirements.AbstractQuestRequirement`
- 声明: `public abstract class AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public AbstractQuestRequirement(QuestRequirementType type)
public abstract boolean check(Character chr, Integer npcid)
public abstract void processData(Data data)
public QuestRequirementType getType()
```

### `org.gms.server.quest.requirements.BuffExceptRequirement`
- 声明: `public class BuffExceptRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public BuffExceptRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.BuffRequirement`
- 声明: `public class BuffRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public BuffRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.CompletedQuestRequirement`
- 声明: `public class CompletedQuestRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public CompletedQuestRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.EndDateRequirement`
- 声明: `public class EndDateRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public EndDateRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.FieldEnterRequirement`
- 声明: `public class FieldEnterRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public FieldEnterRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.InfoExRequirement`
- 声明: `public class InfoExRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public InfoExRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public List<String> getInfo()
```

### `org.gms.server.quest.requirements.InfoNumberRequirement`
- 声明: `public class InfoNumberRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public InfoNumberRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public short getInfoNumber()
```

### `org.gms.server.quest.requirements.IntervalRequirement`
- 声明: `public class IntervalRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public IntervalRequirement(Quest quest, Data data)
public long getInterval()
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.ItemRequirement`
- 声明: `public class ItemRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public ItemRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int getItemAmountNeeded(int itemid, boolean complete)
```

### `org.gms.server.quest.requirements.JobRequirement`
- 声明: `public class JobRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public JobRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.MaxLevelRequirement`
- 声明: `public class MaxLevelRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public MaxLevelRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.MesoRequirement`
- 声明: `public class MesoRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public MesoRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.MinLevelRequirement`
- 声明: `public class MinLevelRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public MinLevelRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.MinTamenessRequirement`
- 声明: `public class MinTamenessRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public MinTamenessRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.MobRequirement`
- 声明: `public class MobRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public MobRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int getRequiredMobCount(int mobid)
```

### `org.gms.server.quest.requirements.MonsterBookCountRequirement`
- 声明: `public class MonsterBookCountRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public MonsterBookCountRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.NpcRequirement`
- 声明: `public class NpcRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public NpcRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public int get()
```

### `org.gms.server.quest.requirements.PetRequirement`
- 声明: `public class PetRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public PetRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.QuestRequirement`
- 声明: `public class QuestRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 3

```text
public QuestRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
```

### `org.gms.server.quest.requirements.ScriptRequirement`
- 声明: `public class ScriptRequirement extends AbstractQuestRequirement {`
- 方法数（启发式提取）: 4

```text
public ScriptRequirement(Quest quest, Data data)
public void processData(Data data)
public boolean check(Character chr, Integer npcid)
public boolean get()
```

## `org.gms.service`

### `org.gms.service.AccountService`
- 声明: `public class AccountService {`
- 方法数（启发式提取）: 19

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
public void resetAllLoggedIn(int id)
public void banAccount(int accountId, String reason)
public void unbanAccount(int accountId)
public void resetAllLoggedIn()
public void ban(Character chr, String reason)
public void ban(String str, String reason, boolean isAccount)
public boolean isBanned(String ip)
public QuickslotkeymappedDO getQuickSlotKeyMap(int accountId)
```

### `org.gms.service.AuthService`
- 声明: `public class AuthService {`
- 方法数（启发式提取）: 2

```text
public Map<String, String> getToken(String name, String password)
public Map<String, String> refreshToken(String token)
```

### `org.gms.service.AutobanConfigService`
- 声明: `public class AutobanConfigService {`
- 方法数（启发式提取）: 3

```text
public void loadConfigs()
public List<AutobanConfigDTO> getConfigList()
public void updateConfig(AutobanConfigDTO dto)
```

### `org.gms.service.CashShopService`
- 声明: `public class CashShopService {`
- 方法数（启发式提取）: 6

```text
public List<ModifiedCashItemDO> loadAllModifiedCashItems()
public List<CashCategory> getAllCategoryList()
public Page<CashShopSearchRtnDTO> getCommodityByCategory(CashCategory data)
public CashShopSearchRtnDTO getCommodityBySn(Integer sn)
public void changeOnSale(ModifiedCashItemDO data)
public void batchChangeOnSale(CashShopBatchOnSaleReqDTO submit)
```

### `org.gms.service.CharacterService`
- 声明: `public class CharacterService {`
- 方法数（启发式提取）: 20

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
```

### `org.gms.service.CommandService`
- 声明: `public class CommandService {`
- 方法数（启发式提取）: 7

```text
public void loadCommands(final HashMap<String, Command> registeredCommands, final List<Pair<List<String>, List<String>>> commandsNameDesc)
public Page<CommandReqDTO> getCommandListFromDB(CommandReqDTO request)
public String getDescriptionByCommandInfoDO(CommandInfoDO CommandDO)
public CommandInfoDO updateCommand(CommandReqDTO request)
public void reloadEventsByGMCommand()
public void reloadPortalsByGMCommand()
public void reloadMapsByGMCommand()
```

### `org.gms.service.CommonService`
- 声明: `public class CommonService {`
- 方法数（启发式提取）: 4

```text
public EquipmentInfoRtnDTO getEquipmentInfoByItemId(EquipmentInfoReqDTO submitData)
public Integer getOnlinePlayerCountByWorldId(Integer worldId)
public Integer getAllWorldsOnlinePlayersCount(List<Integer> worldIdList)
public List<InformationResult> getInformation(InformationSearch condition)
```

### `org.gms.service.ConfigService`
- 声明: `public class ConfigService {`
- 方法数（启发式提取）: 11

```text
public List<GameConfigDO> loadGameConfigs()
public ConfigTypeDTO getConfigTypeList()
public Page<GameConfigDO> getConfigList(GameConfigReqDTO condition)
public void addConfig(GameConfigDO condition)
public void updateConfig(GameConfigDO condition)
public void deleteConfig(Long id)
public void deleteConfigList(List<Long> ids)
public int importYml(MultipartFile file)
public ResponseEntity<Resource> exportYml()
public String getFilename()
public Collector<GameConfigDO, ?, Map<String, Object>> toMap()
```

### `org.gms.service.DropService`
- 声明: `public class DropService {`
- 方法数（启发式提取）: 2

```text
public Page<DropSearchRtnDTO> getDropList(DropSearchReqDTO data, boolean isGlobal)
public Long modifyDropData(DropSearchRtnDTO data, boolean isGlobal, boolean isDelete)
```

### `org.gms.service.FamilyService`
- 声明: `public class FamilyService {`
- 方法数（启发式提取）: 1

```text
public void loadAllFamilies()
```

### `org.gms.service.FileTreeService`
- 声明: `public class FileTreeService {`
- 方法数（启发式提取）: 4

```text
public String readFile(String currentKey, String filename)
public void writeFile(String currentKey, String filename, String content)
public List<FileTreeNodeDTO> tree(String currentKey)
public File resolveByTreeKey(String currentKey)
```

### `org.gms.service.GachaponService`
- 声明: `public class GachaponService {`
- 方法数（启发式提取）: 8

```text
public void updatePool(GachaponRewardPoolDO submit)
public void deletePool(Integer id)
public Page<GachaponPoolSearchRtnDTO> getPools(GachaponPoolSearchReqDTO condition)
public List<GachaponRewardDO> getRewards(Integer poolId)
public void updateReward(GachaponRewardDO reward)
public void deleteReward(Integer id)
public void doGachapon(Character player, int gachaponId)
public List<GachaponRewardDO> getRewardsByNpcId(Integer npcId)
```

### `org.gms.service.GiveService`
- 声明: `public class GiveService {`
- 方法数（启发式提取）: 1

```text
public void give(GiveResourceReqDTO submitData)
```

### `org.gms.service.HpMpAlertService`
- 声明: `public class HpMpAlertService {`
- 方法数（启发式提取）: 9

```text
public static final Map<Integer, HpMpAlertDO> cacheMap = new ConcurrentHashMap<>()
public byte getHpAlert(int characterId)
public void setHpAlert(int characterId, byte alert)
public float getHpAlertPer(int characterId)
public byte getMpAlert(int characterId)
public void setMpAlert(int characterId, byte alert)
public float getMpAlertPer(int characterId)
public void saveAll()
public void clear()
```

### `org.gms.service.InventoryService`
- 声明: `public class InventoryService {`
- 方法数（启发式提取）: 7

```text
public List<InventoryTypeRtnDTO> getInventoryTypeList()
public Page<InventorySearchReqDTO> getCharacterList(InventorySearchReqDTO data)
public List<InventorySearchRtnDTO> getInventoryList(InventorySearchReqDTO data)
public void deleteInventoryByCharacterId(int cid)
public void updateInventory(InventorySearchRtnDTO data)
public void deleteInventory(InventorySearchRtnDTO data)
public List<PetignoresDO> getPetIgnoreByPetId(Integer petId)
```

### `org.gms.service.ItemService`
- 声明: `public class ItemService {`
- 方法数（启发式提取）: 1

```text
public Equip getEquipmentInfoByItemId(Integer itemId)
```

### `org.gms.service.LangResourceService`
- 声明: `public class LangResourceService {`
- 方法数（启发式提取）: 3

```text
public String getI18n(LangResourcesDO langResourcesDO)
public void insertOrUpdateI18n(LangResourcesDO langResourcesDO)
public void deleteI18n(LangResourcesDO langResourcesDO)
```

### `org.gms.service.MonsterBookService`
- 声明: `public class MonsterBookService {`
- 方法数（启发式提取）: 1

```text
public List<MonsterbookDO> getByCharacterId(int cid)
```

### `org.gms.service.MtsService`
- 声明: `public class MtsService {`
- 方法数（启发式提取）: 1

```text
public void deleteMtsByCharacterId(int cid)
```

### `org.gms.service.NameChangeService`
- 声明: `public class NameChangeService {`
- 方法数（启发式提取）: 6

```text
public void applyAllNameChange()
public void applyNameChange(int characterId, String characterName)
public List<NamechangesDO> getAllNameChanges()
public void doNameChange(NamechangesDO data)
public boolean registerNameChange(Character chr, String newName)
public void cancelPendingNameChange(Character chr, boolean needFinish)
```

### `org.gms.service.NewYearCardService`
- 声明: `public class NewYearCardService {`
- 方法数（启发式提取）: 2

```text
public void startPendingNewYearCardRequests()
public List<NewyearDO> loadPlayerNewYearCards(Character chr)
```

### `org.gms.service.NoteService`
- 声明: `public class NoteService {`
- 方法数（启发式提取）: 4

```text
public void sendNormal(String message, String senderName, String receiverName)
public void sendWithFame(String message, String senderName, String receiverName)
public void show(Character chr)
public Optional<NotesDO> delete(int noteId)
```

### `org.gms.service.NpcService`
- 声明: `public class NpcService {`
- 方法数（启发式提取）: 5

```text
public List<PlayernpcsFieldDO> getPlayerNpcFields(PlayernpcsFieldDO condition)
public List<PlayernpcsDO> getPlayerNpcDOs(PlayernpcsDO condition)
public List<PlayernpcsEquipDO> getPlayerNpcEquipDOs(PlayernpcsEquipDO condition)
public List<PlayerNPC> getPlayerNPC(PlayernpcsDO condition)
public PlayerNPC createPlayerNPC(PlayernpcsDO playerNpcDO, List<PlayernpcsEquipDO> playerNpcEquipDOS)
```

### `org.gms.service.NxCodeService`
- 声明: `public class NxCodeService {`
- 方法数（启发式提取）: 1

```text
public void clearExpirations()
```

### `org.gms.service.NxCouponService`
- 声明: `public class NxCouponService {`
- 方法数（启发式提取）: 2

```text
public List<Integer> selectActiveCouponIds(int weekDay, int hourDay)
public List<NxcouponsDO> getNxCoupons(NxcouponsDO condition)
```

### `org.gms.service.QuestService`
- 声明: `public class QuestService {`
- 方法数（启发式提取）: 2

```text
public void deleteQuestProgressByCharacter(int cid)
public List<QuestStatus> getQuestStatusByCharacter(int cid)
```

### `org.gms.service.ServerService`
- 声明: `public class ServerService {`
- 方法数（启发式提取）: 2

```text
public List<WorldListRtnDTO> worldList()
public List<ChannelListRtnDTO> channelList(int worldId)
```

### `org.gms.service.ShopService`
- 声明: `public class ShopService {`
- 方法数（启发式提取）: 4

```text
public Page<ShopSearchRtnDTO> getShopList(ShopSearchReqDTO data)
public Page<ShopItemSearchRtnDTO> getShopItemList(ShopSearchReqDTO data)
public ShopItemSearchRtnDTO getShopItem(Long id)
public Long modifyShopItem(ShopItemSearchRtnDTO data, boolean isDelete)
```

### `org.gms.service.UserDetailsImpl`
- 声明: `public class UserDetailsImpl implements UserDetails {`
- 方法数（启发式提取）: 11

```text
public UserDetailsImpl(Integer id, String name, String password, Collection<? extends GrantedAuthority> authorities)
public static UserDetailsImpl build(AccountsDO user, Collection<? extends GrantedAuthority> authorities)
public Collection<? extends GrantedAuthority> getAuthorities()
public Integer getId()
public String getPassword()
public String getUsername()
public boolean isAccountNonExpired()
public boolean isAccountNonLocked()
public boolean isCredentialsNonExpired()
public boolean isEnabled()
public boolean equals(Object o)
```

### `org.gms.service.UserDetailsServiceImpl`
- 声明: `public class UserDetailsServiceImpl implements UserDetailsService {`
- 方法数（启发式提取）: 2

```text
public UserDetailsServiceImpl(AccountsMapper userRepository)
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException
```

### `org.gms.service.WorldTransferService`
- 声明: `public class WorldTransferService {`
- 方法数（启发式提取）: 5

```text
public void applyAllWorldTransfer()
public boolean checkWorldTransferEligibility(WorldtransfersDO data)
public void doWorldTransfer(WorldtransfersDO data)
public boolean registerWorldTransfer(Character chr, int newWorld)
public void cancelPendingWorldTransfer(Character chr, boolean needFinish)
```

## `org.gms.util`

### `org.gms.util.BCrypt`
- 声明: `public class BCrypt {`
- 方法数（启发式提取）: 10

```text
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

### `org.gms.util.BasePageUtil`
- 声明: `public class BasePageUtil<T> {`
- 方法数（启发式提取）: 8

```text
public static <T> BasePageUtil<T> create(Collection<T> data)
public static <T> BasePageUtil<T> create(Collection<T> data, BasePageDTO basePageDTO)
public static <T> BasePageUtil<T> create(Collection<T> data, Integer pageNo, Integer pageSize)
public static <T> BasePageUtil<T> create(Collection<T> data, boolean onlyTotal, boolean notPage)
public BasePageUtil<T> filter(Predicate<T> predicate)
public BasePageUtil<T> sorted(Comparator<? super T> comparator)
public Page<T> page()
public <R> Page<R> page(Function<T, R> mapper)
```

### `org.gms.util.CashIdGenerator`
- 声明: `public class CashIdGenerator {`
- 方法数（启发式提取）: 3

```text
public static synchronized void loadExistentCashIdsFromDb()
public static synchronized int generateCashId()
public static synchronized void freeCashId(int cashId)
```

### `org.gms.util.CustomSpringBeanConfig`
- 声明: `public class CustomSpringBeanConfig {`
- 方法数（启发式提取）: 2

```text
public SpringDocConfigProperties springDocConfigProperties()
public SwaggerUiConfigProperties swaggerUiConfigProperties()
```

### `org.gms.util.DatabaseConnection`
- 声明: `public class DatabaseConnection {`
- 方法数（启发式提取）: 1

```text
public static Connection getConnection() throws SQLException
```

### `org.gms.util.ExtendUtil`
- 声明: `public class ExtendUtil {`
- 方法数（启发式提取）: 2

```text
public static ExtendValueDO getExtendValue(String extendId, String extendType, String extendName)
public static void saveOrUpdateExtendValue(String extendId, String extendType, String extendName, String extendValue)
```

### `org.gms.util.HexTool`
- 声明: `public class HexTool {`
- 方法数（启发式提取）: 4

```text
public static String toHexString(byte[] bytes)
public static String toCompactHexString(byte[] bytes)
public static byte[] toBytes(String hexString)
public static String toStringFromCharset(final byte[] bytes)
```

### `org.gms.util.I18nUtil`
- 声明: `public class I18nUtil {`
- 方法数（启发式提取）: 10

```text
public static final Locale LANGUAGE = Locale.forLanguageTag(ServerManager.getApplicationContext().getBean(ServiceProperty.class).getLanguage())
public static final MessageSource messageSource = ServerManager.getApplicationContext().getBean("messageSource", MessageSource.class)
public static final MessageSource logSource = ServerManager.getApplicationContext().getBean("logSource", MessageSource.class)
public static final MessageSource exceptionSource = ServerManager.getApplicationContext().getBean("exceptionSource", MessageSource.class)
public static String getMessage(String code, Object... args)
public static String getMessage(Locale locale, String code, Object... args)
public static String getLogMessage(String code, Object... args)
public static String getLogMessage(Locale locale, String code, Object... args)
public static String getExceptionMessage(String code, Object... args)
public static String getExceptionMessage(Locale locale, String code, Object... args)
```

### `org.gms.util.IntervalBuilder`
- 声明: `public class IntervalBuilder {`
- 方法数（启发式提取）: 5

```text
public IntervalBuilder()
public void addInterval(int from, int to)
public boolean inInterval(int point)
public boolean inInterval(int from, int to)
public void clear()
```

### `org.gms.util.JwtUtils`
- 声明: `public class JwtUtils {`
- 方法数（启发式提取）: 3

```text
public String generateJwtToken(String username)
public String getUserNameFromJwtToken(String token)
public boolean validateJwtToken(String authToken)
```

### `org.gms.util.LRUCache`
- 声明: `public class LRUCache<K, V> extends LinkedHashMap<K, V> {`
- 方法数（启发式提取）: 3

```text
public LRUCache()
public LRUCache(int capacity)
public boolean removeEldestEntry(Map.Entry<K, V> eldest)
```

### `org.gms.util.NumberTool`
- 声明: `public class NumberTool {`
- 方法数（启发式提取）: 4

```text
public static long BytesToLong(byte[] aToConvert)
public static byte[] LongToBytes(long nToConvert)
public static int floatToInt(float f)
public static int doubleToInt(double d)
```

### `org.gms.util.PacketCreator`
- 声明: `public class PacketCreator {`
- 方法数（启发式提取）: 485

```text
public static final List<Pair<Stat, Integer>> EMPTY_STATUPDATE = Collections.emptyList()
public static long getTime(long utcTimestamp)
public static Packet showHpHealed(int cid, int amount)
public static Packet setExtraPendantSlot(boolean toggleExtraSlot)
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
public static Packet spawnPlayerMapObject(Client target, Character chr, boolean enteringField)
public static Packet onNewYearCardRes(Character user, int cardId, int mode, int msg)
public static Packet onNewYearCardRes(Character user, NewYearCardRecord newyear, int mode, int msg)
public static Packet updateHiredMerchantBox(HiredMerchant hm)
public static Packet updatePlayerShopBox(PlayerShop shop)
public static Packet removePlayerShopBox(PlayerShop shop)
public static Packet facialExpression(Character from, int expression)
public static Packet movePlayer(int chrId, InPacket movementPacket, long movementDataLength)
public static Packet moveSummon(int cid, int oid, Point startPos, InPacket movementPacket, long movementDataLength)
public static Packet moveMonster(int oid, boolean skillPossible, int skill, int skillId, int skillLevel, int pOption, Point startPos, InPacket movementPacket, long movementDataLength)
public static Packet summonAttack(int cid, int summonOid, byte direction, List<SummonAttackEntry> allDamage)
public static Packet summonAttack(int cid, int summonSkillId, byte direction, List<SummonAttackEntry> allDamage)
public static Packet closeRangeAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, Map<Integer, List<Integer>> damage, int speed, int direction, int display)
public static Packet rangedAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, int projectile, Map<Integer, List<Integer>> damage, int speed, int direction, int display)
public static Packet magicAttack(Character chr, int skill, int skilllevel, int stance, int numAttackedAndDamage, Map<Integer, List<Integer>> damage, int charge, int speed, int direction, int display)
public static Packet throwGrenade(int cid, Point pos, int keyDown, int skillId, int skillLevel)
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
public static Packet giveDebuff(List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet giveForeignDebuff(int chrId, List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet cancelForeignFirstDebuff(int cid, long mask)
public static Packet cancelForeignDebuff(int cid, long mask)
public static Packet giveForeignBuff(int chrId, List<Pair<BuffStat, Integer>> statups)
public static Packet cancelForeignBuff(int chrId, List<BuffStat> statups)
public static Packet cancelBuff(List<BuffStat> statups)
public static Packet cancelDebuff(long mask)
public static Packet giveForeignSlowDebuff(int chrId, List<Pair<Disease, Integer>> statups, MobSkill skill)
public static Packet cancelForeignSlowDebuff(int chrId)
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
public static Packet updateParty(int forChannel, Party party, PartyOperation op, PartyCharacter target)
public static Packet partyPortal(int townId, int targetId, Point position)
public static Packet updatePartyMemberHP(int cid, int curhp, int maxhp)
public static Packet multiChat(String name, String chattext, int mode)
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
public static Packet sendSpouseChat(Character partner, String msg)
public static Packet OnCoupleMessage(String fiance, String text, boolean spouse)
public static Packet addMessengerPlayer(String from, Character chr, int position, int channel)
public static Packet removeMessengerPlayer(int position)
public static Packet updateMessengerPlayer(String from, Character chr, int position, int channel)
public static Packet joinMessenger(int position)
public static Packet messengerChat(String text)
public static Packet messengerNote(String text, int mode, int mode2)
public static Packet showPet(Character chr, Pet pet, boolean remove, boolean hunger)
public static Packet movePet(int cid, int pid, byte slot, List<LifeMovementFragment> moves)
public static Packet petChat(int cid, byte index, int act, String text)
public static Packet petFoodResponse(int cid, byte index, boolean success, boolean balloonType)
public static Packet commandResponse(int cid, byte index, boolean talk, int animation, boolean balloonType)
public static Packet showOwnPetLevelUp(byte index)
public static Packet showPetLevelUp(Character chr, byte index)
public static Packet changePetName(Character chr, String newname, int slot)
public static Packet loadExceptionList(final int cid, final int petId, final byte petIdx, final List<Integer> data)
public static Packet petStatUpdate(Character chr)
public static Packet showForcedEquip(int team)
public static Packet summonSkill(int cid, int summonSkillId, int newStance)
public static Packet skillCooldown(int sid, int time)
public static Packet skillBookResult(Character chr, int skillid, int maxlevel, boolean canuse, boolean success)
public static Packet getMacros(SkillMacro[] macros)
public static Packet showAllCharacterInfo(int worldid, List<Character> chars, boolean usePic)
public static Packet updateMount(int charid, Mount mount, boolean levelup)
public static Packet crogBoatPacket(boolean type)
public static Packet boatPacket(boolean type)
public static Packet getMiniGame(Client c, MiniGame minigame, boolean owner, int piece)
public static Packet getMiniGameReady(MiniGame game)
public static Packet getMiniGameUnReady(MiniGame game)
public static Packet getMiniGameStart(MiniGame game, int loser)
public static Packet getMiniGameSkipOwner(MiniGame game)
public static Packet getMiniGameRequestTie(MiniGame game)
public static Packet getMiniGameDenyTie(MiniGame game)
public static Packet getMiniRoomError(int status)
public static Packet getMiniGameSkipVisitor(MiniGame game)
public static Packet getMiniGameMoveOmok(MiniGame game, int move1, int move2, int move3)
public static Packet getMiniGameNewVisitor(MiniGame minigame, Character chr, int slot)
public static Packet getMiniGameRemoveVisitor()
public static Packet getMiniGameOwnerWin(MiniGame game, boolean forfeit)
public static Packet getMiniGameVisitorWin(MiniGame game, boolean forfeit)
public static Packet getMiniGameTie(MiniGame game)
public static Packet getMiniGameClose(boolean visitor, int type)
public static Packet getMatchCard(Client c, MiniGame minigame, boolean owner, int piece)
public static Packet getMatchCardStart(MiniGame game, int loser)
public static Packet getMatchCardNewVisitor(MiniGame minigame, Character chr, int slot)
public static Packet getMatchCardSelect(MiniGame game, int turn, int slot, int firstslot, int type)
public static Packet openRPSNPC()
public static Packet rpsMesoError(int mesos)
public static Packet rpsSelection(byte selection, byte answer)
public static Packet rpsMode(byte mode)
public static Packet fredrickMessage(byte operation)
public static Packet getFredrick(byte op)
public static Packet getFredrick(Character chr)
public static Packet addOmokBox(Character chr, int amount, int type)
public static Packet addMatchCardBox(Character chr, int amount, int type)
public static Packet removeMinigameBox(Character chr)
public static Packet getPlayerShopChat(Character chr, String chat, byte slot)
public static Packet getTradeChat(Character chr, String chat, boolean owner)
public static Packet hiredMerchantBox()
public static Packet getOwlMessage(int msg)
public static Packet owlOfMinerva(Client c, int itemId, List<Pair<PlayerShopItem, AbstractMapObject>> hmsAvailable)
public static Packet getOwlOpen(List<Integer> owlLeaderboards)
public static Packet retrieveFirstMessage()
public static Packet remoteChannelChange(byte ch)
public static Packet getHiredMerchant(Character chr, HiredMerchant hm, boolean firstTime)
public static Packet updateHiredMerchant(HiredMerchant hm, Character chr)
public static Packet hiredMerchantChat(String message, byte slot)
public static Packet hiredMerchantVisitorLeave(int slot)
public static Packet hiredMerchantOwnerLeave()
public static Packet hiredMerchantOwnerMaintenanceLeave()
public static Packet hiredMerchantMaintenanceMessage()
public static Packet leaveHiredMerchant(int slot, int status2)
public static Packet viewMerchantVisitorHistory(List<HiredMerchant.PastVisitor> pastVisitors)
public static Packet viewMerchantBlacklist(Set<String> chrNames)
public static Packet hiredMerchantVisitorAdd(Character chr, int slot)
public static Packet spawnHiredMerchantBox(HiredMerchant hm)
public static Packet removeHiredMerchantBox(int id)
public static Packet spawnPlayerNPC(PlayerNPC npc)
public static Packet getPlayerNPC(PlayerNPC npc)
public static Packet removePlayerNPC(int oid)
public static Packet sendYellowTip(String tip)
public static Packet givePirateBuff(List<Pair<BuffStat, Integer>> statups, int buffid, int duration)
public static Packet giveForeignPirateBuff(int cid, int buffid, int time, List<Pair<BuffStat, Integer>> statups)
public static Packet sendMTS(List<MTSItemInfo> items, int tab, int type, int page, int pages)
public static Packet noteError(byte error)
public static Packet useChalkboard(Character chr, boolean close)
public static Packet trockRefreshMapList(Character chr, boolean delete, boolean vip)
public static Packet sendWorldTransferRules(int error, Client c)
public static Packet showWorldTransferSuccess(Item item, int accountId)
public static Packet sendNameTransferRules(int error)
public static Packet sendNameTransferCheck(String availableName, boolean canUseName)
public static Packet showNameChangeSuccess(Item item, int accountId)
public static Packet showNameChangeCancel(boolean success)
public static Packet showWorldTransferCancel(boolean success)
public static Packet showMTSCash(Character chr)
public static Packet MTSWantedListingOver(int nx, int items)
public static Packet MTSConfirmSell()
public static Packet MTSConfirmBuy()
public static Packet MTSFailBuy()
public static Packet MTSConfirmTransfer(int quantity, int pos)
public static Packet notYetSoldInv(List<MTSItemInfo> items)
public static Packet transferInventory(List<MTSItemInfo> items)
public static Packet showCouponRedeemedItems(int accountId, int maplePoints, int mesos, List<Item> cashItems, List<Pair<Integer, Integer>> items)
public static Packet showCash(Character mc)
public static Packet enableCSUse(Character mc)
public static Packet getFindResult(Character target, byte type, int fieldOrChannel, byte flag)
public static Packet getWhisperResult(String target, boolean success)
public static Packet getWhisperReceive(String sender, int channel, boolean fromAdmin, String message)
public static Packet sendAutoHpPot(int itemId)
public static Packet sendAutoMpPot(int itemId)
public static Packet showOXQuiz(int questionSet, int questionId, boolean askQuestion)
public static Packet updateGender(Character chr)
public static Packet enableReport()
public static Packet giveFinalAttack(int skillid, int time)
public static Packet loadFamily(Character player)
public static Packet sendFamilyMessage(int type, int mesos)
public static Packet getFamilyInfo(FamilyEntry f)
public static Packet showPedigree(FamilyEntry entry)
public static Packet updateAreaInfo(int area, String info)
public static Packet getGPMessage(int gpChange)
public static Packet getItemMessage(int itemid)
public static Packet addCard(boolean full, int cardid, int level)
public static Packet showGainCard()
public static Packet showForeignCardEffect(int id)
public static Packet changeCover(int cardid)
public static Packet aranGodlyStats()
public static Packet showIntro(String path)
public static Packet showInfo(String path)
public static Packet showForeignInfo(int cid, String path)
public static Packet openUI(byte ui)
public static Packet lockUI(boolean enable)
public static Packet disableUI(boolean enable)
public static Packet itemMegaphone(String msg, boolean whisper, int channel, Item item)
public static Packet removeNPC(int objId)
public static Packet removeNPCController(int objId)
public static Packet reportResponse(byte mode)
public static Packet sendHammerData(int hammerUsed)
public static Packet sendHammerMessage()
public static Packet playPortalSound()
public static Packet showMonsterBookPickup()
public static Packet showEquipmentLevelUp()
public static Packet showItemLevelup()
public static Packet showSpecialEffect(int effect)
public static Packet showMakerEffect(boolean makerSucceeded)
public static Packet showForeignMakerEffect(int cid, boolean makerSucceeded)
public static Packet showForeignEffect(int effect)
public static Packet showForeignEffect(int chrId, int effect)
public static Packet showOwnRecovery(byte heal)
public static Packet showRecovery(int chrId, byte amount)
public static Packet showWheelsLeft(int left)
public static Packet updateQuestFinish(short quest, int npc, short nextquest)
public static Packet showInfoText(String text)
public static Packet questError(short quest)
public static Packet questFailure(byte type)
public static Packet questExpire(short quest)
public static Packet makerResult(boolean success, int itemMade, int itemCount, int mesos, List<Pair<Integer, Integer>> itemsLost, int catalystID, List<Integer> INCBuffGems)
public static Packet makerResultCrystal(int itemIdGained, int itemIdLost)
public static Packet makerResultDesynth(int itemId, int mesos, List<Pair<Integer, Integer>> itemsGained)
public static Packet makerEnableActions()
public static Packet getMultiMegaphone(String[] messages, int channel, boolean showEar)
public static Packet getGMEffect(int type, byte mode)
public static Packet findMerchantResponse(boolean map, int extra)
public static Packet disableMinimap()
public static Packet sendFamilyInvite(int playerId, String inviter)
public static Packet sendFamilySummonRequest(String familyName, String from)
public static Packet sendFamilyLoginNotice(String name, boolean loggedIn)
public static Packet sendFamilyJoinResponse(boolean accepted, String added)
public static Packet getSeniorMessage(String name)
public static Packet sendGainRep(int gain, String from)
public static Packet showBoughtCashPackage(List<Item> cashPackage, int accountId)
public static Packet showBoughtQuestItem(int itemId)
public static Packet onCashItemGachaponOpenFailed()
public static Packet onCashGachaponOpenSuccess(int accountid, long boxCashId, int remainingBoxes, Item reward, int rewardItemId, int rewardQuantity, boolean bJackpot)
public static Packet sendMesoLimit()
public static Packet removeItemFromDuey(boolean remove, int Package)
public static Packet sendDueyParcelReceived(String from, boolean quick)
public static Packet sendDueyParcelNotification(boolean quick)
public static Packet sendDueyMSG(byte operation)
public static Packet sendDuey(int operation, List<DueyPackage> packages)
public static Packet sendDojoAnimation(byte firstByte, String animation)
public static Packet getDojoInfo(String info)
public static Packet getDojoInfoMessage(String message)
public static Packet blockedMessage(int type)
public static Packet blockedMessage2(int type)
public static Packet updateDojoStats(Character chr, int belt)
public static Packet levelUpMessage(int type, int level, String charname)
public static Packet marriageMessage(int type, String charname)
public static Packet jobMessage(int type, int job, String charname)
public static Packet trembleEffect(int type, int delay)
public static Packet getEnergy(String info, int amount)
public static Packet dojoWarpUp()
public static Packet itemExpired(int itemid)
public static Packet MobDamageMobFriendly(Monster mob, int damage, int remainingHp)
public static Packet shopErrorMessage(int error, int type)
public static Packet finishedSort(int inv)
public static Packet finishedSort2(int inv)
public static Packet bunnyPacket()
public static Packet hpqMessage(String text)
public static Packet showEventInstructions()
public static Packet leftKnockBack()
public static Packet rollSnowBall(boolean entermap, int state, Snowball ball0, Snowball ball1)
public static Packet hitSnowBall(int what, int damage)
public static Packet snowballMessage(int team, int message)
public static Packet coconutScore(int team1, int team2)
public static Packet hitCoconut(boolean spawn, int id, int type)
public static Packet customPacket(String packet)
public static Packet customPacket(byte[] packet)
public static Packet spawnGuide(boolean spawn)
public static Packet talkGuide(String talk)
public static Packet guideHint(int hint)
public static void addCashItemInformation(OutPacket p, Item item, int accountId)
public static void addCashItemInformation(OutPacket p, Item item, int accountId, String giftMessage)
public static Packet showWishList(Character mc, boolean update)
public static Packet showBoughtCashItem(Item item, int accountId)
public static Packet showBoughtCashRing(Item ring, String recipient, int accountId)
public static Packet showCashShopMessage(byte message)
public static Packet showCashInventory(Client c)
public static Packet showGifts(List<Pair<Item, String>> gifts)
public static Packet showGiftSucceed(String to, ModifiedCashItemDO item)
public static Packet showBoughtInventorySlots(int type, short slots)
public static Packet showBoughtStorageSlots(short slots)
public static Packet showBoughtCharacterSlot(short slots)
public static Packet takeFromCashInventory(Item item)
public static Packet deleteCashItem(Item item)
public static Packet refundCashItem(Item item, int maplePoints)
public static Packet putIntoCashInventory(Item item, int accountId)
public static Packet openCashShop(Client c, boolean mts) throws Exception
public static Packet sendVegaScroll(int op)
public static Packet resetForcedStats()
public static Packet showCombo(int count)
public static Packet earnTitleMessage(String msg)
public static Packet CPUpdate(boolean party, int curCP, int totalCP, int team)
public static Packet CPQMessage(byte message)
public static Packet playerSummoned(String name, int tab, int number)
public static Packet playerDiedMessage(String name, int lostCP, int team)
public static Packet startMonsterCarnival(Character chr, int team, int opposition)
public static Packet sheepRanchInfo(byte wolf, byte sheep)
public static Packet sheepRanchClothes(int id, byte clothes)
public static Packet incubatorResult()
public static Packet pyramidGauge(int gauge)
public static Packet pyramidScore(byte score, int exp)
public static Packet spawnDragon(Dragon dragon)
public static Packet moveDragon(Dragon dragon, Point startPos, InPacket movementPacket, long movementDataLength)
public static Packet removeDragon(int chrId)
public static Packet changeBackgroundEffect(boolean remove, int layer, int transition)
public static Packet setNPCScriptable(Map<Integer, String> scriptableNpcIds)
public static Packet familyBuff(int type, int buffnr, int amount, int time)
public static Packet cancelFamilyBuff()
public static Packet UseTreasureBox(int type)
public static Packet updateClientSettings(byte hp, byte mp)
```

### `org.gms.util.Pair`
- 声明: `public class Pair<E, F> {`
- 方法数（启发式提取）: 6

```text
public Pair(E left, F right)
public E getLeft()
public F getRight()
public String toString()
public int hashCode()
public boolean equals(Object obj)
```

### `org.gms.util.Quartet`
- 声明: `public class Quartet<A, B, C, D> {`
- 方法数（启发式提取）: 0

### `org.gms.util.Randomizer`
- 声明: `public class Randomizer {`
- 方法数（启发式提取）: 8

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

### `org.gms.util.RateLimitUtil`
- 声明: `public class RateLimitUtil {`
- 方法数（启发式提取）: 2

```text
public static RateLimitUtil getInstance()
public boolean check(String ip)
```

### `org.gms.util.RequireUtil`
- 声明: `public class RequireUtil {`
- 方法数（启发式提取）: 13

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

### `org.gms.util.StringUtil`
- 声明: `public class StringUtil {`
- 方法数（启发式提取）: 7

```text
public static String getLeftPaddedStr(String in, char padchar, int length)
public static String getRightPaddedStr(String in, char padchar, int length)
public static String joinStringFrom(String[] arr, int start)
public static String joinStringFrom(String[] arr, int start, String sep)
public static String makeEnumHumanReadable(String enumName)
public static int countCharacters(String str, char chr)
public static boolean isNumeric(String str)
```

### `org.gms.util.ThreadLocalUtil`
- 声明: `public class ThreadLocalUtil {`
- 方法数（启发式提取）: 4

```text
public static void setCurrentClient(Client c)
public static Client getCurrentClient()
public static void removeCurrentClient()
public static int getClientLang()
```

### `org.gms.util.Trio`
- 声明: `public class Trio<A, B, C> {`
- 方法数（启发式提取）: 0

## `org.gms.util.packets`

### `org.gms.util.packets.Fishing`
- 声明: `public class Fishing {`
- 方法数（启发式提取）: 3

```text
public static double[] fetchFishingLikelihood()
public static void doFishing(Character chr, int baitLevel, double yearLikelihood, double timeLikelihood)
public static int getRandomItem()
```

### `org.gms.util.packets.WeddingPackets`
- 声明: `public class WeddingPackets extends PacketCreator {`
- 方法数（启发式提取）: 15

```text
public List<String> asWishList = new ArrayList<>()
public int getMarriageStatus()
public int getMarriageRequest()
public int getType()
public int getMap()
public int getItem()
public static Packet onMarriageRequest(String name, int playerid)
public static Packet onTakePhoto(String ReservedGroomName, String ReservedBrideName, int m_dwField, List<Character> m_dwUsers)
public static Packet OnMarriageResult(int marriageId, Character chr, boolean wedding)
public static Packet OnMarriageResult(final byte msg)
public static Packet OnNotifyWeddingPartnerTransfer(int partner, int mapid)
public static Packet OnWeddingProgress(boolean setBlessEffect, int groom, int bride, byte step)
public static Packet sendWeddingInvitation(String groom, String bride)
public static Packet sendWishList()
public static Packet onWeddingGiftResult(byte mode, List<String> itemnames, List<Item> items)
```
