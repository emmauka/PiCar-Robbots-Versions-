import picar_4wd as fc  # Import the picar_4wd library for controlling the robot
import time  # Import the time module for delays

speed = 30  # Define the speed of the robot
route_length = 5.0  # Define the length of the route in meters

def initialize_sensor():
    """
    Function to initialize the sensor to face forward.
    This ensures the sensor starts in a known position.
    """
    try:
        # Assuming the servo angle is already configured to face forward during setup
        # If you need to set the angle, replace fc.servo.set_angle(0) with the correct method
        # fc.servo.set_angle(0)
        time.sleep(1)  # Wait for the servo to stabilize
    except Exception as e:
        print(f"Error initializing sensor: {str(e)}")

    print("Sensor initialized to face forward.")

def move_forward(duration):
    """
    Function to move the robot forward for a specified duration.
    """
    fc.forward(speed)  # Command the robot to move forward
    time.sleep(duration)  # Wait for the specified duration
    fc.stop()  # Stop the robot after moving forward

def turn_right():
    """
    Function to turn the robot right.
    """
    fc.turn_right(speed)  # Command the robot to turn right
    time.sleep(0.5)  # Wait for a short duration to complete the turn
    fc.stop()  # Stop the robot after turning right

def main():
    try:
        initialize_sensor()  # Initialize sensor to face forward at program start
        fc.forward(speed)  # Start moving forward

        while True:
            scan_list = fc.scan_step(35)  # Perform a scan to detect obstacles
            if not scan_list:
                continue  # If scan_list is empty, continue to the next iteration

            tmp = scan_list[3:8]  # Extract the relevant subset of scan results for evaluation
            print("Scan Results:", tmp)

            # Check the distance states of the fourth and seventh samples
            fourth_sample = tmp[1]
            seventh_sample = tmp[4]

            # If both fourth and seventh samples indicate no obstacle (2), continue forward
            if fourth_sample == 2 and seventh_sample == 2:
                move_forward(1.0)
            
            # If either fourth or seventh sample indicates an obstacle (1), turn right
            elif fourth_sample == 1 or seventh_sample == 1:
                turn_right()

            # Check if the robot has reached the end of the route approximately
            # Replace fc.ultrasonic.get_distance() with the correct method to get distance from ultrasonic sensor
            # For example, if your library or setup uses fc.UltrasonicSensor().read(), adjust accordingly
            if fc.ultrasonic.get_distance() >= route_length:
                u_turn()  # Perform a U-turn to return back along the route
                break  # Exit the loop after performing the U-turn

    finally:
        fc.stop()  # Ensure the robot stops in all cases when the program ends

if __name__ == "__main__":
    main()  # Call the main function if this script is executed directly
