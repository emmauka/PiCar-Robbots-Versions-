import picar_4wd as fc

speed = 30

def main():
    while True:
        scan_list = fc.scan_step(20)  # Fine resolution scan
        if not scan_list:
            continue

        front_scan = scan_list[3:7]  # Assuming this scans the front area

        print("Scan List:", scan_list)

        # Check if there is an obstacle within 30 cm
        if any(distance < 15 for distance in front_scan):
            fc.turn_right(speed)  # Turn right to avoid obstacle
        else:
            fc.forward(speed)  # Proceed forward if no obstacle detected

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()  # Stop the car when the script terminates
