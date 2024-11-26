import picar_4wd as fc
import time
import curses

speed = 30
stop_flag = False  # Flag to track stop command

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control: Use arrow keys to drive the car. Press 's' to stop, 'q' to quit.")

    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            fc.forward(speed)
        elif key == curses.KEY_DOWN:
            fc.backward(speed)
        elif key == curses.KEY_LEFT:
            fc.turn_left(speed)
        elif key == curses.KEY_RIGHT:
            fc.turn_right(speed)
        elif key == ord('s'):
            stop_car()
        elif key == ord('q'):
            break
        else:
            fc.stop()
        
        time.sleep(0.1)

    fc.stop()
    stdscr.addstr(2, 0, "Manual control stopped. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

def stop_car():
    global stop_flag
    if not stop_flag:  # Ensure stop command is processed once
        fc.stop()
        stop_flag = True

if __name__ == "__main__":
    curses.wrapper(main)
