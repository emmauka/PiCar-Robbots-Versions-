import picar_4wd as fc
import time
import signal
import sys

speed = 30

def signal_handler(sig, frame):
    print("Exiting and stopping the robot")
    fc.stop()
    sys.exit(0)

def main():
    while True:
        scan_list = fc.scan_step(10)  # Adjusted to detect obstacles within 10 cm
        if not scan_list or len(scan_list) < 10:
            continue

        tmp = scan_list[3:7]
        print(tmp)
        
        # Check if any front scans detect an obstacle within 10 cm
        if any(distance < 10 for distance in tmp):
            # If obstacle detected, stop and evaluate
            fc.stop()
            time.sleep(0.1)

            # Check again to determine clear path
            scan_list = fc.scan_step(10)
            if not scan_list or len(scan_list) < 10:
                continue  # Skip iteration if scan_list is invalid
            
            left_clear = all(distance >= 10 for distance in scan_list[0:3])
            right_clear = all(distance >= 10 for distance in scan_list[7:10])

            if left_clear:
                print("Turning left to avoid obstacle")
                fc.turn_left(speed)
                time.sleep(0.5)
                fc.stop()
            elif right_clear:
                print("Turning right to avoid obstacle")
                fc.turn_right(speed)
                time.sleep(0.5)
                fc.stop()
            else:
                # If both sides are blocked, back up slightly and turn right as default
                print("Both sides blocked, attempting slight right")
                fc.backward(speed)
                time.sleep(0.5)
                fc.turn_right(speed)
                time.sleep(0.5)
        else:
            fc.forward(speed)  # No obstacle detected, move forward

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Register signal handler for Ctrl + C
    try:
        main()
    finally:
        fc.stop()
