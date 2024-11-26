import picar_4wd as fc
import time

speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle
turn_duration = 0.90  # Duration to ensure a proper turn (adjust as necessary)

distance_to_move_first = 35  # Distance to move for the first turn in centimeters
move_duration_first = 1.17  # Calculated time to move forward for 35 cm

distance_to_move_second = 90  # Distance to move for the second turn in centimeters
move_duration_second = 3.00  # Calculated time to move for the 90 cm

distance_to_move_third = 60  # Distance to move for the third turn in centimeters
move_duration_third = 2.00  # Calculated time to move forward for 60 cm

distance_to_move_fourth = 80  # Distance to move for the fourth turn in centimeters
move_duration_fourth = 2.67  # Calculated time to move for 80 cm

def check_obstacle():
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
        time.sleep(0.1)  # Sleep briefly to allow for repeated checking
    fc.stop()
    return False  # No obstacle detected

def turn_and_check(turn_func, turn_duration):
    """Perform a turn and check for obstacles during the turn."""
    turn_func(speed)
    start_time = time.time()
    while time.time() - start_time < turn_duration:
        if check_obstacle():
            fc.stop()
            return True  # Obstacle detected
        time.sleep(0.1)
    fc.stop()
    return False  # No obstacle detected

def main():
    while True:
        # Move forward with continuous obstacle detection
        print("Moving forward...")
        if move_forward_with_obstacle_detection(2.0):
            print("Obstacle detected! Starting avoidance maneuvers.")
            
            # Turn right and move forward with obstacle detection
            if turn_and_check(fc.turn_right, turn_duration):
                continue

            if move_forward_with_obstacle_detection(move_duration_first):
                continue

            # Turn left and move forward with obstacle detection
            if turn_and_check(fc.turn_left, turn_duration):
                continue

            if move_forward_with_obstacle_detection(move_duration_second):
                continue

            # Turn left again and move forward with obstacle detection
            if turn_and_check(fc.turn_left, turn_duration):
                continue

            if move_forward_with_obstacle_detection(move_duration_third):
                continue

            # Turn left one more time and move forward with obstacle detection
            if turn_and_check(fc.turn_left, turn_duration):
                continue

            if move_forward_with_obstacle_detection(move_duration_fourth):
                continue

            # Stop for 2 seconds
            time.sleep(2)

        else:
            fc.forward(speed)
            time.sleep(0.1)  # Short sleep to allow time for obstacle detection
            fc.stop()

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
