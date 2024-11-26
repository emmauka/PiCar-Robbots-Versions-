import picar_4wd as fc
import time

speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle
turn_duration = 0.90  # Duration to ensure a proper turn (adjust as necessary)

def check_obstacle():
    """Check if there's an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def move_forward_until_obstacle():
    """Move forward continuously until an obstacle is detected."""
    while True:
        if check_obstacle():
            fc.stop()
            return  # Obstacle detected, stop moving forward
        fc.forward(speed)
        time.sleep(0.1)

def move_forward(duration):
    """Move forward for a specified duration."""
    end_time = time.time() + duration
    while time.time() < end_time:
        if check_obstacle():
            fc.stop()
            return True  # Obstacle detected
        fc.forward(speed)
        time.sleep(0.1)  # Sleep briefly to allow for repeated checking
    fc.stop()
    return False  # No obstacle detected

def turn_right():
    """Turn right for the specified duration."""
    fc.turn_right(speed)
    time.sleep(turn_duration)
    fc.stop()

def turn_left():
    """Turn left for the specified duration."""
    fc.turn_left(speed)
    time.sleep(turn_duration)
    fc.stop()

def main():
    print("Starting...")

    # Move straight until an obstacle is detected
    print("Moving forward until obstacle is detected...")
    move_forward_until_obstacle()

    # Perform turn and move sequences
    print("Performing avoidance maneuvers...")
    
    # Turn right and move forward with obstacle detection
    turn_right()
    if move_forward(1.17):  # Adjusted time to move forward
        return

    # Turn left and move forward with obstacle detection
    turn_left()
    if move_forward(3.00):  # Adjusted time to move forward
        return

    # Turn left again and move forward with obstacle detection
    turn_left()
    if move_forward(2.00):  # Adjusted time to move forward
        return

    # Turn left one more time and move forward with obstacle detection
    turn_left()
    if move_forward(2.67):  # Adjusted time to move forward
        return

    print("Finished avoidance maneuvers. Continuing forward...")
    move_forward_until_obstacle()  # Continue moving forward after avoidance

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
