import picar_4wd as fc
import time
import threading

speed = 30

# Distances and durations for different movements
move_duration_first = 1.33
move_duration_second = 4.15
move_duration_third = 2.05
move_duration_fourth = 2.67
move_duration_fifth = 1.9
move_duration_sixth = 2.0
move_duration_seventh = 10.10

# Obstacle detection thresholds
initial_obstacle_threshold = 30  # Initial threshold in cm
close_obstacle_threshold = 20    # Closer threshold in cm

# Global variable to hold the latest scan data
latest_scan_data = []

# Thread function for continuous ultrasonic scanning
def continuous_scanning():
    global latest_scan_data
    while True:
        scan_list = []
        for angle in range(5, 200, 65):  # Rotate sensor to scan different angles
            distance = fc.get_distance_at(angle)
            scan_list.append(distance)
            time.sleep(0.3)
        latest_scan_data = scan_list

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def turn_right(duration):
    """Turn the car right for a specified duration."""
    fc.turn_right(speed)
    time.sleep(duration)
    fc.stop()

def turn_left(duration):
    """Turn the car left for a specified duration."""
    fc.turn_left(speed)
    time.sleep(duration)
    fc.stop()

def is_obstacle_detected(threshold):
    """Check if there is an obstacle within the given threshold distance."""
    global latest_scan_data
    if not latest_scan_data:
        return False

    # Check the middle section of the scan list for obstacles
    tmp = latest_scan_data[3:7]
    print(f"Obstacle distances: {tmp}")
    return any(distance is not None and distance < threshold for distance in tmp)

def main():
    obstacle_threshold = initial_obstacle_threshold

    # Start the continuous scanning thread
    scan_thread = threading.Thread(target=continuous_scanning)
    scan_thread.daemon = True
    scan_thread.start()

    while True:
        # Move forward initially
        move_forward(1)

        # Detect the first obstacle
        if is_obstacle_detected(obstacle_threshold):
            # Perform the first maneuver sequence
            turn_right(0.5)
            move_forward(move_duration_first)
            turn_left(0.8)
            move_forward(move_duration_second)

            # Change the obstacle threshold to a closer distance
            obstacle_threshold = close_obstacle_threshold

        # Continue with the rest of the predefined maneuvers
        while True:
            if is_obstacle_detected(obstacle_threshold):
                # Handle close obstacle detection within the predefined route
                turn_right(0.5)
                move_forward(1)
                turn_left(0.8)
                move_forward(1)
            else:
                # Continue following the predefined route
                move_forward(1)
                turn_right(0.5)
                move_forward(move_duration_third)
                turn_left(0.48)
                move_forward(move_duration_third)
                turn_left(0.3)
                move_forward(move_duration_fourth)

                # Additional obstacle avoidance maneuver
                if is_obstacle_detected(obstacle_threshold):
                    turn_left(0.5)
                    move_forward(move_duration_fifth)
                    turn_right(0.5)
                    move_forward(move_duration_sixth)
                else:
                    move_forward(move_duration_seventh)

                # Stop for 2 seconds
                time.sleep(2)

                # Continue moving forward for 2 seconds after avoiding the obstacle
                fc.forward(speed)
                time.sleep(2)
                fc.stop()
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
