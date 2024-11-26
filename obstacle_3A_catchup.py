import picar_4wd as fc
import time

speed = 25
distance_to_move_first = 40  # Distance to move for the first and turns in centimeters
move_duration_first = 1.33  # Calculated time to move forward for 35 cm

distance_to_move_second = 123.55  # Distance to move for the second and turns in centimeters
move_duration_second = 4.17  # Calculated time to move for the 35 cm

distance_to_move_third = 69.00  # Distance to move for the third turns in centimeters
move_duration_third = 2.27  # Calculated time to move forward for 85 cm

distance_to_move_fourth = 124  # Distance to move for the fourth and turns in centimeters
move_duration_fourth = 2.73  # Calculated time to move for 80 cm

distance_to_move_fifth = 125
move_duration_fifth = 3.00

distance_to_move_sixth = 60
move_duration_sixth = 2.0

distance_to_move_seventh = 235
move_duration_seventh = 6.60

obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

def precise_sleep(duration):
    """Sleep for a specified duration with high precision."""
    end_time = time.perf_counter() + duration
    while time.perf_counter() < end_time:
        pass

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    precise_sleep(duration)
    fc.stop()

def main():
    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]
        print(tmp)

        # If an obstacle is detected (any distance less than the threshold), start avoidance
        if any(distance < obstacle_threshold for distance in tmp):
            fc.turn_left(speed)
            precise_sleep(0.50)  # Adjust the time to ensure a proper left turn
            fc.stop()

            move_forward(move_duration_first)  # Move forward for the first distance

            # Turn right and move forward
            fc.turn_right(speed)
            precise_sleep(0.95)  # Adjust the time to ensure a proper right turn
            fc.stop()

            move_forward(move_duration_second)  # Move forward for the second distance

            # Turn left and move forward
            fc.turn_left(speed)
            precise_sleep(0.50)  # Adjust the time to ensure a proper left turn
            fc.stop()

            # Wait for 2 seconds before activating the sensor
            precise_sleep(2.0)

            # Activate the sensor and continue on the defined route
            scan_list = fc.scan_step(35)
            tmp = scan_list[3:7]
            if any(distance < obstacle_threshold for distance in tmp):
                print("Obstacle detected after second turn")

            move_forward(move_duration_third)  # Move forward for the third distance

            # Turn right and move forward
            fc.turn_right(speed)
            precise_sleep(0.59)  # Adjust the time to ensure a proper right turn
            fc.stop()

            move_forward(move_duration_fourth)  # Move forward for the fourth distance

            fc.turn_right(speed)
            precise_sleep(0.50)
            fc.stop()

            move_forward(move_duration_fifth)  # Move forward for the fifth distance

            fc.turn_left(speed)
            precise_sleep(0.50)
            fc.stop()

            move_forward(move_duration_sixth)  # Move forward for the sixth distance

            fc.turn_right(speed)
            precise_sleep(0.19)
            fc.stop()

            move_forward(move_duration_seventh)  # Move forward for the seventh distance

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
