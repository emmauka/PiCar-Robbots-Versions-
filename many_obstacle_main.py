import picar_4wd as fc  # Import the Picar 4WD library
import time  # Import the time library for delays

# Constants
speed = 30  # Speed of the car
obstacle_threshold = 1  # Distance in cm to consider an obstacle

# Distances in feet, converted to cm (1 foot = 30.48 cm)
feet_to_cm = 30.48
distances = {
    "initial_forward": 6 * feet_to_cm,  # 6 feet forward movement
    "right_turn": 1.5 * feet_to_cm,  # 1.5 feet forward after turning right
    "left_turn_1": 3.4 * feet_to_cm,  # 3.4 feet forward after turning left
    "forward_2": 2 * feet_to_cm,  # 2 feet forward
    "left_turn_2": 3.9 * feet_to_cm,  # 3.9 feet forward after turning left again
    "right_turn_2": 3 * feet_to_cm,  # 3 feet forward after turning right again
    "final_forward": 10 * feet_to_cm,  # 10 feet forward
}

# Time durations for movements based on speed (cm/s)
cm_per_second = 20  # Approximate speed of the car in cm/s
durations = {key: val / cm_per_second for key, val in distances.items()}  # Calculate durations for each distance

def check_obstacle():
    """Check for an obstacle directly in front of the car."""
    distance = fc.get_distance_at(0)  # Get distance directly ahead
    return distance < obstacle_threshold  # Return True if obstacle is within threshold, else False

def move_forward_with_obstacle_detection(duration):
    """Move the car forward with continuous obstacle detection."""
    end_time = time.time() + duration  # Calculate end time for movement
    while time.time() < end_time:  # Move forward until the end time is reached
        if check_obstacle():  # Check for obstacle
            fc.stop()  # Stop the car if obstacle is detected
            return True  # Return True indicating an obstacle was detected
        fc.forward(speed)  # Move the car forward
        time.sleep(0.1)  # Small delay to avoid CPU overload
    fc.stop()  # Stop the car after moving forward for the specified duration
    return False  # Return False indicating no obstacle was detected

def turn_right():
    """Turn the car slightly right."""
    fc.turn_right(speed)  # Turn the car right
    time.sleep(0.45)  # Adjust time for slight right turn (fine-tune as necessary)
    fc.stop()  # Stop the car after turning

def turn_left():
    """Turn the car slightly left."""
    fc.turn_left(speed)  # Turn the car left
    time.sleep(0.45)  # Adjust time for slight left turn (fine-tune as necessary)
    fc.stop()  # Stop the car after turning

def main():
    # Initial forward movement (6 feet)
    if move_forward_with_obstacle_detection(durations["initial_forward"]):
        print("Obstacle detected during initial forward movement.")
        return  # Stop the program if obstacle is detected

    # Turn slight right and move forward (1.5 feet)
    turn_right()
    if move_forward_with_obstacle_detection(durations["right_turn"]):
        print("Obstacle detected during right turn movement.")
        return  # Stop the program if obstacle is detected

    # Turn slight left and move forward (3.4 feet)
    turn_left()
    if move_forward_with_obstacle_detection(durations["left_turn_1"]):
        print("Obstacle detected during first left turn movement.")
        return  # Stop the program if obstacle is detected

    # Move forward (2 feet)
    if move_forward_with_obstacle_detection(durations["forward_2"]):
        print("Obstacle detected during second forward movement.")
        return  # Stop the program if obstacle is detected

    # Turn slight left and move forward (3.9 feet)
    turn_left()
    if move_forward_with_obstacle_detection(durations["left_turn_2"]):
        print("Obstacle detected during second left turn movement.")
        return  # Stop the program if obstacle is detected

    # Turn slight right and move forward (3 feet)
    turn_right()
    if move_forward_with_obstacle_detection(durations["right_turn_2"]):
        print("Obstacle detected during second right turn movement.")
        return  # Stop the program if obstacle is detected

    # Turn slight left and move forward (10 feet)
    turn_left()
    if move_forward_with_obstacle_detection(durations["final_forward"]):
        print("Obstacle detected during final forward movement.")
        return  # Stop the program if obstacle is detected

    print("Task completed successfully. Goal reached.")  # Indicate that the task is completed

if __name__ == "__main__":
    try:
        main()  # Run the main function
    finally:
        fc.stop()  # Ensure the car stops if the program is interrupted
