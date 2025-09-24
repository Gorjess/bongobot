# Created by 954860224@qq.com
"""
bongobot 快速设置脚本
一键完成环境配置和依赖安装
"""
import subprocess
import sys
from pathlib import Path


def main():
    """快速设置主函数"""
    print("🚀 bongobot 快速设置")
    print("=" * 40)
    
    # 检查是否在项目根目录
    if not Path("bongobot").exists() or not Path("setup.py").exists():
        print("❌ 请在项目根目录运行此脚本")
        input("按回车键退出...")
        sys.exit(1)
    
    print("📋 即将执行以下操作:")
    print("1. 检查 Python 环境")
    print("2. 创建虚拟环境")
    print("3. 安装基础依赖")
    print("4. 配置项目")
    
    confirm = input("\n继续吗? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes', '是']:
        print("取消设置")
        sys.exit(0)
    
    try:
        # 运行环境设置脚本
        print("\n🔧 运行环境设置脚本...")
        subprocess.run([sys.executable, "scripts/setup_environment.py"], check=True)
        
        print("\n🎉 快速设置完成！")
        print("\n📋 下一步:")
        print("1. 激活虚拟环境: venv\\Scripts\\activate")
        print("2. 运行程序: bongobot")
        print("3. 查看帮助: python -m bongobot --help")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ 设置失败: {e}")
        print("请手动运行: python scripts/setup_environment.py")
    except KeyboardInterrupt:
        print("\n\n⚠️  用户取消设置")
    
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
