# key_listener.py

from pynput.keyboard import Listener, Key
from colorama import Fore

def on_press(key, is_running1, is_running2, is_running3, autoclicker_running, is_roblox_active):
    """
    Listens for key presses. Specifically toggles automation on/off with F1 and F2 keys.
    """
    try:
        if is_roblox_active():
            if key == Key.f1:
                autoclicker_running[0] = not autoclicker_running[0]
                if autoclicker_running[0]:
                    print(f"{Fore.GREEN}\nAutoclicker started.\n")
                else:
                    print(f"{Fore.YELLOW}\nAutoclicker stopped.\n")

            elif key == Key.f2:
                if not is_running3[0] and not is_running2[0]:
                    is_running1[0] = not is_running1[0]
                    if is_running1[0]:
                        print(f"{Fore.GREEN}\nAutomation 1 started.\n")
                    else:
                        print(f"{Fore.YELLOW}\nAutomation 1 stopped.\n")
                else:
                    print(f"{Fore.CYAN}\nAnother automation is running. Please stop current automation before proceeding.\n")


            elif key == Key.f3:
                if not is_running3[0] and not is_running1[0]:
                    is_running2[0] = not is_running2[0]
                    if is_running2[0]:
                        print(f"{Fore.GREEN}\nAutomation 2 started.\n")
                    else:
                        print(f"{Fore.YELLOW}\nAutomation 2 stopped.\n")
                else:
                    print(f"{Fore.CYAN}\nAnother automation is running. Please stop current automation before proceeding.\n")

            elif key == Key.f4:
                if not is_running1[0] and not is_running2[0]:
                    is_running3[0] = not is_running3[0]
                    if is_running3[0]:
                        print(f"{Fore.GREEN}\nAutomation 3 started.\n")
                    else:
                        print(f"{Fore.YELLOW}\nAutomation 3 stopped.\n")
                else:
                    print(f"{Fore.CYAN}\nAnother automation is running. Please stop current automation before proceeding.\n")
                        
        else:
            print(f"{Fore.BLUE}Roblox is not active.")
    except AttributeError:
        pass

def start_listener(is_running1, is_running2, is_running3, autoclicker_running, is_roblox_active):
    """
    Start the key listener.
    """
    listener = Listener(on_press=lambda key: on_press(key, is_running1, is_running2, is_running3, autoclicker_running, is_roblox_active))
    listener.start()
