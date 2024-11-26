import picar_4wd as fc
import time
import signal
import sys

# Constants and initial setup
Track_line_speed = 30        # Speed of the car (in cm/s)
zigzag_duration = 1          # Duration for each zig-zag motion (in seconds)
zigzag_cycles = 5            # Number of zig-zag cycles
turn_duration = 2            # Duration for a 180-degree turn (adjust as needed)
turn_speed = 60              # Speed for turning (adjust as needed)

# Signal handler function for Ctrl+C
def signal_handler(sig, frame):
    print("\nExiting and stopping the robot")
    fc.stop()                 # Stop the car
    sys.exit(0)               # Exit the program

# Function to perform a zig-zag motion
def zigzag_motion(cycles):
    for _ in range(cycles):  # Loop to repeat the zig-zag motion
        print("Moving forward in a zig-zag pattern...")
        # Move forward and turn left
        fc.forward(Track_line_speed)
        fc.turn_left(turn_speed)
        time.sleep(zigzag_duration)
        
        # Move forward and turn right
        fc.forward(Track_line_speed)
        fc.turn_right(turn_speed)
        time.sleep(zigzag_duration)

# Function to perform a 180-degree turn
def perform_180_turn():
    print("Performing a 180-degree turn...")
    fc.turn_left(turn_speed)  # Turn left for 180 degrees
    time.sleep(turn_duration) # Adjust duration for a full turn
    fc.stop()                 # Stop turning

# Function to move forward and perform zig-zag, then return
def drive_and_return():
    print("Moving from Startpunkt to Endpunkt")
    
    # Move forward in a zig-zag pattern
    zigzag_motion(zigzag_cycles)
    
    print("Reached destination")
    perform_180_turn()
    
    print("Moving back to the start point...")
    
    # Move back in a zig-zag pattern
    zigzag_motion(zigzag_cycles)
    
    print("Returned to start point")

# Main program execution
if __name__ == '__main__':
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Move forward until distance_traveled reaches stop_distance
        drive_and_return()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected")
        fc.stop()               # Stop the car if Ctrl+C is pressed
