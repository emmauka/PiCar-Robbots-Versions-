import picar_4wd as fc
import time
import curses

speed = 30

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.addstr(0, 0, "Manual Control with Rotating Ultrasonic Sensor: Use arrow keys to drive the car. Press 's' to stop, 'q' to quit.")
    
    direction = 'left'  # Initial direction for rotating the ultrasonic sensor
    scan_result = []
    
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
        scan_result = fc.get_distance_at(0)  # Get distance at center (0 degrees)
        
        # Display ultrasonic scan result
        stdscr.addstr(1, 0, f"Ultrasonic Scan: {scan_result} cm")
        
        # Rotate the ultrasonic sensor direction
        if direction == 'left':
            fc.servo.set_angle(0)  # Rotate left
            direction = 'straight'
        elif direction == 'straight':
            fc.servo.set_angle(90)  # Center position (straight)
            direction = 'right'
        elif direction == 'right':
            fc.servo.set_angle(180)  # Rotate right
            direction = 'left'
        
        time.sleep(0.5)  # Delay to control the rotation speed

    fc.stop()
    stdscr.addstr(2, 0, "Practice session ended. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)