import os
import time
try:
    import pyautogui as pag
except:
    print("Could not find PYAUTOGUI. Downloading now...")
    if not os.path.exists("requirements.txt"):
        print("You must run this file in the same directory as requirements.txt!")
        print("Download the full antiwork repo - not just main.py: https://github.com/thecarpetjasp/antiwork/")
        exit()
    os.system("pip install -r requirements.txt")
    print("\nDownload successful.")
    print("Re-run main.py now.")
    exit()

"""
To use the program, run with 'python main.py'. Set the WAIT_DELAY
variable in seconds. This will determine how long you must be idle
before automation starts.

Once the automated mouse begins moving - simply move your mouse
manually to stop.
"""

# Set this to how many seconds the mouse should be idle before automation kicks in
WAIT_DELAY = 5

# Initialising configurations
prev_position = pag.position()
start_time = None
steps = 5
switch = False

print("Program is active...")

while True:
    try:
        time.sleep(0.1)
        # Checks to see if the mouse has moved from its previous position
        if pag.position().y == prev_position.y:
            # If so, and there is no recorded time, then we start recording now
            if not start_time:
                start_time = time.time()
                continue
            # Checks if the mouse has been idle for our predefined number of seconds
            if time.time() - start_time > WAIT_DELAY:
                # Alternate between our X-Axis direction of movement
                switch = not(switch)
                #
                # We only automate mouse movements along the X-Axis!
                #
                # The X-axis acts like a hidden dimension to our entire script
                # because our logic only checks for movement along the Y-Axis.
                #
                # We can safely use the Y-axis as an explicit check as any natural
                # human mouse movements will contain at least (1) pixel movement
                # along the Y-axis - making the X-axis a hidden area for automation
                # to avoid resets.
                #
                # This makes for a more cleaner and efficient code design.
                for _ in range(steps):
                    direction = steps * (1 if switch else -1)
                    pag.moveTo(pag.position().x+direction, pag.position().y)
                    if pag.position().y != prev_position.y:
                        break
        else:
            # Resets our configurations if the mouse starts / is moving.
            prev_position = pag.position()
            start_time = None
    except KeyboardInterrupt:
        print("Program terminated.")
        break