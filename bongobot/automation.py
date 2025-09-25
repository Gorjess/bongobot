# Created by 954860224@qq.com
import time
import random
from typing import List
import os
import logging
import ctypes

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
    # 加载模板为 RGB，便于按缩放比例生成多尺寸版本
    try:
        base_img = Image.open(template_path).convert("RGB")
    except Exception as open_err:
        logger.error(f"加载模板失败: {open_err}")
        return False

    # 读取系统缩放（Windows），并构造待尝试的缩放系数列表
    def _get_system_scale() -> float:
        try:
            if os.name != 'nt':
                return 1.0
            user32 = ctypes.windll.user32
            gdi32 = ctypes.windll.gdi32
            hdc = user32.GetDC(0)
            LOGPIXELSX = 88
            dpi = gdi32.GetDeviceCaps(hdc, LOGPIXELSX)
            user32.ReleaseDC(0, hdc)
            if dpi and dpi > 0:
                return float(dpi) / 96.0
        except Exception:
            pass
        return 1.0

    sys_scale = _get_system_scale()
    candidate_scales: List[float] = []
    for s in [sys_scale, 1.0, sys_scale * 0.9, sys_scale * 1.1]:
        if s <= 0:
            continue
        # 去重（允许 ±3% 视为同一尺寸）
        if all(abs(s - es) > 0.03 for es in candidate_scales):
            candidate_scales.append(s)

    box = None
    # 先尝试基于 OpenCV 的置信度匹配（多尺寸）
    try:
        for s in candidate_scales:
            img = base_img if abs(s - 1.0) < 0.03 else base_img.resize(
                (max(1, int(base_img.width * s)), max(1, int(base_img.height * s))),
                Image.LANCZOS,
            )
            logger.debug(f"尝试匹配：缩放系数 {s:.2f}，confidence={confidence}")
            try:
                box = pyautogui.locateOnScreen(img, confidence=confidence)
            except pyautogui.ImageNotFoundException:
                logger.debug("模板未找到（OpenCV 置信度匹配）")
                continue
            # 其它异常交给外层 except 触发回退
            if box:
                break
    except Exception:
        # 出现后端异常时进行回退：无置信度的精确匹配，多尺寸尝试
        logger.exception(
            "locateOnScreen 调用失败（可能是截图后端/OpenCV/Pillow 环境问题），尝试回退到无置信度匹配…"
        )
        try:
            for s in candidate_scales:
                img = base_img if abs(s - 1.0) < 0.03 else base_img.resize(
                    (max(1, int(base_img.width * s)), max(1, int(base_img.height * s))),
                    Image.LANCZOS,
                )
                logger.debug(f"回退精确匹配：缩放系数 {s:.2f}")
                try:
                    box = pyautogui.locateOnScreen(img)
                except pyautogui.ImageNotFoundException:
                    logger.debug("回退匹配：模板未找到（精确匹配）。")
                    continue
                if box:
                    logger.warning("已回退为无置信度匹配并成功定位模板（建议检查 OpenCV/Pillow 安装）。")
                    break
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
