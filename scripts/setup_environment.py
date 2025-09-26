# Created by 954860224@qq.com
"""
bongobot 环境设置脚本
用于创建虚拟环境和安装依赖
"""
import sys
import os
import subprocess
import platform
from pathlib import Path


def print_header(title: str) -> None:
    """打印标题头"""
    print("=" * 50)
    print(f" {title}")
    print("=" * 50)


def check_python_version() -> bool:
    """检查Python版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python版本过低: {version.major}.{version.minor}")
        print("请安装 Python 3.8 或更高版本")
        return False
    
    print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro}")
    return True


def create_virtual_environment() -> bool:
    """创建虚拟环境"""
    print("\n📦 创建虚拟环境...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        # 检查虚拟环境是否完整
        pip_path = venv_path / "Scripts" / "pip.exe"
        if pip_path.exists():
            print("⚠️  虚拟环境已存在，跳过创建")
            return True
        else:
            print("⚠️  虚拟环境不完整，重新创建...")
            try:
                import shutil
                shutil.rmtree(venv_path)
            except Exception as e:
                print(f"⚠️  删除旧虚拟环境失败: {e}")
                print("请手动删除venv目录后重试")
                return False
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], 
                      check=True, capture_output=True, text=True)
        print("✅ 虚拟环境创建成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 创建虚拟环境失败: {e}")
        return False


def get_activation_command() -> str:
    """获取虚拟环境激活命令"""
    if platform.system() == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"


def install_dependencies(dev_mode: bool = False) -> bool:
    """安装依赖"""
    mode_text = "开发环境" if dev_mode else "基础运行"
    print(f"\n📚 安装{mode_text}依赖包...")
    
    # 确定pip路径
    if platform.system() == "Windows":
        pip_path = Path("venv/Scripts/pip.exe")
    else:
        pip_path = Path("venv/bin/pip")
    
    if not pip_path.exists():
        print(f"❌ 找不到pip: {pip_path}")
        return False
    
    # 升级pip和基础工具
    try:
        print("⬆️  升级pip和基础工具...")
        subprocess.run([str(pip_path), "install", "--upgrade", "pip", "setuptools", "wheel"], 
                      check=True, capture_output=True, text=True)
        print("✅ pip和基础工具已升级")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  升级失败: {e}")
    
    # 选择要安装的依赖文件
    if dev_mode:
        requirements_file = Path("requirements-dev.txt")
        if not requirements_file.exists():
            print("⚠️  找不到requirements-dev.txt，回退到基础依赖")
            requirements_file = Path("requirements.txt")
    else:
        requirements_file = Path("requirements.txt")
    
    if not requirements_file.exists():
        print("❌ 找不到依赖文件")
        return False
    
    try:
        print(f"📦 安装依赖: {requirements_file.name}")
        # 添加详细输出，不隐藏安装过程
        result = subprocess.run([str(pip_path), "install", "-r", str(requirements_file), "-v"], 
                              check=True, text=True)
        print("✅ 依赖包安装成功")
        
        # 如果是开发模式，还要安装当前包为可编辑模式
        if dev_mode:
            try:
                print("🔧 安装当前包为开发模式...")
                subprocess.run([str(pip_path), "install", "-e", ".", "-v"], 
                              check=True, text=True)
                print("✅ 开发模式安装成功")
            except subprocess.CalledProcessError as e:
                print(f"⚠️  开发模式安装失败: {e}")
                print("尝试不使用-e参数安装...")
                try:
                    subprocess.run([str(pip_path), "install", "."], 
                                  check=True, text=True)
                    print("✅ 包安装成功")
                except subprocess.CalledProcessError as e2:
                    print(f"❌ 包安装也失败: {e2}")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 安装依赖失败: {e}")
        print("尝试逐个安装核心依赖...")
        
        # 尝试逐个安装核心依赖
        core_packages = [
            "pyautogui>=0.9.54",
            "pydirectinput>=1.0.4", 
            "pywin32>=311",
            "opencv-python>=4.8.0",
            "numpy>=1.24.0",
            "Pillow>=11.0.0",
            "PyYAML>=6.0.0"
        ]
        
        failed_packages = []
        for package in core_packages:
            try:
                print(f"  安装 {package}...")
                subprocess.run([str(pip_path), "install", package], 
                              check=True, capture_output=True, text=True)
                print(f"  ✅ {package} 安装成功")
            except subprocess.CalledProcessError:
                print(f"  ❌ {package} 安装失败")
                failed_packages.append(package)
        
        if failed_packages:
            print(f"❌ 以下包安装失败: {failed_packages}")
            return False
        else:
            print("✅ 核心依赖安装完成")
            return True


def print_usage_instructions() -> None:
    """打印使用说明"""
    activation_cmd = get_activation_command()
    
    print("\n" + "=" * 50)
    print(" 🎉 环境设置完成!")
    print("=" * 50)
    print("\n📋 使用说明:")
    print(f"1. 激活虚拟环境: {activation_cmd}")
    print("2. 安装bongobot包: python -m pip install -e .")
    print("3. 运行程序: bongobot")
    print("4. 或者: python -m bongobot")
    print("5. 退出虚拟环境: deactivate")
    print("\n💡 提示: 每次使用前都需要先激活虚拟环境")


def main() -> None:
    """主函数"""
    print_header("bongobot 环境设置")
    
    # 检查Python版本
    if not check_python_version():
        input("\n按回车键退出...")
        sys.exit(1)
    
    # 询问安装模式
    print("\n🤔 请选择安装模式:")
    print("1. 基础运行环境（仅安装运行所需依赖）")
    print("2. 完整开发环境（包含测试、格式化工具等）")
    
    while True:
        choice = input("\n请输入选择 (1/2) [默认: 1]: ").strip()
        if choice == "" or choice == "1":
            dev_mode = False
            break
        elif choice == "2":
            dev_mode = True
            break
        else:
            print("❌ 无效选择，请输入 1 或 2")
    
    # 创建虚拟环境
    if not create_virtual_environment():
        input("\n按回车键退出...")
        sys.exit(1)
    
    # 安装依赖
    if not install_dependencies(dev_mode):
        input("\n按回车键退出...")
        sys.exit(1)
    
    # 打印使用说明
    print_usage_instructions()
    
    if dev_mode:
        print("\n🛠️  开发环境设置完成！")
        print("额外可用命令:")
        print("- 运行测试: pytest")
        print("- 代码格式化: black bongobot/")
        print("- 代码检查: flake8 bongobot/")
        print("- 类型检查: mypy bongobot/")
    
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
