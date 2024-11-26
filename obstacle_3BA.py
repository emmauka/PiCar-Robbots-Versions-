import picar_4wd as fc
import time


# Constants
speed = 30
obstacle_threshold = 20  # Distance in front of the car to consider an obstacle (in cm)

# Move durations based on distances (in seconds)
move_durations = [
    (1.33, 40),  # (duration, distance)
    (3.83, 115),
    (2.05, 62),
    (2.67, 119),
    (1.9, 91),
    (10.17, 305)
]

turn_durations = {
    "right": 0.5,
    "left": 0.5
}

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def turn(direction, duration):
    """Turn the car in the specified direction for a specified duration."""
    if direction == "left":
        fc.turn_left(speed)
    elif direction == "right":
        fc.turn_right(speed)
    time.sleep(duration)
    fc.stop()

def reverse_and_turn():
    """Reverse a bit and turn left or right depending on obstacle location."""
    fc.backward(speed)
    time.sleep(0.5)
    fc.stop()

    # Scan for obstacles to determine direction to turn
    scan_list = fc.scan_step(35)
    if not isinstance(scan_list, list):
        print("Error: scan_list is not a list")
        return

    left_clear = all(distance > obstacle_threshold for distance in scan_list[:3])
    right_clear = all(distance > obstacle_threshold for distance in scan_list[-3:])

    if left_clear:
        turn("left", turn_durations["left"])
    elif right_clear:
        turn("right", turn_durations["right"])
    else:
        # If neither side is clear, just turn right by default
        turn("right", turn_durations["right"])

def main():
    move_index = 0
    turns = ["right", "left", "right", "left", "right", "left"]

    while move_index < len(move_durations):
        duration, _ = move_durations[move_index]

        # Move forward for the current segment
        start_time = time.time()
        while time.time() - start_time < duration:
            # Scan for obstacles
            scan_list = fc.scan_step(35)
            if not isinstance(scan_list, list):
                print("Error: scan_list is not a list")
                continue

            # Check the middle section of the scan list for obstacles
            tmp = scan_list[3:7]
            print(tmp)

            # If an obstacle is detected (any distance less than the threshold), start avoidance
            if any(distance < obstacle_threshold for distance in tmp):
                reverse_and_turn()
                break

            # Keep moving forward if no obstacle is detected
            fc.forward(speed)

        fc.stop()

        # Perform the turn for this segment
        if move_index < len(turns):
            turn(turns[move_index], turn_durations[turns[move_index]])

        move_index += 1

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
