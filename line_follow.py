import picar_4wd as fc
import time

# Constants for motor speeds and proportional gain
BASE_SPEED = 50
KP = 0.1  # Proportional gain, adjust this value based on testing

def follow_line():
    print("Starting line following...")
    try:
        while True:
            # Read grayscale values
            grayscale_values = fc.get_grayscale_list()
            print(f"Grayscale Values: {grayscale_values}")
            
            # Calculate error based on sensor readings
            error = calculate_error(grayscale_values)
            
            # Adjust motor speeds based on error
            adjust_motors(error)
            
            time.sleep(0.1)  # Adjust sleep time as needed for responsiveness
            
    except KeyboardInterrupt:
        print("Line following stopped.")
        fc.stop()

def calculate_error(grayscale_values):
    # Example: Calculate error based on left and right sensor readings
    left_sensor = grayscale_values[0]  # Adjust index based on sensor position
    right_sensor = grayscale_values[2]
    
    # Example error calculation (adjust as per your sensor and line configuration)
    error = left_sensor - right_sensor
    
    return error

def adjust_motors(error):
    # Example: Adjust motor speeds based on error
    correction = KP * error
    left_speed = BASE_SPEED - correction
    right_speed = BASE_SPEED + correction
    fc.forward(left_speed, right_speed)

if __name__ == '__main__':
    follow_line()
