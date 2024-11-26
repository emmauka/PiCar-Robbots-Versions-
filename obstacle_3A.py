import picar_4wd as fc
import time

speed = 30
obstacle_threshold = 2  # Distance in cm to consider an obstacle
fc.forward(180.00)

# Movement durations for specific distances (based on your format)
distance_to_move_first = 40
move_duration_first = 1.33

distance_to_move_second = 123.78
move_duration_second = 4.23

distance_to_move_third = 66
move_duration_third = 2.13

distance_to_move_fourth = 128
move_duration_fourth = 2.76

distance_to_move_fifth = 94
move_duration_fifth = 2.38

distance_to_move_sixth = 60
move_duration_sixth = 2.0

distance_to_move_seventh = 270
move_duration_seventh = 6.98

def move_forward(duration):
    start_time = time.perf_counter()
    fc.forward(speed)
    while time.perf_counter() - start_time < duration:
        time.sleep(0.01)
    fc.stop()

def turn_right(duration):
    start_time = time.perf_counter()
    fc.turn_right(speed)
    while time.perf_counter() - start_time < duration:
        time.sleep(0.01)
    fc.stop()

def turn_left(duration):
    start_time = time.perf_counter()
    fc.turn_left(speed)
    while time.perf_counter() - start_time < duration:
        time.sleep(0.01)
    fc.stop()

def main():
    while True:
        # Scan for obstacles
        distance = fc.get_distance_at(0)  # Scan the front directly

        if distance < obstacle_threshold:
            # First obstacle detected: turn right
            turn_right(0.50)
            move_forward(move_duration_first)
            
            # Continue moving and scanning after the first turn
            while True:
                distance = fc.get_distance_at(0)
                if distance < obstacle_threshold:
                    # Second obstacle detected: turn left
                    turn_left(0.80)
                    move_forward(move_duration_second)
                    
                    # Continue moving and scanning after the second turn
                    while True:
                        distance = fc.get_distance_at(0)
                        if distance < obstacle_threshold:
                            # Third obstacle detected: turn right
                            turn_right(0.55)
                            move_forward(move_duration_third)
                            
                            # Fourth obstacle detected: turn left again
                            while True:
                                distance = fc.get_distance_at(0)
                                if distance < obstacle_threshold:
                                    turn_left(0.58)
                                    move_forward(move_duration_fourth)
                                    break  # Exit the loop after the fourth turn
                            break  # Exit the loop after the third turn
                    break  # Exit the loop after the second turn
        else:
            # Move forward if no obstacle is detected
            start_time = time.perf_counter()
            fc.forward(speed)
            while time.perf_counter() - start_time < 0.1:
                time.sleep(0.01)
            fc.stop()

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
