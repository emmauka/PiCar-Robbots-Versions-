import picar_4wd as fc
import time

speed = 26
distance_to_move_first = 40  # Distance to move for the first and turns in centimeters
move_duration_first = 1.33  # Calculated time to move forward for 35 cm

distance_to_move_second = 115  # Distance to move for the second and turns in centimeters
move_duration_second = 3.83  # Calculated time to move for the 35 cm

distance_to_move_third = 62  # Distance to move for the third turns in centimeters
move_duration_third = 2.05  # Calculated time to move forward for 85 cm

distance_to_move_fourth = 119  # Distance to move for the fourth and turns in centimeters
move_duration_fourth = 2.67  #Calculated time to move for 80 cm

distance_to_move_fifth = 91
move_duration_fifth =  1.9

distance_to_move_sixth = 305
move_duration_sixth = 10.17

obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()


def stop_car(duration):
    fc.stop()
    time.sleep(duration)

def adjust_ultrasonic(direction):
    """Adjust the ultrasonic sensor direction."""
    if direction == 'left':
        fc.turn_left(speed)
        time.sleep(0.5)  # Adjust time as needed
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
            fc.turn_left(speed)
            time.sleep(0.50)  # I can Adjust the time to ensure a proper right turn
            fc.stop()

            move_forward(move_duration_first)  # Move forward for 60 cm

            # Turn left and move forward
            fc.turn_right(speed)
            time.sleep(0.80)  # I can Adjust the time to ensure a proper left turn
            fc.stop()
            scan_list = fc.scan_step(45)

            move_forward(move_duration_second)  # Move forward for 60 cm
  
        if any(distance < obstacle_threshold for distance in tmp):
            fc.stop = stop_car(1)
        
            # Turn left again and move forward
            fc.turn_left(speed)
            time.sleep(0.50)  # I can Adjust the time to ensure a proper left turn
            fc.stop()
            scan_list = fc.scan_step(45)

            fc.wait(1)
            time.sleep(1)

            move_forward(move_duration_third)  # Move forward for 80 cm

            # Turn left one more time and move forward
            fc.turn_right(speed)
            time.sleep(0.48)  # Adjust the time to ensure a proper left turn
            fc.stop()

            fc.turn_left(speed)
            time.sleep(0.40)
            fc.stop()

            move_forward(move_duration_third)

            fc.turn_left(speed)
            time.sleep(0.30)
            fc.stop()

            move_forward(move_duration_fourth)  # Move forward for 80 cm

            # Stop for 2 seconds
            time.sleep(2)

            # Continue moving forward
            fc.forward(speed)
            time.sleep(2)  # Move forward for 5 seconds after avoiding the obstacle
            fc.stop()

        else:
            # Move forward if no obstacle is detected
                        fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()

