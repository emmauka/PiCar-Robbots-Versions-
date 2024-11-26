import picar_4wd as fc
import time

speed = 30  # Speed of the car
obstacle_threshold = 60  # Threshold distance in centimeters to consider an obstacle

def move_forward_until_obstacle():
    """Move the car forward continuously until an obstacle is detected in front."""
    print("Starting the car and moving forward.")
    fc.forward(speed)
    
    try:
        while True:
            # Perform a scan
            scan_list = fc.scan_step(35)
            if not scan_list:
                print("No scan data received. Continuing...")
                continue

            # Print the full scan list for debugging
            print("Scan list:", scan_list)

            # Check the middle section of the scan list for obstacles in front
            middle_index = len(scan_list) // 2
            front_distance = scan_list[middle_index]

            print("Front distance:", front_distance)

            # If an obstacle is detected directly in front, stop the car
            if front_distance < obstacle_threshold:
                print("Obstacle detected in front! Stopping...")
                fc.stop()
                break

            time.sleep(0.1)  # Check for obstacles every 0.1 seconds
    except KeyboardInterrupt:
        print("Stopping the car due to KeyboardInterrupt.")
        fc.stop()

if __name__ == "__main__":
    move_forward_until_obstacle()
