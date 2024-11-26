import picar_4wd as fc
import time

# Speed and time settings
speed = 30
turn_time = 1.5  # Time for 90-degree turn
move_forward_times = [1.5, 3, 2, 6]  # Times for moving forward in each step after turning

def avoid_obstacle():
    # Perform right turn
    print("Turning right")
    fc.turn_right(speed)
    time.sleep(turn_time)  # Adjust time for a 90-degree turn
    fc.stop()

    for move_time in move_forward_times:
        print(f"Moving forward for {move_time} seconds")
        fc.forward(speed)
        time.sleep(move_time)  # Adjust time for the distance
        fc.stop()
        
        # Perform left turn if not the last forward movement
        if move_time != move_forward_times[-1]:
            print("Turning left")
            fc.turn_left(speed)
            time.sleep(turn_time)  # Adjust time for a 90-degree turn
            fc.stop()

def move_forward_until_obstacle():
    print("Moving forward until an obstacle is detected")
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2, 2, 2, 2]:  # Detected an obstacle
            fc.stop()
            avoid_obstacle()
            break

        fc.forward(speed)
        time.sleep(0.1)  # Short sleep to allow scan to proceed
    fc.stop()

def main():
    try:
        # Move forward until an obstacle is encountered
        move_forward_until_obstacle()

        # Wait for 2 seconds
        print("Waiting for 2 seconds")
        time.sleep(2)

        # Continue moving forward to the starting point
        print("Returning to start position")
        fc.forward(speed)
        time.sleep(10)  # Adjust time based on the actual distance to return to the start point
        fc.stop()

        print("Mission complete!")

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
