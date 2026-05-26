# SCM订单导出工具

基于Selenium的SCM订单自动化导出工具，用于自动填写订单信息、添加版型明细、填写量体数据、确认下单并导出ET。

## 环境要求

- Python 3.7+
- Chrome浏览器
- ChromeDriver (版本147)

## 安装依赖

```bash
pip install selenium webdriver-manager
```

## 配置文件

### config.json

主配置文件，包含：

- `loginUrl`: 登录URL
- `username`: 用户名
- `password`: 密码
- `customerCode`: 客商代码
- `chimaSize`: 默认尺码
- `fabricWidth`: 默认门幅
- `fabricNo`: 面料编号
- `fabricStyle`: 面料风格
- `banxingConfigs`: 版型配置列表

### 映射配置.json

包含定制选项和量体部位的映射表，用于：
- 版型属性映射（定制选项）
- 量体部位映射（量体信息）

## 使用方法

1. 修改 `config.json` 配置文件
2. 运行主程序：

```bash
python scm_order_et_export.py
```

## 功能流程

1. **登录** - 自动登录SCM系统
2. **填写订单信息** - 自动填写客商等信息
3. **添加版型明细** - 根据配置添加多个版型
   - 设置面料信息（面料编号、风格、门幅）
   - 修改定制选项
   - 填写量体信息（尺码、落差、调整数据）
4. **保存订单** - 保存主表订单
5. **确认下单** - 在订单列表确认订单
6. **ET导出** - 导航到ET导出管理页面
7. **获取面料耗量** - 每5分钟查询一次，最多5次

## config.json 配置示例

```json
{
  "loginUrl": "https://scm.example.com/login",
  "username": "admin",
  "password": "password",
  "customerCode": "C001",
  "chimaSize": "50",
  "fabricWidth": 74,
  "fabricNo": "ET算料",
  "fabricStyle": "平板",
  "banxingConfigs": [
    {
      "banxing": "1KN003",
      "chimaSize": "50",
      "luocha": "R",
      "fabricWidth": 74,
      "fabricNo": "WDDD2",
      "fabricStyle": "平板",
      "customOptions": {
        "手巾袋": "无",
        "后背": "整里"
      },
      "liangtiData": {
        "fullBust": "+5"
      }
    }
  ]
}
```

## 注意事项

1. 运行前确保Chrome浏览器已安装
2. 确保config.json配置正确
3. 面料耗量查询最多等待25分钟（5分钟 × 5次）
4. 脚本会自动保存流水号到serial_counter.txt
