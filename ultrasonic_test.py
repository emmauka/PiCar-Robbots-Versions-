import picar_4wd as fc
import time

def test_ultrasonic_sensor():
    """Test the ultrasonic sensor by printing distance readings continuously."""
    try:
        while True:
            distance = fc.get_distance_at(0)  # Get distance directly in front
            print(f"Distance: {distance} cm")
            time.sleep(0.5)  # Wait for 0.5 seconds before the next reading
    except KeyboardInterrupt:
        print("Test stopped by user.")
        fc.stop()

if __name__ == "__main__":
    test_ultrasonic_sensor()
