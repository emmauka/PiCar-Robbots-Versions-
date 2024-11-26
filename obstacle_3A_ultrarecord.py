import picar_4wd as fc
import time
import curses

speed = 30

def record_movements(stdscr, movements_file):
    movements = []
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Ultrasonic Sensor: Use arrow keys to drive the car. Press 's' to stop recording and save, 'q' to quit recording.")

    try:
        while True:
            key = stdscr.getch()

            if key == curses.KEY_UP:
                fc.forward(speed)
                movements.append((time.perf_counter(), 'forward', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_DOWN:
                fc.backward(speed)
                movements.append((time.perf_counter(), 'backward', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_LEFT:
                fc.turn_left(speed)
                movements.append((time.perf_counter(), 'left', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_RIGHT:
                fc.turn_right(speed)
                movements.append((time.perf_counter(), 'right', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == ord('s'):
                fc.stop()
                break
            elif key == ord('q'):
                return None
            else:
                fc.stop()
                movements.append((time.perf_counter(), 'stop', 0, fc.get_distance_at(0), fc.scan_step(35)))

            time.sleep(0.1)

    finally:
        fc.stop()
        # Save recorded movements to file
        with open(movements_file, 'w') as file:
            for move in movements:
                file.write(f"{move[0]},{move[1]},{move[2]},{move[3]},{move[4]}\n")

def main(stdscr):
    movements_file = 'movements.txt'
    record_movements(stdscr, movements_file)

if __name__ == "__main__":
    curses.wrapper(main)
