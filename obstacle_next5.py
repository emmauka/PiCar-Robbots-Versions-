import picar_4wd as fc
import time

speed = 30
route_length = 5.0

def initialize_sensor():
    """
    Function to initialize the sensor to face forward.
    """
    try:
        fc.servo.set_angle(0)  # Adjust to set the sensor to face forward
        time.sleep(1)
    except Exception as e:
        print(f"Error initializing sensor: {str(e)}")
    print("Sensor initialized to face forward.")

def move_forward(duration):
    """
    Function to move the robot forward for a specified duration.
    """
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def turn_left():
    """
    Function to turn the robot left.
    """
    fc.turn_left(speed)
    time.sleep(0.5)
    fc.stop()

def turn_right():
    """
    Function to turn the robot right.
    """
    fc.turn_right(speed)
    time.sleep(0.5)
    fc.stop()

def u_turn():
    """
    Function to perform a U-turn.
    """
    fc.turn_left(speed)
    time.sleep(1.0)
    fc.stop()

def main():
    try:
        initialize_sensor()
        
        while True:
            scan_list = fc.scan_step(35)
            if not scan_list:
                continue

            tmp = scan_list[3:7]
            print("Scan Results:", tmp)

            if tmp == [2, 2, 2, 2]:
                move_forward(1.0)
                continue

            elif len(tmp) >= 4 and (tmp[1] == 1 or tmp[2] == 1):
                turn_left()
                move_forward(1.0)
                continue

            elif len(tmp) >= 4 and (tmp[1] == 0 or tmp[2] == 0):
                turn_right()
                move_forward(1.0)
                continue

            # Replace with appropriate distance check based on your hardware and library version
            if fc.distance() >= route_length:
                u_turn()
                break

    finally:
        fc.stop()

if __name__ == "__main__":
    main()
