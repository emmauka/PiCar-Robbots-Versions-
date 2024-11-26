import picar_4wd as fc
import time

speed = 30

def main():
    try:
        print("Moving forward...")
        fc.forward(speed)
        time.sleep(2)

        print("Turning right...")
        fc.turn_right(speed)
        time.sleep(2)

        print("Turning left...")
        fc.turn_left(speed)
        time.sleep(2)

        print("Stopping...")
        fc.stop()
    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        fc.stop()

if __name__ == "__main__":
    main()
