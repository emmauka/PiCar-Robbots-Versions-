import RPi.GPIO as GPIO
import time

LED_PIN = 6  # Use GPIO 6 (D6)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)

def main():
    setup()
    try:
        while True:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
