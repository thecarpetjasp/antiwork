import time
import pyautogui as pag

"""
To use the program, run with 'python main.py'. Set the WAIT_DELAY
variable to as many seconds that you want for the mouse movement to
begin from the moment you stopped moving the mouse.

Once the mouse begins moving - simple move your mouse manually to
stop. It's best to manually move your mouse up and down or in all
directions when trying to stop it.
"""

WAIT_DELAY = 5

prev_position = pag.position()
start_time = None
switch = False

print("Program is active...")

while True:
    try:
        if pag.position().y == prev_position.y:
            if not start_time:
                start_time = time.time()
                continue
            if time.time() - start_time > WAIT_DELAY:
                if switch:
                    direction = 50
                else:
                    direction = -50
                switch = not(switch)
                pag.moveTo(pag.position().x+direction, pag.position().y, 0.3)
        else:
            prev_position = pag.position()
            start_time = None
    except KeyboardInterrupt:
        print("Program terminated.")
        break