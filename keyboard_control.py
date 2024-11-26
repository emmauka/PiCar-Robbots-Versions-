import picar_4wd as fc
import time

# Define sensor pins (adjust according to your setup)
SENSOR_LEFT_PIN = 0
SENSOR_RIGHT_PIN = 1

def setup():
    # Initialize your PiCar-4WD here (if needed)
    pass

def line_follow():
    while True:
        # Read sensor values
        left_val = fc.get_distance_at(SENSOR_LEFT_PIN)
        right_val = fc.get_distance_at(SENSOR_RIGHT_PIN)

        # Adjust this threshold based on your sensor readings
        threshold = 300

        if left_val < threshold and right_val < threshold:
            fc.forward(50)  # Move forward at 50% power
        elif left_val < threshold:
            fc.turn_left(30)  # Turn left slightly
        elif right_val < threshold:
            fc.turn_right(30)  # Turn right slightly
        else:
            fc.forward(50)  # Default to forward

        time.sleep(0.1)  # Adjust as needed for responsiveness

def main():
    setup()
    line_follow()

if __name__ == '__main__':
    main()
