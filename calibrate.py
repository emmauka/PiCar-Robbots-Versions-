import picar_4wd as fc
import time
import signal
import sys
from picar_4wd.servo import Servo

# Constants and initial setup
Track_line_speed = 30        # Speed of the car (in cm/s)
stop_distance = 760          # Distance limit to stop (in cm)
reverse_duration = 2         # Duration to reverse (in seconds)
turn_duration = 2.5          # Duration for a 180-degree turn (adjust as needed)
turn_speed = 55              # Speed for turning

# Initialize the servo motor
servo_pin = 1  # Assuming the servo is connected to pin 1
servo = Servo(servo_pin)  # Initialize the servo with the appropriate pin

# Signal handler function for Ctrl+C
def signal_handler(sig, frame):
    print("\nExiting and stopping the robot")
    fc.stop()                 # Stop the car
    sys.exit(0)               # Exit the program

# Function to perform a 180-degree turn
def perform_180_turn():
    fc.turn_left(turn_speed)  # Turn left for 180 degrees
    time.sleep(turn_duration) # Adjust duration for a full turn
    fc.stop()                 # Stop turning

# Function to scan with sensors using the servo motor
def scan_with_sensors():
    print("Scanning with sensors...")

    # Turn servo to the left to scan
    servo.set_angle(45)  # Adjust angle as needed
    time.sleep(1)
    
    # Read sensor values (simulated)
    print("Scanning left:", fc.get_grayscale_list())
    
    # Turn servo to the center
    servo.set_angle(0)
    time.sleep(0.5)
    
    # Turn servo to the right to scan
    servo.set_angle(-45)  # Adjust angle as needed
    time.sleep(1)
    
    # Read sensor values (simulated)
    print("Scanning right:", fc.get_grayscale_list())
    
    # Return servo to the center
    servo.set_angle(0)
    time.sleep(0.5)
    
    print("Scanning complete.")

# Function to drive forward and return to start point
def drive_and_return():
    global stop_distance

    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        distance_traveled = Track_line_speed * elapsed_time  # Distance in cm

        if distance_traveled < stop_distance:
            fc.forward(Track_line_speed)
        else:
            fc.stop()
            scan_with_sensors()  # Perform sensor scan at the stop point

            perform_180_turn()
            time.sleep(1)  # Wait briefly after turn

            # Reverse briefly
            fc.backward(Track_line_speed)
            time.sleep(reverse_duration)
            fc.stop()
            scan_with_sensors()  # Perform sensor scan after reversing
            time.sleep(1)  # Wait after reversing

            # Drive forward to return to start point
            start_time = time.time()  # Reset start time
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_time
                distance_traveled = Track_line_speed * elapsed_time  # Distance in cm

                if distance_traveled < stop_distance:
                    fc.forward(Track_line_speed)
                else:
                    fc.stop()
                    break  # Exit the loop once returned to start point

            break  # Exit the outer loop once returned to start point

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
