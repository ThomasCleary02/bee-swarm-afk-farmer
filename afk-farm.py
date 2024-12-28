import asyncio
from pynput.keyboard import Controller, Listener, Key
from pynput.mouse import Controller as MouseController, Button
import pygetwindow as gw

# Initialize controllers
keyboard = Controller()
mouse = MouseController()

# Flags to control automation states
is_running = False
autoclicker_running = False

def is_roblox_active():
    """
    Check if the active window is Roblox.
    
    Returns:
        bool: True if Roblox is the active window, False otherwise.
    """
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return "Roblox" in active_window.title
    return False

async def hold_key(key, duration):
    """
    Asynchronously simulates holding a keyboard key for a specified duration.

    Args:
        key (str): The key to be pressed (e.g., 'a', 's', 'w', 'd').
        duration (float): Time in seconds to hold the key.

    Returns:
        None
    """
    keyboard.press(key)
    await asyncio.sleep(duration)
    keyboard.release(key)

async def left_click():
    """
    Asynchronously simulates a single left mouse click.

    This presses and releases the left mouse button with a short delay
    to mimic a real mouse click.

    Returns:
        None
    """
    mouse.press(Button.left)  # Press left mouse button
    await asyncio.sleep(0.25)  # Short delay to mimic a real click
    mouse.release(Button.left)  # Release left mouse button

async def key_press_loop():
    """
    Asynchronous loop for key presses.
    """
    global is_running
    while True:
        if is_running:
            await hold_key('a', 0.75)
            await hold_key('s', 0.75)
            await hold_key('d', 0.75)
            await hold_key('w', 0.75)
        else:
            await asyncio.sleep(0.1)  # Small delay to prevent high CPU usage

async def autoclick_loop():
    """
    Asynchronous loop for mouse autoclicking.
    """
    global autoclicker_running
    while True:
        if autoclicker_running:
            await left_click()
            await asyncio.sleep(0.5)  # Delay between clicks
        else:
            await asyncio.sleep(0.1)

def on_press(key):
    """
    Listens for key presses. Specifically toggles automation on/off with F1 and F2 keys.
    """
    global is_running, autoclicker_running
    try:
        if is_roblox_active():
            if key == Key.f1:
                is_running = not is_running
                print("Automation started." if is_running else "Automation stopped.")
            elif key == Key.f2:
                autoclicker_running = not autoclicker_running
                print("Autoclicker started." if autoclicker_running else "Autoclicker stopped.")
        else:
            print("Roblox is not active.")
    except AttributeError:
        pass

async def main():
    """
    Main asynchronous entry point for the script.
    """
    listener = Listener(on_press=on_press)
    listener.start()
    
    # Run key press loop and autoclick loop concurrently
    await asyncio.gather(key_press_loop(), autoclick_loop())

if __name__ == "__main__":
    try:
        print("Starting the script. Press Ctrl+C to stop.")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScript stopped.")
