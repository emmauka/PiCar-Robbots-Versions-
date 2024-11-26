import picar_4wd as fc
import time
import curses

speed = 30
stop_flag = False  # Flag to track stop command

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Ultrasonic: Use arrow keys to drive the car. Press 's' to stop, 'q' to quit.")
    
    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            fc.forward(speed)
            record_movement('forward', speed)
        elif key == curses.KEY_DOWN:
            fc.backward(speed)
            record_movement('backward', speed)
        elif key == curses.KEY_LEFT:
            fc.turn_left(speed)
            record_movement('left', speed)
        elif key == curses.KEY_RIGHT:
            fc.turn_right(speed)
            record_movement('right', speed)
        elif key == ord('s'):
            stop_car()
            record_movement('stop', 0)
        elif key == ord('q'):
            break
        else:
            fc.stop()
            record_movement('stop', 0)
        
        # Scan and record ultrasonic sensor data
        scan_distance = fc.us_dist(15)
        record_ultrasonic(scan_distance)
        
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

def record_movement(action, speed):
    # Record movements and ultrasonic sensor readings to the file
    with open('recorded_movements.txt', 'a') as file:
        timestamp = time.time()
        file.write(f"{action},{speed},{timestamp}\n")

def record_ultrasonic(distance):
    # Record ultrasonic sensor readings to the file
    with open('recorded_movements.txt', 'a') as file:
        file.write(f",,{time.time()},{distance}\n")

if __name__ == "__main__":
    curses.wrapper(main)
