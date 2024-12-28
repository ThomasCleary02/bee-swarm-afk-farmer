# AFK Automation Script for Bee Swarm Simulator

This Python script automates AFK farming in Bee Swarm Simulator by simulating key presses and mouse clicks in a repeating sequence. It is designed to work seamlessly with minimal setup.

## Features
- **Window Detection**: The script checks if Roblox is the active window before running.
- **Key Press Automation**: Simulates holding specific keys (`A`, `S`, `D`, `W`) for a configurable duration.
- **Mouse Autoclicker**: Automates left mouse button clicks.
- **Toggle Controls**: 
  - Press `F1` to toggle key press automation.
  - Press `F2` to toggle the mouse autoclicker.
- **Asynchronous Execution**: Key presses and mouse clicks are handled concurrently for efficient automation.

## Requirements
- Python 3.7 or newer
- Libraries:
  - `pynput` for simulating keyboard and mouse actions
  - `pygetwindow` for detecting the active window
  - `asyncio` (built-in with Python 3.7+)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/ThomasCleary02/bee-swarm-afk-farmer.git
   cd afk-farming-script
   ```

2. Install the required Python library:
    ```bash
    pip install pynput pygetwindow
    ```

3. Run the script:
   ```bash
   python afk-farm.py
   ```

## Usage

1. Launch the script in your terminal.

2. Open Roblox and ensure it is the active window.

3. Use the following controls:
    - Press **F1** to start/stop key press automation.
    - Press **F2** to start/stop the mouse autoclicker.

4. To stop the script, press `Ctrl+C` in the terminal.

## Code Structure
-`hold_key(key, duration)`: Simulates holding a keyboard key for a specified duration.
-`left_click()`: Simulates a single left mouse click.
-`key_press_loop()`: Runs the key press automation in a loop.
-`autoclick_loop()`: Runs the mouse autoclicker in a loop.
-`is_roblox_active()`: Checks if Roblox is the active window.
-`on_press(key)`: Listens for key presses to toggle automation features.


## Notes
- This script is for educational purposes only. Ensure it complies with the terms of service of the platform or game you use it for.
- Adjust the key press durations or add delays if needed to suit your specific use case.

## Troubleshooting
- **Keys or clicks not registering**: Ensure the game window is focused when the script is running.
- **Permission errors**: Run the script with appropriate permissions (e.g., as an administrator if required).
- **Dependencies** not installed: Ensure all required libraries are installed using `pip`.

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- Created using the [pynput](https://pypi.org/project/pynput/) library for simulating keyboard and mouse input.
- Uses [pygetwindow](https://pypi.org/project/PyGetWindow/) to detect the active window.
