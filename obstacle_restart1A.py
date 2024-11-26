import picar_4wd as fc
import time

speed = 30

# Distances and durations for different movements
move_duration_first = 1.33
move_duration_second = 3.83
move_duration_third = 2.05
move_duration_fourth = 2.67
move_duration_fifth = 1.90
move_duration_sixth = 10.17

# Initial obstacle detection threshold
initial_obstacle_threshold = 30  # Initial threshold in cm
close_obstacle_threshold = 10    # Closer threshold in cm

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
    scan_list = fc.scan_step(35)
    if not scan_list:
        return False

    # Check the middle section of the scan list for obstacles
    tmp = scan_list[3:7]
    return any(distance < threshold for distance in tmp)

def main():
    obstacle_threshold = initial_obstacle_threshold

    # Move forward initially
    move_forward(1)

    while True:
        # Detect obstacles continuously
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
                # Perform predefined maneuvers if no close obstacle is detected
                move_forward(1)
                turn_right(0.5)
                move_forward(move_duration_third)
                turn_left(0.48)
                move_forward(move_duration_third)
                turn_left(0.3)
                move_forward(move_duration_fourth)

                # Stop for 2 seconds
                time.sleep(2)

                # Continue moving forward for 2 seconds after avoiding the obstacle
                move_forward(2)
                fc.stop()
                break

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
