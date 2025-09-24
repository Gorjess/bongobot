# -*- coding: utf-8 -*-
# Created by 954860224@qq.com
"""
BongoCat Idle Simulator Installation Configuration
"""
from setuptools import setup, find_packages
import os

def get_version():
    version_file = os.path.join("bongobot", "__init__.py")
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split('"')[1]
    return "1.0.0"

def get_long_description():
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    return "bongobot 闲置模拟器"

def get_requirements():
    """稳健读取 requirements.txt，兼容 BOM/UTF-16 等编码。

    当文件被意外以 UTF-16 保存时，严格的 utf-8 解码会抛出
    UnicodeDecodeError（如 0xff/0xfe 起始字节）。这里做多编码
    回退，最后在读取失败时使用内置依赖列表兜底，保证安装不中断。
    """
    encodings = ["utf-8", "utf-8-sig", "utf-16", "utf-16-le", "utf-16-be"]
    for enc in encodings:
        try:
            with open("requirements.txt", "r", encoding=enc) as f:
                return [
                    line.strip()
                    for line in f
                    if line.strip() and not line.strip().startswith("#")
                ]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            break
    # 兜底（需与 pyproject.toml 保持一致）
    return [
        "pyautogui>=0.9.54",
        "pydirectinput>=1.0.4",
        "pywin32>=311",
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "Pillow>=11.0.0",
        "PyYAML>=6.0.0",
        "setuptools>=45.0.0",
        "wheel>=0.37.0",
    ]

setup(
    name="bongobot",
    version=get_version(),
    author="GorjessJin",
    author_email="954860224@qq.com",
    description="bongobot 闲置模拟器",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gorjess/bongobot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Desktop Environment",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    install_requires=get_requirements(),
    entry_points={
        "console_scripts": [
            "bongobot=bongobot.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml"],
        "assets": ["README.md"],
    },
    data_files=[],
    keywords="automation idle simulation keyboard mouse clicker",
    project_urls={
        "Bug Reports": "https://github.com/Gorjess/bongobot/issues",
        "Source": "https://github.com/Gorjess/bongobot",
    },
)
