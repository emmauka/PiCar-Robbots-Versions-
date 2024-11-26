import picar_4wd as fc
import time

speed = 40
obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

# Distances and durations for movements
distance_to_move_first = 40
move_duration_first = 1.33

distance_to_move_second = 115
move_duration_second = 3.83

distance_to_move_third = 58
move_duration_third = 2.00

distance_to_move_fourth = 119
move_duration_fourth = 2.67

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def stop_car(duration):
    """Stop the car for a specified duration."""
    fc.stop()
    time.sleep(duration)

def clockwise_move(duration):
    """Move the car in a clockwise direction for a specified duration."""
    fc.turn_right(speed)
    time.sleep(duration)
    fc.stop()

def scan(duration):
    fc.scan_list(35)

def main():
    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]

        # If an obstacle is detected (any distance less than the threshold), start avoidance
        if any(distance < obstacle_threshold for distance in tmp):
            # Turn right and move forward
            fc.turn_left(speed)
            time.sleep(0.5)
            fc.stop()
            move_forward(move_duration_first)

            # Turn left and move forward
            fc.turn_right(speed)
            time.sleep(0.10)
            fc.stop()
            move_forward(move_duration_second)

            # After second turn, stop for 3 seconds
            stop_car(3)

            scan_list = fc.scan_step(35) 

            fc.turn_left(speed)
            scan_list = fc.scan_step(35)
            time.sleep(0.8)
            fc.stop()
            move_forward(move_duration_third)
            # Clockwise movement
            clockwise_move(0.3)

            stop_car(3)

            # Turn left again and move forward
            fc.turn_right(speed)
            time.sleep(0.5)
            fc.stop()
            move_forward(move_duration_third)

            # Turn left one more time and move forward
            fc.turn_right(speed)
            time.sleep(0.48)
            fc.stop()

            fc.turn_left(speed)
            time.sleep(0.4)
            fc.stop()
            move_forward(move_duration_third)

            fc.turn_right(speed)
            time.sleep(0.3)
            fc.stop()
            move_forward(move_duration_fourth)

            # Pause for 3 seconds before continuing
            time.sleep(3)

        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
