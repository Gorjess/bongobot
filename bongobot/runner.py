# Created by 954860224@qq.com
import time
import random
from dataclasses import dataclass
from typing import Any, Dict, List
import os
import logging

import pydirectinput
import win32api
import win32con
import win32gui

from .idle import get_user_idle_seconds
from .automation import simulate_keypress, find_and_click_template


@dataclass
class RuntimeState:
    is_simulating: bool = False
    next_search_time: float = 0.0
    next_allowed_click_time: float = 0.0
    last_simulation_time: float = 0.0


def is_safe_to_simulate(logger: logging.Logger) -> bool:
    try:
        hwnd = win32gui.GetForegroundWindow()
        if not hwnd:
            return True
        title = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        screen_w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        if left <= 0 and top <= 0 and right >= screen_w and bottom >= screen_h:
            logger.warning(f"检测到全屏应用: {title}，暂停模拟以避免干扰")
            return False
        sens = ['game','steam','origin','uplay','battle.net','minecraft','league of legends','dota','counter-strike','valorant','discord','zoom','teams','skype','obs','streamlabs']
        if any(k in title.lower() for k in sens):
            logger.warning(f"检测到敏感应用: {title}，暂停模拟以避免干扰")
            return False
        logger.debug(f"安全检查通过，当前前台窗口: {title}")
        return True
    except Exception as e:
        logger.error(f"安全检查失败: {e}，暂停模拟")
        return False


def get_real_user_idle_seconds(state: RuntimeState) -> float:
    sys_idle = get_user_idle_seconds()
    if state.is_simulating and state.last_simulation_time > 0:
        since = time.time() - state.last_simulation_time
        # 在最近一段时间内是程序产生的输入，避免误判为用户回来了
        if since < 5.0:
            return max(sys_idle, 10.0)
    return sys_idle

def step_idle_mode(keys: List[str], clicker: Dict[str, Any], cfg_dir: str, state: RuntimeState, logger: logging.Logger) -> None:
    if not is_safe_to_simulate(logger):
        state.is_simulating = False
        time.sleep(2)
        return
    if not state.is_simulating:
        logger.info("检测到您已闲置，开始模拟输入…")
        state.is_simulating = True
    simulate_keypress(keys)
    state.last_simulation_time = time.time()
    now_ts = time.time()
    if clicker.get('enabled', True) and now_ts >= state.next_search_time and now_ts >= state.next_allowed_click_time:
        # 基于配置文件所在目录解析相对路径，避免受当前工作目录影响
        template_path = os.path.join(cfg_dir, str(clicker['template_path']))
        if find_and_click_template(template_path, float(clicker['confidence'])):
            state.next_allowed_click_time = now_ts + float(clicker['wait_after_click_seconds'])
            logger.info(f"点击完成并进入冷却: {float(clicker['wait_after_click_seconds']):.1f}s")
        state.next_search_time = now_ts + float(clicker['search_interval_seconds'])
    delay = random.uniform(1.0, 2.0)
    logger.debug(f"本轮完成，等待 {delay:.1f} 秒")
    time.sleep(delay)


def step_active_mode(state: RuntimeState, idle_time: float, logger: logging.Logger) -> None:
    if state.is_simulating:
        logger.warning(f"检测到您已回来操作，暂停模拟。(闲置时间从 {idle_time:.3f}s 变为活动状态)")
        state.is_simulating = False
    time.sleep(0.5)


def run_loop(cfg: Dict[str, Any], logger: logging.Logger) -> None:
    threshold = float(cfg['bot']['idle_threshold_seconds'])
    keys = list(cfg['bot']['keys'])
    clicker = cfg['clicker']
    cfg_dir = str(cfg.get('__config_dir', os.getcwd()))
    pydirectinput.FAILSAFE = False
    pydirectinput.PAUSE = 0.02
    state = RuntimeState()
    try:
        while True:
            idle_time = get_real_user_idle_seconds(state)
            logger.debug(f"主循环检查 - 闲置时间: {idle_time:.3f}s, 阈值: {threshold}s, 当前状态: {'模拟中' if state.is_simulating else '等待中'}")
            if idle_time >= threshold:
                step_idle_mode(keys, clicker, cfg_dir, state, logger)
            else:
                step_active_mode(state, idle_time, logger)
    except KeyboardInterrupt:
        logger.info("检测到 Ctrl+C，正在停止程序…")
    except Exception as e:
        logger.error(f"程序运行时发生错误: {e}")
    finally:
        logger.info("程序已停止。")


