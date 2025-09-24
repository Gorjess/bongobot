# Created by 954860224@qq.com
import os
import logging
from datetime import datetime


def setup_logging(level: str = "INFO", write_to_file: bool = False, log_dir: str = "log") -> logging.Logger:
    logger = logging.getLogger('gamebot')
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(console_handler)

    if write_to_file:
        try:
            os.makedirs(log_dir, exist_ok=True)
            log_filename = os.path.join(log_dir, f"gamebot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
            file_handler = logging.FileHandler(log_filename, encoding='utf-8')
            file_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
            file_handler.setFormatter(logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
                                                       datefmt='%Y-%m-%d %H:%M:%S'))
            logger.addHandler(file_handler)
            logger.info(f"日志文件: {log_filename}")
        except Exception as e:
            logger.warning(f"创建日志文件失败，将仅输出到控制台。原因: {e}")

    return logger



