import picar_4wd as fc
import time

speed = 30

# Durations for different movements
move_duration_first = 1.33
move_duration_second = 4.15
move_duration_third = 2.12
move_duration_fourth = 2.73
move_duration_fifth = 1.30
move_duration_sixth = 2.0
move_duration_seventh = 8.67

initial_obstacle_threshold = 30  # Initial distance in cm to consider an obstacle
close_obstacle_threshold = 15  # Closer distance in cm to consider an obstacle

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

def scan_for_obstacles():
    """Scan for obstacles at center, left, and right positions."""
    scan_list = []

    # Scan left
    distance = fc.get_distance_at(45)
    scan_list.append(distance)
    time.sleep(0.1)

    # Scan right
    distance = fc.get_distance_at(135)
    scan_list.append(distance)
    time.sleep(0.1)

    print(f"Obstacle distances: {scan_list}")

def main():
    obstacle_threshold = initial_obstacle_threshold

    while True:
        # Scan for obstacles initially
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]
        print(tmp)

        # If an obstacle is detected (any distance less than the threshold), start avoidance
        if any(distance < obstacle_threshold for distance in tmp):
            # Turn right and move forward
            turn_right(0.50)
            move_forward(move_duration_first)

            # Turn left and move forward
            turn_left(0.82)
            move_forward(move_duration_second)

            # Change obstacle detection threshold after first maneuvers
            obstacle_threshold = close_obstacle_threshold

            # Continue with the rest of the predefined maneuvers
            move_forward(1)

            # Remaining segments with formal obstacle scanning
            turn_right(0.51)
            move_forward(move_duration_third)
            scan_for_obstacles()
            time.sleep(2)

            turn_left(0.57)
            move_forward(move_duration_fourth)
            scan_for_obstacles()
            time.sleep(2)

            turn_right(0.42)
            move_forward(move_duration_fifth)
            scan_for_obstacles()
            time.sleep(2)

            turn_left(0.50)
            move_forward(move_duration_sixth)
            scan_for_obstacles()
            time.sleep(2)

            turn_right(0.12)
            move_forward(move_duration_seventh)
            scan_for_obstacles()
            time.sleep(2)

            # Stop for 2 seconds
            time.sleep(5)

            # Continue moving forward
            fc.forward(speed)
            time.sleep(2)
            fc.stop()
        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
