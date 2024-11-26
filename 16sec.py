import picar_4wd as fc
import time

def move_forward(duration):
    fc.forward(50)  # Assuming 50% power, adjust as needed
    time.sleep(duration)
    fc.stop()

def move_backward(duration):
    fc.backward(50)
    time.sleep(duration)
    fc.stop()

def turn_left(duration):
    fc.turn_left(50)
    time.sleep(duration)
    fc.stop()

def turn_right(duration):
    fc.turn_right(50)
    time.sleep(duration)
    fc.stop()

def main():
    # Move forward in 6-second increments, stopping in between
    for _ in range(8):
        move_forward(6)
        time.sleep(1)  # Small pause between each 6-second move

    # Turn around to face backward
    turn_left(1)  # Adjust duration as needed to face backward

    # Move backward to park
    move_backward(2)  # Adjust duration as needed to reach the parking spot

if __name__ == '__main__':
    main()
