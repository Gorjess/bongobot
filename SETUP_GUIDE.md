# Created by 954860224@qq.com
# bongobot 环境设置指南

## 📋 概述

本项目提供了多种环境设置方式，以满足不同用户的需求：

- **新手用户**：使用一键快速设置
- **有经验用户**：使用手动环境设置
- **开发者**：使用完整开发环境

## 🚀 快速开始（推荐）

### 一键设置

```bash
# 克隆项目
git clone https://github.com/Gorjess/bongobot.git
cd bongobot

# 运行快速设置
python quick_setup.py
```

这将自动完成所有设置步骤。

## 🔧 手动设置

### 1. 基础运行环境

适合只想使用程序的用户：

```bash
# 运行环境设置脚本
python scripts/setup_environment.py

# 选择 "1. 基础运行环境"
# 这将安装 requirements.txt 中的依赖
```

### 2. 完整开发环境

适合想要参与开发的用户：

```bash
# 运行环境设置脚本
python scripts/setup_environment.py

# 选择 "2. 完整开发环境"
# 这将安装 requirements-dev.txt 中的所有依赖
```

## 📦 依赖文件说明

### requirements.txt
包含程序运行所需的核心依赖：
- pyautogui（自动化操作）
- opencv-python（图像识别）
- PyYAML（配置文件解析）
- setuptools, wheel（包管理工具）

### requirements-dev.txt
包含开发环境的完整依赖：
- 所有 requirements.txt 的依赖
- pytest（测试框架）
- black, flake8（代码格式化和检查）
- mypy（类型检查）
- sphinx（文档生成）

## 🛠️ 环境检查

### 检查环境状态

```bash
python scripts/check_environment.py
```

这将检查：
- Python 版本
- 虚拟环境状态
- 依赖包安装情况
- 系统权限
- bongobot 安装状态

### 常见问题排查

1. **Python 版本过低**
   ```
   ❌ Python版本过低: 3.7.x
   ```
   解决：安装 Python 3.8 或更高版本

2. **缺少 setuptools**
   ```
   ❌ 未安装: setuptools
   ```
   解决：运行环境设置脚本会自动安装

3. **虚拟环境未激活**
   ```
   ⚠️ 未在虚拟环境中
   ```
   解决：运行 `venv\Scripts\activate`

4. **权限不足**
   ```
   ❌ 权限不足
   ```
   解决：以管理员身份运行或检查目录权限

## 🎯 使用场景

### 普通用户
```bash
# 1. 快速设置
python quick_setup.py

# 2. 激活环境
venv\Scripts\activate

# 3. 运行程序
bongobot
```

### 开发者
```bash
# 1. 选择开发环境
python scripts/setup_environment.py
# 选择选项 2

# 2. 激活环境
venv\Scripts\activate

# 3. 运行测试
pytest

# 4. 格式化代码
black bongobot/

# 5. 检查代码
flake8 bongobot/
```

### CI/CD 环境
```bash
# 自动化安装（无交互）
python -c "
import subprocess
import sys
subprocess.run([sys.executable, 'scripts/setup_environment.py'], input='1\n', text=True)
"
```

## 📁 文件结构

```
bongobot/
├── requirements.txt          # 基础依赖
├── requirements-dev.txt      # 开发依赖
├── quick_setup.py           # 一键设置脚本
├── scripts/
│   ├── setup_environment.py # 环境设置脚本
│   └── check_environment.py # 环境检查脚本
└── SETUP_GUIDE.md          # 本文件
```

## ⚡ 快速命令参考

| 操作 | 命令 |
|------|------|
| 一键设置 | `python quick_setup.py` |
| 手动设置 | `python scripts/setup_environment.py` |
| 环境检查 | `python scripts/check_environment.py` |
| 激活环境 | `venv\Scripts\activate` |
| 退出环境 | `deactivate` |
| 运行程序 | `bongobot` |
| 运行测试 | `pytest` |
| 格式化代码 | `black bongobot/` |

## 🔍 故障排除

### 1. 安装失败

如果自动安装失败，可以手动安装：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 升级工具
pip install --upgrade pip setuptools wheel

# 安装依赖
pip install -r requirements.txt

# 开发环境额外安装
pip install -r requirements-dev.txt
```

### 2. 模块导入错误

```python
ModuleNotFoundError: No module named 'bongobot'
```

解决方案：
1. 确保虚拟环境已激活
2. 在开发模式下安装：`pip install -e .`

### 3. 权限问题

Windows 下可能遇到权限问题：
1. 以管理员身份运行 PowerShell
2. 或者修改执行策略：`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 📞 获取帮助

如果遇到问题：

1. 查看环境检查结果：`python scripts/check_environment.py`
2. 查看详细日志（开发模式）
3. 提交 Issue：https://github.com/Gorjess/bongobot/issues
4. 发送邮件：954860224@qq.com

## 🎉 完成设置后

设置完成后，您可以：

1. **运行程序**：`bongobot`
2. **查看帮助**：`bongobot --help`
3. **编辑配置**：复制 `examples/config.example.yaml` 到 `config.yaml`
4. **查看文档**：阅读 `docs/usage.md`

祝您使用愉快！🎊
