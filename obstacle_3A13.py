import picar_4wd as fc
import time

speed = 26
obstacle_threshold = 10  # Distance in front of the car to consider an obstacle

# Movement durations (adjust as needed)
move_duration_short = 0.50
move_duration_long = 5.00
move_duration_middle = 1.00

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def move_backward(duration):
    """Move the car backward for a specified duration."""
    fc.backward(speed)
    time.sleep(duration)
    fc.stop()

def turn_left(duration):
    """Turn the car left for a specified duration."""
    fc.turn_left(speed)
    time.sleep(duration)
    fc.stop()

def turn_right(duration):
    """Turn the car right for a specified duration."""
    fc.turn_right(speed)
    time.sleep(duration)
    fc.stop()

def detect_obstacle():
    """Scan for obstacles and return True if an obstacle is detected."""
    scan_list = fc.scan_step(35)
    if not isinstance(scan_list, list):
        return False

    # Print the scan list for debugging
    print("Scan list:", scan_list)

    # Check the middle section of the scan list for obstacles
    middle_scan = scan_list[3:7]
    print("Middle scan section:", middle_scan)
    return any(distance < obstacle_threshold for distance in middle_scan)

def avoid_obstacle():
    """Perform maneuvers to avoid detected obstacles."""
    print("Avoiding obstacle")

    # Backup first
    move_backward(0.5)
    fc.stop()

    # Turn left and move forward
    turn_left(0.8)
    move_forward(move_duration_short)
    fc.stop()

    # Turn right and move forward
    turn_right(1.5)
    move_forward(move_duration_short)
    fc.stop()

    # Turn left and move forward
    turn_left(1.0)
    move_forward(move_duration_short)
    fc.stop()

    # Final adjustment to the right
    turn_right(1.0)
    move_forward(move_duration_short)
    fc.stop()

def main():
    while True:
        if detect_obstacle():
            avoid_obstacle()
        else:
            move_forward(move_duration_short)
            time.sleep(0.1)  # Small delay to allow continuous scanning

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
