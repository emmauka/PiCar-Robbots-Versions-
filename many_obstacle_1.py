import picar_4wd as fc
import time

# Constants
speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle (!!Adjust this to more or less sesitive to obstacle)
turn_duration = 0.5  # Duration to ensure a proper turn (adjust as necessary)
forward_duration = 1.0  # Duration to move forward after a turn

def check_obstacle():
    """Check for an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def move_forward_with_obstacle_detection():
    """Move the car forward with continuous obstacle detection."""
    while True:
        if check_obstacle():
            fc.stop()
            return  # Stop and return if an obstacle is detected
        fc.forward(speed)
        time.sleep(0.1)  # Small delay to avoid CPU overload

def turn_right_and_avoid():
    """Turn right and attempt to avoid the obstacle."""
    fc.turn_right(speed)
    time.sleep(turn_duration)  # Turn right
    fc.stop()

    move_forward_with_obstacle_detection()  # Move forward after turning

def turn_left_and_avoid():
    """Turn left and attempt to avoid the obstacle."""
    fc.turn_left(speed)
    time.sleep(turn_duration)  # Turn left
    fc.stop()

    move_forward_with_obstacle_detection()  # Move forward after turning

def avoid_obstacle():
    """Avoid obstacle by dynamically deciding to turn left or right."""
    # Try turning right first
    turn_right_and_avoid()
    
    # If still facing an obstacle, try turning left
    if check_obstacle():
        turn_left_and_avoid()

    # If still facing an obstacle, try turning left again (to align back)
    if check_obstacle():
        turn_left_and_avoid()

def main():
    while True:
        if check_obstacle():
            avoid_obstacle()
        else:
            fc.forward(speed)
            time.sleep(0.1)  # Small delay to avoid CPU overload

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
