# BongoCat 智能闲置模拟器 🐱

> ⚖️ 合规与免责声明（重要）
>
> 本工具仅用于办公/演示/测试等非对抗场景的防空闲与自动化。严禁用于任何游戏（含 Steam/BongoCat 等）的挂机、刷点、自动开箱或绕过交互等用途。此类行为可能违反平台或游戏条款并带来封禁/法律风险，使用者需自行承担全部后果。作者与贡献者不为误用负责。

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows/)

**Language / 语言**: [🇺🇸 English](README.md) | [🇨🇳 中文](README.zh-CN.md)

</div>

一个智能的自动化工具，用于防止系统进入空闲状态。当检测到用户停止操作时，自动模拟键盘输入和鼠标点击，保持系统活跃状态。

## ✨ 特性

- 🎯 **检测**：自动检测用户是否处于空闲状态
- ⌨️ **键盘模拟**：模拟随机键盘输入，避免触发系统快捷键
- 🖱️ **图像识别点击**：基于模板匹配的点击功能
- 🔧 **高度可配置**：支持自定义所有参数
- 📝 **详细日志**：完整的操作日志记录
- 🚀 **轻量级**：资源占用极低，后台静默运行

## 🚀 快速开始

### 环境要求

- **Python**: 3.8 或更高版本
- **操作系统**: Windows 10/11
- **依赖管理**: pip（Python包管理器）

### 安装方式

#### 方式一：一键快速设置（推荐新手）

```bash
# 1. 克隆项目
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 2. 运行快速设置脚本
python quick_setup.py
```

#### 方式二：手动环境设置

```bash
# 1. 克隆项目
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 2. 运行环境设置脚本
python scripts/setup_environment.py

# 3. 激活虚拟环境
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. 验证安装
bongobot --help
```

#### 方式三：使用 pip 直接安装（发布后可用）

```bash
pip install bongobot
```

#### 方式四：开发者模式

```bash
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 选择完整开发环境（包含测试工具）
python scripts/setup_environment.py
# 在提示时选择 "2. 完整开发环境"
```

### 基本使用

> 注意：直接运行 `bongobot` 需要先安装（会生成命令行入口）。如果你在源码目录直接测试，尚未安装，可以使用 `python -m bongobot` 方式运行。

1. **命令行直接运行**：
   ```bash
   # 需先安装到当前虚拟环境（推荐可编辑安装）
   # python -m pip install -e .
   bongobot
   ```

2. **作为 Python 模块运行**：
   ```bash
   python -m bongobot
   ```

3. **准备并上传你的模板图（可选）**：
   ```bash
   # 将你自己截取的按钮/区域图片放入 assets/ 目录
   # 推荐 PNG 格式，裁剪到最小可识别区域
   # 然后编辑 config.yaml：
   clicker:
     enabled: true
     template_path: "assets/your_template.png"
     confidence: 0.8
   ```

4. **从源码运行（开发者常用）**：
   ```bash
   # 创建并激活虚拟环境
   python -m venv venv
   venv\Scripts\activate

   # 安装依赖
   python -m pip install -r requirements.txt

   # 可编辑安装（会生成 bongobot 命令）
   python -m pip install -e .

   # 运行
   bongobot            # 或
   python -m bongobot
   ```

3. **使用自定义配置**：
   ```bash
   # 复制示例配置文件
   cp examples/config.example.yaml config.yaml
   # 编辑配置文件后运行
   bongobot
   ```

## ⚙️ 配置说明

程序会自动查找配置文件 `config.yaml`，如果不存在则使用默认配置。

### 配置文件示例

```yaml
bot:
  # 用户连续空闲多久后开始模拟输入（秒）
  idle_threshold_seconds: 5.0
  # 用于累计计数的键集合
  keys: ["a", "s", "d", "w", "q", "e", "space", "j", "k", "l"]

clicker:
  # 是否启用模板图点击器
  enabled: true
  # 目标模板图路径
  template_path: "examples/test_btn.png"
  # 模板匹配置信度(0~1)
  confidence: 0.8
  # 点击成功后的冷却时间（秒）
  wait_after_click_seconds: 8.0
  # 连续查找的间隔（秒）
  search_interval_seconds: 1.0

logging:
  # 日志级别：DEBUG/INFO/WARNING/ERROR
  level: "INFO"
  # 是否写入日志文件
  write_to_file: false
  # 日志目录
  dir: "log"
```

### 主要配置项说明

