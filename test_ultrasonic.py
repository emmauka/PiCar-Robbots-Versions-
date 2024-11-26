import RPi.GPIO as GPIO
import time

# Define GPIO pins for the ultrasonic sensor
TRIG_PIN = 18
ECHO_PIN = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(2)  # Allow the sensor to settle

def distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Distance in cm
    return distance

def main():
    setup()
    try:
        while True:
            dist = distance()
            print(f"Measured Distance: {dist:.2f} cm")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
