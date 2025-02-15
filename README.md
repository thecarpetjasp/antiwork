# Mouse Jiggler Script

A simple Python script to simulate mouse movement in order to prevent screen savers or auto-lock features from activating during periods of inactivity.


## How It Works

This script moves your mouse automatically every few seconds if the mouse is idle (does not move vertically). The movement alternates between moving the cursor left and right, mimicking natural user behavior while avoiding detection by anti-idle software.


## Key Features:

- Idle Detection: Waits for a period of inactivity (default 5 seconds).
- Stealth X-Axis Movement: Moves the mouse along the X-axis without triggering unnecessary resets.
- Customizable Delay: Set your own inactivity delay time.
- No Installation Required: Just run the script using Python. `python main.py`


### Requirements
Python 3.x
