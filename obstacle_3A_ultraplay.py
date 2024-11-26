import picar_4wd as fc
import time
import ast  # Import ast to safely evaluate scan_result

def play_movements(movements_file):
    movements = []

    # Read movements from file
    with open(movements_file, 'r') as file:
        for line in file:
            # Strip whitespace and split by comma
            parts = line.strip().split(',')
            
            # Ensure there are exactly 5 parts
            if len(parts) != 5:
                print(f"Ignoring malformed line: {line}")
                continue
            
            timestamp, action, speed, distance, scan_result_str = parts
            
            # Convert necessary values to appropriate types
            try:
                timestamp = float(timestamp)
                speed = int(speed)
                distance = float(distance)
                scan_result = ast.literal_eval(scan_result_str)  # Safely evaluate scan_result
            except ValueError as e:
                print(f"Error parsing line: {line}. Error: {e}")
                continue

            movements.append((timestamp, action, speed, distance, scan_result))

    # Initialize picar_4wd if necessary (check library documentation)
    # fc.setup()  # Uncomment or remove depending on library requirements

    try:
        for move in movements:
            timestamp, action, speed, distance, scan_result = move

            if action == 'forward':
                fc.forward(speed)
            elif action == 'backward':
                fc.backward(speed)
            elif action == 'left':
                fc.turn_left(speed)
            elif action == 'right':
                fc.turn_right(speed)
            elif action == 'stop':
                fc.stop()

            time.sleep(0.1)  # Adjust sleep time as necessary

    finally:
        fc.stop()
        # fc.close()  # Uncomment or remove depending on library requirements

def main():
    movements_file = 'movements.txt'
    play_movements(movements_file)

if __name__ == "__main__":
    main()
