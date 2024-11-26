import picar_4wd as fc
import time

# Speed for the movements
speed = 30

def distance():
    scan_list = fc.scan_step(35)
    if not scan_list:
        return -1  # Return -1 if no valid scan
    return min(scan_list)  # Return the closest detected obstacle distance

def avoid_obstacle():
    print("Obstacle detected! Performing avoidance maneuvers...")
    # Perform right turn
    fc.turn_right(speed)
    time.sleep(1)  # Adjust sleep time to control the turn duration
    fc.stop()

    # Move forward
    fc.forward(speed)
    time.sleep(1)  # Adjust sleep time to control the forward duration
    fc.stop()

    # Perform left turn
    fc.turn_left(speed)
    time.sleep(1)  # Adjust sleep time to control the turn duration
    fc.stop()

    # Move forward
    fc.forward(speed)
    time.sleep(1)  # Adjust sleep time to control the forward duration
    fc.stop()

    # Perform left turn
    fc.turn_left(speed)
    time.sleep(1)  # Adjust sleep time to control the turn duration
    fc.stop()

    # Move forward
    fc.forward(speed)
    time.sleep(1)  # Adjust sleep time to control the forward duration
    fc.stop()

    # Perform left turn to re-align with initial direction
    fc.turn_left(speed)
    time.sleep(1)  # Adjust sleep time to control the turn duration
    fc.stop()

    # Move forward to continue on the path
    fc.forward(speed)
    time.sleep(1)  # Adjust sleep time to control the forward duration
    fc.stop()

    print("Obstacle avoided. Continuing straight...")

def main():
    try:
        while True:
            dist = distance()
            print(f"Distance: {dist:.2f} cm")
            if dist != -1 and dist < 30:  # If an obstacle is detected within 30 cm
                avoid_obstacle()
            else:
                fc.forward(speed)
            time.sleep(0.5)  # Adjust the loop delay as needed
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
