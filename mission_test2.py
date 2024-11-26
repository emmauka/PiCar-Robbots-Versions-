import picar_4wd as fc
import time

# Speed and time settings
speed = 30
travel_time_120cm = 4  # Time to travel 120 cm
travel_time_60cm = 2   # Time to travel 60 cm
turn_time_90_degrees = 3  # Time to turn 90 degrees

def avoid_obstacle():
    # Stop the car before turning
    fc.stop()
    time.sleep(1)

    # Perform right turn to avoid obstacle
    print("Obstacle detected! Turning right to avoid...")
    fc.turn_right(speed)
    time.sleep(turn_time_90_degrees)
    fc.stop()

def move_forward_and_check_obstacles(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        if tmp != [2,2,2,2]:
            avoid_obstacle()
            break

        fc.forward(speed)
        time.sleep(0.1)  # Short sleep to allow scan to proceed
    fc.stop()

def main():
    try:
        # Move forward for 120 cm or until an obstacle is detected
        print("Moving forward for 120 cm or until an obstacle is detected")
        move_forward_and_check_obstacles(travel_time_120cm)

        # Perform right turn
        print("Turning right")
        fc.turn_right(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_60cm)
        fc.stop()

        # Perform left turn
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_60cm)
        fc.stop()

        # Perform left turn
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_60cm)
        fc.stop()

        # Perform left turn to realign with the initial direction
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_60cm)
        fc.stop()

        # Wait for 2 seconds
        print("Waiting for 2 seconds")
        time.sleep(2)

        # Move forward for the remaining distance back to start
        print("Returning to start position")
        fc.forward(speed)
        time.sleep(travel_time_120cm)
        fc.stop()

        print("Mission complete!")

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
