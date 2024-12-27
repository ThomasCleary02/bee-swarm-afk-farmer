import time
from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController, Button

# Initialize controllers
keyboard = Controller()
mouse = MouseController()

def hold_key(key, duration):
    """
    Simulates holding a keyboard key for a specified duration.

    Args:
        key (str): The key to be pressed (e.g., 'a', 's', 'w', 'd').
        duration (float): Time in seconds to hold the key.

    Returns:
        None
    """
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def left_click():
    """
    Simulates a single left mouse click.

    This presses and releases the left mouse button with a short delay
    to mimic a real mouse click.

    Returns:
        None
    """
    mouse.press(Button.left)  # Press left mouse button
    time.sleep(0.1)           # Short delay to mimic a real click
    mouse.release(Button.left)  # Release left mouse button

def main():
    """
    Main function to automate the key pressing and mouse clicking sequence.

    The loop will:
        1. Hold the 'A' key for 0.75 seconds and perform a left mouse click.
        2. Repeat the same process for keys 'S', 'D', and 'W'.

    The sequence runs in an infinite loop until interrupted by the user.

    Returns:
        None
    """
    while True:
        hold_key('a', 0.75)
        left_click()
        hold_key('s', 0.75)
        left_click()
        hold_key('d', 0.75)
        left_click()
        hold_key('w', 0.75)
        left_click()

if __name__ == "__main__":
    try:
        print("Starting the script. Press Ctrl+C to stop.")
        main()
    except KeyboardInterrupt:
        print("\nScript stopped.")
