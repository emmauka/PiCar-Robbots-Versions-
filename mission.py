import picar_4wd as fc
import time

# Speed and time settings
speed = 30
travel_time_200cm = 7  # Adjust this value to match the time it takes for your PiCar to travel 120 cm
travel_time_80cm = 2   # Adjust this value to match the time it takes for your PiCar to travel 60 cm
turn_time_90_degrees = 1.5  # Adjust this value to match the time it takes for your PiCar to turn 90 degrees

def main():
    try:
        # Move forward for 120 cm
        print("Moving forward for 120 cm")
        fc.forward(speed)
        time.sleep(travel_time_200cm)
        fc.stop()

        # Perform right turn
        print("Turning right")
        fc.turn_right(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_80cm)
        fc.stop()

        # Perform left turn
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_80cm)
        fc.stop()

        # Perform left turn
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_80cm)
        fc.stop()

        # Perform left turn to realign with the initial direction
        print("Turning left")
        fc.turn_left(speed)
        time.sleep(turn_time_90_degrees)
        fc.stop()

        # Move forward for 60 cm
        print("Moving forward for 60 cm")
        fc.forward(speed)
        time.sleep(travel_time_80cm)
        fc.stop()

        # Wait for 2 seconds
        print("Waiting for 2 seconds")
        time.sleep(2)

        # Move forward for the remaining distance back to start
        print("Returning to start position")
        fc.forward(speed)
        time.sleep(travel_time_200cm)
        fc.stop()

        print("Mission complete!")

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
