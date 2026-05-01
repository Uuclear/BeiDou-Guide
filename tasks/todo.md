# 任务记录

## 本次（文档加深）

- [x] 头脑风暴：区分「叙述性架构」与「全量符号文档」的可维护边界
- [x] 计划：新增深度导读、ijl15 逐文件说明、gms-server 自动生成索引脚本
- [x] 执行：撰写 `docs/09`、`docs/10`、脚本、`docs/reference/gms-server-api-index.md`、更新 `README`、`.gitignore`
- [x] 验证：本地运行生成脚本，检查索引头部与抽样段落

## 可选后续

- [ ] 在 CI 中定期用上游 tag 重跑 `generate-gms-server-api-index.py` 并附 commit SHA
- [ ] 为 `gms-ui` 增加类似的「页面/接口」索引脚本
- [x] gms-server 逐符号中文职责按 `org/gms` 一级目录分卷（`gms-server-symbol-notes-README.md` + `gms-server-symbol-notes/`）
- [x] 12-源码模块精读：补充 REST 全链路（Security、JWT、Controller、Service、与游戏进程交界）
- [x] 12-源码模块精读：游戏登录链（LoginPasswordHandler、Client.login、finishLogin、SessionCoordinator、Server.registerLoginState）
- [x] 12-源码模块精读：PlayerLoggedinHandler 与 CharacterService.loadCharFromDB、进频道时序
- [x] 12-源码模块精读：Channel、PlayerStorage、MapleMap.addPlayer/removePlayer 与可见性
- [x] 12-源码模块精读：setCharacteridInTransition / setCharacterOnSessionTransitionState 调用链
- [x] 12-源码模块精读：Character.changeMap 与 Portal（ChangeMapHandler、GenericPortal、changeMapInternal）
- [x] GitHub Pages：MkDocs 导航分组、阅读指引页、排版样式（extra.css）、首页强化分层说明
- [x] 12-源码模块精读：getInetSocket / getServerIP / getChannelChange（端口推导、包体字段）
- [x] 12-源码模块精读：PLAYER_LOGGEDIN / PLAYER_MAP_TRANSFER 与 mapTransitioning / setMapTransitionComplete
- [x] 12-源码模块精读：CHANGE_MAP（0x26）收包字段与 ChangeMapHandler 分支
- [x] 12-源码模块精读：MOVE_PLAYER（0x29）、AbstractMovementPacketHandler、setChasing 与 SET_FIELD
- [x] 12-源码模块精读：AbstractDealDamageHandler、攻击框、teleport/movement 距离上下文与 DISTANCE_HACK
- [x] 12-源码模块精读：召唤兽 MOVE_SUMMON / SUMMON_ATTACK / DAMAGE_SUMMON 与 MapleMap.spawnSummon
- [x] 12-源码模块精读：ITEM_PICKUP、MapItem 归属、spawnItemDrop 与 pickItemDrop
- [x] 12-源码模块精读：MobLootEntry、use_spawn_loot_on_animation、dropFromMonster 与 dropItemsFromMonster
- [x] 12-源码模块精读：killMonster、killBy、takenDamage 与 dropOwner
- [x] 12-源码模块精读：distributeExperience、组队分摊、giveExpToCharacter 与白字判定
- [x] 12-源码模块精读：gainExp、gainExpInternal、levelUp 与 getMaxLevel
- [x] 12-源码模块精读：StatEffect.applyTo、applyBuffEffect、registerEffect、reapplyLocalStats / recalcLocalStats
- [x] 12-源码模块精读：cancelEffect、buffExpireTask、PlayerBuffStorage、silentGiveBuffs 与登入还原

## 评审

- gms-server 侧采用「包级地图 + 全量 public 方法签名索引」，避免 5000+ 方法手写说明不可维护；ijl15 体量小，采用按文件说明。
- 索引为启发式提取：以 IDE 与源文件为准；非 public 成员未完全覆盖。
