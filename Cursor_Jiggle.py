import usb_hid
from adafruit_hid.mouse import Mouse
from time import sleep

# Initialize the Mouse object
try:
    m = Mouse(usb_hid.devices)
except Exception as e:
    print("Error initializing Mouse:", e)
    while True:  # Halt if initialization fails
        sleep(1)

# Main loop to move mouse in a square pattern
while True:
    try:
        m.move(-30, 0, 0)  # Move left
        sleep(0.25)
        m.move(30, 0, 0)   # Move right
        sleep(0.25)
        m.move(0, -30, 0)  # Move up
        sleep(0.25)
        m.move(0, 30, 0)   # Move down
        sleep(0.25)
    except Exception as e:
        print("Error during mouse movement:", e)
        sleep(1)  # Brief pause before retrying