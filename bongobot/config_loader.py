# Created by 954860224@qq.com
from pathlib import Path
from typing import Any, Dict
import sys
import yaml


def load_config(path: str | None = None) -> Dict[str, Any]:
    """
    加载 YAML 配置（支持注释）。
    要求：不提供任何默认值；若未读取到配置（文件不存在或内容为空），直接终止程序。
    """
    cfg_path = Path(path) if path else Path(__file__).with_name("config.yaml")
    if not cfg_path.exists():
        print(f"错误: 未找到配置文件 {cfg_path}，程序终止。")
        sys.exit(1)

    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data:
        print(f"错误: 配置文件 {cfg_path} 内容为空或无效，程序终止。")
        sys.exit(1)

    return data



