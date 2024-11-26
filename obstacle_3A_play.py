import picar_4wd as fc
import time

speed = 30

def move(direction, speed, duration):
    if direction == 'forward':
        fc.forward(speed)
    elif direction == 'backward':
        fc.backward(speed)
    elif direction == 'left':
        fc.turn_left(speed)
    elif direction == 'right':
        fc.turn_right(speed)
    time.sleep(duration)
    fc.stop()

def main():
    movements = []
    with open('recorded_movements.txt', 'r') as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            current = lines[i].strip().split(',')
            previous = lines[i - 1].strip().split(',')
            duration = float(current[2]) - float(previous[2])
            movements.append((previous[0], int(previous[1]), duration))

    for move in movements:
        move(*move)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        fc.stop()
        print("Car stopped.")
