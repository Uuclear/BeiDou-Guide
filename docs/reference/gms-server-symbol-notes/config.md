# gms-server 逐符号中文职责 · 分卷 `config`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：5

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

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
