import picar_4wd as fc
from pynput import keyboard

Track_line_speed = 20

def Track_line():
    gs_list = fc.get_grayscale_list()
    if fc.get_line_status(400, gs_list) == 0:
        fc.forward(Track_line_speed)
    elif fc.get_line_status(400, gs_list) == -1:
        fc.turn_left(Track_line_speed)
    elif fc.get_line_status(400, gs_list) == 1:
        fc.turn_right(Track_line_speed)

def on_press(key):
    try:
        if key.char == 'q':  # Stop the car when 'q' is pressed
            fc.stop()
            return False  # Stop listener
    except AttributeError:
        pass

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            Track_line()
    except KeyboardInterrupt:
        fc.stop()
