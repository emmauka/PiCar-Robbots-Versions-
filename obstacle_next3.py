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
            fc.stop()  # Stop the car
            # Decide whether to turn left or right based on obstacle position
            if scan_list[0] == 2:  # If the left side is clear
                fc.turn_left(speed)  # Turn left
            else:  # If the left side is not clear
                fc.turn_right(speed)  # Turn right
            time.sleep(0.5)  # Wait for a moment
            fc.stop()  # Stop the car
            continue  # Continue checking for obstacles
        fc.forward(speed)  # Move forward if no obstacle
    fc.stop()  # Stop the car after the duration

# Function to stop the car for a specified duration
def stop_car(duration):
    fc.stop()  # Stop the car
    time.sleep(duration)  # Wait for the specified duration

# Function to make a U-turn
def u_turn():
    fc.turn_left(speed)  # Turn left
    time.sleep(1.5)  # Wait for the U-turn to complete
    fc.stop()  # Stop the car

# Main function to execute the route with obstacle avoidance
def main():
    try:
        # First segment: Turn left and move forward
        fc.turn_left(speed)  # Turn left
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_first)  # Move forward for the first segment

        # Second segment: Turn right and move forward
        fc.turn_right(speed)  # Turn right
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_second)  # Move forward for the second segment

        # Third segment: Move forward with no turns
        move_forward(move_duration_third)  # Move forward for the third segment

        # Stop for 5 seconds at the destination
        stop_car(5)  # Stop the car for 5 seconds

        # Make a U-turn to return via the same path
        u_turn()  # Execute a U-turn

        # Return path: Reverse of the initial path

        # First segment of return path: Move forward
        move_forward(move_duration_third)  # Move forward for the third segment

        # Second segment of return path: Turn left and move forward
        fc.turn_left(speed)  # Turn left
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_second)  # Move forward for the second segment

        # Third segment of return path: Turn right and move forward
        fc.turn_right(speed)  # Turn right
        time.sleep(0.5)  # Wait for half a second
        fc.stop()  # Stop the car
        move_forward(move_duration_first)  # Move forward for the first segment

    finally:
        fc.stop()  # Ensure the car stops at the end

if __name__ == "__main__":
    main()  # Execute the main function
