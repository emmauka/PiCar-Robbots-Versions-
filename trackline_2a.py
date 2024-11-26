import picar_4wd as fc
import time
import signal
import sys

# Constants and initial setup
Track_line_speed = 30        # Speed of the car (in cm/s)
stop_distance = 760          # Distance limit to stop (in cm)
reverse_duration = 2         # Duration to reverse (in seconds)
turn_duration = 2.5            # Duration for a 180-degree turn (adjust as needed)
turn_speed = 55

# Signal handler function for Ctrl+C
def signal_handler(sig, frame):
    print("\nExiting and stopping the robot")
    fc.stop()                 # Stop the car
    sys.exit(0)               # Exit the program

# Main program execution
if __name__ == '__main__':
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Move forward until distance_traveled reaches stop_distance
        start_time = time.time()
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            distance_traveled = Track_line_speed * elapsed_time  # Distance in cm

            if distance_traveled < stop_distance:
                fc.forward(Track_line_speed)
            else:
                # Stop the car
                fc.stop()
                time.sleep(1)  # Wait briefly before reversing

                # Turn around (180 degrees)
                fc.turn_left(Track_line_speed)  # Adjust direction as needed
                time.sleep(turn_duration)  # Adjust duration for a full turn

                # Stop turning and reverse for reverse_duration seconds
                fc.stop()
                fc.backward(Track_line_speed)
                time.sleep(reverse_duration)

                # Stop the car finally
                fc.stop()
                break  # Exit the loop once the sequence is completed

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected")
        fc.stop()               # Stop the car if Ctrl+C is pressed
