# Created by 954860224@qq.com
import time
import random
from typing import List
import os
import logging

import pydirectinput
import pyautogui
from PIL import Image

logger = logging.getLogger('gamebot')


def simulate_keypress(keys: List[str]) -> None:
    key = random.choice(keys)
    pydirectinput.keyDown(key)
    time.sleep(0.05)
    pydirectinput.keyUp(key)
    logger.info(f"用户闲置中，模拟按键: {key}")


def find_and_click_template(template_path: str, confidence: float) -> bool:
    if not os.path.exists(template_path):
        logger.warning(f"模板图不存在: {template_path}")
        return False
    try:
        box = pyautogui.locateOnScreen(template_path, confidence=confidence)
    except Exception as e:
        # 记录完整堆栈，随后进行一次兼容性回退
        logger.exception(
            "locateOnScreen 调用失败（可能是截图后端/OpenCV/Pillow 环境问题），尝试回退到无置信度匹配…"
        )
        try:
            # 转为 RGB 以避免带 Alpha 的模板导致不兼容
            template_img = Image.open(template_path).convert("RGB")
        except Exception as open_err:
            logger.error(f"加载模板失败: {open_err}")
            return False

        try:
            # 不传 confidence，使用 PIL/pyscreeze 精确匹配作为兜底
            box = pyautogui.locateOnScreen(template_img)
            if box:
                logger.warning("已回退为无置信度匹配并成功定位模板（建议检查 OpenCV/Pillow 安装）。")
            else:
                logger.warning("回退为无置信度匹配后仍未找到模板。")
        except Exception as fallback_err:
            logger.exception(f"回退匹配仍失败: {fallback_err}")
            return False
    if not box:
        logger.info("未在屏幕上找到模板图（可能尚未出现），稍后重试…")
        return False

    c = pyautogui.center(box)
    original_pos = pyautogui.position()
    pydirectinput.moveTo(c.x, c.y)
    pydirectinput.click()
    logger.info(f"已点击模板图: ({c.x}, {c.y})")
    pydirectinput.moveTo(original_pos.x, original_pos.y)
    return True
