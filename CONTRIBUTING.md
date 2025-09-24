# Created by 954860224@qq.com
# 贡献指南

感谢您对 bongobot 项目的兴趣！我们欢迎各种形式的贡献。

## 贡献方式

### 🐛 报告 Bug

如果您发现了 bug，请：

1. 检查 [Issues](https://github.com/Gorjess/bongobot/issues) 确认问题未被报告
2. 使用 Bug 报告模板创建新 issue
3. 提供详细的复现步骤和环境信息

### 💡 功能建议

如果您有新功能的想法：

1. 先在 [Discussions](https://github.com/Gorjess/bongobot/discussions) 讨论
2. 创建 Feature Request issue
3. 详细描述功能需求和使用场景

### 🔧 代码贡献

#### 开发环境设置

1. **Fork 项目**
   ```bash
   # 在 GitHub 上 fork 项目，然后克隆
   git clone https://github.com/YOUR_USERNAME/bongobot.git
   cd bongobot
   ```

2. **设置开发环境**
   ```bash
   # 创建虚拟环境
   python -m venv venv
   
   # 激活虚拟环境
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   
   # 安装依赖
   pip install -r requirements.txt
   pip install -e .[dev]  # 安装开发依赖
   ```

3. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-fix-name
   ```

#### 代码规范

1. **Python 代码风格**
   - 遵循 PEP 8 规范
   - 使用 Black 进行代码格式化
   - 使用 flake8 进行代码检查

   ```bash
   # 格式化代码
   black bongobot/
   
   # 检查代码风格
   flake8 bongobot/
   
   # 类型检查
   mypy bongobot/
   ```

2. **注释和文档**
   - 所有公共函数和类都需要文档字符串
   - 使用中文注释（项目主要面向中文用户）
   - 复杂逻辑需要详细注释

3. **文件头部**
   - 所有新文件都需要添加创建信息：
   ```python
   # Created by 954860224@qq.com
   ```

#### 测试

1. **运行测试**
   ```bash
   # 运行所有测试
   pytest
   
   # 运行覆盖率测试
   pytest --cov=bongobot
   
   # 运行特定测试
   pytest tests/test_config_loader.py
   ```

2. **编写测试**
   - 新功能必须包含测试
   - 测试文件命名：`test_*.py`
   - 测试类命名：`Test*`
   - 测试函数命名：`test_*`

#### 提交规范

1. **提交信息格式**
   ```
   type(scope): description
   
   [optional body]
   
   [optional footer]
   ```

   类型（type）：
   - `feat`: 新功能
   - `fix`: 修复 bug
   - `docs`: 文档更新
   - `style`: 代码格式（不影响功能）
   - `refactor`: 重构
   - `test`: 测试相关
   - `chore`: 构建过程或辅助工具的变动

   示例：
   ```
   feat(clicker): add image template caching
   
   - Cache loaded templates to improve performance
   - Add cache size limit configuration
   - Update documentation
   
   Closes #123
   ```

2. **提交前检查**
   ```bash
   # 运行完整检查
   black bongobot/
   flake8 bongobot/
   mypy bongobot/
   pytest
   ```

#### Pull Request 流程

1. **创建 PR**
   - 确保分支是最新的
   - 填写 PR 模板
   - 关联相关 issues

2. **PR 要求**
   - 通过所有 CI 检查
   - 代码覆盖率不能降低
   - 至少一个 reviewer 的批准
   - 所有讨论都已解决

3. **合并**
   - 使用 "Squash and merge"
   - 保持主分支历史清洁

## 开发指导

### 项目架构

```
bongobot/
├── __init__.py         # 包入口，版本信息
├── __main__.py         # 模块入口点
├── main.py            # 主程序入口
├── config_loader.py   # 配置加载
├── logger_setup.py    # 日志设置
├── runner.py          # 主运行逻辑
├── automation.py      # 自动化操作
└── idle.py           # 空闲检测
```

### 核心组件

1. **配置系统**（config_loader.py）
   - 支持 YAML 格式
   - 默认配置 + 用户配置合并
   - 配置验证

2. **日志系统**（logger_setup.py）
   - 支持多级别日志
   - 控制台和文件输出
   - 结构化日志格式

3. **空闲检测**（idle.py）
   - 系统活动监控
   - 可配置检测间隔
   - 跨平台兼容

4. **自动化操作**（automation.py）
   - 键盘输入模拟
   - 图像识别和点击
   - 操作队列管理

5. **主运行循环**（runner.py）
   - 协调各个组件
   - 异常处理和恢复
   - 优雅关闭

### 添加新功能

1. **新的自动化操作**
   - 在 `automation.py` 中添加新类
   - 继承基础操作类
   - 实现必需的接口方法

2. **新的配置选项**
   - 在默认配置中添加选项
   - 更新配置验证逻辑
   - 添加文档说明

3. **新的检测策略**
   - 在 `idle.py` 中添加检测器
   - 实现统一的检测接口
   - 考虑跨平台兼容性

## 发布流程

1. **版本号更新**
   - 更新 `bongobot/__init__.py` 中的 `__version__`
   - 更新 `pyproject.toml` 中的版本
   - 遵循语义化版本控制

2. **更新文档**
   - 更新 CHANGELOG.md
   - 检查 README.md 的准确性
   - 更新 docs/ 目录下的文档

3. **测试验证**
   - 运行完整测试套件
   - 在不同环境中测试
   - 验证安装包功能

4. **创建发布**
   - 创建 Git tag
   - 编写发布说明
   - 上传到 PyPI

## 社区准则

### 行为准则

- 保持友善和专业
- 尊重不同观点
- 建设性的反馈
- 帮助新贡献者

### 沟通渠道

- **GitHub Issues**: Bug 报告和功能请求
- **GitHub Discussions**: 一般讨论和问答
- **Pull Requests**: 代码审查和讨论
- **Email**: 954860224@qq.com（紧急事务）

### 认可贡献者

- 所有贡献者都会在 README.md 中得到认可
- 重大贡献者可以获得项目维护权限
- 优秀的贡献会在发布说明中特别提及

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。

## 问题和帮助

如果您在贡献过程中遇到任何问题，请随时：

1. 查看现有的 Issues 和 Discussions
2. 创建新的 Discussion 询问
3. 发送邮件到 954860224@qq.com

感谢您的贡献！🎉
