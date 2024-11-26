import picar_4wd as fc
import time
import curses

speed = 30

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Ultrasonic Sensor for Recording:")
    stdscr.addstr(1, 0, "Use arrow keys to drive the car. Press 'q' to quit and save.")
    stdscr.addstr(2, 0, "Recording movements and ultrasonic scans...")

    movements = []

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            fc.forward(speed)
            movements.append(('forward', speed, time.time()))
        elif key == curses.KEY_DOWN:
            fc.backward(speed)
            movements.append(('backward', speed, time.time()))
        elif key == curses.KEY_LEFT:
            fc.turn_left(speed)
            movements.append(('left', speed, time.time()))
        elif key == curses.KEY_RIGHT:
            fc.turn_right(speed)
            movements.append(('right', speed, time.time()))
        elif key == ord('q'):
            break
        else:
            fc.stop()

        # Ultrasonic sensor scanning
        scan_result = fc.scan_step(35)
        movements.append(('ultrasonic', scan_result, time.time()))

        time.sleep(0.1)

    fc.stop()

    with open('movements.txt', 'w') as f:
        for movement in movements:
            f.write(','.join(map(str, movement)) + '\n')

    stdscr.addstr(3, 0, "Recording ended. Movements saved to 'movements.txt'.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
