import picar_4wd as fc
import time

speed = 26
obstacle_threshold = 10  # Distance in cm to consider an obstacle
scan_angle = 70  # Increase scan angle for faster coverage

# Movement durations (adjust as needed)
move_duration_short = 0.5
move_duration_long = 5.0

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
    scan_list = fc.scan_step(scan_angle)
    if not isinstance(scan_list, list):
        return False
    
    # Print the scan list for debugging
    print("Scan list:", scan_list)

    # Check the middle section of the scan list for obstacles
    middle_scan = scan_list[3:7]
    print("Middle scan section:", middle_scan)
    return any(distance < obstacle_threshold for distance in middle_scan)

def continuous_scan():
    """Continuously print scan results and check for obstacles."""
    while True:
        scan_list = fc.scan_step(scan_angle)
        if isinstance(scan_list, list):
            print("Scan list:", scan_list)
            middle_scan = scan_list[3:7]
            print("Middle scan section:", middle_scan)
            if any(distance < obstacle_threshold for distance in middle_scan):
                print("Obstacle detected!")
        else:
            print("Error: Scan did not return a valid list.")
        time.sleep(0.5)  # Adjust the delay as needed

def avoid_obstacle():
    """Perform maneuvers to avoid detected obstacles."""
    print("Avoiding obstacle")

    # Backup first
    move_backward(0.5)

    # Move forward for longer duration to avoid obstacle
    move_forward(move_duration_long)

    # Turn left and move forward
    turn_left(0.8)
    move_forward(move_duration_short)

    # Turn right and move forward
    turn_right(1.5)
    move_forward(move_duration_short)

    # Turn left and move forward
    turn_left(1.0)
    move_forward(move_duration_short)

    # Turn right to get back to the original direction
    turn_right(1.0)
    move_forward(move_duration_short)

def main():
    while True:
        if detect_obstacle():
            avoid_obstacle()
        else:
            move_forward(move_duration_short)
            time.sleep(0.1)  # Reduce delay for faster scanning

if __name__ == "__main__":
    try:
        # Uncomment the following line to perform continuous scanning for debugging
        # continuous_scan()
        
        main()
    finally:
        fc.stop()
