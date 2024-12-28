import asyncio
from pynput.keyboard import Controller as KBController
from pynput.mouse import Controller as MouseController, Button

keyboard = KBController()
mouse = MouseController()

async def hold_key(key: str, duration: float):
    """
    Simulates holding a keyboard key for a specified duration.
    """
    keyboard.press(key)
    await asyncio.sleep(duration)
    keyboard.release(key)

async def left_click():
    """
    Simulates a single left mouse click.
    """
    mouse.press(Button.left)
    await asyncio.sleep(0.25)  # Delay to mimic a real click
    mouse.release(Button.left)

async def autoclick_loop(autoclicker_running):
    """
    Asynchronous loop for mouse autoclicking.
    """
    while True:
        if autoclicker_running[0]:
            await left_click()
            await asyncio.sleep(0.5)  # Delay between clicks
        else:
            await asyncio.sleep(0.1)

async def key_press_loop(is_running):
    """
    Asynchronous loop for key presses.
    """
    while True:
        if is_running[0]:
            await hold_key('a', 0.75)
            await hold_key('s', 0.75)
            await hold_key('d', 0.75)
            await hold_key('w', 0.75)
        else:
            await asyncio.sleep(0.1)  # Small delay to prevent high CPU usage
