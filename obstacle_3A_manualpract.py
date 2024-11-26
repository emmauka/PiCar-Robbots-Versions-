import picar_4wd as fc
import time
import curses

speed = 30

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Ultrasonic Sensor for Practice: Use arrow keys to drive the car. Press 's' to stop, 'q' to quit.")
    
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
            fc.stop()
        elif key == ord('q'):
            break
        else:
            fc.stop()
        
        # Ultrasonic sensor scanning
        scan_result = fc.scan_step(35)
        stdscr.addstr(1, 0, f"Ultrasonic Scan: {scan_result}")
        
        time.sleep(0.1)

    fc.stop()
    stdscr.addstr(2, 0, "Practice session ended. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
