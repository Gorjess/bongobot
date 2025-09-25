# Created by 954860224@qq.com
from pathlib import Path
from typing import Any, Dict
import os
import sys
import shutil
import yaml


def load_config(path: str | None = None) -> Dict[str, Any]:
    """
    加载 YAML 配置（支持注释）。
    读取优先级（规范为单一来源）：
    1) 显式传入的 path
    2) 环境变量 BONGOBOT_CONFIG 指定的路径
    3) 仅当前工作目录下的 config.yaml

    不再回退到包内配置。若未能找到有效配置，将提示从 examples/config.example.yaml 复制。

    返回的配置中注入特殊键 "__config_dir" 表示配置文件所在目录，
    供运行时解析相对路径使用。
    """
    candidates: list[Path] = []

    if path:
        candidates.append(Path(path))

    env_path = os.environ.get("BONGOBOT_CONFIG")
    if env_path:
        candidates.append(Path(env_path))

    candidates.append(Path.cwd() / "config.yaml")

    cfg_path: Path | None = None
    for p in candidates:
        if p and p.exists():
            cfg_path = p
            break

    if not cfg_path:
        example_path = (Path(__file__).resolve().parent.parent / "examples" / "config.example.yaml")
        target_path = Path.cwd() / "config.yaml"
        if example_path.exists():
            try:
                shutil.copyfile(example_path, target_path)
                print(f"首次运行：已从示例复制默认配置到 {target_path}")
                cfg_path = target_path
            except Exception as copy_err:
                print("错误: 未找到配置文件且复制示例配置失败。")
                print(f"示例路径: {example_path}")
                print(f"失败原因: {copy_err}")
                sys.exit(1)
        else:
            print("错误: 未找到配置文件。请在当前目录提供 config.yaml，或通过 BONGOBOT_CONFIG 指定路径。")
            print(f"可参考示例: {example_path}")
            sys.exit(1)

    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        example_path = (Path(__file__).resolve().parent.parent / "examples" / "config.example.yaml")
        print(f"错误: 配置文件 {cfg_path} 内容为空或无效。请参考示例: {example_path}")
        sys.exit(1)

    # 注入配置目录，便于后续相对路径解析
    data["__config_dir"] = str(cfg_path.parent)
    return data



