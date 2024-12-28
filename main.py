# main.py

import asyncio
from app.automation import key_press_loop1, key_press_loop2, key_press_loop3, autoclick_loop
from app.util import is_roblox_active
from app.key_listener import start_listener
from colorama import Fore

async def main():
    # State variables
    is_running1 = [False]  # Mutable list to track automation state
    is_running2 = [False]  # Mutable list to track automation state
    is_running3 = [False]  # Mutable list to track automation state
    autoclicker_running = [False]  # Mutable list to track autoclicker state

    # Start the key listener
    start_listener(is_running1, is_running2, is_running3, autoclicker_running, is_roblox_active)

    # Start automation tasks
    automation_task = asyncio.gather(
        key_press_loop1(is_running1),
        key_press_loop2(is_running2),
        key_press_loop3(is_running3),
        autoclick_loop(autoclicker_running),
    )

    try:
        await automation_task
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    try:
        print(f"{Fore.BLUE}Starting the script. Press Ctrl+C to stop.")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"{Fore.RED}\nScript stopped.{Fore.WHITE}")
