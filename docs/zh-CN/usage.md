# Created by 954860224@qq.com
# bongobot 使用指南

> ⚖️ 合规与免责声明（重要）
>
> 本工具仅用于办公/演示/测试等非对抗场景的防空闲与自动化。严禁用于任何游戏的挂机、刷点、自动开箱或绕过交互等用途。此类行为可能违反平台或游戏条款并带来封禁/法律风险，使用者需自行承担全部后果。

## 快速开始

### 1. 安装

```bash
# 方式一：从 PyPI 安装（发布后可用）
pip install bongobot

# 方式二：在源码目录安装（开发/本地调试）
python -m pip install -e .
```

### 2. 基本运行

```bash
# 使用默认配置运行（需已安装到当前 venv）
bongobot

# 或者使用模块方式运行（无需安装入口脚本）
python -m bongobot
```

### 3. 自定义配置

```bash
# 复制示例配置
cp examples/config.example.yaml config.yaml

# 编辑配置文件
notepad config.yaml  # Windows
# nano config.yaml   # Linux/Mac

# 准备你的模板图（可选）
# 1) 在 assets/ 目录放入你截取的 PNG 模板，例如 my_btn.png
# 2) 编辑 config.yaml：
# clicker:
#   enabled: true
#   template_path: "assets/my_btn.png"
#   confidence: 0.8

# 使用自定义配置运行（未安装入口脚本也可用）
python -m bongobot
```

## 配置详解

### 基本配置结构

```yaml
bot:
  idle_threshold_seconds: 5.0
  keys: ["a", "s", "d", "w", "q", "e", "space", "j", "k", "l"]

clicker:
  enabled: true
  template_path: "examples/test_btn.png"
  confidence: 0.8
  wait_after_click_seconds: 8.0
  search_interval_seconds: 1.0

logging:
  level: "INFO"
  write_to_file: false
  dir: "log"
```

### 配置项说明

#### bot 部分

- **idle_threshold_seconds**: 空闲检测阈值（秒）
  - 用户停止操作多长时间后开始模拟输入
  - 建议值：5-10秒
  - 过小会频繁触发，过大会延迟响应

- **keys**: 模拟按键列表
  - 程序会随机选择这些按键进行模拟
  - 建议使用不会触发系统快捷键的普通字母
  - 支持特殊键：space、enter、tab等

#### clicker 部分

- **enabled**: 是否启用图像点击功能
  - true：启用模板匹配点击
  - false：仅使用键盘模拟

- **template_path**: 模板图片路径
  - 相对路径或绝对路径
  - 支持格式：PNG、JPG、JPEG
  - 建议使用PNG格式以保证匹配精度
  - 默认资源存放在 `assets/` 目录

- **confidence**: 模板匹配置信度
  - 范围：0.0-1.0
  - 0.8表示80%相似度
  - 过低会误点击，过高会匹配不到

- **wait_after_click_seconds**: 点击后冷却时间
  - 成功点击后等待的时间
  - 避免频繁点击
  - 建议值：5-15秒

- **search_interval_seconds**: 搜索间隔
  - 每次搜索模板的间隔时间
  - 避免高CPU占用
  - 建议值：0.5-2秒

#### logging 部分

- **level**: 日志级别
  - DEBUG：详细调试信息
  - INFO：一般信息（推荐）
  - WARNING：警告信息
  - ERROR：仅错误信息

- **write_to_file**: 是否写入日志文件
  - true：写入文件（调试时使用）
  - false：仅控制台输出（推荐）

- **dir**: 日志文件目录
  - 仅在write_to_file=true时有效

## 使用场景

### 1. 远程办公防锁屏

```yaml
bot:
  idle_threshold_seconds: 30.0  # 30秒空闲后激活
  keys: ["shift"]               # 仅使用Shift键，不会产生输入

clicker:
  enabled: false                # 关闭点击功能

logging:
  level: "WARNING"              # 减少日志输出
```

### 2. 游戏挂机点击

```yaml
bot:
  idle_threshold_seconds: 5.0   # 快速响应
  keys: []                      # 不使用键盘模拟

clicker:
  enabled: true
  template_path: "game_button.png"
  confidence: 0.85              # 提高精度
  wait_after_click_seconds: 10.0
  search_interval_seconds: 0.5  # 快速搜索

logging:
  level: "INFO"
  write_to_file: true           # 记录点击日志
```

### 3. 演示保持屏幕

```yaml
bot:
  idle_threshold_seconds: 60.0  # 1分钟空闲检测
  keys: ["f15"]                 # 使用功能键，不影响演示

clicker:
  enabled: false

logging:
  level: "ERROR"                # 最小日志输出
```

## 高级功能

### 模板图片制作

1. **截图工具**：使用截图工具保存目标按钮
2. **图片编辑**：裁剪到最小识别区域
3. **格式转换**：保存为PNG格式
4. **测试验证**：调整confidence值进行测试

### 多配置管理

```bash
# 为不同场景创建配置文件
config-office.yaml      # 办公场景
config-game.yaml        # 游戏场景
config-presentation.yaml # 演示场景

# 使用环境变量指定配置
set BONGOBOT_CONFIG=config-game.yaml
bongobot
```

### 调试模式

```bash
# 启用详细日志
# 在config.yaml中设置
logging:
  level: "DEBUG"
  write_to_file: true

# 运行程序查看详细日志
bongobot
```

## 常见问题

### Q: 程序没有反应？
A: 检查空闲时间设置，确保超过idle_threshold_seconds

### Q: 点击功能不工作？
A: 
1. 检查模板图片路径是否正确
2. 调整confidence值
3. 确保目标在屏幕可见区域

### Q: 被杀毒软件拦截？
A: 将程序目录添加到杀毒软件白名单

### Q: 权限不足？
A: 以管理员身份运行程序

### Q: 如何停止程序？
A: 按Ctrl+C或关闭命令行窗口

## 安全注意事项

1. **合规使用**：遵守公司和法律规定
2. **游戏规则**：注意游戏反作弊政策
3. **隐私保护**：不要在敏感操作时运行
4. **资源监控**：注意CPU和内存使用

## 技术支持

- **项目地址**：https://github.com/Gorjess/bongobot
- **问题报告**：https://github.com/Gorjess/bongobot/issues
- **邮箱**：954860224@qq.com
