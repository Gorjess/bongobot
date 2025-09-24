# Created by 954860224@qq.com
import ctypes
import logging

logger = logging.getLogger('gamebot')


class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]


def get_user_idle_seconds() -> float:
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if not ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
        logger.error("GetLastInputInfo 调用失败")
        return 0.0
    tick_count = ctypes.windll.kernel32.GetTickCount()
    elapsed_ms = tick_count - lastInputInfo.dwTime
    return float(elapsed_ms) / 1000.0


