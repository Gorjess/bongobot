# Created by 954860224@qq.com
from .config_loader import load_config
from .logger_setup import setup_logging
from .runner import run_loop


def main() -> None:
    cfg = load_config()
    log_cfg = cfg.get('logging', {})
    logger = setup_logging(
        level=str(log_cfg.get('level', 'INFO')),
        write_to_file=bool(log_cfg.get('write_to_file', False)),
        log_dir=str(log_cfg.get('dir', 'log')),
    )

    logger.info("--- bongobot 闲置模拟器 ---")
    logger.warning(
        "合规提示：本工具仅用于办公/演示/测试等非对抗场景的防空闲与自动化。"
        "请勿用于任何游戏的挂机/刷点/绕过交互等用途，可能违反平台或游戏条款并带来封禁/法律风险。"
    )
    logger.info(f"将在您停止操作 {cfg['bot']['idle_threshold_seconds']} 秒后自动开始模拟输入。")
    logger.info("当您回来操作时，将自动暂停。")
    logger.info("按 Ctrl+C 终止程序。")    

    run_loop(cfg, logger)


