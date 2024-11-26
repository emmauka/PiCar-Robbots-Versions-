import picar_4wd as fc
import time

# Constants
speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle
scan_angle_range = 90  # Angle range for left and right scanning
turn_duration = 0.5  # Duration to ensure a proper turn (adjust as necessary)
forward_duration = 1.0  # Duration to move forward after a turn

def check_obstacle():
    """Check for an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def scan_left_right():
    """Scan left and right and return the distances."""
    left_distance = fc.get_distance_at(scan_angle_range)  # Get distance to the left
    right_distance = fc.get_distance_at(-scan_angle_range)  # Get distance to the right
    return left_distance, right_distance

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
    """Avoid obstacle by scanning left and right and making a decision."""
    left_distance, right_distance = scan_left_right()

    if left_distance > obstacle_threshold and right_distance > obstacle_threshold:
        if left_distance > right_distance:
            turn_left_and_avoid()
        else:
            turn_right_and_avoid()
    elif left_distance > obstacle_threshold:
        turn_left_and_avoid()
    elif right_distance > obstacle_threshold:
        turn_right_and_avoid()
    else:
        # If both sides are blocked, try turning right first
        turn_right_and_avoid()
        
        # If still facing an obstacle, try turning left
        if check_obstacle():
            turn_left_and_avoid()

def realign_and_continue():
    """Realign the car and continue moving forward."""
    fc.forward(speed)
    time.sleep(forward_duration)  # Move forward for a set duration
    fc.stop()

    # Scan left and right to realign
    left_distance, right_distance = scan_left_right()

    # If more space on the left, turn left to realign
    if left_distance > right_distance:
        fc.turn_left(speed)
        time.sleep(turn_duration)
    else:
        # Otherwise, turn right to realign
        fc.turn_right(speed)
        time.sleep(turn_duration)
    fc.stop()

def main():
    while True:
        if check_obstacle():
            avoid_obstacle()
            realign_and_continue()
        else:
            move_forward_with_obstacle_detection()

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
