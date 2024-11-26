import picar_4wd as fc
import time

def setup():
    print("Setting up the PiCar-4WD")
    fc.forward(0)  # Make sure the car is stopped

def read_sensors():
    grayscale_values = fc.get_grayscale_list()
    ref = [500, 500, 500]  # Example reference values, adjust these based on calibration
    fl_list = [1, 1, 1]    # Example follow line list, adjust these as needed
    line_status = fc.get_line_status(ref, fl_list)
    return grayscale_values, line_status

def line_follow():
    while True:
        grayscale_values, line_status = read_sensors()

        print(f"Grayscale Values: {grayscale_values}, Line Status: {line_status}")

        # Example threshold value, you might need to adjust this
        threshold = 500

        if line_status == "on_line":
            # Both sensors see the line, move forward
            fc.forward(30)
        elif line_status == "left":
            # Left sensor sees the line, turn left
            fc.turn_left(30)
        elif line_status == "right":
            # Right sensor sees the line, turn right
            fc.turn_right(30)
        else:
            # No sensors see the line, stop or adjust as needed
            fc.stop()

        time.sleep(0.1)  # Small delay to avoid excessive CPU usage

def main():
    setup()
    try:
        line_follow()
    except KeyboardInterrupt:
        print("Stopping the PiCar")
        fc.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
        fc.stop()

if __name__ == '__main__':
    main()
