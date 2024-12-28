# util.py

import pygetwindow as gw

def is_roblox_active():
    """
    Check if the Roblox window is active.

    Returns:
        bool: True if Roblox is active, False otherwise.
    """
    windows = gw.getWindowsWithTitle("Roblox")
    return bool(windows)
