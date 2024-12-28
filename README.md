# Bee Swarm Simulator Automation Script

A Python automation script for Bee Swarm Simulator that provides multiple movement patterns and an autoclicker feature. This script helps automate farming activities while maintaining safety and efficiency.

## Features
- **Smart Window Detection**: Only runs when Roblox is the active window
- **Multiple Automation Patterns**:
  - Pattern 1: Basic square movement (A→S→D→W)
  - Pattern 2: Extended rectangular movement with diagonal traversal
  - Pattern 3: Complex pattern with full field coverage
- **Autoclicker**: Automated left-click functionality with configurable timing
- **Safety Features**: 
  - Only one movement pattern can run at a time
  - All features can be toggled independently
  - Automatic deactivation when Roblox loses focus

## Controls
- **F1**: Toggle autoclicker
- **F2**: Toggle Pattern 1 (Basic square)
- **F3**: Toggle Pattern 2 (Extended rectangular)
- **F4**: Toggle Pattern 3 (Complex coverage)
- **Ctrl+C**: Stop the script

## Requirements
- Python 3.7 or newer
- Required libraries:
  - `pynput`: Keyboard and mouse control
  - `pygetwindow`: Window detection
  - `colorama`: Colored console output
  - `asyncio`: Asynchronous execution (included with Python)

## Installation

1. Clone the repository:
```bash
    git clone https://github.com/ThomasCleary02/bee-swarm-afk-farmer.git
    cd bee-swarm-afk-farmer
```

2. Install dependencies:
```bash
    pip install -r requirements.txt
```

## Usage

1. Start the script:
python main.py

2. Launch Roblox and join Bee Swarm Simulator

3. The script will display colored status messages in the console:
   - Green: Feature activated
   - Yellow: Feature deactivated
   - Blue: Roblox window status
   - Cyan: Warning messages (e.g., when trying to activate multiple patterns)
   - Red: Script termination

## Movement Patterns

### Pattern 1 (F2)
- Basic square movement
- Equal duration (0.75s) for each direction
- Ideal for small field coverage

### Pattern 2 (F3)
- Extended rectangular pattern
- Variable durations:
  - Horizontal movements: 1.0s
  - Vertical movements: 0.5s
- Better for medium-sized fields

### Pattern 3 (F4)
- Complex coverage pattern
- Combines multiple movement sequences
- Best for large fields or specific farming patterns
- Full field traversal with optimal timing

## Code Structure

The project is organized into several modules:

- `main.py`: Entry point and asyncio event loop management
- `automation.py`: Core automation functionality and movement patterns
- `key_listener.py`: Keyboard input handling and toggle logic
- `util.py`: Utility functions for window detection

## Contributing

Contributions are welcome! Here are some ways you can help:

1. Adding new movement patterns
2. Optimizing existing patterns
3. Improving window detection
4. Adding new features
5. Bug fixes and performance improvements

Please ensure your code follows the existing structure and includes appropriate documentation.

## Safety Notes

- This script is for educational purposes only
- Ensure compliance with game terms of service
- Use reasonable delays to prevent server strain
- The script only runs when Roblox is the active window to prevent unintended actions

## Troubleshooting

Common issues and solutions:

1. **Script not responding to hotkeys**
   - Ensure Roblox window is active
   - Check if another pattern is already running
   - Verify keyboard permissions

2. **Movement patterns not working**
   - Confirm Roblox is in focus
   - Check console for status messages
   - Ensure no conflicting programs are running

3. **Installation problems**
   - Verify Python version (3.7+)
   - Run `pip install -r requirements.txt` with administrator privileges
   - Check for conflicting Python installations

## License

This project is licensed under the MIT License

## Acknowledgments

- Built with [pynput](https://pypi.org/project/pynput/) for input simulation
- Uses [pygetwindow](https://pypi.org/project/PyGetWindow/) for window management
- Console coloring by [colorama](https://pypi.org/project/colorama/)