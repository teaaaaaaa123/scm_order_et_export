# SCM订单ET导出自动化测试

本项目用于自动化测试SCM系统的订单创建和ET导出流程。

## 功能特性

- 自动登录系统
- 创建定制订单（支持多个版型）
- 填写订单基本信息
- 添加明细并填写量体信息
- 修改定制选项
- 确认下单
- ET导出管理2页面操作

## 环境要求

- Python 3.8+
- Chrome浏览器 147.x
- ChromeDriver 147.x

## 安装依赖

```bash
pip install selenium openpyxl webdriver-manager
```

## 运行方式

```bash
python scm_order_et_export.py
```

## 文件结构

```
Material/
├── scm_order_et_export.py    # 主测试脚本
├── chromedriver-147/         # ChromeDriver
├── config.json               # 配置文件
├── serial_counter.txt        # 流水号计数器
└── requirements.txt          # 依赖清单
```

## 测试流程

1. 登录系统
2. 进入定制下单页面
3. 填写订单信息（客商、客户姓名、交货日期）
4. 保存订单主表（获取生产单号）
5. 循环添加版型明细：
   - 填写明细信息
   - 修改定制选项
   - 填写量体信息
   - 保存明细
6. 返回生产下单管理页面
7. 点击确认下单（处理确认弹窗）
8. 进入ET导出管理2页面
9. 找到订单并完成编辑确认

## 配置说明

### config.json 配置项

| 配置项 | 类型 | 说明 |
|--------|------|------|
| `banxingList` | Array | 版型列表，如 `["1KN001", "6KN368"]` |
| `chimaSize` | String | 尺码，如 `"175"` |
| `fabricWidth` | Number | 面料门幅，如 `74` |
| `customerName` | String | 客商名称 |
| `customerCode` | String | 客商编码 |
| `clientName` | String | 客户姓名 |
| `fabricNo` | String | 面料编号 |
| `liningNo` | String | 里布编号 |
| `color` | String | 颜色 |
| `fabricStyle` | String | 面料风格 |
| `fabricSupply` | String | 面料供应 |
| `sleeveLining` | String | 袖裤里 |
| `fabricPrice` | Number | 面辅料价格 |
| `processingFee` | Number | 加工费 |
| `startSerial` | Number | 开始流水号 |
| `resetSerial` | Boolean | 是否重置流水号 |

### 其他文件

- `serial_counter.txt` - 流水号计数器，自动递增并持久化
- 生产单号在运行时动态获取并存储在内存中

### 版型分类判断

系统根据版型编号自动判断版型类型：

| 版型前缀 | 类型 | 说明 |
|---------|------|------|
| `1KNxxx` | 上衣 | 西装上衣等 |
| `6KNxxx` | 西裤 | 裤子类 |
| `4KNxxx` | 大衣 | 长款外套 |
| `5KNxxx` | 马甲 | 无袖背心类 |

**判断规则：**
- 优先根据完整前缀匹配（如 `1KN`, `6KN`, `4KN`, `5KN`）
- 如果前缀不匹配，则根据第一个字符判断（`1`=上衣, `4`=大衣, `5`=马甲, `6`=西裤）
- 默认类型为 `上衣`

**支持的版型示例：**
- `1KN001` - 上衣
- `6KN368` - 西裤
- `4KN001` - 大衣
- `5KN001` - 马甲
