import picar_4wd as fc
import time
import signal
import sys

# Constants for movement
FORWARD_SPEED = 30
TURN_SPEED = 40
STOP_DISTANCE = 20  # Distance to stop before an obstacle in cm
OBSTACLE_AVOID_DISTANCE = 30  # Distance to move around the obstacle in cm

# Signal handler for Ctrl+C
def signal_handler(sig, frame):
    print("\nExiting and stopping the robot")
    fc.stop()
    sys.exit(0)

# Function to move forward for a specified distance
def move_forward(distance_cm, speed=FORWARD_SPEED):
    duration = distance_cm / FORWARD_SPEED
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

# Function to turn right
def turn_right():
    fc.turn_right(TURN_SPEED)
    time.sleep(1.5)  # Adjust duration to achieve a 90-degree turn
    fc.stop()

# Function to turn left
def turn_left():
    fc.turn_left(TURN_SPEED)
    time.sleep(2.1)  # Adjust duration to achieve a 90-degree turn
    fc.stop()

# Function to scan with the servo
def scan_with_servo():
    servo = fc.Servo(1)
    for angle in range(60, 120, 5):
        servo.set_angle(angle)
        time.sleep(0.1)
    for angle in range(120, 60, -5):
        servo.set_angle(angle)
        time.sleep(0.1)
    servo.set_angle(90)  # Reset to the center

if __name__ == '__main__':
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Step 1: Move forward for 3 meters (300 cm)
        move_forward(300)

        # Step 2: Check for obstacle
        if fc.get_distance_at(0) < STOP_DISTANCE:
            fc.stop()
            time.sleep(1)

            # Step 3: Turn right and move forward 30 cm
            turn_right()
            move_forward(OBSTACLE_AVOID_DISTANCE)

            # Step 4: Turn left and move forward 60 cm
            turn_left()
            move_forward(OBSTACLE_AVOID_DISTANCE * 2)

            # Step 5: Turn left and move forward 30 cm
            turn_left()
            move_forward(OBSTACLE_AVOID_DISTANCE)

            # Step 6: Turn left and move forward 60 cm
            turn_left()
            move_forward(OBSTACLE_AVOID_DISTANCE * 2)

            # Step 7: Scan with the servo
            scan_with_servo()

            # Step 8: Move forward to return to start point (270 cm)
            turn_right()
            move_forward(300 - (OBSTACLE_AVOID_DISTANCE * 2 + OBSTACLE_AVOID_DISTANCE))
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected")
        fc.stop()
