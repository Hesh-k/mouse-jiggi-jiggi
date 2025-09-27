# Mouse Jiggi Jiggi

![](https://github.com/Hesh-k/mouse-jiggi-jiggi/blob/main/Assets/Cursor_movements.gif)


**Mouse Jiggi Jiggi** is a fun CircuitPython project for the Raspberry Pi Pico (RP2040) that turns your microcontroller into a USB HID mouse. The program moves the mouse cursor in a small square pattern continuously and performs random left-clicks every 3 to 10 seconds, keeping your computer active (e.g., to prevent screen lock or simulate activity). This project is perfect for learning about USB HID, CircuitPython, and the RP2040's capabilities.

## Features
- Moves the mouse cursor in a square pattern (left, right, up, down) every second.
- Simulates random left-clicks at intervals between 3 and 10 seconds.
- Built with CircuitPython and the Adafruit HID library for easy USB mouse emulation.
- Shows up as a real mouse in thr device manager.
- Runs on the affordable Raspberry Pi Pico (RP2040) microcontroller.

## Hardware Requirements
- Raspberry Pi Pico (or any RP2040-based board)
- USB cable (Micro-USB, data-capable, not power-only)
- Computer (Windows, macOS, or Linux) to program the Pico and test the mouse functionality

## Software Requirements
- [CircuitPython](https://circuitpython.org/) (version 9.x or later recommended)
- [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries) (for the `adafruit_hid` library)
- [Thonny IDE](https://thonny.org/) (for programming and debugging)
- Python (included with Thonny; no separate installation needed)

## Setup Instructions

### Step 1: Install CircuitPython on the Raspberry Pi Pico
1. **Download CircuitPython**:
   - Visit [circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/).
   - Download the latest `.uf2` file for the Raspberry Pi Pico (e.g., `adafruit-circuitpython-raspberry_pi_pico-en_US-9.x.x.uf2`).

2. **Flash CircuitPython to the Pico**:
   - Press and hold the **BOOTSEL** button on the Pico.
   - Connect the Pico to your computer via a USB cable while holding BOOTSEL.
   - Release BOOTSEL when the `RPI-RP2` drive appears on your computer.
   - Drag and drop the downloaded `.uf2` file onto the `RPI-RP2` drive.
   - The Pico will automatically reboot, and a new drive named `CIRCUITPY` will appear.

3. **Verify Installation**:
   - Open the `CIRCUITPY` drive and check for files like `boot.py` or `boot_out.txt`.
   - If these files are present, CircuitPython is installed correctly.

### Step 2: Install the Adafruit HID Library
1. **Download the Library Bundle**:
   - Go to [circuitpython.org/libraries](https://circuitpython.org/libraries).
   - Download the latest CircuitPython library bundle (e.g., `adafruit-circuitpython-bundle-9.x-mpy.zip`) matching your CircuitPython version.

2. **Extract and Copy the Library**:
   - Unzip the downloaded bundle.
   - Locate the `adafruit_hid` folder inside the `lib` directory of the bundle.
   - Copy the entire `adafruit_hid` folder to the `lib` directory on the `CIRCUITPY` drive.
   - Example structure: `CIRCUITPY/lib/adafruit_hid/mouse.mpy`

3. **Verify Library Installation**:
   - Ensure the `CIRCUITPY/lib/adafruit_hid/` folder contains files like `mouse.mpy`, `keyboard.mpy`, etc.

### Step 3: Install and Configure Thonny IDE
1. **Download Thonny**:
   - Visit [thonny.org](https://thonny.org/) and download the latest version for your operating system (Windows, macOS, or Linux).
   - Install Thonny by following the installer instructions.

2. **Connect the Pico to Thonny**:
   - Connect your Pico to your computer via a USB cable.
   - Open Thonny and go to **Tools > Options > Interpreter**.
   - Select **CircuitPython (generic)** as the interpreter.
   - Choose the correct port (e.g., `COMx` on Windows or `/dev/ttyACM0` on Linux/macOS) for your Pico.
   - Click **OK** to save.

3. **Test the Connection**:
   - In Thonny, click the **Run** button or open the REPL (bottom panel).
   - Type `import os; print(os.uname())` in the REPL to confirm the Pico is running CircuitPython.

### Step 4: Upload and Run the Code
1. **Copy the Code**:
 

2. **Save the Code**:
   - Save the file as `code.py` directly to the `CIRCUITPY` drive via Thonny’s **File > Save as > CircuitPython device**.
   - Naming the file `code.py` ensures it runs automatically when the Pico powers on.

3. **Run the Code**:
   - Click **Run** in Thonny, or disconnect and reconnect the Pico to start the script.
   - The mouse cursor should move in a small square pattern every second and perform random left-clicks every 3 to 10 seconds.
   - Open Thonny’s REPL to monitor debug messages (e.g., “Left click performed”).

### Troubleshooting
- **Code Stops After One Cycle**:
   - Ensure proper indentation in `code.py` (all loop statements under `while True:`).
   - Check the USB cable (must be data-capable, not power-only).
   - Verify the `adafruit_hid` library is correctly installed in `CIRCUITPY/lib`.

- **No Mouse Movement or Clicks**:
   - Confirm CircuitPython is installed (check for `CIRCUITPY` drive).
   - Test on a different USB port or computer to rule out host issues.
   - Increase `sleep(0.25)` to `sleep(0.5)` if the host throttles rapid HID updates.

- **Thonny Connection Issues**:
   - Click **Stop/Restart backend** in Thonny to release the USB port.
   - Ensure the correct interpreter and port are selected in **Tools > Options > Interpreter**.

- **Errors in REPL**:
   - Check Thonny’s REPL for error messages (e.g., “Error initializing Mouse”).
   - Reinstall CircuitPython or the `adafruit_hid` library if errors persist.

### How It Works
- The script uses the `adafruit_hid.mouse` library to emulate a USB mouse.
- The mouse moves in a square pattern (5 pixels left, right, up, down) every second.
- Random left-clicks are triggered every 3 to 10 seconds using `random.uniform()` and `monotonic()` for timing.
- Error handling ensures the script continues running even if USB HID issues occur.


### Customizing the USB Device Name and Safe Reprogramming

By default, the Waveshare YD-RP2040 appears as "VCC-GND Studio YD RP2040" in Device Manager or `lsusb`. To make it look like a generic mouse (e.g., "USB Optical Mouse") and ensure you can reprogram the board without getting locked out, follow these steps.

#### Step 1: Set the USB Device Name
1. **Edit `boot.py`**:
   - Create or edit `boot.py` on the `CIRCUITPY` drive to set the USB device name and optionally hide interfaces for a "pure mouse" setup.
   - Use this code for a basic setup (as currently implemented):

     ```python
     import usb_cdc
     import usb_hid
     import storage
     import supervisor

     print("Running boot.py")  # Debug output to confirm boot.py is executing

     # Set USB identification to mimic a generic mouse
     try:
         supervisor.set_usb_identification(
             vid=0x046D,  # Logitech VID (common for mice)
             pid=0xC077,  # Logitech mouse PID
             manufacturer="Logitech",
             product="USB Optical Mouse"
         )
         print("USB identification set to USB Optical Mouse")  # Confirm success
     except Exception as e:
         print("Error setting USB identification:", e)

     # Optional: Enable only HID mouse (uncomment to hide CIRCUITPY and REPL)
     storage.disable_usb_drive()  # Hides CIRCUITPY drive
       usb_cdc.disable()  # Hides serial console
       usb_hid.enable(devices=[usb_hid.Device.MOUSE])
       usb_hid.set_interface_name(usb_hid.Device.MOUSE, "HID Mouse")

   - Save `boot.py` to the CIRCUITPY drive using Thonny **File > Save as > CircuitPython device**.
   - Reboot the Pico by unplugging/replugging the USB cable or pressing `Ctrl-D` in Thonny’s REPL.
   - Check Device Manager (Windows), System Information (macOS), or `lsusb` (Linux) to confirm the device appears as **"Logitech Inc. Mouse"**.
   - Make sure to Clear USB cache: **Windows (Device Manager > Uninstall device)**, **Linux (`sudo modprobe -r usbhid`)**, **macOS (reboot)**.
  

![](https://github.com/Hesh-k/mouse-jiggi-jiggi/blob/main/Assets/Custom%20_Device_Name.png)

  
  
### Notes
- The current code hides the **CIRCUITPY** drive (`storage.disable_usb_drive()`) but keeps the REPL enabled for debugging via Thonny.
- To hide both **CIRCUITPY** and **REPL** for a true "pure mouse" experience, uncomment the lines for `usb_cdc.disable()`, `usb_hid.enable()`, and `usb_hid.set_interface_name()`.
- **Warning**: Hiding both interfaces prevents easy reprogramming unless you reset the board.
- Use `flash_nuke.uf2` to reset RP2040 board if you can't access to it for re programming.


### Testing
- Connect the Pico to a computer via USB.
- Observe the mouse cursor moving in a square pattern.
- Verify random left-clicks by opening a text editor or clickable UI element (e.g., a button in a browser).
- Check Thonny’s REPL for “Left click performed” messages to confirm click timing.

### Contributing
Feel free to fork this repository & make improvements ♡

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments
- Built with [CircuitPython](https://circuitpython.org/) and [Adafruit’s HID library](https://github.com/adafruit/Adafruit_CircuitPython_HID).
- Inspired by the need to keep computers active in a fun and educational way.
