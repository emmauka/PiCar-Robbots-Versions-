import picar_4wd as fc
import time

speed = 30

# Durations for different movements
move_duration_first = 1.33
move_duration_second = 4.07
move_duration_third = 2.13
move_duration_fourth = 2.70
move_duration_fifth = 2.40
move_duration_sixth = 2.0
move_duration_seventh = 6.60

obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

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

def scan_for_obstacle(direction):
    """Scan for obstacles in a specified direction."""
    if direction == 'right':
        angle = 45
    elif direction == 'left':
        angle = 135
    else:
        return False  # Invalid direction

    distance = fc.get_distance_at(angle)
    time.sleep(0.1)
    print(f"Obstacle distance at {direction}: {distance}")
    return distance < obstacle_threshold

def main():
    # Move straight initially until an obstacle is encountered
    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]
        print(tmp)

        if any(distance < obstacle_threshold for distance in tmp):
            # Perform the series of maneuvers when the first obstacle is encountered
            break
        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)
    
    fc.stop()  # Stop the car before starting maneuvers

    # List of movements and turns to follow
    movements = [
        ('right', move_duration_first),
        ('left', move_duration_second),
        ('right', move_duration_third),
        ('left', move_duration_fourth),
        ('right', move_duration_fifth),
        ('left', move_duration_sixth),
        ('right', move_duration_seventh)
    ]

    for direction, move_duration in movements:
        if scan_for_obstacle(direction):
            print(f"Obstacle detected when scanning {direction}. Proceeding to next segment.")
            continue  # Skip the turn if an obstacle is detected

        if direction == 'right':
            turn_right(0.50)  # Adjust this duration if necessary
        else:
            turn_left(0.50)  # Adjust this duration if necessary

        move_forward(move_duration)

    # Move forward until the endpoint destination
    fc.forward(speed)
    time.sleep(5)  # Adjust this time to ensure it reaches the endpoint
    fc.stop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
