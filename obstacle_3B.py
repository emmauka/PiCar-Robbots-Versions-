import picar_4wd as fc
import time

speed = 30
distance_to_move_first = 35  # Distance to move for the first turn in centimeters
move_duration_first = 1.17  # Calculated time to move forward for 35 cm

distance_to_move_second = 90  # Distance to move for the second turn in centimeters
move_duration_second = 3.00  # Calculated time to move for 90 cm

distance_to_move_third = 60  # Distance to move for the third turn in centimeters
move_duration_third = 2.00  # Calculated time to move forward for 60 cm

distance_to_move_fourth = 80  # Distance to move for the fourth turn in centimeters
move_duration_fourth = 2.67  # Calculated time to move for 80 cm

obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def avoid_obstacle():
    """Perform obstacle avoidance maneuvers."""
    # Turn right and move forward
    fc.turn_right(speed)
    time.sleep(0.90)  # Adjust the time to ensure a proper right turn
    fc.stop()

    move_forward(move_duration_first)  # Move forward for 35 cm

    # Turn left and move forward
    fc.turn_left(speed)
    time.sleep(0.92)  # Adjust the time to ensure a proper left turn
    fc.stop()

    move_forward(move_duration_second)  # Move forward for 90 cm

    # Turn left again and move forward
    fc.turn_left(speed)
    time.sleep(0.94)  # Adjust the time to ensure a proper left turn
    fc.stop()

    move_forward(move_duration_third)  # Move forward for 60 cm

    # Turn left one more time and move forward
    fc.turn_left(speed)
    time.sleep(1)  # Adjust the time to ensure a proper left turn
    fc.stop()

    move_forward(move_duration_fourth)  # Move forward for 80 cm

    # Stop for 2 seconds
    time.sleep(2)

def move_forward_with_obstacle_detection(duration):
    """Move forward for a duration while detecting and avoiding obstacles."""
    start_time = time.time()
    while time.time() - start_time < duration:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue
        
        tmp = scan_list[3:7]
        print(tmp)

        if any(distance < obstacle_threshold for distance in tmp):
            # Simple obstacle avoidance: turn slightly and continue forward
            fc.turn_right(speed)
            time.sleep(0.2)  # Adjust the time for a slight turn to avoid obstacle
            fc.forward(speed)
        else:
            fc.forward(speed)
        
    fc.stop()

def main():
    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]
        print(tmp)

        # If an obstacle is detected (any distance less than the threshold), start avoidance
        if any(distance < obstacle_threshold for distance in tmp):
            avoid_obstacle()

            # Continue moving forward while detecting and avoiding obstacles for 5 seconds
            move_forward_with_obstacle_detection(5)

        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
