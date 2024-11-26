import picar_4wd as fc
import time

speed = 30

distance_to_move_first = 40
move_duration_first = 1.33

distance_to_move_second = 123.55
move_duration_second = 4.17

distance_to_move_third = 69.00
move_duration_third = 2.27

distance_to_move_fourth = 124
move_duration_fourth = 2.73

obstacle_distance_threshold = 60  # Distance in centimeters to consider an obstacle

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def main():
    while True:
        # Move forward until an obstacle is detected
        fc.forward(speed)
        while True:
            scan_list = fc.scan_step(35)
            if scan_list:
                tmp = scan_list[3:7]
                if any(distance < obstacle_distance_threshold for distance in tmp):
                    fc.stop()
                    break  # Exit the loop if an obstacle is detected

        # Perform avoidance maneuvers after detecting an obstacle
        fc.turn_left(speed)
        time.sleep(0.50)  # Adjust the time to ensure a proper left turn
        fc.stop()
        move_forward(move_duration_first)

        fc.turn_right(speed)
        time.sleep(0.95)  # Adjust the time to ensure a proper right turn
        fc.stop()
        move_forward(move_duration_second)

        # Stop after the second turn before continuing
        fc.stop()
        time.sleep(wait_duration_after_second_turn)

        # Activate the sensor again after the second turn
        scan_list = fc.scan_step(35)
        tmp = scan_list[3:7]
        if any(distance < obstacle_distance_threshold for distance in tmp):
            print("Obstacle detected after second turn. Activating sensor.")

        # Continue with the next set of maneuvers after the second turn
        fc.turn_left(speed)
        time.sleep(0.50)  # Adjust the time to ensure a proper left turn
        fc.stop()
        move_forward(move_duration_third)

        fc.turn_right(speed)
        time.sleep(0.59)  # Adjust the time to ensure a proper right turn
        fc.stop()
        move_forward(move_duration_fourth)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
