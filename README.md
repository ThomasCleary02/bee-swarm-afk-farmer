# AFK Automation Script for Bee Swarm Simulator

This Python script automates AFK farming in Bee Swarm Simulator by simulating key presses and mouse clicks in a repeating sequence. It is designed to work seamlessly with minimal setup.

## Features
- Simulates holding specific keys (`A`, `S`, `D`, `W`) for a configurable duration.
- Simulates a left mouse click after each key press.
- Runs in an infinite loop for continuous automation.
- Ability to toggle automation on/off with the `F1` key only if Roblox is the active window.

## Requirements
- Python 3.7 or newer
- `pynput` library for simulating keyboard and mouse actions
- `pygetwindow` library for detecting the active window

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

2. Ensure your game window is focused so the actions register correctly.

3. The script will:
    - Hold the `A` key for 0.75 seconds, then simulate a left mouse click.
    - Repeat the process for the `S`, `D`, and `W` keys.

4. To start/stop the automation, press `F1` while Roblox is the active window. If Roblox is not the active window, the script will notify you and will not toggle the automation.

5. To stop the script, press `Ctrl+C`.

## Code Structure
- `hold_key(key, duration)`: Simulates holding a keyboard key for a given duration.
- `left_click()`: Simulates a single left mouse click.
- `main()`: Automates the sequence of key presses and mouse clicks in a loop.
- `on_press(key)`: Listens for the `F1` key to toggle the automation on/off.


## Notes
- This script is for educational purposes only. Ensure it complies with the terms of service of the platform or game you use it for.
- Adjust the key press durations or add delays if needed to suit your specific use case.

## Troubleshooting
- **Keys or clicks not registering**: Ensure the game window is focused when the script is running.
- **Permission errors**: Run the script with appropriate permissions (e.g., as an administrator if required).

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- Created using the [pynput](https://pypi.org/project/pynput/) library for simulating keyboard and mouse input.
- Uses [pygetwindow](https://pypi.org/project/PyGetWindow/) to detect the active window.
