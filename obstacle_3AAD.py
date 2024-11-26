import picar_4wd as fc
import time

# Constants
speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle
turn_duration = 0.90  # Duration to ensure a proper turn (adjust as necessary)

# Movement durations for the segments
move_duration_first = 1.17  # Time to move forward for the first segment (35 cm)
move_duration_second = 3.00  # Time to move forward for the second segment (90 cm)
move_duration_third = 2.00  # Time to move forward for the third segment (60 cm)
move_duration_fourth = 2.67  # Time to move forward for the fourth segment (80 cm)
move_duration_final = 6.00  # Time to move forward for the final segment (180 cm)

def check_obstacle():
    """Check for an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def move_forward_with_obstacle_detection(duration):
    """Move the car forward for a specified duration with continuous obstacle detection."""
    end_time = time.time() + duration
    while time.time() < end_time:
        if check_obstacle():
            fc.stop()
            return True  # Obstacle detected
        fc.forward(speed)
        time.sleep(0.1)  # Small delay to avoid CPU overload
    fc.stop()
    return False  # No obstacle detected

def main():
    while True:
        # Move forward until an obstacle is detected
        if check_obstacle():
            # Turn right and move forward
            fc.turn_right(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper right turn
            fc.stop()

            if move_forward_with_obstacle_detection(move_duration_first):  # Move forward for the first distance
                continue  # If an obstacle is detected, restart the avoidance process

            # Turn left and move forward
            fc.turn_left(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper left turn
            fc.stop()

            if move_forward_with_obstacle_detection(move_duration_second):  # Move forward for the second distance
                continue  # If an obstacle is detected, restart the avoidance process

            # Turn left again and move forward
            fc.turn_left(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper left turn
            fc.stop()

            if move_forward_with_obstacle_detection(move_duration_third):  # Move forward for the third distance
                continue  # If an obstacle is detected, restart the avoidance process

            # Turn left one more time and move forward
            fc.turn_left(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper left turn
            fc.stop()

            if move_forward_with_obstacle_detection(move_duration_fourth):  # Move forward for the fourth distance
                continue  # If an obstacle is detected, restart the avoidance process

            # Final left turn to align the car back to the original path
            fc.turn_left(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper left turn
            fc.stop()

            if move_forward_with_obstacle_detection(move_duration_fourth):  # Move forward for the fourth distance
                continue  # If an obstacle is detected, restart the avoidance process

            # Final left turn to align the car back to the original path
            fc.turn_left(speed)
            time.sleep(turn_duration)  # Adjust the time to ensure a proper left turn
            fc.stop()


            # Move forward for the final distance (180 cm)
            move_forward_with_obstacle_detection(move_duration_final)
        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
