from pynput import mouse


def on_click(x, y, button, pressed):
    if pressed:
        print(f'Button {button} pressed at ({x}, {y})')
    else:
        print(f'Button {button} released at ({x}, {y})')


# Start the mouse listener
with mouse.Listener(on_click=on_click) as listener:
    print("Mouse listener is active. Press any mouse button to identify it.")
    listener.join()
