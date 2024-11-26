import picar_4wd as fc
import time

# Constants
speed = 30
obstacle_threshold = 30  # Distance in cm to consider an obstacle
scan_threshold = 80  # Distance for a broader scan to find a clear path
scan_angle_range = 90  # Angle range for left and right scanning
turn_duration = 0.5  # Duration to ensure a proper turn (adjust as necessary)
reverse_duration = 1.0  # Duration to reverse when an obstacle is detected
goal_distance = 180  # Goal distance in cm

# Approximate values for distance calculations (adjust based on your car's speed and behavior)
cm_per_second = 20  # Approximate speed of the car in cm/s

# Global variables
distance_traveled = 0  # Total distance traveled by the car

def check_obstacle():
    """Check for an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def scan_left_right():
    """Scan left and right and return the distances."""
    left_distance = fc.get_distance_at(scan_angle_range)  # Get distance to the left
    right_distance = fc.get_distance_at(-scan_angle_range)  # Get distance to the right
    return left_distance, right_distance

def reverse_and_scan():
    """Reverse the car and perform a broader scan to find a clear path."""
    fc.backward(speed)
    time.sleep(reverse_duration)
    fc.stop()

    left_distance = fc.get_distance_at(scan_angle_range)  # Get distance to the left
    right_distance = fc.get_distance_at(-scan_angle_range)  # Get distance to the right
    front_distance = fc.get_distance_at(0)  # Get distance straight ahead

    return left_distance, right_distance, front_distance

def move_forward_with_obstacle_detection(duration):
    """Move the car forward with continuous obstacle detection and update distance traveled."""
    global distance_traveled
    end_time = time.time() + duration
    while time.time() < end_time:
        if check_obstacle():
            fc.stop()
            return True  # Obstacle detected
        fc.forward(speed)
        time.sleep(0.1)  # Small delay to avoid CPU overload
        distance_traveled += cm_per_second * 0.1  # Update distance traveled
        if distance_traveled >= goal_distance:
            fc.stop()
            return False  # Goal reached
    fc.stop()
    return False  # No obstacle detected

def turn_right_and_avoid():
    """Turn right and attempt to avoid the obstacle."""
    fc.turn_right(speed)
    time.sleep(turn_duration)  # Turn right
    fc.stop()
    move_forward_with_obstacle_detection(turn_duration)  # Move forward after turning

def turn_left_and_avoid():
    """Turn left and attempt to avoid the obstacle."""
    fc.turn_left(speed)
    time.sleep(turn_duration)  # Turn left
    fc.stop()
    move_forward_with_obstacle_detection(turn_duration)  # Move forward after turning

def avoid_obstacle():
    """Avoid obstacle by reversing, scanning, and making a decision."""
    left_distance, right_distance, front_distance = reverse_and_scan()

    if front_distance > scan_threshold:
        move_forward_with_obstacle_detection(0.5)  # Move forward if the path is clear
    elif left_distance > scan_threshold and right_distance > scan_threshold:
        if left_distance > right_distance:
            turn_left_and_avoid()
        else:
            turn_right_and_avoid()
    elif left_distance > scan_threshold:
        turn_left_and_avoid()
    elif right_distance > scan_threshold:
        turn_right_and_avoid()
    else:
        # If all directions are blocked, try turning right first
        turn_right_and_avoid()
        
        # If still facing an obstacle, try turning left
        if check_obstacle():
            turn_left_and_avoid()

def realign_and_continue():
    """Realign the car and continue moving forward."""
    fc.forward(speed)
    time.sleep(0.5)  # Move forward for a short duration to realign
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

def turn_around():
    """Turn the car around 180 degrees to face the starting point."""
    fc.turn_right(speed)
    time.sleep(1.8)  # Adjust this duration to achieve a 180-degree turn
    fc.stop()

def main():
    global distance_traveled
    start_time = time.time()

    while distance_traveled < goal_distance:
        if check_obstacle():
            avoid_obstacle()
            realign_and_continue()
        else:
            move_forward_with_obstacle_detection(0.1)  # Move forward in small increments

    # Stop the car when the goal is reached
    fc.stop()
    print("Goal reached! Total distance traveled:", distance_traveled, "cm")
    
    # Turn around to face the starting point
    turn_around()
    print("Car turned around to face the starting point.")

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
