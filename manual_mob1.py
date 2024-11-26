import picar_4wd as fc

def move_forward():
    print("Moving forward")
    fc.forward(100)  # Adjust speed as necessary

def move_backward():
    print("Moving backward")
    fc.backward(100)  # Adjust speed as necessary

def turn_left():
    print("Turning left")
    fc.turn_left(100)  # Adjust speed as necessary

def turn_right():
    print("Turning right")
    fc.turn_right(100)  # Adjust speed as necessary

def stop():
    print("Stopping")
    fc.stop()
