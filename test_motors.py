import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


class Motor:
    def __init__(self, forward_pin, backward_pin):
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.backward_pin, GPIO.OUT)


    def forward(self):
        GPIO.output(self.forward_pin, GPIO.HIGH)
        GPIO.output(self.backward_pin, GPIO.LOW)


    def backward(self):
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.HIGH)


    def stop(self):
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.LOW)



print("Initializing motors...")
motor_left_front = Motor(forward_pin=17, backward_pin=18)
motor_right_front =Motor(forward_pin=27, backward_pin=22)
motor_left_rear = Motor(forward_pin=23, backward_pin=24)
motor_right_rear = Motor(forward_pin=5, backward_pin=6)
print("Motors initialized.")


def test_motors():
    try:
        while True:
            print("Moving motors forward..")
            motor_left_front.forward()
            motor_right_front.forward()
            motor_left_rear.forward()
            motor_right_rear.forward()
            time.sleep(2)
            


            motor_left_front.backward()
            motor_right_front.backward()
            motor_left_rear.backward()
            motor_right_rear.backward()
            time.sleep(2)


            print("Stopping motors.")
            motor_left_front.stop()
            motor_right_front.stop()
            motor_left_rear.stop()
            motor_right_rear.stop()
            time.sleep(1)


    except KeyboardInterrupt:
        print("Ctrl+c pressed. Cleaning up GPIO...")
        GPIO.cleanup()


    except Exception as e:
        print(f"An error occured: {str(e)}")
        GPIO.cleanup()


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    test_motors()






































