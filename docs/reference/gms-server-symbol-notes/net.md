# gms-server 逐符号中文职责 · 分卷 `net`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：296

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

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
