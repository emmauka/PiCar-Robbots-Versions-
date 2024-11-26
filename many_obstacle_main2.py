import picar_4wd as fc
import time

speed = 30  # Speed of the car
obstacle_threshold = 30  # Distance in cm to consider an obstacle
turn_duration = 0.5  # Duration to ensure a proper turn (adjust as necessary)

# Distances for each segment of the path in cm
distances = {
    "straight1": 180,  # Move forward straight for 180 cm (6 feet)
    "right1": 45,      # Move forward 1.5 feet (45 cm) after right turn
    "left1": 103,      # Move forward 3.4 feet (103 cm) after left turn
    "forward1": 60,    # Move forward for 2 feet (60 cm)
    "left2": 119,      # Move forward 3.9 feet (119 cm) after left turn
    "right2": 91,      # Move forward 3 feet (91 cm) after right turn
    "left3": 305       # Move forward 10 feet (305 cm) after left turn
}

# Time durations for movements based on speed (cm/s)
cm_per_second = 20  # Approximate speed of the car in cm/s
durations = {key: val / cm_per_second for key, val in distances.items()}  # Calculate durations for each distance

def check_obstacle():
    """Check for obstacles directly ahead."""
    distance = fc.get_distance_at(0)  # Get distance straight ahead
    return distance < obstacle_threshold

def move_forward(duration):
    """Move the car forward for a specified duration with continuous obstacle detection."""
    end_time = time.time() + duration
    while time.time() < end_time:
        if check_obstacle():
            fc.stop()
            return True  # Obstacle detected
        fc.forward(speed)
    fc.stop()
    return False  # No obstacle detected

def move_with_no_detection(duration):
    """Move the car forward for a specified duration without obstacle detection."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def main():
    # Move straight initially until an obstacle is detected or distance is covered
    if move_forward(durations["straight1"]):
        print("Obstacle detected during initial forward movement.")
    
    # Now perform the maneuvers without further obstacle detection
    fc.turn_right(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["right1"])

    fc.turn_left(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["left1"])

    fc.turn_left(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["forward1"])

    fc.turn_left(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["left2"])

    fc.turn_right(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["right2"])

    fc.turn_left(speed)
    time.sleep(turn_duration)
    fc.stop()
    move_with_no_detection(durations["left3"])
    
    # After completing the path, stop the car and turn to face the opposite direction
    fc.turn_left(speed)
    time.sleep(2 * turn_duration)  # 180-degree turn to face the opposite direction
    fc.stop()

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
