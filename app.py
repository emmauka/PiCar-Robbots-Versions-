from flask import Flask, render_template_string, request, redirect, url_for
import picar_4wd as fc
import time
import threading

app = Flask(__name__)

speed = 30
distance_to_move_first = 35  # Distance to move for the first turn in centimeters
move_duration_first = 1.17  # Calculated time to move forward for 35 cm

distance_to_move_second = 90  # Distance to move for the second turn in centimeters
move_duration_second = 3.00  # Calculated time to move for 90 cm

distance_to_move_third = 65  # Distance to move for the third turn in centimeters
move_duration_third = 2.17  # Calculated time to move forward for 60 cm

distance_to_move_fourth = 80  # Distance to move for the fourth turn in centimeters
move_duration_fourth = 2.67  # Calculated time to move for 80 cm

obstacle_threshold = 2  # Distance in front of the car to consider an obstacle

stop_event = threading.Event()
car_thread = None

def move_forward(duration):
    """Move the car forward for a specified duration."""
    fc.forward(speed)
    time.sleep(duration)
    fc.stop()

def avoid_obstacle():
    """Perform obstacle avoidance maneuvers."""
    fc.turn_right(speed)
    time.sleep(0.90)
    fc.stop()
    move_forward(move_duration_first)
    fc.turn_left(speed)
    time.sleep(0.92)
    fc.stop()
    move_forward(move_duration_second)
    fc.turn_left(speed)
    time.sleep(0.94)
    fc.stop()
    move_forward(move_duration_third)
    fc.turn_left(speed)
    time.sleep(1)
    fc.stop()
    move_forward(move_duration_fourth)
    time.sleep(2)

def move_forward_with_obstacle_detection(duration):
    """Move forward for a duration while detecting and avoiding obstacles."""
    start_time = time.time()
    while time.time() - start_time < duration and not stop_event.is_set():
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue
        
        tmp = scan_list[3:7]
        print(tmp)

        if any(distance < obstacle_threshold for distance in tmp):
            fc.turn_right(speed)
            time.sleep(0.2)
            fc.forward(speed)
        else:
            fc.forward(speed)
        
    fc.stop()

def run_car():
    while not stop_event.is_set():
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)

        if any(distance < obstacle_threshold for distance in tmp):
            avoid_obstacle()
            move_forward_with_obstacle_detection(5)
        else:
            fc.forward(speed)

@app.route('/')
def index():
    return render_template_string('''
        <html>
            <head>
                <title>PiCar Control</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    h1 { 
                        text-align: center; 
                        font-size: 80px; 
                        font-weight: bold; 
                    }
                    .button-container { 
                        text-align: center; 
                        margin-top: 34px; 
                    }
                    button {
                        background-color: #4CAF50; /* Green */
                        border: none;
                        color: white;
                        padding: 65px 72px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 36px;
                        margin: 4px 2px;
                        cursor: pointer;
                        border-radius: 22px;
                    }
                    .stop-button {
                        background-color: #f44336; /* Red */
                    }
                </style>
            </head>
            <body>
                <h1>PiCar Control</h1>
                <div class="button-container">
                    <form action="/start" method="post">
                        <button type="submit">Start</button>
                    </form>
                    <form action="/stop" method="post">
                        <button type="submit" class="stop-button">Stop</button>
                    </form>
                </div>
            </body>
        </html>
    ''')

@app.route('/start', methods=['POST'])
def start():
    global stop_event, car_thread
    stop_event.clear()
    car_thread = threading.Thread(target=run_car)
    car_thread.start()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    global stop_event, car_thread
    stop_event.set()
    if car_thread is not None:
        car_thread.join()
    fc.stop()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
