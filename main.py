import asyncio
from app.automation import key_press_loop, autoclick_loop
from app.util import is_roblox_active
from app.key_listener import start_listener
from colorama import Fore

async def main():
    # State variables
    is_running = [False]  # Mutable list to track automation state
    autoclicker_running = [False]  # Mutable list to track autoclicker state

    # Start the key listener
    start_listener(is_running, autoclicker_running, is_roblox_active)

    # Start automation tasks
    automation_task = asyncio.gather(
        key_press_loop(is_running),
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
