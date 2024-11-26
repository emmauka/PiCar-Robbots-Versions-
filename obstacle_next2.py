import time
import picar_4wd as fc

speed = 30  # Define the speed of the car

# Define move durations for specific segments in seconds
move_duration_first = 2
move_duration_second = 2
move_duration_third = 2

# Function to move forward for a specified duration while checking for obstacles
def move_forward(duration):
    start_time = time.time()  # Record the start time
    while time.time() - start_time < duration:  # Loop for the specified duration
        scan_list = fc.scan_step(35)  # Scan the surroundings
        if not scan_list:  # If no scan data, continue
            continue
        tmp = scan_list[3:7]  # Get the front scan data
        if tmp != [2,2,2,2]:  # If any obstacle detected in the front
            fc.backward(speed)  # Move backward to avoid the obstacle
            time.sleep(0.5)  # Wait for a moment
            fc.stop()  # Stop the car
            fc.turn_left(speed)  # Adjust by turning left
            time.sleep(0.5)  # Wait for a moment
            fc.stop()  # Stop the car
            continue  # Continue checking for obstacles
        fc.forward(speed)  # Move forward if no obstacle
    fc.stop()  # Stop the car after the duration

# Function to stop the car for a specified duration
def stop_car(duration):
    fc.stop()  # Stop the car
    time.sleep(duration)  # Wait for the specified duration

# Function to move the car in a clockwise direction for a specified duration while checking for obstacles
def clockwise_move(duration):
    start_time = time.time()  # Record the start time
    while time.time() - start_time < duration:  # Loop for the specified duration
        scan_list = fc.scan_step(35)  # Scan the surroundings
        if not scan_list:  # If no scan data, continue
            continue
        tmp = scan_list[3:7]  # Get the front scan data
        if tmp != [2,2,2,2]:  # If any obstacle detected in the front
            fc.backward(speed)  # Move backward to avoid the obstacle
            time.sleep(0.5)  # Wait for a moment
            fc.stop()  # Stop the car
            fc.turn_left(speed)  # Adjust by turning left
            time.sleep(0.5)  # Wait for a moment
            fc.stop()  # Stop the car
            continue  # Continue checking for obstacles
        fc.forward(speed)  # Move forward if no obstacle
    fc.stop()  # Stop the car after the duration

# Main function to execute the route with obstacle avoidance
def main():
    try:
        # Turn left and move forward
        fc.turn_left(speed)  # Turn left
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_first)  # Move forward for the first segment

        # Turn right and move forward
        fc.turn_right(speed)  # Turn right
        time.sleep(0.10)  # Wait for 0.1 seconds
        fc.stop()  # Stop the car
        move_forward(move_duration_second)  # Move forward for the second segment

        # Stop for 3 seconds
        stop_car(3)  # Stop the car for 3 seconds

        # Turn left and move forward
        fc.turn_left(speed)  # Turn left
        time.sleep(0.8)  # Wait for 0.8 seconds
        fc.stop()  # Stop the car
        move_forward(move_duration_third)  # Move forward for the third segment

        # Clockwise movement
        clockwise_move(0.3)  # Move in a clockwise direction for 0.3 seconds

        # Stop for 3 seconds
        stop_car(3)  # Stop the car for 3 seconds

        # Turn right and move forward
        fc.turn_right(speed)  # Turn right
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_third)  # Move forward for the third segment again

        # Turn right again and move forward
        fc.turn_right(speed)  # Turn right
        time.sleep(0.48)  # Wait for 0.48 seconds
        fc.stop()  # Stop the car
        move_forward(move_duration_third)  # Move forward for the third segment again

        # Final left turn and move forward
        fc.turn_left(speed)  # Turn left
        time.sleep(0.4)  # Wait for 0.4 seconds
        fc.stop()  # Stop the car
        move_forward(move_duration_third)  # Move forward for the third segment again

        # Final right turn
        fc.turn_right(speed)  # Turn right
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car

    finally:
        fc.stop()  # Ensure the car stops at the end

if __name__ == "__main__":
    main()  # Execute the main function