| 配置项 | 说明 | 推荐值 |
|--------|------|--------|
| `idle_threshold_seconds` | 空闲检测阈值 | 5-10秒 |
| `keys` | 模拟按键列表 | 避免系统快捷键的普通字母 |
| `template_path` | 点击目标图片路径 | 相对或绝对路径 |
| `confidence` | 图像匹配置信度 | 0.75-0.9 |
| `wait_after_click_seconds` | 点击后冷却时间 | 5-15秒 |

## 🎮 使用场景

- **远程办公**：防止电脑因无操作而锁屏
- **游戏挂机**：自动点击游戏中的特定按钮
- **演示展示**：保持屏幕常亮状态
- **系统测试**：模拟用户操作进行压力测试

## 📁 项目结构

```
bongobot/
├── bongobot/              # 主程序包
│   ├── __init__.py        # 包初始化和版本信息
│   ├── __main__.py        # 模块入口点 (python -m bongobot)
│   ├── main.py            # 主程序入口
│   ├── config_loader.py   # 配置文件加载器
│   ├── logger_setup.py    # 日志系统设置
│   ├── runner.py          # 主运行循环逻辑
│   ├── automation.py      # 自动化操作实现
│   └── idle.py            # 空闲状态检测
├── assets/                # 程序资源文件
│   ├── README.md          # 资源文件说明
│   ├── test_btn.png       # 默认模板图片
│   └── __test_btn.png     # 备用模板图片
├── examples/              # 示例和模板文件
│   └── config.example.yaml # 配置文件示例
├── tests/                 # 单元测试
│   ├── __init__.py
│   └── test_config_loader.py
├── docs/                  # 项目文档
│   └── usage.md           # 详细使用指南
├── scripts/               # 环境设置脚本
│   ├── setup_environment.py # 环境配置脚本
│   └── check_environment.py # 环境检查脚本
├── requirements.txt       # 基础依赖列表
├── requirements-dev.txt   # 开发环境依赖
├── setup.py              # 包安装脚本
├── pyproject.toml        # 现代Python项目配置
├── quick_setup.py        # 一键环境设置
├── gamebot.py            # 兼容性启动脚本
└── README.md             # 项目说明文档
```

## 🔧 开发指南

### 环境准备

```bash
# 克隆项目
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 创建虚拟环境
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt
pip install -e .[dev]  # 安装开发依赖
```

### 运行测试

```bash
pytest tests/
```

### 代码格式化

```bash
black bongobot/
flake8 bongobot/
```

## 📋 系统要求

- **操作系统**：Windows 10/11
- **Python 版本**：3.8 或更高
- **依赖库**：
  - pyautogui >= 0.9.54
  - pydirectinput >= 1.0.4
  - pywin32 >= 311
  - opencv-python >= 4.8.0
  - numpy >= 1.24.0
  - Pillow >= 11.0.0
  - PyYAML >= 6.0.0

## ⚠️ 注意事项

1. **管理员权限**：某些情况下可能需要以管理员身份运行
2. **杀毒软件**：可能被误报为恶意软件，请添加白名单
3. **游戏反作弊**：请勿在有反作弊系统的游戏中使用
4. **合规使用**：请遵守相关法律法规和使用条款

## ⚖️ 合规与道德使用（重要）

本项目旨在：
- 在办公/演示/测试等非对抗场景下，避免系统因空闲而锁屏或休眠；
- 用于自动化测试与演示脚本的“保活”辅助工具。

明确禁止的用途：
- 将本项目用于任何网络游戏、单机游戏或在线服务中的“刷点数/挂机/绕过交互”等行为；
- 违反 Steam、游戏开发商（如 BongoCat/BongoCat作者）或平台服务条款的用途；
- 影响其他玩家公平性或破坏游戏经济/排行的行为。

法律与风险提示：
- 使用自动化工具干预游戏进程，可能违反平台与游戏的用户协议，导致封禁、账号处罚或法律风险；
- 任何因不当使用导致的后果由使用者自行承担，作者与贡献者不对误用负责。

推荐的合规描述与使用边界：
- “本工具用于办公与演示场景的防空闲与自动化测试，不适用于任何游戏场景。”
- “请勿在包含反作弊系统或有积分、掉落实时收益的程序中使用。”

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新详情。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- **作者**：GorjessJin
- **邮箱**：954860224@qq.com
- **项目地址**：https://github.com/Gorjess/bongobot

## 🙏 致谢

- 感谢所有贡献者的支持
- 感谢开源社区提供的优秀库
- 特别感谢 bongobot 项目的灵感

---

⭐ 如果这个项目对你有帮助，请给它一个星星！
