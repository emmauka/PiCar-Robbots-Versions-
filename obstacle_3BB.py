import picar_4wd as fc
import time

speed = 30  # Speed of the car
obstacle_threshold = 80  # Threshold distance in centimeters to consider an obstacle

def move_forward_until_obstacle():
    """Move the car forward continuously until an obstacle is detected in front."""
    fc.forward(speed)
    while True:
        # Perform a scan
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

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

if __name__ == "__main__":
    try:
        move_forward_until_obstacle()
    except KeyboardInterrupt:
        fc.stop()
