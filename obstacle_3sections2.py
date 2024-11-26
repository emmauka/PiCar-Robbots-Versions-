import picar_4wd as fc
import time

def test_ultrasonic():
    try:
        # Initialize ultrasonic sensor
        trig_pin = fc.Pin('D4')
        echo_pin = fc.Pin('D5')
        us = fc.Ultrasonic(trig=trig_pin, echo=echo_pin)
        
        # Read distance
        distance = us.get_distance()
        print(f"Distance: {distance} cm")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_ultrasonic()
