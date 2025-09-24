# Created by 954860224@qq.com
"""
bongobot 环境检查脚本
用于检查系统环境和依赖是否正确安装
"""
import sys
import os
import platform
import subprocess
import importlib
from pathlib import Path
from typing import Dict, List, Tuple


def print_header(title: str) -> None:
    """打印标题头"""
    print("=" * 50)
    print(f" {title}")
    print("=" * 50)


def check_python_info() -> Dict[str, str]:
    """检查Python信息"""
    info = {
        "版本": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "路径": sys.executable,
        "平台": platform.platform(),
        "架构": platform.architecture()[0],
    }
    return info


def check_pip_info() -> Dict[str, str]:
    """检查pip信息"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, check=True)
        pip_version = result.stdout.strip()
        
        # 获取pip路径
        result = subprocess.run([sys.executable, "-m", "pip", "show", "pip"], 
                              capture_output=True, text=True, check=True)
        pip_location = ""
        for line in result.stdout.split('\n'):
            if line.startswith('Location:'):
                pip_location = line.split(':', 1)[1].strip()
                break
        
        return {
            "版本": pip_version,
            "位置": pip_location
        }
    except subprocess.CalledProcessError:
        return {"错误": "pip不可用"}


def check_virtual_environment() -> Dict[str, str]:
    """检查虚拟环境"""
    info = {}
    
    # 检查是否在虚拟环境中
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        info["状态"] = "✅ 已激活虚拟环境"
        info["虚拟环境路径"] = sys.prefix
    else:
        info["状态"] = "⚠️  未在虚拟环境中"
    
    # 检查venv目录是否存在
    venv_path = Path("venv")
    if venv_path.exists():
        info["venv目录"] = "✅ 存在"
    else:
        info["venv目录"] = "❌ 不存在"
    
    return info


def check_required_modules() -> Dict[str, str]:
    """检查必需的模块"""
    required_modules = [
        "pyautogui",
        "pydirectinput", 
        "cv2",
        "numpy",
        "PIL",
        "yaml",
        "win32api"
    ]
    
    results = {}
    for module_name in required_modules:
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, '__version__', '未知版本')
            results[module_name] = f"✅ {version}"
        except ImportError:
            results[module_name] = "❌ 未安装"
    
    return results


def check_system_permissions() -> Dict[str, str]:
    """检查系统权限"""
    info = {}
    
    # 检查当前目录权限
    current_dir = Path.cwd()
    info["当前目录"] = str(current_dir)
    
    # 检查读写权限
    try:
        test_file = current_dir / "test_write_permission.tmp"
        test_file.write_text("test")
        test_file.unlink()
        info["目录权限"] = "✅ 可读写"
    except Exception:
        info["目录权限"] = "❌ 权限不足"
    
    # 检查是否为管理员（仅Windows）
    if platform.system() == "Windows":
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            info["管理员权限"] = "✅ 是" if is_admin else "❌ 否"
        except Exception:
            info["管理员权限"] = "❓ 无法检测"
    
    return info


def check_bongobot_installation() -> Dict[str, str]:
    """检查bongobot安装状态"""
    info = {}
    
    # 检查包目录
    bongobot_path = Path("bongobot")
    if bongobot_path.exists() and bongobot_path.is_dir():
        info["包目录"] = "✅ 存在"
        
        # 检查主要文件
        main_files = ["__init__.py", "main.py", "config_loader.py", "automation.py"]
        for file_name in main_files:
            file_path = bongobot_path / file_name
            if file_path.exists():
                info[f"文件 {file_name}"] = "✅ 存在"
            else:
                info[f"文件 {file_name}"] = "❌ 缺失"
    else:
        info["包目录"] = "❌ 不存在"
    
    # 检查配置文件
    config_files = ["config.yaml", "examples/config.example.yaml"]
    for config_file in config_files:
        config_path = Path(config_file)
        if config_path.exists():
            info[f"配置 {config_file}"] = "✅ 存在"
        else:
            info[f"配置 {config_file}"] = "❌ 不存在"
    
    return info


def print_section(title: str, data: Dict[str, str]) -> None:
    """打印检查结果部分"""
    print(f"\n📋 {title}:")
    print("-" * 30)
    for key, value in data.items():
        print(f"{key}: {value}")


def main() -> None:
    """主函数"""
    print_header("bongobot 环境检查")
    
    # 检查各个部分
    python_info = check_python_info()
    pip_info = check_pip_info()
    venv_info = check_virtual_environment()
    modules_info = check_required_modules()
    permissions_info = check_system_permissions()
    bongobot_info = check_bongobot_installation()
    
    # 打印结果
    print_section("Python 环境", python_info)
    print_section("pip 信息", pip_info)
    print_section("虚拟环境", venv_info)
    print_section("必需模块", modules_info)
    print_section("系统权限", permissions_info)
    print_section("bongobot 安装", bongobot_info)
    
    # 总结
    print("\n" + "=" * 50)
    print(" 📊 检查完成")
    print("=" * 50)
    
    # 统计问题
    all_info = {**modules_info, **venv_info, **bongobot_info}
    issues = [key for key, value in all_info.items() if "❌" in value]
    
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个问题:")
        for issue in issues:
            print(f"  - {issue}")
        print("\n💡 建议运行 setup_environment.py 来解决环境问题")
    else:
        print("\n🎉 环境检查通过，可以正常使用!")
    
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
