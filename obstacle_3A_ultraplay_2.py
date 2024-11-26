import picar_4wd as fc
import time

def move(direction, speed, duration=0.05):
    """Move the car in the specified direction with the given speed for the given duration."""
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

def execute_movements(lines):
    initial_time = None

    for i, line in enumerate(lines):
        parts = line.strip().split(',')
        timestamp = float(parts[-1])

        if initial_time is None:
            initial_time = timestamp

        if i > 0:
            previous_parts = lines[i - 1].strip().split(',')
            previous_timestamp = float(previous_parts[-1])
            duration = timestamp - previous_timestamp
        else:
            duration = 0.05  # Default duration for the first movement, can be adjusted

        if parts[0] == 'ultrasonic':
            scan_result = eval(parts[1])  # Assuming scan_result is a list
            print(f"Ultrasonic scan result: {scan_result}")
            # You might want to handle the scan result in some way here
        else:
            direction = parts[0]
            speed = int(parts[1])
            move(direction, speed, duration)

def main():
    with open('movements.txt', 'r') as file:
        lines = file.readlines()
        execute_movements(lines)

if __name__ == "__main__":
    main()
