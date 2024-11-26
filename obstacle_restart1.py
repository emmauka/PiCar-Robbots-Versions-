import picar_4wd as fc
import time

speed = 30

# Define distances and move durations for each segment
distances = {
    "move1": 40,     # Distance to move for the first turn in centimeters
    "move2": 118,    # Distance to move for the second turn in centimeters
    "move3": 62,     # Distance to move for the third turn in centimeters
    "move4": 119,    # Distance to move for the fourth turn in centimeters
    "move5": 91,     # Distance to move for the fifth turn in centimeters
    "move6": 305     # Distance to move for the sixth turn in centimeters
}

# Calculate move durations based on speed (cm/s)
cm_per_second = 20
durations = {key: val / cm_per_second for key, val in distances.items()}

obstacle_threshold = 10  # Distance in front of the car to consider an obstacle (in cm)

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def main():
    try:
        start_time = time.time()  # Record start time for timeout
        
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
                # Stop the car
                fc.stop()
                
                # Perform the predefined sequence of turns and movements
                if time.time() - start_time < 60:  # Perform route for max 60 seconds
                    fc.turn_right(speed)
                    time.sleep(0.50)  # Adjust time for a proper right turn
                    fc.stop()
                    move_forward(durations["move1"])
                    
                    fc.turn_left(speed)
                    time.sleep(0.80)  # Adjust time for a proper left turn
                    fc.stop()
                    move_forward(durations["move2"])
                    
                    fc.turn_right(speed)
                    time.sleep(0.50)  # Adjust time for a proper right turn
                    fc.stop()
                    move_forward(durations["move3"])
                    
                    fc.turn_left(speed)
                    time.sleep(0.48)  # Adjust time for a proper left turn
                    fc.stop()
                    move_forward(durations["move4"])
                    
                    fc.turn_right(speed)
                    time.sleep(0.40)  # Adjust time for a proper right turn
                    fc.stop()
                    move_forward(durations["move5"])
                    
                    fc.turn_left(speed)
                    time.sleep(0.30)  # Adjust time for a slight left turn
                    fc.stop()
                    move_forward(durations["move6"])
                
                else:
                    print("Max time reached. Exiting.")
                    break
            
            else:
                # No obstacle detected, move forward
                fc.forward(speed)
    
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
