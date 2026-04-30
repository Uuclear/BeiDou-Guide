# gms-ui 全量符号索引

> 自动生成：`scripts/generate-full-symbol-docs.py`
> 源码路径：`BeiDou-Server`
> TS/Vue 文件数：151

---

## `App.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `api/account.ts`
- export 符号数: 9
- function 声明数: 0
- const 箭头函数数: 0
```text
export RegisterForm
export GMUpdateForm
export getAccountList
export addAccount
export updateAccountByGM
export deleteAccount
export banAccount
export unbanAccount
export resetLoggedIn
```

## `api/autoban.ts`
- export 符号数: 3
- function 声明数: 0
- const 箭头函数数: 0
```text
export AutobanConfigResult
export getAutobanConfigList
export updateAutobanConfig
```

## `api/cashShop.ts`
- export 符号数: 8
- function 声明数: 0
- const 箭头函数数: 0
```text
export conditionState
export cashShopFormState
export batchFormState
export getAllCategoryList
export getCommodityByCategory
export onSale
export offSale
export batchOnSale
```

## `api/command.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export CommandReq
export getCommandList
export updateCommand
export reloadEventsByGMCommand
export reloadPortalsByGMCommand
export reloadMapsByGMCommand
```

## `api/config.ts`
- export 符号数: 10
- function 声明数: 0
- const 箭头函数数: 0
```text
export ConfigSearch
export ConfigResult
export getConfigTypeList
export getConfigList
export addConfig
export updateConfig
export deleteConfig
export deleteConfigList
export importYml
export exportYml
```

## `api/dashboard.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export getServerStatus
export startServer
export stopServer
export restartServer
export shutdown
export getVersion
```

## `api/drop.ts`
- export 符号数: 9
- function 声明数: 0
- const 箭头函数数: 0
```text
export DropConditionState
export getDrop
export updateDrop
export insertDrop
export deleteDrop
export getGlobalDrop
export updateGlobalDrop
export insertGlobalDrop
export deleteGlobalDrop
```

## `api/fileTree.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export FileTreeForm
export ReadForm
export WriteForm
export treeFile
export readFile
export writeFile
```

## `api/gachapon.ts`
- export 符号数: 7
- function 声明数: 0
- const 箭头函数数: 0
```text
export GachaponPoolSearchCondition
export getPools
export updatePool
export deletePool
export getRewards
export updateReward
export deleteReward
```

## `api/information.ts`
- export 符号数: 3
- function 声明数: 0
- const 箭头函数数: 0
```text
export InformationSearch
export InformationResult
export informationSearch
```

## `api/interceptor.ts`
- export 符号数: 1
- function 声明数: 1
- const 箭头函数数: 0
```text
export HttpResponse
function generateUUID(
```

## `api/inventory.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export InventoryCondition
export getInventoryTypeList
export getCharacterList
export getInventoryList
export updateInventory
export deleteInventory
```

## `api/message.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export MessageRecord
export MessageListType
export queryMessageList
export setMessageStatus
export ChatRecord
export queryChatList
```

## `api/npcShop.ts`
- export 符号数: 6
- function 声明数: 0
- const 箭头函数数: 0
```text
export getShopFilter
export getShopList
export getShopItemList
export deleteShopItem
export addShopItem
export updateShopItem
```

## `api/player.ts`
- export 符号数: 4
- function 声明数: 0
- const 箭头函数数: 0
```text
export GiveForm
export getPlayerList
export givePlayerSrc
export getEquInitialInfo
```

## `api/user.ts`
- export 符号数: 8
- function 声明数: 0
- const 箭头函数数: 0
```text
export LoginData
export SubmitBody
export LoginRes
export login
export logout
export getUserInfo
export getMenuList
export refreshToken
```

## `components/breadcrumb/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/chart/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/footer/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/global-setting/block.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 1
```text
const handleChange = (...) =>
```

## `components/global-setting/form-wrapper.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 1
```text
const handleChange = (...) =>
```

## `components/global-setting/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 3
```text
const cancel = (...) =>
const copySettings = (...) =>
const setVisible = (...) =>
```

## `components/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/menu/index.vue`
- export 符号数: 0
- function 声明数: 1
- const 箭头函数数: 5
```text
function travel(
const goto = (...) =>
const findMenuOpenKeys = (...) =>
const backtrack = (...) =>
const setCollapse = (...) =>
const renderSubMenu = (...) =>
```

## `components/menu/use-menu-tree.ts`
- export 符号数: 1
- function 声明数: 1
- const 箭头函数数: 0
```text
export useMenuTree
function travel(
```

## `components/message-box/index.vue`
- export 符号数: 0
- function 声明数: 2
- const 箭头函数数: 4
```text
function fetchSourceData(
function readMessage(
const getUnreadList = (...) =>
const formatUnreadLength = (...) =>
const handleItemClick = (...) =>
const emptyList = (...) =>
```

## `components/message-box/list.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const allRead = (...) =>
const onItemClick = (...) =>
```

## `components/message-box/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/message-box/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/navbar/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 4
```text
const handleToggleTheme = (...) =>
const handleLogout = (...) =>
const setDropDownVisible = (...) =>
const loadVersion = (...) =>
```

## `components/tab-bar/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `components/tab-bar/tab-item.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 4
```text
const goto = (...) =>
const tagClose = (...) =>
const findCurrentRouteIndex = (...) =>
const actionSelect = (...) =>
```

## `directive/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `directive/permission/index.ts`
- export 符号数: 0
- function 声明数: 1
- const 箭头函数数: 0
```text
function checkPermission(
```

## `env.d.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `hooks/chart-option.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export useChartOption
```

## `hooks/loading.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 3
```text
export useLoading
const handleRefreshToken = (...) =>
const setLoading = (...) =>
const toggle = (...) =>
```

## `hooks/locale.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 1
```text
export useLocale
const changeLocale = (...) =>
```

## `hooks/permission.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export usePermission
```

## `hooks/request.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export useRequest
```

## `hooks/responsive.ts`
- export 符号数: 1
- function 声明数: 2
- const 箭头函数数: 0
```text
export useResponsive
function queryDevice(
function resizeHandler(
```

## `hooks/themes.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export useThemes
```

## `hooks/user.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 1
```text
export useUser
const logout = (...) =>
```

## `hooks/visible.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 2
```text
export useVisible
const setVisible = (...) =>
const toggle = (...) =>
```

## `layout/default-layout.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const setCollapsed = (...) =>
const drawerCancel = (...) =>
```

## `layout/page-layout.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `locale/en-US/base.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `locale/index.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export LOCALE_OPTIONS
```

## `locale/zh-CN/base.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `main.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `mock/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `mock/message-box.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 1
```text
const getMessageList = (...) =>
```

## `mock/user.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/app-menus/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/constants.ts`
- export 符号数: 5
- function 声明数: 0
- const 箭头函数数: 0
```text
export WHITE_LIST
export NOT_FOUND
export REDIRECT_ROUTE_NAME
export DEFAULT_ROUTE_NAME
export DEFAULT_ROUTE
```

## `router/guard/index.ts`
- export 符号数: 1
- function 声明数: 1
- const 箭头函数数: 0
```text
export createRouteGuard
function setupPageGuard(
```

## `router/guard/permission.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export setupPermissionGuard
```

## `router/guard/userLoginInfo.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export setupUserLoginInfoGuard
```

## `router/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/base.ts`
- export 符号数: 3
- function 声明数: 0
- const 箭头函数数: 0
```text
export DEFAULT_LAYOUT
export REDIRECT_MAIN
export NOT_FOUND_ROUTE
```

## `router/routes/externalModules/arco.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/externalModules/beidou.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/index.ts`
- export 符号数: 2
- function 声明数: 1
- const 箭头函数数: 0
```text
export appRoutes
export appExternalRoutes
function formatModules(
```

## `router/routes/modules/account.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/modules/dashboard.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/modules/game.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `router/routes/types.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export Component
export AppRouteRecordRaw
```

## `router/typings.d.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `store/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `store/modules/account/types.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export AccountState
```

## `store/modules/app/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `store/modules/app/types.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export AppState
```

## `store/modules/cashShop/type.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export categoryState
export cashShopState
```

## `store/modules/drop/type.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export DropState
```

## `store/modules/gachapon/type.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export GachaponPoolState
export GachaponRewardState
```

## `store/modules/inventory/type.ts`
- export 符号数: 3
- function 声明数: 0
- const 箭头函数数: 0
```text
export InventoryTypeState
export InventoryEquipmentState
export InventoryState
```

## `store/modules/npcShop/type.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export NpcShopState
export NpcShopItemState
```

## `store/modules/tab-bar/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `store/modules/tab-bar/types.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export TagProps
export TabBarState
```

## `store/modules/user/index.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `store/modules/user/types.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export RoleType
export UserState
```

## `store/page.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export PageState
```

## `types/echarts.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export ToolTipFormatterParams
```

## `types/global.ts`
- export 符号数: 8
- function 声明数: 0
- const 箭头函数数: 0
```text
export AnyObject
export Options
export NodeOptions
export GetParams
export PostData
export Pagination
export TimeRanger
export GeneralChart
```

## `types/mock.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export MockParams
```

## `utils/auth.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 4
```text
const isLogin = (...) =>
const getToken = (...) =>
const setToken = (...) =>
const clearToken = (...) =>
```

## `utils/env.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `utils/event.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export addEventListen
export removeEventListen
```

## `utils/index.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export openWindow
export regexUrl
```

## `utils/is.ts`
- export 符号数: 13
- function 声明数: 0
- const 箭头函数数: 0
```text
export isArray
export isObject
export isString
export isNumber
export isRegExp
export isFile
export isBlob
export isUndefined
export isNull
export isFunction
export isEmptyObject
export isExist
export isWindow
```

## `utils/mapleStoryAPI.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export getIconUrl
export nothing
```

## `utils/monitor.ts`
- export 符号数: 1
- function 声明数: 0
- const 箭头函数数: 0
```text
export handleError
```

## `utils/route-listener.ts`
- export 符号数: 3
- function 声明数: 0
- const 箭头函数数: 0
```text
export setRouteEmitter
export listenerRouteChange
export removeRouteListener
```

## `utils/setup-mock.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export successResponseWrap
export failResponseWrap
```

## `utils/stringUtils.ts`
- export 符号数: 2
- function 声明数: 0
- const 箭头函数数: 0
```text
export isValidString
export timestampToChineseTime
```

## `views/account/list/addForm.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const init = (...) =>
const submitClick = (...) =>
```

## `views/account/list/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 11
```text
const loadData = (...) =>
const pageChange = (...) =>
const pageSizeChange = (...) =>
const resetClick = (...) =>
const addClick = (...) =>
const editClick = (...) =>
const restLoggedInClick = (...) =>
const banClick = (...) =>
const unbanClick = (...) =>
const submitBanClick = (...) =>
const deleteClick = (...) =>
```

## `views/account/list/updateForm.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const init = (...) =>
const submitClick = (...) =>
```

## `views/account/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/account/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/account/player/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 9
```text
const loadData = (...) =>
const refreshClick = (...) =>
const pageChange = (...) =>
const pageSizeChange = (...) =>
const resetClick = (...) =>
const globalGiveClick = (...) =>
const giveClick = (...) =>
const submitClick = (...) =>
const itemChanged = (...) =>
```

## `views/dashboard/informationSearch/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 4
```text
const getImg = (...) =>
const searchData = (...) =>
const resetSearch = (...) =>
const getTag = (...) =>
```

## `views/dashboard/informationSearch/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/dashboard/informationSearch/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/dashboard/workplace/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 8
```text
const loadSeverStatus = (...) =>
const handleButtonClick = (...) =>
const handleShutdownConfirm = (...) =>
const handleShutdownCancel = (...) =>
const handleRestartConfirm = (...) =>
const handleRestartCancel = (...) =>
const handleStopConfigOk = (...) =>
const handleStopConfigCancel = (...) =>
```

## `views/dashboard/workplace/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/dashboard/workplace/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/dashboard/workplace/mock.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 1
```text
const getLineData = (...) =>
```

## `views/game/autoban/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const loadConfigs = (...) =>
const saveClick = (...) =>
```

## `views/game/autoban/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/autoban/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/cashShop/form.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 3
```text
const handleBeforeOk = (...) =>
const handleCancel = (...) =>
const initForm = (...) =>
```

## `views/game/cashShop/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 3
```text
const topCategoryChange = (...) =>
const subCategoryChange = (...) =>
const loadCategories = (...) =>
```

## `views/game/cashShop/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/cashShop/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/cashShop/table.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 6
```text
const pageChange = (...) =>
const loadData = (...) =>
const changeOnSaleFilter = (...) =>
const editClick = (...) =>
const showBatchForm = (...) =>
const handleBatchFormBeforeOk = (...) =>
```

## `views/game/commandInfo/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 9
```text
const loadCommands = (...) =>
const pageChange = (...) =>
const pageSizeChange = (...) =>
const searchData = (...) =>
const resetSearch = (...) =>
const levelChange = (...) =>
const uptClick = (...) =>
const editOk = (...) =>
const resetEditData = (...) =>
```

## `views/game/commandInfo/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/commandInfo/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/config/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 22
```text
const loadTypes = (...) =>
const transI18nType = (...) =>
const transI18nClz = (...) =>
const getClzType = (...) =>
const loadConfigs = (...) =>
const pageChange = (...) =>
const pageSizeChange = (...) =>
const searchData = (...) =>
const resetSearch = (...) =>
const typeChange = (...) =>
const subTypeChange = (...) =>
const addClick = (...) =>
const delClick = (...) =>
const uptClick = (...) =>
const editOk = (...) =>
const resetEditData = (...) =>
const confirmOk = (...) =>
const importClick = (...) =>
const importOk = (...) =>
const customRequest = (...) =>
const uploadSuccess = (...) =>
const exportClick = (...) =>
```

## `views/game/config/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/config/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/drop/global.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 10
```text
const pageChange = (...) =>
const pageSizeChange = (...) =>
const loadData = (...) =>
const resetClick = (...) =>
const filterItemClick = (...) =>
const editClick = (...) =>
const cancelEditClick = (...) =>
const saveClick = (...) =>
const deleteClick = (...) =>
const insertClick = (...) =>
```

## `views/game/drop/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 11
```text
const pageChange = (...) =>
const pageSizeChange = (...) =>
const loadData = (...) =>
const resetClick = (...) =>
const filterMobClick = (...) =>
const filterItemClick = (...) =>
const editClick = (...) =>
const cancelEditClick = (...) =>
const saveClick = (...) =>
const deleteClick = (...) =>
const insertClick = (...) =>
```

## `views/game/drop/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/drop/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/file/index.vue`
- export 符号数: 0
- function 声明数: 6
- const 箭头函数数: 0
```text
function onEditorMount(
function registerCodeCompletion(
function onTreeSelectFile(
function onTreeSelectDiretory(
function onEditorTextChange(
function treeRoot(
```

## `views/game/gachapon/form.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 6
```text
const handleBeforeOk = (...) =>
const handleCancel = (...) =>
const loadData = (...) =>
const initForm = (...) =>
const calcRealProb = (...) =>
const formatter = (...) =>
```

## `views/game/gachapon/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 9
```text
const pageChange = (...) =>
const pageSizeChange = (...) =>
const loadData = (...) =>
const resetClick = (...) =>
const gachaponIdClick = (...) =>
const deleteClick = (...) =>
const insertClick = (...) =>
const editClick = (...) =>
const showRewardFormClick = (...) =>
```

## `views/game/gachapon/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/gachapon/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/gachapon/reward.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 5
```text
const initForm = (...) =>
const loadData = (...) =>
const saveClick = (...) =>
const insertClick = (...) =>
const deleteClick = (...) =>
```

## `views/game/inventory/InventoryUI.vue`
- export 符号数: 0
- function 声明数: 2
- const 箭头函数数: 4
```text
function getFromCacheOrDownload(
function calculatePositionOffsets(
const fetchInventoryData = (...) =>
const drawInventory = (...) =>
const handleMouseMove = (...) =>
const handleMouseLeave = (...) =>
```

## `views/game/inventory/characterSelector.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 3
```text
const openSelector = (...) =>
const searchClick = (...) =>
const selectClick = (...) =>
```

## `views/game/inventory/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 6
```text
const loadType = (...) =>
const tabChange = (...) =>
const useCharacter = (...) =>
const openInventoryUI = (...) =>
const handleOk = (...) =>
const handleCancel = (...) =>
```

## `views/game/inventory/inventoryEquipForm.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 3
```text
const handleBeforeOk = (...) =>
const handleCancel = (...) =>
const initForm = (...) =>
```

## `views/game/inventory/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/inventory/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/inventory/table.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 4
```text
const loadData = (...) =>
const saveClick = (...) =>
const deleteClick = (...) =>
const editClick = (...) =>
```

## `views/game/npcShop/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 11
```text
const pageChange = (...) =>
const pageSizeChange = (...) =>
const loadClick = (...) =>
const resetClick = (...) =>
const loadShopList = (...) =>
const showShopItemClick = (...) =>
const loadShopItemList = (...) =>
const insertItemClick = (...) =>
const saveClick = (...) =>
const deleteClick = (...) =>
const rollbackClick = (...) =>
```

## `views/game/npcShop/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/game/npcShop/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/login/components/login-form.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 2
```text
const handleSubmit = (...) =>
const setRememberPassword = (...) =>
```

## `views/login/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/login/locale/en-US.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/login/locale/zh-CN.ts`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0

## `views/not-found/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 1
```text
const back = (...) =>
```

## `views/redirect/index.vue`
- export 符号数: 0
- function 声明数: 0
- const 箭头函数数: 0
