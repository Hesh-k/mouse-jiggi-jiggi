import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep, monotonic
import random

# Initialize the Mouse object
try:
    m = Mouse(usb_hid.devices)
except Exception as e:
    print("Error initializing Mouse:", e)
    while True:
        sleep(1)

# Initialize timing for random clicks
last_click = monotonic()
next_click_interval = random.uniform(3, 10)  # Random interval between 3 and 10 seconds

# Main loop for mouse movement and random clicks
while True:
    try:
        # Square movement pattern
        m.move(-30, 0, 0)  # Move left
        sleep(0.25)
        m.move(30, 0, 0)   # Move right
        sleep(0.25)
        m.move(0, -30, 0)  # Move up
        sleep(0.25)
        m.move(0, 30, 0)   # Move down
        sleep(0.25)

        # Check if it's time to perform a random left click
        current_time = monotonic()
        if current_time - last_click >= next_click_interval:
            m.click(Mouse.LEFT_BUTTON)  # Perform left click
            print("Left click performed")  # Debug output to REPL
            last_click = current_time
            next_click_interval = random.uniform(3, 10)  # Set next random interval
    except Exception as e:
        print("Error during mouse operation:", e)
        sleep(1)  # Brief pause before retrying