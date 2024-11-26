import picar_4wd as fc
import time
import curses

speed = 30

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control: Use arrow keys to drive the car. Press 'q' to quit.")
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
            movements.append(('stop', 0, time.time()))
        
        time.sleep(0.1)

    fc.stop()
    # Save the recorded movements to a file
    with open('recorded_movements.txt', 'w') as file:
        for move in movements:
            file.write(f"{move[0]},{move[1]},{move[2]}\n")
    
    stdscr.addstr(2, 0, "Recording complete. Movements saved to 'recorded_movements.txt'. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
