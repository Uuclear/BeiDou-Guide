# gms-server 逐符号中文职责 · 分卷 `provider`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：15

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

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
