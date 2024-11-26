import picar_4wd as fc
import time

speed = 30
maneuver_time = 1  # Adjust based on your PiCar's speed and desired movement

def detect_obstacle():
    distance = fc.get_distance_at(0)  # Get distance directly in front
    print(f"Distance: {distance} cm")
    if distance < 30:  # Adjust this threshold based on your environment
        return True
    return False

def avoid_obstacle():
    print("Obstacle detected! Performing avoidance maneuvers...")
    fc.turn_right(speed)
    time.sleep(maneuver_time)
    fc.forward(speed)
    time.sleep(maneuver_time)
    fc.turn_left(speed)
    time.sleep(maneuver_time)
    fc.forward(speed)
    time.sleep(maneuver_time)
    fc.turn_left(speed)
    time.sleep(maneuver_time)
    fc.forward(speed)
    time.sleep(maneuver_time)
    fc.turn_left(speed)
    time.sleep(maneuver_time)
    fc.forward(speed)
    time.sleep(maneuver_time)
    print("Obstacle avoided. Continuing straight...")

def main():
    try:
        while True:
            if detect_obstacle():
                fc.stop()
                avoid_obstacle()
            else:
                fc.forward(speed)
            time.sleep(0.1)  # Adjust for better responsiveness
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
