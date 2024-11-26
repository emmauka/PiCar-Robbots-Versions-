# mobile1_control.py
from flask import Flask, render_template, request
import manual_mob1  # Import the functions from manual_mob1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def move_forward():
    manual_mob1.move_forward()
    return render_template('index.html')  # Render index.html again after action

@app.route('/backward')
def move_backward():
    manual_mob1.move_backward()
    return render_template('index.html')  # Render index.html again after action

@app.route('/left')
def turn_left():
    manual_mob1.turn_left()
    return render_template('index.html')  # Render index.html again after action

@app.route('/right')
def turn_right():
    manual_mob1.turn_right()
    return render_template('index.html')  # Render index.html again after action

@app.route('/stop')
def stop():
    manual_mob1.stop()
    return render_template('index.html')  # Render index.html again after action

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
