# print_pins.py

from picar_4wd.pin import Pin

def main():
    pin_instance = Pin('P0')  # Adjust to the correct pin for your setup
    print("Available pins:", pin_instance.dict())

if __name__ == "__main__":
    main()
