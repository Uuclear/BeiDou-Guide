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

## 评审

- gms-server 侧采用「包级地图 + 全量 public 方法签名索引」，避免 5000+ 方法手写说明不可维护；ijl15 体量小，采用按文件说明。
- 索引为启发式提取：以 IDE 与源文件为准；非 public 成员未完全覆盖。
