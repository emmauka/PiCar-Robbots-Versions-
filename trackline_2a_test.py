import picar_4wd as fc
import time
import signal
import sys

# Constants and initial setup
Track_line_speed = 30        # Speed of the car (in cm/s)
stop_distance = 200          # Distance limit to stop (in cm)
reverse_duration = 2         # Duration to reverse (in seconds)
turn_duration_90 = 1.25      # Duration for a 90-degree turn (adjust as needed)
turn_speed = 55              # Speed for turning (adjust as needed)
parking_space_distance = 30  # Distance between parking spaces (in cm)
number_of_parking_spaces = 3 # Number of parking spaces to park in

# Signal handler function for Ctrl+C
def signal_handler(sig, frame):
    print("\nExiting and stopping the robot")
    fc.stop()                 # Stop the car
    sys.exit(0)               # Exit the program

# Function to move forward until reaching the stop distance
def move_forward_until_stop_distance():
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        distance_traveled = Track_line_speed * elapsed_time  # Distance in cm

        if distance_traveled < stop_distance:
            fc.forward(Track_line_speed)
        else:
            fc.stop()
            break

# Function to perform a 90-degree turn to the right
def turn_right_90():
    fc.turn_right(turn_speed)
    time.sleep(turn_duration_90)
    fc.stop()

# Function to perform a 90-degree turn to the left
def turn_left_90():
    fc.turn_left(turn_speed)
    time.sleep(turn_duration_90)
    fc.stop()

# Function to reverse and park
def reverse_and_park():
    fc.backward(Track_line_speed)
    time.sleep(reverse_duration)
    fc.stop()

# Function to move forward to the next parking space
def move_to_next_parking_space():
    fc.forward(Track_line_speed)
    time.sleep(parking_space_distance / Track_line_speed)
    fc.stop()

# Main program execution
if __name__ == '__main__':
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Move forward until distance_traveled reaches stop_distance
        move_forward_until_stop_distance()

        # Perform the parking routine in a row
        for _ in range(number_of_parking_spaces):
            # Turn right 90 degrees and reverse to park
            turn_right_90()
            reverse_and_park()
            
            # Turn left 90 degrees to face forward
            turn_left_90()
            
            # Move forward to the next parking space if not the last space
            if _ < number_of_parking_spaces - 1:
                move_to_next_parking_space()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected")
        fc.stop()               # Stop the car if Ctrl+C is pressed
