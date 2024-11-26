import picar_4wd as fc
import time
import curses

speed = 30

def record_movements(movements_file, stdscr):
    movements = []
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Ultrasonic Sensor: Use arrow keys to drive the car. Press 's' to stop recording and save, 'q' to quit recording.")

    try:
        while True:
            key = stdscr.getch()

            if key == curses.KEY_UP:
                fc.forward(speed)
                movements.append((time.time(), 'forward', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_DOWN:
                fc.backward(speed)
                movements.append((time.time(), 'backward', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_LEFT:
                fc.turn_left(speed)
                movements.append((time.time(), 'left', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == curses.KEY_RIGHT:
                fc.turn_right(speed)
                movements.append((time.time(), 'right', speed, fc.get_distance_at(0), fc.scan_step(35)))
            elif key == ord('s'):
                break
            elif key == ord('q'):
                return None
            else:
                fc.stop()
                movements.append((time.time(), 'stop', 0, fc.get_distance_at(0), fc.scan_step(35)))

            time.sleep(0.1)

    finally:
        fc.stop()
        # Save recorded movements to file
        with open(movements_file, 'w') as file:
            for move in movements:
                file.write(f"{move[0]},{move[1]},{move[2]},{move[3]},{move[4]}\n")

def main(stdscr):
    movements_file = 'recorded_movements.txt'
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Recording movements and ultrasonic sensor data...")
    stdscr.refresh()
    
    record_movements(movements_file, stdscr)
    
    stdscr.addstr(2, 0, f"Recording saved to {movements_file}. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
