import picar_4wd as fc
import time

speed = 30

# Define distances and durations for each segment of the route
route_segments = [
    ("straight", 118, 3.93),  # (move direction, distance in cm, move duration in seconds)
    ("right", 40, 1.33),
    ("left", 118, 3.93),
    ("right", 62, 2.07),
    ("left", 119, 3.97),
    ("right", 91, 3.03),
    ("slight_left", 305, 10.17),
]

obstacle_threshold = 10  # Adjust as needed for your specific setup

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def calibrate_sensor():
    """Calibrate the ultrasonic sensor for optimal performance."""
    # Example calibration settings (adjust as per your sensor's requirements)
    # Typically, this would involve setting the range and sensitivity
    # Example:
    # fc.sensor.set_range(200)  # Set detection range to 200 cm
    # fc.sensor.set_sensitivity(2)  # Set sensitivity level 2
    pass  # Replace with actual calibration steps based on your sensor's API

def main():
    # Perform sensor calibration before starting the main loop
    calibrate_sensor()

    current_segment_index = 0

    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue
        
        # Check if there's an obstacle in front
        if any(distance < obstacle_threshold for distance in scan_list):
            print("Obstacle detected. Stopping and performing turn.")
            # Perform turn based on the current segment definition
            segment = route_segments[current_segment_index]
            if segment[0] == "right":
                fc.turn_right(speed)
                time.sleep(0.50)
            elif segment[0] == "left":
                fc.turn_left(speed)
                time.sleep(0.80)
            elif segment[0] == "slight_left":
                fc.turn_left(speed)
                time.sleep(0.30)

            fc.stop()

            # Move forward according to the segment definition
            move_forward(segment[2])

            # Move to the next segment
            current_segment_index += 1

            # Check if all segments are completed
            if current_segment_index >= len(route_segments):
                print("Destination reached.")
                break

        else:
            # Move forward if no obstacle detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
