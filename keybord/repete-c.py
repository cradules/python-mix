import time

import win32api
import win32con
import win32gui
from pynput import keyboard

caps_lock_on = False


def send_key_to_window(key, win_title):
    # Find the window by its title
    window_handle = win32gui.FindWindow(None, win_title)

    # If the window exists
    if window_handle:
        # Send the key to the window
        virtual_key_code = win32api.VkKeyScan(key)
        scan_code = win32api.MapVirtualKey(virtual_key_code, 0)

        # Post the keydown message
        win32api.PostMessage(window_handle, win32con.WM_KEYDOWN, virtual_key_code, scan_code)

        # Post the keyup message
        win32api.PostMessage(window_handle, win32con.WM_KEYUP, virtual_key_code, scan_code)


def on_key_change(key):
    global caps_lock_on

    # Check if the pressed key is CAPS LOCK
    if key == keyboard.Key.caps_lock:
        # Toggle CAPS LOCK state
        caps_lock_on = not caps_lock_on


def check_capslock_state():
    while True:
        if caps_lock_on:
            print("CAPS LOCK is ON")
            send_key_to_window('c', "Aion Client (64bit)")
            # Sleep for a short duration to avoid flooding
            time.sleep(0.1)


# Start the keyboard listener in a separate thread
listener = keyboard.Listener(on_press=on_key_change)
listener.start()

print(
    "Keyboard listener is active. Toggle CAPS LOCK to start/stop sending the 'A' key to the 'Aion Client (64bit)' "
    "window.")
check_capslock_state()
