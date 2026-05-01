# gms-server 逐符号中文职责 · 分卷 `aop`

> 自动生成：`scripts/generate-symbol-notes.py`
> 源码路径：`BeiDou-Server`
> 本分卷 Java 文件数：3

[← 返回分卷索引](../gms-server-symbol-notes-README.md)

---

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
