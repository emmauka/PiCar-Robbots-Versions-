import picar_4wd as fc
import time

# Speed of the car
speed = 30

# Distance in front of the car to consider an obstacle (in cm)
obstacle_threshold = 40

# Distances to move in each segment (in cm)
distances = {
    "move1": 40,     # Move forward for 40 cm
    "move2": 115,    # Move forward for 115 cm
    "move3": 62,     # Move forward for 62 cm
    "move4": 119,    # Move forward for 119 cm
    "move5": 91,     # Move forward for 91 cm
    "move6": 305     # Move forward for 305 cm
}

# Calculate move durations based on speed (cm/s)
cm_per_second = 20
durations = {key: val / cm_per_second for key, val in distances.items()}

# Define the route as a list of tuples (segment name, turn direction)
route = [
    ("move1", "right"), ("move2", "left"), ("move3", "right"),
    ("move4", "left"), ("move5", "right"), ("move6", "left")
]

def check_obstacle():
    """Check for obstacles directly ahead."""
    distance = fc.get_distance_at(0)
    return distance < obstacle_threshold

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def main():
    for segment, turn_direction in route:
        # Move forward in the current segment
        move_forward(durations[segment])
        
        # Continuously check for obstacles in the current segment
        while check_obstacle():
            fc.stop()
            print(f"Obstacle detected during {segment}. Performing turn.")
            
            # Perform the predefined turn based on route definition
            if turn_direction == "left":
                fc.turn_left(speed)
                time.sleep(0.5)  # Adjust the time as needed for a proper turn
            elif turn_direction == "right":
                fc.turn_right(speed)
                time.sleep(0.5)  # Adjust the time as needed for a proper turn
            
            # After the turn, move forward again in the current segment
            move_forward(durations[segment])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        fc.stop()
        print("\nProgram interrupted. Exiting.")
