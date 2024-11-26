import picar_4wd as fc
import time

# Constants
speed = 30
obstacle_threshold = 20  # Distance in front of the car to consider an obstacle (in cm)

# Move durations based on distances (in seconds)
move_durations = [
    (1.33, 40),  # (duration, distance)
    (3.83, 115),
    (2.05, 62),
    (2.67, 119),
    (1.9, 91),
    (10.17, 305)
]

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def reverse_and_turn():
    """Reverse a bit and turn left or right depending on obstacle location."""
    fc.backward(speed)
    time.sleep(0.5)
    fc.stop()

    # Scan for obstacles to determine direction to turn
    scan_list = fc.scan_step(35)
    
    # Debugging print to check the scan_list
    print(f"scan_list type: {type(scan_list)}, value: {scan_list}")

    if not isinstance(scan_list, list):
        print("Error: scan_list is not a list")
        return

    left_clear = all(distance > obstacle_threshold for distance in scan_list[:3])
    right_clear = all(distance > obstacle_threshold for distance in scan_list[-3:])

    if left_clear:
        fc.turn_left(speed)
        time.sleep(0.5)
        fc.stop()
    elif right_clear:
        fc.turn_right(speed)
        time.sleep(0.5)
        fc.stop()
    else:
        # If neither side is clear, just turn right by default
        fc.turn_right(speed)
        time.sleep(0.5)
        fc.stop()

def main():
    move_index = 0

    while move_index < len(move_durations):
        duration, distance = move_durations[move_index]

        # Move forward for the current segment
        move_forward(duration)
        move_index += 1

        # Check for obstacles periodically during each segment
        segment_duration = duration
        check_interval = 0.1
        start_time = time.time()

        while time.time() - start_time < segment_duration:
            scan_list = fc.scan_step(35)
            
            # Debugging print to check the scan_list
            print(f"scan_list type: {type(scan_list)}, value: {scan_list}")

            if not scan_list or not isinstance(scan_list, list):
                print("Error: scan_list is not a valid list")
                continue

            tmp = scan_list[3:7]
            print(tmp)

            if any(distance < obstacle_threshold for distance in tmp):
                reverse_and_turn()
                break
            time.sleep(check_interval)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
