import picar_4wd as fc
import time

speed = 30  # Speed of the car
distance_to_move = 60  # Distance to move in centimeters
move_duration = 2.65  # Time to move forward for 60 cm, this needs to be calibrated based on the car's speed
obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

def move_forward(distance):
    """Move the car forward for a specified distance."""
    fc.forward(speed)
    time.sleep(move_duration)  # Move for a duration that corresponds to 60 cm
    fc.stop()

def main():
    while True:
        # Scan for obstacles
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        # Check the middle section of the scan list for obstacles
        tmp = scan_list[3:7]
        print(tmp)
        
        # If an obstacle is detected (any distance less than the threshold), start avoidance
        if any(distance < obstacle_threshold for distance in tmp):
            # Turn right and move forward
            fc.turn_right(speed)
            time.sleep(1)  # Adjust the time to ensure a proper right turn
            fc.stop()
            
            move_forward(distance_to_move)
            
            # Turn left and move forward
            fc.turn_left(speed)
            time.sleep(1.1)  # Adjust the time to ensure a proper left turn
            fc.stop()
            
            move_forward(distance_to_move)
            
            # Turn left again and move forward
            fc.turn_left(speed)
            time.sleep(1)  # Adjust the time to ensure a proper left turn
            fc.stop()
            
            move_forward(distance_to_move)
            
            # Turn left one more time and move forward
            fc.turn_left(speed)
            time.sleep(1)  # Adjust the time to ensure a proper left turn
            fc.stop()
            
            move_forward(distance_to_move)
            
            # Stop for 2 seconds
            time.sleep(2)
            
            # Continue moving forward
            fc.forward(speed)
            time.sleep(5)  # Move forward for 5 seconds after avoiding the obstacle
            fc.stop()
            
        else:
            # Move forward if no obstacle is detected
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
