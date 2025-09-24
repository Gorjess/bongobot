# Created by 954860224@qq.com
# 更新日志

本文档记录了 bongobot 闲置模拟器的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### 计划中的功能
- [ ] 图形界面（GUI）支持
- [ ] 多平台支持（Linux, macOS）
- [ ] 更多的点击策略
- [ ] 配置文件热重载

## [1.0.0] - 2025-09-24

### 新增
- 🎯 空闲检测功能
- ⌨️ 随机键盘输入模拟
- 🖱️ 基于模板匹配的图像点击功能
- 🔧 YAML 配置文件支持
- 📝 完整的日志记录系统
- 🚀 命令行界面支持
- 📦 标准 Python 包结构
- 🔄 支持 `python -m bongobot` 调用
- 📋 详细的项目文档

### 配置选项
- `bot.idle_threshold_seconds`: 空闲检测阈值
- `bot.keys`: 可配置的按键列表
- `clicker.enabled`: 点击器开关
- `clicker.template_path`: 模板图片路径
- `clicker.confidence`: 匹配置信度
- `clicker.wait_after_click_seconds`: 点击冷却时间
- `clicker.search_interval_seconds`: 搜索间隔
- `logging.level`: 日志级别
- `logging.write_to_file`: 文件日志开关
- `logging.dir`: 日志目录

### 技术特性
- 基于 OpenCV 的图像识别
- 使用 pyautogui 和 pydirectinput 进行输入模拟
- 支持 Windows 10/11
- Python 3.8+ 兼容性
- MIT 开源许可证

### 文档
- 完整的 README.md 说明文档
- 配置文件示例和说明
- 安装和使用指南
- 开发环境设置说明

---

## 版本说明

### 语义化版本控制
- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能性新增
- **修订号**：向下兼容的问题修正

### 更新类型
- **新增**：新功能
- **变更**：对现有功能的变更
- **废弃**：不再建议使用的功能
- **移除**：已删除的功能
- **修复**：问题修复
- **安全**：安全相关的修复
