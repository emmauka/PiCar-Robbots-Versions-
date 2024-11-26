import picar_4wd as fc
import time
import keyboard

speed = 30

def manual_control():
    print("Manual control started. Use arrow keys to control the car. Press 'q' to quit.")

    try:
        while True:
            if keyboard.is_pressed('up'):
                fc.forward(speed)
                print("Moving forward")
            elif keyboard.is_pressed('down'):
                fc.backward(speed)
                print("Moving backward")
            elif keyboard.is_pressed('left'):
                fc.turn_left(speed)
                print("Turning left")
            elif keyboard.is_pressed('right'):
                fc.turn_right(speed)
                print("Turning right")
            elif keyboard.is_pressed('q'):
                print("Exiting manual control")
                break
            else:
                fc.stop()
                time.sleep(0.1)  # Small delay to prevent high CPU usage
    finally:
        fc.stop()

if __name__ == "__main__":
    manual_control()
