# gms-server 逐符号中文职责 · 分卷 `exception`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：8

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

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
