from pynput.keyboard import Listener, Key
from colorama import Fore

def on_press(key, is_running, autoclicker_running, is_roblox_active):
    """
    Listens for key presses. Specifically toggles automation on/off with F1 and F2 keys.
    """
    try:
        if is_roblox_active():
            if key == Key.f1:
                is_running[0] = not is_running[0]
                if is_running[0]:
                    print(f"{Fore.GREEN}----------------------\nAutomation started.\n----------------------")
                else:
                    print(f"{Fore.YELLOW}----------------------\nAutomation stopped.\n----------------------")
            elif key == Key.f2:
                autoclicker_running[0] = not autoclicker_running[0]
                if autoclicker_running[0]:
                    print(f"{Fore.GREEN}----------------------\nAutoclicker started.\n----------------------")
                else:
                    print(f"{Fore.YELLOW}----------------------\nAutoclicker stopped.\n----------------------")
        else:
            print(f"{Fore.BLUE}Roblox is not active.")
    except AttributeError:
        pass

def start_listener(is_running, autoclicker_running, is_roblox_active):
    """
    Start the key listener.
    """
    listener = Listener(on_press=lambda key: on_press(key, is_running, autoclicker_running, is_roblox_active))
    listener.start()
